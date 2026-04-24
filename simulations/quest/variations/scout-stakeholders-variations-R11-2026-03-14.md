monitor the situation."

FAIL_WRONG_ORDER: Rows not sorted by probability descending.
FAIL_NO_MITIGATION: Any row missing a mitigation entry.

---

### Step 5a: Engagement window derivation — PM role

Your goal here is to convert the static signals from Phase 1 and Phase 3 into per-quadrant
receptiveness windows that constrain when Step 6b timing can land.

For each quadrant, synthesize:
- Quadrant posture (high-power stakeholders need longer lead; low-interest stakeholders
  have a narrow window near the decision date)
- Gatekeeper lead times from Step 1c (these set the floor on Earliest Engage for any
  quadrant containing a critical-path gatekeeper)
- Inertia rule: inertia stakeholders' windows must open before public announcement,
  regardless of quadrant position

| Quadrant | Earliest Engage | Latest Engage | Constraint Rationale |
|----------|----------------|---------------|----------------------|
| Manage Closely | | | |
| Keep Satisfied | | | |
| Keep Informed | | | |
| Monitor | | | |

After completing this table, copy each window range into the Engagement Window column
of the Phase 3 grid.

FAIL_NO_WINDOW_SUMMARY: You did not produce the per-quadrant window table.

---

### Step 5b: Champion identification and action — PM role

As you identify your champion, think about access: who has the organizational reach to
move this feature past the blockers you identified in Step 1a and Step 4? For each
champion, specify a concrete schedulable action — a specific meeting type, a demo slot,
a co-presentation, an early access offer.

"Engage the champion" is not a champion action. If you cannot put it on a calendar
today, it does not qualify.

FAIL_GENERIC_CHAMPION: Champion identified without a schedulable action.

---

### Step 5c: Champion depth scoring — PM role

Before you commit to this champion as your primary mover, score the relationship
across three dimensions. Your goal is to replace subjective confidence with a
structured fitness check.

| Dimension | Score (1–5) |
|-----------|------------|
| Authority | |
| Proximity | |
| Commitment | |
| **Composite** | |

Gate: Composite >= 9 to treat as primary champion. Below 9: document as supporting
evidence and identify a secondary candidate.

FAIL_BELOW_CHAMPION_THRESHOLD: Composite < 9, no secondary champion identified.

---

### Step 5d: Champion durability — PM role

As you assess the champion relationship, think about its lifecycle — not just its
current strength. Two questions to answer:

1. **Succession path**: If this champion leaves or is reassigned mid-feature, who
   steps into the role? Name them or explicitly document the SPOF risk.
2. **Deterioration signals**: What would you observe that would tell you the
   commitment is eroding? Name at least two concrete triggers (missed syncs,
   delegated decisions, reduced response cadence, competing priority announcements).

FAIL_NO_DURABILITY: Succession path absent or fewer than two deterioration signals.

---

### Step 6a: Frame Type prefill — PM role

Before you populate any comms rows, establish your accepted Frame Type vocabulary
here. Your goal is to make Frame Type a constraint, not a content-time judgment call.

| Quadrant | Accepted Frame Types |
|----------|---------------------|
| Manage Closely | `decision-briefing`, `co-design-invite`, `risk-alignment` |
| Keep Satisfied | `status-assurance`, `executive-summary` |
| Keep Informed | `progress-update`, `feature-preview` |
| Monitor | `awareness-notice` |

Values not in this table are prohibited in Step 6b.

**Rule 1**: Each comms row uses exactly one Frame Type from this table. No two rows
share the same value.
**Rule 2**: All inertia-classified rows get `displacement-acknowledgment` here, at
this prefill step. Do not defer this assignment to Step 6b content time.

FAIL_MISSING_DISPLACEMENT_PREFILL: Inertia row Frame Type not assigned at this step.

---

### Step 6b: Communication strategy per quadrant — PM role

As you build the comms table, your goal is a row per quadrant that names the message,
the delivery format, the timing, and the channel — with timing that falls within the
window you derived in Step 5a.

| Quadrant | Message | Frame Type | Timing | Channel |

Rules:
- Four rows, one per quadrant. Frame Type from Step 6a only. Distinct per row.
- Timing must be a specific relative anchor that falls within the Step 5a window
  for that quadrant. Vague anchors do not qualify.
- Inertia rows: `displacement-acknowledgment`, timing within their derived window.

FAIL_SAME_FRAME: Two or more rows share a Frame Type.
FAIL_VAGUE_TIMING: Timing is not a specific relative anchor.
FAIL_WINDOW_MISMATCH: Timing falls outside the Step 5a derived window for the quadrant.

---

### Step 7: Gatekeeper completeness check — PM role

As you run this check, your goal is to verify that every critical-path gatekeeper
you identified in Step 1c has a visible presence across all three structural surfaces.

Verify each gatekeeper appears in:
- Phase 3 grid (quadrant assigned, source recorded)
- Step 4 veto list (if blocking power present)
- Step 6b comms table (timing within their engagement window)

Any gap triggers an amendment.

FAIL_GATEKEEPER_INCOMPLETE: Any critical-path gatekeeper absent from grid, veto list,
or comms table.

---

### Step 8: Amendment phase — PM role

As you run the amendment pass, your discipline is this: every finding requires an
update. An observation that does not produce a structural change is not an amendment —
it is a note, and notes decay.

Run at least one amendment pass. Look for missed stakeholders, collapsed conflicts,
champion gaps, and window mismatches.

**Amendment mandate**: Update the affected structural level immediately on discovery —
no observation without revision. Amendment-eligible targets:
- Phase 3 grid rows
- Step 4 veto list entries
- Step 6a prefill table (Frame Type reassignment)
- Step 6b comms rows
- Step 1c gatekeeper lead-time tags
- Conflict resolution pathway entries (Authority, Decision Required, Deadline)
- Step 5a engagement window summaries

No observation without revision.

**Amendment execution rule — read both forms before proceeding:**

> **Bad form (do not do this):**
> "Realized the Infrastructure team should probably be included. Will note
> and come back to this after the design review."

> **Correct form (required):**
> - Phase 3 grid: `Infrastructure Lead | High | Medium | Manage Closely | — |
>   [Manage Closely window from Step 5a] | amendment`
> - Step 4: Add veto entry — `Infrastructure Lead | Medium | Architecture hold |
>   Schedule 5-week-early technical alignment session`
> - Step 6a: Confirm `decision-briefing` for Infrastructure Lead row
> - Step 6b: `Manage Closely | Technical architecture alignment | decision-briefing |
>   5 weeks before launch (within Manage Closely window) | 1:1 with Infra lead`
> - Step 5a: If Infrastructure Lead's lead time shifts Manage Closely floor,
>   revise window summary
> - Resolution pathway: If Infrastructure scope creates a conflict with another
>   team, add resolution pathway row with Authority, Decision, Deadline

FAIL_OBSERVATION_ONLY: Finding noted without updating any structural artifact.

---

## V-05 — Dense synthesis + gatekeeper trajectory probe

**Axes**: (1) Maximum structural density — every requirement stated once, precisely, with no narrative padding. (2) Gatekeeper trajectory extension — Step 7 gains a Section B with per-gatekeeper trajectory ratings (Trending Engaged / Stalling / Trending Opposed + last-observed signal + date), amendment-eligible, bonded to the amendment mandate and correct-form example. Hypothesis: all 30 criteria present at maximum compression; trajectory extension is additive and orthogonal — a variation can satisfy C-08 (static lead time) and C-25 (point-in-time mitigation) with no directional signal evidence (trajectory FAIL). This probes a new C-31 candidate.

---

```
## scout-stakeholders

---

### Step 0: Org context check — PM role

Check for CODEOWNERS. If absent, check invocation string for org/team/feature context.
If neither: ask one question — "What org or team is this decision for?" — and wait.
Do not infer org structure and proceed.

FAIL_SILENT_INFERENCE: Proceeding without explicit org context.

---

### Step 1a: Structural conflicts and resolution pathways — Strategy role

Identify two or more structural conflicts. Each entry requires both parties named,
nature of tension stated, and a resolution pathway:

| Conflict | Party A | Party B | Nature | Resolution Authority | Decision Required | Deadline |

- Resolution Authority: specific person or role (not a committee)
- Decision Required: specific ruling needed
- Deadline: named date or milestone

FAIL_ONE_PARTY: Conflict entry missing Party A or Party B.
FAIL_NO_RESOLUTION_PATHWAY: Any conflict missing Authority, Decision Required, or Deadline.

---

### Step 1b: Inertia stakeholder mapping — Strategy role

Identify stakeholders whose workflow, budget, or role is disrupted by this feature:

| Stakeholder | Current Dependency | Feature Disruption | Mitigation Hypothesis |

Structural consequences (all mandatory):
1. Each row → `[INERTIA]` in Phase 3 grid
2. Each row → `displacement-acknowledgment` Frame Type in Step 6b
3. Assignment in Step 6a prefill — not at Step 6b content time

FAIL_NO_INERTIA: No inertia stakeholders identified.

---

### Step 1c: Critical-path gatekeepers — Strategy role

| Stakeholder | Tag | Lead Time | Blocking Reason |

Tag format: `[CRITICAL PATH -- lead time: X]`. Lead times feed Step 5a derivation.

FAIL_NO_GATEKEEPER_TIMING: Any entry missing lead time or blocking reason.

---

### Phase 1 → Phase 2 Transition Gate — PM role

- [ ] Two+ conflicts, both parties named, resolution pathway complete per conflict
- [ ] One+ inertia stakeholders with dependency, disruption, mitigation
- [ ] All critical-path gatekeepers with lead times and blocking reasons

FAIL_INCOMPLETE_PHASE1: Any item absent. Do not begin Phase 2.

---

### Phase 2: User segment analysis — UX role

For each distinct user segment (minimum two):

1. Segment name and primary goal (specific class, not "users")
2. Journey intervention point (current workflow step where feature acts)
3. Adoption friction (specific barrier for this segment)
4. NOT-doing statement: "This feature does not [X] for [segment], by design."

Each segment requires its own NOT-doing statement. "Out of scope" does not qualify.

FAIL_MONOLITH_ASSUMPTION: All segments collapsed into one group.
FAIL_NO_NOT_DOING: No NOT-doing statement produced for any segment.

---

### Phase 2 → Phase 3 Transition Gate — PM role

- [ ] Two+ distinct segments with NOT-doing statement and adoption friction each
- [ ] Segment analysis covers all user classes material to the decision

FAIL_INCOMPLETE_PHASE2: Any item absent. Do not build the grid.

---

### Phase 3: Power/Interest grid — PM role

Build after Phase 1 and Phase 2 complete. Do not build before both phases are done.

| Name | Power | Interest | Quadrant | INERTIA | Engagement Window | Source |

- Quadrant: Manage Closely / Keep Satisfied / Keep Informed / Monitor
- INERTIA: `[INERTIA]` for all Step 1b rows; blank otherwise
- Engagement Window: populated in Step 5a — blank here
- Source: `CODEOWNERS` / `initial-inventory` / `conflict-discovery` /
  `amendment` / `ux-discovery`

Minimum four rows. Every row requires quadrant, power, interest, and source values.

FAIL_PROSE_ONLY: Stakeholders listed as prose.
FAIL_NO_SOURCE: Any row missing Source.
FAIL_NO_ENGAGEMENT_WINDOW: Engagement Window column absent.

---

### Step 4: Veto risk ranking — PM role

| Rank | Stakeholder | Probability | Impact | Mitigation |

Ordered by Probability descending. Each row requires probability, impact, and a
concrete mitigation strategy.

FAIL_WRONG_ORDER: Rows not sorted by probability descending.
FAIL_NO_MITIGATION: Any row missing mitigation.

---

### Step 5a: Engagement window derivation — PM role

Synthesize per-quadrant engagement windows from:
- Quadrant posture (high-power: longer open; low-interest: narrower near decision)
- Step 1c gatekeeper lead times (floor on Earliest Engage per affected quadrant)
- Inertia rule: inertia windows open before public announcement

| Quadrant | Earliest Engage | Latest Engage | Constraint Rationale |
|----------|----------------|---------------|----------------------|
| Manage Closely | | | |
| Keep Satisfied | | | |
| Keep Informed | | | |
| Monitor | | | |

Copy window ranges into the Phase 3 Engagement Window column.

FAIL_NO_WINDOW_SUMMARY: Per-quadrant window table absent.

---

### Step 5b: Champion identification and action — PM role

One or more champions with a concrete schedulable action per champion.
"Engage the champion" does not qualify. Action must be calendar-placeable.

FAIL_GENERIC_CHAMPION: Champion identified without a schedulable action.

---

### Step 5c: Champion depth scoring — PM role

| Dimension | Score (1–5) |
|-----------|------------|
| Authority | |
| Proximity | |
| Commitment | |
| **Composite** | |

Gate: Composite >= 9 = primary champion. Below 9 = supporting evidence; name a
secondary champion candidate.

FAIL_BELOW_CHAMPION_THRESHOLD: Composite < 9, no secondary champion named.

---

### Step 5d: Champion durability — PM role

1. Succession path: named successor or explicit SPOF documentation
2. Deterioration signals: two or more observable commitment triggers

FAIL_NO_DURABILITY: Succession path absent or fewer than two signals.

---

### Step 6a: Frame Type prefill — PM role

Accepted Frame Types (values not listed here are prohibited in Step 6b):

| Quadrant | Accepted Frame Types |
|----------|---------------------|
| Manage Closely | `decision-briefing`, `co-design-invite`, `risk-alignment` |
| Keep Satisfied | `status-assurance`, `executive-summary` |
| Keep Informed | `progress-update`, `feature-preview` |
| Monitor | `awareness-notice` |

Rule 1: One Frame Type per comms row; no duplicates across rows.
Rule 2: All inertia rows: `displacement-acknowledgment` assigned here, before Step 6b.

FAIL_MISSING_DISPLACEMENT_PREFILL: Inertia row Frame Type not assigned at this step.

---

### Step 6b: Communication strategy per quadrant — PM role

| Quadrant | Message | Frame Type | Timing | Channel |

- Four rows (one per quadrant)
- Frame Type from Step 6a; distinct per row
- Timing: specific relative anchor within the Step 5a derived window for the quadrant
- Inertia rows: `displacement-acknowledgment`, timing within inertia-derived window

FAIL_SAME_FRAME: Two or more rows share a Frame Type.
FAIL_VAGUE_TIMING: Timing is not a specific relative anchor.
FAIL_WINDOW_MISMATCH: Timing falls outside the Step 5a derived window for the quadrant.

---

### Step 7: Gatekeeper completeness check and trajectory — PM role

**Section A — Completeness**

Verify each critical-path gatekeeper from Step 1c appears in:
- Phase 3 grid (quadrant assigned)
- Step 4 veto list (if blocking power present)
- Step 6b comms table (timing in-window)

FAIL_GATEKEEPER_INCOMPLETE: Any critical-path gatekeeper absent from any of the three
surfaces above.

**Section B — Trajectory**

For each critical-path gatekeeper, record a directional commitment signal:

| Gatekeeper | Trajectory | Last-Observed Signal | Signal Date |
|------------|-----------|---------------------|------------|

- Trajectory values: `Trending Engaged` / `Stalling` / `Trending Opposed`
- Last-Observed Signal: a specific, concrete behavioral indicator — not an impression
  (e.g., "attended architecture review, asked two follow-up questions" qualifies;
  "seems positive" does not)
- Signal Date: the date of the last concrete observation

Trajectory entries are amendment-eligible. A gatekeeper's status can shift from
Trending Engaged to Stalling between amendment passes. Update accordingly.

FAIL_NO_TRAJECTORY: Section B absent or any gatekeeper row missing trajectory,
signal, or date.

---

### Step 8: Amendment phase — PM role

Run at least one amendment pass. Every finding requires a structural update.

**Amendment mandate**: Update the affected structural level immediately on discovery —
no observation without revision. Amendment-eligible targets:
- Phase 3 grid rows
- Step 4 veto list entries
- Step 6a prefill table (Frame Type reassignment)
- Step 6b comms rows
- Step 1c gatekeeper lead-time tags
- Conflict resolution pathway entries (Authority, Decision Required, Deadline)
- Step 5a engagement window summaries
- Step 7 gatekeeper trajectory entries

No observation without revision.

**Amendment execution rule — read both forms before proceeding:**

> **Bad form (do not do this):**
> "Platform team may need to review. Will follow up. Security lead seems less engaged
> lately — might be worth noting."

> **Correct form (required):**
> - Phase 3 grid: `Platform Lead | High | High | Manage Closely | — |
>   [Manage Closely window] | amendment`
> - Step 4: `Platform Lead | High | Architecture block | Schedule 6-week-early
>   design alignment`
> - Step 6a: `decision-briefing` confirmed for Platform Lead row
> - Step 6b: `Manage Closely | Architecture design alignment | decision-briefing |
>   6 weeks before launch (within Manage Closely window) | 1:1 with Platform Lead`
> - Step 5a: If Platform Lead lead time (6 weeks) revises Manage Closely floor,
>   update window summary
> - Resolution pathway: If Platform approval creates an authority conflict, add
>   pathway row with Authority, Decision Required, Deadline
> - Step 7 trajectory: `Security Lead | Stalling | Missed last two architecture
>   syncs; delegated decision to report | 2026-03-10`

FAIL_OBSERVATION_ONLY: Finding noted without updating any structural artifact.
```

---

## Variation summary

| Variation | Axis | Hypothesis | C-30 | Trajectory probe |
|-----------|------|-----------|------|-----------------|
| V-01 | Phrasing register — rationale-narrative | Rationale context per step does not interfere with FAIL density (C-17) or role heading binding (C-23) | Present | Absent |
| V-02 | Output format — schema-first | Schema-before-rules format satisfies all 30 criteria including C-14 and C-17 with FAIL labels inside constraint tables | Present | Absent |
| V-03 | Inertia framing elevated | "Hidden competitor" as opening conceptual frame reinforces C-18 without displacing C-01 or any structural criterion | Present | Absent |
| V-04 | Lifecycle emphasis + coaching register | Expanded per-segment sub-steps in Phase 2 + second-person facilitative voice satisfy C-07, C-10, C-17, C-23 without structural interference | Present | Absent |
| V-05 | Dense synthesis + gatekeeper trajectory probe | Maximum compression of all 30 + trajectory extension (C-31 candidate): Trending Engaged / Stalling / Trending Opposed per gatekeeper, distinct from C-08 (static lead time) and C-25 (point-in-time mitigation) | Present | Present (C-31 candidate) |
