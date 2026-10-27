---
name: rust-best-practices
description: "MANDATORY for any Rust code (CLIs, axum/tokio services, libraries): modules by feature, traits, thiserror/anyhow, no unwrap, tests per function, edition 2024."
---
# Rust best practices (router)
Idiomatic Rust transposing the team's layering conventions; the project's own rules win. Load only the row(s) that match the task; never load every reference.

## Need -> file
| Need (what the agent is doing) | Load |
|---|---|
| Creating a crate / Cargo, tooling, layout | `references/setup.md` |
| Layering, types, naming | `references/structure.md` |
| Errors, ownership, async, unsafe | `references/code.md` |
| Configuration, logging, SQL | `references/config-data.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
