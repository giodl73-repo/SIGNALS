# quest-score -- R8 Variations
Generated: 2026-03-15

## R8 Design Notes

V-01 is the R8 full-stack baseline: all R7 learnings retained, N_aspirational updated from 14 to
16 to reflect the two new aspirational criteria C-22 (preservation rule SETUP exclusion) and C-23
(C-20 three-form enumeration in diagnostic question). The criterion roster expands from 21 to 23
rows. The preservation rule in Step 1.1 now explicitly names FAILURE PATTERNS as the required
location AND names SETUP as a disqualifying alternative (satisfying C-22). The C-20 diagnostic
question in the roster now enumerates three grammatical form failures -- interrogative, conditional,
and weak-modal (satisfying C-23).

V-02 is the C-22 ablation: the preservation rule uses correct imperative form (passing C-19 and
C-20) but contains no location constraint -- it does not name FAILURE PATTERNS as required or
SETUP as disqualifying. C-22 FAIL expected.

V-03 is the C-23 PARTIAL ablation: the C-20 diagnostic question enumerates exactly two
grammatical form failures (interrogative + conditional) but omits weak-modal ("should"). C-23
PARTIAL expected.

V-04 is the C-23 FAIL ablation: the C-20 diagnostic question enumerates only one grammatical form
failure (interrogative). Conditional and weak-modal omitted. C-23 FAIL expected.

V-05 is the combination pass: all R8 structures retained from V-01, plus the C-22 diagnostic
question explicitly enumerates all three verdict cases (FAIL, PARTIAL, PASS) with structural
examples of each. This surfaces the PARTIAL/PASS boundary for C-22 that V-01 names but does not
fully illustrate -- potential C-24 seed: "C-22 diagnostic question enumerates all three verdict
cases with structural contrasting examples."

C-22 evidence: V-02 (imperative, no location constraint) = FAIL; V-01/V-03/V-04/V-05 (imperative
+ SETUP exclusion) = PASS.

C-23 evidence ladder: V-04 (1 form) = FAIL; V-03 (2 forms) = PARTIAL; V-01/V-02/V-05 (3 forms)
= PASS.

---

## V-01

**Axis:** Baseline -- R8 full stack (N_aspirational=16, C-22 SETUP exclusion embedded in
preservation rule, C-23 three-form enumeration in C-20 diagnostic question, 23-row criterion
roster; all R7 V-05 structures retained unchanged)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The criterion roster will contain exactly 23 rows (C-01 through C-23), the composite formula will use N_aspirational=16, and the C-20 diagnostic question will name all three disqualifying grammatical forms (interrogative, conditional, weak-modal) -- the absence of any one of these in the actual body would clearly falsify the claim that the baseline is R8-complete |
| Secondary effect | Expanding the criterion roster from 21 to 23 rows increases SETUP token density by approximately two diagnostic-question pairs, mildly increasing first-turn SETUP reproduction cost -- this may produce fractional compression in later-variation bodies under token pressure |
| Predicted sites | V-02 (C-22 ablation) is the direct contrast for preservation rule location language; V-03 and V-04 (C-23 ablations) are the direct contrasts for three-form enumeration; the compression effect may appear earliest in V-04 or V-05 as the token-heaviest ablation positions |

---

Score N skill outputs against the v8 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high
on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill
design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

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

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS
action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation
checkpoint.

---

#### Step 1.2 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 16.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/16 = 0.625 pt to the composite. Achieving composite
>= 99 requires at most one aspirational FAIL and no aspirational PARTIAL beyond that one.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 23 verdict rows (C-01 through C-23) in the scoring table, with none missing or duplicated? A matrix with 21 or 22 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=16? Can you re-derive the composite from the 23 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=16 within +/-1 rounding tolerance? An output using N_aspirational=14 (v7 values) or N_aspirational=12 (v6 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=16 (v8 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=14) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-23 with a non-empty diagnostic question for each? A roster with 21 or 22 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 23 rows), C-03 (N-value check: N_aspirational=16), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 23-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-23 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-23): X/16 x 10 = YY.YY pts
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
Note that N_aspirational=16 means each aspirational criterion contributes 10/16 = 0.625 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL.

---

## V-02

**Axis:** C-22 ablation -- preservation rule imperative form (C-19 PASS, C-20 PASS) but contains
no location constraint; neither FAILURE PATTERNS nor SETUP named as required or disqualifying in
the preservation rule text (C-22 FAIL expected)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The preservation rule in Step 1.1 will contain "must be carried forward verbatim" (satisfying C-19 and C-20) but will contain no phrase naming "FAILURE PATTERNS" as the required location or "SETUP" as a disqualifying alternative -- the absence of location constraint text in the preservation rule body is the falsifying structural property for C-22 |
| Secondary effect | A scorer applying the C-22 diagnostic question correctly will find the rule imperative (C-20 PASS) but location-silent, producing C-22 FAIL; a scorer who conflates C-20 and C-22 may award C-22 PASS because the rule is imperative, establishing the boundary between the two criteria as a measurement instrument |
| Predicted sites | V-01 (preservation rule with full SETUP exclusion) is the direct contrast; V-03 and V-04 are unaffected by the C-22 axis and should score identically to V-01 on C-22 |

---

Score N skill outputs against the v8 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high
on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill
design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

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

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder.

---

#### Step 1.2 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 16.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/16 = 0.625 pt to the composite. Achieving composite
>= 99 requires at most one aspirational FAIL and no aspirational PARTIAL beyond that one.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 23 verdict rows (C-01 through C-23) in the scoring table, with none missing or duplicated? A matrix with 21 or 22 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=16? Can you re-derive the composite from the 23 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=16 within +/-1 rounding tolerance? An output using N_aspirational=14 (v7 values) or N_aspirational=12 (v6 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=16 (v8 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=14) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-23 with a non-empty diagnostic question for each? A roster with 21 or 22 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 23 rows), C-03 (N-value check: N_aspirational=16), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 23-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-23 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-23): X/16 x 10 = YY.YY pts
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
Note that N_aspirational=16 means each aspirational criterion contributes 10/16 = 0.625 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL.

---

## V-03

**Axis:** C-23 PARTIAL ablation -- C-20 diagnostic question enumerates exactly two grammatical
form failures (interrogative + conditional); weak-modal form ("should be carried forward") omitted;
C-23 PARTIAL expected

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-20 diagnostic question in the criterion roster will name exactly two disqualifying forms -- interrogative ("Has the worked example been carried forward?") and conditional ("If the axis shifts, carry forward the example") -- without naming the weak-modal form ("The worked example should be carried forward"); the absence of the third form in the C-20 row text is the falsifying structural property for C-23 PARTIAL vs. PASS |
| Secondary effect | A scorer applying C-23 correctly will award C-23 PARTIAL (two forms enumerated) rather than C-23 FAIL or PASS; C-17 will still PASS because the C-20 diagnostic question is mechanism-specific (form-based) even with only two forms -- the C-17/C-23 boundary is the measurement instrument for this variation |
| Predicted sites | V-04 (one form only) is the C-23 FAIL case -- if V-03 earns PARTIAL and V-04 earns FAIL, the threshold between two-form and one-form enumeration is confirmed; V-01 (three forms) is the PASS ceiling; V-02 is unaffected by C-23 axis |

---

Score N skill outputs against the v8 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high
on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill
design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

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

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS
action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation
checkpoint.

---

#### Step 1.2 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 16.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/16 = 0.625 pt to the composite. Achieving composite
>= 99 requires at most one aspirational FAIL and no aspirational PARTIAL beyond that one.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 23 verdict rows (C-01 through C-23) in the scoring table, with none missing or duplicated? A matrix with 21 or 22 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=16? Can you re-derive the composite from the 23 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=16 within +/-1 rounding tolerance? An output using N_aspirational=14 (v7 values) or N_aspirational=12 (v6 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=16 (v8 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=14) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-23 with a non-empty diagnostic question for each? A roster with 21 or 22 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 23 rows), C-03 (N-value check: N_aspirational=16), and C-20 (grammatical form check: at least two disqualifying forms named with examples) interrogate the specific mechanism of each criterion rather than a generic probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Two disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL. Mandatory verb ("must", "shall", "is required to") required for PASS. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 23-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-23 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-23): X/16 x 10 = YY.YY pts
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
Note that N_aspirational=16 means each aspirational criterion contributes 10/16 = 0.625 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL.

---

## V-04

**Axis:** C-23 FAIL ablation -- C-20 diagnostic question enumerates only one grammatical form
failure (interrogative only); conditional and weak-modal forms omitted; C-23 FAIL expected

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-20 diagnostic question in the criterion roster will name only the interrogative form ("Has the worked example been carried forward?") as the disqualifying pattern, without naming conditional or weak-modal forms; the absence of both the second and third forms in the C-20 row text is the falsifying structural property for C-23 FAIL |
| Secondary effect | C-17 will still PASS because the C-20 diagnostic question is mechanism-specific (form detection) even with one form -- a single form is still more specific than a generic probe; this confirms that C-17 and C-23 are independent criteria measuring form-specificity at different granularities |
| Predicted sites | V-03 (two forms) is the direct C-23 PARTIAL contrast; V-01 (three forms) is the C-23 PASS ceiling; V-02 is unaffected by the C-23 axis; together V-02/V-03/V-04 provide the three-point C-23 evidence ladder (FAIL/PARTIAL/PASS) |

---

Score N skill outputs against the v8 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high
on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill
design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

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

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS
action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation
checkpoint.

---

#### Step 1.2 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 16.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/16 = 0.625 pt to the composite. Achieving composite
>= 99 requires at most one aspirational FAIL and no aspirational PARTIAL beyond that one.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 23 verdict rows (C-01 through C-23) in the scoring table, with none missing or duplicated? A matrix with 21 or 22 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=16? Can you re-derive the composite from the 23 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=16 within +/-1 rounding tolerance? An output using N_aspirational=14 (v7 values) or N_aspirational=12 (v6 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=16 (v8 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=14) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-23 with a non-empty diagnostic question for each? A roster with 21 or 22 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 23 rows), C-03 (N-value check: N_aspirational=16), and C-20 (grammatical form check: at least one disqualifying form named) interrogate the specific mechanism of each criterion rather than a generic probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Interrogative form earns C-20 FAIL -- "Has the worked example been carried forward?" is a diagnostic probe, not an enforceable instruction. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 23-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-23 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-23): X/16 x 10 = YY.YY pts
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
Note that N_aspirational=16 means each aspirational criterion contributes 10/16 = 0.625 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL.

---

## V-05

**Axis:** Combination pass -- all R8 structures retained from V-01, plus C-22 diagnostic question
explicitly enumerates all three verdict cases (FAIL, PARTIAL, PASS) with structural contrasting
examples; potential C-24 seed: "C-22 diagnostic question names all three verdict cases with
distinct structural contrasts"

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-22 diagnostic question in the criterion roster will contain all three verdict cases as named structural examples: FAIL case ("rule is imperative, no location language at all -- e.g., 'must be carried forward verbatim' without any FAILURE PATTERNS reference"), PARTIAL case ("rule names required location but omits SETUP exclusion -- e.g., 'must remain in the FAILURE PATTERNS action line' without 'do not relocate it to SETUP'"), and PASS case ("rule names both required location and SETUP exclusion") -- the absence of the three-case enumeration in the C-22 row text is the falsifying structural property |
| Secondary effect | Adding three-case enumeration to C-22 increases the C-22 row token length by approximately the same margin as adding a full worked example, mildly increasing SETUP density beyond V-01; this trades per-criterion diagnostic completeness for SETUP reproduction cost, the same tradeoff established at C-17 and C-23 |
| Predicted sites | V-02 (C-22 FAIL, imperative preservation rule without location) is the primary contrast: a scorer with V-05's three-case C-22 diagnostic will more precisely distinguish the FAIL case (no location at all) from the PARTIAL case (location present, SETUP exclusion absent) than a scorer with V-01's two-case C-22 diagnostic; V-01 establishes the two-case baseline (PARTIAL + FAIL named, but not contrasted as a three-value scale) |

---

Score N skill outputs against the v8 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
Composite score per output. Ranked leaderboard. Excellence signals: outputs scoring unusually high
on a specific criterion. Failure patterns: criteria failing across ALL outputs (rubric gap or skill
design issue?). Regression signals: outputs that passed in a prior round but fail in this round.

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

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action line
must be carried forward verbatim from the prior round, or updated to reflect the current round's
new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example
with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS
action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation
checkpoint.

---

#### Step 1.2 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 16 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 16.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/16 = 0.625 pt to the composite. Achieving composite
>= 99 requires at most one aspirational FAIL and no aspirational PARTIAL beyond that one.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 23 verdict rows (C-01 through C-23) in the scoring table, with none missing or duplicated? A matrix with 21 or 22 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=16? Can you re-derive the composite from the 23 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=16 within +/-1 rounding tolerance? An output using N_aspirational=14 (v7 values) or N_aspirational=12 (v6 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=16 (v8 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=14) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-23 with a non-empty diagnostic question for each? A roster with 21 or 22 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 23 rows), C-03 (N-value check: N_aspirational=16), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? Three verdict cases with structural contrasts: (FAIL) rule is imperative (C-20 PASS) but contains no location language at all -- e.g., "must be carried forward verbatim" without any reference to FAILURE PATTERNS or SETUP earns C-22 FAIL; (PARTIAL) rule names the required location ("must remain in the FAILURE PATTERNS action line") but omits explicit SETUP exclusion language -- e.g., absence of "do not relocate it to SETUP" earns C-22 PARTIAL; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence Quote
| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell
completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names and
exact section locations visible in the scored outputs. Placeholder text such as "[artifact]",
"[section]", or "[verb]" is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 23-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-23 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-23): X/16 x 10 = YY.YY pts
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
Note that N_aspirational=16 means each aspirational criterion contributes 10/16 = 0.625 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL.
