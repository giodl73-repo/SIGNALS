---
name: simulate-stress
description: "Simulate degraded conditions: offline, partial failure, eventual consistency. For each failure scenario: what state is t"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
# simulate-stress

Simulate degraded conditions: offline, partial failure, eventual consistency. For each failure scenario: what state is t

*Full runbook at `simulate-stress.t3/SKILL.md`.*

Write artifact to: signals/simulate/stress/{{topic}}-stress-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-stress-{date}.md). No namespace subdirectory.
Include frontmatter: skill: simulate-stress, topic: {{topic}}, date: {{date}}
