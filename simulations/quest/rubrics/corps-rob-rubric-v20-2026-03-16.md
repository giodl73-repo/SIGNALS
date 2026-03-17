Written to `simulations/quest/rubrics/corps-rob-rubric-v20-2026-03-17.md`. 2175 lines (up from 1998 in v19).

---

**What changed:**

| ID | Criterion | Dep |
|----|-----------|-----|
| C-58 | RULE BOOKEND-AUDIT Dual Anti-Pattern Completeness | C-27 |
| C-59 | RULE VIA-POSITION Dual Anti-Pattern Completeness + VIOLATION-03 Orphan Closure | C-50 |
| C-60 | RULE SYNTHESIS Dual Anti-Pattern Completeness | C-36 |

**Scoring:**

| | v19 | v20 |
|--|-----|-----|
| Aspirational pool | 49 × 5 = 245 | 52 × 5 = 260 |
| Max composite | 335 | 350 |

**Retroactive R20 under v20:**
- V-01: 335 (+C-58)
- V-02: 335 (+C-59)
- V-03: 335 (+C-60)
- V-04: 340 (+C-58 + C-59)
- V-05: 345 (+C-58 + C-59 + C-60, persistent gap still -5)

**Design notes:**

- **C-58** closes the last peer-parity gap: BOOKEND-AUDIT was the only named audit rule without a disqualifying-form declaration for the bare-section case. The three-state ladder (Absent / Present-but-bare / Conforming-present) parallels the escalation patterns in C-26, C-41, C-49.

- **C-59** is the strongest single-axis case structurally: VIOLATION-03 has been dead taxonomy since it was first declared — carrying a Consequence field that no rule ever enforced. AP-2 closes the orphan; the orphan-violation structural gap predates R14.

- **C-60** is the weakest of the three (as flagged in the scorecard): no existing violation covers generic SYNTHESIS content, so the criterion rests on the anti-pattern declaration alone rather than also closing an orphan. Dependency stays at C-36 (subsection schema), not deeper.

**Candidate directions for R21 (persistent gap):** Annotative register meta-criterion (Governs/Include framing), Stage Metrics block, LIFECYCLE POSITION stage header annotation.
