# Skills layout: router + references (lazy loading)

Rule: an agent loads the strict minimum for the task. A skill is cheap to discover (frontmatter), cheap to open (router), and only the needed reference is read.

## Layout

```
.agents/skills/<name>/
  SKILL.md              router: frontmatter + "Need -> file" table (about 1-1.5 KB)
  references/<need>.md  one self-contained need per file (about 1-4 KB)
  scripts/              optional, executed not read
```

## SKILL.md (router)

- Frontmatter `name`, `description` (quoted when it contains `: `). The description says when to use the skill, never its content.
- Optional `Always` block: only rules that apply to every use (a few lines).
- `Need -> file` table: situation (what the agent is doing or which step) -> `references/<file>.md`.
- No procedure in the router. A router over about 1.5 KB is a sign content should move to a reference.

## references/<need>.md

- Title `# <Skill title>: <need>`; self-contained (no "see below", no section numbers of another file; cite `references/<file>.md`).
- One need per file, named by the need (`setup`, `tests`, `code`, `structure`, `flaky`, `report`...). Stack skills use the same names so agents can guess them.
- A rule lives in one file only; others cite it.

## When to split

- Split when a skill is over about 3 KB or serves several distinct needs (create, write code, test, maintain).
- Keep whole a small skill with a single need (design-*, language-*, translation-<pair>, sonar-<language>, e2e-<tool>, deployment-*).

## Agent side

Each agent file has a "Skills" table: Trigger -> skill -> reference. A skill not in the table is loaded only when the owner of the need says so. `AGENTS.md` carries only the lazy-loading rule and the cross-role rules.

## Checklist after splitting

- Every router row points to an existing file; no reference is orphaned.
- No line of the original lost (compare against git HEAD).
- Citations of the old sections ("section 2", "rule 1", "below") updated to `references/<file>.md`.
