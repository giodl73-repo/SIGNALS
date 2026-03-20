---
mode: agent
description: "Topic registration with strategy planning and signal coverage plan."
---
Register a new topic, define its strategy, plan the signals needed for design commit. Output: entry in TOPICS.md, strategy.md in signals/{topic}/. Strategy lists planned signals with namespace, skill, item name, owner role, and priority (essential/recommended/optional). The strategy is the editorial plan for the topic's investigation.

Write artifact to: signals/{topic}/strategy.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
