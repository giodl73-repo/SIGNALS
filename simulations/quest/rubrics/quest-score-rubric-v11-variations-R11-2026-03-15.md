# quest-score -- R11 Variations
Generated: 2026-03-15

## R11 Design Notes

V-01 is the R11 full-stack baseline: all R10 learnings retained, N_aspirational updated from 20
to 22 to reflect the two new aspirational criteria C-28 (regression signals Variation column in
causal position) and C-29 (auto-PASS cascade dependencies name triggering criterion). The criterion
roster expands from 27 to 29 rows. The C-25 "Applied in this rubric" inventory now lists 6 paired
entries (C-23 for C-20, C-24 for C-22, C-26 for C-25, C-27 for C-18, C-28 for C-27, C-29 for
C-16) -- satisfying C-26. The C-28 auto-PASS declaration reads "C-28 auto-PASS when C-07 auto-PASS
fires" -- naming the triggering criterion ID, satisfying C-29. The REGRESSION SIGNALS table
template has 5 columns with Variation in causal position (col 4): Criterion | Prior Verdict |
Current Verdict | Variation | Mechanism -- satisfying C-28. C-11 auto-PASS declarations updated to
include C-28 and C-29. C-07 cascade note updated to cover C-27 and C-28.

V-02 is the C-28 PARTIAL ablation: all C-29 structures intact including the trigger-ID cascade
declaration ("C-28 auto-PASS when C-07 auto-PASS fires"), but the REGRESSION SIGNALS table
template appends Variation as column 5 after Mechanism: Criterion | Prior Verdict | Current Verdict
| Mechanism | Variation. C-27 PASS (Variation column present) but C-28 PARTIAL (not in causal
position). Single-axis isolation: only the regression table column order differs from V-01.

V-03 is the C-29 PARTIAL ablation: all C-28 structures intact including the 5-column causal
regression table (col 4), but the C-28 auto-PASS declaration repeats the underlying condition
without naming the triggering criterion: "C-28 auto-PASS when no prior-round data is available."
C-16 PASS (named declaration present), C-11 PASS (declaration in required list), C-29 PARTIAL
(trigger ID C-07 absent from the cascade declaration). Single-axis isolation: only the cascade
declaration form differs from V-01.

V-04 is the C-29 FAIL ablation: the C-28 auto-PASS declaration is entirely absent from the
auto-PASS block. C-11 FAIL (required C-28 declaration missing from the list), C-29 FAIL
(cascade-dependent criterion absent from declarations block entirely). The 5-column causal
regression table is intact, and the C-29 auto-PASS declaration remains in the block -- confirming
that C-29 FAIL is triggered by C-28's absence, not by C-29's own declaration. Controlled co-failure:
one structural decision (removing the cascade declaration block entry) causes C-11 FAIL + C-29 FAIL
simultaneously.

V-05 is the C-28 PARTIAL + C-29 PARTIAL combination floor: regression table appends Variation as
col 5 (C-28 PARTIAL) AND the C-28 cascade declaration uses condition-repetition form (C-29 PARTIAL).
This is the maximum contrast with V-01 for the two new criteria while preserving all other R11
structures. Expected additive degradation: ~0.45 pt (two PARTIAL verdicts) vs. V-01.

C-28 evidence ladder: V-02 PARTIAL (col 5 after Mechanism); V-05 PARTIAL (col 5); V-01 PASS (col 4 causal position).
C-29 evidence ladder: V-04 FAIL (absent); V-03 PARTIAL (condition, no trigger ID); V-05 PARTIAL (condition, no trigger ID); V-01 PASS (names C-07).

---

## V-01

**Axis:** Baseline -- R11 full stack (N_aspirational=22, 29-row criterion roster, C-28 PASS:
regression table has 5 columns with Variation in causal col 4; C-29 PASS: C-28 cascade declaration
names triggering criterion C-07; C-25 inventory names all 6 paired entries; C-11 includes C-28 and
C-29 declarations; all R10 V-01 structures retained unchanged)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The criterion roster will contain exactly 29 rows (C-01 through C-29), the composite formula will use N_aspirational=22, the C-25 "Applied in this rubric" inventory will list 6 paired entries including "C-28 (for C-27)" and "C-29 (for C-16)", the C-28 auto-PASS declaration will read "C-28 auto-PASS when C-07 auto-PASS fires" naming the trigger criterion, and the REGRESSION SIGNALS table template will have 5 columns with Variation in column 4 between Current Verdict and Mechanism -- absence of any one property clearly falsifies the R11-complete claim |
| Secondary effect | Expanding the criterion roster from 27 to 29 rows increases SETUP token density by two additional diagnostic-question rows; the C-28 and C-29 three-scale diagnostic questions add the most complexity since each must enumerate FAIL/PARTIAL/PASS cases with column-order and cascade-form contrasting examples respectively; under token pressure, later variations may invert the regression table column order (V-02 ablation site) or simplify the cascade declaration to condition-only form (V-03/V-05 ablation site), shifting complexity FROM the auto-PASS block structural precision TO the regression table layout |
| Predicted sites | V-02 (col-5 regression table) is the direct contrast for C-28 PARTIAL; V-03 (condition-not-trigger-ID cascade) is the direct contrast for C-29 PARTIAL; V-04 (absent cascade declaration = C-29 FAIL + C-11 FAIL) is the floor for the cascade block; V-05 (combination: col 5 + condition form) establishes the lowest boundary for the two new criteria combined |

---

Score N skill outputs against the v11 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.

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

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18),
C-28 (for C-27), C-29 (for C-16). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 22.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. A single PARTIAL incurs
~0.23 pt degradation; a single FAIL incurs ~0.45 pt degradation. Achieving composite >= 100
requires 22/22 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 29 verdict rows (C-01 through C-29) in the scoring table, with none missing or duplicated? A matrix with 27 or 28 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=22? Can you re-derive the composite from the 29 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=22 within +/-1 rounding tolerance? An output using N_aspirational=20 (v10 values) or N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all eight auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, and C-29) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the eight declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=22 (v11 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=20) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-29 with a non-empty diagnostic question for each? A roster with 27 or 28 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 29 rows), C-03 (N-value check: N_aspirational=22), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs -- e.g., "Applied in this rubric: C-23, C-24, C-26, C-27, C-28, C-29" without specifying which criterion each targets; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; a 4-column table "Criterion | Prior Verdict | Current Verdict | Mechanism" fails both C-27 and C-28; (PARTIAL) 5 columns present but column order is "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" -- Variation in column 5 inverts the causal chain by placing the detection rule before the identified structural cause; (PASS) column order is "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism" -- Variation in causal position enables the reading: what criterion regressed, what changed structurally, how to detect recurrence. |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 (the cascade-dependent criterion in v11) is absent entirely from the auto-PASS declarations block -- no cascade reference of any form is present; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- e.g., "C-28 auto-PASS when no prior-round data is available" repeats the underlying condition without naming C-07 as the gating criterion, leaving the cascade graph invisible to a reader; (PASS) cascade declaration names the triggering criterion ID -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires" -- making the cascade graph readable without requiring full-list cross-referencing. |

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

1. Write a 29-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-29 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-29): X/22 x 10 = YY.YY pts
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
Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the
composite; a single PARTIAL incurs ~0.23 pt degradation from the ceiling.

---

## V-02

**Axis:** C-28 PARTIAL ablation -- REGRESSION SIGNALS table template appends Variation as column
5 after Mechanism (order: Criterion | Prior Verdict | Current Verdict | Mechanism | Variation);
C-27 PASS (Variation column present), C-28 PARTIAL (not in causal position); all other R11
structures including the trigger-ID cascade declaration ("C-28 auto-PASS when C-07 auto-PASS
fires") identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The REGRESSION SIGNALS template will show column order "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" -- Variation in column 5 after Mechanism; a scorer applying C-28 will award PARTIAL (5 columns present, Variation exists, but causal position violated); C-27 PASS is unaffected (Variation column is present); C-29 PASS is unaffected (the cascade declaration still reads "C-28 auto-PASS when C-07 auto-PASS fires" with trigger ID named) |
| Secondary effect | The inverted column order in the template shifts the causal reading: Mechanism (detection rule) precedes Variation (structural cause) in the header -- a scorer reading across the template reads "how to detect" before "what changed," inverting the intended diagnostic flow; this secondary effect is confined to C-28 PARTIAL since all other structural elements are identical to V-01; the auto-PASS block is unchanged, shifting no burden FROM declarations TO the regression template |
| Predicted sites | V-01 (col 4 causal order) is the direct upward contrast establishing C-28 PASS; V-05 (combination floor) shares the col-5 regression table as its C-28 ablation component -- V-02 and V-05 should both produce C-28 PARTIAL, confirming the column-order mechanism in isolation and in combination |

---

Score N skill outputs against the v11 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.

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

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18),
C-28 (for C-27), C-29 (for C-16). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 22.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. A single PARTIAL incurs
~0.23 pt degradation; a single FAIL incurs ~0.45 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 29 verdict rows (C-01 through C-29) in the scoring table, with none missing or duplicated? A matrix with 27 or 28 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=22? Can you re-derive the composite from the 29 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=22 within +/-1 rounding tolerance? An output using N_aspirational=20 (v10 values) or N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all eight auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, and C-29) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the eight declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=22 (v11 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=20) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-29 with a non-empty diagnostic question for each? A roster with 27 or 28 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 29 rows), C-03 (N-value check: N_aspirational=22), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs -- e.g., "Applied in this rubric: C-23, C-24, C-26, C-27, C-28, C-29" without specifying which criterion each targets; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; a 4-column table "Criterion | Prior Verdict | Current Verdict | Mechanism" fails both C-27 and C-28; (PARTIAL) 5 columns present but column order is "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" -- Variation in column 5 inverts the causal chain by placing the detection rule before the identified structural cause; (PASS) column order is "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism" -- Variation in causal position enables the reading: what criterion regressed, what changed structurally, how to detect recurrence. |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 (the cascade-dependent criterion in v11) is absent entirely from the auto-PASS declarations block -- no cascade reference of any form is present; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- e.g., "C-28 auto-PASS when no prior-round data is available" repeats the underlying condition without naming C-07 as the gating criterion, leaving the cascade graph invisible to a reader; (PASS) cascade declaration names the triggering criterion ID -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires" -- making the cascade graph readable without requiring full-list cross-referencing. |

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

1. Write a 29-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-29 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-29): X/22 x 10 = YY.YY pts
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

| Criterion | Prior Verdict | Current Verdict | Mechanism | Variation |
|-----------|--------------|-----------------|-----------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread).
Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the
composite; a single PARTIAL incurs ~0.23 pt degradation from the ceiling.

---

## V-03

**Axis:** C-29 PARTIAL ablation -- C-28 auto-PASS declaration uses condition-repetition form
("C-28 auto-PASS when no prior-round data is available") instead of trigger-ID form ("C-28
auto-PASS when C-07 auto-PASS fires"); C-16 PASS (named declaration present in standalone block),
C-11 PASS (C-28 declaration is in the required list), C-29 PARTIAL (trigger ID C-07 absent);
all other R11 structures including the 5-column causal regression table identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-28 auto-PASS declaration in Step 1.1 will read "C-28 auto-PASS when no prior-round data is available" -- the underlying condition is stated but the triggering criterion ID "C-07" is absent; a scorer applying C-29 correctly will award PARTIAL (cascade dependency declared, trigger ID absent); C-28 PASS is unaffected since the 5-column causal regression table is intact; C-11 PASS is unaffected since the declaration is present and named |
| Secondary effect | Using condition-repetition for the cascade declaration obscures the cascade graph: a reader inspecting the auto-PASS block sees "C-28 auto-PASS when no prior-round data available" and cannot determine that C-07 is the gating criterion without scanning all criteria; this shifts interpretive burden FROM the auto-PASS block structure TO the reader's cross-referencing effort; the degradation is confined to C-29 PARTIAL since all other structural elements (regression table order, C-25 inventory, C-11 completeness) are intact |
| Predicted sites | V-01 (trigger-ID form "C-07 auto-PASS fires") is the direct upward contrast establishing C-29 PASS; V-04 (cascade declaration absent = C-29 FAIL) is the direct downward contrast; V-05 (combination floor) shares the condition-not-trigger-ID cascade form as its C-29 ablation component -- V-03 and V-05 should both produce C-29 PARTIAL, confirming the trigger-ID mechanism in isolation and in combination |

---

Score N skill outputs against the v11 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when no prior-round data is available (no regression table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.

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

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18),
C-28 (for C-27), C-29 (for C-16). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 22.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. A single PARTIAL incurs
~0.23 pt degradation; a single FAIL incurs ~0.45 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 29 verdict rows (C-01 through C-29) in the scoring table, with none missing or duplicated? A matrix with 27 or 28 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=22? Can you re-derive the composite from the 29 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=22 within +/-1 rounding tolerance? An output using N_aspirational=20 (v10 values) or N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all eight auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, and C-29) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the eight declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=22 (v11 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=20) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-29 with a non-empty diagnostic question for each? A roster with 27 or 28 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 29 rows), C-03 (N-value check: N_aspirational=22), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs -- e.g., "Applied in this rubric: C-23, C-24, C-26, C-27, C-28, C-29" without specifying which criterion each targets; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns but Variation column absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; (PARTIAL) 5 columns present but column order is "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" -- Variation in column 5 inverts the causal chain; (PASS) column order is "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism" -- Variation in causal position. |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 is absent entirely from the auto-PASS declarations block; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- e.g., "C-28 auto-PASS when no prior-round data is available" repeats the condition without naming C-07; (PASS) cascade declaration names the triggering criterion: "C-28 auto-PASS when C-07 auto-PASS fires". |

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

1. Write a 29-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-29 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-29): X/22 x 10 = YY.YY pts
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
Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the
composite; a single PARTIAL incurs ~0.23 pt degradation from the ceiling.

---

## V-04

**Axis:** C-29 FAIL ablation -- C-28 auto-PASS declaration is entirely absent from the auto-PASS
block; C-11 FAIL (required C-28 declaration missing from the 8-item required list), C-29 FAIL
(cascade-dependent criterion absent from declarations block entirely); 5-column causal regression
table intact; C-29 auto-PASS declaration remains present (confirming C-29 FAIL is triggered by
C-28's absence, not by C-29's own omission); controlled co-failure: one structural decision
causes C-11 FAIL + C-29 FAIL simultaneously

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The auto-PASS block in Step 1.1 will contain declarations for C-05, C-07, C-08, C-10, C-21, C-27, and C-29 -- but no C-28 declaration of any form; C-11 FAIL (missing required C-28 declaration) and C-29 FAIL (cascade-dependent C-28 absent from block) will co-fire; the 5-column causal regression table remains intact (C-28 PASS would apply if the declaration existed), confirming that the co-failure is isolated to the absent declaration and not to the regression table structure |
| Secondary effect | Removing the C-28 cascade declaration shifts interpretive burden FROM the auto-PASS block TO the scorer -- the absence is not flagged anywhere in the SETUP; the scorer must notice the gap by comparing the block against C-11's required list; this creates a harder-to-detect failure than V-03's condition-repetition form (where a declaration IS present but malformed) -- the cascade structure is completely invisible rather than merely obscured; the secondary degradation is the C-11 FAIL co-fire, which adds a second aspirational FAIL beyond C-29 |
| Predicted sites | V-03 (condition present but trigger ID absent = C-29 PARTIAL) is the upward contrast at the PARTIAL tier; V-01 (trigger-ID form = C-29 PASS) is the ceiling contrast; V-05 (condition-not-trigger-ID = C-29 PARTIAL) does not share the V-04 mechanism -- V-04 is the only variation where C-28 is entirely absent, making V-04's C-29 FAIL the distinct floor case in the evidence ladder |

---

Score N skill outputs against the v11 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.

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

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18),
C-28 (for C-27), C-29 (for C-16). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 22.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. A single PARTIAL incurs
~0.23 pt degradation; a single FAIL incurs ~0.45 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 29 verdict rows (C-01 through C-29) in the scoring table, with none missing or duplicated? A matrix with 27 or 28 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=22? Can you re-derive the composite from the 29 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=22 within +/-1 rounding tolerance? An output using N_aspirational=20 (v10 values) or N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all eight auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, and C-29) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the eight declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=22 (v11 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=20) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-29 with a non-empty diagnostic question for each? A roster with 27 or 28 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 29 rows), C-03 (N-value check: N_aspirational=22), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns; (PARTIAL) 4-column table with Variation absent; (PASS) 5 columns including Variation. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; (PARTIAL) 5 columns with Variation in column 5 after Mechanism; (PASS) column order "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 is absent entirely from the auto-PASS declarations block; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- condition repeated without naming C-07; (PASS) "C-28 auto-PASS when C-07 auto-PASS fires" -- trigger ID C-07 named explicitly. |

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

1. Write a 29-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-29 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-29): X/22 x 10 = YY.YY pts
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
Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the
composite; a single FAIL incurs ~0.45 pt degradation from the ceiling.

---

## V-05

**Axis:** V-02 x V-03 combination -- REGRESSION SIGNALS table appends Variation as column 5 after
Mechanism (C-28 PARTIAL) AND C-28 auto-PASS declaration uses condition-repetition form without
trigger ID (C-29 PARTIAL); this is the combination floor for the two new R11 criteria; expected
additive degradation ~0.45 pt (two PARTIAL verdicts) from V-01; structural independence confirmed
if V-05 scores approximately between V-04 (two FAILs, ~0.91 pt below V-01) and V-02/V-03 (one
PARTIAL each, ~0.23 pt below V-01)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The auto-PASS block Step 1.1 will contain "C-28 auto-PASS when no prior-round data is available" (condition form, trigger ID absent) AND the REGRESSION SIGNALS table template will use column order "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" (Variation col 5); C-28 PARTIAL (col 5) and C-29 PARTIAL (condition form) will co-fire; C-11 PASS (C-28 declaration present in required list), C-16 PASS (declarations in standalone block), C-27 PASS (Variation column present) will all hold |
| Secondary effect | The two ablation axes are structurally independent: the col-5 regression table affects Phase 3 REGRESSION SIGNALS template only; the condition-based cascade declaration affects Phase 1 auto-PASS block only; their combination should produce additive degradation (~0.45 pt total: two PARTIAL at 0.23 pt each) without interaction effects, confirming that C-28 and C-29 measure distinct structural mechanisms and do not share a common failure mode; shifting both FROM their correct forms TO their PARTIAL states does not amplify the error beyond the additive prediction |
| Predicted sites | V-02 (C-28 PARTIAL alone, ~0.23 pt below V-01) and V-03 (C-29 PARTIAL alone, ~0.23 pt below V-01) are the single-ablation baselines; V-04 (C-11 FAIL + C-29 FAIL, ~0.91 pt below V-01) is the floor for the absent-declaration case; if V-05 scores ~0.45 pt below V-01 and V-04 scores ~0.91 pt below V-01, the structural independence of C-28 and C-29 is confirmed and the two mechanisms are additively independent |

---

Score N skill outputs against the v11 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when no prior-round data is available (no regression table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.

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

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18),
C-28 (for C-27), C-29 (for C-16). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 22 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 22.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. A single PARTIAL incurs
~0.23 pt degradation; a single FAIL incurs ~0.45 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 29 verdict rows (C-01 through C-29) in the scoring table, with none missing or duplicated? A matrix with 27 or 28 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=22? Can you re-derive the composite from the 29 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=22 within +/-1 rounding tolerance? An output using N_aspirational=20 (v10 values) or N_aspirational=18 (v9 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all eight auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, and C-29) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the eight declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=22 (v11 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=20) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-29 with a non-empty diagnostic question for each? A roster with 27 or 28 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 29 rows), C-03 (N-value check: N_aspirational=22), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or fewer than 4 columns; (PARTIAL) 4-column table, Variation absent; (PASS) 5 columns including Variation. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; (PARTIAL) 5 columns with Variation in column 5 after Mechanism; (PASS) column order "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 absent entirely from auto-PASS block; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- condition repeated without naming C-07; (PASS) "C-28 auto-PASS when C-07 auto-PASS fires" -- trigger ID C-07 named. |

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

1. Write a 29-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-29 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-29): X/22 x 10 = YY.YY pts
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

| Criterion | Prior Verdict | Current Verdict | Mechanism | Variation |
|-----------|--------------|-----------------|-----------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided.**

---

#### LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread).
Note that N_aspirational=22 means each aspirational criterion contributes 10/22 ≈ 0.45 pt to the
composite; two PARTIAL verdicts incur ~0.45 pt total degradation from the ceiling.
