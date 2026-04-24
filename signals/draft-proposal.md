for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Author a proposal or ADR with options and trade-offs. Three options minimum (including do-nothing). Each option: description, pros, cons, risk, effort. Recommendation section with rationale. Pulls from scout-feasibility if available. Stock roles: Architect (technical options), PM (business trade-offs).

Write artifact to: signals/draft/proposals/{topic}-proposal-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
