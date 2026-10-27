# AI documentation: feature file (`features/<f>.md`)

## Feature file template
```markdown
---
feature: <name>
updated: YYYY-MM-DD
commit: abc1234
---
# <Feature>
**What**: user-visible behavior. **Why**: the rule that matters.
## Entry points
| Layer | Path | Role |   (UI, API route:line, service, repository, client app, offline queue...)
## Data
Tables touched with columns used; link `../data/schema.md`.
## API
Routes with shapes, or the openapi operationId.
## Flow
`client -> route -> service -> repository -> table` + offline and error branches
## Change set
Files edited together **and every test to update, per layer**: unit tests, e2e scenarios with numbers and their twins on every platform, tour flows, test doubles, persisted stores, strings in each language, release notes, docs.
## Rules and traps
Invariants, validations, permissions, offline behavior, i18n keys, flags.
```
