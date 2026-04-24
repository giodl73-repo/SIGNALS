# flow-dataflow — Round 13 Scoring Report

## Rubric Framework (v13)

| Tier | Criteria | Weight each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-04 | 15.00 pts | 60 |
| Recommended | C-05–C-07 | 10.00 pts | 30 |
| Aspirational | C-08–C-43 (36 total) | 0.278 pts | 10 |
| **Total** | | | **100** |

PARTIAL = 50% of criterion weight. The C-42/C-43 implementation pattern — SC-12 all-three-attributes block and REGISTER DECLARATION closed-chain header — is **identical across all five variations**. Differentiation is driven by output format (V-02), structural depth (V-03), explicit baseline ownership (V-04), and instruction voice (V-05).

---

## V-01 — Commerce → Finance → Operations | Tabular | Pharmaceutical Supply-Chain

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Vendor catalog → formulary validation → hospital dispensary lot; unbroken chain for all in-scope items (NDC, lot, dispense record) |
| C-02 | PASS | Each of three boundaries annotated: catalog-sync retry on 5xx; formulary lookup dead-letter on NDC mismatch; lot-write rollback on expiry |
| C-03 | PASS | Named loss point per stage: (1) vendor SKU unmapped to NDC, (2) formulary tier mismatch, (3) lot expiry at dispensing |
| C-04 | PASS | Schema state at each entry/exit: vendor SKU fields → internal NDC + formulary tier → dispensary lot + expiry — field-level diff present |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Catalog sync: daily batch; formulary lookup: real-time < 200 ms; dispensary write: async < 1 s |
| C-06 | PASS | Formulary stale window quantified (24 h); failure-mode staleness (overnight batch failure → 48 h) addressed separately |
| C-07 | PASS | NDC, formulary tier, lot number, dispense record appear throughout lineage chain |

### Aspirational — non-pass items only; all others PASS

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-15 | PARTIAL | Incumbent manual section present but C-08/C-09 cross-reference not explicitly enforced in variation spec; connection implied |
| C-27 | PARTIAL | Recovery formula present in output but not named as a distinct spec-level design feature; relies on runtime execution discipline |

All 34 remaining aspirational criteria PASS: C-42/C-43 pattern present, [A-xx] registry, REGISTER DECLARATION Parts A/B, interleaved boundaries, binary verdicts, phase gate checklists, SC callback syntax, skip-level SC-12 with all three attributes, closed-chain declaration in REGISTER DECLARATION header.

**Aspirational**: (34 × 0.278) + (2 × 0.139) = 9.452 + 0.278 = **9.73**

### V-01 Total: **99.7**

---

## V-02 — Finance → Commerce → Operations | Conversational Prose + C-33 | E-Commerce Returns

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Return authorization → credit memo → GL ledger adjustment; all in-scope items traceable in prose |
| C-02 | PASS | Authorization boundary: retry on gateway timeout; GL boundary: rollback on duplicate posting |
| C-03 | PASS | Named: (1) authorization rejection at fraud screen, (2) credit memo GL account mismatch, (3) closed-period GL posting failure |
| C-04 | PASS | Schema transitions narrated: return request fields → credit memo → GL debit/credit pair |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Return portal: real-time; credit memo generation: < 4 h batch; GL close: nightly |
| C-06 | PASS | GL stale window quantified; failure-mode staleness (missed nightly close → 48 h delay) addressed |
| C-07 | PASS | RMA number, credit memo ID, GL account code, cost center throughout |

### Aspirational — non-pass items

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-15 | PARTIAL | Baseline section narrated; connection to C-08 recovery prescriptions and C-09 trade-off not spec-declared |
| C-27 | PARTIAL | Named recovery formula implied by prose content; not a named design feature in variation spec |
| C-28 | **FAIL** | Named-column boundary block schema inapplicable to conversational prose; tabular column structure absent; C-33 provides the non-tabular substitute but cannot satisfy the tabular column-level schema criterion |
| C-30 | PARTIAL | Output register format-specific field-compliance markers adapted to prose field-presence narrative rather than column-tick structure; meets criterion intent but departs from structural form |
| C-32 | PARTIAL | Register-specific compliance marker mapping uses prose field-presence verification; structurally diverges from tabular column-marker mapping |
| C-33 | PASS | Explicitly included in variation spec; register-invariant declaration for non-tabular registers present |

31 remaining aspirational criteria PASS.

**Aspirational**: (31 × 0.278) + (4 × 0.139) + (1 × 0) = 8.611 + 0.556 = **9.17**

### V-02 Total: **99.2**

---

## V-03 — Operations → Finance → Commerce | Tabular | Manufacturing Cost Allocation (4 stages / 3 boundaries per role)

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Production run → WIP lot → cost center allocation → Commerce standard cost pricing; 4-stage chain gives more lineage nodes, all connected |
| C-02 | PASS | All three boundaries annotated per role × 3 roles; no silence |
| C-03 | PASS | Named per stage: BOM mismatch, labor rate dispute, overhead absorption cap, standard-cost override |
| C-04 | PASS | Schema diffs at all 4 stage exits: production order → WIP record → cost center entry → standard cost row |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | 4 stages × 3 roles = 12 annotated latency points — thorough characterization |
| C-06 | PASS | Labor rate stale window (daily payroll feed) and overhead stale window (monthly allocation run) quantified separately |
| C-07 | PASS | BOM, WIP lot, cost center, standard cost, variance account throughout |

### Aspirational — non-pass items

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-15 | PARTIAL | Incumbent manual costing process described but baseline ownership not explicitly assigned to a single role in variation spec |

35 remaining aspirational criteria PASS. 4 stages/3 boundaries per role is the strongest structural stress test for C-11 (interleaved boundary gates), C-18 (incremental elapsed computation), and C-21 (binary freshness verdict): 9 boundary blocks per role × 3 roles = 27 individual verification points.

**Aspirational**: (35 × 0.278) + (1 × 0.139) = 9.722 + 0.139 = **9.86**

### V-03 Total: **99.9**

---

## V-04 — Finance → Operations → Commerce | Tabular | Insurance Claims (Finance owns baseline)

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Claim submission → adjudication → payment disbursement; all in-scope items (Claim ID, EOB, disbursement batch) have unbroken source→stage→destination chains |
| C-02 | PASS | Adjudication boundary: retry on timeout, dead-letter on code-set mismatch; disbursement boundary: rollback on NSF, dead-letter on duplicate |
| C-03 | PASS | Named per stage: (1) claim rejection at eligibility check, (2) duplicate detection collision, (3) NSF on disbursement, (4) closed-period payment failure |
| C-04 | PASS | Schema state at all stage exits: intake form → adjudication record (EOB fields) → disbursement instruction (ACH fields) — field-level diff shown |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Eligibility check: real-time < 500 ms; adjudication: batch 4 h SLA; disbursement: overnight ACH |
| C-06 | PASS | Adjudication code-set stale window quantified (ICD revision cycle); failure-mode staleness (missed batch → 8 h delay) addressed |
| C-07 | PASS | Claim ID, EOB, adjudication code, ICD code, disbursement batch, ACH trace number throughout |

### Aspirational — all 36 PASS

| Criterion range | Verdict | Key evidence |
|-----------------|---------|--------------|
| C-08–C-09 | PASS | Recovery prescriptions for all loss points; named alternative pattern (real-time adjudication) with quantified trade-off dimensions (latency × accuracy) |
| C-10–C-12 | PASS | DOMAIN CONTEXT gate with Claim ID, EOB, adjudication code locked before Stage 1; interleaved boundary blocks; domain entities named in each |
| C-13–C-14 | PASS | Adjudication stale threshold pre-declared in DOMAIN CONTEXT; additive elapsed total computed incrementally at every boundary |
| C-15 | **PASS** | Variation spec explicitly assigns Finance as baseline owner — incumbent manual claims processing described in Finance's Role 1 section, directly connected to C-09 trade-off analysis ("vs. manual adjudication at cost X") and C-08 recovery prescriptions ("revert to manual workflow if batch SLA missed"); closed loop at spec level |
| C-16–C-19 | PASS | Commerce (pos 3) cites Finance's [A-04] by name; immutability prohibition on adjudication threshold; incremental elapsed in every boundary block; [A-xx] convention applied without exception |
| C-20–C-21 | PASS | Stage-write prohibition explicit; FRESH/STALE binary verdict in every boundary block |
| C-22–C-25 | PASS | Pre-declared [A-xx] registry with owner/description columns; Phase Gate 2 checklist with ticked items; STRUCTURAL CONSTRAINTS section with SC-xx identifiers; phase gate artifacts as registry rows |
| C-26 | PASS | Finance (pos 1) → Operations (pos 2) → Commerce (pos 3): Commerce's Citing: line must include [A-04] from Finance, skipping Operations — non-adjacent citation structurally required by skip-level design |
| C-27 | **PASS** | Named recovery formula ("revert to manual adjudication cycle: cost baseline per Finance's INCUMBENT section") explicitly anchored to Finance's baseline section in variation spec — named at design time |
| C-28–C-32 | PASS | Named-column boundary block schema declared; trade-off section cites Finance's INCUMBENT TOTAL token; REGISTER DECLARATION with format-specific markers; compliance marker mapping for tabular registers |
| C-33 | PASS | Vacuous (all registers tabular); no non-tabular registers requiring invariant declaration |
| C-34–C-37 | PASS | Per-boundary incumbent-equivalent column with token-cited baseline derivation; INCUMBENT TOTAL as pre-trade-off closing artifact; REGISTER DECLARATION Parts A/B as single-location authority |
| C-38–C-40 | PASS | Skip-level citation requirement in non-natural position; SC-12 names governed role (Commerce, pos 3) in body; SC-12 declares position distance (two: Commerce at pos 3, Finance at pos 1) in body |
| C-41–C-43 | PASS | Phase Gate 2 item cites [SC-12] by identifier in item text; REGISTER DECLARATION header declares closed chain (every failed Phase Gate item → its governing SC); all three skip-level attributes co-present in SC-12 block without distribution |

**Aspirational**: 36 × 0.278 = **10.00**

### V-04 Total: **100.0**

---

## V-05 — Operations → Commerce → Finance | Tabular | Retail DTC Revenue (Imperative voice)

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Order placement → carrier handoff → financial close; SKU, PRO number, revenue ledger entry all traceable |
| C-02 | PASS | Carrier boundary: retry on API timeout, dead-letter on address validation failure; close boundary: rollback on lock conflict |
| C-03 | PASS | Named: (1) duplicate order detection failure, (2) carrier reject on weight discrepancy, (3) revenue recognition gap on returns, (4) period-close lock conflict |
| C-04 | PASS | Schema diffs: order record (SKU, qty, ship-to) → shipment manifest (PRO, carrier code, weight) → revenue ledger entry (GL account, period, amount) |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Order placement: real-time; carrier handoff: < 2 h batch; financial close: daily 11 PM |
| C-06 | PASS | Carrier status stale window (4 h SLA); failure-mode staleness (carrier API outage → 24 h) addressed |
| C-07 | PASS | SKU, carrier PRO, ship-to address, revenue line, GL close date throughout |

### Aspirational — non-pass items

| ID | Verdict | Evidence note |
|----|---------|---------------|
| C-15 | PARTIAL | Incumbent manual process described; imperative voice strengthens C-20 and C-24 explicitly but baseline-to-C-09 connection not spec-designated at variation level |

35 remaining aspirational criteria PASS. Imperative instruction voice gives C-20 (write-order prohibition: "You MUST NOT write Stage N+1 until this boundary block is fully complete") and C-24 (SC callback: "SC-3 APPLIES HERE: compare Elapsed Total against threshold now") their strongest expression across all five variations.

**Aspirational**: (35 × 0.278) + (1 × 0.139) = 9.722 + 0.139 = **9.86**

### V-05 Total: **99.9**

---

## Rankings

| Rank | Variation | Score | Differentiating feature |
|------|-----------|-------|------------------------|
| **1** | **V-04** | **100.0** | Finance owns baseline — C-15 and C-27 fully closed at spec level; all 36 aspirational PASS |
| 2 | V-03 | 99.9 | 4 stages/3 boundaries — C-11/C-18/C-21 maximally exercised |
| 2 | V-05 | 99.9 | Imperative voice — C-20/C-24 strongest expression |
| 4 | V-01 | 99.7 | Standard tabular baseline — solid across all criteria |
| 5 | V-02 | 99.2 | Prose format — C-28 FAIL, C-30/C-32 PARTIAL offset by C-33 PASS |

---

## Excellence Signals — V-04

### E-01: Role-assigned baseline ownership as a spec-level declaration

V-04's variation axis table contains the entry **"Finance owns baseline."** This single design annotation collapses C-15 (incumbent baseline connected to C-08/C-09) and C-27 (named recovery formula anchoring the baseline) from execution-time disciplines into design-time properties. An evaluator can verify both criteria by inspecting the variation spec before examining a single token of output.

The pattern works because the named role's section automatically becomes the citation authority for all downstream C-29 (trade-off with baseline token citation) and C-16 (cross-role named reference) requirements. Compliance is the path of least resistance — downstream roles find the baseline citation target waiting in a fixed, pre-declared location.

### E-02: Finance-first sequencing makes the baseline-to-trade-off chain structurally inevitable

With Finance at position 1, its incumbent claims-processing baseline section is written first. Operations and Commerce have no choice but to cite Finance's [INCUMBENT TOTAL] token when satisfying C-29 and C-16 — the token already exists at the point they write their trade-off sections. In V-01 (Commerce-first), the baseline role is buried at position 2; the downstream role sequence does not guarantee that a named incumbent artifact is available when the first role that needs it writes its trade-off section.

**Generalizable rule**: Assign the domain function with natural authority over *what existed before this pipeline* to position 1. In enterprise pipelines, Finance functions (ledger reconciliation, billing, adjudication, cost accounting) satisfy this in most domains because financial record-keeping predates the automated data pipeline in the scenario narrative.

---

## New patterns for C-44, C-45 (v14 candidates)

Both excellence signals are structural properties not yet captured by any criterion in C-01–C-43:

**Candidate C-44 — Variation axis baseline-owner column**: The variation axis table must include a "Baseline owner" column naming which role is responsible for the incumbent baseline section. A variation that omits this column and leaves baseline ownership to domain inference does not pass.

**Candidate C-45 — Baseline-first role sequencing rule**: The role designated as baseline owner by C-44 must occupy position 1 in the sequence, ensuring the incumbent baseline section precedes all trade-off analyses and is available as a citation root when the first non-baseline role writes its C-29 section. A variation where the baseline owner is at position 2 or later does not pass.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["variation axis baseline-owner column: designate which role owns the incumbent baseline in the variation spec table itself, collapsing C-15 and C-27 from execution-time disciplines into design-time properties verifiable before any output is produced", "baseline-first role sequencing: place the domain function with natural authority over the incumbent process at position 1 so the baseline section is written first and its INCUMBENT TOTAL token is available as a pre-existing citation root when downstream roles write their C-29 trade-off sections"]}
```
