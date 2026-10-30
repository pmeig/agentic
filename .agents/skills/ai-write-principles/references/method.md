# ai-write-principles: method

The project's own rules win. English only (`ai-docs-in-english`).

## Method (always, in order)

1. **Reader and moment**: who reads it (which agent, which model size), when (every session, at a trigger, once), and what they must do differently afterwards. If no behaviour changes, do not write the file.
2. **Smallest file**: every line is paid again at each turn it is loaded. Always-loaded content in few lines, trigger-loaded content in a skill reference, rare content behind a link.
3. **One rule, one place**: link instead of copying; a rule duplicated in two files drifts.
4. **Write for a cold reader**: no "as discussed", no section numbers of another file, no pronoun without referent; name paths, commands, exact values.
5. **Say what to do**, then why in one clause when the reason is not obvious; positive instructions before prohibitions; a few hard "never/always", each with its reason.
6. **Concrete beats abstract**: one real example (input -> output, command -> result) per non-obvious rule; real paths and names from the project.
7. **Structure for scanning**: headings by need, tables for lookups (trigger -> file), numbered steps only for ordered procedures, bullets for parallel rules. No prose recap, no marketing tone, no emphasis inflation (MANDATORY/NEVER only for rules that really are).
8. **Write it, then test it**: hand the file to a cold agent (`Agent`, fresh context) with one realistic task; read what it did and where it hesitated; fix the file, not the task. A file never exercised is a draft.

