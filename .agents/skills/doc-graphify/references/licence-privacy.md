# Graphify: licence, privacy and cost checks

## Check before adopting (ask the lead; record in an ADR)

1. **License**: sources report Creative Commons **BY-NC-SA 4.0** (non-commercial, share-alike). Read the repository `LICENSE` first; a
   commercial or client project may not be allowed to use it. Personal/internal use is the lead's call.
2. **Source of truth**: two repositories are cited (`safishamsi/graphify` and `Graphify-Labs/graphify`, the company is Graphify Labs, YC S26);
   take the one the PyPI package `graphifyy` (two y) points to, and confirm the name on PyPI before installing.
3. **Privacy**: code is parsed locally with tree-sitter (no API call); docs, PDFs, images and video are processed by the model of the
   current assistant session, so their content leaves the machine like any prompt. Exclude secrets, `.env`, customer data and
   private documents (`.graphifyignore` or the tool's ignore mechanism: check the current docs for the file name).
4. **Cost**: AST extraction is free; semantic extraction of documents consumes tokens: say so before running on a large doc set.
