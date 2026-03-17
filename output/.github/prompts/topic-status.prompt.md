---
agent: 'agent'
tools: ['codebase']
description: 'Terminal coverage display computed from signal glob against strategy.'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Show the current state of a topic in the terminal. Signal coverage, open gaps, readiness for target outcome. Does NOT write a file -- display only. For a written artifact use topic-report. Globs simulations/**/{topic}-* to discover all signals. Cross-references against strategy.md planned signals. Computes coverage percentage.

Write artifact to: none (terminal display only)
