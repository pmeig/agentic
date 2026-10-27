---
name: e2e-run
description: "Whenever e2e are about to run: wait for a free machine, loop until all green, a rerun-only pass is flaky."
---
# E2E run (router)
Rules for every e2e run, local or in the CI. Load only the row(s) that match the situation; never load every reference.
## Always (every use)
- Before any local e2e run, test build, push, PR creation or CI rerun, the machine must be free: load `references/free-machine.md`.
## Need -> file
| Situation (what the agent is doing / which step) | Load |
|---|---|
| Before any run, build, push, PR or CI rerun | `references/free-machine.md` |
| Choosing which scenarios to run locally (impact graph) | `references/select-impacted.md` |
| Running the selection, a failure, fix and rerun until green | `references/run-loop.md` |
| A test passes only on rerun or only sometimes | `references/flaky.md` |
| Writing or reviewing any e2e test (all tools) | `references/test-rules.md` |
| Several platforms (Android, web, desktop...): twin suites | `references/twin-e2e.md` |
| The project has no e2e yet | `references/no-e2e.md` |
