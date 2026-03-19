---
name: code
description: Multi-discipline code review of source files, PRs, or diffs. If a spec is provided, each discipline checks spec complian
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Input type:  [full files | PR diff | diff range]
Mode:        [FULL REVIEW | AMEND RUN]
Files:       [list all files in scope, one per line]