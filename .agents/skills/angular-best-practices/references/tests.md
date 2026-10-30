# Angular best practices: unit tests (Vitest)

- Vitest through `@angular/build:unit-test` (jsdom), explicit `import { describe, expect, it, vi } from 'vitest'`.
- Unit-test pure helpers and service cores (no TestBed needed): one `describe` per function, behavior sentences in `it`, `setup()` factories returning fakes, `vi.useFakeTimers()` + `advanceTimersByTime`. Components and pages are covered by e2e (Playwright) unless they hold logic that cannot move to a helper.
- Library directives: a host component with an inline template per variant, `TestBed.createComponent(Host)`, wait for stability (and the libraries' 50 ms debounce) before asserting.
- Accessibility checked in e2e with axe (0 violation).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
