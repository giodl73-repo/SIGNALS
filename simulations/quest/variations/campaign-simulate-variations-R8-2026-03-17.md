Written to `simulations/quest/golden/campaign-simulate-variate-R8-2026-03-17.md`.

---

## campaign-simulate -- Round 8 Variations

**Base**: R7 V-05 (carries C-24 sub-claim architecture + C-25 per-scope Disposition). All five R7 variations score 100/100 on rubric v6; rubric v7 adds C-29/C-30/C-31 post-convergence. R7 V-05 without those three = 92.7 normalized.

**Single-axis variations:**

**V-01 — C-29: Propagation Coverage Gate**
Axis: adds a `CROSS-SKILL DEPENDENCY MAP` section (numbered DR-01..DR-NN) declared before execution, and a `PROPAGATION COVERAGE GATE` section after synthesis with one row per rule — `Covered by [F-ID]` or `OPEN PROPAGATION GAP [DR-NN]`. Zero silent drops. A 6th structural axis row covers this mechanism.

**V-02 — C-30: Confidence-Stratified Action List**
Axis: adds `Confidence: HIGH / LOW` + `Conf rationale` to the Finding Schema. Splits Ranked Findings into two named action tracks: Track 1 (Implement Now — HIGH-confidence / HIGH-blast) and Track 2 (Confirm Spec First — LOW-confidence / HIGH-blast). Merging the tracks fails C-30 even if blast-radius column is present. A 7th compliance checklist row verifies both tracks.

**V-03 — C-31: Type-Constrained Remediation Verb**
Axis: adds `Classification: GAP / CONTRADICTION / ASSUMPTION` to the Finding Schema. Remediations decompose into Verb / Target / Location / Conformance columns. Verb is vocabulary-constrained by Classification: `GAP → add/remove`, `CONTRADICTION → resolve`, `ASSUMPTION → confirm`. A Remediation verb audit fires at Findings Table close.

**Combined variations:**

**V-04 — C-29 + C-30**
Tests whether dependency map gate and confidence stratification interact. OPEN PROPAGATION GAPSs that would be HIGH-blast must appear in Track 2 with a confirmation question. Six structural axis rows.

**V-05 — C-29 + C-30 + C-31 (proposed golden)**
Full integration on the R7 V-05 base. Seven structural axis rows. Key design insight: ASSUMPTION findings naturally map to Track 2 (C-30 confirmation requirement) with Verb "confirm" (C-31) — both criteria point to the same underlying spec clarification. An evaluator can verify C-30 and C-31 from the same row without cross-referencing sections. The per-scope gate table gains a `Classification` column co-located at elevation time.
