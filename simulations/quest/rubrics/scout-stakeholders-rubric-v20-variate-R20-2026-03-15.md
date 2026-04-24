## Round 20 Variations — scout-stakeholders

**Target rubric**: v20 (max 315 pts)
**Baseline**: R19 V-05 (315/315 under v20 — all C-51, C-52, C-53 carried)
**Goal**: All five variations include the full R19 baseline criteria (C-01 through C-50).
V-01/V-02/V-03 each add one criterion via a distinct style axis. V-04 combines V-01+V-02.
V-05 combines all three — target: 315/315, GOLDEN.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence: source staleness band calibration | Step 3c-staleness is positioned BEFORE Step 3b-prefill. Temporal reliability (how fresh?) precedes epistemic basis (how obtained?). An EXPIRED OBSERVED source is functionally equivalent to ASSUMED for decision-making; framing staleness first encodes this dependency in prompt structure. FAIL_UNCALIBRATED_STALENESS. Expected: C-51 PASS, C-52/C-53 not satisfiable → 305/315 |
| V-02 | Output format: synthesis field depth gate | Step 9b uses a transposed audit matrix (fields as column headers, stakeholders as rows, each cell PASS/FAIL/N/A:[code]). Column-pattern detection: a field FAIL across all rows signals a structural synthesis gap, not a per-stakeholder error. Row-pattern detection: multiple FAILs on one stakeholder signals evidence inadequacy. FAIL_SHALLOW_SYNTHESIS. Expected: C-52 PASS, C-51/C-53 not satisfiable → 305/315 |
| V-03 | Inertia framing: competitor response track | Step 0b gains a Response Track column (CONVERT/CONTAIN/CO-EXIST). New Step 0c translates each track into explicit engagement obligation, success criterion, and downstream message requirement BEFORE Phase 1. Step 6b displacement-acknowledgment checked against Step 0c requirements. FAIL_NO_RESPONSE_TRACK + FAIL_RESPONSE_TRACK_ALIGNMENT. Expected: C-53 PASS, C-51/C-52 not satisfiable → 305/315 |
| V-04 | V-01 + V-02 combined | Temporal-primary source qualification (Step 3c before Step 3b) and matrix synthesis audit (Step 9b transposed) operate at independent positions; non-interfering. Expected: C-51 + C-52 PASS, C-53 not satisfiable → 310/315 |
| V-05 | V-01 + V-02 + V-03 combined | All three axes simultaneously; maximum structural density for Round 20 discovery. Expected: C-51 + C-52 + C-53 PASS → 315/315 — GOLDEN |

---

## V-01 — Role Sequence: Source Staleness Band Calibration

**Axis**: Role sequence — Step 3c-staleness prefill is positioned BEFORE Step 3b-prefill (source typology). Temporal reliability context precedes epistemic basis classification. Phase 3 grid gains a Source Age column constrained to Step 3c labels. EXPIRED entries become mandatory Step 8 amendment targets alongside ASSUMED entries.

**Hypothesis**: R19 V-01 inserted Step 3c-staleness after typology because typology was already established. R20 V-01 inverts this: a source's freshness governs the weight its typology can carry. An EXPIRED OBSERVED source warrants the same caution as ASSUMED. Positioning staleness first makes temporal reliability structurally primary in Phase 3 source qualification, preventing stale-but-well-typed evidence from being treated as load-bearing.

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

Identify at least two structural conflicts. Party anchor rule: each Party A and Party B
must either match a Phase 1 segment name verbatim or carry an `[ORG-ROLE: description]` tag.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named authority] | [ruling needed] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition activating escalation] | [action taken] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: Resolution Authority, Decision Required, or Deadline absent.
FAIL_NO_ESCALATION_PATH: no escalation tier row with named owner and trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: party not traceable to Phase 1 segment or ORG-ROLE tag.
FAIL_UNCALIBRATED_SEVERITY: Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces] | [yes / limited / no] | [competitor name from Step 0b] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.
The Step 0b Competitor cell must reference an entry in the Step 0b inventory table.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.
FAIL_NO_COMPETITOR_ENTRY: inertia stakeholder's Step 0b Competitor cell is blank or
references a name not present in the Step 0b inventory table.

---

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [compliance / budget / security / architecture / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

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

All Phase 3 grid Velocity column entries must draw exclusively from this table.

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline cadence; new signals in last review cycle | Unsolicited outreach, escalated involvement, coalition building |
| STABLE | No directional change since last review; consistent with prior cycle | Attendance at expected touchpoints, no new asks, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting; fewer signals than prior cycle | Missed touchpoints, proxy delegation, reduced response cadence |

FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid row omits Velocity label or uses a label
not drawn from this prefill.

---

### Step 3c-staleness: Source staleness band prefill — PM role

ROLE SEQUENCE NOTE: This step precedes Step 3b-prefill (source typology). Temporal
reliability context is established before epistemic basis classification. An EXPIRED
source should be tentatively reclassified as ASSUMED in Step 3b if no refresh is available.

All Phase 3 grid Source Age column entries must draw exclusively from this table.
EXPIRED entries are mandatory amendment targets in Step 8 alongside ASSUMED entries.

| Staleness Band | Criteria | Reliability Implication |
|----------------|----------|------------------------|
| CURRENT | Source confirmed or refreshed within the current sprint cycle (< 14 days) | Evidence is load-bearing; use without qualification |
| STALE | Source confirmed 15–60 days ago; no refresh since prior sprint cycle | Evidence is indicative only; flag for validation at next touchpoint |
| EXPIRED | Source confirmed > 60 days ago, or original observation was one-time with no follow-up | Evidence is unreliable; mandatory reclassification target in Step 8 alongside ASSUMED entries |

Each Source Age cell in the Phase 3 grid must carry exactly one label from this table.

FAIL_UNCALIBRATED_STALENESS: any Phase 3 grid row carries a Source Age value not drawn
from this prefill (e.g., free-form date, numeric day count, or ad hoc freshness label).
Distinct from FAIL_UNANNOTATED_SOURCE (C-46): FAIL_UNANNOTATED_SOURCE fires when the
typology label is absent from the Source cell; FAIL_UNCALIBRATED_STALENESS fires when a
valid typology label is present but the Source Age column is absent or uncalibrated.

---

### Step 3b-prefill: Source typology — PM role

ROLE SEQUENCE NOTE: This step follows Step 3c-staleness. EXPIRED sources from Step 3c
should be classified as ASSUMED here unless a refreshed artifact is available, since
expired evidence is functionally unverifiable at the time of grid construction.

All Source cells in the Phase 3 grid must carry exactly one typology label from this
table. ASSUMED-annotated entries become mandatory Step 8 amendment targets.

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed in meeting, document, or recorded interaction; citable artifact exists | None — confirm at Step 8 if source age is EXPIRED |
| INFERRED | Reasoned from pattern, role, or adjacent signal; not directly witnessed | Flag for validation at next stakeholder touchpoint |
| ASSUMED | No direct or adjacent evidence; based on role stereotype or default expectation | Mandatory Step 8 amendment target — must be confirmed or corrected before synthesis |

Each Source cell must carry exactly one typology label: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Phase 3 grid Source cell present and populated but lacking
a typology label from this prefill.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

Source column format: `[TYPOLOGY: source description]` drawn from Step 3b-prefill.
Source Age column: one label from Step 3c-staleness prefill.
ASSUMED entries and EXPIRED Source Age entries are both designated mandatory Step 8
amendment targets.

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source entry.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.
FAIL_UNCALIBRATED_VELOCITY: Velocity column absent or any row uses an uncalibrated label.
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
FAIL_UNANCHORED_SCORE: any score outside 0–3 or Evidence cell does not cite a level.

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
displacement-acknowledgment row carries the T+0 baseline.

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor from Step 6b row] | [row1: anchor; row2: anchor] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: any inertia-tagged stakeholder's displacement-acknowledgment
row does not carry the T+0 baseline timing anchor.

---

### Step 6e-priority: Comms priority band prefill — PM role

All Step 6b Priority Band cells must draw values exclusively from this prefill.

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Engagement window closes within the current sprint cycle; any delay risks losing the window | Owner must schedule within 48 hours of plan publication |
| STANDARD | Engagement window extends beyond the current sprint; preferred timing within 1–2 cycles | Owner schedules at next available touchpoint within window |
| DEFERRED | No forcing function; timing is fully opportunistic | Owner documents intended timing; no hard scheduling obligation |

When multiple comms rows share an engagement window, schedule: URGENT first, then
STANDARD, then DEFERRED.

FAIL_UNCALIBRATED_PRIORITY: any Step 6b comms row carries a Priority Band value not
drawn from this prefill.

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
entries, Step 6a frame type assignments, Step 6b comms rows, Step 6e-priority bands,
Step 2c gatekeeper lead-time tags, Step 2a conflict resolution entries, Step 2a
escalation tier entries, trajectory assessments, velocity assessments, source age
assessments, engagement window derivations, champion depth scores, synthesis rows.

Step 8 uses the 3-column amendment protocol. Each row requires all three cells populated.
ASSUMED-annotated Source entries and EXPIRED Source Age entries are mandatory targets.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [structural artifact + row identifier] | [specific change applied] | [confirmed artifact reference with date, OR "not-yet: [named owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.
FAIL_UNVERIFIED_AMENDMENT: any row has a populated Change Made cell but Verification cell
is absent, blank, or carries "not-yet" without a named owner and deadline.

Mandatory ASSUMED amendment obligation: all Source cells annotated ASSUMED in Phase 3
are mandatory targets. Each must carry a populated Verification cell.
Mandatory EXPIRED amendment obligation: all Source Age cells annotated EXPIRED in Phase 3
are mandatory targets. Each must carry a populated Verification cell confirming
reclassification or documenting unresolved status with owner and deadline.

---

### Step 8b: Synthesis coverage audit — PM role

Before Step 9, confirm every Phase 3 grid stakeholder has a designated synthesis row.

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from Step 9 synthesis without justification.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. All stakeholders listed in Step 8b as planned: yes must
appear. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [Step 0b entry or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without documented justification.
```

---

## V-02 — Output Format: Synthesis Field Depth Gate

**Axis**: Output format — Step 9b uses a transposed audit matrix (fields as column headers, stakeholders as rows, each cell carrying PASS / FAIL / N/A:[code]). The matrix exposes column patterns (a field FAIL across all stakeholders = structural synthesis gap) and row patterns (multiple FAILs on one stakeholder = evidence inadequacy). Discrete cells enable count-based completeness analysis not possible in prose audit formats.

**Hypothesis**: R19 V-02 introduced Step 9b as a depth audit table. R20 V-02 specifies the format more precisely: each cell contains only the audit result, not the field value. This separation of audit result from content means the matrix is a checksum layer over Step 9, not a restatement of it. A future criterion could require zero FAILs in a specific column (e.g., all Conflict Exposure cells PASS), a constraint not assessable in the prose-embedded format. The N/A:[code] syntax forces documented justification for every structural absence, extending the reason-code discipline from C-52's field-depth obligation to the audit layer itself.

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

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Conflict blocks the decision entirely or forces a restart if unresolved by deadline; no workaround exists | Escalation Owner must be activated before deadline; delay is not recoverable |
| SIGNIFICANT | Conflict delays the decision or degrades its quality if unresolved; a workaround exists but carries cost | Escalation Owner activated if deadline passes; cost must be documented |
| MANAGEABLE | Conflict resolves within normal process; timeline impact is unlikely even without escalation | No escalation activation required; monitor and confirm at next checkpoint |

FAIL_UNCALIBRATED_SEVERITY: any Step 2a conflict row carries a Severity Band value not
drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. Party anchor rule: each Party A and Party B
must either match a Phase 1 segment name verbatim or carry an `[ORG-ROLE: description]` tag.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named authority] | [ruling needed] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: Resolution Authority, Decision Required, or Deadline absent.
FAIL_NO_ESCALATION_PATH: no escalation tier row with named owner and trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: party not traceable to Phase 1 segment or ORG-ROLE tag.
FAIL_UNCALIBRATED_SEVERITY: Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name] | [current approach disrupted] | [what this feature replaces] | [yes / limited / no] | [competitor name from Step 0b] |

Inertia stakeholders must appear in Phase 3 grid with `[INERTIA]` in Notes.
They must receive `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when feature displaces existing workflow.
FAIL_NO_COMPETITOR_ENTRY: inertia stakeholder's Step 0b Competitor cell blank or references
a name not present in Step 0b inventory.

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

All Source cells in Phase 3 must carry exactly one typology label. ASSUMED entries are
mandatory Step 8 amendment targets.

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact exists | None — confirm at Step 8 if stale |
| INFERRED | Reasoned from pattern or adjacent signal; not directly witnessed | Flag for validation at next touchpoint |
| ASSUMED | No direct or adjacent evidence; based on role stereotype | Mandatory Step 8 amendment target |

Each Source cell must carry: `[TYPOLOGY: source description]`.

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

FAIL_UNANCHORED_SCORE: any score outside 0–3 or Evidence cell does not cite a level.

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
not assigned.

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
FAIL_WRONG_CHANNEL: any row uses a channel not listed as Primary or Fallback for its Frame Type.

---

### Step 6b: Communication strategy per quadrant — PM role

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

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned to Displacement | Audit Result |
|--------------------|------------------------------------|------------------------------------|------------------------------|--------------|
| [name] | [anchor from Step 6b row] | [row1: anchor; row2: anchor] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: any inertia-tagged stakeholder's displacement-acknowledgment
row does not carry the T+0 baseline timing anchor.

---

### Step 6e-priority: Comms priority band prefill — PM role

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Engagement window closes within the current sprint cycle; any delay risks losing the window | Owner must schedule within 48 hours of plan publication |
| STANDARD | Engagement window extends beyond the current sprint; preferred timing within 1–2 cycles | Owner schedules at next available touchpoint within window |
| DEFERRED | No forcing function; timing is fully opportunistic | Owner documents intended timing; no hard scheduling obligation |

FAIL_UNCALIBRATED_PRIORITY: any Step 6b comms row carries a Priority Band value not
drawn from this prefill.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing a comms row, blocking reason, or lead
time violation.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible targets: Phase 3 grid rows, Step 4b veto
entries, Step 6a frame type assignments, Step 6b comms rows, Step 6e-priority bands,
Step 2c gatekeeper lead-time tags, Step 2a conflict resolution entries, Step 2a
escalation tier entries, trajectory assessments, velocity assessments, engagement window
derivations, champion depth scores, synthesis rows.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [structural artifact + row identifier] | [specific change applied] | [confirmed artifact reference with date, OR "not-yet: [named owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.
FAIL_UNVERIFIED_AMENDMENT: any row has a populated Change Made cell but Verification cell
is absent, blank, or carries "not-yet" without named owner and deadline.

Mandatory ASSUMED amendment obligation: all Source cells annotated ASSUMED are mandatory
targets. Each must carry a populated Verification cell.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |
| [name from Phase 3] | no | [documented reason] |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from Step 9 synthesis without justification.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [Step 0b entry or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking inline step citation.
FAIL_SYNTHESIS_GAP: any Step 8b stakeholder absent without documented justification.

---

### Step 9b: Synthesis depth audit matrix — PM role

OUTPUT FORMAT NOTE: This audit matrix is a checksum layer over Step 9, not a restatement
of it. Each cell carries only the audit result — PASS, FAIL, or N/A:[code] — not the
field value itself. This format enables column-pattern detection (a field consistently
absent = structural synthesis gap) and row-pattern detection (multiple FAILs on one
stakeholder = evidence inadequacy).

Permitted N/A reason codes: NO-CONFLICT, NO-CHAMPION-ROLE, MONITOR-ONLY,
NO-COMPETITOR-CONTEXT. Any other justification is not a permitted N/A.

A field is PASS if it carries substantive content in Step 9.
A field is FAIL if it contains only "N/A", "—", "Not applicable", or a placeholder
equivalent with no documented reason code.
A field is N/A:[code] if it carries an undocumented absence with a permitted reason code.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [name] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] |

FAIL_SHALLOW_SYNTHESIS: any cell in this matrix carries FAIL status.
Distinct from FAIL_NO_SYNTHESIS (C-32): FAIL_NO_SYNTHESIS fires when the synthesis step
is absent or a required field column is structurally missing; FAIL_SHALLOW_SYNTHESIS fires
when all fields are structurally present but one carries undocumented N/A or placeholder.
Distinct from FAIL_SYNTHESIS_GAP (C-42): FAIL_SYNTHESIS_GAP fires when a stakeholder row
is absent from synthesis; FAIL_SHALLOW_SYNTHESIS fires when a row is present but a field
within it is functionally empty.
```

---

## V-03 — Inertia Framing: Competitor Response Track

**Axis**: Inertia framing — Response Track (CONVERT/CONTAIN/CO-EXIST) is elevated from a column annotation to a planning instrument. Step 0b gains a Response Track column. A new Step 0c "Response Track engagement obligations" table translates each track into explicit engagement objective, success criterion, and downstream message requirement before Phase 1 begins. Step 2b gains a Response Track column. Step 6b displacement-acknowledgment messages are checked against Step 0c requirements. Step 9 Competitor field cites both competitor name and Response Track.

**Hypothesis**: R19 V-03 added Response Track as a Step 0b column. R20 V-03 promotes it to a planning layer by adding Step 0c, which forces the model to articulate what CONVERT/CONTAIN/CO-EXIST means as an engagement obligation before analyzing stakeholders. This makes strategic intent structurally primary in the inertia analysis chain: a CO-EXIST competitor that receives a CONVERT-framed displacement-acknowledgment message fires FAIL_RESPONSE_TRACK_ALIGNMENT at Step 6b via the Step 0c obligation spec, not just as a labeling error but as a content-alignment failure. The three tracks have qualitatively different message requirements; Step 0c makes these requirements concrete and checkable.

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
before Phase 1 begins.

FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Before Phase 1, name each workflow or tool this feature displaces as a first-class
competitor. Assign three prefill-calibrated attributes per entry.

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

Response Track prefill:

| Response Track | Strategic Intent | Engagement Goal |
|----------------|-----------------|-----------------|
| CONVERT | Move inertia stakeholders from current approach to new feature; displacement is the goal | Adoption; success = stakeholder migrated, current approach retired or deprecated |
| CONTAIN | Limit growth of current approach while new feature matures; coexistence is transitional | Boundary enforcement; success = current approach usage does not expand; checkpoint scheduled |
| CO-EXIST | Current approach and new feature serve different enough needs that permanent coexistence is acceptable | Clarity; success = stakeholders understand boundary conditions and do not experience replacement anxiety |

Competitor inventory table:

| Competitor | Description | Adoption Band | Switching Cost Band | Response Track |
|------------|-------------|---------------|---------------------|----------------|
| [displaced workflow or tool] | [what it does that this feature replaces] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW | CONVERT / CONTAIN / CO-EXIST |

FAIL_NO_COMPETITOR_ENTRY: an inertia-tagged stakeholder appears in Step 2b but no
corresponding entry names the workflow or tool they represent.
FAIL_NO_RESPONSE_TRACK: any competitor entry lacks a Response Track value drawn from the
Response Track prefill (e.g., blank cell, free-form strategy description, or ad hoc label).
Distinct from FAIL_NO_COMPETITOR_ENTRY: FAIL_NO_COMPETITOR_ENTRY fires when the competitor
entry is absent; FAIL_NO_RESPONSE_TRACK fires when the entry is present but lacks a track.

---

### Step 0c: Response Track engagement obligations — Strategy role

INERTIA FRAMING NOTE: Before Phase 1, translate each assigned Response Track from Step 0b
into explicit engagement obligations. These obligations govern what displacement-
acknowledgment messages MUST contain in Step 6b. A message that fails to satisfy its
track's downstream message requirement fires FAIL_RESPONSE_TRACK_ALIGNMENT at Step 6b.

| Competitor | Response Track | Engagement Objective | Success Criterion | Downstream Message Requirement |
|------------|----------------|---------------------|------------------|---------------------------------|
| [name from Step 0b] | CONVERT / CONTAIN / CO-EXIST | [what this track aims to achieve for this competitor] | [observable signal confirming track success] | [what displacement-acknowledgment message must explicitly include] |

Response Track downstream message requirements (mandatory content per track):
- CONVERT: displacement-acknowledgment message MUST include (a) a named conversion path
  identifying the migration route and (b) a migration milestone with a specific date or
  sprint target. A message lacking either element carries FAIL_RESPONSE_TRACK_ALIGNMENT.
- CONTAIN: displacement-acknowledgment message MUST include (a) a containment boundary
  defining where the current approach remains permitted and (b) a review checkpoint date
  when the boundary will be reassessed. A message lacking either carries
  FAIL_RESPONSE_TRACK_ALIGNMENT.
- CO-EXIST: displacement-acknowledgment message MUST (a) explicitly clarify boundary
  conditions distinguishing when to use each approach and (b) avoid any language implying
  that the current approach will be replaced or deprecated. A message violating either
  carries FAIL_RESPONSE_TRACK_ALIGNMENT.

FAIL_RESPONSE_TRACK_ALIGNMENT: any displacement-acknowledgment comms row for a CONVERT,
CONTAIN, or CO-EXIST competitor does not satisfy the corresponding downstream message
requirement from this table. Distinct from FAIL_MISSING_DISPLACEMENT_PREFILL (C-29):
C-29 fires when displacement-acknowledgment frame type is not assigned; FAIL_RESPONSE_TRACK_
ALIGNMENT fires when the frame type is correctly assigned but message content does not
satisfy the track-specific obligation from Step 0c.

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
| CRITICAL | Conflict blocks the decision entirely or forces a restart if unresolved by deadline; no workaround exists | Escalation Owner must be activated before deadline; delay is not recoverable |
| SIGNIFICANT | Conflict delays the decision or degrades its quality if unresolved; a workaround exists but carries cost | Escalation Owner activated if deadline passes; cost must be documented |
| MANAGEABLE | Conflict resolves within normal process; timeline impact is unlikely even without escalation | No escalation activation required; monitor and confirm at next checkpoint |

FAIL_UNCALIBRATED_SEVERITY: any Step 2a conflict row carries a Severity Band value not
drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. Party anchor rule: each Party A and Party B
must either match a Phase 1 segment name verbatim or carry an `[ORG-ROLE: description]` tag.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | budget / timeline / scope / authority / methodology | CRITICAL / SIGNIFICANT / MANAGEABLE | [named authority] | [ruling needed] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: Resolution Authority, Decision Required, or Deadline absent.
FAIL_NO_ESCALATION_PATH: no escalation tier row with named owner and trigger.
FAIL_UNANCHORED_CONFLICT_PARTY: party not traceable to Phase 1 segment or ORG-ROLE tag.
FAIL_UNCALIBRATED_SEVERITY: Severity Band value not drawn from Step 2a-prefill.

---

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor | Response Track |
|-------------|-----------------|--------------|-------------------|--------------------|----------------|
| [name] | [current approach disrupted] | [what this feature replaces] | [yes / limited / no] | [competitor name from Step 0b] | [CONVERT / CONTAIN / CO-EXIST from Step 0b entry] |

Inertia stakeholders must appear in Phase 3 grid with `[INERTIA]` in Notes.
They must receive `displacement-acknowledgment` Frame Type in Step 6b.
The Response Track cell must match the track assigned to the Step 0b Competitor entry.

FAIL_NO_INERTIA: no inertia stakeholders identified when feature displaces existing workflow.
FAIL_NO_COMPETITOR_ENTRY: inertia stakeholder's Step 0b Competitor cell blank or not in inventory.
FAIL_NO_RESPONSE_TRACK: Response Track cell blank or not drawn from Step 0b prefill.

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

Each Source cell must carry: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: any Source cell present and populated but lacking typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | [INERTIA] if applicable |

ASSUMED Source entries are mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE: as defined above.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto |
| MED | 30–70% | Conditional veto |
| LOW | < 30% | Unlikely veto |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a band not from this prefill.

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH first, then MED, then LOW.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY: as defined above.

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

FAIL_UNANCHORED_SCORE: any score outside 0–3 or Evidence cell does not cite a level.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [behavioral evidence] |
| Proximity | [0–3] | level [N]: [behavioral evidence] |
| Commitment | [0–3] | level [N]: [behavioral evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE: as defined above.

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
Rule 4: `displacement-acknowledgment` message content must satisfy the downstream message
requirement for the stakeholder's Response Track as defined in Step 0c.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned.

---

### Step 6c: Channel binding prefill — PM role

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (no fallback; meeting required) |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL: as defined above.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c. Timing anchors must
fall within Step 5a derived engagement windows. Priority Band draws from Step 6e-priority.
Displacement-acknowledgment messages must satisfy Step 0c track requirements (FAIL_RESPONSE_
TRACK_ALIGNMENT fires if CONVERT/CONTAIN/CO-EXIST message obligations are not met).

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [relative anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [track-aligned message: see Step 0c] | [relative anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL: as defined above.
FAIL_RESPONSE_TRACK_ALIGNMENT: displacement-acknowledgment message does not satisfy the
downstream message requirement for its Response Track from Step 0c.

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
| URGENT | Engagement window closes within the current sprint cycle | Owner must schedule within 48 hours |
| STANDARD | Engagement window extends beyond the current sprint | Owner schedules at next touchpoint within window |
| DEFERRED | No forcing function; timing fully opportunistic | Owner documents intended timing |

FAIL_UNCALIBRATED_PRIORITY: any Step 6b comms row carries a Priority Band value not
drawn from this prefill.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing a comms row, blocking reason, or lead
time violation.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible targets: Phase 3 grid rows, Step 4b veto
entries, Step 6a assignments, Step 6b comms rows, Step 6e-priority bands, Step 2c
gatekeeper tags, Step 2a conflict entries, Step 2a escalation entries, trajectory
assessments, velocity assessments, engagement window derivations, champion depth scores,
synthesis rows.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [structural artifact + row identifier] | [specific change applied] | [confirmed artifact reference with date, OR "not-yet: [named owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target.
FAIL_UNVERIFIED_AMENDMENT: Change Made populated but Verification absent or incomplete.

Mandatory ASSUMED amendment obligation: all Source cells annotated ASSUMED are mandatory
targets. Each must carry a populated Verification cell.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name from Phase 3] | yes | — |

FAIL_SYNTHESIS_GAP: any grid stakeholder absent from Step 9 synthesis without justification.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution required: `field: value (Step X)`.
Competitor field must cite both competitor name and Response Track.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [name] [CONVERT/CONTAIN/CO-EXIST] (Step 0b) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP: as defined above.
```

---

## V-04 — V-01 + V-02 Combined

**Axis**: Role sequence (Step 3c-staleness before Step 3b-prefill) + Output format (Step 9b transposed matrix). These operate at independent structural positions — temporal qualification in Phase 3 setup and audit in Step 9b post-synthesis — and are mutually non-interfering.

**Hypothesis**: V-01 establishes that temporal reliability is primary in source qualification. V-02 establishes that synthesis audit results should be discrete checksum values, not embedded prose. Combined, these create a two-layer source-quality accountability chain: staleness is calibrated before evidence is classified (V-01), and the synthesis representation of that evidence is audited for depth post-synthesis (V-02). The combination surfaces whether EXPIRED-reclassified ASSUMED entries (Step 8 mandatory targets from V-01) result in substantive synthesis content or placeholder values that fire FAIL_SHALLOW_SYNTHESIS (V-02).

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
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output terminal state as `[STATE: ...]` before Phase 1 begins.

FAIL_SILENT_INFERENCE / FAIL_WRONG_STATE: as defined above.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | > 70% of affected stakeholders; active migration required |
| ACTIVE | 30–70%; coexists with alternatives; incremental switching |
| MARGINAL | < 30%; already declining or partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Requires retraining, data migration, or process redesign |
| MEDIUM | Requires workflow adjustment and communication |
| LOW | Self-service or transparent; minimal stakeholder action |

| Competitor | Description | Adoption Band | Switching Cost Band |
|------------|-------------|---------------|---------------------|
| [displaced workflow or tool] | [what it replaces] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW |

FAIL_NO_COMPETITOR_ENTRY: inertia-tagged stakeholder appears in Step 2b but no inventory entry.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [pattern] | [touchpoints] | [NOT-doing statement] | [gatekeeper / inertia / neither] |

FAIL_MONOLITH_ASSUMPTION / FAIL_NO_NOT_DOING: as defined above.

---

### Phase 1 → Phase 2 Transition Gate

- [ ] At least two distinct user segments
- [ ] NOT-doing present for each segment
- [ ] Inertia segment displacement NOT-doing addressed

FAIL_INCOMPLETE_PHASE1: any required output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision entirely; no workaround | Escalation Owner activated before deadline |
| SIGNIFICANT | Delays decision; workaround exists but carries cost | Escalation Owner activated if deadline passes |
| MANAGEABLE | Resolves within normal process | No escalation required; monitor |

FAIL_UNCALIBRATED_SEVERITY: Severity Band not drawn from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, escalation tiers

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | [nature] | CRITICAL / SIGNIFICANT / MANAGEABLE | [authority] | [ruling] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY: as defined above.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name] | [current approach] | [displaced by] | [yes / limited / no] | [competitor from Step 0b] |

FAIL_NO_INERTIA / FAIL_NO_COMPETITOR_ENTRY: as defined above.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [lead time] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 2 → Phase 3 Transition Gate

- [ ] At least two structural conflicts complete
- [ ] At least one inertia stakeholder or no-displacement statement
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Trajectory changing faster than baseline; new signals in last review cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Expected touchpoints, no withdrawals |
| DECELERATING | Engagement thinning or sentiment shifting | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: Velocity label absent or not from this prefill.

---

### Step 3c-staleness: Source staleness band prefill — PM role

ROLE SEQUENCE NOTE: This step precedes Step 3b-prefill (source typology). Temporal
reliability is established before epistemic basis classification. EXPIRED sources should
be tentatively reclassified as ASSUMED in Step 3b if no refresh is available.

| Staleness Band | Criteria | Reliability Implication |
|----------------|----------|------------------------|
| CURRENT | Confirmed or refreshed within current sprint cycle (< 14 days) | Load-bearing; use without qualification |
| STALE | Confirmed 15–60 days ago; no refresh since prior sprint | Indicative only; flag for validation |
| EXPIRED | Confirmed > 60 days ago, or one-time observation with no follow-up | Unreliable; mandatory Step 8 amendment target |

Each Source Age cell in Phase 3 must carry exactly one label from this table.

FAIL_UNCALIBRATED_STALENESS: Source Age value not drawn from this prefill.

---

### Step 3b-prefill: Source typology — PM role

ROLE SEQUENCE NOTE: This step follows Step 3c-staleness. EXPIRED sources should be
classified as ASSUMED unless a refreshed artifact is available.

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact exists | None — confirm at Step 8 if EXPIRED |
| INFERRED | Reasoned from pattern or adjacent signal | Flag for validation at next touchpoint |
| ASSUMED | No direct evidence; based on role stereotype | Mandatory Step 8 amendment target |

Each Source cell must carry: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: Source cell lacking typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

ASSUMED entries and EXPIRED Source Age entries are mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE / FAIL_UNCALIBRATED_STALENESS:
as defined above.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto |
| MED | 30–70% | Conditional veto |
| LOW | < 30% | Unlikely veto |

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH → MED → LOW.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY: as defined above.

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
| [name] | [standing] | [calendar-ready commitment] |

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory influence | Occasional touchpoint | Verbal interest; no commitment |
| 2 | Named participant; can advance or delay | Regular loop; async channel | Documented commitment with schedulable action |
| 3 | Final authority or veto power | Peer-level; synchronous on request | Committed with deadline, accountability, contingency |

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE: as defined above.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or SPOF risk] |
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

Rule 1–3: as defined above.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but frame type not assigned.

---

### Step 6c: Channel binding prefill — PM role

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL: as defined above.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current approach first] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL: as above.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned | Audit Result |
|--------------------|------------------------------------|------------------------------------|--------------|--------------|
| [name] | [anchor] | [row1: anchor] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment not at T+0.

---

### Step 6e-priority: Comms priority band prefill — PM role

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint | Schedule within 48 hours |
| STANDARD | Window extends past current sprint | Next touchpoint within window |
| DEFERRED | No forcing function | Document intended timing |

FAIL_UNCALIBRATED_PRIORITY: Priority Band not drawn from this prefill.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper incomplete.

---

### Step 8: Amendment phase — PM role

Minimum one amendment. Eligible targets: Phase 3 grid rows, Step 4b entries, Step 6a
assignments, Step 6b rows, Step 6e-priority bands, Step 2c tags, Step 2a entries,
trajectory/velocity/source age assessments, engagement window derivations, champion
scores, synthesis rows.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row id] | [change applied] | [confirmed ref with date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY / FAIL_UNVERIFIED_AMENDMENT: as defined above.

Mandatory ASSUMED amendment obligation: all ASSUMED Source cells are mandatory targets.
Mandatory EXPIRED amendment obligation: all EXPIRED Source Age cells are mandatory targets.
Each must carry a populated Verification cell.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes | — |

FAIL_SYNTHESIS_GAP: stakeholder absent from Step 9 without justification.

---

### Step 9: Cross-phase synthesis readout — PM role

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [Step 0b entry or N/A] (Step 0b) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP: as defined above.

---

### Step 9b: Synthesis depth audit matrix — PM role

OUTPUT FORMAT NOTE: Each cell carries only the audit result — PASS, FAIL, or N/A:[code].
Permitted N/A reason codes: NO-CONFLICT, NO-CHAMPION-ROLE, MONITOR-ONLY,
NO-COMPETITOR-CONTEXT.

PASS = substantive content in Step 9 field.
FAIL = functionally empty (undocumented N/A, dash, placeholder).
N/A:[code] = absence documented with permitted reason code.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [name] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] |

FAIL_SHALLOW_SYNTHESIS: any cell carries FAIL status.
```

---

## V-05 — V-01 + V-02 + V-03 Combined (GOLDEN)

**Axis**: Role sequence (Step 3c before Step 3b) + Output format (Step 9b matrix) + Inertia framing (Step 0c Response Track engagement obligations). All three axes simultaneously.

**Hypothesis**: V-05 combines temporal-primary source qualification (V-01), checksum synthesis audit (V-02), and planning-instrument Response Track (V-03). The three criteria are mutually non-interfering: C-51 operates at Phase 3 setup, C-52 operates at Step 9b post-synthesis, C-53 operates at Step 0b/0c/2b/6b. Combined, they create a complete accountability chain: evidence is temporally and epistemically qualified before the grid is built (C-51), strategic intent is declared before stakeholder analysis begins (C-53), and synthesis depth is audited with a discrete checksum after synthesis is produced (C-52). This is the target golden prompt for Round 20.

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
| 0.2 | CODEOWNERS absent; invocation string contains team or org identifiers | Extract org context | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask exactly one question: "What org or team is this decision for?" Halt | ORG-BLOCKED |

Output terminal state as `[STATE: ...]` before Phase 1 begins.

FAIL_SILENT_INFERENCE / FAIL_WRONG_STATE: as defined above.

---

### Step 0b: Status-quo competitor inventory — Strategy role

Before Phase 1, name each workflow or tool this feature displaces. Assign three
prefill-calibrated attributes per entry.

Adoption Band prefill:

| Adoption Band | Criteria |
|---------------|----------|
| DOMINANT | > 70% of affected stakeholders; active migration required |
| ACTIVE | 30–70%; coexists with alternatives; incremental switching |
| MARGINAL | < 30%; already declining or partially replaced |

Switching Cost Band prefill:

| Switching Cost Band | Criteria |
|--------------------|----------|
| HIGH | Requires retraining, data migration, or process redesign |
| MEDIUM | Requires workflow adjustment and communication |
| LOW | Self-service or transparent; minimal stakeholder action |

Response Track prefill:

| Response Track | Strategic Intent | Engagement Goal |
|----------------|-----------------|-----------------|
| CONVERT | Move inertia stakeholders from current approach to new feature | Adoption; success = migrated, current approach retired |
| CONTAIN | Limit growth of current approach while new feature matures | Boundary enforcement; success = no expansion, checkpoint scheduled |
| CO-EXIST | Permanent coexistence acceptable; different enough needs | Clarity; success = boundary conditions understood, no replacement anxiety |

| Competitor | Description | Adoption Band | Switching Cost Band | Response Track |
|------------|-------------|---------------|---------------------|----------------|
| [displaced workflow or tool] | [what it replaces] | DOMINANT / ACTIVE / MARGINAL | HIGH / MEDIUM / LOW | CONVERT / CONTAIN / CO-EXIST |

FAIL_NO_COMPETITOR_ENTRY: inertia-tagged stakeholder in Step 2b but no inventory entry.
FAIL_NO_RESPONSE_TRACK: competitor entry present but Response Track absent or uncalibrated.

---

### Step 0c: Response Track engagement obligations — Strategy role

INERTIA FRAMING NOTE: Before Phase 1, translate each Response Track into explicit
engagement obligations. Step 6b displacement-acknowledgment messages are checked against
these requirements. FAIL_RESPONSE_TRACK_ALIGNMENT fires at Step 6b when content does not
satisfy the downstream message requirement.

| Competitor | Response Track | Engagement Objective | Success Criterion | Downstream Message Requirement |
|------------|----------------|---------------------|------------------|---------------------------------|
| [name] | CONVERT / CONTAIN / CO-EXIST | [what this track aims to achieve] | [observable success signal] | [what displacement-acknowledgment must include] |

Downstream message requirements per track:
- CONVERT: message MUST include (a) named conversion path + (b) migration milestone with date.
- CONTAIN: message MUST include (a) containment boundary + (b) review checkpoint date.
- CO-EXIST: message MUST (a) clarify boundary conditions + (b) avoid replacement language.

FAIL_RESPONSE_TRACK_ALIGNMENT: displacement-acknowledgment message fails track requirement.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [pattern] | [touchpoints] | [NOT-doing statement] | [gatekeeper / inertia / neither] |

FAIL_MONOLITH_ASSUMPTION / FAIL_NO_NOT_DOING: as defined above.

---

### Phase 1 → Phase 2 Transition Gate

- [ ] At least two distinct user segments
- [ ] NOT-doing present for each
- [ ] Inertia displacement NOT-doing addressed

FAIL_INCOMPLETE_PHASE1: any output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria | Escalation Implication |
|---------------|----------|------------------------|
| CRITICAL | Blocks decision; no workaround | Escalation Owner activated before deadline |
| SIGNIFICANT | Delays decision; workaround exists | Escalation Owner activated if deadline passes |
| MANAGEABLE | Resolves within normal process | No escalation required |

FAIL_UNCALIBRATED_SEVERITY: Severity Band not from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, escalation tiers

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment OR ORG-ROLE: desc] | [Phase 1 segment OR ORG-ROLE: desc] | [nature] | CRITICAL / SIGNIFICANT / MANAGEABLE | [authority] | [ruling] | [deadline] |

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|
| [name] | [named person above Resolution Authority] | [condition] | [action] |

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY: as defined above.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor | Response Track |
|-------------|-----------------|--------------|-------------------|--------------------|----------------|
| [name] | [current approach] | [displaced by] | [yes / limited / no] | [competitor from Step 0b] | [CONVERT / CONTAIN / CO-EXIST from Step 0b] |

FAIL_NO_INERTIA / FAIL_NO_COMPETITOR_ENTRY / FAIL_NO_RESPONSE_TRACK: as defined above.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [lead time] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 2 → Phase 3 Transition Gate

- [ ] At least two structural conflicts complete
- [ ] At least one inertia stakeholder or no-displacement statement
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill — PM role

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Changing faster than baseline; new signals in last review cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Expected touchpoints, no withdrawals |
| DECELERATING | Engagement thinning or shifting | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: label absent or not from this prefill.

---

### Step 3c-staleness: Source staleness band prefill — PM role

ROLE SEQUENCE NOTE: This step precedes Step 3b-prefill. Temporal reliability is
established before epistemic basis classification. EXPIRED sources should be tentatively
reclassified as ASSUMED in Step 3b if no refresh is available.

| Staleness Band | Criteria | Reliability Implication |
|----------------|----------|------------------------|
| CURRENT | Confirmed or refreshed within current sprint (< 14 days) | Load-bearing; use without qualification |
| STALE | Confirmed 15–60 days ago; no refresh since prior sprint | Indicative only; flag for validation |
| EXPIRED | Confirmed > 60 days ago, or one-time observation without follow-up | Unreliable; mandatory Step 8 amendment target |

Each Source Age cell in Phase 3 must carry exactly one label from this table.

FAIL_UNCALIBRATED_STALENESS: Source Age absent or not drawn from this prefill.

---

### Step 3b-prefill: Source typology — PM role

ROLE SEQUENCE NOTE: Follows Step 3c-staleness. EXPIRED sources tentatively classified
as ASSUMED unless a refreshed artifact is available.

| Typology | Criteria | Amendment Obligation |
|----------|----------|---------------------|
| OBSERVED | Directly witnessed; citable artifact exists | None — confirm at Step 8 if EXPIRED |
| INFERRED | Reasoned from pattern or adjacent signal | Flag for validation at next touchpoint |
| ASSUMED | No direct evidence; based on role stereotype | Mandatory Step 8 amendment target |

Each Source cell must carry: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: Source cell lacking typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

ASSUMED entries and EXPIRED Source Age entries are mandatory Step 8 amendment targets.

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE / FAIL_UNCALIBRATED_STALENESS:
as defined above.

---

### Step 4a: Veto probability band prefill — PM role

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto |
| MED | 30–70% | Conditional veto |
| LOW | < 30% | Unlikely veto |

---

### Step 4b: Veto risk ranking — PM role

Order: HIGH → MED → LOW.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [consequence] | [mitigation] |

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY: as defined above.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not in grid.

---

### Step 5b: Champion identification — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory influence | Occasional touchpoint | Verbal interest; no commitment |
| 2 | Named participant; can advance or delay | Regular loop; async channel | Documented with schedulable action |
| 3 | Final authority or veto | Peer-level; synchronous on request | Committed with deadline, accountability, contingency |

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0–3] | level [N]: [evidence] |
| Proximity | [0–3] | level [N]: [evidence] |
| Commitment | [0–3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE: as defined above.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or SPOF risk] |
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

Rule 1: Each Step 6b row must use a Frame Type from this table.
Rule 2: `displacement-acknowledgment` mandatory for every inertia-tagged stakeholder.
Rule 3: `displacement-acknowledgment` messages must preserve current approach before describing new.
Rule 4: `displacement-acknowledgment` content must satisfy Step 0c track requirements.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but frame type not assigned.

---

### Step 6c: Channel binding prefill — PM role

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL: as defined above.

---

### Step 6b: Communication strategy per quadrant — PM role

Displacement-acknowledgment messages must satisfy Step 0c track requirements.
FAIL_RESPONSE_TRACK_ALIGNMENT fires when CONVERT/CONTAIN/CO-EXIST obligations unmet.

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | URGENT / STANDARD / DEFERRED |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [track-aligned; see Step 0c] | [anchor] | URGENT / STANDARD / DEFERRED |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL /
FAIL_RESPONSE_TRACK_ALIGNMENT: as defined above.

---

### Step 6d-sequence: Displacement comms sequence audit — PM role

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned | Audit Result |
|--------------------|------------------------------------|------------------------------------|--------------|--------------|
| [name] | [anchor] | [row1: anchor] | yes / no | PASS / FAIL |

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment not at T+0.

---

### Step 6e-priority: Comms priority band prefill — PM role

| Priority Band | Scheduling Criteria | Resource Implication |
|---------------|--------------------|--------------------|
| URGENT | Window closes within current sprint | Schedule within 48 hours |
| STANDARD | Window extends past current sprint | Next touchpoint within window |
| DEFERRED | No forcing function | Document intended timing |

FAIL_UNCALIBRATED_PRIORITY: Priority Band not from this prefill.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper incomplete.

---

### Step 8: Amendment phase — PM role

Minimum one amendment. Eligible targets: Phase 3 grid rows, Step 4b entries, Step 6a
assignments, Step 6b rows, Step 6e-priority bands, Step 2c tags, Step 2a entries,
trajectory/velocity/source age assessments, engagement window derivations, champion
scores, synthesis rows.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row id] | [change applied] | [confirmed ref with date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY / FAIL_UNVERIFIED_AMENDMENT: as defined above.

Mandatory ASSUMED amendment obligation: all ASSUMED Source cells are mandatory targets.
Each must carry a populated Verification cell.
Mandatory EXPIRED amendment obligation: all EXPIRED Source Age cells are mandatory targets.
Each must carry a populated Verification cell confirming reclassification or documenting
unresolved status with owner and deadline.

---

### Step 8b: Synthesis coverage audit — PM role

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|
| [name] | yes | — |

FAIL_SYNTHESIS_GAP: stakeholder absent from Step 9 without justification.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution required: `field: value (Step X)`.
Competitor field must cite competitor name and Response Track.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [name] [CONVERT/CONTAIN/CO-EXIST] (Step 0b) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP: as defined above.

---

### Step 9b: Synthesis depth audit matrix — PM role

OUTPUT FORMAT NOTE: Each cell carries only the audit result — PASS, FAIL, or N/A:[code].
Permitted N/A reason codes: NO-CONFLICT, NO-CHAMPION-ROLE, MONITOR-ONLY,
NO-COMPETITOR-CONTEXT.

PASS = substantive content present in Step 9.
FAIL = functionally empty (undocumented N/A, dash, placeholder with no justification).
N/A:[code] = absence documented with a permitted reason code.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [name] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] |

FAIL_SHALLOW_SYNTHESIS: any cell carries FAIL status.
Distinct from FAIL_NO_SYNTHESIS (C-32) and FAIL_SYNTHESIS_GAP (C-42): as defined above.
```
