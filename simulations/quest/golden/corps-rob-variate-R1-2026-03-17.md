---
skill: quest-variate
skill_target: corps-rob
round: 1
date: 2026-03-17
rubric_version: 1
---

# Variate R1 — corps-rob (rubric v1, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v1.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (bottom-up: operational reviews bubble up to leadership) | V-01 |
| Output format (compact single-line findings — minimum-footprint style) | V-02 |
| Phrasing register (workshop facilitation — second-person active, you-are-the-reviewer) | V-03 |
| Inertia framing + lifecycle emphasis (inertia anchor + explicit handoff packets) | V-04 |
| Output format (per-stage scorecard table) + cross-stage coherence (escalation ledger) | V-05 |

---

## V-01 — Role Sequence: Bottom-Up

**Axis**: Role sequence
**Hypothesis**: Running operational stages (teams → pm → tpm) before leadership inverts the usual
information flow. Leadership's exec briefing is informed by what the teams, PM, and TPM already
surfaced rather than framing it first. This should produce a leadership stage that confirms or
contradicts specific upstream findings (C-08 cross-stage coherence), and an exec-office stage that
sees a richer, already-stress-tested artifact. The risk is that leadership feels reactive rather
than strategic — a hypothesis the scoring will test.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGE ORDER (BOTTOM-UP):**
teams → pm → tpm → arch-board → leadership → exec-office

Operational functions review first. Leadership synthesizes last.

If `--stage [name]` is given, run only that stage (ignore sequence).
If `--scope [group]` is given, filter org.yaml roles to that division or tribe only.
If `--stage all` is given, run all six stages in the bottom-up order above.

**SETUP**

1. Read `org.yaml` — identify the role assigned to each stage.
2. Read `.roles/` — load orientation and lens for each assigned role.
3. Fallback if files are absent:
   - teams = Team Leads, pm = Senior PM, tpm = TPM Lead,
     arch-board = Principal Architect, leadership = VP Product,
     exec-office = Chief of Staff

**FOR EACH STAGE, PRODUCE:**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [their orientation in one phrase]

### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[add more if needed; minimum 2 per stage]

### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence, role-specific, citing at least one finding ID]
```

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict, add:

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least one HIGH severity]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one finding ID or risk ID]
```

**LEADERSHIP STAGE — SEQUENCING NOTE:**

Because `leadership` runs after `teams`, `pm`, and `tpm`, the exec briefing has a full picture
of what the organization already surfaced. At least one leadership finding must reference an
upstream stage finding by ID and state whether leadership confirms, escalates, or resolves it.
Do not simply restate the finding — state what leadership's view adds.

**EXEC-OFFICE STAGE — ADDITIONAL REQUIREMENT:**

At least one finding must name a specific S-office mission by its actual title and state
ALIGNED / PARTIAL / GAP with a concrete reason. A Mission Cascade table satisfies this:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage is its own labeled section.

---

## V-02 — Output Format: Compact Single-Line

**Axis**: Output format
**Hypothesis**: A minimum-footprint format — single-line findings with severity inline, no prose
preamble — tests whether the rubric's structural requirements (C-01, C-03, C-04) can be satisfied
at high density. The expected failure mode: findings become so compressed that role-loaded
specificity (C-02) degrades to category labels. The expected benefit: every structural element is
visible and machine-verifiable, eliminating formatting failures.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

Read `org.yaml`. Read `.roles/` for each stage's assigned persona.
Fallback if not found: assign by stage name (PM for pm stage, TPM for tpm stage, etc.)

**COMPACT FORMAT — APPLIES TO ALL STAGES:**

Each stage is exactly this structure. No prose preamble. No introductory paragraphs.

```
## Stage: [stage-name] | ROLE: [name] — [orientation]

F-01 [HIGH/MED/LOW] [specific concern] | Owner: [role] | Resolution: [action]
F-02 [HIGH/MED/LOW] [specific concern] | Owner: [role] | Resolution: [action]
[additional findings if needed; minimum 2]

VERDICT: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED] — [one phrase rationale citing a finding ID]
```

Severity labels must be HIGH, MED, or LOW exactly. No substitutions.
Owner must be a role name, not a generic label like "team" or "stakeholders".
Resolution must be a concrete action, not "review required" or "needs attention".
Finding concern must name the specific artifact or behavior under review — not just the problem domain.

**TPM STAGE — COMPACT ADDITIONS:**

After findings, before verdict:

```
RISK REGISTER:
R-01 [HIGH/HIGH] [specific risk] | Mitigation: [action]
R-02 [MED/MED]  [specific risk] | Mitigation: [action]
R-03 [MED/LOW]  [specific risk] | Mitigation: [action]
[format: [Severity/Likelihood]; minimum 3; at least 1 HIGH/HIGH or HIGH/MED]

GO/NO-GO: GO / NO-GO / GO WITH CONDITIONS — [cite R-ID or F-ID]
```

The GO/NO-GO line must appear as a labeled standalone line, not embedded in prose.

**EXEC-OFFICE STAGE — COMPACT ADDITION:**

After findings, before verdict:

```
MISSION CASCADE:
[S-office mission name] → [program] → [topic] | ALIGNED / PARTIAL / GAP — [one sentence reason]
[minimum 1 entry; mission name must be specific]
```

**CROSS-STAGE COHERENCE (--stage all only):**

When running multiple stages, at least 2 findings across the full run must reference a prior
stage by name and finding ID. Inline reference format:
`[Confirms/Escalates/Contradicts teams F-02: [one sentence]]`

Place the reference at the end of the finding line that references it.

**OUTPUT RULE:** Strict compact format. No stage introductions. No stage conclusions beyond
VERDICT. Each stage section contains: header line, findings, any stage-specific extras, verdict.

---

## V-03 — Phrasing Register: Workshop Facilitation

**Axis**: Phrasing register
**Hypothesis**: Framing the skill as a workshop facilitation script — second-person active,
present-tense, you-are-running-this-review — activates the persona's role more viscerally than
procedural ENFORCE instructions. The model writes the review from inside the moment rather than
executing a template. Hypothesis: richer role-loaded findings (C-02), but possible format
compliance risk (C-03) if the persona voice crowds out structural markers.

---

You are running `/corps-rob`. You are the facilitator. Walk each governance stage as it would
actually happen in the room — or the async equivalent — for a large software organization.

**What you're doing:** You're running a corporate Review of Business. Each function gets its
turn to look at the topic through their own lens before anything ships or gets funded. Your job
is to run each stage faithfully — not as a checklist, but as a real review. Each reviewer has
a documented orientation. They notice different things. Let them.

**Stages to run** (default: all, in this order):
leadership → teams → pm → tpm → arch-board → exec-office

- `--stage [name]` runs one stage
- `--stage all` runs all six
- `--scope [group]` limits roles to one division or tribe from org.yaml

**Loading the reviewers:**
Before you start, pull each stage's assigned persona from `.roles/` via `org.yaml`.
Each persona has an orientation — a documented lens that shapes which problems they notice.
A VP reads for strategic fit and funding exposure. A TPM reads for schedule and unresolved
dependencies. A Principal Architect reads for interface coupling and long-term maintenance
debt. A Senior PM reads for adoption risk and handoff completeness. Let the orientation drive
what each reviewer sees — not a generic list any reviewer could have written.

**Running each stage:**
For each stage, write the review as if the assigned reviewer actually ran it. They are
identified at the top. Their findings are specific to what they would notice — the exact
concerns their role, orientation, and background surface. Each finding carries a severity and
names the person who owns it and what they need to do next. The stage closes with a verdict.

```
## Stage: [stage-name]

ROLE: [name from .roles/ or org.yaml] — [their orientation in one phrase]

Findings:
F-01 [HIGH/MED/LOW] — [what this reviewer found, in their voice and from their lens] — Owner: [role] — Resolution: [what needs to happen]
F-02 [HIGH/MED/LOW] — [second finding specific to this reviewer's domain and orientation] — Owner: [role] — Resolution: [concrete action]
[minimum 2 findings; each must be traceable to this reviewer's specific orientation]

Verdict: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
[One sentence, from this reviewer's perspective, explaining why this is their call.]
```

**Running the tpm stage:**
The TPM's job is risk management and go/no-go. They produce a risk register — a structured
document, not a list of concerns buried in prose. And they make the call explicitly: GO,
NO-GO, or GO WITH CONDITIONS. The call is labeled and top-level. It is not hidden in a
paragraph. The TPM cites a specific finding or risk when they make it.

```
### Risk Register

R-01 | [risk name] | Severity: HIGH | Likelihood: HIGH | Mitigation: [action]
R-02 | [risk name] | Severity: MED  | Likelihood: MED  | Mitigation: [action]
R-03 | [risk name] | Severity: LOW  | Likelihood: LOW  | Mitigation: [action]
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go
GO / NO-GO / GO WITH CONDITIONS — [cite the primary finding or risk driving this call]
```

**Running the exec-office stage:**
The Chief of Staff (or equivalent) connects this topic to what the S-office actually cares
about. They do not say "this supports our strategy." They name the mission — the actual title
of the executive initiative or S-office mission — and say explicitly whether this work aligns,
partially aligns, or gaps against it. They give a specific reason.

If you have a Mission Cascade table available, use it. If not, name the mission inline in
a finding:
`F-[N] [severity] — S-office mission "[actual mission title]" — ALIGNED / PARTIAL / GAP — [specific reason] — Owner: [role] — Resolution: [action]`

**When running multiple stages:**
Later reviewers may have heard about what earlier reviewers found. When a later reviewer's
finding confirms, escalates, or contradicts something from an earlier stage, say so. The
pattern of a concern appearing in multiple stages is more serious than it was in any one
stage alone.

---

## V-04 — Inertia Framing + Lifecycle Emphasis

**Axes**: Inertia framing (status-quo anchor + per-stage inertia check) + lifecycle emphasis
(explicit stage-open and stage-close handoff packets between stages)
**Hypothesis**: Combining an inertia anchor (what this topic displaces or competes with) with
explicit stage-boundary handoff packets produces two structural benefits simultaneously: (1)
each stage's findings are grounded in the status-quo pressure their role feels (C-02 enrichment),
and (2) the handoff packet at stage close forces a look-back that generates C-08 cross-stage
references without relying on the model to recall prior findings unprompted. The handoff packet
also naturally surfaces inter-stage blockers (C-09).

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify roles assigned to each stage.
2. Read `.roles/` — load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic — the existing process,
tool, or behavior this topic would displace or require changing. One sentence, specific.
"Current state" or "existing approach" alone does not satisfy this — name what it is.]

DISPLACEMENT COST: [Who bears the switching cost and what it is — team, tooling, behavior,
or budget. One sentence.]
```

This anchor is permanent for the run. Every stage references it in its INERTIA CHECK.

---

**STAGE EXECUTION — 4 STEPS PER STAGE:**

Complete all four steps before moving to the next stage.

**STEP 1 — STAGE OPEN**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the inertia
baseline looks from this role's perspective. What do they stand to lose or gain if the
status quo changes?]
```

**STEP 2 — FINDINGS**

Write findings grounded in both the loaded persona's orientation and the inertia context.

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
[minimum 2; findings must reflect the loaded persona's specific lens, not generic concerns]
```

**STEP 3 — CROSS-STAGE REFERENCES (Stage 2 onward)**

Scan findings from all prior stages. Identify any finding this stage confirms, escalates,
or contradicts. Write each as:

```
### Cross-Stage References

[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence explaining what
this stage's view adds or changes]
```

For Stage 1: write `First stage — no upstream references.`
At least 2 cross-stage references must appear somewhere across the full run.

**STEP 4 — STAGE CLOSE**

```
### Verdict
VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

### Handoff Packet
PASSING TO NEXT STAGE: [key concern or open question the next stage must address]
BLOCKER: YES — [F-ID] blocks [downstream stage] because [reason] / NO — no downstream blocker
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before cross-stage references:

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After findings, before cross-stage references:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named specifically — "strategic goals" fails]
```

**END-OF-RUN SUMMARY (--stage all only):**

After all stages, write:

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES entries, or "None"]
OPEN HANDOFFS: [list any PASSING TO NEXT STAGE items not resolved by the final stage]
```

---

## V-05 — Per-Stage Scorecard + Escalation Ledger

**Axes**: Output format (per-stage scorecard table) + cross-stage coherence (explicit escalation
ledger at document level) + standard role sequence
**Hypothesis**: Replacing the verdict line with a per-stage scorecard table (dimensions: coverage,
depth, role-specificity, severity calibration) forces the model to evaluate the stage's own output
before closing it. The escalation ledger at document end collects all cross-stage references in
one place, making C-08 and C-10 structurally impossible to miss. Risk: the scorecard may feel
self-referential rather than substantive, degrading the quality of individual findings.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify roles assigned to each stage.
2. Read `.roles/` — load orientation and lens for each role.
3. Fallback if files are absent: assign roles by stage name.

---

**STAGE FORMAT (applies to all stages):**

```
## Stage: [stage-name]

ROLE: [name from .roles/] | LENS: [orientation — one phrase]

### Findings

F-01 [HIGH/MED/LOW] [specific concern grounded in this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern grounded in this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; each concern must name the specific artifact or behavior, not just the domain]

### Stage Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED

### Stage Scorecard

| Dimension         | Rating (1-3) | Note                                              |
|-------------------|--------------|---------------------------------------------------|
| Role specificity  | [1-3]        | [Are findings specific to this role's lens?]      |
| Finding depth     | [1-3]        | [Do findings name specific artifacts/behaviors?]  |
| Severity spread   | [1-3]        | [Does severity vary meaningfully across findings?]|
| Resolution quality| [1-3]        | [Are resolutions concrete and owner-assigned?]    |

[Rating scale: 1 = does not meet standard, 2 = meets standard, 3 = exceeds standard]
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After findings, before stage verdict:

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
```

---

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After findings, before stage verdict:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific]
```

---

**ESCALATION LEDGER (--stage all only — written after all stages):**

```
## Escalation Ledger

This section collects all cross-stage finding threads. A thread exists when the same concern
surfaces in 2 or more stages, whether confirmed, escalated, or contradicted.

| Thread ID | Concern (short)         | Stages Involved      | Pattern                     | Action Required          |
|-----------|------------------------|----------------------|-----------------------------|--------------------------|
| T-01      | [concern name]         | [stage, stage, ...]  | escalating / stable / mixed | [concrete action]        |
[minimum 2 threads for a full run; if fewer than 2 threads exist, write "No threads identified
across [N] stages — [explanation of why concerns did not recur"]

For each thread, cross-reference the specific finding IDs:
T-01: leadership F-02 → teams F-01 → tpm R-02 (escalating — severity increased at each stage)
```

A thread must reflect a genuine pattern of recurrence across stages, not a finding copied from
one stage. The ledger entry must explain why multi-stage recurrence increases severity beyond
the individual stage instance.

**ARCH-BOARD STAGE — SPECIFICITY REQUIREMENT:**

At least one finding must name a specific interface, contract, schema, or coupling point.
"Tight coupling" alone fails. "PaymentService.charge() is called synchronously from 4 callers
with no circuit breaker, creating a cascading failure surface" passes.

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Escalation Ledger appears after all
stage sections, not inside any stage.
