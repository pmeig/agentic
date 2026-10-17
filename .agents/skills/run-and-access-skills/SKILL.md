---
name: run-and-access-skills
description: Use whenever you are blocked on, or about to ask, how to run a command or how to connect to a service (mvn, gradle, java/node versions, vault, sonarqube, docker, a CI client, a repo script, a deploy): look for the skill first, otherwise ask once and write the skill (global for generic tools, inside the repo for repo-specific things). Never write run/connect instructions in AGENTS.md or CLAUDE.md.
---

# How to run and how to connect: always a skill

Knowledge of **how to execute a command or reach a service** never goes in `AGENTS.md`, `CLAUDE.md` or the docs. It lives in a dedicated skill, loaded only when needed:

| What it is | Where the skill goes |
|---|---|
| A **generic tool or service**, the same whatever the repo: build tools (mvn, gradle, pnpm), version managers and wrappers for java/node, vault, SonarQube, docker and its aliases, the git hosting CLI, an emulator/SDK | **Global skill**: `~/.agents/skills/<tool>/SKILL.md`, link `~/.claude/skills/<tool>` |
| Something **specific to one repo**: its scripts, e2e runners, demo/seed helpers, deploy procedure, project keys, URLs, paths, secret paths | **Repo skill**: `<repo>/.agents/skills/<name>/SKILL.md`, link `<repo>/.claude/skills/<name>` |

Real copy always in `.agents`, only a link in `.claude` (Windows: a junction `New-Item -ItemType Junction -Path <link> -Target <folder>`, no admin needed; macOS/Linux: a symlink). A repo skill is committed (`.agents`); the links are recreated after a clone.

`AGENTS.md` may at most name the skill ("to run the e2e, load `<skill>`"); it never contains the commands.

## When you are blocked or about to ask

1. **Look for a skill first**: the global folder, then the repo's `.agents/skills/`. If one covers it, load it and follow it: do not ask.
2. **Look in the repo** (README, scripts, CI configuration, package/build files): if the answer is there, use it **and** write the skill so nobody searches again.
3. **Still missing: ask the lead once**, in one grouped message (what you need to run or reach, what you tried, the exact error). Never guess a URL, a path or a command that changes something; never go looking for a secret elsewhere.
4. **Write the skill** as soon as it works (see template), and tell the lead where the file was created. Writing a global skill creates a file outside the repo: say so.
5. **Maintain it**: when the command, the path or the access changes, update the skill the same day; fix a skill that turned out wrong.

## Template of the skill

```markdown
---
name: <tool-or-topic>            # kebab-case, stable
description: Use when <situation that needs it>: <what it gives>.
---
# <Title>
## Run
Exact commands, copy-pasteable, with the wrapper or version selector the machine needs, working directory, and what success looks like.
## Connect
URL / host / port, the account or role, **where each secret is read from** (secret store path and field, or environment variable) and how to read it in the same command that uses it. Never the value.
## What worked / what is refused
Calls that work, calls refused for lack of privileges and what to ask for.
## Up-check and start
How to know the service is up, how to start it when it is down.
## Pitfalls
Known failures with their cause and fix.
```

Rules: English; short; verified by running it once (or marked `(not run)`); no secret value, token, password or private key in the file, in the report or in a command that gets logged; one skill per tool or topic.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: reread the skills you load, remove what no longer works, report in one line.
