---
skill: quest-variate
skill_target: corps-rob
round: 5
date: 2026-03-17
rubric_version: 4
---

# Variate R5 -- corps-rob (rubric v4, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v4.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

**R4 diagnosis under v4 re-grades:** V-02 R4 is the sole top scorer at 99 under v4.
C-16 and C-17 both PASS; C-18 FAIL is the only gap.

| Variation | v3 Score | v4 Score | v4 Failures |
|-----------|----------|----------|-------------|
| V-02 R4   | 100      | **99**   | C-18 FAIL (9/10 aspirational) |
| V-03 R4   | 100      | **97**   | C-16 FAIL, C-17 N/A->FAIL, C-18 FAIL (7/10) |
| V-04 R3   | 100      | **97**   | C-16 FAIL, C-17 N/A->FAIL, C-18 FAIL (7/10) |
| V-01 R4   | 99.3     | **96.5** | C-16 FAIL, C-17 N/A->FAIL, C-18 FAIL (6.5/10) |

R5 probes a single gap: **C-18 (Explicit Lens Declaration Fill Field)**. C-18
requires a labeled `Lens:` fill field IN THE OUTPUT itself, naming the orientation
dimension by practice domain (e.g., "TPM -- schedule risk + dependency gaps"). It is
distinct from C-14, which is satisfied by role title + filter instruction in the
briefing envelope. C-18 requires the declaration to appear as a structural output field,
not as an instruction to the generator. V-02 R4 satisfies C-14 through its 4-field
briefing envelope but produces no dedicated `Lens:` output field.

The rubric note identifies V-04 R4's STAGE-OPEN FORWARD `Lens:` field as the canonical
C-18 pattern. V-04 R4 satisfies C-18 but fails C-16/C-17. The R5 challenge: can C-18
be added to V-02 R4's architecture (which passes C-16/C-17) without breaking C-14?

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| Output format (Lens: as 5th briefing envelope field) | V-01 | H-A: Briefing envelope Lens: field closes C-18; C-14 unaffected |
| Lifecycle emphasis (Lens: as stage-entry block before briefing envelope) | V-02 | H-B: Stage-entry LENS ACTIVATION block closes C-18; stage-order preserved |
| Phrasing register (Lens: in ROLE line as inline declaration) | V-03 | H-C: Inline ROLE + Lens: combined line closes C-18; smallest footprint |
| Output format + Lifecycle emphasis | V-04 | H-A + H-B: Lens: in both briefing envelope and entry block; belt-and-suspenders |
| Output format + Inertia framing | V-05 | H-A + V-03 R4 inertia evolution: full-integration ceiling candidate |

---

## V-01 -- H-A: Lens: as 5th Briefing Envelope Field (Output Format)

**Axis**: Output format -- where C-18's `Lens:` fill field appears
**Hypothesis**: C-18's pass condition is "labeled declaration field in the output naming
the orientation dimension by practice domain." V-02 R4's briefing envelope currently has
4 fields: PRIOR STAGE SUMMARY, KEY CONCERNS (lens-directed), OPEN QUESTION FORWARDED,
INERTIA STATUS. Adding `Lens:` as a 5th field -- "Lens: [role title] -- [specific
concern dimension for this topic, e.g., 'PM -- adoption readiness + handoff completeness']"
-- provides the explicit fill field C-18 requires. Stage 1 (no briefing envelope) receives
a standalone `LENS:` field in Stage Identity to ensure the declaration appears at every
stage. All V-02 R4 mechanisms preserved: 4-field briefing envelope (C-14 intact), Prior-
Stage Lens Impact + Downstream Risk Shift pair (C-16 intact), explicit anti-copy guard
(C-17 intact).

**Prediction**: C-16 PASS, C-17 PASS, C-18 PASS -> 10/10 aspirational -> composite 100.
Risk: C-18 rubric may require the Lens: field to appear BEFORE findings begin, not as
the last envelope field. If position matters, a 5th-field-last placement may earn PARTIAL.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify roles assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic -- the specific process,
tool, or behavior this topic would displace. One sentence, concrete. "Current state" fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults (VP Product for leadership, Team Leads
   for teams, Senior PM for pm, TPM Lead for tpm, Principal Architect for arch-board,
   Chief of Staff for exec-office).

---

**STAGE FORMAT -- 5 parts per stage:**

**PART 1 -- BRIEFING ENVELOPE (Stage 2+ only)**

Synthesize what prior stages surfaced, filtered through this stage's specific lens.
Distillation, not transcript.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through this stage's lens.
Lens-directed selection required -- a TPM selects for schedule and dependency risk;
a PM selects for adoption and handoff completeness; a Principal Architect selects for
interface coupling. Generic selection (most urgent finding overall) fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA STATUS: [Has any prior finding changed the displacement picture from the global anchor?
YES -- [how the picture has evolved] / NO -- anchor still holds]
Lens: [role title] -- [specific concern dimension this role brings to this topic, named by
practice domain. Example: "PM -- adoption readiness + handoff completeness to eng teams".
Example: "TPM -- schedule risk + external dependency gaps". Generic form ("this role's lens")
fails -- name the domain-specific dimension.]
```

For Stage 1: write `First stage -- no briefing envelope.` Then write the LENS declaration
in Part 2 Stage Identity (see below).

**PART 2 -- STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] -- [orientation in one phrase]

[Stage 1 only -- include LENS declaration here since Stage 1 has no briefing envelope:]
Lens: [role title] -- [specific concern dimension this role brings, named by practice domain.
Same format as briefing envelope Lens: field. Required for Stage 1; omit for Stage 2+
where Lens: appears in the briefing envelope.]

INERTIA CHECK: [threatened / not at risk this stage] -- [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
```

**PART 3 -- FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding that directly responds to the
OPEN QUESTION FORWARDED in the briefing envelope]

### Prior-Stage Lens Impact

[prior stage] F-[N]: [one sentence answering: how does this role's specific orientation
change the way that prior finding reads? What does a [role title] see in that finding
that the prior stage's reviewer could not have seen from their lens?]
[Stage 1: write "First stage -- prior-stage lens impact begins Stage 2."]
[Stage 2+: minimum 1 entry; must name this role's lens perspective, not just confirm/escalate/contradict]
```

**PART 4 -- STAGE CLOSE**

The handoff packet carries two distinct contributions:
- `PASSING TO NEXT STAGE` -- what the next stage must examine (forward charge)
- `DOWNSTREAM RISK SHIFT` -- what downstream consequence this stage's view reveals

`Prior-Stage Lens Impact` (Part 3) answers: how does my role read this prior finding
differently? `Downstream Risk Shift` answers: what failure mode, ownership gap, or
amplifying condition does this stage reveal that downstream stages must now address?
These are not the same question -- do not copy the lens impact into the risk shift.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage -- specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
DOWNSTREAM RISK SHIFT:
[prior stage] F-[N]: [confirm / escalate / contradict] -- [one sentence answering: what
downstream consequence does this stage's finding reveal about that prior finding? What
failure mode becomes visible at this stage that was invisible before?]
[Stage 1: write "First stage -- downstream risk shift begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES -- [F-ID] -- [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH/HIGH or HIGH/MED]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved before proceeding]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific -- "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A -- CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in >=2 stages.
Multi-stage recurrence from independent reviewers is stronger than any single-stage finding.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes for a full 6-stage run; each theme must cite >=2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] -> [stage] [F-ID] -- [one sentence: what does multi-stage recurrence
add to severity that the individual finding alone did not establish?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE -- [reason]".
```

**SECTION B -- ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] -- [one sentence]
BRIEFING CHAIN HEALTH: [Did each briefing envelope distill or copy prior findings? Were
Lens: declarations specific to this topic by practice domain? Any break in the chain?]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES -- or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office -- or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 5 parts
in order. Stage 2+ Lens: field appears in the briefing envelope; Stage 1 Lens: field
appears in Stage Identity. `Prior-Stage Lens Impact` (Part 3) answers how this role reads
a prior finding differently. `Downstream Risk Shift` (Part 4) answers what downstream
consequence that finding now carries. These are distinct contributions -- do not copy
one into the other. End-of-run sections (A then B) appear after all stages.

---

## V-02 -- H-B: LENS ACTIVATION Block Before Each Stage (Lifecycle Emphasis)

**Axis**: Lifecycle emphasis -- when in the stage sequence the lens declaration appears
**Hypothesis**: C-18's pass condition is a labeled declaration field in the output
naming the orientation dimension. A dedicated `LENS ACTIVATION` block before the briefing
envelope (Stage 2+) and before Stage Identity (Stage 1) ensures the lens is declared as
the FIRST structural element at each stage, before any context-loading or findings begin.
This is stronger than a 5th briefing envelope field (V-01) because it makes the lens
declaration structurally prior to the briefing envelope rather than posterior to it.
The `LENS ACTIVATION` block asks: "Before this stage begins, what is this role's specific
analytical orientation for this topic?" and requires a domain-named answer. All V-02 R4
mechanisms preserved unchanged.

**Prediction**: C-16 PASS, C-17 PASS, C-18 PASS -> 10/10 -> composite 100.
Risk: The LENS ACTIVATION block placed before the briefing envelope changes the stage
structure from 5 to 6 parts, which may not affect scoring but adds per-stage overhead.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify roles assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic -- the specific process,
tool, or behavior this topic would displace. One sentence, concrete. "Current state" fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT -- 6 parts per stage:**

**PART 0 -- LENS ACTIVATION (every stage)**

Before any context is loaded or findings are written, declare this role's analytical
orientation for this specific topic. This declaration is a fill field in the output --
it is not an instruction; it must be completed with a topic-specific named value.

```
LENS ACTIVATION:
Role: [name] | Stage: [stage-name]
Lens: [role title] -- [specific concern dimension this role brings to this topic, named
by practice domain. A TPM names a scheduling or dependency dimension. A PM names an
adoption or handoff dimension. A Principal Architect names an interface or coupling
dimension. Name the dimension, not the category. Example: "PM -- adoption velocity
across eng teams + PM-to-eng handoff completeness before sprint 0". Generic form
("this role's lens") fails -- the dimension must be topic-specific.]
```

This block must be completed before Part 1 begins. The Lens: value declared here
governs KEY CONCERNS selection in Part 1 and Prior-Stage Lens Impact targeting in Part 3.

**PART 1 -- BRIEFING ENVELOPE (Stage 2+ only)**

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through the Lens declared in
Part 0. Lens-directed selection required. Generic selection fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA STATUS: [YES -- [how picture evolved] / NO -- anchor still holds]
```

For Stage 1: write `First stage -- no briefing envelope.`

**PART 2 -- STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] -- [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] -- [one sentence: how the global
inertia anchor reads from this role's perspective.]
```

**PART 3 -- FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding that directly responds to OPEN QUESTION FORWARDED]

### Prior-Stage Lens Impact

[prior stage] F-[N]: [one sentence: how does this role's orientation (declared in Part 0)
change the reading of that prior finding? What does a [role title] see that the prior
reviewer could not?]
[Stage 1: write "First stage -- prior-stage lens impact begins Stage 2."]
[Stage 2+: minimum 1 entry; must reference the Lens declared in Part 0, not generic escalation]
```

**PART 4 -- STAGE CLOSE**

`Prior-Stage Lens Impact` (Part 3) answers: how does the declared Lens (Part 0) change
how a prior finding reads? `Downstream Risk Shift` answers: what downstream consequence
does this stage reveal that the prior stage could not have established? These ask different
questions -- do not copy the lens impact into the risk shift.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage -- specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
DOWNSTREAM RISK SHIFT:
[prior stage] F-[N]: [confirm / escalate / contradict] -- [one sentence: what downstream
consequence does this finding carry given what this stage has surfaced? What becomes
visible at this stage that was invisible before?]
[Stage 1: write "First stage -- downstream risk shift begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES -- [F-ID] -- [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH/HIGH or HIGH/MED]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved before proceeding]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific -- "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

**SECTION A -- CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each must cite >=2 F-IDs from different stages]

T-[N]: [stage] [F-ID] -> [stage] [F-ID] -- [what does multi-stage recurrence add?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE -- [reason]".
```

**SECTION B -- ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] -- [one sentence]
LENS ACTIVATION CHAIN HEALTH: [Were Lens: declarations topic-specific at every stage?
Did KEY CONCERNS selections trace to the declared Lens? Any generic declarations?]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES -- or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office -- or "None"]
```

**OUTPUT RULE:** Do not skip stages. Part 0 (LENS ACTIVATION) appears at every stage
before Parts 1-4. The Lens: value declared in Part 0 governs KEY CONCERNS selection
and Prior-Stage Lens Impact targeting -- it is not a restatement of the role title.
`Downstream Risk Shift` answers a different question than `Prior-Stage Lens Impact` --
do not copy one into the other. End-of-run sections (A then B) appear after all stages.

---

## V-03 -- H-C: Lens: as Inline ROLE Line Declaration (Phrasing Register)

**Axis**: Phrasing register -- how the lens declaration is expressed
**Hypothesis**: C-18's pass condition is a labeled declaration field naming the orientation
dimension. The smallest possible form: inline extension of the ROLE line in Stage Identity.
"ROLE: [name] -- [orientation] | Lens: [domain] -- [primary concern dimension]" requires
a named fill field at exactly the same location as the role attribution, requiring no
additional block or section. C-14 is satisfied by the 4-field briefing envelope (unchanged
from V-02 R4). C-18 is satisfied by the inline Lens: on the ROLE line. This tests whether
C-18's "labeled declaration field" is satisfied by an inline pipe-separated extension of an
existing field, or requires a standalone block.

**Prediction**: C-16 PASS, C-17 PASS, C-18 PASS or PARTIAL (risk: inline extension may
be treated as part of the ROLE field, not a dedicated declaration field). Expected score:
99.5-100 under v4.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify roles assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic -- the specific
process, tool, or behavior this topic would displace. One sentence, concrete.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT -- 5 parts per stage:**

**PART 1 -- BRIEFING ENVELOPE (Stage 2+ only)**

Synthesize what prior stages surfaced, filtered through this stage's specific lens.
Distillation, not transcript.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through this stage's lens.
Lens-directed selection required -- a TPM selects for schedule and dependency risk;
a PM selects for adoption and handoff completeness; a Principal Architect selects for
interface coupling. Generic selection fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA STATUS: [YES -- [how picture evolved] / NO -- anchor still holds]
```

For Stage 1: write `First stage -- no briefing envelope.`

**PART 2 -- STAGE IDENTITY**

The ROLE line includes an explicit Lens: declaration naming this role's specific
concern dimension for this topic. This is a fill field in the output -- complete it
with a domain-specific named value.

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] -- [orientation in one phrase] | Lens: [role title] --
[specific concern dimension for this topic by practice domain. Example: "PM -- adoption
velocity + eng handoff completeness". Example: "TPM -- schedule risk from external API
dependency + migration rollback window". Generic form fails -- name the specific dimension.]

INERTIA CHECK: [threatened / not at risk this stage] -- [one sentence: how the global
inertia anchor reads from this role's perspective.]
```

**PART 3 -- FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding directly addressing OPEN QUESTION FORWARDED]

### Prior-Stage Lens Impact

[prior stage] F-[N]: [one sentence: how does the Lens declared in ROLE line above change
the reading of that prior finding? What does this role see that the prior reviewer could not?]
[Stage 1: write "First stage -- prior-stage lens impact begins Stage 2."]
[Stage 2+: minimum 1 entry; must trace to the Lens: value in the ROLE line above]
```

**PART 4 -- STAGE CLOSE**

`Prior-Stage Lens Impact` (Part 3) re-reads a prior finding through the declared Lens.
`Downstream Risk Shift` reveals what downstream consequence this stage uncovers. These
ask different questions -- do not copy the lens impact into the risk shift.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage -- specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
DOWNSTREAM RISK SHIFT:
[prior stage] F-[N]: [confirm / escalate / contradict] -- [one sentence: what downstream
consequence becomes visible at this stage that was invisible before?]
[Stage 1: write "First stage -- downstream risk shift begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES -- [F-ID] -- [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH/HIGH or HIGH/MED]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved before proceeding]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific -- "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

**SECTION A -- CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each must cite >=2 F-IDs from different stages]

T-[N]: [stage] [F-ID] -> [stage] [F-ID] -- [what does multi-stage recurrence add?]
Fallback: if fewer than 2 genuine themes, write "THEME-SPARSE -- [reason]".
```

**SECTION B -- ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] -- [one sentence]
LENS DECLARATION HEALTH: [Were Lens: values in each ROLE line topic-specific and domain-named?
Did Prior-Stage Lens Impact entries trace to the declared Lens? Generic declarations count as gaps.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES -- or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office -- or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. The ROLE line Lens: value is a
fill field requiring a domain-specific named value -- it is not a role description.
`Prior-Stage Lens Impact` (Part 3) traces to the declared Lens. `Downstream Risk Shift`
(Part 4) asks a different question -- do not copy one into the other. End-of-run sections
(A then B) appear after all stages.

---

## V-04 -- H-A + H-B: Lens: in Both Briefing Envelope and Stage Entry (Combination)

**Axes**: Output format (V-01's 5th envelope field) + Lifecycle emphasis (V-02's
LENS ACTIVATION block before envelope)
**Hypothesis**: If either V-01 or V-02's single placement is insufficient for C-18,
the combination ensures the lens declaration appears twice: once as a LENS ACTIVATION
block at stage entry (before context-loading), and once as the 5th field in the briefing
envelope (co-located with KEY CONCERNS). The dual presence provides structural redundancy
for C-18 scoring. It also tests whether dual placement creates a new qualitative dimension
(lens declared before context load, then confirmed after context distillation) that may
surface as a C-19 candidate. All V-02 R4 mechanisms preserved.

**Prediction**: C-16 PASS, C-17 PASS, C-18 PASS (belt-and-suspenders ensures C-18
coverage regardless of which placement the rubric scores). Expected composite: 100.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify roles assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic -- the specific
process, tool, or behavior this topic would displace. One sentence, concrete.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT:**

Each stage opens with a LENS ACTIVATION block, then the BRIEFING ENVELOPE (Stage 2+),
then STAGE IDENTITY, then FINDINGS, then STAGE CLOSE.

**LENS ACTIVATION -- every stage, before everything else**

Before any context is loaded, declare this role's analytical orientation for this topic.

```
LENS ACTIVATION:
Role: [name] | Stage: [stage-name]
Lens: [role title] -- [specific concern dimension for this topic, named by practice domain.
Name the dimension, not the category. Generic form fails.]
```

**BRIEFING ENVELOPE (Stage 2+ only)**

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through the declared Lens above.
Lens-directed selection required. Generic selection fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA STATUS: [YES -- [how picture evolved] / NO -- anchor still holds]
Lens: [confirm or refine the LENS ACTIVATION declaration after seeing context -- same format:
"[role title] -- [concern dimension]". If context does not change the lens, restate it.
If context reveals a more specific dimension, refine it here.]
```

For Stage 1: write `First stage -- no briefing envelope.`

**STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] -- [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] -- [one sentence]
```

**FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern] -- Owner: [role] -- Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern] -- Owner: [role] -- Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding directly addressing OPEN QUESTION FORWARDED]

### Prior-Stage Lens Impact

[prior stage] F-[N]: [how does the declared Lens change the reading of that prior finding?]
[Stage 1: write "First stage -- prior-stage lens impact begins Stage 2."]
[Stage 2+: minimum 1 entry; must trace to the Lens declared in LENS ACTIVATION]
```

**STAGE CLOSE**

`Prior-Stage Lens Impact` re-reads a prior finding through the declared Lens. `Downstream
Risk Shift` reveals downstream consequence. Different questions -- do not copy one into the other.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

### Handoff Packet

PASSING TO NEXT STAGE: [most important open concern -- specific]
DOWNSTREAM RISK SHIFT:
[prior stage] F-[N]: [confirm / escalate / contradict] -- [downstream consequence visible here]
[Stage 1: "First stage -- downstream risk shift begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 across a 6-stage run]
BLOCKER: YES -- [F-ID] -- [what is blocked, which downstream stage] / NO
```

---

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH/HIGH or HIGH/MED]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; specific mission name required]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

**SECTION A -- CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each cites >=2 F-IDs from different stages]

T-[N]: [stage] [F-ID] -> [stage] [F-ID] -- [what does recurrence add to severity?]
Fallback: if fewer than 2 genuine themes, write "THEME-SPARSE -- [reason]".
```

**SECTION B -- ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] -- [one sentence]
LENS DECLARATION CHAIN: [Did LENS ACTIVATION declarations match briefing envelope Lens:
confirmations at each stage? Were refinements substantive or rote re-statements?]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES -- or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office -- or "None"]
```

**OUTPUT RULE:** LENS ACTIVATION appears before every stage. Stage 2+ briefing envelope
contains a Lens: field that confirms or refines the LENS ACTIVATION declaration. Do not
copy lens impact into downstream risk shift. End-of-run sections (A then B) after all stages.

---

## V-05 -- H-A + Inertia Evolution: Full-Integration Ceiling Candidate (Combination)

**Axes**: Output format (V-01's 5th envelope Lens: field) + Inertia framing (V-03 R4's
per-stage evolution tracking + INERTIA TRAJECTORY section)
**Hypothesis**: V-02 R4 passes C-16/C-17 and V-03 R4 adds qualitative inertia evolution
depth. Combining these with an explicit Lens: field (C-18 target) produces the ceiling
candidate under v4: all 10 aspirational criteria PASS. The inertia evolution thread (per-
stage INERTIA EVOLUTION field in briefing envelope + end-of-run INERTIA TRAJECTORY section)
does not interfere with C-14/C-16/C-17/C-18 -- it extends the INERTIA STATUS field rather
than replacing any required element. The Lens: as 5th briefing envelope field coexists with
the INERTIA EVOLUTION field (now a 5th and 6th field pair). Stage 1 receives a standalone
LENS: declaration in Stage Identity.

**Prediction**: C-16 PASS, C-17 PASS, C-18 PASS -> 10/10 aspirational -> composite 100.
Additional signal: does the inertia evolution thread surface a new qualitative dimension
(hardened vs softened posture arc across stages) that warrants a C-19 candidate in v5?

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership -> teams -> pm -> tpm -> arch-board -> exec-office

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify roles assigned to each stage.
2. Read `.craft/roles/` -- load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic -- the specific
process, tool, or behavior this topic would displace. One sentence, concrete.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT -- 5 parts per stage:**

**PART 1 -- BRIEFING ENVELOPE (Stage 2+ only)**

Synthesize what prior stages surfaced, filtered through this stage's specific lens.
Distillation, not transcript. The briefing envelope has 6 fields for Stage 2+.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through this stage's lens.
Lens-directed selection required. Generic selection fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA EVOLUTION: [How has the displacement posture shifted since Stage 1, or since the
immediately prior stage? Name the specific prior finding that changed the picture.
Format: "[Stage name] [F-ID] [hardened / softened] the displacement posture by [one clause]."
Or: "Anchor unchanged -- no prior finding has modified the displacement picture."]
INERTIA STATUS: [Has the displacement picture changed from the global anchor?
YES -- [summary of evolution] / NO -- anchor still holds]
Lens: [role title] -- [specific concern dimension for this topic, named by practice domain.
Example: "TPM -- schedule risk from external API dependency + migration rollback window".
Generic form ("this role's lens") fails -- name the dimension specifically.]
```

For Stage 1: write `First stage -- no briefing envelope.` Then write the LENS declaration
in Part 2 Stage Identity.

**PART 2 -- STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] -- [orientation in one phrase]

[Stage 1 only:]
Lens: [role title] -- [specific concern dimension for this topic by practice domain.
Same format as briefing envelope Lens: field. Required for Stage 1 only.]

INERTIA CHECK: [threatened / not at risk this stage] -- [one sentence]
INERTIA STAGE READING: [Given the current inertia evolution state from Part 1 above,
how does this role interpret the displacement risk as it stands at this stage? One sentence.
Stage 1: "Baseline -- displacement posture not yet modified by any prior finding."]
```

**PART 3 -- FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] -- Owner: [role] -- Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding directly addressing OPEN QUESTION FORWARDED]

### Prior-Stage Lens Impact

[prior stage] F-[N]: [how does the declared Lens (Part 1 or Part 2) change the reading of
that prior finding? What does this role see that the prior reviewer could not?]
[Stage 1: write "First stage -- prior-stage lens impact begins Stage 2."]
[Stage 2+: minimum 1 entry; must trace to the declared Lens, not just confirm/escalate/contradict]
```

**PART 4 -- STAGE CLOSE**

`Prior-Stage Lens Impact` (Part 3) re-reads a prior finding through the declared Lens.
`Downstream Risk Shift` reveals downstream consequence. Do not copy one into the other.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

### Handoff Packet

PASSING TO NEXT STAGE: [most important open concern -- specific.
Final stage: write "PASSING TO ROB SPONSOR:"]
DOWNSTREAM RISK SHIFT:
[prior stage] F-[N]: [confirm / escalate / contradict] -- [downstream consequence visible here]
[Stage 1: "First stage -- downstream risk shift begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 across a 6-stage run]
BLOCKER: YES -- [F-ID] -- [what is blocked, which downstream stage] / NO
```

---

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH/HIGH or HIGH/MED]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE -- ADDITIONAL REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; specific mission name required]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A -- CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each cites >=2 F-IDs from different stages]

T-[N]: [stage] [F-ID] -> [stage] [F-ID] -- [what does recurrence add to severity?]
Fallback: "THEME-SPARSE -- [reason]" if fewer than 2 genuine themes.
```

**SECTION B -- INERTIA TRAJECTORY**

```
## Inertia Trajectory

Synthesize the INERTIA EVOLUTION fields from all briefing envelopes. Map the displacement
posture across all six stages -- compile from the envelopes, do not generate new analysis.

| Stage       | Posture Change                                                |
|-------------|---------------------------------------------------------------|
| leadership  | [hardened / softened / unchanged] -- [one clause or "baseline"] |
| teams       | [hardened / softened / unchanged] -- [one clause]              |
| pm          | [hardened / softened / unchanged] -- [one clause]              |
| tpm         | [hardened / softened / unchanged] -- [one clause]              |
| arch-board  | [hardened / softened / unchanged] -- [one clause]              |
| exec-office | [hardened / softened / unchanged] -- [one clause]              |

NET DISPLACEMENT POSTURE: [hardened / softened / unchanged from Anchor]
KEY TURNING POINT: [which stage finding most shifted the posture, and what it changed]
```

**SECTION C -- ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] -- [one sentence]
LENS DECLARATION HEALTH: [Were Lens: field values topic-specific and domain-named at every
stage? Did Prior-Stage Lens Impact entries trace to the declared Lens? Generic forms count
as gaps.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES -- or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office -- or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Stage 2+ briefing envelope has
6 fields including INERTIA EVOLUTION and Lens:. Stage 1 Lens: field appears in Stage
Identity. INERTIA TRAJECTORY (Section B) compiles from briefing envelope INERTIA EVOLUTION
fields -- no new analysis. `Prior-Stage Lens Impact` answers how the declared Lens changes
a prior finding's reading. `Downstream Risk Shift` answers what downstream consequence
this stage reveals. Do not copy one into the other. End-of-run sections (A then B then C)
appear after all stages.
