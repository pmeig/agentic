# Graphify: install, build and query

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

Also load `references/licence-privacy.md` before the first build.
