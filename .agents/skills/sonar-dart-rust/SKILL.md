---
name: sonar-dart-rust
description: "Only when asked: Sonar setup, coverage, exclusions of a Dart/Flutter or Rust module."
---

# Sonar for Dart / Flutter and Rust (on request only)

These languages are not analysed by every SonarQube: Dart needs a community plugin, Rust depends on the version. Confirm with
`sonar-report` (`references/sonar-check.md`) (language list of the server); **if the language is not listed there is no Sonar check** for the module:
report it, keep the local coverage figures and the linter (`flutter analyze` / `dart analyze`, `cargo clippy`).

## When the language is analysed

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`.
- Coverage can be imported in the **generic** format with `sonar.coverageReportPaths=<file>.xml` or the plugin's lcov property
  (check the plugin or docs page at the refresh).
- Dart / Flutter: `sonar.sources=lib`, `sonar.tests=test`, `sonar.test.inclusions=test/**/*_test.dart`; `flutter test --coverage`
  produces `coverage/lcov.info`.
- Rust: `sonar.sources=src`, `sonar.tests=tests`; coverage from `cargo llvm-cov --lcov --output-path lcov.info` (or tarpaulin), converted
  or imported as the Sonar docs say.

## Out of the analysis

- Tests: `test/**`, `integration_test/**`, `tests/**`, `**/*_test.dart` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior: Dart `**/main.dart`, `**/*.g.dart`, `**/*.freezed.dart`, `**/l10n/**`, `**/models/**` of pure data, themes;
  Rust `src/main.rs` bootstrap, `build.rs`, generated code, pure data structs.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/ , https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/generic-test-data/
