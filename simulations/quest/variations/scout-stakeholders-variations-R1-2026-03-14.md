Written to `simulations/quest/variations/scout-stakeholders-variations-R1-2026-03-14.md`.

---

## Summary

**5 variations, 3 single-axis + 2 combo:**

| ID | Axis | Hypothesis |
|----|------|-----------|
| **V-01** | Role sequence: Strategy first | Conflict discovery before grid placement reduces org-chart-default bias; C-06/C-08 should improve |
| **V-02** | Output format: prose narrative wraps tables | Explicit prose between sections forces reasoning gaps to surface; C-06/C-09 gain depth at scanability cost |
| **V-03** | Inertia framing: status quo as named row | Treating "do nothing" as a calculated stakeholder forces veto ranking to be probability-first and champion action to be inertia-breaking; C-03/C-04 sharpen |
| **V-04** | Role sequence reversed + heavy amendment loop | PM validates last after Strategy+UX; amendment phase is a full second pass with 4 named audits; best coverage of C-07/C-09 |
| **V-05** | Conversational register + action-row tables | Every row contains a verb; imperative phrasing eliminates decorative language; C-04/C-05 produce calendar-ready outputs directly |

**Rubric coverage prediction per variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 CODEOWNERS fallback | + | + | + | + | + |
| C-02 Power/Interest grid | + | + | + | + | + |
| C-03 Veto risks ranked | + | + | ++ | + | ++ |
| C-04 Champion concrete action | + | + | ++ | + | ++ |
| C-05 Comms strategy per quadrant | + | + | + | + | ++ |
| C-06 Conflicts | ++ | ++ | + | ++ | + |
| C-07 Role framing | + | + | + | ++ | + |
| C-08 Critical-path gatekeepers | ++ | ++ | + | ++ | + |
| C-09 Amendment phase | + | ++ | + | ++ | + |
| C-10 Negative-space framing | + | + | + | ++ | + |

`++` = design change specifically targets this criterion. Scoring will verify.
s: **[Stakeholder A] vs. [Stakeholder B] — nature of tension**. Require at least two distinct conflicts. A single stakeholder's risk is not a conflict.

Separately: identify any stakeholder whose scheduling or approval decision constrains the launch timeline (critical-path gatekeepers). For each, note the lead-time required (e.g., "Security Review must begin at least 2 weeks before slot confirmation").

---

**Step 2 — PM Role: Power/Interest Grid**

Using the conflicts identified in Step 1 as constraints, place each stakeholder in a power/interest grid. Power = ability to stop or accelerate the decision. Interest = degree to which this decision affects them or they care about the outcome.

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Notes |
|-------------|-------------|----------------|----------|-------|
| ...         | ...         | ...            | ...      | ...   |

Quadrant labels: **Keep Satisfied** (high power, low interest), **Engage** (high power, high interest), **Champion** (lower power, high interest), **Inform** (low power, low interest).

Flag any stakeholder identified in Step 1 as a critical-path gatekeeper with `[CRITICAL PATH]` in the Notes column, with the lead-time constraint.

---

**Step 3 — UX Role: Journey Implications**

For each stakeholder in the Engage and Champion quadrants, identify the experience-path concern: what moment in their workflow does this decision intersect, and what friction or benefit does it introduce? One sentence per stakeholder is sufficient. If a stakeholder's journey implies a segment split (e.g., bulk users vs. early adopters), call it out here.

---

**Step 4 — PM Role: Veto Risks Ranked by Probability**

List veto risks in descending probability order. Format:

1. **[Stakeholder]** — Probability: HIGH/MEDIUM/LOW. Impact if triggered: [consequence]. Mitigation: [concrete action].

Do not list in grid order or alphabetical order. Rank strictly by probability of the veto materializing. Include at least the top three.

---

**Step 5 — Champion Activation**

Identify the stakeholder(s) most likely to advocate for this decision. For each champion:

- Name them explicitly.
- Give a single concrete activation action — not "engage" or "build relationship," but a specific action (e.g., "give them the live demo slot," "co-present at the all-hands," "grant early access before the announcement").

---

**Step 6 — Communication Strategy Per Quadrant**

| Quadrant | Who | Timing | Message Frame |
|----------|-----|--------|---------------|
| Keep Satisfied | ... | ... | ... |
| Engage | ... | ... | ... |
| Champion | ... | ... | ... |
| Inform | ... | ... | ... |

Timing must be relative to a milestone (e.g., "3 weeks before event," "now," "day of launch"). Message Frame must be distinct per quadrant — do not repeat the same frame.

---

**Step 7 — Amendment Phase**

After completing the grid and strategy, review your analysis for what was not initially obvious. Look for:

- A stakeholder group that should be split into distinct segments with different interest levels
- A missing actor who is downstream of someone already on the grid
- A reframe required for a gatekeeper (e.g., the message that will reduce their review friction)
- For any compliance or security gatekeeper: write one sentence describing what this product does NOT do (data it does not collect, actions it does not take) to pre-answer their likely objection

List each amendment as a numbered finding. If no amendments are warranted, say so explicitly.

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-02 — Output Format: Prose Narrative with Embedded Tables

**Axis**: Output format — prose narrative wraps all tables, reasoning is explicit between sections
**Hypothesis**: Forcing the model to articulate reasoning in prose between each section improves conflict identification (C-06) and amendment discovery (C-09) by preventing silent grid-filling. Cost is scanability; gain is analytical depth.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Org Context Check**

First, determine the org context. Look for a CODEOWNERS file; if found, use it to identify teams and decision owners. If no CODEOWNERS exists, extract the org structure from the invocation string. If neither source provides sufficient context, ask exactly one question: "What org or team is this decision for?" Never infer silently.

---

**Stakeholder Map**

Begin with a brief narrative paragraph identifying who has a stake in this decision. Name the roles: PM is responsible for mapping power and interest accurately. Strategy is responsible for identifying where stakeholder interests conflict. UX is responsible for identifying where this decision intersects stakeholder workflows and experience paths.

Once the landscape is named in prose, populate the grid:

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant |
|-------------|-------------|----------------|----------|

After the table, write a paragraph explaining the two or three most consequential placements — specifically, any stakeholder whose placement surprised you or whose power/interest combination creates a structural risk. This paragraph must name at least two conflicts: pairs of stakeholders optimizing for different outcomes, in tension with each other.

---

**Critical-Path Analysis**

Write a paragraph identifying any stakeholder whose scheduling or approval decision can block the launch timeline independent of whether they support the decision in principle. For each such stakeholder, state the lead time required. These are critical-path gatekeepers — they do not appear in the grid differently, but they operate on a separate timeline that must be managed in parallel.

---

**Veto Risk Register**

Write a paragraph framing the veto landscape, then provide the ranked list:

1. **[Stakeholder]** — Probability: HIGH/MEDIUM/LOW. Impact: [consequence]. Mitigation: [concrete action with timing].

Order is strictly by probability, not grid order. After the list, write one sentence explaining why the top-ranked veto is ranked first (not just what it is, but why it is highest probability given the context).

---

**Champion Identification**

Name the champion(s) in prose. Explain why they are positioned to advocate — what is their interest, and why does their advocacy carry weight with the Engage or Keep Satisfied quadrant stakeholders? Then give the concrete activation action: not a general instruction to engage, but a specific action (e.g., "give them the live demo slot," "have them co-present the first case study").

---

**Communication Strategy**

Introduce the strategy in one sentence, then provide the quadrant table:

| Quadrant | Who | Timing | Message Frame |
|----------|-----|--------|---------------|
| Keep Satisfied | | | |
| Engage | | | |
| Champion | | | |
| Inform | | | |

After the table, write a paragraph noting any timing dependencies between quadrants — specifically, whether the Keep Satisfied stakeholders must be briefed before the Engage quadrants are approached (sequencing risk).

---

**Amendments**

After completing the analysis, review for what was not initially obvious. Write each amendment in prose:

- Did any stakeholder group need to be split into segments with distinct interest levels? Name the split.
- Was any actor missing from the initial landscape? Name them and their quadrant.
- Does any gatekeeper require a "what we are NOT doing" framing to reduce review friction? Write that framing here.

If no amendments arise, write "No amendments — analysis is complete as stated."

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-03 — Inertia Framing: Status Quo as Named Stakeholder

**Axis**: Inertia framing — "do nothing / status quo" treated as an explicit stakeholder row
**Hypothesis**: Making the status quo a named stakeholder forces veto risks to be expressed as probability-ranked responses to an active competitor (inertia), rather than passive observations. C-03 (veto risks ranked by probability) and C-04 (champion concrete action) should improve because the champion's activation is now explicitly framed as countering inertia.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 — Org Context**

Check for CODEOWNERS. If present, extract org structure. If absent, extract from invocation string. If insufficient, ask: "What org or team is this decision for?" Do not infer silently.

---

**Step 1 — Stakeholder Grid (Including Status Quo)**

Map all stakeholders to the power/interest grid. Include **Status Quo / Do Nothing** as a named row. Its power score equals the average power of the two highest-power gatekeepers (inertia derives its strength from the gatekeepers who benefit from not deciding). Its interest score is 1 (inertia has no interest in the outcome — it simply persists unless displaced).

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Notes |
|-------------|-------------|----------------|----------|-------|
| Status Quo / Do Nothing | (calculated) | 1 | Keep Satisfied | Displaced only by explicit gatekeeper decision |
| ...         | ...         | ...            | ...      | ...   |

Roles applied:
- **PM**: places each stakeholder on the grid
- **Strategy**: identifies where stakeholder interests conflict with each other and with the status quo
- **UX**: identifies journey friction that makes the status quo actively painful for users (this is what the champion will deploy)

Flag any stakeholder whose scheduling or approval constrains the timeline with `[CRITICAL PATH — lead time: X]` in Notes.

---

**Step 2 — Conflicts**

List at least two conflicts between stakeholder groups. Format: **[Group A] vs. [Group B] — tension**. The status quo row may appear in a conflict (e.g., "Architects (skeptic cluster) vs. Dev Lead — skeptics reinforce status quo by withholding endorsement"). Single-stakeholder risks do not count.

---

**Step 3 — Veto Risks Ranked by Probability**

Rank by probability of the veto materializing. For each risk, state whether the status quo is the mechanism (i.e., the veto is "they do not decide" rather than "they actively block"):

1. **[Stakeholder]** — Probability: HIGH/MEDIUM/LOW. Mechanism: [active block or inertia]. Impact: [consequence]. Mitigation: [concrete action with timing].

---

**Step 4 — Champion: The Inertia Breaker**

Identify the champion(s). The champion's role is specifically to break inertia — they must have credibility with the gatekeeper quadrant and direct access to the user experience that makes the status quo painful. Give a concrete activation action tied to displacing the status quo (e.g., "give them the demo slot so developers see the tool working before gatekeepers can reframe it as a risk").

---

**Step 5 — Communication Strategy Per Quadrant**

| Quadrant | Who | Timing | Message Frame |
|----------|-----|--------|---------------|
| Keep Satisfied | ... | ... | Risk profile: why this is safer than status quo |
| Engage | ... | ... | ... |
| Champion | ... | ... | ... |
| Inform | ... | ... | ... |

For Keep Satisfied stakeholders, the message frame must explicitly address why the proposed change is lower risk than the status quo. Timing must be relative to a milestone.

---

**Step 6 — Amendment Phase**

Review the analysis for:
- Any stakeholder group that should be split (bulk vs. early-adopter segment with different interest levels)
- Any missing actor who is downstream and not yet represented
- For any compliance or security gatekeeper: one sentence on what this product does NOT do, to reduce their inertia and review friction

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-04 — Combo: Role Sequence Reversed + Explicit Phase Gates with Heavy Amendment

**Axes**: Role sequence (PM last, validates after Strategy + UX) + Lifecycle emphasis (amendment phase is a full analysis loop, not an afterthought)
**Hypothesis**: Running PM last (as validator rather than initiator) forces the grid to reflect insights from Strategy and UX first, reducing default org-chart bias. Treating the amendment phase as a full second loop — not a checklist — produces the richest C-09 findings and best C-07 coverage.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Phase 0 — Context Gate**

CODEOWNERS check: if present, load it for org structure. If absent, use the invocation string. If insufficient, ask one question: "What org or team is this decision for?" Do not proceed without org context.

---

**Phase 1 — Strategy Role: Conflict Landscape**

Strategy runs first. Do not map the grid yet.

Answer these questions:
1. What are the competing definitions of success for this decision across stakeholder groups? (At least two distinct framings.)
2. Which stakeholders are structurally incentivized to resist, delay, or ignore this decision — not because they oppose it, but because their incentives do not include it?
3. Which stakeholder's approval or scheduling decision is on the critical path? What is the minimum lead time they need before a launch milestone? Label these `[CRITICAL PATH]`.

Output: a conflict list (minimum two entries, each naming both parties in tension) and a critical-path list (minimum one entry with lead time).

---

**Phase 2 — UX Role: Experience Intersections**

UX runs second. For each stakeholder group that will interact with this product or decision outcome:
- Identify the moment in their workflow where the decision lands.
- Note whether that group is monolithic or whether a segment within it has substantially higher interest (early adopters, power users, blocked workflows).

Any segment split identified here feeds directly into Phase 3.

---

**Phase 3 — PM Role: Power/Interest Grid**

PM runs last, incorporating the conflict and segment data from Phases 1-2. Place each stakeholder (including any segments split out in Phase 2) on the grid.

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Source |
|-------------|-------------|----------------|----------|--------|
| ...         | ...         | ...            | ...      | (Phase 1 conflict / Phase 2 segment / initial) |

The Source column tracks where each row originated — initial inventory, conflict analysis, or UX segment discovery. Gatekeepers flagged `[CRITICAL PATH]` in Phase 1 carry that tag into Notes with their lead-time constraint.

---

**Phase 4 — Veto Risk Register**

Rank veto risks by probability. Do not follow grid order.

1. **[Stakeholder]** — Probability: HIGH/MEDIUM/LOW. Impact: [consequence]. Mitigation: [action with timing].

---

**Phase 5 — Champion Activation**

Name the champion(s). Give a concrete activation action (not "engage"). The action should be specific enough to put on a calendar.

---

**Phase 6 — Communication Strategy Per Quadrant**

| Quadrant | Who | Timing | Message Frame |
|----------|-----|--------|---------------|
| Keep Satisfied | | | |
| Engage | | | |
| Champion | | | |
| Inform | | | |

Timing is relative to a named milestone. Message Frame is distinct per quadrant.

---

**Phase 7 — Amendment Loop (Full Second Pass)**

This is not a checklist. Run a second pass over the full analysis:

1. **Landscape audit**: Is any stakeholder missing? Is any group that appears as one row actually two distinct segments (different interest level, different message needed)?
2. **Gatekeeper audit**: For every Keep Satisfied stakeholder, ask: does the current communication strategy actually address their concern? If a compliance or security gatekeeper is present, write the "what we are NOT doing" framing — one sentence stating what data the tool does not collect or what action it does not take.
3. **Timeline audit**: Are the timing entries in Phase 6 sequenced correctly? Is there a dependency where Keep Satisfied must be briefed before Engage is approached?
4. **Champion audit**: Is the concrete action in Phase 5 specific enough to execute? Does it need a named owner or a named event?

Output each amendment as a numbered finding. If a finding changes the grid (adds a row, splits a row, re-ranks a veto), make the change and note it.

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`

---

## V-05 — Combo: Conversational Register + Action-Row Table Format

**Axes**: Phrasing register (imperative/conversational, second-person direct) + Output format (every table row is an action, not a label)
**Hypothesis**: Imperative register eliminates decorative language ("consider engaging," "may want to brief") and forces every row to contain a verb. Action-row tables produce directly executable outputs for C-04 (champion concrete action) and C-05 (communication strategy) without requiring post-processing.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Check your org context first.**

Does a CODEOWNERS file exist? If yes, read it — use it to identify who owns what. If not, look at the invocation string for org signals (team name, company, event, scope). If that's also thin, ask one question before doing anything else: "What org or team is this decision for?" Don't guess. Don't infer silently.

---

**Map the stakeholders.**

Use three lenses:
- **PM lens**: who has power over this decision, and who cares about the outcome?
- **Strategy lens**: where do stakeholder interests collide? Name the tension, not just the person.
- **UX lens**: which stakeholders interact with the product in their workflow, and is any large group actually two groups with different levels of interest?

Build the grid:

| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Flag |
|-------------|-------------|----------------|----------|------|

For the Flag column: mark `CRITICAL PATH — [lead time]` for any stakeholder whose approval or scheduling blocks the launch timeline regardless of their support. Leave blank otherwise.

---

**Name the conflicts.**

List at least two conflicts. Each entry must name both parties and the nature of the tension:

- **[Group A] vs. [Group B]**: [what they want that the other doesn't]

A single stakeholder's risk is not a conflict. Two groups optimizing for different outcomes is.

---

**Rank the veto risks.**

Order strictly by probability. Start with the most likely veto:

1. **[Stakeholder]** — Probability: HIGH/MEDIUM/LOW. What happens if this materializes: [consequence]. What to do about it: [concrete action + when].

Don't alphabetize. Don't follow grid order. Lead with the most probable threat.

---

**Activate the champion.**

Name the champion. Then give one specific action — something you can put on a calendar. Not "engage the dev lead." Something like: "Give [name/role] the live demo slot at the all-hands" or "Have [name/role] co-present the first customer case study." If there are two champions, give one action per champion.

---

**Build the communication plan.**

Every row is an action. Timing is relative to a milestone. Message frame is distinct per row.

| Quadrant | Who | Action | Timing | Message: lead with this |
|----------|-----|--------|--------|------------------------|
| Keep Satisfied | | Brief them: [how] | | Risk frame: [specific concern to address] |
| Engage | | Demo to them: [format] | | Value frame: [specific capability to show] |
| Champion | | [specific activation action] | Now | [their motivating frame] |
| Inform | | [channel + format] | | One tool, one link, [time to value] |

---

**Check your work — amendment pass.**

Before finalizing, ask:
- Is any large group on the grid actually two groups? (One with low interest, one with high interest who needs a different action.) If yes, split the row and add the new segment.
- Is there anyone downstream who should be on the grid but isn't? Add them.
- For any compliance or security gatekeeper: write one sentence — "What this product does NOT do: [data it doesn't collect, action it doesn't take]." This pre-answers their likely question before the review starts.
- Are all timing entries sequenced correctly? (Keep Satisfied stakeholders usually need to be briefed before the Engage quadrant is approached.)

List each change as a numbered amendment. If nothing changes, say "No amendments."

---

Write the output to: `simulations/scout/stakeholders/{{topic}}-stakeholders-{{date}}.md`
