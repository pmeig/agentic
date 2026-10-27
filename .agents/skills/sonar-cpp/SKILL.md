---
name: sonar-cpp
description: Only when asked: Sonar setup, coverage, exclusions of a C / C++ module.
---

# Sonar for C / C++ (on request only)

C and C++ analysis depends on the SonarQube edition: confirm with `sonar-report` (`references/sonar-check.md`) that it is available; if not, there is
no Sonar check for this module (report it, keep the local gcov/llvm-cov figures).

## Properties

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`, `sonar.sources=src,include`, `sonar.tests=tests`, `sonar.test.inclusions=tests/**`.
- Build information: `sonar.cfamily.compile-commands=build/compile_commands.json` (CMake `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON`).
- Coverage: build with `--coverage`, run the tests (GoogleTest/Catch2 through `ctest`), then `sonar.cfamily.gcov.reportsPath=<gcov dir>`
  (or the llvm-cov export in the format the docs describe).

## Out of the analysis

- Tests: `tests/**`, `**/*_test.cpp`, `**/*Test.cpp` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Third party and generated: `third_party/**`, `external/**`, `build/**`, `**/moc_*`, `**/ui_*`, `**/qrc_*` (Qt), Unreal `*.generated.h`,
  `Intermediate/**`.
- Without behavior (`sonar.coverage.exclusions`): `**/main.cpp` bootstrap, pure header-only data structs, constants headers.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/c-family/
