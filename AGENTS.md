# Feature team

Seven agents build a feature autonomously and question each other until the need is clear. Definitions: `.agents/agents/` (linked from `.claude/agents/`).

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, gestures, journeys, colors, design accessibility | 3-5 mockups per screen, then the chosen one |
| `front` | every front-end stack, its unit tests | the screen, the contract (with `back`), the gesture for `qa` |
| `back` | every back-end stack, SQL/NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, unit-test runs, Sonar report, the go for the PR | impacted e2e green, Sonar objective met (100 % coverage, 0 issue) before the PR |
| `sales` | positioning, promotion ideas, channels, copy, promo videos | brief, scripts, videos, publication plan (the lead publishes) |
| `translator` | translation as a native speaker of the target language; one skill per language and pair, refreshed monthly | translated texts and files, alternatives on request |
| `documentalist` | docs for AIs (`docs/ai/`, impact graph) and for humans (README, guides, ADR); picks the format | docs in sync with the code, updated as the last step of every development; answers "how does X work" with paths |

## Flow of a feature

```
need ─▶ designer ⇄ front ─▶ front ⇄ back (contract) ─▶ code + unit tests
     ─▶ qa go ─▶ documentalist docs ─▶ push + PR + CI until green (reds back to qa/back/front, flaky fixed) ─▶ merge on the user's yes ─▶ sales (optional)
     any agent can question any other one at any step
```

0. **Branches** (`front`, `git-branch-sync`): after a merged PR, check out the target branch, update it, delete the merged local branch (never `develop`, `release`, `main`). New feature: update the default branch, branch from it.
1. **Need**: the lead (main session) writes `docs/team/<feature>/need.md` (who, what, why, acceptance criteria, open questions).
2. **Design**: `designer` asks `front` for the current screens, proposes **3-5 mockups that really differ** (`design-mockup-variants`) with desktop and mobile PNGs shown inline; the lead (or the user) picks. Output `docs/team/<feature>/design/`.
3. **Contract**: `front` reads the mockup and agrees `docs/team/<feature>/contract.md` with `back` (+ OpenAPI/schema when relevant). A mockup element that cannot be built goes back to `designer` with the reason and a proposal.
4. **Build**: `back` and `front` implement in parallel; a contract change is agreed by both and written first. Each writes the unit tests of its code; `qa` runs them and the Sonar report (`sonar-report`); coverage < 100 % or any issue goes back to the owner.
5. **Platform**: no `devops` agent; the lead or the user owns monorepo, CI/CD and deployment.
6. **Handover to QA**: `front` writes `docs/team/<feature>/gesture.md` (steps, implied data/rules/errors/edge cases/offline, expected result per step); `front` and `back` confirm unit tests are ready.
7. **E2E gate**: `qa` writes the e2e from `gesture.md` and runs locally **only the impacted e2e** (impact graph `docs/ai/graph.yaml`; all when shared code or in doubt; the CI runs all on the PR). A failure goes to its owner with the steps; loop. **Only `qa` decides the PR can be opened**, when the impacted e2e are green; nobody pushes before that go and the docs of step 8. **Several platforms: twin e2e** (same scenarios, numbers, names, steps, expected values, element ids), kept aligned by `qa`; no go while a twin is missing.
8. **Documentation, last step of every development (mandatory)**: after the `qa` go and **before** any push, `front` and `back` brief `documentalist` (files, routes, tables, screens, keys, tours, e2e touched); it updates the AI docs (`docs/ai/`) **and** the human docs (READMEs, guides, changelog), verifies, commits on the same branch and reports "docs done" to `qa` and the lead. Docs-only commits do not rerun the e2e (`qa` confirms nothing else changed). No docs, not done.
9. **Push, PR and CI until green** (lead, `pr-and-ci-follow`): on a free machine, push, open the PR on the default branch, follow the CI of the pushed commit until all green. Reds go to their owner: tests/e2e to `qa` (code or test wrong?), code to `front`/`back`, Sonar to the code owner, infrastructure to the lead/user (never looped). After each fix `qa` reruns the impacted e2e, `documentalist` updates docs if behavior changed, the lead pushes and follows again. **A flaky test is not green**: `qa` finds and fixes the cause (with the owner if in code) until stable. Merge only on the user's explicit yes.
10. **Promotion** (optional, when asked or user-facing): `sales` writes `docs/team/<feature>/promotion/brief.md` (5+ ideas), asks `designer` for visuals and `front` for demo screens, makes scripts/copy/videos and the publication plan; the lead or user validates and publishes.
11. **Translation** (optional, any time): `translator` translates as a native, asks tone and sentence type, proposes alternatives when they truly differ, creates the skill of any new language or pair.
12. **Documentation on request** and on an unknown project before a fix or feature (step 8 covers the end of development): `documentalist` writes and refreshes `docs/ai/` and the human docs; any agent asks it "how does X work / where is Y" by `SendMessage` before scanning the repository.

## Rules for every agent

- **All AI-facing documents are in English**, whatever the language of the user or the product: `AGENTS.md`/`CLAUDE.md`, agent and skill files, `docs/ai/`, `docs/team/`, memory files, prompts, tool descriptions, messages between agents. Only text people read (UI, README, guides, store listings, replies to the user) follows the product/user language.
- **Ask instead of guessing.** Questions go to the owner of the answer (table above) by `SendMessage` (`to: "<agent>"`), short with context; the answer is written back into the feature folder. Only what no agent can answer (business choice, budget, credentials) goes to the user, grouped.
- **Words go through `translator`.** Any text a person will read (UI labels, errors, empty states, store listings, emails, release notes, scripts, captions, slogans, copy, business or legal wording) is written or reviewed by `translator` with tone, sentence type, audience and length limit; a first draft only shows intent and is never shipped unreviewed. It also translates into the other languages and returns what does not fit. Code comments, logs and AI-facing files are out of scope.
- **Empty-directory cleanup**: before handing off, remove directories left empty by your own adds/moves/deletes; leave unrelated ones unless a repository-wide cleanup is asked.
- **Feature-first code and tests**: group production code by business feature, technical layers inside each feature. Per module count files by architectural role (component, service, controller, helper, validator, repository, exception, DTO...): one file of a role stays in the module root; several move all together into a role-named directory, never mixed, per role and feature. Page-specific front code stays in its page; front `core` holds only what every page shares. Tests are organized by feature: unit tests mirror production module and role directories; E2E specs sit in feature subdirectories under the runner's test root. Shared back-end modules/test helpers only for behavior reused by several features; dependencies point downward; never copy code.
- **Technology proposals**: for every new project/module the owning agent recommends the best-fit technology (for a new project `front` and `back` each for their module), compares viable options with concise pros/cons (need, existing stack, team, hosting, cost, performance, maintainability), records options and the lead's decision in the need or contract before implementing. The lead decides; existing modules keep their stack unless a change is approved.
- **Load only the skills of the stack you work in** ("Skill selection"), never other languages'.
- **Done means verified**: built, unit tested, CI green on the PR. Report what was not verified.
- **AI docs are machine-first and cheap to read** (maps, edge lists, tables; no diagrams or prose for the eye; `docs/ai/graph.yaml` maps changed paths to features, tests, e2e; token budget in `documentation-ai`); human docs keep diagrams and readable prose and are not shortened.
- **Blocked on how to run or connect? A skill, never AGENTS.md**: global skill for generic tools (mvn, gradle, vault, sonar, docker, node/java versions), repo skill (`.agents/skills/`) for repo-specific things. Look for it first; else ask the lead once, then write it (`run-and-access-skills`).
- `docs/team/<feature>/` is the shared memory of the team: keep it short and up to date.

## Skill selection

Before writing or reviewing code, each agent finds its stack and loads **only** the matching skills (team skills in
`.agents/skills/`):

1. **The project's own rules first**: its `CLAUDE.md` / `AGENTS.md` and its `.claude/skills` / `.agents/skills` win over the team skills.
2. **Stack of the module you touch** (an existing project keeps its stack): read that module's build files only.
3. **New project or module**: the stack chosen by the lead from the owning agent's proposal, written in `need.md` or `contract.md`.
4. Load the skills of that stack from the table and nothing else: a Kotlin back end loads `kotlin` + `spring-boot` + `sql`, not
   `java`, `typescript` or `go`. A module in another language is the concern of the agent working on it.

| Found in the module | Skills to load |
|---|---|
| `pom.xml` / `build.gradle*` + `.java` sources | `java-best-practices` |
| `.kt` sources (JVM) | `kotlin-best-practices` |
| `spring-boot` dependency | `spring-boot-best-practices` |
| Android (`com.android.application`, Compose) | `kotlin-best-practices`, `ui-responsive-accessible-modular` |
| `package.json` (Node server, CLI, library) | `typescript-best-practices` |
| `@nestjs/core` | + `nestjs-best-practices` |
| `angular.json` / `@angular/core` | `typescript-best-practices`, `angular-best-practices` |
| `react` / `next` | `typescript-best-practices`, `react-best-practices` |
| `vue` / `nuxt` | `typescript-best-practices`, `vue-best-practices` |
| `svelte` / `@sveltejs/kit` | `typescript-best-practices`, `svelte-best-practices` |
| `pyproject.toml` / `requirements*.txt` | `python-best-practices` |
| `go.mod` | `go-best-practices` |
| `Cargo.toml` | `rust-best-practices` |
| `*.csproj` / `*.sln` | `csharp-dotnet-best-practices` |
| `composer.json` | `php-best-practices` |
| `Gemfile` | `ruby-rails-best-practices` |
| `CMakeLists.txt` / `*.pro` / `*.uproject` | `cpp-best-practices` |
| `Package.swift` / `*.xcodeproj` | `swift-best-practices` |
| `pubspec.yaml` | `dart-flutter-best-practices` |
| SQL migrations, schema or queries | `sql-best-practices` |
| shell / PowerShell scripts, CI `run:` steps | `shell-bash-best-practices` |

Role skills, whatever the language:
- every agent: `run-and-access-skills` as soon as it is blocked on how to run a command or connect to a service (global skill for generic tools, repo skill for repo-specific things).
- the lead and `qa`: `pr-and-ci-follow` (push, PR, CI followed until green, reds sent back to `qa`/`front`/`back`, flaky tests fixed, merge only on the user's yes); `qa` also the "Flaky tests" procedure of `e2e-run`.
- `front`: also `git-branch-sync` (branch cleanup after a merge, new feature branch).
- `designer`, `front`: `ui-responsive-accessible-modular`. `designer` also `design-mockup-variants` always, and only when the need calls
  for them the other `design-*` skills (`ux-journeys`, `color-palettes`, `typography-spacing`, `platform-guidelines`,
  `accessibility-review`, `mockup-render`, `microcopy-i18n`, `motion-feedback`).
- `qa`: `sonar-report`, `e2e-run`, `e2e-live-progress`, `e2e-parallelism-init`, and
  `e2e-<tool>-best-practices` for the e2e tool of the project or the one it recommends (`playwright`, `cypress`, `selenium`,
  `webdriverio`, `puppeteer`, `testcafe`, `squish`, `winappdriver`, `maestro`, `appium`, `espresso-compose`, `xcuitest`, `detox`,
  `flutter`, `api`, `bdd`, `accessibility`) with the language skill of that tool. **Only on request**, never by default:
  `sonar-<language>` (`java`, `kotlin`, `javascript-typescript`, `python`, `go`, `csharp`, `php`, `ruby`, `swift`, `cpp`,
  `dart-rust`) to answer `front` / `back` about the Sonar configuration and exclusions of a module.
- `sales`: `promo-communication` always, `promo-video` when a video is involved.
- `translator`: `translation-craft` always, `language-<target>` and `language-<source>`, and `translation-<source>-<target>`; a missing
  language or pair is created with `translation-skill-factory`. Available languages: `en`, `fr`, `ro`, `it`, `es`, `de`.
- `documentalist`: `documentation-ai` for AI docs and `documentation-human` for human docs, plus only the technology skills the job
  needs: `doc-code-analysis` (extract facts), `doc-mermaid` (diagrams), `doc-openapi-asyncapi` (API), `doc-database-schema` (data),
  `doc-architecture-c4-adr` (architecture, decisions), `doc-ai-context-files` (`AGENTS.md`, `llms.txt`), `doc-sites-markdown` (docs
  sites), `doc-graphify` (knowledge graph of a large codebase, license check first). All refresh monthly.
