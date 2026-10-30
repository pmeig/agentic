# Shell scripting best practices: PowerShell

- PowerShell 7, `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, approved verbs (`Get-`, `Set-`, `New-`), parameters with `[CmdletBinding()]` and typed `param()` blocks, `-Confirm:$false` only when the action is intended.
- Secrets with `SecretManagement`/`SecureString`, never printed; PSScriptAnalyzer clean.
