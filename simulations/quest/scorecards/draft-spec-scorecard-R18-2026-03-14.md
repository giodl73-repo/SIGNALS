# /quest:score — draft-spec — Round 18 — v17 Rubric

## Scoring Framework

**Formula**: `(E/5×60) + (R/3×30) + (A/39×85)` · Fixed denominator = 39

---

## Criterion Baseline — All Variations

**Essential (C-01 through C-05)** — PASS for all five variations

All variations explicitly maintain the five structural invariants listed in the variate document:

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-01 | Five numbered phases 0–4 in prescribed order; sub-phase in V-05 does not displace | PASS | PASS | PASS | PASS | PASS |
| C-02 | [SCOUT-STATUS-TABLE] 7 rows in Phase 0 named as invariant | PASS | PASS | PASS | PASS | PASS |
| C-03 | [PM-COVERAGE-TABLE] with Waiver Status column named as invariant | PASS | PASS | PASS | PASS | PASS |
| C-04 | [IG-REGISTER]+[ID-REGISTER] ≥2 IG-IDs named as invariant | PASS | PASS | PASS | PASS | PASS |
| C-05 | Five guided sections Phase 3 in order named as invariant | PASS | PASS | PASS | PASS | PASS |

**Recommended (C-06 through C-08)** — PASS for all five variations

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| C-06 | All fallback branches A/B-1/B-2/B-3/B-catch named as invariant | PASS | PASS | PASS | PASS | PASS |
| C-07 | VERBATIM RESPONSE blocks in each branch named as invariant | PASS | PASS | PASS | PASS | PASS |
| C-08 | Three gate tokens defined; C-08 is additive — [STRATEGY-SCOPE-SEAL] in V-05 does not displace existing three | PASS | PASS | PASS | PASS | PASS |

---

## Aspirational Criteria — Baseline 27 (C-09 through C-35)

These 27 criteria do not depend on extension clusters. All pass for all variations — role ordering within Phase 1 (V-01), column pre-printing (V-02), phrasing register (V-03), inertia framing (V-04), and full extension (V-05) do not alter the structural elements these criteria check.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Waiver Status structural element | PASS | PASS | PASS | PASS | PASS |
| C-10 Waiver propagation rule | PASS | PASS | PASS | PASS | PASS |
| C-11 Condition 1 / Condition 2 distinct | PASS | PASS | PASS | PASS | PASS |
| C-12 C1 without C2 = invalid | PASS | PASS | PASS | PASS | PASS |
| C-13 Waiver chain closure (3 nodes) | PASS | PASS | PASS | PASS | PASS |
| C-14 Risk amplification threshold (2 triggers) | PASS | PASS | PASS | PASS | PASS |
| C-15 AMPLIFIED dual sub-slot format | PASS | PASS | PASS | PASS | PASS |
| C-16 Partial-population structural fail rule | PASS | PASS | PASS | PASS | PASS |
| C-17 PM-CONTRACT-SEAL INVALID IF (both deps) | PASS | PASS | PASS | PASS | PASS |
| C-18 Phase 2 blocked names PM-CONTRACT-SEAL | PASS | PASS | PASS | PASS | PASS |
| C-19 Phase 3 blocked names both tokens | PASS | PASS | PASS | PASS | PASS |
| C-20 SPEC-DRAFT-COMPLETE INVALID IF (seal deps) | PASS | PASS | PASS | PASS | PASS |
| C-21 Cross-namespace signal (location 1 of 2) | PASS | PASS | PASS | PASS | PASS |
| C-22 Cross-namespace signal (location 2 of 2) | PASS | PASS | PASS | PASS | PASS |
| C-23 SPEC-DRAFT-COMPLETE cross-namespace both locs | PASS | PASS | PASS | PASS | PASS |
| C-24 Contradiction scan named range | PASS | PASS | PASS | PASS | PASS |
| C-25 Active inspection guard | PASS | PASS | PASS | PASS | PASS |
| C-26 P0 coverage count before narrative | PASS | PASS | PASS | PASS | PASS |
| C-27 Actor→action directives retain PM: form | PASS | PASS | PASS | PASS | PASS |
| C-28 Phase 1 computationally precedes Phase 2 | PASS | PASS | PASS | PASS | PASS |
| C-29 FINDINGS ≥6 named scan items | PASS | PASS | PASS | PASS | PASS |
| C-30 Finding table named types (4 min) | PASS | PASS | PASS | PASS | PASS |
| C-31 Phase 4 ≥2 amendments + section ref | PASS | PASS | PASS | PASS | PASS |
| C-32 Elimination Path R-ID: [R-XX] format | PASS | PASS | PASS | PASS | PASS |
| C-33 C-03 WAIVER elimination path format | PASS | PASS | PASS | PASS | PASS |
| C-34 Condition 2 R-ID WAIVED exemption | PASS | PASS | PASS | PASS | PASS |
| C-35 CASCADE TO annotation Phase 1 | PASS | PASS | PASS | PASS | PASS |

**Baseline total: 27 PASS across all five variations.**

---

## Aspirational Criteria — Extension Clusters (C-36 through C-47)

### STATUS-QUO-SNAPSHOT Cluster (C-36, C-37, C-45, C-46)

**N/A rule**: Inapplicable to templates without [STATUS-QUO-SNAPSHOT]. Fixed denominator unchanged.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-36 Condition 1 extended to [SQS] presence | N/A — no SQS | N/A | N/A | **PASS** — Condition 1 extended: "INVALID IF [SQS], [IG-REGISTER], or [ID-REGISTER] absent" | **PASS** |
| C-37 [SQS] row structural fail rule co-located | N/A | N/A | N/A | **PASS** — named alternative + blank gap → structural fail, co-located with [SQS] row definition | **PASS** |
| C-45 Structural fail rule dual form (neg + pos) | N/A | N/A | N/A | **PASS** — "A row with named alternative but blank Gap is a structural fail. Do not leave Gap blank when Alternative is populated." Both forms co-located | **PASS** |
| C-46 Invalidity rule scoped to "this phase block" | N/A | N/A | N/A | **PASS** — Condition 1: "absent from this phase block" scope qualifier present | **PASS** |

---

### Phase 1.5 Cluster (C-38, C-39, C-40, C-47)

**N/A rule**: Inapplicable to templates without a named fractional sub-phase emitting a second pre-Phase-2 gate token.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-38 Multi-token Phase 2 gate (two named deps) | N/A — no Phase 1.5 | N/A | N/A | N/A — Phase 1.5 absent | **PASS** — Phase 2 REQUIRES: [PM-CONTRACT-SEAL] AND [STRATEGY-SCOPE-SEAL]; both named in Phase 2 preamble |
| C-39 Named fractional sub-phase (ordinal + role + seal) | N/A | N/A | N/A | N/A | **PASS** — Phase 1.5 STRATEGY INERTIA SCOPING inserted between Phase 1 and Phase 2; header names ordinal (1.5) and role scope; emits [STRATEGY-SCOPE-SEAL]; C-01 phases unaffected |
| C-40 Gate token INVALID IF cross-refs co-located structural rule by name | N/A | N/A | N/A | N/A — [STRATEGY-SCOPE-SEAL] absent (no Phase 1.5); C-37 alone is insufficient | **PASS** — [STRATEGY-SCOPE-SEAL] INVALID IF: requires [SQS] presence AND names the C-37 structural fail rule within [SQS] block as a precondition |
| C-47 Multi-input ENTER absorbs fractional sub-phase EXIT into chain | N/A | N/A | N/A | N/A | **PASS** — Phase 2 ENTER names both [PM-CONTRACT-SEAL] (Phase 1 EXIT) AND [STRATEGY-SCOPE-SEAL] (Phase 1.5 EXIT); C-44 chain unbroken; multi-input declaration in ENTER block itself |

---

### Ceremony / Style Cluster (C-41, C-42, C-43, C-44)

**No N/A condition** — applicable to all templates.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-41 ENTER/EXIT ceremony at all 5 numbered phases | **FAIL** — Architect-first role ordering does not introduce ceremony blocks; phase body prose only | **FAIL** — pre-printed table stubs do not introduce ceremony; format axis ≠ structure axis | **FAIL** — second-person framing added to transitions but no structural ENTER/EXIT blocks at phase boundaries | **FAIL** — inertia framing adds [SQS] cluster but no ceremony blocks | **PASS** — formal ENTER and EXIT blocks at all five numbered phases; preconditions and emitted tokens declared at boundary level |
| C-42 Second-person frame with preserved actor-directive separation | **FAIL** — no second-person framing in explanatory prose; actor directives only | **FAIL** — table-dominant format does not introduce second-person frame | **PASS** — "You are now entering Phase 2…" across multiple phase transitions; all actor→action directives retain "PM: scan `scout-requirements` →" form (C-27 preserved); three conditions satisfied | **FAIL** — lifecycle/inertia framing does not introduce second-person orientation prose; no multi-phase second-person frame added | **PASS** — second-person framing throughout; actor→action directives unaffected; multi-phase recurrence confirmed |
| C-43 ROLE markers at numbered phase entry points | **FAIL** — Architect acts first in Phase 1 body but no → ROLE: structural marker at phase entry | **FAIL** — column pre-printing does not introduce entry-level ROLE markers | **FAIL** — second-person framing is a prose style; no structural ROLE markers at phase boundaries | **FAIL** — no ROLE markers introduced by SQS cluster | **PASS** — → ROLE: PM at Phase 1 entry; → ROLE: PM + ARCHITECT at Phase 2 entry; markers at phase boundary level, consistent with body directives |
| C-44 Chained ENTER/EXIT transition notation | **FAIL** — C-41 fails; no ENTER/EXIT blocks to chain | **FAIL** — C-41 fails | **FAIL** — C-41 fails; second-person framing does not satisfy chained block requirement | **FAIL** — C-41 fails | **PASS** — Phase 0 EXIT → Phase 1 ENTER → [PM-CONTRACT-SEAL] → Phase 2 ENTER (+ [STRATEGY-SCOPE-SEAL] via C-47) → [INERTIA-ANALYZED] → Phase 3 ENTER → [SPEC-DRAFT-COMPLETE] → Phase 4 ENTER → amendment list; unbroken named chain |

---

## Score Computation

| Variation | Essential (E/5) | Recommended (R/3) | Aspirational (A/39) | Composite |
|-----------|----------------|-------------------|---------------------|-----------|
| V-01 | 5/5 → 60.00 | 3/3 → 30.00 | 27/39 → 58.85 | **148.85** |
| V-02 | 5/5 → 60.00 | 3/3 → 30.00 | 27/39 → 58.85 | **148.85** |
| V-03 | 5/5 → 60.00 | 3/3 → 30.00 | 28/39 → 61.03 | **151.03** |
| V-04 | 5/5 → 60.00 | 3/3 → 30.00 | 31/39 → 67.56 | **157.56** |
| V-05 | 5/5 → 60.00 | 3/3 → 30.00 | 39/39 → 85.00 | **175.00** |

**Workings:**
- 27/39 × 85 = 2295/39 = 58.846… → 58.85
- 28/39 × 85 = 2380/39 = 61.026… → 61.03
- 31/39 × 85 = 2635/39 = 67.564… → 67.56
- 39/39 × 85 = 85.00

**Golden threshold** (all essential PASS ∧ composite ≥ 85): **all five variations pass.**

---

## Ranking

| Rank | Variation | Composite | A-pass |
|------|-----------|-----------|--------|
| 1 | **V-05** Full extension | **175.00** | 39/39 |
| 2 | V-04 STATUS-QUO-SNAPSHOT | 157.56 | 31/39 |
| 3 | V-03 Second-person frame | 151.03 | 28/39 |
| 4= | V-01 Architect-first | 148.85 | 27/39 |
| 4= | V-02 Table-dominant | 148.85 | 27/39 |

---

## Excellence Signals from V-05

V-05 achieves 175/175 — the second perfect score in the draft-spec series (matching R17 V-01). The five extension clusters (SQS, Phase 1.5, ENTER/EXIT ceremony, ROLE markers, second-person frame) combine independently and additively, with no inter-cluster interference.

**What V-05 did that no lower variation did:**

1. **All five extension clusters active simultaneously** — confirms the rubric's N/A/FAIL asymmetry holds at full scale: the 8 previously-N/A criteria (C-36, C-37, C-38, C-39, C-40, C-45, C-46, C-47) and the 4 previously-FAIL ceremony criteria (C-41, C-42, C-43, C-44) all resolve to PASS when the corresponding clusters are introduced.

2. **C-47 chain closure completes at full extension** — Phase 2 ENTER absorbs both Phase 1 and Phase 1.5 EXIT tokens; the named chain from Phase 0 through Phase 4 is unbroken including the fractional sub-phase.

**Are there new structural patterns in R18 not covered by existing criteria?**

| Observation | Disposition |
|-------------|-------------|
| V-01 role ordering is rubric-agnostic | Rubric evaluates structural presence, not intra-phase role sequence — confirmed, not a gap |
| V-02 format (table stubs) is rubric-agnostic | Format axis does not affect criterion presence — confirmed, not a gap |
| V-03 C-42 achievable without C-41 | Independence already encoded in criterion design — confirmed |
| V-04 SQS cluster scores independently of ceremony cluster | Cluster independence already a design property — confirmed |
| V-05 second 175/175 | Rubric stable — no new structural pattern introduced |

**No new criteria emerge from R18.** The rubric remains stable at 47 criteria.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": []}
```
