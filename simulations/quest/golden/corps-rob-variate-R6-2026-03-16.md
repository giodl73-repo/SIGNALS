---
skill: quest-variate
skill_target: corps-rob
round: 6
date: 2026-03-16
rubric_version: 6
---

# Variate R6 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R6 focus: the three new v6 aspirational criteria (C-22, C-23, C-24) were present as
incidental side effects in R5 V-01 but were never the primary axis. R5 V-01 included
three trailing post-stage sections (Calibration Errors + Role Concern Gaps + Triage
Note Gaps) that satisfied C-22, C-23, and C-24 without any of them being formally
required. R6 promotes each from incidental artifact to named formal requirement.

- C-22: Post-stage role-concern gap scan -- a dedicated section after all stages that
  audits C-16 compliance (role-concern pre-declarations) across every stage. The section
  names any stage missing a topic-specific role-concern declaration. When all stages
  comply, it carries an explicit zero-state: "ROLE CONCERN GAPS: NONE". R5 V-01 had this
  as a small trailing section but never stated "this section is required; its absence is
  a format error; the zero-state line is mandatory on a clean scan." Making the zero-state
  a formal requirement (not just recommended) and naming the section as mandatory closes
  C-22 consistently regardless of whether C-16 passes.

- C-23: Post-stage triage note gap scan -- a dedicated section after all stages that
  audits C-18 compliance (universal per-stage triage note) across every stage. The section
  names any stage where the Triage Note is absent or incomplete (missing any of the three
  required field labels). When all stages comply, it carries "TRIAGE NOTE GAPS: NONE".
  R5 V-01 and V-03 both had Triage Note Gaps sections but neither framed this as a formal
  required section with field-level granularity. A Triage Note with a present section but
  a missing DISTRIBUTION FACTOR field is a C-23 gap even if it passes C-18 at the
  structural level -- the gap scan must detect field-level non-compliance, not just
  section presence.

- C-24: Multi-type post-stage audit suite -- three or more independent post-stage audit
  sections, each covering a distinct pre-commitment dimension. Scope diversity is the key
  requirement: three calibration audits do not satisfy C-24; three sections covering
  calibration compliance, role-concern compliance, and triage note compliance do. R5 V-01
  got C-24 by having Calibration Errors + Role Concern Gaps + Triage Note Gaps as three
  naturally distinct sections. R6 makes the suite pattern an explicit formal requirement:
  a run must produce at least three named audit sections with distinct pre-commitment
  scopes, and each section must satisfy C-19 zero-state protocol independently.

R5 V-01 got C-22 + C-23 + C-24 incidentally (score: 120 under v6). R6 makes each the
explicit target. V-01 targets C-22 alone. V-02 targets C-23 with field-level granularity.
V-03 targets C-24 as an explicit audit-suite format rule. V-04 pairs C-22 + C-23 as
companion gap-scan requirements. V-05 builds the full R6 stack on the R5 V-05 base
(RULES A-K) adding RULES L, M, N for C-22, C-23, C-24.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Post-stage role-concern gap scan as formal required section (explicit zero-state + format error if absent) | V-01 | C-22 |
| Post-stage triage note gap scan as formal required section with field-level compliance granularity | V-02 | C-23 (+ C-18) |
| Multi-type post-stage audit suite as named format rule -- three sections, scope diversity required | V-03 | C-24 |
| Role-concern gap scan + triage note gap scan as companion required sections | V-04 | C-22, C-23 |
| Full R6 stack on R5 V-05 base -- RULES A-N covering all v2-v6 aspirational criteria | V-05 | C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-24 |

---

## V-01 -- Post-Stage Role-Concern Gap Scan

**Axis**: ROLE CONCERN GAPS as a mandatory post-stage section with explicit zero-state
and format error protocol -- not a trailing courtesy section (C-22)
**Hypothesis**: R5 V-01 produced C-22 by appending a "Role Concern Gaps" section after
all stages. That section satisfied C-22 because it existed and carried "GAPS: NONE" when
clean. But R5 V-01 never stated: "this section is required; its absence when stages have
been run is a format error; the zero-state declaration is mandatory for a clean scan."
Without that explicit requirement, a model under low-compliance conditions can omit the
section entirely and not violate any stated rule. The explicit promotion is the mechanism:
naming ROLE CONCERN GAPS as a required post-stage section -- parallel in status to the
Enforcement Audit -- means its absence triggers the same format error protocol as a
missing stage header. Pairing it with RULE ZERO-STATE (C-19) means the section must say
NONE explicitly on a clean result, not end silently. The key claim: moving from "here is
a section I happen to include" to "this section is required and its absence is an error"
changes compliance from incidental to structural.

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
3. Fallback if files absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RULE ZERO-STATE -- APPLIES TO ALL AUDIT AND GAP-CHECK SECTIONS**

Any section that performs an audit, enforcement check, or gap scan must include an
explicit zero-state declaration when the check finds no issues. The zero-state
declaration uses a labeled line ending in `: NONE` (e.g., `VIOLATIONS: NONE`,
`GAPS: NONE`, `ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`). A section that
completes its check and ends without this line is ambiguous -- the reader cannot
distinguish "checked and found nothing" from "check not performed." RULE ZERO-STATE
eliminates that ambiguity. A section that finds real violations does not need a
zero-state line -- it lists violations instead.

**ROLE CONCERN BLOCK -- REQUIRED FIRST SECTION IN EACH STAGE**

Before the Calibration Block, before any finding, every stage must include a
standalone ROLE CONCERN block:

```
### Role Concern

ROLE CONCERN: [one sentence naming what this role most fears about THIS specific topic.
Must reference the artifact, domain, or risk area under review.
PASSES: "PM fears the three-team dependency on the auth service will slip the Q2 gate
without a named owner for the interface contract."
FAILS: "A PM cares about alignment and delivery timelines." Generic role descriptions
do not satisfy this section regardless of accuracy.]
```

**CALIBRATION BLOCK -- REQUIRED AFTER ROLE CONCERN, BEFORE FINDINGS**

```
### Calibration

MOST CRITICAL: [concern this role would rate highest -- traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]
```

Findings must match the declared spread. Append a `## Calibration Errors` section
naming any stage where actual spread deviates from declared spread. If all stages
honor their spread:

```
## Calibration Errors

CALIBRATION ERRORS: NONE
```

[RULE ZERO-STATE applies -- explicit NONE required even on a clean run]

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [concern this role would flag but not lose sleep over] -> LOW
PLANNED SPREAD: [N] findings -- [distribution]
[TRIAGE NOTE: if spread is uniform -- reason for justified uniformity]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 per stage; severity must match planned spread]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

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
alignment or gap to the artifact under review. "Strategic goals" does not satisfy this.

**ROLE CONCERN GAPS -- REQUIRED POST-STAGE SECTION**

After completing all stages, this section is mandatory. Its absence after stages have
been run is a format error equivalent to a missing stage header.

Scan every stage for a ROLE CONCERN block. A stage fails this scan if: (a) the ROLE
CONCERN block is absent, or (b) the declared concern is generic -- it does not reference
the specific artifact, domain, or risk area under review. Append:

```
## Role Concern Gaps

[List each stage that fails the scan with the specific failure reason:
 (a) block absent, or (b) content is generic -- not topic-specific]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific ROLE CONCERN block]
```

The ROLE CONCERN GAPS line must be explicit:
- If gaps exist: list each stage and failure type
- If no gaps: write `ROLE CONCERN GAPS: NONE`

A Role Concern Gaps section that ends without this line -- whether gaps exist or not --
violates RULE ZERO-STATE. The section must be present even when all stages comply.

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS**

After Role Concern Gaps, scan every stage for a Triage Note. A stage fails this scan
if the Triage Note section is absent, or if a Calibration Block declares uniform spread
without a Triage Note explaining the uniformity. Append:

```
## Triage Note Gaps

[List each stage with a missing Triage Note or missing justification for uniform spread]

TRIAGE NOTE GAPS: NONE
[required if every stage satisfies its triage note obligation]
```

[RULE ZERO-STATE applies -- explicit TRIAGE NOTE GAPS: NONE required on a clean scan]

---

## V-02 -- Post-Stage Triage Note Gap Scan with Field-Level Compliance

**Axis**: TRIAGE NOTE GAPS as a mandatory post-stage section with field-level compliance
granularity -- section presence is necessary but not sufficient (C-23 + C-18)
**Hypothesis**: R5 V-01 and V-03 both produced C-23 by including a Triage Note Gaps
section. But both checked only structural presence: is the section there, does it have
content? Neither checked field-level compliance: is HIGH DRIVER populated? Is LOW ANCHOR
populated? Is DISTRIBUTION FACTOR populated with specific content rather than a
placeholder? C-23's pass condition is stricter than "section is present": the section
must name each stage where the Triage Note was absent OR incomplete. A Triage Note that
has HIGH DRIVER and LOW ANCHOR but omits DISTRIBUTION FACTOR is a C-23 gap. A Triage
Note that has all three labeled fields but leaves DISTRIBUTION FACTOR as "[the reasoning
dimension]" without actual content is also a gap. Making field-level compliance the
explicit scope of the gap scan -- and naming the three required fields so the model knows
what to check -- produces C-23 coverage beyond section-presence checking. The zero-state
line "TRIAGE NOTE GAPS: NONE" is required on a clean scan; its absence when the scan
finds no gaps is itself a compliance gap (RULE ZERO-STATE / C-19).

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
3. Fallback if absent: assign by stage name.

**TRIAGE NOTE -- REQUIRED IN EVERY STAGE AFTER FINDINGS**

Every stage must include a Triage Note section after findings, before the Verdict.
The Triage Note must use exactly these three labeled fields, each on its own line:

```
HIGH DRIVER:         [which finding was ranked most critical and why -- name the specific
                      concern and the reasoning. What made it the top risk from this
                      role's perspective? Reference the finding concern, not just the ID.]
LOW ANCHOR:          [which finding was ranked least critical and why it was demoted --
                      name the specific property (recoverability, blast radius, timeline
                      independence) that placed it lowest. Reference the concern.]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread for
                      this stage -- e.g., "reversibility before milestone gate",
                      "shared vs. independent dependency chains". Must be specific to
                      this stage's risk landscape, not a generic description.]
```

All three fields must be populated with specific content in every stage unconditionally.
A Triage Note that includes HIGH DRIVER and LOW ANCHOR but omits DISTRIBUTION FACTOR is
a partial failure. A DISTRIBUTION FACTOR field left as a placeholder is a partial
failure. A stage without a Triage Note section is a format error.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Calibration

MOST CRITICAL: [the single concern this role would rate highest] -> HIGH
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

[F-03 LOW if planned; minimum 2 per stage; severity must match planned spread]

### Triage Note

HIGH DRIVER:         [specific concern and reasoning -- not just the finding ID]
LOW ANCHOR:          [specific concern and the property that demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension -- not a placeholder]

[All three field labels required; section mandatory in every stage unconditionally]

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
alignment or gap. "Strategic priorities" does not satisfy this.

**TRIAGE NOTE GAPS -- REQUIRED POST-STAGE SECTION**

After completing all stages, this section is mandatory. A run that omits it is
incomplete regardless of whether per-stage Triage Notes are present and correct.

Scan every stage for a compliant Triage Note. A stage fails this scan if any of the
following are true:
- (a) The Triage Note section is absent from the stage
- (b) Any of the three required field labels is missing (HIGH DRIVER, LOW ANCHOR,
      DISTRIBUTION FACTOR)
- (c) Any field label is present but its content is a placeholder (e.g., "[the
      reasoning dimension]", "TBD", or equivalent non-content)

Append:

```
## Triage Note Gaps

[List each stage that fails the scan. For each failing stage, name:
 -- the stage identifier
 -- which condition failed: (a) section absent, (b) field label missing, or
    (c) field content is a placeholder
 -- the specific field label that is missing or unpopulated if condition (b) or (c)]

TRIAGE NOTE GAPS: NONE
[required if every stage passes all three compliance conditions for Triage Notes]
```

The TRIAGE NOTE GAPS line must be explicit:
- If gaps exist: list each stage and condition code
- If no gaps: write `TRIAGE NOTE GAPS: NONE`

A Triage Note Gaps section that ends without this line violates the zero-state protocol.

**ROLE CONCERN GAPS -- REQUIRED AFTER TRIAGE NOTE GAPS**

After Triage Note Gaps, scan every stage for a topic-specific role-concern declaration
(a ROLE CONCERN block or equivalent). Append:

```
## Role Concern Gaps

[List each stage missing a topic-specific role-concern declaration]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying declaration]
```

---

## V-03 -- Multi-Type Post-Stage Audit Suite

**Axis**: RULE AUDIT-SUITE -- three or more independent post-stage audit sections with
distinct pre-commitment scopes as a named format requirement (C-24)
**Hypothesis**: C-24 is not satisfied by having one large enforcement section that
covers multiple pre-commitment types. It requires three or more sections each with
its own named scope, its own zero-state declaration protocol, and its own gaps list.
The critical distinction is scope diversity: three sections covering calibration
compliance in three different ways do not satisfy C-24; three sections covering
calibration compliance, role-concern compliance, and triage note compliance do.
R5 V-01 got C-24 by coincidence of having three naturally distinct trailing sections.
Making the suite pattern a named RULE -- "after all stages, produce at least three
independent post-stage audit sections covering distinct pre-commitment dimensions;
each section must have its own scope and its own zero-state declaration" -- produces
C-24 reliably because the model is instructed to produce the suite, not just to include
individual sections. Naming the three required dimensions (calibration, role-concern,
triage note) ensures scope diversity is explicit. Requiring each section to independently
satisfy RULE ZERO-STATE means a model cannot satisfy C-24 by merging the three into a
single combined section that happens to cover all three topics.

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

**RULE AUDIT-SUITE -- REQUIRED AFTER ALL STAGES**

After all stages are complete, produce a mandatory Post-Stage Audit Suite. The suite
must contain at least three independent sections, each covering a distinct
pre-commitment dimension. Combining dimensions into a single section does not satisfy
this rule -- each dimension must be its own labeled section with its own scope
declaration, its own findings list, and its own zero-state declaration.

**Required dimensions (minimum three, covering distinct pre-commitment types):**

1. **Calibration compliance** -- did each stage's findings match its Calibration Block
   spread? One entry per stage that declared a spread.

2. **Role-concern compliance** -- does each stage have a topic-specific role-concern
   declaration (a ROLE CONCERN block or equivalent named field)? One entry per stage.

3. **Triage note compliance** -- does each stage have a Triage Note? If uniform severity
   was declared, was a justification provided? One entry per stage.

Each suite section must:
- Have a distinct labeled header (e.g., `## Calibration Compliance`, `## Role Concern
  Compliance`, `## Triage Note Compliance`)
- List each stage that failed its dimension's compliance check
- Carry an explicit zero-state declaration when no stages fail (e.g., `CALIBRATION
  COMPLIANCE: ALL STAGES PASS`, `ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`)

A single merged section that covers all three dimensions does not satisfy RULE AUDIT-SUITE
even if the content is correct -- section isolation is required. Three sections that all
cover the same dimension (e.g., three calibration audits at different granularity levels)
do not satisfy RULE AUDIT-SUITE -- scope diversity is required.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Calibration

MOST CRITICAL: [the single concern this role would rate highest] -> HIGH
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

[F-03 LOW if planned in spread; minimum 2 per stage; severity must match planned spread]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk -- named]    | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk -- named]    | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk -- named]    | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Risk Register -- Update Protocol

| Field           | Value                                                                        |
|-----------------|------------------------------------------------------------------------------|
| Trigger Events  | [specific events that require a status change -- list 2-3, topic-specific]   |
| Owner Role      | [role responsible for status updates -- by role title, not by person name]   |
| Revisit Cadence | [schedule or trigger condition specific to this topic's delivery rhythm]     |

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE**

After all stages, produce three independent sections. Each section is required:

```
## Calibration Compliance

[For each stage that declared a Calibration Block spread, list any stage where the
 actual severity distribution of findings deviated from the declared spread.]

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with their declared vs. actual spread]
```

```
## Role Concern Compliance

[For each stage, list any stage missing a topic-specific role-concern declaration.
 A generic role description ("PM cares about alignment") is a compliance failure
 even if a block is present with that content.]

ROLE CONCERN GAPS: NONE
[or list failing stages with failure reason]
```

```
## Triage Note Compliance

[For each stage, list any stage missing a Triage Note. For stages with uniform
 severity spread and no written justification, flag the missing justification.]

TRIAGE NOTE GAPS: NONE
[or list failing stages]
```

Each zero-state line is mandatory when the check is clean. A section that ends
without its zero-state line is an incomplete check. The three sections must appear
as independent labeled top-level sections -- they must not be merged into a single
section or presented as sub-sections of a larger audit.

---

## V-04 -- Role-Concern Gap Scan + Triage Note Gap Scan

**Axes**: Both post-stage gap scan types as formal companion requirements (C-22 + C-23)
**Hypothesis**: V-01 established ROLE CONCERN GAPS as a formal required section. V-02
established TRIAGE NOTE GAPS as a formal required section with field-level granularity.
C-22 and C-23 audit different dimensions: C-22 checks whether the role's topic-specific
fear was declared before findings began (C-16 compliance); C-23 checks whether the
calibration decision was documented after findings ended (C-18 compliance). They audit
structurally opposite ends of the stage -- the opening pre-commitment versus the closing
documentation -- so pairing them does not create scope overlap. The hypothesis is that
requiring both gap scan types simultaneously, each as a named mandatory section, produces
C-22 + C-23 without compression artifacts. The pair also naturally creates a partial
C-24 signal: two of the three sections required for the audit suite (C-24) are present.
A run that also includes a third distinct audit section (e.g., Calibration Errors)
satisfies C-24. V-04 pairs the two new criteria and relies on the Calibration Errors
section (already present in V-01 as a companion to the Calibration Block) to complete
the suite.

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
3. Fallback if absent: assign by stage name.

**TWO RUN-LEVEL FORMAT RULES:**

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement
scan must include an explicit zero-state declaration when the check finds no issues.
The declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS` (e.g.,
`ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`, `VIOLATIONS: NONE`). A section
that ends after confirming a clean result without printing this line is ambiguous.
RULE ZERO-STATE does not apply to sections that find real violations -- those sections
list violations instead.

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections
are required. Both sections must be present regardless of per-stage compliance. Their
absence is a format error:

Section 1 -- ROLE CONCERN GAPS: scans every stage for a topic-specific role-concern
declaration. Reports any stage missing one or carrying a generic declaration.

Section 2 -- TRIAGE NOTE GAPS: scans every stage for a compliant Triage Note. Reports
any stage where the Triage Note is absent or where uniform severity was declared without
justification. At the field-level: reports any stage where HIGH DRIVER, LOW ANCHOR, or
DISTRIBUTION FACTOR is missing or left as a placeholder.

Both sections are independent -- they do not share content or combine into a single
merged audit. Each section carries its own zero-state declaration under RULE ZERO-STATE.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain;
               generic role descriptions do not satisfy this section]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [concern this role would flag but not lose sleep over] -> LOW
PLANNED SPREAD: [N] findings -- [distribution]
[TRIAGE NOTE: required if spread is uniform -- reason for justified uniformity]

### Findings

F-01 HIGH [specific concern -- most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; must match declared spread]

### Triage Note

HIGH DRIVER:         [which finding drove HIGH assignment and why -- name the specific
                      concern, not just the finding ID]
LOW ANCHOR:          [which finding was rated lowest and why it was demoted -- name the
                      property that placed it lowest (recoverability, blast radius, etc.)]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the severity spread for this
                      stage -- stage-specific, not a generic description]

[All three field labels required; present in every stage unconditionally]

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
alignment or gap. Abstract references to "strategic objectives" do not satisfy this.

**CALIBRATION ERRORS -- REQUIRED AFTER FINAL STAGE**

Scan every stage where a Calibration Block was declared. For each stage, check whether
the actual severity distribution of findings matches the PLANNED SPREAD. Append:

```
## Calibration Errors

[List each stage where actual findings deviate from the declared Calibration Block spread.
 Format: Stage [name]: declared [N HIGH, N MED, N LOW], actual [N HIGH, N MED, N LOW]]

CALIBRATION ERRORS: NONE
[required if every stage with a declared spread delivered matching findings]
```

[RULE ZERO-STATE applies -- explicit NONE required on a clean scan]

**ROLE CONCERN GAPS -- REQUIRED AFTER CALIBRATION ERRORS**

Scan every stage for a ROLE CONCERN block (or equivalent topic-specific declaration
of what the loaded role fears about THIS topic). A stage fails this scan if: (a) the
block is absent, or (b) the declared concern is generic and does not reference the
specific artifact, domain, or risk area under review. Append:

```
## Role Concern Gaps

[List each stage that fails the scan with failure reason:
 (a) block absent -- stage: [name]
 (b) content is generic -- stage: [name], content does not reference the topic]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific concern declaration]
```

[RULE BOOKEND-AUDIT applies -- this section is mandatory; its absence is a format error]
[RULE ZERO-STATE applies -- explicit ROLE CONCERN GAPS: NONE required on a clean scan]

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS**

Scan every stage for a compliant Triage Note. A stage fails this scan if any of the
following are true:
- (a) The Triage Note section is absent
- (b) Any of the three required field labels is missing: HIGH DRIVER, LOW ANCHOR,
      DISTRIBUTION FACTOR
- (c) A field label is present but its content is a placeholder (e.g., "[reasoning
      dimension]", "TBD")

Append:

```
## Triage Note Gaps

[List each stage that fails. For each: stage name + failure condition code (a/b/c)
 + specific field label if condition (b) or (c)]

TRIAGE NOTE GAPS: NONE
[required if every stage passes all compliance conditions]
```

[RULE BOOKEND-AUDIT applies -- this section is mandatory; its absence is a format error]
[RULE ZERO-STATE applies -- explicit TRIAGE NOTE GAPS: NONE required on a clean scan]

---

## V-05 -- Full R6 Stack on R5 V-05 Base

**Axes**: All eleven R5 criteria (C-11 through C-21) as RULES A-K + three new R6 criteria
(C-22, C-23, C-24) as RULES L, M, N -- complete v2 through v6 aspirational coverage
encoded as fourteen structural format requirements
**Hypothesis**: R5 V-05 built RULES A-K covering C-11 through C-21 and produced the
highest expected composite of any R5 variation. V-05 extends that proven base with three
additional rules targeting the v6 delta: RULE L (post-stage role-concern gap scan, C-22),
RULE M (post-stage triage note gap scan with field-level compliance, C-23), and RULE N
(post-stage audit suite, C-24). RULE N is naturally satisfied when RULE L (Role Concern
Gaps section) + RULE M (Triage Note Gaps section) + the Calibration Errors section
required by RULE D produce three independently scoped sections -- the suite emerges from
the rules rather than requiring a separate enforcement. The fourteen rules occupy
non-overlapping structural locations: RULES A-C govern finding and verdict generation;
RULE D governs per-stage Calibration Blocks; RULE E governs the tpm Update Protocol;
RULE F governs per-stage ROLE CONCERN blocks; RULE G governs per-stage Triage Notes;
RULE H governs the post-run Enforcement Audit; RULE I governs zero-state declarations
in all check sections; RULE J governs the Enforcement Audit table format; RULE K
governs Triage Note field-label vocabulary; RULE L governs the Role Concern Gaps
post-stage section; RULE M governs the Triage Note Gaps post-stage section; RULE N
governs the audit suite (three independent sections, scope diversity). RULE N depends
on RULES L and M being satisfied plus at least one additional independent audit section
-- the Calibration Errors section from RULE D satisfies the third dimension. The
composite uplift from adding RULES L, M, N to the R5 V-05 base should be additive given
structural independence. Expected score under v6: 60 + 20 + (11 * 5) = 135 minimum if
all criteria satisfied.

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
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm, etc.)

**FOURTEEN FORMAT RULES -- APPLY TO THE FULL RUN:**

**RULE A -- SEVERITY DISCRIMINATION:** Within each stage's findings, severity labels
must vary. At least one finding per stage must be HIGH. At least one finding across the
full run must be below HIGH (MED or LOW). A stage where all findings carry the same
severity label violates RULE A unless RULE D (Calibration Block) or RULE G (Triage
Note) explicitly justifies the uniform distribution.

**RULE B -- CONDITIONAL ITEMIZATION:** When any verdict is APPROVED WITH CONDITIONS,
BLOCKED WITH CONDITIONS, or GO WITH CONDITIONS, conditions must be listed as numbered
discrete items. Each item names: (1) what must happen, (2) who owns it by role title,
(3) the finding or risk ID driving the condition. Conditions embedded only in prose
rationale violate RULE B. Unconditional verdicts: write `CONDITIONS: N/A`.

**RULE C -- RISK REGISTER STATUS:** The tpm risk register must include a Status column
with values from OPEN / WATCH / MITIGATED. At least 2 distinct status values must
appear across the register. A register without a Status column, or with all rows at the
same status, violates RULE C.

**RULE D -- CALIBRATION BLOCK:** Before writing findings for each stage, print a
Calibration Block naming the most critical concern (-> HIGH), the least critical concern
(-> LOW), and the planned spread. Findings must match the declared spread. When planned
spread is uniform, include a Triage Note in the Calibration Block explaining why
uniformity is genuinely justified. A stage with uniform severity and no Triage Note
violates RULE D.

**RULE E -- UPDATE PROTOCOL:** The tpm risk register must include an Update Protocol
table with three fields: Trigger Events, Owner Role, and Revisit Cadence. All three
fields must be populated with topic-specific values. Generic placeholders or a missing
Update Protocol section violates RULE E. RULE C must pass for RULE E to be scoreable.

**RULE F -- ROLE CONCERN:** Every stage must begin with a standalone ROLE CONCERN block
appearing before the Calibration Block. The block contains one sentence naming what
the loaded role most fears about THIS specific topic. The sentence must reference the
artifact, domain, or risk area under review. Generic role descriptions ("a PM cares
about alignment") violate RULE F. The ROLE CONCERN must appear as the first named
section after the ROLE: line in each stage.

**RULE G -- UNIVERSAL TRIAGE NOTE:** Every stage must include a Triage Note section
after findings, before the Verdict. The note must contain exactly three fields: HIGH
DRIVER, LOW ANCHOR, and DISTRIBUTION FACTOR. All three fields are required in every
stage regardless of severity spread. A missing Triage Note section or an incomplete
Triage Note (any field absent or left as placeholder) violates RULE G. See RULE K for
the field-label format requirement.

**RULE H -- ENFORCEMENT AUDIT:** After the final stage, print a mandatory Enforcement
Audit section that checks every pre-commitment declared during the run against the
actual output. The audit must cover: all Calibration Block spreads (RULE D), the Update
Protocol (RULE E), and all ROLE CONCERN declarations (RULE F). A run without an
Enforcement Audit section violates RULE H. RULE J governs the required table format.

**RULE I -- ZERO-STATE DECLARATION:** Every section in the run that performs an audit,
gap check, or enforcement scan -- including the Enforcement Audit Summary VIOLATIONS
line, the Triage Note Gaps section, the Calibration Errors section, the Role Concern
Gaps section, and any other check section -- must include an explicit zero-state
declaration when the check finds no issues. The declaration uses a labeled line ending
in `: NONE` or `: ALL STAGES PASS` (e.g., `VIOLATIONS: NONE`, `GAPS: NONE`,
`CALIBRATION ERRORS: NONE`). A section that ends after confirming a clean result without
printing this line violates RULE I. A section that finds real violations does not need
a zero-state line -- it lists the violations instead.

**RULE J -- ENFORCEMENT AUDIT TABLE FORMAT:** The Enforcement Audit required by RULE H
must be a named-column table. Prose narrative describing the same content does not
satisfy RULE J. The table must include at minimum these named columns: (1) Stage or
scope, (2) Pre-Commitment Declared, (3) Honored (YES/NO), (4) Deviation. A table with
unlabeled columns does not satisfy RULE J. RULE H must pass for RULE J to be scoreable.

**RULE K -- NAMED TRIAGE FIELD VOCABULARY:** Every Triage Note required by RULE G
must use exactly these three labeled field names: `HIGH DRIVER:`, `LOW ANCHOR:`, and
`DISTRIBUTION FACTOR:`. Each label must be printed as a standalone field name on its
own line followed by its content. Prose sentences that contain the same information
without these field labels do not satisfy RULE K. RULE G must pass for RULE K to be
scoreable.

**RULE L -- ROLE CONCERN GAP SCAN:** After all stages are complete, a mandatory
ROLE CONCERN GAPS section is required. This section is independent of the Enforcement
Audit (RULE H) -- it audits C-16 compliance at the document level. The section scans
every stage for a ROLE CONCERN block (RULE F) and names any stage where: (a) the block
is absent, or (b) the content is generic -- it does not reference the specific artifact,
domain, or risk area under review. When all stages comply, the section carries an explicit
zero-state under RULE I. Its absence after stages have been run violates RULE L regardless
of per-stage ROLE CONCERN compliance.

**RULE M -- TRIAGE NOTE GAP SCAN:** After all stages are complete, a mandatory TRIAGE
NOTE GAPS section is required. This section is independent of the Enforcement Audit
(RULE H) -- it audits C-18 compliance at the document level with field-level granularity.
The section scans every stage for a compliant Triage Note (RULE G) and names any stage
where: (a) the Triage Note section is absent, (b) any of the three required field labels
is missing, or (c) a field label is present but its content is a placeholder. When all
stages comply, the section carries an explicit zero-state under RULE I. Its absence after
stages have been run violates RULE M regardless of per-stage Triage Note compliance.

**RULE N -- POST-STAGE AUDIT SUITE:** After all stages are complete, a suite of three or
more independent post-stage audit sections must be present, each covering a distinct
pre-commitment dimension. RULE L (Role Concern Gaps), RULE M (Triage Note Gaps), and the
Calibration Errors section from RULE D together satisfy the minimum suite requirement
when each covers a distinct scope. RULE N is violated if any two suite sections share
the same pre-commitment scope. Three calibration audits at different granularity levels
do not satisfy RULE N -- scope diversity is required. Each suite section must independently
satisfy RULE I (zero-state declaration). RULE H, RULE L, and RULE M must all pass for
RULE N to be scoreable; if only two of the three are present, RULE N cannot be satisfied.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain;
               RULE F -- must not be a generic role description]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern this role would surface] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required if uniform -- explain why the risk landscape is genuinely
 uniform. E.g., "All findings rated HIGH because each concern independently blocks
 the go-live gate with no recovery path outside the shared milestone."]

[RULE D -- Calibration Block required; RULE F -- ROLE CONCERN must appear before this]

### Findings

F-01 HIGH [specific concern -- most critical item per calibration]
          Owner: [role]
          Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
          Owner: [role]
          Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 per stage; RULE A + RULE D apply]

### Triage Note

HIGH DRIVER:         [which finding was ranked most critical and why -- name the specific
                      concern, not just the ID. What made it the top risk for this role?]
LOW ANCHOR:          [which finding was ranked least critical and why it was demoted --
                      what property (recoverability, blast radius, timeline) placed it
                      lowest? Name the concern and the reasoning.]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread for
                      this stage -- e.g., "reversibility before milestone gate",
                      "shared vs. independent dependency chains", "timeline compression"]

[RULE G -- all three fields required unconditionally; no stage may omit Triage Note]
[RULE K -- field labels required; prose sentences without labels violate this section]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

CONDITIONS:
[RULE B -- numbered items if conditional, N/A if unconditional]
1. [what must happen] -- Owner: [role title] -- Finding: [F-NN or R-NN]
2. [what must happen] -- Owner: [role title] -- Finding: [F-NN or R-NN]
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
[minimum 3 rows; at least 1 HIGH; RULE C -- Status column, 2+ distinct values]

### Risk Register -- Update Protocol

| Field           | Value                                                                       |
|-----------------|-----------------------------------------------------------------------------|
| Trigger Events  | [2-3 specific events that require a status change -- topic-specific]        |
| Owner Role      | [role title responsible for updates -- not a person name]                   |
| Revisit Cadence | [schedule or condition specific to this topic's delivery rhythm]            |

[RULE E -- all three fields required; generic placeholders violate this section]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk or finding ID]

CONDITIONS:
[RULE B -- numbered items if GO WITH CONDITIONS, N/A if GO or NO-GO]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission       | Program         | Artifact/Topic | Alignment               |
|------------------------|-----------------|----------------|-------------------------|
| [named mission]        | [program name]  | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named -- "strategic goals" fails C-08]
```

**CROSS-STAGE COHERENCE:** When running --stage all, later stages should reference
prior-stage findings where relevant. Format: `[prior stage] F-[N]: confirm / escalate /
contradict -- [one sentence]`. Aim for at least 2 cross-stage references across the run.

**ENFORCEMENT AUDIT -- REQUIRED AFTER FINAL STAGE:**

```
## Enforcement Audit

[RULE J -- this section must be a named-column table; prose narrative does not qualify]

| Stage        | Pre-Commitment Declared                        | Honored | Deviation                         |
|--------------|------------------------------------------------|---------|-----------------------------------|
| [stage-name] | Role Concern: [first few words of declaration] | YES/NO  | [deviation if NO, or --]          |
| [stage-name] | Calibration spread: [e.g., 1 HIGH, 2 MED, 1 LOW] | YES/NO | [actual spread if NO, or --]   |
| tpm          | Update Protocol: Trigger/Owner/Cadence populated | YES/NO | [missing fields if NO, or --]  |
[one row per pre-commitment per stage; cover all stages run; RULE H + RULE J]

### Enforcement Summary

COMMITMENTS DECLARED: [N]
COMMITMENTS HONORED: [N]
VIOLATIONS: [list stage + commitment type for each Honored = NO row, or NONE]
```

[RULE I -- VIOLATIONS: NONE required explicitly when no violations found]

**CALIBRATION ERRORS -- REQUIRED AFTER ENFORCEMENT AUDIT:**

```
## Calibration Errors

[List each stage where actual findings deviate from the declared Calibration Block spread]

CALIBRATION ERRORS: NONE
[required if every stage honored its declared spread -- RULE I applies]
```

**ROLE CONCERN GAPS -- REQUIRED AFTER CALIBRATION ERRORS:**

```
## Role Concern Gaps

[List each stage missing a topic-specific role-concern declaration, with failure reason:
 (a) block absent -- stage: [name]
 (b) content is generic -- stage: [name]]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific declaration -- RULE I applies]
```

[RULE L -- this section is mandatory; its absence is a format error]

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS:**

```
## Triage Note Gaps

[List each stage that fails triage note compliance. For each: stage name + failure code:
 (a) section absent, (b) field label missing + which label, (c) field content placeholder
 + which field]

TRIAGE NOTE GAPS: NONE
[required if every stage passes all compliance conditions -- RULE I applies]
```

[RULE M -- this section is mandatory; its absence is a format error]

[RULE N -- Calibration Errors + Role Concern Gaps + Triage Note Gaps constitute the
 three-section audit suite; each section covers a distinct pre-commitment dimension;
 each section independently satisfies RULE I; scope diversity is maintained]

**FORMAT ERROR PROTOCOL:** If any of RULES A through N are violated and not already
captured in the above audit sections, append a `## Format Errors` section after Triage
Note Gaps. Each entry names: the rule violated, the stage it occurred in, and the
correction required. If no format errors exist outside the audit sections:

```
## Format Errors

FORMAT ERRORS: NONE
```

[RULE I applies -- explicit FORMAT ERRORS: NONE required on a clean run]
