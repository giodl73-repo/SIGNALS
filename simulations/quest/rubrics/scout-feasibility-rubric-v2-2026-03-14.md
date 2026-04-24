**scout-feasibility-rubric-v2-2026-03-14.md** written. Here's what changed:

**New criteria (from Round 1 excellence signals):**

| ID | Pattern | Source |
|----|---------|--------|
| C-11 | Inference gate block precedes component scoring | V-02's "do not proceed until visible" vs V-01's instruction-only disclosure |
| C-12 | Budget analysis precedes complexity scoring | V-02's PM-first ordering makes the hour budget constraint visible when ratings are read |

**C-09 tightened** — pass condition now requires all four chain elements explicitly: sum of estimates, available hours, delta, over/under flag. V-04/V-05 fail because they collect both inputs but never complete the chain.

**Scoring formula updated:**
```
aspirational_pass / 4 * 10   (was / 2 * 10)
```
Total points unchanged at 100. V-04/V-05 drop from 95 to ~87 in v2 — still golden (recommended alone = 90), but V-02's structural advantage is now captured in the rubric.
 scores 90 — above the 80 golden threshold even with no aspirational points.

### v2 Changes (from Round 1 excellence signals)

Three new patterns observed in V-02 (the only perfect score) and absent in V-04/V-05:

1. **Gate beats instruction** — V-01 said "DISCLOSE these inferences explicitly." V-02 said "Do not proceed until they are visible." The gate is why C-03/C-04 flip from FAIL to PASS. C-11 rewards visible gate evidence in the output itself: the three inference values appear as a contiguous block before any component scoring.

2. **PM-first ordering** — Placing PM budget computation before component complexity scoring makes the hour budget structurally unavoidable. V-04/V-05 collected hours but never let the budget constraint inform complexity ratings. C-12 rewards outputs where the budget analysis visibly precedes or accompanies complexity scoring.

3. **Explicit sum-and-compare chain** — V-05 had both inputs (available hours, estimated hours) in separate phases but never chained them to an over/under conclusion. V-04 collected available hours but never summed per-component estimates. The chain requires four elements: sum of estimates, available hours, delta, and an explicit over/under flag. C-09 pass condition is tightened in v2 to require all four.

**Scoring change**: aspirational pool expands from 2 to 4 criteria. Formula denominator updated. Total aspirational points remain 10.

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

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

Derived from trace findings (SF) and Round 1 scorecard (R1):

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| SF-01 | C-04 | Skill falls back to CLAUDE.md assertion but never tells the user |
| SF-02 | C-05 | Missing canonical schema not flagged as blocker; Architect scores complexity without noting the gap |
| SF-03 | C-03 | "One sprint" used in calculations without a visible inference statement |
| R1-01 | C-09 | Available hours and estimated hours computed in separate phases but never chained to an over/under conclusion (V-04, V-05) |
| R1-02 | C-11 | Inference disclosure present but scattered or post-scoring; gate not enforced (V-01) |
| R1-03 | C-12 | Hour budget computed after complexity scoring; budget constraint invisible when ratings are read (V-04, V-05) |

---

## Round 1 Calibration Reference

| Rank | Variation | v1 Composite | v2 Composite | Golden (v2) |
|------|-----------|--------------|--------------|-------------|
| 1 | V-02 PM leads | 100 | 100 | YES |
| 2 | V-04 Interrogative | 95 | ~87 | YES |
| 3 | V-05 Phased+inertia | 95 | ~87 | YES |
| 4 | V-03 Prose | 83 | ~83 | NO (C-01 essential fail) |
| 5 | V-01 Baseline | 66 | ~64 | NO (C-03/C-04 essential fail) |

v2 tightens separation at the top: V-02 remains the only perfect score. V-04/V-05 drop from 95
to ~87 because C-09 now requires the complete chain (both fail R1-01) and neither satisfies the
new C-11/C-12. Golden threshold still reached by V-04/V-05 on recommended alone (90 pts without
aspirational); losing aspirational points does not drop them below 80.
