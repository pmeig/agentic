---
name: ai-write-commands
description: "ai-writer: create or revise a slash command or user-invoked prompt file (.claude/commands/*.md): arguments, allowed tools, shell injection, output contract."
---

# Slash commands

Load `ai-write-principles` first. A command is a prompt the **user** triggers by name (`/name args`). If the model should also decide to use it, write a skill (`ai-write-skills`); when both fit, one skill beats a command plus a skill.

## File

`.claude/commands/<name>.md` (project) or `~/.claude/commands/<name>.md` (personal); subfolders namespace the name. Name: short, verb-first, kebab-case (`review-pr`, `release-notes`).

```markdown
---
description: One line shown in the command menu.
argument-hint: [pr-number] [--fix]
allowed-tools: Bash(git diff:*), Read, Grep
model: sonnet
---
<prompt body>
```

- `description`: what it does, for a human choosing from a list (<= ~80 characters).
- `argument-hint`: shown while typing; mirrors the arguments the body uses.
- `allowed-tools`: the minimum that removes permission prompts; scope Bash narrowly (`Bash(git diff:*)`, not `Bash`).

## Body

1. One-sentence goal, then numbered steps; the last step is the **output contract** (format, length, where the result goes).
2. Arguments: `$ARGUMENTS` (all) or `$1`, `$2`; say what to do when empty (ask once, or use a default).
3. Live context with a bang-prefixed shell command (output injected before the model runs) and file content with `@path`: only for small, stable output that saves a tool round trip.
4. Side effects (commit, push, delete, send): state them and require confirmation unless the command's whole purpose is that action.
5. No secrets in the body; reference a path or an environment variable.

## Test

Run it with arguments, with none, and with a bad one; there should be no permission prompt for allowed tools, and the output must follow the contract.

## Monthly refresh

Last refreshed: 2026-10 (initial writing; confirm sources at the first use of a later month)

Check the slash-commands and skills pages for the commands-skills merge status, frontmatter fields, argument syntax and injection syntax; update; set the date; report.

## Sources

- https://code.claude.com/docs/en/slash-commands
