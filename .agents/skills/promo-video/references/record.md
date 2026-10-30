# Promotional video: record

## 2. Record the real app

- **Web**: Playwright with `recordVideo` (size 1280x720 or the target viewport) or scripted screenshots; drive the flow by script
  so the take is repeatable (`e2e-playwright-best-practices`); slow the pointer, hide devtools, fixed window size.
- **Android**: emulator with `adb shell screenrecord` or `scrcpy --record`, touches visible (`adb shell settings put system show_touches 1`),
  a script or a Maestro flow to drive it (`e2e-maestro-best-practices`), animations on, demo mode in the status bar
  (`adb shell cmd statusbar demo` or the System UI demo mode).
- **iOS**: `xcrun simctl io booted recordVideo`, status bar override with `xcrun simctl status_bar booted override`.
- Several short takes beat one long one; record at 60 fps when possible and at the target resolution (portrait for 9:16).
- Ask `front` for the demo account, data and the exact flow; ask `qa` for a stable environment.
