## flow-dataflow — Round 5 Scoring (Rubric v4)

---

### Scoring Summary Table

| Criterion | Category | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| **C-01** Data lineage chain | essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** Boundary error handling | essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** Data loss point identification | essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** Schema state at each stage | essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** Latency characterization | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-06** Stale data windows | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** Domain framing | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** Recovery prescriptions | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-09** Pattern trade-off analysis | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-10** Pre-trace entity inventory | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-11** Systematic boundary labeling | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-12** Verified-unchanged assertion | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-13** Structural completeness enforcement | aspirational | **FAIL** | PASS | **FAIL** | PASS | PASS |
| **C-14** Incumbent baseline anchoring | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-15** Structured incumbent baseline table | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-16** Full recovery-to-baseline traceability | aspirational | PASS | PASS | PASS | PASS | PASS |

---

### Per-Variation Detail

---

#### V-01 — Baseline Table Column Structure: 3-Column Minimal

**C-01 PASS** — Six stages explicitly chained (vendor portal → legal entity → tax identity → banking → payment terms → ERP master); input/output schema required per stage creates unbroken lineage.

**C-02 PASS** — SECTION 4 labels B1->2 through B5->6 and requires either a named mechanism or `no handling — risk accepted` for each. Silence not permitted.

**C-03 PASS** — "Loss point: a concrete named failure mode — 'errors may occur' does not qualify" mandated for every stage.

**C-04 PASS** — Input schema, transformations (field-level), and output schema required per stage; `verified: no field added, removed, renamed, or retyped` required for no-change stages.

**C-05 PASS** — Latency annotation required per stage with value/range/characterization options.

**C-06 PASS** — SECTION 5 requires running accumulation, threshold comparison, and both normal-operation and worst-case scenarios addressed separately.

**C-07 PASS** — DOMAIN CONTEXT declares VendorRequest, LegalEntityRecord, TaxIdentityRecord, BankingDetailRecord, PaymentTermsProfile, VendorMasterRecord; entity vocabulary precedes stage trace.

**C-08 PASS** — SECTION 6 requires paired prescription for every `no handling` annotation and every named loss point; specific mechanism required; generic advice disqualified.

**C-09 PASS** — SECTION 7 requires named alternative, ≥2 trade-off dimensions, one quantified comparison against INCUMBENT TOTAL.

**C-10 PASS** — DOMAIN CONTEXT section appears before SECTION 3 (stage trace); entity vocabulary declared before first stage.

**C-11 PASS** — "Label all boundaries: B1->2, B2->3, B3->4, B4->5, B5->6" — complete inventory of five labels with B[N]->[N+1] format explicitly stated.

**C-12 PASS** — "if no change, state: `verified: no field added, removed, renamed, or retyped`" — exact token required per stage transformation entry.

**C-13 FAIL** — No structural table or protocol gate maps to C-02, C-03, or C-04. BOUNDARY CHECKS and STAGE TRACE are prose sections with listed requirements; blank or missing items are not structurally visible. The recovery section is also prose-only. No C-13 surface exists anywhere in the prompt.

**C-14 PASS** — "cite the fallback by its Manual Step column value from the SECTION 1 INCUMBENT BASELINE TABLE" — every prescription required to name a specific step (e.g., "AP coordinator collects and photocopies vendor tax forms"). Vendor-domain examples ground the mandate.

**C-15 PASS (floor)** — Three-column table (Manual Step | Actor | Elapsed Time) explicitly templated. Meets minimum exactly: step name serves as identifier, Actor = responsible role, Elapsed Time = frequency. Five distinct vendor-specific steps required. Minimal form: no Step ID column, citation target is name-only.

**C-16 PASS (name-based, lower precision)** — "every recovery entry must carry a named step citation" — all entries mandated. Citation target is Manual Step column value. Names can be paraphrased; no ID format to prevent ambiguity. Weakest C-16 enforcement among all five variations.

**Score:**
- Essential: 4/4 × 60 = 60
- Recommended: 3/3 × 30 = 30
- Aspirational: 8/9 × 10 = **8.89**
- **Composite: 98.89**
- All essential pass: YES — Golden threshold: MET

---

#### V-02 — Recovery Citation Structure: Recovery Audit Table with Baseline Step Column

**C-01 PASS** — Six stages (RMA → physical receipt → condition assessment → inventory reinstatement → credit memo → account adjustment) with input/output schema per stage.

**C-02 PASS** — BOUNDARY TABLE provides pre-populated rows for B1->2 through B5->6 with Error Handling column; blank cell = structural gap. "No handling — risk accepted" option explicit.

**C-03 PASS** — Loss point required per stage with "concrete named failure" mandate; generic disqualified.

**C-04 PASS** — Input schema, transformations, output schema per stage; `verified: no field added, removed, renamed, or retyped` for no-change stages.

**C-05 PASS** — Latency required per stage and as Boundary Latency column in BOUNDARY TABLE.

**C-06 PASS** — STALE ANALYSIS with threshold from DOMAIN CONTEXT; two scenarios (normal, worst-case) with FRESH/STALE verdict.

**C-07 PASS** — Entity vocabulary (ReturnRequest, RMARecord, PhysicalReturnReceipt, ConditionAssessment, InventoryReinstatement, CreditMemo, CustomerAccountAdjustment) declared; BOUNDARY TABLE has "Entity at Risk" column that must cite domain entities — "data" or "records" disqualified.

**C-08 PASS** — RECOVERY AUDIT TABLE requires one row per `no handling` entry and one row per named loss point; Recovery Mechanism column required with specific mechanism; generic advice disqualified.

**C-09 PASS** — TRADE-OFF ANALYSIS requires named alternative, ≥2 dimensions, one comparing automated elapsed against INCUMBENT TOTAL.

**C-10 PASS** — DOMAIN CONTEXT declared before STAGE TRACE; entity vocabulary established first.

**C-11 PASS** — BOUNDARY TABLE rows are B1->2 through B5->6 — structurally enumerated inventory; every row must carry the label.

**C-12 PASS** — `verified: no field added, removed, renamed, or retyped` mandated for no-change transformations.

**C-13 PASS** — BOUNDARY TABLE maps to C-02: five pre-populated rows, blank cell in Error Handling column is structurally visible. Also RECOVERY AUDIT TABLE is structural (though it maps to C-08, not C-02/03/04). C-13 satisfied by the BOUNDARY TABLE alone.

**C-14 PASS** — "Baseline Step Cited column rule: cite the exact Manual Step column value from the INCUMBENT BASELINE TABLE" — named step required per recovery row; "manual review" without table row name fails.

**C-15 PASS (standard)** — Four-column table (Manual Step | Actor | Duration | Entity Handled) — exceeds minimum: step name + actor + time + entity. Returns-domain-specific examples required. No Step ID column; citation target is step name.

**C-16 PASS (structural enforcement, name-based)** — "Every row must carry a citation — a blank Baseline Step Cited cell is a structural gap for C-16." Enforcement surface is the recovery table itself: blank cell is co-located with the mechanism description. Higher compliance enforcement than V-01's prose mandate; every violation is immediately visible. Name-based citation (not ID-based) means paraphrase ambiguity remains, but structural blank-cell detection compensates.

**Score:**
- Essential: 4/4 × 60 = 60
- Recommended: 3/3 × 30 = 30
- Aspirational: 9/9 × 10 = **10**
- **Composite: 100**
- All essential pass: YES — Golden threshold: MET

---

#### V-03 — Step ID Precision: Numbered Incumbent Baseline Identifiers

**C-01 PASS** — Six stages (contract activation → usage metering → invoice generation → payment collection → dispute resolution → cash application) with input/output schema per stage; entity vocabulary includes ContractRecord through RevenueLedgerPosting.

**C-02 PASS** — SECTION 4 labels B1->2 through B5->6 with named mechanism or `no handling — risk accepted` required per boundary.

**C-03 PASS** — "Loss point: concrete named failure" required per stage; generic disqualified.

**C-04 PASS** — Input schema, transformations (field-level), output schema per stage; `verified: no field added, removed, renamed, or retyped` required.

**C-05 PASS** — Latency annotation required per stage.

**C-06 PASS** — SECTION 5 stale analysis with running accumulation, two scenarios compared against declared threshold.

**C-07 PASS** — Entity vocabulary (ContractRecord, UsageMeteringEvent, InvoiceRecord, PaymentRecord, DisputeRecord, CashApplicationEntry, RevenueLedgerPosting) declared in SECTION 2; domain-specific terms appear throughout stage trace.

**C-08 PASS** — SECTION 6 requires paired prescription for every `no handling` annotation and every loss point; specific mechanism required.

**C-09 PASS** — SECTION 7 requires named alternative, ≥2 trade-off dimensions, one comparison against INCUMBENT TOTAL.

**C-10 PASS** — SECTION 2 (entity vocabulary) appears before SECTION 3 (stage trace); entities declared first.

**C-11 PASS** — "Label all boundaries: B1->2, B2->3, B3->4, B4->5, B5->6" — complete B[N]->[N+1] inventory.

**C-12 PASS** — `verified: no field added, removed, renamed, or retyped` required for no-change stages.

**C-13 FAIL** — BOUNDARY CHECKS is a prose section (not a table or gate) listing requirements. STAGE TRACE is also prose-listed. No structural table or inline protocol gate where missing items are visible as blank cells or absent gate blocks. The mandate is strong but the enforcement is register-only, not structural. Same failure mode as V-01.

**C-14 PASS** — "cite by its Step ID (MS-NN format)... A recovery prescription that describes step content without citing the Step ID does not satisfy C-16" — names the pre-automation process at step-ID granularity. Domain-specific example (MS-01: "Finance analyst exports usage data from billing spreadsheet") grounds the mandate.

**C-15 PASS (extended)** — Four-column table with Step ID column (Step ID | Manual Step | Actor | Duration); MS-NN format required for each row. Exceeds minimum: adds machine-verifiable identifier to name, actor, and duration. Highest C-15 depth among variations without a recovery table.

**C-16 PASS (ID-verifiable, highest precision without table)** — "Every recovery entry must carry a Step ID citation" — MS-NN format required; paraphrase prevention built in. A prescription either contains "MS-03" or it does not — no interpretation required. Weaker enforcement than V-02/V-05 (no structural blank-cell detection) but highest citation precision among prose-mandate variations.

**Score:**
- Essential: 4/4 × 60 = 60
- Recommended: 3/3 × 30 = 30
- Aspirational: 8/9 × 10 = **8.89**
- **Composite: 98.89**
- All essential pass: YES — Golden threshold: MET

---

#### V-04 — Phrasing Register: Hard Imperative + Per-Entry Positional Citation Mandate

**C-01 PASS** — Six stages (renewal trigger → entitlement reactivation → proration → invoice → payment retry → confirmation posting) with five-item per-stage requirements; "You may not skip a section" enforces lineage completeness.

**C-02 PASS** — Inline BOUNDARY GATE per stage requires error handling item (a); `no handling — risk accepted [B[N]->[N+1]]` as exact fallback token. "A gate with any item missing is a protocol failure."

**C-03 PASS** — "Loss point: a concrete named failure mode as it would appear in an incident report — 'errors may occur' fails" — more specific standard than other variations.

**C-04 PASS** — Input schema (item 1), transformations (item 2, exact token required for no-change), output schema (item 3) per stage; omitting any item is a protocol failure.

**C-05 PASS** — "Latency: value, range, or characterization — silence fails" (item 4 per stage).

**C-06 PASS** — STALE ANALYSIS requires "each addend" shown, two scenarios, "state verdict using exactly the token FRESH or STALE."

**C-07 PASS** — Entity vocabulary (RenewalTrigger, EntitlementRecord, ProrationCalculation, RenewalInvoice, PaymentAttempt, RenewalConfirmation) declared in DOMAIN CONTEXT; all entities domain-specific.

**C-08 PASS** — "For every `no handling — risk accepted` gate annotation and every named loss point... you must provide a paired recovery prescription."

**C-09 PASS** — "You must name an alternative... You must state at least two trade-off dimensions. At least one must compare against the INCUMBENT TOTAL."

**C-10 PASS** — DOMAIN CONTEXT section (entity vocabulary + staleness threshold) appears before STAGE TRACE WITH INLINE BOUNDARY GATES.

**C-11 PASS** — Inline gates explicitly labeled B1->2 through B5->6 with per-gate label requirements; "Use label B[N]->[N+1] in every annotation" in each gate instruction.

**C-12 PASS** — "you must state exactly: `verified: no field added, removed, renamed, or retyped`" for no-change stages; hard imperative elevates requirement clarity.

**C-13 PASS** — Inline BOUNDARY GATE is a protocol gate where missing items are stated as "protocol failures." Gate structure maps directly to C-02 (boundary error handling). Gate requirement: "(a) Error handling: ... (b) Boundary latency: ... (c) Schema continuity: ..." — any missing item is a visible structural failure. "Stage N does not open until BOUNDARY GATE B[N-1]->[N] is fully stated" creates positional enforcement.

**C-14 PASS** — Recovery entry structure requires "Fallback: [Step ID in MS-NN format] — [Manual Step value from INCUMBENT BASELINE TABLE]" — named pre-automation step required; "generic terms such as 'manual review' without a Step ID are protocol failures."

**C-15 PASS (extended)** — Four-column table with Step ID (Step ID | Manual Step | Actor | Duration); MS-NN format required for all rows; subscription-renewal-specific examples required.

**C-16 PASS (positional mandate, ID-verifiable)** — "Every recovery entry must carry a Fallback line — entries without one are protocol failures." Positional enforcement: the Fallback item (Step ID citation) must appear as item 2 in a three-part required structure, before the mechanism description. Position-verifiable: a recovery entry either has a Fallback line second or it structurally fails. Combined with MS-NN format, citation is both positional and ID-verifiable.

**Score:**
- Essential: 4/4 × 60 = 60
- Recommended: 3/3 × 30 = 30
- Aspirational: 9/9 × 10 = **10**
- **Composite: 100**
- All essential pass: YES — Golden threshold: MET

---

#### V-05 — Combined: Step IDs + Recovery Audit Table + Per-Entry Mandate + Schema-Diff Tables

**C-01 PASS** — Six stages (standard cost update → PO cost adjustment → inventory revaluation → COGS recalculation → variance posting/GL reconciliation) with per-stage schema-diff tables creating explicit entry/exit schema at each hand-off; entity chain (StandardCostRecord → PurchaseOrderLine → InventoryLot → COGSRecord → CostVariance → GLCostEntry) spans all stages.

**C-02 PASS** — Inline BOUNDARY GATE per stage (Steps 2–5) with three required items; `no handling — risk accepted [B[N]->[N+1]]` as exact token; "a gate with any item missing is a structural gap."

**C-03 PASS** — "Loss point: concrete named failure" required per stage after schema-diff table; appears as a mandatory standalone item.

**C-04 PASS** — Per-stage schema-diff table (Field | Entry Schema | Transformations | Exit Schema) — each field row has its own Transformations cell; "a blank Transformations cell is a structural gap visible without reading stage prose." Strongest C-04 enforcement across all variations: violations visible at field level, not just stage level.

**C-05 PASS** — Latency annotation after schema-diff table per stage; also Boundary latency as item (b) per gate.

**C-06 PASS** — STEP 7 STALE ANALYSIS shows addend-by-addend accumulation after each stage and boundary; two scenarios with exact FRESH/STALE tokens required.

**C-07 PASS** — Entity vocabulary (StandardCostRecord, PurchaseOrderLine, InventoryLot, COGSRecord, CostVariance, GLCostEntry) declared in STEP 1; domain-specific entity names (not "data" or "records") required in recovery audit table's "Named Entity Protected" column.

**C-08 PASS** — RECOVERY AUDIT TABLE (STEP 8) requires one row per `no handling` gate annotation and one row per named loss point; Recovery Mechanism column required; generic advice explicitly disqualified; blank cell in any of six columns is a structural gap.

**C-09 PASS** — STEP 9 requires named alternative cost revaluation architecture, ≥2 trade-off dimensions, one comparison against INCUMBENT TOTAL from STEP 0.

**C-10 PASS** — STEP 1 (DOMAIN CONTEXT) appears before STEP 2 (first stage); entity vocabulary declared in STEP 1 before any stage or schema-diff content.

**C-11 PASS** — Inline gates labeled B1->2 through B4->5 (five stages, four inter-stage gates plus the terminal stage at Step 6 with no outbound gate). All B[N]->[N+1] labels explicitly required in gate items; complete gate inventory structurally embedded in stage ordering.

**C-12 PASS** — Schema-diff table Transformations cell rule: "if no change for a field, write exactly: `verified: no field added, removed, renamed, or retyped`. A blank cell or bare 'unchanged' fails." Applied per field, per stage — strongest C-12 enforcement; `verified` assertion is required at field granularity rather than stage granularity.

**C-13 PASS** — Three structural surfaces, all mapping to scorable essential criteria:
1. Schema-diff tables (maps to C-04): blank Transformations cell = visible field-level gap
2. Inline BOUNDARY GATES (maps to C-02): missing gate item = structural gap
3. RECOVERY AUDIT TABLE (maps to C-08 via C-03/C-02): blank cell in any of six columns = visible gap

**C-14 PASS** — Recovery audit table requires "Manual Step Cited" column with "exact Manual Step column value from STEP 0, verbatim" — named pre-automation step required, verbatim. Cost-revaluation-specific examples ground the mandate (e.g., "Cost accountant exports current standard costs from ERP to spreadsheet").

**C-15 PASS (extended)** — Four-column table with Step ID (Step ID | Manual Step | Actor | Duration); MS-NN format required exactly; five cost-revaluation-specific steps minimum. "This table and its INCUMBENT TOTAL are the sole authority" — table given canonical status.

**C-16 PASS (maximum enforcement)** — Two separate citation columns in recovery audit table: "Step ID Cited (MS-NN from STEP 0)" AND "Manual Step Cited (exact value from STEP 0)." Every row must carry both. "A blank cell in either citation column is a visible, scorable C-16 gap." Combines ID-verifiable precision (Step ID Cited, substring-checkable) with verbatim name (Manual Step Cited, paraphrase-prevention). Dual-column enforcement is highest C-16 compliance surface across all R5 variations.

**Score:**
- Essential: 4/4 × 60 = 60
- Recommended: 3/3 × 30 = 30
- Aspirational: 9/9 × 10 = **10**
- **Composite: 100**
- All essential pass: YES — Golden threshold: MET

---

### Composite Scores and Ranking

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| 1 | **V-05** | **100** | YES | Quadruple structural enforcement; dual citation columns; schema-diff tables; highest C-12, C-13, C-15, C-16 depth |
| 2 | **V-04** | **100** | YES | Positional citation mandate + inline gates + Step IDs; strong C-13 (gate) and C-16 (position-verifiable); no recovery table |
| 3 | **V-02** | **100** | YES | Recovery audit table enforces C-16 structurally; strong C-13 (boundary table + recovery table); name-based citation only |
| 4 | **V-03** | 98.89 | YES | Highest citation precision (MS-NN IDs) among no-table variations; C-13 FAIL (prose boundary checks) |
| 5 | **V-01** | 98.89 | YES | C-15 floor (3-col); name-based C-16 citation; C-13 FAIL (no structural surface); weakest C-16 enforcement |

V-02, V-04, V-05 all achieve perfect composite (100). V-03 and V-01 tie at 98.89, both failing C-13 — neither provides a structural table or gate that maps to C-02, C-03, or C-04.

**Tiebreaker (V-03 vs V-01):** V-03 has ID-verifiable C-16 citations (MS-NN format) and a stronger C-15 (4-col + Step ID) vs V-01's name-only, 3-col minimum. V-03 is qualitatively superior despite the same composite.

---

### Excellence Signals from V-05 (Top Scorer)

**Signal 1 — Dual citation columns (Step ID + verbatim Manual Step)**
V-05's recovery audit table requires both a "Step ID Cited (MS-NN)" column and a "Manual Step Cited (exact value)" column on every row. This goes beyond R4's V-03/V-05 pattern (per-row citation) and beyond V-02/V-03 within R5 (single citation column). The dual-column design closes two independent failure modes: (a) an ID-without-name citation that orphans the reference from human-readable context, and (b) a name-without-ID citation that allows paraphrase to satisfy the letter but not the verifiability test. The structural gap (blank cell) is checkable in either column independently.

**Signal 2 — Per-field schema-diff tables**
Prior rounds tracked schema at stage level. V-05's schema-diff table (Field | Entry Schema | Transformations | Exit Schema) tracks each field individually: a field that changes without a Transformations entry is a blank cell — visible without reading prose. This makes C-04 violations addressable at field granularity rather than stage granularity, and C-12 (`verified: no change`) applies per field rather than per stage. The Transformations cell rule ("blank cell or bare 'unchanged' fails") is the per-field analogue of C-12's stage-level verified-unchanged assertion.

**Signal 3 — Three structural surfaces covering three distinct required-section types**
V-05 accumulates three structural surfaces (schema-diff tables → C-04, inline gates → C-02, recovery audit table → C-08/C-03), each mapping to a different scorable requirement. V-02 achieves two surfaces (boundary table → C-02, recovery table → C-08). V-04 achieves one gate surface (→ C-02). The quadruple-scaffolding coherence test confirms that structural density at this level does not crowd out essential coverage — all four essential criteria pass at equal strength to simpler variations.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual citation columns in recovery audit table (Step ID Cited in MS-NN format + Manual Step Cited verbatim in separate columns) creates two independent C-16 verification surfaces: ID column is substring-verifiable, name column prevents orphaned references; blank in either column is a visible scorable gap", "Per-field schema-diff tables (Field | Entry Schema | Transformations | Exit Schema) make C-04 and C-12 violations visible at field granularity — a field that changes without a Transformations entry is a blank cell detectable without reading prose, elevating verified-unchanged assertion from stage-level to field-level"]}
```
