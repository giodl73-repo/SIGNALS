## flow-resilience — Round 7 Scorecard

**Rubric**: v7 (19 aspirational, denominator 19)
**Baseline**: R6 V-05, composite 94.21 (8/19 aspirational)
**Open criteria entering R7**: C-19, C-26, C-27

---

### Scoring Key

| Tier | Points | Condition |
|------|--------|-----------|
| Essential | 60 | All essential criteria pass |
| Proficient | 30 | All proficient criteria pass |
| Aspirational | (pass/19) × 10 | Fractional |

Baseline inherits: essential all PASS, proficient all PASS, aspirational C-17 C-18 C-20 C-21 C-22 C-23 C-24 C-25 PASS (8/19).

---

## Per-Variation Criterion Evaluation

### V-01 — Architecture-to-Contract Forward Reference (C-26 only)

**Change**: Mechanism column in the architecture table now names downstream artifacts by exact section title — `**Column Contract** section below` and `**Row Descriptors** section below`.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Scenario Coverage | PASS | Inherited from baseline — three classes present |
| C-02 Four-Field Structure | PASS | Inherited |
| C-03 Gap Identification | PASS | Inherited |
| C-04–C-08 (essential) | PASS | Inherited |
| C-09–C-16 (proficient) | PASS | Inherited |
| C-17 Four-level architecture table | PASS | Inherited |
| C-18 Column ownership contract | PASS | Inherited |
| C-19 Per-row field table schema | **FAIL** | Row Descriptors remain prose paragraphs; imperatives not inside table cells |
| C-20 Phase gate section | PASS | Inherited |
| C-21 Architecture table present | PASS | Inherited — required for C-26 |
| C-22 Column/slot level distinction | PASS | Inherited |
| C-23 Imperatives co-located at row | PASS | Inherited — required for C-27 |
| C-24 No horizontal rule between rows | PASS | Inherited |
| C-25 Unified index # column | PASS | Inherited |
| C-26 Architecture-to-contract forward ref | **PASS** | Mechanism column names `Column Contract` and `Row Descriptors` by exact section title; C-21 passes so dependency guard satisfied |
| C-27 Consequence-enumeration before fill | **FAIL** | Stakes appear inside fill instruction, not before it; C-23 passes but C-27 requires stakes *before* the imperative |

**Aspirational pass count**: 9/19
**Composite**: 60 + 30 + (9/19 × 10) = 60 + 30 + **4.74** = **94.74**

---

### V-02 — Consequence-Enumeration Before Fill (C-27 only)

**Change**: Row 3 descriptor gains a *Resolution-outcome stakes* paragraph before `**Write this row now.**` — "oversell if node A wins; double-charge if node B wins; duplicate fulfillment if merge is naive."

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 (essential) | PASS | Inherited |
| C-09–C-16 (proficient) | PASS | Inherited |
| C-17 Four-level architecture table | PASS | Inherited |
| C-18 Column ownership contract | PASS | Inherited |
| C-19 Per-row field table schema | **FAIL** | Row Descriptors still prose; no table cell container |
| C-20 Phase gate | PASS | Inherited |
| C-21 Architecture table present | PASS | Inherited |
| C-22 Column/slot level distinction | PASS | Inherited |
| C-23 Imperatives co-located at row | PASS | Inherited |
| C-24 No horizontal rule | PASS | Inherited |
| C-25 Unified index | PASS | Inherited |
| C-26 Architecture-to-contract forward ref | **FAIL** | Mechanism column still describes function without naming section titles; no title-level pointer present |
| C-27 Consequence-enumeration before fill | **PASS** | Row 3 names "oversell / double-charge / duplicate fulfillment" as distinct per-outcome business consequences positioned before fill instruction; C-23 passes so dependency guard satisfied |

**Aspirational pass count**: 9/19
**Composite**: 60 + 30 + (9/19 × 10) = 60 + 30 + **4.74** = **94.74**

---

### V-03 — Per-Row Field Table Schema (C-19 only)

**Change**: Row Descriptors prose section replaced by a **Row Descriptor Table** (`# | Scenario Class | Content Descriptor`). `**Write this row now.**` / `**Do not advance**` imperatives now reside inside table cells.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 (essential) | PASS | Inherited |
| C-09–C-16 (proficient) | PASS | Inherited |
| C-17 Four-level architecture table | PASS | Inherited |
| C-18 Column ownership contract | PASS | Inherited |
| C-19 Per-row field table schema | **PASS** | Row Descriptor Table provides per-row field schema; imperatives appear inside table cells at cell granularity, not in adjacent prose |
| C-20 Phase gate | PASS | Inherited |
| C-21 Architecture table present | PASS | Inherited |
| C-22 Column/slot level distinction | PASS | Inherited |
| C-23 Imperatives co-located at row | PASS | Imperatives remain co-located at cell granularity; structural container changed from prose paragraph to table cell but co-location property preserved |
| C-24 No horizontal rule | PASS | Inherited |
| C-25 Unified index | PASS | Inherited |
| C-26 Architecture-to-contract forward ref | **FAIL** | Mechanism column does not name section titles; Slot row still describes function without a title-level pointer to `Row Descriptor Table` |
| C-27 Consequence-enumeration before fill | **FAIL** | Stakes not enumerated before fill in the table cell; content describes what to write, not per-outcome consequences branching before the imperative |

**Aspirational pass count**: 9/19
**Composite**: 60 + 30 + (9/19 × 10) = 60 + 30 + **4.74** = **94.74**

---

### V-04 — Forward Reference + Consequence-Enumeration (C-26 + C-27)

**Change**: Both C-26 and C-27 axes applied; Row Descriptors remain prose (C-19 still fails).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 (essential) | PASS | Inherited |
| C-09–C-16 (proficient) | PASS | Inherited |
| C-17–C-18, C-20–C-22, C-24–C-25 | PASS | Inherited |
| C-19 Per-row field table schema | **FAIL** | Prose container retained; imperatives not inside table cells |
| C-23 Imperatives co-located | PASS | Inherited |
| C-26 Architecture-to-contract forward ref | **PASS** | `Column Contract section below` and `Row Descriptors section below` named as exact titles in Mechanism column; C-21 passes |
| C-27 Consequence-enumeration before fill | **PASS** | Row 3 prose descriptor: "oversell if node A wins; double-charge if node B wins; duplicate fulfillment if merge is naive" appears before `**Write this row now.**`; business consequences are distinct per resolution outcome; C-23 passes |

**Aspirational pass count**: 10/19
**Composite**: 60 + 30 + (10/19 × 10) = 60 + 30 + **5.26** = **95.26**

---

### V-05 — All Three Axes (C-19 + C-26 + C-27) ← **Round 7 ceiling**

**Change**: Row Descriptor Table replaces prose (C-19); Mechanism column gains section title pointers (C-26); Row 3 table cell gains consequence-enumeration before fill (C-27). The C-27 stakes sentence sits inside the Row 3 table cell, before `**Write this row now.**`, satisfying C-19 (table cell container) and C-27 (stakes before fill) in one structure.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-08 (essential) | PASS | Inherited |
| C-09–C-16 (proficient) | PASS | Inherited |
| C-17 Four-level architecture table | PASS | Inherited |
| C-18 Column ownership contract | PASS | Inherited |
| C-19 Per-row field table schema | **PASS** | Row Descriptor Table with `# | Scenario Class | Content Descriptor` columns; imperatives inside cells at cell granularity |
| C-20 Phase gate | PASS | Inherited |
| C-21 Architecture table present | PASS | Inherited |
| C-22 Column/slot level distinction | PASS | Inherited |
| C-23 Imperatives co-located at row | PASS | Imperatives in cells; co-location preserved in new container |
| C-24 No horizontal rule | PASS | Inherited |
| C-25 Unified index | PASS | Inherited |
| C-26 Architecture-to-contract forward ref | **PASS** | Slot row Mechanism now reads "Bold **Write this row now.** / **Do not advance** imperatives co-located inside the **Row Descriptor Table** section below" — exact title pointer; C-21 passes |
| C-27 Consequence-enumeration before fill | **PASS** | Row 3 cell: "oversell if node A wins; double-charge if node B wins; duplicate fulfillment if merge is naive" — three distinct per-outcome business consequences, positioned before `**Write this row now.**`; C-23 passes; C-19's table cell container provides clean structural separation |

**Aspirational pass count**: 11/19
**Composite**: 60 + 30 + (11/19 × 10) = 60 + 30 + **5.79** = **95.79**

---

## Rankings

| Rank | Variation | Aspirational | Composite | Delta vs Baseline |
|------|-----------|-------------|-----------|-------------------|
| 1 | **V-05** (C-19 + C-26 + C-27) | 11/19 | **95.79** | +1.58 |
| 2 | **V-04** (C-26 + C-27) | 10/19 | **95.26** | +1.05 |
| 3= | **V-01** (C-26) | 9/19 | **94.74** | +0.53 |
| 3= | **V-02** (C-27) | 9/19 | **94.74** | +0.53 |
| 3= | **V-03** (C-19) | 9/19 | **94.74** | +0.53 |

---

## Excellence Signals (V-05)

**1. Structural upgrade enables criterion composability.** The Row Descriptor Table (C-19) is not just a container change — it creates the exact structural unit that C-27 needs. Placing the consequence-stakes sentence inside the table cell before the imperative satisfies two criteria with one structure. Neither criterion undermines the other; the table cell granularity makes both visibly correct.

**2. Forward reference as closed-loop auditability.** Naming `Column Contract section below` and `Row Descriptor Table section below` in the architecture table's Mechanism column turns the architecture table into a verifiable index. A reader can confirm each named artifact exists. The chain is auditable without holding the full prompt in memory — and breaking either section makes the architecture claim visibly false.

**3. Consequence-first framing elevates fill from content spec to outcome spec.** Enumerating "oversell if A wins / double-charge if B wins / duplicate fulfillment if merge is naive" *before* the fill instruction reframes adequacy: a vague fill is not just incomplete, it is visibly inadequate against named business stakes. This shifts the fill requirement from "write something here" to "write something that prevents these outcomes."

**4. Dependency guards encode structural integrity.** C-26 cannot pass if C-21 fails; C-27 cannot pass if C-23 fails. V-05 earns both derived criteria only because it also satisfies both structural criteria they extend. The scoring system correctly rewards the full chain, not isolated additions.

---

```json
{"top_score": 95.79, "all_essential_pass": true, "new_patterns": ["structural-upgrade-enables-criterion-composability", "forward-reference-as-closed-loop-auditability", "consequence-first-framing-elevates-fill-to-outcome-spec"]}
```
