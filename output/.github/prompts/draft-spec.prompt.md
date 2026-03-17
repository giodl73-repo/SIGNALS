---
agent: 'agent'
tools: ['codebase']
description: 'Specification authoring with guided section structure and self-review.'
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


Author a specification from intent with guided section structure. Pulls context from any scout signals for the topic. Guided section authoring: purpose, requirements (from scout-requirements if available), design, constraints, open questions. Self-review on completion: flag open questions, gaps, and ambiguity. Stock role: Architect.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md
