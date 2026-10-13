---
title: Add Prompt
description: Add a new prompt to the site from its raw text: Claude Code writes the title and description, builds the page, runs the checks and logs the change.
meta: Claude Code Prompt
---

Takes a raw prompt text and handles the full addition workflow: writes the title and one-sentence description, creates the source file in `codes/prompts/md/`, adds it to the list order in `scripts/prompts/build.py`, rebuilds the pages and the site nav, runs the build check and the browser test, and adds a version entry to the site's `docs/PATCHNOTES.md`.

Use it when adding any new prompt to the site. Paste the prompt text below the `Prompt:` label before running.

## Prompt

```
Add this new prompt to the website. Follow the process and rules in @codes/prompts/docs/PRD.md, and the site-wide rules it points to in @docs/PRD.md. Check the prompt text against the content and writing rules before adding it, and tell me about anything you changed or would change. Add a version entry to @docs/PATCHNOTES.md. When you are done, run the build and the checks the prompts PRD lists, tell me which passed, and count every length limit with a script rather than by eye:

Title: Generate a title based on the prompt that I have provided.

Description: Generate a description based on the prompt that I have provided.

Prompt:
```
