**R12 scoring complete.**

---

## Leaderboard

| Rank | Variation | Score | Essential |
|------|-----------|-------|-----------|
| 1 | V-04 | **69.50** | 5/5 |
| 1 | V-05 | **69.50** | 5/5 |
| 3 | V-01 | 69.17 | 5/5 |
| 3 | V-02 | 69.17 | 5/5 |
| 5 | V-03 | 68.83 | 5/5 |

Golden threshold: 80. Gap: ~10.5 pts.

---

## What happened

**The three new criteria (C-36, C-37, C-38) all PASS across all five variations.** Target achieved. But the composite scores are lower than R11 V-05 because R12 dropped the explicit IA Phase B — the cost ledger, budget verdict, net direction, seal token, C1 RESULT pre-flight, and dual C1/C2 Phase C entry. That regression accounts for ~15 failing aspirational criteria that R11 V-05 passed.

**V-04/V-05 win by satisfying both C-10 (GO WITH CONDITIONS resolution owner) and C-30 (PRE-COMMITMENT named in Phase C exit checklist).** V-01 passes C-30 but misses C-10. V-02 passes C-10 but misses C-30. V-03 misses both.

**One new pattern extracted** — Phase C exit conditions as a numbered table (`# | Compliance Item | Verified?`) rather than prose/checkbox list. V-04/V-05 use this; it makes each condition findable by row number. Candidate for C-39.

---

## R13 Direction

Take R11 V-05 as the base (full IA Phase B intact) and integrate the R12 wins into it:
- C-36: add READ RECEIPT ordering to Phase C/D exit condition table
- C-37: replace prose C2 block with (a)–(e) PRESENT/ABSENT table
- C-38: add `[IA-VERDICT: ...] | [ROLE-MECHANISM: ...]` slot labels to F-01 template
- C-10: add resolution-owner column to GO WITH CONDITIONS output
- C-39 candidate: convert Phase C exit checklist to numbered table

```json
{"top_score": 69.50, "all_essential_pass": true, "new_patterns": ["Phase C exit conditions expressed as a numbered table (# | Compliance Item | Verified?) rather than a prose or checkbox list — each condition independently findable by row number without prose parsing; not captured by C-30 or C-36 which only require naming, not table structure"]}
```
t

#### PASS across all five variations

| ID | Evidence |
|----|---------|
| C-14 | F-01 IA-RESPONSE finding in every role section names IA verdict as counterpoint — [IA-VERDICT] slot present in Description template |
| C-15 | Domain-lens binary test + revise + drop present in all; C-05 at template level |
| C-27 | B1/PRE-COMMITMENT structurally precedes B4/Findings in all variations; "produce before accessing IA document" |
| C-31 | [IA-VERDICT] in F-01 Description is within the finding body text, not a standalone section anchor |
| C-33 | C2 RESULT explicitly checks receipt fields (a)–(e) present/absent — not Phase B ledger content. All: "C2 does NOT re-check Phase B content" or equivalent |
| C-34 | F-01 designated as type IA-RESPONSE in findings template in all variations; Type column or type-label present |
| C-35 | All enforce READ RECEIPT (B2) before C2 RESULT (B3) in document order with explicit enforcement language |
| C-36 | All name READ RECEIPT-before-C2-RESULT ordering in Phase C / Block 3 / Section 3 compliance check as a named compliance item |
| C-37 | All enumerate fields (a)–(e) in C2 RESULT with per-field PRESENT/ABSENT verdict; explicit "do not collapse to summary" |
| C-38 | All declare F-01 Description as [IA-VERDICT: ...] \| [ROLE-MECHANISM: ...] named schema slots visible in template |

#### PARTIAL across all five variations

| ID | Evidence |
|----|---------|
| C-18 | All have named phase gates with exit conditions. Missing: (c) which rubric criteria each phase gates; domain-lens is a per-finding inline check within B4, not the Phase B4 exit condition |
| C-23 | Receipt block structurally precedes findings in all. Missing: C-23's specific required fields (Budget verdict, Budget strength, cost row, initial position) — R12 receipt fields differ (IA reference / Cost framing / Evidence basis / Recommended action / Confidence qualifier) |
| C-26 | C2 RESULT output line present in B3 for all. Missing: C1 RESULT output line (pre-flight Phase B checklist) — the C1/C2 dual structure from R11 is absent; R12 puts C2 inline in Phase B with no C1 |

#### FAIL across all five variations

| ID | Reason |
|----|--------|
| C-09 | Consensus sections require "characterize tension" or "because: ..." but none mandate naming the structural/architectural mechanism as WHY; passes C-03 but fails C-09 |
| C-11 | No explicit IA Phase B output section — the IA is an external document, not a selected reviewer with their own section sequenced first |
| C-12 | No requirement to name architectural mechanism in divergence explanations — not a requirement in any variation's consensus template |
| C-13 | No enumerated ban list of >= 3 prohibited perspective-label phrases |
| C-16 | AMEND handling mentions "AMEND-specified" reason only — no structured output block with named fields (a) what amended (b) roles changed (c) superseded findings |
| C-17 | No IA Phase B section — IA cost framing as budget authority with explicit cost terms is absent |
| C-19 | No IA cost ledger with named-row x named-column schema |
| C-20 | No IA Phase B to reference as technical phase entry condition |
| C-21 | No net direction column; no cost ledger present |
| C-22 | R12 puts C2 RESULT inline in Phase B (B3). No dual C1/C2 sub-conditions declared as Phase C entry structure |
| C-24 | Findings tables have ID/Type/Severity/Description/Evidence columns — no Domain-Lens column showing gate compliance per finding |
| C-25 | No budget verdict; no three-clause WORSE/BETTER/Conclusion formula |
| C-28 | No three-clause formula; no per-line output structure requirement |
| C-29 | No [PRE-COMMITMENT SEALED] token or equivalent seal closing the PRE-COMMITMENT block |
| C-32 | R12 READ RECEIPT fields (d)/(e) are "Recommended action"/"Confidence qualifier" — not cost row / initial position; no cross-reference to PRE-COMMITMENT for those fields |

#### Differentiating criteria

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-10 | FAIL | PASS | FAIL | PASS | PASS | V-02: "resolution owner" in Block 4. V-04/V-05: "named resolution owner" + separate row. V-01/V-03: no conditions detail in Phase D |
| C-30 | PASS | FAIL | FAIL | PASS | PASS | V-01: checklist has "☐ PRE-COMMITMENT appears before READ RECEIPT for every role." V-04/V-05: table row 2 = "B1 PRE-COMMITMENT precedes B2 READ RECEIPT." V-02: Block 3 check omits PRE-COMMITMENT presence. V-03: pre-advance check omits PRE-COMMITMENT |

---

## Composite Score Calculation

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|-----------|---------------|-----------------|-------------------|-----------|
| V-01 | 60 | 5 | 4.17 (11P×0.333 + 3Pr×0.167) | **69.17** |
| V-02 | 60 | 5 | 4.17 (11P×0.333 + 3Pr×0.167) | **69.17** |
| V-03 | 60 | 5 | 3.83 (10P×0.333 + 3Pr×0.167) | **68.83** |
| V-04 | 60 | 5 | 4.50 (12P×0.333 + 3Pr×0.167) | **69.50** |
| V-05 | 60 | 5 | 4.50 (12P×0.333 + 3Pr×0.167) | **69.50** |

Aspirational pass counts:
- Shared PASS: C-14, C-15, C-27, C-31, C-33, C-34, C-35, C-36, C-37, C-38 = 10
- Shared PARTIAL: C-18, C-23, C-26 = 3
- Shared FAIL: C-09, C-11, C-12, C-13, C-16, C-17, C-19, C-20, C-21, C-22, C-24, C-25, C-28, C-29, C-32 = 15
- V-01: + C-30 PASS → 11P, 3Pr, 16F
- V-02: + C-10 PASS → 11P, 3Pr, 16F
- V-03: no add → 10P, 3Pr, 17F
- V-04: + C-10 PASS + C-30 PASS → 12P, 3Pr, 15F
- V-05: + C-10 PASS + C-30 PASS → 12P, 3Pr, 15F

---

## Leaderboard

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | **V-04** | 69.50 | YES | Lifecycle + Format; table exit conditions; C-10 + C-30 PASS |
| 1 | **V-05** | 69.50 | YES | Lifecycle + Format + Register; same score, stronger enforcement language |
| 3 | V-01 | 69.17 | YES | Lifecycle emphasis; C-30 PASS but C-10 FAIL |
| 3 | V-02 | 69.17 | YES | Output format (tables); C-10 PASS but C-30 FAIL |
| 5 | V-03 | 68.83 | YES | Phrasing register; neither C-10 nor C-30 PASS |

**Golden threshold**: 80. No variation reaches golden. Gap: ~10.5 pts.

---

## Excellence Signals

### What V-04/V-05 did better than V-01/V-02

**Phase C exit conditions as a numbered table (not a prose/checkbox list)**

V-04/V-05 express exit conditions as a table with columns `# | Condition | Status`:

```
| 2 | B1 PRE-COMMITMENT precedes B2 READ RECEIPT for every role | ☐ |
| 3 | B2 READ RECEIPT precedes B3 C2 RESULT for every role — C-35 ordering compliance item | ☐ |
```

V-01 uses a prose checklist with inline annotations. The table form makes each condition independently findable by row number without parsing surrounding text. This is not explicitly required by any current criterion — it is a format improvement over what C-30 and C-36 already capture.

**C-10 (GO WITH CONDITIONS) + C-30 (PRE-COMMITMENT in exit condition)**

V-04/V-05 are the only variations that pass both. V-01 passes C-30 but misses C-10 (no GO WITH CONDITIONS conditions detail). V-02 passes C-10 but misses C-30 (PRE-COMMITMENT absent from Block 3 compliance check). The combination requires: Phase D conditions table with resolution owner + Phase C exit table with PRE-COMMITMENT row.

---

## Failure Patterns

### Pattern 1 — IA Phase B regression (15 failing criteria)

R12 variations dropped the explicit Inertia Advocate Phase B (cost ledger, budget verdict, net direction column, three-clause formula, seal token, C1 RESULT pre-flight). R11 V-05 had all of these. R12 added C-36/C-37/C-38 correctly but collapsed the IA into an external document reference. This eliminated:

C-11, C-17, C-19, C-20, C-21, C-22, C-25, C-26 (partial), C-28, C-29, C-32

**R13 must restore IA Phase B from R11 V-05 and integrate C-36/C-37/C-38 into that structure — not substitute for it.**

### Pattern 2 — Consensus depth missing (C-09, C-12, C-13)

All variations have consensus sections that identify agreement/disagreement but none require:
- WHY roles diverge (architectural mechanism) — C-09
- Name-specific mechanism as cause of divergence — C-12
- Enumerated ban list of perspective-label phrases — C-13

These require additions to the consensus template (not just rewording).

### Pattern 3 — C1 RESULT absent (C-22, C-26 partial)

R12 eliminated the C1 pre-flight checkpoint (Phase B completeness check before Phase C starts). All variations have C2 RESULT per role but no C1 RESULT. The dual C1/C2 structure from R11 needs to be restored.

### Pattern 4 — Findings table missing Domain-Lens column (C-24)

All R12 findings tables have ID/Type/Severity/Description/Evidence. None add Domain-Lens as a column. This was present in earlier rounds and was dropped.

---

## R13 Direction

The R12 target (C-36/C-37/C-38) was fully achieved — all five variations PASS all three new criteria. The drop in composite score vs R11 V-05 is entirely explained by Pattern 1: the IA Phase B regression.

**R13 task**: Take R11 V-05 as the base (which had the full IA chain), and apply the R12 patterns (C-36 exit condition table, C-37 per-field C2 RESULT table, C-38 [IA-VERDICT]|[ROLE-MECHANISM] slots) to it without restructuring the phase model. Also add C-10 GO WITH CONDITIONS detail and Phase C exit conditions as a numbered table (potential C-39).

Expected R13 ceiling: R11 V-05 score + 3 new criteria (C-36/C-37/C-38) + C-10 + C-30 + potential C-39 = near-golden.

```json
{"top_score": 69.50, "all_essential_pass": true, "new_patterns": ["Phase C exit conditions expressed as a numbered table (# | Compliance Item | Verified?) rather than a prose or checkbox list — each condition independently findable by row number without prose parsing; not captured by C-30 or C-36 which only require naming, not table structure"]}
```
