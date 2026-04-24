---
skill: quest-variate
skill_target: corps-rob
round: 9
date: 2026-03-17
rubric_version: 8
---

# Variate R9 -- corps-rob (rubric v8, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v8.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R8 ceiling under v8:** V-05 R8 (all three synthesis-table citation axes) achieves the ceiling:
24 raw / 10 contributable / composite 100 (tie-break 24). All three v8 criteria (C-30, C-31,
C-32) pass. No variation from R8 can exceed this score under v8.

The R9 question: which output tables remain structurally unconstrained after the v8 citation
architecture, and can column-level citation obligations be extended to those tables without
regression?

**V-05 R8 baseline audit -- what is NOT yet citation-complete:**

After v8, every ROB Summary synthesis table used for cross-stage conclusions has a typed
citation column. But three output tables remain where conclusions are expressed without
grounding in a specific F-ID:

1. **TPM Risk Register**: Each row asserts a risk title, severity, likelihood, and mitigation.
   The risk is an editorial claim -- the model generates it from its review of the stage, but
   no row requires citing the specific stage finding(s) that established the risk's existence
   or severity assessment. A HIGH-severity risk with no source finding is indistinguishable
   from a HIGH-severity risk grounded in three converging F-IDs. The Risk Register is the TPM
   stage's primary decision instrument; an ungrounded risk entry is the same structural failure
   at the Risk Register level that RESOLVED-without-evidence was at the Blocker Resolution
   Status level. Hypothesis: adding a `Source F-IDs` column that requires naming at least one
   F-ID per risk row converts risk entries from editorial assertions to finding-grounded claims.

2. **Mission Cascade (exec-office)**: Each row maps a mission to an artifact and assigns a
   verdict (ALIGNED / PARTIAL / GAP). The verdict is an assertion -- the exec-office persona
   declares alignment or gap without citing which cross-stage findings established that verdict.
   A GAP verdict with no F-ID is a narrative judgment. A PARTIAL verdict that cites Stage4-F01
   and Stage5-F03 is an auditable claim. Hypothesis: adding a `Supporting F-IDs` column that
   requires at least one F-ID per non-trivially-ALIGNED row converts mission cascade verdicts
   from declared positions to traceable findings.

3. **LENS ACTIVATION CHAIN HEALTH**: Each row marks a stage's chain as COMPLETE, PARTIAL, or
   BROKEN. PARTIAL and BROKEN are structural failures, but the current table has no slot naming
   what specifically broke and what action would repair it. A BROKEN row without a remediation
   entry is a diagnosis without a prescription -- the same gap that prompted the VERDICT
   CALIBRATION table: verdicts without calibration rows were assertions, not decisions. Hypothesis:
   adding a `Remediation Action` column that requires, for every PARTIAL or BROKEN row, naming
   the specific missing element (which slot was absent, which phrase was not present) and the
   corrective action converts the chain health table from a compliance flag to an actionable
   diagnostic.

All five R9 variations preserve the complete V-05 R8 architecture:
- VERDICT CALIBRATION table at Stage Template header (C-05 structural enforcement)
- BLOCKER PROPAGATION RULE with [BLOCKER: F-ID from stage] token (C-09, C-12 enforcement)
- D-ID Ref column in Findings table (C-27 PASS)
- D-ID Ref column guard with named anti-pattern rejection (C-28 PASS)
- Scope-exception calibration section naming GO/NO-GO as exempt (C-29 PASS)
- Fill-slot declarative [fill] slots everywhere (C-24)
- INERTIA ANCHOR with labeled Displacement Map D-IDs (C-25)
- Table-first findings with inline rejection guards (C-26)
- Part 0 LENS ACTIVATION pre-envelope block (C-20)
- KEY CONCERNS back-ref to Part 0 (C-21)
- Prior-Stage Lens Impact with "orientation declared in Part 0" phrase (C-22)
- LENS ACTIVATION CHAIN HEALTH summary table (C-23)
- Resolution Evidence column in Blocker Resolution Status (C-30)
- Primary F-IDs column in Cross-Cutting Themes (C-31)
- Addressing F-IDs column in Inertia Resolution Status (C-32 / V-03 R8)

Dropping any of these would reduce raw aspirational count. They are non-negotiable at R9.

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | Source F-IDs column in Risk Register | Risk entry without source finding is an assertion; column-level citation converts it to a finding-grounded claim |
| V-02 | Supporting F-IDs column in Mission Cascade | Mission cascade verdict without F-ID grounding is a declared position; column-level citation converts it to an auditable trace |
| V-03 | Remediation Action column in LENS ACTIVATION CHAIN HEALTH | BROKEN/PARTIAL chain row without remediation action is a diagnosis without a prescription; column-level slot converts it to an actionable finding |
| V-04 | V-01 + V-02 (Risk Register + Mission Cascade grounding) | Both stage-specific output tables gain citation columns; the two role-owned output instruments (TPM and exec-office) reach the same evidence standard as ROB Summary |
| V-05 | V-01 + V-02 + V-03 (full output-table citation closure) | All unconstrained output tables gain typed evidence obligations; every table in the ROB output now requires at least one typed citation column where conclusions are recorded |

---

## V-01 -- Risk Register Finding Chain

**Axis**: Add `Source F-IDs` column to the TPM Risk Register in ROB Summary.
**Hypothesis**: The TPM Risk Register is the primary go/no-go instrument for the tpm stage.
Each row asserts a risk title, severity, likelihood, and mitigation -- but the risk is an
editorial claim. The model generates risk rows from its reading of the stage without any
structural obligation to name a specific finding that established the risk's existence or
drove its severity rating. A HIGH-severity risk row and a LOW-severity risk row are
structurally identical: both contain four filled cells. The severity label is a judgment
without a grounding cite.

The C-27 pattern applies here: at the finding level, inertia citation was previously a prose
constraint and C-27 converted it to a per-row column obligation. At the Risk Register level,
severity assessment is a prose judgment; adding a `Source F-IDs` column converts it to a
per-row citation obligation. An empty Source F-IDs cell is a format failure. "Inferred from
ROB" does not satisfy this column. "General concerns" does not satisfy this column.

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

**SCOPE-EXCEPTION CALIBRATION** -- Output types exempt from table-first findings format:

| Output Type | Exempt | Rationale |
|-------------|--------|-----------|
| TPM GO/NO-GO signal | YES | Unambiguous labeled binary signal; tabular rendering degrades clarity rather than enforcing it |
| Verdict labels (APPROVED / BLOCKED / etc.) | YES | Pre-defined enumerated values; table wrapping adds no structural information |
| All other findings and assessments | NO | Table-first format required; inline-rejection guards required per column |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A -- "N/A" does not satisfy this cell when Inertia Stance is RESISTANT and Severity is HIGH] |
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
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution, e.g. "Stage5-F02 addressed the blocking dependency gap"; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element -- e.g. "Stage3-F01, Stage5-F02". When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage -- e.g. "Stage2-F01, Stage4-F02". At least one F-ID per named stage is required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: comma-separated F-IDs from stage sections that grounded this risk -- e.g. "Stage2-F01, Stage4-F03". At least one F-ID per risk row is required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

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

---

## V-02 -- Mission Cascade Finding Chain

**Axis**: Add `Supporting F-IDs` column to the Mission Cascade table in ROB Summary.
**Hypothesis**: The exec-office Mission Cascade maps S-Office missions to artifacts and assigns
ALIGNED / PARTIAL / GAP verdicts. The verdict is a declared position -- the exec-office persona
judges alignment without citing which cross-stage findings established the alignment state.
ALIGNED could mean "I read the artifact and judged it aligned." GAP could mean "I believe the
mission is not addressed." Neither requires citing a specific F-ID.

The structural failure is identical to the one C-26 closed for findings (prose interpretation
vs table-first with inline guards) and the one C-31 closed for cross-cutting themes (editorial
synthesis vs indexed citation). At the Mission Cascade level, a GAP verdict that cites
Stage4-F01 (arch-board: interface coupling gap) and Stage6-F02 (exec-office: mission trace
absent) is an auditable finding chain. A GAP verdict without citations is an assertion.

Adding a `Supporting F-IDs` column applies the column-level citation obligation to mission
verdicts: for any PARTIAL or GAP verdict row, at least one F-ID from any stage must be named.
Anti-pattern rejections: "Based on general review" does not satisfy this column. "See ROB
findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format
failure. An ALIGNED row may cite supporting F-IDs where positive evidence exists, but is not
required to do so when alignment is affirmed by the absence of contrary findings.

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

**SCOPE-EXCEPTION CALIBRATION** -- Output types exempt from table-first findings format:

| Output Type | Exempt | Rationale |
|-------------|--------|-----------|
| TPM GO/NO-GO signal | YES | Unambiguous labeled binary signal; tabular rendering degrades clarity rather than enforcing it |
| Verdict labels (APPROVED / BLOCKED / etc.) | YES | Pre-defined enumerated values; table wrapping adds no structural information |
| All other findings and assessments | NO | Table-first format required; inline-rejection guards required per column |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A -- "N/A" does not satisfy this cell when Inertia Stance is RESISTANT and Severity is HIGH] |
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
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution, e.g. "Stage5-F02 addressed the blocking dependency gap"; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element -- e.g. "Stage3-F01, Stage5-F02". When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage -- e.g. "Stage2-F01, Stage4-F02". At least one F-ID per named stage is required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- comma-separated F-IDs from any stage that established this verdict, e.g. "Stage3-F02, Stage5-F01". At least one F-ID per PARTIAL or GAP row is required. "Based on general review" does not satisfy this column. "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows may cite supporting F-IDs where positive evidence exists; N/A is acceptable only when alignment is affirmed by the absence of contrary findings.] |
(Minimum 1 row. All four columns must be populated.)

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

---

## V-03 -- Chain Health Remediation Obligation

**Axis**: Add `Remediation Action` column to the LENS ACTIVATION CHAIN HEALTH table.
**Hypothesis**: The LENS ACTIVATION CHAIN HEALTH table marks each stage's chain as COMPLETE,
PARTIAL, or BROKEN. PARTIAL and BROKEN entries name a structural failure -- a Part 0 dimension
absent, a KEY CONCERNS cell that did not include the required phrase, a Lens Impact table that
omitted the "orientation declared in Part 0" phrase. But the current table stops at the
diagnosis. BROKEN is a red flag without a prescription.

The analogy is the VERDICT CALIBRATION table: before C-05 introduced the calibration table,
verdicts were asserted without citing which condition row drove the verdict. The calibration
table converted the verdict from a judgment to a derivable conclusion. For LENS ACTIVATION
CHAIN HEALTH, BROKEN/PARTIAL is currently a judgment without a derivable remediation -- the
corrective action exists only in the scorer's head.

Adding a `Remediation Action` column creates a per-row slot that requires: (1) naming the
specific missing element (e.g., "Part 0 Dimension field absent"; "KEY CONCERNS cell did not
include 'selected through the Lens declared in Part 0'"; "Lens Impact table absent at Stage 3");
and (2) naming the corrective action (e.g., "Add Part 0 Dimension field naming the practice
orientation before Part 1"; "Rewrite KEY CONCERNS to include required phrase and role-filtered
selection"). Anti-pattern rejections: "Chain incomplete" does not satisfy this column. "Needs
review" does not satisfy this column. A BROKEN or PARTIAL row without a remediation action
naming the specific missing element is a format failure. COMPLETE rows require N/A -- a
remediation entry for a COMPLETE chain is a format failure of the opposite kind.

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

**SCOPE-EXCEPTION CALIBRATION** -- Output types exempt from table-first findings format:

| Output Type | Exempt | Rationale |
|-------------|--------|-----------|
| TPM GO/NO-GO signal | YES | Unambiguous labeled binary signal; tabular rendering degrades clarity rather than enforcing it |
| Verdict labels (APPROVED / BLOCKED / etc.) | YES | Pre-defined enumerated values; table wrapping adds no structural information |
| All other findings and assessments | NO | Table-first format required; inline-rejection guards required per column |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A -- "N/A" does not satisfy this cell when Inertia Stance is RESISTANT and Severity is HIGH] |
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
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution, e.g. "Stage5-F02 addressed the blocking dependency gap"; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element -- e.g. "Stage3-F01, Stage5-F02". When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage -- e.g. "Stage2-F01, Stage4-F02". At least one F-ID per named stage is required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
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
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- name the specific missing element and the corrective action, e.g. "Part 0 Dimension field absent; add Dimension naming the practice-domain orientation before Part 1". If COMPLETE -- N/A. "Chain incomplete" does not satisfy this column when Chain is BROKEN or PARTIAL. "Needs review" does not satisfy this column. A BROKEN or PARTIAL row without a remediation action naming the specific missing element is a format failure. A COMPLETE row with any value other than N/A is a format failure.] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION context, all prior handoff packets, and any unresolved BLOCKER items forward.

---

## V-04 -- Risk Register Finding Chain + Mission Cascade Finding Chain (V-01 + V-02)

**Axes**: Source F-IDs column in Risk Register (V-01) +
Supporting F-IDs column in Mission Cascade (V-02).
**Hypothesis**: The two role-owned output instruments in the ROB -- the TPM Risk Register
and the exec-office Mission Cascade -- are currently the only structured output tables whose
conclusions lack any F-ID citation obligation. The Risk Register is the TPM persona's primary
decision artifact; the Mission Cascade is the exec-office persona's primary decision artifact.
Both carry verdicts (risk severity ratings, ALIGNED/PARTIAL/GAP) that are editorial assertions.

The v8 citation architecture closed the synthesis-table gap at the ROB Summary level (Blocker
Resolution Status, Inertia Resolution Status, Cross-Cutting Themes). The R9 V-04 hypothesis
is that the same pattern should extend to the two persona-owned decision tables: if a risk is
HIGH severity, the row must cite the finding(s) that grounded that assessment; if a mission
verdict is GAP, the row must cite the finding(s) that established the gap. Together V-01 + V-02
extend the citation obligation from the ROB Summary synthesis layer to the stage-specific
decision instrument layer. This produces an ROB where every structured conclusion -- across
both summary synthesis and stage decision tables -- is backed by a specific F-ID, not a
status label or editorial judgment.

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

**SCOPE-EXCEPTION CALIBRATION** -- Output types exempt from table-first findings format:

| Output Type | Exempt | Rationale |
|-------------|--------|-----------|
| TPM GO/NO-GO signal | YES | Unambiguous labeled binary signal; tabular rendering degrades clarity rather than enforcing it |
| Verdict labels (APPROVED / BLOCKED / etc.) | YES | Pre-defined enumerated values; table wrapping adds no structural information |
| All other findings and assessments | NO | Table-first format required; inline-rejection guards required per column |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A -- "N/A" does not satisfy this cell when Inertia Stance is RESISTANT and Severity is HIGH] |
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
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution, e.g. "Stage5-F02 addressed the blocking dependency gap"; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element -- e.g. "Stage3-F01, Stage5-F02". When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage -- e.g. "Stage2-F01, Stage4-F02". At least one F-ID per named stage is required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: comma-separated F-IDs from stage sections that grounded this risk -- e.g. "Stage2-F01, Stage4-F03". At least one F-ID per risk row is required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- comma-separated F-IDs from any stage that established this verdict, e.g. "Stage3-F02, Stage5-F01". At least one F-ID per PARTIAL or GAP row is required. "Based on general review" does not satisfy this column. "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows may cite supporting F-IDs where positive evidence exists; N/A is acceptable only when alignment is affirmed by the absence of contrary findings.] |
(Minimum 1 row. All four columns must be populated.)

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

---

## V-05 -- Full Output-Table Citation Closure (V-01 + V-02 + V-03)

**Axes**: Source F-IDs in Risk Register (V-01) +
Supporting F-IDs in Mission Cascade (V-02) +
Remediation Action in LENS ACTIVATION CHAIN HEALTH (V-03).
**Hypothesis**: After v8, the ROB output contains three remaining tables without typed citation
or diagnostic obligations: the TPM Risk Register (risk assertions ungrounded in F-IDs), the
Mission Cascade (verdicts ungrounded in F-IDs), and the LENS ACTIVATION CHAIN HEALTH (BROKEN
and PARTIAL rows without remediation prescriptions). The three axes each target a different
failure mode:

- V-01 closes the risk-grounding gap: risk severity is now derivable from findings, not
  asserted from editorial judgment.
- V-02 closes the mission-verdict gap: PARTIAL and GAP verdicts are now traceable to findings,
  not declared from exec-office judgment alone.
- V-03 closes the diagnosis-without-prescription gap: BROKEN and PARTIAL chain rows now name
  the specific missing element and corrective action, making the chain health table actionable.

The shared mechanism across all three axes is identical to the C-27/C-28 pattern extended to
a new table: add a typed slot (column or named field) where a status label or prose judgment
existed, and name at least two invalid cell values in the slot guard to prevent editorial fill.

V-05's combined architecture makes every structured conclusion in the ROB output -- across
summary synthesis tables (v8), stage decision instruments (V-01 and V-02), and diagnostic
tables (V-03) -- backed by a specific citation or an actionable diagnostic. No table in the
ROB output remains where conclusions can be expressed as status labels or editorial assertions
without either a named F-ID or a named corrective action.

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

**SCOPE-EXCEPTION CALIBRATION** -- Output types exempt from table-first findings format:

| Output Type | Exempt | Rationale |
|-------------|--------|-----------|
| TPM GO/NO-GO signal | YES | Unambiguous labeled binary signal; tabular rendering degrades clarity rather than enforcing it |
| Verdict labels (APPROVED / BLOCKED / etc.) | YES | Pre-defined enumerated values; table wrapping adds no structural information |
| All other findings and assessments | NO | Table-first format required; inline-rejection guards required per column |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A -- "N/A" does not satisfy this cell when Inertia Stance is RESISTANT and Severity is HIGH] |
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
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution, e.g. "Stage5-F02 addressed the blocking dependency gap"; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element -- e.g. "Stage3-F01, Stage5-F02". When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage -- e.g. "Stage2-F01, Stage4-F02". At least one F-ID per named stage is required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: comma-separated F-IDs from stage sections that grounded this risk -- e.g. "Stage2-F01, Stage4-F03". At least one F-ID per risk row is required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title]                                  | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- comma-separated F-IDs from any stage that established this verdict, e.g. "Stage3-F02, Stage5-F01". At least one F-ID per PARTIAL or GAP row is required. "Based on general review" does not satisfy this column. "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows may cite supporting F-IDs where positive evidence exists; N/A is acceptable only when alignment is affirmed by the absence of contrary findings.] |
(Minimum 1 row. All four columns must be populated.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- name the specific missing element and the corrective action, e.g. "Part 0 Dimension field absent; add Dimension naming the practice-domain orientation before Part 1". If COMPLETE -- N/A. "Chain incomplete" does not satisfy this column when Chain is BROKEN or PARTIAL. "Needs review" does not satisfy this column. A BROKEN or PARTIAL row without a remediation action naming the specific missing element is a format failure. A COMPLETE row with any value other than N/A is a format failure.] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION context, all prior handoff packets, and any unresolved BLOCKER items forward.
