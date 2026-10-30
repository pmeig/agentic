# Push, pull request and CI: everything green, ask before merging

"Green" = every check completed with success or skipped, none pending, no flaky left unaddressed, the PR mergeable and up to date with the base:
`gh pr view <n> --json statusCheckRollup,mergeStateStatus` shows 0 pending, 0 red, state clean. New commits on the base start new runs: check again right before asking. Summarize in a few lines (rounds, what was red and how it was fixed, final checks) and **ask the user for an explicit yes** before merging (squash for a feature PR; a merge commit for a release PR between long-lived branches, never deleting them). After the merge `front` cleans the branches (`git-branch-sync`).
