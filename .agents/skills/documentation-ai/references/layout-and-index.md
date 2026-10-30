# AI documentation: layout, INDEX and format choice

## Layout (create only what exists)
```
.agents/docs/
  INDEX.md          product in 3 lines, stack, modules, reading budget with cost per file, first moves per task, names of the skills that run/connect
  graph.yaml        IMPACT GRAPH (required, see `references/impact-graph.md`)
  structure.md      annotated tree (depth 2-3) + module table (module | purpose | stack | entry point | owns data)
  features/<f>.md  template in `references/feature-file.md`
  api/              openapi.yaml (generated when possible), asyncapi.yaml if events, endpoints.md (METHOD path | handler:line | auth | tables | feature)
  data/             schema.dbml, schema.md (relations as edge lists FK + logical, one line per table), migrations.md (tool, how to add one, rollback rule)
  architecture.md   context + containers + deployment as edge lists
  conventions.md    naming, layering, errors, test and folder rules, workflow, **definition of done**
  glossary.md       domain word -> code name
  gotchas.md        traps, generated files, flaky tests, order dependencies, never-open files
  decisions/        ADRs (NNNN-title.md)
```
No `commands.md`: how to run/connect is a skill (`run-and-access-skills`); INDEX only names it.

## Format choice
tree -> annotated tree + table · impact -> `graph.yaml` · journey -> one-line chain · architecture -> edge list · tables -> DBML + edge list · REST -> OpenAPI · events -> AsyncAPI · states -> `state -[event]-> state` · decisions -> ADR · tool entry -> `AGENTS.md`/`llms.txt` · big codebase queries -> `doc-graphify` (complement only).
