Scorecard written. Here's the summary:

---

## scout-naming R3 — Score Summary

**All 5 variations: 98.3/100** (R3 target hit, up from R2's 97.5)

| Rank | Variation | Aspirational cleared | Score |
|------|-----------|----------------------|-------|
| 1 | V-05 (all R2 + labeled C-14) | C-10/C-11/C-12/C-13/C-14 | 98.3 |
| 2 | V-04 (UX-first + labeled C-14) | C-10/C-11/C-12/C-13/C-14 | 98.3 |
| 3 | V-03 (labeled C-14) | C-10/C-11/C-12/C-13/C-14 | 98.3 |
| 4 | V-01 (UX-first, inline C-14) | C-10/C-11/C-12/C-13/C-14 | 98.3 |
| 5 | V-02 (conversational, inline C-14) | C-10/C-11/C-12/C-13/C-14 | 98.3 |

**Two new patterns:**

1. **Labeled record structure** (V-03/V-04/V-05) — explicit `(1) Dimensions / (2) vs. Status-quo / (3) Vocabulary` sub-lines convert C-14 from instruction-inferred to output-verifiable. A missing sub-part is a visible structural gap.

2. **Gate 3 binary status flag** (V-03/V-04/V-05) — `"Status-quo benchmarked: yes/no"` generalizes the gate pattern from counts to cross-phase consistency flags.

**Confirmed hypotheses:** role sequence (UX-first) and phrasing register (conversational) are both neutral on compliance — neither moves the score. Structural gates + labeled output records are the compliance driver.

**Ceiling unchanged at 98.3** until `--validate` (C-09) is implemented.

```json
{"top_score": 98.3, "all_essential_pass": true, "new_patterns": ["Labeled record structure for multi-part rationale (TOP PICK with explicit (1) Dimensions / (2) vs. Status-quo / (3) Vocabulary sub-lines) converts C-14 from instruction-inferred to output-verifiable — a missing sub-part is a visible structural gap, not an omitted clause in prose. The record form should be preferred over inline instructions for any criterion requiring multiple distinct elements in the same output block.", "Gate 3 extended with binary status flag ('Status-quo benchmarked: yes/no') encodes a cross-phase consistency check — model must confirm the prior-phase artifact exists before DECIDE proceeds. This generalizes the Gate 2 count pattern: gates can carry both counters (how many advanced) and flags (did a required prior step complete)."]}
```
e GENERATE. |
| C-11 | Generation-time Constraint Enforcement | PASS | "mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." Instruction-based enforcement. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four numbered phase separators with gate boundaries. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." Three-value counter present. C-11 output-verifiable. |
| C-14 | 3-part DECIDE Rationale | PASS | Rationale requirements: (1) two dimensions by name, (2) status-quo Strategy outperformance, (3) vocab connection. Inline 3-part form — all elements present. Note: prose instructions, not labeled sub-part record. A missing element detectable only by reading prose, not by inspecting structure. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6 (C-09 fails)

```
composite = (5/5 × 60) + (3/3 × 30) + (5/6 × 10)
          = 60 + 30 + 8.3
          = 98.3
```

**Score: 98.3 / 100 — GOLDEN**

---

### V-02: Phrasing register (conversational)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "You will produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | "Role weights are fixed for this run: Strategy: 25% \| PM: 25% \| GTM: 20% \| UX: 20% \| Design: 10%. Sum: 100%." Formula explicit. Matrix header lists all 5 columns. |
| C-03 | Collision Check (namespace + external) | PASS | "run a collision check on the top 3 candidates: Internal: any namespace conflict... External: npm/PyPI... Report: [candidate] / [class] / [hit or clear]." Both classes, top 3. |
| C-04 | Top Pick Named + Justified | PASS | "(1) At least two scoring dimensions — name them... (2) How this name beats the status-quo on positioning... (3) A connection to at least one vocabulary term..." Conversational framing, all elements present. |
| C-05 | Constraint Parsed + Applied | PASS | "check each candidate against it during generation. Any candidate that violates the constraint gets labeled [DISQ: constraint] here and does not advance to scoring." |
| C-06 | Disqualification Logic Labeled | PASS | "If a candidate scores below 6 on Strategy or PM, label it [DISQ: low score] in the Composite column — this is a structural rule, not a judgment call." Rule stated explicitly. Tally in DECIDE. |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: Name it and state its composite score. One sentence on why it is the fallback." All three elements. |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum one entry on: Status-quo gap, Vocabulary coverage, Role weighting calibration. Severity: P1/P2/P3." |
| C-09 | `--validate` flag | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "extract 5-10 vocabulary terms... Domain vocabulary: [term1, term2, ...] Source: [file name(s)]." Named source, 5-10 terms. |
| C-11 | Generation-time Constraint Enforcement | PASS | "check each candidate against it during generation. Any candidate that violates the constraint gets labeled [DISQ: constraint] here and does not advance to scoring." Instruction-based. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four phase headers. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." Three-value counter present. C-11 output-verifiable. |
| C-14 | 3-part DECIDE Rationale | PASS | "(1) At least two scoring dimensions... (2) How this name beats the status-quo on positioning... (3) A connection to at least one vocabulary term..." Conversational framing, inline 3-part. All three elements present. Same verification risk as V-01 — prose form, not labeled record. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6

```
composite = 60 + 30 + 8.3 = 98.3
```

**Score: 98.3 / 100 — GOLDEN**

Sub-criterion note: Phrasing register (conversational) is neutral on compliance — all structural requirements pass at identical strength to imperative-register variations. Hypothesis confirmed: instructional voice does not affect structural enforcement outcomes.

---

### V-03: C-14 labeled sub-parts

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | "Strategy 25% \| PM 25% \| GTM 20% \| UX 20% \| Design 10% \| Sum: 100%." Formula explicit. All 5 columns in matrix. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3: Internal (repo namespace) + External (npm/PyPI + brand). Report: [candidate] / [class] / [hit or clear]." |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK record contains Name, Score, and explicitly labeled sub-parts (1)/(2)/(3). Well above essential bar. |
| C-05 | Constraint Parsed + Applied | PASS | "Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-06 | Disqualification Logic Labeled | PASS | "Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]. Label in Composite column." DISQUALIFIED SUMMARY with tally by cause. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP section: Name, Score, "Fallback rationale: [One sentence — why is this a credible alternative?]" |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum one entry on: Status-quo gap, Vocabulary coverage, Role weighting calibration. Severity: P1/P2/P3." |
| C-09 | `--validate` flag | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." Instruction-based. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four numbered phase separators. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." GATE 3 extended: "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3." Multi-gate confirmation — Gate 3 adds binary status flag. |
| C-14 | 3-part DECIDE Rationale | PASS | TOP PICK section contains explicitly labeled sub-parts: `(1) Dimensions: [...]`, `(2) vs. Status-quo: [...]`, `(3) Vocabulary: [...]` as distinct named lines. Strongest C-14 form — a missing sub-part is a visible gap in the output record, not an omitted clause in prose. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6

```
composite = 60 + 30 + 8.3 = 98.3
```

**Score: 98.3 / 100 — GOLDEN**

Sub-criterion note: Gate 3 now includes status-quo benchmarking confirmation (`Status-quo benchmarked: yes/no`) — an implicit C-13 extension not present in V-01/V-02. Strongest C-14 verification mechanism in the round.

---

### V-04: Combined (role sequence + labeled C-14)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | UX-first column order: UX 20% \| PM 25% \| GTM 20% \| Strategy 25% \| Design 10% \| Sum 100%. Formula explicit. All 5 columns. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3: Internal (repo namespace) + External (npm/PyPI + brand)." |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK record with labeled (1) Dimensions, (2) vs. Status-quo, (3) Vocabulary. Sub-part (1) adds: "If UX and Strategy scores diverged, address that tension explicitly" — C-04 with scoring-frame awareness. |
| C-05 | Constraint Parsed + Applied | PASS | "Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-06 | Disqualification Logic Labeled | PASS | "Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]. Label in Composite column." DISQUALIFIED SUMMARY with tally. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP section: Name, Score, "Fallback rationale: [One sentence.]" |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum one entry on: UX-first scoring effect, Status-quo gap, Vocabulary coverage. Severity: P1/P2/P3." |
| C-09 | `--validate` flag | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Any candidate violating the parsed constraint → mark [DISQ: constraint] here." Instruction-based. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four numbered phase separators. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." GATE 3: "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3." Multi-gate extended. |
| C-14 | 3-part DECIDE Rationale | PASS | Labeled sub-parts: `(1) Dimensions: [... If UX and Strategy scores diverged, address that tension explicitly.]`, `(2) vs. Status-quo: [...]`, `(3) Vocabulary: [...]`. All three as distinct labeled lines. Sub-part (1) cross-references the UX-first scoring frame — strongest coupling of scoring axis to rationale format. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6

```
composite = 60 + 30 + 8.3 = 98.3
```

**Score: 98.3 / 100 — GOLDEN**

Sub-criterion note: The UX-first + labeled C-14 combination is the most analytically productive R3 axis pair. Sub-part (1) must name the UX/Strategy trade-off if one occurred, producing the most informative DECIDE output when the scoring frame surfaces a genuine tension.

---

### V-05: Combined — all R2 axes + labeled C-14

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | TIER SCORING SYSTEM block: all 5 roles, Weight sum 100%, formula with multipliers, range 3.0–9.0 declared. Inherits R2 V-02's numeric bridge fix. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3: Internal (repo namespace) + External (npm/PyPI + brand)." |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK record: Name, Score (numeric composite required), labeled (1)/(2)/(3) sub-parts. Strongest output format in the round. |
| C-05 | Constraint Parsed + Applied | PASS | Generation-time enforcement instruction + Constraint column in SCORE matrix (PASS/FAIL per candidate). Dual-mechanism. |
| C-06 | Disqualification Logic Labeled | PASS | "DISQUALIFICATION RULE (structural, not judgment): Any LOW on Strategy or PM → [DISQ: low Strategy] or [DISQ: low PM]. No judgment required." Strongest C-06 in the round — tied R2 V-02/V-05. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP section: Name, Score (numeric composite), "Fallback rationale: [One sentence.]" |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum one entry on: Tier boundary calibration, Status-quo gap, Vocabulary coverage, Disqualification patterns." Four mandated topics — most prescriptive C-08 in the round. |
| C-09 | `--validate` flag | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." + GATE 2 counter + Constraint matrix column. Triple-signal verification — strongest C-11 in the round. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four numbered phase separators with gates. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." GATE 3: "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3." Multi-gate extended. |
| C-14 | 3-part DECIDE Rationale | PASS | Labeled sub-parts: `(1) Dimensions: [... state the specific rationale for each tier assigned...]`, `(2) vs. Status-quo: [...]`, `(3) Vocabulary: [...]`. Sub-part (1) requires tier-specific rationale (e.g., "Strategy: HIGH — signals X clearly"), adding precision over generic dimension reference. No conflict between tier-weight bridge and labeled sub-part structure confirmed. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 5/6

```
composite = 60 + 30 + 8.3 = 98.3
```

**Score: 98.3 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 (all R2 axes + labeled C-14) | 5/5 | 3/3 | 5/6 | **98.3** | YES |
| 2 | V-04 (role sequence + labeled C-14) | 5/5 | 3/3 | 5/6 | **98.3** | YES |
| 3 | V-03 (labeled C-14) | 5/5 | 3/3 | 5/6 | **98.3** | YES |
| 4 | V-01 (role sequence, inline C-14) | 5/5 | 3/3 | 5/6 | **98.3** | YES |
| 5 | V-02 (conversational, inline C-14) | 5/5 | 3/3 | 5/6 | **98.3** | YES |

**All five variations reach 98.3 — the R3 target.** R3's contribution is not a score advance (ceiling stays at 98.3 until C-09 is implemented) but a verifiability advance: labeled sub-part form converts C-14 from an instruction-level requirement to an output-level record where a missing element is a visible structural gap.

---

## Sub-criterion Quality Analysis — Within the 98.3 Cluster

| Sub-criterion | V-05 | V-04 | V-03 | V-01 | V-02 |
|---------------|------|------|------|------|------|
| C-14 form | Labeled + tier rationale precision | Labeled + UX/Strategy tension instruction | Labeled sub-parts | Inline 3-part (R2 V-04 form) | Inline 3-part (conversational) |
| C-13 gate coverage | Gate 2 + Gate 3 extended | Gate 2 + Gate 3 extended | Gate 2 + Gate 3 extended | Gate 2 only | Gate 2 only |
| C-06 mechanism | Structural DISQ (no judgment) | Floor rule | Floor rule | Floor rule | Floor rule |
| C-08 mandated topics | 4 | 3 | 3 | 3 | 3 |
| C-11 signals | Instruction + Gate 2 + Constraint column | Instruction + Gate 2 | Instruction + Gate 2 | Instruction + Gate 2 | Instruction + Gate 2 |

**Ranking rationale:**
- **V-05 leads**: strongest C-06 (structural DISQ), C-08 (4 mandated topics), C-11 (triple-signal), C-14 (labeled + tier-precision). Structural bet resolved: no conflict between tier-weight bridge and labeled sub-parts.
- **V-04 second**: tied on C-14 form quality (labeled sub-parts); unique in coupling UX/Strategy tension explicitly to sub-part (1). Most analytically valuable DECIDE output when scoring frame produces divergence.
- **V-03 third**: labeled C-14 + Gate 3 extended — confirms that labeled sub-parts alone produce the C-14 structural advance without additional axes. Control variation for C-14 form isolation.
- **V-01 fourth**: inline 3-part C-14 (R2 V-04 carry), UX-first column. Column reordering analytically interesting but DECIDE does not mandate addressing the UX/Strategy tension without V-04's explicit divergence instruction.
- **V-02 fifth**: phrasing register confirmed as compliance-neutral. C-14 inline form satisfies rubric but lacks structural verifiability. Useful negative: conversational register does not degrade compliance.

---

## R3 vs R2 Progress

| Metric | R2 | R3 |
|--------|----|----|
| Score ceiling | 97.5 | 98.3 |
| Formula denominator | aspirational/4 | aspirational/6 |
| Variations hitting ceiling | 5/5 | 5/5 |
| New criteria cleared | C-11 + C-12 | C-13 + C-14 |
| C-14 form quality | Inline (R2 V-05 best) | Labeled sub-parts (V-03/V-04/V-05) |
| New ceiling mechanism | C-09 (design gap) | C-09 (design gap, unchanged) |

---

## Excellence Signals — Round 3

### E-1: Labeled record structure converts 3-part rationale from instruction to output-verifiable record (V-03/V-04/V-05)

R2's best C-14 mechanism embedded requirements as inline instructions within a prose paragraph. A missing element was detectable only by reading prose. R3 V-03/V-04/V-05 structure DECIDE as a named record:

```
TOP PICK
  Name: [winner]
  Score: [value]
  (1) Dimensions: [...]
  (2) vs. Status-quo: [...]
  (3) Vocabulary: [...]
```

A missing sub-part is a visible structural gap — the labeled line is absent. This is the same verification mechanism that Gate 2 provided for C-11: from "we believe it happened because no violations appeared" to "we can confirm it happened by reading a required output line."

**New pattern**: Labeled record structure for multi-part rationale requirements makes compliance verifiable by inspection. The record form should be preferred over inline instructions whenever a criterion requires multiple distinct elements in the same output block.

### E-2: Gate 3 extended with binary status flag encodes cross-phase consistency check (V-03/V-04/V-05)

R2 Gate 3: `"Surviving after score disqualification: N. Collisions checked: top 3."` R3 V-03/V-04/V-05 extend Gate 3: `"Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3."` The flag confirms the vs. Status-Quo column was completed before DECIDE — the model cannot write sub-part (2) without having identified the status-quo in SETUP.

**New pattern**: Gate confirmation can encode binary status flags (was a prior-phase artifact produced?) in addition to counts (how many items advanced). Gates are a general cross-phase consistency enforcement mechanism, not just a volume check.

### E-3: Role sequence and phrasing register are neutral on compliance; structural gates are the primary driver (V-01/V-02 confirm)

V-01 (UX-first) and V-02 (conversational) both score 98.3. Column order and instructional voice do not affect rubric compliance. Confirmed compliance driver: structural gates + labeled output records.

Secondary finding: role sequence affects output quality without affecting rubric score. V-04's UX-first + labeled C-14 coupling produces the most informative DECIDE artifact when UX and Strategy diverge — but this is not captured by any current rubric criterion. **Structural axes that do not affect rubric score can still increase output usefulness by coupling the scoring frame to required rationale content.**

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- All R2 structural advantages preserved (structural DISQ, tier-weight bridge, 4 C-08 topics, gate-confirmed C-11)
- C-14 upgraded from inline instruction to labeled output record — no conflict with tier-weight format confirmed
- Gate 3 extended with status-quo benchmarking flag
- Triple-signal C-11 verification (instruction + Gate 2 counter + Constraint matrix column)

**V-04** is the closest alternative and the most analytically productive R3 variation. UX-first + labeled C-14 is the one axis combination where a scoring-frame choice is structurally visible in the rationale. Recommended if tier-weight bridge is judged as execution risk.

**V-03** is the minimal labeled-C-14 variation. Confirms that labeled sub-parts alone produce the structural advance without additional axes — useful as a control for C-14 form isolation.

---

```json
{"top_score": 98.3, "all_essential_pass": true, "new_patterns": ["Labeled record structure for multi-part rationale (TOP PICK with explicit (1) Dimensions / (2) vs. Status-quo / (3) Vocabulary sub-lines) converts C-14 from instruction-inferred to output-verifiable — a missing sub-part is a visible structural gap, not an omitted clause in prose. The record form should be preferred over inline instructions for any criterion requiring multiple distinct elements in the same output block.", "Gate 3 extended with binary status flag ('Status-quo benchmarked: yes/no') encodes a cross-phase consistency check — model must confirm the prior-phase artifact exists before DECIDE proceeds. This generalizes the Gate 2 count pattern: gates can carry both counters (how many advanced) and flags (did a required prior step complete)."]}
```
