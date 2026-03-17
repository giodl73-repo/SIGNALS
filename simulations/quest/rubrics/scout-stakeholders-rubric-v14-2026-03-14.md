## scout-stakeholders rubric — v14

**v14 written.** Two new criteria extracted from Round 13 excellence signals (V-04/V-05 axis):

| ID | Name | Source | Dependency |
|----|------|--------|------------|
| C-35 | Pre-phase format constraint propagation | V-01/V-04 axis | C-33 |
| C-36 | Attribution-fused synthesis notation | V-02/V-04 axis | C-34 |

**Updated totals:** 28 aspirational × 5 = 140 pts; **max 230 pts**. Golden threshold (>= 80) unchanged.

**Under v14 (Round 13 re-scored):**
- V-03 → 210/230 (C-33, C-34, C-35, C-36 absent)
- V-01 → 220/230 (C-35 PASS; C-36 not satisfiable — C-34 absent)
- V-02 → 220/230 (C-36 PASS; C-35 not satisfiable — C-33 absent)
- V-04 → 230/230 (C-35 PASS, C-36 PASS — first perfect score under v14)
- V-05 → 230/230 (C-35 PASS, C-36 PASS)

**Distinction logic:**

**C-35 — Pre-phase format constraint propagation** (depth, 5 pts)
The global format enforcement mechanism required by C-33 is placed at the prompt header before Phase 1 begins, establishing format obligations at construction time for every downstream structural step. The header placement propagates the constraint forward without requiring per-step repetition; FAIL_NO_PARSEABLE_FORMAT placed at the prompt header fires at the first offending structural output in execution order, rather than as a post-hoc audit applied after all steps complete.

- Distinct from C-33: C-33 requires uniform parseable format across all structural elements; C-35 requires the enforcement point to be the prompt header before Phase 1, making the constraint active at construction time rather than checked retrospectively
- Not satisfiable if C-33 is absent

**C-36 — Attribution-fused synthesis notation** (depth, 5 pts)
Synthesis cells use `field: value (Step X / C-YY)` inline notation, structurally fusing attribution with synthesis content within each cell. No separate attribution sub-step is required; the citation is encoded within the cell value itself, not collected in a footnote block or dedicated attribution section appended after the synthesis readout. FAIL_NO_ATTRIBUTION fires at the synthesis step if any field cell lacks fused inline citation in this notation form. A variation that satisfies C-34 via a post-synthesis attribution appendix (all five fields cited, but not fused inline within cells) = C-34 PASS, C-36 FAIL.

- Distinct from C-34: C-34 requires per-field step citation; C-36 requires that citation to be structurally fused inline within each synthesis cell using `field: value (source)` notation rather than separated into a distinct sub-step or section
- Not satisfiable if C-34 is absent

---

### v13 to v14 changes summary

| Criterion | Name | Type | Dependency |
|-----------|------|------|------------|
| C-35 | Pre-phase format constraint propagation | depth | C-33 |
| C-36 | Attribution-fused synthesis notation | depth | C-34 |

Aspirational count: 26 → 28. Max: 220 → 230. Golden threshold unchanged.

---

### v12 to v13 changes (retained for history)

Two new criteria extracted from Round 12:

| ID | Name | Source | Dependency |
|----|------|--------|------------|
| C-33 | Machine-parseable structural format | V-03 axis | C-02 |
| C-34 | Attributed synthesis rows | V-04 axis | C-32 |

**C-33 — Machine-parseable structural format** (depth, 5 pts)
Every structural output in the prompt — every grid, risk table, scoring table, prefill table, communication schedule, and synthesis readout — uses a machine-parseable format (Markdown pipe table or equivalent key-value structure) uniformly across all steps. FAIL_NO_PARSEABLE_FORMAT fires at any structural step that produces output in non-parseable prose or freeform layout. The constraint applies uniformly across all structural elements, not only at the synthesis step.

A variation can satisfy C-32 (synthesis step produces all five required fields) while presenting synthesis rows as prose paragraphs with no table or key-value structure (C-33 FAIL).

- Distinct from C-02: C-02 is satisfied by a grid in any legible form; C-33 requires parseable format across all structural elements
- Distinct from C-32: C-32 requires the synthesis step to exist with required fields; C-33 requires all structural outputs — including but not limited to synthesis rows — to use parseable format
- Not satisfiable if C-02 is absent

**C-34 — Attributed synthesis rows** (depth, 5 pts)
Each synthesis row produced by the C-32 synthesis step includes per-field source attribution — each of the five required fields (grid position, engagement window, conflict exposure, champion status, comms frame type) carries an explicit citation naming the originating step or criterion that produced it (e.g., "grid position: Phase 3 / C-02", "engagement window: Step 5a", "conflict exposure: Step 1a / C-06", "champion status: Step 5b", "comms frame type: Step 6a / C-13"). FAIL_NO_ATTRIBUTION must be present as an inline gate label at the synthesis step if attribution is absent from any field. Synthesis rows that contain all five required field values but no source citation per field = FAIL.

- Distinct from C-32: C-32 requires field presence; C-34 requires each field to name its originating step
- Distinct from C-22: C-22 requires the amendment mandate to enumerate structural targets; C-34 requires per-field attribution within synthesis rows themselves
- Not satisfiable if C-32 is absent

Point totals updated: aspirational 24 → 26 (120 → 130 pts); max 210 → 220. Golden threshold unchanged.

**Round 12 under v13:** V-03 scores 215/220 (C-33 PASS; C-34 FAIL). V-04 scores 215/220 (C-33 FAIL; C-34 PASS). V-01, V-02, V-05 each score 210/220 (C-33 FAIL, C-34 FAIL).

---

### v11 to v12 changes (retained for history)

Two new criteria extracted from Round 11 V-05 (dense synthesis + trajectory probe):

**C-31 — Stakeholder trajectory probe column** (depth, 5 pts)
Adds a Trajectory column to the Power/Interest grid with per-row directional assessment (ascending toward advocate / stable / descending toward risk) plus observable-signal rationale. FAIL_NO_TRAJECTORY enforces structural presence. Amendment mandate gains "trajectory assessments" as an eligible target.

- Distinct from C-02: C-02 is a static snapshot of current position; C-31 is a forward probe of directional movement
- Distinct from C-28: C-28 covers champion relationship durability only; C-31 covers every stakeholder in the grid
- Not satisfiable if C-02 absent

**C-32 — Dense cross-phase synthesis readout** (depth, 5 pts)
A dedicated post-analysis synthesis step collapses grid position, engagement window, conflict exposure, champion status, and frame type into a single compact row per stakeholder or per quadrant. FAIL_NO_SYNTHESIS gates the step. Amendment mandate gains "synthesis readout rows" alongside all prior target types.

- Distinct from individual analysis steps (C-02, C-05, C-13, C-30, C-31): each produces one attribute type; C-32 aggregates across phases
- Distinct from C-22: C-22 names targets in the mandate; C-32 requires the synthesis artifact itself to exist
- Not satisfiable if C-02 absent

Point totals updated: aspirational 22 → 24 (110 → 120 pts); max 200 → 210. Golden threshold unchanged.

Round 12 confirms three structural properties:
- Column-integrated trajectory (Phase 3 construction time) satisfies C-31 without requiring a separate post-grid sub-step; FAIL_NO_TRAJECTORY placed at grid construction step is structurally tighter than placement at a deferred section.
- Per-quadrant synthesis (4 rows) satisfies C-32's "per stakeholder or per quadrant" pass condition; quadrant-level aggregation preserves all five required fields with no information loss on C-31.
- Format register is structurally irrelevant to C-01 through C-32 criterion satisfaction: machine-parseable and prose-rich formats both achieve 210/210 under v12.

---

### v10 to v11 changes (retained for history)

**C-30 — Engagement window derivation and comms binding** (depth, 5 pts)
Step 5a is a dedicated sub-step that derives a per-stakeholder or per-quadrant engagement window from the Power/Interest grid quadrant position and the gatekeeper lead-time data established in Step 1c. Champion steps renumber to 5b/5c/5d. Three structural requirements all present: (1) Engagement Window column in the Power/Interest grid with FAIL_NO_ENGAGEMENT_WINDOW. (2) Step 6b comms timing anchors must fall within the Step 5a derived window. (3) Amendment mandate enumerates "Step 5a engagement window summaries."

- Distinct from C-05: C-05 is satisfied by any relative timing anchor; C-30 requires that anchor to be derived from and bounded by a prior window step
- Distinct from C-08: C-08 tags individual gatekeepers; C-30 synthesizes them into a grid-level window column that constrains downstream comms
- Not satisfiable if C-05 or C-08 is absent

Point totals updated: aspirational 21 → 22 (105 → 110 pts); max 195 → 200. Golden threshold unchanged.

---

### v9 to v10 changes (retained for history)

Three new criteria extracted from Round 9:

**C-27 — Champion depth scoring table** (depth, 5 pts)
Step 5b: scoring table across Authority / Proximity / Commitment (each 1-5), composite >= 9 threshold gate with inline failure label.

- Distinct from C-04: C-04 confirms a champion + action exists; C-27 requires multi-dimensional fitness scoring
- Not satisfiable if C-04 absent

---

### Complete criterion register (v14)

| ID | Name | Type | Points | Dependency |
|----|------|------|--------|------------|
| C-01 | … | base | 5 | — |
| … | … | … | 5 | … |
| C-27 | Champion depth scoring table | depth | 5 | C-04 |
| C-28 | Champion relationship durability | depth | 5 | C-04 |
| C-29 | … | depth | 5 | … |
| C-30 | Engagement window derivation and comms binding | depth | 5 | C-05, C-08 |
| C-31 | Stakeholder trajectory probe column | depth | 5 | C-02 |
| C-32 | Dense cross-phase synthesis readout | depth | 5 | C-02 |
| C-33 | Machine-parseable structural format | depth | 5 | C-02 |
| C-34 | Attributed synthesis rows | depth | 5 | C-32 |
| C-35 | Pre-phase format constraint propagation | depth | 5 | C-33 |
| C-36 | Attribution-fused synthesis notation | depth | 5 | C-34 |

**Totals:** 28 aspirational × 5 = 140 pts aspirational; **max 230 pts**. Golden threshold >= 80 unchanged.

---

### Round 13 scoring under v14 (max 230)

| Variation | C-30 | C-31 | C-32 | C-33 | C-34 | C-35 | C-36 | Score | Gap |
|-----------|------|------|------|------|------|------|------|-------|-----|
| V-01 Pipe Tables Throughout | PASS | PASS | PASS | PASS | FAIL | PASS | N/A | 220/230 | −10 |
| V-02 Per-Cell Row Citations | PASS | PASS | PASS | FAIL | PASS | N/A | PASS | 220/230 | −10 |
| V-03 Inertia Pseudo-Stakeholder | PASS | PASS | PASS | FAIL | FAIL | N/A | N/A | 210/230 | −20 |
| V-04 Combined C-33 + C-34 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 230/230 | 0 |
| V-05 Lifecycle + C-33 + C-34 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | 230/230 | 0 |

**Notes:**
- C-35 marked N/A for V-02 and V-03 (C-33 absent — not satisfiable)
- C-36 marked N/A for V-01 and V-03 (C-34 absent — not satisfiable)
- V-01 passes C-35: global format constraint placed at prompt header before Phase 1; FAIL_NO_PARSEABLE_FORMAT at header propagates to all downstream structural steps at construction time
- V-02 passes C-36: synthesis cells use `field: value (Step X / C-YY)` inline notation; attribution fused within each cell, no separate attribution section required
- V-04 and V-05 pass both: header-level propagation (C-35) and fused inline notation (C-36) inherited from the combined axis
- V-03 (Inertia as Named Pseudo-Stakeholder): additive framing extends Step 1b and C-02 without conflicting with any prior criterion; no new failure vectors for C-01 through C-34; gap attributable solely to absent C-33/C-34/C-35/C-36
