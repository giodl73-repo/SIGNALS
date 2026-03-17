**prove-topic — Variation Round R4** written to `simulations/quest/golden/prove-topic-variate-R4-2026-03-15.md`.

---

## Summary

Five complete variations targeting C-16 and C-17 — the two new rubric criteria in v4.

| Variation | Axis | Key mechanism | C-16 | C-17 |
|-----------|------|---------------|------|------|
| **V-01** | Adversarial escalation protocol | Named adversarial reviewer registered at campaign open; null across all stages → escalation_state: triggered; handoff status: Escalated (blocks promotion) | Full | Partial (verbal) |
| **V-02** | Mechanical CE-score cap | Counter-evidence state is a formula input: CE-score = -2 when all null, 0 otherwise; final composite = evidence_composite + CE-score; level assigned by number, no override | Partial | Full |
| **V-03** | Stage-exit integrity gate | 3-item compliance gate at end of S2/S3/S4; synthesis compiles 12-item campaign integrity summary; null counter-evidence escalation included at synthesis | Partial | Partial |
| **V-04** | C-16 + C-17 severity stack | Combines V-01 and V-02: two-lock mechanism — CE-score penalty AND escalation block both activate on null. Cannot have one without the other | Full | Full |
| **V-05** | Full excellence compound | R3 V-05 baseline + C-16 + C-17 integrated: all 17 criteria addressed in one body | Full | Full |

**Design pattern across R4:** The C-14/C-16/C-17 severity stack is treated as a unified path — a variation that handles C-16 (escalation) without C-17 (formula consequence) is still exploitable, because the narrative can call the escalation and then assign HIGH anyway. V-04 and V-05 close both locks simultaneously, requiring both the numeric penalty and the status block to be resolved before the campaign can promote.
