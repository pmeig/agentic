# Rust best practices: code (errors, ownership, async, unsafe)

- Errors: libraries define typed errors with `thiserror`, binaries use `anyhow` with `.context("...")`; `?` to propagate; **no `unwrap`/`expect` in production paths** (only in tests or with an invariant comment); map domain errors to HTTP responses in one `IntoResponse` impl.
- Ownership: borrow (`&str`, `&[T]`) in parameters, own (`String`, `Vec<T>`) in structs; clone deliberately; `Arc` for shared read-only state, `Mutex`/`RwLock` (tokio versions in async) only when needed.
- Async: tokio runtime, no blocking calls in async code (`spawn_blocking`), structured tasks (`JoinSet`), cancellation-safe `select!`; async closures (2024) where they simplify.
- `unsafe` only with a `// SAFETY:` comment explaining the invariant; `unsafe extern` blocks (2024).
