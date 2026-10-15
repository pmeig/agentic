---
name: e2e-maestro-best-practices
description: Writing, reviewing or running Maestro YAML e2e flows (Android, iOS, React Native, Flutter, web).
---

# Maestro e2e best practices

- One flow per business gesture in `maestro/<feature>/` (YAML), shared steps in subflows called with `runFlow`; workspace `config.yaml` for flow discovery, tags and global settings.
- Selectors: accessibility id / `id` (testTag, accessibilityIdentifier) first, visible text second, coordinates never; `assertVisible` and `extendedWaitUntil` on a state, no fixed delays.
- Start each flow from a clean state (`launchApp` with `clearState: true`, `clearKeychain` on iOS), seed data through the API (`runScript` or an HTTP call); parameters through `env` (`-e KEY=value`), secrets from Vault.
- Tags (`tags: [smoke, regression]`) with `--include-tags` / `--exclude-tags` to build suites; JUnit output with `--format junit --output report.xml`; screenshots and debug output kept as CI artifacts.
- Parallel: `maestro test --shard-split <n>` (split flows across devices) or `--shard-all <n>` (run all flows on each), one emulator/simulator per shard, count from `e2e-parallelism-init`; or Maestro Cloud.
- Real accessibility labels make the app testable and WCAG compliant at once: the same work serves selectors and accessibility.

Run through `e2e-run`; workers from `e2e-parallelism-init` (key `maestro`).

Sources:
- https://docs.maestro.dev/ , https://github.com/mobile-dev-inc/maestro/releases
- Flag names (`--shard-split`, `--shard-all`, `--format`) are to be re-checked on the CLI reference at the monthly refresh.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources above, update only internet-derived guidance, keep user/project rules, update this date, report changes.
