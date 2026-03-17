Now I have all the data. Let me write the R4 scorecard.

---

## Scorecard — `review-design` Round 4 (v4 rubric)

### Rubric Context

v4 formula: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/8 × 10)`
Aspirational denominator: 8 (C-08 through C-15). Each criterion: **1.25 pts**.
C-15 is the new gate: roster commitment **table** (not prose list) before BLOCK 2.

---

### Essential Criteria (C-01 through C-04)

#### C-01 | Discipline Coverage (6 stock reviewers)

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | 6 stock disciplines in BLOCK 1.5 scheduled list; F-01 fires if any missing from BLOCK 2 |
| V-02 | PASS | Stock table (fixed, 6 rows) in BLOCK 1 + BLOCK 1.5 table; F-01 fires on missing discipline |
| V-03 | PASS | Stock table (fixed) + BLOCK 1.5; "A missing reviewer fires F-01" |
| V-04 | PASS | Stock table + BLOCK 1.5; "Gate: Confirm all reviewers in BLOCK 1.5 have a finding table. A missing reviewer fires F-01." |
| V-05 | PASS | Stock table + BLOCK 1.5; "Every reviewer listed in BLOCK 1.5 must have a finding table in this block. A missing reviewer fires F-01." |

All PASS — unchanged baseline from R3.

---

#### C-02 | Finding Severity Tagged

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | `Sev` column with P1/P2/P3 only; F-02 fires on any other value |
| V-02 | PASS | `Sev` column contract; "Any other value fires F-02 — halt and correct." |
| V-03 | PASS | `Sev: P1, P2, or P3 ONLY. Any other value — HALT, correct it, then continue. F-02 fires.` |
| V-04 | PASS | `Sev` column; "Any other value fires F-02 — halt and correct before proceeding." |
| V-05 | PASS | Same column contract; F-02 |

All PASS — unchanged from R3.

---

#### C-03 | Domain Expert Justified

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Domain expert table with `Signal detected | Expert added | Reason`; F-03 fires on empty Signal; F-07 fires on empty Expert/Reason |
| V-02 | PASS | Same three-column table; F-03 + F-07; "Every row requires all three cells populated" |
| V-03 | PASS | Same table; F-03 + F-07; "VERIFY: every row has all three cells populated." |
| V-04 | PASS | Same table; F-03 + F-07 |
| V-05 | PASS | Same table; F-03 + F-07; count instruction added after |

All PASS — unchanged from R3.

---

#### C-04 | Consensus Block Present

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | BLOCK 3 with "Never omit this block — F-04 fires on omission regardless of review content." |
| V-02 | PASS | BLOCK 3 + "Never omit this block — F-04 fires on omission." |
| V-03 | PASS | BLOCK 3; "DO NOT skip this block. F-04 fires on omission." (imperative form) |
| V-04 | PASS | BLOCK 3; "Gate: This block is mandatory. F-04 fires on omission regardless of review content." |
| V-05 | PASS | BLOCK 3; "F-04 fires on omission regardless of review content." |

All PASS — unchanged from R3.

---

### Recommended Criteria (C-05 through C-07)

#### C-05 | Unique Catches Surfaced

All PASS — all five variations carry BLOCK 4 with F-08 halt and `UNIQUE | none | —` fallback. Unchanged from R3.

#### C-06 | Amend Pathway Described

All PASS — all five variations carry BLOCK 5 with F-05 halt, `Re-run: [reviewer] on [section scope only]`, and explicit anti-full-review enforcement. Unchanged from R3.

#### C-07 | Finding Traceability to Design Section

All PASS — all five variations carry Section column with "P1 rows: Section always required. P2 rows: Section required for >= 50% of rows." Unchanged from R3.

---

### Aspirational Criteria (C-08 through C-15)

#### C-08 | Severity Distribution Sanity

All PASS — all five carry BLOCK 2.5 with Status column and Rationale row requirement if inverted. Unchanged from R3.

#### C-09 | Expert Disagreement Analysis

All PASS — all five carry `SPLIT | [decision] | A: [pos] / B: [pos] — Synthesis: [1-3 sent.]` in BLOCK 3. Unchanged from R3.

#### C-10 | Structural Column Enforcement in Finding Tables

All PASS — all five use `| Sev | Section | Finding |` table in BLOCK 2. Unchanged from R3.

#### C-11 | Three-Field Expert Trace

All PASS — all five use the domain expert table with three distinct columns (`Signal detected | Expert added | Reason`). All provide the three labeled fields in populated form.

#### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block

All PASS — all five place BLOCK 2.5 between BLOCK 2 and BLOCK 3 as a discrete named block with an explicit P3 >= P2 >= P1 check.

---

#### C-13 | Expert Trace in Table Column Form

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | Domain expert table: `| Signal detected | Expert added | Reason |` — three-column table form |
| V-02 | PASS | Same three-column domain expert table |
| V-03 | PASS | Same three-column domain expert table |
| V-04 | PASS | Same three-column domain expert table |
| V-05 | PASS | Same three-column domain expert table |

All PASS — all R4 variations use table form for BLOCK 1 (unlike R3 V-01 which used labeled prose). The C-13 axis is not the design variable in R4.

---

#### C-14 | Named Halt Conditions on Every Mandatory Block

C-14 pass condition enumerates mandatory blocks: "C-01 through C-04" and "findings, pyramid gate, consensus, unique catches, amend." BLOCK 1.5 is **not** in this enumeration.

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | PASS | F-01 through F-09: BLOCK 1 (F-03/F-07), BLOCK 1.5 (F-09), BLOCK 2 (F-01/F-02), BLOCK 2.5 (F-06), BLOCK 3 (F-04), BLOCK 4 (F-08), BLOCK 5 (F-05) — all mandatory blocks covered |
| V-02 | PASS | F-01 through F-08: BLOCK 1 (F-03/F-07), BLOCK 2 (F-01/F-02), BLOCK 2.5 (F-06), BLOCK 3 (F-04), BLOCK 4 (F-08), BLOCK 5 (F-05) — all C-14 enumerated blocks covered. BLOCK 1.5 lacks F-09, but BLOCK 1.5 is not in C-14's enumeration. C-14 PASS. |
| V-03 | PASS | F-01 through F-09: all mandatory blocks covered including BLOCK 1.5 (F-09) |
| V-04 | PASS | F-01 through F-09: all mandatory blocks covered |
| V-05 | PASS | F-01 through F-10: all mandatory blocks covered plus F-10 (orphan detection) as bonus coverage |

All PASS. Critical finding: **V-02 passes C-14 without F-09** because BLOCK 1.5 is not in the C-14 structural block enumeration. The enumeration is exhaustive.

---

#### C-15 | Roster Commitment Table Before Finding Generation

C-15 pass condition: "A roster commitment TABLE appears in the output prior to the first per-reviewer finding block."

| Var | Result | Evidence |
|-----|--------|----------|
| V-01 | **FAIL** | BLOCK 1.5 is a **prose numbered list** (`1. Architect (Stock)`, `2. Code-Quality (Stock)`, ...). The proactive intent is fulfilled — roster committed before BLOCK 2 — but the structural form is a list, not a table. C-15 explicitly requires "roster commitment TABLE." Prose list != table. C-15 FAIL by design. |
| V-02 | PASS | BLOCK 1.5 is a two-column table (`Reviewer | Role`) positioned before BLOCK 2. Table form satisfied. |
| V-03 | PASS | BLOCK 1.5 is a two-column table (`Reviewer | Role`) with F-09 annotation. Table form satisfied. |
| V-04 | PASS | BLOCK 1.5 is a three-column table (`Reviewer | Role | Source`) with F-09 annotation. Extended table form — still satisfies "roster commitment table." |
| V-05 | PASS | BLOCK 1.5 is a three-column table (`Reviewer | Role | Source`) with F-09 + F-10 + count gate. Strongest table form. |

V-01 FAIL by design — isolates C-15 form-sensitivity.

---

### Composite Scores

Formula: `essential_pass/4 × 60 + recommended_pass/3 × 30 + aspirational_pass/8 × 10`

| Var | Essential (4/4→60) | Recommended (3/3→30) | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | Asp (n/8→10) | **Score** | All Essential? | Outcome |
|-----|--------------------|----------------------|------|------|------|------|------|------|------|------|--------------|-----------|----------------|---------|
| V-01 | 60 | 30 | P | P | P | P | P | P | P | **F** | 7/8 → 8.75 | **98.75** | Yes | Golden |
| V-02 | 60 | 30 | P | P | P | P | P | P | P | P | 8/8 → 10 | **100** | Yes | Golden |
| V-03 | 60 | 30 | P | P | P | P | P | P | P | P | 8/8 → 10 | **100** | Yes | Golden |
| V-04 | 60 | 30 | P | P | P | P | P | P | P | P | 8/8 → 10 | **100** | Yes | Golden |
| V-05 | 60 | 30 | P | P | P | P | P | P | P | P | 8/8 → 10 | **100** | Yes | Golden |

`P = PASS, F = FAIL`

---

### Ranking

| Rank | Variation | Score | Outcome | Tiebreaker |
|------|-----------|-------|---------|------------|
| 1 | V-05 (lifecycle + inertia + format) | 100 | Golden | 10 F-IDs + Source column + cross-block count gate + F-10 orphan detection — deepest cross-block integrity enforcement |
| 2 | V-04 (format + lifecycle) | 100 | Golden | Source column makes BLOCK 1→BLOCK 1.5 linkage structurally visible; F-09 anchors it with a named halt |
| 3 | V-03 (phrasing register) | 100 | Golden | Imperative register throughout ("HALT", "DO NOT proceed", "WRITE") — maximum command clarity; F-09 present |
| 4 | V-02 (output-format, no F-09) | 100 | Golden | Minimum winning form for C-15: table present + F-09 absent still scores 100; proves C-14 enumeration is exhaustive |
| 5 | V-01 (lifecycle-emphasis) | 98.75 | Golden | C-15 FAIL confirms form-sensitivity: prose pre-commitment list vs. required table form is the distinguishing criterion |

---

### Design Bet Resolution

| Bet | Predicted | Actual | Finding |
|-----|-----------|--------|---------|
| V-01 vs V-03 delta = 1.25 pts | 1.25 | **1.25** ✓ | C-15 is form-sensitive. Prose pre-commitment list fails C-15 even when proactive intent is fulfilled. Table form is specifically required. |
| V-02 vs V-03 delta = 0 or 1.25 pts | 0 or 1.25 | **0** ✓ | C-14 enumeration is exhaustive — BLOCK 1.5 is not in it. V-02 passes C-14 without F-09. Both score 100. |
| V-03 vs V-04 both 100 | both 100 | **both 100** ✓ | Source column creates qualitative linkage visibility; no rubric-detectable lift beyond V-03. |
| V-04 vs V-05 both 100 | both 100 | **both 100** ✓ | Cross-block count gate + F-10 orphan detection is qualitative; no rubric-detectable lift beyond V-04. |

All four design bets confirmed in the predicted direction.

---

### Key Findings

**C-15 is form-sensitive, not intent-sensitive.** V-01 proves that placing a numbered list before BLOCK 2 satisfies the proactive intent of roster pre-commitment but fails the pass condition. The table form is the rubric gate, not mere positional precedence. A prose list is not a table.

**C-14's structural block enumeration is exhaustive.** V-02 scores 100 without F-09. BLOCK 1.5 is not in C-14's enumeration of mandatory blocks ("findings, pyramid gate, consensus, unique catches, amend"). Once C-15 is satisfied by the table form, C-14 and C-15 are fully independent. F-09 is additive coverage beyond C-14's scope — useful enforcement but not required for either criterion pass.

**Four variations score 100 in R4.** The winner circle is wider than R3 (three variations at 100). The single distinguishing gate is C-15's table form requirement. Any variation that presents a roster table before BLOCK 2 clears the bar regardless of whether F-09 is present.

---

### Excellence Signals (from top-scoring variations)

**From V-02 (minimum winning form for C-15):**
The minimum form to satisfy C-15 is precise: a table (any Markdown table with at least Reviewer and Role columns) positioned before the first finding block. F-09 is optional. This is the floor — sufficient to score 100, leaving qualitative headroom above.

**From V-04 (Source column linkage):**
Adding a `Source` column to BLOCK 1.5 creates a structurally visible contract between BLOCK 1 (where domain experts are selected) and BLOCK 1.5 (where the roster is committed). A `Domain` row with no corresponding BLOCK 1 entry is visually detectable without running the F-10 logic. The Source column is the structural form of the cross-block constraint.

**From V-05 (F-10 orphan detection):**
F-10 introduces a new error class distinct from all prior F-IDs: a reviewer who appears in the commitment table but whose name does not match any `Expert added` value in BLOCK 1. F-03 catches an empty `Signal detected` cell; F-09 catches a count mismatch; F-10 catches an identity mismatch — a reviewer who was renamed or substituted between BLOCK 1 and BLOCK 1.5. This cross-block referential integrity pattern has no prior rubric criterion.

---

### New Patterns for R5

1. **C-15 is form-sensitive, not presence-sensitive.** A prose pre-commitment list at the correct position (before BLOCK 2) fails C-15. Table form is the explicit requirement. Confirmed by V-01 FAIL (98.75) vs. V-02 PASS (100) — a single structural form change, 1.25 pts.

2. **C-14 structural block enumeration is exhaustive.** BLOCK 1.5 is not in the C-14 enumeration. F-09 is not required for C-14 pass once BLOCK 1.5 exists as a table. C-14 and C-15 are independent criteria — neither substitutes for the other, and neither requires the other's enforcement mechanism.

3. **Cross-block referential integrity (F-10 orphan detection) is a new enforcement tier.** F-10 catches a reviewer in BLOCK 1.5 whose name doesn't exactly match any `Expert added` value in BLOCK 1 — a substitution or renaming error that F-03 (missing cell), F-07 (empty cell), and F-09 (count mismatch) cannot catch. This is a candidate for C-16: exact-match cross-block identity verification as a distinct enforcement tier beyond proactive roster commitment.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-15 is form-sensitive: a prose pre-commitment list placed before BLOCK 2 fulfills the proactive intent but fails the table form requirement — 1.25 pt gap confirmed by V-01 FAIL vs V-02 PASS", "C-14 structural block enumeration is exhaustive — BLOCK 1.5 is not in it, so F-09 is not required for C-14 pass once the roster table (C-15) exists; the two criteria are fully independent", "cross-block referential integrity (F-10 orphan detection) is a new enforcement tier: catches a reviewer in BLOCK 1.5 whose name does not match any Expert added value in BLOCK 1 — a substitution error not catchable by F-03, F-07, or F-09 — candidate for C-16"]}
```
