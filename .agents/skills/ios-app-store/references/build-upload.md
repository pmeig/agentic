# iOS App Store Release: build, upload and TestFlight

- Configure the CI build to archive and export the expected signed artifact, validate version/build numbers, and upload to
  TestFlight before App Store submission.
- Use current supported Xcode tooling or the App Store Connect API for repeatable operations; verify endpoints, JWT requirements,
  and permissions from official docs before calling them.
- Apple documentation currently conflicts on direct binary upload: the upload guide and `POST /v1/buildUploads` describe API
  uploads, while the Apps API overview says direct uploads are not supported. Prefer Xcode or Transporter unless Apple's docs and
  the target account's behavior are reconciled.
