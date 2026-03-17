---
name: prove-websearch
description: Web evidence gathering with direct quotes, URLs, and strength-of-evidence rating per source.
allowed-tools: [Read, Write, WebSearch, WebFetch]
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


Search the public web for evidence supporting or refuting the hypothesis. For each search: query used, sources found, evidence extracted (direct quotes with URLs), relevance to hypothesis, strength of evidence (strong/weak/mixed). Cite sources. Do not paraphrase without attribution. Do not use training data as evidence -- every claim must have a URL.

Write artifact to: simulations/prove/investigations/{topic}-websearch-{date}.md
