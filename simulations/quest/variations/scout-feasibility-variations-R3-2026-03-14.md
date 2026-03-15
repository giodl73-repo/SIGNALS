**scout-feasibility-variations-R3-2026-03-14.md** written.

---

## Round 3 Variations

| V | Axis | Core move | C-13 strategy | C-14 strategy |
|---|------|-----------|---------------|---------------|
| **V-01** | Role sequence | Strategy-first: build-vs-buy before complexity | Role in `--- STRATEGY: BUILD-VS-BUY ---` header | Instruction: "end with: [canonical format]" |
| **V-02** | Output format | Template completion: pre-printed skeleton, model fills blanks | Headers pre-printed; model cannot drop them | Fragment pre-printed in every AMENDMENTS row |
| **V-03** | Inertia framing | Status-quo workaround anchors all ratings (new axis) | Role in `--- PM: BUDGET ---` / `--- ARCHITECT: COMPLEXITY ---` headers | Instruction: "end with: [canonical format]" |
| **V-04** | Role sequence + lifecycle | Architect-first + Assessment Contract locks inferences | Role in header per phase | Fragment required per action, format shown inline |
| **V-05** | Template + PM-first + C-13/C-14 | Synthesis: pre-printed skeleton + PM leads + fragment in every row | Pre-printed `## PM: BUDGET` / `## ARCHITECT: COMPLEXITY` headers (unavoidable) | Pre-printed in every AMENDMENTS row + "do not omit" (unavoidable) |

### Key design decisions

**C-13 split**: V-01/V-03/V-04 use dashes-style headers (`--- ROLE: PHASE ---`). V-02/V-05 pre-print markdown headers (`## PM: BUDGET`) that the model cannot reformat. The pre-print approach is the stronger guarantee.

**C-14 split**: V-01/V-03/V-04 rely on instruction ("end with: canonical format"). V-02/V-05 pre-print the score-delta fragment in every AMENDMENTS row — the fragment is already on the page. This is the same structural advantage that separated R2-V-05 from the pack.

**New axis — Inertia framing (V-03)**: Not explored in R1/R2. The status-quo workaround section may improve RED blocker rationale depth (C-05) and amendment specificity (C-10), and adds a new frontmatter field (`inertia_cost_per_sprint`).

**Predicted ceiling**: V-05 (pre-printed headers + pre-printed fragment + PM-first ordering). V-02 is the closest competitor, testing whether template surface alone matches the qualitative depth that PM-first ordering contributes.
u are running /scout-feasibility. Role sequence: STRATEGY -> ARCHITECT -> PM -> VERDICT.

--- SETUP: STACK SCAN ---
Scan for: package.json, tsconfig.json, Cargo.toml.
If none found: state "No canonical stack files found. Inferring from [source]: [what was inferred]."
Required before the inference gate.

--- INFERENCE GATE ---
State as a contiguous block. Do not write any component name until all three appear here:
  Feature:   [one sentence describing what is being assessed]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]

--- STRATEGY: BUILD-VS-BUY ---
Before any complexity or budget analysis, assess each feature component for make-vs-buy options.
| Component | Build / Buy / Use existing | Rationale | Strategic risk |
At least 50% of components must carry a label. Remaining may show "TBD -- see Architect."
Flag any component where the build-vs-buy decision changes with team size or timeline.

--- ARCHITECT: COMPLEXITY ---
Rate each component using the Strategy table above as context.
Rule: a component flagged "Buy" with no available vendor is automatically RED.
Rule: a component flagged "Use existing" with known integration gaps is YELLOW.
| Component | Rating | Rationale | Est. Hours |
Blockers -- required for every RED component:
  [Component]: [Why it is a blocker.] Lift condition: [What specifically must change.]

--- PM: BUDGET ---
Available hours = [team] x [hrs/sprint] x [sprints] = [N] hrs
Carry component hours forward from the Architect table:
| Component | Estimated Hours |
| Total     | [N]             |
Budget chain (all four elements required, as a linked statement):
  Estimated: [N] | Available: [N] | Delta: [+-N] | OVER-BUDGET / UNDER-BUDGET / ON-BUDGET
PM note: if any GREEN or YELLOW component becomes RED due to budget overage, note it here.

--- VERDICT ---
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.
If score < 50: "Scoped to [constraint]: [N]/100. This scope removes [RED items] from the build."
If FEASIBLE WITH CAVEATS: numbered prerequisites list. Every RED-rated component must appear.

--- AMENDMENTS ---
Numbered actions converting RED and YELLOW findings to concrete next steps.
Each action must name the specific component and end with:
  "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts."

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source.
```

---

## V-02: Template-Completion Output Format

**Axis:** Output format -- complete output skeleton with fill-in-the-blank fields; model fills
blanks only; all headers including role-attributed headers are pre-printed
**Hypothesis:** Pre-printing every section header (including role-attributed headers) and the
score-delta fragment makes C-13 and C-14 structurally unavoidable. The model cannot drop what
is already in the template. This tests whether the template surface alone guarantees compliance
more reliably than instruction-based approaches.

```
You are running /scout-feasibility. Complete the output template below.
Every [FIELD] must be filled in. Do not remove, reorder, or rename any section header.

---

## SETUP: STACK SCAN
Files found: [package.json -- yes/no] [tsconfig.json -- yes/no] [Cargo.toml -- yes/no]
[If no canonical files found:]
Stack fallback: "No canonical stack files found. Inferring from [SOURCE]: [WHAT WAS INFERRED]."

## INFERENCE GATE
[All three required. Write as a contiguous block before PM: BUDGET begins.]
  Feature:   [One sentence describing the feature being assessed.]
  Team:      [N engineers -- inferred from: SOURCE]
  Timeline:  [N sprints / N weeks -- inferred from: SOURCE]

## PM: BUDGET
[This section runs before Architect complexity ratings appear.]
Available hours = [TEAM_SIZE] engineers x [HRS_PER_SPRINT] hrs/sprint x [SPRINT_COUNT] sprints = [TOTAL] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

Budget chain:
  Estimated:  [SUM hrs from table above]
  Available:  [TOTAL hrs from formula above]
  Delta:      [AVAILABLE minus ESTIMATED = N hrs]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

## ARCHITECT: COMPLEXITY
[Budget flag from PM: BUDGET is: FLAG. Apply this when assigning ratings.]
[Traffic-light ratings are invalid before PM: BUDGET above is complete.]

| Component | Rating              | Est. Hours | Rationale           |
|-----------|---------------------|------------|---------------------|
| [Name]    | GREEN / YELLOW / RED | [N]       | [Reason for rating] |
| [Name]    | GREEN / YELLOW / RED | [N]       | [Reason for rating] |

RED Blockers:
[For every RED-rated component above, write one entry:]
- [Component]: [Why it is a blocker.] Lift condition: [What must specifically change.]
[If no RED components: write "No RED components."]

## STRATEGY: BUILD-VS-BUY
| Component | Recommendation             | Rationale |
|-----------|----------------------------|-----------|
| [Name]    | Build / Buy / Use existing | [Why]     |
| [Name]    | Build / Buy / Use existing | [Why]     |
[At least 50% of components must carry a recommendation. Remainder may be "TBD".]

## VERDICT
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]

[Complete only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] from the build."

[Complete only if label is FEASIBLE WITH CAVEATS:]
Prerequisites (all RED-rated components must appear):
1. [Prerequisite addressing first RED component]
2. [Prerequisite addressing second RED component]

## AMENDMENTS
[Numbered actions. Each traceable to a RED or YELLOW component.]
[The score-delta line is required for every action. Fill in the brackets -- do not omit the line.]

1. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

2. [Action for COMPONENT (RED/YELLOW): state the concrete next step.]
   Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.

[Add more entries as needed for all RED and YELLOW components.]

---

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source.
```

---

## V-03: Inertia Framing

**Axis:** Inertia framing -- the status-quo workaround is established as the first analytical
act; all feasibility ratings are anchored against the cost of NOT building
**Hypothesis:** Making the inertia cost explicit before any component analysis grounds the
feasibility score in comparative value rather than absolute technical risk. Amendment actions
become more actionable when framed relative to the current workaround. This axis is new --
not explored in R1 or R2 -- and may improve C-05 rationale quality and C-10 specificity.

```
You are running /scout-feasibility. Establish the status quo before any component is rated.
Feasibility is always relative: relative to what the team does if this feature is not built.

--- SETUP: STACK SCAN ---
Scan for: package.json, tsconfig.json, Cargo.toml.
If none found: "No canonical stack files found. Inferring from [source]: [what was inferred]."

--- INFERENCE GATE ---
State as a contiguous block before any component or workaround appears:
  Feature:   [one sentence]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]

--- INERTIA: STATUS QUO ---
What does the team currently do without this feature? Describe the workaround.
Estimate the cost the status quo carries per sprint.
| Current workaround | Sprint cost (manual hrs or $) | Risk if left unchanged |
This baseline informs which RED components are critical blockers vs. acceptable deferrals.

--- PM: BUDGET ---
Available hours = [team] x [hrs/sprint] x [sprints] = [N] hrs
Enumerate component estimates:
| Component | Estimated Hours |
| Total     | [N]             |
Budget chain (all four elements required):
  Estimated: [N] | Available: [N] | Delta: [+-N] | OVER-BUDGET / UNDER-BUDGET / ON-BUDGET

--- ARCHITECT: COMPLEXITY ---
Rate each component. Budget flag from PM: [FLAG].
Traffic-light ratings are not valid before the PM budget chain is closed above.
| Component | Rating | Rationale | Est. Hours | Status-quo risk if deferred |
Blockers -- required for every RED component:
  [Component]: [Why blocked.] Lift condition: [What must change to lift the rating.]
  Status-quo impact if deferred: [How the current workaround gets worse.]

--- STRATEGY: BUILD-VS-BUY ---
| Component | Build / Buy / Use existing | Inertia note (does buying eliminate the workaround?) |
Required for at least 50% of components.

--- VERDICT ---
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.
Inertia summary: "Not building this means [status-quo consequence from Inertia section]."
If score < 50: "Scoped to [constraint]: [N]/100."
If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented.

--- AMENDMENTS ---
Numbered actions converting RED and YELLOW findings to concrete next steps.
Each action must name the specific component and end with:
  "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts."
Where relevant, note whether the action also reduces the status-quo workaround cost.

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source, inertia_cost_per_sprint.
```

---

## V-04: Architect-First + Assessment Contract

**Axes:** Role sequence (Architect-first) + lifecycle emphasis (inference gate as locked contract)
**Hypothesis:** Architect-first avoids PM budget bias on complexity ratings -- complexity is
assessed on technical merit, then PM applies budget pressure as a second pass. The "Assessment
Contract" framing of the inference gate raises the semantic stakes: team and timeline are locked
commitments, not incidental context. This may produce more robust C-11 compliance than
ordering instructions alone, while role-attributed headers flow naturally from the phase structure.

```
You are running /scout-feasibility.
The Architect leads. PM overlays budget after complexity is known.
The Assessment Contract locks inferences before analysis begins.

--- SETUP: STACK SCAN ---
Scan for: package.json, tsconfig.json, Cargo.toml.
If none found: "No canonical stack files found. Inferring from [source]: [what was inferred]."
Summarize detected signals before the contract.

--- ASSESSMENT CONTRACT ---
This contract locks the assessment scope. All sections below reference these values.
Values must not be revised after this block appears.
  Feature:   [one sentence]
  Team:      [N engineers -- source: ___]
  Timeline:  [N sprints/weeks -- source: ___]
[This block must appear as a unit before any component name appears.]

--- ARCHITECT: COMPLEXITY ---
Pure complexity and stack-fit assessment. PM budget constraint is not yet applied.
| Component | Rating | Rationale | Est. Hours |
Blockers -- required for every RED component:
  [Component]: [Why blocked.] Lift condition: [What specifically changes the rating.]

--- PM: BUDGET OVERLAY ---
The Architect's ratings are now in view. Apply the budget constraint.
Available hours = [team from Contract] x [hrs/sprint] x [sprints from Contract] = [N] hrs
Carry estimated hours from Architect table:
| Component | Estimated Hours |
| Total     | [N]             |
Budget chain (all four elements required):
  Estimated: [N] | Available: [N] | Delta: [+-N] | OVER-BUDGET / UNDER-BUDGET / ON-BUDGET
PM note: if any GREEN or YELLOW component becomes RED because the team cannot absorb it
given the budget flag, upgrade its rating and add a blocker entry.

--- STRATEGY: BUILD-VS-BUY ---
| Component | Build / Buy / Use existing | Rationale |
Required for at least 50% of components.

--- VERDICT ---
Score: [0-100]. Label: NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE.
If score < 50: "Scoped to [constraint]: [N]/100."
If FEASIBLE WITH CAVEATS: numbered prerequisites, all RED items represented.

--- AMENDMENTS ---
Numbered actions converting RED and YELLOW findings (from either Architect or PM) to next steps.
Each action must name the specific component and end with:
  "Completing this moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts."

Write artifact: simulations/scout/feasibility/{topic}-feasibility-{date}.md
Frontmatter: skill, topic, date, score, label, team_inferred, timeline_inferred,
hours_available, hours_estimated, stack_source.
```

---

## V-05: Golden Synthesis

**Axes:** Template-completion format + PM-first role sequence + C-13 and C-14 hardcoded in template
**Hypothesis:** Builds on R2-V-05's winning structure but makes C-13 and C-14 structurally
unavoidable through the template surface: role-attributed headers are pre-printed (the model
fills content, not headers), and the score-delta fragment is pre-printed in every AMENDMENTS
row with an explicit "do not omit" instruction. The model cannot omit what it did not generate.
This is the direct synthesis target for v3.

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

| Component | Rating              | Est. Hours | Rationale           |
|-----------|---------------------|------------|---------------------|
| [Name]    | GREEN / YELLOW / RED | [N hrs]   | [Reason for rating] |
| [Name]    | GREEN / YELLOW / RED | [N hrs]   | [Reason for rating] |

RED Blockers:
[For every RED-rated component, write one entry:]
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

[Complete only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope defers [RED ITEMS] to a later sprint."

[Complete only if label is FEASIBLE WITH CAVEATS:]
Prerequisites (every RED-rated component must appear):
1. [Prerequisite for first RED component]
2. [Prerequisite for next RED component]

## AMENDMENTS
[Numbered actions. Each traceable to a specific RED or YELLOW component from Architect or PM.]
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

## Round 3 Design Notes

### What changed from Round 2

R2 closed C-09/C-11/C-12 gaps across all 5 variations. v3 rubric adds C-13 and C-14.
Round 3 starts from a floor where all variations should pass all essential criteria and C-09/C-11/C-12.
The variation is now entirely in how C-13 and C-14 are enforced.

### New axis: Inertia framing (V-03)

Not explored in R1 or R2. May improve:
- C-05 (RED rationale quality -- "deferred" vs "blocked" now has comparative weight)
- C-10 (amendment specificity -- actions grounded in workaround cost, not abstract steps)
- C-07 (scoped alternative -- scope described in terms of inertia impact, not just feature scope)

### C-13 strategy comparison

| V | C-13 mechanism | Risk |
|---|----------------|------|
| V-01 | Role in `--- ROLE: PHASE ---` header format | Model may strip dashes, losing role label |
| V-02 | Role pre-printed in `## PM: BUDGET` skeleton | Model fills content; headers fixed |
| V-03 | Role in `--- ROLE: PHASE ---` header format | Same as V-01 |
| V-04 | Role in `--- ROLE: PHASE ---` header format | Same as V-01 |
| V-05 | Role pre-printed in `## PM: BUDGET` / `## ARCHITECT: COMPLEXITY` skeleton | Strongest: model cannot reformat what is already printed |

### C-14 strategy comparison

| V | C-14 mechanism | Risk |
|---|----------------|------|
| V-01 | Instruction: "end with: [canonical format]" | Model must generate the fragment from instruction |
| V-02 | Fragment pre-printed in every AMENDMENTS row | Strongest: fragment is already on the page |
| V-03 | Instruction: "end with: [canonical format]" | Same as V-01 |
| V-04 | Instruction: "end with: [canonical format]" | Same as V-01 |
| V-05 | Fragment pre-printed in every AMENDMENTS row + "do not omit" | Pre-printed + reinforced |

### Predicted differentiation

| Criterion | Most at risk | Why |
|-----------|-------------|-----|
| C-13 | V-01/V-03/V-04 | Dashes-style headers may be reformatted to prose under compression |
| C-14 | V-01/V-03/V-04 | Instruction-only surfaces require model to generate fragment; V-02/V-05 pre-print it |
| C-09 | V-03 | Inertia section adds content before PM: BUDGET; budget chain may be abbreviated under length pressure |
| C-07 | All | Scoped alternative requires NOT FEASIBLE -- may not trigger in test topic |

### V-golden candidate

V-05 is the direct synthesis target. V-02 is the closest structural competitor on C-13/C-14.
Key research question: does the template-only approach (V-02) match V-05's depth on C-06
rationale quality and C-05 blocker specificity, or does PM-first ordering in V-05 produce
richer qualitative output beyond what the template surface alone achieves?
