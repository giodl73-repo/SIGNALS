Here are the 5 complete variations, written to `simulations/quest/golden/quest-variate-variate-R6-2026-03-15.md`:

---

## Round 6 Summary

**Champion baseline:** R5 V-05 (already has C-26, C-27, C-28, C-29; missing C-25, C-30, C-31)

**Pre-generation VARIATION MAP** implements C-27, C-29, and C-30 (failure-condition prediction columns) at the meta-document level.

| V | Axis | Target | Single-axis change |
|---|------|--------|--------------------|
| **V-01** | output-format | C-25 | `failure-condition:` → `failure-condition-outcome:` + `failure-condition-implementation:` (dual named keys) in Phase 1 headers |
| **V-02** | scoring-granularity | C-30 | VARIATION MAP gains two required columns per row: `failure-condition-outcome prediction` and `failure-condition-implementation prediction` |
| **V-03** | lifecycle-emphasis | C-31 | AXIS-FREEZE PROTOCOL gains **Step 2B** — cross-artifact axis consistency check fires *before* Step 3 (body writing), not just in Phase 3 |
| **V-04** | output-format × lifecycle-emphasis | C-25 + C-31 | C-04 exception. Dual keys (V-01) + in-loop consistency gate (V-03) simultaneously |
| **V-05** | scoring-granularity × lifecycle-emphasis | C-30 + C-31 | C-04 exception. Failure-condition prediction columns in VARIATION MAP (V-02) + in-loop gate that surfaces map predictions at fire-time (V-03) |

**Key R6 finding pre-committed:** V-03 is designated anchor — Step 2B (in-loop gate) is purely additive, fully isolated, and detectable by gate label presence alone. C-31 failure is visible before reading any body.
