# Sonar report: read Sonar (URL, token, project key)

You need the **SonarQube URL**, a **token** and the **project key**. Take them from the project (`sonar-project.properties`, build
files, CI configuration, documented secret store). **A missing one: ask the lead** and wait; never guess a URL, look for a token
elsewhere, print or write one.

**Before asking, load the Sonar skill** (global `sonar` in `~/.agents/skills/`, then a repo skill): if one exists, follow it and do not ask.

**Once the lead has answered, write the skill so nobody asks again** (`run-and-access-skills`): a **global** skill `sonar` for the SonarQube server and where its token is read from, plus, for what is specific to the repo (project key, branch/PR scope), a **repo** skill. Never write it in `AGENTS.md` or the docs. It states how to get the quality gate:
- the SonarQube URL (from the PC and from CI runners if different);
- **where the token is read from** (Vault path and field, or environment variable) and how to read it in the same command that
  uses it. **Never write the token value** in the skill, the report or a repo;
- how to find the project key (and the known keys per project);
- the read-only calls that worked (quality gate, measures, files below 100 %, issues, hotspots) with the scope parameter
  (`pullRequest=<n>` or `branch=<name>`), and those refused for lack of privileges, with what to ask for;
- the up-check and how to start Sonar when it is down.

Keep it short, update it when the access changes, read it first next time. Never write secret values in it.

Once connected, read for the branch or PR: quality gate, coverage (overall and new code), uncovered lines per file, issues,
vulnerabilities, hotspots, duplication. Print `rule`, `file:line`, `message`, `severity`, never the raw answer. A read refused for
insufficient privileges: say so in the report and ask the lead for a token that can read it.
