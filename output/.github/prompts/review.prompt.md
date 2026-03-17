---
agent: 'agent'
tools: ['codebase']
description: 'Team validates the design. Expert and discipline review of specs and code. Persona walkthrough for usability. 12-customer-persona evaluation for adoption. Full default.
'
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


Multi-expert review of a design artifact through 6 standard disciplines and auto-selected domain experts. Auto-select 3-5 domain experts from content signals (e.g., spec mentioning RBAC selects a security architect). Per-reviewer findings with P1/P2/P3 severity. Consensus analysis (2+ reviewers flag same thing), split opinions, unique catches. Amend: address findings one by one, re-run specific reviewers on changed sections. Stock: 6 disciplines (architect, code-quality, documentation, testing, process, implementation) + domain experts.

Write artifact to: simulations/review/design/{topic}-design-{date}.md
