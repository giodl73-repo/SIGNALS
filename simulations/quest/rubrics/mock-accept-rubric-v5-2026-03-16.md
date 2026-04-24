Looking at the R4 scorecard, I can identify two new excellence patterns from the PASS/PARTIAL differential evidence:

1. **C-20** — "Branch-anchor exemplars on both Subject-check branches" — V-05 C-19 PASS evidence names "VERDICT-ECHO examples and NONE examples anchor both branches." V-03 C-19 PASS names the conditional structure but no exemplars. PARTIAL = conditional present without per-branch named examples; PASS = at least one concrete named example per branch.

2. **C-21** — "Enforcement note following CANARY TERMINOLOGY TABLE" — V-04 and V-05 C-18 PASS evidence includes "inline 'Do NOT conflate them.' follows table as enforcement note." V-02 PASS has the table but no enforcement note in evidence. PARTIAL = table without trailing enforcement sentence; PASS = enforcement sentence follows table as a second-layer prohibition.

Aspirational denominator: 11 → 13. Max aspirational: 13 × 1.25 = 16.25. Total ceiling: 106.25.

---

# Scoring Rubric: mock-accept v5

**Changes from v4**: 2 new aspirational criteria (C-20, C-21) extracted from R4 scorecard excellence signals. Aspirational denominator updated from 11 to 13. Ceiling updated from 103.75 to 106.25.

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

REAL-REQUIRED verdict block contains all required structural fields: trigger / Failing evaluation / Failing verdict / Claim + Error-code / Artifact state. All five fields present and populated for each REAL-REQUIRED namespace.

---

#### C-09 — SKIP table present and populated
**Weight**: recommended | **Category**: output-structure

SKIP table records skipped namespaces with reason codes. Explicit empty record required when no namespaces are skipped — omission is not a valid empty SKIP table.

---

#### C-10 — Slot-2-first ordering in MOCK-ACCEPTED argument
**Weight**: recommended | **Category**: output-structure

SLOT 2 (Contrast) written before SLOT 1 (Structural position) in MOCK-ACCEPTED positive argument. Reversed ordering (Slot-1-first) = PARTIAL; Slot-2-first with Slot-1 anchored to SQ-1 = PASS.

---

#### C-11 — Bypass error codes named at guard sites
**Weight**: recommended | **Category**: behavior

ARCH-GUARD-BYPASS and STRATEGY-TO-PM-GUARD-BYPASS appear at the guard invocation site — not only in a summary section. Guard-site naming is required; summary-only = PARTIAL.

---

#### C-12 — Two-list partition with explicit empty records
**Weight**: recommended | **Category**: output-structure

Arch-blocked list and Strategy-blocked list each rendered as explicit named records even when empty. Silent omission of an empty list = FAIL; named empty record = PASS.

---

#### C-13 — CANARY GATE two-branch structure
**Weight**: recommended | **Category**: output-structure

CANARY GATE renders as BRANCH A (all Status fields updated) and BRANCH B (at least one Status field not updated) as mutually exclusive labeled branches. Single-branch or prose-only CANARY GATE = PARTIAL.

---

#### C-14 — VERDICT-ECHO Error-code field present in REAL-REQUIRED verdict
**Weight**: recommended | **Category**: output-structure

Error-code field present in REAL-REQUIRED verdict block. VERDICT-ECHO named as value when role is grammatical subject. Field absent or unnamed = FAIL.

---

#### C-15 — CANARY SUPPRESSED prose reframe in BRANCH B
**Weight**: recommended | **Category**: output-quality

BRANCH B contains a prose reframe of CANARY SUPPRESSED as a non-error outcome — not merely an acknowledgment that the branch exists. Absence of reframe in BRANCH B = PARTIAL.

---

#### C-16 — Non-conflation prose sentence for CANARY SUPPRESSED vs CANARY-FALSE-POSITIVE
**Weight**: recommended | **Category**: output-quality

At least one sentence explicitly distinguishes CANARY SUPPRESSED (correct suppression) from CANARY-FALSE-POSITIVE (wrong assertion) in prose. Mere naming of both terms without distinction = PARTIAL.

---

### Aspirational (up to 16.25 pts)

*Each aspirational criterion scores 1.25 pts on PASS, 0.625 pts on PARTIAL, 0 on FAIL. Denominator: 13.*

---

#### C-17 — CANARY SUPPRESSED as labeled `Semantics:` field in BRANCH B
**Weight**: aspirational | **Category**: output-structure

BRANCH B contains `Semantics: SUCCESS — this is the correct disclosure output, not an error or failure mode.` (or equivalent) as a parseable labeled field, not only as prose. Labeled field makes the positive reframe independently checkable without reading surrounding context.

**Pass**: `Semantics:` (or equivalent label) field present in BRANCH B with SUCCESS-class value and non-error declaration.
**Partial**: Positive reframe present as prose in BRANCH B without labeled field structure.
**Fail**: No positive reframe in BRANCH B.

---

#### C-18 — Dedicated non-conflation structure as CANARY TERMINOLOGY TABLE
**Weight**: aspirational | **Category**: output-structure

A table with at minimum Term / Type / Meaning columns appears before BRANCH A/B, with one row for CANARY SUPPRESSED (Type: Correct output) and one row for CANARY-FALSE-POSITIVE (Type: Named error). The Type column forces per-term categorical distinction that cannot be collapsed into a single prose sentence.

**Pass**: Table with Term + Type columns present before branches; CANARY SUPPRESSED and CANARY-FALSE-POSITIVE occupy separate rows with distinct Type values.
**Partial**: Non-conflation distinction expressed as inline prose only (e.g., `Do NOT conflate: CANARY-FALSE-POSITIVE = wrong assertion. CANARY SUPPRESSED = correct suppression.`) — distinction present but structurally collapsible.
**Fail**: No non-conflation structure present.

---

#### C-19 — Subject-check metacognitive sub-step on Error-code
**Weight**: aspirational | **Category**: behavior

A `Subject-check:` sub-step (or equivalent named step) appears before the Error-code field in the REAL-REQUIRED template. The sub-step explicitly identifies whether the grammatical subject of the surrounding sentence is a role name or an artifact/section/field, and the Error-code value is a direct consequence of the Subject-check result. The NONE branch fires as a deliberate identified outcome, not as a passive default.

**Pass**: Named sub-step present; explicit subject-identification conditional (`If subject = role name → VERDICT-ECHO` / `If subject = artifact → NONE`); Error-code references Subject-check result; NONE is deliberate, not fallback.
**Partial**: Error-code conditional present (e.g., as a Note form) without a named sub-step; NONE branch is passive application of the conditional rather than a deliberate result.
**Fail**: No conditional on Error-code; single unconditional VERDICT-ECHO or NONE.

---

#### C-20 — Branch-anchor exemplars on both Subject-check branches
**Weight**: aspirational | **Category**: output-quality

Both the VERDICT-ECHO branch and the NONE branch of the Subject-check conditional include at least one concrete named example that instantiates the rule — e.g., `If subject = role name [e.g., Head of Operations] → VERDICT-ECHO` and `If subject = artifact [e.g., the Coverage Review table] → NONE`. Anchor examples make both application paths checkable by inspection, not only by rule interpretation.

**Pass**: At least one named concrete example present for each branch (VERDICT-ECHO branch and NONE branch).
**Partial**: Anchor examples present for one branch only, or abstract examples present for both (e.g., "[role name]" without a concrete instance).
**Fail**: No branch-anchor examples; Subject-check conditional expressed as rule only.

*Extracted from R4 scorecard: V-05 C-19 PASS evidence names "VERDICT-ECHO examples and NONE examples anchor both branches" as a distinguishing element absent from V-03's C-19 PASS evidence.*

---

#### C-21 — Enforcement note following CANARY TERMINOLOGY TABLE
**Weight**: aspirational | **Category**: output-quality

An explicit enforcement sentence (e.g., `Do NOT conflate them.`) follows the CANARY TERMINOLOGY TABLE as a second-layer prohibition. The table provides structural distinction; the enforcement note converts the distinction into an imperative that cannot be treated as informational.

**Pass**: Enforcement sentence present immediately following or within the CANARY TERMINOLOGY TABLE block; sentence is imperative in register and names the prohibited action.
**Partial**: CANARY TERMINOLOGY TABLE present without a trailing enforcement sentence; non-conflation instruction present only in prose elsewhere.
**Fail**: No CANARY TERMINOLOGY TABLE; or table present with no enforcement note and no non-conflation prose.

*Extracted from R4 scorecard: V-04 and V-05 C-18 PASS evidence includes "inline 'Do NOT conflate them.' follows table as enforcement note" as an element present in PASS but absent from V-02's C-18 PASS description.*

---

## Scoring Summary

| Band | Points | Notes |
|------|--------|-------|
| Essential | 60 | C-01 through C-05; all-or-nothing gate |
| Recommended | 30 | C-06 through C-16; partial credit allowed |
| Aspirational | up to 16.25 | C-17 through C-21; 1.25 per PASS, 0.625 per PARTIAL |
| **Ceiling** | **106.25** | All criteria PASS |

**Aspirational denominator**: 13 (C-17 through C-21)
**Max aspirational**: 13 × 1.25 = 16.25
