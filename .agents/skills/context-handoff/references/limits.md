# Context handoff: cuts inside a step, images, output, lifetime

- Split work larger than ~30 min or ~40 files read into packages, one fresh agent each, each with its own brief (paths owned, checklist).
- Images: only the designer opens them, 3-4 per round, one board <= 1000 px wide, JPEG/WebP for review, PNG only for the final; never re-view an unchanged image; later agents get the final PNG path, opened at most once, at half scale (later agents open the final PNG once). The lead never views images except the 3-4 key boards for the user.
- Command output: quiet mode, `tail -n 30`, grep for failures; never paste logs into a brief or message.
- Output: tests and builds quiet (`tail`, failures and summary), no logs, lockfiles or generated files in a context. Reading: INDEX, `graph.yaml`, one feature file and the paths it names.
- Questions between agents: one line each way, written to the brief if the answer is lasting.
- Agent lifetime: one work package (~30 min, one concern); a long context is replaced by a fresh agent, never resumed more than once.
- Model: mechanical work (fixtures, renames, translations to apply, docs skeleton) on the smaller model.
