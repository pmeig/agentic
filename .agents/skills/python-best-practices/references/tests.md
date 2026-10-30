# Python best practices: unit tests

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
