Round 3 variations written to `simulations/quest/variations/scout-stakeholders-variations-R3-2026-03-14.md`.

**5 variations generated targeting v3's two new criteria:**

| ID | Axis | C-15 | C-16 | Expected |
|----|------|------|------|----------|
| V-01 | Reversed sequence via structural phase headers | ++ | - | ~125 |
| V-02 | Before/after amendment pair, standard sequence | - | ++ | ~125 |
| V-03 | Anti-pattern at every phase gate | - | - | ~120 |
| V-04 | Minimal combo: C-15 + C-16 | ++ | ++ | 130 |
| V-05 | Full 130 target: all criteria explicit | ++ | ++ | 130 |

**Design logic:**
- V-01 and V-02 isolate each new criterion independently — if either fails, the failure is unambiguous
- V-03 tests C-14 saturation in isolation; if it picks up C-16 incidentally (failure-mode density at the amendment gate), that narrows the v4 rule
- V-04 is the minimal combo — if it doesn't reach 130, one of the two criteria isn't triggered by this combination, which gives v4 a precise design question
- V-05 is maximalist — if it underperforms V-04, criterion overloading is the culprit
 tests reliable C-14 pass and its proximity to C-16 | C-14 |
| **V-04** | Minimal combo -- C-15 + C-16 simultaneously | Reversed phase structure + explicit before/after amendment pair; no other new changes from R2 full-coverage baseline | C-15, C-16 -- expected 130/130 |
| **V-05** | Full 130 target -- all criteria explicitly addressed | Reversed sequence + before/after pair + source-native-to-sequence + all frame types prefilled + failure modes at every gate + NOT doing per segment | C-15, C-16 + full reinforcement -- expected 130/130 |

**Key design decisions:**
- V-01 and V-02 are single-axis: if either fails C-15 or C-16 respectively, the failure isolates to that one design decision
- V-03 tests C-14 saturation independent of C-15/C-16; if V-03 scores C-14 more reliably than R2 variations, it confirms the threshold rule merits promotion to a separate criterion in v4
- V-04 is the minimal combo: if it does not reach 130, one of C-15 or C-16 is not reliably triggered by this specific combination — that narrows the v4 design question
- V-05 is maximalist; if it underperforms V-04, it signals that criterion overloading introduces tradeoffs

**Rubric coverage prediction per R3 variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 CODEOWNERS fallback | + | + | + | + | + |
| C-02 Power/Interest grid | + | + | + | + | + |
| C-03 Veto risks ranked | + | + | + | + | + |
| C-04 Champion concrete action | + | + | + | + | + |
| C-05 Comms strategy per quadrant | + | + | + | + | + |
| C-06 Conflicts | + | + | ++ | + | + |
| C-07 Role framing | ++ | + | + | ++ | ++ |
| C-08 Critical-path gatekeepers | + | + | + | + | + |
| C-09 Amendment phase | + | ++ | + | ++ | ++ |
| C-10 NOT doing framing | + | + | + | + | ++ |
| C-11 Source-tracking column | ++ | ++ | ++ | ++ | ++ |
| C-12 Amendment update mandate | + | ++ | + | ++ | ++ |
| C-13 Prefilled frame types | ++ | ++ | ++ | ++ | ++ |
| C-14 Named failure modes inline | + | + | ++ | + | ++ |
| C-15 Reversed sequence | ++ | - | - | ++ | ++ |
| C-16 Before/after pair | - | ++ | - | ++ | ++ |

`++` = design change specifically targets this criterion. `-` = known gap, not addressed by this variation's axis.

---

## V-01 -- Reversed Sequence via Structural Phase Headers

**Axis**: Role sequence -- Strategy → UX → PM enforced by section structure, not by instruction
**Hypothesis**: Labeling the phases as Phase 1 / Phase 2 / Phase 3 with explicit "build this last" language on the PM grid step makes the reversed sequence structurally unskippable. A model that skips Phase order must actively override a structural label; a model that reorders based on a prose instruction can rationalize doing so. C-15 should pass reliably. C-16 remains absent to isolate the axis.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as your initial inventory. If absent, extract org context from the invocation string. If neither source provides sufficient context, ask exactly one question before proceeding: "What org or team is this decision for?" Do not infer silently.

---

## Phase 1 -- Strategy: Conflict Analysis

Run Phase 1 before building the grid. The grid is built in Phase 3 after this analysis is complete.

Identify at least two structural conflicts in the stakeholder landscape. A conflict requires both parties named and the nature of their tension stated.

Format each entry: **[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

For each conflict, note whether it carries veto risk.

Also identify the inertia stakeholder: the person or group whose incentives align with keeping the current approach in place. Their resistance is structural, not personal. Note them here -- they will appear in the grid in Phase 3.

Finally, flag any stakeholders whose scheduling or approval constrains the launch timeline regardless of support stance. Label each `[CRITICAL PATH]` with the minimum lead time required.

---

## Phase 2 -- UX: Segment Analysis

Run Phase 2 before building the grid.

For each user segment or stakeholder group that will interact with this feature:

1. State their role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One explicit NOT-doing statement: what this product does not provide for this segment

If a segment is not monolithic -- if a sub-group has substantially higher interest or distinct friction -- split them now. Use "segment-analysis" as the source label for any row that originates here.

---

## Phase 3 -- PM: Grid Construction (build this last)

Build the power/interest grid using findings from Phases 1 and 2.

**Do not build this grid before Phase 1 and Phase 2 are complete.** Source labels for each row should already be identifiable from the prior phases.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: extracted from the CODEOWNERS file
- `conflict-discovered`: surfaced by conflict analysis in Phase 1
- `segment-analysis`: identified as a distinct segment in Phase 2
- `initial-inventory`: came from the initial landscape scan; treat as unverified

Any row still labeled `initial-inventory` after the amendment pass is a candidate for review -- it may indicate a gap that Phase 1 or Phase 2 should have surfaced.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
Minimum 4 rows. Critical-path stakeholders from Phase 1 carry `[CRITICAL PATH -- lead time: X]` in Notes.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Do not sort alphabetically or by grid order.

For each entry: Probability (High/Medium/Low) | Impact description | Mitigation action

---

**Step 5 -- Champion Identification**

Name one or more champions from the grid (high power, high interest, favorable stance). For each champion, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

Generic "engage the champion" language is not a champion action.

---

**Step 6 -- Communication Strategy**

Produce one row per quadrant:

| Quadrant | Key Message | Frame Type | Timing | Owner |

- Frame Type must be distinct per row. Examples: `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`
- Timing must be a relative signal: "3 weeks before launch", "day of announcement", "now"
- For the inertia stakeholder's quadrant, Frame Type should acknowledge what is being displaced, not only what is being gained

---

**Step 7 -- Critical-Path Gatekeepers**

For any stakeholder flagged `[CRITICAL PATH]` in Phase 1, confirm here:
- Why they are blocking
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Phases 1 through 7. Ask: what did the initial map miss, collapse, or misplace?

For each amendment, update the grid, veto list, or comms table -- do not observe without updating.

For each amendment entry:
- State what was added, split, or reframed
- Set Source to `amendment`
- Note which prior phase triggered the finding
- Confirm which tables were updated

After the amendment pass, note whether any `initial-inventory` rows have been reclassified or remain unverified.

---

## V-02 -- Before/After Amendment Pair

**Axis**: Amendment section -- bad-form example immediately adjacent to correct-form example
**Hypothesis**: Placing the bad form (observation without revision) directly before the correct form at the exact point of execution is more enforceable than a positive rule alone. The bad form is the actual failure mode; its presence makes the distinction concrete rather than abstract. C-16 should reliably pass. Sequence is standard (PM grid before UX) to isolate the axis.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as your initial inventory. If absent, extract org context from the invocation string. If neither source provides sufficient context, ask exactly one question: "What org or team is this decision for?" Do not proceed by inferring silently.

---

**Step 1 -- Strategy Role: Conflict and Critical-Path Discovery**

Before building the grid, identify:

1. At least two structural conflicts. Each conflict requires both parties named and the nature of the tension stated: **[Group A] vs. [Group B] -- [resource / priority / scope / process / compliance]**. Flag which carry veto risk.
2. The inertia stakeholder: who benefits from the current approach and has structural incentive to resist or delay this decision.
3. Gatekeepers who are on the critical path regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

---

**Step 2 -- PM Role: Power/Interest Grid**

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

Required for every row:
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows. Critical-path stakeholders from Step 1 carry `[CRITICAL PATH -- lead time: X]` in Notes.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants, identify:
- Their workflow intersection with this decision
- Whether the group is monolithic or contains a sub-segment with substantially different interest or friction
- One NOT-doing statement: what this product does not provide for this segment

If a sub-segment emerges, add a new row to the grid with Source = `UX-segment`.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not by grid sequence.

| Rank | Stakeholder | Probability | Impact | Mitigation |

---

**Step 5 -- Champion**

Name one or more champions (high power, high interest, favorable). For each, state a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] introduces, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

Generic "engage the champion" language is not a champion action.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

- Frame Type must be distinct per row: `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`
- Timing must be a relative signal: "3 weeks before launch", "day of", "now"

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder:
- Blocking reason
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Steps 1-7. Run one amendment pass. Minimum one amendment required.

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "Note: it is worth considering whether the data platform team has approval rights over schema changes. This is worth following up on."

**Correct form** (required):
> **Amendment 1**: Grid updated -- added Data Platform (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- schema approval veto promoted to rank 1 at High probability. Comms table updated -- new row added with Frame Type = co-ownership, Timing = 6 weeks before launch. Triggered by: conflict between Backend and Product over schema ownership in Step 1. What changed from initial map: Data Platform was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, or comms) -- do not observe without updating
2. Set Source = `amendment` on new rows
3. State what triggered the finding and which prior step surfaced it
4. State what changed from the initial map

---

## V-03 -- Anti-Pattern Saturation at Every Phase Gate

**Axis**: Named failure modes -- FAIL label at every step where a failure can occur
**Hypothesis**: Placing a named FAIL label inline at every step (not just the steps where R2 variations placed them) raises C-14 from a conditional pass to a reliable pass. It also tests whether failure-mode density at each gate creates the conditions for C-16 to pass naturally even without an explicit before/after pair.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question: "What org or team is this decision for?"

**FAIL_SILENT_INFERENCE**: Inferring an org structure without asking is the most consequential error in this skill. One question is always better than a wrong assumption.

---

**Step 1 -- Strategy Role: Conflicts and Critical Path**

Identify at least two structural conflicts before building the grid. Each conflict requires both parties named.

Format: **[Group A] vs. [Group B] -- [nature]**

Flag which carry veto risk. Identify the inertia stakeholder: who benefits from the current approach staying in place.

Flag gatekeepers whose scheduling or approval constrains the timeline regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_ONE_PARTY**: A single stakeholder's concern listed alone is not a conflict. Two parties required, both named.

**FAIL_NO_INERTIA**: Skipping the inertia stakeholder misses the most predictable source of late-stage veto. If no current approach exists, state that explicitly.

---

**Step 2 -- PM Role: Power/Interest Grid**

Using findings from Step 1, place each stakeholder on the grid.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

Required for every row:
- **Source**: `CODEOWNERS` | `conflict-discovered` | `UX-segment` | `initial-inventory`
- **Quadrant**: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
- Minimum 4 rows

**FAIL_NO_SOURCE**: A row without a Source entry is an unauditable row. Every row requires an origin label.

**FAIL_PROSE_ONLY**: A list of stakeholder names in prose with no grid = FAIL on C-02. The table is required.

---

**Step 3 -- UX Role: Segment Analysis**

For each stakeholder in the Manage Closely and Keep Satisfied quadrants:
- Workflow intersection with this decision
- Whether the group splits into sub-segments with different friction or interest levels
- One NOT-doing statement per segment: what this product explicitly does not provide for them

If a sub-segment is identified, add a row to the grid with Source = `UX-segment`.

**FAIL_MONOLITH_ASSUMPTION**: Treating every quadrant entry as a monolithic group without checking for sub-segments misses the most common source of communication strategy mismatches.

**FAIL_NO_NOT_DOING**: The NOT-doing statement is not optional. Every segment needs one. Generic "out of scope" language does not pass.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Alphabetical or grid-sequence order is not probability order. Rank by likelihood of occurrence.

**FAIL_NO_MITIGATION**: A veto risk without a mitigation action is an observation, not a risk plan.

---

**Step 5 -- Champion**

Name one or more champions. For each, provide a specific, schedulable action.

Examples:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens"
- "Grant [Name]'s team early access at T-3 weeks"

**FAIL_GENERIC_CHAMPION**: "Engage the champion to build support" is not a schedulable action. If you cannot put it on a calendar, it is not a champion action.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

- Frame Type must be distinct per row: `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`
- Timing must be a relative signal: "3 weeks before launch", "day of", "now"

**FAIL_SAME_FRAME**: Same Frame Type on two or more rows means the message has not been differentiated by quadrant. Fix it.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a quantified interval fails the timing requirement. Use relative signals with a unit.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder from Step 1:
- Why they are blocking
- Minimum lead time or hard deadline

**FAIL_NO_TIMING**: "Important stakeholder" with no deadline or lead time is not a gatekeeper flag. Timing is required.

---

**Step 8 -- Amendment Pass**

Review Steps 1-7. Run one amendment pass. Ask: what did the initial map miss, collapse, or misplace?

For each amendment, you must update the affected artifact -- not observe without revising.

For each amendment entry:
1. State what was added, split, or reframed
2. Update the grid, veto list, or comms table
3. Set Source = `amendment` on new rows
4. State what triggered the finding

**FAIL_OBSERVATION_ONLY**: Writing "it may be worth noting that X is also relevant" without updating a table is not an amendment. An amendment that does not change an artifact is not an amendment.

After the amendment pass, check for any `initial-inventory` rows that remain unverified. Each one is a signal that conflict or segment analysis may be incomplete.

---

## V-04 -- Minimal Combo: C-15 + C-16

**Axis**: Combination of C-15 (reversed sequence via structural phase headers) and C-16 (before/after amendment pair) applied simultaneously; no other new changes from the R2 full-coverage baseline
**Hypothesis**: The minimal combination of the two new v3 criteria, applied to a variation that already covered all v2 aspirationals, should reach 130/130. If it does not, one of the two criteria is not yet triggered by this combination in isolation.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory. If absent, extract org context from the invocation string. If neither provides sufficient context, ask exactly one question: "What org or team is this decision for?" Do not infer silently.

---

## Phase 1 -- Strategy: Conflict Analysis

Run this phase before building the grid. The grid is built in Phase 3.

Identify at least two structural conflicts. Each entry requires both parties named and the nature of the tension stated:

**[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

Flag which carry veto risk.

Name the inertia stakeholder: who benefits from keeping the current approach in place, and what is their likely response to this decision?

Flag critical-path gatekeepers with minimum lead time. Label each `[CRITICAL PATH -- lead time: X]`.

---

## Phase 2 -- UX: Segment Analysis

Run this phase before building the grid.

For each user segment:
1. Role or use pattern
2. What they gain
3. What they lose or find harder
4. One NOT-doing statement -- what this product explicitly does not provide for them

If a group is not monolithic, split it now. Use Source = `segment-analysis` for any row originating here.

---

## Phase 3 -- PM: Grid Construction (build this last)

Using findings from Phases 1 and 2, construct the grid. Source labels should already be identifiable from the prior phases.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial landscape scan; treat as unverified until cross-referenced

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
Minimum 4 rows. Critical-path stakeholders carry `[CRITICAL PATH -- lead time: X]` in Notes.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. Not alphabetically, not by grid order.

| Rank | Stakeholder | Probability | Impact | Mitigation |

---

**Step 5 -- Champion**

Name one or more champions. For each, provide a specific, schedulable action:
- "Give [Name] a demo slot at the sprint review on [date]"
- "Co-present at steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks"

Generic "engage the champion" language does not pass.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

- Frame Type must be distinct per row: `risk-mitigation`, `value-capture`, `compliance-alignment`, `awareness-only`, `co-ownership`
- Timing must be a relative signal: "3 weeks before launch", "day of", "now"
- For the inertia stakeholder's quadrant, Frame Type should acknowledge what is being displaced, not only what is gained

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder:
- Blocking reason
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required.

**Amendment execution rule -- the two forms side by side:**

**Bad form** (do not do this):
> "It occurs to me that Legal may also have approval rights here based on data retention policy. This is worth following up on."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Legal added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- Legal data retention veto added at Medium probability. Comms table updated -- Keep Satisfied row revised; Frame Type changed from `compliance-alignment` to `risk-mitigation` to reflect Legal's posture. Triggered by: conflict in Phase 1 between Security and Product over data retention scope. What changed from initial map: Legal was absent from initial-inventory; Phase 1 conflict surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, or comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. State what triggered the finding and which prior phase surfaced it
4. State what changed from the initial map

After all amendments, note any `initial-inventory` rows that remain unverified.

---

## V-05 -- Full 130 Target

**Axis**: All criteria explicitly addressed -- reversed sequence structural enforcement + before/after pair + source native to sequence + frame types prefilled + failure modes at every gate + NOT-doing per segment
**Hypothesis**: Maximalist variation with every criterion explicitly designed in. If this underperforms V-04, it signals that criterion overloading introduces execution tradeoffs; if it matches or exceeds V-04, it confirms that explicit criterion coverage is additive rather than dilutive.

---

You are running `/scout-stakeholders` for the topic: {{topic}}.

**Step 0 -- Org Context**

Check for a CODEOWNERS file. If present, extract team names and owners as initial inventory with Source = `CODEOWNERS`. If absent, extract org context from the invocation string. If context is insufficient, ask exactly one question before proceeding:

> "What org or team is this decision for?"

Do not infer. Do not proceed on an assumed org. This is the first and most consequential check.

---

## Phase 1 -- Strategy: Conflict and Inertia Analysis

**Run Phase 1 before building the grid. The grid is built in Phase 3.**

**1a. Structural conflicts**

Identify at least two conflicts. Each entry requires both parties named and the nature of the tension:

**[Group A] vs. [Group B] -- [nature: resource / priority / scope / process / compliance]**

For each conflict: flag whether it carries veto risk.

**FAIL_ONE_PARTY**: A single stakeholder's concern is not a conflict. Two named parties required.

**1b. Inertia stakeholder**

Name the status-quo: what existing approach does this decision displace? Who benefits from keeping it in place? Their resistance is structural, not personal -- treat their veto probability as at least Medium unless evidence says otherwise.

**1c. Critical-path gatekeepers**

Flag any stakeholders whose scheduling or approval constrains the timeline regardless of support stance. Label each `[CRITICAL PATH -- lead time: X]`.

**FAIL_NO_TIMING**: A critical-path flag without a lead time is not a gatekeeper flag.

---

## Phase 2 -- UX: Segment Analysis

**Run Phase 2 before building the grid.**

For each user segment:

1. Role or use pattern
2. What they gain from this decision
3. What they lose or find harder
4. One NOT-doing statement -- what this product explicitly does not provide for this segment

**FAIL_NO_NOT_DOING**: The NOT-doing statement is not optional. Generic "out of scope" language does not pass.

If a group is not monolithic -- if a sub-segment has substantially higher interest or distinct friction -- split it now. New rows from this phase carry Source = `segment-analysis`.

---

## Phase 3 -- PM: Grid Construction (build this last)

**Build this grid now -- after Phase 1 and Phase 2 are complete.**

Source labels for most rows should already be identifiable from the prior phases. A row with Source = `initial-inventory` after the amendment pass is a visible gap.

| Stakeholder | Power (H/M/L) | Interest (H/M/L) | Quadrant | Source | Notes |
|-------------|---------------|------------------|----------|--------|-------|

**Source label definitions:**
- `CODEOWNERS`: from the CODEOWNERS file
- `conflict-discovered`: surfaced in Phase 1
- `segment-analysis`: surfaced in Phase 2
- `initial-inventory`: from initial scan; unverified until cross-referenced
- `amendment`: added during the amendment pass

Include the inertia stakeholder from Phase 1b. Include all `[CRITICAL PATH]` stakeholders with lead time in Notes.

Quadrant labels: `Manage Closely` | `Keep Satisfied` | `Keep Informed` | `Monitor`
Minimum 4 rows.

**FAIL_NO_SOURCE**: Every row requires a Source entry. A source-free row is an unauditable row.

---

**Step 4 -- Veto Risk Ranking**

List veto risks ordered by probability -- highest first. The inertia stakeholder's veto should appear at its true probability rank, not artificially lowered.

| Rank | Stakeholder | Probability | Impact | Mitigation |

**FAIL_WRONG_ORDER**: Grid-sequence or alphabetical order is not probability order.

---

**Step 5 -- Champion**

Name one or more champions from the grid. For each champion, state a specific, schedulable action:
- "Give [Name] a 10-minute demo slot at the sprint review on [date]"
- "Co-present at program steering; [Name] opens, you detail the tradeoffs"
- "Grant [Name]'s team early access at T-3 weeks before GA"

**FAIL_GENERIC_CHAMPION**: If the action cannot be placed on a calendar, it is not a champion action.

---

**Step 6 -- Communication Strategy**

| Quadrant | Key Message | Frame Type | Timing | Owner |

Prefill all four Frame Type values before completing the rows. Assign one label per quadrant -- no two rows may share a Frame Type.

Accepted values: `risk-mitigation` | `value-capture` | `compliance-alignment` | `awareness-only` | `co-ownership` | `displacement-acknowledgment`

For the inertia stakeholder's quadrant, use `displacement-acknowledgment` or a frame that explicitly names what is being replaced, not only what is being gained.

Timing must be a relative signal with a quantified interval: "3 weeks before launch", "day of announcement", "now", "6 weeks before".

**FAIL_SAME_FRAME**: Same Frame Type on two rows means the message is not differentiated. Fix it.

**FAIL_VAGUE_TIMING**: "Soon" or "before launch" without a unit fails the timing requirement.

---

**Step 7 -- Critical-Path Gatekeepers**

For each `[CRITICAL PATH]` stakeholder confirmed in Phase 1:
- Blocking reason (specific, not generic)
- Minimum lead time or hard deadline

---

**Step 8 -- Amendment Pass**

Review Phases 1-3 and Steps 4-7. Run one amendment pass. Minimum one amendment required. Ask: what did the initial map miss, collapse, or misplace?

**Amendment execution rule -- read both forms before proceeding:**

**Bad form** (do not do this):
> "It occurs to me that the data platform team may have schema approval rights. This is worth following up on."

**Correct form** (required):
> **Amendment 1**: Grid updated -- Data Platform added (Keep Satisfied, H power / M interest, Source: amendment). Veto list updated -- schema approval veto promoted to rank 1 at High probability. Comms table updated -- Keep Satisfied row revised; Frame Type changed to `co-ownership`, Timing set to 6 weeks before launch. Triggered by: Phase 1 conflict between Backend and Product over schema ownership. What changed from initial map: Data Platform was absent from initial-inventory; conflict analysis surfaced the dependency.

For every amendment:
1. Update the affected table (grid, veto, or comms) -- no observation without revision
2. Set Source = `amendment` on new rows
3. State what triggered the finding and which prior phase surfaced it
4. State what changed from the initial map

After all amendments, audit any remaining `initial-inventory` rows. Each one that was not reclassified is a signal that Phase 1 or Phase 2 may be incomplete. Note them explicitly.

**FAIL_OBSERVATION_ONLY**: Writing a finding without updating a table is not an amendment.
