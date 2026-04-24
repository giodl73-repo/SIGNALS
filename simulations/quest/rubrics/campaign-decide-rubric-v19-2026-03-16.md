Written to `simulations/quest/rubrics/campaign-decide-rubric-v19-2026-03-17.md`.

**Changes from v18 → v19:**

| | v18 | v19 |
|-|-----|-----|
| Aspirational denominator | /38 | /41 |
| Aspirational total pts | 19.0 | 20.5 |
| Max composite | 109.0 | 110.5 |

**Three new criteria extracted from R19:**

**C-47 — PRE-COMMITMENT recommendation confidence with falsification condition**
Extends the C-45 PRE-COMMITMENT block to include an expected final recommendation and its falsification condition. Phase 5 recommendation record gains a `Prior Recommendation Confidence (from PRE-COMMITMENT)` fifth column, enabling a recommendation-level before/after delta at synthesis — parallel to C-35's hypothesis-level delta. Implies C-45; independent of C-18 (the four required columns remain present, C-47 is an upward extension).

**C-48 — FINDING REGISTER expected FID count annotations (three-point count chain)**
The pre-seeded FINDING REGISTER gains `[expect: N FIDs]` annotations in each phase-group header, aligned to C-44 minimums. Creates a three-point count chain: C-44 section-header floor → C-48 register-header budget → C-46 close-footer actual. All three points verifiable without body-reading. Implies C-16; the chain requires all three criteria for full verification.

**C-49 — Phase 5 synthesis completeness exit annotation**
Phase 5 closes with `Synthesis completeness: [hypothesis-resolution: filled | recommendation-record: filled | counter-evidence: filled | open-questions: filled]`, confirming all four sub-tables are populated. Pairs with C-30 (entry-point bold labels) and C-39 (section-header gate) to bracket Phase 5 at entry and exit — parallel to the C-44/C-46 audit pair that brackets evidence phases. Independent of C-46 (which governs evidence phases 0–4).
