---
name: doc-graphify
description: "Use for a queryable code knowledge graph with Graphify: when it helps, install, build, query, commit rules, license and privacy checks."
---
# Graphify (router)
Graphify builds a queryable knowledge graph of the codebase; it complements `.agents/docs/`, never replaces it. Load only the row(s) that match the file being written or the question; never load every reference.
## Need -> file
| Need (which document / action) | Load |
|---|---|
| Should we use it? (big vs small codebase) | `references/when-it-helps.md` |
| License, privacy, cost checks before adopting | `references/licence-privacy.md` |
| Install, build, query, commit rules | `references/install-build.md` |
| Using the graph for the docs (INDEX, AGENTS.md line) | `references/documentalist-usage.md` |
| Alternatives when Graphify is not allowed | `references/alternatives.md` |
| Monthly refresh, sources | `references/maintenance.md` |
