I have full context. Now writing all 5 variations.

---

# scout-stakeholders — Round 12 Variations (v12 rubric, max 210)

## Variation Axes

**Three single-axis targets:**
1. **V-01** — Trajectory column placement: Trajectory as a native grid column during Phase 3 construction, not a separate step. Tests whether C-31 is satisfied by inline grid integration vs. a standalone section.
2. **V-02** — Synthesis aggregation level: C-32 synthesis step produces per-quadrant rows (4 rows) instead of per-stakeholder rows. The rubric permits "per stakeholder or per quadrant" — tests whether the compact quadrant form is structurally sufficient.
3. **V-03** — Phrasing register: Strict machine-parseable constraint-rule format (RULE / GATE / FAIL only — no coaching voice, no prose explanation). Tests whether the structural requirements survive full narrative removal.

**Combinations:**
4. **V-04** — Trajectory column (V-01 axis) + Synthesis with explicit source attribution per field (each synthesis column is labeled with its source step in the header).
5. **V-05** — All 32 criteria at maximum density. Inherits V-04's trajectory column + attributed synthesis. Full FAIL label saturation. Complete 9-target amendment mandate. Dense format with no padding.

---

## V-01 — Single Axis: Trajectory as Native Grid Column

**Hypothesis**: C-31 is satisfied by a Trajectory column integrated directly into the Power/Interest grid at Phase 3 construction time, with FAIL_NO_TRAJECTORY enforced at the grid step. This is structurally distinct from R11 V-05's approach of placing trajectory in Step 7 Section B. The amendment mandate gains "trajectory assessments" as an eligible target regardless of where the column lives.

---

### Step 0: CODEOWNERS context check — PM role

Check for a CODEOWNERS file in the repository. If present, extract the org and team structure from it. If absent, check the invocation string for org or team context. If invocation context is also insufficient, ask exactly one question: "What org or team is this decision for?" Do not infer. Do not proceed on an assumed org structure.

FAIL_SILENT_INFERENCE: If you construct any stakeholder analysis without confirming org context from one of these three sources, the analysis is invalid from Step 0.

---

### Phase 1: Strategic conflict and structural landscape — Strategy role

**Step 1a: Structural conflicts and resolution pathways — Strategy role**

Identify at least two structural conflicts. Each conflict entry requires:
- Both stakeholder groups named
- Nature of the tension stated (budget, authority, timeline, scope, data ownership)

FAIL_ONE_PARTY: A conflict entry naming only one party is not a conflict.

For each named conflict, extend the entry with a resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|
| [parties + nature] | [who has decision-making power] | [specific ruling needed] | [date or milestone] |

FAIL_NO_RESOLUTION_PATHWAY: Any named conflict without a resolution authority, specific decision point, and deadline is structurally incomplete. The Phase 1→2 gate will not pass until all conflicts have complete pathways.

**Step 1b: Inertia stakeholder identification — Strategy role**

Identify stakeholders whose primary risk is status-quo defense. These are not active opponents — they are satisfied with the current state and will not advocate for change without displacement acknowledgment.

Tag each inertia stakeholder for grid entry with `[INERTIA]`. The comms table must assign `displacement-acknowledgment` as the Frame Type for all inertia-classified rows. This classification is made here, not at comms population time.

FAIL_NO_INERTIA: If the product displaces any existing tool, workflow, or budget line and no inertia stakeholders are identified, the strategy analysis is incomplete.

**Step 1c: Critical-path gatekeeper tagging — Strategy role**

For each gatekeeper who controls a blocking dependency, apply:

`[CRITICAL PATH — lead time: N weeks — blocks: {specific dependency}]`

The lead-time note must be a specific number of weeks. The blocking reason must be specific, not generic. "Important stakeholder" is not a valid critical-path rationale. These lead times feed the engagement window derivation in Step 5a.

FAIL_NO_GATEKEEPER_TIMING: A critical-path tag without a lead time and specific blocking reason does not satisfy this step.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Confirm all Phase 1 outputs before proceeding:
- [ ] At least two conflicts identified with both parties named and nature stated
- [ ] Resolution pathway table complete per conflict (Authority / Decision / Deadline)
- [ ] Inertia stakeholders identified and tagged `[INERTIA]`
- [ ] At least one critical-path gatekeeper with lead time and blocking reason
- [ ] Resolution pathway present for every named conflict

FAIL_INCOMPLETE_PHASE1: If any item above is absent or incomplete, do not begin Phase 2.

---

### Phase 2: User and buyer segment analysis — UX role

**Step 2: Segment analysis and NOT-doing framing — UX role**

For each distinct user or buyer segment:
1. Name the segment and its decision-making role (buyer / user / influencer / champion-candidate)
2. State the primary job-to-be-done this product addresses for the segment
3. Name the journey stage where the product intersects their workflow
4. Write one NOT-doing statement: what this product explicitly does not provide for this segment

The NOT-doing statement must name a specific capability or outcome the product intentionally withholds for this segment. "Out of scope" is not a NOT-doing statement.

FAIL_MONOLITH_ASSUMPTION: If all segments are collapsed into a single "user" description without distinguishing decision-making roles, Phase 2 is incomplete.
FAIL_NO_NOT_DOING: If any segment lacks a specific NOT-doing statement, the Phase 2 analysis does not pass the gate.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Confirm all Phase 2 outputs before proceeding:
- [ ] All distinct user/buyer segments identified with decision-making roles
- [ ] NOT-doing statement per segment (specific capability named, not generic "out of scope")

FAIL_INCOMPLETE_PHASE2: If any item above is absent or incomplete, do not begin Phase 3.

---

### Phase 3: Power/Interest grid construction — PM role

Build this grid now — after Phase 1 and Phase 2 are complete. Do not construct the grid before both prior phases are finished.

Produce a grid with the following columns:

| Stakeholder | Quadrant | Power | Interest | Source | Trajectory | Notes |
|-------------|----------|-------|----------|--------|------------|-------|

**Quadrant labels:**
- Manage Closely (high power, high interest)
- Keep Satisfied (high power, low interest)
- Keep Informed (low power, high interest)
- Monitor (low power, low interest)

**Source column — accepted values:**
- `CODEOWNERS` — derived from CODEOWNERS file
- `initial-inventory` — identified before any conflict or segment analysis
- `conflict-discovery` — surfaced during Step 1a conflict mapping
- `ux-discovery` — surfaced during Phase 2 segment analysis
- `amendment` — added during Step 8 amendment pass

**Trajectory column — required for every row:**

For each stakeholder, assess directional movement over the project lifecycle. Each Trajectory entry must contain:
1. Direction: **ascending toward advocate** / **stable** / **descending toward risk**
2. Observable signal rationale: at least one concrete observable indicator (e.g., "increasing participation in steering syncs," "delegating responses to reports," "budget exposure in current quarter")

FAIL_NO_TRAJECTORY: If any stakeholder row has no Trajectory entry, the grid is structurally incomplete. The Trajectory column is not optional.
FAIL_PROSE_ONLY: If stakeholders are described in prose without a structured grid, this step has not been executed.
FAIL_NO_SOURCE: If any grid row has no Source entry, provenance is untracked and the grid is incomplete.

Minimum 4 rows required. Apply `[INERTIA]` in the Notes column for all inertia-classified stakeholders from Step 1b.

---

### Step 4: Veto risk ranking — PM role

List all veto-capable stakeholders ordered by probability of veto exercise — highest first. Do not sort alphabetically or by grid sequence. Probability rank must be explicit.

| Stakeholder | Probability | Impact | Mitigation |
|-------------|-------------|--------|------------|

- **Probability**: likelihood this stakeholder exercises a veto (high / medium / low)
- **Impact**: consequence if veto is exercised (scope, timeline, budget, go/no-go decision)
- **Mitigation**: specific response strategy if the veto risk materializes — required per entry

FAIL_WRONG_ORDER: A veto list sorted alphabetically or by grid sequence, without explicit probability ranking, is invalid.
FAIL_NO_MITIGATION: A veto entry with probability and impact but no mitigation column is incomplete.

---

### Step 5a: Engagement window derivation — PM role

Synthesize the critical-path lead times from Step 1c and the quadrant positions from Phase 3 into a per-quadrant engagement window table:

| Quadrant | Earliest Engage | Latest Engage | Constraint Rationale |
|----------|----------------|---------------|---------------------|

Manage Closely stakeholders require the earliest windows. Monitor quadrant allows the latest. Derive from the maximum lead time across all critical-path gatekeepers in each quadrant.

Add an **Engagement Window** column to the Phase 3 grid. Every stakeholder row must contain an engagement window entry derived from this table.

FAIL_NO_ENGAGEMENT_WINDOW: If the Phase 3 grid contains no Engagement Window column, the grid is structurally incomplete.
FAIL_NO_WINDOW_SUMMARY: If any quadrant has no derived window, engagement timing for that quadrant is unconstrained.

The comms step (Step 6b) must anchor timing within the derived window per quadrant. Timing anchors that fall outside the Step 5a window are invalid.

---

### Step 5b: Champion identification and action — PM role

Identify one or more stakeholders as champions — those with both the authority to advocate and demonstrated motivation to act.

For each champion, assign a schedulable action. The action must be specific enough to put on a calendar today:
- "Give 30-minute demo at next weekly team sync" — valid
- "Co-present at Q2 roadmap review" — valid
- "Engage the champion" — NOT a champion action

FAIL_GENERIC_CHAMPION: If the champion action cannot be scheduled as a calendar event with a specific venue or meeting, it does not satisfy this requirement.

---

### Step 5c: Champion depth scoring — PM role

Score the champion across three dimensions:

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|----------|
| Authority | | Organizational decision-making power over the feature's path |
| Proximity | | Access to blockers, sponsors, and influencers |
| Commitment | | Demonstrated investment in the feature's success |

**Composite threshold**: Authority + Proximity + Commitment >= 9 required to proceed.

FAIL_BELOW_CHAMPION_THRESHOLD: If composite score is below 9, either identify a different champion or escalate the gap before proceeding.

---

### Step 5d: Champion durability — PM role

Assess the temporal durability of the champion relationship:

1. **Succession path**: If the champion leaves the project or organization, who assumes the champion role? Name the successor or document this as an unmitigated single point of failure.
2. **Deterioration signals**: Identify 2+ observable triggers indicating champion commitment is eroding (e.g., "missed two consecutive syncs," "decisions delegated to a report without explanation," "response latency increased from same-day to 48+ hours").

FAIL_NO_DURABILITY: If succession path is absent or fewer than two deterioration signals are identified, the durability assessment is incomplete.

---

### Step 6a: Frame Type prefill table — PM role

Before populating the comms table, complete the prefill table. Values not in this table are prohibited in the comms rows.

| Quadrant | Assigned Frame Type |
|----------|---------------------|
| Manage Closely | decision-briefing |
| Keep Satisfied | executive-summary |
| Keep Informed | progress-pulse |
| Monitor | changelog |

**Rule 1**: Each quadrant row in the comms table must use the Frame Type assigned here. Do not change Frame Type during comms row population — amend the prefill table first.

**Rule 2**: All inertia-classified rows must receive `displacement-acknowledgment` as their Frame Type here, at this prefill step, before any comms row is populated. Do not defer this assignment to Step 6b content time.

FAIL_MISSING_DISPLACEMENT_PREFILL: If the `displacement-acknowledgment` assignment for inertia rows is deferred past this prefill step, the inertia chain is broken.

---

### Step 6b: Communication strategy per quadrant — PM role

Produce one comms row per quadrant. Each row must include:

| Quadrant | Message | Frame Type | Timing | Channel |
|----------|---------|------------|--------|---------|

- **Frame Type**: must match the Step 6a prefill assignment for that quadrant
- **Timing**: must fall within the Step 5a engagement window for that quadrant. FAIL_WINDOW_MISMATCH: If timing falls outside the derived window.
- **Channel**: specify the medium (Slack DM, 1:1 meeting, all-hands, email, written memo)

FAIL_SAME_FRAME: If two or more rows share the same Frame Type, the prefill constraint has been violated.
FAIL_VAGUE_TIMING: "When appropriate" or equivalent is not a valid timing anchor. Relative anchors required ("3 weeks before launch," "day of announcement," "Week 2 of the sprint").

---

### Step 7: Cross-phase synthesis readout — PM role

After completing all analysis phases and the comms step, produce a synthesis readout. This step aggregates outputs from prior phases into a single compact row per stakeholder.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Frame Type |
|-------------|---------------|-------------------|-------------------|-----------------|------------|

- **Grid Position**: quadrant label from Phase 3 (e.g., Manage Closely)
- **Engagement Window**: derived range from Step 5a (e.g., "Week 1–3")
- **Conflict Exposure**: name any Step 1a conflict that directly involves this stakeholder, or "None"
- **Champion Status**: "Champion" if designated in Step 5b, otherwise "—"
- **Frame Type**: the Frame Type from the Step 6a prefill assignment

Every stakeholder in the Phase 3 grid must appear in this synthesis table. The synthesis readout is not optional — it is the cross-phase consistency verification that all analysis phases are coherent.

FAIL_NO_SYNTHESIS: If this synthesis step is absent, the analysis is structurally incomplete. An analysis that populates all prior steps without a synthesis readout has not verified cross-phase coherence.

---

### Step 8: Amendment pass — PM role

Run at least one amendment pass. A pass that produces no structural change is not a valid amendment. The analysis is not complete until at least one amendment is executed.

**Amendment execution rule — read both forms before proceeding:**

**Bad form (do not do this):**
> "Noticed that the Infrastructure Lead may also be a veto risk. Will monitor."
> *No structural update produced. Grid, veto list, comms, trajectory, and synthesis are unchanged. This is not an amendment.*

**Correct form (required):**
> "Infrastructure Lead added to Phase 3 grid as Manage Closely [Source: amendment]. Trajectory: Ascending — recently joined product steering committee. Engagement Window: Week 2–4 (inherits Manage Closely window). Veto list: Infrastructure Lead added at Probability: high, Impact: scope, Mitigation: bilateral technical review scheduled 4 weeks before launch. Step 6a prefill: `decision-briefing` confirmed for Infrastructure Lead row. Step 6b: comms row added — decision-briefing via 1:1 meeting, Week 2–3. Step 7 synthesis row: Infrastructure Lead | Manage Closely | Week 2–4 | Conflict exposure: None | Champion: — | decision-briefing."

**Amendment update mandate — no observation without revision:**
Every finding must immediately update at least one structural artifact. Eligible targets: Phase 3 grid rows, Step 4 veto list entries, Step 6a prefill table (Frame Type reassignment), Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict resolution pathway entries (Resolution Authority / Decision Required / Deadline), Step 5a engagement window summaries, trajectory assessments, synthesis readout rows. No observation without revision.

FAIL_OBSERVATION_ONLY: A prose observation with no structural update to any eligible target does not satisfy the amendment requirement.

---

## V-02 — Single Axis: Synthesis as Per-Quadrant Aggregation

**Hypothesis**: C-32 permits "per stakeholder or per quadrant." A per-quadrant synthesis table (4 rows, one per quadrant) that aggregates all members of each quadrant into a single synthesis row is structurally sufficient. This produces a more compact synthesis artifact and tests whether quadrant-level aggregation satisfies the cross-phase coherence requirement.

---

### Step 0: CODEOWNERS context check — PM role

Check for a CODEOWNERS file. If present, extract org context from it. If absent, check the invocation string. If insufficient, ask exactly one question: "What org or team is this decision for?" Never infer silently. Never proceed on an assumed org structure.

FAIL_SILENT_INFERENCE: If any stakeholder analysis is produced without confirmed org context from one of these three sources, the analysis is invalid.

---

### Phase 1: Strategic conflict and structural landscape — Strategy role

**Step 1a: Structural conflicts and resolution pathways — Strategy role**

Identify at least two structural conflicts, each with both parties named and the nature of the tension stated. For each conflict, produce a resolution pathway row:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|

FAIL_ONE_PARTY: Single-party conflict entries are invalid.
FAIL_NO_RESOLUTION_PATHWAY: Any conflict without Resolution Authority, Decision Required, and Deadline is structurally incomplete. The Phase 1→2 gate requires complete pathways for all conflicts.

**Step 1b: Inertia stakeholder identification — Strategy role**

Identify all stakeholders whose primary risk is status-quo defense. Tag each `[INERTIA]` for the grid. The `displacement-acknowledgment` Frame Type will be assigned to all inertia rows at the prefill step (Step 6a), not at comms population time.

FAIL_NO_INERTIA: If the product displaces an existing tool or workflow and no inertia stakeholders are identified, the strategy analysis is incomplete.

**Step 1c: Critical-path gatekeeper tagging — Strategy role**

Tag each critical-path gatekeeper: `[CRITICAL PATH — lead time: N weeks — blocks: {specific dependency}]`

Lead time must be a specific number of weeks. The blocking reason must be specific. These lead times drive the engagement window derivation at Step 5a.

FAIL_NO_GATEKEEPER_TIMING: A critical-path tag without lead time and blocking reason is incomplete.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Required outputs present:
- [ ] Two+ conflicts with both parties, nature of tension, and resolution pathway
- [ ] Inertia stakeholders identified and tagged
- [ ] One+ critical-path gatekeeper with lead time and blocking reason

FAIL_INCOMPLETE_PHASE1: If any required output is absent, do not begin Phase 2.

---

### Phase 2: User and buyer segment analysis — UX role

**Step 2: Segment analysis — UX role**

For each distinct user or buyer segment: (1) name the segment and decision-making role; (2) state the primary job-to-be-done; (3) identify the journey stage; (4) write one specific NOT-doing statement naming a capability this product withholds for this segment.

FAIL_MONOLITH_ASSUMPTION: Segments collapsed into a single "user" without role distinctions fail this step.
FAIL_NO_NOT_DOING: Any segment without a specific NOT-doing statement fails this step.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Required: all segments identified with roles; NOT-doing statement per segment.

FAIL_INCOMPLETE_PHASE2: If required outputs are absent, do not begin Phase 3.

---

### Phase 3: Power/Interest grid construction — PM role

Build after Phase 1 and Phase 2 are complete. Do not build the grid before prior phases are finished.

| Stakeholder | Quadrant | Power | Interest | Source | Trajectory | Engagement Window | Notes |
|-------------|----------|-------|----------|--------|------------|-------------------|-------|

**Quadrant labels:** Manage Closely / Keep Satisfied / Keep Informed / Monitor

**Source accepted values:** `CODEOWNERS` / `initial-inventory` / `conflict-discovery` / `ux-discovery` / `amendment`

**Trajectory column — required per row:**
Each entry: direction (ascending toward advocate / stable / descending toward risk) + one observable signal (e.g., "increased attendance at steering meetings," "delegated three consecutive responses").

FAIL_NO_TRAJECTORY: Any row without a Trajectory entry renders the grid incomplete.
FAIL_PROSE_ONLY: Stakeholders listed in prose without a grid structure fail this step.
FAIL_NO_SOURCE: Any row without a Source entry is missing provenance.

Notes column: apply `[INERTIA]` for all inertia-classified stakeholders. Apply `[CRITICAL PATH]` for gatekeepers tagged in Step 1c.

Minimum 4 rows.

---

### Step 4: Veto risk ranking — PM role

List veto-capable stakeholders ordered by probability, highest first. Not alphabetical. Not by grid sequence.

| Stakeholder | Probability | Impact | Mitigation |
|-------------|-------------|--------|------------|

FAIL_WRONG_ORDER: Non-probability-ordered lists are invalid.
FAIL_NO_MITIGATION: Entries without a mitigation field are incomplete.

---

### Step 5a: Engagement window derivation — PM role

Produce a per-quadrant engagement window table from the Step 1c lead times and Phase 3 quadrant positions:

| Quadrant | Earliest Engage | Latest Engage | Constraint Rationale |
|----------|----------------|---------------|---------------------|

The Phase 3 grid already carries an Engagement Window column (added above). Populate it from this derivation. Step 6b timing must fall within this window per quadrant.

FAIL_NO_ENGAGEMENT_WINDOW: Grid without Engagement Window column is incomplete.
FAIL_NO_WINDOW_SUMMARY: Any quadrant without a derived window is unconstrained.

---

### Step 5b: Champion identification and action — PM role

Name the champion(s) and assign a schedulable action. The action must be placeable on a calendar today with a specific venue or meeting context.

FAIL_GENERIC_CHAMPION: "Engage the champion" and equivalent vague language do not satisfy this step.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|----------|
| Authority | | |
| Proximity | | |
| Commitment | | |

Composite >= 9 required.

FAIL_BELOW_CHAMPION_THRESHOLD: Composite below 9 requires champion reassessment before proceeding.

---

### Step 5d: Champion durability — PM role

1. **Succession path**: name who assumes the champion role if the current champion exits, or document the SPOF.
2. **Deterioration signals**: two or more observable triggers indicating eroding commitment.

FAIL_NO_DURABILITY: Succession path absent or fewer than two deterioration signals — durability assessment is incomplete.

---

### Step 6a: Frame Type prefill table — PM role

Prefill all four quadrant Frame Types before populating comms rows. Values not in this table are prohibited.

| Quadrant | Assigned Frame Type |
|----------|---------------------|
| Manage Closely | decision-briefing |
| Keep Satisfied | executive-summary |
| Keep Informed | progress-pulse |
| Monitor | changelog |

**Rule 1**: No comms row may use a Frame Type not in this table.
**Rule 2**: All inertia-classified rows must receive `displacement-acknowledgment` here, at this step, before any comms row is populated.

FAIL_MISSING_DISPLACEMENT_PREFILL: Displacement-acknowledgment assignment deferred past this step breaks the inertia chain.

---

### Step 6b: Communication strategy per quadrant — PM role

One row per quadrant:

| Quadrant | Message | Frame Type | Timing | Channel |
|----------|---------|------------|--------|---------|

Timing must fall within the Step 5a derived window. Frame Type must match Step 6a assignment. Channel must be specific.

FAIL_SAME_FRAME: Two or more rows sharing a Frame Type violate the prefill constraint.
FAIL_VAGUE_TIMING: Non-relative timing anchors ("when appropriate") are invalid.
FAIL_WINDOW_MISMATCH: Timing outside the Step 5a derived window is invalid.

---

### Step 7: Cross-phase synthesis readout — per-quadrant format — PM role

After completing all analysis phases and the comms step, produce a synthesis readout aggregated by quadrant. One synthesis row per quadrant:

| Quadrant | Members | Engagement Window | Conflicts Represented | Champion Present | Frame Type |
|----------|---------|-------------------|----------------------|------------------|------------|

- **Members**: all stakeholder names in this quadrant
- **Engagement Window**: range from Step 5a for this quadrant
- **Conflicts Represented**: any Step 1a conflict whose parties include at least one member of this quadrant, or "None"
- **Champion Present**: "Yes — [name]" if a champion resides in this quadrant, otherwise "No"
- **Frame Type**: the prefilled Frame Type for this quadrant from Step 6a

Every quadrant with at least one member must have a synthesis row. This step confirms that engagement window, conflict exposure, champion placement, and frame type are coherent across phases for each quadrant.

FAIL_NO_SYNTHESIS: If this synthesis step is absent, cross-phase coherence has not been verified. The analysis is structurally incomplete.

---

### Step 8: Amendment pass — PM role

Run at least one amendment pass that produces a structural update. Prose observations without structural changes are not amendments.

**Amendment execution rule — read both forms:**

**Bad form (do not do this):**
> "The Platform Architect may have concerns about the API contract. Worth noting for later."
> *Observation only. No grid row, veto entry, comms row, or synthesis row updated.*

**Correct form (required):**
> "Platform Architect added to Phase 3 grid as Manage Closely [Source: amendment]. Trajectory: Descending — three API design meetings declined. Engagement Window: Week 1–4 (inherits Manage Closely window). Step 4 veto list: Platform Architect added, Probability: high, Impact: technical scope, Mitigation: async API spec review circulated 2 weeks prior. Step 6a prefill: `decision-briefing` confirmed. Step 6b: comms row added, timing Week 2. Synthesis update: Manage Closely quadrant — Members list updated to include Platform Architect; Conflicts Represented updated to include API Contract Conflict."

**Amendment update mandate — no observation without revision:**
Every finding must update at least one structural artifact. Eligible targets: Phase 3 grid rows, Step 4 veto list entries, Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict resolution pathway entries (Resolution Authority / Decision Required / Deadline), Step 5a engagement window summaries, trajectory assessments, synthesis readout rows. No observation without revision.

FAIL_OBSERVATION_ONLY: A prose observation with no structural update does not satisfy the amendment requirement.

---

## V-03 — Single Axis: Phrasing Register — Constraint-Rule Format

**Hypothesis**: A machine-parseable constraint-rule format (RULE / GATE / FAIL only — no coaching prose, no "consider," no "you should") satisfies all 32 criteria. The structural requirements are determined by the presence of named elements, not by the phrasing used to mandate them. Dense imperative syntax produces lower token count without criterion loss.

---

### STEP-0 — CODEOWNERS context check — PM role

RULE-0.1: Check for a CODEOWNERS file. If present, extract org context.
RULE-0.2: If CODEOWNERS absent, extract org context from the invocation string.
RULE-0.3: If invocation context insufficient, ask exactly one question: "What org or team is this decision for?"
RULE-0.4: Do not construct any stakeholder analysis until org context is confirmed from one of the three sources above.

FAIL_SILENT_INFERENCE: Violation of RULE-0.4 invalidates the analysis.

---

### PHASE-1 — Strategic conflict and structural landscape — Strategy role

**STEP-1A — Structural conflicts and resolution pathways — Strategy role**

RULE-1A.1: Identify a minimum of two structural conflicts.
RULE-1A.2: Each conflict entry must name both parties and state the nature of the tension.
RULE-1A.3: For each conflict, produce a resolution pathway row with: Resolution Authority / Decision Required / Deadline.

FAIL_ONE_PARTY: Conflict entry with fewer than two named parties — invalid.
FAIL_NO_RESOLUTION_PATHWAY: Conflict entry without Resolution Authority, Decision Required, and Deadline — invalid.

**STEP-1B — Inertia stakeholder identification — Strategy role**

RULE-1B.1: Identify all stakeholders whose primary risk is status-quo defense.
RULE-1B.2: Tag each with `[INERTIA]` for grid entry.
RULE-1B.3: `displacement-acknowledgment` Frame Type is mandatory for all `[INERTIA]`-tagged rows. This assignment is made at STEP-6A, not at comms population time.

FAIL_NO_INERTIA: Product displaces an existing tool or workflow with no inertia stakeholders identified — invalid.

**STEP-1C — Critical-path gatekeeper tagging — Strategy role**

RULE-1C.1: Tag each gatekeeper who controls a blocking dependency: `[CRITICAL PATH — lead time: N weeks — blocks: {dependency}]`
RULE-1C.2: Lead time must be a specific number of weeks.
RULE-1C.3: Blocking reason must identify the specific dependency, not a generic importance label.

FAIL_NO_GATEKEEPER_TIMING: Critical-path tag without lead time and blocking reason — invalid.

---

### GATE-1 — Phase 1 → Phase 2 Transition — Strategy role

CHECK-1.1: Two+ conflicts present with both parties and nature stated.
CHECK-1.2: Resolution pathway complete per conflict.
CHECK-1.3: Inertia stakeholders identified and tagged.
CHECK-1.4: One+ critical-path gatekeeper with lead time and blocking reason.
CHECK-1.5: Resolution pathway present for every named conflict.

FAIL_INCOMPLETE_PHASE1: Any CHECK-1.x absent — Phase 2 must not begin.

---

### PHASE-2 — User and buyer segment analysis — UX role

**STEP-2 — Segment analysis — UX role**

RULE-2.1: For each distinct user or buyer segment, produce: segment name, decision-making role (buyer/user/influencer), primary job-to-be-done, journey stage, and NOT-doing statement.
RULE-2.2: The NOT-doing statement must name a specific capability or outcome the product intentionally withholds for this segment.
RULE-2.3: "Out of scope" and equivalent generic phrases are prohibited as NOT-doing statements.

FAIL_MONOLITH_ASSUMPTION: Segments collapsed without role distinctions — invalid.
FAIL_NO_NOT_DOING: Segment without specific NOT-doing statement — invalid.

---

### GATE-2 — Phase 2 → Phase 3 Transition — PM role

CHECK-2.1: All segments present with decision-making roles.
CHECK-2.2: NOT-doing statement per segment (specific capability named).

FAIL_INCOMPLETE_PHASE2: Any CHECK-2.x absent — Phase 3 must not begin.

---

### PHASE-3 — Power/Interest grid construction — PM role

RULE-3.1: Build the grid only after GATE-1 and GATE-2 are cleared.
RULE-3.2: Grid columns required: Stakeholder / Quadrant / Power / Interest / Source / Trajectory / Engagement Window / Notes.
RULE-3.3: Quadrant labels: Manage Closely (HP/HI) / Keep Satisfied (HP/LI) / Keep Informed (LP/HI) / Monitor (LP/LI).
RULE-3.4: Source accepted values: `CODEOWNERS` / `initial-inventory` / `conflict-discovery` / `ux-discovery` / `amendment`.
RULE-3.5: Trajectory entry per row: direction (ascending toward advocate / stable / descending toward risk) + one observable signal.
RULE-3.6: Engagement Window entry per row: derived from STEP-5A. Initially placeholder; finalize after STEP-5A executes.
RULE-3.7: Apply `[INERTIA]` in Notes for all inertia-tagged stakeholders from STEP-1B.
RULE-3.8: Minimum 4 rows.

FAIL_PROSE_ONLY: Stakeholder list in prose without grid structure — invalid.
FAIL_NO_SOURCE: Any row without Source entry — invalid.
FAIL_NO_TRAJECTORY: Any row without Trajectory entry — grid incomplete.
FAIL_NO_ENGAGEMENT_WINDOW: Any row without Engagement Window entry after STEP-5A — grid incomplete.

---

### STEP-4 — Veto risk ranking — PM role

RULE-4.1: List all veto-capable stakeholders ordered by probability, highest first.
RULE-4.2: Do not sort alphabetically or by grid sequence.
RULE-4.3: Required columns: Stakeholder / Probability / Impact / Mitigation.
RULE-4.4: Mitigation must be a specific response strategy, not a generic note.

FAIL_WRONG_ORDER: Non-probability-ordered veto list — invalid.
FAIL_NO_MITIGATION: Veto entry without Mitigation — invalid.

---

### STEP-5A — Engagement window derivation — PM role

RULE-5A.1: Produce per-quadrant window derivation table: Quadrant / Earliest Engage / Latest Engage / Constraint Rationale.
RULE-5A.2: Derive windows from STEP-1C lead times and PHASE-3 quadrant positions.
RULE-5A.3: Populate the Engagement Window column in the PHASE-3 grid from this derivation.
RULE-5A.4: STEP-6B timing must fall within the derived window for its quadrant.

FAIL_NO_WINDOW_SUMMARY: Quadrant without derived window — unconstrained — invalid.
FAIL_WINDOW_MISMATCH (applied at STEP-6B): Timing outside derived window — invalid.

---

### STEP-5B — Champion identification and action — PM role

RULE-5B.1: Identify one+ champion with demonstrated authority and motivation.
RULE-5B.2: Assign a schedulable action: specific enough to place on a calendar today with named venue or meeting.

FAIL_GENERIC_CHAMPION: "Engage the champion" or equivalent vague action — invalid.

---

### STEP-5C — Champion depth scoring — PM role

RULE-5C.1: Score champion on Authority / Proximity / Commitment (each 1–5).
RULE-5C.2: Composite (sum of three scores) must be >= 9 to proceed.

FAIL_BELOW_CHAMPION_THRESHOLD: Composite < 9 — champion reassessment required before proceeding.

---

### STEP-5D — Champion durability — PM role

RULE-5D.1: Name the succession path if the champion exits (name successor or document SPOF).
RULE-5D.2: Identify 2+ deterioration signals (observable triggers for eroding commitment).

FAIL_NO_DURABILITY: Succession path absent or fewer than two deterioration signals — incomplete.

---

### STEP-6A — Frame Type prefill table — PM role

RULE-6A.1: Produce a standalone prefill table before populating comms rows.
RULE-6A.2: Accepted Frame Type values:

| Quadrant | Assigned Frame Type |
|----------|---------------------|
| Manage Closely | decision-briefing |
| Keep Satisfied | executive-summary |
| Keep Informed | progress-pulse |
| Monitor | changelog |

RULE-6A.3: Frame Types not in this table are prohibited in STEP-6B rows.
RULE-6A.4: All inertia-classified rows must receive `displacement-acknowledgment` at this step, before any comms row is populated.

FAIL_MISSING_DISPLACEMENT_PREFILL: `displacement-acknowledgment` assignment deferred past this step — inertia chain broken.

---

### STEP-6B — Communication strategy per quadrant — PM role

RULE-6B.1: Produce one row per quadrant: Quadrant / Message / Frame Type / Timing / Channel.
RULE-6B.2: Frame Type must match STEP-6A prefill assignment.
RULE-6B.3: Timing must be a relative anchor falling within the STEP-5A derived window.
RULE-6B.4: Channel must be a specific medium.

FAIL_SAME_FRAME: Two+ rows with identical Frame Type — prefill constraint violated.
FAIL_VAGUE_TIMING: Non-relative timing anchor — invalid.
FAIL_WINDOW_MISMATCH: Timing outside STEP-5A derived window — invalid.

---

### STEP-7 — Cross-phase synthesis readout — PM role

RULE-7.1: After completing all analysis phases and STEP-6B, produce a per-stakeholder synthesis table.
RULE-7.2: Required columns: Stakeholder / Grid Position / Engagement Window / Conflict Exposure / Champion Status / Frame Type.
RULE-7.3: Grid Position: quadrant label from PHASE-3.
RULE-7.4: Engagement Window: range from STEP-5A.
RULE-7.5: Conflict Exposure: name any STEP-1A conflict involving this stakeholder, or "None."
RULE-7.6: Champion Status: "Champion" if designated in STEP-5B, otherwise "—."
RULE-7.7: Frame Type: prefill assignment from STEP-6A.
RULE-7.8: Every stakeholder in the PHASE-3 grid must appear in the synthesis table.

FAIL_NO_SYNTHESIS: Synthesis step absent — cross-phase coherence unverified — analysis incomplete.

---

### STEP-8 — Amendment pass — PM role

RULE-8.1: Run at least one amendment pass that produces a structural update.
RULE-8.2: Read both forms before executing:

**BAD FORM (prohibited):**
> "Security team may be a veto risk. Flagged for future review."
> No structural update. Not an amendment.

**CORRECT FORM (required):**
> "Security Team added to PHASE-3 grid as Keep Satisfied [Source: amendment]. Trajectory: Ascending — security review participation rate increased in last two sprints. Engagement Window: inherits Keep Satisfied window (Week 3–6). STEP-4 veto list: Security Team added, Probability: medium, Impact: compliance scope, Mitigation: security review scheduled Week 3. STEP-6A prefill: `executive-summary` confirmed for Security Team. STEP-6B: comms row added, executive-summary via email, Week 3. STEP-7 synthesis row: Security Team | Keep Satisfied | Week 3–6 | Conflict exposure: None | Champion: — | executive-summary."

RULE-8.3: Amendment update mandate — no observation without revision. Eligible targets: PHASE-3 grid rows / STEP-4 veto list entries / STEP-6A prefill table / STEP-6B comms rows / STEP-1C gatekeeper lead-time tags / conflict resolution pathway entries (Resolution Authority / Decision Required / Deadline) / STEP-5A engagement window summaries / trajectory assessments / synthesis readout rows. No observation without revision.

FAIL_OBSERVATION_ONLY: Prose observation without structural update — not an amendment.

---

## V-04 — Combination: Trajectory Column + Synthesis with Explicit Source Attribution

**Hypothesis**: C-32 synthesis quality is maximized when each synthesis column header explicitly names its source step (e.g., "Grid Position [Phase 3]" rather than just "Grid Position"). This makes the cross-phase aggregation nature of the synthesis step structurally visible and easier to verify. Combined with V-01's trajectory-as-grid-column placement, this produces the most explicit cross-phase coherence artifact of any variation.

---

### Step 0: CODEOWNERS context check — PM role

This is the most consequential check in the analysis. Org context determines whether the stakeholder map reflects the actual decision-making structure or an assumed one.

Check for a CODEOWNERS file. If present, extract org and team context. If absent, check the invocation string for org or team context. If invocation context is also insufficient, ask exactly one question: "What org or team is this decision for?" Do not proceed on an assumed org structure. Do not infer silently.

FAIL_SILENT_INFERENCE: If stakeholder analysis is constructed without confirmed org context from one of the three sources above, the analysis is invalid.

---

### Phase 1: Strategic conflict and structural landscape — Strategy role

**Step 1a: Structural conflicts and resolution pathways — Strategy role**

Identify at least two structural conflicts. Both parties in each conflict must be named. The nature of the tension must be stated. For each conflict, extend the entry with a resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|

Resolution Authority = who has organizational decision-making power to resolve this conflict. Decision Required = the specific ruling or determination needed. Deadline = the date or milestone by which resolution must occur.

FAIL_ONE_PARTY: A conflict entry naming only one party is not a conflict.
FAIL_NO_RESOLUTION_PATHWAY: A conflict entry without complete Resolution Authority, Decision Required, and Deadline does not pass. The Phase 1→2 transition gate requires all conflicts to have complete pathways.

**Step 1b: Inertia stakeholder identification — Strategy role**

Identify stakeholders whose primary risk is status-quo defense — satisfied with the current state, not actively opposed. Tag each `[INERTIA]` for grid classification. The `displacement-acknowledgment` Frame Type is mandatory for all inertia-classified rows and will be assigned at Step 6a, not at comms population time.

FAIL_NO_INERTIA: If the product displaces an existing tool, workflow, or budget line and no inertia stakeholders appear, the strategy phase is incomplete.

**Step 1c: Critical-path gatekeeper tagging — Strategy role**

Tag each gatekeeper who controls a blocking dependency: `[CRITICAL PATH — lead time: N weeks — blocks: {specific dependency}]`. Specific weeks and specific blocking reason are required. These lead times are the input data for the engagement window derivation at Step 5a.

FAIL_NO_GATEKEEPER_TIMING: A critical-path tag without specific lead time and blocking reason does not satisfy this step.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Verify before proceeding:
- [ ] Two+ conflicts with both parties, nature, and complete resolution pathway
- [ ] Inertia stakeholders identified and tagged
- [ ] One+ critical-path gatekeeper with specific lead time and blocking reason
- [ ] Resolution pathway present for every named conflict

FAIL_INCOMPLETE_PHASE1: Any missing output above stops Phase 2 from beginning.

---

### Phase 2: User and buyer segment analysis — UX role

**Step 2: Segment analysis and NOT-doing framing — UX role**

For each user or buyer segment: (1) name the segment with its decision-making role (buyer / user / influencer); (2) state the primary job-to-be-done; (3) identify the journey stage of intersection; (4) write one NOT-doing statement naming a specific capability or outcome this product intentionally withholds for this segment. "Out of scope" is not a NOT-doing statement.

FAIL_MONOLITH_ASSUMPTION: Collapsed "user" description without segment role differentiation fails this phase.
FAIL_NO_NOT_DOING: Any segment without a specific NOT-doing statement fails this phase.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Verify: all segments have decision-making roles and specific NOT-doing statements.

FAIL_INCOMPLETE_PHASE2: Missing outputs stop Phase 3 from beginning.

---

### Phase 3: Power/Interest grid construction — PM role

Build this grid now — after Phase 1 and Phase 2 are complete. Do not construct the grid before prior phases are finished.

Columns required:

| Stakeholder | Quadrant | Power | Interest | Source | Trajectory | Engagement Window | Notes |
|-------------|----------|-------|----------|--------|------------|-------------------|-------|

**Quadrant labels:** Manage Closely (HP/HI) / Keep Satisfied (HP/LI) / Keep Informed (LP/HI) / Monitor (LP/LI)

**Source accepted values:** `CODEOWNERS` / `initial-inventory` / `conflict-discovery` / `ux-discovery` / `amendment`

**Trajectory column:** For each stakeholder, enter: direction (ascending toward advocate / stable / descending toward risk) + one observable signal rationale confirming the direction (e.g., "joined steering committee 2 weeks ago," "delegated last three review requests to a report," "no meeting attendance in past month").

**Engagement Window column:** Initially blank; populated from Step 5a derivation. A grid row without an Engagement Window entry after Step 5a completes is structurally incomplete.

Notes: Apply `[INERTIA]` for all inertia-classified stakeholders. Apply `[CRITICAL PATH]` for gatekeepers from Step 1c.

FAIL_NO_TRAJECTORY: Any stakeholder row without a Trajectory entry — grid incomplete.
FAIL_NO_ENGAGEMENT_WINDOW: Any stakeholder row without an Engagement Window entry after Step 5a — grid incomplete.
FAIL_PROSE_ONLY: Stakeholders described in prose without a grid structure — invalid.
FAIL_NO_SOURCE: Any grid row without a Source entry — provenance untracked.

Minimum 4 rows.

---

### Step 4: Veto risk ranking — PM role

List all veto-capable stakeholders ordered by probability, highest first. Not alphabetical. Not grid sequence. Probability rank must drive the order.

| Stakeholder | Probability | Impact | Mitigation |
|-------------|-------------|--------|------------|

Mitigation = specific response strategy if the veto risk materializes (e.g., "schedule bilateral review 3 weeks prior," "present ROI case to executive sponsor first").

FAIL_WRONG_ORDER: List not ordered by probability — invalid.
FAIL_NO_MITIGATION: Entry without a mitigation field — incomplete.

---

### Step 5a: Engagement window derivation — PM role

Synthesize the Step 1c critical-path lead times and Phase 3 quadrant positions into a per-quadrant engagement window:

| Quadrant | Earliest Engage | Latest Engage | Constraint Rationale |
|----------|----------------|---------------|---------------------|

Derive: Manage Closely windows are bounded by the maximum lead time among Manage Closely gatekeepers. Propagate window logic to other quadrants based on their dependency relationship to the critical path.

Populate the Engagement Window column in the Phase 3 grid using the derived ranges. Step 6b timing must fall within the derived window for its quadrant.

FAIL_NO_WINDOW_SUMMARY: Quadrant without a derived window is unconstrained — invalid.
FAIL_WINDOW_MISMATCH (enforced at Step 6b): Comms timing anchor outside the derived window — invalid.

---

### Step 5b: Champion identification and action — PM role

Identify the champion(s). Assign a schedulable action per champion. The action must be specific enough to place on a calendar with a named meeting venue or context today.

FAIL_GENERIC_CHAMPION: Vague actions ("engage champion," "build relationship") do not satisfy this step.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|----------|
| Authority | | Org power to advocate for or unblock the feature |
| Proximity | | Relationship access to blockers and sponsors |
| Commitment | | Demonstrated investment in success |

Composite must be >= 9.

FAIL_BELOW_CHAMPION_THRESHOLD: Composite < 9 requires champion reassessment before proceeding.

---

### Step 5d: Champion durability — PM role

1. **Succession path**: If the champion exits, who takes over? Name the successor or document as SPOF.
2. **Deterioration signals**: Two or more observable triggers indicating commitment is eroding.

FAIL_NO_DURABILITY: Succession path or deterioration signals absent — incomplete.

---

### Step 6a: Frame Type prefill table — PM role

Before populating comms rows, complete this prefill table. Prohibited: Frame Type values not appearing in this table.

| Quadrant | Assigned Frame Type |
|----------|---------------------|
| Manage Closely | decision-briefing |
| Keep Satisfied | executive-summary |
| Keep Informed | progress-pulse |
| Monitor | changelog |

Rule 1: No comms row may use a Frame Type not listed here.
Rule 2: All `[INERTIA]`-tagged rows must receive `displacement-acknowledgment` at this step, before any comms row is populated. This assignment must appear in this prefill table, not in a comms row instruction.

FAIL_MISSING_DISPLACEMENT_PREFILL: Inertia Frame Type assignment deferred past this step — inertia chain broken.

---

### Step 6b: Communication strategy per quadrant — PM role

One row per quadrant:

| Quadrant | Message | Frame Type | Timing | Channel |
|----------|---------|------------|--------|---------|

Frame Type must match the Step 6a assignment. Timing must fall within the Step 5a derived window for this quadrant. Channel must be specific.

FAIL_SAME_FRAME: Two or more rows sharing a Frame Type — prefill constraint violated.
FAIL_VAGUE_TIMING: Non-specific relative anchors prohibited.
FAIL_WINDOW_MISMATCH: Timing outside Step 5a window — invalid.

---

### Step 7: Cross-phase synthesis readout — PM role

After completing all analysis phases and the comms step, produce a per-stakeholder synthesis readout. Each synthesis row explicitly attributes its data to its source phase to confirm cross-phase consistency.

| Stakeholder | Grid Position [Phase 3] | Engagement Window [Step 5a] | Conflict Exposure [Step 1a] | Champion Status [Step 5b] | Frame Type [Step 6a] |
|-------------|------------------------|----------------------------|-----------------------------|--------------------------|--------------------|

- **Grid Position [Phase 3]**: quadrant label exactly as assigned in Phase 3
- **Engagement Window [Step 5a]**: the derived window range for this stakeholder's quadrant
- **Conflict Exposure [Step 1a]**: name any Step 1a conflict involving this stakeholder, or "None"
- **Champion Status [Step 5b]**: "Champion — [schedulable action]" if designated, otherwise "—"
- **Frame Type [Step 6a]**: the prefill assignment from Step 6a for this stakeholder's quadrant

Every stakeholder in the Phase 3 grid must appear in the synthesis table. The source attribution in each column header makes the cross-phase dependency chain explicit and inspectable — any inconsistency between the synthesis table and the source phase is immediately visible.

FAIL_NO_SYNTHESIS: Synthesis step absent — cross-phase coherence has not been verified. The analysis is structurally incomplete regardless of how well the prior phases were executed.

---

### Step 8: Amendment pass — PM role

Run at least one amendment pass. The pass must produce at least one structural update to an eligible target.

**Amendment execution rule — read both forms before proceeding:**

**Bad form (do not do this):**
> "Data Engineering Lead seems skeptical based on the last meeting. Keep an eye on their trajectory."
> *Observation only. No structural artifact updated. Not an amendment.*

**Correct form (required):**
> "Data Engineering Lead added to Phase 3 grid as Manage Closely [Source: amendment]. Trajectory: Descending toward risk — missed last two alignment meetings; delegated last three review requests. Engagement Window: inherits Manage Closely window from Step 5a. Step 4 veto list: Data Engineering Lead added, Probability: high, Impact: data pipeline scope, Mitigation: 1:1 technical alignment meeting scheduled 3 weeks prior to review. Step 6a prefill: `decision-briefing` confirmed. Step 6b: comms row added — decision-briefing via 1:1, Week 2 (within Manage Closely window). Step 7 synthesis row: Data Engineering Lead | Manage Closely [Phase 3] | Week 2–4 [Step 5a] | Conflict exposure: Data Ownership Conflict [Step 1a] | Champion: — | decision-briefing [Step 6a]."

**Amendment update mandate — no observation without revision:**
Every finding must update at least one structural artifact. Eligible targets: Phase 3 grid rows, Step 4 veto list entries, Step 6a prefill table (Frame Type reassignment), Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict resolution pathway entries (Resolution Authority / Decision Required / Deadline), Step 5a engagement window summaries, trajectory assessments, synthesis readout rows. No observation without revision.

FAIL_OBSERVATION_ONLY: A prose observation with no structural update to any eligible target does not constitute an amendment.

---

## V-05 — All 32 at Maximum Density

**Hypothesis**: The complete criterion set (C-01 through C-32) is achievable at maximum compression — all structural elements present, no coaching prose, no explanatory padding, FAIL labels dense, step bodies minimal. Inherits V-04's trajectory-as-grid-column and attributed synthesis. Full nine-target amendment mandate. 210/210 target.

---

### Step 0: CODEOWNERS context check — PM role

Check CODEOWNERS → invocation string → one question: "What org or team is this decision for?" Three sources, in order. First confirmed source wins. Do not construct any analysis before org context is confirmed from one of these sources.

FAIL_SILENT_INFERENCE: Analysis constructed without confirmed org context — invalid.

---

### Phase 1: Strategy analysis — Strategy role

**Step 1a: Conflicts and resolution pathways — Strategy role**

Two+ structural conflicts required. Per conflict: both parties named, nature of tension stated, plus resolution pathway row (Resolution Authority / Decision Required / Deadline).

FAIL_ONE_PARTY: Conflict naming only one party — invalid.
FAIL_NO_RESOLUTION_PATHWAY: Conflict without complete Resolution Authority, Decision Required, and Deadline — invalid.

**Step 1b: Inertia stakeholder mapping — Strategy role**

Identify all status-quo-defending stakeholders. Tag each `[INERTIA]`. The `displacement-acknowledgment` Frame Type assignment is executed at Step 6a, not at comms time.

FAIL_NO_INERTIA: Product displaces existing workflow with no inertia stakeholders identified — invalid.

**Step 1c: Critical-path gatekeeper tagging — Strategy role**

Tag: `[CRITICAL PATH — lead time: N weeks — blocks: {dependency}]`. Lead time = specific weeks. Blocking reason = specific dependency. These feed Step 5a window synthesis.

FAIL_NO_GATEKEEPER_TIMING: Critical-path tag without specific lead time and blocking reason — invalid.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Required: two+ complete conflicts with pathways / inertia stakeholders tagged / one+ gatekeeper with lead time.

FAIL_INCOMPLETE_PHASE1: Any required output absent — Phase 2 blocked.

---

### Phase 2: Segment analysis — UX role

**Step 2: User and buyer segments — UX role**

Per segment: name + decision-making role (buyer/user/influencer) + job-to-be-done + journey stage + one specific NOT-doing statement (specific withheld capability — "out of scope" prohibited).

FAIL_MONOLITH_ASSUMPTION: Segments collapsed into undifferentiated "user" — invalid.
FAIL_NO_NOT_DOING: Segment without specific NOT-doing statement — invalid.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Required: all segments with roles + specific NOT-doing per segment.

FAIL_INCOMPLETE_PHASE2: Required outputs absent — Phase 3 blocked.

---

### Phase 3: Power/Interest grid — PM role

Build after Phase 1 and Phase 2 complete. Not before.

| Stakeholder | Quadrant | Power | Interest | Source | Trajectory | Engagement Window | Notes |

Quadrants: Manage Closely (HP/HI) / Keep Satisfied (HP/LI) / Keep Informed (LP/HI) / Monitor (LP/LI)

Source values: `CODEOWNERS` / `initial-inventory` / `conflict-discovery` / `ux-discovery` / `amendment`

**Trajectory** — required per row: direction (ascending toward advocate / stable / descending toward risk) + one observable signal (e.g., "attended three consecutive steering meetings," "response latency now 72+ hours," "delegated last review request").

**Engagement Window** — populated from Step 5a; leave blank until Step 5a completes. FAIL_NO_ENGAGEMENT_WINDOW if empty after Step 5a.

Notes: `[INERTIA]` per Step 1b. `[CRITICAL PATH]` per Step 1c.

Minimum 4 rows.

FAIL_PROSE_ONLY: Prose stakeholder list without grid — invalid.
FAIL_NO_SOURCE: Any row without Source — invalid.
FAIL_NO_TRAJECTORY: Any row without Trajectory — invalid.
FAIL_NO_ENGAGEMENT_WINDOW: Any row without Engagement Window after Step 5a — invalid.

---

### Step 4: Veto risk ranking — PM role

Ordered by probability, highest first. Not alphabetical. Not grid sequence.

| Stakeholder | Probability | Impact | Mitigation |

Mitigation = specific response strategy per entry.

FAIL_WRONG_ORDER: Non-probability order — invalid.
FAIL_NO_MITIGATION: Entry without mitigation — invalid.

---

### Step 5a: Engagement window derivation — PM role

Synthesize Step 1c lead times + Phase 3 quadrant positions:

| Quadrant | Earliest Engage | Latest Engage | Constraint Rationale |

Populate the Engagement Window column in Phase 3 grid from this derivation. Step 6b timing must fall within the derived window per quadrant.

FAIL_NO_WINDOW_SUMMARY: Quadrant without derived window — unconstrained — invalid.

---

### Step 5b: Champion identification and action — PM role

Name champion(s). Schedulable action required per champion. Action must be placeable on a calendar today.

FAIL_GENERIC_CHAMPION: "Engage the champion" or equivalent vague language — not a champion action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) |
|-----------|-------------|
| Authority | |
| Proximity | |
| Commitment | |

Composite >= 9 to proceed.

FAIL_BELOW_CHAMPION_THRESHOLD: Composite < 9 — champion reassessment required before proceeding.

---

### Step 5d: Champion durability — PM role

1. Succession path: name the successor if champion exits, or document SPOF.
2. Two+ deterioration signals: observable triggers indicating eroding commitment.

FAIL_NO_DURABILITY: Succession path absent or fewer than two deterioration signals — incomplete.

---

### Step 6a: Frame Type prefill table — PM role

Prefill before any comms row is populated. Values not in this table are prohibited in Step 6b.

| Quadrant | Assigned Frame Type |
|----------|---------------------|
| Manage Closely | decision-briefing |
| Keep Satisfied | executive-summary |
| Keep Informed | progress-pulse |
| Monitor | changelog |

Rule 1: No comms row may use a Frame Type not in this table.
Rule 2: All `[INERTIA]`-tagged rows receive `displacement-acknowledgment` here, at this step. Not at Step 6b content time.

FAIL_MISSING_DISPLACEMENT_PREFILL: `displacement-acknowledgment` assignment deferred past this step — inertia chain broken.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Message | Frame Type | Timing | Channel |

Frame Type = Step 6a assignment. Timing = relative anchor within Step 5a derived window. Channel = specific medium.

FAIL_SAME_FRAME: Two+ rows with identical Frame Type — prefill constraint violated.
FAIL_VAGUE_TIMING: Non-relative timing anchor — invalid.
FAIL_WINDOW_MISMATCH: Timing outside Step 5a derived window — invalid.

---

### Step 7: Cross-phase synthesis readout — PM role

After all phases and Step 6b, produce per-stakeholder synthesis. Every Phase 3 grid member must have a synthesis row.

| Stakeholder | Grid Position [Phase 3] | Engagement Window [Step 5a] | Conflict Exposure [Step 1a] | Champion Status [Step 5b] | Frame Type [Step 6a] |

- Grid Position: exact quadrant label
- Engagement Window: derived range
- Conflict Exposure: Step 1a conflict name or "None"
- Champion Status: "Champion — [action]" or "—"
- Frame Type: Step 6a prefill value

FAIL_NO_SYNTHESIS: Synthesis step absent — cross-phase coherence not verified — analysis structurally incomplete.

---

### Step 8: Amendment pass — PM role

Minimum one amendment pass producing at least one structural update.

**Bad form (prohibited):**
> "Legal team flagged as possible concern. Worth watching."
> No structural update. Not an amendment.

**Correct form (required):**
> "Legal Counsel added to Phase 3 grid as Keep Satisfied [Source: amendment]. Trajectory: Ascending — two recent compliance review requests initiated. Engagement Window: inherits Keep Satisfied window (Week 4–7). Step 4 veto list: Legal Counsel, Probability: high, Impact: go/no-go compliance gate, Mitigation: legal review package distributed Week 3. Step 6a prefill: `executive-summary` confirmed. Step 6b: comms row added — executive-summary via email, Week 4. Step 7 synthesis row: Legal Counsel | Keep Satisfied [Phase 3] | Week 4–7 [Step 5a] | Conflict exposure: Compliance Scope Conflict [Step 1a] | Champion: — | executive-summary [Step 6a]."

**Amendment update mandate — no observation without revision:**
Every finding must update at least one structural artifact immediately on discovery. Eligible targets: Phase 3 grid rows, Step 4 veto list entries, Step 6a prefill table (Frame Type reassignment), Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict resolution pathway entries (Resolution Authority / Decision Required / Deadline), Step 5a engagement window summaries, trajectory assessments, synthesis readout rows. No observation without revision.

FAIL_OBSERVATION_ONLY: Prose observation without structural update to any eligible target — not an amendment.

---

## Summary — Round 12 Variation Map

| Variation | Axis | C-31 Placement | C-32 Format | Score Target |
|-----------|------|----------------|-------------|--------------|
| V-01 | Trajectory as native grid column | Grid column (Phase 3) | Per-stakeholder table | 210/210 |
| V-02 | Synthesis as per-quadrant aggregation | Grid column (Phase 3) | Per-quadrant table (4 rows) | 210/210 |
| V-03 | Phrasing register: constraint-rule format | Grid column (RULE-3.5) | Per-stakeholder table (RULE-7.x) | 210/210 |
| V-04 | Trajectory column + attributed synthesis | Grid column (Phase 3) | Per-stakeholder with source labels | 210/210 |
| V-05 | All 32 at maximum density | Grid column (dense) | Per-stakeholder attributed (dense) | 210/210 |

**New patterns to watch for C-33+ extraction:**
1. **Source attribution in synthesis headers** (V-04/V-05): Labeling synthesis columns with `[Phase 3]`, `[Step 5a]`, `[Step 1a]` etc. makes cross-phase dependency chains inspectable without reading the full analysis. Could become a criterion requiring synthesis column headers to name their source phases.
2. **Trajectory observable-signal specificity gate**: V-01–V-05 all require "at least one observable signal" in the Trajectory column. A future criterion could require the signal to include a timestamp or recency qualifier (e.g., "last two sprints," "prior 30 days") making trajectory directional claims falsifiable. Distinct from C-31 (directional label present): C-31 requires signal rationale; a C-33 candidate would require that signal to be temporally anchored.
