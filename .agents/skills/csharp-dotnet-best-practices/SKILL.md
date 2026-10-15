---
name: csharp-dotnet-best-practices
description: MANDATORY when writing, reviewing or testing C# / .NET code (ASP.NET Core APIs, workers, libraries, Blazor): the team's conventions transposed to .NET - layered controller/service/repository by feature, constructor injection, options pattern, records, nullable enabled, ProblemDetails errors, xUnit with one nested class per public method and should_..._when_... names - plus .NET 10 / C# 14 practices.
---

# C# / .NET best practices

The user has no .NET project yet: these rules transpose the team's conventions (`java-best-practices`,
`spring-boot-best-practices`) to idiomatic .NET. A project's own rules win.

## 1. Setup

- .NET 10 LTS (`global.json` pins the SDK, `<TargetFramework>net10.0</TargetFramework>`), `Directory.Build.props` for shared settings: `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`, `<AnalysisLevel>latest-recommended</AnalysisLevel>`; central package versions in `Directory.Packages.props`.
- `.editorconfig` with the formatting and analyzer rules, `dotnet format` in CI.
- Solution layout: `src/<App>.Api`, `src/<App>.Application` (services), `src/<App>.Infrastructure` (EF Core, clients), `src/<App>.Domain`; or vertical slices by feature in one project for small services; `tests/` mirroring them.

## 2. Code

- Layering: controller / minimal API endpoint (validation, status codes, DTOs) → service (business rules, transactions) → repository / `DbContext` → infrastructure. A controller never uses the `DbContext`.
- Constructor injection (primary constructors for services: `public sealed class ExpenseService(IExpenseRepository repository, TimeProvider clock)`), lifetimes chosen deliberately (scoped for request work, singleton for stateless), no service locator.
- Configuration with the options pattern (`IOptions<T>`, `ValidateDataAnnotations().ValidateOnStart()`), secrets from Vault/environment/user-secrets, never in `appsettings.json`.
- `record` / `record struct` for DTOs and values, `required` and `init` properties, `sealed` by default, the C# 14 `field` keyword for light normalization in accessors; extension members only for real cross-cutting helpers, never to hide business rules.
- Nullable reference types honoured (no `!` without an invariant), pattern matching `switch` expressions, collection expressions, `TimeProvider` instead of `DateTime.Now`.
- Async all the way (`async Task`, `CancellationToken` on every I/O method, no `.Result`/`.Wait()`), `ConfigureAwait(false)` in libraries.
- Errors: domain exceptions for business failures, one exception handler returning RFC 9457 `ProblemDetails` (`AddProblemDetails`, `IExceptionHandler`); `Result` types where failures are expected flow.
- Data: EF Core with migrations (never `EnsureCreated` in production), `AsNoTracking` for reads, projections to DTOs, no lazy loading; Dapper for hot paths; parameters only (`sql-best-practices`).
- Logging with `ILogger<T>` and message templates (`logger.LogInformation("Created {ExpenseId}", id)`), source-generated `LoggerMessage` in hot paths, OpenTelemetry for traces/metrics, health checks.
- Naming: `PascalCase` types/methods/properties, `_camelCase` private fields, `I` prefix for interfaces, `Async` suffix on async methods; XML doc comments on public API.

## 3. Tests (xUnit)

- One `<Class>Tests` per class; **one nested class per public method**, test names `Should_<result>_When_<condition>`:
  ```csharp
  public sealed class ExpenseServiceTests
  {
      private readonly IExpenseRepository _repository = Substitute.For<IExpenseRepository>();
      private readonly ExpenseService _service;

      public ExpenseServiceTests() => _service = new ExpenseService(_repository, new FakeTimeProvider());

      public sealed class Create : ExpenseServiceTests
      {
          [Fact]
          public async Task Should_save_expense_When_input_is_valid()
          {
              var result = await _service.CreateAsync(ValidInput(), CancellationToken.None);

              result.Id.Should().NotBeEmpty();
              await _repository.Received(1).SaveAsync(Arg.Any<Expense>(), Arg.Any<CancellationToken>());
          }
      }
  }
  ```
- NSubstitute (or Moq) built by hand, AwesomeAssertions/FluentAssertions or xUnit asserts consistently, `[Theory]` + `[InlineData]` for tables, `FakeTimeProvider` for time; `WebApplicationFactory` + Testcontainers for integration tests.
- Cover every branch and error path; coverage via `coverlet` (Cobertura/OpenCover for Sonar).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `[Theory]` with `[InlineData]`, `[MemberData]` or `TheoryData<...>` inside the nested class of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, check official sources for version, practice, and deprecation changes. Update only internet-derived
guidance; preserve user/project rules. Add source URLs, update this date, and briefly report changes.
