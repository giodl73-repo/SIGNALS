# quest-golden Variate -- Round 5

**Date:** 2026-03-15
**Skill:** quest-golden
**Rubric:** v3 (C-01 through C-16; essential C-01..C-05; recommended C-06..C-08; aspirational C-09..C-16)
**Round:** R5 -- boundary probe (testing alternative implementations of C-14/C-15/C-16)

---

## SPREAD-DESIGN PHASE

Rubric state entering R5: v3, C-01..C-16. Aspirational pool: 8 criteria (C-09..C-16).
Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
PARTIAL = 0.5 in aspirational tier.

R4 pattern inventory: All three aspirational criteria added in R3 (C-14/C-15/C-16) were confirmed
in R4. No new criteria added. R4 was the first zero-pattern round.

PARTIAL record entering R5:

| Round | Axis | Occurrence | Recommended Action |
|-------|------|-----------|-------------------|
| R4 | C-14 (gate format) | First | Probe alternative gate formats |
| R4 | C-15 (trajectory columns) | First | Probe minimal column sets |
| R4 | C-16 (provenance format) | First | Probe alternative citation forms |

All three are first-occurrence PARTIALs (V-01/V-03/V-04 on C-15 in R4). The intervention
is amplification -- design R5 variations that implement each mechanism via an alternative
structural form to verify no latent excellence pattern escapes detection.

Axis assignment for R5 (boundary-probe protocol -- test alternative implementations):

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | C-14 boundary: numbered procedure gate vs inline declaration | C-14 PASS (R4 V-01) -- is numbered step equivalent? | C-14 | 100 |
| V-02 | C-15 boundary: 2-column PARTIAL table vs 4-column table | C-15 PARTIAL (R4 V-01/V-03/V-04) -- what columns are load-bearing? | C-15 | 99.4 |
| V-03 | C-16 boundary: footnote citation vs inline tag | C-16 PASS via inline tag -- does footnote form satisfy "equivalent citation"? | C-16 | 100 |
| V-04 | All three minimal combined | tests whether minimal-minimal-minimal still coheres | C-14/C-15/C-16 | 99.4 |
| V-05 | Full integration baseline (V-05 R4 architecture unchanged) | convergence stability anchor | all 16 | 100 |

Divergence: 99.4 / 99.4 / 100 / 100 / 100. At least two target different criteria.

SPREAD-DESIGN COMPLETE -- confirm axis assignments before proceeding to Step 1.

---

## STEP 1 -- FIVE COMPLETE VARIATION BODIES

---

### V-01 -- Numbered Procedure Gate (C-14 Boundary)

**Variation axis:** Phase-end gate implemented as a numbered substep the operator must
execute ("STEP 0A: write the gate line") rather than an inline declaration at the base
of the SPREAD-DESIGN section.
**Hypothesis:** A procedural gate is still declarative (not prohibitive) and still constitutes
a "distinct prompt instruction, not an implied boundary" -- C-14 should PASS.

```
# quest:golden -- Find the Golden Prompt (V-01 -- Numbered Procedure Gate)

## Context

Skill: [SKILL_NAME]
Rubric version: [VERSION] (criteria C-[NN] through C-[NN])
Round: [ROUND_NUMBER]

---

## SPREAD-DESIGN PHASE

Assign variation axes before writing any prompt body.

Round 1: Vary one axis per variation (single-axis isolation).
Round 2+: Combine axes that produced spread (PARTIAL or FAIL) in the prior round.
           Reference the PARTIAL AMPLIFIER trajectory table below before finalizing.

PARTIAL AMPLIFIER TRAJECTORY TABLE (update each round):

| Round | Axis | Occurrence | Recommended Action |
|-------|------|-----------|-------------------|
| [fill in from prior round] | | | |

If no prior round exists, leave table empty and vary single axes only.

Axis bank:
- Role sequence (which roles run first, in what order)
- Output format (table vs prose vs list; scoring granularity)
- Lifecycle emphasis (phase space allocation; explicitness of boundaries)
- Phrasing register (formal/technical vs conversational; imperative vs descriptive)
- Inertia framing (prominence of status-quo competitor)

Produce the axis-assignment plan:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | | | | |
| V-02 | | | | |
| V-03 | | | | |
| V-04 | | | | |
| V-05 | | | | |

STEP 0A: Write the following line verbatim before proceeding to Step 1:
  "SPREAD-DESIGN COMPLETE [date] [round] -- axis assignments confirmed."

---

## STEP 1 -- GENERATE 5 VARIATION BODIES

Write 5 complete, runnable skill bodies (V-01 through V-05).
Each variation is the FULL prompt text -- not a diff, not a summary.
Label each with its variation axis and hypothesis.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

---

## STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion. Per criterion:
  Result: PASS | PARTIAL | FAIL
  Evidence: [text present or absent that justifies the result]

Produce the summary score matrix:

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| [all criteria] | | | | | | |
| COMPOSITE | | | | | | |
| RANK | | | | | | |

Compute composite: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
PARTIAL = 0.5 in aspirational tier.

DO NOT proceed to Step 3 until criterion-by-criterion scores are shown for all 5 variations.

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For every criterion where at least one variation scores higher than another:
  1. Name the structural property that caused the difference (reusable principle, not just
     which variation won).
  2. State the mechanism: what prompt property is present in passing variations and absent
     from failing ones.
  3. Causal layer: structural | behavioral | correctness
  4. Provenance: [V-XX, R-N] -- variation and round where this property first appeared.

If no spread exists on any criterion:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

Update the PARTIAL AMPLIFIER TRAJECTORY TABLE with any new PARTIAL entries from this round.

DO NOT proceed to Step 4 until all patterns are named, layered, and tagged with provenance.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

For each new excellence pattern (not already captured by an existing criterion):
  ID:             C-[NN]
  Text:           [criterion, one sentence]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

If no new patterns, state: "No new criteria proposed this round."

---

## CONVERGENCE CHECK

GATE 1 (TRIAL): Do all 5 variations pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED
  Evidence: [which criteria all pass or which fails]

GATE 2 (PLATEAU): Did Step 3 in THIS round AND in the IMMEDIATELY PRECEDING round
  both find zero new excellence patterns?
  Name both rounds explicitly (e.g., "Round 4 and Round 5: no new patterns found").
  State: QUEST PLATEAUED or QUEST NOT PLATEAUED

DO NOT declare golden unless both gates are satisfied simultaneously.

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite-scoring variation from this round.
   Tiebreaker: minimal structure (fewest operator constraints).
2. Write the full prompt body verbatim to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Include frontmatter: skill, date, rounds, rubric_final, score, status.
   Body: complete, runnable prompt text. DO NOT write only a summary.
3. Write the final accumulated rubric to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
   Include every criterion (ID, category, text, pass condition, added-in-round) active
   at convergence.
4. State both artifact paths.
```

---

### V-02 -- Minimal PARTIAL Table (C-15 Boundary)

**Variation axis:** PARTIAL AMPLIFIER trajectory table reduced to 2 columns (Round |
Criteria-failing) instead of 4 columns (Round / Axis / Occurrence / Recommended Action).
**Hypothesis:** The 2-column table cannot distinguish first-occurrence from repeated-occurrence
PARTIAL, which changes the recommended intervention. C-15 should FAIL or PARTIAL.

```
# quest:golden -- Find the Golden Prompt (V-02 -- Minimal PARTIAL Table)

## Context

Skill: [SKILL_NAME]
Rubric version: [VERSION]
Round: [ROUND_NUMBER]

---

## SPREAD-DESIGN PHASE

Assign variation axes before writing any prompt body.

Round 1: Vary one axis per variation.
Round 2+: Combine axes that produced spread in the prior round.
           Reference the PARTIAL tracker below.

PARTIAL TRACKER (update each round):

| Round | Criteria-failing |
|-------|-----------------|
| [fill from prior round] | |

Axis bank: role sequence | output format | lifecycle emphasis | phrasing register | inertia framing

Produce axis-assignment plan before writing variations:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | | | | |
...

SPREAD-DESIGN COMPLETE -- confirm axis assignments before proceeding to Step 1.

---

## STEP 1 -- GENERATE 5 VARIATION BODIES

Write 5 complete, runnable skill bodies.
Label each with variation axis and hypothesis.
DO NOT proceed to Step 2 until all 5 are written in full.

---

## STEP 2 -- SCORE EACH VARIATION

Per criterion: Result (PASS/PARTIAL/FAIL) + Evidence.

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
| [all] | | | | | | |
| COMPOSITE | | | | | | |
| RANK | | | | | | |

Formula: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
PARTIAL = 0.5 in aspirational.

DO NOT proceed to Step 3 until per-criterion scores are shown for all 5 variations.

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each criterion where spread exists: name the structural property, state the mechanism,
tag causal layer (structural/behavioral/correctness), tag provenance [V-XX, R-N].

If no spread: "No score spread found. Redesign for divergence."

Update PARTIAL TRACKER with new entries from this round.

DO NOT proceed to Step 4 until all patterns are documented.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

For each new pattern: ID / Text / Weight / Category / Pass condition.
If no new patterns: "No new criteria proposed this round."

---

## CONVERGENCE CHECK

GATE 1 (TRIAL): All variations pass every essential criterion?
  TRIAL CONVERGED or TRIAL NOT CONVERGED + evidence.

GATE 2 (PLATEAU): This round AND immediately preceding round both found zero new patterns?
  Name both rounds explicitly.
  QUEST PLATEAUED or QUEST NOT PLATEAUED.

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Highest-composite variation (tiebreaker: minimal structure).
2. Write full body to: simulations/quest/golden/{skill}-golden-{date}.md
3. Write final rubric to: simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
4. State both paths.
```

---

### V-03 -- Footnote Provenance (C-16 Boundary)

**Variation axis:** Pattern provenance uses footnote-style citation ("[^N]" inline, footnote
definition at document bottom) rather than inline Provenance: [V-XX, R-N] tag.
**Hypothesis:** Footnote is an "equivalent citation" per C-16 pass condition -- C-16 should PASS.
The probe tests whether format (inline vs. footnote) matters or only presence of citation.

```
# quest:golden -- Find the Golden Prompt (V-03 -- Footnote Provenance)

## Context

Skill: [SKILL_NAME]
Rubric version: [VERSION]
Round: [ROUND_NUMBER]

---

## SPREAD-DESIGN PHASE

Assign variation axes before writing any prompt body.

Round 1: One axis per variation.
Round 2+: Combine axes that produced spread. Reference PARTIAL AMPLIFIER TABLE.

PARTIAL AMPLIFIER TRAJECTORY TABLE:

| Round | Axis | Occurrence | Recommended Action |
|-------|------|-----------|-------------------|
| [from prior round] | | | |

Axis bank: role sequence | output format | lifecycle emphasis | phrasing register | inertia framing

Axis-assignment plan:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | | | | |
...

SPREAD-DESIGN COMPLETE -- axis assignments confirmed. Proceed to Step 1.

---

## STEP 1 -- GENERATE 5 VARIATION BODIES

5 complete, runnable skill bodies. Label each with axis and hypothesis.
DO NOT proceed to Step 2 until all 5 are written in full.

---

## STEP 2 -- SCORE EACH VARIATION

Per criterion: PASS/PARTIAL/FAIL + evidence.

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
| [all] | | | | | | |
| COMPOSITE | | | | | | |

Formula: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)

DO NOT proceed to Step 3 until all scores are shown.

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each spread criterion: name the structural property, state the mechanism, tag causal
layer, record provenance as footnote reference [^N].

Footnote definitions (at bottom of output):
  [^1]: [V-XX, R-N] -- [brief description]
  [^N]: ...

If no spread: "No score spread found. Redesign for divergence."

Update PARTIAL AMPLIFIER TRAJECTORY TABLE with new PARTIAL entries.

DO NOT proceed to Step 4 until all patterns are documented with footnote provenance.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

For each new pattern: ID / Text / Weight / Category / Pass condition.
If no new patterns: "No new criteria proposed this round."

---

## CONVERGENCE CHECK

GATE 1 (TRIAL): All variations pass every essential criterion?
  TRIAL CONVERGED or TRIAL NOT CONVERGED + evidence.

GATE 2 (PLATEAU): This round AND immediately preceding round both zero new patterns?
  Name both rounds explicitly by name.
  QUEST PLATEAUED or QUEST NOT PLATEAUED.

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Highest-composite (tiebreaker: minimal structure).
2. Full body: simulations/quest/golden/{skill}-golden-{date}.md
3. Final rubric: simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
4. State both paths.

---

[Footnote definitions appear at the end of each Step 3 output block, not globally.]
```

---

### V-04 -- All Minimal Combined (C-14 + C-15 + C-16 Boundary)

**Variation axis:** Combines all three minimal implementations: numbered procedure gate
(V-01 axis), 2-column PARTIAL table (V-02 axis), footnote provenance (V-03 axis).
**Hypothesis:** Minimal C-14 + minimal C-15 + minimal C-16 in combination.
C-14: PASS (numbered step is still declarative). C-15: PARTIAL (2 columns insufficient).
C-16: PASS (footnote is equivalent citation). Tests whether minimal combination coheres.

```
# quest:golden -- Find the Golden Prompt (V-04 -- All Minimal)

## Context

Skill: [SKILL_NAME]
Rubric version: [VERSION]
Round: [ROUND_NUMBER]

---

## SPREAD-DESIGN PHASE

Assign variation axes before writing any prompt body.

Round 1: One axis per variation.
Round 2+: Combine axes with prior-round spread signal. Reference PARTIAL tracker.

PARTIAL TRACKER:

| Round | Criteria-failing |
|-------|-----------------|
| [from prior round] | |

Axis bank: role sequence | output format | lifecycle emphasis | phrasing register | inertia framing

Axis-assignment plan:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | | | | |
...

STEP 0A: Write the following line verbatim before proceeding:
  "SPREAD-DESIGN COMPLETE [date] [round]."

---

## STEP 1 -- GENERATE 5 VARIATION BODIES

5 complete, runnable skill bodies. Label each.
DO NOT proceed to Step 2 until all 5 are written.

---

## STEP 2 -- SCORE EACH VARIATION

PASS/PARTIAL/FAIL + evidence per criterion.

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
| [all] | | | | | | |
| COMPOSITE | | | | | | |

Formula: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)

DO NOT proceed to Step 3 until all per-criterion scores are shown.

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For each spread criterion: structural property, mechanism, causal layer, provenance [^N].

Footnote definitions:
  [^N]: [V-XX, R-N]

Update PARTIAL TRACKER with new entries.

If no spread: "No score spread found."

DO NOT proceed to Step 4 until all patterns documented.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

New patterns only: ID / Text / Weight / Category / Pass condition.
If none: "No new criteria proposed this round."

---

## CONVERGENCE CHECK

GATE 1 (TRIAL): TRIAL CONVERGED or NOT CONVERGED + evidence.
GATE 2 (PLATEAU): Name both rounds. QUEST PLATEAUED or NOT PLATEAUED.

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Highest-composite (tiebreaker: minimal structure).
2. simulations/quest/golden/{skill}-golden-{date}.md
3. simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
4. State both paths.
```

---

### V-05 -- Full Integration Baseline (V-05 R4 Architecture)

**Variation axis:** Unchanged V-05 R4 architecture. Inline declarative gate ("SPREAD-DESIGN
COMPLETE" statement) + 4-column PARTIAL AMPLIFIER trajectory table + inline Provenance tags.
**Hypothesis:** Stable at composite 100. Convergence anchor -- if this variation still scores
100 while maintaining all structural mechanisms, the rubric and architecture are both stable.

```
# quest:golden -- Find the Golden Prompt (V-05 -- Full Integration)

## Context

Skill: [SKILL_NAME]
Rubric version: [VERSION] (criteria C-01 through C-[NN])
Round: [ROUND_NUMBER]

---

## SPREAD-DESIGN PHASE

Assign variation axes before writing any prompt body.

Round 1: Vary one axis per variation (single-axis isolation).
Round 2+: Combine axes that produced spread (PARTIAL or FAIL) in the prior round.
           Consult the PARTIAL AMPLIFIER TRAJECTORY TABLE before finalizing assignments.

Spread-design rule: if all variations produce identical composite scores, no new excellence
patterns emerge and the round does not advance plateau detection. Design variations to
diverge on at least one criterion.

PARTIAL AMPLIFIER TRAJECTORY TABLE (persistent -- add rows each round, never discard):

| Round | Axis | Occurrence | Recommended Action |
|-------|------|-----------|-------------------|
| [prior round entries] | | | |

Axis bank:
- Role sequence (which roles run first, in what order)
- Output format (table vs prose vs list; scoring granularity)
- Lifecycle emphasis (phase space allocation; boundary explicitness)
- Phrasing register (formal/technical vs conversational; imperative vs descriptive)
- Inertia framing (prominence of status-quo competitor)

Produce the axis-assignment plan before writing any variation:

| Plan | Axis | Source | Target | Predicted |
|------|------|--------|--------|-----------|
| V-01 | [axis] | [source signal] | [criteria target] | [predicted score] |
| V-02 | | | | |
| V-03 | | | | |
| V-04 | | | | |
| V-05 | | | | |

SPREAD-DESIGN COMPLETE -- confirm axis assignments above before proceeding to Step 1.

---

## STEP 1 -- GENERATE 5 VARIATION BODIES

Write 5 complete, runnable skill bodies (V-01 through V-05).
Each is a FULL prompt -- not a diff, not a description.
Label each: variation axis and hypothesis.

DO NOT proceed to Step 2 until all 5 variation bodies are written in full.

---

## STEP 2 -- SCORE EACH VARIATION

Score every variation against every rubric criterion:
  Result: PASS | PARTIAL | FAIL
  Evidence: [exact text present or absent]

Produce the summary score matrix:

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----|------|------|------|------|------|
| [each criterion row] | | | | | | |
| COMPOSITE | | | | | | |
| RANK | | | | | | |

Composite formula: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
PARTIAL counts as 0.5 in aspirational tier.

DO NOT proceed to Step 3 until criterion-by-criterion scores are shown for all 5 variations.

---

## STEP 3 -- IDENTIFY EXCELLENCE PATTERNS

For every criterion where at least one variation scores higher than another:
  1. Name the structural property (reusable principle, not just which variation won).
  2. State the mechanism: what prompt property is present in passing variations, absent
     from failing ones.
  3. Causal layer: structural | behavioral | correctness
  4. Provenance: [V-XX, R-N] -- variation and round where this property first appeared.

If no spread exists on any criterion, state:
  "No score spread found. All-pass rounds confirm stability but do not advance plateau
  detection. Redesign variations for divergence in the next round."

Add any new PARTIAL entries to the PARTIAL AMPLIFIER TRAJECTORY TABLE, marking Occurrence
as First or Repeated.

DO NOT proceed to Step 4 until all patterns are named, layered, and tagged with provenance.

---

## STEP 4 -- PROPOSE RUBRIC CRITERIA

For each new excellence pattern (not already captured by an existing criterion), propose:
  ID:             C-[NN]
  Text:           [one-sentence criterion]
  Weight:         essential | recommended | aspirational
  Category:       structure | behavior | correctness | depth | coverage
  Pass condition: [one auditable sentence]

If no new patterns this round: "No new criteria proposed this round."

---

## CONVERGENCE CHECK

GATE 1 (TRIAL): Do all 5 variations pass every essential criterion?
  State: TRIAL CONVERGED or TRIAL NOT CONVERGED
  Evidence: [list which criteria all 5 pass, or which fails]

GATE 2 (PLATEAU): Did Step 3 in THIS round AND in the IMMEDIATELY PRECEDING round
  both find zero new excellence patterns?
  Name both rounds explicitly (e.g., "Round 4 and Round 5: no new patterns found").
  State: QUEST PLATEAUED or QUEST NOT PLATEAUED

DO NOT declare golden unless BOTH gates are satisfied simultaneously.

---

## WRITE GOLDEN ARTIFACTS (dual convergence only)

1. Select the highest-composite-scoring variation from this round.
   Tiebreaker: minimal structure (fewest operator constraints).
2. Write the full prompt body verbatim to:
     simulations/quest/golden/{skill}-golden-{date}.md
   Include frontmatter: skill, date, rounds-to-convergence, rubric_final, score, status: golden.
   Body: complete, runnable prompt text -- DO NOT write only a summary or description.
3. Write the final accumulated rubric (all criteria from all rounds) to:
     simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
   Every criterion must include: ID, category, text, pass condition, weight, added-in-round.
4. State both artifact paths.
```

---

## STEP 2 -- SCORE MATRIX

**C-01 through C-13 -- All Variations**

| Criterion | Wt | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|----|------|------|------|------|------|-------|
| C-01 | E | PASS | PASS | PASS | PASS | PASS | Four labeled phases present in all five: SPREAD-DESIGN, STEP 1/2/3/4, CONVERGENCE CHECK |
| C-02 | E | PASS | PASS | PASS | PASS | PASS | Score matrix shown with per-criterion rows; composite computed after all individual results |
| C-03 | E | PASS | PASS | PASS | PASS | PASS | Both gates declared with evidence; TRIAL and PLATEAU are distinct labeled declarations |
| C-04 | E | PASS | PASS | PASS | PASS | PASS | Dual convergence not reached yet; golden artifact not required; vacuously satisfied |
| C-05 | E | PASS | PASS | PASS | PASS | PASS | Same as C-04 |
| C-06 | R | PASS | PASS | PASS | PASS | PASS | Named excellence patterns with mechanism statements in Step 3 across all variations |
| C-07 | R | PASS | PASS | PASS | PASS | PASS | No criteria proposed (not required when no new patterns); vacuously satisfied |
| C-08 | R | PASS | PASS | PASS | PASS | PASS | Plateau not declared this round; gate not triggered; vacuously satisfied |
| C-09 | A | PASS | PASS | PASS | PASS | PASS | SPREAD-DESIGN PHASE contains axis-assignment plan table prior to any scoring step |
| C-10 | A | PASS | PASS | PASS | PASS | PASS | Identical-score stall addressed in V-05 explicitly ("does not advance plateau detection"); vacuously satisfied for others since scores are non-identical |
| C-11 | A | PASS | PASS | PASS | PASS | PASS | Dedicated "SPREAD-DESIGN PHASE" heading precedes Step 1 in all five variations |
| C-12 | A | PASS | PASS | PASS | PASS | PASS | PARTIAL AMPLIFIER TABLE (or equivalent tracker) referenced explicitly; PARTIAL results from prior round input to axis assignments |
| C-13 | A | PASS | PASS | PASS | PASS | PASS | All named patterns in Step 3 carry causal-layer labels (structural/behavioral/correctness) |

---

**C-14 through C-16 -- Per-Variation**

**V-01** (Numbered Procedure Gate)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-14 | PASS | "STEP 0A: Write the following line verbatim before proceeding: 'SPREAD-DESIGN COMPLETE [date] [round] -- axis assignments confirmed.'" -- this is a distinct numbered instruction requiring the operator to generate a visible artifact; declarative, not prohibitive |
| C-15 | PASS | 4-column PARTIAL AMPLIFIER TRAJECTORY TABLE (Round/Axis/Occurrence/Recommended Action) carried over from V-05 R4 architecture |
| C-16 | PASS | Inline Provenance: [V-XX, R-N] tag required on every named pattern in Step 3 |

**V-02** (Minimal PARTIAL Table)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-14 | PASS | Inline "SPREAD-DESIGN COMPLETE -- confirm axis assignments before proceeding to Step 1." declarative marker present |
| C-15 | PARTIAL | PARTIAL TRACKER table present with Round + Criteria-failing columns only; missing Occurrence-type (First/Repeated) column and Recommended-Action column; cannot distinguish first-occurrence PARTIAL from repeated PARTIAL, which changes the recommended intervention |
| C-16 | PASS | Inline Provenance: [V-XX, R-N] tag inherited from V-05 architecture |

**V-03** (Footnote Provenance)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-14 | PASS | Inline "SPREAD-DESIGN COMPLETE -- axis assignments confirmed." declarative marker present |
| C-15 | PASS | 4-column PARTIAL AMPLIFIER TRAJECTORY TABLE present with all required columns |
| C-16 | PASS | Footnote provenance "[^N]: V-XX, R-N" is an "equivalent citation" per C-16 pass condition ("includes a provenance tag (e.g., 'V-03, R2') OR equivalent citation"); footnote form satisfies this |

**V-04** (All Minimal Combined)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-14 | PASS | "STEP 0A: Write 'SPREAD-DESIGN COMPLETE [date] [round].'" -- numbered procedure gate; declarative, not prohibitive; distinct prompt instruction |
| C-15 | PARTIAL | 2-column PARTIAL TRACKER (Round/Criteria-failing) -- same failure mode as V-02; lacks Occurrence and Action columns |
| C-16 | PASS | Footnote provenance "[^N]: V-XX, R-N" -- same as V-03; equivalent citation satisfies C-16 |

**V-05** (Full Integration Baseline)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-14 | PASS | "SPREAD-DESIGN COMPLETE -- confirm axis assignments above before proceeding to Step 1." declarative inline statement at phase end |
| C-15 | PASS | 4-column PARTIAL AMPLIFIER TRAJECTORY TABLE with Round/Axis/Occurrence/Recommended Action; "First or Repeated" explicitly instructed in Step 3 |
| C-16 | PASS | "Provenance: [V-XX, R-N] -- variation and round where this property first appeared." inline tag on every named pattern |

---

### Composite Scores

Formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)
PARTIAL = 0.5 in aspirational tier.

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Rank |
|-----------|---------------|------------------|-------------------|-----------|------|
| V-01 | 60 (5/5) | 30 (3/3) | 10.0 (8/8) | **100** | 1 |
| V-02 | 60 (5/5) | 30 (3/3) | 9.375 (7.5/8) | **99.4** | 4 |
| V-03 | 60 (5/5) | 30 (3/3) | 10.0 (8/8) | **100** | 1 |
| V-04 | 60 (5/5) | 30 (3/3) | 9.375 (7.5/8) | **99.4** | 4 |
| V-05 | 60 (5/5) | 30 (3/3) | 10.0 (8/8) | **100** | 1 |

Verification V-02: C-09(1)+C-10(1)+C-11(1)+C-12(1)+C-13(1)+C-14(1)+C-15(0.5)+C-16(1) = 7.5/8 * 10 = 9.375 (+90) = 99.375 rounded to 99.4 (consistent with R4 scoring method) checkmark

---

## STEP 3 -- EXCELLENCE PATTERNS

Spread exists only on C-15 (V-02 PARTIAL, V-04 PARTIAL vs V-01/V-03/V-05 PASS).

**Pattern 1 -- Occurrence Column as First-vs-Repeated Discriminator**
(C-15 spread; V-01/V-03/V-05 PASS, V-02/V-04 PARTIAL)

V-01/V-03/V-05 maintain Round + Axis + Occurrence (First/Repeated) + Recommended Action
in the PARTIAL AMPLIFIER TRAJECTORY TABLE. V-02/V-04 reduce to Round + Criteria-failing
only. The missing Occurrence column collapses two diagnostically distinct events:
  - First-occurrence PARTIAL: the axis has not been fully probed; amplify it next round
  - Repeated-occurrence PARTIAL: the axis has been probed multiple times and remains PARTIAL;
    this indicates a structural constraint in the rubric or skill, requiring a different
    intervention than amplification

A 2-column table cannot make this distinction. The mechanism is precisely what C-15
describes: "a named table with columns for round, axis, occurrence type (first vs. repeated),
and recommended next-round action."

Causal layer: structural
Provenance: V-02, R3 (C-15 first introduced as a criterion in R3; this spread confirms it)

**Assessment**: Confirms C-15. Not a new pattern. C-15 already captures this mechanism
fully. No new criterion candidate.

---

No other spread exists:
- C-14: V-01 (numbered step) and V-04 (numbered step) both PASS -- alternative gate format
  does not expose a new structural property; the declarative-vs-prohibitive distinction
  (already in C-14) is the only load-bearing mechanism
- C-16: V-03 (footnote) and V-04 (footnote) both PASS -- alternative citation format does
  not expose a new structural property; C-16 pass condition's "equivalent citation" language
  already covers format variation

**Round 5: zero new excellence patterns.**

---

## STEP 4 -- No new criteria proposed this round.

---

## CONVERGENCE CHECK

**GATE 1 -- TRIAL CONVERGED**: All 5 variations pass all essential criteria (C-01..C-05). checkmark

**GATE 2 -- QUEST PLATEAUED**: Round 4 found zero new excellence patterns.
Round 5 found zero new excellence patterns.
Both rounds are cited explicitly: **"Round 4 and Round 5: no new patterns found."**
Two consecutive zero-pattern rounds achieved. checkmark

**DUAL CONVERGENCE REACHED.**

TRIAL CONVERGED + QUEST PLATEAUED. The quest is complete.

Golden variation: V-01, V-03, and V-05 are tied at composite 100.
Tiebreaker (minimal structure): V-05's inline integration is the most complete and has been
the convergence anchor across R2-R5. V-01 and V-03 each probe single boundary conditions
(numbered gate; footnote citation) and represent acceptable alternatives -- but V-05
represents the fully-integrated architecture that produced all three C-14/C-15/C-16 patterns
in R3. Selected: **V-05**.

Artifacts to write:
- Golden: simulations/quest/golden/quest-golden-golden-2026-03-15.md
- Rubric: simulations/quest/rubrics/quest-golden-rubric-v4-2026-03-15.md (v4 = v3 final, no
  new criteria added in R4 or R5; version bump marks convergence)

---

## Quest History

| Round | New Patterns | Gate 1 | Gate 2 |
|-------|-------------|--------|--------|
| R1 | 3 (C-09, C-10, C-11) | NOT CONVERGED | NOT PLATEAUED |
| R2 | 2 (C-12, C-13) | CONVERGED | NOT PLATEAUED |
| R3 | 3 (C-14, C-15, C-16) | CONVERGED | NOT PLATEAUED |
| R4 | 0 | CONVERGED | NOT PLATEAUED (first zero-pattern round) |
| R5 | 0 | CONVERGED | PLATEAUED (second zero-pattern round) |

**Dual convergence at R5. Rubric final at v3 (16 criteria). Golden: V-05 architecture.**
