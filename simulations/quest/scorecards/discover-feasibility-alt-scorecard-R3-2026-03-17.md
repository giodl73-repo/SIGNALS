## `discover-feasibility-alt` — Round 3 Scoring

**Rubric**: v3 (16 criteria: 5 essential, 3 recommended, 8 aspirational)
**Baseline**: R2 V-05 passed C-01–C-13 + C-14 + C-15; failed only C-16 (2-column table)

---

### Shared Baseline (C-01 through C-13)

All five R3 variations inherit R2 V-05's mechanics on every pre-v3 criterion. Rationale compressed:

| ID | Status | Evidence |
|----|--------|----------|
| C-01 | **PASS** | INFERENCE GATE template requires Feature, Team, Timeline — all present |
| C-02 | **PASS** | VERDICT section enforces score + label + range consistency; prerequisites gated on FEASIBLE WITH CAVEATS + RED |
| C-03 | **PASS** | Every component row carries a traffic-light cell; RED Blockers block has all three sub-fields; "No RED components" escape hatch present |
| C-04 | **PASS** | All four surfaces: INERTIA section + Baseline sentence, Do-nothing cost column in ARCHITECT, "Not building this means:" in VERDICT, "Inertia saved:" in AMENDMENTS |
| C-05 | **PASS** | Item D explicitly prohibits standalone focus sections; focus content flows through Propagation Contract rows into existing sections |
| C-06 | **PASS** | AMENDMENTS template requires component name, color transition, score-delta estimate on every action |
| C-07 | **PASS** | Step 0 Item B computes focus-adjusted economics that feed into ARCHITECT ratings — demonstrably different from no-focus run |
| C-08 | **PASS** | STRATEGY template covers all ARCHITECT components (100% ≥ 50%) |
| C-09 | **PASS** | Propagation Contract rows trace constraint through INERTIA → ARCHITECT → VERDICT → AMENDMENTS (4 sections, well above 2-section threshold) |
| C-10 | **PASS** | AMEND PROTOCOL: Step B identifies affected vs. unaffected; Step C re-weaves only affected sections |
| C-11 | **PASS** | Item C table (pre-section, before INFERENCE GATE) names the primary constraint and explicitly lists downstream sections |
| C-12 | **PASS** | Item D names the exact section heading to avoid ("## COMPLIANCE", "## STAKEHOLDERS") — specificity exceeds the structural-correctness bar |
| C-13 | **PASS** | Step 0 Item B computes focus-adjusted do-nothing cost; the focus lens demonstrably shifts the competitive calculation vs. base cost |

---

### Variation-Level Scoring (C-14, C-15, C-16)

#### V-01 — C-16 Minimal (3-Column Table, Constraint Repeated)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PARTIAL** | AMEND PROTOCOL shows Steps A–B–C (3 named steps). Step B carries "Declare: Unaffected sections will not be rewritten" ✓. Missing: explicit Step D for **update-VERDICT** as a named 4th step. R2 V-05 had Steps A–D; V-01 template truncates at C. Unaffected declaration present; 4-step structure incomplete. |
| C-15 | **PASS** | Item B retains the formula: `base_cost + focus_adjustment = TOTAL per sprint` with unit-rate annotation. Verifiable by inspection. |
| C-16 | **PASS** | Item C table has 3 explicit columns: `Constraint \| Downstream Section \| Stated Effect`. Constraint phrase repeated verbatim on all 4 section rows. Table appears before INFERENCE GATE heading. Binary criterion — structurally unambiguous. |

```
Essential:     5/5 × 60 = 60.000
Recommended:   3/3 × 30 = 30.000
Aspirational:  7.5/8 × 10 = 9.375   (C-14 = 0.5)
Total:         99.375   — Golden
```

---

#### V-02 — C-16 Table-First Ordering

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PARTIAL** | Same AMEND PROTOCOL as V-01 (A–B–C, no Step D). Reordering Step 0 items does not affect AMEND structure. |
| C-15 | **PASS** | Item B economics formula unchanged; table-first ordering moves the table before lens + economics but does not alter the formula. |
| C-16 | **PASS** | 3-column table is now the *first* item in Step 0 — still appears before any section heading. C-16 pass condition is met regardless of whether table precedes or follows lens/economics within Step 0. |

*Note: Table-first ordering may improve C-11 reliability (contract written before lens interpretation) but does not change rubric outcome — C-11 was already PASS.*

```
Essential:     5/5 × 60 = 60.000
Recommended:   3/3 × 30 = 30.000
Aspirational:  7.5/8 × 10 = 9.375
Total:         99.375   — Golden
```

---

#### V-03 — C-16 Explicit Column Semantics

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PARTIAL** | AMEND PROTOCOL unchanged from V-01 (A–B–C). V-03 only changes column header language in Item C. |
| C-15 | **PASS** | Item B formula unchanged. |
| C-16 | **PASS** | Column headers use rubric-aligned language: `Constraint introduced by focus \| Section where it surfaces \| Effect on that section`. "[same]" back-reference on rows 2–4 satisfies the "same constraint phrase repeated" requirement without redundancy. |

*Note: Rubric-aligned column headers reduce interpretation ambiguity but do not earn extra points over V-01's bare column names — C-16 is binary (PASS/FAIL).*

```
Essential:     5/5 × 60 = 60.000
Recommended:   3/3 × 30 = 30.000
Aspirational:  7.5/8 × 10 = 9.375
Total:         99.375   — Golden
```

---

#### V-04 — C-16 + C-14 Named-Unaffected Precision

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PASS** | AMEND PROTOCOL uses explicit numbered steps (1)–(4): (1) parse, (2) identify affected, (3) re-weave only, (4) update VERDICT. Step 2 carries: "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten." — both the 4-step structure and the named-unaffected declaration are present. |
| C-15 | **PASS** | Item B formula unchanged from R2 V-05. |
| C-16 | **PASS** | 3-column table before INFERENCE GATE, constraint repeated per row. |

```
Essential:     5/5 × 60 = 60.000
Recommended:   3/3 × 30 = 30.000
Aspirational:  8/8 × 10 = 10.000
Total:         100.000  — Golden
```

---

#### V-05 — Full Battery (C-16 + C-14 + C-15 Reinforced)

| ID | Result | Evidence |
|----|--------|----------|
| C-14 | **PASS** | Same numbered (1)–(4) protocol + named unaffected declaration as V-04. |
| C-15 | **PASS** | Formula uses exact rubric variable names: `focus_adjusted_total = base_cost + focus_adjustment`. Verifiable by name-matching against rubric spec without interpretation. Strongest form of C-15 — no gap between formula and spec language. |
| C-16 | **PASS** | 3-column table, constraint repeated, before INFERENCE GATE. |

*Note: V-05's C-15 precision (exact rubric variable names) does not score higher than V-04's C-15 PASS — both achieve PASS. The value is implementation reliability: exact variable names eliminate the paraphrase gap that could cause a downstream model to produce prose instead of formula.*

```
Essential:     5/5 × 60 = 60.000
Recommended:   3/3 × 30 = 30.000
Aspirational:  8/8 × 10 = 10.000
Total:         100.000  — Golden
```

---

### Ranking

| Rank | Variation | Score | Band | C-14 | C-15 | C-16 |
|------|-----------|-------|------|------|------|------|
| 1 | **V-04** | **100.000** | Golden | PASS | PASS | PASS |
| 1 | **V-05** | **100.000** | Golden | PASS | PASS | PASS |
| 3 | V-01 | 99.375 | Golden | PARTIAL | PASS | PASS |
| 3 | V-02 | 99.375 | Golden | PARTIAL | PASS | PASS |
| 3 | V-03 | 99.375 | Golden | PARTIAL | PASS | PASS |

All five variations are Golden. The gap between tiers is C-14 PARTIAL vs. PASS.

---

### Excellence Signals (from V-04 / V-05)

**Signal 1 — Numbered steps that mirror rubric function labels exactly**
Using `(1) parse / (2) identify-affected / (3) re-weave-only / (4) update-VERDICT` as the literal step labels eliminates any ambiguity about whether the 4-step structure is present. A model following this prompt cannot conflate "re-weave" with "update VERDICT" into a single step — the rubric's exact vocabulary is the protocol vocabulary.

**Signal 2 — Explicit "Affected: / Unaffected:" dual declaration as a formal utterance**
The declaration "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten." in Step 2 (identify-affected) makes the scope boundary visible as a named artifact, not as an implicit consequence of what gets rewritten. This is more reliable than inferring scope from the re-weave output.

**Signal 3 (V-05) — Exact rubric variable names as formula tokens**
Writing `focus_adjusted_total = base_cost + focus_adjustment` rather than `[base + adjustment = TOTAL]` closes the paraphrase gap: a model reading the prompt will use the exact tokens the rubric expects, making C-15 verifiable by string inspection rather than semantic judgment.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["numbered-step-labels-mirror-rubric-function-vocabulary", "explicit-dual-declaration-affected-unaffected-as-formal-utterance", "exact-rubric-variable-names-as-formula-tokens-eliminate-paraphrase-gap"]}
```
