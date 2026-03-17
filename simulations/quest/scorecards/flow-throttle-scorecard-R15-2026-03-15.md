---

# flow-throttle Scorecard — Round 15

**Rubric:** v15 | **Max composite:** 250 | **Date:** 2026-03-16
**Baseline:** R14 best = 235/250 under v15 (C-38, C-39, C-40 all FAIL)

---

## Scoring Approach

Criteria C-01–C-37 carry from R14 (all PASS across every variation — identical architecture). Only the three new criteria and any observable deltas are scored per-variation.

**Scoring key:** PASS = 5 pts (aspirational), 15 pts (essential). PARTIAL = floor(pts/2). FAIL = 0.

---

## Per-Variation Evaluation

### V-01 — Output Format: count + closure; no PROHIBITED clause

**Section C structure in V-01:**

- Header: *"This section declares 7 required annotations. Completeness verification: count the rows in the table below; the expected row count is 7. A row count below 7 indicates a missing annotation requirement — this section is incomplete and FORMAT CONTRACT COMPLETE may not be stated."*
- Closure (after table): *"This inventory is closed. An annotation not listed here does not exist as a contract requirement. An annotation listed here that is absent from its anchor site in the body is a FORMAT CONTRACT violation."*
- No PROHIBITED clause anywhere in Section C.

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **C-38** | **PASS** | Count declared at Section C header before enumeration: "declares 7 required annotations" + "expected row count is 7" — count-scan verifiable without reading annotation content |
| **C-39** | **PASS** | Canonical form present: sentence 1 — "This inventory is closed. An annotation not listed here does not exist as a contract requirement." Sentence 2 (bidirectional) — "An annotation listed here that is absent from its anchor site in the body is a FORMAT CONTRACT violation." Both directions covered |
| **C-40** | **FAIL** | No PROHIBITED clause inside the annotation inventory. The closure sentence references absence as a violation, but there is no explicit `PROHIBITED:` form with an inline failure-mode annotation — the violation consequence is stated passively, not as an active prohibition |

**C-01–C-05 (essential):** All PASS — structural tables and phase structure unchanged.
**C-06–C-37 (recommended + aspirational):** All PASS — identical to R14 baseline.

**V-01 composite:** 235 (carry) + 5 (C-38) + 5 (C-39) + 0 (C-40) = **245/250**

---

### V-02 — Phrasing Register: count + canonical closure + PROHIBITED with inline annotation

**Section C structure in V-02:**

- Header: *"This section declares 7 required annotations. Count-scan verification: expected rows = 7; a row count below 7 is a completeness gap detectable without reading annotation content."*
- Closure (after table): *"This inventory is closed. An annotation not listed here does not exist as a contract requirement. An annotation listed here that is absent from its anchor site in the body is a FORMAT CONTRACT violation."*
- PROHIBITED (at inventory close, before FORMAT CONTRACT COMPLETE): *"PROHIBITED: annotation dropout at any anchor site listed in this inventory — \*prevents handoff-boundary gap: an annotation absent from its anchor site is detectable only by full body scan; this clause converts dropout into a FORMAT CONTRACT violation identifiable by anchor-ID lookup at this inventory without traversing the body\*"*

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **C-38** | **PASS** | Count declared in Section C header before table: "declares 7 required annotations" + "expected rows = 7" — count-scan is the verification method; row count < 7 = detectable gap |
| **C-39** | **PASS** | Both canonical sentences present. Sentence 1: closure + negation ("not listed here does not exist as a contract requirement"). Sentence 2: bidirectional confirmation ("listed here that is absent... is a FORMAT CONTRACT violation"). Full bidirectional constraint encoded |
| **C-40** | **PASS** | PROHIBITED clause physically located inside Section C (after table rows, before FORMAT CONTRACT COMPLETE — within the annotation inventory's closure logic). Inline failure-mode annotation names the specific failure mode: "handoff-boundary gap" and "detectable only by full body scan" — both failure modes precisely identified |

**C-01–C-05 (essential):** All PASS.
**C-06–C-37:** All PASS — identical to R14.

**V-02 composite:** 235 (carry) + 5 (C-38) + 5 (C-39) + 5 (C-40) = **250/250**

---

### V-03 — Lifecycle Emphasis: PROHIBITED in named sub-block before FORMAT CONTRACT COMPLETE

**Section C structure in V-03:**

- Header: *"This section declares 7 required annotations. Completeness is count-verifiable: expected rows = 7."*
- Closure (after table): *"This inventory is closed. An annotation not listed here does not exist as a contract requirement. An annotation listed here that is absent from its anchor site in the body is a FORMAT CONTRACT violation."*
- **ANNOTATION DROPOUT PROHIBITION** — a named sub-block positioned AFTER Section C ends, BEFORE FORMAT CONTRACT COMPLETE: *"PROHIBITED: omitting any annotation from the anchor site declared in Section C — \*prevents silent precision-site gap...\*"*

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **C-38** | **PASS** | Count declared at Section C header: "declares 7 required annotations" + "expected rows = 7" |
| **C-39** | **PASS** | Canonical two-sentence closure present within Section C: bidirectional constraint on both absence-from-inventory and absence-from-anchor-site |
| **C-40** | **FAIL** | PROHIBITED clause is NOT co-located inside Section C (the annotation inventory). The ANNOTATION DROPOUT PROHIBITION sub-block is a sibling block at FORMAT CONTRACT level — structurally parallel to Section A, Section B, Section C — not contained within Section C. C-40 requires the inventory itself to include the PROHIBITED clause ("extends... into the annotation inventory itself"). The phrase "annotation inventory includes a PROHIBITED clause" forecloses placement outside the inventory block. V-03 tests the co-location question and fails on the strict reading |

**C-01–C-05 (essential):** All PASS.
**C-06–C-37:** All PASS — identical to R14.

**V-03 composite:** 235 (carry) + 5 (C-38) + 5 (C-39) + 0 (C-40) = **245/250**

*Note: V-03 establishes that "annotation inventory includes" requires physical co-location inside Section C. The ANNOTATION DROPOUT PROHIBITION sub-block pattern fails C-40 because it is a FORMAT CONTRACT level element, not an annotation inventory element. This resolves the co-location question: the PROHIBITED clause must appear between the annotation table rows and the closure sentence, not in a sibling block.*

---

### V-04 — Role Sequence + Phrasing Register: all three in Section C; count verification at Role 2 activation

**Section C structure in V-04:**

- Header: *"This section declares 7 required annotations. Count-scan verification: expected rows = 7; a row count below 7 is a completeness gap detectable without reading annotation content. Role 2 activation confirms this count before Phase 1 opens."*
- Closure + PROHIBITED: identical to V-02 (both sentences + PROHIBITED with inline annotation, co-located in Section C)

**Role 2 PHASE 1 ENTRY CONDITION adds annotation count check:**
Annotation inventory count check — confirm Section C row count = 7 before Phase 1 opens. If count < 7: FORMAT CONTRACT COMPLETE stated prematurely; return to Role 1.

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **C-38** | **PASS** | Count declared at Section C header with count-scan verification framing; additionally surfaced at Role 2 activation as an explicit entry condition — strengthens count-scan verifiability to two enforcement points |
| **C-39** | **PASS** | Canonical two-sentence closure in Section C — identical to V-02 |
| **C-40** | **PASS** | PROHIBITED clause co-located in Section C with inline failure-mode annotation — identical placement and form as V-02 |
| **C-36 delta** | PASS (unchanged) | Role 3 activation conditions retain 5 observables from R14. Role 2's Phase 1 entry condition adds a 6th annotation-count check, but this is a Role 2 entry condition, not a Role 3 activation condition. C-36 covers role-activation observable counts and already PASS in R14; the annotation count at Role 2 is additive, not disqualifying |

**C-01–C-05 (essential):** All PASS.
**C-06–C-37:** All PASS — identical to R14 (Role 2 entry condition addition does not conflict with any prior criteria).

**V-04 composite:** 235 (carry) + 5 (C-38) + 5 (C-39) + 5 (C-40) = **250/250**

---

### V-05 — All Three Axes: count + per-row tokens + closure + PROHIBITED before table; activation count; ANNOTATION SCAN GATE

**Section C structure in V-05:**

- Header: count declaration + Role 2 confirmation note
- PROHIBITED (before table): *"PROHIBITED: annotation dropout at any anchor site in this inventory — \*prevents handoff-boundary gap...\*"* (co-located in Section C, preceding the table)
- Annotation table: 7 rows with added `Dropout-prohibited?` column (per-row: YES + per-annotation inline failure-mode token)
- Closure (after table): canonical two-sentence form

**Role 2 PHASE 1 ENTRY CONDITION:** annotation count check (count = 7 required).

**ANNOTATION SCAN GATE:** positioned between TYPE SCAN GATE and TABLE F. 7 scan lines (one per Annot-ID), PROCEED/BLOCKED decision. Purpose annotation with 3 fields (failure mode prevented / gap above Section C PROHIBITED clause / 7-observable audit test). Role 3 activation conditions updated to require PROCEED at both TYPE SCAN GATE and ANNOTATION SCAN GATE (7 observables total at Role 3 boundary).

| Criterion | Status | Evidence |
|-----------|--------|----------|
| **C-38** | **PASS** | Count declared at Section C header before enumeration. Additionally: per-row Dropout-prohibited? column provides a per-entry count signal. At minimum, the header-level count satisfies C-38; the per-row column is additive structural depth |
| **C-39** | **PASS** | Canonical two-sentence closure after the table: "This inventory is closed. An annotation not listed here does not exist as a contract requirement. An annotation listed here that is absent from its anchor site in the body is a FORMAT CONTRACT violation." |
| **C-40** | **PASS** | PROHIBITED clause is co-located in Section C (physically before the annotation table), with inline failure-mode annotation naming "handoff-boundary gap" and the body-scan-only detection problem. Co-location is intra-Section C; PROHIBITED appears as part of the inventory's entry conditions. Stronger placement than V-02 (pre-table vs post-table), fully satisfying "annotation inventory includes a PROHIBITED clause" |

**ANNOTATION SCAN GATE — excess-of-rubric analysis:**

The ANNOTATION SCAN GATE is not tested by any existing criterion (C-01–C-40). It introduces:
- A second construction-time gate between TYPE SCAN GATE and TABLE F
- Purpose annotation (3 fields, parallel to TYPE SCAN GATE's C-26 form)
- 7-observable audit test (parallel to TYPE SCAN GATE's 5-observable audit test, extended to annotation coverage)
- Role 3 activation conditions updated from 5 observables to 7 (adds ANNOTATION SCAN GATE PROCEED + 7 Annot-NN scan lines)

Under v15 rubric, this does not earn additional points (no criterion covers it), but it is a structural pattern that no prior variation has produced at this specificity. This is the C-41 seed.

**C-01–C-05 (essential):** All PASS — structural tables and phase sequence unchanged.
**C-06–C-37:** All PASS — TYPE SCAN GATE unchanged; ANNOTATION SCAN GATE is additive, not a replacement.

**V-05 composite:** 235 (carry) + 5 (C-38) + 5 (C-39) + 5 (C-40) = **250/250**

---

## Ranking

| Rank | Variation | C-38 | C-39 | C-40 | Composite | Predicted | Delta |
|------|-----------|------|------|------|-----------|-----------|-------|
| **1** | **V-05** | PASS | PASS | PASS | **250/250** | 250/250 | +0 |
| **1** | **V-02** | PASS | PASS | PASS | **250/250** | 250/250 | +0 |
| **1** | **V-04** | PASS | PASS | PASS | **250/250** | 250/250 | +0 |
| **4** | V-01 | PASS | PASS | FAIL | 245/250 | 245/250 | +0 |
| **4** | V-03 | PASS | PASS | FAIL | 245/250 | 245/250 | +0 |

All predictions confirmed. No surprises.

**Tiebreaker — structural depth at 250:**

V-05 > V-04 > V-02 on structural depth:
- V-02: minimal path — all three criteria satisfied with one-line additions
- V-04: V-02 + annotation count at Role 2 activation entry condition
- V-05: V-04 + per-row Dropout-prohibited? column + ANNOTATION SCAN GATE + updated Role 3 activation conditions (7 observables)

V-05 is the excellence candidate.

---

## Excellence Signals

**From V-05 (top structural depth at 250/250):**

**Signal 1 — Annotation scan gate as construction-time blocking condition.**
V-05 introduces the ANNOTATION SCAN GATE between TYPE SCAN GATE and TABLE F. The gate has a purpose annotation (3 fields), 7 scan lines (one per Annot-ID), and a PROCEED/BLOCKED decision. This parallels the TYPE SCAN GATE structure exactly: TYPE SCAN GATE blocks on missing risk categories; ANNOTATION SCAN GATE blocks on annotation dropout before the mitigation registry opens. The gap above the Section C PROHIBITED clause is precisely stated: the clause is a contract declaration; the gate is construction-time enforcement. An annotation-absent output cannot be produced by any valid execution path that passes the gate.

**Signal 2 — Per-row dropout prohibition token in annotation inventory.**
V-05 adds a `Dropout-prohibited?` column to the annotation table. Each row carries `YES — *omitting this annotation makes [failure-mode] undetectable at [anchor] without body scan*`. This converts each annotation row from an enumeration entry (passive: here is what is required) into a named enforcement commitment (active: here is what dropout causes at this specific anchor). The column makes per-annotation dropout consequences inspectable by row-scan rather than by returning to the PROHIBITED clause. It extends the prohibition-plus-annotation pattern from inventory-level to per-entry level.

**Signal 3 — PROHIBITED clause before enumeration (V-05) vs after (V-02).**
V-02 places the PROHIBITED clause after the table rows and before the closure sentence. V-05 places it before the table, making the prohibition the entry condition for enumeration rather than the exit condition. This means a reader encounters the dropout prohibition before processing any annotation row — the failure mode is declared before the list is consumed, not after. For C-40 scoring, both placements pass (both are co-located in Section C with inline annotation); V-05's pre-table placement is structurally stronger as an entry declaration.

**C-40 co-location verdict from V-03:**
V-03's ANNOTATION DROPOUT PROHIBITION sub-block (a FORMAT CONTRACT level sibling to Section A/B/C) fails C-40. This establishes that "annotation inventory includes" requires physical co-location inside Section C's block boundary. A named sub-block at FORMAT CONTRACT close — even if positioned immediately after Section C — is not "in the annotation inventory." Round 15 is definitively resolved: the PROHIBITED clause must appear between Section C's opening declaration and its closure sentence.

---

## New Patterns

**Pattern 1 — Annotation scan gate positioned between TYPE SCAN GATE and TABLE F.**
A second construction-time gate with 7 scan lines (one per declared annotation), purpose annotation naming the gap above the Section C PROHIBITED clause, and a PROCEED/BLOCKED decision. Makes annotation dropout a pre-TABLE-F blocking condition parallel to TYPE SCAN GATE's category-elision blocking. Seeds C-41: "annotation scan gate as construction-time enforcement with observable count verification."

**Pattern 2 — Per-row dropout prohibition column in annotation inventory.**
A `Dropout-prohibited?` column with per-annotation YES tokens and inline body-scan-avoidance rationale. Extends the inventory-level PROHIBITED clause to per-entry enforcement, making each annotation's dropout consequence inspectable by row without cross-referencing the inventory-level clause. Strengthens C-40 at maximum per-entry specificity.

---

```json
{"top_score": 250, "all_essential_pass": true, "new_patterns": ["Annotation scan gate between TYPE SCAN GATE and TABLE F — 7-observable construction-time blocking condition for annotation dropout, parallel to TYPE SCAN GATE category-elision blocking; purpose annotation names gap above Section C PROHIBITED clause; seeds C-41", "Per-row Dropout-prohibited? column in annotation inventory — extends inventory-level prohibition to per-entry enforcement with inline body-scan-avoidance rationale per annotation row"]}
```
