---
name: e2e-run
description: Whenever e2e tests are about to run (before push or PR, after merging develop or deploying): wait for a free machine, loop until every e2e is green, treat a rerun-only pass as flaky.
---

# E2E run

Rules for every e2e run, local or against a deployed environment, with or without the user's global skills (`feature-e2e-loop`,
`flaky-tests`; follow them too when loaded).

## 1. The machine must be free

Before any local e2e run, test build, push, PR creation or CI rerun (runners and local tests share the machine):
1. Check that **no CI run is in progress** (`gh run list --status in_progress`, `--status queued`) and that **no `e2e.pid`
   exists** (project path written by the e2e runners, e.g. `android/demo/work/e2e.pid`; it holds the pid of a run in progress).
2. If one is there, **wait** (until-loop with a short sleep, never a long fixed sleep).
3. Once both are free, **wait 30 seconds and check again**; launch only if still clean, otherwise start over.
4. Your own run writes `e2e.pid` at start and removes it at the end, even on failure.

## 2. Loop until green

1. Run **the whole suite** (every e2e tool) with the workers of `e2e-parallelism-init`, steps shown live (`e2e-live-progress`).
2. On a failure, decide first **whether the code or the test is wrong** (trace, screenshot, steps). Code wrong: report to its owner
   (`front` or `back`) with scenario, steps, expected and actual result, trace. Test wrong: fix the test; **never weaken an assertion**.
3. After every fix, rerun the **whole suite** until all is green; only then do the push, the PR or the deployment check go on.
4. The same failure after two fixes: stop and report to the lead with what was tried.

**A test that passes only on rerun is flaky, not a pass.** No automatic retries to hide it (a retry setting only detects
flakiness and the run is reported flaky). Find the cause (fixed sleep instead of a state, shared data or order dependency, port or
resource conflict between workers, machine load: try fewer workers, time or locale) and fix it; add the case to `flaky-tests`
when available.

## Rules for every e2e test (all tools)

- Test user-visible behavior from `gesture.md`; one scenario per path; each test creates its own data; no dependency between tests;
  never a fixed sleep; never weaken an assertion.
- Ports, data and output folders unique per worker and different from the application defaults; secrets from Vault or the
  environment, never in the repo.

## No e2e in the project

`qa` does not ask whether to add e2e: it **proposes the best technology** and builds the suite.
1. Read the stack of every module (build files, "Skill selection" in `AGENTS.md`).
2. Recommend the most adequate tool **per kind of module** with short pros and cons (modules' technologies, need, hosting/CI, speed,
   maintainability), e.g. Playwright for a web front, Maestro or Espresso/XCUITest for mobile, API tests for a back end alone, one
   tool for a journey crossing modules.
3. Write options and recommendation in `docs/team/<feature>/qa.md` (or `need.md`); the lead decides.
4. Then write the e2e from `gesture.md` and calibrate the tool with `e2e-parallelism-init`.

No PR go on an empty suite: zero tests is "nothing verified", not green.
