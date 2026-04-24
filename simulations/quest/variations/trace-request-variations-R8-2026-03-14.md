`simulations/quest/rubrics/trace-request-rubric-v7-R8-2026-03-15.md` written. Here is the extraction summary:

---

## Variation Summary Table

| V | Axis | Key change from R7 V-05 baseline | C-22 | C-23 | New signal | Predicted |
|---|------|----------------------------------|------|------|------------|-----------|
| V-01 | Phrasing register: C-22 advisory | Batch-catalog gate described advisorily; no integer format enforcement | FAIL | PASS | none | 165/170 |
| V-02 | Phrasing register: C-23 advisory | Rem# citation softened to suggestion; no at-boundary placement requirement | PASS | FAIL | none | 165/170 |
| V-03 | Output format: cross-check table | Step 10 gate expressed as a named EC# × TRow# table; three integers derived from cell counts | PASS | PASS | C-24 candidate: cross-check table completeness | 170/170 |
| V-04 | Lifecycle emphasis: scope enumeration | Step 8 re-walk requires a dedicated scope enumeration table (Invoked, Required, Verified?, Gap?) per boundary before re-walk findings | PASS | PASS | C-24 candidate: per-scope auth exhaustiveness | 170/170 |
| V-05 | Two-axis combination (V-03 + V-04) | Cross-check table + scope enumeration table, both required | PASS | PASS | Two C-24 candidates + C-25 speculative | 170/170 |

---

**Single-axis choices (3 of 5):**
- **Phrasing register** → V-01 (C-22 dropped) and V-02 (C-23 dropped) — regression control tests
- **Output format** → V-03 (cross-check table replaces prose gate)
- **Lifecycle emphasis** → V-04 (scope enumeration table in Step 8)

**Two-axis combination:** V-05 = V-03 + V-04

---

**Why these regression tests matter:** R7 V-01 confirmed that DISQUALIFIER pressure is load-bearing for C-20 and C-21. R8 V-01 and V-02 run the same test against C-22 and C-23. If both produce -5 gaps as predicted, the v7 rubric is stable. If either produces 170/170, the DISQUALIFIER wording needs hardening before R9.

---

**Three excellence signal candidates from R8:**

| Signal | Source | Testable condition |
|--------|--------|--------------------|
| ES-1: Cross-check table completeness | V-03, V-05 | K integer cell-verifiable from the visible table; M columns = Step 5 count; N rows = Step 10a count |
| ES-2: Per-scope auth exhaustiveness | V-04, V-05 | Every boundary names a Required Scope/Role; Gap? column marks invoked-vs-required mismatches; Verified? = N at dependent boundary is a structural gap |
| ES-3: Scope-gap Rem# propagation (speculative) | V-05 | Step 8a Gap? entries appear as Rem# entries in Step 11 with exact scope string parameters — a three-way cross-link Step 8a → Step 11 → Step 7/9 |
