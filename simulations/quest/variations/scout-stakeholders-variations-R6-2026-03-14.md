`simulations/quest/variations/scout-stakeholders-variations-R6-2026-03-14.md` written.

---

## Round 6 -- scout-stakeholders -- Design Summary

| ID | Axis | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | Expected |
|----|------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:--------:|
| V-01 | C-20 alone -- prefill-stage inertia binding | - | - | - | ++ | ++ | ++ | - | ~135 |
| V-02 | C-21 alone -- amendment prefill round-trip | - | ++ | - | - | ++ | - | ++ | ~135 |
| V-03 | Phrasing register: conversational/coaching | - | - | - | - | - | - | - | ~120 |
| V-04 | C-20 + C-21 combined | - | ++ | - | ++ | ++ | ++ | ++ | ~145 |
| V-05 | Full seven-axis (155/155 attempt) | ++ | ++ | ++ | ++ | ++ | ++ | ++ | 155 |

---

**Three single-axis tests, then combine:**

**V-01 (C-20 alone)** — Scaffolds C-18 and C-19 as required dependencies, then adds the C-20 distinction: the `displacement-acknowledgment` assignment is stated as rule 3 *within* Step 6a, with `FAIL_MISSING_DISPLACEMENT_PREFILL` at the prefill gate before any row content is written. Amendment example updates grid, veto, and content rows only — no Step 6a revision (C-21 absent). Standard PM-first (C-15 absent). Positive instruction only, no bad-form pair (C-16 absent). Amendment step has no inline FAIL label (C-17 absent). Expected: ~135/155.

**V-02 (C-21 alone)** — Scaffolds C-16 and C-19 as required dependencies, then adds C-21: the correct-form amendment example shows the Step 6a prefill table reassigned first, then the Step 6b content row updated to match. No dedicated inertia sub-step (C-18 absent); Step 6a has accepted-values list but no inertia-specific mandate (C-20 absent). Standard sequence. Incomplete gate coverage. Expected: ~135/155.

**V-03 (Conversational register)** — All essential + recommended + C-09 through C-14 in a coaching/guidance voice. PM/Strategy/UX role labels present in section headings. Frame Types enumerated inline — no separate prefill step. Two inline warnings at specific steps (C-14 passes), most steps carry none. Baseline reference: expected ~120/155.

**V-04 (C-20 + C-21 combined)** — Adds both new axes on top of C-16 + C-18 + C-19 scaffolding. C-20: Step 5a rule 3 mandates inertia assignment at the prefill gate with `FAIL_MISSING_DISPLACEMENT_PREFILL`. C-21: correct-form in Step 7 shows Step 5a prefill update + Step 5b content update. Standard sequence (C-15 absent). UX and champion steps carry no FAIL labels (C-17 absent). Expected: ~145/155.

**V-05 (Full seven-axis)** — Restates R5-V-05's structure as the R6 canonical prompt, with C-20 and C-21 made explicit: Step 6a rule 3 mandates the inertia assignment at the prefill gate; the Step 8 correct-form shows the full round-trip (Step 6a prefill reassigned, then Step 6b content row updated). All seven axes in distinct structural positions. Expected: 155/155.
only with no bad-form pair (fails C-16). Standard sequence (fails C-15). Sparse FAIL coverage -- two inline warnings present at specific steps (passes C-14), but multiple steps carry none (fails C-17). No dedicated inertia sub-step (fails C-18). Baseline reference for whether register variation affects essential/recommended criteria. Expected: ~120/155.

**V-04 (C-20 + C-21 combined)** -- Scaffolds C-16 + C-18 + C-19 as structural requirements, then places both new v6 criteria: C-20 (displacement mandate as explicit rule in the prefill step, FAIL_MISSING_DISPLACEMENT_PREFILL at the prefill gate) and C-21 (correct-form amendment example shows Step 6a prefill update followed by Step 6b content-row update). Standard sequence (fails C-15). UX and champion steps carry no inline FAIL label, giving incomplete gate coverage (fails C-17). Tests independence of C-20 and C-21 at ~145/155.

**V-05 (Full seven-axis, 155/155 attempt)** -- Builds on R5-V-05's confirmed five-axis structure (C-15, C-16, C-17, C-18, C-19), reinforcing the two v6 criteria that R5-V-05 already satisfied: C-20 (Step 6a rule 3 mandates `displacement-acknowledgment` for the inertia quadrant at the prefill gate with FAIL_MISSING_DISPLACEMENT_PREFILL before any row content is written) and C-21 (the correct-form amendment in Step 8 updates the Step 6a prefill table -- Frame Type reassigned -- then updates the Step 6b content row as a complete round-trip). All seven axes occupy distinct structural positions. If this reaches 155/155, all seven axes are compatible.

---

## V-01 -- C-20 Alone: Prefill-Stage Inertia Binding

**Axes**: Inertia three-position elevation (C-18) + standalone Frame Type prefill table (C-19) + displacement mandate stated as explicit rule within the prefill step (C-20)
**Hypothesis**: C-20 is a stable single-axis addition at ~135/155. The key distinction from R5-V-01 (C-18 alone, 125/145): R5-V-01 had the displacement-acknowledgment mandate as an inline note in the communications content step. V-01 here moves it upstream to a numbered rule in the prefill step -- the assignment must be made in Step 6a, before any row content is written, and FAIL_MISSING_DISPLACEMENT_PREFILL fires at the prefill gate. The amendment example updates grid and content rows only; it does not return to Step 6a (C-21 absent). Standard PM-first sequence (C-15 absent). Positive amendment instruction only -- no bad-form example (C-16 absent). Amendment step carries no inline FAIL label -- not every gate covered (C-17 absent).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as the initial stakeholder inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question:

> "What org or team is this decision for?"

Do not infer org structure. Do not proceed on an assumed context. This gate comes before all other steps.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the highest-consequence failure in this skill. A wrong org assumption means every downstream step is built on fiction.

---

**Step 1 -- Stakeholder Inventory and Grid**

Scan available context for all stakeholders. Build the Power/Interest grid. Every inertia stakeholder identified in Step 1b must appear with `[INERTIA]` in the designated column.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Quadrant labels**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Step 2
- `segment-analysis`: surfaced in Step 3
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during Step 8

The `[INERTIA]` column is a required structural marker -- not a Notes annotation. Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 1b appearing without `[INERTIA]` in the designated column is an incomplete row.

---

**Step 1b -- Inertia Stakeholder Mapping**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` (their process changes) | `political` (their standing diminishes) | `ownership` (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

These stakeholders track through three downstream positions: `[INERTIA]` tag in Step 1's grid, a ranked entry in Step 4's veto list, and `displacement-acknowledgment` assigned in Step 6a's prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step propagates to two downstream structural gaps -- `[INERTIA]` absent from the grid and `displacement-acknowledgment` not assigned in Step 6a.

---

**Step 1c -- Critical-Path Gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

**Step 2 -- Conflict Identification**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required.

---

**Step 3 -- UX Segment Analysis**

For each user segment:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. **NOT-doing statement**: what this product explicitly does not provide for this segment

For `[INERTIA]` stakeholders: the NOT-doing statement must address what the new approach does not preserve from the current approach.

If a sub-segment has substantially higher interest or distinct friction, split it. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6a -- Frame Type Prefill**

Before writing any row content in the communication table, complete this assignment table.

| Quadrant | Frame Type |
|----------|------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

**Accepted values -- only values from this list may appear in the communication table:**
- `displacement-acknowledgment`
- `risk-mitigation`
- `value-capture`
- `compliance-alignment`
- `awareness-only`
- `co-ownership`

**Assignment rules:**
1. Assign one value per row.
2. No two rows may share the same Frame Type.
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. Make this assignment here, in the prefill step, before any content is written in Step 6b. Do not defer this assignment to the content population step.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and comply with the rules above.
5. Values not in the accepted list are prohibited.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the quadrant containing an `[INERTIA]` stakeholder is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. This assignment must be made at the prefill stage -- a corrective change made during row population in Step 6b does not satisfy this requirement.

---

**Step 6b -- Communication Table**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing.

Timing must include a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder from Step 1c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment Pass**

Review Steps 1-7. Run one amendment pass. Minimum one amendment required.

For every amendment:
1. Update the affected table (grid, veto list, or comms table) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag `[INERTIA]` in Step 1, and check whether Step 6a assignments need revision before updating Step 6b
4. State what triggered the finding and which prior step surfaced it
5. State what changed from the initial map

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Step 2 or Step 3 may be incomplete. Note them explicitly.

---

## V-02 -- C-21 Alone: Amendment Prefill Round-Trip

**Axes**: Adjacent before/after amendment pair (C-16) + standalone Frame Type prefill table (C-19) + amendment correct-form example shows prefill table update alongside content-row update (C-21)
**Hypothesis**: C-21 is a stable single-axis addition at ~135/155. The key structural requirement: the correct-form half of the amendment pair must show two simultaneous updates -- first, the Step 6a prefill table is revised (Frame Type reassigned for a quadrant), then the Step 6b content row is updated to match. A correct-form example that shows only the Step 6b content-row update without a corresponding Step 6a prefill reassignment fails C-21. No dedicated inertia sub-step (C-18 absent); the Step 6a prefill table has an accepted-values list but carries no rule mandating `displacement-acknowledgment` for any specific quadrant (C-20 absent). Standard sequence (C-15 absent). UX and champion steps carry no inline FAIL label (C-17 absent).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as the initial stakeholder inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question:

> "What org or team is this decision for?"

Do not infer org structure silently. This gate precedes all analysis.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill.

---

**Step 1 -- Stakeholder Grid**

Scan for all stakeholders and build the Power/Interest grid.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Quadrant labels**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Every row requires a Source label: `CODEOWNERS`, `conflict-discovered`, `segment-analysis`, `initial-inventory`, or `amendment`. Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry.

**FAIL_PROSE_ONLY**: A prose list without a grid table does not satisfy the grid requirement.

---

**Step 2 -- UX Segment Analysis**

For each user segment:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. **NOT-doing statement**: what this product explicitly does not provide for this segment

If a group is not monolithic, split it. New rows carry Source = `segment-analysis`.

---

**Step 3 -- Conflict Identification**

Identify at least two structural conflicts. For each:

> **[Group A] vs. [Group B] -- [resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder concern is not a conflict. Two named parties required.

---

**Step 4 -- Veto Risk Ranking**

Order veto risks by probability -- highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order.

**FAIL_NO_MITIGATION**: A veto risk without mitigation is an observation, not a risk plan.

---

**Step 5 -- Champion**

Name one or more champions with a specific, schedulable action per champion.

---

**Step 6a -- Frame Type Prefill**

Before writing any row content in the communication table, complete this assignment table.

| Quadrant | Frame Type |
|----------|------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

**Accepted values -- only values from this list may appear in the communication table:**
- `displacement-acknowledgment`
- `risk-mitigation`
- `value-capture`
- `compliance-alignment`
- `awareness-only`
- `co-ownership`

Assign one value per row. No two rows may share the same Frame Type. Do not proceed to Step 6b until all four assignments are complete, distinct, and drawn from the accepted-values list.

**FAIL_SAME_FRAME**: Two rows with the same Frame Type means the prefill was not completed correctly. Return here before populating rows.

---

**Step 6b -- Communication Table**

Using the Frame Types from Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If an assigned Frame Type feels wrong for a row, return to Step 6a and reassign before continuing.

Timing must include a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks out".

**FAIL_VAGUE_TIMING**: Timing without a quantified unit fails.

---

**Step 7 -- Critical-Path Gatekeepers**

For each critical-path stakeholder:
- Blocking reason (specific)
- Minimum lead time or hard deadline

Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_GATEKEEPER_INCOMPLETE**: Both blocking reason and timing required.

---

**Step 8 -- Amendment Pass**

Review Steps 1-7. Run one amendment pass. Minimum one amendment required.

**Read both forms before proceeding:**

**Bad form** (do not do this):
> "The Compliance team may have approval authority over data classification policies. This is worth following up before launch."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Compliance added (Keep Satisfied, H power / H interest, Source: amendment). Veto list updated -- data classification veto added at High probability, ranked above existing Medium risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Step 3 conflict between Engineering and Legal surfaced an undisclosed sign-off dependency. What changed: Compliance was absent from initial-inventory; conflict analysis surfaced the gap.

For every amendment:
1. Update the affected table (grid, veto list, Step 6a prefill, or Step 6b comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment changes a quadrant's stakeholder composition, return to Step 6a and confirm the Frame Type assignment is still appropriate for that quadrant; if not, reassign in Step 6a first, then update Step 6b to match
4. State what triggered the finding and which prior step surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment.

After all amendments, audit any remaining `initial-inventory` rows. Unclassified rows signal incomplete conflict or segment analysis.

---

## V-03 -- Phrasing Register: Conversational/Coaching

**Axes**: Phrasing register (conversational/instructive voice throughout; guidance framing rather than gated rules)
**Hypothesis**: A coaching register can satisfy all essential and recommended criteria, and aspirational C-09 through C-14, without the structural enforcement language introduced by C-15 through C-21. If it scores ~120/155, the register shift is neutral to the criteria it targets. If it underperforms, register is interfering with C-02, C-03, C-05, or a recommended criterion. Standard PM-first sequence (C-15 absent). Frame Types enumerated inline in instructions -- not a separate prefill step (C-19 absent, C-20/C-21 absent). No bad-form pair (C-16 absent). Two inline warnings present at specific steps (C-14 passes), but most steps carry none (C-17 absent). No dedicated inertia sub-step (C-18 absent).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Checking org context first -- PM role**

Your first move is to look for a CODEOWNERS file. If you find one, pull team names and owners out of it as your initial stakeholder list, labeling each Source = `CODEOWNERS`. If there's no CODEOWNERS file, look at how the skill was invoked -- sometimes the topic or invocation string carries enough org context to get started. If you genuinely can't tell what org or team this decision is for, ask one question before going any further:

> "What org or team is this decision for?"

Don't try to guess. One clarifying question costs almost nothing; proceeding on the wrong org assumption means everything you build from here is solving the wrong problem.

---

**Building the stakeholder grid -- PM role**

With your initial inventory in hand, construct a Power/Interest grid. For each stakeholder, assign Power (H/M/L), Interest (H/M/L), and a quadrant:

- **Manage Closely** -- high power, high interest
- **Keep Satisfied** -- high power, lower interest
- **Keep Informed** -- lower power, high interest
- **Monitor** -- lower power, lower interest

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

For every row, record where this stakeholder came from. Use: `CODEOWNERS`, `conflict-discovered`, `segment-analysis`, or `initial-inventory`. A row without a source is harder to audit later.

Aim for at least four rows. A prose list of names without the grid structure doesn't give you the quadrant view you need for the communication strategy.

---

**Finding the structural conflicts -- Strategy role**

Look for places where stakeholder groups are in real tension with each other. You need at least two conflicts -- not just concerns one stakeholder has, but two named parties in genuine tension:

> **[Group A] vs. [Group B] -- [resource | priority | scope | process | compliance]**

For each conflict, flag whether it carries veto potential. This matters for the ranking step.

---

**Mapping user segments -- UX role**

For each group of users touched by this decision, think through four things:

1. What's their role or use pattern?
2. What do they gain if this decision goes forward?
3. What becomes harder or worse for them?
4. What is this product *not* doing for this group? Be specific -- "does not preserve bulk-export workflows for this team" is useful; "general scope limitations apply" is not.

Before moving on, check whether any group you've listed is really two groups wearing the same label. If a sub-segment has meaningfully different interest levels or distinct friction points, split them into separate rows with Source = `segment-analysis`.

> (Note: treating every entry as one undifferentiated group is the most common mapping error here -- a communication strategy built for a monolith will miss the sub-segment with the real friction.)

---

**Ranking the veto risks -- Strategy role**

Which stakeholders could actually block this decision if they chose to? List them, ordered by probability -- most likely to block comes first. For each entry, include the probability, the potential impact, and a concrete mitigation path.

| Rank | Stakeholder | Probability | Impact | Mitigation |

> (Note: ranking by grid order or alphabetically is not probability order -- sort by actual likelihood, not convenience.)

Don't leave any entry without a mitigation. A risk you've identified but haven't planned for is just an observation.

---

**Finding your champion -- PM role**

Who in the grid can actively help move this forward? Name them, and give a concrete action you can put on a calendar:

- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you provide the technical depth"
- "Grant [Name]'s team early access at T-3 weeks before GA"

"Keep [Name] engaged" isn't enough -- name something you can schedule.

---

**Communication strategy -- PM role**

Now that you know which quadrant each group falls into, work out the right message, timing, and frame for each. Pick a Frame Type that captures the nature of the communication -- one of: `displacement-acknowledgment`, `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`. Each quadrant gets a different label.

| Quadrant | Key Message | Frame Type | Timing | Owner |

Timing should be a specific interval -- "3 weeks before launch", "day of announcement", "6 weeks out". Avoid vague signals like "soon" without a unit.

---

**Critical-path gatekeepers -- PM role**

If any stakeholder's approval or scheduling constrains your timeline regardless of their stance, flag them. For each:
- The specific constraint (not just "they have authority" -- what exactly are they approving or scheduling?)
- The minimum lead time you need, or the hard deadline

Label each one `[CRITICAL PATH -- lead time: X]`.

---

**Amendment pass -- all roles**

Take one pass back over everything. The initial map almost always misses something -- a stakeholder who got collapsed into a group, a conflict that wasn't visible until you worked through the segments, a veto risk that looked lower probability than it actually is. You need to find at least one amendment.

For each amendment:
- Update the actual table -- add the row, revise the veto rank, adjust the timing and Frame Type as needed. Don't just note that something might be worth investigating.
- Set Source = `amendment` on any new rows.
- Write a brief note on what triggered the finding and what changed from the original map.

After amendments, look at any rows still labeled `initial-inventory`. Each one that hasn't been reclassified is a potential signal that the conflict or segment analysis didn't go deep enough.

---

## V-04 -- C-20 + C-21 Combined

**Axes**: Adjacent before/after amendment pair (C-16) + inertia three-position elevation (C-18) + standalone Frame Type prefill table (C-19) + displacement mandate in the prefill step (C-20) + amendment correct-form shows prefill round-trip (C-21)
**Hypothesis**: C-20 and C-21 are independent and mutually compatible at ~145/155. C-20 claims Step 5a rule 3 (the prefill gate -- assignment made here before row population). C-21 claims the amendment correct-form example (the Step 7 gate -- correct-form shows Step 5a prefill revision + Step 5b content update). Both depend on C-19 (the prefill table existing). C-18 is required scaffolding for C-20. Standard sequence (C-15 absent). UX and champion steps carry no inline FAIL label -- not every gate covered (C-17 absent).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as the initial stakeholder inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question:

> "What org or team is this decision for?"

Do not infer. Do not proceed on assumed org structure.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the highest-consequence failure here.

---

**Step 1 -- Stakeholder Grid**

Build the Power/Interest grid. Every inertia stakeholder from Step 1b must appear with `[INERTIA]` in the designated column.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Quadrant labels**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

**Source labels**: `CODEOWNERS` | `conflict-discovered` | `segment-analysis` | `initial-inventory` | `amendment`

The `[INERTIA]` column is a required structural marker. Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder appearing without `[INERTIA]` in the designated column is an incomplete row.

---

**Step 1b -- Inertia Stakeholder Mapping**

Identify stakeholders whose primary relationship to this decision is defending the status quo.

For each inertia stakeholder:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` | `political` | `ownership`
- **Default veto probability**: Medium unless evidence explicitly supports lower

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

Inertia stakeholders track through three downstream positions: `[INERTIA]` in Step 1's grid, a ranked entry in Step 3's veto list, and `displacement-acknowledgment` assigned in Step 5a's prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step creates two downstream structural gaps -- `[INERTIA]` absent from the grid and `displacement-acknowledgment` not assigned in Step 5a.

---

**Step 1c -- Conflict Identification**

Identify at least two structural conflicts:

> **[Group A] vs. [Group B] -- [resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder concern is not a conflict. Two named parties required.

---

**Step 2 -- UX Segment Analysis**

For each user segment:
1. Role or use pattern
2. What they gain
3. What they lose or find harder
4. **NOT-doing statement**: what this product explicitly does not provide for this segment

For `[INERTIA]` stakeholders: the NOT-doing statement must address what the new approach does not preserve from the current approach.

Split non-monolithic groups. Source = `segment-analysis`.

---

**Step 3 -- Veto Risk Ranking**

Order veto risks by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order.

**FAIL_NO_MITIGATION**: A veto risk without mitigation is an observation, not a risk plan.

---

**Step 4 -- Champion**

Name one or more champions with a specific, schedulable action per champion.

---

**Step 5a -- Frame Type Prefill**

Before writing any row content in the communication table, complete this assignment table.

| Quadrant | Frame Type |
|----------|------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

**Accepted values -- only values from this list may appear in the communication table:**
- `displacement-acknowledgment`
- `risk-mitigation`
- `value-capture`
- `compliance-alignment`
- `awareness-only`
- `co-ownership`

**Assignment rules:**
1. Assign one value per row.
2. No two rows may share the same Frame Type.
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. Make this assignment here, in the prefill step, before any content is written in Step 5b. Assigning a different Frame Type for an inertia quadrant with the intent to correct it in Step 5b is not permitted -- the inertia assignment must be made at this gate.
4. Do not proceed to Step 5b until all four assignments are complete, distinct, and comply with the rules above.
5. Values not in the accepted list are prohibited.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the quadrant containing an `[INERTIA]` stakeholder is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. A corrective change made during row population in Step 5b does not satisfy this requirement.

---

**Step 5b -- Communication Table**

Using the Frame Types from Step 5a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

Frame Type must match Step 5a assignments exactly. If an assigned Frame Type feels wrong, return to Step 5a and reassign before continuing.

Timing must include a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means Step 5a was not honored. Return to Step 5a.

**FAIL_VAGUE_TIMING**: Timing without a quantified unit fails.

---

**Step 6 -- Critical-Path Gatekeepers**

For each critical-path stakeholder:
- Blocking reason (specific)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: Both blocking reason and timing required. A gatekeeper entry without either is incomplete.

---

**Step 7 -- Amendment Pass**

Review Steps 1-6. Run one amendment pass. Minimum one amendment required.

**Read both forms before proceeding:**

**Bad form** (do not do this):
> "Finance may have approval authority over budget line allocations for this feature. Worth checking before GA."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Finance added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- budget approval veto added at High probability, ranked above existing Medium risks. Step 5a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 5b row revised accordingly, Timing set to 8 weeks before launch. Triggered by: Step 1c conflict between Product and Operations over resource allocation surfaced an undisclosed finance sign-off dependency. What changed: Finance was absent from initial-inventory; conflict analysis surfaced the gap.

For every amendment:
1. Update the affected table (grid, veto list, Step 5a prefill, or Step 5b comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder: update Step 1b, tag `[INERTIA]` in Step 1, return to Step 5a and assign `displacement-acknowledgment` before updating Step 5b
4. State what triggered the finding and which prior step surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment.

After all amendments, audit any remaining `initial-inventory` rows. Each unclassified row signals that Step 1c or Step 2 may be incomplete.

---

## V-05 -- Full Seven-Axis (155/155 Attempt)

**Axes**: Reversed sequence (C-15) + adjacent before/after amendment pair (C-16) + anti-pattern saturation at every gate (C-17) + inertia three-position elevation (C-18) + standalone Frame Type prefill table (C-19) + displacement mandate in the prefill step (C-20) + amendment correct-form shows prefill round-trip (C-21)
**Hypothesis**: All seven aspirational criteria occupy independent structural positions and can coexist without mutual interference. C-15 claims phase ordering (Strategy -> UX -> PM). C-16 claims amendment example format. C-17 claims inline FAIL coverage at every gate. C-18 claims Phase 1b sub-step + grid column + prefill Frame Type assignment. C-19 claims the prefill/content split between Steps 6a and 6b. C-20 claims Step 6a rule 3 -- the inertia assignment at the prefill gate before any row content is written, with FAIL_MISSING_DISPLACEMENT_PREFILL. C-21 claims the amendment correct-form example in Step 8 -- the correct-form shows both the Step 6a prefill reassignment and the matching Step 6b content update as a complete round-trip. R5-V-05 confirmed C-15 through C-19 at 145/145 under v5 and its patterns for C-20 and C-21 were scored at 155/155 under v6. This variation restates the same structure as the R6 canonical prompt. If it reaches 155/155, all seven axes are compatible.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Strategy: Conflict, Inertia, and Critical-Path Analysis

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

**1a. Structural conflicts**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**1b. Inertia stakeholder mapping**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` (their process changes) | `political` (their standing diminishes) | `ownership` (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

This stakeholder tracks through three downstream positions: `[INERTIA]` tag in the Phase 3 grid, a ranked veto entry in Step 4, and `displacement-acknowledgment` assigned in the Step 6a prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step means the `[INERTIA]` tag will be absent from the grid and the `displacement-acknowledgment` prefill assignment will not be made. The omission propagates to three downstream positions.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

## Phase 2 -- UX: Segment Analysis

**Run Phase 2 before building the grid.**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

For `[INERTIA]` stakeholders specifically: the NOT-doing statement must address what the new approach does not preserve from the current approach -- the loss signal, not just what the product lacks in absolute terms.

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 3 -- PM: Grid Construction

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Every inertia stakeholder from Phase 1b must appear here with `[INERTIA]` in the designated column. All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Phase 1b appearing without `[INERTIA]` in the designated column is an incomplete row. This column is not a Notes annotation -- it is a required structural marker.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank. Do not underrate structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6a -- Frame Type Prefill**

Before writing any row content in the communication table, complete this assignment.

| Quadrant | Frame Type |
|----------|------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

**Accepted values -- only values from this list may appear in the communication table:**
- `displacement-acknowledgment`
- `risk-mitigation`
- `value-capture`
- `compliance-alignment`
- `awareness-only`
- `co-ownership`

**Assignment rules:**
1. Assign one value per row.
2. No two rows may share the same Frame Type.
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. A value-capture or risk-mitigation frame for an inertia stakeholder's quadrant does not acknowledge displacement -- assign the correct value here, in the prefill step, not during row content population in Step 6b.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and match the rules above.
5. Values not in the accepted list above are not permitted.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the inertia stakeholder's quadrant is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. Three-position inertia elevation requires this assignment at the prefill stage -- a post-hoc change in Step 6b does not satisfy this requirement.

---

**Step 6b -- Communication Table**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing -- do not change values during row population.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder confirmed in Phase 1c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment Pass**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "It may be worth noting that the Platform Security team likely requires sign-off on any changes to authentication flows. This could affect the timeline and should be followed up."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Phase 1 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Phase 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b
4. State what triggered the finding and which prior phase surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.
