Written to `simulations/quest/golden/scout-feasibility-golden-2026-03-14.md`.

The document contains:

1. **Frontmatter** — skill, target, date, rounds, rubric, score, status as specified
2. **Prompt body** — V-05 verbatim from the R4 variations file
3. **What made it golden** — 5 patterns distinguishing V-05 from V-01 (the simplest section-first design that also scores 100/100):
   - 5 independent inertia surfaces vs V-01's 3 — model drift loses one, four remain
   - Column anchors inertia at the traffic-light moment (same row as rating), not just before/after
   - AMENDMENTS carry a required third line per action (score-delta + inertia saved), closing the forward/backward loop
   - "Do not omit this line" reinforcement on all five surfaces, not just one
   - `inertia_cost_per_sprint` frontmatter field for machine-readable downstream aggregation

4. **Final rubric criteria summary** — all 17 criteria with the v5 formula, plus the 4-round quest summary table
RRED]."

## INFERENCE GATE
[Write as a contiguous block. All three required before INERTIA: STATUS QUO begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

## INERTIA: STATUS QUO
[Complete before PM: BUDGET. This table is the workaround baseline referenced throughout.]
| Current workaround | Sprint cost (hrs or $ estimate) | Risk if unchanged |
|--------------------|---------------------------------|-------------------|
| [Describe workaround] | [N hrs/sprint or $N/sprint] | [Risk consequence] |
[Add rows for each distinct workaround if multiple exist.]
Baseline: "Without this feature, the team spends approximately [N hrs/sprint or $N/sprint] on [workaround]."

## PM: BUDGET
[This section runs before Architect complexity ratings. Do not write any traffic light before this section is complete.]
Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

Budget chain:
  Estimated:  [SUM hrs from table]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

## ARCHITECT: COMPLEXITY
[Budget flag from PM: BUDGET: FLAG. Use this when assigning ratings below.]
[Traffic-light ratings are not valid before PM: BUDGET above is complete.]
[Do-nothing cost column: reference INERTIA: STATUS QUO and estimate hrs/sprint or $ per component. Required for every row -- do not leave blank.]

| Component | Rating               | Est. Hours | Rationale           | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|---------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] | [Workaround cost from INERTIA]    |
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] | [Workaround cost from INERTIA]    |

RED Blockers:
[For every RED-rated component, write one entry. All sub-fields required -- do not omit any line.]
- [Component]: [Why it is a blocker.] Lift condition: [What must specifically change.]
  Do-nothing cost: [Repeat workaround and cost from Do-nothing cost column above for this component. Do not omit this line.]
[If no RED components: write "No RED components."]

## STRATEGY: BUILD-VS-BUY
| Component | Recommendation             | Rationale |
|-----------|----------------------------|-----------|
| [Name]    | Build / Buy / Use existing | [Why]     |
| [Name]    | Build / Buy / Use existing | [Why]     |
[At least 50% of components must carry a recommendation.]

## VERDICT
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[Status-quo consequence from INERTIA: STATUS QUO. Ongoing cost: N hrs/sprint or $N/sprint. Do not omit this line.]"

[Complete only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] from the build."

[Complete only if label is FEASIBLE WITH CAVEATS:]
Prerequisites (every RED-rated component must appear):
1. [Prerequisite addressing first RED component]
2. [Prerequisite addressing second RED component]

## AMENDMENTS
[Numbered actions. Each traceable to a RED or YELLOW component from Architect or PM.]
[Two lines required per action. Fill in all brackets -- do not omit either line.]

1. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Manual workaround or third-party cost this action eliminates, from Do-nothing cost column. Estimate hrs/sprint or $. Do not omit this line.]

2. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Manual workaround or third-party cost this action eliminates, from Do-nothing cost column. Estimate hrs/sprint or $. Do not omit this line.]

[Continue for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source, inertia_cost_per_sprint.
```

---

## What Made It Golden

V-05 is the R4 synthesis target. The four patterns below distinguish it from V-01 (the simplest section-first design, also 100/100) and explain why V-05 is the recommended production prompt.

**1. Five independent inertia surfaces, not three.**
V-01 carries inertia in three places: the standalone INERTIA section, the "Do-nothing cost:" sub-field in RED Blockers, and the "Inertia impact:" line in VERDICT. V-05 adds two more: a pre-printed "Do-nothing cost" column in the ARCHITECT table (surface 4) and a pre-printed "Inertia saved:" field per AMENDMENT entry (surface 5). Each surface is an independent structural guarantee. Model drift that elides one surface does not lose the criterion -- four others still fire. V-01 has no fallback if one surface drops.

**2. Inertia anchored at the traffic-light moment, not only before and after.**
V-01's column is absent; inertia appears before rating (section) and after rating (blockers, VERDICT). V-05 adds the column so the do-nothing cost is visible in the same row where the traffic light is assigned. This forces holistic reasoning: the model reads rating, hours, rationale, and workaround cost together in one pass. V-01 requires the model to recall the INERTIA section when filling in each blocker; V-05 does not ask for recall -- the column pre-prints the slot in the rating row itself.

**3. AMENDMENTS carry a third required line per action.**
V-01 requires one line per amendment (score-delta only). V-05 requires two lines: score-delta and "Inertia saved:". The second line closes the loop between the forward-looking amendment (fix this) and the backward-looking cost (this is what you save). Combined with the "Do not omit this line" enforcement, this makes the AMENDMENTS section a standalone feasibility argument, not just a to-do list.

**4. "Do not omit this line" reinforcement on all five surfaces.**
V-01 carries this phrase on the one blocker sub-field. V-05 carries it on every pre-printed inertia fragment: ARCHITECT column annotation, RED Blocker "Do-nothing cost:" sub-field, VERDICT "Not building this means:" line, and AMENDMENTS "Inertia saved:" field. The phrase pattern is a behavioral anchor -- it reduces model elision of pre-printed fragments under context pressure.

**5. inertia_cost_per_sprint in frontmatter.**
V-05's artifact frontmatter includes `inertia_cost_per_sprint`, derived from the INERTIA table baseline. V-01 also carries this field (both inherited it from R3). V-02 and V-03 do not. This field makes the status-quo cost machine-readable for downstream topic aggregation.

---

## Final Rubric Criteria (v5)

**Formula:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

### Essential (60 pts)

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Traffic light per component | structure |
| C-02 | Composite score with label | structure |
| C-03 | Team and timeline inference disclosed | correctness |
| C-04 | Stack fallback disclosed when canonical files absent | correctness |
| C-05 | RED blockers enumerated with rationale | coverage |

### Recommended (30 pts)

| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Build-vs-buy recommendation per component | depth |
| C-07 | Scoped fallback score when full scope is infeasible | depth |
| C-08 | Prerequisites listed for conditional feasibility | coverage |

### Aspirational (10 pts, denominator 9)

| ID | Criterion | Category | V-05 |
|----|-----------|----------|------|
| C-09 | PM timeline overlay with complete sum-and-compare chain | depth | PASS |
| C-10 | Amendment actions list at close | behavior | PASS |
| C-11 | Inference gate block precedes component scoring | structure | PASS |
| C-12 | Budget analysis precedes complexity scoring | structure | PASS |
| C-13 | Reviewer role appears in section header | structure | PASS |
| C-14 | Score-delta example fragment in amendment actions | behavior | PASS |
| C-15 | Inertia framing anchors blockers against status-quo cost | depth | PASS |
| C-16 | Inertia section precedes traffic-light assignment | structure | PASS |
| C-17 | Multi-surface inertia redundancy | depth | PASS |

**V-05 score: 100 / 100 -- GOLDEN**

---

## Quest Summary

| Round | Rubric | Discriminator | V-05 score | Key finding |
|-------|--------|--------------|------------|-------------|
| R1 | v2 | C-09 / C-11 (inference gate) | ~87 | Inference disclosure scattered; budget not chained |
| R2 | v3 | C-13 / C-14 (role headers, score-delta fragment) | 100 | Pre-printed role headers + example fragment close both gaps |
| R3 | v4 | C-15 (inertia framing) | ~98.6 | Blockers forward-only; no do-nothing reference |
| R4 | v5 | C-16 / C-17 (section ordering, multi-surface) | 100 | All five inertia surfaces pre-printed; section-first ordering; no omission path |
