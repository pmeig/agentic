---
name: sonar-csharp
description: "Only when asked: Sonar setup, coverage, exclusions of a C# / .NET module."
---

# Sonar for C# / .NET (on request only)

## Scanner and properties

- `dotnet-sonarscanner begin /k:"<repository>" /d:sonar.host.url=... /d:sonar.token=... /d:sonar.cs.opencover.reportsPaths="**/coverage.opencover.xml"`,
  then `dotnet build`, `dotnet test --collect:"XPlat Code Coverage" -- DataCollectionRunSettings.DataCollectors.DataCollector.Configuration.Format=opencover`
  (coverlet), then `dotnet-sonarscanner end /d:sonar.token=...`. The token is passed by the caller, never written in a file.
- Test projects (`*.Tests.csproj`) are recognised by the scanner: keep them out of the sources with
  `sonar.test.inclusions=**/*Tests.cs,**/*Test.cs`.

## Out of the analysis

- Tests: `**/*.Tests/**`, `**/*Tests.cs` in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`.
- Without behavior (`sonar.coverage.exclusions`): `**/Program.cs`, `**/*Dto.cs`, `**/*Entity.cs`, `**/Models/**`, `**/Migrations/**`,
  options classes (`*Options.cs`), generated code (`*.Designer.cs`, `*.g.cs`), `**/Configuration/**`, exception classes without logic.
- Attributes `[ExcludeFromCodeCoverage]` are not used to hide logic.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/scanners/dotnet/introduction/ ,
https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/dotnet-test-coverage/
