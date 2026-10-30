# Graphify: when it helps

Graphify turns a project (code, docs, PDFs, images, optionally video/audio transcripts) into a persistent graph an AI traverses instead
of grepping flat files; the vendors report large token savings on structure questions (figures are theirs, not verified here). It
**complements** `.agents/docs/` (`documentation-ai`): the graph answers "what is connected to what" automatically and stays cheap to
rebuild; the hand-checked docs carry meaning (business rules, traps, conventions, decisions) that a graph cannot infer.

## When to use it

| Situation | Use |
|---|---|
| Big or unknown codebase, many modules, cross-feature impact questions ("what breaks if I change X") | yes: build the graph, then write `.agents/docs/` from `GRAPH_REPORT.md` |
| Small project (a few dozen files) | no: `.agents/docs/` alone is enough |
| Needs business meaning, API contract, DB schema, conventions | no: use `documentation-ai`, `doc-openapi-asyncapi`, `doc-database-schema` |
| Memory of conversations / user facts for an agent | not this tool (that is agent memory, e.g. Graphiti/Zep, a different product) |

Also load `references/licence-privacy.md` before adopting it, and `references/alternatives.md` when Graphify is not allowed.
