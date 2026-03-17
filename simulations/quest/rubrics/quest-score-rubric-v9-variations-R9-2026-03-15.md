# quest-score -- R9 Variations
Generated: 2026-03-15

## R9 Design Notes

V-01 is the R9 full-stack baseline: all R8 learnings retained, N_aspirational updated from 16 to
18 to reflect the two new aspirational criteria C-24 (C-22 three-scale enumeration in diagnostic
question) and C-25 (three-scale enumeration principle in design notes). The criterion roster
expands from 23 to 25 rows. The C-22 diagnostic question in the roster now enumerates all three
verdict cases with structural contrasting examples (FAIL/PARTIAL/PASS) -- satisfying C-24. The
SETUP block now contains a standalone named "Three-Scale Enumeration Principle" section stating
the general design rule -- satisfying C-25.

V-02 is the C-24 PARTIAL ablation: the C-22 diagnostic question enumerates exactly two verdict
cases (FAIL + PARTIAL) but omits the PASS example. C-24 PARTIAL expected. All other R9 structures
identical to V-01 including C-25 standalone principle.

V-03 is the C-24 FAIL ablation: the C-22 diagnostic question enumerates only one verdict case
(FAIL). PARTIAL and PASS cases not illustrated. C-24 FAIL expected. All other R9 structures
identical to V-01 including C-25 standalone principle.

V-04 is the C-25 PARTIAL ablation: all C-24 structures present (three-case C-22 diagnostic), but
the three-scale enumeration principle is embedded only within the C-24 criterion's diagnostic
question row -- not elevated to a standalone named principle section. C-25 PARTIAL expected.

V-05 is the C-24 FAIL + C-25 FAIL combination: the C-22 diagnostic question is a binary probe
(no verdict-case enumeration), and the three-scale enumeration principle is absent from the SETUP
block entirely. C-24 FAIL and C-25 FAIL expected simultaneously. This is the floor variation --
maximum contrast with V-01.

C-24 evidence ladder: V-03 (1 case = FAIL); V-05 (binary probe, 0 cases = FAIL); V-02 (2 cases =
PARTIAL); V-01/V-04 (3 cases = PASS).

C-25 evidence ladder: V-05 (absent = FAIL); V-04 (embedded in C-24 row, not standalone = PARTIAL);
V-01/V-02/V-03 (standalone named section = PASS).

---

## V-01

**Axis:** Baseline -- R9 full stack (N_aspirational=18, 25-row criterion roster, C-22 diagnostic
enumerates all three verdict cases satisfying C-24, SETUP contains standalone three-scale
enumeration principle satisfying C-25; all R8 V-01 structures retained unchanged)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The criterion roster will contain exactly 25 rows (C-01 through C-25), the composite formula will use N_aspirational=18, the C-22 diagnostic question will enumerate all three verdict levels (FAIL/PARTIAL/PASS) with structural contrasting examples, and the SETUP block will contain a standalone named three-scale enumeration principle -- absence of any one of these in the actual body clearly falsifies the R9-complete claim |
| Secondary effect | Expanding the criterion roster from 23 to 25 rows increases SETUP token density by two additional diagnostic-question pairs; the C-25 standalone principle section adds another named block, mildly increasing preamble reproduction cost; under token pressure, later variations may compress the C-25 principle or collapse it into a roster row |
| Predicted sites | V-02 and V-03 (C-24 ablations) are the direct contrasts for C-22 diagnostic coverage; V-04 (C-25 PARTIAL) is the direct contrast for standalone-vs-embedded principle; V-05 (combined floor) establishes the lowest boundary for both new criteria |

---

Score N skill outputs against the v9 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
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

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL,
and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient
for these criteria. Applied in this rubric: C-23 (for C-20, three grammatical form failures),
C-24 (for C-22, three verdict-boundary illustrations). When authoring a new criterion with a
non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 18 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 18.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/18 = 0.556 pt to the composite. Achieving composite
>= 99 requires at most one aspirational FAIL and no additional PARTIAL beyond that.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 25 verdict rows (C-01 through C-25) in the scoring table, with none missing or duplicated? A matrix with 23 or 24 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=18? Can you re-derive the composite from the 25 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=18 within +/-1 rounding tolerance? An output using N_aspirational=16 (v8 values) or N_aspirational=14 (v7 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=18 (v9 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=16) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-25 with a non-empty diagnostic question for each? A roster with 23 or 24 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 25 rows), C-03 (N-value check: N_aspirational=18), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row (e.g., referenced in the C-24 diagnostic question) but is not elevated to a named standalone section or declaration. FAIL: principle absent from SETUP design notes entirely. |

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

1. Write a 25-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-25 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-25): X/18 x 10 = YY.YY pts
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
Note that N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL and no additional
PARTIAL.

---

## V-02

**Axis:** C-24 PARTIAL ablation -- C-22 diagnostic question enumerates exactly two verdict cases
(FAIL + PARTIAL) but omits the PASS example; C-24 PARTIAL expected; all other R9 structures
including C-25 standalone principle identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-22 diagnostic question will name the FAIL case (imperative, no location language) and the PARTIAL case (location named, SETUP exclusion absent) but will contain no PASS example -- the absence of the third case is the falsifying property for C-24 PARTIAL vs. PASS; a scorer applying C-24 correctly will award PARTIAL, not PASS |
| Secondary effect | The C-25 standalone principle block is intact, so C-25 should PASS; the two-case enumeration in C-22's diagnostic does not impair C-17 (which checks mechanism specificity, not three-case coverage); C-24 PARTIAL is the only new degradation relative to V-01 |
| Predicted sites | V-01 (three-case C-22 diagnostic) is the direct upward contrast; V-03 (single-case) is the direct downward contrast; the spread V-03 FAIL / V-02 PARTIAL / V-01 PASS establishes the C-24 discrimination ladder |

---

Score N skill outputs against the v9 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
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

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL,
and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient
for these criteria. Applied in this rubric: C-23 (for C-20, three grammatical form failures),
C-24 (for C-22, three verdict-boundary illustrations). When authoring a new criterion with a
non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 18 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 18.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/18 = 0.556 pt to the composite.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 25 verdict rows (C-01 through C-25) in the scoring table, with none missing or duplicated? A matrix with 23 or 24 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=18? Can you re-derive the composite from the 25 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=18 within +/-1 rounding tolerance? An output using N_aspirational=16 (v8 values) or N_aspirational=14 (v7 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=18 (v9 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=16) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-25 with a non-empty diagnostic question for each? A roster with 23 or 24 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 25 rows), C-03 (N-value check: N_aspirational=18), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? (FAIL) rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language. PASS requires both (a) and (b). |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |

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

1. Write a 25-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-25 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-25): X/18 x 10 = YY.YY pts
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
Note that N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt to
the composite.

---

## V-03

**Axis:** C-24 FAIL ablation -- C-22 diagnostic question enumerates only one verdict case (FAIL);
PARTIAL and PASS cases absent; C-24 FAIL expected; all other R9 structures including C-25
standalone principle identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-22 diagnostic question will describe only the FAIL case (imperative, no location language) without naming or contrasting the PARTIAL or PASS cases -- the absence of at least two cases is the falsifying property for C-24 FAIL (< 2 cases); a scorer applying the < 2 rule correctly will award C-24 FAIL, not PARTIAL |
| Secondary effect | C-25 is intact (standalone principle block), so C-25 PASS; C-17 may earn PARTIAL or FAIL for C-22's diagnostic being insufficiently specific about verdict boundaries, but the C-17 mechanism check is separate from C-24's coverage count -- they are co-degradable but not co-implied |
| Predicted sites | V-02 (two-case = PARTIAL) is the upward contrast; V-01 (three-case = PASS) is two steps above; the V-03/V-02/V-01 ladder is the C-24 discrimination sequence |

---

Score N skill outputs against the v9 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
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

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL, PARTIAL,
and PASS -- with distinct structural contrasting examples. A binary pass/fail probe is insufficient
for these criteria. Applied in this rubric: C-23 (for C-20, three grammatical form failures),
C-24 (for C-22, three verdict-boundary illustrations). When authoring a new criterion with a
non-trivial PARTIAL threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 18 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 18.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/18 = 0.556 pt to the composite.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 25 verdict rows (C-01 through C-25) in the scoring table, with none missing or duplicated? A matrix with 23 or 24 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=18? Can you re-derive the composite from the 25 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=18 within +/-1 rounding tolerance? An output using N_aspirational=16 (v8 values) or N_aspirational=14 (v7 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=18 (v9 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=16) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-25 with a non-empty diagnostic question for each? A roster with 23 or 24 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 25 rows), C-03 (N-value check: N_aspirational=18), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name FAILURE PATTERNS as the required location AND name SETUP as a disqualifying alternative? A rule that is imperative (satisfying C-20) but contains no location language fails C-22. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate verdict cases with structural contrasting examples? A diagnostic question that describes only the FAIL case without illustrating the PARTIAL/PASS boundary earns C-24 FAIL (fewer than two cases). |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |

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

1. Write a 25-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-25 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-25): X/18 x 10 = YY.YY pts
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
Note that N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt to
the composite.

---

## V-04

**Axis:** C-25 PARTIAL ablation -- the three-scale enumeration principle appears embedded within
the C-24 criterion's diagnostic question row in the roster, but is NOT elevated to a standalone
named principle section in SETUP; C-25 PARTIAL expected; C-24 PASS maintained (three-case C-22
diagnostic intact)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The SETUP block will contain no standalone "Three-Scale Enumeration Principle" section; the C-24 diagnostic question will reference the pattern ("applies the three-scale enumeration rule") but the rule itself will not appear as a named standalone section -- the absence of the standalone section is the falsifying property for C-25 PARTIAL (embedded vs. standalone) |
| Secondary effect | C-24 remains PASS because the C-22 diagnostic question still enumerates three verdict cases; C-25 PARTIAL does not degrade C-24; a scorer who conflates C-25 PARTIAL with C-25 FAIL (treating any non-standalone mention as absent) reveals a calibration gap in C-25 scoring |
| Predicted sites | V-01 (standalone principle section = C-25 PASS) is the direct upward contrast; V-05 (no principle anywhere = C-25 FAIL) is the downward contrast; V-04 PARTIAL sits between them, establishing the embedded-vs-standalone boundary |

---

Score N skill outputs against the v9 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
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
          + (aspirational_pass / 18 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 18.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/18 = 0.556 pt to the composite.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 25 verdict rows (C-01 through C-25) in the scoring table, with none missing or duplicated? A matrix with 23 or 24 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=18? Can you re-derive the composite from the 25 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=18 within +/-1 rounding tolerance? An output using N_aspirational=16 (v8 values) or N_aspirational=14 (v7 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=18 (v9 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=16) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-25 with a non-empty diagnostic question for each? A roster with 23 or 24 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 25 rows), C-03 (N-value check: N_aspirational=18), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? (FAIL) rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Note: this criterion applies the three-scale enumeration principle -- any criterion whose PARTIAL is defined by one-of-two-elements-present must have its diagnostic question enumerate FAIL/PARTIAL/PASS with structural contrasts. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row (e.g., referenced in the C-24 diagnostic question) but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |

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

1. Write a 25-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-25 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-25): X/18 x 10 = YY.YY pts
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
Note that N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt to
the composite.

---

## V-05

**Axis:** C-24 FAIL + C-25 FAIL combination -- C-22 diagnostic is a binary probe with no verdict-
case enumeration; three-scale enumeration principle absent from SETUP entirely; C-24 FAIL and
C-25 FAIL expected simultaneously; floor variation -- maximum contrast with V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The C-22 diagnostic question will ask only whether the preservation rule satisfies C-22 without enumerating FAIL/PARTIAL/PASS cases; the SETUP block will contain no mention of the three-scale enumeration principle in any form -- these two absences together produce both C-24 FAIL and C-25 FAIL; the composite degradation is exactly 2 x 0.556 = 1.11 pts below V-01 |
| Secondary effect | C-23 is unaffected (C-20 diagnostic retains three-form enumeration); C-22's binary diagnostic may still earn C-17 PARTIAL if the question is at least mechanism-specific about the location constraint, even without enumerating cases -- C-17 and C-24 measure different properties of the same diagnostic question |
| Predicted sites | V-01 (C-24 PASS + C-25 PASS) is the ceiling contrast; V-02 (C-24 PARTIAL + C-25 PASS) and V-04 (C-24 PASS + C-25 PARTIAL) isolate the individual dimensions; V-05 establishes the floor where both degrade simultaneously |

---

Score N skill outputs against the v9 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence quote.
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
          + (aspirational_pass / 18 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 18.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/18 = 0.556 pt to the composite.

---

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 25 verdict rows (C-01 through C-25) in the scoring table, with none missing or duplicated? A matrix with 23 or 24 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=18? Can you re-derive the composite from the 25 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=18 within +/-1 rounding tolerance? An output using N_aspirational=16 (v8 values) or N_aspirational=14 (v7 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble that states auto-PASS conditions in prose without criterion IDs fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=18 (v9 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=16) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-25 with a non-empty diagnostic question for each? A roster with 23 or 24 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 25 rows), C-03 (N-value check: N_aspirational=18), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name FAILURE PATTERNS as the required location AND name SETUP as a disqualifying alternative? A rule that is imperative (C-20 PASS) but contains no location language fails C-22. A rule that names the required location but not the SETUP prohibition earns C-22 PARTIAL. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate verdict cases with structural contrasting examples illustrating the FAIL/PARTIAL/PASS boundary? A binary probe ("Does the rule name both required location and SETUP exclusion?") earns C-24 FAIL -- verdict-case enumeration is absent. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds? A roster diagnostic question that references the principle only in passing earns C-25 FAIL -- the principle must appear as a named standalone section, not embedded in a criterion row. |

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

1. Write a 25-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-25 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-25): X/18 x 10 = YY.YY pts
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
Note that N_aspirational=18 means each aspirational criterion contributes 10/18 = 0.556 pt to
the composite.
