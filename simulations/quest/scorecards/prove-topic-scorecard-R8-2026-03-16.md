Now I have all the information needed. Let me score all five variations.

---

## R8 Scorecard — prove-topic (rubric v8)

---

### Common Criteria — Same Result Across All Variations

All five variations share the R7 full-stack base. These criteria score identically:

| ID | Pts | All Variations | Evidence Note |
|----|-----|----------------|---------------|
| C-01 | 10 | **PASS** | All 6 EXIT SIGNALs in order: gate_open → hypothesis_locked → websearch_complete → interview_complete → prototype_complete → synthesis_complete |
| C-02 | 10 | **PASS** | All 6 artifact writes confirmed: scout (ROLE B), hypothesis, websearch, interview, prototype, synthesis+handoff |
| C-03 | 10 | **PASS** | SESSION INVARIANTS TABLE registers all three Invariant D templates; each stage INCUMBENT CHECK TABLE carries verbatim template with FORMAT ERROR label |
| C-04 | 10 | **PASS** | SYNTHESIS DECLARATIONS has hypothesis_verdict, confidence_composite, key_risk as labeled key-value pairs |
| C-05 | 10 | **PASS** | Stage 5 Block 3 reconstructs S2→S3→S4 chain with "Cross-check vs Stage 4 exit count: [Match/Mismatch]"; null_tally_final gated as Stage 5 entry condition |
| C-06 | 8 | **PASS** | ROLE B execution fills scout_artifact, scout_loaded, gate_s_cleared; CAMPAIGN BLOCKED path present |
| C-07 | 8 | **PASS** | All 11 HANDOFF TABLE fields + schema_compliance_confirmed; every field has [derived from: X] annotation |
| C-08 | 8 | **PASS** | BLOCK 2 counter-hypothesis resolution table with REFUTED/PARTIALLY REFUTED/OPEN RISK verdicts; OPEN RISK triggers confidence tier reduction |
| C-09 | 1 | **PASS** | null_tally_final >= 3 fires dual_lock (Lock 1 adversarial, Lock 2 -=2 cap); else not_triggered |
| C-10 | 1 | **PASS** | Per-stage INCUMBENT CHECK TABLEs use displacement framing; Stage 5 evidence_summary instructions cite Stage 4 displacement verdict (explicitly in V-01/V-03; via prototype Displacement read in V-02/V-04/V-05) |
| C-11 | 1 | **PASS** | "Template deviation = FORMAT ERROR", "CHAIN INTEGRITY FAILURE. Halt.", "Unlabeled = FAIL" — all mechanical, no advisory softening |
| C-12 | 1 | **PASS** | SESSION INVARIANTS TABLE is a standalone named block before Stage 0 gate_open |
| C-13 | 1 | **PASS** | SYNTHESIS DECLARATIONS section; hypothesis_verdict, confidence_composite, key_risk each on own labeled line |
| C-14 | 2 | **PARTIAL** (1) | FORMAT ERROR and FAIL echo registered labels; dual-lock inline uses "dual_lock_fired / BLOCKED" rather than echoing registered "DUAL-LOCK ERROR" label from SESSION INVARIANTS |
| C-15 | 1 | **PASS** | CAMPAIGN OPEN block with incumbent/status_quo_comparator pre-registered before SESSION INVARIANTS |
| C-16 | 1 | **PASS** | Stages 2, 3, 4 each carry labeled "Displacement read:" synthesis field; artifact write instructions include it in artifact body |
| C-17 | 1 | **PASS** | SYNTHESIS DECLARATIONS section header carries explicit prohibition: "Do not embed these values in prose sentences. Each on its own line, extractable by label match." |
| C-18 | 2 | **PASS** | Invariant C registers FAIL as canonical handoff label; schema_compliance_confirmed row echoes "Invariant E checkpoint — FAIL if any field unlabeled"; V-05 adds "echoes registered failure label from SESSION INVARIANTS" header |
| C-19 | 1 | **PASS** | Invariant D templates use "[incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR]" binding, not literal string |
| C-20 | 1 | **PASS** | All three artifact write instructions: "Artifact body includes Displacement read field. Confirm write." |
| C-21 | 1 | **PASS** | INCUMBENT ANCHOR sub-section present; "Do not re-establish the incumbent per stage. Carry forward from CAMPAIGN OPEN." |
| C-22 | 1 | **PASS** | Invariant D: "Binding: [incumbent from CAMPAIGN OPEN INCUMBENT ANCHOR] resolves to incumbent_name. Literal string = FORMAT ERROR." |
| C-24 | 1 | **PASS** | ROLE A: "incumbent_anchor_read: [INCUMBENT ANCHOR read: resolved incumbent_name confirmed. Invariant D binding active.]" before Stage 0 |
| C-26 | 1 | **PASS** | Binding note names sub-section specifically: "CAMPAIGN OPEN INCUMBENT ANCHOR" not just "CAMPAIGN OPEN" |
| C-27 | 1 | **PASS** | ROLE A commits "displacement_read_contract: [Stages 2, 3, 4 will write Displacement read field to artifact bodies. Stage 5 entry will confirm all three.]" |
| C-28 | 1 | **PASS** | Stage 5 ENTRY CONDITIONS: "All three artifact Displacement read fields confirmed written (websearch, interview, prototype)" present in all variations |
| C-29 | 1 | **PASS** | All five EXIT SIGNALs declare displacement read chain closure ("All three confirmed" or named form) |

**Shared base: 50 (essential) + 24 (recommended) + 19 (aspirational, with C-14 partial) = 93 pts**

---

### Variable Criteria — Per-Variation Analysis

#### C-23 — Stage 5 Cites At Least One Artifact Displacement Read (1 pt)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **PASS** | "cite artifact Displacement reads where available" — advisory but explicitly mentions artifact reads |
| V-02 | **PASS** | Mandatory instruction names all three artifact reads; at-least-one satisfied |
| V-03 | **PASS** | "cite artifact Displacement reads where available" — advisory; at least one instructed |
| V-04 | **PASS** | Mandatory instruction; at-least-one satisfied |
| V-05 | **PASS** | Mandatory instruction; at-least-one satisfied |

#### C-25 — Stage 5 Cites All Three Artifact Displacement Reads (1 pt)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | evidence_summary: "cite artifact Displacement reads where available" — conditional, does not structurally require all three |
| V-02 | **PASS** | "Must cite all three artifact Displacement reads (mandatory — not conditional): websearch..., interview..., prototype... Omission = FAIL." — all three required |
| V-03 | **FAIL** | evidence_summary: "cite artifact Displacement reads where available" — same advisory form as V-01; no structural mandate |
| V-04 | **PASS** | Same mandatory instruction as V-02; all three artifact reads named and required |
| V-05 | **PASS** | Same mandatory instruction; all three artifact reads named and required |

#### C-30 — evidence_summary Instruction Mandates All Three Reads (1 pt)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | "cite Stage 4 displacement verdict explicitly and cite artifact Displacement reads where available" — Stage-4-verdict-only mandate; artifact reads advisory only |
| V-02 | **PASS** | "Must cite all three artifact Displacement reads (mandatory — not conditional)... Omission of any artifact Displacement read = FAIL." — mandatory, names all three types |
| V-03 | **FAIL** | "cite Stage 4 displacement verdict explicitly and cite artifact Displacement reads where available" — advisory conditional; fails C-30 |
| V-04 | **PASS** | Same mandatory instruction as V-02 |
| V-05 | **PASS** | Same mandatory instruction as V-02 |

#### C-31 — Stage 5 Entry Gate Cross-References ROLE A Contract by Field Name (1 pt)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **PASS** | "[ ] All three artifact Displacement read fields confirmed written [per ROLE A displacement_read_contract — websearch, interview, prototype]." — names contract field explicitly |
| V-02 | **FAIL** | "[ ] All three artifact Displacement read fields confirmed written (websearch, interview, prototype). Stage 5 will consume all three." — no `displacement_read_contract` cross-reference |
| V-03 | **FAIL** | "[ ] All three artifact Displacement read fields confirmed written (websearch, interview, prototype). Stage 5 will consume all three." — no contract field name |
| V-04 | **PASS** | "[ ] All three artifact Displacement read fields confirmed written [per ROLE A displacement_read_contract — websearch, interview, prototype]." — PASS |
| V-05 | **PASS** | "[ ] All three artifact Displacement read fields confirmed written [per ROLE A displacement_read_contract — websearch, interview, prototype]." — PASS |

#### C-32 — Stage 5 EXIT SIGNAL Names Each Artifact Type Individually (1 pt)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | "All three artifact Displacement reads confirmed in evidence_summary." — count assertion, no per-artifact enumeration |
| V-02 | **FAIL** | "All three artifact Displacement reads cited in evidence_summary." — count assertion only |
| V-03 | **PASS** | "Displacement read chain closed: websearch Displacement read, interview Displacement read, prototype Displacement read — all three cited in evidence_summary." — names all three individually |
| V-04 | **FAIL** | "All three artifact Displacement reads confirmed in evidence_summary." — count assertion only |
| V-05 | **PASS** | "Displacement read chain closed: websearch Displacement read, interview Displacement read, prototype Displacement read — all three cited in evidence_summary. Chain closed." — named-provenance form |

---

### Composite Scores

| Variation | Base | +C-23 | +C-25 | +C-30 | +C-31 | +C-32 | Total | Essential Pass |
|-----------|------|-------|-------|-------|-------|-------|-------|----------------|
| V-01 | 93 | +1 | +0 | +0 | +1 | +0 | **95** | YES |
| V-02 | 93 | +1 | +1 | +1 | +0 | +0 | **96** | YES |
| V-03 | 93 | +1 | +0 | +0 | +0 | +1 | **95** | YES |
| V-04 | 93 | +1 | +1 | +1 | +1 | +0 | **97** | YES |
| V-05 | 93 | +1 | +1 | +1 | +1 | +1 | **98** | YES |

---

### Ranking

| Rank | Variation | Score | Criterion Delta from Rank Below |
|------|-----------|-------|----------------------------------|
| 1 | **V-05** | 98 | +C-32 (named-provenance EXIT SIGNAL) vs V-04 |
| 2 | **V-04** | 97 | +C-31 (entry gate contract cross-reference) vs V-02 |
| 3 | **V-02** | 96 | +C-25/C-30 (mandatory all-three citation) vs V-01/V-03 |
| 4 | **V-01** | 95 | +C-31 only; loses C-25/C-30/C-32 |
| 4 | **V-03** | 95 | +C-32 only; loses C-25/C-30/C-31 |

V-01 and V-03 tie at 95: each has one of the three R8 targets (C-31 and C-32 respectively) but neither fires the C-25/C-30 mandatory citation mechanism, making their synthesis output underspecified relative to the entry gate or EXIT SIGNAL improvements.

---

### Excellence Signals — V-05

**Signal 1 — Full contract-to-synthesis traceability chain closed at four layers:**
ROLE A commits `displacement_read_contract` pre-stage (C-27) → Stage 5 entry gate explicitly cross-references it by field name (C-31) → evidence_summary instruction mandates all three reads with hard failure language (C-30) → EXIT SIGNAL individually names websearch/interview/prototype in chain closure (C-32). No prior variation closed all four layers simultaneously.

**Signal 2 — Entry condition as contract-verification step, not independent check:**
The Stage 5 entry condition `[per ROLE A displacement_read_contract — websearch, interview, prototype]` changes the structural semantics: Stage 5 is not inventing a new rule about chain completeness; it is verifying that the contract committed by ROLE A is being honored. This makes the entry gate and ROLE A initialization semantically coupled rather than structurally parallel.

**Signal 3 — Named-provenance EXIT SIGNAL converts the campaign audit log:**
"Displacement read chain closed: websearch Displacement read, interview Displacement read, prototype Displacement read" produces an artifact-resolution trace readable without re-reading evidence_summary. Downstream consumers of the EXIT SIGNAL can verify which artifacts were consumed without reopening Stage 5 body. Count assertion ("all three confirmed") does not provide this property.

---

### R9 Open Target

C-10 remains untargeted: no variation anchors a ROLE 2 displacement loop role at Stage 3 to close the three-point displacement loop (Stage 2 → Stage 3 → Stage 4 as a structured adversarial relay).

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["Full contract-to-synthesis traceability chain: ROLE A displacement_read_contract committed pre-stage, Stage 5 entry gate verifies by field name, evidence_summary mandates all three reads by name, EXIT SIGNAL names each artifact type individually — four-layer chain closure", "Stage 5 entry gate as contract-verification step: [per ROLE A displacement_read_contract] cross-wires the entry condition to the pre-stage commitment by field name, making the gate semantically dependent on ROLE A rather than an independently conceived structural check", "Named-provenance EXIT SIGNAL: individually enumerating websearch/interview/prototype in chain-closure declaration produces a machine-verifiable artifact-resolution audit record, distinguishable from count assertion without re-reading evidence_summary"]}
```
