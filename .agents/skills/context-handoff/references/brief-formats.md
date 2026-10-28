# Context handoff: file templates and size caps

All inter-agent files live in `.agents/docs/team/<feature>/`. Machine-first: tables and compact lists, no prose.

## brief-<from>-<to>.md (max 40 lines)

~~~
## Done
- <what was produced — 1 line each, max 5 items>

## Decisions
- <key decision — 1 line, max 5 items>

## Read (in order)
1. <path> — <why, 3 words max>

## Do not read
- <path or topic>

## Tasks
- [ ] <task — 1 line>

## Done criteria
- <criterion — 1 line>
~~~

Never paste file content; always use a path. Section budgets: Done 5, Decisions 5, Read 10, Tasks 10, Done criteria 5.

## gesture.md (max 2 KB)

Written by `front`, read by `qa`. Machine-first tables; no prose.

~~~
# gesture: <feature>

## Steps
| # | Action (user view) | Data / rule implied | Expected result | Test id |
|---|-------------------|---------------------|-----------------|---------|
| 1 | <what the user does> | <data or rule> | <visible result> | <stable-id> |

## Edge cases
| Case | Expected |
|------|----------|
| <edge case> | <result> |

## Offline / permissions
- <rule — omit section if not applicable>
~~~

## qa.md — test plan (max 2 KB)

Written by `qa`. Machine-first table.

~~~
# qa plan: <feature>

| Scenario | Path | Gesture step(s) | Expected |
|----------|------|-----------------|----------|
| happy path | — | all | success state |
| <rule name> | rule | <step numbers> | <result> |
| <error name> | error | <step number> | <error shown> |
| <edge case> | edge | <step number> | <result> |
~~~

## brief-<dev>-documentalist.md (max 20 lines)

One file per dev (`front`, `back`). `documentalist` reads both and merges them.

~~~
## Changed
- <file or module path>: <what changed — 1 line>

## Routes (back only)
- <METHOD /path>: <purpose>

## Schemas / migrations (back only)
- <table or migration name>: <change>

## Translation keys (front only)
- <key>: <screen, sentence type>

## E2E flows
- <scenario name>: <gesture steps covered>
~~~

## contract.md (max 3 KB)

Co-written by `front` and `back`; each author writes only their own section.

~~~
# contract: <feature>

## Endpoints
| Method | Path | Auth | Request body | Response body | Errors |
|--------|------|------|--------------|---------------|--------|
| POST | /api/... | bearer | {field: type} | {field: type} | 400, 404 |

## Events / messages (async only)
| Topic | Direction | Schema |
|-------|-----------|--------|

## Pagination
- strategy: cursor | offset   max: <n>

## Offline / idempotency
- <rule — omit if not applicable>

## Versioning
- <rule — omit if not applicable>
~~~
