---
name: redroid
description: Redroid (Android in Docker) for e2e: WSL2 prerequisites, devices, adb, networks, offline tests, GPU limits, troubleshooting.
---

# Redroid (Android in Docker)

Android runs as a Docker container sharing the host kernel: no VM, boot in about 30 s without snapshot. Used by `qa` as the
Android device of the Maestro e2e (`e2e-maestro-best-practices`, `e2e-run`, `e2e-parallelism-init`). Project scripts, when the
project has them: `e2e/android/redroid/{check-host,start,stop}.sh`.

## Host prerequisites

The kernel must provide `binder`/BinderFS and DMA-BUF heaps. Check: `grep binder /proc/filesystems` (must print `nodev binder`).
Without it the container dies ~14 s after launch (exit 129, `Binder driver could not be opened`).

- Native Linux: usually available; `modprobe binder_linux devices=binder,hwbinder,vndbinder` if built as a module.
- **WSL2**: the stock Microsoft kernel has none, so a custom kernel is needed (`CONFIG_ANDROID_BINDER_IPC=y`,
  `CONFIG_ANDROID_BINDERFS=y`, `CONFIG_ANDROID_BINDER_DEVICES="binder,hwbinder,vndbinder"`, `CONFIG_DMABUF_HEAPS=y`,
  `CONFIG_DMABUF_HEAPS_SYSTEM=y`, `CONFIG_STAGING=y`, IPv6 `ROUTER_PREF`/`ROUTE_INFO`/`MULTIPLE_TABLES`/`SUBTREES`). Ashmem and
  `CONFIG_ANDROID` no longer exist in 6.6: Redroid uses memfd (`androidboot.use_memfd=true`).
- **WSL2 gotcha, modules**: WSL loads modules from a VHD tied to Microsoft's kernel, so a custom kernel gets none. Build as `=y`
  everything Docker needs: netfilter (`NF_*`, `NFT_*`, `XT_*`, `IP_NF_*`), `BRIDGE`, `VETH`, `OVERLAY_FS`, `VXLAN`, `MACVLAN`, `TUN`,
  `DUMMY`. Otherwise `dockerd` fails with `iptables ... RULE_APPEND failed`. Do not turn every `=m` into `=y` (49 MB kernel:
  WSL refused to start, `CreateVm/ConfigureGpu`).
- **WSL2 gotcha, build**: build in a Docker container on a Docker volume, not on `/mnt/<drive>` (case collisions, 9p slowness);
  keep a `wsl` session open during long work, or the VM stops and silently kills detached containers
  (`Start-Process -WindowStyle Hidden wsl -ArgumentList '-e','sleep','7200'`); wait ~25 s after `wsl --shutdown`.
- Install: `kernel=<path with \\>` in `[wsl2]` of `%USERPROFILE%\.wslconfig` after a backup; rollback: restore the backup,
  `wsl --shutdown`. After install check `binder`, `systemctl is-active docker`, `docker run --rm hello-world`.

## Start a device

```bash
docker run -d --privileged --name rd1 redroid/redroid:14.0.0-latest \
  androidboot.use_memfd=true androidboot.redroid_gpu_mode=guest \
  androidboot.redroid_width=1080 androidboot.redroid_height=2280 androidboot.redroid_dpi=420 androidboot.redroid_fps=30
until [ "$(docker exec rd1 getprop sys.boot_completed | tr -d '\r')" = 1 ]; do sleep 2; done   # works before adb is reachable
```

- Image `redroid/redroid:14.0.0-latest` = Android 14. `--privileged` is required. One container per device, one adb serial each.
- `docker logs` ending with `No controlling tty` and a shell prompt is normal; judge by `sys.boot_completed`.
- Settings applied by the project script after boot: soft keyboard off, animations off (`window_animation_scale`,
  `transition_animation_scale`, `animator_duration_scale` = 0), `captive_portal_mode 0`.
- Count: from `e2e-parallelism-init` (ascending from 1, no ceiling), one container per shard of `maestro --shard-split`.
- Always remove with the project `stop.sh` (keeps logs, removes containers, relays and networks by label) in an `always()` step.

## GPU

Rendering is **software** (ANGLE on SwiftShader) with `auto` or `guest`. `host` needs a DRM render node (`/dev/dri/renderD128`) and
Mesa GBM: WSL2 has only `/dev/dxg`, so `host` fails (`no suitable EGLConfig found`, surfaceflinger restarts in a loop). Also,
Android's bionic Mesa GBM has no driver for NVIDIA's proprietary stack even on native Linux. Keep `auto`/`guest` on WSL2 and say
so in reports; do not claim acceleration. For GPU rendering on this PC use the Android Emulator (`-gpu host`), not Redroid.

## Networks and adb

Facts:
- The Android network of a device is **Ethernet `eth0`** of the default Docker bridge. Android airplane mode never touches it: no
  offline badge, no new network afterwards. Flows using `setAirplaneMode` therefore need a shim (below).
- The app (and `ConnectivityWatcher`) reacts to a NEW `Network` object, not to a validation toggle; after a long offline period the
  Android validation backoff delays `VALIDATED` (about 7 s after 8 s offline, about 51 s after 70 s).
- If adb travels through `eth0`, taking `eth0` down kills adb and Maestro (netd destroys the sockets of an address that leaves the
  Android network, adbd with them). **adb must use another interface.**

Layout used by `start.sh` (to copy when a project has no script):
1. Container on the default bridge (no `-p`, no `--network`): `eth0`, the network Android manages.
2. Second Docker network for adb: `docker network create <net>` and `docker network connect <net> <container>` gives `eth1`.
3. Android flushes the address of `eth\d`, so inside the container (`docker exec <c> /system/bin/sh -c ...`): `ip link set eth1 down;
   ip link set eth1 name adb0; ip addr flush dev adb0; ip addr add <cidr> dev adb0; ip link set adb0 up;
   ip route replace default dev adb0 table 200; ip rule add from <ip> lookup 200 priority 5000` (answers leave by `adb0`).
   The new name `adb0` keeps Android from managing it.
4. adb serial: in CI, the runner joins `<net>` and uses `<ip>:5555`; locally the host adb cannot reach a bridge address on
   Windows/WSL, so one `alpine/socat` relay per device publishes `127.0.0.1:<port>` -> `<ip>:5555` (`TCP-LISTEN:5555,fork,reuseaddr`).
5. `adb connect <serial>`, wait `getprop sys.boot_completed` = 1 over adb, then settings, `adb install -r`, `adb reverse tcp:<p> tcp:<p>`.

## Cut and restore the network (offline tests)

Cut = take `eth0` down; restore = bring it up: Android loses the network, then builds a NEW one (validated in about 1 s). It only
works because adb is on `adb0`.

```bash
docker exec <c> /system/bin/sh -c 'ip link set eth0 down'   # offline
docker exec <c> /system/bin/sh -c 'ip link set eth0 up'     # back online, new Network object
```

Follow airplane mode (so Maestro's `setAirplaneMode` works unchanged): `airplane-shim.sh <serial>...` pushes
`airplane-shim-loop.sh` to `/data/local/tmp` and starts it as root (`su 0 setsid nohup sh ...`); the loop polls
`settings get global airplane_mode_on` every 0.5 s and does `ip link set eth0 down` when 1, `up` when 0.

Other levers, weaker: `settings put global airplane_mode_on 1` alone does nothing on Ethernet; `iptables` DROP per uid loses
`VALIDATED` but gives no new Network; `ip link set eth0 down` without a separate adb interface kills adb.

Status (2026-10-22, measured): method above unchanged and validated. The offline flows (14, 15, 26 and 30) each passed 3
runs out of 3 on 2 devices (stable durations, no flake). A first try with only a private-DNS trick (validation lost, same Network
object) failed: the app syncs on a NEW Network and the validation backoff reached 51 s. Notes: Git Bash needs `MSYS_NO_PATHCONV=1`
for `docker exec ... /system/bin/sh`; the `ip` of Android is `/system/bin/ip`. CI: the action `pmeig/github-actions/actions/android/redroid`
must create the second Docker network, rename its interface `adb0` with the rule of step 3 and return the adb serial
`<ip on that network>:5555`, and the workflow must run `e2e/android/redroid/airplane-shim.sh <serials>`; until then the offline flows
fail in the CI. The screen is 1080x2280 (CI value): a flow written on 2400 pixels can hide a row under the bottom bar (flow 04).

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| exit 129 after ~14 s, no device | no binder in the kernel | host prerequisites |
| `dockerd` fails, iptables/nft errors | custom WSL kernel without netfilter built in | netfilter as `=y` |
| containers vanish, `uptime` shows 0 min | WSL VM stopped (no open session) | keep a `wsl` session open |
| `device 127.0.0.1:5555 not connected` right after a stop | adb connect race | wait, retry `adb connect`, check the relay |
| offline badge never shows | airplane mode on Ethernet | shim + adb on `adb0` |
| adb hangs when going offline | adb on `eth0` | second network, `adb0` |
| `no suitable EGLConfig found` | `gpu_mode=host` without DRM node | `auto`/`guest` |

## Monthly refresh

Last refreshed: 2026-10-22. At first use in a later month: re-check the Redroid docs
(https://github.com/remote-android/redroid-doc, WSL2 guide `deploy/wsl.md`, image tags, `androidboot.*` options, GPU modes),
the WSL kernel tag of the host (`uname -r`, https://github.com/microsoft/WSL2-Linux-Kernel) and whether WSL now exposes a DRM
render node for the GPU; update only internet-derived guidance, keep project facts and measures, update the date, report changes.
