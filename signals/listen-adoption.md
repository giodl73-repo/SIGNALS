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


Simulate the adoption curve across team archetypes. Map personas to Rogers archetypes (innovator/early-adopter/early-majority/late-majority/laggard). Month-by-month simulation: who tries first, what spreads, what bridges the chasm. Chasm analysis: the gap between early adopters and early majority. Champion network, churn risks, intervention recommendations ranked by adoption delta. Stock roles: PM, UX, C-01 through C-12, Support, SRE.

Write artifact to: signals/listen/adoption/{topic}-adoption-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
