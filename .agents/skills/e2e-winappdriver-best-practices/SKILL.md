---
name: e2e-winappdriver-best-practices
description: Writing, reviewing or running Windows desktop UI tests (WinAppDriver, Appium Windows driver).
---

# Windows desktop UI test best practices (WinAppDriver / Appium Windows driver)

- WinAppDriver is no longer actively developed: for a new suite use **Appium with the Windows driver** (`appium-windows-driver`, see `e2e-appium-best-practices`), which keeps the same WebDriver API; keep WinAppDriver only for existing suites. Check the status at the monthly refresh.
- Locators: `AutomationId` first (set `AutomationProperties.AutomationId` in XAML/WinForms `AccessibleName`), then `Name`, `ClassName`; XPath last. Accessibility names double as WCAG names.
- Launch the app per test with its `app` capability (path or AUMID), `deviceName: WindowsPC`; close it in teardown; start from a clean profile or data folder.
- Explicit waits on a state (`WebDriverWait`), no sleeps; for several top-level windows switch with `window_handles`.
- One page-object class per window or dialog in the feature folder; the client language follows the module (C#, Java, Python, JS: language skill applies).
- Windows needs an interactive desktop session (no locked screen, Developer Mode on); one session per machine in practice, so parallelism comes from several machines or VMs, count from `e2e-parallelism-init` (usually 1 per desktop).
- Screenshot on failure, JUnit/TRX report in CI.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `winappdriver`).

Sources:
- https://github.com/microsoft/WinAppDriver , https://github.com/appium/appium-windows-driver , https://appium.io/docs/en/latest/

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
