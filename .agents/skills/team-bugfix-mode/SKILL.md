---
name: team-bugfix-mode
description: Use (lead) for a red test, red CI, flaky test or bug with behavior already specified: triage, owners, flaky repair, stop conditions.
---

# Bugfix mode (failing test or bug, behavior unchanged)

For a red e2e/unit test, a CI red or a bug report whose expected behavior is already specified (`gesture.md`, e2e, contract). New or changed behavior, contract or screen = feature (full flow). Doubt: ask the user.

1. **Triage by the lead, no relay**: read the failing log/trace, name the owner (`front`/`back` code, `qa` test), brief **that one agent** with test, trace, suspect files, docs. `qa` first only when "code or test wrong?" is open.
2. **Skipped**: need, design, contract, `gesture.md`, `translator`, `documentalist` skeleton, parallel build.
3. **Kept**: reproduce first (the red test is the proof); fix the cause, never weaken an assertion or widen a timeout without a cause; regression test when none covered the bug; unit tests of touched code (100 %, every condition and loop); `qa` reruns **only the impacted e2e** and Sonar on touched files.
4. **Flaky tests are always repaired**: red then green on rerun, in the loop, in the CI or noticed in passing, is a bug even if this change did not cause it. `qa` fixes the cause (`e2e-run` "Flaky tests": reproduce 10x, cause, fix, prove stable locally and in the CI) with `front`/`back` if the cause is in the code; same branch when small, else its own bugfix right after. Never "known flaky", skipped, retried or quarantined to get green. The report lists each flaky test and its status.
5. **Docs**: `documentalist` only when a documented behavior, route, table, key or gotcha changes; else one line in the commit message. A recurring cause (flaky, env) becomes a gotcha.
6. **Push** through `pr-and-ci-follow`. Stop and report: same failure after two fixes, more than five rounds, infrastructure cause; a fix that changes behavior switches to the full flow (tell the user).
7. A bug found while building a feature stays in that feature's loop (step 4 or 7); bugfix mode is for a red on a merged or PR'd change with no feature in progress.

**Feature, tests red locally**: no mode switch; the failure goes to its owner in the current step's loop. Unit/coverage/Sonar (step 4): `qa` -> `front`/`back` with test, trace, report; contract wrong: both agree, write `contract.md` first, then fix. E2E (step 7): `qa` decides code or test; code -> owner with scenario, steps, expected/actual, trace; test -> `qa`; mockup not buildable or gesture wrong -> `front` -> `designer`/`gesture.md`. After each fix `qa` reruns the impacted e2e plus what the fix touches. No push and no `documentalist` until green; after two failed fixes or five rounds the lead reports to the user.

**Green locally, red in the CI** (local gate = impacted e2e only, other environment): the lead reads the failed logs, classifies, then works in bugfix mode on the open PR:
- **Not selected locally**: `graph.yaml` wrong: `qa` fixes test or sends code to the owner, `documentalist` fixes the graph entry.
- **Environment** (versions, ports, secrets, data, time zone, workers, slower runner): reproduce locally in the CI's conditions (same workers, fresh data, no cache) before changing anything; timing problems are flaky procedure, not a bigger timeout.
- **Sonar**: code owner, with the report; no exclusion without the lead's decision.
- **Infrastructure** (runner, secret, network, same failure on unrelated PRs): lead/user, never looped.
- **Flaky** (red then green, or red only in the CI): not a pass, not an infrastructure excuse; repaired as above and proven stable in the CI.


**A red CI that passes locally**: before any fix, apply `ci-parity-before-push` "Fixing a red CI without extra round trips": read the CI's real environment from its artifacts, reproduce RED locally in it, fix every occurrence of the pattern, prove red-before / green-after, push once. A test that passes both before and after the fix proves nothing.
