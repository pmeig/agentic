---
name: e2e-playwright-best-practices
description: Writing, reviewing or running Playwright e2e tests (web, Electron, API).
---

# Playwright e2e best practices

- Test user-visible behavior, not implementation; each test isolated (own browser context, own data); do not test third-party services, mock them.
- Locators: `getByRole`, `getByLabel`, `getByText`, `getByTestId` (configure `testIdAttribute`); chain and filter to narrow; no XPath or deep CSS. Use `codegen` to find them.
- Web-first assertions only (`await expect(locator).toBeVisible()`), never a manual assertion on a value read earlier; never `waitForTimeout`. `expect.soft` to keep going after a non-blocking failure.
- Fixtures (`test.extend`) for login state (`storageState` produced once in a setup project), data and page objects; one folder per feature in `tests/<feature>/`, specs in a `spec/` folder when there are several.
- Config: `baseURL`, `webServer` with readiness URL, `fullyParallel: true`, `workers` from `e2e-parallelism-init`, `retries: 0` locally (retries only to detect flakiness in CI), `trace: 'on-first-retry'`, `forbidOnly` in CI, projects for chromium, firefox and webkit, HTML + JUnit reporters.
- CI: install only the needed browsers (`npx playwright install --with-deps chromium`), shard with `--shard=i/n` and merge reports (`merge-reports`), upload traces; debug with the trace viewer, not videos.
- Accessibility: axe checks per page (see `e2e-accessibility-best-practices`). Use the `request` fixture for API set-up.
- TypeScript strict + ESLint (`no-floating-promises`); keep `@playwright/test` up to date.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `playwright`).

Sources:
- https://playwright.dev/docs/best-practices
- https://playwright.dev/docs/test-parallel , https://playwright.dev/docs/test-sharding , https://playwright.dev/docs/release-notes

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
