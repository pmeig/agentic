---
name: e2e-puppeteer-best-practices
description: Writing or running Puppeteer e2e tests or browser automation; prefer Playwright for a new suite.
---

# Puppeteer e2e best practices

- For a new e2e suite prefer Playwright (`e2e-playwright-best-practices`); keep Puppeteer for existing suites or Chrome-specific automation (PDF, performance traces).
- Use `page.locator()` (auto-waiting) with ARIA or `data-testid` selectors; wait on a state (`locator.wait()`, `waitForResponse`), never `waitForTimeout`.
- A new `BrowserContext` per test, always close the browser in `finally`/teardown; headless in CI with the sandbox flags the image needs.
- Runner: Jest, Vitest or Mocha with a setup file; screenshot and HTML on failure; unique ports per worker.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `puppeteer`).

Sources:
- https://pptr.dev/guides/ , https://pptr.dev/supported-browsers , https://github.com/puppeteer/puppeteer/releases

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
