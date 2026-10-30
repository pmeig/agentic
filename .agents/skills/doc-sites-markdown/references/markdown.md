# Markdown docs and docs sites: markdown

## Plain Markdown first

Most projects need only `README.md` + `docs/*.md` rendered by GitHub. Stay there until there are 15+ pages, several audiences, search
needs, versions or a public audience. GitHub Markdown renders tables, task lists, alerts (`> [!NOTE]`), footnotes, Mermaid, math and
relative links; keep to that subset for portability.

Layout (Diátaxis, see `documentation-human`):
```
docs/
  index.md                 landing, links by reader
  getting-started.md
  tutorials/  how-to/  reference/  explanation/
  architecture.md  decisions/
  user-guide/  operations/  contributing/
  assets/                  images, with alt text
  ai/                      AI documentation (documentation-ai), not part of the site navigation
```

## Checks

`npx -y markdown-link-check`, `lychee`, the generator's strict build (`mkdocs build --strict`, Docusaurus `onBrokenLinks: 'throw'`),
`markdownlint-cli2` for style when the project uses it. Node commands run as the project requires.
