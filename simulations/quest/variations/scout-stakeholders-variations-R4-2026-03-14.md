Round 4 variations for `scout-stakeholders` written to `simulations/quest/variations/scout-stakeholders-variations-R4-2026-03-14.md`.

---

## Round 4 Design Summary

| ID | Axis | C-15 | C-16 | C-17 | Expected |
|----|------|:----:|:----:|:----:|:--------:|
| V-01 | C-17 saturation only (single-axis) | - | - | ++ | ~125 |
| V-02 | Inertia prominence as structural section | - | - | - | ~120 |
| V-03 | Prefill-before-execute for frame types | - | - | - | ~120 |
| V-04 | Minimal triple combo: C-15 + C-16 + C-17 | ++ | ++ | ++ | 135 |
| V-05 | Full 135: triple combo + prefill + displacement vocab | ++ | ++ | ++ | 135 |

**Design logic:**

**V-01** — The clean C-17 isolation test. R3 V-03 demonstrated the pattern; V-01 refines it now that C-17 is load-bearing. FAIL_ at every gate (Step 0 through Step 8), standard PM-first sequence, no before/after pair. Deliberately fails C-15 and C-16. If it scores ~125, C-17 is reliably triggered alone.

**V-02** — New axis not yet tested: inertia prominence. Elevates the inertia stakeholder to a named structural section with its own vocabulary (`current-approach`, `displaced-by`, `displacement-acknowledgment`). Inertia stakeholder tracked through grid, veto, and comms table. Seeds a potential C-18; tests whether the displacement framing strengthens C-10 and C-13 beyond what the rubric currently measures.

**V-03** — Tests the prefill-before-execute pattern flagged in R3's excellence signals. Assign all four Frame Type labels before writing any row content. Accepted values enumerated including `displacement-acknowledgment`. If the current rubric scores this no differently than a standard C-13 pass, the execution pattern is not yet a checkable criterion.

**V-04** — Minimal triple combo. Takes R3 V-04's structure (which hit 130/130 with C-15 + C-16) and adds FAIL_ labels to every gate, including the two gates R3 V-05 left uncovered (Step 0 and Step 7). If it reaches 135, the three criteria are mutually compatible.

**V-05** — Maximalist. Triple combo plus prefill-before-execute plus full displacement vocabulary with `[INERTIA]` tracking through all phases and inertia-specific NOT-doing statement required. If it underperforms V-04, criterion overloading is the diagnosis.

**Key C-17 gate coverage for V-01 and V-04/V-05:** FAIL labels confirmed at Step 0 (`FAIL_SILENT_INFERENCE`), Phase 1 (`FAIL_ONE_PARTY`, `FAIL_NO_INERTIA`, `FAIL_NO_TIMING`), Phase 2 (`FAIL_NO_NOT_DOING`, `FAIL_MONOLITH_ASSUMPTION`), Phase 3 (`FAIL_NO_SOURCE`, `FAIL_PROSE_ONLY`), Step 4 (`FAIL_WRONG_ORDER`, `FAIL_NO_MITIGATION`), Step 5 (`FAIL_GENERIC_CHAMPION`), Step 6 (`FAIL_SAME_FRAME`, `FAIL_VAGUE_TIMING`), Step 7 (`FAIL_GATEKEEPER_INCOMPLETE`), Step 8 (`FAIL_OBSERVATION_ONLY`). All 9 gates covered.
types | + | ++ | ++ | + | ++ |
| C-14 Named failure modes inline | ++ | + | + | ++ | ++ |
| C-15 Reversed sequence | - | - | - | ++ | ++ |
| C-16 Before/after pair | - | - | - | ++ | ++ |
| C-17 Anti-pattern saturation | ++ | - | - | ++ | ++ |

`++` = design change specifically targets this criterion. `-` = known gap, not addressed by this variation's axis.

---

## V-01 -- Anti-Pattern Saturation at Every Phase Gate (Single Axis)

**Axis**: C-17 -- named FAIL_ label at every execution step; standard PM-first sequence; no before/after pair
**Hypothesis**: Placing a distinct FAIL_ label inline at every gate makes the anti-pattern vocabulary exhaustive and phase-local. V-03 in R3 demonstrated this pattern and the R3 rubric confirmed it as C-17; this variation refines that prompt into a clean single-axis test now that C-17 is load-bearing. Standard PM-first sequence (deliberately failing C-15) and no before/after pair (deliberately failing C-16) isolate the axis. Expected: ~125/135.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding: "What org or team is this decision for?"

**FAIL_SILENT_INFERENCE**: Inferring an org structure without asking is the most consequential error in this skill. One question is always better than a wrong assumption.

---

**Step 1 -- Strategy Role: Conflicts and Critical Path**

Identify at least two structural conflicts before building the grid. Each conflict requires both parties named and the nature of the tension stated.

Format: **[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

Flag which carry veto risk. Name the inertia stakeholder: who benefits from keeping the current approach in place, and why is their resistance structural rather than personal?

Flag critical-path gatekeepers regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly stated.

**FAIL_NO_INERTIA**: Skipping the inertia stakeholder omits the most predictable source of late-stage resistance. If no current approach exists, state that explicitly -- do not leave it unaddressed.

---

**Step 2 -- PM Role: Power/Interest Grid**

Using findings from Step 1, construct the grid.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

Required for every row:
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

**FAIL_NO_SOURCE**: A row without a Source entry is an unauditable row. Every row requires an origin label.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a grid does not satisfy C-02. The table format is required.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants:
1. Their workflow intersection with this decision
2. Whether the group is monolithic or contains a sub-segment with substantially different friction or interest
3. One NOT-doing statement: what this product explicitly does not provide for this segment

If a sub-segment is identified, add a row to the grid with Source = `UX-segment`.

**FAIL_MONOLITH_ASSUMPTION**: Treating every quadrant entry as a single unified group without checking for sub-segments misses the most common source of communication strategy failures.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required. Generic "out of scope" language does not pass.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Alphabetical or grid-sequence order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

**FAIL_GENERIC_CHAMPION**: "Engage the champion to build support" is not a schedulable action. If you cannot put it on a calendar, it is not a champion action.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

- Frame Type must be distinct per row: `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`
- Timing must be a relative signal: "3 weeks before launch", "day of announcement", "now"
- For the inertia stakeholder's quadrant, Frame Type should acknowledge what is being displaced

**FAIL_SAME_FRAME**: Same Frame Type on two or more rows means the message has not been differentiated by quadrant.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified interval fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder flagged in Step 1:
- Why they are blocking (specific reason, not generic "important")
- Minimum lead time or hard deadline

**FAIL_NO_GATEKEEPER_TIMING**: Listing a stakeholder as critical-path without a lead time or deadline is a planning gap. The timing constraint is the point of the flag.

---

**Step 8 -- Amendment Pass**

Review Steps 1 through 7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

For each amendment:
1. Update the affected table (grid, veto, or comms) -- do not observe without updating
2. Set Source = `amendment` on new rows
3. State what triggered the finding
4. State what changed from the initial map

After the amendment pass, check whether any `initial-inventory` rows remain unverified. Each one is a signal that conflict or segment analysis may be incomplete.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An amendment that does not revise an artifact has not been executed.

---

## V-02 -- Inertia Prominence as Structural Section (Single Axis)

**Axis**: Inertia framing -- displacement vocabulary, `displacement-acknowledgment` frame type required for inertia row, inertia stakeholder tracked through every phase
**Hypothesis**: Elevating the inertia stakeholder from an incidental note to a named structural section -- with its own vocabulary (`displacement-acknowledgment`, `current-approach`, `displaced-by`) and explicit tracking through grid, veto, and comms -- raises C-10 and C-13 pass reliability and seeds a potential C-18. Standard PM-first sequence and no FAIL saturation isolate the inertia axis. Expected: ~120/135.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently.

---

**Step 1 -- Strategy Role: Conflict, Inertia, and Critical-Path Analysis**

Before building the grid, complete three sub-steps in order.

**1a. Structural conflicts**

Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension stated:

**[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

Flag which carry veto risk.

**1b. Inertia Analysis**

Name the current approach being displaced:
- **Current approach**: [what exists today]
- **Displaced-by**: [what this decision replaces it with]
- **Inertia stakeholder**: [who benefits from keeping the current approach in place]
- **Resistance type**: structural (their workflow depends on the status quo) | political (their standing depends on the current approach) | operational (they own the existing system)

The inertia stakeholder's veto probability is at least Medium unless evidence explicitly supports a lower rating. They will appear in the grid, the veto list, and the comms table.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

---

**Step 2 -- PM Role: Power/Interest Grid**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

Required for every row:
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows. The inertia stakeholder from Step 1b must appear here; tag them `[INERTIA]` in Notes. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants:
1. Workflow intersection with this decision
2. Whether the group splits into sub-segments with different friction or interest levels
3. One NOT-doing statement: what this product explicitly does not provide for this segment

For the `[INERTIA]` stakeholder specifically: the NOT-doing statement must address what the new approach does not preserve from the current approach -- not just what it lacks in absolute terms.

If a sub-segment is identified, add a row to the grid with Source = `UX-segment`.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not by grid sequence.

| Rank | Stakeholder | Probability | Impact | Mitigation |

The inertia stakeholder's veto must appear at its true probability rank. Do not underrank structural resistance.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, provide a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

Generic "engage the champion" language is not a champion action.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

Accepted Frame Type values: `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership` | `displacement-acknowledgment`

Assignment rules:
- One label per row. No two rows may share the same Frame Type.
- The inertia stakeholder's quadrant row must use `displacement-acknowledgment` or a custom frame that explicitly names what is being replaced. A generic `value-capture` or `risk-mitigation` frame for the inertia row does not acknowledge displacement.
- Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "6 weeks before".

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder from Step 1c:
- Blocking reason
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Steps 1 through 7. Run one amendment pass. Minimum one amendment required.

For each amendment, update the affected table -- do not observe without updating. Per amendment:
1. State what was added, split, or reframed
2. Update grid, veto list, or comms table
3. Set Source = `amendment` on new rows
4. State what triggered the finding
5. If the amendment affects the inertia stakeholder or introduces a new inertia-adjacent group, update the displacement vocabulary in Step 1b

After the amendment pass, note any `initial-inventory` rows that remain unverified. Note any `[INERTIA]` tags that are absent from the veto list.

---

## V-03 -- Prefill-Before-Execute for Frame Types (Single Axis)

**Axis**: Frame type execution pattern -- assign all four frame type labels before populating row content; enumerate accepted vocabulary including `displacement-acknowledgment`
**Hypothesis**: Requiring Frame Type assignment before row population forces differentiation at the assignment step rather than post-hoc correction. R3 V-05's excellence signals flagged this as a potential C-18 ("Frame Types assigned before rows are populated"). This variation isolates that axis to test whether the execution pattern produces behavior the current rubric does not yet capture. Standard sequence, moderate FAIL coverage, no before/after pair. Expected: ~120/135.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question: "What org or team is this decision for?" Do not infer silently.

---

**Step 1 -- Strategy Role: Conflict and Critical-Path Analysis**

Before building the grid:

1. Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension: **[Group A] vs. [Group B] -- [nature]**. Flag which carry veto risk.
2. Name the inertia stakeholder: who benefits from keeping the current approach in place?
3. Flag critical-path gatekeepers with minimum lead time. Label each `[CRITICAL PATH -- lead time: X]`.

---

**Step 2 -- PM Role: Power/Interest Grid**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

Required:
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants:
1. Workflow intersection with this decision
2. Whether the group contains sub-segments with distinct friction or interest levels
3. One NOT-doing statement: what this product explicitly does not provide for this segment

If a sub-segment is identified, add a row with Source = `UX-segment`.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not by grid sequence.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order.

---

**Step 5 -- Champion**

Name one or more champions. For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6 -- Communication Strategy**

**Before populating the rows, assign a Frame Type label to each quadrant:**

| Quadrant | Frame Type (assign first) |
|----------|--------------------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

Accepted values: `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership` | `displacement-acknowledgment`

Assignment rules:
- Each quadrant must receive a distinct label before any row content is written.
- No two quadrants may share the same Frame Type.
- For the quadrant containing the inertia stakeholder, assign `displacement-acknowledgment` or a frame that explicitly names what is being replaced. A value-capture or risk-mitigation frame does not acknowledge displacement.
- Complete all four Frame Type assignments before writing any row content.

Then complete the full communication table:

| Quadrant | Key Message | Frame Type | Timing | Owner |

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "now".

**FAIL_SAME_FRAME**: If two rows share a Frame Type, the prefill assignment was not honored.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified unit fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder from Step 1:
- Blocking reason
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Steps 1 through 7. Run one amendment pass. Minimum one amendment required.

For each amendment:
1. Update the affected table (grid, veto, or comms) -- do not observe without updating
2. Set Source = `amendment` on new rows
3. State what triggered the finding
4. State what changed from the initial map

If the amendment adds a new stakeholder, reassign Frame Types in the comms table if needed -- duplicate Frame Types are not permissible even after an amendment.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment.

After the amendment pass, note any `initial-inventory` rows that remain unverified.

---

## V-04 -- Minimal Triple Combo: C-15 + C-16 + C-17

**Axis**: Combination of reversed sequence (C-15) + before/after amendment pair (C-16) + anti-pattern saturation at every phase gate (C-17), applied simultaneously; no additional feature coverage beyond what each criterion requires
**Hypothesis**: The three aspirational criteria (C-15, C-16, C-17) are mutually compatible and additive. Reversed sequence forces analysis before synthesis; the before/after pair makes the amendment anti-pattern concrete; FAIL saturation covers all gates. Together they should reach 135/135. If this misses, one gate was uncovered or one criterion triggers a structural conflict with another. Expected: 135/135.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently.

**FAIL_SILENT_INFERENCE**: Proceeding on an assumed org without asking is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Strategy: Conflict and Inertia Analysis

**Run this phase first. The grid is built in Phase 3, after Phases 1 and 2 are complete.**

**1a. Structural conflicts**

Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension:

**[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required.

**1b. Inertia stakeholder**

Name who benefits from keeping the current approach in place. Their resistance is structural, not personal -- treat their veto probability as at least Medium unless evidence says otherwise.

**FAIL_NO_INERTIA**: Skipping the inertia stakeholder omits the most predictable source of late-stage resistance. If no current approach exists, state that explicitly.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is a planning gap. Timing is the point of the flag.

---

## Phase 2 -- UX: Segment Analysis

**Run this phase second. The grid is built in Phase 3.**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

If a group is not monolithic, split it now. New rows from this phase carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 3 -- PM: Grid Construction (build this last)

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
Minimum 4 rows. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. The inertia stakeholder must appear at their true probability rank.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order. Rank by likelihood.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a plan.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, provide a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

- Frame Type must be distinct per row: `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`
- For the inertia stakeholder's quadrant, Frame Type should acknowledge what is being displaced, not only what is being gained
- Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "now"

**FAIL_SAME_FRAME**: Same Frame Type on two or more rows means the message is not differentiated. Fix it.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified interval fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder confirmed in Phase 1:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

**FAIL_GATEKEEPER_INCOMPLETE**: A gatekeeper entry without a blocking reason or timing is incomplete. Both fields are required.

---

**Step 8 -- Amendment Pass**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "It is worth considering whether the Platform Security team has sign-off authority here based on data handling scope. This may be relevant to the timeline."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Platform Security added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- sign-off approval veto added at High probability, ranked above existing Medium-probability risks. Comms table updated -- Keep Satisfied row revised; Frame Type changed to `compliance-alignment`, Timing set to 8 weeks before launch. Triggered by: Phase 1 conflict between Engineering and Compliance over data handling scope. What changed from initial map: Platform Security was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, or comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. State what triggered the finding and which prior phase surfaced it
4. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified is a signal that Phase 1 or Phase 2 may be incomplete.

---

## V-05 -- Full 135 Target: Triple Combo + Prefill + Displacement Vocabulary

**Axis**: Maximalist -- C-15 + C-16 + C-17 + prefill-before-execute for Frame Types + named `displacement-acknowledgment` vocabulary + inertia stakeholder tracked through all phases
**Hypothesis**: Combining all three rubric criteria (C-15, C-16, C-17) with the two R3 V-05 excellence signals (prefill-before-execute, displacement vocabulary) produces 135/135 and seeds the next round's potential criteria. The prefill-before-execute pattern targets C-13 more reliably by creating correct output by construction. The displacement vocabulary encodes the inertia-acknowledgment requirement into the frame type vocabulary itself. If this underperforms V-04, criterion overloading is the diagnosis. Expected: 135/135.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first and most consequential check.

**FAIL_SILENT_INFERENCE**: Proceeding without asking when context is absent is the most consequential error in this skill. One question is always better than a wrong assumption.

---

## Phase 1 -- Strategy: Conflict, Inertia, and Critical-Path Analysis

**Run Phase 1 before building the grid. The grid is built in Phase 3.**

**1a. Structural conflicts**

Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension:

**[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

Flag which carry veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two named parties required, both explicitly identified.

**1b. Inertia and displacement analysis**

Name what this decision displaces:
- **Current approach**: [what exists today]
- **Displaced-by**: [what this decision introduces in its place]
- **Inertia stakeholder**: [who benefits from keeping the current approach in place]
- **Default veto probability**: at least Medium unless evidence explicitly supports a lower rating

The inertia stakeholder tracks through every subsequent phase: grid (tagged `[INERTIA]`), veto list (probability at default or higher), and comms table (Frame Type = `displacement-acknowledgment`).

**FAIL_NO_INERTIA**: Omitting the inertia stakeholder from Phase 1 means it will be omitted from the grid, the veto list, and the comms table. The omission propagates.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time or deadline is incomplete. Timing is the point of the flag.

---

## Phase 2 -- UX: Segment Analysis

**Run Phase 2 before building the grid.**

For each user segment relevant to this decision:
1. Role or use pattern
2. What they gain
3. What they lose or find harder
4. One NOT-doing statement: what this product explicitly does not provide for this segment

For the inertia stakeholder segment specifically: the NOT-doing statement must address what the new approach does not preserve from the current approach, not just what it lacks in absolute terms.

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows carry Source = `segment-analysis`.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is required per segment. Generic "out of scope" language does not pass.

**FAIL_MONOLITH_ASSUMPTION**: Treating every entry as a single unified group without checking for sub-segments misses the most common source of communication strategy mismatches.

---

## Phase 3 -- PM: Grid Construction (build this last)

**Build this grid now -- after Phase 1 and Phase 2 are complete.** Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

The inertia stakeholder from Phase 1b must appear here tagged `[INERTIA]` in Notes. All `[CRITICAL PATH]` stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is unauditable.

**FAIL_PROSE_ONLY**: A prose list of stakeholder names without a table does not satisfy the grid requirement.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. The inertia stakeholder's veto must appear at its true probability rank -- do not artificially lower structural resistance.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each, state a specific, schedulable action:
- "Give [Name] a 10-minute demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action. "Engage the champion" is not schedulable.

---

**Step 6 -- Communication Strategy**

**Before populating the rows, assign a Frame Type label to each quadrant:**

| Quadrant | Frame Type (assign first) |
|----------|--------------------------|
| Manage Closely | |
| Keep Satisfied | |
| Keep Informed | |
| Monitor | |

Accepted values: `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership` | `displacement-acknowledgment`

Assignment rules:
- Each quadrant receives a distinct label. No two quadrants may share a Frame Type.
- The quadrant containing the inertia stakeholder must be assigned `displacement-acknowledgment`. A `value-capture` or `risk-mitigation` frame for the inertia row does not acknowledge displacement -- assign the correct label before writing the message.
- Complete all four Frame Type assignments before writing any row content.

Then complete the full communication table:

| Quadrant | Key Message | Frame Type | Timing | Owner |

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "now", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the prefill assignment was not honored. The table cannot be completed until Frame Types are differentiated.

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
> "It is worth noting that the Data Governance team likely has approval authority over schema changes. This may affect the timeline and should be followed up on."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Data Governance added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- schema approval veto added at High probability, ranked above existing Medium-probability risks. Comms table updated -- Keep Satisfied row revised; Frame Type changed from `compliance-alignment` to `co-ownership`, Timing set to 8 weeks before launch. Triggered by: Phase 1 conflict between Engineering and Platform over data ownership scope. What changed from initial map: Data Governance was absent from initial-inventory; conflict analysis surfaced the dependency.

If the amendment introduces a new inertia-adjacent stakeholder, update Phase 1b's displacement vocabulary and reassign Frame Types in Step 6 if needed.

For every amendment:
1. Update the affected table (grid, veto, or comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. State what triggered the finding and which prior phase surfaced it
4. State what changed from the initial map

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment. An observation without a revision has not been executed.

After all amendments, audit any remaining `initial-inventory` rows. Each one not reclassified is a signal that Phase 1 or Phase 2 may be incomplete. Note them explicitly.
