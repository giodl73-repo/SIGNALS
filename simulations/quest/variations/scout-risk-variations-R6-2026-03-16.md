`simulations/quest/golden/scout-risk-variate-R6-2026-03-16.md`

---

**R6 summary:**

R4 V-05 under v6 rubric = **113/118**. Two gaps: C-21 (embedded diversity rule in STEP 2 is a generation-time rule, not a downstream repair loop with named back-reference) and C-22 (prose FROM/TO doesn't satisfy cell-level vocabulary constraint).

**Five variations:**

| ID | Axis | C-21 | C-22 | Score |
|----|------|------|------|-------|
| V-01 | Lifecycle — Phase 2b standalone diversity audit | PASS | FAIL | 115 |
| V-02 | Output format — vocabulary-constrained typed columns | trivial PASS | PASS | 117 |
| V-03 | Phrasing — explicit "Repair Loop A/B" labels | PASS | FAIL | 115 |
| V-04 | Combined lifecycle+format | PASS | PASS | 117 |
| V-05 | Full integration (R4 V-05 + STEP 2b + typed table) | PASS | PASS | 117 |

**Ceiling = 117** (C-10 PARTIAL is irreducible on base prompts).

**Key design note:** V-02 reaches 117 without C-18 (no diversity gate) because it gains C-15 (type sub-fields from R4 V-03 base) and C-22, netting even. V-01 vs V-03 is the mechanism comparison for C-21: phase extraction vs named loop labels — same score, different structure.
