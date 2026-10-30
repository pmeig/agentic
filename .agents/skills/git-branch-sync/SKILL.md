---
name: git-branch-sync
description: Use (front) after a merged PR to clean the local branch and update the target, and before each new feature to branch from the default branch.
---

# Git branch sync (router)

Owned by `front`, which runs it in the repository of the feature. Load only the row that matches your current situation.

## Need -> file

| Situation | Load |
|---|---|
| After a pull request is merged: clean branch, update target | `references/after-merge.md` |
| Before every new feature: branch from the default branch | `references/before-feature.md` |
| Rules: what is never allowed (force push, reset, history rewrite) | `references/boundaries.md` |
