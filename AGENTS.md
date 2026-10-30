# Feature team

Eight agents create a project or add a feature and question each other until the need is clear. Definitions: `.agents/agents/` (linked from `.claude/agents/`). The lead (main session) loads skill `team-lead` at the start of any project, feature, bug or PR: it routes to the file of the current step.

| Agent | Owns | Delivers |
|---|---|---|
| `designer` | UX, gestures, journeys, colors, design accessibility | 3-5 mockups per feature and page, then the chosen one |
| `front` | every front-end stack, its unit tests, the screenshot library, branches | the screen, the contract (with `back`), the gesture for `qa` |
| `back` | every back-end stack, SQL/NoSQL, its unit tests | the API and storage behind the contract |
| `qa` | e2e tests, unit-test runs, Sonar report, the go for the PR | impacted e2e green, Sonar met (100 % coverage, 0 issue) before the PR |
| `sales` | positioning, promotion, channels, copy, promo videos | brief, scripts, videos, publication plan (the lead publishes) |
| `translator` | translation as a native; skill per language and pair, refreshed monthly | translated texts and files, alternatives on request |
| `documentalist` | AI docs (`.agents/docs/`, impact graph) and human docs (README, guides, ADR) | docs in sync with the code (last step of every development); answers "how does X work" with paths |
| `ai-writer` | every AI-read or AI-run file (agents, skills, AGENTS.md, commands, hooks, prompts, memory), lean and lazy-loaded; agentic design | English files tested on a cold agent |

## Flow

```
need -> designer <-> front <-> back (contract) -> code + unit tests -> qa go -> documentalist docs
     -> push + PR + CI until green -> merge on the user's yes -> sales (optional)
```

`qa` gives the go; then `documentalist` updates the docs; only after "docs done" does the lead push and open the PR, and `qa` follows the CI. Any agent can question any other one. Each step ends with a brief and a stop (skill `context-handoff`). Details per step: `team-lead` -> `references/flow-overview.md`.

