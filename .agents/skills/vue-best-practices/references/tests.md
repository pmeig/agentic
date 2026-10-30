# Vue best practices: unit tests

- Vitest + Vue Test Utils (`mount`) + Testing Library queries: **one `describe` per component or composable/public function**, `it('should ... when ...')`.
- Test composables and stores as functions (`setActivePinia(createPinia())`), components through their rendered output and emitted events; MSW for the API; Playwright e2e with axe for pages.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the component or function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
