#!/bin/bash
# Claude Code only, on any clone (local or cloud): make sure .claude/agents and .claude/skills link to .agents/ so the team agents are registered.
# Idempotent and silent when the links exist.
set -euo pipefail

root="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}"
if [ -e "$root/.claude/agents" ] && [ -e "$root/.claude/skills" ]; then
  exit 0
fi
"$root/setup.sh"
