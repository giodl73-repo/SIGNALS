# prove-prototype — Round 5 Score (v5 rubric)

## Result: All Five Variations — 140 / 140 (ceiling)

All five variations achieve the 140-point ceiling. This is the direct consequence of the Round 5 design intent: every variation was built specifically to close the C-19 trailing-section gap and satisfy the new C-20/C-21 criteria. The rubric ran out of discrimination surface.

---

## Scoring Summary

| Variation | C-19 | C-20 | C-21 | Total |
|-----------|------|------|------|-------|
| V-01 Role Sequence (3 roles) | PASS | PASS | PASS | 140 |
| V-02 Table-Row Format | PASS | PASS | PASS | 140 |
| V-03 Formal Register | PASS | PASS | PASS | PASS | 140 |
| V-04 Lifecycle + B-00 | PASS | PASS | PASS | 140 |
| V-05 Role Sequence (2 roles) | PASS | PASS | PASS | 140 |

All essential, recommended, aspirational, and excellence criteria pass across all variations. The Round 4 gap (phases 8–9 ungated, C-19 partial in V-01/V-03/V-05) is closed in every variation.

---

## Excellence Signals (above-ceiling differentiation)

Three patterns distinguish the best-structured variations:

1. **V-04: completion-line-as-audit-by-scan** — carries E/B-00/delta/calibration *values* in completion lines, creating a cross-phase audit path by completion-scan alone (no need to read phase bodies). No other variation achieves this.

2. **V-01/V-05: role-attribution-as-contamination-guard** — role prohibitions detect in-order but out-of-role content (EVALUATOR writing build description; ANALYST restating results). Orthogonal to phase-gate ordering — a distinct failure class that phase gates cannot catch.

3. **V-04: lifecycle-container-as-second-detection-level** — DEFINE/RUN/EVALUATE containers catch lifecycle inversions at the document-structure level before descending to individual phase inspection.

---

## New Patterns → v6 candidates

| Pattern | Candidate criterion |
|---------|-------------------|
| `completion-line-as-audit-by-scan` | C-22 |
| `role-attribution-as-contamination-guard` | C-23 |
| `lifecycle-container-as-second-detection-level` | C-24 |

---

```json
{"top_score": 140, "all_essential_pass": true, "new_patterns": ["completion-line-as-audit-by-scan", "role-attribution-as-contamination-guard", "lifecycle-container-as-second-detection-level"]}
```
