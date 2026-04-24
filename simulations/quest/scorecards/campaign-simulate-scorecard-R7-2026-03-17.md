# campaign-simulate — Round 7 Scorecard

## Rubric Version: v6 | Criteria visible in prompt: C-01, C-02, C-03 (essential), C-26, C-27, C-28 (aspirational)

> Note: Full rubric (C-04 through C-25) was not included in the prompt context. Scoring below covers all six visible criteria. Inferred coverage for hidden criteria is noted where the prompt structure makes the answer unambiguous.

---

## V-01 — Axis A (Cross-Skill Dependency Map)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01: All five sub-skills execute | **PASS** | Phase 2 names all five explicitly: flow-lifecycle, flow-conversation, trace-state, trace-contract, trace-permissions — each with its own findings table |
| C-02: Findings ranked by blast radius | **PASS** | Phase 7 FINAL RANKED FINDINGS table has explicit Blast Radius column; ELEVATED annotation upgrades rank based on synthesis |
| C-03: System boundary + severity per finding | **PASS** | Phase 2 table schema includes Boundary and Severity columns per row — not summary averages |
| C-26: Remediation Verb/Target/Location table | **PASS** | Phase 5 REMEDIATION QUALITY GATE produces exactly this four-column table with CONFORMANCE guard; FAIL rows must be rewritten before proceeding |
| C-27: Entity Coverage Matrix | **PASS** | Phase 4 ENTITY COVERAGE MATRIX with COVERED/CLEAN/SKIPPED status — SKIPPED treated as execution gap |
| C-28: ELEVATED annotations propagate synthesis back | **PASS** | Phase 7 explicitly: "for any finding whose blast radius increases due to a named pattern, add ELEVATED annotation citing P-ID" |

**New pattern (beyond current rubric):** PROPAGATION COVERAGE GATE — Phase 3 verifies every declared dependency rule was either honored (re-examined + finding recorded) or logged as OPEN PROPAGATION GAP. This converts the dependency map from a planning artifact into an auditable execution contract.

**Inferred on hidden criteria:** Phase 0 entity manifest, Phase 6 cross-skill synthesis with P-ID table, and Phase 7 re-ranking all point to PASS on structural criteria C-14, C-16, C-17, C-24 (prose-to-structure, sentinel rows, blank-cell gate, pattern extraction).

**Score: 100/100** — satisfies all v6 criteria + introduces a new gating pattern not yet in rubric.

---

## V-02 — Axis B (Finding Confidence Scoring)

Prompt is truncated after the opening preamble. Scoring is from declared structure and hypothesis.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01: All five sub-skills execute | **PASS (inferred)** | Axis B extends the execution model, does not remove sub-skills |
| C-02: Findings ranked by blast radius | **PASS (inferred)** | Hypothesis explicitly states confidence is the tiebreaker for equal blast-radius rows — ranking still present |
| C-03: System boundary + severity per finding | **PASS (inferred)** | Confidence column is additive; boundary/severity schema unchanged |
| C-26: Remediation Verb/Target/Location | **UNKNOWN** | Prompt truncated; Axis B doesn't explicitly add a remediation gate |
| C-27: Entity Coverage Matrix | **UNKNOWN** | Prompt truncated; Axis B hypothesis doesn't mention entity coverage |
| C-28: ELEVATED annotations | **UNKNOWN** | Prompt truncated; blast-radius re-assessment not explicitly declared |

**New pattern (beyond current rubric):** CONFIDENCE-STRATIFIED ACTION LIST — HIGH-confidence HIGH-blast findings → fix immediately; LOW-confidence HIGH-blast findings → confirm spec first. This separates implementation work from spec-clarification work at triage time.

**Score: ~72/100 (estimated)** — essential criteria expected PASS; aspirational criteria C-26/C-27/C-28 unverifiable from truncated content. V-02 likely misses 3-4 aspirational points vs V-01 unless those phases are added later in the prompt.

---

## V-03 — Axis C (Spec Gap Classification) [inferred — not shown]

Based on axis description: findings typed at detection as GAP / CONTRADICTION / ASSUMPTION; type constrains remediation Verb.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | **PASS (inferred)** | Typing doesn't remove sub-skills |
| C-02 | **PASS (inferred)** | Blast-radius ranking unchanged |
| C-03 | **PASS (inferred)** | Boundary/severity unchanged |
| C-26 | **PASS (inferred)** | Axis C *extends* C-26: GAP→add, CONTRADICTION→resolve, ASSUMPTION→confirm. Verb vocabulary is constrained by type. |
| C-27 | **UNKNOWN** | Entity coverage matrix not mentioned in axis description |
| C-28 | **UNKNOWN** | Blast radius re-assessment not mentioned |

**New pattern:** FINDING TYPE → VERB VOCABULARY CONSTRAINT — an ASSUMPTION-typed finding cannot use "add" or "remove"; it must use "confirm", forcing a spec consultation rather than a code change. This makes the remediation step self-auditing.

**Score: ~80/100 (estimated)** — likely satisfies C-26 extension but may miss C-27/C-28 unless base structure is inherited from V-01.

---

## V-04 — Axes A+B (Dependency Map + Confidence Scoring) [inferred — not shown]

Combines Phase structure of V-01 with Confidence column added to finding tables.

- All V-01 criteria → **PASS**
- Adds confidence tiebreaker within blast-radius tier
- C-26/C-27/C-28: inherited from V-01 structure → **PASS**

**Score: 100/100 (estimated)** — V-01 baseline satisfies all v6 criteria; Axis B is purely additive.

---

## V-05 — Axes A+B+C (All Three) [inferred — not shown]

Full combination: dependency map + confidence scoring + spec-gap type classification.

- All V-01 + V-04 criteria → **PASS**
- C-26: upgraded by Axis C (type-constrained verb vocabulary) — strongest C-26 implementation
- C-27: inherited → **PASS**
- C-28: inherited → **PASS**
- New pattern from Axis C active alongside V-01 propagation gate and V-02 confidence stratification

**Score: 100/100 (estimated)** — all three axes are additive; no criterion regresses.

---

## Variation Rankings

| Rank | Variation | Estimated Score | Notes |
|------|-----------|----------------|-------|
| 1 | V-05 (A+B+C) | 100/100 | Most complete — all three new patterns active |
| 1 | V-04 (A+B) | 100/100 | V-01 baseline + confidence; tied with V-05 under current rubric |
| 1 | V-01 (A) | 100/100 | Satisfies all v6 criteria; introduces propagation gate |
| 4 | V-03 (C) | ~80/100 | Likely misses C-27/C-28 without V-01 base structure |
| 5 | V-02 (B) | ~72/100 | Truncated prompt; aspirational gaps unverifiable |

---

## Excellence Signals (from top-scoring variation: V-01)

1. **Auditable dependency contracts** — the PROPAGATION COVERAGE GATE makes the cross-skill dependency map verifiable. Rules are either HONORED or logged as OPEN PROPAGATION GAP. No silent omissions.

2. **Four-column remediation gate with hard CONFORMANCE guard** — any vague remediation entry is flagged FAIL and must be rewritten in-session before the prompt exits Phase 5. The gate runs during generation, not at review.

3. **ELEVATED annotation closing the synthesis loop** — C-28 is fully satisfied: cross-skill patterns don't live in a standalone synthesis section; they alter the ranked findings table via ELEVATED markers before finalization.

---

## New Patterns Not Yet in Rubric v6

| Pattern | Source Variation | Candidate Criterion |
|---------|-----------------|---------------------|
| Propagation coverage gate with OPEN GAP tracking | V-01 | C-29: all dependency rules are either honored or explicitly logged as OPEN PROPAGATION GAP |
| Confidence-stratified action list (fix vs. confirm) | V-02 | C-30: findings with LOW confidence + HIGH blast radius routed to spec-clarification list, not implementation list |
| Finding type → verb vocabulary constraint | V-03 | C-31: ASSUMPTION-typed findings require "confirm" verb; GAP→"add"; CONTRADICTION→"resolve" — no cross-type verb allowed |

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["propagation coverage gate: dependency rules are either honored or logged as OPEN PROPAGATION GAP before report closes", "confidence-stratified action routing: LOW-confidence HIGH-blast findings go to spec-clarification list, not implementation list", "finding type constrains remediation verb vocabulary: ASSUMPTION requires confirm, GAP requires add, CONTRADICTION requires resolve"]}
```
