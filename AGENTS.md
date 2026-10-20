# Feature team

Seven agents build a feature autonomously and question each other until the need is clear. Definitions: `.agents/agents/` (linked from `.claude/agents/`).

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, gestures, journeys, colors, design accessibility | 3-5 mockups per screen, then the chosen one |
| `front` | every front-end stack, its unit tests | the screen, the contract (with `back`), the gesture for `qa` |
| `back` | every back-end stack, SQL/NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, unit-test runs, Sonar report, the go for the PR | impacted e2e green, Sonar objective met (100 % coverage, 0 issue) before the PR |
| `sales` | positioning, promotion, channels, copy, promo videos | brief, scripts, videos, publication plan (the lead publishes) |
| `translator` | translation as a native; one skill per language and pair, refreshed monthly | translated texts and files, alternatives on request |
| `documentalist` | docs for AIs (`.agents/docs/`, impact graph) and humans (README, guides, ADR) | docs in sync with the code (last step of every development); answers "how does X work" with paths |

## Flow of a feature

```
need -> designer <-> front -> front <-> back (contract) -> code + unit tests
     -> qa go -> documentalist docs -> push + PR + CI until green -> merge on the user's yes -> sales (optional)
     any agent can question any other one at any step
```

0. **Branches** (`front`, `git-branch-sync`): after a merged PR, check out the target branch, update it, delete the merged local branch (never `develop`, `release`, `main`). New feature: update the default branch, branch from it.
1. **Need**: the lead (main session) writes `.agents/docs/team/<feature>/need.md` (who, what, why, acceptance criteria, open questions).
2. **Design**: `designer` asks `front` for the current screens, proposes **3-5 mockups that really differ** (`design-mockup-variants`), desktop and mobile PNGs shown inline; the lead or user picks. Output `.agents/docs/team/<feature>/design/`.
3. **Contract**: `front` reads the mockup and agrees `contract.md` (same folder) with `back` (+ OpenAPI/schema when relevant). A mockup element that cannot be built goes back to `designer` with the reason and a proposal.
4. **Build**: `back` and `front` implement in parallel; a contract change is agreed by both and written first. Each writes the unit tests of its code; `qa` runs them and the Sonar report (`sonar-report`); coverage < 100 % or any issue goes back to the owner.
5. **Platform**: no `devops` agent; the lead or user owns monorepo, CI/CD and deployment.
6. **Handover**: `front` writes `gesture.md` (steps, implied data/rules/errors/edge cases/offline, expected result per step, stable test ids or accessible names); `front` and `back` confirm unit tests are ready.
7. **E2E gate**: `qa` writes the e2e from `gesture.md` and runs locally **only the impacted e2e** (`e2e-run`; the CI runs all on the PR). A failure goes to its owner with the steps; loop. **Only `qa` gives the PR go**, when the impacted e2e are green; nobody pushes before that go and the docs of step 8. **Several platforms: twin e2e** (same scenarios, numbers, names, steps, values, element ids), aligned by `qa`; no go while a twin is missing.
8. **Documentation, last step of every development (mandatory)**: after the `qa` go and **before** any push, `front` and `back` brief `documentalist` (files, routes, tables, screens, keys, tours, e2e touched); it updates AI and human docs (READMEs, guides, changelog), verifies, commits on the same branch, reports "docs done" to `qa` and the lead. Docs-only commits do not rerun the e2e. No docs, not done.
9. **Push, PR, CI until green** (lead, `pr-and-ci-follow`): push, open the PR on the default branch, follow the CI of the pushed commit; reds go to their owner, flaky tests are fixed. Merge only on the user's explicit yes.
10. **Promotion** (optional): `sales` writes `promotion/brief.md` (5+ ideas), asks `designer` for visuals and `front` for demo screens, makes scripts/copy/videos and the publication plan; the lead or user validates and publishes.
11. **Translation** (optional, any time): `translator` asks tone and sentence type, proposes alternatives when they truly differ, creates the skill of any new language or pair.
12. **Documentation on request**, and on an unknown project before a fix or feature: `documentalist` writes and refreshes `.agents/docs/` and the human docs.

## Bugfix mode (failing test or bug, behavior unchanged)

For a red e2e/unit test, a CI red or a bug report where the expected behavior is already specified (`gesture.md`, e2e, contract). A new or changed behavior, contract or screen is a feature (full flow). Doubt: ask the user.

1. **Triage by the lead, no relay**: read the failing log/trace, name the owner (`front`/`back` code, `qa` test), brief **that one agent** with test, trace, suspect files, docs to read. `qa` first only when "code or test wrong?" is open.
2. **Skipped**: need, design, contract, `gesture.md`, `translator`, `documentalist` skeleton, parallel build.
3. **Kept**: reproduce first (the red test is the proof); fix the cause, never weaken an assertion or widen a timeout without a cause; regression test when none covered the bug; unit tests of touched code (100 %, every condition and loop); `qa` reruns **only the impacted e2e** and Sonar on touched files.
4. **Flaky tests are always repaired**: a test red then green on rerun, in the loop, in the CI or noticed in passing, is a bug even if this change did not cause it. `qa` fixes the cause (`e2e-run` "Flaky tests": reproduce 10x, cause, fix, prove stable locally and in the CI) with `front`/`back` if the cause is in the code; same branch when small, else its own bugfix right after. Never "known flaky", skipped, retried or quarantined to get green. The report lists each flaky test and its status.
5. **Docs**: `documentalist` only when a documented behavior, route, table, key or gotcha changes; else one line in the commit message. A recurring cause (flaky, env) becomes a gotcha.
6. **Push** through `pr-and-ci-follow`. Stop and report: same failure after two fixes, more than five rounds, infrastructure cause; a fix that changes behavior switches to the full flow (tell the user).
7. A bug found while building a feature stays in that feature's loop (step 4 or 7); bugfix mode is for a red on a merged or PR'd change with no feature in progress.

**Feature, tests red locally**: no mode switch, the failure goes to its owner in the current step's loop. Unit/coverage/Sonar (step 4): `qa` -> `front`/`back` with test, trace, report; contract wrong: both agree, write `contract.md` first, then fix. E2E (step 7): `qa` decides code or test; code -> owner with scenario, steps, expected/actual, trace; test -> `qa`; mockup not buildable or gesture wrong -> `front` -> `designer`/`gesture.md`. After each fix `qa` reruns the impacted e2e plus what the fix touches. No push and no `documentalist` until green; after two failed fixes or five rounds the lead reports to the user.

**Green locally, red in the CI** (the local gate ran only the impacted e2e, on another environment). The lead reads the failed logs and classifies, then works in bugfix mode on the open PR:
- **Not selected locally**: `graph.yaml` is wrong: `qa` fixes test or sends code to the owner, `documentalist` fixes the graph entry.
- **Environment** (versions, ports, secrets, data, time zone, workers, slower runner): reproduce locally in the CI's conditions (same workers, fresh data, no cache) before changing anything; timing problems are flaky procedure, not a bigger timeout.
- **Sonar**: code owner, with the report; no exclusion without the lead's decision.
- **Infrastructure** (runner, secret, network, same failure on unrelated PRs): lead/user, never looped.
- **Flaky** (red then green, or red only in the CI): not a pass, not an infrastructure excuse; repaired as above and proven stable in the CI.

## Rules of the lead

- **Be brief with the user**: 3 to 5 lines per answer: what is done, what the user must decide (with a default), what comes next. No recap of earlier choices, no lists of what was not verified unless asked; images and paths carry the detail.
- **No code before the mockup is chosen**: steps 3-4 start after the user validated a mockup or skipped the design. A design change after code exists is a new step 2.
- **Parallelize independent work**: once the contract is written, `back`, `translator` (texts) and the `documentalist` skeleton start in the same message; only real dependencies are sequential.
- **A missing agent is announced at once**: an agent type not registered in the session (list frozen at start) is told to the user immediately and played by a general-purpose agent reading `.agents/agents/<name>.md`. No step is skipped silently.
- **Brief cold agents** with the files to read first, so nobody rediscovers the project.

## Rules for every agent

- **New project** (no code): the lead starts from `create-project`, then `need.md`; `front` and `back` propose technologies. After the lead's decision `documentalist` creates `.agents/docs/INDEX.md` and `graph.yaml` from `need.md` and the stack, marked `(planned)` until the code exists, enriched at step 8. Until then read `need.md`, `contract.md` and the feature folder.
- **Docs first, then the owner**: read `.agents/docs/INDEX.md`, `graph.yaml` and the feature folder before opening code (missing: ask `documentalist`). Not there: `SendMessage` the owner (`documentalist` for "how does X work / where is Y", `front`/`back` for their module). Scan the repository only when nobody knows.
- **AI-facing documents are in English** (`AGENTS.md`, agents, skills, docs, memory, prompts, agent messages); text people read follows the product language (`ai-docs-in-english`).
- **AI docs live in `<project>/.agents/docs/`** (never `docs/ai`, never loose in `docs/`): `INDEX.md`, `graph.yaml`, features, api, data, conventions, and the team workspace `team/<feature>/` (short, current, **local only: gitignored, never committed or pushed**; the lead adds `.agents/docs/team/` to `.gitignore`). Human docs stay where people expect them.
- **AI docs are machine-first and cheap to read** (maps, edge lists, tables; no diagrams or prose; token budget in `documentation-ai`); human docs keep diagrams and readable prose.
- **Ask instead of guessing**: short `SendMessage` with context to the owner of the answer; the answer is written back into the feature folder. Only business choices, budget and credentials go to the user, grouped.
- **Words go through `translator`**: any text a person reads (UI labels, errors, empty states, store listings, emails, release notes, scripts, captions, copy, legal wording) is written or reviewed by `translator` with tone, sentence type, audience, length limit; no unreviewed first draft. Code comments, logs and AI files are out of scope.
- **Empty-directory cleanup**: before handing off, remove directories left empty by your own adds/moves/deletes; leave unrelated ones.
- **Feature-first code and tests**: group production code by business feature, technical layers inside. Per module count files by architectural role (component, service, controller, helper, validator, repository, exception, DTO...): one file of a role stays in the module root; several move together into a role-named directory, never mixed. Page-specific front code stays in its page; front `core` holds only what every page shares. Unit tests mirror production directories; E2E specs sit in feature subdirectories under the runner's test root. Shared modules/helpers only for behavior reused by several features; dependencies point downward; never copy code.
- **Unit tests** (`front`, `back`): yours, for all code with behavior, in the same change. One nested group per public method, parameterized tests first, **every condition exercised** (branch, `&&`/`||` operand, ternary, optional chaining, null/empty check, error path, boundary). **Every loop** (`for`, `while`, `map`/`forEach`, streams, recursion, retries, pagination) gets at least **3 iterations**, plus the empty case and the exits (`break`, `continue`, limit).
- **Sonar setup** (`front`, `back`): when Sonar can analyse the language (ask `qa`), configure once per module: project key, `sonar.sources`, `sonar.tests`, the coverage report path, the coverage tool in the build. Never exclude files or lower a threshold yourself: ask `qa`. URL and token come from the lead through `qa`. Tell `qa` when ready.
- **Technology proposals**: for every new project/module the owner recommends the best-fit technology, compares options with concise pros/cons (need, stack, team, hosting, cost, performance, maintainability), records options and the lead's decision in the need or contract. Existing modules keep their stack unless a change is approved.
- **Done means verified**: built, unit tested, CI green on the PR. Report what was not verified.
- **Blocked on how to run or connect? A skill, never AGENTS.md**: global skill for generic tools, repo skill (`.agents/skills/`) for repo-specific things; look first, else ask the lead once, then write it (`run-and-access-skills`).
- **Load only the skills of your stack** ("Skill selection").

## Skill selection

Before writing or reviewing code, load **only** the matching skills (`.agents/skills/`):

1. The project's own `CLAUDE.md` / `AGENTS.md` and `.claude/skills` / `.agents/skills` win over the team skills.
2. Existing module: keep its stack, read that module's build files only. New project/module: the stack chosen by the lead, written in `need.md` or `contract.md`.
3. Kotlin back end: `kotlin` + `spring-boot` + `sql`, not `java`/`typescript`/`go`. A module in another language is for the agent working on it.

Names are `<x>-best-practices` unless noted.

| Found in the module | Skills |
|---|---|
| `pom.xml` / `build.gradle*` + `.java` | `java` |
| `.kt` (JVM) | `kotlin` |
| `spring-boot` dependency | `spring-boot` |
| Android (`com.android.application`, Compose) | `kotlin`, `ui-responsive-accessible-modular` |
| `package.json` (Node server, CLI, library) | `typescript` |
| `@nestjs/core` | + `nestjs` |
| `angular.json` / `@angular/core` | `typescript`, `angular` |
| `react` / `next` | `typescript`, `react` |
| `vue` / `nuxt` | `typescript`, `vue` |
| `svelte` / `@sveltejs/kit` | `typescript`, `svelte` |
| `pyproject.toml` / `requirements*.txt` | `python` |
| `go.mod` | `go` |
| `Cargo.toml` | `rust` |
| `*.csproj` / `*.sln` | `csharp-dotnet` |
| `composer.json` | `php` |
| `Gemfile` | `ruby-rails` |
| `CMakeLists.txt` / `*.pro` / `*.uproject` | `cpp` |
| `Package.swift` / `*.xcodeproj` | `swift` |
| `pubspec.yaml` | `dart-flutter` |
| SQL migrations, schema, queries | `sql` |
| shell / PowerShell scripts, CI `run:` steps | `shell-bash` |

Role skills:

| Who | Skills |
|---|---|
| every agent | `ai-docs-in-english` before writing any AI-read document; `run-and-access-skills` when blocked |
| lead, `qa` | `pr-and-ci-follow` |
| `front` | `git-branch-sync` |
| `designer`, `front` | `ui-responsive-accessible-modular` |
| `designer` | `design-mockup-variants` always; other `design-*` only when the need calls for them |
| `qa` | `sonar-report`, `e2e-run`, `e2e-live-progress`, `e2e-parallelism-init`, `e2e-<tool>-best-practices` + that tool's language skill. On request only: `sonar-<language>` |
| `sales` | `promo-communication` always, `promo-video` when a video is involved |
| `translator` | `translation-craft`, `language-<target>`, `language-<source>`, `translation-<source>-<target>`; missing ones via `translation-skill-factory`. Languages: `en`, `fr`, `ro`, `it`, `es`, `de` |
| `documentalist` | `documentation-ai`, `documentation-human`, only the needed `doc-*` (see its agent file); all refresh monthly |

## Sync of this file

- D:/projects/ia/team/AGENTS.md is the source. ~/.agents/AGENTS.md is a copy (no symlink without admin rights, no hardlink across drives) loaded by ~/.claude/CLAUDE.md. Whenever the source is modified, replace the copy with it in the same turn (Copy-Item D:\projects\ia\team\AGENTS.md ~/.agents/AGENTS.md) and check both hashes are equal.
