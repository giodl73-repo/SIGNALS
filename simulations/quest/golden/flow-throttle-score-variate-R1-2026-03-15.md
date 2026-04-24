# flow-throttle Score — Round 1
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10)
**Variations scored:** V-01 through V-05 (from flow-throttle-variate-R1-2026-03-15.md)

---

## Scoring Formula (v1)

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
golden    = all essential pass AND composite >= 80
```

---

## V-01 — Role Sequence: Risk-First Discovery Ordering

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|---------|
| C-01 Bottleneck sequencing | essential | PASS | Role 4 Part A: binding tier, numeric limit exceeded, causal reason (lower cap / narrower scope / no burst headroom / shortest window) — explicitly required |
| C-02 Backpressure propagation | essential | PASS | Role 4 Part B: minimum 2 hops from binding constraint; mechanism type and observable effect required per hop |
| C-03 Quantified limits | essential | PASS | Role 3: "Every tier must have a numeric limit. Any tier without a stated number must be marked `unresolvable` with a reason." Role 1 also requires numeric limits as burst path components are traversed |
| C-04 UX per tier | essential | PASS | Role 5: "For every tier from Role 3, state what a user or flow author observes." Error code, run-history visibility, and ignore-Retry-After consequence all required. "Every Role 3 tier must appear in this catalog. No tier may be omitted." |
| C-05 Unprotected burst path | essential | PASS | Role 1 fully dedicated; requires entry component, route, and specific gap reason (absent connector policy / exempt trigger type / gateway bypass / no concurrency cap) |
| C-06 Retry-after handling | recommended | PASS | Role 2 fully dedicated; requires presence/absence of Retry-After, failure mode if absent (retry storm / missing exponential backoff / quota drain / infinite loop), or caller compliance if present |
| C-07 Cascade failure scenario | recommended | PASS | Role 6 Part B: "trace one concrete scenario where the Role 4 binding constraint triggers failure at a second tier, which triggers failure at a third. Name each tier, the causal link at each step, and the compounded effect." Minimum three tiers; generic claims excluded. |
| C-08 Tier risk ranking | recommended | PASS | Role 6 Part A: rank all Role 3 tiers by business risk; top-ranked tier requires blast radius, failure visibility, and recovery time estimate |
| C-09 Mitigation prescriptions | aspirational | FAIL | No section requests specific configuration, pattern, or API-level remediation for identified gaps. Roles 1 and 2 find gaps; no role asks the model to fix them. |
| C-10 Load shape sensitivity | aspirational | FAIL | No load shape analysis in any role. Same-volume uniform-vs-burst distinction is absent. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 0/2
**Composite:** (5/5 × 60) + (3/3 × 30) + (0/2 × 10) = **90**
**Golden:** YES (all essential pass, composite 90 ≥ 80)

---

## V-02 — Output Format: Scorecard with Per-Criterion Running Tally

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|---------|
| C-01 Bottleneck sequencing | essential | PASS | Section 2 dedicated: tier name, numeric limit exceeded, causal reason why this tier binds before all others |
| C-02 Backpressure propagation | essential | PASS | Section 3: minimum 2 hops; mechanism type (queue fill / connection hold / retry amplification / dependency stall / timeout cascade) required per hop |
| C-03 Quantified limits | essential | PASS | Section 1 requires numeric or "unresolvable" with stated reason. Scorecard update after Section 1 explicitly checks: "If C-03 is not yet fully satisfied (any tier lacks a numeric limit), note which tiers are incomplete before continuing." |
| C-04 UX per tier | essential | PASS | Section 4: every Section 1 tier required. Scorecard update after Section 4: "C-04 requires every tier to be present here — flag any tier that appears in Section 1 but not Section 4." |
| C-05 Unprotected burst path | essential | PASS | Section 5 dedicated: entry component, route, specific gap reason |
| C-06 Retry-after handling | recommended | PASS | Section 4: Retry-After presence/absence per tier; ignore-consequence required. Scorecard update tracks C-06 inline. |
| C-07 Cascade failure scenario | recommended | PASS | Section 6 Part B: 3+ named tiers, causal link at each step, compounded throughput/error-rate effect; minimum three tiers |
| C-08 Tier risk ranking | recommended | PASS | Section 6 Part A: tier ranking with blast radius, failure visibility, recovery time estimate for top-ranked tier |
| C-09 Mitigation prescriptions | aspirational | PASS | Section 6 Part C: "for each gap identified (unprotected burst paths, absent Retry-After handling, cascade risk): provide a specific remediation — setting name, API parameter, or implementation pattern. Generic advice does not satisfy this section." Explicitly mirrors rubric pass condition. |
| C-10 Load shape sensitivity | aspirational | PASS | Section 6 Part D: "show that the same total request count produces different throttle outcomes when requests arrive uniformly vs. in bursts. Include at least one numeric comparison (e.g., '100 requests spread over 10 minutes stays under the 12 req/min cap; the same 100 requests in a 30-second burst exceeds it threefold')." Numeric example embedded in instruction. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 2/2
**Composite:** (5/5 × 60) + (3/3 × 30) + (2/2 × 10) = **100**
**Golden:** YES (all essential pass, composite 100 ≥ 80)

---

## V-03 — Phrasing Register: Adversarial Disproof Framing

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|---------|
| C-01 Bottleneck sequencing | essential | PASS | Attempt 1: find the tier whose limit the given volume exceeds; explain why that tier fails first and others do not |
| C-02 Backpressure propagation | essential | PASS | Attempt 2: trace at least two hops; mechanism and observable state required per hop |
| C-03 Quantified limits | essential | PASS | Attempt 1: "the specific rate limit (number + unit — 'limited' is not evidence; a number is)" — explicit rejection of vague language |
| C-04 UX per tier | essential | **FAIL** | No dedicated per-tier UX catalog. Attempt 5 covers UX only for the binding tier's retry-after failure. Other tiers identified in Attempt 1 receive no systematic UX description. Rubric requires "each throttle tier identified has a corresponding UX description. No tier is named without a consequence." The adversarial structure focuses on finding failures rather than cataloging user-visible outcomes per tier. |
| C-05 Unprotected burst path | essential | PASS | Attempt 3 dedicated: entry component, route, specific gap reason (no connector policy / exempt trigger / gateway bypass / no concurrency cap) |
| C-06 Retry-after handling | recommended | PASS | Attempt 5 dedicated: presence/absence, failure mode if absent, what user sees when failure fires |
| C-07 Cascade failure scenario | recommended | PASS | Attempt 4: 3+ tiers in named cascade, causal link at each step, compounded throughput/error-rate effect. Generic claims excluded. |
| C-08 Tier risk ranking | recommended | PARTIAL | Verdict ranks "identified failures by blast radius" — covers highest-risk failure mode with impact, likelihood, and recovery. However, framing is failure-modes not tiers; not all tiers in the Attempt 1 inventory are guaranteed to appear in the ranking. Partial credit: highest-risk tier identified with rationale, but full tier ranking not assured. |
| C-09 Mitigation prescriptions | aspirational | FAIL | No mitigation section. Adversarial framing focuses on proving failures exist, not remediating them. |
| C-10 Load shape sensitivity | aspirational | FAIL | Not present in any attempt. |

**Essential:** 4/5 (C-04 FAIL) | **Recommended:** 2.5/3 (C-08 PARTIAL = 0.5) | **Aspirational:** 0/2
**Composite:** (4/5 × 60) + (2.5/3 × 30) + (0/2 × 10) = 48 + 25 + 0 = **73**
**Golden:** NO (C-04 essential fails)

**Root cause of C-04 failure:** Adversarial disproof structure is organized around five attack vectors (binding limit, propagation, burst path, cascade, retry-after), not around a per-tier enumeration. Tiers appear as evidence in attacks but are never systematically cataloged with UX consequences. The framing creates excellent C-05 and C-07 coverage but trades off C-04.

---

## V-04 — Lifecycle Emphasis: Numbered Checklist with Completion Gates

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|---------|
| C-01 Bottleneck sequencing | essential | PASS | Task 2: "Completion condition: A single tier is named as the binding constraint with a causal reason grounded in the Task 1 data." Must complete before Task 3 opens. |
| C-02 Backpressure propagation | essential | PASS | Task 3: "Completion condition: At least two hops are traced from the binding constraint, each with a named mechanism and an observable effect." |
| C-03 Quantified limits | essential | PASS | Task 1: "Completion condition: Every tier has a numeric rate limit OR is marked 'unresolvable' with a stated reason. No tier has a vague label ('limited', 'throttled') in place of a number." |
| C-04 UX per tier | essential | PASS | Task 4 Part 1: "Completion condition (C-04): Every Task 1 tier has a row in this catalog. No tier may be omitted. If a tier produces no user-visible signal, state that explicitly." |
| C-05 Unprotected burst path | essential | PASS | Task 5: entry component, route, specific gap reason. If no path exists, named controls at every entry point required. |
| C-06 Retry-after handling | recommended | PASS | Task 4 Part 2: "Completion condition (C-06): The binding constraint tier from Task 2 has an explicit Retry-After assessment: present/absent, and the consequence of absence or mishandling stated." Criterion name explicit in task label. |
| C-07 Cascade failure scenario | recommended | PASS | Task 7: "Completion condition: Three or more tiers appear in the cascade, with explicit causal links at each step. Generic claims ('could cascade') do not satisfy this task." |
| C-08 Tier risk ranking | recommended | PASS | Task 6: "Completion condition: All Task 1 tiers appear in the ranking with stated rationale." |
| C-09 Mitigation prescriptions | aspirational | FAIL | No task covers mitigation prescriptions. Gap identification in Tasks 4-5 has no corresponding remediation task. |
| C-10 Load shape sensitivity | aspirational | FAIL | No task covers load shape sensitivity. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 0/2
**Composite:** (5/5 × 60) + (3/3 × 30) + (0/2 × 10) = **90**
**Golden:** YES (all essential pass, composite 90 ≥ 80)

---

## V-05 — Combined: Inertia Framing + Risk-First Role Sequence

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|---------|
| C-01 Bottleneck sequencing | essential | PASS | Role 4 Part A: binding tier, numeric limit exceeded, causal reason this tier binds before others |
| C-02 Backpressure propagation | essential | PASS | Role 4 Part B: minimum 2 hops, mechanism and observable effect per hop |
| C-03 Quantified limits | essential | PASS | Role 3: numeric or "unresolvable" required. Inertia preamble ("the tier whose limit nobody measured at 5x nominal") primes for numeric specificity. Role 1 requires numeric limits as burst path components are traversed. |
| C-04 UX per tier | essential | PASS | Role 5: "For every tier from Role 3" — error code/signal, run-history visibility, ignore-Retry-After consequence. "Every Role 3 tier must appear here. No tier may be omitted." |
| C-05 Unprotected burst path | essential | PASS | Role 1 dedicated; inertia preamble names "the burst path that was never rate-limited because no one tested at the volume where it fires" — primes the model to search for exactly this gap |
| C-06 Retry-after handling | recommended | PASS | Role 2 dedicated; inertia preamble names "the missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry storm" — primes for specificity. Presence/absence, failure mode, and first observable symptom all required. |
| C-07 Cascade failure scenario | recommended | PASS | Role 6 Part B: 3+ named tiers, causal link at each step, compounded throughput/error-rate effect. Generic claims excluded. |
| C-08 Tier risk ranking | recommended | PASS | Role 6 Part A: rank all Role 3 tiers by business risk; top-ranked tier requires blast radius, failure visibility, recovery time |
| C-09 Mitigation prescriptions | aspirational | FAIL | Role 6 Part C (Inertia Exposure Summary) asks what staging didn't exercise and what production exposes — this is discovery framing, not remediation. No specific configuration, pattern, or API-level fix is requested. |
| C-10 Load shape sensitivity | aspirational | FAIL | No load shape sensitivity section. The inertia preamble names burst path failure but does not trigger a same-volume uniform-vs-burst comparison. |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 0/2
**Composite:** (5/5 × 60) + (3/3 × 30) + (0/2 × 10) = **90**
**Golden:** YES (all essential pass, composite 90 ≥ 80)

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-02 Scorecard | 5/5 | 3/3 | 2/2 | **100** | YES |
| V-01 Risk-First | 5/5 | 3/3 | 0/2 | **90** | YES |
| V-04 Checklist | 5/5 | 3/3 | 0/2 | **90** | YES |
| V-05 Inertia+Risk | 5/5 | 3/3 | 0/2 | **90** | YES |
| V-03 Adversarial | 4/5 | 2.5/3 | 0/2 | **73** | NO |

**Ranking:** V-02 > V-01 = V-04 = V-05 > V-03

---

## Excellence Signals — V-02

Four patterns drove V-02 to 100 while the other golden variations plateaued at 90:

**1. Criterion list visible in the prompt header (not just embedded in sections)**
All 10 criteria are listed at the top of the prompt under "Rubric criteria to track." The model sees the complete target before starting Section 1. This creates a metacognitive anchor that suppresses silent criterion elision — the model knows what it hasn't yet addressed throughout every section.

**2. Running scorecard with evidence requirement after each section**
After each analytical section, the model must update a scorecard by naming the specific output element that satisfies each criterion. This self-correction loop catches C-03 elision (vague limits) at the point of production, before later sections compound the omission. It also catches C-04 tier-omission in real time rather than at output review.

**3. "Generic advice does not satisfy this section" language for C-09**
Section 6 Part C uses the exact language: "setting name, API parameter, or implementation pattern. Generic advice does not satisfy this section." This blocks the most common C-09 failure mode (aspirational criterion + hedging pressure = "add retry logic") before it happens.

**4. Numeric example embedded in C-10 instruction**
Section 6 Part D models the exact expected output: "'100 requests spread over 10 minutes stays under the 12 req/min cap; the same 100 requests in a 30-second burst exceeds it threefold'." For the aspirational criterion most vulnerable to hedging ("this may depend on..."), an embedded numeric example eliminates ambiguity about what constitutes a passing answer.

---

## V-03 Failure Analysis

C-04 (UX per tier) fails in V-03 because adversarial disproof is organized around attack vectors, not tier enumeration. The five attempts build a disproof case — they do not build a catalog. Tiers appear as evidence within attacks (Attempt 1 identifies limits, Attempts 3-4 name tiers in paths and cascades) but no attempt requires systematic "for every tier: what does the user see?" coverage. The explicit per-tier UX catalog in V-01, V-02, V-04, V-05 (each has a dedicated role/section/task) is structurally absent from V-03. This is the core architectural limitation of adversarial framing for rubric criteria that require coverage rather than correctness.

---

## Round 2 Direction

The three-way tie at 90 (V-01, V-04, V-05) signals that structural enforcement of C-01 through C-08 is solved. The gap is uniformly C-09 and C-10. Round 2 variations should test:
- Whether adding a mitigation prescriptions section to V-05's inertia role structure produces C-09 without degrading C-05/C-06 (the risk-first gains)
- Whether Section 6 Part C/D from V-02 transplanted into V-01 or V-04's structure produces 100 without requiring the full scorecard overhead
- What happens when C-10 is enforced via a pre-committed volume band table rather than a prose instruction

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["embedded numeric example in criterion instruction models exact expected output — blocks hedging on quantified aspirational criteria", "visible criterion list in prompt header creates metacognitive anchor that suppresses elision across all sections"]}
```
