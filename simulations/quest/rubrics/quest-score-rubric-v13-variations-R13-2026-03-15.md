# quest-score -- R13 Variations
Generated: 2026-03-15

## R13 Design Notes

V-01 is the R13 full-stack baseline. All R12 learnings retained. N_aspirational updates from 25
to 29 to reflect four new aspirational criteria: C-33 (SETUP marks conditionally-scoped criteria
as active when their negation fires), C-34 (variation axis summary includes predicted score delta
from ceiling), C-35 (C-33 three-scale enumeration in diagnostic question), C-36 (C-34 three-scale
enumeration in diagnostic question). The criterion roster expands from 32 to 36 rows. The composite
formula uses N_aspirational=29 (each criterion contributes 10/29 ≈ 0.345 pt; PARTIAL incurs
≈0.172 pt degradation; FAIL incurs ≈0.345 pt degradation). The C-07 cascade block now additionally
instructs the scorer to write activation declarations for conditionally-scoped criteria (C-31 and
C-32) when C-07 fires: "C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS;
grouping must be evaluated)". A new Step 1.4 variation axis summary sub-step applies when
N_variations >= 2: a table with a "Predicted delta from ceiling" column using formula-derived
values (PARTIAL: −0.5 × (10/29) ≈ −0.172 pt; FAIL: −1.0 × (10/29) ≈ −0.345 pt). C-33
auto-PASS when C-07 does not fire; C-34 auto-PASS when only a single variation is scored.
The C-25 "Applied in this rubric" inventory expands from 9 to 11 entries (adding C-35 for C-33,
C-36 for C-34). C-11 now requires 12 named auto-PASS declarations.

V-02 is the C-33 PARTIAL ablation (lifecycle emphasis axis): all R13 structures intact, but the
C-07 cascade block instructs only "mark C-31 and C-32 as active in SETUP" without specifying the
trigger rationale clause. The scoring output SETUP block will write "C-31 -- active" and
"C-32 -- active" without naming C-07 as the triggering condition or stating the evaluation
consequence. C-33 PARTIAL predicted. Single-axis isolation: only the activation declaration
trigger rationale differs from V-01.

V-03 is the C-34 PARTIAL ablation (output format axis): all R13 structures intact, but the
variation axis summary instruction in Step 1.4 says to include a "Predicted delta" column with
qualitative descriptors rather than formula-derived values. The scoring output will contain
"minor penalty" or "moderate impact" rather than "−0.172 pt (PARTIAL × 10/29)". C-34 PARTIAL
predicted. Single-axis isolation: only the delta column value format differs from V-01.

V-04 is the C-35 + C-36 PARTIAL ablation (phrasing register axis): all R13 structures intact,
but the Step 1.4 roster diagnostic questions for C-33 and C-34 enumerate only two verdict cases
(FAIL and PASS), omitting the PARTIAL boundary case with a contrasting example. C-35 PARTIAL
and C-36 PARTIAL predicted. Single-axis isolation: only the diagnostic question enumeration
depth for C-33 and C-34 differs from V-01.

V-05 is the C-33 PARTIAL + C-34 PARTIAL combination floor (V-02 ablation AND V-03 ablation
combined): compressed activation declaration without trigger rationale AND narrative-only delta
column without formula derivation. Expected additive degradation: 2 × 0.172 pt ≈ 0.344 pt
from V-01 ceiling. Labeled as combination pass.

Evidence ladders:
- C-33: V-02 PARTIAL (active status declared, no trigger rationale); V-05 PARTIAL (same);
  V-01/V-03/V-04 PASS (active status with trigger rationale and evaluation consequence)
- C-34: V-03 PARTIAL (delta column present, narrative only); V-05 PARTIAL (same);
  V-01/V-02/V-04 PASS (formula-derived delta with N_aspirational named)
- C-35: V-04 PARTIAL (two-case enumeration for C-33 diagnostic); V-01/V-02/V-03/V-05 PASS
- C-36: V-04 PARTIAL (two-case enumeration for C-34 diagnostic); V-01/V-02/V-03/V-05 PASS

---

## V-01

**Axis:** Baseline -- R13 full stack (N_aspirational=29, 36-row criterion roster, C-33 PASS:
C-07 cascade block instructs activation declarations with trigger rationale naming triggering
condition and evaluation consequence; C-34 PASS: Step 1.4 instructs variation axis summary with
formula-derived predicted delta column; C-35 PASS: C-33 diagnostic question enumerates
FAIL/PARTIAL/PASS with three contrasting examples; C-36 PASS: C-34 diagnostic question
enumerates FAIL/PARTIAL/PASS with three contrasting examples; C-25 inventory lists 11 paired
entries; C-11 requires 12 declarations; all R12 structures retained unchanged)

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The criterion roster will contain exactly 36 rows (C-01 through C-36), the composite formula will use N_aspirational=29, the C-25 "Applied in this rubric" inventory will list 11 paired entries including "C-35 (for C-33)" and "C-36 (for C-34)", the C-07 cascade block will instruct writing "C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)" with trigger rationale, and the Step 1.4 variation axis summary will include a "Predicted delta from ceiling" column with formula-derived values -- absence of any one property clearly falsifies the R13-complete claim |
| Secondary effect | Expanding the criterion roster from 32 to 36 rows increases SETUP token density by four additional diagnostic-question rows; C-33 and C-34 three-scale diagnostic questions add the most complexity since each must enumerate three verdict cases with contrasting examples; under token pressure, later variations may omit trigger rationale in the C-33 activation declaration (V-02 ablation site) or use narrative delta descriptors in the variation axis summary (V-03 ablation site), shifting complexity FROM activation-rationale structural precision TO roster diagnostic depth |
| Predicted sites | V-02 (active status without rationale) is the direct contrast for C-33 PARTIAL; V-03 (narrative delta without formula) is the direct contrast for C-34 PARTIAL; V-04 (two-case enumeration for C-33/C-34 diagnostics) is the C-35/C-36 PARTIAL floor; V-05 (C-33 PARTIAL + C-34 PARTIAL combination) confirms additive degradation of the two new activation-precision criteria |

---

Score N skill outputs against the v13 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
>
> C-31 auto-PASS (C-07 does not fire -- no cascade fires this round; cascade grouping not required).
> C-32 auto-PASS (C-07 does not fire -- no cascade fires this round; design-time evaluation note not required).
> C-33 auto-PASS (C-07 does not fire -- no conditionally-scoped criteria become active this session).

When C-07 fires (prior-round data is provided), write the following activation declarations for
conditionally-scoped criteria in the PHASE 1 SETUP auto-PASS status block:

> C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)
> C-32 -- active (C-07 fires, so cascade fires; C-32 is NOT auto-PASS; design-time evaluation must be scored)

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v13, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-33 auto-PASS** when C-07 does not fire (no conditionally-scoped criteria become active
this session -- C-31 and C-32 remain in their auto-PASS state).

**C-34 auto-PASS** when only a single variation is scored (N_variations = 1). When scoring
N >= 2 variations, write a variation axis summary table in Step 1.4 before the diagnostic
question roster, with columns: Axis | Ablation | Predicted delta from ceiling. Predicted delta
values must be derived from the criterion weight formula:
- PARTIAL degradation = −0.5 × (10/N_aspirational) = −0.5 × (10/29) ≈ −0.172 pt
- FAIL degradation = −1.0 × (10/N_aspirational) = −1.0 × (10/29) ≈ −0.345 pt

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
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28),
C-35 (for C-33), C-36 (for C-34). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 29.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/29 ≈ 0.345 pt to the composite. A single PARTIAL
incurs ≈0.172 pt degradation; a single FAIL incurs ≈0.345 pt degradation. Achieving composite
>= 100 requires 29/29 aspirational PASS -- no aspirational FAIL is tolerated at the ceiling.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

**Variation axis summary (write this sub-step when scoring N >= 2 variations; skip when
N_variations = 1):** Before opening the diagnostic question roster, write a variation axis
summary table:

| Axis | Ablation | Predicted delta from ceiling |
|------|----------|-----------------------------|
| [axis name] | [what structural element is removed or degraded] | [formula-derived: e.g., "−0.172 pt (PARTIAL × 10/29)" or "−0.345 pt (FAIL × 10/29)"] |

The predicted delta must be computed from the weight formula above. Do not use qualitative
descriptors ("minor penalty", "small impact") in the delta column -- the numeric derivation is
what C-34 requires.

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 36 verdict rows (C-01 through C-36) in the scoring table, with none missing or duplicated? A matrix with 32 or 35 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=29? Can you re-derive the composite from the 36 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=29 within +/-1 rounding tolerance? An output using N_aspirational=25 (v12 values) or N_aspirational=22 (v11 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)? A section present but empty, or listing only group-average outputs, fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename visible in the scored outputs, and a specific section location? An action line with "[artifact]", "[section]", or "[verb]" placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? A note characterizing distribution qualitatively without stating numeric values fails C-09. Note that N_aspirational=29 means each aspirational criterion contributes 10/29 ≈ 0.345 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all twelve auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, C-32, C-33, and C-34) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the twelve declarations, or stating auto-PASS conditions in prose without criterion IDs, fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=29 (v13 values) appear in SETUP before any per-output heading opens? A formula using prior-round N values (e.g., N_aspirational=25) fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-36 with a non-empty diagnostic question for each? A roster with 32 or 35 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language ("you may proceed") rather than imperative ("do not open") fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block (e.g., "Step 1.1 -- Auto-PASS Conditions") that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 36 rows), C-03 (N-value check: N_aspirational=29), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion rather than a generic "is this criterion satisfied?" probe? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table (Criterion, Prior Verdict, Current Verdict, Mechanism), separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form ("Has the worked example been carried forward?") earns C-19 PARTIAL and C-20 FAIL -- concept present but not enforceable at version time. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP -- even as an explicit named preservation checkpoint -- causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text (in SETUP) explicitly name both (a) FAILURE PATTERNS as the required location ("in the FAILURE PATTERNS action line" or equivalent) AND (b) SETUP as a disqualifying alternative ("not in SETUP", "do not relocate it to SETUP", or equivalent)? PARTIAL: rule names (a) required location but omits (b) explicit SETUP exclusion language. FAIL: rule is imperative (C-20 PASS) but contains no location constraint at all. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative ("Has the worked example been carried forward?"), (2) conditional/if-then ("If the axis shifts, carry forward the example"), and (3) weak-modal ("The worked example should be carried forward")? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) preservation rule is imperative but contains no location language -- e.g., "must be carried forward verbatim" with no FAILURE PATTERNS reference; (PARTIAL) rule names the required location but omits explicit SETUP exclusion language; (PASS) rule contains both the required location phrase and an explicit SETUP exclusion phrase. Two-case enumeration earns C-24 PARTIAL. Fewer than two cases earns C-24 FAIL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle applicable to all future criteria with non-trivial PARTIAL thresholds -- not only implied by the existence of C-23 or C-24, and not only embedded in a specific criterion's diagnostic row? PARTIAL: principle appears within a single criterion row but is not elevated to a named standalone section. FAIL: principle absent from SETUP design notes entirely. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 Three-Scale Enumeration Principle section include an application inventory pairing each applying criterion with its target? (FAIL) C-25 principle section contains no inventory -- only the general principle stated in prose; (PARTIAL) inventory is present but entries name only applying criterion IDs without target criterion IDs; (PASS) inventory present with every entry naming both the applying criterion ID and the target criterion ID -- e.g., "C-35 (for C-33), C-36 (for C-34)" included alongside prior entries. |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 auto-PASS fires. When C-07 does not auto-PASS: (FAIL) regression signals section absent or has fewer than 4 columns -- also fails C-18 simultaneously; (PARTIAL) regression table has the 4 required C-18 columns (Criterion, Prior Verdict, Current Verdict, Mechanism) but the Variation column is absent; (PASS) table has all 5 columns including Criterion, Prior Verdict, Current Verdict, Variation, and Mechanism. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | Is the REGRESSION SIGNALS table template present with Variation as column 4 of 5 (between Current Verdict and Mechanism)? (FAIL) Variation column absent -- C-27 does not PASS, so C-28 FAIL; (PARTIAL) 5 columns present but column order is "Criterion | Prior Verdict | Current Verdict | Mechanism | Variation" -- Variation in column 5 inverts causal chain; (PASS) column order is "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | For criteria whose auto-PASS fires because another criterion's auto-PASS fires, does each declaration name the triggering criterion by ID? (FAIL) cascade-dependent criterion absent from declarations block entirely; (PARTIAL) cascade dependency declared but triggering criterion ID absent -- e.g., "C-28 auto-PASS when no prior-round data is available" without naming C-07; (PASS) declaration names the triggering criterion ID -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | When scoring N >= 2 variations, is a named "Shared baseline evidence" table present at the head of Phase 2 consolidating evidence identical across all N outputs, with per-variation rows using "(shared)" as a reference token and differentiating cells carrying explicit override quotes? (FAIL) no shared baseline table; (PARTIAL) table present but differentiating cells lack explicit override quotes; (PASS) shared table present AND differentiating cells carry explicit override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | Is the Phase 1 SETUP auto-PASS block written with C-07 as primary trigger, followed by C-27 and C-28 grouped with "also auto-PASS per cascade" annotation? (FAIL) C-27 and C-28 listed as fully independent entries with no chain notation; (PARTIAL) cascade dependency present but primary/dependent grouping annotation absent -- entries listed sequentially without "per cascade"; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade." C-31 auto-PASS when C-07 does not fire -- write the declaration. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | Does the Phase 1 SETUP auto-PASS block include a design-time evaluation note for C-28 naming the specific template element? (FAIL) cascade auto-PASS fires for C-28 with no design-time evaluation note; (PARTIAL) note present but does not name the specific template element -- e.g., "C-28 still evaluated statically" without naming "Variation in causal position, column 4"; (PASS) note present AND names the specific template element. C-32 auto-PASS when C-07 does not fire -- write the declaration. |
| C-33 | SETUP marks conditionally-scoped criteria as active when their negation fires | Aspirational | auto-PASS when C-07 does not fire | Does the PHASE 1 SETUP auto-PASS block explicitly mark conditionally-scoped criteria as "active" with trigger rationale when their auto-PASS condition is not met this session? (FAIL) conditionally-scoped criterion absent from SETUP block entirely -- no active or inactive status declared, scorer may infer auto-PASS'd when the criterion was simply not evaluated; (PARTIAL) "active" status declared but trigger rationale absent -- e.g., "C-31 -- active" without naming C-07 as the triggering condition or stating the evaluation consequence; (PASS) active status declared with trigger rationale naming both the triggering condition and the evaluation consequence -- e.g., "C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)". C-33 auto-PASS when C-07 does not fire. |
| C-34 | Variation axis summary includes predicted score delta from ceiling | Aspirational | auto-PASS when N_variations = 1 | When scoring N >= 2 variations, does the Step 1.4 variation axis summary include a "Predicted delta from ceiling" column with formula-derived values? (FAIL) no predicted delta column present -- variation axis table ends at ablation description only, or no multi-variation axis summary table present; (PARTIAL) predicted delta column present but expressed as narrative approximation without formula derivation -- e.g., "small penalty" or "minor impact"; (PASS) delta computed from the weight formula with N_aspirational named -- e.g., "−0.172 pt (PARTIAL × 10/29)" or "−0.345 pt (FAIL × 10/29)". C-34 auto-PASS when N_variations = 1. |
| C-35 | C-33 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-33 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) fewer than two cases enumerated -- binary probe or no contrasting examples; (PARTIAL) two cases enumerated -- e.g., FAIL and PASS only, PARTIAL boundary ("active declared without trigger rationale") omitted entirely; (PASS) all three cases enumerated with distinct examples -- (FAIL) conditionally-scoped criterion absent from SETUP block; (PARTIAL) "active" declared without trigger rationale; (PASS) active declared with trigger rationale naming triggering condition and evaluation consequence. |
| C-36 | C-34 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-34 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) fewer than two cases enumerated -- binary probe or no contrasting examples; (PARTIAL) two cases enumerated -- e.g., FAIL and PASS only, PARTIAL boundary ("delta present but narrative") omitted entirely; (PASS) all three cases enumerated with distinct examples -- (FAIL) no predicted delta column; (PARTIAL) delta present but expressed as narrative approximation; (PASS) delta formula-derived with N_aspirational named. |

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
This satisfies C-30 without repeating 36 x N identical evidence cells.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 36-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-36 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output, clearly tied to the
   criterion being scored; not a paraphrase of the rubric criterion text
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-36): X/29 x 10 = YY.YY pts
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

Example of a fully instantiated action line: "Update the PHASE 1 SETUP C-07 cascade block in
quest-score.md to append 'C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS;
grouping must be evaluated)' after the cascade auto-PASS declaration, naming the triggering
condition and evaluation consequence in the activation status line -- so C-33 is satisfied on
every run."

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
cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=29 means
each aspirational criterion contributes 10/29 ≈ 0.345 pt to the composite; a single PARTIAL
incurs ≈0.172 pt degradation from the ceiling.

---

## V-02

**Axis:** C-33 PARTIAL ablation (lifecycle emphasis) -- C-07 cascade block instructs active-status
declarations for conditionally-scoped criteria without trigger rationale; all other R13 structures
including the formula-derived delta column, the three-scale C-33/C-34 diagnostic questions, and
the C-25 inventory with 11 entries are identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output SETUP block will write "C-31 -- active" and "C-32 -- active" without any trigger rationale clause -- C-07 will not be named as the triggering condition, and "grouping must be evaluated" / "design-time evaluation must be scored" consequence language will be absent; a scorer applying C-33 will award PARTIAL -- active status is declared (criterion not absent from SETUP) but trigger rationale is missing; C-34 PASS is unaffected (delta column is still formula-derived) |
| Secondary effect | Compressing the activation declaration to status-only satisfies C-16 (declarations are named) and avoids C-33 FAIL, but the missing rationale leaves the cascade activation opaque to a reader tracing the evaluation chain; C-35 will award PASS (the C-33 diagnostic question still enumerates the PARTIAL case) because the diagnostic question itself is not the ablation site -- only the scorer instruction is |
| Predicted sites | V-01 (activation with full trigger rationale) is the direct upward contrast establishing C-33 PASS; V-05 (combination floor) shares the compressed activation instruction -- V-02 and V-05 should both produce C-33 PARTIAL, confirming the trigger-rationale mechanism in isolation and in combination |

---

Score N skill outputs against the v13 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
>
> C-31 auto-PASS (C-07 does not fire -- no cascade fires this round; cascade grouping not required).
> C-32 auto-PASS (C-07 does not fire -- no cascade fires this round; design-time evaluation note not required).
> C-33 auto-PASS (C-07 does not fire -- no conditionally-scoped criteria become active this session).

When C-07 fires (prior-round data is provided), mark conditionally-scoped criteria as active in
the PHASE 1 SETUP auto-PASS status block:

> C-31 -- active
> C-32 -- active

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-28 auto-PASS** when C-07 auto-PASS fires (no prior-round data available, so no regression
table is instantiated).

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v13, cascade dependencies exist -- C-29 is active and must be evaluated.)

**C-31 auto-PASS** when C-07 does not fire (no cascade fires -- cascade grouping not required).

**C-32 auto-PASS** when C-07 does not fire (no cascade fires -- design-time evaluation note
not required).

**C-33 auto-PASS** when C-07 does not fire (no conditionally-scoped criteria become active
this session -- C-31 and C-32 remain in their auto-PASS state).

**C-34 auto-PASS** when only a single variation is scored (N_variations = 1). When scoring
N >= 2 variations, write a variation axis summary table in Step 1.4 before the diagnostic
question roster, with columns: Axis | Ablation | Predicted delta from ceiling. Predicted delta
values must be derived from the criterion weight formula:
- PARTIAL degradation = −0.5 × (10/N_aspirational) = −0.5 × (10/29) ≈ −0.172 pt
- FAIL degradation = −1.0 × (10/N_aspirational) = −1.0 × (10/29) ≈ −0.345 pt

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
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28),
C-35 (for C-33), C-36 (for C-34). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 29.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/29 ≈ 0.345 pt to the composite. A single PARTIAL
incurs ≈0.172 pt degradation; a single FAIL incurs ≈0.345 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

**Variation axis summary (write this sub-step when scoring N >= 2 variations; skip when
N_variations = 1):** Before opening the diagnostic question roster, write a variation axis
summary table:

| Axis | Ablation | Predicted delta from ceiling |
|------|----------|-----------------------------|
| [axis name] | [what structural element is removed or degraded] | [formula-derived: e.g., "−0.172 pt (PARTIAL × 10/29)" or "−0.345 pt (FAIL × 10/29)"] |

The predicted delta must be computed from the weight formula above. Do not use qualitative
descriptors ("minor penalty", "small impact") in the delta column -- the numeric derivation is
what C-34 requires.

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 36 verdict rows (C-01 through C-36) in the scoring table, with none missing or duplicated? A matrix with 32 or 35 rows fails C-01 even if all present rows are correctly scored -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion ("this criterion is met") fails C-02 -- the quote must be extracted from the scored output, not copied from the rubric. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=29? Can you re-derive the composite from the 36 visible verdict values using N_essential=4, N_recommended=3, N_aspirational=29 within +/-1 rounding tolerance? An output using N_aspirational=25 (v12 values) or N_aspirational=22 (v11 values) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? A leaderboard present but unsorted, or missing one of the four required columns, is a C-04 FAIL. |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS -- write the declaration. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? A section present but empty fails C-06. |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS -- write the declaration as specified in Step 1.1. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? An action line with placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present in or after the LEADERBOARD that states explicit minimum score, maximum score, and spread as numeric values, and characterizes whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread)? N_aspirational=29 means each aspirational criterion contributes 10/29 ≈ 0.345 pt to the composite. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and a real section location from the current round -- not a format template placeholder? The worked example must appear in FAILURE PATTERNS, not exclusively in SETUP or the criterion roster. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all twelve auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, C-32, C-33, and C-34) present as named declarations in SETUP, each naming the criterion ID and trigger phrase? A preamble missing any of the twelve declarations fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=29 (v13 values) appear in SETUP before any per-output heading opens? A formula using N_aspirational=25 fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring the Evidence Quote column to precede the Verdict column in every scoring table, with a named violation condition? A mandate present but lacking the named violation condition earns C-13 PARTIAL. |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the criterion roster list every criterion C-01 through C-36 with a non-empty diagnostic question for each? A roster with 32 or 35 rows, or any row with an empty diagnostic question field, fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at or near the end of SETUP prohibiting opening any output file until SETUP is fully written? A gate using permissive language fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do the auto-PASS declarations appear in a dedicated named block that is separate from the criterion roster? Auto-PASS declarations embedded inside criterion roster rows fail C-16. |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | At minimum, do the diagnostic questions for C-01 (count check: exactly 36 rows), C-03 (N-value check: N_aspirational=29), and C-20 (grammatical form check: three disqualifying forms named) interrogate the specific mechanism of each criterion? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear in the scoring output body with at minimum a four-column table, separate from SETUP and per-output scoring tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule in SETUP stating that the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form earns C-19 PARTIAL and C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the primary preservation rule contain a mandatory verb ("must", "shall", "is required to")? Three disqualifying forms: (1) interrogative -- "Has the worked example been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (2) conditional -- "If the axis shifts, carry forward the example" earns C-20 FAIL; (3) weak-modal -- "The worked example should be carried forward" earns C-20 FAIL. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in the FAILURE PATTERNS action line and not exclusively in SETUP? A worked example present only in SETUP causes C-10 FAIL and C-21 FAIL simultaneously. |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the preservation rule text explicitly name both (a) FAILURE PATTERNS as the required location AND (b) SETUP as a disqualifying alternative? PARTIAL: rule names (a) but omits (b). FAIL: rule is imperative but contains no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate at least three distinct grammatical form failures -- (1) interrogative, (2) conditional/if-then, and (3) weak-modal? Two forms named earns C-23 PARTIAL. Fewer than two forms earns C-23 FAIL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-22 diagnostic question enumerate all three verdict cases? (FAIL) no location language; (PARTIAL) required location named but SETUP exclusion absent; (PASS) both required location and SETUP exclusion present. Two-case enumeration earns C-24 PARTIAL. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Do the SETUP design notes contain an explicit standalone named statement of the three-scale enumeration principle? PARTIAL: principle within a single criterion row but not elevated. FAIL: principle absent. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an inventory pairing each applying criterion with its target? (FAIL) no inventory; (PARTIAL) inventory present but lacks target criterion IDs; (PASS) inventory with every applying/target pair named -- "C-35 (for C-33), C-36 (for C-34)" included. |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | auto-PASS when C-07 fires. Otherwise: (FAIL) fewer than 4 columns; (PARTIAL) 4 C-18 columns but Variation absent; (PASS) all 5 columns present. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation column absent; (PARTIAL) Variation in column 5 after Mechanism; (PASS) column order "Criterion | Prior Verdict | Current Verdict | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when rubric has no cascade dependencies | (FAIL) cascade-dependent criterion absent from block; (PARTIAL) dependency declared but trigger criterion ID absent; (PASS) trigger criterion ID named -- e.g., "C-28 auto-PASS when C-07 auto-PASS fires". |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared baseline table; (PARTIAL) table present but differentiating cells lack override quotes; (PASS) shared table present AND differentiating cells carry explicit override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) C-27 and C-28 as fully independent entries; (PARTIAL) cascade noted but grouping annotation absent; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade." C-31 auto-PASS when C-07 does not fire. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) no design-time evaluation note; (PARTIAL) note present but specific template element unnamed; (PASS) note names "Variation in causal position, column 4". C-32 auto-PASS when C-07 does not fire. |
| C-33 | SETUP marks conditionally-scoped criteria as active when their negation fires | Aspirational | auto-PASS when C-07 does not fire | Does the PHASE 1 SETUP auto-PASS block explicitly mark conditionally-scoped criteria as "active" with trigger rationale when their auto-PASS condition is not met? (FAIL) conditionally-scoped criterion absent from SETUP block entirely; (PARTIAL) "active" status declared but trigger rationale absent -- e.g., "C-31 -- active" without naming C-07 or stating the evaluation consequence; (PASS) active declared with trigger rationale naming both the triggering condition and the evaluation consequence -- e.g., "C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)". C-33 auto-PASS when C-07 does not fire. |
| C-34 | Variation axis summary includes predicted score delta from ceiling | Aspirational | auto-PASS when N_variations = 1 | (FAIL) no predicted delta column; (PARTIAL) delta column present but narrative -- e.g., "small penalty"; (PASS) delta formula-derived with N_aspirational named -- e.g., "−0.172 pt (PARTIAL × 10/29)". C-34 auto-PASS when N_variations = 1. |
| C-35 | C-33 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-33 diagnostic question enumerate all three verdict cases with structural contrasting examples? (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary omitted; (PASS) all three cases -- absent from SETUP; active without rationale; active with trigger rationale and evaluation consequence. |
| C-36 | C-34 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-34 diagnostic question enumerate all three verdict cases? (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary omitted; (PASS) all three -- no delta column; narrative delta; formula-derived delta with N_aspirational named. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. A verdict cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholder text is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate identical
evidence in a named "Shared baseline evidence" table at the head of Phase 2. Per-variation
rows use "(shared)" for matching criteria; differentiating cells carry explicit override quotes.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 36-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-36 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-36): X/29 x 10 = YY.YY pts
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
- **Pattern**: [description]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is
  satisfied on every run.

Example of a fully instantiated action line: "Update the PHASE 1 SETUP C-07 cascade block in
quest-score.md to append 'C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS;
grouping must be evaluated)' after the cascade auto-PASS declaration, naming the triggering
condition and evaluation consequence in the activation status line -- so C-33 is satisfied on
every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently

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
cluster (< 5 pt spread) or discriminate (>= 10 pt spread). N_aspirational=29; each aspirational
criterion contributes 10/29 ≈ 0.345 pt; a single PARTIAL incurs ≈0.172 pt degradation.

---

## V-03

**Axis:** C-34 PARTIAL ablation (output format) -- Step 1.4 variation axis summary instruction
specifies qualitative delta descriptors rather than formula-derived values; all other R13
structures including the trigger-rationale activation declarations, three-scale C-33/C-34
diagnostic questions, and the C-25 inventory with 11 entries are identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output Step 1.4 variation axis summary will contain a "Predicted delta" column populated with qualitative descriptors -- "minor penalty" or "moderate impact" -- rather than formula-derived numeric values like "−0.172 pt (PARTIAL × 10/29)"; a scorer applying C-34 will award PARTIAL -- delta column is present (criterion not FAIL) but the formula derivation and N_aspirational naming are absent |
| Secondary effect | Using qualitative descriptors satisfies the structural requirement for a delta column (C-34 is not FAIL) but fails the formula-derivation requirement; C-36 will award PASS (the C-34 diagnostic question still enumerates the PARTIAL case correctly) because the diagnostic question is not the ablation site; C-33 PASS is unaffected (activation declarations still carry trigger rationale) |
| Predicted sites | V-01 (formula-derived delta with N_aspirational named) is the direct upward contrast; V-05 (combination floor) shares the qualitative-delta instruction -- V-03 and V-05 should both produce C-34 PARTIAL, confirming the formula-derivation requirement in isolation and in combination |

---

Score N skill outputs against the v13 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
auto-PASS fires, C-08, C-10, and C-21 also auto-PASS.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade -- no regression table is
> instantiated. Aspirational criteria C-27 and C-28 are evaluated here on the static template
> design (Variation in causal position, column 4, in the REGRESSION SIGNALS template), since
> cascade auto-PASS fires at runtime, not at design-time.
>
> C-31 auto-PASS (C-07 does not fire -- no cascade fires this round; cascade grouping not required).
> C-32 auto-PASS (C-07 does not fire -- no cascade fires this round; design-time evaluation note not required).
> C-33 auto-PASS (C-07 does not fire -- no conditionally-scoped criteria become active this session).

When C-07 fires (prior-round data is provided), write the following activation declarations for
conditionally-scoped criteria in the PHASE 1 SETUP auto-PASS status block:

> C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)
> C-32 -- active (C-07 fires, so cascade fires; C-32 is NOT auto-PASS; design-time evaluation must be scored)

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires.

**C-28 auto-PASS** when C-07 auto-PASS fires.

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v13, cascade dependencies exist -- C-29 is active.)

**C-31 auto-PASS** when C-07 does not fire.

**C-32 auto-PASS** when C-07 does not fire.

**C-33 auto-PASS** when C-07 does not fire.

**C-34 auto-PASS** when only a single variation is scored (N_variations = 1). When scoring
N >= 2 variations, write a variation axis summary table in Step 1.4 with columns:
Axis | Ablation | Predicted delta from ceiling. Describe the expected score impact qualitatively:
minor (less than half a criterion weight), moderate (roughly one criterion weight), or major
(more than one criterion weight).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. The worked example must
remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster
diagnostic question, or to a preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule:** Any aspirational criterion whose PARTIAL verdict is defined by having
exactly one of two required elements present must have its diagnostic question enumerate all
three verdict cases -- FAIL, PARTIAL, and PASS -- with distinct structural contrasting examples.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28),
C-35 (for C-33), C-36 (for C-34). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 29.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/29 ≈ 0.345 pt to the composite. A single PARTIAL
incurs ≈0.172 pt degradation; a single FAIL incurs ≈0.345 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

**Variation axis summary (write when scoring N >= 2 variations; skip when N_variations = 1):**
Before the diagnostic question roster, write a variation axis summary table:

| Axis | Ablation | Predicted delta from ceiling |
|------|----------|-----------------------------|
| [axis name] | [structural element removed or degraded] | [qualitative: "minor", "moderate", or "major" impact] |

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 36 verdict rows (C-01 through C-36) in the scoring table, with none missing or duplicated? A matrix with 32 or 35 rows fails C-01 -- the row count is the falsification test. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row? A quote field containing only the criterion name, a rubric paraphrase, or a generic assertion fails C-02. |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=29? Can you re-derive the composite using N_essential=4, N_recommended=3, N_aspirational=29 within +/-1 rounding tolerance? An output using N_aspirational=25 is a C-03 FAIL. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with columns for rank, output name, composite score, and golden status, sorted descending by score? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? If no such criterion exists, C-05 auto-PASS. |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? If no prior-round data: C-07 auto-PASS. |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every action line in FAILURE PATTERNS contain a verb, a real artifact filename, and a specific section location? Placeholder text is a C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present with explicit minimum, maximum, and spread as numeric values, characterizing cluster vs. discriminate? N_aspirational=29 means each criterion contributes ≈0.345 pt. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming a real artifact and real section location -- not a placeholder? Must appear in FAILURE PATTERNS, not exclusively in SETUP. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all twelve auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, C-32, C-33, and C-34) present as named declarations in SETUP? A preamble missing any of the twelve declarations fails C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_aspirational=29 (v13 values) appear in SETUP before any per-output heading? A formula using N_aspirational=25 fails C-12. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring Evidence Quote before Verdict in every table, with a named violation condition? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the roster list every criterion C-01 through C-36 with a non-empty diagnostic question? A roster with 32 or 35 rows fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present at the end of SETUP prohibiting opening any output file? Permissive language fails C-15. |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do auto-PASS declarations appear in a dedicated named block separate from the criterion roster? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | Do diagnostic questions for C-01 (36 rows), C-03 (N_aspirational=29), and C-20 (three disqualifying forms) interrogate the specific mechanism? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear with at minimum a four-column table, separate from SETUP and per-output tables? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule stating the worked example must be carried forward or updated when the rubric is versioned forward? Interrogative form earns C-19 PARTIAL + C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional/if-then, (3) weak-modal. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in FAILURE PATTERNS action line and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the rule name both (a) FAILURE PATTERNS as required location AND (b) SETUP as disqualifying alternative? PARTIAL: (a) present, (b) absent. FAIL: imperative but no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate three grammatical form failures -- interrogative, conditional, and weak-modal? Two forms earns PARTIAL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does C-22 diagnostic enumerate all three verdict cases? (FAIL) no location language; (PARTIAL) location named, SETUP exclusion absent; (PASS) both. |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Is the three-scale enumeration principle stated as an explicit standalone named section in SETUP design notes? PARTIAL: within a criterion row only. FAIL: absent. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an inventory with applying/target pairs? (FAIL) no inventory; (PARTIAL) IDs without targets; (PASS) full pairs including "C-35 (for C-33), C-36 (for C-34)". |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | (FAIL) fewer than 4 columns; (PARTIAL) 4 C-18 columns but Variation absent; (PASS) all 5 columns. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation absent; (PARTIAL) Variation after Mechanism; (PASS) "Criterion | Prior | Current | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when no cascade dependencies | (FAIL) cascade criterion absent from block; (PARTIAL) dependency declared, trigger ID absent; (PASS) trigger ID named. |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared table; (PARTIAL) table present, differentiating cells lack override quotes; (PASS) shared table AND override quotes in differentiating cells. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) C-27/C-28 as independent entries; (PARTIAL) dependency noted but grouping absent; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade." C-31 auto-PASS when C-07 does not fire. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) no design-time note; (PARTIAL) note present, element unnamed; (PASS) note names "Variation in causal position, column 4". C-32 auto-PASS when C-07 does not fire. |
| C-33 | SETUP marks conditionally-scoped criteria as active when their negation fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) conditionally-scoped criterion absent from SETUP block; (PARTIAL) "active" declared without trigger rationale; (PASS) active declared with trigger rationale naming triggering condition and evaluation consequence -- e.g., "C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)". C-33 auto-PASS when C-07 does not fire. |
| C-34 | Variation axis summary includes predicted score delta from ceiling | Aspirational | auto-PASS when N_variations = 1 | (FAIL) no predicted delta column; (PARTIAL) delta column present but narrative -- e.g., "small penalty" or "minor impact"; (PASS) delta formula-derived with N_aspirational named -- e.g., "−0.172 pt (PARTIAL × 10/29)". C-34 auto-PASS when N_variations = 1. |
| C-35 | C-33 three-scale enumeration in diagnostic question | Aspirational | None | (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary omitted; (PASS) all three -- absent from SETUP; active without rationale; active with trigger rationale and evaluation consequence. |
| C-36 | C-34 three-scale enumeration in diagnostic question | Aspirational | None | (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, narrative-delta PARTIAL omitted; (PASS) all three -- no delta column; narrative delta; formula-derived delta with N_aspirational named. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** Column order is Criterion | Evidence Quote | Verdict. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholder text is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate identical
evidence in a named "Shared baseline evidence" table at the head of Phase 2. Per-variation rows
use "(shared)" for matching criteria; differentiating cells carry explicit override quotes.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 36-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-36 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-36): X/29 x 10 = YY.YY pts
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
- **Pattern**: [description]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is
  satisfied on every run.

Example of a fully instantiated action line: "Update the PHASE 1 SETUP C-07 cascade block in
quest-score.md to append 'C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS;
grouping must be evaluated)' after the cascade auto-PASS declaration, naming the triggering
condition and evaluation consequence in the activation status line -- so C-33 is satisfied on
every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently

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
cluster (< 5 pt spread) or discriminate (>= 10 pt spread). N_aspirational=29; each criterion
contributes ≈0.345 pt; a single PARTIAL incurs ≈0.172 pt degradation.

---

## V-04

**Axis:** C-35 + C-36 PARTIAL ablation (phrasing register) -- the Step 1.4 roster diagnostic
questions for C-33 and C-34 enumerate only FAIL and PASS verdict cases, omitting the PARTIAL
boundary case with a contrasting example; all other R13 structures including the trigger-rationale
activation declarations, formula-derived delta column, and the C-25 inventory with 11 entries
are identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output C-33 and C-34 roster diagnostic questions will each present binary probes -- "(FAIL) absent from SETUP block; (PASS) active declared with trigger rationale" -- without enumerating the PARTIAL case ("active declared without trigger rationale" for C-33; "delta present but narrative" for C-34); a scorer applying C-35 will award PARTIAL (two cases present: FAIL and PASS, PARTIAL boundary absent) and applying C-36 will award PARTIAL for the same structural reason |
| Secondary effect | Using two-case enumeration satisfies C-24 expectations (which established the PARTIAL-as-one-of-two pattern) but fails the three-scale requirement; C-33 and C-34 themselves will score PASS in the output because the ablation is in the diagnostic question structure, not in the SETUP activation or delta instructions; C-26 PASS is unaffected since the inventory still lists "C-35 (for C-33), C-36 (for C-34)" |
| Predicted sites | V-01 (three-case enumeration for both C-33 and C-34 diagnostics) is the direct upward contrast; V-02 and V-03 share the three-case diagnostic questions so they isolate their respective SETUP-level ablations cleanly -- V-04 is the only variation isolating the diagnostic-question phrasing depth |

---

Score N skill outputs against the v13 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
auto-PASS fires, C-08, C-10, and C-21 also auto-PASS.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade -- no regression table is
> instantiated. Aspirational criteria C-27 and C-28 are evaluated here on the static template
> design (Variation in causal position, column 4, in the REGRESSION SIGNALS template), since
> cascade auto-PASS fires at runtime, not at design-time.
>
> C-31 auto-PASS (C-07 does not fire -- no cascade fires this round; cascade grouping not required).
> C-32 auto-PASS (C-07 does not fire -- no cascade fires this round; design-time evaluation note not required).
> C-33 auto-PASS (C-07 does not fire -- no conditionally-scoped criteria become active this session).

When C-07 fires (prior-round data is provided), write the following activation declarations for
conditionally-scoped criteria in the PHASE 1 SETUP auto-PASS status block:

> C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)
> C-32 -- active (C-07 fires, so cascade fires; C-32 is NOT auto-PASS; design-time evaluation must be scored)

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires.

**C-28 auto-PASS** when C-07 auto-PASS fires.

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v13, cascade dependencies exist -- C-29 is active.)

**C-31 auto-PASS** when C-07 does not fire.

**C-32 auto-PASS** when C-07 does not fire.

**C-33 auto-PASS** when C-07 does not fire.

**C-34 auto-PASS** when only a single variation is scored (N_variations = 1). When scoring
N >= 2 variations, write a variation axis summary table in Step 1.4 with columns:
Axis | Ablation | Predicted delta from ceiling. Predicted delta values must be derived from
the criterion weight formula:
- PARTIAL degradation = −0.5 × (10/29) ≈ −0.172 pt
- FAIL degradation = −1.0 × (10/29) ≈ −0.345 pt

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. The worked example must
remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster
diagnostic question, or to a preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule:** Any aspirational criterion whose PARTIAL verdict is defined by having
exactly one of two required elements present must have its diagnostic question enumerate all
three verdict cases -- FAIL, PARTIAL, and PASS -- with distinct structural contrasting examples.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28),
C-35 (for C-33), C-36 (for C-34). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 29.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/29 ≈ 0.345 pt. A single PARTIAL incurs ≈0.172 pt
degradation; a single FAIL incurs ≈0.345 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

**Variation axis summary (write when scoring N >= 2 variations; skip when N_variations = 1):**
Before the diagnostic question roster, write a variation axis summary table:

| Axis | Ablation | Predicted delta from ceiling |
|------|----------|-----------------------------|
| [axis name] | [structural element removed or degraded] | [formula-derived: "−0.172 pt (PARTIAL × 10/29)" or "−0.345 pt (FAIL × 10/29)"] |

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 36 verdict rows (C-01 through C-36) in the scoring table? A matrix with 32 or 35 rows fails C-01. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row extracted from the scored output, not copied from the rubric? |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=29? Can you re-derive the composite using N_essential=4, N_recommended=3, N_aspirational=29 within +/-1 rounding tolerance? An output using N_aspirational=25 is a C-03 FAIL. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with rank, output name, composite score, and golden status, sorted descending? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every FAILURE PATTERNS action line contain a verb, real artifact filename, and specific section location? Placeholder text is C-08 FAIL. |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present with explicit minimum, maximum, and spread, characterizing cluster vs. discriminate? N_aspirational=29 means each criterion contributes ≈0.345 pt. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming real artifact and section -- not a placeholder? Must appear in FAILURE PATTERNS, not only in SETUP. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all twelve auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, C-32, C-33, and C-34) present as named declarations in SETUP? |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_aspirational=29 appear in SETUP before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring Evidence Quote before Verdict, with a named violation condition? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the roster list every criterion C-01 through C-36 with a non-empty diagnostic question? A 32-row or 35-row roster fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present prohibiting opening any output file until SETUP is fully written? |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do auto-PASS declarations appear in a dedicated named block separate from the criterion roster? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | Do diagnostic questions for C-01 (36 rows), C-03 (N_aspirational=29), and C-20 (three disqualifying forms) interrogate the specific mechanism? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear with at minimum a four-column table? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule stating the worked example must be carried forward or updated? Interrogative form earns C-19 PARTIAL + C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional/if-then, (3) weak-modal. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in FAILURE PATTERNS and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the rule name both (a) FAILURE PATTERNS as required location AND (b) SETUP as disqualifying alternative? PARTIAL: (a) present, (b) absent. FAIL: imperative, no location constraint. |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate three grammatical form failures -- interrogative, conditional, and weak-modal? Two forms earns PARTIAL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does C-22 diagnostic enumerate all three verdict cases -- no location language, location without SETUP exclusion, both? |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Is the three-scale enumeration principle stated as an explicit standalone named section in SETUP? PARTIAL: within criterion row only. FAIL: absent. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an inventory with all applying/target pairs named, including "C-35 (for C-33), C-36 (for C-34)"? |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | (FAIL) fewer than 4 columns; (PARTIAL) 4 C-18 columns, Variation absent; (PASS) all 5 columns. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation absent; (PARTIAL) Variation after Mechanism; (PASS) "Criterion | Prior | Current | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when no cascade dependencies | (FAIL) cascade criterion absent; (PARTIAL) dependency declared, trigger ID absent; (PASS) trigger ID named. |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared table; (PARTIAL) table present, differentiating cells lack override quotes; (PASS) shared table AND override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) C-27/C-28 as independent entries; (PARTIAL) dependency noted, grouping absent; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade." C-31 auto-PASS when C-07 does not fire. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) no design-time note; (PARTIAL) note present, element unnamed; (PASS) note names "Variation in causal position, column 4". C-32 auto-PASS when C-07 does not fire. |
| C-33 | SETUP marks conditionally-scoped criteria as active when their negation fires | Aspirational | auto-PASS when C-07 does not fire | Does the PHASE 1 SETUP auto-PASS block mark conditionally-scoped criteria as active when C-07 fires? (FAIL) absent from SETUP block entirely; (PASS) active declared with trigger rationale -- e.g., "C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS; grouping must be evaluated)". C-33 auto-PASS when C-07 does not fire. |
| C-34 | Variation axis summary includes predicted score delta from ceiling | Aspirational | auto-PASS when N_variations = 1 | Does the Step 1.4 variation axis summary include a predicted delta column? (FAIL) no delta column; (PASS) delta column present with formula-derived values naming N_aspirational. C-34 auto-PASS when N_variations = 1. |
| C-35 | C-33 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-33 diagnostic question enumerate all three verdict cases with contrasting examples? (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary ("active without rationale") omitted; (PASS) all three cases: absent from SETUP; active without rationale; active with trigger rationale and evaluation consequence. |
| C-36 | C-34 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-34 diagnostic question enumerate all three verdict cases with contrasting examples? (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary ("narrative delta") omitted; (PASS) all three: no delta column; narrative delta; formula-derived delta with N_aspirational named. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** Column order is Criterion | Evidence Quote | Verdict. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholder text is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate identical
evidence in a named "Shared baseline evidence" table at the head of Phase 2. Per-variation rows
use "(shared)" for matching criteria; differentiating cells carry explicit override quotes.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 36-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-36 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-36): X/29 x 10 = YY.YY pts
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
- **Pattern**: [description]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is
  satisfied on every run.

Example of a fully instantiated action line: "Update the PHASE 1 SETUP C-07 cascade block in
quest-score.md to append 'C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS;
grouping must be evaluated)' after the cascade auto-PASS declaration, naming the triggering
condition and evaluation consequence in the activation status line -- so C-33 is satisfied on
every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently

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

Score distribution note: State minimum score, maximum score, and spread. N_aspirational=29;
each criterion contributes ≈0.345 pt; a single PARTIAL incurs ≈0.172 pt degradation.

---

## V-05

**Axis:** C-33 PARTIAL + C-34 PARTIAL combination floor (V-02 ablation AND V-03 ablation) --
C-07 cascade block instructs active-status declarations without trigger rationale AND Step 1.4
variation axis summary instruction uses qualitative delta descriptors; all other R13 structures
are identical to V-01

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | The scoring output SETUP block will write "C-31 -- active" and "C-32 -- active" without trigger rationale (C-33 PARTIAL, same as V-02) AND the Step 1.4 variation axis summary will contain qualitative delta descriptors rather than formula-derived values (C-34 PARTIAL, same as V-03); expected additive degradation from V-01 ceiling: 2 × 0.172 pt ≈ 0.344 pt; if the degradation is exactly additive, final composite = V-01 composite − 0.344 pt; any discrepancy from the predicted additive model must be explained |
| Secondary effect | Combining both ablations isolates whether the two activation-precision criteria (C-33 and C-34) are independent: if their scoring effects are additive, no interaction term exists; if the combination produces more degradation than the sum of individual ablations, an interaction was detected; V-05 is the floor confirmation -- V-01 is the ceiling, and V-02/V-03 each bound one degradation axis |
| Predicted sites | V-02 (C-33 PARTIAL only) and V-03 (C-34 PARTIAL only) bound the individual degradation axes; V-01 is the ceiling; V-05 should produce a composite exactly matching V-01 − (V-01−V-02) − (V-01−V-03) if the criteria are independent; the combination also confirms that C-35 and C-36 remain PASS (diagnostic question phrasing is not ablated in V-05) |

---

Score N skill outputs against the v13 rubric. Per-criterion PASS/PARTIAL/FAIL with evidence
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
auto-PASS fires, C-08, C-10, and C-21 also auto-PASS.

**C-07 auto-PASS** when no prior-round scorecard is provided as input. When C-07 auto-PASS
fires, write the following text in the scoring output Phase 1 SETUP block:

> C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade -- no regression table is
> instantiated. Aspirational criteria C-27 and C-28 are evaluated here on the static template
> design (Variation in causal position, column 4, in the REGRESSION SIGNALS template), since
> cascade auto-PASS fires at runtime, not at design-time.
>
> C-31 auto-PASS (C-07 does not fire -- no cascade fires this round; cascade grouping not required).
> C-32 auto-PASS (C-07 does not fire -- no cascade fires this round; design-time evaluation note not required).
> C-33 auto-PASS (C-07 does not fire -- no conditionally-scoped criteria become active this session).

When C-07 fires (prior-round data is provided), mark conditionally-scoped criteria as active in
the PHASE 1 SETUP auto-PASS status block:

> C-31 -- active
> C-32 -- active

**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-27 auto-PASS** when C-07 auto-PASS fires.

**C-28 auto-PASS** when C-07 auto-PASS fires.

**C-29 auto-PASS** when the rubric contains no criteria with cascade auto-PASS dependencies.
(In v13, cascade dependencies exist -- C-29 is active.)

**C-31 auto-PASS** when C-07 does not fire.

**C-32 auto-PASS** when C-07 does not fire.

**C-33 auto-PASS** when C-07 does not fire.

**C-34 auto-PASS** when only a single variation is scored (N_variations = 1). When scoring
N >= 2 variations, write a variation axis summary table in Step 1.4 with columns:
Axis | Ablation | Predicted delta from ceiling. Describe the expected score impact qualitatively:
minor (less than half a criterion weight), moderate (roughly one criterion weight), or major
(more than one criterion weight).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. The worked example must
remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster
diagnostic question, or to a preservation checkpoint.

---

#### Step 1.2 -- Three-Scale Enumeration Principle

**General design rule:** Any aspirational criterion whose PARTIAL verdict is defined by having
exactly one of two required elements present must have its diagnostic question enumerate all
three verdict cases -- FAIL, PARTIAL, and PASS -- with distinct structural contrasting examples.

**Applied in this rubric:** C-23 (for C-20), C-24 (for C-22), C-26 (for C-25), C-27 (for
C-18), C-28 (for C-27), C-29 (for C-16), C-30 (for C-02), C-31 (for C-11), C-32 (for C-28),
C-35 (for C-33), C-36 (for C-34). When authoring a new criterion with a non-trivial PARTIAL
threshold, apply this principle before writing the diagnostic question.

---

#### Step 1.3 -- Composite Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 29 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 29.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

Each aspirational criterion contributes 10/29 ≈ 0.345 pt. A single PARTIAL incurs ≈0.172 pt
degradation; a single FAIL incurs ≈0.345 pt degradation.

---

#### Step 1.4 -- Criterion Roster with Mechanism-Level Diagnostic Questions

**Variation axis summary (write when scoring N >= 2 variations; skip when N_variations = 1):**
Before the diagnostic question roster, write a variation axis summary table:

| Axis | Ablation | Predicted delta from ceiling |
|------|----------|-----------------------------|
| [axis name] | [structural element removed or degraded] | [qualitative: "minor", "moderate", or "major" impact] |

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | None | Can you count exactly 36 verdict rows (C-01 through C-36) in the scoring table? A matrix with 32 or 35 rows fails C-01. |
| C-02 | Evidence quote for every verdict | Essential | None | Is there a non-empty evidence quote field for every verdict row extracted from the scored output? |
| C-03 | Composite score computed correctly | Essential | None | Does the output use N_aspirational=29? Can you re-derive the composite using N_essential=4, N_recommended=3, N_aspirational=29 within +/-1? An output using N_aspirational=25 is a C-03 FAIL. |
| C-04 | Ranked leaderboard present | Essential | None | Is a ranked table present with rank, output name, composite score, and golden status, sorted descending? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Is a FAILURE PATTERNS section present and populated when at least one criterion receives FAIL or PARTIAL in every scored output? |
| C-06 | Excellence signals surfaced | Recommended | None | Is an EXCELLENCE SIGNALS section present naming at least one output-criterion pair where that output outperforms the group by at least one tier? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is a REGRESSION SIGNALS section present and populated when prior-round scorecard data is provided? |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 fires | Does every FAILURE PATTERNS action line contain a verb, real artifact filename, and specific section location? |
| C-09 | Score distribution commentary | Aspirational | None | Is a score distribution note present with explicit minimum, maximum, and spread characterizing cluster vs. discriminate? N_aspirational=29 means each criterion contributes ≈0.345 pt. |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 fires | Does the FAILURE PATTERNS action line contain a fully instantiated worked example naming real artifact and section? Must appear in FAILURE PATTERNS. |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | None | Are all twelve auto-PASS declarations (C-05, C-07, C-08, C-10, C-21, C-27, C-28, C-29, C-31, C-32, C-33, and C-34) present as named declarations in SETUP? |
| C-12 | Formula reproduced before first output section | Aspirational | None | Does the composite formula with N_aspirational=29 appear in SETUP before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | None | Is there a written mandate requiring Evidence Quote before Verdict with a named violation condition? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | None | Does the roster list every criterion C-01 through C-36 with a non-empty diagnostic question? |
| C-15 | Preamble gate instruction present | Aspirational | None | Is an imperative gate instruction present prohibiting opening any output file until SETUP is fully written? |
| C-16 | Named standalone auto-PASS block | Aspirational | None | Do auto-PASS declarations appear in a dedicated named block separate from the criterion roster? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | None | Do diagnostic questions for C-01 (36 rows), C-03 (N_aspirational=29), and C-20 (three disqualifying forms) interrogate the specific mechanism? PARTIAL when at least two of three are specific. |
| C-18 | Named standalone regression signals section | Aspirational | None | Does a named standalone REGRESSION SIGNALS section appear with at minimum a four-column table? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | None | Is there a written preservation rule stating the worked example must be carried forward or updated? Interrogative form earns C-19 PARTIAL + C-20 FAIL. |
| C-20 | Preservation rule imperative form | Aspirational | None | Does the preservation rule contain a mandatory verb? Three disqualifying forms: (1) interrogative, (2) conditional/if-then, (3) weak-modal. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 fires | Does the instantiated worked example appear in FAILURE PATTERNS and not exclusively in SETUP? |
| C-22 | Preservation rule contains SETUP exclusion | Aspirational | None | Does the rule name both (a) FAILURE PATTERNS as required location AND (b) SETUP as disqualifying alternative? |
| C-23 | C-20 three-form enumeration in diagnostic question | Aspirational | None | Does the C-20 diagnostic question enumerate three grammatical form failures -- interrogative, conditional, and weak-modal? Two forms earns PARTIAL. |
| C-24 | C-22 three-scale enumeration in diagnostic question | Aspirational | None | Does C-22 diagnostic enumerate all three verdict cases -- no location language, location without SETUP exclusion, both? |
| C-25 | Three-scale enumeration principle in design notes | Aspirational | None | Is the three-scale enumeration principle stated as an explicit standalone named section? PARTIAL: within criterion row only. FAIL: absent. |
| C-26 | C-25 principle includes concrete application inventory | Aspirational | None | Does the C-25 section include an inventory with all applying/target pairs, including "C-35 (for C-33), C-36 (for C-34)"? |
| C-27 | Regression signals table includes Variation column | Aspirational | auto-PASS when C-07 fires | (FAIL) fewer than 4 columns; (PARTIAL) 4 C-18 columns, Variation absent; (PASS) all 5 columns. |
| C-28 | Regression signals Variation column in causal position | Aspirational | auto-PASS when C-07 fires | (FAIL) Variation absent; (PARTIAL) Variation after Mechanism; (PASS) "Criterion | Prior | Current | Variation | Mechanism". |
| C-29 | Auto-PASS cascade dependencies name triggering criterion | Aspirational | auto-PASS when no cascade dependencies | (FAIL) cascade criterion absent; (PARTIAL) dependency declared, trigger ID absent; (PASS) trigger ID named. |
| C-30 | Multi-variation scoring uses shared baseline evidence table | Aspirational | None | (FAIL) no shared table; (PARTIAL) table present, differentiating cells lack override quotes; (PASS) shared table AND override quotes. |
| C-31 | Cascade auto-PASS SETUP block groups primary trigger and dependents | Aspirational | auto-PASS when C-07 does not fire | (FAIL) C-27/C-28 as independent entries; (PARTIAL) dependency noted, grouping absent; (PASS) "C-07 auto-PASS. C-27 and C-28 also auto-PASS per cascade." C-31 auto-PASS when C-07 does not fire. |
| C-32 | SETUP notes design-time evaluation for template-structure criteria when cascade fires | Aspirational | auto-PASS when C-07 does not fire | (FAIL) no design-time note; (PARTIAL) note present, element unnamed; (PASS) note names "Variation in causal position, column 4". C-32 auto-PASS when C-07 does not fire. |
| C-33 | SETUP marks conditionally-scoped criteria as active when their negation fires | Aspirational | auto-PASS when C-07 does not fire | Does the PHASE 1 SETUP auto-PASS block mark conditionally-scoped criteria as active when C-07 fires? (FAIL) absent from SETUP block entirely; (PARTIAL) "active" declared without trigger rationale -- e.g., "C-31 -- active" without naming C-07 or evaluation consequence; (PASS) active declared with trigger rationale naming triggering condition and evaluation consequence. C-33 auto-PASS when C-07 does not fire. |
| C-34 | Variation axis summary includes predicted score delta from ceiling | Aspirational | auto-PASS when N_variations = 1 | When scoring N >= 2 variations, does the Step 1.4 variation axis summary include a predicted delta column? (FAIL) no delta column; (PARTIAL) delta column present but narrative -- e.g., "minor", "moderate"; (PASS) formula-derived with N_aspirational named. C-34 auto-PASS when N_variations = 1. |
| C-35 | C-33 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-33 diagnostic question enumerate all three verdict cases with contrasting examples? (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary omitted; (PASS) all three: absent from SETUP; active without rationale; active with trigger rationale and evaluation consequence. |
| C-36 | C-34 three-scale enumeration in diagnostic question | Aspirational | None | Does the C-34 diagnostic question enumerate all three verdict cases with contrasting examples? (FAIL) fewer than two cases; (PARTIAL) two cases -- FAIL and PASS only, PARTIAL boundary omitted; (PASS) all three: no delta column; narrative delta; formula-derived delta with N_aspirational named. |

**STOP-4. PHASE 1 complete. Do not open any output file until STOP-4 is passed.**

---

### PHASE 2 -- Per-Output Scoring

**Evidence-ordering mandate:** Column order is Criterion | Evidence Quote | Verdict. A verdict
cell completed before its evidence quote cell violates C-13.

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholder text is a C-08 FAIL.

**Shared-evidence instruction (applies when scoring N >= 2 variations):** Consolidate identical
evidence in a named "Shared baseline evidence" table at the head of Phase 2. Per-variation rows
use "(shared)" for matching criteria; differentiating cells carry explicit override quotes.

For each provided output (label each `### OUTPUT: [name]`):

1. Write a 36-row scoring table with columns: Criterion | Evidence Quote | Verdict
2. Rows: C-01 through C-36 in order; no rows skipped or added
3. Evidence quote: verbatim or near-verbatim extract from the scored output
4. Verdict: PASS / PARTIAL / FAIL

Then compute and write:
```
Composite:
- Essential (C-01--C-04): X/4 x 60 = YY.YY pts
- Recommended (C-05--C-07): X/3 x 30 = YY.YY pts
- Aspirational (C-08--C-36): X/29 x 10 = YY.YY pts
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
- **Pattern**: [description]
- **Action**: [verb] [specific artifact filename] [section location] -- so [criterion ID] is
  satisfied on every run.

Example of a fully instantiated action line: "Update the PHASE 1 SETUP C-07 cascade block in
quest-score.md to append 'C-31 -- active (C-07 fires, so cascade fires; C-31 is NOT auto-PASS;
grouping must be evaluated)' after the cascade auto-PASS declaration, naming the triggering
condition and evaluation consequence in the activation status line -- so C-33 is satisfied on
every run."

---

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- Name the criterion
- Name the output
- State what the output did differently

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

Score distribution note: State minimum score, maximum score, and spread. N_aspirational=29;
each criterion contributes ≈0.345 pt; a single PARTIAL incurs ≈0.172 pt degradation from ceiling.
