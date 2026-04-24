Written to `simulations/quest/rubrics/quest-variate-rubric-v12-variations-R13-2026-03-15.md`.

---

## R13 Variations -- Summary

**C-37 candidate: Phase 2 STOP CONDITION manifest-artifact destination coupling**

The new mechanism: in R12/V-01, the Phase 2 STOP reads "Do not proceed to the **Variation Completion Manifest** until..." -- naming the manifest as the *destination* rather than routing Phase 2 -> Phase 3 generically. This is the Phase 2 mirror of C-36 (which couples the Phase 3 gate to the manifest). Neither R11 nor R12 isolated this mechanism; R12/V-02 retained it (C-36 ablation preserved C-37), and R12/V-03 removed it as a side effect of manifest removal.

**Evidence ladder:**

| Variation | Axis | C-35 | C-36 | C-37 | Score (v12) |
|-----------|------|------|------|------|-------------|
| V-01 | Baseline | PASS | PASS | PASS (candidate) | 100.00 |
| V-02 | C-37 ablation (first independent) | PASS | PASS | FAIL | 100.00 (not yet in rubric) |
| V-03 | C-36 ablation (R12/V-02 state) | PASS | FAIL | PASS | 99.66 |
| V-04 | C-35 ablation (R12/V-03 state) | FAIL | entailed | entailed | 99.31 |
| V-05 | C-37 + C-36 combination | PASS | FAIL | FAIL | 99.66 |

**The key structural pattern in each variation:**

- **V-01 vs V-02**: Sole difference is one sentence -- Phase 2 STOP says "proceed to the Variation Completion Manifest" vs "begin Phase 3". Manifest table, Manifest STOP, and Phase 3 STOP (naming manifest) are identical. This isolates C-37 cleanly for the first time.
- **V-03**: Reproduces R12/V-02 exactly -- provides the C-36 single-ablation control in the R13 context.
- **V-04**: Reproduces R12/V-03 / R11/V-02 exactly -- the foundational C-35 floor, both C-36 and C-37 entailed absent.
- **V-05**: Both Phase 2 and Phase 3 gates decouple from the manifest artifact while manifest remains present -- superadditivity test for the C-37/C-36 pair.

**R13->R14 candidate:** None pre-identified. C-37 is confirmed or denied by behavioral comparison of V-01 vs V-02 manifest-skip rates.
