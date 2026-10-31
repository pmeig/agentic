# AI documentation: procedure (new docs or full refresh)

## Procedure
0. Ask `ai-writer` how to write the doc first (rule: step 6 of `documentalist.md`).
1. Scope (project, feature, update); read `AGENTS.md`/`CLAUDE.md`, README, build files. If `.agents/docs/` exists compare its `commit` with `git log` and update only the diff, never rewrite.
2. Extract (`doc-code-analysis`); write in order: structure, data, api, features, `graph.yaml`, flows, architecture, conventions, glossary, gotchas, INDEX last.
3. Verify: paths exist, OpenAPI lints, commands run or `(not run)`; wire the pointer in the root `AGENTS.md` (`doc-ai-context-files`); report created, unverified, stale.

Also load `references/layout-and-index.md` for the file layout, and the reference of each document you write (`references/feature-file.md`, `references/impact-graph.md`).
