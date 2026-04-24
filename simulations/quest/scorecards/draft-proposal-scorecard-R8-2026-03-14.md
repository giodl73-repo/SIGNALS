## draft-proposal — Round 8 Scorecard

**Rubric**: v8 | **Criteria**: C-01–C-31 (31 total) | **Denominator**: /24 | **Date**: 2026-03-14

---

### Summary

| Var | Axis | C-28 | C-29 | C-30 | C-31 | Score |
|-----|------|------|------|------|------|-------|
| V-01 | PM-first throughout | PASS | FAIL | FAIL | FAIL | 98.75 |
| V-02 | Canonical headers at Phase 0 | FAIL | PASS | FAIL | FAIL | 98.75 |
| V-03 | Phase manifest at Phase 0 | FAIL | FAIL | PASS | FAIL | 98.75 |
| **V-04** | **PM-first + table-dominant** | **PASS** | **PASS** | FAIL | FAIL | **99.17** |
| **V-05** | **Lifecycle-heavy + inertia-forward** | FAIL | FAIL | **PASS** | **PASS** | **99.17** |

---

### Key findings

**Ceiling is 99.17, not 100.0.** All five predictions (100.0) were wrong. The four new criteria decompose into two orthogonal axes:
- **C-28/C-29** — role-ordering + format mechanisms (V-04)
- **C-30/C-31** — lifecycle-manifest + computation mechanisms (V-05)

No single-axis variation covers both pairs. V-04 and V-05 are co-ceiling at 99.17. A V-06 combining all four axes would reach 100.0 and is the motivated R9 variation.

**Axis independence confirmed independently for each new criterion:**
- C-28 ≠ C-06/C-21 — ordering orthogonal to dual-role content or slot independence
- C-29 ≠ C-16/C-19 — format constraint orthogonal to numeric P\*I content or label correctness
- C-30 ≠ C-17 — manifest verifiability upgrade orthogonal to correct register ordering
- C-31 ≠ C-27 — DECISION LEAD TIME computation orthogonal to INERTIA OFFSET naming

---

### Excellence Signals

**V-04 — Field-level role enforcement:** `PM FRAMING:` and `ARCHITECT VALIDATION:` as typed slots within the option anatomy template, not only phase-level instructions. Role sequence verifiable at option level — three independent enforcement points (option generation, authoring, sign-off).

**V-05 — Cross-phase causal contract at Phase 0:** `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME` declared as a Phase 0 initialization contract before Phase 2 or Phase 4 execute. Missing chain links route to T-GUARD at initialization rather than at Phase 12 sign-off. Generalizes to any multi-phase computation with a named output field.

---

```json
{"top_score": 99.17, "all_essential_pass": true, "new_patterns": ["cross-phase causal contract at Phase 0: declaring TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME as a typed Phase 0 initialization contract before phase 2 or phase 4 execute converts retroactive chain verification into prospective enforcement — any missing link routes to T-GUARD at initialization rather than at Phase 12 sign-off", "field-level role enforcement: PM FRAMING and ARCHITECT VALIDATION as typed slots within the option anatomy template — role sequence is verifiable at individual option level without phase scan, extending C-06 dual-role participation into C-28 PM-first ordering across three independent enforcement points (option generation, option authoring, sign-off)"]}
```
�� F-NN ID) | PASS | PASS | PASS | PASS | PASS |
| C-16 | Numeric P\*I risk scoring with project-specific anchors | PASS | PASS | PASS | PASS | PASS |
| C-17 | Registers-before-recommendation lifecycle ordering | PASS | PASS | PASS | PASS | PASS |
| C-18 | Front-loaded amendment table (prospective init, trigger rules) | PASS | PASS | PASS | PASS | PASS |
| C-19 | Canonical F-row field labels (FAILURE MODE / TRIGGER CONDITION / MITIGATION) | PASS | PASS | PASS | PASS | PASS |
| C-20 | PREREQUISITE GATE block before recommendation | PASS | PASS | PASS | PASS | PASS |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots (PM + Architect each) | PASS | PASS | PASS | PASS | PASS |
| C-22 | Named trigger IDs (T-NN) with TRIGGER back-reference in amendment rows | PASS | PASS | PASS | PASS | PASS |
| C-23 | T-GUARD sentinel defined with catch-all scope vocabulary | PASS | PASS | PASS | PASS | PASS |
| C-24 | Empty-table completion semantics (explicit T-GUARD enforcement statement) | PASS | PASS | PASS | PASS | PASS |
| C-25 | Sentinel-first trigger ordering (T-GUARD at position 1) | PASS | PASS | PASS | PASS | PASS |
| C-26 | COMPLETION STATUS as Phase 0 typed initialization slot (PENDING → terminal) | PASS | PASS | PASS | PASS | PASS |
| C-27 | INERTIA COST on do-nothing + INERTIA OFFSET per alternative + GATE item | PASS | PASS | PASS | PASS | PASS |
| **C-28** | **PM-first recommendation sign-off ordering** | **PASS** | **FAIL** | **FAIL** | **PASS** | **FAIL** |
| **C-29** | **Table-dominant register format (canonical column headers all 3 registers)** | **FAIL** | **PASS** | **FAIL** | **PASS** | **FAIL** |
| **C-30** | **Phase manifest at Phase 0 initialization** | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** |
| **C-31** | **INERTIA OFFSET vs. TEMPORAL ANCHOR decision lead time** | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |

---

### C-28 Discriminator Detail

**V-01 PASS evidence:** V-01's core axis is PM-first positioning. T-19 fires when the Architect sign-off block occupies position 1 in the recommendation phase sign-off section. The trigger is position-detection only — no content scan required. The PM sign-off block is structurally forced to precede the Architect block by the trigger definition, not merely by prose instruction. C-28 independently verifiable: a reviewer reads the first signatory block header in Phase 12 (or equivalent recommendation phase) and confirms or falsifies without scanning further.

**V-04 PASS evidence:** V-04 combines PM-first with table-dominant. PM-first is enforced at the option anatomy level — every option template includes `PM FRAMING:` as the first typed field and `ARCHITECT VALIDATION:` as the second, establishing role sequence below the phase level. The sign-off section inherits this ordering. T-19 fires on position 1 in sign-off.

**V-02 FAIL evidence:** V-02's axis is canonical register headers at Phase 0. Sign-off block ordering is not addressed. The recommendation phase has a PM block and an Architect block, but their sequence is determined by template default (which may place Architect first). No T-NN fires on position 1 in sign-off. C-28 requires structural enforcement of ordering, not incidental ordering; V-02 provides neither a trigger nor an explicit first-position requirement.

**V-03 FAIL evidence:** V-03's axis is phase manifest and lifecycle ordering. The phase manifest names all phases but does not specify PM-first within Phase 12. The LIFECYCLE ORDERING VERIFICATION confirms register phases appear before recommendation phases but does not constrain the internal ordering within the recommendation phase. C-28 fails for the same reason as V-02: no structural mechanism locks PM to position 1.

**V-05 FAIL evidence:** V-05's INERTIA-CHAIN CONTRACT and phase manifest are depth and lifecycle mechanisms with no effect on sign-off block ordering. The same failure mode as V-02/V-03 applies.

---

### C-29 Discriminator Detail

**V-02 PASS evidence:** V-02 declares three format contracts at Phase 0 initialization before any register is authored:
- Assumption register: `| A-NN | ASSUMPTION | VALIDATION PLAN |`
- Risk register: `| R-NN | RISK | P | I | P*I | MITIGATION |`
- Failure mode register: `| F-NN | FAILURE MODE | TRIGGER CONDITION | MITIGATION |`

T-14, T-15, and T-16 are scoped to Phase 0: if any register is subsequently authored in prose format, the corresponding trigger fires immediately and an amendment row is generated. The format contracts are initialization artifacts, not per-phase instructions.

**V-04 PASS evidence:** V-04 carries V-02's format contract mechanism (table-dominant axis). Additionally, the canonical headers are embedded in the option anatomy template — the comparison matrix (Phase 6) uses typed column headers matching the canonical vocabulary. Format discipline is enforced from option generation through register authoring.

**V-01 FAIL evidence:** V-01's PM-first axis does not include format contracts. Register format is not explicitly constrained — a model may produce prose-formatted registers with embedded field labels (e.g., "P: 3, I: 4, P\*I: 12") that satisfy C-16 content requirements while failing C-29 format requirements. No T-NN fires on prose register format. C-29 requires structural enforcement; incidental table use does not satisfy the criterion.

**V-03 FAIL evidence:** V-03's phase manifest lists all phases but does not declare register format contracts at Phase 0. The LIFECYCLE ORDERING VERIFICATION confirms ordering (C-17/C-30) but makes no claims about column header format. Same failure mode as V-01.

**V-05 FAIL evidence:** Same as V-01/V-03. Lifecycle and inertia mechanisms impose no format constraints on register column headers.

---

### C-30 Discriminator Detail

**V-03 PASS evidence:** V-03 initializes a PHASE MANIFEST block in Phase 0 listing all phases by number and name (e.g., Phase 0: Front-Loaded Amendment Tracking, Phase 1: Scout Inventory, ..., Phase 15: Completion). The LIFECYCLE ORDERING VERIFICATION section within the manifest explicitly names the Phase 8/9/10 < Phase 12 constraint for register-before-recommendation ordering. C-17 compliance becomes a single-block read: a reviewer confirms Phase 8/9/10 appear before Phase 12 in the manifest without scanning the document. T-01 and T-02 fire when the manifest is structurally absent or when phase ordering in the manifest violates the verification constraint.

**V-05 PASS evidence:** V-05's lifecycle-heavy axis combines phase manifest (C-30) with inertia-chain contract. The phase manifest is initialized at Phase 0 as in V-03. The INERTIA-CHAIN CONTRACT at Phase 0 adds a cross-phase dependency annotation to the manifest: Phase 2 (TEMPORAL ANCHOR) and Phase 3 (INERTIA COST anchors) are named as inputs to Phase 4 (DECISION LEAD TIME computation), creating a causal chain declared before any of those phases execute.

**V-01/V-02 FAIL evidence:** Neither PM-first positioning nor canonical register headers require a phase manifest block. C-17 (register-before-recommendation ordering) is satisfied by correct document sequence, but verification still requires a document scan to confirm register phases appear before Phase 12. V-01 and V-02 pass C-17 on content but fail C-30 on verifiability: no phase manifest converts the ordering check into a single-block audit.

**V-04 FAIL evidence:** V-04 combines PM-first and table-dominant axes — both format/role mechanisms. Phase manifest is a lifecycle mechanism outside V-04's axis. C-17 is verified by register sequence (passes) but no PHASE MANIFEST block exists for single-block auditing. V-04 fails C-30 independently of its C-28/C-29 compliance.

---

### C-31 Discriminator Detail

**V-05 PASS evidence:** V-05 declares an INERTIA-CHAIN CONTRACT at Phase 0 with the typed computation:

```
TEMPORAL ANCHOR (Phase 2) − INERTIA OFFSET (Phase 4) = DECISION LEAD TIME per alternative
ESCALATION FLAG: required when DECISION LEAD TIME ≤ 0
```

Each non-do-nothing alternative carries a DECISION LEAD TIME typed slot (not a prose note) in its option anatomy. When TEMPORAL ANCHOR minus INERTIA OFFSET yields a non-positive value, an ESCALATION FLAG typed slot fires with the canonical value "DECISION WINDOW CLOSED — ESCALATE IMMEDIATELY." The PREREQUISITE GATE block (C-20) is extended with a third binary item:
- `DECISION LEAD TIME typed per alternative: complete / not complete`

The contract is defined before Phase 2 executes — the computation constraint is active from Phase 0 initialization. T-08 through T-11 are labeled "inertia-chain break" failures and fire when any link in the chain (TEMPORAL ANCHOR, INERTIA OFFSET, subtraction result, ESCALATION FLAG) is absent or non-typed.

**V-01/V-02/V-03/V-04 FAIL evidence:** C-27 (INERTIA COST on do-nothing + INERTIA OFFSET per alternative + GATE item) passes in all four variations — the per-sprint cost curve and crossover point are present. C-31 requires the additional step of computing and typing DECISION LEAD TIME = TEMPORAL ANCHOR − INERTIA OFFSET and adding ESCALATION FLAG when the result is non-positive. This is not incidentally produced by C-27 compliance: a variation can carry INERTIA COST and INERTIA OFFSET without computing their difference against TEMPORAL ANCHOR. None of V-01 through V-04 include the DECISION LEAD TIME typed slot, the subtraction requirement, the ESCALATION FLAG condition, or the PREREQUISITE GATE extension for lead-time completeness. All four fail C-31 independently.

---

## Score Computation

| Variation | Essential (×60) | Recommended (×30) | Aspirational (/24 × 10) | **Composite** |
|-----------|-----------------|-------------------|--------------------------|---------------|
| V-01 | 4/4 = 60.00 | 3/3 = 30.00 | 21/24 = 8.75 | **98.75** |
| V-02 | 4/4 = 60.00 | 3/3 = 30.00 | 21/24 = 8.75 | **98.75** |
| V-03 | 4/4 = 60.00 | 3/3 = 30.00 | 21/24 = 8.75 | **98.75** |
| V-04 | 4/4 = 60.00 | 3/3 = 30.00 | 22/24 = 9.17 | **99.17** |
| V-05 | 4/4 = 60.00 | 3/3 = 30.00 | 22/24 = 9.17 | **99.17** |

*Each aspirational criterion: 10/24 ≈ 0.417 pts. Three fails = −1.25. Two fails = −0.83.*

---

## Ranking

1. **V-04** — 99.17 (PM-first + table-dominant; passes C-28, C-29; fails C-30, C-31)
1. **V-05** — 99.17 (lifecycle-heavy + inertia-forward; passes C-30, C-31; fails C-28, C-29)
3. **V-01** — 98.75 (passes C-28 only; fails C-29, C-30, C-31)
3. **V-02** — 98.75 (passes C-29 only; fails C-28, C-30, C-31)
3. **V-03** — 98.75 (passes C-30 only; fails C-28, C-29, C-31)

**V-04 and V-05 are the co-ceiling.** The ceiling is 99.17, not 100.0. The four new criteria decompose into two independent pairs (C-28/C-29 = role/format mechanisms; C-30/C-31 = lifecycle/depth mechanisms). No single-axis variation can cover both pairs. The R8 ceiling requires a variation that combines all four, analogous to R7 V-04/V-05 which combined C-25/C-26/C-27 under a unified axis.

**Predicted-vs-actual delta:** All five variations predicted at 100.0. Actual ceiling is 99.17. The prediction error arises from treating single-axis variations as covering all new criteria — PM-first does not incidentally enforce table-dominant format, and lifecycle-heavy does not incidentally enforce PM-first sign-off ordering. The four new criteria require four independent structural mechanisms across two orthogonal axes.

---

## Excellence Signals (from V-04/V-05)

Two structural patterns distinguish V-04/V-05 from V-01/V-02/V-03 at the criterion level. Both are independently verifiable without document-level scanning.

**1. Field-level role enforcement (V-04)**

PM FRAMING and ARCHITECT VALIDATION appear as typed slots within the option anatomy template itself — not only as phase-level dual-role instructions. Role sequence is verifiable at the option level: a reviewer reads the first typed field in any option block and confirms whether PM or Architect is named. This extends C-06 (dual-role participation, phase-level) into C-28 compliance (PM-first ordering, slot-level). The mechanism fires in Phase 4 option generation, Phase 5 option authoring, and Phase 12 recommendation sign-off — three independent enforcement points rather than one.

**2. Cross-phase causal contract at Phase 0 (V-05)**

The INERTIA-CHAIN CONTRACT declares the computation TEMPORAL ANCHOR (Phase 2) − INERTIA OFFSET (Phase 4) = DECISION LEAD TIME before either source phase executes. This converts a cross-phase dependency (typically verified retroactively by reading Phase 2 and Phase 4 in sequence) into a Phase 0 initialization constraint. The contract names the input phases, the output field, and the ESCALATION FLAG condition before any phase is authored. Unanticipated chain breaks (missing TEMPORAL ANCHOR, absent INERTIA OFFSET, uncomputed DECISION LEAD TIME) now route to T-GUARD at Phase 0 rather than being discovered at Phase 12 sign-off. The pattern generalizes: any multi-phase computation with a named output field can be contracted at Phase 0, converting retroactive verification into prospective enforcement.

---

## Round 8 Discriminator Notes

**C-28 axis independence from C-06/C-21:** C-06 requires PM and Architect to each contribute a named perspective (content criterion). C-21 requires each signatory to have an independent F-ROW ANCHOR slot (structure criterion). Neither specifies which signatory appears first. C-28 adds an ordering constraint orthogonal to content quality or slot independence. V-02/V-03/V-05 pass C-06 and C-21 while failing C-28 — the three criteria are independently falsifiable.

**C-29 axis independence from C-16/C-19:** C-16 requires numeric P\*I in the risk register (content criterion). C-19 requires canonical field labels in the failure mode register (label criterion). Neither constrains format (table vs. prose) for all three registers. C-29 adds a format constraint orthogonal to content or label correctness. V-01/V-03/V-05 pass C-16 and C-19 while failing C-29 — prose-format registers with correct numeric P\*I and canonical field labels satisfy C-16/C-19 and fail C-29.

**C-30 axis independence from C-17:** C-17 requires registers to appear before the recommendation in document sequence (ordering criterion). C-30 requires a phase manifest block in Phase 0 listing all phases so that C-17 verification becomes a single-block read rather than a document scan. V-01/V-02/V-04 pass C-17 while failing C-30 — correct register ordering does not imply a manifest exists. The manifest converts C-17 from a scan-dependent criterion to a single-block audit; C-30 is a verifiability upgrade, not a content change.

**C-31 axis independence from C-27:** C-27 requires INERTIA COST on the do-nothing option and INERTIA OFFSET (sprint crossover) on each alternative (content criterion). C-31 requires the subtraction TEMPORAL ANCHOR − INERTIA OFFSET to be computed and typed as DECISION LEAD TIME per alternative, with ESCALATION FLAG when non-positive (computation criterion). V-01/V-02/V-03/V-04 pass C-27 while failing C-31 — a variation can name the sprint crossover point (INERTIA OFFSET) without computing its difference against TEMPORAL ANCHOR. C-31 adds a computable output field and a conditional escalation slot; both are structurally absent unless explicitly targeted.

**Why the ceiling is 99.17 and not 100.0:** The four new criteria decompose into two independent mechanism axes. C-28/C-29 are role-ordering and format mechanisms. C-30/C-31 are lifecycle-manifest and computation mechanisms. A variation targeting one axis cannot satisfy the other without explicitly including the second axis's mechanisms. V-04 and V-05 each cover one axis. A V-06 combining all four axes would score 100.0 by satisfying all 24 aspirational criteria. The R8 ceiling is not a design failure — it confirms axis independence and motivates the R9 combination variation.

---

```json
{"top_score": 99.17, "all_essential_pass": true, "new_patterns": ["cross-phase causal contract at Phase 0: declaring TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME as a typed Phase 0 initialization contract before phase 2 or phase 4 execute converts retroactive chain verification into prospective enforcement — any missing link routes to T-GUARD at initialization rather than at Phase 12 sign-off", "field-level role enforcement: PM FRAMING and ARCHITECT VALIDATION as typed slots within the option anatomy template — role sequence is verifiable at individual option level without phase scan, extending C-06 dual-role participation into C-28 PM-first ordering across three independent enforcement points (option generation, option authoring, sign-off)"]}
```
