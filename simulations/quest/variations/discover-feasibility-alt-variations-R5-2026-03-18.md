Written to `simulations/quest/variations/discover-feasibility-alt-variations-R5-2026-03-18.md`.

---

## Round 5 Variations -- discover-feasibility-alt

**Target axis**: Focus path (C-05, C-07, C-09) — all three have been N/A=1 in every prior round.

**Design summary**:

| | Axis | C-05 | C-07 | C-09 | Composite |
|---|---|---|---|---|---|
| **V-01** | Focus-active baseline (V-01-R4 body unchanged) | PASS | PASS | PASS | **100.000** |
| **V-02** | Focus appended as standalone section (anti-pattern) | FAIL | FAIL | FAIL | **76.750** |
| **V-03** | Focus woven to INERTIA only (1-section propagation) | PASS | PASS | FAIL | **98.750** |
| **V-04** | Focus woven to 4 sections but qualitative/cosmetic only | PASS | FAIL | PASS | **90.000** |
| **V-05** | Focus-active golden + consistent preamble (zero-cost C-13) | PASS | PASS | PASS | **100.000** |

**Key findings embedded**:

- **Focus activation is cost-neutral** — N/A→PASS on C-05, C-07, C-09 costs nothing. The golden template handles the focus path without composite change vs. no-focus R1-R4 runs.
- **V-02 is the first variation to break the golden threshold** (76.750 < 80). The appended anti-pattern compounds across all three blocks: -12 essential, -10 recommended, -1.25 aspirational.
- **C-07 requires arithmetic** — qualitative focus notes (V-04) fail because no rating or score changes; `focus_adjusted_total` formula is required to demonstrably change the base analysis.
- **C-09 is cheap in isolation** (1.25 pts) but lethal in compound with C-05+C-07 (23.25 pts total via V-02).
- **Zero-cost C-13 upgrade holds on the focus-active path** under /8, denominator-invariant.
e appended-block anti-pattern triggers compound failure across all three focus criteria: C-05 (essential), C-07 (recommended), C-09 (aspirational). Composite drops to 76.750 -- first variation to fall below the golden threshold of 80. C-05 alone costs 12 pts (1/5 of the essential block). Compound total: -23.25 pts.
- **V-03**: Single-section propagation (C-09 FAIL) costs 1.25 pts from the aspirational block (1/8 x 10). Cheapest focus failure mode. C-05 PASS (woven, not appended) and C-07 PASS (focus changes INERTIA analysis via focus_adjusted_total) both hold. Composite 98.750.
- **V-04**: Cosmetic focus (C-07 FAIL) costs 10 pts from the recommended block (1/3 x 30). Focus is present in all four sections (C-09 PASS) and woven not appended (C-05 PASS), but the template uses qualitative notes instead of focus_adjusted_total arithmetic -- no rating or score changes. Composite 90.000.
- **V-05**: Zero-cost C-13 upgrade holds on the focus-active path. A preamble ordering directive converts C-13 from N/A=1 to PASS=1 -- numerator unchanged at 8/8, composite unchanged at 100.000. Denominator-invariant property confirmed under /8 on the focus-active path.

### Key discriminators

- **V-01 vs V-02**: appended anti-pattern cost. C-05 FAIL (essential, -12 pts) + C-07 FAIL (recommended, -10 pts) + C-09 FAIL (aspirational, -1.25 pts) = -23.25 pts total. Breaks golden threshold.
- **V-01 vs V-03**: single-section vs 4-section propagation cost. C-09 FAIL = -1.25 pts. Cheapest failure; composite still above golden.
- **V-01 vs V-04**: cosmetic vs quantitative focus cost. C-07 FAIL = -10 pts. Qualitative-only focus fails the "demonstrably changes the base analysis" check; a formula is required.
- **V-02 vs V-04**: both have C-07 FAIL; V-02 additionally has C-05 FAIL (essential) and C-09 FAIL (aspirational). Anti-pattern is 13.25 pts more expensive than cosmetic focus alone (76.750 vs 90.000).
- **V-01 vs V-05**: zero-cost C-13 upgrade on focus-active path. N/A->PASS = no composite change. Confirms denominator-invariant property under /8.

---

## V-01 -- Focus-Active Baseline (V-01-R4 body; focus activated)

**Axis**: Focus path activated. V-01-R4 body carried forward unchanged. Tests whether the golden template with an active focus dimension produces the same composite as a no-focus run.
**Hypothesis**: All three focus criteria convert from N/A to active PASS at zero composite cost. C-05 PASS: focus woven into INERTIA, ARCHITECT, VERDICT, AMENDMENTS via the Propagation Contract -- no standalone section appended. C-07 PASS: focus_adjusted_total is computed in Item C and changes Do-nothing cost cells in ARCHITECT and the "Not building this means:" line in VERDICT -- demonstrably different from a no-focus run. C-09 PASS: focus-introduced constraint appears in all four downstream sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) -- exceeds the 2-section minimum. C-13 N/A: no preamble directive; contributes 1 unchanged. All other criteria: same as V-01-R4 (C-10=1, C-11=1, C-12=1, C-14=1, C-15=1, C-16=1). Expected: C-09=1, C-10=1, C-11=1, C-12=1, C-13=N/A=1, C-14=1, C-15=1, C-16=1 -> 8/8. Composite: 100.000. Identical to V-01-R4 -- focus activation is cost-neutral.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries a regulatory liability that raises what "not replacing it" costs per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section you add at the end. All focus content belongs inside the existing sections, integrated against the named incumbent.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing the economics.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. base_cost-only run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column now. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- specifically in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan now so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- named incumbent's workaround cost ignoring focus lens; source: inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap"; stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate"; requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics computed in Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading:
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              "INERTIA: STATUS QUO -- The manual CSV export + shared Google Sheet the Feature Must Beat"
    (2) INERTIA table first column header:
        Form: "[Named incumbent]" as the column header label (not "What the team does instead" or "Status quo")
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              column header reads "manual CSV export + shared Google Sheet"
    (3) AMENDMENTS inertia-saved framing:
        Form: "recaptured from [Named incumbent]: N hrs/sprint" (not "workaround eliminated" or "savings from replacing")
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              "recaptured from manual CSV export + shared Google Sheet: 8 hrs/sprint"
    Minimum count: At least two of these three anchors are required in the output; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.
If focus changes procurement logic (e.g., compliance focus favors certified third-party over in-house vs. named incumbent), state it in Rationale.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost against the incumbent makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total from Step 0 Item C where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured from named incumbent: N hrs/sprint or $N/sprint. focus_adjustment eliminated: N hrs/sprint or $N/sprint. Total inertia saved: base_cost + focus_adjustment = [stated total] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify which sections are affected. Note whether focus_adjusted_total changes (new base_cost or new focus_adjustment in Item C formula) against the named incumbent.
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in the following order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK -- required before writing the updated Item B:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
             updated Item A table.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
             in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold. Do not write updated Item B until both are confirmed.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula, beginning with `focus_adjusted_total = ...`).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus_adjusted_total if Step 0 Item C formula changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-02 -- Focus Appended as Standalone Section (C-05 FAIL, C-07 FAIL, C-09 FAIL)

**Axis**: The anti-pattern template. Step 0 is reduced to a focus-dimension note with no Propagation Contract. All main sections use base_cost only -- no focus_adjusted_total. A FOCUS ANALYSIS section is appended after AMENDMENTS as a standalone block. This is exactly the pattern the golden template prohibits via Item D.
**Hypothesis**: C-05 FAILS (essential): focus content is additive-only -- it appears exclusively in a standalone FOCUS ANALYSIS block after AMENDMENTS, not woven into any existing section. The main sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) have no focus references. C-07 FAILS (recommended): focus does not demonstrably change the base analysis -- no ratings or scores differ from a no-focus run; the standalone block is supplementary observation, not mechanically integrated. C-09 FAILS (aspirational): focus-introduced constraint does not appear in 2+ downstream sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) -- it appears only in the appended FOCUS ANALYSIS block, which is not one of the enumerated sections. C-13 N/A: no preamble ordering directive. All ordering and mechanism criteria unchanged (C-10=1, C-11=1, C-12=1, C-14=1, C-15=1, C-16=1). Expected: C-05=0, C-07=0, C-09=0, all others=1. Essential: 4/5 x 60 = 48. Recommended: 2/3 x 30 = 20. Aspirational: 7/8 x 10 = 8.75. Composite: 76.750. Below golden threshold (80).

**Changed sections from V-01: Step 0 Propagation Contract replaced with focus-note; main sections stripped of focus; FOCUS ANALYSIS appended after AMENDMENTS.**

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Note the focus dimension.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active: write "Focus: [dimension]" and proceed to INFERENCE GATE. All focus-specific analysis will be consolidated in the FOCUS ANALYSIS section after AMENDMENTS.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading:
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              "INERTIA: STATUS QUO -- The manual CSV export + shared Google Sheet the Feature Must Beat"
    (2) INERTIA table first column header:
        Form: "[Named incumbent]" as the column header label (not "What the team does instead" or "Status quo")
    (3) AMENDMENTS inertia-saved framing:
        Form: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required in the output; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section. (Rename this heading to match anchor (1) above.)

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [base_cost -- workaround cost per sprint, inferred from topic context] | [Risk tied to incumbent if it remains in place] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale vs. named incumbent] |

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row.

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [base_cost per sprint] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [base_cost per sprint.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at approximately base_cost per sprint. State the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured from named incumbent: N hrs/sprint or $N/sprint per sprint.]

Repeat for every RED and YELLOW component.

---

**FOCUS ANALYSIS -- Focus-specific considerations**
[If focus is active, consolidate all focus-specific analysis here. Address how the focus dimension (compliance, stakeholders, requirements, naming, size, or other) affects the overall build-vs-buy decision against the named incumbent. This section supplements the feasibility analysis above.]

Focus dimension: [stated in Step 0]
Key focus considerations for this topic:
- [How the focus dimension is relevant to this feature]
- [What focus-specific risks or benefits exist for the named incumbent]
- [How focus would change priorities if addressed in a future iteration]

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: update FOCUS ANALYSIS with the new dimension.
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-03 -- Focus Woven to INERTIA Only (C-09 FAIL -- Single-Section Propagation)

**Axis**: Propagation Contract reduced to one row (INERTIA only). Focus economics are computed and appear in INERTIA via focus_adjusted_total. ARCHITECT, VERDICT, and AMENDMENTS use base_cost only -- focus does not propagate beyond the first downstream section.
**Hypothesis**: C-05 PASSES: focus content appears in an existing section (INERTIA), not as a standalone appended block. C-07 PASSES: focus demonstrably changes INERTIA -- focus_adjusted_total is computed and replaces base_cost in the INERTIA table and Baseline sentence, making the incumbent cost analysis different from a no-focus run. C-09 FAILS: focus-introduced constraint appears in only one downstream section (INERTIA alone), below the 2-section minimum. ARCHITECT, VERDICT, and AMENDMENTS use base_cost only with no focus references. C-13 N/A: no preamble directive. All ordering and mechanism criteria unchanged. Expected: C-05=1, C-07=1, C-09=0, C-10=1, C-11=1, C-12=1, C-13=N/A=1, C-14=1, C-15=1, C-16=1 -> 7/8. Essential: 5/5 x 60 = 60. Recommended: 3/3 x 30 = 30. Aspirational: 7/8 x 10 = 8.75. Composite: 98.750.

**Changed sections from V-01: Step 0 Propagation Contract reduced to INERTIA only; ARCHITECT, VERDICT, AMENDMENTS stripped of focus references.**

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, it adjusts the cost of the named incumbent in the INERTIA section. A compliance focus may reveal a regulatory liability in the incumbent's gap; a stakeholders focus may surface sign-off overhead tied to the incumbent's approval model. Compute the focus-adjusted cost before writing INERTIA.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your INERTIA focus economics before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete the following two items:

**Item A -- INERTIA Propagation Contract (focus applies to INERTIA only):**
Name the primary constraint this focus introduces and how it surfaces in the INERTIA section.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item B appears in the named incumbent's cost-per-sprint or Baseline sentence] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in the Stated Effect cell above.
  Check: does the Effect column contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the Effect cell to include the phrase
    "`focus_adjusted_total` appears in the INERTIA Baseline sentence." Return here after revising.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item B -- specifically in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item B equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item B plan so the equation label is `focus_adjusted_total`. Return here.

Both conditions satisfied -- write Item B now.

**Item B -- Focus Economics (INERTIA only):**
Compute the focus-adjusted do-nothing cost for the INERTIA section.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- named incumbent's workaround cost ignoring focus lens]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance: "audit exposure: +$X/sprint"; stakeholders: "sign-off overhead: +N hrs/sprint";
    size: "scaling degradation: +N hrs/sprint"; requirements: "+N hrs/sprint per uncovered requirement"]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

The INERTIA section uses focus_adjusted_total. ARCHITECT, VERDICT, and AMENDMENTS use base_cost -- focus adjustment applies to the incumbent cost framing only, not to component complexity ratings.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading:
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header:
        Form: "[Named incumbent]" as the column header label
    (3) AMENDMENTS inertia-saved framing:
        Form: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required in the output; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item B. State how the focus lens changes the named incumbent's ongoing cost. Focus economics apply here and only here.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item B if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale vs. named incumbent] |

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use base_cost.

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [base_cost per sprint] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [base_cost per sprint.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at approximately base_cost per sprint. State the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured from named incumbent: N hrs/sprint or $N/sprint per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 Items A and B with the new focus. Note whether focus_adjusted_total changes (new base_cost or new focus_adjustment). Only INERTIA is affected by a focus shift in this template.
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- Focus Woven to 4 Sections but Cosmetic/Qualitative Only (C-07 FAIL)

**Axis**: Focus Context Contract covers all four downstream sections (C-09 PASS) but uses qualitative descriptions only -- no focus_adjusted_total formula, no arithmetic, no rating changes tied to focus. Focus is "present everywhere but changes nothing."
**Hypothesis**: C-05 PASSES: focus content appears in existing sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), not as an appended standalone block. C-09 PASSES: focus-introduced constraint appears in all four downstream sections -- more than the 2-section minimum. C-07 FAILS: focus content does not demonstrably change the base analysis -- no component rating changes from GREEN/YELLOW/RED based on focus, no score changes, no prerequisite added. The focus notes are qualitative observations ("the focus dimension is relevant here") that accompany the analysis without altering it. Without focus_adjusted_total arithmetic, the competitive math against the named incumbent is identical to a no-focus run. C-13 N/A: no preamble directive. All ordering and mechanism criteria unchanged. Expected: C-05=1, C-07=0, C-09=1, C-10=1, C-11=1, C-12=1, C-13=N/A=1, C-14=1, C-15=1, C-16=1 -> 8/8 aspirational, 2/3 recommended. Essential: 5/5 x 60 = 60. Recommended: 2/3 x 30 = 20. Aspirational: 8/8 x 10 = 10. Composite: 90.000.

**Changed sections from V-01: Step 0 Propagation Contract replaced with qualitative Focus Context Contract; focus_adjusted_total removed from all sections.**

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, note the relevant focus context in each applicable section. The focus dimension (compliance, stakeholders, requirements, naming, size, or other) adds qualitative perspective to the analysis. Integrate this context into the relevant existing sections -- do not add a standalone focus block after AMENDMENTS.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. Focus context belongs inside the existing sections.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Focus Context Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete the Focus Context Contract -- a table noting where and how the focus dimension is contextually relevant. This ensures focus context is woven into all four downstream sections.

**Focus Context Contract:**

| Focus dimension | Section where it surfaces | Contextual note for that section |
|-----------------|--------------------------|----------------------------------|
| [The active focus dimension, e.g., "compliance", "stakeholders", "size"] | INERTIA | [How the focus dimension is relevant to the named incumbent's ongoing risk -- qualitative observation only] |
| [same] | ARCHITECT | [Which components are most affected by the focus dimension -- note for context, ratings based on complexity only] |
| [same] | VERDICT | [How the focus dimension informs the overall recommendation -- qualitative observation only] |
| [same] | AMENDMENTS | [How focus context shapes the priority or framing of amendments -- qualitative observation only] |

All sections use base_cost. Focus notes are qualitative context, not arithmetic adjustments.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading:
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header:
        Form: "[Named incumbent]" as the column header label
    (3) AMENDMENTS inertia-saved framing:
        Form: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required in the output; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section. (Rename this heading to match anchor (1) above.)

[If focus active: include the INERTIA context note from your Focus Context Contract. State qualitatively how the focus dimension is relevant to the named incumbent's ongoing risk. Do not compute a focus-adjusted cost; use base_cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [base_cost -- workaround cost per sprint] | [Risk tied to incumbent -- include focus context note from Focus Context Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale vs. named incumbent] |

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use base_cost.

[If focus active: include the ARCHITECT context note from your Focus Context Contract. State qualitatively which components the focus dimension most affects. Ratings are based on complexity only; the focus note provides supplementary context but does not change the GREEN/YELLOW/RED assignment.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [base_cost per sprint] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [base_cost per sprint.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at approximately base_cost per sprint. State the long-term competitive consequence of the incumbent remaining.]"

[If focus active: include the VERDICT context note from your Focus Context Contract. State qualitatively how the focus dimension informs the recommendation. The composite score does not change based on focus context alone.]

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: include the AMENDMENTS context note from your Focus Context Contract. Note how focus context shapes amendment priority qualitatively.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured from named incumbent: N hrs/sprint or $N/sprint per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 Focus Context Contract with the new focus dimension. The new context notes identify which sections need updating. All four sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) may need context note updates.
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-05 -- Focus-Active Golden + Consistent Preamble (Zero-Cost C-13 Upgrade)

**Axis**: V-01 body with one addition: a preamble section ordering directive. All focus criteria PASS identically to V-01. C-13 upgrades from N/A to active PASS at zero composite cost.
**Hypothesis**: C-05 PASS, C-07 PASS, C-09 PASS: identical to V-01 -- focus path fully active and correct. C-13 PASS: preamble directive "Write STRATEGY before ARCHITECT." matches the template body's section sequence (STRATEGY body precedes ARCHITECT body). Upgrading from N/A=1 to PASS=1 does not change the numerator: both contribute 1 to 8/8. Zero-cost upgrade confirmed on the focus-active path. C-14 PASS: body independently enforces ordering; preamble is purely documentational (the body would hold even with no preamble). C-15 PASS: no conflict -- preamble and body agree on section order. C-16 PASS: both mechanism sentences present. All other criteria unchanged. Expected: C-09=1, C-10=1, C-11=1, C-12=1, C-13=PASS=1, C-14=1, C-15=1, C-16=1 -> 8/8. Composite: 100.000. Identical to V-01. Zero-cost C-13 upgrade holds under /8, denominator-invariant, on the focus-active path.

**Changed section from V-01 (single preamble line added after "AMEND behavior"):**

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries a regulatory liability that raises what "not replacing it" costs per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section you add at the end. All focus content belongs inside the existing sections, integrated against the named incumbent.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**Section ordering**: Write STRATEGY before ARCHITECT. STRATEGY: BUILD-VS-BUY must appear before ARCHITECT: COMPLEXITY in the output.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing the economics.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint, e.g., "HIPAA audit trail requirement", "executive sponsor unassigned", "P99 latency budget exceeded at 3x load"] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. base_cost-only run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column now. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- specifically in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan now so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation provably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- named incumbent's workaround cost ignoring focus lens; source: inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap"; stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate"; requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics computed in Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading:
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              "INERTIA: STATUS QUO -- The manual CSV export + shared Google Sheet the Feature Must Beat"
    (2) INERTIA table first column header:
        Form: "[Named incumbent]" as the column header label (not "What the team does instead" or "Status quo")
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              column header reads "manual CSV export + shared Google Sheet"
    (3) AMENDMENTS inertia-saved framing:
        Form: "recaptured from [Named incumbent]: N hrs/sprint" (not "workaround eliminated" or "savings from replacing")
        e.g., if Named incumbent = "manual CSV export + shared Google Sheet":
              "recaptured from manual CSV export + shared Google Sheet: 8 hrs/sprint"
    Minimum count: At least two of these three anchors are required in the output; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before you finish this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]
  Delta:      [AVAILABLE minus ESTIMATED]
  Flag:       [OVER-BUDGET / UNDER-BUDGET / ON-BUDGET]

---

**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.
If focus changes procurement logic (e.g., compliance focus favors certified third-party over in-house vs. named incumbent), state it in Rationale.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost against the incumbent makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total from Step 0 Item C where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured from named incumbent: N hrs/sprint or $N/sprint. focus_adjustment eliminated: N hrs/sprint or $N/sprint. Total inertia saved: base_cost + focus_adjustment = [stated total] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify which sections are affected. Note whether focus_adjusted_total changes (new base_cost or new focus_adjustment in Item C formula) against the named incumbent.
  For a threshold adjustment: identify which components change color under the new threshold. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in the following order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK -- required before writing the updated Item B:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
             updated Item A table.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
             in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold. Do not write updated Item B until both are confirmed.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula, beginning with `focus_adjusted_total = ...`).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section in turn.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected in step (2).

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus_adjusted_total if Step 0 Item C formula changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## Round 5 Projected Scorecard

**Rubric**: v4 | **Denominator**: /8 aspirational

### V-01 -- Focus-Active Baseline

| Block | Formula | Score |
|-------|---------|-------|
| Essential (C-01..C-05) | 5/5 x 60 | 60.000 |
| Recommended (C-06..C-08) | 3/3 x 30 | 30.000 |
| Aspirational (C-09..C-16) | 8/8 x 10 | 10.000 |
| **Composite** | | **100.000** |

C-09=PASS, C-10=PASS, C-11=PASS, C-12=PASS, C-13=N/A=1, C-14=PASS, C-15=PASS, C-16=PASS.
Golden: YES (all essential PASS, composite >= 80).

### V-02 -- Focus Appended (C-05 FAIL, C-07 FAIL, C-09 FAIL)

| Block | Formula | Score |
|-------|---------|-------|
| Essential (C-01..C-05) | 4/5 x 60 | 48.000 |
| Recommended (C-06..C-08) | 2/3 x 30 | 20.000 |
| Aspirational (C-09..C-16) | 7/8 x 10 | 8.750 |
| **Composite** | | **76.750** |

C-05=FAIL, C-07=FAIL, C-09=FAIL. Essential breakdown: C-01=1, C-02=1, C-03=1, C-04=1, C-05=0 -> 4/5. Recommended: C-06=1, C-07=0, C-08=1 -> 2/3. Aspirational: C-09=0, all others=1 -> 7/8.
Golden: NO (C-05 essential FAIL; composite 76.750 < 80 threshold).

### V-03 -- Single-Section Focus (C-09 FAIL)

| Block | Formula | Score |
|-------|---------|-------|
| Essential (C-01..C-05) | 5/5 x 60 | 60.000 |
| Recommended (C-06..C-08) | 3/3 x 30 | 30.000 |
| Aspirational (C-09..C-16) | 7/8 x 10 | 8.750 |
| **Composite** | | **98.750** |

C-09=FAIL only. Aspirational: C-09=0, all others=1 -> 7/8.
Golden: YES (all essential PASS, composite 98.750 >= 80).

### V-04 -- Cosmetic Focus (C-07 FAIL)

| Block | Formula | Score |
|-------|---------|-------|
| Essential (C-01..C-05) | 5/5 x 60 | 60.000 |
| Recommended (C-06..C-08) | 2/3 x 30 | 20.000 |
| Aspirational (C-09..C-16) | 8/8 x 10 | 10.000 |
| **Composite** | | **90.000** |

C-07=FAIL. Recommended: C-06=1, C-07=0, C-08=1 -> 2/3. C-09=PASS (focus in 4 sections > 2 minimum).
Golden: YES (all essential PASS, composite 90.000 >= 80).

### V-05 -- Focus-Active Golden + Consistent Preamble

| Block | Formula | Score |
|-------|---------|-------|
| Essential (C-01..C-05) | 5/5 x 60 | 60.000 |
| Recommended (C-06..C-08) | 3/3 x 30 | 30.000 |
| Aspirational (C-09..C-16) | 8/8 x 10 | 10.000 |
| **Composite** | | **100.000** |

C-13=PASS (preamble directive matches body sequence). N/A=1 -> PASS=1: numerator unchanged at 8/8.
Zero-cost C-13 upgrade holds on the focus-active path under /8.
Golden: YES.

### Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 60.000 | 30.000 | 10.000 | **100.000** | YES |
| V-02 | 48.000 | 20.000 | 8.750 | **76.750** | NO |
| V-03 | 60.000 | 30.000 | 8.750 | **98.750** | YES |
| V-04 | 60.000 | 20.000 | 10.000 | **90.000** | YES |
| V-05 | 60.000 | 30.000 | 10.000 | **100.000** | YES |

**Rank**: V-01 = V-05 (100.000) > V-03 (98.750) > V-04 (90.000) > V-02 (76.750)

### Excellence Signals (from V-01 / V-05)

1. **Focus activation is cost-neutral** -- C-05, C-07, and C-09 all convert from N/A=1 to PASS=1. No composite change. The golden template handles focus as a zero-cost activation path.

2. **The Propagation Contract is the structural guarantor of C-05 and C-09** -- its 4-row table wires focus into all downstream sections before any section is written. Without it (V-02), both criteria fail.

3. **focus_adjusted_total is the discriminator for C-07** -- qualitative context notes (V-04) fail the "demonstrably changes the base analysis" check. The arithmetic formula is required: subtracting base_cost from focus_adjusted_total must equal focus_adjustment, verifiable by inspection.

4. **The appended anti-pattern is the most expensive failure mode** -- V-02's compound failure (C-05 essential + C-07 recommended + C-09 aspirational) costs 23.25 pts and breaks the golden threshold. No other single design choice in R1-R5 produces this much composite damage.

5. **C-09 is cheap to violate in isolation, expensive in compound** -- single-section propagation (V-03) costs only 1.25 pts aspirationally. But the same propagation failure in V-02 compounds with C-05 and C-07 to cost 23.25 pts total. The Propagation Contract's value is not C-09 alone but keeping all three focus criteria structurally in PASS simultaneously.

6. **Zero-cost C-13 upgrade holds on the focus-active path** -- adding a consistent preamble directive when focus is active upgrades C-13 from N/A to PASS at zero composite cost. Denominator-invariant property confirmed under /8 for focus-active invocations.
