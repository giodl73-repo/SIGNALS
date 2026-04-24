# quest-rubric Variate — Round 6 against rubric v6

**Date:** 2026-03-16
**Skill:** quest-rubric
**Rubric:** v6 (C-01 through C-20; essential C-01–C-05, recommended C-06–C-08, aspirational C-09–C-20)
**Round:** R6 — 3 single-axis + 2 combination

**Round 6 design note:** v6 adds C-19 and C-20 from Round 5 excellence signals E-1 and E-2:

- **C-19** (E-1): The Author phase cites named row identifiers (CM-NN, SA-NN) from pre-phase handoff
  artifacts in criterion text, rather than re-deriving inline. V-03 from R5 originated this pattern;
  the R5 roadmap explicitly named it for v6 absorption.
- **C-20** (E-2): The Author Entry Gate is a structural block — imperative "DO NOT BEGIN until
  [named pre-phase artifacts] are confirmed present" language, naming the specific artifacts. Advisory
  language does not pass. The distinguishing test: does the prompt contain "DO NOT BEGIN" (or
  equivalent imperative blocking phrasing) AND name the specific artifacts by identifier, not just
  by phase label?

Prior-round status: R5 V-04 (output-format × lifecycle-emphasis) is the working anchor. V-03 (role-
sequence solo) demonstrated C-19 as an emergent pattern when Spec Analyst produces named artifacts.
V-05 (all three) was the strongest candidate. R6 uses V-05 as the base and isolates the two new
mechanisms before recombining.

Three specific gaps:

1. **C-19 citation gap**: Prior prompts (V-02, V-04 from R5) have CONVERSION-MAP rows with
   identifiers, but criteria do not carry those identifiers into the canonical criterion row. The
   INERTIA-RECORD block may contain "CM-02 reference" but the CRITERION table row has a standalone
   pass condition. C-19 requires the identifier to appear in the criterion text itself — not just
   in the working block.

2. **C-20 gate gap**: V-05 (R5) has "AUTHOR ENTRY GATE — DO NOT begin writing criteria until:
   Spec Analyst Completion Gate is cleared." This references the gate by name but not the specific
   artifacts by identifier. C-20 requires the gate to name the blocking artifacts ("SA-1 SCHEMA
   BLOCK", "SA-2 CONVERSION-MAP rows CM-01 through CM-last") — phase label reference is insufficient.

3. **C-19/C-20 propagation gap**: Even if an Author Entry Gate names artifacts correctly (C-20 pass)
   and identifiers appear in INERTIA-RECORD blocks (near-miss on C-19), the final CRITERION row's
   Pass Condition may strip identifiers during canonicalization. C-19 requires the identifier to
   survive into the canonical row, since that is the artifact the rubric scores.

---

## Round 6 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis | Author Entry Gate names specific artifacts with imperative blocking language | C-20 |
| V-02 | role-sequence | single-axis | Identifier citation propagated into canonical CRITERION row Pass Condition | C-19 |
| V-03 | phrasing-register | single-axis | Formal-imperative throughout all phase boundaries — hard-stop declarations not checklists | C-20 (register test) |
| V-04 | lifecycle-emphasis × role-sequence | combination (V-01 × V-02) | Imperative named-artifact gate + identifier citation in canonical row | C-19, C-20 |
| V-05 | lifecycle-emphasis × role-sequence × phrasing-register + inertia-framing | combination (all three + named competitor) | Full stack: imperative gate + identifier citation + formal-imperative register + named Status-Quo Rubric | C-07, C-19, C-20 |

**Anchor designation (preliminary):** V-04. C-19 and C-20 target non-competing positions in the
lifecycle: C-20 fires at the Author phase boundary (a gate event); C-19 fires at criterion
canonicalization (a row-content event). Neither mechanism can produce the other's effect. V-04
combines them; if both fire correctly, V-04 should be additive. V-05 adds phrasing-register and
inertia-framing, which are independent of the gate/citation mechanisms — improvement in V-05 over
V-04 would signal that register and competitor framing contribute to C-20 compliance and C-07
specificity respectively.

---

## V-01 — Lifecycle Emphasis: Author Entry Gate with Named Artifact Blocking

**axis:** lifecycle-emphasis
**hypothesis:** C-20 requires the Author Entry Gate to use imperative blocking phrasing AND name
the specific blocking artifacts by identifier, not by phase label. V-05 from R5 has "DO NOT begin
writing criteria until: Spec Analyst Completion Gate is cleared" — this names the gate by label
("Spec Analyst Completion Gate") but not the artifacts it guards (SA-1, SA-2). C-20 tests whether
the gate names the artifacts themselves. V-01 adds one change to R5 V-05: the Author Entry Gate
is rewritten to name SA-1 (SCHEMA BLOCK) and SA-2 (CONVERSION-MAP rows) by identifier, and uses
hard imperative blocking ("DO NOT BEGIN WRITING CRITERIA") rather than advisory checklist. All
other mechanics remain identical to R5 V-05. Failure condition: if C-20 still fails, the model
writes the gate with identifiers but treats it as advisory — the model begins criteria even if
it cannot confirm SA-2 row count. Counter: add a "BLOCKED" declaration the model must write before
the gate can be cleared: "AUTHOR BLOCKED: SA-1 [status: PRESENT / ABSENT]. SA-2 [row count: N
rows, identifiers: CM-01 ... CM-N / EMPTY DECLARATION / ABSENT]."

---

You are building a scoring rubric for a Signal skill. Three roles execute in sequence:

1. **Spec Analyst** — reads the skill spec; produces SA-1 (SCHEMA BLOCK) and SA-2 (CONVERSION-MAP);
   does not write criteria
2. **Author** — reads Spec Analyst output; writes failure modes and criteria; references SA-1 fields
   and SA-2 row identifiers; does not re-derive them
3. **Auditor** — reads all Author criteria as a set; produces consolidated audit table

Your output follows a fixed role-execution template. Spec Analyst outputs appear first.

**Output template (follow this order exactly):**

```
--- SPEC ANALYST ---
SA-1: SCHEMA BLOCK
SA-2: CONVERSION-MAP
--- END SPEC ANALYST ---

--- AUTHOR ---
A-1: Failure Modes
[AUTHOR ENTRY GATE]
A-2: Essential Criteria
A-3: Recommended and Aspirational Criteria
--- END AUTHOR ---

--- STRUCTURAL VERIFICATION ---

--- AUDITOR ---
AU-1: Audit Table
AU-2: Cross-Criterion Pattern Note
AU-3: Auditor Calibration Pair
--- END AUDITOR ---

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### --- SPEC ANALYST ---

You are the Spec Analyst. Your sole output is SA-1 and SA-2. Do not write failure modes or criteria.

#### SA-1: SCHEMA BLOCK

Read the target skill name and output contract from the skill spec.

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

Scan the skill spec for specificity prohibitions ("not generic", "specific to input",
"tailored to X", "not boilerplate", or any "output must not ___" / "must be specific to ___").

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST COMPLETION GATE — DO NOT hand off to Author until:**

- [ ] SA-1 complete with all fields filled (no TBD)
- [ ] SA-2 has one row per prohibition found, OR empty declaration written
- [ ] Each PASS condition is scoreable by inspection
- [ ] Each FAIL condition is the Boolean complement of PASS

### --- END SPEC ANALYST ---

---

### --- AUTHOR ---

You are the Author. The Spec Analyst outputs (SA-1 and SA-2) are above.
Do not re-derive them. Reference them by artifact identifier (SA-1, SA-2, CM-NN).

#### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT advance to the Author Entry Gate until failure mode minimum is met.**

---

#### AUTHOR ENTRY GATE

**DO NOT BEGIN WRITING CRITERIA.** Before writing any criterion, write the following status block:

```
AUTHOR STATUS CHECK
SA-1 SCHEMA BLOCK: [PRESENT — skill field = [value]] / [ABSENT — cannot proceed]
SA-2 CONVERSION-MAP: [PRESENT — [N] rows: CM-01 [quoted prohibition], ..., CM-N [quoted prohibition]]
                   / [EMPTY DECLARATION — no prohibitions found]
                   / [ABSENT — cannot proceed]
Failure modes: [PRESENT — [N] blocking, [N] degrading] / [INSUFFICIENT — cannot proceed]
Category values from SA-1: [list 3 identifiable in this skill: ___, ___, ___]
```

**DO NOT BEGIN WRITING CRITERIA until every field above reads PRESENT, EMPTY DECLARATION, or a
confirmed-sufficient count. Any ABSENT or INSUFFICIENT halts Author execution. Write the missing
artifact before proceeding.**

---

#### A-2: Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.
Category and field values must be drawn from SA-1 output_contract closed lists.

**Sub-step A2a — Draft pass condition.**

If this criterion addresses a specificity requirement: "This criterion operationalizes SA-2
row CM-[N]: [prohibition text]." Cite the row identifier — do not re-derive.

**Sub-step A2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [from A2a]
SA-2 row cited: [CM-NN] / [not a specificity criterion]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration from SA-1
  output_contract]
```

**Sub-step A2c — Produce the CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD; references
  target skill by name or SA-1 output-contract term]
```

**Sub-step A2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

After both confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition from INERTIA-RECORD] |
```

Repeat A2a–A2d for each essential criterion.

---

#### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table. Category values from SA-1.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### --- END AUTHOR ---

---

### --- STRUCTURAL VERIFICATION ---

Scan Author A-2 output for heading patterns. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block, then re-check. Auditor cannot begin until all confirmed.

### --- END STRUCTURAL VERIFICATION ---

---

### --- AUDITOR ---

You are the Auditor. Read all `### CRITERION [C-NN]` blocks from A-2 before writing any output.
Do not write rows one at a time.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column across all rows. Write one sentence: are discriminating
elements varied across types (count, field name, structural pattern, enumeration) or clustered?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
GENERIC: [weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE — DO NOT proceed to Final Rubric until:**

- [ ] AU-1 complete with all essential criteria as rows
- [ ] Every essential criterion: Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] AU-2 written

### --- END AUDITOR ---

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Category and field values drawn from SA-1 output_contract.
Substitute Auditor-revised conditions where Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-02 — Role Sequence: Identifier Citation in Canonical Criterion Row

**axis:** role-sequence
**hypothesis:** C-19 requires CM-NN and SA-NN identifiers to appear in criterion text — specifically
in the canonical criterion row's Pass Condition field, not just in the INERTIA-RECORD working block.
R5 V-03 passes C-19 because Author instructions say "cite the row identifier"; however, if the
model writes "operationalizes CM-02" in the INERTIA-RECORD but then writes a clean standalone
pass condition in the CRITERION table row, C-19 fails (the canonical artifact has lost the
identifier). V-02 closes this gap by requiring the CRITERION row's Pass Condition to begin with or
include the SA-2 row citation if the criterion is a specificity criterion. The canonicalization
step explicitly instructs the model to carry the identifier forward, not drop it. Failure condition:
if C-19 still fails, the model writes the identifier in the INERTIA-RECORD but strips it from the
CRITERION table row, treating the table as a "clean final output" format. Counter: add an explicit
"criterion is a specificity criterion — Pass Condition MUST include CM-NN citation verbatim" note
in the CRITERION block template.

---

You are building a scoring rubric for a Signal skill. Two roles execute in sequence:

1. **Spec Analyst** — reads the skill spec; produces SA-1 (SCHEMA BLOCK) and SA-2 (CONVERSION-MAP
   with row identifiers CM-01 through CM-N); does not write criteria
2. **Author** — reads Spec Analyst output; writes failure modes and criteria; cites SA-2 row
   identifiers (CM-NN) in criterion text where applicable

A third role, **Auditor**, reads all Author criteria as a set before producing the audit table.

**Why identifier citation in the criterion row?**

The CONVERSION-MAP row identifier (CM-NN) is the traceability link between a specificity
prohibition and its operationalization as a criterion. If the identifier appears only in the
Author's working notes (INERTIA-RECORD) but not in the canonical criterion row, the link is
invisible to a downstream evaluator who reads only the Final Rubric. Traceability requires the
identifier to appear where the criterion is stored, not where it was derived.

---

### --- SPEC ANALYST ---

You are the Spec Analyst. Produce SA-1 and SA-2 only. Do not write failure modes or criteria.

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

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If no prohibitions found: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST COMPLETION GATE — DO NOT hand off to Author until:**

- [ ] SA-1 complete with all fields filled (no TBD)
- [ ] SA-2 has one row per prohibition, OR empty declaration written
- [ ] Each PASS scoreable by inspection; each FAIL is Boolean complement of PASS

### --- END SPEC ANALYST ---

---

### --- AUTHOR ---

You are the Author. Do not re-derive SA-1 or SA-2. Reference them by identifier.

#### A-1: Failure Modes

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**AUTHOR ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] Spec Analyst Completion Gate is cleared (confirmed above)
- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] At least 3 distinct category_values from SA-1 are identifiable (list: ___, ___, ___)

---

#### A-2: Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step A2a — Identify criterion type and draft pass condition.**

First: is this criterion a specificity criterion? A specificity criterion operationalizes a
prohibition from SA-2.

- If YES: state "Specificity criterion — operationalizes SA-2 CM-[N]: [quoted prohibition]."
  Draft the pass condition using the SA-2 PASS state as the starting point.
- If NO: state "Not a specificity criterion." Draft the pass condition from the failure modes.

**Sub-step A2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Criterion type: [specificity (CM-NN) / non-specificity]
Draft condition: [from A2a]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration from SA-1
  output_contract]
```

**Sub-step A2c — Produce the CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element; references target skill by name
  or SA-1 output-contract term]
```

**Sub-step A2d — Per-criterion forward gate and CRITERION row.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

After both confirmed, record the CRITERION row. **Citation rule:** if this is a specificity
criterion (Criterion type = specificity), the Pass Condition field in the table row MUST include
the CM-NN reference: write the pass condition as "[final condition]; operationalizes SA-2 CM-[N]."
If not a specificity criterion, omit the citation.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition]; [operationalizes SA-2 CM-N if specificity criterion] |
```

Repeat A2a–A2d for each essential criterion.

---

#### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table. Category values from SA-1.
Apply the same citation rule: specificity criteria include CM-NN in Pass Condition.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### --- END AUTHOR ---

---

### --- STRUCTURAL VERIFICATION ---

Scan A-2 output for heading patterns. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block, then re-check. Auditor cannot begin until all confirmed.

Also verify: for each CRITERION row whose INERTIA-RECORD shows "Criterion type: specificity
(CM-NN)", confirm the Pass Condition column includes "operationalizes SA-2 CM-N". If absent,
revise the row before proceeding.

### --- END STRUCTURAL VERIFICATION ---

---

### --- AUDITOR ---

Read all `### CRITERION [C-NN]` blocks before writing any audit output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
GENERIC: [weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE — DO NOT proceed to Final Rubric until:**

- [ ] AU-1 complete with all essential criteria
- [ ] Every essential criterion: Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] AU-2 written

### --- END AUDITOR ---

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. For specificity criteria, Pass Condition MUST include
CM-NN citation. Substitute Auditor-revised conditions where Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-03 — Phrasing Register: Formal-Imperative Phase Declarations

**axis:** phrasing-register
**hypothesis:** C-20 requires imperative blocking language. R5 V-05 uses checklist-advisory
format: "DO NOT begin writing criteria until: [ ] gate item". The checklist format is still
advisory — the model can interpret unchecked boxes as "to be filled later" and proceed. V-03
replaces checklist-advisory gates with hard-stop declarative language at every phase boundary.
Phase transitions require the model to write an explicit PHASE STATUS declaration before
proceeding — a machine-readable status line ("AUTHOR: BLOCKED / CLEAR") that the model must
output, making it impossible to proceed without committing to a status. If the model writes
"AUTHOR: BLOCKED" and then begins criteria, the structural violation is immediately detectable
by string scan. If it writes "AUTHOR: CLEAR" without the prerequisites being met, the violation
is detectable by content check. This register shift tests whether imperative-declarative phrasing
improves compliance with phase-boundary rules independently of the artifacts named. Failure
condition: if C-20 still fails, the model writes "AUTHOR: CLEAR" prematurely without the
required artifacts. Counter: require the CLEAR declaration to include the artifact inventory
inline — "AUTHOR: CLEAR [SA-1: present, SA-2: CM-01 through CM-N present]" — making a
false CLEAR detectable by inspection.

---

You are building a scoring rubric for a Signal skill. Three roles execute in sequence: Spec
Analyst, Author, Auditor. Each role transition is governed by a PHASE STATUS declaration.
A role may not produce output until it writes its PHASE STATUS and that status is OPEN.
A role signals completion by writing its PHASE STATUS as CLOSED. The next role may not open
until the previous role is CLOSED.

**Output template (follow this order exactly):**

```
SPEC ANALYST: OPEN
  SA-1: SCHEMA BLOCK
  SA-2: CONVERSION-MAP
SPEC ANALYST: CLOSED — [inventory: SA-1 complete, SA-2 N rows / empty]

AUTHOR ENTRY CHECK
AUTHOR: [BLOCKED / OPEN]
  A-1: Failure Modes
  A-2: Essential Criteria
  A-3: Recommended and Aspirational Criteria
AUTHOR: CLOSED — [inventory: N essential criteria, N recommended, N aspirational]

STRUCTURAL VERIFICATION: [PASS / FAIL — list any missing blocks]

AUDITOR: OPEN
  AU-1: Audit Table
  AU-2: Cross-Criterion Pattern Note
  AU-3: Auditor Calibration Pair
AUDITOR: CLOSED

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

**PHASE STATUS rules:**

- SPEC ANALYST: OPEN immediately — no prerequisites.
- SPEC ANALYST: CLOSED requires SA-1 and SA-2 complete. Write inventory inline with CLOSED.
- AUTHOR ENTRY CHECK: written after A-1. Lists each prerequisite with status.
- AUTHOR: OPEN — write only if every line of AUTHOR ENTRY CHECK shows [PRESENT] or [MET].
  If any line shows [ABSENT] or [NOT MET], write AUTHOR: BLOCKED and stop.
- AUTHOR: CLOSED requires A-2 essential criteria complete. Write inventory inline.
- AUDITOR: OPEN only after STRUCTURAL VERIFICATION shows PASS.
- AUDITOR: CLOSED after AU-3 is written.

---

### SPEC ANALYST: OPEN

You are the Spec Analyst. Read the skill spec. Produce SA-1 and SA-2.

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

#### SA-2: CONVERSION-MAP

Scan for specificity prohibitions. Produce one row per prohibition.

| Row | Prohibition (quoted) | Boolean test | PASS | FAIL |
|-----|---------------------|--------------|------|------|
| CM-01 | [quote] | [yes/no] | [observable pass] | [Boolean complement] |

If none: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — inventory: SA-1 [complete / incomplete — list missing fields],
SA-2 [[N] rows: CM-01 ... CM-N / empty declaration written]**

---

### AUTHOR ENTRY CHECK

List each prerequisite with its status:

```
SA-1 SCHEMA BLOCK:        [PRESENT — skill = [value]] / [ABSENT]
SA-2 CONVERSION-MAP:      [PRESENT — [N] rows] / [EMPTY DECLARATION] / [ABSENT]
Failure modes — blocking: [MET — [N] blocking] / [NOT MET — only [N] found]
Failure modes — degrading: [MET — [N] degrading] / [NOT MET — only [N] found]
Category coverage:        [MET — [C1], [C2], [C3] identifiable] / [NOT MET]
```

**AUTHOR: OPEN** (write only if every line above shows PRESENT, EMPTY DECLARATION, or MET)
**AUTHOR: BLOCKED** (write if any line shows ABSENT or NOT MET — write the missing item, then re-run AUTHOR ENTRY CHECK)

---

### A-1: Failure Modes

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

---

### A-2: Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step A2a — Draft pass condition.**

If specificity criterion: cite SA-2 row. "Operationalizes SA-2 CM-[N]: [prohibition]."

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [from A2a]
SA-2 row cited: [CM-NN] / [not a specificity criterion]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration]
CRITERION GATE: [OPEN — inertia test = NO] / [BLOCKED — inertia test still YES]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [Status-Quo Rubric — weakest condition applying to any artifact]
GROUNDED: [condition naming the skill-specific element]
```

**Sub-step A2d — Record criterion.** Only if CRITERION GATE = OPEN and CALIBRATION-PAIR is present.

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat A2a–A2d for each essential criterion.

---

### A-3: Recommended and Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR: CLOSED — inventory: [N] essential criteria (C-01 through C-[N]), [N] recommended,
[N] aspirational**

---

### STRUCTURAL VERIFICATION

Scan A-2 for heading patterns. Pattern scan only.

For each essential C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present with CRITERION GATE = OPEN
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present
```

**STRUCTURAL VERIFICATION: PASS** (all patterns confirmed) /
**STRUCTURAL VERIFICATION: FAIL — missing: [list]** (write missing blocks, re-check)

---

### AUDITOR: OPEN

Read all `### CRITERION [C-NN]` blocks before writing any audit output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

#### AU-2: Cross-Criterion Pattern Note

One sentence on discriminating element variety vs. clustering across all rows.

#### AU-3: Auditor Calibration Pair

```
GENERIC: [Status-Quo Rubric — weakest surviving form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR: CLOSED** (only after AU-1 complete, all Inertia Tests = NO, AU-2 written)

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-04 — Lifecycle Emphasis × Role Sequence (V-01 × V-02, Combination)

**axis:** lifecycle-emphasis × role-sequence
**hypothesis:** V-01 adds a named-artifact Author Entry Gate with imperative blocking language
targeting C-20. V-02 adds CM-NN citation in canonical CRITERION row Pass Condition targeting C-19.
These mechanisms operate at non-competing lifecycle positions: C-20 fires at the Author phase
boundary (before any criterion is written); C-19 fires at criterion canonicalization (when the
CRITERION row is recorded). Neither can produce the other's effect. Combined, V-04 should satisfy
both C-19 and C-20 simultaneously. The Spec Analyst role (from R5 V-03/V-05) is retained because
it is the source of the named artifacts that both gates reference. Failure condition: if C-19 fails
despite citation in CRITERION rows, the Final Rubric reproduction step strips the citation ("clean
final output" behavior). Counter: add explicit citation-retention rule to the Final Rubric section:
"reproduce Pass Condition including any CM-NN citation verbatim — do not simplify." If C-20 fails
despite named-artifact gate, the AUTHOR STATUS CHECK is written but the model writes "AUTHOR: OPEN"
before confirming artifact presence. Counter: add a "HALT — do not write AUTHOR: OPEN until SA-1
and SA-2 are confirmed present" note to the gate.

---

You are building a scoring rubric for a Signal skill. Three roles execute in sequence:

1. **Spec Analyst** — reads the skill spec; produces SA-1 (SCHEMA BLOCK) and SA-2 (CONVERSION-MAP
   with identifiers CM-01 through CM-N); does not write criteria
2. **Author** — reads Spec Analyst output; writes failure modes and criteria; cites SA-2 row
   identifiers in criterion text; does not re-derive them
3. **Auditor** — reads all Author criteria as a set; produces consolidated audit table

Your output follows a fixed role-execution template.

**Output template (follow this order exactly):**

```
--- SPEC ANALYST ---
SA-1: SCHEMA BLOCK
SA-2: CONVERSION-MAP
--- END SPEC ANALYST ---

--- AUTHOR ---
A-1: Failure Modes
[AUTHOR ENTRY GATE — NAMED ARTIFACT BLOCK]
A-2: Essential Criteria
A-3: Recommended and Aspirational Criteria
--- END AUTHOR ---

--- STRUCTURAL VERIFICATION ---

--- AUDITOR ---
AU-1: Audit Table
AU-2: Cross-Criterion Pattern Note
AU-3: Auditor Calibration Pair
--- END AUDITOR ---

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### --- SPEC ANALYST ---

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

#### SA-2: CONVERSION-MAP

Scan for specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [Boolean complement] |

If none: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST COMPLETION GATE — DO NOT hand off to Author until:**

- [ ] SA-1 complete with all fields filled (no TBD)
- [ ] SA-2 has one row per prohibition, OR empty declaration written
- [ ] Each PASS scoreable by inspection; each FAIL is Boolean complement of PASS

### --- END SPEC ANALYST ---

---

### --- AUTHOR ---

You are the Author. Do not re-derive SA-1 or SA-2.

#### A-1: Failure Modes

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

---

#### AUTHOR ENTRY GATE — NAMED ARTIFACT BLOCK

**DO NOT BEGIN WRITING CRITERIA.** Write the following artifact inventory now:

```
ARTIFACT INVENTORY
SA-1 SCHEMA BLOCK:   [PRESENT] skill = [value], fields = [list] / [ABSENT — cannot proceed]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — [CM-01: prohibition-summary], ..., [CM-N: prohibition-summary]
                   / [EMPTY DECLARATION — no prohibitions found in spec]
                   / [ABSENT — cannot proceed]
Failure modes:       [PRESENT] [N] blocking, [N] degrading / [INSUFFICIENT — cannot proceed]
Category coverage:   [PRESENT] 3 identifiable: [C1], [C2], [C3] / [INSUFFICIENT — cannot proceed]
```

**AUTHOR ACCESS: [GRANTED / DENIED]**

Write GRANTED only if all four inventory lines above show PRESENT or EMPTY DECLARATION.
Write DENIED and stop if any line shows ABSENT or INSUFFICIENT. Write the missing artifact, then
re-run ARTIFACT INVENTORY.

**DO NOT advance to A-2 until AUTHOR ACCESS reads GRANTED.**

---

#### A-2: Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.
Category values must come from SA-1 output_contract.

**Sub-step A2a — Identify type and draft pass condition.**

Specificity criterion: one whose pass condition directly operationalizes a prohibition from SA-2.

- If specificity: "Criterion type: specificity. Operationalizes SA-2 CM-[N]: [quoted prohibition]."
  Draft pass condition using SA-2 PASS state as the starting point.
- If not specificity: "Criterion type: non-specificity." Draft from failure modes.

**Sub-step A2b — INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Criterion type: [specificity — CM-NN] / [non-specificity]
Draft condition: [from A2a]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration from SA-1]
```

**Sub-step A2c — CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element; references target skill or SA-1 term]
```

**Sub-step A2d — Forward gate and CRITERION row.**

**DO NOT record this criterion and DO NOT advance until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

Record the CRITERION row. **Citation rule for specificity criteria:** the Pass Condition field
must include the SA-2 identifier: "[final condition]; operationalizes SA-2 CM-[N]."

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition][; operationalizes SA-2 CM-N if specificity] |
```

Repeat A2a–A2d for each essential criterion.

---

#### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table. Category values from SA-1.
Apply citation rule: specificity criteria include CM-NN in Pass Condition.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### --- END AUTHOR ---

---

### --- STRUCTURAL VERIFICATION ---

Scan A-2 for heading patterns.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN] present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN] present
```

Also verify: ARTIFACT INVENTORY block is present and AUTHOR ACCESS = GRANTED.
Also verify: for each specificity criterion (INERTIA-RECORD shows "CM-NN"), the CRITERION row
Pass Condition column includes "operationalizes SA-2 CM-N".

Write any missing blocks, then re-check. Auditor cannot begin until all verified.

### --- END STRUCTURAL VERIFICATION ---

---

### --- AUDITOR ---

Read all `### CRITERION [C-NN]` blocks from A-2 before writing any audit output.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

#### AU-2: Cross-Criterion Pattern Note

One sentence on discriminating element variety vs. clustering.

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
GENERIC: [Status-Quo Rubric — weakest surviving form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE — DO NOT proceed to Final Rubric until:**

- [ ] AU-1 complete with all essential criteria
- [ ] Every essential criterion: Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] AU-2 written

### --- END AUDITOR ---

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce complete criteria table. For specificity criteria, Pass Condition MUST include CM-NN
citation — do not simplify or omit it during reproduction. Substitute Auditor-revised conditions
where Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-05 — Lifecycle Emphasis × Role Sequence × Phrasing Register + Inertia Framing (Full Combination)

**axis:** lifecycle-emphasis × role-sequence × phrasing-register × inertia-framing
**hypothesis:** V-04 (C-19 + C-20) is the combination anchor. V-05 adds two additional axes from
the R5 roadmap: phrasing-register (formal-imperative phase declarations from V-03) and inertia-
framing (the Status-Quo Rubric named as a concrete entity in the opening framing, not just as an
implicit foil in CALIBRATION-PAIR). The Status-Quo Rubric framing tests C-07 (specificity test
present): if the evaluator is told upfront "there is a named competitor — the Status-Quo Rubric —
that your output must beat," the specificity pressure is front-loaded rather than embedded in a
sub-step instruction. The formal-imperative register (PHASE STATUS declarations) tests whether
the AUTHOR: BLOCKED / OPEN declarative format (from V-03) adds compliance beyond the named-
artifact gate from V-04. Failure condition: if V-05 does not improve over V-04 on C-19 and C-20,
the additional framing and register changes are redundant and can be excluded from the base. If
V-05 improves C-07 specificity but not C-19/C-20, the inertia-framing axis is orthogonal to the
gate/citation mechanisms and should be tested in isolation next round.

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
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
golden_threshold: "all essential pass AND composite >= 80"
```

#### SA-2: CONVERSION-MAP

Scan for specificity prohibitions.

| Row | Prohibition (quoted) | Boolean test | PASS | FAIL |
|-----|---------------------|--------------|------|------|
| CM-01 | [quote] | [yes/no] | [observable pass] | [Boolean complement] |

If none: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST: CLOSED — SA-1: [complete / incomplete], SA-2: [[N] rows / empty declaration]**

---

### ARTIFACT INVENTORY

Confirm each artifact is present before Author opens:

```
SA-1 SCHEMA BLOCK:   [PRESENT] skill=[value], fields=[list] / [ABSENT]
SA-2 CONVERSION-MAP: [PRESENT] [N] rows — CM-01: [summary], ..., CM-N: [summary]
                   / [EMPTY DECLARATION]
                   / [ABSENT]
Failure modes:       [PRESENT — will be written in A-1, prerequisite met by SPEC ANALYST: CLOSED]
Category coverage:   [PRESENT — 3 identifiable: [C1], [C2], [C3]] / [INSUFFICIENT]
```

**AUTHOR: OPEN** — write only if SA-1 PRESENT, SA-2 PRESENT or EMPTY DECLARATION, category
coverage PRESENT.

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

The Status-Quo Rubric is your foil. It writes conditions like "output is complete" and "output
follows instructions." Every criterion you write must include a pass condition that beats the
Status-Quo Rubric — it must name a count, a field name, a structural pattern, or an enumeration
from SA-1 output_contract that the Status-Quo Rubric cannot produce.

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

Column note: *Status-Quo Test* replaces *Inertia Test* from prior rounds. The question is
equivalent: "Could the Status-Quo Rubric produce this condition?" NO = grounded. YES = revise.

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
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## Anchor Designation

**Anchor: V-04**

V-04 is designated the combination anchor for Round 6.

**Structural impact:** V-04 targets C-19 and C-20 simultaneously — the two new aspirational
criteria in v6. The mechanisms are non-competing:

- Named Artifact Gate (V-01): fires at the Author Entry Gate; requires ARTIFACT INVENTORY with
  SA-1 and SA-2 by identifier before AUTHOR ACCESS = GRANTED; detectable by inventory-block scan
- Identifier citation in canonical row (V-02): fires at CRITERION row recording; requires CM-NN
  in Pass Condition for specificity criteria; detectable by citation scan in Final Rubric

Neither mechanism can produce the other's effect. The gate controls phase entry; the citation
rule controls row content. A prompt can have one without the other — V-01 has the gate but not
the citation rule; V-02 has the citation rule but a weaker gate.

**Isolation quality:** V-01 and V-02 isolate C-20 and C-19 respectively. If V-04 passes both
while V-01 only passes C-20 and V-02 only passes C-19, the combination is confirmed additive.
If V-04 fails one that its single-axis variation passed:

- C-20 fails in V-04 but passes in V-01: adding the citation rule (V-02) may interfere with gate
  compliance. Investigate: does the ARTIFACT INVENTORY step conflict with the type-identification
  step in A2a? They operate at different points — gate fires before A-2 begins, type identification
  fires per-criterion. If interaction exists, it is ordering, not content.
- C-19 fails in V-04 but passes in V-02: the named-artifact gate adds overhead before A-2 that
  the model may compensate for by simplifying criterion recording. Investigate: are CM-NN citations
  present in INERTIA-RECORD but stripped from CRITERION rows in V-04?

**Detectable interaction with V-05:**

If V-05 improves over V-04 on C-07 (specificity test) but not on C-19/C-20, the Status-Quo Rubric
framing and formal-imperative register are orthogonal to the gate/citation mechanisms — they improve
specificity quality but do not affect structural compliance. If V-05 improves C-20 beyond V-04,
the PHASE STATUS declaration format (AUTHOR: OPEN / BLOCKED) adds compliance beyond the named-
artifact inventory approach. If V-05 offers no improvement, V-04 is the ceiling and the additional
framing is cosmetic.

---

## Combination Roadmap (for Round 7)

**R6 outcome scenarios:**

| Scenario | Expected Outcome | Round 7 Action |
|----------|-----------------|----------------|
| V-04 reaches Golden | C-19 and C-20 both fixed | Run V-05 to test inertia-framing gain; V-04 becomes new base |
| V-01 passes C-20, V-02 fails C-19 | Named-artifact gate works but citation doesn't survive canonicalization | Investigate: does Final Rubric reproduction strip CM-NN from Pass Condition? Tighten: add explicit "retain CM-NN verbatim" note to FINAL RUBRIC section |
| V-02 passes C-19, V-01 fails C-20 | Citation in canonical row works but gate is still advisory | Investigate: does ARTIFACT INVENTORY produce AUTHOR ACCESS = GRANTED without checking SA-2 row count? Tighten: require SA-2 row identifiers to be listed in ARTIFACT INVENTORY (not just row count) |
| Both V-01 and V-02 fail | Neither mechanism sufficient alone | Investigate whether scoring definitions of C-19/C-20 are tighter than what the prompts enforce — may require rubric definition clarification on what "criterion text" means (canonical row only vs. INERTIA-RECORD included) |
| V-03 adds compliance beyond V-01 for C-20 | PHASE STATUS declaration format materially improves gate compliance | Absorb AUTHOR: OPEN / BLOCKED declarative format as E-1 for Round 7 rubric update (C-21); add to V-04 base |
| V-05 improves C-07 specificity beyond V-04 | Status-Quo Rubric naming front-loads specificity pressure | The inertia-framing axis is real; test as single-axis isolation in Round 7 to confirm |
| V-05 adds no improvement over V-04 | Phrasing register and Status-Quo naming are redundant | Retire both as standalone axes; retain only if combination evidence reverses this finding |

**Combination priority for Round 7:**

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-04 base + citation-retention in Final Rubric | lifecycle × role-sequence + reproduction rule | C-19, C-20 | 1 | If canonicalization strips CM-NN, the reproduction step needs an explicit retention instruction |
| V-04 base + SA-2 row enumeration in ARTIFACT INVENTORY | lifecycle × role-sequence + inventory depth | C-20 | 2 | If ARTIFACT INVENTORY lists row count but not identifiers, it does not satisfy C-20's named-artifact requirement |
| V-05 inertia-framing solo | inertia-framing | C-07 | 3 | Isolate Status-Quo Rubric naming to confirm C-07 contribution independently |
