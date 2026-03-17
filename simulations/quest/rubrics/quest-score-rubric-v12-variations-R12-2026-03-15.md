# quest-score -- R12 Variations
Generated: 2026-03-15

## R12 Design Notes

V-01 is the R12 full-stack baseline. All R11 learnings retained. N_aspirational updates from 22
to 25 to reflect three new aspirational criteria: C-30 (multi-variation scoring uses shared
baseline evidence table), C-31 (cascade auto-PASS SETUP block groups primary trigger and
dependents), C-32 (SETUP notes design-time evaluation for template-structure criteria when
cascade fires). The criterion roster expands from 29 to 32 rows. The composite formula uses
N_aspirational=25 (each criterion contributes 10/25 = 0.40 pt, PARTIAL incurs 0.20 pt
degradation). The C-07 cascade block now instructs the scorer to write a grouped declaration --
"C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade" -- and include a design-time
evaluation note naming "Variation in causal position, column 4" as the specific template element
validated for C-28. C-31 and C-32 each auto-PASS when C-07 does not fire. The C-25 "Applied in
this rubric" inventory expands from 6 to 9 entries (adding C-30 for C-02, C-31 for C-11, C-32
for C-28). C-11 now requires 10 named auto-PASS declarations.

V-02 is the C-31 PARTIAL ablation: all R12 structures intact, but the C-07 cascade block
instruction lists C-27 and C-28 as independent entries without "also auto-PASS per cascade"
grouping annotation. The scoring output SETUP block will declare each cascade entry
independently without chain notation. C-31 PARTIAL predicted (cascade noted, grouping absent).
Single-axis isolation: only the cascade declaration grouping style differs from V-01.

V-03 is the C-32 PARTIAL ablation: all R12 structures intact, but the design-time evaluation
note in the C-07 cascade instruction states only that C-28 is "still evaluated at design time"
without naming the specific template element (column order / Variation in causal position).
C-32 PARTIAL predicted (note present, specific element absent). Single-axis isolation: only
the design-time evaluation specificity differs from V-01.

V-04 is the C-30 FAIL ablation: all R12 structures intact, but Phase 2 contains no instruction
for a shared baseline evidence table. The scoring output writes complete per-variation rows for
all 32 x N criteria without consolidation. C-30 FAIL predicted (no shared table).
Single-axis isolation: only the shared-evidence table instruction is absent.

V-05 is the C-31 PARTIAL + C-32 PARTIAL combination floor: independent cascade entries (V-02
ablation) AND design-time note lacking the specific template element (V-03 ablation). Expected
additive degradation: 2 x 0.20 pt = 0.40 pt from V-01 ceiling. Labeled as combination pass.

Evidence ladders:
- C-30: V-04 FAIL (no shared table); V-01/V-02/V-03/V-05 PASS (shared table + override quotes)
- C-31: V-02 PARTIAL (independent, no grouping); V-05 PARTIAL (same); V-01/V-03/V-04 PASS (grouped with "per cascade")
- C-32: V-03 PARTIAL (note present, element unnamed); V-05 PARTIAL (same); V-01/V-02/V-04 PASS (note + column 4 named)

---

## V-01

**Axis:** Baseline -- R12 full stack (N_aspirational=25, 32-row criterion roster, C-30 PASS:
Phase 2 instructs shared baseline evidence table with explicit override quotes; C-31 PASS:
C-07 cascade block instructs grouped declaration "C-07 auto-PASS. C-27 and C-28 also auto-PASS
per cascade"; C-32 PASS: design-time evaluation note names "Variation in causal position,
column 4"; C-25 inventory lists 9 paired entries; C-11 requires 10 declarations; all R11
structures retained unchanged)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The criterion roster will contain exactly 32 rows (C-01 through C-32), the composite formula will use N_aspirational=25, the C-25 "Applied in this rubric" inventory will list 9 paired entries including "C-30 (for C-02)", "C-31 (for C-11)", and "C-32 (for C-28)", the C-07 cascade block will instruct writing "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade", and the design-time evaluation note will name "Variation in causal position, column 4" as the specific template element for C-28 -- absence of any one property clearly falsifies the R12-complete claim |
| Secondary effect | Expanding the criterion roster from 29 to 32 rows increases SETUP token density by three additional diagnostic-question rows; C-30/C-31/C-32 three-scale diagnostic questions add the most complexity since each must enumerate FAIL/PARTIAL/PASS cases with evidence-consolidation, grouping-notation, and template-element contrasting examples respectively; under token pressure, later variations may omit the "per cascade" annotation (V-02 ablation site) or the specific column-order name in the design-time note (V-03 ablation site), shifting complexity FROM the cascade declaration structural precision TO the roster diagnostic depth |
| Predicted sites | V-02 (independent cascade entries, no grouping) is the direct contrast for C-31 PARTIAL; V-03 (design-time note without element name) is the direct contrast for C-32 PARTIAL; V-04 (no shared baseline table) is the C-30 FAIL floor; V-05 (C-31 PARTIAL + C-32 PARTIAL combination) confirms additive degradation of the two new cascade-structure criteria |

---

Score N skill outputs against the v12 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade -- no regression table is
> instantiated. Aspirational criteria C-27 and C-28 are evaluated here on the static template
> design (Variation in causal position, column 4, in the REGRESSION SIGNALS template), since
> cascade auto-PASS fires at runtime, not at design-time.

When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v12, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. The worked example must remain in the FAILURE
PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a
preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL,
PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe
is insufficient for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28).
When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle
before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 25.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/25 = 0.40 pt to the composite. A single PARTIAL
incurs 0.20 pt degradation; a single FAIL incurs 0.40 pt degradation. Achieving composite
>= 100 requires 25/25 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 32 verdict rows (C-01 through C-32) in the scoring table, with none missing or duplicated? A matrix with 29 or 31 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=25? Can you re-derive the composite from the 32 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=25 within +/-1 rounding tolerance? An output using N_aspirational=22 (v11 values) or N_aspirational=20 (v10 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all ten auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, and C-32) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the ten declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=25 (v12 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=22) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-32 with a non-empty diagnostic question for each? A roster with 29 or 31 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 32 rows), C-03 (N-value check: N_aspirational=25), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs -- e.g., "Applied in this rubric: C-23, C-24, C-26, C-27, C-28, C-29, C-30, C-31, C-32" without specifying which criterion each targets; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. Variation captures what changed structurally in the scored output between rounds; Mechanism states the detection rule -- they are distinct columns. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; (PARTIAL) 5 columns present but column order is "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" -- Variation in column 5 inverts the causal chain; (PASS) column order is "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism" -- Variation in causal position enables the reading: what criterion regressed, what changed structurally, how to detect recurrence. |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 (the cascade-dependent criterion) is absent entirely from the auto-PASS declarations block -- no cascade reference present; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- e.g., "C-28 auto-PASS when no prior-round data is available" repeats the underlying condition without naming C-07 as the gating criterion; (PASS) cascade declaration names the triggering criterion ID -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | When scoring N variations (N >= 2), is a named "Shared baseline evidence" table present at the head of Phase 2 consolidating evidence identical across all N outputs, with per-variation rows using "(shared)" as a reference token and differentiating cells carrying explicit override quotes? (FAIL) no shared baseline table present; all N x 32 rows written out in full with identical evidence repeated verbatim; (PARTIAL) shared baseline table present but per-variation differentiating cells lack explicit override quotes -- reference token "(shared)" in differentiating cells without contrasting evidence; (PASS) shared table present AND differentiating cells carry explicit override quotes showing what changed from the shared baseline. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | Is the Phase 1 SETUP auto-PASS block in the scoring output written with C-07 as the primary trigger, followed by C-27 and C-28 grouped together with explicit "also auto-PASS per cascade" or equivalent annotation? (FAIL) cascade-dependent C-27 and C-28 listed as fully independent auto-PASS entries with no chain notation; (PARTIAL) cascade dependency is present in the block but the primary/dependent relationship is implicit -- e.g., all three entries listed sequentially without "per cascade" annotation distinguishing the trigger from the dependents; (PASS) the block declares "C-07 auto-PASS" first then "C-27 and C-28 also auto-PASS per cascade" or equivalent, making the cascade graph directly readable. C-31 auto-PASS when C-07 does not fire -- write the declaration. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | Does the Phase 1 SETUP auto-PASS block in the scoring output include, for C-28's cascade auto-PASS, a design-time evaluation note that names the specific template element being validated? (FAIL) cascade auto-PASS fires for C-28 with no design-time evaluation note in the PHASE 1 SETUP block; (PARTIAL) design-time evaluation note present but identifies only that "C-28 is still evaluated at design time" without naming the specific template element -- e.g., "C-28 still evaluated statically" without naming "Variation in causal position (column 4)"; (PASS) note present AND names the specific template element -- e.g., "C-27 and C-28 are evaluated here on the static template design (Variation in causal position, column 4, in the REGRESSION SIGNALS template)". C-32 auto-PASS when C-07 does not fire -- write the declaration. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations visible in the scored outputs. Placeholder text such as
"[artifact]", "[section]", or "[verb]" is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate evidence
that is identical across all N scored outputs in a named "Shared baseline evidence" table at
the head of Phase 2, before the first per-output heading. Per-variation scoring rows use
"(shared)" as a reference token for criteria where the evidence and verdict match the shared
baseline. Differentiating cells -- where a variation diverges from the shared verdict or
evidence -- carry an explicit override quote from that variation's output, not "(shared)".
This satisfies C-30 without repeating 32 x N identical evidence cells.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 32-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-32 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-32): X/25 x 10 = YY.YY pts
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

Example of a fully instantiated action line: "Update the C-07 cascade auto-PASS block in the
PHASE 1 SETUP of quest-score.md to read 'C-07 auto-PASS. C-27 and C-28 also auto-PASS per
cascade -- no regression table is instantiated.' grouping cascade dependents under the primary
trigger with explicit 'per cascade' annotation -- so C-31 is satisfied on every run."

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
Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to
the composite; a single PARTIAL incurs 0.20 pt degradation from the ceiling.

---

## V-02

**Axis:** C-31 PARTIAL ablation -- C-07 cascade block instructs independent auto-PASS entries
without "also auto-PASS per cascade" grouping annotation; all other R12 structures including
the design-time evaluation note (naming "Variation in causal position, column 4"), the shared
baseline evidence instruction, and the trigger-ID cascade declaration form are identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output SETUP block will list "C-07 auto-PASS", "C-27 auto-PASS when C-07 auto-PASS fires", "C-28 auto-PASS when C-07 auto-PASS fires" as three independent entries without any "per cascade" or "also auto-PASS" chain notation; a scorer applying C-31 will award PARTIAL -- cascade dependency is present (C-07 is named in C-27/C-28 declarations) but primary/dependent grouping annotation is absent; C-32 PASS is unaffected (design-time note still names "column 4") |
| Secondary effect | Removing the grouped cascade notation shifts the cascade declaration block FROM a single chained statement TO three parallel entries; the parallel-entry style satisfies C-29 (trigger ID present in each declaration) and C-16 (entries are named) but fails the C-31 grouping requirement; no other structural property changes, so all 29 other criteria remain at V-01 PASS status |
| Predicted sites | V-01 (grouped "per cascade") is the direct upward contrast establishing C-31 PASS; V-05 (combination floor) shares the independent-entry cascade style as its C-31 ablation component -- V-02 and V-05 should both produce C-31 PARTIAL, confirming the grouping-annotation mechanism in isolation and in combination |

---

Score N skill outputs against the v12 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS -- no prior-round scorecard provided.
> C-27 auto-PASS when C-07 auto-PASS fires -- no regression table is instantiated.
> C-28 auto-PASS when C-07 auto-PASS fires -- no regression table is instantiated.
> [Design-time evaluation note: Aspirational criteria C-27 and C-28 are evaluated here on the
> static template design (Variation in causal position, column 4, in the REGRESSION SIGNALS
> template), since cascade auto-PASS fires at runtime, not at design-time.]

When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v12, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. The worked example must remain in the FAILURE
PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a
preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL,
PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe
is insufficient for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28).
When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle
before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 25.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/25 = 0.40 pt to the composite. A single PARTIAL
incurs 0.20 pt degradation; a single FAIL incurs 0.40 pt degradation. Achieving composite
>= 100 requires 25/25 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 32 verdict rows (C-01 through C-32) in the scoring table, with none missing or duplicated? A matrix with 29 or 31 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=25? Can you re-derive the composite from the 32 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=25 within +/-1 rounding tolerance? An output using N_aspirational=22 (v11 values) or N_aspirational=20 (v10 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all ten auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, and C-32) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the ten declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=25 (v12 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=22) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-32 with a non-empty diagnostic question for each? A roster with 29 or 31 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 32 rows), C-03 (N-value check: N_aspirational=25), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns; (PARTIAL) regression table has the 4 required C-18 columns but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent; (PARTIAL) 5 columns present but Variation in column 5 after Mechanism; (PASS) column order is "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism" -- Variation in causal position. |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires (cascade dependencies), does each declaration name the triggering criterion by ID? (FAIL) C-28 absent entirely from the auto-PASS declarations block; (PARTIAL) cascade dependency declared for C-28 but trigger ID absent -- e.g., "C-28 auto-PASS when no prior-round data is available"; (PASS) cascade declaration names the triggering criterion ID -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | When scoring N variations (N >= 2), is a named "Shared baseline evidence" table present at the head of Phase 2 consolidating evidence identical across all N outputs, with per-variation rows using "(shared)" as a reference token and differentiating cells carrying explicit override quotes? (FAIL) no shared baseline table present; all N x 32 rows written out in full; (PARTIAL) shared baseline table present but differentiating cells lack explicit override quotes; (PASS) shared table present AND differentiating cells carry explicit override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | Is the Phase 1 SETUP auto-PASS block in the scoring output written with C-07 as the primary trigger, followed by C-27 and C-28 grouped together with explicit "also auto-PASS per cascade" or equivalent annotation? (FAIL) cascade-dependent C-27 and C-28 listed as fully independent auto-PASS entries with no chain notation; (PARTIAL) cascade dependency is present but primary/dependent relationship is implicit -- entries listed sequentially without "per cascade" annotation; (PASS) block declares "C-07 auto-PASS" first then "C-27 and C-28 also auto-PASS per cascade" or equivalent. C-31 auto-PASS when C-07 does not fire -- write the declaration. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | Does the Phase 1 SETUP auto-PASS block in the scoring output include, for C-28's cascade auto-PASS, a design-time evaluation note that names the specific template element being validated? (FAIL) cascade auto-PASS fires for C-28 with no design-time evaluation note in SETUP; (PARTIAL) design-time evaluation note present but does not name the specific template element; (PASS) note present AND names "Variation in causal position, column 4" or equivalent specific element. C-32 auto-PASS when C-07 does not fire -- write the declaration. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations visible in the scored outputs. Placeholder text such as
"[artifact]", "[section]", or "[verb]" is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate evidence
that is identical across all N scored outputs in a named "Shared baseline evidence" table at
the head of Phase 2, before the first per-output heading. Per-variation scoring rows use
"(shared)" as a reference token for criteria where the evidence and verdict match the shared
baseline. Differentiating cells carry an explicit override quote from that variation's output,
not "(shared)". This satisfies C-30 without repeating 32 x N identical evidence cells.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 32-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-32 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-32): X/25 x 10 = YY.YY pts
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

Example of a fully instantiated action line: "Update the C-07 cascade auto-PASS block in the
PHASE 1 SETUP of quest-score.md to read 'C-07 auto-PASS. C-27 and C-28 also auto-PASS per
cascade -- no regression table is instantiated.' grouping cascade dependents under the primary
trigger with explicit 'per cascade' annotation -- so C-31 is satisfied on every run."

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
Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to
the composite; a single PARTIAL incurs 0.20 pt degradation from the ceiling.

---

## V-03

**Axis:** C-32 PARTIAL ablation -- C-07 cascade block instruction includes a design-time
evaluation note but does not name the specific template element (column order / Variation in
causal position); C-31 PASS is unaffected (grouped "per cascade" annotation intact); all other
R12 structures identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output SETUP block will contain a design-time evaluation note reading "C-27 and C-28 are still evaluated at design time, since cascade auto-PASS fires at runtime" without naming "Variation in causal position, column 4" or "column 4" as the specific template element; a scorer applying C-32 will award PARTIAL -- note present but specific element absent; C-31 PASS is unaffected (the cascade block still groups "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade") |
| Secondary effect | Removing the specific element name from the design-time note shifts the note FROM a verifiable template-structure claim TO a general procedural statement; the general statement satisfies the "note present" condition for C-32 PARTIAL but fails the "specific element named" condition for C-32 PASS; all other structural properties including C-29 cascade trigger ID naming and C-28 causal column order in the regression template remain at V-01 PASS |
| Predicted sites | V-01 (design-time note naming "column 4") is the direct upward contrast establishing C-32 PASS; V-05 (combination floor) shares this C-32 ablation -- V-03 and V-05 should both produce C-32 PARTIAL, confirming the element-specificity mechanism in isolation and in combination |

---

Score N skill outputs against the v12 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade -- no regression table is
> instantiated. C-27 and C-28 are still evaluated at design time, since cascade auto-PASS
> fires at runtime, not at design-time.

When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v12, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. The worked example must remain in the FAILURE
PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a
preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL,
PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe
is insufficient for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28).
When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle
before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 25.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/25 = 0.40 pt to the composite. A single PARTIAL
incurs 0.20 pt degradation; a single FAIL incurs 0.40 pt degradation. Achieving composite
>= 100 requires 25/25 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 32 verdict rows (C-01 through C-32) in the scoring table, with none missing or duplicated? A matrix with 29 or 31 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=25? Can you re-derive the composite from the 32 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=25 within +/-1 rounding tolerance? An output using N_aspirational=22 (v11 values) or N_aspirational=20 (v10 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all ten auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, and C-32) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the ten declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=25 (v12 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=22) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-32 with a non-empty diagnostic question for each? A roster with 29 or 31 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 32 rows), C-03 (N-value check: N_aspirational=25), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form earns C-19 PARTIAL and C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, and (3) weak-modal? Two forms named earns C-23 PARTIAL. Fewer than two earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) no location language; (PARTIAL) required location named, SETUP exclusion absent; (PASS) both location phrase and SETUP exclusion phrase present. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle? PARTIAL: principle within a single criterion row, not elevated to standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an application inventory pairing each applying criterion with its target? (FAIL) no inventory; (PARTIAL) inventory present but entries lack target criterion IDs; (PASS) every entry names both the applying criterion ID and the target criterion ID including "C-30 (for C-02), C-31 (for C-11), C-32 (for C-28)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 fires. When active: (FAIL) regression section absent or fewer than 4 columns; (PARTIAL) 4 C-18 columns present, Variation column absent; (PASS) all 5 columns including Variation present. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation column absent; (PARTIAL) 5 columns present but Variation in column 5 after Mechanism; (PASS) column order "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | (FAIL) C-28 absent entirely from declarations block; (PARTIAL) cascade dependency declared but trigger ID absent; (PASS) cascade declaration names triggering criterion ID -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared baseline table; all N x 32 rows written out in full; (PARTIAL) shared table present but differentiating cells lack explicit override quotes; (PASS) shared table present AND differentiating cells carry explicit override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) cascade-dependent C-27 and C-28 listed as independent entries with no chain notation; (PARTIAL) cascade noted but "per cascade" annotation absent, primary/dependent distinction implicit; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade" or equivalent. C-31 auto-PASS when C-07 does not fire -- write the declaration. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) cascade auto-PASS fires for C-28 with no design-time evaluation note in SETUP; (PARTIAL) design-time note present but does not name the specific template element; (PASS) note present AND names "Variation in causal position, column 4" or equivalent. C-32 auto-PASS when C-07 does not fire -- write the declaration. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations visible in the scored outputs. Placeholder text is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate evidence
that is identical across all N scored outputs in a named "Shared baseline evidence" table at
the head of Phase 2, before the first per-output heading. Per-variation scoring rows use
"(shared)" as a reference token for criteria where the evidence and verdict match the shared
baseline. Differentiating cells carry an explicit override quote from that variation's output.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 32-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-32 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-32): X/25 x 10 = YY.YY pts
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

Example of a fully instantiated action line: "Update the C-07 cascade auto-PASS block in the
PHASE 1 SETUP of quest-score.md to read 'C-07 auto-PASS. C-27 and C-28 also auto-PASS per
cascade -- no regression table is instantiated.' grouping cascade dependents under the primary
trigger with explicit 'per cascade' annotation -- so C-31 is satisfied on every run."

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
Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to
the composite; a single PARTIAL incurs 0.20 pt degradation from the ceiling.

---

## V-04

**Axis:** C-30 FAIL ablation -- Phase 2 contains no shared-evidence table instruction; all
per-variation scoring rows are written individually with no consolidation mechanism; all
cascade-structure elements (C-31/C-32 grouping and design-time note) are identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output Phase 2 will contain no "Shared baseline evidence" table at its head; all N x 32 scoring rows will appear as independent per-variation tables with identical evidence repeated verbatim; a scorer applying C-30 will award FAIL -- no shared table present, the full-repetition format satisfies C-02 (evidence present in every row) but violates C-30 (no consolidation, no "(shared)" reference tokens, no override quotes); C-31 and C-32 PASS are unaffected (cascade block still groups "per cascade" and names "column 4") |
| Secondary effect | Removing the shared-evidence instruction shifts the scoring token budget FROM boundary-table construction TO per-variation row repetition; under identical token pressure, a multi-variation run without the shared table may produce later variations (V-04, V-05) with truncated evidence quotes as the token budget is consumed by repeated identical rows earlier; this secondary effect tests whether the shared-evidence structure adds enforcement value beyond evidence-completeness checking alone |
| Predicted sites | V-01 (shared table + override quotes) is the direct upward contrast establishing C-30 PASS; V-02 (C-31 PARTIAL, shared table intact) and V-03 (C-32 PARTIAL, shared table intact) should both produce C-30 PASS -- confirming the ablation is single-axis and that C-30 PASS does not depend on the cascade-structure elements being ablated in V-02/V-03 |

---

Score N skill outputs against the v12 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade -- no regression table is
> instantiated. Aspirational criteria C-27 and C-28 are evaluated here on the static template
> design (Variation in causal position, column 4, in the REGRESSION SIGNALS template), since
> cascade auto-PASS fires at runtime, not at design-time.

When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v12, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. The worked example must remain in the FAILURE
PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a
preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL,
PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe
is insufficient for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28).
When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle
before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 25.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/25 = 0.40 pt to the composite. A single PARTIAL
incurs 0.20 pt degradation; a single FAIL incurs 0.40 pt degradation. Achieving composite
>= 100 requires 25/25 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 32 verdict rows (C-01 through C-32) in the scoring table, with none missing or duplicated? A matrix with 29 or 31 rows fails C-01 -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=25? Can you re-derive the composite from the 32 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=25 within +/-1 rounding tolerance? An output using N_aspirational=22 (v11 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard missing one of the four required columns is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? A section present but empty fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? Placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread, and characterizes clustering vs. discrimination? Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and section? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all ten auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, and C-32) present as named declarations in SETUP? A preamble missing any of the ten declarations fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_aspirational=25 (v12 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-32 with a non-empty diagnostic question for each? A roster with 29 or 31 rows, or any row with an empty diagnostic question, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? Permissive language fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 32 rows), C-03 (N-value check: N_aspirational=25), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism)? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form earns C-19 PARTIAL and C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional, (3) weak-modal. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: (a) present, (b) absent. FAIL: rule is imperative but no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, (3) weak-modal? Two forms earns C-23 PARTIAL. Fewer than two earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases? (FAIL) no location language; (PARTIAL) location named, SETUP exclusion absent; (PASS) both location and SETUP exclusion present. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle? PARTIAL: principle embedded in a criterion row. FAIL: principle absent from SETUP entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an application inventory with every entry naming both the applying criterion ID and the target criterion ID? (FAIL) no inventory; (PARTIAL) inventory lacks target IDs; (PASS) full paired inventory including "C-30 (for C-02), C-31 (for C-11), C-32 (for C-28)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 fires. When active: (FAIL) section absent or fewer than 4 columns; (PARTIAL) 4 columns, Variation absent; (PASS) 5 columns including Variation. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation column absent; (PARTIAL) Variation in column 5 after Mechanism; (PASS) column order "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | (FAIL) C-28 absent from declarations block; (PARTIAL) cascade declared but trigger ID absent; (PASS) trigger ID named -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared baseline table; all N x 32 rows written out in full with identical evidence repeated; (PARTIAL) shared table present but differentiating cells lack explicit override quotes; (PASS) shared table present AND differentiating cells carry explicit override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) cascade-dependent C-27 and C-28 listed as independent entries with no chain notation; (PARTIAL) cascade noted but "per cascade" annotation absent; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade" or equivalent. C-31 auto-PASS when C-07 does not fire -- write the declaration. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) cascade fires for C-28 with no design-time note in SETUP; (PARTIAL) design-time note present but specific template element not named; (PASS) note present AND names "Variation in causal position, column 4" or equivalent. C-32 auto-PASS when C-07 does not fire -- write the declaration. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholder text is a C-08 FAIL.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 32-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-32 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-32): X/25 x 10 = YY.YY pts
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

Example of a fully instantiated action line: "Update the C-07 cascade auto-PASS block in the
PHASE 1 SETUP of quest-score.md to read 'C-07 auto-PASS. C-27 and C-28 also auto-PASS per
cascade -- no regression table is instantiated.' grouping cascade dependents under the primary
trigger with explicit 'per cascade' annotation -- so C-31 is satisfied on every run."

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
Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to
the composite; a single PARTIAL incurs 0.20 pt degradation from the ceiling.

---

## V-05

**Axis:** Combination pass -- C-31 PARTIAL ablation (V-02) + C-32 PARTIAL ablation (V-03);
independent cascade entries without "per cascade" annotation AND design-time evaluation note
without specific template element name; all other R12 structures including C-30 shared
baseline instruction identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output SETUP block will list C-07, C-27, C-28 as independent entries without "per cascade" grouping (C-31 PARTIAL) AND the design-time evaluation note will read "C-27 and C-28 are still evaluated at design time" without naming "Variation in causal position, column 4" (C-32 PARTIAL); both PARTIAL verdicts are predicted to be structurally independent -- the grouping annotation and the element-name are distinct syntactic properties, so C-31 PARTIAL does not cause C-32 PARTIAL and vice versa |
| Secondary effect | Combined C-31 + C-32 PARTIAL degradation is predicted to be additive: 2 x 0.20 pt = 0.40 pt from V-01 ceiling (expected composite: 99.60); if the observed degradation is subadditive (< 0.40 pt), the two criteria share a latent structural dependency that the single-axis ablations V-02 and V-03 cannot detect independently; C-30 PASS is unaffected (shared baseline instruction intact), confirming the combination floor is solely driven by cascade-structure elements |
| Predicted sites | V-01 (both PASS: 100.00) is the ceiling; V-02 (C-31 PARTIAL: ~99.80) and V-03 (C-32 PARTIAL: ~99.80) are the single-axis baselines; V-05 (both PARTIAL: ~99.60) confirms additivity if observed degradation equals V-02 delta + V-03 delta |

---

Score N skill outputs against the v12 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS -- no prior-round scorecard provided.
> C-27 auto-PASS when C-07 auto-PASS fires -- no regression table is instantiated.
> C-28 auto-PASS when C-07 auto-PASS fires -- no regression table is instantiated.
> [C-27 and C-28 are still evaluated at design time, since cascade auto-PASS fires at runtime.]

When C-07 auto-PASS fires, C-27 and C-28 also auto-PASS -- no regression table is instantiated.

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v12, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. The worked example must remain in the FAILURE
PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a
preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule (applies to all future criterion authors):** Any aspirational criterion
whose PARTIAL verdict is defined by having exactly one of two required elements present (and the
other absent) must have its diagnostic question enumerate all three verdict cases -- FAIL,
PARTIAL, and PASS -- with distinct structural contrasting examples. A binary pass/fail probe
is insufficient for these criteria.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28).
When authoring a new criterion with a non-trivial PARTIAL threshold, apply this principle
before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 25 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 25.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/25 = 0.40 pt to the composite. A single PARTIAL
incurs 0.20 pt degradation; a single FAIL incurs 0.40 pt degradation. Achieving composite
>= 100 requires 25/25 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 32 verdict rows (C-01 through C-32) in the scoring table, with none missing or duplicated? A matrix with 29 or 31 rows fails C-01 -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=25? Can you re-derive the composite from the 32 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=25 within +/-1 rounding tolerance? An output using N_aspirational=22 (v11 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard missing one of the four required columns is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? A section present but empty fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? Placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread, and characterizes clustering vs. discrimination? Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and section? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all ten auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, and C-32) present as named declarations in SETUP? A preamble missing any of the ten declarations fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_aspirational=25 (v12 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-32 with a non-empty diagnostic question for each? A roster with 29 or 31 rows, or any row with an empty diagnostic question, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? Permissive language fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 32 rows), C-03 (N-value check: N_aspirational=25), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism)? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form earns C-19 PARTIAL and C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional, (3) weak-modal. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: (a) present, (b) absent. FAIL: rule is imperative but no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, (3) weak-modal? Two forms earns C-23 PARTIAL. Fewer than two earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases? (FAIL) no location language; (PARTIAL) location named, SETUP exclusion absent; (PASS) both location and SETUP exclusion present. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle? PARTIAL: principle embedded in a criterion row. FAIL: principle absent from SETUP entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an application inventory with every entry naming both the applying criterion ID and the target criterion ID? (FAIL) no inventory; (PARTIAL) inventory lacks target IDs; (PASS) full paired inventory including "C-30 (for C-02), C-31 (for C-11), C-32 (for C-28)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 fires. When active: (FAIL) section absent or fewer than 4 columns; (PARTIAL) 4 columns, Variation absent; (PASS) 5 columns including Variation. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation column absent; (PARTIAL) Variation in column 5 after Mechanism; (PASS) column order "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | (FAIL) C-28 absent from declarations block; (PARTIAL) cascade declared but trigger ID absent; (PASS) trigger ID named -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared baseline table; all N x 32 rows written out in full; (PARTIAL) shared table present but differentiating cells lack explicit override quotes; (PASS) shared table present AND differentiating cells carry explicit override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) cascade-dependent C-27 and C-28 listed as independent entries with no chain notation; (PARTIAL) cascade noted but "per cascade" annotation absent; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade" or equivalent. C-31 auto-PASS when C-07 does not fire -- write the declaration. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) cascade fires for C-28 with no design-time note in SETUP; (PARTIAL) design-time note present but specific template element not named; (PASS) note present AND names "Variation in causal position, column 4" or equivalent. C-32 auto-PASS when C-07 does not fire -- write the declaration. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholder text is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate evidence
that is identical across all N scored outputs in a named "Shared baseline evidence" table at
the head of Phase 2, before the first per-output heading. Per-variation scoring rows use
"(shared)" as a reference token for criteria where the evidence and verdict match the shared
baseline. Differentiating cells carry an explicit override quote from that variation's output.
This satisfies C-30 without repeating 32 x N identical evidence cells.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 32-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-32 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-32): X/25 x 10 = YY.YY pts
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

Example of a fully instantiated action line: "Update the C-07 cascade auto-PASS block in the
PHASE 1 SETUP of quest-score.md to read 'C-07 auto-PASS. C-27 and C-28 also auto-PASS per
cascade -- no regression table is instantiated.' grouping cascade dependents under the primary
trigger with explicit 'per cascade' annotation -- so C-31 is satisfied on every run."

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
Note that N_aspirational=25 means each aspirational criterion contributes 10/25 = 0.40 pt to
the composite; a single PARTIAL incurs 0.20 pt degradation from the ceiling.
