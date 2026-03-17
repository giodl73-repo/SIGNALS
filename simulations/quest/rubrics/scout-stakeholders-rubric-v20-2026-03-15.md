## scout-stakeholders rubric — v20

**v20 written.** Three new criteria extracted from Round 19 excellence signals across
three structural axes (V-01 source staleness band calibration, V-02 synthesis field
depth gate, V-03 competitor response track):

| ID   | Name                               | Source | Failure Mode                   | Dependency |
|------|------------------------------------|--------|--------------------------------|------------|
| C-51 | Source staleness band calibration  | V-01   | `FAIL_UNCALIBRATED_STALENESS`  | C-46       |
| C-52 | Synthesis field depth gate         | V-02   | `FAIL_SHALLOW_SYNTHESIS`       | C-42       |
| C-53 | Competitor response track          | V-03   | `FAIL_NO_RESPONSE_TRACK`       | C-50       |

**Updated totals:** 45 aspirational × 5 = 225 pts; **max 315 pts**.
Golden threshold (>= 80%) unchanged.

**Under v20 (Round 19 re-scored):**
- V-01 → 300/300 under v19; under v20 carries C-51 (PASS), C-52/C-53 not satisfiable → 305/315
- V-02 → 300/300 under v19; under v20 carries C-52 (PASS), C-51/C-53 not satisfiable → 305/315
- V-03 → 300/300 under v19; under v20 carries C-53 (PASS), C-51/C-52 not satisfiable → 305/315
- V-04 (V-01 + V-02) → 300/300 under v19; under v20 carries C-51 + C-52 (PASS), C-53 not satisfiable → 310/315
- V-05 (V-01 + V-02 + V-03) → 300/300 under v19; under v20 carries C-51 + C-52 + C-53 (PASS) → 315/315 — GOLDEN

**Distinction logic:**

**C-51 — Source staleness band calibration** (depth, 5 pts)
A source staleness band prefill step (Step 3c-staleness) is inserted between Step 3b-prefill
(source typology) and Phase 3 grid population, defining exactly three named staleness bands —
CURRENT (source confirmed or refreshed within the current sprint cycle, < 14 days), STALE
(confirmed 15–60 days ago with no refresh since prior sprint cycle), and EXPIRED (confirmed
> 60 days ago, or one-time observation with no follow-up) — with explicit criteria and
reliability implications for each band. The Phase 3 grid gains a Source Age column; every
row's Source Age cell must carry exactly one label from the Step 3c-staleness prefill.
EXPIRED-annotated Source Age entries become mandatory Step 8 amendment targets alongside
ASSUMED-annotated Source cells; each must carry a Verification cell that either confirms
reclassification (Source typology updated to OBSERVED or INFERRED with a refreshed artifact)
or documents unresolved status with a named owner and deadline.

FAIL_UNCALIBRATED_STALENESS fires at the Phase 3 grid when any row carries a Source Age
value not drawn from the Step 3c-staleness prefill (e.g., free-form date, numeric day count,
or ad hoc freshness label not established in the prefill), or when the Source Age column is
absent entirely.

FAIL_UNCALIBRATED_STALENESS is distinct from FAIL_UNANNOTATED_SOURCE (C-46):
FAIL_UNANNOTATED_SOURCE fires when the epistemic typology label is absent from a Source cell
— the Source cell is present and populated but carries no OBSERVED / INFERRED / ASSUMED label
from the Step 3b-prefill; FAIL_UNCALIBRATED_STALENESS fires when a valid typology label is
present and the Source cell satisfies C-46, but the Source Age column is absent or carries a
value not drawn from the Step 3c-staleness prefill — a temporal-reliability obligation
orthogonal to epistemic classification. A variation that satisfies C-46 with a fully
annotated Source column in `[TYPOLOGY: source description]` format while omitting
Step 3c-staleness and the Source Age column entirely = C-46 PASS, C-51 FAIL.

C-51 is the eighth instance of the calibration motif (named-level prefill + constrained
output column + named failure mode), extending coverage to the temporal-reliability layer
of the source evidence stack. Prior instances in order: C-38 (veto probability bands),
C-41 (trajectory velocity bands), C-44 (champion behavioral anchor levels), C-45 (conflict
severity bands), C-46 (source typology labels — epistemic basis), C-48 (comms priority
bands), C-50 (competitor Adoption Band + Switching Cost Band — the dual-prefill instance).
C-51 introduces the first temporal dimension to source evidence, the first staleness-layer
gate, and extends the EXPIRED entry as a mandatory amendment target alongside ASSUMED
entries — a joint mandatory amendment obligation from two independent source-quality axes
(epistemic basis from C-46 and temporal reliability from C-51).

- Distinct from C-46: C-46 requires each Source cell to carry an epistemic typology label
  (OBSERVED / INFERRED / ASSUMED) from the Step 3b-prefill; C-51 requires a separate
  Step 3c-staleness prefill and a Source Age column constrained to its labels — two
  independent source-quality obligations on the Phase 3 grid, each independently satisfiable
- Distinct from C-23: C-23 requires the amendment phase to include at least one eligible
  structural update target; C-51 designates EXPIRED Source Age entries as mandatory amendment
  targets alongside ASSUMED entries, an eligibility-classification obligation that precedes
  and feeds Step 8 rather than governing its minimum count
- Distinct from C-49: C-49 requires the Step 8 Verification cell to be populated for any
  row with a Change Made entry; C-51 designates which Source Age entries trigger mandatory
  amendment rows — orthogonal obligations, independently satisfiable
- Not satisfiable if C-46 is absent

**C-52 — Synthesis field depth gate** (depth, 5 pts)
A synthesis depth audit step (Step 9b) is inserted after the Step 9 cross-phase synthesis
readout. For each stakeholder row in the synthesis readout, Step 9b audits each of the
required fields (Grid Position, Engagement Window, Conflict Exposure, Champion Status,
Comms Frame Type, Priority Band, Competitor) for substantive content. A field is
functionally empty if it contains only "N/A", "—", "Not applicable", or a placeholder
equivalent with no documented reason. A permitted N/A justification must carry exactly one
of the following reason codes in the format `N/A: [reason-code]`: NO-CONFLICT,
NO-CHAMPION-ROLE, MONITOR-ONLY, NO-COMPETITOR-CONTEXT. Step 9b is a pipe-table audit with
one row per stakeholder and one pass/fail cell per field; a field is PASS if it carries
substantive content or an N/A with a permitted reason code, and FAIL if it carries
undocumented N/A, a dash, or a placeholder with no justification.

FAIL_SHALLOW_SYNTHESIS fires at Step 9b when any field cell in the audit table carries FAIL
status.

FAIL_SHALLOW_SYNTHESIS is distinct from FAIL_NO_SYNTHESIS (C-32): FAIL_NO_SYNTHESIS fires
when the Step 9 synthesis step is absent or a required field column is structurally missing
from the readout — the row or column does not exist; FAIL_SHALLOW_SYNTHESIS fires when all
required fields are structurally present (C-32 PASS) but one carries undocumented N/A or a
placeholder without a permitted reason code — a depth obligation orthogonal to field
presence. A variation that satisfies C-32 with a structurally complete synthesis readout
(all 7 fields per row present) while populating the Conflict Exposure field with "—" for
one stakeholder without any reason code = C-32 PASS, C-52 FAIL.

FAIL_SHALLOW_SYNTHESIS is distinct from FAIL_SYNTHESIS_GAP (C-42): FAIL_SYNTHESIS_GAP
fires when a stakeholder row is absent from the Step 9 synthesis readout entirely — the
stakeholder appeared in the Phase 3 grid but has no synthesis row and no Step 8b omission
justification; FAIL_SHALLOW_SYNTHESIS fires when a stakeholder row is present in synthesis
but a field within it is functionally empty — the stakeholder is represented, but the
representation is substantively incomplete. A variation that satisfies C-42 with every
Phase 3 grid stakeholder represented in synthesis while leaving one field with an
undocumented placeholder = C-42 PASS, C-52 FAIL.

The Step 9b audit mirrors the structural completeness pattern of Step 8b (C-42): C-42
requires a pre-synthesis coverage audit confirming that every Phase 3 stakeholder has a
designated synthesis row; C-52 requires a post-synthesis depth audit confirming that every
field in every synthesis row is substantive — two orthogonal completeness obligations at
adjacent structural positions (before and after Step 9).

- Distinct from C-32: C-32 requires the synthesis step to exist and all required fields to
  be structurally present per row; C-52 requires a subsequent Step 9b depth audit confirming
  each field carries substantive content or a documented N/A justification — a field-depth
  obligation orthogonal to structural presence
- Distinct from C-42: C-42 requires every Phase 3 grid stakeholder to appear in synthesis
  or be explicitly justified for omission at Step 8b; C-52 requires each field in a present
  stakeholder row to be substantive or explicitly justified — a within-row depth obligation
  orthogonal to row coverage
- Distinct from C-35: C-35 requires each synthesis field to carry an inline step citation
  (e.g., "(Phase 3)", "(Step 5a)"); C-52 requires each field to carry substantive content
  in addition to citation — a field can cite the correct step while carrying a placeholder
  value (C-35 PASS, C-52 FAIL)
- Not satisfiable if C-42 is absent

**C-53 — Competitor response track** (depth, 5 pts)
Step 0b (C-50) is extended from a dual-band to a triple-band structure. A Response Track
prefill is added to Step 0b, defining exactly three named response tracks — CONVERT (goal
is to move inertia stakeholders from current approach to new feature; success = adoption;
displacement-acknowledgment comms must include a named conversion path and milestone),
CONTAIN (goal is to limit growth of current approach while new feature matures; coexistence
is transitional; comms must include a containment boundary and review checkpoint), and
CO-EXIST (current approach and new feature serve different enough needs that permanent
coexistence is acceptable; comms must clarify boundary conditions and avoid implying
replacement) — with explicit engagement implications per track. Each competitor entry in
the Step 0b inventory table gains a Response Track column drawn exclusively from the
Response Track prefill.

The Response Track assignment propagates through three downstream steps:
1. Step 2b inertia stakeholder mapping gains a Response Track column citing the track from
   the corresponding Step 0b entry
2. Step 6b displacement-acknowledgment comms rows must align with the assigned track: CONVERT
   messages include a named conversion path and milestone; CONTAIN messages include a
   containment boundary and review checkpoint; CO-EXIST messages clarify boundary conditions
   without implying replacement
3. Step 9 synthesis Competitor field cites both the competitor name and the Response Track:
   e.g., `competitor: Legacy-Workflow [CONVERT] (Step 0b)`

FAIL_NO_RESPONSE_TRACK fires at Step 0b when any competitor entry lacks a Response Track
value drawn from the Response Track prefill (e.g., blank cell, free-form strategy
description, or an ad hoc label not established in the prefill).

FAIL_NO_RESPONSE_TRACK is distinct from FAIL_NO_COMPETITOR_ENTRY (C-50):
FAIL_NO_COMPETITOR_ENTRY fires when an inertia-tagged stakeholder appears in Step 2b but no
corresponding Step 0b entry names the workflow or tool they represent — the competitor entry
itself is absent; FAIL_NO_RESPONSE_TRACK fires when the competitor entry is present (C-50
PASS) but the strategic response track governing how that competitor is to be handled is
undeclared. A variation that satisfies C-50 with a fully populated competitor inventory
(Competitor, Description, Adoption Band, Switching Cost Band) while omitting the Response
Track column and prefill entirely = C-50 PASS, C-53 FAIL.

C-53 is the first criterion whose Step 0b attribute propagates through three downstream
steps (Step 2b → Step 6b → Step 9), extending the inertia obligation chain with a
strategy-intent layer beyond the market-position and switching-cost layers established by
C-50. C-53 is the first strategy-classification calibration gate at the competitor layer:
Adoption Band classifies market position, Switching Cost Band classifies switching friction,
and Response Track classifies strategic intent — three independent competitive dimensions,
each independently satisfiable. C-53 is also the first criterion to impose a content
alignment constraint on the Step 6b comms message (the CONVERT/CONTAIN/CO-EXIST framing
requirement), distinct from C-30 which imposes a framing sequence constraint.

- Distinct from C-50: C-50 requires each displaced workflow or tool to be inventoried in
  Step 0b with calibrated Adoption Band and Switching Cost Band; C-53 requires a third
  prefill-calibrated attribute — the strategic Response Track — an intent-classification
  obligation orthogonal to market-position and switching-cost classification
- Distinct from C-30: C-30 requires the displacement-acknowledgment comms message to address
  what the current approach preserves before describing the new approach (a framing-sequence
  obligation at the message level); C-53 requires the comms message content to align with
  the Response Track assigned in Step 0b (a strategic-alignment obligation) — independently
  satisfiable, since a message can correctly preserve the current approach first (C-30 PASS)
  while failing to include the CONVERT conversion path or CONTAIN containment boundary
  required by its assigned track (C-53 FAIL)
- Distinct from C-47: C-47 requires the displacement-acknowledgment row to carry the T+0
  baseline timing anchor (a sequence-ordering constraint); C-53 requires the message content
  to reflect the Response Track assignment (a strategic-alignment constraint) — orthogonal
  obligations on the same row, independently satisfiable
- Not satisfiable if C-50 is absent

---

### v19 to v20 changes summary

| Criterion | Name                               | Type  | Dependency |
|-----------|------------------------------------|-------|------------|
| C-51      | Source staleness band calibration  | depth | C-46       |
| C-52      | Synthesis field depth gate         | depth | C-42       |
| C-53      | Competitor response track          | depth | C-50       |

Aspirational count: 42 → 45. Max: 300 → 315. Golden threshold unchanged.

C-51 is the eighth instance of the calibration motif, extending coverage to the temporal-
reliability layer of the source evidence stack and introducing a joint EXPIRED + ASSUMED
mandatory amendment obligation. C-52 introduces the first post-synthesis depth audit gate,
closing the structural gap between field presence (C-32) and field depth — a row can
carry all 7 columns (C-32 PASS) while containing placeholder values (C-52 FAIL). C-53
is the first Step 0b attribute to carry strategic-intent classification and the first
three-step downstream propagation chain at the competitor layer (Step 0b → Step 2b →
Step 6b → Step 9).

---

### v18 to v19 changes (retained for history)

Three new criteria extracted from Round 18 excellence signals across three structural
axes (V-01 comms priority band calibration, V-02 amendment verification protocol,
V-03 status-quo competitor inventory):

| Criterion | Name                                  | Type  | Dependency |
|-----------|---------------------------------------|-------|------------|
| C-48      | Comms priority band calibration       | depth | C-25       |
| C-49      | Amendment verification protocol       | depth | C-23       |
| C-50      | Status-quo competitor inventory       | depth | C-11       |

Aspirational count: 39 → 42. Max: 285 → 300. Golden threshold unchanged.

C-48 is the sixth instance of the calibration motif, completing coverage of the comms
resource-sequencing layer after C-38 (veto), C-41 (trajectory), C-44 (champion), C-45
(conflict severity), C-46 (source typology). C-48 is distinct from C-39 (channel binding
— separate prefill obligation on the same table) and C-47 (sequence ordering — different
constraint class). C-49 is the first amendment-phase gate governing execution confirmation
(distinct from target designation, C-46, and update count, C-23); its 3-column protocol
(Amendment Target / Change Made / Verification) mirrors the structural completeness of
C-06 (Authority + Decision + Deadline) and C-07 (Gatekeeper + Blocking Reason + Lead
Time). C-50 is the first pre-Phase-1 criterion and the first with a dual-prefill structure
in a single step (Adoption Band + Switching Cost Band); it extends the inertia obligation
chain backward from inertia mapping (Step 2b) to competitor inventory (Step 0b).

**C-48 — Comms priority band calibration** (depth, 5 pts)
A comms priority band prefill step (Step 6e-priority) is inserted after the channel
binding prefill step (Step 6c) and before Step 6b finalization, defining exactly three
named scheduling-precedence bands — URGENT (window closes within current sprint; any
delay risks losing it), STANDARD (window extends past current sprint; preferred within
1–2 cycles), DEFERRED (no forcing function; timing fully opportunistic) — with scheduling
criteria and resource implications for each band. Step 6b gains a Priority Band column
whose values must be drawn exclusively from the Step 6e-priority prefill labels. Step 9
synthesis gains a Priority Band field with inline step citation. FAIL_UNCALIBRATED_PRIORITY
fires at Step 6b when any comms row carries a Priority Band value not drawn from the
Step 6e-priority prefill (e.g., numeric urgency ranking, free-form language, or ad hoc
tiers not established in the prefill). FAIL_UNCALIBRATED_PRIORITY is distinct from
FAIL_VAGUE_TIMING (C-25): FAIL_VAGUE_TIMING fires when any comms row lacks a timing
anchor entirely; FAIL_UNCALIBRATED_PRIORITY fires when a timing anchor is present and
specific (C-25 PASS) but no calibrated priority band governs scheduling precedence when
multiple rows share an engagement window. Not satisfiable if C-25 is absent.

**C-49 — Amendment verification protocol** (depth, 5 pts)
Step 8 is expanded from a single-row amendment log to a structured 3-column protocol —
Amendment Target, Change Made, Verification — one row per eligible target. The Verification
cell must contain either (a) a confirmed artifact reference with date (e.g., "Phase 3 grid
row updated — [date]") or (b) "not-yet: [named owner] by [deadline]". FAIL_UNVERIFIED_AMENDMENT
fires at Step 8 when any row has a populated Change Made cell but the Verification cell is
absent, blank, or carries "not-yet" without a named owner and deadline. Distinct from
FAIL_OBSERVATION_ONLY (C-23): C-23 fires when no eligible structural target is updated at
all; FAIL_UNVERIFIED_AMENDMENT fires when a target is identified and a change is documented
but the change is unconfirmed. The ASSUMED traceability chain spans three criteria: C-46
(designates ASSUMED Source cells as mandatory targets at grid construction) → C-23 (requires
at least one eligible target updated) → C-49 (requires each updated target to be confirmed).
Not satisfiable if C-23 is absent.

**C-50 — Status-quo competitor inventory** (depth, 5 pts)
A competitor inventory step (Step 0b) is inserted after the org context state machine
(Step 0) and before Phase 1. Step 0b names each displaced workflow or tool as a first-class
competitor and assigns two prefill-calibrated attributes per entry: Adoption Band (DOMINANT
> 70% / ACTIVE 30–70% / MARGINAL < 30%) and Switching Cost Band (HIGH requires migration /
MEDIUM requires adjustment / LOW self-service). Step 2b gains a Step 0b Competitor reference
column linking each inertia stakeholder to the competitor inventory. Step 9 synthesis gains
a Competitor field citing the Step 0b entry. FAIL_NO_COMPETITOR_ENTRY fires at Step 2b when
an inertia-tagged stakeholder's Step 0b Competitor cell is blank or references a name not
present in the Step 0b inventory. Distinct from FAIL_NO_INERTIA (C-11): C-11 fires when
displacement occurs and no inertia stakeholders are identified; FAIL_NO_COMPETITOR_ENTRY
fires when inertia stakeholders are present but the status-quo system they represent has
not been inventoried in Step 0b with calibrated Adoption and Switching Cost Bands. Not
satisfiable if C-11 is absent.

---

### v17 to v18 changes (retained for history)

Three new criteria extracted from Round 17 excellence signals:

| Criterion | Name                                  | Type  | Dependency |
|-----------|---------------------------------------|-------|------------|
| C-45      | Conflict severity band calibration    | depth | C-06       |
| C-46      | Source typology annotation            | depth | C-10       |
| C-47      | Comms displacement sequence ordering  | depth | C-29       |

Aspirational count: 36 → 39. Max: 270 → 285. Golden threshold unchanged.

C-45 is the fifth instance of the calibration motif; C-46 is the first amendment-eligibility
criterion classified by epistemic basis (ASSUMED entries become mandatory Step 8 targets);
C-47 is the first comms gate governing row order rather than presence, content, channel, or
anchor existence.

---

### v16 to v17 changes (retained for history)

Two new criteria extracted from Round 16 excellence signals:

| Criterion | Name                                   | Type  | Dependency |
|-----------|----------------------------------------|-------|------------|
| C-43      | Conflict party segment anchoring       | depth | C-06       |
| C-44      | Champion behavioral anchor calibration | depth | C-20       |

Aspirational count: 34 → 36. Max: 260 → 270. Golden threshold unchanged.

---

### v15 to v16 changes (retained for history)

Three new criteria extracted from Round 15 excellence signals:

| Criterion | Name                         | Type  | Dependency |
|-----------|------------------------------|-------|------------|
| C-40      | Conflict escalation tier     | depth | C-06       |
| C-41      | Trajectory velocity prefill  | depth | C-31       |
| C-42      | Synthesis coverage gate      | depth | C-32       |

Aspirational count: 31 → 34. Max: 245 → 260. Golden threshold unchanged.

---

### v14 to v15 changes (retained for history)

Three new criteria extracted from Round 14 excellence signals:

| Criterion | Name                                        | Type  | Dependency             |
|-----------|---------------------------------------------|-------|------------------------|
| C-37      | Org context state machine label integrity   | depth | C-01                   |
| C-38      | Veto probability calibration bands          | depth | C-22                   |
| C-39      | Comms channel binding                       | depth | C-13                   |

Aspirational count: 28 → 31. Max: 230 → 245. Golden threshold unchanged.

---

## Essential Criteria (60 pts total)

| ID   | Criterion                                | Category    | Pass Condition |
|------|------------------------------------------|-------------|----------------|
| C-01 | **Org context determination**            | correctness | Step 0 state machine emits exactly one of {ORG-RESOLVED-CODEOWNERS, ORG-RESOLVED-CONTEXT, ORG-BLOCKED} before any Phase 1 output. Analysis halts at ORG-BLOCKED and does not proceed until the question is resolved. FAIL_SILENT_INFERENCE: no state label emitted, or analysis proceeds without org resolution. |
| C-02 | **Phase role enforcement: UX → Strategy → PM** | correctness | Steps are explicitly ordered Phase 1 (UX) → Phase 2 (Strategy) → Phase 3 (PM). Phase 2 analysis does not begin before Phase 1 is complete; Phase 3 grid is not built before Phase 2 is complete. Each phase is structurally distinct and carries role labels in step headings. |
| C-03 | **Phase 1 NOT-doing statements**         | correctness | Every Phase 1 segment row carries a NOT-doing statement specific to that segment. Generic "out of scope" language is not a NOT-doing statement. Inertia-classified segments must address what the new approach does not preserve from the current approach. FAIL_NO_NOT_DOING: NOT-doing absent for any segment. |
| C-04 | **Phase 1 minimum segments**             | correctness | Phase 1 identifies at least two distinct user segments with primary use pattern, journey touchpoints affected, NOT-doing statement, and gatekeeper/inertia candidacy. FAIL_MONOLITH_ASSUMPTION: all users treated as a single undifferentiated segment. |
| C-05 | **Phase 1 → Phase 2 gate enforcement**   | correctness | A dedicated Phase 1 → Phase 2 transition gate step is present with an explicit checklist: at least two distinct segments analyzed; NOT-doing present for each segment; inertia displacement NOT-doing addressed if applicable. FAIL_INCOMPLETE_PHASE1: any required Phase 1 output absent; Phase 2 does not begin. |

**Essential points**: 12 pts each × 5 = **60 pts**

---

## Recommended Criteria (30 pts total)

| ID   | Criterion                                         | Category    | Pass Condition |
|------|---------------------------------------------------|-------------|----------------|
| C-06 | **Structural conflict 2-party + resolution pathway** | depth    | Phase 2 identifies at least two structural conflicts, each naming two parties in tension with the nature of the conflict stated. Per-conflict resolution pathway table provides Resolution Authority (named person or body), Decision Required (specific ruling needed), and Deadline (date or milestone). FAIL_ONE_PARTY: any conflict row names only one party. FAIL_NO_RESOLUTION_PATHWAY: any conflict row missing Authority, Decision, or Deadline. |
| C-07 | **Critical-path gatekeeper with lead-time tag**   | correctness | Step 2c identifies at least one critical-path gatekeeper with a blocking reason and minimum lead-time note tagged as "CRITICAL PATH — lead time: X". FAIL_NO_GATEKEEPER_TIMING: a critical-path gatekeeper is named without a lead time. |
| C-08 | **Phase 2 → Phase 3 gate enforcement**            | depth       | A dedicated Phase 2 → Phase 3 transition gate step is present with an explicit checklist: at least two structural conflicts with two anchored parties, complete resolution pathway, and escalation tier row; at least one inertia stakeholder or explicit no-displacement statement; at least one critical-path gatekeeper with lead-time tag. FAIL_INCOMPLETE_PHASE2: any required Phase 2 output absent; Phase 3 does not begin. |

**Recommended points**: 10 pts each × 3 = **30 pts**

---

## Aspirational Criteria (225 pts total)

### Tier 2 — Recommended depth (C-09 through C-25)

| ID   | Criterion                                         | Category | Pass Condition |
|------|---------------------------------------------------|----------|----------------|
| C-09 | **Format constraint: pipe tables**                | coverage | Every structural output — grids, tables, scoring tables, prefill tables, veto tables, synthesis readout, and communication tables — uses Markdown pipe-table format. Prose-only stakeholder lists or freeform layouts are not acceptable structural outputs. FAIL_NO_PARSEABLE_FORMAT: first structural step that produces output in non-parseable prose or freeform layout instead of a pipe table. |
| C-10 | **Source column present with entry per row**      | depth    | Phase 3 Power/Interest grid includes a Source column; every stakeholder row carries a source entry (e.g., CODEOWNERS extraction, invocation string, conflict discovery, prior interview). FAIL_NO_SOURCE: Source column absent or any row missing a source entry. |
| C-11 | **Inertia stakeholders identified**               | depth    | When the feature displaces an existing workflow or tool, Phase 2 Step 2b identifies at least one inertia stakeholder with current approach, displaced-by content, and coalition capacity noted. FAIL_NO_INERTIA: displacement occurs but no inertia stakeholders are identified. |
| C-12 | **PM role phase ownership**                       | coverage | All Phase 3 analytical steps (Steps 3a through 9) and the synthesis readout are explicitly attributed to the PM role; each Phase 3 step heading carries "— PM role" in its heading text. PM role does not appear in Phase 1 or Phase 2 step headings. The PM role is the designated owner of grid construction and the cross-phase synthesis. |
| C-13 | **Comms plan present with Frame Type column**     | coverage | Step 6b communication strategy table is present with at least one row per relevant quadrant and a Frame Type column. The Frame Type column is populated with named frame type labels. FAIL when the comms section is absent or lacks the Frame Type column. |
| C-14 | **Frame Type distinctness across rows**           | coverage | Each Step 6b comms row carries a distinct Frame Type; no two rows share the same Frame Type label. FAIL_SAME_FRAME: two or more rows share the same Frame Type. |
| C-15 | **Inertia NOT-doing preservation**                | depth    | The NOT-doing statement for inertia-classified segments in Phase 1 specifically addresses what the new approach does not preserve from the current approach — not merely what is out of scope. The inertia-segment NOT-doing framing is preserved consistently through Phase 2 Step 2b (displacement framing) and Phase 3 displacement-acknowledgment comms; Phase 2 or Phase 3 content must not contradict the Phase 1 NOT-doing commitment. |
| C-16 | **Phase 3 grid: quadrant labels**                 | correctness | Phase 3 Power/Interest grid assigns a quadrant label per row (e.g., Manage Closely, Keep Satisfied, Keep Informed, Monitor) based on Power and Interest values. FAIL_PROSE_ONLY: stakeholder list without grid structure. |
| C-17 | **Phase 3 grid: power/interest H/M/L**            | correctness | Phase 3 grid includes Power and Interest columns with explicit H/M/L values per row. Power and Interest values must be assigned per stakeholder, not inferred from prose or quadrant label alone. |
| C-18 | **Phase 3 grid: inertia tag in Notes**            | depth    | Every inertia-identified stakeholder (from Step 2b) carries an `[INERTIA]` tag in the Notes column of the Phase 3 Power/Interest grid. FAIL when any inertia stakeholder from Step 2b appears in the grid without the `[INERTIA]` Notes tag. |
| C-19 | **Engagement window derivation (Step 5a)**        | depth    | Step 5a is a dedicated sub-step synthesizing Power/Interest quadrant position and gatekeeper lead times into a derived engagement window per stakeholder or quadrant. Phase 3 grid carries an Engagement Window column updated with derived values. Step 6b timing anchors must fall within derived engagement windows, not merely be any relative anchor. FAIL_NO_ENGAGEMENT_WINDOW: engagement window not derived or not populated in grid. |
| C-20 | **Champion scoring dimensions (Authority / Proximity / Commitment)** | depth | Step 5c contains a champion scoring table with three named dimensions: Authority (organizational decision-making power), Proximity (access to blockers and sponsors), and Commitment (demonstrated investment in the feature's success). FAIL when any dimension is absent from the scoring table. |
| C-21 | **Champion durability (Step 5d)**                 | depth    | Step 5d is present and contains a succession path (who assumes the champion role if the current champion leaves) and at least one deterioration signal (an observable trigger indicating that champion commitment is eroding). FAIL_NO_DURABILITY: succession path absent AND no deterioration signals documented. |
| C-22 | **Veto ranking present with ordering**            | depth    | Step 4b veto risk table is present and ordered HIGH probability first, then MED, then LOW; within band, by judgment. Each entry includes probability band, impact, and a mitigation strategy column. FAIL_WRONG_ORDER: entries not sorted HIGH → MED → LOW. |
| C-23 | **Amendment: at least one eligible target updated** | depth  | Step 8 amendment section documents at least one update to an eligible structural target (Phase 3 grid row, Step 4b veto entry, Step 6a frame type assignment, Step 6b comms row, Step 6e-priority priority band assignment, Step 2c gatekeeper lead-time tag, Step 2a conflict resolution pathway entry, Step 2a escalation tier entry, trajectory assessment, velocity assessment, engagement window derivation, champion depth scores, synthesis readout row, source age assessment). The Change Made cell must be populated. FAIL_OBSERVATION_ONLY: finding documented without updating any eligible structural target. |
| C-24 | **Gatekeeper completeness check (Step 7)**        | depth    | Step 7 is present with a per-gatekeeper row confirming: comms row present (yes/no), blocking reason documented (yes/no), and lead time honored (yes/no). FAIL_GATEKEEPER_INCOMPLETE: any gatekeeper missing a comms row, blocking reason documentation, or lead time honored confirmation. |
| C-25 | **Timing anchor per comms row**                   | coverage | Every Step 6b comms row carries a relative timing anchor (e.g., "T+0", "3 weeks before decision", "day of launch", "within 2 sprints"). FAIL_VAGUE_TIMING: any comms row lacks a timing anchor. |

**Tier 2 points**: 5 pts each × 17 = **85 pts**

---

### Tier 3 — Advanced depth (C-26 through C-53)

| ID   | Criterion                                                        | Category | Pass Condition |
|------|------------------------------------------------------------------|----------|----------------|
| C-26 | **Inertia `displacement-acknowledgment` mandatory assignment**   | depth    | Step 6a Frame Type prefill explicitly lists `displacement-acknowledgment` as a mandatory Frame Type for inertia-tagged stakeholders. Step 6b assigns `displacement-acknowledgment` to every inertia stakeholder's comms row. Step 6a Rule 3 states that `displacement-acknowledgment` messages must address what the current approach preserves before describing the new approach. FAIL_MISSING_DISPLACEMENT_PREFILL: inertia rows exist but `displacement-acknowledgment` not assigned in Step 6a. |
| C-27 | **Champion composite gate >= 6**                                 | depth    | Step 5c includes a composite score row summing the three dimension scores; the composite threshold gate is set at >= 6 (max 9 on the 0–3 scale). An inline failure label fires if the composite falls below threshold. FAIL_BELOW_CHAMPION_THRESHOLD: composite < 6 with no alternative champion identified and no risk documented. |
| C-28 | **CODEOWNERS fallback with invocation inference**                | depth    | Step 0 state machine includes all three branches: (1) CODEOWNERS file present at repository root — extract teams named as owners; (2) CODEOWNERS absent but invocation string contains team or org identifiers — extract org context from invocation string; (3) neither source sufficient — ask exactly one clarifying question ("What org or team is this decision for?") and halt all analysis. All three branches are named and labeled with terminal state identifiers. |
| C-29 | **Displacement-acknowledgment timing anchor**                    | depth    | The displacement-acknowledgment row in Step 6b carries a relative timing anchor. FAIL_DISPLACEMENT_TIMING: displacement-acknowledgment row lacks a timing anchor (distinct from FAIL_VAGUE_TIMING which fires on any comms row). Not satisfiable if C-26 is absent. |
| C-30 | **Phase 3 `displacement-acknowledgment` message framing (preserves current first)** | depth | Step 6a Rule 3 is explicitly present: `displacement-acknowledgment` messages must address what the current approach preserves before describing the new approach. Step 6b displacement-acknowledgment Message cells must demonstrate this framing — the preservation acknowledgment comes first, the transition description second. FAIL when inertia comms rows describe the new approach without first acknowledging what is preserved. |
| C-31 | **Trajectory column with directional label + signal**            | depth    | Phase 3 grid includes a Trajectory column; each row carries a directional label (ascending-toward-advocate / stable / descending-toward-risk) with an observable signal (behavioral or event-based evidence for the direction). FAIL_NO_TRAJECTORY: Trajectory column absent or any row missing directional assessment. |
| C-32 | **Synthesis step with required fields per row**                  | depth    | Step 9 cross-phase synthesis readout is present with one row per stakeholder; each row carries all required fields with inline step citation: Grid Position (Phase 3), Engagement Window (Step 5a), Conflict Exposure (Step 2a), Champion Status (Step 5c), Comms Frame Type (Step 6a), Priority Band (Step 6e-priority), Competitor (Step 0b). FAIL_NO_SYNTHESIS: synthesis step absent. FAIL_NO_ATTRIBUTION: any field lacking inline step citation. |
| C-33 | **Veto mitigation per entry**                                    | depth    | Each Step 4b veto risk entry includes a Mitigation column with a response or mitigation strategy. Probability and impact without a mitigation field = FAIL. FAIL_NO_MITIGATION: any entry lacks a mitigation strategy. |
| C-34 | **Veto ordering HIGH → MED → LOW**                               | depth    | Step 4b veto risk table entries are ordered HIGH probability band first, then MED, then LOW; within each band by judgment. FAIL_WRONG_ORDER: entries not ordered HIGH → MED → LOW by band. |
| C-35 | **Synthesis inline step citation per field**                     | depth    | Each field in the Step 9 synthesis readout carries an inline step citation identifying the step that produced that value (e.g., "grid position: Manage Closely (Phase 3)", "engagement window: sprint+2 (Step 5a)"). FAIL_NO_ATTRIBUTION: any field lacks inline step citation. Distinct from C-32 (field presence): C-32 requires fields to exist; C-35 requires each field to cite its source step. |
| C-36 | **Champion schedulable action**                                  | depth    | Step 5b champion identification table includes a Schedulable Action column; the named action is calendar-ready and specific (e.g., "give demo slot at sprint review", "co-present at design review", "provide early access in Week 3"). Generic "engage champion" or "build relationship" language = FAIL. FAIL_GENERIC_CHAMPION: champion named without a schedulable action. |
| C-37 | **Org state label integrity (FAIL_WRONG_STATE)**                 | depth    | The state label emitted by Step 0 must causally correspond to the branch actually traversed: CODEOWNERS file was used → ORG-RESOLVED-CODEOWNERS; invocation string was used → ORG-RESOLVED-CONTEXT; neither source was sufficient → ORG-BLOCKED. FAIL_WRONG_STATE: the emitted label does not match the branch taken — a label that is present but identifies the wrong branch fires FAIL_WRONG_STATE, not FAIL_SILENT_INFERENCE. Not satisfiable if C-01 is absent. |
| C-38 | **Veto probability calibration bands (Step 4a)**                 | depth    | A prefill step (Step 4a) defines exactly three named probability bands — HIGH (> 70%), MED (30–70%), LOW (< 30%) — with explicit distinguishing criteria and when-to-use guidance before veto ranking begins. Step 4b draws probability values exclusively from these three band labels. FAIL_UNCALIBRATED_PROBABILITY: any Step 4b entry uses a probability value not drawn from the Step 4a prefill (e.g., raw numeric estimate, free-form language, or tiers not defined in the prefill). Not satisfiable if C-22 is absent. |
| C-39 | **Comms channel binding (Step 6c)**                              | depth    | A channel binding prefill step (Step 6c) is inserted between the Frame Type prefill (Step 6a) and the comms plan population (Step 6b), defining the permissible Primary Channel and Fallback Channel per Frame Type before the comms plan is populated. Step 6b Channel column draws values exclusively from the Step 6c binding; fallback may be used only when primary is explicitly unavailable. FAIL_NO_CHANNEL: Channel column absent from the comms table. FAIL_WRONG_CHANNEL: any row uses a channel not listed as Primary or Fallback for its Frame Type. Not satisfiable if C-13 is absent. |
| C-40 | **Conflict escalation tier table**                               | depth    | Step 2a includes a parallel escalation tier table — columns: Escalation Owner (named person or body above Resolution Authority), Escalation Trigger (condition activating escalation), Escalation Action (action taken by Escalation Owner) — one row per conflict. FAIL_NO_ESCALATION_PATH: any conflict row lacks a corresponding escalation tier row with a named Escalation Owner and defined Escalation Trigger. Distinct from C-06 (resolution pathway): C-06 requires Resolution Authority, Decision Required, and Deadline; C-40 requires the separate escalation structure for when the deadline is missed. Not satisfiable if C-06 is absent. |
| C-41 | **Trajectory velocity band prefill (Step 3a)**                   | depth    | A velocity band prefill step (Step 3a) is inserted before Phase 3 grid population, defining exactly three named velocity bands — ACCELERATING (trajectory changing faster than baseline; new signals in last review cycle), STABLE (no directional change since last review; consistent with prior cycle), DECELERATING (engagement thinning; fewer signals than prior cycle) — with explicit observable indicators per band. Phase 3 grid gains a Velocity column; all Velocity cell values must be drawn exclusively from the Step 3a prefill labels. FAIL_UNCALIBRATED_VELOCITY: any Phase 3 grid row omits the Velocity label or uses a designation not established in the Step 3a prefill. Not satisfiable if C-31 is absent. |
| C-42 | **Synthesis coverage gate (Step 8b)**                            | depth    | Step 8b is a dedicated coverage audit step inserted between the amendment phase (Step 8) and the synthesis step (Step 9), containing a pipe-table audit with one row per Phase 3 grid stakeholder recording whether each appears in the Step 9 synthesis readout or carries a documented omission justification. FAIL_SYNTHESIS_GAP: any Phase 3 grid stakeholder is absent from the Step 9 synthesis readout without a documented justification in Step 8b. Distinct from C-32 (synthesis field completeness): C-32 fires when the synthesis step is absent or fields are structurally missing; FAIL_SYNTHESIS_GAP fires when the step is present and fields are complete but a grid stakeholder is silently dropped. Not satisfiable if C-32 is absent. |
| C-43 | **Conflict party segment anchoring**                             | depth    | Each Party A and Party B cell in the Step 2a resolution pathway table must either (a) match a Phase 1 segment name verbatim, or (b) carry an `[ORG-ROLE: description]` tag identifying an org role not captured as a user segment. FAIL_UNANCHORED_CONFLICT_PARTY: any party name in a conflict row neither matches a Phase 1 segment nor carries an `[ORG-ROLE: description]` tag. Distinct from C-06 (party count): C-06 fires when a conflict has fewer than two parties; FAIL_UNANCHORED_CONFLICT_PARTY fires when both parties are present but at least one is not empirically anchored. Not satisfiable if C-06 is absent. |
| C-44 | **Champion behavioral anchor calibration (Step 5b-anchor)**      | depth    | A behavioral anchor prefill step (Step 5b-anchor) is inserted before Step 5c, defining four observable behavioral levels (0–3) per champion scoring dimension (Authority, Proximity, Commitment). Step 5c must draw all dimension scores exclusively from the 0–3 scale; each score's Evidence cell must cite the level number from the Step 5b-anchor prefill that justifies the score. FAIL_UNANCHORED_SCORE: any dimension score falls outside 0–3, or the Evidence cell does not cite a level from the Step 5b-anchor prefill. Distinct from C-20 (dimension presence): C-20 requires the three dimensions to exist; C-44 requires each score to be anchored to a prefill-defined behavioral level. Not satisfiable if C-20 is absent. |
| C-45 | **Conflict severity band calibration (Step 2a-prefill)**         | depth    | A severity band prefill step (Step 2a-prefill) is inserted before the Step 2a conflict identification table, defining exactly three named severity bands — CRITICAL (blocks decision entirely; no workaround), SIGNIFICANT (delays or degrades quality; workaround carries cost), MANAGEABLE (resolves within normal process; timeline impact unlikely) — with escalation implications. Step 2a conflict rows carry a Severity Band column whose values must be drawn exclusively from the Step 2a-prefill labels. FAIL_UNCALIBRATED_SEVERITY: any conflict row carries a Severity Band value not drawn from the Step 2a-prefill. Not satisfiable if C-06 is absent. |
| C-46 | **Source typology annotation (OBSERVED / INFERRED / ASSUMED)**   | depth    | A source typology prefill step (Step 3b-prefill) is inserted before Phase 3 grid population, defining exactly three epistemic typology labels — OBSERVED (directly witnessed; citable artifact exists), INFERRED (reasoned from pattern or adjacent signal; not directly witnessed), ASSUMED (no direct or adjacent evidence; based on role stereotype or default expectation) — with amendment obligations per label. Each Source cell in the Phase 3 grid must carry exactly one typology label in the format `[TYPOLOGY: source description]`. ASSUMED-annotated Source cells are mandatory Step 8 amendment targets. FAIL_UNANNOTATED_SOURCE: any Phase 3 grid Source cell is present and populated but does not carry a typology label from the Step 3b-prefill. Not satisfiable if C-10 is absent. |
| C-47 | **Comms displacement sequence ordering (Step 6d-sequence)**      | depth    | A sequence audit step (Step 6d-sequence) is inserted after Step 6b. For each inertia-tagged stakeholder, the audit confirms that the displacement-acknowledgment comms row carries the T+0 baseline timing anchor — the earliest anchor in that stakeholder's full comms sequence. FAIL_COMMS_SEQUENCE_VIOLATION: any inertia stakeholder's displacement-acknowledgment row does not carry the T+0 baseline (i.e., another comms row for that stakeholder carries an earlier or equal timing anchor). Distinct from FAIL_VAGUE_TIMING (C-25, anchor absent) and FAIL_DISPLACEMENT_TIMING (C-29, displacement row lacks any anchor): both anchors must be present and specific before FAIL_COMMS_SEQUENCE_VIOLATION is assessable. Not satisfiable if C-29 is absent. |
| C-48 | **Comms priority band calibration (Step 6e-priority)**           | depth    | A comms priority band prefill step (Step 6e-priority) is inserted after Step 6c and before Step 6b finalization, defining exactly three named scheduling-precedence bands — URGENT, STANDARD, DEFERRED — with scheduling criteria and resource implications per band. Step 6b gains a Priority Band column; all Priority Band cell values must be drawn exclusively from the Step 6e-priority prefill labels. FAIL_UNCALIBRATED_PRIORITY: any Step 6b comms row carries a Priority Band value not drawn from the prefill (e.g., numeric ranking, free-form urgency language, or ad hoc tier). Distinct from FAIL_VAGUE_TIMING (C-25, timing anchor absent) and FAIL_NO_CHANNEL (C-39, channel absent): all three are independent prefill obligations on the comms table. Not satisfiable if C-25 is absent. |
| C-49 | **Amendment verification protocol (3-column Step 8)**            | depth    | Step 8 uses a 3-column amendment protocol — Amendment Target, Change Made, Verification. The Verification cell must carry either (a) a confirmed artifact reference with date, or (b) "not-yet: [named owner] by [deadline]". FAIL_UNVERIFIED_AMENDMENT: any row has a populated Change Made cell but the Verification cell is absent, blank, or carries "not-yet" without a named owner and deadline. Distinct from FAIL_OBSERVATION_ONLY (C-23): C-23 fires when no update is applied at all; FAIL_UNVERIFIED_AMENDMENT fires when an update is documented but not confirmed. ASSUMED-annotated Source cells carry the Verification obligation through the forward traceability chain: C-46 (designates ASSUMED targets) → C-23 (requires update) → C-49 (requires confirmation). Not satisfiable if C-23 is absent. |
| C-50 | **Status-quo competitor inventory (Step 0b)**                    | depth    | A competitor inventory step (Step 0b) is inserted after Step 0 and before Phase 1. Step 0b names each displaced workflow or tool as a first-class competitor and assigns two prefill-calibrated attributes per entry: Adoption Band (DOMINANT / ACTIVE / MARGINAL) and Switching Cost Band (HIGH / MEDIUM / LOW), each with explicit criteria. Step 2b gains a Step 0b Competitor reference column; Step 9 synthesis gains a Competitor field. FAIL_NO_COMPETITOR_ENTRY: any inertia-tagged stakeholder in Step 2b has a blank or unmatched Step 0b Competitor cell. Distinct from FAIL_NO_INERTIA (C-11): C-11 fires when inertia stakeholders are absent; FAIL_NO_COMPETITOR_ENTRY fires when they are present but the status-quo system they represent is not inventoried with calibrated Adoption and Switching Cost Bands. Not satisfiable if C-11 is absent. |
| C-51 | **Source staleness band calibration (Step 3c-staleness)**        | depth    | A source staleness band prefill step (Step 3c-staleness) is inserted between Step 3b-prefill and Phase 3 grid population, defining exactly three named staleness bands — CURRENT (< 14 days), STALE (15–60 days), EXPIRED (> 60 days or one-time observation with no follow-up) — with reliability implications per band. Phase 3 grid gains a Source Age column; every row's Source Age cell must carry exactly one label from the Step 3c-staleness prefill. EXPIRED entries become mandatory Step 8 amendment targets alongside ASSUMED entries. FAIL_UNCALIBRATED_STALENESS: any Phase 3 grid row carries a Source Age value not drawn from the Step 3c-staleness prefill, or the Source Age column is absent entirely. Distinct from FAIL_UNANNOTATED_SOURCE (C-46): C-46 fires on absent typology label; FAIL_UNCALIBRATED_STALENESS fires when typology is present (C-46 PASS) but the temporal-reliability dimension is uncalibrated. Not satisfiable if C-46 is absent. |
| C-52 | **Synthesis field depth gate (Step 9b)**                         | depth    | A synthesis depth audit step (Step 9b) is inserted after Step 9. Step 9b audits each required field per stakeholder row for substantive content. A field is functionally empty if it contains only "N/A", "—", "Not applicable", or a placeholder with no documented reason. Permitted N/A justification format: `N/A: [reason-code]` where reason-code is one of: NO-CONFLICT, NO-CHAMPION-ROLE, MONITOR-ONLY, NO-COMPETITOR-CONTEXT. Step 9b is a pipe-table audit with one column per field and PASS/FAIL per cell. FAIL_SHALLOW_SYNTHESIS: any field cell in the audit carries FAIL status. Distinct from FAIL_NO_SYNTHESIS (C-32, field structurally absent) and FAIL_SYNTHESIS_GAP (C-42, stakeholder row absent): both C-32 and C-42 must PASS before FAIL_SHALLOW_SYNTHESIS is assessable. Not satisfiable if C-42 is absent. |
| C-53 | **Competitor response track (Step 0b)**                          | depth    | Step 0b (C-50) is extended from dual-band to triple-band structure. A Response Track prefill is added to Step 0b, defining exactly three named response tracks — CONVERT (goal: adoption; comms must include conversion path and milestone), CONTAIN (goal: limit current-approach growth; comms must include containment boundary and review checkpoint), CO-EXIST (permanent coexistence acceptable; comms must clarify boundary conditions without implying replacement) — with engagement implications per track. Each Step 0b competitor entry gains a Response Track column drawn exclusively from the prefill. Response Track propagates to: Step 2b (Response Track column citing the Step 0b assignment), Step 6b (displacement-acknowledgment message content aligned with assigned track), and Step 9 synthesis Competitor field (cites competitor name + track, e.g., `competitor: Legacy-Workflow [CONVERT] (Step 0b)`). FAIL_NO_RESPONSE_TRACK: any Step 0b competitor entry lacks a Response Track value drawn from the prefill. Distinct from FAIL_NO_COMPETITOR_ENTRY (C-50, competitor entry absent): FAIL_NO_RESPONSE_TRACK fires when the entry is present but the strategic intent dimension is undeclared. Not satisfiable if C-50 is absent. |

**Tier 3 points**: 5 pts each × 28 = **140 pts**

**Total aspirational**: 45 × 5 = **225 pts**

---

## Scoring Reference

| Band   | Range  | Meaning |
|--------|--------|---------|
| Golden | >= 80% | Output suitable as a golden example |
| Pass   | 60–79% | Acceptable; essential criteria met |
| Fail   | < 60%  | Missing one or more essential criteria |

**Max score v20**: 315 pts (60 essential + 30 recommended + 225 aspirational)

**v20 absolute thresholds**:
- Golden: >= 252 pts (>= 80% × 315)
- Pass: 189–251 pts (60–79%)
- Fail: < 189 pts (< 60%)

---

## Version History

| Version | Max   | Aspirational | Changes |
|---------|-------|--------------|---------|
| v14     | 230   | 140          | +C-37 (org state label), +C-38 (veto probability bands), +C-39 (comms channel binding) |
| v15     | 245   | 155          | +C-40 (conflict escalation tier), +C-41 (trajectory velocity prefill), +C-42 (synthesis coverage gate) |
| v16     | 260   | 170          | +C-40 (conflict escalation tier), +C-41 (velocity prefill), +C-42 (synthesis coverage) |
| v17     | 270   | 180          | +C-43 (conflict party anchoring), +C-44 (champion behavioral anchor) |
| v18     | 285   | 195          | +C-45 (conflict severity bands), +C-46 (source typology), +C-47 (comms sequence ordering) |
| v19     | 300   | 210          | +C-48 (comms priority bands), +C-49 (amendment verification), +C-50 (competitor inventory) |
| v20     | **315** | **225**    | +C-51 (source staleness bands), +C-52 (synthesis depth gate), +C-53 (competitor response track) |
