## /quest:score — quest-rubric R10 Scorecard

**Rubric:** quest-rubric-rubric-v10-2026-03-15.md
**Variations:** V-01 through V-05 (R10)
**Trace artifact:** placeholder (scoring from variation bodies directly)

---

## Criterion Reference

| Band | IDs | Active denominator notes |
|------|-----|--------------------------|
| Essential | C-01 – C-05 | All active for all variations |
| Recommended | C-06 – C-08 | All active for all variations |
| Aspirational | C-09 – C-32 | C-16, C-17 N/A (no revision phase); C-31 N/A for V-01/V-02/V-03/V-05, ACTIVE for V-04 |

---

## V-01 — R10 Full Integration Baseline

**Axis:** Dual-path evolution hook (AND-framing), source-destination secondary-effect framing, no novel elements.

### Essential

| ID | Evidence | Score |
|----|----------|-------|
| C-01 | Phase 2 checkpoint explicitly checks all five fields; imperative STOP AND REWRITE enforces | PASS |
| C-02 | Planning table header explicitly constrains "3–5 essential + 2–3 recommended + 1–2 aspirational" | PASS |
| C-03 | Phase 3 section list item 7: Scoring with "composite formula (60/30/10), golden threshold (all essential pass AND composite >= 80), PARTIAL handling, N/A handling" | PASS |
| C-04 | Phase 1 failure-mode enumeration gate + Phase 1 STOP CONDITION Gate 2 (no generic failure modes survive) → criteria derive from named failure modes by construction | PASS |
| C-05 | Phase 2 checkpoint "Binary pass condition: Observable signals only; no bare subjective qualifiers" + imperative STOP AND REWRITE | PASS |

**All essential PASS → all-essential-pass = TRUE**

### Recommended

| ID | Evidence | Score |
|----|----------|-------|
| C-06 | Phase 3 output order: Essential → Recommended → Aspirational | PASS |
| C-07 | Phase 1 planning table category column constrained to allowed 5; Gate 4 verifies category coverage | PASS |
| C-08 | Phase 1 STOP CONDITION Gate 3: "No two planning table rows describe the same failure mode. Merge or remove duplicates." | PASS |

### Aspirational (21 active — C-16, C-17, C-31 N/A)

| ID | Evidence | Score |
|----|----------|-------|
| C-09 | Phase 3 Notes requires C-15 self-application slot naming essential criterion + poor output; calibration signal present | PASS |
| C-10 | Contract item 1 AND-framing: BOTH 1a (version-tracking position) AND 1b (mechanism-note position) simultaneously required | PASS |
| C-11 | Phase 3 output order item 3: "Design Rationale (or equivalent block: failure inventory, dominant-failure-mode statement) — must appear before first criteria table; names the dominant failure mode" | PASS |
| C-12 | Phase 2 set-level banned-qualifier audit enumerates 8 terms explicitly; C-12 OR path satisfied (>= 3 pass conditions demonstrate the pattern) | PASS |
| C-13 | Contract item 3 explicitly: "Construction-time filter activity does not satisfy this — the rejection evidence must appear as a named section in the final output." Named section required. | PASS |
| C-14 | Phase 3 section list order: Design Rationale (3) before Essential Criteria (4) — ordering IS the positional gate | PASS |
| C-15 | Phase 3 DR requirement: "contains the self-application result (one essential criterion ID + description of a poor output that fails it) AND at least one named rejected generic criterion; these two items must be co-located in the same section, not distributed" | PASS |
| C-16 | No revision phase | N/A |
| C-17 | No revision phase | N/A |
| C-18 | Phase 2 set-level check enumerates: "good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate" — 8 terms, in construction section | PASS |
| C-19 | Phase 2 checkpoint row: "RPC compliance: co-presence gates are output-state checks — not a required construction mechanism" | PASS |
| C-20 | Phase 3 item 7 explicitly names Scoring section with "formula + threshold + calibration + evolution hook" as required output element | PASS |
| C-21 | Contract item 4: "Equivalence language: Pass conditions permitting non-canonical routes must contain the phrase 'or equivalent block' in the pass condition text" — propagates to generated rubric's C-11 and C-14 | PASS |
| C-22 | Contract item 3 explicitly disqualifies construction-time activity: "Construction-time filter activity does not satisfy this" — C-13 pass condition inherits this language | PASS |
| C-23 | Phase 3 DR: "co-located in the same section, not distributed to separate appendices or notes" — explicit co-location gate | PASS |
| C-24 | Phase 3 section list item 2 "Required Sections" appears before Essential Criteria (item 4) — front-loaded section manifest in the generated output | PASS |
| C-25 | Role definition (SetCoherenceAuditor) does not contain exact phrase "or equivalent block" — Contract item 4 achieves structural equivalence but not via role-definition-level anchor | PARTIAL |
| C-26 | Role definition has no "or equivalent block" phrase; output rubric would have >= 2 non-canonical-route pass conditions (Contract item 4 ensures this) — C-26 applies and fails | FAIL |
| C-27 | Phase 3 DR requires three distinct items (dominant failure mode, self-application, rejected criterion) but does not specify labeled sub-section structure for each — fusion risk unmitigated | PARTIAL |
| C-28 | Phase 3 section list positions Design Rationale (3) before Essential Criteria (4) — section list ordering is the positional gate, not a prose positional instruction | PASS |
| C-29 | Contract item 1b names canonical form: "'this rubric grows when quest-golden discovers excellence patterns' is the canonical form; 'this rubric should be updated over time' does not satisfy (1b)" | PASS |
| C-30 | Phase 1 (enumerate failure modes, all STOP gates) → Phase 2 (derive criteria from enumerated failure modes) — dedicated enumeration phase before criterion generation | PASS |
| C-31 | V-01 introduces no novel contract elements | N/A |
| C-32 | Contract item 1: "Both positions must be present simultaneously. A rubric satisfying only one path is PARTIAL on C-32, not PASS. The Contract must use AND-framing, not OR-framing." | PASS |

**Aspirational:** PASS×18 + PARTIAL×2 (C-25, C-27) + FAIL×1 (C-26) = 19.0/21

### V-01 Score

| Band | Calculation | Points |
|------|-------------|--------|
| Essential | (5/5) × 60 | 60.00 |
| Recommended | (3/3) × 30 | 30.00 |
| Aspirational | (19/21) × 10 | 9.05 |
| **Composite** | | **99.05** |

**All-essential-pass: TRUE | Golden: YES**

---

## V-02 — Phrasing Register (Imperative → Advisory Stops)

**Axis:** All STOP CONDITION and checkpoint failure-handling replaced with advisory language. Contract, planning table, checkpoint structure retained structurally.

### Essential

| ID | Evidence | Score |
|----|----------|-------|
| C-01 | Checkpoint still lists all five fields; but "please consider rewriting" reduces enforcement reliability — structural gate softened | PASS |
| C-02 | Planning table header and "Up to 3–5 essential + 2–3 recommended + 1–2 aspirational" constraint present | PASS |
| C-03 | Phase 3 section list includes Scoring with required content | PASS |
| C-04 | Planning phase exists with failure-mode enumeration, but STOP CONDITION Gate 2 advisory: "Please check that each failure-mode entry is specific" — gateway to generic criteria opened | PARTIAL |
| C-05 | Phase 2 checkpoint advisory: "please consider rewriting the criterion before continuing" — binary-condition enforcement weakened; subjective qualifiers can survive | PARTIAL |

**C-04 and C-05 PARTIAL → all-essential-pass = FALSE**

### Recommended

| ID | Evidence | Score |
|----|----------|-------|
| C-06 | Phase 3 output order unchanged | PASS |
| C-07 | Category constraint in planning table unchanged | PASS |
| C-08 | "It is advisable to confirm no two rows describe the same failure mode" — advisory distinctness gate; overlap risk unmitigated | PARTIAL |

### Aspirational (21 active)

| ID | Evidence | Score |
|----|----------|-------|
| C-09 | Notes C-15 self-application instruction present but advisory enforcement weakens calibration reliability | PARTIAL |
| C-10 | Contract item 1 advisory: "It is recommended that both positions be present simultaneously... please include both where possible" — not AND-enforced; single-path completion may satisfy | PARTIAL |
| C-11 | Phase 3 Design Rationale section required in output order; dominant failure mode naming stated | PASS |
| C-12 | Phase 2 set-level check still lists banned terms; advisory enforcement weakens "no bare qualifiers" gate | PARTIAL |
| C-13 | Contract item 3: "should contain a named rejection log section" — advisory; not mandatory | PARTIAL |
| C-14 | Section ordering unchanged — positional gate structural, not enforcement-dependent | PASS |
| C-15 | Phase 3 DR requirement co-location still stated; advisory delivery reduces enforcement reliability | PARTIAL |
| C-16 | No revision phase | N/A |
| C-17 | No revision phase | N/A |
| C-18 | Phase 2 set-level check enumerates banned terms explicitly — list-level enforcement independent of advisory register | PASS |
| C-19 | Co-presence check present; output-state specification structural, not register-dependent | PASS |
| C-20 | Scoring section in Phase 3 output list | PASS |
| C-21 | Contract item 4: "should contain 'or equivalent block'" — advisory; C-11 and C-14 pass conditions may omit the phrase | PARTIAL |
| C-22 | Contract item 3 does not explicitly disqualify construction-time filter activity; "in the final output" implies it but doesn't state it — explicit disqualification absent | FAIL |
| C-23 | Phase 3 DR co-location requirement stated but advisory framing reduces enforcement | PASS |
| C-24 | Phase 3 Required Sections at position 2 in generated output | PASS |
| C-25 | Role definition lacks "or equivalent block" phrase | PARTIAL |
| C-26 | Role definition lacks phrase; output rubric has >= 2 non-canonical pass conditions → C-26 active and fails | FAIL |
| C-27 | No labeled sub-section structure in DR specified | PARTIAL |
| C-28 | Section list ordering positional gate; structural | PASS |
| C-29 | Contract item 1b names canonical form but advisory framing: "naming the specific trigger event — 'this rubric grows...' is the canonical form" — advisory register may not enforce specific trigger | PARTIAL |
| C-30 | Phase 1 → Phase 2 sequence present; phase structure itself is structural, register affects enforcement within phases but not phase existence | PASS |
| C-31 | No novel elements | N/A |
| C-32 | Contract item 1 advisory AND-framing — "recommended" not "required"; PARTIAL not PASS | PARTIAL |

**Aspirational:** PASS×9 + PARTIAL×10 (C-09,C-10,C-12,C-13,C-15,C-21,C-25,C-27,C-29,C-32) + FAIL×2 (C-22,C-26) = 14.0/21

### V-02 Score

| Band | Calculation | Points |
|------|-------------|--------|
| Essential | (4.0/5) × 60 | 48.00 |
| Recommended | (2.5/3) × 30 | 25.00 |
| Aspirational | (14/21) × 10 | 6.67 |
| **Composite** | | **79.67** |

**All-essential-pass: FALSE | Golden: NO**

---

## V-03 — Output Format (5-Column Table → Prose Failure-Mode Notes)

**Axis:** Planning table replaced with prose failure-mode notes per criterion group. Imperative STOP language retained. Contract unchanged. Phase 2 adds "Traceable to a failure mode" checkpoint row.

### Essential

| ID | Evidence | Score |
|----|----------|-------|
| C-01 | Phase 2 checkpoint retains all-five-fields check; imperative STOP AND REWRITE | PASS |
| C-02 | Prose notes Phase 1 STOP CONDITION: "At least 3 distinct named failure modes" — no upper bound, no 2–3 recommended / 1–2 aspirational constraint; count distribution unenforced | PARTIAL |
| C-03 | Phase 3 output list includes Scoring with required content | PASS |
| C-04 | Phase 2 adds "Traceable to a failure mode" checkpoint row (absent in V-01); prose notes require failure-mode naming before generation | PASS |
| C-05 | Imperative STOP AND REWRITE unchanged; binary-condition checkpoint present | PASS |

**C-02 PARTIAL → all-essential-pass = FALSE**

### Recommended

| ID | Evidence | Score |
|----|----------|-------|
| C-06 | Phase 3 output order unchanged | PASS |
| C-07 | Category coverage required in Phase 1 STOP CONDITION ("Coverage spanning at least 3 of 5 criterion categories") — categories from allowed set | PASS |
| C-08 | Phase 1 STOP CONDITION requires "at least 3 distinct named failure modes" (minimum 3, not 4); prose format makes overlap detection harder than structured columns | PARTIAL |

### Aspirational (21 active)

| ID | Evidence | Score |
|----|----------|-------|
| C-09 | Notes C-15 self-application slot required in Phase 3 | PASS |
| C-10 | Contract item 1 AND-framing unchanged | PASS |
| C-11 | Phase 3 Design Rationale required before criteria; dominant failure mode naming | PASS |
| C-12 | Phase 2 set-level: "No bare: good / sufficient / appropriate / clear / complete / thorough" — 6 terms enumerated; C-12 OR path satisfied | PASS |
| C-13 | Contract item 3 AND-framing: "Named rejection log section in the output document with >= 3 explicitly rejected generic criterion examples. Named section, not inline filtering." | PASS |
| C-14 | Section list ordering — Design Rationale before Essential | PASS |
| C-15 | Phase 3 DR: "contains self-application result AND named rejected generic criterion; co-located" | PASS |
| C-16 | N/A | N/A |
| C-17 | N/A | N/A |
| C-18 | Phase 2 set-level lists 6 banned terms explicitly | PASS |
| C-19 | Co-presence checkpoint present; output-state only | PASS |
| C-20 | Phase 3 Scoring section named in output list | PASS |
| C-21 | Contract item 4 with "or equivalent block" requirement | PASS |
| C-22 | Contract item 3: "Named section, not inline filtering" explicitly disqualifies construction-time; C-13 inherits this | PASS |
| C-23 | Phase 3 DR co-location requirement | PASS |
| C-24 | Phase 3 output list includes Required Sections at position 2 | PASS |
| C-25 | Role definition lacks "or equivalent block" phrase | PARTIAL |
| C-26 | Role definition lacks phrase; >= 2 non-canonical pass conditions predicted | FAIL |
| C-27 | No sub-section label structure specified for DR items | PARTIAL |
| C-28 | Section list ordering is positional gate | PASS |
| C-29 | Contract item 1b names canonical form | PASS |
| C-30 | Phase 1 (prose failure-mode notes, enumeration before Phase 2) → Phase 2 (derive from notes) — dedicated enumeration phase present | PASS |
| C-31 | No novel elements | N/A |
| C-32 | Contract item 1 AND-framing unchanged | PASS |

**Aspirational:** PASS×18 + PARTIAL×2 (C-25, C-27) + FAIL×1 (C-26) = 19.0/21

### V-03 Score

| Band | Calculation | Points |
|------|-------------|--------|
| Essential | (4.5/5) × 60 | 54.00 |
| Recommended | (2.5/3) × 30 | 25.00 |
| Aspirational | (19/21) × 10 | 9.05 |
| **Composite** | | **88.05** |

**All-essential-pass: FALSE | Golden: NO**

---

## V-04 — Inertia Framing (Primary Competitor: Status Quo preamble)

**Axis:** Pre-Phase-1 "Primary Competitor: Status Quo" block added. Novel contract element → C-31 active. Fifth Contract requirement. Extra checkpoint row.

### Essential

| ID | Evidence | Score |
|----|----------|-------|
| C-01 | Phase 2 checkpoint all-five-fields; imperative STOP AND REWRITE | PASS |
| C-02 | Phase 1 planning table header constrains 3–5/2–3/1–2 distribution | PASS |
| C-03 | Phase 3 Scoring section in output list | PASS |
| C-04 | Primary Competitor preamble names dominant failure mode before Phase 1 begins — all subsequent criteria must contend with a named enemy; Phase 1 Gate 2 adds "trace to target skill, not generic document quality" with direct reference to inertia anchor | PASS |
| C-05 | Imperative STOP AND REWRITE; binary-condition checkpoint unchanged | PASS |

**All essential PASS → all-essential-pass = TRUE**

### Recommended

| ID | Evidence | Score |
|----|----------|-------|
| C-06 | Phase 3 output order: Essential → Recommended → Aspirational | PASS |
| C-07 | Category constraint in planning table; Gate 4 category coverage check | PASS |
| C-08 | Phase 1 Gate 3: "No two rows describe the same failure mode" — imperative; Primary Competitor preamble front-loads the dominant failure mode, reducing chance of duplicate entries | PASS |

### Aspirational (22 active — C-16, C-17 N/A; C-31 ACTIVE)

| ID | Evidence | Score |
|----|----------|-------|
| C-09 | Notes C-15 self-application slot; calibration present | PASS |
| C-10 | Contract item 1 AND-framing unchanged | PASS |
| C-11 | Primary Competitor block ("naming the dominant inertia pattern for the target skill") + Design Rationale both before criteria tables; strongest C-11 mechanism in R10 | PASS |
| C-12 | Phase 2 set-level lists: "good / sufficient / appropriate / clear / complete / thorough" (6 terms); C-12 OR path | PASS |
| C-13 | Contract item 3 AND-framing with construction-time disqualification | PASS |
| C-14 | Phase 3 output order: Primary Competitor block + Design Rationale both listed before Essential Criteria | PASS |
| C-15 | Phase 3 DR co-location requirement | PASS |
| C-16 | N/A | N/A |
| C-17 | N/A | N/A |
| C-18 | Phase 2 set-level lists 6 banned terms | PASS |
| C-19 | Co-presence checkpoint present | PASS |
| C-20 | Phase 3 Scoring in output list | PASS |
| C-21 | Contract item 4 with "or equivalent block" | PASS |
| C-22 | Contract item 3 construction-time disqualification explicit | PASS |
| C-23 | Phase 3 DR co-location requirement | PASS |
| C-24 | Phase 3 includes Required Sections at position 2 in output list | PASS |
| C-25 | Role definition lacks "or equivalent block" phrase; role definition is extended (adds Primary Competitor preamble duty) but phrase absent | PARTIAL |
| C-26 | Role definition lacks phrase despite extension; >= 2 non-canonical pass conditions predicted | FAIL |
| C-27 | No labeled sub-sections for DR items specified | PARTIAL |
| C-28 | Section list ordering: Primary Competitor block, Design Rationale, then Essential Criteria — both pre-criteria positions established via section list | PASS |
| C-29 | Contract item 1b names canonical trigger event | PASS |
| C-30 | Phase 1 (failure-mode enumeration, imperative gates) → Phase 2 (criterion derivation); Primary Competitor preamble anchors Phase 0 failure-mode context pre-Phase-1 | PASS |
| C-31 | V-04 introduces one novel element (Primary Competitor preamble block); Phase 2 SetCoherenceAuditor checkpoint adds dedicated row "Primary Competitor preamble block present" — prevents silent drop | PASS |
| C-32 | Contract item 1 AND-framing | PASS |

**Aspirational:** PASS×19 + PARTIAL×2 (C-25, C-27) + FAIL×1 (C-26) = 20.0/22

### V-04 Score

| Band | Calculation | Points |
|------|-------------|--------|
| Essential | (5/5) × 60 | 60.00 |
| Recommended | (3/3) × 30 | 30.00 |
| Aspirational | (20/22) × 10 | 9.09 |
| **Composite** | | **99.09** |

**All-essential-pass: TRUE | Golden: YES**

---

## V-05 — Lifecycle Emphasis (Phase 1 Removed)

**Axis:** Phase 1 planning eliminated. 2-phase structure (Generate+Checkpoint → Emit). Failure-mode enumeration relocated to Contract item 2 (satisfied via output rubric's Design Rationale). Inline failure-mode naming substitutes for planning table.

### Essential

| ID | Evidence | Score |
|----|----------|-------|
| C-01 | Phase 2 checkpoint all-five-fields; imperative STOP AND REWRITE | PASS |
| C-02 | No Phase 1 planning table to constrain essential/recommended/aspirational counts; output section structure separates bands but count ranges (3-5/2-3/1-2) unenforced during generation | PARTIAL |
| C-03 | Phase 3 Scoring section in output list | PASS |
| C-04 | Inline "briefly name the failure mode" is weaker structural guarantee than dedicated Phase 1 — failure-mode anchor exists but no STOP gate enforces it before criterion generation begins | PARTIAL |
| C-05 | Imperative STOP AND REWRITE in Phase 2; binary-condition check present | PASS |

**C-02 and C-04 PARTIAL → all-essential-pass = FALSE**

### Recommended

| ID | Evidence | Score |
|----|----------|-------|
| C-06 | Phase 3 output order unchanged | PASS |
| C-07 | Category coverage not pre-constrained in planning (no Phase 1 table); Phase 2 set-level check spans categories reactively | PASS |
| C-08 | Phase 2 "No duplicate failure mode" check present but no pre-generation distinctness gate; overlap more likely without Phase 1 planning table | PARTIAL |

### Aspirational (21 active — C-16, C-17, C-31 N/A)

| ID | Evidence | Score |
|----|----------|-------|
| C-09 | Notes C-15 self-application slot | PASS |
| C-10 | Contract item 1 AND-framing unchanged | PASS |
| C-11 | Phase 3: "Design Rationale (or equivalent block, before first criteria table — this section satisfies the Phase 0 failure-mode enumeration Contract requirement)" | PASS |
| C-12 | Phase 2 set-level: "No bare: good / sufficient / appropriate / clear / complete / thorough" | PASS |
| C-13 | Contract item 3: Named rejection log, construction-time disqualification, >= 3 entries required | PASS |
| C-14 | Section list ordering: Design Rationale before Essential Criteria | PASS |
| C-15 | Phase 3 DR co-location requirement | PASS |
| C-16 | N/A | N/A |
| C-17 | N/A | N/A |
| C-18 | Phase 2 set-level lists 6 banned terms | PASS |
| C-19 | Co-presence checkpoint present | PASS |
| C-20 | Phase 3 Scoring in output list | PASS |
| C-21 | Contract item 4 "or equivalent block" | PASS |
| C-22 | Contract item 3 construction-time disqualification explicit | PASS |
| C-23 | Phase 3 DR co-location | PASS |
| C-24 | Phase 3 Required Sections at position 2 in output list | PASS |
| C-25 | Role definition lacks "or equivalent block" phrase | PARTIAL |
| C-26 | Role definition lacks phrase; >= 2 non-canonical pass conditions predicted | FAIL |
| C-27 | No sub-section labels for DR items | PARTIAL |
| C-28 | Section list ordering is positional gate | PASS |
| C-29 | Contract item 1b names canonical trigger | PASS |
| C-30 | **No dedicated Phase 1 enumeration phase** — Contract item 2 relocates failure-mode enumeration to the OUTPUT rubric's Design Rationale rather than to the skill's own phase structure; skill construction protocol lacks the required enumeration-before-derivation phase sequence | FAIL |
| C-31 | No novel elements | N/A |
| C-32 | Contract item 1 AND-framing | PASS |

**Aspirational:** PASS×17 + PARTIAL×2 (C-25, C-27) + FAIL×2 (C-26, C-30) = 18.0/21

### V-05 Score

| Band | Calculation | Points |
|------|-------------|--------|
| Essential | (4.0/5) × 60 | 48.00 |
| Recommended | (2.5/3) × 30 | 25.00 |
| Aspirational | (18/21) × 10 | 8.57 |
| **Composite** | | **81.57** |

**All-essential-pass: FALSE | Golden: NO**

---

## Round Summary

| Variation | Composite | All-Essential | Golden | Notes |
|-----------|-----------|---------------|--------|-------|
| V-04 | **99.09** | TRUE | YES | Primary Competitor preamble + C-31 PASS |
| V-01 | 99.05 | TRUE | YES | Full baseline; C-31 N/A |
| V-03 | 88.05 | FALSE | NO | C-02 PARTIAL: prose format loses count constraint |
| V-05 | 81.57 | FALSE | NO | C-02/C-04 PARTIAL, C-30 FAIL |
| V-02 | 79.67 | FALSE | NO | C-04/C-05 PARTIAL; C-22/C-26 FAIL |

**C-07 axis breadth:** 4 of 6 families (phrasing register, output format, inertia framing, lifecycle emphasis). **SET-LEVEL PASS.**

**C-31 confirmation:** V-04 introduces one novel element and adds exactly one dedicated checkpoint row — C-31 PASS confirmed. Zero silent drop.

**C-32 confirmation:** All five variation bodies encode evolution hook as AND requirement. Dual-path baseline established; R9 single-path ablation evidence not re-run.

---

## Excellence Signals — V-04 (Top)

**Signal 1 — Pre-phase enemy anchor is a stronger inertia filter than DR-inertia statement alone.**
V-04's "Primary Competitor: Status Quo" block precedes Phase 1. This means the planning table's failure-mode column must contend with a named enemy before any criterion is drafted. C-11 (inertia framing in Design Rationale) requires the enemy statement in the DR section; V-04 additionally front-loads the enemy before Phase 1, making every planning row a response to the named inertia output. Phase 1 Gate 2 explicitly says "trace to target skill — no entry that could apply to any document survives this gate" with direct reference to the preamble as the inertia anchor. V-01's Phase 1 Gate 2 lacks this explicit pointer back to a named enemy.

**Signal 2 — C-31 checkpoint row technique confirmed: one novel element → one dedicated row → zero silent drop.**
V-04 introduces one novel Contract requirement (Primary Competitor preamble) and immediately adds one checkpoint row ("Primary Competitor preamble block present") to the Phase 2 SetCoherenceAuditor. The set-level design notes confirm this was intentional and scoped precisely. The v11 candidate `c31-checkpoint-row-minimum-count-scales-with-contract-depth` now has a confirmed baseline (1:1 element-to-row mapping works; test needed for 2:1 ratio to confirm the second element silently drops).

**Signal 3 — Source-destination secondary-effect framing (R10→R11 candidate test established).**
V-01/V-02/V-03 hypotheses name both transfer endpoints: "shifts token-budget pressure FROM [source] TO [destination]." V-04/V-05 use directionless tradeoff assertions ("may reduce," "trading structural enforcement for"). The R10→R11 candidate for C-34 (`secondary-effect-source-destination-directionality`) now has a clean comparison baseline: if downstream scoring detects C-18 degradation from V-04/V-05's directional framing vs V-01/V-02/V-03's endpoint-named framing, the candidate crosses threshold.

---

## R10 Set-Level Findings

**C-07 SET-LEVEL PASS** — 4 axis families tested (R9 had 3; R10 recovers breadth deficit).

**Advisory register (V-02 79.67) degrades more than absent planning structure (V-05 81.57).** V-02's advisory framing collapses C-04 and C-05 and propagates partial scores through 10 aspirational criteria simultaneously. V-05's absent Phase 1 costs C-02, C-04, C-08, and C-30 but the imperative enforcement of Phase 2 contains the damage. Register choice is a higher-leverage structural variable than lifecycle phase presence.

**Prose format (V-03 88.05) loses only C-02** — the count constraint is the single mechanism the 5-column table enforces that prose notes cannot. All other structural guarantees (failure-mode derivation, binary conditions, section completeness) survive the format change. This makes C-02's count constraint a disproportionately impactful criterion: it's the only essential criterion whose gate depends on a structural format feature.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["pre-phase-enemy-anchor-provides-persistent-inertia-filter-stronger-than-dr-inertia-statement-alone", "secondary-effect-source-destination-endpoint-naming-enables-tradeoff-detection-candidate-c34"]}
```
