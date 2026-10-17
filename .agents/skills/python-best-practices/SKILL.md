---
name: python-best-practices
description: MANDATORY for any .py file, pyproject.toml or Python test: Python 3.13, uv, type hints, ruff, pydantic, pytest, runs in WSL.
---

# Python best practices

The user's only Python project (`D:\projects\python\sudoku`) is old student code (Python 2, globals, recursion): keep its
reST docstring habit (`:param x:` / `:return:`), nothing else. Run Python the way the project requires.

## 1. Project setup

- Python 3.13, a virtual environment per project (`uv venv` / `python -m venv .venv`), dependencies and tools in `pyproject.toml` (PEP 621), locked (`uv lock` or pinned requirements); never install into the system Python.
- Layout: `src/<package>/` + `tests/` mirroring it, `__main__.py` or a `[project.scripts]` entry point for CLIs.
- Tooling: `ruff` (lint + format, line length 120), `mypy --strict` or `pyright` in CI, `pytest` + `pytest-cov`; same commands in the README and the CI.

## 2. Code

- PEP 8 naming (`snake_case` functions/variables/modules, `PascalCase` classes, `UPPER_SNAKE` constants), 4 spaces, f-strings.
- **Type hints everywhere** (`list[str]`, `X | None`, `TypedDict`, `Protocol`, generics with `[T]` syntax), checked in CI.
- Data: `@dataclass(frozen=True, slots=True)` for values, `pydantic` models for external input/config validation, `enum.StrEnum` for fixed sets.
- No mutable global state and no `global`: pass dependencies explicitly (functions/classes), configuration from the environment loaded once (`pydantic-settings`).
- Iteration over recursion for unbounded data (recursion limit), comprehensions/generators for transformations, `itertools`/`functools` before hand-written loops.
- `pathlib.Path` for files, context managers (`with`) for every resource, `logging` (never `print` in libraries/services), explicit encoding (`encoding="utf-8"`).
- Errors: specific exceptions (custom ones derived from a project base exception), `raise ... from error`, never bare `except:`; validate inputs at the boundary.
- Async (`asyncio`, FastAPI): `async def` end to end for I/O, no blocking calls inside, `asyncio.TaskGroup` for concurrency.
- Layering for APIs: router/controller → service → repository; FastAPI dependencies for injection, pydantic schemas at the edge.
- Docstrings (reST, the user's habit) on public functions: one summary line, `:param:`/`:return:`/`:raises:` when not obvious from the types.

## 3. Tests (pytest)

- `tests/test_<module>.py`; **one class `Test<FunctionName>` per public function**, test names `test_should_<result>_when_<condition>`.
- Fixtures for setup (`conftest.py` for shared ones), `@pytest.mark.parametrize` for input tables, `tmp_path` for files, `monkeypatch` for environment, `unittest.mock`/`pytest-mock` for dependencies at the boundary.
- Cover every branch, error path and edge case; never test dataclasses without logic.

```python
class TestSolve:
    def test_should_return_solved_grid_when_grid_is_valid(self) -> None:
        grid = Grid.parse(EASY)

        result = solve(grid)

        assert result.is_solved()

    def test_should_raise_when_grid_is_inconsistent(self) -> None:
        with pytest.raises(InvalidGridError):
            solve(Grid.parse(INVALID))
```

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `@pytest.mark.parametrize` (with `ids=` naming each case) on the methods of the `Test<Function>` class. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the official sources, update only internet-derived guidance, keep user/project rules, add source URLs, update this date, report changes.
