# Mermaid diagrams: rules that keep diagrams useful

## Rules that keep diagrams useful

1. **One diagram = one question**, 5 to 15 nodes. More: split by layer or feature and link the pieces.
2. **Real names**: use the identifiers of the code (class, route, table) so an AI can grep them; label arrows with the verb or payload.
3. **Direction**: `LR` for flows and pipelines, `TD` for hierarchies; sequence diagrams read top to bottom in time order.
4. **Stable ids, readable labels**: `svc[OrderService]`; quote labels with punctuation `A["POST /orders (auth)"]`.
5. **Source of truth in text**: put a one-line caption above the block saying what it shows and its commit/date.
6. Do not rely on colors alone (accessibility): use shapes or labels too; keep styling minimal (`classDef` only for 2 to 3 groups).
7. For an AI, a table next to the diagram (node | path) is worth more than extra styling.
