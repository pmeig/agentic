# Feature team

Seven agents build a feature autonomously and question each other until the need is clear. Definitions: `.agents/agents/` (linked from `.claude/agents/`).

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, gestures, journeys, colors, design accessibility | 3-5 mockups per feature and page, then the chosen one |
| `front` | every front-end stack, its unit tests, the screenshot library | the screen, the contract (with `back`), the gesture for `qa` |
| `back` | every back-end stack, SQL/NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, unit-test runs, Sonar report, the go for the PR | impacted e2e green, Sonar met (100 % coverage, 0 issue) before the PR |
| `sales` | positioning, promotion, channels, copy, promo videos | brief, scripts, videos, publication plan (the lead publishes) |
| `translator` | translation as a native; skill per language and pair, refreshed monthly | translated texts and files, alternatives on request |
| `documentalist` | AI docs (`.agents/docs/`, impact graph) and human docs (README, guides, ADR) | docs in sync with the code (last step of every development); answers "how does X work" with paths |

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

## Rules for every agent

- **New project** (no code): the lead starts from `create-project`, then `need.md`; `front` and `back` propose technologies. After the lead's decision `documentalist` creates `.agents/docs/INDEX.md` and `graph.yaml` from `need.md` and the stack, marked `(planned)` until the code exists, enriched at step 8.
- **Docs first, then the owner**: read `.agents/docs/INDEX.md`, `graph.yaml` and the feature folder before opening code (missing: ask `documentalist`). Not there: `SendMessage` the owner (`documentalist` for "how does X work / where is Y", `front`/`back` for their module). Scan the repository only when nobody knows.
- **AI-facing documents are in English** (`AGENTS.md`, agents, skills, docs, memory, prompts, agent messages); text people read follows the product language (`ai-docs-in-english`).
- **AI docs live in `<project>/.agents/docs/`** (never `docs/ai`, never loose in `docs/`): `INDEX.md`, `graph.yaml`, features, api, data, conventions, `screens/`, and the team workspace `team/<feature>/` (short, current, **local only: gitignored, never committed or pushed**; the lead adds `.agents/docs/team/` to `.gitignore`). Human docs stay where people expect them.
- **AI docs are machine-first and cheap to read** (maps, edge lists, tables; no diagrams or prose; budget in `documentation-ai`); human docs keep diagrams and readable prose.
- **Ask instead of guessing**: short `SendMessage` with context to the owner of the answer; the answer is written back into the feature folder. Only business choices, budget and credentials go to the user, grouped.
- **Words go through `translator`**: any text a person reads (UI labels, errors, empty states, store listings, emails, release notes, scripts, captions, copy, legal wording) is written or reviewed by `translator` with tone, sentence type, audience, length limit. Code comments, logs and AI files are out of scope.
- **Empty-directory cleanup**: before handing off, remove directories left empty by your own adds/moves/deletes; leave unrelated ones.
- **Feature-first code and tests**: group production code by business feature, technical layers inside. Per module count files by architectural role (component, service, controller, helper, validator, repository, exception, DTO...): one file of a role stays in the module root; several move together into a role-named directory, never mixed. Page-specific front code stays in its page; front `core` holds only what every page shares. Unit tests mirror production directories; E2E specs sit in feature subdirectories under the runner's test root. Shared modules/helpers only for behavior reused by several features; dependencies point downward; never copy code.
- **Unit tests** (`front`, `back`): yours, for all code with behavior, in the same change. One nested group per public method, parameterized tests first, **every condition exercised** (branch, `&&`/`||` operand, ternary, optional chaining, null/empty check, error path, boundary). **Every loop** (`for`, `while`, `map`/`forEach`, streams, recursion, retries, pagination) gets at least **3 iterations**, plus the empty case and the exits (`break`, `continue`, limit).
- **Run little while building**: only the impacted specs (`vitest --related`, one Gradle test class); the full suite, build and coverage once at the end.
- **Coverage target = what the CI gate measures** (read the workflow, ask `qa`): a measured module gets 100 %; an unmeasured one gets every logic condition tested in pure functions, no hours on compiler-generated branches (Compose) or a coverage tool.
- **Container tools are installed once** (JDK, Gradle, Android SDK, browsers, local database): record the commands in the repo's SessionStart hook or a repo skill, never reinstall per agent.
- **Sonar setup** (`front`, `back`): when Sonar can analyse the language (ask `qa`), configure once per module: project key, `sonar.sources`, `sonar.tests`, coverage report path, coverage tool in the build. Never exclude files or lower a threshold yourself: ask `qa`. URL and token come from the lead through `qa`.
- **Technology proposals**: for every new project/module the owner recommends the best-fit technology, compares options (need, stack, team, hosting, cost, performance, maintainability) with concise pros/cons, records options and the lead's decision in the need or contract. Existing modules keep their stack unless a change is approved.
- **Done means verified**: built, unit tested, CI green on the PR. Report what was not verified.
- **Blocked on how to run or connect? A skill, never AGENTS.md**: global skill for generic tools, repo skill (`.agents/skills/`) for repo-specific things; look first, else ask the lead once, then write it (`run-and-access-skills`).

## Skill selection

Load **only** the skills of your stack (`.agents/skills/`) before writing or reviewing code:

1. The project's own `CLAUDE.md` / `AGENTS.md` and `.claude/skills` / `.agents/skills` win over the team skills.
2. Existing module: keep its stack, read that module's build files only. New project/module: the stack chosen by the lead, in `need.md` or `contract.md`.
3. Kotlin back end: `kotlin` + `spring-boot` + `sql`, not `java`/`typescript`/`go`.

Names are `<x>-best-practices` unless noted.

Found in the module -> skills: `pom.xml`/`build.gradle*` + `.java` java; `.kt` (JVM) kotlin; `spring-boot` dependency spring-boot; Android (`com.android.application`, Compose) kotlin + ui-responsive-accessible-modular; `package.json` (Node, CLI, library) typescript; `@nestjs/core` + nestjs; `angular.json`/`@angular/core` typescript + angular; `react`/`next` typescript + react; `vue`/`nuxt` typescript + vue; `svelte`/`@sveltejs/kit` typescript + svelte; `pyproject.toml`/`requirements*.txt` python; `go.mod` go; `Cargo.toml` rust; `*.csproj`/`*.sln` csharp-dotnet; `composer.json` php; `Gemfile` ruby-rails; `CMakeLists.txt`/`*.pro`/`*.uproject` cpp; `Package.swift`/`*.xcodeproj` swift; `pubspec.yaml` dart-flutter; SQL migrations, schema, queries sql; shell/PowerShell scripts, CI `run:` steps shell-bash.

| Who | Role skills |
|---|---|
| every agent | `ai-docs-in-english` before writing any AI-read document; `context-handoff` at the start and end of its package; `run-and-access-skills` when blocked |
| lead, `qa` | `pr-and-ci-follow`; lead: `team-bugfix-mode` |
| `front` | `git-branch-sync` |
| `designer`, `front` | `ui-responsive-accessible-modular` |
| `designer` | `design-mockup-variants` always; other `design-*` only when the need calls for them |
| `qa` | `sonar-report`, `e2e-run`, `e2e-live-progress`, `e2e-parallelism-init`, `redroid` (Android e2e devices in Docker), `e2e-<tool>-best-practices` + that tool's language skill. On request only: `sonar-<language>` |
| `sales` | `promo-communication` always, `promo-video` when a video is involved |
| `translator` | `translation-craft`, `language-<target>`, `language-<source>`, `translation-<source>-<target>`; missing ones via `translation-skill-factory`. Languages: `en`, `fr`, `ro`, `it`, `es`, `de` |
| `documentalist` | `documentation-ai`, `documentation-human`, only the needed `doc-*` (see its agent file); all refresh monthly |

## Sync of this file

D:/projects/ia/team/AGENTS.md is the source; ~/.agents/AGENTS.md is a copy (no symlink without admin rights, no hardlink across drives) loaded by ~/.claude/CLAUDE.md. Whenever the source changes, replace the copy in the same turn (`Copy-Item D:\projects\ia\team\AGENTS.md ~/.agents/AGENTS.md`) and check both hashes are equal.
