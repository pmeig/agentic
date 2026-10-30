# E2E run: rules for every e2e test (all tools)

- Test user-visible behavior from `gesture.md`; one scenario per path; each test creates its own data; no dependency between tests;
  never a fixed sleep; never weaken an assertion.
- Ports, data and output folders unique per worker and different from the application defaults; secrets from Vault or the
  environment, never in the repo.

Also load `references/twin-e2e.md` when the project has e2e on several platforms.
