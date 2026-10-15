---
name: android-google-play
description: Use to prepare, configure, release, or troubleshoot an Android application distributed through Google Play.
---

# Android Google Play Release

Use this skill when the selected deployment target is Google Play. Follow current official Android and Play Console guidance;
fees, policies, API behavior, and console screens can change.

## Gather requirements

- Confirm application ID/package name, current signing setup, version code/name policy, Play Console account status, target track,
  staged rollout requirements, and whether the release is internal, closed, open, or production.
- Ask whether the Play Console app, Google Cloud project, Play Developer API access, and CI identity already exist.
- Confirm the user has approved any account fee, production publication, signing-key change, or irreversible release action.

## Configure the release path

- Create/register the app in Play Console, complete required store listing and policy declarations, and configure Play App Signing
  and upload-key ownership. Never generate, replace, or expose a signing key without explicit user approval.
- Enable the required Play Developer API and link a least-privilege service identity through Play Console API access.
- Prefer short-lived CI credentials and the currently supported secure authentication method; do not commit service-account JSON,
  keystores, passwords, or signing keys.
- If using a community upload action, inspect its current defaults and explicitly configure a non-production test track and
  release status; do not rely on defaults that might publish to production.
- For Android Publisher API automation, create an edit, upload the bundle, update the intended track, then commit the edit.
  Committing applies the edit, so keep production-track commits behind explicit approval and protected deployment gates.
- Prefer GitHub OIDC with Google Workload Identity Federation over service-account JSON keys. The
  `google-github-actions/auth` action is maintained outside Google; verify its current security and support posture before use.
- Configure GitHub Environments and secrets/identity, build a signed AAB, validate version code/name, and upload to the selected
  test track before production.
- Keep release notes, artifacts, rollout percentage, and promotion steps tied to the version being released.
- Google currently lists a one-time US$25 developer-account registration fee; verify the current fee and payment requirements
  before asking the user to approve or pay.
- Personal developer accounts created after November 13, 2023 currently need a closed test with at least 12 testers opted in
  continuously for 14 days, then must apply for production access. Confirm whether this account-specific rule applies before
  promising a production release.

## Assist the account holder

The agent should configure repository workflows, metadata, validation, and upload automation itself when authorized access exists.
Account creation, identity checks, payments, Play Console ownership, and certain API grants require the user. In those cases,
give exact, current console steps and official documentation links; tell the user precisely what to do without requesting private
keys or identity/payment documents in chat, then continue when they confirm.

Never promote to production without explicit approval. Verify the Play track and release status before reporting completion.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Android/Play API, auth, policy, pricing (account fee), track, testing-requirement
(depends on account type and creation date), and UI sources. Verify APIs, upload, credentials, and eligibility; preserve user rules,
update sources/date, and report changes. For console help, capture authorized
current screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- Android Publisher API: https://developers.google.com/android-publisher
- Android Publisher API authorization: https://developers.google.com/android-publisher/authorization
- Play Console account registration: https://support.google.com/googleplay/android-developer/answer/6112435
- Play Console testing requirements: https://support.google.com/googleplay/android-developer/answer/14151465
- Play Console API access: https://support.google.com/googleplay/android-developer/answer/9844686
- Android Publisher API edits: https://developers.google.com/android-publisher/api-ref/rest/v3/edits
- Google Cloud Workload Identity Federation for GitHub Actions: https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines
- Google authentication for GitHub Actions: https://github.com/google-github-actions/auth
