Here is the complete updated rubric:

---

## Rubric: `topic-echo` — v7

**Skill**: `topic:echo`
**Version**: v7
**Date**: 2026-03-16
**Criteria count**: 22 (4 essential / 3 recommended / **15** aspirational)

**Formula**: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/15 × 10)`

Each full aspirational pass ≈ **0.67 pts** (down from 0.77 in v6, denominator grew 13 → 15).

---

### Two new criteria added

**C-21 | Enforcement Pipeline Staging** (aspirational, enforcement)

Encodes the R6 finding that V-01 (pre-gate namespace check) and V-03 (post-gate redundancy check) each solved a criterion by catching failures at a pipeline position the entry-gate cannot reach. Four positions are defined: **pre-gate** (collection-level properties, e.g. namespace diversity across the full set), **entry-gate** (per-entry structural validation), **post-gate** (cross-entry relational checks, e.g. pairwise redundancy), **synthesis-phase** (compositional failures on the integrated output). Each position catches a structurally distinct failure class invisible at the others.

Pass condition: enforcement mechanisms at ≥2 distinct pipeline positions, each naming at least one failure class detectable only at its position. PARTIAL if ≥2 positions are represented but per-position failure-class specificity is unstated. FAIL if all mechanisms operate at a single pipeline position.

**Orthogonality note**: C-21 and C-20 are orthogonal — scope (what is checked) vs. position (when in the pipeline). Two structural-scope mechanisms at pre-gate and post-gate are additive under C-21 even if C-20 would call them scope-redundant.

---

**C-22 | Synthesis Verdict Commitment** (aspirational, meta)

Encodes the R6 V-02 finding that C-13 PASS required binary verdicts (COMPLETE/INCOMPLETE) with hedged language explicitly listed as FAIL conditions. Hedged verdicts ("appears complete", "generally satisfied") are non-verdicts — they transfer the integration decision to the reader rather than resolving it. The commitment contract applies to any verdict-bearing synthesis section. No verdict (omission) is equivalent to a hedged verdict and also FAIL.

Pass condition: every verdict-bearing synthesis section declares exactly two valid terminal states; section spec lists ≥2 hedged-language forms as FAIL conditions; no-verdict case is itself named as FAIL. PARTIAL if binary states are declared but hedged language is not explicitly listed as FAIL. FAIL if graduated or probabilistic verdicts are permitted.

Cross-reference: **C-22 FAIL → C-13 cannot exceed PARTIAL** (C-13's completeness judgment is a specific instance of the C-22 commitment contract; hedged completeness language fails both).

---

Written to `simulations/quest/rubrics/topic-echo-rubric-v7-2026-03-16.md`.
