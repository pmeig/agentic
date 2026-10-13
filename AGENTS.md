# Feature team

Five agents that build a feature together, autonomously, and question each other until the need is clear. Definitions in
`.agents/agents/` (linked from `.claude/agents/`).

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, business gestures, user journeys, colors, accessibility of the design | several mockups per screen, then the chosen one |
| `front` | every front-end framework and language, its unit tests | the screen built from the mockup, the interface contract (with `back`), the business gesture handed to `qa` |
| `back` | every back-end framework and language, SQL and NoSQL, its unit tests | the API and storage behind the contract |
| `devops` | monorepo layout, CI/CD | a repository and pipelines that build, test and deploy every module |
| `qa` | end-to-end tests, the go for the pull request | every e2e green before the PR (only `qa` opens the gate), the whole feature re-run on every deployment |

## Flow of a feature

```
need ─▶ designer ⇄ front ─▶ front ⇄ back (contract) ─▶ front + back: code + unit tests (green)
     ─▶ devops (repo, CI/CD) ─▶ qa: every e2e green = go ─▶ pull request ─▶ deploy ─▶ qa: whole feature again

     any agent can question any other one at any step
```

1. **Need**: the lead (main session) writes `docs/team/<feature>/need.md`: who, what, why, acceptance criteria, open questions.
2. **Design**: `designer` asks `front` for the current screens of the app, then proposes **at least 3 mockups**; the lead (or the
   user when the choice is theirs) picks one. Output in `docs/team/<feature>/design/`.
3. **Contract**: `front` reads the chosen mockup, agrees the interface contract with `back`; output
   `docs/team/<feature>/contract.md` (+ `openapi.yaml` / schema when relevant). A mockup element that cannot be built goes back to
   `designer` with the reason and a proposal.
4. **Build**: `back` and `front` implement in parallel against the contract; any change of the contract is agreed by both and
   written in `contract.md` first. **Unit tests belong to `front` and `back`**: each writes and runs the unit tests of its own
   code, and hands over only when they are all green (with the coverage asked by the project).
5. **Platform**: `devops` sets up or adapts the monorepo and the CI/CD for the technologies chosen; the pipeline runs every unit and
   e2e test and deploys.
6. **Handover to QA**: `front` writes `docs/team/<feature>/gesture.md`: the business gesture step by step, what it implies (data,
   rules, errors, edge cases, offline) and the expected result of each step; `front` and `back` confirm their unit tests are green.
7. **E2E gate before the pull request**: `qa` writes the e2e from `gesture.md` and runs **every e2e test of the project** (not
   only the new ones) against the build of the branch. A failure goes to its owner (`front`, `back` or `devops`) with the steps
   to reproduce, and the loop starts again. **Only `qa` decides that the pull request can be opened**, and only when every e2e is
   green; nobody pushes for a PR or opens one before that go.
8. **After deployment**: once merged and deployed, `qa` runs the whole feature again on the deployed environment and reports.

## Rules for every agent

- **Ask instead of guessing.** A question goes to the agent who owns the answer (table above) through `SendMessage` (`to: "<agent>"`),
  short and with the context needed; the answer is written back into the feature folder (`need.md`, `contract.md`, ...) so that
  nobody asks twice. Only questions no agent can answer (business choice, budget, credentials) go to the user, grouped.
- **Modular code**: one folder per page / feature, a shared `core` sorted by kind of feature, layered back end
  (controller → service → repository), dependencies only pointing downward, nothing copied twice.
- **Choose the technology on purpose**: when a project has none yet, `front` and `back` each propose the most adequate stack with
  2-3 lines of reasons (needs, team, hosting, performance), the lead decides; an existing project keeps its stack.
- **Load only the skills of the stack you work in** (see "Skill selection" below): never the skills of other languages.
- **Done means verified**: built, unit tested, e2e green on the deployed environment. Report what was not verified.
- The feature folder `docs/team/<feature>/` is the shared memory of the team: keep it short and up to date.

## Skill selection

Before writing or reviewing code, each agent finds its stack and loads **only** the matching skills (team skills in
`.agents/skills/`, the user's global ones in `~/.agents/skills/`):

1. **The project's own rules first**: its `CLAUDE.md` / `AGENTS.md` and its `.claude/skills` / `.agents/skills` win over the team skills.
2. **Stack of the module you touch** (an existing project keeps its stack): read the build files of that module only.
3. **New project**: the stack chosen by the lead (proposal of `front` / `back`), written in `docs/team/<feature>/need.md`.
4. Load the skills of that stack from the table, and nothing else: a Kotlin back end loads `kotlin` + `spring-boot` + `sql`,
   not `java`, `typescript` or `go`. A module in another language (e.g. the Angular web of the same monorepo) is the concern of
   the agent working on it.

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

Role skills, loaded whatever the language: `designer` and `front` → `ui-responsive-accessible-modular`; `devops` →
`monorepo-layout`, `github-actions-cicd`, `docker`; `qa` → `feature-e2e-loop`, `flaky-tests` (+ the language skill of the e2e
tool: `typescript-best-practices` for Playwright).
