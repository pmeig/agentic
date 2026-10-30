---
name: pr-and-ci-follow
description: "Use after \"docs done\": push, open the PR, follow the CI until green, send reds to their owner, fix flaky tests, ask before merging."
---
# Push, PR and CI until green (router)
Driven by the lead (main session). The owners fix; the lead dispatches, pushes and follows. Nothing here is skipped because "it is small". Connection or tool problems (git hosting CLI not logged in, runner access): `run-and-access-skills`. Load only the row(s) that match the situation; never load every reference.
## Need -> file
| Situation (what the agent is doing / which step) | Load |
|---|---|
| Before every push, PR creation or CI rerun (machine free) | `references/before-push.md` |
| Pushing the branch, opening the PR | `references/push-and-pr.md` |
| Following the CI of the pushed commit, no run started | `references/follow-ci.md` |
| A check is red: owner, loop, stop conditions | `references/red-routing.md` |
| A check fails then passes, or passes only sometimes | `references/flaky.md` |
| Everything green, asking before merge | `references/merge.md` |
| Monthly refresh | `references/maintenance.md` |
