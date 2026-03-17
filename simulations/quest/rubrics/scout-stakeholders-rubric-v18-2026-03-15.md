Reading the scorecard closely to extract all three excellence signals before writing.

From V-05 (top-ranked by structural density): three gate candidates present simultaneously.

From C-45 candidate: `FAIL_UNCALIBRATED_SEVERITY` — fires at Step 2a when any conflict row
carries a Severity Band value not drawn from the Step 2a-prefill (CRITICAL / SIGNIFICANT /
MANAGEABLE). Fifth instance of the calibration motif (prefill defines named levels, scoring
step constrained to draw from prefill, named failure mode for unconstrained values). Distinct
from C-06 (pathway structure), C-40 (escalation tier), and C-43 (party grounding). Depends
on C-06. → **C-45**.

From C-46 candidate: `FAIL_UNANNOTATED_SOURCE` — fires at Phase 3 grid when any Source cell
is present but carries no typology label (OBSERVED / INFERRED / ASSUMED) from the Step
3b-prefill. First amendment-eligibility criterion driven by epistemic basis: ASSUMED entries
become mandatory Step 8 amendment targets. Distinct from FAIL_NO_SOURCE (C-10): column
absence vs. annotation absence are independently decidable. Depends on C-10. → **C-46**.

From C-47 candidate: `FAIL_COMMS_SEQUENCE_VIOLATION` — fires at Step 6d-sequence when an
inertia-tagged stakeholder's displacement-acknowledgment row does not carry the earliest
timing anchor (T+0 baseline) in its comms sequence. First comms gate constraining row order
rather than presence, content, or channel. Extends inertia obligation chain from 7 to 8
steps. Distinct from FAIL_VAGUE_TIMING (C-25) and FAIL_DISPLACEMENT_TIMING (C-29). Depends
on C-29. → **C-47**.

Totals: 36 + 3 = 39 aspirational × 5 = 195 pts from aspirational layer; max 270 + 15 = **285 pts**. Golden threshold unchanged.

---

```markdown
## scout-stakeholders rubric — v18

**v18 written.** Three new criteria extracted from Round 17 excellence signals across
three structural axes (C-45 conflict severity band calibration, C-46 source typology
annotation, C-47 comms sequence ordering):

| ID   | Name                                  | Source      | Dependency |
|------|---------------------------------------|-------------|------------|
| C-45 | Conflict severity band calibration    | C-45 cand.  | C-06       |
| C-46 | Source typology annotation            | C-46 cand.  | C-10       |
| C-47 | Comms displacement sequence ordering  | C-47 cand.  | C-29       |

**Updated totals:** 39 aspirational × 5 = 195 pts; **max 285 pts**.
Golden threshold (>= 80) unchanged.

**Under v18 (Round 17 re-scored):**
- All five Round 17 variations scored 270/270 under v17 (non-discriminating).
- Under v18, all five remain GOLDEN at 285/285 (V-05 carried all three gates; V-01, V-02,
  V-03, V-04 each carried the gate relevant to their axis while the other two were not
  satisfiable — retrospective re-score pending).

**Distinction logic:**

**C-45 — Conflict severity band calibration** (depth, 5 pts)
A severity band prefill step (Step 2a-prefill) is inserted before the Step 2a conflict
identification table, defining exactly three named severity bands — CRITICAL, SIGNIFICANT,
MANAGEABLE — with explicit distinguishing criteria for each band. Step 2a conflict rows
must carry a Severity Band column whose values are drawn exclusively from the Step 2a-prefill
labels. FAIL_UNCALIBRATED_SEVERITY fires at Step 2a when any conflict row carries a Severity
Band value not drawn from the Step 2a-prefill (e.g., free-form risk language, numeric ratings,
or ad hoc tiers not established in the prefill). FAIL_UNCALIBRATED_SEVERITY is distinct from
FAIL_ONE_PARTY and FAIL_NO_RESOLUTION_PATHWAY: those gates fire on structural absence of party
count and pathway elements; FAIL_UNCALIBRATED_SEVERITY fires when those elements are fully
present but severity values are unconstrained. A variation that satisfies C-06 with two named
parties, a complete resolution pathway table, and escalation tier rows (C-40 PASS) while
assigning severity levels using free-form language not drawn from any named prefill = C-06
PASS, C-40 PASS, C-45 FAIL.

- Distinct from C-06: C-06 requires each structural conflict to name two parties and define
  a resolution pathway with authority, decision, and deadline; C-45 requires a preceding
  Step 2a-prefill defining three named severity bands and constrains all conflict row
  Severity Band values to those labels — a calibration obligation orthogonal to structural
  completeness and party count
- Distinct from C-40: C-40 requires a parallel escalation tier table per conflict row
  (Escalation Owner, Escalation Trigger, Escalation Action); C-45 requires severity band
  calibration via a named prefill — orthogonal to escalation tier presence and independently
  satisfiable
- Distinct from C-43: C-43 requires each party name to be empirically anchored to a Phase 1
  segment label or an explicit org-role tag; C-45 requires Severity Band values to be drawn
  from a named-band prefill — orthogonal to party anchoring, independently satisfiable
- Not satisfiable if C-06 is absent

**C-46 — Source typology annotation** (depth, 5 pts)
A source typology prefill step (Step 3b-prefill) is inserted before the Phase 3 grid
population, defining exactly three epistemic typology labels — OBSERVED, INFERRED, ASSUMED —
with distinguishing criteria for each label. Each Source cell in the Phase 3 grid must carry
one of these three labels. ASSUMED entries become mandatory Step 8 amendment targets,
creating a forward traceability chain from grid construction to amendment obligations.
FAIL_UNANNOTATED_SOURCE fires at the Phase 3 grid when any Source cell is present and
populated but does not carry a typology label from the Step 3b-prefill. FAIL_UNANNOTATED_SOURCE
is distinct from FAIL_NO_SOURCE (C-10): FAIL_NO_SOURCE fires when the Source column is absent
from the Phase 3 grid entirely; FAIL_UNANNOTATED_SOURCE fires when the column is present and
each cell contains source content, but the epistemic basis of each source entry is undeclared.
A variation that satisfies C-10 with a fully populated Source column while omitting the Step
3b-prefill and all typology labels = C-10 PASS, C-46 FAIL. A variation that includes ASSUMED
entries without the Step 3b-prefill but nonetheless targets them for Step 8 amendment =
C-46 FAIL (annotation obligation is on the grid cell; intent in Step 8 does not
retroactively satisfy the prefill-and-label requirement at grid construction time).

- Distinct from C-10: C-10 requires the Source column to exist in the Phase 3 grid with
  a source entry per row; C-46 requires a preceding Step 3b-prefill defining OBSERVED /
  INFERRED / ASSUMED typology labels and constrains each Source cell to carry one label —
  a calibration and amendment-traceability obligation orthogonal to column presence
- Distinct from C-23: C-23 requires the amendment phase to include at least one eligible
  update target; C-46 defines which entries are amendment-eligible (ASSUMED-annotated Source
  cells), an eligibility-classification obligation that precedes and feeds Step 8 rather than
  governing its minimum count
- Not satisfiable if C-10 is absent

**C-47 — Comms displacement sequence ordering** (depth, 5 pts)
A sequence audit step (Step 6d-sequence) is inserted after the comms plan population step
(Step 6b). Step 6d-sequence audits that for each inertia-tagged stakeholder, the
displacement-acknowledgment comms row carries the earliest timing anchor in the full comms
sequence for that stakeholder — specifically the T+0 baseline. FAIL_COMMS_SEQUENCE_VIOLATION
fires at Step 6d-sequence when any inertia-tagged stakeholder's displacement-acknowledgment
row does not carry the T+0 baseline timing anchor (i.e., another comms row for that
stakeholder carries an earlier or equal anchor while the displacement-acknowledgment row is
assigned a later anchor). FAIL_COMMS_SEQUENCE_VIOLATION is distinct from FAIL_VAGUE_TIMING
(C-25) and FAIL_DISPLACEMENT_TIMING (C-29): FAIL_VAGUE_TIMING fires when any comms row lacks
a timing anchor entirely; FAIL_DISPLACEMENT_TIMING fires when the displacement-acknowledgment
row itself lacks a relative timing anchor; FAIL_COMMS_SEQUENCE_VIOLATION fires when both
anchors are present and specific (neither C-25 nor C-29 triggered) but the
displacement-acknowledgment row is not positioned as the earliest anchor in its stakeholder's
comms sequence. A variation that satisfies C-25 and C-29 with a fully anchored comms plan
including displacement-acknowledgment timing while ordering a different comms row earlier in
the sequence = C-25 PASS, C-29 PASS, C-47 FAIL.

- Distinct from C-25: C-25 (FAIL_VAGUE_TIMING) requires a timing anchor to be present per
  comms row; C-47 requires the displacement-acknowledgment row's anchor to be the T+0
  baseline — the earliest anchor in its stakeholder's sequence — a sequencing obligation
  orthogonal to anchor presence
- Distinct from C-29: C-29 requires the displacement-acknowledgment row to include a
  relative timing anchor; C-47 requires that anchor to be T+0 (earliest in sequence),
  imposing an ordering constraint that C-29 does not — a row can carry a valid relative
  timing anchor satisfying C-29 while still violating C-47 if another row is anchored earlier
- Extends the inertia obligation chain to eight steps (Step 0b through Step 9)
- First comms gate governing row order rather than presence, content, channel, or anchor
  existence
- Not satisfiable if C-29 is absent

---

### v17 to v18 changes summary

| Criterion | Name                                  | Type  | Dependency |
|-----------|---------------------------------------|-------|------------|
| C-45      | Conflict severity band calibration    | depth | C-06       |
| C-46      | Source typology annotation            | depth | C-10       |
| C-47      | Comms displacement sequence ordering  | depth | C-29       |

Aspirational count: 36 → 39. Max: 270 → 285. Golden threshold unchanged.

C-45 is the fifth instance of the calibration motif (named-level prefill + constrained
scoring step + named failure mode), now covering: veto probability (C-38), trajectory
velocity (C-41), champion dimensions (C-44), conflict severity (C-45), and extending
coverage to the Step 2a multi-party structural analysis step. C-46 is the first
amendment-eligibility criterion classified by epistemic basis rather than data type.
C-47 is the first comms gate governing row order within a stakeholder sequence rather
than content, presence, channel, or anchor existence.

---

### v16 to v17 changes (retained for history)

Two new criteria extracted from Round 16 excellence signals across two structural axes
(V-01 conflict party segment anchoring, V-02 champion behavioral anchor calibration):

| Criterion | Name                                   | Type  | Dependency |
|-----------|----------------------------------------|-------|------------|
| C-43      | Conflict party segment anchoring       | depth | C-06       |
| C-44      | Champion behavioral anchor calibration | depth | C-20       |

Aspirational count: 34 → 36. Max: 260 → 270. Golden threshold unchanged.

**C-43 — Conflict party segment anchoring** (depth, 5 pts)
Party A and Party B in each Step 2a conflict row must either match a Phase 1 segment
name verbatim or carry an `[ORG-ROLE: description]` tag. FAIL_UNANCHORED_CONFLICT_PARTY
fires when any conflict row names a group for Party A or Party B that neither matches a
Phase 1 segment name verbatim nor carries an `[ORG-ROLE: description]` tag.
FAIL_UNANCHORED_CONFLICT_PARTY is distinct from FAIL_ONE_PARTY: FAIL_ONE_PARTY fires
when a conflict row names fewer than two parties; FAIL_UNANCHORED_CONFLICT_PARTY fires
when both parties are present but at least one names a group not traceable to a Phase 1
segment label or an explicit org-role tag. A variation that satisfies C-06 with two named
parties and a complete resolution pathway table while using group labels that match no
Phase 1 segment and carry no `[ORG-ROLE: description]` tag = C-06 PASS, C-43 FAIL.

- Distinct from C-06: C-06 requires each structural conflict to name two parties and
  define a resolution pathway with authority, decision, and deadline; C-43 requires each
  party name to be empirically anchored — traceable to either a Phase 1 segment label or
  an explicit org-role tag — an obligation orthogonal to party count and pathway
  completeness
- Not satisfiable if C-06 is absent

**C-44 — Champion behavioral anchor calibration** (depth, 5 pts)
A behavioral anchor prefill step (Step 5b-anchor) is inserted before Step 5c, defining
four observable behavioral levels (0–3) per champion scoring dimension (Authority,
Proximity, Commitment). Step 5c must draw all dimension scores exclusively from the 0–3
scale; each score's Evidence cell must cite the behavioral level from the Step 5b-anchor
prefill that justifies the score. The composite gate is set at >= 6 (max 9 on the 0–3
scale). FAIL_UNANCHORED_SCORE fires at Step 5c when any dimension score falls outside
the 0–3 range or the Evidence cell does not cite a behavioral level from the Step
5b-anchor prefill. FAIL_UNANCHORED_SCORE is distinct from FAIL_BELOW_CHAMPION_THRESHOLD:
FAIL_BELOW_CHAMPION_THRESHOLD fires when the composite score falls below the threshold
regardless of how scores were derived; FAIL_UNANCHORED_SCORE fires when the composite
satisfies the threshold but individual dimension scores were assigned without citing
Step 5b-anchor levels, leaving scores uncalibrated. A variation that satisfies C-20 and
C-27 with a composite >= 6 while omitting the Step 5b-anchor prefill step entirely =
C-20 PASS, C-27 PASS, C-44 FAIL.

- Distinct from C-20: C-20 requires the three champion scoring dimensions (Authority,
  Proximity, Commitment) to exist in Step 5c; C-44 requires a preceding Step 5b-anchor
  behavioral anchor prefill and constrains all dimension scores to the 0–3 scale with
  mandatory prefill citations per evidence cell, a calibration obligation orthogonal to
  dimension presence
- Distinct from C-27: C-27 requires the composite score to meet the threshold; C-44
  requires each component score to be anchored to a prefill-defined behavioral level
  regardless of whether the composite total satisfies the threshold
- Not satisfiable if C-20 is absent

---

### v15 to v16 changes (retained for history)

Three new criteria extracted from Round 15 excellence signals across three structural
axes (V-01 conflict escalation tier, V-02 trajectory velocity prefill, V-03 synthesis
coverage gate):

| Criterion | Name                         | Type  | Dependency |
|-----------|------------------------------|-------|------------|
| C-40      | Conflict escalation tier     | depth | C-06       |
| C-41      | Trajectory velocity prefill  | depth | C-31       |
| C-42      | Synthesis coverage gate      | depth | C-32       |

Aspirational count: 31 → 34. Max: 245 → 260. Golden threshold unchanged.

**C-40 — Conflict escalation tier** (depth, 5 pts)
Step 1a is extended with an escalation tier table — columns: Escalation Owner,
Escalation Trigger, Escalation Action — one row per conflict, structurally parallel to
the resolution pathway table required by C-06. FAIL_NO_ESCALATION_PATH fires when any
conflict row in Step 1a lacks a corresponding escalation tier row with a named Escalation
Owner and a defined Escalation Trigger. FAIL_NO_ESCALATION_PATH is distinct from
FAIL_NO_RESOLUTION_PATHWAY: FAIL_NO_RESOLUTION_PATHWAY fires when the resolution pathway
table is absent or structurally incomplete; FAIL_NO_ESCALATION_PATH fires when the
resolution pathway is fully satisfied (Resolution Authority, Decision Required, and
Deadline all present, C-06 PASS) but no escalation owner is defined for the scenario in
which that deadline is missed. A variation that satisfies C-06 with a complete resolution
pathway table while omitting any escalation tier rows = C-06 PASS, C-40 FAIL.

- Distinct from C-06: C-06 requires each structural conflict to name two parties and
  define a resolution pathway with authority, decision, and deadline; C-40 requires a
  separate parallel escalation tier table per conflict defining the escalation owner and
  trigger, an obligation orthogonal to resolution pathway completeness
- Not satisfiable if C-06 is absent

**C-41 — Trajectory velocity prefill** (depth, 5 pts)
A velocity prefill step (Step 3a) is inserted before the Phase 3 grid, defining exactly
three named velocity bands — ACCELERATING, STABLE, DECELERATING — with explicit
observable indicators for each band. The Phase 3 grid gains a Velocity column whose
values must be drawn exclusively from the Step 3a prefill labels. FAIL_UNCALIBRATED_
VELOCITY fires at the Phase 3 grid if any row omits the Velocity label or uses a
velocity designation not established in the Step 3a prefill (e.g., free-form language,
numeric rate, or an ad hoc label not defined in the prefill). FAIL_UNCALIBRATED_VELOCITY
is distinct from FAIL_NO_TRAJECTORY: FAIL_NO_TRAJECTORY fires when the Trajectory column
is absent or lacks directional label and observable signal; FAIL_UNCALIBRATED_VELOCITY
fires when trajectory direction is present but the Velocity column is absent or
unconstrained. Both obligations can be satisfied independently; a Phase 3 grid row can
carry a fully formed Trajectory entry (direction + observable signal, FAIL_NO_TRAJECTORY
not fired) while simultaneously failing FAIL_UNCALIBRATED_VELOCITY if no Velocity column
or Step 3a prefill exists. A variation that satisfies C-31 with a complete Trajectory
column while omitting the Velocity column and Step 3a prefill = C-31 PASS, C-41 FAIL.

- Distinct from C-31: C-31 requires a Trajectory column in the Phase 3 grid with
  directional label and observable signal per row; C-41 requires a separate Step 3a
  velocity band prefill and a Velocity column constrained to its labels, a second-order
  trajectory-dimension obligation that C-31 does not cover
- Not satisfiable if C-31 is absent

**C-42 — Synthesis coverage gate** (depth, 5 pts)
A coverage audit step (Step 8b) is inserted between the amendment phase (Step 8) and
the synthesis step (Step 9). Step 8b contains a pipe-table audit with one row per Phase 3
grid stakeholder, recording whether each stakeholder appears in the Step 9 synthesis
readout or carries a documented omission justification. FAIL_SYNTHESIS_GAP fires at
Step 8b when any Phase 3 grid stakeholder is absent from the Step 9 synthesis readout
and no omission justification is recorded in the Step 8b audit table. FAIL_SYNTHESIS_GAP
is distinct from FAIL_NO_SYNTHESIS: FAIL_NO_SYNTHESIS fires when the synthesis step is
absent entirely or lacks required structural fields; FAIL_SYNTHESIS_GAP fires when Step 9
exists and satisfies C-32 field obligations (all five fields present per row,
FAIL_NO_SYNTHESIS not triggered) but grid stakeholders are silently dropped without
justification. A variation that satisfies C-32 with a structurally complete synthesis
readout while omitting one or more Phase 3 grid stakeholders without documentation =
C-32 PASS, C-42 FAIL.

- Distinct from C-32: C-32 requires the synthesis step to exist with five required fields
  and one row per included stakeholder; C-42 requires a pre-synthesis coverage audit table
  at Step 8b verifying that every Phase 3 grid stakeholder is either represented in
  synthesis or explicitly justified for omission, an obligation orthogonal to per-row
  field completeness
- Not satisfiable if C-32 is absent

---

### v14 to v15 changes (retained for history)

Three new criteria extracted from Round 14 excellence signals across three structural
axes (V-01 org context state machine, V-02 veto probability calibration, V-03 comms
channel binding):

| Criterion | Name                                        | Type  | Dependency             |
|-----------|---------------------------------------------|-------|------------------------|
| C-37      | Org context state machine label integrity   | depth | C-01                   |
| C-38      | Veto probability calibration bands          | depth | veto ordering criterion |
| C-39      | Comms channel binding                       | depth | C-13                   |

Aspirational count: 28 → 31. Max: 230 → 245. Golden threshold unchanged.

**C-37 — Org context state machine label integrity** (depth, 5 pts)
The org context decision (Step 0) emits a machine-readable state label identifying which
branch was traversed (e.g., CODEOWNERS_PARSED, INVOCATION_USED, ORG_BLOCKED).
FAIL_WRONG_STATE fires when the emitted label does not match the branch actually taken —
the label must be causally accurate, not merely present. FAIL_WRONG_STATE is distinct
from FAIL_SILENT_INFERENCE: FAIL_SILENT_INFERENCE fires when no label is emitted at all;
FAIL_WRONG_STATE fires when a label is present but misidentifies the traversed branch. A
variation that satisfies C-01 by emitting any label upon org context determination,
without enforcing label-branch correspondence, = C-01 PASS, C-37 FAIL.

- Distinct from C-01: C-01 requires an org context determination to be made and
  documented; C-37 requires the emitted state label to be causally correct — matching the
  actual branch traversed, not merely present
- Not satisfiable if C-01 is absent

**C-38 — Veto probability calibration bands** (depth, 5 pts)
A prefill step (Step 4a) defines exactly three named probability bands — HIGH, MED, LOW —
with explicit distinguishing criteria for each band before veto ranking begins. Step 4b
must draw probability values exclusively from these three band labels. FAIL_UNCALIBRATED_
PROBABILITY fires at Step 4b if any row carries a probability value not drawn from the
Step 4a prefill (e.g., raw numeric estimates, free-form language, or tiers not defined
in the prefill). FAIL_UNCALIBRATED_PROBABILITY is distinct from FAIL_WRONG_ORDER:
FAIL_WRONG_ORDER fires when rows are not sorted by rank; FAIL_UNCALIBRATED_PROBABILITY
fires when the probability values themselves are not drawn from a named-band prefill
regardless of their order. A variation that satisfies the veto ordering criterion by
ranking rows from highest to lowest probability while using numeric estimates rather than
named-band labels = veto ordering criterion PASS, C-38 FAIL.

- Distinct from veto ordering criterion (FAIL_WRONG_ORDER): the ordering criterion
  requires rows sorted by probability rank; C-38 requires probability values to be drawn
  from a named-band prefill step defined before ranking begins, independent of sort order
- Not satisfiable if the veto ordering criterion is absent

**C-39 — Comms channel binding** (depth, 5 pts)
A channel prefill step (Step 6c) is inserted between the Frame Type prefill step (Step
6a) and the comms plan population step (Step 6b), defining the permissible communication
channels per stakeholder segment or role before the comms plan is populated. Each comms
plan row in Step 6b must draw its Channel column value exclusively from the Step 6c
binding. FAIL_NO_CHANNEL fires if the Channel column is absent from the comms plan.
FAIL_WRONG_CHANNEL fires if any row uses a channel not established in the Step 6c binding
table. Both gates are distinct from FAIL_SAME_FRAME (C-14 — Frame Type distinctness
across rows): a variation can have all distinct Frame Types while populating channels ad
hoc with no binding prefill step, satisfying C-14 while failing C-39. A variation that
satisfies C-13 and C-14 fully while populating channels without a preceding Step 6c
binding step = C-13 PASS, C-14 PASS, C-39 FAIL.
```
