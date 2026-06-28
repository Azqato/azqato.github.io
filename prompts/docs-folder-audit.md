---
title: Docs Folder Audit
description: Crawl the entire codebase, then audit and rewrite every document in /docs to match the current state of the project.
meta: Claude Code Prompt
hidden: true
---

Scans the entire codebase first to build a complete picture of the project, then opens every document in `/docs` and compares it against what was found. Anything outdated, missing, inaccurate, or incomplete gets rewritten. Every file in `/docs` is reviewed without exception.

Use it when documentation has drifted from the codebase, after a significant refactor, or when you need to verify that the `/docs` folder can stand alone as a complete reference for a new contributor or AI model.

## Prompt

```
Perform a full documentation audit of the /docs folder. Your goal is to ensure every document accurately reflects the current state of the codebase with no gaps, outdated information, or missing coverage.
Steps to follow:

Crawl the entire codebase and build a complete picture of what exists: all files, features, components, routes, configs, and logic.
Open every document in /docs one by one.
For each document, compare its content against the actual codebase and identify anything that is outdated, missing, inaccurate, or incomplete.
Rewrite or update each document so it is fully accurate and comprehensive based on the current version of the site.
Do not skip any document. Every single file in /docs must be reviewed and updated.
After all documents are updated, provide a summary of what changed in each file and why.

Standards to uphold:

Every document should be thorough enough that a new contributor or AI model can understand the project entirely from the /docs folder alone.
If a document is missing a section that the codebase clearly warrants, add it.

Make sure to perform a full codebase scan before touching any documentation.
```
