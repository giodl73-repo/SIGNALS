---
skill: quest-variate
skill_target: corps-rob
round: 5
date: 2026-03-16
rubric_version: 5
---

# Variate R5 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R5 focus: the three new v5 aspirational criteria (C-19, C-20, C-21) were present as
side effects in R4 V-02 and V-03 but were never the primary axis. R5 makes each the
explicit target.

- C-19: Zero-deviation explicit declaration -- any audit, enforcement, or gap-check
  section that finds nothing must print an explicit zero-state line ("VIOLATIONS: NONE",
  "GAPS: NONE", or equivalent). Silence after a clean check is ambiguous; the explicit
  declaration distinguishes a system that checked and found nothing from one that did not
  check. R4 V-02 got C-19 incidentally from "VIOLATIONS: NONE" in the Enforcement
  Summary. R4 V-03 got C-19 incidentally from "TRIAGE NOTE GAPS: NONE" in the gap
  check. Neither made zero-state declaration a formal protocol applied universally.

- C-20: Enforcement audit structured table format -- the enforcement audit required by
  C-17 must be a named-column table (>= 4 columns covering stage/scope, pre-commitment
  declared, whether honored, deviation). Prose audit passes C-17; only tabular passes
  C-20. R4 V-02 showed the table as a template but never stated "table required; prose
  does not satisfy this section" as an explicit formal rule.

- C-21: Named triage field vocabulary -- Triage Notes must use explicitly labeled fields
  (HIGH DRIVER:, LOW ANCHOR:, DISTRIBUTION FACTOR: or equivalent named labels), not
  prose sentences that happen to cover the same content. Prose Triage Note covering all
  three elements passes C-18; only a labeled-field Triage Note passes C-21. R4 V-03
  used these labels in the template but never stated "prose does not satisfy this
  section" as an explicit prohibition.

R4 V-02 got C-19 + C-20 as template artifacts. R4 V-03 got C-19 + C-21 as template
artifacts. R5 promotes each from template to named format rule. V-01 generalizes C-19
to a universal zero-state protocol covering all check sections (not just Enforcement
and Triage Note gap checks). V-02 makes the table format a named formal requirement
with an explicit anti-pattern prohibition. V-03 makes field-label vocabulary a named
formal requirement with an explicit prose-prohibition. V-04 pairs the zero-state
protocol (C-19) with named triage vocabulary (C-21). V-05 builds the full R5 stack on
the proven R4 V-05 base (RULES A-H covering C-11 through C-18) adding RULES I, J, K
for C-19, C-20, C-21.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Universal zero-state declaration -- explicit NONE required in every audit/gap-check section | V-01 | C-19 |
| Named-column table as formal requirement for enforcement audit (prose explicitly prohibited) | V-02 | C-20 (+ C-19 scoped to audit) |
| Named field labels as formal requirement for Triage Notes (prose explicitly prohibited) | V-03 | C-21 (+ C-18) |
| Zero-state universal protocol + named triage field vocabulary | V-04 | C-19, C-21 |
| Full R5 stack on R4 V-05 base -- RULES A-K covering all v2-v5 aspirational criteria | V-05 | C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-19, C-20, C-21 |

---

## V-01 -- Universal Zero-State Declaration Protocol

**Axis**: Explicit NONE declaration required in every audit, enforcement, and gap-check
section -- not just in the Enforcement Audit summary (C-19)
**Hypothesis**: R4 V-02 got C-19 from "VIOLATIONS: NONE" in the Enforcement Summary --
one location. R4 V-03 got C-19 from "TRIAGE NOTE GAPS: NONE" in the gap-check trailing
section -- a different location. Neither variation applied the zero-state requirement
universally: a run with both an Enforcement Audit and a Triage Note gap check must
declare zero-state in each. More broadly, any check section -- calibration enforcement,
role concern gap audit, triage note gap audit, enforcement summary -- must print an
explicit zero-state when the check is clean. Making this a named RULE ZERO-STATE
("every check section that finds nothing must say NONE explicitly") closes the
ambiguity gap regardless of which check sections happen to run. A variation that
declares ZERO-STATE universally also creates pressure to produce clean runs by making
the absence of violations a first-class stated outcome rather than a silent default.

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

**RULE ZERO-STATE -- APPLIES TO ALL AUDIT, ENFORCEMENT, AND GAP-CHECK SECTIONS**

Any section that performs an audit, enforcement check, or gap scan -- including
Calibration Enforcement, Role Concern Gaps, Triage Note Gaps, and Enforcement Summary
-- must include an explicit zero-state declaration when the check finds no issues.
"Finds no issues" means no violation, no gap, no missing element. The zero-state
declaration must use a labeled line:

```
VIOLATIONS: NONE
```
or
```
GAPS: NONE
```
or
```
[SECTION-NAME] GAPS: NONE
```

A section that completes its check and then simply ends without a zero-state line is
an ambiguous result. The reader cannot distinguish "checked and found nothing" from
"check was not performed." RULE ZERO-STATE eliminates that ambiguity by requiring
the affirmative statement for every clean-result section.

RULE ZERO-STATE applies to:
- Any trailing enforcement section (Calibration Enforcement, Role Concern Gaps, etc.)
- The Enforcement Audit Summary line (VIOLATIONS: ...)
- Any gap-check section added by other format rules

A section that finds real violations does not need a zero-state line -- it lists them
instead. RULE ZERO-STATE applies only to clean-result sections.

**CALIBRATION BLOCK -- REQUIRED BEFORE FINDINGS IN EACH STAGE**

Before writing any finding for a stage, print a Calibration Block:

```
### Calibration

MOST CRITICAL: [the single concern this role would rate highest] -> HIGH
LEAST CRITICAL: [a real but lower-urgency concern] -> LOW
PLANNED SPREAD: [N] findings -- [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform -- explain why uniformity is genuine]
```

Findings must match the declared spread. Append a `## Calibration Errors` section
naming any stage whose actual spread deviates from its Calibration Block. If all stages
honor their declared spread:

```
## Calibration Errors

VIOLATIONS: NONE
```

[RULE ZERO-STATE applies -- explicit NONE required even on a clean enforcement run]

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Calibration

MOST CRITICAL: [concern this role would rate highest] -> HIGH
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

**ROLE CONCERN GAPS -- REQUIRED AFTER ALL STAGES**

After the final stage, scan every stage for a ROLE CONCERN or equivalent topic-specific
declaration of what the loaded role fears about THIS topic. Append:

```
## Role Concern Gaps

[List each stage missing a topic-specific concern declaration, with correction required]

GAPS: NONE
[if every stage has a qualifying topic-specific concern declaration]
```

[RULE ZERO-STATE applies -- explicit GAPS: NONE required on a clean scan]

**TRIAGE NOTE GAPS -- REQUIRED AFTER ALL STAGES**

After Role Concern Gaps, scan every stage for a Triage Note. A stage without a Triage
Note, or a Calibration Block with a uniform spread and no Triage Note, is a gap. Append:

```
## Triage Note Gaps

[List each stage with a missing or incomplete Triage Note]

TRIAGE NOTE GAPS: NONE
[if every stage satisfies its triage note obligation]
```

[RULE ZERO-STATE applies -- explicit TRIAGE NOTE GAPS: NONE required on a clean scan]

---

## V-02 -- Named-Column Enforcement Audit Table

**Axis**: Enforcement audit section must be a named-column table; prose explicitly
prohibited (C-20); zero-state required in enforcement summary (C-19 scoped to audit)
**Hypothesis**: R4 V-02 introduced the Enforcement Audit as a table with columns Stage /
Pre-Commitment Type / Declared Value / Honored / Deviation. The table appeared in the
template but the prompt never stated "table required; prose does not satisfy this section."
A model that rewrites the table as a prose paragraph can technically cover the same
ground and still pass C-17 (the prose audit exists) while failing C-20 (the table format
is absent). The explicit prohibition is the key: "prose audit does not qualify -- only
a named-column table with at least 4 named columns satisfies this section." Naming the
required columns (Stage, Pre-Commitment Declared, Honored, Deviation) makes the pass
condition verifiable by column existence rather than prose interpretation. Pairing this
with an explicit VIOLATIONS: NONE requirement in the Enforcement Summary closes C-19
for the audit section specifically -- every clean audit must declare itself clean, and
every non-clean audit must list its violations.

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
alignment or gap. "Strategic priorities" does not satisfy this.

**ENFORCEMENT AUDIT -- REQUIRED AFTER ALL STAGES**

After the final stage, print a mandatory Enforcement Audit. The audit checks every
pre-commitment declared during the run (Calibration Block spreads, Update Protocol
fields) against the actual output.

**FORMAT RULE: The Enforcement Audit section must be a named-column table. Prose
narrative describing the same content does not satisfy this section. A table with
unnamed or unlabeled columns does not satisfy this section. The table must include
at minimum these four named columns:**

1. Stage -- the stage or scope where the pre-commitment was declared
2. Pre-Commitment Declared -- what was committed to (spread, update protocol, etc.)
3. Honored -- YES or NO
4. Deviation -- what was actually delivered if Honored = NO, or "--" if Honored = YES

```
## Enforcement Audit

| Stage        | Pre-Commitment Declared                 | Honored | Deviation                              |
|--------------|-----------------------------------------|---------|----------------------------------------|
| [stage-name] | Calibration spread: [e.g., 1H 2M 1L]   | YES/NO  | [actual spread if NO, or --]           |
| [stage-name] | Calibration spread: [distribution]      | YES/NO  | [deviation or --]                      |
| tpm          | Update Protocol: 3 fields populated     | YES/NO  | [missing fields if NO, or --]          |
[one row per pre-commitment per stage; cover all stages run]

### Enforcement Summary

COMMITMENTS DECLARED: [N]
COMMITMENTS HONORED: [N]
VIOLATIONS: [list stage + commitment type for each row where Honored = NO, or NONE]
```

The Enforcement Summary VIOLATIONS line must be explicit:
- If violations exist: list each one by stage and commitment type
- If no violations exist: write `VIOLATIONS: NONE`

A VIOLATIONS line that is simply absent -- leaving the reader to infer a clean result
from the absence of a list -- does not satisfy this section. The affirmative declaration
"VIOLATIONS: NONE" is required for a clean enforcement run.

---

## V-03 -- Named Triage Field Vocabulary

**Axis**: Triage Notes must use explicitly labeled field names; prose sentences
that cover the same content explicitly prohibited (C-21 + C-18)
**Hypothesis**: R4 V-03 used HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR as field
labels in the Triage Note template. These labels appeared because the template showed
them. The prompt never stated: "Triage Notes must use labeled fields; prose sentences
that contain the same information without field labels do not satisfy this section."
The distinction matters: a model under low-compliance conditions may write a Triage
Note as three prose sentences ("The highest risk was F-01 because...; F-03 was rated
low because...; the overall spread reflects...") and satisfy C-18 (content present)
while failing C-21 (no field labels). Making the field-label vocabulary a named
formal requirement -- and explicitly prohibiting the prose alternative -- closes C-21
for any run that includes a Triage Note. The prohibition is the key mechanism: without
it the model can drift to prose and still believe it is complying. The three required
labels HIGH DRIVER: / LOW ANCHOR: / DISTRIBUTION FACTOR: must appear as printable
field names on their own lines, not as section subheadings or as topics embedded in
prose paragraphs.

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

**TRIAGE NOTE FIELD VOCABULARY -- REQUIRED IN EVERY STAGE**

Every stage must include a Triage Note section after findings, before the Verdict.
The Triage Note must use exactly these three labeled field names, each on its own line:

```
HIGH DRIVER:         [content]
LOW ANCHOR:          [content]
DISTRIBUTION FACTOR: [content]
```

**Prose sentences that cover the same content without these field labels do not satisfy
this section.** For example, the following does NOT satisfy the Triage Note requirement:

> "F-01 was rated HIGH because it blocks the release gate. F-03 was rated LOW because
> it is recoverable. The spread reflects the blast radius of each concern."

The following DOES satisfy the requirement:

```
HIGH DRIVER:         F-01 rated HIGH -- blocks the release gate with no recovery path
                     before the milestone; shared dependency means failure propagates
                     across all three downstream teams.
LOW ANCHOR:          F-03 rated LOW -- documentation gap is post-launch recoverable
                     without user impact; no shared dependency with critical path.
DISTRIBUTION FACTOR: Reversibility before the milestone gate. Concerns that cannot be
                     recovered post-launch rank higher; concerns recoverable after
                     launch rank lower.
```

All three field labels are required in every stage. A Triage Note that includes HIGH
DRIVER and LOW ANCHOR but omits DISTRIBUTION FACTOR is a partial failure. A stage
without a Triage Note section is a format error. The Triage Note is required
unconditionally -- present whether severity varies or is uniform.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Findings

F-01 HIGH [specific concern -- grounded in this role's lens]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if appropriate; minimum 2 findings; severity labels must reflect real triage]

### Triage Note

HIGH DRIVER:         [which finding was ranked most critical and why -- name the specific
                      concern, not just the finding ID. What made it the top risk from
                      this role's perspective?]
LOW ANCHOR:          [which finding was ranked least critical and why it was demoted --
                      what property (recoverability, blast radius, timeline independence)
                      placed it lowest?]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread for
                      this stage -- e.g., "reversibility before milestone gate",
                      "shared vs. independent dependency chains", "blast radius of
                      each concern across downstream teams"]

[All three field labels required; prose sentences without labels do not qualify]

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
alignment or gap. "Company objectives" does not satisfy this.

**TRIAGE NOTE GAPS -- REQUIRED AFTER ALL STAGES**

After completing all stages, scan each stage for a compliant Triage Note. A Triage
Note is non-compliant if: (a) the section is absent, (b) any of the three required
field labels is missing, or (c) the field labels are present but the content is a
placeholder. Append:

```
## Triage Note Gaps

[List each stage and field that requires correction]

TRIAGE NOTE GAPS: NONE
[if every stage has a compliant Triage Note with all three field labels populated]
```

The TRIAGE NOTE GAPS line must be explicit. If the scan finds no gaps, write
`TRIAGE NOTE GAPS: NONE`. A gap check that ends without this line leaves ambiguity
about whether the scan was performed.

---

## V-04 -- Zero-State Protocol + Named Triage Field Vocabulary

**Axes**: Universal zero-state declaration (C-19) + named triage field vocabulary as
labeled format requirement (C-21)
**Hypothesis**: V-01 established zero-state declaration as a universal protocol for
all audit and gap-check sections -- any section that finds nothing must say NONE
explicitly. V-03 established named field labels as a formal requirement for Triage
Notes -- prose without labels does not qualify. These two criteria operate at different
structural locations: C-19 governs every check-section tail; C-21 governs the internal
structure of Triage Notes. They do not overlap in purpose or position, so pairing them
tests whether the combination produces both criteria without compression. The key
mechanic in each case is a prohibition: V-01 prohibits silent clean-result sections;
V-03 prohibits prose Triage Notes. Stating both prohibitions explicitly in a single
variation should produce a higher compliance signal than either alone, because each
prohibition is reinforced by the presence of the other -- the model cannot satisfy
the zero-state protocol by silently omitting a Triage Note gap check that would have
had to say NONE.

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
"No issues" means no violation, no gap, no missing or incomplete field. The zero-state
declaration uses a labeled line ending in `: NONE` (e.g., `VIOLATIONS: NONE`,
`GAPS: NONE`, `TRIAGE NOTE GAPS: NONE`). A section that completes its check and ends
without this line is an ambiguous result -- it does not distinguish "checked and found
nothing" from "check skipped." RULE ZERO-STATE does not apply to sections that find
real violations -- those sections list the violations instead.

**RULE FIELD-LABELS:** Every Triage Note must use exactly three named field labels:
`HIGH DRIVER:`, `LOW ANCHOR:`, and `DISTRIBUTION FACTOR:`. Each label must be printed
on its own line followed by its content. Prose sentences that contain the same
information without these labels do not satisfy the Triage Note requirement. A Triage
Note written as prose paragraphs fails RULE FIELD-LABELS even if the content is
substantively correct.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] -- [their orientation in one phrase]

### Calibration

MOST CRITICAL: [concern this role would rate highest] -> HIGH
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

HIGH DRIVER:         [which finding drove the HIGH assignment and what made it the
                      top risk -- reference the specific concern, not just the ID]
LOW ANCHOR:          [which finding was rated lowest and why it was demoted -- name
                      the property that placed it lowest (recoverability, blast
                      radius, timeline independence, etc.)]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the severity spread for
                      this stage -- must be specific enough to distinguish this
                      stage's risk landscape from a generic description]

[RULE FIELD-LABELS -- all three labels required; prose sentences without labels fail]

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

**TRIAGE NOTE GAPS -- REQUIRED AFTER ALL STAGES**

After the final stage, scan each stage for a compliant Triage Note (all three field
labels populated with specific content). Append:

```
## Triage Note Gaps

[List each stage and specific field label missing or left as placeholder]

TRIAGE NOTE GAPS: NONE
[required if scan finds no gaps -- RULE ZERO-STATE applies]
```

**CALIBRATION GAPS -- REQUIRED AFTER TRIAGE NOTE GAPS**

Scan each stage for a Calibration Block and verify that findings match the declared
spread. Append:

```
## Calibration Gaps

[List each stage where findings deviate from the declared Calibration Block spread]

CALIBRATION GAPS: NONE
[required if scan finds no gaps -- RULE ZERO-STATE applies]
```

---

## V-05 -- Full R5 Stack on R4 V-05 Base

**Axes**: All eight R4 criteria (C-11 through C-18) as RULES A-H + three new R5 criteria
(C-19, C-20, C-21) as RULES I, J, K -- complete v2 through v5 aspirational coverage
encoded as eleven structural format requirements
**Hypothesis**: R4 V-05 built the full v2-v4 criterion set as eight format rules and
produced the highest expected composite of any R4 variation (RULES A-H covering
C-12, C-11, C-13, C-14, C-15, C-16, C-18, C-17). V-05 extends that proven base with
three additional rules targeting the v5 delta: RULE I (zero-state declaration, C-19),
RULE J (enforcement audit named-column table, C-20), and RULE K (named triage field
vocabulary, C-21). The eleven rules occupy non-overlapping structural locations: RULE A
governs finding generation; RULE B governs verdict conditions; RULE C governs risk
register status; RULE D governs calibration blocks; RULE E governs update protocol;
RULE F governs role-concern pre-declaration; RULE G governs Triage Note presence and
field structure; RULE H governs the enforcement audit existence; RULE I governs the
zero-state declaration in all check sections; RULE J governs the enforcement audit's
table format; RULE K governs the Triage Note's internal field-label vocabulary. RULE J
and RULE H are sequentially dependent (RULE H must pass for RULE J to be scoreable);
RULE K and RULE G are sequentially dependent (RULE G must pass for RULE K to be
scoreable). All other rules are independent. The composite uplift from adding RULES I,
J, K to the R4 V-05 base should be additive given structural independence.

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

**ELEVEN FORMAT RULES -- APPLY TO THE FULL RUN:**

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
line, the Triage Note Gaps section, the Calibration Gaps section, and any other check
section -- must include an explicit zero-state declaration when the check finds no
issues. The declaration uses a labeled line ending in `: NONE` (e.g., `VIOLATIONS:
NONE`, `GAPS: NONE`). A section that ends after confirming a clean result without
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

[RULE I -- VIOLATIONS: NONE required explicitly when no violations found; silent
 omission of this line when the result is clean violates RULE I]

**FORMAT ERROR PROTOCOL:** If any of RULES A through K are violated and not already
captured in the Enforcement Audit, append a `## Format Errors` section after the
Enforcement Audit. Each entry names: the rule violated, the stage it occurred in, and
the correction required. If no format errors exist outside the Enforcement Audit:

```
## Format Errors

FORMAT ERRORS: NONE
```

[RULE I applies -- explicit FORMAT ERRORS: NONE required on a clean run]
