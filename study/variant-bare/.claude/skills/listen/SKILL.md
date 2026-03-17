---
name: listen
description: "Team simulates post-ship feedback. Customer reactions, support ticket forecasts, and adoption curve simulation before the feature ships. Lightweight default.
"
allowed-tools: [Read, Write, Glob]
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


Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the spec through their lens. Per-persona feedback cards with severity (blocking/major/minor/cosmetic) and NPS prediction (1-10). Cross-persona theme matrix. Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. Stock roles: C-01 through C-12, PM, UX.

Write artifact to: simulations/listen/feedback/{topic}-feedback-{date}.md
