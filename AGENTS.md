# Feature team

Six agents that build a feature together, autonomously, and question each other until the need is clear. Definitions in
`.agents/agents/` (linked from `.claude/agents/`).

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, business gestures, journeys, colors, accessibility of the design | 3 to 5 mockups per screen, then the chosen one |
| `front` | every front-end framework and language, its unit tests | the screen built from the mockup, the contract (with `back`), the business gesture for `qa` |
| `back` | every back-end framework and language, SQL and NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, running the unit tests, the Sonar report, the go for the pull request | every e2e green and Sonar objective reached (100 % coverage, 0 issue) before the PR; the whole feature re-run on every deployment |
| `sales` | positioning, promotion ideas, channels, communication, promotional videos and montage | a promotion brief, scripts and copy, videos, a publication plan (the lead publishes), indicators |
| `translator` | translation between languages as a native speaker of the target language; one skill per language and per language pair, refreshed monthly; creates the skill of any new language or pair | translated texts and translation files, with alternatives when asked |

## Flow of a feature

```
need ─▶ designer ⇄ front ─▶ front ⇄ back (contract) ─▶ front + back: code + unit tests
     ─▶ qa: every e2e green + Sonar objective = go ─▶ pull request ─▶ deploy ─▶ qa: whole feature again ─▶ sales (optional)

     any agent can question any other one at any step
```

0. **Branches (handled by `front`, skill `git-branch-sync`)**: once a pull request is merged, `front` checks out the PR target
   branch, updates it, and deletes the merged local branch (never `develop`, `release` or `main`). For every new feature, `front`
   updates the default branch first and creates the feature branch from it.
1. **Need**: the lead (main session) writes `docs/team/<feature>/need.md`: who, what, why, acceptance criteria, open questions.
2. **Design**: `designer` asks `front` for the current screens, then proposes **3 to 5 mockups that really differ**
   (`design-mockup-variants`) with rendered desktop and mobile PNG screenshots, shown inline before the lead (or the user when the
   choice is theirs) picks one. Output in `docs/team/<feature>/design/`.
3. **Contract**: `front` reads the chosen mockup and agrees the interface contract with `back`: `docs/team/<feature>/contract.md`
   (+ `openapi.yaml` / schema when relevant). A mockup element that cannot be built goes back to `designer` with the reason and a proposal.
4. **Build**: `back` and `front` implement in parallel against the contract; a contract change is agreed by both and written in
   `contract.md` first. **Unit tests belong to `front` and `back`**: each writes those of its own code (coverage asked by the
   project); **`qa` runs them, asks SonarQube and reports** (`sonar-report`). Coverage below 100 % or any issue goes back to the
   owner of the code, who fixes it.
5. **Platform**: no `devops` agent (disabled): the lead or the user sets up the monorepo, the CI/CD and the deployment.
6. **Handover to QA**: `front` writes `docs/team/<feature>/gesture.md`: the business gesture step by step, what it implies (data,
   rules, errors, edge cases, offline) and the expected result of each step; `front` and `back` confirm their unit tests are ready.
7. **E2E gate before the pull request**: `qa` writes the e2e from `gesture.md` and runs **every e2e test of the project** against
   the build of the branch. A failure goes to its owner (`front` or `back`) with the steps to reproduce, and the loop restarts.
   **Only `qa` decides that the pull request can be opened**, and only when every e2e is green; nobody pushes for a PR or opens one before that go.
8. **After deployment**: `qa` runs the whole feature again on the deployed environment and reports.
9. **Promotion (optional, when the lead asks or the feature is user-facing)**: `sales` writes `docs/team/<feature>/promotion/brief.md`
   (at least 5 ideas), asks `designer` for visuals and `front` for demo screens and data, makes scripts, copy and videos, and
   prepares the publication plan; the lead or the user validates and publishes.
10. **Translation (optional, any time a text or a language is needed)**: `translator` translates as a native speaker of the target
   language, asks the tone and the type of sentence, proposes several renderings when they really differ, and creates the skill of
   any new language or pair on request.

## Rules for every agent

- **Ask instead of guessing.** A question goes to the agent who owns the answer (table above) through `SendMessage` (`to: "<agent>"`),
  short and with the context needed; the answer is written back into the feature folder so that nobody asks twice. Only questions
  no agent can answer (business choice, budget, credentials) go to the user, grouped.
- **Empty-directory cleanup**: before handing off repository changes, check directories affected by files you added, moved, or
  deleted. Remove directories left empty by your changes; do not remove unrelated or pre-existing empty directories unless the
  task explicitly asks for a repository-wide cleanup.
- **Feature-first code and tests**: keep front-end and back-end production code grouped by business functionality, with technical
  layers scoped inside each feature rather than global layer-only directories. Within each module, count files by architectural
  role (component, service, controller, helper, validator, repository, exception, DTO, etc.), not by extension. Keep one file of
  a role directly in the module root; when there are multiple files of that role, move all of them into a module-local
  role-named directory. Apply this independently to every role and feature; never mix root-level and nested files of the same
  role. Keep page-specific front-end code inside its page feature; front-end `core` contains only code shared by every page.
  Organize unit and end-to-end tests by feature; unit tests mirror the production module and role directories, and E2E specs live
  in feature-specific subdirectories under the test runner's configured test root. Shared back-end modules and test helpers are
  only for behavior reused by multiple features; dependencies point downward and code is never copied.
- **Technology proposals**: for every new project and every new module, the owning agent recommends the best-fit technology;
  for a new project, `front` and `back` each make a recommendation for their module. Compare multiple viable options when
  practical, with concise pros and cons grounded in the need, existing stack and integration, team, hosting, cost, performance,
  and maintainability. Record the options and lead's decision in the feature need or contract before implementation. The lead
  decides. Existing modules keep their stack and conventions unless a change is approved.
- **AI-facing files**: write instructions, skills, and configuration in English; product-facing text follows the project language.
- **Load only the skills of the stack you work in** ("Skill selection"): never the skills of other languages.
- **Done means verified**: built, unit tested, e2e green on the deployed environment. Report what was not verified.
- `docs/team/<feature>/` is the shared memory of the team: keep it short and up to date.

## Skill selection

Before writing or reviewing code, each agent finds its stack and loads **only** the matching skills (team skills in
`.agents/skills/`, the user's global ones in `~/.agents/skills/`):

1. **The project's own rules first**: its `CLAUDE.md` / `AGENTS.md` and its `.claude/skills` / `.agents/skills` win over the team skills.
2. **Stack of the module you touch** (an existing project keeps its stack): read that module's build files only.
3. **New project or module**: the stack chosen by the lead from the owning agent's proposal, written in `need.md` or `contract.md`.
4. Load the skills of that stack from the table and nothing else: a Kotlin back end loads `kotlin` + `spring-boot` + `sql`, not
   `java`, `typescript` or `go`. A module in another language is the concern of the agent working on it.

| Found in the module | Skills to load |
|---|---|
| `pom.xml` / `build.gradle*` + `.java` sources | `java-best-practices` (+ `java-version`) |
| `.kt` sources (JVM) | `kotlin-best-practices` (+ `java-version`) |
| `spring-boot` dependency | `spring-boot-best-practices` |
| Android (`com.android.application`, Compose) | `kotlin-best-practices`, `android-compose-architecture`, `android-tooling` |
| `package.json` (Node server, CLI, library) | `typescript-best-practices`, `node-api-architecture` (server code), `node-version` |
| `@nestjs/core` | + `nestjs-best-practices` |
| `angular.json` / `@angular/core` | `typescript-best-practices`, `angular-best-practices` (+ `pmeig-ngb-libs` when `@pmeig/*` is used) |
| `react` / `next` | `typescript-best-practices`, `react-best-practices` |
| `vue` / `nuxt` | `typescript-best-practices`, `vue-best-practices` |
| `svelte` / `@sveltejs/kit` | `typescript-best-practices`, `svelte-best-practices` |
| `pyproject.toml` / `requirements*.txt` | `python-best-practices` (+ `python`) |
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
- `front`: also `git-branch-sync` (branch cleanup after a merge, new feature branch).
- `designer`, `front`: `ui-responsive-accessible-modular`. `designer` also `design-mockup-variants` always, and only when the need calls
  for them the other `design-*` skills (`ux-journeys`, `color-palettes`, `typography-spacing`, `platform-guidelines`,
  `accessibility-review`, `mockup-render`, `microcopy-i18n`, `motion-feedback`).
- `qa`: `sonar-report`, `e2e-run`, `e2e-live-progress`, `e2e-parallelism-init`, `feature-e2e-loop`, `flaky-tests`, and
  `e2e-<tool>-best-practices` for the e2e tool of the project or the one it recommends (`playwright`, `cypress`, `selenium`,
  `webdriverio`, `puppeteer`, `testcafe`, `squish`, `winappdriver`, `maestro`, `appium`, `espresso-compose`, `xcuitest`, `detox`,
  `flutter`, `api`, `bdd`, `accessibility`) with the language skill of that tool. **Only on request**, never by default:
  `sonar-<language>` (`java`, `kotlin`, `javascript-typescript`, `python`, `go`, `csharp`, `php`, `ruby`, `swift`, `cpp`,
  `dart-rust`) to answer `front` / `back` about the Sonar configuration and exclusions of a module.
- `sales`: `promo-communication` always, `promo-video` when a video is involved.
- `translator`: `translation-craft` always, `language-<target>` and `language-<source>`, and `translation-<source>-<target>`; a missing
  language or pair is created with `translation-skill-factory`. Available languages: `en`, `fr`, `ro`, `it`, `es`, `de`.
