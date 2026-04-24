## corps-rob Round 7 -- Scorecard (rubric v6)

---

### Baseline Observation

All five variations claim to preserve the complete V-05 R6 architecture. The actual text requires independent verification. Critical divergence found: **V-02 and V-03 weaken the C-25 inertia citation constraint** from "cite a D-ID" to "reference the inertia contribution as a factor." This is an authoring gap introduced by writing V-02/V-03 without the D-ID Ref column -- the prose constraint drifted.

---

### C-01 through C-23 -- All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Stage Attribution | PASS | PASS | PASS | PASS | PASS | Stage {N}: {canonical-name} -- {Role Name} pattern present in all templates |
| C-02 Role-Loaded Perspective | PASS | PASS | PASS | PASS | PASS | Part 0 Dimension field + Constraint requiring Part 0-grounded finding per stage |
| C-03 Finding Specificity | PASS | PASS | PASS | PASS | PASS | "name the specific artifact or behavior... not a category label" inline guard in all |
| C-04 Ownership Floor | PASS | PASS | PASS | PASS | PASS | Owner column explicitly rejects "TBD" in all variations |
| C-05 GO/NO-GO Signal | PASS | PASS | PASS | PASS | PASS | `**TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**` present; V-03/V-05 calibration table explicitly exempts it from verdict-table scope |
| C-06 Cross-Stage References | PASS | PASS | PASS | PASS | PASS | Structured table with confirms/escalates/contradicts required; minimum 2 total |
| C-07 Handoff Packet | PASS | PASS | PASS | PASS | PASS | Cross-Stage Synthesis + Downstream Risk Shift both present with anti-copy constraints |
| C-08 ROB Summary | PASS | PASS | PASS | PASS | PASS | Overall Verdict + Inertia Resolution + Cross-Cutting Themes all present |
| C-09 Inter-Stage Blocker Detection | PASS | PASS | PASS | PASS | PASS | Blocker Field table present in all templates |
| C-10 Cross-Cutting Theme Elevation | PASS | PASS | PASS | PASS | PASS | Cross-Cutting Themes table with recurrence-elevation explanation required |
| C-11 Handoff Packet (full) | PASS | PASS | PASS | PASS | PASS | Forwarded refs + synthesis + risk shift with substance constraint |
| C-12 Stage-Boundary Blocker Field | PASS | PASS | PASS | PASS | PASS | Blocker Field table with YES/NO + downstream stage + reason present |
| C-13 Inertia Anchor | PASS | PASS | PASS | PASS | PASS | INERTIA ANCHOR section with Displacement Map D-IDs present in all |
| C-14 Briefing Envelope | PASS | PASS | PASS | PASS | PASS | Part 1 BRIEFING ENVELOPE present for Stages 2-6 with ROLE/LENS/KEY CONCERNS/PRIOR-STAGE ESCALATIONS |
| C-15 Anti-Redundancy | PASS | PASS | PASS | PASS | PASS | Downstream Risk Shift explicitly prohibited from restating Prior-Stage Lens Impact |
| C-16 Lens-Impact/Risk-Shift Pair | PASS | PASS | PASS | PASS | PASS | Both Prior-Stage Lens Impact table and Downstream Risk Shift slot present |
| C-17 Lens-Impact/Risk-Shift Guard | PASS | PASS | PASS | PASS | PASS | "Do not restate Prior-Stage Lens Impact" constraint enforces separation |
| C-18 Explicit Lens Fill Field | PASS | PASS | PASS | PASS | PASS | Dimension field in Part 0 with role-title-alone rejection guidance |
| C-19 Stage 1 Lens Coverage | PASS | PASS | PASS | PASS | PASS | Stage Identity at Stage 1 carries "(Must contain dimension, not just title.)" |
| C-20 Part 0 Pre-Envelope Block | PASS | PASS | PASS | PASS | PASS | `### Part 0 -- LENS ACTIVATION / Fill before reading any prior-stage context.` present |
| C-21 KEY CONCERNS Back-Ref | PASS | PASS | PASS | PASS | PASS | "selected through the Lens declared in Part 0" phrase required verbatim in KEY CONCERNS cell |
| C-22 Three-Hop Chain | PASS | PASS | PASS | PASS | PASS | Prior-Stage Lens Impact requires "the orientation declared in Part 0" named as governing lens |
| C-23 Chain Health Summary | PASS | PASS | PASS | PASS | PASS | LENS ACTIVATION CHAIN HEALTH table with 6-stage rows present in all |

Essential: **5/5 PASS** all variations. Recommended: **3/3 PASS** all variations.

---

### C-24 through C-26 -- Differential Scoring

#### C-24 -- Finding Slot Structural Completeness

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | 6-column findings table; all slots carry `[fill]` with rejection language; column footer: "An empty D-ID Ref cell where Inertia Stance is RESISTANT and Severity is HIGH is a format failure." Per-finding structural guarantee on all 6 slots. |
| V-02 | PASS | 5-column findings table; Severity/Owner/Resolution all carry inline guards with explicit rejection phrases ("TBD does not satisfy", "needs attention does not satisfy"). Fill-slot discipline preserved for 5 columns. |
| V-03 | PASS | Same 5-column structure as V-02; same inline rejection guards. PASS. |
| V-04 | PASS | Same 6-column structure as V-01 with identical slot guards. PASS. |
| V-05 | PASS | Same 6-column structure; all slot guards present. PASS. |

#### C-25 -- Displacement Map with Labeled D-IDs

The rubric requires: "When a stage's Inertia Stance is RESISTANT and a finding is HIGH severity, the finding must cite a D-ID from the register."

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Inertia Check constraint: "at least 1 finding must cite the inertia D-ID in **its D-ID Ref column**." D-ID Ref column converts the requirement from prose note to per-row cell obligation. Stronger than rubric baseline. |
| V-02 | PARTIAL | Inertia Check constraint: "at least 1 finding must **reference the inertia contribution as a factor**." Omits the D-ID cite requirement -- an executing model can satisfy this phrase without naming D-01 or D-02. Displacement Map with D-IDs present (first half of C-25 passes); finding-level citation obligation weakened (second half partial). |
| V-03 | PARTIAL | Same weakened constraint as V-02: "reference the inertia contribution as a factor." Same partial: Displacement Map present, finding-level D-ID cite not required. |
| V-04 | PASS | Inertia Check constraint: "must cite the inertia D-ID in its D-ID Ref column." Same as V-01. PASS. |
| V-05 | PASS | Same explicit D-ID Ref column cite constraint as V-01/V-04. PASS. |

#### C-26 -- Table-First Findings Format with Inline Rejection Guards

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | 6-column table; all six columns carry typed rejection guards. D-ID Ref column: "[fill: D-{ID}... otherwise N/A]" with explicit format-failure notice at footer. |
| V-02 | PASS | 5-column table; Severity ("no other values"), Finding ("not a category label"), Owner ("TBD does not satisfy"), Resolution ("needs attention does not satisfy") all carry inline rejection guards. F-ID column has no typed guard but this is the key column, not a substance column. Meets C-26 spirit at same level as V-05 R6. |
| V-03 | PASS | Same 5-column structure as V-02 with same inline guards. PASS. |
| V-04 | PASS | Same 6-column structure as V-01. PASS. |
| V-05 | PASS | Same 6-column structure. PASS. |

---

### Composite Scores

Scoring formula: Essential (5 x 12 = 60) + Recommended (3 x 10 = 30) + Aspirational (N_pass, max contributable = 10).

Aspirational raw for all variations: C-09 to C-23 = 15 passes (preserved from V-05 R6). C-24, C-25, C-26 vary per above.

| Variation | C-24 | C-25 | C-26 | Aspirational Raw | Contributable | Composite | Rank |
|-----------|------|------|------|-----------------|---------------|-----------|------|
| V-01 | 1 | 1 | 1 | 18.0 | 10 | **100** | T-1 |
| V-04 | 1 | 1 | 1 | 18.0 | 10 | **100** | T-1 |
| V-05 | 1 | 1 | 1 | 18.0 | 10 | **100** | T-1 |
| V-02 | 1 | 0.5 | 1 | 17.5 | 10 | **100** | T-4 |
| V-03 | 1 | 0.5 | 1 | 17.5 | 10 | **100** | T-4 |

**Tie-break (raw count):** V-01 = V-04 = V-05 at 18.0; V-02 = V-03 at 17.5.

**Within-18 tie-break (excellence signal density):** V-05 > V-04 > V-01. V-05 carries all three R7 axes; V-04 carries two; V-01 carries one. Under v6 this does not change the score, but V-05 presents the highest density of patterns that would seed v7 criteria.

**Final rank:** V-05 (1st) | V-04 (2nd) | V-01 (3rd) | V-02 (4th, tie) | V-03 (4th, tie)

---

### Excellence Signals

These patterns appear in R7 top-scoring variations and are not captured by C-01 through C-26. They are candidates for rubric v7.

**Signal 1 -- D-ID Ref as a structural column (V-01, V-04, V-05)**
Any cross-reference between an earlier structured decision (the Displacement Map) and a later artifact (finding row) should be a named column in the findings table, not a prose footnote. Empty cell = format failure at the same visibility level as empty Owner cell. Pattern: *row-level citation columns for upstream-registered entities.*

**Signal 2 -- Standardized blocker propagation token (V-02, V-04, V-05)**
The `[BLOCKER: {F-ID} from {stage name}]` label creates a machine-scannable token format for an inter-stage obligation. Any item that must flow forward in a stage sequence should have a token format that is detectable by inspection, not just present in a general list. V-02 also introduces a **Blocker Resolution Status table** in the ROB Summary -- closing the audit loop on blockers with a resolution-status column per BLOCKER=YES raised. Pattern: *named-token propagation + end-of-ROB resolution audit for every inter-stage obligation.*

**Signal 3 -- Verdict Calibration table with per-stage rule citation (V-03, V-05)**
A severity x resolution-status matrix maps finding profiles to verdict outcomes deterministically. The Stage Verdict section adds a "Calibration Row Applied" field requiring the model to cite which row drove the verdict. This makes C-05's GO/NO-GO signal auditable from the calibration rule, not from model judgment. The ROB Summary Overall Verdict also carries a "Calibration Row Applied" field. Pattern: *decision calibration table + mandatory rule citation at every decision gate.*

**V-05 structural observation -- full enforcement chain**
V-05 achieves the only fully closed enforcement chain: RESISTANT+HIGH finding -> D-ID Ref column -> BLOCKED verdict (calibration row) -> [BLOCKER: F-ID] token in next stage Part 1 -> Blocker Resolution Status in ROB Summary. No step in this chain depends on prose quality alone. This is the defining architecture marker for v7 scope.

**Authoring gap to note**
V-02 and V-03 exhibit a C-25 regression (PARTIAL) not flagged in the R7 hypothesis. When adding a new axis without the D-ID Ref column, the prose-level inertia citation constraint should explicitly preserve "cite the D-ID from the register" language. The absence is not intentional per the R7 stated goals; it's a template-authoring gap. A v7 rubric criterion for inertia citation should be column-level only, not prose-dependent.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["D-ID Ref as a structural column in findings table -- converts prose citation obligation to per-row cell with empty-cell format failure", "Standardized blocker propagation token [BLOCKER: F-ID from stage] in PRIOR-STAGE ESCALATIONS with Blocker Resolution Status audit table in ROB Summary", "Verdict Calibration table with mandatory Calibration Row Applied field at Stage Verdict and ROB Summary -- makes C-05 GO/NO-GO auditable from a deterministic rule citation"]}
```
