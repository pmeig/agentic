# Lead playbook: step 9, push, PR, CI until green

9. **Push, PR, CI until green** (lead, `pr-and-ci-follow`): push, open the PR on the default branch, follow the CI of the pushed commit; reds go to their owner, flaky tests are fixed. Merge only on the user's explicit yes.

- Load skill `pr-and-ci-follow` and then only the reference of the moment (machine free before a push, push and PR, following the CI, red routing, flaky, merge).
- A red CI on a PR with specified behavior is handled with skill `team-bugfix-mode` -> `references/ci-red.md`.
- After the merge: `front` cleans the branches (`git-branch-sync`); the lead deletes `state.md` with the feature folder when closing the feature (`references/after-feature.md`).
