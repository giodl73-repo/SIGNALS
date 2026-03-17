---
name: signal-review-code
description: Multi-discipline code review with file-level annotations and pass/fail per discipline.
allowed-tools: [Read, Write, Glob, Grep]
param_set: full
---
Multi-discipline code review of source files, PRs, or diffs. If a spec is provided, each discipline checks spec compliance. Per-discipline findings with code-level file:line annotations. Group findings by file. Identify patterns (e.g., "error handling inconsistent across 4 files"). Pass/fail per discipline. Amend: re-run affected disciplines on changed files only. Stock: 6 disciplines + auto-selected domain experts from language/framework context.

Write artifact to: simulations/review/code/{topic}-code-{date}.md
