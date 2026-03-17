Written to `simulations/quest/variations/scout-stakeholders-variations-R8-2026-03-14.md`.

---

## Round 8 — scout-stakeholders — V-01 through V-05

### Design Summary

| ID | Axis | C-15 | C-19 | C-20 | C-23 | C-24 | C-25 | Expected |
|----|------|:----:|:----:|:----:|:----:|:----:|:----:|:--------:|
| V-01 | Lifecycle: phase-transition confirmation gates | ++ | ++ | ++ | ++ | ++ | ++ | 175 |
| V-02 | Role sequence: UX-first | -- | ++ | ++ | ++ | ++ | ++ | ~170 |
| V-03 | Phrasing register: coaching voice | -- | ++ | -- | -- | -- | -- | ~120 |
| V-04 | UX-first + 6a/6b merged | -- | ?? | -- | ++ | ++ | ++ | ~155 |
| V-05 | All 25 + champion scoring + champion durability | ++ | ++ | ++ | ++ | ++ | ++ | 175+ |

---

### V-01 — Phase-Transition Confirmation Gates (175 expected)

**Single axis.** V-01 R7 structure verbatim with two new gates inserted: a `Phase 1 -> Phase 2 Transition Gate` listing required Phase 1 outputs as prerequisites (FAIL_INCOMPLETE_PHASE1), and a `Phase 2 -> Phase 3 Transition Gate` doing the same for Phase 2 (FAIL_INCOMPLETE_PHASE2). All 25 existing criteria survive unchanged — FAIL labels at gate-level extend C-17 coverage without replacing any existing label, and all structural positions (C-18, C-19, C-20, C-22, C-23, C-24, C-25) are unaffected.

**C-26 candidate**: phase-gate prerequisite confirmation — a gate that lists required prior-phase outputs as explicit prerequisites with a FAIL label at the transition. Round 8 scoring will determine whether this is independently satisfiable.

---

### V-02 — Role Sequence: UX-First (170 expected)

**Single axis.** Phase 1 becomes segment analysis (UX role), Phase 2 becomes conflict + inertia + critical-path (Strategy role), Phase 3 is PM grid. Inertia mapping moves to Step 2b and still propagates to three downstream positions. The amendment correct-form example is updated to reference "Phase 2 conflict" as the trigger (matching the new phase numbering). All 24 non-C-15 criteria intact.

**Deliberate loss**: C-15 (-5 pts). Tests whether C-15 is independently excisable from the v8 full set with UX-first rather than PM-first as the sequence violation.

---

### V-03 — Coaching Voice (~120 expected)

**Single axis.** All imperative instructions replaced with second-person coaching register throughout. FAIL labels replaced with "Watch out for" / "A common mistake here is" phrasing. Phase-order mandate ("Run Phase 1 first") softened to advisory ("Start here, before you build any grid or table").

**Deliberate losses**: C-14 and C-17 (no formal FAIL-label names), C-15 (coaching order framing is soft), C-16 (bad/correct form pair becomes a narrative example without the formal "Bad form / Correct form" label structure), C-24 (no mandate sentence to embed prohibition in), C-25 (FAIL_NO_MITIGATION label absent). C-19 survives (prefill table is still a distinct required block). The amendment example survives in coaching form with an update structure. Final score depends on whether the coaching-style prefill block satisfies C-19 and whether advisory language in the inertia step satisfies C-18.

---

### V-04 — UX-First + 6a/6b Merged (~155 expected)

**Combination.** UX-first phase order (C-15 absent). Steps 6a and 6b merged into a single numbered "Step 6" with labeled sub-parts "Part A: prefill" and "Part B: populate." The key question for scoring: does a sub-part within a step qualify as a "distinct step" for C-19 ("standalone prefill table... as a *distinct step* before the comms table is populated")? If not, C-19 fails. If C-19 fails, C-20 and C-21 also fail by dependency. Amendment mandate is updated to reference "Step 6 Part A" as the prefill update target — C-22 and C-24 survive at the mandate level regardless of C-19/C-20 outcome.

---

### V-05 — All 25 + Champion Depth + Durability (175+ expected)

**Combination.** All 25 criteria intact. Three additions:

1. **Champion depth scoring** (Step 5 Part B): authority/proximity/commitment scores (1-5 each), composite (max 15), FAIL_NO_DURABILITY label.
2. **Champion durability** (Step 5 Part C): SPOF risk, succession candidate, deterioration signal.
3. **Inertia-primary preamble**: opening framing paragraph positioning inertia analysis as the structural core.
4. **Extended amendment example**: correct-form example includes a champion depth score revision as an amendment-eligible target ("Champion depth scoring updated -- [Champion] Proximity score revised from 4 to 3...").

**C-26 candidate**: champion quantification depth — scoring scale + composite + FAIL label at the champion step.  
**C-27 candidate**: champion durability — succession + deterioration signal fields per champion entry.
ut asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

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

- Every user segment identified has a NOT-doing statement
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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Phase 1 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment, update the affected structural target (grid, veto list, comms rows, or Step 6a prefill) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows, veto rank and mitigation entries, Step 6a prefill Frame Type assignments, Step 6b communication rows. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 1b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-02 -- Single Axis: Role Sequence (UX First)

**Axis**: Role sequence -- Phase 1 becomes segment analysis (UX role), Phase 2 becomes structural conflict + inertia + critical-path (Strategy role), Phase 3 is PM grid as before
**Hypothesis**: UX-first violates C-15 (which mandates Strategy -> UX -> PM: "conflict/strategy analysis first, UX segment analysis second, PM grid construction last"). All other 24 criteria are satisfiable with UX-first ordering. Inertia mapping lives in Phase 2 (now the Strategy role phase) and propagates to three downstream positions unchanged. FAIL saturation (C-17) survives since gates are within steps, not between phases. Amendment mandate retains "no observation without revision" prohibition (C-24). Veto risk mitigation column retained (C-25). Role labels in headings (C-23) survive since the heading format is unchanged. Expected: ~170/175 (-C-15 = -5 pts).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Segment analysis and NOT-doing statements -- UX role

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 2 -- Structural conflict, inertia, and critical-path analysis -- Strategy role

**Run Phase 2 after Phase 1. Apply segment findings to conflict and inertia analysis.**

**Step 2a -- Structural conflicts -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**Step 2b -- Inertia stakeholder mapping -- Strategy role**

Identify stakeholders whose primary relationship to this decision is defending the status quo -- those who benefit from the current approach, whose role diminishes if the product succeeds, or whose workflow depends on what is being replaced.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` (their process changes) | `political` (their standing diminishes) | `ownership` (they lose control of a system)
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

Update Phase 1 NOT-doing statements for any inertia stakeholder identified here: their NOT-doing statement must address the loss signal -- what the new approach does not preserve from the current approach.

This stakeholder tracks through three downstream positions: `[INERTIA]` tag in the Phase 3 grid, a ranked veto entry in Step 4, and `displacement-acknowledgment` assigned in the Step 6a prefill table.

**FAIL_NO_INERTIA**: Omitting this sub-step means the `[INERTIA]` tag will be absent from the grid and the `displacement-acknowledgment` prefill assignment will not be made. The omission propagates to three downstream positions.

**Step 2c -- Critical-path gatekeeper identification -- Strategy role**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

## Phase 3 -- Power/Interest grid construction -- PM role

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 2
- `segment-analysis`: surfaced in Phase 1
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Every inertia stakeholder from Step 2b must appear here with `[INERTIA]` in the designated column. All critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder from Step 2b appearing without `[INERTIA]` in the designated column is an incomplete row. This column is not a Notes annotation -- it is a required structural marker.

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
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. Assign the correct value here, in the prefill step, not during row content population in Step 6b.
4. Do not proceed to Step 6b until all four assignments are complete, distinct, and match the rules above.
5. Values not in the accepted list above are not permitted.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the inertia stakeholder's quadrant is not assigned `displacement-acknowledgment` in this prefill table, correct the assignment before proceeding. Three-position inertia elevation requires this assignment at the prefill stage.

---

**Step 6b -- Communication table -- PM role**

Using the Frame Types assigned in Step 6a, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Step 6a assignments exactly. Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the Step 6a assignment was not honored. Return to Step 6a.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-path gatekeeper confirmation -- Strategy role**

For each `[CRITICAL PATH]` stakeholder confirmed in Step 2c:
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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Phase 2 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment, update the affected structural target (grid, veto list, comms rows, or Step 6a prefill) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows, veto rank and mitigation entries, Step 6a prefill Frame Type assignments, Step 6b communication rows. Set Source = `amendment` on new rows. If the amendment introduces an inertia-adjacent stakeholder, update Step 2b displacement vocabulary, tag the new row `[INERTIA]` in Phase 3, return to Step 6a and reassign Frame Types if needed, then update Step 6b. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified signals that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

---

## V-03 -- Single Axis: Phrasing Register (Coaching Voice)

**Axis**: Phrasing register -- all imperative instructions converted to second-person coaching voice throughout
**Hypothesis**: Coaching register naturally omits formal FAIL-label naming (C-14, C-17), disrupts the reversed-sequence mandate framing (C-15, which depends on an explicit "Run Phase 1 first" command), and loses the formal before/after amendment pair (C-16, which requires adjacent labeled bad/correct examples in imperative form). C-24 (inline prohibition clause in mandate sentence) fails because coaching voice replaces mandate sentences with advisory guidance. C-25 (FAIL_NO_MITIGATION label) fails because coaching register uses "Watch out for" phrasing instead of formal FAIL labels. C-19 (prefill as distinct step) may survive if the coaching language still presents it as a required constraint block before row population. C-18 (inertia three-position elevation) may partially survive if the three positions are still named in the body text. Expected: ~120/175.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Getting started: do you know who you're mapping?**

Before any stakeholder work, check whether the repo has a CODEOWNERS file. If it does, those team names are your starting inventory -- pull them in with a note that they came from CODEOWNERS. If there's no CODEOWNERS file, look at the invocation string for context. If you genuinely can't tell, just ask:

> "What org or team is this decision for?"

Don't try to guess. A wrong assumption about org structure is harder to recover from than one clarifying question.

---

## Phase 1 -- Finding the structural conflicts (Strategy lens)

**Start here, before you build any grid or table.**

**Understanding the conflict landscape**

You're looking for tensions where two named groups are in genuine opposition -- not just one person having concerns, but two parties who want different things. Try to find at least two. For each one, write it as:

> [Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]

And note whether it carries veto risk.

If you can only name one party, that's a concern, not a conflict. Keep looking.

**The stakeholders who benefit from the current approach**

Some stakeholders aren't opposed to your feature because of your feature -- they're opposed because something they currently own, depend on, or lead gets displaced by it. These are your inertia stakeholders. It's worth looking for them explicitly.

For each one, try to capture:
- What do they rely on today that this decision changes?
- What specifically replaces it?
- Is the displacement primarily about their workflow, their standing, or their system ownership?
- If you're unsure of their resistance level, default to Medium -- you can revise later

If you don't find any, it's worth saying so explicitly. They often hide in "neutral" grid entries.

These stakeholders will reappear in three places later: the grid (marked with an inertia tag), the veto list (where they often rank higher than expected), and the communication table (where their frame should acknowledge displacement, not just tout what's being gained).

**Who controls the clock?**

Some stakeholders don't need to oppose you to block you -- they just need a deadline or approval window you haven't accounted for. Flag any gatekeeper whose sign-off constrains your timeline. Be specific about the lead time.

---

## Phase 2 -- User segment analysis (UX lens)

**Walk through your user segments before building the grid.**

For each segment you're serving, think through:
- What's their role or primary use pattern?
- What do they gain from this decision?
- What becomes harder or disappears for them?
- What is this product explicitly *not* doing for them? (Write one clear "we are not..." statement per segment)

For inertia stakeholders from Phase 1: their "not doing" statement should address what the new approach doesn't preserve from the current one -- the thing they're losing, not just a generic gap.

If a segment isn't really monolithic -- if part of the group has very different interests than the rest -- split them now. You'll want those distinctions in the grid.

---

## Phase 3 -- Building the Power/Interest grid (PM lens)

**Now that you have conflict data and segment data, build the grid.**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

A few things to track per row:
- Where did this stakeholder come from? Use labels like `CODEOWNERS`, `conflict-discovered`, `segment-analysis`, `initial-inventory`, or `amendment`
- Inertia stakeholders from Phase 1 need a marker in the [INERTIA] column -- that column isn't a note, it's a required structural tag
- Critical-path gatekeepers should have their lead time in Notes

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

You need at least 4 rows. A prose list without a table won't work here.

---

**Step 4 -- Veto risk list (Strategy lens)**

Take the veto risks from Phase 1 and order them by probability -- most likely first. Alphabetical or grid-sequence order isn't useful here.

For each entry, include probability, impact, and a mitigation approach. A risk without a mitigation is an observation, not a plan. Watch out for entries that name a risk but don't address what you'd actually do about it.

| Rank | Stakeholder | Probability | Impact | Mitigation |

---

**Step 5 -- Champion identification (PM lens)**

Pick one or more champions from the grid and write a specific action for each. Specific means it could go on a calendar:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

"Engage champion" or "keep informed" doesn't count as an action.

---

**Step 6a -- Assigning Frame Types before writing messages**

Before you write any communication row content, fill in this prefill table. It constrains what goes in the Frame Type column of your communication table -- only these values are allowed, and no two rows can share the same one.

| Quadrant | Frame Type |
|----------|------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

Values you can use:
- `displacement-acknowledgment`
- `risk-mitigation`
- `value-capture`
- `compliance-alignment`
- `awareness-only`
- `co-ownership`

One per row, no repeats. If you have an inertia stakeholder in a quadrant, that quadrant should get `displacement-acknowledgment` -- they need to hear that you understand what's changing for them, not just what's being gained. Make that assignment here, before you write the row content.

---

**Step 6b -- Communication table**

Now write the full row content, using the Frame Types you assigned above.

| Quadrant | Key Message | Frame Type | Timing | Owner |

Match your Frame Types exactly to the prefill. For timing, use a specific interval: "3 weeks before launch", "day of announcement", "6 weeks before".

---

**Step 7 -- Gatekeeper confirmation (Strategy lens)**

For each critical-path stakeholder from Phase 1, confirm:
- What specifically blocks if they haven't signed off?
- What's the minimum lead time or hard deadline?

---

**Step 8 -- Amendment pass**

Go back through everything above with fresh eyes. What did the initial map miss? What was collapsed that should be split? What quadrant placement looks wrong now?

When you find something, update the relevant table or list -- don't just note it. Here's what a good amendment looks like:

> **Amendment 1**: Grid updated -- [Stakeholder] added ([Quadrant], [Power/Interest], Source: amendment). Veto list updated -- [veto] ranked at [probability] with mitigation: [action]. Step 6a prefill updated -- [Quadrant] Frame Type reassigned from `[old]` to `[new]`; Step 6b row revised accordingly, Timing set to [interval]. Triggered by: [what surfaced this]. What changed: [delta from initial map].

The goal is a revision, not an observation. If all you can write is "it might be worth considering..." then you haven't run the amendment yet.

After amendments, look at any rows still tagged `initial-inventory`. If they haven't been reclassified, think about whether Phase 1 or Phase 2 missed something.

---

## V-04 -- Combination: UX-First + Steps 6a/6b Merged

**Axes**: Role sequence (UX first: UX -> Strategy -> PM) + output format (Steps 6a and 6b merged into a single combined prefill-and-populate step labeled "Step 6")
**Hypothesis**: UX-first violates C-15 (-5 pts). Merging 6a and 6b into a single combined step labeled "Step 6 -- Part A: prefill, Part B: populate" threatens C-19 ("a standalone prefill table... appears as a *distinct step* before the comms table is populated" -- the step number is shared, so Part A may not qualify as a distinct step) and C-20 ("must be stated as an explicit rule within the prefill step -- not as a note during content population" -- if Part A and Part B are in the same numbered step, the structural separation that makes C-20 testable disappears). C-24 and C-25 unaffected by the merge. Role labels in headings (C-23) intact. Expected: ~155-160/175 (-C-15, possibly -C-19 and/or -C-20).

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org context check -- PM role**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first gate.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Segment analysis and NOT-doing statements -- UX role

**Run Phase 1 first. The Power/Interest Grid is built in Phase 3, after this phase and Phase 2 are complete.**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 2 -- Structural conflict, inertia, and critical-path analysis -- Strategy role

**Step 2a -- Structural conflicts -- Strategy role**

Identify at least two structural conflicts. For each, name both parties and the nature of the tension:

> **[Group A] vs. [Group B] -- [nature: resource | priority | scope | process | compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**Step 2b -- Inertia stakeholder mapping -- Strategy role**

Identify stakeholders whose primary relationship to this decision is defending the status quo.

For each inertia stakeholder, record:
- **Current approach**: what they depend on today
- **Displaced-by**: what this decision introduces in its place
- **Displacement type**: `workflow` | `political` | `ownership`
- **Default veto probability**: Medium unless evidence explicitly supports a lower rating

This sub-step is mandatory. If no inertia stakeholders exist, state that explicitly.

Update Phase 1 NOT-doing statements for any inertia stakeholder identified here: their NOT-doing statement must address what the new approach does not preserve from the current approach.

This stakeholder tracks through three downstream positions: `[INERTIA]` tag in the Phase 3 grid, a ranked veto entry in Step 4, and `displacement-acknowledgment` assigned in the Step 6 prefill block.

**FAIL_NO_INERTIA**: Omitting this sub-step means the `[INERTIA]` tag will be absent from the grid and the displacement-acknowledgment assignment will not be made. The omission propagates to three downstream positions.

**Step 2c -- Critical-path gatekeeper identification -- Strategy role**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

## Phase 3 -- Power/Interest grid construction -- PM role

**Build this grid now -- after Phase 1 and Phase 2 are complete.**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | [INERTIA] | Source | Notes |
|-------------|---------------|------------------|----------|-----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 2
- `segment-analysis`: surfaced in Phase 1
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`

Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

**FAIL_MISSING_INERTIA_TAG**: An inertia stakeholder appearing without `[INERTIA]` in the designated column is an incomplete row.

---

**Step 4 -- Veto risk ranking -- Strategy role**

List veto risks ordered by probability -- highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action.

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6 -- Frame Type assignment and communication table -- PM role**

This step has two parts. Complete Part A fully before writing any row content in Part B.

**Part A -- Frame Type prefill**

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
3. The quadrant row containing any `[INERTIA]` stakeholder must be assigned `displacement-acknowledgment`. A value-capture or risk-mitigation frame for an inertia stakeholder's quadrant does not acknowledge displacement -- assign the correct value here in Part A, before writing any row content in Part B.
4. Do not proceed to Part B until all four assignments are complete, distinct, and match the rules above.
5. Values not in the accepted list above are not permitted.

**FAIL_MISSING_DISPLACEMENT_PREFILL**: If the inertia stakeholder's quadrant is not assigned `displacement-acknowledgment` in Part A, correct the assignment before proceeding to Part B.

**Part B -- Communication table**

Using the Frame Types assigned in Part A, populate the full communication table.

| Quadrant | Key Message | Frame Type | Timing | Owner |

The Frame Type column must match Part A assignments exactly. Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means Part A assignment was not honored. Return to Part A.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-path gatekeeper confirmation -- Strategy role**

For each `[CRITICAL PATH]` stakeholder from Step 2c:
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
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- authentication sign-off veto added at High probability, ranked above existing Medium-probability risks. Step 6 Part A updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Part B row revised accordingly, Timing set to 6 weeks before launch. Triggered by: Phase 2 conflict between Engineering and Identity Platform over auth token scope surfaced an undisclosed sign-off dependency. What changed: Platform Security was absent from initial-inventory.

For every amendment, update the affected structural target (grid, veto list, comms rows, or Step 6 Part A prefill assignments) -- no observation without revision. Update targets eligible for amendment: Power/Interest grid rows, veto rank and mitigation entries, Step 6 Part A Frame Type assignments, Step 6 Part B communication rows. Set Source = `amendment` on new rows. State what triggered the finding and which prior phase surfaced it. State what changed from the initial map.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Note them explicitly.

---

## V-05 -- Combination: All 25 + Champion Depth Scoring + Champion Durability

**Axes**: Inertia as primary organizing lens throughout preamble + champion depth scoring sub-step (authority/proximity/commitment 1-5, composite) + champion durability assessment (SPOF risk, succession, deterioration signal)
**Hypothesis**: All 25 existing criteria are satisfied. Champion scoring and durability are additive axes that do not disturb grid structure, veto ranking, amendment mandate, FAIL saturation, or any inertia elevation criterion. The inertia-primary preamble reinforces C-18 framing without removing any other structural element. Amendment correct-form example is extended to include a champion score revision (a new amendment-eligible target). Champion scoring may surface C-26 (champion quantification depth); champion durability may surface C-27 (champion continuity planning). Expected: 175/175 + new v9 candidates.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Role ownership:**
- **Strategy role**: conflict identification (Step 1a), inertia mapping (Step 1b), critical-path gatekeepers (Step 1c), veto risk ranking (Step 4), critical-path confirmation (Step 7)
- **UX role**: segment analysis and NOT-doing statements (Phase 2)
- **PM role**: org context check (Step 0), grid construction (Phase 3), champion identification and scoring (Step 5), Frame Type prefill (Step 6a), communication table (Step 6b), amendment pass (Step 8)

**On inertia stakeholders:** The most commonly underweighted stakeholders in a feature decision are those defending the current approach -- not because they are obstructionist, but because their workflow, standing, or system ownership is being displaced. This skill treats inertia analysis as a structural requirement, not an optional consideration. Every inertia stakeholder identified in Phase 1 will propagate to three downstream positions: a tagged row in the grid, a ranked veto entry, and a Frame Type assignment that acknowledges displacement. Missing any one of these positions means the inertia signal was incomplete.

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

**Step 5 -- Champion identification and depth scoring -- PM role**

**Part A -- Champion identification -- PM role**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

**Part B -- Champion depth scoring -- PM role**

For each champion, score on three dimensions (1 = weak, 5 = strong):

| Champion | Authority (1-5) | Proximity (1-5) | Commitment (1-5) | Composite |
|----------|:---------------:|:---------------:|:----------------:|:---------:|

- **Authority**: Does their endorsement carry weight with the decision-makers who control veto risks?
- **Proximity**: How frequently do they interact with stakeholders who need to be moved?
- **Commitment**: How personally invested are they in this outcome -- would they advocate without prompting?

Composite = Authority + Proximity + Commitment (max 15). Champions scoring below 9 should be treated as supporting evidence, not primary movers -- identify a secondary champion or plan to build commitment before relying on them.

**Part C -- Champion durability -- PM role**

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
