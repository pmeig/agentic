---
name: shell-bash-best-practices
description: MANDATORY for any shell/PowerShell script (CI run steps, entrypoints): strict mode, quoting, no echoed secrets, traps, ShellCheck.
---

# Shell scripting best practices (router)

Based on ShellCheck rules and common practice. Windows specifics: run Docker and Python the way the project requires.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Writing or reviewing a Bash script | `references/bash.md` |
| Writing or reviewing a PowerShell script | `references/powershell.md` |
| Scripts run in CI (GitHub Actions steps) | `references/ci.md` |
| Monthly refresh, sources | `references/maintenance.md` |
