# Code analysis for documentation: verify links and paths

## Verify links and paths

Every path written in docs must exist: extract backticked paths and test them, e.g.
`grep -rhoE '\`[A-Za-z0-9_./-]+\.(ts|kt|java|py|go|rs|cs|md|yml|yaml|json|sql)\`' docs | tr -d '\`' | sort -u | while read p; do [ -e "$p" ] || echo "MISSING $p"; done`
and check relative Markdown links (`npx -y markdown-link-check <file>` or `lychee`). Fix or remove, never leave a dead pointer.
