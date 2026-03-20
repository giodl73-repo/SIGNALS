---
mode: agent
description: "Specification authoring with guided section structure and self-review."
---
for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Author a specification from intent with guided section structure. Pulls context from any scout signals for the topic. Guided section authoring: purpose, requirements (from scout-requirements if available), design, constraints, open questions. Self-review on completion: flag open questions, gaps, and ambiguity. Stock role: Architect.

Write artifact to: signals/draft/specs/{topic}-spec-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
