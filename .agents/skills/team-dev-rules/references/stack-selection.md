# Team development rules: stack skill selection

Load **only** the skills of your stack, and inside each one only the references of the task at hand (each stack skill is a router: its `tests.md` row to write tests, its `setup.md` row to create a module, and so on). Existing module: keep its stack, read that module's build files only. New project/module: the stack chosen by the lead, in `need.md` or `contract.md`. Kotlin back end: `kotlin` + `spring-boot` + `sql`, not `java`/`typescript`/`go`.

Names are `<x>-best-practices` unless noted.

Found in the module -> skills: `pom.xml`/`build.gradle*` + `.java` java; `.kt` (JVM) kotlin; `spring-boot` dependency spring-boot; Android (`com.android.application`, Compose) kotlin + ui-responsive-accessible-modular; `package.json` (Node, CLI, library) typescript; `@nestjs/core` + nestjs; `angular.json`/`@angular/core` typescript + angular; `react`/`next` typescript + react; `vue`/`nuxt` typescript + vue; `svelte`/`@sveltejs/kit` typescript + svelte; `pyproject.toml`/`requirements*.txt` python; `go.mod` go; `Cargo.toml` rust; `*.csproj`/`*.sln` csharp-dotnet; `composer.json` php; `Gemfile` ruby-rails; `CMakeLists.txt`/`*.pro`/`*.uproject` cpp; `Package.swift`/`*.xcodeproj` swift; `pubspec.yaml` dart-flutter; SQL migrations, schema, queries sql; shell/PowerShell scripts, CI `run:` steps shell-bash.
