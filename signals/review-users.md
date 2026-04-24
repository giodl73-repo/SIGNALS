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


5 persona advocates walk through a design from their user perspective. Each persona narrates in first person, flags confusion/friction/fear/jargon with exact artifact quotes, gives usability score 1-5. Cross-persona synthesis: universal friction (3+ personas), role-specific friction, persona conflicts (what helps one hurts another). Aggregate usability score. Amend: iterate until no persona scores below 3/5. Stock: Maker, Developer, Compliance, Supervisor, Operator.

Write artifact to: signals/review/users/{topic}-users-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
