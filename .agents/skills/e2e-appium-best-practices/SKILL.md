---
name: e2e-appium-best-practices
description: Writing, reviewing or running Appium e2e tests (Android, iOS, desktop).
---

# Appium e2e best practices

- Appium 2+: install only the needed drivers and plugins (`appium driver install uiautomator2` or `xcuitest`); pin their versions; run `appium driver doctor` in CI.
- Capabilities in one config per platform; `appium:noReset` / `appium:fullReset` chosen on purpose, fresh app state per test; `appium:newCommandTimeout` set.
- Locators: accessibility id first, then id / resource-id, iOS predicate string or class chain, Android UiSelector; XPath is the last resort (slow).
- Explicit waits on a state, no sleeps, no implicit waits. One page object per screen in the feature folder; client in WebdriverIO, Java, Python or another (language skill applies).
- Parallel: one device, emulator or simulator per worker with its own `udid`, `systemPort` and `wdaLocalPort`, count from `e2e-parallelism-init`; device farms (BrowserStack, Sauce Labs, AWS Device Farm) for real devices.
- Prefer a faster native tool for a single platform (Espresso, XCUITest, Maestro) when cross-platform is not a goal.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `appium`).

Sources:
- https://appium.io/docs/en/latest/ , https://appium.io/docs/en/latest/guides/ , https://github.com/appium/appium/releases

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
