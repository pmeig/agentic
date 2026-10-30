---
name: doc-ai-context-files
description: "Write or update the files AI agents read first: AGENTS.md (CLAUDE.md as a one-line pointer), llms.txt for public sites, and skill layout."
---

# Context files for AI agents (router)

The project's own `CLAUDE.md` / `AGENTS.md` wins over these rules. Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Writing or updating AGENTS.md: content, structure, pointer block, CLAUDE.md link | `references/agents-md.md` |
| Writing or updating llms.txt for a public documentation site | `references/llms-txt.md` |
| Verifying or refreshing context files (monthly) | `references/verify.md` |
| Skill layout (router + references pattern), when to split a skill | `references/skills-layout.md` |
