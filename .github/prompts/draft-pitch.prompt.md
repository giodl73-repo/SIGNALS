---
mode: agent
description: "Pitch deck narrative in exec, developer, and maker versions."
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

Author a pitch deck narrative in exec, developer, and maker versions. Pulls from scout-positioning if available. Each version: hook, what it does, why it matters, call to action. Anti-positioning section (what we are NOT). Exec version: outcome-first, ROI framing. Dev version: show the tool, not the business case. Maker version: jargon-free, "can I do this?" framing. Stock roles: PM, Strategy.

Write artifact to: signals/draft/pitches/{topic}-pitch-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
