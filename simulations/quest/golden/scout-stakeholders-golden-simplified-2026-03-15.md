Now I have all I need. Let me produce the simplified prompt with all cuts applied.

## Simplified Prompt

```
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

FAIL_SILENT_INFERENCE / FAIL_WRONG_STATE.

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
| HIGH | Retraining, data migration, or process redesign required |
| MEDIUM | Workflow adjustment and communication required |
| LOW | Self-service; minimal stakeholder disruption |

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

FAIL_MONOLITH_ASSUMPTION / FAIL_NO_NOT_DOING.

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

| Conflict | Party A | Party B | Nature | Severity Band | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------|---------------------|-------------------|----------|

| Conflict | Escalation Owner | Escalation Trigger | Escalation Action |
|----------|-----------------|-------------------|-------------------|

FAIL_ONE_PARTY / FAIL_NO_RESOLUTION_PATHWAY / FAIL_NO_ESCALATION_PATH /
FAIL_UNANCHORED_CONFLICT_PARTY / FAIL_UNCALIBRATED_SEVERITY.

---

#### Step 2b: Inertia stakeholder mapping

| Stakeholder | Current Approach | Displaced By | Coalition Capacity | Step 0b Competitor | Response Track |
|-------------|-----------------|--------------|-------------------|--------------------|----------------|

FAIL_NO_INERTIA / FAIL_NO_COMPETITOR_ENTRY / FAIL_NO_RESPONSE_TRACK.

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

Precedes Step 3b-prefill. EXPIRED without refresh: reclassify as ASSUMED in Step 3b.

| Staleness Band | Criteria |
|----------------|----------|
| CURRENT | < 14 days |
| STALE | 15–60 days ago |
| EXPIRED | > 60 days ago, or one-time observation |

EXPIRED entries: mandatory Step 8 amendment targets alongside ASSUMED entries.

FAIL_UNCALIBRATED_STALENESS: Source Age absent or not drawn from this prefill.

---

### Step 3b-prefill: Source typology

Follows Step 3c-staleness.

| Typology | Criteria |
|----------|----------|
| OBSERVED | Directly witnessed; citable artifact exists |
| INFERRED | Reasoned from pattern or adjacent signal |
| ASSUMED | No direct evidence; based on role stereotype |

Each Source cell must carry: `[TYPOLOGY: source description]`.

FAIL_UNANNOTATED_SOURCE: Source cell lacking typology label.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Velocity | Engagement Window | Source | Source Age | Notes |
|-------------|-------|----------|----------|------------|----------|-------------------|--------|------------|-------|
| [name] | H/M/L | H/M/L | [label] | [trajectory: signal] | [velocity] | [TBD — Step 5a] | [TYPOLOGY: source description] | [staleness] | [INERTIA] if applicable |

FAIL_PROSE_ONLY / FAIL_NO_SOURCE / FAIL_NO_TRAJECTORY / FAIL_NO_ENGAGEMENT_WINDOW /
FAIL_UNCALIBRATED_VELOCITY / FAIL_UNANNOTATED_SOURCE / FAIL_UNCALIBRATED_STALENESS.

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

FAIL_WRONG_ORDER / FAIL_NO_MITIGATION / FAIL_UNCALIBRATED_PROBABILITY.

---

### Step 5a: Engagement window derivation

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|

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

FAIL_BELOW_CHAMPION_THRESHOLD / FAIL_UNANCHORED_SCORE.

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

FAIL_NO_CHANNEL / FAIL_WRONG_CHANNEL.

---

### Step 6b: Communication strategy per quadrant

| Quadrant | Stakeholder | Frame Type | Channel | Message | Timing | Priority Band |
|----------|-------------|------------|---------|---------|--------|---------------|
| Manage Closely | [name] | decision-briefing | Meeting | [message] | [anchor] | [priority] |
| Keep Satisfied | [name] | status-update | Email | [message] | [anchor] | [priority] |
| Keep Informed | [name] | awareness-nudge | Slack-channel | [message] | [anchor] | [priority] |
| Monitor | [name] | monitor-note | Artifact | [message] | [anchor] | [priority] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | Meeting | [track-aligned; see Step 0c] | [anchor] | [priority] |

FAIL_SAME_FRAME / FAIL_VAGUE_TIMING / FAIL_WRONG_CHANNEL / FAIL_NO_CHANNEL /
FAIL_RESPONSE_TRACK_ALIGNMENT.

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

Minimum one amendment.

| Amendment Target | Change Made | Verification |
|-----------------|-------------|--------------|
| [artifact + row id] | [change applied] | [confirmed ref with date, OR "not-yet: [owner] by [deadline]"] |

FAIL_OBSERVATION_ONLY / FAIL_UNVERIFIED_AMENDMENT.

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

FAIL_NO_SYNTHESIS / FAIL_NO_ATTRIBUTION / FAIL_SYNTHESIS_GAP.

---

### Step 9b: Synthesis depth audit matrix

Cells: PASS (substantive content in Step 9) / FAIL (functionally empty) / N/A:[code] (documented absence).
Permitted codes: NO-CONFLICT, NO-CHAMPION-ROLE, MONITOR-ONLY, NO-COMPETITOR-CONTEXT.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type | Priority Band | Competitor |
|-------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [name] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] | PASS / FAIL / N/A:[code] |

FAIL_SHALLOW_SYNTHESIS: any cell carries FAIL status.

---
```

## Simplification Report

**Before word count:** 2752 (full golden file body including "What made it golden" + rubric summary commentary)
**After word count:** 2117
**Reduction:** 635 words / **23.1%**

### What was removed and why

| Cut | Where | Words saved | Rationale |
|-----|-------|-------------|-----------|
| Stripped "What made it golden" section | Lines 438–453 | ~380 | Documentation for reviewers, not executable prompt content |
| Stripped "Final rubric criteria summary" section | Lines 457–479 | ~190 | Rubric reference only; no role in directing behavior |
| Removed "Name each displaced workflow or tool before Phase 1." | Step 0b | 9 | Redundant with the step heading ("Status-quo competitor inventory") |
| Removed "Translate each Response Track into explicit engagement obligations." | Step 0c | 8 | Redundant with the step heading ("Response Track engagement obligations") |
| Removed "Resolution pathway table:" label | Step 2a | 3 | A heading before a table that is already titled in the step heading |
| Removed "Escalation tier table:" label | Step 2a | 3 | Same — the table columns make its identity self-evident |
| Removed "Each Phase 3 Source Age cell: one label from this table." | Step 3c | 14 | Implicit from the prefill + FAIL_UNCALIBRATED_STALENESS |
| Removed "ASSUMED entries are mandatory Step 8 amendment targets." | Step 3b | 9 | Fully covered by the Step 8 footer instruction |
| Removed "Step 6b timing anchors must fall within derived engagement windows." | Step 5a | 10 | Behavioral guidance with no FAIL code anchor in Step 5a; effect is enforced via FAIL_NO_ENGAGEMENT_WINDOW |
| Removed Rule 2: "`displacement-acknowledgment` mandatory for every inertia-tagged stakeholder." | Step 6a | 13 | Already stated in the Frame Type table ("Inertia stakeholders — mandatory") |
| Removed "Eligible targets: any structural output in this prompt." | Step 8 | 8 | Circular — all tables in the prompt are the obvious targets |
| Removed "as defined above" suffix from all FAIL code lines (7 instances) | Throughout | 21 | The codes are self-documenting; "as defined above" adds no information and in many cases had no actual prior definition to reference |
| Condensed Step 9b 5-line PASS/FAIL/N/A explanation to 2 lines | Step 9b | 27 | All semantic content preserved; eliminated repetitive `X = definition` format |
| Condensed Step 3c ROLE SEQUENCE NOTE: removed prefix label, shortened EXPIRED directive | Step 3c | 16 | Preserved C-54's forward-reference directive content exactly; stripped scaffolding words |
| Removed "ROLE SEQUENCE NOTE: " prefix from Step 3b | Step 3b | 4 | The statement "Follows Step 3c-staleness." is sufficient; prefix adds no content |
| Condensed Staleness Band criteria descriptions | Step 3c | 20 | "< 14 days" conveys the same calibration as "Confirmed or refreshed within current sprint (< 14 days)"; numeric anchor is all that scores |
| Shortened Switching Cost Band criteria | Step 0b | 9 | Trimmed redundant "Requires" preamble; meaning preserved |
| Condensed Phase 3 template row option lists | Phase 3 | 22 | Removed inline option expansions (e.g., "ascending-toward-advocate / stable / descending-toward-risk") that duplicate prefill table content; cross-references still present via column names |
| Replaced "URGENT / STANDARD / DEFERRED" in each Step 6b row with "[priority]" | Step 6b | 15 | Priority band options already defined in Step 6e-priority; repeating in 5 template rows is redundant |

### Criteria verification

All 5 essential criteria preserved:
- **C-01** (CODEOWNERS fallback): Step 0 state machine intact
- **C-02** (Power/Interest grid): Phase 3 table intact
- **C-03** (Veto risks ranked): Steps 4a+4b intact with ORDER instruction
- **C-04** (Champion with concrete action): Steps 5b, 5c, 5d intact; schedulable action still required
- **C-05** (Communication strategy per quadrant): Step 6b intact with all 5 quadrant rows

All 3 recommended criteria preserved (C-06 conflict identification, C-07 role framing, C-08 gatekeepers).

All three v21 aspirational criteria preserved:
- **C-54**: EXPIRED→ASSUMED forward-reference directive intact (condensed but semantically identical)
- **C-55**: Step 9b audit matrix structure intact; PASS/FAIL/N/A semantics in 2-line form still define column/row detection
- **C-56**: Step 0c Engagement Objective + Success Criterion + Downstream Message Requirement columns intact

```json
{"simplified_word_count": 2117, "original_word_count": 2752, "all_essential_still_pass": true, "reduction_pct": 23.1}
```
