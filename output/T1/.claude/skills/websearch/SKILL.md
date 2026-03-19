---
name: websearch
description: "Search the public web for evidence supporting or refuting the hypothesis. For each search: query used, sources found, ev"
allowed-tools: [Read, Write, WebSearch, WebFetch]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Search the public web for evidence supporting or refuting the hypothesis. For each search: query used, sources found, evidence extracted (direct quotes with URLs), relevance to hypothesis, strength of evidence (strong/weak/mixed). Cite sources. Do not paraphrase without attribution. Do not use training data as evidence -- every claim must have a URL.