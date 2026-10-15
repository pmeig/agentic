---
name: typescript-best-practices
description: MANDATORY when writing, reviewing or testing TypeScript or JavaScript (Node apps and CLIs, pnpm libraries/monorepos, scripts): the user's conventions - strict ESM, no enums, satisfies/as const, arrow functions, undefined over null, frozen config, dot-kind file names, Vitest with vi.hoisted mocks and describe per function - plus TypeScript 7 practices. Use for any .ts/.js file, tsconfig or package.json.
---

# TypeScript / JavaScript best practices

Based on `D:\projects\typescript\budget\server` (the reference: newest and most careful), `pmeig`, `rpg`, `folderSync`,
`D:\projects\javascript\camille`, plus TypeScript 7 practice. Server layering (controller/service/repository, `useXxx()`):
`node-api-architecture`; Angular: `angular-best-practices`; commands: `node-version`; SQL: `sql-best-practices`.

## 1. Tooling

- **pnpm** (pinned `packageManager`), `engines.node` (or `devEngines`) matching the Docker image, `pnpm-workspace.yaml` (`packages:` for monorepos, `allowBuilds` for native deps), internal deps `workspace:*`.
- **ESM**: `"type": "module"`, `module`/`moduleResolution: "nodenext"` (`bundler` for front-end bundles), relative imports with the `.js` extension, `node:` prefix for built-ins, `import type` for type-only imports.
- tsconfig: `strict`, `noUncheckedIndexedAccess`, `noImplicitOverride`, `noFallthroughCasesInSwitch`, `exactOptionalPropertyTypes` when feasible, `isolatedModules`/`verbatimModuleSyntax`, `skipLibCheck`, target ES2022+, explicit `rootDir: "src"` and `types: ["node"]` (TS 7 defaults: `types: []`, `rootDir` = tsconfig folder, `module: esnext`; `baseUrl`, `moduleResolution: node`, ES5 are gone). No path aliases unless the bundler resolves them at runtime too.
- TS 7 (Go compiler): `tsc` for type checking; tools needing the compiler API (typescript-eslint, Angular templates) stay on TS 6 until 7.1 (`@typescript/typescript6`).
- Scripts: `build` (tsc), `dev` (`tsx watch --env-file-if-exists=.env`), `typecheck` (`tsc --noEmit`), `test` (`vitest run`), `test:coverage`.
- Format: Prettier when the project has it (pmeig: single quotes, semicolons, 2 spaces, width 120); otherwise mirror the file (budget server: 4 spaces, single quotes, no semicolons, `{x}` imports, trailing commas).

## 2. Language

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

## 3. Libraries and monorepos

- `modules/<name>/{package.json, tsconfig.json, README.md, src/index.ts}`; npm name `@pmeig/<prefix>-<name>`; `src/index.ts` re-exports the public API only.
- `package.json`: `exports` with `types` + `default` (`"./package.json"` exported), `sideEffects: false`, `files`, `homepage`/`repository`/`bugs`/`license`; versions `x.y.z-SNAPSHOT` in source, stripped and `workspace:*` rewritten at publish (CI, `github-actions-cicd`).
- Each module's tsconfig extends a shared base (`declaration`, `declarationMap`), `paths` inside `compilerOptions`.

## 4. Unit tests (Vitest)

- `test/` mirrors `src/`, files `<source>.test.ts` (Angular apps: `*.spec.ts` beside the source). Config: `environment: 'node'`, `clearMocks: true`, coverage v8 with `lcov` (Sonar), excludes entry points, entities, DTOs, properties.
- **One `describe` per public function** (top `describe` = the unit or route, nested `describe` per method); `it` (never `test`) with present-tense behavior sentences (`'generates an id for a new expense instead of sending NULL'`); `it.each` for tables; arrange/act/assert separated by blank lines.
- Mocks: `const mocks = vi.hoisted(() => ({...}))`, `vi.mock('<relative path>.js', () => ({useXxx: () => mocks.xxx}))`, module under test imported after the mocks; small factories with overrides (`const request = (overrides: Partial<X> = {}) => ({...defaults, ...overrides})`); `vi.useFakeTimers()` + `vi.setSystemTime()` for dates; `vi.stubEnv` for the environment.
- Test every exported function with behavior, including not-found, invalid input and error paths; never types, interfaces, `useXxx()` accessors or plain property files.

## Unit test rule: nested groups + parameterized tests

- **Keep the nested group per public method** (above) and, inside it, **favor parameterized tests**: when several tests of a method differ only by their inputs and expected results, write one parameterized test instead of copies, with `it.each` (table of objects, `$name` in the title) inside the `describe` of the function. Each case keeps a readable `should_..._when_...` name; separate tests stay for genuinely different arrange or verify steps.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, check official sources for version, practice, and deprecation changes. Update only internet-derived
guidance; preserve user/project rules. Add source URLs, update this date, and briefly report changes.
