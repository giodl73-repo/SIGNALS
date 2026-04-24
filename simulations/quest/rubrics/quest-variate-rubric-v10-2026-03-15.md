---
skill: quest-rubric
skill_target: quest-variate
date: 2026-03-15
version: 10
status: final
rounds_to_convergence: 11
prior_version: quest-rubric-variate-R10-2026-03-15.md
---

# Rubric: quest-variate (v10 -- Final)

Evaluates output from the `quest-variate` skill, which generates N distinct prompt variations
of a skill body. Each variation must be complete and runnable, vary along exactly one axis,
and carry a labeled hypothesis.

**Convergence note**: Final rubric at dual convergence (R10 and R11 both found zero new
excellence patterns). No criteria added in R10 or R11. v10 is the terminal version.
35 criteria total.

**Scoring formula**: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/27 * 10)
PARTIAL = 0.5 in aspirational tier. Max score: 100.

---

## Essential Criteria (C-01 to C-05) -- 60 points

| ID | Category | Text | Pass Condition | Added |
|----|----------|------|----------------|-------|
| C-01 | structure | Each variation is a complete, standalone, runnable skill body | The output contains {N} fully-written prompt bodies, each containing every required skill section, with no references to other variations | R1 |
| C-02 | structure | Exactly {N} variations are produced, labeled V-01 through V-0N | The output contains exactly N variation bodies, all labeled per convention | R1 |
| C-03 | structure | Each variation body includes labeled axis and hypothesis fields | Every variation body has an axis: field naming a canonical axis and a hypothesis: field with a concrete prediction | R1 |
| C-04 | correctness | Single-axis variations change exactly one axis; combination variations are explicitly declared | Single-axis variations contain exactly one axis change; any multi-axis variation carries a pass-type: combination header | R1 |
| C-05 | structure | The canonical axis bank is present and covers all six axes | The skill body includes all six axes: role-sequence, output-format, lifecycle-emphasis, phrasing-register, inertia-framing, scoring-granularity | R1 |

---

## Recommended Criteria (C-06 to C-08) -- 30 points

| ID | Category | Text | Pass Condition | Added |
|----|----------|------|----------------|-------|
| C-06 | coverage | The canonical axis bank in each variation body is complete | All six canonical axes are enumerated within each variation body's axis bank, not only in a shared preamble | R1 |
| C-07 | behavior | Each hypothesis names a concrete observable outcome | The hypothesis field includes a criterion ID, a direction (PASS/FAIL/PARTIAL + why), and a structural mechanism -- all three components present | R1 |
| C-08 | structure | All required skill sections are present in every variation template | Steps 1-4, roles section, preambles, and all named templates are fully written in every variation body | R1 |

---

## Aspirational Criteria (C-09 to C-35) -- 10 points

| ID | Category | Text | Pass Condition | Added |
|----|----------|------|----------------|-------|
| C-09 | structure | A combination candidates section is present in Step 4 | Step 4 contains an item proposing axis pairs for combination with failure modes, residual weaknesses, compound effects, and priority | R2 |
| C-10 | structure | An evaluation order table is present with tier-based sequencing | Step 4 contains an evaluation order table assigning each variation to a tier based on cross-round dependency status | R2 |
| C-11 | depth | Hypothesis failure-condition blocks include a consequence chain | The failure-condition block includes a consequence: field stating what the failure implies for the next action | R2 |
| C-12 | behavior | An anchor variation is designated and justified | The output names one variation as the anchor with structural impact, isolation quality, and detectable failure condition justifications | R3 |
| C-13 | behavior | Instructional register is consistent across non-phrasing-register variations | Non-phrasing-register variations use identical register; divergence appears only in phrasing-register axis variations | R3 |
| C-14 | structure | Structural elements introduced by an axis are axis-attributable | Each new structural element in a variation body is attributable to the variation's declared axis | R3 |
| C-15 | depth | Failure-condition blocks cite a specific prior-round measured baseline | The failure-condition block names round (R-NN), variation (V-NN), and criterion (C-NN) as comparison baseline -- all three non-blank | R3 |
| C-16 | structure | Combination variations carry an explicit pass-type header | Any multi-axis variation body includes pass-type: combination in its header block | R4 |
| C-17 | depth | Combination candidates cite source variation hypotheses by label | Each combination candidate in Step 4 item 2 references source variation labels (e.g., "V-01 R10") for each axis it combines | R6 |
| C-18 | depth | Failure-condition blocks name the round-variation-criterion triple | The failure-condition block contains round-label, source-variation, and criterion-born fields, all non-blank | R6 |
| C-19 | structure | Combination candidates include all four compound-effects sub-elements | Each combination candidate contains: (1) failure modes per axis, (2) residual weakness after first axis only, (3) compound criterion effect when both active, (4) priority with rationale | R6 |
| C-20 | structure | Evaluation order names cross-round dependencies explicitly | The evaluation order table includes a Cross-Round Dependency column citing Round + Variation + Metric for dependent variations, or "none" for independent ones | R7 |
| C-21 | correctness | Mechanism clauses use necessity language | Every mechanism: field uses necessity language ("required input to", "cannot be produced without", "must exist before", or equivalent); probabilistic language triggers a required rewrite | R7 |
| C-22 | depth | Failure-condition evaluative-label includes rank-label | The evaluative-label block contains a non-blank rank-label field naming the comparative ranking of the source instance in its round | R7 |
| C-23 | structure | Step 3 is a dedicated cross-round dependency catalog phase | A named Step 3 section exists solely to produce the dependency catalog that drives Step 4 evaluation order; Step 4 must not begin until Step 3 is complete | R8 |
| C-24 | structure | The evaluation order table includes a Catalog Source column | Every row in the evaluation order table has a non-blank Catalog Source value citing the Step 3 row from which it was derived | R8 |
| C-25 | depth | Evaluative-label quality-dimension names methodological quality, not only rank | The quality-dimension field explains the specific methodological or pedagogical quality demonstrated by the source instance; a field that only restates rank-label triggers a required rewrite | R8 |
| C-26 | structure | COLUMN CONTRACT preamble declares Axis Cost Rationale and Catalog Source with structural incompleteness assertion | The skill body contains a COLUMN CONTRACT block that explicitly names both columns and includes an assertion that tables written without completing the contract must not be committed | R9 |
| C-27 | structure | Step 4 compliance audit uses a dual-checkpoint structure with independent passes | Step 4 item 4 contains two named independent checkpoints (Declaration Check and Population Check) each with its own labeled result, declared structurally independent | R9 |
| C-28 | correctness | "NON-SUPPRESSION INVARIANT ACTIVE" statement appears before checkpoints run | Step 4 item 4 includes the explicit statement "NON-SUPPRESSION INVARIANT ACTIVE: Both checkpoints run and emit results regardless of each other's pass/fail state" before either checkpoint executes | R9 |
| C-29 | structure | Each checkpoint carries its own labeled PASS/FAIL designation | 4a and 4b each emit a named result; a single combined audit result does not satisfy this criterion | R9 |
| C-30 | structure | Evaluation order rendered as a table with per-row Axis Cost Rationale cells | The evaluation order table contains an Axis Cost Rationale column; every row has a non-blank cell; a cell containing only a cost level or tier label without a per-axis reason is structurally incomplete | R9 |
| C-31 | structure | Co-located non-suppression annotations are present at both execution sites | The 4a and 4b blocks each contain a co-location annotation at the execution site asserting the other checkpoint runs regardless of this checkpoint's result | R9 |
| C-32 | behavior | Each checkpoint result carries a FAIL-path directive specifying required remediation | The FAIL outcome for each checkpoint includes a concrete directive stating what must be rewritten or corrected before the checkpoint may be declared complete | R9 |
| C-33 | structure | Execution-site invariant annotation is a labeled block with named header and self-explanatory sub-clause | The co-located annotation at each execution site is a labeled block with a named section header AND an explanatory sub-clause stating why co-location is necessary, making the annotation self-contained without cross-referencing preamble or role definitions; a terse inline NOTE with sub-clause content but no named header does not satisfy this criterion | R9 (confirmed R10/R11) |
| C-34 | behavior | FAIL-path directives with advancement restrictions carry an explicit completion-gate scope note | When a FAIL-path directive contains an advancement restriction, a COMPLETION-GATE SCOPE note (or semantically equivalent statement) must appear within the directive's scope, explicitly clarifying that the restriction governs audit completion status only and does not restrict execution order; position of the note (before or after the restriction) does not affect PASS/FAIL; directives without advancement restrictions are exempt | R9 (confirmed R10/R11) |
| C-35 | behavior | A dedicated auditor role or step enforces per-row axis-cost rationale content quality | A dedicated auditor role or embedded pass classifies each Axis Cost Rationale cell as STRUCTURAL (axis-specific mechanism named) or GENERIC (cost tier or generic claim only), emits per-row verdicts and a summary, and gates Findings Synthesizer's item 3 completion on a PASS summary; an embedded pass within an existing role (e.g., Pass 3 of Column Schema Auditor) satisfies "dedicated step"; Findings Synthesizer cannot declare item 3 complete until this role or step emits PASS | R9 (confirmed R10/R11) |
