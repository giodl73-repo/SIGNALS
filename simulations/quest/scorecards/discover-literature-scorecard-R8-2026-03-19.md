## discover-literature R8 -- Scorecard

**Top score: 170/170. All essential pass: true.**

### Scoring Summary

| Rank | Variation | Raw | C-23 | C-24 | Differentiator |
|------|-----------|-----|------|------|----------------|
| 1 | **V-04** C-23 + C-24 Combination | **170** | PASS | PASS | Minimal 170 design: N-of-4 annotations + canonical pair PASS + C-24 block |
| 1 | **V-05** v8 Ceiling Synthesis | **170** | PASS | PASS | All 24 criteria + inertia front-loading |
| 4 | **V-01** C-23 Completeness | **165** | PASS | **FAIL** | Canonical pair lacks explicit "C-NN PASS" annotations |
| 4 | **V-02** C-24 Redundancy | **165** | **FAIL** | PASS | Phase 1 + Phase 4 tokens have no annotation paragraphs |
| 4 | **V-03** C-24 Alt Vocabulary | **165** | **FAIL** | PASS | **C-24 token-agnosticism confirmed** -- critical experiment passes |

### Key findings

**C-24 FAIL for V-01**: The canonical pair (THRESHOLD NOT MET: + RECOVERY NOTE:) is present but uses prose description ("records the threshold shortfall in the body for auditing") rather than explicit "C-09 PASS, C-16 PASS" annotations. C-20's pass condition (c) requires annotations that "confirm all listed criteria PASS." Only the lifecycle pair satisfies C-20 in V-01 -- one pair is C-20, not two.

**C-23 FAIL for V-02/V-03**: Phase 1 and Phase 4 lifecycle tokens exist but have no annotation paragraphs -- just the token line. C-23 requires each of four tokens to name its specific phase boundary and confirm unconditional emission. Two annotated tokens satisfies C-22; four is C-23.

**Critical experiment (V-03)**: C-24 is confirmed token-agnostic. Domain-named tokens `EVIDENCE PHASE COMPLETE:` + `MAP PHASE COMPLETE:` qualify as an independent C-20 pair for C-24. The full chain is now confirmed: C-18 -> C-20 (R4) -> C-22 (R7) -> C-24 (R8) -- no vocabulary constraints at any level.

**V-04 as minimal 170**: Merging R7 V-03 (four lifecycle tokens) + R7 V-05 (canonical pair PASS annotations) + C-24 independence block is purely additive. C-23 and C-24 are orthogonal -- neither's pass condition references the other.

```json
{"top_score": 170, "all_essential_pass": true, "new_patterns": ["N-of-4 progressive counter annotation: each lifecycle token declares 'Token N of 4 required for C-23 (Phase N boundary instrumented; C-23 in progress at N/4)' -- the count advances at each boundary and the final token declares C-23 fully satisfied, making compliance scannable from any single token and making Phase 1/4 instrumentation self-evidently necessary to complete the count", "C-24 independence verification block as a named structural element placed at the natural completion point (after PHASE 3 COMPLETE: where both pairs are first complete) -- names both pairs, confirms each independently satisfies C-20, runs the remove-either-pair test; C-24 compliance is declared not inferred"]}
```
t the Phase 2 / evidence-gathering boundary -- every run produces PHASE 2 COMPLETE: ... C-22 in progress." PHASE 3 COMPLETE: "second of two unconditional lifecycle tokens required for C-22 -- C-22 fully satisfied." Both name specific phase boundaries. C-18 PASS. |
| C-23 | Full-phase lifecycle instrumentation | **PASS** | Four lifecycle tokens, all annotated with explicit unconditional emission statements and "token N of 4" position declarations: PHASE 1 COMPLETE: "emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:, regardless of claim complexity ... token 1 of 4 required for C-23"; PHASE 2 COMPLETE: "token 2 of 4 ... C-23 in progress (2/4)"; PHASE 3 COMPLETE: "token 3 of 4 ... C-23 in progress (3/4)"; PHASE 4 COMPLETE: "token 4 of 4 ... C-23 fully satisfied. All four phase boundaries are now instrumented ... Each token names its specific phase boundary and emits unconditionally. C-23 PASS." C-22 PASS (dependency met). |
| C-24 | Redundant dual-path multi-criterion infrastructure | **FAIL** | Only one C-20-satisfying pair: the lifecycle pair. Canonical pair (THRESHOLD NOT MET: + RECOVERY NOTE:) annotations read "records the threshold shortfall in the body for auditing without requiring YAML parsing, and adds a named gate token" -- no explicit "C-09 PASS, C-16 PASS"; C-20 pass condition (c) requires annotations that "confirm all listed criteria PASS." Canonical pair does not independently satisfy C-20. C-24 requires two independent C-20-satisfying pairs. C-20 PASS (one pair met); C-24 FAIL (second independent pair absent). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-23 PASS, C-24 FAIL (15 x 5 = 75)
**Raw score: 165/170** | All essential pass: YES | v8 ceiling: NO (C-24 FAIL)

---

#### V-02 -- C-24 Redundancy Annotation

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Identical to R7 V-05 base; all phase content preserved |
| C-09..C-17 | Aspirational through C-17 | **PASS** | Dual typed schemas; canonical pair and lifecycle pair both present with Pair 1/Pair 2 designations |
| C-18 | Multi-criterion token reuse | **PASS** | Canonical pair: THRESHOLD NOT MET: "covers C-09 + C-16 (C-09 PASS, C-16 PASS)" and RECOVERY NOTE: "covers C-12 + C-16 (C-12 PASS, C-16 PASS)." Lifecycle pair: PHASE 2 COMPLETE: "(C-09 PASS). (C-16 PASS)." and PHASE 3 COMPLETE: "(C-13 PASS). (C-16 PASS)." Four multi-criterion tokens. |
| C-19 | Typed token schema block | **PASS** | Both obligations have typed schema blocks. C-17 PASS. |
| C-20 | Dual multi-criterion token synthesis | **PASS** | Both pairs present with explicit condition-(c) PASS annotations. Canonical pair covers C-09, C-12, C-16. Lifecycle pair covers C-09, C-13, C-16. Either pair alone satisfies C-20. C-18 PASS. |
| C-21 | Symmetric dual-obligation typed schema | **PASS** | OBLIGATION A + OBLIGATION B full typed schemas. Verbatim field names in Phase 2/3 output. C-19 PASS. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | PHASE 2 COMPLETE: "emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not." PHASE 3 COMPLETE: "emits unconditionally at the Phase 3 boundary -- every run produces PHASE 3 COMPLETE:." Both name phase boundaries; both unconditional. C-18 PASS. |
| C-23 | Full-phase lifecycle instrumentation | **FAIL** | Only Phase 2 and Phase 3 have lifecycle tokens with unconditional-emission annotations and explicit phase-boundary naming. Phase 1 token: `PHASE 1 COMPLETE: claims=[n] | counter-evidence-noted=[yes/no]` -- no annotation paragraph; does not confirm unconditional emission; no "token N of 4" language. Phase 4 token: `PHASE 4 COMPLETE: recommendation=... | high_risk_claims=[n]` -- no annotation paragraph. C-23 requires each of four tokens to have an annotation naming its specific phase boundary and confirming unconditional emission. Two annotated tokens satisfies C-22; four annotated tokens required for C-23. C-22 PASS (two present); C-23 FAIL (phases 1 and 4 unannotated). |
| C-24 | Redundant dual-path multi-criterion infrastructure | **PASS** | Explicit C-24 Independence Verification block after PHASE 3 COMPLETE:. Pair 1 (canonical): THRESHOLD NOT MET: + RECOVERY NOTE: -- covers C-09, C-12, C-16; both tokens named, both carry PASS annotations; "C-20 PASS for Pair 1 independently." Pair 2 (lifecycle): PHASE 2 COMPLETE: + PHASE 3 COMPLETE: -- covers C-09, C-13, C-16; both tokens named, both carry PASS annotations; "C-20 PASS for Pair 2 independently." Redundancy check: "Removing Pair 1: Pair 2 alone -- C-20 PASS. Removing Pair 2: Pair 1 alone -- C-20 PASS. Four tokens total, all distinct. Neither pair depends on the other. C-24 PASS." C-20 PASS (dependency met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 PASS, C-23 FAIL, C-24 PASS (15 x 5 = 75)
**Raw score: 165/170** | All essential pass: YES | v8 ceiling: NO (C-23 FAIL)

---

#### V-03 -- C-24 Alternative Vocabulary (Critical Experiment)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Domain-named lifecycle tokens do not affect phase content |
| C-09..C-17 | Aspirational through C-17 | **PASS** | Dual typed schemas; canonical pair present with explicit PASS annotations; domain-named lifecycle pair |
| C-18 | Multi-criterion token reuse | **PASS** | Canonical pair: THRESHOLD NOT MET: + RECOVERY NOTE: each cover two criteria with explicit PASS. Lifecycle pair: EVIDENCE PHASE COMPLETE: "(C-09 PASS). (C-16 PASS)." + MAP PHASE COMPLETE: "(C-13 PASS). (C-16 PASS)." Four multi-criterion tokens. |
| C-19..C-21 | Typed schema chain | **PASS** | Both obligations typed; C-15 -> C-17 -> C-19 -> C-21 chain intact. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | EVIDENCE PHASE COMPLETE: "emits unconditionally at the Phase 2 / evidence-gathering boundary -- every run produces EVIDENCE PHASE COMPLETE:, whether the threshold was met or not. The token name identifies the specific phase boundary." MAP PHASE COMPLETE: "emits unconditionally at the Phase 3 / literature-mapping boundary." C-22 is token-agnostic (V-02 R7). C-18 PASS. |
| C-23 | Full-phase lifecycle instrumentation | **FAIL** | Phase 1: `PHASE 1 COMPLETE: claims=[n] | counter-evidence-noted=[yes/no]` -- no annotation. Phase 4: `PHASE 4 COMPLETE: recommendation=... | high_risk_claims=[n]` -- no annotation. Phases 2 and 3 have proper unconditional annotations (EVIDENCE PHASE COMPLETE: and MAP PHASE COMPLETE:); phases 1 and 4 do not. C-23 FAIL. |
| C-24 | Redundant dual-path multi-criterion infrastructure | **PASS** | C-24 Independence Verification block with domain-named lifecycle pair explicitly. Pair 1 (canonical): C-09, C-12, C-16 -- independently C-20. Pair 2 (domain lifecycle): EVIDENCE PHASE COMPLETE: + MAP PHASE COMPLETE: -- C-09, C-13, C-16; "C-20 PASS for Pair 2 independently." Redundancy check passes. "Four tokens total, all distinct. Neither pair depends on the other. C-24 PASS." C-20 is token-agnostic; C-24 inherits via C-18 -> C-20 -> C-24 chain. **C-24 token-agnosticism confirmed.** C-20 PASS (dependency met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-22 PASS, C-23 FAIL, C-24 PASS (15 x 5 = 75)
**Raw score: 165/170** | All essential pass: YES | v8 ceiling: NO (C-23 FAIL)

**Critical experiment result: C-24 PASS with domain-named tokens. C-24 is confirmed token-agnostic. Token-agnosticism chain complete: C-18 -> C-20 (R4) -> C-22 (R7) -> C-24 (R8).**

---

#### V-04 -- C-23 + C-24 First Combination

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | R7 V-03 four-phase structure + R7 V-05 canonical pair annotations; all required phase outputs preserved |
| C-09..C-17 | Aspirational through C-17 | **PASS** | Dual typed schemas; both pairs with explicit PASS annotations; INERTIA SCENARIO: + INERTIA RISK: in Phase 4 |
| C-18 | Multi-criterion token reuse | **PASS** | Canonical pair: THRESHOLD NOT MET: "Pair 1, Token A -- C-09 PASS, C-16 PASS." RECOVERY NOTE: "Pair 1, Token B -- C-12 PASS, C-16 PASS." Lifecycle pair: PHASE 2 COMPLETE: "(C-09 PASS). (C-16 PASS). Pair 2, Token A." PHASE 3 COMPLETE: "(C-13 PASS). (C-16 PASS). Pair 2, Token B." Four multi-criterion tokens. |
| C-19..C-21 | Typed schema chain | **PASS** | Both obligations typed; verbatim field names propagated. C-15 -> C-17 -> C-19 -> C-21 chain intact. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | PHASE 2 COMPLETE: "emits unconditionally at the Phase 2 boundary -- every run produces PHASE 2 COMPLETE:, whether the threshold was met or not... (C-09 PASS). (C-16 PASS). Token 2 of 4 for C-23." PHASE 3 COMPLETE: same pattern for Phase 3. "Second of two required unconditional lifecycle tokens -- C-22 fully satisfied." C-18 PASS. |
| C-23 | Full-phase lifecycle instrumentation | **PASS** | All four lifecycle tokens with N-of-4 position declarations and explicit unconditional emission: PHASE 1 COMPLETE: "emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:, regardless of claim complexity... Token 1 of 4 required for C-23 (Phase 1 boundary instrumented; C-23 in progress at 1/4)." PHASE 2 COMPLETE: "Token 2 of 4 for C-23 (Phase 2 boundary instrumented; C-23 in progress at 2/4)." PHASE 3 COMPLETE: "Token 3 of 4 for C-23 (Phase 3 boundary instrumented; C-23 in progress at 3/4)." PHASE 4 COMPLETE: "emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:, whether recommendation is PROCEED, SEARCH MORE, or REFRAME CLAIM... Token 4 of 4 for C-23 -- C-23 fully satisfied. All four phase boundaries instrumented: Phase 1 / claim-extraction, Phase 2 / evidence-gathering, Phase 3 / literature-mapping, Phase 4 / gap-analysis. Each token emits unconditionally at its specific phase boundary. C-23 PASS." C-22 PASS (dependency met). |
| C-24 | Redundant dual-path multi-criterion infrastructure | **PASS** | C-24 Independence Verification block after PHASE 3 COMPLETE:. Pair 1: "Pair 1 together: C-09, C-12, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 1 independently." Pair 2: "Pair 2 together: C-09, C-13, C-16 -- three distinct aspirational criteria. Both tokens named, both carry PASS annotations. C-20 PASS for Pair 2 independently." Redundancy: "Removing Pair 1: Pair 2 alone -- C-20 PASS. Removing Pair 2: Pair 1 alone -- C-20 PASS. Four tokens total, all distinct. C-24 PASS." C-20 PASS (dependency met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-24 all PASS (16 x 5 = 80)
**Raw score: 170/170** | All essential pass: YES | v8 ceiling: YES

**V-04 is the minimal 170 design: four-phase lifecycle instrumentation (C-23) + dual independent C-20 pairs (C-24), no inertia front-loading. Confirms C-23 and C-24 are orthogonal and purely additive.**

---

#### V-05 -- v8 Ceiling Synthesis (All 24 Criteria)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01..C-08 | Essential + Recommended | **PASS** | Inherited from V-04; inertia front-loading adds Phase 1 gate without affecting other outputs |
| C-09..C-17 | Aspirational through C-17 | **PASS** | Same as V-04; inertia commitment block in Phase 1 is additive |
| C-14 | Inertia guard on PROCEED | **PASS** (maximum) | INERTIA COMMITMENT gate in Phase 1 before any search: "INERTIA SCENARIO: [the default team behavior if this review is ignored -- written before any search]." PHASE 1 COMPLETE: includes `inertia_committed=[yes]`. Phase 4 INERTIA VERIFICATION gate: "Return to the INERTIA SCENARIO committed in Phase 1. Measure the evidence gathered against it." PHASE 4 COMPLETE: includes `inertia_named=[yes]` (structurally required by Phase 1 gate). Maximum C-14 coverage: inertia named before evidence, verified after. |
| C-18..C-21 | Multi-criterion synthesis chain | **PASS** | Same as V-04; four multi-criterion tokens; dual typed schemas. |
| C-22 | Unconditional phase-boundary lifecycle tokens | **PASS** | PHASE 2 COMPLETE: "C-22 is orthogonal to the inertia front-loading axis: PHASE 2 COMPLETE: fires unconditionally at the Phase 2 boundary regardless of whether inertia was committed in Phase 1 (V-04 R7 confirms)." Inertia front-loading does not affect unconditional emission. C-18 PASS. |
| C-23 | Full-phase lifecycle instrumentation | **PASS** | PHASE 1 COMPLETE: "emits unconditionally at the Phase 1 / claim-extraction boundary -- every run produces PHASE 1 COMPLETE:... Token 1 of 4 for C-23 (Phase 1 boundary instrumented; C-23 in progress at 1/4)." PHASE 4 COMPLETE: "emits unconditionally at the Phase 4 / gap-analysis boundary -- every run produces PHASE 4 COMPLETE:... Token 4 of 4 for C-23 -- C-23 fully satisfied. All four phase boundaries instrumented... C-23 PASS." C-22 PASS (dependency met). |
| C-24 | Redundant dual-path multi-criterion infrastructure | **PASS** | Same C-24 Independence Verification block as V-04. Both pairs independently C-20. Redundancy check passes. C-20 PASS (dependency met). |

**Essential**: 5/5 = 60 | **Recommended**: 3/3 = 30 | **Aspirational**: C-09..C-24 all PASS (16 x 5 = 80)
**Raw score: 170/170** | All essential pass: YES | v8 ceiling: YES

**V-05 is the holistic reference implementation: V-04 plus maximum C-14 via inertia front-loading. Confirms all six aspirational axes are orthogonal and fully additive.**

---

### Ranking

| Rank | Variation | Raw | C-23 | C-24 | Path |
|------|-----------|-----|------|------|------|
| 1 | **V-04** C-23 + C-24 Combination | **170** | PASS | PASS | Minimal ceiling design; orthogonality confirmed |
| 1 | **V-05** v8 Ceiling Synthesis | **170** | PASS | PASS | All 24 criteria; maximum C-14 via front-loading |
| 3 | **V-01** C-23 Completeness | **165** | PASS | FAIL | C-23 confirmed; canonical pair lacks explicit PASS annotations |
| 3 | **V-02** C-24 Redundancy | **165** | FAIL | PASS | C-24 confirmed; Phase 1/4 tokens unannotated |
| 3 | **V-03** C-24 Alt Vocabulary | **165** | FAIL | PASS | **C-24 token-agnosticism confirmed** by critical experiment |

V-04 is the minimal 170 design. V-05 adds the C-14 maximum axis. V-03 is the most informative experiment: C-24 inherits token-agnosticism from C-20 via the full dependency chain.

---

### What changed from R7 to R8

| Criterion | R7 top (V-05) | R8 analysis | Change |
|-----------|---------------|-------------|--------|
| C-23 | Did not exist in v7 | V-01 and V-04/V-05 PASS; V-02/V-03 FAIL | C-23 requires explicit "token N of 4" annotations naming phase boundary and confirming unconditional emission -- having a lifecycle token at Phase 1/4 is insufficient without the annotation |
| C-24 | Did not exist in v7 | V-01 FAIL; V-02/V-03/V-04/V-05 PASS | Canonical pair needs explicit "C-NN PASS" annotations (prose description insufficient); lifecycle pair from R7 V-05 already satisfies Pair 2 |
| C-24 token-agnosticism | Not yet tested | V-03 critical experiment PASSES | C-24 inherits token-agnosticism via C-18 -> C-20 -> C-24 dependency chain; domain-named lifecycle pairs qualify |

Score ceiling: 160 (v7) -> 170 (v8). V-04 and V-05 reach the v8 ceiling.

---

### EXCELLENCE SIGNALS

**From V-04 (first 170 design -- minimal ceiling):**
- **N-of-4 progressive counter annotation**: Each lifecycle token declares "Token N of 4 required for C-23 (Phase N boundary instrumented; C-23 in progress at N/4)" within its annotation. The counter advances at each phase boundary; the final token declares "C-23 fully satisfied." This compact structure makes C-23 compliance scannable from any single token without locating all four. It also makes Phase 1 and Phase 4 instrumentation self-evidently necessary -- omitting them breaks the count.
- **C-24 independence verification block as a named structural element**: Placed immediately after PHASE 3 COMPLETE: (where both pairs are first complete), the block provides one grep-verifiable location for the redundancy proof -- naming both pairs, confirming each independently satisfies C-20, and running the remove-either-pair test explicitly. C-24 compliance is declared, not inferred.

**From V-03 (critical experiment -- C-24 token-agnosticism):**
- **Token-agnosticism chain confirmed through C-24**: C-24 inherits token-agnosticism from C-20 via the dependency chain C-18 -> C-20 -> C-24. The full chain: C-18 (one multi-criterion token, any name), C-20 (two tokens forming one pair, any names, R4), C-22 (unconditional emission, any names, R7), C-24 (two independent pairs, any names, R8). No criterion in this chain imposes vocabulary constraints. Any named token carrying the required annotation structure qualifies at every level.

**From V-05 (ceiling synthesis -- hardcoded vs. dynamic field pattern):**
- **Mandatory pre-condition embedding**: V-05's `inertia_committed=[yes]` (fixed value in PHASE 1 COMPLETE:, required by the preceding gate) versus V-04's `inertia_named=[yes/no]` (variable, audited in PHASE 4 COMPLETE:) reveals a design pattern: when a lifecycle token's field verifies a structurally mandatory gate, the field value can be hardcoded. A variable field is an audit gate (the value might be `no`); a hardcoded field is a compliance record (the value is always `yes` because the gate is obligatory). This pattern applies to any unconditional token whose corresponding phase obligation is also unconditional.

---

```json
{"top_score": 170, "all_essential_pass": true, "new_patterns": ["N-of-4 progressive counter annotation: each lifecycle token declares 'Token N of 4 required for C-23 (Phase N boundary instrumented; C-23 in progress at N/4)' -- the count advances at each boundary and the final token declares C-23 fully satisfied, making compliance scannable from any single token and making Phase 1/4 instrumentation self-evidently necessary to complete the count", "C-24 independence verification block as a named structural element placed at the natural completion point (after PHASE 3 COMPLETE: where both pairs are first complete) -- names both pairs, confirms each independently satisfies C-20, runs the remove-either-pair test; C-24 compliance is declared not inferred"]}
```
