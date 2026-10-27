---
name: doc-ai-context-files
description: Use to write the files AI agents read first: AGENTS.md (CLAUDE.md as a link), llms.txt, pointers to .agents/docs/, size rules.
---

# Context files for AI agents

## AGENTS.md (the entry point every agent reads)

Plain Markdown at the repository root, read by Claude Code, Codex, Gemini CLI, Copilot, Cursor, OpenCode, Junie and others.
No schema; short beats complete. **The real file is `AGENTS.md`; `CLAUDE.md` contains the single line `@AGENTS.md` (Claude Code import; a symbolic link also works but needs rights on Windows).** Do not convert an existing real `CLAUDE.md` without asking. Written in English (`ai-docs-in-english`).

Put in it (about 60 to 150 lines):
1. **What the project is** in 3 lines and the module list with folders.
2. **Where to look first**: `.agents/docs/INDEX.md`, then `features/<feature>.md` for a feature, `api/endpoints.md` for routes,
   `data/schema.md` for tables, `conventions.md` before writing code.
3. **Which skill to load to run or connect** (name only): the commands themselves never go in AGENTS.md; they live in a global skill for generic tools or in a repo skill for repo-specific things (`run-and-access-skills`).
4. **Rules that differ from the defaults**: layering, naming, folder rules, test rules, language rules, forbidden things.
5. **Workflow rules**: branches, PRs, CI, who may merge or deploy, what to ask first.
6. **Traps**: generated files, secrets handling (names only), flaky tests.

Leave out: what the code already says, long tutorials, anything that rots fast (counts, versions copied by hand: link the source),
secrets, and instructions an agent follows anyway. Prefer a link to `.agents/docs/` over copying it. Nested `AGENTS.md` in a module folder
may add module-specific rules (the nearest file wins).

## Pointer block to add to the root AGENTS.md

```markdown
## Project map (for AI)
Start with `.agents/docs/INDEX.md` (stack, modules, commands). Then: feature -> `.agents/docs/features/<feature>.md`, routes ->
`.agents/docs/api/endpoints.md`, database -> `.agents/docs/data/schema.md`, conventions -> `.agents/docs/conventions.md`.
Docs were written at commit `<sha>`; check `git log <sha>..HEAD` for what changed since.
```

## llms.txt (only for public documentation sites)

Markdown at the site root (`/llms.txt`), proposed by Jeremy Howard (Sept 2024): H1 title, a blockquote summary, optional paragraphs,
then H2 sections of links `- [Title](url): one-line description`; an `## Optional` section marks skippable links. Optionally
`llms-full.txt` with the full content concatenated. Use it for a published docs site (`doc-sites-markdown`); not needed for a private
repository, where `AGENTS.md` + `.agents/docs/` do the job. Check adoption claims before promising SEO or AI-search gains.

## Related files

- `.github/copilot-instructions.md`, `.cursor/rules`, `GEMINI.md`: tool-specific; prefer one `AGENTS.md` and, if a tool needs its own
  file, a one-line pointer to it, never a divergent copy.
- Skills (`.agents/skills/<name>/SKILL.md`) hold procedures an agent loads on demand; `AGENTS.md` holds what applies to every task. Layout of a skill (router + `references/`) and when to split: `references/skills-layout.md`.

## Verify

Every command in the file was run or marked `(not run)`; every path exists (`doc-code-analysis` link check); file size stays small
enough to be read in full at each session start.

## Sources

- https://agents.md · https://llmstxt.org

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: check agents.md and llmstxt.org for spec changes, which tools read which file
(Claude Code, Codex, Gemini CLI, Copilot, Cursor), update, set the date, report changes.
