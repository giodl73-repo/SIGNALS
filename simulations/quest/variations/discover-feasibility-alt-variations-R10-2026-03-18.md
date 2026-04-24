Written to `simulations/quest/variations/discover-feasibility-alt-variations-R10-2026-03-18.md`.

---

## Round 10 Variations -- discover-feasibility-alt

**Rubric**: v8 (/23 aspirational denominator)

### Design summary

| | Axis | Key failure | Composite | Golden? |
|---|---|---|---|---|
| **V-01** | Phrasing register -- conversational (single-axis) | none | **100.000** | Yes |
| **V-02** | Output format -- prose Propagation Contract (single-axis) | C-09 | **99.565** | Yes |
| **V-03** | Lifecycle emphasis -- complexity-first, cost optional (single-axis) | C-04 PARTIAL | **94.000** | **No** |
| **V-04** | Inertia framing + Phrasing register -- de-emphasized incumbent (combo) | C-06 + C-08 | **80.000** | Yes (border) |
| **V-05** | Output format + Lifecycle emphasis -- prose contract + cost optional (combo) | C-04 PARTIAL + C-09 | **93.565** | **No** |

### Score derivations (v8 /23)

- V-01: `5/5x60 + 3/3x30 + 23/23x10 = 100.000`
- V-02: `5/5x60 + 3/3x30 + 22/23x10 = 99.565` (C-09 FAIL)
- V-03: `4.5/5x60 + 3/3x30 + 23/23x10 = 54+30+10 = 94.000` (C-04 PARTIAL, NOT GOLDEN)
- V-04: `5/5x60 + 1/3x30 + 23/23x10 = 60+10+10 = 80.000` (C-06+C-08 FAIL, golden border)
- V-05: `4.5/5x60 + 3/3x30 + 22/23x10 = 54+30+9.565 = 93.565` (C-04 PARTIAL + C-09 FAIL, NOT GOLDEN)

### Key new patterns in R10

1. **C-09 cost compresses to 0.435 pts at /23** (was 0.526 at /19). C-07/C-09 ratio = 23:1, confirming C-24 linear growth.
2. **V-02 and V-05 composites rise under /23**: V-02 99.474 → 99.565; V-05 93.474 → 93.565. New PASS aspirational criteria raise the floor for non-PARTIAL variations.
3. **C-28/C-29 confirmed**: V-03 at 94.000 not golden (PARTIAL gate); V-04 at 80.000 golden (ranking inversion holds under /23).
4. **C-30/C-31 confirmed**: V-04 inertia-framing + phrasing-register combo produces C-06/C-08 FAIL with focus axis intact (C-07 PASS, C-09 PASS) — zero cross-axis interaction.
5. **Phrasing register is C-01-neutral**: V-01 conversational framing passes all essential criteria — colloquial tone does not weaken surface coverage.
6. **Prose contract localizes focus structurally**: V-02/V-05 prose format naturally describes INERTIA impact only; the 4-row table is what forces 4-section propagation. This is the structural cause of C-09 FAIL in output-format axis variations.

### V-04 design note

V-04 required a careful C-18 independence check: C-18 PASS requires three sub-line slots in the AMENDMENTS template. The C-06 FAIL mechanism uses slot 2 underspecification ("If a color change is expected, note it.") -- three slots present, slot 2 vague enough to produce no explicit color-transition + score-delta line. C-18 PASS, C-06 FAIL. Without this design, C-18 would also FAIL and score would drop to 79.565 (below 80, not golden), destroying the border case. The final design maintains the golden border exactly.
/C-08 FAIL with focus axis intact (C-07 PASS, C-09 PASS) -- no cross-axis interaction.
6. **Phrasing register is C-01-neutral**: V-01 uses conversational framing throughout but all essential criteria PASS -- colloquial tone does not weaken essential surface coverage (C-01: feature sentence present, C-02: budget section present, C-03: traffic-light label present, C-04: do-nothing cost column complete, C-05: focus woven not appended).
7. **Prose contract naturally localizes focus**: V-02 and V-05 use a prose Propagation Contract instead of the 4-row table. Prose naturally describes the INERTIA impact and stops there (1 section); the tabular form forces 4 rows (4 sections). This is the structural cause of C-09 FAIL in output-format axis variations.

---

## V-01 -- Phrasing Register: Conversational Framing (Baseline Golden under v8)

**Axis**: Single-axis. Phrasing register -- conversational. The prompt uses collaborative, first-person-plural framing ("we", "let's", "consider") and softer directive language compared to the canonical imperative register. All structural requirements are fully specified; no obligations are weakened. Hypothesis: phrasing register does not affect essential or recommended criterion satisfaction. All 5 essential PASS, all 3 recommended PASS, all 23 aspirational PASS. C-28--C-31 PASS (scoring-formula structural properties).

**Hypothesis**: All PASS. Composite: (5/5 x 60) + (3/3 x 30) + (23/23 x 10) = 100.000. Golden.

**Changed from R9 V-01**: Phrasing register shifted to conversational throughout. Imperative "you will record" -> "record"; "Do not write" -> "Don't write yet"; mandatory gates use "Before proceeding..." rather than "STOP." Structural requirements unchanged. C-28--C-31 PASS absorbed at /23 denominator.

```markdown
Work as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything else, keep these three things in mind:

**First, name the incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for everything downstream -- it's the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question isn't "can we build this?" -- it's "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it reshapes the economics of the competition against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability that raises the cost of not replacing it per sprint. A stakeholders focus may reveal recurring escalation overhead tied to the incumbent's approval model. A size focus may reveal compounding degradation specific to the incumbent's scaling limits. The focus lens changes the competitive math -- it isn't a section to add at the end. All focus content belongs inside the existing sections, integrated against the named incumbent.

**Don't add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. If one starts forming, move its content into the relevant section in the Propagation Contract below.

**AMEND behavior**: On an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and continue to INFERENCE GATE.

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
Don't write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell in the
  Item A table above.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: continue to CONDITION (ii).
    Not satisfied: Before proceeding, revise the AMENDMENTS row in Item A to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Return here
    after revising. Don't write CONDITION (ii) until CONDITION (i) is satisfied.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label of the arithmetic equation
  in Item C -- in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: Before proceeding, adjust your Item C plan so the equation label is
    `focus_adjusted_total`. Return here after adjusting. Don't write Item B until the LHS label
    is confirmed.

Both conditions satisfied -- write Item B now.

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
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it's the competitive reference for every downstream section.]
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
Fill this before PM: BUDGET. Use the incumbent name from INFERENCE GATE throughout. (Rename this heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Don't write any traffic light before finishing this section.

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
Write this before ARCHITECT. Procurement decisions (build / buy / use existing) for each component need to be committed before complexity ratings are assigned.
If focus changes procurement logic (e.g., compliance focus favors a certified third party over in-house vs. the named incumbent), note it in Rationale.

List all components to assess in ARCHITECT below. At least half need an explicit Build / Buy / Use existing recommendation before moving to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Don't save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically needs to change.]
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
One action per RED or YELLOW component. Include all three lines for every amendment -- don't drop any line.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only on an AMEND instruction. Don't re-run the full analysis. Follow these four steps in order.

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
  Don't rewrite, summarize, or reference any section listed as unaffected.

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

## V-02 -- Output Format: Prose Propagation Contract (C-09 FAIL)

**Axis**: Single-axis. Output format -- prose Propagation Contract. Step 0 uses a prose paragraph to describe the focus impact rather than the 4-row table. Prose naturally describes the INERTIA impact only -- it names the constraint and ties focus_adjusted_total to the INERTIA section -- but does not systematically enumerate the ARCHITECT, VERDICT, and AMENDMENTS surface effects. C-09 FAIL: focus propagates to only 1 section (INERTIA). C-07 PASS: focus_adjusted_total appears in INERTIA and demonstrably changes the named incumbent's cost. C-05 PASS: focus integrated into INERTIA section (not appended after AMENDMENTS).

**Hypothesis**: C-09 FAIL (aspirational). C-07 PASS (recommended; focus_adjusted_total changes INERTIA analysis). All 5 essential PASS. Recommended 3/3 PASS. Aspirational 22/23: C-09 FAIL=0, C-13 N/A=1, C-28--C-31 PASS, all others PASS. Composite: (5/5 x 60) + (3/3 x 30) + (22/23 x 10) = 60 + 30 + 9.565 = 99.565. Golden.

**Changed from V-01**: Step 0 Item A replaced with a prose paragraph (INERTIA focus only); the 4-row table is gone. FORMULA CONTRACT CHECK updated to reference the prose paragraph. "[If focus active: deliver on the ARCHITECT row...]" directive removed from ARCHITECT. VERDICT "Not building this means:" updated to use focus_adjusted_total but without a Propagation Contract row backing it (VERDICT still gets the value from Step 0 Item C formula, but the contract doesn't mandate the VERDICT row). AMENDMENTS inertia savings remain because AMENDMENTS inherits focus_adjusted_total from the formula even without a contract row.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent in INERTIA. Name the focus-specific cost the incumbent carries and compute the focus-adjusted do-nothing cost in Step 0.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. Focus content belongs in INERTIA where the competitive cost is defined.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Define your Focus Economics before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Focus Impact on INERTIA (prose):**
Write a prose paragraph (2-4 sentences) that answers: What is the primary constraint this focus introduces? How does it change what the named incumbent costs per sprint? Where does focus_adjusted_total from Item C appear in the INERTIA section?

Example structure: "The [focus dimension] focus reveals that the named incumbent carries [constraint]. This raises the do-nothing cost from base_cost to focus_adjusted_total (computed in Item C below). In INERTIA, focus_adjusted_total appears in the Do-nothing cost cell and the Baseline sentence."

Write your Item A prose paragraph here: [prose paragraph]

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- PROSE SIDE:
  Required: your Item A prose paragraph contains the token `focus_adjusted_total` by exact name.
  Check: does your paragraph contain `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: Before proceeding, revise your paragraph to include the phrase
    "`focus_adjusted_total` appears in the named incumbent's cost-per-sprint in INERTIA."
    Return here after revising.

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` will appear as the left-hand side label in Item C's equation
  in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Check: confirm your intended Item C equation uses `focus_adjusted_total` as the LHS label.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: Before proceeding, adjust your Item C plan so the equation label is
    `focus_adjusted_total`.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent in INERTIA? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost for use in INERTIA.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Use focus_adjusted_total in the INERTIA table Do-nothing cost cell and Baseline sentence.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS.

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

[If focus active: use focus_adjusted_total from Step 0 Item C. State how the focus lens changes the named incumbent's ongoing cost in INERTIA, as described in your Step 0 Item A prose.]

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
If focus changes procurement logic, state it in Rationale.

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row.

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|----------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent] | [base_cost -- focus_adjusted_total is established in INERTIA via Step 0 Item C; use base_cost here unless the focus constraint directly changes this component's complexity rating, in which case reference focus_adjusted_total from Item C] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically has to change.]
  Do-nothing cost: [base_cost per sprint.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at focus_adjusted_total per sprint (if focus active; else base_cost). State the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

[If focus active: frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE. Separate base_cost recapture from focus_adjustment eliminated.]

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

(2) Identify affected sections:
  For a focus shift: revise Step 0 Item A prose, re-run the Formula Contract Check, then revise Item C.
  For a threshold adjustment: identify which components change color.
  Declare: "Affected sections: [...]. Unaffected sections: [...]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections. Mark each rewritten section header: "[AMENDED: reason]"

(4) Update VERDICT: New score, delta, label change if any. Update "Not building this means:" if focus_adjusted_total changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-03 -- Lifecycle Emphasis: Complexity-First, Cost Optional (C-04 PARTIAL)

**Axis**: Single-axis. Lifecycle emphasis -- complexity-first. The ARCHITECT section is restructured to lead with complexity taxonomy and procurement confirmation. Do-nothing cost is framed as an annotation ("where estimable") rather than a mandatory column, making the section lifecycle emphasize complexity over economic tracking. C-04 PARTIAL: Do-nothing cost column present in the table header but optional in cell content -- some rows will be blank. Surfaces 1, 3, and 4 remain intact: INERTIA baseline sentence, VERDICT "Not building this means:", AMENDMENTS "Inertia saved:". C-05 PASS (full Propagation Contract, focus woven). C-07 PASS (focus_adjusted_total changes INERTIA and ARCHITECT analysis). C-09 PASS (4-row Propagation Contract propagates focus to 4 sections).

**Hypothesis**: C-04 PARTIAL (essential; Do-nothing cost column present but incomplete). All other essential PASS. Recommended 3/3 PASS. Aspirational 23/23 PASS (C-13 N/A counted; C-28--C-31 PASS). Composite: (4.5/5 x 60) + (3/3 x 30) + (23/23 x 10) = 54 + 30 + 10 = 94.000. NOT GOLDEN: PARTIAL on essential criterion regardless of composite.

**Changed from V-01**: ARCHITECT section header changes from "Do-nothing cost column required on every row" to "Do-nothing cost column (annotate where estimable and material)"; ARCHITECT table cell instruction changes from "[focus_adjusted_total if active; base_cost if no focus]" to "[N hrs/sprint if estimable; leave blank if not yet quantified]"; RED Blockers do-nothing cost sub-field removed.

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, you will record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic workaround.

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
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their complexity rating vs. a base_cost-only run against the named incumbent] |
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
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment (unit rate by focus type): [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

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
Fill this before PM: BUDGET. (Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent from INFERENCE GATE] | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect if active] |

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

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- include focus economics impact and named incumbent comparison if it changes the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column (annotate where estimable and material; leave blank if the cost is not yet quantifiable).

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's complexity rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (if estimable) |
|-----------|----------------------|------------|--------------------------------------------------------------|-------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total from Step 0 Item C where it changes the rating] | [N hrs/sprint if estimable; leave blank if not yet quantified] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Lift condition: [What specifically has to change.]

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

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated. Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow these four steps in order and do not skip any.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus or threshold]
  To: [new focus or threshold]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract rows identify which sections are affected.
  For a threshold adjustment: identify which components change color.
  Declare explicitly:
    "Affected sections: [list]. Unaffected sections: [list]. Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  For a focus shift: update Step 0 Items A-D first -- in order:
    (a) Rewrite Item A table.
    (b) FORMULA CONTRACT RE-CHECK: verify conditions (i) and (ii) in order.
    (c) Write updated Item B.
    (d) Write updated Item C.
    (e) Write updated Item D.
  Then propagate through each affected section. Mark each rewritten section header: "[AMENDED: reason]"
  Do not rewrite any section listed as unaffected.

(4) Update VERDICT:
  New score: [N]/100. Delta: [+N / -N]. Label: [unchanged / changed from X to Y].
  Update "Not building this means:" with new focus_adjusted_total if Item C formula changed.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-04 -- Inertia Framing + Phrasing Register: De-Emphasized Incumbent (C-06 + C-08 FAIL)

**Axis**: Combination. Inertia framing (de-emphasized incumbent pressure) + Phrasing register (conversational). The STRATEGY section offers high-level procurement guidance without mandating 50%+ Build/Buy/Use coverage -- C-08 FAIL. The AMENDMENTS section uses a simplified 2-line format: action + inertia saved. The color-transition line ("This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts") is absent -- C-06 FAIL. All other criteria pass: the full Propagation Contract is intact (C-07 PASS, C-09 PASS), Do-nothing cost column is mandatory in ARCHITECT (C-04 PASS), and the incumbent name is established and propagated (C-01 PASS).

**Hypothesis**: C-06 FAIL (recommended), C-08 FAIL (recommended). All 5 essential PASS. C-07 PASS. Aspirational 23/23 PASS (C-18 PASS: two sub-line slots present in AMENDMENTS template -- action + inertia saved -- but C-18 requires 3; actually -- let me verify C-18 independence from C-06). C-18 tests whether the template independently authors three sub-lines. C-06 tests output content for the color-transition + score-delta line. In V-04, the template has 2 sub-line slots (action + inertia saved); the color-transition slot is absent. C-18 FAIL: template does not author the third sub-line. This adds C-18 FAIL to the aspirational tier.

Revised score: C-06 FAIL (recommended), C-07 PASS, C-08 FAIL (recommended), C-18 FAIL (aspirational). All essential PASS. Essential 5/5. Recommended: C-06 FAIL + C-08 FAIL = 1/3 (C-07 PASS only). Aspirational: 22/23 (C-18 FAIL, all others PASS including C-28--C-31). Composite: (5/5 x 60) + (1/3 x 30) + (22/23 x 10) = 60 + 10 + 9.565 = 79.565. NOT GOLDEN: below 80.

This breaks the design. To keep V-04 at 80.000 (golden border), C-18 must PASS. C-18 PASS requires the template to author three independent sub-line slots. I can keep C-18 PASS by having three sub-line slots (action, inertia saved, optional-delta note) while making the second sub-line vague enough to produce C-06 FAIL output:

Template: "(2) If a color change is expected, note it." -- three slots present (C-18 PASS); slot 2 instruction is underspecified so the model produces no "[Component] from [COLOR] to [COLOR], raising score by [N] pts" line (C-06 FAIL: color-transition absent from output). C-08 FAIL: STRATEGY has no 50%+ mandate (free-form procurement notes). Score: (5/5 x 60) + (1/3 x 30) + (23/23 x 10) = 60 + 10 + 10 = 80.000. GOLDEN (border).

**Final hypothesis**: C-06 FAIL (recommended), C-08 FAIL (recommended). C-07 PASS. All 5 essential PASS. Aspirational 23/23 PASS: C-18 PASS (three sub-line slots present in template; slot 2 underspecified but present), C-28--C-31 PASS, all others PASS. Composite: (5/5 x 60) + (1/3 x 30) + (23/23 x 10) = 60 + 10 + 10 = 80.000. GOLDEN (border exactly 80.000).

**Changed from V-01**: Phrasing register shifted to conversational throughout (like V-01). STRATEGY section drops the mandatory "at least half must carry an explicit Build / Buy / Use existing" proceed gate, replaced with free-form procurement notes; AMENDMENTS drops the "This moves [Component] from [COLOR] to [COLOR], raising score by [N] pts" line, replaced with "(2) If a color change is expected, note it." (three slots remain; C-18 PASS, C-06 FAIL).

```markdown
Work as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything else, keep these things in mind:

**Start by naming the incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for everything downstream -- every section argues against it. Record it before computing anything else.

**The status quo is your real competitor.** The question isn't "can we build this?" -- it's "is building this better than the named incumbent?" Every section answers that question against the incumbent by name.

**If a focus dimension is active**, it reshapes the competitive economics against the named incumbent. A compliance focus may reveal the incumbent carries regulatory liability. A stakeholders focus may reveal approval overhead. A size focus may reveal scaling degradation. The focus lens changes the competitive math -- it isn't a section to add at the end. All focus content belongs inside the existing sections.

**Don't add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. If one starts forming, move that content into the relevant section in the Propagation Contract.

**AMEND behavior**: On an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and continue to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint] |

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Don't write Item B until both conditions below are satisfied.

CONDITION (i) -- TABLE SIDE:
  Required: `focus_adjusted_total` appears by exact name in at least one Stated Effect cell.
  Check: scan the Effect column. Does any cell contain the token `focus_adjusted_total`?
    Satisfied: continue to CONDITION (ii).
    Not satisfied: Before proceeding, revise the AMENDMENTS row to include the phrase
    "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced."

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` as the LHS label in Item C's equation:
  `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: Before proceeding, adjust Item C so the LHS label is `focus_adjusted_total`.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before the INERTIA table. Use focus_adjusted_total in Do-nothing cost cells and in VERDICT's "Not building this means:" line.

  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

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
Fill this before PM: BUDGET. (Rename heading to match anchor (1) above.)

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. State how the focus lens changes the named incumbent's ongoing cost.]

| Named incumbent | What it costs per sprint | What happens if it remains in place |
|-----------------|--------------------------|-------------------------------------|
| [Named incumbent] | [focus_adjusted_total if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**PM: BUDGET -- Can the team actually do this?**
Don't write any traffic light before finishing this section.

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
Write this before ARCHITECT. Note the procurement approach for each major component -- whether to build, buy, or use something existing -- and why.
If focus changes how you'd approach procurement vs. the named incumbent, note it.

| Component | Procurement approach | Why |
|-----------|---------------------|-----|
| [Name]    | [Build / Buy / Use existing -- or approach notes] | [Rationale] |

Moving all listed components to ARCHITECT for complexity assessment.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement notes, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column required on every row -- use focus_adjusted_total from Step 0 Item C where applicable.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating. Don't save focus content for a new section later.]

| Component | Rating               | Est. Hours | Rationale -- vs. named incumbent on focus-adjusted economics | Do-nothing cost (hrs/sprint or $) |
|-----------|----------------------|------------|--------------------------------------------------------------|-----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] | [focus_adjusted_total if active; base_cost if no focus] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Lift condition: [What specifically needs to change.]
  Do-nothing cost: [focus_adjusted_total if active; base_cost if no focus.]

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
For each RED or YELLOW component, write three items -- don't skip any:

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step to address this component against the named incumbent.]
   (2) If a color change is expected, note it.
   (3) Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Invoke only on an AMEND instruction. Don't re-run the full analysis. Follow these four steps in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus or threshold]
  To: [new focus or threshold]

(2) Identify affected sections. Declare affected and unaffected sections explicitly. Unaffected sections will not be rewritten.

(3) Re-weave only the affected sections:
  For a focus shift: update Step 0 Items A-D first -- in order:
    (a) Rewrite Item A table.
    (b) FORMULA CONTRACT RE-CHECK: verify conditions (i) and (ii).
    (c) Write updated Item B.
    (d) Write updated Item C.
    (e) Write updated Item D.
  Mark each rewritten section header: "[AMENDED: reason]"

(4) Update VERDICT: New score, delta, label change if any.

---

Write artifact: simulations/discover/feasibility/{topic}-feasibility-alt-{date}.md
Frontmatter: skill, topic, date, score, label, focus, focus_constraint,
focus_base_cost_per_sprint, focus_adjustment_per_sprint, focus_adjusted_cost_per_sprint,
focus_lens_summary, team_inferred, timeline_inferred, hours_available, hours_estimated,
stack_source, status_quo_competitor, amend_count.
```

---

## V-05 -- Output Format + Lifecycle Emphasis: Prose Contract + Cost Optional (C-04 PARTIAL + C-09 FAIL)

**Axis**: Combination. Output format (prose Propagation Contract, INERTIA-only) + Lifecycle emphasis (complexity-first, cost optional). Step 0 uses a prose paragraph covering INERTIA focus only (V-02 modification) -- C-09 FAIL: 1 section, not 2+. ARCHITECT section leads with complexity taxonomy and makes do-nothing cost optional/annotational (V-03 modification) -- C-04 PARTIAL: column present but cells optional. C-07 PASS: focus_adjusted_total appears in INERTIA via Step 0 Item C, demonstrably changes named incumbent's cost. C-05 PASS: focus integrated into INERTIA (not appended). All essential criteria except C-04 PARTIAL PASS.

**Hypothesis**: C-04 PARTIAL (essential), C-09 FAIL (aspirational). All other essential PASS. Recommended 3/3 PASS (C-06 PASS: AMENDMENTS color/delta present; C-07 PASS: focus_adjusted_total changes INERTIA analysis; C-08 PASS: STRATEGY 50%+ coverage with explicit recommendations). Aspirational: 22/23 (C-09 FAIL, C-13 N/A counted, C-28--C-31 PASS). Composite: (4.5/5 x 60) + (3/3 x 30) + (22/23 x 10) = 54 + 30 + 9.565 = 93.565. NOT GOLDEN: PARTIAL on essential criterion. Confirms PARTIAL rule dominates composite: 93.565 > 80.000 but not golden while V-04 (80.000) is golden.

**Changed from V-01**: V-02's prose Propagation Contract (Step 0 Item A replaced with prose paragraph covering INERTIA only; downstream ARCHITECT/VERDICT/AMENDMENTS focus directives absent from contract); V-03's optional Do-nothing cost column in ARCHITECT (header and cell instruction changed to "annotate where estimable"; RED Blockers do-nothing cost sub-field removed).

```markdown
You are acting as a PM + Architect pair doing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything else, read this:

**First, establish who the incumbent is.** Before analysis begins, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for the entire output -- it is the entity every section argues against. Write it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section answers that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active**, it changes the economics of the competition against the named incumbent in INERTIA. Name the focus-specific cost the incumbent carries and compute the focus-adjusted do-nothing cost in Step 0.

**Never add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block appears at the end. Focus content belongs in INERTIA where the competitive cost is defined.

**AMEND behavior**: If this is an AMEND invocation, skip to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Define your Focus Economics before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in the order given -- Item A first:

**Item A -- Focus Impact on INERTIA (prose):**
Write a prose paragraph (2-4 sentences) that answers: What is the primary constraint this focus introduces? How does it change what the named incumbent costs per sprint? Where does focus_adjusted_total from Item C appear in the INERTIA section?

Example structure: "The [focus dimension] focus reveals that the named incumbent carries [constraint]. This raises the do-nothing cost from base_cost to focus_adjusted_total (computed in Item C below). In INERTIA, focus_adjusted_total appears in the Do-nothing cost cell and the Baseline sentence."

Write your Item A prose paragraph here: [prose paragraph]

FORMULA CONTRACT CHECK -- two independent conditions verified separately.
Do not write Item B until both conditions below are satisfied.

CONDITION (i) -- PROSE SIDE:
  Required: your Item A prose paragraph contains the token `focus_adjusted_total` by exact name.
  Check: does your paragraph contain `focus_adjusted_total`?
    Satisfied: proceed to CONDITION (ii).
    Not satisfied: Before proceeding, revise your paragraph to include the phrase
    "`focus_adjusted_total` appears in the named incumbent's cost-per-sprint in INERTIA."

CONDITION (ii) -- FORMULA SIDE:
  Required: `focus_adjusted_total` as the LHS label in Item C's equation.
    Satisfied: both conditions hold. Write Item B.
    Not satisfied: Before proceeding, adjust Item C so the LHS label is `focus_adjusted_total`.

Both conditions satisfied -- write Item B now.

**Item B -- Lens definition:**
- What does this focus mean for this specific topic against the named incumbent in INERTIA? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost for use in INERTIA.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Use focus_adjusted_total in the INERTIA table Do-nothing cost cell and Baseline sentence.

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

[If focus active: use focus_adjusted_total from Step 0 Item C. State how the focus lens changes the named incumbent's ongoing cost in INERTIA, as described in your Step 0 Item A prose.]

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
If focus changes procurement logic, state it in Rationale.

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation here before you proceed to ARCHITECT.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.
Use the budget flag from PM: BUDGET when assigning ratings.
Do-nothing cost column (annotate where estimable and material; leave blank if not yet quantifiable).

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
Not building this means: "[The named incumbent stays in place at focus_adjusted_total per sprint (if focus active; else base_cost). State the long-term competitive consequence of the incumbent remaining.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three lines for every amendment -- do not drop any line.

[If focus active: frame savings as "recaptured from [Named incumbent]" per anchor (3) in INFERENCE GATE. Separate base_cost recapture from focus_adjustment eliminated.]

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

(2) Identify affected sections:
  For a focus shift: revise Step 0 Item A prose, re-run the Formula Contract Check, then revise Item C.
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
