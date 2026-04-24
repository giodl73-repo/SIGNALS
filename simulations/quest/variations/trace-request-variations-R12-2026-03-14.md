---

# trace-request rubric v11 — Skill Body Prompt Variations R12

**File:** `simulations/quest/rubrics/trace-request-rubric-v11-variate-R12-2026-03-15.md`

---

## Variation Summary

| V | Axis | Key change | C-31 | C-32 | C-33 | Predicted |
|---|------|------------|------|------|------|-----------|
| **V-01** | Regression: C-31 advisory | `CONTRADICTION SIGNAL` label removed; replaced with advisory prose; `Scope String Correction` Rem# type removed; Step 8 Header preserved | FAIL | PASS | FAIL | 210/220 |
| **V-02** | Regression: C-32 advisory | Step 8 Header softened to advisory; REQUIRED removed; Match? no longer anchored to header; CONTRADICTION HALT (C-31) preserved intact | PASS | FAIL | FAIL | 210/220 |
| **V-03** | Output format: structured token schema | Step 8 Header requires `VT-N: "exact string"` quoted format + `TOKEN-COUNT: N`; Match? rule explicitly cites schema; C-34 surface: header is machine-parseable without prose reading | PASS | PASS | PASS | 220/220 |
| **V-04** | Output format: row-level verdict token | Step 8c adds `Row-Verdict` column (`PASS`/`HALT`) + required `CHECK RESULT: PASS/FAIL -- N rows, M HALT` summary; checker can scan Row-Verdict without reading Match? or Step 8b prose | PASS | PASS | PASS | 220/220 |
| **V-05** | Two-axis: V-03 + V-04 | Structured schema header + Row-Verdict column + CHECK RESULT; full checker contract: parse `VT-N: "..."` lines, scan Row-Verdict, emit CHECK RESULT — no prose reading at any step | PASS | PASS | PASS | 220/220 |

---

## C-34 Design Surface (R12 yield)

The three new-axis variations probe two separable properties of a live automated checker:

| Property | Source | Structural form |
|---|---|---|
| Parseable input schema | V-03 | `VT-N: "..."` + `TOKEN-COUNT: N` in Step 8 Header |
| Parseable output verdict | V-04 | `Row-Verdict: PASS/HALT` column + `CHECK RESULT:` line |
| Full checker contract | V-05 | Both properties co-present: input schema + output tokens |

V-05 completes the C-34 pre-condition: a runnable checker needs only (1) parse header lines matching `^VT-[0-9]+: ".*"$`, (2) scan `Row-Verdict` column for `HALT`, (3) emit `CHECK RESULT: PASS/FAIL`. No semantic reading required at any step.
