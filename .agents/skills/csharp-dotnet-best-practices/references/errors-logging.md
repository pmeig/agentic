# C# / .NET best practices: errors and logging

- Errors: domain exceptions for business failures, one exception handler returning RFC 9457 `ProblemDetails` (`AddProblemDetails`, `IExceptionHandler`); `Result` types where failures are expected flow.
- Logging with `ILogger<T>` and message templates (`logger.LogInformation("Created {ExpenseId}", id)`), source-generated `LoggerMessage` in hot paths, OpenTelemetry for traces/metrics, health checks.
