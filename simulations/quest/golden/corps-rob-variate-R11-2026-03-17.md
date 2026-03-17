---
skill: quest-variate
skill_target: corps-rob
round: 11
date: 2026-03-17
rubric_version: 9
---

# Variate R11 -- corps-rob (rubric v9, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v9.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R10 ceiling under v9:** V-05 R10 (Phase Gate + Receipt Declaration + Resistance Trajectory)
achieves the ceiling: 27 raw / 10 contributable / composite 100 (tie-break 27). All three v9
criteria (C-33, C-34, C-35) pass; all three R10 structural additions are present. No variation
from R10 can exceed this score under v9.

The R11 question: after the phase-boundary gate (R10 V-01), per-stage receipt enumeration
(R10 V-02), and resistance accumulation (R10 V-03) close the structural gaps at the boundary
and summary levels, which prose slots and derivation steps in the stage output remain without
a typed citation or grounding obligation?

**V-05 R10 baseline audit -- what is NOT yet structurally obligated:**

After R10, every structured table in the ROB output carries typed citation or action columns.
Every stage-to-stage handoff has a receipt declaration. Every phase boundary has a gate
decision. Every inertia stance contributes to an accumulated score. Three positions remain
where conclusions are generated without a typed grounding obligation:

1. **Handoff Packet Cross-Stage Synthesis prose**: Each stage's Handoff Packet contains a
   Cross-Stage Synthesis slot that must "add substance not already visible in the table above."
   The Cross-Stage References Forwarded table above it has specific F-IDs with typed
   relationships. But the synthesis prose slot requires no citation of those F-IDs -- a
   synthesis that characterizes a multi-finding pattern without naming any F-ID satisfies the
   slot. The structural obligation ends at the prose boundary: once in a prose slot, no
   mechanism forces the model to ground the characterization in a specific forwarded F-ID.
   The Cross-Stage References Forwarded table is a typed sender artifact; the synthesis is
   an editorial commentary on it with no citation requirement. Hypothesis: adding a `Synthesis
   F-IDs` typed field immediately below the Cross-Stage Synthesis prose -- requiring at least
   two specific F-IDs from the Cross-Stage References Forwarded table that the synthesis
   characterizes -- converts the prose synthesis from an asserted pattern into a
   finding-grounded characterization. The minimum of two F-IDs is not arbitrary: a
   single-finding synthesis is not a cross-stage pattern; cross-stage synthesis by definition
   requires characterizing at least two findings in relation to each other. A synthesis that
   names a pattern but cites only one F-ID does not satisfy the obligation.

2. **Handoff Packet Downstream Risk Shift prose**: Each stage's Handoff Packet contains a
   Downstream Risk Shift slot that must "name a failure mode or ownership gap newly visible
   from this stage's vantage point." This is the most consequential prose slot in the output:
   it is the mechanism by which a stage introduces net-new risk that no prior stage could have
   seen. But there is no typed obligation that grounds the risk identification in a specific
   F-ID from this stage's Findings or Cross-Stage References. A slot value of "The integration
   coupling identified here creates a deployment-sequencing risk invisible to prior reviewers"
   satisfies the structural requirement while naming no F-ID that established the coupling
   concern. The risk is asserted from stage vantage, not traced to a finding. Hypothesis:
   adding a `Risk Shift Source F-ID` typed field immediately below the Downstream Risk Shift
   prose -- requiring the specific F-ID from this stage's Findings or Cross-Stage References
   that established the failure mode or gap visibility -- converts the risk shift from a
   stage-asserted claim into a finding-grounded one. Unlike Synthesis F-IDs (which requires
   two because cross-stage synthesis is inherently multi-finding), Risk Shift Source F-ID
   requires exactly one: the net-new risk must have a single most-responsible finding that
   established the visibility. If multiple findings together established it, name the primary.

3. **ROB Summary Overall Verdict derivation**: The ROB Summary Overall Verdict has a
   Calibration Row Applied and a Rationale (1-2 sentences citing the dominant cross-stage
   pattern). The VERDICT CALIBRATION table ensures each individual stage verdict is derivable
   from the stage's finding profile. But the cross-stage aggregation step -- from six
   individual stage verdicts to an Overall Verdict -- is editorial. No typed structure maps
   individual stage verdicts to the Overall Verdict, names which stage's verdict drove it, or
   makes the derivation independently verifiable. The VERDICT CALIBRATION table is applied
   stage-by-stage; at the summary level, the Overall Verdict is re-derived from general
   impression rather than the worst-verdict-wins rule that is implicit in the calibration
   logic. Hypothesis: adding a `STAGE VERDICT AGGREGATE` table to the ROB Summary -- one row
   per stage with Stage, Stage Verdict, Governing F-ID (the F-ID cited in that stage's Verdict
   Rationale), and Propagation flag (YES if this stage's verdict drove the Overall Verdict) --
   converts the Overall Verdict from an editorial re-synthesis into a derivable conclusion.
   The Overall Verdict must equal the worst individual stage verdict in the table
   (BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED). Anti-pattern rejections for
   the Governing F-ID column prevent the table from being satisfied by summary-level claims.

All five R11 variations preserve the complete V-05 R10 architecture:
- PHASE GATE section between Stage 3 and Stage 4 (R10 V-01)
- PHASE GATE PROPAGATION RULE at Stage 4 (R10 V-01)
- Phase Gate Resolution Status in ROB Summary (R10 V-01)
- Receipt Declaration field in Part 1 BRIEFING ENVELOPE (R10 V-02)
- RESISTANCE TRAJECTORY table in ROB Summary (R10 V-03)
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

Dropping any of these would reduce raw aspirational count. They are non-negotiable at R11.

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | Handoff Packet grounding: Synthesis F-IDs field | Cross-Stage Synthesis prose characterizes forwarded patterns without naming the F-IDs it synthesizes; a typed Synthesis F-IDs field requiring ≥2 specific F-IDs converts the prose from an asserted characterization into a finding-grounded one |
| V-02 | Handoff Packet grounding: Risk Shift Source F-ID field | Downstream Risk Shift prose names net-new failure modes without grounding them in a specific finding; a typed Risk Shift Source F-ID field requiring exactly one F-ID from the stage's Findings or Cross-Stage References converts the risk shift from a stage-asserted claim into a finding-grounded one |
| V-03 | ROB Summary verdict derivation: Stage Verdict Aggregate table | The Overall Verdict is derived editorially from six stage verdicts; a typed STAGE VERDICT AGGREGATE table with one row per stage, a Governing F-ID per verdict, and a Propagation flag forces the Overall Verdict to equal the worst individual stage verdict and makes the derivation independently verifiable |
| V-04 | V-01 + V-02 (both Handoff Packet prose positions) | Synthesis F-IDs and Risk Shift Source F-ID address the two prose slots in the Handoff Packet that remain ungrounded after R10; combining them closes both prose positions in the same packet structure |
| V-05 | V-01 + V-02 + V-03 (full structural closure) | Synthesis F-IDs closes the synthesis prose grounding gap; Risk Shift Source F-ID closes the risk shift prose grounding gap; Stage Verdict Aggregate closes the Overall Verdict derivation gap; together they address all three unguarded positions identified in the R11 audit |

---

## V-01 -- Synthesis F-IDs in Handoff Packet

**Axis**: Add a `Synthesis F-IDs` typed field below the Cross-Stage Synthesis prose in the
Handoff Packet.
**Hypothesis**: The Cross-Stage Synthesis slot requires prose that "adds substance not already
visible in the table above." The Cross-Stage References Forwarded table above it contains
specific F-IDs with typed relationships. But the synthesis prose is unconstrained by citation
-- the model can characterize a multi-finding pattern without naming any specific forwarded
F-ID and still satisfy the slot. The structural gap is the prose-boundary problem: every
structured table in the ROB output has a typed citation column, but prose slots have no
equivalent mechanism. Adding a typed `Synthesis F-IDs` field immediately below the prose
slot -- requiring at least two specific F-IDs from the Forwarded table that the synthesis
characterizes -- closes the gap. The minimum of two is structural: a cross-stage synthesis
characterizes a pattern across multiple findings; a citation of one finding is a
single-finding observation, not a cross-stage synthesis. Anti-pattern rejections name the
failure modes: "See forwarded table" defers to the table rather than citing from it;
"Based on overall stage findings" generalizes away from specific F-IDs; an empty Synthesis
F-IDs field when the Forwarded table has 2+ rows is a format failure.

Anti-pattern rejections for `Synthesis F-IDs`:
- "See forwarded table" does not satisfy this field.
- "Based on overall stage findings" does not satisfy this field.
- "Forwarded findings reviewed" does not satisfy this field.
A Synthesis F-IDs field with fewer than two specific F-IDs when the Forwarded table contains
2+ rows is a format failure. When the Forwarded table contains exactly one row, one F-ID
satisfies the field -- the two-F-ID minimum applies only when two or more rows are forwarded.
When the Forwarded table is empty, the field must state "No F-IDs forwarded -- synthesis
deferred."

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
{F-ID}]" as its first entry (before any BLOCKER labels if both apply). Absence when Gate
Decision is FAIL or CONDITIONAL is a format failure.

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
| PRIOR-STAGE ESCALATIONS | [fill: At Stage 4 only: if PHASE GATE Decision is FAIL or CONDITIONAL, this cell MUST begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If immediately prior stage had BLOCKER=YES, include "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers AND no FAIL/CONDITIONAL gate.] |
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

**Synthesis F-IDs:** [fill: comma-separated list of at least two F-IDs from the Cross-Stage
References Forwarded table above that this synthesis characterizes -- e.g. "Stage2-F01,
Stage3-F02". When the Forwarded table has exactly one row, one F-ID satisfies this field.
When the Forwarded table is empty, state "No F-IDs forwarded -- synthesis deferred".
"See forwarded table" does not satisfy this field. "Based on overall stage findings" does not
satisfy this field. "Forwarded findings reviewed" does not satisfy this field. A Synthesis
F-IDs field with fewer than two F-IDs when 2+ rows are forwarded is a format failure.]

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
begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence of this label is a format failure.

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
| [fill: stage that raised blocker] | [fill: F-ID] | [fill: stage(s) that received [BLOCKER:] label] | RESOLVED / OPEN | [fill: if RESOLVED -- name the downstream F-ID or stage action that confirmed resolution; if OPEN -- name the owner stage and pending action required. "Discussed" does not satisfy this column. "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure.] |
(Include 1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill: PASS / FAIL / CONDITIONAL] | [fill: F-IDs or NONE] | [fill: YES / NO / N/A if Gate Decision is PASS] | [fill: RESOLVED / OPEN / N/A] |
(One row. Required when --stage all is used.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from the named stages that directly addressed this displacement element. When Status is RESOLVED, at least one F-ID citing a MED or HIGH finding that named this displacement must be present. "General resistance noted" does not satisfy this column. "See findings" does not satisfy this column. An empty Addressing F-IDs cell when Status is RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: comma-separated F-IDs from each named stage -- at least one F-ID per named stage required. "Multiple findings" does not satisfy this column. "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: comma-separated F-IDs from stage sections that grounded this risk. At least one F-ID per risk row is required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title] | [fill: specific trace from mission to artifact] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- at least one F-ID per PARTIAL or GAP row is required. "Based on general review" does not satisfy this column. "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows: N/A is acceptable when alignment is affirmed by the absence of contrary findings.] |
(Minimum 1 row. All four columns must be populated.)

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill: RESISTANT/NEUTRAL/ALIGNED] | [fill: +1/0/-1] | [fill: specific F-ID from this stage if Delta is +1 or -1; N/A if Delta is 0. "RESISTANT due to change fatigue" does not satisfy this column. "Stage stance noted" does not satisfy this column. "General resistance" does not satisfy this column. A +1 or -1 row without a specific F-ID is a format failure. A 0 row with any value other than N/A is a format failure.] | [fill: running total] |
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
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- name the specific missing element and the corrective action; if COMPLETE -- N/A. "Chain incomplete" does not satisfy this column. "Needs review" does not satisfy this column. A BROKEN or PARTIAL row without a remediation action naming the specific missing element is a format failure.] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, PHASE GATE, ROB Summary including RESISTANCE TRAJECTORY and Phase Gate Resolution Status.
--stage {name}: single stage. Fill INERTIA ANCHOR regardless. Fill PHASE GATE if stage is pm or later. Omit Part 1 if first stage. All tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION, PHASE GATE decision, all prior handoff packets, and any unresolved BLOCKER items forward. Recompute RESISTANCE TRAJECTORY from scratch using updated stances.

---

## V-02 -- Risk Shift Source F-ID in Handoff Packet

**Axis**: Add a `Risk Shift Source F-ID` typed field below the Downstream Risk Shift prose in
the Handoff Packet.
**Hypothesis**: The Downstream Risk Shift slot names net-new failure modes or ownership gaps
visible only from this stage's vantage point. It is the most consequential prose slot in the
ROB output -- it is the mechanism by which a stage surfaces risk that no prior stage could
have identified. But there is no typed obligation that grounds the risk identification in a
specific F-ID. A risk shift assertion like "the deployment sequencing dependency exposed here
creates a rollback gap not visible to business-review stages" satisfies the structural
requirement while citing no finding. The risk is a vantage-point claim, not a finding-traced
claim. The structural gap: the Downstream Risk Shift slot is a forward-looking assertion slot,
and forward-looking slots currently have no citation obligation in the ROB architecture.

Risk Shift Source F-ID closes the gap with a single-F-ID field. Unlike Synthesis F-IDs
(which requires at least two because cross-stage synthesis by definition characterizes a
pattern across multiple forwarded findings), a risk shift has a primary source finding:
the specific finding from this stage's Findings table or Cross-Stage References that
established the visibility of the failure mode. When multiple findings contributed, name
the primary. The field accepts F-IDs from the current stage's own Findings (e.g. "Stage4-F02")
or from the current stage's Cross-Stage References table -- in either case, the F-ID must
be from the current stage, not from a prior stage's section directly (the risk shift is a
net-new observation from this stage's vantage point, so its ground must be traceable to a
finding at this stage or re-framed through this stage's cross-stage reading).

Anti-pattern rejections for `Risk Shift Source F-ID`:
- "Based on stage review" does not satisfy this field.
- "See findings" does not satisfy this field.
- "General stage concerns" does not satisfy this field.
An empty or generic cell when the Downstream Risk Shift prose names a specific failure mode
or ownership gap is a format failure.

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
{F-ID}]" as its first entry (before any BLOCKER labels if both apply). Absence when Gate
Decision is FAIL or CONDITIONAL is a format failure.

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
| PRIOR-STAGE ESCALATIONS | [fill: At Stage 4 only: if PHASE GATE Decision is FAIL or CONDITIONAL, this cell MUST begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If immediately prior stage had BLOCKER=YES, include "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers AND no FAIL/CONDITIONAL gate.] |
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
| F-01 | [HIGH/MED/LOW -- no other values] | [fill: name the specific artifact or behavior under review, not a category label] | [fill: role responsible for resolution -- "TBD" does not satisfy this column] | [fill: concrete action that closes the finding -- "needs attention" does not satisfy this column] | [fill: D-{ID} from Displacement Map if Inertia Stance is RESISTANT and Severity is HIGH; otherwise N/A -- "N/A" does not satisfy this cell when Inertia Stance is RESISTANT and Severity is HIGH] |
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
Must add substance not already visible in the table above -- do not copy rows into prose.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

**Risk Shift Source F-ID:** [fill: the specific F-ID from this stage's Findings table or
Cross-Stage References table that established the failure mode or gap visibility named above.
When multiple findings contributed, name the primary. F-IDs must be from the current stage
(e.g. "Stage4-F02") -- this is a net-new observation from this stage's vantage point.
"Based on stage review" does not satisfy this field. "See findings" does not satisfy this
field. "General stage concerns" does not satisfy this field. An empty or generic cell when
the Downstream Risk Shift names a specific failure mode or ownership gap is a format failure.]

---

## PHASE GATE -- After Stage 3 (pm), Before Stage 4 (tpm)

Fill after Stage 3 completes, before Stage 4 begins.

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: explicit count by severity -- "HIGH: N, MED: N, LOW: N" -- counted across all Stage 1-3 findings. "Several HIGH findings" does not satisfy this field. A count without three explicit severity bands is a format failure.] |
| Open HIGH Findings | [fill: comma-separated F-IDs of HIGH findings from Stages 1-3 with no owner or no resolution path. NONE if all HIGH findings assigned. "See prior stages" does not satisfy. A FAIL or CONDITIONAL gate with no F-IDs named is a format failure.] |
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
  Calibration Row Applied: [fill: quote the matching row or name the dominant cross-stage condition]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern. Must reference the
    Resistance Trajectory Cumulative Score when characterizing adoption risk.]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- name downstream F-ID or stage action; if OPEN -- name owner stage and pending action. "Discussed" does not satisfy. "See findings" does not satisfy.] |
(1 row per BLOCKER=YES. Empty if none.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill] | [fill: F-IDs or NONE] | [fill: YES / NO / N/A if PASS] | [fill: RESOLVED / OPEN / N/A] |
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
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill] | [fill: at least one F-ID per row. "Inferred from ROB" does not satisfy. "General concerns" does not satisfy.] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------|------------------|---------|------------------|
| [fill] | [fill] | ALIGNED / PARTIAL / GAP | [fill: at least one F-ID per PARTIAL/GAP row. "Based on general review" does not satisfy. ALIGNED rows: N/A acceptable.] |
(Minimum 1 row. All four columns populated.)

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill] | [fill: +1/0/-1] | [fill: specific F-ID if non-zero; N/A if zero. "RESISTANT due to change fatigue" does not satisfy. A +1 or -1 row without a specific F-ID is a format failure.] | [fill] |
| Stage 2 (teams)      | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill] |
| Stage 3 (pm)         | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill] |
| Stage 4 (tpm)        | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill] |
| Stage 5 (arch-board) | [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill] |
| Stage 6 (exec-office)| [fill] | [fill: +1/0/-1] | [fill: F-ID if non-zero; N/A if zero] | [fill] |
| **TOTAL**            | --     | [fill: sum] | -- | [fill: must equal Stage 6 value] |

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
AMEND: carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION, PHASE GATE, all prior handoff packets, and unresolved BLOCKER items forward. Recompute RESISTANCE TRAJECTORY from scratch.

---

## V-03 -- Stage Verdict Aggregate in ROB Summary

**Axis**: Add a `STAGE VERDICT AGGREGATE` table to ROB Summary.
**Hypothesis**: Six stages each produce a Stage Verdict (APPROVED / APPROVED WITH CONDITIONS /
BLOCKED / DEFERRED) derived from the VERDICT CALIBRATION table. Each Stage Verdict has a
Calibration Row Applied and a Rationale citing at least one F-ID. But the ROB Summary Overall
Verdict is derived from "the dominant cross-stage pattern" in an editorial synthesis -- no
typed structure maps from individual stage verdicts to the Overall Verdict with a defined
aggregation rule. A reader who wants to verify the Overall Verdict must read all six Stage
Verdict sections and apply the aggregation rule manually.

The structural gap is the derivation step: the VERDICT CALIBRATION table makes each stage
verdict derivable from the stage's finding profile; the cross-stage aggregation step is not
equivalently structured. The implicit rule is worst-verdict-wins
(BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED), but this rule is never stated
and no table makes it auditable.

STAGE VERDICT AGGREGATE adds the missing derivation table: one row per stage with the Stage
Verdict, the Governing F-ID (the F-ID cited in that stage's Verdict Rationale that drove
the verdict selection), and a Propagation flag (YES if this stage's verdict equals the
Overall Verdict and was the worst verdict observed; NO otherwise). The Overall Verdict in
the ROB Summary header must equal the worst verdict in the Propagation=YES row(s). Anti-pattern
rejections for the Governing F-ID column prevent the column from being satisfied by summary
claims. Anti-pattern for Propagation: exactly the stage(s) with the worst verdict should
have Propagation=YES; if all stages tie at APPROVED, all rows are NO and Propagation is
vacuous -- the Overall Verdict is APPROVED by exhaustion, not propagation.

Anti-pattern rejections for `Governing F-ID`:
- "See stage findings" does not satisfy this column.
- "Multiple findings" does not satisfy this column.
- "General stage concerns" does not satisfy this column.
A row without the F-ID cited in that stage's Verdict Rationale is a format failure.

Anti-pattern for `Propagation`:
- "All stages" does not satisfy this column.
- A row where Stage Verdict is worse than Overall Verdict showing Propagation=NO is a
  format failure (the worse verdict must have driven the Overall Verdict).

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
{F-ID}]" as its first entry (before any BLOCKER labels if both apply). Absence when Gate
Decision is FAIL or CONDITIONAL is a format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill before reading any prior-stage context.

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title from .craft/roles/] |
| Dimension | [fill: orientation in practice-domain terms. Acceptable: "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Role title alone does not satisfy this cell.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill: name -- title] |
| LENS | [fill: same dimension as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell.] |
| PRIOR-STAGE ESCALATIONS | [fill: At Stage 4 only: if PHASE GATE Decision is FAIL or CONDITIONAL, begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If immediately prior stage had BLOCKER=YES, include "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no blockers AND no FAIL/CONDITIONAL gate.] |
| Receipt Declaration | [fill: enumerate specific F-IDs from the prior stage's Handoff Packet Cross-Stage References Forwarded table. If none forwarded, state "No F-IDs forwarded by {prior stage name}". "Reviewed prior stage handoff" does not satisfy. A Declaration without specific F-IDs or explicit no-forward statement is a format failure.] |

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element name from Displacement Map}] |
| Status-Quo Pressure | [fill: concrete pressure this role's stakeholders face. Not "change is hard."] |
| Inertia Stance | [fill: RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence] |

Constraints:
- Minimum 3 stages must have a non-trivial Inertia Check (D-ID cited, concrete pressure named).
- When Inertia Stance is RESISTANT and any finding is HIGH, at least 1 finding must cite the
  inertia D-ID in its D-ID Ref column.

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) | D-ID Ref |
|------|----------|-------------------------------------------------|--------------|------------------------------|----------|
| F-01 | [HIGH/MED/LOW] | [fill: specific artifact or behavior -- not a category label] | [fill: named role -- "TBD" does not satisfy] | [fill: concrete action -- "needs attention" does not satisfy] | [fill: D-{ID} if RESISTANT+HIGH; otherwise N/A] |
| F-02 | [HIGH/MED/LOW] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Minimum 2 rows. All six columns populated. Empty D-ID Ref when RESISTANT+HIGH is format failure.)

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
| [fill] | [fill] | [fill: must name "the orientation declared in Part 0" as the governing lens] | confirms / escalates / reframes |

### Stage Verdict
Apply the VERDICT CALIBRATION table above. Cite the calibration row that applies.

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

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: "HIGH: N, MED: N, LOW: N" across Stages 1-3. Three bands required. "Several HIGH findings" does not satisfy.] |
| Open HIGH Findings | [fill: F-IDs of unowned or unresolved HIGH findings from Stages 1-3. NONE if all resolved. "See prior stages" does not satisfy. FAIL/CONDITIONAL without F-IDs is format failure.] |
| Gate Decision | [fill: PASS / FAIL / CONDITIONAL] |
| Gate Rationale | [fill: cite at least one F-ID if FAIL or CONDITIONAL.] |

- FAIL: at least one Stage 1-3 HIGH has no owner OR no resolution path.
- CONDITIONAL: all HIGH findings owned + pathed, but at least one resolution unverified.
- PASS: no Stage 1-3 HIGH findings, OR all fully resolved.

If FAIL or CONDITIONAL, Stage 4 PRIOR-STAGE ESCALATIONS MUST begin with
"[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence is format failure.

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED --
    must equal the worst Stage Verdict in the STAGE VERDICT AGGREGATE table below]
  Calibration Row Applied: [fill: quote matching row or name dominant cross-stage condition]
  Rationale: [fill: 1-2 sentences. Must reference RESISTANCE TRAJECTORY Cumulative Score
    when characterizing adoption risk.]

### STAGE VERDICT AGGREGATE
(Fill from Stage Verdict sections. Overall Verdict must equal worst Verdict in this table.)

| Stage | Stage Verdict | Governing F-ID | Propagation |
|-------|--------------|----------------|-------------|
| Stage 1 (leadership) | [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED] | [fill: the F-ID cited in this stage's Verdict Rationale that drove verdict selection -- e.g. "Stage1-F02". "See stage findings" does not satisfy this column. "Multiple findings" does not satisfy this column. "General stage concerns" does not satisfy this column. A row without the F-ID from the stage's Verdict Rationale is a format failure.] | [fill: YES if this stage's verdict equals the Overall Verdict and is the worst observed; NO otherwise. A row where Stage Verdict is worse than Overall Verdict with Propagation=NO is a format failure.] |
| Stage 2 (teams)      | [fill] | [fill: F-ID from Stage 2 Verdict Rationale. "See stage findings" does not satisfy.] | [fill: YES / NO] |
| Stage 3 (pm)         | [fill] | [fill: F-ID from Stage 3 Verdict Rationale] | [fill: YES / NO] |
| Stage 4 (tpm)        | [fill] | [fill: F-ID from Stage 4 Verdict Rationale] | [fill: YES / NO] |
| Stage 5 (arch-board) | [fill] | [fill: F-ID from Stage 5 Verdict Rationale] | [fill: YES / NO] |
| Stage 6 (exec-office)| [fill] | [fill: F-ID from Stage 6 Verdict Rationale] | [fill: YES / NO] |

Aggregation rule (pre-stated, not subject to editorial revision):
BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED
Overall Verdict = worst Stage Verdict in this table.
If all stages are APPROVED, Overall Verdict is APPROVED -- all Propagation values are NO.

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- downstream F-ID or stage action; if OPEN -- owner and pending action. "Discussed" does not satisfy. "See findings" does not satisfy.] |
(1 row per BLOCKER=YES. Empty if none.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill] | [fill: F-IDs or NONE] | [fill: YES / NO / N/A if PASS] | [fill: RESOLVED / OPEN / N/A] |
(One row. Required when --stage all.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill] | [fill] | [fill: F-IDs when RESOLVED. Empty when RESOLVED is format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill] | [fill] | [fill] | [fill] |

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: at least one F-ID per named stage. "Multiple findings" does not satisfy.] | [fill] |
(Minimum 1 row if any concern in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill] | [fill: at least one F-ID. "Inferred from ROB" does not satisfy.] |
(Minimum 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------|------------------|---------|------------------|
| [fill] | [fill] | ALIGNED / PARTIAL / GAP | [fill: at least one F-ID per PARTIAL/GAP row. ALIGNED: N/A acceptable.] |

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if zero. "RESISTANT due to change fatigue" does not satisfy. +1/-1 without F-ID is format failure.] | [fill] |
| Stage 2 (teams)      | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 3 (pm)         | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 4 (tpm)        | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 5 (arch-board) | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 6 (exec-office)| [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| **TOTAL**            | --     | [sum]     | --             | [must equal Stage 6] |

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A | N/A | [COMPLETE/PARTIAL/BROKEN] | [BROKEN/PARTIAL: specific missing element + corrective action; COMPLETE: N/A. "Chain incomplete" does not satisfy.] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |

---

USAGE NOTES
--stage all: all 6 stages, PHASE GATE, ROB Summary including STAGE VERDICT AGGREGATE, RESISTANCE TRAJECTORY, and Phase Gate Resolution Status.
--stage {name}: fill INERTIA ANCHOR regardless. Fill PHASE GATE if stage is pm or later. Omit Part 1 if first stage. STAGE VERDICT AGGREGATE: include only completed stages.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: carry all prior context forward. Recompute STAGE VERDICT AGGREGATE and RESISTANCE TRAJECTORY from scratch.

---

## V-04 -- Synthesis F-IDs + Risk Shift Source F-ID (V-01 + V-02)

**Axes**: Synthesis F-IDs in Handoff Packet Cross-Stage Synthesis (V-01) +
Risk Shift Source F-ID in Handoff Packet Downstream Risk Shift (V-02).
**Hypothesis**: V-01 and V-02 address the two prose slots in the same structural artifact --
the Handoff Packet. The Handoff Packet has three slots: the Cross-Stage References Forwarded
table (typed, citation-complete since v8/v9 in the receiving Receipt Declaration), the
Cross-Stage Synthesis prose (now grounded by Synthesis F-IDs in V-01), and the Downstream
Risk Shift prose (now grounded by Risk Shift Source F-ID in V-02). Together they complete
the citation architecture within the Handoff Packet itself: the typed table was always
citation-grounded (it contains F-IDs by definition); V-01 grounds the synthesis commentary
on that table; V-02 grounds the forward-looking risk assertion that concludes the packet.

The structural interaction: Synthesis F-IDs cites backward (from the forwarded table) while
Risk Shift Source F-ID cites forward (from the current stage's findings establishing new
visibility). They are complementary: the Synthesis F-IDs obligation cannot be satisfied by
a Risk Shift F-ID (the risk shift is net-new from this stage; synthesis characterizes the
forwarded cross-stage picture). A stage could cite Stage3-F01 in Synthesis F-IDs (it was
forwarded) but must cite the current stage's own finding in Risk Shift Source F-ID (the risk
shift is newly visible from this stage). Together they close both prose positions in the
Handoff Packet with the same citation mechanism: named, specific F-IDs in typed fields.

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
    status-quo resistance]

---

## Stage Template

Use the following template for each stage. Fill every [fill] slot. Populate every table.

**VERDICT CALIBRATION**

| Condition | Verdict |
|-----------|---------|
| Any HIGH finding with no owner assigned, OR no resolution path stated, OR TPM NO-GO | BLOCKED |
| Any HIGH finding with an owner and a concrete resolution, OR 2+ MED findings with at least 1 unowned | APPROVED WITH CONDITIONS |
| Any finding requires external input before resolution, and that input is not available at this stage | DEFERRED |
| No HIGH findings; all MED findings have owners and resolutions; LOW findings noted | APPROVED |

BLOCKED takes precedence. DEFERRED only when the stage genuinely cannot resolve.
TPM GO/NO-GO is exempt.

**SCOPE-EXCEPTION CALIBRATION**

| Output Type | Exempt | Rationale |
|-------------|--------|-----------|
| TPM GO/NO-GO signal | YES | Labeled binary; table degrades clarity |
| Verdict labels | YES | Pre-defined enumerated values |
| All other findings and assessments | NO | Table-first required; inline guards required |

**BLOCKER PROPAGATION RULE**: If Stage N BLOCKER=YES, Stage N+1 PRIOR-STAGE ESCALATIONS
MUST begin "[BLOCKER: {F-ID} from {stage name}]". Absence is format failure.

**PHASE GATE PROPAGATION RULE**: If PHASE GATE is FAIL or CONDITIONAL, Stage 4
PRIOR-STAGE ESCALATIONS MUST begin "[PHASE-GATE: {Gate Decision} -- {F-ID}]" (before
any BLOCKER label). Absence is format failure.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION

| Field | Value (fill) |
|-------|-------------|
| Role | [fill: name -- title] |
| Dimension | [fill: practice-domain lens. "schedule risk + dependency management"; "adoption risk + stakeholder readiness"; "interface coupling + system boundary integrity"; "mission alignment + resource cascade". Title alone does not satisfy.] |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only.)

| Field | Value (fill) |
|-------|-------------|
| ROLE | [fill] |
| LENS | [fill: same as Part 0] |
| KEY CONCERNS | [fill: 2-4 concerns through the Lens declared in Part 0. Include phrase "selected through the Lens declared in Part 0".] |
| PRIOR-STAGE ESCALATIONS | [fill: Stage 4: "[PHASE-GATE: {Decision} -- {F-ID}]" first if FAIL/CONDITIONAL; "[BLOCKER: {F-ID} from {stage}]" if prior BLOCKER=YES. NONE only if truly empty.] |
| Receipt Declaration | [fill: specific F-IDs from prior stage Handoff Packet Forwarded table. If none forwarded: "No F-IDs forwarded by {stage name}". "Reviewed prior handoff" does not satisfy. Missing specific F-IDs or no-forward statement is format failure.] |

### Stage Identity
  Stage: {canonical-name} / Role: [fill] / Lens: [fill: dimension from Part 0]

### Inertia Check

| Field | Value (fill) |
|-------|-------------|
| Displacement Row Referenced | [fill: D-{ID} -- {element}] |
| Status-Quo Pressure | [fill: concrete pressure -- not "change is hard"] |
| Inertia Stance | [RESISTANT / NEUTRAL / ALIGNED] |
| Stance Rationale | [fill: one sentence] |

Min 3 stages non-trivial. RESISTANT+HIGH finding: D-ID Ref must be populated.

### Findings

| F-ID | Severity | Finding | Owner | Resolution | D-ID Ref |
|------|----------|---------|-------|------------|----------|
| F-01 | [H/M/L] | [fill: specific concern, not category] | [fill: named role] | [fill: concrete action] | [D-{ID} if RESISTANT+HIGH; else N/A] |
| F-02 | [H/M/L] | [fill] | [fill] | [fill] | [N/A or D-{ID}] |
(Min 2 rows. All 6 columns populated. Empty D-ID Ref when RESISTANT+HIGH: format failure.)

At least 1 finding per stage grounded in Part 0 Dimension.

### Cross-Stage References (Stages 2-6 only)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| [fill] | [fill] | confirms / escalates / contradicts | [fill] |

### Prior-Stage Lens Impact (Stages 2-6 only)

| Source Stage | F-ID | How Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|--------------------------------------------|--------------|
| [fill] | [fill] | [fill: must name "the orientation declared in Part 0"] | confirms / escalates / reframes |

### Stage Verdict

  Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill: quote matching row]
  Rationale: [fill: cite at least one F-ID. One sentence.]

  tpm only: **TPM GO/NO-GO: [GO / GO WITH CONDITIONS / NO-GO]** Rationale: [F-ID citation.]

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| [YES/NO] | [if YES] | [if YES] | [if YES] |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| [fill] | [fill] | confirms / escalates / contradicts |

**Cross-Stage Synthesis:**
[fill: characterize the downstream significance. Must add substance not in the table above.]

**Synthesis F-IDs:** [fill: at least two F-IDs from the Forwarded table that this synthesis
characterizes. One F-ID satisfies when Forwarded table has exactly one row. Empty table:
"No F-IDs forwarded -- synthesis deferred". "See forwarded table" does not satisfy. Fewer
than two F-IDs when 2+ rows forwarded is format failure.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Not a restatement of Prior-Stage Lens Impact.]

**Risk Shift Source F-ID:** [fill: specific F-ID from this stage's Findings or Cross-Stage
References establishing the failure mode or gap visibility. Name primary if multiple.
Must be from current stage. "Based on stage review" does not satisfy. "See findings" does
not satisfy. Empty or generic when risk shift names a specific mode is format failure.]

---

## PHASE GATE -- After Stage 3 (pm), Before Stage 4 (tpm)

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: "HIGH: N, MED: N, LOW: N". Three bands required. "Several HIGH findings" does not satisfy.] |
| Open HIGH Findings | [fill: F-IDs of unowned/unresolved HIGHs from Stages 1-3. NONE if all resolved. FAIL/CONDITIONAL without F-IDs is format failure.] |
| Gate Decision | [PASS / FAIL / CONDITIONAL] |
| Gate Rationale | [fill: cite F-ID if FAIL or CONDITIONAL.] |

FAIL: any Stage 1-3 HIGH unowned or unpathed. CONDITIONAL: all owned/pathed but unverified.
PASS: no Stage 1-3 HIGHs or all fully resolved.
FAIL/CONDITIONAL: Stage 4 PRIOR-STAGE ESCALATIONS must begin "[PHASE-GATE: {Decision} -- {F-ID}]".

---

## ROB Summary

  Overall Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Calibration Row Applied: [fill]
  Rationale: [fill: 1-2 sentences. Reference RESISTANCE TRAJECTORY Cumulative Score for
    adoption risk.]

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- downstream F-ID or action; if OPEN -- owner + pending. "Discussed" does not satisfy.] |
(1 row per BLOCKER=YES. Empty if none.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill] | [F-IDs or NONE] | [YES / NO / N/A if PASS] | [RESOLVED / OPEN / N/A] |

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill] | [fill] | [fill: F-IDs when RESOLVED. Empty when RESOLVED: format failure.] | RESOLVED/OPEN/ESCALATED |
| D-02 | [fill] | [fill] | [fill] | [fill] |

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [2+ stages] | [at least one F-ID per named stage. "Multiple findings" does not satisfy.] | [fill] |

### Risk Register (tpm only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | H/M/L | H/M/L | [fill] | [at least one F-ID. "Inferred from ROB" does not satisfy.] |
(Min 3 rows. At least 1 HIGH.)

### Mission Cascade (exec-office only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------|------------------|---------|------------------|
| [fill] | [fill] | ALIGNED/PARTIAL/GAP | [at least one F-ID per PARTIAL/GAP row. ALIGNED: N/A ok.] |

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if 0. "RESISTANT due to change fatigue" does not satisfy.] | [fill] |
| Stage 2 (teams)      | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 3 (pm)         | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 4 (tpm)        | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 5 (arch-board) | [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| Stage 6 (exec-office)| [fill] | [+1/0/-1] | [F-ID or N/A] | [fill] |
| **TOTAL**            | --     | [sum]     | --             | [must equal Stage 6] |

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 | [P/A] | N/A | N/A | [C/P/B] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 2 | [P/A] | [P/A] | [P/A] | [C/P/B] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 3 | [P/A] | [P/A] | [P/A] | [C/P/B] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 4 | [P/A] | [P/A] | [P/A] | [C/P/B] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 5 | [P/A] | [P/A] | [P/A] | [C/P/B] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |
| Stage 6 | [P/A] | [P/A] | [P/A] | [C/P/B] | [BROKEN/PARTIAL: specific + corrective; COMPLETE: N/A] |

---

USAGE NOTES
--stage all: all 6 stages, PHASE GATE, ROB Summary.
--stage {name}: fill INERTIA ANCHOR regardless; PHASE GATE if pm or later; omit Part 1 at Stage 1.
--scope {group}: filter org.yaml.
AMEND: carry all context forward; recompute RESISTANCE TRAJECTORY from scratch.

---

## V-05 -- Synthesis F-IDs + Risk Shift Source F-ID + Stage Verdict Aggregate (V-01 + V-02 + V-03)

**Axes**: Synthesis F-IDs (V-01) + Risk Shift Source F-ID (V-02) + Stage Verdict Aggregate (V-03).
**Hypothesis**: V-01 closes the Handoff Packet synthesis prose grounding gap; V-02 closes the
Handoff Packet risk shift prose grounding gap; V-03 closes the ROB Summary Overall Verdict
derivation gap. The three axes are structurally independent -- each targets a different
position (Handoff Packet synthesis slot, Handoff Packet risk shift slot, ROB Summary verdict
aggregation table). None of the three regresses any prior criterion.

The structural interaction across all three: V-01 and V-02 both operate in the Handoff Packet
and together complete the citation architecture within that artifact. V-03 operates in the ROB
Summary and uses the Stage Verdict record produced by all six stages -- including the TPM
verdict that the Risk Register and GO/NO-GO (now grounded in Source F-IDs from C-33) feeds
into. When Stage 4 (tpm) produces BLOCKED (driven by a Risk Register HIGH with a Source F-ID),
that verdict appears in the STAGE VERDICT AGGREGATE with Propagation=YES and its Governing
F-ID, making the Overall Verdict traceable from the TPM finding through the Risk Register
Source F-ID, through the Stage Verdict, through the Aggregate table, to the Overall Verdict.
This is the deepest citation chain in the ROB architecture: finding -> risk register row ->
stage verdict -> overall verdict, each link typed and grounded.

V-05 R11 makes the full R11 hypothesis testable: if all three obligations are satisfied, then
the ROB output is structurally complete at every level:
- Table citation per row (v8: C-30, C-31, C-32)
- Operational table citation per row (v9: C-33, C-34, C-35)
- Phase-boundary gate (R10 V-01)
- Per-stage handoff receipt enumeration (R10 V-02)
- Resistance accumulation with grounding F-IDs (R10 V-03)
- Handoff Packet synthesis prose grounded in forwarded F-IDs (R11 V-01)
- Handoff Packet risk shift prose grounded in current-stage F-ID (R11 V-02)
- Overall Verdict derivable from worst stage verdict with governing F-ID per stage (R11 V-03)

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
{F-ID}]" as its first entry (before any BLOCKER labels if both apply). Absence when Gate
Decision is FAIL or CONDITIONAL is a format failure.

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
| PRIOR-STAGE ESCALATIONS | [fill: At Stage 4 only: if PHASE GATE Decision is FAIL or CONDITIONAL, this cell MUST begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". If immediately prior stage had BLOCKER=YES, include "[BLOCKER: {F-ID} from {stage name}]". NONE only if no escalations AND no prior-stage blockers AND no FAIL/CONDITIONAL gate.] |
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

**Synthesis F-IDs:** [fill: comma-separated list of at least two F-IDs from the Cross-Stage
References Forwarded table above that this synthesis characterizes -- e.g. "Stage2-F01,
Stage3-F02". When the Forwarded table has exactly one row, one F-ID satisfies this field.
When the Forwarded table is empty, state "No F-IDs forwarded -- synthesis deferred".
"See forwarded table" does not satisfy this field. "Based on overall stage findings" does not
satisfy this field. "Forwarded findings reviewed" does not satisfy this field. A Synthesis
F-IDs field with fewer than two F-IDs when 2+ rows are forwarded is a format failure.]

**Downstream Risk Shift:**
[fill: name a failure mode or ownership gap newly visible from this stage's vantage point.
Do not restate Prior-Stage Lens Impact -- that table names re-readings through the Part 0
lens; this slot names net-new visibility at this stage's vantage point.]

**Risk Shift Source F-ID:** [fill: the specific F-ID from this stage's Findings table or
Cross-Stage References table that established the failure mode or gap visibility named above.
When multiple findings contributed, name the primary. F-IDs must be from the current stage.
"Based on stage review" does not satisfy this field. "See findings" does not satisfy this
field. "General stage concerns" does not satisfy this field. An empty or generic cell when
the Downstream Risk Shift names a specific failure mode or ownership gap is a format failure.]

---

## PHASE GATE -- After Stage 3 (pm), Before Stage 4 (tpm)

Fill after Stage 3 completes, before Stage 4 begins. Every slot must be populated.
Required when --stage all is used. Fill if stage is pm or later for single-stage runs.

| Field | Value (fill) |
|-------|-------------|
| Phase A Finding Count | [fill: explicit count by severity -- "HIGH: N, MED: N, LOW: N" -- counted across all Stage 1-3 findings. "Several HIGH findings" does not satisfy this field. A count without three explicit severity bands is a format failure.] |
| Open HIGH Findings | [fill: comma-separated F-IDs of HIGH findings from Stages 1-3 with no owner or no resolution path at this gate. NONE if all HIGH findings assigned. "See prior stages" does not satisfy. A FAIL or CONDITIONAL gate with no F-IDs named is a format failure.] |
| Gate Decision | [fill: PASS / FAIL / CONDITIONAL] |
| Gate Rationale | [fill: one sentence naming dominant condition. Cite at least one F-ID if FAIL or CONDITIONAL. "Phase A had issues" does not satisfy.] |

Gate Decision definitions:
- FAIL: at least one Stage 1-3 HIGH finding has no owner assigned OR no resolution path stated.
- CONDITIONAL: all HIGH findings have owners and paths, but at least one resolution is
  not yet verified or depends on an action outside Stage 1-3 scope.
- PASS: no HIGH findings raised in Stages 1-3, OR all HIGH findings fully resolved.

If Gate Decision is FAIL or CONDITIONAL, Stage 4's Part 1 PRIOR-STAGE ESCALATIONS MUST
begin with "[PHASE-GATE: {Gate Decision} -- {F-ID}]". Absence is a format failure.

---

## ROB Summary

Fill after all stages complete.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED --
    must equal the worst Stage Verdict in the STAGE VERDICT AGGREGATE table below]
  Calibration Row Applied: [fill: quote the matching row or name dominant cross-stage condition]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern. Must reference the
    Resistance Trajectory Cumulative Score when characterizing adoption risk.]

### STAGE VERDICT AGGREGATE
(Fill from Stage Verdict sections. Overall Verdict must equal worst Verdict in this table.
Aggregation rule: BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED.)

| Stage | Stage Verdict | Governing F-ID | Propagation |
|-------|--------------|----------------|-------------|
| Stage 1 (leadership) | [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED] | [fill: the F-ID cited in this stage's Verdict Rationale -- e.g. "Stage1-F02". "See stage findings" does not satisfy this column. "Multiple findings" does not satisfy this column. "General stage concerns" does not satisfy this column. A row without the F-ID from the stage's Verdict Rationale is a format failure.] | [fill: YES if this stage's verdict is the worst observed and equals the Overall Verdict; NO otherwise. A row where Stage Verdict is worse than Overall Verdict with Propagation=NO is a format failure.] |
| Stage 2 (teams)      | [fill] | [fill: F-ID from Stage 2 Verdict Rationale. "See stage findings" does not satisfy.] | [YES / NO] |
| Stage 3 (pm)         | [fill] | [fill: F-ID from Stage 3 Verdict Rationale] | [YES / NO] |
| Stage 4 (tpm)        | [fill] | [fill: F-ID from Stage 4 Verdict Rationale] | [YES / NO] |
| Stage 5 (arch-board) | [fill] | [fill: F-ID from Stage 5 Verdict Rationale] | [YES / NO] |
| Stage 6 (exec-office)| [fill] | [fill: F-ID from Stage 6 Verdict Rationale] | [YES / NO] |

### Blocker Resolution Status
| Stage | F-ID | Downstream Stage(s) Notified | Resolution Status | Resolution Evidence |
|-------|------|------------------------------|-------------------|---------------------|
| [fill] | [fill] | [fill] | RESOLVED / OPEN | [fill: if RESOLVED -- name downstream F-ID or stage action; if OPEN -- owner stage + pending action. "Discussed" does not satisfy. "See findings" does not satisfy.] |
(1 row per BLOCKER=YES raised across all stages. Empty if no blockers raised.)

### Phase Gate Resolution Status
| Gate Decision | Open HIGH F-IDs at Gate | Stage 4 PHASE-GATE Label Present | Resolution Status |
|---------------|------------------------|----------------------------------|-------------------|
| [fill: PASS / FAIL / CONDITIONAL] | [fill: F-IDs or NONE] | [fill: YES / NO / N/A if Gate Decision is PASS] | [fill: RESOLVED / OPEN / N/A] |
(One row. Required when --stage all is used.)

### Inertia Resolution Status
| D-ID | Displaced Element | Stage(s) That Surfaced It | Addressing F-IDs | Status |
|------|-------------------|-----------------------------|-----------------|--------|
| D-01 | [fill from INERTIA ANCHOR] | [fill: stage(s)] | [fill: comma-separated F-IDs from named stages. When Status is RESOLVED, at least one F-ID citing MED or HIGH finding required. "General resistance noted" does not satisfy. Empty when RESOLVED is a format failure.] | RESOLVED / OPEN / ESCALATED |
| D-02 | [fill from INERTIA ANCHOR] | [fill] | [fill] | [fill] |
(One row per Displacement Map entry.)

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Primary F-IDs | Why Recurrence Elevates Severity |
|-------|--------------------------|---------------|----------------------------------|
| [fill] | [fill: 2+ stages] | [fill: at least one F-ID per named stage required. "Multiple findings" does not satisfy. "See findings" does not satisfy. A theme row without an F-ID per named stage is a format failure.] | [fill: explain the pattern -- not a copy of any individual finding] |
(Minimum 1 row if any concern appears in 2+ stages.)

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation | Source F-IDs |
|------------|----------|------------|------------|--------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] | [fill: comma-separated F-IDs from stage sections that grounded this risk. At least one F-ID per risk row is required. "Inferred from ROB" does not satisfy this column. "General concerns" does not satisfy this column. An empty Source F-IDs cell is a format failure.] |
(Minimum 3 rows. At least 1 HIGH. All five columns must be populated.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title -- not "strategic priorities") | Trace to Artifact | Verdict | Supporting F-IDs |
|---------------------------------------------------------------|------------------|---------|------------------|
| [fill: actual mission title] | [fill: specific trace] | ALIGNED / PARTIAL / GAP | [fill: for PARTIAL or GAP rows -- at least one F-ID required. "Based on general review" does not satisfy. "See ROB findings" does not satisfy. A PARTIAL or GAP row without an F-ID is a format failure. ALIGNED rows: N/A acceptable.] |
(Minimum 1 row. All four columns must be populated.)

### RESISTANCE TRAJECTORY
| Stage | Inertia Stance | Resistance Delta | Grounding F-ID | Cumulative Score |
|-------|---------------|-----------------|----------------|-----------------|
| Stage 1 (leadership) | [fill: RESISTANT/NEUTRAL/ALIGNED] | [fill: +1/0/-1] | [fill: specific F-ID from this stage if Delta +1 or -1; N/A if Delta 0. "RESISTANT due to change fatigue" does not satisfy. "Stage stance noted" does not satisfy. "General resistance" does not satisfy. A +1 or -1 row without specific F-ID is a format failure. A 0 row with any value other than N/A is a format failure.] | [fill: running total] |
| Stage 2 (teams)      | [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if zero] | [fill] |
| Stage 3 (pm)         | [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if zero] | [fill] |
| Stage 4 (tpm)        | [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if zero] | [fill] |
| Stage 5 (arch-board) | [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if zero] | [fill] |
| Stage 6 (exec-office)| [fill] | [+1/0/-1] | [F-ID if non-zero; N/A if zero] | [fill] |
| **TOTAL**            | --     | [fill: sum] | --             | [must equal Stage 6 Cumulative Score] |

Cumulative Score interpretation (informational -- not a gate):
- Positive: net resistance accumulation; adoption-risk rationale must name dominant RESISTANT stage.
- Negative: net alignment gain; rationale may note largest alignment signal.
- Zero: balanced or null inertia; rationale should note whether genuine balance or absence of signal.

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain | Remediation Action |
|-------|--------|-------------------------|------------------------|-------|--------------------|
| Stage 1 (leadership) | [PRESENT/ABSENT] | N/A (no envelope) | N/A (first stage) | [COMPLETE/PARTIAL/BROKEN] | [fill: if BROKEN or PARTIAL -- name the specific missing element and the corrective action; if COMPLETE -- N/A. "Chain incomplete" does not satisfy this column. "Needs review" does not satisfy this column. A BROKEN or PARTIAL row without a remediation action naming the specific missing element is a format failure.] |
| Stage 2 (teams)      | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 3 (pm)         | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 4 (tpm)        | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 5 (arch-board) | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |
| Stage 6 (exec-office)| [PRESENT/ABSENT] | [PRESENT/ABSENT] | [PRESENT/ABSENT] | [COMPLETE/PARTIAL/BROKEN] | [if BROKEN or PARTIAL -- specific missing element + corrective action; if COMPLETE -- N/A] |

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, PHASE GATE,
ROB Summary including STAGE VERDICT AGGREGATE, RESISTANCE TRAJECTORY, and Phase Gate
Resolution Status.
--stage {name}: fill INERTIA ANCHOR regardless. Fill PHASE GATE if stage is pm or later.
Omit Part 1 if first stage. STAGE VERDICT AGGREGATE: include only completed stages.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR, Displacement Map, VERDICT CALIBRATION,
PHASE GATE decision, all prior handoff packets, and any unresolved BLOCKER items forward.
Recompute STAGE VERDICT AGGREGATE and RESISTANCE TRAJECTORY from scratch using updated data.
