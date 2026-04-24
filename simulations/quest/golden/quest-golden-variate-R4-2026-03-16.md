---
skill: quest-variate
skill_target: quest-golden
round: 4
date: 2026-03-16
rubric: simulations/quest/rubrics/quest-golden-rubric-v4-2026-03-16.md
rubric_version: v4
---

# quest-golden -- Round 4 Variations (V-01 through V-05)

Generated against rubric v4 (18 criteria, C-01..C-18, aspirational denominator = 10).
Single-axis variations V-01 through V-04; full synthesis V-05.

**Context entering R4:**
R3 extracted four new aspirational criteria (C-15..C-18) from V-01 through V-04 excellence
signals. The R3 synthesis (V-05-R3) incorporated V-01 + V-02 + V-04 but NOT V-03 (PARTIAL
trajectory). Against v4, the R3 synthesis likely fails C-17. This round tests each new
mechanism's canonical form, then combines all four in V-05.

**R3 mechanisms carried forward in all R4 variations (base: v3 golden + all 14 v3 criteria):**
- Dual convergence gate (C-01)
- Golden prompt as verbatim artifact (C-02)
- Versioned rubric artifact (C-03)
- Step 3 precedes Step 4 (C-04)
- Rubric loaded at loop start (C-05)
- Per-round iteration record (C-06)
- Contrast naming top vs second (C-07)
- Five-field criterion proposal (C-08)
- What Made It Golden section (C-09)
- Ablated criteria section (C-10)
- Convergence state machine in tabular form (C-11)
- Structural-property labeled field (C-12)
- Extraction completeness gate at Step 3/Step 4 boundary (C-13)
- Contrast as labeled V-NN/V-MM template slot (C-14)

**Formula updated for v4:**
Score = (essential_pass/5)*60 + (recommended_pass/3)*30 + (aspirational_pass/10)*10
Golden threshold: all 5 essential PASS AND composite >= 80.

**Axes assigned:**
- V-01: lifecycle-emphasis -- dedicated SPREAD-DESIGN sub-phase with per-variation table,
  replacing the embedded "Active spread-design" prose note in Step 1 (targets C-15)
- V-02: phrasing-register -- named-round signal-value citation in plateau declaration with
  explicit prohibition on vague "both rounds" language (targets C-16)
- V-03: output-format -- PARTIAL trajectory column in iteration history, fed forward into
  next-round axis assignment (targets C-17)
- V-04: role-sequence -- pre-committed skeleton matrix printed at Step 2 entry before any
  variation is scored or generated (targets C-18)
- V-05: synthesis -- all four (V-01 + V-02 + V-03 + V-04) combined (targets C-15..C-18)

---

## Spread-Design Table

| Plan | Axis | Source signal | Target criteria | Predicted composite |
|------|------|--------------|-----------------|---------------------|
| V-01 | lifecycle-emphasis (SPREAD-DESIGN sub-phase) | C-15 requires dedicated phase with per-variation hypothesis table gated before bodies are written; v3 golden embeds this as a prose note inside Step 1 -- not a gated phase | C-15 PASS; C-17 FAIL (no PARTIAL column); C-18 FAIL (no pre-commit) | 97 |
| V-02 | phrasing-register (named-round signal citation) | C-16 requires "Round R-[N]: patterns = [value]" format; v3 golden says "name both rounds" but does not require signal values or prohibit vague references | C-16 PASS; C-15 FAIL; C-17 FAIL; C-18 FAIL | 97 |
| V-03 | output-format (PARTIAL trajectory column) | C-17 requires near-miss tracking across rounds; v3 golden has no PARTIAL column; all-fail criteria are invisible whether at zero traction or near-passing | C-17 PASS; C-15 FAIL; C-16 FAIL; C-18 FAIL | 97 |
| V-04 | role-sequence (pre-committed skeleton matrix) | C-18 requires matrix printed before scoring; v3 golden shows matrix template as post-hoc summary in Step 2 -- not a pre-commitment artifact | C-18 PASS; C-15 FAIL; C-16 FAIL; C-17 FAIL | 97 |
| V-05 | synthesis -- V-01 + V-02 + V-03 + V-04 | All four mechanisms are structurally independent; SPREAD-DESIGN runs at Step 1 entry, pre-commit at Step 2 entry, PARTIAL in iteration history and Step 3 all-fail block, named-round at GATE 2 | C-15 + C-16 + C-17 + C-18 all PASS | 100 |

---

## V-01 -- Dedicated SPREAD-DESIGN Sub-Phase

**axis:** lifecycle-emphasis
**hypothesis:** C-15 passes when the spread-design is a discrete named sub-phase at the start
of Step 1 with its own entry condition, a per-variation table (Variation | Axis | Hypothesis |
Criteria targeted), and a gate requiring the table to be complete and confirmed before any
variation body is drafted. The v3 golden embeds "Active spread-design: before writing any
variation body, assign one axis per variation..." as a prose note inside Step 1 instructions.
This does not constitute a structural phase: there is no entry condition, no table template,
and no gate preventing a variation body from being started before the planning work is done.

---

You are running quest-golden for skill: {skill-name}.

Find the golden prompt through systematic variation and scoring. Dual convergence: all essential
criteria pass (trial converged) AND no new excellence patterns emerge for two consecutive rounds
(quest plateaued). Both gates must be satisfied in the same round. The converged prompt body is
the golden prompt.

---

STEP 1 -- GENERATE {N} VARIATIONS

**SPREAD-DESIGN**

Entry condition: rubric loaded.

Complete this table before writing any variation body:

| Variation | Axis | Hypothesis (falsifiable: which criterion changes + predicted direction) | Criteria targeted |
|-----------|------|------------------------------------------------------------------------|-------------------|
| V-01      |      |                                                                        |                   |
| V-02      |      |                                                                        |                   |
| V-03      |      |                                                                        |                   |
| V-04      |      |                                                                        |                   |
| V-05      |      |                                                                        |                   |

Check: do any two rows share the same axis? If yes, reassign before continuing.

Available axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
inertia-framing | scoring-granularity

Round 1: one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

DO NOT write any variation body until the SPREAD-DESIGN table is complete and confirmed.

---

Write {N} complete, standalone variation bodies. Each is a full prompt -- not a diff,
not an excerpt, not a reference to other variations.

Label each:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [copied from SPREAD-DESIGN table]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |
| C-11      | A      |      |      |      |      |      |
| C-12      | A      |      |      |      |      |      |
| C-13      | A      |      |      |      |      |      |
| C-14      | A      |      |      |      |      |      |
| C-15      | A      |      |      |      |      |      |
| C-16      | A      |      |      |      |      |      |
| C-17      | A      |      |      |      |      |      |
| C-18      | A      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another, complete this
template in full:

```
Pattern name: [short label]
Structural property: [the design element present in better-scoring variations, absent from
                     worse-scoring ones -- must be a named structural feature, not a
                     variation ID or an outcome description]
Contrast: "V-NN had [structural property]; V-MM did not."
Mechanism: [how the structural property causes the criterion result difference]
Principle: [reusable design rule derived from the structural property]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated for each.
This gate requires completeness for ALL patterns in the current round -- not just the first
pattern encountered. Name every pattern found, state mechanism for each, before proceeding.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 -- TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 -- PLATEAU DETECTION

Iteration history (append one row per round executed):

| Round | Variation IDs scored | Top composite | Excellence signals found | Criterion added |
|-------|---------------------|---------------|--------------------------|-----------------|
| R-NN  | V-01..V-{N}         | [score]       | [signal names or "none"] | [C-NN or "none"]|

Convergence state table (fill before declaring any result):

| Round   | Step 3 patterns   | New patterns? | Loop state          |
|---------|-------------------|---------------|---------------------|
| [R N-1] | [names or "none"] | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"] | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N. Entry condition:
  two consecutive rounds with zero new excellence patterns in Step 3.
- GOLDEN (terminal): PLATEAUED and TRIAL CONVERGED in the same round.

Fill both tables before declaring any result. Name both rounds explicitly in the plateau check.

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden.
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write a "What Made It Golden" section immediately after the prompt body in the same file.
   Include at least two mechanism descriptions. Each must state:
   (a) the round in which the mechanism was first discovered, and
   (b) the output gap it closed.

4. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.
   Include an "Ablated criteria" section: criteria with zero activations across all rounds,
   with a suggested targeted probe approach. If none: "No ablated criteria."

5. State both file paths.

---

## V-02 -- Named-Round Signal-Value Citation

**axis:** phrasing-register
**hypothesis:** C-16 passes when the plateau declaration requires citing explicit round numbers
AND the pattern values for each named round, traceable to the iteration history table --
e.g., "Round R-3: patterns = ['dual-gate-precision']. Round R-4: patterns = ['none']." --
and explicitly prohibits vague alternatives like "both rounds found zero patterns" or "the last
two rounds." The v3 golden says "Name both rounds explicitly in the plateau check" but does not
require the signal-value trace or prohibit abstract references. Without the trace requirement,
a reader can name two round numbers while citing incorrect or estimated pattern lists.

---

You are running quest-golden for skill: {skill-name}.

Find the golden prompt through systematic variation and scoring. Dual convergence: all essential
criteria pass (trial converged) AND no new excellence patterns emerge for two consecutive rounds
(quest plateaued). Both gates must be satisfied in the same round. The converged prompt body is
the golden prompt.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
inertia-framing | scoring-granularity

Label each variation:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |
| C-11      | A      |      |      |      |      |      |
| C-12      | A      |      |      |      |      |      |
| C-13      | A      |      |      |      |      |      |
| C-14      | A      |      |      |      |      |      |
| C-15      | A      |      |      |      |      |      |
| C-16      | A      |      |      |      |      |      |
| C-17      | A      |      |      |      |      |      |
| C-18      | A      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another, complete this
template in full:

```
Pattern name: [short label]
Structural property: [the design element present in better-scoring variations, absent from
                     worse-scoring ones -- must be a named structural feature, not a
                     variation ID or an outcome description]
Contrast: "V-NN had [structural property]; V-MM did not."
Mechanism: [how the structural property causes the criterion result difference]
Principle: [reusable design rule derived from the structural property]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated for each.
This gate requires completeness for ALL patterns in the current round -- not just the first
pattern encountered. Name every pattern found, state mechanism for each, before proceeding.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 -- TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 -- PLATEAU DETECTION

Iteration history (append one row per round executed):

| Round | Variation IDs scored | Top composite | Excellence signals found | Criterion added |
|-------|---------------------|---------------|--------------------------|-----------------|
| R-NN  | V-01..V-{N}         | [score]       | [signal names or "none"] | [C-NN or "none"]|

Convergence state table (fill before declaring any result):

| Round   | Step 3 patterns   | New patterns? | Loop state          |
|---------|-------------------|---------------|---------------------|
| [R N-1] | [names or "none"] | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"] | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N. Entry condition:
  two consecutive rounds with zero new excellence patterns in Step 3.
- GOLDEN (terminal): PLATEAUED and TRIAL CONVERGED in the same round.

Fill both tables before declaring any result.

Cite both rounds by explicit number AND state the pattern values for each, traceable to the
iteration history table:
"Round R-[N]: patterns = [names or 'none']. Round R-[N-1]: patterns = [names or 'none']."
Do not write "both rounds found zero patterns" or "the last two rounds" without naming
the specific round identifiers.

State ONE of:
- QUEST PLATEAUED: Round R-[N]: patterns = [none]. Round R-[N-1]: patterns = [none].
  Both consecutive rounds confirmed zero new patterns.
- QUEST NOT PLATEAUED: Round R-[N] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden.
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write a "What Made It Golden" section immediately after the prompt body in the same file.
   Include at least two mechanism descriptions. Each must state:
   (a) the round in which the mechanism was first discovered, and
   (b) the output gap it closed.

4. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.
   Include an "Ablated criteria" section: criteria with zero activations across all rounds,
   with a suggested targeted probe approach. If none: "No ablated criteria."

5. State both file paths.

---

## V-03 -- PARTIAL Trajectory Column

**axis:** output-format
**hypothesis:** C-17 passes when the iteration history table gains a PARTIAL column recording,
per round, any criterion where all variations fail outright but at least one partially satisfies
the pass condition. The PARTIAL entry feeds the next round's spread-design: an entry of
"C-17: V-03 near-pass because trajectory column present but not fed forward" signals a targeted
axis for the next round. The v3 golden has no PARTIAL column; all-fail criteria are invisible
whether they are at zero traction or one structural step from passing. Without trajectory
tracking, the loop cannot distinguish productive near-misses from complete non-starters.

---

You are running quest-golden for skill: {skill-name}.

Find the golden prompt through systematic variation and scoring. Dual convergence: all essential
criteria pass (trial converged) AND no new excellence patterns emerge for two consecutive rounds
(quest plateaued). Both gates must be satisfied in the same round. The converged prompt body is
the golden prompt.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds. Before assigning axes, consult
the PARTIAL column in the iteration history: any PARTIAL entry signals a near-miss criterion
that a targeted axis may resolve.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
inertia-framing | scoring-granularity

Label each variation:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

After all variations are scored individually, produce the summary matrix:

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |
| C-11      | A      |      |      |      |      |      |
| C-12      | A      |      |      |      |      |      |
| C-13      | A      |      |      |      |      |      |
| C-14      | A      |      |      |      |      |      |
| C-15      | A      |      |      |      |      |      |
| C-16      | A      |      |      |      |      |      |
| C-17      | A      |      |      |      |      |      |
| C-18      | A      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |

Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)

DO NOT proceed to Step 3 until per-criterion evidence is recorded for every variation.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another, complete this
template in full:

```
Pattern name: [short label]
Structural property: [the design element present in better-scoring variations, absent from
                     worse-scoring ones -- must be a named structural feature, not a
                     variation ID or an outcome description]
Contrast: "V-NN had [structural property]; V-MM did not."
Mechanism: [how the structural property causes the criterion result difference]
Principle: [reusable design rule derived from the structural property]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

For each criterion all variations fail, assess whether any variation partially satisfied it:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
PARTIAL: [V-NN near-pass because X] | none
```

DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated for each.
This gate requires completeness for ALL patterns in the current round -- not just the first
pattern encountered. Name every pattern found, state mechanism for each, before proceeding.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 -- TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 -- PLATEAU DETECTION

Iteration history (append one row per round executed):

| Round | Variation IDs | Top composite | Patterns found    | PARTIAL near-misses                              | Criterion added  |
|-------|--------------|---------------|-------------------|--------------------------------------------------|------------------|
| R-NN  | V-01..V-{N}  | [score]       | [names or "none"] | [C-NN: V-MM near-pass because X, or "none"]      | [C-NN or "none"] |

PARTIAL column: for each criterion where all variations fail but at least one partially
satisfies the pass condition, record "C-NN: V-MM near-pass because [reason]." Write "none"
if no such criterion exists. Consult this column when designing axes for the next round.

Convergence state table (fill before declaring any result):

| Round   | Step 3 patterns   | New patterns? | Loop state          |
|---------|-------------------|---------------|---------------------|
| [R N-1] | [names or "none"] | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"] | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N. Entry condition:
  two consecutive rounds with zero new excellence patterns in Step 3.
- GOLDEN (terminal): PLATEAUED and TRIAL CONVERGED in the same round.

Fill both tables before declaring any result. Name both rounds explicitly in the plateau check.

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden.
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write a "What Made It Golden" section immediately after the prompt body in the same file.
   Include at least two mechanism descriptions. Each must state:
   (a) the round in which the mechanism was first discovered, and
   (b) the output gap it closed.

4. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.
   Include an "Ablated criteria" section: criteria with zero activations across all rounds,
   with a suggested targeted probe approach. If none: "No ablated criteria."

5. State both file paths.

---

## V-04 -- Pre-Committed Skeleton Matrix

**axis:** role-sequence
**hypothesis:** C-18 passes when Step 2 opens by printing the empty skeleton matrix (all
C-01..C-18 rows, all variation columns, blank score cells) BEFORE any variation is scored.
This separates structure-commitment from execution: the scorer commits to the evaluation
structure, then populates it. The v3 golden places the matrix template in Step 2 instructions
as the "after all variations are scored" summary artifact -- post-hoc structure, not
pre-commitment. Without pre-commitment, the scorer can observe which variation has the best
narrative flow, then selectively weight criteria to justify the observed ordering; any score
on a criterion not listed before execution is suspect.

---

You are running quest-golden for skill: {skill-name}.

Find the golden prompt through systematic variation and scoring. Dual convergence: all essential
criteria pass (trial converged) AND no new excellence patterns emerge for two consecutive rounds
(quest plateaued). Both gates must be satisfied in the same round. The converged prompt body is
the golden prompt.

---

STEP 1 -- GENERATE {N} VARIATIONS

Write {N} complete, standalone skill body variations. These are full prompts -- not diffs,
not excerpts, not references to other variations.

Round 1: change exactly one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds.

Active spread-design: before writing any variation body, assign one axis per variation and
confirm at least two variations target different rubric criteria.

Axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
inertia-framing | scoring-granularity

Label each variation:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [which criterion changes + predicted direction, falsifiable]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 -- SCORE EACH VARIATION

**2a -- Pre-commit evaluation structure (execute before scoring)**

Print this skeleton matrix before scoring any variation. This commits to the evaluation
structure. Any criterion absent from this skeleton cannot receive a valid score in this round.

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |
| C-11      | A      |      |      |      |      |      |
| C-12      | A      |      |      |      |      |      |
| C-13      | A      |      |      |      |      |      |
| C-14      | A      |      |      |      |      |      |
| C-15      | A      |      |      |      |      |      |
| C-16      | A      |      |      |      |      |      |
| C-17      | A      |      |      |      |      |      |
| C-18      | A      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |

DO NOT score any variation until this skeleton is printed.

**2b -- Per-criterion evidence**

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

**2c -- Fill the matrix**

Transfer PASS/FAIL scores from 2b into the skeleton printed in 2a.
Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)

DO NOT proceed to Step 3 until the matrix is filled and composites computed.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another, complete this
template in full:

```
Pattern name: [short label]
Structural property: [the design element present in better-scoring variations, absent from
                     worse-scoring ones -- must be a named structural feature, not a
                     variation ID or an outcome description]
Contrast: "V-NN had [structural property]; V-MM did not."
Mechanism: [how the structural property causes the criterion result difference]
Principle: [reusable design rule derived from the structural property]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

List any criterion all variations fail:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
```

DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated for each.
This gate requires completeness for ALL patterns in the current round -- not just the first
pattern encountered. Name every pattern found, state mechanism for each, before proceeding.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 -- TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 -- PLATEAU DETECTION

Iteration history (append one row per round executed):

| Round | Variation IDs scored | Top composite | Excellence signals found | Criterion added |
|-------|---------------------|---------------|--------------------------|-----------------|
| R-NN  | V-01..V-{N}         | [score]       | [signal names or "none"] | [C-NN or "none"]|

Convergence state table (fill before declaring any result):

| Round   | Step 3 patterns   | New patterns? | Loop state          |
|---------|-------------------|---------------|---------------------|
| [R N-1] | [names or "none"] | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"] | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N. Entry condition:
  two consecutive rounds with zero new excellence patterns in Step 3.
- GOLDEN (terminal): PLATEAUED and TRIAL CONVERGED in the same round.

Fill both tables before declaring any result. Name both rounds explicitly in the plateau check.

State ONE of:
- QUEST PLATEAUED: [Round X] and [Round Y] both found zero new excellence patterns.
- QUEST NOT PLATEAUED: [Round X] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden.
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write a "What Made It Golden" section immediately after the prompt body in the same file.
   Include at least two mechanism descriptions. Each must state:
   (a) the round in which the mechanism was first discovered, and
   (b) the output gap it closed.

4. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.
   Include an "Ablated criteria" section: criteria with zero activations across all rounds,
   with a suggested targeted probe approach. If none: "No ablated criteria."

5. State both file paths.

---

## V-05 -- Full Synthesis (V-01 + V-02 + V-03 + V-04)

**axis:** synthesis
**hypothesis:** All four new v4 mechanisms pass simultaneously with no essential regression,
achieving 100/100: dedicated SPREAD-DESIGN sub-phase (C-15), named-round signal-value plateau
citation (C-16), PARTIAL trajectory column in iteration history (C-17), pre-committed skeleton
matrix at Step 2 entry (C-18). The mechanisms are structurally independent: SPREAD-DESIGN runs
at Step 1 entry before bodies are drafted, the pre-committed matrix runs at Step 2 entry before
scoring, PARTIAL appears in both the iteration history and Step 3 all-fail diagnosis, and
named-round citation runs at GATE 2. No mechanism blocks or modifies another.

---

You are running quest-golden for skill: {skill-name}.

Find the golden prompt through systematic variation and scoring. Dual convergence: all essential
criteria pass (trial converged) AND no new excellence patterns emerge for two consecutive rounds
(quest plateaued). Both gates must be satisfied in the same round. The converged prompt body is
the golden prompt.

---

STEP 1 -- GENERATE {N} VARIATIONS

**SPREAD-DESIGN**

Entry condition: rubric loaded.

Complete this table before writing any variation body:

| Variation | Axis | Hypothesis (falsifiable: which criterion changes + predicted direction) | Criteria targeted |
|-----------|------|------------------------------------------------------------------------|-------------------|
| V-01      |      |                                                                        |                   |
| V-02      |      |                                                                        |                   |
| V-03      |      |                                                                        |                   |
| V-04      |      |                                                                        |                   |
| V-05      |      |                                                                        |                   |

Check: do any two rows share the same axis? If yes, reassign before continuing.

Available axes: role-sequence | output-format | lifecycle-emphasis | phrasing-register |
inertia-framing | scoring-granularity

Round 1: one axis per variation.
Round 2+: combine axes that produced signal in earlier rounds. Consult the PARTIAL column in
the iteration history before assigning axes.

DO NOT write any variation body until the SPREAD-DESIGN table is complete and confirmed.

---

Write {N} complete, standalone variation bodies. Each is a full prompt -- not a diff,
not an excerpt, not a reference to other variations.

Label each:
```
## V-NN -- [Axis Name]
axis: [name]
hypothesis: [copied from SPREAD-DESIGN table]
[full prompt body -- every step, every instruction, every output contract]
```

DO NOT proceed to Step 2 until all {N} variation bodies are written in full. No placeholders.

---

STEP 2 -- SCORE EACH VARIATION

**2a -- Pre-commit evaluation structure (execute before scoring)**

Print this skeleton matrix before scoring any variation. This commits to the evaluation
structure. Any criterion absent from this skeleton cannot receive a valid score in this round.

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |
| C-11      | A      |      |      |      |      |      |
| C-12      | A      |      |      |      |      |      |
| C-13      | A      |      |      |      |      |      |
| C-14      | A      |      |      |      |      |      |
| C-15      | A      |      |      |      |      |      |
| C-16      | A      |      |      |      |      |      |
| C-17      | A      |      |      |      |      |      |
| C-18      | A      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |

DO NOT score any variation until this skeleton is printed.

**2b -- Per-criterion evidence**

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next.

**2c -- Fill the matrix**

Transfer PASS/FAIL scores from 2b into the skeleton printed in 2a.
Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)

DO NOT proceed to Step 3 until the matrix is filled and composites computed.

---

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where at least one variation scores higher than another, complete this
template in full:

```
Pattern name: [short label]
Structural property: [the design element present in better-scoring variations, absent from
                     worse-scoring ones -- must be a named structural feature, not a
                     variation ID or an outcome description]
Contrast: "V-NN had [structural property]; V-MM did not."
Mechanism: [how the structural property causes the criterion result difference]
Principle: [reusable design rule derived from the structural property]
Scope: skill-specific | transferable
```

If no variation outperforms any other on any criterion, write exactly:
"No score spread found. All-pass rounds confirm stability but do not advance plateau detection.
Redesign variations for divergence in the next round."

For each criterion all variations fail, assess whether any variation partially satisfied it:
```
Criterion: C-NN
Diagnosis: rubric-gap (criterion poorly defined) | skill-gap (all variations share the flaw)
PARTIAL: [V-NN near-pass because X] | none
```

DO NOT proceed to Step 4 until ALL patterns are named AND mechanism stated for each.
This gate requires completeness for ALL patterns in the current round -- not just the first
pattern encountered. Name every pattern found, state mechanism for each, before proceeding.

---

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each pattern from Step 3, propose a criterion with all five required fields:
```
ID:             C-[NN] (next sequential after current rubric's highest)
Text:           [what the criterion measures, one sentence]
Weight:         essential | recommended | aspirational
Category:       structure | behavior | correctness | depth | coverage
Pass condition: [one auditable sentence, no interpretation required]
```

DO NOT proceed to the convergence check until every proposed criterion has all five fields.

---

CONVERGENCE CHECK

GATE 1 -- TRIAL CONVERGENCE

List every essential criterion (weight = E).
For each variation, state whether it PASSes every essential criterion.

State ONE of:
- TRIAL CONVERGED: all {N} variations pass all essential criteria this round.
- TRIAL NOT CONVERGED: [V-NN] fails [C-NN]. [V-NN] fails [C-NN]. ...

GATE 2 -- PLATEAU DETECTION

Iteration history (append one row per round executed):

| Round | Variation IDs | Top composite | Patterns found    | PARTIAL near-misses                         | Criterion added  |
|-------|--------------|---------------|-------------------|---------------------------------------------|------------------|
| R-NN  | V-01..V-{N}  | [score]       | [names or "none"] | [C-NN: V-MM near-pass because X, or "none"] | [C-NN or "none"] |

PARTIAL column: for each criterion where all variations fail but at least one partially
satisfies the pass condition, record "C-NN: V-MM near-pass because [reason]." Write "none"
if no such criterion exists. Consult this column when assigning axes for the next round.

Convergence state table (fill before declaring any result):

| Round   | Step 3 patterns   | New patterns? | Loop state          |
|---------|-------------------|---------------|---------------------|
| [R N-1] | [names or "none"] | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"] | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N. Entry condition:
  two consecutive rounds with zero new excellence patterns in Step 3.
- GOLDEN (terminal): PLATEAUED and TRIAL CONVERGED in the same round.

Fill both tables before declaring any result.

Cite both rounds by explicit number AND state the pattern values for each, traceable to the
iteration history table:
"Round R-[N]: patterns = [names or 'none']. Round R-[N-1]: patterns = [names or 'none']."
Do not write "both rounds found zero patterns" or "the last two rounds" without naming
the specific round identifiers.

State ONE of:
- QUEST PLATEAUED: Round R-[N]: patterns = [none]. Round R-[N-1]: patterns = [none].
  Both consecutive rounds confirmed zero new patterns.
- QUEST NOT PLATEAUED: Round R-[N] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.

Declare golden ONLY if TRIAL CONVERGED AND QUEST PLATEAUED in the same round.

---

WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite variation. Ties: prefer minimal structure.

2. Write the full prompt body to:
   simulations/quest/golden/{skill-name}-golden-{date}.md
   Frontmatter: skill, date, rounds_to_convergence, rubric_version, composite_score, status: golden.
   Body: the complete, verbatim, runnable prompt. Not a summary. Not a description.

3. Write a "What Made It Golden" section immediately after the prompt body in the same file.
   Include at least two mechanism descriptions. Each must state:
   (a) the round in which the mechanism was first discovered, and
   (b) the output gap it closed.

4. Write the accumulated rubric (all criteria from all rounds) to:
   simulations/quest/rubrics/{skill-name}-rubric-v{N}-{date}.md
   All criteria with all five fields. Note which round added each criterion.
   Include an "Ablated criteria" section: criteria with zero activations across all rounds,
   with a suggested targeted probe approach. If none: "No ablated criteria."

5. State both file paths.
