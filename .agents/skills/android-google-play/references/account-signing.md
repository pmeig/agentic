# Android Google Play Release: account, app signing and CI identity

- Create/register the app in Play Console, complete required store listing and policy declarations, and configure Play App Signing
  and upload-key ownership. Never generate, replace, or expose a signing key without explicit user approval.
- Enable the required Play Developer API and link a least-privilege service identity through Play Console API access.
- Prefer short-lived CI credentials and the currently supported secure authentication method; do not commit service-account JSON,
  keystores, passwords, or signing keys.
- Prefer GitHub OIDC with Google Workload Identity Federation over service-account JSON keys. The
  `google-github-actions/auth` action is maintained outside Google; verify its current security and support posture before use.
- Google currently lists a one-time US$25 developer-account registration fee; verify the current fee and payment requirements
  before asking the user to approve or pay.
