# quest-score Variate -- Round 4
# Generated: 2026-03-15

---

## Context: what informed this round

Round 4 targets the v4 rubric. Two excellence signals from Round 3 were promoted to
aspirational criteria:

- **C-15 -- Mandatory bidirectional Change field**: the inline CHANGE annotation is always
  required, not conditional. Every criterion block carries the field with exactly two
  permissible values: `NO CHANGE` or `CHANGE from [prior]: [reason]`. Silent omission is
  syntactically visible. Source: R3-V-02 (Axis H) introduced the mandatory form and passed
  C-15. R3-V-03 (Axis I) used a conditional form ("write here if verdict changes") and
  failed C-15 even though it had a manifest structure.

- **C-16 -- Change Manifest phase**: all inline CHANGE annotations are swept into a dedicated
  structured table before SYNTHESIS begins; SYNTHESIS draws exclusively from this manifest; an
  explicit architectural prohibition prevents SYNTHESIS from re-reading the baseline table.
  Source: R3-V-03 (Axis I) introduced the manifest sweep and passed C-16. R3-V-02 (Axis H)
  passed C-13 and C-15 but had no manifest; its SYNTHESIS re-derives regressions from the
  baseline directly.

**C-13/C-15/C-16 independence reminder**:
- C-13: CHANGE slot exists at scoring site (conditional form acceptable)
- C-15: tightens C-13 -- slot is always present; NO CHANGE is mandatory, not implied
- C-16: tightens C-13 -- a manifest phase collects all slots before SYNTHESIS; SYNTHESIS is
  explicitly prohibited from re-reading the baseline

A prompt can pass C-13 while failing both. R3-V-02 passes C-13 + C-15 but not C-16 (no
manifest). R3-V-03 passes C-13 + C-16 but not C-15 (conditional field). V-04 closes all three.

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

This round uses format/lifecycle/inertia axes -- an orthogonal family to the role-sequence
axes used in the R4 role-based session. Role-based designs (Judge/Analyst/Verifier) enforce
correctness via *who* checks. Format/lifecycle/inertia designs enforce correctness via *how
the output is structured* and *what the scorer is shown before starting*. Both families can
satisfy C-15 and C-16; this session tests whether structural slots and phase gates achieve
the same result without role separation.

| Axis | Label | Mechanism | Target criteria |
|------|-------|-----------|-----------------|
| P | Output format -- Mandatory bidirectional Change field | Every criterion block in the scoring phase contains a `*Change*:` field with exactly two permissible values: `NO CHANGE` or `CHANGE from [prior]: [reason]`. The field is unconditional -- required even when the verdict is unchanged. A scoring block without the field is structurally incomplete. | C-15 directly |
| Q | Lifecycle emphasis -- Change Manifest phase | After all outputs are scored, a dedicated CHANGE MANIFEST phase (Phase 2) sweeps every `*Change*:` CHANGE entry into a structured table. A `[CHANGE MANIFEST COMPLETE]` gate precedes SYNTHESIS. SYNTHESIS is explicitly prohibited from re-reading the baseline or scoring blocks; it draws from the manifest exclusively. | C-16 directly |
| R | Inertia framing -- Anti-pattern anchor for omission + fresh-lookup paths | Before any scoring instructions, two labeled failure modes are shown: Pattern A (omission -- no Change field, silent skip) and Pattern B (fresh-lookup -- SYNTHESIS re-derives regressions from the baseline). The scorer is instructed: do not produce output resembling either pattern. No structural enforcement; pure framing. | C-09 directly; contextualizes C-15/C-16 |

Single-axis runs: V-01 (P), V-02 (Q), V-03 (R)
Combinations: V-04 (P+Q), V-05 (P+Q+R)

Spread design: V-01 and V-02 are diagnostic isolation variations -- each closes exactly one
of the two new failure modes. V-03 is the framing-only contrast, expected to score well on
C-09 but miss C-15/C-16. V-04 is the minimum sufficient combination. V-05 adds the framing
anchor on top to test whether C-09 framing improves evidence quality inside the structural
design.

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v4-2026-03-15.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/9 * 90)`
N_essential=5, N_recommended=2, N_aspirational=9
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 -- Axis P: Output format -- Mandatory bidirectional Change field

**Variation axis**: Output format -- every criterion block carries a `*Change*:` field
unconditionally. Exactly two permissible values: `NO CHANGE` or `CHANGE from [prior]: [reason]`.
No role separation. No manifest phase. Format enforcement only.

**Hypothesis**: The mandatory bidirectional field closes the omission path that a conditional
CHANGE slot leaves open. A scorer who matches baseline must write `NO CHANGE` -- they cannot
silently skip the field. A divergence is forced into the record at the scoring site. Predicts:
C-15 PASS (mandatory field present for every criterion block, unconditional); C-16 FAIL (no
manifest phase, no prohibition on SYNTHESIS re-reading baseline -- SYNTHESIS may consume the
Change fields, but there is no dedicated collection phase or gate); C-09 FAIL (no anti-pattern
anchor). Medium-high scoring variation: passes all prior aspirational criteria from R3, plus
C-15.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

CHANGE TRACKING REQUIREMENT

Every criterion block in the SCORING PHASE must contain a *Change*: field.

The field has exactly two permissible values:

  *Change*: NO CHANGE
  *Change*: CHANGE from [prior verdict]: [one sentence -- what changed and why]

Rules:
  - The *Change*: field is always required. It is not conditional. A criterion
    block without *Change*: is structurally incomplete.
  - Write NO CHANGE when today's verdict matches the prior-round verdict for this
    criterion and output.
  - Write CHANGE from [prior] when today's verdict differs.
  - If no prior-round data is available, write: *Change*: NO PRIOR DATA.
  - Do not omit the field even when no change occurred.

---

SCORING PHASE

For each output, produce a per-criterion scoring block:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output only;
             must uniquely identify this output -- not a description that could
             apply to any well-designed output]
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA

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

Draw from the *Change*: fields written in the SCORING PHASE above. List every
criterion block where *Change*: reads CHANGE from [prior], organized by output:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason from Change field]

If no *Change*: fields indicate a change: "No regressions detected this round."
If no prior round data: "No prior round data; regression analysis not possible."
```

---

## V-02 -- Axis Q: Lifecycle emphasis -- Change Manifest phase

**Variation axis**: Lifecycle emphasis -- adds a dedicated CHANGE MANIFEST phase (Phase 2)
between SCORING and SYNTHESIS, with a `[CHANGE MANIFEST COMPLETE]` gate. SYNTHESIS draws from
the manifest exclusively. An explicit prohibition prevents SYNTHESIS from re-reading the
baseline or scoring blocks. The Change field in scoring is conditional (not mandatory), so
C-15 is not targeted -- only C-16.

**Hypothesis**: The manifest phase closes the fresh-lookup path that C-13 alone leaves open.
By collecting all CHANGE entries before SYNTHESIS begins, SYNTHESIS cannot re-derive
regressions from the baseline -- the manifest is the only data source. Predicts: C-16 PASS
(dedicated manifest phase, gate token, explicit prohibition present); C-15 FAIL (Change field
is conditional -- a scorer who agrees with the baseline can silently omit the field; mandatory
bidirectional form is not required); C-09 FAIL (no anti-pattern anchor). Medium-high scoring:
passes prior aspirational criteria from R3, plus C-16.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score, and a golden-threshold determination. The scorecard includes
a ranked leaderboard, excellence signals, failure patterns, and regression signals.

---

PHASE STRUCTURE

Four phases complete this task in strict sequence:

  Phase 0 -- BASELINE LOAD     Confirm prior-round data; build baseline table.
  Phase 1 -- SCORING           Score all N outputs per criterion.
  Phase 2 -- CHANGE MANIFEST   Collect all inline regression annotations.
  Phase 3 -- SYNTHESIS         Leaderboard, signals, patterns, regressions.

Gate rules:
  - Do not begin Phase 1 until [PRIOR ROUND LOAD COMPLETE] appears.
  - Do not begin Phase 2 until [SCORING COMPLETE] appears.
  - Do not begin Phase 3 until [CHANGE MANIFEST COMPLETE] appears.
  - Phase 3 SYNTHESIS may not re-read the Phase 0 baseline table or Phase 1
    scoring blocks to derive regression data. The Change Manifest is the
    exclusive source for regression signals.

---

PHASE 0: BASELINE LOAD

If prior-round score data is provided, build a baseline table of all prior-round
verdicts before scoring begins:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | ... | C-16 |
  |--------|------|------|------|------|------|------|------|------|-----|------|

If no prior-round data is available: write "No prior data available."

[PRIOR ROUND LOAD COMPLETE]

---

PHASE 1: SCORING

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, produce a scoring table:

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict          | Evidence                           |
  |------|-----------|--------|------------------|------------------------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [specific evidence -- this output] |
  ...

  No row may be skipped. No evidence cell may be blank. Evidence must identify
  this specific output -- not a description that applies to any output.

  If prior data exists and today's verdict for a criterion differs from the
  baseline, add an inline annotation immediately after that table row:

    [CHANGE C-NN: prior [verdict] --> now [verdict] -- [reason]]

  Compute composite:
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
[SCORING COMPLETE]

---

PHASE 2: CHANGE MANIFEST

Do not begin until [SCORING COMPLETE] appears above.

Sweep every [CHANGE ...] annotation written in Phase 1 into this manifest table.
List only entries where a change occurred; unchanged criteria are not listed.

  | Output | Criterion | Prior verdict | Current verdict | Reason           |
  |--------|-----------|---------------|-----------------|------------------|
  | [id]   | C-[NN]    | [prior]       | [current]       | [from annotation]|

If no [CHANGE ...] annotations were written in Phase 1:
  "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

---

PHASE 3: SYNTHESIS

Do not begin until [CHANGE MANIFEST COMPLETE] appears above.

PROHIBITION: Do not re-read the Phase 0 baseline table or Phase 1 scoring blocks
to derive regression data. All regression information must come from the Change
Manifest in Phase 2.

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

From the Change Manifest (Phase 2) only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If the manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-03 -- Axis R: Inertia framing -- Anti-pattern anchor for omission and fresh-lookup paths

**Variation axis**: Inertia framing -- before any scoring instructions, two labeled failure
modes are shown as explicit "do not do this" examples. Pattern A demonstrates the omission
path (C-15 failure mode): no Change field, silent skip when verdict matches. Pattern B
demonstrates the fresh-lookup path (C-16 failure mode): SYNTHESIS re-derives regressions from
the baseline instead of from inline annotations. No structural enforcement -- framing only.

**Hypothesis**: Showing the failure modes before instructions primes the scorer to recognize
and avoid them, improving evidence specificity (C-09) and creating diagnostic depth in
synthesis. Predicts: C-09 PASS (anti-pattern anchor precedes scoring instructions, references
essential criteria, demonstrates specific failure modes); C-15 FAIL (no mandatory Change field;
framing may help but cannot close the structural omission path); C-16 FAIL (no manifest phase
or gate; framing cannot enforce architectural separation). Low-medium scoring contrast
variation: framing raises the quality floor but cannot substitute for structural enforcement.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score, and a golden-threshold determination. The scorecard includes
a ranked leaderboard, excellence signals, failure patterns, and regression signals.

---

ANTI-PATTERN ANCHOR -- READ BEFORE SCORING

The following two patterns produce incorrect output. Read them before beginning
the scoring phase. Do not produce output that resembles either pattern.

PATTERN A -- THE OMISSION PATH
This pattern fails C-15 (mandatory bidirectional Change field):

  C-08 -- Regression signals (A)
  Verdict:  PARTIAL
  Evidence: "A regression section exists and identifies criterion-output pairs
             that degraded from PASS since the prior round."
  [*Change*: field absent]

  Why this fails: When the verdict matches baseline, the scorer moves on with
  nothing written. The Change field is only mentally triggered by divergence.
  In a long scoring pass over many criteria and outputs, divergences are missed.
  The correct form requires writing NO CHANGE for every matching verdict, making
  omission structurally impossible: a missing field is a gap, not a valid state.

PATTERN B -- THE FRESH-LOOKUP PATH
This pattern fails C-16 (Change Manifest phase):

  [SCORING COMPLETE -- no inline CHANGE annotations written during scoring]

  REGRESSION SIGNALS:
  Re-reading prior-round baseline to identify regressions...
  V-01 C-08: PARTIAL --> PASS (improvement, not a regression)
  V-02 C-13: PASS --> PARTIAL (regression detected)
  V-03 C-14: FAIL --> PARTIAL (improvement)

  Why this fails: Regressions were assembled by inspecting the baseline in
  synthesis -- after the scoring pass was finished. Any divergence that occurred
  during scoring was not recorded at the scoring site. If the synthesis-phase
  baseline lookup misses a criterion (attention drift, output ordering confusion)
  the regression is silently lost. The correct form writes CHANGE at the scoring
  site during the scoring pass; synthesis consumes the collected annotations.

---

SCORING PHASE

For each output, produce a scoring table. Each evidence cell must survive the
specificity test: a reader who has not seen this output should be able to identify
it from the evidence alone.

  Output: [output identifier]

  | ID   | Criterion | Weight | Verdict          | Evidence                          |
  |------|-----------|--------|------------------|-----------------------------------|
  | C-01 | [name]    | E      | PASS/PARTIAL/FAIL | [specific evidence -- this output] |
  ...

  No row may be skipped. No evidence cell may be blank.

  If prior data exists and a verdict differs from the prior round, add an inline
  annotation immediately after the row:
    [CHANGE C-NN: prior [verdict] --> now [verdict] -- [reason]]

  Compute composite:
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

If prior-round score data is provided, identify any regression (prior PASS or
PARTIAL to current FAIL; or prior PASS to current PARTIAL) using the inline
[CHANGE ...] annotations written during scoring. Do not re-read the baseline
table to derive this list.

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no annotations were written: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."
```

---

## V-04 -- Axes P+Q: Mandatory Change field + Change Manifest phase

**Variation axes**: Combination of P (output format -- mandatory bidirectional Change field)
and Q (lifecycle emphasis -- Change Manifest phase with gate and SYNTHESIS prohibition).

**Hypothesis**: This is the minimum sufficient combination for C-15 and C-16. Axis P closes
the omission path: every criterion block carries a mandatory `*Change*:` field; NO CHANGE is
required even when the verdict matches. Axis Q closes the fresh-lookup path: a dedicated
Phase 2 collects all CHANGE entries before SYNTHESIS; SYNTHESIS is architecturally prohibited
from re-reading the baseline. Together: every change is recorded at the scoring site (P) and
collected into a manifest before synthesis can read it (Q). Predicts: C-15 PASS (mandatory
field, unconditional, two permissible values); C-16 PASS (manifest phase, gate token, explicit
prohibition); C-14 PASS (baseline load gate in Phase 0); C-09 FAIL (no anti-pattern anchor).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

CHANGE TRACKING ARCHITECTURE

Two structural mechanisms enforce regression detection. Both are required.

MECHANISM 1 -- Mandatory bidirectional Change field (active during SCORING)

  Every criterion block in Phase 1 carries a *Change*: field.
  Exactly three permissible values:

    *Change*: NO CHANGE                              -- verdict matches prior round
    *Change*: CHANGE from [prior verdict]: [reason]  -- verdict differs
    *Change*: NO PRIOR DATA                          -- no prior round score available

  Rules:
  - The field is always required. It is not conditional.
  - A criterion block without *Change*: is structurally incomplete.
  - Write NO CHANGE when today's verdict matches the prior-round verdict.
  - Write CHANGE from [prior] when today's verdict differs.
  - Write NO PRIOR DATA when no prior round score file is available.

MECHANISM 2 -- Change Manifest phase (between SCORING and SYNTHESIS)

  After all outputs are scored, Phase 2 sweeps every *Change*: CHANGE entry
  into a structured table before SYNTHESIS can begin.
  SYNTHESIS draws from this manifest exclusively.
  SYNTHESIS is explicitly prohibited from re-reading the Phase 0 baseline table
  or the Phase 1 scoring blocks to derive regression data.

---

PHASE 0: BASELINE LOAD

If prior-round score data is provided, build a baseline table:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | ... | C-16 |
  |--------|------|------|------|------|------|------|------|------|-----|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

---

PHASE 1: SCORING

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion, write a scoring block:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation; must uniquely identify
             this output -- not a description that could apply to any output]
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA

  No criterion may be skipped for any output.
  No evidence cell may be blank.

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
```

---

## V-05 -- Axes P+Q+R: Mandatory Change field + Change Manifest + Anti-pattern anchor

**Variation axes**: Combination of P (mandatory bidirectional Change field), Q (Change Manifest
phase), and R (inertia framing -- anti-pattern anchor showing omission and fresh-lookup
failure modes before scoring begins).

**Hypothesis**: R adds a framing axis orthogonal to the structural mechanisms in P+Q. P
closes the structural omission path. Q closes the structural fresh-lookup path. R primes the
scorer with the failure modes both paths represent, so that when the mandatory field and
manifest gates appear in the instructions, the scorer understands *why* each mechanism exists.
Predicts: C-15 PASS (mandatory field from P); C-16 PASS (manifest phase from Q); C-09 PASS
(anti-pattern anchor from R, precedes scoring instructions, demonstrates specific failure
modes tied to essential criteria); C-14 PASS (baseline load gate in Phase 0). Tests whether
framing elevates evidence quality beyond what structural enforcement alone produces in V-04.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence quote,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals.

---

ANTI-PATTERN ANCHOR -- READ BEFORE SCORING

Two structural failure modes are prohibited. Read both before scoring begins.

FAILURE MODE A -- OMISSION PATH (prevented by Mechanism 1 below)

  Typical output:

    C-13 -- Inline regression annotation (A)
    Verdict:  PARTIAL
    Evidence: "Each criterion block contains a CHANGE slot that fires when the
               verdict differs from the prior round."
    [no *Change*: field]

  Why this fails: The Change field is absent. A scorer who agrees with the
  baseline verdict has no slot to fill and naturally moves on. The omission is
  invisible -- it looks like compliance. When a divergence occurs in a later
  criterion, the scorer may forget the pattern. The mandatory form closes this:
  writing NO CHANGE is required for every matching verdict; the field's absence
  is a structural gap, not a valid empty state.

FAILURE MODE B -- FRESH-LOOKUP PATH (prevented by Mechanism 2 below)

  Typical output:

    [SCORING COMPLETE -- no *Change*: fields written during scoring]

    PHASE 3 SYNTHESIS -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS -- improvement
    V-02 C-13: prior PASS, now PARTIAL -- regression
    V-03 C-14: prior FAIL, now PARTIAL -- improvement

  Why this fails: Regressions were identified by re-reading the baseline in
  synthesis -- a retrospective lookup. The scoring phase had no concurrent
  recording. If the scorer misattributes a verdict during the baseline lookup
  (output identity confusion, criterion name similarity), the regression is
  silently wrong or missing. The correct form records CHANGE at the scoring site;
  a manifest phase collects all annotations before synthesis begins; synthesis
  reads only from the manifest.

---

CHANGE TRACKING ARCHITECTURE

Two structural mechanisms prevent the failure modes above. Both are required.

MECHANISM 1 -- Mandatory bidirectional Change field (closes Failure Mode A)

  Every criterion block in Phase 1 carries a *Change*: field.
  Exactly three permissible values:

    *Change*: NO CHANGE                              -- verdict matches prior round
    *Change*: CHANGE from [prior verdict]: [reason]  -- verdict differs
    *Change*: NO PRIOR DATA                          -- no prior round score available

  The field is always required. A criterion block without *Change*: is
  structurally incomplete. Conditional forms ("write here if verdict changes")
  are not permitted -- they leave the omission path open.

MECHANISM 2 -- Change Manifest phase (closes Failure Mode B)

  After all outputs are scored, Phase 2 sweeps every *Change*: CHANGE entry
  into a structured table before SYNTHESIS begins.
  SYNTHESIS draws from this manifest exclusively.
  SYNTHESIS is architecturally prohibited from re-reading the Phase 0 baseline
  table or Phase 1 scoring blocks to derive regression data.
  Any regression not recorded at the scoring site via *Change*: is not a
  detectable regression in this round.

---

PHASE 0: BASELINE LOAD

If prior-round score data is provided, build a baseline table:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | ... | C-16 |
  |--------|------|------|------|------|------|------|------|------|-----|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

---

PHASE 1: SCORING

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion, write a scoring block. Each evidence cell
must pass the specificity test: a reader who has not seen this output should be
able to identify it from the evidence alone -- not from a description of what
the criterion requires.

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation; uniquely identifies this
             output; fails if it could describe any well-designed output]
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [one sentence -- what changed and why]
          | NO PRIOR DATA

  No criterion may be skipped. No evidence cell may be blank.

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

Sweep every *Change*: field that reads CHANGE from [prior] from Phase 1 into
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
Manifest in Phase 2.

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
```

---

## Variation summary

| Variation | Axes | Key mechanism | C-15 pred | C-16 pred | C-09 pred | Notes |
|-----------|------|---------------|-----------|-----------|-----------|-------|
| V-01 | P | Mandatory bidirectional `*Change*:` field -- unconditional, two values | PASS | FAIL | FAIL | Closes omission path only; no manifest, no prohibition on SYNTHESIS re-reading baseline |
| V-02 | Q | Change Manifest phase -- gate + prohibition + SYNTHESIS draws from manifest | FAIL | PASS | FAIL | Closes fresh-lookup path only; Change field is conditional -- omission path remains open |
| V-03 | R | Anti-pattern anchor showing both failure modes before scoring instructions | FAIL | FAIL | PASS | Framing only; raises quality floor but cannot close structural gaps |
| V-04 | P+Q | Mandatory Change field + Change Manifest phase | PASS | PASS | FAIL | Minimum sufficient combination for both new criteria; no framing |
| V-05 | P+Q+R | V-04 + anti-pattern anchor for both failure modes | PASS | PASS | PASS | Tests whether framing elevates evidence quality beyond structural enforcement alone |

**Spread design**: V-01 and V-02 are diagnostic isolation variations -- each closes exactly
one of the two C-15/C-16 failure modes. Comparing their scores against V-04 isolates the
marginal value of each mechanism. V-03 is the framing-only low-scoring contrast: expected to
pass C-09 and fail C-15/C-16, confirming that inertia framing alone cannot substitute for
structural enforcement. V-04 is the minimum sufficient combination. V-05 tests whether R
adds measurable diagnostic depth on top of P+Q.

**Orthogonality**: P and Q are architecturally independent -- P operates at the criterion
level during scoring; Q operates at the phase level between scoring and synthesis. R is
independent of both -- it is a pre-scoring framing layer with no structural effect on what
slots are required or what phases exist. The combination V-04 (P+Q) closes both failure modes
without any framing; V-05 (P+Q+R) tests whether framing improves execution even when the
structural mechanisms are already present.

**Formula note**: v4 uses 9 aspirational criteria (C-08 through C-16) at 10 points each,
for an aspirational bucket of 90 points. Total max = 180. Formula:
`(essential_pass/5 * 60) + (recommended_pass/2 * 30) + (aspirational_pass/9 * 90)`.
Golden threshold of composite >= 80 is unchanged from prior rounds.
