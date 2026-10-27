# Sonar report: objective and rules

`front` and `back` **write** the unit tests; `qa` **runs** them, asks SonarQube and reports. The objective is the user's rule:
coverage **100 %** (overall and new code), **0 issue** (bug, code smell), **0 vulnerability**, **0 security hotspot** left to
review, no duplication, quality gate `OK`.

## Rules

- Never reach the objective by excluding files with logic, `// NOSONAR`, lowering a threshold or editing the quality gate. A rule
  wrong for the project is the user's call: ask the lead.
- Read-only on Sonar: no issue transition, hotspot review or quality-gate edit, unless the user asks.
- No pull request go while the Sonar objective is not reached (part of the `qa` gate with the e2e).
