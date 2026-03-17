Written to `simulations/quest/golden/scout-size-variate-R7-2026-03-17.md`.

---

## scout-size — Prompt Variations R7

### What informed this round

R6 V-04/V-05 score **17/17** on the v7 rubric. The rubric adds two new aspirational criteria sourced from the R6 scoring gap:

| Criterion | What it requires | R6 gap |
|-----------|-----------------|--------|
| **C-24** | Synthesis surfaces the three-step commitment chain on **separate labeled lines** — Gate commitment: / Analysis: / Verdict: — not folded into a prose paragraph | R6 V-03 passes C-22 (names PRE-FLIGHT GATE in prose twice) but the three steps are in one sentence |
| **C-25** | PRE-FLIGHT GATE names its downstream **enforcement sections** (outbound mesh) — distinguishing scope-enforcement sections from hypothesis-enforcement section | R6 V-03 passes C-23 (guards point home) but the gate doesn't list its guarantors |

---

### Variation axes

| ID | Single-axis | C-24 | C-25 | Expected score (v7) |
|----|------------|------|------|---------------------|
| **V-01** | Structured synthesis trace only | PASS | FAIL | 98.82 (fails C-20, C-23, C-25) |
| **V-02** | Gate forward-reference only | FAIL | PASS | 98.82 (fails C-21, C-22, C-24) |
| **V-03** | Minimal combination — C-24 + C-25, no self-check | PASS | PASS | **100** |
| **V-04** | Full integration + 25-criterion self-check | PASS | PASS | **100** |
| **V-05** | Full integration + structural definitions for C-24/C-25 disqualifying forms | PASS | PASS | **100** |

---

### Key structural mechanisms added

**C-24** — Every synthesis section gains a labeled `Commitment chain:` block:
```
Gate commitment: [tier] / [sprint range]
Analysis: [key evidence from steps — two or more signal dimensions]
Verdict: "The preliminary hypothesis committed in PRE-FLIGHT GATE..."
```
Explicit prohibition: "A prose paragraph that folds the same information into a single sentence fails C-24."

**C-25** — PRE-FLIGHT GATE adds an enforcement contract after STOP:
```
Scope exclusions: enforced in STEP 1, STEP 2, STEP 3, and STEP 7 SYNTHESIS
Hypothesis: confirmed or revised in STEP 7 SYNTHESIS
```
V-05 self-check disqualifying form: "stating 'preconditions for STEP 1 through STEP 7' is a continuation instruction, not an enforcement contract — fails C-25."
