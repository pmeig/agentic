---
name: team-dev-rules
description: "Code owners (front, back; qa for coverage and test language): load the single rule file you need (code layout, tech proposal, unit tests, coverage, Sonar setup, test language, stack skill selection), never all of them."
---

# Team development rules (router)

The project's own `CLAUDE.md` / `AGENTS.md` and `.claude/skills` / `.agents/skills` win over these rules. Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what you are doing) | Load |
|---|---|
| Creating a file or directory, placing code by role, organising tests | `references/layout.md` |
| New project or module: choosing the technology | `references/tech-proposal.md` |
| Choosing which stack skill(s) to load for a module | `references/stack-selection.md` |
| Writing or reviewing unit tests, running tests while building | `references/unit-tests.md` |
| Deciding how far coverage must go, reading the CI gate | `references/coverage.md` |
| Configuring Sonar for a module | `references/sonar-setup.md` |
| Writing or running any test (language, locale, time zone) | `references/test-language.md` |
