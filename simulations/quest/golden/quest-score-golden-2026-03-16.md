Written to `simulations/quest/golden/quest-score-golden-2026-03-16.md`.

**Summary of what was captured:**

The golden prompt is V-05 (P+Q+R+U+V) at 99.6875, simplified to 1,397 words (21% reduction from 1,761). The five patterns that distinguish it from the baseline:

1. **Formula-change alert** — names both prior (14, v7) and current (16, v8) values before Phase 1, forcing the two-sided delta that C-15 requires
2. **Symmetric Delta Register** — two-column table makes a missing Prior state a structural violation visible by column scan, not logical inference
3. **Bilateral audit PARTIAL-reason labeling** — Reason column resolves the three-way ambiguity of a bare PARTIAL (N/A rule / clean result / silently skipped); originated as C-24 in R7
4. **Model cell + locatability assertion** — binary YES/NO field at Phase 2 entry catches evidence that passes C-11/C-14 (anchor exists, placed correctly) but fails C-23 (unlocatable)
5. **Coverage assertion as phase-boundary table** — section 1e maps all 24 criteria to confirmed or DEFERRED locations; makes total Inertia coverage confirmable in one scan rather than a full re-read
ions 1a through 1e in order. Do not proceed to Phase 2 until all five sections
are written, the bilateral audit shows no Symmetric: NO rows and no blank PARTIAL Reason cells,
and the coverage assertion is complete.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-24 aspirational)
  (b) the exact composite formula text (v8 active: /16 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

Required field:

  Inertia (C-01): Without this load block, criteria count (24), denominator (/16),
  and threshold are unverified -- C-23/C-24 rows missing and composites use /14.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior unknown: "No prior version delta detectable -- scoring under v8 as baseline."

Required field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15 -- prior value (14)
  required; both sides confirm the transition.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

Required field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? | Reason (if PARTIAL) |
  |------------|-----------|---------------------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A] | [reason or "--"] |
  | Regression verdicts | [YES | NO -- [missing] | PARTIAL] | [reason or "--"] |
  | Arithmetic discrepancies | [YES | NO -- [missing] | PARTIAL] | [reason or "--"] |

Verdict rules:
  - Symmetric: YES -- both sides present (Reason: "--"). NO -- any side missing; remediate
    before Phase 2 (Reason: "--").
  - Symmetric: PARTIAL -- N/A rule invoked correctly. Reason column REQUIRED --
    e.g., "PARTIAL -- no prior-round data; N/A rule applied correctly".
    Blank Reason cell = structural violation (remediate before Phase 2).

Required field:

  Inertia (C-18, C-24): Register prevents asymmetric entries; sweep catches them independently.
  The Reason column resolves ambiguity: bare PARTIAL is indistinguishable between an N/A rule,
  a clean result, and a silently-skipped comparison.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

Verify that every criterion ID (C-01 through C-24) appears in at least one Inertia label.
Produce this assertion:

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18, C-24): at 1d |
  | C-24 | YES | Inertia (C-18, C-24): at 1d |
  | C-20 | YES | Inertia (C-20, C-21): at 1e |
  | C-21 | YES | Inertia (C-20, C-21): at 1e |
  | C-11, C-14, C-19, C-23 | DEFERRED | Covered by MODEL CELL + ENTRY LOCK + LOCATABILITY ASSERTION at Phase 2 entry |
  | C-12 | DEFERRED | Covered by arithmetic verification block at 3a |
  | C-09 | DEFERRED | Covered by regression section at 3b |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-22 | DEFERRED | Covered by Phase 2 scoring and synthesis mechanisms |

For any criterion not appearing: add it to DEFERRED with intended coverage location.

Required field:

  Inertia (C-20, C-21): Bare "Inertia: [text]" satisfies C-17 but fails C-20. C-21 requires
  this phase-boundary assertion: total inertia-label coverage confirmable by reading one table,
  not by scanning every label.

PHASE 1 COMPLETE -- proceed only after 1a-1e written, no Symmetric: NO rows,
no blank PARTIAL Reason cells.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + LOCATABILITY ASSERTION + ENTRY LOCK (Phase 2 entry -- write before any verdict row)**

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural
  observation that locates a specific feature in the output -- not a criterion restatement]"

(2) Locatability assertion:
  Locatability test: [YES -- findable at [section] in [output ID] without searching the
  full output | NO -- criterion restatement or not locatable; rewrite before proceeding]

  Rules:
  - Both fields are required. A missing Locatability test field earns C-23 FAIL.
  - Writing YES when the evidence text does not name a specific locatable section or quote
    earns C-23 FAIL -- the assertion must be accurate, not automatic.

(3) Required labeled field:

  Inertia (C-11, C-14, C-23): Model cell at Phase 2 entry prevents evidence defaulting to
  criterion restatement. Locatability assertion catches a model cell that passes C-11/C-14
  but has unlocatable evidence -- C-23 fails if the test is omitted.

(4) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  The ENTRY LOCK field is required; omitting it earns C-19 FAIL.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - Every Inertia label must use criterion-ID anchoring: "Inertia (C-XX): [failure mode]"
    -- not bare "Inertia: [failure mode]".
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/16
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/16 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

Required field:

  Inertia (C-12): YES/NO binary field required. Narrative verification does not satisfy C-12.

**3b. Regression section**

  If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

Required field:

  Inertia (C-09): Section required even when empty.

---

SYNTHESIS

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly with tiebreak rule or
"tied -- no tiebreak applied." "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

Generic rankings are not excellence signals. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**NON-ADDITIVITY ANALYSIS**

For each pair of variations where one uses a strict subset of the other's axes:
  Increment = variation_with_more_axes.composite - variation_with_fewer_axes.composite

For any pair where Increment = 0:

  Redundant axis: [name]
  Criterion target: [criterion]
  Subsuming mechanism: [specific mechanism in the other axis that performs the same function]

All three fields are required. Zero-increment declaration without subsuming mechanism = PARTIAL on C-22.

If no zero-increment pair: "No non-additivity observed -- all axes produced positive increment."
If single variation scored: "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed.

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## What Made It Golden

### 1. Formula-change alert before any computation (C-13, C-15)

The prompt opens with a FORMULA CHANGE ALERT block that names both the prior value (14, v7)
and the current value (16, v8) before Phase 1 begins. This is the only mechanism that prevents
a scorer from loading the correct rubric but silently computing all composites with the wrong
denominator. Without the alert, N_aspirational=16 is visible in Phase 1 but the prior-vs-current
contrast is never forced -- C-15 fails because only the current side is named.

### 2. Symmetric Delta Register with two-column enforcement (C-15, C-18)

The SYMMETRIC DELTA REGISTER requires a Prior state column and a Current state column for every
comparison row. A blank Prior state cell is a visible structural violation -- detectable by
column scan without reading prose. Variations that state only the current formula parameter
(e.g., "N_aspirational=16") produce an invisible one-sided assertion; the register makes the
omission structural rather than logical.

### 3. Bilateral audit PARTIAL-reason labeling (C-24)

Every PARTIAL verdict in the bilateral sweep requires a labeled Reason cell -- e.g.,
"PARTIAL -- no prior-round data; N/A rule applied correctly". A bare PARTIAL is ambiguous
between three distinct conditions (N/A rule invoked, no discrepancy found, silently skipped)
that are indistinguishable by scanning. The Reason column resolves this without requiring
re-reading underlying prose. This pattern originated as C-24 in R7 and became load-bearing
for the R8 champion.

### 4. Model cell + locatability assertion at Phase 2 entry (C-11, C-14, C-23)

The MODEL CELL provides a worked positive example of what constitutes acceptable evidence
(a verbatim quote or named structural feature, not criterion restatement) and must appear
before the first verdict row (C-14). The LOCATABILITY ASSERTION adds a binary YES/NO field
requiring the scorer to affirm that the model evidence is findable at a specific section
without searching the full output. An output can pass C-11 and C-14 (anchor exists, placed at
entry) while failing C-23 if the evidence text is unlocatable -- the assertion catches this
gap with a single required field.

### 5. Coverage assertion as a phase-boundary table (C-20, C-21)

Section 1e produces a single table mapping every criterion ID (C-01 through C-24) to either
a confirmed Inertia-label location or a DEFERRED coverage location in Phase 2/3. This makes
total Inertia coverage confirmable by reading one table rather than scanning every label in
the output. Without this, C-20 (criterion-ID anchoring on every Inertia label) and C-21
(phase-boundary assertion for coverage completeness) can only be verified by full re-read.

---

## Final Rubric Criteria Summary

**Rubric**: quest-score-rubric-v8-2026-03-16.md
**Total criteria**: 24 (C-01 through C-24)
**Formula**: composite = (E/5 * 60) + (R/3 * 30) + (A/16 * 10); PARTIAL = 0.5
**Golden threshold**: ALL 5 essentials PASS AND composite >= 80

| ID | Tier | Text (short) | Category |
|----|------|--------------|----------|
| C-01 | Essential | Rubric load verification | correctness |
| C-02 | Essential | Per-criterion verdict matrix | correctness |
| C-03 | Essential | Evidence for every verdict | correctness |
| C-04 | Essential | Composite score per output with explicit calculation | correctness |
| C-05 | Essential | Failure patterns section (required even when empty) | coverage |
| C-06 | Recommended | Ranked leaderboard | format |
| C-07 | Recommended | Excellence signals | depth |
| C-08 | Recommended | Per-output synthesis notes | depth |
| C-09 | Aspirational | Regression signals (PARTIAL if no prior data, not FAIL) | behavior |
| C-10 | Aspirational | Score arithmetic verification | correctness |
| C-11 | Aspirational | Evidence positive anchor (model cell) | depth |
| C-12 | Aspirational | Discrepancy declaration (binary YES/NO field) | correctness |
| C-13 | Aspirational | Formula version delta declaration | correctness |
| C-14 | Aspirational | Pre-scoring mechanism placement (model cell at Phase 2 entry) | correctness |
| C-15 | Aspirational | Symmetric comparison completeness (both sides of every delta) | correctness |
| C-16 | Aspirational | [see rubric] | -- |
| C-17 | Aspirational | Criterion-ID anchoring on every Inertia label | correctness |
| C-18 | Aspirational | Bilateral symmetry audit sweep | correctness |
| C-19 | Aspirational | Entry lock binary gate declaration | correctness |
| C-20 | Aspirational | Criterion-ID anchoring completeness (all labels use C-XX format) | correctness |
| C-21 | Aspirational | Phase-boundary coverage assertion | correctness |
| C-22 | Aspirational | Non-additivity analysis (required section) | depth |
| C-23 | Aspirational | Model evidence locatability assertion (binary YES/NO) | correctness |
| C-24 | Aspirational | Bilateral audit PARTIAL-reason labeling | correctness |

**Convergence**: R9 confirmed no new patterns. V-05 (P+Q+R+U+V) and V-04 (P+Q+R+U+V+X) tied at
99.6875 without prior-round data. V-04 is capability-equivalent -- achieves C-09 PASS when called
with a prior-round scorecard. The simplified prompt (21% reduction, PASS) is the canonical form.
