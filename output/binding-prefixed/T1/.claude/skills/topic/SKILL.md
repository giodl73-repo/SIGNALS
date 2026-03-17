---
name: topic
description: "Topic namespace -- 6 skills for narrative management.

/topic-new     -> topic registration with strategy planning and signal coverage plan
/topic-status  -> terminal coverage display computed from signal glob
/topic-report  -> shareable status document with progress table and readiness statement
/topic-plan    -> signal strategy revision as new information arrives
/topic-story   -> editorial synthesis of all signals into a coherent narrative
/topic-echo    -> unexpected findings synthesis: what did we learn that we did not expect?

Run any sub-skill directly, or describe your topic management need and the most relevant skill will run.
"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
Register a new topic, define its strategy, plan the signals needed for design commit. Output: entry in TOPICS.md, strategy.md in simulations/{topic}/. Strategy lists planned signals with namespace, skill, item name, owner role, and priority (essential/recommended/optional). The strategy is the editorial plan for the topic's investigation.

Write artifact to: simulations/{topic}/strategy.md
