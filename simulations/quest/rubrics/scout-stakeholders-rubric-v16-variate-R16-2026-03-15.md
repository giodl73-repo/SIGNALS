## Round 16 Variations — scout-stakeholders

**Target rubric**: v16 (max 260 pts)
**Baseline**: R15 V-05 (260/260 under v16 — first perfect score)
**Goal**: All five variations include C-40 + C-41 + C-42 (mandatory for 260/260 under v16). Explore three new structural axes as candidates for C-43/C-44/C-45 in v17.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence: UX → Strategy → PM | Running UX segment analysis before Strategy conflict identification forces conflict parties to reference observed user segments; FAIL_UNANCHORED_CONFLICT_PARTY is a new gate distinct from FAIL_ONE_PARTY |
| V-02 | Champion scoring: behavioral anchor prefill | Replacing the 1-5 free scale with a 0-3 behavioral anchor prefill mirrors the C-38 and C-41 calibration pattern; FAIL_UNANCHORED_SCORE is a new gate distinct from FAIL_BELOW_CHAMPION_THRESHOLD |
| V-03 | Inertia front-loading with risk score | Moving inertia pre-assessment to Step 0b (before Phase 1) and requiring the risk score in Step 9 synthesis rows for inertia stakeholders creates a cross-phase traceability obligation; FAIL_STALE_INERTIA_SCORE is a new gate |
| V-04 | V-01 + V-02 combined | Role sequence inversion and behavioral anchor scoring operate at different phases (Phase 1 UX pre-step vs Step 5b-anchor); they are mutually non-interfering |
| V-05 | V-01 + V-02 + V-03 combined | All three new axes simultaneously; maximum structural density for Round 16 discovery |

---

## V-01 — Role Sequence: UX First

**Axis**: Phase execution order changes from Strategy → UX → PM to UX → Strategy → PM. Phase 1 is now UX (segment analysis). Phase 2 is Strategy (conflicts, inertia, gatekeepers). Party columns in Step 2a must each reference a Phase 1 segment name or bear an explicit `[ORG-ROLE]` tag with a role description.

**Hypothesis**: Running UX segment analysis before conflict identification grounds each conflict party in an observed user segment or explicitly documented org role. A conflict party named as a generic group (e.g., "Engineering") without a Phase 1 segment reference or ORG-ROLE tag cannot be traced to any empirically identified constituency. FAIL_UNANCHORED_CONFLICT_PARTY fires when a Party column names a group that neither matches a Phase 1 segment name nor carries an `[ORG-ROLE: description]` tag. This obligation is entirely orthogonal to FAIL_ONE_PARTY: FAIL_ONE_PARTY fires when only one party is present; FAIL_UNANCHORED_CONFLICT_PARTY fires when two parties are present but neither is anchored to a Phase 1 segment or documented org role.

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

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Party anchor rule: Each Party A and Party B cell must either (a) match a segment name
from Phase 1 verbatim, or (b) carry an `[ORG-ROLE: description]` tag identifying an
org role not captured as a user segment.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment name OR ORG-ROLE: description] | [Phase 1 segment name OR ORG-ROLE: description] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

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

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group — must match a Phase 1 segment or carry ORG-ROLE tag] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two anchored parties, nature, and complete
      resolution pathway entry
- [ ] Escalation tier row present for each conflict (Escalation Owner + Trigger)
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

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

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band labels.

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
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived windows.

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
that violates Step 2c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 2c gatekeeper lead-time tags, conflict
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
a documented justification in this table. FAIL_SYNTHESIS_GAP is distinct from
FAIL_NO_SYNTHESIS: FAIL_SYNTHESIS_GAP fires when synthesis exists but silently omits a
grid stakeholder.

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
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 2a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-02 — Champion Scoring: Behavioral Anchor Prefill

**Axis**: Step 5b-anchor prefill is inserted before Step 5c, defining exactly four behavioral levels (0 = absent, 1 = emergent, 2 = established, 3 = definitive) with explicit behavioral descriptors for each of the three champion dimensions (Authority, Proximity, Commitment). Step 5c uses the anchored 0-3 scale exclusively. The composite gate is >= 6 (of 9 max). FAIL_UNANCHORED_SCORE fires when any dimension score in Step 5c is assigned without citing a level from the Step 5b-anchor prefill.

**Hypothesis**: The baseline 1-5 free scale for champion scoring requires no behavioral anchor — any integer in 1-5 is valid regardless of whether observed behaviors support it. A Step 5b-anchor prefill mirrors the structure of Step 4a (C-38) and Step 3a (C-41) but applies to champion depth dimensions rather than veto probability or trajectory velocity. FAIL_UNANCHORED_SCORE is a new gate distinct from FAIL_BELOW_CHAMPION_THRESHOLD: FAIL_BELOW_CHAMPION_THRESHOLD fires when the composite is below threshold; FAIL_UNANCHORED_SCORE fires when a score is assigned outside the prefill vocabulary or without citing a behavioral level — a violation that can occur even when the composite satisfies the threshold. A variation that satisfies FAIL_BELOW_CHAMPION_THRESHOLD by producing a composite >= 6 using free-form 1-5 scores not tied to behavioral anchors = FAIL_BELOW_CHAMPION_THRESHOLD not fired, FAIL_UNANCHORED_SCORE fires.

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

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band labels.

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

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

All Step 5c dimension scores must draw from this table. Assign the level whose behavioral
descriptor best matches observed evidence. Cite the level number in the Evidence cell.

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority over this decision | No direct contact channel; third-party relay only | No documented statement of support |
| 1 | Advisory influence; can surface concerns but cannot advance or close | Occasional touchpoint; not in regular decision loop | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant or sponsor; can advance or delay but not close unilaterally | In regular decision loop; direct async channel established | Documented commitment with schedulable action and named owner |
| 3 | Final decision authority or veto power; can block, advance, or close unilaterally | Peer-level relationship; synchronous channel available on request | Committed with deadline, named accountability, and contingency if unavailable |

FAIL_UNANCHORED_SCORE: any Step 5c dimension score is outside 0-3, or the Evidence cell
does not cite a level from this prefill table.

---

### Step 5c: Champion depth scoring — PM role

Scores must be drawn from the Step 5b-anchor prefill. Composite gate: >= 6 (max 9).

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | | level [N]: [behavioral evidence matching that level] |
| Proximity | | level [N]: [behavioral evidence matching that level] |
| Commitment | | level [N]: [behavioral evidence matching that level] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative and no risk documented.
FAIL_UNANCHORED_SCORE: any dimension score outside 0-3 or Evidence cell does not cite a
level from the Step 5b-anchor prefill.

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
assessments, champion depth scores (with updated anchor citations), engagement window
derivations, synthesis readout rows.

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
a documented justification in this table.

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
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [composite level] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-03 — Inertia Front-Loading with Risk Score

**Axis**: Step 0b is inserted immediately after the org context state machine (Step 0), before Phase 1. Step 0b requires an Inertia Pre-Assessment table identifying displaced workflows, assigning an Inertia Risk Score (1 = low, 2 = medium, 3 = high) with calibrated band criteria, and recording coalition capacity and impact severity. The Step 0b risk score must be carried forward to the Step 9 synthesis row for each inertia-tagged stakeholder as a traceable field. FAIL_STALE_INERTIA_SCORE fires when any inertia-tagged stakeholder's Step 9 synthesis row omits the Step 0b risk score.

**Hypothesis**: Under the baseline, inertia is identified in Step 1b after conflict analysis has already framed the decision landscape. Stakeholder displacement potential is never scored before Phase 1, and no field in Step 9 traces back to an inertia risk rating. Step 0b creates an inertia risk pre-commitment that is structurally independent from the conflict resolution pathway (C-06) and the synthesis field obligations (C-32): C-06 requires conflict parties and resolution paths; C-32 requires five synthesis fields per row; neither requires a pre-Phase-1 inertia risk score to appear in synthesis. FAIL_STALE_INERTIA_SCORE is a new gate that fires when synthesis exists and satisfies C-32 (all five fields present) but inertia stakeholder rows omit the Step 0b risk score — an obligation orthogonal to per-row field completeness.

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

### Step 0b: Inertia pre-assessment — Strategy role

Before Phase 1 begins, identify displaced workflows and assign an Inertia Risk Score.
This score must be referenced in Step 9 synthesis for every inertia-tagged stakeholder.

Risk Score band definitions:

| Score | Criteria |
|-------|----------|
| 1 (Low) | Coalition capacity is low AND impact severity is low — displaced group unlikely to organize resistance or meaningfully delay the decision |
| 2 (Medium) | Coalition capacity is medium OR impact severity is medium — displaced group may organize or surface friction at key checkpoints |
| 3 (High) | Coalition capacity is high OR impact severity is high — displaced group is likely to actively block, delay, or escalate |

Inertia pre-assessment table:

| Displaced Workflow | Affected Group | Inertia Risk Score | Coalition Capacity | Impact Severity |
|--------------------|---------------|-------------------|--------------------|-----------------|
| [existing practice this decision disrupts] | [group relying on it] | 1 / 2 / 3 | high / medium / low | high / medium / low |

If no workflow is displaced, emit: `[INERTIA-NONE: this decision introduces new capability
without displacing an existing workflow or toolchain]` and proceed to Phase 1.

FAIL_NO_INERTIA_PRE_ASSESSMENT: Step 0b table absent when the decision displaces an
existing workflow.
FAIL_STALE_INERTIA_SCORE: any inertia-tagged stakeholder's Step 9 synthesis row omits
the Step 0b Inertia Risk Score.

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

Reference Step 0b risk scores. Inertia Risk Score from Step 0b must appear in the Notes
cell for each inertia stakeholder row.

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Risk Score |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] | [1 / 2 / 3 from Step 0b] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA: risk-score=N]` in
the Notes column. They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when Step 0b identified displaced
workflows. (If Step 0b emitted INERTIA-NONE, this criterion is not applicable.)

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
- [ ] At least one inertia stakeholder with Step 0b risk score (or INERTIA-NONE documented)
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
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [source] | [INERTIA: risk-score=N] if applicable |

Velocity column draws exclusively from Step 3a prefill labels.
Inertia stakeholder Notes must include the Step 0b risk score in `[INERTIA: risk-score=N]` format.

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

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band labels.

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

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived windows.

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
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first; acknowledges risk-score=N] | [relative anchor] |

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
assessments, Step 0b inertia risk scores, engagement window derivations, synthesis readout rows.

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
a documented justification in this table.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.
All stakeholders listed in Step 8b as "Synthesis Row Planned: yes" must appear here.
Inertia-tagged stakeholders must include Inertia Risk Score from Step 0b.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.
FAIL_SYNTHESIS_GAP: any stakeholder from Step 8b coverage audit absent without documented
justification.
FAIL_STALE_INERTIA_SCORE: any inertia-tagged stakeholder's synthesis row omits the Step 0b
Inertia Risk Score.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Inertia Risk Score |
|-------------|--------------|-------------------|------------------|-----------------|------------------|--------------------|
| [name — non-inertia] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) | N/A |
| [name — inertia] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: displacement-acknowledgment (Step 6a / C-13) | risk-score=[N] (Step 0b) |
```

---

## V-04 — Role Sequence + Behavioral Anchor Scoring

**Axis**: V-01 (UX → Strategy → PM sequence with FAIL_UNANCHORED_CONFLICT_PARTY) + V-02 (Step 5b-anchor prefill with FAIL_UNANCHORED_SCORE). All prior 42 criteria present. C-40, C-41, C-42 all satisfied.

**Hypothesis**: The role sequence inversion operates at the phase boundary between Phase 1 (UX) and Phase 2 (Strategy), inserting a segment-anchor obligation into conflict party identification. The behavioral anchor prefill operates at the champion scoring sub-phase (Step 5b-anchor before Step 5c), inserting a calibration obligation into depth scoring. These two structural additions share no step overlap and do not compete for the same structural slot. FAIL_UNANCHORED_CONFLICT_PARTY and FAIL_UNANCHORED_SCORE are both independently auditable and can coexist in the same rubric without definitional conflict.

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

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Party anchor rule: Each Party A and Party B cell must either (a) match a segment name
from Phase 1 verbatim, or (b) carry an `[ORG-ROLE: description]` tag identifying an
org role not captured as a user segment.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment name OR ORG-ROLE: description] | [Phase 1 segment name OR ORG-ROLE: description] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

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

#### Step 2b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group — must match a Phase 1 segment or carry ORG-ROLE tag] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two anchored parties, nature, and complete
      resolution pathway entry
- [ ] Escalation tier row present for each conflict (Escalation Owner + Trigger)
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

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

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band labels.

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
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

All Step 5c dimension scores must draw from this table. Assign the level whose behavioral
descriptor best matches observed evidence. Cite the level number in the Evidence cell.

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority over this decision | No direct contact channel; third-party relay only | No documented statement of support |
| 1 | Advisory influence; can surface concerns but cannot advance or close | Occasional touchpoint; not in regular decision loop | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant or sponsor; can advance or delay but not close unilaterally | In regular decision loop; direct async channel established | Documented commitment with schedulable action and named owner |
| 3 | Final decision authority or veto power; can block, advance, or close unilaterally | Peer-level relationship; synchronous channel available on request | Committed with deadline, named accountability, and contingency if unavailable |

FAIL_UNANCHORED_SCORE: any Step 5c dimension score is outside 0-3, or the Evidence cell
does not cite a level from this prefill table.

---

### Step 5c: Champion depth scoring — PM role

Scores must be drawn from the Step 5b-anchor prefill. Composite gate: >= 6 (max 9).

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | | level [N]: [behavioral evidence matching that level] |
| Proximity | | level [N]: [behavioral evidence matching that level] |
| Commitment | | level [N]: [behavioral evidence matching that level] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative and no risk documented.
FAIL_UNANCHORED_SCORE: any dimension score outside 0-3 or Evidence cell does not cite a
level from the Step 5b-anchor prefill.

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
that violates Step 2c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 2c gatekeeper lead-time tags, conflict
resolution pathway entries, escalation tier entries, trajectory assessments, velocity
assessments, champion depth scores (with updated anchor citations), engagement window
derivations, synthesis readout rows.

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
a documented justification in this table.

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
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 2a / C-06) | champion status: level [N] composite (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-05 — All Three New Axes Combined

**Axis**: V-01 (UX → Strategy → PM, FAIL_UNANCHORED_CONFLICT_PARTY) + V-02 (Step 5b-anchor prefill, FAIL_UNANCHORED_SCORE) + V-03 (Step 0b inertia pre-assessment, FAIL_STALE_INERTIA_SCORE). All prior 42 criteria present.

**Hypothesis**: All three new axes operate at non-overlapping steps: segment-anchor at Step 2a (Phase 2 Strategy conflict identification), behavioral anchor at Step 5b-anchor (champion scoring pre-step), inertia risk score at Step 0b (pre-Phase-1) and Step 9 (synthesis traceability). None interfere with each other or with any existing criterion. Three new gate labels (FAIL_UNANCHORED_CONFLICT_PARTY, FAIL_UNANCHORED_SCORE, FAIL_STALE_INERTIA_SCORE) all coexist with the existing 42-criterion set. Maximum structural density for Round 16 discovery.

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

### Step 0b: Inertia pre-assessment — Strategy role

Before Phase 1 begins, identify displaced workflows and assign an Inertia Risk Score.
This score must be referenced in Step 9 synthesis for every inertia-tagged stakeholder.

Risk Score band definitions:

| Score | Criteria |
|-------|----------|
| 1 (Low) | Coalition capacity is low AND impact severity is low — displaced group unlikely to organize resistance or meaningfully delay the decision |
| 2 (Medium) | Coalition capacity is medium OR impact severity is medium — displaced group may organize or surface friction at key checkpoints |
| 3 (High) | Coalition capacity is high OR impact severity is high — displaced group is likely to actively block, delay, or escalate |

Inertia pre-assessment table:

| Displaced Workflow | Affected Group | Inertia Risk Score | Coalition Capacity | Impact Severity |
|--------------------|---------------|-------------------|--------------------|-----------------|
| [existing practice this decision disrupts] | [group relying on it] | 1 / 2 / 3 | high / medium / low | high / medium / low |

If no workflow is displaced, emit: `[INERTIA-NONE: this decision introduces new capability
without displacing an existing workflow or toolchain]` and proceed to Phase 1.

FAIL_NO_INERTIA_PRE_ASSESSMENT: Step 0b table absent when the decision displaces an
existing workflow.
FAIL_STALE_INERTIA_SCORE: any inertia-tagged stakeholder's Step 9 synthesis row omits
the Step 0b Inertia Risk Score.

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

#### Step 2a: Structural conflicts, resolution pathways, and escalation tiers — Strategy role

Identify at least two structural conflicts. For each conflict, populate one row in the
resolution pathway table and one row in the escalation tier table.

Party anchor rule: Each Party A and Party B cell must either (a) match a segment name
from Phase 1 verbatim, or (b) carry an `[ORG-ROLE: description]` tag identifying an
org role not captured as a user segment.

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [Phase 1 segment name OR ORG-ROLE: description] | [Phase 1 segment name OR ORG-ROLE: description] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

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

#### Step 2b: Inertia stakeholder mapping — Strategy role

Reference Step 0b risk scores. Inertia Risk Score from Step 0b must appear in the Notes
cell for each inertia stakeholder row.

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Risk Score |
|-------------|-----------------|--------------|-------------------|--------------------|
| [name — must match Phase 1 segment or carry ORG-ROLE tag] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [yes / limited / no] | [1 / 2 / 3 from Step 0b] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA: risk-score=N]` in
the Notes column. They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when Step 0b identified displaced
workflows. (If Step 0b emitted INERTIA-NONE, this criterion is not applicable.)

#### Step 2c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 2 → Phase 3 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two anchored parties, nature, and complete
      resolution pathway entry
- [ ] Escalation tier row present for each conflict (Escalation Owner + Trigger)
- [ ] At least one inertia stakeholder with Step 0b risk score (or INERTIA-NONE documented)
- [ ] At least one critical-path gatekeeper with lead-time tag

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
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [source] | [INERTIA: risk-score=N] if applicable |

Velocity column draws exclusively from Step 3a prefill labels.
Inertia stakeholder Notes must include the Step 0b risk score in `[INERTIA: risk-score=N]` format.

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

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses probability outside these band labels.

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
| [name] | [quadrant] | [from Step 2c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing must fall within derived windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill — PM role

All Step 5c dimension scores must draw from this table. Assign the level whose behavioral
descriptor best matches observed evidence. Cite the level number in the Evidence cell.

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No formal or informal authority over this decision | No direct contact channel; third-party relay only | No documented statement of support |
| 1 | Advisory influence; can surface concerns but cannot advance or close | Occasional touchpoint; not in regular decision loop | Expressed interest verbally; no calendar commitment |
| 2 | Named decision participant or sponsor; can advance or delay but not close unilaterally | In regular decision loop; direct async channel established | Documented commitment with schedulable action and named owner |
| 3 | Final decision authority or veto power; can block, advance, or close unilaterally | Peer-level relationship; synchronous channel available on request | Committed with deadline, named accountability, and contingency if unavailable |

FAIL_UNANCHORED_SCORE: any Step 5c dimension score is outside 0-3, or the Evidence cell
does not cite a level from this prefill table.

---

### Step 5c: Champion depth scoring — PM role

Scores must be drawn from the Step 5b-anchor prefill. Composite gate: >= 6 (max 9).

| Dimension | Level (0–3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | | level [N]: [behavioral evidence matching that level] |
| Proximity | | level [N]: [behavioral evidence matching that level] |
| Commitment | | level [N]: [behavioral evidence matching that level] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative and no risk documented.
FAIL_UNANCHORED_SCORE: any dimension score outside 0-3 or Evidence cell does not cite a
level from the Step 5b-anchor prefill.

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
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [preserves current first; acknowledges risk-score=N] | [relative anchor] |

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
that violates Step 2c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 2c gatekeeper lead-time tags, conflict
resolution pathway entries, escalation tier entries, trajectory assessments, velocity
assessments, Step 0b inertia risk scores, champion depth scores (with updated anchor
citations), engagement window derivations, synthesis readout rows.

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
a documented justification in this table.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.
All stakeholders listed in Step 8b as "Synthesis Row Planned: yes" must appear here.
Inertia-tagged stakeholders must include Inertia Risk Score from Step 0b.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.
FAIL_SYNTHESIS_GAP: any stakeholder from Step 8b coverage audit absent without documented
justification.
FAIL_STALE_INERTIA_SCORE: any inertia-tagged stakeholder's synthesis row omits the Step 0b
Inertia Risk Score.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Inertia Risk Score |
|-------------|--------------|-------------------|------------------|-----------------|------------------|--------------------|
| [name — non-inertia] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 2a / C-06) | champion status: level [N] composite (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) | N/A |
| [name — inertia] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 2a / C-06) | champion status: level [N] composite (Step 5c / C-27) | comms frame type: displacement-acknowledgment (Step 6a / C-13) | risk-score=[N] (Step 0b) |
```
