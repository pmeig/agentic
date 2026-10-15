---
name: shell-bash-best-practices
description: MANDATORY for any shell or PowerShell script (bash, CI run steps, Docker entrypoints): strict mode, quoting, until-loops, no echoed secrets, traps, ShellCheck, WSL specifics.
---

# Shell scripting best practices

Based on the user's scripts (`budget/.github/workflows/*.yml` run steps, `e2e/*/run.sh`, `.agents/skills/demo/scripts/*.sh`,
`Qt/certification/*.ps1`) and ShellCheck rules. Windows specifics: Docker and Python only in WSL (`docker`, `python` skills).

## 1. Bash

- Shebang `#!/usr/bin/env bash`, `set -euo pipefail` at the top (CI `run:` steps already use `bash -e`), `IFS` left default unless needed.
- **Quote every expansion** (`"$var"`, `"$@"`, `"$(cmd)"`), `[[ ... ]]` for tests, `$(...)` never backticks, `local` variables in functions, `readonly` constants in `UPPER_SNAKE`, lowercase for locals.
- Functions for every step, shared helpers in a sourced `lib.sh`; a script does one job and prints what it does; `main "$@"` at the end for larger scripts.
- Wait for a condition, never a fixed sleep: `for _ in $(seq 1 60); do curl -fs -o /dev/null "$url" && break; sleep 1; done` then fail with a clear `::error::` message (GitHub Actions) when it never came.
- Cleanup with `trap cleanup EXIT` (stop processes, remove temp dirs from `mktemp -d`), commands that may legitimately fail followed by `|| true` with a comment.
- Secrets: read into a variable in the same command that uses it, `::add-mask::` in CI, never `echo`/`set -x` them, never on a command line that stays in history; print lengths or HTTP statuses only.
- Portable tools (`grep -E`, `sed -E`, `awk`); `jq` for JSON (never grep on JSON), `curl -fsSL` with `--retry` for networks; for anything beyond ~100 lines or real data structures, write the script in TypeScript/Python instead.
- Git Bash on Windows: `MSYS_NO_PATHCONV=1` for device paths, `cygpath -w` for Windows paths, `cmd //c` for Windows commands; WSL via `wsl.exe -e bash -ic '<alias>'` (aliases need the interactive shell).
- ShellCheck clean (`shellcheck -x`), `shfmt -i 2` formatting.

## 2. PowerShell

- PowerShell 7, `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, approved verbs (`Get-`, `Set-`, `New-`), parameters with `[CmdletBinding()]` and typed `param()` blocks, `-Confirm:$false` only when the action is intended.
- Secrets with `SecretManagement`/`SecureString`, never printed; PSScriptAnalyzer clean.

## 3. In CI (GitHub Actions)

- Values passed through `env:` then used as `"$VAR"`, never `${{ }}` interpolated inside a script (injection); outputs with `echo "name=value" >> "$GITHUB_OUTPUT"`; one step per meaningful action with a name that says it; long scripts moved to files in the repo and linted.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
