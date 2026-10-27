# Push, pull request and CI: every red goes back to its owner, then the loop restarts

| Red | Goes to | Then |
|---|---|---|
| e2e or any test failing | `qa`: decides whether the code or the test is wrong (trace, screenshot, steps); never weakens an assertion | code wrong: `front` or `back` with scenario, steps, expected/actual, trace; test wrong: `qa` fixes it |
| compile, type, lint or unit-test error | owner of the file: `front` (client) or `back` (server) | fix and add the missing test |
| Sonar gate (coverage < 100 %, issues, duplication) | owner of the code, with the report from `sonar-report` | fix the code or add tests; never exclude files or silence a rule without the lead's decision |
| Infrastructure: runner offline, secret/cache/network error, same failure on unrelated PRs | the lead or the user | **do not loop**; report the cause and what to change |
After each fix: `qa` reruns the impacted e2e locally (machine free), `documentalist` updates the docs if the behavior changed (docs only otherwise), then the lead pushes and follows the new run. **Repeat until every check is green.**

## Stop conditions (report to the lead and the user instead of looping)
The same failure after two fixes; more than five rounds; an infrastructure cause; a fix that would change behavior or the public contract (ask first).
