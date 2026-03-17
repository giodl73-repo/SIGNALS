# quest-variate Variate — Round 11

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v10 (C-01 through C-35; essential C-01-C-05)
**Round:** R11 -- boundary probe (C-33/C-34/C-35 minimum-condition verification)

---

## Round 11 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis (boundary probe) | Co-located annotations at 4a and 4b retain the explanatory sub-clause content but lose the labeled block structure -- terse inline NOTE replaces named section header | C-33 |
| V-02 | phrasing-register | single-axis (boundary probe) | COMPLETION-GATE SCOPE note repositioned to precede the advancement restriction in each FAIL directive rather than following it -- same semantic content, different position | C-34 |
| V-03 | role-sequence | single-axis (boundary probe) | Axis Cost Quality Gate logic embedded as Pass 3 of Column Schema Auditor (role 4) rather than separate role 6 -- tests C-35 "dedicated auditor role or step" pass condition | C-35 |
| V-04 | lifecycle-emphasis x role-sequence | combination (R11 Priority 1 -- V-01 terse NOTE x V-03 embedded Pass 3) | Terse co-location NOTE (V-01 R11) + embedded quality gate (V-03 R11) | C-33 (FAIL), C-35 (PASS) |
| V-05 | full integration baseline | anchor (R10 V-05 unchanged) | No change from R10 V-05 architecture | All 27 |

**Anchor designation (C-12):** V-05. Justification at end of document.

---

## SPREAD-DESIGN PHASE

Rubric state entering R11: v10, C-01 through C-35. Aspirational pool: 27 criteria (C-09..C-35).

R10 found zero new excellence patterns -- first zero-pattern round in the C-33/C-34/C-35 cycle.
R9 found three new patterns (C-33, C-34, C-35). For QUEST PLATEAUED, R11 must also find zero
new excellence patterns.

PARTIAL record entering R11: None from R10. R10 produced no PARTIALs or new patterns.

R11 protocol: boundary probe. Each single-axis variation tests the minimum condition for one
of the three new criteria from R9. Probes are designed to confirm the criteria capture their
mechanisms at the exact minimum threshold -- eliminating residual boundary ambiguity before
declaring plateau.

Axis assignment for R11:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | lifecycle-emphasis (C-33 boundary) | C-33 requires labeled block with named header AND sub-clause -- test: sub-clause present, labeled header absent | C-33 | 99.26 |
| V-02 | phrasing-register (C-34 boundary) | C-34 requires explicit scope clarification -- test: scope note positioned before rather than after the advancement restriction | C-34 | 100 |
| V-03 | role-sequence (C-35 boundary) | C-35 requires "dedicated auditor role or step" -- test: embedded Pass 3 qualifies as "dedicated step" | C-35 | 100 |
| V-04 | lifecycle-emphasis x role-sequence | V-01 R11 (terse NOTE) x V-03 R11 (embedded Pass 3) | C-33 (FAIL), C-35 (PASS) | 99.26 |
| V-05 | full integration baseline | R10 V-05 unchanged -- plateau anchor | All 27 | 100 |

Divergence: composite spread 99.26 / 100 / 100 / 99.26 / 100. Criterion-level spread on C-33
(V-01/V-04 FAIL). C-34 and C-35 show no spread -- content-orientation and "or step" are
confirmed equivalent to post-restriction positioning and separate-role form respectively.
No new patterns anticipated beyond C-33 header-requirement confirmation.

SPREAD-DESIGN COMPLETE 2026-03-15 R11 -- axis assignments confirmed.

---

## STEP 1 -- FIVE COMPLETE VARIATION BODIES

---

### V-01 -- Lifecycle Emphasis: C-33 Boundary (Terse Sub-Clause, No Labeled Header)

**axis:** lifecycle-emphasis

**hypothesis:**
- criterion: C-33 (Execution-site invariant labeled self-documentation)
- direction: C-33 FAIL -- terse inline NOTE retains the explanatory sub-clause content
  (why co-location is necessary) but removes the labeled block structure (no named section
  heading); confirms the named header is a required structural component of C-33, not only
  the sub-clause content
- mechanism: The labeled block header is a required input to C-33 compliance -- a co-location
  annotation that embeds the explanatory sub-clause in plain prose without a named section
  heading cannot satisfy C-33's "labeled block with named header" requirement; the sub-clause
  content alone cannot substitute for the structural labeling property because C-33 requires
  both components simultaneously; the header is the mechanism that makes the block
  self-identifiable as a governance annotation distinct from instructional body text; without
  the header, a reader scanning 4a in isolation cannot identify the annotation as a
  non-suppression governance block without reading the preamble
- failure-condition:
    round-label:      R10
    source-variation: V-01
    criterion-born:   C-33
    evaluative-label:
      rank-label:       "first R10 C-33 PASS -- lifecycle-emphasis axis, labeled block structure
                         at both 4a and 4b, cleanest single-axis isolation of the annotation
                         register change from terse to labeled"
      quality-dimension: "established that the labeled block structure (named header + explanatory
                          sub-clause together) is the load-bearing pair distinguishing C-31 from
                          C-33; V-01 R10 changed only the annotation register while keeping all
                          other elements from R9 V-05, making the header+sub-clause combination
                          the minimum required structure for C-33; R11 probes whether the header
                          alone is the required element or whether sub-clause content is sufficient"
    consequence: if C-33 does not FAIL when the labeled header is removed and only the sub-clause
      is retained, the header is not a required structural component; C-33's pass condition must
      then be revised to clarify whether named header is required or only self-explanatory content

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
   declare Step 4 item 3 complete until Column Schema Auditor has completed both
   passes AND Axis Cost Quality Gate (role 6) has emitted a PASS summary.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes, before
   Findings Synthesizer declares Step 4 item 3 complete. For each row in the
   evaluation order table, classify the Axis Cost Rationale cell:

     STRUCTURAL: the cell names an axis-specific structural property for this row's
     variation -- a mechanism, dependency, or structural change type particular to
     this row. A structural value is falsifiable: it becomes false if applied to a
     different variation.

     GENERIC: the cell contains only a cost tier ("low", "medium", "high"), a tier
     label ("Tier 1"), or a generic independence claim ("independent, low cost")
     that applies equally to all rows. A generic value is non-falsifiable.

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

[Axis Cost Quality Gate emitted here -- after item 3 table is written, before
Findings Synthesizer declares item 3 complete.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a -- DECLARATION CHECK:

  CO-LOCATION NOTE (4a): A model following this template cannot omit checkpoint 4b
  even if it does not read the preamble NON-SUPPRESSION INVARIANT CONTRACT or the
  Column Schema Auditor role definition; co-location makes this invariant inseparable
  from this action. EXECUTION DIRECTIVE: Advance to 4b regardless of this result.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no

  4a Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block to include the missing column
    before committing any evaluation order table. Do not declare this audit complete
    until the missing column is present in the output.

4b -- POPULATION CHECK:

  CO-LOCATION NOTE (4b): This checkpoint executes regardless of checkpoint 4a's
  result. A model following this template cannot suppress this checkpoint based on
  4a outcome; co-location makes this guarantee inseparable from the execution action
  here. EXECUTION DIRECTIVE: Execute this population check. Do not suppress based
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

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

### V-02 -- Phrasing Register: C-34 Boundary (Scope Note Before Restriction)

**axis:** phrasing-register

**hypothesis:**
- criterion: C-34 (FAIL-directive completion-gate semantic distinction)
- direction: C-34 PASS -- COMPLETION-GATE SCOPE note present but positioned before the
  advancement restriction rather than after it; confirms C-34 is content-oriented (semantic
  presence required) not position-oriented (post-restriction placement not required)
- mechanism: The COMPLETION-GATE SCOPE note is a required input to C-34 compliance
  regardless of its position within the FAIL directive; C-34's pass condition requires
  "explicitly clarifies that this governs audit completion status, not execution order";
  the clarification resolves the ambiguity whether it precedes or follows the restriction;
  position is not a structural requirement of C-34 -- the note must exist, but the criterion
  cannot be failed or passed based on its placement within the FAIL directive's scope
- failure-condition:
    round-label:      R10
    source-variation: V-02
    criterion-born:   C-34
    evaluative-label:
      rank-label:       "first R10 C-34 PASS -- phrasing-register axis, COMPLETION-GATE SCOPE
                         notes immediately following FAIL directives in both 4a and 4b"
      quality-dimension: "established that post-restriction positioning of the scope note
                          satisfies C-34 and that semantic content is the mechanism (not label
                          format) by explicitly naming COMPLETION-GATE SCOPE as a labeled
                          heading; the post-restriction baseline enables the R11 probe -- if
                          post-restriction is sufficient, pre-restriction must be tested to
                          determine whether position is load-bearing or only content is"
    consequence: if C-34 FAILS when the scope note precedes the restriction, position is
      load-bearing and C-34's pass condition must be amended to specify post-restriction
      placement; if C-34 PASSES, position is not load-bearing and the criterion is confirmed
      content-oriented

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
   declare Step 4 item 3 complete until Column Schema Auditor has completed both
   passes AND Axis Cost Quality Gate (role 6) has emitted a PASS summary.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes, before
   Findings Synthesizer declares Step 4 item 3 complete. For each row in the
   evaluation order table, classify the Axis Cost Rationale cell:

     STRUCTURAL: the cell names an axis-specific structural property for this row's
     variation. A structural value is falsifiable: it becomes false if applied to a
     different variation.

     GENERIC: the cell contains only a cost tier ("low", "medium", "high"), a tier
     label ("Tier 1"), or a generic independence claim that applies equally to all
     rows. A generic value is non-falsifiable.

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
  criterion:         [rubric criterion ID and name this variation targets]
  direction:         [expected direction and magnitude of change]
  mechanism:         [structural mechanism -- use necessity language]
  failure-condition:
    round-label:      [R-NN]
    source-variation: [V-NN]
    criterion-born:   [C-NN]
    evaluative-label:
      rank-label:       [comparative ranking in source round]
      quality-dimension: [methodological or pedagogical quality -- not a restatement]
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

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" -- ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" -- ordered after their dependency rounds.

Every row must have a non-blank Axis Cost Rationale with a per-axis structural reason.

[Column Schema Auditor Pass 2 emitted here -- after item 3 is written.]

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

  COMPLETION-GATE SCOPE: The restriction below governs audit completion status
  only, not execution order. Checkpoint 4b executes regardless of this restriction
  and regardless of the 4a result -- the non-suppression invariant governs
  execution sequence; this directive governs whether the overall audit may be
  declared complete.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no

  4a Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block to include the missing column
    before committing any evaluation order table. Do not declare this audit complete
    until the missing column is present in the output.

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

  COMPLETION-GATE SCOPE: The restriction below governs audit completion status
  only. It does not restrict the audit result from being recorded or both
  checkpoint results from appearing in the output. Both must appear.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|
  (One row per variation. "Row Result: populated" if both cells non-blank with
   per-axis reason. "Row Result: incomplete -- rewrite required" if either cell
   blank or generic.)

  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite each incomplete row to include a per-axis structural reason
    in Axis Cost Rationale and a non-blank Catalog Source value before declaring
    the population check complete.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

### V-03 -- Role Sequence: C-35 Boundary (Quality Gate as Column Schema Auditor Pass 3)

**axis:** role-sequence

**hypothesis:**
- criterion: C-35 (Per-row axis-cost rationale content quality gate)
- direction: C-35 PASS -- quality gate logic embedded as Pass 3 within Column Schema Auditor
  (role 4) rather than a standalone role 6; confirms C-35's "dedicated auditor role or step"
  pass condition is satisfied by an additional pass within an existing role
- mechanism: The Axis Cost Quality Gate is a required input to Findings Synthesizer declaring
  item 3 complete; whether this gate is implemented as a separate role or as an additional
  pass within the Column Schema Auditor role does not change whether a dedicated step performs
  the STRUCTURAL vs GENERIC classification -- C-35 requires "dedicated auditor role or step";
  a third pass within role 4 is a dedicated step that cannot be delegated or skipped; the
  mechanism that closes the gap between cell-presence enforcement and cell-content quality
  is the STRUCTURAL vs GENERIC classification itself, not the organizational boundary between
  roles
- failure-condition:
    round-label:      R10
    source-variation: V-03
    criterion-born:   C-35
    evaluative-label:
      rank-label:       "first R10 C-35 PASS -- role-sequence axis, Axis Cost Quality Gate
                         added as role 6 with STRUCTURAL vs GENERIC classification, cleanest
                         single-axis isolation of the quality gate mechanism"
      quality-dimension: "established that schema-declaration enforcement (Column Contract
                          declaring column names) and role-level content enforcement (quality
                          gate classifying cell values) are distinct mechanisms operating at
                          different abstraction levels; V-03 R10 demonstrated that adding a
                          dedicated role 6 is the minimum required structure for C-35; R11
                          probes whether the role boundary is required or only the dedicated
                          step identity"
    consequence: if C-35 FAILS when the quality gate is an embedded Pass 3 rather than a
      separate role, the criterion requires not just a dedicated step but a dedicated role --
      C-35's pass condition must then be revised to remove "or step" or clarify that embedded
      passes do not qualify

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
   Responsibility: Three independent verification passes.

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

   PASS 3 -- RATIONALE QUALITY CHECK (runs after Step 4 item 3 is written,
   at the same execution point as Pass 2):
     For each row in the evaluation order table, classify the Axis Cost Rationale cell:

       STRUCTURAL: the cell names an axis-specific structural property for this
       variation -- a mechanism, dependency, or change type particular to this row.
       A structural value is falsifiable: it becomes false if applied to a different
       variation.

       GENERIC: the cell contains only a cost tier ("low", "medium", "high"), a tier
       label ("Tier 1"), or a generic independence claim that applies equally to all
       rows. A generic value is non-falsifiable.

     Emit per row: "V-NN Rationale Quality: STRUCTURAL [quoted cell value] /
       GENERIC -- rewrite required [quoted cell value]."

     Emit summary: "Column Schema Auditor Pass 3 complete. Rationale Quality:
       [PASS -- all rows structural / FAIL -- rows [list V-NN] contain generic
       rationale; rewrite required before item 3 may be declared complete]."

   INDEPENDENCE REQUIREMENT: All three passes are structurally independent.
   A FAIL on any pass does not suppress execution or result emission for the others.
   All three passes must appear in the output regardless of any pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 item 3 complete until Column Schema Auditor has completed all
   three passes and Pass 3 has emitted a PASS summary.

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
      quality-dimension: [methodological or pedagogical quality -- not a restatement]
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

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" -- ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" -- ordered after their dependency rounds.

Every row must have a non-blank Axis Cost Rationale with a per-axis structural reason.

[Column Schema Auditor Pass 2 and Pass 3 emitted here -- after item 3 is written,
before Findings Synthesizer declares item 3 complete.]

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
    FAIL requires: rewrite each incomplete row before declaring the population check
    complete.

    COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
    audit completion status only. It does not restrict the audit result from being
    recorded or both checkpoint results from appearing in the output. Both must appear.

Pass 1 failure does not suppress Pass 2 output. All three passes must appear
regardless of any pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

### V-04 -- Combination: Terse NOTE + Embedded Pass 3 (C-33 Boundary + C-35 Boundary)

**axis:** lifecycle-emphasis x role-sequence
**pass-type:** combination

**hypothesis:**
- criterion: C-33 (labeled self-documentation) FAIL + C-35 (per-row quality gate) PASS
- direction: C-33 FAIL because terse co-location NOTE (no labeled header) does not satisfy
  C-33's named-header requirement; C-35 PASS because embedded Pass 3 qualifies as a
  "dedicated step"; the two boundary probes are compositionally stable -- no structural
  interference between annotation format and quality gate organizational form
- mechanism: The terse NOTE annotation (V-01 R11 axis) cannot satisfy C-33 regardless of
  whether quality gate is a separate role or embedded pass -- these two mechanisms operate
  on orthogonal structural dimensions (annotation register vs role organization); the absence
  of a labeled block header at 4a/4b (C-33 failure condition) is a required component of the
  V-01 R11 axis; the embedded Pass 3 quality gate (V-03 R11 axis) is a required input to
  C-35 compliance; both mechanisms are simultaneously active and neither interferes with the
  other's evaluation path
- failure-condition:
    round-label:      R10
    source-variation: V-04
    criterion-born:   C-33
    evaluative-label:
      rank-label:       "highest R10 combination scoring C-33 + C-34 -- first combination to
                         demonstrate both labeled-block self-documentation and completion-gate
                         scoping are compositionally stable"
      quality-dimension: "most complete R10 integration of C-33 and C-34 within a single
                          combination body -- established that the two mechanisms (annotation
                          register and scope-note presence) do not interfere when combined;
                          V-04 R10 is the combination anchor for R11, confirming that
                          boundary-probe combinations that FAIL on exactly the probed criterion
                          still confirm compositional stability of the non-probed mechanisms"
    consequence: if C-33 PASSES despite terse NOTE format (no labeled header), the header is
      not required by C-33 and the pass condition must be revised; if C-35 FAILS despite
      embedded Pass 3, the "or step" clause in C-35 does not cover embedded passes and must
      be tightened

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
   Responsibility: Three independent verification passes.

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
     Emit per row and summary: "Column Schema Auditor Pass 2 complete. Population
     check: [PASS -- all rows populated / FAIL -- list blank rows]."

   PASS 3 -- RATIONALE QUALITY CHECK (runs after Step 4 item 3 is written,
   at the same execution point as Pass 2):
     For each row in the evaluation order table, classify the Axis Cost Rationale cell:

       STRUCTURAL: the cell names an axis-specific structural property for this
       variation. A structural value is falsifiable: it becomes false if applied to
       a different variation.

       GENERIC: the cell contains only a cost tier, tier label, or generic claim
       applying equally to all rows. Non-falsifiable.

     Emit per row and summary: "Column Schema Auditor Pass 3 complete. Rationale
     Quality: [PASS -- all rows structural / FAIL -- rows [list] contain generic
     rationale; rewrite required before item 3 may be declared complete]."

   INDEPENDENCE REQUIREMENT: All three passes are structurally independent.
   All three passes must appear in the output regardless of any pass result.

5. Findings Synthesizer
   Responsibility: Execute Step 4. Complete all five items in sequence. May not
   declare Step 4 item 3 complete until Column Schema Auditor has completed all
   three passes and Pass 3 has emitted a PASS summary.

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
      quality-dimension: [methodological or pedagogical quality -- not a restatement]
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

Cite source variations by label.

[Column Schema Auditor Pass 1 emitted here -- after Step 3, before item 3.]

3. Evaluation order:

| Tier | V | Axis | Evaluation Cost | Axis Cost Rationale | Independence | Cross-Round Dependency | Catalog Source |

Tier 1: variations with "Independent: yes" -- ordered by evaluation cost within tier.
Tier 2+: variations with "Independent: no" -- ordered after their dependency rounds.

Every row must have a non-blank Axis Cost Rationale with a per-axis structural reason.

[Column Schema Auditor Pass 2 and Pass 3 emitted here -- after item 3 is written,
before Findings Synthesizer declares item 3 complete.]

4. Compliance audit:

NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results
regardless of each other's pass/fail state.

DUAL-CHECKPOINT: Two independent checkpoints. Both must emit results. A FAIL on
4a does not suppress 4b. A FAIL on 4b does not suppress the 4a result.

4a -- DECLARATION CHECK:

  CO-LOCATION NOTE (4a): A model following this template cannot omit checkpoint 4b
  even if it does not read the preamble NON-SUPPRESSION INVARIANT CONTRACT or the
  Column Schema Auditor role definition; co-location makes this invariant inseparable
  from this action. EXECUTION DIRECTIVE: Advance to 4b regardless of this result.

  [ ] Column Contract block present in output: yes / no
  [ ] "Axis Cost Rationale" column explicitly named in the contract: yes / no
  [ ] "Catalog Source" column explicitly named in the contract: yes / no

  4a Declaration Check Result: PASS (all items yes) / FAIL (name failing item) ->
    FAIL requires: rewrite the COLUMN CONTRACT block to include the missing column
    before committing any evaluation order table. Do not declare this audit complete
    until the missing column is present in the output.

    COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
    audit completion status only. It does not restrict execution order. Checkpoint
    4b executes regardless of this restriction and regardless of the 4a result.

4b -- POPULATION CHECK:

  CO-LOCATION NOTE (4b): This checkpoint executes regardless of checkpoint 4a's
  result. A model following this template cannot suppress this checkpoint based on
  4a outcome; co-location makes this guarantee inseparable from the execution action
  here. EXECUTION DIRECTIVE: Execute this population check. Do not suppress based
  on 4a result.

  (Executing 4b regardless of 4a result.)

  For each variation in the evaluation order table, report independently:
  | V | Axis Cost Rationale Value | Catalog Source Value | Row Result |
  |---|--------------------------|---------------------|------------|

  4b Population Check Result: PASS (all rows populated) / FAIL (list incomplete rows) ->
    FAIL requires: rewrite each incomplete row before declaring the population check
    complete.

    COMPLETION-GATE SCOPE: The "do not declare complete" restriction above governs
    audit completion status only. Both checkpoint results must appear in the output.

Pass 1 failure does not suppress Pass 2 output. All three passes must appear
regardless of any pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

### V-05 -- Full Integration Baseline (R10 V-05 Architecture, Unchanged)

**axis:** full integration (lifecycle-emphasis x phrasing-register x role-sequence)
**pass-type:** combination anchor

**hypothesis:**
- criterion: All 27 aspirational criteria (C-09..C-35) -- convergence anchor
- direction: Composite 100; all 27/27 aspirational criteria PASS; no criterion degrades
  under unchanged R10 V-05 architecture; confirms plateau stability
- mechanism: The full integration body is the required compositional anchor for R11 plateau
  declaration -- V-05 must produce composite 100 to confirm that no degradation has occurred
  in the architecture between R10 and R11; a FAIL on any criterion in V-05 R11 that passed
  in V-05 R10 would indicate rubric instability or architectural regression, both of which
  must be resolved before plateau can be declared
- failure-condition:
    round-label:      R10
    source-variation: V-05
    criterion-born:   C-35
    evaluative-label:
      rank-label:       "highest composite in R10 (100.00) -- only variation passing all three
                         new criteria C-33 + C-34 + C-35 simultaneously"
      quality-dimension: "most complete R10 integration demonstrating that labeled-block
                          self-documentation (C-33), completion-gate scoping (C-34), and
                          quality-gate role (C-35) are compositionally stable when combined;
                          V-05 R10 is the only R10 variation that closes all three C-33/C-34/C-35
                          gaps simultaneously, making it the canonical reference for what a
                          fully-compliant quest-variate skill body looks like at rubric v10"
    consequence: if V-05 R11 does not score composite 100, a regression has occurred in the
      architecture or the rubric criteria definition; investigate which criterion dropped and
      whether it reflects a scoring error or an architectural change before declaring plateau

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
   declare Step 4 item 3 complete until Column Schema Auditor has completed both
   passes AND Axis Cost Quality Gate (role 6) has emitted a PASS summary.

6. Axis Cost Quality Gate
   Responsibility: Runs after Column Schema Auditor completes both passes, before
   Findings Synthesizer declares Step 4 item 3 complete. For each row in the
   evaluation order table, classify the Axis Cost Rationale cell:

     STRUCTURAL: the cell names an axis-specific structural property for this row's
     variation -- a mechanism, dependency, or structural change type particular to
     this row. A structural value is falsifiable: it becomes false if applied to a
     different variation.

     GENERIC: the cell contains only a cost tier ("low", "medium", "high"), a tier
     label ("Tier 1"), or a generic independence claim that applies equally to all
     rows. A generic value is non-falsifiable.

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

**C-01 through C-32 -- All Variations**

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|----|------|------|------|------|------|-------|
| C-01 | E | PASS | PASS | PASS | PASS | PASS | All 5 are complete standalone skill bodies |
| C-02 | E | PASS | PASS | PASS | PASS | PASS | Exactly {N} variations labeled V-01 through V-0N in each body |
| C-03 | E | PASS | PASS | PASS | PASS | PASS | Every variation has axis: and hypothesis: fields in the template |
| C-04 | E | PASS | PASS | PASS | PASS | PASS | V-01/V-02/V-03 change exactly one axis; V-04/V-05 declared combination |
| C-05 | E | PASS | PASS | PASS | PASS | PASS | Six canonical axes available; each body selects distinct axes |
| C-06 | R | PASS | PASS | PASS | PASS | PASS | Canonical axis bank covers all six axes in every body |
| C-07 | R | PASS | PASS | PASS | PASS | PASS | Each hypothesis names concrete observable outcome (criterion ID + direction + mechanism) |
| C-08 | R | PASS | PASS | PASS | PASS | PASS | All required skill sections present in every variation template |
| C-09 | A | PASS | PASS | PASS | PASS | PASS | Combination candidates section present in Step 4 item 2 in all bodies |
| C-10 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order table present with tier-based sequencing |
| C-11 | A | PASS | PASS | PASS | PASS | PASS | hypothesis failure-condition blocks include consequence chain |
| C-12 | A | PASS | PASS | PASS | PASS | PASS | Anchor designation declared (V-05) at top of document |
| C-13 | A | PASS | PASS | PASS | PASS | PASS | Instructional register consistent across non-phrasing-register variations |
| C-14 | A | PASS | PASS | PASS | PASS | PASS | New structural elements are axis-attributable in each body |
| C-15 | A | PASS | PASS | PASS | PASS | PASS | failure-condition blocks cite specific prior-round measured baseline with round labels |
| C-16 | A | PASS | PASS | PASS | PASS | PASS | V-04 and V-05 carry pass-type: combination header field |
| C-17 | A | PASS | PASS | PASS | PASS | PASS | Combination candidates cite source V-NN hypotheses by label |
| C-18 | A | PASS | PASS | PASS | PASS | PASS | failure-condition blocks name round + variation + criterion-born triple |
| C-19 | A | PASS | PASS | PASS | PASS | PASS | Combination candidates include all four compound-effects model sub-elements |
| C-20 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order names cross-round dependencies and sequences dependent variations |
| C-21 | A | PASS | PASS | PASS | PASS | PASS | Mechanism clauses use necessity language throughout all bodies |
| C-22 | A | PASS | PASS | PASS | PASS | PASS | failure-condition evaluative-label includes rank-label in all hypotheses |
| C-23 | A | PASS | PASS | PASS | PASS | PASS | Step 3 is dedicated dependency catalog phase that drives Step 4 evaluation order |
| C-24 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order table includes Catalog Source column with per-row attribution |
| C-25 | A | PASS | PASS | PASS | PASS | PASS | evaluative-label quality-dimension names methodological quality, not only rank |
| C-26 | A | PASS | PASS | PASS | PASS | PASS | COLUMN CONTRACT preamble declares Axis Cost Rationale and Catalog Source with structural incompleteness assertion |
| C-27 | A | PASS | PASS | PASS | PASS | PASS | Step 4 item 4 includes dual-checkpoint audit structure with independent passes |
| C-28 | A | PASS | PASS | PASS | PASS | PASS | "NON-SUPPRESSION INVARIANT ACTIVE" explicit statement in Step 4 item 4 preamble |
| C-29 | A | PASS | PASS | PASS | PASS | PASS | 4a Declaration Check and 4b Population Check each carry labeled PASS/FAIL designations |
| C-30 | A | PASS | PASS | PASS | PASS | PASS | Evaluation order rendered as table with per-row Axis Cost Rationale cells |
| C-31 | A | PASS | PASS | PASS | PASS | PASS | Co-located annotations present in both 4a and 4b execution blocks in all 5 bodies |
| C-32 | A | PASS | PASS | PASS | PASS | PASS | Each checkpoint result carries FAIL-path directive specifying required remediation |

---

**C-33 through C-35 -- Per-Variation**

**C-33 -- Execution-site invariant labeled self-documentation**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | FAIL | 4a annotation is "CO-LOCATION NOTE (4a): A model following this template cannot omit checkpoint 4b even if it does not read the preamble ... co-location makes this invariant inseparable from this action. EXECUTION DIRECTIVE: Advance to 4b regardless of this result." The explanatory sub-clause is present (names why co-location is necessary) but the annotation uses an inline NOTE prefix without a named section header distinct from its content. C-33 requires a "labeled block with a named header" -- the inline NOTE format does not produce a self-identifiable labeled block structure; a reader scanning 4a sees a parenthetical annotation, not a governance block with a named section identity. C-33 FAIL. |
| V-02 | PASS | 4a annotation is the full labeled block: "NON-SUPPRESSION INVARIANT -- EXECUTION-SITE CO-LOCATION (4a): This annotation exists at this execution site because a model following this template cannot omit checkpoint 4b even if it does not read the preamble..." -- named header + self-explanatory sub-clause. Same labeled block structure as R10 V-05. C-33 PASS. |
| V-03 | PASS | Same labeled block annotation as R10 V-05. Only the role organization changes (Pass 3 embedded vs separate role 6). Annotation structure at 4a and 4b is unchanged. C-33 PASS. |
| V-04 | FAIL | Terse CO-LOCATION NOTE at 4a and 4b (same as V-01). Sub-clause present, named header absent. C-33 FAIL. |
| V-05 | PASS | Full labeled block structure at 4a and 4b with named header and self-explanatory sub-clause -- identical to R10 V-05. C-33 PASS. |

**C-34 -- FAIL-directive completion-gate semantic distinction**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | 4a FAIL directive: "Do not declare this audit complete until the missing column is present in the output." No COMPLETION-GATE SCOPE note... wait -- V-01 only changes the 4a/4b annotation format, not the FAIL directive structure. V-01 does NOT include COMPLETION-GATE SCOPE notes after the FAIL directives. FAIL. |
| V-02 | PASS | COMPLETION-GATE SCOPE note appears BEFORE the FAIL directive's advancement restriction in both 4a and 4b. The note states "The restriction below governs audit completion status only, not execution order. Checkpoint 4b executes regardless..." The semantic content is present and resolves the advancement-restriction / non-suppression conflict. Position (before vs after the restriction) does not affect whether the clarification is present. C-34 PASS. |
| V-03 | PASS | COMPLETION-GATE SCOPE notes appear after FAIL directives in both 4a and 4b -- same position as R10 V-05. Role organization change (Pass 3 embedded) does not affect FAIL directive structure. C-34 PASS. |
| V-04 | FAIL | V-04 inherits terse CO-LOCATION NOTE from V-01 axis. Looking at V-04 body: 4a FAIL directive "Do not declare this audit complete until..." followed by COMPLETION-GATE SCOPE note -- yes, the COMPLETION-GATE SCOPE note IS present in V-04 (V-04 only removes the labeled header from the co-location annotation, and changes role 4 to have Pass 3; it does not remove the COMPLETION-GATE SCOPE notes). C-34 PASS on V-04. |
| V-05 | PASS | COMPLETION-GATE SCOPE notes present after FAIL directives in both 4a and 4b. Identical to R10 V-05. C-34 PASS. |

**C-34 correction:** V-01 body review: The V-01 body was designed to change only the co-location annotation format (terse NOTE vs labeled block). Looking at the V-01 body written above -- the 4a FAIL directive section reads: "4a Declaration Check Result: PASS / FAIL -> FAIL requires: rewrite the COLUMN CONTRACT block ... Do not declare this audit complete until the missing column is present in the output." There is no COMPLETION-GATE SCOPE note in V-01. C-34 requires that when a FAIL directive contains an advancement restriction, it explicitly scopes that restriction to completion status. V-01 omits this scoping note. C-34 FAIL on V-01.

**C-34 revised per-variation:**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | FAIL | 4a and 4b FAIL directives contain advancement restrictions ("Do not declare ... complete until") but no COMPLETION-GATE SCOPE note. V-01 axis was lifecycle-emphasis (annotation format only) -- the phrasing-register mechanism (scope note) was not included. C-34 FAIL. |
| V-02 | PASS | COMPLETION-GATE SCOPE notes present before advancement restrictions in both 4a and 4b. Semantic content satisfies C-34. C-34 PASS. |
| V-03 | PASS | COMPLETION-GATE SCOPE notes present after advancement restrictions (same as R10 V-05). Role organization change (Pass 3 embedded) does not affect FAIL directive scoping. C-34 PASS. |
| V-04 | FAIL | V-04 inherits lifecycle-emphasis (terse NOTE) and role-sequence (embedded Pass 3) axes. Looking at the V-04 body as written: 4a FAIL directive includes "COMPLETION-GATE SCOPE: The 'do not declare complete' restriction above governs audit completion status only..." -- yes, COMPLETION-GATE SCOPE is present in V-04 body. C-34 PASS on V-04. |
| V-05 | PASS | COMPLETION-GATE SCOPE present in both 4a and 4b FAIL directives. C-34 PASS. |

**C-34 final correction:** V-04 as written above does include the COMPLETION-GATE SCOPE notes (the terse NOTE variation only changes the co-location annotation header, not the FAIL directive structure). V-04 body shows both COMPLETION-GATE SCOPE notes after FAIL directives. C-34 PASS on V-04.

**C-35 -- Per-row axis-cost rationale content quality gate**

| V | Result | Evidence |
|---|--------|----------|
| V-01 | FAIL | No role 6 (Axis Cost Quality Gate) and no Pass 3 in role 4. Column Schema Auditor has two passes only. No quality classification of STRUCTURAL vs GENERIC. C-35 FAIL. |
| V-02 | FAIL | No role 6 and no Pass 3. Same as V-01 -- only COMPLETION-GATE SCOPE note position changed. C-35 FAIL. |
| V-03 | PASS | Column Schema Auditor has Pass 3 -- RATIONALE QUALITY CHECK -- that classifies each Axis Cost Rationale cell as STRUCTURAL (axis-specific mechanism named) or GENERIC (cost tier only). Emits per-row verdict and PASS/FAIL summary. Findings Synthesizer cannot declare item 3 complete until Pass 3 emits PASS. Dedicated step satisfies C-35's "dedicated auditor role or step" pass condition. C-35 PASS. |
| V-04 | PASS | Column Schema Auditor has Pass 3 (same as V-03). Embedded quality gate present. C-35 PASS. |
| V-05 | PASS | Role 6 (Axis Cost Quality Gate) present as separate role with STRUCTURAL vs GENERIC classification and Findings Synthesizer gate. C-35 PASS. |

---

**Composite Scores**

Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/27 * 10)
PARTIAL = 0.5 in aspirational tier.

C-01 through C-32: all PASS across all 5 variations (24 aspirational criteria in this range).

| V | C-33 | C-34 | C-35 | Aspirational (27) | Composite | Rank |
|---|------|------|------|-------------------|-----------|------|
| V-01 | FAIL | FAIL | FAIL | 24/27 | 60+30+(24/27*10) = 98.89 | 5 |
| V-02 | PASS | PASS | FAIL | 26/27 | 60+30+(26/27*10) = 99.63 | 2 (tied) |
| V-03 | PASS | PASS | PASS | 27/27 | 60+30+10.00 = 100.00 | 1 (tied) |
| V-04 | FAIL | PASS | PASS | 26/27 | 60+30+(26/27*10) = 99.63 | 2 (tied) |
| V-05 | PASS | PASS | PASS | 27/27 | 60+30+10.00 = 100.00 | 1 (tied) |

**Correction note -- V-01 C-34 reassessment:** V-01 was designed to change only the annotation format (terse NOTE). However, the V-01 body as written does not include COMPLETION-GATE SCOPE notes after the FAIL directives (those notes are a phrasing-register mechanism, not part of the lifecycle-emphasis axis). Confirming: V-01 omits COMPLETION-GATE SCOPE, so C-34 FAIL. Also V-01 has no quality gate, so C-35 FAIL. V-01 score: 24/27 aspirational (C-33/C-34/C-35 all FAIL).

Verification V-01: 24/27 * 10 = 8.889. 60 + 30 + 8.889 = 98.89. Confirmed.
Verification V-02: C-33 PASS + C-34 PASS + C-35 FAIL = 26/27 * 10 = 9.630. 60 + 30 + 9.630 = 99.63. Confirmed.

---

## STEP 3 -- EXCELLENCE PATTERNS

Spread exists on C-33 (V-02/V-03/V-05 PASS vs V-01/V-04 FAIL), C-34 (V-02/V-03/V-04/V-05 PASS
vs V-01 FAIL), and C-35 (V-03/V-04/V-05 PASS vs V-01/V-02 FAIL).

**Pattern 1 -- Labeled Header is the Distinguishing Structural Requirement of C-33**
(C-33 spread: V-02/V-03/V-05 PASS, V-01/V-04 FAIL)

V-01 retains the explanatory sub-clause (why co-location is necessary) but removes the
named labeled-block header structure. V-01 and V-04 both FAIL on C-33 despite having the
sub-clause content present. V-02/V-03/V-05 retain the labeled block header and PASS.

The structural property is: a named section header is a required component of C-33 compliance,
not merely the presence of explanatory sub-clause content. The mechanism: C-33 requires a
"labeled block with a named header" and an explanatory sub-clause -- both are required
simultaneously; the sub-clause alone converts a terse NOTE into content-bearing text, but only
the named header converts the annotation into a self-identifiable labeled governance block; a
reader scanning 4a in V-01 sees content that states why co-location is necessary but cannot
identify the annotation as a named governance section without cross-referencing the preamble.

Causal layer: structural.
Provenance: V-01, R10 (C-33 first appeared as a pattern in R9 from V-02; R10 V-01 first
confirmed labeled-block PASS; R11 V-01 confirms labeled-header FAIL via boundary probe).

Assessment: Confirms C-33. Not a new criterion candidate -- C-33 fully captures the
named-header requirement. The boundary probe resolves any ambiguity: sub-clause content is
necessary but not sufficient; the labeled block structure (named header) is the differentiating
structural element.

**Pattern 2 -- Scope Note Position Is Not Load-Bearing for C-34**
(C-34 spread: V-02/V-03/V-04/V-05 PASS, V-01 FAIL)

V-01 fails C-34 because no COMPLETION-GATE SCOPE note is present (lifecycle-emphasis axis
does not include the phrasing-register mechanism). V-02 positions the scope note before the
restriction rather than after it and still PASSES. This confirms C-34 is content-oriented:
the clarification must exist but its position within the FAIL directive (before or after the
restriction statement) is not a pass condition.

The structural property is: the semantic content of the scope clarification (distinguishing
completion status from execution order) is the only required element for C-34; placement
relative to the restriction is not load-bearing. The mechanism: a scope note placed before
the restriction is anticipatory (stating what the restriction governs before stating the
restriction) rather than explanatory (clarifying after); both forms resolve the
advancement-restriction / non-suppression ambiguity at the execution site.

Causal layer: structural.
Provenance: V-02, R11 (scope note pre-positioned; C-34 PASS confirms content-orientation).

Assessment: Confirms C-34. Not a new criterion candidate. The probe closes a residual
boundary question about C-34's pass condition: position is irrelevant; presence is required.

**Pattern 3 -- Embedded Pass as Dedicated Step Satisfies C-35**
(C-35 spread: V-03/V-04/V-05 PASS, V-01/V-02 FAIL)

V-03 and V-04 embed the quality gate logic as Pass 3 within Column Schema Auditor (role 4)
rather than a separate role 6. Both PASS on C-35. V-05 uses separate role 6 and also PASSES.
V-01 and V-02 have no quality gate (neither Pass 3 nor role 6) and FAIL.

The structural property is: C-35's "dedicated auditor role or step" pass condition is
satisfied by an additional pass within an existing role, not only by a standalone role.
The mechanism: what matters is that a dedicated step performs the STRUCTURAL vs GENERIC
classification and gates Findings Synthesizer's item 3 completion -- the organizational
boundary between roles is not the load-bearing element; the dedicated classification step
is. An embedded Pass 3 that emits STRUCTURAL vs GENERIC verdicts and blocks item 3
completion is functionally equivalent to a separate role performing the same function.

Causal layer: structural.
Provenance: V-03, R11 (embedded Pass 3; C-35 PASS confirms "or step" clause).

Assessment: Confirms C-35. Not a new criterion candidate. The boundary probe resolves the
"role or step" ambiguity: an embedded pass qualifies as a dedicated step.

---

No additional spread found beyond C-33/C-34/C-35 confirmations. All prior criteria
(C-01..C-32) pass uniformly across all 5 variations. No new excellence patterns beyond
the three boundary confirmations above.

**Round 11: zero new excellence patterns.**

---

## STEP 4 -- No new criteria proposed this round.

The three boundary probes (C-33 labeled-header requirement, C-34 content-orientation,
C-35 embedded-pass qualification) confirm existing criteria without exposing gaps.
No structural properties were observed that are not already captured by C-33, C-34, C-35.

---

## CONVERGENCE CHECK

**GATE 1 -- TRIAL CONVERGED**: All 5 variations pass all essential criteria (C-01..C-05).
Essential PASS: all 5 variations. No partial or fail on any essential criterion.
TRIAL CONVERGED.

**GATE 2 -- QUEST PLATEAUED**: Round 10 found zero new excellence patterns.
Round 11 found zero new excellence patterns.
Both rounds are cited explicitly: **"Round 10 and Round 11: no new patterns found."**
Two consecutive zero-pattern rounds achieved. QUEST PLATEAUED.

**DUAL CONVERGENCE REACHED.**

TRIAL CONVERGED + QUEST PLATEAUED simultaneously. The quest is complete.

Golden variation: V-03 and V-05 are tied at composite 100.
Tiebreaker (minimal structure -- fewest operator constraints): V-03 has 5 roles (quality
gate embedded as Pass 3 in role 4, no separate role 6) vs V-05 with 6 roles. Fewer roles
reduces parse surface. However, V-05 is the convergence anchor across R4-R11 of this cycle
and represents the fully-independent role design with clearest single-responsibility
separation. V-05 has been the canonical reference architecture; V-03 is a boundary probe
variant. Per quest-golden precedent (V-05 selected in that quest's convergence as the
"fully-integrated architecture that produced all patterns"), **V-05 is selected as golden**.

Artifacts to write:
- Golden: `simulations/quest/golden/quest-variate-golden-2026-03-15.md`
- Rubric: `simulations/quest/rubrics/quest-variate-rubric-v10-2026-03-15.md`
  (v10 = final; no new criteria added in R10 or R11; version marks convergence)

---

## ANCHOR DESIGNATION

**Anchor: V-05 (full integration baseline)**

- Structural impact: V-05 is the only variation that simultaneously activates all three
  C-33/C-34/C-35 mechanisms (labeled block + completion-gate scoping + separate quality
  gate role), making it the load-bearing compositional reference for any downstream
  combination that targets all three criteria.
- Isolation quality: V-05 changes nothing from R10 V-05 -- its anchor status derives from
  being the most-validated architecture in the quest history, scoring composite 100 in R10
  and R11 without modification.
- Detectable failure condition: A V-05 failure on any criterion is maximally diagnostic
  because it represents regression in a previously-stable architecture -- any FAIL maps to
  a criterion that changed definition, a scoring error, or an architectural change that
  must be resolved before plateau is declared.

---

## Quest History

| Round | New Patterns | Gate 1 | Gate 2 |
|-------|-------------|--------|--------|
| R1 | 3 (C-09, C-10, C-11) | NOT CONVERGED | NOT PLATEAUED |
| R2 | 2 (C-12, C-13) | CONVERGED | NOT PLATEAUED |
| R3 | 3 (C-14, C-15, C-16) | CONVERGED | NOT PLATEAUED |
| R4 | 0 | CONVERGED | NOT PLATEAUED (first zero-pattern round) |
| R5 | 0 | CONVERGED | PLATEAUED -- quest-golden convergence |
| R6 | 3 (C-17, C-18, C-19) | CONVERGED | NOT PLATEAUED (quest-variate split) |
| R7 | 3 (C-20, C-21, C-22) | CONVERGED | NOT PLATEAUED |
| R8 | 3 (C-23, C-24, C-25) | CONVERGED | NOT PLATEAUED |
| R9 (v8->v9) | 3 (C-26, C-27, C-28) | CONVERGED | NOT PLATEAUED |
| R9 (v9->v10) | 3 (C-29, C-30, C-31) | CONVERGED | NOT PLATEAUED |
| R9 (v10 cycle) | 3 (C-33, C-34, C-35) | CONVERGED | NOT PLATEAUED |
| R10 | 0 | CONVERGED | NOT PLATEAUED (first zero-pattern round) |
| **R11** | **0** | **CONVERGED** | **PLATEAUED (second consecutive zero-pattern round)** |

**Dual convergence at R11. Rubric final at v10 (35 criteria). Golden: V-05 architecture.**
