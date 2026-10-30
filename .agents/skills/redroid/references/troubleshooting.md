# Redroid: troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| exit 129 after ~14 s, no device | no binder in the kernel | host prerequisites (`references/prerequisites.md`) |
| `dockerd` fails, iptables/nft errors | custom WSL kernel without netfilter built in | netfilter as `=y` (`references/prerequisites.md`) |
| containers vanish, `uptime` shows 0 min | WSL VM stopped (no open session) | keep a `wsl` session open |
| `device 127.0.0.1:5555 not connected` right after a stop | adb connect race | wait, retry `adb connect`, check the relay |
| offline badge never shows | airplane mode on Ethernet | shim + adb on `adb0` (`references/offline-tests.md`, `references/networks-adb.md`) |
| adb hangs when going offline | adb on `eth0` | second network, `adb0` (`references/networks-adb.md`) |
| `no suitable EGLConfig found` | `gpu_mode=host` without DRM node | `auto`/`guest` (`references/gpu.md`) |
