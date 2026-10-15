---
name: e2e-selenium-best-practices
description: Writing, reviewing or running Selenium WebDriver e2e tests.
---

# Selenium WebDriver e2e best practices

- Selenium 4+: Selenium Manager downloads the drivers, no manual driver binaries. Relative locators and BiDi only when they remove a fragile workaround.
- Locators: id, `data-testid`, accessible name, then short CSS; avoid XPath chains and index-based lookups.
- **Explicit waits** (`WebDriverWait` + `ExpectedConditions`) on a state; never `Thread.sleep`; do not mix implicit and explicit waits (implicit stays 0).
- One Page Object per page or component (locators and actions inside, assertions in the test), kept in the page feature folder.
- A fresh browser session per test (or per worker with a clean profile), always `quit()` in teardown; no shared state or order dependency.
- Parallel with the test runner (JUnit 5 parallel execution, pytest-xdist, NUnit) at the count of `e2e-parallelism-init`, one `WebDriver` per thread (`ThreadLocal`); scale with Selenium Grid (standalone, hub/node or Docker) for more browsers.
- Headless in CI, screenshot and page source on failure, JUnit XML report. Language rules: the matching language skill.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `selenium`).

Sources:
- https://www.selenium.dev/documentation/test_practices/
- https://www.selenium.dev/documentation/webdriver/waits/ , https://www.selenium.dev/documentation/grid/ , https://www.selenium.dev/blog/

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
