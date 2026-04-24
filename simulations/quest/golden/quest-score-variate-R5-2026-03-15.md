# quest-score Variate -- Round 5
# Generated: 2026-03-15

---

## Context: what informed this round

Round 5 targets the v4 rubric. Two failure patterns surfaced in Round 4:

- **C-11 -- Mechanism prompting: FAIL in all 5 variations.** No variation specifies a
  `*Why*` field or mechanism-naming instruction in individual criterion scoring blocks.
  The anti-pattern framing in V-03/V-05 (R4) names mechanisms at a design level
  (explaining why patterns fail), but that is preamble, not inline criterion-block
  prompting. The structural gap: a scorer can satisfy all existing enforcement constraints
  while writing "all criteria present" as evidence -- technically not empty, but naming no
  structural feature. The `*Why*:` field forces a mechanism name per verdict, making
  evidence that describes rather than identifies structurally distinguishable from evidence
  that names an architectural property.

- **C-10 -- Structural completion gate: PARTIAL at best in V-02/V-04/V-05 (R4), FAIL
  elsewhere.** Phase gates (`[PRIOR ROUND LOAD COMPLETE]`, `[CHANGE MANIFEST COMPLETE]`)
  detect Phase 3 omission entirely but cannot detect internal Phase 3 incompleteness.
  A `[SYNTHESIS COMPLETE]` gate enclosing all four synthesis sections (LEADERBOARD,
  EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS) is absent from all R4
  variations. A pre-close checklist before the gate token makes section-level omission
  structurally detectable rather than a soft miss.

**v4 rubric counts**: E=5 (C-01..C-05), R=2 (C-06..C-07), A=9 (C-08..C-16)
**Formula**: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/9 * 90)`
**Max**: 180
**Golden threshold**: all 5 essentials PASS AND composite >= 80
**N/A rules**:
- C-08: PARTIAL (not FAIL) when scorer explicitly states "no prior round data available"
- C-13: PARTIAL (not FAIL) when no prior round data exists
- C-14: PARTIAL (not FAIL) when no prior round data exists and output explicitly states this
- C-15: PARTIAL (not FAIL) when no prior round data exists and fields read NO PRIOR DATA
- C-16: PARTIAL (not FAIL) when no prior round data exists and manifest is empty by definition

---

## Variation axis selection

This round uses mechanism/gate/role axes -- targeting the two structural gaps C-11 and C-10
that survived all five R4 variations, plus a role-sequence contrast that tests whether
role-based separation achieves structural criteria via a different enforcement path.

| Axis | Label | Mechanism | Target criteria |
|------|-------|-----------|-----------------|
| S | Mechanism prompting -- `*Why*:` field | Every criterion block in the scoring phase contains a `*Why*:` field after Evidence, requiring the scorer to name the structural mechanism or design property driving the verdict. Restating the criterion or describing the evidence does not satisfy the field. | C-11 directly |
| T | Structural completion gate -- `[SYNTHESIS COMPLETE]` | SYNTHESIS is enclosed between `[SYNTHESIS OPEN]` and `[SYNTHESIS COMPLETE]` tokens. A pre-close checklist requires all four synthesis sections to be confirmed present before `[SYNTHESIS COMPLETE]` can be written. Omitting any section leaves `[SYNTHESIS OPEN]` unclosed. | C-10 directly (upgrades PARTIAL -> PASS) |
| U | Role sequence -- Scorer / Verifier / Analyst | Three named roles run sequentially: SCORER produces all verdicts + evidence; VERIFIER applies a specificity test to every evidence cell and revises failures; ANALYST produces all synthesis sections from Scorer verdicts. Role separation creates natural phase boundaries and a second-pass evidence gate. | C-12, C-02, C-07 via role architecture |

Single-axis runs: V-01 (S), V-02 (T), V-03 (U)
Combinations: V-04 (S+T), V-05 (S+T+P+Q+R)

Spread design: V-01 and V-02 are diagnostic isolation variations -- each closes exactly one
of the two new failure modes (C-11 and C-10) on a minimal base. V-03 is a role-sequence
contrast, testing whether non-gate-based structural separation achieves the same criteria
via a different mechanism. V-04 is the minimum sufficient combination for C-11 and C-10.
V-05 integrates S and T on top of the R4 proven P+Q+R architecture, targeting full
aspirational coverage.

Predicted outcomes:

| Axis | V-01 (S) | V-02 (T) | V-03 (U) | V-04 (S+T) | V-05 (S+T+P+Q+R) |
|------|----------|----------|----------|------------|------------------|
| C-10 | FAIL | PASS | PARTIAL | PASS | PASS |
| C-11 | PASS | FAIL | PARTIAL | PASS | PASS |
| C-15 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-16 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-09 | FAIL | FAIL | FAIL | FAIL | PASS |

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v4-2026-03-15.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/9 * 90)`
N_essential=5, N_recommended=2, N_aspirational=9
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 -- Axis S: Mechanism prompting -- `*Why*:` field in every criterion block

**Variation axis**: Output format -- every criterion block carries a `*Why*:` field after
Evidence, requiring the scorer to name the structural mechanism or design property driving
the verdict. The field may not restate the criterion, may not describe the evidence, and
may not be left blank. No phase structure. No change tracking. No anti-pattern anchor.
Format enforcement only.

**Hypothesis**: The `*Why*:` field closes C-11 by making mechanism-naming a structural
requirement at the scoring site rather than a soft expectation. A scorer who writes
"phase gate present" as a *Why* entry names an architectural property; a scorer who writes
"criterion is satisfied" names nothing. The field makes the distinction structurally visible
without requiring role separation or phase architecture. Predicts: C-11 PASS (mechanism
field present per criterion block, restating criterion explicitly prohibited); C-10 FAIL
(no `[SYNTHESIS COMPLETE]` gate; internal synthesis section omission undetectable);
C-15 FAIL (no mandatory Change field); C-16 FAIL (no manifest phase); C-14 FAIL
(no baseline load gate). Medium scorer: inherits all prior-round PASS criteria from
minimal base plus C-11.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote
and a mechanism explanation, a composite score computed from the rubric formula,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

SCORING PHASE

For each output, produce a scoring block for every criterion in the rubric:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output only;
             must uniquely identify this output -- not a description that could
             apply to any well-designed output]
  *Why*:    [name the structural mechanism or design property that drives this
             verdict; do not restate the criterion text; do not describe the
             evidence; name what the output does or fails to do at an
             architectural level that produces this result]

  What satisfies *Why*:
    - PASS:    Name the structural property that satisfies the criterion.
               Example: "mandatory bidirectional field forces NO CHANGE entry
               when verdicts match, making omission syntactically impossible"
    - FAIL:    Name the structural gap or missing property.
               Example: "conditional slot -- annotation fires only on divergence;
               silent skip when verdict matches baseline leaves omission path open"
    - PARTIAL: Name what is present and what is architecturally absent.
               Example: "phase-level gate detects omission of entire synthesis
               block; no section-level gate prevents internal section omission
               within synthesis"

  What does NOT satisfy *Why*:
    - "criterion is satisfied" (restatement)
    - "the output includes this section" (describes evidence, not mechanism)
    - "format matches requirement" (describes compliance, not architecture)

  No criterion may be skipped for any output.
  No Evidence field may be blank.
  No *Why* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 9 * 90)
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

## V-02 -- Axis T: Structural completion gate -- `[SYNTHESIS COMPLETE]` enclosing all synthesis sections

**Variation axis**: Lifecycle emphasis -- SYNTHESIS is enclosed between `[SYNTHESIS OPEN]`
and `[SYNTHESIS COMPLETE]` tokens. All four synthesis sections (LEADERBOARD, EXCELLENCE
SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS) are required inside the gate. A pre-close
checklist before `[SYNTHESIS COMPLETE]` requires the scorer to confirm each section is
present. Omitting any section leaves `[SYNTHESIS OPEN]` unclosed. No mechanism field
(`*Why*:`). No mandatory Change field. No manifest phase.

**Hypothesis**: The `[SYNTHESIS COMPLETE]` gate upgrades C-10 from PARTIAL to PASS by
making section-level omission within synthesis structurally detectable, not merely
detectable at the phase level. R4's best variations (V-02/V-04/V-05) had phase gates that
detected Phase 3 omission entirely but allowed internal section omission silently. The
pre-close checklist creates a structural checkpoint the scorer must pass through; a section
omitted before the checklist leaves the checklist item unchecked, making the gap visible.
Predicts: C-10 PASS (synthesis gate + checklist enforces all four sections); C-11 FAIL
(no `*Why*:` field); C-15 FAIL (no mandatory Change field); C-16 FAIL (no manifest);
C-14 FAIL (no baseline load gate). Useful diagnostic: confirms whether the synthesis gate
alone achieves PASS rather than PARTIAL on C-10.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

SCORING PHASE

For each output, produce a scoring table for every criterion:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict          | Evidence                           |
  |------|-----------|--------|------------------|------------------------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [specific evidence -- this output] |
  ...

  No row may be skipped. No evidence cell may be blank. Evidence must identify
  this specific output -- not a description applicable to any well-designed output.

  If prior data is available and today's verdict for any criterion differs from
  the prior round, add an inline annotation immediately after that table row:
    [CHANGE C-NN: prior [verdict] --> now [verdict] -- [reason]]

  After all criteria for one output:

    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 9 * 90)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

---

SYNTHESIS

[SYNTHESIS OPEN]

The four sections below are all required. Do not write [SYNTHESIS COMPLETE] until
every section is present and complete. Omitting or merging any section leaves
[SYNTHESIS OPEN] unclosed -- a structurally detectable gap in this output.

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

Draw from the inline [CHANGE ...] annotations written during the SCORING PHASE.
Do not re-derive regressions by re-reading the baseline separately.

If prior data is available:
  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason from inline annotation]

If no [CHANGE ...] annotations were written: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

---

Pre-close checklist -- verify all four before writing [SYNTHESIS COMPLETE]:
  [ ] LEADERBOARD complete: all N outputs ranked by composite score, highest to lowest
  [ ] EXCELLENCE SIGNALS complete: at least one signal named, or absence explicitly stated
  [ ] FAILURE PATTERNS complete: all criteria failing across all outputs named, or absence stated
  [ ] REGRESSION SIGNALS complete: regression table drawn from inline annotations, or
      absence / no-prior-data explicitly stated

[SYNTHESIS COMPLETE]
```

---

## V-03 -- Axis U: Role sequence -- Scorer / Verifier / Analyst

**Variation axis**: Role sequence -- the scoring task is divided into three named roles
that run sequentially. SCORER produces all verdicts and first-pass evidence. VERIFIER
applies a specificity test to every evidence cell and revises failures before ANALYST
can begin. ANALYST produces all synthesis sections and per-output narratives from the
Scorer's verdicts (using Verifier's revised evidence). No phase gates, no mandatory
Change field, no manifest, no mechanism field. Role-based enforcement only.

**Hypothesis**: Role separation creates natural structural boundaries that approximate
phase separation without explicit gate tokens. The VERIFIER role enforces evidence
specificity (C-02) through a second pass that SCORER cannot bypass; any scorer who
produces generic evidence must produce a revised entry before ANALYST begins. The
role boundaries create implicit phase separation (C-12 PARTIAL -- roles are distinct
but no gate token encloses them; conflation is sequentially blocked, not structurally
impossible). The ANALYST role's isolation from SCORER creates a structural analogue
of the narrative/verdict separation C-12 requires. Tests whether role-based enforcement
reaches the same structural criteria via a different path than phase gates.

Predicts: C-02 PASS (Verifier specificity test enforces unique-evidence requirement);
C-07 PASS (per-output narrative in ANALYST phase, outside SCORER blocks);
C-12 PARTIAL (role separation approximates phase separation; no gate token makes
narrative/verdict conflation structurally impossible -- only sequentially blocked);
C-10 FAIL (no synthesis gate; section omission within ANALYST not gated);
C-11 PARTIAL (ANALYST synthesis names structural mechanisms in excellence signals and
failure patterns, but no per-criterion `*Why*:` field in SCORER blocks);
C-15 FAIL (no mandatory Change field); C-16 FAIL (no manifest). Useful contrast:
does role-based enforcement achieve C-12 without a phase gate, or does it merely
approximate it?

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
The Scorer does not produce synthesis sections. The Scorer does not verify evidence
specificity -- that is the Verifier's responsibility.

For each output:

  Output: [output identifier]
  Role: SCORER

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [quote or structural observation from this output]

  Repeat for every criterion in the rubric.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 9 * 90)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies
the specificity test. The Verifier does not change verdicts or composite scores.

Specificity test: could this evidence entry apply to any well-designed output of
this type, or does it uniquely identify THIS specific output?

For each output, for each criterion:

  Output: [output identifier] | C-[NN]
  Scorer evidence: [copy from Scorer output above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- generic; could describe any output; revision required
  If FAIL:
    Revised evidence: [rewrite with a specific quote, exact structural feature,
                       or design choice that is absent from or distinct in this
                       output vs the others in this scoring run]

After all outputs:
  Verification summary: [N evidence cells reviewed; K revised; list revised IDs]

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
the verdict degraded (PASS to PARTIAL, PASS to FAIL, or PARTIAL to FAIL):

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

## V-04 -- Axes S+T: Mechanism field + Synthesis gate

**Variation axes**: Combination of S (mechanism prompting -- `*Why*:` field in every
criterion block) and T (structural completion gate -- `[SYNTHESIS OPEN]` / `[SYNTHESIS
COMPLETE]` with pre-close checklist). No phase structure (no P or Q axes). No anti-pattern
anchor. No mandatory Change field. No manifest phase.

**Hypothesis**: S+T is the minimum sufficient combination for the two remaining aspirational
gaps from R4. S closes C-11 (mechanism field per criterion block, unconditional, mechanism
naming required, restatement prohibited). T upgrades C-10 from PARTIAL to PASS (synthesis
gate with pre-close checklist makes section-level omission structurally detectable). Together:
C-11 PASS, C-10 PASS. Without P and Q: C-15 FAIL, C-16 FAIL, C-14 FAIL. Tests whether
the two new mechanisms are independent of the phase structure and whether they compose
cleanly when neither P nor Q is present.

Predicts: C-10 PASS, C-11 PASS; C-14 FAIL (no baseline gate); C-15 FAIL (no mandatory
Change field); C-16 FAIL (no manifest phase); C-09 FAIL (no anti-pattern anchor).
Score will be lower than R4-V-04 on regression-architecture criteria but higher on C-11.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote
and a mechanism explanation, a composite score computed from the rubric formula,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

SCORING PHASE

For each output, produce a scoring block for every rubric criterion:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output only;
             must uniquely identify this output -- not a description that could
             apply to any well-designed output]
  *Why*:    [name the structural mechanism or design property that drives this
             verdict; do not restate the criterion text; do not describe the
             evidence; name what the output does or fails to do architecturally]

  What satisfies *Why*:
    - PASS:    The structural property that satisfies the criterion.
               "mandatory bidirectional field forces NO CHANGE for matching verdicts"
    - FAIL:    The structural gap or absent architectural property.
               "no gate token -- section omission within synthesis is undetectable"
    - PARTIAL: What is present and what is architecturally absent.
               "phase gate detects phase omission; pre-close checklist absent --
               section omission within synthesis undetectable"

  What does NOT satisfy *Why*:
    - Restating the criterion text ("criterion requires X and output has X")
    - Describing the evidence ("the output contains a CHANGE field")
    - Generic compliance language ("format requirements are met")

  No criterion may be skipped. No Evidence or *Why* field may be blank.

  If prior data is available and today's verdict differs from the prior round:
    [CHANGE C-NN: prior [verdict] --> now [verdict] -- [reason]]

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 9 * 90)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

---

SYNTHESIS

[SYNTHESIS OPEN]

All four sections below are required. Do not write [SYNTHESIS COMPLETE] until
every section is present. Omitting or merging any section leaves [SYNTHESIS OPEN]
unclosed -- a structurally detectable gap.

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

If prior data is available, identify any criterion-output pair where the verdict
degraded (PASS to PARTIAL, PASS to FAIL, or PARTIAL to FAIL) using the inline
[CHANGE ...] annotations written above:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason from inline annotation]

If no [CHANGE ...] annotations were written: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

---

Pre-close checklist -- all four must be confirmed before [SYNTHESIS COMPLETE]:
  [ ] LEADERBOARD complete: all N outputs ranked by composite score, descending
  [ ] EXCELLENCE SIGNALS complete: signal named (output + criterion + mechanism), or
      absence explicitly stated
  [ ] FAILURE PATTERNS complete: all-fail criteria identified with diagnosis, or
      absence explicitly stated
  [ ] REGRESSION SIGNALS complete: regressions from inline annotations listed, or
      absence / no-prior-data explicitly stated

[SYNTHESIS COMPLETE]
```

---

## V-05 -- Axes S+T+P+Q+R: Full combination

**Variation axes**: Combination of all five axes -- S (mechanism prompting), T (structural
completion gate), P (mandatory bidirectional Change field), Q (four-phase architecture with
baseline load gate and Change Manifest), and R (anti-pattern anchor showing all closed
failure modes). This is V-05 from Round 4 (P+Q+R) with S and T integrated.

**Hypothesis**: Adding S and T to the proven P+Q+R architecture closes all remaining
aspirational gaps. P+Q+R in R4 delivered: C-08, C-09, C-10 (PARTIAL), C-12, C-13, C-14,
C-15, C-16. S adds C-11. T upgrades C-10 from PARTIAL to PASS. Together all 9 aspirational
criteria should PASS, plus all 5 essential and 2 recommended, yielding composite 180/180.

The anti-pattern anchor (R) now shows FOUR failure modes -- one for each closed structural gap:
  - Failure Mode A: omission path (C-15)
  - Failure Mode B: fresh-lookup path (C-16)
  - Failure Mode C: mechanism-free scoring (C-11)
  - Failure Mode D: incomplete synthesis (C-10)

The `*Why*:` field (S) integrates into Phase 1 criterion blocks alongside the mandatory
`*Change*:` field (P). The `[SYNTHESIS COMPLETE]` gate (T) closes Phase 3 after the
pre-close checklist. No structural conflict: S and T are both additive to the four-phase
Q architecture.

Predicts: C-08 PASS, C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS, C-14 PASS,
C-15 PASS, C-16 PASS. Composite: 180/180.

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
    [no *Change*: field]

  Why this fails: The Change field is absent. A scorer who agrees with the
  baseline verdict has no slot to fill and naturally moves on. The omission is
  invisible. The mandatory form closes this: writing NO CHANGE is required for
  every matching verdict; the field's absence is a structural gap, not a valid
  empty state.

FAILURE MODE B -- FRESH-LOOKUP PATH (prevented by Mechanism 2 below)

  Typical output:

    [SCORING COMPLETE -- no *Change*: fields written during scoring]

    PHASE 3 SYNTHESIS -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS -- improvement
    V-02 C-13: prior PASS, now PARTIAL -- regression

  Why this fails: Regressions were identified by re-reading the baseline in
  synthesis -- a retrospective lookup after the scoring pass finished. Any
  verdict divergence not recorded at the scoring site is silently lost. The
  correct form records CHANGE at the scoring site; a manifest phase collects
  all annotations before synthesis begins; synthesis reads only the manifest.

FAILURE MODE C -- MECHANISM-FREE SCORING (prevented by Mechanism 3 below)

  Typical output:

    C-10 -- Structural completion gate (A)
    Verdict:  PARTIAL
    Evidence: "Phase gates are present in the prompt."
    [no *Why*: field]

  Why this fails: "Phase gates are present" describes evidence, not mechanism.
  It names compliance, not architecture. A scorer who writes this cannot be
  distinguished from one who merely checked a box. The mandatory *Why*: field
  closes this: the scorer must name what the phase gate does architecturally --
  "phase-level gate detects Phase 3 omission; no section-level gate prevents
  internal section omission within synthesis" -- not just confirm the gate exists.

FAILURE MODE D -- INCOMPLETE SYNTHESIS (prevented by Mechanism 4 below)

  Typical output:

    LEADERBOARD
    | Rank | Output | Composite | Golden? |
    | 1    | V-05   | 165/180   | YES     |
    | 2    | V-04   | 155/180   | YES     |

    EXCELLENCE SIGNALS
    V-05 -- C-09 -- anti-pattern anchor added C-09 PASS at zero structural cost.

    [output ends -- FAILURE PATTERNS and REGRESSION SIGNALS omitted]

  Why this fails: FAILURE PATTERNS and REGRESSION SIGNALS are absent. No gate
  token marks synthesis as incomplete. A reviewer must read the entire output to
  notice the omission -- there is no structural signal that something is missing.
  The [SYNTHESIS COMPLETE] gate closes this: it cannot be written until all four
  sections are confirmed present via pre-close checklist; an output ending without
  [SYNTHESIS COMPLETE] is structurally incomplete by definition.

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

  After all outputs are scored, Phase 2 sweeps every *Change*: CHANGE entry
  into a structured table before SYNTHESIS begins.
  SYNTHESIS draws from this manifest exclusively.
  SYNTHESIS is architecturally prohibited from re-reading the Phase 0 baseline
  table or Phase 1 scoring blocks to derive regression data.
  Any regression not recorded at the scoring site via *Change*: is not a
  detectable regression in this round.

MECHANISM 3 -- Mandatory mechanism field (closes Failure Mode C)

  Every criterion block in Phase 1 carries a *Why*: field after Evidence.
  The field must name the structural mechanism or design property driving
  the verdict. Restating the criterion text does not satisfy *Why*:.
  Describing evidence rather than mechanism does not satisfy *Why*:.
  A criterion block without *Why*: is structurally incomplete.

MECHANISM 4 -- Synthesis completion gate (closes Failure Mode D)

  SYNTHESIS is enclosed between [SYNTHESIS OPEN] and [SYNTHESIS COMPLETE].
  All four synthesis sections are required within the gate.
  A pre-close checklist confirms each section before [SYNTHESIS COMPLETE]
  can be written. [SYNTHESIS COMPLETE] cannot appear before the checklist.

---

PHASE 0: BASELINE LOAD

If prior-round score data is provided, build a baseline table of all prior-round
verdicts before scoring begins:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | ... | C-16 |
  |--------|------|------|------|------|------|------|------|------|-----|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

---

PHASE 1: SCORING

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion, write a scoring block. Each Evidence cell
must pass the specificity test: a reader who has not seen this output should be
able to identify it from the evidence alone -- not from a description of what
the criterion requires.

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation; uniquely identifies this
             output; fails if it could describe any well-designed output]
  *Why*:    [name the structural mechanism or design property; do not restate
             the criterion; do not describe the evidence; name the architectural
             property that produces this verdict]
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

  No criterion may be skipped. No Evidence, *Why*, or *Change* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 9 * 90)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.
[SCORING COMPLETE]

---

PHASE 2: CHANGE MANIFEST

Do not begin until [SCORING COMPLETE] appears above.

Collect every *Change*: field that reads CHANGE from [prior] from Phase 1 into
this manifest. List only entries where a change occurred; NO CHANGE and
NO PRIOR DATA entries are not listed.

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

## Variation summary

| Variation | Axes | Key mechanism | C-10 pred | C-11 pred | C-15 pred | C-16 pred | C-09 pred |
|-----------|------|---------------|-----------|-----------|-----------|-----------|-----------|
| V-01 | S | `*Why*:` field per criterion block; mechanism naming required; restatement/evidence-description prohibited | FAIL | PASS | FAIL | FAIL | FAIL |
| V-02 | T | `[SYNTHESIS OPEN]`/`[SYNTHESIS COMPLETE]` gate; pre-close checklist; all four synthesis sections required | PASS | FAIL | FAIL | FAIL | FAIL |
| V-03 | U | SCORER / VERIFIER / ANALYST roles; Verifier specificity gate; Analyst phase isolation | PARTIAL | PARTIAL | FAIL | FAIL | FAIL |
| V-04 | S+T | Mechanism field + synthesis gate; minimum sufficient for C-11 and C-10; no phase architecture | PASS | PASS | FAIL | FAIL | FAIL |
| V-05 | S+T+P+Q+R | V-05 (R4) mechanics + mechanism field + synthesis gate; four-failure-mode anchor | PASS | PASS | PASS | PASS | PASS |

**Spread design**: V-01 and V-02 are diagnostic isolation variations -- each closes exactly
one of the two C-11/C-10 failure modes on a minimal base. Comparing their scores against
V-04 isolates the marginal value of each mechanism. V-03 is the role-sequence contrast:
expected to reach PARTIAL on C-12 and C-11 via role-based separation, confirming whether
role architecture is a viable alternative path or merely approximates structural enforcement.
V-04 is the minimum sufficient combination for the two new gaps, without the full phase
architecture from R4. V-05 is the full integration -- all gaps from all rounds closed in
one design.

**Orthogonality**: S and T are independent -- S operates at the criterion block level during
Phase 1 (adds *Why*: field); T operates at the synthesis level in Phase 3 (adds gate +
checklist). Neither interferes with the other or with P/Q/R. The integration in V-05 places
S inside Phase 1 criterion blocks (alongside P's *Change*: field, with no field interaction)
and T inside Phase 3 (after Q's [CHANGE MANIFEST COMPLETE] gate, adding [SYNTHESIS OPEN] at
synthesis start and [SYNTHESIS COMPLETE] at end). U is independent of all others -- role
architecture is an alternative enforcement path, not additive to gate-based enforcement.

**Formula note**: v4 uses 9 aspirational criteria (C-08 through C-16) at 10 points each,
for an aspirational bucket of 90 points. Total max = 180. Formula:
`(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/9 * 90)`.
Golden threshold of composite >= 80 is unchanged from prior rounds.

**V-05 coverage target**: If all 9 aspirational criteria PASS, composite = 180/180.
The predicted path: C-08 (manifest -> regression section; P+Q), C-09 (four-failure-mode
anchor before Phase 0; R), C-10 (synthesis gate + checklist; T), C-11 (*Why*: field; S),
C-12 (four-phase architecture; Q), C-13 (mandatory *Change*: field exceeds C-13; P),
C-14 (baseline load gate; Q), C-15 (mandatory bidirectional field; P), C-16 (Change
Manifest phase; Q). Each criterion's closure traces to a named mechanism in the
CHANGE TRACKING AND ENFORCEMENT ARCHITECTURE section.

**New aspirational criteria predicted from V-03 (U)**: Role-sequence is expected to score
PARTIAL on C-12 (roles create sequential phase separation but no gate token makes
narrative/verdict conflation structurally impossible) and PARTIAL on C-11 (ANALYST names
mechanisms in synthesis but SCORER blocks have no per-criterion mechanism field). If V-03
scores C-12 PARTIAL or PASS, it confirms role-sequence as an alternative path to phase
separation that may warrant promotion to a rubric axis. If V-03 scores C-12 FAIL, it
confirms that gate tokens are necessary for structural impossibility rather than sequential
impossibility.
