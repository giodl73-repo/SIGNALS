---
skill: quest-variate
skill_target: corps-rob
round: 3
date: 2026-03-16
rubric_version: 3
---

# Variate R3 — corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R3 focus: the two new v3 aspirational criteria (C-14, C-15) were not explicitly
targeted in R2. R3 explores axes that surface these gaps.

- C-14: Pre-finding severity calibration — holistic distribution decided before any
  finding is written; Triage Note required when all findings land at the same level.
- C-15: Risk register update protocol — Update Protocol section specifying trigger
  events, owner role, and revisit cadence; makes the register a process artifact.

R2 V-01 used a "silent triage step" to target C-12. R3 escalates: V-01 makes
calibration an explicit printed artifact (Calibration Block) that commits the
severity distribution before any finding is written. V-02 formalizes C-15 as a
structured process table. V-03 enforces the Triage Note sub-requirement of C-14
as a conditional mandatory section. V-04 combines both new v3 criteria. V-05
builds the full v3 stack on R2 V-04's proven all-criteria encoding.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Calibration block (explicit printed severity distribution before findings) | V-01 | C-14 |
| Update protocol as structured process table (trigger/owner/cadence) | V-02 | C-15 |
| Triage Note enforcement (conditional mandatory section on uniform severity) | V-03 | C-14 Triage Note sub-requirement |
| Calibration block + update protocol (both new v3 criteria as format rules) | V-04 | C-14, C-15 |
| Full v3 stack on R2 V-04 base (all v2 criteria + C-14 + C-15) | V-05 | C-11, C-12, C-13, C-14, C-15 |

---

## V-01 — Calibration Block

**Axis**: Pre-calibration as explicit printed artifact (C-14)
**Hypothesis**: R2 V-01 required a "silent triage step" — the model did it mentally
but the output gave no evidence it happened. C-14 checks for process evidence, not
just outcome (C-12 already checked outcome). Making the calibration an explicit
**Calibration Block** printed before findings forces the model to commit to a full
severity distribution in writing before writing any finding. The commitment is
verifiable, the spread is structurally required, and the Triage Note sub-requirement
(required when all findings are the same level) becomes a first-class conditional
rather than an afterthought.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.roles/` — load orientation and lens for each assigned role.
3. Fallback if files absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**CALIBRATION BLOCK — REQUIRED BEFORE FINDINGS IN EACH STAGE**

Before writing any finding for a stage, print this block:

```
### Calibration

ROLE LENS: [what this role most fears about this topic — one phrase]
MOST CRITICAL: [the single concern this role would rate highest] → HIGH
LEAST CRITICAL: [a real but low-urgency concern this role would flag] → LOW
PLANNED SPREAD: [N] findings — [e.g., 1 HIGH, 2 MED, 1 LOW]
```

The Calibration Block is printed. It commits the severity distribution before any
finding is written. Findings must match the planned spread declared in the block.

**TRIAGE NOTE — REQUIRED WHEN SPREAD IS UNIFORM**

If all planned findings in a stage share the same severity level, the Calibration
Block must include a Triage Note:

```
TRIAGE NOTE: All findings rated [level] because [specific reason — e.g., "every
concern blocks the same go-live gate and no recovery path exists outside that window"].
```

A Calibration Block with a uniform spread and no Triage Note is a format error.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Calibration

ROLE LENS: [what this role most fears about this topic]
MOST CRITICAL: [concern] → HIGH
LEAST CRITICAL: [concern] → LOW
PLANNED SPREAD: [N] findings — [distribution]
[TRIAGE NOTE: if spread is uniform — reason for justified uniformity]

### Findings

F-01 HIGH [specific concern — the most critical item per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern — from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 findings per stage; must match declared spread]

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

At least one finding must name a specific S-office mission by name and trace its alignment
or gap to the artifact under review. "Strategic goals" does not satisfy this.

**CALIBRATION ENFORCEMENT:** If any stage's findings do not match the severity distribution
declared in its Calibration Block, append a `## Calibration Errors` section naming the
stage, the declared spread, and the actual spread found.

---

## V-02 — Update Protocol as Process Document

**Axis**: Risk register update protocol as structured process table (C-15)
**Hypothesis**: R2 V-03 introduced "Update Protocol" as a brief inline prose section —
three bullet points describing amendment behavior. C-15 requires more than behavior
guidance: it requires a document that specifies trigger events, owner role, and revisit
cadence as discrete named fields. Structuring the Update Protocol as a required table
with mandatory columns (Trigger / Owner Role / Cadence) makes C-15 pass conditions
verifiable by cell existence rather than prose interpretation. The model cannot satisfy
C-15 by paraphrasing — all three fields must appear.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Findings

F-01 [HIGH/MED/LOW] [specific concern grounded in this role's lens]
     Owner: [role]
     Resolution: [concrete action]

F-02 [HIGH/MED/LOW] [second specific concern]
     Owner: [role]
     Resolution: [concrete action]

[minimum 2 findings per stage]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

The risk register is a living artifact that survives the ROB session. Producing it
requires two components: the register itself and the process that keeps it current.
Both are required.

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

| Field          | Value                                                                        |
|----------------|------------------------------------------------------------------------------|
| Trigger Events | [specific events or milestones that require status change — list 2-3]        |
| Owner Role     | [the role responsible for updating status — named by role, not by person]    |
| Revisit Cadence| [schedule or trigger condition — e.g., "each sprint close", "before each milestone gate"] |

The Update Protocol is a mandatory companion to the register. A risk register without
an Update Protocol section is a snapshot; one with it is a process artifact. All three
fields (Trigger Events, Owner Role, Revisit Cadence) must be populated with values
specific to the topic under review — generic placeholders do not satisfy this section.

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its
alignment or gap. "Strategic priorities" does not satisfy this.

**UPDATE PROTOCOL ENFORCEMENT:** A tpm stage output that includes a risk register
but omits the Update Protocol section is a format error. A protocol with any of the
three required fields missing or left as a generic placeholder is a partial failure —
append a `## Protocol Gaps` section naming which fields require population.

---

## V-03 — Triage Note Enforcement

**Axis**: Conditional mandatory Triage Note section when severity is uniform (C-14 sub-requirement)
**Hypothesis**: C-14 has two pass paths: (a) demonstrated HIGH-to-LOW spread across
findings, or (b) a Triage Note explaining why uniform severity is genuinely justified.
R2 variations targeted path (a) by requiring spread. R3 V-03 targets path (b) by
making the Triage Note a conditional mandatory section — always present in the stage
document, filled in with justification when severity is uniform, or marked N/A when
spread is demonstrated. This makes both C-14 pass paths structurally enforced rather
than optional. The N/A path creates evidence of calibration even when spread is
natural; the filled path provides documented rationale when uniformity is genuine.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Findings

F-01 [HIGH/MED/LOW] [specific concern grounded in this role's lens — most critical]
     Owner: [role]
     Resolution: [concrete action]

F-02 [HIGH/MED/LOW] [second concern — from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[minimum 2 findings per stage; severity labels must reflect this role's actual priorities]

### Triage Note

[If severity varies across findings — write: TRIAGE: Spread confirmed. HIGH = [F-N],
 LOW = [F-N]. Distribution reflects [role]'s natural prioritization.]

[If all findings carry the same severity — write: TRIAGE NOTE: All findings rated
 [severity] because [specific reason — must explain why the risk landscape is genuinely
 uniform, not just "all are important". E.g., "all three concerns share the same
 go-live dependency with no independent mitigation path"]. A Triage Note that restates
 the findings without explaining uniformity does not satisfy this section.]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]
```

The Triage Note section is mandatory in every stage. Its content varies based on the
actual severity distribution — but it is never omitted. A stage without a Triage Note
section is a format error regardless of the severity spread.

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, after Triage Note, before verdict:

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

**TRIAGE NOTE ENFORCEMENT:** Scan the completed output. Any stage missing a Triage
Note section is a format error — append a `## Triage Note Gaps` section listing the
stage names that require correction. A Triage Note that only restates the finding
titles without explaining the severity distribution also fails.

---

## V-04 — Calibration Block + Update Protocol

**Axes**: Pre-calibration block (C-14) + update protocol as process document (C-15)
**Hypothesis**: C-14 and C-15 are structurally independent — C-14 governs findings
output across all stages, C-15 governs the tpm risk register process artifact.
Encoding both as format rules in a single variation targets the full v3 delta without
relying on combination effects. V-01 showed that the Calibration Block works by
committing the severity distribution before findings are written. V-02 showed that
the Update Protocol works by requiring three discrete named fields. Pairing them
produces C-14 + C-15 coverage while keeping the prompt structurally coherent — each
rule applies to a different part of the output, so they do not compete.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name.

**TWO FORMAT RULES — APPLY TO THE FULL RUN:**

**RULE D — CALIBRATION BLOCK:** Before writing any finding for a stage, print a
Calibration Block that commits the severity distribution for that stage. The block
must name the most critical concern (→ HIGH), the least critical concern (→ LOW), and
the planned spread. Findings must match the declared spread. When all findings in a
stage are the same severity level, the Calibration Block must include a Triage Note
explaining why the uniform distribution is genuinely justified — not just "all are
important." A stage where severity is uniform with no Triage Note is a format error.

**RULE E — UPDATE PROTOCOL:** The tpm stage risk register must be accompanied by an
Update Protocol table with three required fields: Trigger Events (what events require
a status update), Owner Role (who performs the update, by role not by name), and
Revisit Cadence (how frequently the register is reviewed). A risk register without an
Update Protocol section, or a protocol with any of the three fields unpopulated, is a
format error.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Calibration

MOST CRITICAL: [concern] → HIGH
LEAST CRITICAL: [concern] → LOW
PLANNED SPREAD: [N] findings — [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: required if spread is uniform — explain why uniformity is genuine]

### Findings

F-01 HIGH [specific concern — most critical per calibration]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 per stage; must match Calibration spread]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

CONDITIONS:
[If APPROVED WITH CONDITIONS — numbered items: (1) what, (2) owner, (3) finding ID.
 If unconditional — CONDITIONS: N/A]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings and calibration section, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status    |
|------|-----------------------------|----------|------------|------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH     |
[minimum 3 rows; at least 1 HIGH; RULE C from v2 — Status column, 2+ distinct values]

### Risk Register — Update Protocol

| Field           | Value                                                                    |
|-----------------|--------------------------------------------------------------------------|
| Trigger Events  | [2-3 specific events that require a status change — topic-specific]      |
| Owner Role      | [role responsible for updates — by role title, not by name]              |
| Revisit Cadence | [schedule or trigger condition specific to this topic's delivery rhythm] |

[RULE E — all three fields required; generic placeholders fail this section]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk ID]

CONDITIONS:
[If GO WITH CONDITIONS — numbered items per RULE B. If GO or NO-GO — CONDITIONS: N/A]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission and trace its alignment
or gap. Abstract references to "strategic priorities" do not satisfy this.

**FORMAT ERROR PROTOCOL:** If RULE D or RULE E are violated, append a `## Format Errors`
section naming: the rule violated, the stage it occurred in, and the correction required.

---

## V-05 — Full v3 Stack on R2 V-04 Base

**Axes**: All three v2 criteria (C-11, C-12, C-13 from R2 V-04) + calibration block
(C-14) + update protocol process document (C-15) — the full v3 target set encoded as
structural format requirements
**Hypothesis**: R2 V-04 produced the highest expected composite by encoding all three
v2 aspirational criteria as format rules (RULE A: severity discrimination, RULE B:
conditional itemization, RULE C: status lifecycle). V-05 extends that proven base with
two additional rules targeting the v3 criteria: RULE D (calibration block, C-14) and
RULE E (update protocol, C-15). Five rules, five criteria, all encoded as format
requirements rather than guidance. The hypothesis is that each rule targets an
independent part of the output structure — calibration governs findings, conditional
itemization governs verdicts, status and update protocol govern the risk register —
so the rules do not compete and the composite uplift should be additive.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.roles/` — load orientation and lens for each assigned role.
3. Fallback if absent: assign by stage name (PM for pm stage, TPM for tpm, etc.)

**FIVE FORMAT RULES — APPLY TO THE FULL RUN:**

**RULE A — SEVERITY DISCRIMINATION:** Within each stage's findings, severity labels
must vary. At least one finding per stage must be HIGH. At least one finding across the
full run must be below HIGH (MED or LOW). A stage where all findings carry the same
severity label violates RULE A unless RULE D (Triage Note) is satisfied.

**RULE B — CONDITIONAL ITEMIZATION:** When any verdict is APPROVED WITH CONDITIONS,
BLOCKED WITH CONDITIONS, or GO WITH CONDITIONS, conditions must be listed as numbered
discrete items. Each item names: (1) what must happen, (2) who owns it, (3) the finding
or risk ID driving the condition. Conditions embedded only in prose rationale are a
format error. Unconditional verdicts: write `CONDITIONS: N/A`.

**RULE C — RISK REGISTER STATUS:** The tpm risk register must include a Status column
with values from OPEN / WATCH / MITIGATED. At least 2 distinct status values must
appear. A register without a Status column, or with all rows in the same status, is a
format error.

**RULE D — CALIBRATION BLOCK:** Before writing findings for each stage, print a
Calibration Block that names the most critical concern (→ HIGH), the least critical
concern (→ LOW), and the planned spread. Findings must match the declared spread. When
planned spread is uniform, include a Triage Note explaining why uniformity is genuine.
A stage with uniform severity and no Triage Note violates RULE D even if RULE A is
technically satisfied.

**RULE E — UPDATE PROTOCOL:** The tpm risk register must include an Update Protocol
table with three fields: Trigger Events, Owner Role, and Revisit Cadence. All three
fields must be populated with topic-specific values. Generic placeholders or a missing
Update Protocol section violates RULE E. RULE C must pass before RULE E is scoreable.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Calibration

MOST CRITICAL: [concern this role would rate highest] → HIGH
LEAST CRITICAL: [concern this role would flag but not lose sleep over] → LOW
PLANNED SPREAD: [N] findings — [distribution, e.g., 1 HIGH, 2 MED, 1 LOW]
[TRIAGE NOTE: if uniform — explain why the risk landscape is genuinely uniform.
 E.g., "All findings rated HIGH because each concern independently blocks the go-live
 gate with no recovery path outside the shared milestone."]

### Findings

F-01 HIGH [specific concern — the most critical item this role surfaced]
          Owner: [role]
          Resolution: [concrete action]

F-02 MED  [second concern from this role's domain]
          Owner: [role]
          Resolution: [concrete action]

[F-03 LOW if planned in spread; minimum 2 per stage; RULE A + D apply]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

CONDITIONS:
[RULE B — numbered items if conditional, N/A if unconditional]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After calibration and findings, before verdict:

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
[minimum 1 row; mission must be named — "strategic goals" fails]
```

**CROSS-STAGE COHERENCE:** When running --stage all, later stages should reference
prior-stage findings where relevant. Format: `[prior stage] F-[N]: confirm / escalate /
contradict — [one sentence]`. At least 2 cross-stage references across the full run.

**FORMAT ERROR PROTOCOL:** If any of Rules A through E are violated, append a
`## Format Errors` section after the final stage. Each entry names: the rule violated,
the stage it occurred in, and the correction required.
