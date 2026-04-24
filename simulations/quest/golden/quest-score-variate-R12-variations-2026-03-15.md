# quest-score Variations -- Round 12
**Skill**: quest-score
**Rubric**: v11 (N_essential=5, N_recommended=2, N_aspirational=25)
**Date**: 2026-03-15
**Round**: 12

---

## Design logic

### Unachieved ceiling entering R12

R11 V-05 was the full stack against rubric v10 (N_aspirational=23, formula `/23 * 220`).
Rubric v11 adds C-31 (SCORER Evidence field -- violation type named at definition site)
and C-32 (SCORER *Why* field -- anti-restatement prohibition at definition site) and
updates the formula to `/25 * 220`. Against v11, the R11 ceiling holders score:

| Variation | Criterion | R11 status | Gap |
|-----------|-----------|------------|-----|
| R11 V-05 | C-03 | FAIL | Uses `/23 * 220`; v11 requires `/25 * 220`. Wrong denominator. |
| R11 V-05 | C-32 | PARTIAL | `*Why* field: "do not restate the criterion; do not describe the evidence."` "Do not describe the evidence" names a content type, not the paraphrase anti-pattern. C-32 requires both: criterion restatement AND evidence paraphrase. |
| R11 V-04 | C-03 | FAIL | Uses `/23 * 220`. |
| R11 V-04 | C-09 | FAIL | No anti-pattern anchor; V-04 R11 followed the V-01 R11 architecture. |
| R11 V-04 | C-28 | PARTIAL | General routing statement ("belongs in ANALYST PER-OUTPUT NARRATIVE section"); C-28 requires per-entry annotation at each category entry. |
| R11 V-01/V-02/V-03 | C-03 | FAIL | Uses `/23 * 220`. |
| R11 V-01/V-02/V-03 | C-09 | FAIL | No anti-pattern anchor. |
| R11 V-01/V-02/V-03 | C-28 | PARTIAL | General routing statement. |
| R11 V-01/V-02/V-03 | C-29 | FAIL | Type-level specificity only; intra-run question absent. |

**Baseline for R12:** All R11 V-01 criterion passes transfer as baseline. Formula
`/25 * 220` is a forced infrastructure change applied to all variations. V-01 R11
already passes C-31 and C-32 by construction. V-03 R12 (table-format base from V-02 R11)
aligns the *Why* column to include both prohibitions as a baseline correction. V-04 R11
already passes C-29, C-30, C-31, C-32 -- all inherited unchanged.

**Secondary diagnostic:** Can APA, PRR, IRQ be isolated on three different base
architectures without disturbing existing profiles? V-01/V-02/V-03 test each axis in
isolation. V-04 combines APA + PRR on the dual-scope V-04 R11 base. V-05 closes the
single V-05 R11 gap (C-32 PARTIAL).

### New axes for R12

| Axis | Label | Mechanism | Target |
|------|-------|-----------|--------|
| APA | Anti-pattern anchor | Pre-scoring block naming >=5 failure modes with typical bad-output examples and closing mechanisms, placed before ROLE 1 | C-09 |
| PRR | Per-entry routing | Each PROHIBITED CONTENT CATEGORIES entry carries its own ANALYST section destination annotation | C-28 |
| IRQ | Intra-run question | VERIFIER dual-scope test adds explicit Question 2 (intra-run) alongside Question 1 (type-level); VERIFIER schema gains separate result fields for both | C-29 |
| APR | Anti-paraphrase fix | SCORER *Why* field definition changes "do not describe the evidence" to "do not paraphrase the evidence" | C-32 |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (APA on role-sequence base)**: R11 V-01 base (bidirectional gate inscription,
  general routing, type-level specificity only, C-30 PASS, C-31 PASS, C-32 PASS) with
  two forced changes: (1) formula `/25 * 220`; (2) 5-mode anti-pattern anchor before
  ROLE 1. C-28 PARTIAL (general routing) and C-29 FAIL (type-level only) preserved
  intentionally to isolate the APA axis. Predicts: C-09 PASS; C-28 PARTIAL; C-29 FAIL.

- **V-02 (PRR on role-sequence base)**: R11 V-01 base with two forced changes: (1) formula
  `/25 * 220`; (2) per-entry routing annotations in PROHIBITED CONTENT CATEGORIES. No
  anchor (C-09 FAIL); no intra-run question (C-29 FAIL). Predicts: C-09 FAIL; C-28 PASS;
  C-29 FAIL.

- **V-03 (IRQ on table-format base)**: R11 V-02 base with two forced changes: (1) formula
  `/25 * 220`; (2) dual-scope specificity test in VERIFIER TABLE (Question 1 + Question 2
  explicit). Baseline correction: *Why* column updated to "do not restate the criterion
  or paraphrase the evidence" (C-32 PASS). No anchor (C-09 FAIL); general routing (C-28
  PARTIAL). Predicts: C-09 FAIL; C-28 PARTIAL; C-29 PASS.

### Combination selections (V-04, V-05)

- **V-04 (APA + PRR on V-04 R11 base)**: V-04 R11 (C-29 PASS dual-scope, C-30 PASS,
  C-31 PASS, C-32 PASS) with three changes: (1) formula `/25 * 220`; (2) 5-mode anchor
  (C-09 PASS); (3) per-entry routing (C-28 PASS). C-29 and C-32 inherited unchanged.
  Predicts: all 25 aspirational PASS; composite 310/310.

- **V-05 (APR on V-05 R11 full-stack base)**: V-05 R11 (C-09 through C-31 PASS, C-28 PASS
  per-entry, C-29 PASS dual-scope) with two changes: (1) formula `/25 * 220`; (2) *Why*
  field "do not describe the evidence" -> "do not paraphrase the evidence" (C-32 PARTIAL
  -> PASS). Minimum repair: one phrase. Predicts: all 25 aspirational PASS; composite
  310/310.

### Variation matrix

| Variation | Base | C-03 | C-09 | C-28 | C-29 | C-32 |
|-----------|------|------|------|------|------|------|
| V-01 | R11 V-01 + APA | PASS (/25) | PASS (anchor, 5 modes) | PARTIAL (general routing) | FAIL (type-level) | PASS (inherited) |
| V-02 | R11 V-01 + PRR | PASS (/25) | FAIL (no anchor) | PASS (per-entry) | FAIL (type-level) | PASS (inherited) |
| V-03 | R11 V-02 + IRQ | PASS (/25) | FAIL (no anchor) | PARTIAL (general routing) | PASS (dual-scope) | PASS (baseline fix) |
| V-04 | R11 V-04 + APA + PRR | PASS (/25) | PASS (anchor) | PASS (per-entry) | PASS (inherited) | PASS (inherited) |
| V-05 | R11 V-05 + APR | PASS (/25) | PASS (inherited) | PASS (inherited) | PASS (inherited) | PASS (fixed) |

---

## V-01 -- Axis: C-09 Anti-Pattern Anchor on Role-Sequence Base

**Variation axis**: C-09 PASS via anti-pattern anchor on the R11 V-01 bidirectional-gate
role-sequence architecture.

**Hypothesis**: C-09 requires a pre-scoring block naming at least one failure mode with a
typical bad-output example and a closing mechanism, placed before scoring instructions.
V-01 R11 had no such block. Adding a 5-mode anchor satisfies C-09 without altering any
other criterion profile. The anchor is orthogonal to C-28 (operates on PROHIBITED CONTENT
CATEGORIES routing) and to C-29 (operates on VERIFIER specificity test scope). Both
intentionally preserved as PARTIAL and FAIL respectively to isolate the APA axis.

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
            + (aspirational_pass / 25 * 220)
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

## V-02 -- Axis: C-28 Per-Entry Routing on Role-Sequence Base

**Variation axis**: C-28 PASS via per-entry routing annotations in PROHIBITED CONTENT
CATEGORIES on the R11 V-01 role-sequence architecture.

**Hypothesis**: C-28 requires each entry in PROHIBITED CONTENT CATEGORIES to name its
specific ANALYST destination. V-01 R11 had a single general routing statement ("All
prohibited content categories belong in the ANALYST role's PER-OUTPUT NARRATIVE section").
This is C-28 PARTIAL. Converting each entry to carry its own routing annotation (e.g.,
"-- belongs in ANALYST Primary differentiator or Verdict spread") satisfies C-28. The
routing annotations are co-located with the category entries; the group header and
categorical structure (C-25 PASS) is unchanged. No anchor (C-09 FAIL) and no intra-run
question (C-29 FAIL) are preserved to isolate the PRR axis.

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
            + (aspirational_pass / 25 * 220)
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

## V-03 -- Axis: C-29 Intra-Run Specificity on Table-Format Base

**Variation axis**: C-29 PASS via dual-scope specificity test on the R11 V-02 table-dominant
architecture.

**Hypothesis**: C-29 requires the VERIFIER specificity test to explicitly state both the
type-level question and the intra-run question. V-02 R11 stated only Question 1 (type-level).
Adding Question 2 and expanding the VERIFIER TABLE to carry separate Type-level and Intra-run
columns satisfies C-29. This change is orthogonal to C-30 (pair-omission prohibition) and
C-12 (structured schema) -- both inherited from V-02 R11. No anchor (C-09 FAIL) and general
routing (C-28 PARTIAL) preserved to isolate the IRQ axis. Baseline correction: *Why* column
updated to carry both prohibitions for C-32 PASS alignment.

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
            + (aspirational_pass / 25 * 220)
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

For each evidence entry, apply both questions:

  Question 1 -- Type-level: could this evidence apply to any well-designed output of
  this type? YES = type-generic = FAIL.

  Question 2 -- Intra-run: could this evidence apply to a different output in this
  scoring run -- i.e., is this description interchangeable with what was written for
  another output in this batch? YES = run-undifferentiating = FAIL.

Either question answering YES triggers specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive PASS.

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

## V-04 -- Combination: APA + PRR on V-04 R11 Base

**Variation axis**: V-04 R11 base (C-29 PASS dual-scope, C-30 PASS, C-31 PASS, C-32 PASS)
with three changes: (1) formula `/25 * 220`; (2) 5-mode anti-pattern anchor (C-09 PASS);
(3) per-entry routing in PROHIBITED CONTENT CATEGORIES (C-28 PASS).

**Hypothesis**: C-09 and C-28 are mutually orthogonal. C-09 operates on the pre-scoring
anchor block (does a failure-mode list precede scoring?). C-28 operates on the PROHIBITED
CONTENT CATEGORIES routing annotations (does each category entry name its ANALYST
destination?). Adding the anchor does not alter the routing annotations and vice versa.
V-04 R11 already closes C-29 (dual-scope VERIFIER) and C-32 (*Why* with both prohibitions)
-- neither is disturbed by either addition. V-04 R12 is the first non-full-stack variation
expected to score 25/25 aspirational, composite 310/310.

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
            + (aspirational_pass / 25 * 220)
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

DUAL-SCOPE SPECIFICITY TEST

For each evidence entry, apply both questions:

  Question 1 -- Type-level: could this evidence apply to any well-designed output of
  this type? YES = type-generic = FAIL.

  Question 2 -- Intra-run: could this evidence apply to a different output in this
  scoring run -- i.e., is this description identical or near-identical to what was
  written for another output in this batch? YES = run-undifferentiating = FAIL.

Either question answering YES triggers specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive PASS.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from SCORER output above]  (required)
  Type-level specificity: PASS | FAIL -- [reason if FAIL]  (required)
  Intra-run specificity: PASS | FAIL -- [name the other output if FAIL]  (required)
  Specificity result: PASS | FAIL  (required)

If Specificity result is FAIL:
  Revised evidence: [rewrite with structural property unique to this output and not
                     applicable to any other output in this run]  (required)

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

## V-05 -- Axis: C-32 Anti-Paraphrase Fix on V-05 R11 Full-Stack Base

**Variation axis**: C-32 PASS via *Why* field anti-paraphrase fix on the V-05 R11 full-stack
lifecycle architecture.

**Hypothesis**: V-05 R11 scored C-32 PARTIAL because the *Why* field definition read "do not
restate the criterion; do not describe the evidence." "Do not describe the evidence" names
a content type but is not the paraphrase anti-pattern explicitly. C-32 PASS requires both
anti-patterns named at the field definition site: criterion restatement AND evidence
paraphrase. Changing "do not describe the evidence" to "do not paraphrase the evidence"
closes the PARTIAL by making both prohibited modes explicit. This is a one-phrase change;
no other field, schema, anchor entry, routing annotation, or gate is altered. Formula
updated from `/23 * 220` to `/25 * 220` as a forced infrastructure change.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

Execution follows four numbered phases across three roles. Each phase declares its own
precondition. No phase may begin while its precondition is unmet.

---

ANTI-PATTERN ANCHOR -- READ BEFORE PHASE 1

Thirteen structural failure modes are prohibited. Read all thirteen before Phase 1 begins.

FAILURE MODE A -- OMISSION PATH
  Typical output: A criterion block where the verdict matches the baseline has no
  *Change*: field. The omission is invisible -- no structural gap marks the missing field.
  Closed by: Mechanism 1 (mandatory bidirectional *Change* field, always required).

FAILURE MODE B -- FRESH-LOOKUP PATH
  Typical output: [SCORER COMPLETE -- no *Change*: fields written during scoring]
  ANALYST REGRESSION SIGNALS: reviewing baseline to identify verdict changes...
  Closed by: Mechanism 2 (Change Manifest + synthesis re-reading prohibition).

FAILURE MODE C -- MECHANISM-FREE SCORING
  Typical output: *Why*: "The prompt uses a gate token before synthesis." Names
  compliance, not architecture. The mechanism is what the gate does, not that it exists.
  Closed by: Mechanism 3 (mandatory *Why* field requiring structural mechanism).

FAILURE MODE D -- INCOMPLETE SYNTHESIS
  Typical output: LEADERBOARD and EXCELLENCE SIGNALS present; FAILURE PATTERNS and
  REGRESSION SIGNALS absent. No gate token marks synthesis as structurally incomplete.
  Closed by: Mechanism 4 (synthesis gate pair + pre-close checkbox checklist).

FAILURE MODE E -- VERIFIER BYPASS PATH
  Typical output: [SCORER COMPLETE] [VERIFIER COMPLETE -- evidence appeared specific]
  ANALYST begins without a review pass.
  Closed by: Mechanism 5 (dedicated VERIFIER role with structural prerequisite).

FAILURE MODE F -- THIN NARRATIVE PATH
  Typical output: Output V-03: Primary differentiator names one feature. Primary miss:
  absent. Verdict spread: absent.
  Closed by: Mechanism 6 (three-field labeled narrative template).

FAILURE MODE G -- ROLE-SKIP PATH
  Typical output: PHASE 1: SCORING ... PHASE 2: CHANGE MANIFEST ... PHASE 3: SYNTHESIS
  Note: evidence verification omitted -- appeared unnecessary.
  Closed by: Mechanism 7 (named role sequence with inter-role gates).

FAILURE MODE H -- UNIDIRECTIONAL GATE PATH
  Typical output: ROLE 2: VERIFIER // Apply the specificity test to each evidence cell.
  [No "Do not begin until [SCORER COMPLETE]" at role definition site.]
  Closed by: Mechanism 8 (bidirectional gate inscription).

FAILURE MODE I -- UNANNOTATED SCHEMA PATH
  Typical output: SCORER schema lists Verdict and Evidence without "(required)" at label.
  Blank cell not structurally distinguishable from filled cell without a separate audit.
  Closed by: Mechanism 9 (inline "(required)" annotation at every mandatory field label).

FAILURE MODE J -- IMPLICIT PROHIBITION PATH
  Typical output: "No additional fields beyond Verdict and Evidence are permitted."
  A model adding a *Why* field reads this as convention, not a named violation.
  Closed by: Mechanism 10 (named PROHIBITED FIELD LABELS list).

FAILURE MODE K -- UNCHECKED SYNTHESIS PATH
  Typical output: Synthesis closes with [ANALYST COMPLETE]. FAILURE PATTERNS absent.
  No pre-close checklist confirms the missing section.
  Closed by: Mechanism 11 (synthesis gate pair with checkbox pre-close checklist).

FAILURE MODE L -- MIXED-PROHIBITION PATH
  Typical output: FORBIDDEN FIELDS: *Note*, narrative text, evaluative prose, *Comment*
  -- field labels and content categories co-listed in one undifferentiated enumeration.
  A novel field label (*Interpretation*) can be read as not explicitly prohibited.
  Closed by: Mechanism 12 (dual-header: PROHIBITED FIELD LABELS and PROHIBITED CONTENT
  CATEGORIES as separately labeled groups with per-entry ANALYST routing destinations).

FAILURE MODE M -- PASS-CELL OMISSION PATH
  Typical output: VERIFIER TABLE instruction reads "Write one row per failing cell.
  Cells with Specificity PASS may be omitted from this table." Passing evidence cells --
  which may still be non-specific -- escape the specificity test entirely.
  Closed by: Mechanism 13 (explicit named prohibition -- "Do not omit any pair even
  where Specificity appears to PASS -- every criterion-output pair requires a review
  block; a VERIFIER that produces only failing-cell blocks is a schema violation").

---

ROLE 1: SCORER

Do not begin until inputs (rubric file, output files, optional prior-round data) are
confirmed available.

--- PHASE 1: BASELINE LOAD ---
Precondition: inputs confirmed available.

If prior-round score data is provided:
  Step 1. Enumerate all output identifiers.
  Step 2. Enumerate all criterion IDs from the rubric (C-01 through C-NN).
  Step 3. Build a baseline verdict table: rows = criteria, columns = outputs,
          cells = prior verdict (PASS | PARTIAL | FAIL | NO DATA).
  Step 4. Write: "Baseline loaded. [N criteria] x [M outputs] table complete."

If no prior data: write "No prior data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

--- PHASE 2: SCORING ---
Precondition: [PRIOR ROUND LOAD COMPLETE] must appear above before Phase 2 begins.

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA (Mechanisms 1, 3, 9, 10, 12)

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; uniquely identifies
             this output -- fails if it could describe any well-designed output of
             this type, OR if the same description fits another output in this run]
             (required)
  *Why*:    [structural mechanism or design property behind the verdict; name the
             architectural property that produces this verdict; do not restate the
             criterion; do not paraphrase the evidence]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)

*Change* is always required. Exactly three permissible values. The field must be present
whether or not the verdict changed -- conditional omission is a schema violation.

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
*Rationale*, and any field name not in the permitted list. Each is a named schema
violation detectable by field-name inspection. (Mechanism 10)

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER
criterion blocks regardless of field label -- including novel field names a model might
invent. Each entry names its specific ANALYST destination, converting this prohibition
from exclusion-only to routing-aware: (Mechanism 12)

  - evaluative prose         -- belongs in ANALYST Primary differentiator or Verdict spread
  - narrative text           -- belongs in ANALYST PER-OUTPUT NARRATIVE (any labeled field)
  - mechanism analysis       -- belongs in ANALYST Primary differentiator or Primary miss
  - interpretive commentary  -- belongs in ANALYST Primary differentiator or Primary miss
  - synthesis language       -- belongs in ANALYST LEADERBOARD, EXCELLENCE SIGNALS, or
                                FAILURE PATTERNS
  - cross-output comparison  -- belongs in ANALYST LEADERBOARD or EXCELLENCE SIGNALS
  - per-output summaries     -- belongs in ANALYST PER-OUTPUT NARRATIVE (Primary
                                differentiator, Primary miss, or Verdict spread)

No prohibited content category lacks a named destination. Inserting any of the above
content types in a SCORER block is a schema violation regardless of label. (Mechanism 12)

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 25 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs before writing [SCORER COMPLETE].

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above. (Mechanisms 7, 8)

--- PHASE 3: EVIDENCE VERIFICATION --- (Mechanisms 5, 13)
Precondition: [SCORER COMPLETE] must appear above before Phase 3 begins.

The Verifier reviews every evidence entry from Phase 2 and applies the dual-scope
specificity test. ANALYST may not begin until [VERIFIER COMPLETE] appears below.
The Verifier does not modify verdicts, scores, or criterion blocks.

DUAL-SCOPE SPECIFICITY TEST

For each evidence entry, apply both questions:

  Question 1 -- Type-level: could this evidence apply to any well-designed output of
  this type? YES = type-generic = FAIL.

  Question 2 -- Intra-run: could this evidence entry apply to a different output in
  this scoring run -- i.e., is this description identical or near-identical to what
  was written for another output in this batch? YES = run-undifferentiating = FAIL.

Either question answering YES triggers specificity FAIL and requires revision.
Evidence must be both type-specific AND run-differentiating to receive PASS.

VERIFIER REVIEW BLOCK SCHEMA (Mechanisms 5, 9, 13)

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from Phase 2 above]  (required)
  Type-level specificity: PASS | FAIL -- [reason if FAIL]  (required)
  Intra-run specificity: PASS | FAIL -- [name the other output if FAIL]  (required)
  Specificity result: PASS | FAIL  (required)

If Specificity result is FAIL:
  Revised evidence: [rewrite with structural property, verbatim quote, or design
                     decision unique to this output and not applicable to any other
                     output in this run]  (required)

Produce one review block per criterion per output. (Mechanism 13)
Do not omit any pair even where Specificity appears to PASS -- every criterion-output
pair requires a review block. A VERIFIER that produces only failing-cell blocks is a
schema violation. Passing evidence cells may still be non-specific; pre-judging a pair
as PASS does not exempt it from review.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above. (Mechanisms 7, 8)

--- PHASE 4A: CHANGE MANIFEST --- (Mechanism 2)
Precondition: [VERIFIER COMPLETE] must appear above before Phase 4A begins.

Sweep every *Change*: CHANGE from [prior] entry from Phase 2. Omit NO CHANGE and
NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE entries found: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

--- PHASE 4B: SYNTHESIS --- (Mechanisms 4, 11)
Precondition: [CHANGE MANIFEST COMPLETE] must appear above before Phase 4B begins.

PROHIBITION: Do not re-read the baseline table or Phase 2 criterion blocks to derive
regression information. All regression data must come from the Change Manifest in Phase
4A. Any verdict change not recorded inline during Phase 2 is not a detectable regression
in this round. (Mechanism 2)

[SYNTHESIS OPEN]

STEP 1 -- LEADERBOARD

Rank all outputs by composite score descending. Break ties by essential PASS count,
then recommended PASS count.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

STEP 2 -- EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the difference;
          name the design property, not the criterion label]

If no differentiation:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
   detection. Redesign variations for divergence in the next round."

STEP 3 -- FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

STEP 4 -- REGRESSION SIGNALS

From the Change Manifest in Phase 4A only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each step before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR no-differentiation statement written.
  [ ] 3. FAILURE PATTERNS: all zero-PASS criteria identified with diagnosis,
         OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

--- PHASE 4C: PER-OUTPUT NARRATIVE --- (Mechanism 6)
Precondition: [SYNTHESIS COMPLETE] must appear above before Phase 4C begins.

For each scored output: (Mechanisms 6, 9)

  Output [output identifier]:
  Primary differentiator:  [the one structural feature explaining why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism most clearly absent;
                            write "None -- all criteria passed" if all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```

---

## Predicted criterion profile

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Complete verdict matrix | PASS | PASS | PASS | PASS | PASS |
| C-02 Evidence per verdict | PASS | PASS | PASS | PASS | PASS |
| C-03 Formula-correct composite | PASS | PASS | PASS | PASS | PASS |
| C-04 Ranked leaderboard | PASS | PASS | PASS | PASS | PASS |
| C-05 Failure patterns | PASS | PASS | PASS | PASS | PASS |
| C-06 Excellence signals | PASS | PASS | PASS | PASS | PASS |
| C-07 Regression signals | PASS | PASS | PASS | PASS | PASS |
| C-08 Golden threshold per output | PASS | PASS | PASS | PASS | PASS |
| C-09 Anti-pattern anchor | PASS | FAIL | FAIL | PASS | PASS |
| C-10 Synthesis gate pair | PASS | PASS | PASS | PASS | PASS |
| C-11 *Why* field per criterion | PASS | PASS | PASS | PASS | PASS |
| C-12 Structured verification block | PASS | PASS | PASS | PASS | PASS |
| C-13 Inline *Change* annotation | PASS | PASS | PASS | PASS | PASS |
| C-14 Baseline Load gate | PASS | PASS | PASS | PASS | PASS |
| C-15 Mandatory bidirectional *Change* | PASS | PASS | PASS | PASS | PASS |
| C-16 Change Manifest phase | PASS | PASS | PASS | PASS | PASS |
| C-17 Evidence specificity test | PASS | PASS | PASS | PASS | PASS |
| C-18 VERIFIER role with gate | PASS | PASS | PASS | PASS | PASS |
| C-19 Three-field labeled narrative | PASS | PASS | PASS | PASS | PASS |
| C-20 Named role sequence + inter-role gates | PASS | PASS | PASS | PASS | PASS |
| C-21 Bidirectional gate inscription | PASS | PASS | PASS | PASS | PASS |
| C-22 Required-field annotation | PASS | PASS | PASS | PASS | PASS |
| C-23 Field-name exclusion rule | PASS | PASS | PASS | PASS | PASS |
| C-24 Pre-close checklist | PASS | PASS | PASS | PASS | PASS |
| C-25 Content-type schema prohibition | PASS | PASS | PASS | PASS | PASS |
| C-26 Checkbox pre-close | PASS | PASS | PASS | PASS | PASS |
| C-27 Required-field annotation token uniformity | PASS | PASS | PASS | PASS | PASS |
| C-28 Per-category placement routing | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-29 Intra-run specificity | FAIL | FAIL | PASS | PASS | PASS |
| C-30 VERIFIER pair-omission prohibition | PASS | PASS | PASS | PASS | PASS |
| C-31 SCORER Evidence field violation naming | PASS | PASS | PASS | PASS | PASS |
| C-32 SCORER *Why* anti-restatement prohibition | PASS | PASS | PASS | PASS | PASS |

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-04 | 5/5 | 2/2 | 25/25 | 310.0 |
| V-05 | 5/5 | 2/2 | 25/25 | 310.0 |
| V-02 | 5/5 | 2/2 | 23/25 | ~291.6 |
| V-01 | 5/5 | 2/2 | 22.5/25 | ~288.0 |
| V-03 | 5/5 | 2/2 | 22.5/25 | ~288.0 |

Notes:
- V-01 and V-03 tie at 288.0: each has one FAIL and one PARTIAL on the remaining three
  open aspirationals, yielding the same 22.5/25 count from opposite directions.
- V-02 leads the single-axis variations at 291.6: C-28 PASS gains +0.5 over C-28 PARTIAL,
  C-09 FAIL loses -1 vs V-01 C-09 PASS, net 23/25 vs 22.5/25.
- V-04 and V-05 both reach 310. V-04 closes C-09 + C-28 on the dual-scope V-04 R11 base.
  V-05 closes the single C-32 PARTIAL on the full-stack V-05 R11 base. Two paths, same
  ceiling.
- V-05 change delta from R11: one phrase in SCORER Phase 2 *Why* field definition
  ("do not describe the evidence" -> "do not paraphrase the evidence"); one formula
  denominator (23 -> 25). All 13 failure modes, all gate architecture, all routing
  annotations, all schema structures unchanged.
- V-03 C-25: V-02 R11 table format had PROHIBITED CONTENT CATEGORIES with a group header
  ("The following content types are prohibited...") satisfying C-25. The general routing
  statement is a single paragraph after the list -- C-28 PARTIAL (general, not per-entry).
  Unchanged in V-03 R12.
