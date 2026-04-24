Done. Here's what changed in v4:

**New criterion:**

| ID | Text | Category |
|----|------|----------|
| C-15 | Inertia framing anchors blockers against status-quo cost | aspirational / depth |

Pass condition: RED blockers and/or amendment actions include a quantified do-nothing alternative (manual process, third-party tool, deferred work + approximate cost). Listing blockers without a workaround reference is a fail.

**Formula:** aspirational denominator bumped from 6 to 7. Total points unchanged at 100.

**Common failure modes:** Two R3 entries added — R3-01 (C-15 absent in V-01/V-02/V-04/V-05) and R3-02 (analytical confirmation that C-12 is a structural ordering problem, not a phrasing problem).

**Round 3 results added** to the calibration reference. V-03 is now the sole 100/100 variation — inertia framing is the discriminator at the top.
------|---------|
| 1 | V-03 Inertia framing | PASS | **100** | YES |
| 2 | V-02 Template-completion | FAIL | ~98.6 | YES |
| 2 | V-05 Golden synthesis | FAIL | ~98.6 | YES |
| 4 | V-01 Strategy-first | FAIL | ~97.0 | YES |
| 4 | V-04 Architect-first | FAIL | ~97.0 | YES |

V-03 earns the perfect score: its inertia axis adds a comparative feasibility dimension that C-05 and C-10 credit but do not require. All five variations remain golden.

---

## Criteria

### Essential (60 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Traffic light per component | essential | structure | Output contains a table or structured list with one row/entry per component. Each row has an explicit GREEN / YELLOW / RED label as its own field — not embedded in prose. Missing table or prose-only format is a hard fail. |
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
| C-11 | Inference gate block precedes component scoring | aspirational | structure | The three inference disclosures (feature, team, timeline) appear as a contiguous block — not scattered — and that block precedes the first component traffic light in document order. A run that discloses inferences only after scoring has begun does not pass. |
| C-12 | Budget analysis precedes complexity scoring | aspirational | structure | The PM hour budget (available hours computation) appears in the output before or concurrent with per-component complexity ratings. This ensures the budget constraint is visible when the reader encounters the complexity scores. A run that computes hours only in a closing section does not pass. |
| C-13 | Reviewer role appears in section header | aspirational | structure | At least one section header in the output carries an explicit reviewer role label (e.g., "PM: BUDGET", "ARCHITECT: COMPLEXITY", "STRATEGY: BUILD-VS-BUY"). The role must be in the header text itself — not only in surrounding instruction prose. A run that names roles only in paragraph text does not pass. |
| C-14 | Score-delta example fragment in amendment actions | aspirational | behavior | The amendment actions section contains an inline example matching the canonical format: "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." The example may use placeholder brackets or a filled-in instance. Stating the requirement without providing an imitable surface is a fail. |
| C-15 | Inertia framing anchors blockers against status-quo cost | aspirational | depth | The RED blockers section and/or amendment actions include a quantified comparison against the status-quo workaround. The rationale must reference what the team would do without this feature (manual process, third-party tool, deferred work) and the approximate cost of that path. Listing blockers and amendments without a do-nothing alternative is a fail. A column, note, or inline sentence per RED component each referencing the workaround cost is sufficient. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

Derived from trace findings (SF), Round 1 scorecard (R1), Round 2 scorecard (R2), and Round 3 scorecard (R3):

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

v3 separates V-05 from the pack for the first time: role-attributed headers + example fragment together produce the only perfect score. All five remain golden. The golden threshold of 80 is not load-bearing at this round — discrimination is at the top.

**C-13 pass distribution**: 1/5 (V-05 only)
**C-14 pass distribution**: 2/5 (V-01, V-05)

### v4 Rubric -- Round 3 Results

Round 3 was designed to close R2 structural gaps. All five variations scored 100/100 on the v3 rubric. v4 differentiates on the new excellence pattern (C-15):

| Rank | Variation | C-15 | Aspirational (7) | v4 Composite | Golden (v4) |
|------|-----------|------|-----------------|--------------|-------------|
| 1 | V-03 Inertia framing | PASS | 7/7 = 10 | **100** | YES |
| 2 | V-02 Template-completion | FAIL | 6/7 ~= 8.6 | **~98.6** | YES |
| 2 | V-05 Golden synthesis | FAIL | 6/7 ~= 8.6 | **~98.6** | YES |
| 4 | V-01 Strategy-first | FAIL | 5/7 ~= 7.1 | **~97.1** | YES |
| 4 | V-04 Architect-first | FAIL | 5/7 ~= 7.1 | **~97.1** | YES |

V-03 earns the perfect score: inertia framing adds a comparative feasibility dimension (status-quo cost) that C-05 and C-10 reward but do not require. All five remain golden.

Key analytical finding: C-12 compliance is entirely structural. V-01 (Strategy-first) and V-04 (Architect-first) cannot pass C-12 regardless of instruction phrasing — PM ordering is the only lever.

**C-15 pass distribution**: 1/5 (V-03 only)
