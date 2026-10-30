# Git branch sync: after the pull request is merged

Run every git command in the feature repository. Never touch remote branches (the forge deletes them or the lead does).

Protected branches — never deleted locally: `develop`, `release`, `main`.

1. Confirm the merge on the forge (PR state `merged`). Do not rely on `git branch --merged` alone: squash and rebase merges leave the feature branch looking unmerged.
2. Note the PR target branch (`base`), for example `develop`, `release` or `main`.
3. `git fetch --prune origin`, then `git checkout <base>` (stash or ask the lead first if the working tree is dirty; never discard changes).
4. `git pull --ff-only origin <base>`. If it cannot fast-forward, stop and tell the lead; never reset or force.
5. Delete the merged local branch, unless it is `develop`, `release` or `main`: `git branch -d <branch>`; when the merge was a squash/rebase and `-d` refuses, `-D` is allowed only because step 1 confirmed the merge.
6. Other local branches already merged into `<base>` may be deleted the same way; keep the protected ones and any branch with unmerged work (ask the lead if unsure).
7. Report: branch deleted, branch now checked out, commit it points to.
