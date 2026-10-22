---
name: android-emulator-e2e
description: qa: run Maestro e2e on local Android emulators started from a booted snapshot (Windows + Git Bash): prerequisites, snapshot creation, run.sh usage, checks, troubleshooting.
---

# Android e2e on local emulators (snapshot start)

Use when a project ships `e2e/android/run.sh` (budget does). It starts up to 4 read-only emulators from a snapshot of a booted
Android (~10 s each instead of ~60 s cold), installs the debug APK, shards the Maestro flows across them, stops everything at the end.
**Never conclude "no emulator on this PC" before checking the project `android/local.properties` (`sdk.dir`) and `~/.android/avd/`**:
the SDK, the AVD and the snapshot are usually there even when `adb`/`maestro` are not on the PATH.

## Where things are (budget, this PC)

- SDK: `D:\programs\IDE\SDK\android` (`sdk.dir` of `android/local.properties`); `emulator/emulator.exe`, `platform-tools/adb.exe`.
- AVD `honor_magic_7_pro` in `~/.android/avd/`; snapshots in `~/.android/avd/honor_magic_7_pro.avd/snapshots/`:
  `e2e-ready-host` (GPU `host`, default), `e2e-ready-swiftshader_indirect` (`E2E_GPU=swiftshader_indirect`). A snapshot only loads with
  the renderer it was made with.
- Maestro: `D:\programs\softwares\maestro\2.11.0\bin` (add it to PATH in the script call, run.sh only checks `command -v maestro`).
- Debug APK: `android/app/build/outputs/apk/debug/app-debug.apk`, built with `SERVER_URL=http://10.0.2.2:3000` (skill `android-gradle`).
- Database/API: `budget_e2e`, Vault profile `e2e`, API on `:3000` (started and stopped by run.sh through `.agents/skills/demo/scripts/demo-db.sh`).
  Needs containers `postgresql` and `vault` running (`p-bdd`/`p-vault` in older docs) (Docker lives in WSL: `wsl -e docker ps`; not in the Git Bash PATH).

## Run

```bash
cd <repo>
export PATH="$PATH:/d/programs/softwares/maestro/2.11.0/bin"
e2e/android/run.sh e2e/android/flows/{14,29,30,31,32,33,34}-*.yaml   # chosen flows
E2E_TAGS=p1 e2e/android/run.sh                                      # a tag
E2E_EMULATORS=2 e2e/android/run.sh ...                              # fewer emulators (default/max 4, lowered to free RAM/CPU)
```

Other knobs: `E2E_RESET=1` (drop and re-migrate `budget_e2e`), `E2E_GPU=swiftshader_indirect`, `E2E_ANIMATIONS=on`.
Report `e2e/android/build/report.xml` (JUnit), failures with screenshots and logs in `e2e/android/build/`, API journal `build/api.log`.
Run it in the background (`run_in_background`), it takes several minutes; list the flows with ✅/❌ from the JUnit report afterwards.

## Before launching (all of them, otherwise the run is wrong or flaky)

1. No CI run and no other local test in progress (runners share this PC): `wsl -e docker ps` shows runners, check GitHub Actions of the branch.
2. No other emulator running (`adb devices`), and stop a developer `pnpm dev` API listening on `:3000` (run.sh needs the port).
3. APK built from the current code (rebuild when Kotlin/resources changed: `android-gradle`); `p-bdd`, `p-vault` up.
4. Free RAM: ~6.3 GB per emulator.

## Snapshot

run.sh calls `ensure_snapshot`: if `snapshots/e2e-ready-<gpu>` is missing it cold-boots the AVD once (`-no-snapshot`, port 5554, no window),
waits for `sys.boot_completed`, then `adb emu avd snapshot save e2e-ready-<gpu>`. This needs **no other emulator running**. To rebuild it:
`rm -r ~/.android/avd/honor_magic_7_pro.avd/snapshots/e2e-ready-host` and run again. The snapshot keeps the app of the day it was made:
run.sh reinstalls the fresh APK with `adb install -r` on every emulator and restarts an emulator that does not keep the app alive.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `maestro is not installed` | add the Maestro `bin` to PATH |
| `API_TOKEN missing` | `API_TOKEN=` line of `android/local.properties` |
| emulator boots cold / slow | snapshot missing or made with another GPU mode; see Snapshot |
| app does not start on some flows | too many emulators for the free RAM: lower `E2E_EMULATORS` |
| port 3000 busy | stop the dev API |
| offline flows (14, 15, 26, 30) | emulators handle airplane mode natively; Redroid needs a shim (skill `redroid`) |

Last verified: 2026-10-22 (script read, snapshot files present). Update this date and the paths when the setup changes.
