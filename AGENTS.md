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

## Flow of a feature (summary; the lead loads skill `team-lead` for the details)

```
need -> designer <-> front -> front <-> back (contract) -> code + unit tests
     -> qa go -> documentalist docs -> push + PR + CI until green -> merge on the user's yes -> sales (optional)
     any agent can question any other one at any step
```

0 branches (`git-branch-sync`) · 1 need (`.agents/docs/team/<feature>/need.md`) · 2 design: 3-5 really different mockups, the user picks (no code before) · 3 contract `front`+`back` · 4 build in parallel, each its unit tests (100 % coverage, 0 Sonar issue) · 5 platform = lead/user · 6 handover `gesture.md` · 7 e2e gate: `qa` runs only the impacted e2e, only `qa` gives the PR go (twin e2e when several platforms) · 8 docs by `documentalist` before any push · 9 push, PR, CI until green, merge only on the user's yes · 10 promotion (optional) · 11 translation (optional) · 12 docs on request.

Red e2e/unit/CI/flaky test with behavior already specified = bugfix mode (lead loads `team-bugfix-mode`). Lead: be brief (3-5 lines), start parity clients together, batch user feedback, parallelize independent work, announce a missing agent at once, brief cold agents with the files to read, keep agents short-lived with few images and quiet logs (all in `team-lead`). `front` keeps the screen library `.agents/docs/screens/` (re-captures only the pages it touches).

## Rules for every agent

- **New project** (no code): the lead starts from `create-project`, then `need.md`; `front` and `back` propose technologies. After the lead's decision `documentalist` creates `.agents/docs/INDEX.md` and `graph.yaml` from `need.md` and the stack, marked `(planned)` until the code exists, enriched at step 8.
- **Code to locate, docs for the rules** (measured on 3+3 questions: reading INDEX + graph + feature file up front cost +26 % tokens to find where something is; the light mode cost -25 % vs the full read and found the repo rules the code does not show). *Locate* ("where / how does X work"): grep the names in the code first; open `.agents/docs/` only if that fails. *Change code*: read `.agents/docs/INDEX.md` and `gotchas.md` (top section "Repo rules a PR must satisfy"), `grep` (do not read in full) `graph.yaml` for your module's impact edges, open the feature file only if a doubt remains; never read the whole docs tree. Docs missing: ask `documentalist`; docs wrong or stale: the code wins, tell `documentalist`. Not found anywhere: `SendMessage` the owner (`documentalist` for "how does X work / where is Y", `front`/`back` for their module). Scan the repository only when nobody knows.
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
- **Tests always run in English** (every type: unit, e2e web and Android, API, Sonar runs): language `en` / `en-US` set explicitly by the test (locale of the browser context, `I18nService.select('en')`, emulator language, `LANG`/`LC_ALL=C.UTF-8` with `TZ`), never read from the machine or the runner; assertions use the English texts or, better, stable test ids. Text-specific tests of another language (translations) set that language explicitly and reset it after.
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
| lead, `qa` | `pr-and-ci-follow`, `ci-parity-before-push`; lead: `team-lead` (at the start of any feature, bug or PR), `team-bugfix-mode` |
| `front` | `git-branch-sync` |
| `designer`, `front` | `ui-responsive-accessible-modular` |
| `front`, `qa`, lead | `guided-tours` only if the project has guided tours (always complete for each new feature); new project: `front` asks the lead whether to add them |
| `designer` | `design-mockup-variants` always; other `design-*` only when the need calls for them |
| `qa` | `sonar-report`, `e2e-run`, `e2e-live-progress`, `e2e-parallelism-init`, `e2e-<tool>-best-practices` + that tool's language skill. On request only: `sonar-<language>` |
| `sales` | `promo-communication` always, `promo-video` when a video is involved |
| `translator` | `translation-craft`, `language-<target>`, `language-<source>`, `translation-<source>-<target>`; missing ones via `translation-skill-factory`. Languages: `en`, `fr`, `ro`, `it`, `es`, `de` |
| `documentalist` | `documentation-ai`, `documentation-human`, only the needed `doc-*` (see its agent file); all refresh monthly |

