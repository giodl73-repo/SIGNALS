---
skill: quest-variate
skill_target: corps-rob
round: 7
date: 2026-03-16
rubric_version: 7
---

# Variate R7 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R7 focus: the three new v7 aspirational criteria (C-25, C-26, C-27) were present as
incidental side effects in R6 but were never the primary axis.

- R6 V-02 produced C-25 by enumerating three failure conditions in the TRIAGE NOTE GAPS
  section: (a) section absent, (b) named field missing, (c) placeholder content. But the
  zero-state line was still "TRIAGE NOTE GAPS: NONE" -- it confirmed section presence rather
  than explicitly declaring field-level compliance across all three conditions. C-25 requires
  the zero-state to cover field-level compliance, not just section presence. Making the three
  conditions the explicit audit schema -- with the zero-state confirming each condition is
  clean, not just the section -- closes C-25 structurally.

- R6 V-03 produced C-26 partially by naming RULE AUDIT-SUITE. But naming a rule is necessary
  rather than sufficient: C-26 requires explicit anti-pattern declarations accompanying the rule.
  "merged section does not satisfy" and "same dimension three times does not satisfy" must be
  labeled declarations printed alongside the rule -- not prose rationale, not implied by example.
  R6 V-03 described these as consequences but never encoded them as named anti-patterns with
  their own labels. Making the anti-patterns first-class named elements of the rule closes C-26.

- R6 V-01 produced C-27 by declaring the ROLE CONCERN GAPS section's absence is a format error.
  But C-27 requires the format spec to declare absence of at least one mandatory gap-scan section
  as a format error -- the criterion is satisfied when either ROLE CONCERN GAPS or TRIAGE NOTE
  GAPS carries the "absence = format error" declaration, but it is maximally satisfied when both
  carry it, making both gap-scan sections structurally enforced rather than aspirationally
  included. R6 V-01 applied the format error to ROLE CONCERN GAPS only. Extending the declaration
  to cover both sections -- and ensuring it uses error/violation language rather than "strongly
  recommended" -- makes C-27 unambiguous regardless of which gap-scan section is audited.

R6 V-01 scored 130 under v7 (gains C-27). R6 V-02 scored 130 (gains C-25). R6 V-03 gains C-26;
full scorecard pending. R7 promotes each from incidental artifact to named primary axis.
V-01 targets C-25. V-02 targets C-26. V-03 targets C-27. V-04 pairs C-25 + C-27 (both gap-scan
protocol criteria). V-05 builds the full R7 stack on the R6 V-05 base (RULES A-N) adding
RULES O, P, Q for the v7 delta.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Field-level triage note compliance audit -- three named failure conditions, zero-state covers field-level clean, not section-level presence | V-01 | C-25 |
| Named audit rule with labeled anti-pattern declarations -- RULE AUDIT-SUITE printed with >= 2 anti-patterns as first-class elements | V-02 | C-26 |
| Gap-scan absence as format error -- explicit format error declaration for both mandatory gap-scan sections using error/violation language | V-03 | C-27 |
| Field-level triage compliance + format error language -- three-condition audit schema paired with format error enforcement on both gap sections | V-04 | C-25, C-27 |
| Full R7 stack on R6 V-05 base -- RULES A-N + RULES O, P, Q covering all v2-v7 aspirational criteria | V-05 | C-25, C-26, C-27 (+ C-11 through C-24) |

---

## V-01 -- Triage Note Field-Level Compliance Audit

**Axis**: TRIAGE NOTE GAPS section with explicit three-condition failure schema and field-level
zero-state declaration (C-25)
**Hypothesis**: R6 V-02 produced C-25 by enumerating three failure conditions in TRIAGE NOTE GAPS
and producing "TRIAGE NOTE GAPS: NONE" on a clean run. But C-25's pass condition is stricter:
the zero-state declaration must cover field-level compliance, not just section presence. A TRIAGE
NOTE GAPS section that finds no missing sections and writes "TRIAGE NOTE GAPS: NONE" confirms
that no stages were missing their Triage Note entirely -- it does not confirm that every HIGH
DRIVER, LOW ANCHOR, and DISTRIBUTION FACTOR field was populated with substantive content. C-25
requires the audit to check all three failure conditions per stage and for the zero-state to
declare that all three conditions are clean: no section absent, no named field missing, no
placeholder content. The mechanism: print the three conditions as a named schema before the
per-stage scan, check each condition explicitly for each stage, and write the zero-state as a
multi-condition confirmation (not just "NONE" but an enumeration of which conditions were checked
and found clean). This ensures C-25 is satisfied structurally -- the model cannot satisfy C-23
with a section-presence check and accidentally omit field-level checking. C-21 (named triage
field vocabulary) must pass for C-25 to be scoreable; V-01 includes the named field labels
to satisfy C-21 as a prerequisite.

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
explicit zero-state declaration when the check finds no issues. The zero-state declaration
uses a labeled line ending in `: NONE` or `: ALL STAGES PASS` (e.g., `VIOLATIONS: NONE`,
`ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`). A section that ends without this
line after finding no issues is ambiguous -- the reader cannot distinguish "checked and found
nothing" from "check not performed." RULE ZERO-STATE eliminates that ambiguity.

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
equivalent placeholder is a partial failure. A stage without a Triage Note section is a
format error. These three named field labels are the required vocabulary -- prose sentences
containing the same information without these labels do not satisfy the Triage Note requirement.

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

This section audits triage note compliance at the field level, not at the section level.
Section presence is necessary but not sufficient. Apply this three-condition schema to
every stage's Triage Note:

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section is absent from the stage
  Condition (b): One or more of the three required field labels is missing
                 (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
  Condition (c): A field label is present but its content is a placeholder
                 (e.g., "[the reasoning dimension]", "TBD", "N/A", or a
                 copy of the field label text with no substantive content)
```

For each stage, check all three conditions independently. A stage fails this audit if
any single condition is triggered. Append:

```
## Triage Note Gaps

[For each failing stage:
 -- Stage: [name]
 -- Condition triggered: (a) / (b) / (c)
 -- If (b): which field label is missing
 -- If (c): which field label has placeholder content and what the placeholder was]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
```

[The TRIAGE NOTE AUDIT RESULT block is required on every run -- even a clean run must
enumerate all three conditions and declare each clean. "TRIAGE NOTE GAPS: NONE" alone
is insufficient; it must be accompanied by the three-condition enumeration confirming
field-level compliance, not just section presence.]

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

## V-02 -- Named Audit Rule with Anti-Pattern Specification

**Axis**: RULE AUDIT-SUITE expressed as a named format rule with at least two explicitly
labeled anti-pattern declarations (C-26)
**Hypothesis**: R6 V-03 named RULE AUDIT-SUITE and described scope diversity as the key
requirement. It described what a non-compliant suite looks like -- "a single merged section
covering all three dimensions does not satisfy RULE AUDIT-SUITE even if the content is
correct" and "three sections that all cover the same dimension do not satisfy RULE AUDIT-SUITE."
But these were prose descriptions of the requirement rather than labeled anti-pattern
declarations. C-26 requires the anti-patterns to be first-class printed elements of the rule:
labeled declarations with their own identifiers that a reader can reference independently of
the rule's positive requirements. The mechanism: each anti-pattern carries a label (ANTI-PATTERN-1,
ANTI-PATTERN-2, or equivalent) that makes it addressable and non-ambiguous. A run can then
audit its own compliance against named anti-patterns rather than re-reading prose rationale.
The key claim: encoding anti-patterns as labeled rule elements rather than prose examples
changes the structural enforceability -- a model following rules can check "did my output
trigger ANTI-PATTERN-1 or ANTI-PATTERN-2?" whereas prose rationale requires interpretation.

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
labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section that ends without this
line after a clean check violates RULE ZERO-STATE.

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
  labeled section with its own scope declaration and its own zero-state line. A merged section
  produces one zero-state line covering multiple scopes; RULE AUDIT-SUITE requires one
  zero-state line per scope.

  ANTI-PATTERN-2 [REPEATED DIMENSION]:
  Three or more sections that all audit the same pre-commitment dimension -- at different
  granularity levels, from different angles, or using different criteria -- do not satisfy
  RULE AUDIT-SUITE. Scope diversity is a structural requirement, not a quality preference.
  Three calibration audits at increasing specificity are one dimension repeated three times;
  they satisfy no more than one section of the minimum three required.
```

Required dimensions (minimum three, each a distinct pre-commitment type):

1. **Calibration compliance** -- did each stage's findings match its Calibration Block spread?
2. **Role-concern compliance** -- does each stage have a topic-specific role-concern declaration?
3. **Triage note compliance** -- does each stage have a Triage Note with all required field labels?

Each suite section must carry its own zero-state declaration under RULE ZERO-STATE.
ANTI-PATTERN-1 and ANTI-PATTERN-2 are named compliance blockers -- a suite that triggers
either anti-pattern does not satisfy RULE AUDIT-SUITE regardless of content quality.

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

HIGH DRIVER:         [which finding drove HIGH assignment and why]
LOW ANCHOR:          [which finding was rated lowest and why it was demoted]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the spread -- stage-specific]

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

[For each stage, list any stage missing a Triage Note or any stage where the Triage
 Note omits any of the three required field labels: HIGH DRIVER, LOW ANCHOR,
 DISTRIBUTION FACTOR.]

TRIAGE NOTE GAPS: NONE
[or list failing stages]
```

Each zero-state line is mandatory when the check is clean (RULE ZERO-STATE). The three
sections must be independent labeled top-level sections -- not merged (ANTI-PATTERN-1),
not covering the same scope at different granularity (ANTI-PATTERN-2).

---

## V-03 -- Gap-Scan Absence as Format Error

**Axis**: Format spec explicitly declares absence of both mandatory gap-scan sections as
a format error using error/violation language (C-27)
**Hypothesis**: R6 V-01 declared that ROLE CONCERN GAPS section's absence "is a format
error equivalent to a missing stage header." That language produced C-27 for V-01 under
v7 retroactive scoring. But C-27's pass condition requires the declaration to cover at
least one mandatory post-stage gap-scan section; the criterion is satisfied by a single
declaration and strengthened by covering both. R6 V-01 applied the format error to ROLE
CONCERN GAPS only -- it did not declare TRIAGE NOTE GAPS's absence a format error. A run
that produces ROLE CONCERN GAPS but omits TRIAGE NOTE GAPS satisfies C-27 on V-01 (one
gap-scan section has the format error declaration) but leaves one gap-scan section without
structural enforcement. V-03's mechanism: both gap-scan sections -- ROLE CONCERN GAPS and
TRIAGE NOTE GAPS -- carry explicit format error declarations using error/violation language.
"Strongly recommended" and "should include" do not satisfy C-27. Only "absence = format
error", "omission is a format violation", or equivalent error-language satisfies. The
declarations are printed as part of the format specification, not as rationale commentary,
making the enforcement visible before any stage runs.

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
3. Fallback if absent: assign by stage name.

**RUN-LEVEL FORMAT RULES:**

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement scan
must include an explicit zero-state declaration when the check finds no issues. The
declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS` (e.g.,
`VIOLATIONS: NONE`, `ROLE CONCERN GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`). A section that
ends after confirming clean status without this line is ambiguous. RULE ZERO-STATE does not
apply to sections that find real violations -- those sections list violations instead.

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. The absence of either section after stages have been run is a format violation
that makes the run incomplete regardless of whether per-stage compliance is otherwise correct.

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

Both sections are independent -- they do not share content or merge into a single combined
audit. Each section carries its own zero-state declaration under RULE ZERO-STATE. The format
violation declarations above are not advisory -- they are format errors with the same
standing as a missing stage header or a missing Go/No-Go verdict in the tpm stage.

**ROLE CONCERN BLOCK -- REQUIRED FIRST SECTION IN EACH STAGE**

Before the Calibration Block, every stage must include a standalone ROLE CONCERN block:

```
### Role Concern

ROLE CONCERN: [one sentence naming what this role most fears about THIS specific topic.
Must reference the artifact, domain, or risk area under review.
PASSES: topic-specific fear that names the concern and the artifact.
FAILS: generic role description ("A PM cares about alignment") regardless of accuracy.]
```

**CALIBRATION BLOCK -- REQUIRED AFTER ROLE CONCERN, BEFORE FINDINGS**

```
### Calibration

MOST CRITICAL: [concern this role would rate highest -- traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]
```

Findings must match the declared spread.

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
LOW ANCHOR:          [which finding was rated lowest and why]
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

After completing all stages, scan every stage for a ROLE CONCERN block. A stage fails
this scan if: (a) the ROLE CONCERN block is absent, or (b) the declared concern is generic
and does not reference the specific artifact, domain, or risk area under review. Append:

```
## Role Concern Gaps

[List each stage that fails the scan with the specific failure reason:
 (a) block absent, or (b) content is generic -- not topic-specific]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific ROLE CONCERN block]
```

The ROLE CONCERN GAPS line must be explicit. Absence of this section is a format error
as declared in RULE BOOKEND-AUDIT -- the run is structurally incomplete without it.

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS**
[RULE BOOKEND-AUDIT: absence of this section after stages have run is a FORMAT VIOLATION]

After ROLE CONCERN GAPS, scan every stage for a Triage Note. A stage fails this scan if:
(a) the Triage Note section is absent, (b) any of the three required field labels is
missing (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR), or (c) any field label is present
but its content is a placeholder. Append:

```
## Triage Note Gaps

[List each stage that fails with: stage name + failure condition code (a/b/c)
 + specific field if condition (b) or (c)]

TRIAGE NOTE GAPS: NONE
[required if every stage passes all compliance conditions]
```

The TRIAGE NOTE GAPS line must be explicit. Absence of this section is a format error
as declared in RULE BOOKEND-AUDIT -- the run is structurally incomplete without it.

**CALIBRATION ERRORS -- REQUIRED AFTER TRIAGE NOTE GAPS**

Scan every stage for Calibration Block compliance. Append:

```
## Calibration Errors

[List each stage where actual findings deviate from the declared Calibration Block spread.
 Format: Stage [name]: declared [N HIGH, N MED, N LOW], actual [N HIGH, N MED, N LOW]]

CALIBRATION ERRORS: NONE
[required if every stage honored its declared spread]
```

[RULE ZERO-STATE applies -- explicit NONE required on a clean scan]

---

## V-04 -- Field-Level Triage Compliance + Format Error Language

**Axes**: Both gap-scan protocol criteria as companion requirements (C-25 + C-27)
**Hypothesis**: V-01 established the three-condition field-level triage audit schema for
C-25. V-03 established format error declarations on both gap-scan sections for C-27. These
criteria audit different dimensions of the same gap-scan subsystem: C-27 enforces that the
sections exist (format error on absence); C-25 enforces that the TRIAGE NOTE GAPS section
checks at the right granularity when it does exist (field-level, not section-level). They
are complementary: C-27 closes the gap of omitting the section entirely; C-25 closes the
gap of including the section but checking only section presence rather than field content.
A run that produces TRIAGE NOTE GAPS (satisfying C-27) but writes only "TRIAGE NOTE GAPS:
NONE" without the three-condition schema satisfies C-27 but not C-25. A run that includes
the three-condition schema (satisfying C-25) but does not declare absence a format error
satisfies C-25 but not C-27. Pairing them in a single variation tests whether the two
requirements can coexist without compression: C-27's format error language must appear in
the format spec; C-25's three-condition schema must appear in the audit section itself.
V-04 also naturally produces C-23 (TRIAGE NOTE GAPS section present and checking stage
compliance) and C-22 (ROLE CONCERN GAPS section present) as prerequisites, since both
gap-scan sections must exist and be compliant for either criterion to be scoreable.

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
3. Fallback if absent: assign by stage name.

**THREE RUN-LEVEL FORMAT RULES:**

**RULE ZERO-STATE:** Every section that performs an audit, gap check, or enforcement scan
must include an explicit zero-state declaration when the check finds no issues. The declaration
uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`. A section that ends without
this line after a clean check is ambiguous and violates RULE ZERO-STATE.

**RULE BOOKEND-AUDIT:** After all stages are complete, two mandatory gap-scan sections are
required. Their absence is a format violation:

```
RULE BOOKEND-AUDIT:
  ROLE CONCERN GAPS: Required post-stage section. Omission after stages have run
  is a FORMAT ERROR. Absence = format error. The section must be present even when
  all stages comply; the absence of gaps does not make the section optional.

  TRIAGE NOTE GAPS: Required post-stage section. Omission after stages have run
  is a FORMAT ERROR. Absence = format error. The section must apply the three-condition
  audit schema (see RULE TRIAGE-AUDIT); RULE ZERO-STATE applies to the result.
```

**RULE TRIAGE-AUDIT:** The TRIAGE NOTE GAPS section must apply the following three-condition
audit schema to every stage. Section presence is not sufficient -- each condition must be
checked independently per stage:

```
RULE TRIAGE-AUDIT:
  Condition (a): Triage Note section absent from the stage
  Condition (b): One or more required field labels missing
                 [HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR]
  Condition (c): Field label present but content is a placeholder
                 [e.g., "[the reasoning dimension]", "TBD", "N/A"]

  Zero-state: When all three conditions are clean across all stages, the section
  must carry a TRIAGE NOTE AUDIT RESULT block confirming field-level compliance:
  (a) NONE, (b) NONE, (c) NONE -- not just "TRIAGE NOTE GAPS: NONE" alone.
  The three-condition enumeration distinguishes field-level clean from section-level
  clean and makes the audit's scope unambiguous.
```

**ROLE CONCERN BLOCK -- REQUIRED FIRST SECTION IN EACH STAGE**

```
### Role Concern

ROLE CONCERN: [topic-specific fear -- one sentence naming what this role most fears about
               THIS specific topic. Must reference the artifact, domain, or risk area.
               PASSES: topic-specific. FAILS: generic role description.]
```

**CALIBRATION BLOCK -- REQUIRED AFTER ROLE CONCERN, BEFORE FINDINGS**

```
### Calibration

MOST CRITICAL: [concern this role would rate highest -- traceable to ROLE CONCERN] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]
```

**TRIAGE NOTE -- REQUIRED IN EVERY STAGE AFTER FINDINGS**

```
### Triage Note

HIGH DRIVER:         [specific concern and reasoning -- name it, not just the ID]
LOW ANCHOR:          [specific concern and the property that demoted it]
DISTRIBUTION FACTOR: [stage-specific reasoning dimension -- not a placeholder]
```

All three fields required unconditionally in every stage. These are the named field labels
required by RULE TRIAGE-AUDIT's Condition (b) check.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear]

### Calibration

MOST CRITICAL: [...] -> HIGH
LEAST CRITICAL: [...] -> LOW
PLANNED SPREAD: [N] findings -- [distribution]
[TRIAGE NOTE: if uniform]

### Findings

F-01 HIGH [specific concern]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 per stage; match declared spread]

### Triage Note

HIGH DRIVER:         [specific concern and reasoning]
LOW ANCHOR:          [specific concern and demotion property]
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
alignment or gap. "Strategic priorities" does not satisfy this.

**ROLE CONCERN GAPS -- REQUIRED POST-STAGE SECTION**
[RULE BOOKEND-AUDIT: absence = format error]

```
## Role Concern Gaps

[List each stage where the ROLE CONCERN block is absent (a) or generic (b)]

ROLE CONCERN GAPS: NONE
[required when every stage has a topic-specific declaration]
```

[RULE ZERO-STATE applies -- explicit NONE required on a clean scan]

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS**
[RULE BOOKEND-AUDIT: absence = format error]
[RULE TRIAGE-AUDIT: apply three-condition schema; zero-state must enumerate all three]

```
## Triage Note Gaps

[For each failing stage: name + condition (a/b/c) + field label if (b) or (c)]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
[required when all three conditions are clean across all stages]
```

**CALIBRATION ERRORS -- REQUIRED AFTER TRIAGE NOTE GAPS**

```
## Calibration Errors

[List each stage where actual findings deviate from declared spread]

CALIBRATION ERRORS: NONE
[required if every stage honored its declared spread]
```

[RULE ZERO-STATE applies]

---

## V-05 -- Full R7 Stack on R6 V-05 Base

**Axes**: All fourteen R6 criteria (C-11 through C-24) as RULES A-N + three new R7 criteria
(C-25, C-26, C-27) as RULES O, P, Q -- complete v2 through v7 aspirational coverage encoded
as seventeen structural format requirements
**Hypothesis**: R6 V-05 built RULES A-N covering C-11 through C-24 and produced the highest
expected composite of any R6 variation. V-05 extends that proven base with three additional
rules targeting the v7 delta: RULE O (field-level triage compliance, C-25), RULE P (named
audit rule with anti-patterns, C-26), and RULE Q (gap-scan absence as format error, C-27).

RULE O upgrades the TRIAGE NOTE GAPS section required by RULE M: where RULE M required the
section to exist and name stages with missing or incomplete Triage Notes, RULE O requires
the section to apply the three-condition audit schema and confirm field-level compliance in
its zero-state. RULE O depends on RULE M and RULE K.

RULE P upgrades RULE N: where RULE N required three independent sections with distinct
pre-commitment scopes, RULE P requires the audit suite requirement to be expressed as a named
format rule with at least two labeled anti-pattern declarations. RULE P depends on RULE N.

RULE Q escalates RULE L and RULE M from "required sections" to "absence = format error"
declarations in the format spec. Where RULE L and RULE M stated their sections must be
present after stages run, RULE Q requires error/violation language to appear in the format
specification itself -- naming the consequence of omission, not just the requirement to
include. RULE Q depends on RULE L and RULE M both passing.

The seventeen rules occupy non-overlapping structural locations. Expected score: 60 + 20 +
(14 * 5) = 150 if all fourteen aspirational criteria satisfy, with v7's three new criteria
adding up to 65 additional aspirational points for a theoretical maximum of 185.

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
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm, etc.)

**SEVENTEEN FORMAT RULES -- APPLY TO THE FULL RUN:**

**RULE A -- SEVERITY DISCRIMINATION:** Within each stage's findings, severity labels must
vary. At least one finding per stage must be HIGH. At least one finding across the full run
must be below HIGH (MED or LOW). A stage where all findings carry the same severity label
violates RULE A unless RULE D (Calibration Block) or RULE G (Triage Note) explicitly
justifies the uniform distribution.

**RULE B -- CONDITIONAL ITEMIZATION:** When any verdict is APPROVED WITH CONDITIONS,
BLOCKED WITH CONDITIONS, or GO WITH CONDITIONS, conditions must be listed as numbered
discrete items. Each item names: (1) what must happen, (2) who owns it by role title,
(3) the finding or risk ID driving the condition. Conditions embedded only in prose
rationale violate RULE B. Unconditional verdicts: write `CONDITIONS: N/A`.

**RULE C -- RISK REGISTER STATUS:** The tpm risk register must include a Status column
with values from OPEN / WATCH / MITIGATED. At least 2 distinct status values must appear
across the register. A register without a Status column, or with all rows at the same
status, violates RULE C.

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
appearing before the Calibration Block. The block contains one sentence naming what the
loaded role most fears about THIS specific topic. The sentence must reference the artifact,
domain, or risk area under review. Generic role descriptions ("a PM cares about alignment")
violate RULE F. The ROLE CONCERN must appear as the first named section after the ROLE:
line in each stage.

**RULE G -- UNIVERSAL TRIAGE NOTE:** Every stage must include a Triage Note section after
findings, before the Verdict. The note must contain exactly three fields: HIGH DRIVER, LOW
ANCHOR, and DISTRIBUTION FACTOR. All three fields are required in every stage regardless of
severity spread. A missing Triage Note section or an incomplete Triage Note (any field absent
or left as placeholder) violates RULE G. See RULE K for the field-label format requirement.

**RULE H -- ENFORCEMENT AUDIT:** After the final stage, print a mandatory Enforcement Audit
section that checks every pre-commitment declared during the run against the actual output.
The audit must cover: all Calibration Block spreads (RULE D), the Update Protocol (RULE E),
and all ROLE CONCERN declarations (RULE F). A run without an Enforcement Audit section
violates RULE H. RULE J governs the required table format.

**RULE I -- ZERO-STATE DECLARATION:** Every section in the run that performs an audit,
gap check, or enforcement scan -- including the Enforcement Audit Summary VIOLATIONS line,
the Triage Note Gaps section, the Calibration Errors section, the Role Concern Gaps section,
and any other check section -- must include an explicit zero-state declaration when the check
finds no issues. The declaration uses a labeled line ending in `: NONE` or `: ALL STAGES PASS`
(e.g., `VIOLATIONS: NONE`, `TRIAGE NOTE GAPS: NONE`, `CALIBRATION ERRORS: NONE`). A section
that ends after confirming a clean result without printing this line violates RULE I. A section
that finds real violations does not need a zero-state line.

**RULE J -- ENFORCEMENT AUDIT TABLE FORMAT:** The Enforcement Audit required by RULE H must
be a named-column table. Prose narrative describing the same content does not satisfy RULE J.
The table must include at minimum these named columns: (1) Stage or scope, (2) Pre-Commitment
Declared, (3) Honored (YES/NO), (4) Deviation. A table with unlabeled columns does not satisfy
RULE J. RULE H must pass for RULE J to be scoreable.

**RULE K -- NAMED TRIAGE FIELD VOCABULARY:** Every Triage Note required by RULE G must use
exactly these three labeled field names: `HIGH DRIVER:`, `LOW ANCHOR:`, and `DISTRIBUTION
FACTOR:`. Each label must be printed as a standalone field name on its own line followed by
its content. Prose sentences containing the same information without these field labels do not
satisfy RULE K. RULE G must pass for RULE K to be scoreable.

**RULE L -- ROLE CONCERN GAP SCAN:** After all stages are complete, a mandatory ROLE CONCERN
GAPS section is required. This section is independent of the Enforcement Audit (RULE H) --
it audits RULE F compliance at the document level. The section scans every stage for a ROLE
CONCERN block (RULE F) and names any stage where: (a) the block is absent, or (b) the content
is generic -- it does not reference the specific artifact, domain, or risk area under review.
When all stages comply, the section carries an explicit zero-state under RULE I. Its absence
after stages have been run violates RULE L. See RULE Q for the format error declaration
requirement.

**RULE M -- TRIAGE NOTE GAP SCAN:** After all stages are complete, a mandatory TRIAGE NOTE
GAPS section is required. This section is independent of the Enforcement Audit (RULE H) --
it audits RULE G compliance at the document level. The section scans every stage for a
compliant Triage Note (RULE G) and names any stage where: (a) the Triage Note section is
absent, (b) any of the three required field labels is missing, or (c) a field label is present
but its content is a placeholder. When all stages comply, the section carries an explicit
zero-state under RULE I and RULE O. Its absence after stages have been run violates RULE M.
See RULE Q for the format error declaration requirement.

**RULE N -- POST-STAGE AUDIT SUITE:** After all stages are complete, a suite of three or more
independent post-stage audit sections must be present, each covering a distinct pre-commitment
dimension. RULE L (Role Concern Gaps), RULE M (Triage Note Gaps), and the Calibration Errors
section from RULE D together satisfy the minimum suite requirement when each covers a distinct
scope. RULE N is violated if any two suite sections share the same pre-commitment scope. Each
suite section must independently satisfy RULE I (zero-state declaration). RULE H, RULE L, and
RULE M must all pass for RULE N to be scoreable. See RULE P for the anti-pattern specification
requirement.

**RULE O -- FIELD-LEVEL TRIAGE COMPLIANCE:** The TRIAGE NOTE GAPS section required by RULE M
must audit triage note compliance at the field level, not at the section level. The section
must apply this three-condition audit schema to every stage:

```
TRIAGE NOTE AUDIT SCHEMA:
  Condition (a): Triage Note section absent from the stage
  Condition (b): One or more required field labels missing
                 [HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR]
  Condition (c): Field label present but content is a placeholder

When all three conditions are clean across all stages, the zero-state block must
enumerate all three conditions explicitly:

  TRIAGE NOTE AUDIT RESULT:
    (a) Section absent:        NONE
    (b) Named field missing:   NONE
    (c) Placeholder content:   NONE
    TRIAGE NOTE GAPS: NONE

"TRIAGE NOTE GAPS: NONE" alone does not satisfy RULE O -- the three-condition
enumeration is required to distinguish field-level compliance from section-presence
compliance. RULE M and RULE K must both pass for RULE O to be scoreable.
```

**RULE P -- NAMED AUDIT RULE WITH ANTI-PATTERNS:** The post-stage audit suite requirement
(RULE N) must be expressed as a named format rule accompanied by at least two explicitly
labeled anti-pattern declarations. The anti-patterns must be printed as labeled elements
of the rule specification, not as prose rationale:

```
RULE AUDIT-SUITE:
  [positive requirement: three independent sections, distinct pre-commitment dimensions,
   each with its own zero-state declaration]

  ANTI-PATTERN-1 [MERGED SECTION]: A single section combining multiple pre-commitment
  dimensions under one header does not satisfy RULE AUDIT-SUITE, even if the combined
  content covers all required dimensions. Section isolation is required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]: Three sections auditing the same pre-commitment
  dimension at different granularity levels do not satisfy RULE AUDIT-SUITE. Scope
  diversity is structural -- each section must cover a distinct pre-commitment type.
```

ANTI-PATTERN-1 and ANTI-PATTERN-2 are named compliance blockers -- a suite that triggers
either anti-pattern fails RULE P regardless of content quality. RULE N must pass for RULE P
to be scoreable.

**RULE Q -- GAP-SCAN ABSENCE AS FORMAT ERROR:** The format specification must declare that
absence of both mandatory post-stage gap-scan sections is a format error. The declarations
must use error/violation language -- "absence = format error", "omission is a format
violation", or equivalent. Language such as "strongly recommended" or "should include" does
not satisfy RULE Q.

```
MANDATORY GAP-SCAN SECTIONS (RULE Q enforcement):

  ROLE CONCERN GAPS: Required post-stage section.
  Absence rule: omission of this section after stages have run is a FORMAT ERROR.
  Absence = format error. The section must be present regardless of per-stage compliance.

  TRIAGE NOTE GAPS: Required post-stage section.
  Absence rule: omission of this section after stages have run is a FORMAT ERROR.
  Absence = format error. The section must be present and must satisfy RULE O.
```

RULE L and RULE M must both pass for RULE Q to be scoreable. The format error declarations
must appear in the format specification, not only in prose commentary.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] -- [their orientation in one phrase]

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

| Stage        | Pre-Commitment Declared                          | Honored | Deviation                          |
|--------------|--------------------------------------------------|---------|-------------------------------------|
| [stage-name] | Role Concern: [first few words of declaration]   | YES/NO  | [deviation if NO, or --]           |
| [stage-name] | Calibration spread: [e.g., 1 HIGH, 2 MED, 1 LOW] | YES/NO | [actual spread if NO, or --]      |
| tpm          | Update Protocol: Trigger/Owner/Cadence populated | YES/NO  | [missing fields if NO, or --]      |
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

**RULE AUDIT-SUITE -- MANDATORY GAP-SCAN SECTIONS (RULE Q: absence = format error)**
[RULE P -- suite expressed as a named rule with anti-pattern declarations below]

```
RULE AUDIT-SUITE:
  Requirement: After all stages run, produce >= 3 independent post-stage audit sections
  covering distinct pre-commitment dimensions. Each section must have its own labeled
  header, its own scope, and its own zero-state declaration under RULE I.

  ANTI-PATTERN-1 [MERGED SECTION]: A single section combining multiple pre-commitment
  dimensions under one header does not satisfy RULE AUDIT-SUITE, even if the combined
  content is correct and covers all required dimensions. Section isolation required.

  ANTI-PATTERN-2 [REPEATED DIMENSION]: Three sections auditing the same pre-commitment
  dimension at different granularity levels do not satisfy RULE AUDIT-SUITE. Scope
  diversity is structural -- each section must cover a distinct pre-commitment type.
```

**ROLE CONCERN GAPS -- REQUIRED POST-STAGE SECTION**
[RULE Q: absence of this section after stages have run is a FORMAT ERROR -- absence = format error]
[RULE L -- independent of Enforcement Audit]

```
## Role Concern Gaps

[List each stage where: (a) ROLE CONCERN block is absent, or (b) content is generic
 and does not reference the specific artifact, domain, or risk area under review]

ROLE CONCERN GAPS: NONE
[required if every stage has a qualifying topic-specific ROLE CONCERN block -- RULE I]
```

**TRIAGE NOTE GAPS -- REQUIRED AFTER ROLE CONCERN GAPS**
[RULE Q: absence of this section after stages have run is a FORMAT ERROR -- absence = format error]
[RULE M -- independent of Enforcement Audit]
[RULE O -- apply three-condition schema; zero-state must enumerate all three conditions]

```
## Triage Note Gaps

[For each failing stage: stage name + condition code (a/b/c) + specific field if (b) or (c)]

TRIAGE NOTE AUDIT RESULT:
  (a) Section absent:        [N stages / NONE]
  (b) Named field missing:   [N stages / NONE]
  (c) Placeholder content:   [N stages / NONE]
  TRIAGE NOTE GAPS: NONE
[required when all three conditions are clean across all stages -- RULE O + RULE I]
```

[The TRIAGE NOTE AUDIT RESULT block with three-condition enumeration is required on every
clean run. "TRIAGE NOTE GAPS: NONE" alone does not satisfy RULE O -- the three-condition
enumeration must be present to confirm field-level compliance.]
