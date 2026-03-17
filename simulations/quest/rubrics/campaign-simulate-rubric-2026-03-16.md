Rubric written to `simulations/quest/rubrics/campaign-simulate-rubric-v1-2026-03-16.md`.

**10 criteria across three tiers:**

**Essential (5)** — the report is useless without these:
- C-01: All five sub-skills invoked and attributed
- C-02: Sequential execution order respected
- C-03: Unified findings report produced (not five raw dumps)
- C-04: Blast radius ranking applied as explicit sort key
- C-05: At least one spec gap or contract violation with spec anchoring

**Recommended (3)** — makes the report actionable:
- C-06: Each finding has source + location + impact
- C-07: Findings span at least three of the five sub-skills
- C-08: Concrete remediation guidance per finding

**Aspirational (2)** — raises the bar for reference-quality output:
- C-09: Compounding cross-skill patterns flagged separately
- C-10: Blast radius rankings include explicit scope rationale

The hardest essential to pass will be **C-05** (spec anchoring) — vague "the spec is unclear" observations won't cut it. The hardest recommended will be **C-07** (coverage breadth) — a campaign that only finds flow-lifecycle issues and nothing from trace skills has a structural gap.
