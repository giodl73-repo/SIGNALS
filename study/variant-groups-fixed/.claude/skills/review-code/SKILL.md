---
name: review-code
description: Multi-discipline code review with file-level annotations and pass/fail per discipline.
allowed-tools: [Read, Write, Glob, Grep]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


Multi-discipline code review of source files, PRs, or diffs. If a spec is provided, each discipline checks spec compliance. Per-discipline findings with code-level file:line annotations. Group findings by file. Identify patterns (e.g., "error handling inconsistent across 4 files"). Pass/fail per discipline. Amend: re-run affected disciplines on changed files only. Stock: 6 disciplines + auto-selected domain experts from language/framework context.

Write artifact to: simulations/review/code/{topic}-code-{date}.md
