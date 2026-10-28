# Context handoff: SendMessage rules

Every character in a SendMessage is paid again on every subsequent turn. Be surgical.

## When to send vs write to a file

| Situation | Action |
|---|---|
| Question whose answer is a lasting rule, path or decision | Write to brief or state.md; send the path only |
| Question whose answer is a one-shot value or status | SendMessage one line; answer in one line |
| Failure report from qa to front or back | SendMessage with structured block (see below) |
| QA go or blocked to lead | One-line format (see below) |
| Lead launching the next agent | Prompt <= 10 lines: role, state.md path, brief path, done criteria only |

## Rules

- **Batch all questions in one message**: never send two messages when one covers them; numbered list, max 5 questions.
- **One line per question, one line per answer**: if the answer is a lasting rule, write it to the brief and send only the path.
- **Never paste file content**: send the path and the relevant line range (`path:L10-L20`).
- **Never paste command output**: send `tail -n 20` of the output and the path to the full log file.
- **Confirm in one word** when nothing more is needed: "done", "go", "fixed", "ack".

## Failure report format (qa -> front or back)

One block per failure; send all failures in one message:

~~~
FAIL <scenario-name>
step: <number and action>
expected: <result>
actual: <result>
trace: <path to trace or screenshot>
owner: front | back
~~~

More than 3 failures: write them to `.agents/docs/team/<feature>/qa-failures-<n>.md` and send the path only.

## QA go / blocked format (qa -> lead)

- Go: `PR go — <n> green, coverage 100 %, 0 Sonar issue`
- Blocked: `BLOCKED — <reason in 5 words>, owner: front | back`
