# Go best practices: unit tests

- `<file>_test.go` beside the code (package `x_test` for black-box tests).
- **One `Test<Type>_<Method>` (or `Test<Function>`) per public function**, table-driven with `t.Run` sub-tests named `should_<result>_when_<condition>`:
  ```go
  func TestService_Create(t *testing.T) {
      tests := []struct {
          name    string
          input   CreateExpense
          wantErr error
      }{
          {name: "should_save_expense_when_input_is_valid", input: validInput()},
          {name: "should_fail_when_amount_is_negative", input: negativeAmount(), wantErr: ErrInvalidAmount},
      }
      for _, tt := range tests {
          t.Run(tt.name, func(t *testing.T) {
              service := NewService(&fakeRepository{}, fixedClock)

              _, err := service.Create(context.Background(), tt.input)

              if !errors.Is(err, tt.wantErr) {
                  t.Fatalf("got %v, want %v", err, tt.wantErr)
              }
          })
      }
  }
  ```
- Hand-written fakes for interfaces (no mocking framework needed), `testing/synctest` for time and concurrency, `httptest` for handlers, Testcontainers for repository integration tests; `t.Parallel()` when independent.
- Cover every branch and error path; `go test -race -cover ./...` in CI with the coverage profile sent to Sonar.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with the table-driven test of the function (`[]struct{name ...}` + `t.Run(tt.name, ...)`). Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.
