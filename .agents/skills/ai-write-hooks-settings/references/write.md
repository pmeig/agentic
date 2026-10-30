# ai-write-hooks-settings: write and test
# hooks-settings: Hooks and settings (write)

Anything that must happen **every time** (format after edit, block a command, inject context at start) is a hook, because the harness executes it; an instruction in a prompt is only a hope.

## Where

| File | Scope |
|---|---|
| `.claude/settings.json` | project, committed |
| `.claude/settings.local.json` | project, personal, not committed |
| `~/.claude/settings.json` | all projects of the user |

Merge, never overwrite: read the file, add the key, keep the rest, keep the JSON valid.

## Hook wiring

```json
{ "hooks": { "PreToolUse": [ { "matcher": "Bash", "hooks": [ { "type": "command", "command": ".claude/hooks/guard.sh" } ] } ] } }
```

- Events (confirm the current list): `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop`, `Notification`, `PreCompact`, `SessionEnd`.
- `matcher`: tool name or regex for tool events; empty for the others.
- The script receives the event JSON on stdin. Exit `0` = ok (stdout becomes context for `SessionStart` and `UserPromptSubmit`); exit `2` = block, stderr goes to the model; other codes = non-blocking error. JSON output allows finer decisions: see the docs.
- Hook messages are AI-facing: English, one actionable sentence (what is blocked, what to do instead).

## Script rules

- Source in `.agents/hooks/`, mirrored to `.claude/hooks/` like the existing `session-start.sh`; keep both identical.
- POSIX shell, fast (< 1 s), idempotent, no network, never waits for input, quiet on success. Quote every variable; never `eval` stdin.
- Parse JSON with `jq` when present, else a fallback; fail open (exit 0) on parse errors unless the hook is a security gate.

## Permissions

`permissions.allow` / `ask` / `deny` with patterns (`Bash(npm run test:*)`, `Read(./.env)`). Allow the narrowest pattern that removes a recurring prompt; deny secrets and destructive commands; never add a blanket `Bash` allow. Values go in `env`; secrets never.

## Test

Pipe a sample event JSON into the script and check exit code and output; then trigger it once in a real session. A blocking hook must be seen blocking.

