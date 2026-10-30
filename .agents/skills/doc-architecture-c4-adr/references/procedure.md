# Architecture documentation: C4, arc42, ADR: procedure

## Procedure

1. Read build files, compose/CI files, deployment folders, `README.md`, existing diagrams.
2. Draw context, then containers, then deployment; components only for the container the task touches.
3. List cross-cutting concepts with the file that implements each (auth middleware, error handler, i18n loader, offline queue).
4. Recover or write ADRs for the decisions that shape the code; link them from the architecture file.
5. Verify every box maps to a folder or image and every arrow to real code or config; mark gaps `(unverified)`.
