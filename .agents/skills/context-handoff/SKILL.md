---
name: context-handoff
description: "Lead and every agent at each step change of a feature: write a handoff brief, end the agent, start the next one cold with only its brief; /clear the lead between steps. Load only the file for the moment."
---

# Context handoff (router)

Principle: a decision is paid once (written in a brief), never carried. The context of a finished step is discarded; the next agent reads **its brief, not the history**. Load only the row that matches the moment.

## Need -> file

| Moment | Load |
|---|---|
| Agent: starting a package, or ending it with a brief | `references/agent-start-finish.md` |
| Writing `state.md` or a brief (format, size, existing deliverables) | `references/files.md` |
| Lead: launching the next agent, clearing context at a gate | `references/lead-launch.md` |
| Which paths may my role read | `references/read-minimum.md` |
| Package too big, images, noisy output, agent lifetime, model choice | `references/limits.md` |
