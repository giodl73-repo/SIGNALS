Written to `simulations/quest/variations/scout-stakeholders-variations-R5-2026-03-14.md`.

---

## Round 5 — scout-stakeholders — Design Summary

| ID | Axis | C-15 | C-16 | C-17 | C-18 | C-19 | Expected |
|----|------|:----:|:----:|:----:|:----:|:----:|:--------:|
| V-01 | Inertia framing: three-position elevation | - | - | - | ++ | - | ~125 |
| V-02 | Prefill constraint: standalone table | - | - | - | - | ++ | ~125 |
| V-03 | Role sequence: Strategy → UX → PM | ++ | - | - | - | - | ~120 |
| V-04 | C-15 + C-16 + C-17 + C-18 | ++ | ++ | ++ | ++ | - | 140 |
| V-05 | Full five-axis (145/145 attempt) | ++ | ++ | ++ | ++ | ++ | 145 |

---

**Three single-axis tests, then combine:**

**V-01 (C-18 alone)** — Refines R4 V-02's inertia prominence into the three-position structural requirement now that C-18 is load-bearing: dedicated sub-step 1b with `current-approach`/`displaced-by`/`displacement-type` vocabulary, `[INERTIA]` column in the grid (not a Notes annotation), and `displacement-acknowledgment` required for the inertia quadrant row. Standard sequence, 3 FAIL labels, inline Frame Type enumeration. Tests whether C-18 is a stable single axis at ~125/145.

**V-02 (C-19 alone)** — Sharpens R4 V-03's prefill pattern into an explicit Step 6a (prefill assignment table with empty slots + accepted-values constraint list) gating Step 6b (content table). The distinction from inline enumeration: 6a is a titled step with an empty table to fill in, and the rules explicitly say "do not proceed to Step 6b until complete." Inertia incidental. Tests whether C-19 is a stable single axis at ~125/145.

**V-03 (C-15 alone)** — First isolated test of the reversed sequence. R4 only tested C-15 inside the triple combo. Explicit "grid is built last" instruction at Phase 3 header. No FAIL saturation, no before/after pair. Tests whether C-15 registers independently (~125) or requires FAIL coverage to activate (~120).

**V-04 (C-15+C-16+C-17+C-18)** — Bolts C-18 onto R4's proven 135/145 triple. The three C-18 positions (Phase 1b sub-step, `[INERTIA]` grid column, `FAIL_NO_DISPLACEMENT_FRAME` at Step 6) are additive with the existing structure. Frame Types remain inline — no Step 6a prefill. Tests whether C-18 adds 5 points cleanly (→140) or creates tension with C-17 saturation.

**V-05 (all five)** — The 145/145 attempt. C-18 and C-19 occupy non-overlapping structural positions: C-18 claims the strategy sub-step + grid column + comms frame assignment, while C-19 claims the 6a/6b split. The Step 8 amendment example explicitly shows updating Step 6a as part of a correct amendment (reinforcing C-16 while exercising the C-18/C-19 interaction). If this underperforms V-04, the interference diagnostic is: which of the three C-18 positions creates friction with the C-19 prefill gate.
 FAIL label at every execution gate (C-17). Dedicated sub-step 1b + `[INERTIA]` column + `displacement-acknowledgment` mandate added (C-18). Frame Types enumerated inline, not as a separate prefill step (no C-19). Expected 140/145. If it underperforms V-04, C-18 creates structural tension with one of the three prior axes.

**V-05** -- Full 145/145 attempt. All five axes firing simultaneously. C-18 claims Phase 1b sub-step + grid column + comms Frame Type assignment. C-19 claims the prefill/content split between Steps 6a and 6b. C-15 claims phase ordering. C-16 claims amendment example format. C-17 claims inline FAIL coverage at every gate. No two axes claim the same structural position. The amendment example in Step 8 shows returning to Step 6a as part of a correct amendment, reinforcing C-16 while demonstrating the C-18/C-19 interaction. If this reaches 145/145, all five axes are compatible.

**Key C-17 gate coverage for V-04 and V-05:** Every named execution gate carries at least one FAIL label. Step 0: FAIL_SILENT_INFERENCE. Phase 1a: FAIL_ONE_PARTY. Phase 1b: FAIL_NO_INERTIA. Phase 1c: FAIL_NO_TIMING. Phase 2: FAIL_NO_NOT_DOING, FAIL_MONOLITH_ASSUMPTION. Phase 3: FAIL_NO_SOURCE, FAIL_PROSE_ONLY, FAIL_MISSING_INERTIA_TAG. Step 4: FAIL_WRONG_ORDER, FAIL_NO_MITIGATION. Step 5: FAIL_GENERIC_CHAMPION. Step 6/6a: FAIL_NO_DISPLACEMENT_FRAME (V-04) or FAIL_MISSING_DISPLACEMENT_PREFILL (V-05). Step 6/6b: FAIL_SAME_FRAME, FAIL_VAGUE_TIMING. Step 7: FAIL_GATEKEEPER_INCOMPLETE. Step 8: FAIL_OBSERVATION_ONLY. All gates covered.

---

## V-01 -- Inertia Framing: Three-Position Structural Elevation (Single Axis)

**Axis**: Inertia framing -- dedicated strategy sub-step for inertia mapping, `[INERTIA]` column required in grid, `displacement-acknowledgment` Frame Type required for inertia quadrant row; all three positions must fire simultaneously
**Hypothesis**: Elevating inertia stakeholders as a first-class structural element across three simultaneous positions (sub-step + grid tag + comms frame type) captures C-18 in isolation. Standard PM-first sequence (fails C-15), no before/after pair (fails C-16), three FAIL labels total (fails C-17 saturation), inline Frame Type enumeration (fails C-19). If it scores ~125/145, C-18 is a stable independent axis.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently.

**FAIL_SILENT_INFERENCE**: Proceeding on an assumed org without asking is the most consequential error in this skill. One question is always better than a wrong assumption.

---

**Step 1 -- Strategy Role: Conflicts, Inertia, and Critical Path**

Before building the grid, complete three sub-steps in order.

**1a. Structural conflicts**

Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

A single stakeholder's concern listed alone is not a conflict. Flag which conflicts carry veto risk.

**1b. Inertia stakeholder mapping**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: workflow (their process changes) | political (their standing diminishes) | ownership (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly -- do not leave the sub-step blank.

This stakeholder tracks through two downstream steps: `[INERTIA]` tag in the grid (Step 2), `displacement-acknowledgment` Frame Type in the comms table (Step 6).

**FAIL_NO_INERTIA_SUBSTEP**: Collapsing inertia identification into a grid note or veto comment does not satisfy this sub-step. The sub-step requires its own entry with all four fields.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of their stance. Label each `[CRITICAL PATH -- lead time: X]`. A timing constraint is the point of this flag.

---

**Step 2 -- PM Role: Power/Interest Grid**

Build the grid using findings from Step 1.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

Required for every row:
- **[INERTIA]**: mark `[INERTIA]` for every stakeholder identified in Step 1b; leave blank otherwise. This is a required column, not a Notes annotation.
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Every stakeholder identified in Step 1b must appear here with the `[INERTIA]` marker populated.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 1b appearing without `[INERTIA]` in the designated column is an incomplete row. The tag is not optional.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants:
1. Workflow intersection with this decision
2. Whether the group contains sub-segments with distinct friction or interest levels
3. One NOT-doing statement: what this product explicitly does not provide for this segment

For `[INERTIA]` stakeholders specifically: the NOT-doing statement must address what the new approach does not preserve from the current approach -- what the stakeholder is losing is the signal, not just what the product lacks in absolute terms.

If a sub-segment is identified, add a row to the grid with Source = `UX-segment`.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not by grid order.

| Rank | Stakeholder | Probability | Impact | Mitigation |

Every `[INERTIA]` stakeholder must appear at their correct probability rank. Do not underrate structural resistance; the default for inertia stakeholders is Medium unless evidence says otherwise.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

Generic "engage the champion" language is not schedulable and does not pass.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

Accepted Frame Type values: `displacement-acknowledgment` | `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership`

Assignment rules:
- One distinct label per quadrant row. No two rows may share a Frame Type.
- The quadrant row containing any `[INERTIA]` stakeholder must use `displacement-acknowledgment`. A value-capture or risk-mitigation frame for an inertia row does not acknowledge displacement -- this is the third position of the inertia structural elevation, and it is not optional.
- Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_NO_DISPLACEMENT_FRAME**: If the inertia stakeholder's quadrant row does not carry `displacement-acknowledgment`, two of the three structural positions are present (sub-step + tag) but the third is absent. All three are required; partial presence fails C-18.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder from Step 1c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Steps 1 through 7. Run one amendment pass. Minimum one amendment required.

For each amendment:
1. Update the affected table (grid, veto, or comms) -- do not observe without updating
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, add `[INERTIA]` to the grid row and assign `displacement-acknowledgment` in the comms table
4. State what triggered the finding and what changed from the initial map

After the amendment pass, audit any `initial-inventory` rows that remain unverified. Each one not reclassified signals that conflict or segment analysis may be incomplete.

---

## V-02 -- Output Format: Standalone Frame Type Prefill Table (Single Axis)

**Axis**: Output format -- standalone prefill table as a distinct numbered step (Step 6a) that constrains accepted Frame Type values before the communication table (Step 6b) is populated; values not appearing in the prefill table are prohibited
**Hypothesis**: Separating Frame Type assignment (Step 6a: prefill constraint table) from content population (Step 6b: communication table) creates a procedural gate that satisfies C-19 -- structurally distinct from enumerating accepted values inline within instructions. Standard sequence (fails C-15). No before/after pair (fails C-16). Moderate FAIL coverage but not every gate (fails C-17). Inertia mentioned in Step 1 but not structurally elevated (fails C-18). If it scores ~125/145, C-19 is a stable independent axis.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently.

**FAIL_SILENT_INFERENCE**: Proceeding on an assumed org without asking is the most consequential error in this skill.

---

**Step 1 -- Strategy Role: Conflicts and Critical Path**

Before building the grid:

1. Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension: **[Group A] vs. [Group B] -- [nature]**. Flag which carry veto risk. A single stakeholder's concern listed alone is not a conflict.
2. Name the inertia stakeholder: who benefits from keeping the current approach in place? Their veto probability is at least Medium.
3. Flag critical-path gatekeepers with minimum lead time. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_ONE_PARTY**: Two named parties required for a conflict entry. A single stakeholder's concern does not satisfy this step.

---

**Step 2 -- PM Role: Power/Interest Grid**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

Required:
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows. The inertia stakeholder from Step 1 must appear. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants:
1. Workflow intersection with this decision
2. Whether the group splits into sub-segments with distinct friction or interest levels
3. One NOT-doing statement: what this product explicitly does not provide for this segment

If a sub-segment is identified, add a row with Source = `UX-segment`.

**FAIL_NO_NOT_DOING**: Generic "out of scope" language does not pass the NOT-doing requirement.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not in grid order.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Alphabetical or grid-sequence order is not probability order.

---

**Step 5 -- Champion**

Name one or more champions. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] opens, you detail the tradeoffs"
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
3. Values not in the accepted list above are not permitted in Step 6b.
4. Do not proceed to Step 6b until all four assignments are complete and distinct.

---

**Step 6b -- Communication Table**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing here -- do not change values during row population.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a prefill assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder from Step 1:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Steps 1 through 7. Run one amendment pass. Minimum one amendment required.

For each amendment:
1. Update the affected table (grid, veto, or comms) -- do not observe without updating
2. Set Source = `amendment` on new rows
3. If the amendment adds a new stakeholder, return to Step 6a and reassign Frame Types if needed before updating Step 6b -- duplicate Frame Types are not permissible even after amendments
4. State what triggered the finding and what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment.

After the amendment pass, note any `initial-inventory` rows that remain unverified.

---

## V-03 -- Role Sequence: Analysis-Before-Synthesis (Single Axis)

**Axis**: Role sequence -- reversed execution order: Phase 1 (Strategy: conflict analysis) runs first, Phase 2 (UX: segment analysis) runs second, Phase 3 (PM: grid construction) runs last; explicit instruction that the grid is built only after both analysis phases are complete
**Hypothesis**: Reversing the sequence so analysis precedes synthesis captures C-15 in isolation. C-15 was only tested in combination (R4 V-04 triple); this is the first single-axis test. No FAIL saturation (fails C-17). No before/after pair (fails C-16). Inertia mentioned but not structurally elevated (fails C-18). Inline Frame Type enumeration (fails C-19). If it scores ~125/145, C-15 registers as an independent axis. If ~120/145, the sequence alone without FAIL coverage is insufficient.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently. Never assume an org structure.

---

## Phase 1 -- Strategy: Conflict and Inertia Analysis

**Run this phase first. The Power/Interest Grid is built in Phase 3, not here.**

The purpose of this phase is to surface the political and organizational landscape before any synthesis happens. Building the grid before conflict analysis risks missing adversarial stakeholders and misclassifying inertia as neutral.

**1a. Structural conflicts**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk. A single stakeholder's concern listed alone is not a conflict.

**1b. Inertia stakeholder**

Name who benefits from keeping the current approach in place. State why their resistance is structural rather than personal. Their default veto probability is Medium.

**1c. Critical-path gatekeepers**

Flag stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`. A gatekeeper without a timing note is an incomplete entry.

---

## Phase 2 -- UX: Segment Analysis

**Run this phase second. The Power/Interest Grid is built in Phase 3, after this phase is complete.**

For each stakeholder segment relevant to this decision:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

If a segment is not monolithic -- if a sub-group has substantially higher interest or distinct friction -- split it now and carry sub-rows forward to Phase 3. New rows from this phase carry Source = `segment-analysis`.

The inertia stakeholder's NOT-doing statement should address what the new approach does not preserve from the current approach.

---

## Phase 3 -- PM: Grid Construction

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Grid construction is synthesis, not discovery. All inputs are ready.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes. Every row requires a Source entry.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not in grid order.

| Rank | Stakeholder | Probability | Impact | Mitigation |

The inertia stakeholder from Phase 1b must appear at their correct probability rank.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a 10-minute demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

Generic "engage the champion" is not schedulable and does not pass.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

Accepted Frame Type values: `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership` | `displacement-acknowledgment`

Each row must carry a distinct Frame Type. No two quadrant rows may share the same label. Timing must be a relative signal with a quantified interval.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder confirmed in Phase 1c:
- Blocking reason (specific)
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. What did the initial map miss, collapse, or misplace?

For each amendment:
1. Update the affected table (grid, veto, or comms)
2. Set Source = `amendment` on new rows
3. State what triggered the finding (which phase surfaced it)
4. State what changed from the initial map

Writing a finding without updating a table is not an amendment.

After the amendment pass, note any `initial-inventory` rows that remain unverified.

---

## V-04 -- Combination: C-15 + C-16 + C-17 + C-18

**Axes**: Role sequence (C-15) + before/after amendment pair (C-16) + anti-pattern saturation at every gate (C-17) + inertia structural three-position elevation (C-18); Frame Type enumeration remains inline (no C-19)
**Hypothesis**: The proven R4 V-04 triple (C-15 + C-16 + C-17 at 135/145) can absorb C-18 without structural conflict. C-18 occupies three new positions -- Phase 1b sub-step, `[INERTIA]` grid column, `displacement-acknowledgment` Frame Type mandate -- none overlapping with C-15 (phase ordering), C-16 (amendment example format), or C-17 (FAIL label coverage). Expected 140/145. If it underperforms V-04, C-18 creates structural tension with one of the three prior axes.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. This is the first and most consequential gate.

**FAIL_SILENT_INFERENCE**: Proceeding on an assumed org without asking is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Strategy: Conflict, Inertia, and Critical-Path Analysis

**Run Phase 1 first. The grid is built in Phase 3, after Phases 1 and 2 are complete.**

**1a. Structural conflicts**

Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**1b. Inertia stakeholder mapping**

Identify stakeholders whose primary relationship to this decision is defending the status quo.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: workflow | political | ownership
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

This stakeholder tracks through two downstream steps: `[INERTIA]` tag in the Phase 3 grid, `displacement-acknowledgment` Frame Type in Step 6.

**FAIL_NO_INERTIA**: Omitting this sub-step or collapsing it into a grid note means the `[INERTIA]` tag will be absent from the grid and the Frame Type mandate will not be executed. The omission propagates to two downstream positions.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

## Phase 2 -- UX: Segment Analysis

**Run Phase 2 before building the grid.**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

For `[INERTIA]` stakeholders specifically: the NOT-doing statement must address what the new approach does not preserve from the current approach.

If a group is not monolithic, split it now. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 3 -- PM: Grid Construction

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases.

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

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Phase 1b appearing without `[INERTIA]` in the designated column is an incomplete row. This is not a Notes annotation -- it is a required column value.

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

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

Accepted Frame Type values: `displacement-acknowledgment` | `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership`

Assignment rules:
- One distinct Frame Type per quadrant row. No two rows may share the same label.
- The quadrant row containing any `[INERTIA]` stakeholder must use `displacement-acknowledgment`. A value-capture or risk-mitigation frame for an inertia row does not satisfy the third position of inertia structural elevation.
- Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two or more rows means messages are not differentiated by quadrant.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

**FAIL_NO_DISPLACEMENT_FRAME**: If the inertia stakeholder's quadrant row does not carry `displacement-acknowledgment`, Phase 1b sub-step and the `[INERTIA]` tag are present but the third position is absent. All three are required.

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
> "It may be worth considering whether the Platform Reliability team has concerns about rollout velocity given their current commitments. This could affect the timeline and might be worth a follow-up conversation."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Platform Reliability added (Keep Satisfied, H power / L interest, Source: amendment). Veto list updated -- rollout velocity veto added at Medium probability, ranked below Engineering lead High-probability veto. Comms table updated -- Keep Satisfied row revised; Frame Type changed to `risk-mitigation`, Timing set to 5 weeks before launch. Triggered by: Phase 1 scope conflict between Engineering and Operations surfaced an undisclosed dependency on Platform Reliability sign-off. What changed: Platform Reliability was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, or comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Phase 1b displacement vocabulary, tag the new row `[INERTIA]`, and assign `displacement-acknowledgment` in Step 6
4. State what triggered the finding (which phase surfaced it)
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete.

---

## V-05 -- Full Combination: C-15 + C-16 + C-17 + C-18 + C-19 (145/145 Attempt)

**Axes**: Role sequence (C-15) + before/after amendment pair (C-16) + anti-pattern saturation at every gate (C-17) + inertia structural three-position elevation (C-18) + standalone Frame Type prefill table as distinct step (C-19)
**Hypothesis**: All five aspirational criteria occupy independent structural positions and can coexist without mutual interference. C-18 claims Phase 1b sub-step + grid column + comms Frame Type assignment. C-19 claims the prefill/content split between Steps 6a and 6b. C-15 claims phase ordering. C-16 claims amendment example format. C-17 claims inline FAIL coverage at every gate. No two axes claim the same structural position. The amendment example in Step 8 shows returning to Step 6a as part of a correct amendment, reinforcing C-16 while demonstrating the C-18/C-19 interaction. If this reaches 145/145, all five axes are compatible. If it underperforms V-04, one of the two new criteria is creating interference.

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
- **Displacement type**: workflow (their process changes) | political (their standing diminishes) | ownership (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

This stakeholder tracks through three downstream positions: `[INERTIA]` tag in the Phase 3 grid, ranked veto entry in Step 4, and `displacement-acknowledgment` in the Step 6a prefill.

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
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. A value-capture or risk-mitigation frame for an inertia stakeholder's quadrant does not acknowledge displacement -- assign the correct value here, not during row content population in Step 6b.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and match the rules above.
5. Values not in the accepted list above are not permitted.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the inertia stakeholder's quadrant is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. Three-position inertia elevation requires this assignment at the prefill stage -- a post-hoc change in Step 6b does not satisfy C-18.

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
> "It may be worth noting that the Data Governance team likely has approval authority over schema changes. This could affect the timeline and should be followed up."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Data Governance added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- schema approval veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 8 weeks before launch. Triggered by: Phase 1 conflict between Engineering and Platform over data ownership scope surfaced an undisclosed sign-off dependency. What changed: Data Governance was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Phase 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b
4. State what triggered the finding and which prior phase surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.
