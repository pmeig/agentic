# ai-write-agent-definitions: write and test
# agent-definitions: Agent definitions (write)

File: `.agents/agents/<name>.md` (`.claude/agents/` is a link to it, never a second copy). One agent = one role owning a defined set of files.

## Frontmatter

```yaml
---
name: kebab-case-unique
description: <routing text, see below>
model: sonnet            # alias only (haiku | sonnet); never `opus` in this team
tools: Read, Grep, Bash  # omit = inherits all; list only to restrict the role
---
```

Other fields exist (`disallowedTools`, `skills`, `permissionMode`, `maxTurns`, `mcpServers`, `hooks`, `memory`, `color`, `effort`, `isolation`): add one only for a stated reason and confirm it in the current docs (Monthly refresh); an unknown field is silently ignored, so test it.

## The description is the router

The lead and the harness pick the agent from `description` alone. Order: who the agent is (one clause), what it owns, how it works (one clause), then **"Use to/when ..."** with the triggers. Third person, English, 300-600 characters, single line, no `: ` or ` #` in the unquoted value (invalid YAML, the agent silently fails to load; reword or quote). Add the negative space when two agents are close ("not for X, use `back`").

## Body layout

1. Opening line: `You are the **<name>** (process in the team AGENTS.md).` + goal in one sentence.
2. **Skills table** (Trigger -> skill -> reference), lazy: loaded at the trigger, never up front. First rows: `context-handoff` (start/finish), `ai-docs-in-english`.
3. **How you work**: 5-8 numbered steps; each names its output and its skill.
4. **Boundaries**: what the agent never does, who it asks instead (exact agent names), what it returns (format, size).
5. **Context handoff**: what it receives and returns, which files it must not read.

Procedures, checklists and stack knowledge go to skills. The body is identity, routing and boundaries.

## Rules of thumb

- Imperative verbs, one concern per line; no motivational prose.
- Peers are named exactly as registered; messages between agents carry paths, not pasted content.
- Model: `haiku` for mechanical or transformation roles, `sonnet` for judgement roles; justify any exception in the report.
- Tools: restrict only when a wrong call is costly (read-only reviewer, no network); otherwise inherit.
- After creating an agent: add it to the table in `AGENTS.md` and the agent count in `README.md`, then run `sync-agents-md`. A new agent only exists in a **new session**: tell the lead.

## Test

Spawn the agent cold on one realistic task: it loads the right skills, stays inside its boundaries and returns the promised format.

