Written to `simulations/quest/rubrics/org-chart-rubric-v20-2026-03-17.md`.

---

## v20 summary

**Two new criteria** extracted from Round 19 excellence signals. **315 pts total. Golden = 252/315 (80%).**

---

### C-52 — RATIONALE-FORM-CONTRACT as named pre-section standalone block (depth, 5 pts)

**Bypass closed**: C-50 requires a named prohibition against structural-ordering devices and a MUST directive to cite an observable indicator — but does not specify that the prohibition must appear as a named standalone block. V-01 and V-04 both satisfy C-50 by embedding the prohibition inline within the INERTIA ASSESSMENT header, entangling the rationale-form contract with the section-production instructions. C-52 requires a named `RATIONALE-FORM-CONTRACT` block positioned between the ROLES gate and the INERTIA ASSESSMENT section, independently locatable by name without parsing the section body — parallel to `VIOLATION-LABEL-CONTRACT`.

**Deepens C-50.** Chain: `C-50 -> C-52`.

---

### C-53 — Dual-site RATIONALE-FORM-CONTRACT enforcement: standalone contract + inline INERTIA ASSESSMENT reference (behavior, 5 pts)

**Bypass closed**: C-52 requires the standalone block but does not require a proximate inline reminder within the INERTIA ASSESSMENT section body. A model executing Sub-section 1 without referring back to the standalone contract has no proximate inline enforcement at execution time. C-53 requires dual-site enforcement — standalone contract AND inline section reference — matching the C-16 triple-site principle applied to the rationale-form dimension.

**Deepens C-52.** Full chain: `C-09 -> C-50 -> C-52 -> C-53`.

---

### Updated subsumption hierarchy (flat-case rationale)

```
C-09  flat-case outcome-based rationale
  +-- C-50  anti-structural-device prohibition (STEELMAN FIRST bypass)
       +-- C-52  RATIONALE-FORM-CONTRACT standalone block (inline-embedding bypass)
            +-- C-53  dual-site enforcement (standalone + inline)
```
