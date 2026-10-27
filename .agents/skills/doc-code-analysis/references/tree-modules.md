# Code analysis for documentation: tree and modules

## Tree and modules

- Inventory: `git ls-files | head`, `git ls-files | cut -d/ -f1-2 | sort | uniq -c | sort -rn` (weight per folder).
- Skip: `node_modules`, `build`, `dist`, `.gradle`, `.git`, generated code, lock files, binaries, assets (name them in `gotchas.md`).
- Modules = folders with their own build file (`package.json`, `build.gradle*`, `pom.xml`, `go.mod`, `Cargo.toml`, `*.csproj`,
  `pyproject.toml`, `pubspec.yaml`). One row each: purpose, language/framework (+ version from the build file), entry point, how to run.
- Annotated tree: depth 2 to 3, one comment per folder, in a code fence; folder rules the project applies (feature-first, kind folders).
