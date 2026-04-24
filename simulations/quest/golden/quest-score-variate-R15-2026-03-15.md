# Quest Score -- Round 15 Variations
**Skill**: quest-score
**Rubric**: v14 (C-01--C-05 essential, C-06--C-07 recommended, C-08--C-41 aspirational; denominator /34)
**Scoring context**: quest-rubric outputs (N_essential=4, N_recommended=3, N_aspirational=25)
**Date**: 2026-03-15
**Round**: 15

---

## Design logic

### Unachieved ceiling entering R15

| Criterion | R14 V-01 status | Gap analysis |
|-----------|-----------------|--------------|
| C-35 | FAIL | VERIFIER per-cell table has a single "Audit A" column. Conditions (a) and (b) inside AUDIT A are the two specificity questions, but they share a column; no structural separation exists. C-35 requires Q1-TypeLevel and Q2-IntraRun as independently auditable labeled columns or fields. The column-merge path is the one remaining bypass. |

### R15 variation axes

| Axis | Label | Mechanism |
|------|-------|-----------|
| DC | Dual-column VERIFIER table | Per-cell table gains Q1-TypeLevel and Q2-IntraRun as separate labeled columns; anchor block pre-states both questions as individually labeled verbatim entries; per-cell entries carry "per Q1 above" / "per Q2 above" reference. Closes C-35 via column separation. |
| PP | Specificity pre-pass phase | SPECIFICITY PRE-PASS section before per-cell review builds TYPE-LEVEL SCAN TABLE and INTRA-RUN SCAN TABLE as distinct named phase artifacts. Per-cell table keeps single combined "Specificity" column referencing pre-pass tables. Tests whether phase-artifact separation satisfies C-35 without per-cell column separation. |
| OR | Operational-register phrasing | VERIFIER uses directive scan labels ("TYPE-GENERICITY SCAN:" / "RUN-DUPLICATE SCAN:") with crisp imperative language. Both scans folded into a single per-cell "Specificity-Scan" block. No structural column separation. Tests whether phrasing clarity without structural separation satisfies C-35. |

### Single-axis selections

- **V-01 (DC)**: Dual-column VERIFIER table + anchor block. 5-column consolidated register from R14 best. YES-only gate rule. BOTH...AND + prohibition synthesis gate. Predicts: C-35 PASS.
- **V-02 (PP)**: Specificity pre-pass phase builds two separate scan registers. Per-cell table keeps single combined Specificity column. Same base as V-01 for all other structure. Predicts: C-35 PARTIAL -- structural separation exists at phase level but not at per-cell schema column level.
- **V-03 (OR)**: Operational-register phrasing. Single per-cell Specificity-Scan field. No anchor block. No column separation. Predicts: C-35 FAIL -- directive phrasing does not substitute for structural separation.

### Combination selections

- **V-04 (DC + PP)**: Pre-pass TYPE-LEVEL and INTRA-RUN registers + dual-column per-cell table. Double enforcement at both phase level and cell level. Predicts: C-35 PASS.
- **V-05 (DC + PP + role)**: V-04 + dedicated SPECIFICITY AUDITOR role between ANALYST and VERIFIER, with gate SPECIFICITY AUDIT COMPLETE. VERIFIER entry condition quotes the gate verbatim. Predicts: C-35 PASS with added independent-audit property.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Dual-column per-cell (Q1-TypeLevel, Q2-IntraRun) | YES | NO | NO | YES | YES |
| Anchor block (Q1/Q2 labeled verbatim pre-statement) | YES | NO | NO | YES | YES |
| Specificity pre-pass phase (separate scan registers) | NO | YES | NO | YES | YES |
| Dedicated SPECIFICITY AUDITOR role | NO | NO | NO | NO | YES |
| SPECIFICITY AUDIT COMPLETE gate | NO | NO | NO | NO | YES |
| Single combined Specificity field | NO | YES | YES | NO | NO |
| Operational-register phrasing | NO | NO | YES | NO | NO |
| 5-column consolidated register (YES-only gate) | YES | YES | YES | YES | YES |
| BOTH...AND + prohibition synthesis gate | YES | YES | YES | YES | YES |
| Formula /4, /3, /25 inscribed inline (C-39) | YES | YES | YES | YES | YES |
| *Why* field per criterion (C-11) | YES | YES | YES | YES | YES |
| *Change* field mandatory (C-15) | YES | YES | YES | YES | YES |
| CHANGE MANIFEST phase (C-16) | YES | YES | YES | YES | YES |
| Pre-close checklist with checkboxes (C-24, C-26) | YES | YES | YES | YES | YES |
| Tie-break protocol at leaderboard definition (C-41) | YES | YES | YES | YES | YES |

---

## V-01 -- Axis DC: Dual-column VERIFIER table

**Variation axis**: Output format -- the VERIFIER per-cell table separates Audit A
into two structurally distinct labeled columns: Q1-TypeLevel (type-level specificity
question) and Q2-IntraRun (intra-run duplicate question). A named ANCHOR REVIEW BLOCK
pre-states both questions as individually labeled verbatim entries before the first
per-cell row. Per-cell entries carry "per Q1 above" and "per Q2 above" references.

**Hypothesis**: C-35 PASS -- two independently auditable labeled columns satisfy the
structural separation requirement; C-37 PASS inherited and strengthened by explicit
"per Q1 above" / "per Q2 above" references in the per-cell schema. No per-cell drift
path is open because both questions are locked to verbatim anchor entries. All other
R14 V-01 PASSes preserved; C-35 is the single changed axis.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

PRIOR ROUND LOAD

Load prior-round verdicts before scoring begins.

| Variation | Open aspirationals entering this round |
|-----------|----------------------------------------|
| V-01 R14  | C-35 FAIL                              |
| V-02 R14  | new in this round                      |
| V-03 R14  | new in this round                      |
| V-04 R14  | new in this round                      |
| V-05 R14  | new in this round                      |

[PRIOR ROUND LOAD COMPLETE]

---

ANTI-PATTERN ANCHOR

The following failure modes appear before scoring begins. Each failure mode is
paired with a dedicated closing mechanism that names the criterion ID enforcing
the close. This anchor enables bidirectional lookup: failure mode -> mechanism
-> criterion ID.

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output addresses this criterion by including the required
  structure." [applies to any well-designed output of this type]
  Closing mechanism: C-40 requires the evidence field definition at the schema
  definition site to name cross-type genericity as a named disqualifying pattern;
  C-02 PASS alone does not close generic evidence.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: The same evidence sentence appears in two different outputs'
  cells for the same criterion, with only the output identifier changed.
  Closing mechanism: C-40 requires the evidence field definition to name
  cross-output duplication within the run as a second disqualifying pattern;
  a cross-type anchor alone leaves intra-run duplication undetected.

Failure Mode C -- Silent arithmetic
  Typical output: Composite score is given as "87.3" with no formula expression
  at the scoring site.
  Closing mechanism: C-39 requires the formula with all parameters (denominator,
  weights, counts) to be inscribed inline at the calculation site; C-03 PASS
  does not require inline formula inscription.

Failure Mode D -- Combined specificity field
  Typical output: VERIFIER per-cell table has a single "Audit A" or "Specificity"
  column in which both the type-level and intra-run questions are answered in
  one merged cell.
  Closing mechanism: C-35 requires Q1-TypeLevel and Q2-IntraRun as structurally
  separated labeled columns in the per-cell schema; C-29 PASS (both questions
  stated) does not require column separation.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: LEADERBOARD section breaks ties in synthesis prose with no
  protocol inscribed at the definition site; ties may be broken differently
  across runs.
  Closing mechanism: C-41 requires the tie-break protocol with named secondary
  and tertiary dimensions to be inscribed at the leaderboard definition site;
  C-04 PASS (ranked leaderboard, ties broken or noted) does not require an
  inscribed protocol.

---

ROLE DEPENDENCY MANIFEST

| Role            | Requires                                                                                             | Produces                    | Domain (ONLY)                                                                                               | Cannot Check                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| JUDGE           | [PRIOR ROUND LOAD COMPLETE]                                                                          | [JUDGE STANDARD COMPLETE]   | ACCEPTABLE/UNACCEPTABLE pairs; separating property declarations; CONSOLIDATED PRODUCTION-TIME REGISTER      | Scoring verdicts; format compliance; diagnostic content quality               |
| ANALYST         | [JUDGE STANDARD COMPLETE]                                                                            | [ANALYST COMPLETE]          | Per-criterion scoring; evidence cells; composite; golden; *Why* field; *Change* field; Present/Absent cols  | Evidence quality standards (Judge); format auditing (Verifier)                |
| CHANGE MANIFEST | [ANALYST COMPLETE]                                                                                   | [CHANGE MANIFEST COMPLETE]  | Sweep all *Change*: CHANGE annotations into manifest table                                                  | Re-scoring; re-auditing                                                       |
| VERIFIER        | [ANALYST COMPLETE]                                                                                   | [VERIFIER COMPLETE]         | Format presence: Q1-TypeLevel and Q2-IntraRun per cell; Present/Absent non-emptiness on PARTIAL rows        | Content quality (Confirmer); evidence standards (Judge)                       |
| CONFIRMER       | [VERIFIER COMPLETE]                                                                                  | [CONFIRMATION COMPLETE]     | Content quality: do Present_mechanism and Absent_mechanism cells name specific structural properties?       | Format presence (Verifier); scoring verdicts (Analyst)                        |
| SYNTHESIS       | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output)           | Leaderboard; excellence signals; failure patterns; regression signals                                       | Re-scoring; re-auditing                                                       |

A row with any blank cell is a structural gap. No role may begin unless its
Requires entry appears in the output above.

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin without [ANALYST COMPLETE] above.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Holding any one or two tokens
    does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy this
    gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32, produce a Judge standard entry:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase drawn from an
               actual provided output satisfying this criterion; the 'from
               [Output-N]:' prefix annotation is required on every ACCEPTABLE
               entry -- a missing prefix is a structural violation blocking
               CONSOLIDATED PRODUCTION-TIME REGISTER completion]"
  UNACCEPTABLE: "[text from a provided output, or a representative generic
                 statement that would fail -- drawn from provided inputs]"
  Separating property: [mechanism A] vs [mechanism B]
    -- single labeled declaration; mechanism present in ACCEPTABLE and absent
       in UNACCEPTABLE; expressed as named poles separated by "vs"; not prose

Before issuing [JUDGE STANDARD COMPLETE], produce the CONSOLIDATED
PRODUCTION-TIME REGISTER. This register is the single inspectable artifact
for all JUDGE production-time obligations. No production-time obligation
in this design may be tracked outside this register.

CONSOLIDATED PRODUCTION-TIME REGISTER

Gate rules:
  - Every cell in every required column must contain YES.
  - A blank cell OR a NO cell in any required column blocks [JUDGE STANDARD
    COMPLETE]. Only YES is a passing cell value. A row with NO in any column
    is incomplete and blocks [JUDGE STANDARD COMPLETE] until corrected.

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-02      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-03      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-04      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-05      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-06      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-07      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-08      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-09      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-10      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-11      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-12      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-13      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-14      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-15      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-16      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-17      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-18      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-19      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-20      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-21      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-22      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-23      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-24      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-25      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-26      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-27      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-28      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-29      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-30      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-31      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-32      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |

All 32 rows must show YES in all three columns before [JUDGE STANDARD COMPLETE]
may be issued.

[JUDGE STANDARD COMPLETE]

---

ROLE 2: ANALYST

Domain: Per-criterion scoring; evidence cells; composite computation; *Why* field;
*Change* field; Present_mechanism and Absent_mechanism columns (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

Before writing any evidence cell, verify it against the Judge's
ACCEPTABLE/UNACCEPTABLE pair. If your draft resembles the UNACCEPTABLE pattern,
rewrite before entering the cell.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                          | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|----------------------------------------------|-------------------|------------------|
  | C-01 | [name]    | E  | PASS/PARTIAL/FAIL | [specific evidence grounded in this output]  | --                | --               |

  Evidence field violations (stated at this definition site):
    Disqualifying pattern 1: evidence could describe any well-designed output
      of this type (cross-type genericity) -- trigger a rewrite before filing
    Disqualifying pattern 2: the same description fits another output in this
      run without modification (cross-output duplication) -- trigger a rewrite
    Both disqualifying patterns are named here; either one is a cell violation.

  Per-row annotations (required for EVERY row; blank is a structural violation):
    *Why* (required): [structural mechanism or design property driving the verdict;
                       a criterion restatement or evidence paraphrase is a violation]
    *Change* (required): exactly one of three values:
      NO CHANGE
      CHANGE from [prior verdict]: [reason]
      NO PRIOR DATA

  PARTIAL row additions (required only on PARTIAL verdicts):
    Present_mechanism (required): [specific structural element, mechanism, role,
      gate token, or design property present that prevented FAIL; a generic quality
      phrase is a structural violation]
    Absent_mechanism (required): [specific structural element, mechanism, role,
      gate token, or design gap absent that prevented PASS; a criterion restatement
      is a structural violation]
    A blank Present_mechanism or Absent_mechanism on a PARTIAL row is a structural
    violation equivalent to a blank evidence cell.

  Composite computation (required -- formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [which essential failed, or composite < 80]

  Per-output narrative (required -- three labeled fields):
    Primary differentiator (required): [the structural feature explaining why
      this output scored differently from others in this run]
    Primary miss (required): [the criterion or structural mechanism most clearly
      absent from this output]
    Verdict spread (required): [where this output concentrated its points and why]

PROHIBITED CONTENT CATEGORIES (no cell, annotation, or narrative field may
contain any item in this list):

  A. Evaluative prose -- quality assessment without naming a structural element
     Route: rewrite as structural observation with named mechanism
  B. Criterion restatement -- text that rephrases the criterion label as evidence
     Route: rewrite using a structural feature observable in the output
  C. Cross-output generic text -- same sentence could appear in another output's
     cell for the same criterion without modification
     Route: flag for Verifier Q2-IntraRun audit; rewrite with output-specific detail
  D. Narrative analysis in scoring cells -- mechanism interpretation, comparative
     judgment, or narrative prose in verdict or evidence fields
     Route: defer to per-output narrative section; keep scoring cells factual
  E. Novel field labels -- any label not in the permitted set above
     Route: prohibited; *Note*, *Comment*, *Observation*, or any unlisted label
     is a structural violation regardless of content

  No prohibited content category lacks a named destination.

Score all N outputs.
[ANALYST COMPLETE] -- [N] outputs scored

---

CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.

Sweep all *Change*: CHANGE annotations from every scoring block into a single
manifest table. SYNTHESIS must draw regression signals exclusively from this
manifest and is prohibited from re-reading ANALYST blocks or the baseline table
during synthesis. This prohibition is unconditional.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

If no CHANGE annotations appear: "No changes from prior round detected."

[CHANGE MANIFEST COMPLETE]

---

ROLE 3: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun per cell (separately);
Present_mechanism and Absent_mechanism non-emptiness on PARTIAL rows (see manifest).
Cannot check: content quality of Present_mechanism or Absent_mechanism cells
(Confirmer domain). Cannot check: evidence quality standards (Judge domain).
Do not begin until [ANALYST COMPLETE] appears above.

ANCHOR REVIEW BLOCK

The following two questions are the authority for all per-cell specificity entries.
Per-cell Q1-TypeLevel and Q2-IntraRun entries must be evaluated against these
verbatim question forms. Per-cell entries that answer a paraphrase rather than
these anchored questions are a structural drift.

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type -- i.e., would this evidence be equally valid for a correct implementation
    that is not this specific output?"

  Q2 (Intra-run): "Does this evidence fit another output in this run -- i.e.,
    could the same description appear in a different output's cell for this same
    criterion without modification?"

Per-cell VERIFIER table schema:

  Output: [output identifier] -- VERIFIER Specificity and Diagnostic Column Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)     | Q1-TypeLevel     | Q2-IntraRun      | Audit B | Status   |
  |------|---------|---------------------------------------|------------------|------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- evaluating per Q1 above  | PASS / FAIL      | PASS / FAIL      | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt] -- evaluating per Q2 above  | PASS / FAIL      | PASS / FAIL      | PRESENT | ACCEPTED |

  Q1-TypeLevel (required for every row):
    PASS: evidence would NOT describe any well-designed output of this type
    FAIL: evidence would describe any well-designed output of this type
    Evaluating per Q1 above.

  Q2-IntraRun (required for every row):
    PASS: evidence would NOT fit another output in this run unchanged
    FAIL: the same description fits another output in this run unchanged
    Evaluating per Q2 above.

  Audit B (required for PARTIAL rows; n/a for PASS and FAIL):
    PRESENT: Present_mechanism and Absent_mechanism cells both contain named content
    MISSING: one or both cells are blank, --, or empty

  Status:
    ACCEPTED: all applicable fields pass
    REJECTED: any applicable field fails

For every REJECTED row:
  FLAG: [output ID] / [criterion ID]
    Q1-TypeLevel: [PASS/FAIL -- reason if FAIL]
    Q2-IntraRun:  [PASS/FAIL -- reason if FAIL]
    Audit B:      [PRESENT/MISSING/n/a -- reason if MISSING]

Flagged items require Analyst correction and VERIFIER re-audit. Only flagged
items are reopened; ACCEPTED items are closed.

When all rows ACCEPTED across all N outputs:
[VERIFIER COMPLETE]

---

ROLE 4: CONFIRMER

Domain: Content quality -- do Present_mechanism and Absent_mechanism cells name
specific structural properties? (see manifest).
Cannot check: format presence (Verifier domain), evidence specificity (Judge
domain), scoring verdicts (Analyst domain).
Do not begin until [VERIFIER COMPLETE] appears above.

For each PARTIAL verdict across all outputs:

  Output: [output identifier] -- Diagnostic Content Audit

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status               |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|----------------------|
  | C-[NN]    | [first 15 words]                     | YES/NO    | [first 15 words]                    | YES/NO    | CONFIRMED/CHALLENGED |

  Specificity test:
    YES -- names a specific structural element, mechanism, role, gate token,
           design property, or observable structural gap
    NO  -- uses a criterion label, generic quality phrase, or verdict restatement

For every CHALLENGED row:
  CHALLENGE: [output ID] / [criterion ID]:
    Present: "[excerpt]" -- [specific reason it fails the specificity test]
    Absent:  "[excerpt]" -- [specific reason it fails the specificity test]

Challenged items must be rewritten by the Analyst and re-audited by both Verifier
(Audit B) and Confirmer. Only challenged items are reopened; confirmed items closed.

When all PARTIAL diagnostics are CONFIRMED:
[CONFIRMATION COMPLETE]

---

[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all appear above. Holding any one or two of these
tokens does not satisfy this gate. [CONFIRMATION COMPLETE] alone does not satisfy
this gate. [CHANGE MANIFEST COMPLETE] alone does not satisfy this gate.

LEADERBOARD

Rank all outputs by composite score descending. Tie-break protocol (inscribed
here; applied unconditionally when composite scores are equal):
  Primary:   composite score descending
  Secondary: essential_pass count descending (first tie-break dimension)
  Tertiary:  recommended_pass count descending (second tie-break dimension)
  If tied after tertiary: note the tie explicitly; no further inference applied

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output clearly outperforms others, name
the output, the criterion, and the structural mechanism causing the difference.
If no outlier exists: "No excellence signals in this round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]
If none: "No failure patterns in this round."

REGRESSION SIGNALS

Draw exclusively from [CHANGE MANIFEST COMPLETE] above. Do not re-read ANALYST
blocks or the baseline table during synthesis. This prohibition is unconditional.

  Regression: [output ID] / [criterion ID] -- prior: [verdict] -- current: [verdict]
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- all outputs ranked; tie-break protocol applied per definition above
[ ] EXCELLENCE SIGNALS -- section complete or "no signals" stated explicitly
[ ] FAILURE PATTERNS -- all-fail criteria identified or "none" stated explicitly
[ ] REGRESSION SIGNALS -- drawn from manifest exclusively; re-read prohibition observed

[SYNTHESIS COMPLETE]
```

---

## V-02 -- Axis PP: Specificity pre-pass phase, single combined column

**Variation axis**: Lifecycle emphasis -- a dedicated SPECIFICITY PRE-PASS section
runs before the per-cell VERIFIER review and produces two separately named phase
artifacts: TYPE-LEVEL SCAN TABLE (Q1 per criterion per output) and INTRA-RUN SCAN
TABLE (Q2 per criterion per output). Both tables must be present before per-cell
review begins. The per-cell VERIFIER table then carries a single combined "Specificity"
column that reads "per TYPE-LEVEL SCAN and INTRA-RUN SCAN above" -- the structural
separation lives at the phase-artifact level, not the per-cell column level.

**Hypothesis**: C-35 PARTIAL -- the pre-pass phase produces separate named scan
registers, which is structural separation, but C-35 requires the separation to be
"in the VERIFIER per-cell schema" as "distinct labeled columns or fields." A pre-pass
that feeds a combined Specificity column satisfies the INFORMATION separation
requirement but not the PER-CELL SCHEMA column-separation requirement. The pre-pass
closes Q1/Q2 drift at the phase level; the merged per-cell column re-merges them at
the schema level. Separation exists at one level but is collapsed at the level the
criterion names.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round |
|-----------|----------------------------------------|
| V-01 R14  | C-35 FAIL                              |
| V-02 R14  | new in this round                      |
| V-03 R14  | new in this round                      |
| V-04 R14  | new in this round                      |
| V-05 R14  | new in this round                      |

[PRIOR ROUND LOAD COMPLETE]

---

ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Typical output: "Output includes the required structural element."
  Closing mechanism: C-40 requires cross-type genericity named as disqualifying
  pattern at evidence field definition site; C-02 PASS does not close this.

Failure Mode B -- Intra-run duplicate evidence
  Typical output: Same evidence string for same criterion across two outputs.
  Closing mechanism: C-40 requires cross-output duplication named as second
  disqualifying pattern; cross-type anchor alone does not close this path.

Failure Mode C -- Silent arithmetic
  Typical output: Composite = 84.0 with no formula expression at the site.
  Closing mechanism: C-39 requires formula with all parameters inscribed inline;
  C-03 PASS does not require inline inscription.

Failure Mode D -- Pre-pass without per-cell separation
  Typical output: SPECIFICITY PRE-PASS builds separate Q1/Q2 scan tables, but
  the per-cell VERIFIER schema collapses both into a single "Specificity" column.
  Closing mechanism: C-35 requires structurally separated labeled columns IN the
  per-cell schema; phase-artifact separation alone does not satisfy C-35.

Failure Mode E -- Ad-hoc tie-breaking
  Typical output: LEADERBOARD prose resolves ties without an inscribed protocol.
  Closing mechanism: C-41 requires tie-break protocol with named secondary and
  tertiary dimensions inscribed at the leaderboard definition site; C-04 PASS
  does not require this.

---

ROLE DEPENDENCY MANIFEST

| Role                   | Requires                                                                                             | Produces                       | Domain (ONLY)                                                                                         | Cannot Check                                                        |
|------------------------|------------------------------------------------------------------------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| JUDGE                  | [PRIOR ROUND LOAD COMPLETE]                                                                          | [JUDGE STANDARD COMPLETE]      | ACCEPTABLE/UNACCEPTABLE pairs; separating property; CONSOLIDATED PRODUCTION-TIME REGISTER             | Scoring verdicts; format compliance; diagnostic content quality     |
| ANALYST                | [JUDGE STANDARD COMPLETE]                                                                            | [ANALYST COMPLETE]             | Per-criterion scoring; evidence; composite; golden; *Why*; *Change*; Present/Absent cols              | Evidence standards (Judge); format auditing (Verifier)              |
| CHANGE MANIFEST        | [ANALYST COMPLETE]                                                                                   | [CHANGE MANIFEST COMPLETE]     | Sweep *Change*: CHANGE annotations into manifest table                                                | Re-scoring; re-auditing                                             |
| SPECIFICITY PRE-PASS   | [ANALYST COMPLETE]                                                                                   | [SPECIFICITY SCAN COMPLETE]    | TYPE-LEVEL SCAN TABLE (Q1 per output per criterion); INTRA-RUN SCAN TABLE (Q2 per output per criterion) | Scoring; format auditing beyond specificity dimensions             |
| VERIFIER               | [ANALYST COMPLETE] AND [SPECIFICITY SCAN COMPLETE]                                                   | [VERIFIER COMPLETE]            | Format presence: Specificity column consistency with pre-pass tables; Audit B on PARTIAL rows         | Content quality (Confirmer); evidence standards (Judge)             |
| CONFIRMER              | [VERIFIER COMPLETE]                                                                                  | [CONFIRMATION COMPLETE]        | Content quality: do Present/Absent cells name specific structural properties?                         | Format presence (Verifier); scoring (Analyst)                       |
| SYNTHESIS              | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output)              | Leaderboard; excellence signals; failure patterns; regression signals                                 | Re-scoring; re-auditing                                             |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST and SPECIFICITY PRE-PASS cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin without [ANALYST COMPLETE] AND [SPECIFICITY SCAN COMPLETE] above.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without all three tokens above. Any subset does not satisfy
    this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [verbatim or close paraphrase; 'from [Output-N]:'
               prefix required on every ACCEPTABLE entry]"
  UNACCEPTABLE: "[failing example from inputs or representative generic statement]"
  Separating property: [mechanism A] vs [mechanism B]

Before issuing [JUDGE STANDARD COMPLETE], produce the CONSOLIDATED PRODUCTION-TIME
REGISTER. No production-time obligation may be tracked outside this register.

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank OR NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-02      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-03      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-04      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-05      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-06      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-07      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-08      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-09      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-10      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-11      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-12      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-13      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-14      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-15      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-16      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-17      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-18      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-19      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-20      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-21      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-22      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-23      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-24      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-25      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-26      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-27      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-28      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-29      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-30      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-31      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |
  | C-32      | [name]         | YES/NO       | YES/NO                       | YES/NO                      |

[JUDGE STANDARD COMPLETE]

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|

  Evidence field violations (stated at definition site):
    Disqualifying pattern 1: cross-type genericity
    Disqualifying pattern 2: cross-output duplication within the run
    Both disqualifying patterns named here; either one is a cell violation.

  Per-row annotations (required for EVERY row; blank is a structural violation):
    *Why* (required): [structural mechanism; restatement is a violation]
    *Change* (required): NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA

  PARTIAL row additions:
    Present_mechanism (required): [specific structural element preventing FAIL]
    Absent_mechanism (required): [specific structural element preventing PASS]

  Composite (formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [reason]

  Per-output narrative (required):
    Primary differentiator (required): [structural feature explaining score difference]
    Primary miss (required): [most clearly absent mechanism]
    Verdict spread (required): [where points concentrated and why]

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -- Route: rewrite structurally
  B. Criterion restatement as evidence -- Route: rewrite with observable feature
  C. Cross-output generic text -- Route: flag for SPECIFICITY PRE-PASS; rewrite
  D. Narrative analysis in scoring cells -- Route: defer to narrative section
  E. Novel field labels -- Route: prohibited
  No prohibited content category lacks a named destination.

[ANALYST COMPLETE] -- [N] outputs scored

---

CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.
SYNTHESIS draws regression signals exclusively from this manifest; re-reading
ANALYST blocks or the baseline table during synthesis is prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

[CHANGE MANIFEST COMPLETE]

---

SPECIFICITY PRE-PASS

Do not begin until [ANALYST COMPLETE] appears above.

This phase produces two separately named scan registers before per-cell VERIFIER
review begins. Both registers must be complete before [SPECIFICITY SCAN COMPLETE]
is issued.

TYPE-LEVEL SCAN TABLE
Question: "Could this evidence apply to any well-designed output of this type?"

  | Output | Criterion | Evidence excerpt (first 10 words) | Q1-TypeLevel | Q1 note if FAIL |
  |--------|-----------|-----------------------------------|--------------|-----------------|

INTRA-RUN SCAN TABLE
Question: "Does this evidence fit another output in this run unchanged?"

  | Output | Criterion | Evidence excerpt (first 10 words) | Q2-IntraRun  | Q2 note if FAIL |
  |--------|-----------|-----------------------------------|--------------|-----------------|

Both tables must be populated for all N outputs before the gate is issued.
[SPECIFICITY SCAN COMPLETE]

---

ROLE 3: VERIFIER

Domain: Format presence -- Specificity column consistency with pre-pass scan
results; Present_mechanism and Absent_mechanism non-emptiness on PARTIAL rows.
Cannot check: content quality (Confirmer); evidence standards (Judge).
Do not begin until [ANALYST COMPLETE] AND [SPECIFICITY SCAN COMPLETE] appear above.

Per-cell VERIFIER table:

  Output: [output identifier] -- VERIFIER Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Specificity (per TYPE-LEVEL SCAN and INTRA-RUN SCAN above) | Audit B | Status   |
  |------|---------|-----------------------------------|------------------------------------------------------------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | PASS -- Q1 PASS (per pre-pass) / Q2 PASS (per pre-pass)    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | FAIL -- Q1 FAIL per TYPE-LEVEL SCAN note                   | PRESENT | REJECTED |

  Specificity column: references SPECIFICITY PRE-PASS results; a contradiction
    between pre-pass FAIL and per-cell PASS is a structural violation. This
    column defers to the pre-pass tables as authoritative.

  Audit B (PARTIAL rows): PRESENT if Present/Absent contain named content; MISSING otherwise.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- [Specificity: reason | Audit B: reason]

[VERIFIER COMPLETE]

---

ROLE 4: CONFIRMER

Domain: Content quality on Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status               |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|----------------------|

[CONFIRMATION COMPLETE]

---

[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all present above. Any subset does not satisfy this gate.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally):
  Primary: composite score descending
  Secondary: essential_pass count descending (first tie-break)
  Tertiary: recommended_pass count descending (second tie-break)
  Tied after tertiary: noted explicitly; no further inference

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS
If no outlier: "No excellence signals in this round."

FAILURE PATTERNS
If none: "No failure patterns in this round."

REGRESSION SIGNALS
Draw exclusively from [CHANGE MANIFEST COMPLETE]. Re-reading prohibited.
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- ranked; tie-break protocol applied
[ ] EXCELLENCE SIGNALS -- section present
[ ] FAILURE PATTERNS -- section present
[ ] REGRESSION SIGNALS -- from manifest; re-read prohibition observed

[SYNTHESIS COMPLETE]
```

---

## V-03 -- Axis OR: Operational-register phrasing, single combined field

**Variation axis**: Phrasing register -- the VERIFIER specificity instructions use
operational directive language ("TYPE-GENERICITY SCAN:" / "RUN-DUPLICATE SCAN:")
that names each scan as a distinct labeled directive. However, both scans are written
into a single per-cell "Specificity-Scan" prose block -- not separate labeled columns.
No pre-pass phase. No anchor block with separately labeled verbatim entries.

**Hypothesis**: C-35 FAIL -- directive labeling of two scan types within a single
field does not substitute for structural column separation; the per-cell schema has
one "Specificity-Scan" cell, not two independently auditable columns; C-29 PASS
(both questions stated in the VERIFIER instructions) but C-35 FAIL (structural
separation into distinct fields absent). Phrasing clarity is orthogonal to structural
separation.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round |
|-----------|----------------------------------------|
| V-01 R14  | C-35 FAIL                              |
| V-02 R14  | new in this round                      |
| V-03 R14  | new in this round                      |
| V-04 R14  | new in this round                      |
| V-05 R14  | new in this round                      |

[PRIOR ROUND LOAD COMPLETE]

---

ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Closing mechanism: C-40 names cross-type genericity as disqualifying pattern
  at evidence field definition site.

Failure Mode B -- Intra-run duplicate evidence
  Closing mechanism: C-40 names cross-output duplication as second disqualifying
  pattern at the same definition site.

Failure Mode C -- Silent arithmetic
  Closing mechanism: C-39 requires formula with all parameters inscribed inline
  at the scoring site.

Failure Mode D -- Phrasing clarity without structural separation
  Typical output: VERIFIER has "TYPE-GENERICITY SCAN: PASS / RUN-DUPLICATE SCAN:
  PASS" inside one Specificity-Scan cell -- both scan labels appear in one field.
  Closing mechanism: C-35 requires separate labeled COLUMNS for Q1 and Q2; naming
  two scans inside one cell satisfies C-29 (both questions stated) but not C-35
  (structural column separation in the per-cell schema).

Failure Mode E -- Ad-hoc tie-breaking
  Closing mechanism: C-41 requires tie-break protocol with named dimensions
  inscribed at the leaderboard definition site.

---

ROLE DEPENDENCY MANIFEST

| Role            | Requires                                                                                             | Produces                    | Domain (ONLY)                                                                              | Cannot Check                                              |
|-----------------|------------------------------------------------------------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| JUDGE           | [PRIOR ROUND LOAD COMPLETE]                                                                          | [JUDGE STANDARD COMPLETE]   | ACCEPTABLE/UNACCEPTABLE pairs; separating property; CONSOLIDATED PRODUCTION-TIME REGISTER  | Scoring; format compliance; diagnostic content            |
| ANALYST         | [JUDGE STANDARD COMPLETE]                                                                            | [ANALYST COMPLETE]          | Per-criterion scoring; evidence; composite; golden; *Why*; *Change*; Present/Absent cols   | Evidence standards (Judge); format auditing (Verifier)    |
| CHANGE MANIFEST | [ANALYST COMPLETE]                                                                                   | [CHANGE MANIFEST COMPLETE]  | Sweep *Change*: CHANGE annotations into manifest                                           | Re-scoring; re-auditing                                   |
| VERIFIER        | [ANALYST COMPLETE]                                                                                   | [VERIFIER COMPLETE]         | Format presence: Specificity-Scan non-emptiness; Audit B on PARTIAL rows                   | Content quality (Confirmer); evidence standards (Judge)   |
| CONFIRMER       | [VERIFIER COMPLETE]                                                                                  | [CONFIRMATION COMPLETE]     | Content quality: do Present/Absent cells name specific structural properties?              | Format presence (Verifier); scoring (Analyst)             |
| SYNTHESIS       | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output)           | Leaderboard; excellence signals; failure patterns; regression signals                      | Re-scoring; re-auditing                                   |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST and VERIFIER cannot begin without [ANALYST COMPLETE] above.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without all three tokens above.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [example; 'from [Output-N]:' prefix required]"
  UNACCEPTABLE: "[failing example]"
  Separating property: [mechanism A] vs [mechanism B]

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank OR NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-32 (32 rows; same structure) |

[JUDGE STANDARD COMPLETE]

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|

  Evidence field violations (both named at definition site):
    Disqualifying pattern 1: cross-type genericity
    Disqualifying pattern 2: cross-output duplication within the run

  Per-row annotations (required for EVERY row):
    *Why* (required): [structural mechanism; restatement is FAIL]
    *Change* (required): NO CHANGE | CHANGE from [prior]: [reason] | NO PRIOR DATA

  PARTIAL row additions:
    Present_mechanism (required): [structural element preventing FAIL]
    Absent_mechanism (required): [structural element preventing PASS]

  Composite (formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [reason]

  Per-output narrative (required):
    Primary differentiator (required): [structural feature explaining score difference]
    Primary miss (required): [most clearly absent mechanism]
    Verdict spread (required): [where points concentrated and why]

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -- Route: rewrite structurally
  B. Criterion restatement as evidence -- Route: rewrite with observable feature
  C. Cross-output generic text -- Route: flag for Specificity-Scan; rewrite
  D. Narrative analysis in scoring cells -- Route: defer to narrative section
  E. Novel field labels -- Route: prohibited
  No prohibited content category lacks a named destination.

[ANALYST COMPLETE] -- [N] outputs scored

---

CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.
SYNTHESIS draws regression signals exclusively from this manifest; re-reading
ANALYST blocks during synthesis is prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

[CHANGE MANIFEST COMPLETE]

---

ROLE 3: VERIFIER

Domain: Format presence -- Specificity-Scan non-emptiness; Audit B on PARTIAL rows.
Cannot check: content quality (Confirmer); evidence standards (Judge).
Do not begin until [ANALYST COMPLETE] appears above.

Specificity-Scan instruction:
For each evidence cell, perform two scans and report both results in the
Specificity-Scan field:

  TYPE-GENERICITY SCAN: Would this evidence be equally valid for any correct
  implementation of this type? If yes, flag FAIL -- the evidence is type-generic
  and requires revision.

  RUN-DUPLICATE SCAN: Does this exact evidence appear for the same criterion in
  another output's cell in this run? If yes, flag FAIL -- cross-output duplication
  detected; revision required.

Per-cell VERIFIER table:

  Output: [output identifier] -- VERIFIER Audit

  | ID   | Verdict | Evidence excerpt (first 15 words) | Specificity-Scan                                               | Audit B | Status   |
  |------|---------|-----------------------------------|----------------------------------------------------------------|---------|----------|
  | C-01 | PASS    | [excerpt]                         | TYPE-GENERICITY: PASS / RUN-DUPLICATE: PASS                    | n/a     | ACCEPTED |
  | C-02 | PARTIAL | [excerpt]                         | TYPE-GENERICITY: FAIL (applies to any output) / RUN-DUP: PASS  | PRESENT | REJECTED |

  Specificity-Scan: both scan results reported in one field; ACCEPTED only if
    both TYPE-GENERICITY SCAN and RUN-DUPLICATE SCAN return PASS.
  Audit B (PARTIAL rows): PRESENT if Present/Absent cells contain named content.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- [Specificity-Scan: reason | Audit B: reason]

[VERIFIER COMPLETE]

---

ROLE 4: CONFIRMER

Domain: Content quality on Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|--------|

[CONFIRMATION COMPLETE]

---

[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all present above. Any subset does not satisfy this gate.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally):
  Primary: composite score descending
  Secondary: essential_pass count descending (first tie-break)
  Tertiary: recommended_pass count descending (second tie-break)
  Tied after tertiary: noted explicitly; no further inference

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS
If none: "No excellence signals in this round."

FAILURE PATTERNS
If none: "No failure patterns in this round."

REGRESSION SIGNALS
Draw exclusively from [CHANGE MANIFEST COMPLETE]. Re-reading prohibited.
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- ranked; tie-break protocol applied
[ ] EXCELLENCE SIGNALS -- section present
[ ] FAILURE PATTERNS -- section present
[ ] REGRESSION SIGNALS -- from manifest; re-read prohibition observed

[SYNTHESIS COMPLETE]
```

---

## V-04 -- Axes DC + PP: Dual-column table + pre-pass phase

**Variation axis**: Output format + lifecycle emphasis -- both V-01 and V-02
mechanisms are present: (1) SPECIFICITY PRE-PASS builds TYPE-LEVEL SCAN TABLE
and INTRA-RUN SCAN TABLE as distinct phase artifacts before per-cell review, AND
(2) the per-cell VERIFIER table has Q1-TypeLevel and Q2-IntraRun as separately
labeled columns consistent with the pre-pass tables. The pre-pass tables are
authoritative; the per-cell columns must be consistent with them. An anchor block
pre-states Q1 and Q2 verbatim before the per-cell schema.

Two enforcement points are non-redundant: removing the pre-pass leaves per-cell
columns without authoritative question-anchoring (V-01 scenario); removing the
per-cell columns leaves structural separation at the phase level only (V-02 scenario).

**Hypothesis**: C-35 PASS -- per-cell schema has two structurally distinct labeled
columns; pre-pass provides authoritative question anchoring; per-cell entries carry
"per TYPE-LEVEL SCAN above" / "per INTRA-RUN SCAN above" references.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round |
|-----------|----------------------------------------|
| V-01 R14  | C-35 FAIL                              |
| V-02 R14  | new in this round                      |
| V-03 R14  | new in this round                      |
| V-04 R14  | new in this round                      |
| V-05 R14  | new in this round                      |

[PRIOR ROUND LOAD COMPLETE]

---

ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Closing mechanism: C-40 names cross-type genericity as disqualifying pattern
  at evidence field definition site.

Failure Mode B -- Intra-run duplicate evidence
  Closing mechanism: C-40 names cross-output duplication as second disqualifying
  pattern at the same definition site.

Failure Mode C -- Silent arithmetic
  Closing mechanism: C-39 requires formula with all parameters inscribed inline.

Failure Mode D -- Pre-pass without per-cell column separation
  Typical output: Pre-pass builds Q1 and Q2 registers but the per-cell schema
  collapses both into a single "Specificity" column.
  Closing mechanism: C-35 requires separate labeled columns IN the per-cell schema;
  phase separation alone is insufficient.

Failure Mode E -- Ad-hoc tie-breaking
  Closing mechanism: C-41 requires tie-break protocol with named dimensions
  inscribed at the leaderboard definition site.

---

ROLE DEPENDENCY MANIFEST

| Role                 | Requires                                                                                             | Produces                       | Domain (ONLY)                                                                                             | Cannot Check                                                    |
|----------------------|------------------------------------------------------------------------------------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| JUDGE                | [PRIOR ROUND LOAD COMPLETE]                                                                          | [JUDGE STANDARD COMPLETE]      | ACCEPTABLE/UNACCEPTABLE pairs; separating property; CONSOLIDATED PRODUCTION-TIME REGISTER                 | Scoring; format compliance; diagnostic content                  |
| ANALYST              | [JUDGE STANDARD COMPLETE]                                                                            | [ANALYST COMPLETE]             | Per-criterion scoring; evidence; composite; golden; *Why*; *Change*; Present/Absent cols                  | Evidence standards (Judge); format auditing (Verifier)          |
| CHANGE MANIFEST      | [ANALYST COMPLETE]                                                                                   | [CHANGE MANIFEST COMPLETE]     | Sweep *Change*: CHANGE annotations into manifest                                                          | Re-scoring; re-auditing                                         |
| SPECIFICITY PRE-PASS | [ANALYST COMPLETE]                                                                                   | [SPECIFICITY SCAN COMPLETE]    | TYPE-LEVEL SCAN TABLE (Q1); INTRA-RUN SCAN TABLE (Q2) -- both authoritative for per-cell VERIFIER columns | Scoring; format beyond specificity                              |
| VERIFIER             | [ANALYST COMPLETE] AND [SPECIFICITY SCAN COMPLETE]                                                   | [VERIFIER COMPLETE]            | Format: Q1-TypeLevel and Q2-IntraRun per cell (per pre-pass); Audit B on PARTIAL rows                     | Content quality (Confirmer); evidence standards (Judge)         |
| CONFIRMER            | [VERIFIER COMPLETE]                                                                                  | [CONFIRMATION COMPLETE]        | Content quality: do Present/Absent cells name specific structural properties?                             | Format presence (Verifier); scoring (Analyst)                   |
| SYNTHESIS            | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output)              | Leaderboard; excellence signals; failure patterns; regression signals                                     | Re-scoring; re-auditing                                         |

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST and SPECIFICITY PRE-PASS cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin without [ANALYST COMPLETE] AND [SPECIFICITY SCAN COMPLETE] above.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without all three tokens above. Any subset does not satisfy
    this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [example; 'from [Output-N]:' prefix required]"
  UNACCEPTABLE: "[failing example]"
  Separating property: [mechanism A] vs [mechanism B]

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank OR NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-32 (32 rows; same structure) |

[JUDGE STANDARD COMPLETE]

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|

  Evidence field violations (both named at definition site):
    Disqualifying pattern 1: cross-type genericity
    Disqualifying pattern 2: cross-output duplication within the run

  Per-row annotations (required for EVERY row):
    *Why* (required): [structural mechanism; restatement is FAIL]
    *Change* (required): NO CHANGE | CHANGE from [prior]: [reason] | NO PRIOR DATA

  PARTIAL row additions:
    Present_mechanism (required): [structural element preventing FAIL]
    Absent_mechanism (required): [structural element preventing PASS]

  Composite (formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [reason]

  Per-output narrative (required):
    Primary differentiator (required): [structural feature explaining score difference]
    Primary miss (required): [most clearly absent mechanism]
    Verdict spread (required): [where points concentrated and why]

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -- Route: rewrite structurally
  B. Criterion restatement as evidence -- Route: rewrite with observable feature
  C. Cross-output generic text -- Route: flag for pre-pass; rewrite
  D. Narrative analysis in scoring cells -- Route: defer to narrative section
  E. Novel field labels -- Route: prohibited
  No prohibited content category lacks a named destination.

[ANALYST COMPLETE] -- [N] outputs scored

---

CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.
SYNTHESIS draws regression signals exclusively from this manifest; re-reading
ANALYST blocks or baseline during synthesis is prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

[CHANGE MANIFEST COMPLETE]

---

SPECIFICITY PRE-PASS

Do not begin until [ANALYST COMPLETE] appears above.

Produce two separately named scan registers. Both must be complete before
[SPECIFICITY SCAN COMPLETE] is issued. These registers are authoritative for
the per-cell Q1-TypeLevel and Q2-IntraRun VERIFIER columns.

TYPE-LEVEL SCAN TABLE
Q1 question: "Could this evidence apply to any well-designed output of this type?"

  | Output | Criterion | Evidence excerpt (first 10 words) | Q1-TypeLevel | Q1 note if FAIL |
  |--------|-----------|-----------------------------------|--------------|-----------------|

INTRA-RUN SCAN TABLE
Q2 question: "Does this evidence fit another output in this run unchanged?"

  | Output | Criterion | Evidence excerpt (first 10 words) | Q2-IntraRun  | Q2 note if FAIL |
  |--------|-----------|-----------------------------------|--------------|-----------------|

All N outputs x all criteria populated in both tables before the gate.
[SPECIFICITY SCAN COMPLETE]

---

ROLE 3: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun per cell (per pre-pass
tables); Audit B on PARTIAL rows (see manifest).
Cannot check: content quality (Confirmer); evidence standards (Judge).
Do not begin until [ANALYST COMPLETE] AND [SPECIFICITY SCAN COMPLETE] appear above.

ANCHOR REVIEW BLOCK

Both questions below are authoritative for per-cell entries and must be consistent
with the SPECIFICITY PRE-PASS tables above.

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type?" Per TYPE-LEVEL SCAN TABLE above.

  Q2 (Intra-run): "Does this evidence fit another output in this run unchanged?"
    Per INTRA-RUN SCAN TABLE above.

Per-cell VERIFIER table:

  Output: [output identifier] -- VERIFIER Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)         | Q1-TypeLevel (per pre-pass) | Q2-IntraRun (per pre-pass) | Audit B | Status   |
  |------|---------|-------------------------------------------|-----------------------------|----------------------------|---------|----------|
  | C-01 | PASS    | [excerpt] -- per TYPE-LEVEL SCAN above    | PASS / FAIL                 | PASS / FAIL                | n/a     | ACCEPTED |

  Q1-TypeLevel: consistent with TYPE-LEVEL SCAN TABLE result; contradiction is
    a structural violation detectable by comparison with SPECIFICITY PRE-PASS above.
  Q2-IntraRun: consistent with INTRA-RUN SCAN TABLE result; contradiction is
    a structural violation.
  Audit B (PARTIAL rows): PRESENT if Present/Absent contain named content.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Q1-TypeLevel: [reason] | Q2-IntraRun: [reason] | Audit B: [reason]

[VERIFIER COMPLETE]

---

ROLE 4: CONFIRMER

Domain: Content quality on Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|--------|

[CONFIRMATION COMPLETE]

---

[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all present above. Any subset does not satisfy this gate.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally):
  Primary: composite score descending
  Secondary: essential_pass count descending (first tie-break)
  Tertiary: recommended_pass count descending (second tie-break)
  Tied after tertiary: noted explicitly; no further inference

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS
If none: "No excellence signals in this round."

FAILURE PATTERNS
If none: "No failure patterns in this round."

REGRESSION SIGNALS
Draw exclusively from [CHANGE MANIFEST COMPLETE]. Re-reading prohibited.
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- ranked; tie-break protocol applied per definition above
[ ] EXCELLENCE SIGNALS -- section present
[ ] FAILURE PATTERNS -- section present
[ ] REGRESSION SIGNALS -- from manifest; re-read prohibition observed

[SYNTHESIS COMPLETE]
```

---

## V-05 -- Axes DC + PP + role: Dedicated SPECIFICITY AUDITOR role

**Variation axis**: Output format + lifecycle emphasis + role sequence -- V-04
mechanisms (pre-pass registers + dual-column per-cell table) are preserved, but
the SPECIFICITY PRE-PASS is elevated to a named ROLE: SPECIFICITY AUDITOR with
its own gate token [SPECIFICITY AUDIT COMPLETE]. The VERIFIER entry condition
quotes this gate token verbatim. This makes the two-dimension specificity audit
independently schedulable, independently gateable, and independently verifiable:
an evaluator reading only the VERIFIER entry condition can confirm that a dedicated
role producing both scan registers completed before VERIFIER began -- without reading
the SPECIFICITY AUDITOR role body.

**Hypothesis**: C-35 PASS with the additional independent-audit property: the gate
token [SPECIFICITY AUDIT COMPLETE] appearing in the VERIFIER entry condition makes
the Q1/Q2 separation auditable from the VERIFIER header alone. This is the same
structural property ES-R14-2 identified as a candidate for C-42 in the prior round:
VERIFIER entry condition quoting the SPECIFICITY AUDIT COMPLETE gate identifier
verbatim makes specificity-audit sequencing independently auditable from the VERIFIER
header, without reading the SPECIFICITY AUDITOR role body.

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence, a composite score,
and a golden-threshold determination. The scorecard includes a ranked leaderboard,
excellence signals, failure patterns, and regression signals.

---

PRIOR ROUND LOAD

| Variation | Open aspirationals entering this round |
|-----------|----------------------------------------|
| V-01 R14  | C-35 FAIL                              |
| V-02 R14  | new in this round                      |
| V-03 R14  | new in this round                      |
| V-04 R14  | new in this round                      |
| V-05 R14  | new in this round                      |

[PRIOR ROUND LOAD COMPLETE]

---

ANTI-PATTERN ANCHOR

Failure Mode A -- Generic evidence (cross-type)
  Closing mechanism: C-40 names cross-type genericity as disqualifying pattern
  at evidence field definition site.

Failure Mode B -- Intra-run duplicate evidence
  Closing mechanism: C-40 names cross-output duplication as second disqualifying
  pattern at the same definition site.

Failure Mode C -- Silent arithmetic
  Closing mechanism: C-39 requires formula with all parameters inscribed inline
  at the scoring site.

Failure Mode D -- Combined specificity field (merged columns)
  Typical output: Per-cell VERIFIER table has one "Specificity" column addressing
  both Q1 and Q2 in a single cell, even when both questions are explicitly stated.
  Closing mechanism: C-35 requires structurally separated labeled columns for Q1
  and Q2; a single column addressing both questions satisfies C-29 but not C-35.

Failure Mode E -- Ad-hoc tie-breaking
  Closing mechanism: C-41 requires tie-break protocol with named secondary and
  tertiary dimensions inscribed at the leaderboard definition site.

---

ROLE DEPENDENCY MANIFEST

| Role                    | Requires                                                                                             | Produces                       | Domain (ONLY)                                                                                                                          | Cannot Check                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| JUDGE                   | [PRIOR ROUND LOAD COMPLETE]                                                                          | [JUDGE STANDARD COMPLETE]      | ACCEPTABLE/UNACCEPTABLE pairs; separating property; CONSOLIDATED PRODUCTION-TIME REGISTER                                              | Scoring; format compliance; diagnostic content                  |
| ANALYST                 | [JUDGE STANDARD COMPLETE]                                                                            | [ANALYST COMPLETE]             | Per-criterion scoring; evidence; composite; golden; *Why*; *Change*; Present/Absent cols                                               | Evidence standards (Judge); format auditing (Verifier)          |
| CHANGE MANIFEST         | [ANALYST COMPLETE]                                                                                   | [CHANGE MANIFEST COMPLETE]     | Sweep *Change*: CHANGE annotations into manifest                                                                                       | Re-scoring; re-auditing                                         |
| SPECIFICITY AUDITOR     | [ANALYST COMPLETE]                                                                                   | [SPECIFICITY AUDIT COMPLETE]   | TYPE-LEVEL SCAN TABLE (Q1 per output per criterion); INTRA-RUN SCAN TABLE (Q2 per output per criterion) as authoritative phase artifacts | Scoring; format beyond specificity                              |
| VERIFIER                | [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]                                                  | [VERIFIER COMPLETE]            | Format: Q1-TypeLevel and Q2-IntraRun per cell (per [SPECIFICITY AUDIT COMPLETE]); Audit B on PARTIAL rows                              | Content quality (Confirmer); evidence standards (Judge)         |
| CONFIRMER               | [VERIFIER COMPLETE]                                                                                  | [CONFIRMATION COMPLETE]        | Content quality: do Present/Absent cells name specific structural properties?                                                          | Format presence (Verifier); scoring (Analyst)                   |
| SYNTHESIS               | [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND [CHANGE MANIFEST COMPLETE] (strict conjunction) | (terminal output)              | Leaderboard; excellence signals; failure patterns; regression signals                                                                  | Re-scoring; re-auditing                                         |

A row with any blank cell is a structural gap. No role may begin unless its
Requires entry appears in the output above.

Gate rules (hard):
  - ANALYST cannot begin without [JUDGE STANDARD COMPLETE] above.
  - CHANGE MANIFEST and SPECIFICITY AUDITOR cannot begin without [ANALYST COMPLETE] above.
  - VERIFIER cannot begin without [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE]
    above. Both tokens must be present; [ANALYST COMPLETE] alone does not satisfy this
    gate. [SPECIFICITY AUDIT COMPLETE] alone does not satisfy this gate.
  - CONFIRMER cannot begin without [VERIFIER COMPLETE] above.
  - SYNTHESIS cannot begin without [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE]
    AND [CHANGE MANIFEST COMPLETE] all present above. Any subset does not satisfy
    this gate.
  - No role may operate outside its declared Domain.
  - No role may be skipped or merged with another.

---

ROLE 1: JUDGE

Domain: Evidence quality standards (see manifest).
Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each criterion C-01 through C-32:

  C-[NN]: [criterion name]
  ACCEPTABLE: "from [Output-N]: [example; 'from [Output-N]:' prefix required]"
  UNACCEPTABLE: "[failing example]"
  Separating property: [mechanism A] vs [mechanism B]

CONSOLIDATED PRODUCTION-TIME REGISTER
Gate: every cell must contain YES; blank OR NO blocks [JUDGE STANDARD COMPLETE].

  | Criterion | Criterion name | Pair present | Separating property declared | ACCEPTABLE source annotated |
  |-----------|----------------|--------------|------------------------------|-----------------------------|
  | C-01 through C-32 (32 rows; same structure) |

[JUDGE STANDARD COMPLETE]

---

ROLE 2: ANALYST

Domain: Per-criterion scoring (see manifest).
Do not begin until [JUDGE STANDARD COMPLETE] appears above.

ANALYST OUTPUT SCHEMA -- permitted fields only:

  Output: [output identifier] (required)

  | ID   | Criterion | Wt | Verdict           | Evidence (required)                         | Present_mechanism | Absent_mechanism |
  |------|-----------|----|-------------------|---------------------------------------------|-------------------|------------------|

  Evidence field violations (both named at definition site):
    Disqualifying pattern 1: cross-type genericity
    Disqualifying pattern 2: cross-output duplication within the run

  Per-row annotations (required for EVERY row):
    *Why* (required): [structural mechanism; restatement is FAIL]
    *Change* (required): NO CHANGE | CHANGE from [prior]: [reason] | NO PRIOR DATA

  PARTIAL row additions:
    Present_mechanism (required): [structural element preventing FAIL]
    Absent_mechanism (required): [structural element preventing PASS]

  Composite (formula inscribed inline with all parameters):
    essential_pass    = [count; PARTIAL = 0.5]
    recommended_pass  = [count; PARTIAL = 0.5]
    aspirational_pass = [count; PARTIAL = 0.5]

    composite = (essential_pass / 4 x 60)
              + (recommended_pass / 3 x 30)
              + (aspirational_pass / 25 x 10)
              = [result]

    Golden (required): YES -- all essentials PASS; composite >= 80
                     | NO  -- [reason]

  Per-output narrative (required):
    Primary differentiator (required): [structural feature explaining score difference]
    Primary miss (required): [most clearly absent mechanism]
    Verdict spread (required): [where points concentrated and why]

PROHIBITED CONTENT CATEGORIES:
  A. Evaluative prose -- Route: rewrite structurally
  B. Criterion restatement as evidence -- Route: rewrite with observable feature
  C. Cross-output generic text -- Route: flag for SPECIFICITY AUDITOR; rewrite
  D. Narrative analysis in scoring cells -- Route: defer to narrative section
  E. Novel field labels -- Route: prohibited
  No prohibited content category lacks a named destination.

[ANALYST COMPLETE] -- [N] outputs scored

---

CHANGE MANIFEST

Do not begin until [ANALYST COMPLETE] appears above.
SYNTHESIS draws regression signals exclusively from this manifest; re-reading
ANALYST blocks or the baseline during synthesis is unconditionally prohibited.

  | Output | Criterion | Prior verdict | Current verdict | Reason |
  |--------|-----------|---------------|-----------------|--------|

[CHANGE MANIFEST COMPLETE]

---

ROLE: SPECIFICITY AUDITOR

Domain: TYPE-LEVEL SCAN TABLE and INTRA-RUN SCAN TABLE as authoritative phase
artifacts. These registers are the sole authority for Q1-TypeLevel and Q2-IntraRun
values used by the VERIFIER per-cell columns (see manifest).
Do not begin until [ANALYST COMPLETE] appears above.

Produce two separately named scan registers. Both must be complete for all N
outputs before [SPECIFICITY AUDIT COMPLETE] is issued.

[SPECIFICITY AUDIT COMPLETE] gate confirmation -- both required:
  TYPE-LEVEL SCAN TABLE: complete (all N outputs x all criteria; Q1 PASS/FAIL per cell)
  INTRA-RUN SCAN TABLE: complete (all N outputs x all criteria; Q2 PASS/FAIL per cell)
  All cells populated with no blanks.

TYPE-LEVEL SCAN TABLE
Q1 question: "Could this evidence apply to any well-designed output of this type?"

  | Output | Criterion | Evidence excerpt (first 10 words) | Q1-TypeLevel | Q1 note if FAIL |
  |--------|-----------|-----------------------------------|--------------|-----------------|

INTRA-RUN SCAN TABLE
Q2 question: "Does this evidence fit another output in this run unchanged?"

  | Output | Criterion | Evidence excerpt (first 10 words) | Q2-IntraRun  | Q2 note if FAIL |
  |--------|-----------|-----------------------------------|--------------|-----------------|

[SPECIFICITY AUDIT COMPLETE]

---

ROLE 3: VERIFIER

Domain: Format presence -- Q1-TypeLevel and Q2-IntraRun per cell (per
[SPECIFICITY AUDIT COMPLETE] above); Audit B on PARTIAL rows (see manifest).
Cannot check: content quality (Confirmer); evidence standards (Judge).

Do not begin until [ANALYST COMPLETE] AND [SPECIFICITY AUDIT COMPLETE] appear above.
[ANALYST COMPLETE] alone does not satisfy this gate.
[SPECIFICITY AUDIT COMPLETE]: confirms TYPE-LEVEL SCAN TABLE and INTRA-RUN SCAN TABLE
for all N outputs are complete and authoritative. Per-cell Q1-TypeLevel and Q2-IntraRun
columns must be consistent with those tables. A contradiction between a per-cell PASS
and a pre-audit FAIL for the same output/criterion pair is a structural violation
detectable by comparison against the SPECIFICITY AUDITOR output above.

ANCHOR REVIEW BLOCK

  Q1 (Type-level): "Could this evidence apply to any well-designed output of this
    type?" Per TYPE-LEVEL SCAN TABLE in [SPECIFICITY AUDIT COMPLETE] above.

  Q2 (Intra-run): "Does this evidence fit another output in this run unchanged?"
    Per INTRA-RUN SCAN TABLE in [SPECIFICITY AUDIT COMPLETE] above.

Per-cell VERIFIER table:
(Requires [SPECIFICITY AUDIT COMPLETE] per entry condition above)

  Output: [output identifier] -- VERIFIER Audit

  | ID   | Verdict | Evidence excerpt (first 15 words)        | Q1-TypeLevel (per SA) | Q2-IntraRun (per SA) | Audit B | Status   |
  |------|---------|------------------------------------------|-----------------------|----------------------|---------|----------|
  | C-01 | PASS    | [excerpt]                                | PASS / FAIL           | PASS / FAIL          | n/a     | ACCEPTED |

  Q1-TypeLevel: consistent with TYPE-LEVEL SCAN TABLE; contradiction is structural violation.
  Q2-IntraRun: consistent with INTRA-RUN SCAN TABLE; contradiction is structural violation.
  Audit B (PARTIAL rows): PRESENT if Present/Absent contain named content.

For every REJECTED row:
  FLAG: [output ID] / [criterion ID] -- Q1-TypeLevel: [reason] | Q2-IntraRun: [reason] | Audit B: [reason]

[VERIFIER COMPLETE]

---

ROLE 4: CONFIRMER

Domain: Content quality on Present/Absent cells.
Do not begin until [VERIFIER COMPLETE] appears above.

  | Criterion | Present_mechanism (verbatim excerpt) | Specific? | Absent_mechanism (verbatim excerpt) | Specific? | Status |
  |-----------|--------------------------------------|-----------|-------------------------------------|-----------|--------|

[CONFIRMATION COMPLETE]

---

[SYNTHESIS OPEN]

SYNTHESIS

Do not begin until [VERIFIER COMPLETE] AND [CONFIRMATION COMPLETE] AND
[CHANGE MANIFEST COMPLETE] all present above. Any subset does not satisfy this gate.

LEADERBOARD

Tie-break protocol (inscribed here; applied unconditionally when composite scores
are equal):
  Primary: composite score descending
  Secondary: essential_pass count descending (first tie-break dimension)
  Tertiary: recommended_pass count descending (second tie-break dimension)
  Tied after tertiary: noted explicitly; no further inference applied

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS
If none: "No excellence signals in this round."

FAILURE PATTERNS
If none: "No failure patterns in this round."

REGRESSION SIGNALS
Draw exclusively from [CHANGE MANIFEST COMPLETE]. Re-reading ANALYST blocks or
the baseline during synthesis is unconditionally prohibited.
If none: "No regressions in this round."

Pre-close checklist:
[ ] LEADERBOARD -- all outputs ranked; tie-break protocol applied per definition
[ ] EXCELLENCE SIGNALS -- section present or absence stated
[ ] FAILURE PATTERNS -- section present or absence stated
[ ] REGRESSION SIGNALS -- drawn from manifest; re-read prohibition confirmed

[SYNTHESIS COMPLETE]
```

---

## Predicted discrimination matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-35 (VERIFIER dual-column) | **PASS** | **PARTIAL** | **FAIL** | **PASS** | **PASS** |
| C-37 (anchor block verbatim pre-statement) | PASS | PARTIAL (pre-pass tables exist but no named anchor block) | FAIL (no anchor block) | PASS | PASS |
| C-17 (specificity test present) | PASS | PASS | PASS | PASS | PASS |
| C-29 (both questions stated) | PASS | PASS | PASS | PASS | PASS |
| C-39 (formula inscribed inline) | PASS | PASS | PASS | PASS | PASS |
| C-40 (evidence dual-violation anchor) | PASS | PASS | PASS | PASS | PASS |
| C-41 (leaderboard tie-break protocol) | PASS | PASS | PASS | PASS | PASS |
| All other R14 V-01 PASSes | PASS | PASS | PASS | PASS | PASS |

**Key discriminations**:
- V-01 vs V-02 (C-35): V-01 PASS (per-cell columns separated); V-02 PARTIAL (phase-level separation only) -- load-bearing test: does per-cell-schema column separation satisfy C-35 when phase separation exists but per-cell schema is combined?
- V-01 vs V-03 (C-35): V-01 PASS (structural columns); V-03 FAIL (directive phrasing, no column separation) -- tests whether operational imperative language without structural separation satisfies C-35
- V-04 vs V-02 (C-35): V-04 PASS (pre-pass + per-cell columns); V-02 PARTIAL (pre-pass only) -- confirms per-cell column separation is load-bearing even when pre-pass registers exist
- V-04 vs V-05 (role elevation): identical C-35 predictions; V-05 adds independent-audit property (VERIFIER entry condition cites [SPECIFICITY AUDIT COMPLETE] making Q1/Q2 separation auditable from VERIFIER header alone) -- candidate excellence signal for C-42 in R16
