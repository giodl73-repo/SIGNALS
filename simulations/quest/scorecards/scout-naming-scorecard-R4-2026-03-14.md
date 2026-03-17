## scout-naming R4 — Score Summary

**All 5 variations: 98.75/100** (up from R3's 98.3)

| Rank | Variation | Aspirational cleared | Score |
|------|-----------|----------------------|-------|
| 1 | V-05 (all three + --validate attempt) | C-10–C-16 | 98.75 |
| 2 | V-04 (anchored scale + inertia) | C-10–C-16 | 98.75 |
| 3 | V-03 (inertia framing) | C-10–C-16 | 98.75 |
| 4 | V-02 (exit conditions) | C-10–C-16 | 98.75 |
| 5 | V-01 (anchored scale) | C-10–C-16 | 98.75 |

### Key findings

**Score advance mechanism**: R4's 0.45pt gain (98.3→98.75) comes entirely from C-15 and C-16 being promoted to distinct aspirational criteria in the v4 rubric. All R4 variations already implement both as structural constants, so the advance is immediate across the board. No new criterion was first cleared in R4.

**C-09 status — V-05 reaches 2/4 sub-conditions:**
- Flag recognized and handled: **PASS**
- Row pinned: **FAIL** — Row 2 vs. Row 1 required (row-position conflict with inertia framing)
- Validation Summary present: **PASS**
- Delta notation from prior run: **FAIL** — infrastructure gap, inline prompting cannot retrieve stored prior-run scores

**Four new patterns identified:**

1. **Anchor rubric tier descriptions** (V-01, V-04, V-05) — per-role 1-3/4-6/7-9/10 anchors make scoring interpretation output-verifiable; tier language chains from SETUP → SCORE → DECIDE sub-part (1), creating an auditable displacement argument

2. **Phase exit condition checklists** (V-02, V-05) — convert C-03, C-11, C-15, C-16 from confirmatory to prescriptive; a missing artifact blocks phase close rather than just scoring lower

3. **Generation-time displacement floor** (V-03, V-04, V-05) — status-quo pre-scored in SETUP, [BELOW-SQ: Strategy] filter at GENERATE, Row 1 in SCORE; displacement strength becomes a measurable metric

4. **--validate branch structure** (V-05) — partial C-09 isolates the two blocking requirements with precision: row-position conflict and delta notation infrastructure gap

```json
{"top_score": 98.75, "all_essential_pass": true, "new_patterns": ["Anchor rubric tier descriptions per role (1-3/4-6/7-9/10) create an auditable scoring chain: SETUP declares tiers, SCORE assigns them, DECIDE sub-part (1) references them — combined with benchmark row, displacement argument emerges from rubric tier comparison not DECIDE prose judgment.", "Phase exit condition checklists convert criteria from evaluator-inferred to checklist-enforced — a phase may not close until its checklist clears; C-03 and C-11 become preconditions for phase advance, not post-output observations.", "Status-quo pre-scored as benchmark row with generation-time displacement floor ([BELOW-SQ: Strategy]) at GENERATE; fraction-beating-SQ metric makes incumbency strength measurable; adds [below SQ threshold] as a fourth disqualification class.", "Inline --validate branch (V-05) reaches 2/4 C-09 sub-conditions, isolating two blocking requirements: row-position conflict (C-09 requires Row 1 but inertia framing uses Row 1 for [STATUS QUO]) and delta notation infrastructure gap (prior stored run scores unavailable to inline prompting)."]}
```
rcement mechanism available to inline prompting.", "Status-quo pre-scored as benchmark row in SETUP using anchor rubric; composite used as generation-time displacement floor ([BELOW-SQ: Strategy] marks and excludes candidates that cannot reach a higher Strategy tier); Row 1 in SCORE matrix with full 5-dimension scores; fraction-beating-SQ metric reported at DECIDE. Adds [below SQ threshold] as a fourth disqualification class applied before SCORE. The generation-time floor eliminates strategically weak candidates before they consume scoring effort and makes incumbency strength a measurable metric.", "Inline --validate branch (V-05) reaches 2/4 C-09 sub-conditions and isolates two blocking requirements: (1) row-position conflict -- C-09 requires Row 1 pinned but inertia-framing design places [STATUS QUO] at Row 1; (2) delta notation infrastructure gap -- C-09 requires prior stored run scores for delta comparison which inline prompting cannot retrieve. CONFIRMED/CONDITIONAL/AT RISK verdict is a functional substitute but not a C-09 compliance substitute. Full C-09 requires resolving the row-position definition or adding prior-run score storage outside the prompt."]}
```

---

### V-01: Output Format — Anchored 1-10 Scale

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | "Role weights: Strategy 25% \| PM 25% \| GTM 20% \| UX 20% \| Design 10%. Weight sum: 100%." Composite formula explicit. Five-column matrix. Anchor rubric per role declared and locked in SETUP. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check -- top 3 candidates: Internal (repo namespace) + External (npm/PyPI + brand/domain). Report: [candidate] / [class] / [hit or clear]." Both classes, top 3. |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK: Name, Score, labeled sub-parts (1) Dimensions with integer score + anchor tier, (2) vs. Status-quo, (3) Vocabulary. Exceeds essential bar. |
| C-05 | Constraint Parsed + Applied | PASS | "Parse any constraint from the invocation. Constraint: [text, or 'none']." Generation-time enforcement: "mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-06 | Disqualification Logic Labeled | PASS | "[DISQ: constraint]" at GENERATE, "[DISQ: low Strategy]"/"[DISQ: low PM]" floor rule at SCORE, DISQUALIFIED SUMMARY with tally "[constraint]: N \| [low Strategy]: N \| [low PM]: N \| [collision]: N \| [other]: N". |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP: Name, Score, "Fallback rationale: [One sentence -- when or why this is the preferred alternative.]" |
| C-08 | Findings Register (SF-NN) | PASS | "SF-NN table. At minimum one entry on: Anchor calibration, Status-quo gap, Vocabulary coverage." Three mandated topics including axis-specific finding. |
| C-09 | `--validate` flag | FAIL | Not present. Design gap unchanged. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." GATE 1 confirms: "Vocab: N terms from [source]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Any candidate violating the parsed constraint --> mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." Instruction-based. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four numbered phase separators. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." Three-value counter. |
| C-14 | 3-part DECIDE Rationale | PASS | Sub-part (1): ≥2 dimensions with integer score and anchor-rubric tier ("e.g., Strategy: 8 -- strong; signals X clearly"). Sub-part (2): status-quo from SETUP, specific dimensions where tier is higher. Sub-part (3): vocab term + connection. |
| C-15 | Labeled Sub-part Record | PASS | "(1) Dimensions: [...]", "(2) vs. Status-quo: [...]", "(3) Vocabulary: [...]" as explicitly labeled distinct lines under TOP PICK. |
| C-16 | Gate 3 Binary Status Flags | PASS | GATE 3: "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3." Count + two binary flags. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/8 (C-09 fails)

```
composite = (5/5 × 60) + (3/3 × 30) + (7/8 × 10) = 60 + 30 + 8.75 = 98.75
```

**Score: 98.75 / 100 — GOLDEN**

Sub-criterion note: Anchor rubric creates an auditable scoring chain: SETUP declares what each tier means per role, SCORE assigns tiers, DECIDE sub-part (1) references them. First variation to make scoring interpretation criteria output-verifiable by tier label rather than raw integer.

---

### V-02: Lifecycle Emphasis — Phase Exit Conditions

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." GENERATE EXIT CONDITIONS: "[ ] Candidate count is between 10 and 15 (inclusive)" -- checklist enforces the rubric criterion. |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | "Strategy 25% \| PM 25% \| GTM 20% \| UX 20% \| Design 10% \| Sum: 100%." Composite formula. SETUP EXIT CONDITIONS: "[ ] Role weights declared and sum to 100%." |
| C-03 | Collision Check (namespace + external) | PASS | "Internal + External. Report: [candidate] / [class] / [hit or clear]." SCORE EXIT CONDITIONS: "[ ] Collision report present covering top 3 candidates" + "[ ] Both collision classes reported (internal namespace + external registry)." Strongest C-03 enforcement -- collision check is a checklist precondition for SCORE to close. |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK: Name, Score, labeled sub-parts (1)(2)(3). DECIDE EXIT CONDITIONS: "[ ] TOP PICK named with composite score." |
| C-05 | Constraint Parsed + Applied | PASS | Constraint parsed + generation-time enforcement. GENERATE EXIT CONDITIONS: "[ ] Constraint enforcement applied at generation time (not post-hoc filter)" + "[ ] All constraint-violating candidates labeled [DISQ: constraint] here." |
| C-06 | Disqualification Logic Labeled | PASS | "[DISQ: constraint]", score floor with [DISQ: low Strategy/PM] labels. SCORE EXIT CONDITIONS: "[ ] Score floor applied: all low-scoring candidates labeled [DISQ: low Strategy/PM]." DISQUALIFIED SUMMARY with tally. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP: Name, Score, fallback rationale. DECIDE EXIT CONDITIONS: "[ ] RUNNER-UP named with fallback rationale." |
| C-08 | Findings Register (SF-NN) | PASS | "At minimum one entry on: Exit condition effect (did any exit condition catch a missing artifact?), Status-quo gap, Vocabulary coverage." Axis-specific finding. |
| C-09 | `--validate` flag | FAIL | Not present. Design gap unchanged. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." SETUP EXIT CONDITIONS: "[ ] Domain vocabulary list present (5-10 terms, source named)." |
| C-11 | Generation-time Constraint Enforcement | PASS | "mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." GENERATE EXIT CONDITIONS: "[ ] Constraint enforcement applied at generation time (not post-hoc filter)" + "[ ] All constraint-violating candidates labeled [DISQ: constraint] here." Strongest C-11 -- checklist prevents post-hoc filter. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Exit condition checklists strengthen phase close boundaries. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." Exit conditions verify the count before gate is written. |
| C-14 | 3-part DECIDE Rationale | PASS | "(1) Dimensions: [Name at least two scoring dimensions and state the specific reason...]", "(2) vs. Status-quo: [...]", "(3) Vocabulary: [...]" labeled sub-parts. |
| C-15 | Labeled Sub-part Record | PASS | "(1) Dimensions: [...]", "(2) vs. Status-quo: [...]", "(3) Vocabulary: [...]" as labeled lines. DECIDE EXIT CONDITIONS: "[ ] All three labeled sub-parts present: (1) Dimensions / (2) vs. Status-quo / (3) Vocabulary." Strongest C-15 -- checklist enforces structural presence. |
| C-16 | Gate 3 Binary Status Flags | PASS | GATE 3: "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3." SCORE EXIT CONDITIONS include separate status-quo column confirmation and collision report confirmation -- flags backed by checklist. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/8 (C-09 fails)

```
composite = 60 + 30 + 8.75 = 98.75
```

**Score: 98.75 / 100 — GOLDEN**

Sub-criterion note: V-02's contribution is verification mechanism upgrade, not criterion coverage. Every criterion passes at structurally stronger level: C-03 (collision check is checklist precondition for SCORE close), C-11 (generation-time enforcement is checklist precondition for GATE 2), C-15 (labeled sub-parts are checklist precondition for artifact write). Prescriptive/confirmatory distinction confirmed.

---

### V-03: Inertia Framing — Status-Quo as Scored Benchmark Row

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | "Strategy 25% \| PM 25% \| GTM 20% \| UX 20% \| Design 10% \| Sum: 100%." Composite formula. Row 1 is [STATUS QUO] with all five dimension scores pre-populated from SETUP. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check -- top 3 candidates (excluding [STATUS QUO]): Internal (repo namespace) + External (npm/PyPI + brand/domain). Report: [candidate] / [class] / [hit or clear]." |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK: Name, Score, labeled sub-parts. Sub-part (1) cites actual matrix scores. Sub-part (2) mandates direct numerical comparison ("Strategy: 8 vs. SQ 6") and displacement conclusion label. |
| C-05 | Constraint Parsed + Applied | PASS | Constraint parsed + "mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-06 | Disqualification Logic Labeled | PASS | "[DISQ: constraint]", "[DISQ: low Strategy/PM]" score floor, "[BELOW-SQ: Strategy]" at generation time. DISQUALIFIED SUMMARY with four-class tally: "[constraint]: N \| [low Strategy]: N \| [low PM]: N \| [below SQ threshold]: N \| [collision]: N \| [other]: N". Most complete C-06 taxonomy -- adds new class. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP: Name, Score, "Fallback rationale: [One sentence. Note Beat SQ? status.]" Beat SQ? linkage couples runner-up to displacement argument. |
| C-08 | Findings Register (SF-NN) | PASS | "At minimum one entry on: Benchmark effect (did scoring the status-quo first change candidates generated or how scores were assigned?), Displacement strength (fraction of candidates that beat [STATUS QUO] composite), Vocabulary coverage." |
| C-09 | `--validate` flag | FAIL | Not present. Design gap unchanged. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Any candidate violating the parsed constraint --> mark [DISQ: constraint] here. Do not carry violating candidates into PHASE 3." |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Below SQ threshold: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." Four-value counter -- extends gate to report displacement-floor eliminations separately. |
| C-14 | 3-part DECIDE Rationale | PASS | Sub-part (1) cites actual dimension scores from matrix. Sub-part (2) mandates direct numerical comparison and displacement conclusion label. Sub-part (3) vocab connection. Strongest C-14 -- numerical comparison traceable to matrix row. |
| C-15 | Labeled Sub-part Record | PASS | "(1) Dimensions: [...]", "(2) vs. Status-quo: [...]", "(3) Vocabulary: [...]" labeled lines under TOP PICK. |
| C-16 | Gate 3 Binary Status Flags | PASS | GATE 3: "Surviving after score: N. Status-quo benchmarked: yes. Collisions checked: top 3." "yes" hardcoded -- benchmark is mandatory, cannot be absent in V-03. Satisfies C-16 as a stronger form (obligatory flag). |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/8 (C-09 fails)

```
composite = 60 + 30 + 8.75 = 98.75
```

**Score: 98.75 / 100 — GOLDEN**

Sub-criterion note: V-03's key contribution is the displacement floor at GENERATE: "[BELOW-SQ: Strategy] here and exclude from SCORE." This is the first variation to enforce a strategic quality gate at generation time rather than at SCORE floor. The floor is non-arbitrary -- it is a computed composite from SETUP. Gate 2 counter distinguishes "Below SQ threshold: N" from "Pre-disqualified (constraint): N" -- separate reporting of a new elimination class. Displacement strength becomes a measurable metric.

---

### V-04: Combined — Output Format + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | Full anchor rubric. "Apply consistently to all candidates including status-quo." [STATUS QUO] baseline scores with brief rationale per dimension cited from anchor rubric in SETUP. Strongest C-02 -- rubric applies to benchmark row. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check -- top 3 candidates (excluding [STATUS QUO]): Internal + External." Both classes. |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK: Name, Score, labeled sub-parts. Sub-part (1): integer score + anchor-rubric tier label. Sub-part (2): [STATUS QUO] composite named, dimensions where anchor tier is higher, displacement conclusion. Sub-part (3): vocab. |
| C-05 | Constraint Parsed + Applied | PASS | Constraint parsed + "Any candidate violating the parsed constraint --> mark [DISQ: constraint] here." |
| C-06 | Disqualification Logic Labeled | PASS | "[DISQ: constraint]", "[DISQ: low Strategy/PM]" floor, "[BELOW-SQ: Strategy]". DISQUALIFIED SUMMARY: "[constraint]: N \| [low Strategy]: N \| [low PM]: N \| [below SQ threshold]: N \| [collision]: N \| [other]: N". Five labeled classes. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP: Name, Score, "Fallback rationale: [One sentence. Note Beat SQ? status.]" |
| C-08 | Findings Register (SF-NN) | PASS | "At minimum one entry on: Anchor + benchmark interaction (did rubric descriptions make the benchmark row more or less strict than an implicit scale?), Displacement strength, Vocabulary coverage." Axis-specific finding. |
| C-09 | `--validate` flag | FAIL | Not present. Design gap unchanged. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Any candidate violating the parsed constraint --> mark [DISQ: constraint] here." |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N. Below SQ threshold: N. Pre-disqualified (constraint): N. Advancing to SCORE: N." Four-value counter. |
| C-14 | 3-part DECIDE Rationale | PASS | Sub-part (1): integer score + anchor-rubric tier for each dimension. Sub-part (2): [STATUS QUO] composite named, specific dimensions where anchor tier is higher, displacement conclusion. Sub-part (3): vocab. Strongest C-14 in round -- rubric tier language in sub-part (1) makes scoring chain fully auditable from declaration to rationale. |
| C-15 | Labeled Sub-part Record | PASS | "(1) Dimensions: [...]", "(2) vs. Status-quo: [...]", "(3) Vocabulary: [...]" labeled lines. |
| C-16 | Gate 3 Binary Status Flags | PASS | GATE 3: "Surviving after score: N. Status-quo benchmarked: yes. Collisions checked: top 3." |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/8 (C-09 fails)

```
composite = 60 + 30 + 8.75 = 98.75
```

**Score: 98.75 / 100 — GOLDEN**

Sub-criterion note: V-04 achieves the most auditable scoring chain. Anchor rubric declared in SETUP, applied to [STATUS QUO] in SETUP, applied to all candidates in SCORE, cited in DECIDE sub-part (1). Displacement argument in sub-part (2) names [STATUS QUO] composite and anchor tiers -- comparison verifiable by inspection across three phases without re-reading prose. Hypothesis (anchors + benchmark row = apples-to-apples displacement case) structurally confirmed. No interference between axes detected.

---

### V-05: Combined — All Three + C-09 (--validate)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Candidate Volume (10-15) | PASS | "Produce 10-15 candidate names. If --validate is present, the pinned name does not count toward this total -- generate 10-15 fresh candidates beyond it." Edge case handled correctly. GENERATE EXIT CONDITIONS: "[ ] Fresh candidate count is between 10 and 15." |
| C-02 | Five-Role Scoring Matrix + Declared Weights | PASS | Full anchor rubric with 5 roles. "Apply consistently to all candidates including status-quo and pinned row." [STATUS QUO] baseline scored in SETUP. |
| C-03 | Collision Check (namespace + external) | PASS | "Collision check -- top 3 candidates (excluding [STATUS QUO], including pinned if present): Internal + External." SCORE EXIT CONDITIONS: "[ ] Collision report present covering top 3 (including pinned candidate)" + "[ ] Both collision classes reported." Handles pinned candidate in collision check correctly. |
| C-04 | Top Pick Named + Justified | PASS | TOP PICK: Name, Score, labeled sub-parts (1)(2)(3). "Name: [winner -- may be the pinned candidate or a fresh candidate]" -- winner may be the validated name. |
| C-05 | Constraint Parsed + Applied | PASS | Constraint parsed + generation-time enforcement + GENERATE EXIT CONDITIONS: "[ ] Constraint enforcement applied at generation time (not post-hoc filter)." |
| C-06 | Disqualification Logic Labeled | PASS | "[DISQ: constraint]", "[DISQ: low Strategy/PM]" floor, "[BELOW-SQ: Strategy]". DISQUALIFIED SUMMARY with 5-class tally. |
| C-07 | Runner-Up + Fallback Rationale | PASS | RUNNER-UP: Name, Score, "Fallback rationale: [One sentence. Note Beat SQ? status.]" |
| C-08 | Findings Register (SF-NN) | PASS | "At minimum one entry on: C-09 compliance (did --validate flag handling produce the expected pinned row and Validation Summary? Any edge cases?), Anchor + benchmark interaction, Displacement strength, Exit condition value." Four mandated topics -- most prescriptive C-08 in round. |
| C-09 | `--validate` flag | FAIL | Partial implementation -- 2/4 sub-conditions met. (1) Flag recognized: "IF --validate <name> IS PRESENT IN THE INVOCATION" branch. PASS. (2) Row pinned: Row 2 (after [STATUS QUO]) -- criterion requires Row 1. FAIL -- row position discrepancy. (3) Validation Summary: present with score profile table, anchor tiers, strengths, risks, vs. status-quo, CONFIRMED/CONDITIONAL/AT RISK verdict. PASS. (4) Delta notation: absent -- Validation Summary shows current scores vs. status-quo and rank vs. fresh candidates but no comparison to prior stored run (no delta values). FAIL -- infrastructure gap confirmed. |
| C-10 | Domain Vocabulary Extraction logged | PASS | "Extract 5-10 domain vocabulary terms. Domain vocabulary: [term1, ...] Source: [file name]." SETUP EXIT CONDITIONS: "[ ] Domain vocabulary list present (5-10 terms, source named)." |
| C-11 | Generation-time Constraint Enforcement | PASS | "Any candidate violating the parsed constraint --> mark [DISQ: constraint] here." GENERATE EXIT CONDITIONS: "[ ] Constraint enforcement applied at generation time (not post-hoc filter)." Strongest C-11 via checklist. |
| C-12 | Phase-structured Output | PASS | "--- PHASE 1: SETUP ---" through "--- PHASE 4: DECIDE ---". Four phase separators with exit condition checklists. |
| C-13 | Gate Confirmation Count | PASS | GATE 2: "Generated: N (fresh). Below SQ threshold: N. Pre-disqualified (constraint): N. Advancing to SCORE: N (+ 1 pinned row if --validate active)." Most sophisticated Gate 2 -- handles pinned row count parenthetically. |
| C-14 | 3-part DECIDE Rationale | PASS | Sub-part (1): integer score + anchor-rubric tier. Sub-part (2): [STATUS QUO] composite, specific dimensions where anchor tier is higher, displacement conclusion. Sub-part (3): vocab term. Same quality level as V-04. |
| C-15 | Labeled Sub-part Record | PASS | "(1) Dimensions: [...]", "(2) vs. Status-quo: [...]", "(3) Vocabulary: [...]" labeled lines. DECIDE EXIT CONDITIONS: "[ ] All three labeled sub-parts present" + "[ ] VALIDATION SUMMARY written if --validate was active." Strongest C-15 -- checklist enforces structural presence. |
| C-16 | Gate 3 Binary Status Flags | PASS | GATE 3: "Surviving after score: N. Status-quo benchmarked: yes/no. Collisions checked: top 3." SCORE EXIT CONDITIONS back up both flags with explicit checklists. Strongest C-16 in round. |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 7/8 (C-09 fails)

```
composite = 60 + 30 + 8.75 = 98.75
```

**Score: 98.75 / 100 — GOLDEN**

C-09 failure analysis: V-05 reaches 2 of 4 sub-conditions. Sub-conditions met: flag recognized with branching conditional instruction; Validation Summary section defined with score profile, anchor tiers, strengths, risks, vs. status-quo, and verdict. Sub-conditions unmet: (1) Row position -- C-09 criterion says "Row 1 pinned" but V-05's inertia-framing design places [STATUS QUO] at Row 1 and the pinned candidate at Row 2; fully implementing C-09 within inertia-framing requires either redefining "Row 1" in C-09's pass condition or resolving that C-09 and inertia framing cannot coexist. (2) Delta notation -- C-09 requires "comparing current scores to prior scores" with delta values (e.g., "Prior: 8.2 / Current: 8.5 / delta: +0.3"); V-05's Validation Summary compares current scores against status-quo and rank against fresh candidates; no stored prior-run scores exist to compute delta from. The verdict mechanism is a functional substitute but does not satisfy the literal pass condition. Infrastructure dependency confirmed.

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | V-05 (all three + --validate attempt) | 5/5 | 3/3 | 7/8 | **98.75** | YES |
| 2 | V-04 (anchored scale + inertia) | 5/5 | 3/3 | 7/8 | **98.75** | YES |
| 3 | V-03 (inertia framing) | 5/5 | 3/3 | 7/8 | **98.75** | YES |
| 4 | V-02 (exit conditions) | 5/5 | 3/3 | 7/8 | **98.75** | YES |
| 5 | V-01 (anchored scale) | 5/5 | 3/3 | 7/8 | **98.75** | YES |

All five variations reach 98.75. R4's score advance (98.3 -> 98.75) comes from C-15 and C-16 being promoted to distinct aspirational criteria in the v4 rubric -- all R4 variations already implement both as structural constants, so the advance is immediate across the board. No new criterion was first cleared in R4. Ceiling holds at 98.75 until C-09 is fully implemented.

---

## Sub-criterion Quality Analysis — Within the 98.75 Cluster

| Sub-criterion | V-05 | V-04 | V-03 | V-02 | V-01 |
|---------------|------|------|------|------|------|
| C-02 anchor rubric scope | All rows including pinned + SQ | All rows including SQ | Not present | Not present | Candidate rows only |
| C-06 disqualification classes | 5 ([constraint/low Str/PM/below SQ/collision/other]) | 5 | 4 | 3 | 3 |
| C-08 mandated findings | 4 (C-09 compliance + anchor+benchmark + displacement + exit value) | 3 (anchor+benchmark + displacement + vocab) | 3 (benchmark effect + displacement + vocab) | 3 (exit condition effect + SQ gap + vocab) | 3 (anchor calibration + SQ gap + vocab) |
| C-11 verification strength | Exit condition checklist | Instruction-based | Instruction-based | Exit condition checklist | Instruction-based |
| C-13 gate cardinality | 4 values + pinned row note | 4 values | 4 values | 3 values | 3 values |
| C-14 rationale precision | Integer score + anchor tier; displacement conclusion label | Same as V-05 | Direct numerical comparison ("Strategy: 8 vs. SQ 6"); displacement conclusion | Dimension name + reason stated | Dimension name + anchor tier cited |
| C-15 enforcement | Checklist + exit condition | Structural only | Structural only | Checklist + exit condition | Structural only |
| C-16 enforcement | Exit condition checklist backs Gate 3 flags | Gate 3 line only | Gate 3 line only (hardcoded "yes") | Exit condition checklist backs Gate 3 flags | Gate 3 line only |
| C-09 sub-conditions | 2/4 | 0/4 | 0/4 | 0/4 | 0/4 |

**Ranking rationale:**
- **V-05 leads**: strongest C-08 (4 mandated topics including C-09 compliance), C-09 partial (2/4 sub-conditions -- no other variation attempts implementation), C-13 (handles pinned row count), C-15/C-16 enforced by exit conditions. All structural improvements combined. Exit conditions and inertia framing confirmed to compose without conflict.
- **V-04 second**: most auditable scoring chain (anchor rubric applies to benchmark row in SETUP; tier language chains to DECIDE sub-part (1)). No interference between axes. "Displacement case emerges from rubric language, not DECIDE prose" hypothesis confirmed.
- **V-03 third**: establishes inertia framing as standalone contribution. First [BELOW-SQ: Strategy] generation-time pre-filter. Gate 2 extended to 4 values. Displacement strength metric.
- **V-02 fourth**: exit conditions confirmed as compliance-mechanism innovation. C-11, C-15, C-16 pass at stronger verification level. Prescriptive/confirmatory distinction experimentally confirmed.
- **V-01 fifth**: anchor rubric is output-quality innovation. First variation where scoring interpretation is output-verifiable by tier label. Does not extend to benchmark row or exit conditions.

---

## R4 vs R3 Progress

| Metric | R3 | R4 |
|--------|----|----|
| Score ceiling | 98.3 | 98.75 |
| Formula denominator | aspirational/6 | aspirational/8 |
| Variations hitting ceiling | 5/5 | 5/5 |
| New criteria cleared vs prior round | C-13 + C-14 | none (C-15 + C-16 promoted, not newly cleared) |
| C-15 form | First introduced (V-03/V-04/V-05) | Structural baseline (all 5) |
| C-16 form | First introduced (V-03/V-04/V-05) | Structural baseline (all 5) |
| New ceiling mechanism | C-09 (design gap) | C-09 (partial: 2/4 sub-conditions in V-05) |
| C-09 sub-conditions met | 0/4 | 2/4 (V-05 only) |

---

## Excellence Signals — Round 4

### E-1: Anchor rubric tier descriptions create an auditable scoring chain across all phases (V-01, V-04, V-05)

R3 used numeric scores (1-10) with no per-role interpretation guidance. V-01 introduces per-role anchor descriptions that define what each tier means: "Strategy 7-9 = strong; signals what this product uniquely does or whom it serves." V-04 applies the same rubric to the status-quo benchmark row, making comparisons apples-to-apples. Tier language propagates from SETUP -> SCORE -> DECIDE sub-part (1), creating a scoring chain verifiable by inspection. A candidate that earns "Strategy: 8 -- strong" must beat a status-quo that earned "Strategy: 6 -- adequate" -- the displacement case emerges from rubric language, not from DECIDE prose.

**New pattern**: Per-role anchor rubric tier descriptions make scoring interpretation output-verifiable. Combined with benchmark row, the audit chain is complete: declaration (SETUP) -> assignment (SCORE) -> rationale (DECIDE sub-part 1).

### E-2: Phase exit condition checklists enforce artifact presence as phase-close precondition (V-02, V-05)

R3's gate counters confirmed cardinality after the fact. V-02 introduces exit condition checklists: "[ ] Collision report present covering top 3 candidates" and "[ ] Both collision classes reported" must be checked before SCORE closes. A missing collision check blocks the phase from closing -- it cannot be confirmed-away by writing a smaller counter. Most impactful: C-03 compliance changes from a post-output evaluation criterion to a phase-close precondition. The checklist form generalizes to any criterion requiring an artifact from within a phase.

**New pattern**: Phase exit condition checklists are the strongest compliance enforcement mechanism available to inline prompting. Any criterion requiring an artifact from within a phase can be encoded as a checklist item at the phase-close boundary.

### E-3: Status-quo displacement floor at generation time introduces a strategic quality gate before SCORE (V-03, V-04, V-05)

R2/R3 computed vs. Status-Quo post-generation as a column. V-03 front-loads the comparison: status-quo composite is active as a generation-time floor. Candidates marked [BELOW-SQ: Strategy] are excluded before scoring. Gate 2 counter distinguishes "Below SQ threshold: N" from "Pre-disqualified (constraint): N" -- new elimination class reported separately. Displacement strength at DECIDE ("what fraction of candidates beat [STATUS QUO] composite?") becomes a measurable metric informing positioning decisions.

**New pattern**: Generation-time displacement floor eliminates strategically weak candidates before they consume scoring effort and makes incumbency strength a quantifiable metric.

### E-4: --validate branch isolates C-09 infrastructure requirements with precision (V-05)

V-05's partial implementation reveals two blocking requirements previously underspecified. First: row-position conflict -- C-09's "Row 1 pinned" and inertia framing's "[STATUS QUO] at Row 1" cannot coexist without a definition change. The conflict is structural, not phrasing. Second: delta notation infrastructure gap -- "comparing current scores to prior scores" requires stored prior-run state that inline prompting cannot retrieve. The CONFIRMED/CONDITIONAL/AT RISK verdict mechanism is functionally sound and may satisfy practitioners, but does not satisfy the literal C-09 pass condition. These two findings scope exactly what full C-09 implementation requires: (a) resolve the row-position definition conflict, and (b) add prior-run score storage outside the prompt.

**New pattern**: Partial implementation of a blocked criterion produces more actionable infrastructure requirements than continued deferral. V-05's 2/4 sub-condition result is more useful for unblocking C-09 than a 0/4 result from prior rounds.

---

## Recommended Golden Candidate

**V-05** is the recommended golden candidate:
- Combines all three R4 axes with no interference confirmed
- Strongest C-08 (4 mandated findings, C-09 compliance as required finding)
- Partial C-09 (2/4 sub-conditions) -- most advanced --validate attempt across all rounds
- C-11, C-15, C-16 enforced by exit conditions (strongest verification level in round)
- Gate 2 handles pinned row count separately (most sophisticated gate cardinality)

**V-04** is the closest alternative and the most analytically productive R4 variation for scoring accuracy research. Anchor rubric + benchmark row creates the most auditable displacement argument of any variation across all four rounds -- tier language chains from SETUP through SCORE to DECIDE without re-reading prose. Recommended if exit conditions are judged as execution overhead.

**V-02** is the recommended minimal variation for compliance enforcement research. Exit conditions as the sole axis confirms the prescriptive/confirmatory distinction in isolation.

---

```json
{"top_score": 98.75, "all_essential_pass": true, "new_patterns": ["Anchor rubric tier descriptions per role (1-3/4-6/7-9/10) make scoring interpretation output-verifiable by tier label, not raw integer -- tier language propagates from SETUP declaration through SCORE tier assignment into DECIDE sub-part (1) rationale, creating an auditable scoring chain across three phases. Combined with status-quo benchmark row (V-04/V-05), both candidates and the incumbent are scored on the same rubric so the displacement argument emerges from rubric tier comparison ('Strategy: 8 -- strong vs. SQ Strategy: 6 -- adequate'), not from DECIDE prose judgment.", "Phase exit condition checklists convert rubric criteria from evaluator-inferred to checklist-enforced -- a phase may not close until its checklist clears. Most significant impact: C-03 (collision check) and C-11 (generation-time enforcement) become preconditions for phase advance rather than post-output observations. The checklist form generalizes: any criterion requiring an artifact from within a phase can be encoded as a checklist item at the phase-close boundary, providing the strongest compliance enforcement mechanism available to inline prompting.", "Status-quo pre-scored as benchmark row in SETUP using anchor rubric; composite used as generation-time displacement floor ([BELOW-SQ: Strategy] marks and excludes candidates that cannot reach a higher Strategy tier); Row 1 in SCORE matrix with full 5-dimension scores; fraction-beating-SQ metric reported at DECIDE. Adds [below SQ threshold] as a fourth disqualification class applied before SCORE. The generation-time floor eliminates strategically weak candidates before they consume scoring effort and makes incumbency strength a measurable metric.", "Inline --validate branch (V-05) reaches 2/4 C-09 sub-conditions and isolates two blocking requirements: (1) row-position conflict -- C-09 requires Row 1 pinned but inertia-framing design places [STATUS QUO] at Row 1; (2) delta notation infrastructure gap -- C-09 requires prior stored run scores for delta comparison which inline prompting cannot retrieve. CONFIRMED/CONDITIONAL/AT RISK verdict is a functional substitute but not a C-09 compliance substitute. Full C-09 requires resolving the row-position definition or adding prior-run score storage outside the prompt."]}
```
