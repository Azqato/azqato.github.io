---
title: App Performance
description: Measure where an app is really slow at startup, opening screens, loading content and scrolling, fix the biggest gaps, and prove each fix.
meta: Claude Code Prompt
---

Makes an app feel faster in the four places people notice: how long it takes to start, how fast each screen opens, how quickly its content appears, and how smoothly it scrolls, including long lists and older content further back.

Claude measures before it changes anything. It reads the project, works out what kind of app it is (web, mobile or desktop) and how it can be run and timed, then records a baseline with the same steps repeated several times. From those numbers, and a profile of the slowest paths, it ranks where the real gap is rather than guessing.

It then fixes one thing at a time, smallest owner first, and benchmarks after each fix the same way as before. A fix stays only if its numbers improve beyond the normal run-to-run noise; anything else is undone. Nothing is made faster by removing a feature or content.

It ends with a before and after table for every fix, the tests and build it ran, and a plain list of what it could not measure.

## Prompt

```
Make this app faster where people feel it: startup, opening each screen, loading content, and scrolling, including long lists and older content. Measure before changing anything, change one thing at a time, and keep a fix only if the numbers prove it.

Read first
- Read the project's own instructions, README and build files before acting, and follow any testing or performance rules they set.
- Work out what kind of app this is (web, mobile, desktop or other), how to build and run it locally, and which tools can time it: the browser's performance tools, a platform profiler, the framework's own tracing, or a small script.
- List the main screens and the content each one loads, and where the data comes from (network, database, cache, files).
- If you cannot run or time the app, or cannot tell which screens matter most, stop and ask me. Do not guess numbers.

Measure a baseline
- Use a production-like build where the project allows it, and run against a local copy, never the live service or real users' data.
- Write the measurement down as a repeatable script or a fixed list of steps, so the after numbers are taken exactly the same way.
- Record, with a command or script, never by eye:
  - Startup: time to the first screen people can use, cold and warm.
  - Each main screen: time from the tap or click to the screen being usable.
  - Content: time until the screen's data is shown, for recent and for older items.
  - Scrolling: frame times or dropped frames while scrolling a long list at a steady speed.
  - Supporting numbers where available: bundle or binary size, number and size of network requests, main-thread blocking time, memory.
- Run each measurement at least 3 times and report the median and the spread. Note the device, build type and network setup used.
- Profile the slowest paths and note what owns the time: a large bundle, blocking work at startup, repeated or chained requests, missing caching or pagination, heavy rendering or re-rendering, oversized images, slow queries, or long lists drawn in full.

Find the real gap
- Rank the problems by how much time they cost people, from the measurements, not from what looks slow in the code.
- Keep what you measured separate from what you suspect from reading the code. Mark anything unmeasured as unknown.

Fix one at a time
- Start with the biggest measured gap. Change the smallest piece of code that owns it, using what the project already has (its router, data layer, cache, list component) before adding anything new.
- Ask before installing any new dependency.
- Typical fixes: defer or split work that is not needed for the first screen; load data in parallel instead of one request after another; cache or prefetch what the next screen needs; paginate or virtualize long lists; load older content in pages and index the queries behind it; size and compress images; stop needless re-renders.
- After each fix, rerun the same measurement. Keep the fix only if it improves the target number by more than the run-to-run spread and no other measured number gets worse. Otherwise undo it and say so.
- Never make a number pass by removing a feature, content, or animation people can see, by hiding loading behind a spinner, or by measuring a different way than the baseline.

Verify
- Rerun the full baseline at the end, the same way, on the same setup.
- Run the project's tests, lint and build, and use the main flows (open each screen, scroll, search, go back) to confirm nothing broke. Check the console or logs for new errors.

Report, in this order:
1. Findings: the ranked gaps with their measured cost, and what could not be measured.
2. A table with one row per fix: what changed, the file, the number it targeted, before (median and spread), after, and kept or undone.
3. The final before and after for startup, each screen, content loading and scrolling.
4. The checks run and whether each passed.
5. What is left: gaps not fixed, and why.

Do not commit anything.
```
