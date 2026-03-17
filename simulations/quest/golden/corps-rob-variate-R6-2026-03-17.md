---
skill: quest-variate
skill_target: corps-rob
round: 6
date: 2026-03-17
rubric_version: 5
---

# Variate R6 -- corps-rob (rubric v5, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v5.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R5 diagnosis under v5 re-grades:** Both V-01 R5 and V-02 R5 composite at 100. V-02 R5
leads on raw aspirational count (15 vs 11). The sole path to 15/15 raw requires C-20
(pre-envelope Part 0 block), which then unlocks C-21, C-22, C-23 via the N/A dependency
chain. V-01 R5's architecture (standalone Lens: in Stage Identity) tops out at 11 raw
because C-20 through C-23 remain unreachable without the pre-envelope position.

| Variation | v4 Score | v5 Score | v5 Failures |
|-----------|----------|----------|-------------|
| V-02 R5   | 99 (v4)  | **100**  | none -- 15 raw, composite ceiling |
| V-01 R5   | 96.5 (v4)| **100**  | C-20 FAIL, C-21--C-23 N/A->FAIL -- 11 raw |
| V-02 R4   | 99 (v4)  | **99**   | C-19 FAIL, C-20--C-23 FAIL/N/A -- 9 raw |

R6 probes three structural questions, each independent of the Part 0 architecture:

1. **Phrasing register** -- Does expressing the prompt as fill-slot declarative templates
   (every output element as a labeled [fill] slot) improve structural compliance vs.
   imperative/instructive register? Hypothesis: visible blank slots make omissions
   detectable in the output, strengthening C-18/C-19/C-20 compliance.

2. **Inertia framing** -- Does elevating inertia to a first-class anchor (INERTIA ANCHOR
   section at run open, per-stage INERTIA CHECK as a required structural step) strengthen
   C-13 compliance and ground C-02 role-loaded findings in concrete displacement context?
   Hypothesis: named displacement entries in the anchor give each stage's INERTIA CHECK
   a concrete referent, preventing generic "change is hard" output.

3. **Output format** -- Does expressing findings as structured tables (F-ID | Severity |
   Finding | Owner | Resolution) with mandatory columns improve C-04 compliance vs. prose
   numbered findings? Hypothesis: mandatory Owner and Resolution columns make omission a
   visible format error rather than an implicit prose gap.

All 5 variations preserve the Part 0 LENS ACTIVATION architecture from V-02 R5. Dropping
Part 0 would reduce raw aspirational ceiling from 15 to 11 (or lower). The Part 0
architecture is non-negotiable at R6.

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register -- fill-slot declarative | Fill slots make structural omissions visible in the output |
| V-02 | Inertia framing -- prominent status-quo competitor | Named displacement anchor grounds C-13 and strengthens C-02 |
| V-03 | Output format -- table-first structured findings | Mandatory table columns enforce C-04 ownership and resolution |
| V-04 | V-01 fill-slot + V-02 inertia | Combined: omission detection + concrete displacement context |
| V-05 | V-01 fill-slot + V-02 inertia + V-03 table-first | Maximum structural compliance: three axes combined |

---

## V-01 -- Phrasing Register: Fill-Slot Declarative Template

**Axis**: Phrasing register -- imperative vs. fill-slot declarative
**Hypothesis**: Expressing every structural element as a labeled `[fill]` slot forces
the executing model to populate each slot explicitly. An unfilled slot is visible in the
output; prose instructions can be satisfied implicitly. This should strengthen C-18
(Lens fill field), C-19 (Stage 1 coverage), C-20 (Part 0 block), C-21 (KEY CONCERNS
back-reference), and C-22 (Lens Impact reference) because each is a dedicated output slot
that cannot be silently skipped.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml to identify the assigned role for each stage.
- Read .craft/roles/<role-file>.md to load the persona for each stage.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name} (optional; restrict to one division or tribe)
             AMEND: re-run a specific stage with updated inputs or scope

STAGE SEQUENCE (default --stage all):
  Stage 1: leadership    Stage 2: teams    Stage 3: pm
  Stage 4: tpm           Stage 5: arch-board    Stage 6: exec-office

INERTIA ANCHOR (fill once before Stage 1):
  What this topic displaces: [fill: name the system, process, or workflow being replaced or changed]
  Cost-bearer: [fill: which team, role, or system absorbs the change cost]

For each stage in the run, produce the following template exactly. Fill every [fill] slot
with substantive content. A visible unfilled slot indicates non-compliance.

---

STAGE TEMPLATE

## Stage {N}: {canonical-name} -- {Role Name from org.yaml}

### Part 0 -- LENS ACTIVATION
This block precedes the briefing envelope. Fill before reading any prior-stage context.

  Role:      [fill: role name and title from .craft/roles/]
  Dimension: [fill: orientation in practice-domain terms. Name the lens dimension, not just
    the role title. Acceptable examples: "schedule risk + dependency management" (TPM);
    "adoption risk + stakeholder readiness" (PM); "interface coupling + system boundary
    integrity" (Principal Architect); "mission alignment + resource cascade" (Chief of
    Staff). "TPM perspective" or role title alone does not satisfy this slot.]

### Part 1 -- BRIEFING ENVELOPE
(Fill for Stages 2 through 6. This section is absent at Stage 1.)

  ROLE:     [fill: name -- title]
  LENS:     [fill: same dimension as Part 0]
  KEY CONCERNS: [fill: 2-4 concerns forwarded from prior stages, selected through the
    Lens declared in Part 0. This slot must contain the phrase "selected through the Lens
    declared in Part 0" as part of the selection instruction. Do not copy prior findings
    verbatim -- select and reframe through your lens.]
  PRIOR-STAGE ESCALATIONS: [fill: items explicitly escalated from prior stage handoff
    packets, or NONE if no escalations exist]

### Stage Identity
  Stage:    {canonical-name}
  Role:     [fill: name -- title]
  Lens:     [fill: same dimension as Part 0]
  (At Stage 1, this Lens: line is the sole lens declaration for this stage because Part 1
  is absent. It must contain the dimension, not just the role name.)

### Inertia Check
  [fill: state the status-quo pressure this role faces given the INERTIA ANCHOR. Name
  what the role's stakeholders are defending or what change this role's stakeholders
  resist. Generic "change is hard" does not satisfy this slot. At least 3 of the 6
  stages must have a non-trivial Inertia Check that names a specific pressure.]

### Findings
Number every finding. Each must name the specific artifact or concern under review.

  F-01 [HIGH/MED/LOW]: [fill: specific concern -- not a domain category]. Owner: [fill:
    role]. Resolution: [fill: concrete action that resolves the concern].
  F-02 [HIGH/MED/LOW]: [fill]. Owner: [fill]. Resolution: [fill].
  [Additional findings as warranted. Minimum 2 per stage.]

  Constraint: At least one finding per stage must be grounded in the Part 0 Dimension --
  the concern must be specific to this role's practice orientation, not a generic concern
  any reviewer would raise for any topic.

### Cross-Stage References
(Fill for Stage 2 onward. Minimum 2 backward references total across all stages in a
multi-stage run. Absent at Stage 1.)

  - [source stage] [F-ID]: [confirms / escalates / contradicts] -- [fill: note explaining
    how this stage's lens changes or confirms the prior finding]

### Prior-Stage Lens Impact
(Fill for Stage 2 onward. Absent at Stage 1.)

  - [source stage] [F-ID]: [fill: how this finding reads differently through the
    orientation declared in Part 0. This slot must name "the orientation declared in
    Part 0" as the governing lens.] -- [confirms / escalates / reframes]

### Stage Verdict
  Verdict:   [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: cite at least one F-ID from the findings above. One sentence.]

  tpm stage only -- add this top-level labeled signal above the verdict:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk entry. One sentence.]

### Blocker Field
  BLOCKER: [fill: YES / NO]
  [If YES: fill -- blocking F-ID | downstream stage blocked | reason the downstream stage
  cannot proceed without resolution of this finding.]

### Handoff Packet

  Cross-Stage References Forwarded:
  - [source stage] [F-ID]: [confirms / escalates / contradicts] -- [fill: note]
  [List all cross-stage references this stage surfaces for downstream stages.]

  Cross-Stage Synthesis:
  [fill: characterize the downstream significance of the collected cross-stage picture.
  Must add substance not already stated in Cross-Stage References Forwarded above -- do
  not copy reference entries into prose. Acceptable additions: a pattern across multiple
  references; a risk escalation beyond any single reference; a downstream action not
  stated in any individual reference.]

  Downstream Risk Shift:
  [fill: name a failure mode or ownership gap that becomes newly visible from this stage's
  vantage point. Do not restate Prior-Stage Lens Impact content -- that slot names how
  prior work reads differently through this role's lens; this slot names what is net-new
  visible at this stage's vantage point.]

---

END OF STAGE TEMPLATE (repeat for each stage in the run)

---

ROB SUMMARY

After all stages complete, produce this summary section.

## ROB Summary

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern or the most
    severe unresolved finding across stages]

### Cross-Cutting Themes
  [fill: name each concern that appeared independently in 2 or more stages. For each
  theme: cite the 2+ stages that surfaced it; explain why recurrence across stages elevates
  severity beyond any single-stage instance. Do not copy individual findings verbatim --
  characterize the pattern of recurrence. Minimum 1 theme if any concern recurs.]

### Risk Register (tpm stage only)
  | Risk Title | Severity | Likelihood | Mitigation |
  |------------|----------|------------|------------|
  | [fill: specific risk name] | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
  (Minimum 3 rows. At least 1 HIGH severity. Prose-only risk summaries do not satisfy
  this section.)

### Mission Cascade (exec-office stage only)
  | S-Office Mission (actual title) | Trace to Artifact | Verdict |
  |---------------------------------|-------------------|---------|
  | [fill: actual mission title -- not "strategic priorities"] | [fill: specific path from mission to artifact] | ALIGNED / PARTIAL / GAP |
  (Minimum 1 row. Vague alignment claims do not satisfy this section.)

### LENS ACTIVATION CHAIN HEALTH
  [fill: report per-stage chain status for every stage in the run]
  - Stage 1 (leadership):   Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [N/A -- no envelope at Stage 1] | Lens Impact [N/A -- first stage] -> Chain: [COMPLETE / PARTIAL / BROKEN]
  - Stage 2 (teams):        Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
  - Stage 3 (pm):           Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
  - Stage 4 (tpm):          Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
  - Stage 5 (arch-board):   Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
  - Stage 6 (exec-office):  Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]

---

USAGE NOTES

--stage all          Run all 6 stages in sequence. Produce the ROB Summary at the end.
--stage {name}       Run a single stage. Omit Part 1 if no prior stages exist. All slots
                     still required.
--scope {group}      Filter org.yaml to the named division or tribe. Run all selected
                     stages for that scope only.
AMEND               Re-run a named stage using prior outputs as context. Carry all prior
                     handoff packets forward.

---

## V-02 -- Inertia Framing: Prominent Status-Quo Competitor

**Axis**: Inertia framing -- minimal mention vs. prominent status-quo competitor
**Hypothesis**: Elevating the INERTIA ANCHOR to a first-class pre-run section, with
named displacement entries that each stage's INERTIA CHECK must reference, prevents
generic "change is hard" output and grounds C-02 role-loaded findings in concrete
displacement context. A named displacement map also makes C-13 structurally
self-enforcing: each INERTIA CHECK must cite a specific entry, not infer one from thin
air.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml to identify the assigned role for each stage.
- Read .craft/roles/<role-file>.md to load the persona for each stage.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name} (optional)
             AMEND: re-run a specific stage

STAGE SEQUENCE (default --stage all):
  Stage 1: leadership    Stage 2: teams    Stage 3: pm
  Stage 4: tpm           Stage 5: arch-board    Stage 6: exec-office

---

## INERTIA ANCHOR

Establish the inertia baseline before Stage 1. This section is the evidence source for
all per-stage INERTIA CHECKs. Every field must be populated.

**Status-Quo Competitor:** Name the system, process, or approach this topic displaces.
This is not the topic -- it is what the topic replaces or competes with for adoption.

**Displacement Map:**
| ID  | Displaced Element | Who Bears the Cost | Change Type |
|-----|-------------------|--------------------|-------------|
| D-01| {name the specific thing displaced} | {team, role, or system} | {migration / behavior change / tooling switch / process change} |
| D-02| {name another displaced element} | {cost-bearer} | {change type} |
(Minimum 2 rows. These entries are the raw material each stage's INERTIA CHECK must cite.)

**Inertia Risk Statement:** One sentence naming the strongest single source of status-quo
resistance -- the displacement most likely to create adoption friction or political
resistance across the ROB stages.

---

## Stage Instructions

For each stage in the run, produce the following sections in order.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Declare before opening any prior-stage context.

  Role: {name} -- {title}
  Dimension: {orientation in practice-domain terms -- name the lens, not just the role
    title. Examples: "schedule risk + dependency management" (TPM) | "adoption risk +
    stakeholder readiness" (PM) | "interface coupling + system boundary integrity"
    (Principal Architect) | "mission alignment + resource cascade" (Chief of Staff).
    Role title alone does not satisfy this field.}

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

  ROLE:     {name} -- {title}
  LENS:     {same dimension as Part 0}
  KEY CONCERNS:  Select 2-4 concerns from prior stages, filtered through the Lens
    declared in Part 0. State explicitly: "concerns selected through the Lens declared
    in Part 0." Do not copy all prior findings -- select only what this role's lens
    makes salient.
  PRIOR-STAGE ESCALATIONS: Items explicitly escalated from prior handoff packets, or
    NONE.

### Stage Identity
  Stage:    {canonical-name}
  Role:     {name} -- {title}
  Lens:     {same dimension as Part 0}
  (At Stage 1 this is the sole lens declaration. Must name the dimension.)

### Inertia Check
From the INERTIA ANCHOR Displacement Map, identify the row most relevant to this
reviewing role. This check must cite a specific Displacement Map entry by ID -- generic
statements do not satisfy this section.

  Displacement Entry Referenced: D-{ID} -- {displaced element name}
  Status-Quo Pressure: What is this role's stakeholders defending against this topic?
    What does the role risk if the topic succeeds? What does it cost the role if the
    topic fails? Name the concrete pressure -- not "change is hard."
  Inertia Stance: {RESISTANT / NEUTRAL / ALIGNED} -- one sentence explaining the
    posture this role takes toward the displacement.

  At least 3 of the 6 stages must have a populated, non-trivial Inertia Check that
  cites a specific Displacement Map entry and names a concrete stakeholder pressure.
  When Inertia Stance is RESISTANT and any finding is HIGH severity, at least one
  finding in that stage must reference the inertia contribution as a factor.

### Findings
At least 2 findings per stage. Each names the specific artifact or concern under review.

  F-01 [HIGH/MED/LOW]: {specific concern}. Owner: {role}. Resolution: {action}.
  F-02 [HIGH/MED/LOW]: ... Owner: ... Resolution: ...
  [Additional findings as warranted.]

  At least one finding per stage must reflect the loaded persona's specific lens from
  Part 0 -- a concern only this role's orientation would surface.

### Cross-Stage References
(Stage 2 onward. At least 2 backward references total across all stages.)

  - {source stage} {F-ID}: {confirms / escalates / contradicts} -- {note}

### Prior-Stage Lens Impact
(Stage 2 onward.)

  - {source stage} {F-ID}: Reading through the orientation declared in Part 0, {how this
    finding reads differently} -- {confirms / escalates / reframes}

### Stage Verdict
  Verdict: {APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED}
  Rationale: Cite at least one F-ID. One sentence.

  tpm stage only -- top-level labeled signal:
  **TPM GO/NO-GO: {GO / GO WITH CONDITIONS / NO-GO}**
  Rationale: {cite specific F-ID or risk register entry. One sentence.}

  When Inertia Stance is RESISTANT and the verdict is BLOCKED or APPROVED WITH
  CONDITIONS, explain how inertia is a contributing factor in the rationale.

### Blocker Field
  BLOCKER: {YES / NO}
  If YES: {blocking F-ID} blocks {downstream stage} because {reason the downstream
  stage cannot proceed without resolution}.

### Handoff Packet

  Cross-Stage References Forwarded:
  - {source stage} {F-ID}: {confirms / escalates / contradicts} -- {note}

  Cross-Stage Synthesis (must add substance beyond the forwarded references above):
  {Downstream significance: risk escalation beyond any single reference; named pattern
  across multiple references; or a specific downstream action not stated in any
  individual reference. Do not copy reference entries into prose.}

  Downstream Risk Shift (do not restate from Prior-Stage Lens Impact):
  {Name a failure mode or ownership gap newly visible from this stage's vantage point.
  This is net-new -- not a re-reading of what was already seen through the Part 0 lens.}

---

## ROB Summary

After all stages complete, produce this section.

### Overall Verdict
  {APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED}
  Rationale: 1-2 sentences citing the dominant cross-stage pattern.

### Inertia Resolution Status
For each Displacement Map entry from the INERTIA ANCHOR, report whether any stage
finding has addressed or escalated the displacement risk:
| D-ID | Displaced Element | Stage(s) That Surfaced It | Status |
|------|-------------------|-----------------------------|--------|
| D-01 | {element}         | {stage(s)}                  | RESOLVED / OPEN / ESCALATED |
| D-02 | ...               | ...                         | ... |

### Cross-Cutting Themes
Name each concern that appeared independently in 2 or more stages. For each theme:
cite the 2+ stages; explain why recurrence across stages elevates severity beyond any
single-stage instance. Minimum 1 theme if any concern recurs.

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
Minimum 3 entries. At least 1 HIGH severity.

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict |
|---------------------------------|------------------|---------|
At least 1 named mission title. "Strategic priorities" does not satisfy this section.

### LENS ACTIVATION CHAIN HEALTH
Per-stage chain status across all stages in the run:
- Stage 1 (leadership):   Part 0 {PRESENT/ABSENT} | KEY CONCERNS Ref [N/A -- no envelope] | Lens Impact [N/A -- first stage] -> {COMPLETE / PARTIAL / BROKEN}
- Stage 2 (teams):        Part 0 {PRESENT/ABSENT} | KEY CONCERNS Ref {PRESENT/ABSENT} | Lens Impact Ref {PRESENT/ABSENT} -> {COMPLETE / PARTIAL / BROKEN}
- Stage 3 (pm):           Part 0 {PRESENT/ABSENT} | KEY CONCERNS Ref {PRESENT/ABSENT} | Lens Impact Ref {PRESENT/ABSENT} -> {COMPLETE / PARTIAL / BROKEN}
- Stage 4 (tpm):          Part 0 {PRESENT/ABSENT} | KEY CONCERNS Ref {PRESENT/ABSENT} | Lens Impact Ref {PRESENT/ABSENT} -> {COMPLETE / PARTIAL / BROKEN}
- Stage 5 (arch-board):   Part 0 {PRESENT/ABSENT} | KEY CONCERNS Ref {PRESENT/ABSENT} | Lens Impact Ref {PRESENT/ABSENT} -> {COMPLETE / PARTIAL / BROKEN}
- Stage 6 (exec-office):  Part 0 {PRESENT/ABSENT} | KEY CONCERNS Ref {PRESENT/ABSENT} | Lens Impact Ref {PRESENT/ABSENT} -> {COMPLETE / PARTIAL / BROKEN}

---

USAGE NOTES
--stage all: all 6 stages in sequence; produce INERTIA ANCHOR before Stage 1.
--stage {name}: single stage; produce INERTIA ANCHOR regardless; omit Part 1 if first stage.
--scope {group}: filter org.yaml to the named division or tribe.
AMEND: re-run a named stage; carry INERTIA ANCHOR and prior handoff packets forward.

---

## V-03 -- Output Format: Table-First Structured Findings

**Axis**: Output format -- prose findings vs. table-first structured findings
**Hypothesis**: Expressing findings as table rows with mandatory columns (F-ID | Severity
| Finding | Owner | Resolution) makes C-04 owner and resolution requirements a format
error when absent rather than a prose gap. A model filling a table must populate Owner
and Resolution cells; in prose it can omit them without the output looking incomplete.
Same hypothesis applies to cross-stage references and Prior-Stage Lens Impact as tables.

---

You are running a Review of Business (ROB) for: {{topic}}

INPUTS
- Read org.yaml for stage role assignments.
- Read .craft/roles/<role-file>.md for each assigned persona.
- Arguments: --stage {all | leadership | teams | pm | tpm | arch-board | exec-office}
             --scope {group-name}
             AMEND: re-run a specific stage

STAGE SEQUENCE (default --stage all):
  Stage 1: leadership    Stage 2: teams    Stage 3: pm
  Stage 4: tpm           Stage 5: arch-board    Stage 6: exec-office

INERTIA ANCHOR (fill before Stage 1):
  What this topic displaces: {system or process being replaced}
  Cost-bearer: {team, role, or system absorbing the change}

---

## Stage Instructions

Produce every section in the order shown. Use table format for all structured data.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
(Before the briefing envelope at every stage, including Stage 1.)

| Field | Value |
|-------|-------|
| Role | {name} -- {title} |
| Dimension | {orientation in practice-domain terms. Examples: "schedule risk + dependency management" (TPM); "adoption risk + stakeholder readiness" (PM); "interface coupling + system boundaries" (Principal Architect). Role title alone is insufficient.} |

### Part 1 -- BRIEFING ENVELOPE
(Stages 2-6 only. Absent at Stage 1.)

| Field | Value |
|-------|-------|
| ROLE | {name} -- {title} |
| LENS | {same dimension as Part 0} |
| KEY CONCERNS | {2-4 concerns from prior stages, selected through the Lens declared in Part 0. Include the phrase "selected through the Lens declared in Part 0" in this cell.} |
| PRIOR-STAGE ESCALATIONS | {items escalated from prior handoff packets, or NONE} |

### Stage Identity
  Stage: {canonical-name}
  Role:  {name} -- {title}
  Lens:  {same dimension as Part 0}
  (At Stage 1, this is the sole Lens declaration. Must contain dimension, not just title.)

### Inertia Check
{State the status-quo pressure from this role's perspective relative to the INERTIA
ANCHOR. Name what the role's stakeholders are defending or resisting. At least 3 stages
must have a non-trivial Inertia Check that names a specific pressure.}

### Findings

| F-ID | Severity | Finding (specific concern -- not a domain name) | Owner (role) | Resolution (concrete action) |
|------|----------|-------------------------------------------------|--------------|------------------------------|
| F-01 | HIGH/MED/LOW | {specific concern naming the artifact or behavior} | {role} | {concrete action. "Needs attention" does not satisfy this column.} |
| F-02 | HIGH/MED/LOW | {specific concern} | {role} | {action} |

Minimum 2 rows per stage. All five columns must be populated.
At least 1 finding per stage must be grounded in the Part 0 Dimension -- a concern
specific to this role's practice orientation, not generic across all reviewers.

### Cross-Stage References
(Stages 2-6 only.)

| Source Stage | F-ID | Relationship | Note |
|--------------|------|--------------|------|
| {stage} | {F-ID} | confirms / escalates / contradicts | {why this stage's lens changes or confirms the prior finding} |

Minimum 2 backward references total across all stages in a multi-stage run.

### Prior-Stage Lens Impact
(Stages 2-6 only.)

| Source Stage | F-ID | How the Part 0 Orientation Changes the Reading | Relationship |
|--------------|------|------------------------------------------------|--------------|
| {stage} | {F-ID} | {explicit text naming "the orientation declared in Part 0" as the governing lens} | confirms / escalates / reframes |

### Stage Verdict
  Verdict: {APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED}
  Rationale: {cite at least one F-ID from the Findings table. One sentence.}

  tpm stage only -- top-level labeled signal:
  **TPM GO/NO-GO: {GO / GO WITH CONDITIONS / NO-GO}**
  Rationale: {cite specific F-ID or risk register row. One sentence.}

### Blocker Field
| BLOCKER | Blocking F-ID | Downstream Stage | Reason |
|---------|---------------|------------------|--------|
| YES / NO | {if YES} | {if YES} | {if YES: reason the downstream stage cannot proceed without resolution} |

### Handoff Packet

**Cross-Stage References Forwarded:**
| Source Stage | F-ID | Relationship |
|--------------|------|--------------|
| {stage} | {F-ID} | confirms / escalates / contradicts |

**Cross-Stage Synthesis** (must add substance beyond the table above):
{Characterize the downstream significance of the cross-stage picture. Do not copy table
rows into prose. Acceptable additions: pattern across multiple rows; risk escalation
beyond any single row; downstream action not captured in any individual row.}

**Downstream Risk Shift** (do not restate from Prior-Stage Lens Impact):
{Name a failure mode or ownership gap newly visible from this stage's vantage point.
Net-new visibility -- not a re-reading of prior findings through the Part 0 lens.}

---

## ROB Summary

Produce after all stages complete.

  **Overall Verdict:** {APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED}
  **Rationale:** 1-2 sentences citing the dominant cross-stage pattern.

### Cross-Cutting Themes
| Theme | Stages That Surfaced It | Why Recurrence Elevates Severity |
|-------|--------------------------|----------------------------------|
| {name} | {stage(s)} | {explain the pattern -- not a copy of any individual finding} |
Minimum 1 row if any concern appears in 2+ stages.

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
Minimum 3 rows. At least 1 HIGH severity. Prose-only summaries do not satisfy this.

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace Path to Artifact | Verdict |
|---------------------------------|------------------------|---------|
At least 1 row. Mission must be named by actual title, not paraphrased.

### LENS ACTIVATION CHAIN HEALTH
| Stage | Part 0 | KEY CONCERNS Ref Part 0 | Lens Impact Ref Part 0 | Chain Status |
|-------|--------|-------------------------|------------------------|--------------|
| Stage 1 (leadership) | PRESENT/ABSENT | N/A (no envelope) | N/A (first stage) | COMPLETE / PARTIAL / BROKEN |
| Stage 2 (teams) | PRESENT/ABSENT | PRESENT/ABSENT | PRESENT/ABSENT | COMPLETE / PARTIAL / BROKEN |
| Stage 3 (pm) | PRESENT/ABSENT | PRESENT/ABSENT | PRESENT/ABSENT | COMPLETE / PARTIAL / BROKEN |
| Stage 4 (tpm) | PRESENT/ABSENT | PRESENT/ABSENT | PRESENT/ABSENT | COMPLETE / PARTIAL / BROKEN |
| Stage 5 (arch-board) | PRESENT/ABSENT | PRESENT/ABSENT | PRESENT/ABSENT | COMPLETE / PARTIAL / BROKEN |
| Stage 6 (exec-office) | PRESENT/ABSENT | PRESENT/ABSENT | PRESENT/ABSENT | COMPLETE / PARTIAL / BROKEN |

---

USAGE NOTES
--stage all: all 6 stages in sequence; produce ROB Summary at the end.
--stage {name}: single stage; omit Part 1 if no prior stages; all tables still required.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage using prior outputs as context.

---

## V-04 -- Fill-Slot + Prominent Inertia (V-01 + V-02)

**Axes**: Phrasing register (fill-slot) + Inertia framing (prominent status-quo competitor)
**Hypothesis**: Combining fill-slot structural enforcement with a named Displacement Map
creates the strongest C-13 compliance path: the anchor provides concrete referents that
each INERTIA CHECK [fill] slot must cite, preventing both omission (slot is visibly blank)
and generic output (slot must reference a specific map entry). Together these two axes
also increase C-02 compliance because the Part 0 Dimension slot plus the Inertia Check
slot form a dual grounding mechanism for role-loaded findings.

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

Fill before Stage 1. Every slot must contain substantive content.

  Status-Quo Competitor:
  [fill: name the system, process, or approach this topic displaces -- not the topic
  itself, but what the topic replaces or competes with for adoption]

  Displacement Entries (fill minimum 2):
    D-01: Displaced element: [fill] | Cost-bearer: [fill: team, role, or system] | Change type: [fill: migration / behavior change / tooling switch / process change]
    D-02: Displaced element: [fill] | Cost-bearer: [fill] | Change type: [fill]
    [Additional entries as warranted]

  Inertia Risk Statement:
  [fill: one sentence naming the strongest single source of status-quo resistance -- the
  displacement entry most likely to create adoption friction or political resistance]

---

## Stage Template

Fill every [fill] slot. A visible unfilled slot is non-compliant.

---

## Stage {N}: {canonical-name} -- {Role Name}

### Part 0 -- LENS ACTIVATION
Fill this block before reading any prior-stage context.

  Role:      [fill: role name and title from .craft/roles/]
  Dimension: [fill: orientation in practice-domain terms. Name the lens dimension, not
    just the role title.
    Acceptable: "schedule risk + dependency management" | "adoption risk + stakeholder
    readiness" | "interface coupling + system boundary integrity" | "mission alignment +
    resource cascade"
    Not acceptable: "TPM perspective" or role title alone.]

### Part 1 -- BRIEFING ENVELOPE
(Fill for Stages 2-6. Absent at Stage 1.)

  ROLE:     [fill: name -- title]
  LENS:     [fill: same dimension as Part 0]
  KEY CONCERNS: [fill: 2-4 concerns from prior stages, selected through the Lens
    declared in Part 0. This slot must contain the explicit phrase "selected through the
    Lens declared in Part 0." Do not copy prior findings verbatim.]
  PRIOR-STAGE ESCALATIONS: [fill: items explicitly escalated from prior handoff packets,
    or NONE]

### Stage Identity
  Stage: {canonical-name}
  Role:  [fill: name -- title]
  Lens:  [fill: same dimension as Part 0]
  (At Stage 1, this Lens: line is the sole lens declaration for this stage. It must
  contain the dimension, not just the role name.)

### Inertia Check
From the INERTIA ANCHOR, identify the Displacement Entry most relevant to this role.
This slot must cite a specific D-ID entry -- generic statements do not satisfy this slot.

  Displacement Entry Referenced: [fill: D-{ID} -- {displaced element name}]
  Status-Quo Pressure: [fill: what this role's stakeholders are defending; what the role
    risks if the topic succeeds; what it costs the role if the topic fails. Not "change
    is hard." Name the concrete pressure from the cited displacement entry.]
  Inertia Stance: [fill: RESISTANT / NEUTRAL / ALIGNED]
  Stance Rationale: [fill: one sentence explaining the posture]

  Constraints:
  - At least 3 of the 6 stages must have a non-trivial Inertia Check (citing a specific
    D-ID and naming a concrete stakeholder pressure).
  - When Inertia Stance is RESISTANT and any finding is HIGH severity, at least one
    finding in this stage must reference the inertia contribution as a factor.

### Findings
Minimum 2 findings per stage. Each names a specific artifact or concern under review.

  F-01 [HIGH/MED/LOW]: [fill: specific concern -- not a domain category]. Owner: [fill:
    role]. Resolution: [fill: concrete action that resolves the concern].
  F-02 [HIGH/MED/LOW]: [fill]. Owner: [fill]. Resolution: [fill].
  [Additional findings as warranted]

  Constraint: At least one finding per stage must be grounded in the Part 0 Dimension --
  the concern must be specific to this role's practice orientation, not generic.

### Cross-Stage References
(Stages 2-6 only. Minimum 2 backward references total across all stages.)

  - [source stage] [F-ID]: [confirms / escalates / contradicts] -- [fill: note]

### Prior-Stage Lens Impact
(Stages 2-6 only.)

  - [source stage] [F-ID]: [fill: how this finding reads differently through the
    orientation declared in Part 0. Name "the orientation declared in Part 0" explicitly.]
    -- [confirms / escalates / reframes]

### Stage Verdict
  Verdict:   [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: cite at least one F-ID. One sentence.]

  tpm stage only:
  **TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**
  Rationale: [fill: cite specific F-ID or risk entry. One sentence.]

### Blocker Field
  BLOCKER: [fill: YES / NO]
  [If YES: fill -- blocking F-ID | downstream stage blocked | reason the downstream stage
  cannot proceed without resolution]

### Handoff Packet

  Cross-Stage References Forwarded:
  [fill: list each forwarded reference with source stage, F-ID, and relationship type]

  Cross-Stage Synthesis:
  [fill: characterize the downstream significance of the collected cross-stage picture.
  Must add substance not already stated in Cross-Stage References Forwarded above.
  Acceptable: pattern across multiple references; risk escalation beyond any single
  reference; downstream action not stated in any individual reference. Do not copy.]

  Downstream Risk Shift:
  [fill: name a failure mode or ownership gap newly visible from this stage's vantage
  point. Do not restate Prior-Stage Lens Impact -- that slot names how prior work reads
  differently through this role's lens; this slot names what is net-new visible here.]

---

## ROB Summary

After all stages complete, fill this section.

  Overall Verdict: [fill: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
  Rationale: [fill: 1-2 sentences citing the dominant cross-stage pattern]

### Inertia Resolution Status
For each Displacement Entry from the INERTIA ANCHOR:
[fill: D-{ID} {element}] -- surfaced at: [fill: stage(s)] -- status: [fill: RESOLVED / OPEN / ESCALATED]
(Minimum 2 entries matching the INERTIA ANCHOR.)

### Cross-Cutting Themes
[fill: name each concern that appeared independently in 2+ stages. For each: cite the
stages; explain why recurrence elevates severity beyond any single-stage instance. Do not
copy individual findings verbatim. Minimum 1 theme if any concern recurs.]

### Risk Register (tpm stage only)
| Risk Title | Severity | Likelihood | Mitigation |
|------------|----------|------------|------------|
| [fill]     | HIGH/MED/LOW | HIGH/MED/LOW | [fill: concrete action] |
(Minimum 3 rows. At least 1 HIGH severity.)

### Mission Cascade (exec-office stage only)
| S-Office Mission (actual title) | Trace to Artifact | Verdict |
|---------------------------------|------------------|---------|
| [fill: actual title -- not "strategic priorities"] | [fill] | ALIGNED / PARTIAL / GAP |
(Minimum 1 row.)

### LENS ACTIVATION CHAIN HEALTH
[fill: report per-stage chain status for all stages in the run]
- Stage 1 (leadership):   Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [N/A -- no envelope at Stage 1] | Lens Impact [N/A -- first stage] -> Chain: [COMPLETE / PARTIAL / BROKEN]
- Stage 2 (teams):        Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
- Stage 3 (pm):           Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
- Stage 4 (tpm):          Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
- Stage 5 (arch-board):   Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]
- Stage 6 (exec-office):  Part 0 [PRESENT/ABSENT] | KEY CONCERNS Ref [PRESENT/ABSENT] | Lens Impact Ref [PRESENT/ABSENT] -> Chain: [COMPLETE / PARTIAL / BROKEN]

---

USAGE NOTES
--stage all: all 6 stages in sequence. Fill INERTIA ANCHOR, all stage templates, ROB Summary.
--stage {name}: single stage. Fill INERTIA ANCHOR. Omit Part 1 if no prior stages.
--scope {group}: filter org.yaml to named division or tribe.
AMEND: re-run a named stage. Carry INERTIA ANCHOR and prior handoff packets forward.

---

## V-05 -- Fill-Slot + Prominent Inertia + Table-First (All Three Axes)

**Axes**: Phrasing register (fill-slot) + Inertia framing (prominent) + Output format
(table-first)
**Hypothesis**: The three axes are mutually reinforcing. Fill slots make omissions
visible; the Displacement Map gives each inertia slot a concrete referent; table columns
make C-04 owner/resolution a format requirement. Together they represent the maximum
structural enforcement design: every criterion that can be reduced to a slot or column
is given a slot or column, leaving the executing model no silent escape from structural
compliance. This is the candidate for highest raw aspirational count under v5 because
the table format for LENS ACTIVATION CHAIN HEALTH makes per-stage chain status
(C-23) a visible fill-row rather than a prose paragraph.

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
A visible unfilled slot or an empty table where content is required indicates
non-compliance.

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
| F-01 | HIGH/MED/LOW | [fill] | [fill] | [fill. "Needs attention" does not satisfy this column.] |
| F-02 | HIGH/MED/LOW | [fill] | [fill] | [fill] |
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
