# Recreates the links that Claude Code needs after a clone: git does not keep Windows junctions.
# .agents/ holds the real files (read by Codex, Copilot, Gemini, Cursor...), .claude/ only links to them.
$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
New-Item -ItemType Directory -Force (Join-Path $root '.claude') | Out-Null
foreach ($name in 'agents', 'skills') {
    $link = Join-Path $root ".claude\$name"
    if (-not (Test-Path $link)) {
        New-Item -ItemType Junction -Path $link -Target (Join-Path $root ".agents\$name") | Out-Null
    }
    Write-Output ".claude\$name -> .agents\$name"
}
