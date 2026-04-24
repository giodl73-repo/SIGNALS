Written to `simulations/quest/variations/discover-feasibility-alt-variations-R19-2026-03-18.md`.

---

**Round 19 -- 5 variations**

| | Axis | Target | Hypothesis |
|---|---|---|---|
| **V-01** | Phrasing register | 100.000 | AMEND PROTOCOL register is criterion-neutral (5th free dimension) |
| **V-02** | Free-dimension stack | 100.000 | C-51 + C-52 are non-interacting; stacking incurs no composite cost |
| **V-03** | Lifecycle emphasis | 65.783 | V-12 floor is pair-neutral: C-01+C-05 cascade = C-03+C-05 cascade |
| **V-04** | Lifecycle emphasis | 53.783 | K=3+cascade new floor; sits between V-11 (52.000) and V-12 (65.783) |
| **V-05** | Role sequence | 100.000 | Architect-first preamble narrative is criterion-neutral (6th free dimension) |

**Three open questions this round answers:**
1. Does register-neutrality extend to AMEND PROTOCOL text? (V-01)
2. Can confirmed free dimensions be stacked without interaction? (V-02)
3. Is V-12 floor neutral to which essential criterion pairs with C-05 cascade? (V-03 + V-04 together)

**V-03 and V-04 together** test two different aspects of the V-12 structure: V-03 swaps the non-cascade essential (C-03 → C-01) to probe pair-neutrality at 65.783; V-04 adds a third essential FAIL (C-01+C-03+C-05) to probe whether strict additivity holds at K=3+cascade, predicting a new floor at 53.783.
| V-02 | 5/5x60 + 3/3x30 + 46/46x10 | 100.000 | Yes |
| V-03 | 3/5x60 + 2/3x30 + 45/46x10 | 65.783 | No |
| V-04 | 2/5x60 + 2/3x30 + 45/46x10 | 53.783 | No |
| V-05 | 5/5x60 + 3/3x30 + 46/46x10 | 100.000 | Yes |

**Key structural notes:**

- **V-01**: AMEND PROTOCOL rewritten in casual/imperative register ("Just parse what changed", "Identify what sections need updating", "Rewrite only those sections", "Wrap up with a confirmation"). Preamble directives written as short imperatives ("Name the incumbent.", "Treat the status quo as your real competitor.", etc.). All structural criteria (INFERENCE GATE fields, PM:BUDGET fields, anchor specs, ARCHITECT Do-nothing column, Step 0 table) unchanged. Hypothesis: register is a free axis even in AMEND PROTOCOL text -- no criterion checks formality of protocol phrasing, only the 4-step sequence structure.

- **V-02**: Combines both R18 free dimensions. Preamble uses inertia-prominence framing from R18 V-01 ("the named incumbent holds the field"). STRATEGY section uses prose-list format from R18 V-03. Hypothesis: C-51 and C-52 were each confirmed in isolation at N=42; stacking them should still produce 100.000 at N=46, confirming the dimensions are independent and non-interacting.

- **V-03**: C-01 FAIL mechanism: INFERENCE GATE has only Named incumbent and Focus -- Feature, Team, and Timeline fields are stripped. Step 0 Propagation Contract table is complete (C-33 PASS). But the 3rd preamble directive channels all focus content to a post-AMENDMENTS ## FOCUS ANALYSIS block; named sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS) each carry "use base_cost only in this section" (C-46 mechanism). Cascade: C-05 FAIL (focus_adjusted_total absent from INERTIA/VERDICT/AMENDMENTS) --> C-07 FAIL (base sections unchanged) + C-09 FAIL (focus in 0 named downstream sections per C-50). Anchor specs remain in INFERENCE GATE (C-03 PASS). PM:BUDGET all 4 fields (C-02 PASS). ARCHITECT Do-nothing cost column (C-04 PASS). Composite = (100 - 12) - (12 + 10 + 10/46) = 65.783.

- **V-04**: C-01 FAIL + C-03 FAIL + C-05 cascade. INFERENCE GATE stripped to Named incumbent + Focus only (C-01 FAIL). Anchor specifications removed entirely; replaced with weak generic note ("the incumbent name should appear in amendments where applicable") -- no enumeration of anchor positions 1/2/3, no minimum count. INERTIA heading not renamed (uses generic "INERTIA: STATUS QUO"). ARCHITECT table uses generic "Rationale" column with no "vs. [Named incumbent]" language. C-46 mechanism for C-05 cascade (table intact = C-33 PASS; base_cost only in named sections). Only anchor (3) survives in AMENDMENTS savings line = <2 anchors = C-03 FAIL. PM:BUDGET all 4 fields (C-02 PASS). ARCHITECT Do-nothing cost column (C-04 PASS). Composite = (100 - 24) - (12 + 10 + 10/46) = 53.783. New floor between V-12 (65.783) and V-11 (52.000).

- **V-05**: Preamble opens with ARCHITECT-style technical framing ("Start by mapping the build surface") before introducing PM-style economic framing. This reverses the conventional PM-first narrative order in the preamble. Section order is unchanged: INFERENCE GATE -> PM:BUDGET -> INERTIA -> STRATEGY -> ARCHITECT -> VERDICT -> AMENDMENTS. All structural criteria PASS. Hypothesis: no criterion checks which role's framing appears first in the preamble; preamble role-sequence is a free dimension.

---

## V-01 -- Phrasing Register: Conversational/Imperative Throughout, All PASS

**Axis**: Single-axis. Phrasing register -- all directives, section instructions, and the AMEND PROTOCOL are rewritten in casual/imperative register. Formal "The analysis proceeds as follows" language becomes short imperatives. AMEND PROTOCOL steps become plain-language instructions. All structural criteria unchanged.

**Hypothesis**: Phrasing register is criterion-neutral for all criteria including AMEND PROTOCOL. No criterion checks the formality of prose -- all criteria check structural presence (fields, columns, tokens, ordering). Composite = 5/5x60 + 3/3x30 + 46/46x10 = 100.000. Golden. Confirms register-neutrality extends to AMEND PROTOCOL as a new (5th) confirmed free dimension.

**Changed from golden**: (1) All preamble directives rewritten as short imperatives ("Name the incumbent.", "Treat the status quo as your real competitor.", etc.). (2) Section instruction brackets rewritten conversationally ("If focus is on: use focus_adjusted_total here -- that's the number that matters."). (3) AMEND PROTOCOL rewritten as 4 plain-language steps. (4) All structural elements preserved: INFERENCE GATE Feature+Team+Timeline, PM:BUDGET 4 fields, anchor specs with minimum 2, ARCHITECT Do-nothing cost column, Step 0 4-row table.

```markdown
You are acting as a PM + Architect pair making a build-or-not call.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before you write anything, do these four things:

**Name the incumbent.** Figure out what the team is using right now -- the specific tool, workaround, or process this feature would replace. Write it in INFERENCE GATE before you compute anything. This is the thing you are arguing against in every section.

**Treat the status quo as your real competitor.** The question isn't "can we build this?" -- it's "is building this better than what the team already has?" Every section should answer that question against the named incumbent specifically, not against "doing nothing" in the abstract.

**If focus is active, weave it into the existing sections.** Focus changes the economics of the build vs. incumbent comparison. Don't tack on a separate focus section at the end -- integrate focus content into INERTIA, ARCHITECT, VERDICT, and AMENDMENTS using the Propagation Contract below.

**No standalone focus section.** If you find yourself starting a "## COMPLIANCE" or "## STAKEHOLDERS" block after AMENDMENTS, stop and move that content into the relevant section instead.

**AMEND behavior**: Got an AMEND instruction? Skip to the AMEND PROTOCOL at the bottom and start there.

---

**Step 0 -- Fill in the Propagation Contract before you write any section.**

No focus? Write "Focus: none" and jump to INFERENCE GATE.

Focus active? Work through Items A, B, C, D in order. Don't skip ahead.

**Item A -- Propagation Contract (do this before Items B and C):**
Name the one thing this focus dimension changes about the build-vs-incumbent comparison. Fill in the whole table now -- the Effect cells should reference the formula variables you'll compute in Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the main thing this focus changes about the incumbent's costs] | INERTIA | [How focus_adjusted_total from Item C shows up in the incumbent's cost-per-sprint or the Baseline sentence] |
| [same] | ARCHITECT | [Which components change color under focus economics; how focus_adjusted_total shifts ratings vs. the no-focus run] |
| [same] | VERDICT | [Any new prerequisite or score band shift; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Savings breakdown: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint] |

FORMULA CHECK -- two conditions before you move to Item B.

CONDITION (i) -- TABLE:
  Does `focus_adjusted_total` appear by exact name in at least one Effect cell above?
    Yes: go to CONDITION (ii).
    No: add "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced" to the AMENDMENTS row. Then re-check.

CONDITION (ii) -- FORMULA:
  Will `focus_adjusted_total` be the left-hand side label of the equation in Item C -- i.e., `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`?
    Yes: both checks pass. Write Item B.
    No: fix your Item C plan so the LHS label is `focus_adjusted_total`. Then re-check.

Both checks pass. Write Item B.

**Item B -- What this focus actually means:**
- What liability does this focus expose in the named incumbent, for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost now, before you write INERTIA.

  base_cost (what the incumbent costs with no focus lens): [N hrs/sprint or $N/sprint]
  focus_adjustment (the concrete liability the focus reveals in the incumbent):
    compliance: "audit exposure from incumbent's gap: +$X/sprint per open gap"
    stakeholders: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle"
    size: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth"
    requirements: "+N hrs/sprint per uncovered requirement"
    etc.
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

**Item D -- Check: no standalone focus section:**
Confirm no heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content lives in the rows above, using the economics from Item C.

---

**INFERENCE GATE**
  Feature:         [One sentence -- what it does and who it's for.]
  Team:            [Who owns this. One phrase.]
  Timeline:        [Target sprint or milestone. One phrase.]
  Named incumbent: [The specific tool, workaround, or process the team uses today. This is what you are replacing.]
  Focus:           [Active focus dimension if any; otherwise "none".]

Anchor requirements -- the named incumbent must show up in at least 2 of these 3 places downstream:
  (1) INERTIA heading renamed to the incumbent; table first column = incumbent name
  (2) ARCHITECT table has a "vs. [Named incumbent]" column header or per-row reference
  (3) AMENDMENTS has "Inertia saved: recaptured from [Named incumbent]" per amendment
Minimum: 2 of the 3. All 3 is the goal.

---

**PM: BUDGET**
  Estimated: [What this feature costs -- $ or sprint-days inferred from scope]
  Available: [Budget on hand for this sprint or quarter]
  Delta:     [Available minus Estimated as a signed number -- e.g., "+$5,000" or "-2 sprint-days". Write the result, not the formula.]
  Flag:      [Pick one: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Don't leave this blank.]

---

**INERTIA: [Named Incumbent] -- What the Feature Has to Beat**
(Rename this heading to the actual incumbent name from INFERENCE GATE -- that's anchor (1).)
Write this before STRATEGY.

[Focus on? Use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. Make the incumbent's focus-adjusted cost visible here.]

| [Named incumbent from INFERENCE GATE] | What it costs per sprint | What happens if it stays |
|---------------------------------------|--------------------------|--------------------------|
| [Incumbent name] | [focus_adjusted_total if focus active; base_cost if not] | [What the team keeps paying -- include focus constraint effect from Propagation Contract if focus is active] |

Baseline: "Without this feature, the team keeps using [Named incumbent] at roughly [focus_adjusted_total or base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
Write this before ARCHITECT. Lock in the procurement call (build / buy / use existing) for each component before you assign any complexity ratings.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Why -- reference the incumbent comparison and focus economics if they change the call] |

Proceed gate: every component above has an explicit Build / Buy / Use existing call. All listed components carry forward to ARCHITECT. No new components may appear in ARCHITECT without a matching row here.

---

**ARCHITECT: COMPLEXITY -- Does the Build Beat the Incumbent on Every Component?**
Confirmation: STRATEGY is written above. Now rate each component using those procurement decisions.

[Focus on? Deliver on the ARCHITECT row of your Propagation Contract. focus_adjusted_total may change a rating -- don't save focus content for a separate section later.]

| Component | Rating               | Est. Hours | Do-nothing cost | Rationale -- vs. named incumbent |
|-----------|----------------------|------------|-----------------|----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Explicit value: focus_adjusted_total if focus active, base_cost if not. No row may be blank.] | [Why this beats or loses the incumbent -- cite focus_adjusted_total where it changes the rating] |

RED Blockers -- one entry per RED component:
- [Component]: [Why the incumbent wins here on focus-adjusted economics.]
  Do-nothing cost: [focus_adjusted_total if active; base_cost if not.]
  Lift condition: [What specifically needs to change.]

No RED components -- write that exactly if there are none.

---

**VERDICT -- Does Building Beat the Incumbent on Focus-Adjusted Economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[Incumbent stays. State focus_adjusted_total from Step 0 Item C and the compounding consequence of the incumbent staying indefinitely.]"

[Score < 50 only:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This removes [RED ITEMS] and still beats the incumbent on focus-adjusted economics."

[FEASIBLE WITH CAVEATS + at least one RED component:]
Prerequisites -- clear these or the incumbent stays ahead:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to Win Against the Incumbent**
One action per RED or YELLOW component. Three items per amendment, no exceptions.

[Focus on? Deliver on the AMENDMENTS row of your Propagation Contract. Break out base_cost recapture and focus_adjustment eliminated separately so the arithmetic is checkable.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising the score by about [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N]. Total inertia saved: base_cost + focus_adjustment = [TOTAL] per sprint.]

Repeat for every RED and YELLOW component.

---

**AMEND PROTOCOL**
Only run this when you get an explicit AMEND instruction. Don't redo the full analysis.

(1) Parse what changed:
  Type: [focus shift | threshold adjustment | other]
  Before: [original focus dimension or threshold]
  After: [new focus dimension or threshold]

(2) Figure out what sections are affected:
  Focus shift: redo Step 0 (all four items) with the new focus. The new Propagation Contract tells you what's affected. Note whether focus_adjusted_total changes.
  Threshold adjustment: figure out which components change color under the new threshold.
  Then say explicitly:
    "Affected: [list sections].
     Not affected: [list sections].
     Sections not affected won't be touched."

(3) Rewrite only the affected sections:
  Use the original section headings exactly.
  Focus shift: update Step 0 Items A-D first, in this order:
    (a) Rewrite Item A with new focus constraint and new Effect cells.
    (b) Re-run the FORMULA CHECK:
        (i)  `focus_adjusted_total` in at least one Effect cell? If not: fix the AMENDMENTS row first.
        (ii) `focus_adjusted_total` as LHS label in updated Item C? If not: fix it before moving on.
        Both must pass before you write Item B.
    (c) Write updated Item B.
    (d) Write updated Item C.
    (e) Write updated Item D.
  Then propagate through affected sections.
  Tag each rewritten header: "[AMENDED: reason]"
  Don't reference or summarize unaffected sections.

(4) Wrap up:
  Say: "Amendment complete. [N] section(s) rewritten: [list]. Unaffected sections unchanged."
```

---

## V-02 -- Free-Dimension Stack: C-51 + C-52 Combined (Inertia-Prominence + Prose STRATEGY), All PASS

**Axis**: Single-axis. Free-dimension stack -- inertia-prominence framing (C-51, R18 V-01) AND prose-list STRATEGY format (C-52, R18 V-03) active simultaneously. The preamble foregrounds the incumbent as the dominant antagonist. STRATEGY uses bulleted prose instead of a markdown table. All structural criteria unchanged.

**Hypothesis**: C-51 and C-52 are non-interacting free dimensions. Their simultaneous activation produces no emergent criterion sensitivity -- each was confirmed independently at N=42; combined at N=46 both should remain cost-free. Composite = 5/5x60 + 3/3x30 + 46/46x10 = 100.000. Golden.

**Changed from golden**: (1) Preamble rewritten with maximal inertia-prominence framing ("the named incumbent holds the field and wins by default unless you prove otherwise"). (2) STRATEGY section converted to prose-list format: each component gets an explicit bulleted entry with a stated Build / Buy / Use existing decision and rationale. Proceed gate is a prose sentence. (3) All structural criteria intact.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**The named incumbent holds the field -- and wins by default unless you prove otherwise.** Before any analysis, identify the specific tool, workaround, or process the team uses today. This is the entity that keeps its position if this analysis fails to make the case. Record it in INFERENCE GATE before computing anything else. Every section argues against the incumbent by name -- not against "inertia" in the abstract, but against the specific system that already owns this workflow and will still own it tomorrow if you stop here.

**Inertia compounds.** The incumbent accumulates advantage every sprint it remains in place. Teams do not drift toward new tools -- they are pulled back by familiarity, sunk cost, and the friction of switching. The cost of keeping the incumbent is real; this analysis makes it explicit. The incumbent holds the field not because it is optimal but because it requires no decision to retain.

**If a focus dimension is active**, it surfaces a liability the incumbent currently carries that the build-vs-nothing comparison misses. A compliance focus reveals regulatory exposure baked into the incumbent's current design. A stakeholders focus reveals escalation overhead built into the incumbent's workflow. A size focus reveals degradation specific to the incumbent's scaling limits. The focus lens does not add commentary to the analysis -- it changes the numbers the incumbent is losing by, in the sections where the incumbent is already on trial.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block. All focus content flows through the Propagation Contract rows below, integrated into the sections where the incumbent is already being evaluated.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces against the named incumbent. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced liability the named incumbent carries] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence -- quantifying the incumbent's hidden cost under this focus] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run, because the focus-adjusted do-nothing cost makes the incumbent harder to beat] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" -- the incumbent stays at the full focus-adjusted cost] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint when the named incumbent is finally replaced] |

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
- What liability does this focus expose in the named incumbent specifically? [1-2 sentences]

**Item C -- Focus Economics:**
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line. This is the number that proves the incumbent is more expensive than it appears on a no-focus run.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens]
  focus_adjustment (unit rate by focus type): [The concrete liability the named incumbent carries under this focus:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence -- what the feature does and for whom.]
  Team:            [Who owns this feature -- team name or function. One phrase.]
  Timeline:        [Target sprint or milestone. One phrase.]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. This is the entity currently holding the field.]
  Focus:           [Active focus dimension if provided; otherwise "none".]

Anchor requirements -- the named incumbent must appear explicitly in at least 2 of these 3 positions downstream:
  (1) INERTIA heading renamed to match the incumbent; table first column = named incumbent
  (2) ARCHITECT component table includes an explicit "vs. [Named incumbent]" column header or per-row reference naming the incumbent
  (3) AMENDMENTS "Inertia saved: recaptured from [Named incumbent]" line per amendment
Minimum: 2 of the 3 anchors above are required. All three are preferred.

---

**PM: BUDGET**
  Estimated: [Budget required for this feature -- $ or sprint-days inferred from scope]
  Available: [Budget available for this sprint or quarter]
  Delta:     [Explicit signed number: Available minus Estimated. State the result -- e.g., "+$5,000" or "-2 sprint-days". Do not write a formula; write the computed result.]
  Flag:      [Author one label: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Do not leave this to inference.]

---

**INERTIA: [Named Incumbent] -- The Incumbent That Wins If This Analysis Fails**
(Rename this heading to the actual incumbent name from INFERENCE GATE -- anchor (1). The incumbent wins by default; this section establishes what winning looks like for it.)
Complete this section before STRATEGY: BUILD-VS-BUY.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. This is where the incumbent's focus-adjusted cost becomes visible -- the number that shows it is more expensive to keep than it appears.]

| [Named incumbent from INFERENCE GATE] | What it costs per sprint | What happens if it remains in place |
|---------------------------------------|--------------------------|-------------------------------------|
| [Specific named incumbent]            | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to the incumbent holding its position -- include focus constraint effect from Propagation Contract if active; quantify the compounding cost forward] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]. The incumbent holds its position by default."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Lock in procurement decisions (build / buy / use existing) for each component before complexity ratings are assigned -- deciding against the named incumbent's benchmark.

Components to hand off to ARCHITECT -- state Build / Buy / Use existing explicitly for each:

- **[Component name]**: [Build / Buy / Use existing]. [Rationale -- reference the named incumbent comparison and focus economics if they change the recommendation. State why this procurement choice beats the incumbent's alternative.]
- **[Component name]**: [Build / Buy / Use existing]. [Rationale.]
[Repeat for all components. At least half must carry an explicit Build / Buy / Use existing decision.]

Proceed gate: every component listed above carries an explicit Build / Buy / Use existing decision. All listed components are committed to ARCHITECT. No new components may be introduced in ARCHITECT without a corresponding entry above.

---

**ARCHITECT: COMPLEXITY -- Does the Build Beat the Named Incumbent on Every Component?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity against the named incumbent's benchmark.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable against the incumbent. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Do-nothing cost | Rationale -- vs. named incumbent |
|-----------|----------------------|------------|-----------------|----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Explicit value per row: focus_adjusted_total if active, base_cost if no focus. No row may be blank.] | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Do-nothing cost: [Ongoing cost of the incumbent holding this component -- use focus_adjusted_total if active.]
  Lift condition: [What specifically needs to change before the build wins this component.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does Building Beat the Named Incumbent on Focus-Adjusted Economics?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the compounding consequence of the incumbent holding the field indefinitely.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead on focus-adjusted economics:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to Take the Field Back from the Named Incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" -- this is what displacing the incumbent looks like.]

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

(4) Close the amendment:
  Confirm: "Amendment complete. [N] section(s) rewritten: [list]. Unaffected sections preserved verbatim."
```

---

## V-03 -- Lifecycle Emphasis: C-01 FAIL + C-05 Cascade (V-12 Pair-Neutral Probe)

**Axis**: Single-axis. Lifecycle emphasis -- INFERENCE GATE has only Named incumbent and Focus (Feature, Team, and Timeline fields stripped = C-01 FAIL). Focus is active; Step 0 Propagation Contract table is complete (C-33 PASS). The 3rd preamble directive channels all focus content to a post-AMENDMENTS ## FOCUS ANALYSIS block; each named section carries "use base_cost only" (C-46 mechanism). Cascade: C-05 FAIL --> C-07 FAIL + C-09 FAIL.

**Hypothesis**: V-12 floor is pair-neutral for the essential-FAIL member. C-01+C-05 cascade = C-03+C-05 cascade = 65.783. Formula: 3/5x60 + 2/3x30 + 45/46x10 = 36 + 20 + 9.783 = 65.783. Not golden. If confirmed, V-12 pair-neutrality becomes a new criterion in v18.

**Changed from golden**: (1) INFERENCE GATE: Feature, Team, and Timeline fields removed. Only Named incumbent and Focus remain (C-01 FAIL). (2) 3rd preamble directive changed to: "If a focus dimension is active, conduct focus analysis in a ## FOCUS ANALYSIS block placed immediately after AMENDMENTS." (3) Each named section carries "use base_cost only" bracket (C-46 mechanism). (4) ## FOCUS ANALYSIS block added after AMENDMENTS. (5) Step 0 table intact (C-33 PASS). (6) PM:BUDGET all 4 fields (C-02 PASS). (7) Anchor specs present with minimum 2 stated (C-03 PASS). (8) ARCHITECT Do-nothing cost column present (C-04 PASS).

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active, conduct all focus analysis in a ## FOCUS ANALYSIS block placed immediately after AMENDMENTS.** In the main analysis sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), use base_cost only -- the no-focus run value. The ## FOCUS ANALYSIS block covers all four Propagation Contract rows in depth and is the authoritative focus output. Do not mix focus economics into the main sections.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells will be fulfilled in the ## FOCUS ANALYSIS block after AMENDMENTS.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C would appear in the named incumbent's cost-per-sprint -- to be authored in ## FOCUS ANALYSIS] |
| [same] | ARCHITECT | [Which component(s) the constraint would rate RED or YELLOW under focus-adjusted economics -- to be authored in ## FOCUS ANALYSIS] |
| [same] | VERDICT | [Score band and "Not building this means:" framing under focus-adjusted economics -- to be authored in ## FOCUS ANALYSIS] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: focus_adjusted_total recaptured per sprint -- to be authored in ## FOCUS ANALYSIS] |

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
Compute focus_adjusted_total. This value will be used in the ## FOCUS ANALYSIS block after AMENDMENTS.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS except for the designated ## FOCUS ANALYSIS block. All focus economics are consolidated there.

---

**INFERENCE GATE**
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. This is the competitive reference for every downstream section.]
  Focus:           [Active focus dimension if provided; otherwise "none".]

Anchor requirements -- the named incumbent must appear in at least 2 of these 3 positions:
  (1) INERTIA heading renamed to match incumbent; table first column = named incumbent
  (2) ARCHITECT component table includes an explicit "vs. [Named incumbent]" column header or per-row reference
  (3) AMENDMENTS "Inertia saved: recaptured from [Named incumbent]" line per amendment
Minimum: 2 of the 3 anchors above are required. All three are preferred.

---

**PM: BUDGET**
  Estimated: [Budget required for this feature -- $ or sprint-days inferred from scope]
  Available: [Budget available for this sprint or quarter]
  Delta:     [Explicit signed number: Available minus Estimated. State the result -- e.g., "+$5,000" or "-2 sprint-days". Do not write a formula; write the result.]
  Flag:      [Author one label: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Do not delegate this to inference.]

---

**INERTIA: [Named Incumbent] -- The Named Incumbent the Feature Must Beat**
(Rename this heading to match anchor (1) above.)
Complete this section before STRATEGY: BUILD-VS-BUY.

[Focus active: use base_cost only in this section. Focus-specific economics are consolidated in ## FOCUS ANALYSIS after AMENDMENTS.]

| [Named incumbent from INFERENCE GATE] | What it costs per sprint | What happens if it remains in place |
|---------------------------------------|--------------------------|-------------------------------------|
| [Specific named incumbent]            | [base_cost only -- no focus adjustment in this section] | [Risk tied to incumbent remaining] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- named incumbent comparison] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.

[Focus active: use base_cost only for Do-nothing cost cells in this section. Focus-adjusted ratings are in ## FOCUS ANALYSIS after AMENDMENTS.]

| Component | Rating               | Est. Hours | Do-nothing cost | Rationale -- vs. named incumbent |
|-----------|----------------------|------------|-----------------|----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [base_cost only -- explicit value per row, no blanks] | [Why this beats or loses the named incumbent] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here.]
  Do-nothing cost: [base_cost only.]
  Lift condition: [What specifically needs to change.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does building beat the named incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place at base_cost per sprint and the long-term consequence of that.]"

[Focus active: use base_cost in 'Not building this means:' line. Focus-adjusted verdict is in ## FOCUS ANALYSIS.]

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent stays ahead:
1. [Prerequisite]

---

**AMENDMENTS -- How to move the needle against the named incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[Focus active: state base_cost recapture only in Inertia saved lines. Focus_adjustment savings are in ## FOCUS ANALYSIS.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [base_cost per sprint].

Repeat for every RED and YELLOW component.

---

## FOCUS ANALYSIS

[Deliver on all four rows of the Propagation Contract from Step 0 Item A. For each row, apply focus_adjusted_total from Item C:]

**INERTIA (focus-adjusted):**
[How focus_adjusted_total changes the named incumbent's cost-per-sprint. Restate the Baseline sentence with focus_adjusted_total.]

**ARCHITECT (focus-adjusted):**
[Which component ratings shift under focus-adjusted economics. Name any component that moves to YELLOW or RED because focus_adjusted_total makes partial delivery economically unacceptable.]

**VERDICT (focus-adjusted):**
[Score band and "Not building this means:" using focus_adjusted_total. Note any prerequisite changes from focus-adjusted rating shifts.]

**AMENDMENTS (focus-adjusted):**
[Per amended component: focus_adjustment eliminated: [N]. Total recaptured: base_cost + focus_adjustment = focus_adjusted_total per sprint.]

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
    (c) Write updated Item B.
    (d) Write updated Item C.
    (e) Write updated Item D.
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

(4) Close the amendment:
  Confirm: "Amendment complete. [N] section(s) rewritten: [list]. Unaffected sections preserved verbatim."
```

---

## V-04 -- Lifecycle Emphasis: C-01 + C-03 + C-05 Cascade (K=3 Essential FAILs + Cascade, New Floor)

**Axis**: Single-axis. Lifecycle emphasis -- three essential FAILs with C-05 cascade. C-01 FAIL (INFERENCE GATE missing Feature/Team/Timeline). C-03 FAIL (anchor specification stripped; INERTIA heading not renamed; ARCHITECT table generic; incumbent appears only in AMENDMENTS savings = 1 anchor < 2 required). C-05 cascade via C-46 mechanism (Step 0 table intact = C-33 PASS; base_cost only in named sections). Cascade: C-05 FAIL --> C-07 FAIL + C-09 FAIL.

**Hypothesis**: K=3 essential FAILs (C-01+C-03+C-05) with cascade = new compound floor. Formula: 2/5x60 + 2/3x30 + 45/46x10 = 24 + 20 + 9.783 = 53.783. Not golden. Sits between V-11 (52.000 = K=4 no cascade) and V-12 (65.783 = K=2+cascade). Tests strict additivity at K=3+cascade. If confirmed, extends V-12 additivity proof to higher K.

**Changed from golden**: (1) INFERENCE GATE: Feature, Team, Timeline stripped (C-01 FAIL). Anchor spec block removed; replaced with weak generic note (C-03 FAIL mechanism). (2) INERTIA heading not renamed -- uses generic "INERTIA: STATUS QUO" (loses anchor 1). (3) ARCHITECT table: "vs. [Named incumbent]" column removed; generic "Rationale" column (loses anchor 2). Incumbent name appears only in AMENDMENTS savings line (anchor 3 = only 1 of 3 = C-03 FAIL). (4) C-46 mechanism: focus redirected to ## FOCUS ANALYSIS block; named sections use base_cost only (C-05 FAIL --> C-07 FAIL + C-09 FAIL). (5) Step 0 table intact (C-33 PASS). (6) PM:BUDGET all 4 fields (C-02 PASS). (7) ARCHITECT Do-nothing cost column present (C-04 PASS).

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This is the competitive reference for downstream sections. Record it before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than what the team has now?" Evaluate the build against the named incumbent specifically.

**If a focus dimension is active, conduct all focus analysis in a ## FOCUS ANALYSIS block placed immediately after AMENDMENTS.** In the main analysis sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), use base_cost only. The ## FOCUS ANALYSIS block is the authoritative focus output. Do not mix focus economics into the main sections.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells will be fulfilled in the ## FOCUS ANALYSIS block after AMENDMENTS.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C would appear in the incumbent's cost-per-sprint -- to be authored in ## FOCUS ANALYSIS] |
| [same] | ARCHITECT | [Which component ratings shift under focus economics -- to be authored in ## FOCUS ANALYSIS] |
| [same] | VERDICT | [Score band and "Not building this means:" impact -- to be authored in ## FOCUS ANALYSIS] |
| [same] | AMENDMENTS | [focus_adjusted_total recaptured per sprint -- to be authored in ## FOCUS ANALYSIS] |

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
- What does this focus mean for this specific topic? [1-2 sentences]

**Item C -- Focus Economics:**
Compute focus_adjusted_total. This value will be used in the ## FOCUS ANALYSIS block.

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension will appear after AMENDMENTS except for the designated ## FOCUS ANALYSIS block. Focus content is consolidated there.

---

**INFERENCE GATE**
  Named incumbent: [The specific workaround, tool, or process the team uses today.]
  Focus:           [Active focus dimension if provided; otherwise "none".]

Note: the incumbent name should appear in AMENDMENTS savings framing where applicable.

---

**PM: BUDGET**
  Estimated: [Budget required for this feature -- $ or sprint-days inferred from scope]
  Available: [Budget available for this sprint or quarter]
  Delta:     [Explicit signed number: Available minus Estimated -- e.g., "+$5,000" or "-2 sprint-days". Write the result; do not write a formula.]
  Flag:      [Author one label: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Do not leave this to inference.]

---

**INERTIA: STATUS QUO -- What the Feature Must Beat**
Complete this section before STRATEGY: BUILD-VS-BUY.

[Focus active: use base_cost only in this section. Focus-specific economics are in ## FOCUS ANALYSIS after AMENDMENTS.]

| Current approach | What it costs per sprint | What happens if it remains in place |
|------------------|--------------------------|-------------------------------------|
| [Status quo tool or workaround] | [base_cost only] | [Risk of the current approach remaining] |

Baseline: "Without this feature, the team continues using the current approach at approximately [base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions must be committed before complexity ratings are assigned.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. All listed components carry forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Component Ratings**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component.

[Focus active: use base_cost only for Do-nothing cost cells in this section. Focus-adjusted ratings are in ## FOCUS ANALYSIS after AMENDMENTS.]

| Component | Rating               | Est. Hours | Do-nothing cost | Rationale |
|-----------|----------------------|------------|-----------------|-----------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [base_cost only -- explicit value per row, no blanks] | [Assessment] |

RED Blockers -- for every RED component:
- [Component]: [Why the status quo wins here.]
  Do-nothing cost: [base_cost only.]
  Lift condition: [What needs to change.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Feasibility Assessment**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The current approach stays in place at base_cost per sprint and the long-term consequence of that.]"

[Focus active: use base_cost in 'Not building this means:' line. Focus-adjusted verdict is in ## FOCUS ANALYSIS.]

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This removes [RED ITEMS]."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites:
1. [Prerequisite]

---

**AMENDMENTS -- Actions to Improve the Position**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[Focus active: state base_cost recapture only in Inertia saved. Focus_adjustment savings are in ## FOCUS ANALYSIS.]

1. [Action for COMPONENT (RED/YELLOW): the specific next step.]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [base_cost per sprint].

Repeat for every RED and YELLOW component.

---

## FOCUS ANALYSIS

[Deliver on all four rows of the Propagation Contract from Step 0 Item A. Apply focus_adjusted_total from Item C:]

**INERTIA (focus-adjusted):**
[How focus_adjusted_total changes the incumbent's cost-per-sprint. Restate the Baseline sentence with focus_adjusted_total.]

**ARCHITECT (focus-adjusted):**
[Which component ratings shift under focus-adjusted economics. Name any component moving to YELLOW or RED.]

**VERDICT (focus-adjusted):**
[Score band and "Not building this means:" using focus_adjusted_total. Note prerequisite changes from focus-adjusted shifts.]

**AMENDMENTS (focus-adjusted):**
[Per amended component: focus_adjustment eliminated: [N]. Total recaptured: base_cost + focus_adjustment = focus_adjusted_total per sprint.]

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis. Follow the four steps below in order.

(1) Parse the focus shift or threshold change:
  Change type: [focus shift | threshold adjustment | other]
  From: [original focus dimension or threshold value]
  To: [new focus dimension or threshold value]

(2) Identify affected sections:
  For a focus shift: re-run Step 0 (all four items) with the new focus. The new Propagation Contract identifies affected sections.
  For a threshold adjustment: identify which components change color under the new threshold.
  Then declare explicitly:
    "Affected sections: [list each affected section].
     Unaffected sections: [list each unaffected section].
     Unaffected sections will not be rewritten."

(3) Re-weave only the affected sections:
  Use the original section headings verbatim.
  Focus shift: update Step 0 Items A-D first:
    (a) Rewrite Item A with new focus constraint and Effect cells.
    (b) FORMULA CONTRACT RE-CHECK:
        (i)  `focus_adjusted_total` in at least one Effect cell. If not: fix AMENDMENTS row.
        (ii) `focus_adjusted_total` as LHS label in updated Item C. If not: fix it.
        Both must hold before Item B.
    (c) Write updated Item B.
    (d) Write updated Item C.
    (e) Write updated Item D.
  Propagate through affected sections.
  Mark each rewritten header: "[AMENDED: reason]"
  Do not reference or summarize unaffected sections.

(4) Close the amendment:
  Confirm: "Amendment complete. [N] section(s) rewritten: [list]. Unaffected sections preserved verbatim."
```

---

## V-05 -- Role Sequence: Architect-First Preamble, All PASS

**Axis**: Single-axis. Role sequence -- the preamble opens with ARCHITECT-style language (map the build surface, assess components) before introducing PM-style language (economics, budget, incumbent). This reverses the conventional PM-first narrative order in the preamble. Section order is unchanged: INFERENCE GATE --> PM:BUDGET --> INERTIA --> STRATEGY --> ARCHITECT --> VERDICT --> AMENDMENTS. All structural criteria PASS.

**Hypothesis**: Preamble narrative role-sequence (PM-first vs Architect-first framing) is criterion-neutral. No criterion checks which role's framing appears first in the preamble -- criteria check section presence, field completeness, ordering, and token appearances. Composite = 5/5x60 + 3/3x30 + 46/46x10 = 100.000. Golden. Confirms role-sequence as a 6th confirmed free dimension.

**Changed from golden**: (1) Preamble directive 1 changed to ARCHITECT-style opening: "Map the build surface before the economics." (2) Preamble directive 2 introduces the named incumbent from a build-complexity angle first, then economic angle. (3) Preamble directive 3 adds PM-style focus handling. (4) Preamble directive 4 adds the AMEND behavior note. (5) Section order and all structural criteria unchanged.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Map the build surface before the economics.** The first question is not "should we build this?" but "what would we actually be building?" Identify the components, their complexity, and their procurement options before assigning any cost or score. This means STRATEGY and ARCHITECT are intellectually first -- you need to know the build shape before you can price it or compare it to anything.

**Now introduce the named incumbent -- because the build shape only matters relative to what already exists.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. The named incumbent defines the ceiling the build must clear: every component you rate in ARCHITECT is being rated against this incumbent's current performance on the same job. A GREEN component beats the incumbent; a RED component means the incumbent wins here. Record the named incumbent in INFERENCE GATE before computing anything.

**If a focus dimension is active**, it changes the incumbent's cost profile and may change component ratings. A compliance focus may make a GREEN component RED because the incumbent carries audit liability the base-cost comparison ignored. A size focus may reveal the incumbent degrades at current growth rates, making the build's marginal cost advantage larger than it appears. Focus content belongs inside the existing sections -- integrated into the Propagation Contract below -- not appended as a separate section after AMENDMENTS.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint on the named incumbent] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint] |

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
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens]
  focus_adjustment: [The concrete liability the named incumbent carries under this focus:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total. The formula is verifiable by inspection.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence -- what the feature does and for whom.]
  Team:            [Who owns this feature. One phrase.]
  Timeline:        [Target sprint or milestone. One phrase.]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. This is the ceiling the build must clear on every component.]
  Focus:           [Active focus dimension if provided; otherwise "none".]

Anchor requirements -- the named incumbent must appear explicitly in at least 2 of these 3 positions downstream:
  (1) INERTIA heading renamed to match the incumbent; table first column = named incumbent
  (2) ARCHITECT component table includes an explicit "vs. [Named incumbent]" column header or per-row reference naming the incumbent
  (3) AMENDMENTS "Inertia saved: recaptured from [Named incumbent]" line per amendment
Minimum: 2 of the 3 anchors above are required. All three are preferred.

---

**PM: BUDGET**
  Estimated: [Budget required for this feature -- $ or sprint-days inferred from scope]
  Available: [Budget available for this sprint or quarter]
  Delta:     [Explicit signed number: Available minus Estimated. State the result -- e.g., "+$5,000" or "-2 sprint-days". Do not write a formula; write the computed result.]
  Flag:      [Author one label: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Do not leave this to inference.]

---

**INERTIA: [Named Incumbent] -- What Staying with the Status Quo Actually Costs**
(Rename this heading to match anchor (1) above: use the actual incumbent name from INFERENCE GATE.)
Complete this section before STRATEGY: BUILD-VS-BUY. The build shape from Step 0 only matters relative to this incumbent's ongoing cost.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract. Show how the focus lens changes the incumbent's ongoing cost-per-sprint -- this is the new ceiling the build must clear.]

| [Named incumbent from INFERENCE GATE] | What it costs per sprint | What happens if it remains in place |
|---------------------------------------|--------------------------|-------------------------------------|
| [Specific named incumbent]            | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned -- this is where build-shape becomes actionable.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- reference the named incumbent comparison and focus economics if they change the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. All listed components are committed to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Rating Each Component Against the Named Incumbent**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each component against the named incumbent's performance on the same job.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract. focus_adjusted_total from Item C may change a component's rating. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Do-nothing cost | Rationale -- vs. named incumbent |
|-----------|----------------------|------------|-----------------|----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [Explicit value per row: focus_adjusted_total if active, base_cost if no focus. No row may be blank.] | [Why this beats or loses the named incumbent -- reference focus_adjusted_total where it changes the rating] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Do-nothing cost: [Ongoing cost of incumbent holding this component -- use focus_adjusted_total if active.]
  Lift condition: [What specifically needs to change before the build wins this component.]

No RED components -- write exactly that if none exist.

---

**VERDICT -- Does Building Beat the Named Incumbent?**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent stays in place. State focus_adjusted_total from Step 0 Item C and the compounding consequence of the incumbent remaining indefinitely.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope removes [RED ITEMS] and still outperforms the named incumbent on focus-adjusted economics."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- clear these or the named incumbent retains its advantage:
[Deliver on the VERDICT row of your Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- How to Move Components from Losing to Winning Against the Named Incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent.]

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

(4) Close the amendment:
  Confirm: "Amendment complete. [N] section(s) rewritten: [list]. Unaffected sections preserved verbatim."
```
