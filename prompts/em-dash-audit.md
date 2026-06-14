---
title: Em Dash Audit
description: Find and replace em dashes in every form across all project files, then update the writing style documentation.
meta: Claude Code Prompt
---

Audits every HTML page and documentation file in a project for em dashes in all three forms: the literal Unicode character, the `&mdash;` HTML entity, and double dashes used as punctuation. Each instance is replaced with the most context appropriate alternative (comma, colon, semicolon, parentheses, or period), while CSS custom properties such as `--color-bg` are left untouched because they are valid CSS variable syntax.

Use it after writing or importing content to enforce the project writing style in a single pass. The prompt also updates `docs/PRD.md` with a Writing Style section and ensures all patch notes and documentation files reflect the changes made.

## Prompt

```
Prepare a full audit of all HTML pages and documentation files in this project. Search for em dashes in both forms: the literal Unicode character — and the HTML entity &mdash;. These must be searched independently since a search for one will not catch the other. Also search for double dashes -- used as punctuation (but do not change CSS custom properties like --bg or --accent, which are valid CSS variable syntax).
Replace every instance found using the appropriate alternative based on context:
* Comma: the most natural replacement in most cases; keeps the sentence flowing without drawing attention to itself
* Colon: good when introducing a list, explanation, or elaboration after a complete clause
* Semicolon: useful when connecting two closely related independent clauses that could stand alone as sentences
* Parentheses: work well for asides or extra information that is supplementary rather than central to the sentence
* Period: sometimes the cleanest fix is splitting the sentence into two; shorter sentences are often clearer anyway
After fixing all instances, update docs/PRD.md to include a Writing Style section documenting this methodology, including the note that em dashes appear in both the literal character and HTML entity forms and both are prohibited. After making these changes, ensure the patch notes and documentation files are all up to date describing the changes you just made.
```
