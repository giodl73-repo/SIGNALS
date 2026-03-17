Written. Here's a summary of what changed:

---

## v3 Changes

**Two new aspirational criteria from Round 3 signals:**

- **C-13** — Anti-conflation prohibition stated per gate, not globally
  - Cause: V-02 had two prohibition sentences, one per gate. The structural distinction: each gate's prohibition names a specific contamination path (GATE 1: "high composite doesn't excuse an essential fail"; GATE 2: "don't score it if GATE 1 didn't pass"). A single general prohibition leaves both paths open.

- **C-14** — Each scorecard instance contains an inline gate-independence record
  - Cause: V-03's SQS pattern forced a per-scorecard record ("This scorecard beats the Status-Quo Scorer because..."), not just a preamble promise. C-12 is a promise to evaluate independently. C-14 is post-hoc evidence the promise was kept — verified at each instance rather than once at the prompt level.

**Formula updated**: aspirational denominator `/ 4` → `/ 6` (6 aspirational criteria now).

**New failure modes**: QG-10 (global-only prohibition) and QG-11 (preamble prohibition with no per-instance record).

**Excellence Signals Log**: Round 3 section appended with Patterns 3 and 4.

---

The distinction between C-12/C-13/C-14 is a ladder: C-12 = prohibition present, C-13 = prohibition is gate-specific, C-14 = independence evidenced per scorecard. A variation needs all three to close every conflation path.
a Detail

### Essential (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Full loop with 2+ rounds of named variations and scores | essential | behavior | Output includes at least two full scoring rounds, each containing named variations (V-NN format) with per-criterion pass/fail and a composite score. A rubric that is created but never applied to variations is a hard fail. A loop with only one round of variations is a hard fail. |
| C-02 | Dual convergence declared with both conditions named | essential | behavior | Output declares convergence by naming both independent conditions: (a) all scenarios pass for the trial dimension, and (b) no new excellence patterns for 2 consecutive rounds for the quest dimension. Declaring convergence without stating both conditions is a hard fail. Declaring only one condition is a hard fail. |
| C-03 | Golden prompt body written as a self-contained skill artifact | essential | behavior | Output includes a prompt body (not just a reference or summary) labeled as the golden prompt or skill body. The body must be self-contained — a reader could copy it as the skill's operative prompt without modification. A description of what the prompt should contain, without the prompt itself, is a hard fail. |
| C-04 | Final rubric produced with all three tiers | essential | coverage | Output includes a final rubric with essential, recommended, and aspirational criterion tiers, each containing at least one criterion. The rubric must be the converged version (reflecting all approved QU3/QU4 criterion additions). A rubric with only one tier or a v1 rubric with no additions from the loop is a hard fail unless the loop ran zero approved criterion additions. |
| C-05 | Numeric composite tracked per round per variation | essential | correctness | For every scoring round, output includes a numeric composite score (0-100) per variation computed from the formula: (essential_pass/N_essential x 60) + (recommended_pass/N_recommended x 30) + (aspirational_pass/N_aspirational x 10). A round with pass/fail tallies but no computed composite is a hard fail. A composite reported without showing which formula was applied is a fail. |

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
| C-10 | Dual convergence achieved in 5 rounds or fewer | aspirational | behavior | The trial dimension (all scenarios pass) and quest dimension (no new patterns) both converge within the first 5 rounds. Round count is computed from round 1 (first variation set). Convergence in round 6 or later is a fail for this criterion only -- it does not affect essential/recommended scoring. |
| C-11 | Composite formula embedded inline with concrete denominators | aspirational | correctness | The prompt body states the composite formula verbatim in the scoring step, with concrete numeric denominators resolved to the current rubric's criterion counts (e.g., essential_pass/5 x 60, not essential_pass/N_essential x 60). A prompt body that shows a scoring matrix with a COMPOSITE row but no formula is a fail. A formula with unresolved symbolic denominators is a fail. When the rubric adds criteria across rounds, the formula must update to reflect the new counts. |
| C-12 | Anti-conflation guard present in the dual-gate section | aspirational | behavior | The prompt body contains an explicit prohibition against collapsing the essential gate and the composite gate into a single check -- stated as a DO NOT rule or a procedural prohibition (e.g., "Do not conflate GATE 1 with GATE 2 -- they are independent checks" or "Execute both gates separately -- a single paragraph covering both is not acceptable"). Labeling two separate gate sections without an anti-conflation instruction is insufficient. The prohibition must be stated in the prompt body, not inferred from structure. |
| C-13 | Anti-conflation prohibition stated per gate, not globally | aspirational | behavior | The prompt body states a dedicated prohibition sentence for each scoring gate independently. GATE 1's prohibition must specify that a passing composite score does not satisfy GATE 1 if any essential criterion is PARTIAL or FAIL. GATE 2's prohibition must specify that it is only evaluated when GATE 1 is already satisfied. A single general "Do not conflate" sentence covering both gates without naming the specific cross-contamination path for each is a fail, even when C-12 is satisfied. Both gate-specific prohibition sentences must be present. |
| C-14 | Each scorecard instance contains an inline gate-independence record | aspirational | behavior | The prompt body's scoring step requires the operator to produce, per individual scorecard, an explicit record that the essential gate and composite gate were evaluated as independent checks -- not only that a prohibition was stated in the preamble. A per-scorecard record of the form "Essential gate evaluated independently of composite: Y" or a comparative sentence documenting what a conflating approach would have scored differently is sufficient. A preamble prohibition with no per-instance evidence requirement is a fail for this criterion. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Excellence Signals Log

### Round 1 -- 2026-03-15

**Pattern 1: Formula embedding separates 80 from 68**

- **Signal**: V-01 and V-02 scored 80; V-03, V-04, V-05 scored 68. The only structural cause: V-01/V-02 stated the composite formula explicitly in the prompt body's scoring step. V-03/V-04/V-05 showed a COMPOSITE matrix row without stating the formula, making the prompt body operator-dependent.
- **Evidence**: V-02 body: "Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)". V-03/V-04/V-05: matrix template with COMPOSITE row, formula absent.
- **Mechanism**: Self-containment failure. A prompt body that requires the operator to carry scoring rules from external context cannot be called a self-contained skill artifact for scoring purposes.
- **Principle**: All numeric rules (formulas, denominators) must be embedded inline in the step that uses them. A matrix template is scaffolding, not instruction. -> **C-11**

**Pattern 2: Anti-conflation guard prevents the most common C-02 failure mode**

- **Signal**: V-03 and V-04 had the strongest gate-separation language. V-03: "Do not conflate TRIAL CONVERGED with QUEST PLATEAUED. They are independent gates asking different questions." V-04: "Execute both gates separately. A single paragraph covering both is not acceptable."
- **Evidence**: All 5 variations passed C-02 in Round 1, but the structural property that makes C-02 robust across operator interpretations is the explicit prohibition -- not just labeling two sections.
- **Mechanism**: Gate-separation achieved by labeling is fragile; an operator can write a single compound paragraph that nominally references both gates. The prohibition must be stated.
- **Principle**: For any dual-gate declaration, the prompt body must explicitly prohibit collapsing the gates into a single check. Anti-conflation language is not redundant with gate labeling -- it forecloses a different failure path. -> **C-12**

### Round 3 -- 2026-03-16

**Pattern 3: Gate-specific prohibition closes the granularity gap**

- **Signal**: V-02 stated two prohibition sentences, one per gate. V-01 had no prohibition (C-12 FAIL). The structural distinction: per-gate prohibitions each foreclose a distinct cross-contamination path that a single general "do not conflate" sentence leaves open. Both V-01 and V-02 reached GOLDEN (82.5), but V-02's structure is more resistant to operator drift across future rounds.
- **Evidence**: V-02 GATE 1 prohibition: "Do not consider the composite score in GATE 1. A composite of 95 does not satisfy GATE 1 if any essential criterion is PARTIAL or FAIL. Do not conflate." V-02 GATE 2 prohibition: "Do not apply GATE 2 to a variation where GATE 1 is NOT SATISFIED. Do not conflate. A variation with an essential FAIL is FAIL regardless of its composite score."
- **Mechanism**: Each gate's prohibition names the specific contamination path for that gate. GATE 1's prohibition closes the "high composite exempts an essential failure" path. GATE 2's prohibition closes the "score it anyway even if essential fails" path. A single prohibition covers neither path at the gate level -- it relies on the operator's inference about which gate applies.
- **Principle**: Anti-conflation must be stated at the granularity of each gate, not globally. One prohibition per gate, each naming the specific cross-contamination it forecloses. -> **C-13**

**Pattern 4: Per-scorecard independence proof closes the execution gap**

- **Signal**: V-03's Status-Quo Scorer (SQS) framing required the operator to document, per individual scorecard, why their gate evaluation was not conflated. This produced execution-level evidence of independence, not only a preamble promise. V-01 had no prohibition; V-03 had both a preamble prohibition (C-12) and a per-instance record (C-14).
- **Evidence**: V-03 Step 3 analysis required: "beats the Status-Quo Scorer by: [one sentence per criterion where anti-conflation evaluation prevented a verdict]." V-03 per-scorecard record required: "This scorecard beats the Status-Quo Scorer because: [one sentence documenting that GATE 1 and GATE 2 were evaluated independently]."
- **Mechanism**: A preamble prohibition (C-12) is a promise to evaluate independently. A per-scorecard record (C-14) is post-hoc evidence the promise was kept. Without the per-instance record, a prompt satisfying C-12 can still produce scorecards where both gates are functionally collapsed -- the operator followed the structure but not the intent. The SQS pattern makes the intent verifiable at each instance.
- **Principle**: Gate independence must be evidenced at each scoring instance, not only declared in the preamble. The execution record closes the gap between stated intent and actual operator behavior. -> **C-14**

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
| QG-10 | C-13 | Single anti-conflation sentence covers both gates globally; no gate-specific prohibition naming the contamination path for GATE 1 and GATE 2 independently |
| QG-11 | C-14 | Prompt body contains anti-conflation prohibition in preamble but scoring step has no per-scorecard gate-independence record; independence declared once, not evidenced per instance |
