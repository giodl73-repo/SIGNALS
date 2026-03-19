---
name: inertia
description: Deep analysis of the inertia competitor -- the option to do nothing. Why would teams keep their current workaround inste
allowed-tools: [Read, Write, Glob]
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


Deep analysis of the inertia competitor -- the option to do nothing. Why would teams keep their current workaround instead of adopting this feature? Maps: current workaround in detail, switching cost (time, training, disruption), inertia threat score (always HIGH by default), specific conditions under which inertia loses. This is the most important analysis in Signal. Every feature decision must answer: why does inertia lose? If you cannot answer that, stop. AMEND: quantify switching costs, identify specific workaround failure modes.

Write artifact to: simulations/discover/inertia/{{topic}}-inertia-{{date}}.md
Include frontmatter: skill: discover-inertia, topic: {{topic}}, date: {{date}}, inertia_score: HIGH|MEDIUM|LOW