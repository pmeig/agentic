---
name: ios-app-store
description: Use to prepare, configure, test, release, or troubleshoot an iOS app distributed through App Store Connect.
---

# iOS App Store Release

Use this skill when the selected deployment target is Apple's App Store. Follow current Apple Developer and App Store Connect
documentation; account requirements, API behavior, pricing, and console screens can change.

## Gather requirements

- Confirm bundle identifier, Xcode/project setup, signing method, version/build-number policy, App Store Connect app status,
  target TestFlight/App Store track, regions, and release timing.
- Ask whether the Apple Developer Program membership, App Store Connect app record, team roles, and App Store Connect API access
  already exist.
- Confirm explicit approval before membership fees, changing signing identities, submitting for review, or releasing to production.

## Configure the release path

- Register the bundle identifier and required capabilities. Verify the existing certificates, provisioning profiles, entitlements,
  and signing team before changing signing.
- Prefer Xcode automatic signing when suitable; otherwise document certificate/profile ownership, renewal, and secure storage.
- Use App Store Connect API keys for automation only with the minimum required role and protected storage. Never commit API
  private keys, certificates, provisioning profiles, or signing credentials.
- Configure the CI build to archive and export the expected signed artifact, validate version/build numbers, and upload to
  TestFlight before App Store submission.
- Complete required privacy details, export-compliance responses, age rating, store listing, screenshots, and review information.
- Use current supported Xcode tooling or the App Store Connect API for repeatable operations; verify endpoints, JWT requirements,
  and permissions from official docs before calling them.

## Assist the account holder

The agent should configure project files, CI workflows, metadata, validation, and upload automation itself when authorized access
exists. Apple account ownership, two-factor authentication, agreements, payments, team invitations, and App Review require the
user. Give exact, current App Store Connect/Apple Developer steps and official documentation links; use current interface
screenshots when an authorized browser/screenshot tool is available. Never ask for Apple IDs, passwords, private keys, or recovery
codes in chat. Continue the setup after the user completes required account actions.

Generate store screenshots from the actual app/simulator at the required device sizes; never fabricate app screenshots. Redact
account identifiers and personal data in console walkthroughs.

Never submit or release to production without explicit approval. Verify processing, TestFlight availability, and release status
before reporting completion.

## Apple-specific constraints

- App Store distribution currently requires Apple Developer Program membership. Apple lists US$99 annually, with local currency,
  taxes, and possible regional or educational waivers; verify the account's current enrollment price before asking for approval.
- Create an app record in the App Store Connect website before uploading a build; Apple says the API does not create app records.
- Apple documentation currently conflicts on direct binary upload: the upload guide and `POST /v1/buildUploads` describe API
  uploads, while the Apps API overview says direct uploads are not supported. Prefer Xcode or Transporter unless Apple's docs and
  the target account's behavior are reconciled.
- Apple documentation has differing role guidance for creating API keys. Verify the target account's Users and Access permissions
  rather than assuming an Account Holder/Admin role is sufficient.
- Privacy disclosures and export-compliance classifications require truthful, informed owner input. The agent may gather evidence
  and prepare reviewed metadata but must not infer or attest to the organization's legal or data-handling position.
- Recheck Apple's current Xcode upload requirement, screenshot specifications, TestFlight limits, and API behavior monthly;
  requirements can change.

## Monthly refresh

Last refreshed: 2026-10

At first use in a later month, recheck official Apple/App Store API, Xcode, pricing, and UI sources. Verify APIs, JWT, commands,
signing, and requirements; preserve user rules, update sources/date, and report changes. For UI help, capture authorized current
screens with sensitive data redacted, or disclose unavailable access and provide official links/navigation.

## Official sources

- Apple Developer Program enrollment: https://developer.apple.com/help/account/membership/program-enrollment/
- Create an App Store Connect app record: https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app/
- App Store Connect API overview: https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api/
- App Store Connect API Apps collection: https://developer.apple.com/documentation/appstoreconnectapi/apps
- API key creation: https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api
- API JWT generation: https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests
- Upload builds: https://developer.apple.com/help/app-store-connect/manage-builds/upload-builds/
- Build upload endpoint: https://developer.apple.com/documentation/appstoreconnectapi/post-v1-builduploads
- Xcode distribution: https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases
- TestFlight overview: https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/
- App privacy details: https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/
- Export compliance: https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance/
- Screenshot specifications: https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/
- GitHub-hosted runners: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
- GitHub Actions secrets: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
- GitHub Actions secure use: https://docs.github.com/en/actions/reference/security/secure-use
