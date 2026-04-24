Written to `simulations/quest/golden/prove-topic-variate-R6-2026-03-16.md`.

---

## R6 Variates — prove-topic

Five complete variations targeting the three new v6 criteria:

| Variation | Axis | Criteria Targeted | Key Change |
|-----------|------|-------------------|------------|
| V-01 | Single: ROLE A binding confirmation | C-24 (+ C-22 floor) | ROLE A adds Step 1: reads CAMPAIGN OPEN INCUMBENT ANCHOR sub-section, records `incumbent_anchor_read` before Stage 0 gates |
| V-02 | Single: Per-artifact Displacement read | C-25 (+ C-16/C-20 floors) | Stages 2/3/4 each add "Displacement read:" field to stage body + artifact content; Stage 5 evidence_summary must cite all three by artifact + value |
| V-03 | Single: Binding note sub-section precision | C-26 (+ C-19/C-22 floors) | Invariant D templates change from `{status_quo_comparator}` to `[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]`; binding note names sub-section specifically with FORMAT ERROR failure label |
| V-04 | Combined: C-24 + C-26 | C-24 + C-26 | ROLE A reads INCUMBENT ANCHOR sub-section by name; Invariant D binding note names sub-section; ROLE A Step 2 verifies the two chain references match |
| V-05 | All-axis: C-24 + C-25 + C-26 | All three | All changes combined; Stage 0 EXIT SIGNAL explicitly confirms displacement read commitment; Stage 5 entry conditions require all three artifact Displacement reads |

**Structural design notes:**

- V-01 vs V-04 isolates C-24 alone vs C-24+C-26 together — tests whether sub-section naming in ROLE A's trace (V-04) produces materially different output than parent-block tracing (V-01)
- V-02 is the only variation that adds the per-artifact Displacement read chain — Stage 5's FAIL condition for "fewer than three artifacts" is the distinguishing instruction
- V-03 vs V-04 isolates C-26 alone vs C-26+C-24 — tests whether ROLE A's pre-stage binding confirmation adds signal when the sub-section binding note is already present
- V-05 is the only variation that includes Stage 0 EXIT SIGNAL explicitly naming "displacement read commitment active" as a pre-advance confirmation
