# TypeScript / JavaScript best practices: code (language idioms, errors, naming)

Server layering: controller → service → repository → infrastructure client; Angular: `angular-best-practices`; SQL: `sql-best-practices`.

- **No `enum`**: string-literal unions, or a frozen object + derived type (`const Status = Object.freeze({...} as const); type Status = (typeof Status)[keyof typeof Status]`).
- `interface` for domain/entity shapes, `type` for unions, mapped/derived types (`Omit`, `Pick`, `ReturnType<typeof useX>`) and row shapes. `satisfies` to check literals without widening; `as const` for constant tables and schemas; no `any` (use `unknown` + narrowing), no non-null `!` except right after a check the compiler cannot see.
- Arrow `const` functions by default; `function` declarations only for overloads or hoisting needs. Classes only for errors or when a framework requires them (decorator DI libraries).
- **`undefined` = absent** in the code (`?.`, `??`, `??=` lazy caches); `null` only at boundaries (SQL rows, JSON APIs) and converted at the mapping (`?? null` / `?? undefined`).
- Immutability: `readonly` fields and arrays, `Object.freeze(...) satisfies Readonly<X>` for configuration, spread to copy, no mutation of parameters.
- Errors: subclasses of `Error` with `name` and typed fields (`HttpError(statusCode, message)`); wrap with `{cause}`; `catch (error: unknown)` and narrow; fail-fast getters for missing initialization; never an empty `catch` without a comment.
- Async: `async/await`, `Promise.all` for independent work, mark intentional floating promises `void`, `AbortSignal` for cancellable I/O; never mix callbacks and promises.
- Validation of external input at the edge (JSON schema / zod) with types derived from the schema or kept identical in shape.
- Naming: files kebab-case + dot-kind suffix (`expense.repository.ts`, `request.dto.ts`, `database.helper.ts`, `mail.client.ts`, `auth.properties.ts`), camelCase values, PascalCase types, `UPPER_SNAKE` module constants; kind folders only from two files (`file-kind-folders`).
- JSDoc: one sentence on each exported function/constant about intent or the business rule; `//` comments explain why, in English.
- Plain JavaScript: ESM too, JSDoc `@param {Type}` typing with `// @ts-check`, same naming; no unreachable code after `throw`.
