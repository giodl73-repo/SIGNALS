---
name: signal-topic-new
description: Topic registration with strategy planning and signal coverage plan.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
Register a new topic, define its strategy, plan the signals needed for design commit. Output: entry in TOPICS.md, strategy.md in simulations/{topic}/. Strategy lists planned signals with namespace, skill, item name, owner role, and priority (essential/recommended/optional). The strategy is the editorial plan for the topic's investigation.

Write artifact to: simulations/{topic}/strategy.md
