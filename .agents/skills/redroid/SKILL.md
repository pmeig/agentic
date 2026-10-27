---
name: redroid
description: "Redroid (Android in Docker) for e2e: WSL2 prerequisites, devices, adb, networks, offline tests, GPU limits, troubleshooting."
---
# Redroid (router)
Android in Docker, the Android device of the `qa` Maestro e2e. Load only the row(s) that match the situation; never load every reference.
## Need -> file
| Situation (what the agent is doing / which step) | Load |
|---|---|
| Checking the host kernel (binder), WSL2 custom kernel | `references/prerequisites.md` |
| Starting or stopping a device, image, settings, count | `references/start-device.md` |
| adb connection, second network, `adb0`, relay | `references/networks-adb.md` |
| Offline / airplane mode flows, network cut and restore | `references/offline-tests.md` |
| GPU rendering questions | `references/gpu.md` |
| Something fails (exit 129, adb, EGL, dockerd) | `references/troubleshooting.md` |
| Monthly refresh, sources | `references/maintenance.md` |
