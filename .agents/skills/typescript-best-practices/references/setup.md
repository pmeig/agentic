# TypeScript / JavaScript best practices: setup (tooling, build, dependencies)

- **pnpm** (pinned `packageManager`), `engines.node` (or `devEngines`) matching the Docker image, `pnpm-workspace.yaml` (`packages:` for monorepos, `allowBuilds` for native deps), internal deps `workspace:*`.
- **ESM**: `"type": "module"`, `module`/`moduleResolution: "nodenext"` (`bundler` for front-end bundles), relative imports with the `.js` extension, `node:` prefix for built-ins, `import type` for type-only imports.
- tsconfig: `strict`, `noUncheckedIndexedAccess`, `noImplicitOverride`, `noFallthroughCasesInSwitch`, `exactOptionalPropertyTypes` when feasible, `isolatedModules`/`verbatimModuleSyntax`, `skipLibCheck`, target ES2022+, explicit `rootDir: "src"` and `types: ["node"]` (TS 7 defaults: `types: []`, `rootDir` = tsconfig folder, `module: esnext`; `baseUrl`, `moduleResolution: node`, ES5 are gone). No path aliases unless the bundler resolves them at runtime too.
- TS 7 (Go compiler): `tsc` for type checking; tools needing the compiler API (typescript-eslint, Angular templates) stay on TS 6 until 7.1 (`@typescript/typescript6`).
- Scripts: `build` (tsc), `dev` (`tsx watch --env-file-if-exists=.env`), `typecheck` (`tsc --noEmit`), `test` (`vitest run`), `test:coverage`.
- Format: Prettier when the project has it (pmeig: single quotes, semicolons, 2 spaces, width 120); otherwise mirror the file (budget server: 4 spaces, single quotes, no semicolons, `{x}` imports, trailing commas).
