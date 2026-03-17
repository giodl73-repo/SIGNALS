Golden document written to `simulations/quest/golden/quest-variate-golden-2026-03-15.md`.

**What's in it:**

- **Frontmatter** — `score: 100`, `status: GOLDEN`, 11 rounds, v10 rubric
- **Prompt body** — simplified form (27% reduction, QU5 PASS): the NON-SUPPRESSION INVARIANT CONTRACT preamble and EVALUATION ORDER TABLE SCHEMA are gone; the COLUMN CONTRACT, all 6 roles, Steps 1-4, and both co-location blocks survive intact
- **Simplification note** — flags the C-33 trade-off: the simplified co-location annotations at 4a/4b keep the named header and EXECUTION DIRECTIVE but drop the explanatory sub-clause, which means full rubric compliance (composite 100) requires restoring those paragraphs from the R11 variate file
- **What made it golden** — four patterns: dual-role column governance, triple-site non-suppression invariant, COMPLETION-GATE SCOPE distinction, full C-33+C-34+C-35 integration
- **Rubric summary** — all 35 criteria in tier tables, with round-of-origin for each aspirational criterion
 V-0N)
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

   Pass 1 and Pass 2 are structurally independent. A FAIL on Pass 1 does not
   suppress execution or result emission for Pass 2. Both passes must appear
   in the output regardless of either pass result.

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
catalog is complete.

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

Complete the Column Contract before writing any table. Write: "Column Contract
complete. Proceeding to findings." before any table is written.

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

Derived from Step 3 dependency catalog. Apply the Column Contract columns.

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
    EXECUTION DIRECTIVE: Execute this population check. Do not suppress based
    on 4a result.

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
    audit completion status only. Both checkpoint results must appear in the output.

Pass 1 failure does not suppress Pass 2 output. Both passes must appear
regardless of either pass result.

C-24 Pass: yes only if Declaration Check Result is PASS AND Population Check
Result is PASS.

5. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.
```

---

## What Made It Golden

Four patterns distinguish V-05 from the baseline (V-01 in any given round):

**1. Dual-role architecture for column governance (C-26 + C-30 + C-35)**
V-05 separates structural concern into two dedicated roles (Column Schema Auditor runs
declaration + population passes; Axis Cost Quality Gate classifies cell content as
STRUCTURAL vs GENERIC). Early variations collapsed these into one pass or omitted the
quality gate entirely. The separation is load-bearing: Pass 1 can fail while Pass 2 still
runs; the quality gate blocks Findings Synthesizer's item 3 completion independently of
whether columns are merely present. Each role has one job and one gate.

**2. Non-suppression invariant at preamble AND execution site (C-27 + C-28 + C-31 + C-33)**
V-05 declares the invariant three times: once in the preamble (governs intent), once as
"NON-SUPPRESSION INVARIANT ACTIVE:" before the checkpoints run (C-28), and once at each
execution site via a named labeled block "NON-SUPPRESSION INVARIANT -- EXECUTION-SITE
CO-LOCATION (4a/4b):" with EXECUTION DIRECTIVE line (C-31/C-33). Variations that relied
on the preamble alone produced short-circuit suppression failures. Co-location at the
execution site makes the invariant inseparable from the action it governs.

**3. COMPLETION-GATE SCOPE distinction in FAIL directives (C-34)**
V-05 distinguishes "audit completion status" from "execution order" within each FAIL
directive. Earlier variations included advancement restrictions ("do not declare complete
until...") without clarifying that the restriction governs completion status only -- not
whether 4b runs. The COMPLETION-GATE SCOPE note resolves the apparent conflict between
"4a FAIL blocks completion" and "4b runs regardless." Without it, a model following the
FAIL directive literally could suppress 4b to avoid declaring the audit complete.

**4. Full integration of all three C-33/C-34/C-35 mechanisms simultaneously (C-12 anchor)**
V-05 is the only variation in the quest history that activates labeled-block annotation
(C-33), completion-gate scoping (C-34), and dedicated quality-gate role (C-35) at the
same time without any single-axis isolation. Single-axis probes confirmed each mechanism
individually; V-05 confirmed they are compositionally stable. A FAIL on any criterion in
V-05 is maximally diagnostic because it represents regression in a previously-verified
architecture.

---

## Simplification Note

The simplified body (27% reduction, QU5 pass) removes the explanatory sub-clauses from
the co-location annotations at 4a and 4b, retaining only the named header and EXECUTION
DIRECTIVE line. This trades C-33 full compliance (which requires both named header AND
explanatory sub-clause) for a smaller prompt. The essential criteria (C-01 through C-05)
are unaffected.

Operators who need full rubric compliance (composite 100, all 35 criteria) should restore
the sub-clause paragraphs at 4a and 4b from the V-05 body in
`quest-variate-variate-R11-2026-03-15.md` (lines 1770-1777 and 1796-1804).

---

## Final Rubric Criteria Summary (v10 -- 35 criteria)

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/27 * 10)`

### Essential (C-01 to C-05) -- 60 pts

| ID | Text |
|----|------|
| C-01 | Each variation is a complete, standalone, runnable skill body |
| C-02 | Exactly {N} variations produced, labeled V-01 through V-0N |
| C-03 | Each variation body includes labeled axis and hypothesis fields |
| C-04 | Single-axis variations change exactly one axis; combination variations explicitly declared |
| C-05 | Canonical axis bank present, covers all six axes |

### Recommended (C-06 to C-08) -- 30 pts

| ID | Text |
|----|------|
| C-06 | Canonical axis bank complete in each variation body (not only in shared preamble) |
| C-07 | Each hypothesis names a concrete observable outcome (criterion ID + direction + mechanism) |
| C-08 | All required skill sections present in every variation template |

### Aspirational (C-09 to C-35) -- 10 pts

| ID | Text | Added |
|----|------|-------|
| C-09 | Combination candidates section present in Step 4 | R2 |
| C-10 | Evaluation order table with tier-based sequencing | R2 |
| C-11 | Hypothesis failure-condition blocks include consequence chain | R2 |
| C-12 | Anchor variation designated and justified | R3 |
| C-13 | Instructional register consistent across non-phrasing-register variations | R3 |
| C-14 | Structural elements introduced by an axis are axis-attributable | R3 |
| C-15 | Failure-condition blocks cite specific prior-round measured baseline | R3 |
| C-16 | Combination variations carry explicit pass-type header | R4 |
| C-17 | Combination candidates cite source variation hypotheses by label | R6 |
| C-18 | Failure-condition blocks name round-variation-criterion triple | R6 |
| C-19 | Combination candidates include all four compound-effects sub-elements | R6 |
| C-20 | Evaluation order names cross-round dependencies explicitly | R7 |
| C-21 | Mechanism clauses use necessity language | R7 |
| C-22 | Failure-condition evaluative-label includes rank-label | R7 |
| C-23 | Step 3 is a dedicated cross-round dependency catalog phase | R8 |
| C-24 | Evaluation order table includes Catalog Source column | R8 |
| C-25 | Evaluative-label quality-dimension names methodological quality, not only rank | R8 |
| C-26 | COLUMN CONTRACT preamble declares Axis Cost Rationale and Catalog Source with structural incompleteness assertion | R9 |
| C-27 | Step 4 compliance audit uses dual-checkpoint structure with independent passes | R9 |
| C-28 | "NON-SUPPRESSION INVARIANT ACTIVE" statement appears before checkpoints run | R9 |
| C-29 | Each checkpoint carries its own labeled PASS/FAIL designation | R9 |
| C-30 | Evaluation order rendered as table with per-row Axis Cost Rationale cells | R9 |
| C-31 | Co-located non-suppression annotations present at both execution sites | R9 |
| C-32 | Each checkpoint result carries FAIL-path directive specifying required remediation | R9 |
| C-33 | Execution-site invariant annotation is a labeled block with named header and self-explanatory sub-clause | R9 (confirmed R10/R11) |
| C-34 | FAIL-path directives with advancement restrictions carry explicit completion-gate scope note | R9 (confirmed R10/R11) |
| C-35 | Dedicated auditor role or step enforces per-row axis-cost rationale content quality and gates Findings Synthesizer's item 3 completion | R9 (confirmed R10/R11) |

**Convergence:** TRIAL CONVERGED + QUEST PLATEAUED at R11.
R10 (zero new patterns) + R11 (zero new patterns) = two consecutive zero-pattern rounds.
Rubric final at v10. No further criteria additions anticipated.
