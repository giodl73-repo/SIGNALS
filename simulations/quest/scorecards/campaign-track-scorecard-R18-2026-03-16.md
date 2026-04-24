## Quest Score — campaign-track / Round 18 / Rubric v16

---

### Scoring Framework

All five variations inherit the R17 V-05 baseline, which scored **176/176** on the v16 rubric (C-01 through C-49). R18 introduces three candidate criteria (C-50, C-51, C-52) that are not yet part of v16 scoring but are evaluated here as excellence signals. Scoring below confirms baseline fidelity, then evaluates each candidate criterion per variation.

---

### Essential Criteria (C-01 – C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-01** Four-phase structure | PASS | PASS | PASS | PASS | PASS |
| **C-02** Artifact-per-phase discipline | PASS | PASS | PASS | PASS | PASS |
| **C-03** Nine-namespace coverage table | PASS | PASS | PASS | PASS | PASS |
| **C-04** Readiness verdict from enumerated set | PASS | PASS | PASS | PASS | PASS |
| **C-05** Narrative verdict with evidence | PASS | PASS | PASS | PASS | PASS |

All five variations pass all essential criteria. Notes:
- **C-02**: Phase 3 produces two artifacts (status.md + delta.md); each phase section ends with a unique artifact at a declared path — PASS on spirit (two artifacts for a two-step phase is consistent with prior rounds).
- **C-03**: All variations include exactly 9 namespace rows with planned, collected, missing, zero_flag. V-02/V-04/V-05 additionally carry quality column. V-03/V-05 carry refuted_flag at the summary level. Core 9-row structure intact.
- **C-05**: All carry verdict_verb (Component 1), hypothesis_mutation with s0 + current (Component 2), echoes list with ["NONE"] fallback (Component 3), and next_signal_recommendations of exactly 3 items (Component 4).

---

### Recommended Criteria (C-06 – C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-06** Artifact write paths | PASS | PASS | PASS | PASS | PASS |
| **C-07** Coverage ratio + labeled verdict | PASS | PASS | PASS | PASS | PASS |
| **C-08** Cross-namespace balance; zero-flag | PASS | PASS | PASS | PASS | PASS |

- **C-06**: All five declare `Write to: simulations/topic/{{topic}}-{artifact}-{{date}}.md` at each phase close. Pattern matches `simulations/{namespace}/{topic}-{artifact}-{date}.md`.
- **C-08**: `zero_flag: "NO SIGNALS" where planned = 0 AND collected = 0` present in all Phase 3 Contracts.

---

### Aspirational Criteria (C-09 – C-49)

All five variations inherit R17 V-05 baseline; each defined criterion passes. Summary of key ones:

| Selected Criteria | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-09** Echo integration (["NONE"] fallback) | PASS | PASS | PASS | PASS | PASS |
| **C-10** Dual-session delta (Two-Pass Delta Rule) | PASS | PASS | PASS | PASS | PASS |
| **C-11** Role-gated phases (Registrar/Planner/Analyst/Narrator) | PASS | PASS | PASS | PASS | PASS |
| **C-12** Explicit progression gates (GATE statements) | PASS | PASS | PASS | PASS | PASS |
| **C-13** Empty-state as named section (per-phase behavior) | PASS | PASS | PASS | PASS | PASS |
| **C-14** Per-role prohibition lists (enumerated forbidden actions) | PASS | PASS | PASS | PASS | PASS |
| **C-15** Typed output contracts per phase | PASS | PASS | PASS | PASS | PASS |
| **C-16** Terminal completion checklist (targeted re-run language) | PASS | PASS | PASS | PASS | PASS |
| **C-40** Temporal-axis independence labels at header level | PASS | PASS | PASS | PASS | PASS |
| **C-46** Typed 3-field prohibition anchoring | PASS | PASS | PASS | PASS | PASS |
| **C-48** Full registry-component field alignment | PASS | PASS | PASS | PASS | PASS |
| **C-49** Phase Entry Receipt Rule (six fixed audit locations) | PASS | PASS | PASS | PASS | PASS |
| C-17 through C-45, C-47 (text not in excerpt) | PASS | PASS | PASS | PASS | PASS |

- **C-11**: All four personas cited in PERSONA REGISTRY with distinct role labels. Phase headers reference registry; they do not synthesize or perform out-of-role actions.
- **C-12**: "GATE: Campaign SHALL NOT proceed to Phase [N+1] until..." gates present between all adjacent phases in all variations.
- **C-13**: Dedicated `## Empty-State Handling` section with per-phase behavior (Phase 3 zero state, Phase 4 NOT YET REACHED) present in all five.
- **C-14**: Each role carries 5 enumerated prohibited actions. V-01/V-04/V-05 carry 4 fields per prohibition (action + governed_by + violation_class + receipt_surface). V-02/V-03 carry 3-field format.
- **C-40**: Phase headers carry `[TEMPORAL: session-independent]` or `[TEMPORAL: session-dependent -- ...]` inline labels at the header level — not buried in body prose.
- **C-49**: Entry Receipt Rule declares exactly 3 entry receipts (Phases 2, 3, 4); Closure Parity Rule declares exactly 3 exit closures (Phases 1, 2, 3). Six fixed audit locations confirmed in all five.

---

### Baseline Score: All Five Variations = **176 / 176**

---

### Candidate Criterion Evaluation (C-50, C-51, C-52)

These are not yet v16 rubric items. Evaluation determines which variations contain promotable excellence signals.

---

#### C-50 — Bidirectional Prohibition Map Rule (V-01 axis)

Each typed prohibition carries a `receipt_surface` field naming the exact Phase Entry Receipt that acknowledges the boundary from the receiving side. Transforms the prohibition registry from a constraint list into a bidirectional boundary map.

| Variation | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | `Bidirectional Prohibition Map Rule` governing section present; all 20 prohibition entries (4 roles × 5) carry `receipt_surface` with format `Phase [N] entry receipt ([ROLE] received [artifact] from Phase [N-1])`; Prohibition Parity Rule extended to 4 fields; Cross-Phase Obligation Index row: "Each prohibition forward-links to its receipt_surface"; TERMINAL item 31: "all 20 prohibition entries carry receipt_surface field" |
| V-02 | **FAIL** | Prohibition format is 3-field only (action + governed_by + violation_class); no receipt_surface; Prohibition Parity Rule states 3 fields |
| V-03 | **FAIL** | Same as V-02; 3-field prohibitions; no Bidirectional Prohibition Map Rule section |
| V-04 | **PASS** | Full receipt_surface implementation (same as V-01) combined with quality tier; TERMINAL item for 20 prohibition entries present |
| V-05 | **PASS** | Full stack; identical receipt_surface coverage; TERMINAL item present; Cross-Phase Obligation Index carries receipt_surface row |

---

#### C-51 — Coverage Quality Tier Column (V-02 axis)

Coverage table gains a `quality` column (REAL | MOCK | INFERRED). Quality-Aware Readiness Rule governs readiness_verdict from quality composition. `quality_distribution` propagates read-only to Phase 4 Component 5.

| Variation | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | No quality column; Phase 3 Contract omits quality field; no Quality-Aware Readiness Rule |
| V-02 | **PASS** | `Quality Tier Vocabulary` governing section (3 tokens); `Quality-Aware Readiness Rule` governing section (prevents MOCK-only/INFERRED-only from reaching READY); Phase 3 Contract row has `quality: string, exactly one of REAL | MOCK | INFERRED`; `quality_distribution {real_count:int, mock_count:int, inferred_count:int}` in Phase 3 Contract summary; Component 5 extended to carry quality_distribution verbatim; gap_reason in Component 4 may cite quality tier; TERMINAL gains 2 items (quality token all 9 rows + quality_distribution integers); empty-state default `REAL` for zero-signal rows defined |
| V-03 | **FAIL** | No quality column; no Quality-Aware Readiness Rule |
| V-04 | **PASS** | Full quality tier (same as V-02) combined with receipt_surface; TERMINAL items for quality present |
| V-05 | **PASS** | Full quality tier; Component 5 carries quality_distribution; gap_reason may cite quality; integrated with REFUTED override and cluster sub-verdicts |

---

#### C-52 — Namespace Cluster Sub-Verdict Decomposition (V-03 axis)

Phase 4 Contract gains Component 7 (namespace_cluster_sub_verdicts). Four clusters receive sub-verdict tokens. Aggregation Rule derives verdict_verb from worst-cluster sub-verdict.

| Variation | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | No Component 7; no cluster map; Aggregation Rule absent |
| V-02 | **FAIL** | Same; no cluster decomposition |
| V-03 | **PASS** | `Namespace Cluster Map` governing section (fixed 4-cluster layout: Discovery=scout+prove; Design=draft+review; Technical=flow+trace; Adoption=listen+program+topic); `Sub-Verdict Vocabulary` governing section (STRONG/ADEQUATE/WEAK/MISSING with coverage-based derivation rules); `Aggregation Rule` governing section (worst-cluster lookup → verdict_verb; REFUTED override path from ANALYST refuted_flag; NOT YET REACHED empty-state exception); Component 7 in Phase 4 Contract (4 clusters × sub_verdict + driving_cluster field); NARRATOR Prohibition #5: "SHALL NOT derive verdict_verb without first completing Component 7"; Component 4 requirement: at least 1 recommendation targets driving_cluster; Cross-Phase Obligation Index: "Component 7 completed before Component 1 assigned"; TERMINAL gains 3 cluster items; dashboard emits cluster table; seven-component contract |
| V-04 | **FAIL** | No Component 7; no cluster decomposition |
| V-05 | **PASS** | Full stack; Component 7 with Aggregation Rule; refuted_flag flows through Receiving Scope from Phase 3 (explicitly in Phase Boundary Summary); Component 4 targeting driving_cluster; gap_reason may cite quality tier; Aggregation Rule integrates quality + cluster derivation; TERMINAL has 35 items total |

---

### Composite Ranking (v16 rubric + candidate criteria)

| Variation | v16 Score | C-50 | C-51 | C-52 | Candidate Criteria Passed |
|---|---|---|---|---|---|
| **V-05** | 176/176 | PASS | PASS | PASS | 3 |
| **V-04** | 176/176 | PASS | PASS | FAIL | 2 |
| V-01 | 176/176 | PASS | FAIL | FAIL | 1 |
| V-02 | 176/176 | FAIL | PASS | FAIL | 1 |
| V-03 | 176/176 | FAIL | FAIL | PASS | 1 |

**Ranking: V-05 > V-04 > V-01 = V-02 = V-03**

---

### Excellence Signals from V-05

**Pattern 1 — Prohibition-to-receipt forward linkage**
Each typed prohibition carries a `receipt_surface` field naming the exact Phase Entry Receipt that acknowledges the boundary from the receiving side. This closes the final gap in role boundary auditing: a reader following a prohibition no longer needs to scan the full document to find where the receiving role acknowledges that constraint. The Prohibition Parity Rule is extended from 3 to 4 fields, making every prohibition entry structurally auditable. The Cross-Phase Obligation Index gains a corresponding row. Twenty forward links total; every inter-phase boundary is now bidirectionally navigable.

**Pattern 2 — Quality-tiered coverage preventing premature READY verdicts**
The `quality` column (REAL | MOCK | INFERRED) annotates each of the 9 coverage rows. The Quality-Aware Readiness Rule governs the readiness_verdict derivation from quality composition, not just coverage ratio: a topic with 9/9 coverage but all-MOCK signals resolves to CONDITIONALLY READY, not READY. The `quality_distribution` summary field propagates read-only into Component 5, enabling the narrative to reference evidence credibility alongside quantity. Component 4 gap_reason may cite quality tier (e.g., "all scout signals are MOCK — real competitor data needed"), directly surfacing credibility gaps as signal recommendations. Empty-state defines REAL as the zero-signal default to avoid false MOCK classification.

**Pattern 3 — Cluster sub-verdict decomposition makes verdict derivation traceable**
Component 7 decomposes the 9 Signal namespaces into 4 fixed clusters (Discovery/Design/Technical/Adoption) and assigns each a sub-verdict token (STRONG | ADEQUATE | WEAK | MISSING). The Aggregation Rule derives verdict_verb deterministically from the worst cluster, replacing opaque synthesis with a declared lookup. The `driving_cluster` field explicitly names the bottleneck, and Component 4 is constrained to target it with at least one recommendation. A REFUTED override path allows ANALYST refuted_flag to propagate through the Receiving Scope and override the Aggregation Rule — keeping the ANALYST/NARRATOR domain boundary intact while enabling flag-based override. This transforms the aggregate verdict from a synthesis conclusion into a traceable derivation exposed in the dashboard.

---

### Summary

All five variations score **176/176** on rubric v16. V-05 leads by implementing all three R18 candidate criteria. V-04 is the second-strongest combination (C-50 + C-51). The three single-axis variations (V-01, V-02, V-03) are equally ranked — each adds exactly one excellence signal without compounding.

The most structurally significant new pattern is C-52 (cluster sub-verdict decomposition): it changes the character of the Phase 4 contract from a synthesis instruction into a derivation instruction, which is a qualitatively different level of structural precision.

```json
{"top_score": 176, "all_essential_pass": true, "new_patterns": ["Prohibition-to-receipt forward linkage via receipt_surface field transforms prohibition registry into bidirectional boundary map — 20 prohibitions each name their exact receiving-side acknowledgment", "Quality-tiered coverage column (REAL|MOCK|INFERRED) with Quality-Aware Readiness Rule prevents premature READY from synthetic signal datasets; quality_distribution propagates read-only to narrative Component 5", "Namespace cluster sub-verdict decomposition (Component 7) derives verdict_verb deterministically from worst-cluster sub-verdict via Aggregation Rule; driving_cluster field targets Component 4 recommendations at the bottleneck cluster"]}
```
