Here is the complete v15 rubric:

---

# trace-request Rubric — v15 (2026-03-15)

**What changed from v14:**

**New criterion: C-39 — Pre-execution halt boundary declaration** (Tier A, V-03)

The V-03 `TRACE CONTRACT` pre-declares `HALT-EXPECTED-BOUNDARY: "BC-5 -- PreOperation elevated FLS bypass"` and `HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-5 AND Step 8c Match? = N for BC-5 row"` as machine-greppable tokens **before any trace step executes**, then closes the loop with `TRACE CONTRACT validation: HALT fired at HALT-EXPECTED-BOUNDARY (BC-5). Contract prediction confirmed.`

**What is testable:**
1. TRACE CONTRACT block present before any trace step begins
2. `HALT-EXPECTED-BOUNDARY:` token naming the specific predicted boundary (BC-N + label)
3. `HALT-EXPECTED-CONDITION:` token naming the dual-surface predicate for that boundary
4. `TRACE CONTRACT validation:` token present after execution
5. Validation confirms HALT-EXPECTED-BOUNDARY matches Row-Verdict = HALT row by boundary ID
6. Match checkable without prose reading

**Dependency:** C-39 depends on C-38 AND C-35

**Scale:** 245 → **250** (aspirational: 31 → 32 criteria, 155 → 160 pts). Golden threshold: **200/250 (80%)**.

---

**Signals not promoted — C-40 design surfaces:**
- **Tier B** (`DECLARE CONTRADICTION:` token in Step 8b): V-02/V-05 only; needs consistent multi-round evidence before the testable surface can be frozen
- **Tier C** (pre-trace CHECKER ALGORITHM commitment): needs multi-round evidence that placement before Step 1 vs. mid-trace produces measurable quality difference
- **Tier D** (error path category taxonomy): completeness aid, no new structural token surface

File written to `simulations/quest/rubrics/trace-request-rubric-v15-2026-03-15.md`.
