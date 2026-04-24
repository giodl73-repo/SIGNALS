Written to `simulations/quest/variations/scout-feasibility-variations-R4-2026-03-14.md`.

---

## Round 4 Variations — Summary

**Context:** v4 rubric adds C-15 (inertia framing, aspirational, denominator 7). Under v4, R3's V-03 is the sole 100/100 — it had inertia by design. V-02/V-05 drop to 98.6; V-01/V-04 to 97.0. R4 goal: all 5 pass both C-12 and C-15. Foundation: V-05 R3 (PM-first, pre-printed template) inherited by all.

| V | Axis | C-15 mechanism |
|---|------|----------------|
| **V-01** | Inertia section placement | Pre-printed `## INERTIA: STATUS QUO` section + "Do-nothing cost:" sub-field in RED Blockers |
| **V-02** | Inertia column mandate | Pre-printed "Do-nothing cost" column in ARCHITECT table + blockers inherit it |
| **V-03** | Inertia scope (decision-surface only) | `Not building this means:` line in VERDICT + pre-printed `Inertia saved:` field per amendment |
| **V-04** | Axes 1+2: Section + column | Section establishes aggregate baseline; column anchors per-component; blockers carry field |
| **V-05** | Full synthesis (all axes) | Section + column + blockers field + VERDICT line + AMENDMENTS field — all surfaces pre-printed |

**Key design decision:** Three single-axis variations test *where* inertia structurally lives (section / column / decision-surface). V-04 and V-05 combine them. All five inherit C-12 (PM-first) and C-13/C-14 (pre-printed headers + C-14 fragment) from R3.

**Predicted ceiling:** V-05 — maximum surface coverage, no omission path for C-15. V-04 is the closest competitor (section + column, leaner). V-03 tests the minimum-overhead floor: decision-surface only.
 all downstream sections reference
  it by name.
- V-02 tests whether embedding the do-nothing cost as a pre-printed table column in the ARCHITECT
  section is sufficient without a standalone section -- inertia and complexity rating appear in
  the same row at the moment of judgment.
- V-03 tests whether concentrating inertia at the decision surface only (VERDICT + AMENDMENTS)
  keeps analysis clean while still satisfying C-15 -- the pass condition explicitly allows
  "blockers and/or amendment actions."

**C-12 guaranteed in all variations**: PM-first ordering inherited from R3 foundation.

**C-13 and C-14 guaranteed**: Pre-printed markdown headers and pre-printed score-delta fragment
inherited from R3 V-05.

**Predicted ceiling**: V-05 -- maximum surface coverage prevents any partial-omission failure;
also the richest analytical output. V-04 is the closest structural competitor.

---

## V-01: Inertia Section Placement

**Axis:** Inertia placement -- pre-printed `## INERTIA: STATUS QUO` section between INFERENCE
GATE and PM: BUDGET; RED Blockers carry a pre-printed "Do-nothing cost:" sub-field referencing
the section
**Hypothesis:** A standalone, named section makes the workaround baseline a first-class
analytical artifact that all downstream sections (PM, Architect, VERDICT, AMENDMENTS) can
reference by name. The pre-printed "Do-nothing cost:" field in the blockers section makes
C-15 structurally unavoidable for every RED component.

```
You are running /scout-feasibility. Fill in this structured template.
All section headers are fixed. PM leads. Every gate must fire before the next section begins.
Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: STACK SCAN
Files found: [List each of package.json / tsconfig.json / Cargo.toml as found / not found]
[If none found:]
Stack fallback: "No canonical stack files found. Inferring from [SOURCE]: [WHAT WAS INFERRED]."

## INFERENCE GATE
[Write as a contiguous block. All three required before INERTIA: STATUS QUO begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

## INERTIA: STATUS QUO
[Complete before PM: BUDGET. This baseline is referenced by name in RED Blockers below.]
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

| Component | Rating               | Est. Hours | Rationale           |
|-----------|----------------------|------------|---------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] |
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] |

RED Blockers:
[For every RED-rated component, write one entry. All sub-fields required -- do not omit any line.]
- [Component]: [Why it is a blocker.] Lift condition: [What must specifically change.]
  Do-nothing cost: [What the team continues doing without this component -- reference INERTIA: STATUS QUO. Estimate hrs/sprint or $. Do not omit this line.]
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
Inertia impact: "Not building this means [status-quo consequence from INERTIA: STATUS QUO], costing approximately [N hrs/sprint or $N/sprint] ongoing."

[Complete only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] from the build."

[Complete only if label is FEASIBLE WITH CAVEATS:]
Prerequisites (every RED-rated component must appear):
1. [Prerequisite addressing first RED component]
2. [Prerequisite addressing second RED component]

## AMENDMENTS
[Numbered actions. Each traceable to a RED or YELLOW component from Architect or PM.]
[The score-delta line is required for every action. Fill in the brackets -- do not omit the line.]

1. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

2. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

[Continue for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source, inertia_cost_per_sprint.
```

---

## V-02: Do-Nothing Column in Architect Table

**Axis:** Inertia column mandate -- no standalone section; inertia is a pre-printed "Do-nothing
cost" column in the ARCHITECT:COMPLEXITY table; RED blockers automatically reference it
**Hypothesis:** Embedding inertia as a pre-printed column in the ARCHITECT table makes the
comparative feasibility judgment visible at the exact moment each component is rated. The reader
sees traffic light, hours, rationale, and workaround cost in a single row. If the column is
pre-printed, the model cannot omit it. C-15 is satisfied without an additional section and without
requiring the model to locate and repeat data from a prior section. Tests whether per-component
column placement is a more direct C-15 surface than a standalone section.

```
You are running /scout-feasibility. Fill in this structured template.
All section headers are fixed. PM leads. Every gate must fire before the next section begins.
Do not reorder, rename, or remove any section header, column header, or template fragment.

---

## SETUP: STACK SCAN
Files found: [List each of package.json / tsconfig.json / Cargo.toml as found / not found]
[If none found:]
Stack fallback: "No canonical stack files found. Inferring from [SOURCE]: [WHAT WAS INFERRED]."

## INFERENCE GATE
[Write as a contiguous block. All three required before PM: BUDGET begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

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
[Do-nothing cost column: describe what the team does without this component if not built. Estimate hrs/sprint or $ if possible. Required for every row -- do not leave blank.]

| Component | Rating               | Est. Hours | Rationale           | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|---------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] | [Workaround and cost without this]|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] | [Workaround and cost without this]|

RED Blockers:
[For every RED-rated component, write one entry. The "Without this:" field must repeat the
Do-nothing cost from the table above -- do not omit.]
- [Component]: [Why it is a blocker.] Lift condition: [What must specifically change.]
  Without this: [Do-nothing cost from ARCHITECT table row above. Repeat the workaround and cost estimate. Do not omit this line.]
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

[Complete only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] from the build."

[Complete only if label is FEASIBLE WITH CAVEATS:]
Prerequisites (every RED-rated component must appear):
1. [Prerequisite addressing first RED component]
2. [Prerequisite addressing second RED component]

## AMENDMENTS
[Numbered actions. Each traceable to a RED or YELLOW component from Architect or PM.]
[The score-delta line is required for every action. Fill in the brackets -- do not omit the line.]

1. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

2. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

[Continue for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source.
```

---

## V-03: Inertia Concentrated at Decision Surface

**Axis:** Inertia scope -- no inertia during analysis sections; VERDICT carries a mandatory
"Not building this means..." summary line; each AMENDMENT entry carries a pre-printed
"Inertia saved:" field
**Hypothesis:** C-15's pass condition allows "RED blockers section and/or amendment actions" --
the amendment surface alone is sufficient. Concentrating inertia at the decision surface (where
the reader acts, not where they analyze) keeps the analysis sections lean. The pre-printed
"Inertia saved:" field per amendment is structurally unavoidable. Tests the minimal
structurally-guaranteed approach: least template overhead, full criterion coverage.

```
You are running /scout-feasibility. Fill in this structured template.
All section headers are fixed. PM leads. Every gate must fire before the next section begins.
Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: STACK SCAN
Files found: [List each of package.json / tsconfig.json / Cargo.toml as found / not found]
[If none found:]
Stack fallback: "No canonical stack files found. Inferring from [SOURCE]: [WHAT WAS INFERRED]."

## INFERENCE GATE
[Write as a contiguous block. All three required before PM: BUDGET begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

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

| Component | Rating               | Est. Hours | Rationale           |
|-----------|----------------------|------------|---------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] |
| [Name]    | GREEN / YELLOW / RED | [N]        | [Reason for rating] |

RED Blockers:
[For every RED-rated component, write one entry.]
- [Component]: [Why it is a blocker.] Lift condition: [What must specifically change.]
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
Not building this means: "[Describe what the team continues doing as a workaround and the approximate cost: N hrs/sprint or $N/sprint ongoing. Do not omit this line.]"

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
   Inertia saved: [Manual workaround or third-party cost this action eliminates. Estimate hrs/sprint or $. Do not omit this line.]

2. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [Manual workaround or third-party cost this action eliminates. Estimate hrs/sprint or $. Do not omit this line.]

[Continue for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source.
```

---

## V-04: Inertia Section + Column (Axes 1+2)

**Axes:** Inertia placement (section) + inertia column mandate (Architect table)
**Hypothesis:** The section (V-01 axis) establishes a named, quantified workaround baseline
as a first-class artifact. The ARCHITECT column (V-02 axis) forces per-component anchoring
at the moment of rating. Together they create two mutually-reinforcing surfaces: the section
gives the reader the aggregate status-quo picture; the column gives per-component granularity.
RED Blockers inherit both -- the column value appears in the blocker entry. This is the
strongest dual-surface approach before the full synthesis.

```
You are running /scout-feasibility. Fill in this structured template.
All section headers are fixed. PM leads. Every gate must fire before the next section begins.
Do not reorder, rename, or remove any section header, column header, or template fragment.

---

## SETUP: STACK SCAN
Files found: [List each of package.json / tsconfig.json / Cargo.toml as found / not found]
[If none found:]
Stack fallback: "No canonical stack files found. Inferring from [SOURCE]: [WHAT WAS INFERRED]."

## INFERENCE GATE
[Write as a contiguous block. All three required before INERTIA: STATUS QUO begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

## INERTIA: STATUS QUO
[Complete before PM: BUDGET. Establishes the workaround baseline referenced in ARCHITECT: COMPLEXITY below.]
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
Inertia impact: "Not building this means [status-quo consequence from INERTIA: STATUS QUO], costing approximately [N hrs/sprint or $N/sprint] ongoing."

[Complete only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] from the build."

[Complete only if label is FEASIBLE WITH CAVEATS:]
Prerequisites (every RED-rated component must appear):
1. [Prerequisite addressing first RED component]
2. [Prerequisite addressing second RED component]

## AMENDMENTS
[Numbered actions. Each traceable to a RED or YELLOW component from Architect or PM.]
[The score-delta line is required for every action. Fill in the brackets -- do not omit the line.]

1. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

2. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

[Continue for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source, inertia_cost_per_sprint.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Inertia section (V-01) + column mandate (V-02) + decision-surface concentration (V-03)
**Hypothesis:** Maximum structural coverage of C-15 across every relevant surface: standalone
section establishes the workaround baseline, ARCHITECT column anchors each component against it,
RED Blockers carry a mandatory "Do-nothing cost:" field, VERDICT carries a mandatory inertia
impact line, and each AMENDMENT carries a pre-printed "Inertia saved:" field. No surface where
inertia should appear is left to model discretion. This is the direct synthesis target for R4.

```
You are running /scout-feasibility. Fill in this structured template.
All section headers are fixed. PM leads. Every gate must fire before the next section begins.
Do not reorder, rename, or remove any section header, column header, or template fragment.

---

## SETUP: STACK SCAN
Files found: [List each of package.json / tsconfig.json / Cargo.toml as found / not found]
[If none found:]
Stack fallback: "No canonical stack files found. Inferring from [SOURCE]: [WHAT WAS INFERRED]."

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

## Round 4 Design Notes

### What changed from Round 3

R3 closed C-01 through C-14 gaps. v4 rubric adds C-15 (inertia framing, aspirational,
denominator now 7). All five R4 variations inherit the V-05 R3 template foundation -- the
only variation is how C-15 is embedded. All five maintain PM-first ordering (C-12) and
pre-printed headers (C-13/C-14).

### R3 scores under v4 rubric (calibration)

| Variation | Aspirational under v4 | v4 Score |
|-----------|----------------------|----------|
| V-03 (Inertia framing) | 7/7 (has C-15 by design) | 100 |
| V-02 (Template) | 6/7 (C-15 absent) | ~98.6 |
| V-05 (Golden synthesis) | 6/7 (C-15 absent) | ~98.6 |
| V-01 (Strategy-first) | 5/7 (C-12 + C-15 absent) | ~97.0 |
| V-04 (Architect-first) | 5/7 (C-12 + C-15 absent) | ~97.0 |

### C-15 mechanism comparison

| V | C-15 surface | Structural strength | Sections added |
|---|--------------|---------------------|---------------|
| V-01 | Section + blockers field | Strong (pre-printed field) | INERTIA section |
| V-02 | Architect column + blockers inherit | Moderate-strong (column pre-printed) | Column only |
| V-03 | VERDICT line + AMENDMENTS field | Moderate-strong (pre-printed at decision surface) | Two pre-printed fields |
| V-04 | Section + column + blockers field | Strong (two pre-printed surfaces) | INERTIA section + column |
| V-05 | Section + column + blockers + VERDICT + AMENDMENTS | Strongest (all surfaces pre-printed) | INERTIA + column + two fields |

### C-15 pass condition analysis

C-15 passes when: "RED blockers and/or amendment actions include a quantified do-nothing
alternative."

| V | Why C-15 passes |
|---|-----------------|
| V-01 | RED Blockers carry pre-printed "Do-nothing cost:" sub-field (blockers surface) |
| V-02 | RED Blockers carry pre-printed "Without this:" sub-field sourced from ARCHITECT column (blockers surface) |
| V-03 | AMENDMENTS carry pre-printed "Inertia saved:" field per action with workaround estimate (amendments surface) |
| V-04 | Blockers field AND VERDICT inertia impact line (blockers + verdict surfaces) |
| V-05 | All five surfaces: section + column + blockers field + VERDICT line + AMENDMENTS field |

### Predicted differentiation

All five variations should score 100/100 under v4 rubric. The within-100 differentiation is:

| Dimension | Strongest | Why |
|-----------|----------|-----|
| C-15 structural guarantee | V-05 | All surfaces pre-printed; no omission path |
| Analytical depth (live run) | V-04/V-05 | Section + column together produce richer quantification |
| Template overhead | V-03 | Minimal additions; decision-surface only |
| C-15 proximity to traffic-light | V-02/V-04/V-05 | Column puts do-nothing cost in the same row as the rating |

### Open research question for R4

Does the INERTIA: STATUS QUO section (V-01/V-04/V-05) improve the quality of inertia
quantification relative to embedded column or amendments-only approaches? The section forces
the model to reason about the workaround holistically before any component is rated; the column
forces local per-component reasoning. These may produce different quantification accuracy on
live model runs.

### V-golden candidate

**V-05** is the direct synthesis target:
- All C-01 through C-14 structural guarantees from R3 V-05
- C-15 covered on all five relevant surfaces
- "Do not omit" reinforcement on every pre-printed inertia field
- Maximum analytical depth from combined section + column

**V-04** is the closest structural competitor (section + column, without decision-surface
repetition). Key open question: does V-05's VERDICT + AMENDMENTS inertia repetition improve
output quality enough to justify the additional template overhead, or does V-04's leaner
surface produce equivalent C-15 depth?
