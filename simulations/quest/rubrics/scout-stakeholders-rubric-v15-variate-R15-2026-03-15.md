## Round 15 Variations — scout-stakeholders

**Target rubric**: v15 (max 245 pts)
**Baseline**: R14 V-05 (245/245 under v15 — first perfect score)
**Goal**: All five variations include C-37 + C-38 + C-39 (mandatory for 245/245). Explore three new structural axes as candidates for C-40/C-41/C-42 in v16.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Conflict escalation tier | Extending Step 1a with a named escalation owner + trigger when Resolution Authority misses Deadline adds a second auditable column absent from C-06; FAIL_NO_ESCALATION_PATH is a new gate distinct from FAIL_NO_RESOLUTION_PATHWAY |
| V-02 | Trajectory velocity prefill | Inserting a Step 3a prefill binding trajectory velocity to calibrated ACCELERATING/STABLE/DECELERATING bands before grid population mirrors the C-38 calibration pattern for the trajectory dimension; FAIL_UNCALIBRATED_VELOCITY is a new gate |
| V-03 | Synthesis coverage gate | Inserting Step 8b as a completeness audit table between the amendment phase and synthesis forces every grid stakeholder to appear in synthesis or be explicitly documented as omitted; FAIL_SYNTHESIS_GAP is a new gate distinct from FAIL_NO_SYNTHESIS |
| V-04 | V-01 + V-02 combined | Escalation tier and velocity prefill operate at different phases (Phase 1 vs Phase 3 grid pre-step); they are mutually non-interfering and both gate labels coexist |
| V-05 | V-01 + V-02 + V-03 combined | All three new axes simultaneously; maximum structural density for Round 15 discovery |

---

## V-01 — Conflict Escalation Tier

**Axis**: Step 1a extended with a named escalation owner and trigger condition when Resolution Authority misses Deadline.

**Hypothesis**: C-06 requires a conflict to have two named parties, a nature statement, and a Resolution Authority. It does not require an escalation path when Resolution Authority fails to close the conflict by Deadline. A conflict table with a Resolution Authority column satisfies C-06 regardless of whether a missed-deadline escalation path is defined. FAIL_NO_ESCALATION_PATH fires when any conflict row lacks a named escalation owner and trigger — a new gate label not satisfiable from C-06 alone.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: Org context state machine — PM role

Traverse the decision tree below. Emit exactly one terminal state label before any
Phase 1 output. Do not proceed past ORG-BLOCKED without an answer.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners; these are primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as a labeled line — e.g., `[STATE: ORG-RESOLVED-CODEOWNERS]` —
before Phase 1 begins. The label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts relevant to this feature decision. For each
conflict, populate one row of the resolution pathway table, then one row of the escalation
tier table.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name matching resolution row] | [named person or body above Resolution Authority] | [condition that activates escalation — e.g., "Deadline passed without ruling"] | [action taken by Escalation Owner] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.
FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with
a named Escalation Owner and a defined Escalation Trigger.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [can they recruit other resistors? yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] Escalation tier row present for each conflict (Escalation Owner + Trigger)
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [what this product explicitly does NOT provide for this segment] | [gatekeeper candidate / inertia candidate / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: the NOT-doing must address what the new approach does
  not preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.

---

### Step 4a: Probability band prefill — PM role

All Step 4b entries must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band
labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived
windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative and no risk documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here.
Rule 3: displacement-acknowledgment rows must address what the current approach preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned here.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish the permitted channel for each
Frame Type. Step 6b rows must use only the Primary Channel or Fallback Channel listed.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (meeting required; no fallback) |

Rule: Fallback may be used only when primary is explicitly unavailable. Document reason
in Message cell.

FAIL_WRONG_CHANNEL: any Step 6b row uses a channel not listed as Primary or Fallback for
its Frame Type.
FAIL_NO_CHANNEL: Channel column absent from Step 6b comms table.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing |
|----------|-------------|------------|---------|---------|--------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: channel not permitted for the assigned Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, escalation tier entries, trajectory assessments, engagement
window derivations, synthesis readout rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

After amendment pass, audit all `initial-inventory` Source rows — confirm or flag each.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-02 — Trajectory Velocity Prefill

**Axis**: Step 3a prefill defines trajectory velocity bands (ACCELERATING/STABLE/DECELERATING) with explicit criteria before the Phase 3 grid is populated. Each grid trajectory designation draws velocity from the prefill.

**Hypothesis**: The Phase 3 grid Trajectory column currently requires a directional label (ascending-toward-advocate / stable / descending-toward-risk) and an observable signal. Neither the trajectory criterion nor any existing criterion requires velocity to be drawn from a named-band prefill. A grid row can carry a trajectory label without any velocity annotation; and even if velocity is present, it can be free-form without violating any existing criterion. Step 3a mirrors the structure of Step 4a (C-38) but applies to trajectory velocity rather than veto probability. FAIL_UNCALIBRATED_VELOCITY is a new gate label distinct from FAIL_NO_TRAJECTORY.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: Org context state machine — PM role

Traverse the decision tree below. Emit exactly one terminal state label before any
Phase 1 output. Do not proceed past ORG-BLOCKED without an answer.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners; these are primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as a labeled line — e.g., `[STATE: ORG-RESOLVED-CODEOWNERS]` —
before Phase 1 begins. The label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [reason] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [what this product explicitly does NOT provide for this segment] | [gatekeeper candidate / inertia candidate / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: the NOT-doing must address what the new approach does
  not preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

All Phase 3 grid Trajectory entries must use exactly one Velocity label from this table.

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory is changing faster than baseline engagement cadence; new signals surfaced in last review cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change in engagement pattern since last review; signal consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid Trajectory entry omits Velocity label, or
uses a velocity designation not drawn from this prefill table.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

Velocity column must draw exclusively from Step 3a prefill labels.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.

---

### Step 4a: Probability band prefill — PM role

All Step 4b entries must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band
labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived
windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative and no risk documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here.
Rule 3: displacement-acknowledgment rows must address what the current approach preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned here.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish the permitted channel for each
Frame Type. Step 6b rows must use only the Primary Channel or Fallback Channel listed.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (meeting required; no fallback) |

Rule: Fallback may be used only when primary is explicitly unavailable. Document reason
in Message cell.

FAIL_WRONG_CHANNEL: any Step 6b row uses a channel not listed as Primary or Fallback for
its Frame Type.
FAIL_NO_CHANNEL: Channel column absent from Step 6b comms table.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing |
|----------|-------------|------------|---------|---------|--------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: channel not permitted for the assigned Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, trajectory assessments, velocity assessments, engagement
window derivations, synthesis readout rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

After amendment pass, audit all `initial-inventory` Source rows — confirm or flag each.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-03 — Synthesis Coverage Gate

**Axis**: Step 8b inserted between amendment phase and synthesis. Step 8b is a coverage audit table confirming every Phase 3 grid stakeholder has a corresponding synthesis row. FAIL_SYNTHESIS_GAP fires when any grid stakeholder is absent from the synthesis readout without documented justification in the Step 8b audit.

**Hypothesis**: C-32 requires the synthesis step to exist and to contain five required fields per row. It does not require a pre-synthesis audit confirming every grid stakeholder is represented. A synthesis step can satisfy C-32 by containing correctly attributed rows for a subset of grid stakeholders — C-32 does not fire if rows are present but incomplete in coverage. Step 8b makes coverage a structural obligation: every grid row must either appear in synthesis or be explicitly documented as omitted with a reason. FAIL_SYNTHESIS_GAP is a new gate label distinct from FAIL_NO_SYNTHESIS (C-32).

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: Org context state machine — PM role

Traverse the decision tree below. Emit exactly one terminal state label before any
Phase 1 output. Do not proceed past ORG-BLOCKED without an answer.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners; these are primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as a labeled line — e.g., `[STATE: ORG-RESOLVED-CODEOWNERS]` —
before Phase 1 begins. The label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [reason] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [what this product explicitly does NOT provide for this segment] | [gatekeeper candidate / inertia candidate / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: the NOT-doing must address what the new approach does
  not preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.

---

### Step 4a: Probability band prefill — PM role

All Step 4b entries must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band
labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived
windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative and no risk documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here.
Rule 3: displacement-acknowledgment rows must address what the current approach preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned here.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish the permitted channel for each
Frame Type. Step 6b rows must use only the Primary Channel or Fallback Channel listed.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (meeting required; no fallback) |

Rule: Fallback may be used only when primary is explicitly unavailable. Document reason
in Message cell.

FAIL_WRONG_CHANNEL: any Step 6b row uses a channel not listed as Primary or Fallback for
its Frame Type.
FAIL_NO_CHANNEL: Channel column absent from Step 6b comms table.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing |
|----------|-------------|------------|---------|---------|--------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: channel not permitted for the assigned Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, trajectory assessments, engagement window derivations,
synthesis readout rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

After amendment pass, audit all `initial-inventory` Source rows — confirm or flag each.

---

### Step 8b: Synthesis coverage audit — PM role

Before Step 9, confirm every Phase 3 grid stakeholder has a designated synthesis row.

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason — e.g., merged with row above, duplicate role] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from the Step 9 synthesis readout without
a documented justification in this table. FAIL_SYNTHESIS_GAP is distinct from
FAIL_NO_SYNTHESIS (which fires when the synthesis step itself is absent): FAIL_SYNTHESIS_GAP
fires when synthesis exists but silently omits a grid stakeholder.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.
All stakeholders listed in Step 8b as "Synthesis Row Planned: yes" must appear here.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.
FAIL_SYNTHESIS_GAP: any stakeholder from Step 8b coverage audit absent without documented
justification.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-04 — Conflict Escalation Tier + Trajectory Velocity Prefill

**Axis**: V-01 (conflict escalation tier) + V-02 (trajectory velocity prefill). All prior 39 criteria present.

**Hypothesis**: The escalation tier operates at Phase 1 (Step 1a extension) and the velocity prefill operates at Phase 3 (new Step 3a before grid population). They share no step overlap and do not compete for the same structural slot. FAIL_NO_ESCALATION_PATH and FAIL_UNCALIBRATED_VELOCITY are both present and independently auditable. Both new properties satisfy C-33 (parseable format) without ambiguity.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: Org context state machine — PM role

Traverse the decision tree below. Emit exactly one terminal state label before any
Phase 1 output. Do not proceed past ORG-BLOCKED without an answer.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners; these are primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as a labeled line — e.g., `[STATE: ORG-RESOLVED-CODEOWNERS]` —
before Phase 1 begins. The label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name matching resolution row] | [named person or body above Resolution Authority] | [condition activating escalation] | [action taken by Escalation Owner] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.
FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with
a named Escalation Owner and defined Escalation Trigger.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [reason] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] Escalation tier row present for each conflict (Escalation Owner + Trigger)
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [what this product explicitly does NOT provide for this segment] | [gatekeeper candidate / inertia candidate / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: the NOT-doing must address what the new approach does
  not preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

All Phase 3 grid Trajectory entries must include exactly one Velocity label from this table.

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals in last review cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; signal consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid Trajectory entry omits Velocity label, or
uses a velocity designation not drawn from this prefill table.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

Velocity column draws exclusively from Step 3a prefill labels.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.

---

### Step 4a: Probability band prefill — PM role

All Step 4b entries must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band
labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived
windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative and no risk documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here.
Rule 3: displacement-acknowledgment rows must address what the current approach preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned here.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish the permitted channel for each
Frame Type. Step 6b rows must use only the Primary Channel or Fallback Channel listed.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (meeting required; no fallback) |

Rule: Fallback may be used only when primary is explicitly unavailable. Document reason
in Message cell.

FAIL_WRONG_CHANNEL: any Step 6b row uses a channel not listed as Primary or Fallback for
its Frame Type.
FAIL_NO_CHANNEL: Channel column absent from Step 6b comms table.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing |
|----------|-------------|------------|---------|---------|--------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: channel not permitted for the assigned Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, escalation tier entries, trajectory assessments, velocity
assessments, engagement window derivations, synthesis readout rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

After amendment pass, audit all `initial-inventory` Source rows — confirm or flag each.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-05 — All Three New Axes Combined

**Axis**: V-01 (conflict escalation tier) + V-02 (trajectory velocity prefill) + V-03 (synthesis coverage gate). All prior 39 criteria present.

**Hypothesis**: All three new axes operate at non-overlapping steps: escalation tier at Step 1a (Phase 1), velocity prefill at Step 3a (Phase 3 pre-grid), coverage gate at Step 8b (post-amendment pre-synthesis). None interfere with each other or with any existing criterion. Three new gate labels (FAIL_NO_ESCALATION_PATH, FAIL_UNCALIBRATED_VELOCITY, FAIL_SYNTHESIS_GAP) all coexist with the existing 39-criterion set and with the three Round 14 gate labels (FAIL_WRONG_STATE, FAIL_UNCALIBRATED_PROBABILITY, FAIL_WRONG_CHANNEL). Maximum structural density for Round 15 discovery.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: Org context state machine — PM role

Traverse the decision tree below. Emit exactly one terminal state label before any
Phase 1 output. Do not proceed past ORG-BLOCKED without an answer.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners; these are primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as a labeled line — e.g., `[STATE: ORG-RESOLVED-CODEOWNERS]` —
before Phase 1 begins. The label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name matching resolution row] | [named person or body above Resolution Authority] | [condition activating escalation — e.g., "Deadline passed without ruling"] | [action taken by Escalation Owner] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.
FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with
a named Escalation Owner and defined Escalation Trigger.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [reason] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] Escalation tier row present for each conflict (Escalation Owner + Trigger)
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [what this product explicitly does NOT provide for this segment] | [gatekeeper candidate / inertia candidate / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: the NOT-doing must address what the new approach does
  not preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

All Phase 3 grid Trajectory entries must include exactly one Velocity label from this table.

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals surfaced in last review cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; signal consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid Trajectory entry omits Velocity label, or
uses a velocity designation not drawn from this prefill table.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

Velocity column draws exclusively from Step 3a prefill labels.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.

---

### Step 4a: Probability band prefill — PM role

All Step 4b entries must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band
labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived
windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative and no risk documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here.
Rule 3: displacement-acknowledgment rows must address what the current approach preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned here.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish the permitted channel for each
Frame Type. Step 6b rows must use only the Primary Channel or Fallback Channel listed.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (meeting required; no fallback) |

Rule: Fallback may be used only when primary is explicitly unavailable. Document reason
in Message cell.

FAIL_WRONG_CHANNEL: any Step 6b row uses a channel not listed as Primary or Fallback for
its Frame Type.
FAIL_NO_CHANNEL: Channel column absent from Step 6b comms table.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing |
|----------|-------------|------------|---------|---------|--------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: channel not permitted for the assigned Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, escalation tier entries, trajectory assessments, velocity
assessments, engagement window derivations, synthesis readout rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

After amendment pass, audit all `initial-inventory` Source rows — confirm or flag each.

---

### Step 8b: Synthesis coverage audit — PM role

Before Step 9, confirm every Phase 3 grid stakeholder has a designated synthesis row.

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason — e.g., merged with row above, duplicate role] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from the Step 9 synthesis readout without
a documented justification in this table. Distinct from FAIL_NO_SYNTHESIS: FAIL_NO_SYNTHESIS
fires when the synthesis step itself is absent; FAIL_SYNTHESIS_GAP fires when synthesis
exists but silently omits a grid stakeholder.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.
All stakeholders listed in Step 8b as "Synthesis Row Planned: yes" must appear here.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.
FAIL_SYNTHESIS_GAP: any stakeholder from Step 8b coverage audit absent without documented
justification.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## New gate labels introduced this round

| Label | Variation | Step | Distinct From |
|-------|-----------|------|---------------|
| FAIL_NO_ESCALATION_PATH | V-01, V-04, V-05 | Step 1a escalation tier | FAIL_NO_RESOLUTION_PATHWAY (C-06): existing label fires when resolution pathway fields are absent; FAIL_NO_ESCALATION_PATH fires when no escalation tier row exists for the conflict, independent of whether the resolution pathway is complete |
| FAIL_UNCALIBRATED_VELOCITY | V-02, V-04, V-05 | Step 3a / Phase 3 grid | FAIL_NO_TRAJECTORY: existing label fires when the Trajectory column is absent or a row has no direction; FAIL_UNCALIBRATED_VELOCITY fires when a Velocity label is absent or not drawn from the Step 3a prefill, independent of trajectory direction |
| FAIL_SYNTHESIS_GAP | V-03, V-05 | Step 8b / Step 9 | FAIL_NO_SYNTHESIS (C-32): existing label fires when the synthesis step itself is absent; FAIL_SYNTHESIS_GAP fires when synthesis exists but a grid stakeholder is silently omitted without a documented justification in the Step 8b coverage audit |

## Predicted scoring under v15

All five variations include C-37 (org state machine label integrity), C-38 (veto probability
calibration bands), and C-39 (comms channel binding) — necessary for 245/245 under v15.

New gate labels are candidates for C-40, C-41, C-42 in v16.

| Variation | Predicted v15 Score | New Gate Labels Present |
|-----------|---------------------|------------------------|
| V-01 | 245/245 | FAIL_NO_ESCALATION_PATH |
| V-02 | 245/245 | FAIL_UNCALIBRATED_VELOCITY |
| V-03 | 245/245 | FAIL_SYNTHESIS_GAP |
| V-04 | 245/245 | FAIL_NO_ESCALATION_PATH, FAIL_UNCALIBRATED_VELOCITY |
| V-05 | 245/245 | FAIL_NO_ESCALATION_PATH, FAIL_UNCALIBRATED_VELOCITY, FAIL_SYNTHESIS_GAP |
