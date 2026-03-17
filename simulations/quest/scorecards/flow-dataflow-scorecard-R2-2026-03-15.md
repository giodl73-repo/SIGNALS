# flow-dataflow Quest Score — Round 2

## Variation Evaluation

---

### V-01 — Table-First Lineage

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Table structure per entity enforces source → stage(s) → destination; entity cannot appear in later rows without an earlier row establishing origin |
| C-02 | Boundary error handling | **PASS** | "Error Handling" column is mandatory; exact fallback text "NONE — risk accepted" provided — silence has no valid form |
| C-03 | Data loss point identification | **PASS** | "Loss Points" column required per stage; explicit counter-example given ("duplicate suppression silently drops...") forecloses generic language |
| C-04 | Schema state at each stage | **PASS** | "Schema In / Schema Out" columns with "Write 'unchanged' only if you have verified no field changes" — strongest schema-diff driver of any variation |
| C-05 | Latency characterization | **PASS** | "Latency" column with "Blank is not allowed" — no escape hatch |
| C-06 | Stale data windows | **PASS** | Step 3 explicitly separates normal-operation window from failure-mode window per entity |
| C-07 | Domain framing | **PASS** | Step 1 domain inventory bans "data" / "records" before the table is even drawn |
| C-08 | Recovery prescriptions | **PASS** | Step 4 requires prescription for every "NONE" and every loss point; naming mechanism + boundary + scope |
| C-09 | Pattern trade-off analysis | **PASS** | Step 5 requires quantified trade-off using scenario's domain terms |

**Essential**: 4/4 PASS → 60 pts
**Recommended**: 3/3 PASS → 30 pts
**Aspirational**: 2/2 PASS → 10 pts
**Composite**: **100** | Golden: **YES**

---

### V-02 — Role Sequence (Finance → Operations → Commerce)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Final synthesis requires consolidated source-to-destination chain for every entity |
| C-02 | Boundary error handling | **PASS** | Commerce lens targets every boundary explicitly; "NONE — risk accepted" language included |
| C-03 | Data loss point identification | **PASS** | Operations lens requires "at least one concrete data loss point per stage" verbatim |
| C-04 | Schema state at each stage | **PARTIAL** | Finance lens flags schema changes on auditable fields only; non-Finance stages (operational routing, commerce enrichment) have no systematic schema-diff requirement — a Commerce stage altering SKU fields would pass silently |
| C-05 | Latency characterization | **PASS** | Operations lens explicitly adds latency characterization to every already-identified stage |
| C-06 | Stale data windows | **PASS** | Operations lens separates normal-operation and failure-scenario stale windows |
| C-07 | Domain framing | **PASS** | Each lens is introduced with a domain entity list; Finance names LedgerEntry/Invoice, Operations names PurchaseOrder/GoodsReceipt, Commerce names SKU/OrderLineItem |
| C-08 | Recovery prescriptions | **PASS** | Commerce lens pairs recovery prescriptions to every "NONE" and loss point |
| C-09 | Pattern trade-off analysis | **PASS** | Final synthesis requires ≥2 trade-off dimensions, one quantified |

**Essential**: 3.5/4 → 52.5 pts
**Recommended**: 3/3 → 30 pts
**Aspirational**: 2/2 → 10 pts
**Composite**: **92.5** | Golden: **NO** (C-04 not all-essential pass)

---

### V-03 — Lifecycle Emphasis (Numbered Phase Walk)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Phase 0 pipeline map + Phase 1 per-stage trace creates complete chain; entity list required before trace begins |
| C-02 | Boundary error handling | **PASS** | Phase 2 is dedicated entirely to boundary audit; boundary labels B1-2, B2-3 create a systematic checklist — strongest C-02 driver of any variation |
| C-03 | Data loss point identification | **PASS** | Phase 1 loss point requirement with counter-example ("null WarehouseCode silently drops...") explicitly disqualifies generic language |
| C-04 | Schema state at each stage | **PASS** | Phase 1 requires "Entry schema" and "Exit schema" with explicit diff: added, removed, renamed, retyped; "pass-through" must be stated explicitly |
| C-05 | Latency characterization | **PASS** | Phase 1 requires latency; "Required; do not omit" |
| C-06 | Stale data windows | **PASS** | Phase 3 is dedicated to stale data; normal-operation and failure-mode windows required per entity, with named failure condition |
| C-07 | Domain framing | **PASS** | Phase 0 entity list requires domain names before the trace can proceed |
| C-08 | Recovery prescriptions | **PASS** | Phase 4 template includes mechanism + boundary + scope + one concrete implementation detail; generic advice explicitly disqualified |
| C-09 | Pattern trade-off analysis | **PASS** | Phase 5 requires quantification or qualification in scenario domain terms |

**Essential**: 4/4 PASS → 60 pts
**Recommended**: 3/3 PASS → 30 pts
**Aspirational**: 2/2 PASS → 10 pts
**Composite**: **100** | Golden: **YES**

---

### V-04 — Conversational / Imperative (Truncated)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Questions 1–3 per stage drive schema in → transformations → schema out chain |
| C-02 | Boundary error handling | **PARTIAL** | "Audit the handoffs" section begins asking for error handling but prompt is truncated before establishing "NONE — risk accepted" fallback language or covering all boundary types |
| C-03 | Data loss point identification | **PASS** | Question 5 requires a named, specific failure mode with concrete counter-example |
| C-04 | Schema state at each stage | **PASS** | Questions 1, 2, 3 drive entry schema, transformations, exit diff per stage |
| C-05 | Latency characterization | **PASS** | Question 4 requires timing characterization |
| C-06 | Stale data windows | **FAIL** | Stale data section absent — prompt truncated before this topic is reached |
| C-07 | Domain framing | **PASS** | "Call things by their real names" with explicit entity examples; "records" or "data" without domain noun flagged |
| C-08 | Recovery prescriptions | **FAIL** | Recovery section absent — truncated |
| C-09 | Pattern trade-off analysis | **FAIL** | Pattern trade-off section absent — truncated |

**Essential**: 3.5/4 → 52.5 pts
**Recommended**: 2/3 → 20 pts
**Aspirational**: 0/2 → 0 pts
**Composite**: **72.5** | Golden: **NO**

---

## Ranking

| Rank | Variation | Composite | Golden | Decisive Differentiator |
|------|-----------|-----------|--------|------------------------|
| 1 (tie) | **V-01** | 100 | YES | Table column = rubric row; Schema In/Out with verified-unchanged rule strongest C-04 driver |
| 1 (tie) | **V-03** | 100 | YES | Boundary labels B1-2/B2-3 + dedicated Phase 2 strongest C-02 driver |
| 3 | V-02 | 92.5 | NO | C-04 gap: schema diff only enforced for Finance-auditable fields, not all stages |
| 4 | V-04 | 72.5 | NO | Prompt truncated; stale data, recovery, and pattern sections missing |

---

## Excellence Signals from Top-Scoring Variations

**Signal 1 — Table column = rubric criterion (V-01)**
Each rubric criterion maps to a mandatory table column. A blank cell is structurally visible — the analyst cannot skip schema state by not mentioning it. The column header is the enforcement.

**Signal 2 — Explicit fallback text anchoring (V-01, V-03)**
Providing the exact string "NONE — risk accepted" as the only valid non-pass value for C-02 eliminates silence as an option. Without this, the model writes "error handling varies by deployment" and C-02 fails.

**Signal 3 — Numbered boundary labels (V-03)**
Assigning B1-2, B2-3, … identifiers in Phase 0 creates a checklist that Phase 2 must complete. Each label is a named target; the analyst cannot skip a boundary by not knowing it exists.

**Signal 4 — Counter-example disqualification (V-01, V-03, V-04)**
All top variations provide an explicit bad example alongside the requirement ("Generic phrases like 'errors may occur' fail" / "Not 'network issues'"). This shapes the distribution of model outputs toward specificity.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["table-column-as-rubric-row: mapping each rubric criterion to a mandatory table column makes omission structurally visible at every cell", "fallback-text-anchoring: providing the exact NONE-risk-accepted string as the only valid non-pass value eliminates silence as a response to boundary error handling", "numbered-boundary-labels: assigning B1-2 B2-3 identifiers in the pipeline map creates a checklist that the boundary audit phase must complete entry by entry"]}
```
