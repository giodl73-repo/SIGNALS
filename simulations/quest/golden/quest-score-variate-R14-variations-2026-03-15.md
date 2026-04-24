# quest-score Variations -- Round 14
**Skill**: quest-score
**Rubric**: v13 (N_essential=5, N_recommended=2, N_aspirational=31)
**Date**: 2026-03-15
**Round**: 14

---

## Design logic

### Unachieved ceiling entering R14

R13 was scored against rubric v13 (N_aspirational=31). Rubric v13 added C-36 (anti-pattern
anchor criterion-indexed closing mechanism), C-37 (VERIFIER anchor block dual-question
verbatim pre-statement), and C-38 (baseline load table per-variation open-item
decomposition). Formula update: `/28 * 220` -> `/31 * 220`.

R13 V-01 achieved C-36, C-37, C-38 PASS as new PASSes under v13, but left two aspirationals
open:

| Variation | Criterion | R13 status | Gap |
|-----------|-----------|------------|-----|
| R13 V-01 | C-34 | FAIL | PROHIBITED section ends after per-entry routing annotations; terminal assertion "No prohibited content category lacks a named destination" is absent |
| R13 V-01 | C-35 | FAIL | VERIFIER combines type-level and intra-run into a single Specificity field; questions are not in structurally separated labeled columns |

**Baseline for R14:** All R13 V-01 criterion passes carry forward (C-08 through C-33,
C-36 through C-38). Formula `/31 * 220` is infrastructure -- a variation using `/28`
produces C-03 FAIL on every output. R13 V-01 passed C-36 (criterion IDs in mechanism
descriptions), C-37 (VERIFIER anchor review block), and C-38 (per-variation baseline
table), making it the structural base for all five R14 variations. R13 V-02 passed C-34
(per-entry routing + terminal assertion), making it the C-34 reference. R13 V-04 passed
C-35 (VERIFIER TABLE with separate Type-level/Intra-run columns), making it the C-35
reference.

### New axes for R14

| Axis | Label | Mechanism | Target |
|------|-------|-----------|--------|
| NCA | Negative completeness assertion | Terminal assertion closes PROHIBITED list: "No prohibited content category lacks a named destination." Converts the list from open enumeration to self-verifying set. | C-34 |
| DSC | Dual-scope column separation | VERIFIER TABLE separates Type-level and Intra-run into distinct labeled columns; Specificity = conjunction; each column independently auditable | C-35 |
| TFS | Table-format SCORER | SCORER uses per-output table rows (Criterion, Weight, Verdict, Evidence, *Why*, *Change*) instead of criterion blocks; all C-36/C-37/C-38 features preserved; tests format stability across SCORER schema change | format axis |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (NCA on R13 V-01 block base)**: R13 V-01 base + terminal assertion added to end
  of PROHIBITED list. VERIFIER ANCHOR REVIEW BLOCK preserved (C-37 PASS). Per-variation
  baseline table preserved (C-38 PASS). Criterion IDs in mechanism descriptions preserved
  (C-36 PASS). 5-mode anchor A-E / Mechanisms 1-5 preserved (C-33 PASS). VERIFIER uses
  combined single Specificity field (C-35 FAIL intentionally). Predicts: C-34 PASS; C-35 FAIL.

- **V-02 (DSC on R13 V-01 block base)**: R13 V-01 base + separate Type-level and Intra-run
  columns added to VERIFIER TABLE. VERIFIER ANCHOR REVIEW BLOCK preserved (C-37 PASS).
  Per-variation baseline table preserved (C-38 PASS). Criterion IDs in mechanism descriptions
  preserved (C-36 PASS). PROHIBITED section ends after routing annotations without terminal
  assertion (C-34 FAIL intentionally). Predicts: C-34 FAIL; C-35 PASS.

- **V-03 (TFS on R13 V-01 architecture)**: R13 V-01 architecture mapped onto a table-format
  SCORER (per-output scoring table with Criterion / Weight / Verdict / Evidence / *Why* /
  *Change* columns). All C-36/C-37/C-38 features preserved. No NCA addition (C-34 FAIL
  intentionally). VERIFIER uses combined Specificity field (C-35 FAIL intentionally). Tests
  whether the format change from criterion blocks to table rows is compatible with the
  C-33/C-36/C-37/C-38 architecture. Predicts: C-33 PASS; C-34 FAIL; C-35 FAIL;
  C-36/C-37/C-38 PASS.

### Combination selections (V-04, V-05)

- **V-04 (NCA + DSC, R14 ceiling)**: V-01 NCA terminal assertion + V-02 DSC dual-column
  VERIFIER TABLE + all R13 V-01 base features (5-mode anchor / C-33, criterion IDs / C-36,
  anchor review block / C-37, per-variation table / C-38) + formula `/31`. All three open
  aspirationals closed simultaneously. Predicts: C-34 PASS; C-35 PASS; 31/31 aspirationals;
  composite 310/310.

- **V-05 (V-04 + inertia framing)**: Same architectural features as V-04 (NCA + DSC + all
  R13 V-01 features + formula `/31`) rewritten in inertia-framing register. Each structural
  constraint is named as a defense against a named model inertia path; the anchor frames
  failure modes as "what a model does by default"; role boundaries are introduced as
  "inertia override" declarations. Predicted criterion profile identical to V-04 (31/31).
  Tests whether inertia-framing language produces measurably different execution behavior.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Formula | /31 | /31 | /31 | /31 | /31 |
| SCORER format | block | block | table | block | block |
| Terminal assertion NCA (C-34) | YES | NO | NO | YES | YES |
| Dual-scope columns DSC (C-35) | NO | YES | NO | YES | YES |
| Criterion IDs in mechanisms (C-36) | YES | YES | YES | YES | YES |
| VERIFIER anchor review block (C-37) | YES | YES | YES | YES | YES |
| Per-variation baseline table (C-38) | YES | YES | YES | YES | YES |
| 5-mode anchor 1:1 (C-33) | YES | YES | YES | YES | YES |
| Inertia framing | NO | NO | NO | NO | YES |
| C-34 prediction | PASS | FAIL | FAIL | PASS | PASS |
| C-35 prediction | FAIL | PASS | FAIL | PASS | PASS |

---

## V-01 -- Axis NCA: Terminal Assertion on R13 V-01 Block Base

**Variation axis**: C-34 PASS via terminal assertion "No prohibited content category lacks
a named destination" appended after all per-entry routing annotations in the PROHIBITED
CONTENT CATEGORIES section. All R13 V-01 features preserved: criterion IDs in mechanism
descriptions (C-36), VERIFIER anchor review block (C-37), per-variation baseline table
(C-38), 5-mode anchor (C-33). VERIFIER uses combined single Specificity field; C-35 FAIL
intentionally preserved to isolate the NCA axis.

**Hypothesis**: C-34 is closed by the terminal assertion form. Adding one line after the
PROHIBITED list converts the list from an open enumeration to a self-verifying set. The
combined Specificity field in the VERIFIER does not interfere with the assertion. C-35
FAIL is maintained because the type-level and intra-run questions remain in a single
Specificity slot. Predicted open aspirationals: C-35 only; C-34 closes.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ANTI-PATTERN ANCHOR -- READ BEFORE ROLE 1

Five structural failure modes are prohibited. Each closing mechanism description names
the criterion ID that enforces it. Read all five before scoring begins.

FAILURE MODE A -- SILENT *Change* OMISSION PATH
  Typical output: [C-15 scored] Verdict: PASS / Evidence: "Defines four required fields
  with (required) annotation at each." / *Why*: "Annotation-at-site architecture forces
  blank-cell visibility." [*Change* field absent -- verdict matched baseline so field was
  treated as optional.]
  Closing mechanism: C-15 requires the mandatory bidirectional *Change* field to be
  present regardless of whether the verdict changed; Mechanism 1 enforces this by declaring
  exactly three permissible values at the field definition site: NO CHANGE | CHANGE from
  [prior verdict]: [reason] | NO PRIOR DATA. Omitting the field when the verdict matches
  baseline is the inertia path Mechanism 1 closes; conditional omission is a schema
  violation detectable by field-name inspection.

FAILURE MODE B -- GENERIC EVIDENCE PATH
  Typical output: Evidence: "The output includes a named VERIFIER role with a gate
  token separating it from the ANALYST phase."
  This could describe any well-designed scoring prompt; it does not identify this output
  specifically.
  Closing mechanism: C-02 requires evidence to identify the specific output being scored;
  Mechanism 2 names the violation type at the Evidence field definition site: "fails if it
  could describe any well-designed output of this type, OR if the same description fits
  another output in this run." Any entry matching either pattern is a cell violation and
  triggers VERIFIER revision.

FAILURE MODE C -- CRITERION-RESTATEMENT *Why* PATH
  Typical output: *Why*: "The output has a synthesis gate pair enclosing the four required
  synthesis sections, which satisfies the synthesis gate pair criterion."
  Names criterion compliance, not the architectural property producing the verdict.
  Closing mechanism: C-11 requires the *Why* field to name the structural mechanism or
  design property behind the verdict; Mechanism 3 places anti-restatement and
  anti-paraphrase prohibitions at the *Why* field definition site: "do not restate the
  criterion or paraphrase the evidence." Only the architectural property that causes the
  verdict satisfies the field.

FAILURE MODE D -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE]
  [ANALYST begins immediately]
  LEADERBOARD: ... Note: evidence appeared specific enough; VERIFIER step omitted.
  Closing mechanism: C-21 requires each downstream role to carry a bidirectional gate
  inscription naming the upstream gate token; Mechanism 4 places the entry condition on
  the ANALYST role definition site: "Do not begin until [VERIFIER COMPLETE] appears
  above." C-33 requires this failure mode to have its own dedicated mechanism; Mechanism 4
  is Mode D's dedicated mechanism and is not shared with Mechanisms 1-3 or 5. A bypass
  is structurally detectable as an absent gate token in the transcript.

FAILURE MODE E -- SYNTHESIS INCOMPLETENESS PATH
  Typical output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS: [entry]
  / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent, gate closed
  anyway.
  Closing mechanism: C-24 requires a pre-close checklist enumerating each required synthesis
  section before [SYNTHESIS COMPLETE] may be written; Mechanism 5 places [ ] checkboxes at
  each synthesis section label, structurally preventing gate closure while any box is
  unconfirmed. C-33 requires this mode to have its own dedicated mechanism; Mechanism 5 is
  Mode E's dedicated mechanism. An unchecked box is structurally visible without a separate
  audit.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition at its definition site naming
the upstream gate token required above. Role-skipping is structurally detectable by the
absence of the required gate token.

---

ROLE 1: SCORER

BASELINE LOAD PHASE

If prior-round score data is provided, build a per-variation baseline table before any
output is scored. One row per variation; each row names the variation identifier and
lists its open aspirationals from the prior round.

  | Variation | Open aspirationals from prior round          |
  |-----------|----------------------------------------------|
  | [V-ID]    | [criterion IDs, e.g., C-34, C-35] or "none" |

If no prior data: write "No prior-round data. *Change* fields will read NO PRIOR DATA."

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
             text is a cell violation and will be flagged for VERIFIER revision]
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
            + (aspirational_pass / 31 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
dual-scope specificity test. The Verifier does not modify verdicts, scores, or SCORER
blocks. The ANALYST role may not begin until [VERIFIER COMPLETE] appears below.

ANCHOR REVIEW BLOCK

Before reviewing any criterion-output pair, confirm both specificity questions verbatim.
This block is the authoritative statement of each question; per-row review entries must
apply these exact questions without rephrasing.

  Q1 -- Type-level: "Could this evidence apply to any well-designed output of this
  type?" YES = type-generic = FAIL. Required revision if YES.

  Q2 -- Intra-run: "Could this evidence apply to a different output in this scoring
  run -- i.e., is this description interchangeable with what was written for another
  output in this batch?" YES = run-undifferentiating = FAIL. Required revision if YES.

Either question answering YES triggers Specificity FAIL. Evidence must be both
type-specific AND run-differentiating to receive overall Specificity PASS.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from SCORER output above]  (required)
  Specificity: PASS | FAIL -- [if FAIL: state which question failed and why]  (required)

If Specificity is FAIL:
  Revised evidence: [structural property unique to this output and not interchangeable
                     with any other output in this run]  (required)

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

## V-02 -- Axis DSC: Dual-Scope Columns on R13 V-01 Block Base

**Variation axis**: C-35 PASS via separate Type-level and Intra-run columns in the VERIFIER
TABLE, each column recording an independent PASS/FAIL result. All R13 V-01 features
preserved: criterion IDs in mechanism descriptions (C-36), VERIFIER anchor review block
(C-37), per-variation baseline table (C-38), 5-mode anchor (C-33). PROHIBITED section
ends after routing annotations without terminal assertion; C-34 FAIL intentionally
preserved to isolate the DSC axis.

**Hypothesis**: C-35 requires structural separation of the two specificity dimensions into
distinct labeled slots. The VERIFIER TABLE's column schema makes the separation explicit:
Type-level and Intra-run are independent columns each with their own PASS/FAIL value.
A combined Specificity field that addresses both in one cell satisfies C-29 but not C-35.
The DSC axis adds column separation without any change to the PROHIBITED section. Predicted
open aspirationals: C-34 only; C-35 closes.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ANTI-PATTERN ANCHOR -- READ BEFORE ROLE 1

Five structural failure modes are prohibited. Each closing mechanism description names
the criterion ID that enforces it. Read all five before scoring begins.

FAILURE MODE A -- SILENT *Change* OMISSION PATH
  Typical output: [C-15 scored] Verdict: PASS / Evidence: "Defines four required fields
  with (required) annotation at each." / *Why*: "Annotation-at-site architecture forces
  blank-cell visibility." [*Change* field absent -- verdict matched baseline so field was
  treated as optional.]
  Closing mechanism: C-15 requires the mandatory bidirectional *Change* field to be
  present regardless of whether the verdict changed; Mechanism 1 enforces this by declaring
  exactly three permissible values at the field definition site: NO CHANGE | CHANGE from
  [prior verdict]: [reason] | NO PRIOR DATA. Conditional omission is a schema violation
  detectable by field-name inspection.

FAILURE MODE B -- GENERIC EVIDENCE PATH
  Typical output: Evidence: "The output includes a named VERIFIER role with a gate
  token separating it from the ANALYST phase."
  This could describe any well-designed scoring prompt; it does not identify this output.
  Closing mechanism: C-02 requires evidence to identify the specific output being scored;
  Mechanism 2 names the violation type at the Evidence field definition site: "fails if it
  could describe any well-designed output of this type, OR if the same description fits
  another output in this run." Any entry matching either pattern is a cell violation and
  triggers VERIFIER revision.

FAILURE MODE C -- CRITERION-RESTATEMENT *Why* PATH
  Typical output: *Why*: "The output has a synthesis gate pair enclosing the four required
  synthesis sections, which satisfies the synthesis gate pair criterion."
  Names criterion compliance, not the architectural property producing the verdict.
  Closing mechanism: C-11 requires the *Why* field to name the structural mechanism or
  design property behind the verdict; Mechanism 3 places anti-restatement and
  anti-paraphrase prohibitions at the *Why* field definition site: "do not restate the
  criterion or paraphrase the evidence." Only the architectural property that causes the
  verdict satisfies the field.

FAILURE MODE D -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE]
  [ANALYST begins immediately]
  LEADERBOARD: ... Note: evidence appeared specific enough; VERIFIER step omitted.
  Closing mechanism: C-21 requires each downstream role to carry a bidirectional gate
  inscription naming the upstream gate token; Mechanism 4 places the entry condition on
  the ANALYST role definition site: "Do not begin until [VERIFIER COMPLETE] appears
  above." C-33 requires this failure mode to have its own dedicated mechanism; Mechanism 4
  is Mode D's dedicated mechanism and is not shared with Mechanisms 1-3 or 5. A bypass
  is structurally detectable as an absent gate token in the transcript.

FAILURE MODE E -- SYNTHESIS INCOMPLETENESS PATH
  Typical output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS: [entry]
  / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent, gate closed
  anyway.
  Closing mechanism: C-24 requires a pre-close checklist enumerating each required synthesis
  section before [SYNTHESIS COMPLETE] may be written; Mechanism 5 places [ ] checkboxes at
  each synthesis section label, structurally preventing gate closure while any box is
  unconfirmed. C-33 requires this mode to have its own dedicated mechanism; Mechanism 5 is
  Mode E's dedicated mechanism. An unchecked box is structurally visible without a separate
  audit.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition at its definition site naming
the upstream gate token required above. Role-skipping is structurally detectable by the
absence of the required gate token.

---

ROLE 1: SCORER

BASELINE LOAD PHASE

If prior-round score data is provided, build a per-variation baseline table before any
output is scored. One row per variation; each row names the variation identifier and
lists its open aspirationals from the prior round.

  | Variation | Open aspirationals from prior round          |
  |-----------|----------------------------------------------|
  | [V-ID]    | [criterion IDs, e.g., C-34, C-35] or "none" |

If no prior data: write "No prior-round data. *Change* fields will read NO PRIOR DATA."

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
             text is a cell violation and will be flagged for VERIFIER revision]
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

Inserting any prohibited content category in a SCORER criterion block is a schema
violation regardless of how the containing field is labeled.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 31 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
dual-scope specificity test independently for each dimension. The Verifier does not
modify verdicts, scores, or SCORER blocks. The ANALYST role may not begin until
[VERIFIER COMPLETE] appears below.

ANCHOR REVIEW BLOCK

Before reviewing any criterion-output pair, confirm both specificity questions verbatim.
This block is the authoritative statement of each question; per-row review entries must
apply these exact questions without rephrasing.

  Q1 -- Type-level: "Could this evidence apply to any well-designed output of this
  type?" YES = type-generic = FAIL. Required revision if YES.

  Q2 -- Intra-run: "Could this evidence apply to a different output in this scoring
  run -- i.e., is this description interchangeable with what was written for another
  output in this batch?" YES = run-undifferentiating = FAIL. Required revision if YES.

Either question answering YES triggers Specificity FAIL. Evidence must be both
type-specific AND run-differentiating to receive overall Specificity PASS.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.
Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips
PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific.

  | Output | Criterion | Scorer evidence | Type-level | Intra-run | Specificity | Revised evidence |
  |--------|-----------|-----------------|------------|-----------|-------------|------------------|

  Type-level (required): PASS | FAIL -- [reason if FAIL; per Q1 above]
  Intra-run (required): PASS | FAIL -- [name the other output if FAIL; per Q2 above]
  Specificity (required): PASS | FAIL (FAIL if either Type-level or Intra-run is FAIL)
  Revised evidence (required when Specificity is FAIL): structural property unique to
    this output and not interchangeable with any other output in this run; N/A when PASS

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

## V-03 -- Axis TFS: Table-Format SCORER on R13 V-01 Architecture

**Variation axis**: SCORER format -- criterion blocks (block format) replaced with a
per-output scoring table (Criterion | Weight | Verdict | Evidence | *Why* | *Change*
columns). All R13 V-01 architectural features preserved: criterion IDs in mechanism
descriptions (C-36), VERIFIER anchor review block (C-37), per-variation baseline table
(C-38), 5-mode anchor (C-33). No NCA addition (C-34 FAIL). No DSC addition (C-35 FAIL).
Tests whether table-format scoring is compatible with C-33/C-36/C-37/C-38 stability.

**Hypothesis**: The table-format SCORER from R12 V-03 maps cleanly to the R13 V-01
architectural features. C-33/C-36/C-37/C-38 operate on the anchor block and VERIFIER --
both are pre-SCORER and post-SCORER respectively -- and neither is affected by the
SCORER schema format change. C-34 FAIL is maintained (no terminal assertion). C-35 FAIL
is maintained (VERIFIER uses combined Specificity field; the table format does not
require column separation). The key test: does a format change in SCORER produce any
unexpected evidence that reveals new criteria for v14?

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The scorecard includes a ranked
leaderboard, excellence signals, failure patterns, regression signals, and per-output
narrative notes.

---

ANTI-PATTERN ANCHOR -- READ BEFORE ROLE 1

Five structural failure modes are prohibited. Each closing mechanism description names
the criterion ID that enforces it. Read all five before scoring begins.

FAILURE MODE A -- SILENT *Change* OMISSION PATH
  Typical output: [table row scored] Verdict: PASS / Evidence: "..." / *Why*: "..."
  [*Change* cell blank -- verdict matched baseline so cell was left empty.]
  Closing mechanism: C-15 requires the mandatory bidirectional *Change* field present
  in every row regardless of whether the verdict changed; Mechanism 1 enforces this by
  declaring exactly three permissible values: NO CHANGE | CHANGE from [prior verdict]:
  [reason] | NO PRIOR DATA. A blank *Change* cell is a schema violation even when the
  verdict is identical to baseline.

FAILURE MODE B -- GENERIC EVIDENCE PATH
  Typical output: Evidence cell: "The output uses a named role sequence with gate tokens."
  This applies to any scoring prompt with named roles; it does not identify this output.
  Closing mechanism: C-02 requires evidence to identify the specific output being scored;
  Mechanism 2 names the violation pattern at the Evidence column definition site: "fails
  if it could describe any well-designed output of this type, OR if the same description
  fits another output in this run." Any such cell is a violation and triggers VERIFIER
  revision.

FAILURE MODE C -- CRITERION-RESTATEMENT *Why* PATH
  Typical output: *Why* cell: "Satisfies the synthesis gate pair criterion because both
  opening and closing tokens are present."
  Names compliance, not the architectural property producing the verdict.
  Closing mechanism: C-11 requires the *Why* field to name the structural mechanism
  behind the verdict; Mechanism 3 places anti-restatement prohibitions at the *Why*
  column definition site: "do not restate the criterion or paraphrase the Evidence cell."
  Only the architectural property that causes the verdict satisfies the field.

FAILURE MODE D -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE]
  [ANALYST begins immediately with leaderboard]
  Closing mechanism: C-21 requires each downstream role to carry a bidirectional gate
  inscription naming the required upstream token; Mechanism 4 places the entry condition
  at the ANALYST role definition site: "Do not begin until [VERIFIER COMPLETE] appears
  above." C-33 requires Mode D to have its own dedicated mechanism; Mechanism 4 is that
  mechanism. A bypass is structurally visible as an absent gate token.

FAILURE MODE E -- SYNTHESIS INCOMPLETENESS PATH
  Typical output: [SYNTHESIS OPEN] / LEADERBOARD present / [SYNTHESIS COMPLETE] --
  EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS absent.
  Closing mechanism: C-24 requires a pre-close checklist enumerating each required
  synthesis section before [SYNTHESIS COMPLETE] may be written; Mechanism 5 places
  [ ] checkboxes at each synthesis section, preventing gate closure while any checkbox
  is unconfirmed. C-33 requires Mode E to have its own dedicated mechanism; Mechanism 5
  is that mechanism.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition naming the upstream gate token
required above.

---

ROLE 1: SCORER

Do not begin until inputs (rubric file, output files, optional prior-round data) are
confirmed available.

BASELINE LOAD PHASE

If prior-round score data is provided, build a per-variation baseline table before any
output is scored. One row per variation; each row names the variation identifier and
lists its specific open aspirationals from the prior round.

  | Variation | Open aspirationals from prior round          |
  |-----------|----------------------------------------------|
  | [V-ID]    | [criterion IDs, e.g., C-34, C-35] or "none" |

If no prior data: write "No prior-round data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

SCORING PHASE

For each output, produce one scoring table followed by the composite calculation and
golden determination.

  Output: [output identifier]

  | Criterion | Weight | Verdict | Evidence | *Why* | *Change* |
  |-----------|--------|---------|----------|-------|----------|

  Column rules:

  Criterion (required): criterion ID and short name (e.g., "C-01 Complete verdict matrix")
  Weight (required): E (essential) | R (recommended) | A (aspirational)
  Verdict (required): PASS | PARTIAL | FAIL -- no cell may be blank or omitted
  Evidence (required): specific structural observation from this output; must name a
    feature specific to this output; fails if it could describe any well-designed output
    of this type, OR if the same description fits another output in this run -- VERIFIER
    will flag and revise such cells
  *Why* (required): structural mechanism or design property behind the verdict; do not
    restate the criterion or paraphrase the Evidence cell
  *Change* (required): NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA

  No table row may be omitted. No cell in Verdict, Evidence, *Why*, or *Change* may
  be blank.

PROHIBITED CONTENT IN SCORING TABLE CELLS

PROHIBITED FIELD LABELS (extra columns): *Note*, *Comment*, *Observation*, *Context*
-- adding a column with a prohibited header is a named schema violation.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in scoring
table cells regardless of column header, including novel column headers a model might
add. Each entry names its canonical ANALYST destination:
  - evaluative prose         -- belongs in ANALYST Primary differentiator or Verdict spread
  - narrative text           -- belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)
  - interpretive commentary  -- belongs in ANALYST Primary differentiator or Primary miss
  - mechanism analysis       -- belongs in ANALYST Primary differentiator or Primary miss
  - synthesis language       -- belongs in ANALYST LEADERBOARD, EXCELLENCE SIGNALS, or
                                FAILURE PATTERNS
  - cross-output comparison  -- belongs in ANALYST LEADERBOARD or EXCELLENCE SIGNALS
  - per-output summaries     -- belongs in ANALYST PER-OUTPUT NARRATIVE (Primary
                                differentiator, Primary miss, or Verdict spread)

Inserting any prohibited content category in a scoring table cell is a schema violation
regardless of column header.

COMPOSITE CALCULATION (below each output table)

  essential_pass    = [count of E rows at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R rows at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A rows at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 31 * 220)
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

ANCHOR REVIEW BLOCK

Before reviewing any criterion-output pair, confirm both specificity questions verbatim.
This block is the authoritative statement of each question; per-row review entries must
apply these exact questions without rephrasing.

  Q1 -- Type-level: "Could this evidence apply to any well-designed output of this
  type?" YES = type-generic = FAIL. Required revision if YES.

  Q2 -- Intra-run: "Could this evidence apply to a different output in this scoring
  run -- i.e., is this description interchangeable with what was written for another
  output in this batch?" YES = run-undifferentiating = FAIL. Required revision if YES.

Either question answering YES triggers Specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive Specificity PASS.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from scoring table above]  (required)
  Specificity: PASS | FAIL -- [if FAIL: state which question failed and cite the
               other output when Intra-run fails]  (required)

If Specificity is FAIL:
  Revised evidence: [specific structural property unique to this output and not
                     interchangeable with any other output in this run]  (required)

For every output, for every criterion, produce one review block. Do not omit any pair
even where Specificity appears to PASS.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST PHASE

Collect every *Change* cell reading CHANGE from [prior] from SCORER tables. Omit
NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE entries: "No changes; manifest is empty."

[CHANGE MANIFEST COMPLETE]

SYNTHESIS PHASE

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
  Primary differentiator:  [structural feature most explaining this output's position
                            relative to others; name the design property]  (required)
  Primary miss:            [criterion or structural mechanism most clearly absent;
                            "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [distribution across essential / recommended / aspirational
                            tiers and what design choices drove it]  (required)

[ANALYST COMPLETE]
```

---

## V-04 -- Combination NCA + DSC: R14 Ceiling

**Variation axis**: R14 ceiling -- V-01 R13 architecture (5-mode anchor C-33, criterion
IDs C-36, VERIFIER anchor review block C-37, per-variation baseline table C-38) + V-01
NCA terminal assertion (C-34) + V-02 DSC dual-column VERIFIER TABLE (C-35) + formula
`/31 * 220`. All three open aspirationals from R13 closed simultaneously.

**Hypothesis**: C-34 and C-35 are orthogonal. C-34 operates on the SCORER's PROHIBITED
CONTENT CATEGORIES section (a terminal line after the routing list). C-35 operates on
the VERIFIER TABLE column schema (separate Type-level and Intra-run columns). Neither
interferes with the other or with C-33/C-36/C-37/C-38. Adding both simultaneously to the
R13 V-01 base should produce 31/31 aspirational PASS, composite 310/310.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

---

ANTI-PATTERN ANCHOR -- READ BEFORE ROLE 1

Five structural failure modes are prohibited. Each closing mechanism description names
the criterion ID that enforces it. Read all five before scoring begins.

FAILURE MODE A -- SILENT *Change* OMISSION PATH
  Typical output: [C-15 scored] Verdict: PASS / Evidence: "Defines four required fields
  with (required) annotation at each." / *Why*: "Annotation-at-site architecture forces
  blank-cell visibility." [*Change* field absent -- verdict matched baseline so field was
  treated as optional.]
  Closing mechanism: C-15 requires the mandatory bidirectional *Change* field to be
  present regardless of whether the verdict changed; Mechanism 1 enforces this by declaring
  exactly three permissible values at the field definition site: NO CHANGE | CHANGE from
  [prior verdict]: [reason] | NO PRIOR DATA. Conditional omission is a schema violation
  detectable by field-name inspection.

FAILURE MODE B -- GENERIC EVIDENCE PATH
  Typical output: Evidence: "The output includes a named VERIFIER role with a gate
  token separating it from the ANALYST phase."
  This could describe any well-designed scoring prompt; it does not identify this output.
  Closing mechanism: C-02 requires evidence to identify the specific output being scored;
  Mechanism 2 names the violation type at the Evidence field definition site: "fails if it
  could describe any well-designed output of this type, OR if the same description fits
  another output in this run." Any entry matching either pattern is a cell violation and
  triggers VERIFIER revision.

FAILURE MODE C -- CRITERION-RESTATEMENT *Why* PATH
  Typical output: *Why*: "The output has a synthesis gate pair enclosing the four required
  synthesis sections, which satisfies the synthesis gate pair criterion."
  Names criterion compliance, not the architectural property producing the verdict.
  Closing mechanism: C-11 requires the *Why* field to name the structural mechanism or
  design property behind the verdict; Mechanism 3 places anti-restatement and
  anti-paraphrase prohibitions at the *Why* field definition site: "do not restate the
  criterion or paraphrase the evidence." Only the architectural property that causes the
  verdict satisfies the field.

FAILURE MODE D -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE]
  [ANALYST begins immediately]
  LEADERBOARD: ... Note: evidence appeared specific enough; VERIFIER step omitted.
  Closing mechanism: C-21 requires each downstream role to carry a bidirectional gate
  inscription naming the upstream gate token; Mechanism 4 places the entry condition on
  the ANALYST role definition site: "Do not begin until [VERIFIER COMPLETE] appears
  above." C-33 requires this failure mode to have its own dedicated mechanism; Mechanism 4
  is Mode D's dedicated mechanism and is not shared with Mechanisms 1-3 or 5. A bypass
  is structurally detectable as an absent gate token in the transcript.

FAILURE MODE E -- SYNTHESIS INCOMPLETENESS PATH
  Typical output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS: [entry]
  / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent, gate closed
  anyway.
  Closing mechanism: C-24 requires a pre-close checklist enumerating each required synthesis
  section before [SYNTHESIS COMPLETE] may be written; Mechanism 5 places [ ] checkboxes at
  each synthesis section label, structurally preventing gate closure while any box is
  unconfirmed. C-33 requires this mode to have its own dedicated mechanism; Mechanism 5 is
  Mode E's dedicated mechanism. An unchecked box is structurally visible without a separate
  audit.

---

ROLE SEQUENCE

Three named roles execute in fixed order:

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

Each downstream role carries an explicit entry condition at its definition site naming
the upstream gate token required above. Role-skipping is structurally detectable by the
absence of the required gate token.

---

ROLE 1: SCORER

BASELINE LOAD PHASE

If prior-round score data is provided, build a per-variation baseline table before any
output is scored. One row per variation; each row names the variation identifier and
lists its open aspirationals from the prior round.

  | Variation | Open aspirationals from prior round          |
  |-----------|----------------------------------------------|
  | [V-ID]    | [criterion IDs, e.g., C-34, C-35] or "none" |

If no prior data: write "No prior-round data. *Change* fields will read NO PRIOR DATA."

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
             text is a cell violation and will be flagged for VERIFIER revision]
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
            + (aspirational_pass / 31 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier scans every Evidence entry produced by the Scorer and applies the dual-scope
specificity test independently for each dimension. The Verifier does not modify verdicts,
scores, or SCORER blocks. The ANALYST role may not begin until [VERIFIER COMPLETE] appears
below.

ANCHOR REVIEW BLOCK

Before reviewing any criterion-output pair, confirm both specificity questions verbatim.
This block is the authoritative statement of each question; per-row review entries must
apply these exact questions without rephrasing.

  Q1 -- Type-level: "Could this evidence apply to any well-designed output of this
  type?" YES = type-generic = FAIL. Required revision if YES.

  Q2 -- Intra-run: "Could this evidence apply to a different output in this scoring
  run -- i.e., is this description interchangeable with what was written for another
  output in this batch?" YES = run-undifferentiating = FAIL. Required revision if YES.

Either question answering YES triggers Specificity FAIL. Evidence must be both
type-specific AND run-differentiating to receive overall Specificity PASS.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.
Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips
PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific.

  | Output | Criterion | Scorer evidence | Type-level | Intra-run | Specificity | Revised evidence |
  |--------|-----------|-----------------|------------|-----------|-------------|------------------|

  Type-level (required): PASS | FAIL -- [reason if FAIL; per Q1 above]
  Intra-run (required): PASS | FAIL -- [name the other output if FAIL; per Q2 above]
  Specificity (required): PASS | FAIL (FAIL if either Type-level or Intra-run is FAIL)
  Revised evidence (required when Specificity is FAIL): structural property unique to
    this output and not interchangeable with any other output in this run; N/A when PASS

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

## V-05 -- Combination NCA + DSC + Inertia Framing

**Variation axis**: Phrasing register. Same architectural features as V-04 (NCA terminal
assertion, DSC dual-column VERIFIER TABLE, 5-mode anchor / C-33, criterion IDs / C-36,
anchor review block / C-37, per-variation table / C-38, formula `/31`) rewritten in an
inertia-framing register. Each structural constraint is introduced as an explicit override
of a named model inertia path. Role definitions frame their constraints as defenses against
known default behaviors.

**Hypothesis**: V-01 through V-04 use a neutral structural register -- they define schemas
and prohibit deviations without naming the behavioral pull toward those deviations. A model
executing the prompt experiences the constraints as abstract rules. Inertia framing makes
each rule viscerally recognizable by naming the default path it overrides: "a model will
omit the terminal assertion because the list reads as complete once the last entry is
written" is more actionable than "a terminal assertion is required." The predicted criterion
profile is identical to V-04 (31/31 aspirationals PASS). The discriminator is behavioral.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

This skill overrides five model inertia paths and two structural shortcut paths. Each
path is a behavior a model executes by default without constraint, and each produces a
predictable scoring failure. Read the inertia paths before any other instruction.

---

INERTIA PATHS -- READ BEFORE ROLE 1

Five inertia paths produce structural failures in scoring. Each path is named, shown as
a typical default output, and closed by a dedicated override mechanism that names the
criterion ID enforcing the close.

INERTIA PATH A -- OMISSION-ON-MATCH
  What a model does by default: when the verdict matches the baseline, the *Change*
  field is omitted. The model treats "no change" as an absence condition rather than
  a required value to write. The field disappears when it contains the most common value.
  Typical inertia output: [criterion scored, verdict matches baseline, *Change* absent]
  Closing mechanism: C-15 requires the mandatory bidirectional *Change* field always
  present; Override Mechanism 1 declares exactly three permissible values at the field
  definition site: NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA.
  Writing NO CHANGE when the verdict is unchanged is the required behavior this override
  enforces; omitting the field when the verdict matches baseline is the inertia path this
  override closes.

INERTIA PATH B -- TYPE-LEVEL EVIDENCE
  What a model does by default: evidence cells describe category-level properties rather
  than output-specific structural observations. Type-level descriptions require less
  cognitive retrieval than output-differentiating observations; the model generates
  plausible evidence that could apply to any well-designed output of the same type.
  Typical inertia output: Evidence: "The output includes a named VERIFIER role with a
  gate token separating it from the ANALYST phase." (applies to any scoring prompt)
  Closing mechanism: C-02 requires specific output-identifying evidence; Override
  Mechanism 2 names the violation pattern at the Evidence field definition site: "fails
  if it could describe any well-designed output of this type, OR if the same description
  fits another output in this run." A VERIFIER role is structurally required to flag and
  revise any cell matching this pattern.

INERTIA PATH C -- CRITERION RESTATEMENT AS MECHANISM
  What a model does by default: the *Why* field receives a restatement of the criterion
  or a paraphrase of the evidence. The model treats "explaining why" as equivalent to
  "confirming what." The structural mechanism that produces the verdict is substituted
  with the compliance claim that the verdict is justified.
  Typical inertia output: *Why*: "The output has a synthesis gate pair enclosing the
  four required synthesis sections, which satisfies the synthesis gate pair criterion."
  Closing mechanism: C-11 requires the *Why* field to name the structural mechanism or
  design property behind the verdict; Override Mechanism 3 places anti-restatement and
  anti-paraphrase prohibitions at the *Why* field definition site. Only the architectural
  property that causes the verdict is acceptable; compliance claims are the inertia path
  this override closes.

INERTIA PATH D -- VERIFIER BYPASS
  What a model does by default: after completing the SCORER phase, the model transitions
  directly to synthesis. Verification is an interruption to the forward narrative of
  scoring; models skip it when the gate structure is not explicitly enforced.
  Typical inertia output: [SCORER COMPLETE] / [ANALYST begins] / Note: evidence appeared
  specific; VERIFIER step omitted.
  Closing mechanism: C-21 requires each downstream role to carry a bidirectional gate
  inscription; Override Mechanism 4 places an explicit entry condition at the ANALYST
  role definition site: "Do not begin until [VERIFIER COMPLETE] appears above." C-33
  requires this inertia path to have its own dedicated override mechanism; Mechanism 4
  is Path D's dedicated mechanism and is not shared with Mechanisms 1-3 or 5. A bypass
  is structurally visible as an absent gate token.

INERTIA PATH E -- SYNTHESIS GATE CLOSURE WITHOUT SECTION AUDIT
  What a model does by default: when synthesis sections are partially complete, the model
  writes [SYNTHESIS COMPLETE] anyway. Completion pressure overrides section completeness;
  the gate closes on the assumption that "enough" sections are present.
  Typical inertia output: [SYNTHESIS OPEN] / LEADERBOARD: [table] / EXCELLENCE SIGNALS:
  [entry] / [SYNTHESIS COMPLETE] -- FAILURE PATTERNS and REGRESSION SIGNALS absent.
  Closing mechanism: C-24 requires a pre-close checklist enumerating each required
  synthesis section before [SYNTHESIS COMPLETE] may be written; Override Mechanism 5
  places [ ] checkboxes at each synthesis section label. C-33 requires this inertia path
  to have its own dedicated mechanism; Mechanism 5 is Path E's dedicated mechanism. An
  unchecked box is structurally visible -- the gate cannot appear while a checkbox is open.

---

ROLE SEQUENCE

Three named roles execute in fixed order. The inertia path at each role boundary is
named to make bypass structurally recognizable.

  SCORER  --[SCORER COMPLETE]-->  VERIFIER  --[VERIFIER COMPLETE]-->  ANALYST

  Inertia path at SCORER/VERIFIER boundary: ANALYST is the natural continuation after
  scoring; VERIFIER is an interruption. Gate token [SCORER COMPLETE] forces the interrupt.

  Inertia path at VERIFIER/ANALYST boundary: after VERIFIER, synthesis is the natural
  continuation. Gate token [VERIFIER COMPLETE] enforces the boundary.

  Each downstream role carries an explicit entry condition naming the required upstream
  gate token. Role-skipping is structurally detectable as an absent gate token.

---

ROLE 1: SCORER

INERTIA OVERRIDE: models load prior-round data during synthesis when a regression is
detected. This skill requires prior-round data to be loaded BEFORE scoring begins so
that inline *Change* annotations can be written at the scoring site. Loading it
retroactively is the inertia path the BASELINE LOAD PHASE closes.

BASELINE LOAD PHASE

If prior-round score data is provided, build a per-variation baseline table before any
output is scored. One row per variation; each row names the variation identifier and
lists its open aspirationals from the prior round. The per-variation structure makes
each variation's open items addressable by row key without a full-table scan.

  | Variation | Open aspirationals from prior round          |
  |-----------|----------------------------------------------|
  | [V-ID]    | [criterion IDs, e.g., C-34, C-35] or "none" |

If no prior data: write "No prior-round data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

Scoring may not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

SCORING PHASE

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA

INERTIA OVERRIDE: models naturally write Verdict first, then rationalize Evidence.
The field order below is the required production order; it does not prevent verdict-first
execution but makes the schema order explicit.

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; must identify this output
             specifically -- fails if it could describe any well-designed output of this
             type (Inertia Path B), OR if the same description fits another output in
             this run; generic text is a cell violation -- VERIFIER will flag and revise it]
             (required)
  *Why*:    [the structural mechanism or design property behind the verdict; name the
             architectural property that produces this verdict; do not restate the criterion
             (Inertia Path C) or paraphrase the evidence (Inertia Path C)]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)
          [Inertia Path A override: this field is ALWAYS required. Writing NO CHANGE when
           the verdict is unchanged is the behavior this field enforces. Omitting the field
           when the verdict matches baseline is the inertia path this field closes.]

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
and any field name not in the permitted list. Models invent new field names when they want
to add content outside the schema; naming the inertia path closes it. Inserting a field
with a prohibited label is a named schema violation detectable by field-name inspection.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER
criterion blocks regardless of field label -- including novel field names a model might
invent. Each entry names the inertia pull that makes the category tempting and the
canonical ANALYST home where it belongs:
  - evaluative prose         -- inertia: SCORER *Why* field feels like evaluation;
                                belongs in ANALYST Primary differentiator or Verdict spread
  - narrative text           -- inertia: criterion block reads as a small story;
                                belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)
  - interpretive commentary  -- inertia: scorer adds context to justify the verdict;
                                belongs in ANALYST Primary differentiator or Primary miss
  - mechanism analysis       -- inertia: deep mechanism explanation expands *Why*;
                                belongs in ANALYST Primary differentiator or Primary miss
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
            + (aspirational_pass / 31 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

INERTIA OVERRIDE: models executing VERIFIER check only the evidence cells they expect
to be generic. This skill requires VERIFIER to check EVERY evidence cell, including
those that appear specific. The inertia path is selective coverage; the override is the
pair-omission prohibition below.

The Verifier scans every Evidence entry produced by the Scorer and applies the dual-scope
specificity test independently for each dimension. The Verifier does not modify verdicts,
scores, or SCORER blocks. The ANALYST role may not begin until [VERIFIER COMPLETE] appears
below.

ANCHOR REVIEW BLOCK

Before reviewing any criterion-output pair, confirm both specificity questions verbatim.
This block is the authoritative statement of each question. Per-row review entries must
apply these exact questions without rephrasing. Rephrasing per-row is the question-drift
inertia path; this anchor block is the override that closes it.

  Q1 -- Type-level: "Could this evidence apply to any well-designed output of this
  type?" YES = type-generic = FAIL. Required revision if YES.

  Q2 -- Intra-run: "Could this evidence apply to a different output in this scoring
  run -- i.e., is this description interchangeable with what was written for another
  output in this batch?" YES = run-undifferentiating = FAIL. Required revision if YES.

Either question answering YES triggers Specificity FAIL. Evidence must be both
type-specific AND run-differentiating to receive overall Specificity PASS.

INERTIA OVERRIDE: models applying the dual-scope test ask only the type-level question
(Path B) and treat intra-run similarity as out of scope. Q2 is a structurally distinct
column -- independently auditable. The Type-level and Intra-run columns in the table
below are the structural override that makes both questions independently recorded.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.

INERTIA OVERRIDE: models write only the rows for evidence they flagged as failing.
This skill explicitly prohibits selective coverage. Do not omit any pair even where
Specificity appears to PASS. A VERIFIER that writes only failing rows is the inertia
path; the pair-omission prohibition is the override.

  | Output | Criterion | Scorer evidence | Type-level | Intra-run | Specificity | Revised evidence |
  |--------|-----------|-----------------|------------|-----------|-------------|------------------|

  Type-level (required): PASS | FAIL -- [reason if FAIL; per Q1 above]
  Intra-run (required): PASS | FAIL -- [name the other output if FAIL; per Q2 above]
  Specificity (required): PASS | FAIL (FAIL if either Type-level or Intra-run is FAIL)
  Revised evidence (required when Specificity is FAIL): structural property unique to
    this output and not interchangeable with any other output in this run; N/A when PASS

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

CHANGE MANIFEST PHASE

INERTIA OVERRIDE: models re-read SCORER blocks during synthesis to identify regressions.
This skill prohibits that re-read. The Change Manifest built here is the only permitted
source of regression data in synthesis. Re-reading SCORER or the baseline during
synthesis is the inertia path this manifest prohibition closes.

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
