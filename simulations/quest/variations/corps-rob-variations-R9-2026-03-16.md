Written to `simulations/quest/variations/corps-rob-variations-R9-2026-03-16.md`.

---

## Variate R9 -- corps-rob Summary

**Baseline**: R8 V-05 scores **170** under v9 rubric. Six failing criteria, 35 pts of headroom. Max = 205.

### Variation axes

| Variation | Axis | Targets | Predicted score |
|-----------|------|---------|----------------|
| **V-01** | RULE CARRY-FORWARD -- per-stage carry block naming upstream findings by stage+ID | C-06 | **180** |
| **V-02** | Enforcement format richness -- Update Protocol block + stage-per-row tables in audit sections | C-15, C-20 | **180** |
| **V-03** | SYNTHESIS section -- BLOCKERS subsection + CROSS-CUTTING THEMES subsection | C-09, C-10 | **180** |
| **V-04** | Carry forward + RULE CONDITIONAL-ITEM (enumerated conditions in conditional verdicts) | C-06, C-11 | **185** |
| **V-05** | Full R9 stack: all six axes on R8 V-05 base | C-06, C-09, C-10, C-11, C-15, C-20 | **205** |

### Key structural decisions

**RULE CARRY-FORWARD** (C-06): mandatory CARRY FORWARD section per stage (except the first), placed before Calibration. Cross-stage references are labeled artifacts, not prose accidents. CARRY: NONE is the zero-state.

**RULE AUDIT-TABLE** (C-20): stage-per-row table inserted above each existing AUDIT RESULT block. The AUDIT RESULT block is explicitly preserved (C-29 not voided). Both coexist inside the same section.

**RULE SYNTHESIS** (C-09, C-10): declared as a summary-level artifact, not an audit dimension -- so it does not count toward RULE AUDIT-SUITE's three sections and does not trigger ANTI-PATTERN-1 or ANTI-PATTERN-2.

**RULE CONDITIONAL-ITEM** (C-11): explicitly named as distinct from RULE CONDITION-ENUM (audit schema enumeration) to prevent model conflation.

**C-30 and C-31 preserved** in all variations: preamble schemas remain in the preamble, rule citation anchors remain in post-stage section headers.
on naming any preceding-stage finding that bears on this stage's scope,
by upstream stage name and finding ID. In a 6-stage --stage all run, pm through exec-office
each carry at least one reference site; the pm-to-teams and tpm-to-pm pair reliably
produces the 2+ named cross-stage references C-06 requires. CARRY: NONE is the zero-state
when nothing carries (RULE ZERO-STATE applies). All R8 V-05 passing criteria preserved:
preamble schemas (C-30), rule citation anchors (C-31), RULE AUDIT-SUITE (C-24, C-26),
per-condition AUDIT RESULT blocks (C-29).

**V-02**: C-15 requires Update Protocol with trigger events, owner role, and revisit cadence
-- a contained addition to TPM, no structural disruption elsewhere. C-20 requires
enforcement audit sections to use a 4-column table; a stage-per-row table is added above
each section's existing AUDIT RESULT block, satisfying C-20 without removing the per-
condition enumeration (C-29). Three RULE AUDIT-SUITE sections remain independent (C-24, C-26
preserved). Preamble schemas (C-30) and header rule citations (C-31) unchanged.

**V-03**: C-09 requires at least 1 inter-stage blocker named with upstream stage, finding ID,
and downstream stage impact. C-10 requires at least 1 cross-cutting theme named at document
level in a Synthesis section, citing 2+ stages with severity elevation explanation. A SYNTHESIS
section placed after stages and before POST-STAGE AUDIT SUITE satisfies both. SYNTHESIS is not
an audit section and does not count toward RULE AUDIT-SUITE's three required sections -- it is
a summary-level analysis artifact declared by RULE SYNTHESIS. ANTI-PATTERN-2 is not triggered
because SYNTHESIS covers cross-stage patterns, a different scope from calibration/role-concern/
triage-note. Both subsections apply RULE ZERO-STATE.

**V-04**: C-11 requires that APPROVED WITH CONDITIONS verdicts enumerate conditions as numbered
items each with owner and finding/risk reference. Combined with RULE CARRY-FORWARD (C-06),
these reinforce each other: upstream findings enter carry blocks (cross-stage references),
unresolved carries become conditional verdict items. RULE CONDITIONAL-ITEM is named distinctly
from RULE CONDITION-ENUM (audit schema enumeration) to prevent model confusion.

**V-05**: All six axes stacked on R8 V-05 base. Additions live in structurally distinct
locations: C-06 in CARRY FORWARD sections, C-11 in Verdict format, C-15 in TPM risk register,
C-09+C-10 in SYNTHESIS, C-20 in audit section tables. Named rules prevent collapse under
generation pressure: RULE CARRY-FORWARD, RULE CONDITIONAL-ITEM, RULE SYNTHESIS, RULE
AUDIT-TABLE. Preamble schemas (C-30) and rule citation anchors in section headers (C-31)
preserved from R8 V-05 base. Predicted composite: 205.

---

## V-01 -- Cross-Stage Coherence via RULE CARRY-FORWARD

**Axis**: RULE CARRY-FORWARD added as a run-level rule; each stage after the first
includes a CARRY FORWARD section (before Calibration) naming upstream findings relevant
to this stage's scope by stage name and finding ID.
**Hypothesis**: C-06 requires at least 2 cross-stage references in a multi-stage run,
each naming the upstream stage and finding ID. R8 V-05 contains no referencing instruction;
downstream stages write independently. RULE CARRY-FORWARD with a mandatory labeled section
ensures references appear as verifiable artifacts, not incidentally in prose. The section
placement before Calibration lets the current stage's calibration account for escalations.
In a --stage all run, five stages (teams through exec-office) each have a CARRY FORWARD
site; the pm-to-teams and tpm-to-pm pair satisfies the minimum of 2 even if others write
CARRY: NONE. CARRY FORWARD is a per-stage section -- it is not one of the three RULE
AUDIT-SUITE post-stage sections, so C-24 and C-26 are not affected.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RUN-LEVEL SCHEMAS AND RULES**

The following schemas and rules are declared at run level. All post-stage audit sections
reference these declarations by name rather than redeclaring them.

**TRIAGE NOTE AUDIT SCHEMA** (run-level declaration):

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

**ROLE CONCERN AUDIT SCHEMA** (run-level declaration):

```
ROLE CONCERN AUDIT SCHEMA:
  Condition (a): Role Concern block is absent from the stage
  Condition (b): Role Concern block is present but contains a generic description
                 that does not reference the specific artifact, domain, or risk area
                 under review
```

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement scan
must include an explicit zero-state declaration when the check finds no issues. The
declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section
that ends after confirming clean status without this line is ambiguous.

**RULE CONDITION-ENUM:** Any audit result block that applies a named schema with labeled
conditions must enumerate each condition's result independently. An aggregate NONE
declaration violates RULE CONDITION-ENUM even if the check is clean.

```
RULE CONDITION-ENUM:
  Required form (clean run):
    (a) [condition label]: NONE
    (b) [condition label]: NONE
    [(c) [condition label]: NONE  -- if schema has a third condition]
    [SECTION LABEL]: NONE

  VIOLATION [AGGREGATE-NONE]:
  A single "SECTION LABEL: NONE" without per-condition enumeration does not satisfy
  RULE CONDITION-ENUM. The reader cannot confirm each condition was checked independently.
```

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. Absence of either section is a FORMAT VIOLATION making the run incomplete.

```
MANDATORY GAP-SCAN SECTIONS:
  Section 1 -- ROLE CONCERN GAPS: absence = FORMAT VIOLATION
  Section 2 -- TRIAGE NOTE GAPS: absence = FORMAT VIOLATION
```

**RULE AUDIT-SUITE:** After all stages are complete, produce a Post-Stage Audit Suite
containing at least three independent sections, each covering a distinct pre-commitment
dimension.

```
RULE AUDIT-SUITE:
  Requirement: >= 3 independent post-stage audit sections, each covering a single
  pre-commitment dimension, each with its own zero-state under RULE ZERO-STATE.

  ANTI-PATTERN-1 [MERGED SECTION]:
  A single section combining multiple pre-commitment dimensions under one header does
  not satisfy RULE AUDIT-SUITE. Section isolation required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three sections auditing the same pre-commitment dimension at different granularity
  do not satisfy RULE AUDIT-SUITE. Scope diversity is structural, not a quality preference.
```

Required dimensions:
1. Calibration compliance -- findings match declared Calibration Block spread
2. Role-concern compliance -- each stage has topic-specific role-concern declaration
3. Triage note compliance -- each stage has Triage Note with all fields checked using
   TRIAGE NOTE AUDIT SCHEMA (preamble declaration applies)

**RULE CARRY-FORWARD:** In any multi-stage run, each stage after the first must include a
CARRY FORWARD section before the Calibration block. The section names any finding from a
preceding stage that bears on this stage's scope, referencing the upstream stage by name
and the finding by ID.

```
RULE CARRY-FORWARD:
  Requirement: Every stage except the first includes a CARRY FORWARD section. Each
  referenced entry names the upstream stage (e.g., "teams") and finding ID (e.g., "F-02"),
  plus a statement of what this stage does with it (escalates / confirms unresolved /
  resolves / registers as risk).

  At least two cross-stage references must appear across the full multi-stage run.

  When no preceding-stage finding bears on this stage's scope:
  CARRY: NONE  (RULE ZERO-STATE applies)
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain.
               PASSES: names the concern and the artifact.
               FAILS: generic description ("A PM cares about alignment")]

### Carry Forward
[RULE CARRY-FORWARD applies -- omit this section for the first stage in the sequence only]

[For each preceding-stage finding relevant to this stage's scope:
   From [upstream stage] [F-NN]: [brief concern] -- [this stage's action: escalate /
   confirm unresolved / resolve / register as risk]]

CARRY: NONE
[required if no upstream findings bear on this stage; RULE ZERO-STATE applies]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; severity must match declared spread]

### Triage Note

HIGH DRIVER:         [the specific finding ranked most critical -- name it and explain
                      what property drove the HIGH assignment from this role's perspective]
LOW ANCHOR:          [the specific finding ranked least critical -- name it and explain
                      what property demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension that shaped the full spread --
                      not a placeholder; specific to this stage's risk landscape]

[All three field labels required; present in every stage unconditionally]
[Placeholder content in any field triggers Condition (c) of TRIAGE NOTE AUDIT SCHEMA]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk -- named]    | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk -- named]    | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk -- named]    | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE**

After all stages, produce three independent sections (RULE AUDIT-SUITE applies --
ANTI-PATTERN-1 and ANTI-PATTERN-2 prohibit merging or repeating dimensions):

```
## Calibration Compliance

[For each stage that declared a Calibration Block spread, list any stage where the
 actual severity distribution of findings deviated from the declared spread.]

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with declared vs. actual spread]
```

```
## Role Concern Compliance
[Applies ROLE CONCERN AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b)
 -- If (b): quote the generic content]

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE
```

```
## Triage Note Compliance
[Applies TRIAGE NOTE AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b) / (c)
 -- If (b): which field label is missing
 -- If (c): which field label has placeholder content]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).

---

## V-02 -- Enforcement Format Richness (Update Protocol + Audit Table)

**Axis**: Two independent additions to the enforcement format: (1) a Risk Register Update
Protocol block in the TPM stage specifying trigger events, owner role, and revisit cadence
(C-15); (2) a stage-per-row table added above each audit section's existing AUDIT RESULT
block, using Stage / Pre-Commitment / Honored / Deviation columns (C-20).
**Hypothesis**: C-15 is a contained TPM-only addition with no structural effect on other
sections. C-20 requires the enforcement audit to use a structured table; inserting a
stage-per-row table above each section's AUDIT RESULT block satisfies C-20 without
removing the per-condition enumeration required by C-29 -- both coexist in the same
section (table for C-20, AUDIT RESULT block for C-29). The three RULE AUDIT-SUITE sections
remain independent (C-24, C-26 preserved). Key risk: the table's Deviation column must
not replace the AUDIT RESULT's per-condition enumeration -- the AUDIT RESULT block must
still appear beneath the table. Preamble schemas (C-30) and section header rule citations
(C-31) unchanged.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RUN-LEVEL SCHEMAS AND RULES**

The following schemas and rules are declared at run level. All post-stage audit sections
reference these declarations by name rather than redeclaring them.

**TRIAGE NOTE AUDIT SCHEMA** (run-level declaration):

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

**ROLE CONCERN AUDIT SCHEMA** (run-level declaration):

```
ROLE CONCERN AUDIT SCHEMA:
  Condition (a): Role Concern block is absent from the stage
  Condition (b): Role Concern block is present but contains a generic description
                 that does not reference the specific artifact, domain, or risk area
                 under review
```

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement scan
must include an explicit zero-state declaration when the check finds no issues. The
declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section
that ends after confirming clean status without this line is ambiguous.

**RULE CONDITION-ENUM:** Any audit result block that applies a named schema with labeled
conditions must enumerate each condition's result independently. An aggregate NONE
declaration violates RULE CONDITION-ENUM even if the check is clean.

```
RULE CONDITION-ENUM:
  Required form (clean run):
    (a) [condition label]: NONE
    (b) [condition label]: NONE
    [(c) [condition label]: NONE  -- if schema has a third condition]
    [SECTION LABEL]: NONE

  VIOLATION [AGGREGATE-NONE]:
  A single "SECTION LABEL: NONE" without per-condition enumeration does not satisfy
  RULE CONDITION-ENUM.
```

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. Absence of either section is a FORMAT VIOLATION making the run incomplete.

```
MANDATORY GAP-SCAN SECTIONS:
  Section 1 -- ROLE CONCERN GAPS: absence = FORMAT VIOLATION
  Section 2 -- TRIAGE NOTE GAPS: absence = FORMAT VIOLATION
```

**RULE AUDIT-SUITE:** After all stages are complete, produce a Post-Stage Audit Suite
containing at least three independent sections, each covering a distinct pre-commitment
dimension.

```
RULE AUDIT-SUITE:
  Requirement: >= 3 independent post-stage audit sections, each covering a single
  pre-commitment dimension, each with its own zero-state under RULE ZERO-STATE.

  ANTI-PATTERN-1 [MERGED SECTION]:
  A single section combining multiple pre-commitment dimensions does not satisfy
  RULE AUDIT-SUITE. Section isolation required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three sections auditing the same dimension at different granularity do not satisfy
  RULE AUDIT-SUITE. Scope diversity is structural, not a quality preference.
```

Required dimensions:
1. Calibration compliance -- findings match declared Calibration Block spread
2. Role-concern compliance -- each stage has topic-specific role-concern declaration
3. Triage note compliance -- each stage has Triage Note with all fields checked using
   TRIAGE NOTE AUDIT SCHEMA (preamble declaration applies)

**RULE AUDIT-TABLE:** Each section in the Post-Stage Audit Suite must contain a stage-per-row
table above its AUDIT RESULT block. The table must have at least four named columns.

```
RULE AUDIT-TABLE:
  Required columns: Stage | Pre-Commitment | Honored | Deviation
  Required: one row per stage in the run.
  Required: the AUDIT RESULT block still appears beneath the table (RULE CONDITION-ENUM applies).

  VIOLATION [PROSE-ONLY]:
  An audit section that lists compliance findings in prose without a structured table
  does not satisfy RULE AUDIT-TABLE even if the content is otherwise correct.
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain.
               PASSES: names the concern and the artifact.
               FAILS: generic description ("A PM cares about alignment")]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; severity must match declared spread]

### Triage Note

HIGH DRIVER:         [the specific finding ranked most critical -- name it and explain
                      what property drove the HIGH assignment from this role's perspective]
LOW ANCHOR:          [the specific finding ranked least critical -- name it and explain
                      what property demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension that shaped the full spread --
                      not a placeholder; specific to this stage's risk landscape]

[All three field labels required; present in every stage unconditionally]
[Placeholder content in any field triggers Condition (c) of TRIAGE NOTE AUDIT SCHEMA]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk -- named]    | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk -- named]    | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk -- named]    | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Update Protocol

TRIGGER EVENTS:   [events or milestones requiring a status update -- specific to this run's
                   risks, e.g., "mitigation action confirmed complete by owner", "milestone
                   gate passed", "risk condition no longer active"]
UPDATE OWNER:     [role responsible for updating risk status after each trigger event --
                   by role, not by person name]
REVISIT CADENCE:  [when the register is reviewed -- e.g., "weekly tpm sync before sprint
                   commit", "at milestone -1 week", "before each go/no-go gate"]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE + RULE AUDIT-TABLE**

After all stages, produce three independent sections. Each section contains a stage-per-row
table (RULE AUDIT-TABLE) above its AUDIT RESULT block (RULE CONDITION-ENUM). Sections must
be independent -- not merged (ANTI-PATTERN-1), not repeating scope (ANTI-PATTERN-2):

```
## Calibration Compliance
[RULE AUDIT-TABLE applies]

| Stage       | Pre-Commitment (Planned Spread)     | Honored | Deviation |
|-------------|-------------------------------------|---------|-----------|
| [stage]     | [N findings: X HIGH, Y MED, Z LOW]  | YES     | NONE      |
...

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with declared vs. actual spread]
```

```
## Role Concern Compliance
[Applies ROLE CONCERN AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE AUDIT-TABLE applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

| Stage       | Pre-Commitment (Role Concern block)          | Honored | Deviation |
|-------------|----------------------------------------------|---------|-----------|
| [stage]     | topic-specific role-concern declaration      | YES     | NONE      |
...

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE
```

```
## Triage Note Compliance
[Applies TRIAGE NOTE AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE AUDIT-TABLE applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

| Stage       | Pre-Commitment (Triage Note: 3 named fields)           | Honored | Deviation |
|-------------|--------------------------------------------------------|---------|-----------|
| [stage]     | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR populated | YES     | NONE      |
...

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).

---

## V-03 -- Synthesis Section (Blockers + Cross-Cutting Themes)

**Axis**: A mandatory SYNTHESIS section placed after all stages and before the Post-Stage
Audit Suite, containing two subsections: BLOCKERS (satisfying C-09) and CROSS-CUTTING
THEMES (satisfying C-10). Both subsections use RULE ZERO-STATE for their clean states.
**Hypothesis**: C-09 requires at least 1 inter-stage blocker named with upstream stage,
finding ID, and downstream stage impact. C-10 requires at least 1 cross-cutting theme
named at document level citing 2+ stages with severity elevation explanation. RULE SYNTHESIS
declares SYNTHESIS as a summary-level analysis artifact -- not an audit section -- so it
does not count toward RULE AUDIT-SUITE's three required sections and does not trigger
ANTI-PATTERN-1 (merging) or ANTI-PATTERN-2 (scope repetition). The BLOCKERS subsection
satisfies C-09's explicit blocker format requirement; CROSS-CUTTING THEMES satisfies C-10's
requirement for a named document-level theme with stage citations. In a multi-stage run
where every stage is well-formed, the SYNTHESIS section makes cross-stage analysis a
first-class artifact rather than an incidental observation.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RUN-LEVEL SCHEMAS AND RULES**

The following schemas and rules are declared at run level. All post-stage audit sections
reference these declarations by name rather than redeclaring them.

**TRIAGE NOTE AUDIT SCHEMA** (run-level declaration):

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

**ROLE CONCERN AUDIT SCHEMA** (run-level declaration):

```
ROLE CONCERN AUDIT SCHEMA:
  Condition (a): Role Concern block is absent from the stage
  Condition (b): Role Concern block is present but contains a generic description
                 that does not reference the specific artifact, domain, or risk area
                 under review
```

**RULE ZERO-STATE:** Every section that performs an audit, gap check, enforcement scan,
or synthesis subsection must include an explicit zero-state declaration when it finds no
issues. The declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`.

**RULE CONDITION-ENUM:** Any audit result block that applies a named schema with labeled
conditions must enumerate each condition's result independently. An aggregate NONE
declaration violates RULE CONDITION-ENUM even if the check is clean.

```
RULE CONDITION-ENUM:
  Required form (clean run):
    (a) [condition label]: NONE
    (b) [condition label]: NONE
    [(c) [condition label]: NONE  -- if schema has a third condition]
    [SECTION LABEL]: NONE

  VIOLATION [AGGREGATE-NONE]:
  A single "SECTION LABEL: NONE" without per-condition enumeration does not satisfy
  RULE CONDITION-ENUM.
```

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. Absence of either section is a FORMAT VIOLATION making the run incomplete.

```
MANDATORY GAP-SCAN SECTIONS:
  Section 1 -- ROLE CONCERN GAPS: absence = FORMAT VIOLATION
  Section 2 -- TRIAGE NOTE GAPS: absence = FORMAT VIOLATION
```

**RULE AUDIT-SUITE:** After all stages are complete, produce a Post-Stage Audit Suite
containing at least three independent sections, each covering a distinct pre-commitment
dimension.

```
RULE AUDIT-SUITE:
  Requirement: >= 3 independent post-stage audit sections, each covering a single
  pre-commitment dimension, each with its own zero-state under RULE ZERO-STATE.

  ANTI-PATTERN-1 [MERGED SECTION]:
  A single section combining multiple pre-commitment dimensions does not satisfy
  RULE AUDIT-SUITE. Section isolation required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three sections auditing the same dimension at different granularity do not satisfy
  RULE AUDIT-SUITE. Scope diversity is structural, not a quality preference.
```

Required dimensions:
1. Calibration compliance -- findings match declared Calibration Block spread
2. Role-concern compliance -- each stage has topic-specific role-concern declaration
3. Triage note compliance -- each stage has Triage Note with all fields checked using
   TRIAGE NOTE AUDIT SCHEMA (preamble declaration applies)

**RULE SYNTHESIS:** After all stages are complete and before the Post-Stage Audit Suite,
produce a mandatory SYNTHESIS section. SYNTHESIS is a summary-level analysis artifact --
not an audit dimension, not counted toward RULE AUDIT-SUITE's three required sections.

```
RULE SYNTHESIS:
  Subsection 1 -- BLOCKERS
    Identify any finding from an upstream stage that creates a hard blocker for a
    downstream stage -- a finding that prevents the downstream stage from reaching
    a verdict without resolution. For each blocker:
      - Upstream stage and finding ID (or description)
      - Downstream stage affected
      - The impact: what cannot proceed without resolution
    Zero-state: BLOCKERS: NONE  (RULE ZERO-STATE applies if no blockers exist)

  Subsection 2 -- CROSS-CUTTING THEMES
    Identify any concern that surfaces in 2 or more stages. For each theme:
      - Name it at document level (distinct from any single stage finding)
      - Cite the stages and finding IDs where it appeared
      - Explain why repetition across stages increases severity above the per-stage level
    Zero-state: CROSS-CUTTING THEMES: NONE  (RULE ZERO-STATE applies if no themes exist)
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain.
               PASSES: names the concern and the artifact.
               FAILS: generic description ("A PM cares about alignment")]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; severity must match declared spread]

### Triage Note

HIGH DRIVER:         [the specific finding ranked most critical -- name it and explain
                      what property drove the HIGH assignment from this role's perspective]
LOW ANCHOR:          [the specific finding ranked least critical -- name it and explain
                      what property demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension that shaped the full spread --
                      not a placeholder; specific to this stage's risk landscape]

[All three field labels required; present in every stage unconditionally]
[Placeholder content in any field triggers Condition (c) of TRIAGE NOTE AUDIT SCHEMA]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk -- named]    | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk -- named]    | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk -- named]    | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**SYNTHESIS -- RULE SYNTHESIS (required after all stages, before Post-Stage Audit Suite)**

```
## Synthesis

### Blockers
[RULE SYNTHESIS applies]

[For each finding that creates a hard blocker for a downstream stage:]

  Upstream: [stage] [F-NN] -- [concern description]
  Downstream: [stage] -- [what cannot proceed without resolution]

BLOCKERS: NONE
[required if no cross-stage blockers exist; RULE ZERO-STATE applies]

### Cross-Cutting Themes
[RULE SYNTHESIS applies]

[For each concern appearing in 2+ stages:]

THEME-[NN]: [name -- distinct from any individual stage finding]
  Stages: [stage1] ([F-NN]), [stage2] ([F-NN])
  Severity elevation: [why appearance in N stages increases priority above the per-stage finding]

CROSS-CUTTING THEMES: NONE
[required if no concern appears in 2+ stages; RULE ZERO-STATE applies]
```

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE**

After Synthesis, produce three independent sections (RULE AUDIT-SUITE applies --
ANTI-PATTERN-1 and ANTI-PATTERN-2 prohibit merging or repeating dimensions):

```
## Calibration Compliance

[For each stage that declared a Calibration Block spread, list any stage where the
 actual severity distribution of findings deviated from the declared spread.]

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with declared vs. actual spread]
```

```
## Role Concern Compliance
[Applies ROLE CONCERN AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b)
 -- If (b): quote the generic content]

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE
```

```
## Triage Note Compliance
[Applies TRIAGE NOTE AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b) / (c)
 -- If (b): which field label is missing
 -- If (c): which field label has placeholder content]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).

---

## V-04 -- Carry Forward + Conditional Verdict Enumeration

**Axis**: RULE CARRY-FORWARD (from V-01) combined with RULE CONDITIONAL-ITEM, which
requires APPROVED WITH CONDITIONS and GO WITH CONDITIONS verdicts to enumerate their
conditions as numbered items, each naming what must happen, the owner role, and the
finding or risk reference.
**Hypothesis**: C-11 requires that at least one conditional verdict in the run lists
its conditions as >= 2 numbered items, each with (1) what must happen, (2) who owns it,
(3) finding/risk ID. The mechanism: RULE CONDITIONAL-ITEM declares the enumerated-item
format as a named run-level rule, making conditional verdicts machine-checkable at output
time. Combined with RULE CARRY-FORWARD (C-06), the two criteria reinforce each other
structurally: upstream unresolved findings appear in carry blocks (C-06 cross-stage
references), and when those findings prevent unconditional approval the verdict enumerates
resolution requirements (C-11). The escalation chain becomes: teams raises F-02 -> pm
carries it forward (cross-stage reference) -> pm issues APPROVED WITH CONDITIONS with
items 1. [resolve F-02] Owner: Teams Lead Ref: F-02 and 2. [confirm alignment] Owner:
PM Ref: F-03. RULE CONDITIONAL-ITEM is explicitly distinct from RULE CONDITION-ENUM
(which governs audit schema result blocks) to prevent conflation.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RUN-LEVEL SCHEMAS AND RULES**

The following schemas and rules are declared at run level. All post-stage audit sections
reference these declarations by name rather than redeclaring them.

**TRIAGE NOTE AUDIT SCHEMA** (run-level declaration):

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

**ROLE CONCERN AUDIT SCHEMA** (run-level declaration):

```
ROLE CONCERN AUDIT SCHEMA:
  Condition (a): Role Concern block is absent from the stage
  Condition (b): Role Concern block is present but contains a generic description
                 that does not reference the specific artifact, domain, or risk area
                 under review
```

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement scan
must include an explicit zero-state declaration when the check finds no issues. The
declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section
that ends after confirming clean status without this line is ambiguous.

**RULE CONDITION-ENUM:** Any audit result block that applies a named schema with labeled
conditions must enumerate each condition's result independently. An aggregate NONE
declaration violates RULE CONDITION-ENUM even if the check is clean.

```
RULE CONDITION-ENUM:
  Required form (clean run):
    (a) [condition label]: NONE
    (b) [condition label]: NONE
    [(c) [condition label]: NONE  -- if schema has a third condition]
    [SECTION LABEL]: NONE

  VIOLATION [AGGREGATE-NONE]:
  A single "SECTION LABEL: NONE" without per-condition enumeration does not satisfy
  RULE CONDITION-ENUM.
```

**RULE CONDITIONAL-ITEM:** [distinct from RULE CONDITION-ENUM] Any verdict of APPROVED
WITH CONDITIONS or GO WITH CONDITIONS must enumerate the conditions as numbered items
before the Rationale line.

```
RULE CONDITIONAL-ITEM:
  Requirement: A conditional verdict must list its conditions as numbered items.
  Each item states:
    (1) what must happen before approval is unconditional
    (2) the role responsible (by role, not by person name)
    (3) the finding or risk driving the condition (by ID or description)
  Minimum 2 items when verdict is conditional.

  Required form:
    VERDICT: APPROVED WITH CONDITIONS
    Conditions:
      1. [What must happen] -- Owner: [role] -- Ref: [F-NN or R-NN]
      2. [Second condition] -- Owner: [role] -- Ref: [F-NN or R-NN]
    Rationale: [one sentence citing a finding ID]

  VIOLATION [PROSE-CONDITIONS]:
  Conditions stated only within the Rationale prose do not satisfy RULE CONDITIONAL-ITEM.
  The conditions must be enumerated as discrete items before the Rationale line.
```

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. Absence of either section is a FORMAT VIOLATION making the run incomplete.

```
MANDATORY GAP-SCAN SECTIONS:
  Section 1 -- ROLE CONCERN GAPS: absence = FORMAT VIOLATION
  Section 2 -- TRIAGE NOTE GAPS: absence = FORMAT VIOLATION
```

**RULE AUDIT-SUITE:** After all stages are complete, produce a Post-Stage Audit Suite
containing at least three independent sections, each covering a distinct pre-commitment
dimension.

```
RULE AUDIT-SUITE:
  Requirement: >= 3 independent post-stage audit sections, each covering a single
  pre-commitment dimension, each with its own zero-state under RULE ZERO-STATE.

  ANTI-PATTERN-1 [MERGED SECTION]:
  A single section combining multiple pre-commitment dimensions does not satisfy
  RULE AUDIT-SUITE. Section isolation required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three sections auditing the same dimension at different granularity do not satisfy
  RULE AUDIT-SUITE. Scope diversity is structural, not a quality preference.
```

Required dimensions:
1. Calibration compliance -- findings match declared Calibration Block spread
2. Role-concern compliance -- each stage has topic-specific role-concern declaration
3. Triage note compliance -- each stage has Triage Note with all fields checked using
   TRIAGE NOTE AUDIT SCHEMA (preamble declaration applies)

**RULE CARRY-FORWARD:** In any multi-stage run, each stage after the first must include a
CARRY FORWARD section before the Calibration block. The section names any finding from a
preceding stage that bears on this stage's scope, referencing the upstream stage by name
and the finding by ID.

```
RULE CARRY-FORWARD:
  Requirement: Every stage except the first includes a CARRY FORWARD section. Each
  referenced entry names the upstream stage and finding ID, plus this stage's action
  (escalates / confirms unresolved / resolves / registers as risk).

  At least two cross-stage references must appear across the full multi-stage run.

  When no preceding-stage finding bears on this stage:
  CARRY: NONE  (RULE ZERO-STATE applies)
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain.
               PASSES: names the concern and the artifact.
               FAILS: generic description ("A PM cares about alignment")]

### Carry Forward
[RULE CARRY-FORWARD applies -- omit for the first stage in the sequence only]

[For each preceding-stage finding relevant to this stage's scope:
   From [upstream stage] [F-NN]: [concern] -- [this stage's action]]

CARRY: NONE
[required if no upstream findings bear on this stage; RULE ZERO-STATE applies]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; severity must match declared spread]

### Triage Note

HIGH DRIVER:         [the specific finding ranked most critical -- name it and explain
                      what property drove the HIGH assignment from this role's perspective]
LOW ANCHOR:          [the specific finding ranked least critical -- name it and explain
                      what property demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension that shaped the full spread --
                      not a placeholder; specific to this stage's risk landscape]

[All three field labels required; present in every stage unconditionally]
[Placeholder content in any field triggers Condition (c) of TRIAGE NOTE AUDIT SCHEMA]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
[If APPROVED WITH CONDITIONS -- RULE CONDITIONAL-ITEM applies:]
Conditions:
  1. [What must happen] -- Owner: [role] -- Ref: [F-NN]
  2. [Second condition] -- Owner: [role] -- Ref: [F-NN]
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk -- named]    | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk -- named]    | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk -- named]    | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
[If GO WITH CONDITIONS -- RULE CONDITIONAL-ITEM applies: enumerate conditions before Rationale]
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE**

After all stages, produce three independent sections (RULE AUDIT-SUITE applies --
ANTI-PATTERN-1 and ANTI-PATTERN-2 prohibit merging or repeating dimensions):

```
## Calibration Compliance

[For each stage that declared a Calibration Block spread, list any stage where the
 actual severity distribution of findings deviated from the declared spread.]

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with declared vs. actual spread]
```

```
## Role Concern Compliance
[Applies ROLE CONCERN AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b)
 -- If (b): quote the generic content]

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE
```

```
## Triage Note Compliance
[Applies TRIAGE NOTE AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b) / (c)
 -- If (b): which field label is missing
 -- If (c): which field label has placeholder content]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).

---

## V-05 -- Full R9 Stack

**Axis**: All six failing R8 V-05 criteria added simultaneously to the R8 V-05 base:
RULE CARRY-FORWARD (C-06), RULE SYNTHESIS with BLOCKERS and THEMES (C-09, C-10),
RULE CONDITIONAL-ITEM (C-11), Update Protocol in TPM (C-15), and RULE AUDIT-TABLE
for stage-per-row tables in each audit section (C-20).
**Hypothesis**: The six additions occupy structurally distinct locations that do not
interact: C-06 (CARRY FORWARD) is a per-stage section before Calibration; C-11
(RULE CONDITIONAL-ITEM) modifies only the Verdict format; C-15 (Update Protocol) is
a single block inside the TPM stage; C-09 and C-10 (SYNTHESIS) are a post-stage section
before the audit suite; C-20 (RULE AUDIT-TABLE) adds a table inside each existing audit
section without replacing the AUDIT RESULT block. No addition touches the preamble schema
declarations (C-30 preserved), no addition removes rule citations from section headers
(C-31 preserved). RULE CONDITIONAL-ITEM is named explicitly as distinct from RULE
CONDITION-ENUM. RULE SYNTHESIS is declared as a non-audit artifact to prevent ANTI-PATTERN
confusion. RULE AUDIT-TABLE is declared with the explicit requirement that AUDIT RESULT
blocks remain (so C-29 is not voided by the table format). If all six criteria pass, the
composite score reaches 205 -- maximum under v9.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RUN-LEVEL SCHEMAS AND RULES**

The following schemas and rules are declared at run level. All post-stage audit sections
reference these declarations by name rather than redeclaring them.

**TRIAGE NOTE AUDIT SCHEMA** (run-level declaration):

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

**ROLE CONCERN AUDIT SCHEMA** (run-level declaration):

```
ROLE CONCERN AUDIT SCHEMA:
  Condition (a): Role Concern block is absent from the stage
  Condition (b): Role Concern block is present but contains a generic description
                 that does not reference the specific artifact, domain, or risk area
                 under review
```

**RULE ZERO-STATE:** Every section that performs an audit, gap check, enforcement scan,
or synthesis subsection must include an explicit zero-state declaration when it finds no
issues. The declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`.

**RULE CONDITION-ENUM:** [governs audit schema result blocks] Any audit result block that
applies a named schema with labeled conditions must enumerate each condition's result
independently. An aggregate NONE declaration violates RULE CONDITION-ENUM.

```
RULE CONDITION-ENUM:
  Required form (clean run):
    (a) [condition label]: NONE
    (b) [condition label]: NONE
    [(c) [condition label]: NONE  -- if schema has a third condition]
    [SECTION LABEL]: NONE

  VIOLATION [AGGREGATE-NONE]:
  A single "SECTION LABEL: NONE" without per-condition enumeration does not satisfy
  RULE CONDITION-ENUM.
```

**RULE CONDITIONAL-ITEM:** [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
Any verdict of APPROVED WITH CONDITIONS or GO WITH CONDITIONS must enumerate conditions as
numbered items before the Rationale line.

```
RULE CONDITIONAL-ITEM:
  Each item must state: (1) what must happen, (2) the responsible role, (3) finding/risk ref.
  Minimum 2 items when verdict is conditional.

  Required form:
    VERDICT: APPROVED WITH CONDITIONS
    Conditions:
      1. [What must happen] -- Owner: [role] -- Ref: [F-NN or R-NN]
      2. [Second condition] -- Owner: [role] -- Ref: [F-NN or R-NN]
    Rationale: [one sentence]

  VIOLATION [PROSE-CONDITIONS]:
  Conditions stated only in Rationale prose do not satisfy RULE CONDITIONAL-ITEM.
```

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. Absence of either section is a FORMAT VIOLATION making the run incomplete.

```
MANDATORY GAP-SCAN SECTIONS:
  Section 1 -- ROLE CONCERN GAPS: absence = FORMAT VIOLATION
  Section 2 -- TRIAGE NOTE GAPS: absence = FORMAT VIOLATION
```

**RULE AUDIT-SUITE:** After all stages are complete, produce a Post-Stage Audit Suite
containing at least three independent sections, each covering a distinct pre-commitment
dimension.

```
RULE AUDIT-SUITE:
  Requirement: >= 3 independent post-stage audit sections, each covering a single
  pre-commitment dimension, each with its own zero-state under RULE ZERO-STATE.

  ANTI-PATTERN-1 [MERGED SECTION]:
  A single section combining multiple pre-commitment dimensions does not satisfy
  RULE AUDIT-SUITE. Section isolation required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three sections auditing the same dimension at different granularity do not satisfy
  RULE AUDIT-SUITE. Scope diversity is structural, not a quality preference.
```

Required dimensions:
1. Calibration compliance -- findings match declared Calibration Block spread
2. Role-concern compliance -- each stage has topic-specific role-concern declaration
3. Triage note compliance -- each stage has Triage Note with all fields checked using
   TRIAGE NOTE AUDIT SCHEMA (preamble declaration applies)

**RULE AUDIT-TABLE:** Each section in the Post-Stage Audit Suite must contain a stage-per-row
table (Stage / Pre-Commitment / Honored / Deviation) above its AUDIT RESULT block. RULE
CONDITION-ENUM still applies to the AUDIT RESULT block.

```
RULE AUDIT-TABLE:
  Required table columns: Stage | Pre-Commitment | Honored | Deviation
  Required: one row per stage in the run.
  Required: AUDIT RESULT block beneath the table (RULE CONDITION-ENUM applies).

  VIOLATION [PROSE-ONLY]:
  An audit section without a structured table does not satisfy RULE AUDIT-TABLE.
```

**RULE CARRY-FORWARD:** In any multi-stage run, each stage after the first must include a
CARRY FORWARD section before the Calibration block.

```
RULE CARRY-FORWARD:
  Requirement: Every stage except the first includes a CARRY FORWARD section. Each
  referenced entry names the upstream stage and finding ID, plus this stage's action.
  At least two cross-stage references must appear across the full multi-stage run.
  When no preceding-stage finding bears on this stage: CARRY: NONE (RULE ZERO-STATE applies)
```

**RULE SYNTHESIS:** After all stages and before the Post-Stage Audit Suite, produce a
mandatory SYNTHESIS section. SYNTHESIS is a summary-level analysis artifact -- not an
audit section, not counted toward RULE AUDIT-SUITE's three required dimensions.

```
RULE SYNTHESIS:
  Subsection 1 -- BLOCKERS
    For each finding that hard-blocks a downstream stage: upstream stage, finding ID,
    downstream stage, and the impact preventing the downstream stage from proceeding.
    Zero-state: BLOCKERS: NONE  (RULE ZERO-STATE applies)

  Subsection 2 -- CROSS-CUTTING THEMES
    For each concern surfacing in 2+ stages: name at document level, cite stages with
    finding IDs, explain why repetition increases severity above the per-stage finding.
    Zero-state: CROSS-CUTTING THEMES: NONE  (RULE ZERO-STATE applies)
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain.
               PASSES: names the concern and the artifact.
               FAILS: generic description ("A PM cares about alignment")]

### Carry Forward
[RULE CARRY-FORWARD applies -- omit for the first stage in the sequence only]

[For each preceding-stage finding relevant to this stage's scope:
   From [upstream stage] [F-NN]: [concern] -- [this stage's action: escalate /
   confirm unresolved / resolve / register as risk]]

CARRY: NONE
[required if no upstream findings bear on this stage; RULE ZERO-STATE applies]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; severity must match declared spread]

### Triage Note

HIGH DRIVER:         [the specific finding ranked most critical -- name it and explain
                      what property drove the HIGH assignment from this role's perspective]
LOW ANCHOR:          [the specific finding ranked least critical -- name it and explain
                      what property demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension that shaped the full spread --
                      not a placeholder; specific to this stage's risk landscape]

[All three field labels required; present in every stage unconditionally]
[Placeholder content in any field triggers Condition (c) of TRIAGE NOTE AUDIT SCHEMA]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
[If APPROVED WITH CONDITIONS -- RULE CONDITIONAL-ITEM applies:]
Conditions:
  1. [What must happen] -- Owner: [role] -- Ref: [F-NN]
  2. [Second condition] -- Owner: [role] -- Ref: [F-NN]
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk -- named]    | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk -- named]    | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk -- named]    | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Update Protocol

TRIGGER EVENTS:   [events or milestones requiring a risk status update -- specific to this
                   run's risks, e.g., "mitigation action confirmed complete by owner",
                   "milestone gate passed", "risk condition resolved in sprint review"]
UPDATE OWNER:     [role responsible for status updates -- by role, not by person name]
REVISIT CADENCE:  [when the register is reviewed -- e.g., "weekly tpm sync before sprint
                   commit", "at milestone -1 week", "before each go/no-go gate"]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
[If GO WITH CONDITIONS -- RULE CONDITIONAL-ITEM applies: enumerate conditions before Rationale]
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**SYNTHESIS -- RULE SYNTHESIS (required after all stages, before Post-Stage Audit Suite)**

```
## Synthesis

### Blockers
[RULE SYNTHESIS applies]

[For each finding that creates a hard blocker for a downstream stage:]
  Upstream: [stage] [F-NN] -- [concern description]
  Downstream: [stage] -- [what cannot proceed without resolution]

BLOCKERS: NONE
[required if no cross-stage blockers exist; RULE ZERO-STATE applies]

### Cross-Cutting Themes
[RULE SYNTHESIS applies]

[For each concern appearing in 2+ stages:]
THEME-[NN]: [name -- distinct from any individual stage finding]
  Stages: [stage1] ([F-NN]), [stage2] ([F-NN])
  Severity elevation: [why appearance in N stages increases priority above the per-stage finding]

CROSS-CUTTING THEMES: NONE
[required if no concern appears in 2+ stages; RULE ZERO-STATE applies]
```

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE + RULE AUDIT-TABLE**

After Synthesis, produce three independent sections. Each section contains a stage-per-row
table (RULE AUDIT-TABLE) above its AUDIT RESULT block (RULE CONDITION-ENUM). Sections must
be independent -- not merged (ANTI-PATTERN-1), not repeating scope (ANTI-PATTERN-2):

```
## Calibration Compliance
[RULE AUDIT-TABLE applies]

| Stage       | Pre-Commitment (Planned Spread)     | Honored | Deviation |
|-------------|-------------------------------------|---------|-----------|
| [stage]     | [N findings: X HIGH, Y MED, Z LOW]  | YES     | NONE      |
...

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with declared vs. actual spread]
```

```
## Role Concern Compliance
[Applies ROLE CONCERN AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE AUDIT-TABLE applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

| Stage       | Pre-Commitment (Role Concern block)          | Honored | Deviation |
|-------------|----------------------------------------------|---------|-----------|
| [stage]     | topic-specific role-concern declaration      | YES     | NONE      |
...

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE
```

```
## Triage Note Compliance
[Applies TRIAGE NOTE AUDIT SCHEMA (preamble declaration)]
[RULE CONDITION-ENUM applies]
[RULE AUDIT-TABLE applies]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

| Stage       | Pre-Commitment (Triage Note: 3 named fields)           | Honored | Deviation |
|-------------|--------------------------------------------------------|---------|-----------|
| [stage]     | HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR populated | YES     | NONE      |
...

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).
