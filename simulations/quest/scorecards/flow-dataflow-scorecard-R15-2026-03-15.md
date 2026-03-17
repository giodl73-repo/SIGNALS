# flow-dataflow Round 15 — Scorecard

## Rubric v12 | 5 Variations | C-01–C-28

---

## Scoring Methodology

- Essential C-01–C-04: 14 pts each (56 max)
- Recommended C-05–C-07: 10 pts each (30 max)
- Aspirational C-08–C-28: 0.65 pts each (13.65 max); PARTIAL = 0.33
- Total possible: 99.65

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (C-01–C-04)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Stage enumeration | PASS | PASS | PASS | PASS | PASS |
| **C-02** Error handling at every boundary | PASS | PASS | PASS | PASS | PASS |
| **C-03** Data loss point per stage | PASS | PASS | PASS | PASS | PASS |
| **C-04** Schema state at each stage | PASS | PASS | PASS | PASS | PASS |

All four essential criteria pass in all five variations. Every variation provides `T-03` stage enumeration before any trace begins, mandates `[B-NN->NN] error handling` per stage (or an explicit `NH-NN — no handling — risk accepted` annotation), requires `LP-NN` data loss point per stage, and enforces typed exit manifests plus the `verified: no field added, removed, renamed, or retyped` assertion for unchanged stages.

**Essential sub-total: 56 / 56 all variations.**

---

### Recommended Criteria (C-05–C-07)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-05** Latency characterization | PASS | PASS | PASS | PASS | PASS |
| **C-06** Stale data windows | PASS | PASS | PASS | PASS | PASS |
| **C-07** Domain framing | PASS | PASS | PASS | PASS | PASS |

- C-05: All variants carry per-stage latency annotations plus Transport(ms)/Processing(ms)/Total(ms) decomposition in the boundary inventory.
- C-06: All variants require `Normal: [window]. Failure mode: [separate quantified window]` per stage — the separation is explicit.
- C-07: V-01/V-04 name `Invoice, PurchaseOrder, SKU, LedgerEntry` directly; V-02/V-03 enforce entity inventory before traces; V-05 explicitly forbids "record" or "item" as entity labels.

**Recommended sub-total: 30 / 30 all variations.**

---

### Aspirational Criteria (C-08–C-28)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-08 | Recovery prescriptions | PASS | PASS | PASS | PASS | PASS |
| C-09 | Pattern trade-off analysis | PASS | PASS | PASS | PASS | PASS |
| C-10 | Pre-trace entity inventory | PASS | PASS | PASS | PASS | PASS |
| C-11 | Systematic boundary labeling | PASS | PASS | PASS | PASS | PASS |
| C-12 | Verified-unchanged schema assertion | PASS | PASS | PASS | PASS | PASS |
| C-13 | Structural completeness enforcement | PASS | PASS | PASS | PASS | PASS |
| C-14 | Incumbent baseline anchoring | PASS | PASS | PASS | PASS | PASS |
| C-15 | Structured incumbent baseline table | PASS | PASS | PASS | PASS | PASS |
| C-16 | Full recovery-to-baseline traceability | PASS | PASS | PASS | PASS | PASS |
| C-17 | Entity-at-risk annotation per boundary | PASS | PASS | PASS | PASS | PASS |
| C-18 | Structured recovery audit table | PASS | PASS | PASS | PASS | PASS |
| C-19 | Typed stage-exit manifests | PASS | PASS | PASS | PASS | PASS |
| C-20 | Field-level entity-at-risk traceability | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-21 | Decomposed boundary latency | PASS | PASS | PASS | PASS | PASS |
| C-22 | Cumulative SLA% with domination point | PASS | PASS | PASS | PASS | PASS |
| C-23 | Structurally separate closure gate | PASS | PASS | PASS | PASS | PASS |
| C-24 | Pre-declared complete output scaffold | PASS | PASS | PASS | **PARTIAL** | PASS |
| C-25 | Stage-to-role assignment map | PASS | PASS | PASS | PASS | PASS |
| C-26 | Pre-trace FM-NN register + lifecycle resolution | PASS | PASS | PASS | PASS | PASS |
| C-27 | FM-NN resolution section scaffold pre-registration | PASS | PASS | PASS | PASS | PASS |
| C-28 | Inline FM-NN acknowledgment with deferred resolution | PASS | PASS | PASS | PASS | PASS |

---

#### Aspirational Evidence Notes

**C-20 — PARTIAL all variations**: Every variant provides an "Entity at Risk" column (satisfying C-17's entity-name requirement) plus a separate or combined `entity.field` column (satisfying field-level identification). However, C-20's pass condition specifies the combined notation `entity.field_name — risk description` with an inline risk description. No variation's boundary inventory design explicitly enforces the `— risk description` suffix in a single cell. The information is present across two columns but not in the required combined format. All receive 0.33 pts.

**C-24 — PARTIAL V-04 only**: V-04's inertia design produces T-01 (Incumbent Baseline) in PHASE 1 _before_ the output scaffold is declared in PHASE 2. The scaffold does retroactively list T-01 with the note "[already produced in PHASE 1]", and T-01 does not appear mid-trace. However, the C-24 navigational contract requirement ("declares every output table…before the first stage trace entry") implies pre-declaration before first _appearance_, not just before first trace. T-01 appears before it can be consulted in the scaffold, weakening the navigational contract for that artifact. PARTIAL (0.33 pts).

**C-27 — PASS all variations**: All five variations explicitly name the FM-NN resolution section in the STEP 0 / Phase 1 scaffold before Stage 1 traces, using language equivalent to "FM-NN lifecycle resolution audit" with dependency citation (T-02 or equivalent prediction register). This is a full-round baseline achievement — R15's primary design target.

**C-28 — PASS all variations**: All five incorporate inline acknowledgments during stage traces with explicit deferral statements. V-02's structural mechanism is strongest: a running Inline Acknowledgment Log (T-07) where each stage block appends rows rather than embedding prose notes, making accumulated evidence visible as a table artifact before resolution commits. V-01/V-03/V-04 use explicit per-stage acknowledgment bullet format with `— resolution deferred to T-07 (Phase N)`. V-05 uses `— resolution deferred to T-07` with an explanatory note: "That's it — no status decision yet. Evidence accumulates across stages before you resolve anything."

**C-25 — PASS all**: V-03 activates the multi-role path (Commerce → Operations → Finance) and includes a Stage-to-Role Assignment Map in STEP 0 with "Every stage from T-03 must appear." Single-role designs (V-01, V-02, V-04, V-05) satisfy by default.

**C-14/C-15/C-16 — V-04 strongest**: V-04's "Recovery Framing" column specifies `Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency]` — the most explicit step-level fallback framing in any variation. The 5-row minimum on T-01 (vs. 4-row in other variations) and individually referenceable `IB-NN` identifiers make V-04 the strongest C-16 design despite its C-24 PARTIAL.

**C-22 — V-02 strongest**: V-02 presents the Domination Point as a named dedicated table (`| Domination Boundary | Exact Cumulative SLA% | Justification |`) rather than inline prose, converting the SLA budget finding into a referenceable structured artifact.

---

## Score Summary

| Criteria | Max | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|-----|------|------|------|------|------|
| Essential (×14) | 56.00 | 56.00 | 56.00 | 56.00 | 56.00 | 56.00 |
| Recommended (×10) | 30.00 | 30.00 | 30.00 | 30.00 | 30.00 | 30.00 |
| Aspirational (×0.65, PARTIAL=0.33) | 13.65 | 13.33 | 13.33 | 13.33 | 13.01 | 13.33 |
| **Total** | **99.65** | **99.33** | **99.33** | **99.33** | **99.01** | **99.33** |

**Aspirational breakdown**: 20 PASS (13.00) + 1 PARTIAL C-20 (0.33) = 13.33 for V-01/V-02/V-03/V-05. V-04: 19 PASS (12.35) + 2 PARTIAL C-20/C-24 (0.66) = 13.01.

---

## Variation Ranking

| Rank | Variation | Score | Distinguishing Factor |
|------|-----------|-------|-----------------------|
| 1 | **V-02** | 99.33 | Running acknowledgment log table (T-07) as structural C-28 enforcement; per-stage Boundary Annotation Table; Domination Point as named table artifact |
| 2 | **V-01** | 99.33 | Phase completion guards ("PHASE N COMPLETE when…Declare: 'PHASE N COMPLETE'") prevent partial-phase errors; back-fill protocol for T-04 entity.field stubs well-defined |
| 3 | **V-03** | 99.33 | Multi-role design with "Predicting Role" column in T-02; per-role FM-NN attribution enables cross-role resolution validation; Commerce-first sequencing establishes entity.field vocabulary early |
| 4 | **V-05** | 99.33 | Compressed checklist format confirms structural compliance achievable without phase-gate overhead; imperative register compensates for compressed lifecycle on domain framing (C-07) |
| 5 | **V-04** | 99.01 | Richest C-14/C-15/C-16 design (baseline-first framing, 5-row minimum, "Recovery Framing" column); penalized by C-24 PARTIAL for T-01 pre-scaffold appearance; "T-01 Manual Safeguard at Risk" column in prediction register is the strongest novel pattern not in any other variation |

---

## Excellence Signals (from V-02 — Top Variation)

**ES-1: Running FM-NN acknowledgment log table (T-07)** — Instead of per-stage prose acknowledgment bullets, V-02 designates T-07 as a running log table. Each stage block appends rows with the mini-table "T-07 rows appended this stage." The consolidated T-07 table appears after all stage traces and is explicitly consumed by T-08 (resolution audit). This converts C-28's deferred-acknowledgment discipline from a prose expectation into a structural table-append protocol — omission is visible as a missing row.

**ES-2: Separate log vs. resolution artifacts** — V-02 distinguishes T-07 (Inline Acknowledgment Log: FM-NN, Stage ID, Boundary/Condition, Deferral Statement) from T-08 (FM-NN Resolution Audit: FM-NN, Status, T-07 Entries Consulted, Evidence/Reason). The scaffold declaration in STEP 0 registers both with explicit dependency (`T-08 depends on T-02, T-07`). This makes the evidence-accumulation chain structurally traceable: stage traces → T-07 rows → T-08 resolution draws on T-07 entries.

**ES-3: Stage Boundary Annotation Table per stage** — V-02's stage trace block contains a sub-table with columns `Boundary | Error Handling (mechanism or NH-NN label) | Data Loss Point (LP-NN label) | Latency | Normal Stale Window | Failure-Mode Stale Window`. This collapses C-02, C-03, C-05, and C-06 into a single co-located table per stage, making gaps structurally visible at the stage level — a missing cell in any column is an immediate C-compliance gap.

**ES-4: Domination Point as named table artifact** — V-02 presents the domination point as a dedicated single-row table (`| Domination Boundary | Exact Cumulative SLA% | Justification (one sentence, domain-grounded) |`) rather than a prose block following the boundary inventory. This converts the finding into a citable, referenceable artifact.

---

## Notable Pattern from V-04 (Not in Top, Still Excellence Signal)

**ES-5: "T-01 Manual Safeguard at Risk" column in FM-NN prediction register** — V-04's T-03 (prediction register) adds a column naming the specific manual safeguard from T-01 that each predicted failure mode bypasses. This pre-declares the automation gap at prediction time, before stage traces begin. The corresponding T-07 resolution column is "T-01 Safeguard That Confirmed or Exonerated" — creating bidirectional traceability: prediction → manual safeguard bypassed → resolution citing whether the pipeline retained or eliminated the safeguard. This is the strongest C-26 evidence chain design in R15 and a candidate for R16 adoption.

---

```json
{"top_score": 99.33, "all_essential_pass": true, "new_patterns": ["Running FM-NN acknowledgment log table (T-07) accumulates rows across all stage traces via per-stage append mini-tables — converts C-28 deferred-acknowledgment discipline from prose expectation into structural table-append protocol where omission is a missing row; separate log artifact (T-07) consumed by resolution audit (T-08) makes evidence accumulation chain explicitly traceable in the scaffold", "Stage Boundary Annotation Table per stage collapses C-02 error handling, C-03 loss point, C-05 latency, and C-06 stale window into a single co-located sub-table per stage — gaps are structurally visible at stage level as missing cells rather than requiring cross-section inspection", "FM-NN prediction register includes a 'T-01 Manual Safeguard at Risk' column naming the specific pre-automation safeguard each failure mode bypasses — pre-declares automation exposure at prediction time; resolution section column 'T-01 Safeguard That Confirmed or Exonerated' creates bidirectional traceability from failure prediction through manual safeguard to resolution status"]}
```
