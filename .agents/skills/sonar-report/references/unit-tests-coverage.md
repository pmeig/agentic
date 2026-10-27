# Sonar report: run the unit tests with coverage

1. Machine free first (`e2e-run`, `references/free-machine.md`).
2. For each changed module (the whole project before a PR), run the unit tests **with coverage** with the module's own command
   (Vitest `--coverage`, Gradle/Maven + Jacoco, pytest-cov, `go test -cover`, `cargo llvm-cov`, `dotnet test` + coverlet, Flutter
   `--coverage`, Xcode coverage...), with the language tools as the project runs them.
3. A failing unit test is not a Sonar matter: send it to its owner (`front` or `back`) with the test, message and stack.
