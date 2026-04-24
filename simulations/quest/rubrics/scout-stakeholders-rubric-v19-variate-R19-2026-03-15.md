## Round 19 Variations — scout-stakeholders

**Target rubric**: v19 (max 300 pts)
**Baseline**: R18 V-05 (300/300 under v19 — all C-48, C-49, C-50 carried)
**Goal**: All five variations include C-48 + C-49 + C-50 (mandatory for 300/300 baseline).
Explore three new single-axis structures as candidates for C-51/C-52/C-53 in v20.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register: source staleness band calibration | Phase 3 source typology (C-46) classifies epistemic basis but has no temporal dimension. A source staleness prefill (CURRENT/STALE/EXPIRED) is the 8th calibration motif instance. FAIL_UNCALIBRATED_STALENESS is distinct from FAIL_UNANNOTATED_SOURCE (C-46): C-46 fires when typology label is absent; new gate fires when typology is present but no staleness band governs temporal reliability |
| V-02 | Lifecycle emphasis: synthesis field depth gate | Step 9 requires field presence (C-32) and stakeholder coverage (C-42), but no gate fires when fields are structurally present but functionally empty. A synthesis depth audit (Step 9b) fires FAIL_SHALLOW_SYNTHESIS when any field carries undocumented N/A or placeholder content — distinct from FAIL_NO_SYNTHESIS (C-32) and FAIL_SYNTHESIS_GAP (C-42) |
| V-03 | Inertia framing: competitor response track | Step 0b (C-50) assigns Adoption Band + Switching Cost Band but no strategic response track. A Response Track prefill (CONVERT/CONTAIN/CO-EXIST) extends Step 0b to triple-band structure and propagates a response track citation through Step 2b and Step 9. FAIL_NO_RESPONSE_TRACK fires when a Step 0b entry lacks a Response Track drawn from the prefill |
| V-04 | V-01 + V-02 combined | Source staleness calibration (Step 3c) and synthesis depth gate (Step 9b) operate at independent phases; mutually non-interfering |
| V-05 | V-01 + V-02 + V-03 combined | All three new axes simultaneously; maximum structural density for Round 19 discovery |

---

## V-01 — Phrasing register: Source Staleness Band Calibration

**Axis**: Phrasing register — adds Step 3c-staleness (source staleness band prefill: CURRENT/STALE/EXPIRED) between Step 3b-prefill and Phase 3 grid. Phase 3 grid gains a Source Age column constrained to Step 3c labels. EXPIRED entries become mandatory ASSUMED-reclassification targets alongside the existing ASSUMED amendment obligation from C-46.

**Hypothesis**: Phase 3 source typology (OBSERVED/INFERRED/ASSUMED) classifies epistemic basis but has no temporal reliability gate. A source with OBSERVED typology can still be dangerously stale if the observation was made two quarters ago. A staleness prefill (CURRENT/STALE/EXPIRED) with explicit day-count criteria is the 8th instance of the calibration motif, extending coverage to the temporal-reliability layer of the source evidence stack. FAIL_UNCALIBRATED_STALENESS is a new gate distinct from FAIL_UNANNOTATED_SOURCE (C-46): FAIL_UNANNOTATED_SOURCE fires when the typology label is absent from a Source cell; FAIL_UNCALIBRATED_STALENESS fires when a typology label is present and valid (C-46 PASS) but no staleness band governs temporal reliability — a row can satisfy C-46 while failing FAIL_UNCALIBRATED_STALENESS.

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

### Step 0b: Status-quo competitor inventory — Strategy role

Before Phase 1, name each workflow or tool this feature displaces as a first-class
competitor. Assign two prefill-calibrated attributes per entry.

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | Used by > 70% of affected stakeholders as primary workflow; replacing it requires active migration |
| ACTIVE | Used by 30–70% of affected stakeholders; coexists with alternatives; switching is incremental |
| MARGINAL | Used by < 30% of affected stakeholders; already declining or already partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Migration requires retraining, data migration, or process redesign; stakeholder resistance is expected |
| MEDIUM | Migration requires workflow adjustment and communication; resistance is possible but manageable |
| LOW | Migration is self-service or transparent; minimal stakeholder action required |

Competitor inventory table:

| Competitor | Description | Adoption Band | Switching Cost Band |
|------------|-------------|---------------|---------------------|
| [displaced workflow or tool] | [what it does that this feature replaces] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW |

FAIL_NO_COMPETITOR_ENTRY: an inertia-tagged stakeholder appears in Step 2b but no
corresponding entry in this table names the workflow or tool that stakeholder represents.
Distinct from FAIL_NO_INERTIA (C-11): C-11 fires when inertia stakeholders are absent;
FAIL_NO_COMPETITOR_ENTRY fires when inertia stakeholders are present (C-11 PASS) but their
represented status-quo system is not inventoried here with calibrated Adoption and
Switching Cost Bands.

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
drawn from this prefill.

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
| [name] | [named person or body above Resolution Authority] | [condition activating escalation] | [action taken by Escalation Owner] |

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

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] | [competitor name from Step 0b] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.
The Step 0b Competitor cell must reference an entry in the Step 0b inventory table.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.
FAIL_NO_COMPETITOR_ENTRY: an inertia stakeholder's Step 0b Competitor cell is blank or
references a name not present in the Step 0b inventory table.

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

### Step 3c-staleness: Source staleness band prefill — PM role

Before populating the Phase 3 grid, establish the staleness bands that all Source Age
column entries must draw from. EXPIRED entries are mandatory ASSUMED-reclassification
targets — they must be either reclassified to OBSERVED or INFERRED with a refreshed
artifact, or annotated as unresolved in the Step 8 amendment table.

| Staleness Band | Criteria | Reliability Implication |
|----------------|----------|------------------------|
| CURRENT | Source confirmed or refreshed within the current sprint cycle (< 14 days) | Evidence is load-bearing; use without qualification |
| STALE | Source confirmed 15–60 days ago; no refresh since prior sprint cycle | Evidence is indicative only; flag for validation at next touchpoint |
| EXPIRED | Source confirmed > 60 days ago, or original observation was one-time with no follow-up | Evidence is unreliable; mandatory reclassification target in Step 8 alongside ASSUMED entries |

Each Source Age cell in the Phase 3 grid must carry exactly one label from this table.

FAIL_UNCALIBRATED_STALENESS: any Phase 3 grid row carries a Source Age value not drawn
from this prefill (e.g., free-form date, numeric day count, or ad hoc freshness label
not established here). Distinct from FAIL_UNANNOTATED_SOURCE (C-46):
FAIL_UNANNOTATED_SOURCE fires when the typology label is absent from the Source cell;
FAIL_UNCALIBRATED_STALENESS fires when a valid typology label is present (C-46 PASS) but
the Source Age column is absent or uncalibrated — a row satisfies C-46 while failing
FAIL_UNCALIBRATED_STALENESS.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [observable signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

Source column format: `[TYPOLOGY: source description]` where TYPOLOGY is drawn from
Step 3b-prefill. Source Age column: one label from Step 3c-staleness prefill.
ASSUMED entries and EXPIRED Source Age entries are both designated mandatory Step 8
amendment targets.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source entry.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses a label not from Step 3a.
FAIL_UNANNOTATED_SOURCE: any Source cell lacks typology label from Step 3b-prefill.
FAIL_UNCALIBRATED_STALENESS: Source Age column absent or any entry not drawn from Step 3c.

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
row does not carry the T+0 baseline timing anchor.
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
source age assessments, engagement window derivations, champion depth scores (with
updated anchor citations), synthesis readout rows.

Step 8 uses the 3-column amendment protocol. Each row requires all three cells to be
populated. ASSUMED-annotated and EXPIRED-annotated Source entries are mandatory targets.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [structural artifact + row identifier] | [specific change applied] | [confirmed artifact reference with date, OR "not-yet: [named owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target
(Change Made cell absent or blank).
FAIL_UNVERIFIED_AMENDMENT: any row has a populated Change Made cell but the Verification
cell is absent, blank, or carries "not-yet" without a named owner and deadline.
Distinct from FAIL_OBSERVATION_ONLY: FAIL_OBSERVATION_ONLY fires when no update is
applied; FAIL_UNVERIFIED_AMENDMENT fires when an update is documented but not confirmed.

Mandatory ASSUMED amendment obligation: All Source cells annotated ASSUMED in the Phase 3
grid are mandatory targets. Each must carry a populated Verification cell.
Mandatory EXPIRED amendment obligation: All Source Age cells annotated EXPIRED in the
Phase 3 grid are mandatory targets. Each must carry a populated Verification cell
confirming reclassification or documenting unresolved status with owner and deadline.

---

### Step 8b: Synthesis coverage audit — PM role

Before Step 9, confirm every Phase 3 grid stakeholder has a designated synthesis row.

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from the Step 9 synthesis readout without
a documented justification in this table.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. All stakeholders listed in Step 8b as "Synthesis Row
Planned: yes" must appear. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [Step 0b entry or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without documented justification.
```

---

## V-02 — Lifecycle Emphasis: Synthesis Field Depth Gate

**Axis**: Lifecycle emphasis — adds Step 9b (synthesis depth audit) after Step 9. For each stakeholder row in the synthesis readout, each of the 7 required fields must either carry substantive content or an explicit N/A justification with a reason code. FAIL_SHALLOW_SYNTHESIS fires when any field is functionally empty without documentation.

**Hypothesis**: Step 9 requires that fields are present (C-32) and stakeholders are covered (C-42), but neither gate fires when a field is structurally present yet functionally empty — carrying "N/A", "—", or a placeholder with no explanation. A synthesis depth audit (Step 9b) closes this gap by requiring either a substantive value OR a documented N/A justification with a named reason code. FAIL_SHALLOW_SYNTHESIS is distinct from FAIL_NO_SYNTHESIS (C-32): C-32 fires when the synthesis step is absent or a required field is structurally missing; FAIL_SHALLOW_SYNTHESIS fires when all fields are structurally present but one is functionally empty without justification — a depth obligation orthogonal to field presence. FAIL_SHALLOW_SYNTHESIS is also distinct from FAIL_SYNTHESIS_GAP (C-42): C-42 fires when a stakeholder row is absent; FAIL_SHALLOW_SYNTHESIS fires when a stakeholder row is present but a field within it is undocumented.

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

### Step 0b: Status-quo competitor inventory — Strategy role

Before Phase 1, name each workflow or tool this feature displaces as a first-class
competitor. Assign two prefill-calibrated attributes per entry.

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | Used by > 70% of affected stakeholders as primary workflow; replacing it requires active migration |
| ACTIVE | Used by 30–70% of affected stakeholders; coexists with alternatives; switching is incremental |
| MARGINAL | Used by < 30% of affected stakeholders; already declining or already partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Migration requires retraining, data migration, or process redesign; stakeholder resistance is expected |
| MEDIUM | Migration requires workflow adjustment and communication; resistance is possible but manageable |
| LOW | Migration is self-service or transparent; minimal stakeholder action required |

Competitor inventory table:

| Competitor | Description | Adoption Band | Switching Cost Band |
|------------|-------------|---------------|---------------------|
| [displaced workflow or tool] | [what it does that this feature replaces] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW |

FAIL_NO_COMPETITOR_ENTRY: an inertia-tagged stakeholder appears in Step 2b but no
corresponding entry in this table names the workflow or tool that stakeholder represents.

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
conflict rows must draw from.

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Conflict blocks the decision entirely or forces a restart if unresolved by deadline; no workaround exists | Escalation Owner must be activated before deadline; delay is not recoverable |
| SIGNIFICANT | Conflict delays the decision or degrades its quality if unresolved; a workaround exists but carries cost | Escalation Owner activated if deadline passes; cost must be documented |
| MANAGEABLE | Conflict resolves within normal process; timeline impact is unlikely even without escalation | No escalation activation required; monitor and confirm at next checkpoint |

FAIL_UNCALIBRATED_SEVERITY: any Step 2a conflict row carries a Severity Band value not
drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. Party anchor rule: Each Party A and Party B
must either match a Phase 1 segment name verbatim or carry an `[ORG-ROLE: description]` tag.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | [nature] | CRITICAL / SIGNIFICANT / MANAGEABLE | [named authority] | [ruling needed] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: Resolution Authority, Decision Required, or Deadline absent.
FAIL_NO_ESCALATION_PATH: no escalation tier row with named owner and trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: party name not traceable to Phase 1 segment or ORG-ROLE tag.
FAIL_UNCALIBRATED_SEVERITY: Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name or group] | [current approach disrupted] | [what this feature replaces] | [yes / limited / no] | [competitor name from Step 0b] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in Notes.
They must receive `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when feature displaces existing workflow.
FAIL_NO_COMPETITOR_ENTRY: inertia stakeholder's Step 0b Competitor cell blank or
references a name not in the Step 0b inventory.

---

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with anchored parties, calibrated severity band,
      complete resolution pathway, and escalation tier row
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals in last review cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid row omits Velocity label or uses a label
not drawn from this prefill.

---

### Step 3b-prefill: Source typology — PM role

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact exists | None — confirm at Step 8 if stale |
| INFERRED | Reasoned from pattern or adjacent signal; not directly witnessed | Flag for validation at next touchpoint |
| ASSUMED | No direct or adjacent evidence; based on role stereotype | Mandatory Step 8 amendment target |

Each Source cell must carry exactly one typology label: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Source cell present and populated but lacking typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | [INERTIA] if applicable |

ASSUMED Source entries are mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source entry.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or uncalibrated.
FAIL_UNANNOTATED_SOURCE: any Source cell lacks typology label.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a probability value not from these bands.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH first, then MED, then LOW.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER: entries not ordered HIGH → MED → LOW.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: band not drawn from Step 4a prefill.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column with derived values.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not populated in grid.

---

### Step 5b: Champion identification — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority | No direct contact channel | No documented statement of support |
| 1 | Advisory influence only | Occasional touchpoint | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant; can advance or delay but not close | In regular decision loop; direct async channel | Documented commitment with schedulable action |
| 3 | Final decision authority or veto power | Peer-level relationship; synchronous channel on request | Committed with deadline, named accountability, and contingency |

FAIL_UNANCHORED_SCORE: any dimension score outside 0–3, or Evidence cell does not cite
a level from this prefill.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [behavioral evidence] |
| Proximity | [0–3] | level [N]: [behavioral evidence] |
| Commitment | [0–3] | level [N]: [behavioral evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative identified and no risk documented.
FAIL_UNANCHORED_SCORE: score outside 0–3 or Evidence cell does not cite a Step 5b-anchor level.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
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
| `displacement-acknowledgment` | Meeting | — (no fallback) |

FAIL_NO_CHANNEL: Channel column absent from comms table.
FAIL_WRONG_CHANNEL: any row uses a channel not listed for its Frame Type.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.
FAIL_WRONG_CHANNEL: any row uses an unpermitted channel.
FAIL_NO_CHANNEL: Channel column absent.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor] | [row1: anchor; row2: anchor] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment row does not carry T+0 baseline.

---

### Step 6e-priority: Comms priority band prefill — PM role

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint; delay risks losing the window | Schedule within 48 hours of plan publication |
| STANDARD | Window extends beyond current sprint; preferred within 1–2 cycles | Schedule at next available touchpoint within window |
| DEFERRED | No forcing function; timing is fully opportunistic | Document intended timing; no hard scheduling obligation |

When multiple comms rows share an engagement window: URGENT first, then STANDARD, then DEFERRED.

FAIL_UNCALIBRATED_PRIORITY: any Step 6b Priority Band value not drawn from this prefill.
Distinct from FAIL_VAGUE_TIMING: timing anchor absent (C-25) vs. priority band uncalibrated.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: gatekeeper missing comms row, blocking reason, or lead time honored.

---

### Step 8: Amendment phase — PM role

3-column amendment protocol. ASSUMED-annotated Source entries are mandatory targets.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [structural artifact + row identifier] | [specific change applied] | [confirmed artifact reference + date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.
FAIL_UNVERIFIED_AMENDMENT: Change Made cell populated but Verification cell absent, blank,
or carries "not-yet" without named owner and deadline. Distinct from FAIL_OBSERVATION_ONLY:
FAIL_OBSERVATION_ONLY fires when no update is applied; FAIL_UNVERIFIED_AMENDMENT fires when
an update is documented but not confirmed.

Mandatory ASSUMED amendment obligation: all ASSUMED Source cells must carry a populated
Verification cell.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from Step 9 without justification here.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution required.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [Step 0b entry or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without justification.

---

### Step 9b: Synthesis depth audit — PM role

After populating the Step 9 synthesis readout, audit each field per stakeholder row for
substantive content. A field is functionally empty if it contains only "N/A", "—",
"Not applicable", or a placeholder equivalent with no documented reason.

Permitted N/A justification format: `N/A: [reason code — one of: NO-CONFLICT,
NO-CHAMPION-ROLE, MONITOR-ONLY, NO-COMPETITOR-CONTEXT]`

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor | All Fields Substantive? |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|------------------------|
| [name] | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL |

A field is PASS if it carries substantive content or an N/A with a permitted reason code.
A field is FAIL if it carries undocumented N/A, a dash, or a placeholder with no justification.

FAIL_SHALLOW_SYNTHESIS: any field in this audit carries FAIL status. Distinct from
FAIL_NO_SYNTHESIS (C-32): FAIL_NO_SYNTHESIS fires when the synthesis step is absent or
a required field is structurally missing; FAIL_SHALLOW_SYNTHESIS fires when all fields
are structurally present (C-32 PASS) but one is functionally empty without a permitted
N/A justification. Distinct from FAIL_SYNTHESIS_GAP (C-42): FAIL_SYNTHESIS_GAP fires
when a stakeholder row is absent from synthesis; FAIL_SHALLOW_SYNTHESIS fires when a
stakeholder row is present but a field within it is undocumented.
```

---

## V-03 — Inertia Framing: Competitor Response Track

**Axis**: Inertia framing — extends Step 0b (C-50) from dual-band to triple-band structure. A Response Track prefill (CONVERT/CONTAIN/CO-EXIST) is added to Step 0b. Each competitor entry gains a Response Track column drawn from the prefill. The response track citation propagates through Step 2b (Competitor reference now includes track) and Step 9 (synthesis Competitor field cites track). FAIL_NO_RESPONSE_TRACK fires when a Step 0b entry lacks a Response Track drawn from the prefill.

**Hypothesis**: Step 0b (C-50) inventories each status-quo competitor with Adoption Band and Switching Cost Band, but no gate governs strategic intent for how each competitor is to be handled. Two features could have the same competitor with DOMINANT adoption and HIGH switching cost but require fundamentally different engagement strategies — one tries to convert inertia stakeholders, another accepts coexistence. A Response Track prefill (CONVERT/CONTAIN/CO-EXIST) is the first strategy-classification calibration gate at the competitor layer. FAIL_NO_RESPONSE_TRACK is distinct from FAIL_NO_COMPETITOR_ENTRY (C-50): C-50 fires when a competitor entry is absent; FAIL_NO_RESPONSE_TRACK fires when a competitor entry is present (C-50 PASS) but the strategic response track is undeclared. A variation that satisfies C-50 with a fully populated competitor inventory while omitting the Response Track column and prefill = C-50 PASS, FAIL_NO_RESPONSE_TRACK.

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
| 0.2 | CODEOWNERS absent; invocation string contains org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output `[STATE: <label>]` before Phase 1. Label must match branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted label does not correspond to the source actually used.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Before Phase 1, name each displaced workflow or tool as a first-class competitor.
Assign three prefill-calibrated attributes per entry.

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | Used by > 70% of affected stakeholders as primary workflow; active migration required |
| ACTIVE | Used by 30–70%; coexists with alternatives; switching is incremental |
| MARGINAL | Used by < 30%; already declining or partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Migration requires retraining, data migration, or process redesign; resistance expected |
| MEDIUM | Migration requires workflow adjustment; resistance is possible but manageable |
| LOW | Migration is self-service or transparent; minimal stakeholder action required |

Response Track prefill:

| Response Track | Criteria | Engagement Implication |
|----------------|----------|------------------------|
| CONVERT | Goal is to move inertia stakeholders from current approach to new feature; success = adoption | Displacement-acknowledgment comms must include a named conversion path and milestone |
| CONTAIN | Goal is to limit growth of current approach while new feature matures; coexistence is transitional | Displacement-acknowledgment comms must include a containment boundary and review checkpoint |
| CO-EXIST | Current approach and new feature serve different enough needs that permanent coexistence is acceptable | Displacement-acknowledgment comms must clarify boundary conditions and avoid messaging that implies replacement |

Competitor inventory table:

| Competitor | Description | Adoption Band | Switching Cost Band | Response Track |
|------------|-------------|---------------|---------------------|----------------|
| [displaced workflow or tool] | [what it does] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW | CONVERT / CONTAIN / CO-EXIST |

FAIL_NO_COMPETITOR_ENTRY: an inertia-tagged stakeholder appears in Step 2b but no
corresponding entry in this table names the workflow or tool they represent.
FAIL_NO_RESPONSE_TRACK: any competitor entry in this table lacks a Response Track value
drawn from the Response Track prefill (e.g., blank, free-form strategy description, or
ad hoc label not from this prefill). Distinct from FAIL_NO_COMPETITOR_ENTRY: C-50 fires
when the competitor entry is absent; FAIL_NO_RESPONSE_TRACK fires when the entry is
present (C-50 PASS) but the strategic response track is undeclared.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern] | [affected touchpoints] | [explicit NOT-doing for this segment] | [gatekeeper / inertia / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: address what the new approach does not preserve.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 1 → Phase 2 Transition Gate — UX role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration — Strategy role

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision entirely; no workaround | Escalation Owner activated before deadline |
| SIGNIFICANT | Delays decision or degrades quality; workaround carries cost | Escalation Owner activated if deadline passes |
| MANAGEABLE | Resolves within normal process; timeline impact unlikely | No escalation activation required |

FAIL_UNCALIBRATED_SEVERITY: any conflict row carries Severity Band not drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | [nature] | CRITICAL / SIGNIFICANT / MANAGEABLE | [named authority] | [ruling] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY: apply as defined.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor | Response Track |
|-------------|-----------------|--------------|-------------------|--------------------|----------------|
| [name] | [current approach disrupted] | [what this feature replaces] | [yes / limited / no] | [competitor from Step 0b] | [Response Track from Step 0b] |

Inertia stakeholders must appear in Phase 3 with `[INERTIA]` tag.
They must receive `displacement-acknowledgment` Frame Type in Step 6b.
The displacement-acknowledgment message must align with the Response Track assigned
in Step 0b: CONVERT messages include a conversion path; CONTAIN messages include a
containment boundary; CO-EXIST messages clarify boundary conditions.

FAIL_NO_INERTIA: no inertia stakeholders when feature displaces existing workflow.
FAIL_NO_COMPETITOR_ENTRY: Step 0b Competitor cell blank or name not in Step 0b table.

---

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with anchored parties, calibrated severity band,
      complete resolution pathway, and escalation tier row
- [ ] At least one inertia stakeholder with Step 0b Competitor and Response Track
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent.

---

### Step 3a: Trajectory velocity band prefill — PM role

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline; new signals in last cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Expected attendance, no new asks |
| DECELERATING | Engagement thinning; fewer signals than prior cycle | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 row omits Velocity or uses unlisted label.

---

### Step 3b-prefill: Source typology — PM role

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact | None — confirm at Step 8 if stale |
| INFERRED | Reasoned from pattern or adjacent signal | Flag for validation at next touchpoint |
| ASSUMED | No direct evidence; based on role stereotype | Mandatory Step 8 amendment target |

Each Source cell format: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: Source cell present but lacks typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | [direction: observable signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [TYPOLOGY: source] | [INERTIA] if applicable |

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE: apply as defined.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto under specific circumstances |
| LOW | < 30% | Limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry not drawn from these band labels.

---

### Step 4b: Veto risk ranking — PM role

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY: apply as defined.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW: window not derived or not in grid.

---

### Step 5b: Champion identification — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory influence only | Occasional touchpoint | Verbal interest only |
| 2 | Named decision participant | Regular loop; async channel | Documented with schedulable action |
| 3 | Final authority or veto power | Peer-level; synchronous on request | Deadline + accountability + contingency |

FAIL_UNANCHORED_SCORE: score outside 0–3 or Evidence does not cite a level from this prefill.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE: apply as defined.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals.

---

### Step 6a: Frame Type prefill and assignment — PM role

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment` not assigned.

---

### Step 6c: Channel binding prefill — PM role

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback) |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL: apply as defined.

---

### Step 6b: Communication strategy per quadrant — PM role

For inertia stakeholders, the Message cell must reflect the Response Track assigned in
Step 0b: CONVERT — include a conversion path; CONTAIN — include a containment boundary
and review checkpoint; CO-EXIST — clarify boundary conditions without implying replacement.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia] | displacement-acknowledgment | Meeting | [track-aligned message] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL: apply as defined.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned | Audit Result |
|--------------------|------------------------------------|------------------------------------|--------------|--------------|
| [name] | [anchor] | [other rows and anchors] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment row does not carry T+0 baseline.

---

### Step 6e-priority: Comms priority band prefill — PM role

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint; delay risks losing it | Schedule within 48 hours of plan publication |
| STANDARD | Window extends past current sprint; preferred within 1–2 cycles | Next available touchpoint within window |
| DEFERRED | No forcing function; opportunistic timing | Document intended timing; no hard obligation |

FAIL_UNCALIBRATED_PRIORITY: any Step 6b Priority Band not drawn from this prefill.
Distinct from FAIL_VAGUE_TIMING (timing absent) vs. priority band uncalibrated.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: gatekeeper missing comms row, blocking reason, or lead time honored.

---

### Step 8: Amendment phase — PM role

3-column protocol. ASSUMED-annotated Source entries are mandatory targets.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row identifier] | [change applied] | [confirmed artifact reference + date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY: no eligible structural target updated.
FAIL_UNVERIFIED_AMENDMENT: Change Made populated but Verification absent or undocumented.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes / no | [reason if no] |

FAIL_SYNTHESIS_GAP: stakeholder absent from synthesis without justification here.

---

### Step 9: Cross-phase synthesis readout — PM role

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [entry + Response Track] (Step 0b) |

The Competitor field must include both the competitor name and the Response Track from
Step 0b — e.g., "competitor: Legacy-Workflow [CONVERT] (Step 0b)".

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP: apply as defined.
```

---

## V-04 — V-01 + V-02 Combined

**Axis**: Source staleness band calibration (Step 3c) + synthesis field depth gate (Step 9b).

**Hypothesis**: Source staleness (Step 3c, operating at Phase 3 grid population) and synthesis depth audit (Step 9b, operating after Step 9) are structurally independent — no shared steps, no shared failure modes. Both can be satisfied simultaneously without tradeoffs.

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
| 0.1 | CODEOWNERS present | Extract teams as primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string has org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output `[STATE: <label>]` before Phase 1. Label must match branch actually taken.

FAIL_SILENT_INFERENCE / FAIL_WRONG_STATE: apply as defined.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | > 70% primary workflow; active migration required |
| ACTIVE | 30–70%; coexists; switching is incremental |
| MARGINAL | < 30%; declining or partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Retraining, data migration, or process redesign required; resistance expected |
| MEDIUM | Workflow adjustment and communication required; resistance manageable |
| LOW | Self-service or transparent migration; minimal stakeholder action |

| Competitor | Description | Adoption Band | Switching Cost Band |
|------------|-------------|---------------|---------------------|
| [displaced workflow or tool] | [what it does] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW |

FAIL_NO_COMPETITOR_ENTRY: inertia stakeholder in Step 2b has no matching Step 0b entry.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [pattern] | [touchpoints] | [explicit NOT-doing] | [gatekeeper / inertia / neither] |

FAIL_MONOLITH_ASSUMPTION / FAIL_NO_NOT_DOING: apply as defined.

---

### Phase 1 → Phase 2 Transition Gate

- [ ] At least two distinct segments; NOT-doing per segment; inertia NOT-doing addressed

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision; no workaround | Escalation Owner before deadline |
| SIGNIFICANT | Delays or degrades; workaround carries cost | Escalation Owner if deadline passes |
| MANAGEABLE | Normal process resolution; unlikely timeline impact | No escalation required |

FAIL_UNCALIBRATED_SEVERITY: Severity Band not drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE] | [Phase 1 segment OR ORG-ROLE] | [nature] | CRITICAL / SIGNIFICANT / MANAGEABLE | [authority] | [ruling] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY: apply as defined.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name] | [current approach] | [feature replaces] | [yes / limited / no] | [competitor from Step 0b] |

FAIL_NO_INERTIA / FAIL_NO_COMPETITOR_ENTRY: apply as defined.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper without lead time.

---

### Phase 2 → Phase 3 Transition Gate

- [ ] Two structural conflicts with anchored parties, calibrated severity, complete
      resolution pathway, escalation tier row
- [ ] Inertia stakeholder (or no-displacement statement)
- [ ] Critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: required Phase 2 output absent.

---

### Step 3a: Trajectory velocity band prefill

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Faster than baseline; new signals in last cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Expected touchpoints, no new asks |
| DECELERATING | Thinning engagement; fewer signals | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: Phase 3 row omits Velocity or uses unlisted label.

---

### Step 3b-prefill: Source typology

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact | None — confirm at Step 8 if stale |
| INFERRED | Reasoned from pattern or adjacent signal | Flag for validation at next touchpoint |
| ASSUMED | No direct evidence; role stereotype | Mandatory Step 8 amendment target |

Each Source cell: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: Source cell present but lacks typology label.

---

### Step 3c-staleness: Source staleness band prefill — PM role

Before populating the Phase 3 grid, establish the staleness bands governing temporal
reliability of all Source Age column entries. EXPIRED entries are mandatory targets
in Step 8 alongside ASSUMED entries.

| Staleness Band | Criteria | Reliability Implication |
|----------------|----------|------------------------|
| CURRENT | Confirmed < 14 days ago | Load-bearing; use without qualification |
| STALE | Confirmed 15–60 days ago | Indicative only; flag for validation at next touchpoint |
| EXPIRED | Confirmed > 60 days ago, or one-time observation with no follow-up | Unreliable; mandatory Step 8 reclassification target |

Each Source Age cell in the Phase 3 grid must carry exactly one label from this table.

FAIL_UNCALIBRATED_STALENESS: Source Age column absent or any entry not drawn from this
prefill. Distinct from FAIL_UNANNOTATED_SOURCE (C-46): FAIL_UNANNOTATED_SOURCE fires when
typology label absent from Source cell; FAIL_UNCALIBRATED_STALENESS fires when typology
is present (C-46 PASS) but Source Age is absent or uncalibrated.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | [direction: signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [TYPOLOGY: source] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

ASSUMED and EXPIRED entries are both mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE / FAIL_UNCALIBRATED_STALENESS.

---

### Step 4a: Veto probability band prefill

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto under specific circumstances |
| LOW | < 30% | Limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY: Step 4b entry not drawn from these bands.

---

### Step 4b: Veto risk ranking

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY.

---

### Step 5a: Engagement window derivation

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW.

---

### Step 5b: Champion identification

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION.

---

### Step 5b-anchor: Champion dimension anchor prefill

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory only | Occasional touchpoint | Verbal interest |
| 2 | Named participant; can advance or delay | Regular loop; async channel | Documented with schedulable action |
| 3 | Final authority or veto | Peer-level; synchronous on request | Deadline + accountability + contingency |

FAIL_UNANCHORED_SCORE.

---

### Step 5c: Champion depth scoring

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE.

---

### Step 5d: Champion durability

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY.

---

### Step 6a: Frame Type prefill and assignment

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

FAIL_MISSING_DISPLACEMENT_PREFILL.

---

### Step 6c: Channel binding prefill

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback) |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL.

---

### Step 6b: Communication strategy per quadrant

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia] | displacement-acknowledgment | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL.

---

### Step 6d-sequence: Displacement comms sequence audit

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms (with Timing) | T+0 Assigned | Audit Result |
|--------------------|------------------------------------|-----------------------------|--------------|--------------|
| [name] | [anchor] | [other rows: anchors] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION.

---

### Step 6e-priority: Comms priority band prefill

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint | Schedule within 48 hours |
| STANDARD | Window extends past current sprint | Next touchpoint within window |
| DEFERRED | No forcing function | Document intended timing |

FAIL_UNCALIBRATED_PRIORITY: Priority Band not from this prefill. Distinct from FAIL_VAGUE_TIMING.

---

### Step 7: Gatekeeper completeness check

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE.

---

### Step 8: Amendment phase

3-column protocol. ASSUMED-annotated and EXPIRED-annotated Source entries are mandatory targets.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row] | [change applied] | [confirmed reference + date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY / FAIL_UNVERIFIED_AMENDMENT: apply as defined.

Mandatory ASSUMED amendment obligation and mandatory EXPIRED amendment obligation both apply.

---

### Step 8b: Synthesis coverage audit

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes / no | [reason if no] |

FAIL_SYNTHESIS_GAP.

---

### Step 9: Cross-phase synthesis readout

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [Step 0b entry or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP.

---

### Step 9b: Synthesis depth audit — PM role

After populating Step 9, audit each field per stakeholder row for substantive content.
Permitted N/A format: `N/A: [reason code — one of: NO-CONFLICT, NO-CHAMPION-ROLE,
MONITOR-ONLY, NO-COMPETITOR-CONTEXT]`

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor | All Fields Substantive? |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|------------------------|
| [name] | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL |

FAIL_SHALLOW_SYNTHESIS: any field carries FAIL (undocumented N/A or placeholder).
Distinct from FAIL_NO_SYNTHESIS (field absent) and FAIL_SYNTHESIS_GAP (row absent).
```

---

## V-05 — V-01 + V-02 + V-03 Combined (Maximum Structural Density)

**Axis**: Source staleness band calibration (Step 3c) + synthesis field depth gate (Step 9b) + competitor response track (Step 0b Response Track).

**Hypothesis**: All three axes operate at independent lifecycle phases — Step 3c at grid population, Step 0b Response Track at pre-Phase-1, Step 9b at post-synthesis — with no structural interference. V-05 is the maximum structural density variation for Round 19. Step 9 synthesis gains three new fields simultaneously (Priority Band from C-48, Competitor from C-50, Response Track from V-03 axis) — the most information-dense synthesis readout across all R19 variations. The V-03 Response Track propagation creates the only constraint in this variation that spans three steps: Step 0b (Response Track assigned) → Step 2b (track cited in inertia mapping) → Step 6b (displacement-acknowledgment message aligned to track) → Step 9 (Competitor field cites track).

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
| 0.1 | CODEOWNERS present | Extract teams as primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation string has org identifiers | Extract org context from invocation string | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither sufficient | Ask: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output `[STATE: <label>]` before Phase 1. Label must match branch actually taken.

FAIL_SILENT_INFERENCE / FAIL_WRONG_STATE: apply as defined.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | > 70% primary workflow; active migration required |
| ACTIVE | 30–70%; coexists; incremental switching |
| MARGINAL | < 30%; declining or partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Retraining, data migration, or process redesign; resistance expected |
| MEDIUM | Workflow adjustment and communication; resistance manageable |
| LOW | Self-service or transparent; minimal stakeholder action |

Response Track prefill:

| Response Track | Criteria | Engagement Implication |
|----------------|----------|------------------------|
| CONVERT | Goal is stakeholder adoption of new feature; success = full migration | Displacement comms must include a conversion path and milestone |
| CONTAIN | Limit growth of current approach while new feature matures; coexistence is transitional | Displacement comms must include a containment boundary and review checkpoint |
| CO-EXIST | Permanent coexistence is acceptable; different-enough use cases | Displacement comms must clarify boundary conditions; avoid replacement messaging |

Competitor inventory table:

| Competitor | Description | Adoption Band | Switching Cost Band | Response Track |
|------------|-------------|---------------|---------------------|----------------|
| [displaced workflow or tool] | [what it does] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW | CONVERT / CONTAIN / CO-EXIST |

FAIL_NO_COMPETITOR_ENTRY: inertia stakeholder in Step 2b has no matching Step 0b entry.
FAIL_NO_RESPONSE_TRACK: any competitor entry lacks a Response Track from the prefill.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [pattern] | [touchpoints] | [explicit NOT-doing] | [gatekeeper / inertia / neither] |

FAIL_MONOLITH_ASSUMPTION / FAIL_NO_NOT_DOING: apply as defined.

---

### Phase 1 → Phase 2 Transition Gate

- [ ] Two distinct segments; NOT-doing per segment; inertia NOT-doing addressed

FAIL_INCOMPLETE_PHASE1.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision; no workaround | Escalation Owner before deadline |
| SIGNIFICANT | Delays or degrades; workaround costly | Escalation Owner if deadline passes |
| MANAGEABLE | Normal process; unlikely timeline impact | No escalation required |

FAIL_UNCALIBRATED_SEVERITY.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 OR ORG-ROLE] | [Phase 1 OR ORG-ROLE] | [nature] | CRITICAL / SIGNIFICANT / MANAGEABLE | [authority] | [ruling] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [above authority] | [condition] | [action] |

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor | Response Track |
|-------------|-----------------|--------------|-------------------|--------------------|----------------|
| [name] | [current approach] | [replaced by] | [yes / limited / no] | [competitor from Step 0b] | [Response Track from Step 0b] |

Inertia stakeholders must appear in Phase 3 with `[INERTIA]` tag.
Displacement-acknowledgment comms message must align with the Response Track assigned.

FAIL_NO_INERTIA / FAIL_NO_COMPETITOR_ENTRY: apply as defined.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING.

---

### Phase 2 → Phase 3 Transition Gate

- [ ] Two conflicts with anchored parties, calibrated severity, complete resolution pathway,
      escalation tier row
- [ ] Inertia stakeholder with Step 0b Competitor and Response Track
- [ ] Critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2.

---

### Step 3a: Trajectory velocity band prefill

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Faster than baseline; new signals | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Expected touchpoints, no new asks |
| DECELERATING | Thinning engagement; fewer signals | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY.

---

### Step 3b-prefill: Source typology

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact | None |
| INFERRED | Reasoned from pattern | Flag for validation |
| ASSUMED | No direct evidence | Mandatory Step 8 target |

Format: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE.

---

### Step 3c-staleness: Source staleness band prefill — PM role

| Staleness Band | Criteria | Reliability Implication |
|----------------|----------|------------------------|
| CURRENT | Confirmed < 14 days | Load-bearing; use without qualification |
| STALE | Confirmed 15–60 days | Indicative; flag for validation at next touchpoint |
| EXPIRED | Confirmed > 60 days, or one-time with no follow-up | Unreliable; mandatory Step 8 reclassification target |

Each Source Age cell must carry exactly one label from this table.

FAIL_UNCALIBRATED_STALENESS: Source Age absent or entry not drawn from this prefill.
Distinct from FAIL_UNANNOTATED_SOURCE: C-46 fires on absent typology; new gate fires
when typology is present but temporal reliability is uncalibrated.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | [direction: signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [TYPOLOGY: source] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

ASSUMED and EXPIRED entries are both mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE / FAIL_UNCALIBRATED_STALENESS.

---

### Step 4a: Veto probability band prefill

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto under specific circumstances |
| LOW | < 30% | Limited authority or low stake |

FAIL_UNCALIBRATED_PROBABILITY.

---

### Step 4b: Veto risk ranking

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY.

---

### Step 5a: Engagement window derivation

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW.

---

### Step 5b: Champion identification

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION.

---

### Step 5b-anchor: Champion dimension anchor prefill

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory only | Occasional touchpoint | Verbal interest |
| 2 | Named participant; advance or delay | Regular loop; async channel | Documented with schedulable action |
| 3 | Final authority or veto | Peer-level; synchronous on request | Deadline + accountability + contingency |

FAIL_UNANCHORED_SCORE.

---

### Step 5c: Champion depth scoring

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE.

---

### Step 5d: Champion durability

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or single-point-of-failure risk] |
| Deterioration signal 1 | [observable trigger] |
| Deterioration signal 2 | [observable trigger] |

FAIL_NO_DURABILITY.

---

### Step 6a: Frame Type prefill and assignment

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders — mandatory |

FAIL_MISSING_DISPLACEMENT_PREFILL.

---

### Step 6c: Channel binding prefill

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback) |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL.

---

### Step 6b: Communication strategy per quadrant

For inertia stakeholders, the Message cell must align with the Response Track from Step 0b:
CONVERT — include conversion path and milestone; CONTAIN — include containment boundary
and review checkpoint; CO-EXIST — clarify boundary conditions without replacement framing.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia] | displacement-acknowledgment | Meeting | [track-aligned message] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL.

---

### Step 6d-sequence: Displacement comms sequence audit

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms (with Timing) | T+0 Assigned | Audit Result |
|--------------------|------------------------------------|-----------------------------|--------------|--------------|
| [name] | [anchor] | [other rows: anchors] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION.

---

### Step 6e-priority: Comms priority band prefill

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint | Schedule within 48 hours |
| STANDARD | Window extends past current sprint | Next touchpoint within window |
| DEFERRED | No forcing function | Document intended timing |

FAIL_UNCALIBRATED_PRIORITY: Priority Band not from this prefill. Distinct from FAIL_VAGUE_TIMING.

---

### Step 7: Gatekeeper completeness check

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE.

---

### Step 8: Amendment phase

3-column protocol. ASSUMED-annotated and EXPIRED-annotated Source entries are both
mandatory targets.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row] | [change applied] | [confirmed reference + date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY / FAIL_UNVERIFIED_AMENDMENT: apply as defined.

Mandatory ASSUMED and mandatory EXPIRED amendment obligations both apply.

---

### Step 8b: Synthesis coverage audit

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes / no | [reason if no] |

FAIL_SYNTHESIS_GAP.

---

### Step 9: Cross-phase synthesis readout

One compact row per stakeholder. Inline attribution required.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [entry + Response Track] (Step 0b) |

Competitor field format: `competitor: [Competitor Name] [RESPONSE-TRACK] (Step 0b)` —
e.g., "competitor: Legacy-Workflow [CONVERT] (Step 0b)".

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP.

---

### Step 9b: Synthesis depth audit — PM role

After populating Step 9, audit each field per stakeholder row.
Permitted N/A format: `N/A: [reason code — one of: NO-CONFLICT, NO-CHAMPION-ROLE,
MONITOR-ONLY, NO-COMPETITOR-CONTEXT]`

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor | All Fields Substantive? |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|------------------------|
| [name] | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL | PASS / FAIL |

FAIL_SHALLOW_SYNTHESIS: any field carries FAIL status.
Distinct from FAIL_NO_SYNTHESIS (C-32): field absent vs. field present but empty.
Distinct from FAIL_SYNTHESIS_GAP (C-42): stakeholder row absent vs. row present but shallow.
```

---

## Interference Check — V-05 Three-Axis

| Axis | Phase | New Obligation | Interference with Other Axes |
|------|-------|---------------|------------------------------|
| V-01 (staleness) | Step 3c + Phase 3 Source Age | FAIL_UNCALIBRATED_STALENESS at grid | None — grid population layer |
| V-02 (depth gate) | Step 9b post-synthesis | FAIL_SHALLOW_SYNTHESIS at synthesis audit | None — post-synthesis layer |
| V-03 (response track) | Step 0b + Step 2b + Step 6b + Step 9 | FAIL_NO_RESPONSE_TRACK at Step 0b | None — competitor inventory layer |

All three axes operate at structurally disjoint steps. V-05 Step 9 Competitor field now
carries both the competitor name and Response Track (V-03) in the same cell. V-05 Step 9b
audits that Competitor field for substantive content (V-02). V-05 Phase 3 grid carries
Source Age column (V-01) alongside existing Source typology. All three are independently
satisfiable and mutually reinforcing.

## New Gate Candidate Analysis for v20

| Candidate | Failure Mode | Step | Motif Fit | Dependency |
|-----------|-------------|------|-----------|------------|
| C-51 | FAIL_UNCALIBRATED_STALENESS | Step 3c + Phase 3 Source Age | 8th calibration motif instance; first temporal-layer gate | C-46 |
| C-52 | FAIL_SHALLOW_SYNTHESIS | Step 9b synthesis depth audit | 3-cell completeness extension to synthesis output layer | C-32 |
| C-53 | FAIL_NO_RESPONSE_TRACK | Step 0b Response Track | First strategy-classification gate at competitor layer; extends C-50 to triple-band | C-50 |
