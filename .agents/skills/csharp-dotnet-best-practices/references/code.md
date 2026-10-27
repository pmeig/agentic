# C# / .NET best practices: code

- Configuration with the options pattern (`IOptions<T>`, `ValidateDataAnnotations().ValidateOnStart()`), secrets from Vault/environment/user-secrets, never in `appsettings.json`.
- `record` / `record struct` for DTOs and values, `required` and `init` properties, `sealed` by default, the C# 14 `field` keyword for light normalization in accessors; extension members only for real cross-cutting helpers, never to hide business rules.
- Nullable reference types honoured (no `!` without an invariant), pattern matching `switch` expressions, collection expressions, `TimeProvider` instead of `DateTime.Now`.
- Async all the way (`async Task`, `CancellationToken` on every I/O method, no `.Result`/`.Wait()`), `ConfigureAwait(false)` in libraries.
