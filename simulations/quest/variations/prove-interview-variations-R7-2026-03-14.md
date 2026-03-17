---

## Cross-Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Inertia framing | ABSENT | PARTIAL-A | — | PASS minimal | PASS maximum |
| Output format | — | Named table, no Switch Cost column | Switch Cost column, no table | Minimal both | Full both |
| Role sequence | Standard (S-00 first) | Standard | S-01 → S-02 → S-00 (incumbent last) | Standard | Standard |
| Lifecycle emphasis | — | — | — | Post-S00 gate | Per-step gates + post-coupling gate |
| Phrasing register | Descriptive | Descriptive | Descriptive | Descriptive | Imperative throughout |

**C-22 isolation design:**

- **V-01** — Tests cost of C-22 absence. Confirms the 5-pt gap between 155 and 160 is attributable solely to C-22.
- **V-02** — Tests PARTIAL-A boundary: table present, Switch Cost column absent. One conjunction element; no propagation. Predicted 2–3 pts.
- **V-03** — Tests PARTIAL-B boundary: Switch Cost column present in Inertia Verdict Matrix, no named table to source it. Role-sequence inversion is a non-C-22 variation axis that tests whether incumbent-last sequencing changes C-09/C-13 floor behavior. Predicted 2–3 pts.
- **V-04** — Tests minimum C-22 PASS: one coupling factor, one rating, explicit sourcing in Switch Cost column. Lifecycle gate prevents skipping. The `before proceeding` language at the post-Step-1 gate is the structural enforcement mechanism.
- **V-05** — Tests maximum C-22 architecture: multi-factor table, per-row coupling-factor attribution in Switch Cost column, COLUMN POLICY additive-only row, incumbent switching friction in Arc Signal. Architecture investment for C-23+ extraction (likely: per-factor incumbent friction claim in Arc Signal, or Switch Cost column compliance block analogous to COLUMN POLICY for evidence columns).

**Predicted scores:** V-01 = 155, V-02 ≈ 157, V-03 ≈ 157, V-04 = 160, V-05 = 160.

**C-22 PARTIAL ambiguity to watch:** The rubric defines PARTIAL as "one element present without the other." V-02 and V-03 each have exactly one element. The 2–3 pt PARTIAL band may resolve differently depending on whether the grader treats a named table without a Switch Cost column as more structurally complete than a Switch Cost column without a table — the table is the source artifact; the column is the derived artifact. If source > derived in PARTIAL credit, V-02 may score 3 and V-03 may score 2. If symmetric, both score 2. This asymmetry is the primary prediction risk.
