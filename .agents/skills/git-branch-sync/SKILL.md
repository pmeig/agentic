---
name: git-branch-sync
description: Use (front agent) when a feature branch has been merged to clean up the local branch and update the PR target branch, and before every new feature to update the default branch and create the feature branch.
---

# Git Branch Sync

Owned by `front`, which runs it in the repository of the feature. Run every git command in that repository; never touch the
remote branches (the forge deletes them or the lead does).

Protected branches, never deleted locally: `develop`, `release`, `main`.

## After the pull request is merged

1. Confirm the merge on the forge (PR state `merged`). Do not rely on `git branch --merged` alone: squash and rebase merges leave
   the feature branch looking unmerged.
2. Note the PR target branch (`base`), for example `develop`, `release` or `main`.
3. `git fetch --prune origin`, then `git checkout <base>` (stash or ask the lead first if the working tree is dirty; never discard changes).
4. `git pull --ff-only origin <base>`. If it cannot fast-forward, stop and tell the lead; never reset or force.
5. Delete the merged local branch, unless it is `develop`, `release` or `main`: `git branch -d <branch>`; when the merge was a
   squash/rebase and `-d` refuses, `-D` is allowed only because step 1 confirmed the merge.
6. Other local branches already merged into `<base>` may be deleted the same way; keep the protected ones and any branch with
   unmerged work (ask the lead if unsure).
7. Report: branch deleted, branch now checked out, commit it points to.

## Before every new feature

1. Find the default branch of the project (the repository's default on the forge, `git symbolic-ref refs/remotes/origin/HEAD`; ask
   the lead when the project uses `develop` or `release` as integration branch).
2. `git fetch --prune origin`, `git checkout <default>`, `git pull --ff-only origin <default>`.
3. Create the feature branch from it: `git checkout -b <type>/<feature>` (name from `need.md`, kebab-case, the repository's own
   prefix convention first, for example `feat/`, `fix/`).
4. Never start a feature on top of an old feature branch or an out-of-date default branch.
5. Write the branch name in `.agents/docs/team/<feature>/need.md` for the other agents.

## Boundaries

- No force push, no `reset --hard`, no history rewriting, no deletion of a branch whose work is not merged.
- Opening the pull request stays subject to the `qa` go (`AGENTS.md`).
