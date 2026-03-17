---

## mock-all Variate — Round 5

**File:** `simulations/quest/golden/mock-all-variate-R5-2026-03-15.md`

---

### What R4 left open

v5 adds no new criteria — C-09 through C-17 (denominator 9) unchanged. R4 V-01/V-02/V-04/V-05 predicted 100; R4 V-03 (inertia-framing, no vocab columns) hit 98.9. Three open questions drove R5:

| Question | R4 state |
|---|---|
| Does **role identity** enforce C-11 more reliably than PHASE labels? | Untested R1–R4 |
| Does **pure conversational register** maintain 100 while improving C-07/C-10? | R3 V-03 was vocab-columns disguised as "phrasing-register" |
| Can **inertia-framing** reach 100 by adding vocab columns to R4 V-03's base? | R4 V-03: C-17 FAIL was the only miss |

---

### Axis-Assignment Plan

| Variation | Axis | Target Criteria | Predicted |
|---|---|---|---|
| **V-01** | role-sequence (new) | C-11, C-14, C-16, C-17 via role identity | 100 |
| **V-02** | phrasing-register (conversational) | C-07/C-10 quality; C-14/C-16/C-17 maintained | 100 |
| **V-03** | inertia-framing (upgraded — adds vocab columns to R4 V-03) | C-17 fix + C-07/C-10 quality | 100 |
| **V-04** | role-sequence + lifecycle-emphasis | C-11 dual-channel enforcement, C-14/C-16/C-17 | 100 |
| **V-05** | role-sequence + phrasing-register + output-format (minimal skeleton) | Three concurrent C-11 mechanisms + quality | 100 |

---

### Key design decisions per variation

**V-01 (role-sequence)** — The central bet: "As the CLASSIFIER, you only classify" constrains at the identity level, not the procedural level. ROLE STOP gates enumerate all five required fields. Vocab columns in CLASSIFIER output close C-17.

**V-02 (conversational)** — Same structural machinery as R4 V-04; only the voice changes. "Stop. Do not write any artifact body until every row... is filled." is a gate phrase even in conversational register. Hypothesis: conversational framing warms up the artifact body generation, improving C-07 depth.

**V-03 (inertia upgrade)** — R4 V-03 verbatim plus vocabulary columns injected into the classification table. Fixes the one known miss. The inertia block frames each artifact body as answering "what blind spot does this namespace fill?" — a semantic anchor for richer generation.

**V-04 (role + lifecycle)** — Dual-channel: PHASE labels AND role identity declarations at every boundary. PHASE N GATE phrases enumerate five fields. Tests whether identity + procedure are additive or redundant.

**V-05 (full ceiling)** — Minimal pre-printed table stubs (structural C-11 guarantee) + role declarations (identity C-11 enforcement) + conversational bridges between roles ("You've just finished classifying. Now, as the GENERATOR..."). Three concurrent C-11 mechanisms with lower skeleton weight than R3/R4 full pre-print.
