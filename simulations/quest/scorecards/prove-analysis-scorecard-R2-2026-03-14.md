## Round 2 Scorecard — prove-analysis

**Scoring basis:** Structural analysis of prompt designs (trace artifact: placeholder). Each criterion assessed for the prompt's capacity to produce a passing output, not actual output evaluation.

---

### Criterion-by-Criterion Scoring

#### V-01: Null-table + MECHANISM [Required] + QUANTIFIED CLAIMS [Required]

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Source" column: "Not 'the data'...if you cannot name it, do not add a row" |
| C-02 | Pattern stated | PASS | "Pattern found" column: "Write 'No pattern detected' if none. Do not hedge." |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" column: "Explicit link required" |
| C-04 | Correlation vs causal labeled | PASS | Fixed three-option "Correlation or causal?" column; no other terms permitted |
| C-05 | Strength assessed | PASS | "Strength" column: "tier + at least one of: number, rate, count, or logical argument" |
| C-06 | Multiple sources | PASS | "Minimum two rows required" — structural floor |
| C-07 | Counter-patterns | PASS | COUNTER-PATTERN SUMMARY [Required] collects all "Null met" rows explicitly |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required]: "at least one numeric claim must appear here" |
| C-09 | Causal mechanism proposed | PASS | MECHANISM [Required] section with three pre-printed sentence templates that are verbatim C-09 pass condition sentences |
| C-10 | Scope and validity | PASS | VERDICT.Scope field: "conditions under which patterns hold and where they may not generalize" |
| C-11 | Per-source structured format | PASS | 6-column table; each essential obligation occupies a named column |
| C-12 | Null/falsification framing | PASS | Null expectation pre-stated before any row; "Null expectation met?" column enforces per-row comparison |
| C-13 | Vocabulary precision | FAIL | Table column enforces vocabulary in that column only; MECHANISM section and VERDICT narrative have no forbidden-terms guard; hedged terms can appear in non-table text |

**Score: 60 + 30 + (5+5+5+5+0) = 110/115**

---

#### V-02: Vocabulary-Locked Table

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Source" column: "not 'the data'...if you cannot name it, do not add a row" |
| C-02 | Pattern stated | PASS | "Pattern found" column: "No pattern detected" if none, no hedging |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" column: explicit link required |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" column restricted to ONLY vocabulary contract terms |
| C-05 | Strength assessed | PASS | "Strength" column: tier + number/rate/count/argument |
| C-06 | Multiple sources | PASS | "Minimum two rows required" |
| C-07 | Counter-patterns | PASS | COUNTER-PATTERNS [Required]: "at least one entry" |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required] with numeric floor |
| C-09 | Causal mechanism proposed | FAIL | No MECHANISM section or mechanism sentence prompt anywhere in the template; vocabulary precision does not incidentally produce mechanism content |
| C-10 | Scope and validity | PASS | VERDICT.Scope field present |
| C-11 | Per-source structured format | PASS | 5-column table; each essential obligation in a named column |
| C-12 | Null/falsification framing | FAIL | No null expectation stated; no "Null expectation met?" column; no falsification language anywhere |
| C-13 | Vocabulary precision | PASS | VOCABULARY CONTRACT (forbidden terms listed + required replacements) + "Relationship type" column restricted to contract terms + VOCABULARY COMPLIANCE CHECK audits ALL relationship claims before VERDICT — strongest C-13 structural guarantee of any variation |

**Score: 60 + 30 + (0+5+5+0+5) = 105/115**

---

#### V-03: Per-Source Falsification Blocks

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Source identifier" field: "Specific named artifact...Not 'the data'...if you cannot name it, do not use this source" |
| C-02 | Pattern stated | PASS | "Pattern" field: "No pattern detected" if none, no hedging |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" field: "Explicit link required — start with 'This bears on the hypothesis because...'" |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" field with three named options |
| C-05 | Strength assessed | PASS | "Strength" field: tier + number/rate/N of M/effect size/p-value |
| C-06 | Multiple sources | PASS | "Minimum two sources required" |
| C-07 | Counter-patterns | PASS | "Counter-evidence" field per source; explicitly asks for weakening/contradicting data |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required] |
| C-09 | Causal mechanism proposed | PASS | "Mechanism" field per source inside the falsification block with three sentence templates; fires inside the per-source analysis context |
| C-10 | Scope and validity | PASS | SYNTHESIS.Scope (C-10) field with "at least one explicit boundary condition" |
| C-11 | Per-source structured format | PASS | Per-source blocks with 8 labeled fields; each essential obligation occupies a named field; "numbered block with labeled fields qualifies" — labeled-field blocks satisfy the pass condition |
| C-12 | Null/falsification framing | PASS | Strongest C-12 coverage: per-source falsification block with source-specific null condition ("if the hypothesis were false, what would THIS specific source show?") + observed + null verdict — richer than V-01/V-05's shared null expectation |
| C-13 | Vocabulary precision | FAIL | "Relationship type" field has fixed three-option vocabulary, but SYNTHESIS and QUANTIFIED CLAIMS sections have no vocabulary contract covering them; hedged terms can appear in synthesis narrative |

**Score: 60 + 30 + (5+5+5+5+0) = 110/115**

---

#### V-04: Mechanism-Front-Loaded Analysis

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Source" field in PHASE 2: "Specific named artifact...Not 'the data'" |
| C-02 | Pattern stated | PASS | "Pattern found" field: "No pattern detected" if none, no hedging |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" field: "Explicit link — do not leave it implicit" |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" field derived from mechanism status with three options; causal claim flows from mechanism verdict |
| C-05 | Strength assessed | PASS | "Strength" field: tier + number/rate/N of M/effect size/argument |
| C-06 | Multiple sources | PASS | "Minimum two sources required" |
| C-07 | Counter-patterns | PASS | "Counter-evidence" per source + SYNTHESIS.Disconfirming data |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required] |
| C-09 | Causal mechanism proposed | PASS | Most thorough C-09 coverage: mechanism is the organizing frame — PHASE 1 requires mechanism prediction before any source; PHASE 2 adjudicates per-source confirmation; PHASE 3 renders mechanism verdict |
| C-10 | Scope and validity | PASS | SYNTHESIS.Scope (C-10) field |
| C-11 | Per-source structured format | PASS | PHASE 2 per-source blocks have 8 labeled fields covering all essential obligations; "numbered block with labeled fields qualifies" — labeled-field block structure satisfies the pass condition |
| C-12 | Null/falsification framing | FAIL | "Expected if mechanism operates" is confirmatory framing, not falsification framing; no null expectation stated; "Mechanism not confirmed" handles disconfirmation but does not ask "if hypothesis were FALSE, what would this source show?" — pass condition requires explicit falsification sentence |
| C-13 | Vocabulary precision | FAIL | "Relationship type" field enforces vocabulary within that field only; PHASE 1, PHASE 3, and SYNTHESIS narrative have no vocabulary contract or compliance check |

**Score: 60 + 30 + (5+5+5+0+0) = 105/115**

---

#### V-05: Full Aspirational Stack

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Source named | PASS | "Source" column: "Specific named artifact...not 'the data'...if you cannot name it, do not add a row" |
| C-02 | Pattern stated | PASS | "Pattern found" column: "No pattern detected" if none, no hedging |
| C-03 | Hypothesis connection | PASS | "Hypothesis bearing" column: "Explicit link. One to two sentences. Do not leave implicit." |
| C-04 | Correlation vs causal labeled | PASS | "Relationship type" column: ONLY vocabulary contract terms; C-04 and C-13 co-enforced by same column |
| C-05 | Strength assessed | PASS | "Strength" column: tier + number/rate/count/argument |
| C-06 | Multiple sources | PASS | "Minimum two rows required" |
| C-07 | Counter-patterns | PASS | Dual guarantee: "Null met" rows ARE counter-patterns by table structure + COUNTER-PATTERN SUMMARY [Required] collects them separately; C-07 cannot be missed without also violating the table |
| C-08 | Quantified claims | PASS | QUANTIFIED CLAIMS [Required] with numeric floor; pre-printed "N of M analyzed sources met the null expectation" template |
| C-09 | Causal mechanism proposed | PASS | MECHANISM ANALYSIS [Required] with three sentence templates + mechanism verdict ("established/plausible/ruled out/untestable"); mechanism verdict feeds directly into VERDICT.Causal claim |
| C-10 | Scope and validity | PASS | VERDICT.Scope field: "state at least one explicit boundary condition...do not omit" |
| C-11 | Per-source structured format | PASS | 6-column table; all five essential obligations in named columns; the aspirational criterion's pass condition is structurally guaranteed by the table header |
| C-12 | Null/falsification framing | PASS | Null expectation pre-stated in HYPOTHESIS AND FALSIFICATION SETUP; "Null expectation met?" column per row; COUNTER-PATTERN SUMMARY harvests null-met rows; null framing and mechanism prediction co-located in setup section, making them reinforce each other |
| C-13 | Vocabulary precision | PASS | VOCABULARY CONTRACT (forbidden terms explicitly listed + required replacements) + "Relationship type" column restricted to contract terms + VOCABULARY COMPLIANCE REVIEW before VERDICT auditing "all Relationship type cells, mechanism entries, and counter-pattern sentences" — extends enforcement beyond table column to all non-table sections |

**Score: 60 + 30 + (5+5+5+5+5) = 115/115**

---

### Composite Scores and Ranking

| Rank | Variation | Essential (60) | Recommended (30) | Aspirational (25) | Total | vs Predicted |
|------|-----------|----------------|------------------|-------------------|-------|-------------|
| 1 | V-05 Full Aspirational Stack | 60 | 30 | 25 | **115** | = predicted |
| 2 | V-01 Prescribed Hybrid | 60 | 30 | 20 | **110** | = predicted |
| 2 | V-03 Per-Source Falsification | 60 | 30 | 20 | **110** | = predicted |
| 4 | V-02 Vocabulary-Locked Table | 60 | 30 | 15 | **105** | = predicted |
| 4 | V-04 Mechanism-Front-Loaded | 60 | 30 | 15 | **105** | +15 vs predicted 90 |

**V-04 re-score note:** The predicted 90/115 implied lost recommended points that the template does not actually lose — QUANTIFIED CLAIMS [Required] is present, COUNTER-PATTERNS are covered via "Counter-evidence" per source. C-11 is borderline but "numbered block with labeled fields qualifies" applies to V-04's per-source labeled-field structure. Score is 105, not 90.

**All-essential-pass:** True across all five variations — consistent with R1 finding that per-source labeled-field structure is sufficient to guarantee C-01 through C-05 in every structural form tested.

---

### C-13 Gap Analysis

The C-13 failure mode is the same across V-01, V-03, V-04: a named column/field enforces vocabulary within that cell, but non-table narrative sections (mechanism descriptions, synthesis paragraphs, verdict sentences) have no enforcement. The model can write "This appears to suggest a connection" in the MECHANISM section of V-01 without violating any structural constraint. V-02 and V-05 close this by:

1. Pre-printing a FORBIDDEN TERMS list (visible at template fill-in time)
2. Explicitly extending the contract to "table cells, mechanism entries, counter-pattern entries, and verdict sentences"
3. Adding a COMPLIANCE REVIEW step that requires the model to audit its own output before proceeding

This three-layer structure is the C-13 structural guarantee. A column header alone ("Relationship type [ONLY vocabulary contract terms]") enforces that one column — it cannot reach prose text.

---

### Excellence Signals from V-05

These are the structural patterns in V-05 that do not appear in R1's excellence signals:

**1. Vocabulary contract extended globally, not just to the table column**
R1 identified "table columns eliminate criteria bleeding" — but column enforcement only covers one cell per row. V-05's VOCABULARY CONTRACT applies to ALL output text and the COMPLIANCE REVIEW audits non-table sections. The insight: a column header is a narrow structural guarantee; a named contract section covering the entire output is a global one.

**2. Mechanism verdict as synthesis artifact, not supplementary content**
V-01 requires a MECHANISM sentence per source. V-05 goes further: MECHANISM ANALYSIS renders a verdict ("Mechanism established / plausible / ruled out / untestable") that is explicitly cited in VERDICT.Causal claim. Mechanism content is load-bearing for the verdict computation, not an appendix. This makes C-09 matter structurally — it cannot be skimmed because the verdict field requires its output.

**3. Null expectation and mechanism prediction co-located in a preamble setup section**
V-01 states the null expectation once before the table. V-05 co-locates the null expectation AND the proposed mechanism in a single HYPOTHESIS AND FALSIFICATION SETUP section. This forces the model to commit to both what it expects (mechanism) and what failure would look like (null) before examining any source — falsification framing and mechanism prediction reinforce each other rather than competing for structural attention.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["vocabulary contract extended to ALL output text via named FORBIDDEN TERMS section plus compliance review step -- column header alone only enforces one cell per row; a named contract section is a global structural guarantee", "mechanism verdict as synthesis artifact: requiring a verdict field (established/plausible/ruled out/untestable) that feeds directly into VERDICT.Causal claim makes C-09 load-bearing rather than supplementary -- mechanism content cannot be skimmed because the verdict computation depends on it", "null expectation and mechanism prediction co-located in a preamble setup section before any source is named -- pairing falsification framing and mechanism prediction in one structural block forces simultaneous commitment to both, preventing post-hoc rationalization of either"]}
```
