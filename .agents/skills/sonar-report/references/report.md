# Sonar report: write the report

`.agents/docs/team/<feature>/sonar.md` (replace the previous one) and a summary to the lead:

| Module | Language | Sonar | Tests | Coverage | Issues | Vulnerabilities | Hotspots | Gate |
|---|---|---|---|---|---|---|---|---|

After `qa` has validated the tests, delete `.scannerwork/` of the scanned module (skill `sonar`, "Cleanup after a local scan").

Under it, what is not clean: uncovered files with their lines, each issue (rule, `file:line`, message), each hotspot, and what was
not verified (language without Sonar, token limits).
