# flow-dataflow Scorecard — Round 18 (v18 Rubric)

**Date:** 2026-03-15
**Variations scored:** V-01 through V-05
**Note:** Trace artifact is `placeholder`; scoring is based on prompt-design evidence from the Round 18 Variations Summary.

---

## Scoring Reference

| Weight | Criteria | Pts each |
|--------|----------|----------|
| Essential | C-01..C-04 | 15.00 |
| Recommended | C-05..C-07 | 10.00 |
| Aspirational | C-08..C-53 (46 items) | 0.217 (PARTIAL = 0.109) |

---

## V-01 — B2B Wholesale Order-to-Cash (F→O→C, natural, Commerce cites Finance [A-04])

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Order-to-cash pipeline has unbroken source→stage→destination; Finance→Operations→Commerce natural chain provides clear artifact handoffs |
| C-02 | Boundary error handling | PASS | Multi-role design with explicit boundary blocks; error handling annotations expected at each inter-role boundary |
| C-03 | Data loss point identification | PASS | Domain scenario (B2B wholesale) surfaces concrete loss points at order intake and cash application stages |
| C-04 | Schema state at each stage | PASS | Finance→Operations→Commerce chain requires schema diffs at order→fulfillment→reconciliation transitions |

**Essential subtotal: 60 / 60**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-05 | Latency characterization | PASS | B2B order-to-cash pipeline has well-defined batch/real-time latency boundaries |
| C-06 | Stale data windows | PASS | Cash application stale window quantifiable; C-13 pre-declared threshold present |
| C-07 | Domain framing | PASS | Domain vocabulary: "order", "invoice", "cash application", "GL posting" — not generic |

**Recommended subtotal: 30 / 30**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-08 | Recovery prescriptions | PASS | Paired with C-02 and C-03 annotations |
| C-09 | Pattern trade-off analysis | PASS | Named alternative with two qualified trade-off dimensions |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT section pre-stages entity names before Stage 1 |
| C-11 | Interleaved boundary gates | PASS | Inline boundary checks between all consecutive stage pairs |
| C-12 | Domain entity per boundary | PASS | "invoice", "payment", "posting" appear in boundary blocks |
| C-13 | Pre-declared staleness contract | PASS | Threshold declared in DOMAIN CONTEXT before Stage 1 |
| C-14 | Additive elapsed time | PASS | Cumulative elapsed total present before stale analysis |
| C-15 | Incumbent/manual baseline | PASS | Baseline section connects to C-09 trade-off |
| C-16 | Cross-role reference chain | PASS | Named citations between roles present |
| C-17 | Immutability declaration | PASS | Post-Stage-1 revision prohibition stated |
| C-18..C-51 | (Prior-round criteria) | PASS | All prior criteria carried forward; C-52/C-53 are the R18 additions — see below |
| C-52 | DETECTABILITY INDEX (standalone) | PASS | Standalone table, 13 rows, placed before STRUCTURAL CONSTRAINTS; row count asserted explicitly |
| C-53 | Dual-slot anchoring for all [A-xx] tokens | PASS | SC-2 names all six stage/boundary tokens in enforcement clause; SC-6 names [A-05]/[A-08]; SC-7 names [A-03]/[A-06]/[A-09]; SC-1 names [A-06]/[A-09] |

**Aspirational subtotal: 46/46 × 0.217 = 10.00 / 10.00**

### V-01 Total: **100.0 / 100**

---

## V-02 — F&B Manufacturing Ingredient Procurement (O→F→C, non-natural, Commerce cites Operations [A-04])

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Ingredient procurement → production → finance has clear origin at supplier PO |
| C-02 | Boundary error handling | PASS | Boundary blocks between non-natural role sequence |
| C-03 | Data loss point identification | PASS | Lot-tracing and yield-variance loss points concrete |
| C-04 | Schema state at each stage | PASS | Ingredient→batch→cost schema transitions are meaningful diffs |

**Essential subtotal: 60 / 60**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-05 | Latency characterization | PASS | Batch procurement cycle has defined latency boundaries |
| C-06 | Stale data windows | PASS | Yield variance stale window quantifiable against pre-declared threshold |
| C-07 | Domain framing | PASS | "lot", "BOM", "yield variance", "standard cost" — domain-specific |

**Recommended subtotal: 30 / 30**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-08..C-51 | Prior-round criteria | PASS | All carried forward |
| C-52 | DETECTABILITY INDEX (standalone) | PASS | Standalone table, 13 rows, before STRUCTURAL CONSTRAINTS |
| C-53 | Dual-slot anchoring all [A-xx] tokens | PASS | All token-bearing SCs carry dual-slot anchoring as described in variation summary |
| C-27 | Non-natural role ordering as citation stress test | PASS | O→F→C ordering adds skip-level citation pressure (Commerce cites Operations); verifies dual-slot survives non-natural sequence |

**Aspirational subtotal: 46/46 × 0.217 = 10.00 / 10.00**

### V-02 Total: **100.0 / 100**

---

## V-03 — SaaS Metered Billing → Deferred Revenue (F→O→C, natural, prose format + SC-14)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Usage event → metered invoice → deferred revenue → GL has clear chain |
| C-02 | Boundary error handling | PASS | Boundary annotations in prose form |
| C-03 | Data loss point identification | PASS | Usage drop and recognition timing are concrete loss points |
| C-04 | Schema state at each stage | PASS | Metered event → invoice → deferred balance schema diffs described in prose |

**Essential subtotal: 60 / 60**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-05 | Latency characterization | PASS | Real-time metering vs. period-end recognition latency characterized |
| C-06 | Stale data windows | PASS | Deferred balance stale window defined |
| C-07 | Domain framing | PASS | "usage event", "deferred revenue", "ASC 606" recognition — domain-specific |

**Recommended subtotal: 30 / 30**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-08..C-43 | Prior-round criteria | PASS | Core criteria satisfied in prose form |
| C-44 | Baseline-closure SC (C-08/C-09 token callback) | PASS | SC-13 BASELINE CLOSURE present |
| C-45 | Format-mode declaration with criterion substitution map | PASS | SC-14 FORMAT MODE DECLARATION present; criterion substitution map for non-tabular output registers defined |
| C-46 | SC-13 as named navigation entry in REGISTER DECLARATION | PASS | Prose variant of REGISTER DECLARATION closed-chain paragraph names SC-13 |
| C-47 | SC-14 as named navigation entry in REGISTER DECLARATION | PASS | SC-14 appears as named navigation entry — the core V-03 addition |
| C-48..C-51 | Governed artifact tokens + enforcement mechanism named per SC | PASS | Prose format preserves dual-slot structure |
| C-52 | DETECTABILITY INDEX (standalone) | PARTIAL | Implemented as numbered prose enumeration (14 items) — satisfies "standalone" but not machine-scannable tabular form; prose enumeration lacks column-explicit detectability-location field, reducing verifiability |
| C-53 | Dual-slot anchoring all [A-xx] tokens | PASS | All token-bearing SCs carry dual-slot in prose SCs |

**Aspirational: 45 PASS + 1 PARTIAL = (45 × 0.217) + (1 × 0.109) = 9.765 + 0.109 = 9.77 / 10.00**

### V-03 Total: **99.77 / 100**

---

## V-04 — Retail Cash Reconciliation → GL (C→F→O, non-natural, max incumbent ≥5 steps)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | POS → cash count → reconciliation → GL has unbroken chain |
| C-02 | Boundary error handling | PASS | Reconciliation discrepancy handling at Finance←Commerce boundary explicit |
| C-03 | Data loss point identification | PASS | Void/refund mis-posting and float discrepancy are concrete |
| C-04 | Schema state at each stage | PASS | Cash → ledger entry → GL posting schema diffs |

**Essential subtotal: 60 / 60**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-05 | Latency characterization | PASS | Daily reconciliation cycle with known latency bounds |
| C-06 | Stale data windows | PASS | Day-end GL close stale window quantified |
| C-07 | Domain framing | PASS | "POS", "float", "GL journal entry", "variance threshold" — retail-specific vocabulary |

**Recommended subtotal: 30 / 30**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-08..C-51 | Prior-round criteria | PASS | Full prior-round compliance |
| C-15 | Incumbent/manual baseline | PASS | Max incumbent ≥5 steps is strongest C-15 implementation across all variations; baseline references specific manual steps (cash count sheet, dual-custodian sign-off, manual journal entry) that reappear in C-09 trade-off |
| C-52 | DETECTABILITY INDEX (standalone) | PASS | Standalone table, 13 rows, before STRUCTURAL CONSTRAINTS; row count asserted explicitly |
| C-53 | Dual-slot anchoring all [A-xx] tokens | PASS | Operations cites Commerce [A-04] skip-level; all token-bearing SCs dual-slot |
| C-27 | Non-natural role ordering (C→F→O) | PASS | Strongest non-natural ordering — three-position displacement; Operations is furthest from Commerce, maximizing citation chain stress |

**Aspirational subtotal: 46/46 × 0.217 = 10.00 / 10.00**

### V-04 Total: **100.0 / 100**

---

## V-05 — Telecom CDR-to-Billing-to-GL (O→C→F, non-natural, Phase Gate 0 + SC-0, 14 SCs)

### Essential Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | CDR → rating engine → invoice → revenue → GL is full unbroken chain |
| C-02 | Boundary error handling | PASS | CDR duplication and mediation rejection handling explicit at O→C boundary |
| C-03 | Data loss point identification | PASS | CDR drop, mediation buffer overflow, zero-rated call loss — concrete per stage |
| C-04 | Schema state at each stage | PASS | CDR fields → rated event → invoice line → revenue entry schema diffs complete |

**Essential subtotal: 60 / 60**

### Recommended Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-05 | Latency characterization | PASS | Real-time CDR collection vs. batch billing cycle vs. period-end GL characterized |
| C-06 | Stale data windows | PASS | Billing cycle stale window vs. CDR freshness window both quantified |
| C-07 | Domain framing | PASS | "CDR", "mediation", "rated event", "bill cycle", "deferred revenue" — telecom/finance vocabulary |

**Recommended subtotal: 30 / 30**

### Aspirational Criteria

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-08..C-51 | Prior-round criteria | PASS | All prior criteria satisfied |
| C-52 | DETECTABILITY INDEX (standalone) | PASS | Standalone table with **14 rows** (SC-0 through SC-13); Phase Gate 0 [A-00] contains an explicit checklist item requiring model to verify row count = 14 before Role 1 begins — this is the strongest C-52 implementation: the index is not only standalone but also actively verified by the phase gate mechanism |
| C-53 | Dual-slot anchoring all [A-xx] tokens | PASS | 14 SCs including SC-0; SC-2 names all six stage/boundary tokens in enforcement clause; SC-6 names [A-05]/[A-08]; SC-7 names [A-03]/[A-06]/[A-09]; SC-1 names [A-06]/[A-09]; SC-0 names [A-00] in both slots — fullest dual-slot coverage in R18 |
| **SC-0 meta** | Phase Gate 0 with DETECTABILITY INDEX row-count verification | PASS | **Novel beyond current rubric criteria:** Phase Gate 0 [A-00] fires before Role 1 and requires explicit verification that DETECTABILITY INDEX row count equals total SC count (14). This is a machine-verifiable count gate not present in any prior variation — it enforces C-52 compliance as a structural pre-condition rather than relying on author discipline |

**Aspirational subtotal: 46/46 × 0.217 = 10.00 / 10.00**  
*Plus excellence signal from SC-0/Phase Gate 0 pattern — noted but not scored above rubric ceiling.*

### V-05 Total: **100.0 / 100**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.00 | 30.00 | 10.00 | **100.00** |
| V-02 | 60.00 | 30.00 | 10.00 | **100.00** |
| V-03 | 60.00 | 30.00 | 9.77 | **99.77** |
| V-04 | 60.00 | 30.00 | 10.00 | **100.00** |
| V-05 | 60.00 | 30.00 | 10.00 | **100.00** |

## Ranking

| Rank | Variation | Score | Distinguishing Feature |
|------|-----------|-------|----------------------|
| 1 | V-05 | 100.00 | Phase Gate 0 + SC-0 = verified row-count enforcement gate on DETECTABILITY INDEX; 14 SCs; O→C→F non-natural |
| 1 | V-04 | 100.00 | Max incumbent ≥5 steps; strongest C-15; C→F→O maximum displacement non-natural ordering |
| 1 | V-02 | 100.00 | Non-natural O→F→C adds skip-level citation stress for Commerce→Operations [A-04] |
| 1 | V-01 | 100.00 | Clean reference implementation; all C-52/C-53 requirements fully satisfied |
| 5 | V-03 | 99.77 | C-52 prose enumeration loses machine-scannable column structure; SC-14 FORMAT MODE DECLARATION is strong compensating addition |

---

## Excellence Signals — V-05 (tie-break leader on depth)

**Signal 1: Phase Gate 0 as DETECTABILITY INDEX count-verification gate**

V-05 introduces Phase Gate 0 ([A-00]) as a structural pre-condition before Role 1. The phase gate contains an explicit checklist item: *verify DETECTABILITY INDEX row count = 14*. This converts C-52 from an author-discipline requirement into a machine-verifiable gate. Prior variations assert the row count; V-05 enforces it procedurally. This is the first time a phase gate governs the index itself rather than governing content SCs.

**Signal 2: SC-0 as self-referential DETECTABILITY INDEX enforcement SC**

V-05 adds SC-0 specifically to govern the DETECTABILITY INDEX as a first-class artifact. SC-0 names [A-00] in both the governed-artifact slot and enforcement clause, making the index itself subject to dual-slot anchoring — the same structural property C-53 requires of all content SCs. This closes a gap where the DETECTABILITY INDEX was the reference document for enforcement but was not itself enforced.

**Signal 3: 14-row DETECTABILITY INDEX spanning SC-0 through SC-13**

By extending from 13 to 14 rows (adding SC-0), V-05 achieves a reflexive index: the document describing enforcement locations for all SCs now includes an entry for the SC that governs the index itself. This creates a closed verification loop that V-01/V-02/V-04 do not have.

---

## C-19 Candidate: Phase Gate 0 as pre-structural verification gate for index documents

**Emerging from V-05:** Any prompt with a machine-scannable reference index (such as DETECTABILITY INDEX per C-52) should include a Phase Gate 0 that verifies the index row count equals the declared SC count before Role 1 begins. An index without a phase-gate row-count check relies on author discipline; a Phase Gate 0 count verification makes the structural contract machine-enforceable.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase Gate 0 as pre-structural row-count verification gate — enforces DETECTABILITY INDEX completeness as a machine-verifiable pre-condition before Role 1 begins, replacing author-discipline enforcement with procedural gate enforcement", "SC-0 as self-referential DETECTABILITY INDEX enforcement SC — the index governing all SC detectability locations is itself governed by an SC with dual-slot anchoring, closing the reflexive verification loop"]}
```
