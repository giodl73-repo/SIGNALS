The R18 variate file is already complete (2154 lines, all 5 variations). Here's what it contains:

---

**File**: `simulations/quest/golden/prove-topic-variate-R18-2026-03-16.md`
**Rubric**: v17 (C-01–C-17, 9 criteria)
**Baseline**: R17 V-05 structural stack (C-15 tamper-resistant reads, C-16 three-block Stage 5, C-17 dependency inversion)

## R18 Variations

| Variation | Axis | Type | New pattern probed | Target criteria |
|-----------|------|------|--------------------|-----------------|
| **V-01** | `role_dependency_annotation` | single | ROLE OWNERSHIP TABLE gains a `DEPENDS ON` column — C-17 made first-class and auditable rather than inferred from execution order | C-17 PASS+ |
| **V-02** | `displacement_momentum_score` | single | Each stage incumbent check adds a DISPLACEMENT DELTA (-2 to +2); deltas accumulate into `displacement_momentum_score` flowing into Stage 5 BLOCK 3 — trajectory-aware displacement verdict | new C-18 candidate |
| **V-03** | `block3_multi_stage_chain` | single | BLOCK 3 reconstructs displacement evidence from all three stages (S2, S3, S4) individually rather than just Stage 4 aggregate — per-stage trajectory flags contradictions | C-16 PASS+ |
| **V-04** | `role_dependency_annotation` + `block3_multi_stage_chain` | combined | V-01 + V-03 — dependency audit at the role level, full displacement chain audit at Stage 5 | C-16 PASS+ + C-17 PASS+ |
| **V-05** | all three + full structural stack | full | V-01 + V-02 + V-03 on top of C-15 artifact reads at every inter-stage boundary, C-16 three-block structure, C-17 dependency inversion, ATOMIC DUAL-LOCK | 9/9 aspirational target |

---

The file is ready for `/quest:score` to evaluate all five variations against the v17 rubric.
