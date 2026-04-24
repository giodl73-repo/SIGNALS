## Round 2 Scorecard — scout-feasibility (v2 Rubric)

---

### Scoring Method

Each criterion scored PASS / PARTIAL / FAIL against the prompt design. A criterion PASSes when the instruction reliably enforces the output requirement — not just mentions it.

Formula:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

---

### Criterion-by-Criterion Evaluation

#### C-01 — Traffic light per component (essential)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 3 mandates `| Component | GREEN / YELLOW / RED | ...` table with rating as its own column |
| V-02 | PASS | Phase 5 table `| Component | Rating | Rationale | Hours |` — explicit labeled column |
| V-03 | PASS | RULE 1 explicitly prohibits prose-embedded labels; table row required |
| V-04 | PASS | Q5 table `| Component | Rating | ...` — label column explicit |
| V-05 | PASS | Phase 2 table `| Component | Rating | Rationale | Hours (from Phase 1) |` — column explicit |

#### C-02 — Composite score with label (essential)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 4 dedicated slot: "Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE" |
| V-02 | PASS | Phase 7: "Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE" |
| V-03 | PASS | RULE 6 + step 8: dedicated verdict section with score and label required |
| V-04 | PASS | Q7: "Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE" |
| V-05 | PASS | F1: "Composite score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE" |

#### C-03 — Team and timeline inference disclosed (essential)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 1 is a named slot with hard gate: "Do not write FINDING 2 until all three appear here" — contiguous, pre-scoring |
| V-02 | PASS | Phase 2 inference gate: "Do not continue until all three are visible" — contiguous block, before Phase 5 ratings |
| V-03 | PASS | RULE 2: "Scoring any component is PROHIBITED until the following block appears as a unit" — contiguous block required |
| V-04 | PASS | Q2: "Do not proceed to Q3 without all three values" — contiguous block, Q2 precedes Q5 ratings |
| V-05 | PASS | INFERENCE GATE: "Do not proceed until all three are visible" — explicit gate before PHASE 1 and PHASE 2 |

#### C-04 — Stack fallback disclosed when canonical files absent (essential)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 0 is required first: "write one sentence naming the fallback source and what was inferred" |
| V-02 | PASS | Phase 1: "If absent: name the fallback source and state what was inferred. Required." |
| V-03 | PASS | Step 1: "name the fallback source and state what was inferred. Required before step 2." |
| V-04 | PASS | Q1: "write one sentence naming the fallback file and what was inferred" |
| V-05 | PASS | SETUP: "write one sentence naming the fallback file and what was inferred. Required before the inference gate." |

#### C-05 — RED blockers enumerated with rationale (essential)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 5: required for every RED component with why + lift condition; "Omit only if no component is RED" |
| V-02 | PASS | Phase 5 inline: "Blockers (required for every RED component): [Component]: [Why blocked] -- [Lift condition]" |
| V-03 | PASS | RULE 4: "Every RED component MUST have a blocker entry: why blocked, and what specific change lifts the rating. PROHIBITED to omit." |
| V-04 | PASS | Q5: "For every RED component: why is it blocked? What would lift it?" — inline with ratings |
| V-05 | PASS | Phase 2 inline: "Blockers (required for every RED component): [Component]: [Why blocked] -- [Lift condition]" |

#### C-06 — Build-vs-buy recommendation per component (recommended)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 6: table with Build/Buy/Use existing, "Required for at least 50% of components" |
| V-02 | PASS | Phase 6: table with Build/Buy/Use existing, "Required for at least 50% of components" |
| V-03 | PASS | RULE 5: "At least 50% of components MUST carry a Build / Buy / Use existing label" |
| V-04 | PASS | Q6: table, "Required for at least 50% of components" |
| V-05 | PASS | Phase 3: table, "Required for at least 50% of components" |

#### C-07 — Scoped fallback score when NOT FEASIBLE (recommended)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 7: "Required when score < 50 (NOT FEASIBLE)... Omit if score >= 50" — conditional enforced |
| V-02 | PASS | Phase 7: "If score < 50: 'Scoped to [constraint]: [N]/100.' Required." |
| V-03 | PASS | Step 8: "Add scoped alternative if score < 50" |
| V-04 | PASS | Q7: "If score < 50: 'Scoped to [constraint]: [N]/100.' Required." |
| V-05 | PASS | F3: "[IF NOT FEASIBLE] Scoped alternative..." — condition tied to label, not just score |

#### C-08 — Prerequisites listed for FEASIBLE WITH CAVEATS (recommended)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 8: "Required when label is FEASIBLE WITH CAVEATS. Numbered list. Every RED-rated component from F3 must appear." |
| V-02 | PASS | Phase 7: "If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented" |
| V-03 | PASS | Step 8: "Add prerequisites if FEASIBLE WITH CAVEATS" |
| V-04 | PASS | Q7: "If FEASIBLE WITH CAVEATS: numbered prerequisite list, all RED items included" |
| V-05 | PASS | F4: "[IF FEASIBLE WITH CAVEATS] Prerequisites: numbered list, all RED items represented" |

#### C-09 — PM timeline overlay with complete sum-and-compare chain (aspirational)

This is the key R1 gap. All five R2 variations were designed to close it.

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 2 template has all four: "Estimated: [N] \| Available: [N] \| Delta: [+-N] \| OVER-BUDGET / UNDER-BUDGET / ON-BUDGET" — explicit template, component table above it provides the sum |
| V-02 | PASS | Phase 3 produces per-component totals. Phase 4 closes chain with all four: Estimated, Available, Delta, Flag — each on its own labeled line |
| V-03 | PASS | RULE 3 enumerates all four elements (a)-(d) explicitly; steps 3+4 sequence sum then chain; chain must close before step 5 ratings |
| V-04 | PASS | Q3 produces per-component hour table with Total. Q4: "Estimated [N from Q3] \| Available [N] \| Delta [+-N] \| OVER / UNDER / ON-BUDGET" — references Q3 explicitly, all four linked |
| V-05 | PASS | Phase 1 has component table then "Close the budget chain — all four elements required before Phase 2: Estimated: [N] \| Available: [N] \| Delta: [+-N] \| OVER-BUDGET / UNDER-BUDGET / ON-BUDGET" |

#### C-10 — Amendment actions list at close (aspirational)

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 9: component name + "State what changes in the feasibility score if completed" + example "(e.g., 'Completing this moves [Component] from RED to YELLOW, raising score ~10 pts')" |
| V-02 | PASS | Phase 8: "Each must name the specific RED or YELLOW component and state what changes in the feasibility score if the action is completed" |
| V-03 | PASS | Step 9: "Each action must state what changes in the feasibility score if completed" |
| V-04 | PASS | Q8: "State what changes in the feasibility score if the action is completed" |
| V-05 | PASS | F5: score-delta with example format: "Completing this moves [Component] from RED to YELLOW, raising score by approximately [N] pts." |

#### C-11 — Inference gate block precedes component scoring (aspirational)

R1 gap: inference scattered or post-scoring. All R2 variations address with gates before the ratings phase.

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 1 (inference) precedes FINDING 3 (ratings). "Do not write FINDING 2 until all three appear here" enforces the block |
| V-02 | PASS | Phase 2 (inference gate) precedes Phase 5 (traffic lights). "Do not continue until all three are visible" |
| V-03 | PASS | RULE 2: "Scoring any component is PROHIBITED until the following block appears as a unit." Step 2 (inference) enforced before step 5 (ratings). Block contiguity explicit |
| V-04 | PASS | Q2 (inference, contiguous, "do not proceed to Q3 without all three") precedes Q5 (ratings) |
| V-05 | PASS | INFERENCE GATE is before PHASE 1 (budget) and PHASE 2 (ratings). "Do not proceed until all three are visible" |

#### C-12 — Budget analysis precedes complexity scoring (aspirational)

R1 gap: budget computed in closing section, ratings visible without budget constraint.

| V | Result | Evidence |
|---|--------|----------|
| V-01 | PASS | FINDING 2 (budget chain, "Required before FINDING 3") precedes FINDING 3 (ratings) |
| V-02 | PASS | Phase 4 (budget chain, "required before Phase 5") precedes Phase 5 (traffic lights) — sum-first is the design axis |
| V-03 | PASS | RULE 3: "Traffic-light ratings are PROHIBITED until the budget chain appears and is closed." Steps 3+4 enumerate+close before step 5 ratings |
| V-04 | PASS | Q4 (budget chain, "Do not proceed to Q5 without the flag") precedes Q5 (ratings) |
| V-05 | PASS | PHASE 1 PM: BUDGET precedes PHASE 2 ARCHITECT: COMPLEXITY. "Traffic-light ratings are PROHIBITED before the Phase 1 chain is closed." Role-labeling makes ordering structurally visible |

---

### Composite Scores

| V | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Golden? |
|---|---------------|-----------------|------------------|-----------|---------|
| V-01 FINDINGS-mirror | 5/5 = 60 | 3/3 = 30 | 4/4 = 10 | **100** | YES |
| V-02 Sum-first | 5/5 = 60 | 3/3 = 30 | 4/4 = 10 | **100** | YES |
| V-03 Prohibitive | 5/5 = 60 | 3/3 = 30 | 4/4 = 10 | **100** | YES |
| V-04 Interrogative+sum-first | 5/5 = 60 | 3/3 = 30 | 4/4 = 10 | **100** | YES |
| V-05 Golden synthesis | 5/5 = 60 | 3/3 = 30 | 4/4 = 10 | **100** | YES |

**Round 2 outcome: All five variations score 100/100.**

---

### Rank (with enforcement-robustness differentiation)

All five share rank 1 on score. Differentiation is by enforcement mechanism strength — relevant for predicting resilience under length pressure or context truncation:

| Rank | Variation | Enforcement mechanism | Differentiator |
|------|-----------|----------------------|----------------|
| 1a | V-02 Sum-first | Hard phase separation — "no ratings in this phase" | Structural impossibility of collapse: ratings literally cannot appear in Phase 3 |
| 1b | V-05 Golden synthesis | Role-attributed phases + prohibitive + gate | Most mechanisms stacked; role labels (PM, Architect, Strategy) anchor structural ordering in section headers |
| 1c | V-03 Prohibitive | Output rules with "PROHIBITED" + numbered steps | Rules-of-output framing is hardest to override under compression; no inline template reduces ambiguity about format |
| 1d | V-04 Interrogative+sum-first | Q-sequence + "no ratings yet" in Q3 | Q-frame is familiar; "no ratings yet" is explicit local prohibition preventing bleed from Q3 into Q5 |
| 1e | V-01 FINDINGS-mirror | Named output slots with gate instructions | Slot-filling model is predictable; risk is template elision under length pressure vs structural impossibility |

---

### Excellence Signals from Round 2

**R2 produced two patterns not present in R1:**

**R2-E1: Role-attributed phase headers (V-05)**
V-05 introduces "PHASE 1 -- PM: BUDGET" and "PHASE 2 -- ARCHITECT: COMPLEXITY." The reviewer persona is embedded in the section label, not just the instruction text. This means the document structure itself signals who is computing what — a reader (or model under compression) cannot reach PHASE 2 without having completed PM's work. The role label is a structural reminder that survives section-header skimming.

**R2-E2: Score-delta example fragment (V-01, V-05)**
Both variations include a concrete example of the amendment format: `"Completing this moves [Component] from RED to YELLOW, raising score ~10 pts."` An example fragment reduces ambiguity about what "state what changes in the feasibility score" means — the model has a surface to imitate rather than a requirement to interpret. This is different from R1's V-05 which required score-delta without an example.

---

### Round 1 vs Round 2 Comparison

| Criterion | R1 worst | R2 worst |
|-----------|----------|----------|
| C-09 (sum-and-compare chain) | FAIL (4/5 variations) | PASS (5/5) |
| C-11 (inference precedes ratings) | FAIL (3/5 variations) | PASS (5/5) |
| C-12 (budget precedes ratings) | FAIL (4/5 variations) | PASS (5/5) |

The three R1 structural gaps were systematically closed across all five axes. The v2 rubric correctly predicted this: the scoring formula already accounted for R2 being a high-scoring round by expanding the aspirational pool from 2 to 4 criteria — but all five variations satisfy all four aspirational criteria at design level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Role-attributed phase headers embed reviewer persona in section labels, making structural ordering visible without reading instruction text", "Score-delta example fragment in amendment instruction reduces ambiguity by providing an imitable surface"]}
```
