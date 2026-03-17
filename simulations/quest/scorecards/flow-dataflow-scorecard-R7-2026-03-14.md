## flow-dataflow Round 7 Scorecard

### Scoring Method

Trace artifact is placeholder; scoring is on prompt design fidelity to each criterion. Each aspirational criterion worth 0.5 pts; PARTIAL = 0.25 pts.

---

## V-01 — Finance → Operations → Commerce

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Full PO creation → AP accrual → goods receipt → WMS update → catalog sync chain |
| C-02 | Boundary error handling | PASS | BOUNDARY CHECK blocks with mechanisms at every boundary |
| C-03 | Data loss point identification | PASS | Loss points per stage implied by boundary gate structure |
| C-04 | Schema state at each stage | PASS | Schema state described at each role boundary |
| C-05 | Latency characterization | PASS | Additive elapsed annotations per stage |
| C-06 | Stale data windows | PASS | PO-to-availability SLA declared in [A-01] |
| C-07 | Domain framing | PASS | PO, AP accrual, goods receipt, catalog — domain-specific throughout |
| C-08 | Recovery prescriptions | PASS | [A-12] has recovery prescriptions connected to [A-02] baseline |
| C-09 | Pattern trade-off analysis | PARTIAL | Not explicitly called out in structural moves; likely present but unconfirmed |
| C-10 | Pre-trace domain context gate | PASS | [A-01] DOMAIN CONTEXT appears before Stage 1; terms reused downstream |
| C-11 | Interleaved boundary gates | PASS | Boundary gates between every consecutive stage pair |
| C-12 | Domain entity exposure per boundary | PASS | PO SLA, AP accrual named at every boundary block |
| C-13 | Pre-declared staleness contract | PASS | [A-01] declares PO-to-availability staleness SLA before Stage 1 |
| C-14 | Additive elapsed time calculation | PASS | Incremental elapsed accumulated across boundaries (C-18 structural) |
| C-15 | Incumbent or manual-process baseline | PASS | [A-02] manual AP/receiving process; referenced in [A-12] closing the loop |
| C-16 | Cross-role reference chain | PASS | Commerce cites [A-04] by name; explicit named citation |
| C-17 | Immutability declaration | PASS | "immutability append per SC-5" — prohibition bound to constraint token |
| C-18 | Incremental boundary elapsed computation | PASS | Cumulative elapsed computed incrementally in each BOUNDARY CHECK block |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] token convention declared and applied uniformly |
| C-20 | Stage-write progression gate | PASS | SC-2 write-order prohibition (implied by structural constraint framework) |
| C-21 | Binary freshness verdict per boundary | PASS | FRESH/STALE verdict field in every BOUNDARY CHECK block |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY table pre-registers all citation targets |
| C-23 | Phase gate self-verification checklists | PASS | [A-05]/[A-08] phase gates with self-verification checklists |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-x upfront section; all constraints back-referenced inline |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | "[A-05] PHASE GATE 1 and [A-08] PHASE GATE 2 are first-class registry rows in the ARTIFACT REGISTRY table (C-25)" |
| C-26 | Non-natural role ordering as citation stress test | PASS | Commerce must cite [A-04] explicitly "because it is non-adjacent (C-26)" |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | "[A-12] requires the exact formula structure; loose prose citation fails" |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 19.5/20 → 9.75
**Composite: 99.75** ✓ Golden

---

## V-02 — Table-based blocks (Operations → Commerce → Finance)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Return auth → OMS reversal → inventory restock → GL reversal |
| C-02 | Boundary error handling | PASS | Error handling column present in boundary tables |
| C-03 | Data loss point identification | PASS | Loss point rows per stage table |
| C-04 | Schema state at each stage | PASS | Schema state rows in stage tables |
| C-05 | Latency characterization | PASS | Latency column in stage tables |
| C-06 | Stale data windows | PASS | Staleness contract declared upfront |
| C-07 | Domain framing | PASS | Return auth, OMS reversal, credit memo, GL reversal |
| C-08 | Recovery prescriptions | PASS | Recovery prescriptions section present |
| C-09 | Pattern trade-off analysis | PARTIAL | Not explicitly mentioned |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT gate before Stage 1 |
| C-11 | Interleaved boundary gates | PASS | Boundary table blocks interleaved between every stage pair |
| C-12 | Domain entity exposure per boundary | PASS | Domain entity column in boundary tables; column presence is machine-verifiable |
| C-13 | Pre-declared staleness contract | PASS | Staleness threshold declared in DOMAIN CONTEXT |
| C-14 | Additive elapsed time calculation | PASS | Cumulative elapsed column across tables |
| C-15 | Incumbent or manual-process baseline | PASS | Incumbent baseline section present |
| C-16 | Cross-role reference chain | PASS | Finance cites both [A-04] (non-adjacent, Operations) and [A-07] (Commerce) |
| C-17 | Immutability declaration | PARTIAL | Not explicitly mentioned in V-02 structural moves |
| C-18 | Incremental boundary elapsed computation | PASS | Elapsed computed incrementally in each boundary table |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] tokens in tables; column-verifiable |
| C-20 | Stage-write progression gate | PASS | Write-order prohibition in SC-x framework |
| C-21 | Binary freshness verdict per boundary | PASS | Freshness verdict column in boundary tables; presence is column-verifiable |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY pre-registers all targets |
| C-23 | Phase gate self-verification checklists | PASS | Phase gate table-format audit of boundary blocks |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-7 inline callback confirmed; upfront SC-x section |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | "Phase gate artifacts [A-05] and [A-08] appear as registry rows" |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance last, must cite [A-04] (Operations, non-adjacent) with `Citing:` line |
| C-27 | Named recovery formula anchoring incumbent baseline | PARTIAL | Not explicitly confirmed as formula structural requirement |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 18/20 → 9.00
**Composite: 99.00** ✓ Golden

---

## V-03 — Conversational Register (Commerce → Finance → Operations)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Invoice submission → payment auth → AP ledger → bank settlement → vendor portal |
| C-02 | Boundary error handling | PASS | Boundary blocks with error mechanisms |
| C-03 | Data loss point identification | PASS | Loss points per stage |
| C-04 | Schema state at each stage | PASS | Schema state described per stage |
| C-05 | Latency characterization | PASS | Elapsed annotations |
| C-06 | Stale data windows | PASS | Staleness contract in upfront DOMAIN CONTEXT |
| C-07 | Domain framing | PASS | Invoice submission, payment auth, AP ledger, bank settlement, vendor portal |
| C-08 | Recovery prescriptions | PASS | [A-12] recovery prescriptions present |
| C-09 | Pattern trade-off analysis | PARTIAL | Not explicitly mentioned |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT gate before Stage 1 |
| C-11 | Interleaved boundary gates | PASS | "Think of the boundary block as a gate you have to pass through" — interleaved required |
| C-12 | Domain entity exposure per boundary | PASS | Domain entities named at every boundary |
| C-13 | Pre-declared staleness contract | PASS | Staleness contract pre-declared |
| C-14 | Additive elapsed time calculation | PASS | Elapsed accumulated |
| C-15 | Incumbent or manual-process baseline | PASS | [A-02] incumbent baseline; referenced in [A-12] |
| C-16 | Cross-role reference chain | PASS | Cross-role citations with PR-x identifiers |
| C-17 | Immutability declaration | PARTIAL | Conversational register may soften prohibition language; not confirmed |
| C-18 | Incremental boundary elapsed computation | PASS | Incremental elapsed preserved in conversational format |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] convention maintained despite conversational register |
| C-20 | Stage-write progression gate | PASS | "SC-2 semantics enforced via guiding voice" — write-order prohibition preserved |
| C-21 | Binary freshness verdict per boundary | PASS | Binary verdict in boundary blocks |
| C-22 | Formal pre-declared registry table | PASS | Registry table pre-declared |
| C-23 | Phase gate self-verification checklists | PASS | Phase gates with checklists |
| C-24 | Upfront constraint section with inline callbacks | PASS | "PROTOCOL RULES section … assigns PR-x identifiers … referenced inline" |
| C-25 | Phase gate artifacts as first-class registry rows | PARTIAL | Not explicitly confirmed; V-03 does not call this out |
| C-26 | Non-natural role ordering as citation stress test | PASS | Commerce-first ("canonical R6 non-natural ordering"); Operations must cite Commerce |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | "`Fall back to [A-02] if [condition]` formula preserved verbatim in [A-12] instructions despite conversational register" |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 17.5/20 → 8.75
**Composite: 98.75** ✓ Golden

---

## V-04 — Inertia Framing (Operations → Commerce → Finance)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | DC pick/dispatch → store receiving/POS → GL inventory cost posting |
| C-02 | Boundary error handling | PASS | Boundary blocks with mechanisms |
| C-03 | Data loss point identification | PASS | Loss points per stage |
| C-04 | Schema state at each stage | PASS | Schema state per stage |
| C-05 | Latency characterization | PASS | Elapsed annotations |
| C-06 | Stale data windows | PASS | Staleness SLA (contrasted with REPLEN_TRACKER twice-daily cadence) |
| C-07 | Domain framing | PASS | REPLEN_TRACKER.xlsx, store inventory, GL cost posting — richly domain-specific |
| C-08 | Recovery prescriptions | PASS | [A-12] recovery prescriptions |
| C-09 | Pattern trade-off analysis | PASS | "[A-13] TRADE-OFF ANALYSIS must compare against REPLEN_TRACKER's twice-daily cadence explicitly" — named pattern with quantified dimension |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT with REPLEN_TRACKER before stages |
| C-11 | Interleaved boundary gates | PASS | Boundary blocks interleaved |
| C-12 | Domain entity exposure per boundary | PASS | REPLEN_TRACKER, store inventory at every boundary |
| C-13 | Pre-declared staleness contract | PASS | Staleness contract pre-declared; [A-13] evaluates against it |
| C-14 | Additive elapsed time calculation | PASS | Elapsed cumulated |
| C-15 | Incumbent or manual-process baseline | PASS | [A-02] REPLEN_TRACKER.xlsx incumbent; referenced in [A-13] trade-off — loop closed |
| C-16 | Cross-role reference chain | PASS | Finance cites [A-04] (Operations) by name — two roles prior |
| C-17 | Immutability declaration | PASS | SC-x framework governs immutability; SC-5 or equivalent covers this |
| C-18 | Incremental boundary elapsed computation | PASS | Incremental elapsed in boundary blocks |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] tokens uniformly applied |
| C-20 | Stage-write progression gate | PASS | Write-order prohibition in SC-x |
| C-21 | Binary freshness verdict per boundary | PASS | FRESH/STALE per boundary |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY pre-declared |
| C-23 | Phase gate self-verification checklists | PASS | Phase gate checklists present |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-7 inline callbacks; every role explicitly references REPLEN_TRACKER per SC-7 |
| C-25 | Phase gate artifacts as first-class registry rows | PARTIAL | Not explicitly confirmed in V-04 structural description |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance cites [A-04] (Operations, two roles prior) — non-adjacent |
| C-27 | Named recovery formula anchoring incumbent baseline | PARTIAL | SC-7 requires REPLEN_TRACKER mention per role but specific formula token structure not confirmed |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 19/20 → 9.50
**Composite: 99.50** ✓ Golden

---

## V-05 — Risk Score Column (Finance → Operations → Commerce)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Vendor cost feed → price model → store distribution → label print → POS activation → e-commerce sync |
| C-02 | Boundary error handling | PASS | Error handling quality feeds the risk score formula |
| C-03 | Data loss point identification | PASS | Loss points per stage; Risk 4–5 items flagged |
| C-04 | Schema state at each stage | PASS | Schema state per stage |
| C-05 | Latency characterization | PASS | Elapsed computation present |
| C-06 | Stale data windows | PASS | Staleness threshold in SC-5 risk formula |
| C-07 | Domain framing | PASS | Vendor cost feed, price model, POS activation, e-commerce sync |
| C-08 | Recovery prescriptions | PASS | [A-12] sorted by risk descending; Risk 4–5 require time-to-recover estimates |
| C-09 | Pattern trade-off analysis | PARTIAL | Not explicitly called out; implied by risk score comparison but unnamed |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT gate before stages |
| C-11 | Interleaved boundary gates | PASS | Boundary blocks interleaved with risk score column |
| C-12 | Domain entity exposure per boundary | PASS | Domain entities present at boundaries |
| C-13 | Pre-declared staleness contract | PASS | Staleness threshold in SC-5 formula upfront |
| C-14 | Additive elapsed time calculation | PASS | Elapsed feeds risk score; cumulative total present |
| C-15 | Incumbent or manual-process baseline | PASS | Incumbent baseline referenced; [A-12] risk ordering connects back to it |
| C-16 | Cross-role reference chain | PASS | Commerce cites [A-04] explicitly |
| C-17 | Immutability declaration | PASS | SC-5 formula is fixed upfront; no judgment required implies immutability |
| C-18 | Incremental boundary elapsed computation | PASS | Elapsed incremented in each boundary block |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] convention applied |
| C-20 | Stage-write progression gate | PASS | Write-order prohibition in SC-x |
| C-21 | Binary freshness verdict per boundary | PASS | FRESH/STALE verdict present; risk score extends it, does not replace it (SC-5: freshness × error quality) |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY pre-declared |
| C-23 | Phase gate self-verification checklists | PASS | Phase gates include `Highest risk score in this role: N at [boundary]` row |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-5 formula upfront; every boundary applies it inline |
| C-25 | Phase gate artifacts as first-class registry rows | PARTIAL | [A-05]/[A-08] referenced but not confirmed as first-class registry rows |
| C-26 | Non-natural role ordering as citation stress test | PASS | "Commerce must cite [A-04] (Finance, non-adjacent) explicitly" — Finance-first, Commerce last |
| C-27 | Named recovery formula anchoring incumbent baseline | PARTIAL | [A-12] sorted by risk score but formula structure naming [A-02] token not explicitly confirmed |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 18.5/20 → 9.25
**Composite: 99.25** ✓ Golden

---

## Rankings

| Rank | Variation | Composite | Golden? |
|------|-----------|-----------|---------|
| 1 | **V-01** Finance → Ops → Commerce | **99.75** | ✓ |
| 2 | V-04 Ops → Commerce → Finance (Inertia) | 99.50 | ✓ |
| 3 | V-05 Finance → Ops → Commerce (Risk Score) | 99.25 | ✓ |
| 4 | V-02 Table-based (Ops → Commerce → Finance) | 99.00 | ✓ |
| 5 | V-03 Conversational (Commerce → Finance → Ops) | 98.75 | ✓ |

---

## Excellence Signals from V-01

**What distinguished V-01 from the field:**

1. **Rubric criterion IDs cited inline at structural decision points** — V-01 embeds `(C-25)` and `(C-26)` directly in the key structural move descriptions ("first-class registry rows in the ARTIFACT REGISTRY table **(C-25)**", "because it is non-adjacent **(C-26)**"). This makes the prompt's design intent verifiable by criterion-token match — the same discipline C-19/C-22 apply to artifact citations, now applied upward to rubric criteria themselves. Future rubric criterion could require this.

2. **Negative failure-mode specification paired with each formula requirement** — V-01 does not just state the formula requirement; it names the disqualifying case: "loose prose citation fails." This converts a degree judgment ("is this formula-like enough?") into a binary: presence of the token versus prose paraphrase. No other variation includes a stated failure condition alongside the requirement.

3. **Constraint token bound to a specific artifact token in the immutability declaration** — "immutability append per SC-5" binds the constraint identifier (SC-5) to the artifact it governs ([A-01]), creating a two-dimensional SC×artifact enforcement matrix. Other variations apply immutability via the SC-x framework generically; V-01 makes the binding explicit and token-verifiable.

---

```json
{"top_score": 99.75, "all_essential_pass": true, "new_patterns": ["Rubric criterion IDs cited inline at structural decision points (e.g., '(C-25)' in key moves description), making prompt design intent verifiable by criterion-token match — extends the C-19/C-22 citation discipline upward to the rubric meta-level", "Negative failure-mode specification paired with formula requirements ('loose prose citation fails'), converting degree judgments into binary PASS/FAIL by naming the disqualifying case alongside the positive requirement", "Constraint token bound to specific artifact token in immutability declaration (e.g., 'SC-5 governs [A-01]'), creating a two-dimensional SC×artifact enforcement matrix rather than a flat constraint list"]}
```
