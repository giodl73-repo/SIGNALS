## Round 11 Variations -- discover-feasibility-alt

**Rubric**: v9 (/25 aspirational denominator)

---

### Design summary

| | Axis | Key failure | Composite | Golden? |
|---|---|---|---|---|
| **V-01** | Phrasing register -- formal/technical | none | **100.000** | Yes |
| **V-02** | Role sequence -- STRATEGY omitted | C-08 FAIL, C-10 N/A | **90.000** | Yes |
| **V-03** | Lifecycle emphasis -- BUDGET no Delta/Flag | C-02 PARTIAL | **94.000** | **No** |
| **V-04** | Output format -- AMENDMENTS C-06 isolated | C-06 FAIL | **90.000** | Yes |
| **V-05** | Role sequence + Lifecycle -- STRATEGY omitted + BUDGET no Delta/Flag | C-02 PARTIAL + C-08 FAIL | **84.000** | **No** |

### Score derivations (v9 /25)

- V-01: `5/5x60 + 3/3x30 + 25/25x10 = 100.000`
- V-02: `5/5x60 + 2/3x30 + 25/25x10 = 90.000` (C-08 FAIL; C-10 N/A counts as PASS)
- V-03: `4.5/5x60 + 3/3x30 + 25/25x10 = 94.000` (C-02 PARTIAL -- NOT GOLDEN)
- V-04: `5/5x60 + 2/3x30 + 25/25x10 = 90.000` (C-06 FAIL)
- V-05: `4.5/5x60 + 2/3x30 + 25/25x10 = 84.000` (C-02 PARTIAL + C-08 FAIL -- NOT GOLDEN)

### Key new patterns generated for v10

1. **C-32 bidirectionality**: V-01 formal register = 100.000, confirming the free-axis claim in both register directions.
2. **C-10 N/A on STRATEGY omission**: STRATEGY omission fires the N/A pass condition, not C-10 FAIL. Targeting C-10 FAIL requires ARCHITECT *before* a *present* STRATEGY, not STRATEGY removal.
3. **Equal recommended-tier cost**: V-02 (C-08 FAIL = 90.000) and V-04 (C-06 FAIL = 90.000) are parity-matched from different single recommended FAILs, confirming independent equal cost (10 pts each).
4. **C-02 PARTIAL = 94.000**: Essential PARTIAL formula is criterion-independent -- same 94.000 as R10 C-04 PARTIAL.
5. **PARTIAL gate dominates at 84.000**: V-05 (84.000) is not golden; R10 V-04 (80.000) is golden. Ranking inversion from C-28/C-29 confirmed for C-02 PARTIAL, not just C-04 PARTIAL.
present STRATEGY section.
3. **C-06 FAIL and C-08 FAIL are equal-cost and independently accountable**: V-02 (C-08 FAIL = 90.000) and V-04 (C-06 FAIL = 90.000) both score 90.000. Each recommended criterion costs 10 pts independently (10/30 pts at 3 recommended criteria). Combined with R10 V-04 (C-06+C-08 = 80.000 = 20 pts compound), confirms additivity: no amplification or discount for pairing these criteria.
4. **C-02 PARTIAL = 94.000 confirms criterion-independent essential PARTIAL weight**: C-02 PARTIAL (BUDGET arithmetic present but Delta/Flag absent) yields 94.000, the same composite as C-04 PARTIAL in R10. Essential PARTIAL penalty = 6 pts regardless of which essential criterion carries the PARTIAL (each essential = 12 pts at 5 essential criteria; PARTIAL weight = 0.5 = 6 pts lost). The PARTIAL formula is uniform across the essential tier.
5. **Essential PARTIAL + 1 recommended FAIL = 84.000, NOT GOLDEN**: V-05 (C-02 PARTIAL + C-08 FAIL) scores 84.000 but is not golden. Extends C-28/C-29 ranking inversion: 84.000 composite is not golden while R10 V-04's 80.000 composite is. The PARTIAL gate dominates composite rank regardless of which essential criterion is PARTIAL.

### V-02 design note

C-10 behavior under STRATEGY omission: C-10 tests "STRATEGY section precedes ARCHITECT table." The rubric passes C-10 as N/A when the output contains no STRATEGY section -- the precondition of the criterion is simply absent. This is distinct from C-10 FAIL, which requires ARCHITECT to appear before a present STRATEGY. The discovery here is that STRATEGY omission and STRATEGY reordering have asymmetric C-10 consequences: omission = N/A (no cost); reordering = FAIL (full cost). To target C-10 FAIL explicitly, a future variation must present STRATEGY after ARCHITECT, not remove it.

### V-04 design note

C-18 independence from C-06: C-18 tests whether the template independently authors three sub-line slots. V-04 uses three slots (1. action, (2) vague rating note, inertia saved) with slot 2 underspecified. C-18 PASS (three slots present in template); C-06 FAIL (slot 2 produces no explicit "[Component] from [COLOR] to [COLOR], raising score by [N] pts" line in output). The "(2) If a rating change is expected, note it." instruction is deliberately vague -- it does not author the color-transition + score-delta line as required by C-06. This preserves the three-slot template structure (C-18) while suppressing the explicit quantified transition (C-06).

---

## V-01 -- Phrasing Register: Formal/Technical (Baseline Golden under v9)

**Axis**: Single-axis. Phrasing register -- formal/technical. The prompt uses strict second-person imperative framing ("You are acting as", "Do not", "you will record", "STOP.") and precise technical language throughout. All structural requirements are fully specified; no obligations are weakened. R10 V-01 established that conversational register is criterion-neutral (C-32 PASS). This variation tests the opposite end: formal/technical register is also criterion-neutral. Hypothesis: phrasing register does not affect any criterion in either direction.

**Hypothesis**: All PASS. C-32 PASS (formal register is criterion-neutral, confirming bidirectionality). Composite: (5/5 x 60) + (3/3 x 30) + (25/25 x 10) = 100.000. Golden.

**Changed from R10 V-01**: All phrasing shifted to formal/technical register throughout. "Work as" -> "You are acting as"; "keep these three things in mind" -> "observe the following directives"; "Don't" -> "Do not"; "Before proceeding, revise..." -> "STOP. Revise..."; "Both conditions satisfied -- write Item B now." -> "Both conditions are satisfied. Write Item B."; "Fill this before PM: BUDGET." -> "Complete this section before PM: BUDGET."; "Don't write any traffic light" -> "Do not write any traffic light"; soft AMEND gate -> "If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL." Structural requirements unchanged.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it reshapes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability that raises the cost of not replacing it per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section to add at the end. All focus content must appear inside the existing sections, integrated against the named incumbent.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. If one begins forming, move its content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions are satisfied. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions are satisfied. Write Item B.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation demonstrably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

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
    Minimum count: at least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Complete this section before PM: BUDGET. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before completing this section.

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
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.
If focus changes procurement logic (e.g., compliance focus favors a certified third party over in-house vs. the named incumbent), note it in Rationale.

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation before proceeding to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment. Do not omit any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in this order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold before writing updated Item B.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

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

## V-02 -- Role Sequence: STRATEGY Section Omitted (C-08 FAIL, C-10 N/A)

**Axis**: Single-axis. Role sequence -- STRATEGY section eliminated entirely. The BUILD-VS-BUY analysis is removed; components proceed directly to ARCHITECT with procurement approach captured inline in the Rationale column. C-08 FAIL: no dedicated STRATEGY section with 50%+ Build/Buy/Use coverage. C-10: passes N/A -- the rubric's N/A pass condition fires when no STRATEGY section is present in the output (C-10 tests "STRATEGY precedes ARCHITECT"; if STRATEGY is absent, the criterion is vacuously N/A, not FAIL). All essential and focus-axis criteria unaffected.

**Hypothesis**: C-08 FAIL (recommended), C-10 N/A (aspirational -- counts as PASS). All 5 essential PASS. C-06 PASS, C-07 PASS. Aspirational: 25/25 PASS (C-10 N/A counted as PASS). Composite: (5/5 x 60) + (2/3 x 30) + (25/25 x 10) = 60 + 20 + 10 = 90.000. Golden.

**Key question probed**: Does STRATEGY omission trigger C-10 FAIL or C-10 N/A? Hypothesis: N/A, not FAIL. Confirms C-10 N/A pass condition and establishes that the only way to trigger C-10 FAIL is to present ARCHITECT before a present STRATEGY section.

**Changed from V-01**: STRATEGY: BUILD-VS-BUY section removed entirely. ARCHITECT header updated: "Confirmation: STRATEGY: BUILD-VS-BUY is written above." removed; "No new components may be added in ARCHITECT without a corresponding STRATEGY entry." removed; inline procurement note added to ARCHITECT intro. All other sections unchanged.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it reshapes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability that raises the cost of not replacing it per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section to add at the end. All focus content must appear inside the existing sections, integrated against the named incumbent.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. If one begins forming, move its content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions are satisfied. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions are satisfied. Write Item B.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation demonstrably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

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
    Minimum count: at least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Complete this section before PM: BUDGET. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before completing this section.

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
Before rating components, identify each component's procurement approach (Build / Buy / Use existing) in the Rationale column.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- procurement approach + vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|-------------------------------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Build/Buy/Use existing: [approach]. Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment. Do not omit any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in this order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold before writing updated Item B.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

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

## V-03 -- Lifecycle Emphasis: BUDGET Streamlined, No Delta/Flag (C-02 PARTIAL)

**Axis**: Single-axis. Lifecycle emphasis -- BUDGET section compressed. The budget section retains the available-hours formula and the component estimate table, but removes the Delta and Flag summary lines. C-02 PARTIAL: arithmetic is present (hours formula, component estimates, summed total) but the structural completeness gate (explicit Delta and Flag closing the budget analysis) is absent. All other sections including Do-nothing cost column in ARCHITECT (C-04 PASS), full Propagation Contract (C-33 PASS), and AMENDMENTS color-transition (C-06 PASS) are unchanged.

**Hypothesis**: C-02 PARTIAL (essential). All other essential PASS. Recommended 3/3 PASS. Aspirational 25/25 PASS. Composite: (4.5/5 x 60) + (3/3 x 30) + (25/25 x 10) = 54 + 30 + 10 = 94.000. NOT GOLDEN (PARTIAL gate). Confirms that C-02 PARTIAL = 94.000, same composite as C-04 PARTIAL from R10. Essential PARTIAL penalty is uniform across the essential tier.

**Changed from V-01**: PM: BUDGET section: Delta and Flag lines removed from the arithmetic summary block. "Compare Total to Available hours when assigning the VERDICT score." added in their place. All other sections unchanged.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it reshapes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability that raises the cost of not replacing it per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section to add at the end. All focus content must appear inside the existing sections, integrated against the named incumbent.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. If one begins forming, move its content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions are satisfied. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions are satisfied. Write Item B.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation demonstrably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

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
    Minimum count: at least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Complete this section before PM: BUDGET. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before completing this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

Compare Total to Available hours when assigning the VERDICT score.

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.
If focus changes procurement logic (e.g., compliance focus favors a certified third party over in-house vs. the named incumbent), note it in Rationale.

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation before proceeding to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget comparison from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment. Do not omit any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in this order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold before writing updated Item B.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

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

## V-04 -- Output Format: AMENDMENTS C-06 Isolated FAIL (C-06 FAIL Only)

**Axis**: Single-axis. Output format -- AMENDMENTS color-transition suppressed. AMENDMENTS template uses three sub-line slots (C-18 PASS: template independently authors three structural items) but slot 2 is replaced with a vague directive that does not produce the explicit color-transition + score-delta line required by C-06. C-06 FAIL: "[Component] from [COLOR] to [COLOR], raising score by approximately [N] pts" absent from output. STRATEGY fully intact (C-08 PASS). Focus axis unaffected (C-09 PASS via table). All essential PASS.

**Hypothesis**: C-06 FAIL (recommended). All 5 essential PASS. C-07 PASS, C-08 PASS. C-18 PASS (three sub-line slots present in template; slot 2 underspecified but present). Aspirational: 25/25 PASS. Composite: (5/5 x 60) + (2/3 x 30) + (25/25 x 10) = 60 + 20 + 10 = 90.000. Golden.

**Parity target**: V-02 (C-08 FAIL) = 90.000 and V-04 (C-06 FAIL) = 90.000. Both achieve the same composite from different single recommended-tier FAILs. Confirms equal and independent cost per recommended criterion (10 pts each at /3 recommended with 30 total weight).

**Changed from V-01**: AMENDMENTS template sub-line 2 changed from "This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts." to "(2) If a rating change is expected, note it." Three slots preserved (C-18 PASS); slot 2 instruction underspecified (C-06 FAIL). All other sections unchanged.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it reshapes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability that raises the cost of not replacing it per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section to add at the end. All focus content must appear inside the existing sections, integrated against the named incumbent.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. If one begins forming, move its content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions are satisfied. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions are satisfied. Write Item B.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation demonstrably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

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
    Minimum count: at least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Complete this section before PM: BUDGET. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before completing this section.

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
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.
If focus changes procurement logic (e.g., compliance focus favors a certified third party over in-house vs. the named incumbent), note it in Rationale.

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation before proceeding to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) If a rating change is expected, note it.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in this order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold before writing updated Item B.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

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

## V-05 -- Role Sequence + Lifecycle: STRATEGY Omitted + BUDGET Streamlined (C-02 PARTIAL + C-08 FAIL)

**Axis**: Combination. Role sequence (STRATEGY omitted, V-02 mechanism) + Lifecycle emphasis (BUDGET no Delta/Flag, V-03 mechanism). C-02 PARTIAL: budget arithmetic present but Delta and Flag lines absent. C-08 FAIL: no STRATEGY section with 50%+ Build/Buy/Use coverage. C-10 N/A: STRATEGY absent, criterion vacuously passes. All other essential criteria PASS. AMENDMENTS color-transition intact (C-06 PASS). Propagation Contract table intact (C-09 PASS, C-33 PASS).

**Hypothesis**: C-02 PARTIAL (essential), C-08 FAIL (recommended), C-10 N/A (aspirational -- PASS). All other essential PASS. C-06 PASS, C-07 PASS. Aspirational: 25/25 PASS. Composite: (4.5/5 x 60) + (2/3 x 30) + (25/25 x 10) = 54 + 20 + 10 = 84.000. NOT GOLDEN (PARTIAL gate).

**Ranking inversion extended**: V-05 (84.000) outranks R10 V-04 (80.000) by composite but is not golden while R10 V-04 is golden. Extends C-28/C-29 from R10: the ranking inversion is not specific to C-04 PARTIAL -- any essential PARTIAL creates the same inversion regardless of which essential criterion carries it or how many recommended criteria additionally FAIL. 84.000 composite with C-02 PARTIAL is not golden; 80.000 composite without PARTIAL is golden.

**Changed from V-01**: STRATEGY: BUILD-VS-BUY section removed (V-02 mechanism); ARCHITECT inline procurement note added. PM: BUDGET Delta and Flag lines removed (V-03 mechanism); "Compare Total to Available hours when assigning the VERDICT score." substituted.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it reshapes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability that raises the cost of not replacing it per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it is not a section to add at the end. All focus content must appear inside the existing sections, integrated against the named incumbent.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. If one begins forming, move its content into the relevant section in the Propagation Contract below.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Do not write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions are satisfied. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan so the equation label is `focus_adjusted_total`.
    Return here after adjusting. Do not write Item B until the LHS label is confirmed.

Both conditions are satisfied. Write Item B.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is what makes the competitive calculation demonstrably different from a no-focus run against the named incumbent.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection: subtracting base_cost from focus_adjusted_total equals focus_adjustment.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

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
    Minimum count: at least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Complete this section before PM: BUDGET. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Do not write any traffic light before completing this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

Compare Total to Available hours when assigning the VERDICT score.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Before rating components, identify each component's procurement approach (Build / Buy / Use existing) in the Rationale column.
Use the budget comparison from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- procurement approach + vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|-------------------------------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Build/Buy/Use existing: [approach]. Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment. Do not omit any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in this order:
    (a) Rewrite Item A table with new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
             If not satisfied: revise the updated AMENDMENTS row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold before writing updated Item B.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula).
    (e) Write updated Item D (failure-mode rejection for new focus dimension).
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

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
