---
name: ai-write-principles
description: "MANDATORY for ai-writer before writing or reviewing any AI-facing file: audience, English, brevity, structure, examples, testing the file on a cold agent, size budget."
---

# Writing files for an AI: principles

The project's own rules win. English only (`ai-docs-in-english`). Applies to every file type; type-specific rules live in the `ai-write-*` skill of that type.

## Method (always, in order)

1. **Reader and moment**: who reads it (which agent, which model size), when (every session, at a trigger, once), and what they must do differently afterwards. If no behaviour changes, do not write the file.
2. **Smallest file**: every line is paid again at each turn it is loaded. Always-loaded content in few lines, trigger-loaded content in a skill reference, rare content behind a link.
3. **One rule, one place**: link instead of copying; a rule duplicated in two files drifts.
4. **Write for a cold reader**: no "as discussed", no section numbers of another file, no pronoun without referent; name paths, commands, exact values.
5. **Say what to do**, then why in one clause when the reason is not obvious; positive instructions before prohibitions; a few hard "never/always", each with its reason.
6. **Concrete beats abstract**: one real example (input -> output, command -> result) per non-obvious rule; real paths and names from the project.
7. **Structure for scanning**: headings by need, tables for lookups (trigger -> file), numbered steps only for ordered procedures, bullets for parallel rules. No prose recap, no marketing tone, no emphasis inflation (MANDATORY/NEVER only for rules that really are).
8. **Write it, then test it**: hand the file to a cold agent (`Agent`, fresh context) with one realistic task; read what it did and where it hesitated; fix the file, not the task. A file never exercised is a draft.

## Size budget

| File | Target |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | read in full every session: as short as possible (`doc-ai-context-files`) |
| Agent definition | body <= ~100 lines; procedures live in skills |
| Skill router (`SKILL.md`) | ~1-1.5 KB |
| Skill reference | ~1-4 KB, one need |
| Slash command | <= ~40 lines |
| Memory file | one fact, <= ~15 lines |

Over budget: split by need or delete the least useful lines. Do not go so telegraphic that a cold reader cannot parse it.

## Review checklist (before delivering)

- English, valid frontmatter, every path and command exists or is marked `(not run)`.
- No duplicate of another file's rule; no contradiction with `AGENTS.md`.
- Description says **when**, never **what is inside**.
- Cold-agent test done, result noted in the report.
- No secrets, tokens or personal data.

## Monthly refresh

Last refreshed: 2026-10 (initial writing; confirm sources at the first use of a later month)

At the first use in a later month: read the sources, update this file, keep the user's own rules, set the date, report what changed in one line.

## Sources

- Anthropic, prompting best practices: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
- Anthropic engineering, "Effective context engineering for AI agents", "Writing effective tools for agents": https://www.anthropic.com/engineering
- Claude Code docs (memory, sub-agents, skills, hooks, settings): https://code.claude.com/docs
- AGENTS.md convention: https://agents.md
