# Sonar report: fixes, the owner of the code does them

Leave the loop only at **coverage 100 % and 0 issue / 0 vulnerability / 0 hotspot**. Otherwise:
1. Owner from the file path: front-end module → `front`, back-end module / SQL → `back`, test or e2e file → `qa`; a shared file →
   the agent who last changed it.
2. Send them (`SendMessage`) the exact items (file, lines, rule, message, uncovered lines). They fix with the smallest change, add
   tests or fix the code, one commit per round.
3. `qa` reruns the tests and Sonar; loop.
4. Stop and report to the lead after two identical failures of the same item, or when a fix would change a behavior or `contract.md`.
