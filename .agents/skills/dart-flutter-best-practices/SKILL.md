---
name: dart-flutter-best-practices
description: MANDATORY for any Dart or Flutter code: pages/ and core/ modules, MVVM view models, repositories, offline-first, flutter_test, Dart 3.
---

# Dart / Flutter best practices (router)

The user has no Flutter project yet: these rules transpose the team's Android/Angular conventions to Flutter
(official Flutter architecture guide: UI layer with views + view models, data layer with repositories + services).

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
