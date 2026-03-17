Now I have all the structural detail I need. Let me write the scorecard.

---

## org-scan R11 Scorecard — 2026-03-16

### Summary

| Rank | Variation | Essential | Recommended | Aspirational | Score | Notes |
|------|-----------|-----------|-------------|--------------|-------|-------|
| 1 | V-01 Named boundaries (PHASE N/N+1) | 5/5 | 3/3 | 44/44 | **100** | All criteria structural invariants |
| 1 | V-02 Schema-first declaration | 5/5 | 3/3 | 44/44 | **100** | Strongest C-42 form |
| 1 | V-03 Analytical arc + role bindings | 5/5 | 3/3 | 44/44 | **100** | Strongest C-44 form |
| 1 | V-04 TABLE G architecture + actor boundaries | 5/5 | 3/3 | 44/44 | **100** | Strongest C-43 form |
| 1 | V-05 Full integration, tight register | 5/5 | 3/3 | 44/44 | **100** | All 4 new criteria in block structure |

R11 invariants eliminate all aspiration-level differentiation: C-41 through C-44 were embedded as structural invariants across all 5 variations, so there are no aspirational failures to discriminate on. All essential and recommended criteria are structurally enforced in every variation.

---

### V-01 — Named Boundaries (PHASE N / PHASE N+1)

**Axis**: C-41 — PHASE 1/2/3/4 BOUNDARY: header above both exit and entry blocks at all 3 transitions. Terminal SYNTHESIZER / END BOUNDARY added for completeness.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Areas named and traceable | PASS | SYNTHESIZER: "every area cites at least one TABLE B row. Anti-fabrication: no area without TABLE B row support" |
| C-02 | Multi-source scan 3+ of 7 | PASS | Gate checklist item 3: "3+ source types in TABLE B? -- no: Source floor not met -- halt." |
| C-03 | Headcount as range with rationale | PASS | SCANNER step 6: "estimate range, 2-3 sentences, cite TABLE B and TABLE D rows" |
| C-04 | Cross-cutting concerns with boundary note | PASS | TABLE D: Boundary Note column REQUIRED; SCANNER step 4: "explain why concern spans team lines" |
| C-05 | Raw analysis only — no org chart | PASS | CRITICAL CONSTRAINT preamble + "(Restated in SCHEMA DECLARATION below.)" |
| C-06 | Team boundary candidates with seam rationale | PASS | TABLE C: SCANNER step 3 requires seam rationale to name driving pattern |
| C-07 | Org shape named and justified | PASS | TABLE F: two rows, Current State references dominant pattern from PASS TOKEN |
| C-08 | Evidence gaps flagged explicitly | PASS | TABLE E: 4 gap types including prediction-not-resolved |
| C-09 | 5+ file paths as evidence | PASS | Gate: path floor is precondition blocking Phase 2/3 gate pass |
| C-10 | Current / recommended state separated | PASS | TABLE F: exactly two rows labeled Current State and Recommended State |
| C-11 | Anti-fabrication language per section | PASS | PREDICTOR, SCANNER, SYNTHESIZER roles each carry anti-fabrication clause |
| C-12 | Hard sequencing gate | PASS | Gate evaluation section between SCANNER and SYNTHESIZER; halt strings enforced |
| C-13 | Critical constraint stated twice | PASS | Preamble + "(Restated in SCHEMA DECLARATION below.)" with restatement |
| C-14 | Verification checklist with confirmation sentence | PASS | "Gate checklist -- evaluate each item in order; do not skip" + PASS TOKEN sentence |
| C-15 | Structural group labels | PASS | PHASE 1/2/3/4 numbered phase labels as discrete structural groups |
| C-16 | File path floor as gate condition | PASS | "Path floor: collect at least 5 distinct file paths. Floor is a gate precondition" |
| C-17 | Gate confirmation token named format | PASS | "Gate clear -- [N sources scanned], [M paths collected], dominant pattern: [pattern label]" |
| C-18 | Gate failure output named string | PASS | FAIL TOKEN + 4 additional halt strings all named |
| C-19 | Inertia Match column in scan output | PASS | TABLE B: Inertia Match column REQUIRED (dictionary-constrained) |
| C-20 | GATE TOKEN PROTOCOL block | PASS | "### GATE TOKEN PROTOCOL" block defines pass and fail tokens before any phase begins |
| C-21 | Required column enforcement | PASS | "Status: REQUIRED" annotations on every column header row across all tables |
| C-22 | Formal phase contract bidirectional | PASS | "SCANNER postcondition... GATEKEEPER precondition... These two blocks name the same contract from both sides." |
| C-23 | Inertia pattern dictionary enumerated | PASS | 7-pattern table with fixed labels; "Free text is structurally invalid" |
| C-24 | Self-documenting pass token | PASS | Token includes N sources, M paths, dominant pattern label |
| C-25 | Inertia Match column-order enforcement | PASS | "Column-order rule: Inertia Match precedes File Path Evidence. Inverting the order is a schema violation." |
| C-26 | Dictionary invalidity statement | PASS | "Free text is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable." |
| C-27 | Full-schema status annotation | PASS | "Status applies to every column across all tables" + per-column REQUIRED/optional values throughout |
| C-28 | Bilateral contract declaration sentence | PASS | "These two blocks name the same contract from both sides. Both must hold before SYNTHESIZER begins." |
| C-29 | Schema violation label | PASS | "Inverting the order is a schema violation." |
| C-30 | Universal schema governing statement | PASS | "This schema governs every table in this skill. Status applies to every column across all tables." |
| C-31 | Named phase boundary header at gate | PASS | "### PHASE 2 / PHASE 3 BOUNDARY: GATE EVALUATION" |
| C-32 | Sequential evaluation enforcement | PASS | "Gate checklist -- evaluate each item in order; do not skip:" |
| C-33 | Named gate entry condition | PASS | "SCANNER COMPLETE -- control transfers to GATEKEEPER" required before checklist begins |
| C-34 | Dual-register inertia dictionary | PASS | Dictionary table has both "Structural Tells" and "Behavioral Signals" columns |
| C-35 | Hypothesis confirmation tracking column | PASS | TABLE B: "Hypothesis Held" column (yes/no/partial); TABLE E: prediction-not-resolved type |
| C-36 | Gate entry as role control-transfer | PASS | "Gate entry failure is equivalent to a control-transfer failure between named roles -- the SCANNER has not handed off." |
| C-37 | Schema-first table definition | PASS | SCHEMA DECLARATION section defines TABLE A–G before any role instruction begins |
| C-38 | Phase lifecycle ceremony at every boundary | PASS | EXIT + ENTRY condition blocks at PHASE 1/2, 2/3, 3/4 boundaries |
| C-39 | Hypothesis-first phase architecture | PASS | PREDICTOR role produces TABLE A before any SCANNER work; SYNTHESIZER closes TABLE G |
| C-40 | Dictionary as PRIMARY ANALYTICAL FRAMEWORK | PASS | "### INERTIA PATTERN DICTIONARY -- PRIMARY ANALYTICAL FRAMEWORK" with posture declaration |
| C-41 | Named boundary at every phase transition | PASS | "### PHASE 1 / PHASE 2 BOUNDARY:" above EXIT (PREDICTOR) and ENTRY (SCANNER); same for all 3 transitions |
| C-42 | SCHEMA DECLARATION as named block | PASS | "### SCHEMA DECLARATION" section header wrapping TABLE A–G |
| C-43 | Dedicated prediction-resolution table | PASS | TABLE G: "Sole structural purpose: close every TABLE A prediction row-by-row...TABLE A -> TABLE B -> TABLE G" |
| C-44 | Dictionary declaration names full arc | PASS | "analytical spine through which all evidence is interpreted -- from prediction through verification through synthesis" |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 44/44

```
composite = (5/5 × 60) + (3/3 × 30) + (44/44 × 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100**

---

### V-02 — Schema Declaration as Named Block (Schema-First)

**Axis**: C-42 — SCHEMA DECLARATION appears as the FIRST named structural block, before framework declaration and before gate token definitions. Uses GROUP A/B/C/D boundary labels (canonical C-41 form). Tables annotated "Produced by: ROLE" under each header.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS (all) | Same structural enforcement as V-01; GROUP A/B labels structurally equivalent |
| C-09–C-40 | Aspirational C-09 through C-40 | PASS (all) | All enforcement mechanisms present; GROUP A/B is canonical form of C-15 |
| C-41 | Named boundary at every phase transition | PASS | "### GROUP A / GROUP B BOUNDARY:" above EXIT CONDITION (PREDICTOR) and ENTRY CONDITION (SCANNER); same format at GROUP B/C and GROUP C/D boundaries |
| C-42 | SCHEMA DECLARATION as named block | PASS — strongest form | SCHEMA DECLARATION is the FIRST named structural block in the skill, appearing before GATE TOKEN PROTOCOL and INERTIA PATTERN DICTIONARY; output contract established before analytical posture |
| C-43 | Dedicated prediction-resolution table | PASS | TABLE G: "Sole structural purpose: close every TABLE A prediction row-by-row... TABLE A -> TABLE B -> TABLE G" |
| C-44 | Dictionary declaration names full arc | PASS | "analytical spine through which all evidence is interpreted -- from prediction through verification through synthesis" |

**Note**: V-02 adds "Produced by: ROLE" annotations under each table header in the schema (e.g., "*Produced by: PREDICTOR before any scan evidence is collected.*"). This is not captured by any existing criterion — the schema becomes self-documenting about which role produces each table.

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 44/44

**Score: 100 / 100**

---

### V-03 — Analytical Arc with Role Assignments

**Axis**: C-44 — framework declaration explicitly assigns each phase to a named role: "PREDICTOR applies it in the prediction phase... SCANNER applies it in the verification phase... SYNTHESIZER applies it in the synthesis phase." Framework declaration appears FIRST (before schema), making the analytical posture the opening anchor.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS (all) | All structural enforcement mechanisms present |
| C-09–C-40 | Aspirational C-09 through C-40 | PASS (all) | Framework-first then schema ordering; PHASE 1/2/3/4 boundary labels |
| C-41 | Named boundary at every phase transition | PASS | "### PHASE 1 / PHASE 2 BOUNDARY:" above EXIT CONDITION and ENTRY CONDITION; same at PHASE 2/3 and PHASE 3/4 |
| C-42 | SCHEMA DECLARATION as named block | PASS | "### SCHEMA DECLARATION" section header present; appears after framework (second position, not first) |
| C-43 | Dedicated prediction-resolution table | PASS | TABLE G: "Sole structural purpose: close every TABLE A prediction row-by-row. Makes hypothesis resolution a first-class schema-level output artifact. Completes the three-table loop: TABLE A -> TABLE B -> TABLE G." |
| C-44 | Dictionary declaration names full arc | PASS — strongest form | "It is the analytical spine through which all evidence is interpreted -- from prediction through verification through synthesis... PREDICTOR applies it in the prediction phase to form hypotheses... SCANNER applies it in the verification phase to label each finding... SYNTHESIZER applies it in the synthesis phase to resolve predictions." Explicitly per-role, not just arc-level. |

**Note**: Role instructions in V-03 open with the phase label: "Phase: prediction", "Phase: verification", "Phase: synthesis." This links each role instruction to its phase in the framework arc — not captured by any criterion.

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 44/44

**Score: 100 / 100**

---

### V-04 — TABLE G Architecture + Actor Boundary Names

**Axes**: C-43 (richest TABLE G declaration) + C-41 (ROLE / ROLE boundary names). Uses PREDICTOR / SCANNER / GATEKEEPER / SYNTHESIZER boundary naming instead of PHASE N/N+1 or GROUP A/B.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS (all) | All structural enforcement present |
| C-09–C-40 | Aspirational C-09 through C-40 | PASS (all) | Role-named boundaries satisfy all sequencing and gate criteria |
| C-41 | Named boundary at every phase transition | PASS | "### PREDICTOR / SCANNER BOUNDARY:" above EXIT CONDITION and ENTRY CONDITION; "### SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION"; "### GATEKEEPER / SYNTHESIZER BOUNDARY:" — actor-named form |
| C-42 | SCHEMA DECLARATION as named block | PASS | "### SCHEMA DECLARATION" section header wrapping TABLE A–G |
| C-43 | Dedicated prediction-resolution table | PASS — strongest form | TABLE G has: "Purpose: Explicit closure... Sole structural purpose: make hypothesis resolution a first-class schema-level output artifact... No other content belongs here. SYNTHESIZER mandate: close the hypothesis loop opened by PREDICTOR and threaded through SCANNER." Plus expanded schema (Prior Assessment, Resolution Note columns). Plus "Completeness rule: every TABLE A Prediction ID must appear as a TABLE G row. A TABLE A prediction with no TABLE G row is a structural gap -- add TABLE E row, type: prediction-not-resolved." |
| C-44 | Dictionary declaration names full arc | PASS | "analytical spine through which all evidence is interpreted -- from prediction through verification through synthesis" |

**Note 1**: TABLE G includes a "Completeness rule" with explicit remediation path — not captured by C-43, which describes only the purpose declaration. A named compliance rule embedded in the schema makes TABLE G structural compliance enforceable.

**Note 2**: "SYNTHESIZER mandate" embedded in TABLE G — a role obligation declared in the schema definition, making TABLE G not just a structural output but a role contract.

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 44/44

**Score: 100 / 100**

---

### V-05 — Full Integration, Tight Register

**Axis**: All 4 criteria in BLOCK 1/2/3/4 preamble. C-44 in BLOCK 1, C-42 as BLOCK 2 label, C-43 in TABLE G, C-41 at every boundary. Location-addressable by block number. ROLE / ROLE boundary names (same as V-04).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-08 | Essential + Recommended | PASS (all) | Compressed instructions preserve all structural requirements |
| C-09–C-40 | Aspirational C-09 through C-40 | PASS (all) | Block structure makes criteria location-addressable; all enforcement present |
| C-41 | Named boundary at every phase transition | PASS | "### PREDICTOR / SCANNER BOUNDARY:" above both EXIT and ENTRY; same at SCANNER/GATEKEEPER and GATEKEEPER/SYNTHESIZER boundaries |
| C-42 | SCHEMA DECLARATION as named block | PASS | "### BLOCK 2 -- SCHEMA DECLARATION" — block number + SCHEMA DECLARATION label makes it doubly addressable |
| C-43 | Dedicated prediction-resolution table | PASS | TABLE G: "Sole structural purpose: close every TABLE A prediction row-by-row. Makes hypothesis resolution a first-class schema-level output artifact. Completes the loop: TABLE A -> TABLE B -> TABLE G." |
| C-44 | Dictionary declaration names full arc | PASS — strong form | "It is the analytical spine through which all evidence is interpreted -- from prediction through verification through synthesis. PREDICTOR applies it in prediction; SCANNER applies it in verification; SYNTHESIZER applies it in synthesis." Role-phase binding present (same level as V-03). |

**Note**: The BLOCK 1/2/3/4 structure assigns a number to each pre-instruction declaration block. "Restated in BLOCK 2" in the constraint line makes the restatement location-addressable by block number, not just by section name.

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 44/44

**Score: 100 / 100**

---

## Score Summary

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-01 | **100** |
| 1 | V-02 | **100** |
| 1 | V-03 | **100** |
| 1 | V-04 | **100** |
| 1 | V-05 | **100** |

**All variations achieve 100/100.** R11's design — C-41 through C-44 embedded as structural invariants across all 5 — produces a flat score ceiling. The round confirms these four criteria are reliable and robustly implementable across different form axes. No variation breaks any prior criterion.

---

## Excellence Signals

Four new patterns emerge from axis-specific implementations that aren't captured by C-41 through C-44:

**Signal 1 — Schema-first ordering as output-contract anchor (V-02)**: SCHEMA DECLARATION placed before the PRIMARY ANALYTICAL FRAMEWORK declaration makes the output contract the structural anchor that precedes analytical posture. C-42 requires only the named block; C-42's strongest form requires the block to appear first so agents see what they must produce before learning how to think about it. Candidate for C-45.

**Signal 2 — Role-phase binding in framework declaration (V-03, V-05)**: The framework declaration explicitly assigns each phase to a named role ("PREDICTOR applies it in prediction; SCANNER in verification; SYNTHESIZER in synthesis"), transforming the analytical arc from a posture description into a per-role execution contract. C-44 requires only the three-phase arc string; the role-bound form makes the dictionary an instruction to each role by name. Candidate for C-45 or C-46.

**Signal 3 — TABLE G completeness rule with remediation path (V-04)**: After TABLE G's column definitions, a named "Completeness rule" states both the coverage requirement (every TABLE A Prediction ID) and the exact remediation path (add TABLE E row, type: prediction-not-resolved). C-43 describes the table's purpose declaration; the completeness rule makes structural compliance and non-compliance both machine-verifiable from the schema alone without reading instructions. Candidate for C-46 or C-47.

**Signal 4 — Actor-named boundary headers (V-04, V-05)**: Using ROLE / ROLE BOUNDARY format (PREDICTOR / SCANNER BOUNDARY) names the transition actors in the header itself, making each phase boundary identify who transfers control rather than where in the phase sequence it falls. C-41 requires the named boundary header above both exit and entry blocks; the actor-named form adds semantic content (the actors) to the structural content (the named section). Candidate for C-47 or C-48.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["schema-first ordering: SCHEMA DECLARATION placed before PRIMARY ANALYTICAL FRAMEWORK declaration makes output contract the structural anchor established before analytical posture — strongest form of C-42 not yet a criterion", "role-phase binding in framework declaration: explicitly assigns each dictionary phase to a named role (PREDICTOR in prediction, SCANNER in verification, SYNTHESIZER in synthesis), transforming the analytical arc from a posture description to a per-role execution contract — extends C-44 beyond phase-arc naming", "TABLE G completeness rule with remediation path: a named Completeness rule after column definitions states required coverage (every TABLE A Prediction ID) AND exact remediation step (TABLE E, type: prediction-not-resolved), making TABLE G structural compliance machine-verifiable from schema alone", "actor-named boundary headers: ROLE / ROLE BOUNDARY format (PREDICTOR / SCANNER BOUNDARY) names transition actors in the header, adding semantic actor-transfer content to structural phase-position labeling — extends C-41 from phase-position labeling to role-transfer actor identification"]}
```
