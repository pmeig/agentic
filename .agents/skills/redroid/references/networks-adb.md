# Redroid: networks and adb

Facts:
- The Android network of a device is **Ethernet `eth0`** of the default Docker bridge. Android airplane mode never touches it: no
  offline badge, no new network afterwards. Flows using `setAirplaneMode` therefore need a shim (`references/offline-tests.md`).
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
