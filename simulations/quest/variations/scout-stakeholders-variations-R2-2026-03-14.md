Written to `simulations/quest/variations/scout-stakeholders-variations-R2-2026-03-14.md`.

---

## Round 2 — 5 Variations for `scout-stakeholders`

**Design logic:** R1 produced three 100-point outputs (V-01, V-04, V-05) that each contributed one of the four new v2 aspirational criteria. R2 targets getting all four into at least two variations simultaneously.

| ID | Axis | Key changes from R1 baseline | Criteria targeted |
|----|------|------------------------------|-------------------|
| **V-01** | Source column enforced as required grid field | Source column added to grid with 3 defined labels; Step 7 becomes revision loop with numbered source audit | C-11, C-12 |
| **V-02** | Prose narrative repaired + Frame Type column | Adds discrete UX Analysis section (fixes R1 C-07 PARTIAL); adds Frame Type column with prefilled labels; adds "make the change" mandate | C-07 fix, C-12, C-13 |
| **V-03** | Inertia framing repaired + inline failure modes | Adds dedicated UX section (fixes R1 C-07 PARTIAL); inline anti-pattern label at every step where failure can occur | C-07 fix, C-13, C-14 |
| **V-04** | Full combo: reversed sequence + all four new criteria | V-04 R1 natively had C-11/C-12; adds Frame Type column (C-13) and anti-pattern at every phase gate (C-14) | C-11, C-12, C-13, C-14 — expected 120/120 |
| **V-05** | Conversational + source column + amendment mandate + failure modes | V-05 R1 natively had C-13/partial C-14; adds Source column (C-11) and explicit "make the change" mandate (C-12); failure modes at all steps | C-11, C-12, C-13, C-14 — expected 120/120 |

**Key design decisions:**
- V-01 is the minimal intervention — adds only the two missing source/amendment criteria to the clean baseline, preserving all R1 strengths
- V-02 and V-03 repair the two 95-point R1 variations (each failed C-07 for the same structural reason: UX not separated) — if they now score full recommended + aspirational, they confirm the UX section fix is the load-bearing repair
- V-04 and V-05 are the full-coverage combos; both should reach 120 but through structurally different designs (formal phased vs. conversational imperative)
120/120 |
| **V-05** | Conversational + source column + amendment mandate + failure modes | Combo (C-11 + C-12 + C-13 + C-14) | V-05 R1 already had C-13 and partial C-14. Adding C-11 (Source column) and C-12 (amendment update mandate — "make the change, don't just note it") closes remaining gaps. All failure modes inline at the step where failure occurs. Expected: 120/120 |

**Rubric coverage prediction per R2 variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 CODEOWNERS fallback | + | + | + | + | + |
| C-02 Power/Interest grid | + | + | + | + | + |
| C-03 Veto risks ranked | + | + | + | + | + |
| C-04 Champion concrete action | + | + | + | + | + |
| C-05 Comms strategy per quadrant | + | + | + | + | + |
| C-06 Conflicts | + | + | + | ++ | + |
| C-07 Role framing | + | ++ | ++ | ++ | + |
| C-08 Critical-path gatekeepers | + | + | + | + | + |
| C-09 Amendment phase | + | + | + | ++ | + |
| C-10 Negative-space framing | + | + | + | + | + |
| C-11 Source-tracking column | ++ | - | - | ++ | ++ |
| C-12 Amendment update mandate | ++ | ++ | ++ | ++ | ++ |
| C-13 Prefilled frame types | + | ++ | ++ | ++ | ++ |
| C-14 Named failure modes inline | + | + | ++ | ++ | ++ |

`++` = design change specifically targets this criterion. `-` = known gap, not addressed by this variation's axis.

---

## V-01 — Source Column Enforced as Required Grid Field

**Axis**: Grid structure — Source column required for every row; amendment loop mandates updates, not observations
**Hypothesis**: Making Source a required column (not an optional audit note) makes the amendment phase a traceable gap-detection scan. Every "initial-inventory" row that should have been conflict-discovered becomes a visible defect. C-11 and C-12 should reliably pass without disrupting V-01's clean baseline coverage of all other criteria.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names, owners, and scope. If absent, extract org context from the invocation string. If neither source provides sufficient context, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently.

---

**Step 1 -- Strategy Role: Conflict and Critical-Path Discovery**

Run this step before building the grid. Answer:

1. What are at least two competing definitions of success across stakeholder groups? Name both parties in each entry.
2. Which stakeholders are structurally incentivized to resist, delay, or deprioritize this decision -- not because they oppose it, but because their incentives do not include it?
3. Whose scheduling or approval decision constrains the launch timeline regardless of their support stance? State the minimum lead time. Label each `[CRITICAL PATH]`.

Output: a conflict list (minimum two entries, both parties named per entry) and a critical-path list (minimum one entry with lead time). Format conflicts as: **[Group A] vs. [Group B] -- nature of tension**.

---

**Step 2 -- PM Role: Power/Interest Grid**

Using conflict and critical-path findings from Step 1, place each stakeholder on the grid. The **Source** column is required -- every row must have an origin label.

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Source | Notes |
|-------------|-------------|----------------|----------|--------|-------|
| | | | | (conflict-discovered / UX-segment / initial-inventory) | |

**Source label definitions:**
- **conflict-discovered**: this row was identified through conflict analysis in Step 1
- **UX-segment**: this row was identified as a distinct segment in Step 3 (fill retroactively)
- **initial-inventory**: this row came from the initial landscape scan before any analytical phase

Any row remaining as "initial-inventory" after the amendment phase is a candidate for review -- it may indicate a gap that conflict analysis should have surfaced.

Critical-path stakeholders flagged in Step 1 carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: **Keep Satisfied** (high power, low interest) | **Engage** (high power, high interest) | **Champion** (lower power, high interest) | **Inform** (low power, low interest).

---

**Step 3 -- UX Role: Experience Intersections and Segment Detection**

For each stakeholder in the Engage and Champion quadrants, identify:
- The moment in their workflow where this decision intersects their work
- Whether this group is monolithic or whether a sub-segment has substantially higher interest (early adopters, power users, blocked workflows)

If a segment split is identified: add the sub-segment as a new row to the Step 2 grid with Source = `UX-segment`.

---

**Step 4 -- Veto Risk Register**

Rank strictly by probability. Do not follow grid order or alphabetical order.

1. **[Stakeholder]** -- Probability: HIGH / MEDIUM / LOW. Impact if triggered: [consequence]. Mitigation: [concrete action with timing].

---

**Step 5 -- Champion Activation**

Name the champion(s). Give one concrete activation action per champion -- specific enough to put on a calendar or assign an owner. Not "engage" or "build the relationship."

Examples of acceptable actions: "Give [role] the live demo slot at the sprint review." "Have [role] co-present the first customer case study at the all-hands."

---

**Step 6 -- Communication Strategy**

| Quadrant | Who | Frame Type | Timing | Message: lead with this |
|----------|-----|-----------|--------|------------------------|
| Keep Satisfied | | Risk-reduction | [relative to milestone] | Why this is lower risk than status quo |
| Engage | | Value-demonstration | [relative to milestone] | Specific capability or outcome to show |
| Champion | | Activation | Now | Their motivating frame and the concrete ask |
| Inform | | Awareness | [relative to milestone] | One tool, one link, time-to-value |

The **Frame Type** column is required. Each row must carry a distinct type -- using the same frame on multiple rows = FAIL.

---

**Step 7 -- Amendment Phase (Revision Loop)**

This is a revision loop. For each finding, update the grid, veto list, or comms table -- do not only observe.

Audit items:

1. **Landscape**: Is any group on the grid actually two distinct segments with different interest levels? If yes: split the row, add the new segment with Source = `UX-segment`, and note the amendment.
2. **Missing actors**: Is anyone downstream who is not yet represented? Add them to the grid with Source = `amendment-discovery`.
3. **Gatekeeper reframe**: For any compliance or security gatekeeper in Keep Satisfied: write one sentence -- "What this product does NOT do: [data it does not collect, action it does not take]." This pre-answers their likely objection.
4. **Source audit**: Review every "initial-inventory" row. Was this actor assumed before any analysis was run? Should they have been conflict-discovered instead? Note any re-sourcing.

Number each amendment. For each finding that changes the grid, re-rank list, or comms table: make the change and note it.

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-02 -- Prose Narrative Repaired + Frame Type Column

**Axis**: Output format -- prose narrative with embedded tables, UX structurally separated (repairs R1 C-07 gap), Frame Type column in comms table (C-13), amendment update mandate (C-12)
**Hypothesis**: R1 V-02 scored 95 because UX was collapsed into prose without a dedicated section. Adding a discrete UX section repairs C-07. Adding the Frame Type column to the comms table structurally prevents same-frame repetition (C-13). Adding explicit amendment update mandate (C-12) converts observations to revisions. All other V-02 strengths preserved: sequencing rationale paragraph, "why is this the top veto" explanation.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Org Context**

First, determine the org context. Check for a CODEOWNERS file; if found, use it to identify teams and decision owners. If no CODEOWNERS file exists, extract the org structure from the invocation string. If neither source provides sufficient context, ask exactly one question: "What org or team is this decision for?" Never infer silently.

---

**Stakeholder Landscape (Strategy + PM)**

Begin with a brief narrative paragraph naming who has a stake in this decision and where interest conflicts lie. Name at least two conflicts: pairs of stakeholder groups optimizing for different outcomes, in tension with each other. Format each conflict: **[Group A] vs. [Group B] -- nature of tension**. A single stakeholder's risk is not a conflict.

Once the conflict landscape is named in prose, populate the grid:

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Notes |
|-------------|-------------|----------------|----------|-------|

After the grid, write a paragraph explaining the two or three most consequential placements -- specifically any stakeholder whose placement was shaped by a conflict identified above, and any critical-path gatekeeper whose scheduling constrains the launch timeline. For each critical-path gatekeeper, state the lead time required.

---

**UX Analysis**

This section is analytically distinct from the stakeholder grid. For each stakeholder in the Engage and Champion quadrants:
- Name the moment in their workflow where this decision lands
- State whether this group is monolithic or whether a segment within it has substantially higher interest (early adopters, power users, blocked workflows)

If a segment split is identified here, add the sub-segment as a new row to the grid above and note the addition.

---

**Veto Risk Register**

Write one sentence framing the veto landscape, then provide the list in descending probability order:

1. **[Stakeholder]** -- Probability: HIGH / MEDIUM / LOW. Impact: [consequence]. Mitigation: [action with timing].

After the list, write one sentence explaining why the top-ranked veto is ranked first -- not what it is, but why it is the highest-probability threat given this specific context.

---

**Champion Identification**

Name the champion(s) in prose. Explain why their advocacy carries weight with the gatekeeper quadrant stakeholders. Then state the concrete activation action: not a general intent to engage, but a specific action (e.g., "give them the live demo slot at the sprint review," "have them co-present the first customer case study").

---

**Communication Strategy**

One sentence introducing the strategy, then the table:

| Quadrant | Who | Frame Type | Timing | Message: lead with this |
|----------|-----|-----------|--------|------------------------|
| Keep Satisfied | | Risk-reduction | | |
| Engage | | Value-demonstration | | |
| Champion | | Activation | | |
| Inform | | Awareness | | |

The **Frame Type** column is required. Each row must carry a distinct frame type label -- same frame across multiple rows = FAIL.

After the table, write a paragraph noting any sequencing dependency between quadrants -- specifically whether Keep Satisfied stakeholders must be briefed before the Engage quadrant is approached.

---

**Amendments**

After completing the analysis, review for what was not initially obvious. For each finding: update the relevant section above -- do not only observe.

- Did any stakeholder group need to be split into sub-segments with distinct interest levels? Name the split and add the row.
- Was any actor missing from the initial landscape? Name them, assign a quadrant, and add them to the grid.
- For any compliance or security gatekeeper: write one sentence -- "What this product does NOT do: [data it does not collect, action it does not take]." This pre-answers their likely objection.
- Are the timing entries in the comms table sequenced correctly?

Number each amendment. For each finding that changes a section: make the change and note it. If no amendments arise, write "No amendments -- analysis is complete as stated."

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-03 -- Inertia Framing Repaired + Named Failure Modes Inline

**Axis**: Inertia framing (status quo as named stakeholder) + dedicated UX section (repairs R1 C-07 gap) + named anti-pattern labels inline at each step (C-14)
**Hypothesis**: R1 V-03 scored 95 because UX was collapsed into a Step 1 annotation. Adding a dedicated UX phase repairs C-07. Inserting named anti-patterns inline at each step -- at the exact moment the failure can occur, not in a preamble -- produces reliably distinct outputs (C-14). Inertia framing preserved: status quo row, probability-mechanism distinction in veto register, champion framed explicitly as inertia-breaker.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context Check**

Check for CODEOWNERS. If present, extract team names and owners. If absent, extract from the invocation string. If insufficient, ask exactly one question: "What org or team is this decision for?" Do not infer silently.

Anti-pattern: Skipping this step and defaulting to generic role names (PM, Eng Lead, Security) -- produces an org-chart, not a stakeholder map.

---

**Step 1 -- Strategy: Conflict Discovery**

Before placing anyone on the grid, name the conflict landscape. Answer:

1. What are at least two competing definitions of success across stakeholder groups? Each entry names both parties.
2. Which actors are structurally incentivized to delay or deprioritize this decision -- not because they oppose it, but because their incentives exclude it?
3. Which actor's scheduling or approval decision is on the critical path? State minimum lead time. Label `[CRITICAL PATH]`.

Output: conflict list (minimum two entries, format: **[Group A] vs. [Group B] -- tension**) and critical-path list (minimum one entry with lead time).

Anti-pattern: "Security team is risk-averse" -- that is one group's disposition, not a conflict between two groups. A conflict names both parties and what each wants that the other does not.

---

**Step 2 -- PM: Power/Interest Grid (Including Status Quo)**

Place stakeholders on the grid. Include **Status Quo / Do Nothing** as a named row. Its power = average of the two highest-power gatekeeper scores (inertia derives strength from gatekeeper reluctance); its interest = 1 (inertia has no interest in the outcome -- it simply persists until displaced). Quadrant: Keep Satisfied.

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Notes |
|-------------|-------------|----------------|----------|-------|
| Status Quo / Do Nothing | (calculated) | 1 | Keep Satisfied | Displaced only by explicit gatekeeper decision |
| | | | | |

Critical-path stakeholders from Step 1 carry `[CRITICAL PATH -- lead time: X]` in Notes.

Anti-pattern: Status Quo row with a high interest score -- inertia is not a motivated actor. Its power derives from gatekeeper inertia, not its own agenda. Setting interest above 2 misrepresents the mechanism.

---

**Step 3 -- UX: Experience Intersections and Segment Detection**

For each stakeholder in the Engage and Champion quadrants, identify:
- The moment in their workflow where this decision intersects their work
- Whether this group is monolithic or whether a sub-segment has substantially higher interest (power users, early adopters, blocked workflows)

Any segment split identified here should be added as a new row to the Step 2 grid.

Anti-pattern: Treating all developers or all users as a single bloc with uniform interest -- if one sub-segment is actively blocked by the status quo, their interest score differs from the broader group's. They require a separate row.

---

**Step 4 -- Veto Risk Register**

Rank strictly by probability. For each risk, state whether the mechanism is active opposition or inertia:

1. **[Stakeholder]** -- Probability: HIGH / MEDIUM / LOW. Mechanism: active-block or inertia. Impact: [consequence]. Mitigation: [concrete action with timing].

Anti-pattern: Listing risks in grid order or alphabetically -- probability rank is not the same as org hierarchy or alphabetical position. Lead with the most likely threat.

---

**Step 5 -- Champion: The Inertia Breaker**

Name the champion(s). The champion's role is to break inertia -- they must have credibility with gatekeeper-quadrant stakeholders and direct exposure to the user experience that makes the status quo painful. Give one concrete activation action tied to displacing the status quo.

Anti-pattern: "Have the dev lead champion the tool." Name the specific action: "Give [role] the live demo slot so practitioners see it working before gatekeepers can reframe it as a risk."

---

**Step 6 -- Communication Strategy**

| Quadrant | Who | Frame Type | Timing | Message: lead with this |
|----------|-----|-----------|--------|------------------------|
| Keep Satisfied | | Risk-reduction | [relative to milestone] | Why this is safer than status quo |
| Engage | | Value-demonstration | [relative to milestone] | Specific capability or outcome |
| Champion | | Activation | Now | Their motivating frame and the concrete ask |
| Inform | | Awareness | [relative to milestone] | One tool, one link, time-to-value |

The **Frame Type** column is required. Each row must carry a distinct label -- same frame across rows = FAIL.

Anti-pattern: "Keep Satisfied: highlight benefits. Engage: highlight benefits. Champion: highlight benefits." -- The frame must be distinct per quadrant because each group's concern is structurally different.

---

**Step 7 -- Amendment Phase**

For each finding, make the update -- do not only observe.

1. **Segment check**: Is any group on the grid actually two groups with different interest levels? If yes: split the row and add the new segment.
2. **Missing actors**: Is anyone downstream who is not yet represented? Add them with quadrant assignment.
3. **Gatekeeper reframe**: For any compliance or security gatekeeper, write one sentence -- "What this product does NOT do: [data it does not collect, action it does not take]." This pre-answers their likely inertia.
4. **Status Quo displacement**: Is the champion's action in Step 5 specific enough to counter the calculated power of the Status Quo row? If not, sharpen the action.

Number each amendment. Update the relevant section for each finding.

Anti-pattern: "Amendment 1: consider briefing the security team earlier" -- update the comms table timing entry and note what changed.

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-04 -- Full Combo: Reversed Sequence + All Four New Aspirational Criteria

**Axes**: Role sequence (Strategy then UX then PM validates last) + Source column required (C-11) + Amendment update mandate (C-12) + Prefilled Frame Types in comms table (C-13) + Named failure modes at each phase gate (C-14)
**Hypothesis**: R1 V-04 scored 100/100 and already contained C-11 (Source column) and C-12 (amendment update mandate) natively. Adding C-13 (prefilled Frame Type column with distinct labels per row) and C-14 (named anti-pattern at each phase gate) closes the remaining aspirational gaps. Expected score: 120/120.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Phase 0 -- Context Gate**

CODEOWNERS check: if present, load it for org structure. If absent, use the invocation string. If insufficient, ask one question: "What org or team is this decision for?" Do not proceed without org context.

Anti-pattern: Proceeding with assumed org structure -- generic roles (PM, Eng Lead, Security) produce an org-chart-shaped output, not a stakeholder map. If the invocation string names a team, product, or event, use it.

---

**Phase 1 -- Strategy Role: Conflict Landscape**

Strategy runs first. Do not map the grid yet.

Answer these questions:
1. What are at least two competing definitions of success for this decision across stakeholder groups? Each entry must name both parties.
2. Which stakeholders are structurally incentivized to resist, delay, or ignore this decision -- not because they oppose it, but because their incentives do not include it?
3. Which stakeholder's approval or scheduling decision is on the critical path? What is the minimum lead time they need before the launch milestone? Label these `[CRITICAL PATH]`.

Output: a conflict list (minimum two entries, both parties named per entry) and a critical-path list (minimum one entry with lead time).

Anti-pattern: "Security is a risk" -- this is a single-stakeholder observation, not a conflict. A conflict names two groups in tension and what each wants that the other does not.

---

**Phase 2 -- UX Role: Experience Intersections**

UX runs second. For each stakeholder group that interacts with this product or decision outcome:
- Identify the moment in their workflow where the decision lands
- Note whether that group is monolithic or whether a segment within it has substantially higher interest (early adopters, power users, blocked workflows)

Any segment split identified here feeds directly into Phase 3 as a new grid row.

Anti-pattern: A UX section that produces only one-line workflow notes with no segment observation -- large stakeholder groups almost always contain sub-segments with different interest levels. No segment finding is a signal that analysis was surface-level.

---

**Phase 3 -- PM Role: Power/Interest Grid**

PM runs last, incorporating conflicts from Phase 1 and segment data from Phase 2. The **Source** column is required -- every row must have an origin label.

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Source | Notes |
|-------------|-------------|----------------|----------|--------|-------|
| | | | | (conflict-discovered / UX-segment / initial-inventory) | |

**Source label definitions:**
- **conflict-discovered**: surfaced by Phase 1 conflict analysis
- **UX-segment**: surfaced by Phase 2 segment detection
- **initial-inventory**: from the initial landscape scan before any analytical phase

Critical-path stakeholders from Phase 1 carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: **Keep Satisfied** | **Engage** | **Champion** | **Inform**.

Anti-pattern: Every row labeled "initial-inventory" -- if conflict analysis and UX segment detection produced no new actors, one of those phases was not run seriously. The Source column makes this gap visible.

---

**Phase 4 -- Veto Risk Register**

Rank veto risks by probability. Do not follow grid order.

1. **[Stakeholder]** -- Probability: HIGH / MEDIUM / LOW. Impact: [consequence]. Mitigation: [action with timing].

Anti-pattern: Alphabetical ordering or grid ordering -- probability rank is not org hierarchy. The most likely veto leads the list.

---

**Phase 5 -- Champion Activation**

Name the champion(s). Give a concrete activation action -- specific enough to put on a calendar or assign to an owner.

Anti-pattern: "Engage the dev lead early." Give the action: "Give [role] the live demo slot at the sprint review" or "Have [role] co-present the first customer case study at the all-hands."

---

**Phase 6 -- Communication Strategy Per Quadrant**

| Quadrant | Who | Frame Type | Timing | Message: lead with this |
|----------|-----|-----------|--------|------------------------|
| Keep Satisfied | | Risk-reduction | [relative to milestone] | Why this is safer than status quo |
| Engage | | Value-demonstration | [relative to milestone] | Specific capability or outcome to show |
| Champion | | Activation | Now | Their motivating frame and the concrete ask |
| Inform | | Awareness | [relative to milestone] | One tool, one link, time-to-value |

The **Frame Type** column is required. Each row must carry a distinct type label. Same frame across rows = FAIL.

Timing must be relative to a named milestone, not an absolute date.

Anti-pattern: Four rows all framing around "highlight the value" -- Keep Satisfied stakeholders need a risk-reduction frame, not a value pitch. Their concern is structurally different from the Engage quadrant's concern.

---

**Phase 7 -- Amendment Loop (Full Revision Pass)**

This is a revision loop. For each finding, update the grid, veto list, or comms table. Do not only observe.

1. **Landscape audit**: Is any row on the grid actually two distinct segments with different interest levels? If yes: split the row, add the new row with Source = `amendment-discovery`, and note the change.
2. **Gatekeeper audit**: For every Keep Satisfied stakeholder, does the comms table frame address their actual concern? For any compliance or security gatekeeper, write one sentence: "What this product does NOT do: [data it does not collect, action it does not take]."
3. **Timeline audit**: Are the timing entries in Phase 6 correctly sequenced? Keep Satisfied stakeholders typically need to be briefed before the Engage quadrant is approached. If not, update the timing entries.
4. **Champion audit**: Is the Phase 5 action specific enough to execute? Does it name an event or an owner? If not, sharpen it.
5. **Source audit**: Review every "initial-inventory" row. Should any have been conflict-discovered or UX-segment? If so, re-source and note.

Number each amendment. For every finding that changes a section: make the change and note it.

Anti-pattern: "Amendment 1: We should consider briefing the security team earlier." -- That is an observation. Update the comms table timing entry for Keep Satisfied and write "Amendment 1: Updated Keep Satisfied timing from [day of] to [2 weeks before] -- Security Review requires lead time flagged in Phase 1 conflict analysis."

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-05 -- Conversational + Source Column + Amendment Mandate + Named Failure Modes

**Axes**: Phrasing register (imperative/conversational, second-person direct) + Source column in grid (C-11) + Amendment update mandate (C-12) + Named failure modes at each step (C-14)
**Hypothesis**: R1 V-05 scored 100/100 and already had C-13 (prefilled frame types in action-row comms table) and partial C-14 (named failure modes at C-01/C-03/C-04 steps). Adding C-11 (Source column as required grid field) and C-12 (explicit amendment update mandate -- "make the change, don't just note it") closes the remaining aspirational gaps. Named failure modes appear at the exact step where each failure can occur. Expected score: 120/120.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Check your org context first.**

Does a CODEOWNERS file exist? If yes, read it -- use it to identify who owns what. If not, look at the invocation string for org signals (team name, company, event, scope). If that's also thin, ask one question before doing anything else: "What org or team is this decision for?"

Don't guess. Don't infer silently. Anti-pattern: assuming generic roles (PM, Eng Lead, Security) when the invocation names a specific org or product -- this produces a generic org-chart, not a map of this decision's stakeholders.

---

**Map the stakeholders.**

Use three lenses:
- **PM lens**: who has power over this decision, and who cares about the outcome?
- **Strategy lens**: where do stakeholder interests collide? Name the tension, not just the person.
- **UX lens**: which stakeholders interact with the product in their workflow -- and is any large group actually two groups with different levels of interest?

Build the grid. The **Source** column is required -- every row must have an origin label:

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Source | Flag |
|-------------|-------------|----------------|----------|--------|------|
| | | | | (conflict-discovered / UX-segment / initial-inventory) | |

For the **Flag** column: mark `CRITICAL PATH -- [lead time]` for any stakeholder whose approval or scheduling blocks the launch timeline regardless of their support. Leave blank otherwise.

Anti-pattern: Every row says "initial-inventory" -- a grid full of initial-inventory rows means conflict analysis and UX segment detection surfaced nothing, which is almost never accurate. The source column makes this gap visible.

---

**Name the conflicts.**

List at least two. Each entry must name both parties and the tension:

- **[Group A] vs. [Group B]**: [what each wants that the other doesn't]

Anti-pattern: "Security team resists change" -- that is one group's disposition. Name the second group they are in tension with and what competing outcome each is optimizing for. A single stakeholder's risk is not a conflict.

---

**Rank the veto risks.**

Order strictly by probability -- most likely threat first:

1. **[Stakeholder]** -- Probability: HIGH / MEDIUM / LOW. What happens if this materializes: [consequence]. What to do about it: [concrete action + when].

Anti-pattern: Listing in the same order as the grid gives an org-hierarchy-shaped risk register, not a probability-shaped one. Don't alphabetize. Don't follow grid order.

---

**Activate the champion.**

Name the champion. Give one specific action -- something you can put on a calendar or assign to an owner:

"Give [role] the live demo slot at the sprint review."
"Have [role] co-present the first customer case study at the all-hands."

Anti-pattern: "Engage the dev lead" -- generic engagement instructions cannot be added to a project plan as a task. If the action cannot be assigned to a person with a date or event, it is not specific enough.

---

**Build the communication plan.**

Every row is an action. Timing is relative to a milestone. Frame Type is distinct per row.

| Quadrant | Who | Frame Type | Action | Timing | Message: lead with this |
|----------|-----|-----------|--------|--------|------------------------|
| Keep Satisfied | | Risk-reduction | Brief them: [channel + format] | [before milestone] | Why this is safer than status quo |
| Engage | | Value-demonstration | Demo to them: [format] | [relative to milestone] | Specific capability or outcome |
| Champion | | Activation | [specific activation action] | Now | Their motivating frame and the concrete ask |
| Inform | | Awareness | [channel + format] | [relative to milestone] | One tool, one link, time-to-value |

Anti-pattern: Every row labeled "Value-demonstration" -- each quadrant's concern is structurally different. Risk-reduction for Keep Satisfied is not the same frame as value-demonstration for Engage. Same Frame Type across rows = FAIL.

---

**Check your work -- amendment pass.**

For each finding: make the update, then note what changed. Don't only observe.

- Is any group on the grid actually two groups with different interest levels? If yes: split the row, add the new segment with Source = `UX-segment`, update the comms table.
- Is there anyone downstream who should be on the grid but isn't? Add them with Source = `amendment-discovery`.
- For any compliance or security gatekeeper: write one sentence -- "What this product does NOT do: [data it doesn't collect, action it doesn't take]." This pre-answers their likely question before the review starts.
- Are timing entries sequenced correctly? Keep Satisfied stakeholders usually need briefing before the Engage quadrant is approached. If not, update the timing entries.
- Review every "initial-inventory" row -- should any have been conflict-discovered or UX-segment? Re-source and note.

Number each amendment. Anti-pattern: "Amendment 1: We should brief the security team earlier" -- that is an observation, not a revision. Update the comms table timing entry for Keep Satisfied and write: "Amendment 1: Updated Keep Satisfied timing from [day of] to [2 weeks before] -- Security Review requires lead time identified in conflict analysis."

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`
