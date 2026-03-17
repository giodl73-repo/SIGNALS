## org-scan Quest Score — Round 8

**All 5 variations score 100.** The R8 author explicitly targeted all 32 criteria in every variation, and all placement is confirmed.

---

### Criterion results by variation

All 32 criteria — C-01 through C-32 — PASS in all 5 variations. The new R8 criteria (C-29 through C-32) each have verbatim placement confirmed:

| New Criterion | All 5 pass? | Strongest implementation |
|---|---|---|
| C-29 schema violation label | YES | V-02/V-05 — two-sentence treatment with framing sentence before violation label |
| C-30 universal governing statement | YES | V-02 — appears before all instructions (schema-first design makes it structurally primary) |
| C-31 named phase boundary header | YES | V-02/V-05 — exact GROUP A / GROUP B format matching rubric example |
| C-32 sequential evaluation enforcement | YES | V-03 — adds named gate entry condition as pre-checklist precondition |

---

### Ranking (all at 100, ranked by robustness)

1. **V-03** — gate entry condition adds a pre-gate checkpoint; phase exit conditions mirror gate conditions for dual enforcement
2. **V-02** — schema-first design; strongest C-29 with two-sentence framing + violation label
3. **V-04** — most analytically rich: Behavioral Signals column in dictionary, Hypothesis Held tracking column, prediction-not-resolved gap type
4. **V-05** — tightest command register; C-29 appears twice (schema note + gate item 5)
5. **V-01** — solid baseline; no implementation distinguishes it from prior rounds

---

### Excellence signals (candidates for C-33+)

1. **Named gate entry condition** (V-03) — requires the phase completion statement to be written before gate evaluation can begin; sequential enforcement on the gate itself, not just within the gate
2. **Behavioral signals column in dictionary** (V-04) — adds human-observable behavioral tells alongside code-structural tells; dual-register dictionary
3. **Hypothesis confirmation tracking column** (V-04) — `Hypothesis Held: yes / no / partial` links scan rows to Phase 1 predictions; combined with TABLE A and the "prediction not resolved" gap type, forms a complete hypothesis-test-result loop

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named gate entry condition requires phase completion statement before checklist evaluation begins adding pre-gate checkpoint distinct from sequential item evaluation", "behavioral signals column in inertia dictionary adds human-observable tells alongside structural code tells making dictionary dual-register", "hypothesis confirmation tracking column links scan evidence rows to prior predictions with yes/no/partial vocabulary enabling machine-verifiable prediction outcome loop"]}
```
ER begins; PASS TOKEN and FAIL TOKEN as named constants |
| C-21 | PASS | OUTPUT SCHEMA (COMPLETE): all 6 tables declare Status REQUIRED / optional for every column |
| C-22 | PASS | "Phase 1 postcondition: SCANNER has covered 3+ source types..." + "Phase 2 precondition: Phase 1 postcondition is satisfied and the PASS TOKEN is written." |
| C-23 | PASS | INERTIA PATTERN DICTIONARY with 7 enumerated labels before SCANNER begins |
| C-24 | PASS | PASS TOKEN encodes N sources scanned, M paths collected, dominant pattern label |
| C-25 | PASS | "Column order is a structural constraint. Inertia Match precedes File Path Evidence in every row." GATEKEEPER item 5 verifies column order |
| C-26 | PASS | Dictionary: "Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable." |
| C-27 | PASS | "This schema governs every table in this skill. Status applies to every column." All tables annotate Status for every column including optional Confidence |
| C-28 | PASS | "These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins." |
| C-29 | PASS | "Inverting the order is a schema violation." in column-order structural constraint sentence |
| C-30 | PASS | "This schema governs every table in this skill. Status applies to every column." as opening OUTPUT SCHEMA governing statement |
| C-31 | PASS | "SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION:" -- named phase boundary header as structurally identifiable element |
| C-32 | PASS | "Evaluate each item in order; do not skip:" in GATEKEEPER checklist |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 24/24 → capped at 10
**Score: 100**

---

#### V-02 — Output Format

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 | PASS | "Anti-fabrication rule (synthesis): Every GROUP B claim must trace to a TABLE A row." |
| C-02 | PASS | GROUP A: all 7 source types listed; "Cover at least 3 of the 7" |
| C-03 | PASS | TABLE D schema + "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on TABLE D rows.]" |
| C-04 | PASS | TABLE C: Concern Name, Boundaries Crossed, Boundary Note all REQUIRED |
| C-05 | PASS | Preamble: "(stated here; restated in output schema)"; output schema: "CRITICAL CONSTRAINT (restated in output schema): TABLE A through TABLE F are raw analysis. No org chart." |
| C-06 | PASS | TABLE B: Boundary Name, Inertia Match, File Path Evidence, Seam Rationale all REQUIRED |
| C-07 | PASS | TABLE E: Dimension (Current/Recommended), Shape, Justification, Dominant Inertia Pattern all REQUIRED; two rows instruction in GROUP B |
| C-08 | PASS | TABLE F: Gap Type, Description, Resolution Condition all REQUIRED; "Do not omit gaps to appear complete" |
| C-09 | PASS | TABLE A: "5-path floor is a gate precondition"; GROUP A / GROUP B gate item 2 enforces and halts |
| C-10 | PASS | TABLE E: "Exactly two rows -- one for Current State, one for Recommended State. ... Separate current state from recommended state clearly -- label each." |
| C-11 | PASS | "Anti-fabrication rule (scan)" in GROUP A + "Anti-fabrication rule (synthesis)" in GROUP B |
| C-12 | PASS | "GROUP A / GROUP B BOUNDARY: GATE EVALUATION: This boundary is a hard sequencing gate. GROUP B cannot begin until the gate is complete and the PASS TOKEN is written." |
| C-13 | PASS | Preamble + output schema restates constraint; CRITICAL CONSTRAINT is the last line of the OUTPUT SCHEMA block |
| C-14 | PASS | Gate: 5-item numbered checklist; "Evaluate each item in order; do not skip:" |
| C-15 | PASS | "GROUP A -- SCAN PHASE" and "GROUP B -- SYNTHESIS PHASE" -- exact GROUP A / GROUP B labels matching rubric example |
| C-16 | PASS | TABLE A: "5-path floor is a gate precondition"; "If item 2 fails: Write 'Path floor not met'. Halt. Do not produce GROUP B output." |
| C-17 | PASS | PASS TOKEN: named-token format with source count, path count, dominant pattern |
| C-18 | PASS | FAIL TOKEN: "Path floor not met" as named constant |
| C-19 | PASS | TABLE A: Inertia Match REQUIRED; "Dictionary label only -- free text invalid" |
| C-20 | PASS | "GATE TOKEN PROTOCOL" named block before GROUP A begins; both tokens as named constants |
| C-21 | PASS | "OUTPUT SCHEMA (COMPLETE -- defined before instructions to govern all phases)": all 6 tables declare Status for every column |
| C-22 | PASS | Phase 1 postcondition + Phase 2 precondition + "These two blocks name the same contract from both sides. Both must hold before GROUP B begins." |
| C-23 | PASS | INERTIA PATTERN DICTIONARY with 7 enumerated labels before GROUP A begins |
| C-24 | PASS | PASS TOKEN encodes N sources, M paths, dominant pattern |
| C-25 | PASS | "Column order rule: Inertia Match precedes File Path Evidence in every row. This is a schema constraint, not a display preference." Gate item 5 verifies column order |
| C-26 | PASS | Dictionary: invalidity statement verbatim |
| C-27 | PASS | "This schema governs every table in this skill. Status applies to every column." All 6 tables fully annotated including optional Confidence |
| C-28 | PASS | "These two blocks name the same contract from both sides. Both must hold before GROUP B begins." |
| C-29 | PASS | "Inverting the order is a schema violation." added to column order rule sentence in TABLE A schema |
| C-30 | PASS | "This schema governs every table in this skill. Status applies to every column." as schema-first opening governing statement |
| C-31 | PASS | "GROUP A / GROUP B BOUNDARY: GATE EVALUATION:" -- named phase boundary header |
| C-32 | PASS | "Evaluate each item in order; do not skip:" in gate checklist |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 24/24 → capped at 10
**Score: 100**

---

#### V-03 — Lifecycle Emphasis

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 | PASS | "SECTION 2.1: Name each distinct area of work. Every area must cite the SCAN TABLE row(s) that evidence it." |
| C-02 | PASS | Phase 1 lists all 7 source types with extraction instructions; 3+ required |
| C-03 | PASS | SECTION 2.4: Headcount Table + "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences drawing on Headcount Table rows above.]" |
| C-04 | PASS | SECTION 2.3: Cross-Cutting Concerns Table with Concern Name, Boundaries Crossed, Boundary Note all REQUIRED |
| C-05 | PASS | Preamble + PHASE 2 entry: "CRITICAL CONSTRAINT (restated at Phase 2 entry): This skill produces raw analysis only." |
| C-06 | PASS | SECTION 2.2: Team Boundaries Table with Boundary Name, Inertia Match, File Path Evidence, Seam Rationale all REQUIRED |
| C-07 | PASS | SECTION 2.5: Org Shape Table with exactly two rows, Justification column, Dominant Inertia Pattern column |
| C-08 | PASS | SECTION 2.6: Evidence Gaps Table with optional "Affected Sections" column; "Do not omit gaps to appear complete" |
| C-09 | PASS | Phase 1 exit conditions: "At least 5 distinct file paths present across File Path Evidence column"; gate checks and halts on failure |
| C-10 | PASS | SECTION 2.5: "Produce the Org Shape Table with exactly two rows: Current State and Recommended State. ... Separate current state from recommended state clearly -- label each." |
| C-11 | PASS | "Anti-fabrication rule (Phase 1)" in scan phase + "Anti-fabrication rule (Phase 2)" in synthesis phase |
| C-12 | PASS | "PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION: This boundary is a hard sequencing gate. Phase 2 cannot begin until gate evaluation is complete and the PASS TOKEN is written." |
| C-13 | PASS | Preamble + OUTPUT SCHEMA governs all tables + PHASE 2 entry restates constraint |
| C-14 | PASS | Gate: 5-item numbered checklist; "Evaluate each item in order; do not skip:" |
| C-15 | PASS | "PHASE 1: EVIDENCE COLLECTION" and "PHASE 2: SYNTHESIS" -- discrete named phases with explicit entry/exit conditions per phase |
| C-16 | PASS | Phase 1 exit conditions include path floor; "If item 2 fails: Write 'Path floor not met'. Halt. Do not begin Phase 2." |
| C-17 | PASS | PASS TOKEN: "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]" |
| C-18 | PASS | "If item 2 fails: Write 'Path floor not met'. Halt." |
| C-19 | PASS | SCAN TABLE: Inertia Match REQUIRED; dictionary values only; GATEKEEPER item 3 verifies non-empty |
| C-20 | PASS | "GATE TOKEN PROTOCOL / Both tokens are defined here as constants before Phase 1 begins." |
| C-21 | PASS | "This schema governs every table in this skill. Status applies to every column." All tables annotate Status for every column |
| C-22 | PASS | Phase 1 postcondition + Phase 2 precondition + "These two blocks name the same contract from both sides. Both must hold before Phase 2 begins." |
| C-23 | PASS | INERTIA PATTERN DICTIONARY: "Internalize this dictionary before Phase 1 begins." 7 enumerated labels |
| C-24 | PASS | PASS TOKEN encodes N sources, M paths, dominant pattern |
| C-25 | PASS | "Column order is a structural constraint. Inertia Match precedes File Path Evidence in every row." Gate item 5 verifies |
| C-26 | PASS | Dictionary: invalidity statement verbatim |
| C-27 | PASS | "This schema governs every table in this skill. Status applies to every column." All scan and synthesis tables fully annotated |
| C-28 | PASS | "These two blocks name the same contract from both sides. Both must hold before Phase 2 begins." |
| C-29 | PASS | "Inverting the order is a schema violation." in column-order structural constraint |
| C-30 | PASS | "This schema governs every table in this skill. Status applies to every column." as opening OUTPUT SCHEMA governing statement |
| C-31 | PASS | "PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:" -- named phase boundary header |
| C-32 | PASS | "Evaluate each item in order; do not skip:" in gate checklist; additionally: "Gate entry condition: The PHASE 1 COMPLETE statement has been written." adds named precondition before evaluation begins |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 24/24 → capped at 10
**Score: 100**

---

#### V-04 — Inertia Framing + Output Format

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 | PASS | "Anti-fabrication rule (Phase 3): Every claim must trace to a TABLE B row. Unlabeled inference is prohibited." |
| C-02 | PASS | Phase 2: all 7 source types; "Cover at least 3 of the 7" |
| C-03 | PASS | TABLE E + "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences from TABLE E rows.]" |
| C-04 | PASS | TABLE D: Concern Name, Boundaries Crossed, Boundary Note all REQUIRED |
| C-05 | PASS | Preamble + OUTPUT SCHEMA + Phase 3: three-location restatement; final: "CRITICAL CONSTRAINT (restated): This skill produces raw analysis only." |
| C-06 | PASS | TABLE C: Boundary Name, Inertia Match, File Path Evidence, Seam Rationale all REQUIRED |
| C-07 | PASS | TABLE F: two rows (Current State / Recommended State), Justification, Dominant Inertia Pattern all REQUIRED |
| C-08 | PASS | TABLE G: Gap Type, Description, Resolution Condition; includes "prediction not resolved" as a named gap type for TABLE A hypotheses not confirmed or disconfirmed |
| C-09 | PASS | TABLE B: "5-path floor is a gate precondition"; gate item 2 enforces and halts |
| C-10 | PASS | TABLE F: "Exactly two rows (Current State, Recommended State). Reference the dominant inertia pattern from the PASS TOKEN. Separate current state from recommended state clearly -- label each." |
| C-11 | PASS | Anti-fabrication rules in Phase 2 (Evidence Collection) and Phase 3 (Synthesis) |
| C-12 | PASS | "PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION: This boundary is a hard sequencing gate. Phase 3 cannot begin until the gate is complete and the PASS TOKEN is written." |
| C-13 | PASS | Preamble + OUTPUT SCHEMA + Phase 3 -- three restatements; most restatement-dense variation |
| C-14 | PASS | Gate: 5-item numbered checklist; "Evaluate each item in order; do not skip:" |
| C-15 | PASS | "PHASE 1: PATTERN CLASSIFICATION" / "PHASE 2: EVIDENCE COLLECTION" / "PHASE 3: SYNTHESIS" -- three discrete named phases |
| C-16 | PASS | TABLE B: "5-path floor is a gate precondition"; "If item 2 fails: Write 'Path floor not met'. Halt. Do not begin Phase 3." |
| C-17 | PASS | PASS TOKEN: named-token format with source count, path count, dominant pattern |
| C-18 | PASS | FAIL TOKEN: "Path floor not met" as named constant |
| C-19 | PASS | TABLE B: Inertia Match REQUIRED; "this column precedes File Path Evidence"; Hypothesis Held optional column links evidence back to TABLE A predictions |
| C-20 | PASS | "GATE TOKEN PROTOCOL" named block before any phase begins |
| C-21 | PASS | "This schema governs every table in this skill. Status applies to every column." All 7 tables (A-G) annotate Status for every column |
| C-22 | PASS | Phase 2 postcondition + Phase 3 precondition + "These two blocks name the same contract from both sides. Both must hold before Phase 3 begins." |
| C-23 | PASS | "INERTIA PATTERN DICTIONARY (PRIMARY ANALYTICAL FRAMEWORK)" leads the entire prompt; 7 enumerated labels in 4-column table with Description, Behavioral Signals, and Structural Tells |
| C-24 | PASS | PASS TOKEN encodes N sources, M paths, dominant pattern |
| C-25 | PASS | "Column order rule: Inertia Match precedes File Path Evidence in every TABLE B row. This is a schema constraint, not a display preference." Gate item 5 verifies |
| C-26 | PASS | Dictionary: invalidity statement verbatim |
| C-27 | PASS | "This schema governs every table in this skill. Status applies to every column." All 7 tables annotate Status for every column including TABLE A (Pattern Hypotheses) with Confidence Prior: optional |
| C-28 | PASS | "These two blocks name the same contract from both sides. Both must hold before Phase 3 begins." |
| C-29 | PASS | "Inverting the order is a schema violation." in TABLE B column order rule |
| C-30 | PASS | "This schema governs every table in this skill. Status applies to every column." as opening OUTPUT SCHEMA governing statement |
| C-31 | PASS | "PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION:" -- named phase boundary header |
| C-32 | PASS | "Evaluate each item in order; do not skip:" in gate checklist |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 24/24 → capped at 10
**Score: 100**

---

#### V-05 — Phrasing Register + Lifecycle Emphasis

| Criterion | Verdict | Evidence |
|---|---|---|
| C-01 | PASS | Step 1 in GROUP B: "List distinct work areas. Cite SCAN TABLE row for each. No evidence? Write: 'Area not evidenced -- insufficient scan signal.'" |
| C-02 | PASS | GROUP A scan steps: all 7 source types listed; "Cover at least 3 of 7" |
| C-03 | PASS | Step 4: S3 + "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences from S3 rows.]" |
| C-04 | PASS | Step 3: S2 with Concern Name, Boundaries Crossed, Boundary Note all REQUIRED |
| C-05 | PASS | Preamble: "Stated here. Restated in GROUP B. Non-negotiable." + GROUP B: "CRITICAL CONSTRAINT (restated): Raw analysis only." |
| C-06 | PASS | Step 2: S1 with Boundary Name, Inertia Match, File Path Evidence, Seam Rationale all REQUIRED |
| C-07 | PASS | Step 5: S4 with two rows, Current State / Recommended State, Dominant Inertia Pattern; "Separate current state from recommended state clearly. Label each." |
| C-08 | PASS | Step 6: S5 with Gap Type, Description, Resolution Condition; "Do not omit gaps to appear complete." |
| C-09 | PASS | SCAN TABLE: "File Path Evidence | REQUIRED | 5-path minimum is a gate condition"; gate item 2 enforces and halts |
| C-10 | PASS | Step 5: "Two rows: Current State, Recommended State." Group B exit condition 3: "Current State and Recommended State labeled and separated." |
| C-11 | PASS | GROUP A scan steps include path requirement; GROUP B: "Anti-fabrication rule: Cite SCAN TABLE row(s) for every claim. No unlabeled inference." |
| C-12 | PASS | "GROUP A / GROUP B BOUNDARY: GATE EVALUATION: Hard gate. GROUP B cannot begin until PASS TOKEN is written." |
| C-13 | PASS | Preamble: "Stated here. Restated in GROUP B." + GROUP B restates constraint |
| C-14 | PASS | Gate: 5-item numbered checklist; "Evaluate each item in order; do not skip:" |
| C-15 | PASS | "GROUP A -- SCAN" and "GROUP B -- SYNTHESIS" with explicit entry/exit conditions per group |
| C-16 | PASS | SCAN TABLE: "5-path minimum is a gate condition"; gate: "Item 2 fails: Write 'Path floor not met'. Stop." |
| C-17 | PASS | PASS TOKEN: named-token format with source count, path count, dominant pattern |
| C-18 | PASS | FAIL TOKEN: "Path floor not met" as named constant |
| C-19 | PASS | SCAN TABLE: "Inertia Match | REQUIRED | Dictionary label only; precedes File Path Evidence" |
| C-20 | PASS | "GATE TOKEN PROTOCOL / Define both tokens now. Use by name throughout." Both tokens defined |
| C-21 | PASS | "This schema governs every table in this skill. Status applies to every column." SCAN TABLE annotates all columns; synthesis tables S1-S5 mark REQUIRED for every column inline |
| C-22 | PASS | "Phase 1 postcondition: SCAN TABLE has 3+ sources, 5+ paths, valid dictionary labels, column order verified." + "Phase 2 precondition: Phase 1 postcondition is met. PASS TOKEN is written." |
| C-23 | PASS | INERTIA PATTERN DICTIONARY: 7 enumerated labels; "No free text." |
| C-24 | PASS | PASS TOKEN encodes N sources, M paths, dominant pattern |
| C-25 | PASS | "Column order mandatory: Inertia Match before File Path Evidence. Inverting the order is a schema violation." Gate item 5 verifies |
| C-26 | PASS | Dictionary: "Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable." |
| C-27 | PASS | "This schema governs every table in this skill. Status applies to every column." SCAN TABLE fully annotated; all synthesis tables have REQUIRED on every column |
| C-28 | PASS | "These two blocks name the same contract from both sides. Both must hold before GROUP B begins." |
| C-29 | PASS | "Inverting the order is a schema violation." in SCAN TABLE column order note; C-29 phrasing also appears in gate item 5 |
| C-30 | PASS | "This schema governs every table in this skill. Status applies to every column." as opening OUTPUT SCHEMA governing statement |
| C-31 | PASS | "GROUP A / GROUP B BOUNDARY: GATE EVALUATION:" -- named phase boundary header matching rubric example |
| C-32 | PASS | "Evaluate each item in order; do not skip:" in gate checklist |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 24/24 → capped at 10
**Score: 100**

---

### Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Total |
|---|---|---|---|---|
| V-01 Role Sequence | 60 | 30 | 10 | **100** |
| V-02 Output Format | 60 | 30 | 10 | **100** |
| V-03 Lifecycle Emphasis | 60 | 30 | 10 | **100** |
| V-04 Inertia Framing + Output Format | 60 | 30 | 10 | **100** |
| V-05 Phrasing Register + Lifecycle Emphasis | 60 | 30 | 10 | **100** |

All 5 variations score 100. The author's coverage summary confirms all 32 criteria were explicitly targeted in every variation, and all placement is verified.

---

### Ranking

With all variations at 100, ranking is by implementation quality of the new R8 criteria (C-29 through C-32) and overall structural robustness:

1. **V-03** — strongest C-32 implementation: adds a named gate entry condition ("Gate entry condition: The PHASE 1 COMPLETE statement has been written.") that makes sequential enforcement two-step — verify the completion statement was written, then evaluate checklist items. Phase exit conditions mirror gate conditions creating dual enforcement layer. "Affected Sections" optional column in Evidence Gaps table goes beyond the criterion.

2. **V-02** — strongest C-29 treatment: column order rule is two sentences ("This is a schema constraint, not a display preference. Inverting the order is a schema violation.") — violation label is reinforced by a preceding framing sentence. Schema-first design means C-30 governing statement appears before any instructions, making it structurally primary.

3. **V-04** — most analytically distinctive: inertia dictionary leads the prompt as "PRIMARY ANALYTICAL FRAMEWORK" with a 4-column table adding Behavioral Signals alongside Structural Tells; TABLE A captures pattern hypotheses before evidence collection; Hypothesis Held column tracks prediction confirmation; "prediction not resolved" gap type creates cross-phase accountability. Most coverage of structural innovation beyond the rubric.

4. **V-05** — tightest command register; C-29 phrasing appears twice (SCAN TABLE note and gate item 5 verification instruction); Group B exit conditions make "Current State and Recommended State labeled and separated" an exit-verifiable criterion, not just a synthesis instruction.

5. **V-01** — solid role-sequence baseline; SCANNER / GATEKEEPER boundary header satisfies C-31 but differs from the GROUP A / GROUP B label in the rubric example. No implementation distinguishes V-01 from prior rounds.

---

### Excellence Signals

Patterns from top variations that exceed criterion minimum and represent candidates for future formalization:

1. **Named gate entry condition** (V-03): Before evaluating gate checklist items, a named entry condition verifies that the phase completion statement was written. "Gate entry condition: The PHASE 1 COMPLETE statement has been written." This adds a pre-gate checkpoint — sequential evaluation enforcement on the gate itself, not just within the gate. Not captured in C-32 (which targets evaluation order within the checklist, not the precondition for starting the checklist).

2. **Behavioral signals column in inertia dictionary** (V-04): The dictionary table adds a "Behavioral Signals" column alongside "Structural Tells," giving agents two registers of observable evidence per pattern — code-observable tells and human-behavior-observable tells. This makes the dictionary actionable for organizational context where file structure alone may be ambiguous.

3. **Hypothesis confirmation tracking column** (V-04): "Hypothesis Held | optional | yes / no / partial -- references TABLE A prediction" links each scan evidence row back to the Phase 1 prediction, creating machine-verifiable confirmation/disconfirmation tracking. Combined with TABLE A (predictions) and TABLE G ("prediction not resolved" gap type), this forms a complete hypothesis-test-result loop across three phases.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named gate entry condition requires phase completion statement before checklist evaluation begins adding pre-gate checkpoint distinct from sequential item evaluation", "behavioral signals column in inertia dictionary adds human-observable tells alongside structural code tells making dictionary dual-register", "hypothesis confirmation tracking column links scan evidence rows to prior predictions with yes/no/partial vocabulary enabling machine-verifiable prediction outcome loop"]}
```
