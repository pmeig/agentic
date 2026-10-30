# Routing evals

Rerun after any change to an agent or skill `description`, a skills table, or a skill split. Method: for each prompt, start a cold `haiku` agent (or ask the lead) and check which agent is chosen and which skill/reference is loaded first. Pass = both match. Record failures as the prompt plus what was chosen, then fix the **description**, not the prompt.

| # | Prompt | Expected agent | Expected skill -> reference |
|---|---|---|---|
| 1 | "Add a settings page with a dark mode toggle" | lead -> `designer` first | `team-lead` -> `flow-overview.md`, `design-mockup-variants` |
| 2 | "Which colors for an expense list, WCAG AA?" | `designer` | `design-color-palettes` |
| 3 | "Build the screen from the chosen mockup in Angular" | `front` | `angular-best-practices`, `typescript-best-practices` |
| 4 | "Expose GET /expenses with pagination in Spring Boot" | `back` | `spring-boot-best-practices`, `java-best-practices` |
| 5 | "Should this table live in PostgreSQL or MongoDB?" | `back` | `sql-best-practices` |
| 6 | "Write the Playwright e2e for the checkout gesture" | `qa` | `e2e-playwright-best-practices`, `e2e-run` |
| 7 | "Sonar shows 92 % coverage, what now?" | `qa` | `sonar-report` |
| 8 | "CI is red on the e2e job" | lead -> `qa` | `team-bugfix-mode`, `pr-and-ci-follow` |
| 9 | "Document how the payment flow works" | `documentalist` | `documentation-ai` -> `feature-file.md` |
| 10 | "Draw the C4 container diagram" | `documentalist` | `doc-architecture-c4-adr` -> `c4.md` |
| 11 | "Translate these UI strings from French to Romanian" | `translator` | `translation-fr-ro`, `translation-craft` |
| 12 | "Write a 30 s promo video script" | `sales` | `promo-video` -> `script.md` |
| 13 | "Create a new skill for our Terraform conventions" | `ai-writer` | `ai-write-skills` -> `write.md` |
| 14 | "Write the system prompt and tool descriptions for our support bot" | `ai-writer` | `ai-write-prompts` -> `write.md` |
| 15 | "Update AGENTS.md with the new test command" | `ai-writer` (not `documentalist`) | `doc-ai-context-files` -> `agents-md.md` |
| 16 | "Add a hook that blocks `git push --force`" | `ai-writer` | `ai-write-hooks-settings` -> `write.md` |
| 17 | "Design a multi-agent system that triages bug reports" | `ai-writer` | `ai-write-agentic` -> `patterns.md` |
| 18 | "Write the README for the new module" | `documentalist` (not `ai-writer`) | `documentation-human` |

Notes: rows 15 and 18 test the `ai-writer` / `documentalist` boundary. Keep this file under ~2 KB; it is not loaded automatically.
