---
name: github-actions-deployment
description: Use to configure secure deployments, protected environments, artifact promotion, and cloud identity in GitHub Actions.
---

# GitHub Actions Deployment

Use this skill for deployment workflows after the branch strategy and target platform have been selected.

## Workflow structure

- Separate `quality.yml`, `build.yml`, and `deploy.yml` by responsibility. Keep required E2E jobs in `quality.yml`.
- Maximize parallelism for independent jobs and use `needs` only for required artifacts, metadata, approvals, or deployment
  ordering.
- Build versioned immutable artifacts once. Promote the selected artifact between environments; do not rebuild for production
  unless the user explicitly chooses a different model.
- Use GitHub Environments for environment-scoped approvals, secrets, and deployment history. Keep workflow permissions minimal.

## Authentication and secrets

- Prefer OIDC federation and short-lived cloud identities over long-lived cloud keys where supported.
- Restrict identity trust to the intended organization/repository, workflow, ref, and GitHub Environment.
- Inspect the repository's actual OIDC subject claims before writing cloud trust policies. GitHub's default subject format can
  differ for repositories created after 2026-07-15; never copy a generic `sub` condition without checking the current token.
- Never put credentials, signing keys, or secret values in workflow YAML, source files, command-line logs, or artifacts.
- Ask before changing repository/environment secrets, production protection rules, or external access.

## Deployment gates

- Publish and deploy only tags or artifacts produced by the selected build workflow.
- Run post-deployment smoke/e2e tests against the actual target environment and retain a clear rollback path.
- Never mark a deployment successful until health checks and required QA verification pass.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Actions, Environments, OIDC, security, and API sources. Verify action versions,
permissions, claims, and protections; preserve user rules, update sources/date, and report changes. For UI help, capture authorized
current screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- GitHub Actions environments: https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment
- GitHub Actions OIDC: https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- GitHub Actions workflow syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
- GitHub OIDC token claims: https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect#understanding-the-oidc-token
