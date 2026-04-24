Written to `simulations/quest/variations/discover-feasibility-alt-variations-R13-2026-03-18.md`.

---

## Round 13 Variations — discover-feasibility-alt

| | Axis | Mechanism | Target Failure(s) | Composite | Golden? |
|---|---|---|---|---|---|
| **V-01** | Lifecycle emphasis | INFERENCE GATE — Team/Timeline lines removed | C-01 FAIL | 88.000 | No |
| **V-02** | Output format | Focus-active prose contract (no 4-row table) | C-33 FAIL | 99.706 | Yes |
| **V-03** | Role sequence | focus_adjusted_total computed in Step 0 but stripped from all downstream directives | C-05 FAIL + C-07 FAIL + C-09 FAIL | 77.706 | No |
| **V-04** | Lifecycle + inertia compound | Team/Timeline removed AND anchor minimum = 1 | C-01 FAIL + C-03 FAIL | 76.000 | No |
| **V-05** | Inertia + role sequence compound | Anchor minimum = 1 AND STRATEGY removed | C-03 FAIL + C-08 FAIL | 78.000 | No |

### New patterns these target for v12

- **C-01 FAIL = 88.000** (V-01): Extends C-38 criterion-neutrality to C-01. The INFERENCE GATE completeness failure matches the propagation failure (C-03 R12) at the same 88.000 floor.

- **C-33 FAIL independent of C-09** (V-02): The previously always-compound C-33+C-09 pattern is not structurally obligatory. Prose contracts can propagate focus to 2+ sections (C-09 PASS) while failing the table-structure criterion (C-33 FAIL). New composite 99.706 — one aspirational FAIL vs. two.

- **C-05 cascade at /34** (V-03): C-23 cascade formula at the new denominator — 77.706 (vs. pre-/34 values). Confirms the cascade still produces composite < 80 at /34 and the formula 4/5×60 + 2/3×30 + 33/34×10 is correct.

- **Two-essential-FAIL additivity** (V-04): 60−12−12 = 36 essential pts → 76.000. First confirmation that co-occurring essential FAILs are additive with no amplification. Opens the lower essential floor topology.

- **Cross-tier FAIL additivity** (V-05): 88 (essential FAIL) − 10 (recommended FAIL) = 78.000. New floor point between V-04 (76) and the two-recommended-FAIL border (80). Confirms essential and recommended tier costs add independently.
loor (76.000, V-04) and two-recommended-FAIL border (80.000).

### Key mechanism decisions

**V-01 mechanism (C-01 FAIL)**: INFERENCE GATE template removes the "Team:" and "Timeline:" lines entirely. Feature slot retained. Without the Team and Timeline template lines, the model produces an INFERENCE GATE that is incomplete on C-01 (requires Feature + Team + Timeline). C-02 budget arithmetic unchanged: PM: BUDGET uses [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] as independent placeholders, not derived from INFERENCE GATE lines. C-03 anchor minimum unchanged (2+ required). C-04 do-nothing cost column unchanged. Focus inactive: C-05 N/A.

**V-02 mechanism (C-33 FAIL, C-09 PASS)**: Focus active. Step 0 Item A replaced with prose description of the four propagation effects (not a 4-row table). Formula Contract Check (conditions i and ii) and Items B-D retained. All downstream section directives (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) retain focus_adjusted_total references -- C-09 PASS (focus_adjusted_total in 2+ sections). C-33 requires the 4-row table structure; prose form fails C-33 regardless of propagation coverage. C-07 PASS: focus demonstrably changes component ratings (ARCHITECT directive unchanged). All essential criteria unchanged from golden.

**V-03 mechanism (C-05 FAIL cascade)**: Focus active. Step 0 computes focus_adjusted_total via Items A-D (4-row table present; C-33 PASS). But downstream section directives strip all focus_adjusted_total references: INERTIA cost cell uses "[base_cost]" unconditionally; ARCHITECT do-nothing cost uses base_cost; VERDICT "Not building this means:" references base_cost only; AMENDMENTS inertia-saved framing omits focus_adjustment. C-05 FAIL: focus_adjusted_total absent from INERTIA + VERDICT + AMENDMENTS. Cascade per C-23: C-07 FAIL (focus never visible in base analysis), C-09 FAIL (focus_adjusted_total in 0 downstream sections). C-33 PASS (table structurally intact; deficiency is downstream-only).

**V-04 mechanism (C-01 FAIL + C-03 FAIL)**: Two simultaneous essential FAILs. INFERENCE GATE removes Team and Timeline lines (C-01 FAIL). INFERENCE GATE anchor minimum reduced from "at least two of these three anchors are required" to "anchor (1) is required. Anchors (2) and (3) are optional traceability aids" per R12 V-01 mechanism (C-03 FAIL). All recommended and aspirational unchanged from golden. Tests essential-tier FAIL additivity.

**V-05 mechanism (C-03 FAIL + C-08 FAIL)**: Two-axis compound across essential and recommended tiers. C-03 FAIL: anchor minimum = 1 per R12 V-01. C-08 FAIL: STRATEGY section removed; procurement captured inline in ARCHITECT Rationale column per R11 V-02. ARCHITECT heading updated to remove STRATEGY back-reference; inline procurement note added to table template. C-10 N/A per C-35 (STRATEGY absent). No focus: C-07 N/A, C-09 N/A, C-33 N/A. C-06 PASS (AMENDMENTS color-transition unchanged). C-04 PASS (do-nothing cost column mandate unchanged). All N/A count as PASS: aspirational 34/34 x 10 = 10.

### Floor derivations under v11 (denominator /34)

| Variation | Definition | Formula | Composite | Golden? |
|-----------|-----------|---------|-----------|---------|
| V-01 | C-01 FAIL | 4/5x60 + 3/3x30 + 34/34x10 | 88.000 | No (essential FAIL) |
| V-02 | C-33 FAIL, C-09 PASS (prose contract, focus active) | 5/5x60 + 3/3x30 + 33/34x10 | 99.706 | Yes |
| V-03 | C-05 FAIL + C-07 FAIL + C-09 FAIL (cascade, focus active) | 4/5x60 + 2/3x30 + 33/34x10 | 77.706 | No (FAIL gate + <80) |
| V-04 | C-01 FAIL + C-03 FAIL | 3/5x60 + 3/3x30 + 34/34x10 | 76.000 | No (FAIL gate + <80) |
| V-05 | C-03 FAIL + C-08 FAIL (C-10 N/A) | 4/5x60 + 2/3x30 + 34/34x10 | 78.000 | No (FAIL gate + <80) |

---

## V-01 -- Lifecycle Emphasis: INFERENCE GATE Team/Timeline Absent (C-01 FAIL)

**Axis**: Single-axis. Lifecycle emphasis -- INFERENCE GATE completeness weakened. Team and Timeline lines removed from the INFERENCE GATE template. Feature slot retained; Team and Timeline slots absent entirely. C-01 requires Feature + Team + Timeline; template by design produces Feature only. C-02 budget arithmetic unchanged (PM: BUDGET uses [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] as independent placeholders). All other sections unchanged from golden.

**Hypothesis**: C-01 FAIL (essential). All other essential PASS. All recommended PASS. All aspirational PASS. Composite: `4/5x60 + 3/3x30 + 34/34x10 = 88.000`. Not golden (essential FAIL gate). Confirms C-38 criterion-neutrality for C-01: C-01 FAIL = C-03 FAIL (R12 V-01) = 88.000.

**Changed from golden**: INFERENCE GATE section -- "Team: [N engineers -- inferred from: SOURCE]" and "Timeline: [N sprints / N weeks -- inferred from: SOURCE]" lines removed. Feature and Named incumbent block unchanged. Anchor minimum unchanged (at least two required). PM: BUDGET formula and all other sections unchanged.

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
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
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

## V-02 -- Output Format: Focus-Active Prose Contract, Table Absent (C-33 FAIL, C-09 PASS)

**Axis**: Single-axis. Output format -- Step 0 Item A Propagation Contract written as prose description rather than 4-row table. Focus is active. The four propagation effects (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) are described in paragraph form instead of the table structure. All four effects are still described and all downstream section directives retain focus_adjusted_total references -- C-09 PASS (focus_adjusted_total in 2+ sections: INERTIA + VERDICT + AMENDMENTS). C-33 requires the 4-row table structure; prose form fails C-33. C-07 PASS: focus demonstrably changes component ratings (ARCHITECT directive unchanged). All essential criteria unchanged from golden.

**Hypothesis**: C-33 FAIL (aspirational). All essential PASS. All recommended PASS. All other aspirational PASS. Composite: `5/5x60 + 3/3x30 + 33/34x10 = 99.706`. Golden. New pattern: C-33 can FAIL independently of C-09. Splits the always-compound C-33+C-09 FAIL in v11 floor V-02 (99.412 = two aspirational FAILs). Confirms the contract structure is independent of downstream propagation coverage.

**Changed from golden**: Step 0 Item A: 4-row table replaced with prose paragraph descriptions of INERTIA, ARCHITECT, VERDICT, and AMENDMENTS effects. Formula Contract Check labels adjusted from "TABLE SIDE" to "PROSE SIDE." All downstream section directives (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) retain full focus_adjusted_total references unchanged from golden.

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
Name the primary constraint this focus introduces. Describe how it surfaces in each of the four downstream sections. The descriptions reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

Write the four propagation effects as connected prose:

INERTIA: State the primary focus-introduced constraint and how focus_adjusted_total from Item C will appear in the named incumbent's cost-per-sprint or Baseline sentence in the INERTIA section.

ARCHITECT: State which component(s) the focus constraint rates RED or YELLOW and how focus_adjusted_total changes their rating compared to a no-focus run against the named incumbent.

VERDICT: State any prerequisite added and/or score band impact; confirm focus_adjusted_total will appear in "Not building this means:" tied to the named incumbent.

AMENDMENTS: State the focus-specific inertia savings -- base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when the named incumbent is replaced.

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- PROSE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one of the four effect
  descriptions above.
  Check: scan the four descriptions. Does any contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS description to include the phrase
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
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the prose descriptions in Item A, using the economics from Item C's formula.

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

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA effect described in Step 0 Item A. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Step 0 Item A if active] |

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

[If focus active: deliver on the ARCHITECT effect described in Step 0 Item A. focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

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
[Deliver on the VERDICT effect described in Step 0 Item A.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[If focus active: deliver on the AMENDMENTS effect described in Step 0 Item A. Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
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
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract descriptions identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Rewrite each affected section with the amendment applied. Use the original section headings verbatim.
  For a focus shift: update Step 0 Items A-D first -- in this order:
    (a) Rewrite Item A prose descriptions with new focus constraint and new effect descriptions.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` appears by exact name in at least one effect description.
             If not satisfied: revise the updated AMENDMENTS description now before proceeding.
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

## V-03 -- Role Sequence: Focus Economics Computed But Not Propagated Downstream (C-05 FAIL cascade)

**Axis**: Single-axis. Role sequence -- Step 0 computes focus_adjusted_total correctly (4-row table present, Formula Contract Check passes, Items B-D intact; C-33 PASS) but downstream section directives strip all references to focus_adjusted_total. INERTIA do-nothing cost uses [base_cost]; ARCHITECT do-nothing column uses base_cost; VERDICT uses base_cost; AMENDMENTS inertia-saved omits focus_adjustment. C-05 requires focus_adjusted_total in INERTIA + VERDICT + AMENDMENTS; absent from all three = C-05 FAIL. Per C-23: C-05 FAIL cascades to C-07 FAIL (focus not demonstrably visible in base analysis) + C-09 FAIL (focus_adjusted_total in 0 downstream sections). C-33 PASS (table structurally intact; deficiency is downstream only).

**Hypothesis**: C-05 FAIL (essential) + C-07 FAIL (recommended) + C-09 FAIL (aspirational). All other essential PASS. C-06 PASS, C-08 PASS. C-33 PASS. Composite: `4/5x60 + 2/3x30 + 33/34x10 = 48 + 20 + 9.706 = 77.706`. Not golden (essential FAIL gate AND composite < 80). Confirms C-23 cascade at /34 denominator: 77.706.

**Changed from golden**: (1) INERTIA table cost cell: "[focus_adjusted_total from Step 0 Item C if active; base_cost if no focus]" replaced with "[base_cost]" unconditionally; focus-active note removed entirely. (2) INERTIA Baseline: "[focus_adjusted_total or base_cost]" replaced with "[base_cost]". (3) ARCHITECT section: "use focus_adjusted_total from Step 0 Item C where applicable" replaced with "use base_cost for all rows"; focus-active ARCHITECT row directive "[If focus active: ...]" removed. (4) ARCHITECT table Rationale and Do-nothing cost cells: focus_adjusted_total references removed; base_cost used unconditionally. (5) VERDICT: "State focus_adjusted_total from Step 0 Item C" replaced with "State base_cost"; "[focus_adjusted_total or base_cost]" in VERDICT Baseline replaced with "[base_cost]". (6) AMENDMENTS: "[If focus active: focus_adjustment eliminated: ... Total inertia saved: ...]" block removed; only base inertia-saved line retained.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it introduces a constraint worth noting in the setup phase. Record the focus lens and compute the focus economics in Step 0, but all downstream section analysis uses the base incumbent cost.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end.

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

**Item C -- Focus Economics (reference computation):**
Compute the focus-adjusted do-nothing cost for reference. This is a Step 0 reference value only.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Note: downstream analysis sections use base_cost. The focus_adjusted_total is recorded here for reference.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS.

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

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [base_cost] | [Risk tied to incumbent] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [base_cost per sprint]."

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

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation before proceeding to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use base_cost for all rows.

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [base_cost] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [base_cost.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at [base_cost] per sprint. State the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint].

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected.
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
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- Lifecycle + Inertia Framing Compound: INFERENCE GATE Incomplete AND Anchor Minimum = 1 (C-01 FAIL + C-03 FAIL)

**Axis**: Compound. Two simultaneous essential FAILs. Lifecycle emphasis: INFERENCE GATE removes Team and Timeline lines (C-01 FAIL). Inertia framing: anchor minimum reduced to 1 per R12 V-01 mechanism (C-03 FAIL). Tests whether essential FAIL costs are additive with no inter-criterion amplification.

**Hypothesis**: C-01 FAIL + C-03 FAIL (essential). All recommended PASS. All aspirational PASS. Composite: `3/5x60 + 3/3x30 + 34/34x10 = 36 + 30 + 10 = 76.000`. Not golden (essential FAIL gate AND composite < 80). New pattern: Two-essential-FAIL additivity -- 76.000 = 88.000 (single FAIL) - 12 (second independent FAIL). No amplification between co-occurring essential FAILs.

**Changed from golden**: (1) INFERENCE GATE: "Team: [N engineers -- inferred from: SOURCE]" and "Timeline: [N sprints / N weeks -- inferred from: SOURCE]" lines removed. (2) INFERENCE GATE anchor minimum: "at least two of these three anchors are required; all three are recommended" replaced with "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." All other sections unchanged from golden.

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
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
    Propagation anchor -- use the following form in the INERTIA section heading:
    (1) INERTIA section heading (required):
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header (optional):
        Form: "[Named incumbent]" as the column header label
    (3) AMENDMENTS inertia-saved framing (optional):
        Form: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: anchor (1) is required. Anchors (2) and (3) are optional traceability aids.

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
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
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

## V-05 -- Inertia Framing + Role Sequence Compound: Anchor Minimum = 1 AND STRATEGY Removed (C-03 FAIL + C-08 FAIL)

**Axis**: Compound. Two-axis compound across essential and recommended tiers. Inertia framing: anchor minimum = 1 per R12 V-01 (C-03 FAIL). Role sequence: STRATEGY section removed; procurement inline in ARCHITECT Rationale per R11 V-02 (C-08 FAIL). C-10 N/A per C-35 (STRATEGY absent). No focus: C-07 N/A, C-09 N/A, C-33 N/A. C-06 PASS (color-transition unchanged). C-04 PASS (do-nothing cost column mandate unchanged). All N/A = PASS in their respective tiers.

**Hypothesis**: C-03 FAIL (essential) + C-08 FAIL (recommended). C-10 N/A. All other essential PASS. C-06 PASS, C-07 N/A. Composite: `4/5x60 + 2/3x30 + 34/34x10 = 48 + 20 + 10 = 78.000`. Not golden (essential FAIL gate AND composite < 80). New pattern: Essential + recommended FAIL cross-tier additivity = 78.000. Falls between two-essential-FAIL floor (V-04, 76.000) and two-recommended-FAIL border (80.000).

**Changed from golden**: (1) INFERENCE GATE anchor minimum: "at least two of these three anchors are required; all three are recommended" replaced with "anchor (1) is required. Anchors (2) and (3) are optional traceability aids." (2) STRATEGY section removed entirely. (3) ARCHITECT heading: "Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity." replaced with "Rate each component for complexity. Capture Build / Buy / Use existing decisions inline in the Rationale column."

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
    Propagation anchor -- use the following form in the INERTIA section heading:
    (1) INERTIA section heading (required):
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header (optional):
        Form: "[Named incumbent]" as the column header label
    (3) AMENDMENTS inertia-saved framing (optional):
        Form: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: anchor (1) is required. Anchors (2) and (3) are optional traceability aids.

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
Rate each component for complexity. Capture Build / Buy / Use existing decisions inline in the Rationale column.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics (Build/Buy/Use existing) | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating; state Build/Buy/Use existing decision] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

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
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
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
