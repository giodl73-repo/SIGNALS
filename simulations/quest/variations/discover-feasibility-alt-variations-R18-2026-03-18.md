Written to `simulations/quest/variations/discover-feasibility-alt-variations-R18-2026-03-18.md`.

---

**Round 18 -- 5 variations**

| | Axis | Target | Composite | New pattern |
|---|---|---|---|---|
| **V-01** | Inertia framing | All PASS, focus active, maximal incumbent emphasis | 100.000 | Inertia-prominence framing is criterion-neutral |
| **V-02** | Lifecycle emphasis | C-05 FAIL cascade (C-46), C-33 PASS, /42 denominator | 77.762 | Confirms V-09 floor at /42; C-23 formula 78-10/N at N=42 |
| **V-03** | Output format | STRATEGY as prose-list (no table), all PASS | 100.000 | STRATEGY format is criterion-neutral across C-08/C-10/C-11/C-12/C-16 |
| **V-04** | Phrasing register + Lifecycle emphasis | C-02 FAIL + C-04 FAIL, formal register | 76.000 | Extends C-44 to C-02+C-04 pair; C-34 at compound-FAIL floor |
| **V-05** | Lifecycle emphasis + Inertia framing | C-03 FAIL + C-05 FAIL cascade, focus active | 65.762 | New compound floor: essential propagation FAIL + focus cascade |

**Floor derivations (v16, /42):**

| Variation | Formula | Composite | Golden? |
|-----------|---------|-----------|---------|
| V-01 | 5/5x60 + 3/3x30 + 42/42x10 | 100.000 | Yes |
| V-02 | 4/5x60 + 2/3x30 + 41/42x10 | 77.762 | No |
| V-03 | 5/5x60 + 3/3x30 + 42/42x10 | 100.000 | Yes |
| V-04 | 3/5x60 + 3/3x30 + 42/42x10 | 76.000 | No |
| V-05 | 3/5x60 + 2/3x30 + 41/42x10 | 65.762 | No |

**Key structural notes:**

- **V-02**: C-46 mechanism. Step 0 table intact (C-33 PASS). Preamble 3rd directive channels focus to `## FOCUS ANALYSIS` after AMENDMENTS. Each named section carries `[Focus active: use base_cost only in this section.]`. Result: C-05 FAIL (focus_adjusted_total absent from INERTIA/VERDICT/AMENDMENTS) → C-07 FAIL (base sections unchanged) → C-09 FAIL (focus in 0 named downstream sections per C-50). Aspirational cost at /42: 10/42 = 0.238 pts.

- **V-04**: C-02 FAIL = PM: BUDGET block absent entirely. C-04 FAIL = Do-nothing cost column removed from ARCHITECT table and RED Blockers. Formal/technical register throughout (Directives 1-5, "The analysis proceeds as follows"). C-34 confirmed at 76.000 floor.

- **V-05**: C-03 FAIL mechanism — anchor specifications stripped from INFERENCE GATE; INERTIA heading rename directive removed; ARCHITECT table uses generic "Rationale" column with no "vs. [Named incumbent]" reference. Only anchor (3) survives in AMENDMENTS. One anchor < 2 required = C-03 FAIL. C-05 FAIL via C-46 (same as V-02). Compound: (3/5x60) + (2/3x30) + (41/42x10) = 36 + 20 + 9.762 = 65.762. New floor not in the v16 table.
rrent floor table.

**Structural notes:**
1. **V-02 C-46 mechanism**: Step 0 4-row table is present and complete (C-33 PASS). But the 3rd preamble directive channels focus to a post-AMENDMENTS ## FOCUS ANALYSIS block, and each downstream section carries "[Focus active: use base_cost only in this section.]" This voids focus_adjusted_total from all three C-05 destinations despite the table committing to them (C-46). Cascade: C-05 FAIL → C-07 FAIL (base sections unchanged) + C-09 FAIL (focus in 0 named downstream sections per C-50). Aspirational cost: C-09 FAIL = 10/42 = 0.238 pts.
2. **V-04 denominator**: aspirational = 42/42 x 10 = 10.000 (all aspirational PASS/N/A at /42). Composite = 36 + 30 + 10 = 76.000.
3. **V-05 compound formula**: C-03 FAIL costs 12 pts (essential). C-05 FAIL costs 12 pts (essential) + cascade to C-07 FAIL (10 pts recommended) + C-09 FAIL (0.238 pts aspirational). Total cost: 12 + 12 + 10 + 0.238 = 34.238 pts from 100. Composite = 65.762. Golden-breaking on essential-PASS gate (two essential FAILs) AND composite < 80.

**Floor derivations under v16 (denominator /42):**

| Variation | Definition | Formula | Composite | Golden? |
|-----------|-----------|---------|-----------|---------|
| V-01 | All PASS, focus active, maximal inertia framing | 5/5x60 + 3/3x30 + 42/42x10 | 100.000 | Yes |
| V-02 | C-05 FAIL cascade (C-46: table present, downstream base_cost only) | 4/5x60 + 2/3x30 + 41/42x10 | 77.762 | No (essential FAIL gate + cascade) |
| V-03 | All PASS, STRATEGY prose-list format | 5/5x60 + 3/3x30 + 42/42x10 | 100.000 | Yes |
| V-04 | C-02 FAIL + C-04 FAIL, formal register, no focus | 3/5x60 + 3/3x30 + 42/42x10 | 76.000 | No (essential FAIL gate) |
| V-05 | C-03 FAIL + C-05 FAIL cascade, focus active | 3/5x60 + 2/3x30 + 41/42x10 | 65.762 | No (essential FAIL gate + composite < 80) |

V-02 detail: 48 + 20 + (41/42x10) = 48 + 20 + 9.762 = 77.762. C-09 FAIL costs 10/42 = 0.238 pts.
V-04 detail: 36 + 30 + 10 = 76.000. Same composite as V-07 rubric floor (C-01+C-03 pair, C-44 canonical); new pair C-02+C-04.
V-05 detail: 36 + 20 + 9.762 = 65.762. New compound floor: not in the current rubric floor table. C-03 FAIL (essential) + cascade C-05→C-07+C-09 (essential + recommended + aspirational) combined for first time.

---

## V-01 -- Inertia Framing: Maximal Incumbent Emphasis, Focus Active, All PASS

**Axis**: Single-axis. Inertia framing -- the status-quo competitor is positioned as the dominant antagonist in every preamble directive and section header. Language is intensified to foreground incumbent entrenchment, inertia cost, and competitive stakes. All structural criteria unchanged.

**Hypothesis**: Inertia-prominence framing is criterion-neutral. No rubric criterion tests how loudly the incumbent is foregrounded in preamble language -- all criteria are structural (presence, ordering, coverage, behavior). Making the incumbent the narrative center of gravity does not move any criterion score. Composite = 5/5x60 + 3/3x30 + 42/42x10 = 100.000. Golden.

**Changed from golden**: (1) Preamble rewritten to foreground incumbent entrenchment more aggressively -- "the named incumbent holds the field" framing. (2) Section headers add "Against the Named Incumbent" language where structurally neutral. (3) Focus directives emphasize that focus sharpens the competitive case against the incumbent specifically. (4) All structural criteria (INFERENCE GATE fields, BUDGET block, anchor specs, ARCHITECT Do-nothing column, VERDICT/AMENDMENTS framing) unchanged.

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**The named incumbent holds the field -- and will keep holding it unless you prove otherwise.** Before any analysis, identify the specific workaround, tool, or process the team uses today. This is the entity that will win if you do not build. Record it in INFERENCE GATE before computing anything else. Every section must argue against this incumbent by name -- not against "doing nothing" in the abstract, but against the specific system that already owns the workflow.

**Inertia is not passive.** Teams do not drift toward new tools -- they are pulled back to the incumbent by familiarity, sunk cost, and the absence of a compelling reason to switch. The incumbent's advantage compounds every sprint it remains in place. The cost of keeping the incumbent is real and growing; this analysis makes that cost visible.

**When focus is active**, it exposes a liability the incumbent currently carries that your team may not have priced. A compliance focus reveals regulatory exposure in the incumbent's current design. A stakeholders focus reveals approval overhead baked into the incumbent's workflow. A size focus reveals degradation the incumbent produces at current growth rates. The focus lens does not add commentary -- it changes the numbers the incumbent is losing by, and it changes them in the sections where the incumbent is already being evaluated.

**Do not add a standalone focus section after AMENDMENTS.** No "## COMPLIANCE" or "## STAKEHOLDERS" block should appear at the end. All focus content flows through the Propagation Contract rows below, integrated into the sections where the incumbent is already on trial.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces against the named incumbent. Complete the full table before moving to Item B or Item C. The Stated Effect cells reference the formula variables that Item C will compute -- wire the contract to the economics before computing them.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced liability the named incumbent carries] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence -- quantifying the incumbent's hidden cost] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus run, because the focus-adjusted do-nothing cost makes the incumbent harder to beat] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:" -- i.e., the incumbent stays in place at the full focus-adjusted cost] |
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

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint -- the named incumbent's workaround cost ignoring the focus lens; inferred from topic context]
  focus_adjustment (unit rate by focus type): [The concrete liability the named incumbent carries under this focus:
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
  Delta:     [Explicit signed number: Available minus Estimated. State the result as a number -- e.g., "+$5,000" or "-2 sprint-days". Do not write a formula; write the computed result.]
  Flag:      [Author one label: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Do not leave this to inference -- write the label.]

---

**INERTIA: [Named Incumbent] -- The Case for the Status Quo the Feature Must Defeat**
(Rename this heading to match anchor (1) above: use the actual incumbent name from INFERENCE GATE.)
Complete this section before STRATEGY: BUILD-VS-BUY. Use the incumbent name throughout -- it is the entity that wins if this analysis fails to make the case.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). Make the incumbent's focus-adjusted cost visible before comparing it to any build option.]

| [Named incumbent from INFERENCE GATE] | What it costs per sprint | What happens if it remains in place |
|---------------------------------------|--------------------------|-------------------------------------|
| [Specific named incumbent]            | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active; name what the incumbent costs the team compounding forward] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]. The incumbent holds its position by default."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned -- deciding procurement against the named incumbent's benchmark, not in the abstract.
If focus changes procurement logic (e.g., compliance focus favors a certified third party over in-house because the incumbent's gap introduces audit liability), state it in Rationale.

Components to hand off to ARCHITECT -- each must carry an explicit Build / Buy / Use existing decision before any ARCHITECT row is written:

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale -- reference the named incumbent comparison and focus economics if they change the recommendation] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

---

**ARCHITECT: COMPLEXITY -- Does the Build Beat the Named Incumbent on Every Component?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity against the named incumbent's benchmark.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating -- a component may rate YELLOW or RED because the focus-adjusted do-nothing cost makes partial delivery economically unacceptable. Do not save focus content for a new section later.]

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
[Deliver on the VERDICT row of your Propagation Contract (Step 0 Item A).]
1. [Prerequisite]

---

**AMENDMENTS -- How to Take the Field Back from the Named Incumbent**
One action per RED or YELLOW component. Include all three items for every amendment. Do not omit any item.

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent. Frame savings as "recaptured from [Named incumbent]" -- this is what winning looks like.]

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

## V-02 -- Lifecycle Emphasis: C-05 FAIL Cascade at /42 (V-09 Floor Confirmation)

**Axis**: Single-axis. Lifecycle emphasis -- focus is active, the Step 0 Propagation Contract table IS present (C-33 PASS), but a preamble directive channels all focus analysis to a post-AMENDMENTS ## FOCUS ANALYSIS block. Each downstream section carries an explicit instruction to use base_cost only. This voids focus_adjusted_total from all three C-05 destinations (INERTIA, VERDICT, AMENDMENTS) via the C-46 mechanism. Cascade: C-05 FAIL → C-07 FAIL + C-09 FAIL.

**Hypothesis**: C-05 FAIL (C-46 pattern) + C-07 FAIL + C-09 FAIL. C-33 PASS (table structurally intact). Composite: `4/5x60 + 2/3x30 + 41/42x10 = 48 + 20 + 9.762 = 77.762`. Not golden. Confirms V-09 rubric floor at /42 (was 77.750 at /40 in R17 V-02). Empirical anchor for C-23 cascade formula 78 - 10/N at N=42: 78 - 10/42 = 77.762.

**Changed from golden**: (1) Preamble 3rd directive changed to: redirect focus to a post-AMENDMENTS ## FOCUS ANALYSIS block. (2) INERTIA focus bracket changed to: "use base_cost only in this section." (3) ARCHITECT focus bracket changed to: "use base_cost only for Do-nothing cost cells." (4) VERDICT focus bracket changed to: "use base_cost in 'Not building this means:' line." (5) AMENDMENTS focus bracket changed to: "state base_cost recapture only." (6) ## FOCUS ANALYSIS section added after AMENDMENTS. (7) All other criteria intact: INFERENCE GATE has Feature+Team+Timeline (C-01 PASS), PM: BUDGET has all four fields (C-02 PASS), anchor specs present (C-03 PASS), Do-nothing cost column on every row (C-04 PASS), Step 0 table complete (C-33 PASS).

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**Establish the named incumbent.** Before any analysis, record in INFERENCE GATE the specific workaround, tool, or process the team uses today. This name becomes the competitive reference for all downstream sections -- it is the entity every section argues against. Record it in INFERENCE GATE before computing anything else.

**The status quo is your real competitor.** The question is not "can we build this?" -- it is "is building this better than the named incumbent?" Every section must answer that question against the incumbent by name, not against a generic workaround.

**If a focus dimension is active, conduct a dedicated focus analysis in a ## FOCUS ANALYSIS block placed immediately after AMENDMENTS.** In the main analysis sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), use base_cost only -- the no-focus run value. The ## FOCUS ANALYSIS block covers all four Propagation Contract rows in depth and is the authoritative focus output. Do not mix focus economics into the main sections.

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
| [same] | VERDICT | [Score band impact and "Not building this means:" framing under focus-adjusted economics -- to be authored in ## FOCUS ANALYSIS] |
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
  Feature:         [One sentence.]
  Team:            [Who owns this. One phrase.]
  Timeline:        [Sprint or milestone target. One phrase.]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
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

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation before proceeding to ARCHITECT.

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
[Which component(s) change rating under focus-adjusted economics. Identify any component that moves to YELLOW or RED because focus_adjusted_total makes partial delivery economically unacceptable.]

**VERDICT (focus-adjusted):**
[Score band and "Not building this means:" line using focus_adjusted_total. Note any prerequisites that emerge from the focus-adjusted rating changes.]

**AMENDMENTS (focus-adjusted):**
[For each amended component: focus_adjustment eliminated: [N]. Total inertia saved: base_cost + focus_adjustment = focus_adjusted_total per sprint.]

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

## V-03 -- Output Format: STRATEGY as Prose-List, All PASS

**Axis**: Single-axis. Output format -- the STRATEGY: BUILD-VS-BUY section uses a prose-list format (bulleted items with explicit Build/Buy/Use recommendations) instead of a markdown table. All structural criteria unchanged. No focus.

**Hypothesis**: STRATEGY section format (table vs. prose-list) is criterion-neutral. C-08 requires explicit Build/Buy/Use for ≥50% of components -- satisfied by prose bullets. C-10 requires STRATEGY before ARCHITECT -- satisfied by section ordering. C-11 requires forward-declaration of components -- satisfied in prose. C-12 requires ARCHITECT to back-reference STRATEGY -- satisfied by the confirmation sentence. C-16 requires proceed-gate text in STRATEGY body and confirmation text in ARCHITECT body -- both present in prose. Composite = 5/5x60 + 3/3x30 + 42/42x10 = 100.000. Golden.

**Changed from golden**: (1) STRATEGY section rewritten as prose-list: each component gets a bullet with explicit Build/Buy/Use + rationale. (2) Proceed gate rewritten as prose sentence. (3) All other sections and criteria unchanged.

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
Compute the focus-adjusted do-nothing cost before writing the INERTIA table. Use focus_adjusted_total in every Do-nothing cost cell and in VERDICT's "Not building this means:" line.

State the formula as a labeled arithmetic equation:

  base_cost (no-focus run value): [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries:
    compliance focus: "audit exposure from incumbent's gap: +$X/sprint per open gap";
    stakeholders focus: "sign-off overhead in incumbent model: +N hrs/sprint per approval cycle";
    size focus: "scaling degradation at incumbent's limit: +N hrs/sprint per sprint at current growth rate";
    requirements focus: "+N hrs/sprint per uncovered requirement"; etc.]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

Every downstream Do-nothing cost cell uses focus_adjusted_total.

**Item D -- Failure-mode rejection:**
No section heading matching the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") will appear after AMENDMENTS. All focus content flows through the rows in Item A's table, using the economics from Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [Who owns this. One phrase.]
  Timeline:        [Sprint or milestone target. One phrase.]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace. Establish this first -- it is the competitive reference for every downstream section.]
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
(Rename this heading to match anchor (1) above: use the actual incumbent name from INFERENCE GATE.)
Complete this section before STRATEGY: BUILD-VS-BUY. Use the incumbent name throughout.

[If focus active: use focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of your Propagation Contract (Step 0 Item A). State how the focus lens changes the named incumbent's ongoing cost.]

| [Named incumbent from INFERENCE GATE] | What it costs per sprint | What happens if it remains in place |
|---------------------------------------|--------------------------|-------------------------------------|
| [Specific named incumbent]            | [focus_adjusted_total from Step 0 Item C if active; base_cost if no focus] | [Risk tied to incumbent -- include focus constraint effect from Propagation Contract if active] |

Baseline: "Without this feature, the team continues using [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions (build / buy / use existing) for each component must be committed before complexity ratings are assigned. If focus changes procurement logic, note it in the component rationale.

Components to hand off to ARCHITECT -- state Build / Buy / Use existing for each:

- **[Component name]**: [Build / Buy / Use existing]. [Rationale -- why this procurement choice against the named incumbent; include focus economics if it changes the recommendation.]
- **[Component name]**: [Build / Buy / Use existing]. [Rationale.]
[Repeat for all components. At least half must have an explicit Build / Buy / Use recommendation.]

Proceed gate: every component listed above carries an explicit Build / Buy / Use existing recommendation. All listed components are committed to ARCHITECT. No new components may be added in ARCHITECT without a corresponding entry above.

---

**ARCHITECT: COMPLEXITY -- Where does the build beat or lose to the named incumbent?**
Confirmation: STRATEGY: BUILD-VS-BUY is written above. Using those procurement decisions, rate each listed component for complexity.

[If focus active: deliver on the ARCHITECT row of your Propagation Contract (Step 0 Item A). focus_adjusted_total from Item C may change a component's rating. Do not save focus content for a new section later.]

| Component | Rating               | Est. Hours | Do-nothing cost | Rationale -- vs. named incumbent |
|-----------|----------------------|------------|-----------------|----------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]        | [focus_adjusted_total or base_cost -- explicit value per row, no blanks] | [Why this beats or loses the named incumbent] |

RED Blockers -- for every RED component:
- [Component]: [Why the named incumbent wins here on focus-adjusted economics.]
  Do-nothing cost: [Ongoing cost of incumbent holding this component -- use focus_adjusted_total if active.]
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

[If focus active: deliver on the AMENDMENTS row of your Propagation Contract (Step 0 Item A). Separate base_cost recapture from focus_adjustment eliminated so the arithmetic is transparent.]

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

## V-04 -- Phrasing Register + Lifecycle Emphasis: C-02 FAIL + C-04 FAIL, Formal Register

**Axis**: Combined. Phrasing register (formal/technical throughout) + lifecycle emphasis (two essential criteria removed). PM: BUDGET block absent (C-02 FAIL). ARCHITECT Do-nothing cost column absent (C-04 FAIL). No focus.

**Hypothesis**: C-02 FAIL + C-04 FAIL. All recommended PASS. All aspirational PASS/N/A. Composite: `3/5x60 + 3/3x30 + 42/42x10 = 36 + 30 + 10 = 76.000`. Not golden. Extends C-44 criterion-neutrality to the C-02+C-04 essential pair. Canonical V-07 pair was C-01+C-03 (R13). C-02+C-04 produces the same 76.000 floor, confirming the additivity claim is pair-neutral. Formal register confirms C-34: technical phrasing incurs zero composite cost at the compound-FAIL floor.

**Changed from golden**: (1) PM: BUDGET block removed entirely (C-02 FAIL). (2) ARCHITECT table: Do-nothing cost column removed (C-04 FAIL). (3) RED Blockers: Do-nothing cost line removed (C-04 FAIL). (4) Preamble and section headers rewritten in formal/technical register. (5) All other criteria intact.

```markdown
This analysis establishes the technical and economic feasibility of a proposed feature by evaluating it against the named incumbent -- the specific tool, process, or workaround the team currently operates.

Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

The analysis proceeds as follows. Prior to any section authoring, the following directives govern execution:

**Directive 1 -- Named incumbent establishment.** The analysis begins by identifying the specific workaround, tool, or process currently in use. This entity is designated the named incumbent and serves as the competitive reference throughout the analysis. The named incumbent is recorded in INFERENCE GATE before any computation is performed.

**Directive 2 -- Competitive framing.** The analysis does not evaluate whether the feature can be built in isolation. It evaluates whether building the feature produces a superior outcome relative to the named incumbent. Each section produces a verdict against the named incumbent by name.

**Directive 3 -- Focus dimension handling.** When a focus dimension is specified, the analysis integrates the focus constraint into the existing section structure rather than appending a separate section. The focus constraint modifies the competitive economics against the named incumbent and propagates through INERTIA, ARCHITECT, VERDICT, and AMENDMENTS via the Propagation Contract.

**Directive 4 -- No standalone focus section.** No section heading corresponding to the focus dimension (e.g., "## COMPLIANCE", "## STAKEHOLDERS") shall appear after AMENDMENTS. Focus content is distributed through the Propagation Contract rows.

**Directive 5 -- AMEND invocation.** If the current invocation is an AMEND instruction, execution proceeds directly to the AMEND PROTOCOL at the end of this template. No re-analysis is performed.

---

**Step 0 -- Propagation Contract construction. Execute before authoring any section.**

If focus is inactive: record "Focus: none" and proceed to INFERENCE GATE.

If focus is active, execute Items A through D in sequence. Item A must be completed before Items B, C, or D are written.

**Item A -- Propagation Contract:**
Identify the primary constraint introduced by the focus dimension. Populate the following table completely before proceeding to Item B or Item C.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C appears in the named incumbent's cost-per-sprint or Baseline sentence] |
| [same] | ARCHITECT | [Which component(s) the constraint rates RED or YELLOW; how focus_adjusted_total changes their rating vs. a no-focus evaluation] |
| [same] | VERDICT | [Prerequisite added and/or score band impact; confirm focus_adjusted_total appears in "Not building this means:"] |
| [same] | AMENDMENTS | [Focus-specific inertia savings: base_cost recaptured + focus_adjustment eliminated = focus_adjusted_total recaptured per sprint] |

FORMULA CONTRACT VERIFICATION -- two conditions must be satisfied before proceeding to Item B.

CONDITION (i):
  Requirement: the token `focus_adjusted_total` must appear by exact name in at least one Effect cell of the Item A table.
  Verification: scan the Effect column.
    Condition satisfied: proceed to CONDITION (ii).
    Condition not satisfied: revise the AMENDMENTS row of Item A to include "`focus_adjusted_total` recaptured per sprint when [Named incumbent] is replaced." Verify CONDITION (i) again before proceeding.

CONDITION (ii):
  Requirement: `focus_adjusted_total` shall serve as the left-hand side label of the arithmetic equation in Item C, in the form `focus_adjusted_total = base_cost + focus_adjustment = [TOTAL]`.
  Verification: confirm the planned Item C equation uses this label.
    Condition satisfied: both conditions are verified. Proceed to Item B.
    Condition not satisfied: revise the Item C equation plan. Verify CONDITION (ii) again before proceeding to Item B.

**Item B -- Focus lens definition:**
- Specify what this focus dimension implies for the current topic relative to the named incumbent. [1-2 sentences]

**Item C -- Focus economics computation:**
The focus-adjusted do-nothing cost shall be computed before the INERTIA table is authored. This value is applied to all Do-nothing cost cells and to the "Not building this means:" line in VERDICT.

  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Unit rate specific to the focus type and the named incumbent's liability:
    compliance: audit exposure per open gap; stakeholders: sign-off overhead per cycle;
    size: degradation per sprint at current growth rate; requirements: cost per uncovered requirement]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

**Item D -- Focus containment:**
No section heading corresponding to the focus dimension shall appear after AMENDMENTS. All focus content is distributed through Item A's Propagation Contract rows and Item C's formula.

---

**INFERENCE GATE**
  Feature:         [One sentence.]
  Team:            [Responsible team or function. One phrase.]
  Timeline:        [Target sprint or delivery milestone. One phrase.]
  Named incumbent: [The specific workaround, tool, or process currently in use. This entity is the competitive reference for all downstream sections.]
  Focus:           [Active focus dimension if specified; otherwise "none".]

Incumbent propagation requirements -- the named incumbent shall appear explicitly in at least 2 of the following 3 anchor positions:
  (1) INERTIA heading renamed to match the incumbent; table first column = named incumbent
  (2) ARCHITECT component table contains a column header or row-level reference naming the incumbent
  (3) AMENDMENTS contains "Inertia saved: recaptured from [Named incumbent]" per amendment entry
Minimum propagation threshold: 2 of 3 anchor positions. All 3 are the expected standard.

---

**INERTIA: [Named Incumbent] -- Status Quo Analysis**
(Rename this heading per anchor (1): substitute the actual incumbent name from INFERENCE GATE.)
This section shall be completed prior to STRATEGY: BUILD-VS-BUY.

[If focus active: apply focus_adjusted_total from Step 0 Item C. Deliver on the INERTIA row of the Propagation Contract.]

| [Named incumbent from INFERENCE GATE] | Cost per sprint | Consequence of continued operation |
|---------------------------------------|-----------------|-------------------------------------|
| [Named incumbent]                     | [focus_adjusted_total if active; base_cost if no focus] | [Risk profile of incumbent remaining -- include focus constraint if active] |

Baseline statement: "Absent this feature, the team operates on [Named incumbent] at approximately [focus_adjusted_total or base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
This section shall be authored prior to ARCHITECT: COMPLEXITY. Procurement decisions -- build, buy, or use existing -- must be committed for each component before complexity ratings are assigned.

Components to be evaluated in ARCHITECT are listed below. Each component carries an explicit procurement recommendation. At least 50% of listed components must carry an explicit Build / Buy / Use existing designation.

| Component | Procurement decision | Rationale |
|-----------|---------------------|-----------|
| [Name]    | Build / Buy / Use existing | [Basis for the decision; reference the named incumbent and focus economics where applicable] |

Proceed gate: all components listed above carry a Build / Buy / Use existing designation. These components are committed to ARCHITECT. No additional components may be introduced in ARCHITECT without a corresponding entry in this section.

---

**ARCHITECT: COMPLEXITY -- Component-level feasibility against the named incumbent**
Verification: STRATEGY: BUILD-VS-BUY is recorded above. Component ratings below apply the procurement decisions established there.

[If focus active: deliver on the ARCHITECT row of the Propagation Contract. focus_adjusted_total may change component ratings. Focus content is not deferred to a later section.]

| Component | Rating               | Estimated hours | Rationale -- competitive position vs. named incumbent |
|-----------|----------------------|-----------------|-------------------------------------------------------|
| [Name]    | GREEN / YELLOW / RED | [N]             | [Assessment of build vs. named incumbent] |

RED Blockers -- one entry per RED component:
- [Component]: [Basis for the named incumbent's competitive advantage on this component.]
  Lift condition: [Specific condition required for the build to achieve competitive parity.]

No RED components -- state this explicitly if no RED components exist.

---

**VERDICT -- Feasibility determination relative to the named incumbent**
Composite score: [N]/100
Label: [NOT FEASIBLE / FEASIBLE WITH CAVEATS / FEASIBLE]
Not building this means: "[The named incumbent remains in operation. State focus_adjusted_total from Step 0 Item C and the long-term consequence of continued incumbent operation.]"

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100. This scope eliminates [RED ITEMS] while maintaining competitive advantage over the named incumbent."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites -- the following conditions must be met or the named incumbent retains competitive advantage:
[Deliver on the VERDICT row of the Propagation Contract.]
1. [Prerequisite]

---

**AMENDMENTS -- Prescribed actions to improve the competitive position**
One amendment per RED or YELLOW component. Each amendment entry contains three required sub-lines. No sub-line may be omitted.

[If focus active: deliver on the AMENDMENTS row of the Propagation Contract. Separate base_cost recapture from focus_adjustment eliminated.]

1. [Prescribed action for COMPONENT (RED/YELLOW).]
   (2) This action transitions [Component] from [COLOR] to [COLOR], increasing the composite score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [N hrs/sprint or $N/sprint]. [If focus active: focus_adjustment eliminated: [N hrs/sprint or $N/sprint]. Total recaptured: base_cost + focus_adjustment = [TOTAL] per sprint.]

Apply this structure to every RED and YELLOW component.

---

**AMEND PROTOCOL**
This protocol is invoked exclusively upon receipt of an explicit AMEND instruction. The full analysis is not re-executed. The following four steps are executed in sequence.

(1) Classify the amendment:
  Type: [focus shift | threshold adjustment | other]
  Prior state: [original focus dimension or threshold value]
  Revised state: [new focus dimension or threshold value]

(2) Determine affected scope:
  Focus shift: re-execute Step 0 (Items A-D) under the revised focus. The updated Propagation Contract identifies affected sections.
  Threshold adjustment: identify which components change rating classification under the revised threshold.
  Declare explicitly:
    "Affected sections: [enumerated list].
     Unaffected sections: [enumerated list].
     Unaffected sections will not be modified."

(3) Revise affected sections only:
  Apply the amendment to each affected section. Section headings are preserved verbatim.
  Focus shift: update Step 0 Items A-D in the following sequence:
    (a) Revise Item A with updated focus constraint and Effect cells.
    (b) FORMULA CONTRACT RE-VERIFICATION:
        (i)  `focus_adjusted_total` present in at least one Effect cell. If absent: revise AMENDMENTS row.
        (ii) `focus_adjusted_total` as LHS label in updated Item C. If absent: revise equation label.
        Both conditions verified before proceeding to Item B.
    (c) Revise Item B for the new focus lens.
    (d) Revise Item C with updated economics.
    (e) Revise Item D for the new focus dimension.
  Propagate the updated contract to all affected sections.
  Each revised section header is marked: "[AMENDED: reason]"
  Unaffected sections are not referenced or summarized.

(4) Amendment closure:
  State: "Amendment complete. [N] section(s) revised: [list]. Unaffected sections are unchanged."
```

---

## V-05 -- Lifecycle Emphasis + Inertia Framing: C-03 FAIL + C-05 FAIL Cascade, Focus Active

**Axis**: Combined. Lifecycle emphasis (two essential criteria fail) + inertia framing (preamble foregrounds incumbent strongly, but structural anchor specifications stripped from INFERENCE GATE creating the C-03 FAIL). Focus active, C-05 FAIL via C-46 mechanism (standalone block, base_cost in named sections). Cascade: C-05 FAIL → C-07 FAIL + C-09 FAIL. C-33 PASS (table intact).

**Hypothesis**: C-03 FAIL + C-05 FAIL cascade (C-07 FAIL + C-09 FAIL). C-33 PASS. Composite: `3/5x60 + 2/3x30 + 41/42x10 = 36 + 20 + 9.762 = 65.762`. Not golden. New compound floor: essential pair C-03+C-05 with focus cascade. Tests cross-axis compound: propagation failure (C-03, structural) + focus cascade (C-05→C-07+C-09). First empirical data point at this floor.

**Changed from golden**: (1) INFERENCE GATE: anchor (1), (2), (3) specifications and minimum count language removed. Only a generic incumbent note remains. (2) INERTIA heading rename directive removed. INERTIA table first column changed to "[Status quo tool]" (generic). (3) ARCHITECT table: "vs. [Named incumbent]" column header removed; rationale column is generic. (4) C-03 result: only anchor (3) is structurally guaranteed (AMENDMENTS Inertia saved line). Incumbent appears in <2 anchors = C-03 FAIL. (5) C-05 FAIL: focus redirected to standalone ## FOCUS ANALYSIS block after AMENDMENTS; each named section uses base_cost only (C-46 mechanism). (6) Step 0 table is intact (C-33 PASS). (7) INFERENCE GATE Feature+Team+Timeline present (C-01 PASS). PM: BUDGET all four fields present (C-02 PASS). STRATEGY present and before ARCHITECT (C-08, C-10 PASS).

```markdown
You are acting as a PM + Architect pair performing a build-or-not decision.
Inputs: Topic, Focus (optional: compliance | stakeholders | requirements | naming | size | other)

Before writing anything, observe the following directives:

**The named incumbent is the competitive reference.** This analysis does not evaluate feasibility in isolation -- it evaluates whether building this feature beats what the team already has. Identify the specific workaround, tool, or process in use and record it in INFERENCE GATE. Every section speaks to this incumbent.

**Inertia is an active force.** Teams default to the status quo because it is known and low-friction. The cost of staying with the incumbent is real but often invisible. This analysis makes it visible.

**If a focus dimension is active, conduct focus analysis in a dedicated ## FOCUS ANALYSIS block placed immediately after AMENDMENTS.** In the named analysis sections (INERTIA, ARCHITECT, VERDICT, AMENDMENTS), use base_cost only. The ## FOCUS ANALYSIS block covers all four Propagation Contract rows and is the authoritative focus output.

**AMEND behavior**: If this is an AMEND invocation, proceed directly to the AMEND PROTOCOL at the end before writing anything.

---

**Step 0 -- Build the Propagation Contract before writing any section.**

If focus is inactive: write "Focus: none" and proceed to INFERENCE GATE.

If focus is active, complete all four items in order -- Item A first:

**Item A -- Propagation Contract (before lens definition and before economics):**
Name the primary constraint this focus introduces. Complete the full table before moving to Item B or Item C. The Stated Effect cells will be fulfilled in the ## FOCUS ANALYSIS block after AMENDMENTS.

| Constraint introduced by focus | Section where it surfaces | Effect on that section |
|-------------------------------|--------------------------|------------------------|
| [One phrase -- the primary focus-introduced constraint] | INERTIA | [How focus_adjusted_total from Item C changes the incumbent's cost -- to be detailed in ## FOCUS ANALYSIS] |
| [same] | ARCHITECT | [Which component ratings shift under focus economics -- to be detailed in ## FOCUS ANALYSIS] |
| [same] | VERDICT | [Score band and "Not building this means:" impact under focus economics -- to be detailed in ## FOCUS ANALYSIS] |
| [same] | AMENDMENTS | [focus_adjusted_total recaptured per sprint -- to be detailed in ## FOCUS ANALYSIS] |

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
Compute focus_adjusted_total. This value is applied in the ## FOCUS ANALYSIS block after AMENDMENTS.

  base_cost: [N hrs/sprint or $N/sprint]
  focus_adjustment: [Concrete focus-specific liability the named incumbent carries]
  focus_adjusted_total = base_cost + focus_adjustment = [TOTAL per sprint]

**Item D -- Failure-mode rejection:**
No section heading corresponding to the focus dimension will appear after AMENDMENTS except for the designated ## FOCUS ANALYSIS block. Focus content is consolidated there.

---

**INFERENCE GATE**
  Feature:         [One sentence -- what the feature does and for whom.]
  Team:            [Who owns this. One phrase.]
  Timeline:        [Sprint or milestone target. One phrase.]
  Named incumbent: [The specific workaround, tool, or process the team uses today that this feature would replace.]
  Focus:           [Active focus dimension if provided; otherwise "none".]

Note: the incumbent name should appear in AMENDMENTS savings framing as applicable.

---

**PM: BUDGET**
  Estimated: [Budget required for this feature -- $ or sprint-days inferred from scope]
  Available: [Budget available for this sprint or quarter]
  Delta:     [Explicit signed number: Available minus Estimated -- e.g., "+$5,000" or "-2 sprint-days". State the result; do not write a formula.]
  Flag:      [Author one label: OVER BUDGET (Delta negative) | WITHIN BUDGET (Delta zero or positive) | AT RISK (Delta close to zero or uncertain). Do not leave this to inference.]

---

**INERTIA: STATUS QUO -- What the Feature Must Beat**
Complete this section before STRATEGY: BUILD-VS-BUY.

[Focus active: use base_cost only in this section. Focus-specific economics are in ## FOCUS ANALYSIS after AMENDMENTS.]

| [Status quo tool] | What it costs per sprint | What happens if it remains in place |
|-------------------|--------------------------|-------------------------------------|
| [Current workaround or tool] | [base_cost only] | [Risk of incumbent remaining] |

Baseline: "Without this feature, the team continues using the current approach at approximately [base_cost per sprint]."

---

**STRATEGY: BUILD-VS-BUY**
Write this section before ARCHITECT. Procurement decisions must be committed before complexity ratings are assigned.

List all components to assess in ARCHITECT below. At least half must carry an explicit Build / Buy / Use existing recommendation before proceeding.

| Component | Build / Buy / Use existing | Why |
|-----------|----------------------------|-----|
| [Name]    | [Recommendation]           | [Rationale] |

Proceed gate: the components listed above each carry a Build / Buy / Use existing recommendation. Carrying all listed components forward to ARCHITECT. No new components may be added in ARCHITECT without a corresponding STRATEGY entry.

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
Not building this means: "[The current approach stays in place at base_cost per sprint and its long-term consequence.]"

[Focus active: use base_cost in 'Not building this means:' line. Focus-adjusted verdict is in ## FOCUS ANALYSIS.]

[Only if score < 50:]
Scoped alternative: "Scoped to [CONSTRAINT]: [N]/100."

[Only if label is FEASIBLE WITH CAVEATS and at least one RED component exists:]
Prerequisites:
1. [Prerequisite]

---

**AMENDMENTS -- Actions to Improve the Position**
One action per RED or YELLOW component. Include all three items for every amendment.

[Focus active: state base_cost recapture only in Inertia saved. Focus_adjustment savings are in ## FOCUS ANALYSIS.]

1. [Action for COMPONENT (RED/YELLOW).]
   (2) This moves [Component] from [COLOR] to [COLOR], raising score by approximately [N] pts.
   Inertia saved: recaptured from [Named incumbent]: [base_cost per sprint].

Repeat for every RED and YELLOW component.

---

## FOCUS ANALYSIS

[Deliver on all four rows of the Propagation Contract from Step 0 Item A. Apply focus_adjusted_total from Item C:]

**INERTIA (focus-adjusted):**
[How focus_adjusted_total changes the named incumbent's cost-per-sprint. Restate the Baseline sentence with focus_adjusted_total.]

**ARCHITECT (focus-adjusted):**
[Which component ratings shift under focus-adjusted economics. Name any component that moves to YELLOW or RED due to focus_adjusted_total.]

**VERDICT (focus-adjusted):**
[Score band and "Not building this means:" using focus_adjusted_total. Note any prerequisite changes from focus-adjusted rating shifts.]

**AMENDMENTS (focus-adjusted):**
[Per amended component: focus_adjustment eliminated: [N]. Total recaptured: base_cost + focus_adjustment = focus_adjusted_total per sprint.]

---

**AMEND PROTOCOL**
Invoke only when an AMEND instruction is received. Do not re-run the full analysis.

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
    (c) Write updated Item B.
    (d) Write updated Item C.
    (e) Write updated Item D.
  Then propagate the updated contract through each affected section.
  Mark each rewritten section header with: "[AMENDED: reason]"
  Do not rewrite, summarize, or reference any section listed as unaffected.

(4) Close the amendment:
  Confirm: "Amendment complete. [N] section(s) rewritten: [list]. Unaffected sections preserved verbatim."
```
