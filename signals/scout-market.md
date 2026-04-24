for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Size the addressable market and rank segments by fit. Use developer headcount for tooling segments, dollar TAM for platform/enterprise segments -- do not mix units in the same table. Scoring: pain severity, WTP, accessibility on 1-10 scale, equal weights, composite = average. Composite rank = fit score + (10 - GTM difficulty). Recommend beachhead segment with rationale. Stock roles: Strategy (TAM/SAM/SOM), PM (segment fit), GTM (go-to-market difficulty).

Write artifact to: signals/scout/market/{topic}-market-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
