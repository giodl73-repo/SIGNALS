Written to `simulations/quest/golden/trace-inspect-variate-R6-2026-03-17.md`.

---

## trace-inspect — Variations R6 (v3 rubric)

**Entry state**: R5 champion V-05 = 94/100. Two systematic gaps remain — both C-08 and C-13 are PARTIAL across all R5 variations.

**Root cause of both gaps**: R5 never made either criterion a *required structural output*. Instructions said "minimum 3 rows" (C-08) and "transition sentences" (C-10), but no variation forced the model to emit a verifiable block that a reviewer could audit independently.

---

### Variation axes chosen

| # | Axis | Type |
|---|------|------|
| V-01 | Output format — **FLOOR CHECK block** after Step 3b (C-08) | Single |
| V-02 | Output format — **PREREQUISITE CHECKPOINT block** opening each sub-step (C-13) | Single |
| V-03 | Lifecycle emphasis — **SOURCE PRE-COMMITMENT block** opening Step 3b (C-08 variant) | Single |
| V-04 | C-08 floor enforcement + C-13 checkboxes | Combined |
| V-05 | All three axes + inertia framing | Full integration |

---

### What each axis does mechanically

**V-01 (FLOOR CHECK)**: After the Step 3b findings table, the executor must emit a named block listing every finding ID, row count, distinct Source types, and Action-uniqueness status. A FAIL result BLOCKS advance to Step 3c. Bare count without IDs fails. This converts C-08 from an instruction to a required structural output.

**V-02 (PREREQUISITE CHECKPOINT)**: Before each Phase 3 sub-step body begins, the executor emits a `Prerequisite: / Named artifact: / Check: YES` block. The named-artifact field must cite the specific section produced by the prior step — generic path fails. This distinguishes C-13 (pre-step, named artifact) from C-10 (post-step transition sentence).

**V-03 (SOURCE PRE-COMMITMENT)**: Step 3b opens with a pre-commitment block requiring one seeded finding per represented Source type *before any table row is written*. Seeds must name a specific gap from Stage 1 or execution — generic placeholder fails. This prevents the homogeneous-SA failure mode by forcing source diversity at synthesis time rather than post-hoc.

**V-04**: Both V-01 + V-02. Tests whether the two output-format axes interfere or compound cleanly.

**V-05**: All three axes + the inertia framing paragraph ("the primary alternative is skipping it...") inherited from R5 V-05. Predicted 100/100 if no regression occurs.

---

### Predicted scores

| ID | C-08 | C-13 | Predicted total |
|----|------|------|-----------------|
| V-01 | PASS | FAIL | ~94 (C-13 still absent) |
| V-02 | PARTIAL | PASS | ~91 (C-08 still absent) |
| V-03 | PASS | FAIL | ~94 (C-13 still absent) |
| V-04 | PASS | PASS | ~100 |
| V-05 | PASS | PASS | ~100 |
