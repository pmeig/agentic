# Run and access: skill template

Copy and fill in; delete sections that do not apply. Rules: English; short; verified by running once (or marked `(not run)`); no secret value, token, password or private key in the file, in the report or in a command that gets logged; one skill per tool or topic.

~~~markdown
---
name: <tool-or-topic>
description: "Use when <situation that needs it>: <what it gives>."
---
# <Title>

## Run
Exact commands, copy-pasteable, with the wrapper or version selector the machine needs,
working directory, and what success looks like.

## Connect
URL / host / port, the account or role, **where each secret is read from**
(secret store path and field, or environment variable) and how to read it in
the same command that uses it. Never the value.

## What worked / what is refused
Calls that work; calls refused for lack of privileges and what to ask for.

## Up-check and start
How to know the service is up; how to start it when it is down.

## Pitfalls
Known failures with their cause and fix.
~~~
