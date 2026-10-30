# Dart / Flutter best practices: setup

- Latest stable Flutter/Dart 3 (FVM or `.fvmrc` to pin), `analysis_options.yaml` with `flutter_lints` or `very_good_analysis`, `dart format` + `flutter analyze` in CI, null safety everywhere.
- Layout: `lib/main.dart` (wiring), `lib/pages/<name>/<name>_page.dart` + view model + widgets, `lib/core/<kind of feature>/` (data, network, storage, auth, ui, l10n), `test/` mirroring `lib/`.
