---
skill: quest-variate
skill_target: corps-rob
round: 1
date: 2026-03-16
rubric_version: 1
---

# Variate R1 — corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (risk-first vs standard stage order) | V-01 |
| Output format (table-centric findings vs prose list) | V-02, V-05 |
| Phrasing register (imperative/procedural vs descriptive/role-oriented) | V-03 |
| Lifecycle emphasis + cross-stage coherence (explicit gate handoffs + escalation protocol) | V-04 |
| Inertia framing (inertia anchor + per-stage inertia check) | V-05 |

---

## V-01 — Role Sequence: Risk-First Ordering

**Axis**: Role sequence
**Hypothesis**: Running tpm before teams prevents the optimism-bubble failure mode where teams
self-review positively and TPM must override them. Front-loading risk framing calibrates every
subsequent stage against an established risk baseline, producing more calibrated findings and
fewer verdict reversals across the run.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGE ORDER (RISK-FIRST):**
tpm → arch-board → leadership → teams → pm → exec-office

If `--stage [name]` is given, run only that stage (ignore sequence).
If `--scope [group]` is given, filter org.yaml roles to that division or tribe only.
If `--stage all` is given, run all stages in the risk-first order above.

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. If `org.yaml` is absent, use: tpm=TPM Lead, arch-board=Principal Architect,
   leadership=VP Product, teams=Team Leads, pm=Senior PM, exec-office=Chief of Staff.

**FOR EACH STAGE, PRODUCE THIS DOCUMENT:**

```
## Stage: [stage-name]

ROLE: [name loaded from .craft/roles/] — [their orientation in one phrase]

### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens — not a category] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
[add more if needed; minimum 2 per stage]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence, specific to this stage's findings]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict, include:

```
### Risk Register

| ID   | Risk                        | Severity | Likelihood | Mitigation            |
|------|-----------------------------|----------|------------|-----------------------|
| R-01 | [specific risk]             | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk]             | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk]             | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least one rated HIGH severity]

### Go/No-Go

GO / NO-GO / GO WITH CONDITIONS
Rationale: [cite at least one finding or risk by ID]
```

**SEQUENCE NOTE:** Because tpm runs before teams and pm in this ordering, the risk register is
established before team self-reviews occur. When running the teams and pm stages, check whether
any team-level findings confirm or contradict a risk in the tpm register. If they do, cite the
risk ID.

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage is its own labeled section.

---

## V-02 — Output Format: Table-Centric

**Axis**: Output format
**Hypothesis**: Tabular output for findings and risk register makes C-03 format compliance
machine-verifiable and C-07 (structured risk register) structurally impossible to fail. Table
format forces owner and resolution into discrete columns, eliminating the most common C-04
failure: findings without explicit resolution paths.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

Read `org.yaml`. Read `.craft/roles/` for each stage's assigned persona.
Fallback if not found: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**OUTPUT FORMAT: ALL FINDINGS IN TABLES**

For each stage:

```
## Stage: [stage-name]

ROLE: [name] | ORIENTATION: [lens from .craft/roles/ — one phrase]

**Findings**

| ID   | Finding                        | Severity | Owner  | Resolution               |
|------|-------------------------------|----------|--------|--------------------------|
| F-01 | [specific concern]            | HIGH     | [role] | [concrete action]        |
| F-02 | [specific concern]            | MED      | [role] | [concrete action]        |
[minimum 2 rows; severity must differ across at least 2 rows]

**Verdict:** APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence]
```

**TPM STAGE — ADDITIONAL TABLES:**

```
**Risk Register**

| ID   | Risk             | Severity | Likelihood | Mitigation        | Status |
|------|-----------------|----------|------------|-------------------|--------|
| R-01 | [specific risk] | HIGH     | HIGH       | [mitigation]      | OPEN   |
| R-02 | [specific risk] | MED      | MED        | [mitigation]      | OPEN   |
| R-03 | [specific risk] | LOW      | LOW        | [mitigation]      | WATCH  |
[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED]

**Go/No-Go**

| Decision              | Rationale                                         |
|-----------------------|---------------------------------------------------|
| GO WITH CONDITIONS    | [cite finding or risk ID from tables above]       |
[Decision must be: GO / NO-GO / GO WITH CONDITIONS — one row, no ambiguity]
```

**EXEC-OFFICE STAGE — ADDITIONAL TABLE:**

```
**Mission Cascade**

| S-Office Mission   | Program         | Artifact/Topic | Alignment           |
|--------------------|-----------------|----------------|---------------------|
| [named mission]    | [program name]  | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named — "strategic goals" fails this criterion]
```

**OUTPUT RULE:** No prose finding lists. All findings in tables. Each stage is its own labeled
section with its own findings table. Stages are never merged.

---

## V-03 — Phrasing Register: Descriptive / Role-Oriented

**Axis**: Phrasing register
**Hypothesis**: Describing what each role cares about — rather than issuing procedural ENFORCE
instructions — activates the persona's lens more naturally. The model writes from inside the
role rather than executing a checklist, producing richer role-loaded findings that satisfy C-02
without mechanical compliance.

---

You are running `/corps-rob`. Your job is to conduct a corporate Review of Business for the
given topic, simulating each stage as it would actually run in a large software organization.

**What a ROB is:** A staged review process where each function examines a topic through their
own lens before the company commits to shipping or investing. The ROB surfaces what engineering,
PM, TPM, and executive leadership each care about — and creates a record before it is too late
to act.

**Stages to run** (default: all, in this order):
leadership, teams, pm, tpm, arch-board, exec-office

- `--stage [name]` runs one stage
- `--scope [group]` limits roles to one division from org.yaml

**The roles:** Load each stage's persona from `.craft/roles/` via `org.yaml`. Each persona
has an orientation — a documented lens that shapes which problems they notice. An exec sponsor
notices strategic fit and funding risk. A TPM notices schedule slip and unresolved dependencies.
A principal architect notices interface coupling and long-term maintenance burden. Let the loaded
orientation shape what each stage finds — not a generic list of concerns, but this role's
specific anxieties about this specific topic.

**What each stage document should look like:**

Each stage document reads as if the named role actually ran the review. The role is identified
at the top. The findings are specific to what that role would notice — not generic observations
anyone could have made. Each finding carries a severity and names someone who owns it and what
they should do. The document closes with a verdict.

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/ or org.yaml] — [their orientation in one phrase]

Findings:
F-01 [HIGH/MED/LOW] — [what this role found, in their voice] — Owner: [role] — Resolution: [what needs to happen]
F-02 [HIGH/MED/LOW] — [second finding specific to this role's domain] — Owner: [role] — Resolution: [action]
[minimum 2 findings; each must be specific to this role's orientation]

Verdict: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
[one sentence, from this role's perspective, explaining why]
```

**The tpm stage** closes with a risk register (not a prose list) and makes the go/no-go call
explicitly — a labeled line at the top of the verdict section, not buried in paragraph prose:

```
### Risk Register

R-01 | [risk name] | Severity: HIGH | Likelihood: HIGH | Mitigation: [action]
R-02 | [risk name] | Severity: MED  | Likelihood: MED  | Mitigation: [action]
R-03 | [risk name] | Severity: LOW  | Likelihood: LOW  | Mitigation: [action]
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go
GO / NO-GO / GO WITH CONDITIONS — [cite the primary risk or finding driving this call]
```

**The exec-office stage** traces at least one named executive-level mission to this topic and
says whether the work aligns or there is a gap. "This supports our strategic priorities" does
not satisfy this — the mission must be named and the alignment or gap must be specific.

---

## V-04 — Lifecycle Emphasis + Cross-Stage Coherence

**Axes**: Lifecycle emphasis (explicit phase gates) + cross-stage coherence (named escalation protocol)
**Hypothesis**: Explicit stage-boundary gates with a required cross-stage handoff section at
each stage opening produce C-06 (cross-stage coherence) and C-09 (inter-stage blocker detection)
without relying on the model to remember earlier findings — the protocol forces a look-back at
each transition.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify roles assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each assigned role.
3. Write a one-line header before Stage 1: `TOPIC: [topic] | SCOPE: [scope or "all"]`

**STAGE EXECUTION PROTOCOL**

Each stage runs in four steps — complete all four before moving to the next stage.

**STEP 1 — STAGE OPEN**
Print the stage name and loaded role. No content yet.

**STEP 2 — STAGE BODY**
Write findings. Minimum 2 per stage.
Format: `F-[N] [HIGH/MED/LOW] [specific concern — not a category] — Owner: [role] — Resolution: [action]`

**STEP 3 — CROSS-STAGE REFERENCES**
Scan findings from all prior stages. Name any finding this stage confirms, escalates, or
contradicts. At least 2 cross-stage references must appear somewhere across the full run.
Format: `[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence]`
If no upstream finding is relevant: `No upstream reference applicable.`

**STEP 4 — STAGE VERDICT AND CLOSE**
```
VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

BLOCKER CHECK: Does any finding in this stage block a downstream stage?
  YES → BLOCKS [stage-name] — F-[N] — [reason the downstream stage cannot proceed]
  NO  → No downstream blocker identified.
```

**COMPLETE STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] — [orientation]

### Findings
F-01 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [action]
F-02 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [action]

### Cross-Stage References
[prior stage findings this stage confirms, escalates, or contradicts]
[or "No upstream reference applicable." for Stage 1]

### Verdict
VERDICT: [decision]
Rationale: [one sentence citing a finding ID]

### Blocker Check
[BLOCKS statement or "No downstream blocker identified."]
```

**TPM STAGE — ADDITIONAL REQUIREMENTS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk            | Severity | Likelihood | Mitigation   |
|------|----------------|----------|------------|--------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [action]     |
| R-02 | [specific risk] | MED      | MED        | [action]     |
| R-03 | [specific risk] | LOW      | LOW        | [action]     |
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite 1-2 finding or risk IDs]
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by name and trace its alignment
or gap to the artifact:
`F-[N] [severity] S-office mission "[mission name]" — ALIGNED / GAP — [specific reason] — Owner: [role] — Resolution: [action]`

**CROSS-STAGE ENFORCEMENT:** If fewer than 2 cross-stage references appear across the full run,
add a `## Cross-Stage Summary` section at the end naming the most important finding threads that
ran across multiple stages.

---

## V-05 — Full Integration: Table Format + Inertia Framing + Go/No-Go Ritual

**Axes**: Output format (tables) + inertia framing (structural per-stage check) + standard role
sequence + explicit go/no-go ritual
**Hypothesis**: Combining structured tables (C-03, C-07 structural satisfaction), inertia as a
named anchor per stage (C-02 enrichment via status-quo pressure), mission cascade table (C-08),
and a go/no-go ritual block (C-05 unambiguous signal) produces the highest composite score by
targeting five rubric criteria simultaneously without any single axis dominating.

---

You are running `/corps-rob`. Conduct a full corporate Review of Business (ROB) for the given
topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — single stage only
- `--stage all` — full sequence
- `--scope [group]` — limit to one division or tribe from org.yaml

**SETUP**

1. Read `org.yaml` — roles per stage.
2. Read `.craft/roles/` — persona orientation and lens for each assigned role.
3. Before Stage 1, write the INERTIA ANCHOR:

```
## Inertia Anchor

INERTIA BASELINE: [what the organization currently does instead of this topic — the process,
tool, or behavior this topic would displace. One sentence, specific.]
```

This anchor is permanent for the full run. Every stage must reference it briefly.
Reference format: `INERTIA: [threatened / not at risk this stage] — [one sentence]`

---

**STAGE FORMAT (applies to all stages):**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] | LENS: [role orientation — one phrase]

**Findings**

| ID   | Finding                                                   | Severity | Owner  | Resolution               |
|------|----------------------------------------------------------|----------|--------|--------------------------|
| F-01 | [specific concern grounded in this role's lens]          | HIGH     | [role] | [concrete action]        |
| F-02 | [second specific concern from this role's domain]        | MED      | [role] | [concrete action]        |
[minimum 2 rows; severity must vary across at least 2 rows]

**Inertia Check:** INERTIA BASELINE [threatened / not at risk this stage] — [one sentence]

**Cross-Stage References:**
[After Stage 1: cite any prior-stage finding this stage confirms, escalates, or contradicts.
 Format: [stage] F-[N] — [confirm/escalate/contradict] — [one sentence]
 First stage: write "First stage — no upstream references."]

**Verdict:**
VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence, role-specific, citing a finding ID]
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

```
**Risk Register**

| ID   | Risk                     | Severity | Likelihood | Mitigation                    | Source Stage |
|------|--------------------------|----------|------------|-------------------------------|--------------|
| R-01 | [specific risk]          | HIGH     | HIGH       | [concrete mitigation action]  | [stage]      |
| R-02 | [specific risk]          | MED      | MED        | [concrete mitigation action]  | [stage]      |
| R-03 | [specific risk]          | MED      | LOW        | [concrete mitigation action]  | [stage]      |
[minimum 3 rows; at least 1 HIGH; Source Stage traces risk to originating stage]

**Go/No-Go Ritual**

> **GO/NO-GO DECISION: GO / NO-GO / GO WITH CONDITIONS**
> Primary rationale: [cite 1-2 risk register IDs]
> Conditions (GO WITH CONDITIONS only): [what must be resolved before full GO]
> Owner: [role responsible for tracking conditions]
```

---

**ARCH-BOARD STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific interface, contract, schema, or coupling point — not a
category. "Tight coupling identified" fails. "UserService.getById contract assumes unversioned
internal response shape shared across 3 callers" passes.

---

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

```
**Mission Cascade**

| S-Office Mission      | Program          | Artifact/Topic | Alignment               |
|-----------------------|------------------|----------------|-------------------------|
| [named mission]       | [program name]   | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named — "strategic priorities" or "company goals" fails]
```

---

**CROSS-CUTTING THEMES (--stage all only, written after all stages):**

```
## Cross-Cutting Themes

| Theme                 | Stages              | Severity Pattern            | Recommended Action       |
|-----------------------|---------------------|-----------------------------|--------------------------|
| [theme name]          | [stage, stage, ...] | escalating / stable / mixed | [action]                 |
[or: "No cross-cutting themes identified — [reason]" if nothing recurs across 2+ stages]
```

A theme must be distinct from any single-stage finding. Copying one finding from one stage and
labeling it a theme does not satisfy this. The theme must name the pattern of recurrence — why
the same concern appearing in multiple stages is more serious than it was in any one stage alone.
