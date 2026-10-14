---
name: deployment-kubernetes
description: Use when the user's deployment requirements call for a Kubernetes cluster and workload configuration.
---

# Kubernetes Deployment

Recommend Kubernetes only when the user's scale, availability, isolation, or orchestration requirements justify its operational
cost. Do not provision a cluster merely because the application uses containers.

## Questions and design

- Confirm the chosen cluster provider, ownership, regions, environments, ingress/domain, storage, availability, and monthly budget.
- Inspect existing cluster conventions and choose the established deployment tool (Helm, Kustomize, or manifests).
- Define namespaces and least-privilege service accounts, resource requests/limits, readiness/liveness/startup probes, ingress/TLS,
  autoscaling only when needed, and secret integration.
- Decide where persistent data lives, how it is backed up, and how upgrades and rollback work before deploying stateful services.

## Safe execution

- Keep manifests and charts versioned; pin image tags and chart/provider versions.
- Keep secret values out of Git; use the approved external secret manager or encrypted secret workflow.
- Run lint/render/diff checks and show the planned changes. Ask before cluster creation, RBAC escalation, public exposure, paid
  resources, or production apply.
- Deploy the immutable artifact, wait for rollout and health, run smoke/e2e checks, and document rollback.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Kubernetes/provider API, release, and security sources. Verify API versions,
deprecations, CLI, and provider configuration; preserve user rules, update sources/date, and report changes. For console help,
capture authorized current screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- Kubernetes documentation: https://kubernetes.io/docs/home/
- Kubernetes security checklist: https://kubernetes.io/docs/concepts/security/security-checklist/
- Kubernetes workloads: https://kubernetes.io/docs/concepts/workloads/
