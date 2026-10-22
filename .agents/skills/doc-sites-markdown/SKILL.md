---
name: doc-sites-markdown
description: Use when human docs outgrow a few Markdown files or must be published: layout, docs site generator choice, link checks, deployment.
---

# Markdown docs and docs sites

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

## Choosing a site generator

| Tool | Choose when | Notes (verify at refresh) |
|---|---|---|
| **Docusaurus** | React team, versioned docs, blog, i18n, large community | Node; MDX; Mermaid via `@docusaurus/theme-mermaid`; search plugin |
| **Astro Starlight** | fast static docs, good defaults, i18n, accessibility | Node; Mermaid via a plugin |
| **VitePress** | Vue/Vite team, light and fast | Node; Mermaid via plugin |
| **MkDocs Material** / **Zensical** | Python team, Markdown-only, great search | the MkDocs Material team announced **Zensical** as its successor and mkdocs-material is to be minimally maintained until late 2026: for a new site evaluate Zensical, keep existing MkDocs sites working |
| **GitHub Pages + Jekyll / plain** | tiny public site | no build tooling |
| **Hugo** | many pages, speed, Go | templating learning curve |
Recommend with pros and cons grounded in the project's stack, host (the team's self-hosted runners and Freebox VM or GitHub Pages),
languages and effort; the lead decides and the choice goes into an ADR (`doc-architecture-c4-adr`). Never add a site generator the
lead did not approve.

## Site rules

- Source in the repo (`docs/`), build in CI, output not committed. Navigation file (`mkdocs.yml`, `sidebars.ts`, `astro.config.mjs`) lists pages by Diátaxis kind.
- Reference pages generated: OpenAPI rendered by the site (Redoc/Scalar plugin) from `.agents/docs/api/openapi.yaml`, so there is one source.
- Mermaid enabled; diagrams stay as text.
- Search on, dark mode on, mobile layout checked; headings in order; alt text on images; language switch if the docs are translated.
- Deploy: GitHub Pages workflow or the project's CI/CD; the docs build is a CI check (broken links fail it).
- Public site: add `llms.txt` (`doc-ai-context-files`) and a sitemap.

## Checks

`npx -y markdown-link-check`, `lychee`, the generator's strict build (`mkdocs build --strict`, Docusaurus `onBrokenLinks: 'throw'`),
`markdownlint-cli2` for style when the project uses it. Node commands run as the project requires.

## Sources

- https://diataxis.fr · https://docusaurus.io · https://starlight.astro.build · https://vitepress.dev · https://squidfunk.github.io/mkdocs-material · https://zensical.org
- https://docs.github.com/en/get-started/writing-on-github

## Monthly refresh

Last refreshed: 2026-10 (Zensical vs MkDocs Material transition under way). At first use in a later month: re-check each generator's
status and latest version, Mermaid support, GitHub Markdown features; update the table, set the date, report changes.
