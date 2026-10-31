---
name: sonar-go
description: "Only when asked: Sonar setup, coverage, exclusions of a Go module."
---

# Sonar for Go (on request only)

## Properties

- `sonar.projectKey`, `sonar.sourceEncoding=UTF-8`, `sonar.sources=.`, `sonar.tests=.`, `sonar.test.inclusions=**/*_test.go`,
  `sonar.exclusions=**/vendor/**`.
- Coverage: `go test -coverprofile=coverage.out ./...` then `sonar.go.coverage.reportPaths=coverage.out`; test report optional with
  `go test -json ./... > report.json` and `sonar.go.tests.reportPaths=report.json`.

## Out of the analysis

- Tests: `**/*_test.go` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `**/main.go` (bootstrap), generated code (`**/*.pb.go`, `**/mock_*.go`, `**/*_gen.go`),
  files holding only struct / type declarations (`**/model/**`, `**/dto/**`, `**/entity/**`), `**/migrations/**`, `**/cmd/**` wiring.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/go/ ,
https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/go-test-coverage/
