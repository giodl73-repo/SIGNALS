Written to `simulations/quest/rubrics/scout-feasibility-rubric-v5-2026-03-14.md`. Here's the summary of what changed:

---

## v5 changes

**Two new aspirational criteria** (denominator 7 -> 9):

| ID | Text | Category | What it captures |
|----|------|----------|-----------------|
| C-16 | Inertia section precedes traffic-light assignment | structure | R4 pattern 2 -- section-first placement forces holistic workaround reasoning *before* ratings are assigned; VERDICT/AMENDMENTS-only placement fails |
| C-17 | Multi-surface inertia redundancy | depth | R4 pattern 1 -- workaround baseline in 2+ independent structural locations; each surface is an independent guarantee that survives model drift |

**Formula update:**
```
aspirational_pass / 9 * 10   (was / 7)
```

**v5 separation at the top:**
- V-01 / V-04 / V-05 (section-first, 2+ surfaces) → **100/100**
- V-02 (column-only, no prior section) → **~98.9** (C-16 fail)
- V-03 (VERDICT+AMENDMENTS only, single-surface) → **~97.8** (C-16 + C-17 fail)

**Two new failure modes** added (R4-01 for C-16, R4-02 for C-17).

**Key analytical finding:** C-16 is a document-ordering property -- no instruction phrasing compensates for placing the inertia baseline after the traffic-light table. Mirrors the R3-02 finding for C-12.
ve already been assigned and the model cannot calibrate ratings against the workaround baseline.

**C-17 pass condition:** The inertia / workaround baseline appears in at least two independent structural locations (e.g., a dedicated section AND a table column; a dedicated section AND a per-RED blocker sub-field; a column AND an AMENDMENTS reference). Each surface is an independent structural guarantee that the criterion survives model drift. A single-surface inertia treatment satisfies C-15 but does not pass C-17.

**Formula:** aspirational denominator bumped from 7 to 9. Total points unchanged at 100.

**Round 4 result:** All five R4 variations scored 100/100 on the v4 rubric. C-16 and C-17 are the discriminators at this level. Section-first designs (V-01/V-04/V-05) pass both; do-nothing-column design (V-02) passes C-17 but fails C-16 (no standalone section before traffic lights); decision-surface-only design (V-03) fails both (VERDICT + AMENDMENTS placement, single-surface). V-05 remains the recommended golden candidate (5 independent inertia surfaces, section-first ordering).

---

## Criteria

### Essential (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Traffic light per component | essential | structure | Output contains a table or structured list with one row/entry per component. Each row has an explicit GREEN / YELLOW / RED label as its own field -- not embedded in prose. Missing table or prose-only format is a hard fail. |
| C-02 | Composite score with label | essential | structure | Output contains a numeric score (0-100) and one of the three labels: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE. Both must appear together in a dedicated verdict section. |
| C-03 | Team and timeline inference disclosed | essential | correctness | Output contains explicit statements of the inferred team size, sprint/timeline, and feature description before any component scoring. A sentence buried after scoring does not pass. Omitting any of the three values is a hard fail. |
| C-04 | Stack fallback disclosed when canonical files absent | essential | correctness | When no package.json / tsconfig.json / Cargo.toml is found, output contains an explicit disclosure sentence naming the fallback source (CLAUDE.md, program.yaml, etc.) and stating what was inferred from it. |
| C-05 | RED blockers enumerated with rationale | essential | coverage | Every RED-rated component is listed in a dedicated blockers section or inline note explaining *why* it is a blocker and what would need to change to lift the rating. |

### Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | Build-vs-buy recommendation per component | recommended | depth | At least 50% of components carry a Build / Buy / Use existing label. The Strategy role (or equivalent framing) must be attributed or implied. |
| C-07 | Scoped fallback score when full scope is infeasible | recommended | depth | When overall score is below 50 (NOT FEASIBLE), output includes a scoped alternative score with the constraint that enables it (e.g., "Scoped to flat binding only: 62/100"). Omitting this when blockers exist is a fail. |
| C-08 | Prerequisites listed for conditional feasibility | recommended | coverage | When score is FEASIBLE WITH CAVEATS, output contains a numbered or bulleted prerequisite list. All RED-rated items must be represented. |

### Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | PM timeline overlay with complete sum-and-compare chain | aspirational | depth | Output contains all four elements as a linked chain: (a) sum of per-component estimated hours, (b) available hours derived from inferred team size and timeline, (c) the delta between them, (d) an explicit over-budget or under-budget flag. Collecting both figures in separate sections without chaining them to a conclusion is a fail. |
| C-10 | Amendment actions list at close | aspirational | behavior | Output ends with a short action list (numbered) that converts RED findings into concrete next steps for the requesting team. Each action must be traceable to a specific RED or YELLOW component. |
| C-11 | Inference gate block precedes component scoring | aspirational | structure | The three inference disclosures (feature, team, timeline) appear as a contiguous block -- not scattered -- and that block precedes the first component traffic light in document order. A run that discloses inferences only after scoring has begun does not pass. |
| C-12 | Budget analysis precedes complexity scoring | aspirational | structure | The PM hour budget (available hours computation) appears in the output before or concurrent with per-component complexity ratings. This ensures the budget constraint is visible when the reader encounters the complexity scores. A run that computes hours only in a closing section does not pass. |
| C-13 | Reviewer role appears in section header | aspirational | structure | At least one section header in the output carries an explicit reviewer role label (e.g., "PM: BUDGET", "ARCHITECT: COMPLEXITY", "STRATEGY: BUILD-VS-BUY"). The role must be in the header text itself -- not only in surrounding instruction prose. A run that names roles only in paragraph text does not pass. |
| C-14 | Score-delta example fragment in amendment actions | aspirational | behavior | The amendment actions section contains an inline example matching the canonical format: "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." The example may use placeholder brackets or a filled-in instance. Stating the requirement without providing an imitable surface is a fail. |
| C-15 | Inertia framing anchors blockers against status-quo cost | aspirational | depth | The RED blockers section and/or amendment actions include a quantified comparison against the status-quo workaround. The rationale must reference what the team would do without this feature (manual process, third-party tool, deferred work) and the approximate cost of that path. Listing blockers and amendments without a do-nothing alternative is a fail. A column, note, or inline sentence per RED component each referencing the workaround cost is sufficient. |
| C-16 | Inertia section precedes traffic-light assignment | aspirational | structure | A dedicated inertia / status-quo section or equivalent contiguous block appears in document order before the first component traffic-light rating. Inertia framing that appears only in the VERDICT or AMENDMENTS sections does not pass -- the workaround baseline must be visible when the model assigns ratings, not after. Decision-surface-only inertia placement fails this criterion. |
| C-17 | Multi-surface inertia redundancy | aspirational | depth | The inertia / workaround baseline appears in at least two independent structural locations (e.g., a dedicated section AND a per-component table column; a dedicated section AND a per-RED blocker sub-field). Each surface is an independent structural guarantee that survives model drift. A single-surface inertia treatment (satisfying C-15) does not pass C-17. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

Derived from trace findings (SF), Round 1 scorecard (R1), Round 2 scorecard (R2), Round 3 scorecard (R3), and Round 4 scorecard (R4):

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| SF-01 | C-04 | Skill falls back to CLAUDE.md assertion but never tells the user |
| SF-02 | C-05 | Missing canonical schema not flagged as blocker; Architect scores complexity without noting the gap |
| SF-03 | C-03 | "One sprint" used in calculations without a visible inference statement |
| R1-01 | C-09 | Available hours and estimated hours computed in separate phases but never chained to an over/under conclusion (V-04, V-05) |
| R1-02 | C-11 | Inference disclosure present but scattered or post-scoring; gate not enforced (V-01) |
| R1-03 | C-12 | Hour budget computed after complexity scoring; budget constraint invisible when ratings are read (V-04, V-05) |
| R2-01 | C-13 | Reviewer roles named in instruction prose but absent from section headers; role disappears under header-only skimming (V-01, V-02, V-03, V-04) |
| R2-02 | C-14 | Amendment actions require score-delta statement but provide no example; model must interpret rather than imitate (V-02, V-03, V-04) |
| R3-01 | C-15 | Blockers and amendments present but framed only forward (what to fix) with no backward reference to workaround cost; comparative feasibility dimension absent (V-01, V-02, V-04, V-05) |
| R3-02 | C-12 | C-12 compliance is entirely determined by role ordering (PM-before-Architect). No instruction phrasing compensates for Architect-first or Strategy-first sequences. Variations that place Architect lead (V-04) or Strategy lead (V-01) structurally fail C-12 regardless of wording. |
| R4-01 | C-16 | Inertia framing placed only in VERDICT and/or AMENDMENTS after all traffic lights are assigned; workaround context unavailable during component rating so the model cannot calibrate RED thresholds against it. Decision-surface-only designs (V-03 pattern) produce shallower quantification even when C-15 passes. |
| R4-02 | C-17 | Single-surface inertia (column only, or section only) satisfies C-15 minimum but is a single point of model-drift failure. Any surface the model omits or collapses eliminates the inertia guarantee entirely. Two independent surfaces each provide a fallback if the other is elided. |

---

## Round Calibration Reference

### v2 Rubric -- Round 1 Results

| Rank | Variation | v1 Composite | v2 Composite | Golden (v2) |
|------|-----------|--------------|--------------|-------------|
| 1 | V-02 PM leads | 100 | 100 | YES |
| 2 | V-04 Interrogative | 95 | ~87 | YES |
| 3 | V-05 Phased+inertia | 95 | ~87 | YES |
| 4 | V-03 Prose | 83 | ~83 | NO (C-01 essential fail) |
| 5 | V-01 Baseline | 66 | ~64 | NO (C-03/C-04 essential fail) |

### v3 Rubric -- Round 2 Results

Round 2 was designed to close R1 structural gaps. All five variations scored 100/100 on the v2 rubric. v3 differentiates on the two new excellence patterns (C-13, C-14):

| Rank | Variation | C-13 | C-14 | Aspirational (6) | v3 Composite | Golden (v3) |
|------|-----------|------|------|-----------------|--------------|-------------|
| 1 | V-05 Golden synthesis | PASS | PASS | 6/6 = 10 | **100** | YES |
| 2 | V-01 FINDINGS-mirror | FAIL | PASS | 5/6 ~= 8 | **~98** | YES |
| 3 | V-02 Sum-first | FAIL | FAIL | 4/6 ~= 7 | **~97** | YES |
| 3 | V-03 Prohibitive | FAIL | FAIL | 4/6 ~= 7 | **~97** | YES |
| 3 | V-04 Interrogative+sum-first | FAIL | FAIL | 4/6 ~= 7 | **~97** | YES |

v3 separates V-05 from the pack for the first time: role-attributed headers + example fragment together produce the only perfect score. All five remain golden.

**C-13 pass distribution**: 1/5 (V-05 only)
**C-14 pass distribution**: 2/5 (V-01, V-05)

### v4 Rubric -- Round 3 Results

Round 3 was designed to close R3 structural gaps. All five variations scored 100/100 on the v3 rubric. v4 differentiates on the new excellence pattern (C-15):

| Rank | Variation | C-15 | Aspirational (7) | v4 Composite | Golden (v4) |
|------|-----------|------|-----------------|--------------|-------------|
| 1 | V-03 Inertia framing | PASS | 7/7 = 10 | **100** | YES |
| 2 | V-02 Template-completion | FAIL | 6/7 ~= 8.6 | **~98.6** | YES |
| 2 | V-05 Golden synthesis | FAIL | 6/7 ~= 8.6 | **~98.6** | YES |
| 4 | V-01 Strategy-first | FAIL | 5/7 ~= 7.1 | **~97.1** | YES |
| 4 | V-04 Architect-first | FAIL | 5/7 ~= 7.1 | **~97.1** | YES |

V-03 earns the perfect score: inertia framing adds a comparative feasibility dimension (status-quo cost) that C-05 and C-10 reward but do not require. All five remain golden.

Key analytical finding: C-12 compliance is entirely structural. V-01 (Strategy-first) and V-04 (Architect-first) cannot pass C-12 regardless of instruction phrasing -- PM ordering is the only lever.

**C-15 pass distribution**: 1/5 (V-03 only)

### v5 Rubric -- Round 4 Results

Round 4 was designed to close R3 structural gaps. All five variations scored 100/100 on the v4 rubric. v5 differentiates on the two new excellence patterns (C-16, C-17):

| Rank | Variation | C-16 | C-17 | Aspirational (9) | v5 Composite | Golden (v5) |
|------|-----------|------|------|-----------------|--------------|-------------|
| 1 | V-01 Inertia section | PASS | PASS | 9/9 = 10 | **100** | YES |
| 1 | V-04 Section + column | PASS | PASS | 9/9 = 10 | **100** | YES |
| 1 | V-05 Full synthesis | PASS | PASS | 9/9 = 10 | **100** | YES |
| 4 | V-02 Do-nothing column | FAIL | PASS | 8/9 ~= 8.9 | **~98.9** | YES |
| 5 | V-03 Decision-surface only | FAIL | FAIL | 7/9 ~= 7.8 | **~97.8** | YES |

Three section-first designs separate from the pack: standalone INERTIA section before ARCHITECT table passes C-16; standalone section plus any second surface passes C-17. Column-only design (V-02) passes C-17 but fails C-16 -- column placement is within the ARCHITECT table (concurrent with rating), not a dedicated prior block. Decision-surface-only design (V-03) fails both -- inertia context arrives only after all ratings are assigned, single-surface.

V-05 remains the recommended golden candidate: 5 independent inertia surfaces, section-first ordering, no omission path for any aspirational criterion. V-04 is the closest competitor (4 surfaces, leaner template).

Key analytical finding: C-16 compliance is a document-ordering property. No inertia instruction compensates for a design that places the workaround baseline after the traffic-light table.

**C-16 pass distribution**: 3/5 (V-01, V-04, V-05)
**C-17 pass distribution**: 4/5 (V-01, V-02, V-04, V-05)
