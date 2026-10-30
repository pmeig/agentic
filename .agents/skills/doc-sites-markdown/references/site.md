# Markdown docs and docs sites: site

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
