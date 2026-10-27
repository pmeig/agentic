---
name: documentation-ai
description: "MANDATORY for the documentalist writing docs FOR AN AI: .agents/docs/ layout, impact graph, machine-first formats, token budget, end-of-development update."
---
# AI documentation (router)
Docs for an AI in `.agents/docs/` (same path in every project), in English, machine-first (maps, edge lists, `path:line`; no diagrams). Load only the row(s) that match the file being written or the question; never load every reference.
## Need -> file
| Need (which document / action) | Load |
|---|---|
| Principles: language, location, formats, index first, freshness stamp | `references/principles.md` |
| Folder layout, `INDEX.md`, which format for what | `references/layout-and-index.md` |
| `graph.yaml` impact graph (also the local e2e gate) | `references/impact-graph.md` |
| `features/<f>.md` template | `references/feature-file.md` |
| Token budget, caps, measuring | `references/token-budget.md` |
| `conventions.md` definition of done | `references/conventions-done.md` |
| Create or refresh the docs (procedure, write order) | `references/procedure.md` |
| End-of-development update (before push/PR) | `references/update-after-dev.md` |
| Monthly refresh | `references/maintenance.md` |
