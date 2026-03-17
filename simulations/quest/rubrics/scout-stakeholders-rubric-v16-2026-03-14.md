## scout-stakeholders rubric — v16

**v16 written.** Three new criteria extracted from Round 15 excellence signals across three structural axes (V-01 conflict escalation tier, V-02 trajectory velocity prefill, V-03 synthesis coverage gate):

| ID | Name | Source | Dependency |
|----|------|--------|------------|
| C-40 | Conflict escalation tier | V-01 axis | C-06 |
| C-41 | Trajectory velocity prefill | V-02 axis | C-31 |
| C-42 | Synthesis coverage gate | V-03 axis | C-32 |

**Updated totals:** 34 aspirational × 5 = 170 pts; **max 260 pts**. Golden threshold (>= 80) unchanged.

**Under v16 (Round 15 re-scored):**
- V-01 → 250/260 (C-40 PASS; C-41 not satisfiable — no velocity prefill; C-42 not satisfiable — no coverage gate)
- V-02 → 250/260 (C-41 PASS; C-40 not satisfiable — no escalation tier; C-42 not satisfiable — no coverage gate)
- V-03 → 250/260 (C-42 PASS; C-40 not satisfiable — no escalation tier; C-41 not satisfiable — no velocity prefill)
- V-04 → 255/260 (C-40 PASS, C-41 PASS; C-42 not satisfiable — no coverage gate)
- V-05 → 260/260 (C-40 PASS, C-41 PASS, C-42 PASS — first perfect score under v16)

**Distinction logic:**

**C-40 — Conflict escalation tier** (depth, 5 pts)
Step 1a is extended with an escalation tier table — columns: Escalation Owner, Escalation Trigger, Escalation Action — one row per conflict, structurally parallel to the resolution pathway table required by C-06. FAIL_NO_ESCALATION_PATH fires when any conflict row in Step 1a lacks a corresponding escalation tier row with a named Escalation Owner and a defined Escalation Trigger. FAIL_NO_ESCALATION_PATH is distinct from FAIL_NO_RESOLUTION_PATHWAY: FAIL_NO_RESOLUTION_PATHWAY fires when the resolution pathway table is absent or structurally incomplete; FAIL_NO_ESCALATION_PATH fires when the resolution pathway is fully satisfied (Resolution Authority, Decision Required, and Deadline all present, C-06 PASS) but no escalation owner is defined for the scenario in which that deadline is missed. A variation that satisfies C-06 with a complete resolution pathway table while omitting any escalation tier rows = C-06 PASS, C-40 FAIL.

- Distinct from C-06: C-06 requires each structural conflict to name two parties and define a resolution pathway with authority, decision, and deadline; C-40 requires a separate parallel escalation tier table per conflict defining the escalation owner and trigger, an obligation orthogonal to resolution pathway completeness
- Not satisfiable if C-06 is absent

**C-41 — Trajectory velocity prefill** (depth, 5 pts)
A velocity prefill step (Step 3a) is inserted before the Phase 3 grid, defining exactly three named velocity bands — ACCELERATING, STABLE, DECELERATING — with explicit observable indicators for each band. The Phase 3 grid gains a Velocity column whose values must be drawn exclusively from the Step 3a prefill labels. FAIL_UNCALIBRATED_VELOCITY fires at the Phase 3 grid if any row omits the Velocity label or uses a velocity designation not established in the Step 3a prefill (e.g., free-form language, numeric rate, or an ad hoc label not defined in the prefill). FAIL_UNCALIBRATED_VELOCITY is distinct from FAIL_NO_TRAJECTORY: FAIL_NO_TRAJECTORY fires when the Trajectory column is absent or lacks directional label and observable signal; FAIL_UNCALIBRATED_VELOCITY fires when trajectory direction is present but the Velocity column is absent or unconstrained. Both obligations can be satisfied independently; a Phase 3 grid row can carry a fully formed Trajectory entry (direction + observable signal, FAIL_NO_TRAJECTORY not fired) while simultaneously failing FAIL_UNCALIBRATED_VELOCITY if no Velocity column or Step 3a prefill exists. A variation that satisfies C-31 with a complete Trajectory column while omitting the Velocity column and Step 3a prefill = C-31 PASS, C-41 FAIL.

- Distinct from C-31: C-31 requires a Trajectory column in the Phase 3 grid with directional label and observable signal per row; C-41 requires a separate Step 3a velocity band prefill and a Velocity column constrained to its labels, a second-order trajectory-dimension obligation that C-31 does not cover
- Not satisfiable if C-31 is absent

**C-42 — Synthesis coverage gate** (depth, 5 pts)
A coverage audit step (Step 8b) is inserted between the amendment phase (Step 8) and the synthesis step (Step 9). Step 8b contains a pipe-table audit with one row per Phase 3 grid stakeholder, recording whether each stakeholder appears in the Step 9 synthesis readout or carries a documented omission justification. FAIL_SYNTHESIS_GAP fires at Step 8b when any Phase 3 grid stakeholder is absent from the Step 9 synthesis readout and no omission justification is recorded in the Step 8b audit table. FAIL_SYNTHESIS_GAP is distinct from FAIL_NO_SYNTHESIS: FAIL_NO_SYNTHESIS fires when the synthesis step is absent entirely or lacks required structural fields; FAIL_SYNTHESIS_GAP fires when Step 9 exists and satisfies C-32 field obligations (all five fields present per row, FAIL_NO_SYNTHESIS not triggered) but grid stakeholders are silently dropped without justification. A variation that satisfies C-32 with a structurally complete synthesis readout while omitting one or more Phase 3 grid stakeholders without documentation = C-32 PASS, C-42 FAIL.

- Distinct from C-32: C-32 requires the synthesis step to exist with five required fields and one row per included stakeholder; C-42 requires a pre-synthesis coverage audit table at Step 8b verifying that every Phase 3 grid stakeholder is either represented in synthesis or explicitly justified for omission, an obligation orthogonal to per-row field completeness
- Not satisfiable if C-32 is absent

---

### v15 to v16 changes summary

| Criterion | Name | Type | Dependency |
|-----------|------|------|------------|
| C-40 | Conflict escalation tier | depth | C-06 |
| C-41 | Trajectory velocity prefill | depth | C-31 |
| C-42 | Synthesis coverage gate | depth | C-32 |

Aspirational count: 31 → 34. Max: 245 → 260. Golden threshold unchanged.

---

### v14 to v15 changes (retained for history)

Three new criteria extracted from Round 14 excellence signals across three structural axes (V-01 org context state machine, V-02 veto probability calibration, V-03 comms channel binding):

| Criterion | Name | Type | Dependency |
|-----------|------|------|------------|
| C-37 | Org context state machine label integrity | depth | C-01 |
| C-38 | Veto probability calibration bands | depth | veto ordering criterion |
| C-39 | Comms channel binding | depth | C-13 |

Aspirational count: 28 → 31. Max: 230 → 245. Golden threshold unchanged.

**C-37 — Org context state machine label integrity** (depth, 5 pts)
The org context decision (Step 0) emits a machine-readable state label identifying which branch was traversed (e.g., CODEOWNERS_PARSED, INVOCATION_USED, ORG_BLOCKED). FAIL_WRONG_STATE fires when the emitted label does not match the branch actually taken — the label must be causally accurate, not merely present. FAIL_WRONG_STATE is distinct from FAIL_SILENT_INFERENCE: FAIL_SILENT_INFERENCE fires when no label is emitted at all; FAIL_WRONG_STATE fires when a label is present but misidentifies the traversed branch. A variation that satisfies C-01 by emitting any label upon org context determination, without enforcing label-branch correspondence, = C-01 PASS, C-37 FAIL.

- Distinct from C-01: C-01 requires an org context determination to be made and documented; C-37 requires the emitted state label to be causally correct — matching the actual branch traversed, not merely present
- Not satisfiable if C-01 is absent

**C-38 — Veto probability calibration bands** (depth, 5 pts)
A prefill step (Step 4a) defines exactly three named probability bands — HIGH, MED, LOW — with explicit distinguishing criteria for each band before veto ranking begins. Step 4b must draw probability values exclusively from these three band labels. FAIL_UNCALIBRATED_PROBABILITY fires at Step 4b if any row carries a probability value not drawn from the Step 4a prefill (e.g., raw numeric estimates, free-form language, or tiers not defined in the prefill). FAIL_UNCALIBRATED_PROBABILITY is distinct from FAIL_WRONG_ORDER: FAIL_WRONG_ORDER fires when rows are not sorted by rank; FAIL_UNCALIBRATED_PROBABILITY fires when the probability values themselves are not drawn from a named-band prefill regardless of their order. A variation that satisfies the veto ordering criterion by ranking rows from highest to lowest probability while using numeric estimates rather than named-band labels = veto ordering criterion PASS, C-38 FAIL.

- Distinct from veto ordering criterion (FAIL_WRONG_ORDER): the ordering criterion requires rows sorted by probability rank; C-38 requires probability values to be drawn from a named-band prefill step defined before ranking begins, independent of sort order
- Not satisfiable if the veto ordering criterion is absent

**C-39 — Comms channel binding** (depth, 5 pts)
A channel prefill step (Step 6c) is inserted between the Frame Type prefill step (Step 6a) and the comms plan population step (Step 6b), defining the permissible communication channels per stakeholder segment or role before the comms plan is populated. Each comms plan row in Step 6b must draw its Channel column value exclusively from the Step 6c binding. FAIL_NO_CHANNEL fires if the Channel column is absent from the comms plan. FAIL_WRONG_CHANNEL fires if any row uses a channel not established in the Step 6c binding table. Both gates are distinct from FAIL_SAME_FRAME (C-14 — Frame Type distinctness across rows): a variation can have all distinct Frame Types while populating channels ad hoc with no binding prefill step, satisfying C-14 while failing C-39. A variation that satisfies C-13 and C-14 fully while populating channels without a preceding Step 6c binding step = C-13 PASS, C-14 PASS, C-39 FAIL.

- Distinct from C-13: C-13 requires Frame Type prefill and displacement-acknowledgment for inertia rows; C-39 requires a separate channel binding prefill step constraining the Channel column, an obligation orthogonal to Frame Type
- Distinct from C-14: C-14 requires Frame Type values to be distinct across comms rows; C-39 requires Channel values to be drawn from a pre-defined prefill binding rather than freely chosen at population time
- Not satisfiable if C-13 is absent

**Round 14 under v15:**
- V-01 → 235/245 (C-37 PASS; C-38 not satisfiable — no calibration bands; C-39 not satisfiable — no channel binding)
- V-02 → 235/245 (C-38 PASS; C-37 not satisfiable — no state machine; C-39 not satisfiable — no channel binding)
- V-03 → 235/245 (C-39 PASS; C-37 not satisfiable — no state machine; C-38 not satisfiable — no calibration bands)
- V-04 → 240/245 (C-37 PASS, C-38 PASS; C-39 not satisfiable — no channel binding)
- V-05 → 245/245 (C-37 PASS, C-38 PASS, C-39 PASS — first perfect score under v15)

---

### v13 to v14 changes (retained for history)

Two new criteria extracted from Round 13 excellence signals (V-04/V-05 axis):

| Criterion | Name | Type | Dependency |
|-----------|------|------|------------|
| C-35 | Pre-phase format constraint propagation | depth | C-33 |
| C-36 | Attribution-fused synthesis notation | depth | C-34 |

Aspirational count: 26 → 28. Max: 220 → 230. Golden threshold unchanged.

**C-35 — Pre-phase format constraint propagation** (depth, 5 pts)
The global format enforcement mechanism required by C-33 is placed at the prompt header before Phase 1 begins, establishing format obligations at construction time for every downstream structural step. The header placement propagates the constraint forward without requiring per-step repetition; FAIL_NO_PARSEABLE_FORMAT placed at the prompt header fires at the first offending structural output in execution order, rather than as a post-hoc audit applied after all steps complete.

- Distinct from C-33: C-33 requires uniform parseable format across all structural elements; C-35 requires the enforcement point to be the prompt header before Phase 1, making the constraint active at construction time rather than checked retrospectively
- Not satisfiable if C-33 is absent

**C-36 — Attribution-fused synthesis notation** (depth, 5 pts)
Synthesis cells use `field: value (Step X / C-YY)` inline notation, structurally fusing attribution with synthesis content within each cell. No separate attribution sub-step is required; the citation is encoded within the cell value itself, not collected in a footnote block or dedicated attribution section appended after the synthesis readout. FAIL_NO_ATTRIBUTION fires at the synthesis step if any field cell lacks fused inline citation in this notation form. A variation that satisfies C-34 via a post-synthesis attribution appendix (all five fields cited, but not fused inline within cells) = C-34 PASS, C-36 FAIL.

- Distinct from C-34: C-34 requires per-field step citation; C-36 requires that citation to be structurally fused inline within each synthesis cell using `field: value (source)` notation rather than separated into a distinct sub-step or section
- Not satisfiable if C-34 is absent

**Round 13 under v14:**
- V-03 → 210/230 (C-33, C-34, C-35, C-36 absent)
- V-01 → 220/230 (C-35 PASS; C-36 not satisfiable — C-34 absent)
