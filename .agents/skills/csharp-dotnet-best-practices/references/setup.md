# C# / .NET best practices: setup

- .NET 10 LTS (`global.json` pins the SDK, `<TargetFramework>net10.0</TargetFramework>`), `Directory.Build.props` for shared settings: `<Nullable>enable</Nullable>`, `<ImplicitUsings>enable</ImplicitUsings>`, `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>`, `<AnalysisLevel>latest-recommended</AnalysisLevel>`; central package versions in `Directory.Packages.props`.
- `.editorconfig` with the formatting and analyzer rules, `dotnet format` in CI.
- Solution layout: `src/<App>.Api`, `src/<App>.Application` (services), `src/<App>.Infrastructure` (EF Core, clients), `src/<App>.Domain`; or vertical slices by feature in one project for small services; `tests/` mirroring them.
