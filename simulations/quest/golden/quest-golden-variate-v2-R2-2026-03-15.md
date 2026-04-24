# quest-golden Variate — Round 2 (against rubric v2)

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v2 (C-01 through C-12; essential C-01–C-05; aspirational C-09–C-12)
**Round:** R2 — 3 single-axis passes (V-01/V-02/V-03) + 2 combination passes (V-04/V-05)

**Round 2 design note:** Round 1 (against rubric v1) produced two excellence signals
absorbed into v2 as aspirational criteria:

- **C-11** — Composite formula embedded inline with concrete denominators
  R1 V-01/V-02 scored 80 and included inline formulas (scored ~80 under v1). R1 V-03/V-04/V-05
  used symbolic denominators (`N_essential`) or placed the formula outside the scoring section.
  The only structural difference was formula placement and resolution.

- **C-12** — Anti-conflation guard present in the dual-gate section
  R1 V-03 ("Do not conflate TRIAL CONVERGED with QUEST PLATEAUED") and V-04 ("A single
  paragraph covering both is not acceptable") had explicit prohibitions. R1 V-01/V-02/V-05
  lacked any such guard.

No R1 variation had both. Round 2 isolates each mechanism, then combines.

**v2 formula (resolved denominators required):**
```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/4 * 10)
```

**Failure modes newly documented in v2:**
- QG-08: Score matrix present but COMPOSITE row uses symbolic denominator (e.g., `N_essential`)
- QG-09: Gate declarations present but anti-conflation guard absent — operator produces a merged gate paragraph

---

## Round 2 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | output-format | single-axis | COMPOSITE row in score matrix template contains formula with resolved denominators from active rubric; operator must fill counts before filling composite | C-11 |
| V-02 | phrasing-register | single-axis | Dual-gate section opens with IS:/IS NOT: constitutive pair defining conflation; the IS NOT form names the required two-section structure | C-12 |
| V-03 | lifecycle-emphasis | single-axis | Phase 2 scoring ends with a mandatory "2b — denominator resolution" sub-step (E=[n], R=[n], A=[n]) that must complete before the COMPOSITE row is written | C-11 |
| V-04 | output-format × phrasing-register | combination (R2 Priority 1) | Score matrix COMPOSITE row requires resolved formula (V-01 mechanism) + IS:/IS NOT anti-conflation pair at gate header (V-02 mechanism); both applied simultaneously | C-11, C-12 |
| V-05 | inertia-framing × lifecycle-emphasis | combination (R2 Priority 2) | Status-Quo Golden competitor named at top (fails Failure 1: symbolic denominators; fails Failure 2: merged gate paragraph); denominator-resolution sub-step closes Failure 1 mechanically | C-11, C-12 |

**Anchor designation:** V-04. Targets both new criteria via orthogonal mechanisms (format
change for C-11, phrasing change for C-12). No sub-step overhead. Detectable failure mode:
if V-04 passes C-11 but fails C-12, the IS/IS NOT pair is insufficient and a harder gate is
needed; if V-04 fails C-11 despite the matrix template, the template instruction is
insufficient and a lifecycle sub-step (V-03 mechanism) must be added in Round 3.

---

## V-01 — Output Format: Formula-Anchored COMPOSITE Row

**axis:** output-format
**hypothesis:** R1 V-03/V-04/V-05 scored 68 and would fail C-11. Their matrices used
symbolic denominators or placed the formula in a separate reference section. Operators
write the COMPOSITE row after completing criterion rows — this is the moment the formula
is needed. If the formula with resolved denominators is present in the score matrix
template as part of the COMPOSITE row instructions, the operator must write it at the
point of use. The resolved formula is not retrievable from memory or a prior section; it
must be computed at authoring time. Failure condition: if COMPOSITE row formula presence
does not improve relative to R1 V-03/V-04/V-05, the issue is not template placement but
prompt omission of the formula entirely (the operator skips it regardless of template).

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the full variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE DEFINITION
  TRIAL CONVERGED: all variations in this round pass every essential rubric criterion.
  QUEST PLATEAUED: this round AND the immediately preceding round both found zero new
    excellence patterns.
Both gates must be satisfied simultaneously in the same round.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete, runnable skill body variations.

Round 1: vary exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Before writing any variation, assign axes and verify at least two variations will diverge
on at least one criterion. Rounds where all variations produce identical composite scores
generate no excellence patterns — no patterns means the round does not count toward the
two consecutive zero-pattern rounds required for plateau detection. Design divergence first.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each:
  ## V-NN — [Axis Name]
  axis: [name]
  hypothesis: [criterion expected to change + direction]
  [full prompt body — every instruction, every step, every output contract]

DO NOT proceed to Step 2 until all {N} variation bodies are written in full.

---

STEP 2 — SCORE EACH VARIATION

Score every criterion for every variation. Per-criterion scores come before composite.

For each variation, complete this scorecard before starting the next:

### SCORECARD: V-NN — [axis label]

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS/FAIL | [quote or structural note] |
| C-02 | E | PASS/FAIL | [quote or structural note] |
| C-03 | E | PASS/FAIL | [quote or structural note] |
| C-04 | E | PASS/FAIL | [quote or structural note] |
| C-05 | E | PASS/FAIL | [quote or structural note] |
| C-06 | R | PASS/FAIL | [quote or structural note] |
| C-07 | R | PASS/FAIL | [quote or structural note] |
| C-08 | R | PASS/FAIL | [quote or structural note] |
| C-09 | A | PASS/FAIL | [quote or structural note] |
| C-10 | A | PASS/FAIL | [quote or structural note] |
| C-11 | A | PASS/FAIL | [quote or structural note] |
| C-12 | A | PASS/FAIL | [quote or structural note] |
| **COMPOSITE** | — | [value] | Count criteria from active rubric: E=[n], R=[n], A=[n]. Compute: `(E_pass/[E] * 60) + (R_pass/[R] * 30) + (A_pass/[A] * 10)` = [result] |

The COMPOSITE evidence cell must show the formula with resolved counts from the rubric
provided in {rubric-content}. Count the criteria before writing the formula. Do not use
N_essential, N_recommended, or N_aspirational as denominators.

Complete each variation's full scorecard before starting the next variation.

After all {N} scorecards are complete, produce the summary:

| V | COMPOSITE | RANK | Essential failures |
|---|-----------|------|--------------------|

DO NOT proceed to Step 3 until all scorecards have evidence in every row.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation outperforms another:
  Pattern name: [short label]
  Mechanism: [structural property present in passing variations, absent from failing ones]
  Principle: [transferable rule — not "V-02 scored higher" but the design choice that caused it]
  Scope: skill-specific | transferable

If no variation outperforms any other on any criterion, state exactly:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

List any criterion all variations fail:
  Diagnosis: rubric-gap | skill-gap

DO NOT proceed to Step 4 until all patterns have mechanisms stated.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each excellence pattern from Step 3, propose a criterion with all five fields:
  ID:             C-[NN] (next sequential ID after current rubric's highest)
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence; no interpretation required]

DO NOT proceed to convergence check until all proposed criteria have all five fields.

---

CONVERGENCE CHECK

GATE 1 — TRIAL CONVERGENCE

Ask: do all {N} variations in this round pass every essential criterion?

List every essential criterion (C-01 through C-05). Verify each variation against each.

State exactly one of:
  TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

DO NOT proceed to Gate 2 until Gate 1 is declared.

---

GATE 2 — PLATEAU DETECTION

Ask: did Step 3 in this round AND in the immediately preceding round both find zero new
excellence patterns?

Name the current round by label. State what Step 3 found.
Name the immediately preceding round by label. State what Step 3 found.
Do not write "the last two rounds."

State exactly one of:
  QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

DO NOT declare QUEST PLATEAUED unless both rounds are explicitly named and both confirm
zero new patterns.

---

DUAL CONVERGENCE RULE

Declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, verbatim, runnable. Not a summary. Not a description.
3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields per criterion, round of addition noted.
4. State both file paths.

---

## V-02 — Phrasing Register: IS:/IS NOT: Anti-Conflation Constitutive Pair

**axis:** phrasing-register
**hypothesis:** R1 V-03 ("Do not conflate TRIAL CONVERGED with QUEST PLATEAUED. They are
independent gates.") and V-04 ("A single paragraph covering both is not acceptable") both
passed what would have been C-12. Both used imperative prohibitions. V-02 tests whether
restructuring the same prohibition as a constitutive IS/IS NOT pair increases durability.
The IS form defines what two-gate independence looks like; the IS NOT form names the
forbidden merged-paragraph form. A definitional pair fires at authoring time — the operator
reads the definition before writing the gate section and knows the required form before
producing output, rather than violating a prohibition they may not encounter until
gate-section time. Failure condition: if C-12 pass rates are not higher than R1 V-03/V-04
(imperative prohibition), the constitutive form adds no benefit over the simpler imperative
form and should not be carried into combination runs.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the full variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE DEFINITION
  TRIAL CONVERGED: all variations pass every essential rubric criterion this round.
  QUEST PLATEAUED: this round AND the immediately preceding round both found zero new
    excellence patterns.
Both gates must be satisfied simultaneously in the same round.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete, standalone skill body variations.

Round 1: vary exactly one axis per variation.
Round 2+: combine axes that produced signal in prior rounds.

Before writing any variation, assign axes. Verify at least two variations target different
criteria. Rounds where all variations produce identical composite scores cannot advance
plateau detection — identical scores produce no spread, no spread produces no patterns, and
no patterns cannot count toward the two-round plateau requirement. Design divergence first.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each:
  ## V-NN — [Axis Name]
  axis: [name]
  hypothesis: [criterion expected to change + direction]
  [complete skill body — all instructions, all steps, all output contracts]

DO NOT proceed to Step 2 until all {N} bodies are complete.

---

STEP 2 — SCORE EACH VARIATION

Score every criterion for every variation. Per-criterion scores precede composite.

| Criterion | Weight | V-01 | V-02 | ... |
|-----------|--------|------|------|-----|
| C-01      | E      |      |      |     |
| C-02      | E      |      |      |     |
| C-03      | E      |      |      |     |
| C-04      | E      |      |      |     |
| C-05      | E      |      |      |     |
| C-06      | R      |      |      |     |
| C-07      | R      |      |      |     |
| C-08      | R      |      |      |     |
| C-09      | A      |      |      |     |
| C-10      | A      |      |      |     |
| C-11      | A      |      |      |     |
| C-12      | A      |      |      |     |
| COMPOSITE |        |      |      |     |
| RANK      |        |      |      |     |

DO NOT proceed to Step 3 until all cells have per-criterion results with evidence.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation outperforms another:
  Pattern name: [label]
  Mechanism: [structural property present in passing, absent in failing]
  Principle: [transferable rule — state the design choice, not a comparison]
  Scope: skill-specific | transferable

If no spread: "No score spread found. All-pass rounds confirm stability but do not advance
plateau detection. Redesign for divergence."

List all-fail criteria with diagnosis: rubric-gap | skill-gap.

DO NOT proceed to Step 4 until patterns name mechanisms.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern:
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence]

---

CONVERGENCE CHECK

**INDEPENDENT GATES IS:** two separately labeled sections — GATE 1 and GATE 2 — each with
its own question, its own evidence, and its own state declaration. GATE 1 asks whether
variations pass essential criteria. GATE 2 asks whether two consecutive rounds found no new
patterns. These are different questions requiring different evidence. Two scorers reading
only the convergence section must be able to audit each gate independently.

**INDEPENDENT GATES IS NOT:** a merged paragraph that combines criterion pass-rates with
pattern-discovery history into a single verdict. A merged paragraph cannot be audited: a
scorer cannot verify the trial question without examining the score matrix, and cannot
verify the plateau question without examining the excellence-pattern sections. One paragraph,
two gates, zero auditability.

---

GATE 1 — TRIAL CONVERGENCE

Ask: do all {N} variations in this round pass every essential criterion?

List essential criteria (C-01 through C-05). Check each variation against each.

State exactly one of:
  TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [continue per failing pair]

DO NOT write Gate 2 until Gate 1 is declared.

---

GATE 2 — PLATEAU DETECTION

Ask: did Step 3 in this round AND in the immediately preceding round both find zero new
excellence patterns?

Name the current round by label. State what Step 3 found.
Name the immediately preceding round by label. State what Step 3 found.
Do not write "the last two rounds" or "the previous two rounds."

State exactly one of:
  QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

DO NOT declare QUEST PLATEAUED unless both rounds are explicitly named and both show zero
new patterns.

---

DUAL CONVERGENCE RULE

Declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED in the same round.
TRIAL CONVERGED alone is not sufficient. QUEST PLATEAUED alone is not sufficient.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, verbatim, runnable. Not a summary.
3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields per criterion, round of addition noted.
4. State both file paths.

---

## V-03 — Lifecycle Emphasis: Denominator-Resolution Sub-Step

**axis:** lifecycle-emphasis
**hypothesis:** R1 V-03/V-04/V-05 failed C-11 (would have). Their score matrices used
symbolic denominators or placed the formula outside the scoring section. The mechanism
is timing: the formula is written as part of the score matrix template, before criteria
are counted. If the formula appears in the template, the operator may copy the template
form — including symbolic denominators — without substituting actual counts. A
denominator-resolution sub-step forces the operator to count criteria (E=[n], R=[n],
A=[n]) before writing the COMPOSITE row. This is a structural gate: the COMPOSITE row
cannot be completed without the sub-step output because the sub-step output provides the
denominators the COMPOSITE row requires. This differs from V-01's approach: V-01 anchors
the formula in the template; V-03 forces active computation of the denominators as a named
lifecycle step. If V-03 passes C-11 and V-01 does not, the issue is active computation (not
template anchoring). If both pass, the mechanisms are equivalent and the simpler one (V-01)
is preferred.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the full variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE DEFINITION
  TRIAL CONVERGED: all variations pass every essential rubric criterion this round.
  QUEST PLATEAUED: this round AND the immediately preceding round both found zero new
    excellence patterns.
Both gates must be satisfied simultaneously in the same round.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete, standalone skill body variations.

Round 1: vary exactly one axis per variation.
Round 2+: combine axes that produced signal in prior rounds.

Active spread-design: before writing any variation, assign axes and verify divergence. A
round where all variations produce identical composite scores cannot advance plateau
detection. Identical scores → no spread → no patterns → round does not count toward the
two-round plateau requirement. Design divergence before writing.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each:
  ## V-NN — [Axis Name]
  axis: [name]
  hypothesis: [criterion + direction]
  [full prompt body]

DO NOT proceed to Step 2 until all {N} bodies are complete.

---

STEP 2 — SCORE EACH VARIATION

Score every criterion for every variation. Per-criterion scores precede composite.

For each variation V-NN, complete all three scoring sub-steps before starting the next:

**Sub-step 2a — Per-criterion scoring:**

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS/FAIL | [quote or structural note] |
| C-02 | E | PASS/FAIL | [quote or structural note] |
| C-03 | E | PASS/FAIL | [quote or structural note] |
| C-04 | E | PASS/FAIL | [quote or structural note] |
| C-05 | E | PASS/FAIL | [quote or structural note] |
| C-06 | R | PASS/FAIL | [quote or structural note] |
| C-07 | R | PASS/FAIL | [quote or structural note] |
| C-08 | R | PASS/FAIL | [quote or structural note] |
| C-09 | A | PASS/FAIL | [quote or structural note] |
| C-10 | A | PASS/FAIL | [quote or structural note] |
| C-11 | A | PASS/FAIL | [quote or structural note] |
| C-12 | A | PASS/FAIL | [quote or structural note] |

**Sub-step 2b — Denominator resolution (required before COMPOSITE):**

Count criteria by tier in the rubric provided in {rubric-content}:

```
E = [count of essential criteria]    (C-01 through C-??)
R = [count of recommended criteria]  (C-?? through C-??)
A = [count of aspirational criteria] (C-?? through C-??)
```

DO NOT proceed to sub-step 2c until this block is written with integer counts.

**Sub-step 2c — Composite computation:**

COMPOSITE = (E_pass/[E] * 60) + (R_pass/[R] * 30) + (A_pass/[A] * 10) = [score]

After completing sub-steps 2a → 2b → 2c for all {N} variations, produce the summary:

| V | COMPOSITE | RANK | Essential failures |
|---|-----------|------|--------------------|

DO NOT proceed to Step 3 until all variations have completed all three sub-steps.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation outperforms another:
  Pattern name: [label]
  Mechanism: [structural property present in passing, absent in failing]
  Principle: [transferable rule]
  Scope: skill-specific | transferable

If no spread: "No score spread found. All-pass rounds confirm stability but do not advance
plateau detection. Redesign for divergence."

All-fail criteria → diagnosis: rubric-gap | skill-gap.

DO NOT proceed to Step 4 until patterns name mechanisms.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern:
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence]

---

CONVERGENCE CHECK — TWO INDEPENDENT GATES

Execute both gates fully and separately. Do not conflate them. Do not write a single
paragraph covering both. The two gates ask different questions (criterion pass-rates vs.
pattern-discovery history), require different evidence, and must be declared separately.

GATE 1 — TRIAL CONVERGENCE

Ask: do all {N} variations pass every essential criterion?

List essential criteria (C-01 through C-05). Check each variation against each.

State exactly one of:
  TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [continue per failing pair]

---

GATE 2 — PLATEAU DETECTION

Ask: did Step 3 in this round AND in the immediately preceding round both find zero new
excellence patterns?

Name the current round by label. State what Step 3 found.
Name the immediately preceding round by label. State what Step 3 found.
Do not write "the last two rounds."

State exactly one of:
  QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

---

DUAL CONVERGENCE RULE

Declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, verbatim, runnable. Not a summary.
3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields per criterion, round of addition noted.
4. State both file paths.

---

## V-04 — Output Format × Phrasing Register: Formula-Anchored COMPOSITE Row + IS:/IS NOT: Anti-Conflation Guard

**axis:** output-format × phrasing-register
**hypothesis:** V-01 (formula anchored in scorecard COMPOSITE row) and V-02 (IS/IS NOT
anti-conflation pair at gate header) each target one new criterion. The combination tests
whether the mechanisms are independent: if both can be applied in the same prompt without
structural interference, V-04 should pass both C-11 and C-12. C-11 is addressed in Step 2
(scoring section); C-12 is addressed in the convergence check section. These are distinct
sections of the prompt. The only interaction risk is cognitive load — adding structure to
both sections may cause an operator to abbreviate one. Failure mode to watch: if V-04 passes
C-11 and fails C-12, the operator compressed the gate section to compensate for the scorecard
overhead. If V-04 passes C-12 and fails C-11, the IS/IS NOT pair distracted from resolving
denominators. If neither fails, the combination is effective and is a Round 3 anchor candidate.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

Run the full variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE DEFINITION
  TRIAL CONVERGED: all variations pass every essential rubric criterion this round.
  QUEST PLATEAUED: this round AND the immediately preceding round both found zero new
    excellence patterns.
Both gates must be satisfied simultaneously in the same round.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete, standalone skill body variations.

Round 1: vary exactly one axis per variation.
Round 2+: combine axes that produced signal in prior rounds.

Active spread-design: assign axes before writing. Verify at least two variations target
different criteria. Rounds where all variations produce identical composite scores do not
advance plateau detection — identical scores produce no excellence patterns, and no new
patterns cannot count toward the two-round plateau gate. Design divergence first.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each:
  ## V-NN — [Axis Name]
  axis: [name]
  hypothesis: [criterion + direction]
  [complete skill body — every instruction, every step, every output contract]

DO NOT proceed to Step 2 until all {N} bodies are complete. No placeholders.

---

STEP 2 — SCORE EACH VARIATION

Score every criterion for every variation. Per-criterion scores come before composite.

For each variation, produce one complete scorecard before starting the next:

### SCORECARD: V-NN — [axis label]

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS/FAIL | [quote or structural reference] |
| C-02 | E | PASS/FAIL | [quote or structural reference] |
| C-03 | E | PASS/FAIL | [quote or structural reference] |
| C-04 | E | PASS/FAIL | [quote or structural reference] |
| C-05 | E | PASS/FAIL | [quote or structural reference] |
| C-06 | R | PASS/FAIL | [quote or structural reference] |
| C-07 | R | PASS/FAIL | [quote or structural reference] |
| C-08 | R | PASS/FAIL | [quote or structural reference] |
| C-09 | A | PASS/FAIL | [quote or structural reference] |
| C-10 | A | PASS/FAIL | [quote or structural reference] |
| C-11 | A | PASS/FAIL | [quote or structural reference] |
| C-12 | A | PASS/FAIL | [quote or structural reference] |
| **COMPOSITE** | — | [value] | Count from {rubric-content}: E=[n], R=[n], A=[n]. Formula: `(E_pass/[E] * 60) + (R_pass/[R] * 30) + (A_pass/[A] * 10)` = [result] |

The COMPOSITE evidence cell must show the formula with concrete counts. Count criteria from
{rubric-content} before writing the denominators. Do not use N_essential, N_recommended, or
N_aspirational. The formula in the evidence cell must match the formula in the rubric.

After all {N} scorecards are complete, produce the summary:

| V | COMPOSITE | RANK | Essential failures |
|---|-----------|------|--------------------|

DO NOT proceed to Step 3 until all scorecards have evidence in every row.

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation outperforms another:
  Pattern name: [label]
  Mechanism: [structural property present in passing, absent in failing]
  Principle: [transferable rule]
  Scope: skill-specific | transferable

If no spread: "No score spread found. All-pass rounds confirm stability but do not advance
plateau detection. Redesign for divergence."

All-fail criteria → diagnosis: rubric-gap | skill-gap.

DO NOT proceed to Step 4 until all patterns have mechanisms stated.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern:
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence]

---

CONVERGENCE CHECK

**CONFLATION IS:** writing a single paragraph that addresses both "do variations pass
essential criteria?" and "have two consecutive rounds found no new patterns?" without
labeling them as Gate 1 and Gate 2. A merged paragraph cannot be audited per-gate because
the two questions have different evidence requirements: the trial question requires reading
score matrix rows; the plateau question requires reading the excellence-pattern log across
two named rounds. One paragraph cannot satisfy both requirements. A merged verdict is not
acceptable regardless of correctness.

**CONFLATION IS NOT:** two separately labeled sections, each with its own question, its
own evidence, and its own state declaration (TRIAL CONVERGED/NOT CONVERGED for Gate 1;
QUEST PLATEAUED/NOT PLATEAUED for Gate 2). This is the only acceptable form.

---

GATE 1 — TRIAL CONVERGENCE

Ask: do all {N} variations pass every essential criterion this round?

List essential criteria (C-01 through C-05). Verify each variation against each.

State exactly one of:
  TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [continue per failing pair]

DO NOT write Gate 2 until Gate 1 is declared.

---

GATE 2 — PLATEAU DETECTION

Ask: did Step 3 in this round AND in the immediately preceding round both find zero new
excellence patterns?

Name the current round by label. State what Step 3 found.
Name the immediately preceding round by label. State what Step 3 found.
Do not write "the last two rounds" or "the previous two rounds."

State exactly one of:
  QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

DO NOT declare QUEST PLATEAUED unless both rounds are explicitly named and both show zero
new patterns.

DUAL CONVERGENCE RULE: declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED in
the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, verbatim, runnable. Not a summary. Not a description.
3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields per criterion, round of addition noted.
4. State both file paths.

---

## V-05 — Inertia Framing × Lifecycle Emphasis: Status-Quo Golden Competitor + Denominator Audit

**axis:** inertia-framing × lifecycle-emphasis
**hypothesis:** The status-quo golden competitor motivates WHY C-11 and C-12 matter; the
denominator-resolution sub-step (V-03 mechanism) enforces C-11 mechanically. These two
mechanisms operate at different points: competitor framing fires at the generation phase
header (the operator reads the failure pattern before writing anything); the denominator
sub-step fires mid-scoring (the operator must produce E=[n] counts before writing the
COMPOSITE row). If motivation alone were sufficient, V-05 would be redundant with V-02.
If mechanical forcing alone were sufficient, V-05 would be redundant with V-03. The
hypothesis is that they address different failure modes: operators who understand C-11 but
forget to resolve denominators are helped by the sub-step; operators who do not understand
why C-12 matters (and compress the gate section) are helped by the competitor framing. If
V-05 passes both C-11 and C-12 at higher rates than V-03 alone (which only addresses C-11)
or V-02 alone (which only addresses C-12), the mechanisms are complementary, not redundant.

---

You are running /quest:golden for Signal skill: {skill-name}.

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

**THE STATUS-QUO GOLDEN**

Every variation you generate competes against the status-quo golden prompt: the prompt that
completes the loop, produces score matrices, and declares convergence — but fails on the
two patterns that separate good from excellent.

**Status-Quo Golden Failure 1 — Symbolic denominators:**
The score matrix COMPOSITE row reads: `(essential_pass/N_essential * 60) + ...`
Two operators applying this formula use different counts. One uses the v1 rubric count;
another uses the v2 count. The formula is unresolved. The correct form names the actual
integer counts from the active rubric: `(essential_pass/5 * 60) + (recommended_pass/3 * 30)
+ (aspirational_pass/4 * 10)` for a rubric with 5 essential, 3 recommended, 4 aspirational
criteria. Symbolic denominators make every composite score potentially wrong.

**Status-Quo Golden Failure 2 — Merged gate paragraph:**
The convergence check reads: "All variations pass essential criteria and this round found
no new patterns (Round 2 also found none), so the quest is plateaued and golden."
One paragraph, two gates, no labels. The trial question (do variations pass essential
criteria?) and the plateau question (have two consecutive rounds found no new patterns?)
require different evidence. A merged paragraph cannot be audited per-gate. An operator
who writes this form has answered neither question reliably.

A variation closes Failure 1 by producing a resolved formula with integer denominators in
the scoring section. A variation closes Failure 2 by producing two labeled gate sections,
each with its own evidence and its own state declaration.

---

Run the full variation-score-extract-propose loop until dual convergence.

DUAL CONVERGENCE DEFINITION
  TRIAL CONVERGED: all variations pass every essential rubric criterion this round.
  QUEST PLATEAUED: this round AND the immediately preceding round both found zero new
    excellence patterns.
Both gates must be satisfied simultaneously in the same round.

---

STEP 1 — GENERATE VARIATIONS

Write {N} complete, standalone skill body variations. Each variation must close at least
one of the two status-quo golden failure modes.

Round 1: vary exactly one axis per variation.
Round 2+: combine axes that produced signal in prior rounds.

Before writing each variation, state:
  a. Which failure mode(s) this variation closes (Failure 1 | Failure 2 | both).
  b. The structural mechanism: what in the prompt body prevents the failure.

Verify divergence: at least two variations must target different rubric criteria. A round
where all variations produce identical composite scores cannot advance plateau detection.
Identical scores produce no spread; no spread produces no new patterns; no new patterns
means the round does not count toward the two-round plateau gate.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
      inertia-framing | scoring-granularity

Label each:
  ## V-NN — [Axis Name]
  axis: [name]
  failure-modes-closed: [Failure 1 | Failure 2 | both]
  mechanism: [structural property that prevents the failure]
  hypothesis: [criterion + direction]
  [complete skill body — all instructions, all steps, all output contracts]

DO NOT proceed to Step 2 until all {N} bodies are complete.

---

STEP 2 — SCORE EACH VARIATION

Score every criterion for every variation. Per-criterion scores precede composite.

For each variation V-NN, complete all three sub-steps before starting the next:

**Sub-step 2a — Score each criterion:**

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|---------|
| C-01 | E | PASS/FAIL | [quote or structural note] |
| C-02 | E | PASS/FAIL | [quote or structural note] |
| C-03 | E | PASS/FAIL | [quote or structural note] |
| C-04 | E | PASS/FAIL | [quote or structural note] |
| C-05 | E | PASS/FAIL | [quote or structural note] |
| C-06 | R | PASS/FAIL | [quote or structural note] |
| C-07 | R | PASS/FAIL | [quote or structural note] |
| C-08 | R | PASS/FAIL | [quote or structural note] |
| C-09 | A | PASS/FAIL | [quote or structural note] |
| C-10 | A | PASS/FAIL | [quote or structural note] |
| C-11 | A | PASS/FAIL | [quote or structural note] |
| C-12 | A | PASS/FAIL | [quote or structural note] |

**Sub-step 2b — Denominator audit (closes Status-Quo Failure 1):**

Count criteria by tier from {rubric-content}:
```
E = [count of essential criteria]    — verify by listing C-IDs in this tier
R = [count of recommended criteria]  — verify by listing C-IDs in this tier
A = [count of aspirational criteria] — verify by listing C-IDs in this tier
Formula: (essential_pass/E * 60) + (recommended_pass/R * 30) + (aspirational_pass/A * 10)
```

DO NOT fill the COMPOSITE row until this block contains integer counts (not N_essential,
not N_recommended, not N_aspirational).

**Sub-step 2c — Composite and status-quo audit:**

COMPOSITE = (E_pass/[E] * 60) + (R_pass/[R] * 30) + (A_pass/[A] * 10) = [score]

Status-Quo Failure 1 closed by this variation? YES/NO
Status-Quo Failure 2 closed by this variation? YES/NO

After completing sub-steps 2a → 2b → 2c for all {N} variations, produce the summary:

| V | COMPOSITE | RANK | F1 closed | F2 closed | Essential failures |
|---|-----------|------|----------|----------|--------------------|

---

STEP 3 — IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation outperforms another:
  Pattern name: [label]
  Mechanism: [structural property present in passing, absent in failing]
  Principle: [transferable rule]
  Scope: skill-specific | transferable

If no spread: "No score spread found. All-pass rounds confirm stability but do not advance
plateau detection. Redesign for divergence."

All-fail criteria → diagnosis: rubric-gap | skill-gap.

DO NOT proceed to Step 4 until patterns name mechanisms.

---

STEP 4 — PROPOSE RUBRIC CRITERIA

For each pattern:
  ID:             C-[NN]
  Text:           [one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [auditable, one sentence]

---

CONVERGENCE CHECK — TWO INDEPENDENT GATES

This section closes Status-Quo Failure 2. Two labeled sections, each fully executed.

GATE 1 — TRIAL CONVERGENCE

Ask: do all {N} variations pass every essential criterion?

List essential criteria (C-01 through C-05). Verify each variation against each.

State exactly one of:
  TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
  TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [continue per failing pair]

---

GATE 2 — PLATEAU DETECTION

Ask: did Step 3 in this round AND in the immediately preceding round both find zero new
excellence patterns?

Name the current round by label. State what Step 3 found.
Name the immediately preceding round by label. State what Step 3 found.
Do not write "the last two rounds" or "the previous two rounds."

State exactly one of:
  QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
  QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
    not yet achieved.

---

DUAL CONVERGENCE RULE

Declare golden ONLY when TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.
2. Write the full prompt body to:
     simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden
   Body: complete, verbatim, runnable. Not a summary.
3. Write the accumulated rubric to:
     simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria from all rounds, all five fields per criterion, round of addition noted.
4. State both file paths.
