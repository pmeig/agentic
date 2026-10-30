# Rust best practices: structure (layering, types, naming)

- Layering: handler (axum extractors, status) → service (business rules) → repository (sqlx queries) → infrastructure; dependencies passed as structs holding trait objects or generics (`Arc<dyn ExpenseRepository>`), built in `main`.
- Types make invalid states unrepresentable: newtypes for ids and money (`struct ExpenseId(Uuid)`), enums for states, `#[non_exhaustive]` on public enums of libraries, builders for many optional fields.
- Naming: `snake_case` functions/modules, `PascalCase` types, `SCREAMING_SNAKE_CASE` constants; `///` doc comments with examples on every public item.
