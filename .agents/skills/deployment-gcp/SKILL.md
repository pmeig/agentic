---
name: deployment-gcp
description: Use when deploying an application to Google Cloud or configuring its Google Cloud environment and CI/CD identity.
---

# Google Cloud Deployment

Apply this skill only after the lead selects Google Cloud and approves the target environment.

## Plan and provision safely

- Reconfirm project ID, region, environment count, expected services, data location, availability, and budget before provisioning.
- Choose the simplest suitable service (for example, Cloud Run for a containerized service, Firebase Hosting for static web content,
  or GKE only when orchestration requirements justify it). Verify current product fit and pricing with official Google Cloud docs.
- Ask before creating projects, enabling billable APIs, allocating public IPs, databases, load balancers, or other chargeable
  resources. Configure budget alerts when available.
- Use Terraform only when requested or justified, following the `terraform` skill.

## Identity and delivery

- Prefer GitHub Actions Workload Identity Federation with short-lived credentials over service-account JSON keys.
- Apply least-privilege IAM roles, separate deployment identities by environment where practical, and scope access to the required
  project and services.
- Keep configuration and secrets out of source control. Use protected GitHub Environments and environment-scoped secrets or
  provider secret stores.
- Build an immutable artifact once, then promote it according to the selected branch-strategy skill. Add health checks,
  observability, rollback instructions, and a post-deployment smoke/e2e run.

## User assistance

If project ownership, organization policy, billing, domain verification, or identity setup requires account-holder action, give
the user exact console navigation and the minimum required settings. Continue automation after the user confirms; never claim the
environment is deployed until it has been exercised.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Google Cloud API/CLI, release, pricing, and console sources. Verify services,
API versions, `gcloud`, IAM, and Workload Identity Federation; preserve user rules, update sources/date, and report changes. For
console help, capture authorized current screenshots with sensitive data redacted, or disclose unavailable access and provide
official links/navigation.

## Official sources

- Cloud Run documentation: https://cloud.google.com/run/docs
- GitHub Actions Workload Identity Federation: https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines
- IAM overview: https://cloud.google.com/iam/docs/overview
- Google Cloud pricing calculator: https://cloud.google.com/products/calculator
