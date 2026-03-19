---
name: specify-proposal
description: "Author a proposal or ADR with options and trade-offs. Three options minimum (including do-nothing). Each option: descrip"
allowed-tools: [Read, Write, Edit, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Author a proposal or ADR with options and trade-offs. Three options minimum (including do-nothing). Each option: description, pros, cons, risk, effort. Recommendation section with rationale. Pulls from scout-feasibility if available. Stock roles: Architect (technical options), PM (business trade-offs).