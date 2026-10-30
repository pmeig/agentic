# Rust best practices: unit tests

- Unit tests in a `#[cfg(test)] mod tests` at the bottom of the file, **one sub-module per public function**, test names `should_<result>_when_<condition>`:
  ```rust
  #[cfg(test)]
  mod tests {
      use super::*;

      mod create {
          use super::*;

          #[test]
          fn should_save_expense_when_input_is_valid() {
              let service = Service::new(FakeRepository::default());

              let result = service.create(valid_input());

              assert!(result.is_ok());
          }

          #[test]
          fn should_fail_when_amount_is_negative() {
              let service = Service::new(FakeRepository::default());

              assert!(matches!(service.create(negative_amount()), Err(ExpenseError::InvalidAmount)));
          }
      }
  }
  ```
- Integration tests in `tests/`, `#[tokio::test]` for async, fakes implementing the traits (or `mockall` when needed), `proptest` for invariants, `insta` for snapshot outputs; cover every `match` arm and error path (`cargo llvm-cov` for coverage).

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `rstest` `#[case]` / `#[values]` (or a table iterated in the test) inside the module of the function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
