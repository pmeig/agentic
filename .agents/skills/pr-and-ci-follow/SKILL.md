---
name: pr-and-ci-follow
description: Use after "docs done": push, open the PR, follow the CI until green, send reds to their owner, fix flaky tests, ask before merging.
---

# Push, pull request and CI until green

Driven by the lead (main session). The owners fix; the lead dispatches, pushes and follows. Nothing here is skipped because "it is small". Connection or tool problems (git hosting CLI not logged in, runner access): `run-and-access-skills`.

## 1. Before every push, PR creation or CI rerun: the machine must be free
Runners and local tests share the machine. Check **both**: no CI run in progress (any branch) and no e2e pid file of a live local run (`e2e-run`, section 1). Something blocks: wait (a background until-loop), do not kill another run, tell the user what blocks. Free: wait 30 seconds, check again, launch only if still clean.

## 2. Push and open the PR
- `git branch --show-current`: never push on the default or a protected branch; never `--force`, never `--no-verify`; uncommitted work is not pushed (say so).
- If the branch's previous PR is merged or closed, do not push more on it: tell the user and branch again from the updated default branch.
- Open the PR against the default branch unless told otherwise. Title = conventional commit (`feat(scope): ...`). Body = what changed, what to check (migration, contract change, new key), and the docs touched.

## 3. Follow the CI of the pushed commit
- Wait (at most 2 minutes) for the run of **this commit** to exist; follow it to the end; read the failed logs. `gh pr checks` right after a push still shows the previous run.
- **No run started** after 2 minutes: the PR probably conflicts with the base (the CI does not start on a conflicting PR) or the base moved. Merge the base into the branch (a merge, never a rebase or a force push), resolve conflicts keeping what both sides added, then `qa` reruns the impacted e2e (all when unsure) before pushing the merge. Nothing to merge and still no run: path filters or late Actions, report it instead of waiting.

## 4. Every red goes back to its owner, then the loop restarts
| Red | Goes to | Then |
|---|---|---|
| e2e or any test failing | `qa`: decides whether the code or the test is wrong (trace, screenshot, steps); never weakens an assertion | code wrong: `front` or `back` with scenario, steps, expected/actual, trace; test wrong: `qa` fixes it |
| compile, type, lint or unit-test error | owner of the file: `front` (client) or `back` (server) | fix and add the missing test |
| Sonar gate (coverage < 100 %, issues, duplication) | owner of the code, with the report from `sonar-report` | fix the code or add tests; never exclude files or silence a rule without the lead's decision |
| Infrastructure: runner offline, secret/cache/network error, same failure on unrelated PRs | the lead or the user | **do not loop**; report the cause and what to change |
After each fix: `qa` reruns the impacted e2e locally (machine free), `documentalist` updates the docs if the behavior changed (docs only otherwise), then the lead pushes and follows the new run. **Repeat until every check is green.**

## 5. Flaky tests are not green
A check that fails then passes on a rerun, or a test that only passes sometimes, is **not** a pass and is never just rerun. `qa` fixes the cause (procedure "Flaky tests" of `e2e-run`), with the owner when the cause is in the code, and shows it stable (several consecutive green runs, in the CI too) before the PR counts as green.

## 6. Stop conditions (report to the lead and the user instead of looping)
The same failure after two fixes; more than five rounds; an infrastructure cause; a fix that would change behavior or the public contract (ask first).

## 7. Everything green: ask before merging
"Green" = every check completed with success or skipped, none pending, no flaky left unaddressed, the PR mergeable and up to date with the base:
`gh pr view <n> --json statusCheckRollup,mergeStateStatus` shows 0 pending, 0 red, state clean. New commits on the base start new runs: check again right before asking. Summarize in a few lines (rounds, what was red and how it was fixed, final checks) and **ask the user for an explicit yes** before merging (squash for a feature PR; a merge commit for a release PR between long-lived branches, never deleting them). After the merge `front` cleans the branches (`git-branch-sync`).

## Monthly refresh
Last refreshed: 2026-10. At first use in a later month: recheck the hosting CLI commands you rely on, update, report in one line.
