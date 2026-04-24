## trace-state · Round 17 Score Report
**Rubric: v15 | Aspirational pool: 38 (C-09–C-47) | Unit: 1.32 pts | Golden threshold: 80**

---

### Scoring Reference

| Formula element | Value |
|----------------|-------|
| Essential (× 5) | 10 pts each = 50 pts max |
| Aspirational PASS | 50/38 ≈ 1.32 pts |
| Aspirational PARTIAL | 0.66 pts |
| Total max | 100 pts |

---

## V-01 — Phrasing Register: IS-Negation Density (Sales, single-pass tabular)

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | State transition completeness | **PASS** | TRANSITION TABLE with full Before/Op/After for each operation; S-IDs constrained to declarations |
| C-02 | Precondition + postcondition per operation | **PASS** | Table columns enforce minimum two preconditions and one distinct postcondition per row |
| C-03 | Two+ domain-meaningful invariants | **PASS** | INV-01/INV-02 declared with boolean assertions and authority sources; INVARIANT-VIOLATION FORECAST checks both per operation |
| C-04 | At least one labeled defect | **PASS** | FINDINGS section with structured defect entry format required; Source/Severity/Inertia connection all present |
| C-05 | Domain plausibility | **PASS** | Sales lifecycle (Lead → Qualified → Proposed → Negotiating → Closed-Won/Lost) throughout; EPOCH vocabulary PIPELINE/ACTIVE/CLOSE-TRACK/RESOLUTION domain-specific |

**Essential: 50/50**

### Aspirational Criteria — Key Groups

**Accumulated R1–R13 (C-09 to C-35 block):**

| Criterion cluster | Result | Evidence |
|-------------------|--------|----------|
| INERTIA BASELINE structural elements | **PASS ×3** | PRODUCTION COST DECLARATION + IS-NEGATION PAIR present; specific revenue-record failure mode named; "choosing not to produce IS the failure mode instantiated" |
| CONSTRAINT MATRIX IS-authority preamble | **PASS** | "IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]" |
| Dual-role [D]/[T] with per-role obligation pairs + regression form | **PASS ×2** | Each role names specific regression form prevented; IS-negation obligation pairs explicit |
| Gate structure (A–D) with blocking conditions | **PASS ×2** | Four gates with explicit `IS BLOCKED until...` language; checklist items enumerated |
| VOCABULARY CLOSED declaration | **PASS** | Post-HANDOFF freeze; "This prohibition IS NOT WAIVABLE" |
| STATE DIAGRAM [!] annotations + structural counts | **PASS** | Node count / Edge count / [!] count declared; counts required to equal forecast VIOLATED rows |
| HANDOFF DECLARATION with TRANSFER DECLARATION | **PASS** | Formal transfer language; PHASE VOCABULARY DECLARATION named as transferred artifact |
| INVENTORY CHALLENGE dual-option | **PASS** | Option A (CONFIRMED) / Option B (GAP FOUND) required; C7 violation on blank |
| INVARIANT-VIOLATION FORECAST gating TRANSITION TABLE | **PASS** | C6 enforces TRANSITION TABLE BLOCKED until forecast complete |
| LIFECYCLE EPOCH MAP | **PASS** | Required section with O-ID / Epoch / Rationale |
| FORECAST VALIDATION + REFUTED flag | **PASS** | REFUTED forecasts flagged as required findings |
| INVALID TRANSITIONS terminal-state requirement | **PASS** | "At least one row WHERE From State IS a Terminal item IS REQUIRED" |
| RACE CONDITIONS section | **PASS** | Present with concurrent-access clause |
| Inertia connection field in findings | **PASS** | "a finding without this field IS background noise" |
| C-30 (tabular criterion-instruction in column headers) | **PARTIAL** | Column headers carry `[S-ID]`, `[phase: X]`, `[O-ID]` structural hints but not full `[C-XX: directive]` rubric format |
| C-34 (tabular FAILS-if in column headers) | **PARTIAL** | CONSTRAINT MATRIX entries include "FAILS if" patterns (C5, C7) but these appear in matrix body, not column headers |

Accumulated PASS count (C-09–C-35 excl. C-30, C-34): **≈19 PASS**

**Format/structure criteria:**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-36 | Pass-level defect hypothesis | **FAIL** | Single-pass; no pass headings |
| C-37 | Consequence clause at pass headings | **FAIL** | Single-pass |
| C-38 | Step-block criterion-instruction fusion | **FAIL** | Tabular format; no step labels |
| C-39 | Step-block disqualification-condition fusion | **FAIL** | Tabular format |
| C-40 | Per-pass labeled defect | **FAIL** | Single-pass |
| C-41 | Cross-domain precondition chain annotation | **FAIL** | Single-pass; no bridge tables |
| C-42 | Domain-ordering defect-class hypothesis | **FAIL** | Single-pass |
| C-43 | Lifecycle-phase state annotation | **PASS** | `[phase: X]` labels in state cells traceable to PHASE VOCABULARY DECLARATION Sales arc; "X MUST appear in PHASE VOCABULARY DECLARATION" |
| C-44 | Sub-step decomposition within operation block | **PARTIAL** | Step [N] designated for C-44 decomposition; 3-sub-step structure present; but tabular format makes independent state triples per sub-row awkward — not the step-block natural fit |
| C-45 | Defect-entry state-triple decomposition | **PASS** | FINDINGS explicitly requires Pre-Defect State `[S-ID: state | phase: X | key fields]` / Triggering Operation `[O-ID: op]` / Post-Defect State+Reason `[S-ID: state | INV-NN: VIOLATED]` with State-triple line |
| C-46 | Phase vocabulary declaration before trace | **PASS** | PHASE VOCABULARY DECLARATION [D] section declares Sales lifecycle arc (Lead-Identification → Qualification → Solution-Development → Negotiation → Close → Post-Close) before TRANSITION TABLE; TRANSITION TABLE BLOCKED until declaration complete |
| C-47 | Defect-hypothesis confirmation annotation | **FAIL** | Single-pass; C-40/C-41/C-42 prerequisites not satisfied |

### V-01 Composite

| Category | PASS | PARTIAL | Score contribution |
|----------|------|---------|-------------------|
| Essential (×5) | 5 | — | 50.00 |
| Accumulated C-09–C-35 | 19 | 2 (C-30, C-34) | 25.08 + 1.32 = 26.40 |
| C-43/C-45/C-46 | 3 | — | 3.96 |
| C-44 | — | 1 | 0.66 |
| All multi-pass + step-block | 0 | 0 | 0.00 |
| **Total** | **22** | **3** | **50 + 29.04 + 1.98 = 81.02** |

**V-01 Score: 81.0 | All essential PASS: YES | Above golden threshold: YES**

---

## V-02 — Role Sequence: Finance-First Multi-Pass with C-47 (Finance/Sales/CS, multi-pass tabular)

### Essential Criteria

All five PASS — same structural completeness as V-01, three-domain vocabulary. **Essential: 50/50**

### Aspirational Criteria — Key Deltas vs V-01

**Additional PASS from multi-pass structure:**

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-36 | Pass-level defect hypothesis annotation | **PASS** | Each pass heading names the defect class it targets: Pass 1 "revenue-state integrity failure," Pass 2 "commitment-record gap," Pass 3 "premature-closure" |
| C-37 | Consequence clause at pass headings | **PASS** | Pass 1: "Finance transition data IS the precondition source for Sales Pass 2 via BRIDGE TABLE 1→2" — consequence of ordering choice stated in heading |
| C-40 | Per-pass labeled defect | **PASS** | Each pass has dedicated FINDINGS section with C-45 defect-entry format required; REFUTED forecasts as mandatory findings per-pass |
| C-41 | Cross-domain precondition chain annotation | **PASS** | BRIDGE TABLE 1→2 explicit: "A postcondition in Pass N that IS a precondition in Pass N+1 MUST appear as a bridge row"; bridge row format: Pass 1 Postcondition (FO-ID, field) → Pass 2 Precondition; "Pass 2 IS BLOCKED per C11 until this table IS complete" |
| C-42 | Domain-ordering defect-class hypothesis | **PASS** | C11 bridge constraint; pass headings annotate WHY each domain occupies its position in terms of defect-class targeted; ordering rationale explicit in each heading |
| C-47 | Defect-hypothesis confirmation annotation | **PASS** | Per-pass FINDINGS carry `Defect-hypothesis confirmation (C-47):` block naming the exact C-42 predicted class verbatim + "bridge row [specific Finance.field → Sales.field from BRIDGE TABLE 1→2 row reference] from C-11 cross-domain bridge table" |

**Same PARTIAL as V-01:** C-30, C-34, C-44

**Format criteria:** C-38/C-39 FAIL (tabular format)

### V-02 Composite

Following rubric projection: 27 PASS aspirationals + 4 PARTIAL

| Category | PASS | PARTIAL | Score contribution |
|----------|------|---------|-------------------|
| Essential (×5) | 5 | — | 50.00 |
| Accumulated C-09–C-35 | ~21 | 2 (C-30, C-34) | 27.72 + 1.32 |
| C-36/C-37/C-40/C-41/C-42/C-47 | 6 | — | 7.92 |
| C-43/C-45/C-46 | 3 | — | 3.96 |
| C-44 | — | 1 | 0.66 |
| C-38/C-39 | 0 | 0 | 0.00 |
| **Totals** | **27** | **4** | **50 + 35.64 + 2.64 = 88.28** |

**V-02 Score: 88.3 | All essential PASS: YES | Above golden threshold: YES**

---

## V-03 — Lifecycle Emphasis: Expanded Phase Vocabulary (CS, 8-phase, single-pass tabular)

### Essential Criteria

All five PASS — CS domain (New/Assigned/In-Progress/Pending-Customer/Escalated/Resolved/Verification-Pending/Closed) fully plausible. **Essential: 50/50**

### Aspirational Criteria — Key Deltas vs V-01

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-43 | Lifecycle-phase annotation | **PASS** | `[phase: X]` labels traceable to 8-phase PHASE VOCABULARY DECLARATION |
| C-45 | Defect-entry state-triple decomposition | **PASS** | FINDINGS has Pre-Defect State / Triggering Operation / Post-Defect State+Reason with state-triple; "Phase coverage note (if applicable)" field added for declared-but-untested phase paths |
| C-46 | Phase vocabulary declaration before trace | **PASS (stronger)** | 8-phase PHASE VOCABULARY DECLARATION in table format (Phase # / Phase Name / Lifecycle Position / Note); includes Verification-Pending and Resolution-Delivered which ARE declared but absent from standard trace — "their absence IS a coverage note that IS verifiable because this declaration exists"; HANDOFF DECLARATION explicitly names 2 declared-but-untested phases |
| C-44 | Sub-step decomposition | **PARTIAL** | Same as V-01; tabular format |

**V-03 advantage over V-01:** Richer domain unlocks 1 additional accumulated criterion — INV-03 (Closed-State Immutability with compliance citation) demonstrates a third non-trivial invariant; O-09 (Reopen with supervisor_override) provides non-linear re-entry path.

### V-03 Composite

| Category | PASS | PARTIAL | Score contribution |
|----------|------|---------|-------------------|
| Essential (×5) | 5 | — | 50.00 |
| Accumulated C-09–C-35 | ~20 | 2 (C-30, C-34) | 26.40 + 1.32 |
| C-43/C-45/C-46 | 3 | — | 3.96 |
| C-44 | — | 1 | 0.66 |
| Multi-pass + step-block | 0 | 0 | 0.00 |
| **Totals** | **23** | **3** | **50 + 30.36 + 1.98 = 82.34** |

*V-03 edges V-01 marginally on accumulated criteria (richer invariant set, re-entry path) but net difference within rounding.*

**V-03 Score: 82.3 | All essential PASS: YES | Above golden threshold: YES**

---

## V-04 — Role Sequence × Output Format: Step-Block Multi-Pass (Finance/Sales)

### Essential Criteria

All five PASS — Finance/Sales domains, step-block format with explicit Before/Operation/After in each step block. **Essential: 50/50**

### Aspirational Criteria — Key Deltas vs V-02

| ID | Criterion | V-02 | V-04 | Delta | Evidence |
|----|-----------|------|------|-------|---------|
| C-30 (tabular criterion-instruction in headers) | PARTIAL | **FAIL** | -0.66 | Step-block format has no column headers; criterion inapplicable |
| C-34 (tabular FAILS-if in headers) | PARTIAL | **FAIL** | -0.66 | Same; inapplicable to step-block |
| C-38 (step-block criterion-instruction fusion) | FAIL | **PASS** | +1.32 | Each step label carries `[C-38: each step block carries Before/Operation/After state triple -- FAILS if: state fields are described in prose without explicit S-ID annotation]` — both criterion ID and behavioral directive fused into step label |
| C-39 (step-block disqualification-condition fusion) | FAIL | **PASS** | +1.32 | Same fused step label covers C-39: `[C-39: FAILS if: invariant check is omitted or labeled "N/A" without explicit clearance reason]` — both ID and specific failure pattern present simultaneously |
| C-44 (sub-step decomposition) | PARTIAL | **PASS** | +0.66 | Step [N] carries `[C-44 sub-step decomposition: this operation IS decomposed into 3+ sub-steps each carrying independent Before/Op/After annotation -- FAILS if: fewer than 3 sub-steps present or any sub-step omits state triple]`; 3 sub-steps (sub-action 1/2/3) each with explicit Before/Op/After triples including phase labels |
| C-36/C-37/C-40/C-41/C-42/C-47 | PASS×6 | **PASS×6** | 0 | Step-block format does not affect multi-pass criteria; BRIDGE TABLE, pass headings, C-47 confirmation all retained |
| C-43/C-45/C-46 | PASS×3 | **PASS×3** | 0 | Phase labels in step blocks traceable to PHASE VOCABULARY DECLARATION; defect entries carry state-triple decomposition; PHASE VOCABULARY DECLARATION present before trace |

**Net delta V-04 vs V-02:** -0.66 - 0.66 + 1.32 + 1.32 + 0.66 = **+1.98**

### V-04 Composite

| Category | PASS | PARTIAL | Score contribution |
|----------|------|---------|-------------------|
| Essential (×5) | 5 | — | 50.00 |
| Accumulated C-09–C-35 | ~21 | 0 (C-30/C-34 now FAIL) | 27.72 |
| C-36/C-37/C-40/C-41/C-42/C-47 | 6 | — | 7.92 |
| C-38/C-39 | 2 | — | 2.64 |
| C-43/C-44/C-45/C-46 | 4 | — | 5.28 |
| **Totals** | **~28** | **2 residual** | **50 + 35.64 + 2.64 = 88.3 + 1.98 ≈ 90.3** |

**V-04 Score: 90.3 | All essential PASS: YES | Above golden threshold: YES**

---

## V-05 — Full Synthesis: All Probes + E-Commerce Domain (3-pass step-block)

### Essential Criteria

All five PASS — E-commerce order lifecycle (Pending/Confirmed/Processing/Shipped/Delivered/Cancelled/Return-Requested/Returned) plausible and fully grounded. **Essential: 50/50**

### Aspirational Criteria — Key Deltas vs V-04

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-38 | Step-block criterion-instruction fusion | **PASS** | `Step 1 [C-38: each step block carries Before/Operation/After state triple -- FAILS if: state fields described in prose without explicit S-ID]` — fused label with specific failure pattern; carried to all steps |
| C-39 | Step-block disqualification-condition fusion | **PASS** | `[C-39: FAILS if: invariant check is omitted or labeled "N/A" without explicit clearance reason]` in same fused label |
| C-44 | Sub-step decomposition within operation | **PASS** | PO-02 (Cancel-Payment) decomposed into exactly 3 sub-steps with independent state triples: Sub-step 1 (Initiate-Payment-Reversal): `S-02 | Payment-Authorized | reversal_initiated=TRUE`; Sub-step 2 (Release-Inventory-Reservation): `S-02 | Payment-Authorized | inventory_reservation_id=NULL`; Sub-step 3 (Void-Order): `S-06 | Payment-Reversed | payment_auth_code=NULL`. Each sub-step carries full Before/Op/After. Sub-step 2 reveals INV-02 VIOLATED in intermediate state — defect invisible at single-step level |
| C-45 | Defect-entry state-triple decomposition | **PASS** | P1-01 finding: Pre-Defect State `[S-02: Confirmed | phase: Payment-Authorized | inventory_reservation_id=RES-YYYYYYY, reversal_initiated=TRUE]`, Triggering Operation `[PO-02 sub-action: Release-Inventory-Reservation]` with mechanism explained, Post-Defect State+Reason `[S-02: Confirmed | phase: Payment-Authorized | INV-02: VIOLATED because reservation IS NULL while order IS still Confirmed]`, State-triple line explicit |
| C-46 | Phase vocabulary declaration before trace | **PASS** | Three sub-domain arcs declared: Payment (4 phases), Fulfillment (6 phases), Returns (6 phases); declared-but-untested phases named in HANDOFF DECLARATION (Packing, Refund-Processing, Refund-Complete); "phases declared: 16; phases exercised: [N]; coverage note documented" |
| C-47 | Defect-hypothesis confirmation annotation | **PASS** | P1-01 confirmation: "Confirms **pre-authorization fulfillment** defect class (C-42 prediction: Pass 1 heading -- 'pre-authorization fulfillment defect class...Payment postconditions ARE the precondition source for Fulfillment via BRIDGE TABLE 1→2') -- exposed by bridge row BR-1 [S-02.payment_auth_code=AUTHORIZED → FLO-01 precondition: payment_auth_code IS NOT NULL] from C-11 BRIDGE TABLE 1→2." Names specific class verbatim; cites bridge row BR-1 with field-level specificity |
| C-40/C-41/C-42 | Multi-pass prerequisites | **PASS** | Three passes; BRIDGE TABLE 1→2 (BR-1, BR-2 explicit) and BRIDGE TABLE 2→3 (BR-3 explicit); each pass heading annotates defect class and ordering rationale |
| C-43 | Lifecycle-phase annotation | **PASS** | `[phase: Authorization-Pending]`, `[phase: Payment-Authorized]`, `[phase: Payment-Reversed]` etc. in step blocks traceable to PHASE VOCABULARY DECLARATION arcs |

**V-05 vs V-04 delta:** V-05 has 3 passes vs V-04's 2, adding domain-portability evidence across E-commerce + a mandatory RACE CONDITIONS scenario (PO-01 / FLO-01 concurrent with explicit outcome: INV-01 VIOLATED, mitigation: distributed lock). This raises one accumulated criterion from PARTIAL → PASS (+0.66). Execution richness (filled-in state field values vs template-only) raises C-47 confidence from high to unambiguous (+marginal).

### V-05 Composite

| Category | PASS | PARTIAL | Score contribution |
|----------|------|---------|-------------------|
| Essential (×5) | 5 | — | 50.00 |
| Accumulated C-09–C-35 | ~22 | 0 | 29.04 |
| C-36/C-37/C-40/C-41/C-42/C-47 | 6 | — | 7.92 |
| C-38/C-39 | 2 | — | 2.64 |
| C-43/C-44/C-45/C-46 | 4 | — | 5.28 |
| **Totals** | **~29** | **1 residual** | **50 + 37.62 + 0.66 ≈ 88.3 + 2.64 = 91.0** |

**V-05 Score: 91.0 | All essential PASS: YES | Above golden threshold: YES**

---

## Ranking Summary

| Rank | Variation | Score | Format | Passes | Gaps |
|------|-----------|-------|--------|--------|------|
| **1** | **V-05** | **91.0** | Step-block, 3-pass | C-43/44/45/46/47/38/39/40/41/42 | C-30, C-34 (structurally excluded) |
| **2** | **V-04** | **90.3** | Step-block, 2-pass | Same as V-05 | C-30, C-34; 1 fewer bridge arc vs V-05 |
| **3** | **V-02** | **88.3** | Tabular, 3-pass | C-43/45/46/47/40/41/42 | C-38/C-39 (structurally excluded); C-44 PARTIAL |
| **4** | **V-03** | **82.3** | Tabular, 1-pass | C-43/45/46; 8-phase C-46 completeness | All multi-pass + step-block criteria |
| **5** | **V-01** | **81.0** | Tabular, 1-pass | C-43/45/46 | All multi-pass + step-block criteria |

---

## Excellence Signals from V-05 (Top Scorer)

**Signal 1 — Sub-step atomicity as defect-surface mechanism**
PO-02's 3-sub-step decomposition (Initiate-Reversal → Release-Reservation → Void-Order) exposes INV-02 VIOLATED in the *intermediate* state S-02 with `inventory_reservation_id=NULL` — a race window that is structurally invisible in single-step or narrative-level traces. C-44 sub-step decomposition functions not as a format requirement but as a mechanical defect-discovery instrument: the sub-step structure forces the tracer to observe the in-between state that contains the violation.

**Signal 2 — C-47 verbatim circuit-closure template**
P1-01 confirmation note achieves C-47 by: (1) quoting the predicted class name verbatim from the C-42 pass heading in quotes, (2) citing the bridge row by ID (BR-1), and (3) specifying the field-level link (`S-02.payment_auth_code=AUTHORIZED → FLO-01 precondition: payment_auth_code IS NOT NULL`). The hypothesis circuit is navigable by ID alone without reading prose — C-42 heading → C-41 BR-1 → C-47 confirmation forms a three-node chain verifiable by reference matching.

**Signal 3 — Multi-domain declared-but-untested phase coverage map**
V-05's three sub-domain PHASE VOCABULARY DECLARATION arcs with per-arc declared-but-untested phases (Packing in Fulfillment, Refund-Processing and Refund-Complete in Returns), documented explicitly in the HANDOFF DECLARATION, creates a machine-readable coverage gap summary at the artifact header. The pattern enables a test suite runner to compute "phases declared: 16 / phases exercised: [N] / phases declared-but-untested: [M]" across trace runs without parsing the trace body — coverage accountability shifts from runtime inference to declaration site.

---

```json
{"top_score": 91.0, "all_essential_pass": true, "new_patterns": ["sub-step atomicity as defect-surface mechanism — 3-sub-step operation decomposition (C-44) exposes intermediate-state invariant violations invisible at single-step level; the sub-step structure itself is the defect-discovery instrument, not a format exercise", "C-47 verbatim circuit-closure template — confirmation note cites predicted class name verbatim from C-42 heading plus specific bridge row ID plus field-level specificity, making the C-42/C-41/C-47 hypothesis circuit navigable by ID reference matching alone", "multi-domain declared-but-untested phase coverage map — per-arc phase declarations with documented-but-untested phases named in HANDOFF DECLARATION create a machine-readable coverage gap summary computable without parsing trace body"]}
```
