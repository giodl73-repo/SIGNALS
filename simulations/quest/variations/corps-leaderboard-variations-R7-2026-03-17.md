**Variate R7 — `corps-leaderboard`** — 5 complete variations written to
`simulations/quest/golden/corps-leaderboard-variate-R7-2026-03-17.md`

---

## Summary

### Variation Map

| | Variation | Primary Axis | C-22 Mechanism | C-23 Mechanism |
|--|-----------|--------------|----------------|----------------|
| **V-01** | Decision-Table Layout | Output format | Pre-write check table (Phase 7) appears immediately before the action template; `prevents:` rule also stated in the template's Breaks field definition — two structurally distinct table rows | Two mandatory fallback rows in the 1-away table: Level 1 (threshold-1 + numeric gap) and Level 2 (threshold-2 + numeric gap) |
| **V-02** | Formal MUST/SHALL/WHEN Spec | Phrasing register | Two MUST clauses at independent locations: MUST in the pre-write decision table, MUST in the action template body — each independently keyword-auditable | WHEN/THEN conditional names Level 1 and Level 2 as separate MUST items, both required when list is empty |
| **V-03** | Strict Forward-Only Phase Gates | Lifecycle emphasis | Pre-write check in Phase 7 is an explicit gate condition — Breaks cannot be written until the check is consulted; template definition restates the rule; Phase 7 cannot close without both | Phase 6 is a named gate that cannot close until both Level 1 and Level 2 are written — gate language makes absence a structural failure |
| **V-04** | 4-Role Pipeline + MUST Spec | Role sequence + phrasing | Compiler role split into pre-write decision step then template-filling — two structurally distinct locations within same role; MUST language at each | Compiler Task B requires both levels as MUST items when list is empty; named as Compiler error if either level is absent |
| **V-05** | Skeptic-First + Inertia Framing | Inertia framing + role sequence | Pre-write check table is a named "decision before action" — framed as the Skeptic's inertia score driving the Breaks field; `prevents:` rule stated in table AND restated in template; score-0 case made a Compiler error | "If the Skeptic is right, write Level 1 and Level 2" — the cascade is framed as the team's two-sprint counter-argument to the Skeptic; both levels required or "the Skeptic wins" |

### What changed V-01 through V-05 vs R6

All five R6 variations scored 100/100 against v6 but none passed both C-22 and C-23 simultaneously. R7 addresses this by:

1. **C-22 fix (all five)**: The pre-write check table is now a first-class structural element placed *immediately before* the action template in every variation — not a note inside the template. The `prevents:` rule appears in the table AND again in the template's Breaks field definition. Two independent trigger surfaces.

2. **C-23 fix (all five)**: The if-none clause is restructured from "name one nearest-miss" (R6 C-21 level) to "write Level 1 and Level 2, both required." Each level carries a specific name and numeric count. Written absence of either level is named as a structural failure or gate condition violation.
