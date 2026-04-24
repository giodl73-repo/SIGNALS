Now I have everything needed to score the variations. Let me evaluate each one.

---

# flow-dataflow — Round 2 Scorecard

**Rubric version:** v2  
**Date:** 2026-03-14  
**Trace artifact:** placeholder (structural evaluation of prompt designs)

---

## Scoring Method

No live trace artifact exists; this round scores the **structural capacity** of each prompt design to produce a passing output. A criterion is **PASS** when the template provides a mechanism that guarantees the criterion behavior; **PARTIAL** when the mechanism is present but relies on declarative compliance without enforcement; **FAIL** when absent.

---

## Criterion Evaluation by Variation

### V-01 — Phrasing Register (Imperative Checkpoint Commands)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Pipeline path in DOMAIN CONTEXT + stage sequence produces unbroken chain |
| C-02 | PASS | `BOUNDARY CHECK` + `STOP. Complete all four lines before writing Stage 2.` + explicit `NONE` requirement |
| C-03 | PASS | `Data loss risk:` field with disqualifying examples ("errors may occur" explicitly rejected) |
| C-04 | PASS | Schema at source + `Schema in / Transform / Schema out` diff per intermediate stage |
| C-05 | PASS | `Latency contribution:` field in every stage block |
| C-06 | PASS | Dedicated `STALE DATA WINDOWS` section, two-row requirement, "Do not combine" instruction |
| C-07 | PASS | DOMAIN CONTEXT gate locks entity names; `Entity: [entity from DOMAIN CONTEXT — not 'record' or 'data']` field enforces reuse in every stage and boundary |
| C-08 | PASS | `RECOVERY PRESCRIPTIONS` table required for every NONE boundary + every loss inventory `no` row; "Add retry logic does not qualify" explicitly excluded |
| C-09 | PASS | 2-column trade-off table with Consistency, Latency, Operational cost dimensions (≥2 dimensions met) |
| C-10 | PASS | `STOP. Fill every field before proceeding to Stage 1.`; entity, consumer, and cadence locked before first stage; "mandatory in every stage block and every BOUNDARY CHECK" |
| C-11 | PASS | STOP command before each boundary + "Writing two consecutive stage blocks without a BOUNDARY CHECK between them is not permitted" — behavioral + negative framing |
| C-12 | PASS | `Domain entity at boundary: [entity name from DOMAIN CONTEXT — 'data' or 'records' fails]` explicit required field with disqualifier stated |

```
Essential passed:     4 / 4   => (4/4) * 60 = 60
Recommended passed:   3 / 3   => (3/3) * 30 = 30
Aspirational passed:  5 / 5   => (5/5) * 10 = 10
                                 Composite    = 100

Golden: YES — all essential PASS, composite = 100
```

**Relative strength:** C-11 is strong (behavioral + negative framing). C-10 is template-forced (vocabulary seeded from blank-filling, not narrative). C-09 is 2-column only. No incumbent enrichment.

---

### V-02 — Inertia Framing (Manual Incumbent First)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Explicit `## DATA LINEAGE CHAIN` section with unbroken-chain instruction per entity; strongest C-01 surface in R2 |
| C-02 | PASS | BOUNDARY CHECK fires after each stage, "must be completed before the next stage opens," explicit NONE |
| C-03 | PASS | Stage `Data loss risk:` + boundary `Loss exposure:` + incumbent comparison; loss points grounded in known failure modes |
| C-04 | PASS | `Schema in / Transform / Schema out` diff per stage |
| C-05 | PASS | `Latency contribution:` per stage |
| C-06 | PASS | Two-row STALE DATA WINDOWS + `vs Incumbent` column; failure-mode row required separately |
| C-07 | PASS | INCUMBENT section seeds entity names from business narrative before DOMAIN CONTEXT template fires; richest C-07 surface after V-05 |
| C-08 | PASS | Recovery prescriptions + `Closes incumbent gap?` column; richer than V-01 |
| C-09 | PASS | 3-column table (incumbent / current / alternative); quantifies improvement over manual process |
| C-10 | PASS | INCUMBENT narrative seeds vocabulary organically before DOMAIN CONTEXT gate; two surfaces for vocabulary lock |
| C-11 | **PARTIAL** | "A BOUNDARY CHECK fires after every stage block and must be completed before the next stage opens" — declarative only; no STOP command before each boundary; no explicit anti-batch prohibition ("do not write two consecutive stage blocks"). Structurally interleaved in template but compliance relies on declarative instruction register, which R1 showed is skip-susceptible |
| C-12 | **PARTIAL** | `Domain entity at boundary:` required field with disqualifier exists, but C-11 partial enforcement lowers confidence that the field appears inline at every boundary rather than in a post-hoc summary |

```
Essential passed:     4 / 4   => (4/4) * 60 = 60
Recommended passed:   3 / 3   => (3/3) * 30 = 30
Aspirational passed:  3 + 0.5 + 0.5 = 4/5   => (4/5) * 10 = 8
                                               Composite    = 98

Golden: YES — all essential PASS, composite = 98 ≥ 80
```

**Relative strength:** Richest C-01 (explicit lineage chain section), C-07, C-09, C-10, C-08 via incumbent linkage. Weakest C-11 of the five variations.

---

### V-03 — Lifecycle Emphasis (Data State Machine)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Stage-state sequence (LIVE → IN-FLIGHT → STAGED → PERSISTED) + pipeline path; chain is encoded in state labels |
| C-02 | PASS | `STATE TRANSITION` gate required between every stage pair; `Error handling:` field mandatory; NONE explicit |
| C-03 | PASS | `Data loss risk:` in stage blocks + `Loss exposure:` in STATE TRANSITION; `State at Loss` column in inventory strengthens specificity |
| C-04 | PASS | `Schema at source`, `Schema in / Transform / Schema out`, plus `Schema delta:` in every STATE TRANSITION; two schema surfaces per stage boundary |
| C-05 | PASS | `Latency contribution:` per stage + `Time-in-transition:` per STATE TRANSITION; additive LIVE→PERSISTED elapsed calculation |
| C-06 | PASS | Stale threshold declared as **contract** in DOMAIN CONTEXT (`Stale threshold: [entity] enters STALE if PERSISTED not reached within N units`) before any stage written; STALE STATE ANALYSIS then derives normal/failure from elapsed time calculation, not synthesized post-hoc |
| C-07 | PASS | DOMAIN CONTEXT gate + `Entity:` required field in every STATE TRANSITION creates independent domain-vocabulary surface at every transition edge |
| C-08 | PASS | Recovery prescriptions + `State-machine fit:` column ("prevents entity stranded IN-FLIGHT" / "enables replay from STAGED"); most precise C-08 framing in R2 |
| C-09 | PASS | State-machine framing of trade-offs: "which states does the alternative eliminate, shorten, or make more recoverable?" + 3 dimensions (Consistency, LIVE→PERSISTED latency, Operational cost) |
| C-10 | PASS | DOMAIN CONTEXT + state machine contract declared before Stage 1; stale threshold and initial/target state in DOMAIN CONTEXT; entity, consumer, cadence all locked |
| C-11 | PASS | STATE TRANSITION is structurally required: each stage block declares an exit-state (`Entity state exiting:`), which is the input contract for the following STATE TRANSITION (`Entity state entering:`); batching is architecturally awkward because exit-state of stage N is undefined until the transition is written. "Do not write the next stage until its STATE TRANSITION is complete" + repeat instruction at bottom |
| C-12 | PASS | `Entity: [entity name from DOMAIN CONTEXT — not 'data' or 'records']` required field in every STATE TRANSITION; disqualifier explicitly stated |

```
Essential passed:     4 / 4   => (4/4) * 60 = 60
Recommended passed:   3 / 3   => (3/3) * 30 = 30
Aspirational passed:  5 / 5   => (5/5) * 10 = 10
                                 Composite    = 100

Golden: YES — all essential PASS, composite = 100
```

**Relative strength:** Strongest C-06 mechanism (contractual threshold before tracing), strongest C-08 (state-machine-fit column), structurally hardest C-11 to batch. No incumbent enrichment means C-10 is template-forced and C-09 is 3-column only vs state-machine framing.

---

### V-04 — Phrasing Register + Inertia Framing

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Pipeline path in PHASE 2 + stage sequence in PHASE 3; lineage chain implicit from stages |
| C-02 | PASS | `BOUNDARY CHECK` + `STOP. Complete all four lines. Do not write Stage 2 until this check is done.` + explicit NONE + "does NONE reproduce a PHASE 1 recovery failure?" |
| C-03 | PASS | Stage `Data loss risk:` + boundary `Loss exposure:` + PHASE 1 comparison; "new automation-introduced failure, or inherited from PHASE 1?" |
| C-04 | PASS | `Schema in / Transform / Schema out` diff per stage |
| C-05 | PASS | `Latency contribution:` per stage |
| C-06 | PASS | `STALE DATA WINDOWS` two rows + "Do not combine" + `vs Incumbent (PHASE 1)` column |
| C-07 | PASS | PHASE 1 incumbent narrative + PHASE 2 DOMAIN CONTEXT; entity names emerge from business story before formal gate; strongest C-07 after V-05 |
| C-08 | PASS | Recovery prescriptions + `Closes PHASE 1 gap?` column; paired to loss inventory and NONE boundaries |
| C-09 | PASS | 3-column (incumbent / current / alternative) with Freshness, Consistency, Operational cost; quantifies improvement over manual process |
| C-10 | PASS | `STOP. Complete all fields before proceeding to PHASE 2.` + `STOP. Lock vocabulary.` + "All entity names established here are mandatory in every stage block, boundary check, stale analysis, and recovery prescription" |
| C-11 | PASS | `STOP. Complete before writing next stage.` + **explicit anti-batch instruction**: "Do not batch all stage blocks first and then write boundary checks. Interleave them." — strongest behavioral anti-batch enforcement in the non-state-machine variations |
| C-12 | PASS | `Domain entity at boundary: [entity name from PHASE 2]` + STOP-phrased instruction; disqualifier noted |

```
Essential passed:     4 / 4   => (4/4) * 60 = 60
Recommended passed:   3 / 3   => (3/3) * 30 = 30
Aspirational passed:  5 / 5   => (5/5) * 10 = 10
                                 Composite    = 100

Golden: YES — all essential PASS, composite = 100
```

**Relative strength:** Best explicit anti-batch instruction for C-11 among non-state-machine variations ("Do not batch all stage blocks first and then write boundary checks. Interleave them."). Narrative-first C-10. 3-column C-09. No state-machine means C-06/C-08 are less structurally grounded than V-03/V-05.

---

### V-05 — Full Synthesis (All Three Axes)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Stage-state sequence + pipeline path; state labels (LIVE → IN-FLIGHT → STAGED → PERSISTED) encode chain |
| C-02 | PASS | `STATE TRANSITION` gate + `STOP. Complete all fields before writing STAGE 2.` + NONE required ("does this reproduce a PHASE 1 recovery failure?") |
| C-03 | PASS | Stage `Data loss risk:` + transition `Loss exposure:` + incumbent comparison ("PHASE 1 failure reproduced, or new failure?"); richest loss-point surface |
| C-04 | PASS | `Schema at source`, `Schema in / Transform / Schema out` + `Schema delta:` in every STATE TRANSITION |
| C-05 | PASS | `Latency contribution:` per stage + `Time-in-transition:` per transition; STALE STATE ANALYSIS sums both |
| C-06 | PASS | Stale threshold declared as **contract in PHASE 2** before any stage written, with `Incumbent stale window:` comparison; STALE STATE ANALYSIS derives both normal and failure-mode from elapsed calculation, plus `vs Incumbent failure` comparison |
| C-07 | PASS | PHASE 1 narrative seeds entity names from business story; STATE TRANSITION `Entity:` field exposes domain vocabulary at every boundary; richest C-07 surface in R2 |
| C-08 | PASS | Recovery prescriptions + `State-machine fit:` ("prevents entity stranded IN-FLIGHT") + `Closes PHASE 1 gap?` columns; richest C-08 surface in R2 |
| C-09 | PASS | 3-column (PHASE 1 incumbent / current / alternative) + state-machine framing ("which states does the alternative eliminate?") + STALE STATE ANALYSIS feeding Freshness row |
| C-10 | PASS | PHASE 1 narrative + PHASE 2 state machine contract + stale threshold; entity/consumer/cadence locked in PHASE 1; state labels force vocabulary reuse at every transition; richest C-10 in R2 |
| C-11 | PASS | STATE TRANSITION structural contract (exit-state feeds next transition as input) + `STOP. Complete all fields before writing STAGE 2.` + "Do not batch stage blocks. Interleave. No two consecutive stage blocks without a STATE TRANSITION. No exceptions." — structural + behavioral + negative framing; strongest C-11 in R2 |
| C-12 | PASS | `Entity: [entity name from PHASE 1 — not 'data' or 'records']` required field in every STATE TRANSITION + STOP; disqualifier explicit; structural guarantee enforced at every boundary |

```
Essential passed:     4 / 4   => (4/4) * 60 = 60
Recommended passed:   3 / 3   => (3/3) * 30 = 30
Aspirational passed:  5 / 5   => (5/5) * 10 = 10
                                 Composite    = 100

Golden: YES — all essential PASS, composite = 100
```

**Relative strength:** Richest mechanism for every single criterion. Only variation that achieves all three: narrative vocabulary seeding (C-10), structural C-11 barrier (state-machine exit-state contract), and state-machine-anchored recovery (C-08).

---

## Variation Rankings

| Rank | V | Composite | Golden | Decisive difference |
|------|---|-----------|--------|---------------------|
| 1 (tied) | **V-05** | 100 | YES | Richest on C-06 (contractual threshold), C-08 (state-machine fit + incumbent gap), C-10 (narrative + state contract), C-11 (structural + behavioral), C-09 (3-column + state framing) |
| 1 (tied) | **V-04** | 100 | YES | Strongest explicit anti-batch instruction for C-11; richest C-10/C-09 among non-state-machine |
| 1 (tied) | **V-03** | 100 | YES | Strongest structural C-11 guarantee; contractual C-06; state-machine-fit C-08 |
| 1 (tied) | **V-01** | 100 | YES | Clean baseline; STOP commands + negative framing; 2-column C-09 (minimal pass) |
| 5 | **V-02** | 98 | YES | Richest C-01 (explicit lineage chain section), C-09 (3-col), C-10 (narrative); weakest C-11/C-12 (declarative only, no STOP command, no anti-batch prohibition) |

---

## Excellence Signals from Top Variation (V-05)

Three structural patterns in V-05 produce criterion-level richness not captured by the current v2 rubric:

**Signal 1 — Contractual stale threshold (C-06 enrichment)**
V-03/V-05 declare the stale threshold as a binding contract in PHASE 2 before any stage is written:
`[entity] enters STALE if PERSISTED not reached within [N units]`. STALE STATE ANALYSIS then derives elapsed time from stage latencies and compares against the declared threshold. This is structurally different from a post-hoc STALE DATA WINDOWS section: the threshold is a precondition to tracing, not a conclusion from tracing. The v2 rubric C-06 only requires the analysis section to appear with two rows — it does not require the threshold to be declared before tracing.

**Signal 2 — State-machine-fit column in recovery prescriptions (C-08 enrichment)**
V-03/V-05 require each recovery prescription to state which state it protects: "prevents entity stranded IN-FLIGHT" / "enables replay from STAGED without re-extracting LIVE." Current C-08 PASS condition only requires a "paired, specific recovery suggestion." State-machine-fit column produces recovery prescriptions that are anchored to state contracts, not just generic mechanism names. A model cannot write "add idempotency key" without specifying which state transition it closes.

**Signal 3 — Incumbent-baseline three-column trade-off (C-09 enrichment)**
V-02/V-04/V-05 produce a 3-column trade-off table (incumbent / current / alternative). Current C-09 requires "Named alternative pattern with at least two quantified or qualified trade-off dimensions." The 3-column form forces the model to quantify what the automated pipeline actually improved over the manual process, not just compare two abstractions. The Freshness row in the STALE STATE ANALYSIS feeds the first column directly, anchoring the trade-off to a calculated value.

**Signal 4 — Phased protocol gate (meta-pattern)**
V-05's `PHASE 1 → PHASE 2 → PHASE 3` protocol with hard STOP gates between phases creates a causal ordering guarantee: vocabulary is seeded from narrative (PHASE 1) → state contracts are declared (PHASE 2) → tracing begins (PHASE 3). No stage can be written before both vocabulary and state contracts are established. This is more robust than a single pre-trace DOMAIN CONTEXT gate because it separates narrative seeding from structural contract declaration.

---

## New Patterns Not Yet in v2 Rubric

Two patterns from V-05 could become v3 aspirational criteria:

1. **Pre-trace stale contract** — stale threshold declared as a contract before Stage 1 (not a section at the end). Encodes the observation that contractual C-06 is structurally stronger than synthetic C-06.
2. **State-anchored recovery prescriptions** — every recovery prescription states which state it protects. Enriches C-08 from "specific mechanism" to "specific mechanism + state contract it closes."

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["contractual stale threshold declared in pre-trace phase before Stage 1 written (not post-hoc section)", "state-machine-fit column in recovery prescriptions anchors each mechanism to a named state contract it protects"]}
```
