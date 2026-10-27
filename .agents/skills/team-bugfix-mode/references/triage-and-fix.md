# Bugfix mode: triage and fix loop

For a red e2e/unit test, a CI red or a bug report whose expected behavior is already specified (`gesture.md`, e2e, contract). New or changed behavior, contract or screen = feature (full flow, skill `team-lead`). Doubt: ask the user.

1. **Triage by the lead, no relay**: read the failing log/trace, name the owner (`front`/`back` code, `qa` test), brief **that one agent** with test, trace, suspect files, docs. `qa` first only when "code or test wrong?" is open.
2. **Skipped**: need, design, contract, `gesture.md`, `translator`, `documentalist` skeleton, parallel build.
3. **Kept**: reproduce first (the red test is the proof); fix the cause, never weaken an assertion or widen a timeout without a cause; regression test when none covered the bug; unit tests of touched code (100 %, every condition and loop); `qa` reruns **only the impacted e2e** and Sonar on touched files.
4. **Flaky tests are always repaired**: red then green on rerun, in the loop, in the CI or noticed in passing, is a bug even if this change did not cause it. `qa` fixes the cause (`e2e-run`, `references/flaky.md`: reproduce 10x, cause, fix, prove stable locally and in the CI) with `front`/`back` if the cause is in the code; same branch when small, else its own bugfix right after. Never "known flaky", skipped, retried or quarantined to get green. The report lists each flaky test and its status.
5. **Docs**: `documentalist` only when a documented behavior, route, table, key or gotcha changes; else one line in the commit message. A recurring cause (flaky, env) becomes a gotcha.
6. **Push** through `pr-and-ci-follow`. Stop and report: same failure after two fixes, more than five rounds, infrastructure cause; a fix that changes behavior switches to the full flow (tell the user).
7. A bug found while building a feature stays in that feature's loop (step 4 or 7); bugfix mode is for a red on a merged or PR'd change with no feature in progress.
