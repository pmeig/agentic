---
name: sonar-swift
description: Only when asked: Sonar setup, coverage, exclusions of a Swift module.
---

# Sonar for Swift (on request only)

Swift analysis depends on the SonarQube edition and version: confirm with `sonar-report` (`references/sonar-check.md`) that Swift is analysed; if not,
there is no Sonar check for this module (report it, keep the Xcode coverage figures).

## Properties

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`, `sonar.sources=<App>`, `sonar.tests=<App>Tests`, `sonar.test.inclusions=**/*Tests.swift`.
- Coverage: tests run with `xcodebuild test -enableCodeCoverage YES -resultBundlePath ...`; convert the result bundle to the Sonar
  generic coverage XML (`xccov view --report --json` then a converter) and set `sonar.coverageReportPaths=<file>.xml`.
  The exact property and format are to be re-checked on the Swift page of the Sonar docs at the monthly refresh.

## Out of the analysis

- Tests: `**/*Tests/**`, `**/*UITests/**`, `**/*Tests.swift` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `**/*App.swift` (entry point), `**/Models/**` value types without logic,
  `**/DTO/**`, SwiftUI previews (`*_Previews`, `#Preview`), `Package.swift`, generated code (`*.generated.swift`), asset catalogs.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/swift/
