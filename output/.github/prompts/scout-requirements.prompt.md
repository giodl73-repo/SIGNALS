---
agent: 'agent'
tools: ['codebase']
description: 'Requirements extraction with MoSCoW prioritization and dependency graph.'
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


Extract and prioritize requirements from a product concept. Search for prior scout signals in BOTH simulations/scout/ (real runs) AND simulations/trace/skill/ (hand-compiled traces) -- never silently skip the trace directory. MoSCoW prioritization. Dependency graph (which requirements block others). Ambiguity flags (requirements needing clarification). Suspicious silences (areas with no requirements). Stock roles: PM (user-facing), Architect (technical), UX (usability), Compliance (regulatory).

Write artifact to: simulations/scout/requirements/{topic}-requirements-{date}.md
