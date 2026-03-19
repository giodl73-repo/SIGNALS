If --compact: output the winning prompt body only. Skip rubric criteria summary and 'What Made It Golden' section.

# quest:golden -- Find the Golden Prompt (V-05 -- Full Integration)

## Context

Skill: [SKILL_NAME]
Rubric version: [VERSION] (criteria C-[NN] through C-[NN])
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
     signals/quest/golden/{skill}-golden-{date}.md
   Include frontmatter: skill, date, rounds-to-convergence, rubric_final, score, status: golden.
   Body: complete, runnable prompt text -- DO NOT write only a summary or description.
3. Write the final accumulated rubric (all criteria from all rounds) to:
     signals/quest/rubrics/{skill}-rubric-v{N}-{date}.md
   Every criterion must include: ID, category, text, pass condition, weight, added-in-round.
4. State both artifact paths.
