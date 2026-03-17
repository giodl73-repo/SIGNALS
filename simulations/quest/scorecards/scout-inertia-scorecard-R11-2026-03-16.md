## scout-inertia — Quest Score R11

**Rubric**: v11 (ceiling 180) | **Variations**: V-01 through V-05 | **Date**: 2026-03-17

---

## Per-Variation Scoring

### V-01 — Lifecycle emphasis

**Axis**: Stage-boundary lifecycle; `[A-16 PRIMARY KEY RULE]` + `[A-19 REFERENTIAL INTEGRITY RULE]` bracket-prefix; `[BRIDGE COMPLETION COMMAND]` directive in BRIDGE COMPLETION STATUS sub-section.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage 3 prompts specific tool/file name, role, ongoing cost with unit |
| C-02 | PASS | Stage 4 table, minimum 2 categories, unit requirement stated |
| C-03 | PASS | Stage 5A table, HIGH default, quantified-justification column |
| C-04 | PASS | Stage 5B table, falsifiability requirement stated, FM-[N] citation column |
| C-05 | PASS | Stage 1 C-05 question, minimum 2 rows, "slow" fails example given |
| A-08 | PASS | Stage 1 (FM) precedes Stage 5B (DC) by construction |
| A-10 | PASS | `## FAIL-FIRST DECLARATION` as structural first section |
| A-11 | PASS | All 5 criteria have labeled questions in respective stages |
| A-12 | PASS | FAIL-FIRST stage listing names Q3 (closes C-05→R-02) and Q4 (closes C-05→C-04) with chain refs |
| A-13 | PASS | All sections tabular; blank cell = visible gap |
| A-14 | PASS | `## STAGE 1 -- FAILURE MODE INVENTORY`, FM-[N] first column, before Stage 5B |
| A-15 | PASS | `## STAGE 6 -- COMPLETENESS CHECK` structurally last |
| A-16 | PASS | `[A-16 PRIMARY KEY RULE]: No FM-[N] identifier may appear in any later section...` in Stage 1 |
| A-17 | PASS | C-01 through C-05 each have labeled question; full coverage |
| A-18 | PASS | Stage 6 uses `Check (Y / N)` binary column, all 5 criteria mapped |
| A-19 | PASS | Source rule in Stage 1 + `[A-19 REFERENTIAL INTEGRITY RULE]` named rule at Stage 5B |
| A-20 | PASS | Ongoing cost `(e.g., 2 hours/week)`, Estimate `(e.g., 3 days)`, Duration `(e.g., 18 months)`, Frequency `(e.g., 2x/sprint)`, Trigger `(e.g., file > 10MB)` |
| A-21 | PASS | DC threshold column: `Measurable threshold (e.g., >10MB, >3 failures/week)` |
| A-22 | PASS | `### BRIDGE COMPLETION STATUS` block with Y/N table positioned between Stage 1 and Stage 3 |
| A-23 | PASS | `[A-16 PRIMARY KEY RULE]` contains A-16; `[A-19 REFERENTIAL INTEGRITY RULE]` contains A-19 — bracket-prefix form |
| A-24 | PASS | `>10MB` (size-based) + `>3 failures/week` (frequency-based) — two distinct threshold types in same label |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: Complete Q3 and Q4 before proceeding to Stage 3...` as named directive before Y/N table |

**Score: 180 / 180** ✓ All essential PASS

---

### V-02 — Phrasing register (COMMAND)

**Axis**: Imperative COMMAND phrasing; `PRIMARY KEY RULE [A-16]` + `CITATION INTEGRITY RULE [A-19]` bracket-suffix; `[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4...` all-caps directive.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | `[C-01 COMMAND]` prompts exact name, role, cost with unit |
| C-02 | PASS | `[C-02 COMMAND]` with [UNIT RULE] rejecting unitless estimates |
| C-03 | PASS | `[C-03 COMMAND]` with HIGH default, quantified justification required |
| C-04 | PASS | `[C-04 COMMAND]` with falsifiability requirement, FM-[N] citation |
| C-05 | PASS | `[C-05 COMMAND]` minimum 2 rows, reject "slow" |
| A-08 | PASS | Section 1 (FM) before Section 5 (DC) |
| A-10 | PASS | `[FAIL-FIRST RULE]:` label as structural first element in FAIL-FIRST section |
| A-11 | PASS | 5 COMMAND labels, one per criterion |
| A-12 | PASS | FAIL-FIRST bullet list names Q3/Q4 with chain refs |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | `## SECTION 1 -- FAILURE MODE INVENTORY`, FM-[N] first column |
| A-15 | PASS | `## COMPLETENESS CHECK` structurally last |
| A-16 | PASS | `PRIMARY KEY RULE [A-16]: ASSIGN all FM-[N] identifiers in this table first. NO FM-[N] reference may appear...` |
| A-17 | PASS | All 5 COMMAND labels present |
| A-18 | PASS | Y/N binary column, all 5 criteria |
| A-19 | PASS | Source rule (`PRIMARY KEY RULE [A-16]`) + `CITATION INTEGRITY RULE [A-19]` at Section 5 |
| A-20 | PASS | All unit-bearing columns carry inline examples |
| A-21 | PASS | `(e.g., >10MB, >3 failures/week)` in Q4 and DC threshold columns |
| A-22 | PASS | `## BRIDGE COMPLETION GATE` block with Y/N table between Q4 and Section 2 |
| A-23 | PASS | `PRIMARY KEY RULE [A-16]` contains A-16 (bracket-suffix); `CITATION INTEGRITY RULE [A-19]` contains A-19 (bracket-suffix) |
| A-24 | PASS | Same dual-type example — size + frequency |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE AUTHORING SECTION 2 THROUGH SECTION 5...` all-caps directive before Y/N table |

**Score: 180 / 180** ✓ All essential PASS

---

### V-03 — Inertia framing

**Axis**: Status-quo competitor framing; `STATUS QUO LOCK RULE [A-16]` + `STATUS QUO CITATION RULE [A-19]` domain-prefixed bracket-suffix; `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]` block heading.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | C-01 question in Section 2 prompts exact workaround name, role, cost with unit |
| C-02 | PASS | C-02 question in Section 3 with unit requirement |
| C-03 | PASS | C-03 question in Section 4, HIGH default, quantified justification |
| C-04 | PASS | C-04 question in Section 5, falsifiability requirement |
| C-05 | PASS | C-05 question in Section 1, minimum 2 rows, precision example |
| A-08 | PASS | Section 1 (FM) before Section 5 (DC) |
| A-10 | PASS | `## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR` as structural first section |
| A-11 | PASS | 5 labeled questions, one per criterion |
| A-12 | PASS | Q3 and Q4 named in FAIL-FIRST with chain refs |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | `## SECTION 1 -- THE STATUS QUO'S VULNERABILITIES: FAILURE MODE INVENTORY`, FM-[N] first column |
| A-15 | PASS | `## SECTION 6 -- COMPLETENESS VERIFICATION` structurally last |
| A-16 | PASS | `STATUS QUO LOCK RULE [A-16]: Assign all FM-[N] identifiers in this table first. No FM-[N] may appear in any later section...` |
| A-17 | PASS | All 5 criteria have labeled questions |
| A-18 | PASS | `Satisfied? (Y / N)` binary column, all 5 criteria |
| A-19 | PASS | Source rule (`STATUS QUO LOCK RULE [A-16]`) + `STATUS QUO CITATION RULE [A-19]` at Section 5 |
| A-20 | PASS | All unit-bearing columns carry inline examples |
| A-21 | PASS | `(e.g., >10MB, >3 failures/week)` in threshold columns |
| A-22 | PASS | `## BRIDGE COMPLETION GATE -- READY TO PROCEED?` block with Y/N table between Section 1 and Section 2 |
| A-23 | PASS | `STATUS QUO LOCK RULE [A-16]` contains A-16; `STATUS QUO CITATION RULE [A-19]` contains A-19 — **stress test confirmed: domain-prefix form satisfies A-23** |
| A-24 | PASS | Dual-type threshold example present |
| A-25 | PASS | `[ACTION REQUIRED: COMPLETE BRIDGE BEFORE PROCEEDING]: Both Q3 and Q4 must be populated before...` as named block heading, co-located with Y/N table |

**Score: 180 / 180** ✓ All essential PASS

---

### V-04 — Output format (triple-block bridge)

**Axis**: Consolidated Q3/Q4/gate within single Stage 2; `[A-16 PRIMARY KEY CONSTRAINT]` + `[A-19 CITATION INTEGRITY CONSTRAINT]` bracket-prefix variant labels; `### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3` as sub-section heading.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Stage 3 C-01 question with specific tool, role, cost |
| C-02 | PASS | Stage 4 C-02 question, two categories minimum, unit requirement |
| C-03 | PASS | Stage 5A C-03 question, HIGH default |
| C-04 | PASS | Stage 5B C-04 question, falsifiability, FM-[N] cite |
| C-05 | PASS | Stage 1 C-05 question, minimum 2 rows, precision example |
| A-08 | PASS | Stage 1 before Stage 5B |
| A-10 | PASS | `## FAIL-FIRST DECLARATION` as structural first section |
| A-11 | PASS | 5 labeled questions |
| A-12 | PASS | Q3 and Q4 named with chain refs in FAIL-FIRST |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | `## STAGE 1 -- FAILURE MODE INVENTORY`, FM-[N] first column |
| A-15 | PASS | `## STAGE 6 -- COMPLETENESS CHECK` structurally last |
| A-16 | PASS | `[A-16 PRIMARY KEY CONSTRAINT]: Assign all FM-[N] identifiers in this table first. No FM-[N] identifier may appear in the Defeat Conditions table (Stage 5B) or any other downstream section...` |
| A-17 | PASS | All 5 criteria have labeled questions |
| A-18 | PASS | Y/N binary column, all 5 criteria |
| A-19 | PASS | Source rule (`[A-16 PRIMARY KEY CONSTRAINT]`) + `[A-19 CITATION INTEGRITY CONSTRAINT]` at Stage 5B |
| A-20 | PASS | All unit-bearing columns carry inline examples |
| A-21 | PASS | `(e.g., >10MB, >3 failures/week)` in Q4 and DC threshold columns |
| A-22 | PASS | `### [BRIDGE COMPLETION COMMAND]...` sub-section with Y/N table inside Stage 2, before Stage 3 |
| A-23 | PASS | `[A-16 PRIMARY KEY CONSTRAINT]` contains A-16; `[A-19 CITATION INTEGRITY CONSTRAINT]` contains A-19 — bracket-prefix variant label form |
| A-24 | PASS | Dual-type threshold example present |
| A-25 | PASS | `### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3` — Markdown heading is a named structural element; directive co-located with Y/N table by definition as the section heading — **stress test confirmed: heading-as-directive satisfies A-25** |

**Score: 180 / 180** ✓ All essential PASS

> **V-04 excess signal**: The bridge verdict table introduces an "If N: action required" column (`Return to Stage 1 and complete actor mapping`), converting the gate from binary status check into a prescriptive action plan. This exceeds A-25 — the table itself becomes instructional, not just the command label.

---

### V-05 — All axes combined

**Axis**: COMMAND phrasing + inertia framing + `[A-16 PRIMARY KEY RULE]` + `[A-19 CITATION INTEGRITY RULE]` bracket-prefix + dual-type A-24 + `[BRIDGE COMPLETION COMMAND]` A-25 directive. R10 V-05 confirmation run.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | `[C-01 COMMAND]` with "unnamed competitor's current champion" framing |
| C-02 | PASS | `[C-02 COMMAND]` with [UNIT RULE] |
| C-03 | PASS | `[C-03 COMMAND]` with inertia framing |
| C-04 | PASS | `[C-04 COMMAND]` with FM-[N] derivation path |
| C-05 | PASS | `[C-05 COMMAND]` minimum 2 rows |
| A-08 | PASS | Section 1 before Section 5 |
| A-10 | PASS | `## [FAIL-FIRST DECLARATION] -- THE UNNAMED COMPETITOR` as structural first section |
| A-11 | PASS | 5 COMMAND labels |
| A-12 | PASS | Q3/Q4 named with chain refs in FAIL-FIRST |
| A-13 | PASS | All sections tabular |
| A-14 | PASS | `## SECTION 1 -- FAILURE MODE INVENTORY`, FM-[N] first column |
| A-15 | PASS | `## COMPLETENESS CHECK` structurally last |
| A-16 | PASS | `[A-16 PRIMARY KEY RULE]: ASSIGN all FM-[N] identifiers here first...` |
| A-17 | PASS | All 5 criteria have COMMAND labels |
| A-18 | PASS | Y/N binary column, all 5 criteria |
| A-19 | PASS | Source rule (`[A-16 PRIMARY KEY RULE]`) + `[A-19 CITATION INTEGRITY RULE]` at Section 5 |
| A-20 | PASS | All unit-bearing columns carry inline examples |
| A-21 | PASS | `(e.g., >10MB, >3 failures/week)` in Q4 and DC threshold columns |
| A-22 | PASS | `## BRIDGE COMPLETION GATE` block with Y/N table between Q4 and Section 2 |
| A-23 | PASS | `[A-16 PRIMARY KEY RULE]` contains A-16; `[A-19 CITATION INTEGRITY RULE]` contains A-19 — bracket-prefix |
| A-24 | PASS | Dual-type threshold example confirmed |
| A-25 | PASS | `[BRIDGE COMPLETION COMMAND]: CONFIRM Q3 AND Q4 ARE POPULATED BEFORE AUTHORING SECTION 2 THROUGH SECTION 5...` directive before Y/N table |

**Score: 180 / 180** ✓ All essential PASS

---

## Composite Score Table

| Variation | Essential (100) | Advanced (80) | Total | Rank |
|-----------|----------------|---------------|-------|------|
| V-01 | 100 | 80 | **180** | T-1 |
| V-02 | 100 | 80 | **180** | T-1 |
| V-03 | 100 | 80 | **180** | T-1 |
| V-04 | 100 | 80 | **180** | T-1 |
| V-05 | 100 | 80 | **180** | T-1 |

All five variations score 180/180. No differentiation by score.

---

## R11 Findings

### A-24 retroactive confirmation

A-24 was already passing in R10 V-01/V-02/V-03. All three used `(e.g., >10MB, >3 failures/week)` before the criterion was formalized. R11 scores confirm A-24 was a retroactive pass — it was not a new generation requirement. R10 V-01/V-02/V-03 should be re-read as 180/180 if evaluated under v11.

### A-23 stress test — domain-prefix form passes (V-03)

`STATUS QUO LOCK RULE [A-16]` and `STATUS QUO CITATION RULE [A-19]` satisfy A-23. The criterion is confirmed as purely ID-in-label-text with no positional constraint within the label. The domain prefix does not invalidate the ID. This establishes A-23 as label-content-only: any label that contains the criterion ID in any position (prefix, suffix, inline) passes.

### A-25 stress test — heading-as-directive passes (V-04)

`### [BRIDGE COMPLETION COMMAND]: COMPLETE Q3 AND Q4 BEFORE STAGE 3` as a Markdown section heading satisfies A-25. The heading is structurally co-located with the Y/N verdict table (it is the heading of the section containing the table). The criterion is confirmed as structural-element-type-agnostic: heading, inline bracket-label, and action-phrase block all satisfy the "named structural element co-located with the status table" requirement.

### V-04 excess signal — remediation column

V-04's bridge verdict table carries an "If N: action required" column specifying the exact return action for each failed artifact. This exceeds A-25 (which requires only the command directive). The remediation column is a new structural pattern: the gate table becomes both a status check AND an action dispatch table. No current criterion captures this distinction.

---

## Excellence Signals

From the top-scoring cluster (all tied at 180/180), the patterns that distinguish structural quality:

1. **Domain-framed rule labels with criterion IDs (V-03)** — Naming integrity rules with domain vocabulary (`STATUS QUO LOCK RULE`) while embedding the rubric ID in the label combines semantic coherence with traceability. Authors reading the template see domain-meaningful names; auditors can verify compliance without external reference.

2. **Sub-section heading as command directive (V-04)** — Using a Markdown heading as the A-25 directive means the gate section cannot be entered without reading the command — the heading IS the barrier. Separate prose directive blocks can be skimmed past; a heading cannot.

3. **Remediation column in bridge verdict table (V-04)** — Adding "If N: action required" transforms the gate from a binary readout into a prescriptive action dispatch. An author who sees N for Q3 doesn't need to re-read instructions — the action is in the same row.

4. **Dual-type threshold example as format universality signal (all)** — `>10MB, >3 failures/week` demonstrates that the operator+value+unit pattern applies across structurally different threshold families (size vs. frequency). A single-type example leaves authors unsure whether rate-based thresholds need the same format. Two types eliminate that ambiguity at the authoring point.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["A-23 is label-content-only: domain-prefix bracket-suffix form passes (STATUS QUO LOCK RULE [A-16]) confirming no positional constraint within label text", "A-25 is structural-element-type-agnostic: Markdown section heading above Y/N table satisfies co-location requirement as well as inline bracket-label or block directive", "Remediation column in bridge gate table (If N: action required per artifact) converts binary status check to prescriptive action dispatch — exceeds A-25, no current criterion captures this", "A-24 confirmed retroactively passing in R10 V-01/V-02/V-03 — dual-type threshold example was structurally present before the criterion was formalized"]}
```
