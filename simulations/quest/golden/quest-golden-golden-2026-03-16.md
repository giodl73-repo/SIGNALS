Golden prompt document written to `simulations/quest/golden/quest-golden-golden-2026-03-16.md`.

**What's in it:**

- **Frontmatter:** skill, date, rounds=5, rubric_final=v4, score=100, status=GOLDEN
- **Prompt body:** R4 V-05 (full synthesis) + two R5 integrations:
  - **V-00 column** added to the Step 2 pre-committed skeleton matrix with an explanatory note about its contrast-enforcement role
  - **Expanded convergence gate** replaced the flat CONVERGENCE CHECK with 6 named sub-steps: history completeness → GATE 1 essentials list → GATE 1 result (with anti-patterns) → iteration history append → convergence state table → GATE 2 result (with anti-patterns + UNRESOLVABLE state)
- **What Made It Golden:** 5 mechanisms, each with round discovered and gap closed
- **Rubric summary table:** all 18 criteria with tier, category, description, and round added
mpt body is the golden prompt.

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

| Criterion | Weight | V-00 | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|------|
| C-01      | E      |      |      |      |      |      |      |
| C-02      | E      |      |      |      |      |      |      |
| C-03      | E      |      |      |      |      |      |      |
| C-04      | E      |      |      |      |      |      |      |
| C-05      | E      |      |      |      |      |      |      |
| C-06      | R      |      |      |      |      |      |      |
| C-07      | R      |      |      |      |      |      |      |
| C-08      | R      |      |      |      |      |      |      |
| C-09      | A      |      |      |      |      |      |      |
| C-10      | A      |      |      |      |      |      |      |
| C-11      | A      |      |      |      |      |      |      |
| C-12      | A      |      |      |      |      |      |      |
| C-13      | A      |      |      |      |      |      |      |
| C-14      | A      |      |      |      |      |      |      |
| C-15      | A      |      |      |      |      |      |      |
| C-16      | A      |      |      |      |      |      |      |
| C-17      | A      |      |      |      |      |      |      |
| C-18      | A      |      |      |      |      |      |      |
| COMPOSITE |        |      |      |      |      |      |      |
| RANK      |        |      |      |      |      |      |      |

V-00 is the inertia baseline: the prior champion (or the round-entry prompt) scored without
modification. It is always present in the matrix. Naming V-00 explicitly makes contrast
enforcement and discovery identification legible -- any variation that fails to outperform
V-00 on its targeted criteria should be redesigned.

DO NOT score any variation until this skeleton is printed.

**2b -- Per-criterion evidence**

Score every variation against every rubric criterion using PASS / FAIL.

For each variation, for each criterion:
```
Criterion: C-NN
Result: PASS | FAIL
Evidence: "[text from the variation body that confirms or denies, or 'absent' if FAIL]"
```

Complete all criteria for one variation before moving to the next. Include V-00.

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

This phase runs after Step 4 in every round. It is the only place the loop exits.
Execute all sub-steps in order. Do not skip ahead.

**Sub-step 1 -- History completeness**

Verify the iteration history table contains one row per executed round, including the
current round. If any round is missing: UNRESOLVABLE -- rebuild history before evaluating
either gate.

**Sub-step 2 -- GATE 1 essentials list**

List every essential criterion (weight = E) from the active rubric.
For each variation (including V-00), state whether it passes every essential criterion.

**Sub-step 3 -- GATE 1 result**

State ONE of:
- GATE 1 = PASS: all {N} variations pass all essential criteria this round.
- GATE 1 = FAIL: [V-NN] fails [C-NN]. ...

Anti-patterns (each = automatic GATE 1 = FAIL):
- "at least one variation passes all essentials"
- "the top variation passes" (without confirming all variations)
- citing composite score as trial evidence

If GATE 1 = FAIL: do not proceed to Sub-step 4. State the failures, then continue to the
next round.

**Sub-step 4 -- Iteration history (append, do not replace)**

| Round | Variation IDs | Top composite | Patterns found    | PARTIAL near-misses                         | Criterion added  |
|-------|--------------|---------------|-------------------|---------------------------------------------|------------------|
| R-NN  | V-01..V-{N}  | [score]       | [names or "none"] | [C-NN: V-MM near-pass because X, or "none"] | [C-NN or "none"] |

PARTIAL column: for each criterion where all variations fail but at least one partially
satisfies the pass condition, record "C-NN: V-MM near-pass because [reason]." Write "none"
if no such criterion exists. Consult this column when assigning axes for the next round.

**Sub-step 5 -- Convergence state table**

| Round   | Step 3 patterns   | New patterns? | Loop state          |
|---------|-------------------|---------------|---------------------|
| [R N-1] | [names or "none"] | Y / N         | RUNNING / PLATEAUED |
| [R N]   | [names or "none"] | Y / N         | RUNNING / PLATEAUED |

State definitions:
- RUNNING: fewer than two consecutive zero-pattern rounds recorded.
- PLATEAUED: current round AND immediately preceding round both show N.

**Sub-step 6 -- GATE 2 result**

Cite both rounds by explicit number AND state the pattern values for each, traceable to the
iteration history table:
"Round R-[N]: patterns = [names or 'none']. Round R-[N-1]: patterns = [names or 'none']."

State ONE of:
- GATE 2 = PASS: two named consecutive rounds confirmed zero new patterns.
- GATE 2 = FAIL: Round R-[N] found [pattern names]. Two consecutive zero-pattern rounds
  not yet achieved.
- GATE 2 = UNRESOLVABLE: fewer than 2 rounds in history -- cannot evaluate.

Anti-patterns (each = automatic GATE 2 = FAIL):
- "the last two rounds" without naming round identifiers
- "both rounds found zero patterns" without traceable round numbers
- "patterns have stabilized"

If GATE 2 = UNRESOLVABLE or GATE 2 = FAIL: do not proceed to WRITE GOLDEN ARTIFACTS.
Continue to the next round.

**Declaration**

Declare golden ONLY if GATE 1 = PASS AND GATE 2 = PASS in the same round.

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

## WHAT MADE IT GOLDEN

Four structural mechanisms distinguish the final champion from any single-round variation.
Each mechanism closes a specific output gap; each was discovered in a named round.

---

**Mechanism 1: SPREAD-DESIGN phase with hypothesis table (discovered Round 3, V-01)**

Gap closed: Without a pre-variation design phase, variations are generated ad-hoc. Coverage
is accidental; redundant hypotheses go undetected; the loop cannot distinguish "we tested
this axis" from "we never tried this angle." Two variations could test the same formatting
change under different labels and leave entire structural regions unexplored.

The SPREAD-DESIGN phase forces the executor to commit to a hypothesis table before writing
any body. The table requires one named axis per row, a falsifiable hypothesis, and targeted
criteria. A cross-check (do any two rows share the same axis?) prevents redundancy. V-05
must synthesize the strongest single-axis hypotheses from V-01..V-04, making the final
variation a principled accumulator rather than a guess.

---

**Mechanism 2: Named-round convergence citation (discovered Round 3, V-02)**

Gap closed: Without named-round citation, the loop can declare QUEST PLATEAUED after a
single zero-pattern round by vague phrasing ("the last two rounds showed no patterns"). This
is a false plateau -- the two-round requirement exists precisely because one zero-pattern
round can be a statistical accident; two consecutive named rounds is the structural test.

The named-round gate requires: cite Round R-[N] and Round R-[N-1] by explicit identifier,
state the pattern value for each, trace both to the iteration history table. Anti-patterns
are enumerated: "the last two rounds," "both rounds found zero patterns" without round
numbers, "patterns have stabilized." Any anti-pattern triggers GATE 2 = FAIL automatically.

---

**Mechanism 3: Pre-committed scoring matrix (discovered Round 3, V-04)**

Gap closed: Without pre-commitment, scoring is post-hoc -- the extractor sees which
variation produced the best output and constructs justifying evidence backward. This
introduces hindsight bias and makes the scoring sequence unauditable. A criterion not listed
before execution cannot receive a valid score.

The pre-committed skeleton matrix is printed in its entirety -- all criteria, all columns,
all cells empty -- before any variation is scored. Filling the matrix is a separate step
(2c) that occurs only after per-criterion evidence (2b) is complete for every variation.
The structure of the matrix cannot be revised after execution begins.

---

**Mechanism 4: V-00 inertia baseline as permanent scoring column (discovered Round 5, V-03)**

Gap closed: Without a named baseline in the scoring matrix, contrast enforcement is
implicit. A variation that fails to outperform the prior champion on its targeted criteria
is not visibly identified as regressive -- it simply receives a lower composite score. The
inertia baseline makes this legible: V-00's column is always present, always scored, and
any variation whose targeted criteria score equal to or below V-00 is a redesign candidate.

V-00 also sharpens discovery identification. In Step 4 INERTIA LACKED analysis, the
structural property absent from V-00 is precisely the thing being discovered. Naming V-00
in the matrix enforces the connection between the scoring table and the excellence
extraction step.

---

**Mechanism 5: Expanded convergence gate with sub-steps and anti-patterns (discovered Round 5, V-01)**

Gap closed: Without sub-step decomposition, the convergence check is the most structurally
compressed phase in the loop relative to its consequence. A single paragraph can satisfy
a loosely worded gate by asserting convergence without showing the evaluation sequence. The
executor can write "both gates pass" without naming failing criteria, without citing round
numbers, without distinguishing GATE 1 from GATE 2.

The expanded gate enforces sequential sub-step execution: history completeness first, then
GATE 1 essentials list, then GATE 1 result with explicit anti-patterns, then iteration
history append, then convergence state table, then GATE 2 result with explicit anti-patterns,
then the declaration. Each sub-step has a named failure mode. GATE 1 = FAIL short-circuits
evaluation (skip to next round); GATE 2 = UNRESOLVABLE is an explicit third state that
prevents false plateau claims when fewer than two rounds exist.

---

## FINAL RUBRIC CRITERIA SUMMARY

18 criteria across 3 tiers. Full rubric: simulations/quest/rubrics/quest-golden-rubric-v4-2026-03-16.md

| ID   | Tier          | Category    | Description                                               | Round added |
|------|---------------|-------------|-----------------------------------------------------------|-------------|
| C-01 | Essential     | structure   | Dual convergence termination gate                         | R1          |
| C-02 | Essential     | behavior    | Golden prompt written as full verbatim skill body         | R1          |
| C-03 | Essential     | behavior    | Final rubric written as standalone versioned artifact     | R1          |
| C-04 | Essential     | correctness | QU2 (excellence extraction) precedes QU3 (proposal)      | R1          |
| C-05 | Essential     | structure   | Rubric present and loaded at loop start                   | R1          |
| C-06 | Recommended   | depth       | Per-round iteration record with all required fields       | R1          |
| C-07 | Recommended   | depth       | Excellence signal isolation: TOP HAD / SECOND LACKED      | R1          |
| C-08 | Recommended   | correctness | Five-field criterion proposal (ID/text/weight/cat/pass)   | R1          |
| C-09 | Aspirational  | depth       | "What Made It Golden" with mechanism + round + gap        | R2          |
| C-10 | Aspirational  | coverage    | Ablated criteria section with targeted probe approach     | R2          |
| C-11 | Aspirational  | correctness | Convergence state machine in tabular form                 | R2          |
| C-12 | Aspirational  | structure   | Structural-property labeled field in delta block          | R2          |
| C-13 | Aspirational  | structure   | Extraction completeness gate at Step 3 / Step 4 boundary | R2          |
| C-14 | Aspirational  | depth       | Contrast as labeled V-NN/V-MM template slot with INERTIA  | R2          |
| C-15 | Aspirational  | structure   | Named SPREAD-DESIGN phase with per-variation hypothesis   | R3          |
| C-16 | Aspirational  | correctness | Named-round convergence citation with anti-vague gate     | R3          |
| C-17 | Aspirational  | depth       | PARTIAL trajectory column in iteration history            | R3          |
| C-18 | Aspirational  | correctness | Pre-committed scoring matrix printed before scoring       | R3          |

**Formula:**
Score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/10 * 10)
Golden threshold: all 5 essentials PASS AND composite >= 80.
