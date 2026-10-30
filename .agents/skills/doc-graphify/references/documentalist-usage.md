# Graphify: how the documentalist uses it

## How the documentalist uses it

1. Build the graph (after the checks above). Read `GRAPH_REPORT.md`: modules (communities), central files (god nodes), unexpected coupling.
2. Use it to find the **change set** of a feature and cross-feature dependencies faster; verify each claim in the code before writing it
   into `.agents/docs/` (a graph can contain stale or duplicated nodes after heavy refactors: rebuild before trusting).
3. Put in `.agents/docs/INDEX.md` and `commands.md`: that the graph exists, the rebuild command, when it was built (commit stamp), and
   `graphify query/path/explain` as the first move for impact questions.
4. Add one line to the root `AGENTS.md` project-map block (`doc-ai-context-files`): "dependency questions: `graphify query` / `graph.json`".
5. Never replace `.agents/docs/` by the graph, and never present graph output as verified business knowledge.

Also load `references/install-build.md` to build or query the graph and `references/licence-privacy.md` for the checks.
