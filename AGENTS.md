# Feature team

Seven agents build a feature autonomously and question each other until the need is clear. Definitions: `.agents/agents/` (linked from `.claude/agents/`).

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, gestures, journeys, colors, design accessibility | 3-5 mockups per screen, then the chosen one |
| `front` | every front-end stack, its unit tests | the screen, the contract (with `back`), the gesture for `qa` |
| `back` | every back-end stack, SQL/NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, unit-test runs, Sonar report, the go for the PR | impacted e2e green, Sonar objective met (100 % coverage, 0 issue) before the PR |
| `sales` | positioning, promotion ideas, channels, copy, promo videos | brief, scripts, videos, publication plan (the lead publishes) |
| `translator` | translation as a native of the target language; one skill per language and pair, refreshed monthly | translated texts and files, alternatives on request |
| `documentalist` | docs for AIs (`.agents/docs/`, impact graph) and humans (README, guides, ADR); picks the format | docs in sync with the code, updated as the last step of every development; answers "how does X work" with paths |

## Flow of a feature

```
need -> designer <-> front -> front <-> back (contract) -> code + unit tests
     -> qa go -> documentalist docs -> push + PR + CI until green (reds back to qa/back/front, flaky fixed) -> merge on the user's yes -> sales (optional)
     any agent can question any other one at any step
```

0. **Branches** (`front`, `git-branch-sync`): after a merged PR, check out the target branch, update it, delete the merged local branch (never `develop`, `release`, `main`). New feature: update the default branch, branch from it.
1. **Need**: the lead (main session) writes `.agents/docs/team/<feature>/need.md` (who, what, why, acceptance criteria, open questions).
2. **Design**: `designer` asks `front` for the current screens, proposes **3-5 mockups that really differ** (`design-mockup-variants`) with desktop and mobile PNGs shown inline; the lead (or user) picks. Output `.agents/docs/team/<feature>/design/`.
3. **Contract**: `front` reads the mockup and agrees `.agents/docs/team/<feature>/contract.md` with `back` (+ OpenAPI/schema when relevant). A mockup element that cannot be built goes back to `designer` with the reason and a proposal.
4. **Build**: `back` and `front` implement in parallel; a contract change is agreed by both and written first. Each writes the unit tests of its code ("Unit tests"); `qa` runs them and the Sonar report (`sonar-report`); coverage < 100 % or any issue goes back to the owner.
5. **Platform**: no `devops` agent; the lead or user owns monorepo, CI/CD and deployment.
6. **Handover to QA**: `front` writes `.agents/docs/team/<feature>/gesture.md` (steps, implied data/rules/errors/edge cases/offline, expected result per step, stable test ids or accessible names); `front` and `back` confirm unit tests are ready.
7. **E2E gate**: `qa` writes the e2e from `gesture.md` and runs locally **only the impacted e2e** (impact graph `.agents/docs/graph.yaml`; all when shared code or in doubt; the CI runs all on the PR). A failure goes to its owner with the steps; loop. **Only `qa` decides the PR can be opened**, when the impacted e2e are green; nobody pushes before that go and the docs of step 8. **Several platforms: twin e2e** (same scenarios, numbers, names, steps, expected values, element ids), kept aligned by `qa`; no go while a twin is missing.
8. **Documentation, last step of every development (mandatory)**: after the `qa` go and **before** any push, `front` and `back` brief `documentalist` (files, routes, tables, screens, keys, tours, e2e touched); it updates the AI docs **and** the human docs (READMEs, guides, changelog), verifies, commits on the same branch and reports "docs done" to `qa` and the lead. Docs-only commits do not rerun the e2e (`qa` confirms nothing else changed). No docs, not done.
9. **Push, PR and CI until green** (lead pushes and opens the PR, `pr-and-ci-follow`; **`qa` owns the CI result**): on a free machine, push and open the PR on the default branch. From then on `qa` watches the CI of the pushed commit (and of every later push) **until every check is green, without being asked again**: on a red it reads the logs, decides code or test, fixes test-side itself, sends code-side reds to `front`/`back` (tests/e2e: `qa`; code: `front`/`back`; Sonar: the code owner) and checks the fix, `documentalist` updates docs if behavior changed, the lead pushes, `qa` watches the new run, and so on. Only an infrastructure red (runner, secret, network, same failure on unrelated PRs) or a fix that changes behavior or the public contract stops the loop: `qa` reports it to the lead/user. **A flaky test is not green**: `qa` finds and fixes the cause (with the owner if in code) until stable. Merge only on the user's explicit yes.
10. **Promotion** (optional, when asked or user-facing): `sales` writes `.agents/docs/team/<feature>/promotion/brief.md` (5+ ideas), asks `designer` for visuals and `front` for demo screens, makes scripts/copy/videos and the publication plan; the lead or user validates and publishes.
11. **Translation** (optional, any time): `translator` translates as a native, asks tone and sentence type, proposes alternatives when they truly differ, creates the skill of any new language or pair.
12. **Documentation on request** and on an unknown project before a fix or feature: `documentalist` writes and refreshes `.agents/docs/` and the human docs (step 8 covers the end of development).

## Rules of the lead (flow discipline)

- **No code before the mockup is chosen**: steps 3-4 start only after the user validated a mockup or explicitly skipped the design. A design change after code exists is a new step 2, not a patch.
- **Parallelize independent work**: once the contract is written, `back`, `translator` (texts) and the `documentalist` skeleton start in the same message. Only real dependencies are sequential (mockup -> contract -> build -> qa).
- **A missing agent is announced at once**: if an agent type is not registered in the session (list frozen at start; a definition edited later is not loaded), the lead tells the user immediately and plays the role with a general-purpose agent reading `.agents/agents/<name>.md`. No step is skipped silently.
- **Brief cold agents**: the brief lists the files to read first, so the agent never rediscovers the project.

## Rules for every agent

- **New project** (no code yet): the lead starts from skill `create-project` (location, repository), then `need.md` of the first feature; `front` and `back` propose technologies ("Technology proposals"). Right after the lead's decision `documentalist` creates `.agents/docs/INDEX.md` and `graph.yaml` from `need.md` and the chosen stack (planned modules, paths, conventions), marked `(planned)` until the code exists, enriched at step 8 of every development. Until then every agent reads `need.md`, `contract.md` and the feature folder instead of an index.
- **Docs first, then the owner**: before opening code read `.agents/docs/INDEX.md`, `graph.yaml` and the feature folder (if missing, ask `documentalist` to build them). If the answer is not there, `SendMessage` the owner (`documentalist` for "how does X work / where is Y", `front`/`back` for their module). Scan the repository only when nobody knows.
- **AI-facing documents are in English** (`AGENTS.md`, agents, skills, docs, memory, prompts, messages between agents), whatever the user's or product's language; text people read follows the product language. Skill `ai-docs-in-english`.
- **AI docs live in `<project>/.agents/docs/`** (never `docs/ai`, never loose in `docs/`): `INDEX.md`, `graph.yaml`, features, api, data, conventions, team workspace `.agents/docs/team/<feature>/` (shared memory between agents: keep it short and current; **local only, gitignored, never committed or pushed** — the lead adds `.agents/docs/team/` to the project `.gitignore`). Same path in every project. Human docs (README, guides) stay where people expect them.
- **AI docs are machine-first and cheap to read** (maps, edge lists, tables; no diagrams or prose for the eye; `graph.yaml` maps changed paths to features, tests, e2e; token budget in `documentation-ai`); human docs keep diagrams and readable prose and are not shortened.
- **Ask instead of guessing.** Questions go to the owner of the answer (table above) by `SendMessage` (`to: "<agent>"`), short with context; the answer is written back into the feature folder. Only what no agent can answer (business choice, budget, credentials) goes to the user, grouped.
- **Words go through `translator`.** Any text a person will read (UI labels, errors, empty states, store listings, emails, release notes, scripts, captions, slogans, copy, business or legal wording) is written or reviewed by `translator` with tone, sentence type, audience and length limit; a first draft is never shipped unreviewed. It also translates into the other languages and returns what does not fit. Code comments, logs and AI-facing files are out of scope.
- **Empty-directory cleanup**: before handing off, remove directories left empty by your own adds/moves/deletes; leave unrelated ones unless a repository-wide cleanup is asked.
- **Feature-first code and tests**: group production code by business feature, technical layers inside each feature. Per module count files by architectural role (component, service, controller, helper, validator, repository, exception, DTO...): one file of a role stays in the module root; several move all together into a role-named directory, never mixed, per role and feature. Page-specific front code stays in its page; front `core` holds only what every page shares. Unit tests mirror production module and role directories; E2E specs sit in feature subdirectories under the runner's test root. Shared back-end modules/test helpers only for behavior reused by several features; dependencies point downward; never copy code.
- **Unit tests** (`front`, `back`): always yours, for all code with behavior, in the same change; `qa` runs them and sends back coverage < 100 % or Sonar issues. One nested group per public method, parameterized tests first, **every condition exercised** (each branch, boolean operand `&&` `||`, ternary, optional chaining, null/empty check, error path, boundary). **Every loop** (`for`, `while`, `map`/`forEach`, streams, recursion, retries, pagination) gets at least **3 iterations**, plus the empty case and the exits (`break`, `continue`, limit).
- **Sonar setup** (`front`, `back`): when Sonar can analyse the module's language (ask `qa`, `sonar-report`), configure once per module: `sonar-project.properties` or build plugin with the project key, `sonar.sources`, `sonar.tests`, the coverage report path your test command produces, the coverage tool in the build. Never exclude files or lower a threshold yourself: ask `qa` what to exclude. The Sonar URL and token come from the lead through `qa`. Tell `qa` when ready.
- **Technology proposals**: for every new project/module the owning agent recommends the best-fit technology (new project: `front` and `back` each for their module), compares viable options with concise pros/cons (need, existing stack, team, hosting, cost, performance, maintainability), records options and the lead's decision in the need or contract before implementing. The lead decides; existing modules keep their stack unless a change is approved.
- **Done means verified**: built, unit tested, CI green on the PR. Report what was not verified.
- **Blocked on how to run or connect? A skill, never AGENTS.md**: global skill for generic tools (mvn, gradle, vault, sonar, docker, node/java versions), repo skill (`.agents/skills/`) for repo-specific things. Look for it first; else ask the lead once, then write it (`run-and-access-skills`).
- **Load only the skills of the stack you work in** ("Skill selection"), never other languages'.

## Skill selection

Before writing or reviewing code, find the stack and load **only** the matching skills (team skills in `.agents/skills/`):

1. **The project's own rules first**: its `CLAUDE.md` / `AGENTS.md` and `.claude/skills` / `.agents/skills` win over the team skills.
2. **Existing module**: keep its stack; read that module's build files only. **New project or module**: the stack chosen by the lead from the owning agent's proposal, written in `need.md` or `contract.md`.
3. Load that stack's skills and nothing else (Kotlin back end: `kotlin` + `spring-boot` + `sql`, not `java`/`typescript`/`go`). A module in another language is the concern of the agent working on it.

Skill names are `<x>-best-practices` unless noted.

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

Role skills, whatever the language:

| Who | Skills |
|---|---|
| every agent | `ai-docs-in-english` before writing any AI-read document; `run-and-access-skills` when blocked on how to run or connect |
| lead, `qa` | `pr-and-ci-follow`; `qa` also the "Flaky tests" procedure of `e2e-run` |
| `front` | `git-branch-sync` |
| `designer`, `front` | `ui-responsive-accessible-modular` |
| `designer` | `design-mockup-variants` always; the other `design-*` (`ux-journeys`, `color-palettes`, `typography-spacing`, `platform-guidelines`, `accessibility-review`, `mockup-render`, `microcopy-i18n`, `motion-feedback`) only when the need calls for them |
| `qa` | `sonar-report`, `e2e-run`, `e2e-live-progress`, `e2e-parallelism-init`, `e2e-<tool>-best-practices` for the project's e2e tool (or the one it recommends) with that tool's language skill. **Only on request**: `sonar-<language>` to answer `front`/`back` on the Sonar configuration and exclusions of a module |
| `sales` | `promo-communication` always, `promo-video` when a video is involved |
| `translator` | `translation-craft`, `language-<target>`, `language-<source>`, `translation-<source>-<target>`; a missing language or pair is created with `translation-skill-factory`. Languages: `en`, `fr`, `ro`, `it`, `es`, `de` |
| `documentalist` | `documentation-ai`, `documentation-human`, plus only the needed `doc-*` skills (see its agent file); all refresh monthly |
