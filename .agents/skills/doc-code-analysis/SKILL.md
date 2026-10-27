---
name: doc-code-analysis
description: "Use to extract facts from a codebase before documenting: tree, modules, routes, features by layer, tests per feature, per-language tools."
---
# Code analysis for documentation (router)
Never document from memory. Extract, then write. Prefer the dedicated tools (Glob, Grep) in a session; the shell commands below are
the portable equivalents to put in `.agents/docs/commands.md` so they can be rerun.
Load only the row(s) that match the file being written or the question; never load every reference.
## Need -> file
| Need (which document / action) | Load |
|---|---|
| Folder inventory, modules, annotated tree | `references/tree-modules.md` |
| Features by layer, change set, tests per feature | `references/features-by-layer.md` |
| Routes and handlers (grep patterns per stack) | `references/routes.md` |
| Dependencies between modules/layers per language | `references/deps.md` |
| Symbols, env, flags, history, hot spots | `references/other-extractions.md` |
| Check that paths and links in docs exist | `references/link-check.md` |
| Monthly refresh | `references/maintenance.md` |
