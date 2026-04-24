## quest-golden — Round 1 Scorecard

**Rubric:** v1 | **Variations:** V-01..V-05 | **Trace:** placeholder (design-quality evaluation)

---

### Scoring Key

| Call | Meaning |
|------|---------|
| PASS | Criterion structurally addressed by the variation design |
| PARTIAL | Implicitly covered or addressed with noted risk |
| FAIL | Not addressed |

Composite formula: `(essential_score/5)*60 + (recommended_score/3)*30 + (aspirational_score/2)*10`
PARTIAL counts as 0.5 in score arithmetic; PASS required for `all_essential_pass`.

---

### V-01 — Role Sequence

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | CONVERGENCE JUDGE as final distinct role with explicit mandate to check both gates simultaneously |
| C-02 Golden prompt as full skill body | essential | PARTIAL | Skill body names roles with mandates — full-body output implied but not explicitly required |
| C-03 Final rubric as standalone artifact | essential | PARTIAL | RUBRIC KEEPER role manages rubric lifecycle; standalone write-out not stated |
| C-04 QU2 precedes QU3 | essential | PASS | ANALYST and CRITERION AUTHOR are distinct sequential roles; ordering is unbypassable by construction |
| C-05 Rubric present at loop start | essential | PASS | RUBRIC KEEPER is the first role; load-before-start is structurally enforced |
| C-06 Per-round iteration record | recommended | PARTIAL | Role sequence implies records per round but format/fields not specified |
| C-07 Excellence signal isolation | recommended | PARTIAL | No dedicated isolation step; ANALYST role covers general analysis |
| C-08 Criterion proposal completeness | recommended | PARTIAL | CRITERION AUTHOR role writes proposals; tier + pass-condition fields not prescribed |
| C-09 "What made it golden" narrative | aspirational | FAIL | No explanatory or narrative emphasis in the role design |
| C-10 Persistent gap identification | aspirational | FAIL | Not addressed |

**Essential score:** (1+0.5+0.5+1+1)/5 = 4.0/5 → ×60 = **48**
**Recommended score:** (0.5+0.5+0.5)/3 = 1.5/3 → ×30 = **15**
**Aspirational score:** 0/2 → ×10 = **0**
**Composite: 63** | all_essential_pass: NO (C-02, C-03 partial)

---

### V-02 — Output Format (Tables Throughout)

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | Convergence check table with two required columns makes dual-gate failure visible by inspection |
| C-02 Golden prompt as full skill body | essential | PARTIAL | Format discipline enforces structured output; full-body requirement not stated |
| C-03 Final rubric as standalone artifact | essential | PARTIAL | Artifact discipline implied; standalone write-out not explicit |
| C-04 QU2 precedes QU3 | essential | PARTIAL | Table structure maps rounds but doesn't order QU2/QU3 steps within a round |
| C-05 Rubric present at loop start | essential | PARTIAL | Table 1 requires rubric reference per variation; initialization gate not explicit |
| C-06 Per-round iteration record | recommended | PASS | 4-column round-log table directly addresses all C-06 fields |
| C-07 Excellence signal isolation | recommended | PASS | Contrast column in Table 3 structurally enforces isolation vs description |
| C-08 Criterion proposal completeness | recommended | PASS | Proposal table with fixed rows enforces tier + pass-condition presence |
| C-09 "What made it golden" narrative | aspirational | FAIL | Tables suppress mechanism narrative; contrast column captures delta not explanation |
| C-10 Persistent gap identification | aspirational | FAIL | Not addressed |

**Essential score:** (1+0.5+0.5+0.5+0.5)/5 = 3.0/5 → ×60 = **36**
**Recommended score:** 3/3 → ×30 = **30**
**Aspirational score:** 0/2 → ×10 = **0**
**Composite: 66** | all_essential_pass: NO (C-02..C-05 partial)

---

### V-03 — Lifecycle Emphasis (Hard Phase Gates)

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | PHASE 4 with two-condition exit table; PHASE 3 artifact must exist before PHASE 4 can run |
| C-02 Golden prompt as full skill body | essential | PARTIAL | Protocol document structure describes loop; full skill body output not explicitly required |
| C-03 Final rubric as standalone artifact | essential | PARTIAL | Phases cover rubric use; write-out as standalone file not stated in any phase EXIT CONDITION |
| C-04 QU2 precedes QU3 | essential | PASS | QU2 and QU3 named as ordered steps within PHASE 3; stated sequence |
| C-05 Rubric present at loop start | essential | PASS | PHASE 0 INITIALIZATION with rubric as entry condition |
| C-06 Per-round iteration record | recommended | PASS | Entry/exit conditions per phase generate structured per-round documentation |
| C-07 Excellence signal isolation | recommended | PARTIAL | PHASE 3 covers analysis but no dedicated isolation step; contrast not formalized |
| C-08 Criterion proposal completeness | recommended | PARTIAL | PHASE 3 includes criterion proposal step; tier + pass-condition not in EXIT CONDITION |
| C-09 "What made it golden" narrative | aspirational | FAIL | Protocol register discourages mechanism explanation |
| C-10 Persistent gap identification | aspirational | FAIL | Not addressed |

**Essential score:** (1+0.5+0.5+1+1)/5 = 4.0/5 → ×60 = **48**
**Recommended score:** (1+0.5+0.5)/3 = 2.0/3 → ×30 = **20**
**Aspirational score:** 0/2 → ×10 = **0**
**Composite: 68** | all_essential_pass: NO (C-02, C-03 partial)

---

### V-04 — Phrasing Register (Conversational / Intent-First)

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PARTIAL | Two-bullet convergence condition stated; variation notes softer language may weaken gate precision — risk acknowledged |
| C-02 Golden prompt as full skill body | essential | PARTIAL | Intent-first prose invites completeness but does not require it |
| C-03 Final rubric as standalone artifact | essential | PARTIAL | Not addressed in design description |
| C-04 QU2 precedes QU3 | essential | PASS | "QU2 must precede QU3 because..." grounds the ordering in purpose; model reasons toward compliance |
| C-05 Rubric present at loop start | essential | PARTIAL | Intent-first style implies it but no structural gate |
| C-06 Per-round iteration record | recommended | PARTIAL | Not explicitly formatted; prose style may produce records but fields not fixed |
| C-07 Excellence signal isolation | recommended | PARTIAL | Explanatory style may surface what distinguished the winner but no isolation mechanism |
| C-08 Criterion proposal completeness | recommended | PARTIAL | Intent framing explains why criteria matter; field completeness not enforced |
| C-09 "What made it golden" narrative | aspirational | PASS | Explanatory register explicitly predicted to produce mechanism narrative; strongest C-09 design of the five |
| C-10 Persistent gap identification | aspirational | FAIL | Not addressed |

**Essential score:** (0.5+0.5+0.5+1+0.5)/5 = 3.0/5 → ×60 = **36**
**Recommended score:** (0.5+0.5+0.5)/3 = 1.5/3 → ×30 = **15**
**Aspirational score:** 1/2 → ×10 = **5**
**Composite: 56** | all_essential_pass: NO (C-01..C-03, C-05 partial)

---

### V-05 — Combination: Inertia Framing + Lifecycle Emphasis

| Criterion | Tier | Call | Evidence |
|-----------|------|------|----------|
| C-01 Dual convergence termination | essential | PASS | Phase gates from lifecycle axis; PHASE 4 convergence check requires both conditions |
| C-02 Golden prompt as full skill body | essential | PARTIAL | Loop produces winner output; full-body format not explicitly required |
| C-03 Final rubric as standalone artifact | essential | PARTIAL | Phases include rubric management; standalone artifact write-out not in any EXIT CONDITION |
| C-04 QU2 precedes QU3 | essential | PASS | Phase gates with QU2 and QU3 as ordered steps within PHASE 3 |
| C-05 Rubric present at loop start | essential | PASS | PHASE 0 explicitly initializes rubric and inertia baseline together |
| C-06 Per-round iteration record | recommended | PASS | Phase entry/exit structure generates per-round documentation |
| C-07 Excellence signal isolation | recommended | PASS | Inertia baseline as named primary competitor; contrast = "what loop adds vs unconstrained" — sharpest isolation mechanism in the set |
| C-08 Criterion proposal completeness | recommended | PARTIAL | PHASE 3 includes criterion proposal; tier + pass-condition fields not specified in EXIT CONDITION |
| C-09 "What made it golden" narrative | aspirational | PASS | "What Made It Golden" framed as "what inertia missed" — mechanistic by construction |
| C-10 Persistent gap identification | aspirational | FAIL | Not addressed in either contributing axis |

**Essential score:** (1+0.5+0.5+1+1)/5 = 4.0/5 → ×60 = **48**
**Recommended score:** (1+1+0.5)/3 = 2.5/3 → ×30 = **25**
**Aspirational score:** 1/2 → ×10 = **5**
**Composite: 78** | all_essential_pass: NO (C-02, C-03 partial)

---

### Summary Scoreboard

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite | All Essential |
|-----------|------|------|------|------|------|------|------|------|------|------|-----------|---------------|
| V-01 Role Sequence | PASS | PARTIAL | PARTIAL | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | FAIL | FAIL | **63** | NO |
| V-02 Output Format | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS | PASS | PASS | FAIL | FAIL | **66** | NO |
| V-03 Lifecycle Gates | PASS | PARTIAL | PARTIAL | PASS | PASS | PASS | PARTIAL | PARTIAL | FAIL | FAIL | **68** | NO |
| V-04 Conversational | PARTIAL | PARTIAL | PARTIAL | PASS | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PASS | FAIL | **56** | NO |
| **V-05 Inertia+Lifecycle** | **PASS** | PARTIAL | PARTIAL | **PASS** | **PASS** | **PASS** | **PASS** | PARTIAL | **PASS** | FAIL | **78** | NO |

**Rank:** V-05 (78) > V-03 (68) > V-02 (66) > V-01 (63) > V-04 (56)

---

### Excellence Signals — V-05

**Signal 1: Inertia baseline as named reference point**
V-05 is the only variation that names the unconstrained output as an explicit artifact (PHASE 0). Every subsequent contrast in PHASE 3 is measured against "what did the loop add that the inertia prompt did not produce" rather than comparing variations against each other. This makes C-07 isolation structurally automatic — the contrast is with a fixed reference, not a moving target.

**Signal 2: Combination axis yields emergent C-09 coverage**
Neither lifecycle-alone (V-03) nor inertia-alone would hit C-09. The combination produces a natural "What Made It Golden" framing: the answer is always "what the inertia baseline lacked." This is a reuse pattern — semantic anchors provide the vocabulary for mechanism narratives that protocol documents cannot generate alone.

**Signal 3: Phase gates prevent inertia baseline from being skipped**
V-05 places the inertia initialization inside PHASE 0 with an explicit artifact. Because PHASE 3's entry condition requires PHASE 0's output, the inertia comparison cannot be deferred or omitted without breaking the gate chain.

---

### Cross-Variation Gap Analysis

**C-02 and C-03 are universally PARTIAL** — no variation in R1 explicitly requires (a) that the golden prompt be written as a full deployable skill body or (b) that the final rubric be written to a standalone file. These are both essential criteria. The gap is structural: none of the five axes (role-sequence, output-format, lifecycle, phrasing, inertia) directly address artifact writing as a terminal act. R2 should test an axis that enforces terminal artifact production (e.g., an "output contract" axis or explicit loop-exit checklist).

**C-10 universally fails** — no variation incorporates ablated criteria tracking. This aspirational criterion has no natural home in any current axis. Would require an explicit "what the rubric is NOT measuring" section.

---

```json
{"top_score": 78, "all_essential_pass": false, "new_patterns": ["inertia baseline as named primary contrast anchor sharpens C-07 signal isolation by measuring loop contribution against a fixed unconstrained reference", "lifecycle phase gates combined with semantic anchors yield emergent mechanism narrative coverage that neither axis produces alone"]}
```
