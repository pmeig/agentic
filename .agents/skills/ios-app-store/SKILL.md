---
name: ios-app-store
description: "Use to prepare, configure, test, release, or troubleshoot an iOS app distributed through App Store Connect."
---

# iOS App Store Release (router)

Use this skill when the selected deployment target is Apple's App Store. Follow current Apple Developer and App Store Connect
documentation; account requirements, API behavior, pricing, and console screens can change. Project rules win.
Load only the row(s) that match the task; never load every reference.

## Always (every use)

Never submit or release to production without explicit approval. Verify processing, TestFlight availability, and release status before reporting completion.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Start: bundle ID, signing method, versioning, approvals | `references/requirements.md` |
| Membership, app record, certificates, profiles, API keys | `references/account-signing.md` |
| CI archive, upload, TestFlight, upload conflicts | `references/build-upload.md` |
| Privacy, export compliance, screenshots, listing, review | `references/store-listing.md` |
| User must act in Apple account or console | `references/account-holder-help.md` |
| Monthly refresh, official sources | `references/maintenance.md` |
