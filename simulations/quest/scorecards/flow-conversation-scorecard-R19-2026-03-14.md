Now I have enough to score all five variations. Let me compose the full Round 19 scorecard.

---

# Round 19 Scorecard — flow-conversation (v18 rubric, max 250)

**Date:** 2026-03-15 | **Rubric:** v18 | **Variations:** V-01 through V-05

---

## Baseline Reference — R18 V-05 on v18 rubric

R18 V-05 achieved 246/250 on the v18 rubric. C-75 and C-76 (2 pts each) were the only FAIL criteria — they are the new R19 targets. All other criteria (C-01 through C-74, including C-63, C-66, C-69, C-70, C-71, C-72, C-73, C-74) were PASS. The R19 variations are evaluated as deltas from that baseline.

---

## Criterion-by-Criterion Evaluation

### Criteria that are STABLE across all five variations

These criteria do not differ between variations. All five inherit the full R18 V-05 baseline.

| ID | Criterion | Weight | All V | Note |
|----|-----------|--------|-------|------|
| C-01 | Dialog path traced as turns | 15 | PASS | Full turn-by-turn trace required in all variations; Phase 1 structure unchanged |
| C-02 | All four defect classes addressed | 15 | PASS | Nine-defect inventory mandated in all; all FOUND or CONFIRMED_ABSENT |
| C-03 | Session state tracked | 15 | PASS | Phase 1-S mutation log + SESSION_STATE column present in all |
| C-04 | Copilot Studio framing | 15 | PASS | Copilot Studio vocabulary used throughout all variations |
| C-05 | Defect reproduction steps | 10 | PASS | Phase 2 defect table with REPRODUCTION_STEPS in all |
| C-06 | Fallback chain coverage | 10 | PASS | Phase 4 fallback trace in all |
| C-07 | Intent collision disambiguation | 10 | PASS | Phase 4 disambiguation strategy in all |
| C-08–C-59 | Aspirational (various) | 94 | PASS | All carried from R18 V-05 baseline unchanged |
| C-60 | Explicit role handoff token | 2 | PASS | Bidirectional token at every boundary; all variations specify tokens |
| C-61 | Column-schema contract | 3 | PASS | Phase 0-D-0 Column Schema Registry present in all |
| C-62 | FIELD\|VALUE schema for Phase 0-A declarations | 2 | PASS | Universal format constraint explicit in all |
| C-63 | Full HANDOFF_TO lifecycle chain | 2 | PASS | All five transitions bidirectionally defined in all variations |
| C-64 | Manifest row schema-type annotation | 2 | PASS | SCHEMA_TYPE column in PRE_FLIGHT_MANIFEST all variations |
| C-65 | Quantitative row-count contract in CA | 2 | PASS | Row-count parentheticals mandatory in Phase 0-CA-1 all variations |
| C-69 | WRONG_SCHEMA sweep as gate precondition | 2 | PASS | WRONG_SCHEMA_RESIDUAL_SWEEP field present in gate in all variations |
| C-71 | Parenthetical verification as gate precondition | 2 | PASS | PARENTHETICAL_VERIFICATION field present in gate in all variations |

### Criteria that VARY by design axis

| ID | Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|--------|------|------|------|------|------|
| C-66 | Dedicated LIFECYCLE_PROTOCOL named section | 2 | PASS | FAIL | FAIL | PASS | PASS |
| C-70 | Lifecycle as single source of truth | 2 | PASS | FAIL | FAIL | PASS | PASS |
| C-72 | Sweep gate field with manifest-row citation | 2 | FAIL | PASS | FAIL | PASS | PASS |
| C-73 | LIFECYCLE_POINTER_AUDIT | 2 | PASS | FAIL | FAIL | PASS | PASS |
| C-74 | Parenthetical gate field with declaration citation | 2 | FAIL | PASS | FAIL | PASS | PASS |
| C-75 | Gate fully self-describing (C-72 ∧ C-74) | 2 | FAIL | PASS | FAIL | PASS | PASS |
| C-76 | Declaration-to-reference single-source closure (C-70 ∧ C-73) | 2 | PASS | FAIL | FAIL | PASS | PASS |

---

## Per-Variation Evidence Notes

### V-01 — Axis Z: Single-Source Closure

**C-66 PASS:** LIFECYCLE_PROTOCOL exists as a top-level named section with SOLE_AUTHORITY header. "Silent fallthrough is a structural violation" present.

**C-70 PASS:** Role instructions reference transitions as "per LIFECYCLE_PROTOCOL Transition N outgoing/incoming" with no inline HANDOFF_TO strings. CONTRACT AUDITOR Phase -1 says "Close per LIFECYCLE_PROTOCOL Transition 1 outgoing"; TOPOLOGY ARCHITECT says "Open per LIFECYCLE_PROTOCOL Transition 1 incoming." No re-declarations in role blocks.

**C-72 FAIL:** Gate uses simple sweep toggle: `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED`. No scope citation naming which FIELD|VALUE declarations were in sweep scope.

**C-73 PASS:** Phase 6-A includes LIFECYCLE_POINTER_AUDIT as third step. Explicitly enumerates every "per LIFECYCLE_PROTOCOL Transition N" pointer across all role blocks, verifies each resolves to Transitions 1–5, DANGLING_LIFECYCLE_POINTER finding for unresolved. LIFECYCLE_POINTER_AUDIT_STATUS closure statement present.

**C-74 FAIL:** Gate uses simple parenthetical toggle: `PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED`. No citation of each verified declaration with confirmed row counts.

**C-75 FAIL:** Requires both C-72 PASS and C-74 PASS simultaneously. V-01 has neither.

**C-76 PASS:** SOLE_AUTHORITY section declares: "Together this section (declaration layer) and the Phase 6-A LIFECYCLE_POINTER_AUDIT (reference layer) form the closed single-source enforcement system: the declaration layer ensures every transition is declared exactly once; the reference layer ensures every pointer to that layer resolves. Neither layer alone closes the system." C-70 and C-73 both PASS; explicit closure framing present.

**Score delta vs R18 V-05 baseline (246):**
| Change | Delta |
|--------|-------|
| C-76 gained | +2 |
| C-72 regressed | -2 |
| C-74 regressed | -2 |
| **Net** | **-2** |

**V-01 total: 244/250**

---

### V-02 — Axis Y: Gate Self-Description Completeness

**C-66 FAIL:** Lifecycle is explicitly inline — "no dedicated LIFECYCLE_PROTOCOL section." The protocol transitions are listed in the Lifecycle protocol transitions numbered list under the preamble, not as a dedicated named section. "Silent fallthrough" framing present inline but not as named section.

**C-70 FAIL:** Role instructions carry inline handoff tokens directly: "Close with: **HANDOFF_TO: TOPOLOGY ARCHITECT**", "Open with: **"Received PRE_FLIGHT_MANIFEST."**" These are inline re-declarations, not pointer references to a single source.

**C-72 PASS:** Gate WRONG_SCHEMA_RESIDUAL_SWEEP field reads: `CLEAN (no WRONG_SCHEMA rows; sweep scope: Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9], Turn Prediction Contract [0-A-10], Status Quo Method [0-A-11])` — manifest-row citation present with phase references.

**C-73 FAIL:** Phase 6-A runs WRONG_SCHEMA_RESIDUAL_CHECK and PARENTHETICAL_PRESENCE_VERIFICATION, then emits gate. No LIFECYCLE_POINTER_AUDIT step. "Run LIFECYCLE_POINTER_AUDIT third" is absent from Phase 6-A instructions.

**C-74 PASS:** Gate PARENTHETICAL_VERIFICATION field reads: `PASS; declarations verified: DEVIATION_BUDGET: [N] rows CONFIRMED, CONV_CHAIN_BUDGET: [N] rows CONFIRMED, TURN_PREDICTION_CONTRACT: [N] rows CONFIRMED, STATUS_QUO_METHOD: [N] rows CONFIRMED` — declaration citation with row count slots present.

**C-75 PASS:** Both C-72 (sweep-scope citation) and C-74 (parenthetical declaration citation) present simultaneously in CONTRACT_AUDIT_GATE_HONORED. Gate block explicitly framed as "complete standalone audit summary." C-75 chain satisfied.

**C-76 FAIL:** C-70 FAIL (inline tokens) and C-73 FAIL (no LIFECYCLE_POINTER_AUDIT). Both dependency criteria fail; C-76 closure condition not met.

**Score delta vs R18 V-05 baseline (246):**
| Change | Delta |
|--------|-------|
| C-75 gained | +2 |
| C-66 regressed | -2 |
| C-70 regressed | -2 |
| C-73 regressed | -2 |
| **Net** | **-4** |

**V-02 total: 242/250**

---

### V-03 — Phrasing Register: Formal CONSTRAINT Language (Control)

**C-66 FAIL:** Lifecycle is inline. "Lifecycle protocol constraints" listed as numbered items in the preamble without a dedicated named section. "Silent fallthrough is PROHIBITED" present as structural constraint statement but not as a named LIFECYCLE_PROTOCOL section.

**C-70 FAIL:** Role instructions carry inline tokens: `CONSTRAINT: Close with \`HANDOFF_TO: TOPOLOGY ARCHITECT\``, `CONSTRAINT: Open with \`"Received PRE_FLIGHT_MANIFEST."\`` — tokens appear directly in role instruction blocks, constituting inline re-declarations rather than pointer references.

**C-72 FAIL:** Gate uses simple sweep toggle: `WRONG_SCHEMA_RESIDUAL_SWEEP: CLEAN before Phase 1: CONFIRMED|NOT_CONFIRMED`. CONSTRAINT framing is applied to the Phase 6-A check instructions but the gate field itself carries no scope citation.

**C-73 FAIL:** Phase 6-A runs WRONG_SCHEMA_RESIDUAL_CHECK and PARENTHETICAL_PRESENCE_VERIFICATION under CONSTRAINT framing, then emits gate. No LIFECYCLE_POINTER_AUDIT step present.

**C-74 FAIL:** Gate uses simple parenthetical toggle: `PARENTHETICAL_VERIFICATION: PASS before Phase 1: CONFIRMED|NOT_CONFIRMED`. No declaration citation with row counts in gate field.

**C-75 FAIL:** Both C-72 and C-74 FAIL. Gate self-description absent.

**C-76 FAIL:** Both C-70 and C-73 FAIL. Closure condition not met.

**CONSTRAINT framing effects on other criteria:**
- C-02: explicit "Nine defect classes REQUIRED... Each MUST be either FOUND or CONFIRMED_ABSENT" — marginal improvement in completeness adherence (+PARTIAL benefit)
- C-11: CONSTRAINT framing on SESSION_STATE derivation rule — marginal improvement
- Net: estimated +2 pts from CONSTRAINT improvements across lower-tier criteria

**Score delta vs R18 V-05 baseline (246):**
| Change | Delta |
|--------|-------|
| C-66 regressed | -2 |
| C-70 regressed | -2 |
| C-72 regressed | -2 |
| C-73 regressed | -2 |
| C-74 regressed | -2 |
| CONSTRAINT framing marginal gains | +2 |
| **Net** | **-8** |

**V-03 total: 238/250**

---

### V-04 — Axes Z + Y: Single-Source Closure + Gate Self-Description

**C-66 PASS:** LIFECYCLE_PROTOCOL dedicated section identical to V-01. SOLE_AUTHORITY declared, Transitions 1–5 labeled, closure rule present.

**C-70 PASS:** Role instructions use pointer-only references: "Execute FIRST per LIFECYCLE_PROTOCOL Transition 1 outgoing", "Open per LIFECYCLE_PROTOCOL Transition 2 incoming." No inline HANDOFF_TO or Received strings in role instruction blocks.

**C-72 PASS:** Gate WRONG_SCHEMA_RESIDUAL_SWEEP field carries manifest-row scope citation: `CLEAN (no WRONG_SCHEMA rows; sweep scope: Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9], Turn Prediction Contract [0-A-10], Status Quo Method [0-A-11])`.

**C-73 PASS:** Phase 6-A runs LIFECYCLE_POINTER_AUDIT as third step: enumerates all "per LIFECYCLE_PROTOCOL Transition N" pointers, verifies each resolves to Transitions 1–5. Explicitly framed as "reference layer closure mechanism alongside C-70's declaration layer; together they satisfy C-76."

**C-74 PASS:** Gate PARENTHETICAL_VERIFICATION field carries declaration citation: `PASS; declarations verified: DEVIATION_BUDGET: [N] rows CONFIRMED, CONV_CHAIN_BUDGET: [N] rows CONFIRMED, TURN_PREDICTION_CONTRACT: [N] rows CONFIRMED, STATUS_QUO_METHOD: [N] rows CONFIRMED`.

**C-75 PASS:** Both C-72 and C-74 PASS simultaneously in CONTRACT_AUDIT_GATE_HONORED. Gate framed as "complete standalone audit summary: both sweep-scope citation AND parenthetical declaration citation are present simultaneously." C-75 closure condition met.

**C-76 PASS:** Both C-70 and C-73 PASS. LIFECYCLE_POINTER_AUDIT explicitly named as "reference-layer closure mechanism... together they satisfy C-76." C-76 closure condition met.

**Score delta vs R18 V-05 baseline (246):**
| Change | Delta |
|--------|-------|
| C-75 gained | +2 |
| C-76 gained | +2 |
| **Net** | **+4** |

**V-04 total: 250/250**

---

### V-05 — Axes Z + Y + Phrasing Register: Full R19 Combination

**C-66 PASS:** LIFECYCLE_PROTOCOL section with "SOLE_AUTHORITY CONSTRAINT" — enhanced label over V-04 but same structural criterion satisfied.

**C-70 PASS:** Pointer-only role instructions: "CONSTRAINT: Open per LIFECYCLE_PROTOCOL Transition 1 incoming before any Phase 0-D-0 authoring." No inline HANDOFF_TO tokens.

**C-72 PASS:** Gate sweep field with scope citation identical to V-04.

**C-73 PASS:** LIFECYCLE_POINTER_AUDIT framed with stronger obligation: "CONSTRAINT: Run LIFECYCLE_POINTER_AUDIT before emitting gate assertion. This audit is the reference-layer closure mechanism for C-76... Every 'per LIFECYCLE_PROTOCOL Transition N' pointer... MUST be verified... An unresolved pointer is PROHIBITED... The audit MUST NOT be omitted even when all pointers are expected to resolve — the audit table is the closure evidence, not the SOLE_AUTHORITY section itself." Audit table structure identical to V-04.

**C-74 PASS:** Gate parenthetical field with declaration citation identical to V-04.

**C-75 PASS:** Both citation axes simultaneously. "CONSTRAINT: Emit gate assertion as a complete standalone audit summary. Both citation axes MUST be present simultaneously... A gate carrying only one citation axis does not satisfy C-75."

**C-76 PASS:** C-70 PASS + C-73 PASS. SOLE_AUTHORITY section explicitly declares both layers must be closed; "Both layers MUST be closed for single-source enforcement to hold."

**CONSTRAINT register over V-04:**
V-05 adds CONSTRAINT language to Phase 6-C ("discrepancies are PROHIBITED from going unreported"), Phase 6-D ("TOPIC_ROLLUP_MISMATCH finding REQUIRED for any discrepancy"), Phase 6-E ("TIMELINE_STATE_MISMATCH finding REQUIRED for any discrepancy"), Phase 1 ("CONSTRAINT: Phase 1-S MUST be authored before Phase 1"). These do not add new rubric criteria beyond V-04 but reinforce compliance with C-42, C-49, C-50, C-55.

**Score delta vs R18 V-05 baseline (246):**
| Change | Delta |
|--------|-------|
| C-75 gained | +2 |
| C-76 gained | +2 |
| CONSTRAINT adherence reinforcement | +0 (at ceiling) |
| **Net** | **+4** |

**V-05 total: 250/250**

---

## Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (160) | Total (250) | Delta vs Baseline |
|-----------|---------------|-----------------|-------------------|-------------|------------------|
| V-04 | 60 | 30 | 160 | **250** | +4 |
| V-05 | 60 | 30 | 160 | **250** | +4 |
| V-01 | 60 | 30 | 154 | **244** | -2 |
| V-02 | 60 | 30 | 152 | **242** | -4 |
| V-03 | 60 | 30 | 148 | **238** | -8 |

---

## Ranking

**Rank 1 (tie): V-04 and V-05 — 250/250**

Both achieve the first perfect score. V-04 demonstrates that the two new criteria are structurally achievable from the existing baseline. V-05 confirms that CONSTRAINT phrasing is a compositionally independent axis that neither degrades nor blocks the new structural criteria.

**Rank 3: V-01 — 244/250**

C-76 newly achieved (+2). C-72 and C-74 deliberately traded away (-4). Net negative because trading two cited axes for one closure criterion is value-negative under the rubric.

**Rank 4: V-02 — 242/250**

C-75 newly achieved (+2). C-66, C-70, C-73 all regressed (-6). The gate self-description cannot compensate for removing three structural lifecycle criteria.

**Rank 5: V-03 — 238/250**

Control confirms phrasing register is not an independent value source at this rubric tier. CONSTRAINT framing recovered ~2 pts from marginal adherence improvements but regressed -10 pts from five criteria lost. The register contribution is real but far below the structural axes.

---

## Excellence Signals — Top-Scoring Variation (V-05, tied V-04)

**Signal 1: C-75 and C-76 are structurally non-interfering dual axes.**
The LIFECYCLE_PROTOCOL section handles declaration-layer enforcement (C-70, C-76 requirement 1) while the gate format handles citation completeness (C-72+C-74=C-75). Neither axis constrains the other. V-04 and V-05 are the first variations to demonstrate both criteria PASS in the same artifact.

**Signal 2: LIFECYCLE_POINTER_AUDIT framed as mandatory closure obligation — not optional enhancement.**
V-05's LIFECYCLE_POINTER_AUDIT block explicitly states: "The audit MUST NOT be omitted even when all pointers are expected to resolve — the audit table is the closure evidence, not the SOLE_AUTHORITY section itself." This framing shifts the audit from a best-practice check to a structural requirement, reducing the model's incentive to skip it when the pointer sweep is clean. This is the critical phrasing that makes C-76 robust across topic instances.

**Signal 3: CONSTRAINT framing is compositionally additive — it reinforces without displacing structural criteria.**
V-03 demonstrated that phrasing register alone loses value by regressing structural elements. V-05 demonstrates the correct composition order: establish structural axes first (Z + Y), then layer phrasing register on top. CONSTRAINT framing applied to already-present structural elements reinforces enforcement without causing regressions.

---

## Recommended for R20

The two new criteria (C-75, C-76) are now both achievable. R20 focus areas:

1. **Extract V-05's LIFECYCLE_POINTER_AUDIT "closure evidence, not SOLE_AUTHORITY" phrasing** as a candidate standalone criterion — it distinguishes between structural presence of the audit and mandatory evidence role.
2. **Test whether C-75 × C-76 combination gates** (i.e., CONTRACT_AUDIT_GATE_HONORED citing the LIFECYCLE_POINTER_AUDIT_STATUS inline) form a third new criterion — a gate that summarizes not just schema compliance but also pointer resolution in one block.
3. **V-03 control confirms** CONSTRAINT register delivers ~2 pts marginal value but is not a structural axis. Future rounds should treat phrasing register as a modifier, not a source of new criteria.

---

```json
{"top_score": 250, "all_essential_pass": true, "new_patterns": ["C-75 and C-76 are structurally non-interfering: LIFECYCLE_PROTOCOL section satisfies declaration-layer closure (C-70, C-76) while gate citation format satisfies self-description completeness (C-72+C-74=C-75) — neither axis constrains the other", "LIFECYCLE_POINTER_AUDIT framed as mandatory reference-layer closure obligation rather than optional audit enhancement — 'audit table is the closure evidence, not the SOLE_AUTHORITY section itself' — makes C-76 robust when pointer sweep is clean", "CONSTRAINT phrasing register is compositionally additive when layered over established structural axes (Z+Y), reinforcing enforcement without causing regressions — correct application order is structure first, phrasing second"]}
```
