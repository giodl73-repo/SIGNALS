---
name: draft-proposal
description: Proposal or ADR with three-option minimum and recommendation rationale.
allowed-tools: [Read, Write, Edit, Glob]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


Author a proposal or ADR with options and trade-offs. Three options minimum (including do-nothing). Each option: description, pros, cons, risk, effort. Recommendation section with rationale. Pulls from scout-feasibility if available. Stock roles: Architect (technical options), PM (business trade-offs).

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md
