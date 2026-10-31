# E2E run: loop until green

Also load `references/free-machine.md` before launching and `references/select-impacted.md` to choose the scenarios.

1. Run **the selected scenarios** (every e2e tool involved; all when the selection says so) with the workers of `e2e-parallelism-init`, steps shown live (`e2e-live-progress`).
2. On a failure, diagnose before any change. Open the screenshot, the view hierarchy and the log of the failed step (in CI: download the artifacts); for a flow that passes elsewhere, open the same step there. Write two lines: what you see (and how it differs from the passing step), then the root cause. No cause, no fix.
   - Fix the cause everywhere it applies (every flow or screen with the same pattern), so one push is enough. Never a guess: blind swipe, fixed pause, extra retry.
   - Code wrong: report to its owner (`front` or `back`) with scenario, steps, expected and actual result, the two lines. Test wrong: fix the test; **never weaken an assertion**.
3. When an e2e is red (locally or in CI), rerun locally only the flows/tests that failed. If the fix changes application code (not just the test), rerun every flow that concerns the fixed code. Never replay the whole suite for a red; CI runs the full suite on push anyway. Repeat until all is green; only then do the push or the PR go on. The deployment check runs the whole feature.
4. The same failure after two fixes: stop and report to the lead with what was tried.
