# quest-score -- R10 Variations
Generated: 2026-03-15

## R10 Design Notes

V-01 is the R10 full-stack baseline: all R9 learnings retained, N_aspirational updated from 18
to 20 to reflect the two new aspirational criteria C-26 (C-25 principle includes concrete
application inventory) and C-27 (regression signals table includes Variation column). The
criterion roster expands from 25 to 27 rows. The C-25 "Applied in this rubric" inventory now
lists 4 paired entries (C-23 for C-20, C-24 for C-22, C-26 for C-25, C-27 for C-18) -- satisfying
C-26. The REGRESSION SIGNALS table template has 5 columns including Variation -- satisfying C-27.
C-11 auto-PASS declarations updated to include C-27. C-09 contribution note updated to 0.5 pt.

V-02 is the C-26 PARTIAL ablation: the C-25 "Applied in this rubric" inventory names only the
applying criterion IDs (C-23, C-24, C-26, C-27) without pairing them to their target criterion
IDs. C-26 PARTIAL expected. All other R10 structures identical to V-01 including the standalone
C-25 principle section and the 5-column regression table.

V-03 is the C-26 FAIL ablation: the C-25 section states the general three-scale enumeration
principle but contains no "Applied in this rubric" inventory at all. C-26 FAIL expected. All
other R10 structures identical to V-01 including the 5-column regression table.

V-04 is the C-27 PARTIAL ablation: all C-26 structures present (full paired inventory in C-25),
but the REGRESSION SIGNALS table template has only 4 columns (Criterion | Prior Verdict | Current
Verdict | Mechanism) -- the Variation column is absent. C-27 PARTIAL expected.

V-05 is the C-26 FAIL + C-27 PARTIAL combination: the C-25 section contains no "Applied in this
rubric" inventory (C-26 FAIL), and the REGRESSION SIGNALS table template has only 4 columns
(C-27 PARTIAL). This is the floor variation -- maximum contrast with V-01.

C-26 evidence ladder: V-03 (no inventory = FAIL); V-05 (no inventory = FAIL); V-02 (inventory
present, target IDs absent = PARTIAL); V-01 (full paired inventory = PASS); V-04 (full paired
inventory = PASS).

C-27 evidence ladder: V-04 (Variation column absent = PARTIAL); V-05 (Variation column absent =
PARTIAL); V-01/V-02/V-03 (5-column table = PASS).

---

## V-01

**Axis:** Baseline -- R10 full stack (N_aspirational=20, 27-row criterion roster, C-26 PASS:
C-25 inventory names both applying criterion ID and target criterion ID for all 4 entries; C-27
PASS: regression signals table has 5 columns including Variation; C-11 includes C-27 auto-PASS
declaration; all R9 V-01 structures retained unchanged)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The criterion roster will contain exactly 27 rows (C-01 through C-27), the composite formula will use N_aspirational=20, the C-25 "Applied in this rubric" inventory will list 4 paired entries naming both applying criterion ID and target criterion ID, and the REGRESSION SIGNALS table template will have 5 columns including Variation -- absence of any one property clearly falsifies the R10-complete claim |
| Secondary effect | Expanding the criterion roster from 25 to 27 rows increases SETUP token density by two additional diagnostic-question rows; the C-26 three-scale diagnostic question adds the most complexity since it must enumerate FAIL/PARTIAL/PASS cases for the inventory criterion itself; under token pressure, later variations may compress the C-25 inventory to criterion IDs only (V-02 ablation site) or drop the Variation column from the regression template (V-04 ablation site) |
| Predicted sites | V-02 and V-03 (C-26 ablations) are the direct contrasts for C-25 inventory completeness; V-04 (C-27 PARTIAL) is the direct contrast for regression table column count; V-05 (combined floor) establishes the lowest boundary for both new criteria |

---

Score N skill outputs against the v10 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
quote. Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring
unusually high on a specific criterion. Failure patterns: criteria failing across ALL outputs
(rubric gap or skill design issue?). Regression signals: outputs that passed in a prior round
but fail in this round.

---

### PHASE 1 -- SETUP

*Complete all steps below before opening any output file.*

---

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. When C-05
auto-PASS fires, C-08, C-10, and C-21 also auto-PASS -- no universal failures to diagnose,
exemplify, or locate.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS fires,
write: "Prior-round scorecard not provided. C-07 auto-PASS -- no regression comparison possible."
When C-07 auto-PASS fires, C-27 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS
action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation
checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL,
and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient
for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18).
When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before
writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 20 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 20.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/20 = 0.5 pt to the composite. Achieving composite
>= 100 requires 20/20 aspirational PASS -- there is no room for any aspirational FAIL at the
ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 27 verdict rows (C-01 through C-27) in the scoring table, with none missing or duplicated? A matrix with 25 or 26 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=20? Can you re-derive the composite from the 27 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=20 within +/-1 rounding tolerance? An output using N_aspirational=18 (v9 values) or N_aspirational=16 (v8 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all six auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=20 (v10 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=18) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-27 with a non-empty diagnostic question for each? A roster with 25 or 26 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 27 rows), C-03 (N-value check: N_aspirational=20), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs -- e.g., "Applied in this rubric: C-23, C-24, C-26, C-27" without specifying which criterion each targets; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. Note: Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 27-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-27 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-27): X/20 x 10 = YY.YY pts
- Composite = YY.YY/100
- Golden: YES/NO -- all 4 essentials PASS, YY.YY >= 80
```

---

### PHASE 3 -- Synthesis

#### FAILURE PATTERNS

Check for criteria with FAIL or PARTIAL in every scored output.

If none: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS.
C-21 auto-PASS.**

If universal failures exist, for each:
- **Criterion**: [ID and name]
- **Pattern**: [description of how the criterion fails or partially fails across all outputs]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is
  satisfied on every run.

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction to
the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score,
spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or
discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier
(PASS vs. PARTIAL or PARTIAL vs. FAIL):
- Name the criterion
- Name the output
- State what the output did differently from the group majority

---

#### REGRESSION SIGNALS

If prior-round scorecard data is provided, C-07 auto-PASS does NOT apply.

| Criterion | Prior Verdict | Current Verdict | Variation | Mechanism |
|-----------|--------------|-----------------|-----------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread).
Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the
composite; the two-failure floor (one FAIL + one PARTIAL) incurs 0.75 pt total degradation from
the ceiling.

---

## V-02

**Axis:** C-26 PARTIAL ablation -- C-25 "Applied in this rubric" inventory lists applying
criterion IDs only, without pairing each to its target criterion ID; C-26 PARTIAL expected;
all other R10 structures including C-27 5-column regression table identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-25 section will contain an "Applied in this rubric:" list naming C-23, C-24, C-26, C-27 without specifying which criterion each targets -- the absence of the paired target IDs is the falsifying property for C-26 PARTIAL vs. PASS; a scorer applying C-26 correctly will award PARTIAL, not PASS, because entries lack the target criterion ID field |
| Secondary effect | The C-25 standalone principle block is intact and the C-27 5-column regression table is intact, so C-25 PASS and C-27 PASS should hold; C-26 PARTIAL is the only new degradation relative to V-01; C-24 PASS is unaffected since the C-22 diagnostic question is identical to V-01 |
| Predicted sites | V-01 (full paired inventory) is the direct upward contrast; V-03 (no inventory) is the direct downward contrast; the spread V-03 FAIL / V-02 PARTIAL / V-01 PASS establishes the C-26 discrimination ladder |

---

Score N skill outputs against the v10 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
quote. Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring
unusually high on a specific criterion. Failure patterns: criteria failing across ALL outputs
(rubric gap or skill design issue?). Regression signals: outputs that passed in a prior round
but fail in this round.

---

### PHASE 1 -- SETUP

*Complete all steps below before opening any output file.*

---

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. When C-05
auto-PASS fires, C-08, C-10, and C-21 also auto-PASS -- no universal failures to diagnose,
exemplify, or locate.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS fires,
write: "Prior-round scorecard not provided. C-07 auto-PASS -- no regression comparison possible."
When C-07 auto-PASS fires, C-27 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS
action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation
checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL,
and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient
for these criteria.

**Applied in this rubric:** C-23, C-24, C-26, C-27. When authoring a new criterion with a
non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 20 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 20.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 27 verdict rows (C-01 through C-27) in the scoring table, with none missing or duplicated? A matrix with 25 or 26 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=20? Can you re-derive the composite from the 27 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=20 within +/-1 rounding tolerance? An output using N_aspirational=18 (v9 values) or N_aspirational=16 (v8 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all six auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=20 (v10 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=18) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-27 with a non-empty diagnostic question for each? A roster with 25 or 26 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 27 rows), C-03 (N-value check: N_aspirational=20), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs -- e.g., "Applied in this rubric: C-23, C-24, C-26, C-27" without specifying which criterion each targets; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. Note: Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 27-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-27 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-27): X/20 x 10 = YY.YY pts
- Composite = YY.YY/100
- Golden: YES/NO -- all 4 essentials PASS, YY.YY >= 80
```

---

### PHASE 3 -- Synthesis

#### FAILURE PATTERNS

Check for criteria with FAIL or PARTIAL in every scored output.

If none: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS.
C-21 auto-PASS.**

If universal failures exist, for each:
- **Criterion**: [ID and name]
- **Pattern**: [description of how the criterion fails or partially fails across all outputs]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is
  satisfied on every run.

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction to
the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score,
spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or
discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier
(PASS vs. PARTIAL or PARTIAL vs. FAIL):
- Name the criterion
- Name the output
- State what the output did differently from the group majority

---

#### REGRESSION SIGNALS

If prior-round scorecard data is provided, C-07 auto-PASS does NOT apply.

| Criterion | Prior Verdict | Current Verdict | Variation | Mechanism |
|-----------|--------------|-----------------|-----------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread).
Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the
composite; the two-failure floor (one FAIL + one PARTIAL) incurs 0.75 pt total degradation from
the ceiling.

---

## V-03

**Axis:** C-26 FAIL ablation -- C-25 section states the general three-scale enumeration principle but contains no "Applied in this rubric" inventory at all; C-26 FAIL expected; all other R10 structures including C-27 5-column regression table identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-25 section will be a standalone named block containing the general design rule prose but no "Applied in this rubric:" list of any kind -- the complete absence of any inventory is the falsifying property for C-26 FAIL vs. PARTIAL; a scorer applying C-26 correctly will award FAIL because no inventory exists to carry the paired entries |
| Secondary effect | C-25 PASS holds (standalone named section present with the general rule); C-27 PASS holds (5-column regression table intact); C-26 FAIL is the only degradation from V-01; the cost is exactly 0.5 pt from the aspirational budget |
| Predicted sites | V-02 (applying-IDs-only inventory = PARTIAL) is the direct upward contrast; V-01 (full paired inventory = PASS) is the ceiling contrast; V-05 (combined floor with no inventory) shares C-26 FAIL but adds C-27 PARTIAL degradation |

---

Score N skill outputs against the v10 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote. Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

---

### PHASE 1 -- SETUP

*Complete all steps below before opening any output file.*

---

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. When C-05 auto-PASS fires, C-08, C-10, and C-21 also auto-PASS -- no universal failures to diagnose, exemplify, or locate.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS fires, write: "Prior-round scorecard not provided. C-07 auto-PASS -- no regression comparison possible." When C-07 auto-PASS fires, C-27 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression table is instantiated).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion whose PARTIAL verdict is defined by having exactly one of two required elements present (and the other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient for these criteria. When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 20 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 20.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 27 verdict rows (C-01 through C-27) in the scoring table, with none missing or duplicated? A matrix with 25 or 26 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=20? Can you re-derive the composite from the 27 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=20 within +/-1 rounding tolerance? An output using N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? Placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster or discriminate? Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all six auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=20 (v10 values) appear in SETUP before any per-output heading opens? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-27 with a non-empty diagnostic question for each? A roster with 25 or 26 rows fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block separate from the criterion roster? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 27 rows), C-03 (N-value check: N_aspirational=20), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism)? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form earns C-19 PARTIAL and C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative earns C-19 PARTIAL + C-20 FAIL; (2) conditional earns C-20 FAIL; (3) weak-modal earns C-20 FAIL. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion. FAIL: rule is imperative but contains no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, and (3) weak-modal? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID. |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns; (PARTIAL) regression table has the 4 required C-18 columns but the Variation column is absent; (PASS) table has all 5 columns including Variation. Note: Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 27-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-27 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the criterion being scored
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-27): X/20 x 10 = YY.YY pts
- Composite = YY.YY/100
- Golden: YES/NO -- all 4 essentials PASS, YY.YY >= 80
```

---

### PHASE 3 -- Synthesis

#### FAILURE PATTERNS

Check for criteria with FAIL or PARTIAL in every scored output.

If none: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS.**

If universal failures exist, for each:
- **Criterion**: [ID and name]
- **Pattern**: [description of how the criterion fails or partially fails across all outputs]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is satisfied on every run.

Example of a fully instantiated action line: "Add a Score distribution note instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster or discriminate -- so C-09 is satisfied on every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently from the group majority

---

#### REGRESSION SIGNALS

If prior-round scorecard data is provided, C-07 auto-PASS does NOT apply.

| Criterion | Prior Verdict | Current Verdict | Variation | Mechanism |
|-----------|--------------|-----------------|-----------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster or discriminate. Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

---

## V-04

**Axis:** C-27 PARTIAL ablation -- REGRESSION SIGNALS table template has only 4 columns (Criterion | Prior Verdict | Current Verdict | Mechanism); Variation column absent; C-27 PARTIAL expected; all other R10 structures including C-26 PASS (full paired inventory) identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The REGRESSION SIGNALS table template will have exactly 4 columns matching the C-18 minimum requirement but missing the Variation column required by C-27; a scorer applying C-27 correctly will award PARTIAL, not FAIL, because C-18 is satisfied and only the fifth column is absent |
| Secondary effect | C-26 PASS holds (full paired inventory in C-25 section intact); C-18 PASS holds (4-column table satisfies C-18 minimum); C-27 PARTIAL is the only degradation from V-01; the cost is exactly 0.25 pt from the aspirational budget (PARTIAL = 0.5 credit on a 0.5 pt criterion) |
| Predicted sites | V-01/V-02/V-03 (5-column table = C-27 PASS) are the upward contrasts for C-27; V-05 (combined floor with 4-column table) shares C-27 PARTIAL; the V-04/V-05 pair establishes that C-27 PARTIAL is achievable independently of C-26 verdict |

---

Score N skill outputs against the v10 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote. Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

---

### PHASE 1 -- SETUP

*Complete all steps below before opening any output file.*

---

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. When C-05 auto-PASS fires, C-08, C-10, and C-21 also auto-PASS -- no universal failures to diagnose, exemplify, or locate.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS fires, write: "Prior-round scorecard not provided. C-07 auto-PASS -- no regression comparison possible." When C-07 auto-PASS fires, C-27 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression table is instantiated).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion whose PARTIAL verdict is defined by having exactly one of two required elements present (and the other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18). When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 20 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 20.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 27 verdict rows (C-01 through C-27) in the scoring table, with none missing or duplicated? A matrix with 25 or 26 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=20? Can you re-derive the composite from the 27 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=20 within +/-1 rounding tolerance? An output using N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? Placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster or discriminate? Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all six auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=20 (v10 values) appear in SETUP before any per-output heading opens? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-27 with a non-empty diagnostic question for each? A roster with 25 or 26 rows fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block separate from the criterion roster? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 27 rows), C-03 (N-value check: N_aspirational=20), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism)? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional, (3) weak-modal. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: rule names (a) but omits (b). FAIL: rule is imperative but contains no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, and (3) weak-modal? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases? (FAIL) rule is imperative but contains no location language; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) no inventory -- only the general principle stated in prose; (PARTIAL) inventory present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID. |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Variation. Note: Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 27-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-27 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the criterion being scored
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-27): X/20 x 10 = YY.YY pts
- Composite = YY.YY/100
- Golden: YES/NO -- all 4 essentials PASS, YY.YY >= 80
```

---

### PHASE 3 -- Synthesis

#### FAILURE PATTERNS

Check for criteria with FAIL or PARTIAL in every scored output.

If none: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS.**

If universal failures exist, for each:
- **Criterion**: [ID and name]
- **Pattern**: [description of how the criterion fails or partially fails across all outputs]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is satisfied on every run.

Example of a fully instantiated action line: "Add a Score distribution note instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster or discriminate -- so C-09 is satisfied on every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently from the group majority

---

#### REGRESSION SIGNALS

If prior-round scorecard data is provided, C-07 auto-PASS does NOT apply.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster or discriminate. Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

---

## V-05

**Axis:** C-26 FAIL + C-27 PARTIAL floor -- C-25 section contains no "Applied in this rubric" inventory (C-26 FAIL) AND the REGRESSION SIGNALS table template has only 4 columns with Variation absent (C-27 PARTIAL); this is the floor variation establishing maximum contrast with V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-25 section will state the general three-scale enumeration principle as a standalone named block but contain no inventory, and the REGRESSION SIGNALS table will have only 4 columns -- the two ablations are independent and should each score exactly as their single-axis counterparts (C-26 FAIL from V-03, C-27 PARTIAL from V-04); composite = 99.25 |
| Secondary effect | C-25 PASS holds (standalone named section present); C-18 PASS holds (4-column table satisfies C-18); combined degradation is exactly 0.75 pt (C-26 FAIL = 0.5 pt + C-27 PARTIAL = 0.25 pt); all essential and recommended criteria should PASS |
| Predicted sites | V-03 (C-26 FAIL only, C-27 PASS) establishes C-26 cost; V-04 (C-27 PARTIAL only, C-26 PASS) establishes C-27 cost; V-01 (both PASS) is the ceiling; the spread of 0.75 pt confirms the criteria are strictly independent -- no interaction effect |

---

Score N skill outputs against the v10 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote. Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

---

### PHASE 1 -- SETUP

*Complete all steps below before opening any output file.*

---

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. When C-05 auto-PASS fires, C-08, C-10, and C-21 also auto-PASS -- no universal failures to diagnose, exemplify, or locate.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS fires, write: "Prior-round scorecard not provided. C-07 auto-PASS -- no regression comparison possible." When C-07 auto-PASS fires, C-27 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression table is instantiated).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion whose PARTIAL verdict is defined by having exactly one of two required elements present (and the other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient for these criteria. When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 20 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 20.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/20 = 0.5 pt to the composite.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 27 verdict rows (C-01 through C-27) in the scoring table, with none missing or duplicated? A matrix with 25 or 26 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=20? Can you re-derive the composite from the 27 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=20 within +/-1 rounding tolerance? An output using N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? Placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster or discriminate? Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all six auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=20 (v10 values) appear in SETUP before any per-output heading opens? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-27 with a non-empty diagnostic question for each? A roster with 25 or 26 rows fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block separate from the criterion roster? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 27 rows), C-03 (N-value check: N_aspirational=20), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism)? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional, (3) weak-modal. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: rule names (a) but omits (b). FAIL: rule is imperative but contains no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, and (3) weak-modal? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases? (FAIL) rule is imperative but contains no location language; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) no inventory -- only the general principle stated in prose; (PARTIAL) inventory present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID. |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns; (PARTIAL) regression table has the 4 required C-18 columns but the Variation column is absent; (PASS) table has all 5 columns including Variation. Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 27-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-27 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the criterion being scored
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-27): X/20 x 10 = YY.YY pts
- Composite = YY.YY/100
- Golden: YES/NO -- all 4 essentials PASS, YY.YY >= 80
```

---

### PHASE 3 -- Synthesis

#### FAILURE PATTERNS

Check for criteria with FAIL or PARTIAL in every scored output.

If none: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS.**

If universal failures exist, for each:
- **Criterion**: [ID and name]
- **Pattern**: [description of how the criterion fails or partially fails across all outputs]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is satisfied on every run.

Example of a fully instantiated action line: "Add a Score distribution note instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster or discriminate -- so C-09 is satisfied on every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently from the group majority

---

#### REGRESSION SIGNALS

If prior-round scorecard data is provided, C-07 auto-PASS does NOT apply.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|--------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster or discriminate. Note that N_aspirational=20 means each aspirational criterion contributes 10/20 = 0.5 pt to the composite; the combined floor (C-26 FAIL + C-27 PARTIAL) incurs exactly 0.75 pt total degradation from the ceiling.
