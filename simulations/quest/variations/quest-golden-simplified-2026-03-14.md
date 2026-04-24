798 words original → 634 words simplified = **164 words removed = 20.6% reduction.** Right in target range. Now let me verify all 13 criteria coverage and produce the final output.

---

## Simplified Prompt Body

```
You are running quest-golden for {skill}.

DO NOT proceed past any section until the section is complete.

LOAD INPUTS

1. Load the skill spec from signal.skills.yaml or the spec file.
2. Load the current rubric from simulations/quest/rubrics/{skill}-rubric-*.md.
   If no rubric file exists: write a v1 rubric with at least one essential criterion.
   Write it to disk before continuing.

FOR EACH ROUND, EXECUTE STEPS 1-4 IN ORDER.

STEP 1 -- GENERATE VARIATIONS

Generate 5 complete, runnable prompt bodies (V-01 through V-05) -- not diffs, not summaries.
Per variation, state:
  - Axis: [the single design dimension this variation tests]

Round 1: each variation must vary only one axis.
Round 2+: combine axes that produced signal in earlier rounds.

Spread-design rule: if all variations produce identical composite scores, the round
generates no new excellence patterns and does not advance plateau detection. Design
variations to diverge on at least one criterion.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

STEP 2 -- SCORE EACH VARIATION

For each variation, score every criterion (criterion-by-criterion -- not just composite).
Per criterion:
  Result: PASS | PARTIAL | FAIL
  Evidence: [text present or absent]

Produce a summary score matrix (compute composite using rubric formula):

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| C-01      | E  |      |      |      |      |      |
...
| COMPOSITE |    |      |      |      |      |      |
| RANK      |    |      |      |      |      |      |

DO NOT proceed to Step 3 until you have criterion-by-criterion scores for all 5 variations.

STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For every criterion where at least one variation scores higher than another:
  1. Name the structural property that caused the difference.
     Write it as a reusable principle -- not which variation won but what design
     choice caused the difference.
  2. Tag its scope: skill-specific | transferable
  3. State the mechanism: the specific prompt property present in passing variations
     and absent from failing ones.

List any criterion all variations fail:
  Diagnosis: rubric-gap | skill-gap

If no variation outperforms any other on any criterion, state:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

DO NOT proceed to Step 4 until all patterns are named and scoped.

STEP 4 -- PROPOSE RUBRIC CRITERIA

For each excellence pattern from Step 3, propose a rubric criterion with all five fields:
  ID:             C-[NN]
  Text:           [criterion description, one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

State each proposal explicitly. Wait for approval before adding to the rubric.
On approval: update the rubric file on disk, increment the version number, state path.

CONVERGENCE -- CHECK BOTH GATES INDEPENDENTLY

GATE 1 (TRIAL): Do all variations in this round pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED

GATE 2 (PLATEAU): Did Step 3 in this round AND the immediately preceding round both
  find zero new excellence patterns?
  Name both rounds explicitly (e.g., "Round 3 and Round 4: no new patterns found").
  State: QUEST PLATEAUED (Round X and Round Y: no new patterns) or QUEST NOT PLATEAUED

DO NOT declare golden unless both gates are satisfied simultaneously.
If only Gate 1 is satisfied: run another round.
If only Gate 2 is satisfied: run another round.

WRITE GOLDEN ARTIFACTS (on dual convergence only)

1. Select the highest-composite-scoring variation from this round.
2. Write it verbatim -- the full prompt body -- to:
     simulations/quest/golden/{skill}-golden-{date}.md
3. Write the final accumulated rubric (all criteria across all rounds) to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md

DO NOT write only a summary of the prompt. Write the complete prompt body.
DO NOT declare this task complete until both files are written to disk and paths stated.
```

---

## Simplification Report

### Removals (zero criterion work)

| # | Removed text | Words | Why |
|---|---|---|---|
| 1 | `"State the path and version."` (LOAD INPUTS) | 5 | No criterion requires path/version logging during input loading |
| 2 | `"(description field) or"` in LOAD INPUTS step 1 | 3 | Excess specificity; file path already identifies the source |
| 3 | `"Each variation must be a full prompt -- not a diff, not a summary."` (separate line) | 13 | Merged into Generate line as `"-- not diffs, not summaries"` with net 10-word save |
| 4 | `"Each must include: / - Label: V-NN"` | 6 | Label is redundant — V-01 through V-05 already specified in Generate line |
| 5 | `"- Hypothesis: [what this axis is predicted to change relative to a generic approach]"` | 14 | No criterion (essential or otherwise) requires a Hypothesis field on variations; Axis alone covers C-12 |
| 6 | `"After all criteria, compute and state the composite score using the rubric formula."` | 14 | Folded into matrix line as `"(compute composite using rubric formula)"`; COMPOSITE row in matrix already implies it |
| 7 | `"Look at the score spread across all variations."` (Step 3 opener) | 8 | Completely redundant with the `"For every criterion where..."` instruction immediately following |
| 8 | `"In Round 2+: list any variation that passed a criterion last round but fails now."` | 15 | Regression tracking is not captured by any of the 13 criteria |
| 9 | `"If NOT CONVERGED: list which variations failed which essential criteria."` (GATE 1) | 11 | C-03 only requires checking both gate states; the State line covers it |
| 10 | `"Body: the complete, runnable prompt text."` | 6 | Fully covered by `"DO NOT write only a summary"` two lines later |
| 11 | `"Frontmatter: skill, target_skill, date, rounds, rubric, score, status: GOLDEN"` | 11 | No criterion specifies frontmatter fields; C-04 requires the prompt body at the right path, not specific metadata |
| 12 | `"Diagnosis: rubric-gap (criterion unclear or unachievable) \| skill-gap (skill design does not produce this behavior)"` parentheticals | 9 | Explanations add no criterion coverage; labels alone are sufficient |

### Condensations (same criterion coverage, tighter phrasing)

| # | Original | Simplified | Words saved |
|---|---|---|---|
| 13 | 3-line Step 2 intro | 1-line `"For each variation, score every criterion (criterion-by-criterion -- not just composite)."` | 14 |
| 14 | `"Evidence: [quote the specific variation text that justifies the result, or note the absent property]"` | `"Evidence: [text present or absent]"` | 11 |
| 15 | Step 3 item 1 expansion: `"not 'V-03 passed' but the design choice V-03 made that others did not, as a property a future skill designer could apply"` | `"not which variation won but what design choice caused the difference"` | 12 |
| 16 | `"Pass condition: [one sentence, auditable -- a reviewer can determine PASS or FAIL without ambiguity]"` | `"Pass condition: [one auditable sentence]"` | 9 |
| 17 | `"Step 3 in this round AND Step 3 in the immediately preceding round"` | `"Step 3 in this round AND the immediately preceding round"` | 3 |
| 18 | `"For each excellence pattern from Step 3, propose a new rubric criterion. Every criterion proposal must include all five fields:"` | `"For each excellence pattern from Step 3, propose a rubric criterion with all five fields:"` | 7 |

### Criterion coverage verification

| ID | Criterion | Covered by | Result |
|----|-----------|------------|--------|
| C-01 | Full 4-phase loop | STEP 1–4 headers + FOR EACH ROUND + DO NOT gates | PASS |
| C-02 | Per-criterion pass/fail per variation | "criterion-by-criterion -- not just composite" + Result format + matrix | PASS |
| C-03 | Both convergence conditions | GATE 1 + GATE 2 + "DO NOT declare golden unless both" + If-only rules | PASS |
| C-04 | Golden prompt artifact written | WRITE GOLDEN step 2 path + DO NOT write summary + DO NOT declare complete | PASS |
| C-05 | Final rubric artifact written | WRITE GOLDEN step 3 path + DO NOT declare complete | PASS |
| C-06 | Excellence pattern named/abstracted | Step 3 item 1: "reusable principle -- not which variation won but what design choice" | PASS |
| C-07 | Criterion with full fields | Step 4 five-field format | PASS |
| C-08 | Plateau cites both rounds | GATE 2: "Name both rounds explicitly" | PASS |
| C-09 | Score separation | Spread-design rule: "Design variations to diverge on at least one criterion" | PASS |
| C-10 | Pattern generalizability | Step 3 item 2: "Tag its scope: skill-specific \| transferable" | PASS |
| C-11 | Explains why uniform rounds stall | Spread-design rule causal statement + "No score spread" quoted text | PASS |
| C-12 | Active spread-design instruction in generation | Spread-design rule is in STEP 1 (generation phase) | PASS |
| C-13 | Causal ≠ competitive framing alone | Spread-design rule is causal, not competitive/inertia framing | PASS |

All 13 criteria pass. All 5 essential criteria pass. ✅

```json
{"simplified_word_count": 634, "original_word_count": 798, "all_essential_still_pass": true}
```
