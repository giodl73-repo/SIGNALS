---
skill: quest-variate
skill_target: corps-rob
round: 4
date: 2026-03-17
rubric_version: 3
---

# Variate R4 — corps-rob (rubric v3, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v3.
Single-axis variations V-01 through V-03, then combinations V-04 through V-05.

**R3 diagnosis under v3 re-grades:** V-04 R3 is the sole 100-scorer (7/7 aspirational).
Every other R3 variation drops when v3 adds C-14 and C-15:

| Variation | v2 Score | v3 Score | v3 Failures |
|-----------|----------|----------|-------------|
| V-04 R3   | 100      | **100**  | none        |
| V-03 R3   | 98       | **97.1** | C-10 FAIL, C-15 FAIL (5/7) |
| V-05 R3   | 100      | **97.1** | C-14 FAIL, C-15 FAIL (5/7) |
| V-01 R3   | 99       | **96.4** | C-14 FAIL, C-15 FAIL, C-11 PARTIAL (4.5/7) |
| V-02 R3   | 97       | **94.7** | C-08 PARTIAL, C-10 FAIL, C-14 FAIL, C-15 FAIL (4/7) |

The new ceiling pattern (V-04 R3) has four mechanisms: full briefing envelope (C-14) +
explicit anti-copy instruction between the two backward-synthesis surfaces (C-15) +
Cross-Cutting Themes section (C-10) + bi-directional closing packet (C-11). R4 probes
three questions:

1. **C-14 form** — Does C-14 require the full 4-field briefing envelope, or does a
   compressed 3-field Stage-Open Context (one-line role-filtered forwarded concern)
   satisfy "role-loading operates on forwarded context at stage open"?

2. **C-15 mechanism** — Does C-15 require an explicit negative instruction ("must add
   substance not already stated"), or can structurally distinct field names (different
   questions per surface) serve as an implicit anti-redundancy constraint?

3. **Inertia thread depth** — Can explicit inertia evolution tracking across stages
   (hardened/softened trajectory per stage, synthesized at end-of-run) surface a new
   qualitative dimension that becomes a C-16 candidate?

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| C-14 form: compressed Stage-Open Context (3-field) vs. full briefing envelope (4-field) | V-01 |
| C-15 mechanism: structural field separation (different questions) vs. explicit anti-copy instruction | V-02 |
| Inertia thread depth: per-stage evolution tracking + end-of-run trajectory vs. anchor-only | V-03 |
| Axes 1+2 on V-05 R3 base: minimal C-14 + structural C-15 + 3-section design | V-04 |
| Axes 3+4 on V-04 R3 base: inertia evolution tracking + pre-printed briefing envelope | V-05 |

---

## V-01 — Compressed Stage-Open Context (C-14 Form, Single-Axis)

**Axis**: C-14 form (lifecycle emphasis at stage open)
**Hypothesis**: C-14's pass condition is "role-loading operates on forwarded context at
stage open before any findings are written." A compressed 3-field Stage-Open Context block
(CONCERN: prior F-ID through this role's lens | FORWARDED: verbatim question | INERTIA:
one clause) satisfies this mechanism without the overhead of the full 4-field briefing
envelope (PRIOR STAGE SUMMARY + KEY CONCERNS multi-row table + OPEN QUESTION FORWARDED +
INERTIA STATUS). V-01 replaces Part 1 on V-04 R3's proven base with the compressed form
and preserves all other mechanisms: global anchor, inertia check, cross-stage references
in findings, bi-directional handoff packet with explicit anti-copy constraint, cross-cutting
themes section. Expected benefit: C-14 PASS with a smaller per-stage footprint. Expected
risk: the rubric may require the full KEY CONCERNS multi-row table for C-14 (the specific
lens-directed F-ID selection that V-04 R3's briefing envelope enforces). If so, V-01 earns
C-14 PARTIAL rather than PASS, and the per-stage surface reduction comes at the cost of
C-08 strength (V-02 R3 shows that removing the full briefing envelope degrades C-08 to
PARTIAL even when other coherence mechanisms remain).

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

INERTIA: [What the organization currently does instead of this topic — the specific process,
tool, or behavior this topic would displace. One sentence, concrete. "Current state" fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults (VP Product for leadership, Team Leads
   for teams, Senior PM for pm, TPM Lead for tpm, Principal Architect for arch-board,
   Chief of Staff for exec-office).

---

**STAGE FORMAT — 4 parts per stage:**

**PART 1 — STAGE-OPEN CONTEXT (Stage 2+ only)**

Before writing any findings, load the forwarded question through this role's specific lens.
This step happens at stage open, before findings begin.

```
### Stage-Open Context

ROLE-FILTERED FORWARD: [prior stage name] → [this role's title]:
CONCERN: [F-ID from prior stage most relevant to this role's orientation] — [one-phrase summary]
FORWARDED: [verbatim text from prior stage Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA: [unchanged / evolved — one clause only]

Lens filter rule: select the prior finding most relevant to this role's specific
orientation before writing any findings below. A TPM selects for schedule and dependency
risk. A PM selects for adoption readiness and handoff completeness. A Principal Architect
selects for interface coupling and maintenance debt. Selecting the most urgent finding
overall (without lens filtering) fails this criterion.

[Stage 1: write "First stage — no forwarded context."]
```

**PART 2 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
```

**PART 3 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding that directly addresses the
FORWARDED question from Stage-Open Context above]

### Cross-Stage References

[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: how this
role's lens reads the significance of that prior finding]
[Stage 1: write "First stage — no cross-stage references."]
[Stage 2+: minimum 1 entry; must cite a specific F-ID from a prior stage]
```

**PART 4 — STAGE CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
CROSS-STAGE SYNTHESIS:
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what does this
stage's view add to the downstream significance of that prior finding?
Must add substance not already stated in the Cross-Stage References section above.]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

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

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in >=2 stages.
Multi-stage recurrence from independent reviewers is stronger than any single-stage finding:
two lenses reached the same conclusion without coordination. Document the convergence and
explain what it adds to severity that the individual finding alone did not.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes for a full 6-stage run; each theme must cite >=2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] -> [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add to severity that the individual finding alone did not establish?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE — [reason]".
```

**SECTION B — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
STAGE-OPEN CHAIN HEALTH: [Did each Stage-Open Context correctly filter prior findings through
the incoming role's lens? Did the lens-selected concern differ by role from stage to stage,
or was the same concern selected regardless of orientation? One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 4 parts
in order. Stage-Open Context (Part 1) for Stage 2+ precedes Stage Identity (Part 2) —
role-loading on forwarded context happens before findings begin. CROSS-STAGE SYNTHESIS in
the Handoff Packet must add downstream significance not already stated in the Cross-Stage
References section in the same stage. End-of-run sections (A then B) appear after all stages.

---

## V-02 — Structural Field Separation (C-15 Mechanism, Single-Axis)

**Axis**: C-15 mechanism (output format of the anti-redundancy constraint)
**Hypothesis**: C-15's pass condition requires that when both Cross-Stage References (findings
body) and CROSS-STAGE SYNTHESIS (handoff packet) are present, the two surfaces do not collapse
into copies. V-04 R3 satisfies this with an explicit negative instruction: "Must add substance
not already stated in the Cross-Stage References section above." V-02 tests whether replacing
that instruction with structurally distinct field names — asking different questions by design
— makes copy behavior impossible without requiring a negative guard. The findings section uses
`### Prior-Stage Lens Impact` (question: how does this role's specific orientation change
the reading of a prior finding?) and the handoff packet uses `DOWNSTREAM RISK SHIFT:` (question:
what downstream consequence does this stage's view reveal that the lens impact could not have
established?). Different questions produce different answers structurally. Expected benefit:
C-15 PASS via structural field separation — copy behavior cannot satisfy both questions
simultaneously. Expected risk: the rubric requires an "explicit guard" — two differently
named fields may be treated as implicit rather than explicit, earning C-15 PARTIAL rather
than PASS even if the structural separation succeeds in preventing copy output.

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

INERTIA: [What the organization currently does instead of this topic — the specific process,
tool, or behavior this topic would displace. One sentence, concrete. "Current state" fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT — 5 parts per stage:**

**PART 1 — BRIEFING ENVELOPE (Stage 2+ only)**

Synthesize what prior stages surfaced, filtered through this stage's specific lens.
Distillation, not transcript.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through this stage's lens.
Lens-directed selection required — a TPM selects for schedule and dependency risk;
a PM selects for adoption and handoff completeness; a Principal Architect selects for
interface coupling. Generic selection (most urgent finding overall) fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA STATUS: [Has any prior finding changed the displacement picture from the global anchor?
YES — [how the picture has evolved] / NO — anchor still holds]
```

For Stage 1: write `First stage — no briefing envelope.`

**PART 2 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
```

**PART 3 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding that directly responds to the
OPEN QUESTION FORWARDED in the briefing envelope]

### Prior-Stage Lens Impact

[prior stage] F-[N]: [one sentence answering: how does this role's specific orientation
change the way that prior finding reads? What does a [role title] see in that finding
that the prior stage's reviewer could not have seen from their lens?]
[Stage 1: write "First stage — prior-stage lens impact begins Stage 2."]
[Stage 2+: minimum 1 entry; must name this role's lens perspective, not just confirm/escalate/contradict]
```

**PART 4 — STAGE CLOSE**

The handoff packet carries two distinct contributions:
- `PASSING TO NEXT STAGE` — what the next stage must examine (forward charge)
- `DOWNSTREAM RISK SHIFT` — what downstream consequence this stage's view reveals (backward significance)

These ask different questions. `Prior-Stage Lens Impact` (Part 3) answers: how does my
role read this prior finding differently? `Downstream Risk Shift` answers: what failure
mode, ownership gap, or amplifying condition does this stage reveal that downstream stages
must now address? These are not the same question — do not copy the lens impact into the
risk shift.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
DOWNSTREAM RISK SHIFT:
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence answering: what
downstream consequence does this stage's finding reveal about that prior finding? What
failure mode becomes visible at this stage that was invisible before? Who owns the problem
differently now, given what this stage has surfaced?]
[Stage 1: write "First stage — downstream risk shift begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

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

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in >=2 stages.
Multi-stage recurrence from independent reviewers is stronger than any single-stage finding:
two lenses reached the same conclusion without coordination. Document the convergence and
explain what it adds to severity that the individual finding alone did not.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each must cite >=2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] -> [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add to severity that the individual finding alone did not establish?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE — [reason]".
```

**SECTION B — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BRIEFING CHAIN HEALTH: [Did each briefing envelope distill or copy prior findings? Were
KEY CONCERNS selections lens-directed or generic? Any break in the chain? One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 5 parts
in order. `Prior-Stage Lens Impact` (Part 3) answers "how does my role read this prior
finding differently?" — it is a re-reading through a new lens. `Downstream Risk Shift`
(Part 4 packet) answers "what downstream consequence does my stage's view reveal?" — it
is a forward-looking consequence statement. These are distinct contributions. End-of-run
sections (A then B) appear after all stages.

---

## V-03 — Inertia Escalation Track (C-16 Candidate, Single-Axis)

**Axis**: Inertia thread depth (lifecycle emphasis — how extensively the displacement
picture is tracked across stages)
**Hypothesis**: V-04 R3's inertia mechanism is a global anchor (set before Stage 1) +
per-stage INERTIA CHECK (one sentence at stage open). This captures whether inertia is
threatened but does not track how the displacement posture evolves across stages. V-03
adds an explicit evolution thread: the briefing envelope gains `INERTIA EVOLUTION:` (how
the displacement picture has shifted since Stage 1, tied to a specific F-ID), the per-stage
identity gains `INERTIA STAGE READING:` (how this role interprets the current posture given
the evolution state), and a new end-of-run `## Inertia Trajectory` section maps the full
posture arc across all 6 stages. Expected benefit: the evolution thread surfaces a qualitative
dimension — which stage findings harden or soften the displacement picture — that the anchor
alone cannot capture, and makes a strong case for C-16 in v4. Expected risk: the additional
INERTIA EVOLUTION field in every briefing envelope adds per-stage overhead; a model may
populate it with anchor-copies ("anchor unchanged") for most stages, producing shallow
trajectory entries rather than genuine posture evolution analysis.

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

INERTIA: [What the organization currently does instead of this topic — the specific process,
tool, or behavior this topic would displace. One sentence, concrete. "Current state" fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT — 5 parts per stage:**

**PART 1 — BRIEFING ENVELOPE (Stage 2+ only)**

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through this stage's lens.
Lens-directed selection required — a TPM selects for schedule and dependency risk;
a PM selects for adoption; a Principal Architect selects for interface coupling.
Generic selection fails.]
OPEN QUESTION FORWARDED: [verbatim from prior stage's Handoff Packet "PASSING TO NEXT STAGE"]
INERTIA EVOLUTION: [How has the displacement posture shifted since Stage 1, or since the
immediately prior stage? Name the specific prior finding that changed the picture, if any.
Format: "[Stage name] [F-ID] [hardened / softened] the displacement posture by [one clause]."
Or: "Anchor unchanged — no prior finding has modified the displacement picture."]
```

For Stage 1: write `First stage — no briefing envelope.`

**PART 2 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
INERTIA STAGE READING: [Given the current inertia evolution state from Part 1 above,
how does this role interpret the displacement risk as it stands at this stage? One sentence.
Stage 1: "Baseline — displacement posture not yet modified by any prior finding."]
```

**PART 3 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding that directly responds to the
OPEN QUESTION FORWARDED in the briefing envelope]

### Cross-Stage References

[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence]
[Stage 1: write "First stage — no cross-stage references."]
[Stage 2+: minimum 1 entry; must cite a specific F-ID from a prior stage]
```

**PART 4 — STAGE CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
CROSS-STAGE SYNTHESIS:
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what does this
stage's finding add to the significance of the prior finding or change about its resolution
path? Must add substance not already stated in the Cross-Stage References section above.]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

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

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in >=2 stages.
Multi-stage recurrence from independent reviewers is stronger than any single-stage finding:
two lenses reached the same conclusion without coordination. Document that convergence and
explain what multi-stage recurrence adds to severity that the individual finding did not.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each must cite >=2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] -> [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add to severity that the individual finding alone did not establish?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE — [reason]".
```

**SECTION B — INERTIA TRAJECTORY**

```
## Inertia Trajectory

Synthesize the INERTIA EVOLUTION fields from all briefing envelopes. Map the displacement
posture across all six stages — do not generate new analysis, compile from the envelopes.

| Stage       | Posture Change                                                |
|-------------|---------------------------------------------------------------|
| leadership  | [hardened / softened / unchanged] — [one clause or "baseline"] |
| teams       | [hardened / softened / unchanged] — [one clause]              |
| pm          | [hardened / softened / unchanged] — [one clause]              |
| tpm         | [hardened / softened / unchanged] — [one clause]              |
| arch-board  | [hardened / softened / unchanged] — [one clause]              |
| exec-office | [hardened / softened / unchanged] — [one clause]              |

NET DISPLACEMENT POSTURE: [hardened / softened / unchanged from Anchor]
KEY TURNING POINT: [which stage finding most shifted the posture, and what it changed]
```

**SECTION C — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BRIEFING CHAIN HEALTH: [Did each briefing envelope distill or copy prior findings? Were
KEY CONCERNS selections lens-directed or generic? Any break in the chain? One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 5 parts
in order. CROSS-STAGE SYNTHESIS in the Handoff Packet must add substance not already stated
in Cross-Stage References. INERTIA TRAJECTORY (Section B) compiles from briefing envelope
INERTIA EVOLUTION fields — it does not introduce new analysis. End-of-run sections
(A then B then C) appear after all stages.

---

## V-04 — V-05 R3 Base + Minimal C-14 + Structural C-15 (Combination)

**Axes**: Axis 1 (C-14 minimal form) + Axis 2 (C-15 structural separation) on V-05 R3 base
**Hypothesis**: V-05 R3 scored 100 under v2 but drops to 97.1 under v3 (fails C-14 and C-15).
Its minimal 3-section design is the smallest structure that passed all v2 criteria. V-04
upgrades V-05 R3 with the minimum additions required to pass C-14 and C-15 under v3:
(1) A compressed STAGE-OPEN FORWARD block prepended to Section 1 for Stage 2+ — satisfying
C-14's "role-loading at stage open" requirement with a 3-field single-line structure;
(2) A `### Prior-Stage Reading` subsection in Section 2 findings — creating a second
backward-synthesis surface alongside the handoff packet, enabling C-15 to apply;
(3) `DOWNSTREAM SIGNIFICANCE:` as the packet synthesis field name — asking a different
question than the Prior-Stage Reading ("what consequence does this reveal downstream?")
so copy behavior is structurally impossible without a negative instruction.
Expected benefit: 100 under v3 with the smallest possible per-stage footprint, preserving
V-05 R3's minimal architecture. Expected risk: C-14's minimal form (3-field Stage-Open
Forward) may earn PARTIAL rather than PASS if the rubric requires the full 4-field briefing
envelope; C-15's structural separation may earn PARTIAL rather than PASS if the rubric
requires an explicit negative guard. Combined failure mode: both PARTIAL -> 7/7 drops to
~5.6/7 -> score around 96.

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

INERTIA: [What the organization currently does instead of this topic — the specific process,
tool, or behavior this topic would displace. One sentence, concrete. "Current state" fails.]
DISPLACEMENT COST: [Who bears the switching cost. One sentence.]
```

4. Fallback if files absent: assign by stage name.

---

**STAGE FORMAT — 3 sections per stage:**

**SECTION 1 — STAGE IDENTITY**

For Stage 2+, begin with the STAGE-OPEN FORWARD block before the stage header. This
step must appear before any findings are written — role-loading on forwarded context
happens at stage open.

```
STAGE-OPEN FORWARD (Stage 2+ only):
[prior stage] -> [this stage]:
CONCERN: [F-ID] ([concern in one phrase filtered through this role's lens])
FORWARDED: [verbatim PASSING TO NEXT STAGE text from prior stage handoff packet]
INERTIA: [unchanged / shifted — one clause]
Lens: [which aspect of the forwarded concern is most relevant to this role's orientation?
State it before findings begin. A TPM names a schedule or dependency dimension. A PM names
an adoption or handoff dimension. A Principal Architect names an interface or coupling
dimension. Generic selection fails.]

[Stage 1: omit this block entirely — write the stage header directly.]

## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
```

**SECTION 2 — FINDINGS**

At least one finding per stage must be grounded in the loaded role's specific orientation
from `.roles/`. Generic findings that any reviewer could have written (e.g., "timeline
is aggressive," "adoption may be slow") do not satisfy C-02 on their own. Stage 2+ requires
at least one finding that directly addresses the STAGE-OPEN FORWARD CONCERN above.

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; each finding names the specific artifact or behavior under review]

### Prior-Stage Reading

[prior stage] F-[N]: [one sentence: what does this role's orientation reveal about that
prior finding that the prior stage reviewer could not have seen? How does this role's lens
change the reading of that finding's severity or ownership?]
[Stage 1: write "First stage — prior-stage reading begins Stage 2."]
[Stage 2+: minimum 1 entry; must name the role-specific lens perspective, not just
confirm/escalate/contradict without lens attribution]
```

**SECTION 3 — STAGE CLOSE**

The handoff packet carries two contributions. `PASSING TO NEXT STAGE` is the forward
charge — what the next stage must examine. `DOWNSTREAM SIGNIFICANCE` is the backward
contribution — what consequence for downstream stages this prior finding carries now that
this stage has reviewed it. These are different questions: `Prior-Stage Reading` (Section 2)
asks how this role reads a prior finding; `Downstream Significance` asks what consequence
that finding acquires downstream given this stage's view. Do not copy the Prior-Stage
Reading into Downstream Significance.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change this verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:"]
DOWNSTREAM SIGNIFICANCE:
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what downstream
consequence does this prior finding carry now that this stage has reviewed it? What failure
mode, amplifying condition, or ownership gap becomes visible at this stage that was not
visible before?]
[Stage 1: write "First stage — downstream significance begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings (Section 2), before Stage Close (Section 3):

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | MED      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH/HIGH]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
Conditions (if GO WITH CONDITIONS): [what must be resolved before proceeding]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings (Section 2), before Stage Close (Section 3):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic goals" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in >=2 stages.
Multi-stage recurrence from independent reviewers is stronger than any single-stage finding:
two lenses reached the same conclusion without coordination. Document that convergence and
explain what it adds to severity that the individual finding did not.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes for a full run; each theme must cite >=2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] -> [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add? Why is convergence across two independent reviewer lenses more significant than either
finding alone?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE — [reason]".
```

**SECTION B — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 3 sections
in order. For Stage 2+, STAGE-OPEN FORWARD appears before the `## Stage:` header — role-loading
on forwarded context precedes all findings. `Prior-Stage Reading` (Section 2) answers "how
does my role read this prior finding?" — it is a lens-specific re-reading. `Downstream
Significance` (Section 3 packet) answers "what downstream consequence does this finding
carry now?" — it is a forward-looking consequence statement about downstream stages. These
questions cannot be answered identically. End-of-run sections (A then B) appear after all stages.

---

## V-05 — Pre-Printed Envelope + Inertia Evolution (Combination)

**Axes**: Axis 3 (inertia thread depth) + Axis 4 (pre-printed template structural guarantee)
on V-04 R3 base
**Hypothesis**: V-04 R3 achieves 100 under v3. Two new axes are applied simultaneously:
(1) Pre-printed briefing envelope (strongest structural guarantee for C-14 — model fills
`[FIELD]` slots rather than generating the structure, eliminating the class of failures
where the envelope collapses to prose or omits fields);
(2) Inertia evolution tracking thread from V-03 (C-16 candidate — adds INERTIA EVOLUTION
field to the briefing envelope, INERTIA STAGE READING to stage identity, and a new
INERTIA TRAJECTORY section at end-of-run).
Both axes build on V-04 R3's proven 100-scoring architecture; neither axis removes any
mechanism. Expected benefit: V-05 scores 100 under v3 with the strongest C-14 structural
guarantee in any R4 variation AND surfaces the inertia trajectory pattern for C-16 evaluation.
Expected risk: the pre-printed envelope adds prompt surface and the inertia evolution fields
add per-stage overhead; combined pressure may produce briefing envelope entries that are
formally complete (all `[FIELD]` slots filled) but qualitatively shallow — particularly the
INERTIA EVOLUTION field, which requires the model to identify which prior finding changed
the displacement posture rather than defaulting to "anchor unchanged."

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
3. Before Stage 1, write the INERTIA ANCHOR block (pre-printed — fill all fields):

```
## Inertia Anchor

INERTIA: [process/tool/behavior this topic displaces — one sentence; "current state" fails]
DISPLACEMENT COST: [who bears it and what it is — one sentence]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT — 5 parts per stage:**

**PART 1 — BRIEFING ENVELOPE (Stage 2+ only)**

Pre-printed structure — fill all `[FIELD]` slots. Do not omit any field or collapse
to prose. Do not skip this part for Stage 2+.

```
### Briefing Envelope

PRIOR STAGE: [stage-name]
ROLE THIS STAGE: [role-title] | ORIENTATION: [one-phrase lens]
KEY CONCERNS (lens-directed — select what this role most needs from prior findings):
  [F-ID]: [concern phrase viewed through this role's lens]
  [F-ID]: [concern phrase viewed through this role's lens]
  (add rows as needed; minimum 1 row; do not select generically)
OPEN QUESTION FORWARDED: [verbatim PASSING TO NEXT STAGE text from prior handoff packet]
INERTIA EVOLUTION: [Has any prior finding hardened or softened the displacement posture?]
  [Stage name] [F-ID] [hardened / softened] — [one clause explaining the posture shift]
  [Or: "Anchor unchanged — no prior finding has modified the displacement posture."]
```

For Stage 1: write `## Stage 1 — No briefing envelope.` and proceed to Part 2.

**PART 2 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
INERTIA STAGE READING: [Given INERTIA EVOLUTION from Part 1 above, how does this role
interpret the current displacement posture? What does it mean for this review?
One sentence. Stage 1: "Baseline — no prior evolution; posture reads from Anchor directly."]
```

**PART 3 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; Stage 2+ requires at least one finding that directly addresses the
OPEN QUESTION FORWARDED from Part 1]

### Cross-Stage References

[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: role-lens-specific
reading of that prior finding]
[Stage 1: write "First stage — no cross-stage references."]
[Stage 2+: minimum 1 entry; must cite a specific F-ID from a prior stage]
```

**PART 4 — STAGE CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:"]
CROSS-STAGE SYNTHESIS:
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what does this
stage's finding add to the significance of the prior finding or change about its resolution
path? Must add substance not already stated in the Cross-Stage References section above.]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total >= 5 entries across a 6-stage run]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is affected] / NO
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

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

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings (Part 3), before Stage Close (Part 4):

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order.

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in >=2 stages.
Multi-stage recurrence from independent reviewers is stronger than any single-stage finding:
two lenses reached the same conclusion without coordination. Document that convergence and
explain what multi-stage recurrence adds to severity that the individual finding did not.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes; each must cite >=2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] -> [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add to severity that the individual finding alone did not establish?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE — [reason]".
```

**SECTION B — INERTIA TRAJECTORY**

```
## Inertia Trajectory

Compile from INERTIA EVOLUTION fields in all briefing envelopes. Do not generate new
analysis — map what each envelope recorded.

| Stage       | Posture Change                                                 |
|-------------|----------------------------------------------------------------|
| leadership  | [hardened / softened / unchanged] — [one clause or "baseline"] |
| teams       | [hardened / softened / unchanged] — [one clause]               |
| pm          | [hardened / softened / unchanged] — [one clause]               |
| tpm         | [hardened / softened / unchanged] — [one clause]               |
| arch-board  | [hardened / softened / unchanged] — [one clause]               |
| exec-office | [hardened / softened / unchanged] — [one clause]               |

NET DISPLACEMENT POSTURE: [hardened / softened / unchanged from Anchor]
KEY TURNING POINT: [which stage finding most shifted the posture, and what it changed]
```

**SECTION C — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BRIEFING CHAIN HEALTH: [Did each briefing envelope distill or copy prior findings? Were
KEY CONCERNS selections lens-directed or generic? Any break in the chain? One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 5 parts
in order. Briefing Envelope (Part 1) is pre-printed — fill all `[FIELD]` slots; do not
collapse to prose or omit any row. CROSS-STAGE SYNTHESIS must add substance not already
stated in Cross-Stage References. INERTIA TRAJECTORY (Section B) compiles from INERTIA
EVOLUTION fields in briefing envelopes — it does not introduce new analysis. End-of-run
sections (A then B then C) appear after all stages.
