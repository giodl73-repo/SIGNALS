---
name: topic-new
description: Topic registration with strategy planning and signal coverage plan.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Register a new topic, define its strategy, plan the signals needed for design commit. Output: entry in TOPICS.md, strategy.md in simulations/{topic}/. Strategy lists planned signals with namespace, skill, item name, owner role, and priority (essential/recommended/optional). The strategy is the editorial plan for the topic's investigation.

Write artifact to: simulations/{topic}/strategy.md
