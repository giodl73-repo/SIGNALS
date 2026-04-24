## flow-throttle Round 2 — Variation Scoring

**Rubric v2** | Max composite: 110 | Golden threshold: all 5 essential PASS + composite ≥ 80

---

### Criterion Definitions (v2)

| Band | Essential (C-01–C-05, 60 pts) | Recommended (C-06–C-08, 30 pts) | Aspirational (C-09–C-12, 20 pts) |
|------|--|-|-|
| Pass condition | Full structural enforcement | Dedicated section or column | Explicit requirement in prompt |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/4 * 20)`. PARTIAL = 0.5 pass.

---

## V-01 — Source Citation Column in TABLE A

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01: Primary bottleneck + causal reason | **PASS** | Dedicated "BOTTLENECK AND CAUSAL REASON" section explicitly requires Tier-ID, numeric limit exceeded, source doc, and "the causal reason this tier binds before all others" |
| C-02: Backpressure propagation ≥ 2 hops | **PASS** | TABLE B requires Tier-ID, named mechanism (queue-fill / connection-hold / etc.), observable effect; minimum two hops |
| C-03: ≥ 2 throttle tiers with enforcing component | **PASS** | TABLE A with Tier-ID, Component, Scope columns; Binding? enforces single-Y constraint |
| C-04: UX for every tier | **PASS** | TABLE C requires one row per Tier-ID — error code, Retry-After Y/N + value, run history visibility, failure-if-ignored |
| C-05: Unprotected burst path | **PASS** | TABLE D requires ≥ 1 row with entry component, structural gap reason, Tier-IDs bypassed, consequence |
| C-06: Retry-After handling assessed | **PASS** | TABLE C has "Retry-After present? (Y/N)", "Retry-After value", "Failure if Retry-After ignored" per tier |
| C-07: Two-tier cascade | **PASS** | "RISK RANKING AND CASCADE SCENARIO" requires cascade with Tier-IDs, minimum three tiers, business risk ranking |
| C-08: Numeric threshold cited | **PASS** | TABLE A Limit column requires "number + unit"; `unknown [reason]` only if genuinely unconfirmable |
| C-09: Mitigations with tradeoffs | **PARTIAL** | "MITIGATION PRESCRIPTIONS" section requires component + setting + target value + observable outcome; no explicit tradeoff field |
| C-10: Comparative severity ranking | **PASS** | RISK RANKING section requires ranked list by business risk; top tier gets blast radius + failure visibility justification |
| C-11: Threshold sourcing provenance | **PASS** | Source column in TABLE A with concrete passing/failing examples ("Power Automate limits reference — 'Request limits and allocations'" passes; "PA documentation" fails); `not documented` required when limit unknown |
| C-12: Coverage self-verification | **FAIL** | No self-verification section of any kind |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 2.5/4 → 12.5 pts

**Composite: 102.5** | All essential pass: **YES** | Band: **GOLD**

---

## V-02 — Mandatory Terminal Self-Verification

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01: Primary bottleneck + causal reason | **PARTIAL** | Binding? Y/N in tier inventory identifies the tier; no dedicated section requiring the causal reason why it binds before others. RISK RANKING requires blast radius + failure visibility, not binding causality. |
| C-02: Backpressure propagation ≥ 2 hops | **PASS** | BACKPRESSURE section requires Tier-ID, mechanism (queue-fill / etc.), observable effect; minimum two hops |
| C-03: ≥ 2 throttle tiers with enforcing component | **PASS** | THROTTLE TIER INVENTORY with Tier-IDs and component names |
| C-04: UX for every tier | **PASS** | USER EXPERIENCE CATALOG explicitly requires every tier to have error code, Retry-After, run history visibility, failure-if-ignored |
| C-05: Unprotected burst path | **PASS** | UNPROTECTED BURST PATHS section with entry component, route, gap reason, consequence |
| C-06: Retry-After handling assessed | **PASS** | UX section requires Retry-After compliance plus "explicit verdict on whether Retry-After handling is correct" for the binding constraint |
| C-07: Two-tier cascade | **PASS** | RISK RANKING section requires cascade with "minimum three tiers... causal link at each step" |
| C-08: Numeric threshold cited | **PASS** | Tier inventory requires "rate limit value (number + unit)"; `unknown [reason]` only if undocumentable |
| C-09: Mitigations with tradeoffs | **PARTIAL** | MITIGATION PRESCRIPTIONS requires gap + component + exact setting + observable outcome; no tradeoff field |
| C-10: Comparative severity ranking | **PASS** | RISK RANKING section requires ranking by business risk with blast radius + failure visibility justification for top tier |
| C-11: Threshold sourcing provenance | **PARTIAL** | No Source column or source register in tier inventory; the self-verification C-11 line forces the model to acknowledge this gap, earning partial credit per rubric's "honest reporting" rule |
| C-12: Coverage self-verification | **PASS** | COVERAGE SELF-VERIFICATION table pre-prints all 12 criteria by name; COVERED/PARTIAL/NOT COVERED are the only valid values; explicit note that "honest reporting earns credit" |

**Essential:** 4.5/5 → 54 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 3/4 → 15 pts

**Composite: 99** | All essential pass: **NO** (C-01 PARTIAL) | Band: **SILVER**

---

## V-03 — Source-Register Phase Before Tier Inventory

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01: Primary bottleneck + causal reason | **PARTIAL** | Phase 1 Binding? = Y identifies the tier; Phase 4 risk ranking covers blast radius + recovery time but not binding causality. No dedicated bottleneck-and-causal section. |
| C-02: Backpressure propagation ≥ 2 hops | **PASS** | Phase 2A: "trace propagation outward. Minimum two hops. Each hop: Tier-ID, mechanism, observable effect." |
| C-03: ≥ 2 throttle tiers with enforcing component | **PASS** | Phase 1 tier inventory with Tier-IDs, component names, scope |
| C-04: UX for every tier | **PASS** | Phase 3: "For every Phase 1 tier: error code, Retry-After present... No tier omitted." |
| C-05: Unprotected burst path | **PASS** | Phase 2B: "identify any path where burst traffic enters without a rate limit. Entry component, route, specific gap reason." |
| C-06: Retry-After handling assessed | **PASS** | Phase 3 requires Retry-After verdict for binding constraint explicitly |
| C-07: Two-tier cascade | **PASS** | Phase 4 CASCADE SCENARIO: "minimum three tiers. Use Phase 1 Tier-IDs. Name the causal link at each step." |
| C-08: Numeric threshold cited | **PASS** | Phase 1 requires "a number with a unit"; undocumented tiers from Phase 0 get `unknown [undocumented]` |
| C-09: Mitigations with tradeoffs | **PARTIAL** | Phase 4 MITIGATION PRESCRIPTIONS requires four fields; no explicit tradeoff field |
| C-10: Comparative severity ranking | **PASS** | Phase 4 RISK RANKING: "rank all Phase 1 tiers by business risk. Top-ranked tier: blast radius, failure visibility, recovery time." |
| C-11: Threshold sourcing provenance | **PASS** | Phase 0 source register commits sources before numbers; Phase 1 "[Source N]" citation links every limit to a named register entry; numbers without Phase 0 registration are flagged invented |
| C-12: Coverage self-verification | **FAIL** | Completion Check maps to phases (Phase 0–4 completeness), not to C-01 through C-12 by name. Criterion requires the section to "name each criterion" — phase-level reporting does not satisfy this. |

**Essential:** 4.5/5 → 54 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 2.5/4 → 12.5 pts

**Composite: 96.5** | All essential pass: **NO** (C-01 PARTIAL) | Band: **SILVER**

---

## V-04 — Combined: Source Column + Terminal Self-Verification

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01: Primary bottleneck + causal reason | **PASS** | Dedicated "BOTTLENECK AND CAUSAL REASON" section (preserved from V-01) requires Tier-ID, numeric limit, source document, and "the causal reason this tier binds first" |
| C-02: Backpressure propagation ≥ 2 hops | **PASS** | TABLE B with Tier-ID From, mechanism vocabulary, observable effect; minimum two hops |
| C-03: ≥ 2 throttle tiers with enforcing component | **PASS** | TABLE A with Tier-ID, Component, Scope; Binding? at-most-one-Y constraint |
| C-04: UX for every tier | **PASS** | TABLE C one row per Tier-ID — error code, Retry-After, run history visibility, failure-if-ignored |
| C-05: Unprotected burst path | **PASS** | TABLE D with structural gap reason requirement; minimum one row |
| C-06: Retry-After handling assessed | **PASS** | TABLE C Retry-After columns per tier |
| C-07: Two-tier cascade | **PASS** | "RISK RANKING AND CASCADE SCENARIO" with cascade from binding constraint, minimum three tiers, Tier-IDs |
| C-08: Numeric threshold cited | **PASS** | TABLE A Limit column requires number + unit; Source column enforces attribution |
| C-09: Mitigations with tradeoffs | **PARTIAL** | "MITIGATION PRESCRIPTIONS" requires specific component + setting/parameter + target value + observable outcome; tradeoff field not explicitly required |
| C-10: Comparative severity ranking | **PASS** | RISK RANKING section with blast radius + failure visibility + recovery time justification for top tier |
| C-11: Threshold sourcing provenance | **PASS** | Source column in TABLE A with strong concrete examples and explicit failing examples ("PA documentation", "connector reference" named as insufficient); `not documented` required when limit unknown |
| C-12: Coverage self-verification | **PASS** | COVERAGE SELF-VERIFICATION table pre-prints all 12 criteria; COVERED/PARTIAL/NOT COVERED vocabulary; "Honest reporting earns credit. An output that marks a criterion NOT COVERED and explains why outscores one that silently omits it." |

**Essential:** 5/5 → 60 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 3.5/4 → 17.5 pts

**Composite: 107.5** | All essential pass: **YES** | Band: **GOLD**

---

## V-05 — Full Integration (Source Register + Inertia + Burst/Uniform + Mitigation + Self-Check)

| Criterion | Status | Evidence |
|-----------|--------|---------|
| C-01: Primary bottleneck + causal reason | **PARTIAL** | Phase 1 Binding? = Y identifies the tier; Phase 4 risk ranking gives blast radius + failure visibility for top-ranked tier. The causal reason "this tier binds before all others at the given volume" is not structurally required in any phase. V-05's phase structure replaced the dedicated BOTTLENECK section. |
| C-02: Backpressure propagation ≥ 2 hops | **PASS** | Phase 2A: "trace propagation outward. Each hop: Tier-ID or component, mechanism (queue-fill / connection-hold / etc.), observable effect. Minimum two hops." |
| C-03: ≥ 2 throttle tiers with enforcing component | **PASS** | Phase 1 TABLE with Tier-ID, Component, Scope, Binding? |
| C-04: UX for every tier | **PASS** | Phase 3: "For every Phase 1 tier... No tier omitted." |
| C-05: Unprotected burst path | **PASS** | Phase 2B with entry component, route, structural gap reason; motivated by inertia framing ("find it") |
| C-06: Retry-After handling assessed | **PASS** | Phase 3 requires explicit verdict on binding constraint Retry-After handling |
| C-07: Two-tier cascade | **PASS** | Phase 4: "trace one concrete cascade... Tier-IDs, causal link at each step, compounded effect. Minimum three tiers." |
| C-08: Numeric threshold cited | **PASS** | Phase 1 requires number + unit; non-Phase-0-registered numbers flagged as invented |
| C-09: Mitigations with tradeoffs | **PARTIAL** | Phase 5 requires four fields (Gap, Component, Specific change, Expected outcome); gate condition enforces completeness; no tradeoff field. Inertia framing motivates specificity but not tradeoffs explicitly. |
| C-10: Comparative severity ranking | **PASS** | Phase 4 risk ranking with blast radius + failure visibility + recovery time for top tier; self-check C-10 row maps to burst/uniform distinction also covered by Phase 1 BURST column |
| C-11: Threshold sourcing provenance | **PASS** | Phase 0 source register; Phase 1 `Source ref` column citing "[N]"; inertia preamble explicitly names invented thresholds as the third failure mode; strong structural enforcement |
| C-12: Coverage self-verification | **PASS** | COVERAGE SELF-VERIFICATION table pre-prints all 12 criteria; same honest-reporting language as V-04 |

**Essential:** 4.5/5 → 54 pts | **Recommended:** 3/3 → 30 pts | **Aspirational:** 3.5/4 → 17.5 pts

**Composite: 101.5** | All essential pass: **NO** (C-01 PARTIAL) | Band: **SILVER**

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Composite | Band |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|------|
| V-01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | FAIL | **102.5** | GOLD |
| V-02 | PARTIAL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PARTIAL | PASS | **99** | SILVER |
| V-03 | PARTIAL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | FAIL | **96.5** | SILVER |
| V-04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | PASS | **107.5** | GOLD |
| V-05 | PARTIAL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | PASS | PASS | PASS | **101.5** | SILVER |

**Rank:** V-04 > V-01 > V-05 > V-02 > V-03

---

## Excellence Signals from V-04

**1. Dual enforcement at different structural positions.**
C-11 is enforced at TABLE A write time (Source column adjacent to Limit); C-12 is enforced at terminal position (self-check section after all content). The two mechanisms address different criteria at different moments in the output — no crowding, no token budget conflict. This is the core V-04 design insight.

**2. Preserved BOTTLENECK AND CAUSAL REASON section is load-bearing for C-01.**
V-02, V-03, and V-05 all migrated to phase-based structures and implicitly assumed the binding constraint would be named in phase output. None got C-01 PASS. V-04 preserved the dedicated section from R1's V-01, which explicitly requires "the causal reason this tier binds before all others." Phase-gated structures that subsume this into risk ranking fail C-01 because risk rank ≠ binding causality at the given volume.

**3. Source column with concrete passing/failing examples beats generic "cite your sources."**
V-04 (and V-01) names "PA documentation" and "connector reference" as failing examples — not just too-vague-to-verify but specifically called out as invalid. This anchors the column at write time rather than relying on the model to judge adequacy retrospectively.

**4. Honest-reporting incentive in the self-check is structurally reinforced.**
V-04 states: "An output that marks a criterion NOT COVERED and explains why outscores one that silently omits it." This directly counteracts the backfill risk identified in V-02's hypothesis — the model is explicitly told that self-reporting a gap earns more than papering over it.

**Remaining gap across all variations:** C-09 is PARTIAL in every variation. No prompt in Round 2 added an explicit tradeoff field to the mitigation section. Round 3 opportunity: add a fifth mitigation field ("Tradeoff: what does this mitigation cost?") to convert PARTIAL → PASS on C-09 and raise V-04's ceiling from 107.5 → 110.

---

```json
{"top_score": 108, "all_essential_pass": true, "new_patterns": ["dual enforcement at different structural positions — C-11 via Source column at TABLE A write time, C-12 via terminal self-check, neither crowds the other", "preserved BOTTLENECK AND CAUSAL REASON section is load-bearing for C-01 — phase-gate variants that absorb this into risk ranking lose the essential pass", "source column with concrete named failing examples anchors attribution quality at write time"]}
```
