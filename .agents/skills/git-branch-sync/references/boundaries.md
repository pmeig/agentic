# Git branch sync: boundaries

- No force push, no `reset --hard`, no history rewriting, no deletion of a branch whose work is not merged.
- Opening the pull request stays subject to the `qa` go (`AGENTS.md`).
- Never touch remote branches directly; let the forge or the lead handle them.
- Protected branches (`develop`, `release`, `main`) are never deleted locally under any circumstance.
