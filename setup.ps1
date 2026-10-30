# Recreates the links that tools need after a clone: git does not keep Windows junctions.
# .agents/ holds the real files and is the only source. Tools that read AGENTS.md and .agents/ directly
# (Codex, Copilot, Cursor, Gemini...) need nothing; Claude Code reads .claude/, which only links to .agents/.
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
New-Item -ItemType Directory -Force (Join-Path $root '.claude') | Out-Null
foreach ($name in 'agents', 'skills') {
    $link = Join-Path $root ".claude\$name"
    $item = Get-Item $link -Force -ErrorAction SilentlyContinue
    # a missing or broken link (for example an absolute one from another machine) is replaced
    if ($item -and $item.LinkType -and -not (Test-Path $item.Target)) { $item.Delete() }
    if (-not (Test-Path $link)) {
        New-Item -ItemType Junction -Path $link -Target (Join-Path $root ".agents\$name") | Out-Null
    }
    Write-Output ".claude\$name -> .agents\$name"
}
