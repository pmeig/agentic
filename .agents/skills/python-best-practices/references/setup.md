# Python best practices: setup

- Python 3.13, a virtual environment per project (`uv venv` / `python -m venv .venv`), dependencies and tools in `pyproject.toml` (PEP 621), locked (`uv lock` or pinned requirements); never install into the system Python.
- Layout: `src/<package>/` + `tests/` mirroring it, `__main__.py` or a `[project.scripts]` entry point for CLIs.
- Tooling: `ruff` (lint + format, line length 120), `mypy --strict` or `pyright` in CI, `pytest` + `pytest-cov`; same commands in the README and the CI.
