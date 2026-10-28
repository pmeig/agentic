# Context handoff: an agent starts or finishes a package

## Starting (agent)

The next agent reads: its agent file, the brief, the paths in **Read**. Nothing else unless the brief is insufficient: then it asks the previous owner by `SendMessage` (answer one line, written to the brief) instead of exploring. What your role may read: `references/read-minimum.md`.

## Finishing (agent)

The finishing agent writes `brief-<from>-<to>.md` (format: `references/files.md`), deletes its scratch (unchosen proposals, render HTML, temporary boards; nothing is moved to an archive folder), reports in 3 lines to the lead with the brief path, and **stops**. It is not resumed (at most once, for a fix of its own deliverable).
