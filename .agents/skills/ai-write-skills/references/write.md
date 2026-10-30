# ai-write-skills: write and test
# skills: Skills (write)

A skill is packaged know-how loaded on demand. Layout and split rules: `doc-ai-context-files` -> `references/skills-layout.md` (single source; do not restate it).

## Before creating

Search `.agents/skills/` for a skill already covering the need and extend it rather than add a near-duplicate. A skill is worth it for a recurring task, a non-obvious procedure, or domain facts the model gets wrong unaided. Not for what the model already knows well.

## Frontmatter

```yaml
---
name: kebab-case-equal-to-folder
description: "<who> + <when to use>. Never the content."
---
```

- `description` is the only text always in context: it decides whether the skill loads. Start with the actor when role-specific (`qa:`, `lead only:`), then the trigger situations in the words a user or agent would use. One or two sentences, <= ~250 characters; quote it if it contains `: `.
- Optional fields (`allowed-tools`, `disable-model-invocation`, `user-invocable`, `argument-hint`, `model`, `context`, `agent`, `paths`, `hooks`): only with a stated reason; confirm in the current docs.
- Add the skill to the agent tables that should load it (`ai-write-agent-definitions`).

## Body

- Router (`SKILL.md`): optional `Always` block, then the `Need -> file` table. No procedure.
- `references/<need>.md`: self-contained, named by need (`setup`, `tests`, `code`, `structure`, `report`...). Open with the decision the reader must take, then steps, one example, the pitfalls seen in practice.
- `scripts/`: helpers the agent runs rather than reads; document inputs and outputs in the reference that uses them; quiet output (summary and failures).
- Skills on moving facts (tools, versions, platform rules) end with **Monthly refresh** (`Last refreshed: <YYYY-MM>`) and **Sources**. Stable house conventions do not need one.

## Registration

Claude Code sees skills through `.claude/skills` (a link to `.agents/skills`): verify the new folder appears there; on a machine with a global copy, link it (`sync-agents-md`). A skill added mid-session is available from the next session.

## Test

Cold agent, one realistic task that should trigger the skill, phrased without naming it: it must find and load the skill, read only the needed reference, and succeed. If it did not trigger, rewrite the description, not the body.

