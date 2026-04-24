---
skill: quest-variate
skill_target: corps-rob
round: 7
date: 2026-03-17
rubric_version: 6
---

# Variate R7 -- corps-rob (rubric v6, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v6.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R6 diagnosis under v6 re-grades:** V-05 R6 (fill-slot + prominent inertia + table-first)
achieves the ceiling: 18 raw / 10 contributable / composite 100 (tie-break 18). All three
v6 criteria (C-24, C-25, C-26) pass. No variation from R6 can exceed this score under v6.

The R7 question: can the prompt architecture be further hardened without regression -- and
do the new axes reveal excellence patterns that would justify rubric evolution beyond v6?

Three structural questions remain open after V-05 R6:

1. **D-ID citation in finding rows**: C-25 requires findings to "cite a D-ID" when Inertia
   Stance is RESISTANT and Severity is HIGH, but V-05 R6 encodes this as a prose constraint
   note below the Findings table -- not as a table column. The executing model can satisfy
   the prose constraint with a free-text reference that is not machine-scannable. Hypothesis:
   adding a dedicated `D-ID Ref` column to the Findings table converts C-25 from a
   constraint reminder into a column-level format requirement, making D-ID omission visible
   in the same way an empty Owner cell is visible.

2. **Blocker forward propagation**: The BLOCKER field at each stage records YES/NO locally,
   but the only mechanism ensuring a YES blocker reaches the next stage is the Handoff
   Packet's Cross-Stage References Forwarded list -- which can carry it without flagging it
   as a blocker. The receiving stage's Part 1 PRIOR-STAGE ESCALATIONS slot has no explicit
   rule requiring it to pick up BLOCKER=YES items. Hypothesis: adding an explicit propagation
   rule (BLOCKER=YES at Stage N -> the blocking F-ID MUST appear in Stage N+1's
   PRIOR-STAGE ESCALATIONS slot, labeled as BLOCKER) prevents orphaned blockers.

3. **Verdict calibration**: The four Stage Verdict outcomes (APPROVED / APPROVED WITH
   CONDITIONS / BLOCKED / DEFERRED) are uncalibrated. The executing model chooses freely
   given no formal mapping from finding severity to verdict. Hypothesis: adding a compact
   verdict calibration table at the Stage Template header -- mapping severity/resolution
   combinations to verdict -- makes verdicts consistent across stages and evaluators,
   making C-05 (GO/NO-GO signal) more reliable as a stopping condition.

All five R7 variations preserve the complete V-05 R6 architecture:
- Fill-slot declarative [fill] slots everywhere (C-24)
- INERTIA ANCHOR with labeled Displacement Map D-IDs (C-25)
- Table-first findings with inline rejection guards (C-26)
- Part 0 LENS ACTIVATION pre-envelope block (C-20)
- KEY CONCERNS back-ref to Part 0 (C-21)
- Prior-Stage Lens Impact with "orientation declared in Part 0" phrase (C-22)
- LENS ACTIVATION CHAIN HEALTH summary table (C-23)

Dropping any of these would reduce raw aspirational count. They are non-negotiable at R7.

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | D-ID Ref column in Findings table | Column-level enforcement converts C-25 prose constraint to format requirement |
| V-02 | Explicit blocker forward propagation rule | BLOCKER=YES at stage N forces F-ID into stage N+1 PRIOR-STAGE ESCALATIONS |
| V-03 | Verdict calibration table | Formal severity->verdict mapping makes C-05 GO/NO-GO consistent |
| V-04 | V-01 D-ID column + V-02 blocker propagation | Dual enforcement: inertia citation + inter-stage communication |
| V-05 | V-01 + V-02 + V-03 (full integration) | Maximum structural enforcement on all three open axes |

---

## V-01 -- D-ID Ref Column in Findings Table

**Axis**: Output format -- Findings table column design
**Hypothesis**: C-25 requires that when Inertia Stance is RESISTANT and a finding is HIGH
severity, the finding must cite a D-ID from the Displacement Map. V-05 R6 encodes this as
a prose constraint below the Findings table. Adding a `D-ID Ref` column to the table body
makes the citation a visible cell -- empty when N/A, populated with the D-ID when the
RESISTANT+HIGH condition is met. An empty cell in a required column is a format failure;
a prose constraint can be satisfied with any passing mention.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

---

## INERTIA ANCHOR

Fill before Stage 1. Every slot and every table cell must be populated.

  Status-Quo Competitor: [fill: name the system, process, or behavior this topic
    displaces -- not the topic, but what it replaces or competes with]

  Displacement Map:
  | D-ID | Displaced Element | Cost-Bearer (team/role/system) | Change Type |
  |------|-------------------|---------------------------------|-------------|
  | D-01 | [fill]            | [fill]                          | [migration / behavior change / tooling switch / process change] |
  | D-02 | [fill]            | [fill]                          | [fill] |
  (Minimum 2 rows. Each stage's INERTIA CHECK must cite a row from this table by D-ID.)

  Inertia Risk Statement: [fill: one sentence naming the strongest single source of
    status-quo resistance -- the displacement most likely to create adoption friction]

---

## Stage Template

Use the following template for each stage. Fill every [fill] slot. Populate every table.
A visible unfilled slot or an empty table where content is required indicates non-compliance.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets, or NONE] |

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element name from Displacement Map}] |
| Status-Quo Pressure | [fill: what this role's stakeholders defend; what the role risks if topic succeeds or fails. Not "change is hard." Name the concrete pressure.] |
| Inertia Stance | [fill: RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence explaining the posture] |

Constraints:
- Minimum 3 stages must have a non-trivial Inertia Check (D-ID cited, concrete pressure named).
- When Inertia Stance is RESISTANT and any finding is HIGH severity, at least 1 finding
  must cite the inertia D-ID in its D-ID Ref column (see Findings table below).

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) | D-ID Ref |
|------|----------|-------------------------------------------------|--------------|------------------------------|----------|
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Minimum 2 rows. All six columns must be populated. An empty D-ID Ref cell where
Inertia Stance is RESISTANT and Severity is HIGH is a format failure.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension -- a
concern specific to this role's practice orientation, not generic across all reviewers.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill: why this stage's lens changes or confirms the reading] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict
  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: cite at least one F-ID. One sentence.]

  tpm stage only -- top-level labeled signal required:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill -- reason the downstream stage cannot proceed without resolution] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance of the forwarded cross-stage picture.
Must add substance not already visible in the table above -- do not copy rows into prose.
Acceptable: pattern across multiple rows; risk escalation beyond any single row;
downstream action not captured in any individual row.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Why Recurrence Elevates Severity |
|-------|--------------------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict |
|---------------------------------------------------------------|------------------|---------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP |
(Minimum 1 row.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain |
|-------|--------|-------------------------|------------------------|-------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, and all prior handoff packets forward.

---

## V-02 -- Explicit Blocker Forward Propagation

**Axis**: Lifecycle emphasis -- inter-stage blocker communication
**Hypothesis**: A BLOCKER=YES at Stage N is only useful if Stage N+1 receives and acts on
it. V-05 R6 places the blocker in the Handoff Packet's Cross-Stage References Forwarded
list, but that list carries all references -- the receiver has no explicit structural
obligation to elevate BLOCKER items above ordinary escalations. Adding a forward
propagation rule -- BLOCKER=YES at Stage N requires the blocking F-ID to appear in Stage
N+1's PRIOR-STAGE ESCALATIONS cell labeled as [BLOCKER] -- makes blocker reception
visible and machine-scannable. An unlabeled or missing blocker in the next stage's Part 1
is a format failure, not a prose omission.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

---

## INERTIA ANCHOR

Fill before Stage 1. Every slot and every table cell must be populated.

  Status-Quo Competitor: [fill: name the system, process, or behavior this topic
    displaces -- not the topic, but what it replaces or competes with]

  Displacement Map:
  | D-ID | Displaced Element | Cost-Bearer (team/role/system) | Change Type |
  |------|-------------------|---------------------------------|-------------|
  | D-01 | [fill]            | [fill]                          | [migration / behavior change / tooling switch / process change] |
  | D-02 | [fill]            | [fill]                          | [fill] |
  (Minimum 2 rows. Each stage's INERTIA CHECK must cite a row from this table by D-ID.)

  Inertia Risk Statement: [fill: one sentence naming the strongest single source of
    status-quo resistance -- the displacement most likely to create adoption friction]

---

## Stage Template

Use the following template for each stage. Fill every [fill] slot. Populate every table.
A visible unfilled slot or an empty table where content is required indicates non-compliance.

**BLOCKER PROPAGATION RULE**: If Stage N's Blocker Field contains BLOCKER=YES, then Stage
N+1's Part 1 PRIOR-STAGE ESCALATIONS cell MUST include the blocking F-ID labeled as
[BLOCKER: {F-ID} from {stage name}]. Absence of the [BLOCKER: ...] label in PRIOR-STAGE
ESCALATIONS when the immediately prior stage had BLOCKER=YES is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets. If the immediately prior stage had BLOCKER=YES, this cell MUST include "[BLOCKER: {F-ID} from {stage name}]" as the first entry. NONE only if no escalations AND no prior-stage blockers.] |

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element name from Displacement Map}] |
| Status-Quo Pressure | [fill: what this role's stakeholders defend; what the role risks if topic succeeds or fails. Not "change is hard." Name the concrete pressure.] |
| Inertia Stance | [fill: RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence explaining the posture] |

Constraints:
- Minimum 3 stages must have a non-trivial Inertia Check (D-ID cited, concrete pressure named).
- When Inertia Stance is RESISTANT and any finding is HIGH severity, at least 1 finding
  must reference the inertia contribution as a factor.

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) |
|------|----------|-------------------------------------------------|--------------|------------------------------|
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] |
(Minimum 2 rows. All five columns must be populated.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension -- a
concern specific to this role's practice orientation, not generic across all reviewers.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill: why this stage's lens changes or confirms the reading] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict
  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: cite at least one F-ID. One sentence.]

  tpm stage only -- top-level labeled signal required:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill -- reason the downstream stage cannot proceed without resolution. If YES, the blocking F-ID MUST appear in the next stage's PRIOR-STAGE ESCALATIONS labeled as [BLOCKER].] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance of the forwarded cross-stage picture.
Must add substance not already visible in the table above -- do not copy rows into prose.
Acceptable: pattern across multiple rows; risk escalation beyond any single row;
downstream action not captured in any individual row.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status |
|-------|------|------------------------------|-------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Why Recurrence Elevates Severity |
|-------|--------------------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict |
|---------------------------------------------------------------|------------------|---------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP |
(Minimum 1 row.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain |
|-------|--------|-------------------------|------------------------|-------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, all prior handoff packets, and any unresolved BLOCKER items forward.

---

## V-03 -- Verdict Calibration Table

**Axis**: Output format -- verdict definition and calibration
**Hypothesis**: The four Stage Verdict options (APPROVED / APPROVED WITH CONDITIONS /
BLOCKED / DEFERRED) are uncalibrated in V-05 R6. The executing model selects from four
options without a formal mapping from finding characteristics to verdict outcome. This
makes C-05 (unambiguous GO/NO-GO signal) inconsistent across runs: two instances running
the same ROB for the same topic might produce different verdicts for the same finding
profile. Adding a compact verdict calibration table -- a severity x resolution-status
mapping -- at the Stage Template header makes verdict selection deterministic and
comparable across stages and runs.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

---

## INERTIA ANCHOR

Fill before Stage 1. Every slot and every table cell must be populated.

  Status-Quo Competitor: [fill: name the system, process, or behavior this topic
    displaces -- not the topic, but what it replaces or competes with]

  Displacement Map:
  | D-ID | Displaced Element | Cost-Bearer (team/role/system) | Change Type |
  |------|-------------------|---------------------------------|-------------|
  | D-01 | [fill]            | [fill]                          | [migration / behavior change / tooling switch / process change] |
  | D-02 | [fill]            | [fill]                          | [fill] |
  (Minimum 2 rows. Each stage's INERTIA CHECK must cite a row from this table by D-ID.)

  Inertia Risk Statement: [fill: one sentence naming the strongest single source of
    status-quo resistance -- the displacement most likely to create adoption friction]

---

## Stage Template

Use the following template for each stage. Fill every [fill] slot. Populate every table.
A visible unfilled slot or an empty table where content is required indicates non-compliance.

**VERDICT CALIBRATION** -- Use this table to determine the Stage Verdict. Select the row
that best matches the finding profile at this stage. When multiple rows apply, use the
highest-severity applicable verdict.

| Condition | Verdict |
|-----------|---------|
| Any HIGH finding with no owner assigned, OR no resolution path stated, OR TPM NO-GO | BLOCKED |
| Any HIGH finding with an owner and a concrete resolution, OR 2+ MED findings with at least 1 unowned | APPROVED WITH CONDITIONS |
| Any finding requires external input before resolution, and that input is not available at this stage | DEFERRED |
| No HIGH findings; all MED findings have owners and resolutions; LOW findings noted | APPROVED |

Note: BLOCKED takes precedence over APPROVED WITH CONDITIONS. DEFERRED applies only when
the stage genuinely cannot resolve the finding within its scope -- not as a hedge.
The TPM GO/NO-GO signal is exempt from this table (it is a labeled binary, not a verdict).

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets, or NONE] |

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element name from Displacement Map}] |
| Status-Quo Pressure | [fill: what this role's stakeholders defend; what the role risks if topic succeeds or fails. Not "change is hard." Name the concrete pressure.] |
| Inertia Stance | [fill: RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence explaining the posture] |

Constraints:
- Minimum 3 stages must have a non-trivial Inertia Check (D-ID cited, concrete pressure named).
- When Inertia Stance is RESISTANT and any finding is HIGH severity, at least 1 finding
  must reference the inertia contribution as a factor.

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) |
|------|----------|-------------------------------------------------|--------------|------------------------------|
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] |
(Minimum 2 rows. All five columns must be populated.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension -- a
concern specific to this role's practice orientation, not generic across all reviewers.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill: why this stage's lens changes or confirms the reading] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict
Apply the VERDICT CALIBRATION table above to select the verdict for this stage's finding
profile. Cite the calibration row that applies.

  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table]
  Rationale: [fill: cite at least one F-ID and name the finding that drove the verdict. One sentence.]

  tpm stage only -- top-level labeled signal required:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill -- reason the downstream stage cannot proceed without resolution] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance of the forwarded cross-stage picture.
Must add substance not already visible in the table above -- do not copy rows into prose.
Acceptable: pattern across multiple rows; risk escalation beyond any single row;
downstream action not captured in any individual row.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table
    or name the dominant cross-stage condition that drove the overall verdict]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Why Recurrence Elevates Severity |
|-------|--------------------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict |
|---------------------------------------------------------------|------------------|---------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP |
(Minimum 1 row.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain |
|-------|--------|-------------------------|------------------------|-------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, and all prior handoff packets forward.

---

## V-04 -- D-ID Column + Blocker Propagation (V-01 + V-02)

**Axes**: Output format (D-ID Ref column in Findings) + Lifecycle emphasis (explicit
blocker forward propagation)
**Hypothesis**: These two axes address distinct failure modes that compound each other.
V-01's D-ID column makes the RESISTANT+HIGH->inertia-citation link visible at the row
level; V-02's propagation rule makes blocker reception visible at the next-stage Part 1
level. Together: a finding that is HIGH severity and raised by a RESISTANT stage must
cite its D-ID (visible in the finding row), and if that finding is a blocker, the next
stage must receive it with the [BLOCKER:] label (visible in Part 1). These two visibility
requirements close a path where a HIGH inertia-driven finding could be raised, noted
as blocking, yet fail to carry its inertia context into the downstream stage.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

---

## INERTIA ANCHOR

Fill before Stage 1. Every slot and every table cell must be populated.

  Status-Quo Competitor: [fill: name the system, process, or behavior this topic
    displaces -- not the topic, but what it replaces or competes with]

  Displacement Map:
  | D-ID | Displaced Element | Cost-Bearer (team/role/system) | Change Type |
  |------|-------------------|---------------------------------|-------------|
  | D-01 | [fill]            | [fill]                          | [migration / behavior change / tooling switch / process change] |
  | D-02 | [fill]            | [fill]                          | [fill] |
  (Minimum 2 rows. Each stage's INERTIA CHECK must cite a row from this table by D-ID.)

  Inertia Risk Statement: [fill: one sentence naming the strongest single source of
    status-quo resistance -- the displacement most likely to create adoption friction]

---

## Stage Template

Use the following template for each stage. Fill every [fill] slot. Populate every table.
A visible unfilled slot or an empty table where content is required indicates non-compliance.

**BLOCKER PROPAGATION RULE**: If Stage N's Blocker Field contains BLOCKER=YES, then Stage
N+1's Part 1 PRIOR-STAGE ESCALATIONS cell MUST include "[BLOCKER: {F-ID} from {stage name}]"
as its first entry. Absence of this label when the immediately prior stage had BLOCKER=YES
is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets. If the immediately prior stage had BLOCKER=YES, this cell MUST begin with "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers.] |

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element name from Displacement Map}] |
| Status-Quo Pressure | [fill: what this role's stakeholders defend; what the role risks if topic succeeds or fails. Not "change is hard." Name the concrete pressure.] |
| Inertia Stance | [fill: RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence explaining the posture] |

Constraints:
- Minimum 3 stages must have a non-trivial Inertia Check (D-ID cited, concrete pressure named).
- When Inertia Stance is RESISTANT and any finding is HIGH severity, at least 1 finding
  must cite the inertia D-ID in its D-ID Ref column (see Findings table below).

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) | D-ID Ref |
|------|----------|-------------------------------------------------|--------------|------------------------------|----------|
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Minimum 2 rows. All six columns must be populated. An empty D-ID Ref cell where
Inertia Stance is RESISTANT and Severity is HIGH is a format failure.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension -- a
concern specific to this role's practice orientation, not generic across all reviewers.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill: why this stage's lens changes or confirms the reading] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict
  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: cite at least one F-ID. One sentence.]

  tpm stage only -- top-level labeled signal required:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill -- reason the downstream stage cannot proceed without resolution. If YES, the blocking F-ID MUST appear labeled as [BLOCKER: {F-ID} from {this stage name}] in the next stage's PRIOR-STAGE ESCALATIONS.] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance of the forwarded cross-stage picture.
Must add substance not already visible in the table above -- do not copy rows into prose.
Acceptable: pattern across multiple rows; risk escalation beyond any single row;
downstream action not captured in any individual row.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status |
|-------|------|------------------------------|-------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Why Recurrence Elevates Severity |
|-------|--------------------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict |
|---------------------------------------------------------------|------------------|---------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP |
(Minimum 1 row.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain |
|-------|--------|-------------------------|------------------------|-------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, all prior handoff packets, and any unresolved BLOCKER items forward.

---

## V-05 -- D-ID Column + Blocker Propagation + Verdict Calibration (Full Integration)

**Axes**: D-ID Ref column (V-01) + Blocker forward propagation (V-02) + Verdict
calibration table (V-03)
**Hypothesis**: The three R7 axes are mutually reinforcing and each targets a distinct
gap in V-05 R6. V-01's D-ID column makes inertia-finding citation machine-scannable.
V-02's blocker propagation makes blocker reception at the receiving stage structurally
required. V-03's verdict calibration table makes the BLOCKED/APPROVED judgment
reproducible from finding characteristics alone. Together: every path from
inertia-driven finding to blocking verdict to downstream reception is structurally
enforced -- no element depends on prose compliance alone. This is the candidate for
highest excellence signal density under v6: if any of these three axes generates a
distinct output quality marker not captured by C-01 through C-26, it surfaces here.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

---

## INERTIA ANCHOR

Fill before Stage 1. Every slot and every table cell must be populated.

  Status-Quo Competitor: [fill: name the system, process, or behavior this topic
    displaces -- not the topic, but what it replaces or competes with]

  Displacement Map:
  | D-ID | Displaced Element | Cost-Bearer (team/role/system) | Change Type |
  |------|-------------------|---------------------------------|-------------|
  | D-01 | [fill]            | [fill]                          | [migration / behavior change / tooling switch / process change] |
  | D-02 | [fill]            | [fill]                          | [fill] |
  (Minimum 2 rows. Each stage's INERTIA CHECK must cite a row from this table by D-ID.)

  Inertia Risk Statement: [fill: one sentence naming the strongest single source of
    status-quo resistance -- the displacement most likely to create adoption friction]

---

## Stage Template

Use the following template for each stage. Fill every [fill] slot. Populate every table.
A visible unfilled slot or an empty table where content is required indicates non-compliance.

**VERDICT CALIBRATION** -- Use this table to determine the Stage Verdict. Select the row
that best matches the finding profile at this stage. When multiple rows apply, use the
highest-severity applicable verdict.

| Condition | Verdict |
|-----------|---------|
| Any HIGH finding with no owner assigned, OR no resolution path stated, OR TPM NO-GO | BLOCKED |
| Any HIGH finding with an owner and a concrete resolution, OR 2+ MED findings with at least 1 unowned | APPROVED WITH CONDITIONS |
| Any finding requires external input before resolution, and that input is not available at this stage | DEFERRED |
| No HIGH findings; all MED findings have owners and resolutions; LOW findings noted | APPROVED |

Note: BLOCKED takes precedence over APPROVED WITH CONDITIONS. DEFERRED applies only when
the stage genuinely cannot resolve the finding within its scope -- not as a hedge.
The TPM GO/NO-GO signal is exempt from this table (it is a labeled binary, not a verdict).

**BLOCKER PROPAGATION RULE**: If Stage N's Blocker Field contains BLOCKER=YES, then Stage
N+1's Part 1 PRIOR-STAGE ESCALATIONS cell MUST include "[BLOCKER: {F-ID} from {stage name}]"
as its first entry. Absence of this label when the immediately prior stage had BLOCKER=YES
is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets. If the immediately prior stage had BLOCKER=YES, this cell MUST begin with "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers.] |

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element name from Displacement Map}] |
| Status-Quo Pressure | [fill: what this role's stakeholders defend; what the role risks if topic succeeds or fails. Not "change is hard." Name the concrete pressure.] |
| Inertia Stance | [fill: RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence explaining the posture] |

Constraints:
- Minimum 3 stages must have a non-trivial Inertia Check (D-ID cited, concrete pressure named).
- When Inertia Stance is RESISTANT and any finding is HIGH severity, at least 1 finding
  must cite the inertia D-ID in its D-ID Ref column (see Findings table below).

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) | D-ID Ref |
|------|----------|-------------------------------------------------|--------------|------------------------------|----------|
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Minimum 2 rows. All six columns must be populated. An empty D-ID Ref cell where
Inertia Stance is RESISTANT and Severity is HIGH is a format failure.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension -- a
concern specific to this role's practice orientation, not generic across all reviewers.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill: why this stage's lens changes or confirms the reading] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict
Apply the VERDICT CALIBRATION table above to select the verdict for this stage's finding
profile. Cite the calibration row that applies.

  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table]
  Rationale: [fill: cite at least one F-ID and name the finding that drove the verdict. One sentence.]

  tpm stage only -- top-level labeled signal required:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill -- reason the downstream stage cannot proceed without resolution. If YES, the blocking F-ID MUST appear labeled as [BLOCKER: {F-ID} from {this stage name}] in the next stage's PRIOR-STAGE ESCALATIONS.] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance of the forwarded cross-stage picture.
Must add substance not already visible in the table above -- do not copy rows into prose.
Acceptable: pattern across multiple rows; risk escalation beyond any single row;
downstream action not captured in any individual row.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table
    or name the dominant cross-stage condition that drove the overall verdict]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status |
|-------|------|------------------------------|-------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Why Recurrence Elevates Severity |
|-------|--------------------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict |
|---------------------------------------------------------------|------------------|---------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP |
(Minimum 1 row.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain |
|-------|--------|-------------------------|------------------------|-------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION context, all prior handoff packets, and any unresolved BLOCKER items forward.
