# quest-score Variations -- Round 6
**Skill**: quest-score
**Rubric**: v5 (N_essential=5, N_recommended=2, N_aspirational=11)
**Date**: 2026-03-15
**Round**: 6

---

## Design logic

### Unachieved ceilings entering R6

R5 V-05 was the full stack against the v4 rubric (N_aspirational=9). Rubric v5 adds
C-17 (evidence specificity gate) and C-18 (exhaustive failure-mode anchor). Against
v5, R5 V-05 scores:

| Criterion | R5 V-05 status | Gap |
|-----------|----------------|-----|
| C-17 | FAIL | Phase 1 carries an inline instruction ("each Evidence cell must pass the specificity test") but no dedicated second-pass VERIFIER phase with gate token. Rubric v5 note: "a general instruction to 'be specific' in the scoring phase does not satisfy this criterion." The inline instruction is in the same phase as scoring -- not a structurally distinct second pass. |
| C-18 | PASS | R5 V-05 has 4 named mechanisms + 4 failure-mode blocks (A through D), one per mechanism. 4 / 4 = exhaustive coverage. |
| C-03 | FAIL (formula) | R5 V-05 composite formula uses `/9 * 90` (v4 weights). v5 requires `/11 * 110`. Wrong denominator and weight produce an incorrect composite score derivation. |

Primary target for R6: C-17 (VERIFIER phase gate). Forced infrastructure update: formula
correction to `/11 * 110`. Design question: does adding VERIFIER as a fifth named mechanism
require a fifth failure-mode block to maintain C-18?

### New axes for R6

| Axis | Label | Mechanism | Target criteria |
|------|-------|-----------|-----------------|
| V | Verification phase gate | A dedicated PHASE 2 (EVIDENCE VERIFICATION) inserted between Phase 1 (Scoring) and Phase 2 (Change Manifest). Gate token `[VERIFIER COMPLETE]` required before any downstream phase begins. Every evidence cell revisited with explicit specificity test: "could this evidence apply to any well-designed output of this type?" Cells that fail require revision before the gate can close. Synthesis is structurally unreachable without traversing this gate. | C-17 directly |
| W | In-block specificity annotation | After the Evidence field in each criterion block, a mandatory `Specificity: PASS | FAIL -- revised: [...]` field is required. No separate verification phase. Tests whether in-block attestation at the scoring site satisfies C-17's "dedicated verification pass" requirement or produces only PARTIAL (same pass, same phase, not a structurally distinct second pass). | C-17 probe |
| X | Role-sequence VERIFIER | SCORER / VERIFIER / ANALYST role architecture (from R5 V-03 Axis U) with formula /11 * 110 and VERIFIER role applying specificity test. No explicit gate tokens between roles -- role-name headings define structural boundaries. Tests whether a named VERIFIER role without inter-role gate tokens satisfies C-17 ("VERIFIER role, verification phase, or equivalent second-pass") or produces only PARTIAL. | C-17 probe via role vs phase |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (V)**: Verification phase gate. Minimal base (scoring + verification phase +
  synthesis). Formula /11 * 110. No *Why* field, no Change tracking, no anchor.
  Predicts: C-17 PASS (dedicated phase with gate token, specificity test, revision
  requirement, synthesis structurally blocked until [VERIFIER COMPLETE]);
  C-11 FAIL (no *Why*); C-09 FAIL (no anchor); C-15 FAIL (no Change field);
  C-16 FAIL (no manifest); C-14 FAIL (no baseline load gate).

- **V-02 (W)**: In-block specificity annotation. Minimal base + mandatory Specificity
  field in every criterion block. Formula /11 * 110. No *Why*, no Change, no anchor,
  no separate verification phase.
  Predicts: C-17 PARTIAL (in-block specificity check is present but operates in the
  same pass as scoring -- rubric requires a structurally distinct second pass);
  C-02 PASS or PARTIAL (in-block specificity may improve evidence quality but the
  Verifier is concurrent with, not downstream of, scoring);
  C-09 FAIL; C-11 FAIL; C-15 FAIL; C-16 FAIL.

- **V-03 (X)**: Role-sequence VERIFIER. SCORER / VERIFIER / ANALYST architecture.
  Formula /11 * 110. No gate tokens between roles, no Change tracking, no anchor.
  Predicts: C-17 PASS (rubric text: "VERIFIER role, verification phase, or equivalent
  second-pass" -- a named VERIFIER role with structural responsibility is a role);
  C-12 PARTIAL (role headings approximate phase separation; conflation is sequentially
  blocked but not structurally impossible without gate tokens);
  C-07 PASS (per-output narrative in ANALYST phase, outside SCORER blocks);
  C-11 PARTIAL (ANALYST synthesis names mechanisms in excellence/failure sections;
  no per-criterion *Why* field in SCORER blocks);
  C-15 FAIL; C-16 FAIL; C-14 FAIL.

### Combination selections (V-04, V-05)

- **V-04 (V + R5-V05 architecture + formula fix)**: R5 V-05 full stack (4-phase
  architecture, *Why* field, *Change* field, Change Manifest, Synthesis gate+checklist,
  4-failure-mode anchor, 4 named mechanisms) PLUS verification phase inserted as Phase 1.5
  PLUS formula /11 * 110. Does NOT declare VERIFIER as Mechanism 5 and does NOT add
  Failure Mode E to anchor. Diagnostic question: does C-18 score the VERIFIER phase as
  an unnamed fifth mechanism (requiring a fifth failure-mode block that is absent) or as
  an unnamed structural element that doesn't increment the mechanism count?
  Predicts: C-17 PASS (verification phase gate present); C-18 PASS (4 explicitly named
  mechanisms + 4 failure-mode blocks; VERIFIER phase undeclared as mechanism); all R5
  criteria carried; composite: 200 or near-200.

- **V-05 (Full stack R6)**: V-04 PLUS Mechanism 5 (VERIFIER phase explicitly declared
  as a named mechanism in the enforcement architecture) PLUS Failure Mode E (VERIFIER
  bypass path) added to the anti-pattern anchor. 5 named mechanisms = 5 failure-mode
  blocks required for C-18. Formula /11 * 110. Ceiling variation.
  Predicts: all C-01 through C-18 PASS; composite 200/200.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Verification phase gate (`[VERIFIER COMPLETE]`) | YES | NO | NO | YES | YES |
| In-block `Specificity:` field per criterion block | NO | YES | NO | NO | NO |
| VERIFIER as named role (SCORER/VERIFIER/ANALYST) | NO | NO | YES | NO | NO |
| Formula `/11 * 110` | YES | YES | YES | YES | YES |
| *Why*: field per criterion block (C-11) | NO | NO | NO | YES | YES |
| Mandatory *Change*: field (C-15) | NO | NO | NO | YES | YES |
| Change Manifest phase (C-16) | NO | NO | NO | YES | YES |
| Anti-pattern anchor (C-09) | NO | NO | NO | YES | YES |
| Failure Mode E: VERIFIER bypass (new) | NO | NO | NO | NO | YES |
| VERIFIER declared as Mechanism 5 (new) | NO | NO | NO | NO | YES |
| Failure-mode blocks / named mechanisms | 0/0 | 0/0 | 0/0 | 4/4 | 5/5 |
| Baseline load gate (C-14) | NO | NO | NO | YES | YES |
| Synthesis gate + pre-close checklist (C-10) | NO | NO | NO | YES | YES |
| Per-output narrative in isolated phase (C-12) | NO | NO | PARTIAL | YES | YES |

---

## V-01 -- Axis V: Dedicated verification phase gate

**Variation axis**: Lifecycle emphasis -- a dedicated PHASE 2 (EVIDENCE VERIFICATION)
is inserted between PHASE 1 (SCORING) and SYNTHESIS. The gate token `[VERIFIER COMPLETE]`
is required before synthesis can begin. Every evidence cell from Phase 1 is revisited
under an explicit specificity test. Cells that fail the test must carry a revised entry.
Synthesis is structurally unreachable until the gate closes. Single axis -- no *Why*
field, no Change tracking, no anti-pattern anchor. Formula corrected to /11 * 110.

**Hypothesis**: A dedicated verification phase with a gate token satisfies C-17 by
making synthesis structurally unreachable without traversing the evidence specificity
check. The phase is distinct from scoring (it runs after [SCORING COMPLETE]), the
specificity test is explicitly stated ("could this evidence apply to any well-designed
output of this type?"), and revision is required before the gate can close. This
distinguishes the phase from the inline instruction in R5 V-05 Phase 1, which ran
concurrently with scoring in the same pass. Predicts: C-17 PASS (dedicated phase,
gate token, explicit test, revision requirement, synthesis blocked); C-11 FAIL (no
*Why*); C-09 FAIL (no anchor); C-15 FAIL (no Change field); C-16 FAIL (no manifest);
C-14 FAIL (no baseline load gate); C-10 FAIL (no synthesis gate). C-03 PASS (formula
/11 * 110 matches v5 rubric).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

PHASE 1: SCORING

For each output, produce a scoring block for every criterion in the rubric:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output only;
             must uniquely identify this output -- not a description that
             could apply to any well-designed output of this type]

  No criterion may be skipped. No evidence field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 11 * 110)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORING COMPLETE]

---

PHASE 2: EVIDENCE VERIFICATION

Do not begin until [SCORING COMPLETE] appears above.

Every evidence entry written in Phase 1 must pass the specificity test before
synthesis can proceed. This phase is a structural prerequisite to synthesis --
the SYNTHESIS section is unreachable until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence entry apply to a different output in
this scoring run, or to any well-designed output of this type?" If yes, the cell
fails specificity and revision is required before this phase can close.

For every output, for every criterion:

  Output: [output identifier] | C-[NN]
  Phase 1 evidence: [copy from Phase 1 scoring block above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- could describe another output or any well-designed output
                       of this type; revision required
  If FAIL:
    Revised evidence: [rewrite with a specific structural property, verbatim
                       quote, or design decision that is absent from or distinct
                       in this output versus the others scored in this run]

After all outputs are verified:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] appears above.

Use Phase 1 verdicts and composite scores. Where Phase 2 revised an evidence cell,
the revised entry is the authoritative record for synthesis narrative purposes.

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
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded (PASS to PARTIAL, PASS to FAIL, or PARTIAL to FAIL):

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-02 -- Axis W: In-block specificity annotation

**Variation axis**: Output format -- every criterion block carries a mandatory
`Specificity:` field immediately after Evidence. The field requires the scorer to
attest, at the scoring site, whether the evidence uniquely identifies this output or
is generic. If generic, a revised entry is required before the block can be considered
complete. No separate verification phase. No gate token. Formula /11 * 110.

**Hypothesis**: The `Specificity:` field embeds evidence verification at the scoring
site rather than in a downstream phase. This closes the generic-evidence path locally --
a scorer who writes generic evidence must immediately revise rather than moving on.
However, this operates concurrently with the scoring pass (same phase, same role) rather
than as a "structurally distinct second pass." The rubric criterion C-17 requires a
VERIFIER role, verification phase, or equivalent second-pass -- the phrase "second-pass"
implies downstream execution after the scoring pass ends. An in-block field is not a
second pass; it is an extended first pass. Predicts: C-17 PARTIAL (specificity check
mechanism exists and forces revision; but it operates in the same pass as scoring, not as
a downstream structural prerequisite); C-02 improved (generic evidence is locally
correctable); C-11 FAIL (no *Why* field); C-09 FAIL; C-15 FAIL; C-16 FAIL.
Useful contrast to V-01: same target (C-17) via different structural path; partial
vs full pass expected to discriminate rubric enforcement from rubric intent.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

SCORING PHASE

For each output, produce a scoring block for every criterion in the rubric:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:     PASS | PARTIAL | FAIL
  Evidence:    [specific quote or structural observation from this output only]
  Specificity: PASS -- uniquely identifies this output; this evidence cannot
                       describe any other output in this run without modification
             | FAIL -- too generic; could describe any well-designed output of
                       this type without modification
               If FAIL, revised evidence is required before this block is complete:
               Revised: [rewrite with a concrete structural property, verbatim
                         phrase, or design decision present or absent uniquely
                         in this output versus the others in this run]

  Rules:
    - No criterion may be skipped.
    - No Evidence or Specificity field may be blank.
    - An Evidence cell that fails Specificity must carry a Revised entry.
    - A block with Specificity: FAIL and no Revised entry is structurally incomplete.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 11 * 110)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

---

SYNTHESIS

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
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [reason]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded (PASS to PARTIAL, PASS to FAIL, or PARTIAL to FAIL):

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-03 -- Axis X: Role-sequence VERIFIER (contrast)

**Variation axis**: Role sequence -- the scoring task is divided into three named roles
that run sequentially: SCORER (verdicts + evidence), VERIFIER (specificity test on all
evidence cells), ANALYST (synthesis + per-output narratives). Role names define structural
boundaries; no gate tokens between roles. Formula /11 * 110. No Change tracking, no
mandatory *Change* field, no anti-pattern anchor.

**Hypothesis**: The rubric text for C-17 says "A VERIFIER role, verification phase, or
equivalent second-pass exists that explicitly states and applies the specificity test."
A named VERIFIER role with explicit structural responsibility for specificity checking
satisfies the "VERIFIER role" clause without requiring a phase-level gate token. The
VERIFIER runs after the SCORER completes all outputs (sequential constraint), applies
the specificity test to every cell, and must reach its own completion marker before
ANALYST begins. This is structurally equivalent to a verification phase in terms of
downstream blocking -- ANALYST cannot receive the work until VERIFIER has signed off.
Predicts: C-17 PASS (named VERIFIER role; explicit specificity test; ANALYST
structurally blocked until [VERIFIER COMPLETE]); C-12 PARTIAL (role-name headings
create structural separation, but no gate token makes narrative/verdict conflation
structurally impossible -- only sequentially blocked); C-07 PASS (PER-OUTPUT NARRATIVE
section in ANALYST phase, outside all SCORER verdict blocks); C-11 PARTIAL (ANALYST
synthesis names mechanisms in excellence signals and failure patterns, but no per-criterion
*Why* field in SCORER blocks); C-15 FAIL (no mandatory Change field); C-16 FAIL (no
manifest); C-14 FAIL (no baseline load gate); C-10 FAIL (no synthesis gate).

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
The Scorer does not produce synthesis sections -- that is the Analyst's role.

For each output:

  Output: [output identifier]
  Role: SCORER

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [quote or structural observation from this output]

  Repeat for every criterion in the rubric. No criterion may be skipped.
  No evidence field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 11 * 110)
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
             | FAIL -- generic; could describe any output of this type; revision
                       required before Analyst may use this cell
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

For each output, write a 2-4 sentence narrative covering:
  - The primary structural differentiator (what this output does that others do not)
  - The primary miss (what structural property it lacks that a higher scorer has)
  - The verdict spread interpretation (why this output scored where it did)

  Output [output identifier]:
  [narrative -- reference at least one structural feature or design property by name;
   do not merely list PASS/FAIL counts]

[ANALYST COMPLETE]
```

---

## V-04 -- Axes V + R5-V05 architecture + formula fix

**Variation axes**: R5 V-05 full-stack architecture (four-phase: Baseline Load, Scoring
with *Why* and *Change* fields, Change Manifest, Synthesis with gate + pre-close
checklist; four-failure-mode anchor; four named mechanisms) PLUS a verification phase
inserted as Phase 1.5 between Phase 1 and Phase 2 PLUS formula corrected to /11 * 110.
The VERIFIER phase is NOT declared as a named mechanism in the Change Tracking section,
and no Failure Mode E is added to the anchor.

**Hypothesis**: The four R5 mechanisms handle C-09 through C-16. Adding the verification
phase (Phase 1.5 with [VERIFIER COMPLETE] gate) handles C-17. The formula correction
handles C-03. C-18 should PASS because the anchor covers 4 failure modes for 4 explicitly
named mechanisms -- the VERIFIER phase is present in the prompt but not declared as a
mechanism, so it does not increment the required failure-mode count. This creates a
diagnostic: if a rubric scorer counts the VERIFIER phase as an unnamed fifth mechanism
and marks C-18 FAIL (4 failure-mode blocks but 5 named mechanisms), V-05 closes that
gap. If C-18 PASS (only mechanisms in the Change Tracking section count), the two
variations will score the same on C-18, and the R6 scorecard should call this out.
Predicts: C-17 PASS; C-18 PASS (4/4 named); C-03 PASS; all R5 criteria carried.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism
explanation, a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

ANTI-PATTERN ANCHOR -- READ BEFORE SCORING

Four structural failure modes are prohibited. Read all four before Phase 0 begins.

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

    [SCORING COMPLETE -- no *Change*: fields written during scoring]

    PHASE 3 SYNTHESIS -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS -- improvement
    V-02 C-13: prior PASS, now PARTIAL -- regression

  Why this fails: Regressions were identified by re-reading the baseline in
  synthesis -- a retrospective lookup after the scoring pass finished. Any verdict
  divergence not recorded inline during scoring is silently lost. The correct form
  records CHANGE at the scoring site; a manifest phase collects all annotations
  before synthesis begins; synthesis reads only the manifest.

FAILURE MODE C -- MECHANISM-FREE SCORING (prevented by Mechanism 3 below)

  Typical output:

    C-10 -- Structural completion gate (A)
    Verdict:  PARTIAL
    Evidence: "Phase gates are present in the prompt."
    [no *Why*: field]

  Why this fails: "Phase gates are present" describes evidence, not mechanism. It
  names compliance, not architecture. A scorer who writes this cannot be distinguished
  from one who merely checked a box. The mandatory *Why*: field closes this: the
  scorer must name what the gate does architecturally -- "phase-level gate detects
  Phase 3 omission; no section-level gate prevents section omission within synthesis"
  -- not just confirm the gate exists.

FAILURE MODE D -- INCOMPLETE SYNTHESIS (prevented by Mechanism 4 below)

  Typical output:

    LEADERBOARD
    | Rank | Output | Composite | Golden? |
    | 1    | V-05   | 165/200   | YES     |
    | 2    | V-04   | 155/200   | YES     |

    EXCELLENCE SIGNALS
    V-05 -- C-09 -- anti-pattern anchor present; C-09 PASS at zero structural cost.

    [output ends -- FAILURE PATTERNS and REGRESSION SIGNALS omitted]

  Why this fails: FAILURE PATTERNS and REGRESSION SIGNALS are absent. No gate token
  marks synthesis as incomplete. A reviewer must read the entire output to notice the
  omission -- there is no structural signal that something is missing. The
  [SYNTHESIS COMPLETE] gate closes this: it cannot be written until all four sections
  are confirmed present via pre-close checklist.

---

CHANGE TRACKING AND ENFORCEMENT ARCHITECTURE

Four structural mechanisms prevent the failure modes above. All are required.

MECHANISM 1 -- Mandatory bidirectional Change field (closes Failure Mode A)

  Every criterion block in Phase 1 carries a *Change*: field.
  Exactly three permissible values:

    *Change*: NO CHANGE                              -- verdict matches prior round
    *Change*: CHANGE from [prior verdict]: [reason]  -- verdict differs
    *Change*: NO PRIOR DATA                          -- no prior round score available

  The field is always required. It is not conditional.
  A criterion block without *Change*: is structurally incomplete.
  Conditional forms ("write here if verdict changes") are not permitted.

MECHANISM 2 -- Change Manifest phase (closes Failure Mode B)

  After all outputs are scored, Phase 2 sweeps every *Change*: CHANGE entry into a
  structured table before SYNTHESIS begins.
  SYNTHESIS draws from this manifest exclusively.
  SYNTHESIS is architecturally prohibited from re-reading the Phase 0 baseline table
  or Phase 1 scoring blocks to derive regression data.
  Any regression not recorded at the scoring site via *Change*: is not a detectable
  regression in this round.

MECHANISM 3 -- Mandatory mechanism field (closes Failure Mode C)

  Every criterion block in Phase 1 carries a *Why*: field after Evidence.
  The field must name the structural mechanism or design property driving the verdict.
  Restating the criterion text does not satisfy *Why*:.
  Describing evidence rather than mechanism does not satisfy *Why*:.
  A criterion block without *Why*: is structurally incomplete.

MECHANISM 4 -- Synthesis completion gate (closes Failure Mode D)

  SYNTHESIS is enclosed between [SYNTHESIS OPEN] and [SYNTHESIS COMPLETE].
  All four synthesis sections are required within the gate.
  A pre-close checklist confirms each section before [SYNTHESIS COMPLETE] can be
  written. [SYNTHESIS COMPLETE] cannot appear before the checklist is complete.

---

PHASE 0: BASELINE LOAD

If prior-round score data is provided, build a baseline table of all prior-round
verdicts before scoring begins:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 |
  |--------|------|------|------|------|------|------|------|------|------|------|
  | Output | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 |
  |--------|------|------|------|------|------|------|------|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

---

PHASE 1: SCORING

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion, write a scoring block:

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
               field forces NO CHANGE entry, making omission syntactically impossible"
    - FAIL:    Name the gap. Example: "no mechanism field -- compliance cannot be
               distinguished from mechanism understanding at the scoring site"
    - PARTIAL: Name what is present and absent. Example: "phase gate detects Phase 3
               omission; pre-close checklist absent -- section omission within
               synthesis undetectable"

  No criterion may be skipped.
  No Evidence, *Why*, or *Change* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 11 * 110)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORING COMPLETE]

---

PHASE 1.5: EVIDENCE VERIFICATION

Do not begin until [SCORING COMPLETE] appears above.

Every evidence entry written in Phase 1 must pass the specificity test before the
Change Manifest phase can begin. This phase is a structural prerequisite -- Phase 2
is unreachable until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence entry apply to a different output in this
scoring run, or to any well-designed output of this type?" If yes, the cell fails
specificity and revision is required.

For every output, for every criterion:

  Output: [output identifier] | C-[NN]
  Phase 1 evidence: [copy from Phase 1 scoring block]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- could describe another output; revision required
  If FAIL:
    Revised evidence: [rewrite with a specific structural property, verbatim quote,
                       or design decision unique to this output in this scoring run]

After all outputs are verified:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

PHASE 2: CHANGE MANIFEST

Do not begin until [VERIFIER COMPLETE] appears above.

Collect every *Change*: field that reads CHANGE from [prior] from Phase 1 into this
manifest. List only entries where a change occurred; NO CHANGE and NO PRIOR DATA
entries are not listed.

  | Output | Criterion | Prior verdict | Current verdict | Reason for change |
  |--------|-----------|---------------|-----------------|-------------------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

---

PHASE 3: SYNTHESIS

Do not begin until [CHANGE MANIFEST COMPLETE] appears above.

PROHIBITION: Do not re-read the Phase 0 baseline table or Phase 1 scoring blocks
to derive regression information. All regression data must come from the Change
Manifest in Phase 2. Any regression not recorded in Phase 1 via a *Change*: field
is not a detectable regression in this round.

[SYNTHESIS OPEN]

All four sections below are required inside this gate. Do not write [SYNTHESIS COMPLETE]
until every section is present. Omitting or merging any section leaves [SYNTHESIS OPEN]
unclosed.

---

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

---

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

---

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

---

REGRESSION SIGNALS

From the Change Manifest in Phase 2 only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

---

Pre-close checklist -- all four must be confirmed before [SYNTHESIS COMPLETE]:
  [ ] LEADERBOARD complete: all N outputs ranked by composite score, descending
  [ ] EXCELLENCE SIGNALS complete: signal named (output + criterion + mechanism), or
      absence explicitly stated
  [ ] FAILURE PATTERNS complete: all-fail criteria identified with diagnosis, or
      absence explicitly stated
  [ ] REGRESSION SIGNALS complete: drawn from Change Manifest; regressions listed
      or absence / no-prior-data explicitly stated

[SYNTHESIS COMPLETE]
```

---

## V-05 -- Full stack R6: V-04 + Mechanism 5 + Failure Mode E

**Variation axes**: V-04 full stack PLUS VERIFIER phase declared as a fifth named
mechanism in the Change Tracking section PLUS Failure Mode E (VERIFIER bypass path)
added to the anti-pattern anchor. 5 named mechanisms = 5 failure-mode blocks required
for C-18 exhaustive coverage. Formula /11 * 110. Ceiling variation.

**Hypothesis**: V-04 achieves C-17 via the verification phase gate but leaves ambiguous
whether the VERIFIER phase is a "named structural mechanism" for C-18 purposes. V-05
eliminates the ambiguity by declaring VERIFIER as Mechanism 5 and adding Failure Mode E
(showing what bypassing the VERIFIER phase looks like). The anchor now has five
failure-mode blocks -- one per named mechanism -- satisfying C-18's exhaustive coverage
requirement unambiguously. All five R5 aspirational criteria remain in force; the two
new criteria (C-17, C-18) are explicitly closed by the VERIFIER phase gate and the
five-block anchor respectively. Predicts: all C-01 through C-18 PASS; composite 200/200.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism
explanation, a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

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
  writing NO CHANGE is required for every matching verdict; the field's absence is
  a structural gap, not a valid empty state.

FAILURE MODE B -- FRESH-LOOKUP PATH (prevented by Mechanism 2 below)

  Typical output:

    [SCORING COMPLETE -- no *Change*: fields written during scoring]

    PHASE 3 SYNTHESIS -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS -- improvement
    V-02 C-13: prior PASS, now PARTIAL -- regression

  Why this fails: Regressions were identified by re-reading the baseline in synthesis
  -- a retrospective lookup after the scoring pass finished. Any verdict divergence
  not recorded inline during scoring is silently lost. The correct form records
  CHANGE at the scoring site; a manifest phase collects all annotations before
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
  scorer must name what the gate does architecturally -- "phase-level gate detects
  Phase 3 omission; no section-level gate prevents section omission within synthesis"
  -- not just confirm the gate exists.

FAILURE MODE D -- INCOMPLETE SYNTHESIS (prevented by Mechanism 4 below)

  Typical output:

    LEADERBOARD
    | Rank | Output | Composite | Golden? |
    | 1    | V-05   | 165/200   | YES     |
    | 2    | V-04   | 155/200   | YES     |

    EXCELLENCE SIGNALS
    V-05 -- C-09 -- anti-pattern anchor present; C-09 PASS at zero structural cost.

    [output ends -- FAILURE PATTERNS and REGRESSION SIGNALS omitted]

  Why this fails: FAILURE PATTERNS and REGRESSION SIGNALS are absent. No gate token
  marks synthesis as incomplete. A reviewer must read the entire output to notice the
  omission. The [SYNTHESIS COMPLETE] gate closes this: it cannot be written until all
  four sections are confirmed present via pre-close checklist.

FAILURE MODE E -- VERIFIER BYPASS PATH (prevented by Mechanism 5 below)

  Typical output:

    PHASE 1: SCORING
    ...
    Evidence: [specific quote from this output]
    [no verification phase; no [VERIFIER COMPLETE] gate]

    PHASE 2: CHANGE MANIFEST
    ...

    [CHANGE MANIFEST COMPLETE]

  Why this fails: Phase 1 carries an instruction to "write specific evidence that
  uniquely identifies this output," but the instruction runs concurrently with scoring
  -- a scorer who writes generic evidence ("phase gate present in the prompt") passes
  the same instruction a scorer who writes specific evidence. No downstream phase
  challenges the evidence cells before synthesis proceeds. The VERIFIER phase closes
  this: every evidence cell is revisited after scoring ends; cells that could describe
  any well-designed output must be revised; synthesis is structurally unreachable until
  [VERIFIER COMPLETE] appears; the gap between a general instruction and a structural
  second pass is the difference between intent and enforcement.

---

CHANGE TRACKING AND ENFORCEMENT ARCHITECTURE

Five structural mechanisms prevent the failure modes above. All are required.

MECHANISM 1 -- Mandatory bidirectional Change field (closes Failure Mode A)

  Every criterion block in Phase 1 carries a *Change*: field.
  Exactly three permissible values:

    *Change*: NO CHANGE                              -- verdict matches prior round
    *Change*: CHANGE from [prior verdict]: [reason]  -- verdict differs
    *Change*: NO PRIOR DATA                          -- no prior round score available

  The field is always required. It is not conditional.
  A criterion block without *Change*: is structurally incomplete.
  Conditional forms ("write here if verdict changes") are not permitted.

MECHANISM 2 -- Change Manifest phase (closes Failure Mode B)

  After all outputs are scored, Phase 2 sweeps every *Change*: CHANGE entry into a
  structured table before SYNTHESIS begins.
  SYNTHESIS draws from this manifest exclusively.
  SYNTHESIS is architecturally prohibited from re-reading the Phase 0 baseline table
  or Phase 1 scoring blocks to derive regression data.
  Any regression not recorded at the scoring site via *Change*: is not a detectable
  regression in this round.

MECHANISM 3 -- Mandatory mechanism field (closes Failure Mode C)

  Every criterion block in Phase 1 carries a *Why*: field after Evidence.
  The field must name the structural mechanism or design property driving the verdict.
  Restating the criterion text does not satisfy *Why*:.
  Describing evidence rather than mechanism does not satisfy *Why*:.
  A criterion block without *Why*: is structurally incomplete.

MECHANISM 4 -- Synthesis completion gate (closes Failure Mode D)

  SYNTHESIS is enclosed between [SYNTHESIS OPEN] and [SYNTHESIS COMPLETE].
  All four synthesis sections are required within the gate.
  A pre-close checklist confirms each section before [SYNTHESIS COMPLETE] can be
  written. [SYNTHESIS COMPLETE] cannot appear before the checklist is complete.

MECHANISM 5 -- Evidence verification phase (closes Failure Mode E)

  After Phase 1 (Scoring) and before Phase 2 (Change Manifest), a dedicated
  verification phase revisits every evidence cell with an explicit specificity test.
  The test: "could this evidence apply to any well-designed output of this type?"
  Cells that fail the test require a revised entry before the gate can close.
  Phase 2 is structurally unreachable until [VERIFIER COMPLETE] appears.
  A general instruction to "write specific evidence" in Phase 1 does not satisfy this
  mechanism -- the enforcement requires a structurally distinct second pass with a
  gate token, not a co-located instruction.

---

PHASE 0: BASELINE LOAD

If prior-round score data is provided, build a baseline table of all prior-round
verdicts before scoring begins:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 |
  |--------|------|------|------|------|------|------|------|------|------|------|
  | Output | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 |
  |--------|------|------|------|------|------|------|------|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

---

PHASE 1: SCORING

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion, write a scoring block:

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
               field forces NO CHANGE entry, making omission syntactically impossible"
    - FAIL:    Name the gap. Example: "no mechanism field -- compliance cannot be
               distinguished from mechanism understanding at the scoring site"
    - PARTIAL: Name what is present and absent. Example: "phase gate detects Phase 3
               omission; pre-close checklist absent -- section omission undetectable"

  No criterion may be skipped.
  No Evidence, *Why*, or *Change* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 11 * 110)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORING COMPLETE]

---

PHASE 1.5: EVIDENCE VERIFICATION

Do not begin until [SCORING COMPLETE] appears above.

This is Mechanism 5. Every evidence entry written in Phase 1 must pass the specificity
test before Phase 2 can begin. This phase is a structural prerequisite -- Phase 2 is
unreachable until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence entry apply to a different output in this
scoring run, or to any well-designed output of this type?" If yes, the cell fails
specificity and revision is required.

For every output, for every criterion:

  Output: [output identifier] | C-[NN]
  Phase 1 evidence: [copy from Phase 1 scoring block]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- could describe another output; revision required
  If FAIL:
    Revised evidence: [rewrite with a specific structural property, verbatim quote,
                       or design decision unique to this output in this scoring run]

After all outputs are verified:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

PHASE 2: CHANGE MANIFEST

Do not begin until [VERIFIER COMPLETE] appears above.

Collect every *Change*: field that reads CHANGE from [prior] from Phase 1 into this
manifest. List only entries where a change occurred; NO CHANGE and NO PRIOR DATA
entries are not listed.

  | Output | Criterion | Prior verdict | Current verdict | Reason for change |
  |--------|-----------|---------------|-----------------|-------------------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

---

PHASE 3: SYNTHESIS

Do not begin until [CHANGE MANIFEST COMPLETE] appears above.

PROHIBITION: Do not re-read the Phase 0 baseline table or Phase 1 scoring blocks
to derive regression information. All regression data must come from the Change
Manifest in Phase 2. Any regression not recorded in Phase 1 via a *Change*: field
is not a detectable regression in this round.

[SYNTHESIS OPEN]

All four sections below are required inside this gate. Do not write [SYNTHESIS COMPLETE]
until every section is present. Omitting or merging any section leaves [SYNTHESIS OPEN]
unclosed.

---

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

---

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

---

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

---

REGRESSION SIGNALS

From the Change Manifest in Phase 2 only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

---

Pre-close checklist -- all five must be confirmed before [SYNTHESIS COMPLETE]:
  [ ] LEADERBOARD complete: all N outputs ranked by composite score, descending
  [ ] EXCELLENCE SIGNALS complete: signal named (output + criterion + mechanism), or
      absence explicitly stated
  [ ] FAILURE PATTERNS complete: all-fail criteria identified with diagnosis, or
      absence explicitly stated
  [ ] REGRESSION SIGNALS complete: drawn from Change Manifest; regressions listed
      or absence / no-prior-data explicitly stated
  [ ] VERIFIER phase traversed: [VERIFIER COMPLETE] appears above; evidence cells
      revised as needed; verification summary written

[SYNTHESIS COMPLETE]
```

---

## Variation summary

| Variation | Axes | Key mechanism | C-17 pred | C-18 pred | C-11 pred | C-10 pred | C-09 pred |
|-----------|------|---------------|-----------|-----------|-----------|-----------|-----------|
| V-01 | V | VERIFIER phase gate; synthesis unreachable until [VERIFIER COMPLETE] | PASS | N/A (no anchor) | FAIL | FAIL | FAIL |
| V-02 | W | In-block Specificity field; same-pass verification; no downstream gate | PARTIAL | N/A (no anchor) | FAIL | FAIL | FAIL |
| V-03 | X | SCORER/VERIFIER/ANALYST roles; role-name boundary; [VERIFIER COMPLETE] gate | PASS | N/A (no anchor) | PARTIAL | FAIL | FAIL |
| V-04 | V + R5-V05 | VERIFIER phase as Phase 1.5 + all R5 mechanisms; 4 failure modes / 4 mechanisms | PASS | PASS | PASS | PASS | PASS |
| V-05 | V + R5-V05 + E | V-04 + Mechanism 5 declared + Failure Mode E; 5 failure modes / 5 mechanisms | PASS | PASS | PASS | PASS | PASS |

**Spread design**: V-01 is the diagnostic isolation for C-17 via phase gate -- confirms
the gate-token mechanism achieves C-17 PASS on a minimal base. V-02 tests the adjacent
failure mode: in-block checking expected to produce PARTIAL on C-17, isolating the
"second-pass" requirement of the rubric. V-03 is the role-sequence contrast: tests
whether role-based enforcement reaches the same C-17 verdict via a different structural
path, and whether it achieves C-12 via role separation without gate tokens. V-01 vs V-02
vs V-03 together should clearly discriminate the "structurally distinct second pass"
requirement. V-04 shows that C-17 composes cleanly with all R5 mechanisms. V-05
closes the C-18 ambiguity introduced by V-04's unnamed fifth mechanism.

**Diagnostic value of V-04 vs V-05**: If both score identically on C-18 (PASS), the
rubric's "named structural mechanism" scope is confirmed as "mechanisms declared in the
enforcement architecture section." If V-04 scores C-18 FAIL (rubric scorer counts the
VERIFIER phase as an unnamed mechanism requiring a failure-mode block), the R6 scorecard
should call this as a rubric clarification opportunity for v6.

**Formula correction**: All five variations use `/11 * 110` for aspirational criteria.
R5 V-05 used `/9 * 90` (v4 formula). A rubric scorer running R5 V-05 against v5 should
note C-03 FAIL due to formula mismatch; all R6 variations close this gap.
