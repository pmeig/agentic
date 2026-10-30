# NestJS best practices: unit tests

- `Test.createTestingModule` with the dependencies replaced by mocks (`useValue`), or plain instantiation for services; `*.spec.ts` beside the source (or mirrored in `test/`), **one `describe` per public method**, `it('should ... when ...')`.
- e2e with `supertest` on the Nest app and a Testcontainers database; cover validation errors, guards and error filters, not only 200.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the method. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
