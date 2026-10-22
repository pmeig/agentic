---
name: sonar
description: Use to read or run SonarQube on this PC: local server, token from Vault (never printed), scan a module, quality gate and measures.
---
# SonarQube on this PC (and the Vault token behind it)
## Connect
- Server: `http://localhost:9000` (container `sonar`; `http://sonar.pmeig` through the proxy; CI runners use `http://sonar:9000`). Up-check: `curl -s localhost:9000/api/system/status` -> `"status":"UP"`.
- Token: Vault (container `vault`, started from WSL), secret `pmeig/cicd/sonar`, field `token` (the CI reads it as `pmeig/cicd/data/sonar token`). Vault root token is loaded by the interactive WSL shell. Read it into a variable in the SAME command that uses it, never print it:
```bash
raw=$(printf '%s\n' 'echo "@@$(vault kv get -field=token pmeig/cicd/sonar 2>/dev/null)@@"' | wsl.exe -e bash -ic 'p-dc exec -T vault bash -i' 2>&1)
export SONAR_TOKEN=$(printf '%s' "$raw" | tr -d '\r' | grep -o '@@[^@]*@@' | tail -1 | tr -d '@')
curl -s -u "$SONAR_TOKEN:" localhost:9000/api/authentication/validate    # {"valid":true}
```
## Run (Node module, e.g. budget server/)
After `pnpm test:coverage` (lcov in `coverage/lcov.info`), no repo file and no scanner install needed:
`cmd //c "lm n 24 && cd /d <module> && pnpm dlx @sonar/scan -Dsonar.projectKey=<key> -Dsonar.sources=src -Dsonar.tests=test -Dsonar.javascript.lcov.reportPaths=coverage/lcov.info -Dsonar.coverage.exclusions=<same as CI> -Dsonar.qualitygate.wait=true"` with `SONAR_TOKEN` and `SONAR_HOST_URL=http://localhost:9000` exported. Community edition: only the main branch (`develop` for budget); a local scan of a feature branch goes to a throwaway project key (`qa-<feature>-<module>`), never over the real key.
## Read (read-only API, `-u "$SONAR_TOKEN:"`)
`api/measures/component?component=<key>&metricKeys=coverage,line_coverage,branch_coverage,bugs,vulnerabilities,code_smells,security_hotspots,duplicated_lines_density`, `api/issues/search?componentKeys=<key>&resolved=false`, `api/hotspots/search?projectKey=<key>`, `api/project_branches/list?project=<key>`, `api/components/search?qualifiers=TRK`.
## Known keys
budget server: `budget-server` (CI, branch `develop`). Only `server/` is scanned by the budget CI; android and web have no Sonar.
## Pitfalls
`wsl.exe ... bash -ic` prints the shell banner: always extract between markers. A scan of an unpushed branch warns about missing blame information: harmless. Delete throwaway projects only when the user asks.
Deleting a project (`POST api/projects/delete`) answers 403 with the Vault CI token (scan + read only): use the Sonar UI or an admin token.
