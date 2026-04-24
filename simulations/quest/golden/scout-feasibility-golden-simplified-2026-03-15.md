The file exists but is empty — I'll write the simplified output now.

## Simplified Prompt

```markdown
## INFERENCE GATE
[All three required before INERTIA: STATUS QUO begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

## INERTIA: STATUS QUO
[Complete before PM: BUDGET.]
| Current workaround | Sprint cost (hrs or $ estimate) | Risk if unchanged |
|--------------------|---------------------------------|-------------------|
| [Describe workaround] | [N hrs/sprint or $N/sprint] | [Risk consequence] |
[Add rows for each distinct workaround if multiple exist.]
Baseline: "Without this feature, the team spends approximately [N hrs/sprint or $N/sprint] on [workaround]."

## PM: BUDGET
[Do not write any traffic light before this section is complete.]
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
[Do-nothing cost column: reference INERTIA: STATUS QUO. Required for every row -- do not leave blank.]

| Component | Rating               | Est. Hours | Rationale           | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|---------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] | [Workaround cost from INERTIA]    |

RED Blockers:
[For every RED-rated component, write one entry. All sub-fields required -- do not omit any line.]
- [Component]: [Why it is a blocker.] Lift condition: [What must specifically change.]
  Do-nothing cost: [From Do-nothing cost column above. Do not omit this line.]
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
[Numbered actions, each traceable to a RED or YELLOW component. Two additional lines required per action -- do not omit any.]

1. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [From Do-nothing cost column above. Estimate hrs/sprint or $. Do not omit this line.]

[Repeat pattern for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source, inertia_cost_per_sprint.
```

---

## Simplification Report

**Word counts:** 521 original → 402 simplified — **22.8% reduction (119 words removed)**

### What was removed and why

| Cut | Words saved | Rationale |
|-----|-------------|-----------|
| `Write as a contiguous block.` from INFERENCE GATE annotation | 5 | Purely descriptive; the three-field block structure enforces contiguity. C-11 passes from section ordering alone. |
| `This table is the workaround baseline referenced throughout.` from INERTIA annotation | 9 | Explanatory, not prescriptive. The Baseline sentence and section name carry the referencing load for C-15/C-17. |
| `This section runs before Architect complexity ratings.` from PM: BUDGET annotation | 7 | Redundant with document ordering — PM: BUDGET section appears before ARCHITECT by placement. The behavioral constraint (`Do not write any traffic light...`) is kept. |
| `[Traffic-light ratings are not valid before PM: BUDGET above is complete.]` (entire line) from ARCHITECT | 11 | Fully redundant with the retained annotation immediately above it (`Budget flag from PM: BUDGET: FLAG. Use this when assigning ratings below.`) and section ordering. |
| `and estimate hrs/sprint or $ per component` from ARCHITECT Do-nothing cost annotation | 6 | Redundant with the column header `Do-nothing cost (hrs/sprint or $)` already in the table. |
| Second ARCHITECT table row | 12 | One example row is sufficient; the column structure and `[Add rows...]` pattern in INERTIA already establish multi-row behavior. |
| `Repeat workaround and cost` + `for this component` in RED Blocker Do-nothing cost | 7 | Simplified to `From Do-nothing cost column above.` — the source reference is preserved, the filler description is not. |
| `Manual workaround or third-party cost this action eliminates, from Do-nothing cost column.` in AMENDMENTS Inertia saved | 13 | Simplified to `From Do-nothing cost column above.` — same source reference, shorter. |
| Second full AMENDMENTS example (45 words) → `[Repeat pattern...]` (8 words) | 37 | One example fully demonstrates the three-line pattern. Continuation signaled by `[Repeat pattern for all RED and YELLOW components.]` |
| Merged two AMENDMENTS annotations into one (saved slack words) | 8 | `[Numbered actions. Each traceable...] [Two lines required...Fill in all brackets -- do not omit either line.]` → `[Numbered actions, each traceable... Two additional lines required per action -- do not omit any.]` |

### Criteria verification (all 17)

All 5 essential (C-01–C-05): **PASS** — ARCHITECT table with traffic lights, VERDICT with composite score and label, INFERENCE GATE with team/timeline disclosure, `stack_source` in artifact frontmatter, RED Blockers section intact.

All 3 recommended (C-06–C-08): **PASS** — STRATEGY section intact, VERDICT conditionals intact.

All 9 aspirational (C-09–C-17): **PASS** — PM budget chain intact (C-09), AMENDMENTS section intact (C-10), INFERENCE GATE ordering maintained (C-11), PM before ARCHITECT ordering maintained (C-12), `PM:` and `ARCHITECT:` section prefixes intact (C-13), score-delta line in amendment template (C-14), five inertia surfaces all present (C-15/C-16/C-17): INERTIA section, Do-nothing cost column, RED Blocker sub-field, VERDICT "Not building this means:", AMENDMENTS "Inertia saved:".

```json
{"simplified_word_count": 402, "original_word_count": 521, "all_essential_still_pass": true, "reduction_pct": 22.8}
```
