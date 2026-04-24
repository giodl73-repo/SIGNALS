Now I have full context on what the quest-rubric skill produces and the v12 rubric's structural requirements (C-29 AUDITOR-PRE, C-30 dual-column PARTIAL-CREDIT MANIFEST, C-31 structural redundancy guard, C-32 MANIFEST-ROW VERIFICATION, plus C-23–C-26 from R7). Writing the five complete variations:

---

# quest-rubric Variate — v12, Round 12

**Date:** 2026-03-16
**Rubric:** v12 (C-01–C-32; denominator /27)
**Variation axes selected:**
- V-01: Role sequence (AUDITOR leads, pre-spec gate)
- V-02: Output format (table-centric criteria)
- V-03: Phrasing register (direct imperative, minimal explanation)
- V-04: Combined — Lifecycle emphasis + Inertia framing
- V-05: Combined — Role sequence + Output format + Phrasing register

---

## V-01 — Role Sequence: AUDITOR leads, construction gate closes before spec is read

**Variation axis:** Role order. AUDITOR runs Phase 0 before SPEC ANALYST reads anything. The construction gate and formula structure are declared while the skill spec is still unread.

**Hypothesis:** Pre-spec gate closure makes C-29 compliance structurally mandatory rather than a discipline requirement. When the formula must be written before spec content is available, retroactive AUDITOR-PRE insertion becomes impossible by construction — the AI cannot "discover" the formula needs from the spec and then back-fill the declaration.

---

```
# quest-rubric

You are producing a scoring rubric for the skill described in the input. This rubric
is the objective function for quest-golden: it defines exactly what a passing output
looks like and gives evaluators unambiguous tests.

---

## Phase 0 — AUDITOR: Construction Gate (pre-spec)

Before reading the skill spec, write the AUDITOR-PRE block. This block locks the
formula structure, weight classes, and scoring tiers that govern every criterion
you will write. The construction gate closes on AUDITOR-PRE: CLOSED. No criterion
may be written until the gate is closed.

AUDITOR-PRE: OPEN
  weight_classes: essential | recommended | aspirational
  formula: (E/[N_e] * 60) + (R/[N_r] * 30) + (A/[N_a] * 10)
  essential_behavior: binary pass/fail; a single essential FAIL floors the score
    regardless of recommended and aspirational performance
  recommended_partial: PARTIAL = 0.5 on any recommended criterion; requires
    per-criterion PARTIAL-CONDITION block
  aspirational_partial: PARTIAL = 0.5 on any aspirational criterion; requires
    per-criterion PARTIAL-CONDITION block
  manifest_column_structure: "Criterion ID | Partial boundary | Pass condition"
  note: N_e, N_r, N_a are placeholders; fill denominators after criteria are counted;
    formula structure is fixed now and must be reproduced verbatim at every subsequent
    structural position where a formula appears
AUDITOR-PRE: CLOSED

Gate closed. Proceed to Phase 1.

---

## Phase 1 — PRE-DECLARATION REGISTER

Before writing any criterion, list every criterion you anticipate in the register.
This is the batch enforcement position. Inline AUDITOR-PRE blocks per criterion
(Phase 2) are the second enforcement position. Both positions must be active.

PRE-DECLARATION REGISTER: OPEN
  | ID   | Weight      | Short name (anticipated) |
  |------|-------------|--------------------------|
  | C-01 | essential   | [name — TBD until spec read] |
  | ...  | ...         | ... |
  [Complete after reading spec in Phase 2. Return here and fill names.]
PRE-DECLARATION REGISTER: CLOSED

Proceed to Phase 2.

---

## Phase 2 — SPEC ANALYST: Read and Extract

Read the skill spec. Produce SA-1:

SA-1: OPEN
  skill_name: [name]
  non_negotiables:
    - [each is an essential criterion candidate]
  excellence_signals:
    - [each is an aspirational criterion candidate]
  partial_credit_surfaces:
    - [each is a PARTIAL-CONDITION candidate]
  formula: [reproduce AUDITOR-PRE formula verbatim — do not collapse to binary counting]
SA-1: CLOSED

Return to the PRE-DECLARATION REGISTER and fill criterion names. Then proceed.

---

## Phase 3 — VERDICT TIER DECLARATION

VERDICT TIER: OPEN
  PASS:    score >= 70 AND all essential criteria pass
  PARTIAL: score 50-69 AND all essential criteria pass
  FAIL:    any essential criterion fails OR score < 50
VERDICT TIER: CLOSED

---

## Phase 4 — AUTHOR: Write Criteria

Write criteria in order: essential first, then recommended, then aspirational.

For each criterion, write an inline AUDITOR-PRE block immediately before the
criterion body. This is the second enforcement position (the PRE-DECLARATION
REGISTER is the first). Both positions must be active simultaneously.

  AUDITOR-PRE: C-NN
    weight: essential | recommended | aspirational
    partial_applies: yes | no
  AUDITOR-PRE: C-NN CLOSED

  C-NN — [short name]
  Weight: essential | recommended | aspirational
  Category: correctness | depth | format | coverage | behavior
  Text: [one falsifiable statement]
  Pass condition: [exact evidence required to pass]
  PARTIAL-CONDITION: [exact evidence earning 0.5; required for recommended and
    aspirational; omit for essential]

Essential criteria must cover at minimum:
  - Structural completeness (all required sections present)
  - Formula correctness at every structural position (anti-collapse)
  - Criteria falsifiability (each criterion has a testable pass condition)

---

## Phase 5 — PARTIAL-CREDIT MANIFEST + MANIFEST-ROW VERIFICATION

After all criteria are written, produce the manifest:

PARTIAL-CREDIT MANIFEST: OPEN
  | Criterion ID | Partial boundary | Pass condition |
  |--------------|-----------------|----------------|
  [one row per recommended and aspirational criterion;
   both columns required — manifest with only one column fails C-30]
PARTIAL-CREDIT MANIFEST: CLOSED

Immediately run verification:

MANIFEST-ROW VERIFICATION: OPEN
  For each manifest row:
  (a) Confirm "Partial boundary" reproduces the PARTIAL-CONDITION from the
      criterion body verbatim — no paraphrase
  (b) Confirm "Pass condition" reproduces the Pass condition from the criterion
      body verbatim — no paraphrase
  (c) Log any incoherence as REGISTER REVISION: [ID] and correct before closing
MANIFEST-ROW VERIFICATION: CLOSED

---

## Phase 6 — FINAL RUBRIC

FINAL RUBRIC: OPEN
  [All criteria C-01 through C-NN, in order, full text]

  Formula: (E/{N_e} * 60) + (R/{N_r} * 30) + (A/{N_a} * 10)
  [Reproduce verbatim — do not collapse to binary counting]

  | Score   | Verdict | Condition                         |
  |---------|---------|-----------------------------------|
  | >= 70   | PASS    | all essential pass                |
  | 50-69   | PARTIAL | all essential pass                |
  | < 50    | FAIL    | —                                 |
  | any essential fail | FAIL | regardless of score        |
FINAL RUBRIC: CLOSED

---

## Input

**Skill spec:**
{{SKILL_SPEC}}

**Sample outputs (calibrate non-negotiables, excellence signals, partial surfaces):**
{{SAMPLE_OUTPUTS}}
```

---

## V-02 — Output Format: Table-centric criteria, manifest as view filter

**Variation axis:** Output format. Criteria rendered as table rows (columns: ID, Weight, Category, Text, Pass condition, Partial condition). The PARTIAL-CREDIT MANIFEST becomes a filtered view of this same table restricted to non-essential rows, automatically satisfying dual-column structure.

**Hypothesis:** A single table structure for all criteria eliminates formula inconsistency (C-24) — the denominator is the row count of the table, forcing one formula at one structural position. The dual-column PARTIAL-CREDIT MANIFEST (C-30) is satisfied as a structural property of the criteria table itself: any output that fills the table fills the manifest.

---

```
# quest-rubric

Produce a scoring rubric for the skill described below. Output format: criteria
as a structured table; the PARTIAL-CREDIT MANIFEST is a filtered view of that table.

---

## Phase 0 — AUDITOR-PRE

Declare the construction gate before reading the skill spec.

AUDITOR-PRE: OPEN
  weight_classes: essential | recommended | aspirational
  formula: (E/[N_e] * 60) + (R/[N_r] * 30) + (A/[N_a] * 10)
  essential_behavior: binary; a single essential FAIL floors the score
  partial_behavior: PARTIAL = 0.5; per-criterion Partial condition column is required
    for every recommended and aspirational row
  manifest_columns: reproduced from criteria table — "ID | Partial condition | Pass condition"
  reproduction_rule: formula reproduced verbatim at SA-1, at FINAL RUBRIC, and at any
    other structural position where a formula appears; do not collapse to binary counting
AUDITOR-PRE: CLOSED

---

## Phase 1 — SPEC ANALYST

Read the skill spec. Produce SA-1:

SA-1: OPEN
  skill_name:
  non_negotiables: [list]
  excellence_signals: [list]
  partial_credit_surfaces: [list]
  formula: [reproduce AUDITOR-PRE formula verbatim — do not collapse to binary counting]
SA-1: CLOSED

---

## Phase 2 — VERDICT TIER DECLARATION

VERDICT TIER: OPEN
  PASS:    score >= 70 AND all essential pass
  PARTIAL: score 50-69 AND all essential pass
  FAIL:    any essential fails OR score < 50
VERDICT TIER: CLOSED

---

## Phase 3 — AUTHOR: Criteria Table

Write all criteria as rows in one Markdown table with these exact columns:

| ID | Weight | Category | Text | Pass condition | Partial condition |
|----|--------|----------|------|----------------|-------------------|

Column definitions:
- **ID**: C-01, C-02, ... (sequential, no gaps)
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Text**: one falsifiable statement of what the criterion tests; must be checkable
  by an evaluator who has not authored the rubric
- **Pass condition**: exact evidence required for a PASS verdict
- **Partial condition**: exact evidence earning a PARTIAL (0.5) verdict;
  required for recommended and aspirational rows; write "n/a — binary" for essential rows

Write essential rows first (3-5 rows), then recommended (2-4 rows), then aspirational.

Essential rows must cover:
  - All required structural sections present
  - Formula anti-collapse (weighted formula present at all structural positions)
  - Every criterion has a testable pass condition (no vague tests)

---

## Phase 4 — PRE-DECLARATION REGISTER + Inline AUDITOR-PRE Blocks

Both enforcement positions must be active simultaneously (structural redundancy).

**Enforcement position 1 — PRE-DECLARATION REGISTER (batch):**

PRE-DECLARATION REGISTER: OPEN
  | ID   | Weight      | Short name |
  |------|-------------|------------|
  [one row per criterion in the table above — names match table Text column summary]
PRE-DECLARATION REGISTER: CLOSED

**Enforcement position 2 — inline AUDITOR-PRE per criterion:**

For each criterion in the table, write a one-line inline block:
  AUDITOR-PRE: C-NN | weight: [w] | partial_applies: yes/no | CLOSED

Write all inline blocks as a compact list here (not interleaved with the table):
  [list of inline AUDITOR-PRE lines]

---

## Phase 5 — PARTIAL-CREDIT MANIFEST

The manifest is a view filter over the criteria table restricted to non-essential rows.
Both columns are required. Missing one column fails the dual-column requirement.

PARTIAL-CREDIT MANIFEST: OPEN
  | ID   | Partial condition (from table — verbatim) | Pass condition (from table — verbatim) |
  |------|------------------------------------------|----------------------------------------|
  [one row per recommended and aspirational criterion]
PARTIAL-CREDIT MANIFEST: CLOSED

MANIFEST-ROW VERIFICATION: OPEN
  Confirm each manifest row reproduces the table cell text verbatim.
  Log REGISTER REVISION: [ID] for any cell that diverges; correct before closing.
MANIFEST-ROW VERIFICATION: CLOSED

---

## Phase 6 — FINAL RUBRIC

FINAL RUBRIC: OPEN
  [Reproduce the criteria table verbatim]

  Formula: (E/{N_e} * 60) + (R/{N_r} * 30) + (A/{N_a} * 10)
  [Reproduce verbatim — do not collapse to binary counting]
  N_e = [count of essential rows]; N_r = [count of recommended rows];
  N_a = [count of aspirational rows]
FINAL RUBRIC: CLOSED

---

## Input

**Skill spec:**
{{SKILL_SPEC}}

**Sample outputs:**
{{SAMPLE_OUTPUTS}}
```

---

## V-03 — Phrasing Register: Direct imperative, minimal explanation

**Variation axis:** Phrasing register. Every instruction is a bare imperative. No explanatory prose around why a step exists. No hedging. One action per sentence.

**Hypothesis:** Imperative phrasing eliminates evaluator variance on binary essential criteria. "Write the AUDITOR-PRE block" leaves no room for an output that omits it to claim partial compliance. The total prompt length is shorter, reducing the surface area for confusion about which requirements are structural vs advisory.

---

```
# quest-rubric

Produce a scoring rubric for the skill spec below.

---

## Step 1: AUDITOR-PRE

Write this block before reading the skill spec.

AUDITOR-PRE: OPEN
  weight_classes: essential | recommended | aspirational
  formula: (E/[N_e] * 60) + (R/[N_r] * 30) + (A/[N_a] * 10)
  essential: binary pass/fail; one fail floors the score
  recommended/aspirational: PARTIAL = 0.5; each criterion needs a PARTIAL-CONDITION
  manifest: two columns required — "Partial boundary" and "Pass condition"
  reproduction: reproduce this formula verbatim wherever a formula appears; never collapse
AUDITOR-PRE: CLOSED

---

## Step 2: PRE-DECLARATION REGISTER

List every criterion you will write.

PRE-DECLARATION REGISTER: OPEN
  | ID   | Weight      | Short name |
  [fill after reading spec — return here]
PRE-DECLARATION REGISTER: CLOSED

---

## Step 3: Read the spec. Produce SA-1.

SA-1: OPEN
  skill_name:
  non_negotiables:
  excellence_signals:
  partial_credit_surfaces:
  formula: [AUDITOR-PRE formula verbatim — do not collapse]
SA-1: CLOSED

Fill the PRE-DECLARATION REGISTER now.

---

## Step 4: VERDICT TIER DECLARATION

VERDICT TIER: OPEN
  PASS:    >= 70 AND all essential pass
  PARTIAL: 50-69 AND all essential pass
  FAIL:    any essential fails OR < 50
VERDICT TIER: CLOSED

---

## Step 5: Write each criterion.

For each criterion, write an inline AUDITOR-PRE block first, then the criterion body.

  AUDITOR-PRE: C-NN | weight: [w] | partial: yes/no | CLOSED

  C-NN — [short name]
  Weight: [w]
  Category: [c]
  Text: [one falsifiable statement]
  Pass condition: [exact evidence for PASS]
  PARTIAL-CONDITION: [exact evidence for 0.5; omit for essential]

Write essential first (3-5). Then recommended. Then aspirational.

Essential must cover: structural completeness, formula anti-collapse, criteria falsifiability.

---

## Step 6: PARTIAL-CREDIT MANIFEST

PARTIAL-CREDIT MANIFEST: OPEN
  | Criterion ID | Partial boundary | Pass condition |
  [one row per recommended/aspirational criterion; both columns required]
PARTIAL-CREDIT MANIFEST: CLOSED

---

## Step 7: MANIFEST-ROW VERIFICATION

MANIFEST-ROW VERIFICATION: OPEN
  Check each row:
  - "Partial boundary" = PARTIAL-CONDITION text verbatim
  - "Pass condition" = Pass condition text verbatim
  Log REGISTER REVISION: [ID] for any divergence. Correct. Then close.
MANIFEST-ROW VERIFICATION: CLOSED

---

## Step 8: FINAL RUBRIC

FINAL RUBRIC: OPEN
  [All criteria, full text, in order]
  Formula: (E/{N_e} * 60) + (R/{N_r} * 30) + (A/{N_a} * 10)
  [Reproduce verbatim. Do not collapse to binary counting.]
  | Score | Verdict | Condition |
  | >= 70 | PASS    | all essential pass |
  | 50-69 | PARTIAL | all essential pass |
  | < 50  | FAIL    | — |
  | essential fail | FAIL | regardless of score |
FINAL RUBRIC: CLOSED

---

## Input

**Skill spec:**
{{SKILL_SPEC}}

**Sample outputs:**
{{SAMPLE_OUTPUTS}}
```

---

## V-04 — Combined: Lifecycle emphasis + Inertia framing

**Variation axis (combined):** (1) Phase gates are heavily foregrounded with explicit OPEN/CLOSED tokens at every transition, and phase exit conditions are named explicitly. (2) The status-quo competitor — an ad-hoc prose rubric written without construction gates, formula constraints, or manifest — is named at the opening and used as a contrast anchor throughout.

**Hypothesis:** Naming the prose-rubric inertia competitor sets a minimum quality floor that evaluators can apply mechanically ("would a prose rubric do this?"), grounding criteria that are otherwise abstract. Explicit phase exit conditions make C-31 (both enforcement positions simultaneously active) machine-detectable: each phase's CLOSED token can be checked for required fields before the next phase opens.

---

```
# quest-rubric

You are producing a scoring rubric for the skill described below.

## Why this skill exists

The alternative to running quest-rubric is a prose rubric: a list of bullet points
describing what good output looks like, written informally, with no formula,
no enforcement structure, and no partial-credit semantics. Prose rubrics produce
inconsistent scores across evaluators — two reviewers reading the same output reach
different verdicts because the criteria are ambiguous. quest-rubric eliminates this by
requiring that every criterion be falsifiable, that partial credit be explicitly bounded,
and that the formula be reproduced verbatim wherever it appears.

Every structural element below exists because a prose rubric omits it.

---

## PHASE 0 — CONSTRUCTION GATE
**Exit condition:** AUDITOR-PRE: CLOSED written. Formula structure locked.
**Inertia contrast:** A prose rubric has no construction gate. Formula can be introduced
  at any point, or not at all.

Write the AUDITOR-PRE block before reading the skill spec. The formula structure and
boundary declarations below must exist before any spec content is available.

AUDITOR-PRE: OPEN
  weight_classes: essential | recommended | aspirational
  formula: (E/[N_e] * 60) + (R/[N_r] * 30) + (A/[N_a] * 10)
  essential_behavior:
    - binary pass/fail
    - a single FAIL floors the score regardless of R and A components
    - no PARTIAL-CONDITION applies
  recommended_behavior:
    - PARTIAL = 0.5
    - per-criterion PARTIAL-CONDITION block required; absence makes partial credit
      subjective, reverting to prose-rubric behavior
  aspirational_behavior:
    - PARTIAL = 0.5
    - per-criterion PARTIAL-CONDITION block required; same reason
  manifest_structure:
    - two columns required: "Partial boundary" AND "Pass condition"
    - single-column manifest collapses the boundary/condition distinction,
      reintroducing the ambiguity a prose rubric carries
  reproduction_rule:
    - formula reproduced verbatim at SA-1 and FINAL RUBRIC
    - do not collapse to binary counting at any structural position
AUDITOR-PRE: CLOSED

Phase 0 exit confirmed: construction gate closed.

---

## PHASE 1 — BATCH PRE-DECLARATION
**Exit condition:** PRE-DECLARATION REGISTER: CLOSED with all anticipated criteria listed.
**Inertia contrast:** A prose rubric has no register. Criteria are added, removed, or
  reordered without tracking, so evaluators cannot verify the set is complete.

PRE-DECLARATION REGISTER: OPEN
  [List every criterion you anticipate, with ID, weight, and short name.
   Complete after reading spec. Return here and fill names.]
  | ID   | Weight      | Short name |
  |------|-------------|------------|
PRE-DECLARATION REGISTER: CLOSED

Phase 1 exit confirmed: register closed.

---

## PHASE 2 — SPEC ANALYSIS
**Exit condition:** SA-1: CLOSED.
**Inertia contrast:** A prose rubric skips formal spec analysis. Criteria reflect
  the author's memory of the skill, not the spec's actual non-negotiables.

Read the skill spec. Produce SA-1:

SA-1: OPEN
  skill_name:
  non_negotiables:
    - [each is a candidate essential criterion; a prose rubric conflates these with
       nice-to-haves because there is no essential tier]
  excellence_signals:
    - [each is a candidate aspirational criterion; a prose rubric has no aspirational
       tier; these patterns are invisible]
  partial_credit_surfaces:
    - [each informs a PARTIAL-CONDITION; a prose rubric has no partial-credit semantics]
  formula: [reproduce AUDITOR-PRE formula verbatim; do not collapse to binary counting]
SA-1: CLOSED

Return to PRE-DECLARATION REGISTER. Fill criterion short names.

Phase 2 exit confirmed: SA-1 closed, register updated.

---

## PHASE 3 — VERDICT TIER DECLARATION
**Exit condition:** VERDICT TIER: CLOSED.
**Inertia contrast:** A prose rubric has no explicit PASS/FAIL threshold. Evaluators
  set their own bars, producing inconsistent verdicts.

VERDICT TIER: OPEN
  PASS:    score >= 70 AND all essential criteria pass
  PARTIAL: score 50-69 AND all essential criteria pass
  FAIL:    any essential criterion fails OR score < 50
VERDICT TIER: CLOSED

Phase 3 exit confirmed: verdict tiers declared.

---

## PHASE 4 — CRITERION AUTHORING
**Exit condition:** All criteria written with inline AUDITOR-PRE blocks.
**Structural redundancy:** Both enforcement positions (PRE-DECLARATION REGISTER and
  inline AUDITOR-PRE blocks) must be active simultaneously. The register is the batch
  position; the inline block is the per-criterion position. One without the other is
  a partial enforcement structure — closer to a prose rubric than a full rubric.
**Inertia contrast:** A prose rubric has no per-criterion enforcement. A criterion
  added at the end is indistinguishable from one present from the start.

For each criterion:

  AUDITOR-PRE: C-NN
    weight: essential | recommended | aspirational
    partial_applies: yes | no
    inertia_contrast: [one sentence naming what a prose rubric would omit or obscure
      that this criterion makes explicit]
  AUDITOR-PRE: C-NN CLOSED

  C-NN — [short name]
  Weight: essential | recommended | aspirational
  Category: correctness | depth | format | coverage | behavior
  Text: [one falsifiable statement — checkable without authoring context]
  Pass condition: [exact evidence required for PASS]
  PARTIAL-CONDITION: [exact evidence earning 0.5; required for non-essential;
    absence reverts partial-credit evaluation to prose-rubric subjectivity]

Essential criteria (3-5):
  Cover the prose-rubric failure modes: missing structure, collapsed formula,
  untestable criterion text.

Recommended criteria (2-4):
  Cover behaviors visible in well-formed outputs but not in minimal outputs.

Aspirational criteria:
  Cover excellence patterns from sample outputs.

Phase 4 exit confirmed: all criteria written with inline AUDITOR-PRE blocks.

---

## PHASE 5 — PARTIAL-CREDIT MANIFEST + VERIFICATION
**Exit condition:** MANIFEST-ROW VERIFICATION: CLOSED with no open REGISTER REVISIONs.
**Inertia contrast:** A prose rubric has no manifest. Partial-credit verdicts rely
  entirely on evaluator judgment, reintroducing the variance prose rubrics produce.

PARTIAL-CREDIT MANIFEST: OPEN
  | Criterion ID | Partial boundary | Pass condition |
  |--------------|-----------------|----------------|
  [one row per recommended and aspirational criterion;
   both columns required — a single-column manifest is a prose-rubric regression]
PARTIAL-CREDIT MANIFEST: CLOSED

MANIFEST-ROW VERIFICATION: OPEN
  For each row, verify:
  (a) "Partial boundary" = PARTIAL-CONDITION text from criterion above — verbatim
  (b) "Pass condition" = Pass condition text from criterion above — verbatim
  (c) Boundary and pass condition are coherent (pass condition is strictly stronger
      than boundary — if boundary == pass condition, one of them is wrong)
  Log REGISTER REVISION: [ID] for any issue. Resolve. Then close.
MANIFEST-ROW VERIFICATION: CLOSED

Phase 5 exit confirmed: manifest verified, no open revisions.

---

## PHASE 6 — FINAL RUBRIC
**Exit condition:** FINAL RUBRIC: CLOSED.
**Inertia contrast:** A prose rubric has no final rubric block. The criteria list
  IS the rubric, with no formula, no threshold table, and no reproducibility guarantee.

FINAL RUBRIC: OPEN
  [All criteria C-01 through C-NN, in order, full text including PARTIAL-CONDITIONs]

  Formula: (E/{N_e} * 60) + (R/{N_r} * 30) + (A/{N_a} * 10)
  [Reproduce verbatim from AUDITOR-PRE — do not collapse to binary counting]
  N_e = [count]; N_r = [count]; N_a = [count]

  | Score           | Verdict | Condition                  |
  |-----------------|---------|----------------------------|
  | >= 70           | PASS    | all essential pass         |
  | 50-69           | PARTIAL | all essential pass         |
  | < 50            | FAIL    | —                          |
  | essential fail  | FAIL    | regardless of score        |
FINAL RUBRIC: CLOSED

Phase 6 exit confirmed: final rubric closed.

---

## Input

**Skill spec:**
{{SKILL_SPEC}}

**Sample outputs (use to calibrate non-negotiables, partial surfaces, and
excellence signals; note where prose rubrics would conflate tiers):**
{{SAMPLE_OUTPUTS}}
```

---

## V-05 — Combined: Role sequence + Output format + Phrasing register

**Variation axis (combined):** (1) AUDITOR leads before SPEC ANALYST (V-01 axis); (2) criteria rendered as table rows (V-02 axis); (3) all instructions as direct imperatives with no explanatory prose (V-03 axis).

**Hypothesis:** The three axes reinforce each other along the same failure path. AUDITOR-first sets the formula before spec content is available; table format makes the denominator an observable row count rather than a claim; imperative phrasing closes the gap between "the prompt says to do X" and "the prompt requires X." Together they eliminate the three most common partial-compliance patterns: retroactive AUDITOR-PRE insertion (C-29), formula drift across positions (C-24), and hedged instructions that an evaluator reads as optional.

---

```
# quest-rubric

Produce a scoring rubric for the skill spec below.

---

## Step 1: AUDITOR-PRE (write before reading spec)

AUDITOR-PRE: OPEN
  weight_classes: essential | recommended | aspirational
  formula: (E/[N_e] * 60) + (R/[N_r] * 30) + (A/[N_a] * 10)
  essential: binary; one fail floors score
  non-essential: PARTIAL = 0.5; Partial condition column required in every non-essential row
  manifest_columns: "Criterion ID | Partial boundary | Pass condition" (both required)
  reproduction: reproduce formula verbatim at SA-1, at FINAL RUBRIC, and at every
    subsequent structural position; never collapse to binary counting
AUDITOR-PRE: CLOSED

---

## Step 2: PRE-DECLARATION REGISTER (batch enforcement position)

Fill after Step 3; return here.

PRE-DECLARATION REGISTER: OPEN
  | ID   | Weight      | Short name |
PRE-DECLARATION REGISTER: CLOSED

---

## Step 3: Read spec. Produce SA-1.

SA-1: OPEN
  skill_name:
  non_negotiables:
  excellence_signals:
  partial_credit_surfaces:
  formula: [AUDITOR-PRE formula — verbatim; do not collapse]
SA-1: CLOSED

Fill PRE-DECLARATION REGISTER. Then continue.

---

## Step 4: VERDICT TIER DECLARATION

VERDICT TIER: OPEN
  PASS:    >= 70, all essential pass
  PARTIAL: 50-69, all essential pass
  FAIL:    essential fails OR < 50
VERDICT TIER: CLOSED

---

## Step 5: Criteria table + inline AUDITOR-PRE blocks

Write inline AUDITOR-PRE blocks as a compact list first (per-criterion enforcement position):

  AUDITOR-PRE: C-01 | weight: essential | partial: no | CLOSED
  AUDITOR-PRE: C-02 | weight: essential | partial: no | CLOSED
  ... (one line per criterion)

Then write the criteria table:

| ID | Weight | Category | Text | Pass condition | Partial condition |
|----|--------|----------|------|----------------|-------------------|

Column rules:
- **Text**: one falsifiable statement; no vague verbs ("consider", "ensure")
- **Pass condition**: exact evidence for PASS; an evaluator must be able to check it
  without authoring context
- **Partial condition**: exact evidence for 0.5; write "n/a — binary" for essential rows
- **Category**: correctness | depth | format | coverage | behavior

Row order: essential rows first (3-5), then recommended, then aspirational.

Essential rows must include at minimum:
  1. A row testing structural completeness of the rubric output
  2. A row testing formula anti-collapse (weighted formula at all structural positions)
  3. A row testing criteria falsifiability (every Pass condition is checkable)

---

## Step 6: PARTIAL-CREDIT MANIFEST

PARTIAL-CREDIT MANIFEST: OPEN
  | Criterion ID | Partial boundary | Pass condition |
  [one row per non-essential criterion; both columns required; source: criteria table]
PARTIAL-CREDIT MANIFEST: CLOSED

---

## Step 7: MANIFEST-ROW VERIFICATION

MANIFEST-ROW VERIFICATION: OPEN
  Check: "Partial boundary" = Partial condition cell verbatim.
  Check: "Pass condition" = Pass condition cell verbatim.
  Log REGISTER REVISION: [ID] for divergence. Correct. Close.
MANIFEST-ROW VERIFICATION: CLOSED

---

## Step 8: FINAL RUBRIC

FINAL RUBRIC: OPEN
  [Reproduce criteria table verbatim]
  Formula: (E/{N_e} * 60) + (R/{N_r} * 30) + (A/{N_a} * 10)
  [Verbatim. Do not collapse.]
  N_e = [row count]; N_r = [row count]; N_a = [row count]
  | >= 70          | PASS    | all essential pass        |
  | 50-69          | PARTIAL | all essential pass        |
  | < 50           | FAIL    | —                         |
  | essential fail | FAIL    | regardless of score       |
FINAL RUBRIC: CLOSED

---

## Input

**Skill spec:**
{{SKILL_SPEC}}

**Sample outputs:**
{{SAMPLE_OUTPUTS}}
```

---

## Variation Comparison

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role sequence | AUDITOR-first (pre-spec) | Standard | Standard | Standard | AUDITOR-first |
| Output format | Prose criteria | Table criteria | Prose criteria | Prose criteria | Table criteria |
| Phrasing | Formal explanatory | Formal explanatory | Direct imperative | Formal explanatory | Direct imperative |
| Inertia framing | None | None | None | Named competitor | None |
| Lifecycle emphasis | Standard | Standard | Minimal | Heavy (exit conditions) | Minimal |
| C-29 mechanism | Pre-spec gate forces it | Post-spec gate | Post-spec gate | Phase-exit labeled gate | Pre-spec gate forces it |
| C-30 mechanism | Explicit two-column block | Structural (table column) | Explicit two-column block | Explicit + contrast note | Structural (table column) |
| C-31 mechanism | Register + inline list | Register + inline list | Register + inline list | Register + inline + exit gates | Register + inline compact |
| C-32 mechanism | Verbatim reproduction check | Verbatim check against table | Verbatim check | Verbatim + coherence check | Verbatim check against table |

## Single-axis independence hypotheses (R12 targets)

**V-01 vs V-05:** Both are AUDITOR-first. V-01 uses prose criteria; V-05 adds table + imperative. If V-01 scores lower than V-05 on C-24 (formula consistency), the table format is the differentiating factor.

**V-02 vs V-05:** Both are table-centric. V-02 uses standard phrasing; V-05 adds AUDITOR-first + imperative. If V-02 passes C-30 (dual-column manifest) as reliably as V-05, the table axis is doing the work independently.

**V-03 vs V-05:** Both are imperative. V-03 is single-axis; V-05 adds AUDITOR-first + table. If V-03 passes C-01–C-05 (essential binary criteria) at the same rate as V-05, imperative phrasing is sufficient for essential compliance without the other axes.

**V-04 unique probe:** The only variation with inertia framing and explicit phase exit conditions. Primary test: does naming the prose-rubric competitor improve PARTIAL-CONDITION specificity (C-23) by giving criterion authors a concrete contrast target? Secondary test: do phase exit conditions make C-31 enforcement detectable by structural scan alone?
