Scorecard written. Here is the summary:

---

## Round 5 Results — `review-design`

**All five variations score 100. Winner circle: 5/5 (up from 4/5 in R4).**

### Score Table

| Var | Axis | Score | Outcome |
|-----|------|-------|---------|
| V-01 | role-sequence (domain-first) | **100** | Golden |
| V-02 | lifecycle (F-11 split halt) | **100** | Golden |
| V-03 | output-format (BLOCK 5 table) | **100** | Golden |
| V-04 | combined (F-11 + F-12 + table) | **100** | Golden |
| V-05 | combined maximum (full R5 stack) | **100** | Golden |

### Why All Five Hit 100

R5 made C-16 (Source column) and C-17 (F-10 orphan detection) baseline requirements across all variations. These were the two new v5 gates. With all 10 aspirational criteria pre-satisfied, the rubric ceiling is met uniformly — the distinguishing gaps are now rubric-invisible.

### Key Design Bet Confirmations

- **V-01 FAIL corrected**: R5 V-01 uses a proper 3-column table in BLOCK 1.5 (vs R4's prose list). C-15 PASS confirmed — the form-sensitivity finding from R4 is still the gate.
- **Role sequence is rubric-neutral**: Domain-first ordering in V-01/V-05 produces no scoring difference. Qualitative lift (consensus density) requires evidence from practice, not rubric.
- **F-11 and F-12 are additive**: F-11 targets BLOCK 3 synthesis content; F-12 targets BLOCK 2.5→BLOCK 5 count parity. Distinct error classes, no overlap.

### New Patterns (v6 candidates)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-11 is a content-completeness halt — a new enforcement class distinct from all prior F-IDs (which fire on structural absence, count mismatch, or identity mismatch): F-11 fires on content quality within a mandatory row (SPLIT synthesis field empty), converting C-09 from a post-hoc rubric check into an inline generation halt; C-18 candidate for v6", "F-12 completes the cross-block count-parity pattern: F-09 locked domain expert count at BLOCK 1 and verified at BLOCK 1.5; F-12 locks P1 count at BLOCK 2.5 and verifies at BLOCK 5; the anchor-then-verify pattern now spans the full output lifecycle; C-19 candidate for v6", "BLOCK 5 as 4-column table extends the structural column enforcement argument (C-10 for BLOCK 2, C-13 for BLOCK 1, C-16 for BLOCK 1.5) to the amend pathway — a blank Re-run Scope cell is visually detectable where a missing Re-run line in a code block is not; C-20 candidate for v6"]}
```
-----|--------|----------|
| V-01 | PASS | BLOCK 5 code-block format with Finding/Section/Action/Re-run; F-05 scoped to specific section |
| V-02 | PASS | Same code-block format; F-05 present |
| V-03 | PASS | BLOCK 5 as 4-column table: `P1 Finding | Section | Action | Re-run Scope`; F-05 fires on "full review" in Re-run Scope cell |
| V-04 | PASS | Same 4-column table; F-05 + F-12 present |
| V-05 | PASS | Same 4-column table; F-05 + F-12 present |

All PASS — C-06 requires structured amend with section-scoped re-run; both code-block and table form satisfy this criterion.

#### C-07 | Finding Traceability to Design Section

All PASS — all five carry `Section` column in BLOCK 2 with "P1 rows: Section always required. P2 rows: Section required for >= 50% of rows." Unchanged from R4.

---

### Aspirational Criteria (C-08 through C-17)

#### C-08 | Severity Distribution Sanity

All PASS — all five carry BLOCK 2.5 with Status column and Rationale row requirement when inverted.

#### C-09 | Expert Disagreement Analysis

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | SPLIT row format with Synthesis field in BLOCK 3; no inline halt |
| V-02 | PASS | Same + F-11: "An empty or absent synthesis field fires F-11. Halt and complete the synthesis before continuing." F-11 converts post-hoc detection to inline halt — structurally stronger, rubric score identical |
| V-03 | PASS | SPLIT row with Synthesis; no F-11 |
| V-04 | PASS | SPLIT + F-11 enforcement |
| V-05 | PASS | SPLIT + F-11 enforcement |

All PASS. V-02/V-04/V-05 are qualitatively stronger on C-09 (inline halt vs. post-hoc), but both forms satisfy the rubric pass condition.

#### C-10 | Structural Column Enforcement in Finding Tables

All PASS — all five use `| Sev | Section | Finding |` table format in BLOCK 2.

#### C-11 | Three-Field Expert Trace

All PASS — all five use the three-column domain expert table (`Signal detected | Expert added | Reason`) with labeled column form.

#### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block

All PASS — all five position BLOCK 2.5 between BLOCK 2 and BLOCK 3 as a discrete named block with the P3 >= P2 >= P1 check.

#### C-13 | Expert Trace in Table Column Form

All PASS — all five use three-column table form for domain expert trace. Resolved in R3, stable since.

---

#### C-14 | Named Halt Conditions on Every Mandatory Block

C-14 enumeration covers: findings (BLOCK 2), pyramid gate (BLOCK 2.5), consensus (BLOCK 3), unique catches (BLOCK 4), amend (BLOCK 5), plus C-01–C-04 content blocks. BLOCK 1.5 is not in the enumeration (confirmed R4).

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | F-01–F-10: BLOCK 1 (F-03, F-07), BLOCK 2 (F-01, F-02), BLOCK 2.5 (F-06), BLOCK 3 (F-04), BLOCK 4 (F-08), BLOCK 5 (F-05), BLOCK 1.5 (F-09, F-10) — all C-14 enumerated blocks covered |
| V-02 | PASS | F-01–F-11: same coverage + F-11 on BLOCK 3 SPLIT rows — additive beyond C-14 scope |
| V-03 | PASS | F-01–F-10: same coverage as V-01 |
| V-04 | PASS | F-01–F-12: F-11 (BLOCK 3) + F-12 (BLOCK 5) — additive beyond C-14 scope |
| V-05 | PASS | F-01–F-12: full stack; all mandatory blocks covered plus F-11, F-12 as bonus coverage |

All PASS.

---

#### C-15 | Roster Commitment Table Before Finding Generation

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 1.5 is a **three-column table** (`Reviewer | Role | Source`) with Domain rows listed first, then Stock rows — table form confirmed; R4 V-01 FAIL was due to prose list; R5 V-01 fixes this |
| V-02 | PASS | BLOCK 1.5 three-column table (Stock rows first, then Domain rows); table form confirmed |
| V-03 | PASS | Same three-column table (Stock first, then Domain); table form confirmed |
| V-04 | PASS | Same three-column table; F-09 + F-10 gate present |
| V-05 | PASS | Three-column table with Domain rows first; F-09 + F-10 gate present |

All PASS. **Key R5 change**: V-01 in R4 scored 98.75 because BLOCK 1.5 was a prose numbered list. R5 V-01 carries a proper three-column table — C-15 FAIL is corrected.

---

#### C-16 | Source Column in Roster Commitment Table

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 1.5 template explicitly shows `Reviewer | Role | Source` with `Domain` and `Stock` values |
| V-02 | PASS | Same three-column template with Source column and Stock/Domain values |
| V-03 | PASS | Same |
| V-04 | PASS | Same |
| V-05 | PASS | Same; "Source column distinguishes Stock from Domain" explicitly stated |

All PASS. C-16 is a new v5 gate included at baseline in all R5 variations. R4 V-01–V-03 did not have it; R4 V-04/V-05 introduced it. All R5 variations carry it forward.

---

#### C-17 | Cross-Block Reviewer Identity Verification (Orphan Detection)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | F-10 present: "Orphaned domain expert — BLOCK 1.5 contains a Domain row whose Reviewer name has no matching Expert added value in the BLOCK 1 domain expert table"; gate explicitly states "F-10 fires on any mismatch" |
| V-02 | PASS | F-10 present in failure mode registry; gate check after BLOCK 1.5 |
| V-03 | PASS | F-10 present; same gate |
| V-04 | PASS | F-10 present; same gate |
| V-05 | PASS | F-10 present; same gate; "F-10 fires on any mismatch" |

All PASS. C-17 is a new v5 gate included at baseline in all R5 variations. Previously introduced in R4 V-05 only.

---

### Composite Scores

Formula: `essential_pass/4 × 60 + recommended_pass/3 × 30 + aspirational_pass/10 × 10`

| Var | Essential (4->60) | Recommended (3->30) | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | C-17 | Asp (n/10->10) | **Score** | All Essential? | Outcome |
|-----|-------------------|----------------------|------|------|------|------|------|------|------|------|------|------|-----------------|-----------|----------------|---------|
| V-01 | 60 | 30 | P | P | P | P | P | P | P | P | P | P | 10/10 -> 10 | **100** | Yes | Golden |
| V-02 | 60 | 30 | P | P | P | P | P | P | P | P | P | P | 10/10 -> 10 | **100** | Yes | Golden |
| V-03 | 60 | 30 | P | P | P | P | P | P | P | P | P | P | 10/10 -> 10 | **100** | Yes | Golden |
| V-04 | 60 | 30 | P | P | P | P | P | P | P | P | P | P | 10/10 -> 10 | **100** | Yes | Golden |
| V-05 | 60 | 30 | P | P | P | P | P | P | P | P | P | P | 10/10 -> 10 | **100** | Yes | Golden |

`P = PASS`

---

### Ranking

| Rank | Variation | Score | Outcome | Tiebreaker |
|------|-----------|-------|---------|------------|
| 1 | V-05 (domain-first + full enforcement stack) | 100 | Golden | F-10 + F-11 + F-12 + BLOCK 5 table + domain-first ordering — maximum enforcement depth across all four error classes: identity, synthesis, count parity, structural visibility |
| 2 | V-04 (F-11 + F-12 + table) | 100 | Golden | F-11 + F-12 additive coverage confirmed; BLOCK 5 table closes structural visibility gap; tightest amend completeness enforcement outside domain-first |
| 3 | V-02 (F-11) | 100 | Golden | F-11 converts C-09 from post-hoc to inline halt; synthesis quality structurally enforced; cleaner isolation of single axis vs V-04 |
| 4 | V-03 (BLOCK 5 table) | 100 | Golden | BLOCK 5 structural column enforcement; same C-10 argument applied to amend pathway; Re-run Scope cell blank is visible where Re-run line missing in code block is not |
| 5 | V-01 (domain-first) | 100 | Golden | Confirms role-sequence is rubric-neutral; domain-first ordering does not lift v5 rubric score; tiebreaker position only |

---

### Design Bet Resolution

| Bet | Predicted | Actual | Finding |
|-----|-----------|--------|---------|
| V-01 scores 100 (fixed C-15 from R4 V-01) | 100 | **100** v | R5 V-01 carries a 3-column table in BLOCK 1.5, correcting the R4 prose-list FAIL. All five R5 variations clear C-15. |
| V-01 vs V-02-V-05: role-sequence is rubric-neutral | rubric tie | **tied at 100** v | Domain-first ordering does not affect any v5 criterion. The test was always qualitative (consensus density) — rubric score confirms neutrality. |
| V-02/V-03 isolation: F-11 and BLOCK 5 table are independent | additive | **additive** v | F-11 targets BLOCK 3 synthesis completeness; BLOCK 5 table targets amend structural visibility. Independent error classes — no overlap detected. |
| V-04 vs V-02+V-03: F-11 + F-12 additive, not redundant | additive | **additive** v | F-11 enforces within-BLOCK-3 synthesis quality; F-12 enforces BLOCK 2.5->BLOCK 5 count parity. Distinct error classes confirmed. |
| V-05 achieves 100 (full stack) | 100 | **100** v | Maximum enforcement stack clears all 10 aspirational criteria. Basis for v6 criterion extraction confirmed. |

All five design bets confirmed.

---

### Key Findings

**All five R5 variations score 100.** The winner circle has expanded from 4/5 in R4 to 5/5 in R5. The R4 distinguishing gate was C-15 form-sensitivity (V-01 FAIL at 98.75). In R5, all five variations include a proper roster commitment table (C-15 PASS) plus C-16 (Source column) and C-17 (F-10) at baseline — the two new v5 gates are pre-satisfied across the entire variation set.

**The rubric ceiling is met but the enforcement stack is not uniform.** V-05 carries F-11, F-12, BLOCK 5 table, and domain-first ordering that V-01 lacks. The qualitative gap is measurable: V-01 cannot catch a missing synthesis note at generation time (F-11 absent), cannot detect an under-counted amend entry set (F-12 absent), and cannot make a blank Re-run Scope cell visible (code-block BLOCK 5). All three gaps are rubric-invisible in v5 — they are the extraction candidates for C-18/C-19/C-20.

**F-11 + F-12 + BLOCK 5 table form a coherent enforcement tier.** Each addresses a completeness gap in a different output block: F-11 closes BLOCK 3 synthesis omission, F-12 closes BLOCK 5 undercount, and BLOCK 5 table makes F-05/F-12 failures structurally visible. The pattern is consistent with the enforcement evolution from R1 (C-10 structural columns) through R3 (C-14 named F-IDs) through R4 (C-15/C-16/C-17 proactive + structural + identity).

---

### Excellence Signals (from V-05, top-ranked variation)

**From V-05 + V-02/V-04 (F-11 synthesis halt):**
F-11 is the first halt condition that fires within a content block rather than on block presence or count. F-01-F-04 fire on missing blocks; F-09, F-12 fire on count mismatches; F-10 fires on identity mismatch — all are structural checks. F-11 fires on a content quality condition: a SPLIT row whose synthesis field is empty or absent. This is a new enforcement class: content completeness within a mandatory row, not structural block presence. If a SPLIT row with no synthesis cannot proceed past BLOCK 3, synthesis quality improves from aspirational to blocked.

**From V-04/V-05 (F-12 amend count parity):**
F-12 completes the count-parity pattern that F-09 began at BLOCK 1.5. F-09: Domain rows in BLOCK 1.5 = Domain expert count in BLOCK 1. F-12: BLOCK 5 entry count = P1 count from BLOCK 2.5. Both are cross-block count gates that lock a count at an upstream block and verify it at a downstream block. The P1 count locked at BLOCK 2.5 is the natural anchor for amend completeness — every P1 must have an amend entry, and F-12 makes that verifiable rather than inspectable.

**From V-03/V-04/V-05 (BLOCK 5 table form):**
The structural column argument from C-10 (R1) applies directly to BLOCK 5: a blank `Re-run Scope` cell in a table is visible; a missing `Re-run:` line inside a fenced code block is not. The code-block form used in V-01/V-02 satisfies C-06, but it allows silent omission of the Re-run field. Table form enforces column presence structurally. Three prior criteria (C-10, C-13, C-16) all follow the same pattern: column-form converts a skippable field into a visible blank. BLOCK 5 table form is the natural next application.

**From V-01/V-05 (domain-first ordering is rubric-neutral):**
V-01 confirms that placing domain experts first in BLOCK 1.5 and BLOCK 2 does not affect the v5 rubric score in either direction. Role sequencing is not a criterion gap — it is a generation strategy. The v5 rubric is form-sensitive (C-15, C-16 distinguish table from non-table) but not sequence-sensitive. If domain-first ordering produces measurably denser consensus blocks in practice, the evidence must come from qualitative review, not rubric scoring.

---

### New Patterns for R6

1. **F-11 is a content-completeness halt — a new enforcement class.** All prior halts are structural (missing block, missing cell, count mismatch, identity mismatch). F-11 fires on content quality within a row: synthesis field empty in a SPLIT row. This extends the named-halt pattern from block structure into block content. F-11 is a C-18 candidate: named halt condition on synthesis completeness for SPLIT rows in BLOCK 3.

2. **F-12 completes the cross-block count-parity pattern.** F-09 locks domain expert count at BLOCK 1 and verifies at BLOCK 1.5. F-12 locks P1 count at BLOCK 2.5 and verifies at BLOCK 5. The pattern is: anchor a count at a gate block, verify it at the downstream output block. F-12 is a C-19 candidate: amend count parity gate enforcing BLOCK 5 completeness against BLOCK 2.5 P1 count.

3. **BLOCK 5 as 4-column table extends C-10's structural column enforcement to the amend pathway.** C-10 (R1) covers BLOCK 2 finding tables. C-13/C-16 extend the column-visibility argument to BLOCK 1 expert trace and BLOCK 1.5 roster. BLOCK 5 is the remaining output block where a missing field (Re-run Scope) can be silently omitted in code-block format. Table form is the candidate for C-20: structural column enforcement in BLOCK 5.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["F-11 is a content-completeness halt — a new enforcement class distinct from all prior F-IDs (which fire on structural absence, count mismatch, or identity mismatch): F-11 fires on content quality within a mandatory row (SPLIT synthesis field empty), converting C-09 from a post-hoc rubric check into an inline generation halt; C-18 candidate for v6", "F-12 completes the cross-block count-parity pattern: F-09 locked domain expert count at BLOCK 1 and verified at BLOCK 1.5; F-12 locks P1 count at BLOCK 2.5 and verifies at BLOCK 5; the anchor-then-verify pattern now spans the full output lifecycle; C-19 candidate for v6", "BLOCK 5 as 4-column table extends the structural column enforcement argument (C-10 for BLOCK 2, C-13 for BLOCK 1, C-16 for BLOCK 1.5) to the amend pathway — a blank Re-run Scope cell is visually detectable where a missing Re-run line in a code block is not; C-20 candidate for v6"]}
```
