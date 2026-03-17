# quest-score Variations -- Round 7
**Skill**: quest-score
**Rubric**: v6 (N_essential=5, N_recommended=2, N_aspirational=13)
**Date**: 2026-03-15
**Round**: 7

---

## Design logic

### Unachieved ceilings entering R7

R6 V-05 was the full stack against the v5 rubric (N_aspirational=11). Rubric v6 adds
C-19 (prescribed per-output narrative fields) and C-20 (inter-role gate architecture).
Against v6, R6 V-05 scores:

| Criterion | R6 V-05 status | Gap |
|-----------|----------------|-----|
| C-03 | FAIL (formula) | Uses `aspirational_pass / 11 * 110` (v5 weights). v6 requires `/ 13 * 130`. Wrong denominator and weight produce incorrect composite derivation. |
| C-07 | FAIL | SYNTHESIS contains LEADERBOARD + EXCELLENCE SIGNALS + FAILURE PATTERNS + REGRESSION SIGNALS but no per-output narrative section. C-07 requires "a section per output exists beyond the verdict table." |
| C-19 | FAIL | No per-output narrative of any kind; derives from C-07 gap. Three-field requirement inapplicable because no section exists at all. |
| C-20 | FAIL | Uses phase labels ("PHASE 1 / PHASE 1.5 / PHASE 2 / PHASE 3"), not named role sequence. [SCORING COMPLETE] and [VERIFIER COMPLETE] are phase-level gate tokens. C-20 requires "the prompt defines a named role sequence (e.g., SCORER → VERIFIER → ANALYST); each pair of adjacent roles has a gate token." Phase naming ≠ role naming. |

Secondary reference: R6 V-03 used a named role architecture (ROLE 1: SCORER → [SCORER COMPLETE] →
ROLE 2: VERIFIER → [VERIFIER COMPLETE] → ROLE 3: ANALYST) and achieved C-07 PASS via a per-output
narrative section in ANALYST. It scored C-19 PARTIAL (the narrative template listed three topics as
prose bullets -- "write a 2-4 sentence narrative covering X, Y, Z" -- but did not prescribe three
labeled fields; C-19 requires labeled fields, not prose-covered topics). It scored C-12 PARTIAL
("role-name headings create structural separation, but no gate token makes narrative/verdict
conflation structurally impossible -- only sequentially blocked"). C-20 is expected PASS for V-03
(named roles, inter-role gates present).

Primary targets for R7: C-03 (formula), C-07 (narrative), C-19 (three-field), C-20 (inter-role
gates). Forced infrastructure update: formula corrected to `/ 13 * 130`; baseline table expanded
to include C-19 and C-20 in all V-04/V-05 variations.

### New axes for R7

| Axis | Label | Mechanism | Target criteria |
|------|-------|-----------|-----------------|
| Y | Three-field labeled narrative | ANALYST role adds three PRESCRIBED LABELED FIELDS per output: `Primary differentiator:`, `Primary miss:`, `Verdict spread:`. Tests whether labeled-field form (vs R6 V-03's prose-bullet template) satisfies C-19 PASS vs PARTIAL. | C-19 |
| Z | Inline narrative scaffold | Three prescribed fields placed inline in the scoring phase immediately after each output's composite, without a separate ANALYST role or inter-role gates. Tests whether C-19 can PASS without role separation; whether C-07 PASSes with same-phase placement; whether C-12 and C-20 independently gate their own verdicts. | C-19, C-07, C-12, C-20 |
| C12P | SCORER schema prohibition | Adds an explicit SCORER output schema (Verdict + Evidence only) with a stated prohibition on narrative text in SCORER blocks, framing violations as structurally detectable. Tests whether explicit schema prohibition tips C-12 from PARTIAL to PASS beyond what gate tokens alone achieve. | C-12 |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (Y)**: Three-field labeled narrative in ANALYST role. R6 V-03 role architecture
  base (SCORER / VERIFIER / ANALYST with [SCORER COMPLETE] and [VERIFIER COMPLETE] inter-role
  gates). Formula /13 * 130. No *Why* field, no Change tracking, no anchor, no baseline load.
  Predicts: C-19 PASS (three labeled fields); C-20 PASS (named roles + inter-role gates);
  C-07 PASS (per-output narrative in ANALYST, downstream of verdict blocks); C-12 PARTIAL
  (role separation with gate tokens, but no schema prohibition -- narrative could technically
  appear in SCORER format without a detectable violation); C-03 PASS (formula /13 * 130);
  C-11 FAIL (no *Why*); C-09 FAIL (no anchor); C-13/C-14/C-15/C-16 FAIL (no Change
  infrastructure); C-17 PASS (VERIFIER role with [VERIFIER COMPLETE] gate); C-18 FAIL (no
  anchor, failure-mode blocks = 0).

- **V-02 (Z)**: Inline three-field scaffold. Single-phase scoring (no named roles). Narrative
  scaffold with three prescribed labeled fields written inline immediately after each output's
  composite score. Gate tokens: [SCORING COMPLETE] and [SYNTHESIS COMPLETE] (C-10 synthesis
  gate). No [SCORER COMPLETE] / [VERIFIER COMPLETE] inter-role gates.
  Predicts: C-19 PASS (three labeled fields present per output); C-20 FAIL (no named role
  sequence; synthesis gate present but no inter-role gates -- exactly the rubric's "role-skip
  path" failure mode); C-07 PARTIAL (narrative scaffold beyond verdict cells but inline within
  scoring phase -- C-07 requires "section per output beyond the verdict table"; inline scaffold
  is adjacent to but not a separate section from the scoring block); C-12 FAIL (narrative
  in same section as scoring; conflation is not structurally blocked); C-03 PASS (formula
  updated); C-11 FAIL; C-17 FAIL (no VERIFIER role or verification phase).

- **V-03 (Y + C12P)**: V-01 base plus an explicit SCORER output schema prohibition.
  SCORER blocks defined as consisting of exactly Verdict and Evidence; any additional text
  is labeled a structural violation; per-output narrative is explicitly forbidden in SCORER
  output. ANALYST has the three-field labeled narrative (same as V-01).
  Predicts: C-12 PASS (schema contract makes narrative-in-SCORER a named structural violation,
  not merely a convention -- the prohibition labels the boundary as structurally enforced, not
  just sequential; conflation is "structurally impossible given the boundary" per rubric text);
  C-19 PASS; C-20 PASS; C-07 PASS; C-03 PASS; remaining gaps same as V-01.

### Combination selections (V-04, V-05)

- **V-04 (Y + R6-V05 + formula fix)**: R6 V-05 full-stack architecture (5 named mechanisms,
  5 failure-mode anchor blocks, *Why* field, *Change* field, Change Manifest phase, Baseline
  Load gate, Synthesis completion gate + pre-close checklist) PLUS role naming added to the
  phase architecture PLUS three-field per-output narrative in ANALYST section PLUS formula
  /13 * 130. The two new mechanisms (C-19, C-20) are NOT declared as named mechanisms in the
  enforcement section, and NO new failure-mode blocks are added to the anchor (remains 5/5).
  Diagnostic question: does C-18 score 5/5 (PASS) when the ANALYST narrative and inter-role
  gates are present but undeclared as mechanisms? If yes, V-05's explicit naming is redundant
  for C-18. If no (rubric scorer counts narrative template and role-gate architecture as unnamed
  mechanisms requiring failure-mode blocks), V-05 closes that gap.
  Predicts: C-03 PASS (formula); C-07 PASS; C-12 PASS (roles + gate + prohibition from V-03
  architecture); C-17 PASS (VERIFIER role); C-18 PASS (5/5 named mechanisms); C-19 PASS;
  C-20 PASS; C-11 PASS (*Why* field); C-13/C-15/C-16 PASS (Change infrastructure); C-14 PASS
  (Baseline Load gate inside SCORER role); composite 220/220 predicted.

- **V-05 (Full stack R7)**: V-04 PLUS Mechanism 6 (three-field narrative template) and
  Mechanism 7 (inter-role gate architecture) declared in the enforcement section PLUS Failure
  Mode F (thin narrative path, closes Mechanism 6) and Failure Mode G (role-skip path, closes
  Mechanism 7) added to the anti-pattern anchor. 7 named mechanisms / 7 failure-mode blocks.
  Predicts: all C-01 through C-20 PASS; composite 220/220.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Three-field labeled narrative (ANALYST or inline) | YES (ANALYST) | YES (inline) | YES (ANALYST) | YES (ANALYST) | YES (ANALYST) |
| Named role sequence (SCORER/VERIFIER/ANALYST) | YES | NO | YES | YES | YES |
| [SCORER COMPLETE] inter-role gate | YES | NO | YES | YES | YES |
| [VERIFIER COMPLETE] inter-role gate | YES | NO | YES | YES | YES |
| Synthesis gate [SYNTHESIS OPEN/COMPLETE] | NO | YES (incomplete) | NO | YES | YES |
| SCORER schema prohibition (C-12P) | NO | NO | YES | YES | YES |
| Formula `/13 * 130` | YES | YES | YES | YES | YES |
| *Why*: field per criterion block (C-11) | NO | NO | NO | YES | YES |
| Mandatory *Change*: field (C-15) | NO | NO | NO | YES | YES |
| Change Manifest phase (C-16) | NO | NO | NO | YES | YES |
| Anti-pattern anchor (C-09) | NO | NO | NO | YES | YES |
| Mechanism 6 (narrative template declared) + Failure Mode F | NO | NO | NO | NO | YES |
| Mechanism 7 (inter-role gates declared) + Failure Mode G | NO | NO | NO | NO | YES |
| Failure-mode blocks / named mechanisms | 0/0 | 0/0 | 0/0 | 5/5 | 7/7 |
| Baseline Load gate inside SCORER (C-14) | NO | NO | NO | YES | YES |
| Baseline table includes C-19, C-20 | n/a | n/a | n/a | YES | YES |

---

## V-01 -- Axis Y: Three-field ANALYST narrative, minimal base

**Variation axis**: Role sequence + depth -- three named roles (SCORER / VERIFIER / ANALYST)
carry the structural work. The innovation over R6 V-03 is the ANALYST's PER-OUTPUT NARRATIVE
section: instead of a prose template ("write a 2-4 sentence narrative covering X, Y, Z"), each
output requires three LABELED FIELDS: `Primary differentiator:`, `Primary miss:`, `Verdict
spread:`. Formula corrected to /13 * 130. No *Why* field, no Change tracking, no anti-pattern
anchor, no baseline load gate. Single axis.

**Hypothesis**: Labeled fields satisfy C-19 where R6 V-03's prose bullets produced PARTIAL.
The rubric's C-19 pass condition states each per-output narrative must contain all three
prescribed fields; a narrative that "addresses" the topics in prose may omit a field silently
(C-19 PARTIAL). A labeled-field schema makes each field required by name; absence of a
labeled field is structurally visible. The role architecture with [SCORER COMPLETE] and
[VERIFIER COMPLETE] inter-role gates satisfies C-20 ("the prompt defines a named role
sequence; each pair of adjacent roles has a gate token"). Predicts: C-19 PASS (three
labeled fields); C-20 PASS (named roles + inter-role gates); C-07 PASS (per-output narrative
section in ANALYST, downstream of verdict blocks); C-12 PARTIAL (role gate separation present
but no schema prohibition on narrative-in-SCORER blocks -- convention-blocked, not schema-
impossible); C-17 PASS (named VERIFIER role, [VERIFIER COMPLETE] gate, specificity test
explicitly stated, revision required, ANALYST structurally blocked until [VERIFIER COMPLETE]).

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score
computed from the rubric formula, and a golden-threshold determination. The
scorecard includes a ranked leaderboard, excellence signals, failure patterns,
regression signals, and per-output narrative notes.

---

ROLE 1: SCORER

The Scorer produces a per-criterion verdict and evidence entry for every output.
The Scorer does not verify evidence specificity -- that is the Verifier's role.
The Scorer does not produce per-output narratives or synthesis -- those are the Analyst's role.

For each output:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output;
             uniquely identifies this output -- not a description that
             could apply to any well-designed output of this type]

  Repeat for every criterion in the rubric. No criterion may be skipped.
  No Evidence field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 13 * 130)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not change verdicts or composite scores.

Specificity test: could this evidence entry apply to any well-designed output of
this type, or does it uniquely identify THIS specific output in this scoring run?

For each output, for each criterion:

  Output: [output identifier] | C-[NN]
  Scorer evidence: [copy from Scorer output above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- generic; could describe any output of this type;
                       revision required before Analyst may use this cell
  If FAIL:
    Revised evidence: [rewrite with a specific quote, named structural element,
                       or design choice that is absent from or distinct in this
                       output versus the others in this scoring run]

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

The Analyst uses the Scorer's verdicts and composite scores (substituting Verifier's
revised evidence where revision occurred) to produce synthesis and per-output narratives.
The Analyst does not modify verdicts or scores.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically: "No differentiating excellence signals."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded (PASS to PARTIAL, PASS to FAIL, or PARTIAL to FAIL):

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PER-OUTPUT NARRATIVE

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label; this field is required]
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; if the
                            output passed all criteria, write "None -- all criteria passed";
                            this field is required]
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers; this field is required]

[ANALYST COMPLETE]
```

---

## V-02 -- Axis Z: Inline three-field scaffold, no role separation

**Variation axis**: Output format + lifecycle emphasis -- the three prescribed narrative fields
appear INLINE in the scoring phase, immediately after each output's composite score and before
moving to the next output. No named roles. No inter-role gate tokens. Gate tokens present:
[SCORING COMPLETE] (after all outputs) and [SYNTHESIS COMPLETE] (enclosing synthesis sections).
Formula /13 * 130. No *Why*, no Change tracking, no anchor.

**Hypothesis**: C-19 does not require phase separation -- it requires the three labeled fields to
exist in the per-output narrative section, wherever that section appears. If the narrative scaffold
is written inline after each output's composite, the three fields are present and labeled. C-07
may PASS (narrative "beyond the verdict table" -- scaffold follows the criterion blocks for an
output) or PARTIAL (narrative is in the same phase as scoring, not a structurally distinct
section). C-20 will FAIL: no named role sequence, no inter-role gates -- this is the rubric's
"role-skip path" failure mode (synthesis gate present but VERIFIER and ANALYST phases are
convention-blocked, not structurally gated). C-12 will FAIL: narrative is inline with scoring,
not in a downstream phase. The C-19 PASS + C-20 FAIL combination isolates whether C-19 and C-20
are truly orthogonal (C-19 operates on content of narrative; C-20 operates on role architecture).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, regression signals, and per-output narrative notes.

---

SCORING PHASE

For each output, produce a scoring block for every criterion in the rubric:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output only;
             must uniquely identify this output -- not a description that could
             apply to any well-designed output of this type]

  No criterion may be skipped. No Evidence field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 13 * 130)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

  Immediately after the composite score, write the narrative scaffold for this output:

  NARRATIVE -- [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property]
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely]
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended / aspirational]

Score all N outputs, each followed by its NARRATIVE scaffold.

[SCORING COMPLETE]

---

SYNTHESIS

[SYNTHESIS OPEN]

All four sections below are required inside this gate. Do not write [SYNTHESIS COMPLETE]
until every section is present.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No score spread found."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

[SYNTHESIS COMPLETE]
```

---

## V-03 -- Axes Y + C12P: Role architecture + C-19 + SCORER schema prohibition

**Variation axes**: V-01 base (three-field labeled narrative, role architecture, /13 * 130)
PLUS an explicit SCORER output schema that defines permitted fields and labels narrative
insertion as a structural violation. The SCORER role's criterion block is defined as containing
exactly Verdict and Evidence; any text outside these fields is a schema violation detectable
by format inspection. Single additional axis (C12P) layered on V-01.

**Hypothesis**: R6 V-03 scored C-12 PARTIAL because role-name headings and gate tokens block
ANALYST from starting before SCORER but do not structurally prevent the SCORER from emitting
narrative content alongside verdict blocks. The prohibition + schema contract closes this: it
defines the SCORER output schema as Verdict + Evidence only, labels additions as structural
violations, and makes narrative-in-SCORER format-detectable (a block with extra fields violates
the schema without needing a downstream role to catch it). Rubric C-12 pass condition: "conflation
of narrative into verdict table cells is structurally impossible given the boundary." A named
violation with format-detectable trigger satisfies "structurally impossible" -- the schema
cannot accommodate narrative without a visible format break. Predicts: C-12 PASS; C-19 PASS;
C-20 PASS; C-07 PASS. All other predictions same as V-01.

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score
computed from the rubric formula, and a golden-threshold determination. The
scorecard includes a ranked leaderboard, excellence signals, failure patterns,
regression signals, and per-output narrative notes.

---

ROLE 1: SCORER

SCORER OUTPUT SCHEMA

Every SCORER criterion block consists of exactly and only these two fields:

  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific structural observation]

No additional fields, labels, or free text are permitted in SCORER output.
Per-output narrative, synthesis language, verdict summaries, evaluative prose, and
structural interpretations are PROHIBITED in SCORER blocks. Any SCORER criterion block
containing text beyond Verdict and Evidence is a structural violation detectable by
schema inspection. Narrative content belongs exclusively in the Analyst's PER-OUTPUT
NARRATIVE section.

---

For each output, produce a criterion block for every rubric criterion:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output;
             uniquely identifies this output -- not a description that could
             apply to any well-designed output of this type]

  No criterion may be skipped. No Evidence field may be blank.
  No text outside Verdict and Evidence is permitted in SCORER criterion blocks.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 13 * 130)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not modify verdicts, scores, or SCORER blocks.

Specificity test: could this evidence entry apply to any well-designed output of
this type, or does it uniquely identify THIS specific output in this scoring run?

For each output, for each criterion:

  Output: [output identifier] | C-[NN]
  Scorer evidence: [copy from Scorer output above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- generic; could describe any output of this type;
                       revision required before Analyst may use this cell
  If FAIL:
    Revised evidence: [rewrite with a specific quote, named structural element,
                       or design choice that is absent from or distinct in this
                       output versus the others in this scoring run]

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

The Analyst uses the Scorer's verdicts and composite scores (substituting Verifier's
revised evidence where revision occurred) to produce synthesis and per-output narratives.
The Analyst does not modify verdicts, scores, or SCORER blocks.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically: "No differentiating excellence signals."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PER-OUTPUT NARRATIVE

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label; this field is required]
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS; required]
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers; this field is required]

[ANALYST COMPLETE]
```

---

## V-04 -- Axes Y + R6-V05 architecture + formula fix

**Variation axes**: R6 V-05 full-stack architecture (5 named mechanisms, 5 failure-mode anchor
blocks, *Why* field, *Change* field, Change Manifest phase, Baseline Load gate inside SCORER,
Synthesis completion gate with pre-close checklist) PLUS role naming applied to the phase
architecture PLUS three-field per-output narrative in ANALYST section after synthesis PLUS
formula /13 * 130 PLUS SCORER schema prohibition (from V-03). The two new mechanisms (C-19
narrative template, C-20 inter-role gates) are NOT declared as named mechanisms in the
enforcement section. Anchor remains at 5 failure modes / 5 named mechanisms.

**Hypothesis**: The role naming + inter-role gates satisfy C-20. The three-field per-output
narrative satisfies C-19. The SCORER schema prohibition tips C-12 to PASS. The formula fix
satisfies C-03. All R6 V-05 criteria are carried: *Why* field (C-11), mandatory *Change*
field (C-15), Change Manifest (C-16), Baseline Load gate (C-14), synthesis gate (C-10),
anti-pattern anchor with 5 failure modes (C-09), 5/5 coverage (C-18), VERIFIER phase (C-17).
C-07 PASS via per-output narrative in ANALYST role. Diagnostic: does C-18 score 5/5 PASS
(anchor covers the 5 explicitly named mechanisms; narrative template and inter-role gates
are structural elements present but unnamed as mechanisms) or FAIL (rubric scorer counts
undeclared structural mechanisms as requiring failure-mode blocks)? V-05 closes the gap
by declaring both as named mechanisms with explicit failure-mode blocks.

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism
explanation, a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals. Per-output narrative notes follow synthesis.

---

ANTI-PATTERN ANCHOR -- READ BEFORE SCORING

Five structural failure modes are prohibited. Read all five before Phase 0 begins.

FAILURE MODE A -- OMISSION PATH (prevented by Mechanism 1 below)

  Typical output:

    C-13 -- Inline regression annotation (A)
    Verdict:  PARTIAL
    Evidence: "Each criterion block contains a CHANGE slot that fires when the
               verdict differs from the prior round."
    [no *Change*: field present]

  Why this fails: The Change field is absent. A scorer whose verdict matches the
  baseline has no slot to fill and moves on. The omission is invisible -- no
  structural gap signals that a field is missing. The mandatory form closes this:
  writing NO CHANGE is required for every matching verdict; the field's absence
  is a structural gap, not a valid empty state.

FAILURE MODE B -- FRESH-LOOKUP PATH (prevented by Mechanism 2 below)

  Typical output:

    [SCORER COMPLETE -- no *Change*: fields written during scoring]

    ANALYST ROLE -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS -- improvement
    V-02 C-13: prior PASS, now PARTIAL -- regression

  Why this fails: Regressions were identified by re-reading the baseline in the
  Analyst role -- a retrospective lookup after the scoring pass finished. Any verdict
  divergence not recorded inline during scoring is silently lost. The correct form
  records CHANGE at the scoring site; a manifest phase collects all annotations before
  synthesis begins; synthesis reads only the manifest.

FAILURE MODE C -- MECHANISM-FREE SCORING (prevented by Mechanism 3 below)

  Typical output:

    C-10 -- Structural completion gate (A)
    Verdict:  PARTIAL
    Evidence: "Phase gates are present in the prompt."
    [no *Why*: field]

  Why this fails: "Phase gates are present" describes evidence, not mechanism. It
  names compliance, not architecture. A scorer who writes this cannot be distinguished
  from one who merely checked a box. The mandatory *Why*: field closes this: the
  scorer must name what the gate does architecturally, not just confirm it exists.

FAILURE MODE D -- INCOMPLETE SYNTHESIS (prevented by Mechanism 4 below)

  Typical output:

    LEADERBOARD
    | 1 | V-05 | 165/200 | YES |
    | 2 | V-04 | 155/200 | YES |

    EXCELLENCE SIGNALS
    V-05 -- C-09 -- anti-pattern anchor present.

    [output ends -- FAILURE PATTERNS and REGRESSION SIGNALS absent]

  Why this fails: FAILURE PATTERNS and REGRESSION SIGNALS are absent. No gate token
  marks synthesis as incomplete. A reviewer must read the entire output to notice the
  omission. The [SYNTHESIS COMPLETE] gate closes this: it cannot be written until all
  required sections are confirmed present via pre-close checklist.

FAILURE MODE E -- VERIFIER BYPASS PATH (prevented by Mechanism 5 below)

  Typical output:

    [SCORER COMPLETE]
    [VERIFIER COMPLETE -- skipped; all evidence appeared specific]
    ANALYST ROLE: CHANGE MANIFEST ...

  Why this fails: The VERIFIER role was skipped by convention. The [VERIFIER COMPLETE]
  gate appears but was never traversed -- no evidence cells were reviewed, no specificity
  test applied. Without a verification pass that explicitly reviews each cell and requires
  revision where generic, any general instruction to "write specific evidence" in SCORER
  blocks is intent, not enforcement. The VERIFIER role with explicit specificity test and
  revision requirement closes this: ANALYST cannot begin until [VERIFIER COMPLETE] appears
  after a completed review pass; a gate that appears without a prior review pass is a
  structural violation.

---

ENFORCEMENT ARCHITECTURE

Five structural mechanisms prevent the failure modes above. All are required.

MECHANISM 1 -- Mandatory bidirectional Change field (closes Failure Mode A)

  Every criterion block in SCORER carries a *Change*: field.
  Exactly three permissible values:

    *Change*: NO CHANGE                              -- verdict matches prior round
    *Change*: CHANGE from [prior verdict]: [reason]  -- verdict differs
    *Change*: NO PRIOR DATA                          -- no prior round score available

  The field is always required. It is not conditional.
  A criterion block without *Change*: is structurally incomplete.
  Conditional forms ("write here if verdict changes") are not permitted.

MECHANISM 2 -- Change Manifest phase (closes Failure Mode B)

  After SCORER completes and VERIFIER completes, ANALYST begins with a Change Manifest
  phase that sweeps every *Change*: CHANGE entry into a structured table.
  SYNTHESIS draws from this manifest exclusively.
  SYNTHESIS is architecturally prohibited from re-reading the baseline table or SCORER
  blocks to derive regression data.
  Any regression not recorded at the scoring site via *Change*: is not a detectable
  regression in this round.

MECHANISM 3 -- Mandatory mechanism field (closes Failure Mode C)

  Every criterion block in SCORER carries a *Why*: field after Evidence.
  The field must name the structural mechanism or design property driving the verdict.
  Restating the criterion text does not satisfy *Why*:.
  Describing evidence rather than mechanism does not satisfy *Why*:.
  A criterion block without *Why*: is structurally incomplete.

MECHANISM 4 -- Synthesis completion gate (closes Failure Mode D)

  SYNTHESIS in the ANALYST role is enclosed between [SYNTHESIS OPEN] and [SYNTHESIS COMPLETE].
  All four synthesis sections are required within the gate.
  A pre-close checklist confirms each section before [SYNTHESIS COMPLETE] can be written.
  [SYNTHESIS COMPLETE] cannot appear before the checklist is complete.

MECHANISM 5 -- Evidence verification role (closes Failure Mode E)

  After SCORER and before ANALYST, a dedicated VERIFIER role revisits every evidence
  cell with an explicit specificity test: "could this evidence apply to any well-designed
  output of this type?" Cells that fail require a revised entry.
  ANALYST is structurally unreachable until [VERIFIER COMPLETE] appears.
  A general instruction to "write specific evidence" in SCORER does not satisfy this
  mechanism -- enforcement requires a structurally distinct role with a gate token,
  not a co-located instruction.

---

ROLE 1: SCORER

SCORER OUTPUT SCHEMA

Every SCORER criterion block consists of exactly Verdict, Evidence, *Why*, and *Change*.
No additional fields are permitted. Narrative text, synthesis language, per-output
summaries, and evaluative prose are PROHIBITED in SCORER output. Any SCORER block
containing text beyond the four defined fields is a structural violation.

PHASE 0: BASELINE LOAD (within SCORER, before scoring begins)

If prior-round score data is provided, build a baseline table before any output is scored:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 |
  |--------|------|------|------|------|------|------|------|------|------|------|
  | Output | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 |
  |--------|------|------|------|------|------|------|------|------|------|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

PHASE 1: SCORING (within SCORER, after [PRIOR ROUND LOAD COMPLETE])

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation; uniquely identifies this
             output; fails if it could describe any well-designed output of this type]
  *Why*:    [name the structural mechanism or design property; do not restate the
             criterion; do not describe the evidence; name the architectural property
             that produces this verdict]
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [one sentence -- what changed and why]
          | NO PRIOR DATA

  What satisfies *Why*:
    - PASS:    Name the property that satisfies. Example: "mandatory bidirectional
               field forces NO CHANGE entry, making omission syntactically visible"
    - FAIL:    Name the gap. Example: "no mechanism field -- compliance indistinguishable
               from mechanism understanding at the scoring site"
    - PARTIAL: Name what is present and what is absent.

  No criterion may be skipped.
  No Evidence, *Why*, or *Change* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 13 * 130)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

This is Mechanism 5. The Verifier reviews every evidence entry from SCORER and applies the
specificity test before ANALYST may begin. ANALYST is structurally unreachable until
[VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence entry apply to a different output in this
scoring run, or to any well-designed output of this type?" If yes, the cell fails
specificity and revision is required before this role can close.

For every output, for every criterion:

  Output: [output identifier] | C-[NN]
  SCORER evidence: [copy from SCORER output above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- could describe another output or any well-designed output
                       of this type; revision required
  If FAIL:
    Revised evidence: [rewrite with a specific structural property, verbatim quote,
                       or design decision unique to this output in this scoring run]

After all outputs are verified:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

PHASE 2: CHANGE MANIFEST (within ANALYST, before synthesis)

Collect every *Change*: field that reads CHANGE from [prior] from SCORER into this manifest.
List only entries where a change occurred; NO CHANGE and NO PRIOR DATA entries are omitted.

  | Output | Criterion | Prior verdict | Current verdict | Reason for change |
  |--------|-----------|---------------|-----------------|-------------------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

PHASE 3: SYNTHESIS (within ANALYST, after [CHANGE MANIFEST COMPLETE])

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above. Any regression
not recorded in SCORER via a *Change*: field is not a detectable regression in this round.

[SYNTHESIS OPEN]

All four sections below are required inside this gate. Do not write [SYNTHESIS COMPLETE]
until every section is present. Omitting or merging any section leaves [SYNTHESIS OPEN]
unclosed.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest in Phase 2 only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

Pre-close checklist -- all five must be confirmed before [SYNTHESIS COMPLETE]:
  [ ] LEADERBOARD complete: all N outputs ranked by composite score, descending
  [ ] EXCELLENCE SIGNALS complete: signal named (output + criterion + mechanism), or
      absence explicitly stated
  [ ] FAILURE PATTERNS complete: all-fail criteria identified with diagnosis, or
      absence explicitly stated
  [ ] REGRESSION SIGNALS complete: drawn from Change Manifest; regressions listed
      or absence / no-prior-data explicitly stated
  [ ] VERIFIER role traversed: [VERIFIER COMPLETE] appears above; all evidence cells
      reviewed; verification summary written

[SYNTHESIS COMPLETE]

PHASE 4: PER-OUTPUT NARRATIVE (within ANALYST, after [SYNTHESIS COMPLETE])

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label; this field is required]
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS; required]
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers; this field is required]

[ANALYST COMPLETE]
```

---

## V-05 -- Full stack R7: V-04 + Mechanism 6 + Mechanism 7 + Failure Modes F + G

**Variation axes**: V-04 full-stack PLUS Mechanism 6 (three-field narrative template) declared
as a named mechanism PLUS Mechanism 7 (inter-role gate architecture) declared as a named
mechanism PLUS Failure Mode F (thin narrative path, prevented by Mechanism 6) and Failure Mode G
(role-skip path, prevented by Mechanism 7) added to the anti-pattern anchor. Seven named
mechanisms / seven failure-mode blocks. This closes the C-18 ambiguity introduced by V-04: if
a rubric scorer counts the narrative template and inter-role gates as unnamed mechanisms requiring
failure-mode blocks, V-04 would score C-18 FAIL; V-05 eliminates that interpretation by declaring
both as named mechanisms with explicit anchor coverage.

**Hypothesis**: All seven mechanisms are named; seven failure-mode blocks cover each named
mechanism; C-18's exhaustive-coverage requirement (one failure-mode block per named structural
mechanism) is satisfied at 7/7. All other V-04 predictions carry forward. Predicts: all C-01
through C-20 PASS; composite 220/220.

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism
explanation, a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals. Per-output narrative notes follow synthesis.

---

ANTI-PATTERN ANCHOR -- READ BEFORE SCORING

Seven structural failure modes are prohibited. Read all seven before Phase 0 begins.

FAILURE MODE A -- OMISSION PATH (prevented by Mechanism 1 below)

  Typical output:

    C-13 -- Inline regression annotation (A)
    Verdict:  PARTIAL
    Evidence: "Each criterion block contains a CHANGE slot that fires when the
               verdict differs from the prior round."
    [no *Change*: field present]

  Why this fails: The Change field is absent. A scorer whose verdict matches the
  baseline has no slot to fill and moves on. The omission is invisible -- no
  structural gap signals that a field is missing. The mandatory form closes this:
  writing NO CHANGE is required for every matching verdict; the field's absence is
  a structural gap, not a valid empty state.

FAILURE MODE B -- FRESH-LOOKUP PATH (prevented by Mechanism 2 below)

  Typical output:

    [SCORER COMPLETE -- no *Change*: fields written during scoring]

    ANALYST ROLE -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS
    V-02 C-13: prior PASS, now PARTIAL -- regression

  Why this fails: Regressions were identified by re-reading the baseline in ANALYST --
  a retrospective lookup after scoring finished. Any divergence not recorded inline is
  silently lost. The correct form records CHANGE at the scoring site; a Change Manifest
  phase collects all annotations before synthesis begins; synthesis reads only the manifest.

FAILURE MODE C -- MECHANISM-FREE SCORING (prevented by Mechanism 3 below)

  Typical output:

    C-10 -- Structural completion gate (A)
    Verdict:  PARTIAL
    Evidence: "Phase gates are present in the prompt."
    [no *Why*: field]

  Why this fails: "Phase gates are present" describes evidence, not mechanism. It names
  compliance, not architecture. The *Why*: field closes this: the scorer must name the
  architectural property -- what the gate does and what path it closes -- not merely
  confirm the gate exists.

FAILURE MODE D -- INCOMPLETE SYNTHESIS (prevented by Mechanism 4 below)

  Typical output:

    LEADERBOARD
    | 1 | V-05 | 165/200 | YES |
    EXCELLENCE SIGNALS
    V-05 -- C-09 -- anti-pattern anchor present.
    [output ends -- FAILURE PATTERNS and REGRESSION SIGNALS absent]

  Why this fails: FAILURE PATTERNS and REGRESSION SIGNALS are absent. No gate token
  marks synthesis as incomplete. The [SYNTHESIS COMPLETE] gate closes this: it cannot
  be written until all required sections are confirmed present via pre-close checklist.

FAILURE MODE E -- VERIFIER BYPASS PATH (prevented by Mechanism 5 below)

  Typical output:

    [SCORER COMPLETE]
    [VERIFIER COMPLETE -- skipped; evidence appeared specific]
    ANALYST: CHANGE MANIFEST ...

  Why this fails: The VERIFIER role was skipped by convention. Without a verification
  pass that explicitly applies the specificity test to each cell and requires revision
  where generic, a general instruction to "write specific evidence" in SCORER is intent,
  not enforcement. The VERIFIER role with gate closes this: ANALYST cannot begin until
  [VERIFIER COMPLETE] appears after a completed review pass.

FAILURE MODE F -- THIN NARRATIVE PATH (prevented by Mechanism 6 below)

  Typical output:

    Output V-03:
    Primary differentiator: V-03 uses a three-role architecture (SCORER, VERIFIER,
    ANALYST) which separates verdict production from synthesis. This is the key structural
    feature that explains V-03's higher score on C-12 and C-20 relative to other outputs.

    [Primary miss: absent -- not written]
    [Verdict spread: absent -- not written]

  Why this fails: The narrative names one structural feature (three-role architecture) but
  omits the primary miss and the verdict spread interpretation. A scorer reading only this
  narrative cannot determine what structural gap the output has, or how its points
  distributed across essential / recommended / aspirational tiers. C-07 is satisfied
  (structural feature present) while C-19 fails (only one of three required fields).
  The three-field labeled template closes this: Primary differentiator, Primary miss, and
  Verdict spread are required labeled fields; writing one field does not discharge the
  others; each field's absence is structurally visible by name.

FAILURE MODE G -- ROLE-SKIP PATH (prevented by Mechanism 7 below)

  Typical output:

    PHASE 1: SCORING
    ...
    [SCORING COMPLETE]

    PHASE 2: CHANGE MANIFEST
    ...
    [CHANGE MANIFEST COMPLETE]

    PHASE 3: SYNTHESIS
    ...
    [SYNTHESIS COMPLETE]

    Note: Evidence verification was omitted; all evidence appeared specific.

  Why this fails: The VERIFIER role was skipped because no inter-role gate token required
  it. The [SYNTHESIS COMPLETE] gate confirms synthesis is complete but cannot detect that
  VERIFIER never ran. A scorer who decides VERIFIER is unnecessary can proceed directly
  from SCORER to synthesis with no structural signal of the skip. The inter-role gate
  architecture closes this: [SCORER COMPLETE] must appear before VERIFIER begins;
  [VERIFIER COMPLETE] must appear before ANALYST begins; an output where [VERIFIER
  COMPLETE] is absent or appears without a preceding [SCORER COMPLETE] is structurally
  detectable as an invalid role sequence.

---

ENFORCEMENT ARCHITECTURE

Seven structural mechanisms prevent the failure modes above. All are required.

MECHANISM 1 -- Mandatory bidirectional Change field (closes Failure Mode A)

  Every criterion block in SCORER carries a *Change*: field.
  Exactly three permissible values:

    *Change*: NO CHANGE                              -- verdict matches prior round
    *Change*: CHANGE from [prior verdict]: [reason]  -- verdict differs
    *Change*: NO PRIOR DATA                          -- no prior round score available

  The field is always required. It is not conditional.
  A criterion block without *Change*: is structurally incomplete.
  Conditional forms ("write here if verdict changes") are not permitted.

MECHANISM 2 -- Change Manifest phase (closes Failure Mode B)

  After SCORER and VERIFIER complete, ANALYST sweeps every *Change*: CHANGE entry into
  a structured manifest before synthesis begins. SYNTHESIS draws from this manifest only.
  SYNTHESIS is architecturally prohibited from re-reading the baseline table or SCORER
  blocks to derive regression data. Any regression not recorded at the scoring site is
  not a detectable regression in this round.

MECHANISM 3 -- Mandatory mechanism field (closes Failure Mode C)

  Every criterion block in SCORER carries a *Why*: field after Evidence.
  The field must name the structural mechanism or design property driving the verdict.
  Restating the criterion text does not satisfy *Why*:.
  Describing evidence rather than mechanism does not satisfy *Why*:.
  A criterion block without *Why*: is structurally incomplete.

MECHANISM 4 -- Synthesis completion gate (closes Failure Mode D)

  SYNTHESIS in ANALYST is enclosed between [SYNTHESIS OPEN] and [SYNTHESIS COMPLETE].
  All four synthesis sections are required within the gate.
  A pre-close checklist confirms each section before [SYNTHESIS COMPLETE] can be written.
  [SYNTHESIS COMPLETE] cannot appear before the checklist is complete.

MECHANISM 5 -- Evidence verification role (closes Failure Mode E)

  After SCORER and before ANALYST, a dedicated VERIFIER role revisits every evidence cell
  with an explicit specificity test: "could this evidence apply to any well-designed output
  of this type?" Cells that fail require a revised entry before [VERIFIER COMPLETE] can
  appear. ANALYST is structurally unreachable until [VERIFIER COMPLETE] appears.

MECHANISM 6 -- Three-field narrative template (closes Failure Mode F)

  Each per-output narrative section in ANALYST contains three prescribed labeled fields:
  Primary differentiator, Primary miss, and Verdict spread. Each field is always required
  and named; a narrative entry lacking any of the three fields is structurally incomplete
  by label inspection. A narrative that discusses one or two fields as prose topics without
  labeling them as separate required fields does not satisfy this mechanism.

MECHANISM 7 -- Inter-role gate architecture (closes Failure Mode G)

  For a scoring sequence with K named roles, K-1 inter-role gate tokens are required in
  prescribed order. In a three-role sequence (SCORER / VERIFIER / ANALYST): [SCORER
  COMPLETE] must appear before VERIFIER begins; [VERIFIER COMPLETE] must appear before
  ANALYST begins. These gates are in addition to the synthesis completion gate (C-10)
  and the baseline load gate (C-14). An output where any inter-role gate is absent or
  appears out of order is structurally detectable as an invalid role sequence. A synthesis
  gate alone does not satisfy this mechanism.

---

ROLE 1: SCORER

SCORER OUTPUT SCHEMA

Every SCORER criterion block consists of exactly Verdict, Evidence, *Why*, and *Change*.
No additional fields are permitted. Narrative text, synthesis language, per-output
summaries, and evaluative prose are PROHIBITED in SCORER output. Any SCORER block
containing text beyond the four defined fields is a structural violation detectable by
schema inspection. Narrative content belongs exclusively in the Analyst's PER-OUTPUT
NARRATIVE section.

PHASE 0: BASELINE LOAD (within SCORER, before scoring begins)

If prior-round score data is provided, build a baseline table before any output is scored:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 |
  |--------|------|------|------|------|------|------|------|------|------|------|
  | Output | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 |
  |--------|------|------|------|------|------|------|------|------|------|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

PHASE 1: SCORING (within SCORER, after [PRIOR ROUND LOAD COMPLETE])

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation; uniquely identifies this
             output; fails if it could describe any well-designed output of this type]
  *Why*:    [name the structural mechanism or design property; do not restate the
             criterion; do not describe the evidence; name the architectural property
             that produces this verdict]
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [one sentence -- what changed and why]
          | NO PRIOR DATA

  What satisfies *Why*:
    - PASS:    Name the property that satisfies.
    - FAIL:    Name the gap.
    - PARTIAL: Name what is present and what is absent.

  No criterion may be skipped.
  No Evidence, *Why*, or *Change* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 13 * 130)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

This is Mechanism 5. The Verifier reviews every evidence entry from SCORER and applies the
specificity test before ANALYST may begin. ANALYST is structurally unreachable until
[VERIFIER COMPLETE] appears below. This role cannot be skipped; [VERIFIER COMPLETE]
appearing without a preceding completed review pass is a structural violation (Failure Mode G).

Specificity test: ask "could this evidence entry apply to a different output in this
scoring run, or to any well-designed output of this type?" If yes, the cell fails
specificity and revision is required before [VERIFIER COMPLETE] can appear.

For every output, for every criterion:

  Output: [output identifier] | C-[NN]
  SCORER evidence: [copy from SCORER output above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- could describe another output or any well-designed output
                       of this type; revision required
  If FAIL:
    Revised evidence: [rewrite with a specific structural property, verbatim quote,
                       or design decision unique to this output in this scoring run]

After all outputs are verified:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

PHASE 2: CHANGE MANIFEST (within ANALYST, before synthesis)

This is Mechanism 2. Collect every *Change*: field that reads CHANGE from [prior] into
this manifest. List only entries where a change occurred.

  | Output | Criterion | Prior verdict | Current verdict | Reason for change |
  |--------|-----------|---------------|-----------------|-------------------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

PHASE 3: SYNTHESIS (within ANALYST, after [CHANGE MANIFEST COMPLETE])

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above. Any regression
not recorded in SCORER via a *Change*: field is not a detectable regression in this round.

[SYNTHESIS OPEN]

All four sections below are required inside this gate. Do not write [SYNTHESIS COMPLETE]
until every section is present. Omitting or merging any section leaves [SYNTHESIS OPEN]
unclosed.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest in Phase 2 only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

Pre-close checklist -- all five must be confirmed before [SYNTHESIS COMPLETE]:
  [ ] LEADERBOARD complete: all N outputs ranked by composite score, descending
  [ ] EXCELLENCE SIGNALS complete: signal named (output + criterion + mechanism), or
      absence explicitly stated
  [ ] FAILURE PATTERNS complete: all-fail criteria identified with diagnosis, or
      absence explicitly stated
  [ ] REGRESSION SIGNALS complete: drawn from Change Manifest; regressions listed
      or absence / no-prior-data explicitly stated
  [ ] VERIFIER role traversed: [VERIFIER COMPLETE] appears above; all evidence cells
      reviewed; verification summary written

[SYNTHESIS COMPLETE]

PHASE 4: PER-OUTPUT NARRATIVE (within ANALYST, after [SYNTHESIS COMPLETE])

This is Mechanism 6. For each scored output, write three prescribed labeled fields.
Each field is always required. A narrative entry missing any labeled field is structurally
incomplete; the absence of a label is detectable by name.

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label; this field is required]
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS; required]
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers; this field is required]

[ANALYST COMPLETE]
```

---

## Variation summary

| Variation | Axes | Key mechanisms | C-03 | C-07 | C-12 | C-17 | C-18 | C-19 | C-20 |
|-----------|------|----------------|------|------|------|------|------|------|------|
| V-01 | Y | Role arch + three-field ANALYST template | PASS | PASS | PARTIAL | PASS | FAIL (0/0) | PASS | PASS |
| V-02 | Z | Inline scaffold, no roles, synthesis gate | PASS | PARTIAL | FAIL | FAIL | FAIL (0/0) | PASS | FAIL |
| V-03 | Y+C12P | Role arch + schema prohibition + three-field | PASS | PASS | PASS | PASS | FAIL (0/0) | PASS | PASS |
| V-04 | Y+R6V05 | Full stack + roles + three-field + 5/5 anchor | PASS | PASS | PASS | PASS | PASS (5/5) | PASS | PASS |
| V-05 | Full R7 | V-04 + Mech 6+7 + FM F+G + 7/7 anchor | PASS | PASS | PASS | PASS | PASS (7/7) | PASS | PASS |

**Diagnostic value of V-01 vs V-02**: V-01 has role separation + three-field narrative; V-02
has inline three-field narrative without role architecture. Both should PASS C-19. The
divergence on C-20 (V-01 PASS, V-02 FAIL) confirms C-19 and C-20 are orthogonal -- narrative
field presence is independent of role architecture.

**Diagnostic value of V-01 vs V-03**: Both role architectures + three-field narrative. V-01
has no schema prohibition; V-03 adds SCORER output schema with explicit prohibition. If V-01
scores C-12 PARTIAL and V-03 scores C-12 PASS, the prohibition is necessary and sufficient.
If both score identically, C-12 is satisfied by gate tokens + role separation alone.

**Diagnostic value of V-04 vs V-05**: Both should PASS C-20, C-19, and all carried criteria.
V-04 has 5 named mechanisms / 5 failure modes; V-05 has 7. If V-04 scores C-18 PASS (5/5 named
mechanisms cover the anchor), the two new structural elements (narrative template, inter-role
gates) are not counted as unnamed mechanisms. If V-04 scores C-18 FAIL, V-05 closes the gap.

**Formula correction**: All five variations use `/13 * 130` for aspirational criteria. R6
variations used `/11 * 110` (v5 formula). A rubric scorer running any R6 variation against v6
should note C-03 FAIL due to formula mismatch. All R7 variations close this gap.
