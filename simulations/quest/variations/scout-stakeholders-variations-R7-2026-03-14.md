Written to `simulations/quest/variations/scout-stakeholders-variations-R7-2026-03-14.md`.

---

## Round 7 -- scout-stakeholders -- Design Summary

| ID | Axis | C-15 | C-18 | C-20 | C-22 | C-23 | Expected |
|----|------|:----:|:----:|:----:|:----:|:----:|:--------:|
| V-01 | C-23 alone -- role label heading binding | ++ | ++ | ++ | ++ | ++ | 165 |
| V-02 | Role sequence: PM-first | -- | ++ | ++ | ++ | -- | ~155 |
| V-03 | Inertia framing: reduced | ++ | -- | -- | ++ | -- | ~150 |
| V-04 | C-23 + PM-first combined | -- | ++ | ++ | ++ | ++ | ~160 |
| V-05 | Full 165/165 canonical | ++ | ++ | ++ | ++ | ++ | 165 |

---

**V-01 (C-23 alone)** — V-05 R6 verbatim + role labels in every heading. No other changes. C-22 was already present in V-05 R6. Single axis: does "-- Strategy role" / "-- UX role" / "-- PM role" in heading text satisfy C-23 without disturbing any prior structure? Expected: 165/165.

**V-02 (Role sequence: PM-first)** — Grid constructed first, then UX, then Strategy with retroactive [INERTIA] tagging at Step 3b. C-15 absent. C-23 absent. C-18/C-20/C-22 all retained. Tests whether C-15 is independently excisable. Expected: ~155/165.

**V-03 (Inertia framing: reduced)** — No dedicated inertia sub-step, no [INERTIA] column, no displacement-acknowledgment rule in prefill. Prefill table retained (C-19 passes), amendment mandate names prefill (C-22 passes), round-trip example retained (C-21 passes). C-18 and C-20 absent. Tests whether the inertia axis is independently excisable. Expected: ~150/165.

**V-04 (C-23 + PM-first)** — V-02 PM-first with role labels. Tests C-23/PM-first compatibility. Grid step = "-- PM role", UX step = "-- UX role", conflict/inertia steps = "-- Strategy role". Expected: ~160/165.

**V-05 (Full 165/165 canonical)** — All 23 criteria simultaneously. Adds a role-ownership summary at the top. The Round 7 golden candidate if scored at 165/165. Key distinction from V-01: clean authoritative rewrite with the role-ownership preamble; V-01 is the minimal-delta proof.
ppear in the grid as ordinary rows without structural elevation. Standalone prefill table retained (C-19 passes). Amendment mandate still names "Step 6a prefill" (C-22 passes). Correct-form amendment example still demonstrates a prefill round-trip (C-21 retained). C-15 retained (Strategy-first). C-23 absent. Tests whether the C-18/C-20 pair is independently excisable. Expected: ~150/165 (-C-18, -C-20, -C-23).

**V-04 (C-23 + PM-first combined)** -- V-02 PM-first sequence with role labels added to all step headings. Tests whether C-23 and PM-first coexist without interference. Each step is labeled at the heading level: grid step (PM role), UX step (UX role), conflict/inertia steps (Strategy role). Expected: ~160/165 (gains C-23 over V-02; still lacks C-15).

**V-05 (Full 165/165 canonical)** -- Authoritative Round 7 rewrite integrating all 23 criteria. Strategy-first reversed sequence (C-15), three-position inertia elevation (C-18), prefill constraint table (C-19), displacement mandate in prefill (C-20), amendment prefill round-trip (C-21), mandate enumerating Step 6a (C-22), role labels in every heading (C-23), FAIL saturation at every gate (C-17), adjacent before/after amendment pair (C-16). Adds a role-ownership summary at the top. If it reaches 165/165, it becomes the Round 7 golden candidate.

---

## V-01 -- C-23 Alone: Role Label Heading Binding

**Axes**: All of V-05 R6 (C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22) + role label in every step heading (C-23)
**Hypothesis**: Role-label-in-heading is a pure additive axis on V-05 R6. Adding "-- [Role] role" to every step and phase heading satisfies C-23 without disturbing any prior structure. Phase boundaries remain Strategy / UX / PM. FAIL saturation is unaffected (FAIL labels live in step body text, not headings). Inertia tracking propagates through identical downstream positions. Amendment mandate continues to enumerate "Step 6a prefill". Expected: 165/165.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Structural conflict, inertia, and critical-path analysis -- Strategy role

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

**Step 1a -- Structural conflicts -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**Step 1b -- Inertia stakeholder mapping -- Strategy role**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` (their process changes) | `political` (their standing diminishes) | `ownership` (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

This stakeholder tracks through three downstream positions: `[INERTIA]` tag in the Phase 3 grid, a ranked veto entry in Step 4, and `displacement-acknowledgment` assigned in the Step 6a prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step means the `[INERTIA]` tag will be absent from the grid and the `displacement-acknowledgment` prefill assignment will not be made. The omission propagates to three downstream positions.

**Step 1c -- Critical-path gatekeeper identification -- Strategy role**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

## Phase 2 -- Segment analysis and NOT-doing statements -- UX role

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

## Phase 3 -- Power/Interest grid construction -- PM role

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Every inertia stakeholder from Step 1b must appear here with `[INERTIA]` in the designated column. All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 1b appearing without `[INERTIA]` in the designated column is an incomplete row. This column is not a Notes annotation -- it is a required structural marker.

---

**Step 4 -- Veto risk ranking -- Strategy role**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank. Do not underrate structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6a -- Frame Type prefill -- PM role**

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

**Step 6b -- Communication table -- PM role**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing -- do not change values during row population.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-path gatekeeper confirmation -- Strategy role**

For each `[CRITICAL PATH]` stakeholder confirmed in Step 1c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment pass -- all roles**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "It may be worth noting that the Platform Security team likely requires sign-off on any changes to authentication flows. This could affect the timeline and should be followed up."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Phase 1 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b
4. State what triggered the finding and which prior phase surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-02 -- Role Sequence: PM-First

**Axes**: PM-first sequence (grid constructed before conflict and segment analysis). All of V-05 R6 structural criteria retained except C-15 (reversed sequence) and C-23 (role heading binding), which are absent.
**Hypothesis**: C-15 (analysis-before-synthesis sequence) is independently excisable. PM-first tests whether grid-before-analysis is compatible with all other aspirational criteria. [INERTIA] tags are applied retroactively at Step 3b -- after conflict analysis identifies inertia stakeholders, the grid is updated. C-18 three-position elevation retained. C-20 retained. C-22 retained. C-15 absent. C-23 absent. Expected: ~155/165 (-C-15, -C-23).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

**Step 1 -- Initial Stakeholder Grid**

Build the initial Power/Interest grid from all available inventory (CODEOWNERS + general product context). Source most rows as `initial-inventory` here. Conflict analysis (Step 3a) and segment analysis (Step 2) will reclassify rows and add new ones.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source labels**: `CODEOWNERS` | `conflict-discovered` | `segment-analysis` | `initial-inventory` | `amendment`

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Leave the [INERTIA] column blank here -- inertia stakeholders are identified in Step 3b and tagged retroactively. Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

---

**Step 2 -- UX Segment Analysis**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows added to the Step 1 grid carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

**Step 3a -- Conflict Identification**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk. Any new stakeholder surfaced here: add to the Step 1 grid with Source = `conflict-discovered`.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

---

**Step 3b -- Inertia Stakeholder Mapping**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` | `political` | `ownership`
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

After identifying each inertia stakeholder: return to the Step 1 grid and tag them `[INERTIA]` in the designated column. Update Source to `conflict-discovered` if they were listed as `initial-inventory` and this step confirms their inertia role.

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

Each inertia stakeholder tracks through three downstream positions: `[INERTIA]` tag in Step 1's grid, a ranked entry in Step 4's veto list, and `displacement-acknowledgment` assigned in Step 6a's prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step leaves the `[INERTIA]` column blank and the `displacement-acknowledgment` prefill assignment unmade. The omission propagates to three downstream positions.

---

**Step 3c -- Critical-Path Gatekeeper Identification**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Return to the Step 1 grid and label each `[CRITICAL PATH -- lead time: X]` in Notes.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

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
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. Assign the correct value here, in the prefill step, before any row content is populated in Step 6b.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and match the rules above.
5. Values not in the accepted list above are not permitted.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the inertia stakeholder's quadrant is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. A corrective change made during row population in Step 6b does not satisfy this requirement.

---

**Step 6b -- Communication Table**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder confirmed in Step 3c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment Pass**

Review Steps 1-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "The Legal team may need to review the data retention policy changes before launch. This dependency should be confirmed."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Legal added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- data retention approval veto added at High probability, ranked above existing Medium risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 8 weeks before launch. Triggered by: Step 3a conflict between Engineering and Compliance over retention scope surfaced an undisclosed Legal sign-off dependency. What changed: Legal was absent from initial-inventory; conflict analysis surfaced the gap.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Step 3b displacement vocabulary, tag the new row `[INERTIA]` in Step 1, return to Step 6a and reassign Frame Types if needed, then update Step 6b
4. State what triggered the finding and which prior step surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Step 2 or Step 3 may be incomplete. Note them explicitly.

---

## V-03 -- Inertia Framing: Reduced

**Axes**: Inertia axis simplified -- no dedicated inertia sub-step, no [INERTIA] column, no displacement-acknowledgment rule in the prefill. All other V-05 R6 criteria retained: reversed sequence (C-15), adjacent before/after pair (C-16), FAIL saturation at every gate (C-17), standalone prefill constraint table (C-19), amendment prefill round-trip example (C-21), amendment mandate naming Step 6a prefill (C-22). C-23 absent.
**Hypothesis**: C-18 (three-position inertia elevation) and C-20 (displacement mandate in prefill) are independently excisable without disturbing the remaining criteria. The prefill table continues to enforce Frame Type uniqueness as a pure procedural constraint without inertia-specific rules. The correct-form amendment example can still demonstrate a prefill round-trip without an inertia-specific trigger. Expected: ~150/165 (-C-18, -C-20, -C-23).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Strategy: Conflict and Critical-Path Analysis

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

**Step 1a -- Structural Conflicts**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk. Include any stakeholders who may resist because they depend on the current approach -- these are high-probability veto candidates.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**Step 1b -- Critical-Path Gatekeeper Identification**

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

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 3 -- PM: Grid Construction

**Build this grid now -- after Phase 1 and Phase 2 are complete.**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Stakeholders who depend on the status quo or whose role diminishes if this decision succeeds should be ranked at their true probability -- do not underrate structural resistance.

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
3. Choose the Frame Type that best captures the nature of the communication relationship for each quadrant.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and drawn from the accepted list.
5. Values not in the accepted list above are not permitted.

**FAIL_SAME_FRAME**: Two rows with the same Frame Type means the prefill was not completed correctly. Return here before populating rows.

---

**Step 6b -- Communication Table**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder confirmed in Step 1b:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment Pass**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "The Finance team may have approval authority over the budget allocation for this initiative. This is worth investigating before the decision is finalized."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Finance added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- budget approval veto added at High probability, ranked above existing Medium risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 8 weeks before launch. Triggered by: Phase 1 conflict between Product and Operations over resource allocation surfaced an undisclosed Finance sign-off dependency. What changed: Finance was absent from initial-inventory; conflict analysis surfaced the gap.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment changes a quadrant's stakeholder composition, return to Step 6a and confirm the Frame Type assignment is still appropriate; if not, reassign in Step 6a first, then update Step 6b to match
4. State what triggered the finding and which prior phase surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-04 -- C-23 + PM-First Combined

**Axes**: PM-first sequence (C-15 absent) + role label in every step heading (C-23)
**Hypothesis**: C-23 and PM-first coexist without interference. The heading-level role labels survive the reordering: the grid step becomes "-- PM role", the UX step becomes "-- UX role", the conflict/inertia steps become "-- Strategy role". C-18, C-20, C-22 all retained. C-15 absent (PM-first violates analysis-before-synthesis). Expected: ~160/165 (gains C-23 vs V-02; still lacks C-15).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

**Step 1 -- Initial stakeholder grid -- PM role**

Build the initial Power/Interest grid from all available inventory. Source most rows as `initial-inventory` here. Steps 2-3 will reclassify rows and add new ones.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source labels**: `CODEOWNERS` | `conflict-discovered` | `segment-analysis` | `initial-inventory` | `amendment`

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Leave the [INERTIA] column blank here -- inertia stakeholders are identified in Step 3b and tagged retroactively. Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

---

**Step 2 -- Segment analysis -- UX role**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows added to the Step 1 grid carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

**Step 3a -- Conflict identification -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk. Any new stakeholder surfaced here: add to the Step 1 grid with Source = `conflict-discovered`.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

---

**Step 3b -- Inertia stakeholder mapping -- Strategy role**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` | `political` | `ownership`
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

After identifying each inertia stakeholder: return to the Step 1 grid and tag them `[INERTIA]` in the designated column.

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

Each inertia stakeholder tracks through three downstream positions: `[INERTIA]` tag in Step 1's grid, a ranked entry in Step 4's veto list, and `displacement-acknowledgment` assigned in Step 6a's prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step leaves the `[INERTIA]` column blank and the `displacement-acknowledgment` prefill assignment unmade. The omission propagates to three downstream positions.

---

**Step 3c -- Critical-path gatekeeper identification -- Strategy role**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Return to the Step 1 grid and label each `[CRITICAL PATH -- lead time: X]` in Notes.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

**Step 4 -- Veto risk ranking -- Strategy role**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank. Do not underrate structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6a -- Frame Type prefill -- PM role**

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
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. Assign the correct value here, in the prefill step, before any row content is populated in Step 6b.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and match the rules above.
5. Values not in the accepted list above are not permitted.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the inertia stakeholder's quadrant is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. A corrective change made during row population in Step 6b does not satisfy this requirement.

---

**Step 6b -- Communication table -- PM role**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-path gatekeeper confirmation -- Strategy role**

For each `[CRITICAL PATH]` stakeholder confirmed in Step 3c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment pass -- all roles**

Review Steps 1-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "The Procurement team may have approval authority over vendor contracts associated with this decision. This should be confirmed before launch."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Procurement added (Keep Satisfied, H power / L interest, Source: amendment). Veto list updated -- vendor contract approval veto added at High probability, ranked above existing Medium risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 10 weeks before launch. Triggered by: Step 3a conflict between Engineering and Finance over build-vs-buy surfaced an undisclosed Procurement sign-off dependency. What changed: Procurement was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Step 3b displacement vocabulary, tag the new row `[INERTIA]` in Step 1, return to Step 6a and reassign Frame Types if needed, then update Step 6b
4. State what triggered the finding and which prior step surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Step 2 or Step 3 may be incomplete. Note them explicitly.

---

## V-05 -- Full 165/165 Canonical

**Axes**: Reversed sequence (C-15) + adjacent before/after amendment pair (C-16) + anti-pattern saturation at every gate (C-17) + inertia three-position elevation (C-18) + standalone Frame Type prefill table (C-19) + displacement mandate in prefill step (C-20) + amendment correct-form prefill round-trip (C-21) + amendment mandate enumerates Step 6a (C-22) + role label in every step heading (C-23)
**Hypothesis**: All nine aspirational criteria occupy independent structural positions and can coexist simultaneously. C-23 (role-in-heading) occupies the heading text exclusively -- it does not conflict with FAIL labels in the step body (C-17), with the inertia tracking chain (C-18, C-20), or with the amendment pair structure (C-16, C-21, C-22). A role-ownership summary is added at the top as a navigational aid. If this reaches 165/165, it becomes the Round 7 golden candidate.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Analytical role assignments**: Strategy owns Phase 1 (conflicts, inertia, critical-path) and Steps 4, 7. UX owns Phase 2 (segment analysis). PM owns Phase 3 (grid construction) and Steps 5, 6a, 6b. All roles participate in Step 8 (amendment pass). Step 0 is a PM-led gate.

---

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Structural conflict, inertia, and critical-path analysis -- Strategy role

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

**Step 1a -- Structural conflicts -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**Step 1b -- Inertia stakeholder mapping -- Strategy role**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` (their process changes) | `political` (their standing diminishes) | `ownership` (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

This stakeholder tracks through three downstream positions: `[INERTIA]` tag in the Phase 3 grid, a ranked veto entry in Step 4, and `displacement-acknowledgment` assigned in the Step 6a prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step means the `[INERTIA]` tag will be absent from the grid and the `displacement-acknowledgment` prefill assignment will not be made. The omission propagates to three downstream positions.

**Step 1c -- Critical-path gatekeeper identification -- Strategy role**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

## Phase 2 -- Segment analysis and NOT-doing statements -- UX role

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

## Phase 3 -- Power/Interest grid construction -- PM role

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Every inertia stakeholder from Step 1b must appear here with `[INERTIA]` in the designated column. All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 1b appearing without `[INERTIA]` in the designated column is an incomplete row. This column is not a Notes annotation -- it is a required structural marker.

---

**Step 4 -- Veto risk ranking -- Strategy role**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank. Do not underrate structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6a -- Frame Type prefill -- PM role**

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

**Step 6b -- Communication table -- PM role**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing -- do not change values during row population.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-path gatekeeper confirmation -- Strategy role**

For each `[CRITICAL PATH]` stakeholder confirmed in Step 1c:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment pass -- all roles**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "It may be worth noting that the Data Governance team likely requires sign-off on any schema changes introduced by this feature. This dependency should be confirmed before the decision is finalized."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Data Governance added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- schema change approval veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Phase 1 conflict between Platform Engineering and Data Platform over schema ownership surfaced an undisclosed Data Governance sign-off dependency. What changed: Data Governance was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, comms, or Step 6a prefill) -- no observation without revision
2. Set Source = `amendment` on new rows
3. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b
4. State what triggered the finding and which prior phase surfaced it
5. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.
