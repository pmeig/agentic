# Android Google Play Release: build and upload

- If using a community upload action, inspect its current defaults and explicitly configure a non-production test track and
  release status; do not rely on defaults that might publish to production.
- For Android Publisher API automation, create an edit, upload the bundle, update the intended track, then commit the edit.
  Committing applies the edit, so keep production-track commits behind explicit approval and protected deployment gates.
- Configure GitHub Environments and secrets/identity, build a signed AAB, validate version code/name, and upload to the selected
  test track before production.
- Keep release notes, artifacts, rollout percentage, and promotion steps tied to the version being released.
