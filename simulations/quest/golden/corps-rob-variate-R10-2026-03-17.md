---
skill: quest-variate
skill_target: corps-rob
round: 10
date: 2026-03-17
rubric_version: 9
---

# Variate R10 -- corps-rob (rubric v9, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v9.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R9 ceiling under v9:** V-05 R9 (all three operational-table citation axes) achieves the ceiling:
27 raw / 10 contributable / composite 100 (tie-break 27). All three v9 criteria (C-33, C-34, C-35)
pass. No variation from R9 can exceed this score under v9.

The R10 question: after citation completeness reaches every structured table in the ROB output,
which prose slots and structural boundaries remain ungrounded, and can typed structural obligations
be extended to those positions without regression?

**V-05 R9 baseline audit -- what is NOT yet structurally obligated:**

After v9, every structured table in the ROB output carries a typed citation column where conclusions
are recorded. But four positions remain where content is produced without a structural obligation
that forces explicit enumeration or grounding:

1. **Phase boundary between Stage 3 and Stage 4**: The ROB transitions from business review
   (leadership, teams, pm) to technical and executive review (tpm, arch-board, exec-office) without
   any explicit synthesis gate. The BLOCKER PROPAGATION RULE carries individual blockers forward
   one stage at a time, but no structure forces a consolidated business-readiness checkpoint before
   the technical phases begin. A TPM who runs Stage 4 without knowing that Stage 3 had two open
   HIGH findings and a CONDITIONAL gate is reviewing against an incomplete picture. Hypothesis:
   adding an explicit PHASE GATE section between Stage 3 and Stage 4 -- with a typed finding count,
   open HIGH F-ID list, and a labeled gate decision that must propagate into Stage 4's PRIOR-STAGE
   ESCALATIONS -- converts the implicit phase boundary into an auditable structural gate.

2. **Handoff Packet receipt at Part 1**: The BLOCKER PROPAGATION RULE requires receiving stages to
   acknowledge blockers by F-ID ("[BLOCKER: {F-ID} from {stage name}]"). But all other forwarded
   findings from the Handoff Packet -- the Cross-Stage References Forwarded table, the Downstream
   Risk Shift -- are received silently. The receiving stage's KEY CONCERNS may reflect them, but
   no typed field enumerates what was actually received. Hypothesis: adding a `Receipt Declaration`
   field to Part 1 BRIEFING ENVELOPE that requires naming the specific forwarded F-IDs received
   from the prior stage's Handoff Packet -- not a prose summary, but an enumerated list -- closes
   the sender/receiver asymmetry and converts silent receipt into explicit acknowledgment.

3. **Resistance accumulation across stages**: The ROB Summary's Inertia Resolution Status table
   tracks whether each Displacement Map entry was resolved, but no ROB Summary table shows how
   resistance evolved across stages as a running signal. Six stages each declare RESISTANT / NEUTRAL
   / ALIGNED, but the overall trajectory (growing resistance, declining resistance, stable
   resistance) is invisible at the summary level. Hypothesis: adding a RESISTANCE TRAJECTORY table
   to the ROB Summary -- with one row per stage, a typed Resistance Delta (+1/-1/0), a mandatory
   Grounding F-ID for non-zero deltas, and a Cumulative Score column -- converts the per-stage
   inertia stances from scattered labels into a finding-grounded accumulation that makes the
   adoption-risk trajectory auditable.

4. (Reserved for V-04/V-05 structural interaction -- see combination variations below.)

All five R10 variations preserve the complete V-05 R9 architecture:
- VERDICT CALIBRATION table at Stage Template header (C-05)
- BLOCKER PROPAGATION RULE with [BLOCKER: F-ID from stage] token (C-09, C-12)
- D-ID Ref column in Findings table (C-27 PASS)
- D-ID Ref column guard with named anti-pattern rejection (C-28 PASS)
- Scope-exception calibration naming GO/NO-GO as exempt (C-29 PASS)
- Fill-slot declarative [fill] slots everywhere (C-24)
- INERTIA ANCHOR with labeled Displacement Map D-IDs (C-25)
- Table-first findings with inline rejection guards (C-26)
- Part 0 LENS ACTIVATION pre-envelope block (C-20)
- KEY CONCERNS back-ref to Part 0 (C-21)
- Prior-Stage Lens Impact with "orientation declared in Part 0" phrase (C-22)
- LENS ACTIVATION CHAIN HEALTH summary table with Remediation Action column (C-23, C-35)
- Resolution Evidence column in Blocker Resolution Status (C-30)
- Primary F-IDs column in Cross-Cutting Themes (C-31)
- Addressing F-IDs column in Inertia Resolution Status (C-32)
- Source F-IDs column in Risk Register (C-33)
- Supporting F-IDs column in Mission Cascade (C-34)

Dropping any of these would reduce raw aspirational count. They are non-negotiable at R10.

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle Emphasis: Phase Gate between Stage 3 and Stage 4 | The implicit business-review / technical-review boundary is unguarded; a typed PHASE GATE section with finding count, open HIGH F-IDs, and a propagating gate decision converts the boundary into an auditable gate |
| V-02 | Role Sequence: Receipt Declaration in Part 1 BRIEFING ENVELOPE | Forwarded Handoff Packet findings are received silently by all stages except blockers; a typed Receipt Declaration field that enumerates received F-IDs closes the sender/receiver asymmetry |
| V-03 | Inertia Framing: Resistance Trajectory table in ROB Summary | Per-stage inertia stances are scattered labels with no accumulation; a typed RESISTANCE TRAJECTORY table with delta, grounding F-ID, and cumulative score converts stance sequence into an auditable adoption-risk signal |
| V-04 | V-01 + V-02 (Phase Gate + Receipt Declaration) | The phase boundary gate and the handoff receipt obligation address adjacent structural gaps in the stage handoff chain; combining them closes both the inter-phase gate and the intra-phase receipt gap |
| V-05 | V-01 + V-02 + V-03 (full structural closure) | Phase Gate closes the phase-boundary gap; Receipt Declaration closes the handoff receipt gap; Resistance Trajectory closes the accumulation gap; together they address all three unguarded structural positions identified in the R10 audit |

---

## V-01 -- Phase Gate

**Axis**: Add a `PHASE GATE` section between Stage 3 (pm) and Stage 4 (tpm).
**Hypothesis**: The ROB moves from business review (stages 1-3: leadership, teams, pm) to
technical and executive review (stages 4-6: tpm, arch-board, exec-office) without any
explicit synthesis point. The BLOCKER PROPAGATION RULE propagates individual blockers one
stage at a time, but no structure forces a consolidated readiness assessment before the
technical phases begin. A TPM running Stage 4 with two open HIGH findings from Stage 2 and
a PM cross-alignment gap from Stage 3 has no structural signal that the business review
concluded in a FAIL or CONDITIONAL state.

The analogy is the VERDICT CALIBRATION table: before C-05, each stage produced a verdict as
an editorial judgment. The calibration table converted verdicts from assertions into
derivable conclusions by naming the conditions. At the phase-boundary level, the Stage 3 to
Stage 4 transition is currently an editorial handoff -- no structure names the business-review
finding profile, no typed decision gate is issued, no label propagates into Stage 4. The
PHASE GATE section adds all three: a typed finding count by severity, an open HIGH F-IDs
field, and a Gate Decision (PASS / FAIL / CONDITIONAL) with definitions. If Gate Decision is
FAIL or CONDITIONAL, Stage 4's Part 1 PRIOR-STAGE ESCALATIONS must begin with
"[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence of this label when Gate Decision is FAIL
or CONDITIONAL is a format failure.

Anti-pattern rejections for Phase A Finding Count: "Several HIGH findings" does not satisfy
this field. "Multiple concerns raised" does not satisfy this field. Anti-pattern rejections
for Open HIGH Findings: "See prior stages" does not satisfy this field. "Various HIGH items"
does not satisfy this field. A FAIL or CONDITIONAL gate with no Open HIGH F-IDs named is a
format failure.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .craft/roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               [PHASE GATE] -> Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

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

**PHASE GATE PROPAGATION RULE**: If the PHASE GATE decision is FAIL or CONDITIONAL, then
Stage 4's Part 1 PRIOR-STAGE ESCALATIONS cell MUST include "[PHASE-GATE: {Gate Decision} --
{F-ID}]" as its first entry (before any BLOCKER labels if both apply). Absence of this
label when Phase Gate Decision is FAIL or CONDITIONAL is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .craft/roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets. At Stage 4 only: if PHASE GATE Decision is FAIL or CONDITIONAL, this cell MUST begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If the immediately prior stage had BLOCKER=YES, this cell MUST begin with "[BLOCKER: {F-ID} from {stage name}]" (after any PHASE-GATE label). NONE only if no escalations AND no prior-stage blockers AND no FAIL/CONDITIONAL phase gate.] |

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

## PHASE GATE -- After Stage 3 (pm), Before Stage 4 (tpm)

Fill after Stage 3 completes, before Stage 4 begins. Every slot must be populated.
This section is required when --stage all is used. When --stage {name} runs a single stage,
fill PHASE GATE if the stage is pm (concluding Phase A) or tpm or later (carry forward).

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: explicit count by severity -- "HIGH: N, MED: N, LOW: N" -- counted across all Stage 1-3 findings. "Several HIGH findings" does not satisfy this field. "Multiple concerns raised" does not satisfy this field. A count without three explicit severity bands is a format failure.] |
| Open HIGH Findings | [fill: comma-separated F-IDs of HIGH findings from Stages 1-3 that have no owner or no resolution path at the time of this gate. NONE if all HIGH findings have been assigned an owner and a concrete resolution. "See prior stages" does not satisfy this field. "Various HIGH items" does not satisfy this field. A FAIL or CONDITIONAL gate with no F-IDs named is a format failure.] |
| Gate Decision | [fill: PASS / FAIL / CONDITIONAL] |
| Gate Rationale | [fill: one sentence naming the dominant condition. Cite at least one F-ID if Gate Decision is FAIL or CONDITIONAL. "Phase A had issues" does not satisfy this field. "Concerns noted" does not satisfy this field.] |

Gate Decision definitions:
- FAIL: at least one Stage 1-3 HIGH finding has no owner assigned OR no resolution path stated.
- CONDITIONAL: all HIGH findings have owners and resolution paths, but at least one resolution
  is not yet verified or depends on an action outside Stage 1-3 scope.
- PASS: no HIGH findings raised in Stages 1-3, OR all HIGH findings fully resolved with
  owner and concrete resolution confirmed.

If Gate Decision is FAIL or CONDITIONAL, Stage 4's Part 1 PRIOR-STAGE ESCALATIONS MUST
begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence of this label when Gate
Decision is FAIL or CONDITIONAL is a format failure.

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

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill: PASS / FAIL / CONDITIONAL] | [fill: F-IDs from PHASE GATE, or NONE] | [fill: YES / NO / N/A (if Gate Decision is PASS)] | [fill: RESOLVED / OPEN -- if FAIL or CONDITIONAL, name the stage action or F-ID that confirmed resolution; if PASS, N/A] |
(One row. Required when --stage all is used.)

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
| [fill: actual mission title] | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- comma-separated F-IDs from any stage that established this verdict. At least one F-ID per PARTIAL or GAP row is required. "Based on general review" does not satisfy this column. "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows: N/A is acceptable when alignment is affirmed by the absence of contrary findings.] |
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
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, PHASE GATE, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Fill PHASE GATE if stage is pm or later. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION context, PHASE GATE decision, all prior handoff packets, and any unresolved BLOCKER items forward.

---

## V-02 -- Handoff Receipt Declaration

**Axis**: Add a `Receipt Declaration` field to Part 1 BRIEFING ENVELOPE (Stages 2-6).
**Hypothesis**: The BLOCKER PROPAGATION RULE requires receiving stages to acknowledge blockers
by F-ID ("[BLOCKER: {F-ID} from {stage name}]"). But all other forwarded findings from the
Handoff Packet -- the Cross-Stage References Forwarded table, the Downstream Risk Shift slot
-- are received silently. The receiving stage's KEY CONCERNS may reflect them, but no typed
field forces the receiving stage to enumerate what was actually forwarded.

The sender/receiver asymmetry is structural: the Handoff Packet has a typed F-ID table
(Cross-Stage References Forwarded) with enumerated forwarded items, but the receiving stage
has no obligation to acknowledge receipt of those items by F-ID. KEY CONCERNS is role-filtered
and selective by design -- it is not a receipt acknowledgment. The stage could ignore forwarded
findings entirely and KEY CONCERNS would still satisfy C-21 if it cited the prior-stage context
through the Part 0 lens.

Receipt Declaration adds a typed field to Part 1 that requires naming the specific forwarded
F-IDs received from the prior stage's Handoff Packet Cross-Stage References Forwarded table.
Anti-pattern rejections: "Reviewed prior stage handoff" does not satisfy this field. "See
forwarded references" does not satisfy this field. "Handoff reviewed" does not satisfy this
field. A Receipt Declaration that does not name at least one specific forwarded F-ID from
the prior stage's Handoff Packet is a format failure. If the prior stage's Handoff Packet
has no Cross-Stage References Forwarded rows (empty table), the Receipt Declaration must
explicitly state "No F-IDs forwarded by {prior stage name}" -- a blank or generic cell is
still a format failure when this condition applies.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .craft/roles/<role-file>.md for each assigned persona.
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
| Role | [fill: name -- title from .craft/roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets. If the immediately prior stage had BLOCKER=YES, this cell MUST begin with "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers.] |
| Receipt Declaration | [fill: enumerate the specific F-IDs received from the prior stage's Handoff Packet Cross-Stage References Forwarded table -- e.g. "Received: Stage2-F01 (escalates), Stage2-F03 (confirms)". If the prior stage's Handoff Packet forwarded no F-IDs, state "No F-IDs forwarded by {prior stage name}". "Reviewed prior stage handoff" does not satisfy this field. "See forwarded references" does not satisfy this field. "Handoff reviewed" does not satisfy this field. A Receipt Declaration that does not name at least one specific forwarded F-ID or explicitly declare no forwarded F-IDs is a format failure.] |

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
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element. When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage. At least one F-ID per named stage is required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: comma-separated F-IDs from stage sections that grounded this risk. At least one F-ID per risk row is required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title] | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- at least one F-ID required. "Based on general review" does not satisfy this column. "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows: N/A acceptable when alignment is affirmed by absence of contrary findings.] |
(Minimum 1 row. All four columns must be populated.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A. "Chain incomplete" does not satisfy this column. "Needs review" does not satisfy this column.] |
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

## V-03 -- Resistance Trajectory

**Axis**: Add a `RESISTANCE TRAJECTORY` table to ROB Summary.
**Hypothesis**: Six stages each declare an Inertia Stance (RESISTANT / NEUTRAL / ALIGNED) in
their Inertia Check section. The Inertia Resolution Status table in ROB Summary tracks whether
each Displacement Map entry was resolved. But no ROB Summary table shows how resistance
evolved across the stages as a running signal.

Three distinct trajectories are structurally invisible under v9: (1) resistance that starts
HIGH and declines as stages address displacement elements; (2) resistance that starts NEUTRAL
and escalates as technical stages reveal integration costs; (3) resistance that is stable
throughout but concentrated in a single high-leverage displacement. All three produce the
same Inertia Resolution Status entries -- the trajectory information is lost.

The RESISTANCE TRAJECTORY table adds one row per stage with a typed Resistance Delta (+1 for
RESISTANT, 0 for NEUTRAL, -1 for ALIGNED), a mandatory Grounding F-ID for non-zero deltas,
and a Cumulative Score column that accumulates the running total. This converts the per-stage
inertia stances from scattered labels into a finding-grounded trajectory that makes
adoption-risk evolution auditable at the summary level.

Anti-pattern rejections for the Grounding F-ID column: "RESISTANT due to change fatigue" does
not satisfy this column. "Stage stance noted" does not satisfy this column. "General resistance"
does not satisfy this column. A RESISTANT (+1) or ALIGNED (-1) row without a specific F-ID
that grounded the stance determination is a format failure. NEUTRAL (0) rows use N/A for
Grounding F-ID -- a NEUTRAL row with an F-ID does not satisfy the anti-pattern guard (the
stance requires no grounding cite when no directional signal is present).

The final Cumulative Score row must sum the column. A positive total indicates net resistance
accumulation across the ROB; a negative total indicates net alignment gain; zero indicates
balanced or null inertia. The ROB Summary Rationale must reference the Cumulative Score when
it characterizes adoption risk.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .craft/roles/<role-file>.md for each assigned persona.
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
| Role | [fill: name -- title from .craft/roles/] |
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
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill -- reason the downstream stage cannot proceed without resolution.] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance of the forwarded cross-stage picture.
Must add substance not already visible in the table above.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.]

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table
    or name the dominant cross-stage condition that drove the overall verdict]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern. Must reference the
    Resistance Trajectory Cumulative Score when characterizing adoption risk.]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action; if OPEN -- name owner stage and pending action. "Discussed" does not satisfy this column. "See findings" does not satisfy this column.] |
(Include 1 row per BLOCKER=YES raised. Empty if no blockers raised.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill] | [fill: comma-separated F-IDs. When Status is RESOLVED, at least one F-ID citing MED or HIGH finding required. "General resistance noted" does not satisfy this column. An empty cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: at least one F-ID per named stage required. "Multiple findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: at least one F-ID per risk row required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title] | [fill] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- at least one F-ID required. "Based on general review" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows: N/A acceptable.] |
(Minimum 1 row. All four columns must be populated.)

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill: RESISTANT / NEUTRAL / ALIGNED] | [fill: +1 / 0 / -1 -- RESISTANT=+1, NEUTRAL=0, ALIGNED=-1] | [fill: if Delta is +1 or -1 -- the specific F-ID from this stage's Inertia Check or Findings that grounded the stance determination, e.g. "Stage1-F02". If Delta is 0 (NEUTRAL) -- N/A. "RESISTANT due to change fatigue" does not satisfy this column. "Stage stance noted" does not satisfy this column. "General resistance" does not satisfy this column. A +1 or -1 row without a specific F-ID is a format failure. A 0 row with any value other than N/A is a format failure.] | [fill: running total -- Stage 1 only: equals Delta value] |
| Stage 2 (teams)      | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 3 (pm)         | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 4 (tpm)        | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 5 (arch-board) | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 6 (exec-office)| [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| **TOTAL**            | --     | [fill: sum of column] | -- | [fill: final cumulative score -- must equal Stage 6 Cumulative Score] |

Cumulative Score interpretation (informational -- not a gate):
- Positive: net resistance accumulation; adoption-risk rationale must name the dominant RESISTANT stage.
- Negative: net alignment gain; rationale may note which stage produced the largest alignment signal.
- Zero: balanced or null inertia; rationale should note whether this reflects genuine balance or absence of signal.

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary including RESISTANCE TRAJECTORY.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION context, all prior handoff packets, and any unresolved BLOCKER items forward. Recompute RESISTANCE TRAJECTORY from scratch using updated stances.

---

## V-04 -- Phase Gate + Handoff Receipt Declaration (V-01 + V-02)

**Axes**: PHASE GATE between Stage 3 and Stage 4 (V-01) +
Receipt Declaration in Part 1 BRIEFING ENVELOPE (V-02).
**Hypothesis**: V-01 and V-02 address adjacent structural gaps in the same handoff chain.
V-01 closes the inter-phase gap: the transition from business review to technical and
executive review has no structural gate. V-02 closes the intra-stage gap: each receiving
stage has no typed acknowledgment of what was forwarded to it by the prior stage's Handoff
Packet.

Together they create a two-level receipt architecture. The PHASE GATE is a synthesized
inter-phase receipt: before Stage 4 runs, the ROB produces a consolidated statement of what
Phase A left unresolved, at what severity, and with what gate decision. The Receipt
Declaration is a per-stage intra-phase receipt: before each stage runs, Part 1 enumerates
the specific forwarded F-IDs received from the immediately prior stage. Together they close
the sender/receiver accountability gap at both levels: high (phase-to-phase) and low
(stage-to-stage).

The structural interaction between V-01 and V-02: when the PHASE GATE Decision is FAIL or
CONDITIONAL, Stage 4's Part 1 must contain both a "[PHASE-GATE: {Gate Decision} -- {F-ID}]"
label in PRIOR-STAGE ESCALATIONS and a Receipt Declaration that enumerates the forwarded
F-IDs from Stage 3's Handoff Packet. These are two independent obligations -- a stage could
satisfy the PHASE-GATE label without enumerating Receipt Declaration F-IDs, or vice versa.
Both must be present when applicable.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .craft/roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               [PHASE GATE] -> Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

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

**PHASE GATE PROPAGATION RULE**: If the PHASE GATE decision is FAIL or CONDITIONAL, then
Stage 4's Part 1 PRIOR-STAGE ESCALATIONS cell MUST include "[PHASE-GATE: {Gate Decision} --
{F-ID}]" as its first entry (before any BLOCKER labels if both apply). Absence of this
label when Phase Gate Decision is FAIL or CONDITIONAL is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .craft/roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: escalated items from prior handoff packets. At Stage 4: if PHASE GATE Decision is FAIL or CONDITIONAL, this cell MUST begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If immediately prior stage had BLOCKER=YES, include "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers AND no FAIL/CONDITIONAL gate.] |
| Receipt Declaration | [fill: enumerate the specific F-IDs received from the prior stage's Handoff Packet Cross-Stage References Forwarded table -- e.g. "Received: Stage2-F01 (escalates), Stage2-F03 (confirms)". If the prior stage forwarded no F-IDs, state "No F-IDs forwarded by {prior stage name}". "Reviewed prior stage handoff" does not satisfy this field. "See forwarded references" does not satisfy this field. A Receipt Declaration that does not name at least one specific forwarded F-ID or explicitly declare no forwarded F-IDs is a format failure.] |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} if Inertia Stance RESISTANT and Severity HIGH; otherwise N/A] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Minimum 2 rows. All six columns must be populated.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict

  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table]
  Rationale: [fill: cite at least one F-ID and name the finding that drove the verdict. One sentence.]

  tpm stage only:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance. Must add substance not in the table above.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.]

---

## PHASE GATE -- After Stage 3 (pm), Before Stage 4 (tpm)

Fill after Stage 3 completes, before Stage 4 begins.

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: explicit count -- "HIGH: N, MED: N, LOW: N" across all Stage 1-3 findings. "Several HIGH findings" does not satisfy this field. A count without three severity bands is a format failure.] |
| Open HIGH Findings | [fill: comma-separated F-IDs of HIGH findings from Stages 1-3 with no owner or no resolution path. NONE if all HIGH findings assigned. "See prior stages" does not satisfy this field. A FAIL or CONDITIONAL gate with no F-IDs named is a format failure.] |
| Gate Decision | [fill: PASS / FAIL / CONDITIONAL] |
| Gate Rationale | [fill: cite at least one F-ID if FAIL or CONDITIONAL. "Phase A had issues" does not satisfy this field.] |

Gate Decision definitions:
- FAIL: at least one Stage 1-3 HIGH finding has no owner assigned OR no resolution path stated.
- CONDITIONAL: all HIGH findings have owners and paths, but at least one resolution is unverified.
- PASS: no HIGH findings in Stages 1-3, OR all fully resolved.

If Gate Decision is FAIL or CONDITIONAL, Stage 4's PRIOR-STAGE ESCALATIONS MUST begin with
"[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence of this label is a format failure.

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row or name dominant cross-stage condition]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- name downstream F-ID or stage action; if OPEN -- name owner and pending action. "Discussed" does not satisfy. "See findings" does not satisfy.] |
(1 row per BLOCKER=YES. Empty if none.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill: PASS / FAIL / CONDITIONAL] | [fill: F-IDs or NONE] | [fill: YES / NO / N/A if PASS] | [fill: RESOLVED / OPEN / N/A] |
(One row. Required when --stage all.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill] | [fill] | [fill: F-IDs required when RESOLVED. "General resistance noted" does not satisfy. Empty when RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill] | [fill] | [fill] | [fill] |

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: at least one F-ID per named stage. "Multiple findings" does not satisfy. "See findings" does not satisfy.] | [fill] |
(Minimum 1 row if any concern in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill] | HIGH/MED/LOW | HIGH/MED/LOW | [fill] | [fill: at least one F-ID per row. "Inferred from ROB" does not satisfy. "General concerns" does not satisfy.] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------|------------------|---------|------------------|
| [fill] | [fill] | ALIGNED / PARTIAL / GAP | [fill: at least one F-ID per PARTIAL/GAP row. "Based on general review" does not satisfy. ALIGNED rows: N/A acceptable.] |
(Minimum 1 row. All four columns populated.)

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A | N/A | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages, PHASE GATE, ROB Summary.
--stage {name}: fill INERTIA ANCHOR regardless. Fill PHASE GATE if stage is pm or later.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION, PHASE GATE, all prior handoff packets, and unresolved BLOCKER items forward.

---

## V-05 -- Phase Gate + Handoff Receipt Declaration + Resistance Trajectory (V-01 + V-02 + V-03)

**Axes**: PHASE GATE (V-01) + Receipt Declaration (V-02) + RESISTANCE TRAJECTORY (V-03).
**Hypothesis**: V-01 closes the inter-phase boundary gap; V-02 closes the per-stage handoff
receipt gap; V-03 closes the resistance accumulation gap. The three axes are independent --
each addresses a different structural position (the Stage 3 / Stage 4 boundary, the Part 1
field set, the ROB Summary table set). None of the three regresses any v9 criterion.

The structural interaction across all three: the PHASE GATE (V-01) feeds Stage 4's
PRIOR-STAGE ESCALATIONS with a typed gate label; the Receipt Declaration (V-02) at Stage 4
must enumerate the forwarded F-IDs from Stage 3's Handoff Packet independently of the gate
label; the RESISTANCE TRAJECTORY (V-03) accumulates the inertia signal from all six stages
including Stage 4 and later. When Stage 4 inherits a PHASE-GATE FAIL, the TPM Inertia Stance
is more likely RESISTANT (reflecting the inherited Phase A concerns), which would contribute
+1 to the trajectory -- making the Phase Gate outcome visible in the adoption-risk table.
This is not a structural requirement, but a natural consequence of the three axes operating
in combination.

V-05 makes the R10 hypothesis testable in a single prompt: if all three structural obligations
are satisfied -- phase gate produces a typed decision, every stage enumerates its receipt of
forwarded findings, and the resistance trajectory accumulates into a finding-grounded score --
then the ROB output is structurally complete at every level: table citation (v8), operational
table citation (v9), phase-boundary gate (R10 V-01), per-stage receipt enumeration (R10 V-02),
and resistance accumulation (R10 V-03).

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .craft/roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE: Stage 1: leadership -> Stage 2: teams -> Stage 3: pm ->
               [PHASE GATE] -> Stage 4: tpm -> Stage 5: arch-board -> Stage 6: exec-office

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

**PHASE GATE PROPAGATION RULE**: If the PHASE GATE decision is FAIL or CONDITIONAL, then
Stage 4's Part 1 PRIOR-STAGE ESCALATIONS cell MUST include "[PHASE-GATE: {Gate Decision} --
{F-ID}]" as its first entry (before any BLOCKER labels). Absence when Gate Decision is FAIL
or CONDITIONAL is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .craft/roles/] |
| Dimension | [fill: orientation in practice-domain terms. Name the lens dimension, not just the role title. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell. Role-filtered selection -- not verbatim copy of prior findings.] |
| PRIOR-STAGE ESCALATIONS | [fill: At Stage 4 only: if PHASE GATE Decision is FAIL or CONDITIONAL, begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If immediately prior stage had BLOCKER=YES, include "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers AND no FAIL/CONDITIONAL gate.] |
| Receipt Declaration | [fill: enumerate the specific F-IDs received from the prior stage's Handoff Packet Cross-Stage References Forwarded table -- e.g. "Received: Stage3-F01 (escalates), Stage3-F02 (confirms)". If the prior stage forwarded no F-IDs, state "No F-IDs forwarded by {prior stage name}". "Reviewed prior stage handoff" does not satisfy this field. "See forwarded references" does not satisfy this field. A Receipt Declaration that does not name at least one specific forwarded F-ID or explicitly declare no forwarded F-IDs is a format failure.] |

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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} if Inertia Stance RESISTANT and Severity HIGH; otherwise N/A] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Minimum 2 rows. All six columns must be populated.)

Constraint: At least 1 row per stage must be grounded in the Part 0 Dimension.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill] |

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: explicit text naming "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict

  Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row from the VERDICT CALIBRATION table]
  Rationale: [fill: cite at least one F-ID and name the finding that drove the verdict. One sentence.]

  tpm stage only:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk register row. One sentence.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [fill: YES/NO] | [if YES: fill] | [if YES: fill] | [if YES: fill] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance. Must add substance not in the table above.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.]

---

## PHASE GATE -- After Stage 3 (pm), Before Stage 4 (tpm)

Fill after Stage 3 completes, before Stage 4 begins.

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: explicit count -- "HIGH: N, MED: N, LOW: N" across Stages 1-3. "Several HIGH findings" does not satisfy this field. A count without three severity bands is a format failure.] |
| Open HIGH Findings | [fill: comma-separated F-IDs of HIGH findings from Stages 1-3 with no owner or no resolution path. NONE if all assigned. "See prior stages" does not satisfy. A FAIL or CONDITIONAL gate without F-IDs named is a format failure.] |
| Gate Decision | [fill: PASS / FAIL / CONDITIONAL] |
| Gate Rationale | [fill: cite at least one F-ID if FAIL or CONDITIONAL. "Phase A had issues" does not satisfy.] |

Gate Decision definitions:
- FAIL: at least one Stage 1-3 HIGH finding has no owner assigned OR no resolution path stated.
- CONDITIONAL: all HIGH findings have owners and paths, but at least one resolution is unverified.
- PASS: no HIGH findings in Stages 1-3, OR all fully resolved.

If Gate Decision is FAIL or CONDITIONAL, Stage 4's PRIOR-STAGE ESCALATIONS MUST begin with
"[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence is a format failure.

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote the matching row or name dominant cross-stage condition]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern. Must reference the
    Resistance Trajectory Cumulative Score when characterizing adoption risk.]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- downstream F-ID or stage action; if OPEN -- owner stage and pending action. "Discussed" does not satisfy. "See findings" does not satisfy.] |
(1 row per BLOCKER=YES. Empty if none.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill: PASS / FAIL / CONDITIONAL] | [fill: F-IDs or NONE] | [fill: YES / NO / N/A if PASS] | [fill: RESOLVED / OPEN / N/A] |
(One row. Required when --stage all.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill] | [fill] | [fill: F-IDs required when RESOLVED. "General resistance noted" does not satisfy. Empty when RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill] | [fill] | [fill] | [fill] |

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: at least one F-ID per named stage. "Multiple findings" does not satisfy. "See findings" does not satisfy.] | [fill] |
(Minimum 1 row if any concern in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill] | HIGH/MED/LOW | HIGH/MED/LOW | [fill] | [fill: at least one F-ID per row. "Inferred from ROB" does not satisfy. "General concerns" does not satisfy.] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------|------------------|---------|------------------|
| [fill] | [fill] | ALIGNED / PARTIAL / GAP | [fill: at least one F-ID per PARTIAL/GAP row. "Based on general review" does not satisfy. ALIGNED rows: N/A acceptable.] |
(Minimum 1 row. All four columns populated.)

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill: RESISTANT/NEUTRAL/ALIGNED] | [fill: +1/0/-1] | [fill: specific F-ID from this stage if +1 or -1; N/A if 0. "RESISTANT due to change fatigue" does not satisfy. "Stage stance noted" does not satisfy. "General resistance" does not satisfy. A +1 or -1 row without specific F-ID is a format failure. A 0 row with any value other than N/A is a format failure.] | [fill: running total] |
| Stage 2 (teams)      | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 3 (pm)         | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 4 (tpm)        | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 5 (arch-board) | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| Stage 6 (exec-office)| [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill: running total] |
| **TOTAL**            | --     | [fill: sum] | -- | [fill: final score -- must equal Stage 6 value] |

Cumulative Score interpretation:
- Positive: net resistance; Rationale must name the dominant RESISTANT stage.
- Negative: net alignment gain; Rationale may note the largest alignment signal.
- Zero: balanced or null inertia; Rationale should note whether this reflects genuine balance.

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A | N/A | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A. "Chain incomplete" does not satisfy. "Needs review" does not satisfy.] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific + corrective; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages, PHASE GATE, ROB Summary including RESISTANCE TRAJECTORY and Phase Gate Resolution Status.
--stage {name}: fill INERTIA ANCHOR regardless. Fill PHASE GATE if stage is pm or later. Omit Part 1 if first stage.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION, PHASE GATE, all prior handoff packets, and any unresolved BLOCKER items forward. Recompute RESISTANCE TRAJECTORY from scratch using updated stances.
