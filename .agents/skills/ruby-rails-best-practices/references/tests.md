# Ruby / Rails best practices: unit tests

- `spec/` mirroring `app/`; **one `describe '#method'` (or `'.method'`) per public method**, `context 'when ...'`, `it 'should ...'` style descriptions (`it 'saves the expense'` under `context 'when the input is valid'`).
- `let`/`subject` for setup, FactoryBot factories (no fixtures sprawl), `instance_double` for collaborators, `travel_to` for time, request specs for APIs, system specs (Capybara) or Playwright for e2e.
- Cover every branch and error path; SimpleCov coverage for Sonar.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with a table of cases iterated inside the `describe` of the method (`[...].each { |input, expected| it "..." }`) or shared examples. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
