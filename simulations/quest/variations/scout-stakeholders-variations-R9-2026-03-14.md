Written to `simulations/quest/variations/scout-stakeholders-variations-R9-2026-03-14.md`.

---

## Round 9 -- V-01 through V-05

### Design Summary

| ID | Axis | C-15 | C-19 | C-26 | New Candidates | Expected |
|----|------|:----:|:----:|:----:|:---------------|:--------:|
| V-01 | All 26 + champion depth/durability + phase gates | ++ | ++ | ++ | C-27 (champion scoring), C-28 (champion durability) | 180 |
| V-02 | Single axis: C-26 deliberately absent | ++ | ++ | **--** | -- | 175 |
| V-03 | Single axis: conflict resolution pathway | ++ | ++ | ++ | C-27 candidate (resolution pathway) | 180+ |
| V-04 | Single axis: stakeholder engagement window | ++ | ++ | ++ | C-28 candidate (engagement window) | 180+ |
| V-05 | All 26 + all new axes combined | ++ | ++ | ++ | C-27 + C-28 + C-29 + C-30 | 180+ |

---

### Variation axis choices

**V-01** merges V-05 R8 (champion depth scoring + durability) with V-01 R8 (phase transition gates) — the first full-26 variation under v9 with champion extensions, confirming all axes are simultaneously satisfiable.

**V-02** is the C-26 independence probe. Transition gates are removed; the phase sequence remains Strategy→UX→PM with standard ordering language (satisfying C-15) but no dedicated between-phase gate steps. Expected -5 pts, confirming C-26 is independently excisable from the v9 full set.

**V-03** introduces **conflict resolution pathways** (lifecycle emphasis axis): a per-conflict table in Step 1a naming the resolution authority, required decision, and deadline. The Phase 1→Phase 2 gate checklist includes "resolution pathway present for each conflict." Amendment mandate extended to include resolution pathway entries. New FAIL: `FAIL_NO_RESOLUTION_PATHWAY`.

**V-04** introduces **stakeholder engagement windows** (output format axis): an Engagement Window column in the grid plus Step 5a to derive per-quadrant windows before Step 6b. Comms timing must fall within the derived window. New FAILs: `FAIL_NO_ENGAGEMENT_WINDOW` at Phase 3, `FAIL_NO_WINDOW_SUMMARY` at Step 5a, `FAIL_WINDOW_MISMATCH` at Step 6b.

**V-05** combines all axes: all 26 + champion depth/durability (Steps 5c-5d) + conflict resolution pathways (Step 1a) + engagement windows (grid column + Step 5a). Four new amendment-eligible target classes. The amendment correct-form example in V-05 demonstrates resolution pathway, engagement window, and champion score revisions in a single amendment entry.
ia stakeholders:** The most commonly underweighted stakeholders in a feature decision are those defending the current approach -- not because they are obstructionist, but because their workflow, standing, or system ownership is being displaced. This skill treats inertia analysis as a structural requirement, not an optional consideration. Every inertia stakeholder identified in Phase 1 will propagate to three downstream positions: a tagged row in the grid, a ranked veto entry, and a Frame Type assignment that acknowledges displacement. Missing any one of these three positions means the inertia signal was incomplete.

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

**Phase 1 -> Phase 2 Transition Gate -- PM role**

Before proceeding to Phase 2, confirm all Phase 1 outputs are present:

- At least two structural conflicts named, each with both parties and tension type explicitly stated
- Inertia sub-step completed (or explicitly noted as "no inertia stakeholders found")
- Each inertia stakeholder entry includes: current approach, displaced-by, displacement type, veto probability
- At least one critical-path gatekeeper flagged with lead time or deadline

**FAIL_INCOMPLETE_PHASE1**: Do not proceed to Phase 2 if any required output above is absent. Phase 2's NOT-doing statements depend on the displacement vocabulary established in Step 1b. A grid built without Phase 1 conflict data will have incomplete Source labels and underweighted veto entries.

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

**Phase 2 -> Phase 3 Transition Gate -- PM role**

Before building the grid in Phase 3, confirm all Phase 2 outputs are present:

- Every user segment has a NOT-doing statement
- Any non-monolithic groups have been split into sub-segments where warranted
- All rows introduced during segment analysis carry Source = `segment-analysis`
- Inertia stakeholder NOT-doing statements address displacement loss specifically (not generic absence)

**FAIL_INCOMPLETE_PHASE2**: Do not proceed to Phase 3 if any required output above is absent. Grid rows built before segment analysis is complete will carry unresolved Source = `initial-inventory` labels that should have been reclassified before construction, not during the amendment pass.

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

**Step 5a -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

**Step 5b -- Champion depth scoring -- PM role**

For each champion, score on three dimensions (1 = weak, 5 = strong):

| Champion | Authority (1-5) | Proximity (1-5) | Commitment (1-5) | Composite |
|----------|:---------------:|:---------------:|:----------------:|:---------:|

- **Authority**: Does their endorsement carry weight with the decision-makers who control veto risks?
- **Proximity**: How frequently do they interact with stakeholders who need to be moved?
- **Commitment**: How personally invested are they in this outcome -- would they advocate without prompting?

Composite = Authority + Proximity + Commitment (max 15). Champions scoring below 9 should be treated as supporting evidence, not primary movers -- identify a secondary champion or plan to build commitment before relying on them.

**Step 5c -- Champion durability -- PM role**

For each champion, assess:
- **Single-point-of-failure risk**: If this person moves to another role or leaves the org, does champion coverage collapse?
- **Succession**: Who is the next most likely champion in this stakeholder's network, and what would it take to activate them?
- **Deterioration signal**: What early sign would indicate this champion is losing commitment? (e.g., stops attending reviews, delegates to a lower-level proxy, starts hedging in steering conversations)

**FAIL_NO_DURABILITY**: A champion plan with a single named person and no succession or deterioration signal is a plan with a single point of failure.

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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Champion depth scoring updated -- [Primary Champion] Proximity score revised from 4 to 3 (Platform Security is a required audience and [Primary Champion] has no direct relationship there; secondary champion candidate identified in the Keep Satisfied quadrant). Triggered by: Phase 1 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency; champion proximity gap identified as a result.

For every amendment, update the affected structural target (grid, veto list, comms rows, Step 6a prefill, or champion scoring) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows, veto rank and mitigation entries, Step 6a prefill Frame Type assignments, Step 6b communication rows, champion depth scores and durability assessments. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-02 -- Single Axis: C-26 Deliberately Absent (175 expected)

**Axis**: Lifecycle emphasis -- V-01 R9 structure verbatim with both transition gates removed. All 25 non-C-26 criteria intact. Tests whether C-26 is independently excisable from the full v9 criterion set.

**Hypothesis**: C-26 fails (no between-phase transition gate steps present). All other 25 criteria pass unchanged. The correct phase sequence (Strategy -> UX -> PM) remains intact for C-15; FAIL labels within steps remain for C-17; all structural positions (C-18 through C-25) unaffected. Champion additions carry FAIL_NO_DURABILITY and are independently satisfiable. Expected: 175/180 (-C-26 = -5 pts).

**Deliberate loss**: C-26 (-5 pts). The two transition gates are removed. Phase boundary language replaced with standard "Run Phase 2 before building the grid" and "Build this grid now -- after Phase 1 and Phase 2 are complete" directives, which satisfy C-15 (correct order explicit) without the dedicated between-phase gate steps that C-26 requires.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Role ownership:**
- **Strategy role**: structural conflict identification (Step 1a), inertia stakeholder mapping (Step 1b), critical-path gatekeeper identification (Step 1c), veto risk ranking (Step 4), critical-path gatekeeper confirmation (Step 7)
- **UX role**: segment analysis and NOT-doing statements (Phase 2)
- **PM role**: org context check (Step 0), Power/Interest grid construction (Phase 3), champion identification, scoring, and durability (Step 5), Frame Type prefill (Step 6a), communication table (Step 6b), amendment pass (Step 8)

**On inertia stakeholders:** The most commonly underweighted stakeholders in a feature decision are those defending the current approach -- not because they are obstructionist, but because their workflow, standing, or system ownership is being displaced. This skill treats inertia analysis as a structural requirement, not an optional consideration. Every inertia stakeholder identified in Phase 1 will propagate to three downstream positions: a tagged row in the grid, a ranked veto entry, and a Frame Type assignment that acknowledges displacement. Missing any one of these three positions means the inertia signal was incomplete.

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

**Step 5a -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

**Step 5b -- Champion depth scoring -- PM role**

For each champion, score on three dimensions (1 = weak, 5 = strong):

| Champion | Authority (1-5) | Proximity (1-5) | Commitment (1-5) | Composite |
|----------|:---------------:|:---------------:|:----------------:|:---------:|

- **Authority**: Does their endorsement carry weight with the decision-makers who control veto risks?
- **Proximity**: How frequently do they interact with stakeholders who need to be moved?
- **Commitment**: How personally invested are they in this outcome -- would they advocate without prompting?

Composite = Authority + Proximity + Commitment (max 15). Champions scoring below 9 should be treated as supporting evidence, not primary movers -- identify a secondary champion or plan to build commitment before relying on them.

**Step 5c -- Champion durability -- PM role**

For each champion, assess:
- **Single-point-of-failure risk**: If this person moves to another role or leaves the org, does champion coverage collapse?
- **Succession**: Who is the next most likely champion in this stakeholder's network, and what would it take to activate them?
- **Deterioration signal**: What early sign would indicate this champion is losing commitment? (e.g., stops attending reviews, delegates to a lower-level proxy, starts hedging in steering conversations)

**FAIL_NO_DURABILITY**: A champion plan with a single named person and no succession or deterioration signal is a plan with a single point of failure.

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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Champion depth scoring updated -- [Primary Champion] Proximity score revised from 4 to 3 (Platform Security is a required audience and [Primary Champion] has no direct relationship there; secondary champion candidate identified in the Keep Satisfied quadrant). Triggered by: Phase 1 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency; champion proximity gap identified as a result.

For every amendment, update the affected structural target (grid, veto list, comms rows, Step 6a prefill, or champion scoring) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows, veto rank and mitigation entries, Step 6a prefill Frame Type assignments, Step 6b communication rows, champion depth scores and durability assessments. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-03 -- Single Axis: Conflict Resolution Pathway (180 expected + C-27 candidate)

**Axis**: Lifecycle emphasis -- all 26 criteria intact; new structured section added within Step 1a. For each conflict, a resolution pathway is required: named resolution authority, specific decision required, and deadline. Phase transition gates retained (C-26 satisfied). Champion sections not present (single-axis).

**Hypothesis**: All 26 criteria pass. Conflict resolution pathway is additive: it extends Step 1a without displacing C-06 (conflict identification), C-08 (critical-path gatekeepers), or C-25 (veto risk mitigation). FAIL_NO_RESOLUTION_PATHWAY fires at Step 1a when a conflict has no named authority. Distinct from C-25: mitigation lowers veto probability; a resolution pathway closes the underlying conflict by naming who decides and what they decide. A conflict can be fully mitigated and have no resolution authority. The Phase 1 -> Phase 2 gate checklist adds "resolution pathway present for each conflict" as a required Phase 1 output. Amendment mandate extended to include conflict resolution pathway entries as amendment-eligible targets. Expected: 180/180 + C-27 candidate.

**New C-27 candidate -- Conflict resolution pathway**: For each conflict in Phase 1, a structured entry naming (1) the resolution authority (named role, not "leadership"), (2) the decision required to close the conflict, and (3) the deadline for that decision. FAIL_NO_RESOLUTION_PATHWAY fires at the conflict step. Distinct from C-06 (identifies parties and tension), C-08 (timeline blockers), and C-25 (veto mitigation): resolution pathway closes the conflict structurally by naming the decision-making mechanism, not just responding to risk. Not satisfiable if C-06 is absent.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Role ownership:**
- **Strategy role**: structural conflict identification and resolution pathways (Step 1a), inertia stakeholder mapping (Step 1b), critical-path gatekeeper identification (Step 1c), veto risk ranking (Step 4), critical-path gatekeeper confirmation (Step 7)
- **UX role**: segment analysis and NOT-doing statements (Phase 2)
- **PM role**: org context check (Step 0), Power/Interest grid construction (Phase 3), champion identification (Step 5), Frame Type prefill (Step 6a), communication table (Step 6b), amendment pass (Step 8), phase transition gates

---

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Structural conflict, inertia, and critical-path analysis -- Strategy role

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

**Step 1a -- Structural conflicts and resolution pathways -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

For each conflict, specify a resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|

- **Resolution Authority**: the named role or team who has the standing to make the call that closes this conflict. "Leadership" is not a named authority. "VP of Engineering" or "Platform Steering Committee" are named authorities.
- **Decision Required**: the specific agreement that would end the conflict. "Alignment" is not a decision. "Confirm whether auth token scope changes require Platform Security sign-off before merge" is a decision.
- **Deadline**: when this decision must be made to avoid impacting the critical path. Derive from the earliest `[CRITICAL PATH]` lead time where the conflict intersects.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**FAIL_NO_RESOLUTION_PATHWAY**: A conflict without a named resolution authority and specific required decision is an observation, not a plan. Both fields are required per conflict entry.

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

**Phase 1 -> Phase 2 Transition Gate -- PM role**

Before proceeding to Phase 2, confirm all Phase 1 outputs are present:

- At least two structural conflicts named, each with both parties, tension type, and resolution pathway (authority + decision + deadline)
- Inertia sub-step completed (or explicitly noted as "no inertia stakeholders found")
- Each inertia stakeholder entry includes: current approach, displaced-by, displacement type, veto probability
- At least one critical-path gatekeeper flagged with lead time or deadline

**FAIL_INCOMPLETE_PHASE1**: Do not proceed to Phase 2 if any required output above is absent. Phase 2's NOT-doing statements depend on the displacement vocabulary established in Step 1b. A grid built without Phase 1 conflict data will have incomplete Source labels and underweighted veto entries.

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

**Phase 2 -> Phase 3 Transition Gate -- PM role**

Before building the grid in Phase 3, confirm all Phase 2 outputs are present:

- Every user segment has a NOT-doing statement
- Any non-monolithic groups have been split into sub-segments where warranted
- All rows introduced during segment analysis carry Source = `segment-analysis`
- Inertia stakeholder NOT-doing statements address displacement loss specifically (not generic absence)

**FAIL_INCOMPLETE_PHASE2**: Do not proceed to Phase 3 if any required output above is absent. Grid rows built before segment analysis is complete will carry unresolved Source = `initial-inventory` labels that should have been reclassified before construction, not during the amendment pass.

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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Resolution pathway updated -- Platform Security conflict added: Authority = VP Engineering, Decision Required = confirm auth token sign-off requirement before merge, Deadline = T-6 weeks. Triggered by: Phase 1 conflict between Engineering and Identity Platform surfaced undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; resolution authority identified as VP Engineering.

For every amendment, update the affected structural target (grid, veto list, comms rows, Step 6a prefill, or conflict resolution pathways) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows, veto rank and mitigation entries, Step 6a prefill Frame Type assignments, Step 6b communication rows, conflict resolution pathway entries. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-04 -- Single Axis: Stakeholder Engagement Window (180 expected + C-28 candidate)

**Axis**: Output format -- all 26 criteria intact; Power/Interest grid gains an "Engagement Window" column; a new Step 5a derives per-quadrant windows before Step 6b. Communication timing in Step 6b must fall within the derived window. Phase transition gates retained (C-26 satisfied). Champion depth and durability not present (single-axis).

**Hypothesis**: All 26 criteria pass. Engagement window is additive: extends the grid output format and introduces a timing-validation gate without displacing C-02 (grid structure), C-05 (comms timing per quadrant), C-19 (prefill as distinct step), or C-26 (transition gates). Distinct from C-05: C-05 requires timing present per quadrant row; engagement window requires timing to align with the stakeholder's receptiveness window. A comms row can satisfy C-05 (has timing) and fail the window check (timing outside window). FAIL_WINDOW_MISMATCH fires at Step 6b. FAIL_NO_ENGAGEMENT_WINDOW fires at Phase 3 grid. FAIL_NO_WINDOW_SUMMARY fires at Step 5a. Expected: 180/180 + C-28 candidate.

**New C-28 candidate -- Stakeholder engagement window**: A dedicated pre-comms step (Step 5a) derives a per-quadrant engagement window from the grid's Engagement Window column. Communication row timing in Step 6b must fall within the derived window. FAIL_WINDOW_MISMATCH fires when timing is outside the window; FAIL_NO_ENGAGEMENT_WINDOW fires at grid construction when a row is missing a window. Distinct from C-05 (timing present) and C-08 (critical-path lead times). Not satisfiable if C-05 is absent.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Role ownership:**
- **Strategy role**: structural conflict identification (Step 1a), inertia stakeholder mapping (Step 1b), critical-path gatekeeper identification (Step 1c), veto risk ranking (Step 4), critical-path gatekeeper confirmation (Step 7)
- **UX role**: segment analysis and NOT-doing statements (Phase 2)
- **PM role**: org context check (Step 0), Power/Interest grid construction (Phase 3), engagement window summary (Step 5a), champion identification (Step 5b), Frame Type prefill (Step 6a), communication table (Step 6b), amendment pass (Step 8), phase transition gates

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

**Phase 1 -> Phase 2 Transition Gate -- PM role**

Before proceeding to Phase 2, confirm all Phase 1 outputs are present:

- At least two structural conflicts named, each with both parties and tension type explicitly stated
- Inertia sub-step completed (or explicitly noted as "no inertia stakeholders found")
- Each inertia stakeholder entry includes: current approach, displaced-by, displacement type, veto probability
- At least one critical-path gatekeeper flagged with lead time or deadline

**FAIL_INCOMPLETE_PHASE1**: Do not proceed to Phase 2 if any required output above is absent. Phase 2's NOT-doing statements depend on the displacement vocabulary established in Step 1b. A grid built without Phase 1 conflict data will have incomplete Source labels and underweighted veto entries.

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

**Phase 2 -> Phase 3 Transition Gate -- PM role**

Before building the grid in Phase 3, confirm all Phase 2 outputs are present:

- Every user segment has a NOT-doing statement
- Any non-monolithic groups have been split into sub-segments where warranted
- All rows introduced during segment analysis carry Source = `segment-analysis`
- Inertia stakeholder NOT-doing statements address displacement loss specifically (not generic absence)

**FAIL_INCOMPLETE_PHASE2**: Do not proceed to Phase 3 if any required output above is absent. Grid rows built before segment analysis is complete will carry unresolved Source = `initial-inventory` labels that should have been reclassified before construction, not during the amendment pass.

---

## Phase 3 -- Power/Interest grid construction -- PM role

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Engagement Window | Source | Notes |
|-------------|---------------|------------------|----------|-----------|-------------------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

**Engagement Window**: The calendar period during which this stakeholder's influence is highest or their receptiveness to input is greatest. Expressed as a relative range: "T-8 to T-4 weeks", "T-2 weeks to T-0", "day of announcement only". Rules: (1) for critical-path stakeholders, the window must not extend past their lead time; (2) for inertia stakeholders, the window must open before any public announcement -- displacement signals received post-announcement carry higher veto risk.

Every inertia stakeholder from Step 1b must appear here with `[INERTIA]` in the designated column. All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 1b appearing without `[INERTIA]` in the designated column is an incomplete row. This column is not a Notes annotation -- it is a required structural marker.

**FAIL_NO_ENGAGEMENT_WINDOW**: A grid row without an Engagement Window entry cannot be used to validate communication timing. Every row requires a window.

---

**Step 4 -- Veto risk ranking -- Strategy role**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank. Do not underrate structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5a -- Engagement window summary -- PM role**

Before assigning Frame Types or writing communication rows, derive a per-quadrant engagement window from the grid. The quadrant window is the intersection of all row windows in that quadrant -- the period during which all stakeholders in the quadrant are reachable simultaneously. If a quadrant has only one stakeholder, that stakeholder's window is the quadrant window.

| Quadrant | Engagement Window (derived) | Binding Constraint |
|----------|----------------------------|-------------------|

The Binding Constraint column names the stakeholder whose window is the narrowest (earliest close or latest open). Communication timing in Step 6b must fall within this derived window.

**FAIL_NO_WINDOW_SUMMARY**: Proceeding to Step 6b without derived quadrant windows means communication timing cannot be validated against stakeholder receptiveness. Complete this step before Step 6b.

**Step 5b -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action. Champion actions must be scheduled within the champion's engagement window from Phase 3.

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

Using the Frame Types assigned in Step 6a and the engagement windows derived in Step 5a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing -- do not change values during row population.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before". Timing must fall within the derived engagement window for the quadrant from Step 5a.

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

**FAIL_WINDOW_MISMATCH**: Timing that falls outside the derived engagement window for the quadrant means the communication will reach the stakeholder outside their receptiveness peak. Return to Step 5a and revise the window derivation or adjust timing.

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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Engagement Window: T-8 to T-4 weeks, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 5a window summary updated -- Keep Satisfied derived window revised to T-8 to T-4 weeks (Platform Security is the binding constraint; their sign-off window closes at T-4 weeks). Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to T-6 weeks (within updated window). Triggered by: Phase 1 conflict between Engineering and Identity Platform surfaced undisclosed sign-off dependency. What changed: Platform Security absent from initial-inventory; engagement window tightened for Keep Satisfied quadrant.

For every amendment, update the affected structural target (grid, veto list, comms rows, Step 6a prefill, or engagement window summary) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows (including Engagement Window column), veto rank and mitigation entries, Step 5a quadrant window summaries, Step 6a prefill Frame Type assignments, Step 6b communication rows. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-05 -- Combination: All 26 + Champion Depth/Durability + Conflict Resolution Pathway + Engagement Window (180 expected + multiple candidates)

**Axes**: All 26 criteria + champion depth scoring (Step 5c) + champion durability (Step 5d) from V-01 R9 + conflict resolution pathway from V-03 + engagement window column and Step 5a from V-04. Phase transition gates (C-26) present. Amendment mandate and correct-form example cover all new amendment-eligible targets.

**Hypothesis**: All 26 criteria pass simultaneously with all four additive axes. Conflict resolution pathway table in Step 1a extends the Phase 1 -> Phase 2 gate checklist without disrupting C-06, C-08, or C-25. Engagement window column in the grid and derived window in Step 5a extend C-02 and C-05 without disrupting C-19 (Step 6a prefill remains a distinct step before Step 6b). Champion scoring and durability (Steps 5c-5d) remain independent of resolution pathway and window axes. The four axes are mutually non-interfering: each adds to a different structural layer (conflict analysis, grid format, comms timing, champion assessment). Amendment mandate extended to cover all new targets. Expected: 180/180 + C-27 (conflict resolution pathway), C-28 (engagement window), C-29 (champion quantification depth), C-30 (champion durability) as v10 candidates.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Role ownership:**
- **Strategy role**: structural conflict identification and resolution pathways (Step 1a), inertia stakeholder mapping (Step 1b), critical-path gatekeeper identification (Step 1c), veto risk ranking (Step 4), critical-path gatekeeper confirmation (Step 7)
- **UX role**: segment analysis and NOT-doing statements (Phase 2)
- **PM role**: org context check (Step 0), Power/Interest grid construction (Phase 3), engagement window summary (Step 5a), champion identification, scoring, and durability (Steps 5b-5d), Frame Type prefill (Step 6a), communication table (Step 6b), amendment pass (Step 8), phase transition gates

**On inertia stakeholders:** The most commonly underweighted stakeholders in a feature decision are those defending the current approach -- not because they are obstructionist, but because their workflow, standing, or system ownership is being displaced. This skill treats inertia analysis as a structural requirement, not an optional consideration. Every inertia stakeholder identified in Phase 1 will propagate to three downstream positions: a tagged row in the grid, a ranked veto entry, and a Frame Type assignment that acknowledges displacement. Missing any one of these three positions means the inertia signal was incomplete.

---

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Structural conflict, inertia, and critical-path analysis -- Strategy role

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

**Step 1a -- Structural conflicts and resolution pathways -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

For each conflict, specify a resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|

- **Resolution Authority**: the named role or team with standing to make the resolving call. "Leadership" is not a named authority.
- **Decision Required**: the specific agreement that closes the conflict. "Alignment" is not a decision.
- **Deadline**: when this decision must be made to avoid critical-path impact.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**FAIL_NO_RESOLUTION_PATHWAY**: A conflict without a named resolution authority and specific required decision is an observation, not a plan.

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

**Phase 1 -> Phase 2 Transition Gate -- PM role**

Before proceeding to Phase 2, confirm all Phase 1 outputs are present:

- At least two structural conflicts named, each with both parties, tension type, and resolution pathway (authority + decision + deadline)
- Inertia sub-step completed (or explicitly noted as "no inertia stakeholders found")
- Each inertia stakeholder entry includes: current approach, displaced-by, displacement type, veto probability
- At least one critical-path gatekeeper flagged with lead time or deadline

**FAIL_INCOMPLETE_PHASE1**: Do not proceed to Phase 2 if any required output above is absent. Phase 2's NOT-doing statements depend on the displacement vocabulary established in Step 1b. A grid built without Phase 1 conflict data will have incomplete Source labels and underweighted veto entries.

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

**Phase 2 -> Phase 3 Transition Gate -- PM role**

Before building the grid in Phase 3, confirm all Phase 2 outputs are present:

- Every user segment has a NOT-doing statement
- Any non-monolithic groups have been split into sub-segments where warranted
- All rows introduced during segment analysis carry Source = `segment-analysis`
- Inertia stakeholder NOT-doing statements address displacement loss specifically (not generic absence)

**FAIL_INCOMPLETE_PHASE2**: Do not proceed to Phase 3 if any required output above is absent. Grid rows built before segment analysis is complete will carry unresolved Source = `initial-inventory` labels that should have been reclassified before construction, not during the amendment pass.

---

## Phase 3 -- Power/Interest grid construction -- PM role

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Engagement Window | Source | Notes |
|-------------|---------------|------------------|----------|-----------|-------------------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

**Engagement Window**: The calendar period during which this stakeholder's influence is highest or their receptiveness to input is greatest. Expressed as a relative range: "T-8 to T-4 weeks", "T-2 weeks to T-0", "day of announcement only". For critical-path stakeholders, the window must not extend past their lead time. For inertia stakeholders, the window must open before any public announcement.

Every inertia stakeholder from Step 1b must appear here with `[INERTIA]` in the designated column. All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 1b appearing without `[INERTIA]` in the designated column is an incomplete row. This column is not a Notes annotation -- it is a required structural marker.

**FAIL_NO_ENGAGEMENT_WINDOW**: A grid row without an Engagement Window entry cannot be used to validate communication timing. Every row requires a window.

---

**Step 4 -- Veto risk ranking -- Strategy role**

List veto risks ordered by probability -- highest first. Every `[INERTIA]` stakeholder must appear at their true probability rank. Do not underrate structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5a -- Engagement window summary -- PM role**

Before assigning Frame Types or writing communication rows, derive a per-quadrant engagement window from the grid. The quadrant window is the intersection of all row windows in that quadrant.

| Quadrant | Engagement Window (derived) | Binding Constraint |
|----------|----------------------------|-------------------|

The Binding Constraint column names the stakeholder whose window is narrowest. Communication timing in Step 6b must fall within this derived window.

**FAIL_NO_WINDOW_SUMMARY**: Proceeding to Step 6b without derived quadrant windows means communication timing cannot be validated against stakeholder receptiveness.

**Step 5b -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action within the champion's engagement window from Phase 3.

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

**Step 5c -- Champion depth scoring -- PM role**

For each champion, score on three dimensions (1 = weak, 5 = strong):

| Champion | Authority (1-5) | Proximity (1-5) | Commitment (1-5) | Composite |
|----------|:---------------:|:---------------:|:----------------:|:---------:|

- **Authority**: Does their endorsement carry weight with the decision-makers who control veto risks?
- **Proximity**: How frequently do they interact with stakeholders who need to be moved?
- **Commitment**: How personally invested are they in this outcome -- would they advocate without prompting?

Composite = Authority + Proximity + Commitment (max 15). Champions scoring below 9 should be treated as supporting evidence, not primary movers.

**Step 5d -- Champion durability -- PM role**

For each champion, assess:
- **Single-point-of-failure risk**: If this person moves to another role or leaves the org, does champion coverage collapse?
- **Succession**: Who is the next most likely champion in this stakeholder's network, and what would it take to activate them?
- **Deterioration signal**: What early sign would indicate this champion is losing commitment? (e.g., stops attending reviews, delegates to a lower-level proxy, starts hedging in steering conversations)

**FAIL_NO_DURABILITY**: A champion plan with a single named person and no succession or deterioration signal is a plan with a single point of failure.

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

Using the Frame Types assigned in Step 6a and the engagement windows derived in Step 5a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. If the assigned Frame Type feels wrong for a quadrant, return to Step 6a and reassign before continuing -- do not change values during row population.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before". Timing must fall within the derived engagement window for the quadrant from Step 5a.

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

**FAIL_WINDOW_MISMATCH**: Timing that falls outside the derived engagement window for the quadrant means the communication is misaligned with stakeholder receptiveness.

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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Engagement Window: T-8 to T-4 weeks, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Resolution pathway updated -- Platform Security conflict added: Authority = VP Engineering, Decision Required = confirm auth token sign-off requirement before merge, Deadline = T-6 weeks. Step 5a window summary updated -- Keep Satisfied derived window revised to T-8 to T-4 weeks (Platform Security is the binding constraint). Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to T-6 weeks (within updated window). Champion depth scoring updated -- [Primary Champion] Proximity score revised from 4 to 3 (Platform Security is a required audience and [Primary Champion] has no direct relationship there; secondary champion candidate identified). Triggered by: Phase 1 conflict between Engineering and Identity Platform surfaced undisclosed sign-off dependency. What changed: Platform Security absent from initial-inventory; engagement window tightened; resolution authority identified; champion proximity gap confirmed.

For every amendment, update the affected structural target (grid, veto list, comms rows, Step 6a prefill, conflict resolution pathways, engagement window summary, or champion scoring) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows (including Engagement Window column), veto rank and mitigation entries, conflict resolution pathway entries, Step 5a quadrant window summaries, Step 6a prefill Frame Type assignments, Step 6b communication rows, champion depth scores and durability assessments. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.
