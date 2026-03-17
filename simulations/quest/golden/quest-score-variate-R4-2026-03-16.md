# quest-score Variations -- Round 4 (v4-2026-03-16 rubric)
**Skill**: quest-score
**Rubric**: v4-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-16 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=8**
**Date**: 2026-03-16
**Round**: 4

---

## Context: what informed this round

Round 3 targeted the v3 rubric. The R3 champion carried axes D+E+F+G+H:

| Axis | Mechanism | Phase | Criterion target |
|------|-----------|-------|-----------------|
| D | MODEL CELL advisory -- positive evidence anchor instruction | Phase 2 entry | C-11, C-14 |
| E | YES/NO labeled declaration field for arithmetic verification | Phase 3 | C-12 |
| F | FORMULA CHANGE ALERT at load time (prompt-level) | Phase 1 | C-13 (prompt side) |
| G | Phase 1 delta block in scorer's output -- names prior AND current N_aspirational | Phase 1 | C-13 (output side) |
| H | Phase 2 entry lock -- gates first evidence row on model cell firing | Phase 2 | C-14 |

R3 ceiling: V-04 and V-05 reached 99.17 (with G+H at Phase 1 + Phase 2). V-03 (Axis I: per-row
annotation) reached only a ceiling because it placed all new enforcement at Phase 3, reinforcing
C-10 without advancing C-13/C-14.

v4 adds two new Aspirational criteria extracted from R3 signals:

| Change | R3 (v3) | R4 (v4) | Design consequence |
|--------|---------|---------|-------------------|
| C-15 (symmetric comparison completeness) | Not in rubric | New Aspirational -- every delta comparison must name both prior and current state | R3's Axis G required both sides for the formula delta only. C-15 generalizes this to ALL comparisons: regression verdicts, arithmetic discrepancies, any prior-vs-current contrast. V-03's Axis I named N_aspirational=6 (current) on every row but never wrote the prior value (4), earning PARTIAL on C-13. C-15 captures the full failure class. |
| C-16 (phase-distinct mechanism distribution) | Not in rubric | New Aspirational -- mechanisms must exist at 2+ distinct lifecycle phases | R3 V-04 champion (G+H) achieves C-16 already because G is at Phase 1 and H is at Phase 2. The criterion formalized what the champion demonstrated: phase distribution produces additive gains impossible with single-phase enforcement. |
| N_aspirational | 6 (C-09--C-14) | 8 (C-09--C-16) | Formula denominator changes: aspirational_pass / 6 -> aspirational_pass / 8 |

**What R4 variations must achieve beyond the R3 base (D+E+F+G+H):**

1. C-15 PASS: Every variation must ensure scorers write BOTH prior-state AND current-state values
   for every delta comparison -- formula parameters, regression verdicts, and arithmetic
   discrepancies. R3's G covered the formula delta. C-15 requires the complete audit.

2. C-16 PASS: R3's champion achieves this with G (Phase 1) + H (Phase 2). R4 variations must
   either explicitly carry this property or actively reinforce it, since C-16 is now scored.

3. N_aspirational update: All variations update the FORMULA CHANGE ALERT to declare
   N_aspirational=8 (was 6 in v3), and the delta block to write "N_aspirational: 6 -> 8".

**Variation axes explored this round:**

| Code | Axis | Target criterion | Hypothesis |
|------|------|-----------------|-----------|
| J | SYMMETRIC DELTA REGISTER -- mandatory two-column table at Phase 1 for all comparisons | C-15 | Structural requirement (Prior State | Current State columns) prevents one-sided comparisons by making the prior-state column a required cell, not an optional annotation |
| K | PHASE MECHANISM INVENTORY -- pre-Phase-1 declaration of which mechanisms activate at each phase | C-16 | Forcing explicit pre-declaration of Phase 1/2/3 mechanisms raises scorer awareness of phase distribution, turning accidental C-16 compliance into deliberate structural choice |
| L | SYMMETRY AUDIT SWEEP -- late-Phase-1 verification check that each comparison in the delta register has both sides filled | C-15 (redundant catch) | A post-write audit at Phase 1 exit catches any one-sided comparison before scoring begins; orthogonal to J's structural enforcement, analogous to E's role for arithmetic |
| M | Inertia framing -- explicit naming of the bare-scorecard baseline as the structural competitor at each phase | C-03, C-16 | Naming what inertia produces (no delta register, all mechanisms at Phase 3, evidence restatement) sets a concrete negative foil, motivating each departure and raising evidence cell precision |

Single-axis variations: V-01 (J), V-02 (K), V-03 (L).
Combined variations: V-04 (J+K, additive C-15+C-16), V-05 (J+K+M, highest ceiling candidate).

---

## V-01: Axis J -- Symmetric Delta Register

**Variation axis**: Output format -- mandatory DELTA REGISTER table with Prior State | Current State
columns at Phase 1 entry.

**Hypothesis**: A pre-formatted two-column register at Phase 1 forces symmetric comparisons for
ALL delta types (formula parameters, regression verdicts, arithmetic discrepancies) by making the
Prior State column structurally required. A blank Prior State cell is a visible structural gap
detectable without reading cell content -- the same way a blank evidence cell is detectable.
Scorers who would otherwise write only the current value (N_aspirational=8) are forced to
retrieve and state the prior value (6) because the column exists and blank cells are violations.
This drives C-15 from PARTIAL to PASS for all delta-containing scoring runs.

---

You are running quest-score against the v4 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v4 rubric changes the aspirational denominator from the v3 value.

  N_aspirational: 6 (v3) -> 8 (v4)

Composite formula (v4, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using aspirational_pass / 6. Any computation using the v3 denominator
is an error regardless of where the instruction appears. If a conflict exists between this
prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD AND DELTA REGISTER

Before scoring any output, complete the following in order. Do not proceed to Phase 2 until
all three sections are written.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-16 aspirational)
  (b) the exact composite formula text (as written above)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

A load summary missing any one of (a)--(d) earns PARTIAL on C-01. Missing the section
entirely earns FAIL.

**1b. Formula version delta**

Write the following in your scoring output (not just internally -- it must appear in the
output the user reads):

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If you cannot determine the prior version, write:
  "No prior version delta detectable -- scoring under v4 as the baseline version."

This declaration satisfies C-13's output-side requirement. The FORMULA CHANGE ALERT above
satisfies the prompt-side requirement; C-13 requires the declaration to appear in the scorer's
output.

**1c. SYMMETRIC DELTA REGISTER**

Produce the following table. Fill every cell before proceeding to Phase 2.

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [value from prior rubric version] | [value in v4] |
  | Regression verdicts | [prior-round verdict for each regressed pair, or "No prior-round data -- row N/A"] | [current verdict, or "--"] |
  | Arithmetic discrepancies | [stated score if discrepancy found, or "No discrepancy identified -- row N/A"] | [computed score if discrepancy found, or "--"] |

Rules:
  - A blank Prior State cell is a structural violation. Write the value, or write "N/A --
    [reason]" to trigger the N/A rule (earns C-15 PARTIAL for that row, not FAIL).
  - A blank Current State cell is also a structural violation.
  - If a row type has no applicable comparison in this scoring run, write in Prior State:
    "No prior-state value available in this scoring context." This earns PARTIAL for
    C-15 on that row -- it confirms the scorer audited the cell rather than skipping it.
  - The register must contain at least the N_aspirational row. Add rows for any additional
    delta comparisons encountered during scoring.

PHASE 1 COMPLETE -- proceed to Phase 2 only after 1a, 1b, and 1c are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL INSTRUCTION (fire at Phase 2 entry -- before any evidence row is written)**

The first evidence cell you write in this section is the model cell for all subsequent cells.
Write it as:
  Evidence (model): "from [output ID], [section or criterion]: [verbatim quote or structural
  observation that locates a specific feature in the output -- not a restatement of the
  criterion]"

Test: could a reader find the referenced feature in the output using only this evidence text?
If YES: acceptable. If NO: rewrite before entering the cell.

ENTRY LOCK: do not write any verdict row until the model cell above is written and passes
the test. A verdict written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature
    of the scored output. Evidence that restates the criterion ("the output has a leaderboard")
    is criterion restatement, not evidence -- rewrite it.
  - No row may be blank or missing.

After the table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 8 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs. Then proceed to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

Pick one output. Recompute its composite from the stated verdict counts and formula.

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/8
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

The "Matches stated score:" field is required. "Verification performed" or narrative equivalents
do not satisfy C-12 -- the binary declaration is required.

If a discrepancy is found, update the SYMMETRIC DELTA REGISTER Arithmetic Discrepancy row
with the stated score (Prior State) and computed score (Current State).

**3b. Regression section**

If a prior-round scorecard was provided:
  - Name any criterion-output pair that degraded from PASS (or PARTIAL) to a lower verdict.
  - Format: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  - Any regression entry must provide both the prior verdict AND the current verdict
    (symmetric). Writing only the current verdict is a C-15 violation.
  - Update the SYMMETRIC DELTA REGISTER Regression Verdicts row with the prior and current
    verdicts for each regressed pair.

If no prior-round file was provided:
  "No prior round data -- regression analysis cannot be performed."

Do not omit this section. An absent regression section earns C-09 FAIL.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

Ties must be noted explicitly. "See scores above" does not satisfy C-06 -- the ranking must
be a distinct sorted structure.

**EXCELLENCE SIGNALS**

For each criterion where one output clearly outperforms others, write:
  Signal: [output ID] -- [criterion ID] -- [specific structural mechanism in that output
          that produced the higher score -- name the design property, not the criterion label]

"V-05 scored highest overall" is not an excellence signal. The signal requires a specific
output-criterion pair and a structural explanation.

If no criterion shows a spread: "No score spread found. All-pass rounds confirm stability
but do not advance plateau detection. Consider redesigning variations for divergence."

**FAILURE PATTERNS**

For each criterion receiving PARTIAL or FAIL across ALL outputs:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES**

For each output, one paragraph explaining what structural choices drove its score relative
to other outputs. Do not list verdict counts -- explain the mechanism.

---

## V-02: Axis K -- Phase Mechanism Inventory

**Variation axis**: Lifecycle emphasis -- pre-Phase-1 MECHANISM INVENTORY requiring explicit
declaration of active mechanisms at Phase 1, Phase 2, and Phase 3 before any scoring begins.

**Hypothesis**: Forcing the scorer to consciously declare which mechanisms activate at each
lifecycle phase converts accidental C-16 compliance (present in R3 champions because G+H
happen to span phases 1 and 2) into deliberate structural choice. A mechanism inventory that
declares "Phase 1: [list], Phase 2: [list], Phase 3: [list]" makes phase gaps visible before
scoring begins rather than detectable only in post-hoc analysis. This also creates a
self-checking loop: a scorer who declares "Phase 1: none" must then ask why Phase 1 is
unguarded before proceeding. C-16 PASS becomes the expected outcome rather than a ceiling
signal.

---

You are running quest-score against the v4 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v4 rubric changes the aspirational denominator from the v3 value.

  N_aspirational: 6 (v3) -> 8 (v4)

Composite formula (v4, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

---

MECHANISM INVENTORY (write before Phase 1)

Before writing any load summary, scoring table, or verification block, declare your
enforcement mechanism plan for this scoring run. Name at least one active mechanism
at each phase you intend to use.

  MECHANISM INVENTORY
  Phase 1 (pre-scoring: formula declarations, delta blocks, load summaries):
    Active: [list each mechanism you will deploy -- e.g., "formula version delta block",
             "load summary with all four elements", "formula change alert acknowledgment"]

  Phase 2 (during evidence writing: model cells, entry locks, positive anchors):
    Active: [list each mechanism you will deploy -- e.g., "MODEL CELL at Phase 2 entry",
             "entry lock: no verdict before model cell written"]

  Phase 3 (post-scoring: arithmetic re-derivation, discrepancy declaration, regression):
    Active: [list each mechanism you will deploy -- e.g., "arithmetic re-derivation block",
             "YES/NO discrepancy declaration field", "regression section with prior/current verdicts"]

  Phase coverage: [count of phases with at least one active mechanism listed above]

Minimum standard: Phase coverage must be >= 2 to achieve C-16 PASS. If your inventory
shows coverage = 1, add mechanisms to a second phase before proceeding.

MECHANISM INVENTORY COMPLETE -- proceed to Phase 1.

---

PHASE 1: LOAD

Complete all three steps before proceeding to Phase 2.

**1a. Formula version delta declaration**

Write in your scoring output:
  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

Both values must appear. Writing only the current value (N_aspirational=8) earns PARTIAL on
C-13. Writing both (N_aspirational: 6 -> 8) earns PASS.

If prior version is not determinable:
  "No prior version delta detectable -- scoring under v4 as the baseline version."

**1b. Load summary**

Produce a block naming all four required elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-16 aspirational)
  (b) exact composite formula: composite = (E/5*60) + (R/3*30) + (A/8*10)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

Missing any one of (a)--(d) earns PARTIAL on C-01. Missing the section earns FAIL.

PHASE 1 COMPLETE

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (fire at Phase 2 entry)**

Write your first evidence cell as:
  Evidence (model): "from [output ID]: [verbatim quote or specific structural reference
  locating a feature in the output]"

Test: can a reader find the referenced feature using only this text? If YES: proceed.
If NO: rewrite before entering the cell.

ENTRY LOCK: no verdict row may be written until the model cell is written and passes the test.

For each output, produce:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Column rules:
  - Evidence must reference the output's specific content, not restate the criterion.
  - No row may be blank.

After the table:
  essential_pass = [E count; PARTIAL=0.5]
  recommended_pass = [R count; PARTIAL=0.5]
  aspirational_pass = [A count; PARTIAL=0.5]
  composite = (E/5 * 60) + (R/3 * 30) + (A/8 * 10) = [result]
  Golden: YES | NO -- [reason if NO]

Score all N outputs.

PHASE 2 COMPLETE

---

PHASE 3: VERIFY AND REGRESSION

**3a. Arithmetic verification**

For one output, recompute composite from stated counts:
  Verification (output: [ID]):
    Stated: E=[X]/5, R=[X]/3, A=[X]/8
    Computed: ([X]/5*60) + ([X]/3*30) + ([X]/8*10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

The binary declaration field is required. Narrative equivalents do not satisfy C-12.

**3b. Symmetric regression section**

If prior-round data provided:
  For each regression (PASS or PARTIAL -> lower verdict):
    [Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]
  Both prior and current verdicts are required for each entry.

If no prior-round data:
  "No prior round data -- regression analysis cannot be performed."

PHASE 3 COMPLETE

---

SYNTHESIS

Produce the following in order after Phase 3.

**LEADERBOARD**: ranked table by composite descending, ties noted.

**EXCELLENCE SIGNALS**: output-criterion pairs where one output clearly leads, with structural
explanation of the mechanism producing the outlier score. "Scored highest overall" is not
a signal -- name the criterion and the mechanism.

**FAILURE PATTERNS**: criteria receiving no PASS across all outputs. Required section even when
empty: "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES**: one paragraph per output explaining structural drivers, not
verdict count lists.

---

## V-03: Axis L -- Symmetry Audit Sweep

**Variation axis**: Phrasing register -- imperative "write both sides" language at every
delta-comparison instruction, plus a SYMMETRY AUDIT SWEEP table at Phase 1 exit that explicitly
checks each comparison for bilateral completeness before Phase 2 begins.

**Hypothesis**: Conversational imperative phrasing ("write both: old value -> new value")
lowers cognitive overhead at the moment of writing, reducing one-sided comparisons that
occur not from structural absence but from drafting momentum. The SYMMETRY AUDIT SWEEP at
Phase 1 exit is a post-write catch mechanism -- analogous to Axis E's role for arithmetic
(a required YES/NO field that makes silent errors visible). Together, L produces C-15 PASS
through two orthogonal mechanisms: upfront instruction (prevents) and sweep check (catches),
without requiring a structural table format change.

---

You are running quest-score against the v4 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- v4 DENOMINATOR UPDATE

N_aspirational changed. Write both values where the formula appears:

  N_aspirational: 6 (v3 rubric) -> 8 (v4 rubric, now active)

Every time you write a formula or score breakdown, write both sides:
  OLD: aspirational_pass / 6 * 10  [no longer valid]
  NEW: aspirational_pass / 8 * 10  [v4 active formula]

If you catch yourself writing only "N_aspirational=8" without "was 6", stop and add the
prior value. Both sides, every time.

Full formula (v4):
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 8 * 10)
  PARTIAL = 0.5, FAIL = 0. Golden: ALL 5 essentials PASS AND composite >= 80.

---

PHASE 1: LOAD

**Step 1: Load summary**

Write a block that lists:
  - All criteria IDs with their tier (essential/recommended/aspirational) -- write all 16
  - The composite formula exactly as above
  - The golden threshold condition
  - How many outputs you are about to score and which ones

**Step 2: Formula version delta**

Write this sentence out loud in your output:
  "N_aspirational changed from 6 (v3) to 8 (v4). Old denominator is retired."

Both values, both versions. If you cannot confirm the prior version, write:
  "Prior version not confirmed -- scoring under v4 as baseline."

**Step 3: SYMMETRY AUDIT SWEEP (Phase 1 exit gate)**

Before leaving Phase 1, look at every comparison you have made so far. For each one, ask:
"Did I write both the before value and the after value?"

Write the audit result:

  SYMMETRY AUDIT (Phase 1 exit)
  | Comparison | Before value written? | After value written? | Symmetric? |
  |------------|-----------------------|---------------------|------------|
  | N_aspirational denominator | [YES/NO] | [YES/NO] | [YES/NO] |
  | [any other comparisons made in this phase] | [YES/NO] | [YES/NO] | [YES/NO] |

If any row shows Symmetric? = NO: go back and add the missing side before proceeding.
All rows Symmetric? = YES is the gate condition for leaving Phase 1.

PHASE 1 COMPLETE -- all Phase 1 symmetry checks pass.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL EVIDENCE CELL -- write this first, before any verdict**

Your first evidence cell sets the standard for all the others. Write it as a complete
example:
  Model cell: "from [output ID], [section/structure name]: [exact quote or structural
  observation that would let a reader locate this feature in the output]"

Ask yourself: if someone read only this evidence, could they find the thing I'm describing
in the output? If yes, it's good. If no, it's criterion restatement -- rewrite it.

GATE: do not write any verdict until the model cell above is written and you have answered
"yes" to the locatability question.

For each output, write a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Guidance for evidence cells:
  - Quote a phrase from the output, OR
  - Name a section title + what is in it, OR
  - Describe a structural feature specific to this output
  - Do NOT write: "the output satisfies this criterion" or "the output has [criterion name]"

After each table:
  Breakdown: E=[X]/5, R=[X]/3, A=[X]/8
  Composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]
  Golden: YES | NO -- [reason]

Score all N outputs.

---

PHASE 3: VERIFY

**Arithmetic check**

Pick one output and compute its composite from scratch using the stated verdict counts.

  Re-checking [output ID]:
    E=[X]/5, R=[X]/3, A=[X]/8
    Formula: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]
    Matches stated score: YES | NO -- if NO: stated [X], computed [Y]

Write "YES" or "NO". Do not write "seems correct" or "checks out" -- a binary answer is
required so that errors are visible rather than buried in narrative.

**Regression check**

If you have a prior-round scorecard, look for any output-criterion pair that was better
before and is worse now. Write both sides:
  "[Output ID] / [Criterion ID]: was [old verdict], now [new verdict]"
  Both the old verdict and the new verdict are required -- writing only the current verdict
  means the comparison is half-done.

If no prior scorecard: "No prior round data -- skipping regression."

**SYMMETRY AUDIT SWEEP (Phase 3 exit)**

Before writing SYNTHESIS, run the symmetry sweep again for comparisons added in Phase 3:

  SYMMETRY AUDIT (Phase 3 exit)
  | Comparison | Before value written? | After value written? | Symmetric? |
  |------------|-----------------------|---------------------|------------|
  | Arithmetic discrepancy (if any) | [YES/NO] | [YES/NO] | [YES/NO] |
  | Regression verdicts (if any) | [YES/NO] | [YES/NO] | [YES/NO] |

If any row is not symmetric: fix it before writing SYNTHESIS.

---

SYNTHESIS

**LEADERBOARD**: ranked by composite descending, ties noted.

**EXCELLENCE SIGNALS**: for each criterion where one output leads, name the output, the
criterion, and the specific structural mechanism producing the outlier. No general "scored
highest" statements.

**FAILURE PATTERNS**: criteria with no PASS across all outputs. Write the section even when
empty: "No failure patterns found."

**PER-OUTPUT SYNTHESIS NOTES**: one paragraph per output explaining what structural choices
drove its score. Explain mechanism, not verdict counts.

---

## V-04: Axes J+K -- Symmetric Delta Register + Phase Mechanism Inventory

**Variation axes**: Output format (J: DELTA REGISTER) + Lifecycle emphasis (K: MECHANISM INVENTORY)

**Hypothesis**: J and K target fully independent failure modes. J prevents one-sided
comparisons (C-15) by making the Prior State column structurally required in a Phase 1 table.
K prevents single-phase clustering (C-16) by requiring explicit pre-declaration of mechanisms
at each phase. An output that passes J can still fail K (all mechanisms cluster at Phase 1,
no Phase 2 or Phase 3 mechanisms declared). An output that passes K can still fail J
(mechanisms are distributed across phases, but regression entries write only current verdicts).
Neither criterion can satisfy the other. Combining J+K should produce fully additive gains on
C-15 and C-16 -- the same additivity pattern observed in R3 for G+H on C-13 and C-14.

---

You are running quest-score against the v4 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT

N_aspirational denominator changed from v3 to v4. Write both values in the formula delta block.

  N_aspirational: 6 (v3) -> 8 (v4)

v4 formula (active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden: ALL 5 essentials PASS AND composite >= 80.

Using aspirational_pass / 6 in any computation is a formula version error.

---

MECHANISM INVENTORY (write before Phase 1 -- complete before writing the load summary)

Declare the active enforcement mechanisms you will deploy at each lifecycle phase in this run.

  MECHANISM INVENTORY
  Phase 1 (pre-scoring):
    Active: [list -- at minimum: FORMULA CHANGE ALERT acknowledgment, formula version delta
             block with both prior and current values, load summary with all 4 elements,
             SYMMETRIC DELTA REGISTER filled before scoring]
  Phase 2 (during evidence writing):
    Active: [list -- at minimum: MODEL CELL at Phase 2 entry, ENTRY LOCK on first verdict row]
  Phase 3 (post-scoring):
    Active: [list -- at minimum: arithmetic re-derivation, YES/NO discrepancy declaration,
             regression section with symmetric prior/current entries]

  Phase coverage count: [N of phases with >= 1 active mechanism]

Gate: Phase coverage count must be >= 2. If coverage = 1, add mechanisms to a second phase
before writing the load summary.

MECHANISM INVENTORY WRITTEN -- Phase coverage confirmed >= 2.

---

PHASE 1: LOAD AND SYMMETRIC DELTA REGISTER

Complete all steps in order. Do not advance to Phase 2 until all steps are written.

**1a. Load summary**

Block naming:
  (a) all criteria IDs with tier labels (essential: C-01--C-05; recommended: C-06--C-08;
      aspirational: C-09--C-16)
  (b) exact formula: composite = (E/5*60) + (R/3*30) + (A/8*10)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

Missing any one of (a)--(d) earns C-01 PARTIAL.

**1b. Formula version delta block**

Write in scorer output (required, not just in prompt instructions):
  Formula version delta: N_aspirational changed from 6 (v3) to 8 (v4).

Both sides. Prior value first, current value second. This satisfies C-13's output-side
requirement AND pre-populates the N_aspirational row of the SYMMETRIC DELTA REGISTER.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | 6 (v3) | 8 (v4) |
  | Regression verdict pairs | [prior verdict for each regressed pair, or "No prior-round data -- row N/A"] | [current verdict, or "--"] |
  | Arithmetic discrepancy | [stated composite if discrepancy found, or "No discrepancy -- row N/A"] | [computed composite if discrepancy found, or "--"] |

Register rules:
  - Prior State column must be filled for every row. A blank Prior State cell is a structural
    gap equivalent to a blank evidence cell -- detectable by column scan without reading content.
  - "No prior-round data -- row N/A" is the correct Prior State entry when prior data is
    unavailable. This earns PARTIAL on C-15 for that row, not FAIL.
  - Add rows as additional delta comparisons are encountered during scoring.

SYMMETRIC DELTA REGISTER COMPLETE

PHASE 1 COMPLETE

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- fires before any verdict row)**

Write as the first action of Phase 2:
  MODEL CELL: Evidence (example): "from [output ID], [section or structural element]:
  [verbatim excerpt or structural observation that lets a reader locate this feature in
  the output]"

Locatability test: can a reader find the referenced feature using only this evidence text?
If YES: proceed. If NO: rewrite.

ENTRY LOCK: no verdict row may appear until the MODEL CELL above is written and passes the
locatability test. This lock is the Phase 2 enforcement mechanism.

For each output, produce:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Evidence rules:
  - Must reference specific content in the scored output (quote, section name, structural
    observation).
  - Must NOT restate the criterion label ("the output has a leaderboard" is criterion
    restatement, not evidence).

After each table:
  E=[X]/5, R=[X]/3, A=[X]/8
  composite = ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]
  Golden: YES | NO -- [reason if NO]

Score all N outputs.

PHASE 2 COMPLETE

---

PHASE 3: VERIFY

**3a. Arithmetic re-derivation**

For one output:
  Verification ([output ID]):
    Stated: E=[X]/5, R=[X]/3, A=[X]/8
    Recomputed: ([X]/5*60) + ([X]/3*30) + ([X]/8*10) = [value]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

Binary declaration required. Update the SYMMETRIC DELTA REGISTER Arithmetic row if a
discrepancy is found.

**3b. Regression section with symmetric verdicts**

If prior-round scorecard provided:
  For each regression: [Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]
  Update the SYMMETRIC DELTA REGISTER Regression row with the prior and current verdicts.
  A regression entry that names only the current verdict is a C-15 violation -- add the
  prior verdict.

If no prior-round data:
  "No prior round data -- regression analysis cannot be performed."
  The SYMMETRIC DELTA REGISTER Regression row already contains "No prior-round data -- row N/A."

PHASE 3 COMPLETE

---

SYNTHESIS

**LEADERBOARD**: all outputs ranked by composite descending. Ties noted explicitly.

**EXCELLENCE SIGNALS**: output-criterion pairs where one output leads the field. Structural
explanation required (name the design property, not the criterion label).

**FAILURE PATTERNS**: criteria with no PASS across all outputs. Required even when empty.

**PER-OUTPUT SYNTHESIS NOTES**: one paragraph per output on structural score drivers.

---

## V-05: Axes J+K+M -- Full Integration with Inertia Baseline

**Variation axes**: Output format (J: DELTA REGISTER) + Lifecycle emphasis (K: MECHANISM INVENTORY) + Inertia framing (M: explicit naming of the bare-scorecard baseline as the structural competitor)

**Hypothesis**: V-04 carries J+K for additive C-15+C-16 gains. The additional inertia framing
axis (M) tests whether naming the bare-scorecard baseline explicitly at each phase raises the
motivation and precision of each enforcement mechanism. The hypothesis is that framing each
structural choice as a deliberate departure from inertia -- rather than a compliance obligation
-- produces higher-quality evidence cells and more complete phase coverage, because each
mechanism has a concrete negative foil. The inertia baseline also makes C-15/C-16 failures
structurally visible at the moment of writing: a scorer who names the inertia pattern ("inertia:
writes only current value") cannot then write only the current value without consciously
violating the framing. This variation should reach or exceed the v4 ceiling.

---

You are running quest-score against the v4 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

INERTIA BASELINE DECLARATION

Before any enforcement mechanism fires, name what the default (inertia) scoring behavior
produces. This is the baseline you are deliberately departing from at each phase.

  INERTIA SCORECARD (what the bare minimum produces):
  - Phase 1: no load summary or formula check; scoring begins immediately without declaring
    criteria, formula, or delta; N_aspirational written as current value only (no prior)
  - Phase 2: evidence cells restate criterion labels; no model cell; verdicts written before
    any evidence standard is established; anchor deferred to Phase 3 or absent
  - Phase 3: no arithmetic check; no discrepancy declaration; regression entries write current
    verdict only (no prior verdict); or regression section omitted entirely
  - Inertia C-15 failure mode: every comparison names only the current-state value
  - Inertia C-16 failure mode: all mechanisms cluster at Phase 3 (or absent), Phases 1+2 unguarded

  Scoring cost of inertia: C-01 FAIL, C-03 PARTIAL/FAIL, C-05 FAIL (if absent),
    C-09 FAIL, C-10 PARTIAL, C-11 FAIL, C-12 FAIL, C-13 FAIL, C-15 FAIL, C-16 FAIL

Every enforcement mechanism you deploy below is an explicit departure from this baseline.

---

FORMULA CHANGE ALERT -- DEPARTURE FROM INERTIA (silent formula carry-over)

Inertia failure mode: scorer applies v3 denominator (aspirational_pass / 6) silently.
Departure: write both values before any computation.

  N_aspirational: 6 (v3) -> 8 (v4)

v4 formula (active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden: ALL 5 essentials PASS AND composite >= 80.

---

MECHANISM INVENTORY -- DEPARTURE FROM INERTIA (single-phase clustering)

Inertia failure mode: all mechanisms at Phase 3, or absent. Phases 1 and 2 unguarded.
Departure: declare mechanisms at 2+ distinct phases before writing the load summary.

  MECHANISM INVENTORY
  Phase 1 (pre-scoring -- inertia leaves this unguarded):
    Deployed: [list -- at minimum: formula version delta block naming prior AND current values,
               load summary with all 4 elements, SYMMETRIC DELTA REGISTER pre-populated]
    Inertia failure prevented: [name it -- e.g., formula version carry-over, missing load
                                 verification, one-sided N_aspirational annotation]

  Phase 2 (during evidence writing -- inertia has restatement and deferred anchor here):
    Deployed: [list -- at minimum: MODEL CELL at Phase 2 entry, ENTRY LOCK on first verdict row]
    Inertia failure prevented: [name it -- e.g., evidence restatement, anchor deferred past
                                 first three cells]

  Phase 3 (post-scoring):
    Deployed: [list -- at minimum: arithmetic re-derivation, YES/NO discrepancy declaration,
               regression section with symmetric prior/current verdicts]
    Inertia failure prevented: [name it -- e.g., silent arithmetic errors, one-sided
                                 regression entries, missing regression section]

  Phase coverage: [N phases with >= 1 mechanism]

Gate: Phase coverage >= 2. If coverage = 1, identify which phase is unguarded and add
mechanisms before proceeding.

MECHANISM INVENTORY WRITTEN

---

PHASE 1: LOAD AND SYMMETRIC DELTA REGISTER

*Inertia failure modes addressed at this phase: no load summary, no delta declared, N_aspirational
named as current value only (prior value absent).*

**1a. Load summary**

Four required elements (inertia omits all):
  (a) all criteria IDs with tier labels: C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-16 aspirational
  (b) exact formula: composite = (E/5*60) + (R/3*30) + (A/8*10)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

Any missing element earns C-01 PARTIAL.

**1b. Formula version delta block**

*Departure from inertia (current value only -> both values):*

Write in output (visible to reader, not only in prompt):
  Formula version delta: N_aspirational changed from 6 (v3) to 8 (v4).

Both sides required. Inertia would write only "N_aspirational=8" without the prior.
Satisfies C-13 output-side requirement AND pre-populates the N_aspirational row in the
SYMMETRIC DELTA REGISTER.

**1c. SYMMETRIC DELTA REGISTER**

*Departure from inertia (one-sided comparisons -> both-sided table with structural enforcement):*

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | 6 (v3) | 8 (v4) |
  | Regression verdict pairs | [prior verdicts, or "No prior-round data -- row N/A"] | [current verdicts, or "--"] |
  | Arithmetic discrepancy | [stated composite if discrepancy found, or "No discrepancy -- row N/A"] | [computed composite if discrepancy found, or "--"] |

Register rules:
  - Blank Prior State cell: structural violation (inertia: "N_aspirational=8" without prior).
    Write the value or write "N/A -- [reason]." Blank = detected by column scan, same as
    blank evidence cell.
  - Regression and discrepancy rows may be filled during Phase 3 -- return and update the
    register rather than writing them only in Phase 3 prose. The register is the single
    source of truth for symmetric comparisons.
  - Add rows for each new delta comparison encountered.

PHASE 1 COMPLETE

---

PHASE 2: SCORE EACH OUTPUT

*Inertia failure modes addressed at this phase: evidence restatement, model cell absent or
deferred, anchor fires after evidence pattern is established.*

**MODEL CELL -- Phase 2 entry gate**

*Departure from inertia (no model cell, or model cell mid-Phase-2 or later):*

Write as the very first action of Phase 2, before any verdict row:
  MODEL CELL: "from [output ID], [section or structural element]: [verbatim quote or structural
  observation sufficient for a reader to locate this feature in the output]"

Locatability test: can a reader find the referenced feature using only this evidence text?
YES: proceed. NO: rewrite until YES.

ENTRY LOCK: prevents the inertia pattern (verdicts written before evidence standard is set).
No verdict row may appear above the MODEL CELL in Phase 2.

For each output:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Evidence standard (departure from inertia restatement):
  - ACCEPTABLE: verbatim quote, named section + what is in it, structural observation specific
    to this output
  - INERTIA (NOT acceptable): "the output has [criterion name]", "this criterion is met",
    "the output provides a leaderboard" without naming what the leaderboard contains or how
    it is structured

After each table:
  E=[X]/5, R=[X]/3, A=[X]/8
  composite = ([X]/5 * 60) + ([X]/3 * 30) + ([X]/8 * 10) = [result]
  Golden: YES | NO -- [reason if NO]

Score all N outputs.

PHASE 2 COMPLETE

---

PHASE 3: VERIFY AND REGRESSION

*Inertia failure modes addressed at this phase: silent arithmetic errors, one-sided regression
entries, regression section absent.*

**3a. Arithmetic re-derivation**

*Departure from inertia (no check, or narrative "seems correct"):*

  Verification ([output ID]):
    Stated: E=[X]/5, R=[X]/3, A=[X]/8
    Recomputed: ([X]/5*60) + ([X]/3*30) + ([X]/8*10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

Binary YES/NO required. Inertia would write "verification performed" without a named result.
Update SYMMETRIC DELTA REGISTER Arithmetic row if discrepancy found.

**3b. Symmetric regression section**

*Departure from inertia (only current verdict written, or section absent):*

If prior-round scorecard provided:
  [Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]
  Both verdicts required. Update SYMMETRIC DELTA REGISTER Regression row.
  Inertia pattern to avoid: "[Output ID] / [Criterion ID]: current=[verdict]" with no prior.

If no prior-round data:
  "No prior round data -- regression analysis cannot be performed."

Do not omit this section. Absent section = C-09 FAIL (inertia default).

PHASE 3 COMPLETE

---

SYNTHESIS

*Inertia failure modes addressed: synthesis section absent, or lists verdict counts without
structural explanation.*

**LEADERBOARD**: all outputs ranked by composite descending. Ties noted explicitly.
*Inertia: pointer to scores above. Departure: distinct ranked structure with all outputs present.*

**EXCELLENCE SIGNALS**: output-criterion pairs where structural choices produced outlier scores.
Format: [Output ID] -- [Criterion ID] -- [structural mechanism causing the difference].
*Inertia: "V-X scored highest overall." Departure: specific output-criterion-mechanism triple.*

**FAILURE PATTERNS**: criteria with no PASS across all outputs. Required even when empty.
*Inertia: section omitted when no patterns exist. Departure: explicit empty-section statement.*

**PER-OUTPUT SYNTHESIS NOTES**: one paragraph per output on structural score drivers.
*Inertia: "V-X scored E=5/5, R=2/3, A=4/8." Departure: explanation of mechanism, not counts.*
