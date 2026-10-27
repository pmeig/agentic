# iOS App Store Release: account, app record and signing

- Register the bundle identifier and required capabilities. Verify the existing certificates, provisioning profiles, entitlements,
  and signing team before changing signing.
- Prefer Xcode automatic signing when suitable; otherwise document certificate/profile ownership, renewal, and secure storage.
- Use App Store Connect API keys for automation only with the minimum required role and protected storage. Never commit API
  private keys, certificates, provisioning profiles, or signing credentials.
- App Store distribution currently requires Apple Developer Program membership. Apple lists US$99 annually, with local currency,
  taxes, and possible regional or educational waivers; verify the account's current enrollment price before asking for approval.
- Create an app record in the App Store Connect website before uploading a build; Apple says the API does not create app records.
- Apple documentation has differing role guidance for creating API keys. Verify the target account's Users and Access permissions
  rather than assuming an Account Holder/Admin role is sufficient.
