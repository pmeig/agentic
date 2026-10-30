# Java best practices: code style and idioms

- 2-space indentation, K&R braces, **braces always** (no braceless `if`), max ~140 columns, explicit imports (no wildcard, no unused).
- `final` on fields, parameters and locals; **no `var`**: explicit types.
- Immutability first: `List.of`/`Map.of`/`List.copyOf` for returned collections (defensive copies), `Stream.toList()`, no setters on value types.
- Streams and method references for transformations (`map`, `flatMap(Collection::stream)`, `Collectors.partitioningBy/groupingBy`); a plain loop when it reads better or needs early exit.
- Null: constant-first comparisons (`null != value`, `"x".equals(input)`, `Boolean.TRUE.equals(flag)`). Prefer `Optional` as a **return type** for "may be absent" (never as a field or parameter); mark packages `@NullMarked` (JSpecify) and use `@Nullable` for the exceptions.
- Modern Java (25+): records, sealed interfaces + pattern matching `switch` (exhaustive, no `default` on sealed types), text blocks for SQL/JSON, `instanceof` patterns, flexible constructor bodies (validate before `super(...)`), virtual threads for blocking I/O, `ScopedValue` instead of `ThreadLocal` for request context. Preview features only when the project enables them.
- Exceptions: unchecked domain exceptions (`BusinessException`, `TechnicalException`) carrying a code; wrap checked ones with message + cause (`throw new XxxException("Failed to create file: " + name, e)`); try-with-resources; never swallow.
- Concurrency: use concurrent collections only when shared between threads; `synchronized` sparingly, prefer `java.util.concurrent` locks/atomics.
- Javadoc on public API (what and why, one or two sentences); no commented-out code.

Boilerplate (getters, constructors, builders, logger): `references/lombok.md`. Naming and layering: `references/structure.md`.
