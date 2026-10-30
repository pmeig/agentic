# Shell scripting best practices: in CI (GitHub Actions)

- Values passed through `env:` then used as `"$VAR"`, never `${{ }}` interpolated inside a script (injection); outputs with `echo "name=value" >> "$GITHUB_OUTPUT"`; one step per meaningful action with a name that says it; long scripts moved to files in the repo and linted.
