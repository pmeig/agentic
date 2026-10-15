---
name: e2e-squish-best-practices
description: Writing, reviewing or running Squish (Qt Group) GUI e2e tests for Qt, QML, Java and desktop apps.
---

# Squish e2e best practices

- Squish is a commercial tool (Qt Group); use it for Qt/QML, Java Swing/SWT/JavaFX and native desktop apps where open-source tools reach few controls. Check the licence before adding it to CI.
- Test suites in a script language of the module (Python or JavaScript preferred) under `squish/<feature>/suite_<name>/tst_<gesture>/`; one test case per business gesture of `gesture.md`.
- **Object Map**: give the application objects stable `objectName`s (Qt) or identifying properties; keep real names in the Object Map, never recorded absolute coordinates or indexes; maintain the map in version control.
- Synchronization: `waitForObject`, `waitForObjectExists`, `waitFor(condition, timeout)` on a state; no `snooze` as a delay.
- Shared steps in `shared/scripts` (functions per screen, a page-object style); data-driven tests through `testData` files; verifications with `test.compare`, `test.verify`.
- Run headless in CI with `squishserver` and `squishrunner --testsuite ... --reportgen junit,<file>`; one `squishserver` port and one X/virtual display per worker, count from `e2e-parallelism-init`.
- Accessibility: expose accessible names/roles in the Qt app and assert them through the objects.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `squish`).

Sources:
- https://doc.qt.io/squish/ , https://www.qt.io/product/quality-assurance/squish
- Command and report options are to be re-checked on the Squish manual at the monthly refresh.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
