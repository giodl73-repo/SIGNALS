Now I have everything needed to score. Let me write the full evaluation.

---

# flow-dataflow — Round 20 Scoring (Rubric v17)

**Rubric**: v17 · 46 criteria · Max 111.35
**Variations**: V-01 through V-05
**Trace artifact**: placeholder — scoring is structural (prompt design as output proxy)

---

## Scoring Method

Each variation is evaluated as a prompt design: the question is whether the structural machinery reliably produces compliant output for each criterion. All five variations share a well-evolved baseline from R19 (CMD-01 through CMD-21, STEP 0a/0b, triple-count, PG-NN gates, T-PARITY). R20 adds CMD-22 through CMD-25 targeting C-42 through C-46.

**PASS** = structural mechanism present and sufficient to reliably enforce the criterion.
**PARTIAL** = mechanism present but insufficiently explicit to guarantee compliant content (half credit: 7 pts for Recommended, 0.33 for Aspirational).
**FAIL** = mechanism absent.

---

## V-01 — Lifecycle Emphasis

**Axis**: STEP 0a/0b split + four-tier ACCUMULATION PROTOCOL as explicit contract.

### Essential (C-01–C-04)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Stage enumeration | **PASS** | T-03 required before any trace; CMD-08 enforces |
| C-02 | Error handling at every boundary | **PASS** | T-04 with NH-NN/LP-NN identifiers; B[N]->[N+1] annotations |
| C-03 | Data loss point identification | **PASS** | Stage traces require concrete named LP-NN per stage |
| C-04 | Schema state at each stage | **PASS** | T-06 typed exit manifests; CMD-05 prohibits prose-only |

**Essential subtotal: 56.00 / 56.00**

### Recommended (C-05–C-07)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Latency characterization | **PASS** | T-04 Transport(ms) + Processing(ms); CMD-10 prohibits "Negligible" |
| C-06 | Stale data windows | **PASS** | Phase 5 explicitly requires "stale data window under normal operation and under failure-mode conditions separately" |
| C-07 | Domain framing | **PASS** | T-01 entity inventory; CMD-07 prohibits undeclared entities; Finance/Operations domain vocabulary |

**Recommended subtotal: 30.00 / 30.00**

### Aspirational (C-08–C-46)

All 39 criteria PASS. Key evidence for new criteria:

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Recovery prescriptions | PASS | T-10 with specific IB-NN citations; T-11 closure gate |
| C-09 | Pattern trade-off analysis | PASS | Phase 5: "at least two trade-off dimensions, at least one quantified or qualified in domain terms" |
| C-10 | Pre-trace entity inventory | PASS | T-01 before Stage 1 |
| C-11 | Systematic boundary labeling | PASS | B[N]->[N+1] format, CMD-09 |
| C-12 | Verified-unchanged schema assertion | PASS | T-06 typed manifests with field-level assertions |
| C-13 | Structural completeness enforcement | PASS | T-04/T-10/T-11 tables enforce visible gaps |
| C-14 | Incumbent baseline anchoring | PASS | T-05 named IB process; T-10 cites IB-NN steps |
| C-15 | Structured IB table | PASS | T-05: IB-NN, Step Name, Responsible Role, Elapsed Time |
| C-16 | Full recovery-to-baseline traceability | PASS | CMD-13/14 require specific IB-NN step identifiers in every T-10 row |
| C-17 | Entity-at-risk per boundary | PASS | T-04 Entity at Risk column; CMD-11 prohibits generic labels |
| C-18 | Structured recovery audit table | PASS | T-10 six-column table (NH/LP ID, Triggering, Recovery, IB-NN, Boundary, Role) |
| C-19 | Typed stage-exit manifests | PASS | T-06 typed per stage; field_name: TYPE(precision) notation |
| C-20 | Field-level entity-at-risk traceability | PASS | entity.field format in T-04; stub back-fill mechanism |
| C-21 | Decomposed boundary latency | PASS | Separate Transport(ms) and Processing(ms) columns |
| C-22 | Cumulative SLA% with domination point | PASS | T-04 SLA% This + Cumulative SLA%; T-08 standalone domination table |
| C-23 | Structurally separate closure gate | PASS | T-11 per-identifier CLOSED/OPEN table |
| C-24 | Pre-declared complete output scaffold | PASS | STEP 0b scaffold with all tables; CMD-01 prohibits undeclared artifacts |
| C-25 | Stage-to-role assignment map | PASS | Single-role design — satisfied by default |
| C-26 | FM-NN prediction register + lifecycle | PASS | T-02 pre-trace + T-09 post-trace with CONFIRMED/EXONERATED/NEW |
| C-27 | FM-NN resolution section scaffold pre-registration | PASS | T-09 declared in scaffold before Stage 1 |
| C-28 | Inline FM-NN acknowledgment with deferral | PASS | T-07 rows appended per stage with deferral statement citing T-09 |
| C-29 | Append-log as named table artifact | PASS | T-07 pre-declared; CMD-04 prohibits prose bullets |
| C-30 | SLA domination as named table artifact | PASS | T-08 standalone, CMD-12 |
| C-31 | Checkpoint count statement | PASS | CHECKPOINT form required at every stage |
| C-32 | Per-stage checkpoint count [N] | PASS | [N] rows appended required in checkpoint |
| C-33 | Scaffold binding header | PASS | CMD-02 enforces "Mandatory Columns (exact names)" label exactly |
| C-34 | Per-phase completion gate block | PASS | PG-01 through PG-04 required |
| C-35 | Phase gate PG-NN pre-registration | PASS | All PG-NN pre-declared in scaffold; CMD-01 |
| C-36 | Count parity verification gate | PASS | T-PARITY standalone arithmetic table |
| C-37 | CMD-NN command register | PASS | CMD-01 through CMD-25 with positive imperative + DO NOT prohibitions |
| C-38 | CMD as scaffold entry zero | PASS | CMD is first scaffold row; CMD-18 enforces positional primacy |
| C-39 | CMD Binding column on every scaffold row | PASS | CMD Binding column on every T-NN, PG-NN, T-PARITY row |
| C-40 | Running total column in PG-NN gates | PASS | T-07 Running Total in every PG-NN gate; CMD-19; declared in Mandatory Columns |
| C-41 | Dual-count checkpoint [N]+[M] | PASS | ACCUMULATION PROTOCOL Tier 1 explicitly defines [M] = sum of all [N] through this stage |
| C-42 | IB-NN Coverage column in PG-NN gates | **PASS** | CMD-21: "Carry IB-NN Coverage column in every PG-NN gate block, pre-declared in scaffold Mandatory Columns"; monotonic growth rule stated |
| C-43 | IB table precedes scaffold as artifact zero | **PASS** | ORDERING RULE + STEP 0a explicit; CMD-22: "DO NOT declare T-05 as a future artifact when it already exists above" |
| C-44 | Triple-count checkpoint | **PASS** | CMD-23 explicitly prohibits [N]+[M] only; ACCUMULATION PROTOCOL Tier 1 states the IB-NN list rule; IB-NN Coverage growth rule documented |
| C-45 | Role-attributed rows in recovery audit table | **PASS** | CMD-24: Responsible Role sixth column from T-01/T-05 vocabulary; T-10 Mandatory Columns declares six columns |
| C-46 | Handoff continuity contract | **PASS** | T-04 Mandatory Columns includes Sending Role Delivery Guarantee + Receiving Role Acceptance Requirement; CMD-25; single-role design makes all boundaries exempt under the criterion's own exemption rule |

**Aspirational subtotal: 25.35 / 25.35**

**V-01 Total: 111.35 / 111.35**

---

## V-02 — Output Format: IB-Col?/HO-Col? Flag Columns

**Axis**: Scaffold gains IB-Col? and HO-Col? flag columns creating structural self-contradiction enforcement.

### Essential (C-01–C-04)

All four PASS. Same infrastructure as V-01.

**Essential subtotal: 56.00 / 56.00**

### Recommended (C-05–C-07)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Latency characterization | **PASS** | T-04 Transport(ms) + Processing(ms); CMD-10 |
| C-06 | Stale data windows | **PARTIAL** | Phase 5: "stale data window analysis" — does not explicitly require failure-mode staleness addressed separately from normal-operation staleness. V-01/V-03/V-04/V-05 all specify separation explicitly; V-02's terse Phase 5 is ambiguous on whether a model would address both modes. |
| C-07 | Domain framing | **PASS** | T-01 entity inventory; CMD-07 |

**Recommended subtotal: 25.00 / 30.00** (C-06 PARTIAL = 5 pts)

### Aspirational (C-08–C-46)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Pattern trade-off analysis | **PARTIAL** | Phase 5: "Pattern trade-off" only. No explicit requirement for ≥2 trade-off dimensions or domain-quantified dimension. Other variations specify "at least two trade-off dimensions, at least one quantified or qualified in domain terms" explicitly. |
| C-42 | IB-NN Coverage column in PG-NN gates | **PASS** | IB-Col? = YES on all PG-NN scaffold rows; SCAFFOLD AUDIT step verifies self-consistency; CMD-21 present — uniquely the strongest C-42 enforcement of any variation via self-contradiction mechanism |
| C-43 | IB table precedes scaffold | **PASS** | IB ORDERING RULE explicit; CMD-22; scaffold T-05 entry reads "Artifact zero -- produced above scaffold" |
| C-44 | Triple-count checkpoint | **PASS** | CMD-23 with IB-NN list required; monotonic growth rule stated |
| C-45 | Role-attributed recovery | **PASS** | CMD-24; T-10 Mandatory Columns shows Responsible Role as sixth column |
| C-46 | Handoff continuity contract | **PASS** | HO-Col? = YES on T-04 row; SCAFFOLD AUDIT verifies both handoff contract columns in Mandatory Columns; CMD-25 |
| All other aspirational | — | **PASS** | Same infrastructure as V-01 |

**Aspirational subtotal: 25.03 / 25.35** (C-09 PARTIAL = 0.33 pts)

**V-02 Total: 106.03 / 111.35**

---

## V-03 — Role Sequence: Finance/Operations Split with T-12

**Axis**: Finance Controller (Stages 1-3) / Operations Analyst (Stages 4-6); T-12 dedicated bilateral contract table; T-25 stage assignment map; CMD Role Owner column.

### Essential (C-01–C-04)

All four PASS. T-03/T-04/T-06/T-11 infrastructure intact across both role sections.

**Essential subtotal: 56.00 / 56.00**

### Recommended (C-05–C-07)

All three PASS. Phase 5: "At least two trade-off dimensions, one quantified. Stale data window: normal operation vs failure-mode staleness addressed separately." T-04 latency columns complete.

**Recommended subtotal: 30.00 / 30.00**

### Aspirational (C-08–C-46)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-25 | Stage-to-role assignment map | **PASS** | T-25 Stage Assignment Map declared in scaffold with Stage ID, Stage Name, Assigned Role; multi-role design activates criterion; Finance Controller: Stages 1-3, Operations Analyst: Stages 4-6 |
| C-42 | IB-NN Coverage column in PG-NN gates | **PASS** | CMD-21; PG-NN rows include IB-NN Coverage in Mandatory Columns; both Finance-owned (PG-01/PG-02) and Operations-owned (PG-03/PG-04) gates declare it; PG-02 gate explicitly shows IB-NN Coverage for T-12 row |
| C-43 | IB table precedes scaffold | **PASS** | IB ORDERING RULE; CMD-22; T-05 role vocabulary in STEP 0a explicitly governs both Finance and Operations role names downstream |
| C-44 | Triple-count checkpoint | **PASS** | CMD-23; Finance stages and Operations stages both close with triple-count; IB-NN list expands to include Operations-owned IB steps in later stages |
| C-45 | Role-attributed recovery | **PASS** | CMD-24; Phase 4 note distinguishes Finance vs Operations roles explicitly: "Finance Controller recovery rows say 'Finance Controller'; Operations Analyst recovery rows say 'Operations Analyst'" |
| C-46 | Handoff continuity contract | **PASS** ★ | T-12 dedicated Handoff Continuity Contract table (unique to V-03); T-04 handoff contract columns; T-25 role map; CMD-25 covers both T-04 columns and T-12 as primary contract; PG-01 checks T-12 declared in scaffold; T-12 format explicitly requires Delivery Guarantee (named artifact) + Acceptance Requirement (named precondition) with domain role names |
| All other aspirational | — | **PASS** | Full CMD-01 through CMD-25 infrastructure |

**Aspirational subtotal: 25.35 / 25.35**

**V-03 Total: 111.35 / 111.35**

---

## V-04 — Phrasing Register: Coaching-Imperative with Explicit Arithmetic

**Axis**: Structural requirements taught as formulas (M_k = M_(k-1) + N_k) and diagnostic questions ("who gets paged at 3am?", two-question handoff heuristic).

### Essential (C-01–C-04)

All four PASS. CMD register and scaffold infrastructure complete.

**Essential subtotal: 56.00 / 56.00**

### Recommended (C-05–C-07)

All three PASS. Phase 5: "at least two trade-off dimensions (at least one quantified in domain terms). Discuss the stale data window under normal operation and under failure-mode conditions separately."

**Recommended subtotal: 30.00 / 30.00**

### Aspirational (C-08–C-46)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-42 | IB-NN Coverage column in PG-NN gates | **PASS** | CMD-21; PG-NN Mandatory Columns declares IB-NN Coverage; coaching note explains purpose: "at PG-03, the IB-NN Coverage column should contain IB steps automated through the traced stages" |
| C-43 | IB table precedes scaffold | **PASS** | "A note on structure before you begin" explains WHY IB comes first ("everything the pipeline automates is departing from T-05"); CMD-22; the explanatory framing is unique to V-04 and makes the ordering self-motivating |
| C-44 | Triple-count checkpoint | **PASS** ★ | M_k = M_(k-1) + N_k formula explicitly taught; IB_list_k = IB_list_(k-1) ∪ {new IB steps at k} stated as an arithmetic rule; contradiction test stated: "A list at stage k that is shorter than the list at stage k-1 is a contradiction. Flag it explicitly." Strongest arithmetic correctness guarantee of any variation. |
| C-45 | Role-attributed recovery | **PASS** ★ | "Who gets paged at 3am?" heuristic; Phase 4 reminder: "If the Responsible Role would be 'team' or 'system,' look at T-05's Responsible Role column for the IB-NN step you are citing and use that role name." Ensures correct content not just column presence. |
| C-46 | Handoff continuity contract | **PASS** ★ | Two-question heuristic for CMD-25: "(1) What does the sending role commit to delivering, specifically? (2) What does the receiving role need to see before it starts processing?" Both answers must name specific artifacts or field sets; Phase 2 instructions apply the two questions for T-04 |
| All other aspirational | — | **PASS** | Full CMD infrastructure |

**Aspirational subtotal: 25.35 / 25.35**

**V-04 Total: 111.35 / 111.35**

---

## V-05 — Combination: Inertia-First + Role-Attributed Recovery + Handoff Continuity

**Axis**: IB-first framing as structural identity ("the pipeline replaces manual steps, not adds stages"); T-03 IB-NN Steps Replaced column; compound verification chain; CMD-24 traces recovery role directly to T-05 cited row.

### Essential (C-01–C-04)

All four PASS. Same infrastructure, reinforced by IB-anchor framing at every stage.

**Essential subtotal: 56.00 / 56.00**

### Recommended (C-05–C-07)

All three PASS. Phase 5: "one quantified. Stale data window: normal operation vs failure-mode addressed separately." Phase 5 additionally requires naming the highest-Elapsed-Time IB step and confirming displacement status — connects T-05 Elapsed Time back to synthesis.

**Recommended subtotal: 30.00 / 30.00**

### Aspirational (C-08–C-46)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-14 | Incumbent baseline anchoring | **PASS** ★ | Phase 5 uniquely requires identifying "the IB step that represented the highest manual effort (by Elapsed Time in T-05) and confirm whether it has been fully automated or partially displaced" — IB-anchor persists through synthesis, not just trace phases |
| C-15 | Structured IB table | **PASS** ★ | T-05 Elapsed Time column cited in Phase 5 synthesis; IB-anchor framing makes T-05 the most heavily referenced table in the response |
| C-16 | Full recovery-to-baseline traceability | **PASS** | All T-10 IB-NN citations enforced; Phase 4: "trace to the IB-NN step cited in that row, find its Responsible Role in T-05, and use that exact role name" |
| C-42 | IB-NN Coverage column in PG-NN gates | **PASS** ★ | CMD-21; PG-NN Mandatory Columns; PG-04 check: "IB-NN list at final checkpoint covers all T-03 'IB-NN Steps Replaced' claims" — unique cross-reference between T-03 forward declarations and PG-04 audit |
| C-43 | IB table precedes scaffold as artifact zero | **PASS** ★ | ORDERING RULE; CMD-22; T-03 "Depends On = T-05" structurally encodes the dependency; stage trace framing: "Stage [ID] automates IB-[NN]: [step name from T-05]" makes IB-anchor the response identity |
| C-44 | Triple-count checkpoint | **PASS** ★ | CMD-23; checkpoint IB-NN list must equal T-03's "IB-NN Steps Replaced" for each stage — contradiction between T-03 claim and checkpoint list is flaggable, creating three-level verification |
| C-45 | Role-attributed recovery | **PASS** ★ | CMD-24: "must come from T-05 Responsible Role column" for the cited row — not just vocabulary list but mechanical trace to specific T-05 row. Phase 4 instruction: "For each T-10 row, trace to the IB-NN step cited in that row, find its Responsible Role in T-05, and use that exact role name" |
| C-46 | Handoff continuity contract | **PASS** | T-04 handoff contract columns; CMD-25 with T-05 role vocabulary enforcement for role names; T-05 provides the canonical role names that flow into T-04 contract columns |
| All other aspirational | — | **PASS** | Full CMD-01 through CMD-25 infrastructure |

**Aspirational subtotal: 25.35 / 25.35**

**V-05 Total: 111.35 / 111.35**

---

## Score Summary

| Rank | Variation | Essential | Recommended | Aspirational | **Total** |
|------|-----------|-----------|-------------|--------------|-----------|
| 1 | **V-05** Combination: Inertia-first + role recovery + handoff | 56.00 | 30.00 | 25.35 | **111.35** |
| 2 | **V-03** Finance/Operations role split with T-12 | 56.00 | 30.00 | 25.35 | **111.35** |
| 3 | **V-04** Coaching-imperative with arithmetic formulas | 56.00 | 30.00 | 25.35 | **111.35** |
| 4 | **V-01** Lifecycle emphasis + four-tier accumulation | 56.00 | 30.00 | 25.35 | **111.35** |
| 5 | **V-02** IB-Col?/HO-Col? flag columns | 56.00 | **25.00** (C-06 PARTIAL) | **25.03** (C-09 PARTIAL) | **106.03** |

**Tiebreak ranking (V-01/V-03/V-04/V-05 all at 111.35)**:
- V-05 first: only variation with T-03 IB displacement column + six-level IB verification chain + Phase 5 T-05 Elapsed Time synthesis
- V-03 second: only variation with T-12 dedicated bilateral contract table and T-25 role map — most demonstrably satisfies C-46 for multi-role pipelines
- V-04 third: explicit M_k = M_(k-1) + N_k formula guarantees arithmetic correctness, not just column presence — strongest C-44 content guarantee
- V-01 fourth: strong lifecycle ordering with ORDERING RULE + four-tier ACCUMULATION PROTOCOL; all criteria PASS but less structural innovation

---

## V-02 Penalty Detail

| Criterion | Tier | Expected | Actual | Penalty |
|-----------|------|----------|--------|---------|
| C-06 Stale data windows | Recommended | 10.00 | 5.00 (PARTIAL) | −5.00 |
| C-09 Pattern trade-off analysis | Aspirational | 0.65 | 0.33 (PARTIAL) | −0.32 |

**Root cause**: V-02 Phase 5 is terse ("Pattern trade-off, stale data window analysis, dominant failure mode summary") compared to all other variations which explicitly require (a) ≥2 trade-off dimensions with at least one quantified, and (b) failure-mode staleness addressed separately from normal-operation staleness. The structural innovation of V-02 (IB-Col?/HO-Col? flags) is concentrated in Phase 1 scaffold enforcement and does not extend Phase 5 precision. V-02 achieves the strongest C-42 enforcement of any single variation via self-contradiction mechanism — the Phase 5 gap is isolated and would be easy to fix.

---

## Excellence Signals from V-05 (Top-Ranked)

**1. T-03 IB-NN Steps Replaced column creates a pre-declared displacement contract**

V-05 adds an "IB-NN Steps Replaced" column to T-03 Stage Enumeration. Every stage forward-declares which IB steps it automates, and CMD-08 prohibits leaving that column blank. This creates a six-level verification chain: T-05 → T-03 claim → stage trace opener ("Stage [ID] automates IB-[NN]") → checkpoint running list → PG-NN coverage column → PG-03/PG-04 audit comparing checkpoint list to T-03 claims. A displacement claim in T-03 that does not appear in the final checkpoint's IB-NN list is a structurally flaggable contradiction between the stage's forward declaration and the trace's coverage evidence.

**2. Recovery role traced directly to T-05 cited row, not just role vocabulary list**

V-01/V-02/V-04 enforce Responsible Role as "from T-01/T-05 vocabulary." V-03 enforces "Finance Controller" or "Operations Analyst." V-05 is the only variation where CMD-24 says "must come from T-05 Responsible Role column" for the specific cited IB-NN row: "For each T-10 row, trace to the IB-NN step cited in that row, find its Responsible Role in T-05, and use that exact role name." This closes the vocabulary-drift gap: a recovery row for IB-03 must carry the exact role from T-05's IB-03 row, not any role from T-05 generally.

**3. IB-anchor framing as response identity, not setup instruction**

V-05 frames the entire response around IB displacement: "the pipeline does not add stages to a blank canvas; it replaces named manual steps." Every stage trace opens with "Stage [ID] automates IB-[NN]: [step name]" and Phase 5 requires identifying the highest-effort IB step by Elapsed Time and confirming its displacement status. This framing makes C-42/C-43/C-44/C-45/C-46 convergent rather than parallel — they all trace to the same T-05 reference artifact, so compliance with one criterion implicitly reinforces the others.

---

## Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|----------------|
| 1 | V-05 | 111.35 | T-03 displacement column + CMD-24 T-05 row tracing + six-level IB verification |
| 2 | V-03 | 111.35 | T-12 dedicated bilateral contract table + T-25 role map (strongest C-46) |
| 3 | V-04 | 111.35 | M_k formula + IB-NN list arithmetic + "who gets paged?" heuristic (strongest C-44 content) |
| 4 | V-01 | 111.35 | Four-tier ACCUMULATION PROTOCOL explicit contract + ORDERING RULE |
| 5 | V-02 | 106.03 | IB-Col?/HO-Col? flags strongest for C-42; Phase 5 gaps in C-06/C-09 |

---

```json
{"top_score": 111.35, "all_essential_pass": true, "new_patterns": ["T-03 IB-NN Steps Replaced column pre-declares per-stage displacement claims before any trace, creating a flaggable contradiction when PG-04 coverage audit does not confirm all T-03 claims", "Recovery Responsible Role must trace to the T-05 row cited (not just T-05 vocabulary list), closing the vocabulary-drift gap between IB step assignment and recovery ownership", "IB-anchor-as-response-identity framing makes C-42 through C-46 convergent rather than parallel — all five criteria reference the single T-05 table produced before the scaffold, so compliance with one reinforces the others"]}
```
