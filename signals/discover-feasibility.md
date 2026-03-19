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

Write artifact: simulations/discover/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source, inertia_cost_per_sprint.