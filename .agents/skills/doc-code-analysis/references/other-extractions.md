# Code analysis for documentation: other useful extractions

## Other useful extractions

- Symbols/outline: `ctags -R --fields=+n`, language servers, `tree-sitter` queries, typedoc/dokka/javadoc/sphinx/godoc/rustdoc for APIs.
- Config and env: grep `process.env`, `System.getenv`, `os.environ`, `@Value(`, `Environment.GetEnvironmentVariable`; list names only.
- Feature flags, i18n keys (resource folders), permissions/roles, error codes: one table each when the project has them.
- History: `git log --stat --since`, `git shortlog -sn`, `git log --format=%s -- <path>` to recover intent and recent changes.
- Size and hot spots: `git log --since=6.months --name-only --pretty=format: | sort | uniq -c | sort -rn | head` (where changes happen).
