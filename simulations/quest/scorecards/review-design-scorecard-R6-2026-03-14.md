Now I have everything needed. Let me score all five variations.

---

# Scorecard — review-design Round 6

## Rubric Summary (v6)

- **Essential (60%)**: C-01 through C-04 — must all pass
- **Recommended (30%)**: C-05 through C-07
- **Aspirational (10%)**: C-08 through C-20 — 13 criteria, each ~0.769 pts
- **Formula**: `(essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/13 * 10)`

v6 baseline: R5-V05 already carries F-11 (C-18), F-12 (C-19), and BLOCK 5 4-column table (C-20). R6 axes are three new structural bets: register isolation (V-01), BLOCK 3 4-column Synthesis column (V-02), BLOCK 0 pre-scan catalogue (V-03), and combined forms (V-04, V-05).

---

## Criterion-by-Criterion Analysis

### C-01 | All 6 Stock Disciplines Present

All five variations include all 6 stock disciplines (Architect, Code-Quality, Documentation, Testing, Process, Implementation) in a fixed stock table and require a finding block per reviewer via F-01 enforcement.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | Fixed stock table + F-01 fires on absence |
| V-02 | **PASS** | Fixed stock table + F-01 fires on absence |
| V-03 | **PASS** | Fixed stock table + F-01 fires on absence |
| V-04 | **PASS** | Fixed stock table + F-01 fires on absence |
| V-05 | **PASS** | Fixed stock table + F-01 fires on absence |

---

### C-02 | Severity Tag on Every Finding

All variations use a structured `Sev | Section | Finding` table with column contract "P1, P2, or P3 only — any other value fires F-02."

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | `Sev SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.` |
| V-02 | **PASS** | `Sev: P1, P2, or P3 only. Any other value fires F-02 — halt and correct.` |
| V-03 | **PASS** | Same as V-02 |
| V-04 | **PASS** | Same as V-02 |
| V-05 | **PASS** | `Sev SHALL contain exactly one of P1, P2, or P3. Any other value is non-conformant under F-02.` |

---

### C-03 | Domain Expert Auto-Selection Justified

All variations include a `Signal detected | Expert added | Reason` domain expert table in BLOCK 1. F-03 fires on empty Signal detected. V-03/V-04/V-05 add BLOCK 0 pre-scan which strengthens signal coverage before table fill.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | Three-column domain expert table; F-03 fires on empty Signal detected |
| V-02 | **PASS** | Same three-column table; F-03 named |
| V-03 | **PASS** | BLOCK 0 pre-scan feeds BLOCK 1; F-03 fires on empty or non-BLOCK-0 signal |
| V-04 | **PASS** | BLOCK 0 + BLOCK 1 two-pass detection |
| V-05 | **PASS** | BLOCK 0 + BLOCK 1 + formal language: "SHALL NOT add any domain expert whose Signal detected value is absent from this catalogue" |

---

### C-04 | Consensus Block Present

All variations include BLOCK 3 with F-04 firing on omission.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | `BLOCK 3 absence fires F-04 regardless of review content.` |
| V-02 | **PASS** | `F-04 fires if this block is omitted.` |
| V-03 | **PASS** | `F-04 fires on omission.` |
| V-04 | **PASS** | `F-04 fires if this block is omitted.` |
| V-05 | **PASS** | `BLOCK 3 absence fires F-04 regardless of review content.` |

---

### C-05 | Unique Catches Surfaced

All variations include BLOCK 4 with F-08 firing on omission, and a fallback row for empty catches.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | BLOCK 4 with `| UNIQUE | none | — |` fallback; F-08 on omission |
| V-02 | **PASS** | Same |
| V-03 | **PASS** | Same |
| V-04 | **PASS** | Same |
| V-05 | **PASS** | Same |

---

### C-06 | Amend Pathway Described

All variations include BLOCK 5 with a 4-column table, section-scoped Re-run Scope requirement, and F-05 firing on "full review."

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | `| P1 Finding \| Section \| Action \| Re-run Scope |` + F-05 on "full review" |
| V-02 | **PASS** | Same table form + F-05 + F-12 gate |
| V-03 | **PASS** | Same |
| V-04 | **PASS** | Same |
| V-05 | **PASS** | Same with formal language |

---

### C-07 | Finding Traceability to Design Section

All variations require Section populated for all P1 rows and ≥50% of P2 rows as explicit column contracts in BLOCK 2.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | "P1 rows: Section MUST be populated. P2 rows: Section MUST be populated in >= 50% of P2 rows." |
| V-02 | **PASS** | Same numeric threshold stated |
| V-03 | **PASS** | Same |
| V-04 | **PASS** | Same |
| V-05 | **PASS** | Same with formal language |

---

### C-08 | Severity Distribution Sanity

All variations include BLOCK 2.5 as a dedicated gate with a Status column and F-06 requiring a Rationale row when inverted.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | `| Severity \| Count \| Status |` table; F-06 fires on inverted without Rationale |
| V-02 | **PASS** | Same |
| V-03 | **PASS** | Same |
| V-04 | **PASS** | Same |
| V-05 | **PASS** | Same |

---

### C-09 | Expert Disagreement Analysis

All variations require SPLIT row synthesis. V-01/V-03 use merged `Reviewers / Synthesis` column with inline `— Synthesis:` marker; V-02/V-04/V-05 use 4-column form with dedicated Synthesis cell. Both forms enforce F-11, but 4-column form makes synthesis visibly absent rather than requiring content inspection.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | F-11 declared; synthesis text required inline; "Synthesis field MUST name the underlying design tension" |
| V-02 | **PASS** | Dedicated Synthesis column; blank Synthesis cell fires F-11; "must name the underlying design tension" |
| V-03 | **PASS** | Same as V-01 format (3-column) with F-11 |
| V-04 | **PASS** | 4-column Synthesis dedicated column |
| V-05 | **PASS** | 4-column Synthesis with formal language |

---

### C-10 | Structural Column Enforcement in Finding Tables

All variations use `Sev | Section | Finding` table format for per-reviewer findings.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | All use identical BLOCK 2 table structure |

---

### C-11 | Three-Field Expert Trace

All variations use `Signal detected | Expert added | Reason` as three distinct labeled table columns in BLOCK 1.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | All include three-column domain expert table; F-03 on empty Signal detected, F-07 on empty Expert added or Reason |

---

### C-12 | Severity Pyramid Gate as Dedicated Lifecycle Block

All variations position BLOCK 2.5 as a discrete block between BLOCK 2 and BLOCK 3 with explicit lifecycle instruction "positioned between BLOCK 2 and BLOCK 3."

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | BLOCK 2.5 header explicitly marks position; Status column table present |

---

### C-13 | Expert Trace in Table Column Form

All variations use the three-column table form (not labeled prose) for domain expert selection.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | `| Signal detected \| Expert added \| Reason |` table in all variations |

---

### C-14 | Named Halt Conditions on Every Mandatory Block

All variations carry the full F-01 through F-12 registry. Every mandatory block has at least one named F-ID with a stated trigger.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | F-01–F-12 all defined; BLOCK 4 now carries F-08 (previously the gap that caused failure in R3) |
| V-02 | **PASS** | Same registry |
| V-03 | **PASS** | Same registry |
| V-04 | **PASS** | Same registry |
| V-05 | **PASS** | Same registry |

---

### C-15 | Roster Commitment Table Before Finding Generation

All variations include BLOCK 1.5 as a Markdown table before any finding block is generated.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | `| Reviewer \| Role \| Source |` table positioned before BLOCK 2 |

---

### C-16 | Source Column in Roster Commitment Table

All variations include a `Source` column (`Domain` / `Stock`) in BLOCK 1.5.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | Source column present with explicit Domain/Stock distinction |

---

### C-17 | Cross-Block Reviewer Identity Verification (Orphan Detection)

All variations declare F-10 with exact trigger: "Domain row Reviewer name has no matching Expert added value in BLOCK 1."

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | F-10 in registry; BLOCK 1.5 gate explicitly checks exact name match |

---

### C-18 | Content-Completeness Halt on SPLIT Synthesis Field

All variations declare F-11. V-01/V-03 enforce via inline marker in merged cell; V-02/V-04/V-05 enforce via dedicated Synthesis column cell.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | F-11 declared; "An empty or absent Synthesis field is non-conformant under F-11. The block SHALL NOT be closed until all SPLIT row Synthesis fields are populated." |
| V-02 | **PASS** | F-11 declared; "A blank Synthesis cell fires F-11" in dedicated column context |
| V-03 | **PASS** | F-11 declared; fires on empty or absent Synthesis field |
| V-04 | **PASS** | F-11 + dedicated Synthesis column |
| V-05 | **PASS** | F-11 + dedicated Synthesis column + formal language |

---

### C-19 | Cross-Block Count-Parity for P1 Findings

All variations record `P1 count` at BLOCK 2.5 and enforce F-12 gate before BLOCK 5 closes.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01 | **PASS** | "This value is the anchor for the BLOCK 5 conformance gate (F-12)." Gate checks entry count ≥ P1 count |
| V-02 | **PASS** | Same; "F-12 fires if BLOCK 5 entry count < P1 count" |
| V-03 | **PASS** | Same |
| V-04 | **PASS** | Same |
| V-05 | **PASS** | Same with formal language |

---

### C-20 | BLOCK 5 Amend Pathway in 4-Column Table Form

All variations use `| P1 Finding | Section | Action | Re-run Scope |` 4-column table for BLOCK 5.

| Var | Result | Evidence |
|-----|--------|---------|
| V-01–V-05 | **PASS** | Identical 4-column BLOCK 5 structure in all variations |

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
| **Essential** | 60 | 60 | 60 | 60 | 60 | 60 |
| **Recommended** | 30 | 30 | 30 | 30 | 30 | 30 |
| **Aspirational** | 10 | 10 | 10 | 10 | 10 | 10 |
| **TOTAL** | 100 | **100** | **100** | **100** | **100** | **100** |

---

## Round 6 Ranking

All five variations score **100** on v6. This is the expected outcome: v6 was designed from R5 new_patterns that were already baked into the R5-V05 baseline. R6 is pushing axes that the current rubric cannot yet distinguish.

| Rank | Var | Score | Structural depth |
|------|-----|-------|-----------------|
| 1 | V-05 | 100 | All three axes: formal register + BLOCK 0 pre-scan + 4-column BLOCK 3 Synthesis |
| 2 | V-04 | 100 | Two structural axes: BLOCK 0 pre-scan + 4-column BLOCK 3 |
| 2 | V-02 | 100 | 4-column BLOCK 3 Synthesis column (single-axis isolation) |
| 2 | V-03 | 100 | BLOCK 0 pre-scan catalogue (single-axis isolation) |
| 5 | V-01 | 100 | Register-only isolation (single-axis); structure identical to R5-V05 |

Within the tie, V-05 is qualitatively richest: the only variation that combines all three novel R6 axes. V-01 is weakest within the 100 tier — its sole contribution is the register variable, which can only be evaluated empirically (actual model output quality), not by prompt analysis.

---

## Excellence Signals (V-05 — top structural variation)

**BLOCK 3 4-column Synthesis column**: V-02/V-04/V-05 split `Reviewers / Synthesis` into two distinct columns: `Reviewers` and `Synthesis`. A blank `Synthesis` cell for a SPLIT row is structurally visible — the same blank-cell enforcement argument that motivated C-10 (Sev column), C-13 (Signal detected column), C-16 (Source column), and C-20 (Re-run Scope column). With a merged cell, F-11 enforcement depends on detecting absence within a text value; with a dedicated column, it degrades to detecting a blank cell. This is the final column-separation gap in the lifecycle.

**BLOCK 0 pre-scan signal catalogue**: V-03/V-04/V-05 introduce a two-pass structure: detect first (BLOCK 0), assign second (BLOCK 1). BLOCK 1 is restricted — no expert whose signal is absent from BLOCK 0 may be added. This creates a cross-block traceability constraint at the detection phase, extending the anchor-then-verify pattern upstream of BLOCK 1. F-03 already fires on an empty Signal detected cell; BLOCK 0 now enforces that the signal must have been catalogued before the expert assignment table is even opened.

**Formal declarative register as isolated axis**: V-01 controls for register by holding structure constant (identical to R5-V05) and switching from imperative ("Halt and restructure immediately") to formal declarative ("A conformance failure is declared when...the output SHALL NOT proceed"). This is the cleanest isolation of the register variable across all six rounds. Whether register affects adherence can only be answered empirically — but V-01 makes the experiment runnable.

---

## v7 Criterion Candidates

The three R6 axes produce three candidate criteria for v7:

**C-21 candidate | BLOCK 3 Dedicated Synthesis Column**
- V-02, V-04, V-05 separate Synthesis from Reviewers into a structurally distinct column in BLOCK 3
- Blank-cell detection replaces content inspection for F-11
- V-01, V-03 score 100 without it — confirms aspirational
- Pattern: extends column-separation enforcement to the last merged-cell block

**C-22 candidate | BLOCK 0 Pre-Scan Signal Catalogue**
- V-03, V-04, V-05 add a BLOCK 0 catalogue pass before BLOCK 1 expert assignment
- Decouples signal detection from table filling; BLOCK 1 restricted to catalogued signals
- V-01, V-02 score 100 without it — confirms aspirational
- Pattern: extends anchor-then-verify upstream into the detection phase

**C-23 candidate | Formal Declarative Register Throughout**
- V-01 and V-05 use MUST/SHALL/non-conformant vs. imperative commands
- R2 established that conversational register degraded C-08 adherence
- V-01 holds structure constant — register is the single variable
- Whether register affects adherence is an empirical question; rubric cannot test prompt quality, only structure — this may remain uncodifiable as a rubric criterion unless output-level scoring shows a measurable gap

---

## Scorecard Output

Written to `simulations/quest/scorecards/review-design-scorecard-R6-2026-03-14.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["BLOCK 3 4-column Synthesis column: split 'Reviewers / Synthesis' merged cell into dedicated Reviewers and Synthesis columns — blank Synthesis cell is now structurally detectable, same blank-cell enforcement argument as Sev column (C-10), Source column (C-16), Re-run Scope column (C-20); closes the last merged-cell gap in the lifecycle", "BLOCK 0 pre-scan signal catalogue: two-pass structure — BLOCK 0 catalogs all domain signals before BLOCK 1 assigns experts; BLOCK 1 restricted to signals present in BLOCK 0 catalogue; extends anchor-then-verify pattern upstream into the detection phase; V-01/V-02 score 100 without it, confirming aspirational", "Formal declarative register (MUST/SHALL/non-conformant) as isolated axis: V-01 holds all R5-V05 structure constant with register as the single variable; R2 showed conversational register degraded enforcement — formal declarative is the opposite pole; effect is empirical, not rubric-detectable from prompt analysis alone"]}
```
