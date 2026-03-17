---
skill: quest-golden
skill_target: flow-conversation
date: 2026-03-14
rounds: 20
rubric_final: flow-conversation-rubric-v20-2026-03-14.md
score: 254
status: GOLDEN
---

# flow-conversation — Golden Prompt (R20)

**Winning variation:** V-05 — Combined: Lifecycle Emphasis + Output Format + Phrasing Register
**Simplification:** PASS (20% reduction — simplified body preferred)
**Rubric version:** v19 at scoring (C-01–C-78, max 254); v20 extracted from R20 signals (C-79–C-81, max 260)

---

## Prompt Body

You are simulating a Copilot Studio conversation-flow trace for: {{topic}}

Five sequential roles execute this protocol. Silent fallthrough is a structural violation.
All transitions are declared in the LIFECYCLE_PROTOCOL section; role instructions reference
by transition number only.

---

### LIFECYCLE_PROTOCOL (SOLE_AUTHORITY — MANDATORY NAMED SECTION)

**DIRECTIVE:** This section MUST be authored as a FIELD|VALUE table. It is the declaration
layer for all role-transition events.

| FIELD | VALUE |
|-------|-------|
| SECTION_NAME | LIFECYCLE_PROTOCOL |
| AUTHORITY_CLASS | SOLE_AUTHORITY |
| DECLARATION_LAYER | This section: every role-transition event is declared exactly once here, and nowhere else in role instruction blocks. |
| REFERENCE_LAYER | Phase 6-A LIFECYCLE_POINTER_AUDIT: verifies every pointer of the form "per LIFECYCLE_PROTOCOL Transition T-N" in role instruction blocks resolves to a labeled transition in this section. |
| CLOSURE_STATEMENT | Neither layer alone closes the single-source enforcement system. Declaration-layer discipline without reference-layer verification leaves dangling pointers to non-existent or re-numbered transitions undetected. Reference-layer verification without declaration-layer discipline allows unauthorized re-declarations that create divergence points. Both layers must operate simultaneously. |
| SILENT_FALLTHROUGH_RULE | Every boundary: outgoing HANDOFF_TO token + incoming acknowledgment required. |
| T-1 | Phase -1 → Topology Architect. Outgoing: `HANDOFF_TO: TOPOLOGY ARCHITECT`. Incoming: `"Received PRE_FLIGHT_MANIFEST."` |
| T-2 | Topology Architect → Contract Auditor. Outgoing: `HANDOFF_TO: CONTRACT AUDITOR for Phase 0-CA-1`. Incoming: `"Received Phase 0-A artifacts."` |
| T-3 | Contract Auditor → Developer. Outgoing: `GATE_STATUS: [value]. HANDOFF_TO: DEVELOPER`. Incoming: `"Received GATE_STATUS: [value]. Proceeding\|Blocked."` |
| T-4 | Developer → Auditor. Outgoing: `DEVELOPER_CERTIFICATION: COMPLETE. HANDOFF_TO: AUDITOR`. Incoming: `"Received DEVELOPER_CERTIFICATION: COMPLETE. Beginning independent audit."` |
| T-5 | Auditor → Report Producer. Outgoing: `AUDITOR_CERTIFICATION: COMPLETE. HANDOFF_TO: REPORT PRODUCER`. Incoming: `"Received AUDITOR_CERTIFICATION: COMPLETE."` |

**DIRECTIVE:** Role instruction blocks MUST reference transitions by T-N number only.
Inline re-declaration outside this section is UNAUTHORIZED_DIVERGENCE_POINT.

---

### PHASE -1 — CONTRACT AUDITOR (Pre-Flight Manifest)

**DIRECTIVE:** Issue PRE_FLIGHT_MANIFEST (REQUIRED_DECLARATION|PHASE_REF|SCHEMA_TYPE|STATUS: PENDING).
All 11 declarations. SCHEMA_TYPE = FIELD|VALUE for 0-A-6, 0-A-8, 0-A-9, 0-A-10, 0-A-11.
Close per LIFECYCLE_PROTOCOL T-1.

---

### PHASE 0 — TOPOLOGY ARCHITECT

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-1 receive acknowledgment.

Author Phase 0-D-1 through 0-D-5 and Phase 0-A-6 through 0-A-11. FIELD|VALUE declarations:
two-column table rows only; prose substitution is WRONG_SCHEMA by definition.

**COLUMN_SCHEMA_CONTRACT** (required table before Phase 1):

| COLUMN_NAME | FORMAT | ALLOWED_VALUES | REQUIRED_WHEN |
|-------------|--------|----------------|---------------|

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-2.

---

### PHASE 0-CA-1 — CONTRACT AUDITOR (Completeness Gate)

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-2 receive acknowledgment.

Update manifest rows (COMPLETE|MISSING|WRONG_SCHEMA). A FIELD|VALUE declaration authored in
multi-column or prose format MUST be marked WRONG_SCHEMA (not MISSING). Verify all deltas
(COVERAGE_DELTA, CHAIN_BUDGET_DELTA, PREDICTION_CONTRACT_SIGNED, STATUS_QUO_METHOD_SIGNED,
COLUMN_SCHEMA_COMPLETE). Per FIELD|VALUE declaration: `NAME: PASS|FAIL (count N rows: [breakdown])`.
PRE_FLIGHT_MANIFEST_STATUS: PASS|FAIL.

**DIRECTIVE — CONTRACT_AUDIT_GATE_HONORED SCHEMA:** Emit as FIELD|VALUE table. Every field
below is mandatory; a missing row is a schema gap the Phase 6-A Auditor MUST flag as a gate
structural finding:

| FIELD | VALUE |
|-------|-------|
| STATUS | PASS\|FAIL |
| STANDALONE_DECLARATION | This CONTRACT_AUDIT_GATE_HONORED block is a complete standalone audit summary. A verifier reading this block does not need to navigate to Phase 6-A tables or Phase 0-CA-1 output to confirm format compliance (WRONG_SCHEMA sweep) and row-count completeness (parenthetical verification). |
| WRONG_SCHEMA_RESIDUAL_SWEEP | CONFIRMED\|NOT_CONFIRMED (sweep scope: [named declarations checked]; or "CLEAN — no WRONG_SCHEMA rows found") |
| PARENTHETICAL_VERIFICATION | CONFIRMED\|NOT_CONFIRMED ([DECLARATION: N rows CONFIRMED, ...]) |
| BUDGET_UTILIZATION_VERIFIED | PASS\|FAIL |
| BUDGET_STATUS_CONSISTENT | PASS\|FAIL |

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-3.

---

### PHASE 1–5 — DEVELOPER

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-3 receive acknowledgment. GATE_STATUS: FAIL blocks
execution — document block reason and stop.

**Phase 1** Turn table: every COLUMN_SCHEMA_CONTRACT column present in every row. Phase 1-S
SESSION_TIMELINE (mutation log) MUST precede Phase 1 SESSION_STATE authoring; SESSION_STATE
cells MUST cite Phase 1-S source entry.

**Phase 1-T** Topic aggregate (strictly additive: does not replace Phase 1 turn table).

**Phase 2** Nine defect classes:
1. Dead end 2. Infinite loop 3. Intent collision 4. Missing fallback 5. TIMELINE_ANOMALY
6. PREDICTION_DEVIATION 7. CHAIN_BUDGET_EXCEEDED

P0 defects: EXECUTION_HALT block (HALT_TRIGGER|ROOT_CAUSE|MVF_RECOMMENDATION|MVF_SCOPE|
UNBLOCKED_BY|CHAIN_BREAK_TRACE|CHAIN_REPAIR) BEFORE lower-severity defects.

**Phase 3** ENTANGLEMENT_MAP (3-E): ENTANGLEMENT_VERDICT per FOUND defect.

**Phase 4** Fallback chain trace to completion. Escalation path trace. Disambiguation strategy
per intent collision.

**Phase 4-SQ** STATUS_QUO_SIMULATION: abbreviated trace using only STATUS_QUO_METHOD.
Per turn: TURN_ID|TOPIC_MATCHED|AGENT_RESPONSE_SUMMARY|SQ_DEFECT_FOUND|SQ_DEFECT_CLASS|REMARKS.
STATUS_QUO_FINDINGS summary after.

**Phase 5** In sequence:
1. DEVIATION_BUDGET_UTILIZATION (SEVERITY|BUDGET|ACTUAL_DEVIATES|STATUS; OVERALL_BUDGET_STATUS)
2. CHAIN_BUDGET_UTILIZATION (HEAD_CONV|CHAIN_BUDGET|HEAD_DEVIATES_COUNT|STATUS per chain; CHAIN_BUDGET_EXCEEDED findings)
3. COVERAGE_QUALITY_GATE: CLEAN|DEGRADED (CLEAN requires TIMELINE_ANOMALY_RATE = 0; DEGRADED makes all five ratios PROVISIONAL)
4. CONSTRAINT_CHAIN_STATUS_SUMMARY (CHAIN_ID|HEAD_CONV|CHAIN_LENGTH|TURNS_SUSPENDED|FINAL_STATUS)
5. Five coverage ratios: topic_coverage_ratio · transitions_exercised/total_declared · slot_path_coverage · TIMELINE_ANOMALY_RATE · PATH_ADHERENCE_RATIO
6. Phase 5-F STATUS_QUO_COVERAGE: per FOUND defect DEFECT_ID|DEFECT_CLASS|FOUND_BY_SIMULATION|FOUND_BY_STATUS_QUO|DETECTION_METHOD|SQ_BLIND_SPOT. STATUS_QUO_GAP_SUMMARY.

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-4.

---

### PHASE 6 — AUDITOR

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-4 receive acknowledgment.

**Phase 6-A:**

**DIRECTIVE:** Emit CONTRACT_AUDIT_GATE_HONORED as FIELD|VALUE table per schema declared in
Phase 0-CA-1. STANDALONE_DECLARATION field MUST be populated with prescribed text; an empty
or missing STANDALONE_DECLARATION row is a Phase 6-A structural gap finding. Include:

- LIFECYCLE_POINTER_AUDIT sub-table: enumerate every "per LIFECYCLE_PROTOCOL Transition T-N"
  reference found across all role instruction blocks (ROLE|POINTER_TEXT|TARGET_TRANSITION|
  RESOLVED: YES|NO). Unresolved = DANGLING_LIFECYCLE_POINTER finding.
- SIMULATION_DELTA_COMPLETE: PASS|FAIL.

**Phase 6-B** Severity Co-Residency Audit: every FOUND defect row verified for both
SEVERITY_CLASS and INVARIANT_CITE; CONFIRMED_ABSENT rows EXEMPT.

**Phase 6-C** Entanglement map consistency.

**Phase 6-D** Topic aggregate consistency: conformance_rollup vs DEVIATES count per topic;
TOPIC_ROLLUP_MISMATCH findings.

**Phase 6-E** SESSION_TIMELINE replay verification.

**Phase 6-F** Fix Viability: per EXECUTION_HALT block —
CONV_VIOLATIONS_INTRODUCED|CONV_VIOLATIONS_DETAIL|VIABILITY|CHAIN_REPAIR_COMPLETE.

**Phase 6-G** Chain Integrity: per CHAIN-NN (CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED;
CHAIN_VERDICT_INCONSISTENCY findings).

**Phase 6-H** Combined:
- PATH_ADHERENCE_AUDIT: per-turn PREDICTION_MATCH; PATH_ADHERENCE_RATIO_VERIFIED;
  CRITICAL_PATH_ESCALATION_VERIFIED.
- PLAN_INTEGRITY_AUDIT: EXECUTION_HALT_IN_PLAN + CHAIN_REPAIR_IN_SCOPE;
  DEPENDENCY_ORDER_VALID per PLAN_ITEM; PLAN_INTEGRITY_AUDIT: PASS|FAIL; DEPENDENCY_CYCLE_CHECK.
- PLAN_TIER_OVERRIDE_PRESENT + OVERRIDE_TIER_HONORED for CRITICAL-path PREDICTION_DEVIATION defects.
- STATUS_QUO_COVERAGE_AUDIT: DETECTION_METHOD per defect; AUTOMATIC_CLASSIFICATION_VERIFIED;
  STATUS_QUO_COVERAGE_AUDIT: PASS|FAIL.

**DIRECTIVE:** Close per LIFECYCLE_PROTOCOL T-5.

---

### PHASE 7 — REMEDIATION PLANNER

**DIRECTIVE:** Open per LIFECYCLE_PROTOCOL T-5 receive acknowledgment.

Topologically sorted REMEDIATION_PLAN. Per FOUND defect: PLAN_ITEM (PLAN_ID: RP-NN|DEFECT_REF|
SEVERITY_CLASS|SCOPE|DEPENDENCY_ON|PLAN_TIER|TIER_RATIONALE|CHAIN_REPAIR_ITEMS|UNBLOCKED_BY).
CRITICAL-path PREDICTION_DEVIATION defects carry PLAN_TIER_OVERRIDE: IMMEDIATE.
PLAN_SUMMARY: PLAN_ITEM_COUNT|IMMEDIATE_COUNT|NEXT_SPRINT_COUNT|BACKLOG_COUNT|
DEPENDENCY_CYCLE_CHECK: PASS|CYCLE_FOUND.

---

## What Made It Golden

Five axes were tested. V-05 combined the three that independently contributed, while V-03
(the other 254 scorer) used DIRECTIVE labels as the enforcement mechanism. V-05 chose
schema enforcement over label enforcement — making omissions auditable rather than just
prohibited.

### 1. LIFECYCLE_PROTOCOL as a FIELD|VALUE block

All prior variations authored the LIFECYCLE_PROTOCOL as prose or mixed prose+table. V-05
made the entire section — including SECTION_NAME, AUTHORITY_CLASS, DECLARATION_LAYER,
REFERENCE_LAYER, CLOSURE_STATEMENT, and SILENT_FALLTHROUGH_RULE — mandatory FIELD|VALUE
rows. This converts C-77's "narrative must be present" into a table-schema enforcement:
the Auditor can flag a missing CLOSURE_STATEMENT row as WRONG_SCHEMA, the same mechanism
used for all other declarations. The structural enforcement path is uniform.

### 2. CLOSURE_STATEMENT as a named mandatory row

The two-layer closure — "Neither layer alone closes the single-source enforcement system" —
is what separates C-76 (both layers operating) from C-77 (both layers declared as design
intent). V-01 expressed this as prose framing. V-03 expressed it as DIRECTIVE text. V-05
made it a named FIELD|VALUE row with a required value string. The Auditor can flag its
absence without inference; it either exists as a table row or it does not.

### 3. CONTRACT_AUDIT_GATE_HONORED as a declared schema with STANDALONE_DECLARATION

V-01 implied standalone completeness from the presence of gate fields. V-05 made
STANDALONE_DECLARATION a mandatory named row in the gate schema, declared in Phase 0-CA-1
and enforced by Phase 6-A. The verifier does not infer standalone capability — they check
for the row. If absent, Phase 6-A flags it as a structural gap finding (same weight as
MISSING). C-78 fires because the framing statement is schema-enforced, not prose-dependent.

### 4. Bidirectional schema enforcement for the gate block

Phase 0-CA-1 declares the CONTRACT_AUDIT_GATE_HONORED FIELD|VALUE schema (where the gate
is specified). Phase 6-A enforces it (where the gate is emitted). A model satisfying
Phase 6-A without satisfying Phase 0-CA-1 is structurally inconsistent — the schema
enforcement is bidirectional, not deferred to a single audit phase.

### 5. DIRECTIVE labels eliminate prose hedging space

Every structural requirement in V-05 carries an explicit DIRECTIVE label. This is the
pattern V-03 pioneered: DIRECTIVE-labeled instructions leave no prose hedging space for
omission. V-05 retained all DIRECTIVE labels from V-03 and added schema enforcement
on top. The combination means two independent failure modes for omissions: label
violation (MUST) and schema gap (auditable by Auditor). V-01, by contrast, relied on
prose framing that the model could satisfy with paraphrase.

---

## Final Rubric Criteria Summary (v20)

**Max score: 260 | Aspirational: 170 | Required: 120 | Recommended: 50 | Essential: 45**

### Essential (60 pts)

| ID | Criterion | Weight |
|----|-----------|--------|
| C-01 | Dialog path traced as turns | 15 |
| C-02 | All four defect classes addressed | 15 |
| C-03 | Session state tracked | 15 |
| C-04 | Copilot Studio framing | 15 |

### Recommended (30 pts)

| ID | Criterion | Weight |
|----|-----------|--------|
| C-05 | Defect reproduction steps | 10 |
| C-06 | Fallback chain coverage | 10 |
| C-07 | Intent collision disambiguation | 10 |

### Required — 1 pt block (13 pts)

| ID | Criterion | Weight |
|----|-----------|--------|
| C-08 | Graph coverage metric | 1 |
| C-09 | Adversarial turn injection | 1 |
| C-10 | Prohibited vocabulary gate | 1 |
| C-11 | Turn-level conformance verdict | 1 |
| C-12 | Topic graph pre-declaration | 1 |
| C-13 | Session variable registry | 1 |
| C-14 | Invariant register | 1 |
| C-15 | Escalation path | 1 |
| C-16 | Phase 0 contract | 1 |
| C-17 | Role separation | 1 |
| C-18 | Slot-fill coverage | 1 |
| C-19 | Orphan topic detection | 1 |
| C-20 | Recovery verdict | 1 |

### Required — multi-pt block A (C-21–C-44, 67 pts)

| ID | Criterion | Weight |
|----|-----------|--------|
| C-21 | Severity co-residency audit | 4 |
| C-22 | Transition map | 3 |
| C-23 | Entanglement (3-E) | 3 |
| C-24 | Topic aggregate (1-T) | 2 |
| C-25 | Session timeline | 2 |
| C-26 | Mutation log | 2 |
| C-27 | TIMELINE_ANOMALY | 4 |
| C-28 | Phase 6-D topic rollup audit | 2 |
| C-29 | Phase 6-E timeline replay | 2 |
| C-30 | Mutation-first authoring | 2 |
| C-31 | AUTHORIZED_REWRITERS | 2 |
| C-32 | Contract Auditor gate | 3 |
| C-33 | Phase 6-A audit block | 3 |
| C-34 | COVERAGE_QUALITY_GATE | 3 |
| C-35 | SIMULATION_DELTA | 3 |
| C-36 | CONSTRAINT_VERDICTS | 3 |
| C-37 | Arithmetic evidence | 3 |
| C-38 | EXECUTION_HALT | 4 |
| C-39 | Phase 6-F viability | 3 |
| C-40 | PROPAGATION + CHAIN_ID | 3 |
| C-41 | CHAIN_EFFECTS | 3 |
| C-42 | Constraint chain summary | 2 |
| C-43 | Chain integrity audit | 3 |
| C-44 | CHAIN_BREAK_TRACE | 3 |

### Required — multi-pt block B (C-45–C-76, 80 pts)

| ID | Criterion | Weight |
|----|-----------|--------|
| C-45 | DEVIATION_BUDGET | 3 |
| C-46 | Budget utilization block | 3 |
| C-47 | CONV_CHAIN_BUDGET | 3 |
| C-48 | CHAIN_BUDGET_EXCEEDED | 3 |
| C-49 | Remediation plan | 3 |
| C-50 | Plan integrity audit | 3 |
| C-51 | TURN_PREDICTION_CONTRACT | 3 |
| C-52 | PREDICTION_DEVIATION | 3 |
| C-53 | PATH_ADHERENCE | 3 |
| C-54 | PLAN_TIER_OVERRIDE | 3 |
| C-55 | STATUS_QUO_METHOD | 3 |
| C-56 | STATUS_QUO_SIMULATION | 3 |
| C-57 | STATUS_QUO_COVERAGE | 3 |
| C-58 | STATUS_QUO_COVERAGE_AUDIT | 3 |
| C-59 | Pre-flight manifest | 2 |
| C-60 | Handoff tokens | 2 |
| C-61 | COLUMN_SCHEMA_CONTRACT | 2 |
| C-62 | FIELD\|VALUE schema | 3 |
| C-63 | HANDOFF_TO chain | 2 |
| C-64 | Manifest schema-type annotation | 2 |
| C-65 | Quantitative row-count contract | 3 |
| C-66 | WRONG_SCHEMA sweep | 3 |
| C-67 | Parenthetical verification | 3 |
| C-68 | Sweep as gate precondition | 3 |
| C-69 | Lifecycle single source of truth | 3 |
| C-70 | Parenthetical as gate precondition | 3 |
| C-71 | WRONG_SCHEMA gate field | 3 |
| C-72 | LIFECYCLE_POINTER_AUDIT | 3 |
| C-73 | Parenthetical gate field | 3 |
| C-74 | CONTRACT_AUDIT_GATE_HONORED self-describing | 3 |
| C-75 | Declaration-to-reference closure | 3 |
| C-76 | Both layers operating | 3 |

### Aspirational (v19 additions — 4 pts)

| ID | Criterion | Weight | Chain |
|----|-----------|--------|-------|
| C-77 | LIFECYCLE_PROTOCOL SOLE_AUTHORITY header + two-layer closure narrative with "neither layer alone" statement | 2 | C-77 → C-76 → C-73 → C-70 → C-66 → C-63 |
| C-78 | CONTRACT_AUDIT_GATE_HONORED explicit standalone completeness declaration as named field | 2 | C-78 → C-75 → C-72 ^ C-74 |

### Aspirational (v20 additions — 6 pts)

| ID | Criterion | Weight | Chain | Source variation |
|----|-----------|--------|-------|-----------------|
| C-79 | LIFECYCLE_PROTOCOL_DESIGN_CONTRACT issued by Phase -1 before TA authoring; TA receives and reproduces SOLE_AUTHORITY DECLARATION | 2 | C-79 → C-77 | V-04 (R20) |
| C-80 | Two-layer closure strings DIRECTIVE-prescribed with exact mandatory text inside LIFECYCLE_PROTOCOL section | 2 | C-80 → C-77 | V-03 (R20) |
| C-81 | STANDALONE_DECLARATION as mandatory named FIELD\|VALUE row, Phase 0-CA-1 prescribes exact text, Phase 6-A independently flags absence as structural finding | 2 | C-81 → C-78 → C-75 → C-72 ^ C-74 | V-02 + V-03 (R20) |

---

## Scoring Summary

| Tier | Threshold | V-05 (v19) | V-05 (v20 potential) |
|------|-----------|-----------|---------------------|
| Essential pass | 45 | 60 / 60 | 60 / 60 |
| Recommended pass | 50 | 90 / 90 | 90 / 90 |
| Required pass | 120 | 250 / 250 | 250 / 250 |
| Aspirational (v19) | 164 | 254 / 254 | 254 / 254 |
| Aspirational (v20) | 170 | — | 260 / 260 (ceiling) |

V-05 is the ceiling variation for v19 (254/254). It also seeds all three v20 criteria
(C-79 from V-04, C-80 from V-03, C-81 from V-02 + V-03), making it the source for the
next rubric round's aspirational tier rather than merely a solver of the current one.
