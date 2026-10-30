# Code analysis for documentation: dependencies between modules and layers

## Dependencies between modules and layers

| Language | Command |
|---|---|
| TypeScript/JS | `npx -y dependency-cruiser --output-type mermaid src` (or `dot`), `npx -y madge --image graph.svg src`, `--circular` to find cycles |
| Java | `jdeps -summary -recursive <jar>`; Gradle: `./gradlew dependencies`, module graph plugins |
| Kotlin/Android | `./gradlew :app:dependencies`, `./gradlew projects` |
| Python | `pydeps <package>`, `pipdeptree`, `import-linter` |
| Go | `go list -deps ./...`, `go mod graph`, `go mod why` |
| Rust | `cargo tree`, `cargo modules` |
| .NET | `dotnet list package`, `dotnet sln list` |
Run language commands the way the project requires (version managers, wrappers, containers) as written in its AGENTS.md/README; never assume a global tool.
Turn the result into a Mermaid `flowchart` (`doc-mermaid`) limited to meaningful edges (layer rules, cross-feature imports).
