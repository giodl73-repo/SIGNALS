
## Round 10 Variations — scout-stakeholders

**Target rubric**: v10 (max 195 pts)
**Goal**: First variation to achieve 195/195 by combining C-27 (champion depth scoring), C-28 (champion durability), and C-29 (conflict resolution pathway) with all 26 prior criteria.

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | All 29 combined | Merging R9 V-01 (champion depth+durability) with R9 V-03 (resolution pathway) achieves 195/195 with no interference |
| V-02 | C-29 deliberately absent | Single-axis isolation: confirms C-29 is the missing 5 pts from R9 V-01 (target: 190/195) |
| V-03 | C-27 + C-28 deliberately absent | Single-axis isolation: confirms champion chain is the missing 10 pts from R9 V-03 (target: 185/195) |
| V-04 | All 29 + engagement window (potential C-30) | New per-quadrant engagement window derivation step adds a timing-in-window gate distinct from C-05; coexists with all 29 |
| V-05 | All 29 + gatekeeper trajectory (potential C-30) | New temporal signal tracking per critical-path gatekeeper at Step 7; distinct from C-08 (lead times) and C-25 (mitigation) |

---

## V-01 — All 29 Criteria Combined

**Axis**: First attempt at 195/195. Merges the champion depth scoring + durability chain (Step 5b, Step 5c) from R9 V-01 with the conflict resolution pathway table (Step 1a extension) from R9 V-03. All 26 prior criteria intact.

**Hypothesis**: C-27 + C-28 + C-29 are mutually non-interfering. Step 1a extension (resolution pathway table) lives in a different structural layer from Steps 5b-5c (champion quantification). Phase 1→2 gate checklist extension for resolution pathway verification is compatible with FAIL_INCOMPLETE_PHASE1 coverage. Amendment mandate can enumerate all three new target classes alongside the prior six.

```
Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: CODEOWNERS context check — PM role

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

Identify at least two structural conflicts relevant to this feature decision. For each conflict:

1. Name the stakeholder groups in tension (two named parties minimum).
2. State the nature of the tension (budget, timeline, scope, authority, methodology, etc.).
3. Complete the resolution pathway entry in the table below.

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|
| [conflict name: Party A vs Party B] | [who has decision-making power to resolve] | [specific ruling needed to unblock] | [date or milestone] |

Resolution Authority is the named person or body with legitimate power to close the
conflict. Decision Required is the specific determination, not a general area of concern.
Deadline is the latest date or milestone at which the conflict must be resolved for the
feature to proceed.

FAIL_ONE_PARTY: a conflict names only one stakeholder — a single-stakeholder risk is
not a structural conflict.
FAIL_NO_RESOLUTION_PATHWAY: a conflict is named without a complete resolution pathway
entry (Authority, Decision Required, and Deadline all required).

#### Step 1b: Inertia stakeholder mapping — Strategy role

Identify stakeholders whose primary relationship to this feature is resistance born from
displacement of their current approach. For each inertia stakeholder:

- Name the stakeholder or group.
- Document their current approach (what they do today that this feature disrupts).
- Document the displaced-by field: what this feature replaces or threatens.
- Note coalition capacity: can they recruit other resistors?

Inertia stakeholders must appear in the Phase 3 grid with the `[INERTIA]` tag in the
Notes column. They must receive the `displacement-acknowledgment` Frame Type in the
Step 6b comms table. These assignments are not optional.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an
existing workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

Identify stakeholders whose approval or non-objection is required before this feature
can ship. For each gatekeeper:

- Tag them `[CRITICAL PATH -- lead time: X]` where X is the minimum advance notice
  required to engage them (e.g., "6 weeks", "sprint-before-launch").
- State the blocking reason (compliance sign-off, budget approval, security review,
  architecture board, etc.).

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Before proceeding to Phase 2, confirm all Phase 1 outputs are present:

- [ ] At least two structural conflicts identified, each with two named parties and a
      nature statement
- [ ] Resolution pathway entry complete for each conflict (Authority, Decision Required,
      Deadline)
- [ ] At least one inertia stakeholder identified, or an explicit statement that no
      current-approach displacement applies
- [ ] At least one critical-path gatekeeper identified with a lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output is absent. Do not begin Phase 2
until this gate clears.

---

### Phase 2: User segment analysis — UX role

For each relevant user segment:

1. Name the segment and its primary use pattern for this feature area.
2. Describe the journey touchpoints affected by this decision.
3. Write one NOT-doing statement: what this product explicitly does not provide for
   this segment within this decision scope. Generic "out of scope" language is not a
   NOT-doing statement.
4. Note any segment-specific friction that makes them a gatekeeper candidate or an
   inertia stakeholder candidate.

For inertia-classified segments: the NOT-doing statement must address what the new
approach does not preserve from the current approach — not only what is new.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single undifferentiated segment.
FAIL_NO_NOT_DOING: omitting the NOT-doing statement for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Before proceeding to Phase 3, confirm all Phase 2 outputs are present:

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing statement present for each segment
- [ ] Inertia segment displacement NOT-doing addressed, if inertia stakeholders were
      identified in Phase 1

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output is absent. Do not build the grid
until this gate clears.

---

### Phase 3: Power/Interest grid — PM role

Build the Power/Interest grid now — after Phase 1 and Phase 2 are complete.

| Stakeholder | Power | Interest | Quadrant | Source | Notes |
|-------------|-------|----------|----------|--------|-------|
| ...         | H/M/L | H/M/L    | [label]  | [origin] | [INERTIA] if applicable |

Grid requirements:
- Minimum 4 rows.
- Quadrant labels: Manage Closely / Keep Satisfied / Keep Informed / Monitor.
- Source column values: `CODEOWNERS`, `initial-inventory`, `conflict-discovery`,
  `amendment`, `ux-discovery`.
- Inertia-classified stakeholders must carry `[INERTIA]` in the Notes column.

FAIL_PROSE_ONLY: stakeholder list presented as prose without a grid structure.
FAIL_NO_SOURCE: any row is missing a Source value.

---

### Step 4: Veto risk ranking — PM role

List all stakeholders who could veto or block this decision. Order by probability —
highest first. Do not order alphabetically or by grid sequence.

| Rank | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| 1    | ...         | ...         | ...    | ...        |

Each entry must include a mitigation strategy alongside probability and impact.
A veto list with probability and impact but no mitigation column is incomplete.

FAIL_WRONG_ORDER: entries are not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.

---

### Step 5a: Champion identification and action — PM role

Identify one or more champions: stakeholders who have organizational standing to
advocate for this feature and a concrete stake in its success.

For each champion, specify a schedulable action — a calendar-ready commitment that
advances the feature. Examples: "secure a 20-minute demo slot in the Q2 planning
meeting," "request co-presenter status at the architectural review board," "arrange
early access for the pilot group and document outcomes."

Generic "engage the champion" or "leverage the relationship" is not a champion action.

FAIL_GENERIC_CHAMPION: a champion is named without a schedulable action.

---

### Step 5b: Champion depth scoring — PM role

For each champion identified in Step 5a, complete the scoring table:

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Authority — organizational power to commit resources or override objections | | |
| Proximity — direct access to the blockers and sponsors who matter | | |
| Commitment — demonstrated investment in this feature's success (past actions) | | |
| **Composite** | **(sum)** | **Gate: composite >= 9 required to proceed as primary champion** |

Scoring guide: 1 = absent or symbolic; 3 = credible but limited; 5 = strong and demonstrated.

If the composite score is below 9: this stakeholder is supporting evidence, not a
primary mover. Document who can serve as primary champion, or declare the feature
champion-deficient and note the risk.

FAIL_BELOW_CHAMPION_THRESHOLD: composite score below 9 with no alternative primary
champion identified and no champion-deficiency risk documented.

---

### Step 5c: Champion durability — PM role

Assess the temporal continuity of the champion relationship.

**Succession path**: If the identified champion leaves this project or organization,
who assumes the champion role? Name the successor candidate or explicitly document
that no succession path exists and note the single-point-of-failure risk.

**Deterioration signals**: Identify one or more observable triggers that would indicate
champion commitment is eroding before it becomes a crisis. Examples: missed syncs
without explanation, feature decisions delegated to non-champions, reduced response
velocity on feature-related asks, public hedging in planning forums.

FAIL_NO_DURABILITY: succession path is absent AND no deterioration signals are documented.

---

### Step 6a: Frame Type prefill constraint — PM role

Before populating the communication table, establish the permitted Frame Type values.
The prefill table below defines the constraint. Only values listed here are permitted
in Step 6b. Values not in this table are prohibited in the comms rows.

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest: needs the full decision picture before acting |
| `status-update` | High-power, low-interest: headline and ask only; no supporting detail |
| `awareness-nudge` | Low-power, high-interest: keep invested and informed without burdening |
| `monitor-note` | Low-power, low-interest: minimal; send only when a threshold event occurs |
| `displacement-acknowledgment` | Inertia stakeholders: lead with what is preserved, then what changes |

Rule 1: Each row in Step 6b must use a distinct Frame Type. No two rows may share the
same Frame Type value.
Rule 2: The `displacement-acknowledgment` Frame Type is mandatory for all
inertia-classified rows. This assignment must be made here, in the prefill step, before
any comms row is populated.
Rule 3: Any row assigned `displacement-acknowledgment` must address what the current
approach preserves — not only what is new or changed.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist in the grid but
`displacement-acknowledgment` is not assigned in this prefill step before content
population.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate the communication table using only Frame Types from the Step 6a prefill table.

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | ... | decision-briefing | ... | 3 weeks before milestone |
| Keep Satisfied | ... | status-update | ... | 1 week before milestone |
| Keep Informed | ... | awareness-nudge | ... | Same week as announcement |
| Monitor | ... | monitor-note | ... | Day of release |
| [inertia row] | ... | displacement-acknowledgment | ... | Pre-announcement |

Each row must include a timing value with a relative anchor (e.g., "3 weeks before
sprint-end", "day of release", "pre-announcement"). "ASAP" and "TBD" are not timing
values.

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row has a timing value without a relative anchor.

---

### Step 7: Gatekeeper completeness check — PM role

For each critical-path gatekeeper identified in Step 1c:

- Confirm a comms row is present in Step 6b.
- Confirm the blocking reason is documented.
- Confirm the lead time from Step 1c is honored: Step 6b timing must not violate the
  minimum advance-notice constraint.

FAIL_GATEKEEPER_INCOMPLETE: a critical-path gatekeeper has no comms row, has a missing
blocking reason, or has a Step 6b timing that violates the Step 1c lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment is required. An amendment is a finding that changes the
stakeholder landscape: a new stakeholder added, an existing stakeholder reframed or
promoted, a conflict resolved or escalated, a veto risk re-ranked, a resolution pathway
authority or deadline updated, a champion assessment revised.

**Amendment mandate**: Update the affected structural level immediately on discovery —
no observation without revision. Eligible update targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags, and
conflict resolution pathway entries (Resolution Authority, Decision Required, Deadline).
Enumerating a finding without updating at least one of these targets is not an amendment.

**Amendment anti-pattern — read both forms before proceeding:**

> **Bad form**: "Noted that the Security team raised concerns about data residency
> scoping during architecture review. This may affect the roadmap timeline."
>
> *(Observation only. No structural level updated. No grid row changed. No veto rank
> revised. No resolution pathway updated. This is not an amendment.)*

> **Correct form**: "Security team elevated data residency concern at architecture
> review (source: architecture-review-meeting-2026-03-12).
> — Grid: Security Team row updated from Keep Informed to Manage Closely
>   (Source column: `amendment`).
> — Veto list: Security Team moved from Rank 3 to Rank 1; mitigation updated to
>   'schedule data-residency compliance session before sprint-end.'
> — Resolution pathway: Decision Required updated to 'Approval of data-residency-
>   compliant storage approach'; Deadline updated to 'end of current sprint.'
> — Step 6a prefill: Frame Type for Security Team row confirmed as `decision-briefing`.
> — Step 6b: Security Team comms timing updated to '4 weeks before milestone.'
> — Amendment logged: Security team elevated from informed to decision-maker due to
>   residency scope expansion confirmed at architecture review."
>
> *(All affected structural levels updated. Resolution pathway revised. Finding traceable.)*

After the amendment pass, audit all `initial-inventory` rows in the Source column.
Any row still carrying `initial-inventory` after the amendment pass is a visible gap —
either confirm the stakeholder with a citation or flag for follow-up.

FAIL_OBSERVATION_ONLY: a finding is documented without updating any structural level.
```

---

## V-02 — C-29 Deliberately Absent

**Axis**: Single-axis isolation of C-29. All 26 prior criteria present. Champion depth scoring (C-27) and champion durability (C-28) present. Conflict resolution pathway (C-29) absent: Step 1a names conflicts with parties and nature but provides no resolution pathway table. FAIL_NO_RESOLUTION_PATHWAY not present. Phase 1→2 gate checklist does not include resolution pathway verification. Amendment mandate does not enumerate conflict resolution pathway entries.

**Hypothesis**: This variation scores 190/195 — matching the R9 V-01 score under v10. Confirms C-29 is the sole criterion distinguishing V-01 from a 195 score, and that its omission does not disturb C-27 or C-28.

```
Map the stakeholder landscape for a product decision. Follow this sequence exactly:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: CODEOWNERS context check — PM role

Check for a CODEOWNERS file at the repository root. If present, extract org context
from the file: teams named as owners are primary stakeholder candidates. If CODEOWNERS
is absent, check the invocation context string for team or org identifiers. If neither
source provides sufficient org context, ask exactly one question: "What org or team is
this decision for?" Do not infer silently. Do not proceed on an assumed org structure.

FAIL_SILENT_INFERENCE: proceeding with an assumed org context when CODEOWNERS is absent
and invocation context is insufficient.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts — Strategy role

Identify at least two structural conflicts relevant to this feature decision. For each
conflict:

1. Name the stakeholder groups in tension (two named parties minimum).
2. State the nature of the tension (budget, timeline, scope, authority, methodology).

FAIL_ONE_PARTY: a conflict names only one stakeholder — a single-stakeholder risk is
not a structural conflict.

#### Step 1b: Inertia stakeholder mapping — Strategy role

Identify stakeholders whose primary relationship to this feature is resistance born from
displacement of their current approach. For each inertia stakeholder:

- Name the stakeholder or group.
- Document their current approach (what they do today that this feature disrupts).
- Document the displaced-by field: what this feature replaces or threatens.
- Note coalition capacity: can they recruit other resistors?

Inertia stakeholders must appear in the Phase 3 grid with the `[INERTIA]` tag. They
must receive the `displacement-acknowledgment` Frame Type in the comms table.

FAIL_NO_INERTIA: no inertia stakeholders identified when the feature displaces an
existing workflow or toolchain.

#### Step 1c: Critical-path gatekeepers — Strategy role

Identify stakeholders whose approval is required before this feature can ship. For each
gatekeeper:

- Tag them `[CRITICAL PATH -- lead time: X]`.
- State the blocking reason.

FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Before proceeding to Phase 2, confirm all Phase 1 outputs are present:

- [ ] At least two structural conflicts identified, each with two named parties and a
      nature statement
- [ ] At least one inertia stakeholder identified (or explicit no-displacement statement)
- [ ] At least one critical-path gatekeeper identified with a lead-time tag

FAIL_INCOMPLETE_PHASE1: any required Phase 1 output is absent. Do not begin Phase 2
until this gate clears.

---

### Phase 2: User segment analysis — UX role

For each relevant user segment:

1. Name the segment and its primary use pattern.
2. Describe the journey touchpoints affected by this decision.
3. Write one NOT-doing statement: what this product explicitly does not provide for
   this segment. Generic "out of scope" is not a NOT-doing statement.
4. Note gatekeeper or inertia candidacy.

For inertia-classified segments: the NOT-doing statement must address what the new
approach does not preserve from the current approach.

FAIL_MONOLITH_ASSUMPTION: treating all users as a single segment.
FAIL_NO_NOT_DOING: omitting the NOT-doing statement for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Before proceeding to Phase 3, confirm all Phase 2 outputs are present:

- [ ] At least two distinct user segments analyzed
- [ ] NOT-doing statement present for each segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required Phase 2 output is absent. Do not build the grid
until this gate clears.

---

### Phase 3: Power/Interest grid — PM role

Build the Power/Interest grid now — after Phase 1 and Phase 2 are complete.

| Stakeholder | Power | Interest | Quadrant | Source | Notes |
|-------------|-------|----------|----------|--------|-------|
| ...         | H/M/L | H/M/L    | [label]  | [origin] | [INERTIA] if applicable |

Requirements: 4+ rows, quadrant labels, Source column
(`CODEOWNERS` / `initial-inventory` / `conflict-discovery` / `amendment` /
`ux-discovery`), `[INERTIA]` tag for inertia-classified stakeholders.

FAIL_PROSE_ONLY: stakeholder list without a grid structure.
FAIL_NO_SOURCE: any row missing a Source value.

---

### Step 4: Veto risk ranking — PM role

List all stakeholders who could block this decision. Order by probability — highest
first.

| Rank | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| 1    | ...         | ...         | ...    | ...        |

Each entry must include a mitigation strategy.

FAIL_WRONG_ORDER: entries not ordered by probability rank.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.

---

### Step 5a: Champion identification and action — PM role

Identify one or more champions with organizational standing and a concrete stake in
this feature's success. Specify a schedulable action for each champion.

FAIL_GENERIC_CHAMPION: a champion is named without a schedulable action.

---

### Step 5b: Champion depth scoring — PM role

For each champion, complete the scoring table:

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Authority — power to commit resources or override objections | | |
| Proximity — access to blockers and sponsors | | |
| Commitment — demonstrated investment (past actions) | | |
| **Composite** | **(sum)** | **Gate: composite >= 9 to proceed as primary champion** |

If composite < 9: document who can serve as primary champion or declare the feature
champion-deficient.

FAIL_BELOW_CHAMPION_THRESHOLD: composite below 9 with no alternative or risk statement.

---

### Step 5c: Champion durability — PM role

**Succession path**: Name who assumes the champion role if the current champion departs.
If no successor exists, document the single-point-of-failure risk.

**Deterioration signals**: Identify observable triggers indicating champion commitment
is eroding (e.g., missed syncs, delegated decisions, reduced response velocity).

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

Define the permitted Frame Type values before populating the comms table.

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` is mandatory for inertia rows — assign here,
before any row is populated.
Rule 3: `displacement-acknowledgment` rows must address what the current approach
preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment`
not assigned in this prefill step.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using only Frame Types from Step 6a.

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | ... | decision-briefing | ... | 3 weeks before milestone |
| Keep Satisfied | ... | status-update | ... | 1 week before milestone |
| Keep Informed | ... | awareness-nudge | ... | Announcement week |
| Monitor | ... | monitor-note | ... | Day of release |
| [inertia] | ... | displacement-acknowledgment | ... | Pre-announcement |

Timing requires a relative anchor. "ASAP" and "TBD" are not timing values.

FAIL_SAME_FRAME: two or more rows share the same Frame Type.
FAIL_VAGUE_TIMING: any row has no relative timing anchor.

---

### Step 7: Gatekeeper completeness check — PM role

For each critical-path gatekeeper from Step 1c: confirm comms row present, blocking
reason documented, and Step 6b timing honors the Step 1c lead-time constraint.

FAIL_GATEKEEPER_INCOMPLETE: gatekeeper has no comms row, missing blocking reason, or
timing that violates the lead time.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required.

**Amendment mandate**: Update the affected structural level on discovery — no
observation without revision. Eligible targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags.

**Amendment anti-pattern:**

> **Bad form**: "Security team raised data residency concerns. May affect timeline."
>
> *(Observation only. No structural level updated.)*

> **Correct form**: "Security team elevated at architecture review.
> — Grid: updated to Manage Closely (Source: `amendment`).
> — Veto list: moved to Rank 1; mitigation revised.
> — Step 6a prefill: confirmed `decision-briefing`.
> — Step 6b: timing updated to '4 weeks before milestone.'
> — Amendment logged: escalation confirmed at architecture review."
>
> *(All affected structural levels updated. Prefill round-trip confirmed.)*

After amendment pass, audit all `initial-inventory` Source rows. Unrevised rows are
visible gaps.

FAIL_OBSERVATION_ONLY: finding documented without updating any structural level.
```

---

## V-03 — C-27 + C-28 Deliberately Absent

**Axis**: Single-axis isolation of the champion chain. All 26 prior criteria present. Conflict resolution pathway (C-29) present. Champion depth scoring (C-27) and champion durability (C-28) absent: Step 5 has only Step 5a (champion with concrete action). No scoring table at Step 5b, no durability gate at Step 5c.

**Hypothesis**: This variation scores 185/195 — matching the R9 V-03 score under v10. Confirms C-27 and C-28 together are the missing 10 pts from that configuration, and that their removal does not disturb C-29.

```
Map the stakeholder landscape for a product decision. Follow this sequence:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
both Phase 1 and Phase 2 are complete.

---

### Step 0: CODEOWNERS context check — PM role

Check for a CODEOWNERS file at the repository root. Extract org context from it
if present. If absent, check the invocation context string. If neither provides
sufficient context, ask exactly one question: "What org or team is this decision
for?" Do not infer silently. Do not proceed on an assumed org structure.

FAIL_SILENT_INFERENCE: proceeding with an assumed org when no source provides context.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

Identify at least two structural conflicts. For each:

1. Name both stakeholder groups in tension.
2. State the nature of the tension.
3. Complete the resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|
| [Party A vs Party B] | [decision-maker] | [specific ruling] | [date/milestone] |

FAIL_ONE_PARTY: conflict names only one stakeholder.
FAIL_NO_RESOLUTION_PATHWAY: conflict named without a complete pathway entry.

#### Step 1b: Inertia stakeholder mapping — Strategy role

Identify stakeholders facing displacement from their current approach.

- Name the stakeholder.
- Document their current approach and the displaced-by field.
- Note coalition capacity.

Inertia stakeholders require `[INERTIA]` tag in the grid and `displacement-acknowledgment`
Frame Type in the comms table.

FAIL_NO_INERTIA: no inertia stakeholders when the feature displaces an existing workflow.

#### Step 1c: Critical-path gatekeepers — Strategy role

Tag each required approver `[CRITICAL PATH -- lead time: X]` and state the blocking
reason.

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Confirm all Phase 1 outputs are present:

- [ ] Two or more conflicts, each with two named parties, nature, and resolution pathway
- [ ] Inertia stakeholder identified or no-displacement stated
- [ ] Critical-path gatekeeper(s) identified with lead-time tags

FAIL_INCOMPLETE_PHASE1: any required output absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

For each segment:

1. Name the segment and use pattern.
2. Describe affected journey touchpoints.
3. Write one NOT-doing statement (what this feature explicitly does not provide for
   this segment).
4. Note gatekeeper or inertia candidacy.

Inertia segment NOT-doing must address what the new approach does not preserve.

FAIL_MONOLITH_ASSUMPTION: single undifferentiated user segment.
FAIL_NO_NOT_DOING: NOT-doing statement absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Confirm all Phase 2 outputs are present:

- [ ] Two or more distinct segments analyzed
- [ ] NOT-doing statement per segment
- [ ] Inertia segment displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required output absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

Build the grid after both Phase 1 and Phase 2 are complete.

| Stakeholder | Power | Interest | Quadrant | Source | Notes |
|-------------|-------|----------|----------|--------|-------|
| ...         | H/M/L | H/M/L    | [label]  | [origin] | [INERTIA] if applicable |

Requirements: 4+ rows, quadrant labels, Source column
(`CODEOWNERS` / `initial-inventory` / `conflict-discovery` / `amendment` /
`ux-discovery`), `[INERTIA]` tag for inertia rows.

FAIL_PROSE_ONLY: prose list without grid structure.
FAIL_NO_SOURCE: any row missing Source.

---

### Step 4: Veto risk ranking — PM role

Order all potential blockers by probability — highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| 1    | ...         | ...         | ...    | ...        |

FAIL_WRONG_ORDER: not ordered by probability.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.

---

### Step 5: Champion identification and action — PM role

Identify one or more champions with organizational standing and a concrete stake in
this feature. For each, specify a schedulable action.

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 6a: Frame Type prefill constraint — PM role

Permitted Frame Type values (constraint table — values not listed here are prohibited
in Step 6b):

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here before
content population.
Rule 3: `displacement-acknowledgment` rows must address what the current approach
preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but prefill assignment absent.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using only Frame Types from Step 6a.

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | ... | decision-briefing | ... | 3 weeks before |
| Keep Satisfied | ... | status-update | ... | 1 week before |
| Keep Informed | ... | awareness-nudge | ... | Announcement week |
| Monitor | ... | monitor-note | ... | Day of release |
| [inertia] | ... | displacement-acknowledgment | ... | Pre-announcement |

Each row requires a timing value with a relative anchor.

FAIL_SAME_FRAME: two rows share the same Frame Type.
FAIL_VAGUE_TIMING: timing without a relative anchor.

---

### Step 7: Gatekeeper completeness check — PM role

For each critical-path gatekeeper from Step 1c: comms row present, blocking reason
documented, Step 6b timing within lead-time constraint.

FAIL_GATEKEEPER_INCOMPLETE: any completeness check fails.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required. An amendment changes the stakeholder landscape.

**Amendment mandate**: Update the affected structural level on discovery — no
observation without revision. Eligible targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags,
conflict resolution pathway entries (Authority, Decision, Deadline).

**Amendment anti-pattern:**

> **Bad form**: "Security team raised data residency concerns at architecture review."
>
> *(No structural level updated. Not an amendment.)*

> **Correct form**: "Security team elevated at architecture review.
> — Grid: moved to Manage Closely (Source: `amendment`).
> — Veto list: promoted to Rank 1; mitigation updated.
> — Resolution pathway: Decision Required updated to 'residency-compliant storage
>   approach approval'; Deadline updated to sprint-end.
> — Step 6a prefill: confirmed `decision-briefing` assignment.
> — Step 6b: timing revised to '4 weeks before milestone.'
> — Amendment logged with source and date."
>
> *(All affected levels updated, including resolution pathway entry.)*

After the amendment pass, audit all `initial-inventory` Source rows.
Unrevised rows are visible gaps.

FAIL_OBSERVATION_ONLY: finding documented without updating any structural level.
```

---

## V-04 — All 29 + Stakeholder Engagement Window (Potential C-30)

**Axis**: All 29 criteria present. Adds a new structural layer: per-quadrant engagement window derivation. The Power/Interest grid gains an Engagement Window column. A new step (Step 5a: Engagement window derivation) appears before the Frame Type prefill, establishing the temporal receptiveness constraint for each quadrant. Step 6b timing must fall within the derived window. Champion steps renumber to 5b/5c/5d. Three new FAIL labels introduced.

**Hypothesis**: Engagement window is additive and orthogonal to all 29 criteria. The receptiveness derivation step (5a) establishes a temporal constraint that Step 6b timing must satisfy — distinct from C-05 (timing present) and C-08 (lead times defined): a comms row can pass C-05 (has timing) and fail C-30 (timing falls outside the derived window). V-04 scores 195/195 on all 29 confirmed criteria; the engagement window pattern is the v10 C-30 candidate.

```
Map the stakeholder landscape for a product decision. Follow this sequence:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: CODEOWNERS context check — PM role

Check for a CODEOWNERS file. If absent, check invocation context. If neither provides
org context, ask exactly one question: "What org or team is this decision for?" Do not
infer silently.

FAIL_SILENT_INFERENCE: proceeding without confirmed org context.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

Identify at least two structural conflicts. For each:

1. Name both stakeholder groups in tension.
2. State the nature of the tension.
3. Complete the resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|
| [Party A vs Party B] | [decision-maker] | [specific ruling] | [date/milestone] |

FAIL_ONE_PARTY: conflict names only one stakeholder.
FAIL_NO_RESOLUTION_PATHWAY: conflict named without a complete pathway entry.

#### Step 1b: Inertia stakeholder mapping — Strategy role

Identify stakeholders facing displacement from their current approach.

- Name the stakeholder; document current approach, displaced-by field, coalition capacity.
- Inertia stakeholders require `[INERTIA]` tag in grid and `displacement-acknowledgment`
  Frame Type in comms table.

FAIL_NO_INERTIA: no inertia stakeholders when displacement is present.

#### Step 1c: Critical-path gatekeepers — Strategy role

Tag each required approver `[CRITICAL PATH -- lead time: X]` with blocking reason.

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Confirm Phase 1 outputs:

- [ ] Two or more conflicts with named parties, nature, and resolution pathway
- [ ] Inertia stakeholder identified or no-displacement stated
- [ ] Critical-path gatekeeper(s) with lead-time tags

FAIL_INCOMPLETE_PHASE1: any required output absent.

---

### Phase 2: User segment analysis — UX role

For each segment: name and use pattern, journey touchpoints, NOT-doing statement,
gatekeeper/inertia candidacy. Inertia NOT-doing must address what is not preserved.

FAIL_MONOLITH_ASSUMPTION: single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing statement absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Confirm Phase 2 outputs:

- [ ] Two or more segments analyzed
- [ ] NOT-doing per segment
- [ ] Inertia displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required output absent.

---

### Phase 3: Power/Interest grid — PM role

Build the grid after Phase 1 and Phase 2 are complete. Include an Engagement Window
column identifying the period during which each quadrant is receptive to outreach.

| Stakeholder | Power | Interest | Quadrant | Source | Engagement Window | Notes |
|-------------|-------|----------|----------|--------|-------------------|-------|
| ... | H/M/L | H/M/L | [label] | [origin] | [start] to [end] | [INERTIA] if applicable |

Engagement Window rules:
1. Critical-path gatekeeper windows must close no later than the Step 1c lead time
   permits (i.e., window end <= feature-date minus lead time).
2. Inertia stakeholder windows must open before any public announcement date.
3. Monitor quadrant windows are threshold-triggered; no fixed window required.

FAIL_PROSE_ONLY: prose list without grid structure.
FAIL_NO_SOURCE: any row missing Source.
FAIL_NO_ENGAGEMENT_WINDOW: grid built without Engagement Window column.

---

### Step 5a: Engagement window derivation — PM role

Before proceeding to champion assessment or Frame Type prefill, derive the per-quadrant
engagement window summary from the grid.

| Quadrant | Window Start | Window End | Constraint Source |
|----------|-------------|------------|-------------------|
| Manage Closely | ... | ... | [lead time / decision milestone] |
| Keep Satisfied | ... | ... | [planning cycle / budget gate] |
| Keep Informed | ... | ... | [announcement date] |
| Monitor | (threshold-triggered) | — | — |
| Inertia | ... | ... | [pre-announcement constraint] |

This table is the timing constraint for Step 6b. Every comms row in Step 6b must have
a timing value that falls within the derived window for that stakeholder's quadrant.

FAIL_NO_WINDOW_SUMMARY: Step 5a derivation absent; comms timing is unconstrained.

---

### Step 5b: Champion identification and action — PM role

Identify one or more champions with organizational standing. For each, specify a
schedulable action.

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9 to proceed as primary champion** |

If composite < 9: document alternative primary champion or declare champion-deficiency.

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative or risk documented.

---

### Step 5d: Champion durability — PM role

**Succession path**: Name the successor if champion departs, or document the SPOF risk.

**Deterioration signals**: Observable triggers indicating eroding commitment.

FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented.

---

### Step 6a: Frame Type prefill constraint — PM role

Permitted Frame Type values (constraint table):

| Frame Type | When to Use |
|------------|-------------|
| `decision-briefing` | High-power, high-interest |
| `status-update` | High-power, low-interest |
| `awareness-nudge` | Low-power, high-interest |
| `monitor-note` | Low-power, low-interest |
| `displacement-acknowledgment` | Inertia stakeholders |

Rule 1: Each Step 6b row must use a distinct Frame Type.
Rule 2: `displacement-acknowledgment` mandatory for inertia rows — assign here before
content population.
Rule 3: `displacement-acknowledgment` rows must address what the current approach
preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but prefill assignment absent.

---

### Step 6b: Communication strategy per quadrant — PM role

Populate using only Frame Types from Step 6a. Timing must fall within the Step 5a
derived window for the row's quadrant.

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | ... | decision-briefing | ... | [within window] |
| Keep Satisfied | ... | status-update | ... | [within window] |
| Keep Informed | ... | awareness-nudge | ... | [within window] |
| Monitor | ... | monitor-note | ... | [threshold trigger] |
| [inertia] | ... | displacement-acknowledgment | ... | [pre-announcement] |

FAIL_SAME_FRAME: two rows share the same Frame Type.
FAIL_VAGUE_TIMING: timing without a relative anchor.
FAIL_WINDOW_MISMATCH: timing value falls outside the Step 5a derived window for that
quadrant.

---

### Step 7: Gatekeeper completeness check — PM role

For each critical-path gatekeeper: comms row present, blocking reason documented,
Step 6b timing within lead-time constraint and within Step 5a derived window.

FAIL_GATEKEEPER_INCOMPLETE: any check fails.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required.

**Amendment mandate**: Update the affected structural level on discovery — no
observation without revision. Eligible targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags,
conflict resolution pathway entries, Step 5a engagement window summaries.

**Amendment anti-pattern:**

> **Bad form**: "Security team raised concerns at architecture review. May affect
> timeline."
>
> *(No structural level updated.)*

> **Correct form**: "Security team elevated at architecture review.
> — Grid: moved to Manage Closely; Engagement Window updated to '8 weeks before
>   milestone to 4 weeks before milestone' (Source: `amendment`).
> — Veto list: promoted to Rank 1; mitigation revised.
> — Resolution pathway: updated Decision Required and Deadline.
> — Step 5a: Manage Closely window summary revised to reflect updated constraint.
> — Step 6a prefill: `decision-briefing` confirmed.
> — Step 6b: timing revised to fall within updated window.
> — Amendment logged with source."
>
> *(All affected levels updated. Window summary revised. Prefill round-trip confirmed.)*

After amendment pass, audit all `initial-inventory` Source rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any structural level.
```

---

## V-05 — All 29 + Gatekeeper Risk Trajectory (Potential C-30)

**Axis**: All 29 criteria present. Adds a new structural layer at Step 7: per-gatekeeper risk trajectory assessment. Each critical-path gatekeeper receives a trajectory rating (Trending Engaged / Stalling / Trending Opposed) alongside a last-observed signal (the most recent concrete evidence for that rating). The trajectory rating must be updated in the amendment pass if new signals arrive. Three new FAIL labels.

**Hypothesis**: Gatekeeper trajectory is a temporal stakeholder intelligence pattern distinct from all 29 current criteria. C-08 confirms a gatekeeper exists with a lead time; C-25 provides mitigation for veto risks; gatekeeper trajectory adds a directional commitment signal per gatekeeper with observable evidence — a variation can satisfy C-08 (gatekeeper tagged, lead time stated) with no trajectory rating or signal evidence. This is the candidate for a new criterion: temporal gatekeeper commitment signal with observable evidence and amendment-eligible trajectory entries.

```
Map the stakeholder landscape for a product decision. Follow this sequence:
Phase 1 (Strategy) → Phase 2 (UX) → Phase 3 (PM). Do not build the grid until
Phase 1 and Phase 2 are complete.

---

### Step 0: CODEOWNERS context check — PM role

Check for a CODEOWNERS file. If absent, check invocation context. If neither provides
org context, ask exactly one question: "What org or team is this decision for?" Do not
infer silently.

FAIL_SILENT_INFERENCE: proceeding without confirmed org context.

---

### Phase 1: Strategic analysis — Strategy role

#### Step 1a: Structural conflicts and resolution pathways — Strategy role

Identify at least two structural conflicts. For each:

1. Name both stakeholder groups in tension.
2. State the nature of the tension.
3. Complete the resolution pathway:

| Conflict | Resolution Authority | Decision Required | Deadline |
|----------|---------------------|-------------------|----------|
| [Party A vs Party B] | [decision-maker] | [specific ruling] | [date/milestone] |

FAIL_ONE_PARTY: only one stakeholder named in a conflict.
FAIL_NO_RESOLUTION_PATHWAY: conflict named without a complete pathway entry.

#### Step 1b: Inertia stakeholder mapping — Strategy role

Identify displaced-workflow stakeholders. For each: name, current approach, displaced-by,
coalition capacity. These stakeholders require `[INERTIA]` in grid and
`displacement-acknowledgment` in comms.

FAIL_NO_INERTIA: no inertia stakeholders when feature displaces an existing workflow.

#### Step 1c: Critical-path gatekeepers — Strategy role

Tag each required approver `[CRITICAL PATH -- lead time: X]` with blocking reason.

FAIL_NO_GATEKEEPER_TIMING: gatekeeper named without a lead time.

---

### Phase 1 → Phase 2 Transition Gate — Strategy role

Confirm Phase 1 outputs:

- [ ] Two or more conflicts with named parties, nature, and resolution pathway
- [ ] Inertia stakeholder identified or no-displacement stated
- [ ] Critical-path gatekeeper(s) with lead-time tags

FAIL_INCOMPLETE_PHASE1: any required output absent.

---

### Phase 2: User segment analysis — UX role

For each segment: name and use pattern, journey touchpoints, NOT-doing statement,
gatekeeper/inertia candidacy. Inertia NOT-doing must address what is not preserved.

FAIL_MONOLITH_ASSUMPTION: single undifferentiated segment.
FAIL_NO_NOT_DOING: NOT-doing absent for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

Confirm Phase 2 outputs:

- [ ] Two or more segments analyzed
- [ ] NOT-doing per segment
- [ ] Inertia displacement NOT-doing addressed (if applicable)

FAIL_INCOMPLETE_PHASE2: any required output absent.

---

### Phase 3: Power/Interest grid — PM role

Build the grid after Phase 1 and Phase 2 are complete.

| Stakeholder | Power | Interest | Quadrant | Source | Notes |
|-------------|-------|----------|----------|--------|-------|
| ... | H/M/L | H/M/L | [label] | [origin] | [INERTIA] if applicable |

Requirements: 4+ rows, quadrant labels, Source column, `[INERTIA]` tag for inertia rows.

FAIL_PROSE_ONLY: prose list without grid structure.
FAIL_NO_SOURCE: any row missing Source.

---

### Step 4: Veto risk ranking — PM role

Order all potential blockers by probability — highest first.

| Rank | Stakeholder | Probability | Impact | Mitigation |
|------|-------------|-------------|--------|------------|
| 1    | ...         | ...         | ...    | ...        |

FAIL_WRONG_ORDER: not ordered by probability.
FAIL_NO_MITIGATION: any entry lacks a mitigation strategy.

---

### Step 5a: Champion identification and action — PM role

Identify one or more champions with organizational standing. For each, specify a
schedulable action.

FAIL_GENERIC_CHAMPION: champion named without a schedulable action.

---

### Step 5b: Champion depth scoring — PM role

| Dimension | Score (1-5) | Evidence |
|-----------|-------------|----------|
| Authority | | |
| Proximity | | |
| Commitment | | |
| **Composite** | **(sum)** | **Gate: >= 9 to proceed as primary champion** |

If composite < 9: document alternative or declare champion-deficiency.

FAIL_BELOW_CHAMPION_THRESHOLD: composite < 9 with no alternative or risk documented.

---

### Step 5c: Champion durability — PM role

**Succession path**: Name successor if champion departs, or document SPOF risk.

**Deterioration signals**: Observable triggers indicating eroding commitment.

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
Rule 3: `displacement-acknowledgment` rows must address what the current approach
preserves.

FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but prefill assignment absent.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Stakeholder | Frame Type | Message | Timing |
|----------|-------------|------------|---------|--------|
| Manage Closely | ... | decision-briefing | ... | 3 weeks before |
| Keep Satisfied | ... | status-update | ... | 1 week before |
| Keep Informed | ... | awareness-nudge | ... | Announcement week |
| Monitor | ... | monitor-note | ... | Day of release |
| [inertia] | ... | displacement-acknowledgment | ... | Pre-announcement |

FAIL_SAME_FRAME: two rows share the same Frame Type.
FAIL_VAGUE_TIMING: timing without a relative anchor.

---

### Step 7: Gatekeeper completeness check and trajectory — PM role

For each critical-path gatekeeper from Step 1c, complete both sections:

**Section A — Completeness**: Confirm comms row present, blocking reason documented,
Step 6b timing within lead-time constraint.

**Section B — Trajectory assessment**:

| Gatekeeper | Trajectory | Last Observed Signal | Signal Date |
|------------|------------|----------------------|-------------|
| [name] | Trending Engaged / Stalling / Trending Opposed | [concrete observable evidence] | [date] |

Trajectory ratings:
- **Trending Engaged**: recent positive signals (responded to outreach, attended review,
  forwarded feature to their team, increased meeting attendance).
- **Stalling**: ambiguous signals (delayed responses, delegated to subordinates,
  absent from scheduled touchpoints, hedged language in forums).
- **Trending Opposed**: recent negative signals (escalated concerns to their manager,
  publicly questioned the approach, withdrew from the review process).

Last Observed Signal must be a concrete observable event, not an inference. "Seems
interested" is not a signal. "Attended architecture review and asked clarifying
questions" is a signal.

FAIL_GATEKEEPER_INCOMPLETE: comms row absent, blocking reason missing, or lead-time
constraint violated.
FAIL_NO_TRAJECTORY: gatekeeper completeness check present but trajectory rating and
last observed signal absent.

---

### Step 8: Amendment phase — PM role

Minimum one amendment required.

**Amendment mandate**: Update the affected structural level on discovery — no
observation without revision. Eligible targets: grid rows, veto list entries,
Step 6a prefill table, Step 6b comms rows, Step 1c gatekeeper lead-time tags,
conflict resolution pathway entries, Step 7 gatekeeper trajectory entries.

**Amendment anti-pattern:**

> **Bad form**: "Security team raised concerns at architecture review."
>
> *(No structural level updated.)*

> **Correct form**: "Security team escalated at architecture review.
> — Grid: moved to Manage Closely (Source: `amendment`).
> — Veto list: promoted to Rank 1; mitigation updated.
> — Resolution pathway: Decision Required and Deadline updated.
> — Step 6a prefill: `decision-briefing` confirmed.
> — Step 6b: timing revised to '4 weeks before milestone.'
> — Step 7 trajectory: updated from Stalling to Trending Opposed;
>   Last Observed Signal: 'Escalated data-residency scope to VP Engineering
>   during architecture review (2026-03-12).'
> — Amendment logged with source."
>
> *(All levels updated. Trajectory entry revised. Prefill round-trip confirmed.)*

After amendment pass, audit all `initial-inventory` Source rows.

FAIL_OBSERVATION_ONLY: finding documented without updating any structural level.
```

---

## Scoring Predictions (under v10 rubric, max 195)

| Variation | Predicted Score | C-27 | C-28 | C-29 | New Pattern |
|-----------|----------------|------|------|------|-------------|
| V-01 | 195/195 | PASS | PASS | PASS | — |
| V-02 | 190/195 | PASS | PASS | absent | — |
| V-03 | 185/195 | absent | absent | PASS | — |
| V-04 | 195/195 | PASS | PASS | PASS | Engagement window (C-30 candidate) |
| V-05 | 195/195 | PASS | PASS | PASS | Gatekeeper trajectory (C-30 candidate) |

---

## New C-30 Candidates

| ID | Name | Source | Distinction |
|----|------|--------|-------------|
| C-30a | Stakeholder engagement window | V-04 | Per-quadrant receptiveness window column in grid; derivation step before Frame Type prefill; timing-in-window validation (FAIL_WINDOW_MISMATCH); distinct from C-05 (timing present) and C-08 (lead times): a row can pass both with timing outside the derived window |
| C-30b | Gatekeeper risk trajectory | V-05 | Per-gatekeeper trajectory rating (Trending Engaged / Stalling / Trending Opposed) + last observed signal + signal date at Step 7; amendment-eligible trajectory entries; distinct from C-08 (lead times), C-25 (veto mitigation): trajectory tracks directional commitment, not static risk |
