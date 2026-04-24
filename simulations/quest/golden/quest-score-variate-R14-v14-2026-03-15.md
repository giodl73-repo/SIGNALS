# quest-rubric Score — Round 14 (Rubric v14, Targeting C-43/C-44)
**Date:** 2026-03-15
**Rubric:** v14 (denominator /36, C-09–C-44; essential gate C-01–C-05)
**Composite formula:** 0.6 × essential_score + 0.3 × recommended_score + 0.1 × aspirational_score
**Target criteria:** C-43 (emit phase closes with per-criterion evaluability declaration: artifact + scan method), C-44 (each declaration names excluded instruction content)

---

## Scoring Notes

**Baseline (all R13 criteria pass, C-43/C-44 fail):** 34/36 aspirational × 100 = 94.444 → composite = 60 + 30 + 9.444 = 99.444

**C-43 discrimination pivot:** Does Phase 9 independently *produce* a terminal evaluability section with named artifact and scan method as distinct labeled columns? V-02 references Phase 8.5 output (PARTIAL); V-03 produces prose notes without column separation (PARTIAL); V-01/V-04/V-05 produce a formal table as terminal Phase 9 content (PASS).

**C-44 discrimination pivot:** Does the evaluability declaration name the *specific excluded instruction content* for each criterion? V-01 has no Independence column (FAIL); V-03 has prose without exclusion clause (FAIL); V-02/V-04/V-05 require "Yes -- independently verifiable without reading [named content]" (PASS).

**C-11 note:** All 5 variations satisfy C-11 through the base Phase 3-4 structure (skill-specific criterion construction with no-qualitative audit). V-03/V-04/V-05 add EVALUABILITY COMPETITOR framing as a secondary mechanism; ablation map "C-11 ablated" for V-01/V-02 means the secondary mechanism is removed, not that C-11 fails.

---

## V-01 -- Output Format

**Axis:** Phase 9 closes with CRITERION EVALUABILITY MAP table (C-NN | Verification Artifact | Scan Method). C-44 ablated -- no Independence column.

| ID | Score | Evidence |
|----|-------|---------|
| C-01 | PASS | Five-field criterion structure required throughout Phases 3-4; Phase 4.5 audit catches missing fields |
| C-02 | PASS | Phase 3: 3-5 essential; Phase 4: 2-3 recommended; ROLE: BUILDER ASPIRATIONAL: 1-2 aspirational |
| C-03 | PASS | Phase 1 failure mode analysis grounds essential criteria in skill-specific blocking failures |
| C-04 | PASS | Phase 4.5 Pass field checks require LOCATION + OBSERVABLE + STANDARD; qualitative-only flags and rewrites |
| C-05 | PASS | Phase 8 requires THREE-STATE SCORING TABLE with composite formula and golden threshold |
| C-06 | PASS | Phase 5.75 tier-divergence scan enforces >= 2 distinct majority categories; Phase 7 requires >= 3 |
| C-07 | PASS | Phase 3 ordering follows blocking (most critical) to suboptimal severity hierarchy |
| C-08 | PASS | Phase 9 emit manifest includes Notes section; checklist format standard output |
| C-09 | PASS | LOCATION + OBSERVABLE + STANDARD triad gives author exact fix target on failure |
| C-10 | PASS | ROLE: MECHANISM DEFINER Independence Map requires all rows "Yes -- affects C-NN only" |
| C-11 | PASS | Phase 4.5 no-qualitative check forces skill-specific observables; COMPETITOR blocks require derivation from wrong-implementation description |
| C-12 | PASS | COMPETITOR blocks inline before each criterion serve as calibration pairs |
| C-13 | PASS | Phase 9 STOP CONDITION blocks emit until CRITERION EVALUABILITY MAP present; DEFINER OUTPUT GATE + MECHANISM DEFINER GATE also block earlier phases |
| C-14-C-42 | PASS | All R13 structural mechanisms present: DEFINER OUTPUT GATE, MECHANISM DEFINER GATE, PHASE-LOCALITY RULE (three prohibited zones enumerated verbatim), tier-divergence scan, Phase 6.75 three-step placement + coverage audit, Phase 7 pre-emit verification, Independence Map as named section, COMPETITOR blocks inline per criterion, three-state scoring |
| **C-43** | **PASS** | Phase 9 section 10 (after vN Candidates): terminal CRITERION EVALUABILITY MAP table; columns: C-NN, Verification Artifact, Scan Method; every structural criterion required to have a row; STOP CONDITION blocks emit if section absent or any row blank; named artifact + scan method as distinct labeled columns satisfies C-43's structural separation requirement |
| **C-44** | **FAIL** | CRITERION EVALUABILITY MAP has exactly three columns: C-NN, Verification Artifact, Scan Method. No Independence column. A row of the form "C-01 | Essential Criteria section | scan for 'Not [X], but [Y]' pattern" passes without naming what the evaluator is freed from reading. C-44 requires explicit excluded-content naming per row; the three-column design makes this structurally impossible |

**Essential (C-01-C-05):** 5/5 PASS
**Recommended (C-06-C-08):** 3/3 PASS
**Aspirational (C-09-C-44):** 35/36 (C-44 FAIL = 0, all others = 1)
**Aspirational score:** 35/36 x 100 = 97.222
**Composite:** 0.6 x 100 + 0.3 x 100 + 0.1 x 97.222 = **99.722**

---

## V-02 -- Lifecycle Emphasis

**Axis:** Phase 8.5 EVALUABILITY GATE (four columns: C-NN, Verification Artifact, Scan Method, Independence). Phase 9 *references* gate output as terminal section -- "reproduce Phase 8.5 EVALUABILITY GATE output verbatim as the final section." No EVALUABILITY COMPETITOR.

| ID | Score | Evidence |
|----|-------|---------|
| C-01-C-05 | PASS | Same five-field structure; same failure-mode grounding; same scoring format |
| C-06-C-08 | PASS | Same tier-divergence enforcement; same Notes/checklist structure |
| C-09-C-42 | PASS | All R13 structural mechanisms present; Phase 8.5 gate is additive |
| **C-43** | **PARTIAL** | The final section of the emitted document contains named artifact + scan method per criterion -- terminal position is present. But C-43 requires the *emit phase* to close with the declaration. Phase 9 achieves this via reference ("include Phase 8.5 EVALUABILITY GATE output as final section"), not independent production. A rubric evaluator reading Phase 9's emit manifest finds "section 11: reproduce Phase 8.5 output" -- the declaration exists in the document but was produced at Phase 8.5, not at Phase 9 close. Terminal position requirement met by reference; Phase 9 independent terminal production not met |
| **C-44** | **PASS** | Phase 8.5 EVALUABILITY GATE Independence column explicitly requires: "Yes -- independently verifiable without reading [name the specific excluded content]." STOP CONDITION blocks Phase 9 until every row has Independence in the required form -- "Independently verifiable" without naming excluded content is explicitly called incomplete. Exclusion naming is a pre-Phase-9 structural condition enforced before Phase 9 opens, reproduced in the final section |

**Essential (C-01-C-05):** 5/5 PASS
**Recommended (C-06-C-08):** 3/3 PASS
**Aspirational (C-09-C-44):** 34 + 0.5 (C-43 PARTIAL) + 1 (C-44 PASS) = 35.5/36
**Aspirational score:** 35.5/36 x 100 = 98.611
**Composite:** 0.6 x 100 + 0.3 x 100 + 0.1 x 98.611 = **99.861**

---

## V-03 -- Inertia Framing

**Axis:** EVALUABILITY COMPETITOR block before Phase 9 names the rubric-without-evaluability-map gap. Phase 9 closes with EVALUABILITY NOTES (prose sentences, one per criterion). No Phase 8.5 gate. C-44 ablated.

| ID | Score | Evidence |
|----|-------|---------|
| C-01-C-05 | PASS | Same five-field structure; same failure-mode grounding; same scoring format |
| C-06-C-08 | PASS | Same tier-divergence and checklist structure |
| C-09-C-42 | PASS | All R13 structural mechanisms present; EVALUABILITY COMPETITOR is additive |
| **C-43** | **PARTIAL** | Phase 9 closes with EVALUABILITY NOTES section -- declarations are present (one sentence per structural criterion), section is terminal, STOP CONDITION blocks deferred entries. But C-43 requires "named verification artifact" and "scan method" as distinct structural elements. Prose form ("C-NN is verifiable by scanning [location] for [observable]") conflates artifact and method in a single sentence; no labeled columns separate them. A reader cannot scan for "Verification Artifact:" as a distinct field -- artifact and method must be parsed from prose. STOP CONDITION prevents absent/deferred entries but does not enforce column-separation structural requirement |
| **C-44** | **FAIL** | EVALUABILITY NOTES entries provide verification paths in prose. The EVALUABILITY COMPETITOR correctly names the gap ("no single document section states 'C-NN is verifiable... without reading [Y]'") but the REQUIRED APPROACH specifies prose declarations of the form: "C-NN is verifiable by [description]." No "without reading [excluded content]" clause is required. The competitor diagnoses the exclusion-naming gap but the required approach does not close it: independence is implied by scan specificity, not declared explicitly |

**Essential (C-01-C-05):** 5/5 PASS
**Recommended (C-06-C-08):** 3/3 PASS
**Aspirational (C-09-C-44):** 34 + 0.5 (C-43 PARTIAL) + 0 (C-44 FAIL) = 34.5/36
**Aspirational score:** 34.5/36 x 100 = 95.833
**Composite:** 0.6 x 100 + 0.3 x 100 + 0.1 x 95.833 = **99.583**

---

## V-04 -- Output Format + Lifecycle Emphasis + Inertia Framing

**Axis:** Phase 8.5 EVALUABILITY GATE (four columns including Independence) + EVALUABILITY COMPETITOR embedded in Design Rationale + Phase 9 terminal CRITERION EVALUABILITY MAP independently produced with all four columns.

| ID | Score | Evidence |
|----|-------|---------|
| C-01-C-05 | PASS | Same five-field structure; same grounding; same scoring format |
| C-06-C-08 | PASS | Same tier-divergence and checklist structure |
| C-09-C-42 | PASS | All R13 structural mechanisms present; Phase 8.5 gate and EVALUABILITY COMPETITOR are additive |
| **C-43** | **PASS** | Phase 9 independently produces CRITERION EVALUABILITY MAP as section 11 (explicitly listed in Phase 9 emit manifest after vN Candidates): "all four columns (C-NN, Verification Artifact, Scan Method, Independence) must be present for every structural criterion." Phase 9 STOP CONDITION blocks if section 11 absent or any column missing. Unlike V-02, Phase 9's emit manifest names section 11 as a structural requirement -- the terminal section is produced by Phase 9, not deferred. Named artifact + scan method as distinct labeled columns satisfies C-43 |
| **C-44** | **PASS** | Two independent enforcement points. (a) Phase 8.5 EVALUABILITY GATE Independence column: "Yes -- independently verifiable without reading [name the excluded content]" required before Phase 9 opens; generic "independently verifiable" explicitly called incomplete; STOP CONDITION blocks Phase 9 until all rows populated. (b) Phase 9 terminal table Independence column: Phase 9 STOP CONDITION states "A terminal section... with Independence cells stating 'independently verifiable' without naming excluded content, is incomplete." Both enforcement points require named excluded content; the pre-Phase-9 gate removes the option to open Phase 9 without named exclusion; the Phase 9 STOP removes the option to close Phase 9 without the Independence column populated |

**Essential (C-01-C-05):** 5/5 PASS
**Recommended (C-06-C-08):** 3/3 PASS
**Aspirational (C-09-C-44):** 36/36 (all PASS)
**Aspirational score:** 36/36 x 100 = 100.0
**Composite:** 0.6 x 100 + 0.3 x 100 + 0.1 x 100 = **100.0**

---

## V-05 -- Output Format + Lifecycle Emphasis + Inertia Framing + Role Sequence

**Axis:** Same three-mechanism stack as V-04 plus ROLE: EVALUABILITY AUDITOR (between Phase 8 and Phase 9) with named exit gate EVALUABILITY GATE; Phase 9 opens with PREREQUISITE quoting gate identifier verbatim.

| ID | Score | Evidence |
|----|-------|---------|
| C-01-C-05 | PASS | Same five-field structure; same grounding; same scoring format |
| C-06-C-08 | PASS | Same tier-divergence and checklist structure |
| C-09-C-42 | PASS | All R13 structural mechanisms present; ROLE: EVALUABILITY AUDITOR is additive; Phase 9 PREREQUISITE adds entry condition without displacing any emit section |
| **C-43** | **PASS** | Phase 9 terminal CRITERION EVALUABILITY MAP produced as section 11; STOP CONDITION: "Emit is incomplete until section 11 is present as the final section, the EVALUABILITY GATE identifier appears in the Phase 9 PREREQUISITE header, the map contains one row per structural criterion with all four columns populated." Terminal position independently guaranteed by Phase 9's own emit manifest. Named artifact + scan method as distinct labeled columns satisfies C-43 |
| **C-44** | **PASS** | ROLE: EVALUABILITY AUDITOR EVALUABILITY GATE requires Independence field: "'Yes -- independently verifiable' without the exclusion name fails this column." Phase 9 PREREQUISITE quotes the gate identifier verbatim: "EVALUABILITY GATE: Criterion Evaluability Map with all C-NN rows populated, Verification Artifact and Scan Method named for every structural criterion, and Independence field naming excluded content for every row." The exclusion-naming requirement is embedded in Phase 9's entry condition -- an evaluator reading only Phase 9's header can confirm the Independence field requirement was stated as a gate condition, independently, without reading ROLE: EVALUABILITY AUDITOR's instruction body |

**Essential (C-01-C-05):** 5/5 PASS
**Recommended (C-06-C-08):** 3/3 PASS
**Aspirational (C-09-C-44):** 36/36 (all PASS)
**Aspirational score:** 36/36 x 100 = 100.0
**Composite:** 0.6 x 100 + 0.3 x 100 + 0.1 x 100 = **100.0**

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| V-04 | 100.0 | 100.0 | 100.0 | **100.0** | 1 (tied) |
| V-05 | 100.0 | 100.0 | 100.0 | **100.0** | 1 (tied) |
| V-02 | 100.0 | 100.0 | 98.611 | **99.861** | 3 |
| V-01 | 100.0 | 100.0 | 97.222 | **99.722** | 4 |
| V-03 | 100.0 | 100.0 | 95.833 | **99.583** | 5 |

All_essential_pass: true for all 5 variations.

---

## Discrimination Summary

| | C-43 | C-44 | Composite |
|-|------|------|-----------|
| V-01 | PASS | **FAIL** | 99.722 |
| V-02 | **PARTIAL** | PASS | 99.861 |
| V-03 | **PARTIAL** | **FAIL** | 99.583 |
| V-04 | PASS | PASS | **100.0** |
| V-05 | PASS | PASS | **100.0** |

**Isolation results confirmed:**
- V-01 vs V-02 (C-43): V-01 PASS (terminal production), V-02 PARTIAL (gate-reference) -- terminal production instruction in Phase 9 is load-bearing for C-43; a gate-reference without independent Phase 9 production is insufficient
- V-01 vs V-03 (C-43): V-01 PASS (formal table), V-03 PARTIAL (prose notes) -- column separation (labeled "Verification Artifact" and "Scan Method" as distinct table columns) is load-bearing; prose sentences conflating artifact and method do not satisfy the structural requirement
- V-01 vs V-02 (C-44): V-01 FAIL (no Independence column), V-02 PASS (gate forces exclusion naming) -- Phase 8.5 gate is the operative C-44 mechanism; absence of Independence column in Phase 9 table makes C-44 impossible regardless of STOP conditions
- V-04 vs V-05 (role-gate vs phase-gate): identical scores -- role-gate enforcement (ROLE: EVALUABILITY AUDITOR) is equivalent to phase-gate enforcement (Phase 8.5 EVALUABILITY GATE) for C-43/C-44

---

## Excellence Signals

**ES-R14-1** (V-04, V-05): Combined Phase 8.5 gate + Phase 9 terminal table makes C-44 a pre-condition enforced before Phase 9 opens, not an emit-time instruction directive.

V-01 places C-44 enforcement in Phase 9's terminal section instruction only -- C-44 fails because no Independence column exists. V-02 enforces C-44 at Phase 8.5 but only references the result in Phase 9 -- C-43 is PARTIAL because Phase 9 doesn't independently produce the terminal section. V-04 combines both: Phase 8.5 STOP CONDITION blocks Phase 9 until Independence is named (C-44 as pre-condition) AND Phase 9 independently produces the terminal four-column table (C-43 as emit-time structural requirement). The two enforcement points are non-redundant: removing Phase 8.5 makes C-44 fail even with a Phase 9 STOP CONDITION (V-01 confirms); removing Phase 9 terminal production makes C-43 PARTIAL even with a Phase 8.5 gate (V-02 confirms). The combination is necessary.

**ES-R14-2** (V-05 specific): Phase 9 PREREQUISITE quoting the EVALUABILITY GATE identifier verbatim makes evaluability sequencing independently auditable from Phase 9's entry condition alone -- the same independent-audit property C-41 captures for aspirational construction sequencing.

V-04 achieves C-43+C-44 PASS through phase-gate enforcement; V-05 achieves identical scores AND adds: Phase 9's PREREQUISITE states "EVALUABILITY GATE: Criterion Evaluability Map with all C-NN rows populated, Verification Artifact and Scan Method named for every structural criterion, and Independence field naming excluded content for every row." An evaluator reading only Phase 9 can confirm the Independence field requirement was stated as an entry condition without reading ROLE: EVALUABILITY AUDITOR's instruction body -- identical to how ROLE: BUILDER ASPIRATIONAL's PREREQUISITE makes the MECHANISM DEFINER GATE auditable from the role header alone (C-41). This structural property appears in V-05 but not V-04, is not captured by C-43 or C-44, and is a candidate for C-45 in R15.

---

## R14 to R15 Signal

V-04 and V-05 score identically (100.0), confirming role-gate enforcement is equivalent to phase-gate enforcement for C-43/C-44. ES-R14-2 identifies a property in V-05 beyond C-43/C-44: Phase 9 PREREQUISITE quoting the EVALUABILITY GATE identifier makes evaluability sequencing independently auditable from Phase 9 entry alone.

R15 should test: (a) whether Phase 9 PREREQUISITE quoting gate identifier is independently discriminating (candidate C-45), and (b) whether Phase 8.5 gate can be collapsed into Phase 9's terminal section instruction while preserving C-44 PASS -- if a Phase 9 Independence column requirement alone (no prior gate) achieves C-44, Phase 8.5 is eliminable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase 9 PREREQUISITE quoting the EVALUABILITY GATE identifier verbatim makes evaluability sequencing independently auditable from Phase 9 entry alone without reading the EVALUABILITY AUDITOR role body -- the same independent-audit property C-41 captures for aspirational construction sequencing, not yet captured by C-43 or C-44", "Phase 8.5 gate + Phase 9 terminal table are non-redundant enforcement points: Phase 8.5 makes C-44 a pre-Phase-9 structural condition removing the option to open Phase 9 without named excluded content, while Phase 9 terminal production makes C-43 an emit-time structural requirement removing the option to close Phase 9 without the formal table; the combination is necessary because each point fails independently when the other is removed"]}
```
