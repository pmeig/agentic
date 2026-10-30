# Team development rules: Sonar setup

- **Sonar setup** (`front`, `back`): when Sonar can analyse the language (ask `qa`), configure once per module: project key, `sonar.sources`, `sonar.tests`, coverage report path, coverage tool in the build. Never exclude files or lower a threshold yourself: ask `qa`. URL and token come from the lead through `qa`.
- Language-specific setup, only when asked: the `sonar-<language>` skill of the module.
