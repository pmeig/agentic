# E2E run: no e2e in the project

`qa` does not ask whether to add e2e: it **proposes the best technology** and builds the suite.
1. Read the stack of every module (build files, `team-dev-rules` `references/stack-selection.md`).
2. Recommend the most adequate tool **per kind of module** with short pros and cons (modules' technologies, need, hosting/CI, speed,
   maintainability), e.g. Playwright for a web front, Maestro or Espresso/XCUITest for mobile, API tests for a back end alone, one
   tool for a journey crossing modules.
3. Write options and recommendation in `.agents/docs/team/<feature>/qa.md` (or `need.md`); the lead decides.
4. Then write the e2e from `gesture.md` and, only if this PC has no entry for the tool yet, calibrate it with `e2e-parallelism-init`.

No PR go on an empty suite: zero tests is "nothing verified", not green.
