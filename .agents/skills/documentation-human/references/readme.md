# Documentation for humans: README skeleton

## README skeleton (project and each module)

Every README has the architecture: a diagram, the annotated folder tree and a table of layers.

1. Title, one-sentence purpose, status badges only if they are real and maintained.
2. **What it does**: 3 to 6 lines, the main features.
3. **Architecture**: a Mermaid diagram of the modules and flows (`doc-mermaid`), the annotated folder tree, and a table of layers
   (layer | folder | responsibility). Link to `.agents/docs/structure.md` rather than duplicating it.
4. **Quick start**: prerequisites with versions, install, run, test; commands copy-pasteable and checked.
5. **Configuration**: environment variables and secrets by name (never values), where they live.
6. **Features / modules**: table with a link to each module README or feature doc.
7. **Tests and quality**: how to run unit and e2e, coverage and Sonar targets.
8. **Deployment**: how it ships, environments, links to the CI/CD.
9. **Contributing and license**.
A module README repeats only 3, 4 and 7 for that module and links up to the root README.
