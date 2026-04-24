---
skill: quest-variate
skill_target: corps-rob
round: 2
date: 2026-03-16
rubric_version: 2
---

# Variate R2 — corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R2 focus: the three new v2 aspirational criteria (C-11, C-12, C-13) were not explicitly
targeted in R1. R2 explores axes that surface these gaps.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Severity triage protocol (explicit calibration step before findings) | V-01 | C-12 |
| Conditional verdict itemization (structured CONDITIONS: block template) | V-02 | C-11 |
| Living risk register (status lifecycle as first-class artifact) | V-03 | C-13 |
| All three new aspirational criteria encoded as formatting rules | V-04 | C-11, C-12, C-13 |
| Descriptive register (R1 V-03 best practice) + living register + severity triage | V-05 | C-02, C-12, C-13 |

---

## V-01 — Severity Triage Protocol

**Axis**: Severity calibration (C-12)
**Hypothesis**: An explicit triage step before writing findings — where the model must
name the single most critical concern and the single least critical concern before
assigning any labels — forces severity discrimination by anchoring the distribution.
Without this anchor, models inflate toward HIGH uniformly because HIGH reads as thorough.
The triage step makes the spread structurally required before any label appears.

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

**SEVERITY TRIAGE — RUN BEFORE WRITING EACH STAGE'S FINDINGS**

Before writing any finding for a stage, complete this triage step silently:

1. What is the single most critical concern this role would surface? (This will be HIGH.)
2. What is the single least critical concern — something real but low urgency? (This will be LOW.)
3. All other concerns fall between HIGH and LOW.

The triage step is not printed. It disciplines the output. A stage where all findings
carry the same severity label indicates triage was skipped. HIGH must appear at least
once per stage; at least one finding across the full run must be rated below HIGH.

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Findings

F-01 HIGH [specific concern grounded in this role's lens — the most critical item they found]
     Owner: [role]
     Resolution: [concrete action]

F-02 MED [second concern, less urgent but real — from this role's domain]
     Owner: [role]
     Resolution: [concrete action]

[F-03 LOW if applicable; minimum 2 findings per stage; severity must vary across findings]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID from this stage]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation            |
|------|-----------------------------|----------|------------|-----------------------|
| R-01 | [specific risk]             | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk]             | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk]             | LOW      | LOW        | [concrete mitigation] |
[minimum 3 entries; severity must vary — R-01 HIGH is required; R-03 must be below MED]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one finding or risk ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its alignment
or gap to the artifact. Generic "strategic goals" references do not satisfy this.

**SEVERITY ENFORCEMENT:** If the completed run has no finding rated below HIGH, append
a `## Triage Note` section identifying which stage's findings were over-inflated and what
the corrected severity distribution should be.

---

## V-02 — Conditional Verdict Itemization

**Axis**: Conditional verdict structure (C-11)
**Hypothesis**: Embedding a mandatory `CONDITIONS:` block template inside the verdict
section — identical to the finding format — makes C-11 compliance the structural default
rather than an improvement. When the template is always present, the model either fills
it or explicitly marks it as not applicable. Prose rationale as a substitute becomes
structurally awkward rather than structurally easy.

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

F-01 [HIGH/MED/LOW] [specific concern — not a category, specific to this role's lens]
     Owner: [role]
     Resolution: [concrete action]

F-02 [HIGH/MED/LOW] [second specific concern]
     Owner: [role]
     Resolution: [concrete action]

[minimum 2 findings per stage]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

CONDITIONS:
[If APPROVED WITH CONDITIONS or GO WITH CONDITIONS — list each condition as a numbered item.
 Each item must state: (1) what must happen, (2) who owns it, (3) the finding or risk ID driving it.
 Example:
   1. PM must confirm rollout sequencing aligns with Q3 migration window — Owner: PM Lead — Ref: F-02
   2. Arch-board sign-off on contract versioning approach required before ship — Owner: Principal Architect — Ref: F-01
 If verdict is unconditional — write: CONDITIONS: N/A]
```

The CONDITIONS: block is mandatory in every verdict. N/A is a valid value for unconditional
verdicts. A verdict that states conditions only inside the Rationale sentence fails
C-11 — conditions must be enumerated discretely, not embedded in prose.

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation            |
|------|-----------------------------|----------|------------|-----------------------|
| R-01 | [specific risk]             | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk]             | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk]             | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one finding or risk ID]

CONDITIONS:
[If GO WITH CONDITIONS — list numbered items as above.
 Each item: (1) what resolves this condition, (2) owner, (3) risk or finding ID.
 If GO or NO-GO — write: CONDITIONS: N/A]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission and trace its alignment or gap.

**CONDITIONS ENFORCEMENT:** A conditional verdict with zero items in its CONDITIONS: block
is a format error. Re-write the verdict as APPROVED if no conditions can be named — do not
issue a conditional verdict without itemizing the conditions.

---

## V-03 — Living Risk Register

**Axis**: Risk register as a living artifact (C-13)
**Hypothesis**: Framing the risk register as a persistent state document — not a snapshot —
and requiring status values (OPEN / WATCH / MITIGATED) plus update semantics produces C-13
compliance and makes the register useful beyond the initial ROB session. Without explicit
status framing, models produce a risk list that reads as past tense — valid at the moment
of writing, unusable for re-review. Status makes each row a present-tense state.

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

The risk register is a living artifact. Each row carries a status that can be updated
after the initial ROB run as risks are resolved. Status vocabulary: OPEN (unmitigated,
requires action) / WATCH (mitigation in progress, not confirmed) / MITIGATED (resolution
confirmed — retain row for audit trail).

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                        | Status    |
|------|-----------------------------|----------|------------|-----------------------------------|-----------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation action]      | OPEN      |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation action]      | OPEN      |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation action]      | WATCH     |
[minimum 3 rows; at least 1 HIGH severity; Status must be one of OPEN / WATCH / MITIGATED;
 at least 2 distinct Status values across the register]

### Risk Register — Update Protocol

When this ROB is re-run or amended:
- Update Status for any risk that has been mitigated (do not delete rows — mark MITIGATED)
- Add new rows for newly discovered risks
- Retain the original Mitigation field; append updated notes as: "[updated: action]"

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk by R-ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its alignment
or gap to the artifact under review. "Strategic priorities" does not satisfy this.

**STATUS ENFORCEMENT:** A risk register without a Status column, or with all rows in the
same status, fails C-13. At least 2 distinct status values must appear across the register.
Initial ROB runs default to OPEN / WATCH; MITIGATED is only valid if the mitigation is
confirmed in the same run.

---

## V-04 — All Three New Criteria as Formatting Rules

**Axes**: C-11 (conditional itemization) + C-12 (severity discrimination) + C-13 (status
lifecycle) — all three v2 aspirational criteria encoded directly as formatting rules
**Hypothesis**: Encoding all three new rubric criteria as structural format requirements —
not guidance or suggestions — makes them default-on behavior. Each criterion becomes a
format error to violate rather than a quality improvement to aspire to. Combined with the
standard essential-criteria structure from R1 best practice, this produces the highest
expected R2 composite uplift by targeting the full v2 delta in one prompt.

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

**THREE FORMAT RULES — APPLY TO EVERY STAGE:**

**RULE A — SEVERITY DISCRIMINATION:** Within each stage's findings, severity labels must
vary. At least one finding must be rated HIGH. At least one finding across the full run
must be rated below HIGH (MED or LOW). A uniform-severity stage is a format error.

**RULE B — CONDITIONAL ITEMIZATION:** When any verdict is APPROVED WITH CONDITIONS, BLOCKED
WITH CONDITIONS, or GO WITH CONDITIONS, the conditions must be listed as numbered discrete
items. Each item must name: (1) what must happen, (2) who owns it, (3) the finding or risk
ID that drives the condition. Conditions buried inside the Rationale sentence are a format
error. Unconditional verdicts: write `CONDITIONS: N/A`.

**RULE C — RISK REGISTER STATUS:** The TPM risk register must include a Status column with
values from: OPEN / WATCH / MITIGATED. At least 2 distinct status values must appear.
A register without a Status column, or with all rows in the same status, is a format error.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

### Findings

F-01 HIGH  [specific concern grounded in this role's lens — most critical item]
           Owner: [role]
           Resolution: [concrete action]

F-02 MED   [second specific concern from this role's domain]
           Owner: [role]
           Resolution: [concrete action]

[F-03 LOW if applicable; minimum 2 per stage; RULE A applies — severity must vary]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

CONDITIONS:
[RULE B — numbered items if conditional, N/A if unconditional]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation                   | Status     |
|------|-----------------------------|----------|------------|------------------------------|------------|
| R-01 | [specific risk — named]     | HIGH     | HIGH       | [concrete mitigation]        | OPEN       |
| R-02 | [specific risk — named]     | MED      | MED        | [concrete mitigation]        | OPEN       |
| R-03 | [specific risk — named]     | LOW      | LOW        | [concrete mitigation]        | WATCH      |
[minimum 3 rows; at least 1 HIGH; RULE C — Status column required, 2+ distinct values]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one risk or finding ID]

CONDITIONS:
[RULE B — numbered items if GO WITH CONDITIONS, N/A if GO or NO-GO]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission and trace its alignment or
gap. "Strategic goals" or "company priorities" does not satisfy this criterion.

**EXEC-OFFICE — MISSION CASCADE:**

```
### Mission Cascade

| S-Office Mission       | Program         | Artifact/Topic | Alignment               |
|------------------------|-----------------|----------------|-------------------------|
| [named mission]        | [program name]  | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named]
```

**CROSS-STAGE COHERENCE:** When running --stage all, later stages should reference
prior-stage findings where relevant. Format: `[prior stage] F-[N]: confirm / escalate /
contradict — [one sentence]`. At least 2 cross-stage references across the full run.

**FORMAT ERROR PROTOCOL:** If any of Rules A, B, or C are violated, append a
`## Format Errors` section after the final stage naming: the rule violated, the stage
it occurred in, and the correction required.

---

## V-05 — Descriptive Register + Living Risk Register + Severity Triage

**Axes**: Phrasing register (descriptive/role-oriented, from R1 V-03) + living risk
register (C-13) + severity triage (C-12)
**Hypothesis**: R1 V-03's descriptive register produced the strongest C-02 signal —
findings that read as if the role actually wrote them rather than executing a format
checklist. Pairing that natural-voice framing with the two most structurally verifiable
new criteria (C-12, C-13) produces strong C-02 + C-12 + C-13 coverage without the
mechanical feel that undercuts role authenticity when too many rules are stacked.
The severity triage emerges from the role's own priorities, not a fixed ordering rule.

---

You are running `/corps-rob`. Your job is to conduct a corporate Review of Business for
the given topic, simulating each stage as it would run in a real software organization.

**What a ROB is:** A staged review where each function examines a topic through their own
lens before the organization commits to shipping or investing. Every stage surfaces a
different kind of risk — and creates a record before it is too late to act.

**Stages to run** (default: all, in this order):
leadership → teams → pm → tpm → arch-board → exec-office

- `--stage [name]` runs one stage
- `--stage all` runs the full sequence
- `--scope [group]` limits roles to one division from org.yaml

**The roles:** Load each stage's persona from `.roles/` via `org.yaml`. Each persona
has an orientation — a documented lens that shapes what problems they notice. A PM notices
adoption and cross-team alignment risk. A TPM notices schedule slip and unresolved
dependencies. A principal architect notices interface coupling and long-term maintenance
burden. An exec sponsor notices strategic fit and funding risk.

Let the loaded orientation shape what each stage finds. Not a checklist — this role's
specific concerns about this specific topic. Generic findings that any role could have
written indicate the persona was not loaded.

**Severity from the role's own triage:** Each role carries a natural prioritization.
A TPM's highest severity concern is not the same as a PM's. Before writing findings for
each stage, identify: what is this role most alarmed about? That is HIGH. What would they
flag but not lose sleep over? That is LOW. Everything else is MED. The severity
distribution should reflect this role's judgment — not a uniform assessment.

**What each stage document looks like:**

Each stage reads as if the named role wrote it. The role is identified at the top. The
findings reflect what that role would notice — not what anyone would notice. Each finding
carries a severity grounded in the role's priorities and names an owner and a next step.
The document closes with a verdict.

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

Findings:
F-01 HIGH — [what this role found, in their voice — the thing they are most alarmed about]
     Owner: [role]
     Resolution: [what needs to happen]

F-02 MED  — [second concern from this role's domain — real but not the top priority]
     Owner: [role]
     Resolution: [action]

[F-03 LOW if applicable; minimum 2 per stage; severity must reflect role-specific triage]

Verdict: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
[one sentence, in this role's voice, citing a specific finding]

[If conditional: list each condition as a numbered item — what must happen, who owns it,
 which finding drives it. Conditions embedded only in prose rationale are insufficient.]
```

**The tpm stage** produces a risk register that is a living artifact — a document a
reviewer can return to as risks are resolved. Each risk carries a status that tracks its
current state beyond the initial ROB session:

```
### Risk Register

| ID   | Risk                     | Severity | Likelihood | Mitigation                        | Status    |
|------|--------------------------|----------|------------|-----------------------------------|-----------|
| R-01 | [risk — specific name]   | HIGH     | HIGH       | [concrete mitigation action]      | OPEN      |
| R-02 | [risk — specific name]   | MED      | MED        | [concrete mitigation action]      | OPEN      |
| R-03 | [risk — specific name]   | LOW      | LOW        | [concrete mitigation action]      | WATCH     |

Status values: OPEN (unmitigated, action needed) / WATCH (mitigation in progress) /
MITIGATED (resolution confirmed — keep row for audit trail).
Minimum 3 rows; at least 1 HIGH; at least 2 distinct Status values.

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS — [primary rationale citing a risk ID or finding ID]
[If GO WITH CONDITIONS: list conditions as numbered items — what, who, which risk/finding]
```

**The exec-office stage** traces at least one named executive-level mission to this topic
and states whether the work aligns or there is a gap. "This supports our strategic
priorities" is not enough — the mission must be named and the alignment or gap must be
specific.

**Across the full run:** Each role's severity judgment should produce a distribution
across the run where not everything is HIGH. A run where every finding from every stage
carries the same severity label signals that the role-specific triage step was skipped.

When a concern from an earlier stage resurfaces in a later stage, name it: confirm,
escalate, or contradict. This makes the escalation chain (teams → pm → tpm) visible
rather than implicit.
