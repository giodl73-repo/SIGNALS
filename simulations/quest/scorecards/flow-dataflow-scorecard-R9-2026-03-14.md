# flow-dataflow Scorecard — Round 9

> **Scoring basis**: trace artifact is `placeholder`; evaluation is design-level — assessing whether each variation's structural innovations reliably produce criterion-satisfying output.

**Baseline assumption (C-01..C-04, C-06..C-07, C-08..C-14, C-16..C-27):** Carried from R8 as PASS unless a variation's design specifically stresses or strengthens a criterion. Differences are called out per variation.

---

## V-01 — Output format axis (Finance → Operations → Commerce)

Natural order. All tabular. BOUNDARY BLOCK SCHEMA + REGISTER DECLARATION + SC-7 + SC-8.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01 | Lineage chain | PASS | Natural order preserves unbroken source → stage → destination |
| C-02 | Boundary error handling | PASS | Boundary schema enforces error-handling column presence |
| C-03 | Data loss identification | PASS | Schema enforces loss-point annotation per stage |
| C-04 | Schema at each stage | PASS | Stage table schema captures entry/exit field diffs |
| C-05 | Latency characterization | PASS | SC-7 mandates `Stage Latency` column — structurally enforced, not opportunistic |
| C-06 | Stale data windows | PASS | Carried from prior rounds |
| C-07 | Domain framing | PASS | Domain entity names in lineage chain |
| C-09 / C-29 | Trade-off / trade-off as required section | PASS | SC-8 mandates `[A-13] TRADE-OFF ANALYSIS` with explicit `[A-01]` + `[A-02]` token citations |
| C-15 | Incumbent baseline | PASS | Assumed passing from R8; SC-8 trade-off mandate creates closure loop |
| C-16 | Cross-role reference chain | PASS | Natural order (Finance → Ops → Commerce) minimizes citation distance |
| C-26 | Non-natural ordering as citation stress test | **FAIL** | Natural order does not exercise non-adjacent citation compliance |
| C-28 | Named-column boundary schema | PASS | BOUNDARY BLOCK SCHEMA declares column schema before any role output |
| C-29 | Trade-off as required section | PASS | SC-8 structural mandate with dual token citations |
| C-30 | Output register declaration | PASS | REGISTER DECLARATION explicit |
| C-31 | Pre-declared schema section | PASS | Standalone BOUNDARY BLOCK SCHEMA before any role — discoverable without reading role instructions |
| C-32 | Register-specific compliance markers | PASS | REGISTER DECLARATION enumerates column-name as verification method per field |
| C-33 | Register-invariant declaration | PASS | Tabular-default, no deviation — criterion trivially satisfied |

**Score breakdown:**
- Essential (C-01..C-04): 60 / 60
- Recommended (C-05..C-07): 30 / 30
- Aspirational (C-08..C-33, 26 criteria × 0.385 pts): 25 PASS + 0 PARTIAL + 1 FAIL (C-26) = 9.62 / 10

**V-01 total: 99.6 → 98**

---

## V-02 — Role sequence axis (Operations → Commerce → Finance)

Same structural fixes as V-01. Finance-last ordering isolates citation-chain effects.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01..C-04 | Essential | PASS | All 4 — structural fixes unchanged |
| C-05 | Latency | PASS | SC-7 inherited |
| C-06..C-07 | Recommended | PASS | Unchanged |
| C-16 | Cross-role reference chain | **PARTIAL** | Finance-last requires Operations and Commerce roles to be cited backward across maximum distance; citation integrity depends on execution compliance, not structural enforcement |
| C-26 | Non-natural ordering as citation stress | PASS | Operations → Commerce → Finance exercises non-adjacent citation path |
| C-28..C-33 | R8/R9 gap fixes | PASS | Same as V-01: BOUNDARY BLOCK SCHEMA, REGISTER DECLARATION, SC-7, SC-8 |

**Score breakdown:**
- Essential: 60 / 60
- Recommended: 30 / 30
- Aspirational: 25 PASS + 1 PARTIAL + 0 FAIL = 25 × 0.385 + 0.192 = 9.82 / 10

**V-02 total: 99.8 — but C-16 PARTIAL reflects real execution risk**
**Adjusted: 93** (citation-chain PARTIAL carries practical downstream risk beyond point math)

---

## V-03 — Phrasing register axis (Commerce → Finance → Operations, conversational)

REGISTER INVARIANT DECLARATION serves as combined C-31 + C-32 + C-33 anchor. No column headers.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01..C-04 | Essential | PASS | Structural — register-independent |
| C-05 | Latency | PASS | SC-7 conversational equivalent: `Stage latency:` sentence-opener per hypothesis |
| C-06..C-07 | Recommended | PASS | Stale windows and domain framing register-independent |
| C-16 | Cross-role reference chain | PARTIAL | Commerce → Finance → Operations is non-natural; non-adjacent citation in prose harder to trace than named column |
| C-26 | Non-natural ordering | PASS | Commerce-first is non-natural |
| C-28 | Named-column boundary schema | **PARTIAL** | Conversational register has no column headers — inherent structural limitation; REGISTER INVARIANT DECLARATION names expected fields but cannot provide column-existence verification |
| C-31 | Pre-declared schema section | PASS | REGISTER INVARIANT DECLARATION appears before any role output; fields enumerated with marker form — satisfies "discoverable without reading role instructions" |
| C-32 | Register-specific compliance markers | PASS | Sentence-opener and bold-keyword mapping enumerated per field |
| C-33 | Register-invariant declaration | PASS | Core structural innovation of V-03 — explicitly names surviving criteria and per-criterion check method in conversational form |

**Score breakdown:**
- Essential: 60 / 60
- Recommended: 30 / 30
- Aspirational: 23 PASS + 2 PARTIAL (C-16, C-28) + 1 FAIL (N/A) = 23 × 0.385 + 2 × 0.192 = 8.855 + 0.385 = 9.24 / 10

**V-03 total: 99.24 — but C-28 PARTIAL is structurally irreducible in conversational**
**Adjusted: 87** (C-28 limitation is inherent, not addressable; evaluator verification degrades silently on re-use without re-reading REGISTER INVARIANT DECLARATION)

---

## V-04 — Combined: role sequence (Commerce → Operations → Finance) + lifecycle emphasis

Maximally non-natural. 7-column boundary schema adds `Incumbent Equiv.`. SC-10 requires `[A-12] INCUMBENT TOTAL` before TRADE-OFF ANALYSIS.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01..C-04 | Essential | PASS | Structural fixes unchanged |
| C-05 | Latency | PASS | SC-7 inherited; 7-column schema includes Stage Latency |
| C-06..C-07 | Recommended | PASS | Unchanged |
| C-15 | Incumbent baseline | PASS | SC-10 `[A-12] INCUMBENT TOTAL` is a required artifact before trade-off; `Incumbent Equiv.` per boundary row creates granular comparison |
| C-16 | Cross-role reference chain | **PARTIAL** | Finance-last is maximally non-natural — longest citation chain; Commerce and Operations roles must be cited backward from Finance |
| C-26 | Non-natural ordering | PASS | Commerce → Operations → Finance most stressed ordering |
| C-28..C-30 | R8 gap fixes | PASS | 7-column schema covers C-28; SC-8 covers C-29; REGISTER DECLARATION covers C-30 |
| C-31 | Pre-declared schema | PASS | 7-column schema declared before any role |
| C-32 | Compliance markers | PASS | Column names enumerated in REGISTER DECLARATION |
| C-33 | Register-invariant | PASS | All tabular — trivially satisfied |
| C-09 / C-29 | Trade-off depth | PASS+ | SC-9 `Incumbent Equiv.` column makes trade-off numerically grounded per boundary, not just aggregate |

**Score breakdown:**
- Essential: 60 / 60
- Recommended: 30 / 30
- Aspirational: 25 PASS + 1 PARTIAL (C-16) = 25 × 0.385 + 0.192 = 9.817 / 10

**V-04 total: 99.8 — C-16 PARTIAL from maximum citation distance**
**Adjusted: 94** (citation stress real but mitigated by strong lifecycle scaffolding)

---

## V-05 — Combined: dual-register + REGISTER TRANSLATION TABLE

Finance (tabular) → Commerce (conversational) → Operations (tabular). REGISTER TRANSLATION TABLE unifies C-31 + C-32 + C-33 in one artifact.

| ID | Criterion | Score | Evidence |
|----|-----------|-------|----------|
| C-01..C-04 | Essential | PASS | Structural — register-independent |
| C-05 | Latency | PASS | SC-7 tabular column for Finance/Operations; `Stage latency:` opener for Commerce conversational — both mapped in REGISTER TRANSLATION TABLE |
| C-06..C-07 | Recommended | PASS | Unchanged |
| C-16 | Cross-role reference chain | **PARTIAL** | Operations must cite Finance across a conversational Commerce hop — two-register citation chain is non-trivial; conversational middle section lacks column anchors for backward citation |
| C-26 | Non-natural ordering | **PARTIAL** | Finance is natural first; Commerce and Operations are non-natural; partial credit — not maximally stressed |
| C-28 | Named-column boundary schema | PASS (Finance, Operations) / **PARTIAL** (Commerce) | Tabular roles satisfy fully; conversational Commerce uses REGISTER TRANSLATION TABLE to map field compliance markers — partial structural equivalence |
| C-31 | Pre-declared schema section | PASS | REGISTER TRANSLATION TABLE is a single pre-role structure declaring schema for all registers |
| C-32 | Register-specific compliance markers | PASS | REGISTER TRANSLATION TABLE explicitly maps each field to column-name (tabular) or sentence-opener/bold-keyword (conversational) |
| C-33 | Register-invariant declaration | PASS | REGISTER TRANSLATION TABLE names surviving criteria for conversational Commerce and maps check method — cleanest implementation of C-33 across all variations |

**Score breakdown:**
- Essential: 60 / 60
- Recommended: 30 / 30
- Aspirational: 23 PASS + 3 PARTIAL (C-16, C-26, C-28-Commerce) = 23 × 0.385 + 3 × 0.192 = 8.855 + 0.577 = 9.43 / 10

**V-05 total: 99.43**
**Adjusted: 95** (REGISTER TRANSLATION TABLE is the most unified C-31/C-32/C-33 implementation; execution risk from two-register citation gap)

---

## Composite Scores and Ranking

| Rank | Variation | Score | Decisive Factor |
|------|-----------|-------|-----------------|
| 1 | **V-01** | **98** | All R9 fixes, natural order, no execution risk |
| 2 | V-05 | 95 | REGISTER TRANSLATION TABLE unifies C-31+C-32+C-33; dual-register citation stress costs points |
| 3 | V-04 | 94 | Per-boundary INCUMBENT TOTAL is strongest C-15/C-09 integration; Finance-last citation stress |
| 4 | V-02 | 93 | Same fixes as V-01; Finance-last citation stress without V-04's lifecycle offset |
| 5 | V-03 | 87 | C-28 inherently PARTIAL in conversational — structurally irreducible limitation |

**All essential criteria (C-01..C-04): PASS across all five variations.**

---

## Excellence Signals (from V-01)

**ES-01 — BOUNDARY BLOCK SCHEMA as a standalone pre-role section**
The schema is declared as a named, discrete document section appearing before any role output. Evaluators verify column completeness by comparing role output columns against the pre-declared set — no reading of role instructions required. This is the structural form C-31 codifies; V-01 is its cleanest implementation.

**ES-02 — REGISTER DECLARATION with explicit column-name-as-verification-method enumeration**
Each field in the REGISTER DECLARATION names not just the field but the verification method (column name for tabular register). Evaluator verification is a column-scan, not a semantic read. V-05 extends this to dual registers simultaneously.

**ES-03 — SC-7 Stage Latency as required table column**
Closing C-05 via a structural column requirement rather than a prompt suggestion prevents regression across future variations. V-08's boundary column innovations had created a C-05 gap; SC-7 closes it as a schema-level guarantee.

**ES-04 — SC-8 [A-13] TRADE-OFF ANALYSIS as structurally required section with dual token citations**
Previous rounds showed C-09/C-29 failing or partial because trade-off analysis was opportunistic. Mandating the section name and requiring named token citations to both `[A-01]` and `[A-02]` makes the criterion a pass/fail structural gate rather than a quality judgment.

---

## Notable V-05 Signal (not top-ranked, but strongest architectural contribution)

**REGISTER TRANSLATION TABLE as single unified multi-register compliance artifact** — a pre-role lookup structure that simultaneously declares the boundary block schema (C-31), maps per-field compliance markers for all registers in scope (C-32), and identifies surviving criteria with check methods for non-tabular registers (C-33). Eliminates the need for three separate compliance sections when the output alternates registers mid-sequence. Candidate for C-34.

---

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["unified-register-translation-table-as-single-artifact-satisfying-C31-C32-C33", "per-boundary-incumbent-equiv-column-enabling-granular-pipeline-vs-manual-audit-trail"]}
```
