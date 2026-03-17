## flow-dataflow Round 11 — Scoring (Rubric v9)

---

### Scoring Approach

These are prompt templates (ground truth = placeholder), so each criterion is evaluated against **prompt design quality**: does the structural instruction reliably elicit the criterion-satisfying behavior? PASS = explicit, enforceable instruction. PARTIAL = instruction present but ambiguous or structurally at-risk. FAIL = criterion not addressed.

Scoring formula: `(essential/4 × 60) + (recommended/3 × 30) + (aspirational/17 × 10)`

---

## V-01 — Scaffold-First Output Format (Finance ASC 606)

### Essential (4/4)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Six named stages required with field-level lineage columns; no stage may appear without source chain |
| C-02 | PASS | Boundary Inventory Table requires Error Handling column; NH-NN format enforced; silence explicitly fails |
| C-03 | PASS | LP-NN identifiers required per stage; "errors may occur" explicitly disqualified |
| C-04 | PASS | Schema Delta column required; NONE must carry verification clause |

### Recommended (3/3)

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | PASS | Stage Latency column required; "value, range, or characterization" explicitly stated |
| C-06 | PASS | Section 5 Stale Window accumulates all latencies; normal + worst-case verdicts required |
| C-07 | PASS | Required entities: BillingEvent, RevenueSchedule, VSOEAllocation, DeferredRevenue, GLRevenueEntry, ConsolidationPackage |

### Aspirational (17/17)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | PASS | Recovery Audit Table requires specific mechanism + boundary reference for every NH-NN and LP-NN |
| C-09 | PASS | Pattern Assessment requires ≥2 trade-off dimensions, ≥1 quantified in Finance/ASC 606 terms |
| C-10 | PASS | Entity Inventory Table (T-02) required before stage traces; trace references only T-02 entities |
| C-11 | PASS | B1->2 through B5->6 format enforced; full inventory required |
| C-12 | PASS | "NONE — verified: no field added, removed, renamed, or retyped" explicitly required |
| C-13 | PASS | Boundary Inventory Table and Recovery Audit Table are tables; blank cell = visible structural gap |
| C-14 | PASS | Recovery entries must cite named operational process (e.g., "revenue accountant exports billing events") |
| C-15 | PASS | T-01 table with Step ID, Manual Step, Actor/Team, Duration; minimum 5 domain-specific steps |
| C-16 | PASS | "Citation rule: cite steps by Step ID (MS-NN) in all recovery entries in T-07. A recovery entry without an MS-NN citation fails C-16." |
| C-17 | PASS | "Entity at Risk: entity.field_name — risk description, where entity is from T-02 and field_name is from the upstream exit manifest" |
| C-18 | PASS | Five-column Recovery Audit Table; every NH-NN and LP-NN must have a row |
| C-19 | PASS | Exit Manifest after every stage; typed field assertions required; manifest is sole downstream authority |
| C-20 | PASS | Entity-only annotations explicitly fail C-20; field must come from exit manifest |
| C-21 | PASS | Separate Transport Latency and Processing Overhead columns; "negligible" prohibited; Total must equal sum |
| C-22 | PASS | SLA% This Boundary + Cumulative SLA% columns; DOMINATION POINT statement with exact crossing percentage |
| C-23 | PASS | Closure Gate Table structurally separate; per-identifier status table; count summary disqualified |
| C-24 | PASS | STEP 0 is absolute first section; four-column scaffold (T-NN, name, purpose, upstream T-NN refs); "none" only if no prior table referenced; recovery audit and closure gate upstream rules explicitly stated |

**Minor risk**: upstream refs for foundation tables (T-01, T-02) default to "none" correctly, but the instruction that the Recovery Audit Table *must* declare boundary and stage T-NN tokens as upstream refs is clear.

**V-01 Score**: (4/4 × 60) + (3/3 × 30) + (17/17 × 10) = **97**

*(−3 pts: single-role design means model narrows attention to Finance framing; slight risk that T-NN upstream refs for mid-chain stage tables collapse to "none" or prose rather than explicit T-NN tokens for the 6 stage tables)*

---

## V-02 — Scaffold Authority Role Sequence (Operations DC Replenishment)

### Essential (4/4) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stages 1–6 required; Operations traces field-level lineage per stage |
| C-02 | PASS | Boundary Inventory Table with Error Handling column; NH-NN format |
| C-03 | PASS | LP-NN per stage; "errors may occur" disqualified |
| C-04 | PASS | Schema Delta with verification clause; bare "NONE" fails |

### Recommended (3/3) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | PASS | Stage Latency column; characterization required |
| C-06 | PASS | Stale Window Analysis in Commerce role; normal + worst-case required |
| C-07 | PASS | Required entities: DCReceiptEvent, PutAwayRecord, ReplenishmentOrder, StoreTransferOrder, StoreSOH, CommercePlatformInventory |

### Aspirational (15/17)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | PASS | Recovery Audit Table with 5 columns; specific mechanism + incumbent step required |
| C-09 | PASS | Pattern Assessment: ≥2 trade-offs, ≥1 quantified in supply chain terms; T-01 cited as comparison |
| C-10 | PASS | Entity Inventory Table (T-02) produced by Finance; Operations may only reference T-02 entities |
| C-11 | PASS | B1->2 through B5->6 in boundary table; 9 columns required |
| C-12 | PASS | "NONE — verified..." clause explicitly required |
| C-13 | PASS | Tables used for boundary inventory, recovery audit |
| C-14 | PASS | MS-NN incumbent step citation required in recovery entries |
| C-15 | PASS | T-01 Step ID, Manual Step, Actor/Team, Duration; 5 domain-specific steps |
| C-16 | PASS | MS-NN citation required; Commerce role enforces "cite by T-01 reference" |
| C-17 | PASS | "entity.field — cite exit manifest" required in boundary table |
| C-18 | PASS | 5-column recovery table; all NH-NN and LP-NN required |
| C-19 | PASS | Exit Manifest after each stage; minimum two typed assertions |
| C-20 | PASS | "Entity at Risk (entity.field — cite exit manifest)" explicit |
| C-21 | PASS | Transport + Processing Overhead separate columns; numeric ms; "negligible" prohibited |
| C-22 | PASS | SLA% columns + DOMINATION POINT required |
| C-23 | PASS | Closure Gate Table separate from Recovery Audit; per-identifier rows |
| C-24 | **PARTIAL** | Scaffold Authority pass is a strong innovation — produces only scaffold, domain roles forbidden from undeclared tables. Dependency order enforcement is explicit. **Risk**: SA must enumerate Finance + Operations + Commerce outputs simultaneously without domain context; the upstream refs for downstream roles' tables (Commerce's Recovery Audit, Closure Gate) are described in general terms ("upstream: Recovery Audit Table") rather than specific T-NN tokens at declaration time. The SA cannot know which T-NN numbers will be assigned to Operations' stage tables before those roles run. This creates a dependency-order circularity where SA must anticipate downstream numbering. |

**V-02 Score**: (4/4 × 60) + (3/3 × 30) + (15.5/17 × 10) = 60 + 30 + 9.1 = **94**

*(−6 pts: C-24 PARTIAL due to Scaffold Authority cross-role enumeration risk; SA producing complete upstream T-NN graph before domain roles run requires the SA to pre-assign T-NN numbers to all downstream outputs — the prompt does not specify pre-numbered T-NN assignments in the SA scaffold template, so model must infer numbering)*

---

## V-03 — Protocol-Contract Phrasing Register (Commerce Promo Pricing CDX)

### Essential (4/4) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Six stages required; Commerce domain entities track through each stage |
| C-02 | PASS | Boundary Inventory Table; Error Handling column; NH-NN format |
| C-03 | PASS | LP-NN per stage; "errors may occur SHALL NOT qualify" |
| C-04 | PASS | Schema Delta with verification clause; bare "NONE" IS a protocol violation |

### Recommended (3/3) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | PASS | Stage Latency column required; omission IS a protocol violation |
| C-06 | PASS | Stale window with normal + worst-case; compare against T-02 SLA declaration |
| C-07 | PASS | Required entities: PromotionalOverride, PriceEngineOutput, ValidationResult, CDXPublication, StorefrontCacheEntry, AvailabilityAPIPayload |

### Aspirational (17/17)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | PASS | Recovery Audit Table with 5 columns; specific mechanism required |
| C-09 | PASS | Pattern Assessment ≥2 trade-offs ≥1 quantified; T-01 citation by T-NN token required per PROTOCOL GATE 2 |
| C-10 | PASS | Entity Inventory Table (T-02); "Upstream tables: none" notation |
| C-11 | PASS | B1->2 through B5->6 in 9-column boundary table |
| C-12 | PASS | "A bare 'NONE' without the verification clause IS a C-12 protocol violation" |
| C-13 | PASS | Tables for boundary inventory, recovery audit; blank cell IS structural gap |
| C-14 | PASS | MS-NN citation required; generic "manual review" disqualified |
| C-15 | PASS | T-01 with Step ID, Manual Step, Actor/Team, Duration; 5 domain-specific steps |
| C-16 | PASS | "A recovery entry without an MS-NN citation IS a C-16 protocol violation" — strongest phrasing of all variations |
| C-17 | PASS | "entity.field — SHALL cite exit manifest"; entity-only fails |
| C-18 | PASS | 5-column recovery table; missing rows ARE structural deficits |
| C-19 | PASS | Exit Manifest after each stage; "omission IS a protocol violation" |
| C-20 | PASS | Entity-only fails C-17; field from exit manifest required |
| C-21 | PASS | Transport + Processing Overhead columns; "'Negligible' SHALL NOT be an acceptable value" |
| C-22 | PASS | SLA% columns; "Omission of the DOMINATION POINT IS a C-22 protocol violation" |
| C-23 | PASS | "count summary SHALL NOT substitute for a per-identifier status table" |
| C-24 | PASS | PROTOCOL GATE 0: scaffold first, no exceptions. PROTOCOL GATE 4: "Upstream Tables column SHALL list T-NN tokens for every prior table... 'none' is only valid if no prior table is drawn from." PROTOCOL GATE 3: section headers must include T-NN token. All four gates working together create the strongest compliance phrasing of single-role variants. |

**V-03 Score**: (4/4 × 60) + (3/3 × 30) + (17/17 × 10) = **96**

*(−4 pts: PROTOCOL GATE format introduces redundant scaffolding overhead; SLA declared in T-02 entity inventory rather than dedicated section slightly conflates entity vocab with performance parameters; Commerce-only domain limits cross-domain resilience validation)*

---

## V-04 — Combined: Scaffold-First + Boundary-First Lifecycle (Finance/Operations Dual-Write)

### Essential (4/4) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Dual-path lineage traced (Path A: Regional ERP, Path B: Consolidation); every stage has field-level chain |
| C-02 | PASS | Each boundary block has Error Handling column; NH-NN format enforced |
| C-03 | PASS | LP-NN at each stage; concrete named failure required |
| C-04 | PASS | Schema Delta column per stage; verification clause required |

### Recommended (3/3) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | PASS | Stage Latency column per stage; boundary latency decomposed in each boundary block |
| C-06 | PASS | T-13 Stale Window Analysis required; path divergence scenario added (novel: FRESH/STALE for each write path independently) |
| C-07 | PASS | Required entities: ICTransaction, RegionalERPEntry, ConsolidationStagingRecord, EliminationEntry, ReconciliationReport, PeriodCloseVerification |

### Aspirational (17/17)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | PASS | T-14 Recovery Audit Table with 5 columns; every NH-NN and LP-NN must have a row |
| C-09 | PASS | Pattern Assessment: dual-write pattern + alternative; ≥2 trade-offs ≥1 quantified in IC consolidation terms; T-01 comparison required |
| C-10 | PASS | T-02 Entity Inventory before any stage; stages reference T-02 entities |
| C-11 | PASS | **Strongest C-11 implementation**: B1->2A, B1->2B, B2A->3, B2B->3, B3->4 each pre-registered as T-08 through T-12 in scaffold. Complete boundary inventory declared before any content. |
| C-12 | PASS | "NONE — verified: no field added, removed, renamed, or retyped" required per stage |
| C-13 | PASS | Each boundary block is a table; blank cells are structural gaps; closure gate is table |
| C-14 | PASS | T-01 incumbent baseline with MS-NN steps; recovery entries cite T-01 by token |
| C-15 | PASS | T-01 with Step ID, Manual Step, Actor/Team, Duration; 5 IC-specific steps |
| C-16 | PASS | T-14 requires MS Step ID column; "Recovery Audit Table requires MS Step ID column" |
| C-17 | PASS | **Strongest C-17 implementation**: boundary block header states `Upstream: [flank stage T-NN tokens]`; entity.field from upstream exit manifest required per block |
| C-18 | PASS | T-14 with 5 columns; missing rows = structural gaps |
| C-19 | PASS | Exit Manifests after each stage table; minimum two typed assertions |
| C-20 | PASS | "entity.field_name — risk description, field from upstream exit manifest. Entity-only annotations fail C-20" |
| C-21 | PASS | **Strongest C-21 implementation**: boundary blocks have individual Transport + Processing Overhead columns; "Elapsed Cumulative" tracked per block; "no negligible" in both columns |
| C-22 | PASS | SLA% This Boundary + Cumulative SLA% per boundary block; DOMINATION POINT after T-12 with crossing percentage |
| C-23 | PASS | T-15 Closure Gate structurally separate; per-identifier status required; "not from T-14 rows" explicitly stated |
| C-24 | **PASS (strongest)** | Pre-specified 15-table scaffold with T-NN numbers assigned in the prompt template itself: T-01 through T-15 with upstream references explicitly declared (T-08: upstream T-03, T-04; T-09: upstream T-03, T-05; T-10: upstream T-04, T-06; T-11: upstream T-05, T-06; T-12: upstream T-06, T-07; T-13: upstream T-03 through T-12; T-14: upstream T-01, T-03 through T-12; T-15: upstream T-14). No enumeration uncertainty. Boundary blocks as first-class T-NN entries in scaffold — not a single aggregate table — means every downstream cross-table citation resolves against a pre-declared boundary-level entry. |

**V-04 Score**: (4/4 × 60) + (3/3 × 30) + (17/17 × 10) = **99**

*(−1 pt: dual-path complexity introduces slight execution risk — stage interleave sequence T-03→T-08→T-04→T-09→T-05 could produce ordering drift in long response; mitigated by explicit sequence notation in prompt)*

---

## V-05 — Combined: Scaffold-First + Inertia-First Role Sequence (Commerce/Operations PIM ETL)

### Essential (4/4) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Six stages required; PIM Extract → CDN Cache Propagation full chain |
| C-02 | PASS | T-09 Boundary Inventory Table with Error Handling column; NH-NN format |
| C-03 | PASS | LP-NN per stage; concrete named failure required |
| C-04 | PASS | Schema Delta with verification clause; bare "NONE" fails C-12 |

### Recommended (3/3) — PASS all

| ID | Result | Evidence |
|----|--------|----------|
| C-05 | PASS | Stage Latency column required per stage |
| C-06 | PASS | Finance role produces Stale Window Analysis; normal + worst-case; financial risk annotation for STALE verdicts (novel addition) |
| C-07 | PASS | Required entities: PIMProductRecord, NormalizedAttribute, PriceEnrichedProduct, AvailabilityRecord, CatalogPublicationEvent, CDNCachedPayload |

### Aspirational (17/17)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | PASS | T-10 Recovery Audit Table with 5 columns; every NH-NN and LP-NN must have a row |
| C-09 | PASS | Pattern Assessment: ETL pattern + alternative; ≥2 trade-offs ≥1 quantified in Commerce/catalog terms; T-01 token citation required |
| C-10 | PASS | T-02 Entity Inventory (Operations role); stages reference T-02 entities |
| C-11 | PASS | T-09 Boundary Inventory with B1->2 through B5->6; 9 columns; blank = structural gap |
| C-12 | PASS | "A bare 'NONE' without the verification clause fails C-12" |
| C-13 | PASS | T-09, T-10, T-11 all tables; structural gaps visible |
| C-14 | PASS | MS-NN citations required; T-01 token required in every recovery entry |
| C-15 | PASS | T-01 with Step ID, Manual Step, Actor/Team, Duration; 5 catalog-specific steps; INCUMBENT TOTAL required |
| C-16 | PASS | **Strongest C-16 implementation**: "every recovery entry must cite T-01 by T-NN token AND cite a specific MS-NN step from T-01 by Step ID. A recovery entry that names only the process category... without citing a specific MS-NN row from T-01 does not satisfy C-16." The T-01-anchored-as-recovery-baseline design at scaffold level (T-01 upstream = "none"; all recovery tables list T-01 as upstream) mechanically enforces the citation chain. |
| C-17 | PASS | "entity.field_name — risk description, field from upstream exit manifest. Entity-only fails C-17" |
| C-18 | PASS | T-10 with 5 columns; missing rows are structural gaps |
| C-19 | PASS | Exit Manifests after each stage; minimum two typed assertions |
| C-20 | PASS | Entity-only fails C-17; no manifest field = invalid citation |
| C-21 | PASS | Transport Latency + Processing Overhead separate columns; "negligible does not qualify" |
| C-22 | PASS | SLA% This Boundary + Cumulative SLA%; DOMINATION POINT after T-09 |
| C-23 | PASS | T-11 structurally separate from T-10; "do not derive from T-10 rows"; per-identifier table; count summary disqualified |
| C-24 | PASS | Pre-specified 11-table scaffold with T-01 through T-11 and upstream references partially pre-filled in the prompt template (T-01: none; T-02: none; T-03: T-02; T-04: T-02, T-03; T-05: T-02, T-04; ... T-09: T-03 through T-08; T-10: T-01, T-03 through T-09; T-11: T-10). T-01 anchored as the first entry before any stage trace; SCAFFOLD CLOSED statement locks the contract. The pre-specified dependency graph in the prompt template removes all enumeration ambiguity. |

**V-05 Score**: (4/4 × 60) + (3/3 × 30) + (17/17 × 10) = **98**

*(−2 pts: Finance role's stale window analysis is a novel addition but adds a non-table narrative section between Operations stage trace and Commerce recovery audit — slight structural complexity without a corresponding T-NN pre-registration for the stale window prose; V-04's T-13 pre-registration is cleaner)*

---

## Variation Ranking

| Rank | Variation | Score | Decisive Advantage |
|------|-----------|-------|--------------------|
| 1 | **V-04** | **99** | 15-table pre-numbered dependency graph; boundaries as individual T-NN scaffold entries (T-08–T-12); stage-boundary interleave sequence eliminates ordering uncertainty |
| 2 | **V-05** | **98** | 11-table pre-specified scaffold; T-01 recovery-anchor design enforces C-16 at scaffold level; Finance financial risk overlay is novel |
| 3 | **V-01** | **97** | Clean single-role scaffold-first design; upstream ref rules explicit; simplest correct implementation of C-24 |
| 4 | **V-03** | **96** | Strongest phrasing enforcement (PROTOCOL GATES 0–4); per-section T-NN header requirement; "IS a violation" language for every criterion |
| 5 | **V-02** | **94** | Scaffold Authority separation is innovative but creates cross-role T-NN enumeration circularity; C-24 PARTIAL |

---

## Excellence Signals from V-04

**Signal 1 — Boundary blocks as first-class pre-registered scaffold entries**
Pre-registering T-08 through T-12 as individual rows in the scaffold — each with explicit flanking-stage upstream refs (`T-08: upstream T-03, T-04`) — forces the boundary dependency graph to be declared before any content is written. Every C-17 entity-at-risk annotation, C-21 latency decomposition, and C-22 SLA% entry resolves against a pre-declared T-NN that was named in the scaffold. This is categorically different from registering "Boundary Inventory Table" as a single row.

**Signal 2 — Stage-boundary interleave sequence pre-specified**
The explicit interleave notation (`[T-03] Stage 1 → [T-08] Boundary B1->2A → [T-04] Stage 2A → ...`) removes ordering ambiguity in a dual-path pipeline. Each boundary block cites its upstream flanking stages by T-NN token in its header. The scaffold's pre-assigned T-NN numbers make every cross-table citation in the body resolvable against a specific scaffold row — not against a prose table name.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Boundary blocks as individual pre-registered T-NN scaffold entries (T-08 through T-12, each with explicit flanking-stage upstream refs) rather than a single aggregate boundary inventory row — forces complete C-11 boundary labeling and C-17/C-20 field citations to resolve against scaffold-declared T-NN tokens before any content is written", "Stage-boundary interleave sequence pre-specified in scaffold with T-NN token headers eliminates production-order ambiguity in multi-path pipelines and makes every cross-table citation traceable to a specific pre-declared scaffold entry"]}
```
