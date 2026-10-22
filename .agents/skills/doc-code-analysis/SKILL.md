---
name: doc-code-analysis
description: Use to extract facts from a codebase before documenting: tree, modules, routes, features by layer, tests per feature, per-language tools.
---

# Code analysis for documentation

Never document from memory. Extract, then write. Prefer the dedicated tools (Glob, Grep) in a session; the shell commands below are
the portable equivalents to put in `.agents/docs/commands.md` so they can be rerun.

## 1. Tree and modules

- Inventory: `git ls-files | head`, `git ls-files | cut -d/ -f1-2 | sort | uniq -c | sort -rn` (weight per folder).
- Skip: `node_modules`, `build`, `dist`, `.gradle`, `.git`, generated code, lock files, binaries, assets (name them in `gotchas.md`).
- Modules = folders with their own build file (`package.json`, `build.gradle*`, `pom.xml`, `go.mod`, `Cargo.toml`, `*.csproj`,
  `pyproject.toml`, `pubspec.yaml`). One row each: purpose, language/framework (+ version from the build file), entry point, how to run.
- Annotated tree: depth 2 to 3, one comment per folder, in a code fence; folder rules the project applies (feature-first, kind folders).

## 2. Features by layer

Feature-first projects keep a feature in one folder per module (`pages/<name>/`, `features/<name>/`): list them, then for each find
the layers. Method:
1. Start from the **entry points**: UI routes/screens, HTTP routes, queue consumers, scheduled jobs, CLI commands.
2. Follow the calls down: controller → service → repository → client (grep the imported names).
3. Collect the **change set**: files that import each other inside the feature + translation keys + tests + migrations.
4. Tests per feature: unit tests mirroring the source path, e2e specs by feature folder; note the command to run just them.

## 3. Routes and handlers (what to grep)

| Stack | Pattern |
|---|---|
| Fastify/Express | `\.(get\|post\|put\|patch\|delete)\(` , `register(`, route files |
| NestJS | `@Controller(`, `@Get(`, `@Post(`... |
| Spring | `@(Rest)?Controller`, `@(Get\|Post\|Put\|Delete\|Request)Mapping` |
| Ktor | `routing {`, `get("`, `post("` |
| FastAPI/Flask/Django | `@app.(get\|post)`, `@router.`, `urlpatterns`, `path(` |
| ASP.NET | `[ApiController]`, `[Http(Get\|Post)]`, `MapGet(` |
| Go | `HandleFunc(`, `r.(Get\|Post)(`, `e.(GET\|POST)(` |
| Angular | `Routes`, `loadComponent`, `path:` in `*.routes.ts` |
| Android Compose | `NavHost`, `composable(`, route constants |
| Jobs/events | `@Scheduled`, `cron`, `@MessagePattern`, `subscribe(` |
Record `METHOD path | file:line | auth | feature`; `doc-openapi-asyncapi` turns it into the contract.

## 4. Dependencies between modules and layers

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

## 5. Other useful extractions

- Symbols/outline: `ctags -R --fields=+n`, language servers, `tree-sitter` queries, typedoc/dokka/javadoc/sphinx/godoc/rustdoc for APIs.
- Config and env: grep `process.env`, `System.getenv`, `os.environ`, `@Value(`, `Environment.GetEnvironmentVariable`; list names only.
- Feature flags, i18n keys (resource folders), permissions/roles, error codes: one table each when the project has them.
- History: `git log --stat --since`, `git shortlog -sn`, `git log --format=%s -- <path>` to recover intent and recent changes.
- Size and hot spots: `git log --since=6.months --name-only --pretty=format: | sort | uniq -c | sort -rn | head` (where changes happen).

## 6. Verify links and paths

Every path written in docs must exist: extract backticked paths and test them, e.g.
`grep -rhoE '\`[A-Za-z0-9_./-]+\.(ts|kt|java|py|go|rs|cs|md|yml|yaml|json|sql)\`' docs | tr -d '\`' | sort -u | while read p; do [ -e "$p" ] || echo "MISSING $p"; done`
and check relative Markdown links (`npx -y markdown-link-check <file>` or `lychee`). Fix or remove, never leave a dead pointer.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: check that the tools above still exist and their flags (dependency-cruiser,
madge, jdeps, pydeps, tbls, lychee), add tools for new frameworks met in projects, update, set the date, report changes.
