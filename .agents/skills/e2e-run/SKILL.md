---
name: e2e-run
description: Whenever e2e are about to run: wait for a free machine, loop until all green, a rerun-only pass is flaky.
---

# E2E run

Rules for every e2e run, local or in the CI.

## 1. The machine must be free

Before any local e2e run, test build, push, PR creation or CI rerun (runners and local tests share the machine):
1. Check that **no CI run is in progress** (`gh run list --status in_progress`, `--status queued`) and that **no `e2e.pid`
   exists** (project path written by the e2e runners, e.g. `android/demo/work/e2e.pid`; it holds the pid of a run in progress).
2. If one is there, **wait** (until-loop with a short sleep, never a long fixed sleep).
3. Once both are free, **wait 30 seconds and check again**; launch only if still clean, otherwise start over.
4. Your own run writes `e2e.pid` at start and removes it at the end, even on failure.

## Selecting the e2e to run (local gate)

Locally run **only the scenarios the change impacts**; once they are green the push or the PR may happen, and the CI then runs **every** e2e. This skill is self-contained: the selection input is the project's impact graph, `.agents/docs/graph.yaml`, kept by `documentalist`.
1. Changed files: `git diff --name-only <base>...HEAD` plus uncommitted files.
2. For each file, take the longest matching prefix in `paths` of the graph -> features -> their `e2e` scenario numbers. Add the scenarios created or edited in this change, and the cross-screen scenarios (`tours` key: guided tours, every-page walks) when a screen, an element id/anchor or a text changed.
3. **Run all instead** when: a file is under `shared`, no prefix matches, the graph is missing or older than the code (its `commit` stamp against `git log`), the change is a merge bringing unknown content, or you doubt. A selection is never a guess.
4. No graph: read the diff and the test names, select the same way, say it in the report and lean towards running more; ask `documentalist` to build the graph.
5. Several platforms: select by scenario number on every platform; run the reference platform first, then its twins (twin rule below).
6. A red scenario outside the selection, or a regression only the CI finds, means the graph is wrong: report it to `documentalist` to fix `graph.yaml`, and rerun with the corrected selection.
7. Report which scenarios ran and why.

## 2. Loop until green

1. Run **the selected scenarios** (every e2e tool involved; all when the selection says so) with the workers of `e2e-parallelism-init`, steps shown live (`e2e-live-progress`).
2. On a failure, decide first **whether the code or the test is wrong** (trace, screenshot, steps). Code wrong: report to its owner
   (`front` or `back`) with scenario, steps, expected and actual result, trace. Test wrong: fix the test; **never weaken an assertion**.
3. After every fix, rerun the selection (plus what the fix impacts) until all is green; only then do the push or the PR go on (the CI runs the whole suite). The deployment check runs the whole feature.
4. The same failure after two fixes: stop and report to the lead with what was tried.

## Flaky tests: fix them, never hide them

**A test that passes only on rerun, or only sometimes, is flaky, not a pass.** No automatic retries to hide it (a retry setting only detects flakiness; the run is reported flaky). `qa` fixes the cause, with the owner (`front`/`back`) when the cause is in the code:
1. **Reproduce**: rerun the single test several times (10) alone, then in parallel with the others, then under load; note the failing step and the trace/screenshot of failures only.
2. **Find the cause**, most frequent first: a fixed sleep instead of waiting for a state; a transient element (toast, snackbar, animation) the test cannot catch; shared data or order dependency between tests (one account/dataset per test); port, folder or resource conflict between workers; a race (request not finished, element not yet interactive); machine load (try fewer workers); time zone, locale or date at midnight; an external service. A real race in the application is a bug: send it to the owner.
3. **Fix the cause**: wait for the state (never a long fixed sleep), isolate the data, give each worker its own ports and outputs, assert on the final state, stabilize the clock; do not weaken the assertion or widen a timeout without a cause.
4. **Prove it**: the test passes repeatedly (the 10 alone, then the whole selection several times, then in the CI), and the result is stated in the report.
5. **Record the case** (symptom, cause, fix) for `documentalist` to add to the project's gotchas, so it is not rediscovered.
Two failed fixes on the same flaky test: report to the lead with what was tried instead of looping.

## Rules for every e2e test (all tools)

- Test user-visible behavior from `gesture.md`; one scenario per path; each test creates its own data; no dependency between tests;
  never a fixed sleep; never weaken an assertion.
- Ports, data and output folders unique per worker and different from the application defaults; secrets from Vault or the
  environment, never in the repo.
- **Several platforms, twin e2e.** When the project has e2e for different platforms (for example an Android app and a web app, or mobile, desktop and web) the suites must be **twins**: the same scenarios with the same number and name, the same business steps and expected values, and the same stable element ids (test tag, `data-testid`, accessible name). One platform is written and green first (the project's order, usually the reference client), then its twins; a scenario added, changed or removed on one platform is added, changed or removed on every other platform in the same change. A behavior one platform cannot do (airplane mode in a browser, a browser-only page) keeps the scenario and its expected result and changes only the steps, or is declared platform-only in the test and in the README. Make the CI fail when a scenario has no twin.

## No e2e in the project

`qa` does not ask whether to add e2e: it **proposes the best technology** and builds the suite.
1. Read the stack of every module (build files, "Skill selection" in `AGENTS.md`).
2. Recommend the most adequate tool **per kind of module** with short pros and cons (modules' technologies, need, hosting/CI, speed,
   maintainability), e.g. Playwright for a web front, Maestro or Espresso/XCUITest for mobile, API tests for a back end alone, one
   tool for a journey crossing modules.
3. Write options and recommendation in `.agents/docs/team/<feature>/qa.md` (or `need.md`); the lead decides.
4. Then write the e2e from `gesture.md` and calibrate the tool with `e2e-parallelism-init`.

No PR go on an empty suite: zero tests is "nothing verified", not green.
