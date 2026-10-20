#!/bin/bash
# Cloud sessions only: recreate the .claude/agents and .claude/skills links so the team agents are registered at start.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

"${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/../.." && pwd)}/setup.sh"
