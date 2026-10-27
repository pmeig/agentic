# C# / .NET best practices: data

- Data: EF Core with migrations (never `EnsureCreated` in production), `AsNoTracking` for reads, projections to DTOs, no lazy loading; Dapper for hot paths; parameters only (`sql-best-practices`).
