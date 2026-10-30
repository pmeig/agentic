# Team development rules: coverage target

- **Coverage target = what the CI gate measures** (read the workflow, ask `qa`): a measured module gets 100 %; an unmeasured one gets every logic condition tested in pure functions, no hours on compiler-generated branches (Compose) or a coverage tool.
- `qa` runs the unit tests and the Sonar report (`sonar-report`); a gap below 100 % on a measured module goes back to the code owner.
