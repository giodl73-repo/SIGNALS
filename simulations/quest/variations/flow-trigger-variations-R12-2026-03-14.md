**Round 12 variations written** to `simulations/quest/rubrics/flow-trigger-rubric-v7-R12-2026-03-15.md`.

---

## Round 12 — Design Summary

**New signal candidates** (beyond C-23):

| Signal | Mechanism | Variation |
|--------|-----------|-----------|
| **Prediction Closure Report (PCR)** | Role 0 returns post-cataloging to tally confirmed / ⚠-flagged / silent gap predictions; silent gaps feed pathology as a second evidence stream | V-01, V-04 |
| **Remediation Coverage Gate** | Phase 4 gate after pathology verifies every DETECTED/INDETERMINATE IF-* label has a remediation; "remediation-orphaned" is a new named status | V-03 |
| **Mesh Closure Certificate** | Required final block verifying 4 coverage dimensions (D1 TC-2/TC-3 annotation, D2 TC-1 annotation, D3 forward mesh fulfillment, D4 verdict) per IF-* label with PASS/FAIL/N/A | V-05 |

**Persistent gaps closed** (never scored across R1–R11):

| Criterion | How R12 closes it |
|-----------|------------------|
| **C-07** (environment named) | All five variations require named environment + solution layer as explicit scenario fields |
| **C-11** (enforcement rule caption) | V-02/V-05 require verbatim-emit caption immediately after trigger table; V-01/V-03/V-04 include enforcement rule text inline |
| **C-13** (per-automation arithmetic) | V-02/V-04/V-05 encode as a required per-automation table schema field; V-01/V-03 require per-automation intermediate arithmetic |

**Variation axes:**

| Variation | Axis |
|-----------|------|
| V-01 | Role sequence — Role 0 post-cataloging return arc (PCR) |
| V-02 | Output format — gap-closing schema targeting C-07/C-11/C-13 + C-21/C-22/C-23 |
| V-03 | Lifecycle emphasis — four-gate lifecycle + remediation coverage check |
| V-04 | Combined: role sequence + prosecution/adjudication framing |
| V-05 | Combined: lifecycle + format + inertia framing + Mesh Closure Certificate |
