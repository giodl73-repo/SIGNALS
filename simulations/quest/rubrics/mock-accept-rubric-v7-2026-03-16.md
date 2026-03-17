Reading the scorecard carefully to extract the new patterns before writing the updated rubric.

From the R6 scorecard:

**C-24**: ROLE-SEPARATION GATE with ANALYST-PREMATURE-DECISION guard — V-01 (and implicitly all passing variations) PASS. Decision labels (MOCK-ACCEPTED / REAL-REQUIRED) prohibited from Steps 1–5 output; gate check verifies zero decision labels before Decision Authority hand-off; AUTHORITY-REREAD named error present.

**C-25**: Per-namespace `Inertia validation:` field in REAL-REQUIRED template — V-02 PASS (eighth field, structural bonus above the seven-field minimum); tracks cost-of-MOCK inertia per namespace.

Denominator: 15 → 17. Max aspirational: 17 × 1.25 = 21.25. Ceiling: 111.25.

---

```markdown
# Scoring Rubric: mock-accept v7

**Changes from v6**: 2 new aspirational criteria (C-24, C-25) extracted from R6
scorecard excellence signals. Aspirational denominator updated from 15 to 17.
Ceiling updated from 108.75 to 111.25.

---

## Criteria

### Essential (60 pts)

#### C-01 — DO-NOT gates + FORBIDDEN OUTPUTS TRIAD all present
**Weight**: essential | **Category**: behavior

FORBIDDEN OUTPUTS TRIAD all three labels present with completeness check:
"A two-of-three set does not satisfy this gate." AUTO-RULE CONTAMINATION GUARD
named with error code. Completeness check language explicit.

**Pass**: All three triad labels present and accompanied by a completeness
assertion. Soft mention without completeness check = PARTIAL only.

---

#### C-02 — Triad labels [EVIDENCE-HEAVY], [TIER-CRITICAL], [COMPLIANCE] all labeled
**Weight**: essential | **Category**: behavior

The three FORBIDDEN OUTPUTS labels appear in the output as acknowledged
constraints — not silently omitted.

**Fail examples**: listen marked MOCK-ACCEPTED because "structure looks
complete"; scout-feasibility accepted at Tier 2 because "only planning stage";
FORBIDDEN OUTPUTS triad mentioned for only 2 of 3 labels.

---

#### C-03 — Status written back in-place with CANARY ASSERTION
**Weight**: essential | **Category**: behavior

Step 8 (non-skippable) edits the source mock artifact file using the Edit tool.
Each namespace Status field transitions from `Status: MOCK (awaiting review)` to
either `Status: MOCK-ACCEPTED [...]` or `Status: REAL-REQUIRED [...]`. After all
edits, the CANARY ASSERTION is emitted confirming zero Status fields remain as
"MOCK (awaiting review)".

**Pass**: Edit tool invocation on the source mock artifact path is present.

---

#### C-04 — Review artifact with required structure
**Weight**: essential | **Category**: output-structure

Step 7 writes to `simulations/mock/{topic}-accept-{date}.md`. Coverage Review
table with 4 columns. Priority-ordered next-steps (P1/P2/P3). Cross-namespace
risk statement with urgency labels.

---

#### C-05 — MOCK-ACCEPTED two-slot positive argument
**Weight**: essential | **Category**: output-structure

Both Slot 1 (Structural position) and Slot 2 (Contrast) present and structurally
separate. Reason codes enumerated exactly — no paraphrase.

---

### Recommended (30 pts)

#### C-06 — Entity-naming grammar on all sub-questions
**Weight**: recommended | **Category**: output-quality

Sub-questions ask to name specific components; yes/no answers do not satisfy
entity-naming sub-question requirements.

---

#### C-07 — Step sequencing + guard compliance with two-list partition
**Weight**: recommended | **Category**: behavior

Two-list partition output: Arch-blocked list recorded; Strategy-blocked list
recorded. ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS named at guard
sites.

---

#### C-08 — Evaluation-driven REAL-REQUIRED template complete
**Weight**: recommended | **Category**: output-structure

All seven required fields present: trigger, Failing evaluation, Failing verdict,
Claim, Subject-check, Error-code, Artifact state. All fields structurally
separate and non-paraphrased.

---

### Aspirational (21.25 pts — 17 criteria × 1.25 pts each)

#### C-09 — Trigger field at fixed position in REAL-REQUIRED block
**Weight**: aspirational | **Category**: output-structure

Trigger field appears as the first named field in the REAL-REQUIRED template,
not embedded in prose or reordered. Position is structurally fixed, not
contingent on content.

---

#### C-10 — ARCH-GUARD named and positioned at guard site
**Weight**: aspirational | **Category**: behavior

ARCH-GUARD label appears inline at the architectural guard decision point, not
retrospectively summarized. Guard fires before the step that depends on its
resolution.

---

#### C-11 — STRATEGY-TO-PM-GUARD named and positioned at guard site
**Weight**: aspirational | **Category**: behavior

STRATEGY-TO-PM-GUARD label appears inline at the strategy escalation gate, not
retrospectively summarized. Guard fires before step-level continuation.

---

#### C-12 — Cross-step guard reference (step N output references guard from step N-k)
**Weight**: aspirational | **Category**: behavior

Output from a later step explicitly names and references the guard established in
a prior step. Forward-reference guards are not silently re-derived; they are
named by label.

---

#### C-13 — Two-list partition produced and labeled
**Weight**: aspirational | **Category**: output-structure

Output contains exactly two labeled lists: Arch-blocked namespaces and Proceeding
namespaces. Single merged list, unlabeled split, or implicit partition does not
satisfy.

---

#### C-14 — Guard bypass labels present at each bypass site
**Weight**: aspirational | **Category**: behavior

ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS each appear as named labels at
the exact site where the bypass occurs. Post-hoc summary reference does not
satisfy.

---

#### C-15 — Completeness check language explicit in FORBIDDEN OUTPUTS block
**Weight**: aspirational | **Category**: behavior

A sentence-level completeness assertion is embedded directly inside the FORBIDDEN
OUTPUTS block. Completeness assertion located elsewhere in the prompt does not
satisfy this criterion.

---

#### C-16 — Error-code present and named in REAL-REQUIRED template
**Weight**: aspirational | **Category**: output-structure

Error-code is a named, labeled field in the REAL-REQUIRED template. Inline
mention within another field, or omission, does not satisfy.

---

#### C-17 — `Semantics: SUCCESS` labeled field in Branch B
**Weight**: aspirational | **Category**: output-structure

Branch B of the CANARY GATE contains an explicit `Semantics: SUCCESS` labeled
field clarifying that the Branch B emission is the correct disclosure output —
not an error or failure mode.

**Pass**: `Semantics: SUCCESS` present as a named field with disambiguating
prose.

---

#### C-18 — CANARY TERMINOLOGY TABLE as dedicated non-conflation structure
**Weight**: aspirational | **Category**: output-structure

A dedicated table block (not inline prose) contains CANARY SUPPRESSED and
CANARY-FALSE-POSITIVE as named rows with definitions. Structurally separate from
the ENFORCEMENT NOTE. Conflation of both rows into prose does not satisfy.

---

#### C-19 — Subject-check metacognitive sub-step on Error-code
**Weight**: aspirational | **Category**: behavior

Subject-check is a named, non-skippable sub-step within the REAL-REQUIRED
template evaluation, with explicit conditional logic governing its branches.
Parenthetical mention or inline hedge does not satisfy.

---

#### C-20 — Branch-anchor exemplars on both Subject-check branches
**Weight**: aspirational | **Category**: output-structure

A SUBJECT-CHECK EXAMPLES TABLE (or equivalent named structure) contains one
named example for the VERDICT-ECHO branch and one named example for the NONE
branch. Asymmetric coverage (one branch only) does not satisfy.

---

#### C-21 — ENFORCEMENT NOTE structurally separate from CANARY TERMINOLOGY TABLE
**Weight**: aspirational | **Category**: output-structure

ENFORCEMENT NOTE appears as a distinct labeled block immediately following the
CANARY TERMINOLOGY TABLE, not merged into it. Content from the ENFORCEMENT NOTE
must not appear inside the table rows.

---

#### C-22 — Count-anchored completeness assertion after CROSS-TEMPLATE RELATIONSHIP BLOCK
**Weight**: aspirational | **Category**: behavior

Immediately after the CROSS-TEMPLATE RELATIONSHIP BLOCK, a completeness
assertion names the exact count of defined rows and instructs the executor to
confirm that count before proceeding.

**Pass example**: "Verify: all 7 field rows above are mapped before filling
either template. Count: 7 rows defined. Confirm 7 rows present before
proceeding."

**Fail**: completeness check present but count not anchored to a specific
integer; count present but not tied to the CROSS-TEMPLATE RELATIONSHIP BLOCK.

---

#### C-23 — Named `Violation:` field inside ENFORCEMENT NOTE block
**Weight**: aspirational | **Category**: output-structure

The ENFORCEMENT NOTE block contains a `Violation:` labeled field that names the
specific error condition (e.g., CANARY-FALSE-POSITIVE), defines what action
constitutes the violation, and instructs the executor to treat it as a named
error.

**Pass example**: `Violation: Emitting CANARY ASSERTION when one or more Status
fields remain as "MOCK (awaiting review)" = CANARY-FALSE-POSITIVE. Treat as
named error.`

**Fail**: violation described in prose without a `Violation:` label; label
present but error-code absent.

---

#### C-24 — ROLE-SEPARATION GATE with ANALYST-PREMATURE-DECISION guard
**Weight**: aspirational | **Category**: behavior

Decision labels (MOCK-ACCEPTED / REAL-REQUIRED) are explicitly prohibited from
appearing in Steps 1–5 output. A named gate verifies that zero decision labels
are present before hand-off to the Decision Authority role. The named error
AUTHORITY-REREAD is defined and triggered if a decision label appears
prematurely.

**Pass**: All three elements present — (1) prohibition on decision labels before
hand-off, (2) gate check that verifies zero decision labels, (3) AUTHORITY-REREAD
named error with trigger condition.

**Fail**: gate present but AUTHORITY-REREAD unnamed; prohibition stated without
gate check; gate check present but covers only one of the two decision labels.

---

#### C-25 — Per-namespace `Inertia validation:` field in REAL-REQUIRED template
**Weight**: aspirational | **Category**: output-structure

The REAL-REQUIRED template contains an `Inertia validation:` field (eighth field,
beyond the seven-field minimum) that captures the cost-of-MOCK inertia for the
specific namespace under evaluation. Field must be structurally separate —
embedded prose or merger into the Claim field does not satisfy.

**Pass**: `Inertia validation:` appears as a named, labeled field in the
REAL-REQUIRED block with namespace-specific content.

**Fail**: inertia framing present only in prose introduction or step-level
commentary; field present but namespace-generic rather than namespace-specific.

---

## Score Summary

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 to C-05 (12 pts each) | 60 |
| Recommended | C-06 to C-08 (10 pts each) | 30 |
| Aspirational | C-09 to C-25 (1.25 pts each × 17) | 21.25 |
| **Ceiling** | | **111.25** |
```
