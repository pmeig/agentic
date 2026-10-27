# Lead playbook: flow of a feature (existing project)

```
need -> designer <-> front -> front <-> back (contract) -> code + unit tests
     -> qa go -> documentalist docs -> push + PR + CI until green -> merge on the user's yes -> sales (optional)
     any agent can question any other one at any step
     every arrow = brief + agent stops + lead /clear (state.md) -> next agent cold (context-handoff)
```

Load the file of the current step only; the previous steps' files are not needed again.

| Step | What | Load now |
|---|---|---|
| 0 | **Branches** (`front`, `git-branch-sync`): after a merged PR, check out the target branch, update it, delete the merged local branch (never `develop`, `release`, `main`). New feature: update the default branch, branch from it. | nothing more |
| 1 | **Need**: the lead writes `.agents/docs/team/<feature>/need.md` (who, what, why, acceptance criteria, open questions). Unknown project: `documentalist` first (step 12). | nothing more |
| 2 | **Design**: `designer`, per feature and page, 3-5 mockups, the lead or user picks | `references/step-design.md` |
| 3-4 | **Contract** then **build** (`front` + `back`, unit tests) | `references/step-build.md` |
| 5 | **Platform**: the lead or user owns monorepo, CI/CD, deployment | `references/new-project.md` item 5 |
| 6-7 | **Handover** `gesture.md`, then the **E2E gate** (`qa`) | `references/step-qa-gate.md` |
| 8 | **Documentation** (`documentalist`, before any push) | `references/step-docs.md` |
| 9 | **Push, PR, CI until green**, merge on the user's yes | `references/step-pr.md` |
| 10-12 | Promotion, translation, documentation on request | `references/step-optional.md` |

Red test, red CI or flaky test with behavior already specified, no new or changed behavior: skill `team-bugfix-mode`.
