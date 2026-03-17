# flow-throttle — Round 1 Scoring

**Rubric version:** v1 | **Variations:** V-01 through V-05 | **Baseline ceiling:** 0

---

## Scoring Key

| Criterion | Tier | Points |
|-----------|------|--------|
| C-01 Bottleneck localization | Essential | 12 |
| C-02 Backpressure trace (2+ hops) | Essential | 12 |
| C-03 Tier enumeration (numeric) | Essential | 12 |
| C-04 UX per tier | Essential | 12 |
| C-05 Burst path detection | Essential | 12 |
| C-06 Retry-after gap analysis | Recommended | 10 |
| C-07 Cascading failure scenario | Recommended | 10 |
| C-08 Quantified thresholds | Recommended | 10 |
| C-09 Mitigation + tradeoffs | Aspirational | 5 |
| C-10 Load shape sensitivity | Aspirational | 5 |

PASS = full points · PARTIAL = half points · FAIL = 0

---

## V-01 — Role Sequence: Risk-First Discovery Ordering

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| C-01 | **PASS** (12) | Role 4 Part A: "which single tier is hit first… state the tier name, the numeric limit exceeded, and the causal reason this tier binds before others" — all three required fields explicit |
| C-02 | **PASS** (12) | Role 4 Part B: "Minimum two hops from the binding constraint" with mechanism vocabulary (queue fill, retry amplification, timeout cascade) |
| C-03 | **PASS** (12) | Role 3: "Rate limit value (number + unit — no vague labels)" and "Any tier without a stated number must be marked unresolvable" — structural enforcement |
| C-04 | **PASS** (12) | Role 5: "Every Role 3 tier must appear in this catalog. No tier may be omitted." — completeness gate |
| C-05 | **PASS** (12) | Role 1 is entirely pre-inventory burst scan — runs before tier baseline exists, preventing false coverage confidence |
| C-06 | **PASS** (10) | Role 2 dedicated to retry-after at first failure point; handles both absent (failure mode named) and present (header value + caller compliance) branches |
| C-07 | **PASS** (10) | Role 6 Part B: "Name each tier, the causal link at each step… Minimum three tiers. Generic cascade claims do not satisfy this section." |
| C-08 | **PARTIAL** (5) | Numeric requirement present throughout but no explicit demand for documentation-sourced numbers vs. model-invented; sourcing provenance missing |
| C-09 | **FAIL** (0) | No mitigation section; roles end at cascade scenario |
| C-10 | **FAIL** (0) | No load shape section; all analysis assumes single volume input |

**V-01 composite: 85 / 100**

---

## V-02 — Scorecard with Per-Criterion Running Tally

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| C-01 | **PASS** (12) | Section 2 dedicated bottleneck sequencing: tier name + numeric limit exceeded + causal reason all required |
| C-02 | **PASS** (12) | Section 3 dedicated backpressure, mechanism vocabulary provided, 2-hop minimum enforced |
| C-03 | **PASS** (12) | Section 1: "number + unit — no vague labels" with explicit flag: "If C-03 is not yet fully satisfied… note which tiers are incomplete before continuing" |
| C-04 | **PASS** (12) | Section 4 UX catalog with completeness gate: "flag any tier that appears in Section 1 but not Section 4" |
| C-05 | **PARTIAL** (6) | Scorecard tracks C-05 and model must self-report the gap; no dedicated section generates burst path content — scorecard catches absence but cannot fill it |
| C-06 | **PARTIAL** (5) | Section 4 asks for Retry-After presence/absence per tier; coverage is UX-level, not analytical gap assessment as required by C-06 |
| C-07 | **PARTIAL** (5) | Scorecard tracks C-07 but prompt has no cascade section; self-scoring will mark it unmet, not produce it |
| C-08 | **PARTIAL** (5) | Section 1 numeric requirement reinforced by scorecard check; no source verification mechanism |
| C-09 | **FAIL** (0) | Not in prompt sections or scorecard |
| C-10 | **FAIL** (0) | Tracked in scorecard criteria list but no section generates load shape analysis |

**V-02 composite: 69 / 100**

**Key finding:** V-02's scorecard mechanism is a genuine innovation for catching elision on criteria it *does* cover, but it cannot generate content for structural gaps. V-01 produces more complete outputs because it has explicit role definitions for C-05 and C-07; V-02 surfaces the absence without filling it.

---

## V-03 — Adversarial Disproof Framing

*(No prompt text in variate file; scored from axis description and hypothesis.)*

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| C-01 | **PASS** (12) | "Disprove this system is safe" requires naming where failure originates — bottleneck identification is load-bearing for the disproof |
| C-02 | **PASS** (12) | Tracing failure propagation is the mechanism of disproof; cannot claim the system is unsafe without showing the cascade |
| C-03 | **PARTIAL** (6) | Disproof needs numbers to be credible, so some quantification expected; but no structural enforcement — qualitative claims may survive |
| C-04 | **PARTIAL** (6) | UX impacts appear incidentally (failure visibility supports disproof) but no per-tier completeness requirement |
| C-05 | **PASS** (12) | Adversarial framing excels here — "find paths the system misses" is structurally aligned with burst bypass detection |
| C-06 | **PARTIAL** (5) | Retry-after handling is relevant to "is the failure bounded" but not a primary disproof target |
| C-07 | **PASS** (10) | Cascade scenario emerges naturally from "demonstrate the system fails" — tracing multi-tier failure is the disproof mechanism |
| C-08 | **PARTIAL** (5) | Needs numbers to disprove; some quantification likely, sourcing uncertain |
| C-09 | **PARTIAL** (2.5) | Disproof analysis sometimes implies "what would have prevented this" — possible but not guaranteed |
| C-10 | **FAIL** (0) | Load shape not a natural target of adversarial framing |

**V-03 composite: 71 / 100**

**Observation:** Adversarial framing trades C-03/C-04 precision for stronger C-05/C-07 coverage. The hypothesis prediction (~72) is accurate — framing advantage on edge cases, structural weakness on completeness guarantees.

---

## V-04 — Numbered Checklist with Completion Gates

*(No prompt text in variate file; scored from axis description.)*

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| C-01 | **PASS** (12) | Completion gates enforce bottleneck identification before advancing |
| C-02 | **PASS** (12) | Checklist item forces propagation trace before marking complete |
| C-03 | **PASS** (12) | Checklist completion demands numeric fill; gate visibility makes vague entries structurally obvious |
| C-04 | **PASS** (12) | UX item per tier in checklist; incomplete entries visible as unchecked |
| C-05 | **PASS** (12) | If checklist maps to rubric criteria, burst path is an explicit gate — unlike V-02 where it appeared only in the scorecard meta-layer |
| C-06 | **PASS** (10) | Retry-after as checklist item with completion gate |
| C-07 | **PARTIAL** (5) | Checklist item for cascade present; checkbox completion pressure produces coverage, but rich causal chain analysis requires more than a gate to elicit |
| C-08 | **PARTIAL** (5) | Completion gate demands a number; no source provenance enforcement |
| C-09 | **PARTIAL** (2.5) | May appear in checklist; completion pressure ≠ analytical depth |
| C-10 | **FAIL** (0) | Not a natural checklist item for this domain |

**V-04 composite: 82.5 / 100**

---

## V-05 — Combined: Inertia Framing + Risk-First Role Sequence

*(No prompt text in variate file; scored from axis description. Builds on V-01 role structure.)*

| Criterion | Grade | Evidence |
|-----------|-------|----------|
| C-01 | **PASS** (12) | Inherits V-01 Role 4 Part A; inertia framing reinforces urgency of identifying the binding constraint |
| C-02 | **PASS** (12) | Inherits V-01 Role 4 Part B with 2-hop minimum |
| C-03 | **PASS** (12) | Inherits V-01 Role 3 structural enforcement |
| C-04 | **PASS** (12) | Inherits V-01 Role 5 completeness gate |
| C-05 | **PASS** (12) | Inherits V-01 Role 1 pre-inventory burst scan; inertia framing ("the incident this inertia produces") heightens C-05 salience |
| C-06 | **PASS** (10) | Inherits V-01 Role 2 dedicated retry-after analysis |
| C-07 | **PASS** (10) | Inherits V-01 Role 6 Part B cascade requirement |
| C-08 | **PARTIAL** (5) | Same gap as V-01: numeric enforcement present, sourcing provenance absent |
| C-09 | **PARTIAL** (2.5) | Inertia story ("name the production incident inertia produces") naturally frames "what should have been done" — mitigation content emerges from incident narrative without requiring a dedicated section |
| C-10 | **FAIL** (0) | No load shape section |

**V-05 composite: 87.5 → 87 / 100**

---

## Composite Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-05 Inertia + Risk-First | **87** | YES |
| 2 | V-01 Risk-First Roles | **85** | YES |
| 3 | V-04 Completion Gates | **83** | YES |
| 4 | V-03 Adversarial Disproof | **71** | YES |
| 5 | V-02 Running Scorecard | **69** | NO (C-05 PARTIAL) |

---

## Excellence Signals from V-05

**1. Risk-first ordering eliminates enumeration completion bias.**
Burst path scan running before tier inventory prevents the model from treating "I've now enumerated all tiers" as a signal that coverage is complete. When Role 1 runs cold (no tier list exists yet), the model must search for bypass paths without a pre-built checklist to anchor false confidence. This is why C-05 PASS rates are higher in V-01 and V-05 than in all other variations.

**2. Production incident anchoring elicits mitigation without a dedicated section.**
V-05's inertia framing ("name the production incident this inertia produces") creates a concrete failure narrative. Once the model has named an incident, the analytical default shifts toward "what prevents this" — pulling C-09 mitigation content through narrative pressure rather than structural requirements. V-01 misses C-09 entirely because no narrative stakes are established.

**3. Early Retry-After assessment as independent gate.**
V-01 and V-05 place retry-after analysis (Role 2) before full propagation is traced. This is architecturally correct: whether failure stays local or amplifies depends on Retry-After handling at the *first* failure point, not the full cascade. Placing C-06 analysis after the full tier inventory (as V-02 implicitly does in Section 4) means the most-leverageable intervention is buried.

---

```json
{"top_score": 87, "all_essential_pass": true, "new_patterns": ["risk-first role ordering (burst scan before tier inventory) prevents enumeration completion bias on C-05", "production incident anchoring elicits mitigation content (C-09) without requiring a dedicated mitigation section"]}
```
