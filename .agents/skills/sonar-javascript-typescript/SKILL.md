---
name: sonar-javascript-typescript
description: Only when asked: Sonar setup, coverage, exclusions of a JavaScript/TypeScript module (Node, Angular, React, Vue, Svelte).
---

# Sonar for JavaScript / TypeScript (on request only)

Used by `qa` to answer `front` / `back` and to write the Sonar configuration of a JS/TS module (`sonar-report` section 3b).

## Properties

Model: `pmeig/github-actions/actions/node/sonar/setup` (generates the file only when the module has none).

- `sonar.projectKey=<repository>` (`<repository>-<module>` for a module that is not the root), `sonar.projectName`, `sonar.projectVersion`
  (from `package.json`), `sonar.sourceEncoding=UTF-8`.
- `sonar.sources=src`, `sonar.tests=test` (first existing of `test`, `tests`, `__tests__`, otherwise `src`), `sonar.test.inclusions=**/*.test.ts,**/*.spec.ts,**/*.test.tsx,**/*.spec.tsx`.
- `sonar.typescript.tsconfigPaths=tsconfig.json`, `sonar.javascript.lcov.reportPaths=coverage/lcov.info`.
- `sonar.exclusions=jest.config.ts,vitest.config.ts,**/*.spec.ts,**/*.test.ts,**/*.js` (compiled output and tests are not analysed as sources).
- Coverage side: Vitest `coverage.provider: 'v8'`, `reporter: ['text', 'lcov']`, `reportsDirectory: 'coverage'` (Jest: `--coverage` with `lcov`);
  `include: ['src/**']`.

## Out of the analysis

- Tests: out of `sonar.sources`, in `sonar.tests` / `sonar.test.inclusions`, and in `sonar.coverage.exclusions` and `sonar.cpd.exclusions`
  (`**/*.spec.ts`, `**/*.test.ts`, `**/test/**`).
- Without behavior (`sonar.coverage.exclusions`): `**/*.properties.ts`, `**/*.types.ts`, `**/*.dto.ts`, `**/*.entity.ts`,
  `**/*.repository.ts` (SQL constants, thin access), `**/*.client.ts` (thin HTTP/DB client), `**/index.ts` barrels, `main.ts`,
  `server.ts`, `**/*.module.ts` (NestJS), migrations, generated API clients, mocks.
- Angular / React / Vue / Svelte: route declarations, `*.config.ts`, models and interfaces, `environment*.ts`, `main.ts`, generated clients;
  components, services and stores keep their coverage.

## Monthly refresh

Last refreshed: 2026-10. At first use in a later month: re-check the sources, update only internet-derived guidance, keep user/project rules, update this date, report changes.
Sources: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/languages/javascript-typescript-css/ ,
https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/javascript-typescript-test-coverage/ ,
https://vitest.dev/guide/coverage , https://github.com/pmeig/github-actions
