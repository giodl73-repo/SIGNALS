Written to `simulations/quest/rubrics/flow-throttle-rubric-v11-variations-R11-2026-03-15.md`.

---

## Round 11 — flow-throttle Variations Summary

**Design goal:** Two new v11 criteria — C-33 (Phase 0 Inertia Frame) and C-34 (Phase-Anchor Tabular Encoding) — are independently decomposed by testing the two anchors of C-34 separately, then crossing both failure modes.

| V | Axis | C-33 | C-34 | Score |
|---|------|------|------|-------|
| V-01 | Single: Phase 0 alternative label — `### STEP 0 — Baseline Snapshot` | PASS | PASS | **172/172** |
| V-02 | Single: Phase 4 fully prose — all Phase 4 tables removed | PASS | FAIL | **169/172** |
| V-03 | Single: Phase 1 numbered-entry format — TABLE 1 replaced with labeled blocks | PASS | FAIL | **169/172** |
| V-04 | Combination: PA Capacity Planner (R1) + Documentation Verifier (R2) + Phase 0 | PASS | PASS | **172/172** |
| V-05 | Combination: No Phase 0 + Phase 4 fully prose (double failure) | FAIL | FAIL | **166/172** |

**Score spread: 172 / 169 / 169 / 172 / 166 — three levels.**

**Key structural findings this round should confirm:**

1. **C-33 label-inertness** (V-01): "Step 0" is explicitly in the C-33 pass condition — testing it confirms the equivalence class is real, not just declared.

2. **C-34 anchor decomposition** (V-02 vs V-03): V-02 fails via the Phase-4 anchor; V-03 fails via the Phase-1 anchor. Both score 169 but via different missing elements — proving C-34's conjunctive semantics. You can't satisfy C-34 with only one anchor phase.

3. **C-33 role-inertness** (V-04): Phase 0 presence survives a role-axis change; confirms C-33 operates at the phase-structure layer, not the persona layer.

4. **Double-failure floor** (V-05): 166/172 — exactly the R10 ceiling. Failing both C-33 and C-34 loses the full 6 points added by v11, with no interaction effects between the two criteria.
