# quest-rubric Variate — Round 7 against rubric v7

**Date:** 2026-03-16
**Skill:** quest-rubric
**Rubric:** v7 (C-01 through C-22; essential C-01–C-05, recommended C-06–C-08, aspirational C-09–C-22)
**Round:** R7 — 3 single-axis + 2 combination

**Round 7 design note:** v7 adds C-21 (phase-completion status token at every role boundary) and
C-22 (FINAL RUBRIC citation-retention guard). R6 V-05 is the carrying anchor; it scores 99.29
under v7 because both C-21 and C-22 are already satisfied by R6 V-05's full PHASE STATUS protocol
and FINAL RUBRIC retention instruction.

**The only gap entering Round 7:** C-10 (partial credit formula) — the universal miss across all
rounds. No prompt to date has produced a formula that distinguishes PARTIAL from PASS. R7 focuses
exclusively on cracking C-10.

**Why C-10 universally fails:** Every prompt uses `count(PASS) / N` as the numerator. The model
produces exactly what the template shows. When the template is binary, the output is binary. Three
independent mechanisms can break this:

1. **Formula template change** (output-format): replace the binary `count(PASS)` template with a
   weighted sum where PASS=1.0, PARTIAL=0.5, FAIL=0.0. If the model fills in a template, the
   template governs the output.

2. **Verdict tier declaration** (phrasing-register): force the model to emit an explicit
   PASS/PARTIAL/FAIL definition block before writing any criterion. Without a definition of what
   PARTIAL means in this rubric's scoring context, the model has no anchor to use it. A declaration
   block creates the anchor.

3. **Per-criterion PARTIAL-CONDITION step** (lifecycle-emphasis): add sub-step A2e to the Author
   phase, requiring the model to define the partial-credit condition for each criterion before
   recording the CRITERION row. This ties PARTIAL to specific observable states, not just a
   formula variable.

**R6 anchor inheritance:** All five variations inherit R6 V-05's C-21 and C-22 mechanics
(PHASE STATUS tokens at all four role boundaries; CM-NN citation-retention guard in FINAL RUBRIC).
These are non-negotiable. No variation downgrades them.

---

## Round 7 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | output-format | single-axis | Weighted formula template in SA-1 schema + FINAL RUBRIC | C-10 |
| V-02 | phrasing-register | single-axis | VERDICT TIER DECLARATION block before Author phase | C-10 |
| V-03 | lifecycle-emphasis | single-axis | Sub-step A2e: per-criterion PARTIAL-CONDITION | C-10 |
| V-04 | output-format × phrasing-register | combination (V-01 × V-02) | Formula template + verdict declaration | C-10 |
| V-05 | output-format × phrasing-register × lifecycle-emphasis | combination (all three) | Full stack: weighted template + verdict declaration + per-criterion partial | C-10 |

**Anchor designation (preliminary):** V-04. The formula template (V-01) controls output shape;
the verdict declaration (V-02) controls semantic grounding. Neither produces the other's effect.
V-03 is the heaviest change (adds a sub-step per criterion) and may introduce overhead that
degrades other criteria. V-05 tests whether the overhead of V-03 is justified by C-10 gain.

---

## V-01 — Output Format: Partial-Credit Formula Template

**axis:** output-format
**hypothesis:** C-10 fails because the SA-1 schema encodes a binary counting formula — the model
produces what the template shows. V-01 replaces the binary template with a weighted-sum formula
(PASS=1.0, PARTIAL=0.5, FAIL=0.0) in SA-1 `scoring_formula` and in the FINAL RUBRIC section.
If the model fills in a template mechanically, the template governs the output. Failure condition:
model copies the weighted formula but collapses to binary when filling in actual verdicts because
no definition of PARTIAL exists. Counter (for V-04): combine with V-02's VERDICT TIER DECLARATION.
All R6 V-05 mechanics (PHASE STATUS tokens, Status-Quo Rubric framing, ARTIFACT INVENTORY,
CM-NN citation rules) are unchanged.

---

You are building a scoring rubric for a Signal skill.

**The competitor you are beating:** Every rubric you write competes with the Status-Quo Rubric —
a generic scoring checklist that could be applied to any skill's output without reading the spec.
The Status-Quo Rubric passes criteria that say "output is clear," "output is complete," "output
follows instructions." Your rubric must include pass conditions that the Status-Quo Rubric cannot
satisfy: conditions that name specific counts, field names, structural patterns, or enumerations
drawn from THIS skill's output contract. A rubric that the Status-Quo Rubric could produce is
a failed rubric regardless of total score.

Three roles execute in sequence: Spec Analyst, Author, Auditor. Each role transition uses a
PHASE STATUS declaration. A role may not produce output until it writes OPEN. A role signals
completion by writing CLOSED.

**Output template (follow this order exactly):**

```
SPEC ANALYST: OPEN
  SA-1: SCHEMA BLOCK
  SA-2: CONVERSION-MAP
SPEC ANALYST: CLOSED

ARTIFACT INVENTORY
AUTHOR: [BLOCKED / OPEN]
  A-1: Failure Modes
  A-2: Essential Criteria
  A-3: Recommended and Aspirational Criteria
AUTHOR: CLOSED

STRUCTURAL VERIFICATION: [PASS / FAIL]

AUDITOR: OPEN
  AU-1: Audit Table
  AU-2: Cross-Criterion Pattern Note
  AU-3: Auditor Calibration Pair
AUDITOR: CLOSED

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### SPEC ANALYST: OPEN

You are the Spec Analyst. Produce SA-1 and SA-2. Do not write failure modes or criteria.

#### SA-1: SCHEMA BLOCK

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
verdict_values: [PASS, PARTIAL, FAIL]
verdict_weights:
  PASS: 1.0
  PARTIAL: 0.5
  FAIL: 0.0
scoring_formula: >
  composite = (sum(essential_verdict_weights) / N_essential * 60)
            + (sum(recommended_verdict_weights) / N_recommended * 30)
            + (sum(aspirational_verdict_weights) / N_aspirational * 10)
  where each criterion's verdict_weight = 1.0 if PASS, 0.5 if PARTIAL, 0.0 if FAIL
golden_threshold: "all essential criteria PASS AND composite >= 80"
```

Fill every field. Do not use TBD or placeholders.

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions ("not generic", "specific to input",
"tailored to X", "not boilerplate", or any "output must not ___" / "must be specific to ___").

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — SA-1: [complete / incomplete], SA-2: [[N] rows / empty declaration]**

---

### ARTIFACT INVENTORY

Confirm each artifact is present before Author opens:

```
SA-1 SCHEMA BLOCK:   [PRESENT] skill=[value], fields=[list], verdict_weights=[PASS=1.0, PARTIAL=0.5, FAIL=0.0] / [ABSENT]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — CM-01: [summary], ..., CM-N: [summary]
                   / [EMPTY DECLARATION]
                   / [ABSENT]
Category coverage:   [PRESENT — 3 identifiable: [C1], [C2], [C3]] / [INSUFFICIENT]
```

**AUTHOR: OPEN** — write only if SA-1 PRESENT (including verdict_weights), SA-2 PRESENT or
EMPTY DECLARATION, category coverage PRESENT.

**AUTHOR: BLOCKED** — write if any prerequisite is ABSENT or INSUFFICIENT. Write the missing
artifact immediately. Do not proceed until ARTIFACT INVENTORY can be rewritten with all items
PRESENT or EMPTY DECLARATION, then write AUTHOR: OPEN.

---

### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. If minimum not met, write additional failure modes before
proceeding to A-2.

---

### A-2: Essential Criteria (3-5)

The Status-Quo Rubric is your foil. Every criterion you write must include a pass condition that
beats the Status-Quo Rubric — it must name a count, a field name, a structural pattern, or an
enumeration from SA-1 output_contract that the Status-Quo Rubric cannot produce.

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step A2a — Type identification and draft.**

Specificity criterion: operationalizes an SA-2 prohibition.

- Specificity: "Type: specificity — SA-2 CM-[N]: [prohibition]." Draft from SA-2 PASS state.
- Non-specificity: "Type: non-specificity." Draft from failure modes and skill output contract.

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Type: [specificity — CM-NN] / [non-specificity]
Draft condition: [from A2a]
Status-Quo test: Could the Status-Quo Rubric produce this condition without reading this
  skill's spec? [YES — not grounded enough / NO — grounded]
If YES — revised condition: [revision naming a specific SA-1 element; re-run until NO]
Final condition: [condition the Status-Quo Rubric cannot produce]
Discriminating element: [the count, field name, structural pattern, or enumeration from SA-1
  that prevents the Status-Quo Rubric from passing this condition]
CRITERION GATE: [OPEN — Status-Quo test = NO] / [BLOCKED — Status-Quo test still YES]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO RUBRIC: [the condition in its weakest form — what the Status-Quo Rubric would write]
GROUNDED: [the final condition naming the discriminating element; what your rubric writes]
```

**Sub-step A2d — Forward gate and CRITERION row.** Only if CRITERION GATE = OPEN and
CALIBRATION-PAIR is present.

**Citation rule for specificity criteria:** Pass Condition in the table row must include
"operationalizes SA-2 CM-[N]" — do not drop the identifier when recording the row.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition][; operationalizes SA-2 CM-N if specificity] |
```

Repeat A2a–A2d for each essential criterion.

---

### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Each must beat the Status-Quo Rubric.
Apply citation rule: specificity criteria include CM-NN in Pass Condition.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR: CLOSED — [N] essential (C-01 through C-[N]), [N] recommended, [N] aspirational**

---

### STRUCTURAL VERIFICATION

Scan A-2 for heading patterns.

For each essential C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present with CRITERION GATE = OPEN
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present
```

Also verify:
- ARTIFACT INVENTORY block present with AUTHOR: OPEN; SA-1 includes verdict_weights field
- For each specificity criterion (INERTIA-RECORD type = specificity CM-NN), CRITERION row Pass
  Condition includes "operationalizes SA-2 CM-N"

**STRUCTURAL VERIFICATION: PASS** / **FAIL — missing: [list]** (write missing blocks, re-verify)

---

### AUDITOR: OPEN

Read all `### CRITERION [C-NN]` blocks from A-2 before writing any output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

Column note: *Status-Quo Test* — "Could the Status-Quo Rubric produce this condition?" NO = grounded. YES = revise.

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column. Write one sentence: are elements varied across types
(count, field name, structural pattern, enumeration) or clustered in one type?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
STATUS-QUO RUBRIC: [what the Status-Quo Rubric would write for this criterion]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR: CLOSED** — only after AU-1 complete, all Status-Quo Tests = NO (original or revised),
AU-2 written.

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Retain CM-NN citations in Pass Condition for specificity
criteria — do not simplify during reproduction. Substitute Auditor-revised conditions where
Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (sum(essential_verdict_weights) / N_essential * 60)
          + (sum(recommended_verdict_weights) / N_recommended * 30)
          + (sum(aspirational_verdict_weights) / N_aspirational * 10)

where: PASS → weight 1.0 | PARTIAL → weight 0.5 | FAIL → weight 0.0
```

Note: for Essential criteria, PARTIAL is permitted in the formula but a PARTIAL on any essential
criterion does not satisfy the Golden threshold requirement (all essential must PASS).

Golden threshold: all essential criteria PASS AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential PASS + >= 80 | Ship-ready rubric |
| Acceptable | all essential PASS + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential PASS + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential FAIL or PARTIAL | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion with three-state verdict: `- [ ] C-NN: [one-line assertion] — [PASS / PARTIAL / FAIL]`

---

## V-02 — Phrasing Register: Verdict Tier Declaration

**axis:** phrasing-register
**hypothesis:** C-10 fails because PARTIAL has no semantic grounding in any prior prompt — the
model cannot distinguish a PARTIAL criterion state from PASS or FAIL because no definition exists.
V-02 adds a VERDICT TIER DECLARATION block immediately after SPEC ANALYST: CLOSED and before
ARTIFACT INVENTORY. The block forces the model to emit explicit definitions: what PASS means for
this skill's rubric, what PARTIAL means (partial satisfaction condition), and what FAIL means, with
scoring weights assigned. Once PARTIAL is defined before any criterion is written, the Author phase
has a semantic anchor; the formula naturally uses it. Failure condition: model emits the declaration
block but still writes a binary formula in FINAL RUBRIC. Counter (for V-04): combine with V-01's
weighted formula template so the formula shape enforces partial credit independently of the
declaration. All R6 V-05 mechanics are unchanged.

---

You are building a scoring rubric for a Signal skill.

**The competitor you are beating:** Every rubric you write competes with the Status-Quo Rubric —
a generic scoring checklist that could be applied to any skill's output without reading the spec.
The Status-Quo Rubric passes criteria that say "output is clear," "output is complete," "output
follows instructions." Your rubric must include pass conditions that the Status-Quo Rubric cannot
satisfy: conditions that name specific counts, field names, structural patterns, or enumerations
drawn from THIS skill's output contract. A rubric that the Status-Quo Rubric could produce is
a failed rubric regardless of total score.

Three roles execute in sequence: Spec Analyst, Author, Auditor. Each role transition uses a
PHASE STATUS declaration. A role may not produce output until it writes OPEN. A role signals
completion by writing CLOSED.

**Output template (follow this order exactly):**

```
SPEC ANALYST: OPEN
  SA-1: SCHEMA BLOCK
  SA-2: CONVERSION-MAP
SPEC ANALYST: CLOSED

VERDICT TIER DECLARATION

ARTIFACT INVENTORY
AUTHOR: [BLOCKED / OPEN]
  A-1: Failure Modes
  A-2: Essential Criteria
  A-3: Recommended and Aspirational Criteria
AUTHOR: CLOSED

STRUCTURAL VERIFICATION: [PASS / FAIL]

AUDITOR: OPEN
  AU-1: Audit Table
  AU-2: Cross-Criterion Pattern Note
  AU-3: Auditor Calibration Pair
AUDITOR: CLOSED

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### SPEC ANALYST: OPEN

You are the Spec Analyst. Produce SA-1 and SA-2. Do not write failure modes or criteria.

#### SA-1: SCHEMA BLOCK

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
golden_threshold: "all essential pass AND composite >= 80"
```

Fill every field. Do not use TBD or placeholders.

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — SA-1: [complete / incomplete], SA-2: [[N] rows / empty declaration]**

---

### VERDICT TIER DECLARATION

Before writing any criterion, declare the three verdict states this rubric will use. These
definitions govern how every criterion is evaluated and how the scoring formula weights outcomes.

Write the following declaration block now:

```
VERDICT TIER DECLARATION
========================
PASS (weight = 1.0): [describe what it means for an artifact to fully satisfy a criterion
  in this rubric — be specific to the skill's output contract, not generic]
PARTIAL (weight = 0.5): [describe what it means to partially satisfy a criterion — name the
  boundary condition: what is present but insufficient, or what partially matches the pass
  condition. A criterion earns PARTIAL when the observable output satisfies the spirit but
  not the letter of the pass condition, OR when a required element is present but incomplete.]
FAIL (weight = 0.0): [describe what it means to fail a criterion — absent required element,
  wrong structure, or advisory language where mandatory language is required]

Scoring impact:
  PASS on essential → counts toward Golden threshold
  PARTIAL on essential → does NOT count toward Golden threshold; flags for revision
  FAIL on essential → rubric is invalid regardless of composite score
  PARTIAL on recommended/aspirational → contributes 0.5 weight to composite formula
```

Do not proceed to ARTIFACT INVENTORY until VERDICT TIER DECLARATION is written.

---

### ARTIFACT INVENTORY

Confirm each artifact is present before Author opens:

```
SA-1 SCHEMA BLOCK:   [PRESENT] skill=[value], fields=[list] / [ABSENT]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — CM-01: [summary], ..., CM-N: [summary]
                   / [EMPTY DECLARATION]
                   / [ABSENT]
VERDICT TIER DECLARATION: [PRESENT — PASS, PARTIAL, FAIL definitions written] / [ABSENT]
Category coverage:   [PRESENT — 3 identifiable: [C1], [C2], [C3]] / [INSUFFICIENT]
```

**AUTHOR: OPEN** — write only if SA-1 PRESENT, SA-2 PRESENT or EMPTY DECLARATION, VERDICT TIER
DECLARATION PRESENT, category coverage PRESENT.

**AUTHOR: BLOCKED** — write if any prerequisite is ABSENT or INSUFFICIENT. Write the missing
artifact immediately. Do not proceed until all items show PRESENT or EMPTY DECLARATION, then write
AUTHOR: OPEN.

---

### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. If minimum not met, write additional failure modes before
proceeding to A-2.

---

### A-2: Essential Criteria (3-5)

The Status-Quo Rubric is your foil. Every criterion you write must include a pass condition that
beats the Status-Quo Rubric — it must name a count, a field name, a structural pattern, or an
enumeration from SA-1 output_contract that the Status-Quo Rubric cannot produce.

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step A2a — Type identification and draft.**

- Specificity: "Type: specificity — SA-2 CM-[N]: [prohibition]." Draft from SA-2 PASS state.
- Non-specificity: "Type: non-specificity." Draft from failure modes and skill output contract.

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Type: [specificity — CM-NN] / [non-specificity]
Draft condition: [from A2a]
Status-Quo test: Could the Status-Quo Rubric produce this condition without reading this
  skill's spec? [YES — not grounded enough / NO — grounded]
If YES — revised condition: [revision naming a specific SA-1 element; re-run until NO]
Final condition: [condition the Status-Quo Rubric cannot produce]
Discriminating element: [the count, field name, structural pattern, or enumeration from SA-1
  that prevents the Status-Quo Rubric from passing this condition]
CRITERION GATE: [OPEN — Status-Quo test = NO] / [BLOCKED — Status-Quo test still YES]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO RUBRIC: [the condition in its weakest form — what the Status-Quo Rubric would write]
GROUNDED: [the final condition naming the discriminating element; what your rubric writes]
```

**Sub-step A2d — Forward gate and CRITERION row.** Only if CRITERION GATE = OPEN and
CALIBRATION-PAIR is present.

**Citation rule for specificity criteria:** Pass Condition in the table row must include
"operationalizes SA-2 CM-[N]" — do not drop the identifier when recording the row.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition][; operationalizes SA-2 CM-N if specificity] |
```

Repeat A2a–A2d for each essential criterion.

---

### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Each must beat the Status-Quo Rubric.
Apply citation rule: specificity criteria include CM-NN in Pass Condition.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR: CLOSED — [N] essential (C-01 through C-[N]), [N] recommended, [N] aspirational**

---

### STRUCTURAL VERIFICATION

Scan A-2 for heading patterns.

For each essential C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present with CRITERION GATE = OPEN
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present
```

Also verify:
- VERDICT TIER DECLARATION block present with PASS, PARTIAL, FAIL definitions
- ARTIFACT INVENTORY block present with AUTHOR: OPEN
- For each specificity criterion (INERTIA-RECORD type = specificity CM-NN), CRITERION row Pass
  Condition includes "operationalizes SA-2 CM-N"

**STRUCTURAL VERIFICATION: PASS** / **FAIL — missing: [list]** (write missing blocks, re-verify)

---

### AUDITOR: OPEN

Read all `### CRITERION [C-NN]` blocks from A-2 before writing any output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

Column note: *Status-Quo Test* — "Could the Status-Quo Rubric produce this condition?" NO = grounded. YES = revise.

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column. Write one sentence: are elements varied across types
(count, field name, structural pattern, enumeration) or clustered in one type?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
STATUS-QUO RUBRIC: [what the Status-Quo Rubric would write for this criterion]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR: CLOSED** — only after AU-1 complete, all Status-Quo Tests = NO (original or revised),
AU-2 written.

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Retain CM-NN citations in Pass Condition for specificity
criteria — do not simplify during reproduction. Substitute Auditor-revised conditions where
Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Apply the verdict weights from VERDICT TIER DECLARATION (PASS=1.0, PARTIAL=0.5, FAIL=0.0):

```
composite = (sum(essential_verdict_weights) / N_essential * 60)
          + (sum(recommended_verdict_weights) / N_recommended * 30)
          + (sum(aspirational_verdict_weights) / N_aspirational * 10)
```

Golden threshold: all essential criteria PASS AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential PASS + >= 80 | Ship-ready rubric |
| Acceptable | all essential PASS + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential PASS + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential FAIL or PARTIAL | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion with three-state verdict: `- [ ] C-NN: [one-line assertion] — [PASS / PARTIAL / FAIL]`

---

## V-03 — Lifecycle Emphasis: Per-Criterion Partial-Credit Step

**axis:** lifecycle-emphasis
**hypothesis:** C-10 fails because the scoring formula has no per-criterion PARTIAL conditions to
reference — PARTIAL is defined as a formula variable but never grounded in observable output states
per criterion. V-03 adds sub-step A2e to the Author phase: for each criterion, the model must define
the PARTIAL-CONDITION — what observable output state partially satisfies this criterion but does not
fully pass. The CRITERION row template is extended with a `Partial Condition` field. Once every
criterion has a named PARTIAL state, the formula can meaningfully distinguish PASS from PARTIAL.
Failure condition: model writes PARTIAL-CONDITION blocks but still emits a binary formula (count
of PASSes only). Counter (for V-05): combine with V-01's weighted formula template. Single-axis
test here isolates whether the per-criterion step alone is sufficient.

---

You are building a scoring rubric for a Signal skill.

**The competitor you are beating:** Every rubric you write competes with the Status-Quo Rubric —
a generic scoring checklist that could be applied to any skill's output without reading the spec.
The Status-Quo Rubric passes criteria that say "output is clear," "output is complete," "output
follows instructions." Your rubric must include pass conditions that the Status-Quo Rubric cannot
satisfy: conditions that name specific counts, field names, structural patterns, or enumerations
drawn from THIS skill's output contract. A rubric that the Status-Quo Rubric could produce is
a failed rubric regardless of total score.

Three roles execute in sequence: Spec Analyst, Author, Auditor. Each role transition uses a
PHASE STATUS declaration. A role may not produce output until it writes OPEN. A role signals
completion by writing CLOSED.

**Output template (follow this order exactly):**

```
SPEC ANALYST: OPEN
  SA-1: SCHEMA BLOCK
  SA-2: CONVERSION-MAP
SPEC ANALYST: CLOSED

ARTIFACT INVENTORY
AUTHOR: [BLOCKED / OPEN]
  A-1: Failure Modes
  A-2: Essential Criteria (with PARTIAL-CONDITION per criterion)
  A-3: Recommended and Aspirational Criteria (with PARTIAL-CONDITION per criterion)
AUTHOR: CLOSED

STRUCTURAL VERIFICATION: [PASS / FAIL]

AUDITOR: OPEN
  AU-1: Audit Table
  AU-2: Cross-Criterion Pattern Note
  AU-3: Auditor Calibration Pair
AUDITOR: CLOSED

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### SPEC ANALYST: OPEN

You are the Spec Analyst. Produce SA-1 and SA-2. Do not write failure modes or criteria.

#### SA-1: SCHEMA BLOCK

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition, partial_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
  note: PARTIAL verdicts count as 0.5 in the numerator for recommended and aspirational tiers
golden_threshold: "all essential criteria PASS AND composite >= 80"
```

Fill every field. Do not use TBD or placeholders. Note that `partial_condition` is a required
output contract field alongside `pass_condition`.

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — SA-1: [complete / incomplete — partial_condition field present in
output_contract], SA-2: [[N] rows / empty declaration]**

---

### ARTIFACT INVENTORY

Confirm each artifact is present before Author opens:

```
SA-1 SCHEMA BLOCK:   [PRESENT] skill=[value], fields=[list — partial_condition present?] / [ABSENT]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — CM-01: [summary], ..., CM-N: [summary]
                   / [EMPTY DECLARATION]
                   / [ABSENT]
Category coverage:   [PRESENT — 3 identifiable: [C1], [C2], [C3]] / [INSUFFICIENT]
```

**AUTHOR: OPEN** — write only if SA-1 PRESENT (including partial_condition in output_contract),
SA-2 PRESENT or EMPTY DECLARATION, category coverage PRESENT.

**AUTHOR: BLOCKED** — write if any prerequisite is ABSENT or INSUFFICIENT. Write the missing
artifact immediately. Do not proceed until all items show PRESENT or EMPTY DECLARATION, then write
AUTHOR: OPEN.

---

### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. If minimum not met, write additional failure modes before
proceeding to A-2.

---

### A-2: Essential Criteria (3-5)

The Status-Quo Rubric is your foil. Every criterion you write must include a pass condition that
beats the Status-Quo Rubric — it must name a count, a field name, a structural pattern, or an
enumeration from SA-1 output_contract that the Status-Quo Rubric cannot produce.

For each essential criterion, produce four named blocks in order, then record the criterion row.

**Sub-step A2a — Type identification and draft.**

- Specificity: "Type: specificity — SA-2 CM-[N]: [prohibition]." Draft from SA-2 PASS state.
- Non-specificity: "Type: non-specificity." Draft from failure modes and skill output contract.

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Type: [specificity — CM-NN] / [non-specificity]
Draft condition: [from A2a]
Status-Quo test: Could the Status-Quo Rubric produce this condition without reading this
  skill's spec? [YES — not grounded enough / NO — grounded]
If YES — revised condition: [revision naming a specific SA-1 element; re-run until NO]
Final condition: [condition the Status-Quo Rubric cannot produce]
Discriminating element: [the count, field name, structural pattern, or enumeration from SA-1
  that prevents the Status-Quo Rubric from passing this condition]
CRITERION GATE: [OPEN — Status-Quo test = NO] / [BLOCKED — Status-Quo test still YES]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO RUBRIC: [the condition in its weakest form — what the Status-Quo Rubric would write]
GROUNDED: [the final condition naming the discriminating element; what your rubric writes]
```

**Sub-step A2d — PARTIAL-CONDITION block.** Immediately after A2c. Only if CRITERION GATE = OPEN.

Define the observable output state that partially satisfies this criterion — not fully PASS, not
FAIL. A PARTIAL state is present when the required element exists but is incomplete, covers only
a subset of required cases, or uses advisory language where mandatory language is required.

```
### PARTIAL-CONDITION [C-NN]
Full PASS condition: [final condition from INERTIA-RECORD]
PARTIAL state: [observable output condition that partially satisfies — name the specific
  incomplete element: which field is present but incomplete, or which subset is present
  but not the full set]
FAIL state: [required element absent entirely, or structural requirement violated]
Scoring:
  PASS    → 1.0 (counts toward Golden threshold for essential criteria)
  PARTIAL → 0.5 (does NOT satisfy Golden threshold for essential criteria)
  FAIL    → 0.0
```

**Sub-step A2e — Forward gate and CRITERION row.** Only if CRITERION GATE = OPEN and both
CALIBRATION-PAIR and PARTIAL-CONDITION are present.

**Citation rule for specificity criteria:** Pass Condition in the table row must include
"operationalizes SA-2 CM-[N]" — do not drop the identifier when recording the row.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition][; operationalizes SA-2 CM-N if specificity] | [partial state from PARTIAL-CONDITION block] |
```

Repeat A2a–A2e for each essential criterion.

---

### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Each must beat the Status-Quo Rubric.
Apply citation rule: specificity criteria include CM-NN in Pass Condition.
Apply PARTIAL-CONDITION: each criterion requires a PARTIAL-CONDITION block before recording
(same A2d format). Include Partial Condition column in the table.

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|

**AUTHOR: CLOSED — [N] essential (C-01 through C-[N]), [N] recommended, [N] aspirational**

---

### STRUCTURAL VERIFICATION

Scan A-2 for heading patterns.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present with CRITERION GATE = OPEN
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### PARTIAL-CONDITION [C-NN]
- [ ] ### PARTIAL-CONDITION [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present with Partial Condition column filled
```

Also verify:
- ARTIFACT INVENTORY block present with AUTHOR: OPEN
- For each specificity criterion, CRITERION row Pass Condition includes "operationalizes SA-2 CM-N"

**STRUCTURAL VERIFICATION: PASS** / **FAIL — missing: [list]** (write missing blocks, re-verify)

---

### AUDITOR: OPEN

Read all `### CRITERION [C-NN]` blocks from A-2 before writing any output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Partial Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|---------------------------|-----------------|----------------------|--------------------|-------------------|

Column note: *Partial Condition* column — confirm each partial condition is observable and distinct
from both PASS and FAIL; if absent or identical to PASS, mark Revision Required = YES.

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column. Write one sentence: are elements varied across types
(count, field name, structural pattern, enumeration) or clustered in one type?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
STATUS-QUO RUBRIC: [what the Status-Quo Rubric would write for this criterion]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR: CLOSED** — only after AU-1 complete, all Status-Quo Tests = NO, all Partial Conditions
filled and distinct, AU-2 written.

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with both Pass Condition and Partial Condition columns.
Retain CM-NN citations in Pass Condition for specificity criteria — do not simplify during
reproduction. Substitute Auditor-revised conditions where Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = ((E_pass + 0.5 * E_partial) / N_essential * 60)
          + ((R_pass + 0.5 * R_partial) / N_recommended * 30)
          + ((A_pass + 0.5 * A_partial) / N_aspirational * 10)

where:
  E_pass    = count of essential criteria with PASS verdict
  E_partial = count of essential criteria with PARTIAL verdict
  R_pass    = count of recommended criteria with PASS verdict
  R_partial = count of recommended criteria with PARTIAL verdict
  A_pass    = count of aspirational criteria with PASS verdict
  A_partial = count of aspirational criteria with PARTIAL verdict
```

Note: PARTIAL verdicts on Essential criteria contribute 0 to the Golden threshold check
(all essential must PASS) but contribute 0.5 to the composite score.

Golden threshold: all essential criteria PASS AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential PASS + >= 80 | Ship-ready rubric |
| Acceptable | all essential PASS + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential PASS + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential FAIL or PARTIAL | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion] — [PASS / PARTIAL / FAIL]`

---

## V-04 — Output Format × Phrasing Register (V-01 × V-02, Combination)

**axis:** output-format × phrasing-register
**hypothesis:** V-01 changes the formula template (shape of output); V-02 defines PARTIAL before
criteria are written (semantic grounding). These mechanisms operate at non-competing positions:
the formula template fires when SA-1 is produced (before any criteria exist); the VERDICT TIER
DECLARATION fires after Spec Analyst closes and before Author opens (before any criterion is
written). Neither produces the other's effect. Combined, V-04 should satisfy C-10 from both
angles: the model is given a template that requires weighted scoring AND a defined meaning for
PARTIAL before it writes a single criterion. Failure condition: model satisfies both (weighted
formula present, VERDICT TIER DECLARATION written) but the FINAL RUBRIC formula still collapses
to binary because the Auditor phase has no instruction to carry the weighted formula forward.
Counter: FINAL RUBRIC section explicitly restates the weighted formula with verdict weights
inline — not a reference to SA-1.

---

You are building a scoring rubric for a Signal skill.

**The competitor you are beating:** Every rubric you write competes with the Status-Quo Rubric —
a generic scoring checklist that could be applied to any skill's output without reading the spec.
The Status-Quo Rubric passes criteria that say "output is clear," "output is complete," "output
follows instructions." Your rubric must include pass conditions that the Status-Quo Rubric cannot
satisfy: conditions that name specific counts, field names, structural patterns, or enumerations
drawn from THIS skill's output contract. A rubric that the Status-Quo Rubric could produce is
a failed rubric regardless of total score.

Three roles execute in sequence: Spec Analyst, Author, Auditor. Each role transition uses a
PHASE STATUS declaration. A role may not produce output until it writes OPEN. A role signals
completion by writing CLOSED.

**Output template (follow this order exactly):**

```
SPEC ANALYST: OPEN
  SA-1: SCHEMA BLOCK
  SA-2: CONVERSION-MAP
SPEC ANALYST: CLOSED

VERDICT TIER DECLARATION

ARTIFACT INVENTORY
AUTHOR: [BLOCKED / OPEN]
  A-1: Failure Modes
  A-2: Essential Criteria
  A-3: Recommended and Aspirational Criteria
AUTHOR: CLOSED

STRUCTURAL VERIFICATION: [PASS / FAIL]

AUDITOR: OPEN
  AU-1: Audit Table
  AU-2: Cross-Criterion Pattern Note
  AU-3: Auditor Calibration Pair
AUDITOR: CLOSED

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### SPEC ANALYST: OPEN

You are the Spec Analyst. Produce SA-1 and SA-2. Do not write failure modes or criteria.

#### SA-1: SCHEMA BLOCK

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
verdict_values: [PASS, PARTIAL, FAIL]
verdict_weights:
  PASS: 1.0
  PARTIAL: 0.5
  FAIL: 0.0
scoring_formula: >
  composite = (sum(essential_verdict_weights) / N_essential * 60)
            + (sum(recommended_verdict_weights) / N_recommended * 30)
            + (sum(aspirational_verdict_weights) / N_aspirational * 10)
  where each criterion's verdict_weight = 1.0 if PASS, 0.5 if PARTIAL, 0.0 if FAIL
golden_threshold: "all essential criteria PASS AND composite >= 80"
```

Fill every field. Do not use TBD or placeholders.

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — SA-1: [complete / incomplete — verdict_weights present], SA-2: [[N] rows / empty declaration]**

---

### VERDICT TIER DECLARATION

Write the three-state verdict definition before Author opens. These definitions govern every
criterion evaluation and the scoring formula.

```
VERDICT TIER DECLARATION
========================
PASS (weight = 1.0): criterion fully satisfied — all required elements present, correct
  structure, mandatory language used, no omissions detectable by inspection
PARTIAL (weight = 0.5): criterion partially satisfied — required element present but
  incomplete OR required structure present but partially filled OR one of N required
  conditions met but not all N. Observable boundary: [define the specific partial state
  relevant to this skill's output contract — e.g., "criterion names target skill but
  omits date" or "formula present but denominator not stated"]
FAIL (weight = 0.0): required element absent, wrong structure, or advisory language
  ("should", "ideally") used where mandatory language ("must", "required") is specified

Scoring impact on Golden threshold:
  Essential criteria: ALL must be PASS (not PARTIAL, not FAIL) for Golden status
  Recommended criteria: PARTIAL counts as 0.5 weight in composite formula
  Aspirational criteria: PARTIAL counts as 0.5 weight in composite formula
```

Do not proceed to ARTIFACT INVENTORY until VERDICT TIER DECLARATION is written with all three
states defined and scoring impact stated.

---

### ARTIFACT INVENTORY

Confirm each artifact is present before Author opens:

```
SA-1 SCHEMA BLOCK:   [PRESENT] skill=[value], verdict_weights=[PASS=1.0, PARTIAL=0.5, FAIL=0.0] / [ABSENT]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — CM-01: [summary], ..., CM-N: [summary]
                   / [EMPTY DECLARATION]
                   / [ABSENT]
VERDICT TIER DECLARATION: [PRESENT — 3 states defined with scoring impact] / [ABSENT]
Category coverage:   [PRESENT — 3 identifiable: [C1], [C2], [C3]] / [INSUFFICIENT]
```

**AUTHOR: OPEN** — write only if SA-1 PRESENT (verdict_weights included), SA-2 PRESENT or
EMPTY DECLARATION, VERDICT TIER DECLARATION PRESENT, category coverage PRESENT.

**AUTHOR: BLOCKED** — write if any prerequisite is ABSENT or INSUFFICIENT. Write the missing
artifact immediately. Do not proceed until all items show PRESENT or EMPTY DECLARATION, then
write AUTHOR: OPEN.

---

### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. If minimum not met, write additional failure modes before
proceeding to A-2.

---

### A-2: Essential Criteria (3-5)

The Status-Quo Rubric is your foil. Every criterion you write must include a pass condition that
beats the Status-Quo Rubric — it must name a count, a field name, a structural pattern, or an
enumeration from SA-1 output_contract that the Status-Quo Rubric cannot produce.

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step A2a — Type identification and draft.**

- Specificity: "Type: specificity — SA-2 CM-[N]: [prohibition]." Draft from SA-2 PASS state.
- Non-specificity: "Type: non-specificity." Draft from failure modes and skill output contract.

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Type: [specificity — CM-NN] / [non-specificity]
Draft condition: [from A2a]
Status-Quo test: Could the Status-Quo Rubric produce this condition without reading this
  skill's spec? [YES — not grounded enough / NO — grounded]
If YES — revised condition: [revision naming a specific SA-1 element; re-run until NO]
Final condition: [condition the Status-Quo Rubric cannot produce]
Discriminating element: [the count, field name, structural pattern, or enumeration from SA-1
  that prevents the Status-Quo Rubric from passing this condition]
CRITERION GATE: [OPEN — Status-Quo test = NO] / [BLOCKED — Status-Quo test still YES]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO RUBRIC: [the condition in its weakest form — what the Status-Quo Rubric would write]
GROUNDED: [the final condition naming the discriminating element; what your rubric writes]
```

**Sub-step A2d — Forward gate and CRITERION row.** Only if CRITERION GATE = OPEN and
CALIBRATION-PAIR is present.

**Citation rule for specificity criteria:** Pass Condition in the table row must include
"operationalizes SA-2 CM-[N]" — do not drop the identifier when recording the row.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition][; operationalizes SA-2 CM-N if specificity] |
```

Repeat A2a–A2d for each essential criterion.

---

### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Each must beat the Status-Quo Rubric.
Apply citation rule: specificity criteria include CM-NN in Pass Condition.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR: CLOSED — [N] essential (C-01 through C-[N]), [N] recommended, [N] aspirational**

---

### STRUCTURAL VERIFICATION

Scan A-2 for heading patterns.

For each essential C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present with CRITERION GATE = OPEN
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present
```

Also verify:
- SA-1 includes verdict_weights (PASS=1.0, PARTIAL=0.5, FAIL=0.0)
- VERDICT TIER DECLARATION block present with PASS, PARTIAL, FAIL defined
- ARTIFACT INVENTORY block present with AUTHOR: OPEN
- For each specificity criterion, CRITERION row Pass Condition includes "operationalizes SA-2 CM-N"

**STRUCTURAL VERIFICATION: PASS** / **FAIL — missing: [list]** (write missing blocks, re-verify)

---

### AUDITOR: OPEN

Read all `### CRITERION [C-NN]` blocks from A-2 before writing any output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

Column note: *Status-Quo Test* — "Could the Status-Quo Rubric produce this condition?" NO = grounded. YES = revise.

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column. Write one sentence: are elements varied across types
(count, field name, structural pattern, enumeration) or clustered in one type?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
STATUS-QUO RUBRIC: [what the Status-Quo Rubric would write for this criterion]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR: CLOSED** — only after AU-1 complete, all Status-Quo Tests = NO (original or revised),
AU-2 written.

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Retain CM-NN citations in Pass Condition for specificity
criteria — do not simplify during reproduction. Substitute Auditor-revised conditions where
Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Apply verdict weights from VERDICT TIER DECLARATION. Reproduce the weighted formula from SA-1
verbatim — do not collapse to binary counting:

```
composite = (sum(essential_verdict_weights) / N_essential * 60)
          + (sum(recommended_verdict_weights) / N_recommended * 30)
          + (sum(aspirational_verdict_weights) / N_aspirational * 10)

where: PASS → weight 1.0 | PARTIAL → weight 0.5 | FAIL → weight 0.0
```

Golden threshold: all essential criteria PASS AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential PASS + >= 80 | Ship-ready rubric |
| Acceptable | all essential PASS + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential PASS + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential FAIL or PARTIAL | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion with three-state verdict: `- [ ] C-NN: [one-line assertion] — [PASS / PARTIAL / FAIL]`

---

## V-05 — Output Format × Phrasing Register × Lifecycle Emphasis (Full Combination)

**axis:** output-format × phrasing-register × lifecycle-emphasis
**hypothesis:** V-04 (weighted formula + verdict declaration) is the combination anchor for C-10.
V-05 adds V-03's per-criterion PARTIAL-CONDITION step (lifecycle-emphasis axis). The three
mechanisms target C-10 at three different points in the lifecycle: formula template (SA-1 phase),
verdict definition (inter-phase gap between SA close and Author open), and per-criterion
PARTIAL-CONDITION (Author A-2 sub-step). If V-05 reaches C-10 PASS and V-04 does not, the per-
criterion step is load-bearing — the model needs to work out PARTIAL per criterion before the
formula can mean something. If V-04 and V-05 both pass C-10, the per-criterion step is redundant
and should be excluded from the base (it adds overhead to every criterion). All R6 V-05 mechanics
(PHASE STATUS tokens at all four role boundaries, Status-Quo Rubric framing, ARTIFACT INVENTORY,
CM-NN citation rules, citation-retention guard in FINAL RUBRIC) are preserved in full.

---

You are building a scoring rubric for a Signal skill.

**The competitor you are beating:** Every rubric you write competes with the Status-Quo Rubric —
a generic scoring checklist that could be applied to any skill's output without reading the spec.
The Status-Quo Rubric passes criteria that say "output is clear," "output is complete," "output
follows instructions." Your rubric must include pass conditions that the Status-Quo Rubric cannot
satisfy: conditions that name specific counts, field names, structural patterns, or enumerations
drawn from THIS skill's output contract. A rubric that the Status-Quo Rubric could produce is
a failed rubric regardless of total score.

Three roles execute in sequence: Spec Analyst, Author, Auditor. Each role transition uses a
PHASE STATUS declaration. A role may not produce output until it writes OPEN. A role signals
completion by writing CLOSED.

**Output template (follow this order exactly):**

```
SPEC ANALYST: OPEN
  SA-1: SCHEMA BLOCK
  SA-2: CONVERSION-MAP
SPEC ANALYST: CLOSED

VERDICT TIER DECLARATION

ARTIFACT INVENTORY
AUTHOR: [BLOCKED / OPEN]
  A-1: Failure Modes
  A-2: Essential Criteria (with PARTIAL-CONDITION per criterion)
  A-3: Recommended and Aspirational Criteria (with PARTIAL-CONDITION per criterion)
AUTHOR: CLOSED

STRUCTURAL VERIFICATION: [PASS / FAIL]

AUDITOR: OPEN
  AU-1: Audit Table
  AU-2: Cross-Criterion Pattern Note
  AU-3: Auditor Calibration Pair
AUDITOR: CLOSED

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### SPEC ANALYST: OPEN

You are the Spec Analyst. Produce SA-1 and SA-2. Do not write failure modes or criteria.

#### SA-1: SCHEMA BLOCK

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition, partial_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
verdict_values: [PASS, PARTIAL, FAIL]
verdict_weights:
  PASS: 1.0
  PARTIAL: 0.5
  FAIL: 0.0
scoring_formula: >
  composite = (sum(essential_verdict_weights) / N_essential * 60)
            + (sum(recommended_verdict_weights) / N_recommended * 30)
            + (sum(aspirational_verdict_weights) / N_aspirational * 10)
  where each criterion's verdict_weight = 1.0 if PASS, 0.5 if PARTIAL, 0.0 if FAIL
golden_threshold: "all essential criteria PASS AND composite >= 80"
```

Fill every field. `partial_condition` is a required output contract field. Do not use TBD or
placeholders.

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — SA-1: [complete / incomplete — verify: partial_condition in
output_contract, verdict_weights present], SA-2: [[N] rows / empty declaration]**

---

### VERDICT TIER DECLARATION

Write the three-state verdict definition before Author opens. These definitions govern every
criterion evaluation and the scoring formula.

```
VERDICT TIER DECLARATION
========================
PASS (weight = 1.0): criterion fully satisfied — all required elements present, correct
  structure, mandatory language used, no omissions detectable by inspection of the artifact
PARTIAL (weight = 0.5): criterion partially satisfied — required element present but
  incomplete OR required structure present but partially filled OR required language present
  in some instances but not all. The PARTIAL state is observable without content-analysis:
  it must be detectable by a string scan or structural inspection. "Unclear" is not a
  PARTIAL state; "field present but empty" or "N-1 of N required items present" is.
FAIL (weight = 0.0): required element absent, wrong structure, or advisory language
  ("should", "ideally") used where mandatory language ("must", "required") is specified

Scoring impact:
  Essential criteria: ALL must be PASS for Golden threshold. PARTIAL blocks Golden.
  Recommended criteria: PARTIAL counts as 0.5 weight in composite formula.
  Aspirational criteria: PARTIAL counts as 0.5 weight in composite formula.
```

Do not proceed to ARTIFACT INVENTORY until VERDICT TIER DECLARATION is written with all three
states defined, observable conditions stated, and scoring impact for essential vs.
recommended/aspirational stated separately.

---

### ARTIFACT INVENTORY

Confirm each artifact is present before Author opens:

```
SA-1 SCHEMA BLOCK:   [PRESENT] skill=[value], fields=[list — partial_condition present?],
                     verdict_weights=[PASS=1.0, PARTIAL=0.5, FAIL=0.0] / [ABSENT]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — CM-01: [summary], ..., CM-N: [summary]
                   / [EMPTY DECLARATION]
                   / [ABSENT]
VERDICT TIER DECLARATION: [PRESENT — 3 states defined, observable conditions stated,
                            scoring impact differentiated] / [ABSENT]
Category coverage:   [PRESENT — 3 identifiable: [C1], [C2], [C3]] / [INSUFFICIENT]
```

**AUTHOR: OPEN** — write only if SA-1 PRESENT (partial_condition and verdict_weights included),
SA-2 PRESENT or EMPTY DECLARATION, VERDICT TIER DECLARATION PRESENT with all required content,
category coverage PRESENT.

**AUTHOR: BLOCKED** — write if any prerequisite is ABSENT or INSUFFICIENT. Write the missing
artifact immediately. Do not proceed until ARTIFACT INVENTORY can be rewritten with all items
PRESENT or EMPTY DECLARATION, then write AUTHOR: OPEN.

---

### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading. If minimum not met, write additional failure modes before
proceeding to A-2.

---

### A-2: Essential Criteria (3-5)

The Status-Quo Rubric is your foil. Every criterion you write must include a pass condition that
beats the Status-Quo Rubric — it must name a count, a field name, a structural pattern, or an
enumeration from SA-1 output_contract that the Status-Quo Rubric cannot produce.

For each essential criterion, produce four named blocks in order, then record the criterion row.

**Sub-step A2a — Type identification and draft.**

- Specificity: "Type: specificity — SA-2 CM-[N]: [prohibition]." Draft from SA-2 PASS state.
- Non-specificity: "Type: non-specificity." Draft from failure modes and skill output contract.

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Type: [specificity — CM-NN] / [non-specificity]
Draft condition: [from A2a]
Status-Quo test: Could the Status-Quo Rubric produce this condition without reading this
  skill's spec? [YES — not grounded enough / NO — grounded]
If YES — revised condition: [revision naming a specific SA-1 element; re-run until NO]
Final condition: [condition the Status-Quo Rubric cannot produce]
Discriminating element: [the count, field name, structural pattern, or enumeration from SA-1
  that prevents the Status-Quo Rubric from passing this condition]
CRITERION GATE: [OPEN — Status-Quo test = NO] / [BLOCKED — Status-Quo test still YES]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO RUBRIC: [the condition in its weakest form — what the Status-Quo Rubric would write]
GROUNDED: [the final condition naming the discriminating element; what your rubric writes]
```

**Sub-step A2d — PARTIAL-CONDITION block.** Immediately after A2c. Only if CRITERION GATE = OPEN.

```
### PARTIAL-CONDITION [C-NN]
Full PASS condition: [final condition from INERTIA-RECORD]
PARTIAL observable state: [what specific partial output state earns 0.5 — name the incomplete
  element: which required field is present but empty, or which subset of N required items is
  present, or which mandatory language is present in some but not all instances]
FAIL observable state: [required element entirely absent, or structural requirement violated]
Scoring: PASS=1.0 | PARTIAL=0.5 | FAIL=0.0
For essential criteria: PARTIAL does not satisfy Golden threshold.
```

**Sub-step A2e — Forward gate and CRITERION row.** Only if CRITERION GATE = OPEN and both
CALIBRATION-PAIR and PARTIAL-CONDITION are present.

**Citation rule for specificity criteria:** Pass Condition in the table row must include
"operationalizes SA-2 CM-[N]" — do not drop the identifier when recording the row.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition][; operationalizes SA-2 CM-N if specificity] | [PARTIAL observable state from PARTIAL-CONDITION block] |
```

Repeat A2a–A2e for each essential criterion.

---

### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Each must beat the Status-Quo Rubric.
Apply citation rule: specificity criteria include CM-NN in Pass Condition.
Apply PARTIAL-CONDITION: each criterion requires a PARTIAL-CONDITION block before recording
(same A2d format). Include Partial Condition column in the table.

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|

**AUTHOR: CLOSED — [N] essential (C-01 through C-[N]), [N] recommended, [N] aspirational**

---

### STRUCTURAL VERIFICATION

Scan A-2 for heading patterns.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present with CRITERION GATE = OPEN
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### PARTIAL-CONDITION [C-NN]
- [ ] ### PARTIAL-CONDITION [C-NN] present with PARTIAL observable state filled, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present with Partial Condition column filled
```

Also verify:
- SA-1 includes verdict_weights and partial_condition in output_contract
- VERDICT TIER DECLARATION block present with PASS, PARTIAL, FAIL defined (all observable)
- ARTIFACT INVENTORY block present with AUTHOR: OPEN
- For each specificity criterion, CRITERION row Pass Condition includes "operationalizes SA-2 CM-N"

**STRUCTURAL VERIFICATION: PASS** / **FAIL — missing: [list]** (write missing blocks, re-verify)

---

### AUDITOR: OPEN

Read all `### CRITERION [C-NN]` blocks from A-2 before writing any output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Partial Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|---------------------------|-----------------|----------------------|--------------------|-------------------|

Column note: for each row, confirm Partial Condition is observable and distinct from both PASS and
FAIL. If absent or non-observable ("somewhat passes"), mark Revision Required = YES.

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column. Write one sentence: are elements varied across types
(count, field name, structural pattern, enumeration) or clustered in one type?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
STATUS-QUO RUBRIC: [what the Status-Quo Rubric would write for this criterion]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR: CLOSED** — only after AU-1 complete, all Status-Quo Tests = NO (original or revised),
all Partial Conditions filled and observable, AU-2 written.

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with both Pass Condition and Partial Condition columns.
Retain CM-NN citations in Pass Condition for specificity criteria — do not simplify or omit
during reproduction. Substitute Auditor-revised conditions where Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition | Partial Condition |
|----|-----------|----------|--------|----------------|-------------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Apply verdict weights declared in VERDICT TIER DECLARATION. Reproduce verbatim from SA-1 —
do not collapse to binary counting:

```
composite = (sum(essential_verdict_weights) / N_essential * 60)
          + (sum(recommended_verdict_weights) / N_recommended * 30)
          + (sum(aspirational_verdict_weights) / N_aspirational * 10)

where: PASS → weight 1.0 | PARTIAL → weight 0.5 | FAIL → weight 0.0
```

Expanded form for scorecards:

```
composite = ((E_pass + 0.5 * E_partial) / N_essential * 60)
          + ((R_pass + 0.5 * R_partial) / N_recommended * 30)
          + ((A_pass + 0.5 * A_partial) / N_aspirational * 10)
```

Note: PARTIAL verdicts on Essential criteria contribute 0.5 to the composite formula but do NOT
count toward the Golden threshold check (all essential must PASS).

Golden threshold: all essential criteria PASS AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential PASS + >= 80 | Ship-ready rubric |
| Acceptable | all essential PASS + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential PASS + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential FAIL or PARTIAL | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion with three-state verdict: `- [ ] C-NN: [one-line assertion] — [PASS / PARTIAL / FAIL]`

---

## Anchor Designation

**Preliminary anchor: V-04**

V-04 targets C-10 from two non-competing positions — the formula template (SA-1 phase, before
any criteria exist) and the verdict declaration (inter-phase gap, before Author opens). If V-04
reaches C-10 PASS, the per-criterion step from V-05 is optional overhead and should be excluded
from the base prompt.

**Interaction test for V-05 vs. V-04:**

If V-05 passes C-10 but V-04 does not: the PARTIAL-CONDITION step is load-bearing. The model
cannot populate a PARTIAL formula variable without having worked out what PARTIAL means per
criterion. Add the PARTIAL-CONDITION step to V-04 to create the R8 base.

If V-04 passes C-10 and V-05 also passes: the PARTIAL-CONDITION step is redundant for C-10
(formula template + verdict declaration are sufficient). Exclude V-03 mechanics from R8 base.
Investigate whether V-05 improves other aspirational criteria (C-13 foil pair quality, C-15
specificity conversion) as a secondary benefit.

If neither V-04 nor V-05 passes C-10: investigate whether the FINAL RUBRIC reproduction step
strips the weighted formula back to binary. Counter for R8: add an explicit "DO NOT collapse to
binary counting — reproduce the weighted formula verbatim from SA-1" guard in the FINAL RUBRIC
section, analogous to the CM-NN citation-retention guard (C-22).

---

## Combination Roadmap (for Round 8)

| Scenario | Expected Outcome | Round 8 Action |
|----------|-----------------|----------------|
| V-04 passes C-10 | Formula template + verdict declaration sufficient | V-04 becomes base; retire V-03 axis; verify no other criteria regress |
| V-05 passes C-10, V-04 fails | Per-criterion PARTIAL-CONDITION is load-bearing | Merge PARTIAL-CONDITION step from V-05 into V-04 base |
| Neither passes C-10 | Formula stripping at FINAL RUBRIC reproduction | Add explicit anti-collapse guard to FINAL RUBRIC section; test as single-axis V-01 in R8 |
| C-10 passes AND C-13 improves | Partial-credit framing improves foil-pair quality | Test PARTIAL-CONDITION as C-13 booster axis in R8 isolation |
| Any currently-passing criterion regresses in V-05 | PARTIAL-CONDITION step introduces overhead that destabilizes other mechanics | Keep V-03 axis isolated; do not merge into base if regression detected |
