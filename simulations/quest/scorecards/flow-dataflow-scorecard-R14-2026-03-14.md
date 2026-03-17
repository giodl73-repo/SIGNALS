I now have enough context to score all 5 variations. Let me evaluate against the full v14 rubric.

---

# flow-dataflow — Round 14 Scoring Report

## Rubric Framework (v14)

| Tier | Criteria | Weight each | Max |
|------|----------|-------------|-----|
| Essential | C-01–C-04 | 15.00 pts | 60 |
| Recommended | C-05–C-07 | 10.00 pts | 30 |
| Aspirational | C-08–C-45 (38 total) | 0.2632 pts | 10 |
| **Total** | | | **100** |

PARTIAL = 50% of criterion weight. The R14 structural addition — SC-13 BASELINE CLOSURE with inline callbacks at [A-12] and [A-14] — is **present in all five variations**, resolving C-44 universally. C-45 (SC-14 FORMAT MODE DECLARATION) is present in V-02 and V-05 (prose), and vacuously satisfied in V-01, V-03, V-04 (tabular). The R13 pattern of C-15 PARTIAL (execution discipline only) and C-28 FAIL / C-30/C-32 PARTIAL in prose is fully closed by v14 structural additions. All five variations achieve perfect essential + recommended scores. Differentiation is driven by secondary structural density and novel enforcement mechanisms.

---

## V-01 — Finance → Operations → Commerce | Retail Omnichannel | Tabular

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | POS transaction → aggregation service → revenue management → GL journal entry → consolidation → corporate ledger → management reporting feed; unbroken chain for all in-scope items (POS transaction record, aggregation batch, GL journal entry, management reporting feed) |
| C-02 | PASS | Each boundary annotated: carrier retry on API timeout, dead-letter on address validation failure; close boundary rollback on lock conflict; plus explicit no-handling flags where applicable referencing [A-12] |
| C-03 | PASS | Named per stage: (1) POS transaction aggregation batch mismatch, (2) revenue management classification failure, (3) GL journal entry duplication, (4) consolidation snapshot gap, (5) corporate ledger lock conflict, (6) management reporting feed truncation |
| C-04 | PASS | Schema at every stage entry/exit: POS record fields → aggregation batch fields → revenue management entry → GL debit/credit pair → consolidation snapshot → ledger line → reporting row — field-level diff present |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | POS: real-time; aggregation: daily batch window; revenue management: < 30 min batch; GL journal: async < 5 min; consolidation: nightly; ledger: daily close; reporting: 23:59 ET |
| C-06 | PASS | Consolidation stale window quantified vs [A-02] threshold; failure-mode staleness (missed nightly batch → 48 h delay) addressed separately |
| C-07 | PASS | POS transaction record, aggregation batch, revenue management entry, GL journal entry, consolidation snapshot, corporate ledger line, management reporting feed throughout lineage chain |

### Aspirational — all 38 PASS

| Criterion range | Verdict | Key evidence |
|-----------------|---------|--------------|
| C-08–C-09 | PASS | Recovery prescriptions for all [A-12] items using `Fall back to [A-01] if [condition]` formula; [A-14] names alternative pattern (event-driven real-time GL posting) with ≥2 quantified dimensions |
| C-10–C-12 | PASS | [A-02] DOMAIN CONTEXT before Stage 1 with entity vocabulary locked; interleaved boundary blocks between every stage pair; domain entity named in each boundary block Entity column |
| C-13–C-15 | PASS | Staleness SLA pre-declared in [A-02]; incremental elapsed computed at every boundary; **C-15 PASS** — SC-13 BASELINE CLOSURE enforces [A-01] in both [A-12] (callback at section header) and [A-14] (callback at section header); connection is token-verifiable not execution-dependent |
| C-16–C-19 | PASS | Operations Citing: [A-01],[A-02],[A-04]; Commerce Citing: [A-01],[A-02],[A-04],[A-07]; SC-5 immutability verbatim; SC-3 incremental at every block; [A-xx] citation convention applied without exception |
| C-20–C-22 | PASS | SC-2 write-order prohibition explicit; SC-4 FRESH/STALE binary at every boundary; ARTIFACT REGISTRY table with Token/Artifact/Owner/Description before any role output |
| C-23–C-27 | PASS | [A-05] and [A-08] checklists with ticked items; SC-xx callbacks with [Apply SC-x at every block] syntax; [A-05]/[A-08] as first-class registry rows; Commerce (pos 3) cites Finance (pos 1) [A-04] skip-level per SC-12; [A-12] description in registry names the formula `Fall back to [A-01] if [condition]` |
| C-28–C-33 | PASS | BOUNDARY BLOCK SCHEMA standalone section with exact column header strings matching Part A; [A-14] cites [A-01]+[A-02]+[A-13]; REGISTER DECLARATION Parts A/B as sole authority for C-34/C-35; C-31 pre-declared schema section present; C-32 per-field column marker in Part A; C-33 vacuous PASS (tabular) |
| C-34–C-38 | PASS | `Incumbent Equiv.` column with `[A-01]: [named step + duration]` in every boundary block; [A-13] INCUMBENT TOTAL table before [A-14] with role breakdown and Grand Total; REGISTER DECLARATION Parts A/B as single-location authority; baseline-first ordering (SC-11); skip-level citation required per SC-12 |
| C-39–C-43 | PASS | SC-12 names governed role (Commerce) in body; SC-12 declares position distance (two: Commerce pos 3, Finance pos 1); Phase Gate 2 item cites [SC-12] by number; REGISTER DECLARATION closed-chain paragraph declares complete navigation taxonomy; all three skip-level SC-12 attributes co-present in single SC block |
| **C-44** | **PASS** | **SC-13 BASELINE CLOSURE** declared in STRUCTURAL CONSTRAINTS with explicit dual obligation: [A-01] in [A-12] AND [A-01] in [A-14]; inline callbacks `[Per SC-13, cite [A-01] in [A-12].]` and `[Per SC-13, cite [A-01] in [A-14].]` at both section headers; REGISTER DECLARATION closed-chain paragraph updated to include SC-13 as fourth navigation path alongside Parts A/B and SC-12 |
| **C-45** | **PASS** | Vacuous PASS — tabular register throughout; no non-tabular registers requiring a criterion substitution map; C-45's precondition (non-tabular variant) is not triggered |

**Aspirational**: 38 × 0.2632 = **10.00**

### V-01 Total: **100.0**

---

## V-02 — Finance → Commerce → Operations | Healthcare Claims Adjudication | Prose

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | EDI claim submission → eligibility verification → clinical review queue → adjudication engine → EOB generation → payment authorization → provider disbursement; all in-scope items (EDI claim record, eligibility result, adjudication decision, EOB document, disbursement confirmation) traceable in prose paragraphs |
| C-02 | PASS | Eligibility boundary: retry on gateway timeout; clinical-review boundary: dead-letter on code-set mismatch; disbursement boundary: rollback on NSF; all explicitly labeled with `**Error handling:**` bold tag |
| C-03 | PASS | Named: (1) claim rejection at eligibility screen, (2) adjudication code-set mismatch, (3) EOB generation failure on missing procedure code, (4) payment authorization NSF, (5) disbursement batch failure on closed period |
| C-04 | PASS | Schema transitions narrated per SC-7 prose form: EDI fields → eligibility result fields → adjudication decision record → EOB document fields → payment instruction → disbursement confirmation record |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Stage latency at every stage via `**Stage latency:**` bold label; eligibility: real-time < 2 s; clinical review: 4 h SLA; adjudication: batch; EOB: < 15 min; payment: weekly run at 16:00 Friday |
| C-06 | PASS | Adjudication code-set stale window quantified (ICD revision cycle); failure-mode staleness (missed weekly payment run → 7 day delay) addressed via separate labeled paragraph |
| C-07 | PASS | EDI claim record, eligibility verification result, clinical review queue item, adjudication decision, EOB document, payment authorization record, provider disbursement confirmation throughout |

### Aspirational — all 38 PASS

| Criterion range | Verdict | Key evidence |
|-----------------|---------|--------------|
| C-08–C-09 | PASS | `Fall back to [A-01] if [condition]` formula at every recovery item in [A-12]; [A-14] names alternative (real-time adjudication) with quantified trade-off dimensions |
| C-10–C-12 | PASS | [A-02] DOMAIN CONTEXT before Stage 1; prose boundary paragraphs interleaved (between every stage pair in [A-04], [A-07], [A-10]); `**[entity]**:` opener names domain entity from [A-02] vocabulary in every boundary paragraph |
| C-13–C-15 | PASS | Staleness SLA in [A-02] before Stage 1; `**Elapsed:**` incremental at every paragraph; **C-15 PASS** — SC-13 with callbacks at [A-12] and [A-14] headers makes baseline-recovery and baseline-trade-off connection token-verifiable, not execution-dependent |
| C-16–C-19 | PASS | Commerce Citing: [A-01],[A-02],[A-04]; Operations Citing: [A-01],[A-02],[A-04],[A-07]; SC-5 verbatim in [A-02]; SC-3 per paragraph; [A-xx] convention without exception |
| C-20–C-22 | PASS | SC-2 write-order prohibition in prose form; `**Verdict:**` = FRESH/STALE at every boundary paragraph; ARTIFACT REGISTRY with prose-adapted description |
| C-23–C-27 | PASS | [A-05]/[A-08] checklists; SC callback syntax with `[Apply SC-x at every paragraph]`; [A-05]/[A-08] as registry rows; Operations (pos 3) cites Finance (pos 1) [A-04] skip-level per SC-12; [A-12] registry row names recovery formula |
| **C-28** | **PASS** | **SC-14 criterion substitution map** declares: C-28 prose substitute = "Named bold labels present by token match in boundary paragraphs, per Part A compliance markers; evaluator verifies by label-string scan, not column-position scan." BOUNDARY BLOCK SCHEMA standalone section declares the labeled field sequence. With SC-14 present and bold labels uniformly applied, C-28 is satisfied by its declared prose-mode equivalent. R13 FAIL resolved. |
| **C-30** | **PASS** | SC-14 substitution map: C-30 → "Field compliance verified by bold-label presence per Part A; same token-match verifiability standard, different structural token (label vs column header)." REGISTER DECLARATION Part A provides the field compliance markers used in every boundary paragraph. R13 PARTIAL resolved. |
| **C-32** | **PASS** | SC-14 substitution map: C-32 → "Per-field bold-label token as declared compliance marker; complete mapping in REGISTER DECLARATION Part A; an evaluator uses Part A as the column-header-to-label translation table." R13 PARTIAL resolved. |
| C-29, C-31, C-33 | PASS | [A-14] cites [A-01]+[A-02]+[A-13]; BOUNDARY BLOCK SCHEMA standalone section pre-declares label sequence; REGISTER INVARIANTS section declares all seven required labels |
| C-34–C-38 | PASS | `**Incumbent equiv.:** [A-01]: [named step + duration]` in every boundary paragraph; [A-13] with bold role lines and Grand Total immediately before [A-14]; REGISTER DECLARATION Parts A/B sole authority; SC-11 baseline-first; SC-12 skip-level citation required |
| C-39–C-43 | PASS | SC-12 names Operations (governed role) in body; SC-12 declares position distance (two); Phase Gate 2 item cites [SC-12] by number; closed-chain paragraph in REGISTER DECLARATION includes SC-13 and SC-14; SC-12 attributes co-present |
| **C-44** | **PASS** | SC-13 BASELINE CLOSURE in STRUCTURAL CONSTRAINTS with inline callbacks at [A-12] and [A-14] headers; REGISTER DECLARATION closed-chain paragraph lists SC-13 as governing authority for baseline-closure failures |
| **C-45** | **PASS** | **SC-14 FORMAT MODE DECLARATION** as named SC entry in STRUCTURAL CONSTRAINTS; three-row criterion substitution table mapping C-28, C-30, C-32 to prose-mode bold-label equivalents; evaluator can determine compliance for all three criteria by criterion ID without output structure inspection; REGISTER DECLARATION closed-chain paragraph lists SC-14 as governing authority for format-mode compliance failures |

**Aspirational**: 38 × 0.2632 = **10.00**

### V-02 Total: **100.0**

---

## V-03 — Commerce → Finance → Operations | Manufacturing Invoice | Tabular | 4 stages/role (9 boundary blocks)

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Sales order → inventory check → production order → BOM pick list → materials requisition → PO creation → vendor invoice → AP validation → payment authorization → disbursement → goods receipt → production floor release; 12-stage chain, all in-scope items (sales order record, BOM pick list, purchase order, vendor invoice, disbursement confirmation, goods receipt scan) connected |
| C-02 | PASS | All 9 boundary blocks across 3 roles × 3 blocks each annotated; no silence; `no handling — see [A-12]` used explicitly where appropriate |
| C-03 | PASS | Named per stage: BOM mismatch (Stage 3), materials requisition quantity error (Stage 4), PO pricing discrepancy (Stage 5), vendor invoice coding error (Stage 6), AP validation hold (Stage 7), payment authorization timeout (Stage 9), disbursement NSF (Stage 10), goods receipt barcode failure (Stage 11), production floor token collision (Stage 12) |
| C-04 | PASS | Schema diffs at all 12 stage exits — 4 per role; field-level diff showing each entity transformation |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | 12 stage latency annotations across 4 stages × 3 roles; thorough characterization per stage |
| C-06 | PASS | Vendor invoice price stale window (daily feed) and goods receipt stale window (production shift boundary) quantified; failure-mode staleness for each addressed separately |
| C-07 | PASS | Sales order record, BOM pick list, materials requisition, purchase order, vendor invoice, AP validation record, payment authorization, disbursement confirmation, goods receipt scan, production floor release token throughout |

### Aspirational — all 38 PASS

| Criterion range | Verdict | Key evidence |
|-----------------|---------|--------------|
| C-08–C-09 | PASS | Recovery formula applied at every [A-12] item citing [A-01]; [A-14] names alternative (ERP direct-requisition bypass) with quantified dimensions |
| C-10–C-14 | PASS | [A-02] DOMAIN CONTEXT gate; 9 interleaved boundary blocks (3 per role) between every consecutive stage pair — highest structural density among 5 variations; entity named in every block; staleness SLA pre-declared; incremental elapsed across all 9 blocks |
| **C-15** | **PASS** | SC-13 BASELINE CLOSURE present in STRUCTURAL CONSTRAINTS; callbacks at [A-12] header `[Per SC-13, cite [A-01] in [A-12].]` and [A-14] header `[Per SC-13, cite [A-01] in [A-14].]`; REGISTER DECLARATION includes SC-13 in closed-chain paragraph. SC-13 survives 9-block boundary density and 12-stage elapsed chain — callback obligation enforced regardless of distance from STRUCTURAL CONSTRAINTS |
| C-16–C-19 | PASS | Finance Citing: [A-01],[A-02],[A-04]; Operations Citing: [A-01],[A-02],[A-04],[A-07]; SC-5 verbatim; incremental elapsed at all 9 blocks; [A-xx] convention |
| C-20–C-22 | PASS | SC-2 per stage advance (11 applications across 12 stages); FRESH/STALE at all 9 boundary blocks; ARTIFACT REGISTRY table |
| C-23–C-27 | PASS | [A-05]/[A-08] checklists; callback syntax; gate artifacts as registry rows; Operations (pos 3) cites Commerce (pos 1) [A-04] skip-level; formula named in [A-12] registry description |
| C-28–C-33 | PASS | BOUNDARY BLOCK SCHEMA with exact column headers; [A-14] cites all three tokens; REGISTER DECLARATION Parts A/B sole authority; C-31 pre-declared schema; C-32 per-field column markers; C-33 vacuous PASS (tabular) |
| C-34–C-38 | PASS | Incumbent Equiv. column with [A-01] token in all 9 blocks (highest coverage — 9 rows vs 4–6 in other tabular variations); [A-13] table with Commerce/Finance/Operations rows and Grand Total; REGISTER DECLARATION authority; SC-11; skip-level citation |
| C-39–C-43 | PASS | SC-12 body: names Operations (governed role), declares position distance (two: Operations pos 3, Commerce pos 1); Phase Gate 2 item cites [SC-12]; closed-chain declaration includes SC-13; SC-12 attributes co-present |
| **C-44** | **PASS** | SC-13 BASELINE CLOSURE in STRUCTURAL CONSTRAINTS with dual callbacks at [A-12] and [A-14]; REGISTER DECLARATION closed-chain includes SC-13; maximum structural stress on callback mechanism across 9 boundary blocks and 12 stages |
| **C-45** | **PASS** | Vacuous PASS — tabular register throughout |

**Aspirational**: 38 × 0.2632 = **10.00**

### V-03 Total: **100.0**

---

## V-04 — Operations → Commerce → Finance | SaaS Subscription Billing | Tabular | ≥5 baseline steps + SC-15

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Subscriber sign-up event → entitlement provisioning → subscription plan record → invoice document → payment processing → payment confirmation event → revenue recognition entry → GL posting; all in-scope items (subscriber sign-up event, entitlement record, subscription plan record, invoice document, payment confirmation, revenue recognition entry, GL posting) connected |
| C-02 | PASS | Entitlement provisioning boundary: retry on activation timeout; subscription-to-invoice boundary: dead-letter on plan-code mismatch; payment gateway boundary: rollback on NSF; revenue recognition boundary: dead-letter on period-close lock |
| C-03 | PASS | Named: (1) entitlement activation failure, (2) plan-code mismatch at invoice generation, (3) payment gateway NSF, (4) duplicate subscription detection collision, (5) revenue recognition period-close lock, (6) GL posting timeout |
| C-04 | PASS | Schema diffs at all stage exits: sign-up event fields → entitlement record → subscription plan fields → invoice document fields → payment transaction fields → confirmation event → revenue recognition entry fields → GL posting record |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | Sign-up: real-time; entitlement: < 60 s; subscription record: async; invoice: batch < 4 h; payment: real-time gateway; revenue recognition: nightly; GL: monthly close |
| C-06 | PASS | Plan-code stale window (quarterly update cycle); failure-mode staleness (missed nightly revenue recognition → 24 h) addressed |
| C-07 | PASS | Subscriber sign-up event, entitlement record, subscription plan record, invoice document, payment transaction, payment confirmation event, revenue recognition entry, GL posting throughout |

### Aspirational — all 38 PASS

| Criterion range | Verdict | Key evidence |
|-----------------|---------|--------------|
| C-08–C-09 | PASS | SC-15 RECOVERY FORMULA applied at every [A-12] item: `RECOVERY: [loss point] → [manual equivalent step from [A-01]] → [verification]`; each item names a specific [A-01] step by name; [A-14] cites [A-01]+[A-02]+[A-13] with ≥2 dimensions |
| C-10–C-14 | PASS | [A-02] gate; boundary blocks interleaved; entity named per block; staleness SLA from [A-02]; incremental elapsed at every block |
| **C-15** | **PASS** | SC-13 BASELINE CLOSURE with callbacks at [A-12] and [A-14] headers; SC-15 doubly enforces [A-01] at item level. Maximum inertia framing (≥5 steps) ensures distinct manual equivalents for every Incumbent Equiv. cell and every recovery item — baseline is provably covered, not opportunistically cited |
| C-16–C-19 | PASS | Commerce Citing: [A-01],[A-02],[A-04]; Finance Citing: [A-01],[A-02],[A-04],[A-07] (Finance at pos 3 cites Operations at pos 1 skip-level per SC-12); SC-5 verbatim; [A-xx] convention |
| C-20–C-22 | PASS | SC-2 per stage; binary FRESH/STALE at every block; ARTIFACT REGISTRY |
| C-23–C-27 | PASS | [A-05]/[A-08] checklists; SC callback syntax; gate artifacts as registry rows; Finance (pos 3) cites Operations (pos 1) skip-level; **C-27 PASS** — SC-15 named in variation as "named spec-level design feature of this variation" in SC-15 text itself; formula structure explicitly declared |
| C-28–C-33 | PASS | BOUNDARY BLOCK SCHEMA; [A-14] cites all three tokens; REGISTER DECLARATION Parts A/B; C-31/C-32 present; C-33 vacuous PASS |
| C-34–C-38 | PASS | Incumbent Equiv. column with [A-01] token throughout; [A-13] immediately before [A-14] with Operations/Commerce/Finance rows; REGISTER DECLARATION authority; SC-11; skip-level |
| C-39–C-43 | PASS | SC-12 body: names Finance (governed role), declares position distance (two: Finance pos 3, Operations pos 1); Phase Gate 2 item cites [SC-12]; closed-chain includes SC-13; all SC-12 attributes co-present |
| **C-44** | **PASS** | SC-13 BASELINE CLOSURE in STRUCTURAL CONSTRAINTS with callbacks at [A-12] and [A-14] headers; REGISTER DECLARATION closed-chain includes SC-13; SC-15 adds a second structural guarantee that every [A-12] item cites [A-01] at step level — making C-44 doubly enforced in this variation |
| **C-45** | **PASS** | Vacuous PASS — tabular register throughout |

**Aspirational**: 38 × 0.2632 = **10.00**

### V-04 Total: **100.0**

---

## V-05 — Operations → Finance → Commerce | E-commerce Fulfillment | Prose + Imperative Voice

### Essential — 60/60

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Warehouse pick confirmation → packing verification → shipping label → carrier handoff scan → in-transit GPS event → delivery attempt scan → delivery confirmation event → order status update → customer notification; all in-scope items (pick confirmation event, pack verification record, shipping label, carrier handoff scan, delivery confirmation event, order status update) traceable in prose paragraphs |
| C-02 | PASS | Each boundary has `**Error handling:**` bold label; packing boundary: retry on weight discrepancy; carrier handoff: dead-letter on label scan failure; delivery attempt: rollback on address mismatch; explicit `no handling — see [A-12]` where no mechanism exists |
| C-03 | PASS | Named: (1) barcode scan failure at packing verification, (2) label creation error on weight discrepancy, (3) carrier handoff rejection on hazmat flag, (4) GPS event gap in transit, (5) delivery attempt failure on access restriction, (6) duplicate confirmation event |
| C-04 | PASS | Schema transitions narrated with `**Schema in:**` / `**Schema out:**` labels per SC-7: pick event fields → pack record → shipping label → carrier scan record → GPS event → delivery record → order status → notification payload |

### Recommended — 30/30

| ID | Verdict | Evidence |
|----|---------|----------|
| C-05 | PASS | `**Stage latency:**` label at every stage; pick: < 30 s; packing: < 20 min; label: < 2 min; carrier: real-time; in-transit: hourly GPS; delivery: same-day cutoff 14:00 |
| C-06 | PASS | Carrier status stale window (4 h GPS interval); failure-mode staleness (GPS blackout → 24 h) addressed separately in [A-11] |
| C-07 | PASS | Pick confirmation event, pack verification record, shipping label, carrier handoff scan, in-transit GPS event, delivery attempt record, delivery confirmation event, order status update, customer notification throughout |

### Aspirational — all 38 PASS

| Criterion range | Verdict | Key evidence |
|-----------------|---------|--------------|
| C-08–C-09 | PASS | `Fall back to [A-01] if [condition]` formula at every [A-12] item in imperative form; [A-14] names alternative (pre-positioned carrier API) with ≥2 dimensions |
| C-10–C-14 | PASS | [A-02] gate; prose boundary paragraphs interleaved between every stage pair; `**[entity]**:` opener names entity from [A-02]; staleness SLA pre-declared; `**Elapsed:**` incremental at every paragraph |
| **C-15** | **PASS** | SC-13 BASELINE CLOSURE in imperative form: "Write [A-01] as a citation token in two places and only those two places satisfy this constraint." Callbacks `[Per SC-13, cite [A-01] in [A-12].]` and `[Per SC-13, cite [A-01] in [A-14].]` at section headers. Imperative phrasing is the strongest enforcement voice for this criterion |
| C-16–C-19 | PASS | Finance Citing: [A-01],[A-02],[A-04]; Commerce Citing: [A-01],[A-02],[A-04],[A-07]; SC-5 verbatim in [A-02]; SC-3 per paragraph; [A-xx] token convention |
| C-20–C-22 | PASS | SC-2: "Do not write Stage N+1 until..." — imperative prohibition gives strongest expression; `**Verdict:**` FRESH/STALE per paragraph; ARTIFACT REGISTRY |
| C-23–C-27 | PASS | [A-05]/[A-08] checklists; SC callback syntax; gate artifacts as registry rows; Commerce (pos 3) cites Operations (pos 1) [A-04] skip-level per SC-12; formula named in [A-12] registry row |
| **C-28** | **PASS** | SC-14 substitution map (imperative form): "use Part A compliance marker strings as the token targets" for C-28 → named bold labels by token match. BOUNDARY BLOCK SCHEMA standalone section declares label sequence. Evaluator verifies by label-string scan. R13-class FAIL fully resolved by SC-14 |
| **C-30** | **PASS** | SC-14: "Field compliance verified by bold-label presence per Part A; same token-match standard, different structural token type." Part A provides complete field compliance markers used uniformly |
| **C-32** | **PASS** | SC-14: "the complete per-field mapping is in Part A; use Part A as the substitution authority." Part A is the per-field bold-label declaration. R13 PARTIAL resolved |
| C-29, C-31, C-33 | PASS | [A-14] cites all three tokens; BOUNDARY BLOCK SCHEMA standalone section pre-declares label sequence; REGISTER INVARIANTS section lists all seven required labels |
| C-34–C-38 | PASS | `**Incumbent equiv.:** [A-01]: [named step + duration]` in every paragraph; [A-13] bold role lines + Grand Total before [A-14]; REGISTER DECLARATION Parts A/B sole authority; SC-11; skip-level citation |
| C-39–C-43 | PASS | SC-12 names Commerce (governed role) in body; SC-12 declares position distance (two: Commerce pos 3, Operations pos 1); Phase Gate 2 item cites [SC-12] by number; closed-chain paragraph includes SC-13 and SC-14; SC-12 attributes co-present |
| **C-44** | **PASS** | SC-13 BASELINE CLOSURE in imperative second-person voice: "if you write a recovery item without [A-01] it is a protocol violation" and "Writing either section without the [A-01] token is a protocol violation detectable by token scan." Strongest enforcement phrasing among all 5 variations |
| **C-45** | **PASS** | SC-14 FORMAT MODE DECLARATION in imperative form with three-row criterion substitution table; REGISTER DECLARATION closed-chain paragraph lists SC-14 as governing authority for format-mode compliance failures; evaluator navigation path from failed C-28/C-30/C-32 check to SC-14 to prose-mode substitute is token-verifiable |

**Aspirational**: 38 × 0.2632 = **10.00**

### V-05 Total: **100.0**

---

## Rankings

| Rank | Variation | Score | Differentiating feature |
|------|-----------|-------|------------------------|
| **1** | **V-04** | **100.0** | SC-15 dual enforcement — every recovery item must name the specific [A-01] step it maps to, not just cite token; ≥5 baseline steps guarantee distinct manual equivalents for all boundary and recovery cells; C-44 doubly enforced |
| 2 | V-02 | 100.0 | First clean prose implementation of SC-14 criterion substitution map; closes R13 C-28 FAIL + C-30/C-32 PARTIAL through declared prose equivalence, not structural approximation |
| 3 | V-05 | 100.0 | Imperative voice gives SC-13 and SC-14 strongest enforcement phrasing; C-20 prohibition ("Do not write...") and SC-14 ("Do not produce markdown tables...") are maximally directive |
| 4 | V-03 | 100.0 | Highest structural density — 9 boundary blocks across 3 roles; SC-13 callback survives maximum distance from STRUCTURAL CONSTRAINTS to [A-12]/[A-14]; 9 Incumbent Equiv. cells |
| 5 | V-01 | 100.0 | Standard tabular C-44 baseline; all criteria met; least novel structural feature |

---

## Excellence Signals — V-04

### E-01: SC-15 as per-item baseline step-mapping beyond token citation

SC-13 requires [A-01] to appear as a citation token in [A-12] and [A-14]. SC-15 adds a second structural layer: each recovery item must name the specific [A-01] manual step it maps to, using the formula `RECOVERY: [loss point] → [manual equivalent step from [A-01]] → [verification]`. This distinction is significant:

- **SC-13** enforces: "Is [A-01] cited anywhere in [A-12]?" — section-level token check
- **SC-15** enforces: "Does each recovery item name a specific [A-01] step?" — item-level step mapping

An evaluator auditing [A-12] under SC-13 only needs one `[A-01]` token to pass. Under SC-15, every item is independently auditable against [A-01]'s named step list. A recovery item that cites `[A-01]` without naming which step maps to it fails SC-15 even if it passes SC-13. This is a qualitatively different constraint — it forces the [A-01] baseline to be a structured lookup table for every recovery action, not just a citation target.

### E-02: Maximum inertia framing as audit-surface multiplier

Requiring ≥5 named manual steps in [A-01] ensures that every boundary block's Incumbent Equiv. cell and every recovery item in [A-12] can cite a distinct named step. With ≥3 steps (the minimum in other variations), a three-stage pipeline can satisfy all Incumbent Equiv. cells and recovery items with the same three steps repeatedly — the baseline is technically covered but the correspondence is shallow. With ≥5 steps and SC-15's per-item mapping requirement, each of the five manual steps is traceable to specific boundary transitions and recovery scenarios. The baseline becomes a complete coverage ledger.

**Generalizable rule**: Require ≥N baseline steps where N equals the number of structurally distinct boundary-or-recovery events in the variation. When N ≥ 5, step reuse becomes detectable as a coverage gap rather than hidden behind legitimate repetition.

---

## New patterns for C-46, C-47 (v15 candidates)

Both V-04 excellence signals surface structural properties not yet captured in C-01–C-45:

**Candidate C-46 — Per-item baseline step-mapping SC**: STRUCTURAL CONSTRAINTS must contain a named SC requiring every recovery item in [A-12] to identify the specific [A-01] step it maps to by name — not just cite [A-01] as a section-level token. A recovery item that cites `[A-01]` without naming the manual step fails this criterion. SC-13 establishes token-citation obligation at section level; C-46 establishes step-mapping obligation at item level.

**Candidate C-47 — Minimum baseline step count proportional to boundary count**: [A-01] must contain ≥N named manual steps, where N is declared in the variation spec and is sufficient to provide a distinct manual equivalent for every boundary block in the variation. A baseline with fewer steps than structurally distinct boundary events forces step reuse, masking whether baseline coverage is genuine. The step count declaration must appear in [A-01]'s registry description (e.g., "≥5 named steps with durations") and Phase Gate 1 must verify the count.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SC-15 per-item baseline step-mapping: require each recovery item to name the specific [A-01] manual step it maps to using a named formula structure — section-level token citation (SC-13) is necessary but not sufficient; item-level step mapping creates a recovery-to-baseline correspondence audit-able at each item without inspecting surrounding prose", "minimum baseline step count proportional to boundary density: require [A-01] to contain at least as many named manual steps as there are structurally distinct boundary events in the variation, declared in the registry row and verified in Phase Gate 1; fewer steps than boundary events forces reuse that masks genuine coverage gaps behind legitimate repetition"]}
```
