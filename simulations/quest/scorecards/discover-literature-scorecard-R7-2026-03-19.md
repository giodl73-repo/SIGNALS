---

## discover-literature R7 -- Scorecard

### Scoring Summary

| Rank | Variation | Raw | C-22 | C-21 | C-20 | Differentiator |
|------|-----------|-----|------|------|------|----------------|
| 1 | **V-01** C-22 Baseline | **160** | PASS | PASS | PASS | Minimum-change isolation: confirms R6 V-04 lifecycle tokens satisfy C-22 with explicit unconditional-emission annotations |
| 1 | **V-02** Domain-Named Tokens | **160** | PASS | PASS | PASS | **Critical experiment PASSES**: EVIDENCE PHASE COMPLETE: + MAP PHASE COMPLETE: confirm C-22 token-agnosticism |
| 1 | **V-03** Dense Instrumentation | **160** | PASS | PASS | PASS | Four unconditional lifecycle tokens (all phases); C-22 minimum is a floor, not a ceiling |
| 1 | **V-04** Inertia Front-Loading | **160** | PASS | PASS | PASS | C-22 orthogonal to inertia axis: pre-committed Phase 1 inertia does not affect boundary token emission |
| 1 | **V-05** v7 Ceiling Synthesis | **160** | PASS | PASS | PASS | Two independent C-20 paths + dual typed schemas + inertia front-loading; holistic reference implementation |

**Top score: 160/160. All essential PASS. v7 ceiling reached by all five variations.**

---

### Per-Variation Scoring

#### V-01 -- C-22 Baseline Confirmation

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Inherited from R6 V-04; no structural changes to output phases |
| C-09..C-19 | (same structural profile as R6 V-04) | **PASS** | Dual typed schemas for OBLIGATION A + OBLIGATION B; enforcement contract identical; Phase 2/3 enforcement identical |
| C-18 | Multi-criterion token reuse | **PASS** | PHASE 2 COMPLETE: annotation names C-09 + C-16 with explicit "(C-09 PASS)" and "(C-16 PASS)". PHASE 3 COMPLETE: names C-13 + C-16 with explicit "(C-13 PASS)" and "(C-16 PASS)". Each token covers two distinct criteria. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | PHASE 2 COMPLETE: (a) contextually named, (b) lists C-09 + C-16, (c) "(C-09 PASS). (C-16 PASS)." -- condition (c) met. PHASE 3 COMPLETE: (a) contextually named, (b) lists C-13 + C-16, (c) "(C-13 PASS). (C-16 PASS)." -- condition (c) met. Two distinct tokens. Three distinct criteria (C-09, C-13, C-16). C-20 satisfied via lifecycle path. C-18 PASS (prerequisite met). |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A full typed schema for RECOVERY NOTE:; OBLIGATION B full typed schema for TIER EMPTY:. {field_name}, {title_fragment}, {outcome} verbatim in Phase 2; {tier_name}, {why_no_sources_qualified}, {search_that_would_address_gap} verbatim in Phase 3 tier instructions. C-19 PASS (prerequisite met). |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | PHASE 2 COMPLETE: annotation: "emits unconditionally at the Phase 2 boundary -- every run, whether the threshold was met or not"; annotation names "Phase 2 boundary" explicitly. PHASE 3 COMPLETE: annotation: "emits unconditionally at the Phase 3 boundary -- every run, whether tiers were fully populated or contained empty entries"; annotation names "Phase 3 boundary" explicitly. "Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied." Two named tokens, each naming its phase boundary, each unconditional. C-18 PASS (dependency met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 all PASS (14 x 5 = 70)
**Raw score: 160/160** | All essential pass: YES | v7 ceiling: YES

---

#### V-02 -- Lifecycle Token Vocabulary (Domain-Named Tokens) -- CRITICAL EXPERIMENT

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Domain-named tokens do not affect output structure or phase content |
| C-09..C-19 | (same structural profile as V-01) | **PASS** | Enforcement contract identical; dual typed schemas for OBLIGATION A + OBLIGATION B; TIER ENTRY:/TIER EMPTY: usage unchanged |
| C-18 | Multi-criterion token reuse | **PASS** | EVIDENCE PHASE COMPLETE: annotation: "(C-09 PASS). (C-16 PASS)." -- dual criteria named explicitly. MAP PHASE COMPLETE: annotation: "(C-13 PASS). (C-16 PASS)." -- dual criteria named explicitly. Token names differ from canonical but each covers two criteria. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | EVIDENCE PHASE COMPLETE: satisfies condition (a) named, (b) C-09 + C-16, (c) "(C-09 PASS)/(C-16 PASS)" explicit. MAP PHASE COMPLETE: satisfies same three conditions for C-13 + C-16. Two distinct tokens, three distinct criteria. C-20 is token-agnostic; domain-named tokens qualify identically to PHASE N COMPLETE: names. C-18 PASS. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A and OBLIGATION B dual typed schemas present and unchanged from V-01. C-21 is structure-dependent; token name changes in Phase 2/3 boundary lines do not affect schema block structure. C-19 PASS. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | EVIDENCE PHASE COMPLETE: annotation: "emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces EVIDENCE PHASE COMPLETE:, whether the threshold was met or not"; annotation names "Phase 2 boundary" explicitly. MAP PHASE COMPLETE: annotation: "emits unconditionally at the Phase 3 / literature-mapping boundary"; annotation names "Phase 3 boundary" explicitly. "Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied." C-22 pass condition names no specific token vocabulary; "at least two named tokens" requires labels, not PHASE N COMPLETE: labels specifically. PASS confirms C-22 is token-agnostic. C-18 PASS. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 all PASS (14 x 5 = 70)
**Raw score: 160/160** | All essential pass: YES | v7 ceiling: YES

**Critical experiment result: C-22 PASS. C-22 is confirmed token-agnostic. Domain-named unconditional boundary tokens qualify.**

---

#### V-03 -- Dense Phase Instrumentation (All 4 Phases)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Additional PHASE 1/4 COMPLETE: tokens add structure; all required outputs preserved |
| C-09..C-19 | (same structural profile as V-01) | **PASS** | Dual typed schemas; THRESHOLD NOT MET: and RECOVERY NOTE: annotations by description; contract section identical |
| C-18 | Multi-criterion token reuse | **PASS** | PHASE 2 COMPLETE: "(C-09 PASS). (C-16 PASS)." PHASE 3 COMPLETE: "(C-13 PASS). (C-16 PASS)." Both are explicit dual-criterion tokens. PHASE 1 COMPLETE: annotation notes C-11 compliance checking and C-16; PHASE 4 COMPLETE: annotation notes C-14 + C-16. Four multi-criterion tokens present. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | PHASE 2 COMPLETE: and PHASE 3 COMPLETE: with explicit condition-(c) PASS statements satisfy C-20. Three distinct criteria (C-09, C-13, C-16). C-18 PASS. Additional PHASE 1 COMPLETE: + PHASE 4 COMPLETE: annotations mention criteria by function description rather than explicit C-NN PASS, which is normal C-16 scope. C-20 satisfied by the primary pair. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A + OBLIGATION B full typed schemas present and unchanged. Lifecycle additions do not touch the enforcement contract. C-19 PASS. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | Minimum two tokens met by PHASE 2 COMPLETE: + PHASE 3 COMPLETE: (both explicit "(C-13 PASS). (C-16 PASS)." / "(C-09 PASS). (C-16 PASS)."; both annotated with phase boundary; both unconditional; "C-22 fully satisfied" stated). PHASE 1 COMPLETE: and PHASE 4 COMPLETE: extend the pattern beyond the minimum -- four unconditional lifecycle tokens, all four phase gates instrumented. C-18 PASS. C-22 PASS by both minimum and extension. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 all PASS (14 x 5 = 70)
**Raw score: 160/160** | All essential pass: YES | v7 ceiling: YES

**Additional finding: Full-phase lifecycle instrumentation is achievable without friction. All four phase gates emit unconditional tokens. C-22 minimum (two) is a floor; V-03 demonstrates the ceiling is four.**

---

#### V-04 -- C-22 + Inertia Front-Loading

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Pre-committed inertia scenario adds Phase 1 gate; all required Phase 2-5 outputs preserved |
| C-09..C-19 | (same structural profile as V-01) | **PASS** | Dual typed schemas; contract identical; lifecycle tokens added at Phase 2/3 boundary |
| C-14 | Inertia guard on PROCEED | **PASS** | INERTIA SCENARIO: committed in Phase 1 before any search. Phase 4 is a verification gate: "Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it." INERTIA SCENARIO: and INERTIA RISK: tokens present in Phase 4. Inertia named before any evidence is gathered -- maximum strength for C-14. |
| C-18 | Multi-criterion token reuse | **PASS** | PHASE 2 COMPLETE: "(C-09 PASS). (C-16 PASS)." PHASE 3 COMPLETE: "(C-13 PASS). (C-16 PASS)." Both explicit dual-criterion tokens. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | PHASE 2 COMPLETE: + PHASE 3 COMPLETE: with explicit condition-(c) PASS statements. Three distinct criteria. C-20 satisfied via lifecycle path, orthogonal to the inertia front-loading axis. C-18 PASS. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A + OBLIGATION B full typed schemas present. Inertia front-loading is orthogonal to contract schema structure (confirmed by R6 V-03 at C-21 level). C-19 PASS. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | PHASE 2 COMPLETE: annotation: "This token is orthogonal to the inertia front-loading axis: whether the inertia scenario was committed before or after this phase, PHASE 2 COMPLETE: fires unconditionally at the Phase 2 boundary." PHASE 3 COMPLETE: annotation: "PHASE 3 COMPLETE: fires unconditionally at the Phase 3 boundary regardless of the inertia framing design." Both annotations name their phase boundaries explicitly. "C-22 fully satisfied." Pre-committed inertia does not affect unconditional emission at Phase 2/3 boundaries. Axes combine cleanly. C-18 PASS. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 all PASS (14 x 5 = 70)
**Raw score: 160/160** | All essential pass: YES | v7 ceiling: YES

**Confirmed: C-22 is orthogonal to the inertia front-loading axis. Pre-commitment in Phase 1 does not affect unconditional lifecycle token emission at Phase 2/3 boundaries.**

---

#### V-05 -- v7 Ceiling Synthesis (All 22 Criteria)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Inherited from R6 V-05 (scored 155/155 under v6) |
| C-09..C-17 | All aspirational through C-17 | **PASS** | Dual typed schemas; enforcement contract identical to V-04/V-05 R6 |
| C-18 | Multi-criterion token reuse | **PASS** | Three independent token paths: (1) THRESHOLD NOT MET: serves C-09 + C-16 explicitly. (2) RECOVERY NOTE: serves C-12 + C-16 explicitly. (3) PHASE 2 COMPLETE: serves C-09 + C-16. (4) PHASE 3 COMPLETE: serves C-13 + C-16. Four multi-criterion tokens. |
| C-19 | Typed token schema block | **PASS** | OBLIGATION B full typed schema. OBLIGATION A full typed schema. C-17 PASS. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | Two independent C-20 paths: (a) THRESHOLD NOT MET: "C-09 PASS. C-16 PASS." + RECOVERY NOTE: "C-12 PASS. C-16 PASS." -- canonical pair path from R5 V-05. (b) PHASE 2 COMPLETE: "(C-09 PASS). (C-16 PASS)." + PHASE 3 COMPLETE: "(C-13 PASS). (C-16 PASS)." -- lifecycle path from R6 V-04. Either path alone satisfies C-20. Both present: maximum redundancy. C-18 PASS. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A + OBLIGATION B full typed schemas. Both OBLIGATION A fields ({field_name}, {title_fragment}, {outcome}) verbatim in Phase 2; OBLIGATION B fields ({tier_name}, {why_no_sources_qualified}, {search_that_would_address_gap}) verbatim in Phase 3 tier instructions. C-19 PASS. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | PHASE 2 COMPLETE: "decisive observability upgrade over THRESHOLD NOT MET:"; "every run produces PHASE 2 COMPLETE: with status=MET"; names Phase 2 boundary; "(C-09 PASS). (C-16 PASS)." PHASE 3 COMPLETE: "decisive observability upgrade for empty-tier compliance"; "every run produces PHASE 3 COMPLETE: with tiers_empty=0"; names Phase 3 boundary; "(C-13 PASS). (C-16 PASS)." "Second of two required unconditional phase-boundary lifecycle tokens -- C-22 fully satisfied." C-18 PASS. Inertia front-loading (Phase 1 INERTIA COMMITMENT) does not affect unconditional emission. |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 all PASS (14 x 5 = 70)
**Raw score: 160/160** | All essential pass: YES | v7 ceiling: YES

**V-05 is the holistic reference implementation: two independent C-20 paths, dual typed schemas, inertia front-loading, unconditional lifecycle tokens, all 22 criteria.**

---

### Ranking

| Rank | Variation | Raw | C-22 | C-20 path | Differentiator |
|------|-----------|-----|------|-----------|----------------|
| 1 | **V-05** v7 Ceiling Synthesis | **160** | PASS | Dual (canonical + lifecycle) | Maximum coverage; two independent C-20 paths; inertia front-loading |
| 1 | **V-03** Dense Instrumentation | **160** | PASS | Lifecycle | Four-phase instrumentation; extends C-22 minimum to full coverage |
| 1 | **V-04** Inertia Front-Loading | **160** | PASS | Lifecycle | Proves C-22 orthogonal to inertia axis; cleanest cross-axis combination |
| 1 | **V-01** C-22 Baseline | **160** | PASS | Lifecycle | Minimum-change isolation; cleanest diagnostic for C-22 alone |
| 1 | **V-02** Domain-Named Tokens | **160** | PASS | Lifecycle | **Critical experiment**: confirms C-22 token-agnosticism |

All five reach the v7 ceiling. Sub-ranking: V-05 is the reference implementation (maximum redundancy). V-02 is the most informative experiment. V-03 extends the pattern furthest beyond the minimum.

---

### What changed from R6 to R7

| Criterion | R6 winners (V-04/V-05) | R7 all variations | Change |
|-----------|------------------------|-------------------|--------|
| C-22 | FAIL (criterion did not exist in v6) | PASS | Unconditional phase-boundary tokens with explicit boundary-naming annotations satisfy C-22; R6 V-04 design already contained the required tokens -- only the explicit C-22 annotation was missing |
| C-20 path | V-04/V-05: lifecycle path | V-01..V-05: lifecycle path confirmed | All R7 variations carry explicit "(C-NN PASS)" on lifecycle token annotations, unlike R6 V-01/V-02/V-03 which used description-only prose and failed C-20 |

Score ceiling: 155 (v6 fully satisfied by R6 V-04/V-05) -> 160 (v7 fully satisfied by all five R7 variations).

---

### EXCELLENCE SIGNALS

**From V-02 (critical experiment):**
- **C-22 is token-agnostic**: Domain-named boundary tokens (`EVIDENCE PHASE COMPLETE:`, `MAP PHASE COMPLETE:`) satisfy C-22 without using `PHASE N COMPLETE:` naming. The pass condition requires (a) named tokens, (b) unconditional emission, (c) annotation naming the phase boundary -- no implicit vocabulary constraint. Parallel to C-20 token-agnosticism confirmed in R6 V-04.

**From V-03 (dense instrumentation):**
- **Full-phase lifecycle coverage**: Four unconditional lifecycle tokens (PHASE 1..4 COMPLETE:) make every phase gate boundary-verifiable. The C-22 minimum (two tokens) is a floor; all four phases can be instrumented without friction. PHASE 4 COMPLETE: with `inertia_named=[yes/no]` makes C-14 compliance checkable at the Phase 4 boundary without scanning the Phase 4 body.

**From V-04 (orthogonality proof):**
- **Inertia front-loading is orthogonal to lifecycle tokens**: Pre-committing the inertia scenario in Phase 1 before any search does not affect unconditional emission of PHASE 2 COMPLETE: and PHASE 3 COMPLETE: at their respective boundaries. The two axes (pre-commitment timing, boundary observability) combine cleanly with no interference.

---

```json
{"top_score": 160, "all_essential_pass": true, "new_patterns": ["C-22 is token-agnostic: domain-named unconditional boundary tokens (EVIDENCE PHASE COMPLETE:, MAP PHASE COMPLETE:) satisfy C-22 without PHASE N COMPLETE: naming -- any named token that emits unconditionally at a phase boundary with an annotation naming that boundary qualifies, confirmed by V-02 critical experiment", "Full-phase lifecycle instrumentation: four unconditional PHASE N COMPLETE: tokens across all phases (V-03) extend observability beyond the C-22 minimum; PHASE 1 COMPLETE: makes claim enumeration boundary-verifiable; PHASE 4 COMPLETE: with inertia_named=[yes/no] makes C-14 compliance boundary-verifiable -- C-22 minimum of two is a floor not a ceiling"]}
```
