# Redroid: cut and restore the network (offline tests)

Also load `references/networks-adb.md` (adb must be on `adb0`, step 3 of the layout).

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
