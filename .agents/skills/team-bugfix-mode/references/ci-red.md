# Bugfix mode: green locally, red in the CI

**Green locally, red in the CI** (local gate = impacted e2e only, other environment): the lead reads the failed logs, classifies, then works in bugfix mode on the open PR (`references/triage-and-fix.md`):
- **Not selected locally**: `graph.yaml` wrong: `qa` fixes test or sends code to the owner, `documentalist` fixes the graph entry.
- **Environment** (versions, ports, secrets, data, time zone, workers, slower runner): reproduce locally in the CI's conditions (same workers, fresh data, no cache) before changing anything; timing problems are flaky procedure, not a bigger timeout.
- **Sonar**: code owner, with the report; no exclusion without the lead's decision.
- **Infrastructure** (runner, secret, network, same failure on unrelated PRs): lead/user, never looped.
- **Flaky** (red then green, or red only in the CI): not a pass, not an infrastructure excuse; repaired as above and proven stable in the CI.

**A red CI that passes locally**: before any fix, apply `ci-parity-before-push` "Fixing a red CI without extra round trips": read the CI's real environment from its artifacts, reproduce RED locally in it, fix every occurrence of the pattern, prove red-before / green-after, push once. A test that passes both before and after the fix proves nothing.
