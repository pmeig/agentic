# Python best practices: code

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
