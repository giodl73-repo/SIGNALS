# org-scan Skill Scoring — Round 13 (Rubric v13)

## Scoring Framework

| Band | Criteria | Points Each | Max |
|---|---|---|---|
| Essential | C-01 to C-05 | 12 pts | 60 |
| Recommended | C-06 to C-08 | 10 pts | 30 |
| Aspirational | C-09 to C-49 (41 criteria) | 2 pts | 10 (capped) |
| **Total** | | | **100** |

Aspirational cap: 10 pts regardless of how many of the 41 criteria pass.

---

## V-01 — Baseline R13

**Axis**: Control condition — all C-46/47/48/49 invariants fully written, no new axis applied.

### Essential (60 pts)

| Criterion | Result | Evidence |
|---|---|---|
| C-01 Areas named and traceable | PASS | TABLE B Area column, scan sourced from 7-type list |
| C-02 Multi-source scan 3+ of 7 | PASS | "Scan at least 3 of 7 source types" explicit; 7 types enumerated |
| C-03 Headcount range with rationale | PASS | TABLE C FTE Range REQUIRED (range, not point value); Headcount Range section with TABLE C rationale |
| C-04 Cross-cutting concerns with boundary note | PASS | TABLE D with Boundary Note REQUIRED column |
| C-05 Raw analysis only | PASS | Critical constraint stated in preamble AND restated in Phase 3 entry |

**Essential score: 60/60**

### Recommended (30 pts)

| Criterion | Result | Evidence |
|---|---|---|
| C-06 Team boundary candidates with seam rationale | PASS | TABLE E Seam Rationale REQUIRED (cite TABLE B row) |
| C-07 Org shape named and justified | PASS | Org Shape section: dominant pattern from PASS TOKEN, CURRENT STATE / RECOMMENDED STATE separated, justified from TABLE B |
| C-08 Evidence gaps flagged explicitly | PASS | TABLE F with Gap/Implication/Source Types Checked; absence of source types explicitly noted |

**Recommended score: 30/30**

### Aspirational (C-09 to C-49) — cap 10 pts

| Criterion | Result | Evidence |
|---|---|---|
| C-09 5+ file paths cited | PASS | TABLE B File Path Evidence REQUIRED; gate condition enforces 5+ paths |
| C-10 Current vs recommended state separated | PASS | Org Shape: "Separate CURRENT STATE... from RECOMMENDED STATE" |
| C-11 Anti-fabrication language | PASS | Phase 1: "TABLE A is prediction only"; Phase 2: "Report only findings from files actually read" |
| C-12 Hard sequencing gate | PASS | Gate between SCANNER/GATEKEEPER blocks Phase 3 until PASS token |
| C-13 Constraint stated twice | PASS | Preamble + "CONSTRAINT RESTATEMENT" in Phase 3 |
| C-14 Verification checklist with confirmation | PASS | 5-item numbered checklist; "Write PASS or FAIL token. No prose substitution." |
| C-15 Structural group labels | PASS | GROUP A / GROUP B / GROUP C clearly labeled |
| C-16 File path floor as gate condition | PASS | "This requirement blocks gate passage" explicitly stated |
| C-17 Gate confirmation token named-format | PASS | "Gate clear -- [N] sources scanned, [N] paths cited, dominant pattern: [PATTERN-ID]" |
| C-18 Gate failure output named string | PASS | "Path floor not met -- [N] paths found, 5 required"; halt instruction included |
| C-19 Inertia Match column | PASS | TABLE B Inertia Match REQUIRED (dictionary value only) |
| C-20 Bidirectional gate token protocol block | PASS | GATE TOKEN PROTOCOL block defines both tokens before Phase 1; "self-contained" |
| C-21 Required table column enforcement | PASS | All columns annotated REQUIRED in schema |
| C-22 Formal bilateral phase contract | PASS | "postcondition of Phase 2 and the precondition of Phase 3. Both sides name the same contract. Both must hold." |
| C-23 Inertia pattern dictionary | PASS | I-01 through I-07 named values; dictionary embedded before phases |
| C-24 Self-documenting pass token | PASS | Token includes source count, path count, dominant pattern ID |
| C-25 Inertia Match column-order enforcement | PASS | "Column order fixed: Inertia Match before File Path Evidence. Inverting the order is a schema violation." |
| C-26 Dictionary invalidity statement | PASS | "Free text in the Inertia Match column is structurally invalid -- unconstrained values make pattern comparison across runs unverifiable." |
| C-27 Full-schema status annotation | PASS | "This schema governs every table in this skill. Status applies to every column." — every column has Status |
| C-28 Bilateral contract declaration sentence | PASS | "This bilateral contract declaration: the postcondition block above and the precondition block below name the same contract from both sides." |
| C-29 Schema violation label | PASS | "Inverting the order is a schema violation." |
| C-30 Universal schema governing statement | PASS | "This schema governs every table in this skill. Status applies to every column." |
| C-31 Named phase boundary header | PASS | "SCANNER / GATEKEEPER BOUNDARY: GATE EVALUATION:" as named header |
| C-32 Sequential evaluation enforcement | PASS | "evaluate each item in order; do not skip" |
| C-33 Named gate entry condition | PASS | "Named gate entry condition: SCANNER COMPLETE declaration must appear above." |
| C-34 Dual-register inertia dictionary | PASS | Dictionary table has Structural Code Signals + Behavioral Signals columns |
| C-35 Hypothesis confirmation tracking column | PASS | TABLE B Hypothesis Held (yes/no/partial); TABLE F includes unresolved prediction gap type |
| C-36 Gate entry as role control-transfer declaration | PASS | "SCANNER COMPLETE -- control transfers to GATEKEEPER" |
| C-37 Schema-first table definition | PASS | SCHEMA DECLARATION before any phase instructions; TABLE A through G defined |
| C-38 Phase lifecycle ceremony at every boundary | PASS | Every boundary: exit condition (PREDICTOR COMPLETE / SCANNER COMPLETE / SYNTHESIZER COMPLETE) + entry condition (PREDICTOR COMPLETE present / PASS TOKEN present) |
| C-39 Hypothesis-first phase architecture | PASS | Phase 1 dedicated to prediction before any file reading; Phase 3 resolves predictions against evidence |
| C-40 Dictionary as primary analytical framework | PASS | "This dictionary is the PRIMARY ANALYTICAL FRAMEWORK for this skill." |
| C-41 Named boundary section at every phase transition | PASS | PREDICTOR/SCANNER BOUNDARY, SCANNER/GATEKEEPER BOUNDARY, GATEKEEPER/SYNTHESIZER BOUNDARY, SYNTHESIZER/END BOUNDARY — all four named |
| C-42 Schema declaration as named structural block | PASS | "SCHEMA DECLARATION" named block header before phase instructions |
| C-43 Dedicated prediction-resolution table (TABLE G) | PASS | TABLE G -- Prediction Resolution is a dedicated named table |
| C-44 Dictionary declaration names full analytical arc | PASS | "operates from prediction through verification through synthesis" |
| C-45 Table role attribution | PASS | Every table: "Produced by: [ROLE]..." annotation |
| C-46 Role-phase binding in PAF declaration | PASS | "PREDICTOR applies it in Phase 1 ... SCANNER applies it in Phase 2 ... SYNTHESIZER applies it in Phase 3" |
| C-47 TABLE G completeness rule with named remediation path | PASS | Completeness rule present; named remediation: TABLE G unresolved row + TABLE F gap entry with exact column values |
| C-48 Actor-named boundary headers | PASS | PREDICTOR/SCANNER BOUNDARY, SCANNER/GATEKEEPER BOUNDARY, GATEKEEPER/SYNTHESIZER BOUNDARY, SYNTHESIZER/END BOUNDARY |
| C-49 Three-layer role-contract completeness | PASS | C-45 + C-46 + C-48 all present; emergent property structurally established |

All 41 aspirational criteria: PASS → capped at **10/10**

**V-01 Total: 100/100**

---

## V-02 — ROLE SCOPE DECLARATION

**Axis**: Phrasing register — formal ROLE SCOPE DECLARATION block at each phase start.

All C-01 through C-49 carry over from V-01. The ROLE SCOPE DECLARATION blocks add:
- PREDICTOR: Authority (PAF Phase 1 binding citation), Permitted outputs (TABLE A only), Prohibited outputs (file reads / scan tables / gate token / org chart), Constraint check
- SCANNER: Authority (PAF Phase 2 binding citation), Permitted outputs (TABLE B/C/D), Prohibited outputs (PREDICTOR domain / GATEKEEPER domain / synthesis), Constraint check
- SYNTHESIZER: Authority (PAF Phase 3 binding citation), Permitted outputs (TABLE E/F/G / Org Shape / Headcount Range), Prohibited outputs (new scan evidence / new hypotheses / org chart), Constraint check

The boundary note in PREDICTOR/SCANNER BOUNDARY explicitly references: "ROLE SCOPE DECLARATION for SCANNER follows immediately below at Phase 2 start." Same for GATEKEEPER/SYNTHESIZER BOUNDARY → SYNTHESIZER scope declaration.

| Criterion | Result | Evidence |
|---|---|---|
| C-01 through C-49 | PASS (all) | Same as V-01 — all invariants preserved |

**V-02 Total: 100/100**

**Excellence signal**: ROLE SCOPE DECLARATION creates a fourth structural verification layer. Each role's compliance is independently auditable from three independent locations: PAF block (framework level), schema attribution (table level), and the role's own scope declaration (phase level). The Prohibited outputs list makes constraint violations role-specific: "Constraint check: no org chart production occurs in Phase X" appears three times, once per role, instead of only at two global declaration points (preamble + Phase 3 restatement). This is not captured by any of C-09 through C-49.

---

## V-03 — PHASE COMPLETION PROOF

**Axis**: Lifecycle emphasis — PHASE COMPLETION PROOF block after each phase exit.

All C-01 through C-49 carry over from V-01. The PHASE COMPLETION PROOF blocks add:

- **PREDICTOR proof**: PAF binding honored (cite PAF sentence + TABLE A row count), TABLE attribution honored (cite schema declaration), Constraint maintained (no file reads / org chart), STATUS: [CONFIRMED / FAIL]
- **SCANNER proof**: PAF binding honored (all TABLE B Inertia Match = I-0x), TABLE attribution honored (TABLE B/C/D exist per schema), Constraint maintained (no hypothesis / synthesis / org chart), STATUS
- **SYNTHESIZER proof**: PAF binding honored (TABLE G Evidence Summary cites TABLE B rows), TABLE attribution honored (TABLE E/F/G per schema), TABLE G completeness count (TABLE A rows = TABLE G rows), Constraint maintained, STATUS

Gate checklist gains new item: "PHASE COMPLETION PROOF for SCANNER shows STATUS: CONFIRMED" — the proof is now a hard gate prerequisite, not just an execution record.

| Criterion | Result | Evidence |
|---|---|---|
| C-01 through C-49 | PASS (all) | All invariants preserved; gate checklist expands but core criteria all satisfied |
| C-33 in particular | PASS (stronger) | "SCANNER COMPLETE declaration and PHASE COMPLETION PROOF for SCANNER must both appear above" — gate entry condition is now a compound requirement |

**V-03 Total: 100/100**

**Excellence signal (1)**: PHASE COMPLETION PROOF closes the temporal verification gap in C-49. C-49 establishes a pre-declared structural completeness property (three layers at definition time); the proof block makes it verifiable at execution time — each phase produces a verifiable STATUS record confirming PAF binding was honored, tables were produced per schema, and constraint was maintained. This is a third temporal verification point: PAF declaration (before phase), PHASE COMPLETION PROOF (after phase), gate token (between phases).

**Excellence signal (2)**: The gate checklist now includes proof confirmation as a checklist item (item 2: "PHASE COMPLETION PROOF for SCANNER shows STATUS: CONFIRMED"), making the proof's STATUS a machine-verifiable gate prerequisite, not just a non-binding self-report.

---

## V-04 — GATEKEEPER as Named Fourth Role

**Axis**: Role sequence — GATEKEEPER explicitly named as a fourth role (Phase 2.5) with ROLE SCOPE DECLARATION.

Structural changes from V-01:
- PAF block extended: "GATEKEEPER applies it in Phase 2.5 to verify that all Inertia Match values are valid dictionary IDs before permitting synthesis to begin — the GATEKEEPER is the enforcement point for dictionary compliance between scan and synthesis."
- GATE TOKEN PROTOCOL updated: "One of these strings must appear as the **sole output of the GATEKEEPER role**. No prose substitution. The GATEKEEPER role produces this token and nothing else."
- GROUP B.5 -- GATEKEEPER PHASE introduced with:
  - ROLE SCOPE DECLARATION: GATEKEEPER (Authority: PAF Phase 2.5 binding, Permitted: PASS or FAIL token only, Prohibited: scan evidence / hypothesis / synthesis / table production / org chart, Constraint check: any output beyond the token is a GATEKEEPER scope violation)
  - Phase 2.5 exit: "GATEKEEPER COMPLETE -- token written -- control transfers to SYNTHESIZER."
- SCANNER exit updated: "SCANNER COMPLETE -- control transfers to GATEKEEPER."
- SCANNER ROLE SCOPE DECLARATION Prohibited list: "gate token production (GATEKEEPER domain)"

| Criterion | Result | Evidence |
|---|---|---|
| C-01 through C-49 | PASS (all) | All invariants preserved; GATEKEEPER presence extends but does not break any existing criterion |
| C-46 | PASS (extended) | PAF now names four roles: PREDICTOR (Phase 1), SCANNER (Phase 2), GATEKEEPER (Phase 2.5), SYNTHESIZER (Phase 3) |
| C-36 | PASS (strengthened) | "SCANNER COMPLETE -- control transfers to GATEKEEPER" — control-transfer now names GATEKEEPER as the specific receiving role |

**V-04 Total: 100/100**

**Excellence signal**: GATEKEEPER as a named role with Phase 2.5 PAF binding and "sole output" constraint transforms gate failure from a boundary condition into a named role output. A gate violation (GATEKEEPER producing anything beyond the token) is now structurally identifiable as a GATEKEEPER scope violation, not merely a missing structural element. The "sole output" language in the GATE TOKEN PROTOCOL and ROLE SCOPE DECLARATION's "Constraint check: GATEKEEPER produces a single token. Any output beyond the token is a GATEKEEPER scope violation." creates the strongest possible enforcement framing: the violation type is named before it can occur.

---

## V-05 — Full Combination

**Axis**: All three axes (V-02 ROLE SCOPE DECLARATION + V-03 PHASE COMPLETION PROOF + V-04 GATEKEEPER) + TABLE G cross-phase attribution columns.

Structural changes unique to V-05 beyond combining the three axes:

**TABLE G schema expanded** to "Prediction Resolution and Cross-Phase Audit":
```
Produced by: SYNTHESIZER after gate passage. Serves as cross-phase role completion record.

| Column                              | Status     |
| Pattern ID                          | REQUIRED   |
| Pattern Name                        | REQUIRED   |
| Structural Prediction (from TABLE A)| REQUIRED   |
| Behavioral Prediction (from TABLE A)| REQUIRED   |
| Predicted by                        | REQUIRED (always: PREDICTOR -- Phase 1) |
| Evidence Summary                    | REQUIRED (cite TABLE B row) |
| Evidence rows cited                 | REQUIRED (TABLE B row identifiers, comma-separated) |
| Scanned by                          | REQUIRED (always: SCANNER -- Phase 2) |
| Resolution                          | REQUIRED (confirmed / refuted / partial) |
| Resolved by                         | REQUIRED (always: SYNTHESIZER -- Phase 3) |
```

**TABLE G cross-phase attribution** statement embedded in schema: "The 'Predicted by', 'Scanned by', and 'Resolved by' columns make TABLE G a three-role, three-phase completion audit record. Every row traces from the role that originated the prediction, through the role that collected the evidence, to the role that produced the resolution. No inference required -- the attribution is explicit in every row."

**TABLE G completeness rule remediation path** extended to populate all attribution columns in unresolved rows: "Predicted by = 'PREDICTOR -- Phase 1', Scanned by = 'SCANNER -- Phase 2 (no matching evidence)', Resolved by = 'SYNTHESIZER -- Phase 3 (unresolved)'."

**PHASE COMPLETION PROOFs reference cross-phase attribution seeding**:
- PREDICTOR proof: "Cross-phase attribution seeded: TABLE G 'Predicted by' column will carry 'PREDICTOR -- Phase 1' for every row originated here."
- SCANNER proof: "Cross-phase attribution seeded: TABLE G 'Evidence rows cited' and 'Scanned by' columns will carry TABLE B row identifiers and 'SCANNER -- Phase 2' for every row of TABLE B used."
- SYNTHESIZER proof: "Cross-phase attribution complete: TABLE G 'Predicted by' = PREDICTOR Phase 1 for all rows. TABLE G 'Scanned by' = SCANNER Phase 2 for all rows. TABLE G 'Resolved by' = SYNTHESIZER Phase 3 for all rows. Attribution chain is complete and verifiable from TABLE G alone."

**SYNTHESIZER / END BOUNDARY** extended: "TABLE G cross-phase attribution chain complete: every row carries PREDICTOR (Phase 1) / SCANNER (Phase 2) / SYNTHESIZER (Phase 3) attribution."

| Criterion | Result | Evidence |
|---|---|---|
| C-01 through C-49 | PASS (all) | All invariants preserved across all three axes; TABLE G expansion adds columns but doesn't remove any required column |
| C-43 in particular | PASS (extended) | TABLE G is now a "cross-phase role completion audit record" — same dedicated purpose, richer structure |
| C-45 in particular | PASS (extended) | TABLE G schema annotation upgraded: "Serves as cross-phase role completion record" alongside "Produced by: SYNTHESIZER" |
| C-47 in particular | PASS (extended) | Remediation path explicitly populates all cross-phase attribution columns for unresolved rows |
| C-49 in particular | PASS (extended) | TABLE G attribution columns mean every named role can derive its complete execution history from the output table alone, not just from skill structure |

**V-05 Total: 100/100**

**Excellence signal**: TABLE G cross-phase attribution columns produce an emergent structural property beyond C-49. C-49 establishes that "every named role can derive its full responsibility set from skill structure alone." V-05 produces a stronger claim at the output level: "every named role can prove its complete execution history from TABLE G alone — from the prediction it originated, through the evidence collected on its behalf, to the resolution it produced or received." This is not a structural declaration property (C-49) but an output completeness property: a row in TABLE G is a complete cross-role audit record, self-contained without reference to the instruction sequence or phase labels.

---

## Ranking

All five variations achieve the same rubric score under v13. The rubric has no criterion that differentiates between them — C-01 through C-49 are all fully satisfied by V-01 (the baseline), and V-02 through V-05 add structural depth that exceeds the current ceiling.

| Rank | Variation | Score | Distinguishing structural depth |
|---|---|---|---|
| 1 (tied) | V-05 | 100/100 | All three axes + TABLE G cross-phase attribution — strongest emergent output property |
| 1 (tied) | V-04 | 100/100 | GATEKEEPER as named 4th role — strongest sequential enforcement |
| 1 (tied) | V-03 | 100/100 | PHASE COMPLETION PROOF — temporal verification closed at execution time |
| 1 (tied) | V-02 | 100/100 | ROLE SCOPE DECLARATION — strongest per-role independent auditability |
| 1 (tied) | V-01 | 100/100 | Baseline; establishes rubric ceiling as control |

**V-05 is the preferred candidate for R14 baseline** because it combines all three axes and adds the TABLE G cross-phase attribution columns, producing the richest structural foundation for the next wave of criteria.

---

## Excellence Signals (C-50 candidates)

### Signal 1 (from V-02): Role scope declaration as pre-phase named block

**Pattern**: Each phase opens with a `ROLE SCOPE DECLARATION: [ROLE]` block naming Authority (PAF citation), Permitted outputs (exact table list), Prohibited outputs (domain violations explicitly listed), and Constraint check (role-specific constraint confirmation). This creates a fourth verification layer: each role is independently auditable about its obligations and prohibitions without reading the instruction sequence. Constraint enforcement becomes role-local rather than only global (preamble + Phase 3 restatement). Not captured by any existing criterion.

### Signal 2 (from V-03): Phase completion proof as post-phase named block

**Pattern**: Each phase closes with a `PHASE COMPLETION PROOF -- [ROLE]` block that verifies PAF binding honored, table attribution honored, and constraint maintained, with STATUS: CONFIRMED / FAIL. This closes the compliance loop that C-49 opens: C-49 declares completeness at definition time; the proof block verifies it at execution time. The PHASE COMPLETION PROOF also becomes a hard gate prerequisite (gate checklist item: "PHASE COMPLETION PROOF for SCANNER shows STATUS: CONFIRMED"), making proof failure a structural gate blocker rather than a non-binding self-report.

### Signal 3 (from V-04): GATEKEEPER as named role with sole output constraint

**Pattern**: GATEKEEPER is a named fourth role with PAF Phase 2.5 binding, its own ROLE SCOPE DECLARATION, permitted output = PASS or FAIL token only, and an explicit scope violation definition ("any output beyond the token is a GATEKEEPER scope violation"). Gate failure is now a named role output rather than a structural boundary condition. This is the strongest enforcement framing for sequential constraint: violations are named, typed, and identifiable from the role's own scope declaration before they occur.

### Signal 4 (from V-05): TABLE G cross-phase attribution columns

**Pattern**: TABLE G gains "Predicted by", "Evidence rows cited", "Scanned by", and "Resolved by" columns, making every row a complete three-role, three-phase execution record. The completeness rule remediation path is extended to populate attribution columns even for unresolved rows. PHASE COMPLETION PROOFs reference cross-phase attribution seeding, and the SYNTHESIZER / END BOUNDARY confirms the attribution chain is complete. This produces a new output-level emergent property: "every named role can prove its complete execution history from TABLE G alone," stronger than C-49's process-level claim because it holds at the output artifact, not just the skill structure.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["role scope declaration block at phase start: each role explicitly names its PAF authority, permitted outputs, and prohibited outputs, making it independently auditable without reading the instruction sequence", "phase completion proof block at phase exit: post-phase verification confirms PAF binding honored, table attribution honored, and constraint maintained, adding a third temporal verification point and becoming a hard gate checklist prerequisite", "GATEKEEPER as named fourth role with PAF phase binding and sole output constraint: gate failure becomes a named role output rather than a boundary condition, making scope violations structurally identifiable before they occur", "TABLE G cross-phase attribution columns (Predicted by, Scanned by, Resolved by): TABLE G becomes a three-role three-phase completion audit record where every row proves complete execution history from output table alone without reference to the instruction sequence"]}
```
