# Code analysis for documentation: features by layer

## Features by layer

Feature-first projects keep a feature in one folder per module (`pages/<name>/`, `features/<name>/`): list them, then for each find
the layers. Method:
1. Start from the **entry points**: UI routes/screens, HTTP routes, queue consumers, scheduled jobs, CLI commands.
2. Follow the calls down: controller → service → repository → client (grep the imported names).
3. Collect the **change set**: files that import each other inside the feature + translation keys + tests + migrations.
4. Tests per feature: unit tests mirroring the source path, e2e specs by feature folder; note the command to run just them.

Also load `references/routes.md` for the grep patterns of entry points.
