---
name: terraform
description: Use to provision or manage deployment infrastructure as code with Terraform.
---

# Terraform Infrastructure

Use Terraform when the user selects it or when infrastructure reuse and review justify it.

## State and environment boundaries

- Inspect the project's existing Terraform layout and provider versions first; do not replace or import infrastructure blindly.
- Select a remote state backend with encryption, access controls, and locking for shared environments. Keep state files and
  credentials out of Git.
- Represent environments using the established repository convention (separate directories, workspaces, or explicit variables);
  do not introduce multiple schemes without a reason.
- Pin provider and module versions, document required variables, and store sensitive values in an approved secret manager rather
  than `.tfvars` committed to source control.

## Change workflow

- Format and validate configuration, initialize with the project's backend settings, inspect the full plan, and report resources
  to be created, changed, or destroyed.
- Ask for explicit approval before `terraform apply`, state migration, import, destroy, or any production change.
- Apply only the approved plan, capture outputs without exposing secrets, and verify the deployed services and health checks.
- Provide rollback and state-recovery guidance. Never claim success based only on a successful plan.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Terraform, provider, backend, and registry sources. Verify provider/resource
versions, backend behavior, and CLI; preserve user rules, update sources/date, and report changes. For console prerequisites,
capture authorized current screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- Terraform documentation: https://developer.hashicorp.com/terraform/docs
- Terraform state and backends: https://developer.hashicorp.com/terraform/language/state
- Terraform Registry: https://registry.terraform.io/
- Terraform providers: https://developer.hashicorp.com/terraform/language/providers
