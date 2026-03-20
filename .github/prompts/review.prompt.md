---
mode: agent
description: "Team validates the design. Expert and discipline review of specs and code. Persona walkthrough for usability. 12-customer-persona evaluation for adopt"
---
confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


Multi-expert review of a design artifact through 6 standard disciplines and auto-selected domain experts. Auto-select 3-5 domain experts from content signals (e.g., spec mentioning RBAC selects a security architect). Per-reviewer findings with P1/P2/P3 severity. Consensus analysis (2+ reviewers flag same thing), split opinions, unique catches. Amend: address findings one by one, re-run specific reviewers on changed sections. Stock: 6 disciplines (architect, code-quality, documentation, testing, process, implementation) + domain experts.

Write artifact to: signals/review/design/{topic}-design-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
