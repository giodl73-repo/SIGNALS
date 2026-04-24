# quest-score Variations -- Round 10
**Skill**: quest-score
**Rubric**: v9 (N_essential=5, N_recommended=2, N_aspirational=22)
**Date**: 2026-03-15
**Round**: 10

---

## Design logic

### Unachieved ceiling entering R10

R9 V-05 was the full stack against rubric v8 (N_aspirational=20, formula `/20 * 200`).
Rubric v9 adds C-28 (per-category placement routing) and C-29 (intra-run specificity)
and updates the formula to `/22 * 220`. Against v9, the two prior ceiling holders score:

| Variation | Criterion | R9 status | Gap |
|-----------|-----------|-----------|-----|
| R9 V-05 | C-03 | FAIL | Uses `/20 * 200`. v9 requires `/22 * 220`. Wrong denominator and weight. |
| R9 V-05 | C-28 | PARTIAL | General routing statement only: "Narrative and commentary belong exclusively in the Analyst's PER-OUTPUT NARRATIVE section." C-28 requires per-entry routing -- each prohibited category entry must individually name its ANALYST destination. A single general statement does not satisfy C-28. |
| R9 V-05 | C-29 | PASS | VERIFIER asks "could this evidence entry apply to a different output in this scoring run, or to any well-designed output of this type?" Intra-run question present. C-29 PASS. |
| R9 V-04 | C-03 | FAIL | Uses `/20 * 200`. |
| R9 V-04 | C-28 | PASS | Each PROHIBITED CONTENT CATEGORY entry names its ANALYST destination individually: "evaluative prose -- belongs in ANALYST Primary differentiator or Verdict spread". Per-entry granularity. C-28 PASS. |
| R9 V-04 | C-29 | FAIL | VERIFIER asks only the type-level question: "could this evidence apply to any well-designed output of this type?" Intra-run dimension absent. C-29 FAIL. |

**Primary gaps for R10:**
1. **Formula (C-03)**: All R9 variations use `/20 * 200`. v9 requires `/22 * 220`.
2. **C-28 + C-29 combined**: No R9 variation has both. V-04 has C-28 PASS + C-29 FAIL.
   V-05 has C-28 PARTIAL + C-29 PASS. R10 full stack must combine both in one variation.

### Variation axes for R10

Three single-axis variations (V-01 through V-03), two combinations (V-04 and V-05):

| Variation | Axis | C-28 target | C-29 target |
|-----------|------|-------------|-------------|
| V-01 | Role sequence (bidirectional gate inscription) | PARTIAL (general routing) | FAIL (type-level only) |
| V-02 | Output format (table-dominant scoring matrix) | PARTIAL (general routing) | FAIL (type-level only) |
| V-03 | Lifecycle emphasis (numbered phases with phase-level preconditions) | PARTIAL (general routing) | FAIL (type-level only) |
| V-04 | V-01 (role sequence) + C-28 per-entry routing | PASS (per-entry) | FAIL (type-level only) |
| V-05 | V-03 (lifecycle) + C-28 per-entry routing + C-29 intra-run specificity | PASS (per-entry) | PASS (intra-run + type-level) |

---

## V-01 -- Axis: Role Sequence (Bidirectional Gate Inscription)

**Variation axis**: Role sequence -- bidirectional gate inscription at every role
handoff.

**Hypothesis**: Writing each downstream role definition with an explicit "Do not begin
until [gate token] appears above" entry condition closes the role-skipping path that
upstream-only gate declarations leave open. A model reading the VERIFIER definition
sees its entry condition without searching upstream for the gate declaration. The
downstream inscription is the testable artifact; the upstream gate is the token that
satisfies it.

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
            + (aspirational_pass / 22 * 220)
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

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs or
                         "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

The Analyst uses SCORER verdicts and composite scores (substituting VERIFIER revised
evidence where revision occurred) to produce synthesis and per-output narratives.

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

## V-02 -- Axis: Output Format (Table-Dominant Scoring Matrix)

**Variation axis**: Output format -- tabular verdict matrix replaces block-by-block
criterion scoring.

**Hypothesis**: A table-dominant format makes criterion completeness auditable at a
glance: an empty table cell is structurally visible without reading prose blocks. The
matrix structure -- every criterion row must be filled for every scored output -- closes
the row-omission path that sequential block-by-block scoring leaves implicit. A scorer
who skips a row produces a structurally incomplete table, not an invisible omission.

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
            + (aspirational_pass / 22 * 220)
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

Write one row per failing cell. Cells with Specificity PASS may be omitted from this
table.

  | Output | Criterion | Scorer evidence | Specificity | Revised evidence |
  |--------|-----------|-----------------|-------------|------------------|

  Specificity (required): PASS | FAIL
  Revised evidence (required when FAIL): specific structural property unique to this
    output; blank when PASS

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

## V-03 -- Axis: Lifecycle Emphasis (Numbered Phases with Phase-Level Preconditions)

**Variation axis**: Lifecycle emphasis -- every phase carries its own numbered header
and declares its entry precondition at the execution site, not only at the role header.

**Hypothesis**: A role-level entry condition tells a model it cannot begin a role until
a gate token appears. A phase-level precondition repeats this requirement at the specific
execution site. Double-inscription -- role-level AND phase-level -- means a model reading
only the phase header still encounters its entry condition. Phase 2 cannot be reached
without seeing [PRIOR ROUND LOAD COMPLETE]. Phase 4B cannot be reached without seeing
[CHANGE MANIFEST COMPLETE]. The precondition is an environmental constraint at the
execution site, not only a declaration at the role boundary.

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
            + (aspirational_pass / 22 * 220)
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

## V-04 -- Combination: Role Sequence (V-01) + C-28 Per-Entry Routing

**Variation axis**: V-01 role sequence architecture + per-entry placement routing
annotation in PROHIBITED CONTENT CATEGORIES.

**Hypothesis**: The exclusion-without-routing failure path (C-28) remains open when
the prohibition lists categories without naming where each belongs. A scorer who cannot
use evaluative prose in SCORER needs to know which ANALYST section it belongs in --
otherwise the prohibition is a dead end. Adding "evaluative prose -- belongs in ANALYST
Primary differentiator or Verdict spread" converts each prohibition from exclusion-only
to routing-aware. Every prohibited content type becomes a redirect, not a wall.

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
is scored. Rows = criterion IDs. Columns = output identifiers. Cells = prior verdict.

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
             architectural property; do not restate the criterion or paraphrase evidence]
             (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [reason]
          | NO PRIOR DATA  (required)

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.

PROHIBITED FIELD LABELS: *Note*, *Comment*, *Observation*, *Context*, *Interpretation*,
and any field name not in the permitted list. Inserting a field with a prohibited label
is a named schema violation detectable by field-name inspection.

PROHIBITED CONTENT CATEGORIES: The following content types are prohibited in SCORER
criterion blocks regardless of field label -- including novel field names a model might
invent. Each entry names the specific ANALYST section where that content type belongs,
converting this prohibition from exclusion-only to routing-aware:

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
content types in a SCORER block is a schema violation regardless of label.

No criterion may be skipped. (required: no cell may be blank)
No Evidence, *Why*, or *Change* field may be blank.

After all criteria for one output:

  essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
  recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
  aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 2 * 30)
            + (aspirational_pass / 22 * 220)
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

## V-05 -- Full Stack R10: Lifecycle (V-03) + C-28 Per-Entry Routing + C-29 Intra-Run Specificity

**Variation axis**: V-03 lifecycle (numbered phases, phase-level preconditions) +
C-28 per-entry routing annotation + C-29 dual-scope specificity test.

**Hypothesis**: C-28 and C-29 are mutually orthogonal -- C-28 operates on the SCORER
schema (per-entry routing in PROHIBITED CONTENT CATEGORIES) and C-29 operates on the
VERIFIER specificity test (adding the intra-run question to the type-level question).
No R9 variation combined both. This variation inherits V-03's numbered-phase lifecycle
for double-inscription gate compliance, adds V-04's per-entry routing for C-28 PASS,
and adds the R9 V-05 intra-run specificity question ("could this entry apply to a
different output in this scoring run?") for C-29 PASS. The formula is updated to
`/22 * 220`. Expected to be the first variation scoring PASS on both C-28 and C-29.

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

Twelve structural failure modes are prohibited. Read all twelve before Phase 1 begins.

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

---

ROLE 1: SCORER

Do not begin until inputs (rubric file, output files, optional prior-round data) are
confirmed available.

--- PHASE 1: BASELINE LOAD ---
Precondition: inputs confirmed available.

If prior-round score data is provided:
  Step 1. Enumerate all output identifiers.
  Step 2. Enumerate all criterion IDs from the rubric.
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
            + (aspirational_pass / 22 * 220)
            = [result]  (required)

  Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
       |  NO  -- [which essential failed, or composite < 80]

Score all N outputs before writing [SCORER COMPLETE].

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above. (Mechanisms 7, 8)

--- PHASE 3: EVIDENCE VERIFICATION --- (Mechanism 5)
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

VERIFIER REVIEW BLOCK SCHEMA (Mechanisms 5, 9)

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from Phase 2 above]  (required)
  Type-level specificity: PASS | FAIL -- [reason if FAIL]  (required)
  Intra-run specificity: PASS | FAIL -- [name the other output if FAIL]  (required)
  Specificity result: PASS | FAIL  (required)

If Specificity result is FAIL:
  Revised evidence: [rewrite with structural property, verbatim quote, or design
                     decision unique to this output and not applicable to any other
                     output in this run]  (required)

Produce one review block per criterion per output. No block may be omitted.

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
