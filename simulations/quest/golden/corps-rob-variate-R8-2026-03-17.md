---
skill: quest-variate
skill_target: corps-rob
round: 8
date: 2026-03-17
rubric_version: 7
---

# Variate R8 -- corps-rob (rubric v7, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v7.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R7 diagnosis under v7 re-grades:** V-05 R7 (D-ID column + blocker propagation + verdict
calibration) achieves the ceiling: 21 raw / 10 contributable / composite 100 (tie-break 21).
All three v7 criteria (C-27, C-28, C-29) pass. No variation from R7 can exceed this score
under v7.

The R8 question: can the prompt architecture be further hardened without regression -- and
do the new axes reveal excellence patterns that would justify rubric evolution beyond v7?

Three structural questions remain open after V-05 R7:

1. **Blocker resolution traceability**: The Blocker Resolution Status table in ROB Summary
   records which BLOCKER=YES items were raised and whether they were RESOLVED or OPEN, but
   does not name the artifact that produced the RESOLVED state. An executing model can mark
   an item RESOLVED based on editorial judgment without citing a specific downstream F-ID or
   handoff packet entry. The RESOLVED label is semantically indistinguishable from an
   assertion. Hypothesis: adding a `Resolution Evidence` column that requires naming the
   downstream F-ID or stage action that closed the blocker converts RESOLVED from a label
   into a traceable citation -- the same column-level obligation that C-27 applies to D-ID
   citations in finding rows.

2. **Cross-cutting theme finding chain**: The Cross-Cutting Themes table identifies which
   stages share a theme and explains why recurrence elevates severity, but does not cite the
   specific findings that constitute the theme. An executing model can write a plausible
   theme description that is not grounded in any specific F-ID. Hypothesis: adding a
   `Primary F-IDs` column requiring at least one F-ID per named stage converts the theme
   from an editorial synthesis to an indexed chain that is auditable without re-reading
   individual stage sections.

3. **Inertia resolution evidence**: The Inertia Resolution Status table tracks whether each
   D-ID from the Displacement Map was addressed across stages, but RESOLVED means only that
   some stage surfaced the displacement -- not that any finding named and closed it. The
   D-ID Ref column (C-27) ensures findings cite D-IDs; the Inertia Resolution Status table
   should complete the reverse trace: from D-ID to the specific finding(s) that addressed
   it. Hypothesis: adding an `Addressing F-IDs` column makes the D-ID-to-finding chain
   navigable in both directions -- forward (C-27: finding cites D-ID) and backward (new:
   D-ID row cites addressing findings).

All five R8 variations preserve the complete V-05 R7 architecture:
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

Dropping any of these would reduce raw aspirational count. They are non-negotiable at R8.

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | Resolution Evidence column in Blocker Resolution Status | RESOLVED label without citation is an assertion; column-level evidence converts it to a trace |
| V-02 | Primary F-IDs column in Cross-Cutting Themes | Theme without F-ID grounding is editorial; column-level citation converts it to an indexed chain |
| V-03 | Addressing F-IDs column in Inertia Resolution Status | Completes D-ID chain: C-27 (finding -> D-ID) + new (D-ID -> addressing finding) |
| V-04 | V-01 + V-02 (blocker closure + theme chain) | Dual synthesis-table audit closure on the two highest-use ROB Summary tables |
| V-05 | V-01 + V-02 + V-03 (full synthesis-table audit closure) | All three ROB Summary status tables gain named-citation columns; maximum structural evidence chain |

---

## V-01 -- Blocker Resolution Traceability

**Axis**: Add `Resolution Evidence` column to Blocker Resolution Status table in ROB Summary.
**Hypothesis**: The Blocker Resolution Status table currently closes the blocker loop by
recording RESOLVED or OPEN per raised BLOCKER=YES item. But RESOLVED is a label that depends
on the executing model's editorial judgment -- the table does not require naming any specific
downstream artifact that produced the resolved state. Adding a `Resolution Evidence` column
applies the C-27 column-level citation obligation pattern to the resolution audit table: an
empty or vague cell when Resolution Status is RESOLVED is a format failure, not a prose
quality gap. This converts the resolution audit from assertion-level to evidence-level.

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

---

## V-02 -- Cross-Cutting Theme Finding Chain

**Axis**: Add `Primary F-IDs` column to the Cross-Cutting Themes table in ROB Summary.
**Hypothesis**: The Cross-Cutting Themes table synthesizes which concerns appear across
multiple stages and explains why recurrence elevates severity, but does not require citing
the specific findings that constitute the theme. An executing model can produce a plausible
theme description without grounding it in any F-ID. The resulting "theme" is editorial
synthesis -- the same quality gap that C-26 closed for findings (prose interpretation vs
table-first format with inline guards) exists here at the summary level. Adding a
`Primary F-IDs` column applies the indexed-citation pattern to theme synthesis: a theme row
without at least one F-ID per named stage is a format failure, and "multiple findings" does
not satisfy the column.

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

## V-03 -- Inertia Resolution Evidence

**Axis**: Add `Addressing F-IDs` column to the Inertia Resolution Status table in ROB Summary.
**Hypothesis**: The D-ID Ref column (C-27) establishes a forward trace: when a stage finding
is RESISTANT+HIGH, the finding row cites the D-ID from the Displacement Map. The Inertia
Resolution Status table establishes which D-IDs were surfaced across stages and their overall
status -- but the reverse trace is absent. RESOLVED means some stage surfaced the
displacement; it does not name the finding(s) that addressed it. The D-ID-to-finding chain
is navigable only by re-reading stage sections. Adding `Addressing F-IDs` completes the
bidirectional chain: C-27 makes findings cite D-IDs (forward); the new column makes D-ID
rows cite addressing findings (backward). A RESOLVED status without at least one F-ID is an
assertion; an F-ID citation is evidence.

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
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status |
|-------|------|------------------------------|-------------------|
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element -- e.g. "Stage3-F01, Stage5-F02". When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
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

---

## V-04 -- Blocker Resolution Traceability + Cross-Cutting Theme Finding Chain (V-01 + V-02)

**Axes**: Resolution Evidence column in Blocker Resolution Status (V-01) +
Primary F-IDs column in Cross-Cutting Themes (V-02).
**Hypothesis**: The two highest-use ROB Summary tables are the Blocker Resolution Status
(which closes the inter-stage blocker audit loop) and the Cross-Cutting Themes (which
elevates recurrent concerns to program-level risks). Both currently express conclusions
without primary-evidence citations. V-01 targets RESOLVED labels; V-02 targets theme
synthesis. Together they extend the column-level citation obligation established by C-27
for finding rows to the two ROB Summary synthesis tables that carry the most structural
weight in disposition decisions. If V-01 and V-02 each independently generate observable
output quality markers, their combination should produce the highest density of those
markers among the first three single-axis variations.

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
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] |
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

## V-05 -- Full Synthesis-Table Audit Closure (V-01 + V-02 + V-03)

**Axes**: Resolution Evidence in Blocker Resolution Status (V-01) +
Primary F-IDs in Cross-Cutting Themes (V-02) +
Addressing F-IDs in Inertia Resolution Status (V-03).
**Hypothesis**: The three R8 axes each target the same structural gap on a different ROB
Summary synthesis table: conclusions expressed as status labels (RESOLVED/OPEN) or
synthesized assertions (theme descriptions) without naming the primary-evidence F-ID that
produced the conclusion. The pattern is identical to the one that C-27/C-28 closed for
finding rows -- where inertia citation was previously a prose constraint and became a
per-row column obligation. Extending the column-level citation obligation to all three ROB
Summary synthesis tables closes the evidence gap at the summary level the way C-27 closed
it at the finding level. V-05's combined architecture makes every conclusion in the ROB
Summary auditable from a specific F-ID without re-reading stage sections. The architecture
observation is: the C-27 pattern should apply uniformly to all structured tables where the
evidence-to-conclusion hop is currently prose-dependent. The three axes together represent
a complete instantiation of this principle across the summary layer.

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
