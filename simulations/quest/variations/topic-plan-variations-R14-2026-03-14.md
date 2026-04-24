Written to `simulations/quest/rubrics/topic-plan-rubric-v13-variate-R14-2026-03-15.md`.

---

## Round 14 Variations — Summary

**Floor preserved from R13 V-01 in all 5 variations:**
- C-42: Rule 1 PASS/FAIL cover identical 5 columns; Rules 2–4 also symmetric
- C-43: All four rules carry paired examples
- C-40: Every null template cites `(Rule 3)`
- C-41: Schema columns carry `[Rule N: ...]` annotations

---

**V-01 — Lifecycle Emphasis (single axis)**
- Adds four explicit PHASE declarations: Pre-read (1–2), Read (3a), Analysis (3b–6), Build (7–10)
- Each boundary has a mandatory checkpoint table; gate must clear before next phase opens
- *Hypothesis*: Named phase gates reduce cross-phase contamination in assumption extraction and delta identification (targets C-03, C-09)

**V-02 — Unified Per-Column Exhibit (single axis)**
- Replaces separate PASS/FAIL lists in all four CONTRACT rules with `| Column | PASS | FAIL |` exhibit tables
- The table format makes C-42 structural: adding a PASS row without a FAIL row is a visible gap in the same table
- *Hypothesis*: Structural format outperforms instructed enforcement for column completeness — V-03/V-04/V-05 from R13 failed C-42 not from missing instruction but from missing affordance

**V-03 — Pre-emptive Threshold Defender (single axis)**
- Moves the Defender from after proposals (R13 V-01 Step 7b) to before proposals (Step 6b)
- Step 6b produces a Change Warrant Table with per-type evidence thresholds
- Proposals that don't clear the warrant are excluded at inception, not post-hoc
- Adds `Warrant met?` column to proposals; Rule 1 PASS/FAIL updated to include `Warrant met?` (replaces `Defender verdict`)
- *Hypothesis*: Threshold-first framing produces fewer preference-only proposals than challenge-after framing

**V-04 — Lifecycle + Unified Exhibit (V-01 + V-02)**
- Phase gates from V-01 + exhibit tables from V-02
- *Hypothesis*: Phase gates guard the temporal axis; exhibit tables guard the structural axis — independent failure modes addressed together

**V-05 — Full Ceiling (V-01 + V-02 + V-03 + CONTRACT Exhibit Audit)**
- All three single axes combined
- Adds a `CONTRACT Exhibit Audit` meta-step before Phase 1: the model produces a table (`Rule | Columns governed | PASS coverage | FAIL coverage | Symmetric?`) and must correct any "No" rows before proceeding
- *Hypothesis*: A self-referential audit that forces the model to count and compare its own PASS/FAIL coverage before execution is the maximum structural enforcement available for C-42/C-43
