# quest-score Variations -- Round 11
**Skill**: quest-score
**Rubric**: v10 (N_essential=5, N_recommended=2, N_aspirational=23)
**Date**: 2026-03-15
**Round**: 11

---

## Design logic

### Unachieved ceiling entering R11

R10 V-05 was the full stack against rubric v9 (N_aspirational=22, formula `/22 * 220`).
Rubric v10 adds C-30 (VERIFIER pair-omission prohibition) and updates the formula to
`/23 * 220`. Against v10, the R10 ceiling holders score:

| Variation | Criterion | R10 status | Gap |
|-----------|-----------|------------|-----|
| R10 V-05 | C-03 | FAIL | Uses `/22 * 220`. v10 requires `/23 * 220`. Wrong denominator produces incorrect composite. |
| R10 V-05 | C-30 | PARTIAL | "Produce one review block per criterion per output. No block may be omitted." Positive coverage mandate satisfies C-12 but does not name the PASS-cell skip pattern as a prohibited deviation. C-30 requires explicit named prohibition: "Do not omit any pair even where Specificity appears to PASS." |
| R10 V-04 | C-03 | FAIL | Uses `/22 * 220`. |
| R10 V-04 | C-30 | PARTIAL | Same: positive mandate without explicit skip-prohibition. |
| R10 V-01 | C-03 | FAIL | Uses `/22 * 220`. |
| R10 V-01 | C-30 | PARTIAL | "For every output, for every criterion, produce one review block." Positive mandate only. |
| R10 V-02 | C-03 | FAIL | Uses `/22 * 220`. |
| R10 V-02 | C-30 | FAIL | Explicit permission: "Write one row per failing cell. Cells with Specificity PASS may be omitted." |
| R10 V-03 | C-03 | FAIL | Uses `/22 * 220`. |
| R10 V-03 | C-30 | PARTIAL | "Produce one review block per criterion per output. No block may be omitted." Positive mandate only. |

**Primary gap for R11:** C-30 is the single criterion where all R10 variations score PARTIAL
or FAIL. V-02 R10 demonstrates the worst case: explicit PASS-cell omission permission makes
passing evidence cells -- which may still be non-specific -- invisible to the specificity
test. V-01 R10 demonstrates the near-miss: a positive coverage mandate satisfies C-12 but
leaves the explicit-exception path open. C-30 requires naming the skip anti-pattern as a
prohibited deviation. Formula update is a forced infrastructure change.

**Secondary diagnostic:** Can the explicit prohibition be grafted onto three different base
architectures (role sequence, table format, lifecycle phases) without disturbing existing
compliance profiles? V-01, V-02, V-03 isolate C-30 on each base. V-04 adds C-29 intra-run
specificity to V-01 R11. V-05 assembles the full stack.

### New axis for R11

| Axis | Label | Mechanism | Target criteria |
|------|-------|-----------|-----------------|
| PRH | Pair-omission prohibition | Add explicit named prohibition: "Do not omit any pair even where Specificity appears to PASS -- every criterion-output pair requires a review block; a VERIFIER that skips PASS-judged pairs is a schema violation." C-30 follows C-15 over C-13: a positive mandate leaves the exception path open; an explicit prohibition names the anti-pattern as a violation. | C-30 |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (PRH on role-sequence base)**: R10 V-01 base (bidirectional gate inscription,
  positive coverage mandate, type-level specificity only, general routing statement) with
  two forced changes: (1) formula `/23 * 220`; (2) add explicit PRH prohibition after
  "For every output, for every criterion, produce one review block." Predicts: C-30 PASS
  (explicit prohibition present); C-29 FAIL (no intra-run question); C-28 PARTIAL (general
  routing statement inherited); C-03 PASS (formula updated). All other R10 V-01 verdicts
  inherited.

- **V-02 (PRH on table-format base)**: R10 V-02 base (table-dominant VERIFIER, SCORER per-
  output table, type-level specificity only) with two forced changes: (1) formula `/23 *
  220`; (2) replace "Write one row per failing cell. Cells with Specificity PASS may be
  omitted" with "Write one row per criterion per output" PLUS explicit PRH prohibition.
  Minimum repair to a C-30 FAIL: removing the explicit permission and adding the explicit
  prohibition. Predicts: C-30 PASS; C-12 PASS (table schema unchanged); C-29 FAIL
  (type-level only); C-28 PARTIAL (general routing inherited); C-03 PASS.

- **V-03 (PRH on lifecycle-phase base)**: R10 V-03 base (numbered phases, double
  inscription, type-level specificity only) with two forced changes: (1) formula `/23 *
  220`; (2) add explicit PRH prohibition to Phase 3 after "Produce one review block per
  criterion per output. No block may be omitted." Predicts: C-30 PASS (explicit
  prohibition); C-29 FAIL (type-level only); C-28 PARTIAL (general routing); C-03 PASS.
  All other R10 V-03 verdicts inherited.

### Combination selections (V-04, V-05)

- **V-04 (PRH + IRQ)**: V-01 R11 base (C-30 PASS, formula /23) PLUS IRQ: add the intra-run
  specificity question to the VERIFIER. Specificity test becomes dual-scope: (1) type-level
  and (2) intra-run. VERIFIER REVIEW BLOCK SCHEMA gains Type-level specificity and Intra-run
  specificity as separate labeled fields plus a combined Specificity result. Predicts: C-30
  PASS; C-29 PASS (both questions present); C-28 PARTIAL (general routing unchanged); C-03
  PASS. Composite ceiling above V-01 R11 by one aspirational PASS.

- **V-05 (Full stack R11)**: R10 V-05 full-stack architecture with all R11 changes: (1)
  formula `/23 * 220`; (2) explicit PASS-cell omission prohibition in VERIFIER Phase 3;
  (3) Failure Mode M (PASS-cell omission path) + Mechanism 13; (4) baseline table extended
  to C-30. C-29 dual-scope specificity and C-28 per-entry routing inherited from R10 V-05
  unchanged. Predicts: all C-01 through C-30 PASS; composite 310/310.

### Variation matrix

| Variation | Base | C-03 | C-28 | C-29 | C-30 |
|-----------|------|------|------|------|------|
| V-01 | R10 V-01 + PRH | PASS (/23) | PARTIAL | FAIL (type-level) | PASS (explicit prohibition) |
| V-02 | R10 V-02 + PRH | PASS (/23) | PARTIAL | FAIL (type-level) | PASS (explicit prohibition) |
| V-03 | R10 V-03 + PRH | PASS (/23) | PARTIAL | FAIL (type-level) | PASS (explicit prohibition) |
| V-04 | V-01 R11 + IRQ | PASS (/23) | PARTIAL | PASS (dual-scope) | PASS (explicit prohibition) |
| V-05 | R10 V-05 + PRH + formula | PASS (/23) | PASS (per-entry) | PASS (dual-scope) | PASS (explicit prohibition) |

---

## V-01 -- Axis: C-30 Explicit Prohibition on Role-Sequence Base

**Variation axis**: C-30 PASS via explicit pair-omission prohibition on the R10 V-01
bidirectional-gate role-sequence architecture.

**Hypothesis**: The single change required to advance R10 V-01 from C-30 PARTIAL to PASS
is adding an explicit named prohibition at the VERIFIER coverage instruction site. The
positive mandate "For every output, for every criterion, produce one review block" satisfies
C-12 but leaves the PASS-cell skip path open. Adding "Do not omit any pair even where
Specificity appears to PASS -- a VERIFIER that skips PASS-judged pairs is a schema
violation" closes that path by naming the anti-pattern as a violation detectable at the
instruction site without restructuring the role architecture.

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
             type]  (required)
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
            + (aspirational_pass / 23 * 220)
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

## V-02 -- Axis: C-30 Explicit Prohibition on Table-Format Base

**Variation axis**: C-30 PASS via explicit pair-omission prohibition on the R10 V-02
table-dominant architecture; minimum repair to a C-30 FAIL output.

**Hypothesis**: R10 V-02 explicitly authorized PASS-cell omission: "Write one row per
failing cell. Cells with Specificity PASS may be omitted." This is C-30 FAIL -- the
explicit permission is the failure, not the table schema structure. The minimum repair
is two operations: (1) remove "Cells with Specificity PASS may be omitted" and (2) add
the explicit prohibition targeting that pattern by name. C-12 compliance (labeled fields
covering every pair) is orthogonal to the coverage instruction change and should be
unaffected. This tests whether a C-30 FAIL can be converted to C-30 PASS without any
structural change to the table schema itself.

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
    the architectural property; do not restate the criterion text
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
            + (aspirational_pass / 23 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier scans every Evidence cell in every scoring table and applies the specificity
test. The ANALYST role may not begin until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = FAIL = cell must be revised before this role can close.

VERIFIER TABLE

Write one row per criterion per output -- covering every criterion-output pair.
Do not omit any pair even where Specificity appears to PASS. A VERIFIER that skips
PASS-judged pairs is a schema violation; passing evidence cells may still be non-specific.

  | Output | Criterion | Scorer evidence | Specificity | Revised evidence |
  |--------|-----------|-----------------|-------------|------------------|

  Specificity (required): PASS | FAIL
  Revised evidence (required when FAIL): specific structural property unique to this
    output; write N/A when Specificity is PASS

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

## V-03 -- Axis: C-30 Explicit Prohibition on Lifecycle-Phase Base

**Variation axis**: C-30 PASS via explicit pair-omission prohibition on the R10 V-03
numbered-phase lifecycle architecture with double-inscription gate preconditions.

**Hypothesis**: The numbered-phase architecture inscribes gate preconditions at both
the role header and the phase header ("Do not begin until [SCORER COMPLETE]" at ROLE 2
definition AND "Precondition: [SCORER COMPLETE] must appear above before Phase 3 begins"
at Phase 3 header). The C-30 prohibition can be inserted inside Phase 3's coverage
instruction without altering either inscription. This tests whether the prohibition
survives double-inscription: the phase-level precondition is an entry condition (when
may Phase 3 begin?); the PRH prohibition is a coverage rule (what must Phase 3 produce?).
They operate on different dimensions and should not interfere.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism explanation, a composite
score, and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, regression signals, and per-output narrative notes.

Execution follows four numbered phases across three roles. Each phase declares its own
precondition. No phase may begin while its precondition is unmet.

---

ROLE 1: SCORER

Do not begin until inputs (rubric file, output files, optional prior-round data) are
confirmed available.

--- PHASE 1: BASELINE LOAD ---
Precondition: inputs confirmed available.

If prior-round score data is provided:
  Step 1. Enumerate all output identifiers (V-01, V-02, ..., V-NN).
  Step 2. Enumerate all criterion IDs from the rubric (C-01 through C-NN).
  Step 3. Build a baseline verdict table: rows = criteria, columns = outputs,
          cells = prior verdict (PASS | PARTIAL | FAIL | NO DATA).
  Step 4. Write: "Baseline loaded. [N criteria] x [M outputs] table complete."

If no prior data: write "No prior data. *Change* fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

--- PHASE 2: SCORING ---
Precondition: [PRIOR ROUND LOAD COMPLETE] must appear above before Phase 2 begins.

For each output, score every criterion in the rubric in sequence.

SCORER CRITERION BLOCK SCHEMA

Every criterion block consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output; uniquely identifies
             this output -- fails if it could describe any well-designed output of
             this type]  (required)
  *Why*:    [structural mechanism or design property behind the verdict; name the
             architectural property; do not restate the criterion]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Rationale*, and
any field name not in the permitted list. Each is a named schema violation detectable
by field-name inspection.

PROHIBITED CONTENT CATEGORIES: the following content types are prohibited in SCORER
criterion blocks regardless of field label, including novel labels a model might invent:
  - evaluative prose
  - narrative text
  - interpretive commentary
  - mechanism analysis (beyond the structural property in *Why*)
  - synthesis language
  - cross-output comparison
  - per-output summaries

All prohibited content categories belong in the ANALYST PER-OUTPUT NARRATIVE section.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 23 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs before writing [SCORER COMPLETE].

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

--- PHASE 3: EVIDENCE VERIFICATION ---
Precondition: [SCORER COMPLETE] must appear above before Phase 3 begins.

The Verifier reviews every evidence entry from Phase 2 and applies the specificity test.
ANALYST may not begin until [VERIFIER COMPLETE] appears below. The Verifier does not
modify verdicts, scores, or criterion blocks.

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = specificity FAIL = revision required.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from Phase 2 output above]  (required)
  Specificity: PASS | FAIL  (required)

If Specificity is FAIL:
  Revised evidence: [specific structural property unique to this output]  (required)

Produce one review block per criterion per output. No block may be omitted.
Do not omit any pair even where Specificity appears to PASS -- every criterion-output
pair requires a review block. Pre-judging a pair as PASS does not exempt it from review;
passing evidence cells may still be non-specific. A VERIFIER that produces only failing-
cell blocks is a structural error regardless of schema correctness.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

--- PHASE 4A: CHANGE MANIFEST ---
Precondition: [VERIFIER COMPLETE] must appear above before Phase 4A begins.

Sweep every *Change*: CHANGE from [prior] entry from Phase 2. Omit NO CHANGE and
NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason |  (required)
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE entries found: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

--- PHASE 4B: SYNTHESIS ---
Precondition: [CHANGE MANIFEST COMPLETE] must appear above before Phase 4B begins.

PROHIBITION: Do not re-read the baseline table or Phase 2 criterion blocks to derive
regression information. All regression data must come from the Change Manifest in
Phase 4A. Any verdict change not recorded inline during Phase 2 is not a detectable
regression in this round.

[SYNTHESIS OPEN]

STEP 1 -- LEADERBOARD

Rank all outputs by composite score descending. Break ties by essential PASS count,
then recommended PASS count.

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

STEP 2 -- EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism; name the design
          property, not the criterion label]

If no differentiation: "No differentiating excellence signals detected this round."

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
         mechanism, OR explicit no-differentiation statement.
  [ ] 3. FAILURE PATTERNS: all zero-PASS criteria identified with diagnosis,
         OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

--- PHASE 4C: PER-OUTPUT NARRATIVE ---
Precondition: [SYNTHESIS COMPLETE] must appear above before Phase 4C begins.

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

## V-04 -- Combination: Role Sequence (V-01 R11) + C-29 Intra-Run Specificity

**Variation axis**: V-01 R11 base (C-30 PASS via explicit prohibition, formula /23) PLUS
IRQ: add the intra-run specificity question to the VERIFIER dual-scope test for C-29 PASS.

**Hypothesis**: C-30 and C-29 are mutually orthogonal. C-30 operates on the VERIFIER
coverage instruction (explicit prohibition on omitting PASS-judged pairs). C-29 operates
on the VERIFIER specificity test formulation (adding the intra-run question to the type-
level question). A prompt can pass C-30 while failing C-29 -- V-01 R11 demonstrates this.
Adding the intra-run question requires extending the VERIFIER REVIEW BLOCK SCHEMA with
separate Type-level specificity and Intra-run specificity result fields plus a combined
Specificity result field. The PRH prohibition text is unchanged because coverage (how many
pairs) is independent of test scope (how many questions per pair). The only schema change
is at the test formulation site; the coverage instruction remains structurally identical.

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
             type, OR if the same description fits another output in this run]  (required)
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
            + (aspirational_pass / 23 * 220)
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

## V-05 -- Full Stack R11: Lifecycle (V-03) + C-30 Explicit Prohibition + Formula /23

**Variation axis**: R10 V-05 full-stack architecture with all R11 changes: (1) formula
`/23 * 220`; (2) explicit PASS-cell omission prohibition in VERIFIER Phase 3 (C-30 PASS);
(3) Failure Mode M (PASS-cell omission path) + Mechanism 13; (4) baseline table reference
extended to C-30. C-29 dual-scope specificity and C-28 per-entry routing are inherited
from R10 V-05 unchanged.

**Hypothesis**: C-30 is mutually orthogonal to C-29 and C-28. C-30 operates on the
VERIFIER coverage instruction; C-29 operates on the VERIFIER specificity test formulation;
C-28 operates on the SCORER prohibition block. Adding the explicit PRH prohibition and
Failure Mode M to R10 V-05 achieves C-30 PASS without disturbing C-29 PASS or C-28 PASS.
The formula fix is the only forced infrastructure change. This variation is the first
expected to score PASS on all 30 criteria simultaneously.

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
  which may still be non-specific -- escape the specificity test entirely. A scorer who
  writes generic evidence for an output pre-judged PASS is never challenged.
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
             criterion; do not describe the evidence]  (required)
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
            + (aspirational_pass / 23 * 220)
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
| C-09 Anti-pattern anchor | FAIL | FAIL | FAIL | FAIL | PASS |
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
| C-28 Per-category placement routing | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS |
| C-29 Intra-run specificity | FAIL | FAIL | FAIL | PASS | PASS |
| C-30 VERIFIER pair-omission prohibition | PASS | PASS | PASS | PASS | PASS |

Notes:
- V-02 C-20 and C-21: V-02 has a role sequence structure (ROLE 1/2/3) with bidirectional
  "Do not begin until" at each role header, satisfying both. No ROLE SEQUENCE diagram at
  the top differs from V-01 but inter-role gates are present.
- V-02 C-28: General routing statement "All prohibited content types belong in the ANALYST
  PER-OUTPUT NARRATIVE section" is PARTIAL (not per-entry). Same as V-01, V-03, V-04.
- V-01/V-04 C-09: No anti-pattern anchor -- these follow the R10 V-01/V-04 architecture
  which omitted the anchor. C-09 FAIL is intentional to maintain single-axis design.

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-05 | 5/5 | 2/2 | 23/23 | 310.0 |
| V-04 | 5/5 | 2/2 | 22/23 | ~300.4 |
| V-01 | 5/5 | 2/2 | 21/23 | ~290.9 |
| V-03 | 5/5 | 2/2 | 21/23 | ~290.9 |
| V-02 | 5/5 | 2/2 | 21/23 | ~290.9 |
