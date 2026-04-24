for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Extract and prioritize requirements from a product concept. Search for prior scout signals in BOTH signals/scout/ (real runs) AND signals/trace/skill/ (hand-compiled traces) -- never silently skip the trace directory. MoSCoW prioritization. Dependency graph (which requirements block others). Ambiguity flags (requirements needing clarification). Suspicious silences (areas with no requirements). Stock roles: PM (user-facing), Architect (technical), UX (usability), Compliance (regulatory).

Write artifact to: signals/scout/requirements/{topic}-requirements-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
