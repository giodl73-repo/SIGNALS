# flow-dataflow — Quest Score — Round 9

> **Note:** Only V-01 and V-02 were provided; V-02 is cut off mid-Phase-2. Scoring reflects the visible prompt structure. V-02 estimates are marked where inference fills gaps.

---

## V-01 — Table Scaffolding Imposed Upfront

**Axis:** Every required output pre-declared as a named table; prose is secondary.

### Essential Criteria (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | **PASS** | Table 3 (Boundary Inventory) + Table 4 (Stage Trace) together mandate source→stage→destination for every entity. Entity must appear in Table 1 first. |
| C-02 | Boundary error handling | **PASS** | Table 3 column "Error Handling or NH-NN" — silence explicitly fails. Table 4 requires boundary annotation per stage. |
| C-03 | Data loss point identification | **PASS** | Table 4 "Named Loss Points" section requires LP-NN format with triggering condition per stage. |
| C-04 | Schema state at each stage | **PASS** | Table 4 Schema Entry + Schema Exit Manifest tables required per stage. Change Description column for altered fields. |

**Essential: 4/4 → 60 pts**

### Recommended Criteria (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-05 | Latency characterization | **PASS** | Table 4 requires `*Latency:*` annotation per stage. Table 3 has Transport + Processing + Total latency columns. |
| C-06 | Stale data windows | **PASS** | Table 5 with Normal Operation and Failure Mode columns. Separation of failure-mode from normal explicitly required. |
| C-07 | Domain framing | **PASS** | Table 1 Entity Inventory forces domain entity naming; "data/records" banned in Table 3 Entity at Risk column. |

**Recommended: 3/3 → 30 pts**

### Aspirational Criteria (10 pts, 10/16 = 0.625 pts each)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-08 | Recovery prescriptions | **PASS** | Table 6 requires a row per NH-NN and LP-NN; "no generic manual review" rule stated. |
| C-09 | Pattern trade-off analysis | **PASS** | Section 8 explicitly required with ≥2 dimensions and ≥1 quantified in domain terms. |
| C-10 | Pre-trace entity inventory | **PASS** | Table 1 gated: "No entity may appear in any downstream table unless it appears here first." |
| C-11 | Systematic boundary labeling | **PASS** | Table 3 uses B[N]->[N+1] format. Table 4 references boundary labels. |
| C-12 | Verified-unchanged schema assertion | **PASS** | Table 4 Schema Exit Manifest: bare "unchanged" without `verified: no field added...` explicitly fails. |
| C-13 | Structural completeness enforcement | **PASS** | All sections are tables — blank cells are structurally visible gaps. Tables map directly to C-02 (Table 3), C-03 (Table 4 LP section), C-04 (Table 4 manifest). |
| C-14 | Incumbent baseline anchoring | **PASS** | Table 6 column "Incumbent Baseline Step (Table 2 ID)" — process category without step ID explicitly fails. |
| C-15 | Structured incumbent baseline table | **PASS** | Table 2 with Step ID, Step Name, Responsible Actor, Elapsed Time. |
| C-16 | Full recovery-to-baseline traceability | **PASS** | Table 6 requires Step ID citation for every row — not just "at least one." |
| C-17 | Entity-at-risk annotation per boundary | **PASS** | Table 3 "Entity at Risk" column — "data/records" explicitly fails. |
| C-18 | Structured recovery audit table | **PASS** | Table 6 columns: Trigger ID, Boundary/Stage, Recovery Mechanism, Baseline Step. Missing row = visible gap. |
| C-19 | Typed stage-exit manifests | **PASS** | Table 4 Schema Exit Manifest requires `Field Name | Type(Precision)`. Must be referenceable downstream. |
| C-20 | Field-level entity-at-risk traceability | **PASS** | Table 3 "Entity.Field at Risk" column: `entity.field_name` format, must resolve against typed manifest. |
| C-21 | Decomposed boundary latency | **PASS** | Table 3 has separate Transport Latency (ms) and Processing Overhead (ms) columns. "Negligible" banned; numeric required. |
| C-22 | Cumulative SLA% with domination point | **PASS** | Table 3 has "SLA% This Boundary" + "Cumulative SLA%." DOMINATION POINT block required with crossing percentage + justification. |
| C-23 | Structurally separate closure gate | **PASS** | Table 7: per-identifier CLOSED/OPEN status. Summary count explicitly disqualified. Structurally separate from Table 6. |

**Aspirational: 16/16 → 10 pts**

### V-01 Composite

```
composite = (4/4 × 60) + (3/3 × 30) + (16/16 × 10)
          = 60 + 30 + 10
          = 100
```

**All essential pass: YES | Composite: 100**

---

## V-02 — Phase-Gated Protocol

**Axis:** Phase gates with entry criteria; next phase blocked until current outputs complete.  
**Status:** Prompt cut off mid-Phase-2. Phases 3–8 not visible. Scoring based on visible structure + reasonable inference from gate pattern.

### Essential Criteria (60 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Data lineage chain | **PASS** (inferred) | Phase-gate structure ensures stages are traced sequentially; entity inventory in Phase 1 constrains vocabulary. |
| C-02 | Boundary error handling | **PASS** | Phase 2 explicitly requires "Named mechanism OR NH-NN flag; silence fails." |
| C-03 | Data loss point identification | **PASS** (inferred) | Stage trace phase (likely Phase 3) would inherit LP-NN requirement from boundary gate structure. |
| C-04 | Schema state at each stage | **PARTIAL** | Not explicitly declared in visible phases. Inferred from Phase 3 likely covering stage trace, but typed manifest format not confirmed visible. |

**Essential: 3.5/4 → 52.5 pts**

### Recommended Criteria (30 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-05 | Latency characterization | **PARTIAL** | Phase 2 references latency at boundary level but no per-stage latency requirement visible. Stage trace phase unconfirmed. |
| C-06 | Stale data windows | **PASS** (inferred) | Phase structure would likely include a dedicated staleness phase, but not confirmed. |
| C-07 | Domain framing | **PASS** | Phase 1 entity inventory explicitly requires domain entity names. Phase 2 references Phase 1 inventory. |

**Recommended: 2/3 → 20 pts (conservative)**

### Aspirational Criteria (10 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-08 | Recovery prescriptions | **PASS** (inferred) | Recovery phase likely Phase 5-6 based on gate pattern. |
| C-09 | Pattern trade-off analysis | **UNKNOWN** | No visible requirement. |
| C-10 | Pre-trace entity inventory | **PASS** | Phase 1 gate: "entity not listed here may not appear in any later phase." |
| C-11 | Systematic boundary labeling | **PASS** | Phase 2 mandates B[N]->[N+1] format. |
| C-12 | Verified-unchanged schema assertion | **UNKNOWN** | Not in visible phases. |
| C-13 | Structural completeness enforcement | **PARTIAL** | Gate conditions create visible gaps by phase completion, but tables not pre-declared — prose responses allowed by default. |
| C-14 | Incumbent baseline anchoring | **PASS** | Phase 1: "every recovery prescription in Phase 6 must cite a Step ID." |
| C-15 | Structured incumbent baseline table | **PASS** | Phase 1: 4-column table with 3-row minimum explicitly required. |
| C-16 | Full recovery-to-baseline traceability | **PARTIAL** | Phase 1 says "every recovery prescription must cite a Step ID" — consistent with C-16, but not confirmed in recovery phase. |
| C-17 | Entity-at-risk annotation per boundary | **PASS** | Phase 2: "Entity at risk: a named entity from the Phase 1 inventory." |
| C-18 | Structured recovery audit table | **UNKNOWN** | Not in visible phases. |
| C-19 | Typed stage-exit manifests | **UNKNOWN** | Not in visible phases. Entity.Field reference requirement seen in Phase 2 but no manifest declaration. |
| C-20 | Field-level entity-at-risk traceability | **PARTIAL** | Phase 2: `entity.field_name` format required but references typed manifest from Phase 3 (not defined). |
| C-21 | Decomposed boundary latency | **UNKNOWN** | Latency decomposition not in visible phases. |
| C-22 | Cumulative SLA% + domination point | **UNKNOWN** | Not in visible phases. |
| C-23 | Structurally separate closure gate | **UNKNOWN** | Not in visible phases. |

**Aspirational visible passes: C-08, C-10, C-11, C-14, C-15 confirmed. Partials: C-13, C-16, C-17, C-20. Unknowns: 7 criteria.**  
**Conservative: 6/16 confirmed → 3.75 pts**

### V-02 Composite (conservative, visible only)

```
composite = (3.5/4 × 60) + (2/3 × 30) + (6/16 × 10)
          = 52.5 + 20 + 3.75
          = 76.25
```

**All essential pass: NO (C-04 PARTIAL) | Composite: ~76 (incomplete — 7 aspirational criteria unverifiable)**

---

## Rankings

| Rank | Variation | Composite | All Essential | Notes |
|------|-----------|-----------|---------------|-------|
| 1 | V-01 | **100** | YES | Complete coverage; every criterion directly addressed by a named table |
| 2 | V-02 | **~76** | NO (C-04 partial) | Prompt truncated; 7 aspirational criteria unverifiable; prose output not blocked |

---

## Excellence Signals (V-01)

1. **Pre-declared table schema as specification** — stating the exact column names in the prompt eliminates the model's freedom to omit required fields; a blank cell is structurally visible in a way a missing prose paragraph is not.
2. **Explicit "fails" language per criterion** — every table rule includes a fail condition ("Negligible is not a valid entry," "bare 'unchanged' fails"), removing ambiguity about what constitutes a pass.
3. **Cross-table reference chains** — Table 6 cites Table 2 Step IDs; Table 3 Entity.Field cites Table 4 manifests; Table 7 cites Table 6 rows. Breaks in the chain are surfaced as dangling references rather than silent omissions.
4. **NH-NN and LP-NN as typed identifiers** — assigning sequential identifiers to "no handling" annotations and loss points converts prose coverage claims into countable, matchable tokens that a closure gate can verify exhaustively.
5. **Domination point as mandatory computed output** — requiring a single named conclusion from the SLA% columns forces the model to synthesize quantitative data rather than present a table and stop.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["pre-declared column schema as prompt specification — blank cell visibility over missing prose", "explicit fail-condition language per table rule", "cross-table reference chains creating dangling-reference failure modes", "typed NH-NN/LP-NN identifiers enabling exhaustive closure gate matching", "mandatory computed synthesis output (domination point) from quantitative table data"]}
```
