# AI documentation: principles

Goal: an AI that has never seen the project finds **where things are, how they connect, what a change touches and which tests to run** in a few reads. Optimize retrieval, not prose. Human docs: `documentation-human`.

1. **All AI-facing documents are in English** (skill `ai-docs-in-english`), whatever the user's or the product's language (`.agents/docs/`, `AGENTS.md`, `.agents/docs/team/`, skills, memory, prompts). Domain words keep their original spelling next to the English name (glossary).
1b. **Location: `<project>/.agents/docs/`** in every project (same path for all agents and projects; team workspace in `.agents/docs/team/<feature>/`). Never `docs/ai`.
2. **Machine-first formats; human readability is irrelevant**: YAML/JSON maps, edge lists (`a -> b`, `a = b`), dense tables, `path:line`. No Mermaid, ASCII art, diagrams, prose or layout for the eye (Mermaid stays in human docs). Contracts keep their native format (OpenAPI, AsyncAPI, DBML, SQL).
3. **Index first**: `INDEX.md` routes to everything else; an AI loads it, then only what it needs.
4. **Exact paths**: every claim points at `path:line` or a folder; a route without its handler is useless.
5. **Derive from the code**; mark `(unverified)`; generated artifacts beat hand-written copies (`doc-code-analysis`).
6. **Small files, stable `##` headings**, one concern per file, kebab-case; split when large.
7. **Say what changes together** (change set), the tests to run, the traps (invariants, generated files, flaky tests, migration order).
8. **Stamp freshness**: front matter `updated`, `commit` (short SHA); a reader compares with `git log`.
