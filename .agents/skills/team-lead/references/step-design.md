# Lead playbook: step 2, design

2. **Design**: `designer` works per feature and per page (several features: one at a time), starting from the real screenshots in `.agents/docs/screens/` (skill `screen-library`); asks `front` only for what is missing. **3-5 mockups that really differ** (`design-mockup-variants`), desktop and mobile PNGs shown inline; the lead or user picks. Output `.agents/docs/team/<feature>/design/`.

- **Batch the user's feedback**: in design iterations gather the decisions into one `designer` round; the designer re-renders only the touched states (`design-mockup-render`, "Iterations").
- **No code before the mockup is chosen**: steps 3-4 start after the user validated a mockup or skipped the design. A design change after code exists is a new step 2.
- **Parity clients start together**: when the project requires parity (web + Android, twin e2e), launch every client in the same build message (mockups per client included); never "web first" unless the user asks.
- Gate: the user chose a mockup -> `designer` writes `brief-designer-front.md` and stops -> lead updates `state.md` and clears (`context-handoff`, `references/lead-launch.md`) -> step 3.
