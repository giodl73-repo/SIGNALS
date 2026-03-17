V-05 exhaustiveness gate is correctly structured with both the integer count summary and the Adv? per-row field, plus explicit DISQUALIFIER blocks labeling C-20 and C-21. The file is complete.

---

## R6 Variations — `trace-request`

File written: `simulations/quest/rubrics/trace-request-rubric-v6-variations-R6-2026-03-14.md` (1413 lines)

---

### Variation summary

| V | Axis | Exhaustiveness gate | C-18 | C-20 | C-21 | Predicted |
|---|------|---------------------|------|------|------|-----------|
| **V-01** | Lifecycle: advisory | Advisory paragraph only — no per-row checklist, no blocking gate | PARTIAL | FAIL | FAIL | **147/160** |
| **V-02** | Output format: checklist + narrative summary | Blocking GATE, per-row named checklist, `"Exhaustiveness check complete."` | PASS | FAIL | FAIL | **150/160** |
| **V-03** | Lifecycle: count gate *(single axis vs V-02)* | V-02 + mandatory integer count summary: `"[N] rows reviewed… [X] Seq# additions made"` | PASS | PASS | FAIL | **155/160** |
| **V-04** | Output format: Adv? per checklist row *(single axis vs V-02)* | V-02 + `Adv? = [Y/N]` per checklist row, narrative summary | PASS | FAIL | PASS | **155/160** |
| **V-05** | Combined: count gate + Adv? checklist + DISQUALIFIERs | All three + explicit `DISQUALIFIER (C-20)` and `DISQUALIFIER (C-21)` blocks | PASS | PASS | PASS | **160/160** |

---

### Design rationale

**Single-axis isolation is clean:** V-03 and V-04 both predict 155/160 but fail *different* criteria — V-03 fails C-21 only, V-04 fails C-20 only. This confirms the two new criteria are independently testable: neither subsumes the other.

**V-01 C-18 = PARTIAL (not FAIL):** The advisory paragraph references the Step 3 boundary inventory and names the re-examination action, crossing the PARTIAL threshold. It earns 2 pts rather than 5 because it doesn't require the model to produce a per-row record before Step 7.

**V-05 DISQUALIFIER logic:** The explicit blocks address the two hedged-compliance failure modes that would pass a lenient scorer — `"all rows reviewed"` (no integer) and `"no additions found"` (no explicit X=0) — plus the ordering rule that no Adv? value may be filled post-hoc after Step 7 begins.

**Scoring gap attribution:**

| V | Missing pts | Gap criteria |
|---|-------------|-------------|
| V-01 | 13 | C-20(0), C-21(0), C-18 PARTIAL(2 vs 5) |
| V-02 | 10 | C-20(0), C-21(0) |
| V-03 | 5 | C-21(0) |
| V-04 | 5 | C-20(0) |
| V-05 | 0 | — |
