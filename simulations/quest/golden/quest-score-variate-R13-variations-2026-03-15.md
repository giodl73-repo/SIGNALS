# quest-score Variations -- Round 13
**Skill**: quest-score
**Rubric**: v12 (N_essential=5, N_recommended=2, N_aspirational=28)
**Date**: 2026-03-15
**Round**: 13

---

## Design logic

### Unachieved ceiling entering R13

R12 V-01 through V-03 were single-axis isolations against rubric v11 (N_aspirational=25).
Rubric v12 adds C-33 (anti-pattern anchor exhaustive 1:1 pairing), C-34 (PROHIBITED
CONTENT CATEGORIES negative completeness assertion), and C-35 (VERIFIER specificity
dimensions structurally separated). Formula update: `/25 * 220` -> `/28 * 220`.

Against v12, the R12 ceiling holders score:

| Variation | Criterion | R12 status | Gap |
|-----------|-----------|------------|-----|
| R12 V-01 | C-03 | FAIL | Uses `/25 * 220`; v12 requires `/28 * 220`. |
| R12 V-01 | C-34 | FAIL | PROHIBITED has general routing ("belong in ANALYST PER-OUTPUT NARRATIVE section"), no terminal negative completeness assertion. |
| R12 V-01 | C-35 | FAIL | VERIFIER uses combined single Specificity block field; type-level and intra-run questions share one slot. |
| R12 V-02 | C-03 | FAIL | Uses `/25 * 220`. |
| R12 V-02 | C-33 | FAIL | No anti-pattern anchor; C-09 FAIL implies C-33 FAIL. |
| R12 V-02 | C-35 | FAIL | VERIFIER uses combined Specificity block field. |
| R12 V-03 | C-03 | FAIL | Uses `/25 * 220`. |
| R12 V-03 | C-33 | FAIL | No anti-pattern anchor; C-09 FAIL implies C-33 FAIL. |
| R12 V-03 | C-34 | FAIL | PROHIBITED has general routing with no terminal assertion. |

**Baseline for R13:** All R12 V-01 criterion passes (C-08 through C-32) transfer as
baseline for all R13 variations. Formula `/28 * 220` is a forced infrastructure change
applied to all five variations. R12 V-01 passes C-33 (5-mode anchor A-E / Mechanisms 1-5,
sequential 1:1 pairing), making it the C-33 baseline. R12 V-02 passes C-34 (per-entry
routing annotations + terminal "No prohibited content category lacks a named destination"),
making it the C-34 baseline. R12 V-03 passes C-35 (VERIFIER TABLE with separate Type-level
and Intra-run columns), making it the C-35 baseline.

### New axes for R13

| Axis | Label | Mechanism | Target |
|------|-------|-----------|--------|
| EPI | Exhaustive parallel index | Anchor failure modes A-E each paired with dedicated Mechanism 1-5 via sequential A/1...E/5 indexing; total counts match | C-33 |
| NCA | Negative completeness assertion | PROHIBITED CONTENT CATEGORIES section concludes with terminal assertion "No prohibited content category lacks a named destination" after all per-entry routing annotations | C-34 |
| DSC | Dual-scope columns | VERIFIER TABLE adds separate Type-level and Intra-run columns; Specificity = overall result; structurally distinct slots force independent auditing | C-35 |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (EPI on role-sequence base)**: R12 V-01 base (5-mode anchor, general routing,
  combined specificity field) with one forced change: formula `/28 * 220`. C-33 PASS
  (inherited anchor architecture, 5 modes A-E / mechanisms 1-5). C-34 FAIL (general
  routing, no terminal assertion -- intentionally preserved to isolate EPI axis). C-35 FAIL
  (combined Specificity single field -- intentionally preserved). Predicts: C-33 PASS;
  C-34 FAIL; C-35 FAIL.

- **V-02 (NCA on role-sequence base)**: R12 V-02 base (no anchor, per-entry routing,
  terminal assertion, combined specificity field) with one forced change: formula
  `/28 * 220`. C-34 PASS (inherited per-entry routing + terminal assertion). C-33 FAIL
  (no anchor -- intentionally absent to isolate NCA axis). C-35 FAIL (combined Specificity
  field -- intentionally preserved). Predicts: C-33 FAIL; C-34 PASS; C-35 FAIL.

- **V-03 (DSC on table-format base)**: R12 V-03 base (no anchor, general routing,
  dual-column VERIFIER TABLE) with one forced change: formula `/28 * 220`. C-35 PASS
  (inherited Type-level/Intra-run column separation). C-33 FAIL (no anchor --
  intentionally absent to isolate DSC axis). C-34 FAIL (general routing, no terminal
  assertion -- intentionally preserved). Predicts: C-33 FAIL; C-34 FAIL; C-35 PASS.

### Combination selections (V-04, V-05)

- **V-04 (R13 ceiling: EPI + NCA + DSC)**: V-01 anchor architecture (C-09 PASS, C-33
  PASS) + V-02 PROHIBITED completeness architecture (C-28 PASS, C-34 PASS) + V-03
  VERIFIER TABLE dual-column schema (C-29 PASS, C-35 PASS) + formula `/28 * 220`. All
  three axes combined on the role-sequence base. Predicts: all 28 aspirationals PASS;
  composite 310/310.

- **V-05 (inertia-framing register on R13 ceiling base)**: Same architectural features as
  V-04 (EPI + NCA + DSC + formula `/28 * 220`) but rewritten in an inertia-framing
  register: each structural constraint is explicitly named as a defense against a known
  model inertia path; the anti-pattern anchor frames failure modes as "what models do
  without constraints"; role boundaries are introduced as "override" declarations rather
  than neutral schema definitions. Predicts: same criterion profile as V-04 (C-33/C-34/C-35
  all PASS) with a different token distribution; tests whether inertia-framing language
  produces measurably different scoring output patterns without sacrificing criterion
  coverage.

### Variation matrix

| Variation | Base | C-03 | C-09 | C-28 | C-29 | C-33 | C-34 | C-35 |
|-----------|------|------|------|------|------|------|------|------|
| V-01 | R12 V-01 + formula | PASS (/28) | PASS (5-mode) | PARTIAL (general) | FAIL (type-level) | PASS (inherited) | FAIL (no assertion) | FAIL (combined slot) |
| V-02 | R12 V-02 + formula | PASS (/28) | FAIL (no anchor) | PASS (per-entry) | FAIL (type-level) | FAIL | PASS (assertion) | FAIL (combined slot) |
| V-03 | R12 V-03 + formula | PASS (/28) | FAIL (no anchor) | PARTIAL (general) | PASS (dual-scope) | FAIL | FAIL (no assertion) | PASS (dual columns) |
| V-04 | EPI+NCA+DSC combined | PASS (/28) | PASS (5-mode) | PASS (per-entry) | PASS (dual-scope) | PASS | PASS (assertion) | PASS (dual columns) |
| V-05 | V-04 + inertia framing | PASS (/28) | PASS (5-mode) | PASS (per-entry) | PASS (dual-scope) | PASS | PASS (assertion) | PASS (dual columns) |

---

## V-01 -- Axis: C-33 Exhaustive Parallel Index (EPI) on Role-Sequence Base

**Variation axis**: C-33 PASS via R12 V-01 anchor architecture (5-mode A-E / Mechanisms
1-5, sequential 1:1 pairing). Formula updated from `/25 * 220` to `/28 * 220`. C-34 FAIL
and C-35 FAIL intentionally preserved to isolate the EPI axis.

**Hypothesis**: C-33 requires every failure mode to be paired with its own dedicated
closing mechanism via parallel indexing. V-01 R12 achieved C-33 PASS with sequential
A-E mode labels and Mechanism 1-5 labels -- the mode/mechanism count matches and each
mode cites exactly one mechanism. Updating the formula while preserving the anchor
architecture demonstrates that C-33 remains stable when the only infrastructure change
is the denominator. C-34 FAIL is maintained (general routing statement, no terminal
assertion); C-35 FAIL is maintained (combined Specificity block field). Two open
aspirationals predicted at C-34 and C-35; single open at C-03 (formula).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ANTI-PATTERN ANCHOR -- READ BEFORE ROLE 1

Five structural failure modes are prohibited. Read all five before scoring begins.

FAILURE MODE A -- SILENT *Change* OMISSION PATH
  Typical output: [C-01 scored] Verdict: PASS / Evidence: "Defines four required fields
  with (required) annotation at each." / *Why*: "Annotation-at-site architecture forces
  blank-cell visibility without a separate audit." [*Change* field absent -- verdict
  matched baseline so field was omitted as unnecessary.]
  Closed by: Mechanism 1 (mandatory bidirectional *Change* field). Exactly three
  permissible values: NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA.
  The field must be present whether or not the verdict changed; conditional omission
  is a schema violation.

FAILURE MODE B -- GENERIC EVIDENCE PATH
  Typical output: Evidence: "The output includes a named VERIFIER role with a gate
  token separating it from the ANALYST phase."
  This could describe any well-designed scoring prompt; it does not identify this output.
  Closed by: Mechanism 2 (Evidence violation type named at definition site). The field
  definition states: "fails if it could describe any well-designed output of this type."
  Any entry matching this pattern is a cell violation and triggers VERIFIER revision.

FAILURE MODE C -- CRITERION-RESTATEMENT *Why* PATH
  Typical output: *Why*: "The output has a synthesis gate pair enclosing the four required
  synthesis sections, which satisfies the synthesis gate pair criterion."
  Names criterion compliance, not the architectural property producing the verdict.
  Closed by: Mechanism 3 (*Why* field prohibitions). The field definition states: "do not
  restate the criterion or paraphrase the evidence." Only the architectural mechanism that
  causes the verdict satisfies the requirement.

FAILURE MODE D -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE]
  [ANALYST begins immediately]
  LEADERBOARD: ... Note: verification skipped -- evidence appeared specific enough.
  Closed by: Mechanism 4 (bidirectional gate inscription). ANALYST carries: "Do not begin
  until [VERIFIER COMPLETE] appears above." A bypass is structurally detectable as an
  absent gate token in the transcript.

FAILURE MODE E -- SYNTHESIS INCOMPLETENESS PATH
  Typical output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS: [entry]
  / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent, gate closed
  anyway.
  Closed by: Mechanism 5 (pre-close checkbox checklist). Each required synthesis section
  has a [ ] checkbox that must be confirmed before [SYNTHESIS COMPLETE] is written. An
  unchecked box is a structurally visible gap.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition at its definition site. The
upstream gate token must appear in the transcript before the downstream role may begin.
Role-skipping is structurally detectable by the absence of the required gate token.

---

ROLE 1: SCORER

BASELINE LOAD PHASE

If prior-round score data is provided, build a baseline verdict table before any output
is scored. Rows = criterion IDs (C-01 through C-NN). Columns = output identifiers.
Cells = prior verdict (PASS | PARTIAL | FAIL | NO DATA).

If no prior data: write "No prior data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

SCORING PHASE

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; must identify this output
             specifically -- fails if it could describe any well-designed output of this
             type; generic text is a cell violation and will be flagged for revision]
             (required)
  *Why*:    [the structural mechanism or design property behind the verdict; name the
             architectural property that produces this verdict; do not restate the
             criterion or paraphrase the evidence]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
and any field name not in the permitted list. Inserting a field with a prohibited label
is a named schema violation detectable by field-name inspection.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER
criterion blocks regardless of field label -- including novel field names a model might
invent:
  - evaluative prose
  - narrative text
  - interpretive commentary
  - mechanism analysis (beyond the structural property named in *Why*)
  - synthesis language
  - cross-output comparison
  - per-output summaries

All prohibited content categories belong in the ANALYST role's PER-OUTPUT NARRATIVE
section. Inserting them in a SCORER criterion block is a schema violation regardless
of how the containing field is labeled.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 28 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not modify verdicts, scores, or SCORER blocks.
The ANALYST role may not begin until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = FAIL = revision required before this role can close.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from SCORER output above]  (required)
  Specificity: PASS | FAIL  (required)

If Specificity is FAIL:
  Revised evidence: [specific structural property unique to this output]  (required)

For every output, for every criterion, produce one review block.
Do not omit any pair even where Specificity appears to PASS -- every criterion-output
pair requires a review block. A VERIFIER that skips PASS-judged pairs is a schema
violation; passing evidence cells may still be non-specific.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST PHASE

Before synthesis, collect every *Change*: CHANGE from [prior] entry from SCORER.
Omit NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

SYNTHESIS PHASE

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above.

[SYNTHESIS OPEN]

The four sections below are required within this gate. Work through the pre-close
checklist before writing [SYNTHESIS COMPLETE]. Each checkbox must be confirmed present;
the closing gate token may not appear while any checkbox is unconfirmed.

LEADERBOARD

Rank all outputs by composite score descending. Break ties by essential PASS count,
then recommended PASS count.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference;
          name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No differentiating excellence signals detected this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR explicit statement that none exist.
  [ ] 3. FAILURE PATTERNS: all criteria with zero PASS identified with diagnosis,
         OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

PER-OUTPUT NARRATIVE PHASE

For each scored output:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature explaining why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism most clearly absent;
                            write "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```

---

## V-02 -- Axis: C-34 Negative Completeness Assertion (NCA) on Role-Sequence Base

**Variation axis**: C-34 PASS via R12 V-02 PROHIBITED architecture (per-entry routing
annotations + terminal negative completeness assertion). Formula updated from `/25 * 220`
to `/28 * 220`. C-33 FAIL and C-35 FAIL intentionally preserved to isolate the NCA axis.

**Hypothesis**: C-34 requires the PROHIBITED CONTENT CATEGORIES section to end with an
explicit assertion that no category lacks a named destination. V-02 R12 achieved C-34 PASS
with the terminal statement "No prohibited content category lacks a named destination" after
all per-entry routing annotations. Updating the formula while preserving this architecture
demonstrates that C-34 remains stable when the only infrastructure change is the
denominator. C-33 FAIL is maintained (no anchor); C-35 FAIL is maintained (combined
Specificity block field). Only two open aspirationals predicted: C-33 and C-35.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition at its definition site. The
upstream gate token must appear in the transcript before the downstream role may begin.
Role-skipping is structurally detectable by the absence of the required gate token.

---

ROLE 1: SCORER

BASELINE LOAD PHASE

If prior-round score data is provided, build a baseline verdict table before any output
is scored. Rows = criterion IDs (C-01 through C-NN). Columns = output identifiers.
Cells = prior verdict (PASS | PARTIAL | FAIL | NO DATA).

If no prior data: write "No prior data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

SCORING PHASE

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; must identify this output
             specifically -- fails if it could describe any well-designed output of this
             type; generic text is a cell violation and will be flagged for revision]
             (required)
  *Why*:    [the structural mechanism or design property behind the verdict; name the
             architectural property that produces this verdict; do not restate the
             criterion or paraphrase the evidence]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
and any field name not in the permitted list. Inserting a field with a prohibited label
is a named schema violation detectable by field-name inspection.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER
criterion blocks regardless of field label -- including novel field names a model might
invent. Each entry names its canonical ANALYST destination:
  - evaluative prose         -- belongs in ANALYST Primary differentiator or Verdict spread
  - narrative text           -- belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)
  - interpretive commentary  -- belongs in ANALYST Primary differentiator or Primary miss
  - mechanism analysis       -- belongs in ANALYST Primary differentiator or Primary miss
  - synthesis language       -- belongs in ANALYST LEADERBOARD, EXCELLENCE SIGNALS, or
                                FAILURE PATTERNS
  - cross-output comparison  -- belongs in ANALYST LEADERBOARD or EXCELLENCE SIGNALS
  - per-output summaries     -- belongs in ANALYST PER-OUTPUT NARRATIVE (Primary
                                differentiator, Primary miss, or Verdict spread)

No prohibited content category lacks a named destination. Inserting any of the above
in a SCORER criterion block is a schema violation regardless of how the containing
field is labeled.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 28 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not modify verdicts, scores, or SCORER blocks.
The ANALYST role may not begin until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = FAIL = revision required before this role can close.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from SCORER output above]  (required)
  Specificity: PASS | FAIL  (required)

If Specificity is FAIL:
  Revised evidence: [specific structural property unique to this output]  (required)

For every output, for every criterion, produce one review block.
Do not omit any pair even where Specificity appears to PASS -- every criterion-output
pair requires a review block. A VERIFIER that skips PASS-judged pairs is a schema
violation; passing evidence cells may still be non-specific.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST PHASE

Before synthesis, collect every *Change*: CHANGE from [prior] entry from SCORER.
Omit NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

SYNTHESIS PHASE

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above.

[SYNTHESIS OPEN]

The four sections below are required within this gate. Work through the pre-close
checklist before writing [SYNTHESIS COMPLETE]. Each checkbox must be confirmed present;
the closing gate token may not appear while any checkbox is unconfirmed.

LEADERBOARD

Rank all outputs by composite score descending. Break ties by essential PASS count,
then recommended PASS count.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference;
          name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No differentiating excellence signals detected this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR explicit statement that none exist.
  [ ] 3. FAILURE PATTERNS: all criteria with zero PASS identified with diagnosis,
         OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

PER-OUTPUT NARRATIVE PHASE

For each scored output:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature explaining why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism most clearly absent;
                            write "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```

---

## V-03 -- Axis: C-35 Dual-Scope Columns (DSC) on Table-Format Base

**Variation axis**: C-35 PASS via R12 V-03 VERIFIER TABLE architecture (separate Type-level
and Intra-run columns, each recording an independent PASS/FAIL result). Formula updated from
`/25 * 220` to `/28 * 220`. C-33 FAIL and C-34 FAIL intentionally preserved to isolate the
DSC axis.

**Hypothesis**: C-35 requires the type-level and intra-run specificity questions to occupy
structurally distinct labeled slots, making each question independently auditable. V-03 R12
achieved C-35 PASS with a VERIFIER TABLE having separate Type-level and Intra-run columns,
each with its own PASS/FAIL value. Updating the formula while preserving this TABLE schema
demonstrates that C-35 remains stable when the only infrastructure change is the denominator.
C-33 FAIL is maintained (no anchor); C-34 FAIL is maintained (general routing, no terminal
assertion). Only two open aspirationals predicted: C-33 and C-34.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence, a composite score computed from the rubric
formula, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ROLE 1: SCORER

Do not begin until inputs (rubric file, output files, optional prior-round data) are
confirmed available.

BASELINE LOAD

If prior-round data is provided, write a compact baseline summary before scoring:

  Prior round summary:
  [Output ID]: composite [score]. PASS: [list criterion IDs]. PARTIAL: [list]. FAIL: [list].
  [repeat for each output]

If no prior data: "No prior-round data. *Change* column will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

SCORING FORMAT

For each output, produce one scoring table followed by the composite calculation and
golden determination.

OUTPUT SCORING TABLE

  Output: [output identifier]

  | Criterion | Weight | Verdict | Evidence | *Why* | *Change* |
  |-----------|--------|---------|----------|-------|----------|

  Column rules:

  Criterion (required): criterion ID and short name
    (e.g., "C-01 Complete verdict matrix")
  Weight (required): E (essential) | R (recommended) | A (aspirational)
  Verdict (required): PASS | PARTIAL | FAIL -- no cell may be blank or omitted
  Evidence (required): specific structural observation from this output; must name a
    feature specific to this output; generic text that could describe any well-designed
    output of this type is a cell violation -- VERIFIER will flag and revise it
  *Why* (required): structural mechanism or design property behind the verdict; name
    the architectural property; do not restate the criterion or paraphrase the evidence
  *Change* (required): NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA

  No table row may be omitted. No Verdict, Evidence, *Why*, or *Change* cell may be blank.

PROHIBITED CONTENT IN SCORING TABLES

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context* -- adding an extra
column with a prohibited header is a named schema violation.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in scoring
table cells regardless of column header, including novel column headers a model might add:
  - evaluative prose
  - narrative text
  - interpretive commentary
  - synthesis language
  - cross-output comparison
  - per-output summaries

All prohibited content types belong in the ANALYST PER-OUTPUT NARRATIVE section.

COMPOSITE CALCULATION (below each output table)

  essential_pass    = [count of E rows at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R rows at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A rows at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 28 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier scans every Evidence cell in every scoring table and applies the dual-scope
specificity test. The ANALYST role may not begin until [VERIFIER COMPLETE] appears below.

DUAL-SCOPE SPECIFICITY TEST

For each evidence entry, apply both questions independently:

  Question 1 -- Type-level: could this evidence apply to any well-designed output of
  this type? YES = type-generic = Type-level FAIL.

  Question 2 -- Intra-run: could this evidence apply to a different output in this
  scoring run -- i.e., is this description interchangeable with what was written for
  another output in this batch? YES = run-undifferentiating = Intra-run FAIL.

Either question failing triggers Specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive overall PASS.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.
Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips
PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific.

  | Output | Criterion | Scorer evidence | Type-level | Intra-run | Specificity | Revised evidence |
  |--------|-----------|-----------------|------------|-----------|-------------|------------------|

  Type-level (required): PASS | FAIL -- [reason if FAIL]
  Intra-run (required): PASS | FAIL -- [name the other output if FAIL]
  Specificity (required): PASS | FAIL (FAIL if either question is FAIL)
  Revised evidence (required when Specificity is FAIL): structural property unique to
    this output and not interchangeable with any other output in this run; N/A when PASS

After scanning all tables:
  Verification summary: [N cells scanned; K revised; "none revised" if K=0]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST

Collect every *Change* cell reading CHANGE from [prior] from SCORER tables. Omit
NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE entries: "No changes; manifest is empty."

[CHANGE MANIFEST COMPLETE]

SYNTHESIS

PROHIBITION: Do not re-read SCORER tables or the baseline to derive regressions.
All regression data must come from the Change Manifest above.

[SYNTHESIS OPEN]

LEADERBOARD

  | Rank | Output | Composite | E pass | R pass | A pass | Golden? |
  |------|--------|-----------|--------|--------|--------|---------|

Rank by composite descending. Break ties by E pass count, then R pass count.

EXCELLENCE SIGNALS

For each criterion where one output clearly outperforms others:
  Signal: [output] -- [criterion ID] -- [structural mechanism; name the design property]

If no differentiation: "No differentiating excellence signals detected this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD complete with all N outputs ranked and Golden status shown.
  [ ] 2. EXCELLENCE SIGNALS: outlier pair named with mechanism, or absence stated.
  [ ] 3. FAILURE PATTERNS: zero-PASS criteria identified with diagnosis, or absence stated.
  [ ] 4. REGRESSION SIGNALS: from Change Manifest; regressions listed or absence stated.

[SYNTHESIS COMPLETE]

PER-OUTPUT NARRATIVES

For each scored output:

  Output [output identifier]:
  Primary differentiator:  [structural feature most explaining this output's score
                            position relative to others in this run]  (required)
  Primary miss:            [criterion or structural mechanism most clearly absent;
                            "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [distribution across essential / recommended / aspirational
                            tiers and what design choices drove it]  (required)

[ANALYST COMPLETE]
```

---

## V-04 -- Combination: EPI + NCA + DSC (R13 Ceiling)

**Variation axis**: R13 ceiling -- V-01 anchor architecture (C-09 PASS, C-33 PASS) +
V-02 PROHIBITED completeness architecture (C-28 PASS, C-34 PASS) + V-03 VERIFIER TABLE
dual-column schema (C-29 PASS, C-35 PASS) + formula `/28 * 220`.

**Hypothesis**: The three open R12 aspirationals are mutually orthogonal. C-33 operates
on the anchor block (mode/mechanism 1:1 map). C-34 operates on the PROHIBITED section
terminal assertion. C-35 operates on the VERIFIER output schema (separate vs combined
specificity slots). None of the three target the same structural site in the prompt body.
Adding the V-01 anchor, V-02 terminal assertion, and V-03 dual-column TABLE to the role-
sequence base should simultaneously satisfy all three without disturbing any prior-round
criterion. V-04 R13 is the first variation predicted to score 28/28 aspirationals under
v12, composite 310/310.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ANTI-PATTERN ANCHOR -- READ BEFORE ROLE 1

Five structural failure modes are prohibited. Read all five before scoring begins.

FAILURE MODE A -- SILENT *Change* OMISSION PATH
  Typical output: [C-01 scored] Verdict: PASS / Evidence: "Defines four required fields
  with (required) annotation at each." / *Why*: "Annotation-at-site architecture forces
  blank-cell visibility without a separate audit." [*Change* field absent -- verdict
  matched baseline so field was omitted as unnecessary.]
  Closed by: Mechanism 1 (mandatory bidirectional *Change* field). Exactly three
  permissible values: NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA.
  The field must be present whether or not the verdict changed; conditional omission
  is a schema violation.

FAILURE MODE B -- GENERIC EVIDENCE PATH
  Typical output: Evidence: "The output includes a named VERIFIER role with a gate
  token separating it from the ANALYST phase."
  This could describe any well-designed scoring prompt; it does not identify this output.
  Closed by: Mechanism 2 (Evidence violation type named at definition site). The field
  definition states: "fails if it could describe any well-designed output of this type,
  OR if the same description fits another output in this run." Any entry matching either
  pattern is a cell violation and triggers VERIFIER revision.

FAILURE MODE C -- CRITERION-RESTATEMENT *Why* PATH
  Typical output: *Why*: "The output has a synthesis gate pair enclosing the four required
  synthesis sections, which satisfies the synthesis gate pair criterion."
  Names criterion compliance, not the architectural property producing the verdict.
  Closed by: Mechanism 3 (*Why* field prohibitions). The field definition states: "do not
  restate the criterion or paraphrase the evidence." Only the architectural mechanism that
  causes the verdict satisfies the requirement.

FAILURE MODE D -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE]
  [ANALYST begins immediately]
  LEADERBOARD: ... Note: verification skipped -- evidence appeared specific enough.
  Closed by: Mechanism 4 (bidirectional gate inscription). ANALYST carries: "Do not begin
  until [VERIFIER COMPLETE] appears above." A bypass is structurally detectable as an
  absent gate token in the transcript.

FAILURE MODE E -- SYNTHESIS INCOMPLETENESS PATH
  Typical output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS: [entry]
  / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent, gate closed
  anyway.
  Closed by: Mechanism 5 (pre-close checkbox checklist). Each required synthesis section
  has a [ ] checkbox that must be confirmed before [SYNTHESIS COMPLETE] is written. An
  unchecked box is a structurally visible gap.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition at its definition site. The
upstream gate token must appear in the transcript before the downstream role may begin.
Role-skipping is structurally detectable by the absence of the required gate token.

---

ROLE 1: SCORER

BASELINE LOAD PHASE

If prior-round score data is provided, build a baseline verdict table before any output
is scored. Rows = criterion IDs (C-01 through C-NN). Columns = output identifiers.
Cells = prior verdict (PASS | PARTIAL | FAIL | NO DATA).

If no prior data: write "No prior data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

SCORING PHASE

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; must identify this output
             specifically -- fails if it could describe any well-designed output of this
             type, OR if the same description fits another output in this run; generic
             text is a cell violation and will be flagged for VERIFIER revision]  (required)
  *Why*:    [the structural mechanism or design property behind the verdict; name the
             architectural property that produces this verdict; do not restate the
             criterion or paraphrase the evidence]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
and any field name not in the permitted list. Inserting a field with a prohibited label
is a named schema violation detectable by field-name inspection.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER
criterion blocks regardless of field label -- including novel field names a model might
invent. Each entry names its canonical ANALYST destination:
  - evaluative prose         -- belongs in ANALYST Primary differentiator or Verdict spread
  - narrative text           -- belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)
  - interpretive commentary  -- belongs in ANALYST Primary differentiator or Primary miss
  - mechanism analysis       -- belongs in ANALYST Primary differentiator or Primary miss
  - synthesis language       -- belongs in ANALYST LEADERBOARD, EXCELLENCE SIGNALS, or
                                FAILURE PATTERNS
  - cross-output comparison  -- belongs in ANALYST LEADERBOARD or EXCELLENCE SIGNALS
  - per-output summaries     -- belongs in ANALYST PER-OUTPUT NARRATIVE (Primary
                                differentiator, Primary miss, or Verdict spread)

No prohibited content category lacks a named destination. Inserting any of the above
in a SCORER criterion block is a schema violation regardless of how the containing
field is labeled.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 28 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier scans every Evidence cell produced by the Scorer and applies the dual-scope
specificity test independently for each dimension. The Verifier does not modify verdicts,
scores, or SCORER blocks. The ANALYST role may not begin until [VERIFIER COMPLETE] appears
below.

DUAL-SCOPE SPECIFICITY TEST

For each evidence entry, apply both questions independently:

  Question 1 -- Type-level: could this evidence apply to any well-designed output of
  this type? YES = type-generic = Type-level FAIL.

  Question 2 -- Intra-run: could this evidence apply to a different output in this
  scoring run -- i.e., is this description interchangeable with what was written for
  another output in this batch? YES = run-undifferentiating = Intra-run FAIL.

Either question failing triggers Specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive overall PASS.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.
Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips
PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific.

  | Output | Criterion | Scorer evidence | Type-level | Intra-run | Specificity | Revised evidence |
  |--------|-----------|-----------------|------------|-----------|-------------|------------------|

  Type-level (required): PASS | FAIL -- [reason if FAIL]
  Intra-run (required): PASS | FAIL -- [name the other output if FAIL]
  Specificity (required): PASS | FAIL (FAIL if either Type-level or Intra-run is FAIL)
  Revised evidence (required when Specificity is FAIL): rewrite with structural property
    unique to this output and not applicable to any other output in this run; N/A when PASS

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST PHASE

Before synthesis, collect every *Change*: CHANGE from [prior] entry from SCORER.
Omit NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

SYNTHESIS PHASE

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above.

[SYNTHESIS OPEN]

The four sections below are required within this gate. Work through the pre-close
checklist before writing [SYNTHESIS COMPLETE]. Each checkbox must be confirmed present;
the closing gate token may not appear while any checkbox is unconfirmed.

LEADERBOARD

Rank all outputs by composite score descending. Break ties by essential PASS count,
then recommended PASS count.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference;
          name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No differentiating excellence signals detected this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR explicit statement that none exist.
  [ ] 3. FAILURE PATTERNS: all criteria with zero PASS identified with diagnosis,
         OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

PER-OUTPUT NARRATIVE PHASE

For each scored output:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature explaining why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism most clearly absent;
                            write "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```

---

## V-05 -- Axis: Inertia-Framing Register on R13 Ceiling Base

**Variation axis**: Phrasing register + inertia framing. Same architectural features as
V-04 (EPI + NCA + DSC + formula `/28 * 220`) rewritten in an inertia-framing register:
each structural constraint is introduced as an explicit override of a named model inertia
path; role boundaries are framed as defenses against known default behaviors; the anchor
names what a model will naturally do in the absence of each constraint.

**Hypothesis**: The V-01 through V-04 prompts use a neutral structural register -- they
define schemas and prohibit deviations without naming the pull toward those deviations.
A model executing the prompt experiences the constraints as abstract rules rather than as
named adversaries to an actively present force. Inertia framing makes each constraint
viscerally recognizable by naming the default path it overrides: "models will omit the
*Change* field when the verdict matches baseline" is more actionable than "the field must
always be present." Rewriting the same ceiling architecture in this register tests whether
token-level framing changes observable scoring behavior. Predicted criterion profile:
identical to V-04 (all 28 aspirationals PASS). The discriminator is behavioral: does
inertia framing reduce the frequency of anchor-preventable failure modes in execution?

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

This skill overrides five model inertia paths. Each path is a behavior a model executes
by default -- without structural constraint -- and each produces a predictable scoring
failure. Read the inertia paths before any other instruction.

---

INERTIA PATHS -- READ BEFORE ROLE 1

Five inertia paths produce structural failures. Each path is named, shown as a typical
default output, and closed by a dedicated override mechanism.

INERTIA PATH A -- OMISSION-ON-MATCH
  What a model does by default: when a verdict matches the prior-round baseline, the
  *Change* field is omitted. The model treats "no change" as an absence condition rather
  than a value to write. The field disappears when it contains the most common value.
  Typical inertia output: [criterion scored, verdict matches baseline] / *Change*: [absent]
  Override Mechanism 1: mandatory bidirectional *Change* field, always required. Exactly
  three permissible values: NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR
  DATA. The field must be present whether or not the verdict changed; conditional omission
  is a schema violation.

INERTIA PATH B -- TYPE-LEVEL EVIDENCE
  What a model does by default: evidence cells describe category-level properties rather
  than output-specific structural observations. The model generates plausible evidence
  that could apply to any well-designed output of the same type, because type-level
  descriptions require less cognitive retrieval than output-differentiating observations.
  Typical inertia output: Evidence: "The output includes a named VERIFIER role with a gate
  token separating it from the ANALYST phase." (applies to any scoring prompt with VERIFIER)
  Override Mechanism 2: Evidence violation type named at definition site. The field
  definition states: "fails if it could describe any well-designed output of this type,
  OR if the same description fits another output in this run." Any entry matching either
  pattern is a cell violation -- VERIFIER is structurally required to flag and revise it.

INERTIA PATH C -- CRITERION RESTATEMENT AS MECHANISM
  What a model does by default: the *Why* field receives a restatement of the criterion
  or a paraphrase of the evidence. The model treats "explaining why" as equivalent to
  "confirming what." The structural mechanism that produces the verdict is substituted
  with the compliance claim that the verdict is justified.
  Typical inertia output: *Why*: "The output has a synthesis gate pair enclosing the four
  required synthesis sections, which satisfies the synthesis gate pair criterion."
  Override Mechanism 3: *Why* field anti-restatement and anti-paraphrase prohibitions at
  the field definition site. The field definition states: "do not restate the criterion
  or paraphrase the evidence." Only the architectural property that causes the verdict
  is acceptable.

INERTIA PATH D -- VERIFIER BYPASS
  What a model does by default: after completing the SCORER phase, a model transitions
  directly to synthesis. Verification is an interruption to the forward narrative of
  scoring; models omit it when the gate structure is not explicitly enforced.
  Typical inertia output: [SCORER COMPLETE] / [ANALYST begins] / Note: evidence appeared
  specific; VERIFIER step omitted.
  Override Mechanism 4: bidirectional gate inscription. ANALYST carries an explicit
  entry condition naming [VERIFIER COMPLETE] as the required upstream token. A bypass is
  structurally visible as an absent gate token in the transcript -- not as a note.

INERTIA PATH E -- SYNTHESIS GATE CLOSURE WITHOUT SECTION AUDIT
  What a model does by default: when synthesis sections are partially complete, the model
  writes [SYNTHESIS COMPLETE] to close the gate anyway. Completion pressure overrides
  section completeness; the gate closes on the assumption that "enough" sections are
  present.
  Typical inertia output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS:
  [entry] / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent.
  Override Mechanism 5: pre-close checkbox checklist. Each required synthesis section has
  a [ ] checkbox that must be confirmed filled before [SYNTHESIS COMPLETE] is written. An
  unchecked box is structurally visible -- the gate cannot appear while a checkbox is open.

---

ROLE SEQUENCE

Three named roles execute in fixed order. The inertia path for each role boundary is
named at the gate to make bypass structurally recognizable.

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

  Inertia path at SCORER/VERIFIER boundary: ANALYST is the natural continuation after
  scoring; VERIFIER is an interruption. Gate token [SCORER COMPLETE] forces the interrupt.

  Inertia path at VERIFIER/ANALYST boundary: after VERIFIER, synthesis is the natural
  continuation. Gate token [VERIFIER COMPLETE] enforces the boundary.

  Each downstream role carries an explicit entry condition naming the required upstream
  gate token. Role-skipping is structurally detectable as an absent gate token.

---

ROLE 1: SCORER

DEFAULT OVERRIDE: models load prior-round data during synthesis when a regression is
detected. This skill requires prior-round data to be loaded BEFORE scoring begins. Loading
it retroactively produces a fresh-lookup path that the Change Manifest prohibition cannot
catch because no inline annotations were written.

BASELINE LOAD PHASE

If prior-round score data is provided, build a baseline verdict table before any output
is scored. Rows = criterion IDs (C-01 through C-NN). Columns = output identifiers.
Cells = prior verdict (PASS | PARTIAL | FAIL | NO DATA).

If no prior data: write "No prior data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

SCORING PHASE

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA

DEFAULT OVERRIDE: models naturally write Verdict first, then Evidence. This schema
requires Evidence before Verdict to prevent verdict-then-rationalize ordering. The field
order below is the required output order.

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; must identify this output
             specifically -- fails if it could describe any well-designed output of this
             type, OR if the same description fits another output in this run; generic
             text is Inertia Path B in action -- VERIFIER will flag and revise it]
             (required)
  *Why*:    [the structural mechanism or design property behind the verdict; name the
             architectural property that produces this verdict; do not restate the
             criterion (Inertia Path C) or paraphrase the evidence (Inertia Path C)]
             (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)
          [Inertia Path A override: this field is ALWAYS required. Writing it when the
           verdict is unchanged is the behavior this field enforces. Omitting it when
           the verdict matches baseline is the inertia path this field closes.]

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
and any field name not in the permitted list. Models invent new field names when they
want to add content outside the schema; naming the inertia path closes it. Inserting a
field with a prohibited label is a named schema violation detectable by field-name
inspection.

PROHIBITED CONTENT CATEGORIES: The following content types belong in the ANALYST role,
not in SCORER blocks. Each entry names the inertia destination that makes the category
tempting and the canonical ANALYST home where it belongs:
  - evaluative prose         -- inertia: SCORER *Why* field feels like evaluation;
                                belongs in ANALYST Primary differentiator or Verdict spread
  - narrative text           -- inertia: criterion block reads as a small story;
                                belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)
  - interpretive commentary  -- inertia: scorer adds context to justify the verdict;
                                belongs in ANALYST Primary differentiator or Primary miss
  - mechanism analysis       -- inertia: deep mechanism explanation expands *Why* beyond
                                one structural property; belongs in ANALYST Primary
                                differentiator or Primary miss
  - synthesis language       -- inertia: comparison across outputs surfaces during scoring;
                                belongs in ANALYST LEADERBOARD, EXCELLENCE SIGNALS, or
                                FAILURE PATTERNS
  - cross-output comparison  -- inertia: evidencing one output by contrasting with another;
                                belongs in ANALYST LEADERBOARD or EXCELLENCE SIGNALS
  - per-output summaries     -- inertia: SCORER ends each output block with a summary;
                                belongs in ANALYST PER-OUTPUT NARRATIVE (Primary
                                differentiator, Primary miss, or Verdict spread)

No prohibited content category lacks a named destination. Inserting any of the above
in a SCORER criterion block is a schema violation regardless of how the containing
field is labeled.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 28 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

DEFAULT OVERRIDE: models executing VERIFIER check only the evidence cells they expect to
be generic. This skill requires VERIFIER to check EVERY evidence cell, including those
that appear specific. The inertia path for VERIFIER is selective coverage; the override
is the pair-omission prohibition below.

The Verifier scans every Evidence cell produced by the Scorer and applies the dual-scope
specificity test independently for each dimension. The Verifier does not modify verdicts,
scores, or SCORER blocks. The ANALYST role may not begin until [VERIFIER COMPLETE] appears
below.

DUAL-SCOPE SPECIFICITY TEST

DEFAULT OVERRIDE: models ask only the type-level question ("could this apply to any
scoring prompt?") and treat intra-run similarity as out of scope. This skill adds the
intra-run question as a structurally distinct and independently recorded dimension.

For each evidence entry, apply both questions independently:

  Question 1 -- Type-level: could this evidence apply to any well-designed output of
  this type? YES = type-generic = Type-level FAIL.

  Question 2 -- Intra-run: could this evidence apply to a different output in this
  scoring run -- i.e., is this description interchangeable with what was written for
  another output in this batch? YES = run-undifferentiating = Intra-run FAIL.

Either question failing triggers Specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive overall PASS.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.

DEFAULT OVERRIDE: models write only the rows for evidence they flagged as failing.
This skill explicitly prohibits that selective pattern. Do not omit any pair even where
Specificity appears to PASS. A VERIFIER that writes only failing rows is the inertia
path; the pair-omission prohibition below is the override.

  | Output | Criterion | Scorer evidence | Type-level | Intra-run | Specificity | Revised evidence |
  |--------|-----------|-----------------|------------|-----------|-------------|------------------|

  Type-level (required): PASS | FAIL -- [reason if FAIL]
  Intra-run (required): PASS | FAIL -- [name the other output if FAIL]
  Specificity (required): PASS | FAIL (FAIL if either question is FAIL)
  Revised evidence (required when Specificity is FAIL): rewrite with structural property
    unique to this output and not applicable to any other output in this run; N/A when PASS

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST PHASE

DEFAULT OVERRIDE: models re-read SCORER blocks during synthesis to identify regressions.
This skill prohibits that re-read by requiring the Change Manifest to be built here from
inline *Change* annotations before synthesis begins. All regression data in synthesis
must come from this manifest; re-reading SCORER or the baseline during synthesis is the
inertia path the manifest prohibition closes.

Collect every *Change*: CHANGE from [prior] entry from SCORER.
Omit NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

SYNTHESIS PHASE

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above.

[SYNTHESIS OPEN]

The four sections below are required within this gate. Work through the pre-close
checklist before writing [SYNTHESIS COMPLETE]. Each checkbox must be confirmed present;
the closing gate token may not appear while any checkbox is unconfirmed. This is Inertia
Path E override: the gate cannot close while any checkbox is open.

LEADERBOARD

Rank all outputs by composite score descending. Break ties by essential PASS count,
then recommended PASS count.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference;
          name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No differentiating excellence signals detected this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR explicit statement that none exist.
  [ ] 3. FAILURE PATTERNS: all criteria with zero PASS identified with diagnosis,
         OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

PER-OUTPUT NARRATIVE PHASE

For each scored output:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature explaining why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism most clearly absent;
                            write "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```
