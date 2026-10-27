---
name: csharp-dotnet-best-practices
description: "MANDATORY for any C# / .NET code (ASP.NET Core, workers, libraries, Blazor): layered by feature, DI, options, records, nullable, ProblemDetails, xUnit, .NET 10."
---

# C# / .NET best practices (router)

The user has no .NET project yet: these rules transpose the team's conventions (`java-best-practices`,
`spring-boot-best-practices`) to idiomatic .NET. A project's own rules win.
Load only the row(s) that match the task; never load every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| SDK, `Directory.Build.props`, analyzers, solution layout | `references/setup.md` |
| Layering, dependency injection, naming | `references/structure.md` |
| Writing C# code: options, records, nullable, async | `references/code.md` |
| Errors (ProblemDetails) and logging | `references/errors-logging.md` |
| Data access (EF Core, Dapper) | `references/data.md` |
| Unit tests (xUnit, nested classes, parameterized, coverage) | `references/tests.md` |
| Monthly refresh | `references/maintenance.md` |
