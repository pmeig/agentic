# Lead playbook: steps 3-4, contract and build

3. **Contract**: `front` reads the mockup and agrees `contract.md` (same folder as the need) with `back` (+ OpenAPI/schema when relevant). An element that cannot be built goes back to `designer` with reason and proposal.
4. **Build**: `back` and `front` implement in parallel; a contract change is agreed by both and written first. Each writes the unit tests of its code; `qa` runs them and the Sonar report (`sonar-report`); coverage < 100 % or any issue goes back to the owner.

- **Parallelize independent work, but price the context cost**: once the contract is written, `back`, `translator` (texts) and the `documentalist` skeleton start in the same message; only real dependencies are sequential. Load `references/parallelism.md` before splitting an agent into several.
- **Parity clients start together**: web + Android and twin e2e are launched in the same build message.
- **Peers and ownership**: give each agent the IDs of the others; if a message fails, hand over through `team/<feature>/handoff-<from>-<to>.md` and tell the lead. One file, one owner: in a shared file (`contract.md`) each author writes only their own section.
- **Split big builds**: when `front-plan.md` estimates a pass above ~30 min, split `front` by directory (helpers and state / components / sheets and shell), each agent committing only its paths.
- Agents load their own skills at their triggers (agent files); do not pre-load or list skills in launch prompts.
