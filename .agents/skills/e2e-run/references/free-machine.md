# E2E run: the machine must be free

Rules for every e2e run, local or in the CI.

Before any local e2e run, test build, push, PR creation or CI rerun (runners and local tests share the machine):
1. Check that **no CI run is in progress** (`gh run list --status in_progress`, `--status queued`) and that **no `e2e.pid`
   exists** (project path written by the e2e runners, e.g. `android/demo/work/e2e.pid`; it holds the pid of a run in progress).
2. If one is there, **wait** (until-loop with a short sleep, never a long fixed sleep).
3. Once both are free, **wait 30 seconds and check again**; launch only if still clean, otherwise start over.
4. Your own run writes `e2e.pid` at start and removes it at the end, even on failure.
