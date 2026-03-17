## Round 5 Scorecard — `discover-feasibility-alt` (v5 Rubric)

---

### V-01 — C-19 Absent (Baseline Confirm)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 | essential | PASS | All six sections present in required order; hard-coded in template. |
| C-02 | essential | PASS | RED Blockers block requires all three sub-fields on every RED component. |
| C-03 | essential | PASS | VERDICT template has score, label, and explicit "Not building this means:" line. |
| C-04 | essential | PASS | All four inertia surfaces present: INERTIA Baseline, ARCHITECT Do-nothing cost column required on every row, "Not building this means:", "Inertia saved:" in every amendment. |
| C-05 | essential | PASS | Item D explicitly rejects standalone section headings; "Never add a standalone focus section" preamble reinforces. |
| C-06 | recommended | PASS | AMENDMENTS template requires component name, color transition, score-delta estimate on every entry. |
| C-07 | recommended | PASS | Propagation contract + focus-adjusted economics in ARCHITECT ratings ensure focus demonstrably changes base sections. |
| C-08 | recommended | PASS | "Cover at least half the components from ARCHITECT" explicit instruction. |
| C-09 | aspirational | PASS | Propagation contract routes constraint through INERTIA → ARCHITECT → VERDICT → AMENDMENTS; multi-section propagation structurally guaranteed. |
| C-10 | aspirational | PASS | AMEND PROTOCOL handles focus shifts and threshold changes with selective re-weave. |
| C-11 | aspirational | PASS | Item A table explicitly names INERTIA, ARCHITECT, VERDICT, AMENDMENTS as routing targets. |
| C-12 | aspirational | PASS | Item D names "## COMPLIANCE", "## STAKEHOLDERS" as the specific failure-mode headings to avoid. |
| C-13 | aspirational | PASS | Focus adjustment is a separable unit rate that demonstrably raises do-nothing cost above no-focus baseline; ARCHITECT ratings can change because of focus economics. |
| C-14 | aspirational | PASS | AMEND PROTOCOL steps (1)–(4) present; step (2) requires explicit "Affected sections: / Unaffected sections:" declaration. |
| C-15 | aspirational | PASS | Three-line arithmetic formula: "Base do-nothing cost + Focus adjustment = Focus-adjusted do-nothing cost"; verifiable by inspection. |
| C-16 | aspirational | PASS | Propagation contract table with three columns appears in Step 0 before INFERENCE GATE. |
| C-17 | aspirational | PASS | Item A (table) precedes Item B (lens prose) and Item C (economics); ordering explicit in Step 0. |
| C-18 | aspirational | PASS | Column headers: "Constraint introduced by focus" / "Section where it surfaces" / "Effect on that section"; `[same]` on rows 2–4. |
| C-19 | aspirational | **FAIL** | Stated Effect cells use prose descriptions only; Item C formula uses prose labels ("Focus-adjusted do-nothing cost"), not the variable token `focus_adjusted_total`. Neither anchor point present — no closed loop. |

**Essential all-pass:** YES | **Aspirational pass count:** 10/11

```
Composite = (5/5 × 60) + (3/3 × 30) + (10/11 × 10)
          = 60 + 30 + 9.091
          = 99.09
```

**Band: Golden** (all essential PASS, no PARTIALs, composite ≥ 80)

---

### V-02 — C-19 Minimal Binding (AMENDMENTS Row Only)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-18 | — | all PASS | Same design as V-01 for all criteria except C-19. |
| C-19 | aspirational | **FAIL** | AMENDMENTS Stated Effect cell template references `` `focus_adjustment` eliminated + `base_cost` recaptured = `focus_adjusted_total` recaptured per sprint`` — correct cell-side binding. **But Item C formula uses prose labels** ("Base do-nothing cost / Focus adjustment / Focus-adjusted do-nothing cost"), not the variable name `focus_adjusted_total`. C-19 lexical test requires `focus_adjusted_total` in **both** locations (table cell AND formula section); grepping the formula section finds nothing. One-sided binding = FAIL, not PARTIAL, per rubric. |

**Essential all-pass:** YES | **Aspirational pass count:** 10/11

```
Composite = (5/5 × 60) + (3/3 × 30) + (10/11 × 10)
          = 60 + 30 + 9.091
          = 99.09
```

**Band: Golden**

> **Design finding:** Expected score was ~99.55 (assuming C-19 PARTIAL for one-cell binding). That does not materialize. V-02 establishes the table-side anchor but not the formula-side anchor. The closed loop is broken. C-19 is binary — FAIL under rubric v5. V-02 lands identically with V-01.

---

### V-03 — C-19 Full + Self-Enforcing Assertion

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-18 | — | all PASS | Same structural design; all prior criteria met identically. |
| C-19 | aspirational | **PASS** | Two conditions both satisfied: (1) All four Stated Effect rows reference `focus_adjusted_total` explicitly (INERTIA: "how `focus_adjusted_total` from Item C appears…"; ARCHITECT: "how `focus_adjusted_total` changes their rating…"; VERDICT: "confirm `focus_adjusted_total` appears in 'Not building this means:'"; AMENDMENTS: "`base_cost` recaptured + `focus_adjustment` eliminated = `focus_adjusted_total` recaptured per sprint"). (2) Item C formula defines `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]` as the named variable. Lexical test passes: grep `focus_adjusted_total` hits both the table cells and the formula section. Additionally, the **formula contract check** assertion ("Verify this is true before writing Item B") makes C-19 a model self-check, converting it from implicit wiring to explicit verification. |

**Essential all-pass:** YES | **Aspirational pass count:** 11/11

```
Composite = (5/5 × 60) + (3/3 × 30) + (11/11 × 10)
          = 60 + 30 + 10.000
          = 100.000
```

**Band: Golden**

---

### V-04 — C-19 Full + Named-Incumbent Framing

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-18 | — | all PASS | All prior criteria met; named-incumbent field and section heading rename do not break any structural requirement. INERTIA section heading "The Named Incumbent the Feature Must Beat" satisfies the section-order requirement (equivalent heading). |
| C-13 | aspirational | **PASS** | Named-incumbent field in INFERENCE GATE anchors the competitive entity explicitly ("the specific workaround, tool, or process the team uses today"). INERTIA table column "Named incumbent" vs generic "What the team does instead" strengthens the competitive calculation's concreteness. Focus-adjusted economics demonstrably change the named incumbent's do-nothing cost, not just abstract "workaround" costs. Strongest C-13 evidence of any variation that lacks the self-enforcing assertion. |
| C-19 | aspirational | **PASS** | All four Stated Effect rows reference `focus_adjusted_total` (AMENDMENTS row: "`base_cost` recaptured + `focus_adjustment` eliminated = `focus_adjusted_total` recaptured per sprint when named incumbent is replaced"). Item C formula: `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`. Lexical test passes in both locations. Named-incumbent framing enriches context of each cell but does not break the token-binding. |

**Essential all-pass:** YES | **Aspirational pass count:** 11/11

```
Composite = (5/5 × 60) + (3/3 × 30) + (11/11 × 10)
          = 60 + 30 + 10.000
          = 100.000
```

**Band: Golden**

---

### V-05 — Full Ceiling (C-19 Full + Self-Enforcing Assertion + Named Incumbent)

| ID | Tier | Result | Evidence |
|----|------|--------|----------|
| C-01 through C-18 | — | all PASS | All criteria satisfied; combines V-03 and V-04 structural elements without conflict. |
| C-13 | aspirational | **PASS** | Named-incumbent field (V-04 axis) + focus-adjusted economics (V-03 axis) together: the status quo is a named entity whose cost is demonstrably raised by the focus lens via an arithmetic formula. Strongest C-13 evidence of all variations. |
| C-19 | aspirational | **PASS** | Three reinforcing mechanisms active simultaneously: (1) All four Stated Effect rows name `focus_adjusted_total`; (2) Item C formula defines `focus_adjusted_total = base_cost + focus_adjustment`; (3) formula contract check assertion between Item A and Item B ("Verify this is true before writing Item B") requires the model to confirm the token appears in at least one cell before proceeding. Full closed loop with explicit self-verification. |

**Essential all-pass:** YES | **Aspirational pass count:** 11/11

```
Composite = (5/5 × 60) + (3/3 × 30) + (11/11 × 10)
          = 60 + 30 + 10.000
          = 100.000
```

**Band: Golden**

---

## Rankings

| Rank | Variation | Score | C-19 | Delta vs. below |
|------|-----------|-------|------|-----------------|
| 1 (tied) | V-03 | 100.000 | PASS | Full closed loop + self-enforcing assertion |
| 1 (tied) | V-04 | 100.000 | PASS | Full closed loop + named incumbent |
| 1 (tied) | V-05 | 100.000 | PASS | Full closed loop + assertion + named incumbent |
| 4 (tied) | V-01 | 99.09 | FAIL | No variable token in either location |
| 4 (tied) | V-02 | 99.09 | FAIL | Cell-side token present; formula-side absent — loop broken |

**V-05 is recommended production prompt** within the 100.000 tier: combines all three reinforcing mechanisms and produces the lowest expected variance across topic variation.

---

## Excellence Signals (from 100.000 variations)

**Signal 1 — Formula section variable naming is the prerequisite anchor for C-19**
V-02 demonstrates the failure mode: a Stated Effect cell can reference `focus_adjusted_total` but C-19 still fails when the formula section (Item C) uses prose labels. The formula section must define `focus_adjusted_total` as a named variable token for the lexical closed loop to be satisfiable. Cell-side binding alone is a dangling reference.

**Signal 2 — Self-enforcing assertion converts C-19 from implicit wiring to explicit model self-check**
V-03's formula contract check ("Verify this is true before writing Item B. If you wrote all four cells without naming the variable, revise the AMENDMENTS cell now.") makes the binding a deliberate step rather than a structural side-effect. This is the assertion pattern: state the condition + provide the correction action if violated.

**Signal 3 — Named-incumbent field in INFERENCE GATE strengthens C-13 without adding a section**
V-04's "Named incumbent: [...]" field anchors all competitive language to a specific entity without requiring a new section. The pattern: one named field propagates a concept through multiple downstream sections (INERTIA heading, Baseline sentence, VERDICT's "Not building this means:", AMENDMENTS framing). Section-free propagation via a single INFERENCE GATE field.

---

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["Formula section variable naming (focus_adjusted_total in Item C) is the prerequisite anchor for C-19 -- Stated Effect cell binding is a dangling reference without a matching token in the formula section; V-02 confirms one-sided binding scores FAIL not PARTIAL", "Self-enforcing assertion between Item A and Item B converts C-19 from implicit structural wiring to explicit model self-check with a named correction action if the variable token is absent", "Named-incumbent field in INFERENCE GATE propagates a competitive entity through INERTIA, VERDICT, and AMENDMENTS without adding a new section -- single-field propagation as the pattern for section-free concept injection"]}
```
