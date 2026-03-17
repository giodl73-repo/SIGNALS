# /quest:score — flow-lifecycle R6

## Scoring Framework

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-26 | 0.556 | 10 |
| **Total** | | | **100** |

Golden threshold: all 5 essential pass + composite ≥ 80.

---

## V-01 — C-26 Isolation: Merged Evidence Axes

**Hypothesis**: C-24 PASS, C-25 PASS, C-26 FAIL.

### Essential

| ID | Score | Evidence note |
|----|-------|---------------|
| C-01 | PASS (12) | State table requires named entry condition + labeled exits on every row |
| C-02 | PASS (12) | SECTION A min-2 per phase × multiple phases → 4+ exception flows |
| C-03 | PASS (12) | Role Registry enforces domain-specific names; Decision Supplement Block requires R-ID at every decision |
| C-04 | PASS (12) | B-01 + B-02 blocks with Cause + Downstream Impact fields present |
| C-05 | PASS (12) | TERMINAL type declared; exits must name destination or TERMINAL |

**Essential: 60/60**

### Recommended

| ID | Score | Evidence note |
|----|-------|---------------|
| C-06 | PASS (10) | Parallel Work Streams section with fork type + join condition |
| C-07 | PASS (10) | EC-01–EC-03 with Trigger + Why Problematic + Correct Response |
| C-08 | PASS (10) | Decision Supplement Block requires Condition + Owner + Branch YES/NO + Fallback (explicitly "required — do not omit") |

**Recommended: 30/30**

### Aspirational

| ID | Score | Evidence note |
|----|-------|---------------|
| C-09 | PASS | Cross-process interactions table present |
| C-10 | PASS | SLA ANALYSIS with AT-RISK flags + B-NN Bottleneck Cross-Ref column |
| C-11 | PASS | Fallback field required in Decision Supplement Block |
| C-12 | PASS | Role Registry with Anti-Generic Check column precedes all tracing |
| C-13 | PASS | EX-1A/B scoped to Phase 1; EX-2A/B scoped to Phase 2 |
| C-14 | PASS | SLA table Bottleneck Cross-Ref column ties AT-RISK rows to B-NN |
| C-15 | PASS | SECTION A precedes SECTION B within every phase block |
| C-16 | PASS | CHAIN STATUS verifies Forward (SLA→B) and Backward (B→SLA) |
| C-17 | PASS | EX-NN blocks use labeled sub-fields (Trigger, Trace, Handling Role, Terminal, Why Problematic) |
| C-18 | PASS | SECTION A / SECTION B ordinal labels encode exception-first as named constraint |
| C-19 | PASS | B-01 Evidence field present; preamble says "each B-NN block must include" |
| C-20 | PASS | `## CHAIN STATUS` dedicated section; CHAIN STATUS: [CLOSED/OPEN] is first output element |
| C-21 | PASS | SECTION A blocks satisfy C-13 + C-15 + C-17 through single structural decision |
| C-22 | PASS | Preamble has concrete example `S-05: Credit Hold Review -- AT-RISK, causal source: B-01` + fail condition sentence |
| C-23 | PASS | Anti-embedding in preamble; CHAIN STATUS section opens with STRUCTURAL CONSTRAINT block |
| C-24 | PASS | Concrete named example in preamble AND in B-01 per-block hint (`e.g., S-05: Credit Hold Review...`) |
| C-25 | PASS | Anti-embedding in preamble AND as opening constraint of `## CHAIN STATUS` section |
| C-26 | **FAIL** | Preamble merges format spec + fail condition into one prose sentence; no `Required format:` / `Fail condition:` labels — axes bundled, not independently labeled |

**Aspirational: 17/18 × 10 = 9.44**

**V-01 Total: 99.44**

---

## V-02 — C-26 Isolation: Separated Labeled Evidence Axes

Single axis change from V-01: Evidence field instruction uses `Required format:` and `Fail condition:` as explicitly labeled, visually distinct sub-fields in both preamble and per-block hint.

| ID | Score | Change |
|----|-------|--------|
| C-26 | **PASS** | `Required format:` and `Fail condition:` now separately labeled → each is an independent verification target |

All other criteria: identical to V-01.

**Aspirational: 18/18 × 10 = 10.00**

**V-02 Total: 100**

---

## V-03 — C-24 Isolation: Preamble-Only Concrete Example

Per-block hint reduced to minimal reference ("using the format above") — no repeated concrete named domain example in per-block. Preamble retains full format contract. Labeled axes (C-26) present.

| ID | Score | Evidence note |
|----|-------|---------------|
| C-22 | PASS | Preamble has concrete filled example + fail condition — format contract present |
| C-24 | **FAIL** | Per-block hint says "using the format above" only; concrete named example (`S-05: Credit Hold Review...`) not repeated at per-block location |
| C-25 | PASS | Dual anti-embedding unchanged |
| C-26 | PASS | Labeled axes present in preamble; C-26 does not depend on C-24 |

All other criteria: PASS. C-24 failure is isolated — no downstream cascade.

**Aspirational: 17/18 × 10 = 9.44**

**V-03 Total: 99.44**

---

## V-04 — C-24 Isolation: Per-Block Concrete Example Only, Preamble Bracket Template

Preamble uses bracket template `[State name -- S-ID]: AT-RISK, causal source: B-[ID]` — no concrete filled-in domain example. Per-block has concrete example. Labeled axes assumed present.

**C-22 failure triggers dependency cascade:**

| ID | Score | Evidence note |
|----|-------|---------------|
| C-22 | **FAIL** | Preamble has bracket template only — no concrete named domain example (e.g., `S-05: Credit Hold Review...`) as required by format contract |
| C-24 | **FAIL** | Fails by C-24→C-22 dependency: preamble location lacks concrete named example regardless of per-block |
| C-26 | **FAIL** | Fails by C-26→C-22 dependency: C-26 cannot pass when C-22 fails; labeled axes in per-block alone do not satisfy the criterion |

Note: V-04 hypothesis stated "fails C-22, C-24 by dependency" but does not mention C-26. The dependency chain C-26→C-22 makes C-26 a third casualty. This is a cascade depth the variation design underestimated.

All other criteria: PASS.

**Aspirational: 15/18 × 10 = 8.33**

**V-04 Total: 98.33**

---

## V-05 — Full R6 Synthesis

Dual-location (preamble AND per-block) for concrete example + labeled axes + dual anti-embedding, all operating as a unified instructional system.

| ID | Score | Evidence note |
|----|-------|---------------|
| C-22 | PASS | Preamble: concrete named example + explicit fail condition |
| C-24 | PASS | Concrete named example at preamble AND per-block, both with labeled axes |
| C-25 | PASS | Anti-embedding at preamble AND CHAIN STATUS section opening |
| C-26 | PASS | `Required format:` / `Fail condition:` as explicitly labeled sub-fields at both locations |

All criteria: PASS.

**Aspirational: 18/18 × 10 = 10.00**

**V-05 Total: 100**

---

## Summary

| Variation | Essential | Recommended | Aspirational | **Total** | All Essential | Golden |
|-----------|-----------|-------------|--------------|-----------|---------------|--------|
| V-01 | 60 | 30 | 9.44 | **99.44** | YES | YES |
| V-02 | 60 | 30 | 10.00 | **100.00** | YES | YES |
| V-03 | 60 | 30 | 9.44 | **99.44** | YES | YES |
| V-04 | 60 | 30 | 8.33 | **98.33** | YES | YES |
| V-05 | 60 | 30 | 10.00 | **100.00** | YES | YES |

**Rank**: V-02 = V-05 (100) > V-01 = V-03 (99.44) > V-04 (98.33)

---

## Excellence Signals

**Top tier: V-02 and V-05 (tied at 100)**

V-02 establishes that labeled axis separation (C-26) is the precise gap between 99.44 and 100 — confirming prose-merged instructions, even when informationally complete, leave the format contract as a single undifferentiated verification target. A model can satisfy the format spec while silently omitting the fail condition (or vice versa) with no detectable boundary.

V-05 achieves the same binary score as V-02 but encodes a different instructional posture: every enforcement point is redundant *and* labeled. The contrast with V-02 is not measurable at the binary criterion level but predicts robustness under prompt compression or section-skipping model behavior.

**New patterns:**

**Pattern 1 — Labeled axis separation is the discriminating criterion at the 99→100 boundary.** The single criterion separating V-01 (99.44) from V-02/V-05 (100) is C-26. Dual-location and dual anti-embedding were already present in V-01. The inference: at high rubric maturity, the remaining point-loss is almost always a *labeling* failure, not a *content* failure. Merged-prose instructions that contain the right content score lower than labeled instructions that present the same content as independently verifiable sub-fields.

**Pattern 2 — Preamble format contract is cascade-initiating; per-block is true redundancy.** V-03 (per-block degraded) fails only C-24. V-04 (preamble degraded) fails C-22 + C-24 + C-26 via the dependency chain. The preamble is load-bearing — removing its format contract collapses the entire Evidence axis. Per-block placement is a recovery path, not a co-anchor. Future rubric design should assign higher weight to preamble-placement criteria than per-block criteria for the same content.

**Pattern 3 — B-NN scaffold asymmetry creates a C-19 coverage gap.** In the V-01 template, B-01 carries the Evidence field with the required format instruction, but B-02 omits the Evidence field entirely from its scaffold. The preamble says "each B-NN block must include" an Evidence sub-field, but a model following scaffold shape over preamble instruction will satisfy C-19 only for B-01. This asymmetry is not captured by any existing criterion. A future C-19 extension (C-27 candidate) could require the Evidence field to appear in every B-NN scaffold position, not just the first, to close the instructional gap for multi-bottleneck traces.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Labeled axis separation (C-26) is the discriminating criterion at the 99→100 boundary: dual-location and dual anti-embedding were already present in V-01 at 99.44; adding explicit Required-format/Fail-condition labels is the sole step to 100, confirming that prose-merged instructions fail not on content but on independent verifiability", "Preamble format contract is cascade-initiating while per-block is true redundancy: V-03 per-block degradation fails only C-24; V-04 preamble degradation fails C-22 + C-24 + C-26 via dependency chain — the preamble is load-bearing anchor, per-block is recovery path, and rubric design should weight preamble-placement criteria higher than per-block criteria for the same content", "B-NN scaffold asymmetry: B-01 carries the Evidence field example in the template but B-02 omits the field entirely, creating a gap where models following scaffold shape satisfy C-19 only for the first bottleneck block — a potential C-27 candidate requiring Evidence field presence in all B-NN scaffold positions to close multi-bottleneck coverage"]}
```
