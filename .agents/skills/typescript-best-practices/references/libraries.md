# TypeScript / JavaScript best practices: libraries and monorepos

- `modules/<name>/{package.json, tsconfig.json, README.md, src/index.ts}`; npm name `@pmeig/<prefix>-<name>`; `src/index.ts` re-exports the public API only.
- `package.json`: `exports` with `types` + `default` (`"./package.json"` exported), `sideEffects: false`, `files`, `homepage`/`repository`/`bugs`/`license`; versions `x.y.z-SNAPSHOT` in source, stripped and `workspace:*` rewritten at publish (CI).
- Each module's tsconfig extends a shared base (`declaration`, `declarationMap`), `paths` inside `compilerOptions`.
