**scout-feasibility-rubric-v3-2026-03-14.md** written. Here's what changed:

**New criteria (from Round 2 excellence signals):**

| ID | Pattern | Source |
|----|---------|--------|
| C-13 | Reviewer role appears in section header | R2-E1: V-05's "PHASE 1 -- PM: BUDGET" vs all others naming roles only in prose |
| C-14 | Score-delta example fragment in amendment actions | R2-E2: V-01 + V-05's imitable surface vs V-02/V-03/V-04's bare requirement |

**Scoring formula updated:**
```
aspirational_pass / 6 * 10   (was / 4 * 10)
```
Total points unchanged at 100.

### v3 Scores

| Rank | Variation | C-13 | C-14 | v3 Composite | Golden? |
|------|-----------|------|------|--------------|---------|
| 1 | V-05 Golden synthesis | PASS | PASS | **100** | YES |
| 2 | V-01 FINDINGS-mirror | FAIL | PASS | **~98** | YES |
| 3 | V-02/V-03/V-04 | FAIL | FAIL | **~97** | YES |

**V-05 earns a perfect score for the first time** — it was ranked 1b in R2's enforcement-robustness analysis, but the rubric now reflects the structural advantage of role-attributed headers. The golden threshold stays non-load-bearing; discrimination has moved to the very top.
 outputs that contain an inline example matching the canonical format.

**Scoring change**: aspirational pool expands from 4 to 6 criteria. Formula denominator updated from 4 to 6. Total aspirational points remain 10.

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

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

Derived from trace findings (SF), Round 1 scorecard (R1), and Round 2 scorecard (R2):

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

v3 separates V-05 from the pack for the first time: role-attributed headers + example fragment together produce the only perfect score. All five remain golden. The golden threshold of 80 is not load-bearing at this round -- discrimination is at the top.

**C-13 pass distribution**: 1/5 (V-05 only)
**C-14 pass distribution**: 2/5 (V-01, V-05)
