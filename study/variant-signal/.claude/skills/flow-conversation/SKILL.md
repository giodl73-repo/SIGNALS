---
name: flow-conversation
description: Multi-turn agent conversation simulation through topic graph with dead-end and loop detection.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Simulate a multi-turn agent conversation through a topic graph. Walk the dialog path: user intents, agent responses, topic transitions, fallback handling, session state. Identify: dead ends (no valid next intent), infinite loops, intent collisions (same utterance maps to multiple topics), missing fallbacks. Stock roles: Copilot Studio domain expert.

Write artifact to: simulations/flow/conversation/{topic}-conversation-{date}.md
