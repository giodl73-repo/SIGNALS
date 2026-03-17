# quest-variate Variate — Round 9

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v9 (C-01 through C-32; essential C-01–C-05)
**Round:** R9 — 4 single-axis passes + 1 combination pass (C-04 combination exception applies to V-05)

---

## Round 9 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | output-format | single-axis | COLUMN CONTRACT gains `Axis Cost Rationale` column; TABLE SCHEMA header gains that column; evaluation order section requires non-empty Axis Cost Rationale per row with a per-axis structural reason — not a tier label alone | C-30 |
| V-02 | lifecycle-emphasis | single-axis | NON-SUPPRESSION INVARIANT CO-LOCATED annotation embedded inside the 4a execution block AND the 4b execution block — making the non-suppression guarantee inseparable from the action it governs at the execution site, not only in the role definition or preamble | C-31 |
| V-03 | phrasing-register | single-axis | Audit output template phrasing changed from observational labels ("PASS / FAIL") to prescriptive enforcement labels ("PASS / FAIL → FAIL requires: [specific remediation action]") for each checkpoint result line and each per-row population check result | C-32 |
| V-04 | role-sequence | single-axis | Axis Cost Auditor role added (role 6, after Findings Synthesizer); verifies that every row in the evaluation order table carries a per-axis structural cost reason in its Evaluation Cost cell, not just a tier label; Findings Synthesizer may not declare item 3 complete until Axis Cost Auditor passes | C-30 |
| V-05 | output-format × lifecycle-emphasis | combination (R9 Priority 1 — V-01 R9 Axis Cost Rationale column × V-02 R9 Execution-Site Co-location) | Combines COLUMN CONTRACT Axis Cost Rationale column (V-01 R9) with NON-SUPPRESSION INVARIANT CO-LOCATED annotations inside 4a and 4b execution blocks (V-02 R9); the column makes C-30 checkable at row level; the co-located annotations make C-31 checkable at execution-template level | C-30, C-31 |

**Anchor designation (C-12):** V-01. See anchor section at end of document.

---

## V-01 — Output Format: Axis Cost Rationale Column

**axis:** output-format

**hypothesis:**
- criterion: C-30 (Evaluation-order axis-cost table)
- direction: C-30 pass rate increases from zero (criterion born R9) to measurable rate; every run produces an evaluation order table with a dedicated Axis Cost Rationale column where each row carries a per-axis structural reason for its tier position and evaluation cost — not a generic tier rule applied in aggregate prose
- mechanism: The Axis Cost Rationale column is declared in the COLUMN CONTRACT before any evaluation order table is written — writing a table without a completed Column Contract is structurally prohibited by the STRUCTURAL INCOMPLETENESS ASSERTION; therefore the Axis Cost Rationale column is a required input to writing any evaluation order table; a generator cannot produce a conforming evaluation order table without first declaring the Axis Cost Rationale column in the Column Contract, and cannot leave any row's Axis Cost Rationale cell empty without violating the REQUIRED annotation in the evaluation order section; the per-row rationale cell is a required structural input to each evaluation order table row
- failure-condition:
    round-label:      R8
    source-variation: V-05
    criterion-born:   C-30
    evaluative-label:
      rank-label:       "strongest combination in R8 — combined NON-SUPPRESSION INVARIANT CONTRACT preamble (V-01 R8) with mandatory per-checkpoint labeled result template (V-04 R8), yet still C-10 PARTIAL due to absence of per-row axis-cost rationale cells in evaluation order table"
      quality-dimension: "most complete demonstration of the C-10 ordering gap in the presence of a fully operational audit structure — established that an evaluation order table can have all structural columns (Tier, Axis, Evaluation Cost, Independence, Cross-Round Dependency, Catalog Source) while still failing C-30 because the tier ordering logic is stated in aggregate prose outside the table rather than as a per-row rationale cell; the combination context made the gap maximally visible by eliminating all other sources of partial credit"
    consequence: if C-30 does not pass with an explicit Axis Cost Rationale column in the Column Contract, the column schema adds overhead without improving per-row rationale coverage; combine with lifecycle-emphasis (V-02 R9) to add execution-site non-suppression co-location for simultaneous C-30 + C-31 coverage

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern — SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does
not explicitly state the non-suppression invariant is structurally incomplete and
must be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier                 <- priority tier (Tier 1 = evaluate first)
  [ ] V                    <- variation label (V-01 through V-0N)
  [ ] Axis                 <- canonical axis name
  [ ] Evaluation Cost      <- low / medium / high + one-line explanation
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural
                              reason this variation is at this cost level — not a
                              generic tier rule; (2) independence claim — why this
                              variation is independent or what prior-round result
                              it depends on. A cell containing only "low" or
                              "Tier 1" with no per-axis reason is structurally
                              incomplete.
  [ ] Independence         <- yes / partial / no + dependency note
  [ ] Cross-Round Dependency  <- Round + Variation + Metric, or "none"
  [ ] Catalog Source       <- required attribution column; every row must name the
                              Step 3 row from which this entry was derived.
                              Format:
                                Independent: "Step 3 row V-NN: independent"
                                Dependent:   "Step 3 row V-NN: depends on [R/V/M]"

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position.
  Must state: (a) the structural property of this axis that drives the cost level
  (e.g., "one-line template change, no role dependencies"); (b) why this variation
  is independent or what prior-round result it requires. A cell containing only a
  cost level or tier label without a per-axis reason is structurally incomplete —
  rewrite before committing the table.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Format per Column Contract above. Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason. A row with a generic rationale ("independent, low
cost") that applies equally to all variations does not satisfy this requirement.
A row with a blank "Axis Cost Rationale" is structurally incomplete — rewrite
before committing the table.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical
   list. Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete — return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 — DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Axis Cost Rationale" column is explicitly named in the contract: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL — name failing item]."

   PASS 2 — POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value is non-blank and contains a per-axis reason: yes / no
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing — rewrite required].
     V-NN Catalog Source: [populated / blank — rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS — all rows populated / FAIL — list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes.

STEP 1 — SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 — VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN — [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism — use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN — the round containing the comparison baseline event]
    source-variation: [V-NN — the specific variation in that round]
    criterion-born:   [C-NN — the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance
                         in its round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or
                          pedagogically excellent — the specific quality
                          demonstrated. NOT a restatement of rank-label.
                          A blank or redundant quality-dimension triggers a
                          required rewrite before this citation block is committed.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY — every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 — CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Column rules:
- "Comparative Claim": quote or paraphrase the hypothesis claim that references a
  prior-round result. Write "none" if no such claim exists.
- "Prior-Round Result Required": the metric that must exist before the claim can be
  verified. Write "n/a" if independent.
- "Round + Variation + Metric": "R[round] / V-NN / [metric]", or "n/a" if independent.
- "Independent": "yes" if no prior-round result required; "no — depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete — return to Step 2 before proceeding.

STEP 4 — FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects
model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis —
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW — one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here — after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have a non-blank Axis Cost Rationale value with a per-axis structural
reason. A generic rationale that applies equally to all rows does not satisfy the
per-row requirement.

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" — ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" — ordered after their dependency rounds.

A blank or generic Axis Cost Rationale in any row is a required rewrite before this
step is complete.

[Column Schema Auditor Pass 2 emitted here — after item 3 is written.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a — DECLARATION CHECK:
  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  Declaration Check Result: PASS (all items yes) / FAIL (name failing item)

  NOTE: A 4a FAIL does not suppress 4b. Advance to 4b regardless of 4a result.

4b — POPULATION CHECK:

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  (One row per variation. "Row Result: populated" if both cells non-blank with
   per-axis reason. "Row Result: incomplete — rewrite required" if either cell
   blank or generic.)

  Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition — one sentence each.

---

## V-02 — Lifecycle Emphasis: Execution-Site Non-Suppression Co-location

**axis:** lifecycle-emphasis

**hypothesis:**
- criterion: C-31 (Execution-site non-suppression co-location)
- direction: C-31 pass rate increases from zero (criterion born R9) to measurable rate; every run produces a compliance audit where the non-suppression invariant is embedded as a required inline annotation inside the 4a execution block AND inside the 4b execution block — making the guarantee co-located with the action it governs so that a model following the execution template cannot omit it even if it ignores the role definition and preamble
- mechanism: The NON-SUPPRESSION INVARIANT CO-LOCATED annotation is embedded at the execution site inside the 4a checkpoint instructions — 4a's execution block cannot be followed without reading the annotation that 4b must execute regardless of 4a's result; the annotation is a required structural element of the 4a execution block; therefore a model following the 4a template has the invariant as a required input to completing the 4a block, and cannot produce a compliant 4a result without the co-located invariant being present; the 4b block similarly carries a co-located annotation asserting its own execution regardless of 4a outcome; the invariant is structurally inseparable from the execution actions it governs
- failure-condition:
    round-label:      R8
    source-variation: V-04
    criterion-born:   C-31
    evaluative-label:
      rank-label:       "strongest C-28 PARTIAL in R8 — non-suppression invariant present in role definition Independence Requirement but absent from execution template, most precisely locating the execution-site gap that C-31 formalizes"
      quality-dimension: "most diagnostic demonstration of role-definition vs execution-template gap — established that a non-suppression invariant in the role definition ('INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent') does not prevent a model from omitting the invariant at the execution site when it follows the template mechanically, because the template itself is silent on failure-state independence; the gap exists precisely because role definitions are setup commentary while execution templates are action directives"
    consequence: if C-31 does not pass with execution-site co-location, the inline annotations add structural verbosity without improving invariant compliance at the action level; combine with output-format (V-01 R9) to add the Axis Cost Rationale column for simultaneous C-30 + C-31 coverage

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern — SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does
not explicitly state the non-suppression invariant is structurally incomplete and
must be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier             <- priority tier (Tier 1 = evaluate first)
  [ ] V                <- variation label (V-01 through V-0N)
  [ ] Axis             <- canonical axis name
  [ ] Evaluation Cost  <- low / medium / high + one-line explanation
  [ ] Independence     <- yes / partial / no + dependency note
  [ ] Cross-Round Dependency  <- Round + Variation + Metric, or "none"
  [ ] Catalog Source   <- required attribution column; every row must name the
                          Step 3 row from which this entry was derived.
                          Format:
                            Independent: "Step 3 row V-NN: independent"
                            Dependent:   "Step 3 row V-NN: depends on [R/V/M]"

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Catalog Source column explicitly declared) produces structurally incomplete
output. The table must not be committed until the contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Format per Column Contract above. Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Catalog Source" value.
A row with a blank "Catalog Source" is structurally incomplete — rewrite before
committing the table.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical
   list. Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete — return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 — DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL — name failing item]."

   PASS 2 — POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Catalog Source: [populated / blank — rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS — all rows populated / FAIL — list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes.

STEP 1 — SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 — VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN — [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism — use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN — the round containing the comparison baseline event]
    source-variation: [V-NN — the specific variation in that round]
    criterion-born:   [C-NN — the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance
                         in its round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or
                          pedagogically excellent — the specific quality
                          demonstrated. NOT a restatement of rank-label.
                          A blank or redundant quality-dimension triggers a
                          required rewrite before this citation block is committed.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY — every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 — CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Column rules:
- "Comparative Claim": quote or paraphrase the hypothesis claim that references a
  prior-round result. Write "none" if no such claim exists.
- "Prior-Round Result Required": the metric that must exist before the claim can be
  verified. Write "n/a" if independent.
- "Round + Variation + Metric": "R[round] / V-NN / [metric]", or "n/a" if independent.
- "Independent": "yes" if no prior-round result required; "no — depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete — return to Step 2 before proceeding.

STEP 4 — FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects
model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis —
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW — one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here — after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have a non-blank Catalog Source value.

| Tier | V | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" — ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" — ordered after their dependency rounds.

A blank Catalog Source in any row is a required rewrite before this step is complete.

[Column Schema Auditor Pass 2 emitted here — after item 3 is written.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a — DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless
  of this checkpoint's result. A model following this execution template cannot
  omit 4b even if it ignores the preamble invariant or role definition. Absence
  of this annotation makes the 4a execution block structurally incomplete.

  [ ] Column Contract block present in output: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  Declaration Check Result: PASS (both items yes) / FAIL (name failing item)

  Advance to 4b regardless of this result. 4a FAIL does not suppress 4b.

4b — POPULATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: This checkpoint
  executes regardless of 4a result. A model following this execution template
  cannot suppress this checkpoint based on 4a outcome. Absence of this annotation
  makes the 4b execution block structurally incomplete.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Catalog Source Value | Row Result |
  |---|---------------------|------------|
  (One row per variation. "Row Result: populated" if Catalog Source non-blank.
   "Row Result: blank — rewrite required" if Catalog Source blank.)

  Population Check Result: PASS (all rows populated) / FAIL (list blank rows)

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition — one sentence each.

---

## V-03 — Phrasing Register: Per-Checkpoint Remediation Directive

**axis:** phrasing-register

**hypothesis:**
- criterion: C-32 (Per-checkpoint remediation directive)
- direction: C-32 pass rate increases from zero (criterion born R9) to measurable rate; every run produces a compliance audit where each checkpoint result line uses prescriptive enforcement phrasing that specifies the required remediation action on FAIL — making the audit output a compliance gate rather than an observation report
- mechanism: The audit output template in Step 4 item 4 uses mandatory prescriptive phrasing for each checkpoint result line: "4a Declaration Check: PASS / FAIL → FAIL requires: [specific action]" and "4b Population Check: PASS / FAIL → FAIL requires: [specific action]"; the FAIL-path directive is structurally embedded in the result line template — a generator cannot produce a conforming checkpoint result without also producing the remediation directive for the FAIL case, because the template itself requires the directive as part of the result line syntax; the prescriptive phrasing register is a required input to producing a compliant checkpoint result, making remediation directives unavoidable rather than optional
- failure-condition:
    round-label:      R8
    source-variation: V-04
    criterion-born:   C-32
    evaluative-label:
      rank-label:       "strongest C-29 implementation in R8 — mandatory per-checkpoint labeled result template with 'rewrite-required' enforcement directive, most directly demonstrating prescriptive vs observational audit phrasing"
      quality-dimension: "cleanest demonstration that audit output register determines whether the audit is an observation report or a compliance gate — established that labeling a checkpoint PASS/FAIL without specifying what must happen next leaves the audit consumer inferring the required response, while prescriptive FAIL-path directives make the audit self-contained and actionable; the phrasing register is the minimal change that converts observational labels into enforcement directives"
    consequence: if C-32 does not pass with prescriptive FAIL-path phrasing, the template adds label syntax overhead without converting the audit from observation to prescription; combine with output-format (V-01 R9) to add the Axis Cost Rationale column for simultaneous C-30 + C-32 coverage, making both the evaluation order and the audit output prescriptive at their respective levels

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern — SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does
not explicitly state the non-suppression invariant is structurally incomplete and
must be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier             <- priority tier (Tier 1 = evaluate first)
  [ ] V                <- variation label (V-01 through V-0N)
  [ ] Axis             <- canonical axis name
  [ ] Evaluation Cost  <- low / medium / high + one-line explanation
  [ ] Independence     <- yes / partial / no + dependency note
  [ ] Cross-Round Dependency  <- Round + Variation + Metric, or "none"
  [ ] Catalog Source   <- required attribution column; every row must name the
                          Step 3 row from which this entry was derived.
                          Format:
                            Independent: "Step 3 row V-NN: independent"
                            Dependent:   "Step 3 row V-NN: depends on [R/V/M]"

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Catalog Source column explicitly declared) produces structurally incomplete
output. The table must not be committed until the contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Format per Column Contract above. Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Catalog Source" value.
A row with a blank "Catalog Source" is structurally incomplete — rewrite before
committing the table.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical
   list. Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete — return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 — DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL — name failing item]."

   PASS 2 — POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Catalog Source: [populated / blank — rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS — all rows populated / FAIL — list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes.

STEP 1 — SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 — VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN — [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism — use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN — the round containing the comparison baseline event]
    source-variation: [V-NN — the specific variation in that round]
    criterion-born:   [C-NN — the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance
                         in its round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or
                          pedagogically excellent — the specific quality
                          demonstrated. NOT a restatement of rank-label.
                          A blank or redundant quality-dimension triggers a
                          required rewrite before this citation block is committed.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY — every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 — CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Column rules:
- "Comparative Claim": quote or paraphrase the hypothesis claim that references a
  prior-round result. Write "none" if no such claim exists.
- "Prior-Round Result Required": the metric that must exist before the claim can be
  verified. Write "n/a" if independent.
- "Round + Variation + Metric": "R[round] / V-NN / [metric]", or "n/a" if independent.
- "Independent": "yes" if no prior-round result required; "no — depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete — return to Step 2 before proceeding.

STEP 4 — FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects
model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis —
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW — one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here — after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have a non-blank Catalog Source value.

| Tier | V | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" — ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" — ordered after their dependency rounds.

A blank Catalog Source in any row is a required rewrite before this step is complete.

[Column Schema Auditor Pass 2 emitted here — after item 3 is written.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a — DECLARATION CHECK:
  [ ] Column Contract block present in output: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  4a Declaration Check: PASS (both items yes) / FAIL → FAIL requires: rewrite
  Column Contract section to explicitly name Catalog Source column; do not
  proceed to 4b until Column Contract names the Catalog Source column.

  Advance to 4b regardless of this result. A 4a FAIL does not suppress 4b.

4b — POPULATION CHECK:

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Catalog Source Value | Row Result |
  |---|---------------------|------------|
  (One row per variation.)
  Row result options:
    "populated" if Catalog Source non-blank.
    "blank → FAIL requires: add Catalog Source value for V-NN before audit
    is marked complete" if Catalog Source blank.

  4b Population Check: PASS (all rows populated) / FAIL → FAIL requires:
  populate Catalog Source column for all blank rows listed above; audit is
  not complete until all rows carry a non-blank Catalog Source value.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if 4a Declaration Check is PASS AND 4b Population Check
is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition — one sentence each.

---

## V-04 — Role Sequence: Axis Cost Auditor Role

**axis:** role-sequence

**hypothesis:**
- criterion: C-30 (Evaluation-order axis-cost table)
- direction: C-30 pass rate increases from zero (criterion born R9) to measurable rate; every run produces a verified evaluation order where the Axis Cost Auditor role confirms that each row's Evaluation Cost cell contains a per-axis structural reason — not a generic tier rule — before the Findings Synthesizer may declare item 3 complete
- mechanism: The Axis Cost Auditor role is a required verification pass that must complete before Step 4 item 3 is declared done — verifying that each row's Evaluation Cost cell contains a per-axis structural reason is a required input to declaring the evaluation order complete; a generator cannot produce a compliant evaluation order without having each row's cost rationale verified, because the Findings Synthesizer is explicitly prohibited from declaring item 3 complete until the Axis Cost Auditor has passed; therefore per-axis structural cost rationale per row is a required input to item 3 completion via role-sequence position; the Axis Cost Auditor role is structurally inseparable from the item 3 completion gate
- failure-condition:
    round-label:      R8
    source-variation: V-05
    criterion-born:   C-30
    evaluative-label:
      rank-label:       "most complete combination in R8 — unified NON-SUPPRESSION INVARIANT CONTRACT with mandatory labeled result template, yet C-10 PARTIAL because the evaluation order table's Tier-level ordering rationale appeared in prose rules outside the table rather than as per-row cells"
      quality-dimension: "most comprehensive demonstration that structural completeness of audit machinery does not imply per-row cost rationale in the evaluation order — established that a fully operational compliance audit (C-28, C-29 satisfied) can coexist with an evaluation order where the ordering logic is stated in aggregate prose ('Tier 1: independent variations ordered by cost') and applied uniformly to all rows, preventing per-row verification of why each specific variation is positioned at its tier; the combination context exposed the C-10/C-30 gap as orthogonal to audit correctness"
    consequence: if C-30 does not pass with an Axis Cost Auditor role, the role adds verification overhead without improving per-row rationale content in the table; combine with output-format (V-01 R9) which adds the Axis Cost Rationale column to the schema, creating a compound mechanism where the schema gate prevents blank cells and the Axis Cost Auditor role verifies content quality

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern — SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does
not explicitly state the non-suppression invariant is structurally incomplete and
must be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier             <- priority tier (Tier 1 = evaluate first)
  [ ] V                <- variation label (V-01 through V-0N)
  [ ] Axis             <- canonical axis name
  [ ] Evaluation Cost  <- low / medium / high + one-line explanation; the
                          explanation must be axis-specific — it must name a
                          structural property of this particular axis (e.g.,
                          "one-line template change, no role dependencies") not
                          a generic cost label ("low" alone is structurally
                          incomplete for this column)
  [ ] Independence     <- yes / partial / no + dependency note
  [ ] Cross-Round Dependency  <- Round + Variation + Metric, or "none"
  [ ] Catalog Source   <- required attribution column; every row must name the
                          Step 3 row from which this entry was derived.
                          Format:
                            Independent: "Step 3 row V-NN: independent"
                            Dependent:   "Step 3 row V-NN: depends on [R/V/M]"

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Catalog Source column explicitly declared) produces structurally incomplete
output. The table must not be committed until the contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high + axis-specific structural reason. Must
  name a structural property of this particular axis, not a generic tier rule.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Format per Column Contract above. Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Catalog Source" value AND a non-generic
"Evaluation Cost" value. A row with only "low" in Evaluation Cost with no per-axis
reason is structurally incomplete — rewrite before committing the table.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical
   list. Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete — return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 — DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL — name failing item]."

   PASS 2 — POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Catalog Source: [populated / blank — rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS — all rows populated / FAIL — list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes
   AND Axis Cost Auditor has completed its pass.

6. Axis Cost Auditor
   Responsibility: After Step 4 item 3 (evaluation order table) is written, verify
   that every row's Evaluation Cost cell contains an axis-specific structural reason,
   not a generic cost label.

   AXIS COST AUDIT — runs after Step 4 item 3 is written, before item 3 is declared
   complete:
     For each variation in the evaluation order table, verify:
       [ ] Evaluation Cost cell contains text beyond a bare cost level (e.g.,
           not only "low" or "high" — must name a structural property of the axis):
           yes / no
     Emit per row: "V-NN Evaluation Cost: [specific — names structural property /
     generic — rewrite required to add per-axis reason]."
     Emit summary: "Axis Cost Auditor complete. Axis cost rationale check:
     [PASS — all rows contain axis-specific structural reason /
      FAIL — list rows with only generic cost labels]."

   The Findings Synthesizer may not declare Step 4 item 3 complete until the Axis
   Cost Auditor has emitted its summary.

STEP 1 — SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 — VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN — [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism — use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN — the round containing the comparison baseline event]
    source-variation: [V-NN — the specific variation in that round]
    criterion-born:   [C-NN — the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance
                         in its round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or
                          pedagogically excellent — the specific quality
                          demonstrated. NOT a restatement of rank-label.
                          A blank or redundant quality-dimension triggers a
                          required rewrite before this citation block is committed.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY — every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 — CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Column rules:
- "Comparative Claim": quote or paraphrase the hypothesis claim that references a
  prior-round result. Write "none" if no such claim exists.
- "Prior-Round Result Required": the metric that must exist before the claim can be
  verified. Write "n/a" if independent.
- "Round + Variation + Metric": "R[round] / V-NN / [metric]", or "n/a" if independent.
- "Independent": "yes" if no prior-round result required; "no — depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete — return to Step 2 before proceeding.

STEP 4 — FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects
model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis —
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW — one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here — after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have a non-blank Catalog Source value AND an axis-specific structural
reason in the Evaluation Cost cell.

| Tier | V | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" — ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" — ordered after their dependency rounds.

A blank Catalog Source or a generic Evaluation Cost in any row is a required rewrite
before this step is complete.

[Column Schema Auditor Pass 2 emitted here — after item 3 is written.]
[Axis Cost Auditor emitted here — after item 3 is written, before item 3 is declared complete.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a — DECLARATION CHECK:
  [ ] Column Contract block present in output: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  Declaration Check Result: PASS (both items yes) / FAIL (name failing item)

  NOTE: A 4a FAIL does not suppress 4b. Advance to 4b regardless of 4a result.

4b — POPULATION CHECK:

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Catalog Source Value | Row Result |
  |---|---------------------|------------|
  (One row per variation. "Row Result: populated" if Catalog Source non-blank.
   "Row Result: blank — rewrite required" if Catalog Source blank.)

  Population Check Result: PASS (all rows populated) / FAIL (list blank rows)

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition — one sentence each.

---

## V-05 — Combination: Output Format x Lifecycle Emphasis

**axis:** output-format x lifecycle-emphasis
**pass-type:** combination

**hypothesis:**
- criteria: C-30 (Evaluation-order axis-cost table) + C-31 (Execution-site non-suppression co-location)
- direction: C-30 and C-31 pass rates both increase from zero (both criteria born R9) to measurable rate simultaneously; the Axis Cost Rationale column (from V-01 R9) makes the evaluation order table's ordering logic independently verifiable per row; the execution-site co-location annotations (from V-02 R9) make the non-suppression invariant inseparable from the audit execution actions at both checkpoints; both criteria are satisfied without either mechanism interfering with the other
- mechanism: The Axis Cost Rationale column is declared in the Column Contract before any table is written — writing a table without the Axis Cost Rationale column declared is structurally prohibited; therefore the Axis Cost Rationale column is a required input to writing any evaluation order table (V-01 R9 mechanism); simultaneously, the NON-SUPPRESSION INVARIANT CO-LOCATED annotations are embedded inside the 4a and 4b execution blocks — these annotations are required structural elements of each execution block; therefore a generator following the 4a template cannot omit the assertion that 4b must execute regardless of 4a's result, and a generator following the 4b template cannot omit the assertion of its own independence from 4a outcome (V-02 R9 mechanism); the two mechanisms operate on distinct structural layers (schema/table layer vs execution-template layer) and cannot interfere
- failure-condition:
    round-label:      R9
    source-variation: V-01
    criterion-born:   C-30
    evaluative-label:
      rank-label:       "R9 Priority 1 combination anchor — V-01 R9 Axis Cost Rationale column designated as the output-format axis source for the R9 Priority 1 combination run"
      quality-dimension: "structural-independence demonstration — established that adding the Axis Cost Rationale column to the Column Contract creates a per-row schema gate that forces per-axis cost reasoning into the evaluation order table without requiring additional roles or lifecycle gates; the column contract mechanism is the minimal structural change that makes C-30 a precondition of table production rather than a post-hoc verification target"
    consequence: if C-30 does not pass in the combination context, the Axis Cost Rationale column coexists with the co-located non-suppression annotations without compound benefit — the two mechanisms are independent and the column's failure does not indicate that the co-location mechanism failed; evaluate V-01 R9 and V-02 R9 scored results separately to determine which single-axis mechanism succeeded before retrying the combination

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

NON-SUPPRESSION INVARIANT CONTRACT

The compliance audit in this run contains two independent checkpoints (Declaration
Check and Population Check). This contract governs their execution behavior.

Invariant: Both checkpoints must emit their labeled results regardless of the
pass/fail state of either checkpoint. A FAIL result on the Declaration Check does
not suppress execution or result emission for the Population Check. A FAIL result
on the Population Check does not suppress the Declaration Check result.

Prohibited pattern — SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
Check result when it fails, and omitting the Population Check output entirely.
Any audit section that exhibits short-circuit suppression is structurally incomplete.

NON-SUPPRESSION STRUCTURAL INCOMPLETENESS ASSERTION: An audit section that does
not explicitly state the non-suppression invariant is structurally incomplete and
must be rewritten before the step is declared complete.

Compliance: The audit section in Step 4 item 4 must include the following statement
before the checkpoints run:
  "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
   regardless of each other's pass/fail state."

COLUMN CONTRACT

Before any evaluation order table is written in this run, declare all required
columns here. A table written without first completing this Column Contract is
structurally incomplete and must not be committed.

Required columns:
  [ ] Tier                 <- priority tier (Tier 1 = evaluate first)
  [ ] V                    <- variation label (V-01 through V-0N)
  [ ] Axis                 <- canonical axis name
  [ ] Evaluation Cost      <- low / medium / high + one-line explanation
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural
                              reason this variation is at this cost level — not a
                              generic tier rule; (2) independence claim — why this
                              variation is independent or what prior-round result
                              it depends on. A cell containing only "low" or
                              "Tier 1" with no per-axis reason is structurally
                              incomplete.
  [ ] Independence         <- yes / partial / no + dependency note
  [ ] Cross-Round Dependency  <- Round + Variation + Metric, or "none"
  [ ] Catalog Source       <- required attribution column; every row must name the
                              Step 3 row from which this entry was derived.
                              Format:
                                Independent: "Step 3 row V-NN: independent"
                                Dependent:   "Step 3 row V-NN: depends on [R/V/M]"

STRUCTURAL INCOMPLETENESS ASSERTION: A generator that writes any evaluation order
table in this run without first completing the Column Contract above (all boxes
checked, Axis Cost Rationale and Catalog Source columns explicitly declared)
produces structurally incomplete output. The table must not be committed until the
contract is complete.

EVALUATION ORDER TABLE SCHEMA

(Apply only after Column Contract is complete and all columns are checked above.)

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Column definitions:
- "Tier": evaluation priority tier; Tier 1 = evaluate first.
- "V": variation label (V-01 through V-0N).
- "Axis": canonical axis name.
- "Evaluation Cost": low / medium / high with a one-line explanation.
- "Axis Cost Rationale": per-axis structural reason for this row's tier position.
  Must state: (a) the structural property of this axis that drives the cost level;
  (b) why this variation is independent or what prior-round result it requires.
  A cell with only a cost level or tier label is structurally incomplete.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Required: non-blank in every row.

REQUIRED: Every row must have non-blank values in both "Axis Cost Rationale" and
"Catalog Source". A row missing either is structurally incomplete — rewrite before
committing the table.

ROLES

1. Axis Selector
   Responsibility: Execute Step 1. Select {N} distinct axes from the canonical
   list. Commit the axis list before Step 2 begins.

2. Variation Author
   Responsibility: Execute Step 2. For each selected axis, write one complete,
   standalone variation body with fully populated hypothesis block including
   failure-condition chain. Do not begin the next variation until the current
   body is complete.

3. Dependency Cataloger
   Responsibility: Execute Step 3. Produce the cross-round dependency catalog.
   All four columns must be non-blank in every row. A blank column means the
   hypothesis is incomplete — return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 — DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Axis Cost Rationale" column is explicitly named in the contract: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL — name failing item]."

   PASS 2 — POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value is non-blank and contains a per-axis reason: yes / no
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing — rewrite required].
     V-NN Catalog Source: [populated / blank — rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS — all rows populated / FAIL — list incomplete rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes.

STEP 1 — SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 — VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN — [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism — use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN — the round containing the comparison baseline event]
    source-variation: [V-NN — the specific variation in that round]
    criterion-born:   [C-NN — the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance
                         in its round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or
                          pedagogically excellent — the specific quality
                          demonstrated. NOT a restatement of rank-label.
                          A blank or redundant quality-dimension triggers a
                          required rewrite before this citation block is committed.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY — every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 — CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Column rules:
- "Comparative Claim": quote or paraphrase the hypothesis claim that references a
  prior-round result. Write "none" if no such claim exists.
- "Prior-Round Result Required": the metric that must exist before the claim can be
  verified. Write "n/a" if independent.
- "Round + Variation + Metric": "R[round] / V-NN / [metric]", or "n/a" if independent.
- "Independent": "yes" if no prior-round result required; "no — depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete — return to Step 2 before proceeding.

STEP 4 — FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects
model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis —
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW — one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here — after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have non-blank values in both Axis Cost Rationale and Catalog Source.

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" — ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" — ordered after their dependency rounds.

A row missing Axis Cost Rationale or Catalog Source is a required rewrite.

[Column Schema Auditor Pass 2 emitted here — after item 3 is written.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a — DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless
  of this checkpoint's result. A model following this execution template cannot
  omit 4b even if it ignores the preamble invariant or role definition. Absence
  of this annotation makes the 4a execution block structurally incomplete.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  Declaration Check Result: PASS (all items yes) / FAIL (name failing item)

  Advance to 4b regardless of this result. 4a FAIL does not suppress 4b.

4b — POPULATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: This checkpoint
  executes regardless of 4a result. A model following this execution template
  cannot suppress this checkpoint based on 4a outcome. Absence of this annotation
  makes the 4b execution block structurally incomplete.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  (One row per variation. "Row Result: populated" if both cells non-blank with
   per-axis reason. "Row Result: incomplete — rewrite required" if either cell
   blank or generic.)

  Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows)

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition — one sentence each.

---

## Round 9 Findings

### Phase 3 — Cross-Round Dependency Catalog

This catalog is a required input to the evaluation order table. The evaluation order
is derived from this catalog, not generated ad hoc.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|
| V-01 | output-format | "C-30 pass rate increases from zero (criterion born R9) to measurable rate — every row carries a non-empty Axis Cost Rationale cell with a per-axis structural reason" | R8 / all-5 / C-10 PARTIAL rate — confirms the ordering gap exists and that aggregate prose ordering did not satisfy C-10 in any R8 variation | R8 / all-5 / C-10 PARTIAL | no — depends on R8/all-5/C-10 PARTIAL |
| V-02 | lifecycle-emphasis | "C-31 pass rate increases from zero (criterion born R9) to measurable rate — NON-SUPPRESSION INVARIANT CO-LOCATED annotation present inside 4a and 4b execution blocks" | R8 / V-04 / C-28 PARTIAL status — confirms the execution-template gap exists and that the role-definition-only placement did not satisfy C-28 | R8 / V-04 / C-28 PARTIAL | no — depends on R8/V-04/C-28 PARTIAL |
| V-03 | phrasing-register | "C-32 pass rate increases from zero (criterion born R9) to measurable rate — each checkpoint result line carries a prescriptive FAIL-path directive" | R8 / V-04 / C-29 strongest — confirms that per-checkpoint labeled results without remediation directives (C-29 pass) is the departure baseline for C-32 | R8 / V-04 / C-29 PASS (strongest) | no — depends on R8/V-04/C-29 PASS status |
| V-04 | role-sequence | "C-30 pass rate increases from zero (criterion born R9) to measurable rate — Axis Cost Auditor verifies each Evaluation Cost cell contains axis-specific structural reason" | R8 / all-5 / C-10 PARTIAL rate — same baseline as V-01; confirms that evaluation cost cells with only tier labels did not satisfy C-10 in any R8 variation | R8 / all-5 / C-10 PARTIAL | no — depends on R8/all-5/C-10 PARTIAL |
| V-05 | output-format × lifecycle-emphasis | "C-30 and C-31 both pass — Axis Cost Rationale column satisfies C-30 and execution-site co-location satisfies C-31 simultaneously" | R9 / V-01 / C-30 pass rate + R9 / V-02 / C-31 pass rate — combination claim is only verifiable once both V-01 and V-02 are scored in R9 | R9 / V-01 / C-30 + R9 / V-02 / C-31 | no — depends on R9/V-01/C-30 and R9/V-02/C-31 |

### Combination Candidates (C-09)

**Priority 1: V-01 (output-format) × V-02 (lifecycle-emphasis) → C-30 + C-31**

Based on V-01 R9 mechanism + V-02 R9 mechanism.

- **Failure modes targeted per axis**: V-01 targets C-30 (ordering logic not per-row verifiable because no Axis Cost Rationale column in schema); V-02 targets C-31 (non-suppression invariant in preamble and role definition only, absent from execution template).
- **Residual weakness after V-01 only**: evaluation order table gains per-row cost rationale (C-30 satisfied), but 4a and 4b execution blocks remain silent on non-suppression at the execution site — a model following the execution template can still short-circuit 4b on 4a FAIL (C-31 not satisfied).
- **Compound criterion effect (both active)**: C-30 and C-31 both satisfied simultaneously; the evaluation order is verifiable per row AND the compliance audit's non-suppression guarantee is inseparable from the execution template — making both the evidence-gathering phase and the audit phase prescriptive at their respective structural layers.
- **Priority**: HIGH — this is the R9 designated combination (V-05); both C-30 and C-31 are new in R9 and vacuous in R8, making the compound effect maximally testable in this round.

Cite: V-01 R9 (Axis Cost Rationale column mechanism), V-02 R9 (execution-site co-location mechanism). Implemented as V-05.

---

**Priority 2: V-03 (phrasing-register) × V-01 (output-format) → C-32 + C-30**

Based on V-03 R9 mechanism + V-01 R9 mechanism.

- **Failure modes targeted per axis**: V-03 targets C-32 (audit output is observational — checkpoint results carry PASS/FAIL labels without remediation directives); V-01 targets C-30 (evaluation order table rows have no per-axis structural cost rationale).
- **Residual weakness after V-03 only**: compliance audit checkpoint results become prescriptive (C-32 satisfied), but evaluation order table rows still lack per-axis structural cost rationale — ordering logic remains in aggregate tier-rule prose (C-30 not satisfied).
- **Compound criterion effect (both active)**: C-30 and C-32 both satisfied; the evaluation order table is per-row verifiable AND the compliance audit is prescriptive — both output layers (table and audit) carry enforceable directives rather than observations.
- **Priority**: HIGH — C-30 and C-32 are the two most structurally independent new criteria in R9 (different layers: table schema vs audit phrasing), making their combination the cleanest two-axis pass available after V-05.

Cite: V-03 R9 (prescriptive phrasing mechanism), V-01 R9 (Axis Cost Rationale column mechanism).

---

**Priority 3: V-02 (lifecycle-emphasis) × V-03 (phrasing-register) → C-31 + C-32**

Based on V-02 R9 mechanism + V-03 R9 mechanism.

- **Failure modes targeted per axis**: V-02 targets C-31 (execution-site gap — non-suppression invariant absent from execution template); V-03 targets C-32 (observational audit — no FAIL-path remediation directives per checkpoint).
- **Residual weakness after V-02 only**: execution-site non-suppression invariant is co-located at 4a and 4b execution blocks (C-31 satisfied), but checkpoint result lines still use observational phrasing ("PASS / FAIL") without prescribing what must happen when FAIL — consumer must infer the remediation action (C-32 not satisfied).
- **Compound criterion effect (both active)**: C-31 and C-32 both satisfied; each checkpoint's execution block carries the non-suppression invariant co-located (making execution-site bypass impossible) AND each result line carries a FAIL-path directive (making the required response explicit) — the audit is both execution-guarded and prescriptive.
- **Priority**: MEDIUM — C-31 + C-32 are the natural audit-layer pair, but their combination is lower priority than V-05 (which targets the distinct C-30 + C-31 pair representing cross-layer coverage) and Priority 2 (which targets C-30 + C-32).

Cite: V-02 R9 (co-located annotation mechanism), V-03 R9 (prescriptive phrasing mechanism).

---

### Evaluation Order (C-10 / C-30)

COLUMN CONTRACT DECLARATION (before writing evaluation order table):

Required columns:
  [x] Tier
  [x] V
  [x] Axis
  [x] Axis Cost Rationale  <- per-row rationale cell: per-axis structural reason
                              for cost level and independence claim
  [x] Independence
  [x] Cross-Round Dependency
  [x] Catalog Source

STRUCTURAL INCOMPLETENESS ASSERTION: An evaluation order table written without
the Column Contract above (all boxes checked, Axis Cost Rationale and Catalog
Source declared) is structurally incomplete. The table below is written only
because the Column Contract above is complete.

Column Contract complete. Proceeding to evaluation order table.

| Tier | V | Axis | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |
|------|---|------|---------------------|--------------|----------------------|----------------|
| 1 | V-03 | phrasing-register | Low cost — single phrasing change to the audit result line template; no new roles, no schema changes, no structural additions; the only change is substituting observational labels for prescriptive labels with FAIL-path text; baseline (R8/V-04/C-29 PASS) is already available, making this the fastest-to-verify variation in the set | no — depends on R8/V-04/C-29 PASS | R8 / V-04 / C-29 PASS | Phase 3 row V-03 |
| 1 | V-01 | output-format | Low cost — adds one column to the Column Contract and table schema header; no role changes; the Axis Cost Rationale column addition is structurally isolated to the preamble and table header; baseline (R8 all-5 C-10 PARTIAL) is already available; evaluate before V-04 to establish whether schema-gate alone achieves C-30 without requiring a verification role | no — depends on R8/all-5/C-10 PARTIAL | R8 / all-5 / C-10 PARTIAL | Phase 3 row V-01 |
| 1 | V-04 | role-sequence | Medium cost — adds a new role (Axis Cost Auditor) and a post-table emission step; structural change is isolated to role 6 and the item 3 completion gate; same R8 C-10 baseline as V-01; evaluate after V-01 to determine whether role-based verification adds coverage beyond schema-gate alone | no — depends on R8/all-5/C-10 PARTIAL | R8 / all-5 / C-10 PARTIAL | Phase 3 row V-04 |
| 1 | V-02 | lifecycle-emphasis | Medium cost — adds inline annotation blocks inside two execution template locations (4a and 4b); structural change is limited to the audit execution blocks; baseline (R8/V-04/C-28 PARTIAL) is already available; evaluate before V-05 to confirm execution-site co-location achieves C-31 as a single-axis result | no — depends on R8/V-04/C-28 PARTIAL | R8 / V-04 / C-28 PARTIAL | Phase 3 row V-02 |
| 2 | V-05 | output-format x lifecycle-emphasis | High cost — combination variation; the compound C-30 + C-31 claim requires V-01 R9 C-30 pass rate and V-02 R9 C-31 pass rate to both be scored before the compound claim is verifiable; evaluate only after Tier 1 variations are scored in R9 | no — depends on R9/V-01/C-30 and R9/V-02/C-31 | R9 / V-01,V-02 / C-30 + C-31 pass rates | Phase 3 row V-05 |

COLUMN SCHEMA AUDIT

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints execute regardless of each
other's result. Pass 1 FAIL does not suppress Pass 2. Both passes appear below.

NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4a Declaration Check
executes now. 4b Population Check executes after, regardless of 4a result.
A model following this audit template cannot suppress 4b on 4a FAIL.

4a Declaration Check:
  [ ] Column Contract block present and all required columns named: yes
  [ ] Axis Cost Rationale column explicitly declared in contract: yes
  [ ] Catalog Source column explicitly declared in contract: yes
  4a Declaration Check: PASS → proceed to 4b
  [FAIL → rewrite Column Contract section to name missing column before proceeding]

NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless
of 4a result.

4b Population Check:
  (Executing 4b regardless of 4a result.)

  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  | V-03 | present — low cost, phrasing-only change, R8/V-04/C-29 baseline | present — Phase 3 row V-03 | populated |
  | V-01 | present — low cost, one-column schema addition, R8/all-5/C-10 baseline | present — Phase 3 row V-01 | populated |
  | V-04 | present — medium cost, new role addition, same R8 C-10 baseline as V-01 | present — Phase 3 row V-04 | populated |
  | V-02 | present — medium cost, inline annotation at two execution sites | present — Phase 3 row V-02 | populated |
  | V-05 | present — high cost, combination, depends on R9/V-01/C-30 and R9/V-02/C-31 | present — Phase 3 row V-05 | populated |

  4b Population Check: PASS → all rows populated
  [FAIL → populate Axis Cost Rationale and Catalog Source for all blank rows before audit is complete]

C-24 Pass: yes — Declaration Check PASS and Population Check PASS.

### Anchor Designation (C-12)

**Anchor: V-01 (output-format / Axis Cost Rationale Column)**

- **Structural impact**: The Axis Cost Rationale column operates at the schema layer — it is declared in the Column Contract before any table is written, making per-row cost rationale a structural precondition of table production rather than a post-hoc verification target; this is the most structurally central mechanism available for C-30 because it gates the table at the schema declaration level.
- **Isolation quality**: The output-format axis change is confined entirely to the Column Contract and table schema header; it introduces no role changes, no lifecycle sub-phases, and no phrasing changes in other sections, making it the cleanest single-axis change in the set and the most reliable isolation baseline for combination runs.
- **Detectable failure condition**: If C-30 does not pass with V-01 R9's schema gate, the Axis Cost Rationale column was declared but left empty or populated with generic values — indicating that the schema-gate mechanism alone is insufficient and a role-based verification pass (V-04 R9) or phrasing enforcement (V-03 R9 applied to the evaluation order section) is required before attempting the combination.
