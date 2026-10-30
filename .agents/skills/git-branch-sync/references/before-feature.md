# Git branch sync: before every new feature

Run every git command in the feature repository.

Protected branches — never deleted locally: `develop`, `release`, `main`.

1. Find the default branch of the project (the repository's default on the forge, `git symbolic-ref refs/remotes/origin/HEAD`; ask the lead when the project uses `develop` or `release` as integration branch).
2. `git fetch --prune origin`, `git checkout <default>`, `git pull --ff-only origin <default>`.
3. Create the feature branch from it: `git checkout -b <type>/<feature>` (name from `need.md`, kebab-case, the repository's own prefix convention first, for example `feat/`, `fix/`).
4. Never start a feature on top of an old feature branch or an out-of-date default branch.
5. Write the branch name in `.agents/docs/team/<feature>/need.md` for the other agents.
