## flow-dataflow — Round 7 Scoring (Rubric v6)

---

### V-01 — Typed Entity Handoff Manifests (Intercompany Settlement)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | PASS | 6 stages fully defined: Subsidiary Ledger Extract → Intercompany Matching → Currency Netting → Settlement Instruction Generation → SWIFT Transmission → Confirmation Reconciliation. Every stage has named source and destination. |
| C-02 | Boundary error handling | PASS | Section 3 boundary table requires "Error Handling (mechanism or NH-NN: 'no handling — risk accepted')" for every row. Blank cell = structural gap. |
| C-03 | Data loss point identification | PASS | LP-NN sequential identifiers required per stage with example grounding ("LP-01: SWIFT BIC code not found in routing table..."). "Errors may occur" explicitly fails. |
| C-04 | Schema state at each stage | PASS | Input schema + transformations with specific field names required. Typed exit manifests add field count + key field assertions (e.g., `net_amount: DECIMAL(18,4); currency_code: CHAR(3)`). Strongest C-04 enforcement of single-axis variations. |
| C-05 | Latency characterization | PASS | Section 2 latency per stage; Section 3 boundary latency column (value, range, or characterization). Standard — not decomposed. |
| C-06 | Stale data windows | PASS | Section 4 accumulates to FRESH/STALE threshold comparison; Section 5 requires separate normal-operation stale window (treasury workstation consumer, Stage 3–5) and worst-case failure mode duration. |
| C-07 | Domain framing | PASS | Section 1 names: SubsidiaryLedgerEntry, IntercompanyMatchRecord, NetPosition, SettlementInstruction, SWIFTMessage, ConfirmationRecord. Finance domain throughout. |
| C-08 | Recovery prescriptions | PASS | Section 6 requires one row per NH-NN + one row per LP-NN. "Generic advice fails" stated. 5-column table enforces specific mechanism. |
| C-09 | Pattern trade-off analysis | PASS | Section 7 requires named alternative (gross SWIFT per transaction, bilateral vs multilateral netting, etc.) + ≥2 dimensions + one comparing automated elapsed time vs INCUMBENT TOTAL in domain terms (settlement cycle minutes, FX risk exposure). |
| C-10 | Pre-trace entity inventory | PASS | Section 1 enumerates all entities before Section 2 begins. Section 3 Entity at Risk must cite from the typed exit manifest (even tighter than C-10 alone). |
| C-11 | Systematic boundary labeling | PASS | B1->2 through B5->6 pre-labeled in table; NH-NN format rule enforced. C-02/C-08 annotations reference labels by name. |
| C-12 | Verified-unchanged schema assertion | PASS | Explicit required phrase: `verified: no field added, removed, renamed, or retyped` for unchanged stages. |
| C-13 | Structural completeness enforcement | PASS | Section 3 boundary table: "a row with any blank cell is a structural gap." Section 6 recovery table: "all five columns are required." Both map to C-02/C-03 requirements. |
| C-14 | Incumbent baseline anchoring | PASS | Section 0 MS-NN Step IDs with explicit citation rule: "cite incumbent steps by Step ID (MS-NN format) in all downstream recovery entries." |
| C-15 | Structured incumbent baseline table | PASS | 4-column table (Step ID, Manual Step, Actor, Duration), minimum 5 intercompany-specific steps. Steps have named identifiers for downstream citation. |
| C-16 | Full recovery-to-baseline traceability | PASS | Section 6 has "Step ID Cited (MS-NN)" column AND "Manual Step Cited (exact value from SECTION 0)" column. Every row requires both. "Generic terms such as 'manual review' without a Step ID do not satisfy C-16." |
| C-17 | Entity-at-risk annotation per boundary | PASS | Section 3 rule: "annotation must name a specific entity AND a specific field from that entity's typed exit manifest." Format: `entity.field_name — risk description`. Field not in manifest = invalid citation. Exceeds C-17 minimum by one tier. |
| C-18 | Structured recovery audit table | PASS | 5-column named table: Trigger ID, Triggering Condition, Recovery Mechanism, Step ID Cited (MS-NN), Manual Step Cited. Every NH-NN and LP-NN must have a corresponding row. |

**Essential: 4/4 PASS → 60 pts. Recommended: 3/3 PASS → 30 pts. Aspirational: 11/11 PASS → 10 pts.**
**Composite V-01: 100**

---

### V-02 — SLA Budget Framing (Retail Vendor Replenishment)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | PASS | 6 stages: POS Depletion Capture → Replenishment Signal Generation → Purchase Order Issuance → Vendor Confirmation → ASN Receipt and Validation → Goods Receipt Posting. Complete chain. |
| C-02 | Boundary error handling | PASS | Section 3 7-column table requires NH-NN or mechanism per boundary. Blank = structural gap. |
| C-03 | Data loss point identification | PASS | LP-NN sequential identifiers per stage required with concrete failure. |
| C-04 | Schema state at each stage | PASS | Input schema + Transformations + Output schema per stage required. No typed exit manifests — standard coverage. C-17 entity-level only (no field traceability from manifests). |
| C-05 | Latency characterization | PASS | Section 3 decomposes boundary latency into Transport Latency + Processing Overhead columns, both requiring numeric values. Stage latency in Section 2. Strongest C-05 of single-axis variations. |
| C-06 | Stale data windows | PASS | Section 4 shows SLA% running total at each step; budget domination point identified by highest % row; Section 5 stale window for WMS consumer + whether domination point determines recovery duration. |
| C-07 | Domain framing | PASS | Section 1 names: DepletionEvent, ReplenishmentSignal, PurchaseOrder, VendorConfirmation, AdvanceShipmentNotice, GoodsReceiptRecord, InventoryLedgerEntry. Operations domain throughout. |
| C-08 | Recovery prescriptions | PASS | Section 6 5-column recovery audit table. One row per NH-NN + one per LP-NN required. |
| C-09 | Pattern trade-off analysis | PASS | Section 7 requires named alternative + ≥2 dimensions + one comparing pipeline SLA budget consumption against INCUMBENT SLA, naming boundary responsible for largest budget share. |
| C-10 | Pre-trace entity inventory | PASS | Section 1 entity inventory before Section 2. Entity at Risk column in Section 3 draws from Section 1. |
| C-11 | Systematic boundary labeling | PASS | B1->2 through B5->6 pre-labeled; NH-NN format required. |
| C-12 | Verified-unchanged schema assertion | PASS | "verified: no field added, removed, renamed, or retyped" phrase required. |
| C-13 | Structural completeness enforcement | PASS | 7-column boundary table — "all seven columns are required — a row with any blank cell is a structural gap." SLA Budget Consumed (%) column adds a new structural surface: blank % = visible gap. |
| C-14 | Incumbent baseline anchoring | PASS | MS-NN Step IDs in Section 0. Section 6 "Step ID Cited (MS-NN)" column enforces citation. |
| C-15 | Structured incumbent baseline table | PASS | 4-column table, 5+ retail-replenishment-specific steps. |
| C-16 | Full recovery-to-baseline traceability | PASS | "Step ID Cited (MS-NN)" + "Manual Step Cited (exact value)" columns in recovery table. |
| C-17 | Entity-at-risk annotation per boundary | PASS | Section 3 Entity at Risk requires "specific domain entity from SECTION 1." Entity-level annotation only (no field-level constraint — typed manifests absent). Meets C-17 minimum. |
| C-18 | Structured recovery audit table | PASS | 5-column named table. Every NH-NN and LP-NN requires a row. |

**Essential: 4/4 PASS → 60 pts. Recommended: 3/3 PASS → 30 pts. Aspirational: 11/11 PASS → 10 pts.**
**Composite V-02: 100**

---

### V-03 — Declaration-to-Reference Closure Enforcement (Subscription Billing)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | PASS | 6 stages: Usage Meter Ingestion → Entitlement Application → Billing Calculation → Invoice Generation → Payment Collection → Revenue Recognition Posting. |
| C-02 | Boundary error handling | PASS | 5-column boundary table; NH-NN format required. |
| C-03 | Data loss point identification | PASS | LP-NN identifiers assigned at declaration in Section 2. "This identifier is a member of the declared set" — forward-declared for Section 6b closure check. |
| C-04 | Schema state at each stage | PASS | Input schema + Transformations + Output schema per stage. No typed manifests — standard coverage at minimum level. |
| C-05 | Latency characterization | PASS | Stage latency in Section 2; Boundary Latency column in Section 3 (value, range, or characterization). Standard — not decomposed. |
| C-06 | Stale data windows | PASS | Section 4 accumulates to FRESH/STALE comparison; Section 5 stale window for revenue controller (Stage 3–5) + worst-case failure mode duration. |
| C-07 | Domain framing | PASS | Section 1: UsageMeterRecord, EntitlementRecord, BillingLineItem, Invoice, PaymentTransaction, RevenueRecognitionEntry. Commerce domain. |
| C-08 | Recovery prescriptions | PASS | Section 6a recovery table + Section 6b closure check. Closure check structurally verifies every declared NH/LP has a recovery row — the only single-axis variation with this meta-enforcement. |
| C-09 | Pattern trade-off analysis | PASS | Section 7 requires named alternative + ≥2 dimensions + one comparing automated elapsed vs INCUMBENT TOTAL. |
| C-10 | Pre-trace entity inventory | PASS | Section 1 entity inventory before Section 2. |
| C-11 | Systematic boundary labeling | PASS | B1->2 through B5->6; NH-NN fixed at declaration; "may not be revised or renumbered in later sections." |
| C-12 | Verified-unchanged schema assertion | PASS | Required phrase stated. |
| C-13 | Structural completeness enforcement | PASS | Section 3 5-column boundary table + Section 6a recovery table + Section 6b closure gate. Section 6b acts as a meta-structural gate making missing recovery rows visible across all criteria simultaneously. |
| C-14 | Incumbent baseline anchoring | PASS | MS-NN Step IDs, citation rule. |
| C-15 | Structured incumbent baseline table | PASS | 4-column table, 5+ billing-specific steps. |
| C-16 | Full recovery-to-baseline traceability | PASS | "Step ID Cited (MS-NN)" + "Manual Step Cited (exact value)" columns required. |
| C-17 | Entity-at-risk annotation per boundary | PASS | Section 3 requires "specific domain entity from SECTION 1." Entity-level. Meets C-17 minimum. |
| C-18 | Structured recovery audit table | PASS | 5-column table in Section 6a + Section 6b closure check verifies row completeness. Strongest C-18 enforcement of any single-axis variation. |

**Essential: 4/4 PASS → 60 pts. Recommended: 3/3 PASS → 30 pts. Aspirational: 11/11 PASS → 10 pts.**
**Composite V-03: 100**

---

### V-04 — Typed Manifests + SLA Budget Framing (Vendor Payment Terms Sync)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | PASS | 6 stages: Supplier Portal Extract → Payment Terms Normalization → Contract Terms Validation → ERP Payment Terms Update → Open PO Application → AP Ledger Reconciliation. |
| C-02 | Boundary error handling | PASS | 7-column boundary table; NH-NN format required. |
| C-03 | Data loss point identification | PASS | LP-NN per stage with concrete named failures. |
| C-04 | Schema state at each stage | PASS | Typed exit manifests required with field count + key field assertions (e.g., `net_days: INTEGER(3); early_pay_discount_pct: DECIMAL(5,4)`). Manifest is "sole authority for field types available to downstream boundary Entity at Risk annotations." |
| C-05 | Latency characterization | PASS | Transport Latency + Processing Overhead columns, both requiring value or range. Stage latency in Section 2. Numeric throughout. |
| C-06 | Stale data windows | PASS | Section 4 SLA% running total; budget domination point identified by label AND field type from exit manifest; Section 5 stale window for AP controller + whether domination point determines recovery window. |
| C-07 | Domain framing | PASS | Section 1: VendorPaymentTermsRecord, NormalizedPaymentTerm, ContractTermsRecord, ERPVendorMasterRecord, OpenPurchaseOrder, APLedgerEntry. Finance domain. |
| C-08 | Recovery prescriptions | PASS | Section 6 5-column recovery table. Every NH-NN + LP-NN requires a row. |
| C-09 | Pattern trade-off analysis | PASS | Section 7 requires named alternative (EDI push vs portal pull, real-time vs batch, centralized vs distributed vendor master) + ≥2 dimensions + one comparing against INCUMBENT SLA naming budget domination point AND its field type as primary architectural driver. Deepest C-09 of dual-axis variations. |
| C-10 | Pre-trace entity inventory | PASS | Section 1 inventory before Section 2. Entity at Risk must cite entity.field_name from exit manifest — tighter than C-10 alone. |
| C-11 | Systematic boundary labeling | PASS | B1->2 through B5->6 labeled; NH-NN fixed. |
| C-12 | Verified-unchanged schema assertion | PASS | "verified: no field added, removed, renamed, or retyped" required. |
| C-13 | Structural completeness enforcement | PASS | 7-column boundary table: blank = structural gap. SLA Budget Consumed (%) adds a quantitative structural surface — a missing % is as visible as a missing entity annotation. |
| C-14 | Incumbent baseline anchoring | PASS | MS-NN Step IDs, citation rule. |
| C-15 | Structured incumbent baseline table | PASS | 4-column table, 5+ payment-terms-specific steps. |
| C-16 | Full recovery-to-baseline traceability | PASS | "Step ID Cited (MS-NN)" + "Manual Step Cited (exact value)" required for every recovery row. |
| C-17 | Entity-at-risk annotation per boundary | PASS | `entity.field_name — risk description` format required. Field must appear in upstream stage's typed exit manifest. "A field not in the manifest is a traceability failure." Deepest C-17 enforcement alongside V-01. |
| C-18 | Structured recovery audit table | PASS | 5-column named table. Every NH-NN + LP-NN requires a row. |

**Essential: 4/4 PASS → 60 pts. Recommended: 3/3 PASS → 30 pts. Aspirational: 11/11 PASS → 10 pts.**
**Composite V-04: 100**

---

### V-05 — All Three R7 Axes Combined (Order-to-Cash)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | PASS | 6 stages across three domains: Order Receipt → Credit Check → Order Fulfillment → Shipment → Invoice Generation → Cash Collection. Finance/Operations/Commerce domain transitions tested; cognitive load risk noted in design but prompt-compliant output covers all stages. |
| C-02 | Boundary error handling | PASS | 7-column boundary table; NH-NN required; "fixed at declaration; member of the declared set" for closure check verification. |
| C-03 | Data loss point identification | PASS | LP-NN per stage, "member of declared set and will be verified in SECTION 6b." Every LP anchored to the closure check. |
| C-04 | Schema state at each stage | PASS | Typed exit manifests with field count + key field assertions (e.g., `credit_limit_usd: DECIMAL(15,2); approval_status: ENUM(APPROVED, PENDING, REJECTED)`). "Field assertions are the sole authority for which field types are available to downstream boundary Entity at Risk annotations." |
| C-05 | Latency characterization | PASS | Transport Latency + Processing Overhead columns, both numeric. Section 4 shows SLA% running total with budget domination sub-component identified (Transport vs Processing Overhead). |
| C-06 | Stale data windows | PASS | Section 4 SLA% running total; domination point identified by label AND field type. Section 5 stale window for AR controller (Stage 4–6) + whether domination point determines recovery duration. |
| C-07 | Domain framing | PASS | Section 1: CustomerPurchaseOrder, CreditAssessmentRecord, FulfillmentOrder, ShipmentRecord, Invoice, PaymentReceipt. Three-domain (Finance/Operations/Commerce) entity coverage. |
| C-08 | Recovery prescriptions | PASS | Section 6a 5-column recovery table + Section 6b closure check. Closure check verifies all declared NH/LP identifiers have recovery rows. Missing row identified without being patched. |
| C-09 | Pattern trade-off analysis | PASS | Section 7 requires named alternative + ≥2 dimensions + one comparing pipeline SLA budget against INCUMBENT SLA naming domination point and field type + one referencing specific domain role (credit controller, warehouse manager, AR specialist) and decision authority in incumbent baseline. Most demanding C-09 specification in any variation. |
| C-10 | Pre-trace entity inventory | PASS | Section 1 inventory before Section 2. Exit manifests anchor entity.field_name citations downstream. |
| C-11 | Systematic boundary labeling | PASS | B1->2 through B5->6; NH-NN "fixed at declaration; member of the declared set." |
| C-12 | Verified-unchanged schema assertion | PASS | Required phrase stated. |
| C-13 | Structural completeness enforcement | PASS | 7-column boundary table (blank = gap) + Section 6a recovery table + Section 6b closure gate. Three independent structural surfaces mapping to C-02, C-03, C-04, C-08, and C-18 simultaneously. Highest C-13 structural depth. |
| C-14 | Incumbent baseline anchoring | PASS | MS-NN Step IDs with citation rule. |
| C-15 | Structured incumbent baseline table | PASS | 4-column table, 5+ order-to-cash-specific steps (credit analyst pulling bureau portal, warehouse pick/pack, etc.). |
| C-16 | Full recovery-to-baseline traceability | PASS | "Step ID Cited (MS-NN)" + "Manual Step Cited (exact value)" columns in Section 6a. Closure check in 6b verifies every declared LP/NH is represented. |
| C-17 | Entity-at-risk annotation per boundary | PASS | `entity.field_name — risk description`; field must appear in upstream typed exit manifest; field not in manifest = invalid citation. Full field-level traceability. |
| C-18 | Structured recovery audit table | PASS | 5-column Section 6a table + Section 6b four-item closure reconciliation. Missing row structurally visible without scorer cross-referencing. |

**Essential: 4/4 PASS → 60 pts. Recommended: 3/3 PASS → 30 pts. Aspirational: 11/11 PASS → 10 pts.**
**Composite V-05: 100**

---

## Composite Scores and Ranking

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|------|-----------|---------------|-----------------|-------------------|-----------|
| 1 | V-05 | 60 | 30 | 10 | **100** |
| 2 | V-04 | 60 | 30 | 10 | **100** |
| 3 | V-01 | 60 | 30 | 10 | **100** |
| 4 | V-02 | 60 | 30 | 10 | **100** |
| 5 | V-03 | 60 | 30 | 10 | **100** |

All five variations are structurally complete against rubric v6. Ranking above is tiebroken by criteria depth beyond minimum pass conditions.

**Tiebreaker rationale:**

- **V-05 > V-04**: V-05 adds Section 6b closure enforcement (meta-verification for C-08/C-18 completeness, detectable false-complete closure statement as a failure signal) and role-level C-09 requirement (domain decision authority in trade-off). V-04 lacks both.
- **V-04 > V-01**: V-04 adds SLA budget decomposition (Transport + Processing Overhead columns) with numeric enforcement at every boundary. V-01 has typed manifests but standard single-column latency.
- **V-01 > V-02**: V-01's typed exit manifests drive C-17 to field-level (entity.field_name) and C-04 to type-assertion depth. V-02's field-level C-04 coverage is standard (input/output schema without typed assertions). V-01 advances more criteria simultaneously from a single mechanism.
- **V-02 > V-03**: V-02's SLA budget framing advances C-05/C-06 depth (numeric decomposition, domination point visibility, SLA breach arithmetic) across more criteria than V-03's closure check, which enhances C-08/C-18 only.

---

## Excellence Signals from V-05 (Top-Ranked)

**Signal 1 — Typed exit manifests drive field-level cascade:**
The EXIT MANIFEST format (`entity | fields: [count] | key field assertions: [field_name: type]`) forces every downstream Entity at Risk annotation to name a specific field type, not just an entity. The constraint "A field not in the manifest is an invalid citation" creates a closed reference system: manifest → boundary annotation → recovery row → incumbent baseline citation. This cascade is the deepest per-criterion linkage chain produced by any R7 variation — each stage's exit feeds the next stage's boundary, which feeds the recovery table, which feeds the incumbent step citation.

**Signal 2 — SLA budget % column makes latency domination arithmetically deterministic:**
The "(Transport + Processing) ÷ INCUMBENT SLA" formula forces a numeric output for every boundary including synchronous API crossings. The domination point is not a relative comparison ("Stage 4 takes longer than Stage 2") but an absolute structural fact (the row with the highest %). Section 4's requirement to cite the domination point by label AND by the specific field type from the exit manifest produces a conclusion that neither typed manifests alone nor SLA framing alone enforces: the field type at the bottleneck boundary is named in the stale analysis.

**Signal 3 — Section 6b closure check shifts gap detection to the producing model:**
The four-item closure check (declared NH identifiers, declared LP identifiers, recovery rows present, missing recovery rows) requires the LLM to enumerate both sets and compute the delta before completing the section. A false-complete closure statement (claiming NONE missing when a row is absent) is detectable because the declared count and table row count are both stated. This produces a testable signal: when a gap exists, does the closure statement reflect it correctly or match the table? V-05 is the only variation where this signal is observable in the output.

**Signal 4 — Cross-domain order-to-cash reveals whether typed manifests hold under domain transition:**
V-05's three-domain scenario (Finance credit check, Operations fulfillment, Commerce invoicing) tests typed manifest propagation across domain boundaries. The S-2 to S-3 boundary (credit assessment service → warehouse management system) crosses Finance into Operations; the manifest for CreditAssessmentRecord must carry field assertions that the FulfillmentOrder manifest at the next stage references. This is the first R7 scenario where manifest citations must survive a domain-handoff, not just a within-domain stage transition.

---

## New R7 Patterns

**Pattern 1 — Typed entity handoff manifests (V-01, V-04, V-05)**
Stage-exit declarations that include field count and at least two key field assertions per entity (`entity_name | fields: [count] | field_name: type`) constrain downstream boundary Entity at Risk annotations from entity-level (`SettlementInstruction at risk`) to field-level (`SettlementInstruction.swift_bic_code: VARCHAR(20) — truncation risk`). This simultaneously deepens C-04 (schema state at exit is quantified) and C-17 (entity-at-risk annotation is field-specific). The manifest becomes a closed reference: a field cited in a boundary annotation that doesn't appear in the upstream stage's manifest is a traceable traceability failure, not just a vague quality issue.

**Pattern 2 — SLA budget framing as latency domination surface (V-02, V-04, V-05)**
Expressing boundary latency as `(Transport Latency + Processing Overhead) ÷ INCUMBENT SLA` produces a structural % column where the domination point is the row with the highest value — visible without summing or comparing. The column also makes SLA breach arithmetic deterministic: if the column sums to > 100%, the Section 4 stale analysis MUST state STALE before the running total comparison. This eliminates a class of LLM hedging ("FRESH, but close to the threshold") by making breach a structural fact observable in the table itself.

**Pattern 3 — Declaration-to-reference closure enforcement (V-03, V-05)**
Section 6b's four-item reconciliation (declared NH set, declared LP set, recovery rows present, missing rows) shifts completeness verification from scorer to producer. The key testable behavior is whether a producing model generates a closure statement that matches the recovery table (false-complete) or matches the declared set (genuine). This produces a diagnostic signal about LLM list-reconciliation reliability: a model that generates NH-01, NH-02, NH-03 in Section 3 but omits NH-02 from Section 6a, then writes "all declared identifiers have a recovery row" in Section 6b, has produced a specific, detectable failure type that pre-numbering alone does not surface.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["typed entity handoff manifests — stage-exit field count and key field assertions constrain downstream Entity at Risk annotations to entity.field_name format, deepening C-04 and C-17 simultaneously through a closed reference system", "SLA budget framing — expressing boundary latency as percentage of declared SLA makes the latency domination point structurally deterministic and SLA breach arithmetically observable in the table before any running-total comparison", "declaration-to-reference closure enforcement — explicit post-recovery reconciliation of declared NH/LP identifier sets against recovery table rows shifts gap detection to the producing model and makes false-complete closure statements detectable as a specific, scorable failure type"]}
```
