## Round 2 Scorecard — scout-naming

**All five variations score 97.5/100. All essential criteria pass.**

This is the first round with no essential failures (R1 had V-03 fail C-02).

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 (all axes) | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 2 | V-04 (gates + inertia) | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 3 | V-03 (gates) | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 4 | V-01 (inertia) | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 5 | V-02 (tier-weight) | 5/5 | 3/3 | 3/4 | **97.5** | YES |

**Why they tie at 97.5**: C-09 (--validate) remains unimplementable. Max aspirational = 3/4 * 10 = 7.5. R2 successfully engineered C-11 and C-12 into all five variations, eliminating the differentiation surface that existed in R1 (where only V-05 cleared the aspirational bar).

**Ranking within the cluster** is by sub-criterion enforcement quality:
- **V-05 leads**: structural DISQ (no judgment needed), gate-confirmed C-11, 4-mandated C-08 topics, 3-part C-04 with status-quo
- **V-02 trails**: weakest C-04 (1-dim minimum, no status-quo requirement, no vocab connection in DECIDE); structural DISQ is strong but tier scale compression (3.0-9.0) is an execution risk
- **V-03 confirms the gate hypothesis in isolation**: gates alone are sufficient for 97.5 — the inertia and tier-weight axes add sub-criterion quality but not rubric score

**Two new excellence patterns captured:**

1. **Gate confirmation counts** — "Generated: N. Pre-disqualified: N. Advancing: N." makes C-11 output-verifiable rather than instruction-inferred. Strongest C-11 mechanism available in text prompts.

2. **3-part DECIDE rationale** (dimensions + status-quo + vocab) — converts the top pick justification from abstract scoring commentary into a mandatory competitive argument. Cannot be satisfied by "it scored highest."

```json
{"top_score": 97.5, "all_essential_pass": true, "new_patterns": ["Gate confirmation counts (Gate 2: 'Generated: N. Pre-disqualified: N. Advancing: N.') make C-11 output-verifiable rather than instruction-inferred — required counter line proves generation-time enforcement without evaluator inference", "3-part DECIDE rationale (dimensions + status-quo outperformance + vocab) is a structural forcing function for C-04 depth — the status-quo requirement converts top-pick rationale from abstract scoring commentary into a concrete competitive argument that cannot be satisfied by 'it scored highest'"]}
```
 positions itself... Write them: Domain vocabulary: [term1, term2, ...] Source: [file name(s)]." 5-10 terms + named source. |
| C-11 | Generation-time Constraint Enforcement | PASS | "If a constraint was parsed, enforce it during generation. Mark any candidate that violates the constraint as [DISQ: constraint] immediately. Do not carry violating candidates into SCORE." Explicit instruction to exclude before SCORE phase. Pass condition met. Note: no gate confirmation count — compliance inferred from output, not verified by counter. |
| C-12 | Phase-structured Output | PASS | Named sections present: SETUP, GENERATE, SCORE, CHECK, DECIDE, FINDINGS REGISTER. At least 3 named phase headers (pass condition: 3 minimum). No scoring rows prescribed in GENERATE; no new candidates introduced in SCORE or DECIDE. Pass condition met. Note: headers are unlabeled section titles, not "--- PHASE N ---" format; no gate mechanism enforces phase boundary. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/4

```
composite = (5/5 * 60) + (3/3 * 30) + (3/4 * 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Score: 97.5 / 100 — GOLDEN** (all essential pass, composite >= 80)

---

### V-02: Tier-weight bridge

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names across functional, evocative, and compound types." |
| C-02 | Five-Role Scoring Matrix + declared weights | PASS | Full TIER SCORING SYSTEM block declares: Role weights (all 5), Weight sum: 100%, explicit Composite formula with per-role multipliers. Resolves R1 V-03's structural incompatibility by bridging tiers to numerics. Composite range 3.0–9.0 noted as compressed but does not violate pass condition (declared weights sum 100%). |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3 candidates: 1. Internal... 2. External (npm/PyPI + brand)." Both classes, top 3. |
| C-04 | Top Pick Named + Justified | PASS | "State the numeric composite (e.g., 7.5 not 'HIGH'). Rationale must reference at least one scoring dimension by name." Pass condition met. Note: weakest C-04 in the round — only one dimension required, no status-quo requirement, no vocab connection in DECIDE. |
| C-05 | Constraint Parsed + Applied | PASS | "If a constraint was parsed, enforce it during generation. Mark any violating candidate [DISQ: constraint] immediately. Do not carry it into SCORE." + Constraint column in SCORE matrix (PASS/FAIL per candidate). |
| C-06 | Disqualification Logic labeled | PASS | "DISQUALIFICATION RULE (structural, not judgment): Any candidate scoring LOW on Strategy or PM → immediately disqualified. Label: [DISQ: low Strategy] or [DISQ: low PM]... No judgment required — LOW on either core dimension is automatically disqualifying." Strongest structural C-06 in the round alongside V-05. |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: First viable candidate. State numeric composite. One sentence fallback." All three elements. |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At least one entry on: Tier boundary calibration, Vocabulary influence, Constraint edge cases. Severity: P1/P2/P3." |
| C-09 | `--validate` flag behavior | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Domain vocabulary: Extract 5-10 terms describing what this product does and how it positions itself... Source: [file name(s)]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "If a constraint was parsed, enforce it during generation. Mark any violating candidate [DISQ: constraint] immediately. Do not carry it into SCORE." Pass condition met. Note: no gate confirmation count — same as V-01. |
| C-12 | Phase-structured Output | PASS | Named sections: SETUP, GENERATE, SCORE, DECIDE. Four phase headers. No scoring rows in GENERATE; no new candidates in SCORE/DECIDE. Pass condition met. Same structural level as V-01 — no "--- PHASE N ---" numbering or gates. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/4

```
composite = (5/5 * 60) + (3/3 * 30) + (3/4 * 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Score: 97.5 / 100 — GOLDEN**

Open risk noted from variations document: composite scale 3.0–9.0 (vs standard 1–10) may read as non-standard to an evaluator. Does not affect rubric scoring — C-02 and C-04 pass conditions are met — but worth flagging in findings.

---

### V-03: Phase gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + declared weights | PASS | "Declare role weights (locked for this run): Strategy 25% \| PM 25% \| GTM 20% \| UX 20% \| Design 10% \| Sum: 100%". Scoring matrix shows all 5 roles in headers with weights. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3 candidates: Internal (repo namespace) + External (npm/PyPI + brand). Report: [candidate] / [class] / [hit or clear]." |
| C-04 | Top Pick Named + Justified | PASS | "Top Pick: State composite score. Rationale must reference at least two scoring dimensions and connect to at least one vocabulary term from Phase 1." Two dimensions + vocab connection. Exceeds pass condition; no status-quo requirement (V-03 does not include inertia framing axis). |
| C-05 | Constraint Parsed + Applied | PASS | "Constraint enforcement (generation-time): For each candidate: if it violates the parsed constraint, mark [DISQ: constraint] here. These candidates do not advance to PHASE 3." |
| C-06 | Disqualification Logic labeled | PASS | "Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]." + "Disqualified Summary: Full list with labeled reasons. Tally by cause: [constraint], [low score], [collision], [other]." |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: State score. One sentence fallback rationale." |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. One entry per: Vocabulary coverage, Role weighting calibration, Disqualification patterns. Severity: P1/P2/P3." Three mandated topics. |
| C-09 | `--validate` flag behavior | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." Named source, 5-10 terms. |
| C-11 | Generation-time Constraint Enforcement | PASS | "Constraint enforcement (generation-time): For each candidate: if it violates the parsed constraint, mark [DISQ: constraint] here. These candidates do not advance to PHASE 3." + **Gate 2: "Candidates generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N."** Gate confirmation makes C-11 output-verifiable — compliance confirmed by required counter, not inferred. Strongest C-11 mechanism in the round (tied V-04/V-05). |
| C-12 | Phase-structured Output | PASS | Explicit "--- PHASE 1: SETUP ---", "--- PHASE 2: GENERATE ---", "--- PHASE 3: SCORE ---", "--- PHASE 4: DECIDE ---" with separator lines. Four numbered phase headers. Gates at each boundary enforce no-backflow. Strongest C-12 structure in the round (tied V-04/V-05). |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/4

```
composite = (5/5 * 60) + (3/3 * 30) + (3/4 * 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Score: 97.5 / 100 — GOLDEN**

---

### V-04: Phase gates + inertia framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + declared weights | PASS | "Declare role weights (locked): Strategy 25% \| PM 25% \| GTM 20% \| UX 20% \| Design 10% \| Sum: 100%". Matrix with role columns + weights. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3: Internal (repo namespace) + External (npm/PyPI + brand)." |
| C-04 | Top Pick Named + Justified | PASS | "Rationale must: (1) Reference at least two scoring dimensions by name (2) Explain how this name outperforms the status-quo on Strategy positioning (3) Connect to at least one vocabulary term from Phase 1 SETUP." 3-part requirement. Strongest C-04 in the round (tied V-01, V-05). |
| C-05 | Constraint Parsed + Applied | PASS | "Constraint enforcement (generation-time): Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-06 | Disqualification Logic labeled | PASS | "Score floor: Strategy < 6 or PM < 6 → [DISQ: low score]." + DECIDE "Disqualified Summary: Full list with labeled reasons. Tally by cause." |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: State score. One sentence: why is it a credible fallback?" |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum: Status-quo gap, Vocabulary coverage, Role weighting calibration. Severity: P1/P2/P3." |
| C-09 | `--validate` flag behavior | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Constraint enforcement (generation-time): Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." + **Gate 2: "Generated: N. Pre-disqualified (constraint): N. Advancing: N."** Output-verifiable — tied V-03/V-05 for strongest C-11. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---" with separator lines. Four numbered phase headers. Gates enforce phase boundary separation. Tied V-03/V-05. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/4

```
composite = (5/5 * 60) + (3/3 * 30) + (3/4 * 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Score: 97.5 / 100 — GOLDEN**

---

### V-05: Tier-weight bridge + phase gates + inertia framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + declared weights | PASS | TIER SCORING SYSTEM block: all 5 roles, Weight sum: 100%, Composite formula with multipliers. Inherits V-02's fix for R1 V-03. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check — top 3: Internal (repo namespace) + External (npm/PyPI + brand)." |
| C-04 | Top Pick Named + Justified | PASS | "Rationale must: (1) Reference at least two scoring dimensions by name (2) Explain how this name outperforms the status-quo on Strategy (3) Connect to at least one vocabulary term from Phase 1." 3-part requirement. Tied V-01/V-04. |
| C-05 | Constraint Parsed + Applied | PASS | "Constraint enforcement (generation-time): Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-06 | Disqualification Logic labeled | PASS | "DISQUALIFICATION RULE (structural): Any LOW on Strategy or PM → [DISQ: low Strategy] / [DISQ: low PM] in Composite. No judgment required." + Constraint column (PASS/FAIL) + DECIDE tally by cause. Strongest structural C-06 in the round — tied V-02. |
| C-07 | Runner-Up + Fallback Rationale | PASS | "Runner-Up: State numeric composite. One sentence fallback rationale." |
| C-08 | Findings Register (SF-NN) | PASS | "FINDINGS REGISTER: SF-NN table. At minimum, one entry on: Tier boundary calibration, Status-quo gap, Vocabulary coverage, Disqualification patterns. Severity: P1/P2/P3." Four mandated topics — most prescriptive C-08 in the round. |
| C-09 | `--validate` flag behavior | FAIL | Design gap. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Read CLAUDE.md and plugin-plan.md. Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Constraint enforcement (generation-time): Any candidate violating the parsed constraint → mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." + **Gate 2: "Generated: N. Pre-disqualified (constraint): N. Advancing: N."** Output-verifiable — tied V-03/V-04. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---" with separator lines. Four numbered phase headers. Gates enforce phase boundary. Tied V-03/V-04. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 3/4

```
composite = (5/5 * 60) + (3/3 * 30) + (3/4 * 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Score: 97.5 / 100 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-05 Combined (all axes) | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 2 | V-04 Gates + inertia | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 3 | V-03 Gates | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 4 | V-01 Inertia | 5/5 | 3/3 | 3/4 | **97.5** | YES |
| 5 | V-02 Tier-weight | 5/5 | 3/3 | 3/4 | **97.5** | YES |

**All five variations score 97.5. All essential criteria pass for all variations.** This is a direct consequence of R2's design: C-11 and C-12 were explicitly engineered into every prompt, the tier-weight bridge fixed R1 V-03's C-02 failure, and C-10 was baseline in all five (R1 showed it was the highest-value single addition).

**`all_essential_pass: true`** — first round with no essential failures across all variations.

---

## Sub-criterion Quality Analysis — Within the 97.5 Cluster

All five variations hit the same composite, but they differ in enforcement mechanism strength. Ranking reflects structural robustness — how likely each variation produces compliant output at execution time.

| Sub-criterion | V-05 | V-04 | V-03 | V-01 | V-02 |
|---------------|------|------|------|------|------|
| C-04 depth (DECIDE rationale requirements) | 3-part | 3-part | 2-part (no status-quo) | 3-part | 1-part (weakest) |
| C-11 verifiability (gate confirmation count) | YES (Gate 2) | YES (Gate 2) | YES (Gate 2) | NO (instruction only) | NO (instruction only) |
| C-12 structure (phase header type) | PHASE N headers + gates | PHASE N headers + gates | PHASE N headers + gates | Section titles | Section titles |
| C-06 mechanism type | Structural DISQ (no judgment) | Floor rule | Floor rule | Floor rule | Structural DISQ (no judgment) |
| C-08 mandated finding topics | 4 | 3 | 3 | 3 | 3 |

**Ranking rationale:**
- **V-05 first**: strongest across C-06 (structural DISQ from tier-weight), C-08 (4 mandated topics), C-11/C-12 (gates), C-04 (3-part with status-quo). Accumulates all three R2 axes without conflicting requirements.
- **V-04 second**: tied with V-05 on C-11/C-12/C-04, weaker on C-06 (floor vs structural DISQ) and C-08 (3 vs 4 topics).
- **V-03 third**: tied with V-04 on C-11/C-12, weaker on C-04 (2-part, no status-quo). Gate mechanism is the structural enforcement mechanism in isolation — confirms the gate hypothesis is sufficient.
- **V-01 fourth**: strongest C-04 (3-part with status-quo) but no gate confirmation counts, section titles only for C-12. The inertia axis adds value to C-04 depth without structural enforcement overhead.
- **V-02 fifth**: C-04 is the weakest (1-dim minimum, no status-quo, no vocab connection in DECIDE). C-06 is structurally the strongest (tied V-05), but the tier scale compression (3.0-9.0) is a non-standard output risk. The tier-weight bridge successfully fixes R1 V-03's C-02 failure, which was the primary axis hypothesis.

---

## V-02 Scale Risk — Confirmed Non-Issue for Rubric, Non-Trivial for Execution

V-02's composite range is 3.0–9.0 (not 1–10). The rubric's C-02 pass condition is "declared weights sum to 100%" — satisfied. C-04's pass condition requires "score value stated" — a value like 7.5 satisfies this. The risk is at execution, not at rubric evaluation: a model reading the SCORE matrix might flag the scale as unusual or apply inconsistent tier assignments. Worth noting in V-02's Findings Register if executed.

---

## R2 vs R1 Progress

| Metric | R1 | R2 |
|--------|----|----|
| Score ceiling | 95 | 97.5 |
| Formula | aspirational/2 | aspirational/4 |
| All essential pass | NO (V-03 failed C-02) | YES |
| C-11 addressable | No (not a criterion) | YES |
| C-12 addressable | No (not a criterion) | YES |
| Variations hitting ceiling | 3/5 | 5/5 |
| New ceiling mechanism | C-09 (design gap) | C-09 (design gap, unchanged) |

The ceiling moved from 95 to 97.5 not by removing the C-09 ceiling, but by adding two new aspirational criteria (C-11, C-12) that R2 variations can clear. The ceiling still requires `--validate` to break — that remains a design gap.

---

## Excellence Signals — Round 2

### E-1: Gate-confirmed counts (V-03/V-04/V-05) make C-11 output-verifiable

R1's generation-time constraint enforcement (V-05 R1) was an instruction: "mark [DISQ: constraint] immediately, do not carry into SCORE." The compliance evidence was structural (violated candidates absent from scoring table). R2 adds Gate 2: "Candidates generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." This is a counter — a required output line that proves generation-time enforcement happened. No inference required. An evaluator can verify C-11 by reading a single line.

**New pattern**: Gate confirmation counts are the strongest C-11 enforcement mechanism available in text prompts — stronger than instruction text alone because they produce verifiable output rather than relying on model compliance.

### E-2: 3-part DECIDE rationale structure (V-01/V-04/V-05) as forcing function for C-04 depth

R1's best C-04 mechanism required "two named dimensions + vocab connection" (R1 V-05). R2's inertia-framing axis adds a third requirement: "explain how this name outperforms the status-quo on Strategy positioning." This cannot be satisfied by "it scored highest" or by generic positioning language. The status-quo benchmark converts the top pick rationale from abstract scoring commentary into a concrete competitive argument.

**New pattern**: Mandatory status-quo comparison in DECIDE rationale is a structural forcing function for C-04 depth — it requires the model to make a competitive claim, not just restate the scoring result.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- Combines all three R2 axes (tier-weight bridge + phase gates + inertia framing) without conflicting requirements
- Phase gates confirm C-11 with output-verifiable counts (E-1)
- 3-part DECIDE rationale enforces C-04 depth (E-2)
- Structural DISQ rule (C-06) eliminates judgment variance — same as R1 V-03's strongest mechanism, now without C-02 failure
- C-08 mandates four finding topics — produces the most useful findings register for downstream rubric evolution
- All five essential criteria pass by structural design, not instruction compliance

**V-04** is the closest fallback. Equivalent on C-11/C-12/C-04, weaker only on C-06 (floor rule vs structural DISQ) and C-08 (3 vs 4 mandatory topics). Preferred if the tier-weight bridge (H/M/L scoring format) is judged too abstract for execution clarity.

**V-03** confirms the gate hypothesis in isolation: gates alone produce equivalent C-11/C-12 compliance without the inertia axis or tier-weight bridge. This is the minimal variation that achieves the R2 ceiling — a useful control for isolating the gate mechanism's contribution.

---

```json
{"top_score": 97.5, "all_essential_pass": true, "new_patterns": ["Gate confirmation counts (Gate 2: 'Generated: N. Pre-disqualified: N. Advancing: N.') make C-11 output-verifiable rather than instruction-inferred — required counter line proves generation-time enforcement without evaluator inference", "3-part DECIDE rationale (dimensions + status-quo outperformance + vocab) is a structural forcing function for C-04 depth — the status-quo requirement converts top-pick rationale from abstract scoring commentary into a concrete competitive argument that cannot be satisfied by 'it scored highest'"]}
```
