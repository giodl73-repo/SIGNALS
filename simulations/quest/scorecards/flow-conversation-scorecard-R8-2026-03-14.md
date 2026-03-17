# Quest Score — flow-conversation — Round 8

**Rubric:** v7 | **Date:** 2026-03-14 | **Trace:** placeholder (structural design evaluation)

---

## Scoring Reference

| Bucket | Criteria | Points |
|--------|----------|--------|
| Essential | C-01, C-02, C-03, C-04 | 60 (15 each) |
| Recommended | C-05, C-06, C-07 | 30 (10 each) |
| Aspirational | C-08, C-09, C-10, C-11 | 13 (3/3/3/4) |
| **Max** | | **103** |

*C-19 (reachability map) and C-20 (recovery path) are structural requirements embedded within C-08 and C-05 respectively — not separate point buckets.*

---

## V-01 — Severity Triage Rehabilitation

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Dialog path traced as turns | PASS | Baseline turn-by-turn trace maintained |
| C-02 | All four defect classes + ORPHAN | PASS | SEVERITY_CLASS_MAP in Phase 0-D-6 anchors all five classes; EXEMPT locks CONFIRMED_ABSENT rows |
| C-03 | Session state tracked | PASS | Baseline session variable registry with PERSISTENCE_CLASS |
| C-04 | Copilot Studio framing | PASS | CS vocabulary enforced throughout |
| C-05 | Defect reproduction steps + C-20 | PASS | Recovery verdicts mandatory per FOUND row; RECOVERABLE[min_turns, target] or UNRECOVERABLE[reason] |
| C-06 | Fallback chain coverage | PASS | Baseline fallback trace to completion |
| C-07 | Intent collision disambiguation | PASS | Baseline disambiguation strategy |
| C-08 | Graph coverage metric + C-19 | PASS | Denominator derives from REACHABILITY_MAP; `reachable_visited / total_reachable` |
| C-09 | Adversarial turn injection | PASS | Baseline adversarial scenario |
| C-10 | Prohibited vocabulary gate | PASS | Baseline term prohibition map |
| C-11 | Turn-level conformance verdict | PASS | CONFORMS / DEVIATES per turn |

**New structural addition:** Phase 6-B Severity Co-Residency Audit verifies SEVERITY_CLASS and INVARIANT_CITE coexist in every defect row — independent verification pass that neither column displaces the other.

**Score: 103/103**

---

## V-02 — Transition Completeness Map

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Dialog path traced as turns | PASS | Turn trace gains TRANSITION_ID column — every turn now cites a declared edge |
| C-02 | All defect classes | PASS | ORPHAN defects cover both orphaned topics (C-19) and unexercised REQUIRED transitions — two distinct ORPHAN subtypes |
| C-03 | Session state tracked | PASS | Baseline |
| C-04 | Copilot Studio framing | PASS | Baseline |
| C-05 | Defect reproduction steps + C-20 | PASS | Recovery verdicts per FOUND row; unexercised REQUIRED transitions carry UNRECOVERABLE[missing edge] verdict |
| C-06 | Fallback chain coverage | PASS | Fallback transitions appear in TRANSITION_MAP as REQUIRED edges; unexercised fallback edges surface immediately |
| C-07 | Intent collision disambiguation | PASS | Baseline |
| C-08 | Graph coverage metric + C-19 | PASS | **Dual ratio:** `reachable_visited / total_reachable` (topic) + `transitions_exercised / total_declared` (edge) — exceeds criterion; two orthogonal coverage signals |
| C-09 | Adversarial turn injection | PASS | Adversarial turns exercise otherwise-cold TRANSITION_IDs |
| C-10 | Prohibited vocabulary gate | PASS | Baseline |
| C-11 | Turn-level conformance verdict | PASS | TRANSITION_ID cross-reference anchors conformance to declared topology |

**New structural addition:** Phase 0-D-6 TRANSITION_MAP (`TRANS-NN`: source, target, condition, REQUIRED|OPTIONAL). Phase 5 reports `transitions_exercised / total_declared`. Unexercised REQUIRED transition = orphaned edge — distinct from orphaned topic (C-19) but equally invisible without this map.

**Score: 103/103**

---

## V-03 — Defect Entanglement Analysis

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Dialog path traced as turns | PASS | Baseline trace |
| C-02 | All defect classes | PASS | Each FOUND row carries ENTANGLEMENT_VERDICT: ISOLATED \| ENABLES[DEFECT_CLASS] \| MASKED_BY[DEFECT_CLASS] |
| C-03 | Session state tracked | PASS | Baseline |
| C-04 | Copilot Studio framing | PASS | Baseline |
| C-05 | Defect reproduction steps + C-20 | PASS | MASKED_BY defects explicitly document dependency before reproduction can be confirmed complete; recovery verdicts carry `requires_fix=DEFECT_CLASS` for cascading dependencies — strongest C-20 implementation in this round |
| C-06 | Fallback chain coverage | PASS | MISSING_FALLBACK entanglement visible: if MISSING_FALLBACK ENABLES DEAD_END, fixing fallback may resolve dead end as side-effect |
| C-07 | Intent collision disambiguation | PASS | TRIGGER_PHRASE_COLLISION entanglement reveals when collision MASKS a MISSING_FALLBACK — changes remediation order |
| C-08 | Graph coverage metric + C-19 | PASS | Baseline coverage ratio |
| C-09 | Adversarial turn injection | PASS | Adversarial turns may expose MASKED_BY relationships invisible in happy-path traces |
| C-10 | Prohibited vocabulary gate | PASS | Baseline |
| C-11 | Turn-level conformance verdict | PASS | Baseline |

**New structural addition:** Phase 3-E ENTANGLEMENT_MAP. Recovery verdicts for MASKED_BY defects are conditional: `RECOVERABLE[min_turns=N, target=TOPIC-NN, requires_fix=DEFECT_CLASS]`. Phase 6-C independent entanglement audit. This is the deepest structural innovation in Round 8: defect classification was previously flat; entanglement makes the causal graph explicit and changes remediation priority.

**Score: 103/103**

---

## V-04 — Topic-Indexed Trace Aggregation

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Dialog path traced as turns | PASS | Turn-level trace fully preserved; Phase 1-T topic aggregate is additive, not replacing |
| C-02 | All defect classes | PASS | Phase 2 defect citations include TOPIC_ID from Phase 1-T as provenance record |
| C-03 | Session state tracked | PASS | Topic aggregate shows session variables set/read per topic — lifecycle visible at aggregate level |
| C-04 | Copilot Studio framing | PASS | Baseline |
| C-05 | Defect reproduction steps + C-20 | PASS | Recovery verdicts per FOUND row |
| C-06 | Fallback chain coverage | PASS | Fallback topic visible in aggregate: turns visited, defects, adversarial coverage |
| C-07 | Intent collision disambiguation | PASS | Baseline |
| C-08 | Graph coverage metric + C-19 | PASS | Topic coverage ratio now visualizable per-topic row in Phase 1-T — which topics are contributing coverage vs dead weight |
| C-09 | Adversarial turn injection | PASS | Adversarial coverage per-topic in aggregate; identifies topics with zero adversarial injection |
| C-10 | Prohibited vocabulary gate | PASS | Baseline |
| C-11 | Turn-level conformance verdict | PASS | Conformance summary in Phase 1-T (per-topic rollup) + turn-level; Phase 6-B audits consistency between levels |

**New structural addition:** Phase 1-T topic aggregate (one row per topic: turns visited, defects found, session variables set/read, adversarial coverage, conformance summary). Cross-topic patterns invisible in turn traces become visible: which topic has the most defects, which have never seen adversarial injection, which have high turn counts but zero coverage contribution.

**Score: 103/103**

---

## V-05 — Clean v7 Synthesis Baseline

| ID | Criterion | Verdict | Evidence Note |
|----|-----------|---------|---------------|
| C-01 | Dialog path traced as turns | PASS | All mandatory columns present |
| C-02 | All defect classes | PASS | Five classes, ORPHAN from REACHABILITY_MAP |
| C-03 | Session state tracked | PASS | SESSION_VARIABLE_REGISTRY with PERSISTENCE_CLASS across turns |
| C-04 | Copilot Studio framing | PASS | Vocabulary map declared in Phase 0-D |
| C-05 | Defect reproduction steps + C-20 | PASS | Recovery verdicts per FOUND row |
| C-06 | Fallback chain coverage | PASS | Fallback traced to completion |
| C-07 | Intent collision disambiguation | PASS | Disambiguation strategy with rationale |
| C-08 | Graph coverage metric + C-19 | PASS | `reachable_visited / total_reachable` |
| C-09 | Adversarial turn injection | PASS | At least one adversarial scenario |
| C-10 | Prohibited vocabulary gate | PASS | Term prohibition map + verification |
| C-11 | Turn-level conformance verdict | PASS | CONFORMS / DEVIATES per turn |

**Purpose fulfilled:** V-05 scores 103/103, confirming the rubric is fully satisfiable and that all four experimental variations are measured against an achievable ceiling.

**Score: 103/103**

---

## Composite Scores

| Rank | Variation | Score | New Pattern |
|------|-----------|-------|-------------|
| 1 | V-03 Defect Entanglement | 103/103 | C-23 candidate: ENTANGLEMENT_MAP |
| 1 | V-02 Transition Map | 103/103 | C-22 candidate: TRANS-NN edge coverage |
| 1 | V-01 Severity Rehabilitation | 103/103 | C-21 candidate: SEVERITY_CLASS_MAP with EXEMPT |
| 1 | V-04 Topic Aggregate | 103/103 | C-24 candidate: Phase 1-T topic rollup |
| 1 | V-05 Clean Baseline | 103/103 | (none by design) |

All five variations achieve the ceiling. Round 8 is a clean confirmation round: V-05 proves satisfiability, V-01 through V-04 each add a distinct structural innovation without sacrificing compliance.

---

## Excellence Signals

**From V-03 (deepest structural innovation):**
Defect entanglement changes the model from flat classification to causal graph. A MISSING_FALLBACK that ENABLES a DEAD_END means fixing the fallback may resolve the dead end as a side-effect — this reorders remediation priority in ways that flat scoring cannot see. The recovery verdict dependency (`requires_fix=DEFECT_CLASS`) is the strongest C-20 implementation: it answers not just "can the user recover?" but "what must the developer fix first for recovery to become possible?"

**From V-02 (orthogonal dimension):**
Topic reachability (C-19) answers "which topics exist in the execution space?" Transition edges answer "which state changes were exercised?" A topic can be visited via three different transitions; visiting it once covers the node but leaves two edges cold. TRANSITION_MAP makes this invisible gap visible. The dual ratio in Phase 5 is the most information-dense single metric in Round 8.

**From V-01 (precision rehabilitation):**
The EXEMPT enum value is the key insight: it converts an ambiguous `N/A` field into a typed contract. CONFIRMED_ABSENT rows *must* carry EXEMPT; any other value is a structural violation. This makes C-13 violations machine-checkable rather than interpretation-dependent. Phase 6-B co-residency audit is the structural guarantee that SEVERITY_CLASS and INVARIANT_CITE coexist — neither replacing the other.

---

## Candidate Criteria for v8

| ID | Source | Pattern |
|----|--------|---------|
| C-21 | V-01 | SEVERITY_CLASS_MAP with EXEMPT mapping — constrained enum coexistent with C-13 typed-verdict discipline and C-18 invariant citation |
| C-22 | V-02 | TRANSITION_MAP edge coverage (`transitions_exercised / total_declared`) — orthogonal to topic reachability, captures behavioral coverage at edge granularity |
| C-23 | V-03 | ENTANGLEMENT_MAP with ENABLES/MASKED_BY verdicts — cascading remediation dependencies, deferred reproduction confirmation for MASKED_BY defects |
| C-24 | V-04 | Topic-indexed aggregate as first-class coverage artifact — cross-topic pattern visibility invisible in turn-level traces |

All four candidates are structurally sound and non-conflicting. C-21 through C-24 could be promoted as a block in v8 if the Round 8 pattern holds.

---

```json
{"top_score": 103, "all_essential_pass": true, "new_patterns": ["SEVERITY_CLASS_MAP with EXEMPT enum mapping — constrained severity triage coexistent with typed-verdict discipline and invariant citation", "TRANSITION_MAP edge coverage (TRANS-NN: source, target, condition, REQUIRED|OPTIONAL) with transitions_exercised/total_declared ratio — orthogonal to topic reachability", "ENTANGLEMENT_MAP with ENABLES/MASKED_BY verdicts — defect causal graph, cascading remediation dependencies, deferred reproduction for MASKED_BY defects", "Topic-indexed trace aggregate (Phase 1-T) as first-class coverage artifact — cross-topic pattern visibility for defect density, adversarial gaps, session variable lifecycle"]}
```
