---
name: e2e-detox-best-practices
description: Writing, reviewing or running Detox e2e tests for React Native.
---

# Detox e2e best practices

- Gray box: Detox synchronizes with network, timers and animations itself, so no sleeps. When the app has a never-idle loop, disable only that synchronization (`device.disableSynchronization()`) for the shortest scope.
- Select with `by.id` (`testID`), then `by.label` / `by.text`; `waitFor(...).toBeVisible().withTimeout(...)` on a state.
- Start clean: `device.launchApp({ newInstance: true, delete: true })` or `reloadReactNative()`, permissions set explicitly; seed data through the API.
- `.detoxrc.js` with an app and a device per platform and configuration (debug local, release CI); Jest as runner, specs in `e2e/<feature>/`; `--workers <n>` (one simulator or emulator per worker) from `e2e-parallelism-init`; `--record-logs failing --take-screenshots failing` in CI.
- Build the app once per CI run and cache it; keep Detox, React Native and the Jest preset aligned.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `detox`).

Sources:
- https://wix.github.io/Detox/docs/introduction/getting-started , https://github.com/wix/Detox/releases

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
