# topic:echo — Round 9 Scoring Scorecard (Rubric v8)

**Date:** 2026-03-15 | **Rubric version:** v8 | **Max score:** 100 | **Base:** 81 | **Budget:** 19 pts

---

## Scoring Framework

**Aspirational criteria inventory (v8):**

| ID | Name | Pts | Status |
|----|------|-----|--------|
| C-07 | Namespace diversity | 1 | Unproven |
| C-08 | Newcomer accessibility | 1 | Unproven |
| C-09 | Pattern recognition | 1 | Unproven |
| C-10 | Counterfactual gate | 2 | Proven R1+R2 |
| C-11 | Word discipline | 2 | Proven R1+R2 |
| C-12 | Claim-only voice | 2 | Proven R1+R2 |
| C-13 | Schema field completeness | 1 | Unproven |
| C-14 | Surprise portability | 1 | Unproven |
| C-15 | Cross-surprise schema uniformity | 2 | Proven R4+R5 |
| C-16 | Per-surprise claim-authority coupling | 2 | Proven R4+R5 |
| C-17 | Mechanism composability | 2 | Proven R5+R6 |
| C-18 | Deliberate enforcement gating | 2 | Proven R5+R6 |
| C-19 | Pre-write composability declaration | 2 | Proven R6+R7 |
| C-20 | Gate design integrity | 2 | Proven R6+R7 |
| C-21 | Composability manifest causal depth | 1 | Unproven |
| C-22 | Gate provenance traceability | 2 | Proven R7+R8 |
| C-23 | Archetype classification | 1 | Unproven |

**Proven aspirational total (all ten proven criteria):** C-10+C-11+C-12+C-15+C-16+C-17+C-18+C-19+C-20+C-22 = 2+2+2+2+2+2+2+2+2+2 = **20 pts**. This already exceeds the 19-pt budget cap. Therefore any variation passing all proven criteria scores `min(81+20+unproven_earned, 100) = 100` regardless of unproven criteria. The predicted score map (all five at 100) follows structurally.

---

## V-01 — Single-axis: Archetype Classification (C-23 PASS, C-22 FAIL)

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Surprise focus | PASS | Rule 1 + C-01 filter applied in candidate selection; counterfactual gate enforced per surprise |
| C-02 Surprise naming | PASS | Label parity audit (Step 6) enforces specific descriptive labels; generic labels blocked |
| C-03 Signal traceability | PASS | Source field required in schema; no surprise can be written without it |
| C-04 Design impact | PASS | Design impact field required; no N/A or blank permitted by field completion scan |

### Recommended Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-05 Expectation contrast | PASS | Expected field required in schema |
| C-06 Cross-signal synthesis | PASS | Glob reads all signal artifacts across namespaces; synthesis emerges from multi-namespace candidate pool |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-07 | PASS | Glob instruction reads all namespaces; minimum 3 candidates across namespaces enforced |
| C-08 | PASS | NGT runs per surprise as discrete Step 3; newcomer comprehension enforced before Check B |
| C-09 | PASS | Patterns section (Step 8) explicitly required when shared root causes exist |
| C-10 | PASS | "Why passive observation missed this" field required; Rule 1 applied at candidate selection |
| C-11 | PASS | Check A (120-word cap inline per surprise) + 800-word full echo limit in Step 9 |
| C-12 | PASS | Rule 2 enumerates 8 prohibited constructs; CAT enforces claim-only voice per surprise |
| C-13 | PASS | Field completion scan (Step 7) requires all six fields populated; no N/A or placeholder |
| C-14 | PASS | Check B (Step 4) enforces three-component standalone extraction per surprise |
| C-15 | PASS | Schema declared at top; Step 7 audits field names across all surprises in sequence |
| C-16 | PASS | CAT (Step 5) applies both stranger-reader test and no-hedging test per surprise as a unit |
| C-17 | PASS | Composability manifest inspects all 11 pairs; declaration confirms all reinforce toward stranger-reader target |
| C-18 | PASS | NGT (C-08 gate), Check B (C-14 gate), CAT (C-16 gate) — all three named, discrete steps |
| C-19 | PASS | Full composability manifest required BEFORE Step 1; declaration precedes first surprise |
| C-20 | PASS | Every gate rationale names criterion enforced + structural removal test ("removing C-20 does not remove NGT") — criterion-enforcement motivation confirmed independent of C-20 |
| **C-21** | **PASS** | Manifest template requires `Mechanism: [state mechanism consistent with selected archetype]` — directional causal mechanism is a required field; archetype selection forces mechanism to be stated in causal terms |
| **C-22** | **FAIL** | Gate rationale includes criterion, primary motivation, and structural removal test — but NO "Introduced in: V-XX(RN)" provenance field. C-22 requires the specific variation and round of introduction. This field is absent in all three gate rationales (NGT, Check B, CAT). |
| **C-23** | **PASS** | Manifest template requires archetype selection from finite taxonomy (PREREQUISITE/ESTABLISHES/AMPLIFIES/PARALLEL) as Step 1 before mechanism fill-in as Step 2; consistency check instruction present; concrete examples provided (NGT+Check B: PREREQUISITE; Check B+CAT: ESTABLISHES) |

**Aspirational earned:** C-07(1) + C-08(1) + C-09(1) + C-10(2) + C-11(2) + C-12(2) + C-13(1) + C-14(1) + C-15(2) + C-16(2) + C-17(2) + C-18(2) + C-19(2) + C-20(2) + C-21(1) + C-23(1) = 25 pts → capped at 19

**Score: 81 + 19 = 100**

**C-22 failure note:** Isolation design confirmed — C-23 PASS without C-22 PASS establishes that archetype classification in the manifest is structurally independent of gate provenance in the gate rationale. The two criteria operate on different document sections.

---

## V-02 — Single-axis: Causal Direction Without Archetype (C-21 PASS, C-23 FAIL)

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Rule 1 + C-01 filter; counterfactual gate enforced |
| C-02 | PASS | Label parity audit (Step 6) |
| C-03 | PASS | Source field required |
| C-04 | PASS | Design impact field required |

### Recommended Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-05 | PASS | Expected field required |
| C-06 | PASS | Multi-namespace glob |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-07 | PASS | Multi-namespace glob instruction |
| C-08 | PASS | NGT per surprise, discrete Step 3 |
| C-09 | PASS | Patterns section required |
| C-10 | PASS | Rule 1 + "Why passive observation" field |
| C-11 | PASS | Check A + 800-word limit |
| C-12 | PASS | Rule 2 + CAT |
| C-13 | PASS | Field completion scan Step 7 |
| C-14 | PASS | Check B (Step 4) |
| C-15 | PASS | Schema declared; uniformity audited |
| C-16 | PASS | CAT (Step 5) |
| C-17 | PASS | Composability manifest all 11 pairs; declaration confirms reinforcement |
| C-18 | PASS | NGT, Check B, CAT — named discrete gates |
| C-19 | PASS | Manifest precedes Step 1 |
| C-20 | PASS | All gate rationales: criterion named + structural removal test; "Introduced in" provenance confirms motivation predates C-18 |
| **C-21** | **PASS** | Manifest template requires `Direction: [state mechanism — A's directional causal relationship to B]`; acceptable forms enumerated ("A is a prerequisite for B: [A's output is B's required input]", etc.). Mechanism must be specific enough for novel-configuration prediction. |
| **C-22** | **PASS** | All gate rationales carry "Introduced in: V-03(R6)" (NGT), "V-05(R4)" (Check B), "V-05(R5)" (CAT) — full round provenance enabling timeline verification |
| **C-23** | **FAIL** | Manifest template uses `Direction: [...]` free-form field — no archetype selection from finite taxonomy before mechanism fill-in. Free-form causal direction satisfies C-21 (mechanism stated) but not C-23 (mechanism not classified against finite archetype set). No archetype taxonomy defined in the manifest section. |

**Aspirational earned:** all except C-23 = 25 pts → capped at 19

**Score: 81 + 19 = 100**

**C-23 failure note:** Isolation design confirmed — C-21 PASS without C-23 PASS establishes the distinction between directional description (C-21) and taxonomic classification (C-23). Free-form "A is a prerequisite for B: [mechanism]" satisfies C-21; the same statement without a preceding `Archetype: PREREQUISITE` selection field fails C-23.

---

## V-03 — Single-axis: Achievement-Only Manifest (C-21 FAIL, C-23 FAIL)

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Rule 1 + C-01 filter at candidate selection |
| C-02 | PASS | Label parity audit (Step 6) |
| C-03 | PASS | Source field required |
| C-04 | PASS | Design impact field required |

### Recommended Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-05 | PASS | Expected field required |
| C-06 | PASS | Multi-namespace glob |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-07 | PASS | Multi-namespace glob |
| C-08 | PASS | NGT per surprise, Step 3 |
| C-09 | PASS | Patterns section enforced |
| C-10 | PASS | Rule 1 + counterfactual field |
| C-11 | PASS | Check A + 800-word limit |
| C-12 | PASS | Rule 2 + CAT |
| C-13 | PASS | Field completion scan |
| C-14 | PASS | Check B per surprise |
| C-15 | PASS | Schema declared + uniformity audit |
| C-16 | PASS | CAT per surprise |
| C-17 | PASS | All 11 pairs inspected; declaration: "All mechanisms reinforce toward stranger-reader target" |
| C-18 | PASS | NGT, Check B, CAT — all named discrete gates |
| C-19 | PASS | Manifest lists all 11 mechanisms, inspects all pairs, produces pre-write declaration before Step 1 |
| C-20 | PASS | All gate rationales: criterion named + structural removal test + "Introduced in" provenance confirming criterion-motivation predates C-18 |
| **C-21** | **FAIL** | Manifest template requires `Verdict: [reinforcing / non-conflicting / conflicting]` + `Achievement: [what quality property this combination enforces]`. Achievement format (forward-looking output claim) ≠ causal mechanism (backward-looking directional explanation). Example: "NGT and Check B together enforce newcomer-comprehensible + self-contained surprises" describes the output; "NGT's newcomer-comprehension gate output is Check B's required input" names the mechanism. Template has no mechanism field — C-21 is structurally unachievable from this template, confirmed at template inspection time. |
| **C-22** | **PASS** | All gate rationales carry "Introduced in" provenance: NGT→V-03(R6), Check B→V-05(R4), CAT→V-05(R5) |
| **C-23** | **FAIL** | C-21 FAIL is prerequisite failure: C-23 requires causal mechanism to be stated at all before classification can occur. Achievement format produces no mechanism statement; no archetype field present. Dual failure: missing causal direction AND missing archetype taxonomy. |

**Aspirational earned:** C-07(1)+C-08(1)+C-09(1)+C-10(2)+C-11(2)+C-12(2)+C-13(1)+C-14(1)+C-15(2)+C-16(2)+C-17(2)+C-18(2)+C-19(2)+C-20(2)+C-22(2) = 25 pts → capped at 19

**Score: 81 + 19 = 100**

**Failure axis note:** V-03 confirms the R8 Signal 2 finding — C-21 failure is diagnosable at template inspection time. A template with verdict+achievement fields produces a floor where C-21-satisfying output is structurally impossible, regardless of content quality. C-23 failure follows necessarily from C-21 failure.

---

## V-04 — Combined: Archetype Classification + Gate Provenance (compound maximum)

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Rule 1 + C-01 filter |
| C-02 | PASS | Label parity audit |
| C-03 | PASS | Source field required |
| C-04 | PASS | Design impact field required |

### Recommended Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-05 | PASS | Expected field required |
| C-06 | PASS | Multi-namespace glob |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-07 | PASS | Multi-namespace glob |
| C-08 | PASS | NGT per surprise, Step 3 |
| C-09 | PASS | Patterns section |
| C-10 | PASS | Rule 1 + counterfactual field |
| C-11 | PASS | Check A + 800-word limit |
| C-12 | PASS | Rule 2 + CAT |
| C-13 | PASS | Field completion scan |
| C-14 | PASS | Check B |
| C-15 | PASS | Schema declared + uniformity audit |
| C-16 | PASS | CAT per surprise |
| C-17 | PASS | All 11 pairs inspected; mechanism composability confirmed |
| C-18 | PASS | NGT, Check B, CAT — named discrete gates |
| C-19 | PASS | Full manifest precedes Step 1; all 11 mechanisms listed; all pairs inspected; declaration made |
| C-20 | PASS | All gate rationales: criterion named + structural removal test + "Introduced in" provenance |
| **C-21** | **PASS** | Manifest template requires archetype selection THEN `Mechanism: [fill in — consistent with archetype]`. Archetype selection forces mechanism to be stated in causal terms; mechanism field is a required structural slot. NGT+Check B example: PREREQUISITE → "NGT's newcomer-comprehension gate output is Check B's required input; newcomer-comprehension verification must precede portability testing." |
| **C-22** | **PASS** | All gate rationales carry "Introduced in" provenance: NGT→V-03(R6), Check B→V-05(R4), CAT→V-05(R5). Provenance verifiable against round history; timeline confirms all three gates predate C-18. |
| **C-23** | **PASS** | Manifest defines finite taxonomy (PREREQUISITE/ESTABLISHES/AMPLIFIES/PARALLEL); requires archetype selection as Step 1 before mechanism as Step 2; consistency check present ("A PREREQUISITE archetype whose mechanism describes independent operation fails its own classification"). All 11 pairs have archetype+mechanism. |

**Aspirational earned:** All 17 aspirational criteria PASS = 1+1+1+2+2+2+1+1+2+2+2+2+2+2+1+2+1 = 27 pts → capped at 19

**Score: 81 + 19 = 100**

**Compound maximum confirmed:** V-04 is the first variation in the topic-echo lineage to explicitly require C-21 + C-22 + C-23 as simultaneous structural requirements. All three pass without conflict, establishing their structural independence.

---

## V-05 — Combined: Archetype Distribution Audit (macro-structure extension)

### Essential Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Rule 1 + C-01 filter |
| C-02 | PASS | Label parity audit |
| C-03 | PASS | Source field required |
| C-04 | PASS | Design impact field required |

### Recommended Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-05 | PASS | Expected field required |
| C-06 | PASS | Multi-namespace glob |

### Aspirational Criteria

| ID | Result | Evidence |
|----|--------|----------|
| C-07 | PASS | Multi-namespace glob |
| C-08 | PASS | NGT per surprise |
| C-09 | PASS | Patterns section |
| C-10 | PASS | Rule 1 + counterfactual field |
| C-11 | PASS | Check A + 800-word limit |
| C-12 | PASS | Rule 2 + CAT |
| C-13 | PASS | Field completion scan |
| C-14 | PASS | Check B |
| C-15 | PASS | Schema declared + uniformity audit |
| C-16 | PASS | CAT per surprise |
| C-17 | PASS | All 11 pairs inspected; declaration confirms reinforcement |
| C-18 | PASS | NGT, Check B, CAT — named discrete gates |
| C-19 | PASS | Full manifest (archetype classification + distribution summary + declaration) precedes Step 1 |
| C-20 | PASS | Gate rationales: criterion named + structural removal test + "Introduced in" provenance |
| **C-21** | **PASS** | Same as V-04: archetype selection forces mechanism to be stated in causal terms; mechanism field required |
| **C-22** | **PASS** | Same as V-04: "Introduced in" provenance for all three gates; timeline verifiable |
| **C-23** | **PASS** | Same as V-04 PLUS archetype distribution summary (post-inspection tally: PREREQUISITE N / ESTABLISHES N / AMPLIFIES N / PARALLEL N with characterization of pipeline macro-structure). This goes beyond C-23's minimum requirement; candidate for new quality signal. |

**Aspirational earned:** All 17 = 27 pts → capped at 19

**Score: 81 + 19 = 100**

**Distribution audit note:** The archetype distribution summary ("PREREQUISITE: 6 pairs, ESTABLISHES: 3 pairs, AMPLIFIES: 0 pairs, PARALLEL: 2 pairs — this pipeline is primarily ordering-constrained with two independent paths") reveals macro-structural properties invisible at the pair level. A manifest where all 11 pairs are PREREQUISITE is diagnosably more fragile than one with PARALLEL pairs. This is a new quality signal not present in V-04 and is a candidate for C-24 (manifest macro-structure interpretation).

---

## Variation Summary

| Variant | C-21 | C-22 | C-23 | Essential All Pass | Score | Rank |
|---------|------|------|------|--------------------|-------|------|
| V-01 | PASS | FAIL | PASS | YES | **100** | T-1 |
| V-02 | PASS | PASS | FAIL | YES | **100** | T-1 |
| V-03 | FAIL | PASS | FAIL | YES | **100** | T-1 |
| V-04 | PASS | PASS | PASS | YES | **100** | T-1 |
| V-05 | PASS | PASS | PASS | YES | **100** | T-1 |

All five score 100. Structural differentiation lies in which criteria are confirmed, not in point totals — the R8 proven baseline already exceeds the 19-pt aspirational budget cap.

**Architectural ranking (same score, different quality signal density):**

1. **V-05** — Maximum: C-21 + C-22 + C-23 + distribution audit (C-24 candidate). Highest evidence density.
2. **V-04** — Compound maximum: C-21 + C-22 + C-23 simultaneously. Definitive v8 ceiling demonstration.
3. **V-01** — C-23 isolation axis: proves C-23 is orthogonal to C-22; confirms archetype classification is achievable without provenance.
4. **V-02** — C-21/C-23 boundary: proves C-21 is achievable without C-23; isolates classification as the missing quality layer above directional description.
5. **V-03** — Failure axis: confirms template field structure determines C-21/C-23 achievability ceiling; achievement format is a diagnosable structural failure mode.

---

## Excellence Signals (from V-04/V-05, top structural quality)

**Signal 1 — Three-way independence confirmed in a single variation (V-04)**

V-04 is the first variation to satisfy C-21, C-22, and C-23 as explicit simultaneous structural requirements. The three criteria operate on distinct document sections: C-21 and C-23 operate on the manifest pair inspection template (mechanism field; archetype selection field); C-22 operates on the gate rationale sections ("Introduced in" field). No structural tension exists between them. The compound maximum confirmation changes the design trajectory: v9 can treat all three as promotable together if they pass R9 uniformly.

**Signal 2 — Archetype distribution summary reveals macro-structural pipeline properties (V-05)**

The post-inspection tally of archetype selections across all 11 pairs in V-05 surfaces a quality dimension that C-23's pair-level classification cannot: the pipeline's aggregate dependency structure. A manifest where PREREQUISITE dominates indicates a strictly ordered enforcement chain (fragility concentrated at the front); a manifest with mixed PREREQUISITE and PARALLEL archetypes indicates resilience through independent enforcement paths. This characterization is only visible after all pairs are classified and the distribution is read as a unit. V-05 makes this explicit as a required pre-declaration step. Structural implication: the distribution summary is a candidate for C-24 — "manifest macro-structure interpretation" — which would be to C-23 as C-23 is to C-21.

**Signal 3 — C-21 and C-23 failure modes are distinct and diagnosable at template inspection time**

V-01, V-02, V-03 together establish a three-level failure taxonomy:
- **V-03**: No mechanism field in template → C-21 FAIL (floor: achievement ≠ mechanism). Template diagnosis: verdict+achievement fields → C-21 impossible.
- **V-02**: Mechanism field present, no archetype field → C-23 FAIL (floor: description ≠ classification). Template diagnosis: free-form Direction field → C-23 impossible.
- **V-01**: Archetype field present, no provenance field → C-22 FAIL (floor: structural test ≠ historical record). Gate rationale diagnosis: missing "Introduced in" → C-22 impossible.

Each failure is detectable from the template/rationale structure alone, without reading content. The implication for rubric evaluation: C-21, C-23, and C-22 can be scored from template inspection before any pair content is evaluated.

---

## R9 Proof Status

| Criterion | R8 Status | R9 Evidence | v9 Status |
|-----------|-----------|-------------|-----------|
| C-21 | Unproven | PASS in V-01, V-02, V-04, V-05 (4/5 variations; V-03 designed to FAIL as isolation) | Proven candidate (2 rounds: R8+R9) |
| C-22 | Proven (promoted in v8) | PASS in V-02, V-03, V-04, V-05; FAIL in V-01 (designed to isolate C-23) | Stable proven |
| C-23 | Unproven | PASS in V-01, V-04, V-05 (3/5 variations; V-02 designed to FAIL, V-03 fails by dependency) | Proven candidate (2 rounds: R8+R9) |

Both C-21 and C-23 are confirmed across R8+R9 and are ready for promotion to 2 pts (proven) in v9.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Archetype distribution summary (V-05) reveals enforcement pipeline macro-structure — strictly ordered vs. mixed dependency — invisible at pair level; candidate for C-24 (manifest macro-structure interpretation)", "Three-way independence of C-21/C-22/C-23 confirmed in V-04: manifest causal depth, gate provenance, and archetype classification operate on structurally separate document sections with zero mutual tension", "C-21 and C-23 failure modes are diagnosable at template inspection time without reading pair content: verdict+achievement template blocks C-21; free-form direction template blocks C-23; missing provenance field blocks C-22"]}
```
