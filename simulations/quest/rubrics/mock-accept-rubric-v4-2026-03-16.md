Looking at the R3 scorecard, I can identify three new excellence patterns from the PASS/PARTIAL/FAIL evidence across V-01 through V-04:

1. **C-17** — "CANARY SUPPRESSED is not an error — it is the correct disclosure output" (positive reframe, not just branch presence). V-01/V-04 PASS; V-02/V-03 PARTIAL because inline fallback named but no non-error declaration.

2. **C-18** — "Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE" explicit non-conflation instruction. V-01/V-04 PASS; V-02/V-03 PARTIAL because SUPPRESSED named but no conflation guard.

3. **C-19** — VERDICT-ECHO conditional Error-code field with explicit NONE branch: `Error-code: [VERDICT-ECHO if role is grammatical subject | NONE if artifact is subject]`. V-03 PASS; V-01/V-02/V-04 FAIL (prose annotation or no structured field at all).

Aspirational denominator: 8 → 11. Max aspirational: 11 × 1.25 = 13.75. Total ceiling: 103.75.

---

# Scoring Rubric: mock-accept v4

**Changes from v3**: 3 new aspirational criteria (C-17, C-18, C-19) extracted from R3 scorecard excellence signals. Aspirational denominator updated from 8 to 11.

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

#### C-08 — Evaluation-driven REAL-REQUIRED template
**Weight**: recommended | **Category**: output-structure

Full evaluation-driven REAL-REQUIRED template: trigger, Failing evaluation, Failing verdict, SQ answer (artifact as subject), Artifact state. VERDICT-ECHO present.

---

### Aspirational (up to 13.75 pts)

#### C-09–C-10
Carried from earlier rounds.

---

#### C-11 — Bypass-error-code fields explicit
**Weight**: aspirational | **Category**: behavior

`bypass-error-code: ARCH-GUARD-BYPASS` and `bypass-error-code: STRATEGY-TO-PM-GUARD-BYPASS` appear as explicit labeled fields at their respective guard sites — not inferred from prose.

---

#### C-12 — Slot-2-first ordering instruction
**Weight**: aspirational | **Category**: output-structure

Skill contains an explicit instruction to write Slot 2 (Contrast) before Slot 1 (Structural position): "WRITE CONTRAST SLOT FIRST — DO NOT write Slot 1 before Slot 2."

---

#### C-13 — SKIP table for auto-flagged rows
**Weight**: aspirational | **Category**: output-structure

SKIP appears in all evaluation columns for auto-flagged namespace rows; auto-flagged rows are not re-evaluated.

---

#### C-14 — CANARY SUPPRESSED two-branch gate structure
**Weight**: aspirational | **Category**: behavior

A BRANCH A / BRANCH B gate structure governs the CANARY ASSERTION step — not an inline fallback. Both branches are labeled and separated. CANARY SUPPRESSED is defined as a distinct terminal output state, not as a variant of CANARY-FALSE-POSITIVE.

**Pass**: Explicit BRANCH A / BRANCH B labels with separate branch bodies. Inline fallback with no gate structure = PARTIAL only.

---

#### C-15 — Empty blocked-lists stated explicitly for both guard steps
**Weight**: aspirational | **Category**: output-structure

Both the Step 3 Arch-blocked guard record and the Step 4 Strategy-blocked guard record carry "REQUIRED OUTPUT even when list is empty" language plus an explicit empty-list notation (e.g., `Arch-blocked: []` or equivalent). Omitting the empty-list notation for either list = PARTIAL. Omitting both = FAIL.

---

#### C-16 — VERDICT-ECHO as structured Error-code field
**Weight**: aspirational | **Category**: output-structure

VERDICT-ECHO appears as a parseable `Error-code:` field, not as a prose annotation. The field is present in the REAL-REQUIRED template as a labeled artifact field with an enumerated value.

**Pass**: `Error-code:` label present with VERDICT-ECHO as an enumerated value. Prose annotation only (e.g., inline bracketed note) = FAIL.

---

#### C-17 — CANARY SUPPRESSED non-error declaration
**Weight**: aspirational | **Category**: behavior

The skill explicitly states that CANARY SUPPRESSED is not an error — framed as a correct and valid terminal output state (e.g., "CANARY SUPPRESSED is not an error — it is the correct disclosure output"). Without this declaration, implementers may incorrectly treat SUPPRESSED as a failure state requiring recovery or retry.

**Pass**: An affirmative non-error statement present. Absence of error framing without a positive declaration = PARTIAL. No mention = FAIL.

**R3 evidence**: V-01 PASS ("CANARY SUPPRESSED is not an error"); V-04 PASS ("it is the correct disclosure output"); V-02/V-03 PARTIAL (named as inline fallback but no non-error declaration).

---

#### C-18 — "Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE" instruction
**Weight**: aspirational | **Category**: behavior

The skill contains an explicit non-conflation instruction preventing CANARY SUPPRESSED from being merged with or treated as CANARY-FALSE-POSITIVE. The two branches serve distinct purposes: SUPPRESSED is a valid disclosure outcome; FALSE-POSITIVE is a detection error. Without explicit separation, downstream consumers may collapse the two states.

**Pass**: "Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE" or equivalent direct instruction present. Implicit separation without a conflation guard = PARTIAL. No distinction = FAIL.

**R3 evidence**: V-01 PASS ("Do NOT conflate CANARY SUPPRESSED with CANARY-FALSE-POSITIVE"); V-04 PASS (same); V-02/V-03 PARTIAL (SUPPRESSED named but no guard instruction).

---

#### C-19 — VERDICT-ECHO conditional Error-code field with explicit NONE branch
**Weight**: aspirational | **Category**: output-structure

The VERDICT-ECHO Error-code field enumerates both the positive case and the NONE case: `Error-code: [VERDICT-ECHO if role is grammatical subject | NONE if artifact is subject]`. The NONE branch makes the field parseable for the non-error path; without it, the field applies only to the failure case and is incomplete as a machine-checkable code.

**Pass**: Conditional enumeration present with both VERDICT-ECHO and NONE branches, keyed to subject identity. Single-value field (VERDICT-ECHO only) with no NONE branch = PARTIAL. Prose annotation or no field = FAIL.

**R3 evidence**: V-03 PASS (`Error-code: [VERDICT-ECHO if role is grammatical subject | NONE if artifact is subject]` — structured field with enumerated conditional values); V-01/V-02 FAIL (prose note only); V-04 FAIL (prose annotation, not a structured field).

---

## Scoring Model

| Band | Criteria | Points each | Max |
|------|----------|------------|-----|
| Essential | C-01–C-05 | 12 (PARTIAL = 6) | 60 |
| Recommended | C-06–C-08 | 10 (PARTIAL = 5) | 30 |
| Aspirational | C-09–C-19 | 1.25 (PARTIAL = 0.625) | 13.75 |
| **Total** | | | **103.75** |
