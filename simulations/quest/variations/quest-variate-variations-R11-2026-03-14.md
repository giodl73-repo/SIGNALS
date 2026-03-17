Written to `simulations/quest/rubrics/quest-variate-rubric-v11-variations-R11-2026-03-15.md`.

---

## R11 Variation Set Summary

**C-35 candidate mechanism:** Phase 2 Variation Completion Manifest -- a structured table (V-ID rows, "All checks passed?" column) the model fills after all per-variation checkpoints pass and before Phase 3 begins. Distinct from C-29 (Phase 3 STOP CONDITION asserts completion) in that the manifest is the STOP CONDITION's checkable evidence base, not a restatement of it.

| Variation | Axis | Single ablation | Expected score |
|-----------|------|----------------|----------------|
| **V-01** | R11 full-stack baseline + C-35 candidate manifest | -- | 28/28 → 100.00 |
| **V-02** | C-35 ablation — manifest absent; Phase 3 STOP CONDITION retained (R10/V-01 Phase 2/3 boundary state exactly) | C-35 | 27/28 → 99.64 |
| **V-03** | C-31 ablation — predicted-site column directional-only framing (R8/V-01 predicted-site state exactly) | C-31 | 27/28 → 99.64 |
| **V-04** | C-30 ablation — primary-effect uses absence framing instead of positive sibling text (R8/V-03 state exactly) | C-30 | 27/28 → 99.64 |
| **V-05** | V-02 x V-03 combination — C-35 + C-31 dual-ablation floor; superadditivity test | C-35 + C-31 | 26/28 → 99.29 |

**Criterion coverage preserved:**
- C-33: V-02 axis names "R10/V-01 Phase 2/3 boundary state exactly"; V-03 names "R8/V-01 predicted-site column state exactly"; V-04 names "R8/V-03 primary-effect state exactly"
- C-32: V-05 names V-02 (C-35 alone) and V-03 (C-31 alone) by V-ID with explicit superadditivity condition
- C-31: V-03 is the ablation; V-01, V-02, V-04 retain if-then conditional structure (set-level pass)
- C-30: V-04 is the ablation; V-01, V-02, V-03 retain positive sibling text anchoring (set-level pass)
- C-34: All variations retain FROM/TO in secondary-effect hypothesis fields

**R11→R12 candidate:** C-35 (Phase 2 Variation Completion Manifest) — confirmed if V-01-generated sets show lower undetected late-variation incompleteness than V-02-generated sets. V-02 and V-05 provide the ablation evidence; the superadditivity test (V-05 vs V-02/V-03) probes whether manifest removal and mechanism-test framing removal interact.
