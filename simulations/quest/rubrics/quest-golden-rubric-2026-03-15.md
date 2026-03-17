# quest-golden rubric v2

**Version**: v2 | **Updated**: Round 1 (2026-03-15) | **Criteria**: 12 across 3 tiers

---

## Quick Reference

| ID | Text | Tier | Added |
|----|------|------|-------|
| C-01 | Full loop with 2+ rounds of named variations and scores | essential | v1 |
| C-02 | Dual convergence declared with both conditions named | essential | v1 |
| C-03 | Golden prompt body written as a self-contained skill artifact | essential | v1 |
| C-04 | Final rubric produced with all three tiers | essential | v1 |
| C-05 | Numeric composite tracked per round per variation | essential | v1 |
| C-06 | Excellence pattern named with structural cause (QU2) | recommended | v1 |
| C-07 | QU3 proposal + approval + QU4 application all present | recommended | v1 |
| C-08 | Quest plateau cited by round name (two specific rounds) | recommended | v1 |
| C-09 | Every prompt body element mapped to a criterion it passed | aspirational | v1 |
| C-10 | Dual convergence achieved in 5 rounds or fewer | aspirational | v1 |
| C-11 | Composite formula embedded inline with concrete denominators | aspirational | v2 R1 |
| C-12 | Anti-conflation guard present in the dual-gate section | aspirational | v2 R1 |

---

## Criteria Detail

### Essential (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Full loop with 2+ rounds of named variations and scores | essential | behavior | Output includes at least two full scoring rounds, each containing named variations (V-NN format) with per-criterion pass/fail and a composite score. A rubric that is created but never applied to variations is a hard fail. A loop with only one round of variations is a hard fail. |
| C-02 | Dual convergence declared with both conditions named | essential | behavior | Output declares convergence by naming both independent conditions: (a) all scenarios pass for the trial dimension, and (b) no new excellence patterns for 2 consecutive rounds for the quest dimension. Declaring convergence without stating both conditions is a hard fail. Declaring only one condition is a hard fail. |
| C-03 | Golden prompt body written as a self-contained skill artifact | essential | behavior | Output includes a prompt body (not just a reference or summary) labeled as the golden prompt or skill body. The body must be self-contained — a reader could copy it as the skill's operative prompt without modification. A description of what the prompt should contain, without the prompt itself, is a hard fail. |
| C-04 | Final rubric produced with all three tiers | essential | coverage | Output includes a final rubric with essential, recommended, and aspirational criterion tiers, each containing at least one criterion. The rubric must be the converged version (reflecting all approved QU3/QU4 criterion additions). A rubric with only one tier or a v1 rubric with no additions from the loop is a hard fail unless the loop ran zero approved criterion additions. |
| C-05 | Composite score tracked numerically per round | essential | correctness | For every scoring round, output includes a numeric composite score (0–100) per variation computed from the formula: (essential_pass/N_essential × 60) + (recommended_pass/N_recommended × 30) + (aspirational_pass/N_aspirational × 10). A round with pass/fail tallies but no computed composite is a hard fail. A composite reported without showing which formula was applied is a fail. |

### Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Excellence pattern extracted per round with specific evidence | recommended | depth | For each round where a new pattern is identified (QU2), output names the pattern, quotes or paraphrases the variation that surfaced it, and states what structural property was responsible. A vague "V-03 performed better" without naming the structural cause is a fail. |
| C-07 | QU3 proposal and QU4 application traced explicitly | recommended | behavior | For each criterion added to the rubric, output shows: (a) the QU3 proposal text, (b) the approval decision (approved / rejected / deferred), and (c) the QU4 application step that updated the rubric. A criterion that appears in the final rubric with no traceable QU3 proposal is a fail. A proposal present but with no (b) decision step is a fail. |
| C-08 | Quest plateau declared with 2-round citation | recommended | coverage | When the quest dimension converges, output cites the two consecutive rounds with no new patterns by name (e.g., "Round 4 and Round 5 produced no new excellence signals"). Declaring plateau without citing both rounds by explicit label is a fail. Citing "the last two rounds" without naming them is a fail. |

### Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Golden prompt body contains only structures that cleared rubric gates | aspirational | depth | The golden prompt body includes an explicit mapping: each structural element in the prompt body is traceable to a passing essential or recommended criterion. Elements present in the prompt body that do not correspond to any criterion are flagged as gratuitous inclusions. A one-sentence mapping table or inline annotation is sufficient. |
| C-10 | Dual convergence achieved in 5 rounds or fewer | aspirational | behavior | The trial dimension (all scenarios pass) and quest dimension (no new patterns) both converge within the first 5 rounds. Round count is computed from round 1 (first variation set). Convergence in round 6 or later is a fail for this criterion only — it does not affect essential/recommended scoring. |
| C-11 | Composite formula embedded inline with concrete denominators | aspirational | correctness | The prompt body states the composite formula verbatim in the scoring step, with concrete numeric denominators resolved to the current rubric's criterion counts (e.g., `essential_pass/5 × 60`, not `essential_pass/N_essential × 60`). A prompt body that shows a scoring matrix with a COMPOSITE row but no formula is a fail. A formula with unresolved symbolic denominators is a fail. When the rubric adds criteria across rounds, the formula must update to reflect the new counts. |
| C-12 | Anti-conflation guard present in the dual-gate section | aspirational | behavior | The prompt body contains an explicit prohibition against collapsing the trial gate and quest gate into a single check — stated as a DO NOT rule or a procedural prohibition (e.g., "Do not conflate TRIAL CONVERGED with QUEST PLATEAUED — they are independent gates" or "Execute both gates separately — a single paragraph covering both is not acceptable"). Labeling two separate gate sections without an anti-conflation instruction is insufficient. The prohibition must be stated in the prompt body, not inferred from structure. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Excellence Signals Log

### Round 1 — 2026-03-15

**Pattern 1: Formula embedding separates 80 from 68**

- **Signal**: V-01 and V-02 scored 80; V-03, V-04, V-05 scored 68. The only structural cause: V-01/V-02 stated the composite formula explicitly in the prompt body's scoring step. V-03/V-04/V-05 showed a COMPOSITE matrix row without stating the formula, making the prompt body operator-dependent.
- **Evidence**: V-02 body: `"Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)"`. V-03/V-04/V-05: matrix template with COMPOSITE row, formula absent.
- **Mechanism**: Self-containment failure. A prompt body that requires the operator to carry scoring rules from external context cannot be called a self-contained skill artifact for scoring purposes.
- **Principle**: All numeric rules (formulas, denominators) must be embedded inline in the step that uses them. A matrix template is scaffolding, not instruction. → **C-11**

**Pattern 2: Anti-conflation guard prevents the most common C-02 failure mode**

- **Signal**: V-03 and V-04 had the strongest gate-separation language. V-03: "Do not conflate TRIAL CONVERGED with QUEST PLATEAUED. They are independent gates asking different questions." V-04: "Execute both gates separately. A single paragraph covering both is not acceptable."
- **Evidence**: All 5 variations passed C-02 in Round 1, but the structural property that makes C-02 robust across operator interpretations is the explicit prohibition — not just labeling two sections.
- **Mechanism**: Gate-separation achieved by labeling is fragile; an operator can write a single compound paragraph that nominally references both gates. The prohibition must be stated.
- **Principle**: For any dual-gate declaration, the prompt body must explicitly prohibit collapsing the gates into a single check. Anti-conflation language is not redundant with gate labeling — it forecloses a different failure path. → **C-12**

---

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| QG-01 | C-02 | Convergence declared after trial passes but quest plateau not checked; only one condition stated |
| QG-02 | C-03 | Output ends with "the golden prompt should include X, Y, Z" rather than the prompt body itself |
| QG-03 | C-05 | Scores tallied as "3/5 essential pass" without computing the numeric composite |
| QG-04 | C-06 | Pattern identified by effect ("V-03 was more specific") without naming the structural property that caused it |
| QG-05 | C-07 | Final rubric contains new criteria with no prior QU3 proposal visible in the output |
| QG-06 | C-04 | Final rubric is the v1 rubric verbatim with no additions, but the loop ran approved QU3 proposals |
| QG-07 | C-01 | Only one round of variations shown; rubric created but no variation-scoring loop executed |
| QG-08 | C-11 | Prompt body shows scoring matrix with COMPOSITE row but never states the formula; operator must supply it from rubric context |
| QG-09 | C-12 | Prompt body labels GATE 1 and GATE 2 as separate sections but contains no explicit prohibition against collapsing them into a single compound check |
