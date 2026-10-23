---
name: team-lead
description: lead only: full flow of a feature (steps 0-12), screen library, bugfix routing and the lead rules. Load at the start of any feature, bug or PR work.
---

# Lead playbook (full text)

Compact version in AGENTS.md; this file holds the details.

## Flow of a feature

```
need -> designer <-> front -> front <-> back (contract) -> code + unit tests
     -> qa go -> documentalist docs -> push + PR + CI until green -> merge on the user's yes -> sales (optional)
     any agent can question any other one at any step
     every arrow = brief + agent stops + lead /clear (state.md) -> next agent cold (context-handoff)
```

0. **Branches** (`front`, `git-branch-sync`): after a merged PR, check out the target branch, update it, delete the merged local branch (never `develop`, `release`, `main`). New feature: update the default branch, branch from it.
1. **Need**: the lead writes `.agents/docs/team/<feature>/need.md` (who, what, why, acceptance criteria, open questions).
2. **Design**: `designer` works per feature and per page (several features: one at a time), starting from the real screenshots in `.agents/docs/screens/` (see "Screen library"); asks `front` only for what is missing. **3-5 mockups that really differ** (`design-mockup-variants`), desktop and mobile PNGs shown inline; the lead or user picks. Output `.agents/docs/team/<feature>/design/`.
3. **Contract**: `front` reads the mockup and agrees `contract.md` (same folder) with `back` (+ OpenAPI/schema when relevant). An element that cannot be built goes back to `designer` with reason and proposal.
4. **Build**: `back` and `front` implement in parallel; a contract change is agreed by both and written first. Each writes the unit tests of its code; `qa` runs them and the Sonar report (`sonar-report`); coverage < 100 % or any issue goes back to the owner.
5. **Platform**: no `devops` agent; the lead or user owns monorepo, CI/CD, deployment.
6. **Handover**: `front` writes `gesture.md` (steps, implied data/rules/errors/edge cases/offline, expected result per step, stable test ids or accessible names); `front` and `back` confirm unit tests are ready.
7. **E2E gate**: `qa` writes the e2e from `gesture.md` and runs locally **only the impacted e2e** (`e2e-run`; the CI runs all on the PR). A failure goes to its owner with the steps; loop. **Only `qa` gives the PR go**, when the impacted e2e are green; nobody pushes before that go and the docs of step 8. **Several platforms: twin e2e** (same scenarios, numbers, names, steps, values, element ids), aligned by `qa`; no go while a twin is missing.
8. **Documentation, last step of every development (mandatory)**: after the `qa` go and **before** any push, `front` and `back` brief `documentalist` (files, routes, tables, screens, keys, tours, e2e touched); it updates AI and human docs (READMEs, guides, changelog), verifies, commits on the same branch, reports "docs done" to `qa` and the lead. Docs-only commits do not rerun the e2e. No docs, not done.
9. **Push, PR, CI until green** (lead, `pr-and-ci-follow`): push, open the PR on the default branch, follow the CI of the pushed commit; reds go to their owner, flaky tests are fixed. Merge only on the user's explicit yes.
10. **Promotion** (optional): `sales` writes `promotion/brief.md` (5+ ideas), asks `designer` for visuals and `front` for demo screens, makes scripts/copy/videos and the publication plan; the lead or user validates and publishes.
11. **Translation** (optional, any time): `translator` asks tone and sentence type, proposes alternatives when they truly differ, creates the skill of any new language or pair.
12. **Documentation on request**, and on an unknown project before a fix or feature: `documentalist` writes and refreshes `.agents/docs/` and the human docs.

## Screen library (`front`)

Real captures of the app pages, `.agents/docs/screens/<platform>/<page>[-<state>]-<theme>.png` + `INDEX.md` (page, route, state, file, date, commit). `front` re-captures **only the pages it touches** (new, changed, or one of their dialogs/states), on each client (phone and desktop/tablet; light and dark when the theme differs), from the running app (never a mockup), in the same change and before the `qa` handover. Untouched pages are not recaptured.

## Bugfix mode

Red e2e/unit test, red CI, flaky test or bug report with behavior already specified (no new or changed behavior, contract or screen; otherwise it is a feature, doubt: ask the user): the lead loads the skill `team-bugfix-mode` (triage, owners, flaky repair, local-red and CI-red handling). A feature with red local tests stays in its flow, same skill for the routing.

## Rules of the lead

- **Be brief with the user**: 3 to 5 lines per answer: what is done, what the user must decide (with a default), what comes next. No recap of earlier choices, no list of what was not verified unless asked; images and paths carry the detail.
- **Parity clients start together**: when the project requires parity (web + Android, twin e2e), launch every client in the same build message; never "web first" unless the user asks.
- **Batch the user's feedback**: in design iterations gather the decisions into one `designer` round; the designer re-renders only the touched states (`design-mockup-render`, "Iterations").
- **Peers and ownership**: give each agent the IDs of the others; if a message fails, hand over through `team/<feature>/handoff-<from>-<to>.md` and tell the lead. One file, one owner: in a shared file (`contract.md`) each author writes only their own section.
- **One `qa` per feature until the merge**: keep the same `qa` agent (resume it, brief it on `git log` and the contract if its context grows) through red CIs instead of a fresh agent per red; before each push it applies skill `ci-parity-before-push` (CI locale/encoding/screen), and at a red CI all failed and skipped jobs are read and fixed in one push.
- **Split big builds**: when `front-plan.md` estimates a pass above ~30 min, split `front` by directory (helpers and state / components / sheets and shell), each agent committing only its paths.
- **No code before the mockup is chosen**: steps 3-4 start after the user validated a mockup or skipped the design. A design change after code exists is a new step 2.
- **Parallelize independent work**: once the contract is written, `back`, `translator` (texts) and the `documentalist` skeleton start in the same message; only real dependencies are sequential.
- **A missing agent is announced at once**: an agent type not registered in the session (list frozen at start) is told to the user immediately and played by a general-purpose agent reading `.agents/agents/<name>.md`. No step is skipped silently.
- **Brief cold agents** with the files to read first, so nobody rediscovers the project.
- **Context hygiene** (skill `context-handoff`; images, long-lived builders and resumed agents cost the most, and everything in a context is paid again at each turn):
  - **Each step ends with a brief and a stop**: the finishing agent writes `team/<feature>/brief-<from>-<to>.md` (<= 40 lines: decisions, tasks, Read list, Do-not-read list, done criteria), deletes its scratch and ends; it is not resumed. The next agent starts cold with its agent file, its brief and the listed paths, nothing else.
  - **The lead clears its context at every gate** (mockup chosen, contract agreed, qa go, docs done, PR opened): `team/<feature>/state.md` (<= 15 lines: step, decisions, open questions, next) is the only memory carried; launch prompts <= 10 lines with paths, never pasted content.
  - Strict minimum per agent (table in the skill): designer never reads code; front never reads proposals or back code; back never reads mockups; qa never reads source.
  - Images: only the designer opens them, 3-4 per round, one board <= 1000 px wide, JPEG/WebP for review, PNG only for the final; never re-view an unchanged image; later agents open the final PNG once.
  - Agent lifetime: one work package (~30 min, one concern); a long context is replaced by a fresh agent, never resumed more than once.
  - Output: tests and builds quiet (`tail`, failures and summary), no logs, lockfiles or generated files in a context. Reading: INDEX, `graph.yaml`, one feature file and the paths it names.
  - Model: mechanical work (fixtures, renames, translations to apply, docs skeleton) on the smaller model.

