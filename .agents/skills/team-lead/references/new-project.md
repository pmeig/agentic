# Lead playbook: new project (no code yet)

A new project is a short setup, then the feature loop (`references/flow-overview.md`) once per feature.

```
create-project -> need.md -> front/back technology proposals -> lead decision -> documentalist skeleton (planned)
               -> platform choice (lead/user) -> first feature: flow-overview.md from step 2
```

1. **Where and how**: load skill `create-project` before scaffolding anything (location, remote repository or local-only Git repository). Add `.agents/docs/team/` to `.gitignore`.
2. **Need**: write `.agents/docs/team/<feature>/need.md` (who, what, why, acceptance criteria, open questions). For a project with several features, one `need.md` per feature, plus the project-level goal in the first one.
3. **Technology**: `front` and `back` each propose the best-fit technology with options and pros/cons (need, stack, team, hosting, cost, performance, maintainability); they load `team-dev-rules` -> `references/tech-proposal.md`. The lead (with the user) decides; the decision is written in `need.md` or `contract.md`. `front` asks, grouped with the other business choices, whether the app gets guided tours.
4. **Docs skeleton**: after the decision `documentalist` creates `.agents/docs/INDEX.md` and `graph.yaml` from `need.md` and the stack, every entry marked `(planned)` until the code exists (enriched at step 8 of each feature). Never an empty index.
5. **Platform** (step 5 of the flow, can run in parallel with the first design round): monorepo layout, CI/CD, deployment. Load only what is needed: `deployment-platform-selection` to choose, then `deployment-aws` / `deployment-gcp` / `deployment-kubernetes`, `terraform`, `docker`, `github-actions-deployment`, `module-versioning` (monorepo with independently versioned modules); mobile stores: `android-google-play`, `ios-app-store`.
6. Continue with `references/flow-overview.md` at step 2 (design) for the first feature.
