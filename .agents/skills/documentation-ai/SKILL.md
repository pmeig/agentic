---
name: documentation-ai
description: MANDATORY for the documentalist when documenting a project FOR AN AI (to fix a bug or add a feature fast): the docs/ai/ layout, what to extract (tree, features by layer, APIs, database schema, flows, conventions), the format to choose for each, freshness stamp and update rules.
---

# AI documentation (`docs/ai/`)

Goal: an AI that has never seen the project finds **where things are, how they connect, and what a change touches** in a few
file reads, without scanning the whole repository. Optimize for retrieval, not for prose: tables, trees, diagrams as text, exact
paths, one fact once. Human-facing docs: `documentation-human`.

## Principles

1. **Index first**: one entry file (`docs/ai/INDEX.md`, under 120 lines) that routes to everything else; an AI loads it, then only
   the file it needs.
2. **Exact paths, never descriptions alone**: every claim points at `path/to/file.ext:line` or a folder. A route without its
   handler file is useless.
3. **Derive from the code, do not invent**: use the extraction tools of `doc-code-analysis`; mark anything you could not verify
   `(unverified)`. Generated artifacts (OpenAPI from the code, schema from the database) beat hand-written copies.
4. **Text formats an LLM reads natively**: Markdown tables, fenced Mermaid (`doc-mermaid`), OpenAPI YAML (`doc-openapi-asyncapi`),
   DBML or SQL (`doc-database-schema`), JSON/YAML for lists. No images as the only source (an image can accompany the text, never replace it).
5. **Small files, stable names**: one feature or one concern per file, kebab-case, under ~300 lines; split when larger.
6. **Say what changes together**: for each feature, the files edited together (the "change set") and the tests to run.
7. **Say the traps**: invariants, generated files not to edit, naming conventions, known flaky tests, order of migrations.
8. **Stamp freshness**: front matter `updated`, `commit` (short SHA the doc was written at). A reader compares with `git log`.

## Layout

```
docs/ai/
  INDEX.md                 entry point: product in 3 lines, stack, modules, how to run/test/build, links to the files below
  structure.md             annotated tree (depth 2-3) + module table (module | purpose | language/framework | entry point | owns data?)
  features/<feature>.md    one per business feature (template below)
  api/
    openapi.yaml           REST contract (generated from code when possible)   -> doc-openapi-asyncapi
    asyncapi.yaml          events/queues/websocket, only if any
    endpoints.md           compact table: METHOD path | handler file:line | auth | tables touched | feature
  data/
    schema.dbml            tables, columns, keys, indexes, relations         -> doc-database-schema
    schema.md              ER diagram (Mermaid) + one line per table: meaning, owner feature, lifecycle
    migrations.md          order, tool, how to add one, rollback rule
  flows/<flow>.md          sequence diagrams of the critical journeys (login, payment, sync...)   -> doc-mermaid
  architecture.md          C4 context + container diagrams, deployment, boundaries     -> doc-architecture-c4-adr
  conventions.md           naming, layering, error handling, test rules, folder rules (what the project demands, with an example file each)
  commands.md              exact commands: install, run, test, lint, build, e2e, deploy (with versions and prerequisites)
  glossary.md              domain words -> code names (table, entity, class); French/English pairs when both exist
  gotchas.md               traps, generated files, flaky tests, order dependencies, known debt
  decisions/               ADRs, one per decision (`NNNN-title.md`)
```

Only create what exists in the project (no `asyncapi.yaml` without events); `INDEX.md` lists what is present.

## Feature file template (`features/<feature>.md`)

```markdown
---
feature: <name>
updated: 2026-10-17
commit: abc1234
---
# <Feature>
**What**: one sentence, the user-visible behavior.  **Why**: the business rule that matters.

## Entry points
| Layer | Path | Role |
|---|---|---|
| UI | web/src/app/pages/x/x.page.ts | screen |
| API | server/src/x/x.controller.ts:42 | POST /x |
| Service | server/src/x/x.service.ts | rules |
| Repository | server/src/x/x.repository.ts | SQL |
| Android | android/.../XScreen.kt | screen + offline queue |

## Data
Tables/collections touched, with columns used. Link to `../data/schema.md#table`.

## API
Endpoints with request/response shape (or link to `../api/openapi.yaml` operationId).

## Flow
```mermaid
sequenceDiagram ...
```

## Change set
Files normally edited together to change this feature **and every test to update, per layer**: unit tests, e2e flows/specs with numbers and twins, tour flows, test doubles, persisted stores, strings, release notes, docs.

## Rules and traps
Invariants, validations, permissions, offline behavior, i18n keys, feature flags.
```

## Procedure

1. **Scope**: whole project, one feature, or an update after a merge. Read `AGENTS.md`/`CLAUDE.md`, `README.md`, root build files.
2. **Existing docs**: if `docs/ai/` exists, read `INDEX.md`, compare its `commit` with `git log`, update only what changed
   (`git diff --stat <commit>..HEAD`), never rewrite from scratch.
3. **Extract** with `doc-code-analysis`: tree, modules, routes, schema, dependencies between modules, tests per feature.
4. **Write** in the order: `structure.md` → `data/` → `api/` → `features/` → `flows/` → `architecture.md` → `conventions.md`,
   `commands.md`, `glossary.md`, `gotchas.md` → `INDEX.md` last.
5. **Verify**: every path exists (`doc-code-analysis` link check), every Mermaid block renders (`doc-mermaid`), OpenAPI lints,
   commands were run or marked `(not run)`.
6. **Wire the agents**: add the pointer to `docs/ai/INDEX.md` in the root `AGENTS.md` (`doc-ai-context-files`) so every agent
   finds it without being told.
7. **Report**: what was created or updated, what is unverified, how stale the rest is.

## Choosing the format (technology fit)

| To show | Use | Skill |
|---|---|---|
| Folder tree, module map | annotated tree in a code fence + table | `doc-code-analysis` |
| Who calls whom, request journey | Mermaid `sequenceDiagram` | `doc-mermaid` |
| Layers, containers, deployment | Mermaid flowchart/C4-style or `architecture-beta` | `doc-mermaid`, `doc-architecture-c4-adr` |
| Tables and relations | DBML + Mermaid `erDiagram` | `doc-database-schema` |
| REST API | OpenAPI 3.x | `doc-openapi-asyncapi` |
| Events, queues, WebSocket | AsyncAPI | `doc-openapi-asyncapi` |
| States of an entity | Mermaid `stateDiagram-v2` | `doc-mermaid` |
| Decisions | ADR | `doc-architecture-c4-adr` |
| Entry point for tools | `AGENTS.md`, `llms.txt` | `doc-ai-context-files` |
| Dependencies and impact across a big codebase, queryable | knowledge graph (`graphify-out/`), complements these docs, never replaces them | `doc-graphify` |

## Keeping it true

- After each merged feature the documentalist (or the owner agent, by `SendMessage`) updates that feature file, `endpoints.md`,
  the schema and the `commit` stamp. A stale doc is worse than none: when a file cannot be verified, say so in its header.
- Prefer generation to hand-editing for API and schema; commit the generator command in `commands.md`.

## Token budget (AI documentation only)

AI docs are loaded at every task, so their size is a recurring cost. **Applies to `docs/ai/` and `AGENTS.md` only; human docs are not shortened.**
Reference result on a 590-file monorepo: the whole folder ~50k tokens, a typical task reading ~3 to 6k.

1. **One entry file with a reading budget**: `INDEX.md` (about 1k tokens) gives the reading order, the cost in tokens of each file, and the rules below ("read one feature file, never the whole folder").
2. **One fact, one place**: a route lives in `api/endpoints.md`, a table in `data/schema.*`, a feature's layers in `features/<f>.md`. Other files link to it instead of repeating it. Module files (`modules/<m>.md`) hold what is specific to the module (stack, tree, conventions, commands, traps), never a copy of the per-feature tables.
3. **Size caps**: INDEX <= 1.2k tokens; feature file <= 1.8k; module file <= 6k; any other file <= 2.5k; split above that. Contract files generated or hand-derived from code (OpenAPI, DBML) are exempt but declared "read by section only".
4. **Read big files by section**: say in INDEX to `grep -n '^## '` then Read with offset/limit; give each file stable `##` headings so a section can be found by name.
5. **Dense formats**: tables, `path:line`, short bullets; no introductions, no repeated context, no narrative; a diagram only when it adds what a table cannot (sequence, state), never one that repeats a table or a DBML `Ref`.
6. **Do not store what the code says**: no copy of source, no long enumerations that `ls`/`grep` gives faster; point at the path.
7. **Never read-heavy by accident**: flag giant or generated files (data-only migrations, lock files, build output) as "never open" in INDEX/gotchas.
8. **Measure**: tokens ~ bytes / 3.6 (`find docs/ai -type f -printf '%s %p\n'`). Report total, the largest files and the typical read path before and after any optimization; remove duplication and prose, never facts, paths or traps.

## Change set and definition of done (completeness)

- In every feature file, "Change set" names, per layer, **what to update**: server files, client files, DTOs and test doubles, persisted stores, strings in each language, tours and tutorial entries, **e2e flows/specs with their numbers and twins**, release notes, docs. A reader must not have to guess that a test exists.
- `conventions.md` ends with a **definition of done** checklist built by reading the project's own skills, `CONTRIBUTING`, CI workflows and README rules; each mandatory step quoted from its source. Writing a test or a flow is part of the change even when running it is postponed.
- When a past change is found to have skipped a step, add the step to the checklist and to the affected feature files immediately.

## Update after a development (last step of every dev)

Runs after `qa` gives the go and before the push or the PR (team flow, `AGENTS.md`):
1. `git diff <base>...HEAD --stat` then read the diff; list routes, tables, screens, keys, tours, flows touched.
2. Update the touched feature files (Change set, rules, traps), `api/endpoints.md` and the contract file, `data/schema.*` and `data/migrations.md`, `structure.md` if a folder moved, `glossary.md` for a new word, the `commit` stamp of each touched file, `INDEX.md` counts (migrations, routes) if they changed.
3. Keep the token budget (no new duplicate); re-measure if a file grew past its cap.
4. Verify paths and commands; commit docs only, on the same branch.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources of the technology skills this one routes to, update
the layout only when a better practice is confirmed, keep the project's rules, update this date, report changes in one line.
