---
name: documentation-ai
description: MANDATORY for the documentalist writing docs FOR AN AI: .agents/docs/ layout, impact graph, machine-first formats, token budget, end-of-development update.
---

# AI documentation (`.agents/docs/`, same path in every project)

Goal: an AI that has never seen the project finds **where things are, how they connect, what a change touches and which tests to run** in a few reads. Optimize retrieval, not prose. Human docs: `documentation-human`.

## Principles
1. **All AI-facing documents are in English** (skill `ai-docs-in-english`), whatever the user's or the product's language (`.agents/docs/`, `AGENTS.md`, `.agents/docs/team/`, skills, memory, prompts). Domain words keep their original spelling next to the English name (glossary).
1b. **Location: `<project>/.agents/docs/`** in every project (same path for all agents and projects; team workspace in `.agents/docs/team/<feature>/`). Never `docs/ai`.
2. **Machine-first formats; human readability is irrelevant**: YAML/JSON maps, edge lists (`a -> b`, `a = b`), dense tables, `path:line`. No Mermaid, ASCII art, diagrams, prose or layout for the eye (Mermaid stays in human docs). Contracts keep their native format (OpenAPI, AsyncAPI, DBML, SQL).
3. **Index first**: `INDEX.md` routes to everything else; an AI loads it, then only what it needs.
4. **Exact paths**: every claim points at `path:line` or a folder; a route without its handler is useless.
5. **Derive from the code**; mark `(unverified)`; generated artifacts beat hand-written copies (`doc-code-analysis`).
6. **Small files, stable `##` headings**, one concern per file, kebab-case; split when large.
7. **Say what changes together** (change set), the tests to run, the traps (invariants, generated files, flaky tests, migration order).
8. **Stamp freshness**: front matter `updated`, `commit` (short SHA); a reader compares with `git log`.

## Layout (create only what exists)
```
.agents/docs/
  INDEX.md          product in 3 lines, stack, modules, reading budget with cost per file, first moves per task, names of the skills that run/connect
  graph.yaml        IMPACT GRAPH (required, below)
  structure.md      annotated tree (depth 2-3) + module table (module | purpose | stack | entry point | owns data)
  features/<f>.md  template below
  api/              openapi.yaml (generated when possible), asyncapi.yaml if events, endpoints.md (METHOD path | handler:line | auth | tables | feature)
  data/             schema.dbml, schema.md (relations as edge lists FK + logical, one line per table), migrations.md (tool, how to add one, rollback rule)
  architecture.md   context + containers + deployment as edge lists
  conventions.md    naming, layering, errors, test and folder rules, workflow, **definition of done**
  glossary.md       domain word -> code name
  gotchas.md        traps, generated files, flaky tests, order dependencies, never-open files
  decisions/        ADRs (NNNN-title.md)
```
No `commands.md`: how to run/connect is a skill (`run-and-access-skills`); INDEX only names it.

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

## Impact graph (`graph.yaml`, required)
One YAML (~2k tokens for a mid-size monorepo) so the AI knows what a change touches:
- `roots`: aliases for long prefixes. `shared`: paths whose change can break any scenario (app shell, HTTP client, auth, DB layer, test ids, proxy, compose): a hit means "run all".
- `paths`: prefix -> feature ids (longest prefix wins; shared widgets list every feature using them). `tours`: cross-screen scenarios to run when a screen, an id/anchor or a string changes.
- `features.<id>`: `routes`, `tables`, `unit` (test folders), `e2e` (scenario numbers), `note`. `e2e`: scenario number -> features.
- Header comment = usage. **It defines the local gate**: only the selected scenarios run locally before a push or PR (`qa`, `e2e-run`), the CI runs all. Never a guess: shared path, no matching prefix, stale graph (`commit` older than the code) or doubt = run all. A red outside the selection, or a regression only the CI finds, means the graph is wrong: fix it the same day.
- Build from imports/call chains, controllers, repositories/migrations, test contents; verify every prefix exists (script); in the end-of-development update add new prefixes, routes, tables, scenarios.

## Token budget (AI docs only; human docs are not shortened)
Reference: a 590-file monorepo, whole folder ~50k tokens, a typical task reads 3-6k.
1. `INDEX.md` (<= 1.2k tokens) gives the reading order, the cost of each file and the rule "one feature file, never the whole folder".
2. **One fact, one place** (a route in `endpoints.md`, a table in `data/schema.*`, a feature's layers in `features/<f>.md`); other files link. Module files hold only module specifics, never the per-feature tables.
3. Caps: feature <= 1.8k tokens, module <= 6k, other <= 2.5k; contract files (OpenAPI, DBML) exempt but "read by section only".
4. Big files by section: `grep -n '^## '` then Read with offset/limit. Flag giant or generated files (data-only migrations, lock files, build output) as "never open".
5. Dense: tables, paths, short bullets; no introductions, repeated context or narrative; no copy of source or long lists that `ls`/`grep` gives.
6. Measure: tokens ~ bytes / 3.6; report total, largest files and typical read path before and after. Remove duplication and prose, never facts, paths or traps.

## Definition of done and completeness
- `conventions.md` ends with a checklist built from the project's own skills, CONTRIBUTING, CI workflows and README, each step quoted from its source. Writing a test or flow is part of the change even when running it is postponed.
- A step found skipped in a past change is added to the checklist and the affected feature files at once.

## Procedure
1. Scope (project, feature, update); read `AGENTS.md`/`CLAUDE.md`, README, build files. If `.agents/docs/` exists compare its `commit` with `git log` and update only the diff, never rewrite.
2. Extract (`doc-code-analysis`); write in order: structure, data, api, features, `graph.yaml`, flows, architecture, conventions, glossary, gotchas, INDEX last.
3. Verify: paths exist, OpenAPI lints, commands run or `(not run)`; wire the pointer in the root `AGENTS.md` (`doc-ai-context-files`); report created, unverified, stale.

## Format choice
tree -> annotated tree + table · impact -> `graph.yaml` · journey -> one-line chain · architecture -> edge list · tables -> DBML + edge list · REST -> OpenAPI · events -> AsyncAPI · states -> `state -[event]-> state` · decisions -> ADR · tool entry -> `AGENTS.md`/`llms.txt` · big codebase queries -> `doc-graphify` (complement only).

## Update after a development (last step of every dev)
After the `qa` go, before the push or PR: `git diff <base>...HEAD --stat` and read the diff; update `graph.yaml`, touched feature files (Change set, rules, traps), `api/*`, `data/*`, `structure.md` if a folder moved, glossary, the `commit` stamp of each touched file and INDEX counts; keep the token budget; verify; commit docs only on the same branch.

## Monthly refresh
Last refreshed: 2026-10. At first use in a later month: recheck the sources of the technology skills this one routes to; update only on confirmed better practice; keep the project's rules; report in one line.
