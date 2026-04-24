Reading the scorecard closely to extract three excellence signals before writing.

From V-01: `FAIL_UNCALIBRATED_PRIORITY` — fires at Step 6b when any comms row carries a
Priority Band value not drawn from the Step 6e-priority prefill (URGENT / STANDARD /
DEFERRED). Sixth instance of the calibration motif. Distinct from FAIL_VAGUE_TIMING (C-25):
C-25 fires when a timing anchor is absent; FAIL_UNCALIBRATED_PRIORITY fires when a timing
anchor is present but no prefill-calibrated priority band governs scheduling precedence
within the engagement window. → **C-48**, depends on C-25.

From V-02: `FAIL_UNVERIFIED_AMENDMENT` — fires at Step 8 when the Change Made cell is
populated but the Verification cell is absent or contains no confirmed artifact reference
and no documented not-yet reason with owner and deadline. Mirrors the 3-cell structural
completeness of C-06 (Authority + Decision + Deadline) and C-07 (Gatekeeper + Blocking
Reason + Lead Time). Distinct from FAIL_OBSERVATION_ONLY (C-23): C-23 fires when no
eligible structural target is updated at all; FAIL_UNVERIFIED_AMENDMENT fires when a target
is identified and a change is documented but the change is unconfirmed — independently
satisfiable. → **C-49**, depends on C-23.

From V-03 structural observations: `FAIL_NO_COMPETITOR_ENTRY` — fires at Step 2b when an
inertia-tagged stakeholder is present (C-11 PASS) but no corresponding Step 0b competitor
entry exists. Step 0b, inserted before Phase 1, names each displaced workflow or tool as a
first-class competitor with Adoption Band (DOMINANT / ACTIVE / MARGINAL) and Switching Cost
Band (HIGH / MEDIUM / LOW), both prefill-calibrated. First criterion extending the obligation
chain backward to pre-Phase-1. Distinct from C-11 (FAIL_NO_INERTIA): C-11 fires when
displacement occurs and no inertia stakeholders are identified; FAIL_NO_COMPETITOR_ENTRY
fires when inertia stakeholders are present but the status-quo competitor inventory (Step 0b)
carries no entry for the displaced workflow or tool they represent. → **C-50**, depends on C-11.

Totals: 39 + 3 = 42 aspirational × 5 = 210 pts from aspirational layer; max 285 + 15 = **300 pts**. Golden threshold unchanged.

---

```markdown
## scout-stakeholders rubric — v19

**v19 written.** Three new criteria extracted from Round 18 excellence signals across
three structural axes (V-01 comms priority band calibration, V-02 amendment verification
protocol, V-03 status-quo competitor inventory):

| ID   | Name                                  | Source      | Dependency |
|------|---------------------------------------|-------------|------------|
| C-48 | Comms priority band calibration       | V-01        | C-25       |
| C-49 | Amendment verification protocol       | V-02        | C-23       |
| C-50 | Status-quo competitor inventory       | V-03        | C-11       |

**Updated totals:** 42 aspirational × 5 = 210 pts; **max 300 pts**.
Golden threshold (>= 80) unchanged.

**Under v19 (Round 18 re-scored):**
- V-01 → 285/285 under v18; under v19 carries C-48 (PASS), C-49/C-50 not satisfiable → 295/300
- V-02 → 285/285 under v18; under v19 carries C-49 (PASS), C-48/C-50 not satisfiable → 295/300
- V-03 → 285/285 under v18; under v19 carries C-50 (PASS), C-48/C-49 not satisfiable → 295/300
- V-04 → 285/285 under v18; under v19 carries C-48 + C-49 (PASS), C-50 not satisfiable → 300/300 — GOLDEN
- V-05 → 285/285 under v18; under v19 carries C-48 + C-49 + C-50 (PASS) → 300/300 — GOLDEN

**Distinction logic:**

**C-48 — Comms priority band calibration** (depth, 5 pts)
A comms priority band prefill step (Step 6e-priority) is inserted after the channel
binding prefill step (Step 6c) and before Step 6b finalization, defining exactly three
named scheduling-precedence bands — URGENT, STANDARD, DEFERRED — with explicit criteria
for each band. Step 6b gains a Priority Band column whose values must be drawn exclusively
from the Step 6e-priority prefill labels. Step 9 synthesis gains a Priority Band field
with inline step citation. FAIL_UNCALIBRATED_PRIORITY fires at Step 6b when any comms row
carries a Priority Band value not drawn from the Step 6e-priority prefill (e.g., numeric
urgency ranking, free-form language, or ad hoc tiers not established in the prefill).
FAIL_UNCALIBRATED_PRIORITY is distinct from FAIL_VAGUE_TIMING (C-25): FAIL_VAGUE_TIMING
fires when any comms row lacks a timing anchor entirely; FAIL_UNCALIBRATED_PRIORITY fires
when a timing anchor is present and specific (C-25 PASS) but no calibrated priority band
governs scheduling precedence when multiple rows share an engagement window. A variation
that satisfies C-25 with a fully anchored comms table while omitting the Step 6e-priority
prefill and Priority Band column = C-25 PASS, C-48 FAIL.

C-48 is the sixth instance of the calibration motif (named-level prefill + constrained
scoring or output column + named failure mode), extending coverage to the comms
resource-sequencing layer. Prior instances: C-38 (veto probability), C-41 (trajectory
velocity), C-44 (champion behavioral anchor), C-45 (conflict severity).

- Distinct from C-25: C-25 (FAIL_VAGUE_TIMING) requires a timing anchor per comms row;
  C-48 requires a preceding Step 6e-priority prefill defining three named bands and
  constrains all Priority Band column values to those labels — a scheduling-precedence
  calibration obligation orthogonal to anchor presence
- Distinct from C-39: C-39 requires Step 6c channel binding constraining the Channel
  column; C-48 requires Step 6e-priority band binding constraining the Priority Band
  column — two independent prefill obligations on the comms table, each independently
  satisfiable
- Distinct from C-47: C-47 requires the displacement-acknowledgment row to carry the
  T+0 baseline timing anchor (a sequence-ordering constraint); C-48 requires all comms
  rows to carry a Priority Band drawn from a named prefill (a scheduling-precedence
  calibration constraint) — orthogonal obligations, independently satisfiable
- Not satisfiable if C-25 is absent

**C-49 — Amendment verification protocol** (depth, 5 pts)
Step 8 is expanded from a single-row amendment log to a structured 3-column protocol —
Amendment Target, Change Made, Verification — one row per eligible target. The
Verification cell must contain either (a) a confirmed artifact reference with date
(e.g., "Phase 3 grid row updated — [date]") or (b) "not-yet" with a named owner and
deadline. FAIL_UNVERIFIED_AMENDMENT fires at Step 8 when any row has a populated Change
Made cell but the Verification cell is absent, blank, or carries "not-yet" without a
named owner and deadline. FAIL_UNVERIFIED_AMENDMENT is distinct from FAIL_OBSERVATION_ONLY
(C-23): FAIL_OBSERVATION_ONLY fires when no eligible structural target is updated at all
(Change Made cell absent); FAIL_UNVERIFIED_AMENDMENT fires when a target is identified and
a change is documented (Change Made populated, FAIL_OBSERVATION_ONLY not triggered) but
the change is unconfirmed. A variation that satisfies C-23 by documenting at least one
amendment while omitting the Verification column entirely = C-23 PASS, C-49 FAIL.

The mandatory ASSUMED amendment obligation (C-46) is preserved: ASSUMED-annotated Source
cells remain mandatory Amendment Target rows; each must also carry a populated Verification
cell, creating a forward traceability chain from grid construction (C-46) through amendment
application (C-23) through verification confirmation (C-49).

The 3-column protocol mirrors the structural completeness patterns of C-06 (Resolution
Authority + Decision Required + Deadline) and C-07 (Gatekeeper + Blocking Reason + Lead
Time): each obligation has a target, a fulfillment cell, and a confirmation cell.

- Distinct from C-23: C-23 (FAIL_OBSERVATION_ONLY) requires at least one eligible
  structural target to be updated; C-49 requires each updated target to carry a Verification
  cell with a confirmed artifact reference or a documented not-yet reason — a confirmation
  obligation orthogonal to whether the change was applied
- Distinct from C-46: C-46 requires ASSUMED Source cells to be designated as mandatory
  amendment targets at grid construction time; C-49 requires the subsequent Verification
  cell to confirm the amendment was applied, an execution-confirmation obligation orthogonal
  to target designation
- Not satisfiable if C-23 is absent

**C-50 — Status-quo competitor inventory** (depth, 5 pts)
A competitor inventory step (Step 0b) is inserted after the org context state machine
(Step 0) and before Phase 1. Step 0b names each displaced workflow or tool as a first-class
"competitor" and assigns two prefill-calibrated attributes per entry: an Adoption Band
(DOMINANT / ACTIVE / MARGINAL) and a Switching Cost Band (HIGH / MEDIUM / LOW), each
defined by an explicit criteria prefill. Step 2b gains a Step 0b Competitor reference
column linking each inertia stakeholder to the competitor inventory. Step 9 synthesis gains
a Competitor field citing the corresponding Step 0b entry. FAIL_NO_COMPETITOR_ENTRY fires
at Step 2b when an inertia-tagged stakeholder appears in the inertia mapping table but no
corresponding Step 0b entry names the workflow or tool that stakeholder represents.
FAIL_NO_COMPETITOR_ENTRY is distinct from FAIL_NO_INERTIA (C-11): FAIL_NO_INERTIA fires
when a feature displaces an existing workflow and no inertia stakeholders are identified at
all; FAIL_NO_COMPETITOR_ENTRY fires when inertia stakeholders are present (C-11 PASS) but
the status-quo system they represent has not been inventoried in Step 0b with calibrated
Adoption and Switching Cost Bands. A variation that satisfies C-11 with a populated Step 2b
inertia table while omitting Step 0b entirely = C-11 PASS, C-50 FAIL.

Step 0b is the first criterion insertion point before Phase 1 — earlier than any prior new
criterion (Step 0 inserts the state machine, but Step 0b operates after it). C-50 extends
the inertia obligation chain backward: competitor inventory (Step 0b) → inertia mapping
with competitor reference (Step 2b) → inertia-tagged grid rows (Phase 3) → displacement
comms rows (Step 6b) → displacement comms sequence audit (Step 6d-sequence) → synthesis
Competitor field (Step 9). C-50 is the first criterion with a dual prefill structure in a
single step (Adoption Band + Switching Cost Band).

- Distinct from C-11: C-11 (FAIL_NO_INERTIA) requires inertia stakeholders to be
  identified when displacement occurs; C-50 requires the displaced workflow or tool to be
  inventoried in a preceding Step 0b competitor table with calibrated Adoption and Switching
  Cost Bands — a pre-Phase-1 structural obligation orthogonal to inertia stakeholder
  identification
- Distinct from C-47: C-47 constrains the ordering of comms rows within an inertia
  stakeholder's sequence; C-50 operates at the pre-Phase-1 competitor inventory layer,
  requiring the status-quo system to be named and banded before any stakeholder analysis
  begins — orthogonal obligations, independently satisfiable
- Not satisfiable if C-11 is absent

---

### v18 to v19 changes summary

| Criterion | Name                                  | Type  | Dependency |
|-----------|---------------------------------------|-------|------------|
| C-48      | Comms priority band calibration       | depth | C-25       |
| C-49      | Amendment verification protocol       | depth | C-23       |
| C-50      | Status-quo competitor inventory       | depth | C-11       |

Aspirational count: 39 → 42. Max: 285 → 300. Golden threshold unchanged.

C-48 is the sixth instance of the calibration motif (named-level prefill + constrained
column + named failure mode), completing coverage of the comms resource-sequencing layer
after C-38 (veto), C-41 (trajectory), C-44 (champion), C-45 (conflict severity). C-49
introduces a 3-column verification protocol at Step 8, the first amendment-phase gate
governing execution confirmation rather than target designation or update count. C-50 is
the first criterion operating pre-Phase-1, extending the inertia obligation chain backward
to the competitor inventory layer before any stakeholder analysis begins.

---

### v17 to v18 changes (retained for history)

Three new criteria extracted from Round 17 excellence signals across three structural axes
(C-45 conflict severity band calibration, C-46 source typology annotation, C-47 comms
sequence ordering):

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
3b-prefill and all typology labels = C-10 PASS, C-46 FAIL.

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
