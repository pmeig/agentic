---
name: shell-bash-best-practices
description: MANDATORY when writing or reviewing shell scripts (bash scripts, CI run steps, Docker entrypoints, PowerShell scripts): the user's conventions from the budget CI and e2e scripts - strict mode, quoted variables, functions in lib files, until-loops instead of fixed sleeps, secrets never echoed, cleanup traps - plus ShellCheck practices and Windows/WSL specifics.
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

Last refreshed: 2026-10

- On the **first use of this skill in a calendar month after the date above**, refresh it before applying it: search the web for
  what changed since that month (new stable versions, newly recommended practices, deprecated or removed APIs and tools).
- Update **only the parts that come from the internet**: add the new practices, change outdated versions, remove what is
  deprecated or removed. Keep it short, prefer official sources (release notes, official docs).
- **Never remove or weaken the user's rules**: everything taken from the user's projects (`D:\projects\...`) or explicit
  instructions and the team conventions (layered controller/service/repository, pages/ + core/ modules, one test group per public
  method with parameterized tests favored, `should_..._when_...` names, mocks built by hand, Lombok always for Java, every branch covered...). When the internet
  contradicts one of them, keep the rule and tell the user about the conflict.
- Then set "Last refreshed" to the current month and tell the user in a few bullets what was added, changed or removed (with sources).
