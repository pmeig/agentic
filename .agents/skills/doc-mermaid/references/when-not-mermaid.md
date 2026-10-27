# Mermaid diagrams: when not Mermaid

## When not Mermaid

| Need | Alternative |
|---|---|
| Very large or precisely laid-out architecture, many nested boxes | D2 or PlantUML + C4-PlantUML, Structurizr DSL (model once, many views) |
| Hand-drawn whiteboard feel, workshops | Excalidraw (`.excalidraw` JSON, exports SVG) |
| Pure graph analysis (dependencies) | Graphviz `dot`, or tool output (`doc-code-analysis`) |
Check that the viewer of the readers renders the chosen tool; otherwise export SVG and keep the source beside it.
