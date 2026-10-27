# Lead playbook: always-on lead rules

- **Be brief with the user**: 3 to 5 lines per answer: what is done, what the user must decide (with a default), what comes next. No recap of earlier choices, no list of what was not verified unless asked; images and paths carry the detail.
- **A missing agent is announced at once**: an agent type not registered in the session (list frozen at start) is told to the user immediately and played by a general-purpose agent reading `.agents/agents/<name>.md`. No step is skipped silently.
- **Brief cold agents** with the files to read first, so nobody rediscovers the project; launch prompts <= 10 lines with paths (skill `context-handoff`, `references/lead-launch.md`).
- **Lazy skills**: never paste or pre-load skills for an agent; each agent loads its own at its triggers (its agent file). Name a skill in a brief only when the task needs a non-obvious one.
