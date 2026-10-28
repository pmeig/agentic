# Run and access: what to do when blocked

1. **Look for a skill first**: the global folder (`~/.agents/skills/`), then the repo's `.agents/skills/`. If one covers it, load it and follow it: do not ask.
2. **Look in the repo** (README, scripts, CI configuration, package/build files): if the answer is there, use it **and** write the skill so nobody searches again.
3. **Still missing: ask the lead once**, in one grouped message (what you need to run or reach, what you tried, the exact error). Never guess a URL, a path or a command that changes something; never go looking for a secret elsewhere.
4. **Write the skill** as soon as it works (see `references/template.md`), and tell the lead where the file was created. Writing a global skill creates a file outside the repo: say so.
5. **Maintain it**: when the command, the path or the access changes, update the skill the same day; fix a skill that turned out wrong.
6. **Container tools are installed once** (JDK, Gradle, Android SDK, browsers, local database): record the commands in the repo's SessionStart hook or a repo skill, never reinstall per agent.
