# Redroid: host prerequisites

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
