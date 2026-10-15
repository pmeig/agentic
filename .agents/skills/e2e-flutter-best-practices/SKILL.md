---
name: e2e-flutter-best-practices
description: Writing, reviewing or running Flutter integration tests (integration_test, Patrol).
---

# Flutter e2e (integration_test) best practices

- `integration_test` package with `IntegrationTestWidgetsFlutterBinding`; tests in `integration_test/<feature>/`; `flutter test integration_test -d <device-id>` (or `flutter drive` for web).
- Find widgets by `Key('...')` or semantics labels, then text; wait with `pumpAndSettle` or a `pumpUntilFound` helper, no fixed delays.
- Fake or local back end injected through the app dependency container or flavors; clean app state per test; fixed clock and locale.
- Native dialogs (permissions, notifications, webviews) need **Patrol** (`patrol test`); keep it for the cases that need it.
- One page-object class per screen; one emulator or simulator per worker, count from `e2e-parallelism-init`; Firebase Test Lab or similar for real devices.
- Widget tests stay in the `front` unit tests; integration tests cover the gestures of `gesture.md`.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `flutter`).

Sources:
- https://docs.flutter.dev/testing/integration-tests , https://docs.flutter.dev/testing/overview , https://patrol.leancode.co/

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
