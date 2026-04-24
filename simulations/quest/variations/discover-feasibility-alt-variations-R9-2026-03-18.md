Written to `simulations/quest/variations/discover-feasibility-alt-variations-R9-2026-03-18.md`.

---

## Round 9 Variations — discover-feasibility-alt

**Target axis**: Essential PARTIAL as a distinct golden-breaking mechanism + cross-criteria compounds with focus active.

### Design summary

| | Axis | Key failure | Composite | Golden? |
|---|---|---|---|---|
| **V-01** | Focus active golden (v7 baseline) | none | **100.000** | Yes |
| **V-02** | C-09 FAIL only: INERTIA-only Propagation Contract (v7 /19 cost check) | C-09 | **99.474** | Yes |
| **V-03** | C-04 PARTIAL: Do-nothing cost column optional; some rows blank | C-04 PARTIAL | **94.000** | **No** |
| **V-04** | C-06 + C-08 FAIL: amendment traceability + strategy coverage degraded | C-06 + C-08 | **80.000** | Yes (border) |
| **V-05** | C-04 PARTIAL + C-09 FAIL compound | C-04 PARTIAL + C-09 | **93.474** | **No** |

### Score derivations

- **V-01**: `(5/5 x 60) + (3/3 x 30) + (19/19 x 10) = 100.000`
- **V-02**: `(5/5 x 60) + (3/3 x 30) + (18/19 x 10) = 99.474` — C-09 FAIL
- **V-03**: `(4.5/5 x 60) + (3/3 x 30) + (19/19 x 10) = 54 + 30 + 10 = 94.000` — C-04 PARTIAL (NOT GOLDEN: PARTIAL on essential regardless of composite)
- **V-04**: `(5/5 x 60) + (1/3 x 30) + (19/19 x 10) = 60 + 10 + 10 = 80.000` — C-06 + C-08 FAIL (GOLDEN: border at exactly 80)
- **V-05**: `(4.5/5 x 60) + (3/3 x 30) + (18/19 x 10) = 54 + 30 + 9.474 = 93.474` — C-04 PARTIAL + C-09 FAIL (NOT GOLDEN)

### New patterns

1. **Essential PARTIAL is composite-independent**: V-03 at 94.000 and V-05 at 93.474 are both not golden despite composite >= 80. The PARTIAL rule operates outside the 80-threshold gate entirely.
2. **PARTIAL inverts the ranking**: V-03 (94.000) is not golden; V-04 (80.000) is. Composite ordering and golden ordering diverge — PARTIAL is categorically different from both essential FAIL (which drops composite) and aspirational FAIL (which never breaks golden alone).
3. **C-09 cost confirmed at 0.526 pts** under v7 /19 denominator (was 0.714 at R8's /14). C-07 vs C-09 ratio is now 19:1, confirming C-24.
4. **Two recommended FAILs = golden border**: C-06 + C-08 compound costs exactly 20 pts, landing at 80.000 minimum golden. A third recommended FAIL would drop to 70.000.
5. **C-06/C-08 orthogonal to C-07/C-09**: the STRATEGY/AMENDMENTS degradation axis (V-04) has zero interaction with focus weaving or propagation — independently satisfiable pairs.
his at the border; three recommended FAILs (C-06 + C-07 + C-08) would give 70.000 (not golden)
4. **PARTIAL rule overrides composite**: V-05 scores 93.474 composite -- higher than R8/V-05 (89.286) -- yet is not golden, while R8/V-05 was golden; the PARTIAL mechanism is composite-independent
5. **C-04 PARTIAL diagnosis**: surface 2 (Do-nothing cost column on every row) is the targeted failure; surfaces 1, 3, and 4 remain intact in both V-03 and V-05

---

## V-01 -- Focus Active Golden Baseline (v7)

**Axis**: Reference baseline. Full golden template with focus active. All five essential PASS, all three recommended PASS, all 19 aspirational PASS or N/A. Propagation Contract complete (all four rows), focus_adjusted_total woven through INERTIA / ARCHITECT / VERDICT / AMENDMENTS, Item D failure-mode rejection present, C-17 static iff-guard present, C-18 three independent AMENDMENTS sub-lines present. Scored under v7 -- establishes 100.000 under /19 aspirational denominator; C-23-C-27 all PASS as structural formula properties.

**Hypothesis**: C-01-C-05 PASS, C-06-C-08 PASS, C-09 PASS (4-row Propagation Contract propagates focus to 4 sections), C-10-C-18 PASS, C-19-C-27 PASS, C-13 N/A. Composite: (5/5 x 60) + (3/3 x 30) + (19/19 x 10) = 100.000. Golden.

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

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component for complexity using these procurement decisions; no new components may be added in ARCHITECT without a corresponding STRATEGY entry.

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

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

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

## V-02 -- C-09 FAIL Only: Focus Woven into INERTIA Only (v7 Denominator Check)

**Axis**: Propagation Contract reduced to INERTIA row only. Focus is woven into the analysis (C-05 PASS: content integrated, not appended) and demonstrably changes the INERTIA economics (C-07 PASS: focus_adjusted_total appears in INERTIA, changing the incumbent's cost). But the ARCHITECT, VERDICT, and AMENDMENTS rows are absent from the contract, and the downstream section instructions do not direct focus propagation -- focus stays in INERTIA only (1 section). C-09 FAIL: 1 < 2 required sections. Scored under v7 to confirm C-09 cost at /19 (0.526 pts vs 0.714 pts at R8's /14 denominator).

**Hypothesis**: C-09 FAIL (aspirational only). C-07 PASS (focus_adjusted_total changes INERTIA economics). All essential PASS. Recommended 3/3 PASS. Aspirational 18/19: C-09 FAIL=0, C-13 N/A=1, C-23-C-27 PASS. Composite: (5/5 x 60) + (3/3 x 30) + (18/19 x 10) = 60 + 30 + 9.474 = 99.474. Golden.

**Changed from V-01**: Step 0 Item A reduced to INERTIA row only; Item A contract check note updated; "[If focus active: deliver on the ARCHITECT row...]" directives removed from ARCHITECT, VERDICT, and AMENDMENTS sections; Do-nothing cost cells use base_cost (not focus_adjusted_total) in ARCHITECT since the contract has no ARCHITECT row.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent in the INERTIA section. Name the focus-specific cost the incumbent carries and compute the focus-adjusted do-nothing cost in Step 0.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. Focus content belongs in INERTIA where the competitive cost is defined.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Focus Contract for INERTIA before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- INERTIA Focus Contract:**
Name the primary constraint this focus introduces and how it affects the named incumbent's cost structure in the INERTIA section.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in the Stated Effect cell in the
  Item A table above.
  Check: does the Effect cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the INERTIA row in Item A to include the phrase
    "`focus_adjusted_total` in the named incumbent's cost-per-sprint." Return here after revising.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- specifically in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan so the equation label is `focus_adjusted_total`.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent in INERTIA? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost for use in INERTIA.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Use focus_adjusted_total in the INERTIA table and Baseline sentence.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required -- this exact name appears in at least two of these three downstream anchors:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS framing: "recaptured from [Named incumbent]: N hrs/sprint"

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
(Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. State how the focus lens changes the named incumbent's ongoing cost in INERTIA.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint from Step 0 Item A] |

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
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row.

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [base_cost -- no focus adjustment in ARCHITECT] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [base_cost per sprint.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at base_cost per sprint and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus or threshold]
  To: [new focus or threshold]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all items) with the new focus.
  For a threshold adjustment: identify which components change color.
  Declare: "Affected sections: [...]. Unaffected sections: [...]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections. Mark each rewritten section header: "[AMENDED: reason]"

(4) Update VERDICT: New score, delta, label change if any.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-03 -- C-04 PARTIAL: Do-Nothing Cost Column Optional

**Axis**: The ARCHITECT table Do-nothing cost column is downgraded from mandatory to conditional ("include where cost is estimable and material"). The RED Blockers do-nothing cost sub-field is also removed. This makes the column present on some rows but absent on others -- C-04 surface 2 PARTIAL. Surfaces 1, 3, and 4 remain intact (INERTIA baseline sentence, VERDICT "Not building this means:", AMENDMENTS "Inertia saved:"). The focus Propagation Contract is complete (all four rows), so C-05 PASS, C-07 PASS, C-09 PASS.

**Hypothesis**: C-04 PARTIAL (essential; Do-nothing cost column present but incomplete). All other essential PASS. Recommended 3/3 PASS (C-06, C-07, C-08 all pass -- AMENDMENTS still has color/delta; STRATEGY has 50%+ coverage; focus woven and changes analysis). Aspirational 19/19 PASS. Composite: (4.5/5 x 60) + (3/3 x 30) + (19/19 x 10) = 54 + 30 + 10 = 94.000. NOT GOLDEN: PARTIAL on essential criterion regardless of composite.

**Changed from V-01**: ARCHITECT table header changes "Do-nothing cost column required on every row" to "Do-nothing cost column (include where cost is estimable and material -- leave blank if unknown)"; cell instruction changed to "[N hrs/sprint if estimable; leave blank if not yet quantified]"; RED Blockers Do-nothing cost sub-field removed.

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
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
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
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in the INERTIA section and in VERDICT's "Not building this means:" line.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS. All focus content flows through the rows in Item A's table.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required -- this exact name appears in at least two of these three downstream anchors:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS framing: "recaptured from [Named incumbent]: N hrs/sprint"

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
(Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect if active] |

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
If focus changes procurement logic, state it in Rationale.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column (include where cost is estimable and material -- leave blank if not yet quantified).

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (if estimable) |
|-----------|----------------------|------------|----------------------------------|-------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [N hrs/sprint if estimable; leave blank if not yet quantified] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated. Frame savings as "recaptured from [Named incumbent]."]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus or threshold]
  To: [new focus or threshold]

(2) Identify affected sections. Declare affected and unaffected sections explicitly.

(3) Re-weave only the affected sections. Mark each rewritten section header: "[AMENDED: reason]"

(4) Update VERDICT: New score, delta, label change if any.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- C-06 + C-08 FAIL: Amendment Traceability + Strategy Coverage Degraded

**Axis**: STRATEGY section is simplified to free-form procurement notes without a mandatory 50%+ Build/Buy/Use coverage requirement (C-08 FAIL). AMENDMENTS section drops the color transition and score-delta obligation, using a generic action format only (C-06 FAIL). The full Propagation Contract is intact (all four rows), focus_adjusted_total woven through all sections (C-05 PASS, C-07 PASS, C-09 PASS). C-18 PASS: AMENDMENTS still has three sub-lines but the second sub-line (color-transition) is absent from the template, making C-18 FAIL would require re-evaluation -- actually, since C-06 FAIL means the color-transition line is absent, C-18 tests whether the template independently *authors* the three sub-lines; if the template drops the color-transition sub-line, C-18 also FAIL. Let me recalculate.

Wait -- C-18 FAIL adds another aspirational failure: (5/5 x 60) + (1/3 x 30) + (18/19 x 10) = 60 + 10 + 9.474 = 79.474. That is below 80 -- NOT GOLDEN. That changes the design.

To keep V-04 as the golden-border case, I need C-06 FAIL without C-18 FAIL. C-06 and C-18 are independent: C-06 tests output content (amendments naming component + color transition + delta), C-18 tests template authoring (three independently-authored sub-lines in the template). A template can fail C-06 (output lacks color transition) while passing C-18 (template does have three sub-line slots but the color-transition instruction is ambiguous enough that the model omits it). Conversely, a merged template instruction can produce C-06-passing output while C-18 fails.

For V-04: design the AMENDMENTS template to have three sub-line slots but make the color-transition slot vague ("note any rating changes"), not mandate the specific "[Component] from [COLOR] to [COLOR], raising score by [N] pts" format. The template has the slot (C-18 PASS: three sub-line slots present) but the slot instruction is underspecified enough that the model produces output without an explicit color transition or delta (C-06 FAIL: color transition absent or delta missing from output).

Revised V-04 design -- confirmed:
- C-06 FAIL: AMENDMENTS color-transition line underspecified; output lacks "[Component] from [COLOR] to [COLOR], raising score by [N] pts"
- C-08 FAIL: STRATEGY lacks 50%+ coverage mandate
- C-07 PASS: full Propagation Contract, focus_adjusted_total in all sections
- C-18 PASS: AMENDMENTS template has three sub-line slots (action + rating note + inertia saved); template authoring present, just underspecified
- Score: (5/5 x 60) + (1/3 x 30) + (19/19 x 10) = 60 + 10 + 10 = 80.000. GOLDEN (border).

**Hypothesis**: C-06 FAIL (recommended), C-08 FAIL (recommended). All essential PASS. C-07 PASS (recommended; focus active and changes analysis). Aspirational 19/19 PASS: C-09 PASS (4-row Propagation Contract, focus in 4 sections), C-18 PASS (three sub-line slots present in AMENDMENTS template), all structural criteria PASS. Composite: (5/5 x 60) + (1/3 x 30) + (19/19 x 10) = 60 + 10 + 10 = 80.000. GOLDEN (border: exactly 80.000).

**Changed from V-01**: STRATEGY section drops mandatory Build/Buy/Use column and 50%+ proceed gate (replaced with free-form procurement notes); AMENDMENTS color-transition sub-line becomes vague "note rating change" instruction without mandating the "[Component] from [COLOR] to [COLOR], raising score by [N] pts" format.

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
Name the primary constraint this focus introduces. Complete the full table before writing Item B or Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
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
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- specifically in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan now so the equation label is `focus_adjusted_total`.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS. All focus content flows through the rows in Item A's table.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required -- this exact name appears in at least two of these three downstream anchors:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS framing: "recaptured from [Named incumbent]: N hrs/sprint"

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
(Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect if active] |

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
Write this before ARCHITECT. Note the likely procurement approach for each major component.
If focus changes how you'd approach procurement vs. the named incumbent, note it in Rationale.

| Component | Procurement Notes | Why |
|-----------|-------------------|-----|
| [Name]    | [Build / Buy / Use existing or approach notes] | [Rationale] |

Proceeding to ARCHITECT with the components listed above.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement notes, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total from Step 0 Item C where it changes the rating] | [focus_adjusted_total if active; base_cost if no focus] |

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
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Frame savings as "recaptured from [Named incumbent]."]

1. [Action for COMPONENT: the specific next step to address this component.]
   Note any rating change this action enables.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus or threshold]
  To: [new focus or threshold]

(2) Identify affected sections. Declare affected and unaffected sections explicitly. Unaffected sections will not be rewritten.

(3) Re-weave only the affected sections. Mark each rewritten section header: "[AMENDED: reason]"

(4) Update VERDICT: New score, delta, label change if any.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-05 -- C-04 PARTIAL + C-09 FAIL Compound

**Axis**: Combines V-02 modification (Propagation Contract INERTIA-only -> C-09 FAIL) with V-03 modification (Do-nothing cost column optional -> C-04 PARTIAL). C-04 PARTIAL (essential): Do-nothing cost column present but incomplete. C-09 FAIL (aspirational): focus woven into INERTIA only (1 section). C-07 PASS: focus_adjusted_total present in INERTIA, demonstrably changes INERTIA economics. C-05 PASS: focus woven into INERTIA section (not appended).

**Hypothesis**: C-04 PARTIAL (essential), C-09 FAIL (aspirational). All other essential PASS. Recommended 3/3 PASS (C-07 PASS: focus changes INERTIA analysis; C-06 PASS: AMENDMENTS color/delta present; C-08 PASS: STRATEGY 50%+ coverage present). Aspirational: 18/19 (C-09 FAIL=0, C-13 N/A=1, all others PASS). Composite: (4.5/5 x 60) + (3/3 x 30) + (18/19 x 10) = 54 + 30 + 9.474 = 93.474. NOT GOLDEN: PARTIAL on essential criterion. Confirms PARTIAL rule dominates: 93.474 composite is higher than any non-golden variation in prior rounds except V-03 in this round (94.000), yet fails golden while R8/V-05 (89.286, no PARTIAL) was golden.

**Changed from V-01**: V-02's INERTIA-only Propagation Contract (removes ARCHITECT/VERDICT/AMENDMENTS rows from Step 0 Item A; removes downstream focus directives from those sections) + V-03's optional Do-nothing cost column in ARCHITECT.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic "workaround."

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent in the INERTIA section. Name the focus-specific cost the incumbent carries and compute the focus-adjusted do-nothing cost in Step 0.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. Focus content belongs in INERTIA where the competitive cost is defined.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build your Focus Contract for INERTIA before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- INERTIA Focus Contract:**
Name the primary constraint this focus introduces and how it affects the named incumbent's cost structure in the INERTIA section.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in the Stated Effect cell in the
  Item A table above.
  Check: does the Effect cell contain the token `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the INERTIA row.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` as the LHS label in Item C equation.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust Item C plan.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent in INERTIA? [1-2 sentences]

**Item C -- Focus Economics:**
  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Use focus_adjusted_total in the INERTIA table and Baseline sentence.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required -- this exact name appears in at least two of these three downstream anchors:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS framing: "recaptured from [Named incumbent]: N hrs/sprint"

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
(Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint from Step 0 Item A] |

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
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column (include where cost is estimable and material -- leave blank if not yet quantified).

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (if estimable) |
|-----------|----------------------|------------|----------------------------------|-------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [N hrs/sprint if estimable; leave blank if not yet quantified] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at base_cost per sprint. State long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis.

(1) Parse the focus shift or threshold change.
(2) Identify affected sections. Declare affected and unaffected sections explicitly.
(3) Re-weave only the affected sections. Mark each rewritten section header: "[AMENDED: reason]"
(4) Update VERDICT: New score, delta, label change if any.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

### Ranking

| Rank | Variation | Composite | Golden? | Failures |
|------|-----------|-----------|---------|---------|
| 1 | V-01 | 100.000 | Yes | none |
| 2 | V-02 | 99.474 | Yes | C-09 (asp) |
| 3 | V-04 | 80.000 | Yes | C-06 (rec) + C-08 (rec) |
| 4 | V-03 | 94.000 | **No** | C-04 PARTIAL (ess) |
| 5 | V-05 | 93.474 | **No** | C-04 PARTIAL (ess) + C-09 (asp) |

Note: ranking is by golden status first (golden > not-golden), then composite within each group.

Gap analysis:
- V-01 -> V-02: -0.526 (C-09 alone at /19; was -0.714 at R8's /14 denominator -- denominator effect confirmed)
- V-01 -> V-04: -20.000 (C-06 + C-08 together; two recommended FAILs = exactly 20 pts)
- V-03 -> V-05: -0.526 (C-09 added on top of PARTIAL; additive, no escalation)
- V-03 -> V-04: V-03 is not golden at 94.000; V-04 is golden at 80.000 -- the PARTIAL rule inverts the composite-based ranking entirely

---

### Excellence signals (V-01)

1. **Propagation Contract as the four-section weave mechanism**: the mandatory four-row table (INERTIA / ARCHITECT / VERDICT / AMENDMENTS) is the structural guarantee that C-09 passes by-construction -- removing or reducing rows directly causes C-09 FAIL (V-02, V-05). The contract forces section-count compliance before any section is written.

2. **FORMULA CONTRACT CHECK as C-07 by-construction**: the two-condition gate (TABLE SIDE: focus_adjusted_total in Item A; FORMULA SIDE: focus_adjusted_total as LHS in Item C) forces the economics variable to be wired before INERTIA or ARCHITECT are written. Without this gate, focus_adjusted_total could be introduced or forgotten mid-template, leaving C-07 dependent on model behavior rather than structural enforcement.

3. **Do-nothing cost mandate as C-04 surface 2 guarantee**: the "Do-nothing cost column required on every row" instruction is the sole structural guarantee for C-04 surface 2. Making it optional (V-03, V-05) is sufficient to cause PARTIAL; the column may appear on some rows but not others when the instruction becomes conditional.

4. **STRATEGY proceed gate as C-08 by-construction**: the explicit "At least half must carry an explicit Build / Buy / Use existing recommendation" + "Proceed gate" forces 50%+ coverage before ARCHITECT begins. Removing the mandate (V-04) degrades C-08 without affecting any focus criterion -- C-06/C-08 and C-07/C-09 are orthogonal axis pairs.

5. **AMENDMENTS three-line mandate as the C-06/C-18 joint guarantee**: "Include all three lines for every amendment -- do not drop any line" forces the color-transition sub-line (satisfying C-06: output carries transition + delta) and encodes three independent sub-line slots (satisfying C-18: template independently authors three obligations). Making the color-transition slot vague (V-04) decouples C-06 from C-18: C-18 can pass while C-06 fails.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-04 PARTIAL breaks golden at high composite: 94.000 (V-03) and 93.474 (V-05) are NOT golden despite composite >= 80 -- PARTIAL on essential is a composite-independent golden-breaker; contrast with essential FAIL which drops composite below 80 (V-04 R8: 77.474) and aspirational FAIL which never breaks golden (V-02: 99.474)", "C-09 FAIL cost confirmed at 0.526 pts under v7 /19 denominator (vs 0.714 pts at R8 /14 denominator) -- C-07 vs C-09 tier ratio is now 19:1; the ratio grows linearly with denominator expansion confirming C-24", "C-06 + C-08 compound at golden border: two recommended FAILs cost exactly 20 pts; composite 80.000 = golden minimum; a third recommended FAIL (C-07 FAIL, focus active) would drop to 70.000 -- not golden -- confirming C-21 aspirational ceiling is essential-isolated", "PARTIAL rule inverts composite ranking: V-03 (94.000, PARTIAL essential) is not golden while V-04 (80.000, no PARTIAL) is golden -- PARTIAL essential overrides composite threshold entirely, making PARTIAL a categorically different failure from both essential FAIL and aspirational FAIL", "C-06/C-08 are orthogonal to C-07/C-09: degrading STRATEGY coverage and AMENDMENTS traceability (V-04) has zero interaction with focus weaving or propagation -- the two axis pairs are independently satisfiable"]}
```
