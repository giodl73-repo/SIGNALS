---
name: scout-market
description: Market sizing and segment ranking by fit score.
allowed-tools: [Read, Write, WebSearch]
param_set: standard
---
Size the addressable market and rank segments by fit. Use developer headcount for tooling segments, dollar TAM for platform/enterprise segments -- do not mix units in the same table. Scoring: pain severity, WTP, accessibility on 1-10 scale, equal weights, composite = average. Composite rank = fit score + (10 - GTM difficulty). Recommend beachhead segment with rationale. Stock roles: Strategy (TAM/SAM/SOM), PM (segment fit), GTM (go-to-market difficulty).

Write artifact to: simulations/scout/market/{topic}-market-{date}.md
