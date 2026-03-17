# flow-dataflow — Round 3 Scoring (Rubric v2)

---

## Scoring Setup

| Tier | Criteria | Max pts | Pts/criterion |
|------|----------|---------|---------------|
| Essential | C-01 – C-04 | 60 | 15 each |
| Recommended | C-05 – C-07 | 30 | 10 each |
| Aspirational | C-08 – C-12 | 10 | 2 each |

PARTIAL = 0.5 of criterion value. Composite = sum of tier scores.

---

## V-01 — Natural Finance-First

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Six stages with explicit system-to-system names; entity vocab (CustomerPayment, AREntry, AgingBucket, JournalEntry, GLPosting, RevenueSnapshot) declared before Stage 1; unbroken lineage chain required. |
| C-02 | **PASS** | BOUNDARY CHECKS section requires all five boundaries (B1->2 through B5->6), each with error-handling mechanism or explicit "no handling — risk accepted." |
| C-03 | **PASS** | All six stage formats require "concrete, named failure mode — 'errors may occur' does not qualify." |
| C-04 | **PASS** | Input schema / transformations (specific field names, "same as input does not qualify") / output schema required per stage. |
| C-05 | **PASS** | Latency annotation required at every stage: value, range, or characterization. |
| C-06 | **PASS** | STALE ANALYSIS sums all latencies vs threshold, normal + worst-case failure explicitly addressed separately. |
| C-07 | **PASS** | Six domain entity names declared; they appear throughout STAGE TRACE sections. |
| C-08 | **PASS** | RECOVERY PRESCRIPTIONS requires paired entry for every "no handling" and every loss point, naming mechanism and boundary/stage; "generic advice does not qualify." |
| C-09 | **PASS** | TRADE-OFF ANALYSIS requires named alternative + 2 dimensions + 1 quantified in AR-to-GL domain terms (e.g., "introduces a 4-hour stale window in aging buckets"). |
| C-10 | **FAIL** | Entity vocab declared in DOMAIN CONTEXT before Stage 1, but no "reference-only" enforcement rule; entities introduced mid-trace would not be caught. |
| C-11 | **PARTIAL** | Boundary labels B1->2 – B5->6 established in BOUNDARY CHECKS (C-02 annotations use them); recovery prescriptions say "boundary or stage" without requiring the B[N]->[N+1] format. C-08 annotations not label-anchored. |
| C-12 | **FAIL** | BOUNDARY CHECKS says "if unchanged, state 'unchanged'" — bare "unchanged" fails C-12 per rubric; no verification-claim requirement. |

**Composite:** 60 + 30 + (2+2+0+1+0) = **95**

---

## V-02 — Table-Dominant Schema Diffs

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Six stages with system names; entity vocab (SalesOrder, OrderLineItem, InventoryReservation, FulfillmentAllocation, ShipmentEvent, Invoice, AREntry) declared before Stage 1. |
| C-02 | **PASS** | BOUNDARY SUMMARY TABLE requires all five rows (B1->2 – B5->6) with error-handling column; blank cell is "structural gap." |
| C-03 | **PASS** | Loss point required per stage; "errors may occur fails" explicit. |
| C-04 | **PASS** | 4-column schema-diff table (Field / Entry Schema / Transformations / Exit Schema) per stage; blank cell is a visible structural gap. |
| C-05 | **PASS** | Latency required after each schema-diff table. |
| C-06 | **PASS** | STALE ANALYSIS sums table latencies vs threshold, both scenarios addressed separately. |
| C-07 | **PASS** | Domain Entity at Risk column in BOUNDARY TABLE requires specific entity name; "data or records does not qualify." |
| C-08 | **PASS** | RECOVERY PRESCRIPTIONS explicitly says "Reference the boundary label (e.g., 'B3->4:') at the start of each entry"; paired with every "no handling" row and loss point. |
| C-09 | **PASS** | TRADE-OFF ANALYSIS names alternative + 2 dimensions + 1 quantified in order-fulfillment domain terms. |
| C-10 | **FAIL** | DOMAIN CONTEXT declares entities before Stage 1 but contains no "reference-only" prohibition; mid-trace entity introductions would not trigger a protocol violation. |
| C-11 | **PASS** | BOUNDARY SUMMARY TABLE establishes complete labeled inventory (B1->2 – B5->6); recovery prescriptions explicitly required to open with "B3->4:" format — C-02 and C-08 annotations both label-anchored. |
| C-12 | **FAIL** | Schema-diff Transformations column uses "— no change" convention; BOUNDARY TABLE says "if N: 'unchanged'" — neither satisfies "verified: no field added, removed, renamed, or retyped." |

**Composite:** 60 + 30 + (2+2+0+2+0) = **96**

---

## V-03 — Inline Boundary Gates

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Five stages with system names; entity vocab (DemandSignal, PurchaseOrder, SupplierOrder, GoodsReceipt, StockLedgerEntry, InventoryPosition) declared in STEP 1. |
| C-02 | **PASS** | BOUNDARY GATE inline before each subsequent stage; "Stage N+1 does not open until BOUNDARY GATE B[N]->[N+1] is fully stated" — omission is a structural protocol violation, not a prose gap. |
| C-03 | **PASS** | Concrete named failure mode required at each stage; "errors may occur fails" explicit. |
| C-04 | **PASS** | Input schema / transformations / output schema format per stage; specific field names required. |
| C-05 | **PASS** | Latency annotation required per stage. |
| C-06 | **PASS** | STEP 7 accumulates step-by-step (each addend shown), normal + worst-case verdict separately. |
| C-07 | **PASS** | Six domain entity names declared; used throughout stage trace and boundary gates. |
| C-08 | **PASS** | STEP 8 requires paired prescription for every "no handling" gate and every named loss point, naming "recovery mechanism and the specific gate label or stage"; generic advice fails. |
| C-09 | **PASS** | STEP 9 requires named alternative + 2 dimensions + 1 in inventory-management domain terms; example demonstrates qualified domain framing ("VMI eliminates B1->2 transmission latency but requires supplier read-access to stock ledger"). |
| C-10 | **FAIL** | STEP 1 entity declaration is a dedicated step, but no "reference-only" protocol-violation rule; mid-trace entity introductions not prohibited. |
| C-11 | **PASS** | Boundary gate labels B1->2 – B4->5 inline; STEP 8 recovery prescriptions required to name "the specific gate label or stage" — the gate label format is unambiguous. C-02 and C-08 annotations both label-anchored. |
| C-12 | **FAIL** | No schema-unchanged verification rule; stage format only requires naming transformations, not verifying absence of change with explicit claim. |

**Composite:** 60 + 30 + (2+2+0+2+0) = **96**

---

## V-04 — Non-Natural O→C→F + Inertia Framing

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Six stages across three roles; entity vocab (GoodsReceipt, SupplierInvoice, PurchaseOrder, ThreeWayMatchResult, PaymentAuthorization, BankPayment, GLEntry) declared in Operations DOMAIN CONTEXT. |
| C-02 | **PASS** | Inline boundary checks before each subsequent stage with "error-handling mechanism or 'no handling — risk accepted'" required; covers B1->2 through B5->6. |
| C-03 | **PASS** | Concrete named loss points required per stage; "errors may occur fails" explicit. |
| C-04 | **PASS** | Input schema / named transformations / output schema per stage. |
| C-05 | **PASS** | Latency required per stage. |
| C-06 | **PASS** | STALE ANALYSIS accumulates stages 1–6 and B1->2 – B5->6; normal + worst-case separately vs threshold. |
| C-07 | **PASS** | Seven domain entity names declared; used throughout; skip-level citation enforces entity reuse across roles. |
| C-08 | **PASS** | Recovery prescriptions require naming mechanism and location; critical failures must reference "Operations INCUMBENT BASELINE as the identified fallback process" — adds concrete fallback specificity above rubric baseline. |
| C-09 | **PASS** | TRADE-OFF ANALYSIS requires named alternative + 2 dimensions + 1 comparing automated latency against Operations INCUMBENT BASELINE total — grounded domain comparison. |
| C-10 | **FAIL** | Entity declaration in OPERATIONS DOMAIN CONTEXT is before Stage 1 but no reference-only rule; Commerce and Finance sections could introduce entities not in Operations DOMAIN CONTEXT without violation. |
| C-11 | **PARTIAL** | Boundary labels B1->2 – B5->6 used inline (C-02 anchored); recovery prescriptions say "naming mechanism and location" — "location" is vague and does not require B[N]->[N+1] format. C-08 annotations not label-anchored. |
| C-12 | **FAIL** | No schema-unchanged verification rule; "state 'unchanged'" (implied by boundary schema transition notes) does not meet rubric threshold. |

**Composite:** 60 + 30 + (2+2+0+1+0) = **95**

---

## V-05 — Combined: Entity Inventory + Boundary Labeling + Schema Verification

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Five stages with system names; STEP 0 entity inventory (UsageEvent, MeteringAggregate, BillingRecord, Invoice, RevenueSchedule, DeferredRevenueEntry, GLPosting) declared before Stage 1; "Reference only entities from the Step 0 DOMAIN ENTITY INVENTORY throughout" enforces lineage closure. |
| C-02 | **PASS** | BOUNDARY CHECKS requires all four boundaries (B1->2 – B4->5) with labeled error-handling or exact "no handling — risk accepted [B[N]->[N+1]]"; "A labeled boundary with no error-handling annotation is a visible, scorable gap." |
| C-03 | **PASS** | Concrete named loss points required per stage; "errors may occur fails" explicit. |
| C-04 | **PASS** | Input schema / named transformations / output schema per stage; "same as input fails." Schema-unchanged rule adds explicit verification for pass-through stages. |
| C-05 | **PASS** | Latency annotation required per stage. |
| C-06 | **PASS** | STALE ANALYSIS shows each addend step-by-step through Stage 5; normal + worst-case separately vs threshold. |
| C-07 | **PASS** | Seven required entity names in STEP 0; "Reference only entities from the Step 0 DOMAIN ENTITY INVENTORY" enforces entity vocabulary throughout. |
| C-08 | **PASS** | Recovery prescriptions require: (1) opening with boundary label or stage, (2) naming recovery mechanism, (3) naming specific entity from Step 0 inventory that recovery protects. All three elements structurally required. |
| C-09 | **PASS** | TRADE-OFF ANALYSIS names alternative + 2 dimensions + 1 quantified in subscription-billing domain terms; example demonstrates required precision ("periodic aggregation introduces a 1-hour recognition lag vs real-time accrual for UsageEvents"). |
| C-10 | **PASS** | STEP 0 is a dedicated entity inventory step before Stage 1; explicit rule: "An entity introduced mid-trace without a prior entry in this inventory is a protocol violation." Reference-only constraint fully enforced. |
| C-11 | **PASS** | All four boundaries require labels following exact B[N]->[N+1] pattern; recovery prescriptions must open with "B2->3:" or "Stage 3 loss point:" format; "A labeled boundary with no error-handling annotation is a visible, scorable gap." C-02 and C-08 annotations both label-anchored. |
| C-12 | **PASS** | Explicit "Schema-unchanged rule" requires: "verified: no field added, removed, renamed, or retyped at this stage." Bare "unchanged" explicitly prohibited by rule text. |

**Composite:** 60 + 30 + (2+2+2+2+2) = **100**

---

## Score Summary and Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | **V-05** | 60/60 | 30/30 | 10/10 | **100** | Yes |
| 2 | **V-02** | 60/60 | 30/30 | 6/10 | **96** | Yes |
| 2 | **V-03** | 60/60 | 30/30 | 6/10 | **96** | Yes |
| 4 | **V-01** | 60/60 | 30/30 | 5/10 | **95** | Yes |
| 4 | **V-04** | 60/60 | 30/30 | 5/10 | **95** | Yes |

All five variations pass all essential criteria and exceed the 80 golden threshold.

---

## Excellence Signals from V-05

**V-05 is the top scorer because it is the only variation to simultaneously satisfy C-10, C-11, and C-12. Three structural patterns produced that result:**

### Signal 1 — Protocol-violation entity lock (C-10 enabler)
STEP 0 names the inventory AND adds an explicit rule: "An entity introduced mid-trace without a prior entry in this inventory is a protocol violation." The combination of pre-declaration + prohibition is what makes C-10 structurally enforceable. Prior variations (V-01 – V-04) declared entities but omitted the prohibition, leaving the constraint aspirational for the model rather than structural for the prompt.

### Signal 2 — Label-embedded "no handling" flag (C-11 enabler)
Requiring the exact text "no handling — risk accepted [B[N]->[N+1]]" with the boundary label embedded inside the flag means every unhandled boundary is self-indexed. Recovery prescriptions that must open with "B2->3:" can now be mechanically verified against the flag text without re-reading the full trace. V-02 and V-03 achieve C-11 via table/gate structure; V-05's embedded-label flag extends the discipline into prose annotations.

### Signal 3 — Named verification statement for unchanged schemas (C-12 enabler)
The rule "If a stage makes no schema change, you must state: 'verified: no field added, removed, renamed, or retyped at this stage'" is the minimum viable text that distinguishes a verified assertion from an assumption. V-01 – V-04 allow "unchanged," which is indistinguishable from inattention. The explicit rule text eliminates that ambiguity.

### New pattern candidate — Entity-anchored recovery prescription
V-05 requires recovery prescriptions to name the specific entity from the Step 0 inventory that the recovery protects — a third required element beyond the current C-08 requirement of (mechanism + boundary). This makes recovery prescriptions entity-addressable: "B2->3: dead-letter queue — protects BillingRecord" vs. "add a dead-letter queue at B2->3." This is a candidate for C-13 in rubric v3.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["entity-anchored recovery prescription: require naming the specific Step 0 inventory entity the recovery protects as a third required element alongside mechanism and boundary label", "label-embedded no-handling flag: embed the boundary label inside the flag text itself so every unhandled boundary is self-indexed and directly addressable in recovery prescriptions without re-reading the trace"]}
```
