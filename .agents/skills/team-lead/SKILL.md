---
name: team-lead
description: "lead only: playbook to create a project or add a feature with the team (steps 0-12), bugfix routing and lead rules. Load at the start of any feature, bug or PR work, then one reference per step."
---

# Lead playbook (router)

Compact flow in `AGENTS.md`; details are split per step. Load only the row(s) for the situation you are in now, never all.

## Always (every lead turn)

Load `references/lead-rules.md` once per session (brevity, missing agent, cold briefs, lazy skills).

## Need -> file

| Situation | Load |
|---|---|
| New project, no code yet | `references/new-project.md`, then `references/flow-overview.md` per feature |
| New feature or change with new behavior in an existing project | `references/flow-overview.md`, then the step file it names, one step at a time |
| Unknown project before a fix or feature | `references/step-optional.md` (step 12: `documentalist` first) |
| Splitting `front`/`back`/other work across several agents | `references/parallelism.md` |
| Feature merged, closing it | `references/after-feature.md` |
| Red test, red CI, flaky test or bug with behavior already specified | skill `team-bugfix-mode` |
| Writing a brief, clearing context between steps | skill `context-handoff` |
