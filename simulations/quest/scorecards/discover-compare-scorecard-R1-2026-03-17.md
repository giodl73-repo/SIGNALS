## discover-compare — Round 1 Scorecard

### Per-Variation Evaluation

---

#### V-01 — Inertia-First Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | Structure explicitly sequences Option A analysis (4 dimensions) then Option B analysis (4 dimensions) before matrix |
| C-02 independent inertia | PASS | VERDICT A and VERDICT B are in physically separate named sections; each carries an explicit "compare against ANCHOR[0] only — not against Option B/A" constraint |
| C-03 decision matrix | PASS | Matrix with Option 0 column assembled after bilateral analysis phases |
| C-04 explicit recommendation | PASS | Recommendation step follows gate, stated before any supporting prose |
| C-05 build/no-build gate | PASS | Gate phase present between matrix and recommendation |
| C-06 differentiated risk | PASS | Separate analysis sections reduce symmetric copying; ANCHOR binding makes identical inertia commentary detectable |
| C-07 actionable AMEND | PASS | AMEND section in structure (format consistent with V-02 evidence) |
| C-08 Option 0 in matrix | PASS | Option 0 defined first as ANCHOR[0]; named column in matrix |
| C-09 audience calibration | FAIL | No audience register declared or conditional branching; single-register output |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 1/2 → 5**
**Composite: 95 | Golden: YES**

---

#### V-02 — Scored Grid (1–5 Numeric Scale)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | STEP 2 scores Option A on all 4 dimensions; STEP 3 scores Option B on all 4 dimensions independently |
| C-02 independent inertia | PASS | STEP 3 explicitly: "Do not score Option B's inertia relative to Option A — score it against the status quo" |
| C-03 decision matrix | PASS | STEP 4 is a 5-row table with Option 0 / Option A / Option B columns and total row |
| C-04 explicit recommendation | PASS | STEP 6 opens with "Recommendation: Option A / Option B / Neither / Conditional on {X}" — not deferrable |
| C-05 build/no-build gate | PASS | STEP 5 explicit threshold test: inertia score ≤ 2 for both → surface "build neither" |
| C-06 differentiated risk | PASS | STEP 3 mandates: "Name Option B's top risk. Must differ from Option A's top risk unless you explain why they are the same." Strongest enforcement of any variation. |
| C-07 actionable AMEND | PASS | Three concrete AMEND slots: Add Option C (add column, rerun totals), Weight dimension (specify multiplier, recalculate), Shift audience (exec vs engineering re-render) |
| C-08 Option 0 in matrix | PASS | STEP 4 matrix has "Option 0" as named column with "anchor" and "baseline" cells |
| C-09 audience calibration | PARTIAL | Audience shift available in AMEND but not activated in primary flow; main prompt is single-register |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 1.5/2 → 7.5**
**Composite: 97.5 | Golden: YES**

---

#### V-03 — Phase-Explicit with Named Boundary Markers

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | Phases 1A–4A cover all 4 dimensions for Option A; Phases 1B–4B cover all 4 for Option B — omission visible as missing phase label |
| C-02 independent inertia | PASS | PHASE 2A: "Compare Option A against STATUS QUO from Phase 0 — not against Option B." PHASE 2B: mirror instruction for Option B. Physical separation plus explicit exclusion. |
| C-03 decision matrix | PASS | Phase 5 assembles matrix from output tokens; structural assembly makes missing scores visible |
| C-04 explicit recommendation | PASS | Phase 7 is dedicated recommendation phase |
| C-05 build/no-build gate | PASS | Phase 6 is dedicated gate phase before recommendation |
| C-06 differentiated risk | PASS | Separate phases 3A/3B produce independent risk assessments; `> Output:` tokens make symmetric copy-paste detectable |
| C-07 actionable AMEND | PASS | Phase 8 AMEND present |
| C-08 Option 0 in matrix | PASS | Phase 0 defines STATUS QUO; Phase 5 matrix includes it as baseline column assembled from `STATUS QUO:` output token |
| C-09 audience calibration | FAIL | No audience register phase; no conditional branching in shown structure |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 1/2 → 5**
**Composite: 95 | Golden: YES**

---

#### V-04 — Conversational / Question-Driven Register

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | Two independent question blocks — one per option — each covering all four dimension questions |
| C-02 independent inertia | PASS | "Would teams bother?" posed per-option with explicit "independently" markers; question framing discourages template-symmetric responses |
| C-03 decision matrix | PASS | Table follows the question blocks |
| C-04 explicit recommendation | PASS | Explicit recommendation step after table |
| C-05 build/no-build gate | PASS | "Is either option even worth building?" is a natural stopping point in the question sequence |
| C-06 differentiated risk | PASS | Fresh reasoning per option reduces symmetric risk, though question framing alone doesn't mandate distinct risks — assessed PASS given structural separation |
| C-07 actionable AMEND | PASS | AMEND present |
| C-08 Option 0 in matrix | PASS | Option 0 column in table per variation design |
| C-09 audience calibration | PARTIAL | Question register implies audience sensitivity ("Would teams bother?" reads conversationally); no explicit register declaration or conditional branch |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 1.5/2 → 7.5**
**Composite: 97.5 | Golden: YES**

---

#### V-05 — Combined: Phase-Explicit + Inertia-First + Audience-Conditional

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 bilateral dimensions | PASS | Bilateral phases 1A–4B cover all 4 dimensions per option; TOKEN RECALL at matrix phase cross-checks all 8 output tokens |
| C-02 independent inertia | PASS | ANCHOR[0] committed at Phase 0 with binding rule; Phases 2A/2B carry independence constraints on VERDICT sentences; TOKEN RECALL at inertia phase enforces recall |
| C-03 decision matrix | PASS | Phase 5 matrix with Option 0 column labeled with ANCHOR[0] value |
| C-04 explicit recommendation | PASS | Phase 7 delivers recommendation with register-conditional framing; not deferrable |
| C-05 build/no-build gate | PASS | Phase 6 dedicated gate phase |
| C-06 differentiated risk | PASS | Separate phases 3A/3B; independence constraints prevent cross-contamination |
| C-07 actionable AMEND | PASS | Phase 8 AMEND includes register override path as concrete slot |
| C-08 Option 0 in matrix | PASS | ANCHOR[0] declared at Phase 0 and required as named column at Phase 5 via TOKEN RECALL |
| C-09 audience calibration | PASS | Phase 0 dual-purpose: declares ANCHOR[0] AND sets audience register; Phase 7 has explicit conditional branching (exec vs engineering framing); activated in primary flow, not deferred to AMEND |

**Essential: 4/4 → 60 | Recommended: 3/3 → 30 | Aspirational: 2/2 → 10**
**Composite: 100 | Golden: YES**

---

### Summary Table

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 Inertia-First | 4/4 | 3/3 | 1/2 | **95** | YES |
| V-02 Scored Grid | 4/4 | 3/3 | 1.5/2 | **97.5** | YES |
| V-03 Phase-Explicit | 4/4 | 3/3 | 1/2 | **95** | YES |
| V-04 Conversational | 4/4 | 3/3 | 1.5/2 | **97.5** | YES |
| V-05 Combined | 4/4 | 3/3 | 2/2 | **100** | YES |

**Rank: V-05 > V-02 = V-04 > V-01 = V-03**

---

### Excellence Signals from V-05

**1. Dual-purpose Phase 0** — A single phase simultaneously commits ANCHOR[0] (status quo) and sets the audience register. Two orthogonal functions resolved in one declaration, with no phase bloat. This is the pattern that activates C-09 in the primary flow rather than deferring it to AMEND.

**2. Token recall binding** — Requiring output phases to echo the Phase 0 ANCHOR[0] declaration at the inertia phase and matrix phase turns structural coherence into a detectable property. If the model drifts from the status quo definition mid-comparison, the TOKEN RECALL instruction surfaces the drift.

**3. Independence constraint on VERDICT sentences** — Rather than relying on physical separation alone (V-03) or explicit exclusion instructions alone (V-02), V-05 imposes a sentence-level constraint: VERDICT-A sentences may not reference Option B, and vice versa. This is the tightest enforcement mechanism for C-02 across all variations.

**4. Three-phase enforcement architecture** — Declare (Phase 0) → Recall (Phases 2A/2B/5/7) → Constrain (VERDICT independence). The three-layer design addresses the same failure mode (C-02 drift) from three angles simultaneously, with each layer catching a different mode of slippage.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dual-purpose declaration phase that commits two orthogonal values (status quo anchor + audience register) simultaneously", "token recall binding: output phases required to echo earlier declarations to make structural drift detectable"]}
```
