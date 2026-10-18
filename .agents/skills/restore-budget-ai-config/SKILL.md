---
name: restore-budget-ai-config
description: Use ONLY when the user wants to go back to the former AI configuration of pmeig/budget (AGENTS.md, CLAUDE.md, the five project skills, the local e2e run.sh scripts) or to the former global setup that agentic replaced: gives the commit to revert, the backups and the exact steps.
---

# Restore the former AI configuration (pmeig/budget and the old global)

## What was changed (2026-10-17)
In `pmeig/budget`, PR #132 (squash commit on `develop`):
- **Commit to revert: `0e64163fd734aeb5b4950a0cce19cc1e36accb90`** (parent `aca7f1b`).
- Removed: `AGENTS.md`, `CLAUDE.md`, `.agents/skills/{budget-run,demo,e2e-android-then-web,feature-tutorial,web-parity}/SKILL.md`, the five junctions of `.claude/skills`, `e2e/android/run.sh`, `e2e/web/run.sh`, `e2e/common/{demo-db,lib}.sh` (the two helpers lived in `.agents/skills/demo/scripts/` until the commit before; the CI never used them).
- Kept: `docs/ai/` (all 25 files), `e2e/web/scripts/in-container.sh` (used by `quality.yml`).
- Edited: e2e and web READMEs, a few `docs/ai` lines and script comments that mentioned `run.sh`.

## Restore the repo
1. `git switch develop && git pull --ff-only && git switch -c revert/ai-config`
2. `git revert 0e64163fd734aeb5b4950a0cce19cc1e36accb90` (a revert commit; resolve conflicts if files changed since, keeping both sides' intent).
3. Recreate the local links (they are not versioned): junctions `.claude/skills/<name>` -> `.agents/skills/<name>` for each restored skill (`New-Item -ItemType Junction`, no admin needed).
4. Open the PR, follow the CI until green, merge only on the user's yes (`pr-and-ci-follow`).
If the revert conflicts too much, restore the files from the backup zip below instead and commit them.

## Backups (outside every scanned folder, never loaded as skills)
- `C:\Users\pierr\budget-ai-config-backup-2026-10-17.zip`: `AGENTS.md`, `CLAUDE.md`, the whole `.agents/` of budget (7 files, scripts included) and `claude-skills-links.txt` (name, link type, target of each junction).
- `C:\Users\pierr\global-agents-backup-2026-10-17.zip`: the former global `~/.agents` (24 skills), `claude-skills-links.txt` (the 24 former junctions of `~/.claude/skills`) and `CLAUDE.md.copy` (the former global `CLAUDE.md`).

## Restore the former global (agentic stays in its repo)
1. Remove the links `~/.agents/skills`, `~/.agents/agents`, `~/.claude/agents` and the per-skill junctions of `~/.claude/skills` (never `synced`); `[System.IO.Directory]::Delete(<link>, $false)` removes a link without touching its target.
2. Expand `agents-home` of the global zip into `~/.agents`, recreate the 24 junctions listed in `claude-skills-links.txt`, and copy `CLAUDE.md.copy` back to `~/.claude/CLAUDE.md`.
Ask the user before touching `~/.agents` or `~/.claude`.
