## org-scan R9 Scoring — V-01 through V-05

---

### Criterion-by-Criterion Evaluation

#### Essential Criteria (C-01 – C-05)

All five variations satisfy all five essential criteria. Common evidence:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-01** areas traceable to scan | PASS — SYNTHESIZER step 1 requires SCAN TABLE row citation per area; "No area without a SCAN TABLE citation" | PASS — "Cite TABLE A row(s) for each area" | PASS — "No area without a citation" | PASS — "No area without evidence" | PASS — "No evidence? Write: 'Area not evidenced'" |
| **C-02** 3+ source types | PASS — 7 source types listed; "cover at least 3" | PASS | PASS | PASS | PASS |
| **C-03** headcount range + rationale | PASS — "Estimated headcount: [X]-[Y] engineers. Rationale: [2-3 sentences...]" | PASS | PASS | PASS | PASS |
| **C-04** cross-cutting concerns + boundary note | PASS — CONCERNS TABLE, "Boundary Note must explain why each concern cannot be assigned to one team" | PASS | PASS | PASS — TABLE D CONCERNS TABLE | PASS — S2 with Boundary Note |
| **C-05** raw analysis only, stated twice | PASS — preamble ("stated here; restated in output schema") + output schema + SYNTHESIZER entry = 3× | PASS — 3× | PASS — preamble + schema + Phase 2 entry | PASS — preamble + schema + Phase 3 entry | PASS — preamble ("Non-negotiable") + schema + GROUP B entry |

**Essential score: 60/60 for all variations.**

---

#### Recommended Criteria (C-06 – C-08)

All five variations satisfy all three recommended criteria.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-06** boundary candidates + seam rationale | PASS — BOUNDARY TABLE, "Seam Rationale must state why this is a natural split, not just where a directory boundary exists" | PASS | PASS | PASS — TABLE C | PASS — S1 |
| **C-07** org shape named + justified | PASS — ORG SHAPE TABLE, Current/Recommended rows, "Reference the dominant inertia pattern from the PASS TOKEN" | PASS | PASS | PASS — TABLE F | PASS — S4 |
| **C-08** gaps and ambiguities flagged | PASS — "Do not omit gaps to appear complete" | PASS | PASS | PASS — TABLE G | PASS — "Do not omit gaps to appear complete" |

**Recommended score: 30/30 for all variations.**

---

#### Aspirational Criteria (C-09 – C-35)

All 27 criteria evaluated across all variations:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| **C-09** 5+ file paths | PASS — REQUIRED column; "collect at least 5 distinct file paths" | PASS — "5-path floor is a gate precondition" in TABLE A schema | PASS — "5-path floor is Phase 1 exit condition" | PASS | PASS — "5-path minimum is a gate condition" |
| **C-10** current vs recommended state separated | PASS — "Produce exactly two rows. Separate current state from recommended state clearly -- label each." | PASS | PASS | PASS | PASS — "Two rows: Current State, Recommended State. Label each." |
| **C-11** anti-fabrication language per section | PASS — SCANNER and SYNTHESIZER each have anti-fabrication rule blocks | PASS | PASS — Phase 1 and Phase 2 both have anti-fabrication rules | PASS — Phase 2 and Phase 3 | PASS — scan and synthesis |
| **C-12** hard sequencing gate | PASS — "Do not evaluate the gate checklist until the SCANNER COMPLETE declaration appears" | PASS — "This boundary is a hard sequencing gate. GROUP B cannot begin until the gate is complete" | PASS | PASS — "Phase 3 cannot begin until gate evaluation is complete" | PASS — "Hard gate. GROUP B cannot begin until PASS TOKEN is written." |
| **C-13** C-05 stated twice (preamble + output format) | PASS — preamble + output schema (both explicit) | PASS | PASS | PASS | PASS |
| **C-14** numbered checklist + confirmation sentence | PASS — 5-item numbered checklist; "If all items pass: Write the PASS TOKEN." | PASS | PASS | PASS | PASS |
| **C-15** structural group labels for phase separation | PASS — "ROLE: SCANNER", "ROLE: GATEKEEPER", "ROLE: SYNTHESIZER" as discrete structural labels | PASS — "GROUP A -- SCAN PHASE", "GROUP B -- SYNTHESIS PHASE" | PASS — "PHASE 1: EVIDENCE COLLECTION", "PHASE 2: SYNTHESIS" | PASS — "PHASE 1: PATTERN HYPOTHESIS", "PHASE 2: EVIDENCE COLLECTION", "PHASE 3: SYNTHESIS" | PASS — "GROUP A -- SCAN", "GROUP B -- SYNTHESIS" |
| **C-16** file path floor as gate condition | PASS — gate item 2: "If this item fails: Write 'Path floor not met'. Halt. Do not begin SYNTHESIZER work." | PASS — "Do not produce GROUP B output" | PASS — "Do not begin Phase 2" | PASS — "Do not begin Phase 3" | PASS — "Item 2 fails: Write 'Path floor not met'. Stop." |
| **C-17** gate confirmation token | PASS — "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]" | PASS | PASS | PASS | PASS |
| **C-18** gate failure output | PASS — FAIL TOKEN: "Path floor not met" | PASS | PASS | PASS | PASS |
| **C-19** Inertia Match column per row | PASS — REQUIRED column; "Dictionary label only; precedes File Path Evidence; free text is a schema violation" | PASS | PASS | PASS — TABLE B | PASS |
| **C-20** GATE TOKEN PROTOCOL block before Phase 1 | PASS — named block before SCANNER begins, both tokens defined as named constants | PASS | PASS | PASS | PASS |
| **C-21** evidence columns declared REQUIRED | PASS — both Inertia Match and File Path Evidence are STATUS: REQUIRED in schema | PASS | PASS | PASS | PASS |
| **C-22** formal bilateral phase contract | PASS — "Phase 1 postcondition (GATEKEEPER confirms)... Phase 2 precondition (SYNTHESIZER entry requires)... These two blocks name the same contract from both sides. Both must hold." | PASS | PASS | PASS — Phase 2 postcondition ↔ Phase 3 precondition | PASS |
| **C-23** inertia pattern dictionary with enumerated labels | PASS — 7-label dictionary; "All Inertia Match values in the SCAN TABLE must use these labels exactly." | PASS | PASS | PASS — "INERTIA PATTERN DICTIONARY (PRIMARY ANALYTICAL FRAMEWORK)" | PASS |
| **C-24** self-documenting pass token | PASS — "[N sources scanned], [M paths collected], dominant pattern: [pattern label]" — source count + path floor status + pattern name | PASS | PASS | PASS | PASS |
| **C-25** Inertia Match before File Path Evidence | PASS — "Column order rule: Inertia Match precedes File Path Evidence in every SCAN TABLE row. This is a structural schema constraint, not a display preference." | PASS — "must precede File Path Evidence" in schema + gate item 5 | PASS | PASS | PASS — "Column order mandatory" |
| **C-26** dictionary invalidity statement | PASS — "Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable." | PASS | PASS | PASS | PASS |
| **C-27** full-schema Status annotation on every column | PASS — "This schema governs every table in this skill. Status applies to every column." + every table has Status column including optional entries | PASS | PASS | PASS | PASS |
| **C-28** bilateral contract declaration sentence | PASS — "These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins." | PASS | PASS | PASS | PASS |
| **C-29** schema violation label | PASS — "Inverting the order is a schema violation." | PASS | PASS | PASS | PASS |
| **C-30** universal schema governing statement | PASS — "This schema governs every table in this skill. Status applies to every column." | PASS — schema defined first, governs all phases | PASS | PASS | PASS |
| **C-31** named phase boundary header | PASS — "SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION:" | PASS — "GROUP A / GROUP B BOUNDARY: GATE EVALUATION:" | PASS — "PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:" | PASS — "PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION:" | PASS — "GROUP A / GROUP B BOUNDARY: GATE EVALUATION:" |
| **C-32** sequential evaluation enforcement | PASS — "Evaluate each item in order; do not skip:" | PASS | PASS | PASS | PASS |
| **C-33** named gate entry condition | PASS — "Gate entry condition: The SCANNER COMPLETE declaration has been written above. Do not evaluate the gate checklist until the SCANNER COMPLETE declaration appears." SCANNER COMPLETE is written as the role handoff transfer action | PASS — "Gate entry condition: The SCAN COMPLETE token has been written. Do not evaluate the checklist until the SCAN COMPLETE token appears above." | PASS — "Gate entry condition: The PHASE 1 COMPLETE statement has been written above. Do not evaluate the gate checklist until that statement appears." | PASS — "Gate entry condition: The EVIDENCE COLLECTION COMPLETE statement has been written above. Do not evaluate the gate checklist until that statement appears." | PASS — "Write SCAN COMPLETE before evaluating the gate checklist:" + "Gate entry condition: SCAN COMPLETE token written above. Do not evaluate until it appears." |
| **C-34** dual-register inertia dictionary (Behavioral Signals column) | PASS — 5-column dictionary with Behavioral Signals column; richest per-pattern behavioral tells | PASS — 5-column dictionary | PASS — 5-column dictionary | PASS — "PRIMARY ANALYTICAL FRAMEWORK"; richest treatment with most detailed behavioral signal rows | PASS — 4-column compact dictionary (Description merged; Structural Tells + Behavioral Signals both present) |
| **C-35** Hypothesis Held column + prediction not resolved gap | PASS — SCAN TABLE has "Hypothesis Held \| optional \| yes / no / partial -- links this row to the SCANNER COMPLETE dominant pattern prediction"; GAPS TABLE includes "prediction not resolved" gap type | PASS — TABLE A has Hypothesis Held; TABLE F has "prediction not resolved" | PASS — SCAN TABLE Hypothesis Held; GAPS TABLE "prediction not resolved" | PASS — TABLE B Hypothesis Held "references TABLE A pattern assessment for the matched label"; TABLE G "prediction not resolved" triggered by both partial Hypothesis Held AND Likely-rated patterns not confirmed/disconfirmed — most complete implementation | PASS — Hypothesis Held "vocabulary constrained; no other values accepted"; S5 includes "prediction not resolved" |

**Aspirational raw: 27 × 2 = 54 pts for all variations → capped at 10.**

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (cap 10) | Total |
|---|---|---|---|---|
| **V-01** | 60 | 30 | 10 | **100** |
| **V-02** | 60 | 30 | 10 | **100** |
| **V-03** | 60 | 30 | 10 | **100** |
| **V-04** | 60 | 30 | 10 | **100** |
| **V-05** | 60 | 30 | 10 | **100** |

---

### Ranking

All five variations score 100 — a perfect-coverage round. Structural differentiation within the top tier:

1. **V-04** — analytically deepest: three-phase hypothesis-first loop (TABLE A predictions → TABLE B evidence → TABLE G closure) makes C-35 structurally inevitable rather than a bolt-on column. Most complete C-35 implementation: "prediction not resolved" triggered by both partial Hypothesis Held AND unresolved Likely-rated patterns. Dictionary framed as PRIMARY ANALYTICAL FRAMEWORK changes agent posture from classify-after-scan to hypothesize-then-verify.
2. **V-01** — strongest behavioral binding for C-33: SCANNER COMPLETE is a *role control-transfer declaration*, not a checklist precondition — makes gate entry failure the same as failing to transfer control between named roles, the strongest possible enforcement framing.
3. **V-02** — schema-first structural clarity: TABLE A through TABLE F defined before any instructions, making every instruction traceable to a letter reference.
4. **V-03** — maximum lifecycle ceremony: explicit named entry conditions, exit conditions, and phase-completion statements at every boundary.
5. **V-05** — maximum concision: tightest imperative register; non-compliance is visibly wrong without requiring prose interpretation.

---

### Excellence Signals

Three new patterns emerged from R9 that made top-scoring variations structurally stronger:

**1. Role-as-control-transfer for gate entry (V-01)** — Framing C-33's named gate entry condition as a *role handoff declaration* (SCANNER COMPLETE transfers control to GATEKEEPER) gives the pre-gate statement behavioral weight beyond a checklist precondition. An agent that has been told it occupies exactly one role at a time and can only transition via a named declaration has a stronger behavioral incentive to write the completion statement than one merely told "write this before evaluating."

**2. Hypothesis-first posture making Hypothesis Held structurally necessary (V-04)** — Adding a Phase 1 PATTERN HYPOTHESIS table (prior assessments before any scanning) changes Hypothesis Held from a tracking column bolted onto the scan to the natural resolution column of a prediction the agent already made. The three-table chain (TABLE A prediction → TABLE B Hypothesis Held → TABLE G prediction not resolved) forms a closed loop that is machine-verifiable without prose inspection.

**3. Dictionary-as-PRIMARY-ANALYTICAL-FRAMEWORK framing (V-04)** — Labeling the inertia dictionary "PRIMARY ANALYTICAL FRAMEWORK" and stating it is "the analytical spine of this skill" before any instructions shifts the agent's default posture from "scan then label findings" to "hypothesize from dictionary then verify against evidence." This framing makes C-34 behavioral signals usable at hypothesis formation time, not just at classification time.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["role-as-control-transfer: framing the named gate entry condition as a role handoff declaration (not a checklist precondition) gives the pre-gate completion statement behavioral enforcement weight proportional to transferring control between named roles", "hypothesis-first posture: adding a Phase 1 prediction table before scanning makes Hypothesis Held structurally necessary as the resolution column of a prior prediction, forming a closed machine-verifiable loop from TABLE A prediction through scan evidence to gap table closure", "dictionary-as-primary-analytical-framework: naming the inertia dictionary the analytical spine before any instructions shifts agent posture from classify-after-scan to hypothesize-then-verify, making behavioral signals usable at prediction formation time rather than only at post-scan labeling"]}
```
