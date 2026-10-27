# Go best practices: structure (layering, injection, interfaces, naming)

- Layering: handler (decode, validate, encode, status) → service (business rules, transactions) → repository (SQL) → infrastructure. A handler never runs SQL; a service never sees `http.Request`.
- Dependencies injected through constructors (`NewService(repo Repository, clock Clock) *Service`), wired in `main`; no package-level mutable state, no `init()` side effects.
- **Interfaces small and defined where they are used** (the consumer), return concrete types; accept interfaces, return structs.
- Naming: short package names (no `util`), `MixedCaps`, exported only what other packages need, doc comment starting with the name on every exported identifier.
