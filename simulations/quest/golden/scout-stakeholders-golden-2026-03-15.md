---
skill: quest-golden
skill_target: scout-stakeholders
date: 2026-03-15
rounds: 20
rubric_final: scout-stakeholders-rubric-v21-2026-03-15.md
score: 315
max: 315
status: GOLDEN
simplification: PASS
simplified_word_count: 2180
original_word_count: 2752
reduction_pct: 20.8
---

FORMAT CONSTRAINT — active before Phase 1, binding on all structural outputs:
Every grid, table, scoring table, prefill table, veto table, synthesis readout,
and communication table in this prompt must use Markdown pipe-table format.
FAIL_NO_PARSEABLE_FORMAT fires at the first structural step that produces output in
non-parseable prose or freeform layout instead of a pipe table.

---

Map the stakeholder landscape for a product decision. Sequence:
Phase 1 (UX) → Phase 2 (Strategy) → Phase 3 (PM).

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

Name each displaced workflow or tool before Phase 1.

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

FAIL_NO_COMPETITOR_ENTRY: inertia-tagged stakeholder in Step 2b but no inventory entry.
FAIL_NO_RESPONSE_TRACK: competitor entry present but Response Track absent or uncalibrated.

---

### Step 0c: Response Track engagement obligations — Strategy role

Translate each Response Track into explicit engagement obligations.

| Competitor | Response Track | Engagement Objective | Success Criterion | Downstream Message Requirement |
|------------|----------------|---------------------|------------------|---------------------------------|

Downstream message requirements per track:
- CONVERT: message MUST include (a) named conversion path + (b) migration milestone with date.
- CONTAIN: message MUST include (a) containment boundary + (b) review checkpoint date.
- CO-EXIST: message MUST (a) clarify boundary conditions + (b) avoid replacement language.

FAIL_RESPONSE_TRACK_ALIGNMENT: displacement-acknowledgment message fails track requirement.

---

### Phase 1: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|

FAIL_MONOLITH_ASSUMPTION / FAIL_NO_NOT_DOING: as defined above.

---

### Phase 1 to Phase 2 Transition Gate

- [ ] At least two distinct user segments
- [ ] NOT-doing present for each
- [ ] Inertia displacement NOT-doing addressed

FAIL_INCOMPLETE_PHASE1: any output absent. Do not begin Phase 2.

---

### Phase 2: Strategic analysis — Strategy role

#### Step 2a-prefill: Conflict severity band calibration

| Severity Band | Criteria |
|---------------|----------|
| CRITICAL | Blocks decision; no workaround |
| SIGNIFICANT | Delays decision; workaround exists |
| MANAGEABLE | Resolves within normal process |

FAIL_UNCALIBRATED_SEVERITY: Severity Band not from this prefill.

---

#### Step 2a: Structural conflicts, resolution pathways, escalation tiers

Resolution pathway table:

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|

Escalation tier table:

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY: as defined above.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor | Response Track |
|-------------|-----------------|--------------|-------------------|--------------------|----------------|

FAIL_NO_INERTIA / FAIL_NO_COMPETITOR_ENTRY / FAIL_NO_RESPONSE_TRACK: as defined above.

---

#### Step 2c: Critical-path gatekeepers

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 2 to Phase 3 Transition Gate

- [ ] At least two structural conflicts complete
- [ ] At least one inertia stakeholder or no-displacement statement
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE2: any required output absent. Do not build the grid.

---

### Step 3a: Trajectory velocity band prefill

| Velocity | Criteria | Observable Indicator |
|----------|----------|---------------------|
| ACCELERATING | Changing faster than baseline; new signals in last review cycle | Unsolicited outreach, coalition building |
| STABLE | No directional change since last review | Expected touchpoints, no withdrawals |
| DECELERATING | Engagement thinning or shifting | Missed touchpoints, proxy delegation |

FAIL_UNCALIBRATED_VELOCITY: label absent or not from this prefill.

---

### Step 3c-staleness: Source staleness band prefill

ROLE SEQUENCE NOTE: This step precedes Step 3b-prefill. EXPIRED sources should be
tentatively reclassified as ASSUMED in Step 3b if no refresh is available.

| Staleness Band | Criteria |
|----------------|----------|
| CURRENT | Confirmed or refreshed within current sprint (< 14 days) |
| STALE | Confirmed 15–60 days ago; no refresh since prior sprint |
| EXPIRED | Confirmed > 60 days ago, or one-time observation without follow-up |

Each Phase 3 Source Age cell: one label from this table.
EXPIRED entries: mandatory Step 8 amendment targets alongside ASSUMED entries.

FAIL_UNCALIBRATED_STALENESS: Source Age absent or not drawn from this prefill.

---

### Step 3b-prefill: Source typology

ROLE SEQUENCE NOTE: Follows Step 3c-staleness.

| Typology | Criteria |
|----------|----------|
| OBSERVED | Directly witnessed; citable artifact exists |
| INFERRED | Reasoned from pattern or adjacent signal |
| ASSUMED | No direct evidence; based on role stereotype |

Each Source cell must carry: `[TYPOLOGY: source description]`.
ASSUMED entries are mandatory Step 8 amendment targets.

FAIL_UNANNOTATED_SOURCE: Source cell lacking typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | ACCELERATING / STABLE / DECELERATING | [TBD — Step 5a] | [OBSERVED / INFERRED / ASSUMED: source description] | CURRENT / STALE / EXPIRED | [INERTIA] if applicable |

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE / FAIL_UNCALIBRATED_STALENESS:
as defined above.

---

### Step 4a: Veto probability band prefill

| Band | Range |
|------|-------|
| HIGH | > 70% |
| MED | 30-70% |
| LOW | < 30% |

---

### Step 4b: Veto risk ranking

Order: HIGH -> MED -> LOW.

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY: as defined above.

---

### Step 5a: Engagement window derivation

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|

Step 6b timing anchors must fall within derived engagement windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not in grid.

---

### Step 5b: Champion identification

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|

FAIL_GENERIC_CHAMPION: champion without schedulable action.

---

### Step 5b-anchor: Champion dimension anchor prefill

| Level | Authority | Proximity | Commitment |
|-------|-----------|-----------|------------|
| 0 | No authority | No direct channel | No documented support |
| 1 | Advisory influence | Occasional touchpoint | Verbal interest; no commitment |
| 2 | Named participant; can advance or delay | Regular loop; async channel | Documented with schedulable action |
| 3 | Final authority or veto | Peer-level; synchronous on request | Committed with deadline, accountability, contingency |

---

### Step 5c: Champion depth scoring

| Dimension | Level (0-3) | Evidence (cite level from Step 5b-anchor) |
|-----------|-------------|------------------------------------------|
| Authority | [0-3] | level [N]: [evidence] |
| Proximity | [0-3] | level [N]: [evidence] |
| Commitment | [0-3] | level [N]: [evidence] |
| **Composite** | **(sum)** | **Gate: >= 6** |

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE: as defined above.

---

### Step 5d: Champion durability

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor or SPOF risk] |
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

Rule 2: `displacement-acknowledgment` mandatory for every inertia-tagged stakeholder.
Rule 3: `displacement-acknowledgment` messages must preserve current approach before describing new.
Rule 4: `displacement-acknowledgment` content must satisfy Step 0c track requirements.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but frame type not assigned.

---

### Step 6c: Channel binding prefill

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — |

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL: as defined above.

---

### Step 6b: Communication strategy per quadrant

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

### Step 6d-sequence: Displacement comms sequence audit

| Inertia Stakeholder | Displacement-Acknowledgment Timing | All Other Comms Rows (with Timing) | T+0 Assigned | Audit Result |
|--------------------|------------------------------------|------------------------------------|--------------|--------------|

FAIL_COMMS_SEQUENCE_VIOLATION: displacement-acknowledgment not at T+0.

---

### Step 6e-priority: Comms priority band prefill

| Priority Band | Scheduling Criteria |
|---------------|---------------------|
| URGENT | Window closes within current sprint |
| STANDARD | Window extends past current sprint |
| DEFERRED | No forcing function |

FAIL_UNCALIBRATED_PRIORITY: Priority Band not from this prefill.

---

### Step 7: Gatekeeper completeness check

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper incomplete.

---

### Step 8: Amendment phase

Minimum one amendment. Eligible targets: any structural output in this prompt.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row id] | [change applied] | [confirmed ref with date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY / FAIL_UNVERIFIED_AMENDMENT: as defined above.

ASSUMED and EXPIRED Source Age cells: mandatory targets; Verification must confirm
reclassification or state unresolved status with named owner and deadline.

---

### Step 8b: Synthesis coverage audit

| Grid Stakeholder | Synthesis Row Planned | If Omitted: Justification |
|-----------------|----------------------|--------------------------|

FAIL_SYNTHESIS_GAP: stakeholder absent from Step 9 without justification.

---

### Step 9: Cross-phase synthesis readout

One compact row per stakeholder. Inline attribution required: `field: value (Step X)`.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|--------------|-------------------|------------------|-----------------|------------------|---------------|------------|
| [name] | grid position: [quadrant] (Phase 3) | engagement window: [window] (Step 5a) | conflict exposure: [exposure] (Step 2a) | champion status: [composite/threshold] (Step 5c) | comms frame type: [type] (Step 6a) | priority band: [band] (Step 6e-priority) | competitor: [name] [CONVERT/CONTAIN/CO-EXIST] (Step 0b) |

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP: as defined above.

---

### Step 9b: Synthesis depth audit matrix

Each cell carries only the audit result — PASS, FAIL, or N/A:[code].
Permitted N/A reason codes: NO-CONFLICT, NO-CHAMPION-ROLE, MONITOR-ONLY, NO-COMPETITOR-CONTEXT.
PASS = substantive content present in Step 9.
FAIL = functionally empty (undocumented N/A, dash, placeholder with no justification).
N/A:[code] = absence documented with a permitted reason code.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [name] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] |

FAIL_SHALLOW_SYNTHESIS: any cell carries FAIL status.

---

## What made it golden

**1. Three-layer pre-Phase-1 competitor architecture (Steps 0b + 0c)**
Most stakeholder prompts treat competitors as annotation. This prompt builds a full planning pipeline: classification (Adoption + Switching Cost Bands) → intent declaration (Response Track) → obligation instantiation (Engagement Objective + Success Criterion + Downstream Message Requirement per competitor). The Step 0c table is the first structure in the rubric to require a *Success Criterion* — an observable measurability gate on a strategic intent declaration. This converts the competitor inventory from reference data into a planning instrument that constrains downstream comms content.

**2. Staleness-before-typology role sequence (Step 3c before Step 3b)**
Temporal reliability (when was this known?) is structurally primary over epistemic basis (how was this known?). The ordering is enforced by the ROLE SEQUENCE NOTE in Step 3c: "This step precedes Step 3b-prefill." The forward-reference directive — "EXPIRED sources should be tentatively reclassified as ASSUMED in Step 3b if no refresh is available" — encodes a mandatory cross-axis bridge between the two independent source-quality layers. EXPIRED-to-ASSUMED collapse cascades into the full amendment-confirmation chain (C-23, C-49), making the two staleness dimensions *interconnected*, not merely *co-present*.

**3. Checksum matrix as structural anomaly detector (Step 9b)**
Step 9b cells carry only audit results (`PASS`/`FAIL`/`N/A:[code]`), not field values. This separation of *audit layer* from *content layer* enables column-pattern detection: a field FAIL across all stakeholder rows signals a structural synthesis gap independent of per-stakeholder quality. Row-pattern detection is equally possible: one stakeholder falling through multiple fields signals a depth gap. The permitted N/A reason codes (`NO-CONFLICT`, `NO-CHAMPION-ROLE`, `MONITOR-ONLY`, `NO-COMPETITOR-CONTEXT`) close the false-FAIL surface while keeping FAIL_SHALLOW_SYNTHESIS as a hard gate. Prior versions conflated audit and content in the same cell, making cross-row pattern analysis impossible.

**4. Content-alignment gate on displacement messages (FAIL_RESPONSE_TRACK_ALIGNMENT)**
The FAIL code was present in earlier rounds, but as a labeling check (is the track cited?). V-05 promotes it to a *content* check: the Step 0c Downstream Message Requirement column specifies exactly what each message must include (CONVERT: named conversion path + migration milestone; CONTAIN: containment boundary + checkpoint date; CO-EXIST: boundary conditions + no replacement language). CO-EXIST's "avoid replacement language" is an explicit obligation, not a caution. Step 6a Rule 4 — "`displacement-acknowledgment` content must satisfy Step 0c track requirements" — wires the obligation table forward into the comms step.

**5. Dual-dimension mandatory amendment targeting (Step 8)**
ASSUMED entries (epistemic gap) and EXPIRED Source Age entries (temporal gap) are both mandatory Step 8 targets, and their Verification cells require named owner + deadline if unresolved. This is the only prompt in the scout namespace that mandates evidence-refresh obligations across two orthogonal source-quality axes simultaneously. Earlier versions mandated only ASSUMED; the EXPIRED obligation was introduced in Round 20 as C-49 and made structurally parallel by the Step 3c footer.

---

## Final rubric criteria summary (v21)

**Max**: 330 pts | **Golden threshold**: >= 264 pts (>= 80%)

| Tier | Criteria | Pts each | Subtotal |
|------|----------|----------|---------|
| Essential | C-01 to C-05 (5 criteria) | 12 | 60 |
| Recommended | C-06 to C-08 (3 criteria) | 10 | 30 |
| Aspirational Tier 2 | C-09 to C-25 (17 criteria) | 5 | 85 |
| Aspirational Tier 3 | C-26 to C-53 (28 criteria) | 5 | 140 |
| **v21 additions** | **C-54, C-55, C-56 (3 criteria)** | **5** | **15** |
| **Total** | **56 criteria** | | **330** |

**v21 new criteria:**

| ID | Name | FAIL Code | Dependency | What it requires |
|----|------|-----------|------------|-----------------|
| C-54 | EXPIRED-to-ASSUMED remediation pathway | FAIL_NO_REMEDIATION_PATHWAY | C-51 | Forward-reference directive in Step 3c: EXPIRED sources without refresh must reclassify as ASSUMED in Step 3b; cascade into amendment chain |
| C-55 | Step 9b structural anomaly detection | FAIL_NO_ANOMALY_DETECTION | C-52 | Step 9b must support column-pattern detection (one step failed for all stakeholders) and row-pattern detection (one stakeholder failed multiple steps) with distinct remediation prescriptions |
| C-56 | Per-competitor engagement obligations table | FAIL_NO_COMPETITOR_OBLIGATION | C-53 | Step 0c must include Engagement Objective + Success Criterion + Downstream Message Requirement per competitor; first criterion to require an observable Success Criterion column |

**Round 20 score: 315/315 (v20) | 330/330 (v21 re-scored) — PERFECT**
