---
name: python-best-practices
description: "MANDATORY for any .py file, pyproject.toml or Python test: Python 3.13, uv, type hints, ruff, pydantic, pytest, runs in WSL."
---

# Python best practices (router)

The user's only Python project (`D:\projects\python\sudoku`) is old student code (Python 2, globals, recursion): keep its
reST docstring habit (`:param x:` / `:return:`), nothing else. Run Python the way the project requires.

Load only the row(s) that match the task; never every reference.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Creating a module / tooling, versions, layout | `references/setup.md` |
| Writing or reviewing code | `references/code.md` |
| Writing or reviewing unit tests | `references/tests.md` |
| Monthly refresh, sources | `references/maintenance.md` |
