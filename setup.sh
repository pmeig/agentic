#!/usr/bin/env sh
# Linux/macOS twin of setup.ps1: recreates the links that Claude Code needs after a clone.
# .agents/ holds the real files (read by Codex, Copilot, Gemini, Cursor...), .claude/ only links to them.
set -eu
root=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$root/.claude"
for name in agents skills; do
  link="$root/.claude/$name"
  [ -e "$link" ] || [ -L "$link" ] || ln -s "../.agents/$name" "$link"
  echo ".claude/$name -> .agents/$name"
done
