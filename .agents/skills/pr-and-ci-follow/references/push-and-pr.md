# Push, pull request and CI: push and open the PR

- `git branch --show-current`: never push on the default or a protected branch; never `--force`, never `--no-verify`; uncommitted work is not pushed (say so).
- If the branch's previous PR is merged or closed, do not push more on it: tell the user and branch again from the updated default branch.
- Open the PR against the default branch unless told otherwise. Title = conventional commit (`feat(scope): ...`). Body = what changed, what to check (migration, contract change, new key), and the docs touched.
