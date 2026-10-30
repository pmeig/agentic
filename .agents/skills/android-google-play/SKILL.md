---
name: android-google-play
description: "Use to prepare, configure, release, or troubleshoot an Android application distributed through Google Play."
---

# Android Google Play Release (router)

Use this skill when the selected deployment target is Google Play. Follow current official Android and Play Console guidance;
fees, policies, API behavior, and console screens can change. Project rules win. Load only the row(s) that match the task; never load every reference.

## Always (every use)

Never promote to production without explicit approval. Verify the Play track and release status before reporting completion.

## Need -> file

| Need (what the agent is doing) | Load |
|---|---|
| Start: package name, signing, versioning, track, approvals | `references/requirements.md` |
| Play Console app, Play App Signing, API access, CI identity, fee | `references/account-signing.md` |
| Signed AAB, upload action, Publisher API edits, GitHub Environments | `references/build-upload.md` |
| Test tracks, closed-test and production-access rules | `references/test-tracks.md` |
| User must act in Play Console or account | `references/account-holder-help.md` |
| Monthly refresh, official sources | `references/maintenance.md` |
