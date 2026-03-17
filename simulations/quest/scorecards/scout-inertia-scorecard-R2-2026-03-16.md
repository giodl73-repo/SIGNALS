## Quest Score — scout-inertia R2

**Rubric version**: v2 | **Variations**: V-01 through V-05 | **No trace artifact — scoring against structural design**

---

### Scoring Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Workaround mapped in detail | PASS | PASS | PASS | **FAIL** | PASS |
| **C-02** Switching cost quantified | PASS | PASS | PASS | PASS | **FAIL** |
| **C-03** Inertia threat score HIGH | PASS | PASS | PASS | PASS | PASS |
| **C-04** Why inertia loses answered | PASS | **FAIL** | PASS | PASS | PASS |
| **C-05** Failure modes identified | PASS | PASS | PASS | PASS | **FAIL** |
| **R-01** Trigger scoped to team type | PASS | PASS | PASS | PASS | PASS |
| **R-02** Role-level precision | PASS | PASS | PASS | PASS | PASS |
| **R-03** At least one cost cited | PASS | PASS | PASS | PASS | PASS |
| **A-01** Per-section revision gate | PASS | PASS | PASS | PASS | PASS |
| **A-02** Column-level structural constraint | PASS | PASS | **FAIL** | PASS | PASS |

---

### Criterion Evidence Notes

**C-01 — V-04 FAIL**: Failure-mode-first lifecycle reconstructs the workaround *from* its cracks. This means actor, frequency, and output artifact emerge as byproducts of failure enumeration rather than declared upfront. A workaround whose actor is "whoever notices the failure" is not mapped — it's inferred. C-01 pass condition requires proactive declaration of who performs it and how often.

**C-02 — V-05 FAIL**: Five claims, one evidence each gives exactly one slot to "switching cost." C-02 requires numbers across 2-of-3 dimensions (time, training, disruption). Packing three quantified dimensions into a single claim+evidence pair produces either an incomplete cost estimate or a claim so dense it loses the structural precision V-05 is designed to enforce. Constraint-via-scarcity cuts against multi-dimensional coverage.

**C-04 — V-02 FAIL**: Two-pass structure produces defeat conditions scoped *per team type* — exactly what R-01 demands. But C-04's pass condition is a synthesized answer to "why inertia loses," not two separate per-team answers. With Pass A and Pass B each contributing their own defeat conditions, V-02 has no section that consolidates into a shared falsifiable statement covering both populations. The answer is structurally split.

**C-05 — V-05 FAIL**: Same scarcity problem as C-02. Two specific failure modes with observable symptoms require two claim slots. V-05 allocates one. Either the analyst violates the sparse contract or C-05 gets a single failure mode and fails the "at least two" gate.

**A-02 — V-03 FAIL**: Grounded-first quantification shifts the analyst's attention toward *evidence chains* rather than *column completeness*. When the structural contract is "every number needs an anchor," the analyst focuses on the anchor, not on whether all column entries meet their semantic type. Column headers in V-03 become weaker than in V-01, where each column header carries an explicit contract enforced by a self-score gate.

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Score | Golden? |
|-----------|-----------|-------------|--------------|-------|---------|
| **V-01** | 5/5 → 60 | 3/3 → 30 | 2/2 → 10 | **100** | YES |
| **V-02** | 4/5 → 48 | 3/3 → 30 | 2/2 → 10 | **88** | NO |
| **V-03** | 5/5 → 60 | 3/3 → 30 | 1/2 → 5 | **95** | YES |
| **V-04** | 4/5 → 48 | 3/3 → 30 | 2/2 → 10 | **88** | NO |
| **V-05** | 3/5 → 36 | 3/3 → 30 | 2/2 → 10 | **76** | NO |

**Rank**: V-01 > V-03 > V-02 = V-04 > V-05

---

### Excellence Signals — V-01

**Signal 1 — Composite gate with back-pointers**
Section 6 is not just a self-score; it lists every criterion with the exact section number to return to on failure. This means an analyst who rushes and fills in vague entries cannot mark the artifact complete without being directed back to the specific section that failed. The gate is not advisory — it is a *completion blocker*. Prior rubric versions had per-section self-scores but no aggregating gate that caught cross-criterion gaps in one place.

**Signal 2 — Role precision as a continuation gate, not a suggestion**
V-01 places the role precision check inside Section 1 with an explicit instruction: *"If the 'who performs it' cell contains 'teams', 'users', 'people', or a department name, replace it before continuing."* This is a pre-condition for entering Section 2, not a scoring note at the end. The enforcement point is before the analyst has completed any section — when the cost of correction is lowest. V-02 has the same check (A1), but it sits within a two-pass structure where the analyst may complete Pass B before circling back.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["composite-gate-with-back-pointers: Section 6 aggregates all per-section pass/fail results and names the specific section to revise on failure, creating a completion gate rather than an advisory score", "role-precision-as-continuation-gate: the role check in Section 1 is a pre-condition for entering Section 2, not a scoring note — early enforcement when correction cost is lowest"]}
```
