# Kotlin best practices: code style and idioms

- Follow the project's indentation (Spring libraries 2 spaces, Android 4 spaces + trailing commas); `kotlin.code.style=official`, `class X : Y` with a space.
- `val` by default; `var` only for `@ConfigurationProperties`, JPA columns, or local accumulators. Immutable collections (`List`, `Map`) in APIs, `toList()` copies when exposing internal state.
- `data class` for values, `sealed interface` + data classes/objects for closed results and states (exhaustive `when`, no `else`), `enum class` for fixed sets, `object` for stateless singletons, `fun interface` for single-method strategies, `value class` for typed ids.
- Nullability: no `!!` (only where an API guarantees non-null, with a comment); `?.let`, elvis with early return (`val token = manager.token(request) ?: return null`), `requireNotNull`/`checkNotNull` with a message, `require(...)` for argument validation. Name unused catch variables `_`.
- Expression bodies for one-liners, named arguments for booleans and multiple same-typed parameters, default arguments instead of overloads (`@JvmOverloads` when Java calls them).
- Extension and top-level functions instead of utility classes (`StringHelper.kt`, lowercase file names for files of top-level functions); `private` top-level `const val` constants; `internal` for module-private API.
- Scope functions: `apply` to configure an object, `let` for nullable transforms, `also` for side effects; never nested scope functions.
- KDoc on public API, in English, linking symbols with `[name]`; no commented-out code, no `println` (use the logger, never log secrets).

Errors: `references/errors-logging.md`. Coroutines and Spring injection: `references/async-spring.md`.
