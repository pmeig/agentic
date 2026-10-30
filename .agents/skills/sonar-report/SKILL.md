---
name: sonar-report
description: "qa only: unit tests with coverage, Sonar check, report, send gaps below 100 % or any issue to the code owner."
---
# Sonar report (router)
Run by `qa`: runs the unit tests with coverage, asks SonarQube, reports, routes gaps to the owner. Load only the row(s) that match the situation; never load every reference.
## Always (every use)
- Objective and rules (no exclusion tricks, read-only, no PR go before it is met): `references/objective-and-rules.md`.
## Need -> file
| Situation (what the agent is doing / which step) | Load |
|---|---|
| Running the unit tests with coverage | `references/unit-tests-coverage.md` |
| Checking Sonar is up and the language is analysed | `references/sonar-check.md` |
| Getting the URL, token, project key; reading the gate | `references/sonar-access.md` |
| A `front`/`back` asks what to exclude; Sonar properties | `references/exclusions.md` |
| Writing the Sonar report | `references/report.md` |
| Gaps below 100 % or issues: who fixes, the loop | `references/fixes-routing.md` |
