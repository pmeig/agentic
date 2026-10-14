---
name: deployment-aws
description: Use when deploying an application to AWS or configuring its AWS environment and CI/CD identity.
---

# AWS Deployment

Apply this skill only after the lead selects AWS and approves the target environment.

## Plan and provision safely

- Reconfirm account, region, environment count, expected services, data location, availability, and budget before provisioning.
- Choose the simplest suitable service (for example, Amplify for supported web frontends, App Runner or ECS for containerized
  services, and managed databases only when required). Verify current service fit and pricing from official AWS documentation.
- Ask before creating accounts, enabling billable services, allocating networking resources, databases, load balancers, or other
  chargeable resources. Configure AWS Budgets alerts when available.
- Use Terraform only when requested or justified, following the `terraform` skill.

## Identity and delivery

- Prefer GitHub Actions OIDC federation to assume a narrowly scoped AWS IAM role; avoid long-lived access keys.
- Apply least-privilege IAM policies, separate roles by environment where practical, and constrain repository, branch, and
  environment claims in the OIDC trust policy. Inspect the repository's actual OIDC subject format before configuring trust.
- Keep secrets out of source control. Use protected GitHub Environments and AWS Secrets Manager or Parameter Store as appropriate.
- Build immutable artifacts once and promote them according to the selected branch-strategy skill. Add health checks,
  observability, rollback instructions, and a post-deployment smoke/e2e run.

## User assistance

If account ownership, billing, identity verification, domain registration, or organization permissions require account-holder
action, give the user exact console navigation and the minimum required settings. Continue automation after the user confirms;
never claim the environment is deployed until it has been exercised.

## Official sources

- AWS IAM OIDC identity providers: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html
- AWS IAM roles for GitHub Actions: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html
- AWS ECS documentation: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
- AWS Pricing Calculator: https://calculator.aws/

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official AWS API/CLI, release, pricing, and console sources. Verify services, syntax, IAM,
and GitHub OIDC trust; preserve user rules, update sources/date, and report changes. For console help, capture authorized current
screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.
