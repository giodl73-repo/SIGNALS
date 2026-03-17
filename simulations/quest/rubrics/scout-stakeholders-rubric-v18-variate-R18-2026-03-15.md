## Round 18 Variations — scout-stakeholders

**Target rubric**: v18 (max 285 pts)
**Baseline**: R17 V-05 (285/285 under v18 — first perfect score; all three new criteria present)
**Goal**: All five variations include C-45 + C-46 + C-47 (mandatory for 285/285 under v18).
Explore three new single-axis structures as candidates for C-48/C-49/C-50 in v19.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format: comms priority band calibration | The comms table has timing anchors (C-25) but no scheduling-precedence gate. A Priority Band prefill (URGENT/STANDARD/DEFERRED) mirrors the C-38/C-41/C-44/C-45 calibration motif at the comms layer; FAIL_UNCALIBRATED_PRIORITY is a new gate distinct from FAIL_VAGUE_TIMING |
| V-02 | Lifecycle emphasis: amendment verification protocol | Step 8 requires one eligible update (C-23) but has no verification gate. A 3-column protocol (Target / Change Made / Verification) adds FAIL_UNVERIFIED_AMENDMENT, distinct from FAIL_OBSERVATION_ONLY: FAIL_OBSERVATION_ONLY fires when no target is updated; FAIL_UNVERIFIED_AMENDMENT fires when a target is updated but not confirmed |
| V-03 | Inertia framing: status-quo competitor inventory | Inertia treatment documents displaced stakeholders but never names the status-quo system as a competitor. Step 0b inventories each displaced workflow with Adoption Band (DOMINANT/ACTIVE/MARGINAL, prefill-calibrated), Switching Cost Band, and Coalition Capacity; FAIL_NO_COMPETITOR_ENTRY fires when an inertia stakeholder has no corresponding Step 0b entry |
| V-04 | V-01 + V-02 combined | Priority band calibration and amendment verification protocol operate at different phases (Step 6e vs Step 8); they are mutually non-interfering |
| V-05 | V-01 + V-02 + V-03 combined | All three new axes simultaneously; maximum structural density for Round 18 discovery |

---

## V-01 — Output Format: Comms Priority Band Calibration

**Axis**: Output format — adds Step 6e-priority (comms priority band prefill) and a Priority Band column to the Step 6b comms table. Priority Band values must be drawn exclusively from the Step 6e-priority prefill. Step 9 synthesis carries a Priority Band field with citation.

**Hypothesis**: The comms plan specifies timing anchors per row (C-25) but provides no mechanism for scheduling precedence when multiple rows fall within the same engagement window. A Priority Band prefill (URGENT/STANDARD/DEFERRED) with explicit scheduling criteria mirrors the calibration motif established by C-38 (veto probability), C-41 (trajectory velocity), C-44 (champion behavioral anchor), and C-45 (conflict severity) — but applies to the comms resource-sequencing layer rather than the analysis layer. FAIL_UNCALIBRATED_PRIORITY is a new gate distinct from FAIL_VAGUE_TIMING (C-25): FAIL_VAGUE_TIMING fires when a timing anchor is absent entirely; FAIL_UNCALIBRATED_PRIORITY fires when a timing anchor is present but no prefill-calibrated priority band governs scheduling precedence — a row can satisfy C-25 while failing FAIL_UNCALIBRATED_PRIORITY.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (UX) → Phase 2 (Strategy) → Phase 3 (PM). Do not begin conflict analysis
until Phase 1 is complete. Do not build the grid until Phase 2 is complete.

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

### Phase 1: User segment analysis — UX role

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

### Phase 1 → Phase 2 Transition Gate — UX role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration — Strategy role

Before identifying conflicts, establish the named severity bands that all Step 2a
conflict rows must draw from. Values outside this table are not permitted in the
Severity Band column.

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Conflict blocks the decision entirely or forces a restart if unresolved by deadline; no workaround exists | Escalation Owner must be activated before deadline; delay is not recoverable |
| SIGNIFICANT | Conflict delays the decision or degrades its quality if unresolved; a workaround exists but carries cost | Escalation Owner activated if deadline passes; cost must be documented |
| MANAGEABLE | Conflict resolves within normal process; timeline impact is unlikely even without escalation | No escalation activation required; monitor and confirm at next checkpoint |

FAIL_UNCALIBRATED_SEVERITY: any Step 2a conflict row carries a Severity Band value not
drawn from this prefill (e.g., free-form risk language, numeric rating, or ad hoc tier
not established here).

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Party anchor rule: Each Party A and Party B cell must either (a) match a segment name
from Phase 1 verbatim, or (b) carry an `[ORG-ROLE: description]` tag identifying an
org role not captured as a user segment.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named person or body] | [specific ruling needed] | [date or milestone] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name matching resolution row] | [named person or body above Resolution Authority] | [condition activating escalation — e.g., "Deadline passed without ruling"] | [action taken by Escalation Owner] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.
FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with
a named Escalation Owner and defined Escalation Trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: any Party A or Party B cell names a group that neither
matches a Phase 1 segment name nor carries an [ORG-ROLE: description] tag.
FAIL_UNCALIBRATED_SEVERITY: any Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

---

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two anchored parties, nature, calibrated
      severity band, complete resolution pathway entry, and escalation tier row
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

All Phase 3 grid Velocity column entries must draw exclusively from this table.

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals surfaced in last review cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; signal consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid row omits Velocity label or uses a velocity
designation not drawn from this prefill.

---

### Step 3b-prefill: Source typology — PM role

Before populating the Phase 3 grid, establish the epistemic typology labels that all
Source cells must carry. ASSUMED-annotated entries become mandatory Step 8 amendment
targets.

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed in meeting, document, or recorded interaction; citable artifact exists | None — confirm at Step 8 if signal is stale |
| INFERRED | Reasoned from pattern, role, or adjacent signal; not directly witnessed | Flag for validation at next stakeholder touchpoint |
| ASSUMED | No direct or adjacent evidence; based on role stereotype or default expectation | Mandatory Step 8 amendment target — must be confirmed or corrected before synthesis |

Each Source cell in the Phase 3 grid must carry exactly one typology label from this
table in the format: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Phase 3 grid Source cell is present and populated but does
not carry a typology label from this prefill.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [observable signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | [INERTIA] if applicable |

Source column format: `[TYPOLOGY: source description]` where TYPOLOGY is drawn from
Step 3b-prefill. ASSUMED entries are designated mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source entry.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.
FAIL_UNANNOTATED_SOURCE: any Source cell lacks typology label from Step 3b-prefill.

---

### Step 4a: Veto probability band prefill — PM role

All Step 4b entries must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a probability value not drawn from
these band labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence if veto exercised] | [mitigation strategy] |

FAIL_WRONG_ORDER: entries not ordered HIGH → MED → LOW.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not drawn from Step 4a prefill.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column with derived values.
Step 6b timing anchors must fall within derived engagement windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not populated in grid.

---

### Step 5b: Champion identification — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing in org] | [specific calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

All Step 5c dimension scores must draw from this table. Cite the level number in the
Evidence cell.

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority over this decision | No direct contact channel; communications routed through intermediaries | No documented statement of support |
| 1 | Advisory influence; can surface concerns but cannot advance or close | Occasional touchpoint; not in regular decision loop | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant or sponsor; can advance or delay but not close unilaterally | In regular decision loop; direct async channel established | Documented commitment with schedulable action and named owner |
| 3 | Final decision authority or veto power; can block, advance, or close unilaterally | Peer-level relationship; synchronous channel available on request | Committed with deadline, named accountability, and contingency if unavailable |

FAIL_UNANCHORED_SCORE: any Step 5c dimension score is outside 0–3, or the Evidence cell
does not cite a level from this prefill table.

---

### Step 5c: Champion depth scoring — PM role

Scores must be drawn from the Step 5b-anchor prefill. Composite gate: >= 6 (max 9).

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [behavioral evidence matching that level] |
| Proximity | [0–3] | level [N]: [behavioral evidence matching that level] |
| Commitment | [0–3] | level [N]: [behavioral evidence matching that level] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative champion identified and
no risk documented.
FAIL_UNANCHORED_SCORE: any score outside 0–3 or Evidence cell does not cite a level from
Step 5b-anchor prefill.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor identified, or single-point-of-failure risk noted] |
| Deterioration signal 1 | [observable trigger indicating champion disengagement] |
| Deterioration signal 2 | [observable trigger indicating champion disengagement] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill and assignment — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

Rule 1: Each Step 6b row must use a Frame Type drawn exclusively from this table.
Rule 2: `displacement-acknowledgment` is mandatory for every inertia-tagged stakeholder.
Rule 3: `displacement-acknowledgment` messages must address what the current approach
preserves before describing the new approach.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this step.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish permitted channels per Frame Type.
Step 6b rows must draw Channel values exclusively from this binding.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback; meeting required) |

Fallback may be used only when primary is explicitly unavailable. Document reason in
Message cell.

FAIL_NO_CHANNEL: Channel column absent from the comms table.
FAIL_WRONG_CHANNEL: any row uses a channel not listed as Primary or Fallback for its
Frame Type.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows. Priority Band column draws exclusively
from Step 6e-priority prefill.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current approach first; transition second] | [relative anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: any row uses a channel not permitted for its Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

For each inertia-tagged stakeholder, audit the full comms sequence to verify the
displacement-acknowledgment row carries the T+0 baseline — the earliest timing anchor
in that stakeholder's comms sequence.

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor from Step 6b row] | [row1: anchor; row2: anchor; ...] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: any inertia-tagged stakeholder's displacement-acknowledgment
row does not carry the T+0 baseline timing anchor (i.e., another comms row for that
stakeholder is anchored earlier while the displacement row is assigned a later anchor).
Distinct from FAIL_VAGUE_TIMING (C-25) and FAIL_DISPLACEMENT_TIMING (C-29): both anchors
must be present and specific before FAIL_COMMS_SEQUENCE_VIOLATION is assessable.

---

### Step 6e-priority: Comms priority band prefill — PM role

Before finalizing the communication table, establish the priority bands governing
scheduling precedence when multiple comms rows fall within the same engagement window.
All Step 6b Priority Band cells must draw values exclusively from this prefill.

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Engagement window closes within the current sprint cycle; any delay risks losing the window entirely | Owner must schedule within 48 hours of plan publication |
| STANDARD | Engagement window extends beyond the current sprint; preferred timing is within 1–2 cycles | Owner schedules at next available touchpoint within window |
| DEFERRED | Stakeholder window carries no forcing function; timing is fully opportunistic | Owner documents intended timing; no hard scheduling obligation |

When multiple comms rows share an engagement window, schedule in this order: URGENT
first, then STANDARD, then DEFERRED.

FAIL_UNCALIBRATED_PRIORITY: any Step 6b comms row carries a Priority Band value not
drawn from this prefill (e.g., numeric ranking, free-form urgency language, or ad hoc
tier not established in this prefill). Distinct from FAIL_VAGUE_TIMING (C-25):
FAIL_VAGUE_TIMING fires when a timing anchor is absent; FAIL_UNCALIBRATED_PRIORITY fires
when a timing anchor is present but no calibrated priority band governs scheduling
precedence within the engagement window.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing a comms row, blocking reason, or
timing that violates the Step 2c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible targets: Phase 3 grid rows, Step 4b veto
entries, Step 6a frame type assignments, Step 6b comms rows, Step 6e-priority priority
band assignments, Step 2c gatekeeper lead-time tags, Step 2a conflict resolution pathway
entries, Step 2a escalation tier entries, trajectory assessments, velocity assessments,
engagement window derivations, champion depth scores (with updated anchor citations),
synthesis readout rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

Mandatory ASSUMED amendment obligation: All Source cells annotated ASSUMED in the Phase 3
grid are mandatory targets. Each must be either (a) upgraded to OBSERVED or INFERRED with
a citable artifact or reasoning, or (b) explicitly flagged as unresolved with a named
next-step and owner. An ASSUMED entry that receives no amendment action in this step =
FAIL_OBSERVATION_ONLY for that entry.

---

### Step 8b: Synthesis coverage audit — PM role

Before Step 9, confirm every Phase 3 grid stakeholder has a designated synthesis row.

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason — e.g., merged with row above, duplicate role] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from the Step 9 synthesis readout without
a documented justification in this table.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. All stakeholders listed in Step 8b as "Synthesis Row
Planned: yes" must appear. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without documented justification.
```

---

## V-02 — Lifecycle Emphasis: Amendment Verification Protocol

**Axis**: Lifecycle emphasis — Step 8 expanded from a single-row amendment log to a
structured 3-column protocol (Amendment Target | Change Made | Verification). Each
amendment must include a Verification cell confirming the structural artifact was updated,
not merely identified. ASSUMED-annotated Source entries remain mandatory targets.

**Hypothesis**: The current amendment phase (FAIL_OBSERVATION_ONLY) fires only when no
eligible structural target is updated at all. No gate exists for the case where a target
is identified and a change is documented in prose, but no verification step confirms the
artifact was actually modified. A 3-column protocol (Target / Change Made / Verification)
mirrors the structural completeness pattern from C-06 (Authority + Decision + Deadline)
and C-07 (Gatekeeper + Blocking Reason + Lead Time). FAIL_UNVERIFIED_AMENDMENT is a new
gate distinct from FAIL_OBSERVATION_ONLY: FAIL_OBSERVATION_ONLY fires when the Change
Made cell is absent (no update applied); FAIL_UNVERIFIED_AMENDMENT fires when a Change
Made cell is populated but the Verification cell is absent or states "not-yet" without a
documented reason and assigned next action — a verification obligation orthogonal to
whether the change was applied.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (UX) → Phase 2 (Strategy) → Phase 3 (PM). Do not begin conflict analysis
until Phase 1 is complete. Do not build the grid until Phase 2 is complete.

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

### Phase 1: User segment analysis — UX role

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

### Phase 1 → Phase 2 Transition Gate — UX role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration — Strategy role

Before identifying conflicts, establish the named severity bands that all Step 2a
conflict rows must draw from. Values outside this table are not permitted in the
Severity Band column.

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Conflict blocks the decision entirely or forces a restart if unresolved by deadline; no workaround exists | Escalation Owner must be activated before deadline |
| SIGNIFICANT | Conflict delays the decision or degrades quality if unresolved; workaround exists but carries cost | Escalation Owner activated if deadline passes |
| MANAGEABLE | Conflict resolves within normal process; timeline impact is unlikely without escalation | No escalation activation required |

FAIL_UNCALIBRATED_SEVERITY: any Step 2a conflict row carries a Severity Band value not
drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Party anchor rule: Each Party A and Party B cell must either (a) match a segment name
from Phase 1 verbatim, or (b) carry an `[ORG-ROLE: description]` tag.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named person or body] | [specific ruling needed] | [date or milestone] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name matching resolution row] | [named person or body above Resolution Authority] | [condition activating escalation] | [action taken by Escalation Owner] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.
FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with
a named Escalation Owner and defined Escalation Trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: any Party A or Party B cell names a group that neither
matches a Phase 1 segment name nor carries an [ORG-ROLE: description] tag.
FAIL_UNCALIBRATED_SEVERITY: any Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

---

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two anchored parties, calibrated severity
      band, complete resolution pathway, and escalation tier row
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

All Phase 3 grid Velocity column entries must draw exclusively from this table.

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals in last cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; signal consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid row omits Velocity label or uses a
designation not drawn from this prefill.

---

### Step 3b-prefill: Source typology — PM role

Before populating the Phase 3 grid, establish the epistemic typology labels that all
Source cells must carry. ASSUMED-annotated entries become mandatory Step 8 amendment
targets.

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed in meeting, document, or recorded interaction; citable artifact exists | None — confirm at Step 8 if stale |
| INFERRED | Reasoned from pattern, role, or adjacent signal; not directly witnessed | Flag for validation at next touchpoint |
| ASSUMED | No direct or adjacent evidence; based on role stereotype or default expectation | Mandatory Step 8 amendment target |

Each Source cell in the Phase 3 grid must carry exactly one typology label from this
table in the format: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Phase 3 grid Source cell is present and populated but does
not carry a typology label from this prefill.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [observable signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | [INERTIA] if applicable |

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source entry.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.
FAIL_UNANNOTATED_SOURCE: any Source cell lacks typology label from Step 3b-prefill.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a probability value not drawn from
these band labels.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH bands first, then MED, then LOW; within band by judgment.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence if veto exercised] | [mitigation strategy] |

FAIL_WRONG_ORDER: entries not ordered HIGH → MED → LOW.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not drawn from Step 4a prefill.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not populated in grid.

---

### Step 5b: Champion identification — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing in org] | [specific calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority over this decision | No direct contact channel; communications routed through intermediaries | No documented statement of support |
| 1 | Advisory influence; can surface concerns but cannot advance or close | Occasional touchpoint; not in regular decision loop | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant or sponsor; can advance or delay but not close unilaterally | In regular decision loop; direct async channel established | Documented commitment with schedulable action and named owner |
| 3 | Final decision authority or veto power; can block, advance, or close unilaterally | Peer-level relationship; synchronous channel available on request | Committed with deadline, named accountability, and contingency if unavailable |

FAIL_UNANCHORED_SCORE: any Step 5c dimension score is outside 0–3, or the Evidence cell
does not cite a level from this prefill table.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [behavioral evidence] |
| Proximity | [0–3] | level [N]: [behavioral evidence] |
| Commitment | [0–3] | level [N]: [behavioral evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative and no risk documented.
FAIL_UNANCHORED_SCORE: any score outside 0–3 or Evidence cell missing Step 5b-anchor citation.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor identified, or single-point-of-failure risk noted] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill and assignment — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

Rule 1: Each Step 6b row must use a Frame Type drawn exclusively from this table.
Rule 2: `displacement-acknowledgment` is mandatory for every inertia-tagged stakeholder.
Rule 3: `displacement-acknowledgment` messages must address what the current approach
preserves before describing the new approach.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this step.

---

### Step 6c: Channel binding prefill — PM role

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback; meeting required) |

FAIL_NO_CHANNEL: Channel column absent from the comms table.
FAIL_WRONG_CHANNEL: any row uses a channel not listed as Primary or Fallback for its
Frame Type.

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
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current approach first; transition second] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: any row uses a channel not permitted for its Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

For each inertia-tagged stakeholder, audit the full comms sequence to verify the
displacement-acknowledgment row carries the T+0 baseline — the earliest timing anchor
in that stakeholder's sequence.

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor from Step 6b] | [row1: anchor; row2: anchor; ...] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: any inertia-tagged stakeholder's displacement-acknowledgment
row does not carry the T+0 baseline timing anchor.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing a comms row, blocking reason, or
timing that violates the Step 2c lead time.

---

### Step 8: Amendment protocol — PM role

For each amendment, populate one row in the amendment table. The protocol requires three
cells per row: Amendment Target (what structural artifact to update), Change Made (the
exact update applied), and Verification (confirmation that the artifact was updated).

| # | Amendment Target | Change Made | Verification |
|---|-----------------|-------------|--------------|
| 1 | [grid row / veto entry / comms row / conflict pathway / escalation entry / trajectory / velocity / engagement window / champion score / synthesis row] | [exact change — e.g., "Source annotation upgraded from ASSUMED to OBSERVED; artifact: meeting notes 2026-03-15"] | confirmed: [artifact reference + date] / not-yet: [reason + assigned owner + deadline] |

Mandatory ASSUMED amendment obligation: All Source cells annotated ASSUMED in the Phase 3
grid are mandatory targets. Each must appear as a row in this table.

FAIL_OBSERVATION_ONLY: any amendment row is missing the Change Made cell (finding noted
without an update applied).
FAIL_UNVERIFIED_AMENDMENT: any amendment row has a Change Made cell populated but the
Verification cell is absent or states "not-yet" without a documented reason and an
assigned owner with a deadline. Distinct from FAIL_OBSERVATION_ONLY: FAIL_OBSERVATION_ONLY
fires when no structural update is documented at all; FAIL_UNVERIFIED_AMENDMENT fires when
a Change Made cell is present and populated, but no confirmation step verifies the
artifact was actually updated — a row can fail FAIL_UNVERIFIED_AMENDMENT without
triggering FAIL_OBSERVATION_ONLY.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from the Step 9 synthesis readout without
a documented justification in this table.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without documented justification.
```

---

## V-03 — Inertia Framing: Status-Quo Competitor Inventory

**Axis**: Inertia framing — Step 0b is inserted after Step 0 (before Phase 1), requiring
each displaced workflow or tool to be inventoried as a named "competitor" with three
prefill-calibrated fields: Adoption Band (DOMINANT/ACTIVE/MARGINAL), Switching Cost Band
(HIGH/MEDIUM/LOW), and Coalition Capacity. Every inertia stakeholder in Step 2b must
reference one Step 0b competitor entry by name. FAIL_NO_COMPETITOR_ENTRY fires when an
inertia stakeholder has no corresponding Step 0b entry.

**Hypothesis**: The current inertia treatment (Step 2b) identifies displaced stakeholder
groups but never names the status-quo system or approach they are invested in as a
first-class entity. Without an inventory of the competitor, there is no calibration gate
on adoption scale or switching cost — two of the primary drivers of inertia intensity.
Adding Step 0b with prefill-calibrated Adoption Band and Switching Cost Band mirrors the
calibration motif from C-38/C-41/C-44/C-45 but applies it to the pre-Phase-1 competitor
layer. FAIL_NO_COMPETITOR_ENTRY is distinct from FAIL_NO_INERTIA (C-11): FAIL_NO_INERTIA
fires when inertia stakeholders are not identified at all; FAIL_NO_COMPETITOR_ENTRY fires
when inertia stakeholders are identified (C-11 PASS) but the status-quo approach they
champion is not inventoried in Step 0b with Adoption Band, Switching Cost Band, and
Coalition Capacity — an obligation orthogonal to stakeholder identification.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Step 0 (org context) → Step 0b (competitor inventory) → Phase 1 (UX) → Phase 2
(Strategy) → Phase 3 (PM). Do not begin Phase 1 until Step 0b is complete.

---

### Step 0: Org context state machine — PM role

Traverse the decision tree below. Emit exactly one terminal state label before Step 0b.
Do not proceed past ORG-BLOCKED without an answer.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners; these are primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as a labeled line — e.g., `[STATE: ORG-RESOLVED-CODEOWNERS]` —
before Step 0b begins. The label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Before Phase 1, identify each existing workflow, tool, or approach that this feature
will displace. These are the status-quo "competitors" of adoption. Each competitor entry
must carry an Adoption Band and a Switching Cost Band drawn exclusively from the prefills
below.

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | Used by the majority of the target group as the default; no significant parallel alternative exists |
| ACTIVE | Used by a significant minority; a parallel alternative exists but this remains the preferred path for its users |
| MARGINAL | Used by a small fraction; parallel alternatives are common; adoption is fragmented or role-specific |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Switching requires data migration, retraining, workflow redesign, or integration changes; timeline impact > 1 sprint |
| MEDIUM | Switching requires process adjustment and targeted communication but no structural rework; timeline impact <= 1 sprint |
| LOW | Switching is transparent or easily reversible; no significant workflow adjustment required |

Competitor inventory table:

| Competitor | Description | Adoption Band | Switching Cost Band | Coalition Capacity |
|------------|-------------|---------------|--------------------|--------------------|
| [name of existing workflow / tool / approach] | [what it does; who relies on it] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW | [yes: organized user base / limited: scattered advocates / no: no identified group] |

Every inertia stakeholder identified in Step 2b must reference one competitor entry from
this table by name (Competitor column). FAIL_NO_COMPETITOR_ENTRY fires when a Step 2b
inertia stakeholder is not traceable to a Step 0b competitor entry.

---

### Phase 1: User segment analysis — UX role

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

### Phase 1 → Phase 2 Transition Gate — UX role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration — Strategy role

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Conflict blocks the decision entirely or forces a restart if unresolved by deadline; no workaround exists | Escalation Owner must be activated before deadline |
| SIGNIFICANT | Conflict delays the decision or degrades quality if unresolved; workaround exists but carries cost | Escalation Owner activated if deadline passes |
| MANAGEABLE | Conflict resolves within normal process; timeline impact is unlikely without escalation | No escalation activation required |

FAIL_UNCALIBRATED_SEVERITY: any Step 2a conflict row carries a Severity Band value not
drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Party anchor rule: Each Party A and Party B cell must either (a) match a segment name
from Phase 1 verbatim, or (b) carry an `[ORG-ROLE: description]` tag.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named person or body] | [specific ruling needed] | [date or milestone] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person or body above Resolution Authority] | [condition activating escalation] | [action taken] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.
FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with
Escalation Owner and Escalation Trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: any Party A or Party B neither matches a Phase 1 segment
name nor carries an [ORG-ROLE: description] tag.
FAIL_UNCALIBRATED_SEVERITY: any Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

Each inertia stakeholder must reference one competitor entry from Step 0b by name.

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|--------------------|--------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] | [Competitor name from Step 0b] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.
FAIL_NO_COMPETITOR_ENTRY: any Step 2b inertia stakeholder carries a Step 0b Competitor
cell that is blank or names a workflow not present in the Step 0b inventory table.
Distinct from FAIL_NO_INERTIA: FAIL_NO_INERTIA fires when inertia stakeholders are absent;
FAIL_NO_COMPETITOR_ENTRY fires when inertia stakeholders exist but the status-quo approach
they champion is not in the Step 0b inventory.

---

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two anchored parties, calibrated severity
      band, complete resolution pathway, and escalation tier row
- [ ] At least one inertia stakeholder with Step 0b competitor reference (or explicit
      no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals in last cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; signal consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid row omits Velocity label or uses a
designation not drawn from this prefill.

---

### Step 3b-prefill: Source typology — PM role

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed in meeting, document, or recorded interaction; citable artifact exists | None — confirm at Step 8 if stale |
| INFERRED | Reasoned from pattern, role, or adjacent signal; not directly witnessed | Flag for validation at next touchpoint |
| ASSUMED | No direct or adjacent evidence; based on role stereotype or default expectation | Mandatory Step 8 amendment target |

Each Source cell in the Phase 3 grid must carry exactly one typology label in the format:
`[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Phase 3 grid Source cell is present and populated but does
not carry a typology label from this prefill.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: description] | [INERTIA] if applicable |

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source entry.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.
FAIL_UNANNOTATED_SOURCE: any Source cell lacks typology label from Step 3b-prefill.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a value not from these band labels.

---

### Step 4b: Veto risk ranking — PM role

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence if veto exercised] | [mitigation strategy] |

FAIL_WRONG_ORDER: entries not ordered HIGH → MED → LOW.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band not drawn from Step 4a prefill.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not populated in grid.

---

### Step 5b: Champion identification — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing in org] | [specific calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority over this decision | No direct contact channel; communications routed through intermediaries | No documented statement of support |
| 1 | Advisory influence; can surface concerns but cannot advance or close | Occasional touchpoint; not in regular decision loop | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant or sponsor; can advance or delay but not close unilaterally | In regular decision loop; direct async channel established | Documented commitment with schedulable action and named owner |
| 3 | Final decision authority or veto power; can block, advance, or close unilaterally | Peer-level relationship; synchronous channel available on request | Committed with deadline, named accountability, and contingency if unavailable |

FAIL_UNANCHORED_SCORE: any Step 5c dimension score is outside 0–3, or the Evidence cell
does not cite a level from this prefill table.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [behavioral evidence] |
| Proximity | [0–3] | level [N]: [behavioral evidence] |
| Commitment | [0–3] | level [N]: [behavioral evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative and no risk documented.
FAIL_UNANCHORED_SCORE: any score outside 0–3 or Evidence cell missing Step 5b-anchor citation.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor identified, or single-point-of-failure risk noted] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill and assignment — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

Rule 1: Each Step 6b row must use a Frame Type drawn exclusively from this table.
Rule 2: `displacement-acknowledgment` is mandatory for every inertia-tagged stakeholder.
Rule 3: `displacement-acknowledgment` messages must address what the current approach
preserves before describing the new approach.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this step.

---

### Step 6c: Channel binding prefill — PM role

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback; meeting required) |

FAIL_NO_CHANNEL: Channel column absent from the comms table.
FAIL_WRONG_CHANNEL: any row uses a channel not listed for its Frame Type.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing |
|----------|-------------|------------|---------|---------|--------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current approach first; competitor name from Step 0b referenced in message] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: any row uses a channel not permitted for its Frame Type.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor from Step 6b] | [row1: anchor; row2: anchor; ...] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: any inertia-tagged stakeholder's displacement-acknowledgment
row does not carry the T+0 baseline timing anchor.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates the Step 2c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible targets: Phase 3 grid rows, Step 4b veto
entries, Step 6a frame type assignments, Step 6b comms rows, Step 2c gatekeeper lead-time
tags, Step 2a conflict resolution pathway entries, Step 2a escalation tier entries,
trajectory assessments, velocity assessments, engagement window derivations, champion
depth scores, synthesis readout rows, Step 0b competitor inventory entries.

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.

Mandatory ASSUMED amendment obligation: All Source cells annotated ASSUMED in Phase 3
are mandatory targets. Each must be upgraded or explicitly flagged with next-step and owner.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from Step 9 without documented justification.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | competitor: [Step 0b name or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without documented justification.
```

---

## V-04 — V-01 + V-02 Combined

**Axes combined**: Output format (comms priority band) + Lifecycle emphasis (amendment
verification protocol). Priority band calibration operates at Step 6e (comms layer);
amendment verification protocol operates at Step 8. They are structurally non-interfering:
FAIL_UNCALIBRATED_PRIORITY fires at the comms table; FAIL_UNVERIFIED_AMENDMENT fires at
the amendment table. Both can be satisfied independently.

**Hypothesis**: V-01 and V-02 address different lifecycle phases and different failure
modes. Their combination tests whether the two new gates are mutually satisfiable — a
complete prompt that passes all v18 criteria while also satisfying both Step 6e-priority
calibration and Step 8 verification protocol should be achievable without tradeoffs.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (UX) → Phase 2 (Strategy) → Phase 3 (PM). Do not begin conflict analysis
until Phase 1 is complete. Do not build the grid until Phase 2 is complete.

---

### Step 0: Org context state machine — PM role

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS file present at repository root | Extract teams named as owners | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output the terminal state as `[STATE: ...]` before Phase 1 begins.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [what this product explicitly does NOT do for this segment] | [gatekeeper candidate / inertia candidate / neither] |

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 1 → Phase 2 Transition Gate

- [ ] At least two distinct segments; NOT-doing present for each; inertia displacement
      NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE1: any required output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision entirely or forces restart; no workaround | Escalation Owner activated before deadline |
| SIGNIFICANT | Delays or degrades quality; workaround exists but costly | Escalation Owner activated if deadline passes |
| MANAGEABLE | Resolves in normal process; timeline impact unlikely | No escalation activation required |

FAIL_UNCALIBRATED_SEVERITY: any conflict row Severity Band not drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named person or body] | [specific ruling] | [date or milestone] |

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [person or body above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY: conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: missing Resolution Authority, Decision Required, or Deadline.
FAIL_NO_ESCALATION_PATH: no escalation tier row with Escalation Owner and Trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: party neither matches Phase 1 segment nor carries
[ORG-ROLE: description] tag.
FAIL_UNCALIBRATED_SEVERITY: Severity Band not from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name] | [disrupted activity] | [replaced approach] | [yes / limited / no] |

FAIL_NO_INERTIA: no inertia stakeholders when feature displaces existing workflow.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [type of sign-off] | [advance notice required] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 2 → Phase 3 Transition Gate

- [ ] Two conflicts with anchored parties, calibrated severity band, resolution pathway,
      escalation tier; inertia stakeholder or no-displacement statement; gatekeeper with lead time

FAIL_INCOMPLETE_PHASE2: any required output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory faster than baseline cadence; new signals in last cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Attendance at expected touchpoints |
| DECELERATING | Engagement thinning; fewer signals than prior cycle | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: any grid row Velocity not from this prefill.

---

### Step 3b-prefill: Source typology

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact exists | None |
| INFERRED | Reasoned from pattern or adjacent signal | Flag for validation |
| ASSUMED | No direct evidence; role stereotype or default | Mandatory Step 8 amendment target |

Source cell format: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Source cell present but lacking typology label.

---

### Phase 3: Power/Interest grid

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD] | [TYPOLOGY: description] | [INERTIA] if applicable |

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE: as defined at their respective steps.

---

### Step 4a: Veto probability band prefill

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto |
| MED | 30–70% | Conditional veto |
| LOW | < 30% | Unlikely veto |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b value not from these labels.

---

### Step 4b: Veto risk ranking

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [strategy] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY as defined.

---

### Step 5a: Engagement window derivation

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW: window not derived or not populated in grid.

---

### Step 5b: Champion identification

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory only | Occasional touchpoint | Verbal interest only |
| 2 | Named decision participant | In regular decision loop | Documented commitment with named owner |
| 3 | Final authority or veto | Peer-level; synchronous channel on request | Committed with deadline and contingency |

FAIL_UNANCHORED_SCORE: score outside 0–3 or Evidence cell missing level citation.

---

### Step 5c: Champion depth scoring

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE as defined.

---

### Step 5d: Champion durability

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals.

---

### Step 6a: Frame Type prefill and assignment

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned here.

---

### Step 6c: Channel binding prefill

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback) |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL as defined.

---

### Step 6b: Communication strategy per quadrant

Priority Band column draws exclusively from Step 6e-priority prefill.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL as defined.

---

### Step 6d-sequence: Displacement comms sequence audit

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor] | [other row timings] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment row not T+0 baseline.

---

### Step 6e-priority: Comms priority band prefill

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint; delay loses the window | Schedule within 48h of plan publication |
| STANDARD | Window extends beyond current sprint; preferred within 1–2 cycles | Schedule at next touchpoint within window |
| DEFERRED | No forcing function; fully opportunistic | Document intended timing; no hard obligation |

FAIL_UNCALIBRATED_PRIORITY: any Step 6b comms row Priority Band not drawn from this
prefill. Distinct from FAIL_VAGUE_TIMING: FAIL_VAGUE_TIMING fires when timing anchor is
absent; FAIL_UNCALIBRATED_PRIORITY fires when timing is present but scheduling precedence
is not governed by a calibrated priority band.

---

### Step 7: Gatekeeper completeness check

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: gatekeeper missing comms row, blocking reason, or lead time
violation.

---

### Step 8: Amendment protocol

For each amendment, populate one row with three required cells.

| # | Amendment Target | Change Made | Verification |
|---|-----------------|-------------|--------------|
| 1 | [structural artifact — grid row / veto entry / comms row / conflict pathway / escalation tier / trajectory / velocity / window / champion score / synthesis row] | [exact update applied] | confirmed: [artifact + date] / not-yet: [reason + owner + deadline] |

Mandatory ASSUMED obligation: All ASSUMED-annotated Source cells are mandatory targets.
Each must be upgraded or flagged with owner and deadline.

FAIL_OBSERVATION_ONLY: Change Made cell absent (finding noted without update).
FAIL_UNVERIFIED_AMENDMENT: Change Made cell populated but Verification cell absent or
"not-yet" without documented reason and assigned owner. Distinct from FAIL_OBSERVATION_ONLY:
FAIL_OBSERVATION_ONLY fires when no update is documented; FAIL_UNVERIFIED_AMENDMENT fires
when an update is documented but confirmation of artifact modification is missing.

---

### Step 8b: Synthesis coverage audit

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes | — |
| [name] | no | [reason] |

FAIL_SYNTHESIS_GAP: stakeholder absent from Step 9 without justification.

---

### Step 9: Cross-phase synthesis readout

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [score/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP as defined.
```

---

## V-05 — V-01 + V-02 + V-03 Combined

**Axes combined**: Output format (comms priority band) + Lifecycle emphasis (amendment
verification protocol) + Inertia framing (status-quo competitor inventory). Maximum
structural density for Round 18. Step 0b, Step 6e-priority, and the 3-column Step 8
protocol coexist without interference: Step 0b operates pre-Phase 1, Step 6e-priority
operates at the comms layer, Step 8 verification protocol operates at the amendment layer.
All three new gate candidates (FAIL_UNCALIBRATED_PRIORITY, FAIL_UNVERIFIED_AMENDMENT,
FAIL_NO_COMPETITOR_ENTRY) are simultaneously satisfiable.

```
FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
Prose annotations are permitted alongside structural outputs but do not replace them.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Step 0 → Step 0b → Phase 1 (UX) → Phase 2 (Strategy) → Phase 3 (PM).

---

### Step 0: Org context state machine — PM role

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS present | Extract owner teams | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation has org identifiers | Extract from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither sufficient | Ask: "What org or team is this decision for?" Halt | ORG-BLOCKED |

Output `[STATE: ...]` before Step 0b begins.

FAIL_SILENT_INFERENCE: no label emitted or analysis proceeds without resolution.
FAIL_WRONG_STATE: label does not match branch actually taken.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | Used by majority as default; no significant parallel alternative |
| ACTIVE | Used by significant minority; parallel alternative exists but this is preferred |
| MARGINAL | Used by small fraction; parallel alternatives common; adoption is fragmented |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Requires migration, retraining, workflow redesign, or integration changes; > 1 sprint |
| MEDIUM | Requires process adjustment and targeted communication; <= 1 sprint |
| LOW | Transparent or easily reversible; no significant adjustment required |

Competitor inventory:

| Competitor | Description | Adoption Band | Switching Cost Band | Coalition Capacity |
|------------|-------------|---------------|--------------------|--------------------|
| [workflow / tool / approach being displaced] | [what it does; who relies on it] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW | [yes / limited / no] |

Every inertia stakeholder in Step 2b must reference one competitor entry by name.

FAIL_NO_COMPETITOR_ENTRY: any Step 2b inertia stakeholder is not traceable to a Step 0b
competitor entry. Distinct from FAIL_NO_INERTIA: FAIL_NO_INERTIA fires when inertia
stakeholders are absent; FAIL_NO_COMPETITOR_ENTRY fires when inertia stakeholders exist
but the status-quo approach they champion is not inventoried with Adoption Band, Switching
Cost Band, and Coalition Capacity.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [explicit NOT-doing for this segment] | [gatekeeper candidate / inertia candidate / neither] |

FAIL_MONOLITH_ASSUMPTION: all users treated as a single segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 1 → Phase 2 Transition Gate

- [ ] At least two segments with NOT-doing; inertia displacement NOT-doing addressed

FAIL_INCOMPLETE_PHASE1: required output absent.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision entirely; no workaround | Activate Escalation Owner before deadline |
| SIGNIFICANT | Delays or degrades quality; workaround exists | Activate if deadline passes |
| MANAGEABLE | Resolves in normal process; low timeline risk | No activation required |

FAIL_UNCALIBRATED_SEVERITY: any conflict row Severity Band not drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named person or body] | [specific ruling] | [date or milestone] |

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [person or body above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY as defined at their steps.

---

#### Step 2b: Inertia stakeholder mapping

Each row must reference one Step 0b competitor entry.

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|--------------------|--------------------|
| [name] | [disrupted activity] | [replaced by] | [yes / limited / no] | [Competitor name from Step 0b] |

FAIL_NO_INERTIA: no inertia stakeholders when feature displaces existing workflow.
FAIL_NO_COMPETITOR_ENTRY: any inertia stakeholder references a competitor not in Step 0b.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [sign-off type] | [advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 2 → Phase 3 Transition Gate

- [ ] Two conflicts with anchored parties, calibrated severity, resolution pathway,
      escalation tier; inertia stakeholder with Step 0b reference; gatekeeper with lead time

FAIL_INCOMPLETE_PHASE2: required output absent.

---

### Step 3a: Trajectory velocity band prefill

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Faster than baseline; new signals last cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change; consistent signal | Expected attendance, no new asks |
| DECELERATING | Thinning engagement; fewer signals | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: Velocity not from this prefill.

---

### Step 3b-prefill: Source typology

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact | None |
| INFERRED | Reasoned from pattern or adjacent signal | Flag for validation |
| ASSUMED | No direct evidence; stereotype or default | Mandatory Step 8 target |

Source format: `[TYPOLOGY: description]`.

FAIL_UNANNOTATED_SOURCE: Source cell present but lacking typology label.

---

### Phase 3: Power/Interest grid

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | [direction: signal] | ACCELERATING / STABLE / DECELERATING | [TBD] | [TYPOLOGY: description] | [INERTIA] if applicable |

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE as defined.

---

### Step 4a: Veto probability band prefill

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto |
| MED | 30–70% | Conditional veto |
| LOW | < 30% | Unlikely veto |

FAIL_UNCALIBRATED_PROBABILITY: value not from these labels.

---

### Step 4b: Veto risk ranking

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [strategy] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY as defined.

---

### Step 5a: Engagement window derivation

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW: window absent from derivation or grid.

---

### Step 5b: Champion identification

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory only | Occasional touchpoint | Verbal interest; no commitment |
| 2 | Named participant; can advance or delay | Regular decision loop; async channel | Documented commitment; named owner |
| 3 | Final authority or veto | Peer-level; synchronous on request | Committed; deadline + contingency |

FAIL_UNANCHORED_SCORE: score outside 0–3 or Evidence missing level citation.

---

### Step 5c: Champion depth scoring

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE as defined.

---

### Step 5d: Champion durability

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals.

---

### Step 6a: Frame Type prefill and assignment

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory; message references Step 0b competitor |

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows without `displacement-acknowledgment`
assigned here.

---

### Step 6c: Channel binding prefill

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback) |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL as defined.

---

### Step 6b: Communication strategy per quadrant

Priority Band column draws exclusively from Step 6e-priority prefill.
Displacement-acknowledgment messages must reference the Step 0b competitor by name.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [Step 0b competitor referenced; preserves current first] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL as defined.

---

### Step 6d-sequence: Displacement comms sequence audit

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor] | [other row timings] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment row not T+0 baseline.

---

### Step 6e-priority: Comms priority band prefill

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint; delay loses window | Schedule within 48h of publication |
| STANDARD | Window extends beyond sprint; preferred within 1–2 cycles | Next touchpoint within window |
| DEFERRED | No forcing function; opportunistic | Document intended timing; no obligation |

FAIL_UNCALIBRATED_PRIORITY: any comms row Priority Band not drawn from this prefill.

---

### Step 7: Gatekeeper completeness check

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: gatekeeper missing comms row, blocking reason, or lead time
violation.

---

### Step 8: Amendment protocol

For each amendment, populate one row with three required cells.

| # | Amendment Target | Change Made | Verification |
|---|-----------------|-------------|--------------|
| 1 | [grid row / veto entry / comms row / conflict pathway / escalation tier / trajectory / velocity / window / champion score / synthesis row / competitor entry] | [exact update applied — e.g., "ASSUMED source upgraded to OBSERVED; artifact: interview notes 2026-03-15"] | confirmed: [artifact + date] / not-yet: [reason + owner + deadline] |

Mandatory ASSUMED obligation: All ASSUMED-annotated Source cells are mandatory targets.

FAIL_OBSERVATION_ONLY: Change Made cell absent.
FAIL_UNVERIFIED_AMENDMENT: Change Made populated but Verification absent or "not-yet"
without documented reason and assigned owner.

---

### Step 8b: Synthesis coverage audit

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes | — |
| [name] | no | [reason] |

FAIL_SYNTHESIS_GAP: stakeholder absent without justification.

---

### Step 9: Cross-phase synthesis readout

One compact row per stakeholder. Inline attribution: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [score/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [name or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP as defined.
```

---

## Round 18 structural summary

| Variation | New Gate Candidate | Fires At | Distinct From |
|-----------|-------------------|----------|---------------|
| V-01 | FAIL_UNCALIBRATED_PRIORITY | Step 6e-priority: any comms row Priority Band not from prefill | FAIL_VAGUE_TIMING (C-25): timing absent vs. priority band absent |
| V-02 | FAIL_UNVERIFIED_AMENDMENT | Step 8: Change Made present but Verification absent or unassigned | FAIL_OBSERVATION_ONLY (C-23): no update applied vs. update applied but unconfirmed |
| V-03 | FAIL_NO_COMPETITOR_ENTRY | Step 2b: inertia stakeholder with no Step 0b competitor reference | FAIL_NO_INERTIA (C-11): no inertia identified vs. inertia identified but competitor not inventoried |
| V-04 | Both V-01 + V-02 | Step 6e and Step 8 | Independently satisfiable; no interference |
| V-05 | All three | Step 6e, Step 8, Step 0b/Step 2b | All three independently satisfiable across three lifecycle phases |
