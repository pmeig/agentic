---
name: e2e-espresso-compose-best-practices
description: Writing, reviewing or running Android Espresso and Jetpack Compose UI tests.
---

# Android Espresso and Compose UI test best practices

- Compose: `createAndroidComposeRule`, `Modifier.testTag`, semantics finders (`onNodeWithText`, `onNodeWithContentDescription`), `waitUntil` on a state. Views: Espresso `onView` with ids and text. Both synchronize automatically; register an `IdlingResource` for custom async work, never `Thread.sleep`.
- Hermetic: fake or MockWebServer back end, in-memory or test database, Hilt `@TestInstallIn` to swap modules, fixed clock and locale; journeys against the real back end belong to the e2e tool of the whole product.
- `AndroidJUnitRunner` with the **Android Test Orchestrator** (`clearPackageData`) so every test starts from a clean app; `ActivityScenario` or the compose rule per test.
- One robot / screen-object class per screen; one test class per gesture in `androidTest/<feature>/`; tests share nothing.
- Run on Gradle Managed Devices (`./gradlew <device>DebugAndroidTest`) or Firebase Test Lab; shard with the instrumentation arguments `numShards` / `shardIndex`. Gradle runs with the JDK of `java-version`; commands per `android-tooling`.
- Accessibility: Espresso `AccessibilityChecks.enable()`, Compose semantics checks.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `espresso`).

Sources:
- https://developer.android.com/training/testing/espresso , https://developer.android.com/develop/ui/compose/testing
- https://developer.android.com/studio/test/gradle-managed-devices

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
