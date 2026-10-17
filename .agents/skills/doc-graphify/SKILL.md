---
name: doc-graphify
description: Use to give an AI a queryable knowledge graph of a codebase with Graphify (tree-sitter AST extraction, graphify-out/ with GRAPH_REPORT.md, graph.json, graph.html; query, path, explain; git hook updates): when it helps, install, build, query, commit rules, license and privacy checks.
---

# Graphify: knowledge graph of the codebase

Graphify turns a project (code, docs, PDFs, images, optionally video/audio transcripts) into a persistent graph an AI traverses instead
of grepping flat files; the vendors report large token savings on structure questions (figures are theirs, not verified here). It
**complements** `docs/ai/` (`documentation-ai`): the graph answers "what is connected to what" automatically and stays cheap to
rebuild; the hand-checked docs carry meaning (business rules, traps, conventions, decisions) that a graph cannot infer.

## When to use it

| Situation | Use |
|---|---|
| Big or unknown codebase, many modules, cross-feature impact questions ("what breaks if I change X") | yes: build the graph, then write `docs/ai/` from `GRAPH_REPORT.md` |
| Small project (a few dozen files) | no: `docs/ai/` alone is enough |
| Needs business meaning, API contract, DB schema, conventions | no: use `documentation-ai`, `doc-openapi-asyncapi`, `doc-database-schema` |
| Memory of conversations / user facts for an agent | not this tool (that is agent memory, e.g. Graphiti/Zep, a different product) |

## Check before adopting (ask the lead; record in an ADR)

1. **License**: sources report Creative Commons **BY-NC-SA 4.0** (non-commercial, share-alike). Read the repository `LICENSE` first; a
   commercial or client project may not be allowed to use it. Personal/internal use is the lead's call.
2. **Source of truth**: two repositories are cited (`safishamsi/graphify` and `Graphify-Labs/graphify`, the company is Graphify Labs, YC S26);
   take the one the PyPI package `graphifyy` (two y) points to, and confirm the name on PyPI before installing.
3. **Privacy**: code is parsed locally with tree-sitter (no API call); docs, PDFs, images and video are processed by the model of the
   current assistant session, so their content leaves the machine like any prompt. Exclude secrets, `.env`, customer data and
   private documents (`.graphifyignore` or the tool's ignore mechanism: check the current docs for the file name).
4. **Cost**: AST extraction is free; semantic extraction of documents consumes tokens: say so before running on a large doc set.

## Install and build (verify flags with `graphify --help` at first use)

```bash
uv tool install graphifyy        # or: pip install graphifyy   (Python; use the project's way to run Python)
graphify install                 # registers the skill/hook with the assistant (Claude Code, Gemini CLI, Codex, Cursor...)
graphify .                       # run from the project root (in an assistant session: /graphify .)
```

- Output folder `graphify-out/`: `GRAPH_REPORT.md` (communities, "god nodes" = most connected, surprising connections), `graph.json`
  (queryable), `graph.html` (interactive view). Sources say the folder is meant to be committed; commit `GRAPH_REPORT.md` and
  `graph.json` only after the license/privacy checks, and ignore large generated HTML if it bloats the repo.
- Query from the terminal: `graphify query "<question>"`, `graphify path <A> <B>` (shortest link between two nodes),
  `graphify explain <node>`.
- Database schema: `graphify extract --postgres "<dsn>"` introspects PostgreSQL (use a local copy and a read-only user; never put the
  password in a committed file or in a command that gets logged; secrets from the project's secret store).
- Claude Code and Gemini CLI: a hook nudges the assistant to the graph before search-style tool calls. A git hook can rebuild the
  graph on each commit (AST only, no API cost, union merge on `graph.json`).

## How the documentalist uses it

1. Build the graph (after the checks above). Read `GRAPH_REPORT.md`: modules (communities), central files (god nodes), unexpected coupling.
2. Use it to find the **change set** of a feature and cross-feature dependencies faster; verify each claim in the code before writing it
   into `docs/ai/` (a graph can contain stale or duplicated nodes after heavy refactors: rebuild before trusting).
3. Put in `docs/ai/INDEX.md` and `commands.md`: that the graph exists, the rebuild command, when it was built (commit stamp), and
   `graphify query/path/explain` as the first move for impact questions.
4. Add one line to the root `AGENTS.md` project-map block (`doc-ai-context-files`): "dependency questions: `graphify query` / `graph.json`".
5. Never replace `docs/ai/` by the graph, and never present graph output as verified business knowledge.

## Other tools of the same family (compare when Graphify is not allowed)

- `dependency-cruiser`, `madge`, `jdeps`, `pydeps`, `go list` (`doc-code-analysis`): module dependency graphs, per language, free of license questions.
- `ctags` / tree-sitter queries: symbol index; Sourcegraph/SCIP: code intelligence for large organizations.

## Sources

- https://github.com/safishamsi/graphify and https://github.com/Graphify-Labs/graphify (confirm which is current)
- https://pypi.org/project/graphifyy
- https://betterstack.com/community/guides/ai/ai-development/graphify-codebase/ · https://www.augmentcode.com/learn/graphify-knowledge-graph-codebase-skill

## Monthly refresh

Last refreshed: 2026-10 (install and commands taken from third-party guides, not yet run on a real project: confirm flags at first use,
mark confirmed ones). At first use in a later month: check the PyPI version and changelog, the license text, the repository of
record, new commands (`update`, `watch`, export formats, MCP server), hook behavior for Claude Code; update, set the date, report changes.
