# flow-dataflow — Round 10 Scoring (v9 Rubric)

> **Note:** V-03 through V-05 were not present in the input. V-02 is truncated mid-prompt (cut off after the incumbent baseline table structure). Scoring proceeds on available content. Top score is determined from V-01 (complete) and V-02 (partial).

---

## V-01 — Scaffold-First, Complete Table Inventory

**Hypothesis:** Pre-declaring every output table before any trace content enforces structural completeness and makes all cross-table citations navigable from line one.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Section 3 requires "Input: entities entering (cite T-02 names)" and explicit transformation description; entities flow from T-02 → stage → T-04 manifests |
| C-02 | Boundary error handling | **PASS** | T-03 column "Handling (NH-NN / mechanism)" is required; silence is structurally visible as a blank cell |
| C-03 | Data loss point identification | **PASS** | Section 3 explicitly mandates "at least one concrete LP-NN per stage"; generic "errors may occur" called out as disqualifier |
| C-04 | Schema state at each stage | **PASS** | Stage-Exit Manifest (T-04 entry) required at each stage with typed field assertions; "verified: no field added…" required for unchanged stages |
| C-05 | Latency characterization | **PASS** | Section 3 requires latency annotation: value, range, or named characterization per stage |
| C-06 | Stale data windows | **PASS** | Section 3 requires normal-operation vs failure-mode staleness quantified separately |
| C-07 | Domain framing | **PASS** | T-02 Entity Inventory with Domain, Key Fields columns; trace may only reference named T-02 entities |
| C-08 | Recovery prescriptions | **PASS** | Section 7 (T-06) requires mechanism per NH-NN and LP-NN; prose-only disqualified |
| C-09 | Pattern trade-off analysis | **PASS** | Section 6 explicitly requires named alternative pattern, ≥2 trade-off dimensions, at least one quantified in domain terms |
| C-10 | Pre-trace entity inventory | **PASS** | Section 2 (T-02) completed before Section 3; undeclared entity explicitly named as failure |
| C-11 | Systematic boundary labeling | **PASS** | T-03 assigns NH-NN at boundary definition; B[N]->[N+1] format explicit in Section 5; all C-02 annotations reference these labels |
| C-12 | Verified-unchanged schema assertion | **PASS** | Section 3 mandates exact "Verified: no field added, removed, renamed, or retyped" language for unchanged stages |
| C-13 | Structural completeness enforcement | **PASS** | T-03 blank cell = visible gap; T-06 missing row = visible gap; both map directly to C-02/C-03/C-04 |
| C-14 | Incumbent baseline anchoring | **PASS** | Section 7 rule: "Incumbent Step must cite a specific Step ID from T-01. Process category only fails." |
| C-15 | Structured incumbent baseline table | **PASS** | T-01 is a named table with Step ID, Step Name, Actor/Role, Elapsed Time, Trigger — five columns, minimum three rows |
| C-16 | Full recovery-to-baseline traceability | **PASS** | T-06 "Incumbent Step (T-01)" column is required for every row, not just ≥1; step-level citation enforced structurally |
| C-17 | Entity-at-risk annotation per boundary | **PASS** | T-03 "Entity at Risk" column required; "Data" or "records" explicitly disqualified; must cite T-02 entity |
| C-18 | Structured recovery audit table | **PASS** | T-06 is a named table with triggering condition, recovery mechanism, boundary/stage, and incumbent step columns; prose disqualified; every NH-NN and LP-NN must have a row |
| C-19 | Typed stage-exit manifests | **PASS** | Section 3 requires `field_name: TYPE(precision)` notation and field count; manifest is designated downstream authority for C-17/C-20/C-04 resolution |
| C-20 | Field-level entity-at-risk traceability | **PASS** | T-03 "Entity.Field at Risk" column requires `entity.field_name` format resolvable against T-04 manifest; entity-name-only explicitly disqualified |
| C-21 | Decomposed boundary latency | **PASS** | T-03 has "Transport (ms)" and "Processing (ms)" as independent columns; "Negligible" disqualified; numeric ms required |
| C-22 | Cumulative SLA% with domination point | **PASS** | T-03 has "SLA%" and "Cumul. SLA%" columns; DOMINATION POINT statement explicitly required after table with crossing percentage and justification |
| C-23 | Structurally separate closure gate | **PASS** | Section 8 (T-07) declared structurally separate; per-identifier CLOSED/OPEN status rows required; summary count explicitly disqualified |
| C-24 | Pre-declared complete output scaffold | **PASS** | Section 0 must be completed before any other content; no table may appear unless declared in Section 0; scaffold presented as table with T-NN notation; prose list disqualified |

**Essential:** 4/4 → 60 pts  
**Recommended:** 3/3 → 30 pts  
**Aspirational:** 17/17 → 10 pts  
**Composite: 100**

---

## V-02 — Interrogative / Conversational Register *(truncated)*

**Note:** Input ends after the incumbent baseline table structure. Sections covering the pipeline trace, boundary inventory, schema diff, recovery audit, and closure gate were not provided. Scoring reflects only the visible portion.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **UNKNOWN** | Trace section not shown |
| C-02 | Boundary error handling | **UNKNOWN** | Boundary section not shown |
| C-03 | Data loss point identification | **UNKNOWN** | Stage trace section not shown |
| C-04 | Schema state at each stage | **UNKNOWN** | Manifest section not shown |
| C-05 | Latency characterization | **UNKNOWN** | Not in visible content |
| C-06 | Stale data windows | **UNKNOWN** | Not in visible content |
| C-07 | Domain framing | **PARTIAL** | No entity inventory table visible yet; conversational framing does not pre-enforce T-02 naming before trace |
| C-08 | Recovery prescriptions | **UNKNOWN** | Recovery section not shown |
| C-09 | Pattern trade-off analysis | **UNKNOWN** | Not in visible content |
| C-10 | Pre-trace entity inventory | **UNKNOWN** | Not in visible content |
| C-11 | Systematic boundary labeling | **UNKNOWN** | Not in visible content |
| C-12 | Verified-unchanged schema assertion | **UNKNOWN** | Not in visible content |
| C-13 | Structural completeness enforcement | **UNKNOWN** | Not in visible content |
| C-14 | Incumbent baseline anchoring | **UNKNOWN** | Recovery section not shown |
| C-15 | Structured incumbent baseline table | **PASS** | Table with Step ID, Step Name, Actor/Role, Elapsed Time, Trigger explicitly shown; Step ID cited-by requirement noted ("name them carefully") |
| C-16 | Full recovery-to-baseline traceability | **UNKNOWN** | Recovery section not shown |
| C-17 | Entity-at-risk annotation per boundary | **UNKNOWN** | Boundary section not shown |
| C-18 | Structured recovery audit table | **UNKNOWN** | Recovery section not shown |
| C-19 | Typed stage-exit manifests | **UNKNOWN** | Not in visible content |
| C-20 | Field-level entity-at-risk traceability | **UNKNOWN** | Not in visible content |
| C-21 | Decomposed boundary latency | **UNKNOWN** | Not in visible content |
| C-22 | Cumulative SLA% with domination point | **UNKNOWN** | Not in visible content |
| C-23 | Structurally separate closure gate | **UNKNOWN** | Not in visible content |
| C-24 | Pre-declared complete output scaffold | **FAIL** | Prompt asks "list every table this response will contain" as a conversational question; the output format is prose/list, not a structured table. Pass condition explicitly states "A prose list of table names does not qualify." No T-NN notation or structured block enforced. |

**Scorable essential:** insufficient visibility to confirm pass  
**Composite: N/A** (incomplete input)

**Key gap visible in V-02:** The conversational register softens the scaffold requirement exactly where precision matters most. C-24 fails at the prompt level — asking the model to list tables in prose is not the same as requiring a structured scaffold table with number, name, purpose, and references columns. The interrogative framing trades mechanical enforcement for naturalness.

---

## V-03 through V-05 — Not Provided

These variations were referenced in the rubric header but were absent from the input. Cannot score.

---

## Excellence Signals (from V-01)

1. **Scaffold-as-navigational-contract:** Declaring every output table in Section 0 with T-NN identifiers before any trace content creates a forward-reference system. Every downstream citation (`cite T-02 names`, `resolvable against T-04 manifest`, `cite a specific Step ID from T-01`) is guaranteed resolvable because the contract is complete before the first trace line is written. This is categorically stronger than retroactively checking that tables are present.

2. **Structural visibility of gaps:** The prompt design makes every gap visible as a blank cell or missing row rather than as a prose omission. Blank in T-03's "Entity at Risk" column, missing row in T-06, missing T-07 row — all fail at a glance. This shifts the compliance burden from the scorer to the output structure itself.

3. **Disqualifier language co-located with criteria:** Each section explicitly states what does *not* qualify ("Negligible is not a value," "prose recovery section does not satisfy," "summary count does not satisfy"). Co-locating the disqualifier at the point of generation prevents plausible-but-failing outputs.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
