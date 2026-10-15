---
name: e2e-xcuitest-best-practices
description: Writing, reviewing or running iOS/macOS XCUITest UI tests.
---

# XCUITest e2e best practices

- Accessibility identifiers (`.accessibilityIdentifier`) on every element a test touches; query by identifier, then label; no coordinates.
- Wait on a state (`waitForExistence(timeout:)`, `XCTNSPredicateExpectation`), never `sleep`; fail with a clear message.
- Launch the app per test with `launchArguments` / `launchEnvironment` to select a fake or local back end and a clean state; reset permissions and data in `setUp`; `continueAfterFailure = false`.
- One page-object struct per screen in `UITests/<Feature>/`.
- Test plans (`.xctestplan`) define suites and configurations (locale, dark mode, Dynamic Type) and parallelization; `xcodebuild test -parallel-testing-enabled YES -parallel-testing-worker-count <n>` with the count from `e2e-parallelism-init`; keep the result bundle (`-resultBundlePath`) and screenshots as CI artifacts.
- Use `performAccessibilityAudit()` on key screens.
- XCUITest runs only on macOS runners; use Maestro or Appium when the suite must run on another OS.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `xcuitest`).

Sources:
- https://developer.apple.com/documentation/xctest/user_interface_tests
- https://developer.apple.com/documentation/xcode/running-tests-and-viewing-results

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
