Written to `simulations/quest/golden/topic-echo-variate-R11-2026-03-16.md`.

---

## Round 11 — Design Summary

**R10 ceiling**: 97.50 (V-05). All five remaining failures + one partial share a single root cause: no CB-ID infrastructure. R11 targets that gap.

**Variation plan:**

| | Axis | C-23 | C-24 | C-25 | C-11 | C-12 | C-14 | C-20 |
|---|---|---|---|---|---|---|---|---|
| **V-01** | Role sequence | PASS | FAIL | FAIL | FAIL | FAIL | PARTIAL | PASS |
| **V-02** | Output format | PARTIAL | FAIL | FAIL | FAIL | FAIL | PARTIAL | PASS |
| **V-03** | Lifecycle emphasis | PASS | PASS | PASS | FAIL | FAIL | PARTIAL | PASS |
| **V-04** | Sequence + lifecycle + C-11/12 | PASS | PASS | PASS | PASS | PASS | PARTIAL | PARTIAL |
| **V-05** | Full synthesis | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

**Key structural additions:**

- **Step 0** (BC): frozen Competitor Belief Register with `HIGH/MEDIUM/LOW` confidence levels — the prerequisite for everything else
- **`defeats: CB-{n}`** field in every entry template — what links surprises back to the declared prior
- **Stage 2 non-derivability sub-test** (V-04/V-05): "Could spec + full CB-set have predicted this?" — C-11 structural gate
- **CB-ID group headers** in Step 7 output (V-04/V-05): ≥2 distinct CB-ID groups — C-12
- **Step 3b redundancy check** (V-05 only): same-CB-ID pairs flagged structurally — C-14 PARTIAL → PASS
- **Confidence-weighted triage** in Step 4 (V-03+): HIGH-confidence defeats first — C-24
- **Surviving Belief Register** in Step 9 (V-03+): undefeated CB-IDs listed by ID — C-25

**Discriminating pairs:**
- V-01 vs V-02: pre-read vs post-read belief declaration — isolates whether C-23 cares about timing
- V-01 vs V-03: C-24/C-25 absent vs present — isolates confidence-weighting + surviving-beliefs value
- V-03 vs V-04: C-11/C-12 absent vs present — isolates non-derivability + grouping value
- V-04 vs V-05: C-14 redundancy check + full phase blocks absent vs present
