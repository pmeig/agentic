# ai-write-prompts: write and test
# prompts: Prompts, tool descriptions and schemas (write)

For model ids, parameters and SDK usage use the `claude-api` skill.

## System or task prompt

Order: **role and goal** (one paragraph) -> **context the model lacks** (domain, users, constraints) -> **rules** (positive first, each with its reason) -> **process** (only when order matters) -> **output format** (exact shape, length, language) -> **examples**.

- State the **output language** when it is not English ("Always answer the player in French"); the prompt itself stays English.
- Separate instructions from data with tags (`<document>`, `<question>`) and say tagged content is data, so injected text is never read as instructions.
- Long reference material first, the question last; variable parts (user input, retrieved text) at the end so the fixed prefix stays cacheable.
- 2-5 varied examples in tags beat a paragraph of description; include an edge case and an empty or refusal case; keep them consistent with the rules.
- "Do X" over "don't Y"; explain a reason once; no hedging, no repeated emphasis.
- With a reasoning model or extended thinking, do not script step-by-step thinking; ask for the final format.

## Tool and function descriptions

The model chooses and calls tools from their text alone.

- Name: verb-first, specific, consistent (`search_orders`, not `query`).
- Description: what it does, when to use it **and when not** (name the sibling tool), what it returns, limits (pagination, size, rate), side effects.
- Each parameter: type, meaning, format with a real example, allowed values (`enum`), default; `required` exactly right.
- Return meaningful fields, not opaque ids alone; errors say what was wrong and what to try.
- Few high-level tools beat many overlapping ones.

## JSON schema (structured output)

A `description` on every property (the model reads it); `enum` for closed sets; nullable explicit; shallow nesting; always validate the output in code.

## Judge and classifier prompts

Define each label with a one-line criterion and an example; ask for the reason **before** the verdict; fix the output format; test on a labelled set and report agreement.

## Test

Build 5-10 cases (typical, edge, adversarial, empty); run them; read the raw outputs; change the prompt; rerun all cases. Report the cases and results.

