#!/usr/bin/env sh
# Linux/macOS twin of setup.ps1: recreates the links tools need after a clone.
# .agents/ holds the real files and is the only source. Tools that read AGENTS.md and .agents/ directly
# (Codex, Copilot, Cursor, Gemini...) need nothing; Claude Code reads .claude/, which only links to .agents/ (relative links).
set -eu
root=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$root/.claude"
for name in agents skills; do
  link="$root/.claude/$name"
  # a missing or broken link (for example an absolute one from another machine) is replaced
  if [ -L "$link" ] && [ ! -e "$link" ]; then rm "$link"; fi
  [ -e "$link" ] || ln -s "../.agents/$name" "$link"
  echo ".claude/$name -> .agents/$name"
done
