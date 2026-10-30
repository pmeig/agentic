# Svelte best practices: unit tests

- Vitest + `@testing-library/svelte`: **one `describe` per component or public function**, `it('should ... when ...')`; test `.svelte.ts` state classes as plain code (`flushSync` after changes), `load` functions and actions as functions with mocked `fetch`.
- Playwright e2e (SvelteKit default) with axe for pages.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the component or function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
