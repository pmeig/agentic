# Run and access: where skills live

Knowledge of **how to execute a command or reach a service** never goes in `AGENTS.md`, `CLAUDE.md` or the docs. It lives in a dedicated skill, loaded only when needed.

## Global vs repo

| What it is | Where the skill goes |
|---|---|
| A **generic tool or service**, the same whatever the repo: build tools (mvn, gradle, pnpm), version managers, vault, SonarQube, docker, git hosting CLI, emulator/SDK | **Global skill**: `~/.agents/skills/<tool>/SKILL.md`, link `~/.claude/skills/<tool>` |
| Something **specific to one repo**: its scripts, e2e runners, demo/seed helpers, deploy procedure, project keys, URLs, paths, secret paths | **Repo skill**: `<repo>/.agents/skills/<name>/SKILL.md`, link `<repo>/.claude/skills/<name>` |

Real copy always in `.agents`, only a link in `.claude` (Windows: a junction `New-Item -ItemType Junction -Path <link> -Target <folder>`, no admin needed; macOS/Linux: a symlink). A repo skill is committed (`.agents`); the links are recreated after a clone.

`AGENTS.md` may at most name the skill ("to run the e2e, load `<skill>`"); it never contains the commands.

## SessionStart hook

Container tools installed once (JDK, Gradle, Android SDK, browsers, local database): record the commands in the repo's SessionStart hook (`.agents/hooks/session-start.sh`) or a repo skill, never reinstall per agent.
