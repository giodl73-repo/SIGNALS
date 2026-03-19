Written to `simulations/quest/variations/discover-feasibility-alt-variations-R17-2026-03-18.md`.

---

**Round 17 -- 5 variations**

| | Axis | Target | Composite | New pattern |
|---|---|---|---|---|
| **V-01** | Lifecycle emphasis | C-01+C-02+C-03+C-04 FAIL (K=4, no focus) | 52.000 | First empirical test of 100-12K at K=4; extends C-48 |
| **V-02** | Inertia framing | C-05 FAIL (appended), C-33 PASS (table), C-09 FAIL (C-46 pattern) | 77.750 | Re-confirms V-09 at /40; tests C-46 at current denominator |
| **V-03** | Output format | C-01 + C-02 FAIL (Team+Timeline absent, PM: BUDGET absent) | 76.000 | Confirms C-44 criterion-neutrality for new pair (C-01+C-02 vs canonical C-01+C-03) |
| **V-04** | Phrasing register + lifecycle | C-02 PARTIAL, focus active, formal register | 94.000 | Confirms C-39 in focus-active context; PARTIAL floor is focus-state-independent |
| **V-05** | Role sequence | C-02 FAIL + C-08 FAIL (no budget block, no STRATEGY) | 78.000 | Confirms C-45 for new essential+recommended pair (C-02+C-08 vs canonical C-03+C-08) |

**Design rationale:**
- V-01 targets the one remaining unconfirmed prediction in the essential-tier profile: K=4 (52.000). K=5 (40.000) will be the only remaining formula-only prediction after R17.
- V-02 re-tests the C-46 cascade formula at /40 -- the empirical anchor was at lower denominators; the formula predicts 77.750 and this confirms it.
- V-03 + V-05 both extend criterion-neutrality claims (C-44 and C-45) to new essential pairs, systematically closing coverage of the cross-product space.
- V-04 is the focus-active PARTIAL test that was skipped in prior rounds -- pairs with R12 V-02 (no-focus C-04 PARTIAL = 94.000) and R16 V-02 (focus+conversational = 100.000) to complete the 2x2 focus-state x PARTIAL matrix.
er this round.

2. **V-02 C-46 construction**: Step 0 4-row table IS present and structurally complete (C-33 PASS). But (a) the 3rd preamble directive redirects focus to a post-AMENDMENTS standalone block, and (b) each downstream section's focus bracket says "use base_cost only in this section." This voids focus_adjusted_total from all three C-05 destinations (INERTIA, VERDICT, AMENDMENTS) despite the table committing to them. C-05 FAIL cascades to C-07 FAIL + C-09 FAIL. Aspirational: 39/40 x 10 = 9.75 (only C-09 FAIL). Composite: 48 + 20 + 9.75 = 77.750.

3. **V-04 C-02 PARTIAL in focus-active context**: C-02 PARTIAL requires arithmetic present but Delta and Flag lines absent (C-37 anatomy). With focus active and all focus criteria PASS (C-05, C-07, C-09, C-33 all PASS), essential = 4.5/5 x 60 = 54, recommended = 3/3 x 30 = 30 (C-07 PASS because focus is woven and demonstrably changes INERTIA baseline), aspirational = 40/40 x 10 = 10. Composite 94.000, not golden: PARTIAL gate fires (C-28/C-42) regardless of focus-axis completeness. Tests C-39 criterion-neutrality across focus states.

**Floor derivations under v15 (denominator /40):**

| Variation | Definition | Formula | Composite | Golden? |
|-----------|-----------|---------|-----------|---------|
| V-01 | C-01+C-02+C-03+C-04 FAIL (four essential FAILs, no focus) | 1/5x60 + 3/3x30 + 40/40x10 | 52.000 | No (essential FAIL gate + composite < 80) |
| V-02 | C-05 FAIL cascade (appended focus, C-33 PASS, C-09 FAIL) | 4/5x60 + 2/3x30 + 39/40x10 | 77.750 | No (essential FAIL gate + cascade) |
| V-03 | C-01 + C-02 FAIL (Team+Timeline absent, PM: BUDGET block absent) | 3/5x60 + 3/3x30 + 40/40x10 | 76.000 | No (essential FAIL gate) |
| V-04 | C-02 PARTIAL + focus active, formal register, all else PASS | (4.5/5x60) + 3/3x30 + 40/40x10 | 94.000 | No (PARTIAL gate) |
| V-05 | C-02 FAIL + C-08 FAIL (PM: BUDGET absent, STRATEGY absent) | 4/5x60 + 2/3x30 + 40/40x10 | 78.000 | No (essential FAIL gate) |

V-01 detail: essential = 12 (1/5 x 60); 12 + 30 + 10 = 52.000.
V-02 detail: 48 + 20 + 9.75 = 77.750. C-09 FAIL costs 10/40 = 0.250 pts; C-07 FAIL costs 10 pts; C-05 FAIL costs 12 pts.
V-03 detail: essential = 36 (3/5 x 60); 36 + 30 + 10 = 76.000. Same composite as V-07 rubric floor (C-01+C-03 pair), different pair.
V-04 detail: essential = 54 (4.5/5 x 60, C-02 PARTIAL); 54 + 30 + 10 = 94.000. Same composite as V-03 rubric floor (C-04 PARTIAL), different criterion and focus state.
V-05 detail: essential = 48 (4/5 x 60, C-02 FAIL); recommended = 20 (C-08 FAIL, C-07 N/A counts as pass); 48 + 20 + 10 = 78.000. Same as V-08 rubric floor (C-03+C-08 pair), different essential criterion.

---

## V-01 -- Lifecycle Emphasis: Four-Essential-FAIL (K=4, C-01+C-02+C-03+C-04 FAIL, No Focus)

**Axis**: Single-axis. Lifecycle emphasis -- four essential criteria simultaneously fail. (1) INFERENCE GATE: Team and Timeline fields removed (C-01 FAIL). (2) PM: BUDGET block removed entirely -- full absence, not PARTIAL (C-02 FAIL). (3) INFERENCE GATE propagation block stripped to a single generic AMENDMENTS note; anchor (1) and anchor (2) removed; minimum count language removed; < 2 anchors = C-03 FAIL. (4) ARCHITECT: Do-nothing cost column removed entirely (C-04 FAIL). No focus. All recommended PASS. All aspirational PASS/N/A.

**Hypothesis**: C-01 FAIL + C-02 FAIL + C-03 FAIL + C-04 FAIL. All recommended PASS. All aspirational PASS/N/A. Composite: `1/5x60 + 3/3x30 + 40/40x10 = 12 + 30 + 10 = 52.000`. Not golden. Extends C-44/C-48 additivity profile 100-12K: K=1 (88), K=2 (76), K=3 (64), K=4 (52 -- first empirical test). Confirms essential-tier FAIL additivity has no amplification through K=4.

**Changed from golden**: (1) INFERENCE GATE: Team and Timeline lines removed. Feature and Named incumbent retained. (2) PM: BUDGET block removed entirely -- no heading, no formula, no table, no output lines. (3) INFERENCE GATE propagation block: anchor (1) and anchor (2) specifications removed; minimum count language removed; only "Note: the incumbent name should appear in AMENDMENTS savings framing as applicable." retained. (4) INERTIA heading directive "(Rename this heading to match anchor (1) above.)" removed. (5) INERTIA table first column header changed to "[Status quo]". (6) ARCHITECT heading: Do-nothing cost directive removed. (7) ARCHITECT table: Do-nothing cost column removed. (8) RED Blockers: Do-nothing cost line removed.

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
    Note: the incumbent name should appear in AMENDMENTS savings framing as applicable.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Complete this section before STRATEGY: BUILD-VS-BUY. Use the incumbent name from INFERENCE GATE throughout.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Status quo | What it costs per sprint | What happens if it remains in place |
|------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

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

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics |
|-----------|----------------------|------------|--------------------------------------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]

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

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" as applicable.]

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

## V-02 -- Inertia Framing: C-05 Append Cascade at /40 (C-46 Pattern, Focus Active)

**Axis**: Single-axis. Inertia framing -- focus redirected to a post-AMENDMENTS standalone block rather than woven into existing sections. The 4-row Propagation Contract table IS present in Step 0 (C-33 PASS by structure). But (a) the 3rd preamble directive instructs focus content to go into a standalone "## [FOCUS DIMENSION] ANALYSIS" block after AMENDMENTS, and (b) each downstream section's focus bracket explicitly says "use base_cost only in this section." This is the C-46 override construction: the table commits to per-section propagation but the downstream template text executes the override. C-05 FAIL cascades to C-07 FAIL + C-09 FAIL. Focus active.

**Hypothesis**: C-05 FAIL (appended). Cascade: C-07 FAIL, C-09 FAIL. C-33 PASS (4-row table structurally intact). All other essential PASS. C-06 PASS, C-08 PASS. All aspirational PASS/N/A except C-09 FAIL. Composite: `4/5x60 + 2/3x30 + 39/40x10 = 48 + 20 + 9.75 = 77.750`. Not golden (essential FAIL gate). Confirms V-09 at /40 (formula 78 - 10/N at N=40 = 77.750). Empirically tests C-46 independence matrix at current denominator.

**Changed from golden**: (1) 3rd preamble directive: focus no longer woven -- redirected to post-AMENDMENTS standalone block. (2) 4th preamble directive: invites "## [FOCUS DIMENSION] ANALYSIS" section rather than rejecting it. (3) Step 0 Item D: delivery instruction for standalone block (replaces failure-mode rejection). (4) INERTIA focus bracket: "use base_cost only; focus analysis belongs in the dedicated block after AMENDMENTS." (5) ARCHITECT focus bracket: same override. (6) VERDICT: base_cost framing only. (7) AMENDMENTS: base_cost savings only. (8) New "## [FOCUS DIMENSION] ANALYSIS" template block added after AMENDMENTS.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, note it in Step 0 and compile all focus-specific analysis in a dedicated ## [FOCUS DIMENSION] ANALYSIS section placed after AMENDMENTS. Base-analysis sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) use base_cost only and do not reference focus_adjusted_total. The focus economics are isolated to their dedicated block.

**Add a ## [FOCUS DIMENSION] ANALYSIS section after AMENDMENTS** when focus is active. This is where focus_adjusted_total, lens definitions, and focus-specific component ratings appear. Do not distribute focus content across the base-analysis sections.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C would appear if this section were focus-adjusted -- reserved for the ## [FOCUS DIMENSION] ANALYSIS block] |
| [same] | ARCHITECT | [Which component(s) the constraint would rate RED or YELLOW on focus-adjusted economics -- reserved for the ## [FOCUS DIMENSION] ANALYSIS block] |
| [same] | VERDICT | [Score band impact and "Not building this means:" on focus-adjusted economics -- reserved for the ## [FOCUS DIMENSION] ANALYSIS block] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint -- reserved for the ## [FOCUS DIMENSION] ANALYSIS block] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise any row in Item A to include the phrase
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
Compute the focus-adjusted do-nothing cost. This value will be used exclusively in the ## [FOCUS DIMENSION] ANALYSIS block after AMENDMENTS -- base-analysis sections use base_cost only.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

The formula is verifiable by inspection. All base-analysis sections below use base_cost only. focus_adjusted_total appears in the ## [FOCUS DIMENSION] ANALYSIS block only.

**Item D -- Delivery instruction:**
After completing AMENDMENTS, write a ## [FOCUS DIMENSION] ANALYSIS section using the economics computed in Item C. That section holds all focus-adjusted analysis: focus_adjusted_total, component re-ratings on focus-adjusted economics, and focus-specific inertia savings. Do not distribute this content across the base-analysis sections.

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

[Focus active: use base_cost only in this section. Focus-adjusted analysis belongs in the ## [FOCUS DIMENSION] ANALYSIS block after AMENDMENTS. Do not use focus_adjusted_total here.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [base_cost -- do not use focus_adjusted_total in this section] | [Risk tied to incumbent on base economics] |

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
| [Name]    | [Recommendation]           | [Rationale against named incumbent on base economics] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use base_cost from context.

[Focus active: rate all components against base economics only in this section. Focus-adjusted component ratings belong in the ## [FOCUS DIMENSION] ANALYSIS block after AMENDMENTS. Do not use focus_adjusted_total here.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on base economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|-----------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent on base economics] | [base_cost -- do not use focus_adjusted_total in this section] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on base economics.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [base_cost]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on base economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at approximately base_cost per sprint. State the long-term competitive consequence of the incumbent remaining on base economics.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on base economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[Focus active: use base_cost savings only in this section. Focus-adjusted inertia savings belong in the ## [FOCUS DIMENSION] ANALYSIS block after AMENDMENTS.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [base_cost per sprint].

Repeat for every RED and YELLOW component.

---

**## [FOCUS DIMENSION] ANALYSIS -- Focus-Adjusted Review**
Using focus_adjusted_total = [TOTAL] per sprint from Step 0 Item C.

Focus lens: [Item B summary -- what this focus dimension means for this topic against the named incumbent.]

Focus-adjusted do-nothing cost: focus_adjusted_total = base_cost + focus_adjustment = [TOTAL] per sprint.

| Component | Focus-adjusted rating | Rationale -- vs. named incumbent on focus_adjusted_total |
|-----------|----------------------|----------------------------------------------------------|
| [Name]    | GREEN / YELLOW / RED | [How focus_adjusted_total changes this rating vs. the base-economics rating above] |

Focus-adjusted VERDICT:
Not building this means: "[The named incumbent stays in place at focus_adjusted_total per sprint. State the focus-compounded competitive consequence.]"

Focus-specific inertia savings per amendment:
- [Component]: base_cost recaptured [N] + focus_adjustment eliminated [N] = focus_adjusted_total [TOTAL] per sprint recaptured when [Named incumbent] is replaced.

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
             If not satisfied: revise the updated row now before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: revise the updated Item C equation label before proceeding.
        Both conditions must hold before writing updated Item B.
    (c) Write updated Item B (lens definition for new focus).
    (d) Write updated Item C (new focus economics formula).
    (e) Write updated Item D (delivery instruction for new focus dimension).
  Then propagate the updated contract through the ## [FOCUS DIMENSION] ANALYSIS block.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update the ## [FOCUS DIMENSION] ANALYSIS block with new focus_adjusted_total if Step 0 Item C formula changed.
  Update prerequisites if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-03 -- Output Format: C-01 + C-02 FAIL (Team+Timeline Absent, PM: BUDGET Block Absent)

**Axis**: Single-axis. Output format -- INFERENCE GATE loses Team and Timeline fields (C-01 FAIL) AND PM: BUDGET block is removed entirely (C-02 FAIL: full absence). No focus. All three anchors present in INFERENCE GATE Named incumbent block (C-03 PASS). Do-nothing cost column present in ARCHITECT (C-04 PASS). C-05 N/A.

**Hypothesis**: C-01 FAIL + C-02 FAIL. All recommended PASS. All aspirational PASS/N/A. Composite: `3/5x60 + 3/3x30 + 40/40x10 = 36 + 30 + 10 = 76.000`. Not golden (essential FAIL gate). Confirms C-44 criterion-neutrality: two-essential-FAIL = 76.000 for the C-01+C-02 pair. The C-44 canonical (R13 V-04) used C-01+C-03; this variation uses C-01+C-02 -- a different pair. Tests whether the 76.000 floor and -24 pt deduction pattern hold regardless of which two essential criteria fail.

**Changed from golden**: (1) INFERENCE GATE: Team and Timeline lines removed. Feature and Named incumbent with all three anchors retained. (2) PM: BUDGET block removed entirely -- no heading, no formula, no table, no output lines. INERTIA directly precedes STRATEGY.

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
Complete this section before STRATEGY: BUILD-VS-BUY. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

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

## V-04 -- Phrasing Register + Lifecycle: C-02 PARTIAL, Focus Active, Formal/Technical Register

**Axis**: Compound. Phrasing register (formal/technical throughout) + lifecycle emphasis (PM: BUDGET arithmetic present but Delta and Flag lines absent = C-02 PARTIAL per C-37). Focus active. Full Step 0 (Items A-D, FORMULA CONTRACT CHECK). All three anchors. Do-nothing cost column in ARCHITECT. C-05 PASS (focus_adjusted_total propagates to INERTIA, VERDICT, AMENDMENTS). C-07 PASS (INERTIA baseline demonstrably shifts). C-09 PASS (all four Propagation Contract sections). C-33 PASS (4-row table). All recommended PASS. All aspirational PASS.

**Hypothesis**: C-02 PARTIAL only. All other essential PASS. All recommended PASS (C-07 PASS: focus active, woven, demonstrably changes analysis). All aspirational PASS. Essential: 4.5/5 x 60 = 54. Composite: `54 + 30 + 10 = 94.000`. Not golden (PARTIAL gate fires per C-28/C-42). Confirms C-39 in focus-active context: the 94.000 PARTIAL floor is criterion-neutral and focus-state-independent. Paired with V-01 R11 (conversational+focus = 100.000) and R12 V-02 (no-focus C-04 PARTIAL = 94.000): formal+focus+C-02 PARTIAL should also land at 94.000.

**Changed from golden**: (1) PM: BUDGET: Delta and Flag lines removed; Estimated and Available retained (C-02 PARTIAL via C-37 anatomy). (2) Register: all directives, item labels, section headings, and instructions rephrased in formal/technical language. No structural change.

```markdown
This analysis is conducted by a PM + Architect pair executing a build-or-not feasibility assessment.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

The following directives govern all sections of this analysis:

**Incumbent identification is required prior to analysis.** The INFERENCE GATE section must record the specific workaround, tool, or process currently employed by the team before any analytical computation begins. This designation serves as the competitive reference for all downstream sections; every section evaluates the proposed feature against this named incumbent by name.

**The named incumbent constitutes the primary competitive reference.** The analytical question is not whether the feature is technically constructible, but whether constructing it produces a superior outcome relative to the named incumbent. All sections frame their evaluations against the named incumbent.

**When a focus dimension is specified**, its introduction reshapes the competitive economics of the named incumbent. A compliance focus surfaces regulatory liability carried by the incumbent per sprint. A stakeholders focus surfaces sign-off overhead inherent to the incumbent's approval model. A size focus surfaces compounding degradation at the incumbent's scaling ceiling. The focus dimension modifies the competitive arithmetic; it is woven into the existing analytical sections rather than appended as a separate section after AMENDMENTS.

**No standalone focus section may appear after AMENDMENTS.** A heading of the form "## COMPLIANCE" or "## STAKEHOLDERS" appearing after AMENDMENTS constitutes a structural violation. Any focus-related content forming such a heading is relocated into the appropriate section of the Propagation Contract below.

**AMEND invocations**: Upon receipt of an AMEND instruction, proceed directly to the AMEND PROTOCOL at the conclusion of this template before executing any other section.

---

**Step 0 -- Propagation Contract Construction (required before any section is written)**

If focus is inactive: record "Focus: none" and proceed to INFERENCE GATE.

If focus is active, execute all four items in sequence -- Item A must be completed first:

**Item A -- Propagation Contract (prior to lens definition and economic computation):**
The primary constraint introduced by the focus dimension is identified and recorded in the table below. The complete table must be authored before proceeding to Item B or Item C. Stated Effect cells reference the formula variables to be computed in Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run against the named incumbent] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" tied to named incumbent] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT VERIFICATION -- two conditions must be independently satisfied before Item B is written.

CONDITION (i) -- TABLE VERIFICATION:
  Requirement: `focus_adjusted_total` must appear by exact token in at least one Stated Effect cell
  in the Item A table above.
  Verification: scan the Effect column. Is the token `focus_adjusted_total` present in any cell?
    Verified: proceed to CONDITION (ii).
    Not verified: execution halted. Revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced."
    Resume at CONDITION (i) after revision.

CONDITION (ii) -- FORMULA VERIFICATION:
  Requirement: `focus_adjusted_total` must appear as the left-hand side label of the arithmetic
  equation in Item C, in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Verification: confirm the intended Item C equation assigns `focus_adjusted_total` as the LHS label.
    Verified: both conditions are satisfied. Item B may be written.
    Not verified: execution halted. Revise the Item C equation plan to assign `focus_adjusted_total`
    as the LHS label. Resume at CONDITION (ii) after revision.

Both conditions verified. Item B is written.

**Item B -- Lens definition:**
- The focus dimension is defined in relation to this topic and the named incumbent as follows: [1-2 sentences]

**Item C -- Focus Economic Computation:**
The focus-adjusted do-nothing cost is computed prior to authoring the INERTIA table. The value focus_adjusted_total is applied in every Do-nothing cost cell and in the VERDICT "Not building this means:" line.

The formula is stated as a labeled arithmetic equation:

  base_cost (no-focus baseline): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost absent the focus lens; inferred from topic context]
  focus_adjustment (focus-type unit rate): [Concrete focus-specific liability carried by the named incumbent:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

All downstream Do-nothing cost cells employ focus_adjusted_total. Verification is performed by subtracting base_cost from focus_adjusted_total to recover focus_adjustment.

**Item D -- Structural violation rejection:**
No section heading corresponding to the active focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content is delivered through the rows of the Item A table, employing the economics established in Item C.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process currently employed by the team that this feature would replace. This designation must be established prior to any downstream computation; it constitutes the competitive reference for all sections.]
    Propagation requirement -- the named incumbent designation must appear in all three downstream anchor positions in the specified forms:
    (1) INERTIA section heading:
        Form: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header:
        Form: "[Named incumbent]" as the column header label
    (3) AMENDMENTS inertia-saved framing:
        Form: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: at least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
This section is completed prior to PM: BUDGET. The named incumbent designation from INFERENCE GATE is employed throughout. (The heading is renamed to correspond to anchor (1) above.)

[When focus is active: focus_adjusted_total from Step 0 Item C is applied. The INERTIA row of the Propagation Contract (Step 0 Item A) is delivered. The effect of the focus lens on the named incumbent's ongoing cost is stated.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- focus constraint effect from Propagation Contract included if active] |

Baseline: "Absent this feature, the team continues operating with [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
No traffic-light assessment may be written prior to completion of this section.

Available hours = [TEAM_SIZE] x [HRS_PER_SPRINT] x [SPRINT_COUNT] = [TOTAL_HOURS] hrs

| Component | Estimated Hours |
|-----------|----------------|
| [Name]    | [N]            |
| **Total** | **[SUM]**      |

  Estimated:  [SUM]
  Available:  [TOTAL_HOURS]

---

**STRATEGY: BUILD-VS-BUY**
This section is written prior to ARCHITECT. Procurement decisions (build / buy / use existing) for each component are committed before complexity ratings are assigned.
Where the focus dimension alters procurement logic (e.g., a compliance focus may favor a certified third party over an in-house build relative to the named incumbent), this is noted in the Rationale column.

All components to be assessed in ARCHITECT are listed below. At least half must carry an explicit Build / Buy / Use existing recommendation prior to proceeding to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- focus economic impact and named incumbent comparison included where it alters the recommendation] |

Proceed gate: all components listed above carry a Build / Buy / Use existing recommendation. All listed components are carried forward to ARCHITECT. No new components may be introduced in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. The procurement decisions established therein are applied in rating each listed component for complexity.
A Do-nothing cost column is required on every row -- focus_adjusted_total from Step 0 Item C is applied where applicable.

[When focus is active: the ARCHITECT row of the Propagation Contract (Step 0 Item A) is delivered. focus_adjusted_total from Item C may alter a component's rating -- a component may rate YELLOW or RED when the focus-adjusted do-nothing cost renders partial delivery economically unacceptable. Focus content is not reserved for a subsequent section.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this component beats or is bested by the named incumbent -- focus_adjusted_total referenced where it alters the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for each RED component:
- [Component]: [Basis on which the named incumbent prevails on focus-adjusted economics.]
  Lift condition: [The specific change required.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus.]

No RED components -- this statement is written verbatim if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent remains in place. focus_adjusted_total from Step 0 Item C is stated, along with the long-term competitive consequence of the incumbent's continuation.]"

[Authored only when score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope eliminates [RED ITEMS] and continues to outperform the named incumbent on focus-adjusted economics."

[Authored only when label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- resolution required or the named incumbent retains competitive advantage on focus-adjusted economics:
[The VERDICT row of the Propagation Contract (Step 0 Item A) is delivered here.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. All three items are required for each amendment entry. No item may be omitted.

[When focus is active: the AMENDMENTS row of the Propagation Contract (Step 0 Item A) is delivered. base_cost recapture and focus_adjustment eliminated are stated separately to maintain arithmetic transparency. Savings are framed as "recaptured from [Named incumbent]" per anchor (3) of INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [When focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

The above structure is repeated for each RED and YELLOW component.

---

**AMEND PROTOCOL**
This protocol is invoked exclusively upon receipt of an AMEND instruction. The full analysis is not re-executed. The four steps below are followed in sequence.

(1) Parsing the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identifying affected sections:
  For a focus shift: Step 0 (all four items) is re-executed with the new focus. The new Propagation Contract rows identify the affected sections. Whether focus_adjusted_total changes is noted.
  For a threshold adjustment: the components whose color classification changes under the new threshold are identified.
  The following declaration is made explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weaving affected sections only:
  Each affected section is rewritten with the amendment applied. Original section headings are used verbatim.
  For a focus shift: Step 0 Items A-D are updated first, in the following order:
    (a) Item A table is rewritten with the new focus constraint and new Stated Effect cells.
    (b) FORMULA CONTRACT RE-VERIFICATION:
        (i)  `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
             If not satisfied: the updated AMENDMENTS row is revised before proceeding.
        (ii) `focus_adjusted_total` will appear as the LHS label in the updated Item C.
             If not satisfied: the updated Item C equation label is revised before proceeding.
        Both conditions must be verified before updated Item B is written.
    (c) Updated Item B is written (lens definition for new focus).
    (d) Updated Item C is written (new focus economics formula).
    (e) Updated Item D is written (structural violation rejection for new focus dimension).
  The updated contract is then propagated through each affected section.
  Each rewritten section header is marked: "[AMENDED: reason]"
  Sections listed as unaffected are not rewritten, summarized, or referenced.

(4) VERDICT update:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  "Not building this means:" is updated with new focus_adjusted_total if Step 0 Item C formula changed.
  Prerequisites are updated if the RED component set changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-05 -- Role Sequence: C-02 FAIL + C-08 FAIL (PM: BUDGET Absent, STRATEGY Absent)

**Axis**: Single-axis. Role sequence -- PM: BUDGET block removed entirely (C-02 FAIL: full absence, not PARTIAL) AND STRATEGY: BUILD-VS-BUY section removed entirely (C-08 FAIL: 0% coverage). No focus. C-01 PASS (Feature, Team, Timeline all present). C-03 PASS (all three anchors). C-04 PASS (Do-nothing cost column on every ARCHITECT row). C-05 N/A. C-06 PASS. C-07 N/A. C-08 FAIL. C-10 N/A (STRATEGY absent, per C-35). C-11/12/14/15/16 N/A (STRATEGY absent). All focus aspirationals N/A.

**Hypothesis**: C-02 FAIL (essential) + C-08 FAIL (recommended). All other essential PASS. C-07 N/A, C-06 PASS. All STRATEGY-dependent aspirationals N/A (pass). Essential: 4/5 x 60 = 48. Recommended: C-06 PASS + C-07 N/A + C-08 FAIL = 2/3 x 30 = 20. Aspirational: 40/40 x 10 = 10. Composite: `48 + 20 + 10 = 78.000`. Not golden (essential FAIL gate). Confirms C-45 criterion-neutrality with a new essential+recommended pair: C-02+C-08 (vs. canonical C-03+C-08 in R13 V-05). Tests whether -22 pt cross-tier deduction holds regardless of which essential criterion fails.

**Changed from golden**: (1) PM: BUDGET block removed entirely -- no heading, no formula, no table, no output lines. (2) STRATEGY: BUILD-VS-BUY section removed entirely. (3) ARCHITECT heading: "Confirmation: STRATEGY: BUILD-VS-BUY is written above." replaced with direct complexity-rating instruction.

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
Complete this section before ARCHITECT: COMPLEXITY. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Rate each component for complexity against the named incumbent.
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
