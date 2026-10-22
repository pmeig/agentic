---
name: e2e-parallelism-init
description: Before e2e on a PC with no parallelism entry: time the suite with 1, 2, 3... workers, record the best.
---

# E2E parallelism initialisation

Calibrate once per PC and per **e2e tool** how many tests run in parallel, and record it so every later run just reads the number.
The key is the tool, not the module: the limit is what the tool costs on this machine (browsers, emulators, devices).

## When it triggers

1. **PC id** (stable, lowercase, no spaces): `<hostname>` + first 8 characters of the machine GUID (Windows
   `(Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Cryptography').MachineGuid`; Linux/WSL `/etc/machine-id`; macOS `IOPlatformUUID`).
2. Config file: `<e2e root>/parallelism/<pc-id>.json` (e.g. `e2e/parallelism/`).
3. Calibrate when **the file does not exist** (create it) **or has no entry for the tool** about to run (add it, keep the others).
   An existing entry: read it and use it. Recalibrate only when asked or when `cpu`/`memoryGb` no longer match the machine.

## Procedure

The machine must be free (`e2e-run` rule 1) and nothing else heavy may run during the measures.
1. Take the **full e2e suite run with that tool** and its parallel option (Playwright `--workers=N`, Cypress parallel groups,
   Maestro shards / one emulator per shard...). Each worker has its own ports, data and output folders; if the suite cannot run in
   parallel as is, fix the isolation first (tests, not assertions).
2. Run with `N = 1, 2, 3, ...`; measure the **wall-clock time**, the failures, and CPU/memory peaks when cheap.
3. **Stop at the first run slower than the previous**, earlier if failures or flakes appear only under load (a run with new
   failures counts as worse), and at the number of logical CPUs or spec files, whichever is smaller.
4. **Keep the best `N`**; within 5 % of each other, the smaller. A failure unrelated to load is a real failure: report it.
5. Write the result and tell the lead: tool, chosen `N`, times, why it stopped.

## Config file

```json
{
  "pcId": "desktop-ab12cd34",
  "cpu": 16,
  "memoryGb": 32,
  "tools": {
    "playwright": {
      "workers": 4,
      "calibratedAt": "2026-10-15",
      "runs": [
        { "workers": 1, "seconds": 412, "failures": 0 },
        { "workers": 4, "seconds": 139, "failures": 0 },
        { "workers": 5, "seconds": 151, "failures": 0 }
      ],
      "reason": "Time went up from 4 to 5 workers: 4 is the optimum."
    }
  }
}
```

Keep `runs` and `reason` (they explain the choice). One file per PC, so files never overwrite each other (commit it unless the
project says otherwise). Every e2e run of the tool on this PC passes its `workers` (`--workers=<n>` or equivalent). CI runners are
PCs too: each gets its own file at its first run.
