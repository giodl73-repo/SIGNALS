Written to `simulations/quest/variations/discover-feasibility-alt-variations-R7-2026-03-18.md`.

---

## Round 7 Variations -- discover-feasibility-alt

**Target axis**: C-17 and C-18 (the two new aspirational criteria introduced in v5).

**Design summary**:

| | Axis | Key criterion | Composite | Golden? |
|---|---|---|---|---|
| **V-01** | Golden baseline (R6/V-01 under v5) | all PASS | **100.000** | Yes |
| **V-02** | C-17 FAIL only -- inference-only guard | C-17 FAIL | **99.000** | Yes |
| **V-03** | C-17 FAIL + C-02 FAIL cascade -- guard removed | C-17 FAIL + C-02 FAIL | **87.000** | **No** |
| **V-04** | C-18 FAIL only -- AMENDMENTS merged instruction | C-18 FAIL | **99.000** | Yes |
| **V-05** | Compound -- C-17 FAIL + C-18 FAIL | both aspirational | **98.000** | Yes |

**Variation axes used**:
- **V-02** (C-17): replaces the static `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` guard with an inference-only instruction ("include if analysis requires them"). Template mechanism removed; model must infer the condition.
- **V-03** (C-17 cascade): removes the guard entirely -- prerequisites block renders unconditionally, triggering C-02 FAIL via cascade.
- **V-04** (C-18): merges the three independently-authored AMENDMENTS sub-lines into one combined instruction. C-04 and C-06 output checks still pass; C-18 template-authoring check fails.
- **V-05**: combines V-02 and V-04 degradations.

**Key findings to be scored in R7**:
1. C-17 and C-18 each cost exactly 1 pt from the aspirational /10 block
2. C-17 FAIL alone is golden-compatible (99); guard removal causes a 13x cascade to 87
3. C-18 FAIL alone is golden-compatible (99); merged instruction still satisfies C-04 and C-06 output checks
4. Compound C-17+C-18 = 98, still well above the golden threshold
5. Aspirational-only failure ceiling: even all 10 aspirational fails = composite 90, golden holds
sfies C-04 (content present) and C-06 (component named, color transition, score delta mentioned). C-18 tests whether the template independently authors all three sub-lines -- it does not, so C-18 FAIL at aspirational. Essential and recommended unchanged.
- **V-05 compound is still golden**: both C-17 and C-18 fail together, costing 2 pts. Composite 98.000 is well above the 80 threshold. Confirms that aspirational-tier failures do not accumulate to a golden-breaking deficit without essential involvement.

---

### Score derivations

**V-01**:
```
Essential:    5/5   * 60 = 60     (C-05 N/A=1)
Recommended:  3/3   * 30 = 30     (C-07 N/A=1)
Aspirational: 10/10 * 10 = 10     (C-09 N/A=1, C-13 N/A=1, C-17 PASS, C-18 PASS)
Composite: 100.000
```

**V-02**:
```
Essential:    5/5   * 60 = 60     (C-05 N/A=1)
Recommended:  3/3   * 30 = 30     (C-07 N/A=1)
Aspirational: 9/10  * 10 =  9     (C-17 FAIL=0; all others PASS or N/A=1)
Composite: 99.000
```

**V-03**:
```
Essential:    4/5   * 60 = 48     (C-02 FAIL=0)
Recommended:  3/3   * 30 = 30
Aspirational: 9/10  * 10 =  9     (C-17 FAIL=0; all others PASS or N/A=1)
Composite: 87.000
```

**V-04**:
```
Essential:    5/5   * 60 = 60     (C-05 N/A=1)
Recommended:  3/3   * 30 = 30     (C-07 N/A=1)
Aspirational: 9/10  * 10 =  9     (C-18 FAIL=0; all others PASS or N/A=1)
Composite: 99.000
```

**V-05**:
```
Essential:    5/5   * 60 = 60     (C-05 N/A=1)
Recommended:  3/3   * 30 = 30     (C-07 N/A=1)
Aspirational: 8/10  * 10 =  8     (C-17 FAIL=0, C-18 FAIL=0; all others PASS or N/A=1)
Composite: 98.000
```

### Key discriminators

- **V-01 vs V-02**: C-17 cost in isolation. Inference-only guard = -1 pt (99.000), golden-compatible. The guarantee shifts from structural to probabilistic without affecting composite enough to break golden.
- **V-02 vs V-03**: cascade cost. V-02 has inference-based guard (C-17 FAIL, C-02 probabilistic PASS) = 99.000. V-03 removes guard entirely (C-17 FAIL, C-02 definite FAIL) = 87.000. Cascade adds -12 pts essential. V-03 is the only non-golden variation this round.
- **V-01 vs V-04**: C-18 cost in isolation. Merged sub-lines = -1 pt (99.000), golden-compatible. C-04 and C-06 output checks still pass because content is present; only the template-authoring check fails.
- **V-04 vs V-02**: same composite (99.000), different mechanism. V-02 fails a conditional-rendering mechanism (C-17). V-04 fails an orthogonality-authoring mechanism (C-18). Both cost 1 pt, both golden-compatible.
- **V-05 vs V-04**: adding C-17 FAIL on top of C-18 FAIL costs 1 additional pt (98.000 vs 99.000). Still golden. Compound aspirational failures do not accumulate to a golden-breaking deficit.

---

## V-01 -- Golden Baseline (R6/V-01 carried forward, scored under v5)

**Axis**: Reference baseline. Full golden template, no focus active. C-17 PASS (explicit iff-guard present in VERDICT as static body text), C-18 PASS (three independently-authored sub-lines in AMENDMENTS). Scored under v5 rubric for the first time -- establishes 100.000 under /10 aspirational denominator.

**Hypothesis**: All 5 essential PASS, all 3 recommended PASS, all 10 aspirational PASS or N/A. C-05/C-07/C-09 N/A=1 (no focus), C-13 N/A=1 (no preamble ordering directive), C-17 PASS (static iff-guard authored in VERDICT body), C-18 PASS (three distinct sub-line instructions in AMENDMENTS). Composite: (5/5 * 60) + (3/3 * 30) + (10/10 * 10) = 100.000. Golden.

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

## V-02 -- C-17 FAIL Only: Inference-Only Prerequisite Guard

**Axis**: The explicit iff-guard in VERDICT is replaced with an inference-based instruction. The static body text `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` is replaced by: `Prerequisites -- include these if the analysis requires them (omit when not applicable):`. The model must infer the condition; no structural guard prevents unconditional rendering. C-17 FAIL (no static iff-guard text); C-02 probabilistic PASS (model likely infers correctly -- the guarantee is probabilistic, not structural).

**Hypothesis**: C-17 FAIL (no static iff-guard authored in template body). C-02 PASS (probabilistic -- model infers suppression from scoring context). Essential: 5/5 (C-02 probabilistic PASS preserved). Recommended: 3/3. Aspirational: 9/10 (C-17 FAIL=0). Composite: (5/5 * 60) + (3/3 * 30) + (9/10 * 10) = 60 + 30 + 9 = 99.000. Golden. Confirms: C-17 FAIL is aspirational-tier only (1 pt cost), golden-compatible; C-17/C-02 independence holds -- a template can fail C-17 while C-02 passes by model inference.

**Changed section from V-01: VERDICT -- `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` replaced with inference-only instruction.**

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
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries]
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
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS inertia-saved framing: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total or base_cost] | [Risk tied to incumbent] |

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

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component for complexity using these procurement decisions; no new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [focus_adjusted_total or base_cost] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent."

Prerequisites -- include these if the analysis requires them (omit when not applicable):
[Deliver on the VERDICT row of your Propagation Contract if focus is active.]
1. [Prerequisite, if applicable]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated. Frame savings as "recaptured from [Named incumbent]".]

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
  For a focus shift: re-run Step 0 (all four items) with the new focus. Identify which sections are affected. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify which components change color. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS for each changed component.
  Then declare: "Affected sections: [...]. Unaffected sections: [...]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections. Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any unaffected section.

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" and prerequisites if changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-03 -- C-17 FAIL + C-02 FAIL Cascade: Guard Removed, Prerequisites Unconditional

**Axis**: The VERDICT prerequisites iff-guard is removed entirely -- not replaced, simply absent. The prerequisites block renders for every output regardless of label or component colors. C-17 FAIL (no static body text guards the block); C-02 FAIL (prerequisites present even for FEASIBLE outputs and even when no RED components exist). This is the canonical cascade case predicted by the v5 rubric changelog.

**Hypothesis**: C-17 FAIL (guard absent from template body) cascades to C-02 FAIL (unconditional rendering makes the iff condition structurally unenforced). Essential: 4/5 (C-02 FAIL=0). Recommended: 3/3. Aspirational: 9/10 (C-17 FAIL=0). Composite: (4/5 * 60) + (3/3 * 30) + (9/10 * 10) = 48 + 30 + 9 = 87.000. NOT Golden. Confirms the v5 floor calculation for the V-03 pattern: 87.000. Confirms V-02/V-03 asymmetry: inference-only guard = 99.000; guard removed = 87.000. Cascade multiplier: 1 aspirational pt becomes 13 pts total when the unconditional rendering triggers C-02 FAIL.

**Changed section from V-01: VERDICT -- iff-guard removed entirely, prerequisites block renders unconditionally.**

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
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row. Return here after revising.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the LHS label of the arithmetic equation in Item C.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan. Return here after adjusting.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table.

  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required -- this exact name appears in all three downstream anchors:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS inertia-saved framing: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total or base_cost] | [Risk tied to incumbent] |

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
Write this before ARCHITECT. Procurement decisions for each component must be committed before complexity ratings are assigned.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component for complexity using these procurement decisions; no new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [focus_adjusted_total or base_cost] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract if focus is active.]
1. [Prerequisite -- list any open RED component prerequisites here, or write "None" if no RED components exist.]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated. Frame savings as "recaptured from [Named incumbent]".]

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

(2) Identify affected sections. Declare: "Affected sections: [...]. Unaffected sections: [...]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections. Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any unaffected section.

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" and prerequisites if changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- C-18 FAIL Only: AMENDMENTS Merged to Single Combined Instruction

**Axis**: The three independently-authored sub-lines in AMENDMENTS are merged into a single combined instruction. Instead of three named obligations (action line, color-transition line, "Inertia saved:" line as separate instructions), the template issues one compound instruction mentioning all three elements in one sentence. C-18 FAIL (template does not independently author all three sub-lines); C-04 PASS (inertia surface content still mentioned in the merged instruction -- surface 4 is present); C-06 PASS (component named, color transition and score-delta mentioned, even if merged).

**Hypothesis**: C-18 FAIL (merged instruction -- not three independently-removable sub-lines as separate template obligations). C-04 PASS (inertia content present in merged instruction). C-06 PASS (component, color transition, score-delta all referenced). Essential: 5/5. Recommended: 3/3. Aspirational: 9/10 (C-18 FAIL=0). Composite: (5/5 * 60) + (3/3 * 30) + (9/10 * 10) = 60 + 30 + 9 = 99.000. Golden. Confirms: C-18 FAIL is aspirational-tier only (1 pt), golden-compatible; merged instruction satisfies output checks (C-04, C-06) while failing the template-authoring check (C-18). Three surfaces -- output presence vs. template structure -- are independently testable.

**Changed section from V-01: AMENDMENTS block -- three sub-lines merged into a single combined instruction per amendment entry. AMEND PROTOCOL step (3) also reflects merged instruction.**

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
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
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
    Not satisfied: STOP. Adjust your Item C plan now. Return here after adjusting.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries]
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
    Propagation required -- this exact name appears in all three downstream anchors in these forms:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS inertia-saved framing: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total or base_cost] | [Risk tied to incumbent] |

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
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component for complexity using these procurement decisions; no new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. focus_adjusted_total may change a component's rating. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [focus_adjusted_total or base_cost] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. For each amendment, write a single entry that: names the specific component and the action to take, states the color transition from [COLOR] to [COLOR] with a score-delta estimate of approximately [N] pts, and notes the inertia savings recaptured from [Named incumbent] ([N hrs/sprint or $N/sprint]; if focus active, add focus_adjustment eliminated and total inertia saved = base_cost + focus_adjustment per sprint).

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated in the entry. Frame savings as "recaptured from [Named incumbent]".]

1. [COMPONENT (RED/YELLOW): action taken, moves from [COLOR] to [COLOR] raising score ~[N] pts, inertia saved: recaptured from [Named incumbent]: [N hrs/sprint].]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. Note whether focus_adjusted_total changes.
  For a threshold adjustment: identify changed components. Affected sections = ARCHITECT + RED Blockers + VERDICT + AMENDMENTS.
  Declare: "Affected sections: [...]. Unaffected sections: [...]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections. Mark each rewritten section header with: "[AMENDED: reason]"
  For each amendment entry: name the component, state the action, color transition, score delta, and inertia savings in one entry.
  Do not rewrite, summarize, or reference any unaffected section.

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" and prerequisites if changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-05 -- Compound: C-17 FAIL + C-18 FAIL (Both Aspirational)

**Axis**: V-02 and V-04 degradations combined. VERDICT uses an inference-only prerequisite guard (C-17 FAIL); AMENDMENTS uses a single combined instruction per entry (C-18 FAIL). All essential and recommended criteria unchanged. C-02 probabilistic PASS; C-04 PASS (inertia content in merged instruction); C-06 PASS (component, color transition, score-delta mentioned).

**Hypothesis**: C-17 FAIL + C-18 FAIL (both aspirational). C-02 PASS (inference-based guard -- probabilistic). C-04 PASS. C-06 PASS. Essential: 5/5. Recommended: 3/3. Aspirational: 8/10 (C-17 FAIL=0, C-18 FAIL=0). Composite: (5/5 * 60) + (3/3 * 30) + (8/10 * 10) = 60 + 30 + 8 = 98.000. Golden. Confirms: compound aspirational failure (2 pts) is golden-compatible. Aspirational-only failure ceiling established: even 10/10 aspirational fail = composite 90.000, golden threshold holds.

**Changed sections from V-01: VERDICT (inference-only guard from V-02) + AMENDMENTS (merged combined instruction from V-04).**

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
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when named incumbent is replaced] |

FORMULA CONTRACT CHECK -- two independent conditions, each verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: STOP. Revise the AMENDMENTS row. Return here after revising.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the LHS label in Item C.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: STOP. Adjust your Item C plan. Return here after adjusting.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table.

  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [N engineers -- inferred from: SOURCE]
  Timeline:        [N sprints / N weeks -- inferred from: SOURCE]
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
    Propagation required -- this exact name appears in all three downstream anchors:
    (1) INERTIA section heading: "INERTIA: STATUS QUO -- The [Named incumbent] the Feature Must Beat"
    (2) INERTIA table first column header: "[Named incumbent]"
    (3) AMENDMENTS inertia-saved framing: "recaptured from [Named incumbent]: N hrs/sprint"
    Minimum count: At least two of these three anchors are required; all three are recommended.

---

**INERTIA: STATUS QUO -- The Named Incumbent the Feature Must Beat**
Fill this before PM: BUDGET. Name the incumbent from INFERENCE GATE throughout this section.

[If focus active: use focus_adjusted_total from Step 0 Item C.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total or base_cost] | [Risk tied to incumbent] |

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
Write this before ARCHITECT. Procurement decisions for each component must be committed before complexity ratings are assigned.

List all components you intend to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. ARCHITECT will rate each component for complexity using these procurement decisions; no new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [focus_adjusted_total or base_cost] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [focus_adjusted_total from Step 0 Item C.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent on focus-adjusted economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total and the long-term competitive consequence.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

Prerequisites -- include these if the analysis requires them (omit when not applicable):
[Deliver on the VERDICT row of your Propagation Contract if focus is active.]
1. [Prerequisite, if applicable]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. For each amendment, write a single entry that: names the specific component and the action to take, states the color transition from [COLOR] to [COLOR] with a score-delta estimate of approximately [N] pts, and notes the inertia savings recaptured from [Named incumbent] ([N hrs/sprint or $N/sprint]; if focus active, add focus_adjustment eliminated and total inertia saved = base_cost + focus_adjustment per sprint).

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated. Frame savings as "recaptured from [Named incumbent]".]

1. [COMPONENT (RED/YELLOW): action taken, moves from [COLOR] to [COLOR] raising score ~[N] pts, inertia saved: recaptured from [Named incumbent]: [N hrs/sprint].]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections. Declare: "Affected sections: [...]. Unaffected sections: [...]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections. Mark each rewritten section header with: "[AMENDED: reason]"
  For each amendment entry: name the component, state the action, color transition, score delta, and inertia savings in one entry.
  Do not rewrite, summarize, or reference any unaffected section.

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" and prerequisites if changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

### Excellence Signals (from V-01)

**V-01 (100.000, Golden)**:
1. **Explicit iff-guard as static body text** -- `[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]` is static body text that structurally prevents unconditional rendering. C-17 PASS by construction, not by model inference.
2. **Three independently-authored AMENDMENTS sub-lines** -- action line, color-transition line ("This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts."), and "Inertia saved:" line are each named as separate obligations on separate lines. Removing any sub-line fires a different criterion: sub-line 3 absent = C-04 PARTIAL; sub-line 2 absent = C-06 FAIL. C-18 PASS confirms the template authors all three independently.
3. **Cascade-safe guarantee chain** -- body enforces STRATEGY-before-ARCHITECT, proceed gate names components before ARCHITECT evaluates them, ARCHITECT opens with explicit back-reference to STRATEGY. C-10/C-11/C-12/C-14/C-15/C-16 all PASS by structural construction.

**V-04 (99.000, Golden despite C-18 FAIL)**:
1. **C-18 FAIL is aspirational-tier and golden-compatible** -- merged AMENDMENTS instruction costs 1 pt but C-04 and C-06 output checks still pass. The template-authoring check (C-18) is stricter than the output checks (C-04, C-06): output can satisfy both from a merged instruction, but the template fails C-18 because sub-lines are not independently authored.

---

### Key Findings

- **C-17 and C-18 are symmetric 1-pt aspirational costs**: each costs 1/10 x 10 = 1 pt. Neither breaks golden in isolation or in compound (V-05: -2 pts = 98.000).
- **C-17/C-02 independence confirmed**: C-17 can FAIL (no static guard) while C-02 PASSes probabilistically (model infers correctly). Guarantee shifts from structural to probabilistic. Only unconditional rendering (guard removed entirely, V-03) cascades to C-02 FAIL.
- **C-17/C-02 cascade asymmetry**: C-17 alone = -1 pt; guard removed entirely (C-17 + C-02 cascade) = -13 pts (1 aspirational + 12 essential). Cascade multiplier: 13x. The essential-tier cost is the load-bearing factor.
- **C-18/C-04/C-06 three-surface independence confirmed**: merged instruction satisfies C-04 and C-06 output checks while failing C-18 template-authoring check. Three distinct failure surfaces independently triggerable from the same AMENDMENTS block.
- **Aspirational-only failure ceiling**: even if all 10 aspirational criteria fail simultaneously, composite = 60 + 30 + 0 = 90.000 -- still golden. The golden threshold is gated exclusively by essential-tier pass status, not aspirational score.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-17/C-18 aspirational symmetry: each costs 1 pt (1/10 * 10); golden-compatible individually (V-02: 99, V-04: 99) and in compound (V-05: 98)", "C-17/C-02 cascade asymmetry: inference-only guard = -1 pt total; guard removed entirely = -13 pts (1 aspirational + 12 essential) -- 13x multiplier when unconditional rendering triggers C-02 FAIL", "aspirational-only failure ceiling: 0/10 aspirational = composite 90.000, still golden -- essential-tier gating is the only golden predicate, aspirational failures cannot break golden without essential involvement", "C-18/C-04/C-06 three-surface independence: merged instruction satisfies C-04 output and C-06 output while failing C-18 template-authoring check -- same AMENDMENTS block, three independently testable failure surfaces"]}
```
