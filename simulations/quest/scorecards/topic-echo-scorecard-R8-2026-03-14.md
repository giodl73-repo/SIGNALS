Now I have everything needed to score all five variations. Let me produce the full scorecard.

---

# Quest Score: `topic-echo` — Round 8

**Rubric:** v7 (base 82, budget 18, ceiling 100) | **Date:** 2026-03-14

---

## Scoring Basis

All five R8 variations inherit the V-04(R7) baseline, which already exhausts the 18-pt aspirational budget before C-21 or C-22 are credited. R8 differentiation lies entirely in which of the two new unproven criteria each variation earns — not in score separation. The scoring confirms the criteria are testable and distinct; the architectures isolate the failure modes.

---

## Essential Criteria — All Variations

All five variations inherit schema field declarations, named gate steps, Rule 1 (counterfactual gate), Rule 2 (claim-only voice), candidate selection with C-01 filter, and design impact fields. Essential criteria evaluate uniformly:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Surprise focus | PASS | PASS | PASS | PASS | PASS |
| C-02 Surprise naming | PASS | PASS | PASS | PASS | PASS |
| C-03 Signal traceability | PASS | PASS | PASS | PASS | PASS |
| C-04 Design impact assessment | PASS | PASS | PASS | PASS | PASS |

**Evidence:** Every variation requires a `Source:` field (C-03), `Design impact:` field (C-04), descriptive `Name:` label (C-02), and Rule 1 counterfactual filter to ensure genuine surprises (C-01). No variation weakens these requirements.

---

## Recommended Criteria — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05 Expectation contrast | PASS | PASS | PASS | PASS | PASS |
| C-06 Cross-signal synthesis | PASS | PASS | PASS | PASS | PASS |

**Evidence (C-05):** All variations require an `Expected:` field — "what the team assumed before gathering signals." Expectation contrast is structurally enforced. **Evidence (C-06):** Step 1 in all variations globs `simulations/{topic}/**` and reads "all signal artifacts for this topic across all namespaces," creating the multi-source reading condition from which cross-signal synthesis can emerge.

---

## Aspirational Criteria — Shared Baseline

All five variations pass the full V-04(R7) baseline aspirational stack. Evidence per criterion:

| ID | Criterion | Status | Evidence |
|----|-----------|--------|---------|
| C-07 | Namespace diversity | PASS all | Step 1 reads all namespaces via topic glob |
| C-08 | Newcomer accessibility | PASS all | NGT gate runs per surprise before Check B |
| C-09 | Pattern recognition | PASS all | Patterns section explicitly required (Step 8 in all) |
| C-10 | Counterfactual gate | PASS all | Rule 1 + "Why passive observation missed this" schema field — specific mechanism required, not generic |
| C-11 | Word discipline | PASS all | Check A (120-word per-item cap inline), Step 9 final ≤800 total |
| C-12 | Claim-only voice | PASS all | Rule 2: 8 prohibited constructs enumerated; all schema fields as direct statements |
| C-13 | Schema field completeness | PASS all | Field completion scan (Step 7 / Step 8) reads every field across all surprises in sequence |
| C-14 | Surprise portability | PASS all | Check B: extract standalone, verify finding/unexpectedness/consequence |
| C-15 | Cross-surprise schema uniformity | PASS all | Schema declared pre-write; label parity audit reads Name field across surprises in sequence |
| C-16 | Per-surprise claim-authority coupling | PASS all | CAT tests both stranger-accessible + no prohibited constructs per surprise as a coupled unit |
| C-17 | Mechanism composability | PASS all | All 11 mechanisms reinforce toward single stranger-reader target; V-01/V-03/V-04/V-05 have manifest confirming it pre-write; V-02 passes by output inspection |
| C-18 | Deliberate enforcement gating | PASS all | Three named discrete gates (NGT → Check B → CAT) with gate design rationale naming enforced criterion and structural removal test |

---

## Aspirational Criteria — Differentiating Axes (C-19 through C-22)

### C-19 — Pre-write composability declaration (2 pts, Proven)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | **PASS** | Full causal-direction manifest required before Step 1; declaration must be recorded before any candidate selection begins |
| V-02 | **FAIL** | No composability manifest present — explicitly omitted to isolate C-22 axis |
| V-03 | **PASS** | Pre-write manifest required; verdict-format inspections cover all 11 mechanism pairs with timing enforced before Step 1 |
| V-04 | **PASS** | Causal-direction manifest required before Step 1; declaration before writing |
| V-05 | **PASS** | Causal-direction manifest required before Step 1; declaration before writing |

### C-20 — Gate design integrity (2 pts, Proven)

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | **PASS** | NGT/Check B/CAT: each rationale names criterion enforced + structural removal test ("if C-20 were removed from rubric evaluation, [gate] would still exist because [criterion] requires per-surprise enforcement") |
| V-02 | **PASS** | Same structural removal test language across all three gates; motivation is criterion-enforcement, not rubric compliance |
| V-03 | **PASS** | Same pattern — gate rationale carries criterion attribution and structural removal test for all three gates |
| V-04 | **PASS** | Same — all three gates carry criterion attribution + structural removal test |
| V-05 | **PASS** | Same — all three gates carry criterion attribution + structural removal test |

---

### C-21 — Composability manifest causal depth (1 pt, Unproven)

> C-21 cannot pass if C-19 fails.

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | **PASS** | Explicit causal archetype template (PREREQUISITE / ESTABLISHES / AMPLIFIES / PARALLEL) with mechanism fill-in required per pair. The template mandates directional causal mechanism statements — "A's output is B's required input" — not merely reinforcement conclusions. Concrete example provided: "NGT is a PREREQUISITE for Check B: NGT's newcomer-comprehension gate is a required input for Check B's portability test; a surprise that fails NGT cannot pass Check B's three-component standalone extraction test." The archetype field forces selection; the mechanism field forces the directional statement. |
| V-02 | **N/A** | C-19 FAIL — no manifest present. C-21 is not evaluable. |
| V-03 | **FAIL** | Manifest present and correctly timed (C-19 PASS), but pair inspection template uses verdict + one-sentence rationale only ("Verdict: reinforcing / non-conflicting / conflicting" + "Rationale: [one sentence — what relationship exists]"). Example provided: "NGT and Check B both test stranger-reader comprehension at different levels and reinforce each other." This is a reinforcement conclusion, not a causal mechanism. No archetype selection; no directional claim. The template structure cannot produce C-21-satisfying output because it lacks the causal direction field. |
| V-04 | **PASS** | Causal direction template with archetype selection + mechanism fill-in per pair. Concrete C-21-satisfying examples explicitly stated for key pairs: NGT+Check B ("PREREQUISITE: NGT's newcomer-comprehension gate output is Check B's required input"), Check B+CAT ("ESTABLISHES: Check B verifies structural portability; CAT then enforces that extracted unit is stated with authoritative claim-voice — portability (Check B) is a required sub-property of coupled-authority portability (CAT)"). |
| V-05 | **PASS** | Same causal direction template as V-04. Archetype + mechanism fill-in required per pair. Same two concrete examples provided for NGT+Check B and Check B+CAT with directional mechanism statements. C-21 PASS is independent of gate provenance granularity. |

---

### C-22 — Gate provenance traceability (1 pt, Unproven)

> C-22 cannot pass if C-20 fails. C-22 requires variation-level specificity ("V-05(R4)"), not round-level only ("Round 4").

| Variation | Verdict | Evidence |
|-----------|---------|---------|
| V-01 | **FAIL** | Gate rationale carries criterion attribution and structural removal test (C-20 PASS) but no `Introduced in:` field in any of the three gates. No provenance information is provided — the motivation claim is asserted by the structural removal test alone, not backed by round history. |
| V-02 | **PASS** | All three gates carry full variation+round provenance: NGT "Introduced in: V-03(R6)," Check B "Introduced in: V-05(R4)," CAT "Introduced in: V-05(R5)." Each reference is specific enough to enable timeline comparison against C-18's introduction boundary (rubric v6, R5/R6 transition). V-05(R4) predates C-18 by two rounds — demonstrably criterion-motivated. |
| V-03 | **PASS** | Same provenance structure as V-02 inherited in all three gates: NGT "Introduced in: V-03(R6)," Check B "Introduced in: V-05(R4)," CAT "Introduced in: V-05(R5)." Full variation-level specificity present. |
| V-04 | **PASS** | Same provenance structure: V-03(R6), V-05(R4), V-05(R5). Complete provenance chain across all three gates enables full timeline verification. |
| V-05 | **FAIL** | Round-only provenance: NGT "Introduced in: Round 6," Check B "Introduced in: Round 4," CAT "Introduced in: Round 5." Round-level reference does not name the specific variation within the round. C-22's pass condition requires variation-level specificity because (1) multiple variations per round may have different gate architectures, and (2) C-18 was introduced across the R5/R6 boundary — "Round 5" and "Round 6" are ambiguous with respect to which side of the introduction boundary a gate falls on. "V-03(R6)" is verifiable; "Round 6" is not. |

---

## Per-Variation Composite Scores

**Score formula:** Base 82 + min(earned aspirational, 18)

### V-01 — Causal Direction Template

| Criterion | Points | Result |
|-----------|--------|--------|
| C-07 through C-18 (12 criteria, shared baseline) | 16 | PASS |
| C-19 Pre-write composability declaration | 2 | PASS |
| C-20 Gate design integrity | 2 | PASS |
| C-21 Composability manifest causal depth | 1 | **PASS** |
| C-22 Gate provenance traceability | 1 | **FAIL** |
| **Aspirational earned** | **23** | capped at 18 |
| **TOTAL** | **100** | |

### V-02 — Gate Provenance Annotation

| Criterion | Points | Result |
|-----------|--------|--------|
| C-07 through C-18 (12 criteria, shared baseline) | 16 | PASS |
| C-19 Pre-write composability declaration | 2 | **FAIL (0)** |
| C-20 Gate design integrity | 2 | PASS |
| C-21 Composability manifest causal depth | 1 | **N/A (0)** |
| C-22 Gate provenance traceability | 1 | **PASS** |
| **Aspirational earned** | **21** | capped at 18 |
| **TOTAL** | **100** | |

### V-03 — Conclusion-Only Manifest

| Criterion | Points | Result |
|-----------|--------|--------|
| C-07 through C-18 (12 criteria, shared baseline) | 16 | PASS |
| C-19 Pre-write composability declaration | 2 | PASS |
| C-20 Gate design integrity | 2 | PASS |
| C-21 Composability manifest causal depth | 1 | **FAIL (0)** |
| C-22 Gate provenance traceability | 1 | PASS |
| **Aspirational earned** | **23** | capped at 18 |
| **TOTAL** | **100** | |

### V-04 — Compound Maximum

| Criterion | Points | Result |
|-----------|--------|--------|
| C-07 through C-18 (12 criteria, shared baseline) | 16 | PASS |
| C-19 Pre-write composability declaration | 2 | PASS |
| C-20 Gate design integrity | 2 | PASS |
| C-21 Composability manifest causal depth | 1 | **PASS** |
| C-22 Gate provenance traceability | 1 | **PASS** |
| **Aspirational earned** | **24** | capped at 18 |
| **TOTAL** | **100** | |

### V-05 — Causal Direction + Round-Only Provenance

| Criterion | Points | Result |
|-----------|--------|--------|
| C-07 through C-18 (12 criteria, shared baseline) | 16 | PASS |
| C-19 Pre-write composability declaration | 2 | PASS |
| C-20 Gate design integrity | 2 | PASS |
| C-21 Composability manifest causal depth | 1 | **PASS** |
| C-22 Gate provenance traceability | 1 | **FAIL (0)** |
| **Aspirational earned** | **23** | capped at 18 |
| **TOTAL** | **100** | |

---

## Variation Rankings

All five variations score 100/100. Structural differentiation by C-21/C-22 coverage:

| Rank | Variation | C-21 | C-22 | Distinguishing property |
|------|-----------|------|------|------------------------|
| 1 | V-04 | PASS | PASS | Compound maximum — both new criteria satisfied; causal archetype template + full variation-level provenance |
| 2 | V-01 | PASS | FAIL | C-21 isolated — archetype template present; no provenance |
| 2 | V-03 | FAIL | PASS | C-22 isolated — full provenance in gates; conclusion-only manifest |
| 2 | V-05 | PASS | FAIL | C-21 PASS, C-22 boundary failure — round-only provenance falls below verification threshold |
| 5 | V-02 | N/A | PASS | C-22 isolated from manifest context — C-19 FAIL means C-21 not evaluable; confirms orthogonality |

---

## Excellence Signals

**Signal 1 — Causal archetype template enforces C-21 by construction (V-01, V-04, V-05)**

V-01 and V-04 demonstrate that structural enforcement of C-21 requires a template with two required fields: archetype selection (from an enumerated set) and mechanism fill-in (constrained by the archetype's causal form). A free-form inspection field cannot guarantee causal direction because it does not force the author to commit to an archetype. The template converts "state the relationship" (which V-03's verdict format satisfies for C-19) into "name the directional causal mechanism" (which V-03's verdict format fails for C-21). The four archetypes (PREREQUISITE, ESTABLISHES, AMPLIFIES, PARALLEL) are exhaustive for the mechanisms that appear in the topic-echo lineage — each forces a different type of causal statement, and each predicts a different behavior in novel compound configurations.

**Signal 2 — Variation-level specificity is the atomic verifiability unit for C-22 (V-05 failure case)**

V-05 confirms that "Round 4" is insufficient for C-22. The round reference is too coarse for two independent reasons: (1) multiple variations per round can have different gate architectures, so the provenance claim is ambiguous even within a round; (2) C-18 was introduced at the R5/R6 boundary, making "Round 5" or "Round 6" references structurally ambiguous with respect to the introduction boundary. "V-05(R4)" is the minimum verifiable unit: it names the exact variation (enabling gate architecture lookup) and the round (enabling boundary comparison). The coarseness threshold for C-22 failure is not about precision preference — it is about whether timeline comparison is computable.

**Signal 3 — C-21/C-22 orthogonality confirmed (V-02)**

V-02's design — provenance in gates, no manifest — confirms that C-22 is independent of C-19 and C-21. Gate-level documentation (C-20, C-22) and manifest-level documentation (C-19, C-21) form two orthogonal pairs. A variation can satisfy the gate pair without the manifest pair, and vice versa. This mirrors the C-17/C-19 orthogonality confirmed in R6: C-17 (output-level composability) can be verified by inspection without producing a manifest; C-19 (process-level commitment) requires a manifest. Similarly, C-20 (gate design integrity) can be established by the structural removal test; C-22 (provenance verifiability) requires the historical reference. Both C-21 and C-22 are "quality dimensions" of their weaker counterparts — they add verifiability/generativity to properties the base criteria already require.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Causal archetype template (PREREQUISITE/ESTABLISHES/AMPLIFIES/PARALLEL) enforces C-21 by construction — archetype selection + mechanism fill-in forces directional causal statement where free-form inspection produces only reinforcement conclusions", "Variation-level specificity is the atomic verifiability unit for C-22 — round-only provenance fails because C-18 was introduced at the R5/R6 boundary, making round references ambiguous; variation+round ('V-05(R4)') is the minimum addressable unit for timeline comparison", "C-21/C-22 orthogonality confirmed — gate-level documentation (C-20, C-22) and manifest-level documentation (C-19, C-21) are independent pairs; V-02 demonstrates C-22 PASS without C-19, mirroring R6's confirmation that C-17 and C-19 are orthogonal"]}
```
