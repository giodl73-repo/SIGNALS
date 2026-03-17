Written to `simulations/quest/golden/corps-rob-variate-R14-2026-03-17.md`.

---

## Variate R14 -- corps-rob

**R14 focus:** v14 adds C-43 and C-44. Both were retroactively earned in R13 by different variations (V-01 earns C-43, V-02 earns C-44), but no R13 variation satisfies both simultaneously. R14 breaks that mutual block.

### Variation Axes Selected (3 single-axis, 2 combination)

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Lifecycle emphasis (AUDIT RESULT boundary explicit at both ordering and independence levels) | V-01 | C-43 + C-44 |
| Phrasing register (C-44 independence as a dedicated named rule, not embedded clause) | V-02 | C-43 + C-44 (alt path) |
| Inertia framing (IB-02 Urgency Gradient field + RULE IB-URGENCY-CASCADE cascade) | V-03 | C-39 |
| Lifecycle + Inertia combined | V-04 | C-43 + C-44 + C-39 |
| All three axes + dual C-44 encoding | V-05 | 265/270 ceiling test |

---

### Variation Summaries

**V-01 — C-43+C-44 Stack Merge** *(Lifecycle emphasis)*
Takes R13 V-01's glossary preamble (C-40+C-42+C-43: label+description pairs) and adds R13 V-02's RULE AUDIT-TABLE additive constraint + independence clause (`mandatory regardless of table presence`). First run combining both stacks. Predicted: **260/270**.

**V-02 — C-44 via Dedicated Named Rule** *(Phrasing register)*
Same C-40+C-42+C-43 exclusivity stack. RULE AUDIT-TABLE carries C-35+C-41 but no independence clause. Independence moves to a new dedicated `RULE AUDIT-INDEPENDENCE` entry. Tests whether a named rule is a stronger C-44 signal than an embedded clause. Predicted: **260/270**.

**V-03 — C-39 Isolated Test** *(Inertia framing)*
V-01 as base, adds `RULE IB-URGENCY-CASCADE` (3 named cascade constraints: Go/No-Go, Risk Register, Inertia Pressure Summary) and Urgency Gradient field on IB-02. First isolated C-39 test on top of a proven C-43+C-44 base. Predicted: **265/270**.

**V-04 — C-43+C-44+C-39 Combined** *(Lifecycle + Inertia framing)*
V-01 + V-03. All R14 target criteria in one run. Minimum-change R14 convergence. Predicted: **265/270**.

**V-05 — Full Convergence + Dual C-44 Encoding** *(All three axes)*
V-04 + adds `RULE AUDIT-INDEPENDENCE` alongside the embedded independence clause. Both encodings of C-44 coexist. Ceiling test: if V-05 = V-04, dual encoding is redundant. Predicted: **265/270**.

### Prediction Table

| V | C-43 | C-44 | C-39 | Expected |
|---|------|------|------|----------|
| V-01 | PASS | PASS (embedded) | FAIL | 260/270 |
| V-02 | PASS | PASS (rule) | FAIL | 260/270 |
| V-03 | PASS | PASS (embedded) | PASS | 265/270 |
| V-04 | PASS | PASS (embedded) | PASS | 265/270 |
| V-05 | PASS | PASS (both) | PASS | 265/270 |
