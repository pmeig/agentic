# Push, pull request and CI: before every push, PR creation or CI rerun

The machine must be free. Runners and local tests share the machine. Check **both**: no CI run in progress (any branch) and no e2e pid file of a live local run (`e2e-run`, `references/free-machine.md`). Something blocks: wait (a background until-loop), do not kill another run, tell the user what blocks. Free: wait 30 seconds, check again, launch only if still clean.
