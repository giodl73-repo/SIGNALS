Written to `simulations/quest/variations/discover-feasibility-alt-variations-R3-2026-03-18.md`.

---

## Round 3 Summary

**Two new criteria targeted:** C-14 (template body is sole structural source) and C-15 (cascade-safe guarantee chain). New aspirational denominator: `/7`.

### Variation axes

| | Axis | C-14 | C-15 | Composite |
|---|---|---|---|---|
| **V-01** | V-01-R2 baseline (no preamble, correct body) | PASS | PASS | **100.000** |
| **V-02** | Body inverted (ARCHITECT before STRATEGY), no preamble | **FAIL** | PASS | **94.286** |
| **V-03** | Body inverted + conflicting preamble (V-05-R2 under v3) | **FAIL** | **FAIL** | **92.143** |
| **V-04** | Correct body, C-11 gate + C-12 back-reference removed | PASS | PASS | **95.714** |
| **V-05** | V-04-R2: consistent preamble + correct body | PASS | PASS | **100.000** |

### Key design decisions

**C-14 vs C-15 are independent**. C-14 is an ordering detector (fails if body has ARCHITECT before STRATEGY). C-15 is a conflict-cascade detector (fails only when a preamble-template ordering conflict makes C-11/C-12 runtime-dependent). V-02 isolates this: body inverted, no preamble -- C-14 FAIL but C-15 PASS.

**V-04 is the critical C-15 probe**: correct body order, but C-11 and C-12 mechanisms removed. C-10/C-14/C-15 all PASS. This confirms C-15 does not fire when C-11/C-12 fail for independent mechanism reasons -- only when a conflict cascades into them.

**V-03 floor under v3**: 92.143 (vs V-05-R2's 93.000). The 0.857-pt drop is the /7 denominator absorbing two new FAIL criteria (C-14, C-15) across the same failure set.
| **100.000** | YES |
| V-02 | C-09=1, C-10=0, C-11=0, C-12=0, C-13=N/A=1, C-14=0, C-15=1 | 3/7 | **94.286** | YES |
| V-03 | C-09=1, C-10=0.5, C-11=0, C-12=0, C-13=0, C-14=0, C-15=0 | 1.5/7 | **92.143** | YES |
| V-04 | C-09=1, C-10=1, C-11=0, C-12=0, C-13=N/A=1, C-14=1, C-15=1 | 4/7 | **95.714** | YES |
| V-05 | C-09=1, C-10=1, C-11=1, C-12=1, C-13=1, C-14=1, C-15=1 | 7/7 | **100.000** | YES |

### Key discriminators

- **V-02 vs V-01**: Isolates C-14 failure from C-15. When body inverts ARCHITECT before STRATEGY and no preamble directive exists, C-14 FAILS (body is not the sole structural source -- it actively enforces wrong ordering). C-10/C-11/C-12 collapse as structural consequences. C-15 PASSES because no preamble-template conflict exists (no preamble to conflict with). Score drop: 5.714 pts.
- **V-03 vs V-02**: Adds C-15 FAIL on top of V-02's failure set. The single preamble directive (conflicting with inverted body) triggers C-13 FAIL and C-10 PARTIAL. C-15 additionally FAILS because preamble-template conflict makes C-11/C-12 runtime-dependent rather than structurally failed. Additional score drop: 2.143 pts.
- **V-04 vs V-01**: Isolates C-11 and C-12 as independently removable while C-14 and C-15 hold. Correct body order keeps C-10/C-14/C-15 intact. No conflict keeps C-13 N/A. Score drop: 4.286 pts from C-11 + C-12 removal.
- **V-05 vs V-01**: Zero-cost C-13 upgrade confirmed under v3 denominator. Adding consistent preamble directive converts C-13 from N/A to active PASS with no composite regression (100.000 unchanged). C-14 still PASS because body independently enforces ordering -- preamble is documentational.
- **V-04 vs V-02**: Critical discriminator for C-15. Both have C-11 and C-12 failing. V-04: C-15 PASS (no conflict; failures are independent mechanism removals). V-02: C-15 PASS (no conflict; failures are structural body-order consequences). Neither triggers the cascade condition. Confirms C-15 is a conflict detector, not an ordering detector.

---

## V-01 -- Baseline Confirm (V-01-R2 exact)

**Axis**: Baseline reconfirmation -- V-01-R2 under rubric v3 (two new aspirational criteria C-14/C-15, denominator /7)
**Hypothesis**: V-01-R2 carries: (a) no preamble ordering directive -- C-13 N/A, C-14 PASS (body is sole structural source by absence of any alternative); (b) body places STRATEGY before ARCHITECT -- C-10 PASS, C-14 PASS (body independently enforces ordering); (c) STRATEGY has forward-declaration + proceed gate -- C-11 PASS; (d) ARCHITECT has confirmation + semantic back-reference -- C-12 PASS; (e) no preamble-template conflict -- C-15 PASS (cascade-safe). Expected: 7/7 aspirational, composite 100.000, all essential PASS. Denominator change /5 -> /7 does not change the score because all 7 criteria pass.

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

## V-02 -- C-14 Isolated Failure (body inverted, no preamble directive)

**Axis**: Template body places ARCHITECT before STRATEGY. No preamble directive present. Isolates C-14 failure without triggering C-15.
**Hypothesis**: C-14 FAILS: body places ARCHITECT before STRATEGY, so the template body is not the sole structural source of correct ordering -- it actively enforces wrong ordering. C-10 FAILS: ARCHITECT physically precedes STRATEGY (no by-construction guarantee). C-11 FAILS: STRATEGY is written after ARCHITECT in template-body order; forward-declaration commits are structurally impossible at STRATEGY execution time (ARCHITECT is already written). C-12 FAILS: ARCHITECT heading is written before STRATEGY exists; no back-reference is possible. C-13 N/A: no preamble directive present; no conflict to evaluate. C-15 PASSES: the cascade-safety criterion specifically requires "a preamble-template ordering conflict" to trigger failure. Without a preamble directive, no conflict exists; C-15's failure condition is absent. The failures of C-10/C-11/C-12 are structural (wrong body order) rather than conflict-cascade (preamble instructs X, body does Y). Predicted composite: 60 + 30 + (3/7 x 10) = 94.286.

**Section order in body**: INFERENCE GATE -> Step 0 -> INERTIA -> PM: BUDGET -> ARCHITECT -> STRATEGY -> VERDICT -> AMENDMENTS

**Changed ARCHITECT heading** (back-reference removed -- STRATEGY has not been written yet):
```
**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.
```

**Changed STRATEGY section** (forward-declaration removed, backward-reference inserted, proceed gate removed):
```
**STRATEGY: BUILD-VS-BUY**
Cover at least half the components from ARCHITECT above. Procurement decisions (build / buy / use existing) for each component -- include focus economics impact and named incumbent comparison if it changes the recommendation.
```

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
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. base_cost-only run] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the Item A table above.
  Check: scan the Effect column now. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here after revising.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation in Item C.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan now. Return here after adjusting.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics computed in Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace.]
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]" as the column header label
    (3) AMENDMENTS inertia-saved framing: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required in the output; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent] |

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

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [focus_adjusted_total if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
Cover at least half the components from ARCHITECT above. Procurement decisions (build / buy / use existing) for each component -- include focus economics impact and named incumbent comparison if it changes the recommendation.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines -- do not drop any.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

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
  For a focus shift: re-run Step 0 (all four items) with the new focus. Declare explicitly:
    "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten."
  For a threshold adjustment: Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for changed components only.

(3) Re-weave only the affected sections. Mark headers with "[AMENDED: reason]". Do not touch unaffected sections.
  For a focus shift: update Step 0 Items A-D in order: (a) Item A, (b) FORMULA CONTRACT RE-CHECK, (c) Item B, (d) Item C, (e) Item D.

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

## V-03 -- C-14 + C-15 Compound Failure (body inverted + conflicting preamble)

**Axis**: V-05-R2 exact re-run under v3 scoring. Body places ARCHITECT before STRATEGY; preamble instructs the opposite. Canonical compound failure: C-13 + C-14 + C-15 all fail simultaneously.
**Hypothesis**: C-13 FAILS: preamble says "Write STRATEGY before ARCHITECT" but body places ARCHITECT before STRATEGY -- direct contradiction. C-10 PARTIAL: execution order is uncertain; a model following template-body writes ARCHITECT first; a model following preamble writes STRATEGY first; neither is by-construction. C-11 FAILS: at STRATEGY's template-body execution time, ARCHITECT is already written -- no forward-declaration is possible. C-12 FAILS: at ARCHITECT's template-body execution time, STRATEGY has not been written -- no back-reference is possible. C-14 FAILS: body places ARCHITECT before STRATEGY; preamble directive cannot substitute for structural ordering; body is not the sole structural source of correct ordering. C-15 FAILS: a preamble-template ordering conflict explicitly exists; it degrades C-10 from by-construction to probabilistic, cascading to C-11/C-12 as runtime-dependent. Under v3 denominator: C-09=1, C-10=0.5, C-11=0, C-12=0, C-13=0, C-14=0, C-15=0 -> 1.5/7. Composite = 60 + 30 + (1.5/7 x 10) = 92.143. This is 0.857 lower than V-05-R2's 93.000 (same failures, but two new failing criteria further dilute the aspirational fraction under the wider /7 denominator).

**Preamble directive** (conflicts with body): "Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY. Required output section sequence: INERTIA -> PM: BUDGET -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. Procurement decisions must be committed before complexity ratings are assigned."

**Body section order**: INFERENCE GATE -> Step 0 -> INERTIA -> PM: BUDGET -> ARCHITECT -> STRATEGY -> VERDICT -> AMENDMENTS.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY. Required output section sequence: INERTIA -> PM: BUDGET -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. Procurement decisions must be committed before complexity ratings are assigned.

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent. The focus lens changes the competitive math -- it is not a section you add at the end. All focus content belongs inside the existing sections, integrated against the named incumbent.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If you find yourself writing one, stop: move that content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Propagation Contract (write this before lens definition and before economics):**

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions.
Do not write Item B until both are satisfied.

CONDITION (i): `focus_adjusted_total` appears in at least one Stated Effect cell. Scan Effect column now.
  Satisfied: proceed to CONDITION (ii).
  Not satisfied: STOP. Revise AMENDMENTS row to include "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced."

CONDITION (ii): `focus_adjusted_total` will be the LHS label in Item C equation.
  Satisfied: write Item B.
  Not satisfied: STOP. Adjust Item C plan now.

**Item B -- Lens definition:** [1-2 sentences]

**Item C -- Focus Economics:**
  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

**Item D -- Failure-mode rejection:** No focus-named section heading after AMENDMENTS.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table column header: "[Named incumbent]"
    (3) AMENDMENTS framing: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors required; all three recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
(Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [cost per sprint]."

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

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [focus_adjusted_total if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**STRATEGY: BUILD-VS-BUY**
Cover at least half the components from ARCHITECT above. Procurement decisions (build / buy / use existing) for each component -- include focus economics impact and named incumbent comparison if it changes the recommendation.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total and long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS:]
Prerequisites:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines.

1. [Action for COMPONENT (RED/YELLOW).]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: [base_cost recaptured: N hrs/sprint. focus_adjustment eliminated: N hrs/sprint. Total: [stated total] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received.

(1) Parse: Change type / From / To.
(2) Declare affected and unaffected sections. Unaffected will not be rewritten.
(3) Re-weave affected sections only. For focus shift: update Step 0 A->RE-CHECK->B->C->D first. Mark headers "[AMENDED: reason]".
(4) Update VERDICT: New score / Delta / Label.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- C-15 Cascade Independence (correct body, C-11 + C-12 mechanisms removed)

**Axis**: Template body retains correct STRATEGY-before-ARCHITECT ordering. No preamble directive. STRATEGY loses the proceed-gate sentence (C-11 FAILS). ARCHITECT heading loses the confirmation + back-reference (C-12 FAILS). Tests whether C-15 PASSES when C-11/C-12 fail for independent mechanism reasons rather than conflict-cascade.
**Hypothesis**: C-10 PASS: body has STRATEGY before ARCHITECT by construction. C-11 FAIL: proceed gate absent (same failure mode as V-02-R2). C-12 FAIL: ARCHITECT back-reference absent (same failure mode as V-03-R2). C-13 N/A: no preamble directive. C-14 PASS: body is the sole structural source and it enforces correct ordering. C-15 PASS: this is the diagnostic result. C-15's failure condition is "preamble-template ordering conflict makes C-11 and C-12 runtime-dependent." No conflict exists here: STRATEGY precedes ARCHITECT in the body (C-10 holds), so C-11 and C-12 are by-construction *reachable* -- they happen to fail because their mechanisms (proceed gate, back-reference text) were removed, not because their execution order is uncertain. C-15 reads as PASS: the guarantee chain is cascade-safe. Predicted composite: 60 + 30 + (4/7 x 10) = 95.714.

**Changed sections from V-01 (STRATEGY and ARCHITECT heading only):**

STRATEGY -- proceed gate removed, forward-declaration retained:
```
**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.
If focus changes procurement logic, state it in Rationale.

List all components you intend to assess in ARCHITECT below.

| Component | Build / Buy / Use existing | Why |
```

ARCHITECT heading -- confirmation + back-reference removed:
```
**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.
```

All other sections identical to V-01.

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

List all components you intend to assess in ARCHITECT below.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
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
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows (Item A table) identify which sections are affected. Note whether focus_adjusted_total changes against the named incumbent.
  For a threshold adjustment: identify which components change color. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component only.
  Then declare explicitly:
    "Affected sections: [list each affected section by exact heading name].
     Unaffected sections: [list each unaffected section by exact heading name, e.g., INFERENCE GATE, PM: BUDGET, STRATEGY].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in the following order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears in at least one Stated Effect cell. If not: revise AMENDMENTS row first.
        (ii) `focus_adjusted_total` will be LHS label in Item C. If not: revise Item C plan first.
        Both conditions must hold before writing Item B.
    (c) Write updated Item B.
    (d) Write updated Item C (beginning with `focus_adjusted_total = ...`).
    (e) Write updated Item D.
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

## V-05 -- Documentational Preamble (V-04-R2 exact)

**Axis**: V-01 template body (all mechanisms intact, STRATEGY before ARCHITECT) + consistent preamble ordering directive matching body order. Tests: (a) C-13 active PASS at zero composite cost under v3; (b) C-14 PASS with preamble present -- body independently enforces ordering, so preamble is documentational not instrumental; (c) C-15 PASS -- no conflict.
**Hypothesis**: All seven aspirational criteria pass. C-13 active PASS (preamble directive matches body order -- no conflict). C-14 PASS: body has STRATEGY before ARCHITECT independently of the preamble directive -- if the preamble were removed, C-10 would still hold. The preamble documents the existing structural guarantee; it does not create a new model-compliance dependency. C-15 PASS: no preamble-template conflict; cascade-safety condition is not triggered. Composite unchanged at 100.000 under v3. Confirms R2-V-04's zero-cost C-13 upgrade result holds under the wider /7 denominator and the two new v3 criteria.

**Added preamble directive**: "Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY. Required output section sequence: INERTIA -> PM: BUDGET -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. Procurement decisions must be committed before complexity ratings are assigned."

All other content identical to V-01.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Write STRATEGY: BUILD-VS-BUY before ARCHITECT: COMPLEXITY. Required output section sequence: INERTIA -> PM: BUDGET -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. Procurement decisions must be committed before complexity ratings are assigned.

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

## Design Notes

### C-14 vs C-15: what each criterion sees

| Configuration | C-14 | C-15 | Reason |
|---------------|------|------|--------|
| Body: STRATEGY before ARCHITECT, no preamble | PASS | PASS | Body is sole structural source; no conflict possible |
| Body: STRATEGY before ARCHITECT, consistent preamble | PASS | PASS | Body enforces independently; preamble is documentational; no conflict |
| Body: ARCHITECT before STRATEGY, no preamble | FAIL | PASS | Body fails to enforce correct ordering; but no preamble-template conflict exists -- C-15 failure condition absent |
| Body: ARCHITECT before STRATEGY, conflicting preamble | FAIL | FAIL | Body fails C-14; conflict exists, makes C-11/C-12 runtime-dependent, fails C-15 |
| Body: STRATEGY before ARCHITECT, C-11/C-12 mechanisms absent, no preamble | PASS | PASS | Body enforces ordering (C-14); failures are independent mechanism removals, not cascade (C-15) |

**C-14 is an ordering detector. C-15 is a conflict-cascade detector. They are independent.**

### Scoring under v3 denominator (/7)

| Variation | Aspirational fraction | Contribution | Composite |
|-----------|----------------------|--------------|-----------|
| V-01 (all pass) | 7/7 | 10.000 | 100.000 |
| V-05 (all pass, consistent preamble) | 7/7 | 10.000 | 100.000 |
| V-04 (C-11 + C-12 absent, rest pass) | 4/7 | 5.714 | 95.714 |
| V-02 (C-10/C-11/C-12/C-14 fail, no conflict) | 3/7 | 4.286 | 94.286 |
| V-03 (C-10 PARTIAL + C-11/C-12/C-13/C-14/C-15 fail) | 1.5/7 | 2.143 | 92.143 |

**New insight from R3**: The 2.143-point gap between V-02 and V-03 is entirely attributable to C-15: V-02 has no preamble directive so C-15 PASS (cascade condition absent), while V-03's preamble-template conflict triggers C-15 FAIL. This cleanly separates "body ordering failure" (C-14) from "conflict-cascade failure" (C-15) as independent composite costs. V-03 is the floor for the v3 series at 92.143 -- 0.857 below V-05-R2's 93.000, reflecting the wider /7 denominator absorbing the same failure set across more criteria.
