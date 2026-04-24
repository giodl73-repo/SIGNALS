## discover-competitors-alt R10 — Scoring (Rubric v9)

### Criterion Evaluation

**Approach**: All 5 variations build on R9 V-05 (which already satisfies C-37, C-38, C-39). The R10 innovations (C-40/C-41/C-42 candidates) are extra-rubric under v9. I evaluate all 39 rubric criteria per variation.

---

### Essential Criteria — C-01 to C-05 (12 pts each)

All five variations carry the complete structural skeleton: competitor table with C0 row, GATE 4 (inertia gate identifying C0), Phase 3 WHITESPACE validation, Phase 5 findings table, AMEND section. **PASS / 5 across all variations.**

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |
| C-05 | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60/60 all variations**

---

### Recommended Criteria — C-06 to C-08 (10 pts each)

**C-06 (Inertia stickiness reasoning)**: GATE 4 in all variations requires a concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — explicitly prohibiting a category label. **PASS all.**

**C-07 (Web-verified competitive claim)**: GATE 1 in all variations mandates an inline WebSearch URL per competitor row; suppresses any row where citation is absent. **PASS all.**

**C-08 (AMEND section with 3 actionable adjustments)**: All variations have AMEND as a 3-row structured table (C-38 satisfied, which implies C-08). Each row names adjustment + output change + slots + gates. **PASS all.**

**Recommended subtotal: 30/30 all variations**

---

### Aspirational Criteria — C-09 to C-39 (5 pts each, 31 criteria)

#### C-09 to C-16

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Cross-dimensional whitespace finding | PASS | PASS | PASS | PASS | PASS | Phase 4 proof requires both dimensions simultaneously |
| C-10 | Table-stakes grounding per finding | PASS | PASS | PASS | PASS | PASS | Anchor column structurally coerced; name-only is malformed |
| C-11 | Fully-cited competitor table | PASS | PASS | PASS | PASS | PASS | GATE 1 applies per row, not just one row |
| C-12 | Self-negating cross-dimensional finding | PASS | PASS | PASS | PASS | PASS | REDUCTION-1 and REDUCTION-2 each show what single dimension loses |
| C-13 | Claim-level finding anchors | PASS | PASS | PASS | PASS | PASS | `Row C{N}, {attribute}: "{value}"` enforces attribute-level cell reference |
| C-14 | AMEND as proof validator | PASS | PASS | PASS | PASS | PASS | Row 1 (shift focus) requires GATE 3 re-run with both reductions; proof rerun failure named |
| C-15 | Inline anchor tag before proof block | PASS | PASS | PASS | PASS | PASS | SOURCE is structurally first row of Phase 4 table |
| C-16 | Gate failure naming | PASS | PASS | PASS | PASS | PASS | Every gate has named failure: "Citation gate failure," "Anchor gate failure," "Proof structure failure," "Inertia naming failure" |

#### C-17 to C-25

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-17 | WHITESPACE grounded by attribute absence | PASS | PASS | PASS | PASS | PASS | ABSENCE-EVIDENCE row requires per-row attribute evidence for every competitor including C0 |
| C-18 | NOT ACCEPTABLE examples for anchoring | PASS | PASS | PASS | PASS | PASS | GATE 2 and Phase 5 both name "name-only" failure pattern with explicit NOT ACCEPTABLE examples |
| C-19 | Synthesis-first output contracts | PASS | PASS | PASS | PASS | PASS | Slot 5 (Focus-scope evidence), slot 3, slot 6 all declared in OUTPUT CONTRACTS before producing phases |
| C-20 | Structural column coercion for anchoring | PASS | PASS | PASS | PASS | PASS | Format template `Row C{N}, {attribute}: "{value}"` makes name-only syntactically non-conforming |
| C-21 | Gate-as-section with PASS/FAIL table | PASS | PASS | PASS | PASS | PASS | All gates are named sections with ≥2 rows (Check/Pass condition/Failure state) |
| C-22 | INERTIA-REF per-finding citation | PASS | PASS | PASS | PASS | PASS | GATE 4 row 3 requires `vs. INERTIA-REF — {reinforces/challenges/contextualizes}: {phrase}` per finding; token name mandatory |
| C-23 | Output contract slot format specification | PASS | PASS | PASS | PASS | PASS | All 6 slots have label + format template in OUTPUT CONTRACTS |
| C-24 | Phase-to-contract back-references | PASS | PASS | PASS | PASS | PASS | Phases reference "(fills slot N, label, PREFLIGHT > OUTPUT CONTRACTS)" full path |
| C-25 | Cross-table structural coercion | PASS | PASS | PASS | PASS | PASS | Anchor column coerced in Phase 2 (collection) and Phase 5 (synthesis) independently |

#### C-26 to C-39

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-26 | Consolidated PREFLIGHT gate block | PASS | PASS | PASS | PASS | PASS | All numbered gates (1-4) inside PREFLIGHT; prose FOCUS CHECK in V-02/V-03 is not a gate, doesn't violate |
| C-27 | Machine-readable phase assignment | PASS | PASS | PASS | PASS | PASS | "Filled by phase" column present in all OUTPUT CONTRACTS |
| C-28 | OUTPUT CONTRACTS co-located within PREFLIGHT | PASS | PASS | PASS | PASS | PASS | OUTPUT CONTRACTS is a subsection of PREFLIGHT in all variations |
| C-29 | Full-path back-reference labels | PASS | PASS | PASS | PASS | PASS | "PREFLIGHT > OUTPUT CONTRACTS" path used when C-28 applies |
| C-30 | Write-token instruction within INERTIA-REF gate | PASS | PASS | PASS | PASS | PASS | GATE 4 write row: "Write at this step: `INERTIA-REF = [C0 name]: [phrase]`" |
| C-31 | Write-token as structural gate row | PASS | PASS | PASS | PASS | PASS | Write directive is the Pass condition of a dedicated table row with named Failure state ("Inertia write failure") |
| C-32 | OUTPUT CONTRACTS declared first within PREFLIGHT | PASS | PASS | PASS | PASS | PASS | All 5: PREFLIGHT header confirms "OUTPUT CONTRACTS is declared first" before GATE 0/EXECUTION DEPENDENCY/Gates 1-4 |
| C-33 | Forward-declared cross-dimensional proof slot | PASS | PASS | PASS | PASS | PASS | Slot 5 (Focus-scope evidence) appears in OUTPUT CONTRACTS table with pipe-delimited format requirement |
| C-34 | Inter-slot dependency column in output contract | PASS | PASS | PASS | PASS | PASS | "Required by" column present naming upstream slot dependencies per row |
| C-35 | Syntactic format template for cross-dimensional proof slot | PASS | PASS | PASS | PASS | PASS | Slot 5 format: `REDUCTION-1 NO: [...] \| REDUCTION-2 NO: [...] \| THEREFORE: [...]` — parse-ready pipe-delimited template |
| C-36 | Cross-dimensional proof as structural PASS/FAIL table | PASS | PASS | PASS | PASS | PASS | Phase 4: 4-row table SOURCE/REDUCTION-1/REDUCTION-2/THEREFORE, each with required value + failure state |
| C-37 | WHITESPACE validation as CANDIDATE-first PASS/FAIL table | PASS | PASS | PASS | PASS | PASS | All 5: Phase 3 is 4-row table, CANDIDATE first, ABSENCE-EVIDENCE, GAP-CONFIRMED, vs-INERTIA-REF, each with failure state |
| C-38 | AMEND as structured table with Slots re-filled and Gates re-run columns | PASS | PASS | PASS | PASS | PASS | All 5: AMEND is a table with those exact column labels; 3 rows; cause-effect-slots-gates queryable by column |
| C-39 | EXECUTION DEPENDENCY table in PREFLIGHT | PASS | PASS | PASS | PASS | PASS | All 5: PREFLIGHT contains EXECUTION DEPENDENCY table; GATE 4 row has "— (root)" in Reads slot |

**Aspirational subtotal: 155/155 all variations**

---

### Extra-Rubric Differentiators (Candidate C-40/C-41/C-42 — not scored under v9)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-40**: FOCUS GATE as named PASS/FAIL gate in PREFLIGHT | YES | NO (prose before PREFLIGHT) | NO (prose before PREFLIGHT) | YES | YES |
| **C-41**: Phase 3 vs-INERTIA-REF uses slot 6 ternary-token format | NO (prose) | YES | NO (prose) | YES | YES |
| **C-42**: EXECUTION DEPENDENCY "Prerequisite steps" column | NO | NO | YES | NO | YES |

---

### Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (155) | Total (245) | Grade |
|-----------|---------------|------------------|-------------------|-------------|-------|
| V-01 | 60 | 30 | 155 | **245** | Exceptional |
| V-02 | 60 | 30 | 155 | **245** | Exceptional |
| V-03 | 60 | 30 | 155 | **245** | Exceptional |
| V-04 | 60 | 30 | 155 | **245** | Exceptional |
| V-05 | 60 | 30 | 155 | **245** | Exceptional |

**Rubric v9 grade band: Exceptional ≥ 231. All 5 variations score 245/245.**

---

### Ranking Under v9

All variations tie at 245/245 under rubric v9. The rubric has no unmet criterion to differentiate them. Ranking falls to candidate criteria:

1. **V-05** — All three innovations (C-40 + C-41 + C-42): GATE 4 root confirmed from four independent positions
2. **V-04** — Two innovations (C-40 + C-41): every gate in PREFLIGHT + Phase 3 format isomorphism
3. **V-01** — One innovation (C-40): FOCUS GATE closes last prose pre-execution gap
4. **V-02** — One innovation (C-41): Phase 3 ternary format coercion
5. **V-03** — One innovation (C-42): Prerequisite steps column (step-level DAG dual readability)

---

### Excellence Signals from V-05

1. **Four-position root confirmation for GATE 4**: OUTPUT CONTRACTS "Required by: Root" (slot level) + EXECUTION DEPENDENCY "Reads slot: — (root)" (data level) + EXECUTION DEPENDENCY "Prerequisite steps: None (root)" (step level) + GATE 0 which resolves the execution start state before the DAG is read. No other step or slot is confirmed from four independent structural positions.

2. **Phase-3/Phase-5 syntactic isomorphism**: Both WHITESPACE vs-INERTIA-REF rows and FINDINGS INERTIA-REF-DELTA cells use identical ternary format. A single token-presence check (`reinforces / challenges / contextualizes` + mechanism phrase) validates both. This removes the format asymmetry that existed when whitespace comparisons were prose.

3. **GATE 0 closes the last prose pre-execution gap**: In V-02/V-03/R9 baseline, FOCUS CHECK is prose before PREFLIGHT — a model must look outside the gate system to know which slots activate. V-01/V-04/V-05 move this into GATE 0 with explicit branch failure states ("Focus activation failure," "Focus inactivation failure"), making focus conditionality a first-class structural gate like GATE 1–4.

---

### Scorecard Written

```json
{"top_score": 245, "all_essential_pass": true, "new_patterns": ["FOCUS GATE as named PASS/FAIL gate within PREFLIGHT — focus conditionality machine-readable at gate level with activation/inactivation branch failure states; last prose pre-execution check moves into the structural gate system", "Phase 3 vs-INERTIA-REF row coerced to slot 6 ternary-token format — whitespace-level and finding-level INERTIA-REF comparisons syntactically isomorphic; both phases checkable by the same token-presence rule", "EXECUTION DEPENDENCY Prerequisite steps column — step ordering readable by step name without slot-tracing; GATE 4 root confirmed from two orthogonal DAG columns (Reads slot: root + Prerequisite steps: None)"]}
```
