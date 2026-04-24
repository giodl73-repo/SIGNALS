## Round 14 Variations — scout-stakeholders

**Target rubric**: v14 (max 230 pts)
**Goal**: Explore three new structural axes while maintaining 230/230 target. All five variations include C-33, C-34, C-35, C-36.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Org context state machine | Formalizing Step 0 as an explicit three-state decision tree with terminal state labels and FAIL_WRONG_STATE adds an auditable structural property absent from C-01 |
| V-02 | Veto probability calibration bands | Prefill table binding veto probability to calibrated H/M/L bands is to Step 4 as Step 6a prefill is to Step 6b — a new constrained-lookup gate yielding FAIL_UNCALIBRATED_PROBABILITY |
| V-03 | Comms channel binding | Frame Type → Channel binding prefill (Step 6c) before the comms table extends the constrained-lookup mechanism of Step 6a to a second structural dimension; FAIL_WRONG_CHANNEL is a new gate label distinct from FAIL_SAME_FRAME |
| V-04 | V-01 + V-02 combined | State machine and calibration bands are mutually non-interfering; both new gate labels coexist with all 36 prior criteria |
| V-05 | V-01 + V-02 + V-03 combined | All three new axes simultaneously; maximum structural density |

---

## V-01 — Org Context State Machine

**Axis**: Step 0 formalized as an explicit three-state decision tree with terminal state labels.

**Hypothesis**: The state machine adds two structural properties absent from C-01: (1) a pipe-table decision tree making the decision logic machine-readable, (2) a terminal state label emitted before Phase 1 that can be audited against the actual source used. C-01 requires the check and the one-question halt behavior; it does not require a labeled state output or a decision tree in parseable format. FAIL_WRONG_STATE is a new gate label.

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

Identify at least two structural conflicts relevant to this feature decision. For each
conflict, populate one row of the resolution pathway table:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | budget / timeline / scope / authority / methodology | [named person or body] | [specific ruling needed] | [date or milestone] |

Resolution Authority: the named person or body with legitimate power to close the conflict.
Decision Required: the specific determination, not a general area of concern.
Deadline: latest date or milestone at which the conflict must be resolved for the feature
to proceed.

FAIL_ONE_PARTY: a conflict row names only one party — a single-stakeholder risk is not a
structural conflict.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row is missing Resolution Authority, Decision
Required, or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

Identify stakeholders whose primary relationship to this feature is resistance born from
displacement of their current approach.

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name or group] | [what they do today that this feature disrupts] | [what this feature replaces or threatens] | [can they recruit other resistors? yes / limited / no] |

Inertia stakeholders must appear in the Phase 3 grid with `[INERTIA]` in the Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

Identify stakeholders whose approval or non-objection is required before this feature
can ship.

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name or group] | [compliance sign-off / budget approval / security review / architecture board / other] | [minimum advance notice: e.g., "6 weeks", "sprint-before-launch"] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Confirm all Phase 1 outputs are present before proceeding:

- [ ] At least two structural conflicts identified, each with two named parties and a
      nature statement
- [ ] Resolution pathway entry complete for each conflict (Authority, Decision Required,
      Deadline)
- [ ] At least one inertia stakeholder identified, or an explicit statement that no
      current-approach displacement applies
- [ ] At least one critical-path gatekeeper identified with a lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output is absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

For each relevant user segment, complete one row:

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [primary use pattern for this feature area] | [affected touchpoints] | [what this product explicitly does NOT provide for this segment in this decision scope] | [gatekeeper candidate / inertia candidate / neither] |

NOT-doing statement requirements:
- Generic "out of scope" language is not a NOT-doing statement.
- For inertia-classified segments: the NOT-doing statement must address what the new
  approach does not preserve from the current approach — not only what is new.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing statement absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Confirm all Phase 2 outputs are present before building the grid:

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing statement present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if inertia stakeholders exist)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output is absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

Build the Power/Interest grid after both Phase 1 and Phase 2 are complete.

| Stakeholder | Power | Interest | Quadrant | Trajectory | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | Manage Closely / Keep Satisfied / Keep Informed / Monitor | ascending-toward-advocate / stable / descending-toward-risk: [observable signal] | [TBD — Step 5a] | CODEOWNERS / initial-inventory / conflict-discovery / amendment / ux-discovery | [INERTIA] if applicable |

Grid requirements:
- Minimum 4 rows.
- Quadrant labels: Manage Closely / Keep Satisfied / Keep Informed / Monitor.
- Trajectory column: per-row directional assessment with one observable-signal rationale.
- Engagement Window column: placeholder `[TBD — Step 5a]`; values derived and filled in
  Step 5a.
- Source column: must be one of the five permitted values.
- Inertia-classified stakeholders must carry `[INERTIA]` in the Notes column.

FAIL_PROSE_ONLY: stakeholder list presented as prose without a grid structure.
FAIL_NO_SOURCE: any row missing a Source value.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing a directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent from the grid.

---

### Step 4: Veto risk ranking — PM role

List all stakeholders who could veto or block this decision. Order by probability,
highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| 1 | [name] | [value] | [value] | [strategy] |

FAIL_WRONG_ORDER: entries are not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.

---

### Step 5a: Engagement window derivation — PM role

Derive the engagement window for each stakeholder or quadrant using the grid quadrant
position (Phase 3) and the gatekeeper lead-time data (Step 1c).

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | Manage Closely / Keep Satisfied / Keep Informed / Monitor | [from Step 1c, or N/A if not a gatekeeper] | [window, e.g., "4–6 weeks before milestone"] | [why this window follows from quadrant + lead time] |

After Step 5a is complete, update the Engagement Window column in the Phase 3 grid with
the derived values (Source: `amendment`).

Engagement Window column in Phase 3 grid must reflect Step 5a values before Step 6b
comms timing is established.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into the grid.

Step 6b comms timing anchors must fall within the Step 5a derived window for each row.

---

### Step 5b: Champion identification and action — PM role

Identify one or more champions: stakeholders with organizational standing to advocate
for this feature and a concrete stake in its success.

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [organizational standing] | [calendar-ready commitment: e.g., "secure 20-min demo in Q2 planning meeting"] |

Generic "engage the champion" or "leverage the relationship" is not a schedulable action.

FAIL_GENERIC_CHAMPION: a champion is named without a schedulable action.

---

### Step 5c: Champion depth scoring — PM role

For each champion identified in Step 5b, complete the scoring table:

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority — organizational power to commit resources or override objections | | |
| Proximity — direct access to blockers and sponsors who matter | | |
| Commitment — demonstrated investment in this feature's success (past actions) | | |
| **Composite** | **(sum)** | **Gate: composite >= 9 required to proceed as primary champion** |

Scoring: 1 = absent or symbolic; 3 = credible but limited; 5 = strong and demonstrated.

If composite < 9: document who can serve as primary champion, or declare the feature
champion-deficient and note the risk.

FAIL_BELOW_CHAMPION_THRESHOLD: composite below 9 with no alternative primary champion
identified and no champion-deficiency risk documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [who assumes the champion role if the current champion departs, or: single-point-of-failure risk documented] |
| Deterioration signal 1 | [observable trigger: e.g., "missed syncs without explanation"] |
| Deterioration signal 2 | [observable trigger: e.g., "feature decisions delegated to non-champions"] |

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

Before populating the communication table, establish the permitted Frame Type values.
Only values listed here are permitted in Step 6b.

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest: needs the full decision picture before acting |
| `status-update` | High-power, low-interest: headline and ask only; no supporting detail |
| `awareness-nudge` | Low-power, high-interest: keep invested and informed without burdening |
| `monitor-note` | Low-power, low-interest: minimal; send only when a threshold event occurs |
| `displacement-acknowledgment` | Inertia stakeholders: lead with what is preserved, then what changes |

Rule 1: Each row in Step 6b must use a distinct Frame Type value.
Rule 2: The `displacement-acknowledgment` Frame Type is mandatory for all
inertia-classified rows. Assign here, before any comms row is populated.
Rule 3: Any row assigned `displacement-acknowledgment` must address what the current
approach preserves — not only what is new or changed.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist in the grid but
`displacement-acknowledgment` is not assigned in this prefill step.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using only Frame Types from the Step 6a prefill table. Step 6b timing
anchors must fall within the Step 5a derived engagement window for each stakeholder.

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | [name] | decision-briefing | [message] | [relative anchor: e.g., "3 weeks before milestone"] |
| Keep Satisfied | [name] | status-update | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | [message preserving current approach first] | [relative anchor] |

FAIL_SAME_FRAME: two or more rows share the same Frame Type value.
FAIL_VAGUE_TIMING: any row has a timing value without a relative anchor.

---

### Step 7: Gatekeeper completeness check — PM role

For each critical-path gatekeeper from Step 1c:

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no: [Step 6b timing vs. Step 1c lead time] |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper has no comms row, missing blocking reason,
or Step 6b timing that violates the Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. An amendment is a finding that changes the stakeholder
landscape: a new stakeholder added, an existing stakeholder reframed or promoted, a
conflict resolved or escalated, a veto risk re-ranked, a resolution pathway authority
or deadline updated, a champion assessment revised.

**Amendment mandate**: Update the affected structural level immediately on discovery.
Eligible update targets: grid rows, veto list entries, Step 6a prefill table, Step 6b
comms rows, Step 1c gatekeeper lead-time tags, conflict resolution pathway entries
(Resolution Authority, Decision Required, Deadline), trajectory assessments, engagement
window derivations, synthesis readout rows.

Enumerating a finding without updating at least one eligible target is not an amendment.

**Anti-pattern — read both forms before proceeding:**

> **Bad**: "Security team raised data residency concerns. This may affect the timeline."
> *(Observation only — no structural level updated.)*

> **Correct**: "Security team elevated data residency concern (source: arch-review-2026-03-15).
> — Grid: Security Team row updated from Keep Informed to Manage Closely (Source: amendment).
> — Veto list: Security Team moved from Rank 3 to Rank 1; mitigation updated.
> — Resolution pathway: Decision Required updated; Deadline updated to sprint-end.
> — Step 6b: Security Team timing updated to 4 weeks before milestone."
> *(All affected structural levels updated.)*

After the amendment pass, audit all `initial-inventory` rows in the Source column. Any
row still carrying `initial-inventory` is a visible gap — confirm with a citation or flag.

FAIL_OBSERVATION_ONLY: a finding documented without updating any eligible structural target.

---

### Step 9: Cross-phase synthesis readout — PM role

Collapse all prior analysis into one compact row per stakeholder. Use inline attribution
notation: each cell value must follow the form `field: value (Step X / C-NN)`.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacks fused inline citation in `field: value (source)` form.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure or N/A] (Step 1a / C-06) | champion status: [primary / secondary / not champion] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-02 — Veto Probability Calibration Bands

**Axis**: Probability band prefill table before Step 4. Veto entries must use calibrated H/M/L band labels from the prefill table.

**Hypothesis**: Calibrated probability bands make veto ranks comparable across runs and auditable against a defined reference. Adding Step 4a as a prefill table before Step 4b (the veto ranking table) is structurally analogous to Step 6a (Frame Type prefill before Step 6b comms table). FAIL_UNCALIBRATED_PROBABILITY is a new gate label distinct from FAIL_WRONG_ORDER.

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

### Step 0: Org context check — PM role

Check for a CODEOWNERS file at the repository root. If present, extract org context
from the file: teams named as owners are primary stakeholder candidates. If CODEOWNERS
is absent, check the invocation context string for team or org identifiers. If neither
source provides sufficient org context, ask exactly one question: "What org or team is
this decision for?" Do not infer silently. Do not proceed on an assumed org structure.

FAIL_SILENT_INFERENCE: proceeding with an assumed org context when CODEOWNERS is absent
and invocation context is insufficient.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | [type] | [named person or body] | [specific ruling needed] | [date or milestone] |

FAIL_ONE_PARTY: a conflict row names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any conflict row missing Resolution Authority, Decision
Required, or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name] | [what they do today that this feature disrupts] | [what this feature replaces] | [yes / limited / no] |

Inertia stakeholders must appear in Phase 3 grid with `[INERTIA]` in Notes column.
They must receive the `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [advance notice required] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts, each with two named parties, nature statement,
      and complete resolution pathway entry
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [use pattern] | [touchpoints] | [explicit non-provision for this segment] | [gatekeeper / inertia / neither] |

For inertia segments: NOT-doing statement must address what the new approach does not
preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing statement absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing statement present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | Manage Closely / Keep Satisfied / Keep Informed / Monitor | ascending-toward-advocate / stable / descending-toward-risk: [signal] | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

Requirements: min 4 rows; quadrant labels; Trajectory column with observable-signal
rationale; Engagement Window column (filled in Step 5a); Source column with permitted
values (CODEOWNERS / initial-inventory / conflict-discovery / amendment / ux-discovery);
[INERTIA] tag for inertia-classified stakeholders.

FAIL_PROSE_ONLY: stakeholder list as prose without grid structure.
FAIL_NO_SOURCE: any row missing Source value.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent from the grid.

---

### Step 4a: Probability band prefill — PM role

Before ranking veto risks, calibrate probability using the band definitions below.
All entries in Step 4b must use exactly one of these band labels.

| Band | Range | When to Use |
|------|-------|-------------|
| HIGH | > 70% | Structural veto: stakeholder has formal authority or demonstrated willingness to block |
| MED | 30–70% | Conditional veto: stakeholder could block under specific circumstances |
| LOW | < 30% | Unlikely veto: limited authority or low stake in the outcome |

FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a probability value outside these
band labels (e.g., freeform text, raw percentage, or synonyms not exactly matching
HIGH / MED / LOW).

---

### Step 4b: Veto risk ranking — PM role

List all stakeholders who could veto or block this decision. Order by band, then by
judgment within band (highest probability first).

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: any Probability Band value not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [e.g., "4–6 weeks before milestone"] | [rationale] |

Update Engagement Window column in Phase 3 grid with derived values (Source: amendment).
Step 6b comms timing anchors must fall within the Step 5a derived window.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into the grid.

---

### Step 5b: Champion identification and action — PM role

| Champion | Standing | Schedulable Action |
|----------|----------|-------------------|
| [name] | [organizational standing] | [calendar-ready commitment] |

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) | Evidence |
|-----------|-------------|---------|
| Authority — power to commit resources or override objections | | |
| Proximity — access to blockers and sponsors | | |
| Commitment — demonstrated investment (past actions) | | |
| **Composite** | **(sum)** | **Gate: composite >= 9 to proceed as primary champion** |

If composite < 9: name alternative primary champion or declare champion-deficient.

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative identified and no risk
documented.

---

### Step 5d: Champion durability — PM role

| Dimension | Assessment |
|-----------|------------|
| Succession path | [successor candidate, or single-point-of-failure risk documented] |
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
Rule 2: `displacement-acknowledgment` is mandatory for inertia rows — assign here.
Rule 3: displacement-acknowledgment rows must address what the current approach preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this prefill step.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | [name] | decision-briefing | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | [preserves current first] | [relative anchor] |

Timing anchors must fall within the Step 5a derived engagement window for each row.

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row has timing without a relative anchor.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
that violates the Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, trajectory assessments, engagement window derivations,
synthesis readout rows.

FAIL_OBSERVATION_ONLY: a finding documented without updating any eligible structural target.

After the amendment pass, audit all `initial-inventory` rows — confirm or flag each.

---

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Each cell must use inline attribution:
`field: value (Step X / C-NN)`.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## V-03 — Comms Channel Binding

**Axis**: Frame Type → Channel binding prefill (Step 6c) before the comms table. Channel column added to Step 6b. FAIL_WRONG_CHANNEL is the new gate label.

**Hypothesis**: Channel binding extends the constrained-lookup mechanism of Step 6a to a second structural dimension. Step 6a constrains Frame Type values; Step 6c constrains Channel values for each Frame Type. A variation can satisfy C-13 (correct Frame Type prefill and distinct types per row) while assigning any channel to any row (no channel constraint) — C-13 PASS, V-03 axis FAIL. The new FAIL_WRONG_CHANNEL gate label is structurally distinct from FAIL_SAME_FRAME.

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

### Step 0: Org context check — PM role

Check for a CODEOWNERS file at the repository root. If present, extract org context
from the file. If CODEOWNERS is absent, check the invocation string for team or org
identifiers. If neither source provides sufficient org context, ask exactly one question:
"What org or team is this decision for?" Do not infer silently.

FAIL_SILENT_INFERENCE: proceeding with an assumed org context when CODEOWNERS is absent
and invocation context is insufficient.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | [type] | [named person or body] | [specific ruling] | [date or milestone] |

FAIL_ONE_PARTY: conflict names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any row missing Resolution Authority, Decision Required,
or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name] | [disrupted approach] | [what this replaces] | [yes / limited / no] |

FAIL_NO_INERTIA: no inertia stakeholders identified when feature displaces existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature statement, and
      complete resolution pathway
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [use pattern] | [touchpoints] | [explicit non-provision] | [gatekeeper / inertia / neither] |

FAIL_MONOLITH_ASSUMPTION: all users treated as a single segment.
FAIL_NO_NOT_DOING: NOT-doing statement absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing statement present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source value.
FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.

---

### Step 4: Veto risk ranking — PM role

| Rank | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| 1 | [name] | [value] | [value] | [strategy] |

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column with derived values. Step 6b timing
anchors must fall within derived windows.

FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not filled into the grid.

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
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here before
any row is populated.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this prefill step.

---

### Step 6c: Channel binding prefill — PM role

Before populating the communication table, establish the permitted channel for each
Frame Type. Step 6b rows must use the Primary Channel or Fallback Channel listed here.
No other channel values are permitted in Step 6b.

| Frame Type | Primary Channel | Fallback Channel |
|------------|----------------|-----------------|
| `decision-briefing` | Meeting | Email-thread |
| `status-update` | Email | Slack-direct |
| `awareness-nudge` | Slack-channel | Artifact |
| `monitor-note` | Artifact | — |
| `displacement-acknowledgment` | Meeting | — (meeting required; no fallback) |

Rule: Fallback channel may only be used when primary channel is explicitly unavailable.
When using fallback, add a note in the Message cell explaining primary unavailability.

FAIL_WRONG_CHANNEL: any Step 6b row uses a channel not listed as Primary or Fallback
for its assigned Frame Type.
FAIL_NO_CHANNEL: any Step 6b row is missing the Channel column entirely.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using Frame Types from Step 6a and channels from Step 6c only. Timing anchors
must fall within Step 5a derived engagement windows.

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
FAIL_NO_CHANNEL: Channel column absent from the comms table.

---

### Step 7: Gatekeeper completeness check — PM role

| Gatekeeper | Comms Row Present | Blocking Reason Documented | Lead Time Honored |
|------------|------------------|---------------------------|-------------------|
| [name] | yes / no | yes / no | yes / no |

FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing comms row, blocking reason, or timing
violating Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, conflict
resolution pathway entries, trajectory assessments, engagement window derivations,
synthesis readout rows.

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

## V-04 — Org State Machine + Veto Calibration

**Axis**: V-01 (org context state machine) + V-02 (veto probability calibration bands). V-03 axis (channel binding) absent.

**Hypothesis**: Step 0 state machine and Step 4a probability band prefill are mutually non-interfering. Both operate in different structural phases: state machine governs the entry condition before Phase 1; calibration bands govern Step 4 veto ranking in Phase 3. No step-numbering conflicts. Both new gate labels (FAIL_WRONG_STATE, FAIL_UNCALIBRATED_PROBABILITY) coexist with all 36 prior criteria and with each other.

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
Phase 1 output.

| Step | Condition | Action | Terminal State |
|------|-----------|--------|----------------|
| 0.1 | CODEOWNERS present at repo root | Extract teams as primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation has team/org identifiers | Extract from invocation | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output: `[STATE: ORG-RESOLVED-CODEOWNERS]` or `[STATE: ORG-RESOLVED-CONTEXT]` or
`[STATE: ORG-BLOCKED]` before Phase 1 begins. Label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | [type] | [named person or body] | [specific ruling] | [date or milestone] |

FAIL_ONE_PARTY: conflict names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any row missing Resolution Authority, Decision Required,
or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name] | [disrupted approach] | [what this replaces] | [yes / limited / no] |

FAIL_NO_INERTIA: no inertia stakeholders identified when feature displaces existing
workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [use pattern] | [touchpoints] | [explicit non-provision] | [gatekeeper / inertia / neither] |

FAIL_MONOLITH_ASSUMPTION: all users treated as a single segment.
FAIL_NO_NOT_DOING: NOT-doing statement absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing statement present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

| Stakeholder | Power | Interest | Quadrant | Trajectory | Engagement Window | Source | Notes |
|-------------|-------|----------|----------|------------|-------------------|--------|-------|
| [name] | H/M/L | H/M/L | [label] | ascending-toward-advocate / stable / descending-toward-risk: [signal] | [TBD — Step 5a] | [source] | [INERTIA] if applicable |

FAIL_PROSE_ONLY: stakeholder list without grid structure.
FAIL_NO_SOURCE: any row missing Source value.
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
labels (freeform text, raw percentage, or synonyms not exactly matching HIGH / MED / LOW).

---

### Step 4b: Veto risk ranking — PM role

| Rank | Stakeholder | Probability Band | Impact | Mitigation |
|------|-------------|-----------------|--------|------------|
| 1 | [name] | HIGH / MED / LOW | [value] | [strategy] |

Order: HIGH bands first, then MED, then LOW; within band by judgment.

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks mitigation strategy.
FAIL_UNCALIBRATED_PROBABILITY: probability band value not from Step 4a table.

---

### Step 5a: Engagement window derivation — PM role

| Stakeholder / Quadrant | Grid Quadrant | Gatekeeper Lead Time | Derived Engagement Window | Derivation Rationale |
|-----------------------|---------------|---------------------|--------------------------|----------------------|
| [name] | [quadrant] | [from Step 1c, or N/A] | [window] | [rationale] |

Update Phase 3 grid Engagement Window column. Step 6b timing anchors must fall within
derived windows.

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

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this prefill step.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | [name] | decision-briefing | [message] | [relative anchor] |
| Keep Satisfied | [name] | status-update | [message] | [relative anchor] |
| Keep Informed | [name] | awareness-nudge | [message] | [relative anchor] |
| Monitor | [name] | monitor-note | [message] | [relative anchor] |
| [quadrant] | [inertia stakeholder] | displacement-acknowledgment | [preserves current first] | [relative anchor] |

Timing anchors must fall within Step 5a derived windows.

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row lacks a relative timing anchor.

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

**Axis**: V-01 (org state machine) + V-02 (veto calibration bands) + V-03 (comms channel binding). All 36 prior criteria present.

**Hypothesis**: All three new axes are mutually non-interfering. State machine operates at Step 0 (pre-Phase 1). Calibration bands operate at Step 4a (Phase 3 pre-veto). Channel binding operates at Step 6c (comms phase). Three new gate labels (FAIL_WRONG_STATE, FAIL_UNCALIBRATED_PROBABILITY, FAIL_WRONG_CHANNEL) all coexist. No structural conflicts between the new axes or with existing criteria. This variation achieves maximum structural density for Round 14 discovery.

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
| 0.1 | CODEOWNERS present at repo root | Extract teams as primary stakeholder candidates | ORG-RESOLVED-CODEOWNERS |
| 0.2 | CODEOWNERS absent; invocation has team/org identifiers | Extract from invocation | ORG-RESOLVED-CONTEXT |
| 0.3 | Neither source sufficient | Ask: "What org or team is this decision for?" Halt all analysis | ORG-BLOCKED |

Output: `[STATE: ORG-RESOLVED-CODEOWNERS]` or `[STATE: ORG-RESOLVED-CONTEXT]` or
`[STATE: ORG-BLOCKED]` before Phase 1 begins. Label must match the branch actually taken.

FAIL_SILENT_INFERENCE: no state label emitted or analysis proceeds without org resolution.
FAIL_WRONG_STATE: emitted state label does not correspond to the source actually used.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |
|----------|---------|---------|--------|---------------------|-------------------|----------|
| [name] | [group] | [group] | [type] | [named person or body] | [specific ruling] | [date or milestone] |

FAIL_ONE_PARTY: conflict names only one party.
FAIL_NO_RESOLUTION_PATHWAY: any row missing Resolution Authority, Decision Required,
or Deadline.

#### Step 1b: Inertia stakeholder mapping — Strategy role

| Stakeholder | Current Approach | Displaced By | Coalition Capacity |
|-------------|-----------------|--------------|-------------------|
| [name] | [disrupted approach] | [what this replaces] | [yes / limited / no] |

Inertia stakeholders must appear in Phase 3 grid with `[INERTIA]` in Notes column.
They must receive `displacement-acknowledgment` Frame Type in Step 6b.

FAIL_NO_INERTIA: no inertia stakeholders when feature displaces existing workflow.

#### Step 1c: Critical-path gatekeepers — Strategy role

| Gatekeeper | Blocking Reason | Lead Time | Tag |
|------------|----------------|-----------|-----|
| [name] | [reason] | [advance notice] | [CRITICAL PATH -- lead time: X] |

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

- [ ] At least two structural conflicts with two named parties, nature, and complete
      resolution pathway entry
- [ ] At least one inertia stakeholder (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper with lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent.

---

### Phase 2: User segment analysis — UX role

| Segment | Primary Use Pattern | Journey Touchpoints Affected | NOT-Doing Statement | Gatekeeper / Inertia Candidacy |
|---------|--------------------|-----------------------------|--------------------|---------------------------------|
| [name] | [use pattern] | [touchpoints] | [explicit non-provision] | [gatekeeper / inertia / neither] |

For inertia segments: NOT-doing must address what new approach does not preserve.

FAIL_MONOLITH_ASSUMPTION: all users as a single segment.
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

### Step 9: Cross-phase synthesis readout — PM role

One compact row per stakeholder. Inline attribution: `field: value (Step X / C-NN)`.

FAIL_NO_SYNTHESIS: synthesis step absent.
FAIL_NO_ATTRIBUTION: any cell lacking fused inline citation.

| Stakeholder | Grid Position | Engagement Window | Conflict Exposure | Champion Status | Comms Frame Type |
|-------------|--------------|-------------------|------------------|-----------------|------------------|
| [name] | grid position: [quadrant] (Phase 3 / C-02) | engagement window: [window] (Step 5a / C-30) | conflict exposure: [exposure] (Step 1a / C-06) | champion status: [status] (Step 5c / C-27) | comms frame type: [type] (Step 6a / C-13) |
```

---

## New gate labels introduced this round

| Label | Variation | Step | Distinct From |
|-------|-----------|------|---------------|
| FAIL_WRONG_STATE | V-01, V-04, V-05 | Step 0 | FAIL_SILENT_INFERENCE (C-01): existing label fires when org context is assumed silently; FAIL_WRONG_STATE fires when a state label is emitted but does not match the actual source used |
| FAIL_UNCALIBRATED_PROBABILITY | V-02, V-04, V-05 | Step 4a/4b | FAIL_WRONG_ORDER: existing label fires on rank ordering; FAIL_UNCALIBRATED_PROBABILITY fires when probability values are not from the defined band set |
| FAIL_WRONG_CHANNEL | V-03, V-05 | Step 6c/6b | FAIL_SAME_FRAME: existing label fires on duplicate Frame Type; FAIL_WRONG_CHANNEL fires when channel violates the Frame Type → Channel binding |
| FAIL_NO_CHANNEL | V-03, V-05 | Step 6b | FAIL_NO_CHANNEL fires when Channel column is absent from the comms table entirely |

## Predicted scoring under v14

All five variations include C-33 (parseable format), C-34 (attributed synthesis rows),
C-35 (pre-phase format constraint propagation), and C-36 (attribution-fused synthesis
notation). All five are predicted to score 230/230 on the existing rubric.

New gate labels are candidates for C-37 through C-40 in v15.

| Variation | Predicted v14 Score | New Gate Labels Present |
|-----------|---------------------|------------------------|
| V-01 | 230/230 | FAIL_WRONG_STATE |
| V-02 | 230/230 | FAIL_UNCALIBRATED_PROBABILITY |
| V-03 | 230/230 | FAIL_WRONG_CHANNEL, FAIL_NO_CHANNEL |
| V-04 | 230/230 | FAIL_WRONG_STATE, FAIL_UNCALIBRATED_PROBABILITY |
| V-05 | 230/230 | FAIL_WRONG_STATE, FAIL_UNCALIBRATED_PROBABILITY, FAIL_WRONG_CHANNEL, FAIL_NO_CHANNEL |
