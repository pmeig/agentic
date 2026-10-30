# Documentation for humans: readers and Diátaxis structure

## Know the reader first

| Reader | Needs | Where |
|---|---|---|
| New developer | what it is, how to run it in 10 minutes, where code lives | `README.md`, `docs/getting-started.md` |
| Contributor | conventions, branch/PR flow, tests, how to add a feature | `CONTRIBUTING.md`, `docs/contributing/` |
| Operator | deploy, config, secrets, monitoring, runbooks | `docs/operations/` |
| End user | what the app does, how to do each task | `docs/user-guide/` (screenshots allowed) |
| Decision maker | why this architecture, trade-offs | `docs/architecture.md`, `docs/decisions/` |

## Structure by need: Diátaxis

Split any larger documentation into four kinds and never mix them in one page (source: diataxis.fr):
- **Tutorials**: learning by doing, one guaranteed path, a result at the end.
- **How-to guides**: a goal, steps, no theory ("How to add a language").
- **Reference**: exact, complete, neutral, dry (config keys, endpoints, commands). Generate it when possible (`doc-openapi-asyncapi`).
- **Explanation**: why and how it fits together (architecture, trade-offs).
