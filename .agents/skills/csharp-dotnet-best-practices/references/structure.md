# C# / .NET best practices: structure and naming

- Layering: controller / minimal API endpoint (validation, status codes, DTOs) → service (business rules, transactions) → repository / `DbContext` → infrastructure. A controller never uses the `DbContext`.
- Constructor injection (primary constructors for services: `public sealed class ExpenseService(IExpenseRepository repository, TimeProvider clock)`), lifetimes chosen deliberately (scoped for request work, singleton for stateless), no service locator.
- Naming: `PascalCase` types/methods/properties, `_camelCase` private fields, `I` prefix for interfaces, `Async` suffix on async methods; XML doc comments on public API.
