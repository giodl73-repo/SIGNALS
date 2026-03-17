## flow-dataflow R16 — Scoring (Rubric v13, C-01–C-31)

---

### Rubric Tier Recap

| Tier | Criteria | Pts Each | Max |
|------|----------|----------|-----|
| Essential | C-01–C-04 | 14 | 56 |
| Recommended | C-05–C-07 | 10 | 30 |
| Aspirational | C-08–C-31 | 0.65 (PARTIAL = 0.33) | 15.60 |
| **Total** | | | **101.60** |

---

### V-01 — Scaffold Column Specification

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | T-03 Stage Enumeration required; "a stage referenced later but absent here fails" |
| C-02 | PASS | Per-stage boundary annotation with NH-NN or explicit "risk accepted" flag |
| C-03 | PASS | LP-NN named scenario required in boundary annotation |
| C-04 | PASS | T-06 Typed Exit Manifests per stage; schema diff at every stage entry |
| C-05 | PASS | Boundary annotation latency line + T-04 Transport/Processing/Total columns |
| C-06 | PASS | Normal stale window + failure-mode stale window (separate) in boundary annotation |
| C-07 | PASS | Entity Inventory enforces domain names; "data/records/payload" prohibited |
| C-08 | PASS | T-10 Recovery Audit Table covers every NH-NN and LP-NN |
| C-09 | PASS | Pattern Trade-Off section with ≥2 dimensions, at least one domain-quantified |
| C-10 | PASS | T-01 Entity Inventory pre-declared; stage traces may only reference entities declared here |
| C-11 | PASS | T-04 Boundary Inventory with B[N]->[N+1] labels; annotations reference labels by name |
| C-12 | PASS | Stage template supplies "verified: no field added, removed, renamed, or retyped" |
| C-13 | PASS | T-04 (boundary table) and T-10 (recovery table) make missing entries structurally visible |
| C-14 | PASS | T-05 Incumbent Baseline; Recovery Framing template requires named operational role |
| C-15 | PASS | T-05 has Step ID, Step Name, Responsible Role, Elapsed Time/Frequency (4 columns) |
| C-16 | PASS | Recovery Framing cell requires IB-NN step name corresponding to T-05 row on every row |
| C-17 | PASS | T-04 "Entity at Risk" column; "must name a specific T-01 entity — not 'data' or 'records'" |
| C-18 | PASS | T-10 has Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary/Stage, Recovery Framing |
| C-19 | PASS | T-06 Typed Exit Manifests with field_name, TYPE(precision), Notes; authority for back-fill |
| C-20 | PARTIAL | T-04 entity.field column enforces field-level specificity ("Format: entity.field_name") but the mandatory "— risk description" suffix from C-20 pass condition is absent from the cell format |
| C-21 | PASS | Transport (ms) and Processing (ms) independent columns; "Negligible" explicitly prohibited |
| C-22 | PASS | T-04 SLA% This + Cumulative SLA% columns; T-08 DOMINATION POINT statement |
| C-23 | PASS | T-11 Closure Gate with per-identifier CLOSED/OPEN; summary count explicitly rejected |
| C-24 | PASS | STEP 0 scaffold pre-declares all 11 tables with T#, Name, Purpose, Mandatory Columns, Depends On |
| C-25 | PASS | Single-role design — satisfies by default per scaffold declaration |
| C-26 | PASS | T-02 FM-NN Prediction Register + T-09 Resolution Audit with CONFIRMED/EXONERATED/NEW and deferral chain |
| C-27 | PASS | T-09 pre-declared in scaffold with purpose "FM-NN Resolution Audit — post-trace lifecycle resolution; consumes T-07 as evidence" |
| C-28 | PASS | Per-stage T-07 APPEND table with FM-NN, Stage ID, Boundary/Condition, Deferral Statement; resolution status prohibited inline |
| C-29 | PASS | T-07 pre-declared in scaffold with "rows appended per stage, not post-trace"; per-stage table appended within stage block; consolidated T-07 at end |
| C-30 | PASS | T-08 pre-declared in scaffold as standalone artifact; footnote "→ Domination analysis: see T-08" in T-04; T-08 produced as separate named section |
| C-31 | PASS | Recovery Framing column with template; all three fields in same cell; "distributing step, actor, and cadence across separate columns fails" explicitly stated |

**V-01 score**: 56 + 30 + (23 × 0.65) + (1 × 0.33) = 56 + 30 + 14.95 + 0.33 = **101.28**

---

### V-02 — Phase-Gated with Per-Stage T-07 Append Checkpoints

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | T-03 in Phase 2; stage referenced in traces but absent fails |
| C-02 | PASS | Boundary annotation in each stage block with NH-NN or explicit risk-accepted |
| C-03 | PASS | LP-NN named scenario in boundary annotation |
| C-04 | PASS | T-08 Stage Exit Manifests per stage; schema diff at every stage entry |
| C-05 | PASS | T-04 Transport/Processing/Total columns + boundary annotation latency line |
| C-06 | PASS | Normal stale window + failure-mode stale window (separate) |
| C-07 | PASS | T-01 Entity Inventory with domain names enforced |
| C-08 | PASS | T-11 Recovery Audit Table covers every NH-NN and LP-NN |
| C-09 | PASS | T-09 Pattern Trade-Off with ≥2 dimensions, at least one domain-quantified |
| C-10 | PASS | T-01 Entity Inventory; entities not declared here may not appear in stage traces |
| C-11 | PASS | T-04 Boundary Inventory with B[N]->[N+1] labels throughout |
| C-12 | PASS | "verified: no field added, removed, renamed, or retyped" in stage template |
| C-13 | PASS | T-04 and T-11 structured tables; missing entries visible |
| C-14 | PASS | T-06 Incumbent Baseline; Recovery Framing requires named operational role (AP Clerk, Inventory Controller, etc.) |
| C-15 | PASS | T-06 has Step ID, Step Name, Responsible Role, Elapsed Time/Frequency |
| C-16 | PASS | T-11 Recovery Framing cites specific T-06 Step IDs on every row |
| C-17 | PASS | T-04 Entity at Risk column; "names a specific T-01 entity" enforced |
| C-18 | PASS | T-11 has Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary/Stage, Recovery Framing |
| C-19 | PASS | T-08 Typed Exit Manifests with field_name, TYPE(precision), Notes |
| C-20 | PARTIAL | entity.field back-fill from T-08 enforces field-level specificity but "— risk description" suffix not required in cell format |
| C-21 | PASS | Transport and Processing independent columns; "Negligible" prohibited |
| C-22 | PASS | T-04 SLA% columns; T-05 standalone domination point |
| C-23 | PASS | T-12 Closure Gate per-identifier; "A summary count does not satisfy this gate" |
| C-24 | PASS | Phase 1 scaffold declares all 12 tables before any domain content; Phase 1 gate enforces no post-scaffold table appearances |
| C-25 | PASS | Single-role design satisfies by default |
| C-26 | PASS | T-02 FM-NN Prediction Register + T-10 Resolution Audit with full lifecycle |
| C-27 | PASS | T-10 pre-declared in scaffold: "Post-trace FM-NN lifecycle resolution; consumes T-07" with dependency listed |
| C-28 | PASS | Per-stage T-07 APPEND CHECKPOINT with table rows; "Do not embed acknowledgments as prose bullets" |
| C-29 | PASS | T-07 pre-declared in scaffold as "running append-log; one checkpoint per stage; consolidated after final stage"; explicit "Appended N rows to T-07 at [Stage ID]" count statement enforces accumulation verification between stages — not post-trace |
| C-30 | PASS | T-05 SLA Domination Point pre-declared in scaffold as separate artifact; footnote "→ Domination analysis: T-05" in T-04; T-05 produced as standalone section |
| C-31 | PASS | T-11 Recovery Framing template; "A row satisfying step citation but omitting actor or cadence fails C-31" explicitly stated |

**V-02 score**: 56 + 30 + (23 × 0.65) + (1 × 0.33) = **101.28**

**V-02 differential**: C-29 enforcement is structurally strongest across all five variations. The explicit count declaration "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended" between every stage is the only mechanism in R16 that structurally *verifies* accumulation between stages rather than merely instructing it. Phase-gate lifecycle provides a second enforcement layer (PHASE 3 COMPLETE gate requires T-07 consolidated before Phase 4 begins).

---

### V-03 — Imperative Commands with Explicit Prohibitions

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | CMD-04 produces T-03 Stage Enumeration |
| C-02 | PASS | CMD-08c boundary annotation with NH-NN or explicit risk-accepted |
| C-03 | PASS | LP-NN named scenario in CMD-08c |
| C-04 | PASS | CMD-08b T-06 Typed Exit Manifests per stage |
| C-05 | PASS | T-04 Transport/Processing/Total columns + boundary latency annotation |
| C-06 | PASS | Normal stale window + failure-mode stale window in CMD-08c |
| C-07 | PASS | CMD-02 enforces domain entity names; "data/records/payload/item" prohibited |
| C-08 | PASS | CMD-11 T-10 Recovery Audit Table |
| C-09 | PASS | CMD-10 Pattern Trade-Off with ≥2 dimensions |
| C-10 | PASS | CMD-02 T-01 Entity Inventory pre-declared |
| C-11 | PASS | T-04 Boundary Inventory with B[N]->[N+1] labels |
| C-12 | PASS | CMD-08a schema diff with "verified" language |
| C-13 | PASS | T-04, T-10 as structural tables |
| C-14 | PASS | CMD-07 T-05 Incumbent Baseline with IB-NN step IDs; Recovery Framing requires named operational role |
| C-15 | PASS | T-05 has Step ID, Step Name, Responsible Role, Elapsed Time/Frequency |
| C-16 | PASS | CMD-11 Recovery Framing cites IB-NN step IDs on every row |
| C-17 | PASS | T-04 Entity at Risk column |
| C-18 | PASS | T-10 with all required columns |
| C-19 | PASS | CMD-08b T-06 Typed Exit Manifests |
| C-20 | PARTIAL | CMD-08d "Format: entity.field_name" — no "— risk description" suffix in cell |
| C-21 | PASS | "Negligible is NOT a valid latency value" in CMD-05; independent columns |
| C-22 | PASS | T-04 SLA% columns; CMD-06 T-08 standalone domination point |
| C-23 | PASS | CMD-13 T-11 Closure Gate; "DO NOT produce a summary count" |
| C-24 | PASS | CMD-01 scaffold with all 11 tables declared; "DO NOT omit T-07 or T-08 from the scaffold" |
| C-25 | PASS | Single-role design satisfies by default |
| C-26 | PASS | CMD-03 T-02 Prediction Register + CMD-12 T-09 Resolution Audit |
| C-27 | PASS | T-09 pre-declared in CMD-01 scaffold with dependency on T-02, T-07 |
| C-28 | PASS | CMD-08e "DO NOT write FM-NN acknowledgments as prose bullets within the stage block. APPEND TABLE ROWS ONLY." |
| C-29 | PASS | T-07 pre-declared in scaffold; CMD-08e explicit prohibition against prose bullets; CMD-09 consolidation step |
| C-30 | PASS | CMD-06 carries three explicit prohibitions: "DO NOT embed as a prose note appended to T-04," "DO NOT produce it as an inline sub-section of T-04," and "T-08 is a separate named table, pre-declared in the scaffold" — strongest C-30 enforcement framing |
| C-31 | PASS | CMD-11: "MUST appear in the SAME Recovery Framing cell" + "DO NOT distribute step, actor, and cadence across separate columns" |

**V-03 score**: 56 + 30 + (23 × 0.65) + (1 × 0.33) = **101.28**

**V-03 differential**: Strongest C-30 enforcement — three explicit DO NOT prohibitions name the failure patterns (prose note, inline sub-section, merged table) before the model reaches those decision points. Also strongest prohibition framing for C-29 (CMD-08e) and C-31 (CMD-11).

---

### V-04 — Two-Role Design with Handoff Gate

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | T-03 Stage Enumeration |
| C-02 | PASS | Boundary annotation in each role section |
| C-03 | PASS | LP-NN in boundary annotations |
| C-04 | PASS | T-09 Stage Exit Manifests per stage |
| C-05 | PASS | T-05 Transport/Processing/Total columns + boundary latency annotation |
| C-06 | PASS | Normal and failure-mode stale windows |
| C-07 | PASS | T-01 Entity Inventory with Finance Controller domain terms enforced |
| C-08 | PASS | T-11 Recovery Audit Table |
| C-09 | PASS | Pattern Trade-Off Analysis with ≥2 dimensions |
| C-10 | PASS | T-01 Entity Inventory; "Operations Analyst may add CDC/pipeline-internal entities if distinct" |
| C-11 | PASS | T-05 Boundary Inventory with B[N]->[N+1] labels; Finance Controller and Operations Analyst populate separate boundary rows |
| C-12 | PASS | "verified: no field added, removed, renamed, or retyped" in stage templates |
| C-13 | PASS | T-05 and T-11 as structural tables |
| C-14 | PASS | T-07 Incumbent Baseline with IB-NN step IDs; Recovery Framing names AP Clerk, Inventory Controller, etc. |
| C-15 | PASS | T-07 has Step ID, Step Name, Responsible Role, Elapsed Time/Frequency |
| C-16 | PASS | T-11 Recovery Framing cites IB-NN step IDs corresponding to T-07 rows |
| C-17 | PASS | T-05 Entity at Risk column |
| C-18 | PASS | T-11 with all required columns |
| C-19 | PASS | T-09 Stage Exit Manifests with typed field declarations |
| C-20 | PARTIAL | T-05 entity.field back-filled from T-09; format enforces field-level specificity but not "— risk description" suffix |
| C-21 | PASS | "Negligible is not a valid latency value"; Transport/Processing as independent columns in T-05 |
| C-22 | PASS | T-05 SLA% columns; T-06 standalone domination point produced by Finance Controller |
| C-23 | PASS | T-12 Closure Gate per-identifier; "No summary counts" |
| C-24 | PASS | STEP 0 scaffold declares all 12 tables before any domain content |
| C-25 | PASS | T-04 Stage Assignment Map with Stage ID, Stage Name, Assigned Role; "A stage with no assigned role is a structural gap" — explicit multi-role compliance |
| C-26 | PASS | T-02 FM-NN Prediction Register (Finance Controller and Operations Analyst contribute separately) + T-10 Resolution Audit |
| C-27 | PASS | T-10 pre-declared in scaffold with dependency on T-02, T-08 |
| C-28 | PASS | Per-stage T-08 APPEND in each role section; "TABLE ROWS ONLY — no prose bullets" |
| C-29 | PASS | T-08 pre-declared as "append-log accumulating during both role sections"; HANDOFF GATE requires "confirm rows are present for all Finance Controller stages" with count statement — cross-role accumulation verification |
| C-30 | PASS | T-06 pre-declared as "Standalone domination artifact — separate from T-05"; Finance Controller's SLA budget authority; footnote "→ Domination analysis: T-06" in T-05 |
| C-31 | PASS | T-11 Recovery Framing template; "Step, actor, and cadence must be in the same Recovery Framing cell — not separate columns" |

**V-04 score**: 56 + 30 + (23 × 0.65) + (1 × 0.33) = **101.28**

**V-04 differential**: Strongest C-25 implementation (explicit Stage Assignment Map T-04 for multi-role design). HANDOFF GATE is a novel structural mechanism — making T-08 append-log completeness a named cross-role transfer condition. Finance Controller domain ownership of SLA budget (T-06) creates natural authority grounding.

---

### V-05 — Inertia Framing + Recovery Framing as Lead Column

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | PASS | T-04 Stage Enumeration |
| C-02 | PASS | Boundary annotation per stage |
| C-03 | PASS | LP-NN in boundary annotation |
| C-04 | PASS | T-07 Stage Exit Manifests per stage |
| C-05 | PASS | T-05 Transport/Processing/Total columns + boundary annotation latency |
| C-06 | PASS | Normal and failure-mode stale windows in boundary annotation |
| C-07 | PASS | T-02 Entity Inventory with domain names; "data/records are not entity names" |
| C-08 | PASS | T-10 Recovery Audit Table |
| C-09 | PASS | Pattern Trade-Off Analysis with ≥2 dimensions |
| C-10 | PASS | T-02 Entity Inventory pre-declared; "Stage traces and T-07 manifests may only reference entities declared here" |
| C-11 | PASS | T-05 Boundary Inventory with B[N]->[N+1] labels |
| C-12 | PASS | "verified: no field added, removed, renamed, or retyped" in stage template |
| C-13 | PASS | T-05 and T-10 as structural tables |
| C-14 | PASS | T-01 produced before scaffold; "Name real operational roles (AP Clerk, Inventory Controller, Finance Analyst, Procurement Coordinator)" — strongest domain anchoring in R16 |
| C-15 | PASS | T-01 has Step ID, Step Name, Responsible Role, Elapsed Time/Frequency (produced before scaffold) |
| C-16 | PASS | T-10 Recovery Framing cites IB-NN step IDs from T-01 on every row |
| C-17 | PASS | T-05 Entity at Risk column |
| C-18 | PASS | T-10 has Row, NH/LP ID, Recovery Framing, Triggering Condition, Recovery Mechanism, Boundary/Stage |
| C-19 | PASS | T-07 Stage Exit Manifests with typed field declarations |
| C-20 | PARTIAL | T-05 entity.field back-fill from T-07 enforces field-level specificity but not "entity.field_name — risk description" format |
| C-21 | PASS | "Negligible is not a valid latency value"; Transport/Processing independent columns in T-05 |
| C-22 | PASS | T-05 SLA% columns; T-06 standalone domination point |
| C-23 | PASS | T-11 Closure Gate per-identifier; "No summary counts" |
| C-24 | PASS | T-00 Output Scaffold declares all 11 tables (T-01 through T-11) before Stage 1 trace; T-01 acknowledged in scaffold as "already produced above" |
| C-25 | PASS | Single-role design satisfies by default |
| C-26 | PASS | T-03 FM-NN Prediction Register + T-09 Resolution Audit with full lifecycle |
| C-27 | PASS | T-09 pre-declared in scaffold with dependency on T-03, T-08 |
| C-28 | PASS | Per-stage T-08 APPEND blocks; "TABLE ROWS ONLY — no prose bullets" |
| C-29 | PASS | T-08 pre-declared in scaffold; "rows appended per stage" in scaffold declaration; per-stage APPEND blocks with "Append one row per T-03 FM-NN that intersects this stage. If none: append one row noting no intersections"; consolidated T-08 at end |
| C-30 | PASS | T-06 pre-declared in scaffold as "Standalone domination artifact — separate from T-05"; footnote "→ Domination analysis: T-06" in T-05; "Do not embed as prose annotation or footnote within T-05" |
| C-31 | PASS | T-10 column order places Recovery Framing FIRST (before Triggering Condition and Recovery Mechanism); explicit note "This ordering commits the fallback contract (which T-01 step to revert to, who performs it, at what cadence) before the technical recovery mechanism is described" — structural gravity toward three-field compliance |

**V-05 score**: 56 + 30 + (23 × 0.65) + (1 × 0.33) = **101.28**

**V-05 differential**: T-01 produced before the scaffold — all IB-NN identifiers exist before any downstream table references them, eliminating forward-reference risk for C-14/C-15/C-16. Recovery Framing as lead column is the strongest C-31 mechanism in R16: column ordering forces the actor and cadence fields before any technical recovery detail can be written.

---

### Ranking Summary

| Rank | Variation | Score | Primary Differentiator |
|------|-----------|-------|----------------------|
| **1** | **V-02** | **101.28** | Per-stage APPEND CHECKPOINT with explicit count declaration — only mechanism in R16 that structurally *verifies* accumulation between stages |
| **2** | **V-05** | 101.28 | Recovery Framing as lead column (C-31 structural gravity) + inertia framing (T-01 before scaffold eliminates forward-reference risk for IB-NN citations) |
| **3** | V-03 | 101.28 | Three explicit DO NOT prohibitions name C-29/C-30 failure patterns before the model reaches the decision point |
| **4** | V-04 | 101.28 | Explicit Stage Assignment Map (C-25) + HANDOFF GATE as cross-role accumulation verification |
| **5** | V-01 | 101.28 | Mandatory Columns scaffold specification — strong baseline but no per-stage verification mechanism |

---

### Excellence Signals

**From V-02 (top)**:

1. **Per-stage append checkpoint count declaration**: `"T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended"` between every stage block is the first mechanism in the rubric series that verifies accumulation quantity between stages rather than merely instructing it. This makes a missing append structurally detectable before the next stage begins — not at consolidated review time.

2. **Phase-gate compound enforcement**: Phase gates require state declarations (`PHASE N COMPLETE`) that serve as local closure checkpoints. PHASE 3's gate requires T-07 consolidated before Phase 4 begins, creating a second verification layer above the per-stage checkpoint.

**From V-05 (second)**:

3. **Recovery Framing as lead column**: Placing Recovery Framing before Triggering Condition and Recovery Mechanism in T-10 creates structural gravity — the model must commit the IB-NN step, actor, and cadence before it can write any technical recovery detail. This exploits left-to-right column ordering as an enforcement mechanism, not just instruction.

4. **Incumbent baseline before scaffold (inertia framing)**: Producing T-01 before any scaffold entry means all IB-NN step identifiers are materialized before the first downstream table references them. Eliminates the forward-reference window where Recovery Framing entries arrive before the T-01 rows they cite exist.

**From V-03**:

5. **Prohibition-first framing for C-30**: Naming the exact failure patterns (`DO NOT embed as a prose note appended to T-04`, `DO NOT produce it as an inline sub-section of T-04`) before the model reaches that section eliminates the ambiguity that allows the boundary between prose-domination and table-domination to collapse. Three prohibitions covering three distinct failure modes.

---

### C-20 Diagnostic (Shared PARTIAL Across All Variations)

All five variations enforce field-level entity specificity in the boundary inventory (`entity.field_name` format) but none explicitly require the `entity.field_name — risk description` format that C-20's pass condition specifies. The risk description is captured in the boundary annotation (NH-NN or LP-NN label), not in the T-04 `entity.field` cell. R17 should test whether explicitly combining the format requirement (`entity.field_name — {risk note from NH/LP annotation}`) in the back-fill instruction moves C-20 from PARTIAL to PASS.

---

```json
{"top_score": 101.28, "all_essential_pass": true, "new_patterns": ["Per-stage append checkpoint count declaration — explicit 'Appended N rows' statement between stages structurally verifies accumulation before next stage begins, not at post-trace consolidation", "Recovery Framing as lead column — column ordering forces three-field template (IB-NN step, actor, cadence) before technical recovery detail, exploiting left-to-right positional gravity as enforcement mechanism"]}
```
