# Context handoff: strict minimum per agent (Read / never read)

| Agent | Reads | Never reads |
|---|---|---|
| `designer` | `need.md`, screens `INDEX.md` + the PNGs of the pages concerned, design-system tokens | code, contract, tests, other features |
| `front` | `brief-designer-front.md`, `design/spec.md` + final PNGs, `contract.md`, the page's directory, `core` APIs it names | proposal HTML, render HTML, back code, other pages |
| `back` | `contract.md`, `brief-front-back.md`, the module and tables it names | mockups, front code, e2e |
| `qa` | `gesture.md`, impacted e2e files, runner output tail | mockups, source code except ids named in `gesture.md` |
| `documentalist` | `brief-*-documentalist.md` (files/routes/tables touched), INDEX, `graph.yaml`, the feature file | the whole repo; it updates only what the brief lists |
| `translator` | key list with screen, tone, sentence type, length limit, target language | code, design |
| `sales` | `need.md`, final spec summary, store/brand facts | code |
