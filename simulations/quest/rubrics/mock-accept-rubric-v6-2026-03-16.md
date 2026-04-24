Reading the scorecard carefully to extract both new patterns before writing the rubric.

From the R5 scorecard:

**C-22**: Count-anchored completeness assertion after CROSS-TEMPLATE RELATIONSHIP BLOCK. V-03/V-05 PASS; V-01/V-02/V-04 FAIL. Denominator row: 2/5.

**C-23**: Named `Violation:` field inside ENFORCEMENT NOTE block. Structural inventory shows V-02/V-04/V-05 PASS; V-01/V-03 FAIL (prose enforcement, no named field). Denominator row: 3/5.

Denominator: 13 → 15. Max aspirational: 15 × 1.25 = 18.75. Ceiling: 108.75.

---

# Scoring Rubric: mock-accept v6

**Changes from v5**: 2 new aspirational criteria (C-22, C-23) extracted from R5 scorecard excellence signals. Aspirational denominator updated from 13 to 15. Ceiling updated from 106.25 to 108.75.

---

## Criteria

### Essential (60 pts)

#### C-01 — DO-NOT gates + FORBIDDEN OUTPUTS TRIAD all present
**Weight**: essential | **Category**: behavior

FORBIDDEN OUTPUTS TRIAD all three labels present with completeness check: "A two-of-three set does not satisfy this gate." AUTO-RULE CONTAMINATION GUARD named with error code. Completeness check language explicit.

**Pass**: All three triad labels present and accompanied by a completeness assertion. Soft mention without completeness check = PARTIAL only.

---

#### C-02 — Triad labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] all labeled
**Weight**: essential | **Category**: behavior

The three FORBIDDEN OUTPUTS labels appear in the output as acknowledged constraints — not silently omitted.

**Fail examples**: listen marked MOCK-ACCEPTED because "structure looks complete"; scout-feasibility accepted at Tier 2 because "only planning stage"; FORBIDDEN OUTPUTS triad mentioned for only 2 of 3 labels.

---

#### C-03 — Status written back in-place with CANARY ASSERTION
**Weight**: essential | **Category**: behavior

Step 8 (non-skippable) edits the source mock artifact file using the Edit tool. Each namespace Status field transitions from `Status: MOCK (awaiting review)` to either `Status: MOCK-ACCEPTED [...]` or `Status: REAL-REQUIRED [...]`. After all edits, the CANARY ASSERTION is emitted confirming zero Status fields remain as "MOCK (awaiting review)".

**Pass**: Edit tool invocation on the source mock artifact path is present.

---

#### C-04 — Review artifact with required structure
**Weight**: essential | **Category**: output-structure

Step 7 writes to `simulations/mock/{topic}-accept-{date}.md`. Coverage Review table with 4 columns. Priority-ordered next-steps (P1/P2/P3). Cross-namespace risk statement with urgency labels.

---

#### C-05 — MOCK-ACCEPTED two-slot positive argument
**Weight**: essential | **Category**: output-structure

Both Slot 1 (Structural position) and Slot 2 (Contrast) present and structurally separate. Reason codes enumerated exactly — no paraphrase.

---

### Recommended (30 pts)

#### C-06 — Entity-naming grammar on all sub-questions
**Weight**: recommended | **Category**: output-quality

Sub-questions ask to name specific components; yes/no answers do not satisfy entity-naming sub-question requirements.

---

#### C-07 — Step sequencing + guard compliance with two-list partition
**Weight**: recommended | **Category**: behavior

Two-list partition output: Arch-blocked list recorded; Strategy-blocked list recorded. ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named at guard sites.

---

#### C-08 — Evaluation-driven REAL-REQUIRED template complete
**Weight**: recommended | **Category**: output-structure

All seven required fields present: trigger field, Failing evaluation, Failing verdict, Claim, Subject-check, Error-code, Artifact state.

---

### Aspirational (1.25 pts each; denominator 15; max 18.75)

#### C-09 through C-16 — Inherited R3 patterns
All eight R3 excellence patterns confirmed present. See v3 rubric for individual definitions.

---

#### C-17 — `Semantics: SUCCESS` labeled field in Branch B
**Weight**: aspirational | **Category**: output-quality

Branch B of the REAL-REQUIRED template carries an explicit `Semantics: SUCCESS` labeled field distinguishing the resolution state from the failure state in Branch A.

**Pass**: Field present and labeled. Unlabeled prose describing success semantics = PARTIAL only.

---

#### C-18 — CANARY TERMINOLOGY TABLE as dedicated non-conflation structure
**Weight**: aspirational | **Category**: output-quality

A dedicated table (minimum two rows: MOCK-ACCEPTED vs. ACCEPTED) appears as a named CANARY TERMINOLOGY TABLE block. The table is not folded into prose — it stands as a separate, addressable structure.

**Pass**: Named table block present with at least two term rows. Inline prose contrast without table structure = PARTIAL only.

---

#### C-19 — Subject-check metacognitive sub-step on Error-code
**Weight**: aspirational | **Category**: behavior

The Error-code field in the REAL-REQUIRED template is accompanied by a Subject-check sub-step that asks the model to verify the error code names the correct subject before emitting the verdict. The sub-step is a named, non-skippable verification gate, not a parenthetical reminder.

**Pass**: Named sub-step with explicit verification instruction present. Parenthetical reminder without gate framing = PARTIAL only.

---

#### C-20 — Branch-anchor exemplars on both Subject-check branches
**Weight**: aspirational | **Category**: output-quality

The Subject-check sub-step provides at least one concrete named example (namespace name, artifact path, or field label) for each branch — one for the PASS branch and one for the FAIL branch. Exemplars may appear in table or prose form; both branches must be covered.

**Pass**: At least one named exemplar per branch present. Conditional structure without per-branch examples = PARTIAL only.

---

#### C-21 — Enforcement note following CANARY TERMINOLOGY TABLE
**Weight**: aspirational | **Category**: output-quality

An enforcement sentence or block appears immediately after the CANARY TERMINOLOGY TABLE as a second-layer prohibition. The enforcement note is structurally separate from the table — it does not appear as a table row or caption. Prose form ("These are distinct. Do NOT conflate them.") and structured block form (ENFORCEMENT NOTE with named fields) both satisfy.

**Pass**: Enforcement sentence or block present after table, structurally separate. Table without trailing enforcement = PARTIAL only.

---

#### C-22 — Cross-template completeness assertion after CROSS-TEMPLATE RELATIONSHIP BLOCK
**Weight**: aspirational | **Category**: behavior

A count-anchored completeness assertion appears immediately after the CROSS-TEMPLATE RELATIONSHIP BLOCK and before either template definition begins. The assertion names the required row count and explicitly states the partial-table failure condition (e.g., "A partial table (fewer than 7 rows) does not satisfy this correspondence requirement."). This applies the same completeness-check mechanism used by the FORBIDDEN OUTPUTS TRIAD to the template correspondence table.

**Pass**: Count anchor present, partial-table condition named explicitly, assertion positioned before first template definition. Table that ends at row 7 and proceeds directly to templates without assertion = FAIL.

---

#### C-23 — Named `Violation:` field inside ENFORCEMENT NOTE block
**Weight**: aspirational | **Category**: output-quality

The ENFORCEMENT NOTE block following the CANARY TERMINOLOGY TABLE includes an explicit named `Violation:` field that identifies the specific conflation error (e.g., using ACCEPTED where MOCK-ACCEPTED is required). The `Violation:` field is structurally named — it appears as a labeled field, not as prose within the block body.

**Pass**: `Violation:` label present as a named field inside the ENFORCEMENT NOTE block. ENFORCEMENT NOTE block present but with only `Rule:` and `Distinction:` fields and no `Violation:` field = PARTIAL only. Prose enforcement note without a block structure = FAIL for this criterion (regardless of C-21 result).

---

## Scoring Summary

| Band | Points | Criteria |
|------|--------|----------|
| Essential | 60 | C-01 through C-05 (12 pts each) |
| Recommended | 30 | C-06 through C-08 (10 pts each) |
| Aspirational | 18.75 max | C-09 through C-23 (1.25 pts each × 15) |
| **Ceiling** | **108.75** | |
