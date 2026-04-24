Scorecard written to `simulations/quest/scorecards/narrate-behavior-scorecard-R7-2026-03-17.md`.

---

## R7 Summary

**All 5 variations: 80/80. Rubric ceiling reached.**

| Variation | Total | Aspirational | C-25 |
|-----------|-------|--------------|------|
| V-31 | 80/80 | 18/18 | PASS |
| V-32 | 80/80 | 17/18 | FAIL |
| V-33 | 80/80 | 17/18 | FAIL |
| V-34 | 80/80 | 18/18 | PASS |
| V-35 | 80/80 | 18/18 | PASS |

**Rank:** V-35 > V-34 > V-31 > V-32 = V-33

**V-31** confirmed the minimal fix hypothesis: percentages + one-sentence interpretation in REPORT closes C-25 with zero structural change elsewhere.

**V-32 and V-33** each introduce a new structural output class (COVERAGE CITATION INDEX, TRIAGE GATE) but fail C-25 — they don't touch the disposition summary. Both still hit the aspirational cap (17 >= 10).

**V-35** is the top scorer by excellence signal density — full disposition traceability chain with all three artifact targets orthogonally confirmed. All four open questions resolved YES.

**3 new patterns for v8:**
- `covered-disposition-spec-citation-registry` — COVERED citations collected into auditable COVERAGE CITATION INDEX
- `investigation-triage-gate-as-structural-artifact` — INVESTIGATION dispositions flow to prioritized resolution queue with zero-escape REQUIRE
- `full-disposition-traceability-chain` — each of the four disposition types routes to a named artifact target

**v8 aspirational tier grows to 21 (C-26/C-27/C-28). Threshold: any 11 of 21.**

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["covered-disposition-spec-citation-registry", "investigation-triage-gate-as-structural-artifact", "full-disposition-traceability-chain"]}
```
 confirmed spec-coverage rate", "INVESTIGATION: [count] ([N%]) -- ambiguity rate pending resolution", "NONE: [count] ([N%]) -- out-of-scope rate", plus Interpretation sentence with three domain-agnostic template forms. REQUIRE enforces: "Inertia disposition summary includes total assumption count, labeled percentages for FINDING / COVERED / INVESTIGATION (at minimum), and an interpretation statement." All C-25 pass conditions met. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 18/18 passes -- cap earned: 10/10
**V-31 Total: 80/80**

Minimal fix confirmed: V-30 failed C-25 because disposition summary emitted counts only. V-31 adds percentage computation and one-sentence interpretation with no structural change to any other section. C-25 fully satisfied. Rubric fully saturated.

---

### V-32 -- COVERED spec-citation

Base: V-30 + COVERED dispositions must cite "spec covers: [section]" + COVERAGE CITATION INDEX in REPORT.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-22 | PASS | All inherited from V-30. |
| C-23 | PASS | Three-form discovery-pathway-ratio rule in DEFINITIONS. REPORT REQUIRE check present. |
| C-24 | PASS | Four dispositions defined. REPORT REQUIRE completeness check present. COVERED citation requirement does not alter C-24 scope -- C-24 checks that each named assumption has a disposition; COVERED citation adds evidence-quality requirement within COVERED outcomes, not a new disposition type. |
| C-25 | FAIL | REPORT disposition summary: "Inertia disposition summary: [count of FINDING / COVERED / INVESTIGATION / NONE dispositions across all 5 sections -- confirms exhaustive disposition completeness]." Counts only -- no labeled percentage fields, no interpretation sentence. C-25 pass condition requires percentages + interpretation. V-32 does not add C-25 framing. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 17/18 passes -- cap earned: 10/10 (17 >= 10 threshold)
**V-32 Total: 80/80**

New structural output class introduced: COVERAGE CITATION INDEX in REPORT collects all COVERED dispositions as (Assumption, Sub-Skill, Spec Section Cited, B-ID) rows. This creates an auditable "spec-defense surface" -- the set of assumptions the spec explicitly addresses, distinguishable from spec-silent (FINDING) and ambiguous (INVESTIGATION) outcomes. Does not satisfy C-25 (no percentages). Excellence signal candidate: covered-disposition-spec-citation-registry.

---

### V-33 -- INVESTIGATION triage gate

Base: V-30 + TRIAGE GATE structural section between S5 and REPORT.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Declared sequence: "S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> TRIAGE GATE -> REPORT." TRIAGE GATE is a compilation step (analogous to BOUNDARY REGISTRY or BACK-ANNOTATE), not a simulation section. The five simulation sub-skills (S1-S5) execute in declared order. TRIAGE GATE is declared and appears after S5 as declared. PASS. |
| C-02--C-22 | PASS | All inherited from V-30. |
| C-23 | PASS | Three-form discovery-pathway-ratio rule in DEFINITIONS. REPORT REQUIRE check present. |
| C-24 | PASS | Four dispositions defined; aggregate completeness check in REPORT REQUIRE. TRIAGE GATE REQUIRE: "Every INVESTIGATION finding from all 5 EXIT GATEs appears in this TRIAGE GATE." Complementary to C-24 aggregate check -- both satisfied simultaneously. |
| C-25 | FAIL | REPORT disposition summary: counts only. No labeled percentage fields, no interpretation sentence. Same failure mode as V-30. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 17/18 passes -- cap earned: 10/10
**V-33 Total: 80/80**

TRIAGE GATE structural analysis: INVESTIGATION dispositions produce observation-type finding table rows (existing V-30 behavior) AND a resolution-required entry in the TRIAGE GATE (new behavior). TRIAGE GATE compiles with Priority assignment (HIGH/MED/LOW derived from Blast Radius and B-ID citation count). REQUIRE enforces zero-escape: no INVESTIGATION disposition exits the simulation without a triage entry. Mirrors how BOUNDARY REGISTRY converts text-named boundaries into structural artifacts -- TRIAGE GATE converts investigation findings into a pre-implementation resolution queue. Excellence signal candidate: investigation-triage-gate-as-structural-artifact.

C-01 composition note: the open question (does TRIAGE GATE satisfy C-01?) resolves YES. C-01 requires simulation sections (S1-S5) appear in declared order; TRIAGE GATE is a compilation step, not a simulation section. Position in declared sequence must match execution position -- V-33 satisfies this.

---

### V-34 -- Combo: C-25 coverage score + COVERED spec-citation

Base: V-31 (C-25 percentages + interpretation) + V-32 (COVERED spec-citation + COVERAGE CITATION INDEX).

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01--C-22 | PASS | All inherited from V-30. |
| C-23 | PASS | Three-form rule in DEFINITIONS + REPORT REQUIRE check. |
| C-24 | PASS | Four dispositions defined; aggregate completeness check in REPORT REQUIRE. COVERED citation requirement composes cleanly with C-24: C-24 checks that every named assumption carries a disposition; V-34 COVERED citation rule adds a quality constraint within COVERED outcomes (citation required), not a new disposition type. No ambiguity introduced. |
| C-25 | PASS | Disposition summary includes labeled percentages for FINDING / COVERED / INVESTIGATION / NONE, total assumption count, and interpretation sentence. Inherits V-31 full C-25 implementation. REQUIRE block explicitly checks all three fields. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 18/18 passes -- cap earned: 10/10
**V-34 Total: 80/80**

Combination verdict: C-25 percentage computation and COVERAGE CITATION INDEX are orthogonal outputs. C-25 reads disposition counts already in the summary. COVERAGE CITATION INDEX reads "spec covers: [section]" notes from INERTIA blocks. No shared resource contention. Two views of COVERED dispositions: quantitative density (C-25) + auditable citation path (INDEX). Open question resolved: COVERED spec-citation composes cleanly with C-24 -- they operate on different properties of COVERED dispositions.

---

### V-35 -- Combo: C-25 + COVERED spec-citation + INVESTIGATION triage gate

Base: V-31 + V-32 + V-33. Full disposition traceability chain: every INERTIA assumption routes to a named artifact target.

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-01 | PASS | Declared sequence: "S1 -> S2 -> BOUNDARY REGISTRY -> BACK-ANNOTATE -> S3 -> S4 -> S5 -> TRIAGE GATE -> REPORT." All compilation steps (BOUNDARY REGISTRY, BACK-ANNOTATE, TRIAGE GATE) declared before first simulation section and appear in declared order. |
| C-02--C-22 | PASS | All inherited. |
| C-23 | PASS | Three-form rule in DEFINITIONS + REPORT REQUIRE. |
| C-24 | PASS | Four dispositions defined with artifact routing annotated in DEFINITIONS: "FINDING: Artifact target: FINDING TABLE", "COVERED: Artifact target: COVERAGE CITATION INDEX", "INVESTIGATION: Artifact target: FINDING TABLE (observation) + TRIAGE GATE (resolution entry)", "NONE: Artifact target: inline statement only." REPORT REQUIRE completeness check present. |
| C-25 | PASS | Disposition summary with labeled percentages, total count, and interpretation sentence. REQUIRE enforces all three fields. |

**Essential**: 40/40 | **Recommended**: 30/30 | **Aspirational**: 18/18 passes -- cap earned: 10/10
**V-35 Total: 80/80**

Full traceability chain structural analysis: three artifact targets are orthogonal.
- FINDING TABLE rows: written by FINDING dispositions (spec-gap) and INVESTIGATION dispositions (observation)
- COVERAGE CITATION INDEX: written by COVERED dispositions only
- TRIAGE GATE: written by INVESTIGATION dispositions only

INVESTIGATION dual-routing is additive (one observation row in FINDING TABLE + one resolution entry in TRIAGE GATE); these are distinct tables with distinct structures. No shared resource contention confirmed. Open question resolved: V-35 three artifact targets compose without conflict.

The new excellence signal full-disposition-traceability-chain is the structural pattern: each of the four disposition outcomes routes to a named artifact, making the disposition system fully observable and auditable at REPORT level.

---

### Open Question Resolutions

| Question | Verdict |
|----------|---------|
| Does a single generic interpretation sentence satisfy C-25? | YES -- V-31/V-34/V-35 provide three domain-agnostic template forms; any one satisfies "brief interpretation statement accompanies the score." Topic-specific wording is not required. |
| Does COVERED spec-citation compose cleanly with C-24 completeness check? | YES -- C-24 checks that every named assumption carries a disposition (one of four). COVERED citation rule constrains evidence quality within COVERED outcomes but does not add a fifth disposition type. C-24 aggregate completeness check reads disposition labels, not citation content. |
| Does TRIAGE GATE as a structural section satisfy C-01 sequence declaration? | YES -- C-01 requires simulation sections (S1-S5) appear in declared order. TRIAGE GATE is a compilation step, not a simulation section. Position in declared sequence must match execution position -- both V-33 and V-35 satisfy this. |
| Do V-35 three artifact targets compose without shared resource conflict? | YES -- FINDING TABLE, COVERAGE CITATION INDEX, TRIAGE GATE are fully orthogonal. INVESTIGATION dual-routing is additive: one observation row in FINDING TABLE and one resolution entry in TRIAGE GATE; distinct tables with distinct structures. |

---

### Rank

All variations tie at 80/80. Secondary differentiation by aspirational coverage and excellence signal contribution:

1. **V-35** (top) -- Full disposition traceability chain: C-25 + COVERED citation + TRIAGE GATE. Three new structural additions, all 18 aspirational pass. Every disposition outcome routes to a named artifact. Most excellence signal material.
2. **V-34** -- C-25 + COVERED citation. 18/18 aspirational. Quantitative density score + auditable citation path for COVERED dispositions. Two orthogonal views.
3. **V-31** -- C-25 minimal fix. 18/18 aspirational. Closes the one v7 gap with minimum overhead. Clean single-axis target.
4. **V-32** -- COVERED citation only. 17/18 aspirational (fails C-25). New COVERAGE CITATION INDEX structural output class without density score.
5. **V-33** -- TRIAGE GATE only. 17/18 aspirational (fails C-25). New structural compilation section for INVESTIGATION dispositions without density score.

---

### Excellence Signals (R7)

#### SIGNAL-1 -- covered-disposition-spec-citation-registry (V-32, V-34, V-35)

V-30 emits COVERED dispositions as inline prose: "spec covers: [section or clause]" within the INERTIA block. This note is not collected or verified in REPORT -- a reviewer cannot enumerate all assumptions the spec defends without scanning all five INERTIA blocks. V-32 promotes COVERED citations to a first-class structural artifact: COVERAGE CITATION INDEX collects (Assumption, Sub-Skill, Spec Section Cited, B-ID) per COVERED disposition. REPORT REQUIRE enforces: "All COVERED dispositions cite a specific spec section" and "COVERAGE CITATION INDEX populated with 1 row per COVERED disposition." Key structural insight: this creates a "spec-defense surface" -- the set of assumptions the spec already handles, distinct from spec-silent (FINDING) and ambiguous (INVESTIGATION) surfaces. A high COVERED count becomes auditable, not just claimed.

#### SIGNAL-2 -- investigation-triage-gate-as-structural-artifact (V-33, V-35)

V-30 routes INVESTIGATION dispositions to observation-type rows in the FINDING TABLE. These rows are interleaved with FINDING and contract-violation rows -- retrieving all unresolved investigations requires filtering the full table. V-33 adds TRIAGE GATE as a structural section between S5 and REPORT: a dedicated compilation of all INVESTIGATION findings with Priority assignment (HIGH/MED/LOW) and "Verify Before Implementation" field. REQUIRE enforces zero-escape: no INVESTIGATION disposition exits the simulation without a TRIAGE GATE entry. The pattern mirrors BOUNDARY REGISTRY (which converts scattered text-name boundary references into a named, typed registry): TRIAGE GATE converts scattered INVESTIGATION observations into a prioritized pre-implementation resolution queue. New structural class: disposition-type-specific compilation section.

#### SIGNAL-3 -- full-disposition-traceability-chain (V-35)

V-35 assigns a named artifact target to each of the four disposition outcomes, explicitly in DEFINITIONS: FINDING -> FINDING TABLE, COVERED -> COVERAGE CITATION INDEX, INVESTIGATION -> FINDING TABLE (observation) + TRIAGE GATE (resolution entry), NONE -> inline statement. This makes the disposition system fully observable at REPORT level: a reviewer can audit which assumptions produced spec-gaps (FINDING TABLE), which were spec-defended (COVERAGE CITATION INDEX), which are unresolved (TRIAGE GATE), and which are out-of-scope (inline). The traceability chain is the analog of how C-19 text-name-to-B-ID pipeline made boundary discovery observable across section tiers. Full dispositions become first-class routing decisions, not just annotation tags.

---

### Rubric Ceiling Analysis

R7 rubric fully saturated. All 18 aspirational criteria satisfiable simultaneously -- confirmed by V-31, V-34, V-35 (18/18). V-32 and V-33 confirm that each new signal-bearing feature (COVERED citation, TRIAGE GATE) is independently achievable without requiring C-25 -- the new features compose with existing structure without creating conflicts.

v8 candidates from R7 excellence signals:
- C-26 from SIGNAL-1: covered-disposition-spec-citation-registry -- COVERED dispositions must cite spec section; COVERAGE CITATION INDEX in REPORT collects and verifies all citations
- C-27 from SIGNAL-2: investigation-triage-gate-as-structural-artifact -- TRIAGE GATE between S5 and REPORT compiles all INVESTIGATION dispositions with Priority and resolution field; REQUIRE enforces zero-escape
- C-28 from SIGNAL-3: full-disposition-traceability-chain -- each disposition type routes to a named artifact target; REPORT can audit completeness per-artifact rather than per-assumption

Aspirational tier grows to 21 in v8. Threshold should increase to "any 11 of 21" to maintain structural challenge proportional to existing progression.

---

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["covered-disposition-spec-citation-registry", "investigation-triage-gate-as-structural-artifact", "full-disposition-traceability-chain"]}
```
