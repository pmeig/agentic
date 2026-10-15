---
name: e2e-testcafe-best-practices
description: Writing, reviewing or running TestCafe e2e tests; prefer Playwright for a new suite.
---

# TestCafe e2e best practices

- For a new web suite prefer Playwright (`e2e-playwright-best-practices`); keep TestCafe for existing suites. Check the project maintenance status at the monthly refresh.
- Selectors: `Selector` on `data-testid` or accessible attributes, `withText` / `filterVisible` to narrow; never brittle CSS chains. No `t.wait()`: rely on the built-in auto-wait and smart assertions (`await t.expect(sel.visible).ok()`).
- Login once with **Roles** (`Role(...)`, `t.useRole`), data seeded through the API (`RequestLogger`/`t.request` or a hook), `fixture` per feature in `tests/<feature>/`; each test independent.
- Page-model classes per page in the feature folder; request hooks / mocks only for services you do not control.
- Parallel: `--concurrency <n>` (one browser instance per unit) with the count from `e2e-parallelism-init`; `--quarantine-mode` only to detect flaky tests, never to hide them; screenshots on fail (`--screenshots takeOnFails=true`); JUnit/JSON reporter in CI.
- TypeScript strict and ESLint (`eslint-plugin-testcafe`).

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `testcafe`).

Sources:
- https://testcafe.io/documentation/402635/guides , https://testcafe.io/documentation/402638/reference/command-line-interface , https://github.com/DevExpress/testcafe/releases
- Option names above are to be re-checked at the monthly refresh.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
