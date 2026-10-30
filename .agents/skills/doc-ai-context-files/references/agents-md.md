# Context files for AI agents: AGENTS.md

Plain Markdown at the repository root, read by Claude Code, Codex, Gemini CLI, Copilot, Cursor, OpenCode, Junie and others.
No schema; short beats complete. **The real file is `AGENTS.md`; `CLAUDE.md` contains the single line `@AGENTS.md` (Claude Code import; a symbolic link also works but needs rights on Windows).** Do not convert an existing real `CLAUDE.md` without asking. Written in English (`ai-docs-in-english`).

Put in it (about 60 to 150 lines):
1. **What the project is** in 3 lines and the module list with folders.
2. **Where to look first**: `.agents/docs/INDEX.md`, then `features/<feature>.md` for a feature, `api/endpoints.md` for routes, `data/schema.md` for tables, `conventions.md` before writing code.
3. **Which skill to load to run or connect** (name only): the commands themselves never go in AGENTS.md; they live in a global skill for generic tools or in a repo skill for repo-specific things (`run-and-access-skills`).
4. **Rules that differ from the defaults**: layering, naming, folder rules, test rules, language rules, forbidden things.
5. **Workflow rules**: branches, PRs, CI, who may merge or deploy, what to ask first.
6. **Traps**: generated files, secrets handling (names only), flaky tests.

Leave out: what the code already says, long tutorials, anything that rots fast (counts, versions copied by hand: link the source), secrets, and instructions an agent follows anyway. Prefer a link to `.agents/docs/` over copying it. Nested `AGENTS.md` in a module folder may add module-specific rules (the nearest file wins).

## Pointer block to add to the root AGENTS.md

~~~markdown
## Project map (for AI)
Start with `.agents/docs/INDEX.md` (stack, modules, commands). Then: feature -> `.agents/docs/features/<feature>.md`, routes ->
`.agents/docs/api/endpoints.md`, database -> `.agents/docs/data/schema.md`, conventions -> `.agents/docs/conventions.md`.
Docs were written at commit `<sha>`; check `git log <sha>..HEAD` for what changed since.
~~~

## Tool-specific files

`.github/copilot-instructions.md`, `.cursor/rules`, `GEMINI.md`: tool-specific; prefer one `AGENTS.md` and, if a tool needs its own file, a one-line pointer to it, never a divergent copy.
