# Push, pull request and CI: follow the CI of the pushed commit

- Wait (at most 2 minutes) for the run of **this commit** to exist; follow it to the end; read the failed logs. `gh pr checks` right after a push still shows the previous run.
- **No run started** after 2 minutes: the PR probably conflicts with the base (the CI does not start on a conflicting PR) or the base moved. Merge the base into the branch (a merge, never a rebase or a force push), resolve conflicts keeping what both sides added, then `qa` reruns the impacted e2e (all when unsure) before pushing the merge. Nothing to merge and still no run: path filters or late Actions, report it instead of waiting.
