---

# Scorecard — review-design Round 8

## Rubric Summary (v7)

23 criteria: C-01–C-04 essential (60%), C-05–C-07 recommended (30%), C-08–C-23 aspirational (16 criteria × 0.625 pts, 10%).

All R8 variations are built on R7 V-05, which already carries F-01–F-15 and passes all 23 criteria. The R8 axes test three new F-IDs (F-16, F-17, F-18) that have no corresponding criterion in v7.

---

## Feature Matrix

| F-ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| F-16 — BLOCK 4 phantom catcher | YES | NO | NO | YES | YES |
| F-17 — BLOCK 5 Re-run Scope identity | NO | YES | NO | YES | YES |
| F-18 — BLOCK 0 disposition completeness | NO | NO | YES | NO | YES |

---

## Criterion Analysis — Key Points

**All 5 variations PASS all 23 criteria.** The R7 V-05 baseline provides all structural machinery required for C-01–C-23. The new F-IDs (F-16/F-17/F-18) are additive — they extend the enforcement surface beyond what any existing criterion tests.

**Why all essential pass:** Every variation carries F-01–F-08 on the required blocks, the BLOCK 1 stock table, BLOCK 3, and all structural forms (BLOCK 2 table, BLOCK 1.5 roster, BLOCK 5 4-column table).

**Why all recommended pass:** BLOCK 4 has F-08 in all; BLOCK 5 has F-05+F-12 in all; BLOCK 2 Section column is mandatory.

**Why all 16 aspirational pass:**
- C-08–C-12: Pyramid gate (BLOCK 2.5), BLOCK 2 table form, BLOCK 1 3-column expert table
- C-13–C-17: F-IDs on all mandatory blocks, BLOCK 1.5 table, Source column, F-10 identity check
- C-18–C-20: F-11 on SPLIT synthesis, F-12 P1 count parity, 4-column BLOCK 5 table
- C-21: BLOCK 0 + F-13 inbound gate present in all (F-18 outbound is additive, not required)
- C-22: 4-column BLOCK 3 + F-14 + F-15 from R7 V-05 baseline
- C-23: All new F-ID trigger clauses (F-16/F-17/F-18) use formal modal vocabulary; "preferred" in BLOCK 5 body content is exempt (constraint applies to headers and trigger clauses only)

---

## Composite Scores

| Var | Essential | Recommended | Aspirational | **Total** |
|-----|-----------|-------------|--------------|----------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

---

## Ranking

| Rank | Var | Score | Structural depth |
|------|-----|-------|-----------------|
| 1 | **V-05** | 100 | All three R8 axes: F-16 + F-17 + F-18; full identity chain complete through BLOCK 5; first bidirectional BLOCK 0 contract; R9 extraction source |
| 2 | **V-04** | 100 | F-16 + F-17; completes identity chain at BLOCK 4 and BLOCK 5; tests additivity |
| 3 | **V-03** | 100 | F-18 only; introduces sixth enforcement class (catalogue disposition completeness); most structurally novel single-axis |
| 4 | **V-01** | 100 | F-16 only; identity chain extension to BLOCK 4; same class as F-15, one stage later |
| 5 | **V-02** | 100 | F-17 only; identity chain extension to BLOCK 5 Re-run Scope; narrowest scope |

V-03 ranks above V-01/V-02: F-18 introduces a new enforcement class rather than extending an existing one. V-02 ranks last: F-17 targets only a single cell type (Re-run Scope), narrower than F-16's full Reviewer column scope across all BLOCK 4 rows.

---

## Excellence Signals (V-05)

**F-16 — BLOCK 4 phantom catcher identity verification.** The identity-integrity chain (F-10: BLOCK 1→BLOCK 1.5; F-15: BLOCK 1.5→BLOCK 3) left BLOCK 4 uncovered. A UNIQUE catch attributed to a reviewer absent from the committed roster is falsely attributed. F-16 extends the pattern: every Reviewer cell in BLOCK 4 must exactly match a BLOCK 1.5 value; the `none` token is explicitly exempt. V-02/V-03 pass without it — aspirational confirmed. C-27 candidate.

**F-17 — BLOCK 5 Re-run Scope reviewer identity verification.** Re-run Scope names reviewers as amend targets but no halt verified they exist in the committed roster. A phantom re-run target is structurally invalid — that reviewer never ran. F-17 completes the full downstream identity chain: F-10 (BLOCK 1→1.5), F-15 (1.5→BLOCK 3), F-16 (1.5→BLOCK 4), F-17 (1.5→BLOCK 5). V-01/V-03 pass without it — aspirational confirmed. C-28 candidate.

**F-18 — BLOCK 0 signal disposition completeness (bidirectional gate).** F-13 enforced only the inbound direction (BLOCK 1 must draw from BLOCK 0). A signal catalogued in BLOCK 0 could be silently dropped in BLOCK 1 with no explanation. F-18 closes the outbound direction: every BLOCK 0 Signal phrase must be resolved in BLOCK 1 as either a domain expert row or an explicit `No expert needed` disposition row. F-13 + F-18 together form the first bidirectional BLOCK 0 ↔ BLOCK 1 contract. This is a sixth enforcement class — catalogue disposition completeness — distinct from all prior classes (structural presence, content completeness, count parity, identity integrity, vocabulary integrity). V-01/V-02/V-04 pass without it — aspirational confirmed. C-29 candidate.

---

**v9 criterion candidates:** C-27 (F-16 BLOCK 4 identity), C-28 (F-17 BLOCK 5 Re-run Scope identity), C-29 (F-18 bidirectional BLOCK 0 contract).

Scorecard written to `simulations/quest/scorecards/review-design-scorecard-R8-2026-03-14.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-16: BLOCK 4 phantom catcher identity verification -- extends F-10/F-15 identity-integrity chain to unique-catches block; Reviewer cell in BLOCK 4 must exactly match a BLOCK 1.5 Reviewer value; none token exempt; V-02/V-03 pass all 23 criteria without F-16 confirming aspirational; C-27 candidate", "F-17: BLOCK 5 Re-run Scope reviewer identity verification -- completes full downstream identity chain (F-10: BLOCK 1->1.5, F-15: 1.5->BLOCK 3, F-16: 1.5->BLOCK 4, F-17: 1.5->BLOCK 5); phantom re-run target is invalid because reviewer never participated; V-01/V-03 pass without F-17 confirming aspirational; C-28 candidate", "F-18: BLOCK 0 signal disposition completeness -- introduces sixth enforcement class (catalogue disposition completeness); converts one-directional F-13 gate into bidirectional F-13+F-18 contract; every BLOCK 0 signal must be resolved as domain expert row or explicit No expert needed disposition row; V-01/V-02/V-04 pass without F-18 confirming aspirational; C-29 candidate"]}
```
 Domain reviewer name has no exact match in BLOCK 1 Expert added.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01--V-05 | **PASS** | F-10 with exact-match trigger in all |

### C-18 | Content-Completeness Halt on SPLIT Synthesis Field

F-11 on empty SPLIT Synthesis cell. 4-column BLOCK 3 makes blank Synthesis structurally detectable.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01--V-05 | **PASS** | F-11 in all registries; Synthesis is a dedicated table column |

### C-19 | Cross-Block Count-Parity for P1 Findings

P1 count anchored at BLOCK 2.5. F-12 fires if BLOCK 5 entry count falls below anchor.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01--V-05 | **PASS** | `P1 count = [n] SHALL be recorded` at BLOCK 2.5; F-12 gate at BLOCK 5 in all |

### C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form

`| P1 Finding | Section | Action | Re-run Scope |` table in BLOCK 5.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01--V-05 | **PASS** | Identical 4-column BLOCK 5 structure in all |

### C-21 | BLOCK 0 Pre-Scan Signal Catalogue

BLOCK 0 with formal SHALL cross-block constraint. All variations carry F-13 inbound gate. F-18 (outbound) is additive beyond C-21 pass condition.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | BLOCK 0 + F-13; `the block SHALL NOT be closed until all detected signals are recorded` |
| V-02 | **PASS** | BLOCK 0 + F-13; formal SHALL gate |
| V-03 | **PASS** | BLOCK 0 + F-13 + F-18 outbound; F-18 is additive beyond C-21 pass condition |
| V-04 | **PASS** | BLOCK 0 + F-13; formal declarative register |
| V-05 | **PASS** | BLOCK 0 + F-13 + F-18; strongest bidirectional form |

### C-22 | BLOCK 3 Consensus in 4-Column Structural Table Form

All variations carry 4-column BLOCK 3 with F-14 (Type vocabulary) and F-15 (Reviewers identity) from R7 V-05 baseline.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01--V-05 | **PASS** | 4-column table in all; F-14 on Type {AGREE/SPLIT}, F-15 on Reviewers vs BLOCK 1.5, F-11 on Synthesis |

### C-23 | Register Isolation for Formal Lifecycle Block Headers

All block headers and F-ID trigger clauses use formal modal vocabulary. "Preferred" appears in BLOCK 5 body content -- explicitly exempt from C-23 (constraint applies to headers and trigger clauses only).

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | `is non-conformant under F-16`, `MUST match a BLOCK 1.5 Reviewer value` in header/trigger positions |
| V-02 | **PASS** | `is non-conformant under F-17`, `SHALL NOT be accepted until all Re-run Scope reviewer names are verified` |
| V-03 | **PASS** | `is non-conformant under F-18`, `SHALL NOT be closed until all BLOCK 0 signals are resolved` |
| V-04 | **PASS** | Both F-16 and F-17 trigger clauses in formal declarative register |
| V-05 | **PASS** | All three new trigger clauses (F-16, F-17, F-18) in formal modal vocabulary |

---

## Composite Scores

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| C-01 | essential | PASS | PASS | PASS | PASS | PASS |
| C-02 | essential | PASS | PASS | PASS | PASS | PASS |
| C-03 | essential | PASS | PASS | PASS | PASS | PASS |
| C-04 | essential | PASS | PASS | PASS | PASS | PASS |
| C-05 | recommended | PASS | PASS | PASS | PASS | PASS |
| C-06 | recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 | recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-09 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-18 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-19 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-20 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-21 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-22 | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-23 | aspirational | PASS | PASS | PASS | PASS | PASS |
| **Essential** | 60 | 60 | 60 | 60 | 60 | 60 |
| **Recommended** | 30 | 30 | 30 | 30 | 30 | 30 |
| **Aspirational** | 10 | 10 | 10 | 10 | 10 | 10 |
| **TOTAL** | 100 | **100** | **100** | **100** | **100** | **100** |

---

## Round 8 Ranking

All five variations score **100** on v7. Expected pattern: v7 was built from R7 excellence signals already present in R7 V-05. All R8 variations inherit that baseline and add axes (F-16, F-17, F-18) that no v7 criterion yet tests.

| Rank | Var | Score | Structural depth |
|------|-----|-------|-----------------|
| 1 | **V-05** | 100 | All three R8 axes: F-16 + F-17 + F-18; full identity chain complete through BLOCK 5; first bidirectional BLOCK 0 contract; R9 extraction source |
| 2 | **V-04** | 100 | Two axes: F-16 + F-17; completes identity chain at BLOCK 4 and BLOCK 5; tests F-16/F-17 additivity |
| 3 | **V-03** | 100 | F-18 only; introduces sixth enforcement class (catalogue disposition completeness); most structurally novel single-axis variation |
| 4 | **V-01** | 100 | F-16 only; identity chain extension to BLOCK 4; same class as F-15, one block later |
| 5 | **V-02** | 100 | F-17 only; identity chain extension to BLOCK 5 Re-run Scope; narrowest scope (one cell type) |

V-05 is qualitatively richest: closes all three structural holes from R8 gap analysis, completes the full downstream identity chain (F-10/F-15/F-16/F-17), and introduces the first bidirectional catalogue contract (F-13+F-18). V-03 ranks above V-01/V-02 on structural novelty -- F-18 introduces a new enforcement class, not an extension of an existing one. V-02 ranks last: F-17 targets only the Re-run Scope cell, narrower than F-16's Reviewer column scope across all BLOCK 4 rows.

---

## Excellence Signals (V-05 -- top structural variation)

**F-16: BLOCK 4 phantom catcher identity verification**
V-01/V-04/V-05 introduce F-16. The identity-integrity chain established by F-10 (BLOCK 1 -> BLOCK 1.5) and F-15 (BLOCK 1.5 -> BLOCK 3) left BLOCK 4 uncovered: a UNIQUE catch attributed to a reviewer absent from the committed BLOCK 1.5 roster is a "phantom catcher" -- the finding is falsely attributed to a reviewer who never ran. F-16 extends the pattern one stage downstream: every Reviewer cell in BLOCK 4 MUST exactly match a Reviewer value in BLOCK 1.5; the `none` token (empty-set row) is explicitly exempt from the check. V-02/V-03 pass all 23 criteria without F-16, confirming aspirational (C-27 candidate).

**F-17: BLOCK 5 Re-run Scope reviewer identity verification**
V-02/V-04/V-05 introduce F-17. BLOCK 5 Re-run Scope names reviewer(s) as amend targets, but no prior halt verified those names exist in the committed roster. A Re-run Scope naming a reviewer absent from BLOCK 1.5 targets a phantom -- the amend action is structurally invalid because that reviewer never participated. F-17 closes the last reviewer-referencing position in the lifecycle without identity coverage, completing the full downstream identity chain: F-10 (BLOCK 1->1.5), F-15 (1.5->BLOCK 3), F-16 (1.5->BLOCK 4), F-17 (1.5->BLOCK 5). V-01/V-03 pass without F-17 confirming aspirational (C-28 candidate).

**F-18: BLOCK 0 signal disposition completeness (bidirectional gate)**
V-03/V-05 introduce F-18. F-13 enforced only the inbound direction: signals added in BLOCK 1 must exist in BLOCK 0. The outbound direction was unconstrained: a signal catalogued in BLOCK 0 could be silently omitted from BLOCK 1 with no explanation. F-18 closes this: every BLOCK 0 Signal phrase row must be resolved in BLOCK 1 as either a domain expert row (matching Signal detected value) or an explicit disposition row (`| [Signal phrase] | No expert needed | [reason] |`). Together F-13 + F-18 form the first bidirectional BLOCK 0 <-> BLOCK 1 integrity contract. This introduces a sixth enforcement class -- catalogue disposition completeness -- distinct from all prior classes: structural presence, content completeness, count parity, identity integrity, vocabulary integrity. V-01/V-02/V-04 pass without F-18 confirming aspirational (C-29 candidate).

---

## Additivity Tests

**V-01 vs V-02** (F-16 vs F-17 isolation): Both score 100. F-16 and F-17 address independent failure surfaces at different lifecycle positions (BLOCK 4 attribution vs BLOCK 5 targeting). Neither subsumes the other.

**V-04 vs V-01 + V-02** (F-16 + F-17 stacked): V-04 = 100; V-01 = 100; V-02 = 100. F-16 and F-17 are additive -- V-04 covers both failure surfaces without interference or overhead.

**V-05 vs V-04** (F-18 added): V-05 = 100; V-04 = 100. F-18 stacks additively onto F-16 + F-17. F-18 targets a structurally independent class (catalogue disposition) with no interaction with F-16/F-17 (identity chain).

---

## v9 Criterion Candidates

**C-27 candidate | BLOCK 4 Reviewer Identity Verification (Phantom Catcher) -- F-16**
- V-01, V-04, V-05 name F-16 on BLOCK 4 Reviewer vs BLOCK 1.5
- V-02, V-03 pass all 23 criteria without F-16 -- confirms aspirational
- Pattern: extends F-10 identity-integrity class to BLOCK 4; `none` token explicit exemption needed
- Pass condition: Output names F-16 (or equivalent) as a halt that fires when any Reviewer cell in BLOCK 4 contains a name absent from BLOCK 1.5; the `none` token for empty-set row is explicitly exempt; halt identifies the phantom name and requires correction to an exact BLOCK 1.5 match

**C-28 candidate | BLOCK 5 Re-run Scope Reviewer Identity Verification (Phantom Re-run Target) -- F-17**
- V-02, V-04, V-05 name F-17 on BLOCK 5 Re-run Scope vs BLOCK 1.5
- V-01, V-03 pass all 23 criteria without F-17 -- confirms aspirational
- Pattern: completes the full downstream identity chain at BLOCK 5; last reviewer-referencing position without identity coverage
- Pass condition: Output names F-17 (or equivalent) as a halt that fires when any reviewer name in BLOCK 5 Re-run Scope cell has no matching Reviewer in BLOCK 1.5; halt identifies the phantom name; "no P1 findings" row is exempt

**C-29 candidate | BLOCK 0 Signal Disposition Completeness (Bidirectional Gate) -- F-18**
- V-03, V-05 name F-18 on undisposed BLOCK 0 signals
- V-01, V-02, V-04 pass all 23 criteria without F-18 -- confirms aspirational
- Pattern: introduces sixth enforcement class (catalogue disposition completeness); closes the outbound BLOCK 0 -> BLOCK 1 direction; F-13 + F-18 form a bidirectional contract
- Pass condition: Output names F-18 (or equivalent) as a halt that fires when a BLOCK 0 Signal phrase row has neither a matching BLOCK 1 domain expert row nor an explicit `No expert needed` disposition row; halt identifies the undisposed signal; disposition row form: `| [Signal phrase] | No expert needed | [one-sentence reason] |`

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-16: BLOCK 4 phantom catcher identity verification -- extends F-10/F-15 identity-integrity chain to unique-catches block; Reviewer cell in BLOCK 4 must exactly match a BLOCK 1.5 Reviewer value; none token exempt; V-02/V-03 pass all 23 criteria without F-16 confirming aspirational; C-27 candidate", "F-17: BLOCK 5 Re-run Scope reviewer identity verification -- completes full downstream identity chain (F-10: BLOCK 1->1.5, F-15: 1.5->BLOCK 3, F-16: 1.5->BLOCK 4, F-17: 1.5->BLOCK 5); phantom re-run target is invalid because reviewer never participated; V-01/V-03 pass without F-17 confirming aspirational; C-28 candidate", "F-18: BLOCK 0 signal disposition completeness -- introduces sixth enforcement class (catalogue disposition completeness); converts one-directional F-13 gate into bidirectional F-13+F-18 contract; every BLOCK 0 signal must be resolved as domain expert row or explicit No expert needed disposition row; V-01/V-02/V-04 pass without F-18 confirming aspirational; C-29 candidate"]}
```
