## scout-stakeholders rubric — v15

**v15 written.** Three new criteria extracted from Round 14 excellence signals across three structural axes (V-01 org context state machine, V-02 veto probability calibration, V-03 comms channel binding):

| ID | Name | Source | Dependency |
|----|------|--------|------------|
| C-37 | Org context state machine label integrity | V-01 axis | C-01 |
| C-38 | Veto probability calibration bands | V-02 axis | veto ordering criterion |
| C-39 | Comms channel binding | V-03 axis | C-13 |

**Updated totals:** 31 aspirational × 5 = 155 pts; **max 245 pts**. Golden threshold (>= 80) unchanged.

**Under v15 (Round 14 re-scored):**
- V-01 → 235/245 (C-37 PASS; C-38 not satisfiable — no calibration bands; C-39 not satisfiable — no channel binding)
- V-02 → 235/245 (C-38 PASS; C-37 not satisfiable — no state machine; C-39 not satisfiable — no channel binding)
- V-03 → 235/245 (C-39 PASS; C-37 not satisfiable — no state machine; C-38 not satisfiable — no calibration bands)
- V-04 → 240/245 (C-37 PASS, C-38 PASS; C-39 not satisfiable — no channel binding)
- V-05 → 245/245 (C-37 PASS, C-38 PASS, C-39 PASS — first perfect score under v15)

**Distinction logic:**

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

---

### v14 to v15 changes summary

| Criterion | Name | Type | Dependency |
|-----------|------|------|------------|
| C-37 | Org context state machine label integrity | depth | C-01 |
| C-38 | Veto probability calibration bands | depth | veto ordering criterion |
| C-39 | Comms channel binding | depth | C-13 |

Aspirational count: 28 → 31. Max: 230 → 245. Golden threshold unchanged.

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
- V-02 → 220/230 (C-36 PASS; C-35 not satisfiable — C-33 absent)
- V-04 → 230/230 (C-35 PASS, C-36 PASS — first perfect score under v14)
- V-05 → 230/230 (C-35 PASS, C-36 PASS)

---

### v12 to v13 changes (retained for history)

Two new criteria extracted from Round 12 excellence signals:

| Criterion | Name | Type | Dependency |
|-----------|------|------|------------|
| C-33 | Machine-parseable structural format | depth | C-02 |
| C-34 | Attributed synthesis rows | depth | C-32 |

Aspirational count: 24 → 26. Max: 210 → 220. Golden threshold unchanged.

**C-33 — Machine-parseable structural format** (depth, 5 pts)
Every structural output in the prompt — every grid, risk table, scoring table, prefill table, communication schedule, and synthesis readout — uses a machine-parseable format (Markdown pipe table or equivalent key-value structure) uniformly across all steps. FAIL_NO_PARSEABLE_FORMAT fires at any structural step that produces output in non-parseable prose or freeform layout. The constraint applies uniformly across all structural elements, not only at the synthesis step.

A variation can satisfy C-32 (synthesis step produces all five required fields) while presenting synthesis rows as prose paragraphs with no table or key-value structure (C-33 FAIL).

- Distinct from C-02: C-02 is satisfied by a grid in any legible form; C-33 requires parseable format across all structural elements
- Distinct from C-32: C-32 requires the synthesis step to exist with required fields; C-33 requires all structural outputs — including but not limited to synthesis rows — to use parseable format
- Not satisfiable if C-02 is absent

**C-34 — Attributed synthesis rows** (depth, 5 pts)
Each synthesis row produced by the C-32 synthesis step includes per-field source attribution — each of the five required fields (grid position, engagement window, conflict exposure, champion status, comms frame type) carries an explicit citation naming the originating step or criterion that produced it (e.g., "grid position: Phase 3 / C-02", "engagement window: Step 5a", "conflict exposure: Step 1a / C-06", "champion status: Step 5b", "comms frame type: Step 6a / C-13"). FAIL_NO_ATTRIBUTION must be present as an inline gate label at the synthesis step if attribution is absent from any field. Synthesis rows that contain all five required field values but no source citation per field = FAIL.

- Distinct from C-32: C-32 requires field presence; C-34 requires each field to name its originating step
- Distinct from C-22: C-22 requires the amendment mandate to enumerate structural targets; C-34 requires per-field attribution within synthesis rows themselves
- Not satisfiable if C-32 is absent

**Round 12 under v13:**
- V-03 → 215/220 (C-33 PASS; C-34 FAIL)
- V-04 → 215/220 (C-33 FAIL; C-34 PASS)
- V-01, V-02, V-05 → 210/220 (C-33 FAIL, C-34 FAIL)

---

### v11 to v12 changes (retained for history)

Two new criteria extracted from Round 11 V-05 (dense synthesis + trajectory probe).
