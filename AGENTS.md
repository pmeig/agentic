# Feature team

Seven agents create a project or add a feature and question each other until the need is clear. Definitions: `.agents/agents/` (linked from `.claude/agents/`). The lead (main session) loads skill `team-lead` at the start of any project, feature, bug or PR: it routes to the file of the current step.

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, gestures, journeys, colors, design accessibility | 3-5 mockups per feature and page, then the chosen one |
| `front` | every front-end stack, its unit tests, the screenshot library, branches | the screen, the contract (with `back`), the gesture for `qa` |
| `back` | every back-end stack, SQL/NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, unit-test runs, Sonar report, the go for the PR | impacted e2e green, Sonar met (100 % coverage, 0 issue) before the PR |
| `sales` | positioning, promotion, channels, copy, promo videos | brief, scripts, videos, publication plan (the lead publishes) |
| `translator` | translation as a native; skill per language and pair, refreshed monthly | translated texts and files, alternatives on request |
| `documentalist` | AI docs (`.agents/docs/`, impact graph) and human docs (README, guides, ADR) | docs in sync with the code (last step of every development); answers "how does X work" with paths |

## Flow

```
need -> designer <-> front -> front <-> back (contract) -> code + unit tests
     -> qa go -> documentalist docs -> push + PR + CI until green -> merge on the user's yes -> sales (optional)
     any agent can question any other one at any step
```

- **New project** (no code): `create-project` -> `need.md` -> `front`/`back` propose technologies -> lead decides -> `documentalist` skeleton (`(planned)`) -> platform (lead/user) -> then the feature flow below, from step 2.
- **New feature**: steps 0-12 below. Red test/CI/flaky with behavior already specified = bugfix mode (skill `team-bugfix-mode`).

0 branches (`git-branch-sync`) · 1 need (`.agents/docs/team/<feature>/need.md`) · 2 design: 3-5 really different mockups, the user picks (no code before) · 3 contract `front`+`back` · 4 build in parallel, each its unit tests (100 % coverage, 0 Sonar issue) · 5 platform = lead/user · 6 handover `gesture.md` · 7 e2e gate: `qa` runs only the impacted e2e, only `qa` gives the PR go (twin e2e when several platforms) · 8 docs by `documentalist` before any push · 9 push, PR, CI until green, merge only on the user's yes · 10 promotion (optional) · 11 translation (optional) · 12 docs on request.

## Lazy loading of skills (every agent, every step)

- **Nothing is loaded in advance.** Load a skill only at the step that needs it, as listed in the "Skills" table of your agent file; not before, not "just in case".
- **Skills are routers**: `SKILL.md` is a short "need -> file" table. Read it, then read only the `references/<file>.md` of the task at hand (writing tests -> the tests file, creating a module -> the setup file). Never read every reference of a skill.
- **Stack skills**: only your module's stack (`team-dev-rules`, `references/stack-selection.md`) and only the references of the task.
- A skill or reference already read in this package is not reread. Skills of another role are not yours: ask the owner.
- Skill layout and how to split a skill: `doc-ai-context-files`, `references/skills-layout.md`.

## Rules for every agent

- **Code to locate, docs for the rules**. *Locate* ("where / how does X work"): grep the names in the code first; open `.agents/docs/` only if that fails. *Change code*: read `.agents/docs/INDEX.md` and `gotchas.md` (top section "Repo rules a PR must satisfy"), `grep` (do not read in full) `graph.yaml` for your module's impact edges, open the feature file only if a doubt remains; never read the whole docs tree. Docs missing: ask `documentalist`; docs wrong or stale: the code wins, tell `documentalist`. Not found anywhere: `SendMessage` the owner (`documentalist` for "how does X work / where is Y", `front`/`back` for their module). Scan the repository only when nobody knows.
- **Handoffs**: each step ends with a brief and a stop; start from your brief, not the history (`context-handoff`, loaded at the start and end of a package).
- **AI-facing documents are in English** (`AGENTS.md`, agents, skills, docs, memory, prompts, agent messages); text people read follows the product language (`ai-docs-in-english`).
- **AI docs live in `<project>/.agents/docs/`** (never `docs/ai`, never loose in `docs/`): `INDEX.md`, `graph.yaml`, features, api, data, conventions, `screens/`, and the team workspace `team/<feature>/` (short, current, **local only: gitignored, never committed or pushed**; the lead adds `.agents/docs/team/` to `.gitignore`). Human docs stay where people expect them. AI docs are machine-first and cheap to read (maps, edge lists, tables; no diagrams or prose; budget in `documentation-ai`); human docs keep diagrams and readable prose.
- **Ask instead of guessing**: short `SendMessage` with context to the owner of the answer; the answer is written back into the feature folder. Only business choices, budget and credentials go to the user, grouped.
- **Words go through `translator`**: any text a person reads (UI labels, errors, empty states, store listings, emails, release notes, scripts, captions, copy, legal wording) is written or reviewed by `translator` with tone, sentence type, audience, length limit. Code comments, logs and AI files are out of scope.
- **Code owners** (`front`, `back`; `qa` for the gates) load `team-dev-rules` at the task that needs a rule: layout, unit tests, coverage, Sonar setup, stack choice. **Tests always run in English** (`team-dev-rules`, `references/test-language.md`).
- **Empty-directory cleanup**: before handing off, remove directories left empty by your own adds/moves/deletes; leave unrelated ones.
- **Done means verified**: built, unit tested, CI green on the PR. Report what was not verified.
- **Blocked on how to run or connect? A skill, never AGENTS.md** (`run-and-access-skills`): global skill for generic tools, repo skill (`.agents/skills/`) for repo-specific things; look first, else ask the lead once, then write it.
- The project's own `CLAUDE.md` / `AGENTS.md` and `.claude/skills` / `.agents/skills` win over the team skills.
