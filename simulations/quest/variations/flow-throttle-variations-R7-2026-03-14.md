---

## flow-throttle — Round 7 Variations

**File:** `simulations/quest/rubrics/flow-throttle-rubric-v7-R7-2026-03-14.md`

---

### Variation Summary

| Variation | Axis | C-25 | C-26 | Predicted |
|-----------|------|------|------|-----------|
| **V-01** | Boundary-event phrase isolation — positional-only name (`PRE-EVALUATION ASSERTIONS`, no phrase) | FAIL | PASS | 145/148 |
| **V-02** | Round-head immediacy probe — transitional sentence before container (name has phrase, but content intervenes) | PASS | FAIL | 145/148 |
| **V-03** | Temporal boundary-event form — `(before any Round 2 construct evaluation begins)`, immediately after heading | PASS | PASS | **148/148** |
| **V-04** | Imperative boundary-event form — `(execute before entering Round 2 evaluation)`, immediately after heading | PASS | PASS | **148/148** |
| **V-05** | Combined double-failure — positional-only name + transitional sentence (both C-25 and C-26 fail) | FAIL | FAIL | 142/148 |

---

### Why these axes

R6 confirmed all content-layer axes (role sequence, output format, lifecycle, register) are inert — they cannot touch the pre-barrier container name or heading adjacency. Only two axes can expose C-25 and C-26:

1. **Container name vocabulary** — does it include a boundary-event phrase, or only a positional qualifier?
2. **Heading-to-container adjacency** — is there any intervening content between `## ROUND 2` and the pre-barrier block?

### Diagnostic value of the predicted spread

The three-level spread (148 / 145 / 142) cleanly triangulates the two new criteria:
- If V-05 scores 142 (not less), it confirms C-25 and C-26 are independent with no hidden cascade into earlier criteria.
- If V-03 and V-04 both reach 148, it confirms both temporal and imperative boundary-event phrase forms satisfy C-25 — no form-specificity hidden in the criterion text.
- V-01 vs. V-02 isolates which criterion each axis targets: V-01 = pure C-25 probe, V-02 = pure C-26 probe.
