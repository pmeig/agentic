# React best practices: unit tests

- Vitest + Testing Library (+ `user-event`), files `*.test.tsx` beside the source: **one `describe` per component or public function**, nested `describe` per behavior group, `it('should ... when ...')`.
- Query by role/label (`getByRole('button', { name: 'Save' })`), never by class or test internals; `data-testid` only for e2e anchors; MSW to mock the API at the network level; fake timers for time.
- Hooks and helpers tested as functions; pages covered by Playwright e2e with axe checks.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the component or function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
