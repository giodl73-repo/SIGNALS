Now I have everything I need. Let me score all five R15 variations.

---

# flow-dataflow — Round 15 Scorecard

## Scoring Summary

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-01 Role sequence (freight billing) | 4/4 | 3/3 | 40/40 | **100** | YES |
| 1 | V-02 Output format (energy trade, prose) | 4/4 | 3/3 | 40/40 | **100** | YES |
| 1 | V-03 Lifecycle emphasis (SaaS, 9 blocks) | 4/4 | 3/3 | 40/40 | **100** | YES |
| 1 | V-04 Role seq + inertia (pharma) | 4/4 | 3/3 | 40/40 | **100** | YES |
| 1 | V-05 Format + imperative voice (federal) | 4/4 | 3/3 | 40/40 | **100** | YES |

---

## V-01: Role Sequence — Freight Billing / Tabular

Finance → Operations → Commerce. SC-13 as fourth closed-chain navigation path.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | PASS | ARTIFACT REGISTRY defines complete chain: carrier invoice receipt → invoice validation → freight audit → cost allocation → GL journal → ledger posting → management reporting feed; unbroken token-chain across all 14 artifacts |
| C-02 | Boundary error handling | PASS | REGISTER DECLARATION Part A requires `Error Handling` column: "Named retry/dead-letter/rollback, or exactly `no handling — see [A-12]`"; silence is explicitly disqualifying |
| C-03 | Data loss point identification | PASS | `Data Loss Flag` column required: `YES — [loss point name]` or `NO`; generic language disqualifying by Part A; stage tables carry same column per SC-7 |
| C-04 | Schema state at each stage | PASS | SC-7 requires `Schema In \| Schema Out` per stage table; `Schema Delta` column required per Part A in every boundary block |
| C-05 | Latency characterization | PASS | SC-7 requires `Stage Latency` with explicit value/range/characterization; SC-3 requires incremental `Elapsed (cumul.)` at every boundary block |
| C-06 | Stale data windows | PASS | [A-11] STALE ANALYSIS requires separate rows for normal-operation and failure-mode elapsed vs [A-02] threshold; SC-13 requires [A-02] threshold declared pre-Stage-1 |
| C-07 | Domain framing | PASS | [A-02] requires entity vocabulary (carrier invoice, freight audit result, cost allocation entry, etc.); Part A requires named entity per boundary block; generic "data" or "records" disqualifying |
| C-08 | Recovery prescriptions | PASS | [A-12] requires specific named recovery per every `no handling — see [A-12]` annotation and `Data Loss Flag: YES`; formula `Fall back to [A-01] if [condition]` required |
| C-09 | Pattern trade-off analysis | PASS | [A-14] requires ≥1 alternative pattern and ≥2 trade-off dimensions; SC-8 enforces this with inline callback on [A-14] instruction |
| C-10 | Pre-trace domain context gate | PASS | [A-02] precedes [A-03] per SC-11/token ordering; entity vocabulary, SLA, downstream consumer, and business cadence declared; SC-5 immutability statement locks threshold before Stage 1 |
| C-11 | Interleaved boundary gates | PASS | SC-2 "[Apply SC-2 before every stage advance]" requires boundary block fully populated before next stage; not post-hoc |
| C-12 | Domain entity exposure per boundary | PASS | `Entity` column required per Part A: "Named entity from [A-02] vocabulary"; `data` or `records` alone explicitly disqualifying |
| C-13 | Pre-declared staleness contract | PASS | [A-02] SLA declared as integer with unit before Stage 1; SC-5 immutability verbatim required; [A-11] derives verdicts by evaluating elapsed against this threshold |
| C-14 | Additive elapsed time calculation | PASS | SC-3 requires `Elapsed (cumul.)` as "sum of all prior stage latencies and all prior boundary latencies" inside every block; [A-11] uses final value from [A-10] |
| C-15 | Incumbent baseline | PASS | [A-01] required first per SC-11; vocabulary reused in [A-02]; SC-13 requires [A-01] in [A-12] (C-08) and [A-14] (C-09), closing the comparison loop |
| C-16 | Cross-role reference chain | PASS | SC-1 requires named token citations (`[A-01], [A-02], [A-04]` for Operations; `[A-01], [A-02], [A-04], [A-07]` for Commerce); SC-3/SC-4/SC-9 callbacks use `[A-02]` and `[A-01]` tokens throughout |
| C-17 | Immutability declaration | PASS | SC-5 requires verbatim: "This threshold is fixed. No subsequent role may revise it after Stage 1 is written." — explicit prohibition on post-trace revision |
| C-18 | Incremental boundary elapsed | PASS | SC-3 "[Apply SC-3 at every boundary block]" computes inside each block, not deferred to [A-11] |
| C-19 | Machine-verifiable citation convention | PASS | ARTIFACT REGISTRY declares `[A-xx]` convention; "Every citation anywhere in this output must use the `[A-xx]` token exactly as spelled in this table"; applied to all 14 artifacts |
| C-20 | Stage-write progression gate | PASS | SC-2 "Stage N+1 may not be written until the preceding BOUNDARY CHECK table is fully populated per BOUNDARY BLOCK SCHEMA" with inline callback at every stage advance |
| C-21 | Binary freshness verdict per boundary | PASS | SC-4 "[Apply SC-4 at every boundary block]" — exactly `FRESH` or `STALE`; derived from [A-02] threshold comparison |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY markdown table pre-declared before any role output; 14-row coverage |
| C-23 | Phase gate self-verification checklists | PASS | [A-05] (9 items) and [A-08] (7 items) per SC-6; each item ticked ✓ or ✗; next role gated |
| C-24 | Upfront constraint section with inline callbacks | PASS | STRUCTURAL CONSTRAINTS section with `[Apply SCx at every ...]` inline callbacks on SC-2, SC-3, SC-4, SC-6, SC-7, SC-8, SC-9, SC-10 |
| C-25 | Phase gate artifacts as registry rows | PASS | [A-05] and [A-08] appear as named rows in ARTIFACT REGISTRY with owner and description |
| C-26 | Non-natural role ordering as citation stress test | PASS | Finance → Operations → Commerce forces Commerce to skip over Operations and cite Finance's [A-04]; non-default order creates the skip-level test |
| C-27 | Named recovery formula anchoring baseline | PASS | [A-12] requires formula `Fall back to [A-01] if [specific named failure condition]`; [A-01] anchors every prescription |
| C-28 | Named-column boundary block schema | PASS | BOUNDARY BLOCK SCHEMA standalone section declares 7-column order matching Part A spellings exactly; "A column absent, renamed, or not matching Part A header strings fails the schema" |
| C-29 | Trade-off as prompt-required section with baseline citation | PASS | SC-8 + [A-14] instruction: all three tokens [A-01], [A-02], [A-13] required; SC-13 inline callback on [A-14] enforces [A-01] |
| C-30 | Output register declaration with field-compliance markers | PASS | REGISTER DECLARATION Parts A and B — row-per-field compliance marker table covering all 8 required fields |
| C-31 | Pre-declared boundary block schema section | PASS | BOUNDARY BLOCK SCHEMA is a standalone named section declared before any role output |
| C-32 | Register-specific compliance marker mapping | PASS | REGISTER DECLARATION Part A maps each required field to `Column Header`, `Required Cell Form`, and `Disqualifying Form` |
| C-33 | Register-invariant declaration (non-tabular) | N/A (tabular) | Tabular register; criterion does not apply |
| C-34 | Incumbent Equiv. column with token-cited baseline | PASS | REGISTER DECLARATION Part A is "sole authoritative reference" for C-34; required form `[A-01]: [named manual step + duration]`; SC-9 "[Apply SC-9 at every boundary block]" |
| C-35 | INCUMBENT TOTAL before trade-off | PASS | REGISTER DECLARATION Part B is "sole authoritative reference" for C-35; SC-10 requires [A-13] immediately before [A-14] with role breakdown table and Grand Total row |
| C-36 | Baseline-first artifact ordering | PASS | SC-11 "No boundary block and no stage trace may appear before [A-01] is fully produced"; [A-01] leads ARTIFACT REGISTRY |
| C-37 | REGISTER DECLARATION Parts A/B as single-location authority | PASS | "This section is the sole authoritative reference for C-34 (`Incumbent Equiv.` cell form) and C-35 (INCUMBENT TOTAL section format)" |
| C-38 | Skip-level citation requirement in non-natural ordering | PASS | SC-12 requires Commerce's `Citing:` to include [A-04] — Finance's output two positions prior; pre-declared in Commerce role header |
| C-39 | Skip-level SC names governed role | PASS | SC-12 "Commerce's `Citing:` line must include `[A-04]`" — governed role (Commerce) named in body |
| C-40 | Skip-level SC declares position distance | PASS | SC-12 "The position distance is two: Commerce occupies position 3, Finance occupies position 1" |
| C-41 | Phase Gate 2 item cites SC-12 by number | PASS | [A-08] item: "[ ] [SC-12]: Commerce's `Citing:` line must include `[A-04]`..." — `[SC-12]` cited by numbered identifier in item text |
| C-42 | C-37+C-41 closed verification chain co-occurrence | PASS | Both present: REGISTER DECLARATION as single-location authority (C-37) and Phase Gate 2 [SC-12] item (C-41) |
| C-43 | All three skip-level SC attributes in single SC block | PASS | SC-12 contains: governed role (Commerce), position distance (two: pos 3 → pos 1), Phase Gate 2 citation instruction — all three in one block |
| C-44 | Baseline-closure SC enforcing C-15's C-08/C-09 connection | PASS | SC-13 explicitly requires [A-01] in [A-12] (recovery, C-08) and [A-14] (trade-off, C-09) with inline callbacks at both section headers |
| C-45 | Format-mode declaration with criterion substitution map (non-tabular) | N/A (tabular) | Tabular register; criterion does not apply |
| C-46 | SC-13 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-13 BASELINE CLOSURE is the governing authority for every baseline-closure failure in [A-12] and [A-14]**; its inline callbacks at both section headers enforce the [A-01] citation obligation by token match without output-prose inspection." Governing authority named; [A-12] and [A-14] both named |
| C-47 | SC-14 as named navigation entry in closed-chain paragraph (non-tabular) | N/A (tabular) | Tabular register; criterion does not apply |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 40/40 (including N/A as satisfied)

```
composite = (4/4 × 60) + (3/3 × 30) + (40/40 × 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

## V-02: Output Format — Energy Trade Settlement / Prose

Finance → Commerce → Operations. SC-13 + SC-14 both in closed-chain paragraph.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | PASS | Pipeline flows trade order entry → position validation → credit limit check → trade confirmation → settlement instruction → nostro funding → counterparty payment; ARTIFACT REGISTRY spans 14 tokens |
| C-02 | Boundary error handling | PASS | Part A requires `**Error handling:**` bold label; "named mechanism" or "no handling — see [A-12]"; silence disqualifying |
| C-03 | Data loss point identification | PASS | `**Data loss:**` bold label required in every boundary paragraph; `YES — [loss point]` form required; generic language disqualifying |
| C-04 | Schema state at each stage | PASS | SC-7 prose form requires `**Schema in:**` and `**Schema out:**` bold labels; `**Schema:**` label required in boundary paragraphs per Part A |
| C-05 | Latency characterization | PASS | `**Stage latency:**` bold label required per SC-7; `**Elapsed:**` cumulative label required per Part A in every boundary paragraph |
| C-06 | Stale data windows | PASS | [A-11] labeled-sentence format with normal and failure-mode scenarios; [A-02] threshold governs verdict |
| C-07 | Domain framing | PASS | [A-02] vocabulary: trade order, credit limit check result, settlement instruction, nostro funding record, etc.; entity paragraph opener `**[entity]**:` required per Part A |
| C-08 | Recovery prescriptions | PASS | [A-12] formula `Fall back to [A-01] if [condition]` required; SC-13 inline callback at [A-12] header |
| C-09 | Pattern trade-off analysis | PASS | [A-14] requires ≥1 alternative pattern, ≥2 dimensions, all three token citations |
| C-10 | Pre-trace domain context gate | PASS | [A-02] before stage traces; settlement SLA, entity vocabulary, business cadence (same-day settlement cutoff 15:30 ET) |
| C-11 | Interleaved boundary gates | PASS | SC-2 prose form: boundary paragraph with all seven labels required before next stage; "[Apply SC-2 before every stage advance]" |
| C-12 | Domain entity exposure per boundary | PASS | Part A: paragraph opens with bold entity from [A-02] vocabulary; generic "data" or "records" without named entity is disqualifying |
| C-13 | Pre-declared staleness contract | PASS | [A-02] settlement SLA declared with SC-5 immutability; [A-11] verdicts derived against this threshold |
| C-14 | Additive elapsed time calculation | PASS | SC-3 requires `**Elapsed:**` as cumulative sum inside each paragraph; [A-11] uses final value from [A-10] |
| C-15 | Incumbent baseline | PASS | [A-01] first per SC-11; entity names reuse; SC-13 closes comparison loop to [A-12] and [A-14] |
| C-16 | Cross-role reference chain | PASS | Commerce cites [A-01], [A-02], [A-04]; Operations cites [A-01], [A-02], [A-04], [A-07] — named token citations throughout |
| C-17 | Immutability declaration | PASS | SC-5 verbatim immutability required |
| C-18 | Incremental boundary elapsed | PASS | SC-3 inside each boundary paragraph; SC-3 for Commerce extends [A-04] final value; for Operations extends [A-07] final value |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` convention; ARTIFACT REGISTRY declares all valid targets |
| C-20 | Stage-write progression gate | PASS | SC-2 "[Apply SC-2 before every stage advance]" with all-seven-labels confirmation |
| C-21 | Binary freshness verdict | PASS | SC-4 `**Verdict:** FRESH` or `STALE` with [A-02] token citation; "[Apply SC-4 at every boundary paragraph]" |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY 14-row table |
| C-23 | Phase gate checklists | PASS | [A-05] (9 items) and [A-08] (7 items) with ✓/✗; SC-6 gates next role |
| C-24 | Upfront constraint section | PASS | STRUCTURAL CONSTRAINTS with inline callbacks |
| C-25 | Phase gate artifacts as registry rows | PASS | [A-05] and [A-08] in ARTIFACT REGISTRY |
| C-26 | Non-natural ordering as citation stress test | PASS | Finance → Commerce → Operations; Operations skips Commerce to cite Finance's [A-04] |
| C-27 | Named recovery formula | PASS | `Fall back to [A-01] if [condition]` in [A-12] |
| C-28 | Named-label boundary schema | PASS | BOUNDARY BLOCK SCHEMA declares bold-label order matching Part A compliance markers; SC-14 criterion substitution map maps C-28 to "named bold labels by token match" |
| C-29 | Trade-off as prompt-required section | PASS | SC-8 + [A-14] instruction + SC-13 inline callback |
| C-30 | Output register declaration | PASS | REGISTER DECLARATION Parts A/B with field-compliance marker table; SC-14 maps C-30 to "bold-label presence per Part A" |
| C-31 | Pre-declared boundary block schema | PASS | BOUNDARY BLOCK SCHEMA standalone section with field-order declaration |
| C-32 | Register-specific compliance marker mapping | PASS | Part A maps each field to `Compliance Marker` + `Required Sentence Form` + `Disqualifying Form`; SC-14 maps C-32 to per-field bold-label token |
| C-33 | Register-invariant declaration | PASS | REGISTER INVARIANTS section explicitly lists all 7 required labels; "A boundary paragraph missing any declared label fails completeness, regardless of whether the information appears in surrounding prose" |
| C-34 | Incumbent equiv. sentence with token | PASS | Part A: `**Incumbent equiv.:** [A-01]: [named manual step + duration]`; SC-9 inline callback |
| C-35 | INCUMBENT TOTAL before trade-off | PASS | Part B: bold-line-per-role format with Grand Total; SC-10 gates [A-14] |
| C-36 | Baseline-first artifact ordering | PASS | SC-11 baseline-first; [A-01] before any stage or boundary content |
| C-37 | REGISTER DECLARATION as single-location authority | PASS | "This section is the sole authoritative reference for C-34 (`Incumbent equiv.` sentence form) and C-35 (INCUMBENT TOTAL paragraph form)" |
| C-38 | Skip-level citation requirement | PASS | SC-12 requires Operations' `Citing:` to include [A-04]; position distance two |
| C-39 | Skip-level SC names governed role | PASS | SC-12 "Operations' `Citing:` line must include `[A-04]`" — Operations named |
| C-40 | Skip-level SC declares position distance | PASS | SC-12 "Operations occupies position 3, Finance occupies position 1" |
| C-41 | Phase Gate 2 item cites SC-12 by number | PASS | [A-08] item: "[ ] [SC-12]: Operations' `Citing:` line must include `[A-04]`..." |
| C-42 | C-37+C-41 co-occurrence | PASS | Both present |
| C-43 | All three skip-level SC attributes in single block | PASS | SC-12 contains governed role, position distance, Phase Gate 2 citation instruction |
| C-44 | Baseline-closure SC enforces C-08/C-09 connection | PASS | SC-13 inline callbacks `[Per SC-13, cite [A-01] in [A-12].]` and `[Per SC-13, cite [A-01] in [A-14].]` |
| C-45 | Format-mode declaration with criterion substitution map | PASS | SC-14 declares PROSE mode; criterion substitution map covers C-28, C-30, C-32 with prose-mode evidence tokens |
| C-46 | SC-13 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-13 BASELINE CLOSURE is the governing authority for every baseline-closure failure in [A-12] and [A-14]**; its inline callbacks at both section headers enforce the [A-01] citation obligation by label-token match." Governing authority named; [A-12] and [A-14] both named |
| C-47 | SC-14 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-14 FORMAT MODE DECLARATION is the governing authority for every format-mode compliance failure**; its criterion substitution map maps each affected criterion ID to its prose-mode evidence token." Named navigation entry with purpose declared |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 40/40

**Score: 100 / 100 — GOLDEN**

---

## V-03: Lifecycle Emphasis — SaaS Revenue Recognition / Tabular (9 boundary blocks)

Commerce → Finance → Operations. 4 stages per role; 9 total boundary blocks. SC-13 closed-chain stress test.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | PASS | 12-stage chain: subscription event → entitlement → billing period → invoice → payment → revenue allocation → deferred revenue → ASC 606 posting → close-period journal → reporting package |
| C-02 | Boundary error handling | PASS | Part A `Error Handling` column required across all 9 boundary blocks |
| C-03 | Data loss point identification | PASS | `Data Loss Flag` column with named loss point required; stage tables carry same column per SC-7 |
| C-04 | Schema state at each stage | PASS | SC-7 `Schema In \| Schema Out` per stage; `Schema Delta` per boundary block |
| C-05 | Latency characterization | PASS | SC-7 `Stage Latency`; SC-3 `Elapsed (cumul.)` across all 9 blocks |
| C-06 | Stale data windows | PASS | [A-11] stale analysis table with normal and failure-mode rows; threshold from [A-02] |
| C-07 | Domain framing | PASS | [A-02] vocabulary: subscription event, entitlement record, billing period, invoice, deferred revenue schedule, etc. |
| C-08 | Recovery prescriptions | PASS | [A-12] formula required; SC-13 inline callback "SC-13 requires [A-01] to appear here; absence is a protocol violation" |
| C-09 | Pattern trade-off analysis | PASS | [A-14] ≥1 pattern, ≥2 dimensions, all three tokens |
| C-10 | Pre-trace domain context gate | PASS | [A-02] before 12 stages; entity vocabulary includes 9 named entities |
| C-11 | Interleaved boundary gates | PASS | SC-2 enforced before every advance across 12 stages; V-03 explicitly states "4 total boundary blocks" per role section |
| C-12 | Domain entity exposure per boundary | PASS | `Entity` column; named entity from [A-02] required; "data" or "records" alone disqualifying |
| C-13 | Pre-declared staleness contract | PASS | [A-02] SLA with SC-5 immutability; 9-block elapsed chain converges at [A-11] |
| C-14 | Additive elapsed time calculation | PASS | SC-3 with "Elapsed (cumul.) accumulates across all 4 blocks" per role; [A-08] Phase Gate 2 checks "[A-07] Block 1 extends [A-04] Block 4 final value (SC-3)" — boundary-to-boundary continuity explicitly verified |
| C-15 | Incumbent baseline | PASS | [A-01] first per SC-11; loop closed via SC-13 |
| C-16 | Cross-role reference chain | PASS | Finance cites [A-01], [A-02], [A-04]; Operations cites [A-01], [A-02], [A-04], [A-07] — named tokens throughout |
| C-17 | Immutability declaration | PASS | SC-5 Commerce appends verbatim |
| C-18 | Incremental boundary elapsed | PASS | SC-3 at every block; V-03's [A-07] Block-1-extends-[A-04]-Block-4 continuity check in Phase Gate 2 adds explicit cross-role elapsed continuity verification |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` convention throughout |
| C-20 | Stage-write progression gate | PASS | SC-2 across 12 stages |
| C-21 | Binary freshness verdict | PASS | SC-4 at every boundary; 9 verdicts total |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY 14-row table |
| C-23 | Phase gate checklists | PASS | [A-05] (9 items) and [A-08] (7 items); SC-6 gates; [A-05] explicitly verifies "All 4 stages" and "All 4 blocks" |
| C-24 | Upfront constraint section | PASS | STRUCTURAL CONSTRAINTS with inline callbacks |
| C-25 | Phase gate artifacts as registry rows | PASS | [A-05] and [A-08] in registry |
| C-26 | Non-natural ordering as citation stress test | PASS | Commerce → Finance → Operations; Operations cites Commerce's [A-04] skip-level |
| C-27 | Named recovery formula | PASS | `Fall back to [A-01] if [condition]` required |
| C-28 | Named-column boundary block schema | PASS | BOUNDARY BLOCK SCHEMA standalone section with 7-column order |
| C-29 | Trade-off as prompt-required section | PASS | SC-8 + [A-14] instruction |
| C-30 | Output register declaration | PASS | REGISTER DECLARATION Parts A/B |
| C-31 | Pre-declared boundary block schema | PASS | Standalone before role output |
| C-32 | Register-specific compliance marker mapping | PASS | Part A field-by-field compliance marker table |
| C-33 | Register-invariant (non-tabular) | N/A (tabular) | Criterion does not apply |
| C-34 | Incumbent Equiv. token-cited | PASS | Part A "sole authoritative reference"; SC-9 with inline callback |
| C-35 | INCUMBENT TOTAL before trade-off | PASS | Part B; SC-10; three-role table with Grand Total; table template pre-printed with [A-04], [A-07], [A-10] row citations |
| C-36 | Baseline-first ordering | PASS | SC-11 |
| C-37 | REGISTER DECLARATION single-location authority | PASS | "sole authoritative reference for C-34 and C-35" |
| C-38 | Skip-level citation requirement | PASS | SC-12 with Operations citing Commerce's [A-04] |
| C-39 | Skip-level SC names governed role | PASS | SC-12 "Operations' `Citing:` line must include `[A-04]`" |
| C-40 | Skip-level SC declares position distance | PASS | SC-12 "Operations occupies position 3, Commerce occupies position 1" |
| C-41 | Phase Gate 2 cites SC-12 | PASS | [A-08] item: "[ ] [SC-12]: Operations' `Citing:` line must include `[A-04]` — Commerce's boundary checks, two positions prior" |
| C-42 | C-37+C-41 co-occurrence | PASS | Both present |
| C-43 | All three skip-level attributes in single block | PASS | SC-12 in V-03 names governed role, declares position distance, requires Phase Gate 2 [SC-12] citation — all three in one block |
| C-44 | Baseline-closure SC enforces C-08/C-09 | PASS | SC-13 inline callbacks on [A-12] and [A-14] |
| C-45 | Format-mode declaration (non-tabular) | N/A (tabular) | Criterion does not apply |
| C-46 | SC-13 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-13 BASELINE CLOSURE is the governing authority for every baseline-closure failure in [A-12] and [A-14]**; its inline callbacks at both section headers make the [A-01] citation obligation token-verifiable." Governing authority named; [A-12] and [A-14] both named. N.B.: paragraph omits the V-01 "reachable from this paragraph" phrase; the structural signal is present but slightly less explicit. SC-13 body confirms: "evaluators navigate to it from the register index without scanning STRUCTURAL CONSTRAINTS." |
| C-47 | SC-14 as named navigation entry (non-tabular) | N/A (tabular) | Criterion does not apply |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 40/40

**Score: 100 / 100 — GOLDEN**

**V-03 structural note**: The Phase Gate 2 [A-08] item explicitly checks "[A-07] Block 1 extends [A-04] Block 4 final value (SC-3)" — the most granular cross-role elapsed continuity checkpoint in R15. This goes beyond C-14/C-18 requirements and is V-03's unique design contribution.

---

## V-04: Role Sequence + Inertia — Pharma Procurement / Tabular (≥5 steps)

Operations → Commerce → Finance. Maximum inertia: ≥5 baseline steps.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | PASS | Chain: requisition → supplier qualification → PO → goods receipt → quality inspection → invoice matching → three-way match → payment authorization → supplier payment |
| C-02 | Boundary error handling | PASS | Part A `Error Handling` column required |
| C-03 | Data loss point identification | PASS | `Data Loss Flag` column with named loss point |
| C-04 | Schema state at each stage | PASS | SC-7 `Schema In \| Schema Out`; `Schema Delta` per boundary block |
| C-05 | Latency characterization | PASS | SC-7 `Stage Latency`; SC-3 `Elapsed (cumul.)` |
| C-06 | Stale data windows | PASS | [A-11] stale analysis table; [A-02] threshold governs |
| C-07 | Domain framing | PASS | [A-02] vocabulary: purchase requisition, supplier qualification record, PO, goods receipt, invoice, three-way match result, etc. |
| C-08 | Recovery prescriptions | PASS | [A-12] formula required; SC-13 inline callback |
| C-09 | Pattern trade-off analysis | PASS | [A-14] with all three tokens; SC-8 + SC-13 enforce |
| C-10 | Pre-trace domain context gate | PASS | [A-02] with entity vocabulary; net-30 supplier payment terms cadence |
| C-11 | Interleaved boundary gates | PASS | SC-2 inline callback at every stage advance |
| C-12 | Domain entity exposure per boundary | PASS | `Entity` column from [A-02] vocabulary required |
| C-13 | Pre-declared staleness contract | PASS | [A-02] SLA from [A-01] total duration; SC-5 immutability |
| C-14 | Additive elapsed time calculation | PASS | SC-3 at every block; [A-07] extends [A-04] final value; [A-10] extends [A-07] |
| C-15 | Incumbent baseline | PASS | [A-01] first; ≥5 steps requirement means richer vocabulary and larger [A-13] Grand Total; SC-13 closes loop to [A-12] and [A-14] — the ≥5 step specification amplifies the comparative quantification in C-09 beyond all other R15 variations |
| C-16 | Cross-role reference chain | PASS | Commerce cites [A-01], [A-02], [A-04]; Finance cites [A-01], [A-02], [A-04], [A-07] |
| C-17 | Immutability declaration | PASS | SC-5 Operations appends verbatim |
| C-18 | Incremental boundary elapsed | PASS | SC-3 at every block; [A-07] extends [A-04], [A-10] extends [A-07] |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` convention |
| C-20 | Stage-write progression gate | PASS | SC-2 across 9 stages (3+3+2) |
| C-21 | Binary freshness verdict | PASS | SC-4 at every block |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY 14-row table |
| C-23 | Phase gate checklists | PASS | [A-05] (4 combined items) and [A-08] (5 combined items) per SC-6. *Note: V-04 consolidates Phase Gate items (e.g., SC-4 and SC-9 together in one [A-08] item) vs. separate items in V-01/V-02/V-05. Structural coverage is complete but model-execution granularity is lower.* |
| C-24 | Upfront constraint section | PASS | STRUCTURAL CONSTRAINTS with inline callbacks (abbreviated form) |
| C-25 | Phase gate artifacts as registry rows | PASS | [A-05] and [A-08] in registry |
| C-26 | Non-natural ordering as citation stress test | PASS | Operations → Commerce → Finance; Finance cites Operations [A-04] skip-level |
| C-27 | Named recovery formula | PASS | `Fall back to [A-01] if [condition]` required |
| C-28 | Named-column boundary block schema | PASS | BOUNDARY BLOCK SCHEMA standalone section |
| C-29 | Trade-off as prompt-required section | PASS | SC-8 + [A-14] |
| C-30 | Output register declaration | PASS | REGISTER DECLARATION Parts A/B |
| C-31 | Pre-declared boundary block schema | PASS | Standalone section |
| C-32 | Register-specific compliance marker mapping | PASS | Part A field-by-field table |
| C-33 | Register-invariant (non-tabular) | N/A (tabular) | Does not apply |
| C-34 | Incumbent Equiv. token-cited | PASS | Part A "sole authoritative reference"; SC-9 |
| C-35 | INCUMBENT TOTAL before trade-off | PASS | Part B; SC-10; rows for Operations, Commerce, Finance, Grand Total — high Grand Total expected from ≥5 step baseline |
| C-36 | Baseline-first ordering | PASS | SC-11; ≥5 steps requirement stated in [A-01] instruction text and [A-05] Phase Gate item |
| C-37 | REGISTER DECLARATION single-location authority | PASS | "sole authoritative reference for C-34 and C-35" |
| C-38 | Skip-level citation requirement | PASS | SC-12 Finance citing Operations [A-04] |
| C-39 | Skip-level SC names governed role | PASS | SC-12 "Finance's `Citing:` line must include `[A-04]`" |
| C-40 | Skip-level SC declares position distance | PASS | SC-12 "Finance occupies position 3, Operations occupies position 1" |
| C-41 | Phase Gate 2 cites SC-12 | PASS | [A-08] item: "[ ] [SC-12]: Finance's `Citing:` line must include `[A-04]` — Operations' boundary checks, two positions prior" |
| C-42 | C-37+C-41 co-occurrence | PASS | Both present |
| C-43 | All three skip-level attributes in single block | PASS | SC-12 names governed role, declares position distance, requires Phase Gate 2 citation — single block |
| C-44 | Baseline-closure SC enforces C-08/C-09 | PASS | SC-13 inline callbacks "[Per SC-13, cite [A-01] in [A-12].]" and "[Per SC-13, cite [A-01] in [A-14].]" |
| C-45 | Format-mode declaration (non-tabular) | N/A (tabular) | Does not apply |
| C-46 | SC-13 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-13 BASELINE CLOSURE is the governing authority for every baseline-closure failure in [A-12] and [A-14]**; its inline callbacks at both section headers make the [A-01] citation obligation mechanically verifiable." + "a complete closed chain reachable from this paragraph." Governing authority named; [A-12] and [A-14] both named |
| C-47 | SC-14 as named navigation entry (non-tabular) | N/A (tabular) | Does not apply |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 40/40

**Score: 100 / 100 — GOLDEN**

---

## V-05: Format + Imperative Voice — Federal Contracting / Prose

Operations → Finance → Commerce. Prose + imperative second-person. SC-13 + SC-14 in closed-chain paragraph.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | PASS | Purchase request → obligation validation → contract vehicle → vendor notification → delivery confirmation → invoice submission → payment certification → disbursement authorization → treasury payment; 14-artifact registry |
| C-02 | Boundary error handling | PASS | Part A `**Error handling:**` bold label required; silence disqualifying |
| C-03 | Data loss point identification | PASS | `**Data loss:**` bold label with `YES — [loss point]` or `NO` required |
| C-04 | Schema state at each stage | PASS | SC-7 `**Schema in:**` and `**Schema out:**` labels; `**Schema:**` label in boundary paragraphs |
| C-05 | Latency characterization | PASS | SC-7 `**Stage latency:**` label; SC-3 `**Elapsed:**` cumulative |
| C-06 | Stale data windows | PASS | [A-11] labeled narrative with normal and failure-mode scenarios; 30-day Prompt Payment Act deadline cadence |
| C-07 | Domain framing | PASS | [A-02] vocabulary: purchase request, obligation validation record, contract vehicle assignment, payment certification record, treasury payment, etc. |
| C-08 | Recovery prescriptions | PASS | [A-12] formula required; SC-13 imperative "you must cite [A-01]"; "Do not omit [A-01]; SC-13 makes its presence mechanically required" — strongest enforcement phrasing in R15 |
| C-09 | Pattern trade-off analysis | PASS | [A-14] all three tokens; ≥1 pattern; ≥2 dimensions; SC-8 and SC-13 enforced with imperative voice |
| C-10 | Pre-trace domain context gate | PASS | [A-02] before stages; entity vocabulary; 30-day Prompt Payment Act provides concrete business cadence |
| C-11 | Interleaved boundary gates | PASS | SC-2 imperative: "Do not write Stage N+1 until you have written the preceding boundary paragraph with all seven required labels. Confirm all labels present. Then write Stage N+1." — strongest gate phrasing in R15 |
| C-12 | Domain entity exposure per boundary | PASS | Part A entity opener `**[entity]**:` required; generic "data" or "records" without named entity disqualifying |
| C-13 | Pre-declared staleness contract | PASS | [A-02] SLA with SC-5 immutability; imperative SC-5: "You must append to [A-02] verbatim..." |
| C-14 | Additive elapsed time calculation | PASS | SC-3 "You must compute `**Elapsed:**` inside each boundary paragraph"; [A-11] uses final value from [A-10] |
| C-15 | Incumbent baseline | PASS | [A-01] first; SC-13 imperative callbacks close loop |
| C-16 | Cross-role reference chain | PASS | Finance cites [A-01], [A-02], [A-04]; Commerce cites [A-01], [A-02], [A-04], [A-07] |
| C-17 | Immutability declaration | PASS | SC-5 "You must append to [A-02] verbatim" |
| C-18 | Incremental boundary elapsed | PASS | SC-3 imperative; "[A-07] extends [A-04] final value; do not reset" |
| C-19 | Machine-verifiable citation convention | PASS | `[A-xx]` convention throughout |
| C-20 | Stage-write progression gate | PASS | SC-2 imperative: "Do not write Stage N+1 until..." — most direct gate phrasing in R15 |
| C-21 | Binary freshness verdict | PASS | SC-4 imperative: "You must set `**Verdict:**` to exactly `FRESH` or `STALE`" |
| C-22 | Formal pre-declared registry table | PASS | ARTIFACT REGISTRY 14-row table |
| C-23 | Phase gate checklists | PASS | [A-05] (9 items) and [A-08] (7 items); imperative gate: "Do not allow Finance/Commerce to begin until all items are ✓" |
| C-24 | Upfront constraint section | PASS | STRUCTURAL CONSTRAINTS with inline imperative callbacks |
| C-25 | Phase gate artifacts as registry rows | PASS | [A-05] and [A-08] in registry |
| C-26 | Non-natural ordering as citation stress test | PASS | Operations → Finance → Commerce; Commerce cites Operations [A-04] skip-level |
| C-27 | Named recovery formula | PASS | "You must use the formula: `Fall back to [A-01] if [specific named failure condition]` at least once" — imperative requirement |
| C-28 | Named-label boundary schema | PASS | BOUNDARY BLOCK SCHEMA with bold-label order; SC-14 maps C-28 to "named bold labels by token match" |
| C-29 | Trade-off as prompt-required section | PASS | SC-8 imperative + SC-13 inline callbacks |
| C-30 | Output register declaration | PASS | REGISTER DECLARATION Parts A/B; SC-14 maps C-30 to bold-label presence |
| C-31 | Pre-declared boundary block schema | PASS | Standalone BOUNDARY BLOCK SCHEMA before roles |
| C-32 | Register-specific compliance marker mapping | PASS | Part A maps each field to compliance marker; SC-14 maps C-32 to per-field bold-label token |
| C-33 | Register-invariant declaration | PASS | REGISTER INVARIANTS section lists all 7 required labels; identical to V-02 structure |
| C-34 | Incumbent equiv. sentence with token | PASS | Part A; SC-9 imperative: "You must write: `**Incumbent equiv.:** [A-01]: ...`. Do not omit `[A-01]`" |
| C-35 | INCUMBENT TOTAL before trade-off | PASS | Part B; SC-10 imperative: "You must produce [A-13] immediately before [A-14]" |
| C-36 | Baseline-first ordering | PASS | SC-11 imperative: "You must write [A-01] first. Do not write any stage or boundary paragraph before [A-01] is complete." — strongest baseline-first phrasing in R15 |
| C-37 | REGISTER DECLARATION single-location authority | PASS | "sole authoritative reference for C-34 and C-35" |
| C-38 | Skip-level citation requirement | PASS | SC-12 imperative: "You must include `[A-04]` in Commerce's `Citing:` line" |
| C-39 | Skip-level SC names governed role | PASS | SC-12 "Commerce occupies position 3" — Commerce named as governed role |
| C-40 | Skip-level SC declares position distance | PASS | SC-12 "Commerce occupies position 3, Operations occupies position 1" |
| C-41 | Phase Gate 2 cites SC-12 | PASS | [A-08] item: "[ ] [SC-12]: You must verify that Commerce's `Citing:` line includes `[A-04]`... Mark ✗ if [A-04] absent" |
| C-42 | C-37+C-41 co-occurrence | PASS | Both present |
| C-43 | All three skip-level attributes in single block | PASS | SC-12 names governed role, position distance, Phase Gate 2 citation obligation — single block |
| C-44 | Baseline-closure SC enforces C-08/C-09 | PASS | SC-13 imperative "[Per SC-13, cite [A-01] in [A-12].]" and "[Per SC-13, cite [A-01] in [A-14].]" |
| C-45 | Format-mode declaration with criterion substitution map | PASS | SC-14 declares PROSE mode with criterion substitution map (C-28, C-30, C-32); identical coverage to V-02 |
| C-46 | SC-13 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-13 BASELINE CLOSURE is the governing authority for every baseline-closure failure in [A-12] and [A-14]**; its inline callbacks at both section headers enforce the [A-01] citation obligation by label-token match." Governing authority named; [A-12] and [A-14] both named |
| C-47 | SC-14 as named navigation entry in closed-chain paragraph | PASS | Closed-chain paragraph: "**SC-14 FORMAT MODE DECLARATION is the governing authority for every format-mode compliance failure**; its criterion substitution map identifies the prose-mode evidence token for each affected criterion ID." Named navigation entry; purpose declared |

**Essential**: 4/4 | **Recommended**: 3/3 | **Aspirational**: 40/40

**Score: 100 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Domain | Register | Essential | Recommended | Aspirational | Score | C-46 | C-47 |
|------|-----------|--------|----------|-----------|-------------|--------------|-------|------|------|
| 1 | V-01 | Freight billing | Tabular | 4/4 | 3/3 | 40/40 | **100** | PASS (4th nav path, enforcement sites named) | N/A |
| 1 | V-02 | Energy trade | Prose | 4/4 | 3/3 | 40/40 | **100** | PASS | PASS |
| 1 | V-03 | SaaS revenue | Tabular | 4/4 | 3/3 | 40/40 | **100** | PASS (slightly less explicit phrase) | N/A |
| 1 | V-04 | Pharma procurement | Tabular | 4/4 | 3/3 | 40/40 | **100** | PASS | N/A |
| 1 | V-05 | Federal contracting | Prose (imperative) | 4/4 | 3/3 | 40/40 | **100** | PASS | PASS |

**All five variations achieve 100/100.** C-46 and C-47 are universal PASSes where applicable.

---

## Within-100 Structural Guarantee Ranking

| Strength | Variations | Why |
|----------|-----------|-----|
| Strongest (tie) | V-01, V-05 | V-01: most granular Phase Gate items (9 + 7); V-05: imperative voice produces the most unambiguous SC obligations ("Do not write", "You must", "Do not omit") |
| Strong | V-02 | Prose + REGISTER INVARIANTS + both SC-13/SC-14 in closed-chain; complete C-46/C-47 coverage for prose register |
| Moderate | V-04 | Maximum inertia (≥5 steps) amplifies [A-13] quantification; Phase Gate items are more consolidated (4 items in [A-05]) — correct coverage but lower model-execution granularity |
| Stress test | V-03 | 9 boundary blocks and 12 stages stress-test SC-3 continuity and SC-13 callback firing rate; Phase Gate 2 explicitly checks cross-role elapsed continuity; moderate phrasing risk in closed-chain paragraph |

---

## Excellence Signals — Round 15

### E-1: SC body declares its own closed-chain registration (bidirectional pointer)

Every R15 SC-13 body contains a sentence explicitly declaring its registration in the REGISTER DECLARATION closed-chain paragraph. For example, V-01: "This SC is registered in REGISTER DECLARATION as the fourth navigation path in the closed-chain paragraph; evaluators navigate to it from the closed-chain paragraph without searching STRUCTURAL CONSTRAINTS." This creates a **bidirectional index**: the register paragraph points to SC-13 (evaluators find it from the index), and SC-13 points back to the register paragraph (evaluators know where the navigation entry lives). Prior rounds had the register entry but not the SC self-declaration of its own registration.

### E-2: Closed-chain paragraph navigation guarantee is register-invariant and boundary-density-invariant

V-03 demonstrates that SC-13's closed-chain paragraph entry holds across 9 boundary blocks and 12 stages. The inline callbacks `[Per SC-13, cite [A-01] in [A-12].]` and `[Per SC-13, cite [A-01] in [A-14].]` fire independently at the two terminal artifacts regardless of how many boundary blocks accumulate. V-02 and V-05 demonstrate the same guarantee holds across prose register variants. The closed-chain navigation entry is structurally invariant to both boundary density and output format.

### E-3: Imperative voice strengthens structural obligation signal without changing rubric outcome

V-05's SC obligations use second-person imperative throughout ("You must", "Do not write", "Do not omit"). All structural criteria score identically to declarative variants. This confirms that voice register is orthogonal to structural compliance at the rubric level, and suggests that imperative phrasing is a model-execution-level intervention — potentially reducing drift in long outputs — not a design-level distinction. A future criterion testing this relationship would need live model runs, not prompt inspection.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SC-13 body self-declares its closed-chain registration in REGISTER DECLARATION, creating a bidirectional pointer: the register index navigates to SC-13 and SC-13 explicitly names its own registration site — making baseline-closure failures reachable in both directions without scanning either document sequentially", "Closed-chain navigation guarantee is invariant to boundary density and output format register: V-03 (9 blocks, tabular) and V-02/V-05 (prose) both satisfy C-46/C-47 at the same structural guarantee level, confirming SC-13 inline callbacks fire at [A-12] and [A-14] independent of how many boundary blocks precede them"]}
```
