Now I have the full picture. Let me produce the R8 scorecard.

---

## flow-dataflow Round 8 Scorecard

### Scoring Method

Trace artifact is placeholder; scoring is on prompt design fidelity to each criterion.
Aspirational: 23 criteria × 10/23 pts each = 10 pts total. PARTIAL = 5/23 pts.

**Note on V-01 / V-02 / V-03**: These are the R7 designs carried into R8 and rescored against C-28..C-30. V-04 and V-05 are the new R8 prompt designs embedded in the scoring prompt.

---

## V-01 — Finance → Operations → Commerce

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | PO creation → AP accrual → GL posting → WMS → catalog availability; unbroken chain |
| C-02 | Boundary error handling | PASS | Every block requires `Error handling:` field; "no handling — see [A-12]" is explicit flag |
| C-03 | Data loss point identification | PASS | Explicit `Loss point:` required per stage block; "errors may occur" disqualified |
| C-04 | Schema state at each stage | PASS | `Schema in:` / `Schema out:` fields required per stage with field-delta note |
| C-05 | Latency characterization | PASS | `Latency: [value, range, or characterization: real-time / near-real / batch / daily]` required per stage body |
| C-06 | Stale data windows | PASS | [A-01] declares staleness SLA; [A-11] stale analysis covers normal-op and failure-mode |
| C-07 | Domain framing | PASS | PO, AP accrual line, supplier receipt voucher, WMS stock-on-hand, catalog availability flag |
| C-08 | Recovery prescriptions | PASS | [A-12] covers every `no handling` flag and loss point with required `Fall back to [A-02]` formula |
| C-09 | Pattern trade-off analysis | PARTIAL | [A-13] exists but prompt doesn't structurally require section as named mandatory output with baseline token |
| C-10 | Pre-trace domain context gate | PASS | [A-01] DOMAIN CONTEXT produced before Stage 1; ≥2 entity terms reappear downstream |
| C-11 | Interleaved boundary gates | PASS | SC-2 prohibits Stage N+1 until preceding block is complete; blocks required inline |
| C-12 | Domain entity exposure per boundary | PASS | `Domain entity at boundary:` required field; "data" / "records" disqualified |
| C-13 | Pre-declared staleness contract | PASS | [A-01] declares threshold before Stage 1 is written; SC-5 locks it |
| C-14 | Additive elapsed time calculation | PASS | SC-3: `Elapsed total (cumulative):` computed as sum of all prior stage + boundary latencies |
| C-15 | Incumbent or manual-process baseline | PASS | [A-02] uses ≥1 entity from [A-01]; referenced by [A-12] (`Fall back to [A-02]`) and [A-13] — loop closed |
| C-16 | Cross-role reference chain | PASS | SC-1 `Citing:` line required; prose back-reference explicitly disqualified |
| C-17 | Immutability declaration | PASS | SC-5 appends verbatim prohibition: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." |
| C-18 | Incremental boundary elapsed computation | PASS | SC-3 requires `Elapsed total (cumulative):` inside each boundary block — not deferred to stale analysis |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` token convention declared in registry header; prose citations disqualified |
| C-20 | Stage-write progression gate | PASS | SC-2: "Write the BOUNDARY CHECK block. Confirm it is complete. Then write Stage N+1." Explicit write-order prohibition |
| C-21 | Binary freshness verdict per boundary | PASS | SC-4: `Freshness verdict: FRESH \| STALE` required in every block; missing verdict fails SC-4 explicitly |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY table with Token, Artifact, Owner, Description before any role output |
| C-23 | Phase gate self-verification checklists | PASS | [A-05]/[A-08] checklists with named SC identifiers; each item must be ✓ before next role begins |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-1..SC-6 declared before roles; every role references them by identifier at point of application |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | [A-05] PHASE GATE 1 and [A-08] PHASE GATE 2 appear as registry rows with token, owner, description |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance-first; Commerce must cite [A-04] (Finance, two roles prior) — SC-1 `Citing:` enforces non-adjacent token |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | [A-12] instructions state required formula structure: "`Fall back to [A-02] if [condition]`" — loose prose citation disqualified |
| C-28 | Named-column boundary block schema | FAIL | Boundary blocks use labeled-line format (`Domain entity at boundary:`, `Error handling:`, etc.), not a named-column table schema. Column existence cannot be verified without rubric knowledge |
| C-29 | Trade-off analysis as prompt-required section with incumbent baseline token citation | FAIL | [A-13] exists and requires [A-02] citation but C-09 PARTIAL confirms it is not structurally mandated as a named section with required token in the role instructions |
| C-30 | Output register declaration with format-specific field-compliance markers | FAIL | Single register (labeled blocks) assumed throughout; no explicit register declaration section; compliance markers are field labels discoverable only by reading prompt prose |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 19.5/23 → 8.48
**Composite: 98.48** ✓ Golden

---

## V-02 — Table-based blocks (Operations → Commerce → Finance)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Return auth → OMS reversal → inventory restock → GL reversal; unbroken chain |
| C-02 | Boundary error handling | PASS | Error handling column present in boundary table schema |
| C-03 | Data loss point identification | PASS | Loss point column per stage table |
| C-04 | Schema state at each stage | PASS | Schema state rows in stage tables |
| C-05 | Latency characterization | PASS | Latency column in stage tables; per-stage annotation explicitly required |
| C-06 | Stale data windows | PASS | Staleness contract declared upfront; failure-mode addressed |
| C-07 | Domain framing | PASS | Return auth, OMS reversal, credit memo, GL reversal |
| C-08 | Recovery prescriptions | PASS | Recovery prescriptions section present and connected to loss flags |
| C-09 | Pattern trade-off analysis | PARTIAL | Trade-off referenced but not structurally required as named section with mandatory token |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT gate before Stage 1; terms reused downstream |
| C-11 | Interleaved boundary gates | PASS | Boundary table blocks interleaved between every stage pair |
| C-12 | Domain entity exposure per boundary | PASS | Domain entity column in boundary tables; column presence is machine-verifiable |
| C-13 | Pre-declared staleness contract | PASS | Staleness threshold declared in DOMAIN CONTEXT before Stage 1 |
| C-14 | Additive elapsed time calculation | PASS | Cumulative elapsed column across boundary tables |
| C-15 | Incumbent or manual-process baseline | PASS | Incumbent baseline section present; referenced in trade-off |
| C-16 | Cross-role reference chain | PASS | Finance cites both [A-04] (Operations, non-adjacent) and [A-07] (Commerce) with explicit tokens |
| C-17 | Immutability declaration | PARTIAL | Threshold lock present but immutability prohibition language not explicitly confirmed as verbatim append |
| C-18 | Incremental boundary elapsed computation | PASS | Elapsed computed incrementally in each boundary table column |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] tokens in tables; applied uniformly |
| C-20 | Stage-write progression gate | PASS | Write-order prohibition in SC-x framework |
| C-21 | Binary freshness verdict per boundary | PASS | Freshness verdict column in boundary tables; column-verifiable |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY pre-registers all targets |
| C-23 | Phase gate self-verification checklists | PASS | Phase gate table-format audit of boundary blocks |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-x section with inline callbacks at every application point |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | Phase gate artifacts appear as registry rows |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance last, must cite [A-04] (Operations, non-adjacent) — inference structurally insufficient |
| C-27 | Named recovery formula anchoring incumbent baseline | PARTIAL | Recovery formula present but specific formula token structure requiring `[A-xx]` not confirmed as explicit requirement |
| C-28 | Named-column boundary block schema | PARTIAL | Boundary blocks are named-column tables (domain entity column, elapsed column, verdict column) making field presence column-verifiable — satisfies the intent. However no explicit "BOUNDARY BLOCK SCHEMA" section formally declaring the required column names is present; schema discovered by reading role instructions rather than a declared section |
| C-29 | Trade-off analysis as prompt-required section with incumbent baseline token citation | FAIL | C-09 PARTIAL in R7 confirms trade-off not structurally required; no named mandatory section declaration |
| C-30 | Output register declaration with format-specific field-compliance markers | PARTIAL | Table format used throughout making compliance markers = column names; no explicit REGISTER DECLARATION section; register must be inferred |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 19.5/23 → 8.48
**Composite: 98.48** ✓ Golden

---

## V-03 — Conversational Register (Commerce → Finance → Operations)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Invoice submission → payment auth → AP ledger → bank settlement → vendor portal |
| C-02 | Boundary error handling | PASS | Boundary blocks include error mechanism prose requirement |
| C-03 | Data loss point identification | PASS | Loss points per stage declared in guiding voice |
| C-04 | Schema state at each stage | PASS | Schema state described per stage |
| C-05 | Latency characterization | PASS | Elapsed annotations per stage preserved in conversational format |
| C-06 | Stale data windows | PASS | Staleness contract pre-declared; failure-mode addressed |
| C-07 | Domain framing | PASS | Invoice submission, payment auth, AP ledger, bank settlement, vendor portal |
| C-08 | Recovery prescriptions | PASS | [A-12] recovery prescriptions present and complete |
| C-09 | Pattern trade-off analysis | PARTIAL | Not structurally required as named section; present but not mandated |
| C-10 | Pre-trace domain context gate | PASS | DOMAIN CONTEXT gate before Stage 1 |
| C-11 | Interleaved boundary gates | PASS | "Think of the boundary block as a gate you must pass through" — interleaved required |
| C-12 | Domain entity exposure per boundary | PASS | Domain entities named at every boundary in conversational narration |
| C-13 | Pre-declared staleness contract | PASS | Staleness contract pre-declared before Stage 1 |
| C-14 | Additive elapsed time calculation | PASS | Elapsed accumulated; `running total` marker preserved in conversational format |
| C-15 | Incumbent or manual-process baseline | PASS | [A-02] incumbent baseline; referenced in [A-12] closing the loop |
| C-16 | Cross-role reference chain | PASS | Cross-role citations with PR-x identifiers; named not prose |
| C-17 | Immutability declaration | PARTIAL | Conversational register may soften verbatim prohibition language; not confirmed as explicit append |
| C-18 | Incremental boundary elapsed computation | PASS | Incremental elapsed preserved in conversational format |
| C-19 | Machine-verifiable citation convention | PASS | [A-xx] convention maintained despite conversational register |
| C-20 | Stage-write progression gate | PASS | SC-2 semantics enforced; write-order prohibition preserved |
| C-21 | Binary freshness verdict per boundary | PASS | Binary verdict required in boundary narrations |
| C-22 | Formal pre-declared registry table | PASS | Registry table pre-declared |
| C-23 | Phase gate self-verification checklists | PASS | Phase gates with checklists; ticking required |
| C-24 | Upfront constraint section with inline callbacks | PASS | PROTOCOL RULES section assigns PR-x identifiers; referenced inline |
| C-25 | Phase gate artifacts as first-class registry rows | PARTIAL | Registry structure present but phase gate artifacts not confirmed as explicit first-class rows with same token/owner/description schema |
| C-26 | Non-natural role ordering as citation stress test | PASS | Commerce-first; Operations must cite Commerce (non-adjacent) — inference insufficient |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | `Fall back to [A-02] if [condition]` formula preserved verbatim in [A-12] instructions despite conversational register |
| C-28 | Named-column boundary block schema | FAIL | Conversational register uses prose narrations for boundary blocks; named-column table schema structurally absent; field presence verifiable only by reading prose |
| C-29 | Trade-off analysis as prompt-required section with incumbent baseline token citation | FAIL | C-09 PARTIAL confirms trade-off not structurally required as named section |
| C-30 | Output register declaration with format-specific field-compliance markers | PARTIAL | Conversational register is used with PR-x compliance markers, but no explicit REGISTER DECLARATION section mapping each required field (elapsed, verdict, entity, error handling) to its register-specific compliance marker; evaluator must infer the mapping from role instructions |

**Essential**: 4/4 → 60.00
**Recommended**: 3/3 → 30.00
**Aspirational**: 19.0/23 → 8.26
**Composite: 98.26** ✓ Golden

---

## V-04 — Inertia Framing: Finance → Operations → Commerce, Seven-Column Schema with SC-9 (Incumbent Equiv.)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Revenue Journal Entry → Inventory Position → Catalog Snapshot; each role has four stages with unbroken chain |
| C-02 | Boundary error handling | PASS | `Error Handling` is a named required column in the seven-column boundary block schema |
| C-03 | Data loss point identification | PASS | `Data Loss Flag` column required: `YES — [named loss point]` or `NO`; generic flags disqualified |
| C-04 | Schema state at each stage | PASS | `Schema Delta` column required: named field changes at boundary or `NONE` |
| C-05 | Latency characterization | PARTIAL | `Elapsed (cumul.)` column is incremental sum of stage + boundary durations implying per-stage durations, but no explicit stage-body latency annotation field is required in the LINEAGE TRACE instructions; stage bodies are open-ended headers with no mandatory latency field |
| C-06 | Stale data windows | PASS | [A-02] STALE SLA CONTRACT pre-declared; Verdict column FRESH/STALE at every boundary derived from [A-02] |
| C-07 | Domain framing | PASS | Revenue Journal Entry, GL system, Inventory Position, WMS, Catalog Snapshot, Storefront Cache — richly domain-specific |
| C-08 | Recovery prescriptions | PASS | [A-14] RECOVERY PRESCRIPTIONS covers every `NONE — see [A-14]` and every YES Data Loss Flag; specific recovery required |
| C-09 | Pattern trade-off analysis | PASS | SC-8 requires [A-15] as structurally required section: ≥1 alternative, ≥2 dimensions, cites [A-02] and [A-03] by token |
| C-10 | Pre-trace domain context gate | PASS | [A-01] DOMAIN CONTEXT required before Stage 1; ≥2 terms reappear in subsequent lineage per role instructions |
| C-11 | Interleaved boundary gates | PASS | SC-2: boundary block between every stage pair; Stage N+1 blocked until block complete |
| C-12 | Domain entity exposure per boundary | PASS | `Entity` is the first named column; "data" or "records" alone would fail by omission of entity column content |
| C-13 | Pre-declared staleness contract | PASS | [A-02] declared before Stage 1; SC-3: "This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1." |
| C-14 | Additive elapsed time calculation | PASS | SC-4: `Elapsed (cumul.) = sum of all prior stage and boundary durations, computed incrementally as a named column field` |
| C-15 | Incumbent or manual-process baseline | PASS | [A-03] INCUMBENT BASELINE with per-step manual durations; cited by token in [A-14] and [A-15] — loop closed |
| C-16 | Cross-role reference chain | PASS | SC-6 citation-opening rule: every role after Role 1 opens with `Citing:` naming specific [A-xx] tokens including ≥1 from non-adjacent role |
| C-17 | Immutability declaration | PASS | SC-3 verbatim: "This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1." Explicit post-Stage-1 prohibition |
| C-18 | Incremental boundary elapsed computation | PASS | SC-4 requires cumulative elapsed as named column field inside every boundary block; not deferred to summary |
| C-19 | Machine-verifiable citation convention | PASS | SC-1: every handoff target uses `[A-xx]` token; applied uniformly by constraint |
| C-20 | Stage-write progression gate | PASS | SC-2: "Do not write Stage N+1 until this block is complete." — explicit write-order prohibition naming gate condition |
| C-21 | Binary freshness verdict per boundary | PASS | SC-5: `Verdict` column contains `FRESH` or `STALE` derived from comparison against [A-02]; no other values permitted |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY with Token, Artifact, Owner, Description — all 16 artifacts pre-registered before roles begin |
| C-23 | Phase gate self-verification checklists | PASS | [A-06], [A-10], [A-16] — checklist items reference named fields; next role blocked until all items ticked |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-1..SC-9 declared before roles; every role instruction references constraints by identifier: `[Apply SC-2]`, `[SC-7]`, `[SC-3 activates]`, `[Apply SC-8]` |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | [A-06] PHASE GATE CHECK — Role 1, [A-10] PHASE GATE CHECK — Role 2, [A-16] PHASE GATE CHECK — Role 3 appear as rows in ARTIFACT REGISTRY with token, owner, description |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance → Operations → Commerce (natural = Commerce → Operations → Finance); Operations must cite [A-02]/[A-03] from Finance (non-adjacent); Commerce must cite both non-adjacent predecessors |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | [A-14] instructions specify required formula structure: `"Fall back to [A-03] if [condition]"` by token — structural requirement, not example |
| C-28 | Named-column boundary block schema | PASS | BOUNDARY BLOCK SCHEMA section explicitly declares seven named columns (Entity, Elapsed (cumul.), Verdict, Error Handling, Schema Delta, Data Loss Flag, Incumbent Equiv.) with required content per column; field completeness verifiable by column existence alone |
| C-29 | Trade-off analysis as prompt-required section with incumbent baseline token citation | PASS | SC-8: "Required TRADE-OFF ANALYSIS: [A-15] is a required named section. ≥1 alternative, ≥2 dimensions, cites [A-02] and [A-03] by token. Apply SC-8 when producing [A-15]." — structurally mandated with token requirement |
| C-30 | Output register declaration with format-specific field-compliance markers | PARTIAL | All three roles use table register; BOUNDARY BLOCK SCHEMA declares named columns (satisfying per-field compliance markers for tabular format); but no explicit REGISTER DECLARATION section is present. Register is implied by schema, not formally declared. C-30 requires explicit declaration of the output register alongside per-field markers |

**Essential**: 4/4 → 60.00
**Recommended**: 2.5/3 → 25.00
**Aspirational**: 22.5/23 → 9.78
**Composite: 94.78** ✓ Golden

---

## V-05 — Finance → Commerce → Operations, Six-Column Schema, Dual-Register Declaration, Required Trade-Off

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Data lineage chain | PASS | Revenue Journal Entry (Finance) → Catalog Snapshot (Commerce) → Inventory Position (Operations); each role traces four stages |
| C-02 | Boundary error handling | PASS | Table-register roles: `Error Handling` column in boundary schema. Conversational role (Commerce): SC-7 requires boundary narration to cover error handling per REGISTER DECLARATION compliance markers |
| C-03 | Data loss point identification | PASS | Table roles: `Data Loss Flag` column. Conversational: boundary narrations must name loss points per declared compliance markers |
| C-04 | Schema state at each stage | PASS | Table roles: `Schema Delta` column. Conversational: schema changes described in narration per compliance markers |
| C-05 | Latency characterization | PARTIAL | Same structural gap as V-04: `Elapsed (cumul.)` column (table) or `running total: X` (conversational) tracks cumulative but per-stage latency annotation is not a required stage-body field; stage bodies are open-ended headers |
| C-06 | Stale data windows | PASS | [A-02] STALE SLA CONTRACT pre-declared by Finance; SC-3 locks it; SC-5 maps verdict to register-specific compliance marker for both registers |
| C-07 | Domain framing | PASS | Revenue Journal Entry, GL system, Catalog Snapshot, Pricing Engine, Inventory Position, WMS |
| C-08 | Recovery prescriptions | PASS | [A-14] RECOVERY PRESCRIPTIONS in Operations role; `Fall back to [A-03] if [condition]` formula required by token |
| C-09 | Pattern trade-off analysis | PASS | SC-8 requires [A-15] as structurally required section: ≥1 alternative, ≥2 dimensions, cites [A-02] and [A-03] by token |
| C-10 | Pre-trace domain context gate | PASS | [A-01] DOMAIN CONTEXT required before Stage 1 with entity vocabulary and reuse requirement |
| C-11 | Interleaved boundary gates | PASS | SC-2: boundary block/narration between every stage pair; Stage N+1 blocked until boundary complete per declared register |
| C-12 | Domain entity exposure per boundary | PASS | Table roles: `Entity` column. Conversational role: entity named in boundary narration per compliance markers |
| C-13 | Pre-declared staleness contract | PASS | [A-02] declared before Stage 1 with explicit lock; SC-3 immutability |
| C-14 | Additive elapsed time calculation | PASS | SC-4: cumulative elapsed as named column (table) or `running total: X` (conversational) at every boundary — format-specific but structurally required in both |
| C-15 | Incumbent or manual-process baseline | PASS | [A-03] INCUMBENT BASELINE; cited by [A-14] (`Fall back to [A-03]`) and [A-15] — loop closed |
| C-16 | Cross-role reference chain | PASS | SC-6 `Citing:` required for every role after Role 1; tokens from non-adjacent roles required |
| C-17 | Immutability declaration | PASS | SC-3: "This threshold is fixed. You may not revise [A-02] after Stage 1 of Role 1." Explicit prohibition |
| C-18 | Incremental boundary elapsed computation | PASS | SC-4: incremental cumulative at every boundary in both registers; format-specific form declared by SC-4 |
| C-19 | Machine-verifiable citation convention | PASS | SC-1: `[A-xx]` tokens uniformly applied; SC-7 register compliance does not override citation convention |
| C-20 | Stage-write progression gate | PASS | SC-2: "Do not write Stage N+1 until this boundary is complete" — write-order prohibition applied to both table and conversational registers |
| C-21 | Binary freshness verdict per boundary | PASS | SC-5: `FRESH`/`STALE` in Verdict column (table) or declared verdict phrase (conversational); register-specific form declared in REGISTER DECLARATION |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY with Token, Artifact, Owner, Description; all 16 artifacts pre-registered |
| C-23 | Phase gate self-verification checklists | PASS | [A-06], [A-10], [A-16] checklists with named fields; next role blocked |
| C-24 | Upfront constraint section with inline callbacks | PASS | SC-1..SC-8 declared before roles; every role references constraints by identifier at application point |
| C-25 | Phase gate artifacts as first-class registry rows | PASS | [A-06], [A-10], [A-16] appear in ARTIFACT REGISTRY as rows with token, owner, description |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance → Commerce → Operations is maximally non-natural (natural = Commerce → Operations → Finance); Operations (Role 3) must cite Finance (Role 1, two positions back) — inference structurally insufficient |
| C-27 | Named recovery formula anchoring incumbent baseline | PASS | [A-14] requires `Fall back to [A-03] if [condition]` by token as structural requirement in role instructions |
| C-28 | Named-column boundary block schema | PARTIAL | Finance/Operations (table register): six named columns satisfy C-28 for those roles. Commerce (conversational register): boundary narrations structurally cannot have named table columns; SC-7 and REGISTER DECLARATION provide compliance markers (required sentence openers, verdict phrases) but these are not named table columns. C-28 requires "named table columns for every structurally required field" — the conversational role fails the letter of this criterion |
| C-29 | Trade-off analysis as prompt-required section with incumbent baseline token citation | PASS | SC-8 mandates [A-15] as required section with [A-02] and [A-03] token citations — structurally required, same as V-04 |
| C-30 | Output register declaration with format-specific field-compliance markers | PASS | REGISTER DECLARATION section explicitly declares Finance = table register, Commerce = conversational register. SC-4 maps cumulative elapsed to `column value` (table) and `running total: X` (conversational). SC-5 maps freshness verdict to `Verdict column FRESH/STALE` (table) and `one of the two verdict phrases from the REGISTER DECLARATION` (conversational). SC-7 enforces register compliance per role. Per-field compliance markers declared for each register — C-30 fully satisfied |

**Essential**: 4/4 → 60.00
**Recommended**: 2.5/3 → 25.00
**Aspirational**: 22.5/23 → 9.78
**Composite: 94.78** ✓ Golden

---

## Rankings

| Rank | Variation | Composite | Golden? | Key gap |
|------|-----------|-----------|---------|---------|
| 1 | **V-01** Finance → Ops → Commerce | **98.48** | ✓ | C-09 PARTIAL, C-28/29/30 FAIL |
| 1 | **V-02** Table-based (Ops → Commerce → Finance) | **98.48** | ✓ | C-09/C-17/C-27/C-28/C-30 PARTIAL, C-29 FAIL |
| 3 | V-03 Conversational (Commerce → Finance → Ops) | 98.26 | ✓ | C-09/C-17/C-25/C-30 PARTIAL, C-28/29 FAIL |
| 4 | V-04 Inertia Framing 7-column (Finance → Ops → Commerce) | 94.78 | ✓ | C-05 PARTIAL, C-30 PARTIAL |
| 4 | V-05 Dual-Register 6-column (Finance → Commerce → Ops) | 94.78 | ✓ | C-05 PARTIAL, C-28 PARTIAL |

---

## Critical Finding: R8 Innovation Regression on C-05

V-04 and V-05 — the R8 innovations — score **3.70 pts lower** than the R7 carry-forwards (V-01/V-02) despite excelling on C-28/C-29/C-29/C-30. Root cause: the R8 designs moved structural requirements *into* boundary block columns (BOUNDARY BLOCK SCHEMA) but removed the explicit per-stage body requirements (Schema in/out, Latency, Loss point) that V-01 carried as stage-body fields. The recommended-tier C-05 (10 pts weight) penalizes this more than the aspirational tier gains (each new criterion ≈ 0.43 pts).

---

## Excellence Signals from V-04 and V-05

**V-04** — Incumbent Equiv. column makes [A-03] structurally present at every boundary gate:

1. **Seven-column schema extends structural audit coverage to the incumbent competitor** — The `Incumbent Equiv.` column places `[A-03]: manual step duration` beside the pipeline's cumulative elapsed at every boundary. SC-9 requires every cell to derive from [A-03] by token, making the manual-process comparison verifiable by column presence at every gate, not just at closing trade-off analysis. The status-quo competitor is embedded in the audit trail, not deferred.

2. **SC×Artifact cross-reference binds column-level requirement to a specific artifact token** — SC-9: "every `Incumbent Equiv.` cell derives its value from [A-03]. A cell that estimates an incumbent duration without citing [A-03] is a protocol violation." This creates a column-specific SC×artifact enforcement matrix: the SC identifier governs a named column, and the artifact token is the required source. Other variations bind SC identifiers to behavioral requirements; V-04 binds them to a specific column's content source.

**V-05** — Dual-register declaration makes structural verification format-independent:

3. **REGISTER DECLARATION maps every required field to its register-specific compliance marker** — SC-4 maps elapsed to `column value` (table) or `running total: X` (conversational); SC-5 maps verdict to `Verdict column` (table) or `declared verdict phrase` (conversational). An evaluator can verify compliance in either register by scanning for the declared marker — no rubric access needed, no prose judgment required. Format-independence is achieved not by eliminating the conversational register but by pre-declaring what compliance looks like in each register.

4. **Finance → Commerce → Operations maximizes non-adjacent citation distance** — Operations (last role) must cite Finance artifacts [A-02] and [A-03] across two role positions. Commerce (middle role) must cite Finance (non-adjacent predecessor). No pair of roles can satisfy SC-6 via the immediately-preceding role alone — citation laziness is detectable as a missing token across all three roles, not just one.

---

## New Patterns for R9 (not yet captured in C-01..C-30)

1. **Per-stage latency as a required stage-body field** — R8 V-04/V-05 track cumulative elapsed in boundary blocks (SC-4) but do not require an explicit latency annotation in each stage body. Excellence: the prompt should require a named `Stage latency:` field (or column equivalent) in every stage body, making each stage's duration independently verifiable at the stage level and not only inferable from the cumulative boundary total. This would close the C-05 gap opened by the R8 innovations.

2. **Incumbent Equiv. column total as a named closing-analysis artifact** — V-04 places `Incumbent Equiv.` at every boundary (SC-9) but does not require summing those cells into a named `Incumbent Total` artifact. Excellence: the prompt should mandate `INCUMBENT TOTAL: sum of all Incumbent Equiv. cells across all roles` as a required artifact produced before [A-15], giving the TRADE-OFF ANALYSIS table a numeric pipeline-vs-incumbent comparison endpoint rather than per-boundary comparisons only. This would make the C-15 loop closure quantitatively auditable.

3. **Formal register translation table as schema inheritance declaration** — V-05 maps fields to compliance markers inline in SC-4/SC-5 but not as a structured table. Excellence: a named REGISTER TRANSLATION TABLE — mapping every required boundary field (Entity, Elapsed, Verdict, Error Handling, Schema Delta, Data Loss Flag) to its compliance marker in each declared register — would make format-switching auditable by table lookup: an evaluator could verify any field in any register by consulting one table, rather than cross-referencing multiple SC identifiers.

---

```json
{"top_score": 98.48, "all_essential_pass": true, "new_patterns": ["Per-stage latency as required stage-body field: R8 innovations moved structural requirements into boundary block columns but removed explicit per-stage latency annotation fields; excellence requires a named Stage latency: field in every stage body so C-05 is verifiable at the stage level independent of the cumulative boundary total", "Incumbent Equiv. column total as named closing-analysis artifact: V-04 requires Incumbent Equiv. at every boundary via SC-9 but does not mandate summing those cells into an INCUMBENT TOTAL artifact; excellence requires the prompt to produce this sum before TRADE-OFF ANALYSIS as a numeric pipeline-vs-incumbent endpoint, making the [A-03] comparison quantitatively auditable rather than per-boundary only", "Formal register translation table as schema inheritance declaration: V-05 maps fields to compliance markers inline in SC-4/SC-5 but not as a structured table; excellence requires a named REGISTER TRANSLATION TABLE mapping every required boundary field to its compliance marker in each declared register, making format-switching auditable by table lookup rather than multi-SC cross-reference"]}
```
