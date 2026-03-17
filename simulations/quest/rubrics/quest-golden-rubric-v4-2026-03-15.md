Reading the Round 4 scorecard carefully before deriving the new criteria.

**Signal 1** (V-01): "PARTIAL" added to GATE 1's prohibition is not cosmetic — it names a rubric verdict state that exists and that a conflating scorer can exploit if only "FAIL" is named. The general principle: prohibition sentences must enumerate every non-PASS rubric verdict label explicitly; a paraphrase leaves escape paths.

**Signal 2** (V-02): Moving the gate-independence requirement from a preamble instruction to a labeled field in the scorecard template creates a visible gap when the field is absent. A preamble instruction can be "complied with" without leaving any trace; a template slot cannot. The distinction: C-14 requires the per-instance record be *required*; C-16 requires the requirement be *structural*.

The ladder now runs: C-12 (guard exists) → C-13 (guard is gate-specific) → C-14 (per-instance evidence) → C-15 (verdict vocabulary exact) → C-16 (evidence is a template slot).

---

```markdown
# Quest Rubric — v4

## Essential (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Full loop with 2+ rounds of named variations and scores | essential | behavior | Output includes at least two full scoring rounds, each containing named variations (V-NN format) with per-criterion pass/fail and a composite score. A rubric that is created but never applied to variations is a hard fail. A loop with only one round of variations is a hard fail. |
| C-02 | Dual convergence declared with both conditions named | essential | behavior | Output declares convergence by naming both independent conditions: (a) all scenarios pass for the trial dimension, and (b) no new excellence patterns for 2 consecutive rounds for the quest dimension. Declaring convergence without stating both conditions is a hard fail. Declaring only one condition is a hard fail. |
| C-03 | Golden prompt body written as a self-contained skill artifact | essential | behavior | Output includes a prompt body (not just a reference or summary) labeled as the golden prompt or skill body. The body must be self-contained — a reader could copy it as the skill's operative prompt without modification. A description of what the prompt should contain, without the prompt itself, is a hard fail. |
| C-04 | Final rubric produced with all three tiers | essential | coverage | Output includes a final rubric with essential, recommended, and aspirational criterion tiers, each containing at least one criterion. The rubric must be the converged version (reflecting all approved QU3/QU4 criterion additions). A rubric with only one tier or a v1 rubric with no additions from the loop is a hard fail unless the loop ran zero approved criterion additions. |
| C-05 | Numeric composite tracked per round per variation | essential | correctness | For every scoring round, output includes a numeric composite score (0-100) per variation computed from the formula: (essential_pass/N_essential x 60) + (recommended_pass/N_recommended x 30) + (aspirational_pass/N_aspirational x 10). A round with pass/fail tallies but no computed composite is a hard fail. A composite reported without showing which formula was applied is a fail. |

## Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Excellence pattern extracted per round with specific evidence | recommended | depth | For each round where a new pattern is identified (QU2), output names the pattern, quotes or paraphrases the variation that surfaced it, and states what structural property was responsible. A vague "V-03 performed better" without naming the structural cause is a fail. |
| C-07 | QU3 proposal and QU4 application traced explicitly | recommended | behavior | For each criterion added to the rubric, output shows: (a) the QU3 proposal text, (b) the approval decision (approved / rejected / deferred), and (c) the QU4 application step that updated the rubric. A criterion that appears in the final rubric with no traceable QU3 proposal is a fail. A proposal present but with no (b) decision step is a fail. |
| C-08 | Quest plateau declared with 2-round citation | recommended | coverage | When the quest dimension converges, output cites the two consecutive rounds with no new patterns by name (e.g., "Round 4 and Round 5 produced no new excellence signals"). Declaring plateau without citing both rounds by explicit label is a fail. Citing "the last two rounds" without naming them is a fail. |

## Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Golden prompt body contains only structures that cleared rubric gates | aspirational | depth | The golden prompt body includes an explicit mapping: each structural element in the prompt body is traceable to a passing essential or recommended criterion. Elements present in the prompt body that do not correspond to any criterion are flagged as gratuitous inclusions. A one-sentence mapping table or inline annotation is sufficient. |
| C-10 | Dual convergence achieved in 5 rounds or fewer | aspirational | behavior | The trial dimension (all scenarios pass) and quest dimension (no new patterns) both converge within the first 5 rounds. Round count is computed from round 1 (first variation set). Convergence in round 6 or later is a fail for this criterion only — it does not affect essential/recommended scoring. |
| C-11 | Composite formula embedded inline with concrete denominators | aspirational | correctness | The prompt body states the composite formula verbatim in the scoring step, with concrete numeric denominators resolved to the current rubric's criterion counts (e.g., essential_pass/5 x 60, not essential_pass/N_essential x 60). A prompt body that shows a scoring matrix with a COMPOSITE row but no formula is a fail. A formula with unresolved symbolic denominators is a fail. When the rubric adds criteria across rounds, the formula must update to reflect the new counts. |
| C-12 | Anti-conflation guard present in the dual-gate section | aspirational | behavior | The prompt body contains an explicit prohibition against collapsing the essential gate and the composite gate into a single check — stated as a DO NOT rule or a procedural prohibition (e.g., "Do not conflate GATE 1 with GATE 2 — they are independent checks" or "Execute both gates separately — a single paragraph covering both is not acceptable"). Labeling two separate gate sections without an anti-conflation instruction is insufficient. The prohibition must be stated in the prompt body, not inferred from structure. |
| C-13 | Anti-conflation prohibition stated per gate, not globally | aspirational | behavior | The prompt body states a dedicated prohibition sentence for each scoring gate independently. GATE 1's prohibition must specify that a passing composite score does not satisfy GATE 1 if any essential criterion is PARTIAL or FAIL. GATE 2's prohibition must specify that it is only evaluated when GATE 1 is already satisfied. A single general "Do not conflate" sentence covering both gates without naming the specific cross-contamination path for each is a fail, even when C-12 is satisfied. Both gate-specific prohibition sentences must be present. |
| C-14 | Each scorecard instance contains an inline gate-independence record | aspirational | behavior | The prompt body's scoring step requires the operator to produce, per individual scorecard, an explicit record that the essential gate and composite gate were evaluated as independent checks — not only that a prohibition was stated in the preamble. A per-scorecard record of the form "Essential gate evaluated independently of composite: Y" or a comparative sentence documenting what a conflating approach would have scored differently is sufficient. A preamble prohibition with no per-instance evidence requirement is a fail for this criterion. |
| C-15 | Gate prohibition sentences enumerate all non-PASS verdict states by rubric label | aspirational | behavior | The prompt body's GATE 1 prohibition sentence names every non-PASS verdict state using the rubric's exact verdict labels — both PARTIAL and FAIL must appear by name. A prohibition that uses a paraphrase such as "does not pass," "any weakness," or "is not fully passing" instead of naming PARTIAL and FAIL explicitly leaves an escape path: a conflating scorer can interpret the paraphrase as covering only FAIL and treat PARTIAL as an ambiguous middle ground not subject to the gate. This criterion is not satisfied by C-13 alone. C-13 requires gate-specific prohibition content; C-15 requires that content to close all rubric-defined non-PASS states by name. A prohibition that names FAIL but not PARTIAL is a fail. A prohibition that names PARTIAL but not FAIL is a fail. |
| C-16 | Gate-independence record is a labeled slot in the scorecard template, not a prose instruction | aspirational | behavior | The prompt body's scorecard template includes a dedicated labeled placeholder for the gate-independence record as a structural element of the template itself — a field a reader can see is blank if not completed (e.g., `Gate-independence record: ___`, a named sub-step completion field, or an equivalent structural slot). The slot must appear inside the template definition, not in a preamble, a parenthetical instruction, or a "note to operator" paragraph. A prompt body that instructs the operator to record gate independence without embedding a corresponding field in the scorecard template produces unverifiable compliance: the instruction may have been "followed" without leaving any detectable trace in the output. This criterion extends C-14: C-14 requires the per-instance record be required; C-16 requires the requirement be structural (a template slot with a visible gap when absent), not rhetorical (an instruction with no output artifact). |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Failure Mode Reference

| Code | Criterion | Failure Mode |
|------|-----------|--------------|
| QG-01 | C-01 | Single-round loop (no variation-to-variation scoring across rounds) |
| QG-02 | C-02 | Convergence declared without stating both trial and quest conditions |
| QG-03 | C-03 | Prompt described but not written as a self-contained body |
| QG-04 | C-04 | Final rubric omits one or more tiers, or uses v1 with no additions |
| QG-05 | C-05 | Round shows pass/fail tallies but no computed composite |
| QG-06 | C-06 | Pattern named without identifying the structural cause |
| QG-07 | C-07 | Criterion in final rubric with no traceable QU3 proposal or approval decision |
| QG-08 | C-08 | Quest convergence declared without citing both plateau rounds by name |
| QG-09 | C-11 | Prompt body scoring step shows composite row without formula or uses symbolic denominators |
| QG-10 | C-12/C-13 | Anti-conflation prohibition is global-only (no gate-specific sentences) |
| QG-11 | C-14 | Gate-independence requirement stated in preamble with no per-instance record in scoring step |
| QG-12 | C-15 | GATE 1 prohibition uses paraphrase ("does not pass") instead of naming PARTIAL and FAIL by rubric label |
| QG-13 | C-16 | Per-instance gate-independence requirement is a prose instruction with no corresponding template slot |

---

## Excellence Signals Log

### Round 1 — 2026-03-15

**Pattern 1: Formula embedding separates 80 from 68**

- **Signal**: V-01 and V-02 scored 80; V-03, V-04, V-05 scored 68. The only structural cause: V-01/V-02 stated the composite formula explicitly in the prompt body's scoring step. V-03/V-04/V-05 showed a COMPOSITE matrix row without stating the formula, making the prompt body operator-dependent.
- **Evidence**: V-02 body: "Composite formula: (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)". V-03/V-04/V-05: matrix template with COMPOSITE row, formula absent.
- **Mechanism**: Self-containment failure. A prompt body that requires the operator to carry scoring rules from external context cannot be called a self-contained skill artifact for scoring purposes.
- **Principle**: All numeric rules (formulas, denominators) must be embedded inline in the step that uses them. A matrix template is scaffolding, not instruction. → **C-11**

**Pattern 2: Anti-conflation guard prevents the most common C-02 failure mode**

- **Signal**: Variations that labeled dual gate sections structurally but omitted an explicit prohibition sentence could still satisfy the structural form while leaving the conflation path open. The anti-conflation guard forces the prohibition to be stated, not inferred.
- **Mechanism**: Structure suggests separation; prohibition enforces it. A reader who sees two labeled sections may still evaluate them as a single composite check unless told explicitly not to.
- **Principle**: Structural separation and explicit prohibition are independent requirements. One does not imply the other. → **C-12**

### Round 3 — 2026-03-15

**Pattern 3: Per-gate prohibition closes contamination paths that a global prohibition leaves open**

- **Signal**: A single "Do not conflate" sentence covering both gates does not name either gate's specific contamination path. GATE 1's path (high composite excusing an essential fail) and GATE 2's path (scoring GATE 2 before GATE 1 resolves) are structurally different failure modes. A global prohibition can be read as applying generally without blocking either path specifically.
- **Mechanism**: Each gate's contamination path has a distinct direction. GATE 1's prohibition must name what cannot substitute for essential passage; GATE 2's prohibition must name the sequential dependency. A single sentence cannot name both directions without becoming a paraphrase.
- **Principle**: Prohibition sentences must be gate-specific to close gate-specific paths. → **C-13**

**Pattern 4: Per-instance gate record converts a preamble promise into post-hoc evidence**

- **Signal**: A preamble prohibition states intent. A per-scorecard record states compliance. The distinction is temporal: the preamble is read before evaluation; the record is produced during evaluation. A prompt body that only prohibits conflation in the preamble has no mechanism to detect whether the prohibition was honored in any given scoring instance.
- **Mechanism**: Compliance detectability. A preamble instruction can be "followed" without leaving any artifact. A per-scorecard field cannot be omitted silently — its absence is visible in the output.
- **Principle**: Independence must be evidenced per instance, not promised per session. → **C-14**

### Round 4 — 2026-03-16

**Pattern 5: Single-word verdict precision closes the partial-escape path (V-01)**

- **Signal**: The R3 baseline scored C-13 PARTIAL because its GATE 1 prohibition named "essential fail" only. V-01 added "PARTIAL or FAIL," closing the path where an essential criterion at PARTIAL — not fully failing — would not trigger GATE 1 blockage. One word is not cosmetic: PARTIAL is a distinct rubric verdict state that a conflating scorer can treat as "close enough to PASS" if it is not explicitly named in the prohibition.
- **Evidence**: R3 baseline prohibition: "a passing composite does not excuse an essential fail." V-01 prohibition: "a passing composite does not excuse an essential criterion that is PARTIAL or FAIL." The added word closes a rubric-defined state that was previously unaddressed.
- **Mechanism**: Paraphrase vocabulary leaves verdict states unnamed. Rubric-label vocabulary closes each verdict state by the name the rubric uses for it. A scorer who sees "does not fail" may interpret "PARTIAL" as not covered; a scorer who sees "PARTIAL or FAIL" cannot.
- **Principle**: Prohibition sentences that use the rubric's exact verdict labels (PASS / PARTIAL / FAIL) are complete; prohibition sentences that use paraphrases are vulnerable to verdict-state slippage. → **C-15**

**Pattern 6: Template slot converts per-instance instruction into detectable artifact (V-02)**

- **Signal**: V-01 satisfied C-13 (gate-specific prohibition language) but not C-14 — the gate-independence requirement remained a preamble instruction with no structural presence in the scorecard output. V-02 added a required `Gate-independence record:` labeled field inside the scorecard template. The key property: a scorecard produced from the V-02 template with the field unfilled has a visible blank; a scorecard produced from V-01 with the preamble instruction "followed but undocumented" leaves no trace.
- **Evidence**: V-02 scorecard template includes `Gate-independence record:` as a named field at the same structural level as `Composite:`. V-01 scorecard template has no corresponding field — the gate-independence requirement is in the preamble only.
- **Mechanism**: Asymmetric accountability. A preamble instruction fails silently (no output artifact marks non-compliance). A template slot fails audibly (the blank field is present and visible). The mechanism shifts burden from operator memory to template structure.
- **Principle**: Requirements embedded as template slots are structurally enforced; requirements stated as prose instructions are rhetorically enforced. Structural enforcement produces detectable artifacts; rhetorical enforcement does not. → **C-16**
```

---

**v4 changes summary:**

- **C-15** — Verdict vocabulary in gate prohibitions must use exact rubric labels (PARTIAL and FAIL named separately), not paraphrases. Derived from Signal 1 / V-01.
- **C-16** — Per-instance gate-independence record must be a structural template slot, not a prose instruction. Derived from Signal 2 / V-02.
- **Formula updated**: aspirational denominator `/6` → `/8`.
- **New failure modes**: QG-12 (paraphrase in prohibition vocabulary) and QG-13 (prose instruction with no template slot).
- **Excellence Signals Log**: Round 4 section appended with Patterns 5 and 6.

The C-12→C-13→C-14→C-15→C-16 ladder now reads: guard exists → guard is gate-specific → evidence is per-instance → vocabulary is exact → evidence is structural.
