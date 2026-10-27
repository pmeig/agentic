# Rust best practices: setup (edition, tooling, layout)

- Edition 2024, `rust-version` in `Cargo.toml` (Cargo resolves dependencies against it), `Cargo.lock` committed for binaries; workspace (`[workspace]`, shared `[workspace.dependencies]`) for several crates.
- `cargo fmt`, `cargo clippy -- -D warnings` (pedantic where reasonable), `cargo deny`/`cargo audit` in CI.
- Layout: `src/main.rs` (wiring), `src/lib.rs` (public API), one module folder per feature (`expense/{mod.rs, handler.rs, service.rs, repository.rs, model.rs}`), shared `core/`.
