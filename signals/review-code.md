iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


Multi-discipline code review of source files, PRs, or diffs. If a spec is provided, each discipline checks spec compliance. Per-discipline findings with code-level file:line annotations. Group findings by file. Identify patterns (e.g., "error handling inconsistent across 4 files"). Pass/fail per discipline. Amend: re-run affected disciplines on changed files only. Stock: 6 disciplines + auto-selected domain experts from language/framework context.

Write artifact to: signals/review/code/{topic}-code-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
