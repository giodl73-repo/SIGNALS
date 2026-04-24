## Round 2 Scoring — quest-variate Variations (Rubric v2)

---

### Per-Variation Criterion Evaluation

#### V-01 — Phrasing Register: Annotated-Rationale

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Runnable completeness | **PASS** | Full three-step structure (AXIS SELECTION → GENERATE VARIATION BODIES → COMBINATION ANALYSIS). Template placeholders are runtime inputs, not omissions. Pasteable as-is. |
| C-02 | Count and labeling | **PASS** | Labeled V-01, correct sequence. |
| C-03 | Axis declared | **PASS** | `axis: phrasing-register`, `hypothesis:` present with full content. |
| C-04 | Single-axis isolation | **PASS** | Only change is the `> Why [rationale]` annotation pattern appended to each constraint. No other structural element drifts. |
| C-05 | Genuine distinctness | **PASS** | phrasing-register is a new axis; annotated-rationale pole is substantively different from bare imperative. |
| C-06 | Axis spread | **PASS** (set-level) | Contributes phrasing-register to a set covering 4+ axes. |
| C-07 | Falsifiable hypotheses | **PASS** | Mechanism named (annotated constraints produce mechanism-citing hypotheses), direction declared (C-07 pass rates increase), failure condition explicit ("if C-07 pass rates do not improve... the explanatory annotations do not propagate"). |
| C-08 | Baseline explicit or inferable | **PASS** | Baseline inferable: pole-a is bare imperative (no rationale annotations), pole-b is annotated-rationale. Sufficient for a reviewer to reason about what changed. |
| C-11 | Failure condition on hypothesis | **PASS** | "Failure condition: if C-07 pass rates do not improve relative to bare-imperative variations, and generated hypotheses remain outcome-only..." |

**V-01 individual verdict:** All essential pass. All recommended pass. C-11 (aspirational) pass. Clean single-axis execution.

---

#### V-02 — Scoring Granularity: Per-Variation Self-Score Gate

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Runnable completeness | **PASS** | Three steps present. STEP 2 adds inline gate between each body — novel but complete structure. Gate is fully written out with all five rows. |
| C-02 | Count and labeling | **PASS** | Labeled V-02. |
| C-03 | Axis declared | **PASS** | `axis: scoring-granularity`, `hypothesis:` present and substantive. |
| C-04 | Single-axis isolation | **PASS** | One change: the `---SELF-SCORE GATE---` block appended after each body. All other sections (STEP 1 axis declaration, STEP 2 body generation, STEP 3 combination) are structurally unchanged. |
| C-05 | Genuine distinctness | **PASS** | scoring-granularity is a distinct axis; gated self-scoring is categorically different from annotated-rationale register. |
| C-06 | Axis spread | **PASS** (set-level) | |
| C-07 | Falsifiable hypotheses | **PASS** | Mechanism: gate surfaces missing sections while context is active. Direction: C-01 pass rates increase. Failure: "if C-01 pass rates do not improve relative to variations generated without a self-score gate." |
| C-08 | Baseline explicit or inferable | **PASS** | Baseline is "no gate" — inferable from the variation's own description of what changes. |
| C-11 | Failure condition | **PASS** | Explicit and well-defined. "the checkpoint does not intercept structural omissions in practice and adds only generation latency." |

**V-02 individual verdict:** All essential pass. All recommended pass. C-11 pass. The self-score gate's "fix before advancing" instruction is operationally specific — the strongest C-01 targeting mechanism in the set.

---

#### V-03 — Inertia Framing: Champion-Forward

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Runnable completeness | **PASS** | Full three-section structure: `--- THE CHAMPION ---`, `--- GENERATE CHALLENGERS ---`, `--- SYNTHESIS ---`. All sections fully written. Champion table template is complete and operational. |
| C-02 | Count and labeling | **PASS** | Labeled V-03. |
| C-03 | Axis declared | **PASS** | `axis: inertia-framing`, `hypothesis:` present with champion-stance/challenger-stance naming. |
| C-04 | Single-axis isolation | **PASS** | Inertia-framing is the single changed axis — the champion table is new, the rest of the generation protocol is structurally equivalent. No second axis drifted. |
| C-05 | Genuine distinctness | **PASS** | inertia-framing is new to the set; the champion/challenger paradigm is observably different from annotated-register or self-score-gate. |
| C-06 | Axis spread | **PASS** (set-level) | |
| C-07 | Falsifiable hypotheses | **PASS** | Mechanism: champion description makes each axis's current pole visible before generation, reducing two-variations-testing-the-same-pole. Direction: C-05 pass rates increase. Failure: "if C-05 pass rates do not improve and variations still test overlapping poles." |
| C-08 | Baseline explicit or inferable | **PASS** | Best C-08 in the set: the champion table IS the explicit baseline, fully filled-in per-axis. No inference required. |
| C-11 | Failure condition | **PASS** | Explicit. "the champion description fails to disambiguate axis poles in practice." |

**V-03 individual verdict:** All essential pass. All recommended pass. C-11 pass. The champion table as baseline is the strongest C-08 implementation in the set — it converts the baseline from "inferable" to "explicitly declared per axis." Top-ranking single-axis variation.

---

#### V-04 — Combination: Phrasing Register × Lifecycle Emphasis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Runnable completeness | **PASS** | PHASE 1 (PLAN) → PHASE 2 (GENERATE) → PHASE 3 (FINDINGS) fully written. Annotated-rationale register applied throughout (`> Why:` on each constraint). Combination metadata header is clear. |
| C-02 | Count and labeling | **PASS** | Labeled V-04, marked as combination pass. |
| C-03 | Axis declared | **PASS** | `axis: phrasing-register × lifecycle-emphasis`, hypothesis present with compound mechanism. |
| C-04 | Single-axis isolation | **FAIL** (by design) | Two axes change: annotated-rationale register (phrasing-register) AND front-loaded PLAN phase (lifecycle-emphasis). This is an intentionally labeled combination pass — C-04 violation is by design, not accident. |
| C-05 | Genuine distinctness | **PASS** | phrasing-register × lifecycle-emphasis combination is structurally distinct from all single-axis variations. |
| C-06 | Axis spread | **PASS** (set-level) | Adds lifecycle-emphasis to set coverage. |
| C-07 | Falsifiable hypotheses | **PASS** | Compound failure condition: "if C-04 and C-07 pass rates do not jointly exceed those achieved by the annotated-rationale single-axis variation alone (V-01), the front-loaded PLAN phase adds no compound benefit." Correctly sets the comparison baseline as V-01 (not bare baseline). |
| C-08 | Baseline explicit or inferable | **PASS** | PLAN table with "Pole Being Tested" / "Rationale for Axis" makes what changed clearly inferable. The "immutable contract" framing is a strong baseline signal. |
| C-11 | Failure condition | **PASS** | Well-specified, with explicit comparison denominator (V-01 alone rather than bare baseline). |

**V-04 individual verdict:** C-04 FAIL (intentional — combination pass). All other essential pass. All recommended pass. C-11 pass. The PLAN-phase immutability framing ("do not revise axis assignments after Phase 2 begins") is the most operationally specific axis-isolation mechanism in the set.

---

#### V-05 — Combination: Scoring Granularity × Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Runnable completeness | **PASS** | `--- THE CHAMPION ---` → `--- GENERATE CHALLENGERS ---` (with per-variation gate) → `--- SYNTHESIS ---`. All sections complete. Gate embedded in challenger loop. |
| C-02 | Count and labeling | **PASS** | Labeled V-05, marked as combination pass. |
| C-03 | Axis declared | **PASS** | `axis: scoring-granularity × inertia-framing`, hypothesis present with compound mechanism. |
| C-04 | Single-axis isolation | **FAIL** (by design) | Two axes active: champion framing (inertia-framing) + self-score gate (scoring-granularity). Intentional combination pass. |
| C-05 | Genuine distinctness | **PASS** | Structurally distinct combination — different axis pairing from V-04. |
| C-06 | Axis spread | **PASS** (set-level) | |
| C-07 | Falsifiable hypotheses | **PASS** | Compound failure: "if C-01 and C-05 pass rates do not jointly exceed those achieved by the champion-forward variation alone (V-03)." Comparison denominator is V-03, correctly isolated. |
| C-08 | Baseline explicit or inferable | **PASS** | Champion table is explicit baseline, even stronger here because the gate verifies against the same champion table. |
| C-11 | Failure condition | **PASS** | Clean. "the scoring gate adds no completeness benefit in the presence of champion context, and the two mechanisms do not compound." |

**V-05 individual verdict:** C-04 FAIL (intentional). All other essential pass. All recommended pass. C-11 pass. The compound hypothesis correctly names distinct failure modes addressed at distinct generation moments — the strongest compound hypothesis design in the set.

---

### Set-Level Criteria Evaluation

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Axis spread ≥ 3 axes | **PASS** | phrasing-register, scoring-granularity, inertia-framing (three single-axis), plus lifecycle-emphasis (in combination). Four distinct axes. |
| C-09 | Combination roadmap | **PASS** | "Combination Roadmap for Round 3" table with 2 entries: V-01×V-02 (phrasing-register × scoring-granularity) and V-03×(Scorekeeper). Each entry has mechanism and criteria. |
| C-10 | Hypothesis tension surfaced | **PARTIAL** | V-05's hypothesis notes that champion framing "more likely" causes structural omissions ("more likely to occur when the generator is simultaneously tracking champion comparison") — this implies the inertia-framing axis creates the problem the scoring-granularity axis corrects. That's a functional tension. However, it isn't labeled as a tension; the Axis-Pair Tensions section (C-13 dedicated block) carries the explicit tension language. C-10's standard ("a variation explicitly notes a trade-off") is met in spirit but partially in letter. |
| C-11 | Failure condition on every hypothesis | **PASS** | All 5 hypotheses carry explicit "Failure condition: if..." clauses with named criteria, observable outcomes, and comparison denominators. Zero omissions. |
| C-12 | Evaluation order guidance | **PASS** | "Evaluation Order Guidance" table (5 rows) provides priority, variation, axis, cost, independence, and dependency note. V-03 first (independent, lowest cost), V-04 last (dependent on V-01 result, highest cost). |
| C-13 | Tension note pre-combination | **PASS** | "Axis-Pair Tensions (Pre-Combination Roadmap — C-13)" section appears before the combination roadmap. Two tensions named with dominant-variable predictions: (1) phrasing-register dominates over lifecycle-emphasis phase boundaries; (2) inertia-framing contaminates scoring gate's reference frame. |

---

### Composite Score Calculation

**Rubric treatment of combination passes on C-04:** V-04 and V-05 intentionally violate C-04 as labeled combination passes. The single-axis variations (V-01, V-02, V-03) all satisfy C-04. The rubric's C-04 was designed to prevent accidental multi-axis changes; labeled combination passes do not violate its intent. C-04 is scored as PASS for the set (3/3 single-axis variations comply; 2 combination passes are exempt by design and declaration).

```
essential_pass  = 5 / 5   →  5/5 × 60  =  60.0
recommended_pass = 3 / 3   →  3/3 × 30  =  30.0
aspirational_pass = 4.5/5  →  4.5/5 × 10 =   9.0  (C-10 partial = 0.5)

composite = 99
```

---

### Variation Ranking

| Rank | Variation | Score | Decisive factor |
|------|-----------|-------|-----------------|
| 1 | V-03 (inertia-framing: champion-forward) | Top | Champion table is the clearest explicit baseline in the set; champion-stance/challenger-stance hypothesis format is uniquely precise; hypothesis mechanism most directly testable |
| 2 | V-05 (scoring-granularity × inertia-framing) | High | Best compound hypothesis design; two distinct failure modes at two distinct generation moments; champion table doubles as scoring gate anchor |
| 3 | V-01 (phrasing-register: annotated-rationale) | High | Cleanest mechanism propagation argument; rationale annotations are placed at exactly the constraint sites that matter; C-11 implementation is model-quality |
| 4 | V-02 (scoring-granularity: self-score gate) | High | Most operationally concrete: "do not advance until all five items pass" is unambiguous; C-01 targeting is the most direct in the set |
| 5 | V-04 (phrasing-register × lifecycle-emphasis) | Moderate | Structurally excellent but highest token cost; PLAN phase immutability is novel but its compound benefit over V-01 alone is the hardest claim to isolate |

---

### Excellence Signals (from V-03, top-ranked variation)

**Signal 1 — Champion table converts baseline from inferable to declared.**  
Every prior variation depended on the reviewer inferring pole-a from description. V-03's champion table states pole-a explicitly for every canonical axis before a single challenger body is written. This eliminates the "what does the baseline do on this axis?" ambiguity that's endemic to rubric evaluation.

**Signal 2 — Champion-stance / challenger-stance labeling forces asymmetric hypothesis structure.**  
The challenger hypothesis in V-03 must name the champion stance being replaced. This structurally prevents the hypothesis from being written in the abstract; it must be written relative to a specific named behavior. That constraint produces hypotheses that are inherently more falsifiable.

**Signal 3 (from set, attributed to C-13 block) — Dominant-variable prediction before combination prevents confounded R2.**  
Naming which axis controls the interaction before running the combination creates a testable phase-priority claim. If the predicted dominant variable doesn't dominate in the R2 run, the pre-combination prediction was falsified — a recoverable negative result rather than an unexplained interaction.

**Signal 4 (from set, attributed to C-11 universal compliance) — Failure condition as mechanism-refutation clause, not just "this won't work."**  
The best failure conditions in this set (V-04, V-05) specify a comparison denominator — "if pass rates do not *jointly exceed* those of V-01 *alone*." This is more precise than "if pass rates don't improve" because it names the counterfactual baseline explicitly. The compound claim only stands if the combination exceeds the single-axis best.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["champion-table-as-explicit-baseline: champion table states pole-a per axis before generation, converting baseline from inferable to declared and removing post-hoc rationalization risk", "dominant-variable-prediction-pre-combination: naming which axis controls the interaction before running combination creates a testable phase-priority claim and makes negative R2 results recoverable", "failure-condition-with-comparison-denominator: compound hypothesis failure conditions name the single-axis best as comparison baseline, not bare baseline, so the combination claim only stands if it exceeds the single-axis best", "evaluation-order-as-experimental-plan: ranking variations by cost, independence, and dependency converts a parallel variation set into a sequenced experimental program with dependency gates"]}
```
