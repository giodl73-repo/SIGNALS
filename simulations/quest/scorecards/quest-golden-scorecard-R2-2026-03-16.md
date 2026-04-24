Scorecard written to `simulations/quest/scorecards/quest-golden-scorecard-R2-2026-03-16.md`.

---

## Round 2 Summary

**Rank:** V-05 (100) > V-02 (98) > V-04 (96) > V-03 (93) > V-01 (91)

**Major shift from R1:** All five variations passed all essential criteria. The R1 universal failure on C-02/C-03 is fully resolved — the output-contract mechanism works.

**Residual gap:** C-12 (structural contrast enforcement) remains the dividing line. Variations without a delta block (V-01, V-03, V-04) still fail it. V-02 and V-05 pass via TOP HAD / SECOND LACKED fields.

**Excellence signal:** V-05 uniquely adds a `TOP HAD / INERTIA LACKED` field in the delta block — not just a prose reference to inertia, but a structural slot that requires the extractor to state what inertia lacked separately from what the runner-up lacked. This prevents crediting inertia-present patterns as loop discoveries. Proposed as **C-14 (aspirational)**.

**Convergence status:** Trial convergence YES. Quest convergence NO (R2 signal not none; R1 also not none). **→ Round 3 needed.**

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inertia-anchored delta field: a dedicated INERTIA LACKED slot in the QU2 delta block validates the signal against unconstrained generation separately from the runner-up contrast, preventing loop credit for patterns inertia already produces"]}
```
elds specified. |
| C-04 QU2 precedes QU3 | essential | PASS | PHASE 3 orders Step QU2 then Step QU3 (conditional on QU2 signal not none); inherited from V-03-R1 lifecycle structure |
| C-05 Rubric present at loop start | essential | PASS | PHASE 0: "Glob simulations/quest/rubrics/... Load latest version. If no rubric exists: invoke quest-rubric. Do not proceed until confirmed." Gate explicit. |
| C-06 Per-round iteration record | recommended | PASS | Round Log table with all four fields: Round, Variations, Top composite, QU2 signal, Criterion added |
| C-07 Excellence signal isolation | recommended | PARTIAL | "Name the observable output difference: what the winner had that the runner-up lacked. The signal is a contrast, not a property list." Instructional anti-pattern prohibition present, but no structural mechanism (no delta block, no contrast column) to enforce it. |
| C-08 Criterion proposal completeness | recommended | PASS | Step QU3 lists Text, Tier, and Pass condition (LOCATION + OBSERVABLE + STANDARD) as required fields |
| C-09 "What made it golden" narrative | aspirational | PASS | GOLDEN OUTPUT: "Section 'What Made It Golden' immediately after the body: each structural mechanism the loop discovered, the round it was found, and the output gap it closed. Minimum 2 mechanisms with explicit round citations." |
| C-10 Persistent gap identification | aspirational | PASS | GOLDEN OUTPUT: "Ablated criteria: list any criteria with zero activations across all rounds with a suggested probe. If none: 'No ablated criteria.'" Explicit requirement, explicit null case. |
| C-11 Structural termination isolation | aspirational | PASS | PHASE 4 is a named, dedicated phase. Entry condition requires PHASE 3 completion; sole content is dual-gate evaluation. Not merged with iteration body. |
| C-12 Contrast-enforced signal isolation | aspirational | FAIL | No structural mechanism in QU2 step. Instructional prohibition ("not a property list") present but no delta block, no contrast column, no paired field. Model can still fill extraction with description that sounds contrastive. |
| C-13 Rationale-grounded sequencing | aspirational | FAIL | No "because" clause accompanying the QU2->QU3 ordering constraint. Step QU3 is conditional ("only if QU2 signal is not none") but the reason for that ordering is not stated. |

**Essential score:** 5/5 -> x60 = **60**
**Recommended score:** 2.5/3 -> x30 = **25**
**Aspirational score:** 3/5 -> x10 = **6**
**Composite: 91** | all_essential_pass: YES

---

### V-02 — Contrast-Delta Notation

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | PHASE 4 two-condition table inherited from V-03-R1; "If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1." |
| C-02 Golden prompt as full skill body | essential | PASS | GOLDEN OUTPUT: "Write the full converged prompt body verbatim." "Full" + "verbatim" explicit; path specified. Weaker exclusion language than V-01 (no anti-patterns listed) but "verbatim" directly addresses R1 gap. |
| C-03 Final rubric as standalone artifact | essential | PASS | "Final rubric -- All criteria, formula, denominator, golden threshold, version history. Standalone file." Explicit standalone requirement; required fields listed. |
| C-04 QU2 precedes QU3 | essential | PASS | PHASE 3: Step QU2 Delta Extraction precedes Step QU3 Criterion Proposal; QU3 conditional on SIGNAL NAME not none |
| C-05 Rubric present at loop start | essential | PASS | PHASE 0: "If no rubric exists: invoke quest-rubric before proceeding." Gate explicit. |
| C-06 Per-round iteration record | recommended | PASS | Round Log with Round, Variations, Top composite, QU2 signal, Criterion added |
| C-07 Excellence signal isolation | recommended | PASS | Delta block rules: "TOP HAD and SECOND LACKED must describe the same element from opposite sides. If both variations had the element, it is not the signal." Structural prohibition on shared-property filling. |
| C-08 Criterion proposal completeness | recommended | PASS | QU3: "Text, Tier, Pass: LOCATION, Pass: OBSERVABLE, Pass: STANDARD" -- three fields required, pass condition decomposed into three sub-fields |
| C-09 "What made it golden" narrative | aspirational | PASS | "Followed by 'What Made It Golden': >= 2 mechanism descriptions, each naming the round it was found and the output gap it closed." |
| C-10 Persistent gap identification | aspirational | PASS | "Ablated criteria: criteria with zero activations and a suggested probe for each. If none: 'No ablated criteria.'" |
| C-11 Structural termination isolation | aspirational | PASS | PHASE 4 named and distinct from PHASE 3 (analysis); sole content is dual-gate evaluation table |
| C-12 Contrast-enforced signal isolation | aspirational | PASS | TOP HAD / SECOND LACKED paired fields structurally require gap-stating. Rules: "Do not fill TOP HAD with a property both variations shared. The delta block must encode an absence in SECOND LACKED, not a shared quality." |
| C-13 Rationale-grounded sequencing | aspirational | FAIL | No "because" clause for QU2->QU3 ordering. The delta block is structural but does not explain why QU2 must precede QU3 in terms that make non-compliance self-evidently wrong. |

**Essential score:** 5/5 -> x60 = **60**
**Recommended score:** 3/3 -> x30 = **30**
**Aspirational score:** 4/5 -> x10 = **8**
**Composite: 98** | all_essential_pass: YES

---

### V-03 — Rationale-Reinforced Sequencing

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | CONVERGENCE JUDGE is the dedicated final role. "Both conditions must be true before the loop exits -- trial convergence alone means... quest convergence alone means..." Both gates named with rationale for why each is insufficient alone. |
| C-02 Golden prompt as full skill body | essential | PASS | Golden Output: "Full converged prompt body verbatim. Not a label. Not a summary. Every line of the deployable skill body -- if a reader cannot use this text directly to run the skill, it fails." Exclusion language present; failure criterion stated. |
| C-03 Final rubric as standalone artifact | essential | PASS | "Standalone file -- separate from the golden prompt, because the rubric is the theory of excellence and the golden prompt is the evidence; conflating them makes neither independently legible." Path and required fields specified. |
| C-04 QU2 precedes QU3 | essential | PASS | ANALYST role precedes CRITERION AUTHOR role. CRITERION AUTHOR: "QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial guess: it reflects the author's priors rather than what the loop actually measured." Structural sequence + rationale. |
| C-05 Rubric present at loop start | essential | PASS | RUBRIC KEEPER is first role: "The rubric must exist before scoring because variation rankings without a grounded objective function are not comparable..." Gate explicit with rationale. |
| C-06 Per-round iteration record | recommended | PASS | Per-Round Record table with Round, Variations, Top composite, Excellence signal, Criterion added |
| C-07 Excellence signal isolation | recommended | PARTIAL | ANALYST: "Name what the winner had that the runner-up lacked -- the contrast, not a description of the winner. Properties shared by both variations are not signals of excellence; only differences qualify." Strong instructional language but no structural mechanism (no delta block). |
| C-08 Criterion proposal completeness | recommended | PASS | CRITERION AUTHOR: "Text, Tier, Pass condition: LOCATION + OBSERVABLE + STANDARD" -- three fields present; "tier determines the criterion's weight in the composite formula" as rationale for tier assignment. |
| C-09 "What made it golden" narrative | aspirational | PASS | Golden Output: "each structural mechanism, the round it was found, the output gap it closed. Minimum 2 mechanisms with round citations." |
| C-10 Persistent gap identification | aspirational | PASS | "Ablated criteria: criteria with zero activations and a suggested probe for each. If none: 'No ablated criteria.'" |
| C-11 Structural termination isolation | aspirational | PASS | CONVERGENCE JUDGE is a named, dedicated role distinct from all iteration roles (VARIATOR, SCORER, ANALYST, CRITERION AUTHOR). Its only mandate is dual-gate evaluation. |
| C-12 Contrast-enforced signal isolation | aspirational | FAIL | ANALYST role uses instructional language only ("the contrast, not a description"). No structural field (no delta block, no contrast column) that enforces gap-stating mechanically. |
| C-13 Rationale-grounded sequencing | aspirational | PASS | CRITERION AUTHOR: "QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial guess." RUBRIC KEEPER: "...because variation rankings without a grounded objective function are not comparable." CONVERGENCE JUDGE: rationale for both conditions. |

**Essential score:** 5/5 -> x60 = **60**
**Recommended score:** 2.5/3 -> x30 = **25**
**Aspirational score:** 4/5 -> x10 = **8**
**Composite: 93** | all_essential_pass: YES

---

### V-04 — Combination: V-05-R1 + Output Contract

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | PHASE 4 two-condition table; "If both YES: proceed to GOLDEN OUTPUT. If either NO: append round log and return to PHASE 1." |
| C-02 Golden prompt as full skill body | essential | PASS | Artifact 1: "Full converged prompt body verbatim -- the complete runnable text, not a summary, not a label, not 'see V-05.' Every line that belongs in the deployed skill body." Exclusion patterns listed; failure criterion stated. |
| C-03 Final rubric as standalone artifact | essential | PASS | Artifact 2: "Standalone file -- separate from Artifact 1; not embedded inside the golden prompt file." Required contents listed; path specified. |
| C-04 QU2 precedes QU3 | essential | PASS | PHASE 3: "Step QU2 -- Excellence Signal Isolation" precedes "Step QU3 -- Criterion Proposal (only if QU2 is not none)." Sequential named steps. |
| C-05 Rubric present at loop start | essential | PASS | PHASE 0: "Load rubric. Glob ... If none: invoke quest-rubric. The rubric defines what 'beating inertia' means in measurable terms." |
| C-06 Per-round iteration record | recommended | PASS | Round Log: Round, Top, vs Inertia, QU2 signal, Criterion -- all fields including inertia comparison column |
| C-07 Excellence signal isolation | recommended | PASS | QU2 compares top vs. second AND top vs. inertia: "Name what the top variation had that neither the runner-up NOR the inertia baseline had." Inertia as fixed reference prevents crediting inertia-present patterns as discoveries. |
| C-08 Criterion proposal completeness | recommended | PASS | "Propose a rubric criterion: Text, Tier, Pass condition: LOCATION + OBSERVABLE + STANDARD" |
| C-09 "What made it golden" narrative | aspirational | PASS | "Section 'What Made It Golden' immediately after the body: each structural mechanism the loop discovered, the round it was found, and the specific inertia gap it closed. Minimum 2 mechanisms with round and inertia-gap citations." |
| C-10 Persistent gap identification | aspirational | PASS | "Ablated criteria: list criteria with zero activations across all rounds with a suggested probe for each. If none: 'No ablated criteria.'" |
| C-11 Structural termination isolation | aspirational | PASS | PHASE 4 is a named, dedicated phase; sole content is convergence table; separate from PHASE 3 analysis. |
| C-12 Contrast-enforced signal isolation | aspirational | FAIL | QU2 uses prose: "Name what the top variation had that neither the runner-up NOR the inertia baseline had." The inertia reference creates a named anchor but no structural delta block or named field that cannot be filled with description. |
| C-13 Rationale-grounded sequencing | aspirational | FAIL | No "because" clause for QU2->QU3 ordering. Inherited from V-05-R1 which also lacked C-13. |

**Essential score:** 5/5 -> x60 = **60**
**Recommended score:** 3/3 -> x30 = **30**
**Aspirational score:** 3/5 -> x10 = **6**
**Composite: 96** | all_essential_pass: YES

---

### V-05 — Full Synthesis

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | PHASE 4: "Both conditions must be true before the loop exits -- trial convergence alone means the rubric stopped evolving before all patterns were found; quest convergence alone means signals ran out before variations reached the essential bar." Two-condition table + rationale. |
| C-02 Golden prompt as full skill body | essential | PASS | Artifact 1: "Complete prompt body verbatim -- every line that belongs in the deployed skill body, not a summary, not 'see V-04,' not a compressed version. If a reader cannot run this text directly as a skill body, it fails this requirement." |
| C-03 Final rubric as standalone artifact | essential | PASS | Artifact 2: "Standalone file separate from Artifact 1 -- the rubric is the theory of excellence; the golden prompt is the evidence; they must be legible independently." Required contents listed; path specified. |
| C-04 QU2 precedes QU3 | essential | PASS | PHASE 3: "QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial guess, not a discovery..." Delta extraction step precedes criterion proposal; conditional execution enforced. |
| C-05 Rubric present at loop start | essential | PASS | PHASE 0: "The rubric must exist before scoring because variation rankings without a grounded objective function are not comparable -- 'beating inertia' is only measurable against explicit criteria." Gate + rationale. |
| C-06 Per-round iteration record | recommended | PASS | Round Log: Round, Top, vs Inertia, QU2 delta (signal), Criterion -- all four required fields |
| C-07 Excellence signal isolation | recommended | PASS | Delta block "TOP HAD / INERTIA LACKED" field: signal validated against inertia. "A variation that outscores the runner-up but produces nothing inertia lacked is not a discovery." |
| C-08 Criterion proposal completeness | recommended | PASS | QU3: "Text, Tier, Pass: LOCATION, Pass: OBSERVABLE, Pass: STANDARD" with tier rationale: "essential = output is wrong without it; recommended = better with it; aspirational = excellent" |
| C-09 "What made it golden" narrative | aspirational | PASS | "Section 'What Made It Golden'... for each structural mechanism state the round it was found and the specific inertia gap it closed. Minimum 2 mechanisms with round citations and inertia-gap descriptions." |
| C-10 Persistent gap identification | aspirational | PASS | "Ablated criteria: list criteria with zero activations across all rounds and a suggested probe for each. If none: 'No ablated criteria.'" |
| C-11 Structural termination isolation | aspirational | PASS | PHASE 4 named and separate; rationale for both conditions stated. Sole mandate is dual-gate evaluation. |
| C-12 Contrast-enforced signal isolation | aspirational | PASS | Delta block: "TOP HAD / SECOND LACKED: [element present in top, absent from second -- stated as an absence]" AND "TOP HAD / INERTIA LACKED: [element present in top, absent from inertia -- this is the discovery]." Dual structural fields; signal = none if INERTIA LACKED cannot be filled with a structural difference. |
| C-13 Rationale-grounded sequencing | aspirational | PASS | PHASE 3: "QU2 must precede QU3 because a criterion not grounded in an observed output gap is an editorial guess, not a discovery -- the loop's value is in what it measures, not what the author expected." Explanatory clause present; non-compliance self-evidently wrong. |

**Essential score:** 5/5 -> x60 = **60**
**Recommended score:** 3/3 -> x30 = **30**
**Aspirational score:** 5/5 -> x10 = **10**
**Composite: 100** | all_essential_pass: YES

---

### Summary Scoreboard

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Composite | All Essential |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|---------------|
| V-01 Output Contract | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | PASS | PASS | FAIL | FAIL | **91** | YES |
| V-02 Contrast-Delta | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | **98** | YES |
| V-03 Rationale-Reinforced | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | PASS | PASS | FAIL | PASS | **93** | YES |
| V-04 V05R1+Contract | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | FAIL | **96** | YES |
| **V-05 Full Synthesis** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **100** | **YES** |

**Rank:** V-05 (100) > V-02 (98) > V-04 (96) > V-03 (93) > V-01 (91)

**Trial convergence:** YES -- all 5 variations pass all 5 essential criteria; all composites >= 80.

---

### Excellence Signals -- V-05 vs V-02

**QU2 -- Delta Extraction:**

```
TOP VARIATION:           V-05
SECOND-RANKED:           V-02
TOP HAD / SECOND LACKED: Dedicated "TOP HAD / INERTIA LACKED" structural field in the delta
                         block -- validates the signal against unconstrained generation, not
                         just against the runner-up. V-02 has no "INERTIA LACKED" field; its
                         delta block only enforces gap vs. second-ranked.
TOP HAD / INERTIA LACKED: The dual-field delta block itself. Inertia baseline exists as prose
                         in V-04-R1 (V-05-R1) and V-04-R2, but neither made the inertia
                         contrast a structural slot in the extraction step.
SIGNAL NAME:             SIGNAL-R2: Inertia-anchored delta field
```

**QU3 -- Criterion Proposal:**

**C-14 -- Inertia-contrast slot in QU2 delta block**

- **Text:** The QU2 extraction structure must include a dedicated field for the inertia contrast -- separate from the runner-up contrast field -- so that a signal absent from the runner-up but present in unconstrained generation is identifiable and excluded from loop credit.
- **Tier:** aspirational (the loop converges without it, but signals are misattributed when absent; elevate to recommended if loops repeatedly credit inertia-present patterns as discoveries)
- **Pass:**
  LOCATION: QU2 extraction step.
  OBSERVABLE: a named field (e.g., "INERTIA LACKED" or "vs baseline") distinct from the runner-up contrast field, requiring the extractor to state what inertia lacked -- not just what the second-ranked lacked.
  STANDARD: two distinct contrast fields present (runner-up and inertia); a single field covering both references = PARTIAL; no inertia contrast field = FAIL.

---

### Convergence Check

| Condition | Status |
|-----------|--------|
| Trial convergence: all variations pass all essential criteria | YES |
| Quest convergence: R2 signal = none AND R1 signal = none | NO (R2: SIGNAL-R2; R1: not none) |
| **Dual convergence** | **NO -- proceed to Round 3** |

---

### Round Log

| Round | Variations | Top composite | QU2 signal | Criterion added |
|-------|------------|--------------|------------|-----------------|
| R-01 | V-01..V-05 | 78 (V-05) | Inertia baseline as primary contrast anchor | C-11, C-12, C-13 (rubric v2) |
| R-02 | V-01..V-05 | 100 (V-05) | SIGNAL-R2: Inertia-anchored delta field | C-14 (pending QU4) |

---

### Cross-Variation Gap Analysis

**C-12 is the single structural dividing line in R2.** V-01, V-03, V-04 each pass all recommended criteria and most aspirationals but fail C-12. The mechanism required for C-12 PASS is a structural field (delta block with gap-forcing rules), not instructional language. Any R3 variation that drops the delta block regresses.

**C-13 and C-12 are independent.** V-02: C-12 PASS, C-13 FAIL. V-03: C-12 FAIL, C-13 PASS. Neither mechanism substitutes for the other. V-05 passes both -- the mechanisms are additive.

**All essentials now pass universally.** The primary R1 gap (C-02, C-03 universally PARTIAL) is fully resolved across all R2 variations. Floor composite is 91; no variation falls below golden threshold.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["inertia-anchored delta field: a dedicated INERTIA LACKED slot in the QU2 delta block validates the signal against unconstrained generation separately from the runner-up contrast, preventing loop credit for patterns inertia already produces"]}
```
