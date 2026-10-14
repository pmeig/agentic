---
name: deployment-platform-selection
description: Use before selecting a deployment platform to gather user constraints, compare free and paid options, and recommend a suitable deployment design.
---

# Deployment Platform Selection

Use this skill before configuring a new deployment environment or recommending a provider.

## Requirements to clarify

Ask only the questions needed for the decision, one at a time:

- Is a free tier required, preferred, or is paid hosting acceptable? What monthly budget ceiling should be respected?
- What application modules, runtimes, traffic, storage, database, background jobs, and availability are needed?
- Which regions, data-residency, compliance, domain, backup, recovery, and operational-support constraints apply?
- Does the user already have a cloud account, domain, hosting provider, or deployment target?

For a new project, ask for the number, names, and promotion order of environments before designing deployment workflows.

## Recommendation

- Offer two or three suitable options with concise trade-offs across cost, operational effort, scalability, and lock-in.
- Check current pricing, free-tier limits, regional availability, and relevant product documentation from official provider sources;
  do not rely on stale estimates or describe a paid resource as free without checking its conditions.
- Prefer the simplest platform that meets the stated requirements. Explain when self-hosting, a managed platform, a container
  service, or an orchestrator is appropriate.
- Ask the user to choose or approve a recommendation before provisioning resources, enabling billable services, or changing a
  production environment.

## Execution and handover

- Once selected and authorized, load only the matching provider and tooling skills and configure the environment end to end.
- Use the user's approved credentials and least-privilege access; never request secrets in chat or commit them.
- If account ownership, billing, identity verification, or a provider-console action requires the user, give exact step-by-step
  instructions, help them complete it, and continue once they confirm.
- Report what was configured and verified, and clearly identify any step still requiring user action.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official provider APIs/CLIs, pricing, free-tier terms, regions, and console sources. Verify
prices and limits before recommending them; preserve user rules, update sources/date, and report changes. For console help, use
authorized current screenshots with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- Google Cloud pricing calculator: https://cloud.google.com/products/calculator
- AWS Pricing Calculator: https://calculator.aws/
- Google Cloud free program and conditions: https://cloud.google.com/free
- AWS Free Tier: https://aws.amazon.com/free/

For other candidates, use that provider's current official product, pricing, free-tier, and regional-availability pages.
