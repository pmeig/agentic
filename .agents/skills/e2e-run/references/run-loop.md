# E2E run: loop until green

Also load `references/free-machine.md` before launching and `references/select-impacted.md` to choose the scenarios.

1. Run **the selected scenarios** (every e2e tool involved; all when the selection says so) with the workers of `e2e-parallelism-init`, steps shown live (`e2e-live-progress`).
2. On a failure, decide first **whether the code or the test is wrong** (trace, screenshot, steps). Code wrong: report to its owner
   (`front` or `back`) with scenario, steps, expected and actual result, trace. Test wrong: fix the test; **never weaken an assertion**.
3. After every fix, rerun the selection (plus what the fix impacts) until all is green; only then do the push or the PR go on (the CI runs the whole suite). The deployment check runs the whole feature.
4. The same failure after two fixes: stop and report to the lead with what was tried.
