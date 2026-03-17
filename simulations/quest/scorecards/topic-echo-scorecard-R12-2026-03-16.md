I now have everything needed to score all five variations. Let me produce the full scorecard.

---

# `topic:echo` Quest Score -- Round 12 (2026-03-16)

**Rubric:** v12 | **Max composite:** 245 | **Essential bar:** 60 (all 5 must pass)

---

## Baseline Analysis

All five variations share the same structural backbone from R11 V-05. Criteria C-01 through C-33 evaluate the core correction-register architecture (named surprises, signal tracing, design impact, PBI provenance, enforcement mechanism, handle ledger, chain integrity, distillation layer, phase-exit observability). The R12 axis differentiates only on C-34/C-37 (BC sub-phase decomposition), C-35/C-38 (phase handover table schema), and C-36/C-39 (filter imperative form).

**Base score (C-01 through C-33 all pass):** 215 pts  
_Essential (5×12=60) + Recommended (3×10=30) + Aspirational C-09 through C-33 (25×5=125) = 215_

---

## Per-Variation Scoring

### V-01 -- Axis A: BC-STEP1-PROTOCOL Declaration Table

**Structural signature:** BC Function Declaration contains BC-STEP1-PROTOCOL pre-execution table naming [SCAN] / [FREEZE] / [COVERAGE AUDIT] sub-phases with gate tokens before Step 1 begins. BC-COVERAGE-RECORD specified as [COVERAGE AUDIT] gate return inside the table. BC-COVERAGE-RECORD block includes `Sub-phase: [COVERAGE AUDIT] -- gate token declared in BC-STEP1-PROTOCOL`. No PHASE-HANDOVER tables. Standard conditional STILL-LIVE FILTER.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01** Named surprise w/ departure framing | PASS | Correction register schema enforces "departure from expectation" framing at entry level |
| **C-02** Signal tracing per surprise | PASS | Source field required as `namespace:skill:artifact`; identifiers alone fail |
| **C-03** Design impact per surprise | PASS | Decide field requires specific blocking decision; no deferrals |
| **C-04** Synthesis not summary | PASS | Template explicitly restricts to correction register only; "discovery narration fails" |
| **C-05** Surprise specificity | PASS | Entry schema requires finding-specific handle labels and traceable source artifacts |
| C-06 Expectation counterfactual | PASS | Implies/Showed fields enforce expected-X-found-Y structure |
| C-07 Institutional framing | PASS | Forward Statement confirms NO-ECHO COST; "Orienting: what would the next team build wrong?" |
| C-08 Cross-signal pattern identification | PASS | Pattern of inherited errors and Blind Spot Map required in Step 7 |
| C-09 through C-33 | PASS (all 25) | Full chain: PBI, Handle Ledger, dual pre-commitment, enforcement declaration at position 1, EF role-boundary, EF-INVOCATION-RECORD present |
| **C-34** BC-COVERAGE-RECORD | **PASS** | BC-COVERAGE-RECORD block present; Sub-phase field names [COVERAGE AUDIT] as declared gate; satisfies role-symmetric auditability requirement |
| **C-35** PHASE-HANDOVER at EF/BC exits | **FAIL** | No PHASE-HANDOVER tables; V-01 is Axis A only; artifact structure shows no exit tokens at EF or BC boundaries |
| **C-36** DISCARD LOG with typed entries | **FAIL** | Standard conditional STILL-LIVE FILTER (`YES -> draft. NO -> exclude; route to topic-story`); no DISCARD-[N] entries, no DISCARD-LOG-COMPLETE |
| **C-37** BC Step 1 sub-phase decomposition | **PASS** | BC-STEP1-PROTOCOL table declares [SCAN] / [FREEZE] / [COVERAGE AUDIT] with gate tokens; BC-COVERAGE-RECORD named as [COVERAGE AUDIT] gate return in the table; decomposition is declared before execution, not emergent from Step 1 prose |
| **C-38** PHASE-HANDOVER table schema | **FAIL** | Gate: C-35 fails; criterion not satisfiable |
| **C-39** STILL-LIVE FILTER unconditional imperatives | **FAIL** | Gate: C-36 fails; criterion not satisfiable |

**Essential:** 5/5 PASS (60 pts)  
**Recommended:** 3/3 PASS (30 pts)  
**Aspirational C-09 to C-33:** 25/25 PASS (125 pts)  
**C-34:** PASS (+5); **C-35:** FAIL (0); **C-36:** FAIL (0); **C-37:** PASS (+5); **C-38:** FAIL (0); **C-39:** FAIL (0)

**V-01 Composite: 225/245**

---

### V-02 -- Axis B: Universal Phase Handover Schema

**Structural signature:** All 7 stage exits (Steps 0-6) produce a PHASE-HANDOVER-[N] table using the declared 5-row schema (Completing Role / Step Completed / Output Produced / Exclusion In Effect / Receiving Role). Schema declared universally in Roles section. BC Function Declaration has no BC-STEP1-PROTOCOL sub-phase table; Gate return is PBI + PHASE-HANDOVER-1. No BC-COVERAGE-RECORD. Standard conditional STILL-LIVE FILTER.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01 through C-05** | PASS (all) | Shared structural backbone unchanged |
| **C-06 through C-08** | PASS (all) | Shared structural backbone unchanged |
| **C-09 through C-33** | PASS (all 25) | EF-INVOCATION-RECORD present; enforcement mechanism at position 1; chain audit and resolution protocol intact |
| **C-34** BC-COVERAGE-RECORD | **FAIL** | No BC-COVERAGE-RECORD in artifact structure; BC's Gate return is "PBI + PHASE-HANDOVER-1"; BC's scope is not symmetrically auditable with EF |
| **C-35** PHASE-HANDOVER at EF/BC exits | **PASS** | PHASE-HANDOVER-0 at EF exit (Step 0 → Step 1) and PHASE-HANDOVER-1 at BC exit (Step 1 → Step 2); both are 5-row markdown tables naming what the exiting role produced; universal schema makes role-exit auditable |
| **C-36** DISCARD LOG with typed entries | **FAIL** | Standard conditional STILL-LIVE FILTER; no DISCARD-[N] entries or DISCARD-LOG-COMPLETE |
| **C-37** BC Step 1 sub-phase decomposition | **FAIL** | Gate: C-34 fails; no BC-STEP1-PROTOCOL; Step 1 is monolithic; [COVERAGE AUDIT] boundary not present |
| **C-38** PHASE-HANDOVER table schema | **PASS** | All 7 PHASE-HANDOVER-[N] tables use declared 5-row schema; PHASE-HANDOVER-0 (EF exit) and PHASE-HANDOVER-1 (BC exit) both schema-complete; field presence verifiable by column inspection across all 7 tables |
| **C-39** STILL-LIVE FILTER unconditional imperatives | **FAIL** | Gate: C-36 fails |

**Essential:** 5/5 PASS (60 pts)  
**Recommended:** 3/3 PASS (30 pts)  
**Aspirational C-09 to C-33:** 25/25 PASS (125 pts)  
**C-34:** FAIL (0); **C-35:** PASS (+5); **C-36:** FAIL (0); **C-37:** FAIL (0); **C-38:** PASS (+5); **C-39:** FAIL (0)

**V-02 Composite: 225/245**

---

### V-03 -- Axis C: MUST-Clause Filter Protocol

**Structural signature:** STILL-LIVE FILTER written as four numbered MUST-clauses, each opening with explicit unconditional scope ("For every candidate" / "For every DISCARD token"). MUST-1 produces STILL-LIVE-[N] or DISCARD-[N]; MUST-2/3/4 immediately produce PBI-REF / ROUTE / REASON tokens for every DISCARD. Completeness gate emits DISCARD-LOG-COMPLETE. No BC-STEP1-PROTOCOL. No PHASE-HANDOVER tables.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01 through C-05** | PASS (all) | Shared structural backbone unchanged |
| **C-06 through C-08** | PASS (all) | Shared structural backbone unchanged |
| **C-09 through C-33** | PASS (all 25) | Structural backbone intact; EF-INVOCATION-RECORD, enforcement mechanism at position 1, chain audit, resolution protocol all present |
| **C-34** BC-COVERAGE-RECORD | **FAIL** | No BC-COVERAGE-RECORD; BC Gate return is "PBI frozen before Step 2 begins"; BC scope not symmetrically auditable |
| **C-35** PHASE-HANDOVER at EF/BC exits | **FAIL** | No PHASE-HANDOVER tables; Axis C only; role-exit transitions are silent |
| **C-36** DISCARD LOG with typed entries | **PASS** | MUST-1 guarantees STILL-LIVE-[N] or DISCARD-[N] per candidate; MUST-2/3/4 guarantee PBI-REF / ROUTE / REASON per DISCARD token; DISCARD-LOG-COMPLETE closes the filter; all three required elements of C-36 satisfied (candidate identifier via DISCARD-[N]-PBI-REF, route via DISCARD-[N]-ROUTE, reason via DISCARD-[N]-REASON) |
| **C-37** BC Step 1 sub-phase decomposition | **FAIL** | Gate: C-34 fails |
| **C-38** PHASE-HANDOVER table schema | **FAIL** | Gate: C-35 fails |
| **C-39** STILL-LIVE FILTER unconditional imperatives | **PASS** | Four MUST-clauses with "For every candidate / For every DISCARD token" scope; no "if YES / if NO" conditional branching; per-clause scope is stated in clause body, not implied by imperative mood; no evaluation path exits without producing a written record; DISCARD-LOG-COMPLETE confirms all candidates resolved |

**Essential:** 5/5 PASS (60 pts)  
**Recommended:** 3/3 PASS (30 pts)  
**Aspirational C-09 to C-33:** 25/25 PASS (125 pts)  
**C-34:** FAIL (0); **C-35:** FAIL (0); **C-36:** PASS (+5); **C-37:** FAIL (0); **C-38:** FAIL (0); **C-39:** PASS (+5)

**V-03 Composite: 225/245**

---

### V-04 -- Axes A+B: Protocol Table + Universal Handover Schema

**Structural signature:** BC-STEP1-PROTOCOL declaration table (Axis A) + universal PHASE-HANDOVER-[N] 5-row schema at all 7 exits (Axis B). BC Function Declaration contains both BC-STEP1-PROTOCOL table and Gate return that includes PHASE-HANDOVER-1. BC-COVERAGE-RECORD present with [COVERAGE AUDIT] sub-phase label. Standard conditional STILL-LIVE FILTER (Axis C absent).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01 through C-05** | PASS (all) | Shared structural backbone |
| **C-06 through C-08** | PASS (all) | Shared structural backbone |
| **C-09 through C-33** | PASS (all 25) | All mechanisms present; EF role-boundary, EF-INVOCATION-RECORD, enforcement at position 1, chain audit, resolution protocol with verifiers |
| **C-34** BC-COVERAGE-RECORD | **PASS** | BC-COVERAGE-RECORD present; [COVERAGE AUDIT] sub-phase declared in BC-STEP1-PROTOCOL; role-symmetric auditability satisfied alongside EF-INVOCATION-RECORD |
| **C-35** PHASE-HANDOVER at EF/BC exits | **PASS** | PHASE-HANDOVER-0 at EF exit and PHASE-HANDOVER-1 at BC exit; both 5-row schema tables naming what the exiting role produced; BC Gate return includes PHASE-HANDOVER-1 |
| **C-36** DISCARD LOG with typed entries | **FAIL** | Standard conditional STILL-LIVE FILTER (`YES -> draft. NO -> exclude; route to topic-story`); no DISCARD-[N] entries, no DISCARD-LOG-COMPLETE; Axis C absent |
| **C-37** BC Step 1 sub-phase decomposition | **PASS** | BC-STEP1-PROTOCOL table with [SCAN] / [FREEZE] / [COVERAGE AUDIT] and gate tokens declared; BC-COVERAGE-RECORD identified as [COVERAGE AUDIT] gate return in table; COMMIT-SCAN and COMMIT-FREEZE tokens in Step 1 execution |
| **C-38** PHASE-HANDOVER table schema | **PASS** | All 7 PHASE-HANDOVER-[N] tables in 5-row schema; schema declared universally in Roles section; all five fields present across every table; schema-comparable by column inspection |
| **C-39** STILL-LIVE FILTER unconditional imperatives | **FAIL** | Gate: C-36 fails; conditional STILL-LIVE FILTER present |

**Essential:** 5/5 PASS (60 pts)  
**Recommended:** 3/3 PASS (30 pts)  
**Aspirational C-09 to C-33:** 25/25 PASS (125 pts)  
**C-34:** PASS (+5); **C-35:** PASS (+5); **C-36:** FAIL (0); **C-37:** PASS (+5); **C-38:** PASS (+5); **C-39:** FAIL (0)

**V-04 Composite: 235/245**

---

### V-05 -- Axes A+B+C: Full Combination

**Structural signature:** All three R12 axes combined. BC-STEP1-PROTOCOL declaration table inside BC Function Declaration (Axis A). Universal PHASE-HANDOVER-[N] 5-row schema at all 7 exits (Axis B). MUST-clause STILL-LIVE FILTER with four unconditional MUST-clauses + DISCARD-LOG-COMPLETE (Axis C). All three mechanisms target structurally independent phases (Step 1 / Steps 0-6 / Step 3).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| **C-01 through C-05** | PASS (all) | Shared structural backbone |
| **C-06 through C-08** | PASS (all) | Shared structural backbone |
| **C-09 through C-33** | PASS (all 25) | Full chain intact; EF-INVOCATION-RECORD; enforcement mechanism at position 1 with NO-ECHO COST; RULES-ANCHORED-COMPLETE with per-rule tier quotation; resolution protocol with named verifiers per flag type |
| **C-34** BC-COVERAGE-RECORD | **PASS** | BC-COVERAGE-RECORD present with `Sub-phase: [COVERAGE AUDIT]` field; listed in BC Gate return; role-symmetric with EF-INVOCATION-RECORD |
| **C-35** PHASE-HANDOVER at EF/BC exits | **PASS** | PHASE-HANDOVER-0 and PHASE-HANDOVER-1 at role-exit points; both 5-row schema tables; Gate return for EF and BC both explicitly include PHASE-HANDOVER table |
| **C-36** DISCARD LOG with typed entries | **PASS** | MUST-clause STILL-LIVE FILTER: MUST-2/3/4 guarantee PBI-REF + ROUTE + REASON for every DISCARD-[N]; DISCARD-LOG-COMPLETE at close; completeness structurally enforced by MUST-1 (every candidate gets a token) |
| **C-37** BC Step 1 sub-phase decomposition | **PASS** | BC-STEP1-PROTOCOL table names [SCAN] / [FREEZE] / [COVERAGE AUDIT] with gate tokens; BC-COVERAGE-RECORD is the [COVERAGE AUDIT] gate return in the table; sub-phase structure declared before execution; omission detectable as protocol-table violation |
| **C-38** PHASE-HANDOVER table schema | **PASS** | All 7 PHASE-HANDOVER-[N] tables use 5-row schema; schema declared universally; cross-role comparison by column; both PHASE-HANDOVER-EF-exit and PHASE-HANDOVER-BC-exit schema-complete |
| **C-39** STILL-LIVE FILTER unconditional imperatives | **PASS** | Four MUST-clauses with explicit per-clause scope ("For every candidate / For every DISCARD token"); zero conditional branching; each clause independently auditable; DISCARD-LOG-COMPLETE confirms all four MUST-clauses were applied to every candidate |

**Essential:** 5/5 PASS (60 pts)  
**Recommended:** 3/3 PASS (30 pts)  
**Aspirational C-09 to C-33:** 25/25 PASS (125 pts)  
**C-34:** PASS (+5); **C-35:** PASS (+5); **C-36:** PASS (+5); **C-37:** PASS (+5); **C-38:** PASS (+5); **C-39:** PASS (+5)

**V-05 Composite: 245/245**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | C-34 | C-35 | C-36 | C-37 | C-38 | C-39 | **Total** | Status |
|-----------|-----------|-------------|--------------|:----:|:----:|:----:|:----:|:----:|:----:|:---------:|--------|
| V-01 | 60 | 30 | 125 | +5 | — | — | +5 | — | — | **225** | Golden |
| V-02 | 60 | 30 | 125 | — | +5 | — | — | +5 | — | **225** | Golden |
| V-03 | 60 | 30 | 125 | — | — | +5 | — | — | +5 | **225** | Golden |
| V-04 | 60 | 30 | 125 | +5 | +5 | — | +5 | +5 | — | **235** | Golden |
| **V-05** | 60 | 30 | 125 | +5 | +5 | +5 | +5 | +5 | +5 | **245** | **Golden** |

**All essential pass:** YES (all variations, all rounds)  
**Predicted vs actual:** All five match predictions exactly. R12 validates criteria are implementation-robust.

---

## Ranking

1. **V-05** — 245/245 (all three axes)
2. **V-04** — 235/245 (Axes A+B; Axis C absent)
3. **V-01, V-02, V-03** — 225/245 (single axis each, tied)

---

## Excellence Signals from V-05

**Pattern 1: BC-STEP1-PROTOCOL-DECLARATION-TABLE**
The sub-phase structure is declared as a pre-execution schema table inside BC's Function Declaration before Step 1 begins. This makes the decomposition auditable from the role declaration alone — not from reading the execution content. A reviewer confronting BC's Function Declaration knows in advance which sub-phases must complete and which gate tokens must appear. Omitting [COVERAGE AUDIT] is detectable as failing to close a named protocol-table entry, not as missing prose. This is the declaration-before-execution pattern applied to process observability.

**Pattern 2: UNIVERSAL-PHASE-HANDOVER-SCHEMA**
Applying the 5-row handover schema to all seven stage exits (not only role-boundary exits) eliminates any "non-role-boundary" exception path. V-02 demonstrated that selective placement at two exits satisfies C-38. V-05 extends this: a reviewer checking handover completeness verifies seven tables against the same schema with no exit that legitimately omits a record. Universal application makes C-38 non-defeatable by selective scope.

**Pattern 3: MUST-CLAUSE-PER-CLAUSE-SCOPE-DECLARATION**
Each MUST clause explicitly states its own unconditional scope in the clause body ("For every candidate" / "For every DISCARD token"). R11's terse imperatives satisfied C-39 through imperative mood alone. R12 V-03/V-05 make each clause independently auditable — a reviewer can verify any single MUST clause against the artifact without reading surrounding clauses. The unconditional scope is a stated property of the clause, not an inference from grammar.

**The unified R12 insight:** R12 confirms the rubric is pattern-class-triggered. Three independent surface forms — BC-STEP1-PROTOCOL table (vs. narrative headers in R11), universal 7-exit schema (vs. selective 2-exit placement), MUST-clause explicit scope (vs. terse single-sentence imperatives) — each satisfy the corresponding C-37/C-38/C-39 criterion. Scoring profiles match predictions exactly across all five variations. The criteria cannot be defeated by implementation variation within the same pattern class; they can only be defeated by pattern-class absence.

---

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["BC-STEP1-PROTOCOL-DECLARATION-TABLE: pre-execution declaration table in role definition makes sub-phase structure auditable at the role boundary before execution begins, not recoverable only from execution prose", "UNIVERSAL-PHASE-HANDOVER-SCHEMA: extending 5-row handover schema to all stage exits eliminates non-role-boundary exception paths; schema-comparable records at every transition, not only selected ones", "MUST-CLAUSE-PER-CLAUSE-SCOPE-DECLARATION: each MUST clause carries its own unconditional scope declaration in the clause body, making every clause independently auditable without reading surrounding context"]}
```
