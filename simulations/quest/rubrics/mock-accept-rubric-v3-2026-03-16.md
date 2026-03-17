Looking at the Round 2 scorecard evidence, I can identify three new excellence patterns not captured in v2:

1. **CANARY SUPPRESSED branch** — V-01 C-03 evidence: "CANARY SUPPRESSED branch defined" beyond just CANARY-FALSE-POSITIVE
2. **Empty blocked-list must be stated explicitly** — V-02 C-07: "Arch-blocked list (must be stated even if empty)"
3. **VERDICT-ECHO named as error code** — V-01 + V-02 C-08: "VERDICT-ECHO named" as a checkable code in the REAL-REQUIRED template

---

# Scoring Rubric: mock-accept v3

**Changes from v2**: 3 new aspirational criteria (C-14, C-15, C-16) extracted from R2 scorecard excellence signals. Aspirational denominator updated from 5 to 8.

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

### Aspirational (10 pts)

#### C-09 — Risk statement with urgency grouping
**Weight**: aspirational | **Category**: output-quality

Step 7 risk statement includes specific Tier N decision at risk, urgency label (BLOCKING | HIGH | MEDIUM), and urgency grouping commentary for each priority group.

---

#### C-10 — Tier sourcing explicit
**Weight**: aspirational | **Category**: output-structure

Step 1 output includes `"Tier: {N} (source: TOPICS.md | --tier | default)"` — source of tier value is named, not inferred.

---

#### C-11 — Named guard-bypass error codes on each role-transition gate
**Weight**: aspirational | **Category**: behavior
**Source**: V-02 full pass vs V-04 partial on C-07 (R1).

Each of the three inter-role gates names its specific bypass error code: ARCH-GUARD-BYPASS (Step 3), STRATEGY-TO-PM-GUARD-BYPASS (Step 4), GUARD-BYPASS CONTAMINATION (Step 4 entry condition). Soft "set aside" language without a named code = PARTIAL only.

**Pass**: All three codes named in their respective guard sections and in the blocked-list recording sections.

---

#### C-12 — Contrast slot (Slot 2) ordered before structural position (Slot 1)
**Weight**: aspirational | **Category**: output-structure
**Source**: V-01 "SLOT 2 placed before SLOT 1 — strongest CONTRAST-INCOMPLETE prevention" (R1).

C-05 requires both slots present. C-12 adds the ordering constraint: Slot 2 first so it cannot be dropped by omission after Slot 1 reads sufficient. SLOT-ORDER-INVERSION named as error code. "DO NOT write Slot 1 (Structural position) before Slot 2 (Contrast)" imperative present.

**Pass**: In every MOCK-ACCEPTED block, Slot 2 (Contrast) label precedes Slot 1 (Structural position). SLOT-ORDER-INVERSION named.

---

#### C-13 — Auto-rule contamination enforced through output structure (SKIP cells)
**Weight**: aspirational | **Category**: output-structure
**Source**: V-03 "SKIP cells prevent downstream contamination structurally" (R1).

Table-first format puts Arch = SKIP / Strategy = SKIP / PM = SKIP in auto-flagged rows. Partial SKIP (only one column) is itself a contamination error. N/A for prose-only formats.

**Pass**: All three role columns show SKIP for auto-flagged rows. AUTO-RULE CONTAMINATION referenced in table rules. **N/A** for prose-only formats → 0 toward numerator, denominator stays 8.

---

#### C-14 — CANARY SUPPRESSED branch defined
**Weight**: aspirational | **Category**: behavior
**Source**: V-01 C-03 evidence — "CANARY SUPPRESSED branch defined" beyond CANARY-FALSE-POSITIVE (R2).

C-03 requires the CANARY ASSERTION and CANARY-FALSE-POSITIVE. C-14 adds a second branch: what happens when the batch contains zero mock artifacts (nothing to write back). A CANARY SUPPRESSED branch prevents the assertion from being vacuously satisfied on an empty batch. Without it, a run against zero mocks emits a passing assertion with no edits made.

**Pass**: CANARY ASSERTION block contains both CANARY-FALSE-POSITIVE branch and a CANARY SUPPRESSED branch covering the zero-mock-artifacts case.

---

#### C-15 — Empty blocked-list explicitly stated (not omitted)
**Weight**: aspirational | **Category**: output-structure
**Source**: V-02 C-07 evidence — "Arch-blocked list (must be stated even if empty)" (R2).

C-07 requires the two-list partition. C-15 adds the no-omission constraint: if zero namespaces are blocked at a gate, the list must be written as "Arch-blocked: (none)" not silently absent. A missing list is indistinguishable from a skipped step; only an explicit "(none)" proves the gate was evaluated.

**Pass**: Both Arch-blocked and Strategy-blocked lists are written in the output for every run, even when empty. Absence of a list = FAIL regardless of whether any namespaces were blocked.

---

#### C-16 — VERDICT-ECHO named as error code in REAL-REQUIRED template
**Weight**: aspirational | **Category**: output-structure
**Source**: V-01 + V-02 C-08 evidence — "VERDICT-ECHO named" (R2).

C-08 requires the evaluation-driven REAL-REQUIRED template. C-16 adds the error-code constraint: VERDICT-ECHO must be named as a specific failure mode (echoing the verdict without re-running the evaluation), making the template violation checkable. A template that says "re-state the failing verdict" without naming VERDICT-ECHO as the error code does not satisfy this criterion.

**Pass**: VERDICT-ECHO appears as a named error code in the REAL-REQUIRED template section. A description of the error in prose without the code = PARTIAL only.

---

## Scoring Formula

```
score = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 8 * 10)
```

Aspirational denominator: **5 → 8**.

Scoring convention: PARTIAL = 0.5 pass. N/A (C-13 for prose-only) = 0 toward numerator, denominator stays 8.

---

## Failure Patterns

| Code | Description | Criterion |
|------|-------------|-----------|
| CONTRAST-INCOMPLETE | MOCK-ACCEPTED written without Slot 2 (Contrast) | C-05 |
| SLOT-ORDER-INVERSION | MOCK-ACCEPTED Slot 1 written before Slot 2 | C-12 |
| ARCH-GUARD-BYPASS | Namespaces proceed past Arch gate without partition recording | C-07, C-11 |
| STRATEGY-TO-PM-GUARD-BYPASS | Namespaces proceed past Strategy gate without partition recording | C-07, C-11 |
| GUARD-BYPASS CONTAMINATION | Step 4 entered without confirming Step 3 guard result | C-11 |
| AUTO-RULE CONTAMINATION | Auto-flagged row evaluated instead of SKIP-asserted | C-13 |
| CANARY-FALSE-POSITIVE | CANARY ASSERTION emitted with Status fields still unrewritten | C-03 |
| CANARY SUPPRESSED | CANARY ASSERTION emitted against zero mock artifacts (vacuous pass) | C-14 |
| EMPTY-LIST-OMISSION | Blocked-list absent from output (indistinguishable from skipped gate) | C-15 |
| VERDICT-ECHO | REAL-REQUIRED verdict copied from evaluation without re-derivation | C-08, C-16 |
