---
name: ai-docs-in-english
description: MANDATORY before writing any file an AI reads (AGENTS.md, agents, skills, .agents/docs, memory, prompts, agent messages): English only.
---

# AI-facing documents are written in English

Everything that configures, instructs or informs an AI is written in **English**, in every project and for every agent.

## In scope (English)
- `AGENTS.md`, `CLAUDE.md`, agent definitions, skill files (frontmatter `name` and `description` included) and the files they ship.
- `.agents/docs/` (INDEX, graph.yaml, features, api, data, conventions, glossary, gotchas), `.agents/docs/team/<feature>/` (need, contract, gesture, design notes).
- Memory files and their index, slash commands, hook messages, prompts and system prompts of the application, tool and function descriptions, JSON-schema descriptions sent to a model, few-shot instructions.
- Messages between agents (`SendMessage`) and reports handed back to the lead.

## Out of scope (keep the language that fits)
- The conversation with the user: reply in the user's language.
- Text people read: UI strings, README and guides, changelog, store listings, release notes, emails, promotion copy; they follow the product language (`translator` reviews them).
- Code comments, logs and commit messages follow the project's convention.
- If an AI must *output* another language (for example narrate in French), write the instruction in English and state the output language explicitly ("Always answer the player in French").

## How to apply
1. Create AI-facing files directly in English, even when the request came in another language.
2. Keep exact identifiers, enum values, file names and domain words unchanged; give the English meaning next to a foreign domain word the first time (glossary).
3. Editing an existing AI-facing file written in another language: say so to the lead and offer to translate it; do not silently rewrite the whole file unless asked.
4. A document that serves both audiences is split: the AI part in English (`.agents/docs/`), the human part in the product language (README, guides).
