# quest-variate Variate — Round 10

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v10 (C-01 through C-35; essential C-01–C-05)
**Round:** R10 — 3 single-axis passes (V-01/V-02/V-03) + 2 combination passes (V-04/V-05)

---

## Round 10 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis | Co-located annotations in 4a and 4b upgraded from terse inline phrases to fully labeled blocks with named headers and self-explanatory sub-clauses stating why co-location is necessary — making each annotation self-contained without requiring cross-reference | C-33 |
| V-02 | phrasing-register | single-axis | FAIL-path directives that include advancement restrictions ("do not declare complete until") gain an explicit COMPLETION-GATE SCOPE note distinguishing the directive's governance scope (audit completion status) from execution order (4b still executes regardless) | C-34 |
| V-03 | role-sequence | single-axis | Axis Cost Quality Gate added as role 6 (after Column Schema Auditor, before Findings Synthesizer declares item 3 complete); role rejects generic abbreviated Axis Cost Rationale values and requires structural per-axis reasons | C-35 |
| V-04 | lifecycle-emphasis x phrasing-register | combination (R10 Priority 1 -- V-01 R10 labeled blocks x V-02 R10 completion-gate scoping) | Combines labeled self-documentation blocks (V-01 R10) with FAIL-directive completion-gate scoping notes (V-02 R10) | C-33, C-34 |
| V-05 | lifecycle-emphasis x phrasing-register x role-sequence | combination (R10 Priority 2 -- full integration) | Combines V-01 R10 + V-02 R10 + V-03 R10 | C-33, C-34, C-35 |

**Anchor designation (C-12):** V-01. Justification at end of document.

---

## SPREAD-DESIGN PHASE

Rubric state entering R10: v10, C-01 through C-35. Aspirational pool: 27 criteria (C-09..C-35).
Three new criteria born from R9 excellence signals: C-33, C-34, C-35 — vacuous-exempt in R9,
live in R10.

PARTIAL record entering R10: None from R9. R9 produced three new patterns as full excellence
signals rather than PARTIALs. No amplification needed.

R9 pattern inventory:
- C-33 born R9 V-02 (labeled self-documentation of co-located annotation)
- C-34 born R9 V-03 (FAIL-directive completion-gate semantic distinction)
- C-35 born R9 V-04 (per-row axis-cost rationale content quality gate)

Axis assignment for R10:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | lifecycle-emphasis | C-33 born R9 V-02 -- co-located annotation is terse; labeled block with self-explanatory sub-clause absent | C-33 | 99.26 |
| V-02 | phrasing-register | C-34 born R9 V-03 -- FAIL-path directives present with advancement restrictions but lack completion-gate semantic scoping note | C-34 | 99.26 |
| V-03 | role-sequence | C-35 born R9 V-04 -- Axis Cost Rationale column present but no dedicated role rejects generic abbreviated values | C-35 | 99.26 |
| V-04 | lifecycle-emphasis x phrasing-register | V-01 R10 x V-02 R10 | C-33 + C-34 | 99.63 |
| V-05 | lifecycle-emphasis x phrasing-register x role-sequence | V-01 R10 x V-02 R10 x V-03 R10 | C-33 + C-34 + C-35 | 100 |

Divergence: composite spread 99.26 / 99.26 / 99.26 / 99.63 / 100. Criterion-level spread:
V-01/V-02/V-03 each pass one distinct new criterion (C-33 / C-34 / C-35) while failing the
other two. Composite parity among single-axis variations reflects each targeting one aspirational
slot in a denominator of 27 -- criterion-level spread is the diagnostic output, not composite
spread.

SPREAD-DESIGN COMPLETE 2026-03-15 R10 -- axis assignments confirmed.

---

## STEP 1 -- FIVE COMPLETE VARIATION BODIES

---

### V-01 -- Lifecycle Emphasis: Labeled Execution-Site Self-Documentation

**axis:** lifecycle-emphasis

**hypothesis:**
- criterion: C-33 (Execution-site invariant labeled self-documentation)
- direction: C-33 pass rate increases from zero (vacuous-exempt R9) to measurable rate in R10;
  every run produces compliance audit blocks where the co-located non-suppression annotation
  is a fully labeled block with a named header and a self-explanatory sub-clause stating why
  co-location is necessary -- making the annotation interpretable without cross-referencing the
  preamble or role definition
- mechanism: The labeled block structure is a required input to C-33 compliance -- a block that
  names only "NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE" as a header without an
  explanatory sub-clause cannot satisfy C-33's pass condition ("sub-clause naming why co-location
  is necessary"); the sub-clause must identify that a model following the template cannot omit
  the governed checkpoint even if the preamble and role definition are not read; without the
  sub-clause, the annotation header alone satisfies C-31 (co-location) but not C-33 (labeled
  self-documentation); the sub-clause is structurally required to close the gap between the
  terse NOTE pattern and the self-explanatory block pattern
- failure-condition:
    round-label:      R9
    source-variation: V-02
    criterion-born:   C-33
    evaluative-label:
      rank-label:       "maximum execution-site coverage in R9 -- fully labeled, self-explanatory annotation block embedded in both 4a and 4b execution sites"
      quality-dimension: "cleanest demonstration that annotation self-documentation is the mechanism separating C-31 from C-33 -- established that a terse NOTE-style co-location satisfies C-31 by placing the invariant at the execution site, while a labeled block with a rationale sub-clause satisfies C-33 by making the annotation self-contained; the sub-clause is the sole distinguishing element between the two patterns, making the annotation-register the load-bearing variable"
    consequence: if C-33 does not pass with labeled blocks in 4a and 4b, the block structure adds
      header overhead without converting terse annotations into self-documenting guarantees; combine
      with phrasing-register (V-02 R10) to add FAIL-directive completion-gate scoping for
      simultaneous C-33 + C-34 coverage

---

```
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

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
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
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural reason
                              this variation is at this cost level -- not a generic tier
                              rule; (2) independence claim -- why this variation is
                              independent or what prior-round result it depends on.
                              A cell containing only "low" or "Tier 1" with no per-axis
                              reason is structurally incomplete.
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
  A cell containing only a cost level or tier label without a per-axis reason is
  structurally incomplete -- rewrite before committing the table.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason. A row with a generic rationale that applies equally
to all variations does not satisfy this requirement.

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
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Axis Cost Rationale" column is explicitly named in the contract: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value is non-blank and contains a per-axis reason: yes / no
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN -- [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism -- use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN -- the round containing the comparison baseline event]
    source-variation: [V-NN -- the specific variation in that round]
    criterion-born:   [C-NN -- the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance in its
                         round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or pedagogically
                          excellent -- the specific quality demonstrated. NOT a
                          restatement of rank-label. A blank or redundant
                          quality-dimension triggers a required rewrite.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY -- every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

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
- "Independent": "yes" if no prior-round result required; "no -- depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete -- return to Step 2 before proceeding.

STEP 4 -- FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis --
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW -- one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have a non-blank Axis Cost Rationale value with a per-axis structural
reason.

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" -- ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" -- ordered after their dependency rounds.

A blank or generic Axis Cost Rationale in any row is a required rewrite before this
step is complete.

[Column Schema Auditor Pass 2 emitted here -- after item 3 is written.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a -- DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    This annotation exists at this execution site because a model following this
    template cannot omit checkpoint 4b even if it does not read the preamble
    NON-SUPPRESSION INVARIANT CONTRACT or the Column Schema Auditor role
    definition. Co-location at this execution site makes the invariant
    inseparable from the action it governs here -- this annotation is
    self-contained and does not depend on preamble or role-definition scope.
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block in this document to include
    the missing column before committing any evaluation order table. Do not declare
    the Declaration Check complete until the missing item is present.

4b -- POPULATION CHECK:

  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    This annotation exists at this execution site because this checkpoint must
    execute regardless of checkpoint 4a's result. A model following this
    execution template cannot suppress this checkpoint based on 4a outcome
    even if the preamble non-suppression contract or role independence
    requirement is not in scope. Co-location makes the guarantee inseparable
    from the execution action here -- this annotation is self-contained.
    EXECUTION DIRECTIVE: Execute this population check. Do not suppress based
    on 4a result.

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  (One row per variation. "Row Result: populated" if both cells non-blank with
   per-axis reason. "Row Result: incomplete -- rewrite required" if either cell
   blank or generic.)

  Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite incomplete rows in the evaluation order table to include
    a non-blank Axis Cost Rationale with a per-axis structural reason and a non-blank
    Catalog Source before declaring the Population Check complete.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

### V-02 -- Phrasing Register: FAIL-Directive Completion-Gate Scoping

**axis:** phrasing-register

**hypothesis:**
- criterion: C-34 (FAIL-directive completion-gate semantic distinction)
- direction: C-34 pass rate increases from zero (vacuous-exempt R9) to measurable rate in R10;
  every run produces compliance audit blocks where each FAIL-path directive that contains an
  advancement restriction carries an explicit COMPLETION-GATE SCOPE note distinguishing the
  directive's scope (audit completion status) from execution order (4b executes regardless),
  resolving the apparent conflict with the non-suppression invariant at the point of use
- mechanism: The COMPLETION-GATE SCOPE note is a required structural element of any
  advancement-restriction directive -- without it, a consumer of the FAIL-path directive cannot
  determine whether "do not declare complete until X" overrides or coexists with the
  non-suppression invariant's "advance to 4b regardless"; the scope note resolves this ambiguity
  at the execution site; a directive that contains an advancement restriction without the scoping
  note is structurally incomplete under C-34; the scoping note is a required input to producing
  a C-34-compliant directive, and cannot be omitted from any directive that carries an
  advancement restriction
- failure-condition:
    round-label:      R9
    source-variation: V-03
    criterion-born:   C-34
    evaluative-label:
      rank-label:       "strongest C-32 implementation in R9 -- mandatory per-checkpoint labeled result template with prescriptive FAIL-path directives, most directly demonstrating the completion-gate vs execution-order tension that C-34 formalizes"
      quality-dimension: "cleanest demonstration that FAIL-path directives with advancement restrictions create a semantic conflict with the non-suppression invariant that must be resolved explicitly at the point of use -- established that prescribing 'do not proceed until X' without scoping the restriction to completion-gate semantics leaves the invariant consumer uncertain whether the directive overrides the non-suppression guarantee; the semantic level-distinction (completion gate vs execution order) is the minimal addition that resolves the conflict without removing either constraint"
    consequence: if C-34 does not pass with completion-gate scoping notes, the FAIL-path
      directives remain ambiguous at the advancement-restriction / non-suppression boundary;
      combine with lifecycle-emphasis (V-01 R10) to add labeled self-documentation for
      simultaneous C-33 + C-34 coverage

---

```
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

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
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
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural reason
                              this variation is at this cost level -- not a generic tier
                              rule; (2) independence claim -- why this variation is
                              independent or what prior-round result it depends on.
                              A cell containing only "low" or "Tier 1" with no per-axis
                              reason is structurally incomplete.
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
  A cell containing only a cost level or tier label without a per-axis reason is
  structurally incomplete -- rewrite before committing the table.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

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
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Axis Cost Rationale" column is explicitly named in the contract: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value is non-blank and contains a per-axis reason: yes / no
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 complete until Column Schema Auditor has completed both passes.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN -- [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism -- use necessity language: "required input
                      to", "cannot be produced without", "must exist before", or
                      equivalent. Probabilistic language triggers a required rewrite.]
  failure-condition:
    round-label:      [R-NN -- the round containing the comparison baseline event]
    source-variation: [V-NN -- the specific variation in that round]
    criterion-born:   [C-NN -- the criterion added or changed due to this event]
    evaluative-label:
      rank-label:       [the comparative ranking applied to the source instance in its
                         round. Cannot be blank.]
      quality-dimension: [why the source instance was methodologically or pedagogically
                          excellent -- the specific quality demonstrated. NOT a
                          restatement of rank-label. A blank or redundant
                          quality-dimension triggers a required rewrite.]
    consequence:      [what the failure condition implies for the next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY -- every section, every instruction, fully written. No diffs.
 No references to other variations. Every structural section present.]

Do not advance to the next variation until the current body is complete.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

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
- "Independent": "yes" if no prior-round result required; "no -- depends on [R/V/M]"
  if a prior-round result is required.

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete -- return to Step 2 before proceeding.

STEP 4 -- FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis --
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW -- one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.
Every row must have a non-blank Axis Cost Rationale value with a per-axis structural
reason.

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" -- ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" -- ordered after their dependency rounds.

[Column Schema Auditor Pass 2 emitted here -- after item 3 is written.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a -- DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless
  of this checkpoint's result. A model following this execution template cannot
  omit 4b even if it ignores the preamble invariant or role definition. Absence
  of this annotation makes the 4a execution block structurally incomplete.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no

  4a Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block in this document to name the
    missing column before committing any evaluation order table. Do not declare this
    audit complete until the missing column is present in the output.

  COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
  audit completion status only. It does not restrict execution order. Checkpoint
  4b executes regardless of this restriction and regardless of the 4a result --
  the non-suppression invariant governs execution sequence; this directive governs
  whether the overall audit may be declared complete.

4b -- POPULATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: This checkpoint executes
  regardless of 4a result. A model following this execution template cannot suppress
  this checkpoint based on 4a outcome. Absence of this annotation makes the 4b
  execution block structurally incomplete.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  (One row per variation. "Row Result: populated" if both cells non-blank with
   per-axis reason. "Row Result: incomplete -- rewrite required" if either cell
   blank or generic.)

  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite each incomplete row to include a per-axis structural reason
    in Axis Cost Rationale and a non-blank Catalog Source value. Do not declare this
    population check complete until all rows pass.

  COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
  audit completion status only. It does not restrict the audit result from being
  recorded or both checkpoint results from appearing in the output. Both must appear.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

### V-03 -- Role Sequence: Axis Cost Quality Gate

**axis:** role-sequence

**hypothesis:**
- criterion: C-35 (Per-row axis-cost rationale content quality gate)
- direction: C-35 pass rate increases from zero (vacuous-exempt R9) to measurable rate in R10;
  every run produces an evaluation order table where each Axis Cost Rationale cell is verified
  by a dedicated role that classifies cells as STRUCTURAL (axis-specific reason named) or
  GENERIC (rejected), making content quality enforcement a role-level gate rather than only a
  schema-declaration requirement
- mechanism: The Axis Cost Quality Gate role is a required input to Findings Synthesizer
  declaring item 3 complete -- without the Quality Gate emitting a PASS summary, Findings
  Synthesizer cannot advance; the role's rejection condition is structural: it distinguishes
  cells containing a named axis-specific mechanism from cells containing only cost tiers or
  generic independence claims; a table with every Axis Cost Rationale cell populated by "low"
  satisfies the Column Contract's cell-presence requirement (C-26) but cannot produce a PASS
  from the Quality Gate because "low" names no axis-specific mechanism; the Quality Gate role
  is therefore the only mechanism that closes the gap between cell-presence (C-26 schema) and
  cell-content quality (C-35 quality gate)
- failure-condition:
    round-label:      R9
    source-variation: V-04
    criterion-born:   C-35
    evaluative-label:
      rank-label:       "strongest C-30 implementation in R9 via role-sequence axis -- Axis Cost Auditor role enforced per-row content quality at the role-gate level"
      quality-dimension: "most diagnostic demonstration that schema-declaration and role-level enforcement are distinct mechanisms -- established that a Column Contract naming the Axis Cost Rationale column enforces cell presence (a cell of any value satisfies the contract) while a dedicated auditor role enforcing structural content quality closes the gap by classifying cell values as substantive or generic; the two mechanisms operate at different abstraction levels and neither can substitute for the other"
    consequence: if C-35 does not pass with an Axis Cost Quality Gate role, per-row content
      quality remains enforced only at the schema level (cell-presence check), allowing generic
      abbreviated values to satisfy the contract; combine with lifecycle-emphasis (V-01 R10) and
      phrasing-register (V-02 R10) for full C-33 + C-34 + C-35 coverage in V-05 R10

---

```
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

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
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
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural reason
                              this variation is at this cost level -- not a generic tier
                              rule; (2) independence claim -- why this variation is
                              independent or what prior-round result it depends on.
                              A cell containing only "low" or "Tier 1" with no per-axis
                              reason is structurally incomplete.
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
  A cell containing only a cost level or tier label without a per-axis reason is
  structurally incomplete -- rewrite before committing the table.
- "Independence": yes / partial / no with a dependency note.
- "Cross-Round Dependency": Round + Variation + Metric, or "none."
- "Catalog Source": the specific Step 3 row from which this entry was derived.
  Required: non-blank in every row.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value containing
a per-axis structural reason.

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
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Axis Cost Rationale" column is explicitly named in the contract: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value is non-blank and contains a per-axis reason: yes / no
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 item 3 complete until Column Schema Auditor has completed both
   passes AND Axis Cost Quality Gate (role 6) has emitted a PASS summary.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes, before
   Findings Synthesizer declares Step 4 item 3 complete. For each row in the
   evaluation order table, classify the Axis Cost Rationale cell:

     STRUCTURAL: the cell names an axis-specific structural property for this row's
     variation -- e.g., a mechanism that drives the cost level for this variation
     specifically (such as "single template line change with no role dependencies --
     low cost"; "adds a role with nested checkpoint logic -- parse surface increases
     for evaluators tracking role interaction"). A structural value is falsifiable:
     replace this row with a different variation and the rationale becomes false.

     GENERIC: the cell contains only a cost tier ("low", "medium", "high"), a tier
     label ("Tier 1"), or a generic independence claim ("independent, low cost",
     "no prior-round dependency") that applies equally to all rows and carries no
     per-axis analysis. A generic value is non-falsifiable: it remains true for every
     row regardless of what variation it describes.

   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted cell value] /
     GENERIC -- rewrite required [quoted cell value]."

   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list V-NN labels] contain generic rationale; rewrite required
     before item 3 may be declared complete."

   Findings Synthesizer must not declare item 3 complete until this role emits
   a PASS summary. A GENERIC result in any row is a required rewrite.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN -- [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism -- use necessity language]
  failure-condition:
    round-label:      [R-NN]
    source-variation: [V-NN]
    criterion-born:   [C-NN]
    evaluative-label:
      rank-label:       [comparative ranking in source round]
      quality-dimension: [methodological or pedagogical quality -- not a restatement
                          of rank-label]
    consequence:      [next action implication]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY -- every section present. No diffs. No cross-references.]

Do not advance to the next variation until the current body is complete.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Validation: all four columns non-blank in every row.

STEP 4 -- FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both active.
- **Priority**: HIGH / MEDIUM / LOW -- one-sentence rationale.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Every row must have a non-blank Axis Cost Rationale with a per-axis structural reason.

[Column Schema Auditor Pass 2 emitted here -- after item 3 table is written.]

[Axis Cost Quality Gate emitted here -- after item 3 table is written, before
Findings Synthesizer declares item 3 complete.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a -- DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless
  of this checkpoint's result. A model following this execution template cannot
  omit 4b even if it ignores the preamble invariant or role definition. Absence
  of this annotation makes the 4a execution block structurally incomplete.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no
  Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block to include the missing column
    before committing any evaluation order table. Do not declare Declaration Check
    complete until the missing item is present.

  Advance to 4b regardless of this result.

4b -- POPULATION CHECK:

  NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: This checkpoint executes
  regardless of 4a result. A model following this execution template cannot suppress
  this checkpoint based on 4a outcome. Absence of this annotation makes the 4b
  execution block structurally incomplete.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|

  Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite incomplete rows before declaring population check complete.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

5. Anchor: one variation. Justify structural impact, isolation quality, and detectable
   failure condition -- one sentence each.
```

---

### V-04 -- Combination: Labeled Blocks + Completion-Gate Scoping (C-33 + C-34)

**axis:** lifecycle-emphasis x phrasing-register
**pass-type:** combination

**hypothesis:**
- criterion: C-33 (labeled self-documentation) + C-34 (completion-gate scoping)
- direction: C-33 and C-34 pass rates each increase from zero (vacuous-exempt R9) to measurable
  rate; each mechanism is independently satisfied within the same skill body, and their coexistence
  does not produce structural interference -- the labeled block sub-clause ("advance to 4b
  regardless") and the completion-gate scope note ("this governs completion status, not execution
  order") operate at different levels and reinforce rather than conflict
- mechanism: The labeled block annotation (C-33) is a required input to making the co-location
  guarantee self-contained; the completion-gate scoping note (C-34) is a required input to making
  the advancement restriction unambiguous; both are required simultaneously to produce an audit
  where the execution-site annotation is both self-documenting and its FAIL-path directives carry
  unambiguous completion semantics; neither mechanism can substitute for the other
- failure-condition:
    round-label:      R9
    source-variation: V-05
    criterion-born:   C-33
    evaluative-label:
      rank-label:       "strongest R9 combination -- combined Axis Cost Rationale column (V-01 R9) with execution-site co-location (V-02 R9), highest composite in R9"
      quality-dimension: "most complete integration of C-30 and C-31 within a single combination body -- established that these two mechanisms are compositionally stable and that their co-presence does not produce interference; confirms that R10 combination testing is appropriate for C-33 + C-34 as the next pairing layer"
    consequence: if C-33 + C-34 do not simultaneously pass in V-04, the two mechanisms
      interfere or one undermines the other; combine with role-sequence (V-03 R10) in V-05
      for full C-33 + C-34 + C-35 coverage

---

```
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

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
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
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural reason
                              this variation is at this cost level -- not a generic tier
                              rule; (2) independence claim -- why this variation is
                              independent or what prior-round result it depends on.
                              A cell containing only "low" or "Tier 1" with no per-axis
                              reason is structurally incomplete.
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

Column definitions match the Column Contract declarations above. Every row must
have a non-blank Axis Cost Rationale value containing a per-axis structural reason.
A cell containing only a cost level or tier label is structurally incomplete.

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
   All four columns must be non-blank in every row. Step 4 must not begin until
   this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3, before Step 4 item 3):
     [ ] Column Contract block present: yes / no
     [ ] "Axis Cost Rationale" explicitly named in contract: yes / no
     [ ] "Catalog Source" explicitly named in contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3):
     Per row: Axis Cost Rationale non-blank with per-axis reason (yes/no) +
     Catalog Source non-blank (yes/no).
     Emit per row and summary: "Column Schema Auditor Pass 2 complete.
     Population check: [PASS / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.

5. Findings Synthesizer
   Responsibility: Execute Step 4. May not declare Step 4 complete until Column
   Schema Auditor has completed both passes.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN -- [Axis Name]
axis: [axis name]
hypothesis:
  criterion:         [C-NN and name]
  direction:         [expected change]
  mechanism:         [necessity language -- "required input to", "cannot be produced
                      without", "must exist before", or equivalent]
  failure-condition:
    round-label:      [R-NN]
    source-variation: [V-NN]
    criterion-born:   [C-NN]
    evaluative-label:
      rank-label:       [comparative ranking in source round]
      quality-dimension: [methodological or pedagogical quality -- not a restatement
                          of rank-label]
    consequence:      [next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY -- every section present. No diffs.]

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Validation: all four columns non-blank in every row.

STEP 4 -- FINDINGS

Column Contract complete. Proceeding to findings.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:
- Failure modes targeted per axis
- Residual weakness after first axis only
- Compound criterion effect (both active): C-NN
- Priority: HIGH / MEDIUM / LOW

[Column Schema Auditor Pass 1 here -- after Step 3, before item 3.]

3. Evaluation order:

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Every row: non-blank Axis Cost Rationale with per-axis structural reason.

[Column Schema Auditor Pass 2 here -- after item 3.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Both must emit results. 4a FAIL does not suppress 4b. 4b FAIL
does not suppress 4a result.

4a -- DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    This annotation exists at this execution site because a model following this
    template cannot omit checkpoint 4b even if it does not read the preamble
    NON-SUPPRESSION INVARIANT CONTRACT or the Column Schema Auditor role
    definition. Co-location at this execution site makes the non-suppression
    invariant inseparable from the action it governs here -- this annotation is
    self-contained and does not depend on preamble or role-definition scope.
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no

  4a Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block to include the missing column
    before committing any evaluation order table. Do not declare this audit complete
    until the missing column is present.

  COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
  audit completion status only. It does not restrict execution order. Checkpoint
  4b executes regardless of this restriction and regardless of the 4a result --
  the non-suppression invariant governs execution sequence; this directive governs
  whether the overall audit may be declared complete.

4b -- POPULATION CHECK:

  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    This annotation exists at this execution site because this checkpoint must
    execute regardless of checkpoint 4a's result. A model following this
    execution template cannot suppress this checkpoint based on 4a outcome even
    if the preamble non-suppression contract or role independence requirement
    is not in scope. Co-location makes this guarantee inseparable from the
    execution action -- this annotation is self-contained.
    EXECUTION DIRECTIVE: Execute this population check. Do not suppress based
    on 4a result.

  For each variation in the evaluation order table:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|

  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite each incomplete row before declaring population check complete.
    Do not declare the population check complete until all rows pass.

  COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
  audit completion status only. It does not restrict the audit result from being
  recorded. Both checkpoint results must appear in the output.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

5. Anchor: one variation. Justify structural impact, isolation quality, and detectable
   failure condition -- one sentence each.
```

---

### V-05 -- Full Integration: Labeled Blocks + Completion-Gate Scoping + Quality Gate (C-33 + C-34 + C-35)

**axis:** lifecycle-emphasis x phrasing-register x role-sequence
**pass-type:** combination

**hypothesis:**
- criterion: C-33 + C-34 + C-35 (all three R10 target criteria simultaneously)
- direction: C-33, C-34, and C-35 each pass in a single skill body; the three mechanisms are
  composable without structural interference; this variation serves as the convergence anchor
  for R10 and as the base candidate for any R11 golden artifact
- mechanism: The labeled block (C-33) is a required input to annotation self-documentation;
  the completion-gate scoping note (C-34) is a required input to advancement-restriction
  disambiguation; the Axis Cost Quality Gate role (C-35) is a required input to Findings
  Synthesizer declaring item 3 complete; all three mechanisms are independently structurally
  necessary and their simultaneous presence is required to produce a skill body where the
  execution-site annotations are self-documenting, the FAIL-path directives are semantically
  unambiguous, and the Axis Cost Rationale cells are quality-verified; no single mechanism
  can be omitted without losing a corresponding criterion
- failure-condition:
    round-label:      R9
    source-variation: V-05
    criterion-born:   C-33
    evaluative-label:
      rank-label:       "highest composite in R9 -- combination of V-01 R9 and V-02 R9, covering C-30 and C-31 simultaneously"
      quality-dimension: "most stable integration point in R9 -- demonstrated that Axis Cost Rationale column (output-format axis, C-30) and execution-site co-location (lifecycle-emphasis axis, C-31) are composable without interaction effects; establishes the R10 combination testing protocol on solid ground by confirming the R9 combination baseline is structurally coherent"
    consequence: if V-05 R10 does not simultaneously pass C-33 + C-34 + C-35, at least one of
      the three mechanisms interferes with the others or is not correctly implemented in
      combination; isolate the failing criterion and return to the corresponding single-axis
      variation (V-01/V-02/V-03) to identify the interaction point

---

```
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

Prohibited pattern -- SHORT-CIRCUIT SUPPRESSION: emitting only the Declaration
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
  [ ] Axis Cost Rationale  <- per-row rationale cell: (1) per-axis structural reason
                              this variation is at this cost level -- not a generic tier
                              rule; (2) independence claim -- why this variation is
                              independent or what prior-round result it depends on.
                              A cell containing only "low" or "Tier 1" with no per-axis
                              reason is structurally incomplete.
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

Column definitions match the Column Contract declarations above. Every row must
have a non-blank Axis Cost Rationale value containing a per-axis structural reason.
A cell containing only a cost level or tier label without a per-axis reason is
structurally incomplete -- rewrite before committing the table.

REQUIRED: Every row must have a non-blank "Axis Cost Rationale" value. A row with
a generic rationale that applies equally to all variations does not satisfy this
requirement.

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
   hypothesis is incomplete -- return to Step 2 before proceeding. Step 4 must
   not begin until this catalog is complete.

4. Column Schema Auditor
   Responsibility: Two independent verification passes.

   PASS 1 -- DECLARATION CHECK (runs after Step 3 is complete, before Step 4
   item 3 is written):
     Verify:
       [ ] Column Contract block is present in the output: yes / no
       [ ] "Axis Cost Rationale" column is explicitly named in the contract: yes / no
       [ ] "Catalog Source" column is explicitly named in the contract: yes / no
     Emit: "Column Schema Auditor Pass 1 complete. Declaration check: [PASS /
     FAIL -- name failing item]."

   PASS 2 -- POPULATION CHECK (runs after Step 4 item 3 is written):
     For each variation in the evaluation order table, verify:
       [ ] Axis Cost Rationale value is non-blank and contains a per-axis reason: yes / no
       [ ] Catalog Source value is non-blank: yes / no
     Emit per row: "V-NN Axis Cost Rationale: [present / missing -- rewrite required].
     V-NN Catalog Source: [populated / blank -- rewrite required]."
     Emit summary: "Column Schema Auditor Pass 2 complete. Population check:
     [PASS -- all rows populated / FAIL -- list blank rows]."

   INDEPENDENCE REQUIREMENT: Pass 1 and Pass 2 are structurally independent.
   A FAIL on Pass 1 does not suppress execution or result emission for Pass 2.
   Both passes must appear in the output regardless of either pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 item 3 complete until Column Schema Auditor has completed both
   passes AND Axis Cost Quality Gate (role 6) has emitted a PASS summary.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes, before
   Findings Synthesizer declares Step 4 item 3 complete. For each row in the
   evaluation order table, classify the Axis Cost Rationale cell:

     STRUCTURAL: the cell names an axis-specific structural property for this
     variation -- a mechanism, dependency, or structural change type that is
     particular to this row (e.g., "single template line change with no role
     dependencies -- low cost because the change surface is isolated";
     "adds a role with nested checkpoint logic -- medium cost because parse
     surface increases for evaluators tracking role interaction"). A structural
     value is falsifiable: it becomes false if applied to a different variation.

     GENERIC: the cell contains only a cost tier ("low", "medium", "high"), a
     tier label ("Tier 1"), or a generic independence claim ("independent, low
     cost", "no prior-round dependency") that applies equally to all rows and
     carries no per-axis analysis. A generic value remains true for any row
     regardless of what variation it describes.

   Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted cell value] /
     GENERIC -- rewrite required [quoted cell value]."

   Emit summary: "Axis Cost Quality Gate: PASS -- all rows structural /
     FAIL -- rows [list V-NN labels] contain generic rationale; rewrite required
     before item 3 may be declared complete."

   Findings Synthesizer must not declare item 3 complete until this role emits
   a PASS summary.

STEP 1 -- SELECT AXES

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes. Do not begin Step 2 until the list is committed.

STEP 2 -- VARIATION BODIES

For each selected axis, write one complete variation body.

### V-NN -- [Axis Name]
axis: [axis name from canonical list]
hypothesis:
  criterion:         [C-NN and name]
  direction:         [expected direction and magnitude]
  mechanism:         [necessity language: "required input to", "cannot be produced
                      without", "must exist before", or equivalent]
  failure-condition:
    round-label:      [R-NN]
    source-variation: [V-NN]
    criterion-born:   [C-NN]
    evaluative-label:
      rank-label:       [comparative ranking in source round]
      quality-dimension: [methodological or pedagogical quality -- not a restatement]
    consequence:      [next action]

A citation block with any required field blank is structurally incomplete.

[COMPLETE SKILL BODY -- every section present. No diffs. No cross-references.]

Do not advance to the next variation until the current body is complete.

STEP 3 -- CROSS-ROUND DEPENDENCY CATALOG

This step is a required input to Step 4. Step 4 must not begin until this
catalog is complete and every row is validated.

| V | Axis | Comparative Claim (quoted) | Prior-Round Result Required | Round + Variation + Metric | Independent |
|---|------|----------------------------|-----------------------------|----------------------------|-------------|

Validation: all four columns non-blank in every row. A blank column means the
hypothesis is incomplete -- return to Step 2 before proceeding.

STEP 4 -- FINDINGS

Complete the Column Contract (declared in the preamble above) before writing any
table in this step. All boxes must be checked. Write: "Column Contract complete.
Proceeding to findings." before any table is written.

1. Variation map:

| V | Axis | Change Made | Hypothesis Summary | C-04 Prediction | C-07 Prediction |
|---|------|-------------|-------------------|-----------------|-----------------|

2. Combination candidates:

For each candidate axis pair, provide all four sub-elements of the compound-effects model:
- **Failure modes targeted per axis**: one criterion failure mode per axis.
- **Residual weakness after first axis only**: concrete gap after only the first axis --
  not a restatement of axis 2.
- **Compound criterion effect (both active)**: specific C-NN achievable only when both
  axes are simultaneously active.
- **Priority**: HIGH / MEDIUM / LOW -- one-sentence rationale.

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

Derived from Step 3 dependency catalog. Apply the EVALUATION ORDER TABLE SCHEMA
defined in the preamble. Column Contract must be complete before writing this table.

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" -- ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" -- ordered after their dependency rounds.

Every row must have a non-blank Axis Cost Rationale with a per-axis structural reason.
A blank or generic Axis Cost Rationale in any row is a required rewrite before this
step is complete.

[Column Schema Auditor Pass 2 emitted here -- after item 3 table is written.]

[Axis Cost Quality Gate emitted here -- after item 3 table is written, before
Findings Synthesizer declares item 3 complete.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a -- DECLARATION CHECK:

  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):
    This annotation exists at this execution site because a model following this
    template cannot omit checkpoint 4b even if it does not read the preamble
    NON-SUPPRESSION INVARIANT CONTRACT or the Column Schema Auditor role
    definition. Co-location at this execution site makes the non-suppression
    invariant inseparable from the action it governs here -- this annotation
    is self-contained and does not depend on preamble or role-definition scope.
    EXECUTION DIRECTIVE: Advance to 4b regardless of this checkpoint's result.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no

  4a Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block to include the missing column
    before committing any evaluation order table. Do not declare this audit complete
    until the missing column is present in the output.

  COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
  audit completion status only. It does not restrict execution order. Checkpoint
  4b executes regardless of this restriction and regardless of the 4a result --
  the non-suppression invariant governs execution sequence; this directive governs
  whether the overall audit may be declared complete.

4b -- POPULATION CHECK:

  NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4b):
    This annotation exists at this execution site because this checkpoint must
    execute regardless of checkpoint 4a's result. A model following this
    execution template cannot suppress this checkpoint based on 4a outcome even
    if the preamble non-suppression contract or role independence requirement is
    not in scope. Co-location makes this guarantee inseparable from the execution
    action -- this annotation is self-contained.
    EXECUTION DIRECTIVE: Execute this population check. Do not suppress based
    on 4a result.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  (One row per variation. "Row Result: populated" if both cells non-blank with
   per-axis reason. "Row Result: incomplete -- rewrite required" if either cell
   blank or generic.)

  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite each incomplete row to include a per-axis structural reason
    in Axis Cost Rationale and a non-blank Catalog Source value before declaring the
    population check complete.

  COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
  audit completion status only. It does not restrict the audit result from being
  recorded or both checkpoint results from appearing in the output. Both must appear.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

## STEP 2 -- SCORE MATRIX

**Base architecture** (shared by all 5 variations): NON-SUPPRESSION INVARIANT CONTRACT,
COLUMN CONTRACT with Axis Cost Rationale, EVALUATION ORDER TABLE SCHEMA, roles 1-5,
Steps 1-4 with terse or labeled co-located annotations, prescriptive FAIL directives,
per-checkpoint labeled results, non-suppression active statement.

**C-01 through C-32 -- All Variations**

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|----|------|------|------|------|------|-------|
| C-01 | E | PASS | PASS | PASS | PASS | PASS | All 5 variations are complete standalone skill bodies |
| C-02 | E | PASS | PASS | PASS | PASS | PASS | Exactly {N} variations labeled V-01 through V-0N in each body |
| C-03 | E | PASS | PASS | PASS | PASS | PASS | Every variation has axis: and hypothesis: fields in the template |
| C-04 | E | PASS | PASS | PASS | PASS | PASS | V-01/V-02/V-03 each change exactly one axis; V-04/V-05 are declared combination (C-04 exception applies) |
| C-05 | E | PASS | PASS | PASS | PASS | PASS | Six canonical axes available; each body selects distinct axes |
| C-06 | R | PASS | PASS | PASS | PASS | PASS | Canonical axis bank covers all six axes in every body |
| C-07 | R | PASS | PASS | PASS | PASS | PASS | Each hypothesis names a concrete observable outcome (criterion ID + direction + mechanism) |
| C-08 | R | PASS | PASS | PASS | PASS | PASS | All required skill sections present in every variation template |
| C-09 | A | PASS | PASS | PASS | PASS | PASS | Combination candidates section present in Step 4 item 2 in all bodies |
| C-10 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order table present with tier-based sequencing in all bodies |
| C-11 | A | PASS | PASS | PASS | PASS | PASS | hypothesis failure-condition blocks include consequence chain (negation clause) |
| C-12 | A | PASS | PASS | PASS | PASS | PASS | Anchor designation declared (V-01 per round anchor designation at top of document) |
| C-13 | A | PASS | PASS | PASS | PASS | PASS | Instructional register is consistent across all non-phrasing-register variations |
| C-14 | A | PASS | PASS | PASS | PASS | PASS | New structural elements (labeled block headers, quality gate role) are axis-attributable |
| C-15 | A | PASS | PASS | PASS | PASS | PASS | failure-condition blocks cite specific prior-round measured baseline (R9 V-02/V-03/V-04 with round labels) |
| C-16 | A | PASS | PASS | PASS | PASS | PASS | V-04 and V-05 carry pass-type: combination header field |
| C-17 | A | PASS | PASS | PASS | PASS | PASS | Combination candidates cite source V-NN hypotheses by label |
| C-18 | A | PASS | PASS | PASS | PASS | PASS | failure-condition blocks name round + variation + criterion-born triple |
| C-19 | A | PASS | PASS | PASS | PASS | PASS | combination candidates include all four compound-effects model sub-elements |
| C-20 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order names cross-round dependencies and sequences dependent variations |
| C-21 | A | PASS | PASS | PASS | PASS | PASS | Mechanism clauses use necessity language throughout all bodies |
| C-22 | A | PASS | PASS | PASS | PASS | PASS | failure-condition evaluative-label includes rank-label in all hypotheses |
| C-23 | A | PASS | PASS | PASS | PASS | PASS | Step 3 is dedicated dependency catalog phase that drives Step 4 evaluation order |
| C-24 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order table includes Catalog Source column with per-row attribution |
| C-25 | A | PASS | PASS | PASS | PASS | PASS | evaluative-label quality-dimension names methodological quality, not only rank |
| C-26 | A | PASS | PASS | PASS | PASS | PASS | COLUMN CONTRACT preamble declares Axis Cost Rationale and Catalog Source with structural incompleteness assertion |
| C-27 | A | PASS | PASS | PASS | PASS | PASS | Step 4 item 4 includes dual-checkpoint audit with Column Schema Auditor Pass 1 + Pass 2 as independent checks |
| C-28 | A | PASS | PASS | PASS | PASS | PASS | "NON-SUPPRESSION INVARIANT ACTIVE" explicit statement in Step 4 item 4 preamble; FAIL on either checkpoint does not suppress the other |
| C-29 | A | PASS | PASS | PASS | PASS | PASS | 4a Declaration Check and 4b Population Check each carry individually labeled PASS/FAIL designations |
| C-30 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order rendered as a table with per-row Axis Cost Rationale cells containing required non-generic values |
| C-31 | A | PASS | PASS | PASS | PASS | PASS | Co-located annotations present in 4a and 4b execution blocks in all 5 bodies |
| C-32 | A | PASS | PASS | PASS | PASS | PASS | Each checkpoint result carries a FAIL-path directive specifying required remediation action |

---

**C-33 through C-35 -- Per-Variation**

**C-33 -- Execution-site invariant labeled self-documentation**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | 4a annotation is a labeled block "NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):" with sub-clause naming why co-location is necessary: "a model following this template cannot omit checkpoint 4b even if it does not read the preamble NON-SUPPRESSION INVARIANT CONTRACT or the Column Schema Auditor role definition. Co-location at this execution site makes the invariant inseparable..." -- labeled header + self-explanatory sub-clause satisfies C-33. Same for 4b block. |
| V-02 | FAIL | 4a annotation is terse: "NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless of this checkpoint's result. A model following this execution template cannot omit 4b even if it ignores the preamble invariant or role definition." This satisfies C-31 (co-location) but is not a labeled block with a named header distinct from its content and a sub-clause explaining its purpose -- C-33 requires the annotation to be self-contained via a labeled structure, not only a terse NOTE-style sentence. FAIL. |
| V-03 | FAIL | Same terse annotation as V-02 base. No labeled block. C-33 FAIL. |
| V-04 | PASS | Both 4a and 4b use labeled block structure with named headers and self-explanatory sub-clauses -- same mechanism as V-01. C-33 PASS. |
| V-05 | PASS | Same labeled block structure as V-01 and V-04. C-33 PASS. |

**C-34 -- FAIL-directive completion-gate semantic distinction**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | FAIL | 4a FAIL directive: "FAIL requires: rewrite the COLUMN CONTRACT block ... Do not declare the Declaration Check complete until the missing item is present." Contains advancement restriction. No COMPLETION-GATE SCOPE note disambiguating this restriction from execution order. C-34 FAIL. |
| V-02 | PASS | 4a FAIL directive: "Do not declare this audit complete until the missing column is present." followed immediately by "COMPLETION-GATE SCOPE: The 'do not declare complete' restriction above governs audit completion status only. It does not restrict execution order. Checkpoint 4b executes regardless..." -- explicit scoping note present for the advancement restriction in 4a. 4b FAIL directive: "Do not declare the population check complete until all rows pass." followed by "COMPLETION-GATE SCOPE: The 'do not declare complete' restriction above governs audit completion status only." -- scoping note present for 4b advancement restriction. Both directives with advancement restrictions carry scoping notes. C-34 PASS. |
| V-03 | FAIL | 4a FAIL directive: "Do not declare Declaration Check complete until the missing item is present." No COMPLETION-GATE SCOPE note. C-34 FAIL. |
| V-04 | PASS | Both 4a and 4b FAIL directives with advancement restrictions carry COMPLETION-GATE SCOPE notes -- same mechanism as V-02. C-34 PASS. |
| V-05 | PASS | Same as V-04. C-34 PASS. |

**C-35 -- Per-row axis-cost rationale content quality gate**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | FAIL | No role 6 (Axis Cost Quality Gate) in roles section. No quality-gate emission point in Step 4 item 3. Column Schema Auditor Pass 2 checks cell presence (populated/blank) but does not classify cell content as STRUCTURAL vs GENERIC. C-35 FAIL. |
| V-02 | FAIL | Same as V-01 -- no Axis Cost Quality Gate role. C-35 FAIL. |
| V-03 | PASS | Role 6 (Axis Cost Quality Gate) present: classifies each Axis Cost Rationale cell as STRUCTURAL (named axis-specific mechanism) or GENERIC (cost tier / generic claim only); emits per-row verdict and PASS/FAIL summary; Findings Synthesizer cannot declare item 3 complete until role 6 emits PASS; Step 4 item 3 includes "[Axis Cost Quality Gate emitted here -- after item 3 table is written, before Findings Synthesizer declares item 3 complete]" placement marker. C-35 PASS. |
| V-04 | FAIL | No role 6. C-35 FAIL. |
| V-05 | PASS | Role 6 present with full STRUCTURAL vs GENERIC classification, per-row and summary emissions, and Findings Synthesizer gate. Same mechanism as V-03. C-35 PASS. |

---

### Composite Scores

Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/27 * 10)
PARTIAL = 0.5 in aspirational tier.

C-01 through C-32: all PASS across all 5 variations (24 aspirational criteria in this range).
C-33/C-34/C-35: each variation passes the specific criteria introduced by its axis.

| V | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Rank |
|---|----------------|------------------|-------------------|-----------|------|
| V-01 | 60 (5/5) | 30 (3/3) | 9.26 (25/27) | **99.26** | 3 (tied) |
| V-02 | 60 (5/5) | 30 (3/3) | 9.26 (25/27) | **99.26** | 3 (tied) |
| V-03 | 60 (5/5) | 30 (3/3) | 9.26 (25/27) | **99.26** | 3 (tied) |
| V-04 | 60 (5/5) | 30 (3/3) | 9.63 (26/27) | **99.63** | 2 |
| V-05 | 60 (5/5) | 30 (3/3) | 10.00 (27/27) | **100.00** | 1 |

Verification V-01: 24 prior aspirational (C-09..C-32) + C-33 + no C-34 + no C-35 = 25/27.
25/27 * 10 = 9.259. 60 + 30 + 9.259 = 99.26. Confirmed.
Verification V-04: 24 prior + C-33 + C-34 = 26/27. 26/27 * 10 = 9.630. 99.63. Confirmed.

---

## STEP 3 -- EXCELLENCE PATTERNS

Spread exists on C-33 (V-01/V-04/V-05 PASS vs V-02/V-03 FAIL), C-34 (V-02/V-04/V-05 PASS
vs V-01/V-03 FAIL), and C-35 (V-03/V-05 PASS vs V-01/V-02/V-04 FAIL).

**Pattern 1 -- Labeled Block Self-Documentation Converts Terse Annotations to Self-Contained Guarantees**
(C-33 spread: V-01/V-04/V-05 PASS, V-02/V-03 FAIL)

V-01/V-04/V-05 upgrade the co-located annotation from a terse inline phrase to a labeled block
with a named header (e.g., "NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a):") and
a self-explanatory sub-clause that states why co-location is necessary: "a model following this
template cannot omit checkpoint 4b even if it does not read the preamble NON-SUPPRESSION INVARIANT
CONTRACT or the Column Schema Auditor role definition." V-02/V-03 retain the terse pattern from R9
V-02's base ("NON-SUPPRESSION INVARIANT CO-LOCATED AT EXECUTION SITE: 4b executes regardless..."),
which satisfies C-31 (co-location present) but not C-33 (annotation is not self-documenting -- its
purpose requires context to understand).

The structural property is: a labeled block with an explanatory sub-clause is a self-contained
semantic unit; a terse note is not. The mechanism: a consumer reading only the 4a block in
V-01/V-04/V-05 can reconstruct the purpose of the annotation without reading the preamble;
a consumer reading only the 4a block in V-02/V-03 sees the invariant asserted but not explained.
Causal layer: structural.
Provenance: V-02, R9 (C-33 first appeared as a pattern in R9 from V-02 "maximum execution-site
coverage").

Assessment: Confirms C-33. Not a new criterion candidate -- C-33 fully captures this mechanism.

**Pattern 2 -- Completion-Gate Scope Note Resolves Advancement-Restriction / Non-Suppression Conflict**
(C-34 spread: V-02/V-04/V-05 PASS, V-01/V-03 FAIL)

V-02/V-04/V-05 add an explicit COMPLETION-GATE SCOPE note immediately after each FAIL-path
directive that contains an advancement restriction. The note states: "The 'do not declare complete'
restriction above governs audit completion status only. It does not restrict execution order.
Checkpoint 4b executes regardless..." V-01/V-03 carry the same FAIL-path directives with
advancement restrictions but no scoping note. The gap is precisely what C-34 formalizes: without
the scoping note, a consumer cannot determine whether "do not declare complete until X" overrides
the non-suppression invariant or coexists with it at a different semantic level.

The structural property is: semantic level annotation for constraints that operate on different
levels (completion gate vs execution order). The mechanism: the scoping note is a required input
to resolving the apparent conflict -- without it, the two constraints ("do not proceed" and
"advance regardless") read as contradictory; with it, each constraint is scoped to its domain and
neither is ambiguous. Causal layer: structural.
Provenance: V-03, R9 (C-34 first appeared as a pattern in R9 from V-03 "strongest C-32
implementation").

Assessment: Confirms C-34. Not a new criterion candidate.

**Pattern 3 -- Quality Gate Role Closes the Gap Between Cell-Presence Enforcement and Cell-Content Quality**
(C-35 spread: V-03/V-05 PASS, V-01/V-02/V-04 FAIL)

V-03/V-05 add an Axis Cost Quality Gate role (role 6) that classifies each Axis Cost Rationale
cell as STRUCTURAL (names an axis-specific mechanism) or GENERIC (contains only a cost tier or
independence claim). V-01/V-02/V-04 have the Column Contract declaring the Axis Cost Rationale
column and the Column Schema Auditor Pass 2 verifying cell presence -- but neither mechanism
enforces content quality. A cell containing only "low" satisfies the schema contract (cell
present) and passes the population check (non-blank) while carrying no analytical value.

The structural property is: quality-gate enforcement at the role level targets cell-content type,
while schema enforcement targets cell-presence only. The mechanism: the Quality Gate role is a
required input to Findings Synthesizer declaring item 3 complete -- a table with a generic
rationale in any row cannot advance to completion; the role's STRUCTURAL vs GENERIC classification
makes the quality distinction machine-checkable rather than analyst-judgment. The Column Contract
alone cannot close this gap because it declares schema requirements (which columns), not content
requirements (what type of value). Causal layer: structural.
Provenance: V-04, R9 (C-35 first appeared as a pattern in R9 from V-04 "strongest C-30
implementation via role-sequence axis").

Assessment: Confirms C-35. Not a new criterion candidate.

---

No additional spread found beyond C-33/C-34/C-35. All prior criteria (C-01..C-32) pass
uniformly across all 5 variations. No new excellence patterns beyond confirmation of the three
R10 target criteria.

**Round 10: zero new excellence patterns.**

---

## STEP 4 -- No new criteria proposed this round.

The three new criteria (C-33, C-34, C-35) were born in R9 and are confirmed in R10.
No patterns emerged that are not already captured by existing criteria.

---

## CONVERGENCE CHECK

**GATE 1 -- TRIAL CONVERGED**: All 5 variations pass all essential criteria (C-01..C-05).
Essential PASS: all 5 variations. No partial or fail on any essential criterion.
TRIAL CONVERGED.

**GATE 2 -- QUEST NOT PLATEAUED**: Round 9 found three new excellence patterns (C-33, C-34, C-35).
Round 10 found zero new excellence patterns.
Only one consecutive zero-pattern round has been reached. Two consecutive zero-pattern rounds
are required for QUEST PLATEAUED. The preceding round (R9) had new patterns.
"Round 9: 3 new patterns found. Round 10: zero new patterns found."
QUEST NOT PLATEAUED.

DO NOT declare golden. TRIAL CONVERGED but QUEST NOT PLATEAUED. Continue to R11.

R11 design: Run five variations with a diverse axis bank targeting confirmed stability of C-33,
C-34, C-35 and any residual boundary conditions. If R11 also finds zero new patterns, dual
convergence is achieved.

---

## ANCHOR DESIGNATION

**Anchor: V-01 (lifecycle-emphasis)**

- Structural impact: The labeled block annotation is the most compositionally load-bearing
  change in R10 -- it is the prerequisite layer for both V-04 and V-05 combinations, making
  it the foundation of the R10 combination stack.
- Isolation quality: V-01 changes exactly the annotation register (terse to labeled block)
  with no role additions or phrasing changes, giving it the cleanest single-axis isolation
  of the three single-axis variations.
- Detectable failure condition: A V-01 failure on C-33 (labeled block absent) is maximally
  diagnosable because the annotation structure is the sole variation from the R9 V-05 base --
  any failure maps directly to the annotation change and cannot be attributed to a confounding
  mechanism.

---

## Quest History

| Round | New Patterns | Gate 1 | Gate 2 |
|-------|-------------|--------|--------|
| R1 | 3 (C-09, C-10, C-11) | NOT CONVERGED | NOT PLATEAUED |
| R2 | 2 (C-12, C-13) | CONVERGED | NOT PLATEAUED |
| R3 | 3 (C-14, C-15, C-16) | CONVERGED | NOT PLATEAUED |
| R4 | 0 | CONVERGED | NOT PLATEAUED (first zero-pattern round) |
| R5 | 0 | CONVERGED | PLATEAUED (second consecutive zero-pattern round) |
| R6 | 3 (C-17, C-18, C-19) | CONVERGED | NOT PLATEAUED (quest-variate split; new criteria from golden architecture) |
| R7 | 3 (C-20, C-21, C-22) | CONVERGED | NOT PLATEAUED |
| R8 | 3 (C-23, C-24, C-25) | CONVERGED | NOT PLATEAUED |
| R9 (rubric v8->v9) | 3 (C-26, C-27, C-28) | CONVERGED | NOT PLATEAUED |
| R9 (rubric v9->v10) | 3 (C-29, C-30, C-31) | CONVERGED | NOT PLATEAUED |
| ... | ... | ... | ... |
| R9 (this cycle) | 3 (C-33, C-34, C-35) | CONVERGED | NOT PLATEAUED |
| **R10** | **0** | **CONVERGED** | **NOT PLATEAUED** |

Note: Quest history rows above R9 are reconstructed from rubric genealogy (C-11..C-35 across
rounds R1..R9). R10 is the first zero-pattern round in the current three-criteria cycle.
R11 is the candidate plateau round.
