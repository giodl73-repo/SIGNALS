## /quest:score — mock-review R17

### Aspirational Baseline Assumptions

Before scoring the distinguishing axes, all variants share the core skill structure (STEP 4 shown, DECISION OUTPUT block, STEP 5 write-back, STEP 6 next-steps). Unless a variation's axis specifically displaces a criterion, all essentials (C-01–C-05), all recommended (C-06–C-08), and the shared aspirational infrastructure (C-09–C-10, C-12–C-14, C-16–C-21, C-23–C-26, C-28, C-30–C-34, C-37–C-40) are treated as **PASS** for all variants. Scoring differentiation comes from the five axes.

---

### Per-Criterion Differentiation Grid

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|:----:|:----:|:----:|:----:|:----:|-------|
| **C-11** Forbidden-output enumeration | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** | V-03/V-05 have [C-27] TRIAD header with per-rule DO NOT labeling |
| **C-15** Entity-naming SQ grammar | PARTIAL | PASS | **PASS** | PASS | **PASS** | V-01 inline SQ-N: format without enforced "Name X" grammar; V-03 imperative verbs satisfy; V-02/V-04/V-05 Row # tables enforce it |
| **C-22** Decision inversion framing | FAIL | FAIL | FAIL | **PASS** | **PASS** | "Inertia reminder at every step heading" (V-04 axis) is the named DEFAULT DECISION POSITION block C-22 requires |
| **C-27** Triad DO NOT coverage | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** | Per-rule individually labeled DO NOT statements require [C-27] TRIAD header (V-03/V-05) |
| **C-29** Phase-gate co-location | PARTIAL | PARTIAL | **PASS** | PARTIAL | **PASS** | Co-located TRIAD block at phase boundary follows from [C-27] labeling |
| **C-35** Strategy-first tier anchoring | **PASS** | FAIL | **PASS** | **PASS** | **PASS** | V-02 Arch-first breaks Strategy→Arch prerequisite |
| **C-36** Arch-first structural contradiction | FAIL | **PASS** | FAIL | FAIL | FAIL | Mutually exclusive with C-35; V-02 is the only Arch→Strategy→PM variant |
| **C-42** Universal criterion-ID labeling | PARTIAL | FAIL | **PASS** | PARTIAL | **PASS** | Scope boundary analysis: V-03/V-05 cover all structural elements; V-01/V-04 missing TRIAD header label; V-02 only C-40 core blocks |
| **C-43** Dedicated Row # column | FAIL | **PASS** | FAIL | **PASS** | **PASS** | Scope boundary analysis: V-01/V-03 use inline SQ-N: prefix; V-02/V-04/V-05 use `\| Row # \| Sub-question \|` table form |

---

### Per-Variant Scoring

**Aspirational denominator**: 35 (as specified in formula)
**Aspirational criteria in rubric**: 34 active criteria
**Base from essential + recommended** (if all pass): 60 + 30 = 90

#### V-01 — Lifecycle Emphasis

| Outcome | Criteria | Count |
|---------|----------|-------|
| FAIL | C-22, C-36, C-43 | 3 × 0 = 0 |
| PARTIAL | C-11, C-15, C-27, C-29, C-42 | 5 × 0.5 = 2.5 |
| PASS | remaining 26 | 26 × 1 = 26 |

Aspirational sum: 28.5 / 35 × 10 = **8.14**
**V-01 total: 98.14**

---

#### V-02 — Output Format (Arch-first)

| Outcome | Criteria | Count |
|---------|----------|-------|
| FAIL | C-22, C-35, C-42 | 3 × 0 = 0 |
| PARTIAL | C-11, C-27, C-29 | 3 × 0.5 = 1.5 |
| PASS | remaining 28 | 28 × 1 = 28 |

Aspirational sum: 29.5 / 35 × 10 = **8.43**
**V-02 total: 98.43**

---

#### V-03 — Phrasing Register ([C-27] TRIAD header, imperative verbs)

| Outcome | Criteria | Count |
|---------|----------|-------|
| FAIL | C-22, C-36, C-43 | 3 × 0 = 0 |
| PARTIAL | — | 0 |
| PASS | remaining 31 | 31 × 1 = 31 |

Notes: C-11/C-27/C-29 all PASS via [C-27] TRIAD header; C-15 PASS via imperative verb phrasing register ("Name...", "State...", "Identify..."); C-42 PASS (universal labeling confirmed in scope boundary analysis).

Aspirational sum: 31 / 35 × 10 = **8.86**
**V-03 total: 98.86**

---

#### V-04 — Role Sequence + Inertia

| Outcome | Criteria | Count |
|---------|----------|-------|
| FAIL | C-36 | 1 × 0 = 0 |
| PARTIAL | C-11, C-27, C-29, C-42 | 4 × 0.5 = 2.0 |
| PASS | remaining 29 | 29 × 1 = 29 |

Notes: C-22 PASS via inertia reminders at every step heading; C-43 PASS via Row # tables; C-42 PARTIAL (TRIAD header still unlabeled per scope boundary analysis).

Aspirational sum: 31 / 35 × 10 = **8.86**
**V-04 total: 98.86**

---

#### V-05 — All Combined

| Outcome | Criteria | Count |
|---------|----------|-------|
| FAIL | C-36 | 1 × 0 = 0 |
| PARTIAL | — | 0 |
| PASS | remaining 33 | 33 × 1 = 33 |

Notes: All four axes combined. [C-15] in table column header closes the last labeling gap. C-42 PASS (universal labeling). C-43 PASS (Row # tables). C-22 PASS (inertia). C-11/C-27/C-29 PASS ([C-27] TRIAD header). C-36 unavoidably FAIL because C-35 is satisfied (mutually exclusive pair — V-05 correctly chose Strategy-first).

Aspirational sum: 33 / 35 × 10 = **9.43**
**V-05 total: 99.43**

---

### Ranking

| Rank | Variant | Score | Decisive differentiator |
|------|---------|-------|------------------------|
| 1 | **V-05** | **99.43** | All axes combined; zero PARTIALs; only unavoidable C-36 FAIL |
| 2 (tie) | V-03 | 98.86 | [C-27] TRIAD labeling eliminates the partial-cluster; loses on C-22/C-43 |
| 2 (tie) | V-04 | 98.86 | Inertia + Row # tables win C-22/C-43; loses TRIAD labeling cluster to partials |
| 4 | V-02 | 98.43 | Row # tables win C-43; Arch-first strategy loses C-35 and C-22 |
| 5 | V-01 | 98.14 | Inline SQ-N: format costs C-43 + C-15; no inertia or TRIAD labeling |

---

### Excellence Signals from V-05

1. **Axis combination without regression** — V-05 stacks four axes without any axis displacing another. The Row # table structure (V-02's axis) provides exactly the slot structure V-03's [C-15] column-header label needs. Axes that reinforce each other compound rather than compete.

2. **Criterion-ID in column header as a two-level anchor** — placing `[C-15]` in the `Sub-question` column header links the sub-question grammar rule to its governing criterion at the template level. The column header becomes a self-labeling compliance anchor: any author filling the table is simultaneously constrained by the row structure (Row #) and annotated with the governing criterion label.

3. **TRIAD block as phase-gate co-resident** (C-27/C-29/C-11 cluster) — labeling the forbidden-output block with `[C-27]` at the phase boundary produces three simultaneous wins: per-rule enumeration (C-11), individually labeled statements (C-27), and phase-gate co-location (C-29). One structural decision satisfies the entire cluster.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Universal criterion-ID labeling on all structural elements (TRIAD header, AUTO-RULE guard header, step headings, slot headers, canary block) — each element carries the criterion it satisfies, enabling a single-scan mechanical audit rather than cross-referencing prose", "Dedicated leftmost Row # column in sub-question tables replaces inline SQ-N: prefix format — rows become independently citable by number, enabling the Artifact state field citation chain (C-14/C-21/C-24) to reference a specific row rather than an embedded prefix", "Criterion-ID annotation in table column header (Sub-question [C-15]) fuses the Row # table structure with its governing criterion label — the column header is a self-labeling compliance anchor that constrains author grammar at the point of entry"]}
```
