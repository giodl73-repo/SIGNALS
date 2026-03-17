---
skill: quest-variate
skill_target: corps-rob
round: 4
date: 2026-03-16
rubric_version: 4
---

# Variate R4 — corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R4 focus: the three new v4 aspirational criteria (C-16, C-17, C-18) were not
targeted in R3. R4 explores axes that surface these gaps.

- C-16: Role-lens pre-declaration — a standalone, topic-specific declaration of what
  the loaded role most fears about THIS topic, printed as a named block before any
  finding as a pre-commitment artifact. Distinct from C-02 (which checks that findings
  reflect the role) — C-16 checks for the upfront declaration, not the findings.
- C-17: Pre-commitment enforcement audit — a post-run section that audits whether
  pre-commitment artifacts declared during the run (calibration blocks, update
  protocols, role lens declarations) were actually honored in the output. Closes the
  loop between declared intent and delivered output; makes pre-commitments falsifiable.
- C-18: Universal per-stage triage note — a Triage Note present in every stage
  unconditionally, documenting the calibration decision regardless of severity spread.
  Distinct from C-14 (which requires a Triage Note only when severity is uniform) —
  C-18 requires it even when spread varies naturally.

R3 V-01 embedded ROLE LENS inside the Calibration Block as a sub-field. R4 V-01
extracts it as a standalone pre-commitment block with its own header — elevating it
from a calibration aid to a first-class artifact. R4 V-02 introduces a post-run
Enforcement Audit section: a table that scans every pre-commitment declared during
the run and explicitly flags violations. R4 V-03 makes the Triage Note unconditional
by giving it three required fields (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR)
that must be populated in every stage, not just when severity is uniform. V-04 pairs
the bookend structure: ROLE CONCERN declares the role's fear before findings, TRIAGE
NOTE documents the calibration result after findings — both unconditional. V-05 builds
the full v4 stack on the proven R3 V-05 base (RULES A-E covering C-11 through C-15)
adding RULES F, G, H for the three new v4 criteria.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Role-lens pre-declaration as standalone ROLE CONCERN block before Calibration | V-01 | C-16 |
| Post-run enforcement audit as required table checking all pre-commitments | V-02 | C-17 |
| Universal three-field Triage Note in every stage unconditionally | V-03 | C-18 |
| Role-Lens Pre-Declaration + Universal Triage Note (stage bookend pair) | V-04 | C-16, C-18 |
| Full R4 stack on R3 V-05 base — RULES A-H covering all v2-v4 aspirational criteria | V-05 | C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18 |

---

## V-01 — Role-Lens Pre-Declaration

**Axis**: Standalone ROLE CONCERN block as first-class pre-commitment artifact (C-16)
**Hypothesis**: R3 V-01 embedded ROLE LENS as a sub-field inside the Calibration Block.
C-16 distinguishes between a role description and a topic-specific pre-commitment: the
declaration must reference the artifact or domain under review, not just repeat the
role's general orientation. Promoting ROLE CONCERN to a standalone section with its own
header — appearing before the Calibration Block — forces the model to instantiate the
role's fear against the specific topic before any calibration planning begins. The
subsequent MOST CRITICAL entry in the Calibration Block should be traceable to the
declared ROLE CONCERN, creating a verifiable link from pre-commitment to calibration to
findings. A stage where ROLE CONCERN is generic ("a PM cares about alignment") fails
C-16 even if the calibration and findings are correct; only topic-specific instantiation
qualifies.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. Fallback if files absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**ROLE CONCERN BLOCK — REQUIRED FIRST SECTION IN EACH STAGE**

Before the Calibration Block, before any finding, print a standalone ROLE CONCERN block:

```
### Role Concern

ROLE CONCERN: [What this role most fears about THIS specific topic — one sentence.
Must reference the artifact, domain, or risk area under review. Examples of what
DOES satisfy: "PM fears the three-team dependency on the auth service will slip the
Q2 gate without a named owner for the interface contract."
Examples of what does NOT satisfy: "A PM cares about alignment and delivery timelines."
Generic role descriptions — however accurate — fail this section.]
```

The ROLE CONCERN block is a pre-commitment artifact. The Calibration Block's MOST
CRITICAL entry must trace back to the declared concern. If the findings do not address
the concern declared in ROLE CONCERN, the stage has an internal consistency gap.

**CALIBRATION BLOCK — REQUIRED AFTER ROLE CONCERN, BEFORE FINDINGS**

After ROLE CONCERN, print a Calibration Block:

```
### Calibration

MOST CRITICAL: [the concern this role would rate highest — traceable to ROLE CONCERN] → HIGH
LEAST CRITICAL: [a real but lower-urgency concern this role would surface] → LOW
PLANNED SPREAD: [N] findings — [e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required only when planned spread is uniform — explain why
 uniformity is genuinely justified, not just "all concerns are important"]
```

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] — [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear — one sentence referencing the artifact or domain]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] → HIGH
LEAST CRITICAL: [concern this role would flag but not lose sleep over] → LOW
PLANNED SPREAD: [N] findings — [distribution]
[TRIAGE NOTE: if spread is uniform — reason for justified uniformity]

### Findings

F-01 HIGH [specific concern — the most critical item per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern — from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 findings; must match declared spread]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 entries; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap to the artifact under review. "Strategic goals" does not satisfy this.

**ROLE CONCERN ENFORCEMENT:** After completing all stages, scan the output. If any stage
is missing its ROLE CONCERN block, or if the ROLE CONCERN content is generic (does not
reference the specific artifact or domain under review), append a `## Role Concern Gaps`
section listing each failing stage and describing the correction required. A block that
restates the role's general orientation without topic-specific instantiation fails even
if all other stage sections are correct.

---

## V-02 — Pre-Commitment Enforcement Audit

**Axis**: Post-run meta-artifact — ENFORCEMENT AUDIT table after the final stage (C-17)
**Hypothesis**: Runs that declare pre-commitments — calibration blocks, update protocol
fields, role lens declarations — have no structural mechanism to verify the output
honored them. A model can declare a 1H-2M-1L spread in a Calibration Block and then
write three HIGH findings with no consequence. C-17 closes this gap by requiring a
post-run Enforcement Audit that explicitly checks each declared pre-commitment against
the actual output. Structuring the audit as a table (Stage / Pre-Commitment Type /
Declared Value / Honored / Deviation) makes violations machine-scannable: every row
where Honored = NO is a format error the model must flag before the run is complete.
The self-auditing structure also reinforces pre-commitment quality — if the model knows
it must verify its own commitments, calibration blocks become more deliberate.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] — [their orientation in one phrase]

### Calibration

MOST CRITICAL: [the single concern this role would rate highest] → HIGH
LEAST CRITICAL: [a real but lower-urgency concern] → LOW
PLANNED SPREAD: [N] findings — [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required when spread is uniform — explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern — most critical per calibration]
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

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Risk Register — Update Protocol

| Field           | Value                                                                        |
|-----------------|------------------------------------------------------------------------------|
| Trigger Events  | [specific events that require a status change — list 2-3, topic-specific]    |
| Owner Role      | [role responsible for status updates — by role title, not by person name]    |
| Revisit Cadence | [schedule or trigger condition specific to this topic's delivery rhythm]     |

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap. "Strategic priorities" does not satisfy this.

**ENFORCEMENT AUDIT — REQUIRED AFTER ALL STAGES**

After the final stage, before any summary, print a mandatory Enforcement Audit section.
The audit checks every pre-commitment declared during the run against the actual output.

```
## Enforcement Audit

| Stage        | Pre-Commitment Type    | Declared Value                  | Honored | Deviation                              |
|--------------|------------------------|---------------------------------|---------|----------------------------------------|
| [stage-name] | Calibration spread     | [e.g., 1 HIGH, 2 MED, 1 LOW]   | YES/NO  | [if NO: what was actually delivered]   |
| [stage-name] | Calibration spread     | [distribution]                  | YES/NO  | [deviation or —]                       |
| tpm          | Update Protocol        | Trigger/Owner/Cadence populated | YES/NO  | [missing fields if NO, or —]           |
[one row per pre-commitment per stage; cover all stages run; cover all pre-commitment types declared]

### Enforcement Summary

COMMITMENTS DECLARED: [N]
COMMITMENTS HONORED: [N]
VIOLATIONS: [list stage names and commitment types where Honored = NO, or NONE]
```

The Enforcement Audit is a required section. It is not optional for "clean" runs —
even a run with zero violations must include the audit table and the summary with
VIOLATIONS: NONE. A run without an Enforcement Audit section is incomplete.

---

## V-03 — Universal Per-Stage Triage Note

**Axis**: Mandatory three-field Triage Note in every stage unconditionally (C-18)
**Hypothesis**: R3 V-03 made the Triage Note conditional: write it when severity is
uniform, mark N/A when severity varies. C-18 removes the conditionality. The Triage
Note is now required in every stage regardless of severity spread — its purpose shifts
from "explain degenerate uniformity" to "document the calibration decision always."
Giving it three required fields (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR) that
must be populated in every stage prevents the model from satisfying the format with
a trivial "spread confirmed" acknowledgment: all three fields require genuine content.
HIGH DRIVER names the specific finding or concern that earned the top rank and why.
LOW ANCHOR names the finding rated least critical and why it was demoted. DISTRIBUTION
FACTOR names the reasoning dimension that shaped the spread. Together they produce a
complete calibration audit trail per stage, not just for the degenerate case.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**TRIAGE NOTE — REQUIRED IN EVERY STAGE AFTER FINDINGS**

After the Findings section, before the Verdict, every stage must include a Triage Note
with three required fields. This section is mandatory regardless of whether severity
labels vary or are uniform across findings.

```
### Triage Note

HIGH DRIVER:         [Which finding or concern was ranked most critical, and what made
                      it the top risk — name the specific concern, not just the finding ID.
                      E.g., "F-01 ranked HIGH because a missed interface contract exposes
                      the auth dependency with no recovery path before the gate."]
LOW ANCHOR:          [Which finding was ranked least critical, and why it was demoted —
                      name the concern and the reasoning. E.g., "F-03 ranked LOW because
                      the documentation gap is recoverable post-launch without user impact."]
DISTRIBUTION FACTOR: [What shaped the overall severity distribution — the primary lens
                      used to rank. E.g., "blast radius", "reversibility", "timeline
                      compression to the Q2 gate", "independent vs. shared recovery paths"]
```

All three fields must be populated with specific content in every stage. A Triage Note
that populates HIGH DRIVER but leaves LOW ANCHOR or DISTRIBUTION FACTOR as a placeholder
is a partial failure. A stage without a Triage Note section is a format error.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] — [their orientation in one phrase]

### Findings

F-01 HIGH [specific concern — grounded in this role's lens]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned; minimum 2 findings; severity labels must reflect real triage]

### Triage Note

HIGH DRIVER: [specific reason F-01 or equivalent was ranked highest]
LOW ANCHOR: [specific reason the lowest-rated finding was demoted]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the spread]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap. "Company objectives" does not satisfy this.

**TRIAGE NOTE ENFORCEMENT:** After completing all stages, scan the output. Any stage
missing a Triage Note section is a format error. Any Triage Note missing one or more
of the three required fields (HIGH DRIVER, LOW ANCHOR, DISTRIBUTION FACTOR) is a
partial failure. Append a `## Triage Note Gaps` section listing every stage and field
that requires correction. A run with zero gaps must still append TRIAGE NOTE GAPS: NONE.

---

## V-04 — Role-Lens Pre-Declaration + Universal Triage Note

**Axes**: Standalone ROLE CONCERN block (C-16) + unconditional three-field Triage Note (C-18)
**Hypothesis**: C-16 and C-18 are structural bookends of a stage — ROLE CONCERN opens
the stage by declaring what the role fears before calibration and findings begin; the
Triage Note closes the findings section by documenting how the calibration decision
actually played out. Together they create a complete per-stage intent-and-result record:
the opening declaration commits the lens, the closing note audits the severity logic.
Neither requires the other to function — they target different parts of the stage
structure — so pairing them tests whether the bookend format is coherent across all
six stages without increasing prompt complexity at either location. The hypothesis is
that the combination produces C-16 and C-18 coverage without compression artifacts
(ROLE CONCERN and Triage Note do not overlap in purpose or position).

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name.

**TWO STAGE-LEVEL FORMAT RULES:**

**RULE OPEN — ROLE CONCERN:** Every stage begins with a standalone ROLE CONCERN block
before any calibration or finding. The block contains one sentence naming what the
loaded role most fears about THIS specific topic. The sentence must reference the
artifact, domain, or risk area under review — not just the role's general orientation.
"A PM cares about alignment" fails. "PM fears the three-team dependency will slip the
Q2 gate without a named owner for the interface contract" passes. Generic role
descriptions do not satisfy this rule regardless of accuracy.

**RULE CLOSE — TRIAGE NOTE:** Every stage ends with a Triage Note section after
findings, before the Verdict. The note must contain three fields: HIGH DRIVER (which
finding was ranked most critical and why), LOW ANCHOR (which finding was ranked least
critical and why it was demoted), and DISTRIBUTION FACTOR (the reasoning dimension
that shaped the severity spread). All three fields are required in every stage
regardless of whether severity varies or is uniform. A Triage Note that omits any of
the three fields is a partial failure. A stage without a Triage Note is a format error.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] — [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear — one sentence referencing the artifact or domain;
               RULE OPEN — generic role descriptions do not satisfy this section]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] → HIGH
LEAST CRITICAL: [a real but lower-urgency concern] → LOW
PLANNED SPREAD: [N] findings — [distribution]
[TRIAGE NOTE: if spread is uniform — explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern — most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 per stage]

### Triage Note

HIGH DRIVER: [which finding drove HIGH and what made it the top risk — be specific]
LOW ANCHOR: [which finding was rated lowest and why it was demoted — be specific]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the spread —
                      e.g., "blast radius", "reversibility", "shared vs. independent
                      recovery paths before the milestone gate"]

[RULE CLOSE — all three fields required; present in every stage unconditionally]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED; 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap. Abstract references to "strategic objectives" do not satisfy this.

**FORMAT ERROR PROTOCOL:** If RULE OPEN or RULE CLOSE is violated, append a
`## Format Errors` section naming: the rule violated, the stage it occurred in, and
the correction required.

---

## V-05 — Full R4 Stack on R3 V-05 Base

**Axes**: All five R3 criteria (C-11 through C-15) as RULES A-E + three new R4 criteria
(C-16, C-17, C-18) as RULES F-H — complete v2 through v4 aspirational coverage encoded
as eight structural format requirements
**Hypothesis**: R3 V-05 built the full v3 criterion set as five format rules (RULE A:
severity discrimination C-12, RULE B: conditional itemization C-11, RULE C: status
lifecycle C-13, RULE D: calibration block C-14, RULE E: update protocol C-15) and
produced the highest expected composite of any R3 variation. V-05 extends that proven
base with three additional rules targeting the v4 delta: RULE F (standalone ROLE CONCERN
block, C-16), RULE G (universal three-field Triage Note, C-18), and RULE H (post-run
Enforcement Audit, C-17). Eight rules across eight criteria, each targeting an
independent structural location in the output — calibration governs finding generation,
the Triage Note governs post-finding documentation, ROLE CONCERN governs per-stage
opening, conditional itemization governs verdict formatting, status and update protocol
govern the risk register, and the Enforcement Audit governs the post-run document tail.
The hypothesis is that the rules occupy non-overlapping output locations, so the
composite uplift across all eight criteria is additive.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm, etc.)

**EIGHT FORMAT RULES — APPLY TO THE FULL RUN:**

**RULE A — SEVERITY DISCRIMINATION:** Within each stage's findings, severity labels
must vary. At least one finding per stage must be HIGH. At least one finding across the
full run must be below HIGH (MED or LOW). A stage where all findings carry the same
severity label violates RULE A unless RULE D (Calibration Block) or RULE G (Triage Note)
explicitly justifies the uniform distribution.

**RULE B — CONDITIONAL ITEMIZATION:** When any verdict is APPROVED WITH CONDITIONS,
BLOCKED WITH CONDITIONS, or GO WITH CONDITIONS, conditions must be listed as numbered
discrete items. Each item names: (1) what must happen, (2) who owns it by role title,
(3) the finding or risk ID driving the condition. Conditions embedded only in prose
rationale violate RULE B. Unconditional verdicts: write `CONDITIONS: N/A`.

**RULE C — RISK REGISTER STATUS:** The tpm risk register must include a Status column
with values from OPEN / WATCH / MITIGATED. At least 2 distinct status values must
appear across the register. A register without a Status column, or with all rows at the
same status, violates RULE C.

**RULE D — CALIBRATION BLOCK:** Before writing findings for each stage, print a
Calibration Block naming the most critical concern (→ HIGH), the least critical concern
(→ LOW), and the planned spread. Findings must match the declared spread. When planned
spread is uniform, include a Triage Note in the Calibration Block explaining why
uniformity is genuine. A stage with uniform severity and no Triage Note violates RULE D.

**RULE E — UPDATE PROTOCOL:** The tpm risk register must include an Update Protocol
table with three fields: Trigger Events, Owner Role, and Revisit Cadence. All three
fields must be populated with topic-specific values. Generic placeholders or a missing
Update Protocol section violates RULE E. RULE C must pass for RULE E to be scoreable.

**RULE F — ROLE CONCERN:** Every stage must begin with a standalone ROLE CONCERN block
appearing before the Calibration Block. The block contains one sentence naming what
the loaded role most fears about THIS specific topic. The sentence must reference the
artifact, domain, or risk area under review. Generic role descriptions ("a PM cares
about alignment") violate RULE F. The ROLE CONCERN must be topic-specific and appear
as the first named section after the ROLE: line in each stage.

**RULE G — UNIVERSAL TRIAGE NOTE:** Every stage must include a Triage Note section
after findings, before the Verdict. The note must contain exactly three fields: HIGH
DRIVER (which finding was ranked most critical and the specific reason), LOW ANCHOR
(which finding was ranked least critical and why it was demoted), and DISTRIBUTION
FACTOR (the reasoning dimension that shaped the severity spread). All three fields are
required in every stage regardless of severity spread. A missing Triage Note or an
incomplete one (any field absent or left as placeholder) violates RULE G.

**RULE H — ENFORCEMENT AUDIT:** After the final stage, print a mandatory Enforcement
Audit section that checks every pre-commitment declared during the run against the
actual output. The audit must cover: all Calibration Block spreads (RULE D), the Update
Protocol (RULE E), and all ROLE CONCERN declarations (RULE F). The audit format is a
table with columns: Stage / Pre-Commitment Type / Declared Value / Honored / Deviation.
Every pre-commitment declared must have a corresponding audit row. An audit row where
Honored = NO must name the specific deviation. A run without an Enforcement Audit
section violates RULE H. A run with zero violations must still produce the audit table
with VIOLATIONS: NONE in the Enforcement Summary.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] — [their orientation in one phrase]

### Role Concern

ROLE CONCERN: [topic-specific fear — one sentence referencing the artifact or domain;
               RULE F — must not be a generic role description]

### Calibration

MOST CRITICAL: [concern traceable to ROLE CONCERN] → HIGH
LEAST CRITICAL: [a real but lower-urgency concern this role would surface] → LOW
PLANNED SPREAD: [N] findings — [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required if uniform — explain why the risk landscape is genuinely
 uniform. E.g., "All findings rated HIGH because each concern independently blocks
 the go-live gate with no recovery path outside the shared milestone."]

[RULE D — Calibration Block required; RULE F — ROLE CONCERN must appear before this]

### Findings

F-01 HIGH [specific concern — most critical item per calibration]
          Owner: [role]
          Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
          Owner: [role]
          Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 per stage; RULE A + RULE D apply]

### Triage Note

HIGH DRIVER: [which finding was ranked most critical and why — name the specific
              concern, not just the ID. What made it the top risk for this role?]
LOW ANCHOR:  [which finding was ranked least critical and why it was demoted — what
              property (recoverability, blast radius, timeline) placed it lowest?]
DISTRIBUTION FACTOR: [the reasoning dimension that shaped the full severity spread
                      for this stage — e.g., "reversibility before milestone gate",
                      "shared vs. independent dependency chains", "timeline compression"]

[RULE G — all three fields required unconditionally; no stage may omit Triage Note]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

CONDITIONS:
[RULE B — numbered items if conditional, N/A if unconditional]
1. [what must happen] — Owner: [role title] — Finding: [F-NN or R-NN]
2. [what must happen] — Owner: [role title] — Finding: [F-NN or R-NN]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Triage Note, before Verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; RULE C — Status column, 2+ distinct values]

### Risk Register — Update Protocol

| Field           | Value                                                                       |
|-----------------|-----------------------------------------------------------------------------|
| Trigger Events  | [2-3 specific events that require a status change — topic-specific]         |
| Owner Role      | [role title responsible for updates — not a person name]                    |
| Revisit Cadence | [schedule or condition specific to this topic's delivery rhythm]            |

[RULE E — all three fields required; generic placeholders violate this section]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk or finding ID]

CONDITIONS:
[RULE B — numbered items if GO WITH CONDITIONS, N/A if GO or NO-GO]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission       | Program         | Artifact/Topic | Alignment               |
|------------------------|-----------------|----------------|-------------------------|
| [named mission]        | [program name]  | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named — "strategic goals" fails C-08]
```

**CROSS-STAGE COHERENCE:** When running --stage all, later stages should reference
prior-stage findings where relevant. Format: `[prior stage] F-[N]: confirm / escalate /
contradict — [one sentence]`. Aim for at least 2 cross-stage references across the run.

**ENFORCEMENT AUDIT — REQUIRED AFTER FINAL STAGE:**

```
## Enforcement Audit

| Stage        | Pre-Commitment Type    | Declared Value                         | Honored | Deviation                         |
|--------------|------------------------|----------------------------------------|---------|-----------------------------------|
| [stage-name] | Role Concern           | [first few words of declared concern]  | YES/NO  | [deviation if NO, or —]           |
| [stage-name] | Calibration spread     | [e.g., 1 HIGH, 2 MED, 1 LOW]          | YES/NO  | [actual spread if NO, or —]       |
| tpm          | Update Protocol        | Trigger/Owner/Cadence populated        | YES/NO  | [missing fields if NO, or —]      |
[one row per pre-commitment per stage; cover all stages run; RULE H]

### Enforcement Summary

COMMITMENTS DECLARED: [N]
COMMITMENTS HONORED: [N]
VIOLATIONS: [list stage + commitment type for each Honored = NO row, or NONE]
```

**FORMAT ERROR PROTOCOL:** If any of RULES A through H are violated and not already
captured in the Enforcement Audit, append a `## Format Errors` section after the
Enforcement Audit. Each entry names: the rule violated, the stage it occurred in, and
the correction required.
