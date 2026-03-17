---
skill: quest-variate
skill_target: corps-rob
round: 8
date: 2026-03-16
rubric_version: 8
---

# Variate R8 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R8 focus: the two new v8 criteria (C-28, C-29) were sourced from R7 V-01. That
variation already achieves them, scoring 140 under v8. But R7 V-02, which achieves
C-26 (RULE AUDIT-SUITE with labeled anti-patterns) via a different structural path,
fails C-25 -- which makes C-28 and C-29 not scoreable by the dependency chain
(C-25 -> C-28 -> C-29). The two 140-point paths are structurally disjoint:

- R7 V-01: C-25 + C-28 + C-29 (named schema + enumerated result), no C-26
- R7 V-02: C-26 (RULE AUDIT-SUITE + ANTI-PATTERNS), no C-25/C-28/C-29

No R7 variation achieved all of C-25, C-26, C-28, and C-29 simultaneously.
R8 targets their combination. The mechanism: graft the TRIAGE NOTE AUDIT SCHEMA
(C-28 source) into the Triage Note Compliance section of RULE AUDIT-SUITE (C-26
source), replacing the section-level field-label check with a three-condition
named-schema audit. The RULE AUDIT-SUITE structure (ANTI-PATTERN-1/2) is
preserved; only the depth of one suite section changes.

Three additional single-axis tests:

- Preamble schema declaration: declare the TRIAGE NOTE AUDIT SCHEMA in the
  preamble (before any stage runs), making C-28's "separate from per-stage
  instances" requirement unambiguous. R7 V-01 declared the schema within the
  post-stage TRIAGE NOTE GAPS section -- co-located with its application.
  Moving the declaration upstream tests whether preamble-level placement is
  more reliable for C-28.

- Enumeration commitment as a run-level rule: express C-29's per-condition
  enumeration requirement as a named run-level rule (RULE CONDITION-ENUM) that
  forbids collapsing the AUDIT RESULT to a single aggregate NONE. A model
  following rules can check its output against the rule without interpreting
  post-stage instructions mid-generation.

- Symmetric schema coverage: apply the same named-schema + enumerated-result
  pattern to ROLE CONCERN GAPS, giving both mandatory gap sections a declared
  schema with labeled conditions. Tests whether symmetric schema enforcement
  improves coverage without diluting either schema.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Graft TRIAGE NOTE AUDIT SCHEMA into RULE AUDIT-SUITE Triage Note Compliance section | V-01 | C-25, C-26, C-28, C-29 |
| Preamble-level schema declaration (schema appears before stages run) | V-02 | C-28 (separation strengthened) |
| RULE CONDITION-ENUM as run-level rule forbidding aggregate NONE | V-03 | C-29 (enumeration as named rule) |
| Symmetric schema: ROLE CONCERN AUDIT SCHEMA mirrors TRIAGE NOTE AUDIT SCHEMA | V-04 | C-27, C-28, C-29 (symmetric) |
| Full R8 stack: preamble schema + graft + enumeration rule + symmetric schema + RULE AUDIT-SUITE | V-05 | C-25, C-26, C-27, C-28, C-29 |

---

## V-01 -- Schema Grafted into RULE AUDIT-SUITE

**Axis**: TRIAGE NOTE AUDIT SCHEMA (C-28) grafted into the Triage Note Compliance
section of RULE AUDIT-SUITE, replacing section-level field-label checking with the
three-condition named-schema audit from R7 V-01 (C-25 + C-28 + C-29)
**Hypothesis**: R7 V-02 failed C-25 because its Triage Note Compliance section
checked "Triage Note absent or field labels missing" -- a two-condition presence
check, not the three-condition (absent / missing field / placeholder content) schema
audit that C-25 requires. The section used section-level checking even though
named fields existed. Replacing that section with the R7 V-01 three-condition schema
audit (TRIAGE NOTE AUDIT SCHEMA + per-stage (a)/(b)/(c) checking + TRIAGE NOTE
AUDIT RESULT block) installs C-25/C-28/C-29 while preserving ANTI-PATTERN-1 and
ANTI-PATTERN-2 in the RULE AUDIT-SUITE declaration. The key structural claim: the
RULE AUDIT-SUITE requires three independent sections each covering a distinct
pre-commitment dimension. Installing a named sub-schema within the Triage Note
section deepens that section without merging it with any other (no ANTI-PATTERN-1
violation) and without repeating a dimension (no ANTI-PATTERN-2 violation). C-26
is preserved; C-25/C-28/C-29 are added.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RULE ZERO-STATE -- APPLIES TO ALL AUDIT AND GAP-CHECK SECTIONS**

Every section that performs an audit, gap check, or enforcement scan must include an
explicit zero-state declaration when the check finds no issues. The zero-state uses a
labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section that ends after
confirming clean status without this line is ambiguous. RULE ZERO-STATE does not
apply to sections that find real violations -- those sections list violations instead.

**RULE AUDIT-SUITE -- REQUIRED AFTER ALL STAGES**

After all stages are complete, produce a mandatory Post-Stage Audit Suite containing at
least three independent sections, each covering a distinct pre-commitment dimension.

```
RULE AUDIT-SUITE:
  Requirement: After all stages run, produce >= 3 independent post-stage audit sections.
  Each section must: (1) have a distinct labeled header, (2) cover a single pre-commitment
  dimension, (3) list each stage that failed its compliance check, and (4) carry an explicit
  zero-state declaration under RULE ZERO-STATE when no stages fail.

  ANTI-PATTERN-1 [MERGED SECTION]:
  A single section that combines multiple pre-commitment dimensions under one header does
  not satisfy RULE AUDIT-SUITE, even if the combined content covers all required dimensions
  and is otherwise correct. Section isolation is required -- each dimension must be its own
  labeled section with its own scope declaration and its own zero-state line.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three or more sections that all audit the same pre-commitment dimension -- at different
  granularity levels, from different angles, or using different criteria -- do not satisfy
  RULE AUDIT-SUITE. Scope diversity is a structural requirement, not a quality preference.
  Three calibration audits at increasing specificity are one dimension repeated three times;
  they satisfy no more than one section of the minimum three required.
```

Required dimensions (minimum three, each a distinct pre-commitment type):

1. **Calibration compliance** -- did each stage's findings match its declared Calibration Block spread?
2. **Role-concern compliance** -- does each stage have a topic-specific role-concern declaration?
3. **Triage note compliance** -- does each stage have a Triage Note with all three required fields checked at the field level using the three-condition schema?

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence referencing the artifact or domain;
               generic role descriptions do not satisfy this section]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required if spread is uniform -- explain why uniformity is genuine]

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
                      what property demoted it (recoverability, blast radius, timeline
                      independence, or equivalent)]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread for this
                      stage -- specific to this stage's risk landscape, not a placeholder]

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
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE**

After all stages, produce three independent sections (RULE AUDIT-SUITE -- ANTI-PATTERN-1
and ANTI-PATTERN-2 prohibit merging or repeating dimensions):

```
## Calibration Compliance

[For each stage that declared a Calibration Block spread, list any stage where the
 actual severity distribution of findings deviated from the declared spread.]

CALIBRATION COMPLIANCE: ALL STAGES PASS
[or list failing stages with declared vs. actual spread]
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

This section audits triage note compliance at the field level using the three-condition
schema. Section presence is necessary but not sufficient.

TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)

For each stage, check all three conditions independently. A stage fails if any
single condition is triggered.

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
[or list failing stages]
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).

---

## V-02 -- Preamble-Level Schema Declaration

**Axis**: TRIAGE NOTE AUDIT SCHEMA declared in the preamble run-level instructions,
before any stage runs, making the schema a true format-level artifact separate from
the post-stage audit that applies it (C-28 separation strengthened)
**Hypothesis**: R7 V-01 achieved C-28 by printing TRIAGE NOTE AUDIT SCHEMA within
the post-stage TRIAGE NOTE GAPS instructions. The schema was declared at the same
level as its application -- post-stage, co-located. C-28 requires the schema to be
"a named format artifact separate from per-stage instances." Declaring it in the
preamble (before stages begin) creates genuine separation: the model commits to the
three-condition structure as a run-level invariant, and the post-stage section
references the pre-declared schema by name rather than re-introducing it. The key
claim: preamble-level schema declaration strengthens C-28 because the schema is
demonstrably separate from its application -- any per-stage audit instance refers
back to the preamble schema, not the other way around. Secondary benefit: the
preamble schema makes the three conditions visible before the model generates
findings, potentially improving per-stage Triage Note quality (C-18/C-21 compliance).

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**TRIAGE NOTE AUDIT SCHEMA -- RUN-LEVEL DECLARATION**

This schema is declared once at run level and applied in the post-stage TRIAGE NOTE GAPS
section. The three conditions below are the only conditions checked against every
stage's Triage Note. They are fixed for the duration of this run.

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

This schema is a format-level artifact. Per-stage Triage Note results are reported
using this schema's condition labels in the post-stage TRIAGE NOTE GAPS section.

**RULE ZERO-STATE -- APPLIES TO ALL AUDIT AND GAP-CHECK SECTIONS**

Any section that performs an audit, enforcement check, or gap scan must include an
explicit zero-state declaration when the check finds no issues. The zero-state uses a
labeled line ending in `: NONE` or `: ALL STAGES PASS` (e.g., `VIOLATIONS: NONE`,
`ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`). A section that ends without this
line after finding no issues is ambiguous -- the reader cannot distinguish "checked and
found nothing" from "check not performed."

**TRIAGE NOTE -- REQUIRED IN EVERY STAGE AFTER FINDINGS**

Every stage must include a Triage Note section after findings, before the Verdict.
The Triage Note must use exactly these three labeled fields on their own lines:

```
HIGH DRIVER:         [the specific finding or concern ranked most critical -- name it and
                      explain what property made it the top risk from this role's perspective.
                      Reference the concern, not just the finding ID.]
LOW ANCHOR:          [the specific finding or concern ranked least critical -- name it and
                      explain what property demoted it (recoverability, blast radius, timeline
                      independence, or equivalent). Reference the concern.]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread for this
                      stage -- e.g., "reversibility before milestone gate", "shared vs.
                      independent dependency chains". Must be specific to this stage's risk
                      landscape.]
```

All three fields must be populated with substantive content in every stage unconditionally.
A Triage Note section that has HIGH DRIVER and LOW ANCHOR but omits DISTRIBUTION FACTOR is
a partial failure. A DISTRIBUTION FACTOR field left as "[the reasoning dimension]" or
equivalent placeholder is a partial failure -- it triggers Condition (c) of the
TRIAGE NOTE AUDIT SCHEMA. A stage without a Triage Note section triggers Condition (a).

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

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
alignment or gap to the artifact under review. Abstract references to "strategic goals"
do not satisfy this.

**TRIAGE NOTE GAPS -- REQUIRED POST-STAGE SECTION**

After completing all stages, this section is mandatory. A run that omits it is
incomplete regardless of whether per-stage Triage Notes are present and correct.

Apply the TRIAGE NOTE AUDIT SCHEMA declared above to every stage's Triage Note.
Check each stage against all three conditions independently.

```
## Triage Note Gaps

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b) / (c) [using TRIAGE NOTE AUDIT SCHEMA labels]
 -- If (b): which field label is missing
 -- If (c): which field label has placeholder content and what the placeholder was]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

[The TRIAGE NOTE AUDIT RESULT block is required on every run -- even a clean run must
enumerate all three conditions using the TRIAGE NOTE AUDIT SCHEMA labels and declare
each clean. "TRIAGE NOTE GAPS: NONE" alone is insufficient; it must be accompanied by
the three-condition enumeration confirming field-level compliance per schema condition.]

[RULE ZERO-STATE applies -- TRIAGE NOTE GAPS: NONE required if all three conditions
are clean across all stages]

**ROLE CONCERN GAPS -- REQUIRED AFTER TRIAGE NOTE GAPS**

Scan every stage for a topic-specific role-concern declaration. A stage fails if:
(a) no role-concern block is present, or (b) the declared concern is generic and
does not reference the specific artifact, domain, or risk area under review. Append:

```
## Role Concern Gaps

[List each failing stage with failure reason: (a) absent or (b) generic content]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific declaration]
```

[RULE ZERO-STATE applies -- explicit NONE required on a clean scan]

---

## V-03 -- RULE CONDITION-ENUM as Run-Level Enforcement

**Axis**: RULE CONDITION-ENUM declared as a named run-level rule that explicitly
forbids collapsing the TRIAGE NOTE AUDIT RESULT to an aggregate NONE, making
C-29's per-condition enumeration a named enforceable commitment before stages run
**Hypothesis**: R7 V-01 achieved C-29 by instructing the post-stage section to use
the enumerated AUDIT RESULT format. But that instruction is embedded in the
post-stage section -- a model generating stages sequentially may not carry the
constraint forward to the audit section. A model following named run-level rules
can check its post-stage output against RULE CONDITION-ENUM before finalizing:
"Did I enumerate each condition or did I write a single aggregate NONE?" The rule
makes the enumeration constraint addressable by name and checkable at output time,
not just at instruction-reading time. Secondary test: does naming C-29's mechanism
as a run-level rule improve C-25 reliability (the rule forces three-condition thinking
even before the audit section), or does it add format complexity without yield?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RULE ZERO-STATE -- APPLIES TO ALL AUDIT AND GAP-CHECK SECTIONS**

Any section that performs an audit, enforcement check, or gap scan must include an
explicit zero-state declaration when the check finds no issues. The zero-state uses a
labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section that ends without
this line after finding no issues is ambiguous. RULE ZERO-STATE does not apply to
sections that find real violations.

**RULE CONDITION-ENUM -- APPLIES TO ALL SCHEMA-BASED AUDIT RESULT BLOCKS**

Any audit result block that applies a named schema with labeled conditions (a), (b), (c)
must enumerate each condition's result independently in the AUDIT RESULT block. A single
aggregate NONE declaration does not satisfy RULE CONDITION-ENUM even if the check is
clean. The required form:

```
RULE CONDITION-ENUM:
  Requirement: When an audit section applies a named schema with labeled conditions,
  the result block must report each condition's outcome separately.

  VIOLATION [AGGREGATE-NONE]:
  Writing "TRIAGE NOTE GAPS: NONE" without enumerating each schema condition as
  individually clean does not satisfy RULE CONDITION-ENUM. The reader cannot
  confirm from a single NONE whether condition (c) was checked independently or
  was bundled with conditions (a) and (b). An aggregate NONE is an underspecified
  result; a per-condition enumeration is the minimum required form.

  Required form (clean run):
    (a) [condition label]: NONE
    (b) [condition label]: NONE
    (c) [condition label]: NONE
    [SECTION LABEL]: NONE

  Required form (failing run):
    (a) [condition label]: [N stages or NONE]
    (b) [condition label]: [N stages or NONE]
    (c) [condition label]: [N stages or NONE]
    [List failing stages with condition triggered]
```

**TRIAGE NOTE -- REQUIRED IN EVERY STAGE AFTER FINDINGS**

Every stage must include a Triage Note section after findings, before the Verdict.
The Triage Note must use exactly these three labeled fields on their own lines:

```
HIGH DRIVER:         [the specific finding or concern ranked most critical -- name it and
                      explain what property made it the top risk from this role's perspective.]
LOW ANCHOR:          [the specific finding or concern ranked least critical -- name it and
                      explain what property demoted it.]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread for this
                      stage -- specific to this stage's risk landscape, not a placeholder.]
```

All three fields must be populated with substantive content in every stage unconditionally.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

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

HIGH DRIVER:         [specific concern and reasoning]
LOW ANCHOR:          [specific concern and the property that demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension -- not a placeholder]

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
alignment or gap to the artifact under review.

**TRIAGE NOTE GAPS -- REQUIRED POST-STAGE SECTION**

After completing all stages, this section is mandatory. A run that omits it is
incomplete regardless of per-stage Triage Note presence.

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

For each stage, check all three conditions independently.

```
## Triage Note Gaps

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

[RULE CONDITION-ENUM applies -- the AUDIT RESULT block must enumerate all three
conditions independently. An aggregate "TRIAGE NOTE GAPS: NONE" without per-condition
enumeration violates RULE CONDITION-ENUM.]

[RULE ZERO-STATE applies -- TRIAGE NOTE GAPS: NONE required if all three conditions
are clean across all stages]

**ROLE CONCERN GAPS -- REQUIRED AFTER TRIAGE NOTE GAPS**

Scan every stage for a topic-specific role-concern declaration. A stage fails if:
(a) no role-concern block is present, or (b) the declared concern is generic and
does not reference the specific artifact, domain, or risk area under review.

```
## Role Concern Gaps

[List each failing stage with failure reason: (a) absent or (b) generic content]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific declaration]
```

[RULE ZERO-STATE applies]

---

## V-04 -- Symmetric Schema Coverage Across Both Gap Sections

**Axis**: ROLE CONCERN AUDIT SCHEMA with (a)/(b) labeled conditions mirrors the
TRIAGE NOTE AUDIT SCHEMA structure, giving both mandatory gap sections a named
schema and an enumerated AUDIT RESULT block (C-27 + C-28/C-29 symmetry)
**Hypothesis**: R7 V-01 applied named schema + enumerated result to TRIAGE NOTE GAPS
only. ROLE CONCERN GAPS uses (a) absent and (b) generic content as failure conditions
but expresses them inline, not as a named schema declaration. Applying symmetric
treatment -- ROLE CONCERN AUDIT SCHEMA with (a)/(b) labeled conditions + ROLE
CONCERN AUDIT RESULT block enumerating each condition as individually clean -- tests
two claims: (1) symmetric schema enforcement across both mandatory gap sections
produces more reliable document-level compliance; (2) the pattern generalizes beyond
triage notes, showing the named-schema + enumerated-result mechanism is format-level
(not triage-specific). C-27 is strengthened by including format error language for
both gap sections. The ROLE CONCERN AUDIT RESULT enumeration extends the C-29
pattern (per-condition zero-state) to the role-concern dimension -- whether this
satisfies C-29 directly or produces a new scoreable criterion in a future rubric
version is a secondary signal.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**RUN-LEVEL FORMAT RULES:**

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement scan
must include an explicit zero-state declaration when the check finds no issues. The
declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section
that ends after confirming clean status without this line is ambiguous.

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. The absence of either section is a format violation that makes the run incomplete
regardless of whether per-stage compliance is otherwise correct.

```
MANDATORY GAP-SCAN SECTIONS:

Section 1 -- ROLE CONCERN GAPS
  Purpose: audits whether every stage produced a topic-specific role-concern declaration
  Absence rule: omission of this section after stages have run is a FORMAT VIOLATION.
                "absence = format error" -- the same class of failure as a missing stage header.

Section 2 -- TRIAGE NOTE GAPS
  Purpose: audits whether every stage produced a compliant Triage Note
  Absence rule: omission of this section after stages have run is a FORMAT VIOLATION.
                "absence = format error" -- the run is structurally incomplete without it.
```

**ROLE CONCERN BLOCK -- REQUIRED FIRST SECTION IN EACH STAGE**

Before the Calibration Block, every stage must include a standalone ROLE CONCERN block:

```
### Role Concern

ROLE CONCERN: [one sentence naming what this role most fears about THIS specific topic.
Must reference the artifact, domain, or risk area under review.
PASSES: topic-specific fear that names the concern and the artifact.
FAILS: generic role description ("A PM cares about alignment") regardless of accuracy.]
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

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

[F-03 LOW if planned in spread; minimum 2 per stage]

### Triage Note

HIGH DRIVER:         [which finding drove HIGH assignment and why]
LOW ANCHOR:          [which finding was rated lowest and why it was demoted]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension]

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
alignment or gap. "Strategic objectives" does not satisfy this.

**ROLE CONCERN GAPS -- REQUIRED POST-STAGE SECTION**
[RULE BOOKEND-AUDIT: absence of this section after stages have run is a FORMAT VIOLATION]

Apply the ROLE CONCERN AUDIT SCHEMA below to every stage's role-concern declaration:

```
ROLE CONCERN AUDIT SCHEMA:
  Condition (a): Role Concern block is absent from the stage
  Condition (b): Role Concern block is present but contains a generic description
                 that does not reference the specific artifact, domain, or risk area
                 under review (e.g., "A PM cares about alignment")
```

For each stage, check both conditions independently.

```
## Role Concern Gaps

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b)
 -- If (b): quote the generic content that failed the specificity check]

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE
```

[The ROLE CONCERN AUDIT RESULT block is required on every run -- even a clean run
must enumerate both conditions as individually clean. An aggregate "ROLE CONCERN GAPS:
NONE" without per-condition enumeration does not confirm that condition (b) was checked
independently.]

[RULE ZERO-STATE applies -- ROLE CONCERN GAPS: NONE required if both conditions are
clean across all stages]

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS**
[RULE BOOKEND-AUDIT: absence of this section after stages have run is a FORMAT VIOLATION]

Apply the TRIAGE NOTE AUDIT SCHEMA below to every stage's Triage Note:

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a copy of
                 the field label text with no substantive content)
```

For each stage, check all three conditions independently.

```
## Triage Note Gaps

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

[The TRIAGE NOTE AUDIT RESULT block is required on every run -- enumerate all three
conditions as individually clean on a clean run.]

[RULE ZERO-STATE applies -- TRIAGE NOTE GAPS: NONE required if all three conditions
are clean across all stages]

---

## V-05 -- Full R8 Stack

**Axis**: All R8 single-axis mechanisms combined -- preamble schema declaration (V-02),
RULE AUDIT-SUITE with grafted three-condition triage schema (V-01), RULE CONDITION-ENUM
(V-03), symmetric schema across both gap sections (V-04), plus RULE BOOKEND-AUDIT
format error enforcement for both gap sections (C-27)
**Hypothesis**: Each single-axis variation targets one mechanism for C-25/C-26/C-28/C-29.
V-05 stacks all axes and tests whether they coexist without structural tension. The
primary risk is section bloat causing earlier criteria to collapse -- the preamble schema
could be skipped if the model decides it's redundant with the post-stage schema; the
RULE AUDIT-SUITE Triage Note section could revert to section-level checking if the model
loses track of the preamble schema. V-05 uses explicit named-rule cross-references to
prevent collapse: the Triage Note Compliance section within RULE AUDIT-SUITE explicitly
says "using the TRIAGE NOTE AUDIT SCHEMA declared in the preamble," and RULE
CONDITION-ENUM is cited in the TRIAGE NOTE AUDIT RESULT block instruction. Named rules
are checkable at output time; prose instructions are not.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each assigned role.
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

Section 1 -- ROLE CONCERN GAPS
  Absence rule: omission after stages have run is a FORMAT VIOLATION.
                "absence = format error"

Section 2 -- TRIAGE NOTE GAPS
  Absence rule: omission after stages have run is a FORMAT VIOLATION.
                "absence = format error"
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
  not satisfy RULE AUDIT-SUITE. Section isolation required -- each dimension its own
  labeled section with its own scope and zero-state.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three sections auditing the same pre-commitment dimension at different granularity
  do not satisfy RULE AUDIT-SUITE. Scope diversity is structural, not a quality
  preference.
```

Required dimensions:
1. Calibration compliance -- findings match declared Calibration Block spread
2. Role-concern compliance -- each stage has topic-specific role-concern declaration
3. Triage note compliance -- each stage has Triage Note with all fields checked using
   TRIAGE NOTE AUDIT SCHEMA (preamble declaration applies)

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

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

**POST-STAGE AUDIT SUITE -- RULE AUDIT-SUITE**

After all stages, produce three independent sections (RULE AUDIT-SUITE -- ANTI-PATTERN-1
and ANTI-PATTERN-2 prohibit merging or repeating dimensions):

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

[For each stage, check both ROLE CONCERN AUDIT SCHEMA conditions independently.]

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b)
 -- If (b): quote the generic content]

ROLE CONCERN AUDIT RESULT:
  (a) Block absent:          [N stages / NONE]
  (b) Generic content:       [N stages / NONE]
  ROLE CONCERN GAPS: NONE

[RULE CONDITION-ENUM applies -- enumerate both conditions independently]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]
```

```
## Triage Note Compliance
[Applies TRIAGE NOTE AUDIT SCHEMA (preamble declaration)]

[For each stage, check all three TRIAGE NOTE AUDIT SCHEMA conditions independently.]

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

[RULE CONDITION-ENUM applies -- enumerate all three conditions independently]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).
