---
name: e2e-webdriverio-best-practices
description: Writing, reviewing or running WebdriverIO e2e tests (web, mobile via Appium).
---

# WebdriverIO e2e best practices

- Selectors: aria labels, `data-testid`, ids; never classes. Prefer one CSS selector over chained `$`/`$$` calls and list indexing.
- Use the built-in retrying assertions (`await expect(el).toBeDisplayed()`); do not wait for existence or display when an interaction or assertion already does; replace `browser.pause()` by `waitForEnabled`/`waitUntil`.
- Async hygiene: `for...of` instead of `forEach`, `Promise.all` for independent operations, ESLint with the WebdriverIO rules.
- Dynamic data and credentials from environment variables (Vault), never hardcoded.
- Page objects per page in the feature folder; `specs` and `suites` by feature; `maxInstances` set to the count of `e2e-parallelism-init`; `retries` only to detect flakiness.
- Mobile: same API on top of Appium (see `e2e-appium-best-practices`).

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `webdriverio`).

Sources:
- https://webdriver.io/docs/bestpractices
- https://webdriver.io/docs/configuration , https://webdriver.io/blog

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
