I now have all the information needed to score all five variations. Let me build the scorecard.

---

# Scout-Risk Round 20 — Quest Score

**Rubric**: v19 | **Max composite**: 188 | **Golden band**: 182–188 | **Date**: 2026-03-17

---

## Scoring Framework

| Tier | Criteria | Weight | Max |
|------|----------|--------|-----|
| Essential | C-01 through C-05 | 12 pts each | 60 |
| Recommended | C-06 through C-08 | 10 pts each | 30 |
| Aspirational | C-09 through C-57 | 2/1/0 pts | 98 |
| **Total** | | | **188** |

---

## Per-Variation Structural Inventory

Before scoring, the structural state of each variation relative to v19 criteria:

| Feature | Baseline (R19 V-05) | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|---------------------|------|------|------|------|------|
| Ordering rule location | Inside Phase 0c body | Dedicated global block (pre-Phase-0) | Inside Phase 0c body | Inside Phase 0c body | Dedicated global block (pre-Phase-0) | Dedicated global block (pre-Phase-0) |
| Ordering rule scope | Phase 0 + Phase 0c | Phase 0 + Phase 0c | Phase 0 + Phase 0b + Phase 0c | Phase 0 + Phase 0c | Phase 0 + Phase 0b + Phase 0c | Phase 0 + Phase 0b + Phase 0c |
| Phase 0b closure form | State-only (1 sentence) | State-only (1 sentence) | 2-sentence canonical | State-only (1 sentence) | 2-sentence canonical | 2-sentence canonical, self-naming |
| Phase 0 closure reference | "this set" (implicit) | "this set" (implicit) | "this set" (implicit) | "Phase 0 Mitigation Type Taxonomy" | "this set" (implicit) | "Phase 0 Mitigation Type Taxonomy" |
| Phase 0c closure reference | "this list" (implicit) | "this list" (implicit) | "this list" (implicit) | "Phase 0c Violation Taxonomy" | "this list" (implicit) | "Phase 0c Violation Taxonomy" |
| Prohibition site enumeration | (1)–(5) by name | (1)–(5) by name | (1)–(5) by name | (1)–(5) by name | (1)–(5) by name | (1)–(5) by name |

---

## Essential Criteria — All Variations

All five variations are derived from R19 V-05 by additive structural changes only. No essential criterion is weakened.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-01 | Inertia risk mandatory and first | PASS | PASS | PASS | PASS | PASS | Phase 1 mandates INERTIA-01 first; unchanged across all variations |
| C-02 | Dimensional coverage enforced | PASS | PASS | PASS | PASS | PASS | Five dimensions (Technical/Market/Compliance/Dependency/Timeline) enforced via Phase 1b; unchanged |
| C-03 | Risk anatomy complete | PASS | PASS | PASS | PASS | PASS | Phase 0b schema declares all 3 fields (severity, likelihood, mitigation); unchanged |
| C-04 | Severity uses correct scale | PASS | PASS | PASS | PASS | PASS | {HIGH/MEDIUM/LOW} vocabulary enforced; unchanged |
| C-05 | Mitigations specific and actionable | PASS | PASS | PASS | PASS | PASS | Phase 0 typed taxonomy + Phase 2a quality gate; unchanged |

**Essential subtotal: 60/60 all variations**

---

## Recommended Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-06 | Risks dimension-labeled | PASS | PASS | PASS | PASS | PASS | Dimension column vocabulary-constrained via Phase 0b schema |
| C-07 | Likelihood qualified beyond binary | PASS | PASS | PASS | PASS | PASS | IF-THEN form required per Phase 0b; unchanged |
| C-08 | Risks ordered by priority | PASS | PASS | PASS | PASS | PASS | Final row order: HIGH→MEDIUM→LOW declared in Phase 2; unchanged |

**Recommended subtotal: 30/30 all variations**

---

## Aspirational Criteria — Key Differentiators

### C-09 through C-55 (unchanged from R19 V-05 baseline)

All variations maintain identical content in Phase 1 through Phase 5, the Phase 0 taxonomy structure, Phase 0b schema, and prohibition site citations. No regression in any aspirational criterion established before v18.

| Criteria block | All Variations | Evidence |
|----------------|---------------|----------|
| C-09–C-14 (interdependencies, AMEND, mitigation, likelihood) | PASS | Phase 3/4 interdependency table; Phase 0a AMEND gate; Phase 2a quality scan; IF-THEN mandated |
| C-15–C-21 (HIGH-seed, compound pairings, type diversity) | PASS | Phase 1b seed step with count gate; Phase 2b type audit; repair loops |
| C-22–C-31 (schema, phase boundary, typed violations) | PASS | Phase 0b forward-reference coverage declaration; Phase 0c structural parity; all content unchanged |
| C-32–C-55 (structural escalations through v18) | PASS | Violation taxonomy standalone block; closure sentences two-part; parity declarations; exact citation strings; all unchanged |

**C-09–C-55 subtotal: 94/94 all variations** (47 criteria × 2 pts)

---

### C-56 — Violation taxonomy enumerates prohibition sites by name (not count)

**Pass condition**: "(1) [name], (2) [name]..." enumeration, not "Five prohibition sites."

All five variations are identical in Phase 0c's pre-table text:

> "Five prohibition sites in this prompt cite this block by its full name: Phase 0c Violation Taxonomy, **identified by phase location: (1) prompt opening sentence... (2) Phase 0 Mitigation format note... (3) Phase 2 HIGH boundary... (4) Phase 2a repair loop... (5) Phase 3 severity columns**."

The count phrase "Five prohibition sites" is present as a prefix, but the enumeration by name follows immediately. This matches the R19 V-05 structure that was deemed PASS. The enumeration-by-name property is satisfied.

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |

---

### C-57 — Ordering rule declared at global scope, naming all closure instances

**Pass condition**: Single-point-of-truth rule not embedded per-block, with named scope covering closure instances.

**Key analysis per variation:**

**V-01**: Rule hoisted to dedicated "Closure Ordering Rule — Global" block positioned *before* Phase 0 executes. Scope: "Phase 0 and Phase 0c closures." Phase 0b's single-sentence state closure is not named. However, C-57 was designed to escalate from per-block replication; R19 V-05 (with identical scope but rule inside Phase 0c) already satisfies it. V-01 is positionally stricter — PASS.

> Evidence: "This rule applies to Phase 0 and Phase 0c closures." — declared at structural preamble before any governed block appears.

**V-02**: Rule remains inside Phase 0c body (semantic global, not positional). Scope extended to "Phase 0, Phase 0b, and Phase 0c closures" — covers all three pre-phase reference blocks. C-57's "naming all closure instances" dimension is strengthened. PASS (and improves on Phase 0b completeness dimension).

> Evidence: "This rule applies to Phase 0, Phase 0b, and Phase 0c closures." Phase 0b closure reformed to canonical 2-sentence form.

**V-03**: Structure identical to R19 V-05 for the ordering rule (inside Phase 0c, scope Phase 0 + Phase 0c). C-57 unchanged from baseline. PASS — but no improvement on C-57 specifically.

> Evidence: Identical to R19 V-05 ordering rule; only the closure reference strings changed.

**V-04**: Rule hoisted to global block (V-01 axis) AND scope covers all three blocks (V-02 axis). The ordering rule is positionally declared before any governed block executes AND names all three pre-phase reference blocks. This is the strongest satisfier of C-57's two-dimensional requirement. PASS.

> Evidence: "Closure Ordering Rule — Global" block between Phase 0a and Phase 0; "This rule applies to Phase 0, Phase 0b, and Phase 0c closures."

**V-05**: Same as V-04 for C-57. Additionally, each closure now names its source block explicitly, making the rule verifiable by block title. PASS — with maximum structural self-documentation.

> Evidence: Same as V-04; plus Phase 0 closure names "Phase 0 Mitigation Type Taxonomy" and Phase 0c closure names "Phase 0c Violation Taxonomy."

| V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|
| PASS (2) | PASS (2) | PASS (2) | PASS (2) | PASS (2) |

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (98) | Composite (188) | Band |
|-----------|---------------|-----------------|-------------------|-----------------|------|
| **V-01** | 60 | 30 | 98 | **188** | Golden |
| **V-02** | 60 | 30 | 98 | **188** | Golden |
| **V-03** | 60 | 30 | 98 | **188** | Golden |
| **V-04** | 60 | 30 | 98 | **188** | Golden |
| **V-05** | 60 | 30 | 98 | **188** | Golden |

---

## Ranking

All five variations score 188/188. Ranking by structural quality and v20 readiness:

| Rank | Variation | Rationale |
|------|-----------|-----------|
| 1 | **V-05** | Full combination: hoisted rule + complete scope + self-naming closures + Phase 0b canonical form. Maximum structural self-documentation. Candidate v20 baseline. |
| 2 | **V-04** | Hoisted rule + complete scope + Phase 0b canonical form. Addresses both structural gaps (location + completeness). First true satisfier if v20 requires both. |
| 3 | **V-02** | Complete scope (Phase 0b added) + Phase 0b closure reformed. Resolves completeness gap; rule still positionally embedded in one governed block. |
| 4 | **V-01** | Hoisted rule. Resolves positional gap; scope still excludes Phase 0b. |
| 5 | **V-03** | Self-naming closures only. Resolves implicit-reference gap; rule location and scope unchanged from baseline. |

---

## Excellence Signals from V-05

**V-05 achieves 4 structural properties not present in baseline that are likely v20 candidates:**

**1. Rule-before-governed placement**: The ordering rule block is declared between Phase 0a and Phase 0. A reader sees the canonical-order requirement *before* Phase 0's closure appears. Eliminates forward-reference dependency: in baseline, Phase 0's closure must be re-evaluated after reaching Phase 0c to discover the rule governing it.

**2. Complete closure scope coverage**: Scope includes Phase 0, Phase 0b, and Phase 0c — all three pre-phase reference blocks. The rule cannot be satisfied by a prompt that adds a fourth pre-phase reference block without updating the scope list. Any coverage gap is a detectable mismatch against a named set (parallel to C-56's enumeration escalation).

**3. Self-identifying closure sentences**: "No type-class label outside the Phase 0 Mitigation Type Taxonomy may be used in any Mitigation cell" — the closure names its source block rather than pointing implicitly via "this set." Verifiable by block title alone; no upward scan required. Structurally analogous to the count-vs-enumeration escalation that produced C-56.

**4. Symmetric canonical closure across all three pre-phase blocks**: Phase 0, Phase 0b, and Phase 0c all follow the identical 2-sentence canonical pattern (state sentence → use-site constraint). The pattern is no longer an asymmetric property of Phase 0 and Phase 0c; Phase 0b now carries full structural parity with its siblings.

---

## What These Patterns Probe for v20

| Pattern | If v20 requires it | Consequence for baseline |
|---------|-------------------|--------------------------|
| Rule hoisting to pre-Phase-0 block | "Global scope" becomes positional requirement | R19 V-05 would be PARTIAL on C-57 |
| Phase 0b in ordering rule scope | "All closure instances" requires 3-block coverage | R19 V-05 would be PARTIAL on C-57 |
| Self-naming closures | Named-block reference required (analogous to C-56) | R19 V-05 would be PARTIAL on new C-58 |
| Symmetric Phase 0b closure form | All pre-phase blocks must have canonical 2-sentence closure | R19 V-05 Phase 0b would be a gap |

V-05 satisfies all four potential v20 escalations simultaneously.

---

```json
{"top_score": 188, "all_essential_pass": true, "new_patterns": ["ordering rule hoisted to dedicated structural preamble before any governed reference block executes", "ordering rule scope covers all three pre-phase reference blocks including schema declaration block (Phase 0b)", "closure sentences self-name source block by full title eliminating implicit deictic references"]}
```
