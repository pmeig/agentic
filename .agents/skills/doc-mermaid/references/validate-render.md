# Mermaid diagrams: validate and render

## Validate and render

```bash
# validate / render one block or file (Node; as the project runs Node commands)
npx -y @mermaid-js/mermaid-cli -i diagram.mmd -o diagram.svg      # also .png / .pdf
npx -y @mermaid-js/mermaid-cli -i README.md -o out.md             # renders every mermaid block of a Markdown file
```

A parse error exits non-zero: use it as the check before delivering. Where Node is unavailable, state `(render not checked)`.
Keep the `.mmd` source; commit images only when a viewer cannot render Mermaid.
