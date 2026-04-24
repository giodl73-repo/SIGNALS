---
skill: quest-variate
skill_target: corps-rob
round: 3
date: 2026-03-17
rubric_version: 2
---

# Variate R3 — corps-rob (rubric v2, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v2.
Single-axis variations V-01 through V-02, then combinations V-03 through V-05.

**R2 diagnosis:** V-05 led at 97. Two universal failures block the ceiling:
- **C-10 FAIL** (all 5 variations): END-OF-RUN SUMMARY fields are run-level diagnostics,
  not document-level Cross-Cutting Theme aggregators. C-10 requires named themes with ≥2
  independent stage F-ID citations and a severity-elevation explanation.
- **C-11 PARTIAL** (all passing variations): Handoff packet at stage close lacks backward
  cross-stage entries with source F-ID + relationship type. Backward synthesis lives at
  stage open (Briefing Envelope) or in a separate References section — not in the packet itself.

R3 explores whether fixing C-10 and C-11 independently and then combining them on V-05's
proven structural base can push the score above 97. V-05 also tests whether the briefing
envelope can be eliminated (consolidating its work into the handoff packet) for a
constraint-minimized design that still passes all 13 criteria.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| C-10 fix only: Cross-Cutting Themes section added; minimal base otherwise | V-01 |
| C-11 fix only: backward F-ID entries in closing handoff packet; V-05 base minus briefing envelope | V-02 |
| C-11 fix on V-05 full base: enriched handoff packet retains briefing envelope | V-03 |
| C-10 + C-11 fix on V-05 full base: both gaps fixed, all V-05 excellence patterns preserved | V-04 |
| Constraint-minimized: no briefing envelope; C-11 via packet; C-10 via themes section; 3-section stage | V-05 |

---

## V-01 — Cross-Cutting Themes (C-10 Fix, Single-Axis)

**Axis**: Lifecycle emphasis (end-of-run cross-cutting theme elevation)
**Hypothesis**: The single structural difference between R2 scores and a C-10 PASS is an
explicit **CROSS-CUTTING THEMES** section after all stages — named themes, ≥2 F-ID citations
per theme from different stages, and a sentence explaining why multi-stage recurrence elevates
severity. V-01 adds this section to a minimal base (V-04 R1 architecture: global anchor +
per-stage inertia check + handoff + blocker) to isolate whether C-10 can be fixed without the
briefing envelope's overhead. Expected benefit: clean C-10 PASS + preserved V-04 R1 score on
all other criteria. Expected risk: the themes section degrades to an index of already-listed
findings rather than synthesizing genuine elevation — "same concern appeared twice" without
explaining what double-recurrence adds.

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
tool, or behavior this topic would displace. One sentence, concrete.
Pass: "Teams manually file ADRs in Confluence after implementation."
Fail: "Current state will need to change."]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: assign by stage name (VP Product for leadership, Team Leads
   for teams, Senior PM for pm, TPM Lead for tpm, Principal Architect for arch-board,
   Chief of Staff for exec-office).

---

**STAGE FORMAT — 4 steps per stage:**

**STEP 1 — STAGE OPEN**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global
inertia anchor reads from this role's perspective. What does this role stand to lose
or protect if the displaced behavior changes?]
```

**STEP 2 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; each finding must name the specific artifact or behavior under review,
not just the problem domain]

Cross-Stage References (Stage 2+ only):
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence]
[Stage 1: write "First stage — no upstream references."]
```

**STEP 3 — VERDICT**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]
```

**STEP 4 — HANDOFF PACKET**

```
### Handoff Packet

PASSING TO NEXT STAGE: [the specific concern the next stage must address — not generic]
BLOCKER: YES — [F-ID] — [what is blocked and why downstream] / NO
```

For exec-office: write `PASSING TO ROB SPONSOR:` instead of `PASSING TO NEXT STAGE:`.
For Stage 1 (leadership): Handoff Packet is required; Cross-Stage References writes
"First stage — no upstream references."

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings (Step 2), before Verdict (Step 3):

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

After Findings, before Verdict:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic goals" or "company priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write after all stage sections, in this order:

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme is a concern that surfaces independently in 2 or more stages.
Independent recurrence is a stronger signal than any single-stage finding: the concern
survived multiple reviewer lenses and role orientations without coordination.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes for a full 6-stage run; each theme must cite ≥2 F-IDs from different stages]

For each theme, write the elevation sentence:
T-[N]: [stage] [F-ID] → [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add to severity that the finding alone did not establish? Why is two independent discoveries
worse than one?]

Fallback: if fewer than 2 genuine themes exist, write:
"THEME-SPARSE RUN — [reason concerns did not recur] — closest candidate: [name + F-IDs]"
```

**SECTION B — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES entry — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. End-of-run sections (A then B)
appear after all stage sections, never inside a stage.

---

## V-02 — Backward-Consolidating Packet (C-11 Fix, Single-Axis)

**Axis**: Lifecycle emphasis (handoff packet at stage close consolidates both forward charge
and backward cross-stage synthesis with F-IDs)
**Hypothesis**: R2's C-11 PARTIAL failure had a consistent pattern: backward synthesis with
F-IDs lived at stage *open* (Briefing Envelope KEY CONCERNS or Received Forward sections),
not at stage *close* where C-11 requires it. V-02 tests whether moving all backward synthesis
into the closing handoff packet — a three-field structure: FORWARD CHARGE + CROSS-STAGE
SYNTHESIS (F-ID entries) + BLOCKER — produces a C-11 PASS without the briefing envelope
overhead. No global anchor in the minimal base. Expected benefit: structural C-11 compliance
because the packet at close now contains F-ID entries with relationship types. Expected risk:
without the briefing envelope, cross-stage coherence (C-08) loses its richest mechanism;
the Cross-Stage Synthesis in the packet may satisfy C-11 but degrade C-08 below PASS
if the model treats it as a transcript rather than an engagement.

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

INERTIA: [What the organization currently does instead of this topic — specific. One sentence.]
DISPLACEMENT COST: [Who bears the switching cost. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT — 3 sections per stage:**

**SECTION 1 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: what does this role
stand to lose or defend given the global inertia anchor?]
```

**SECTION 2 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; each finding must reference the specific artifact or behavior under review]
```

**SECTION 3 — STAGE CLOSE**

The handoff packet consolidates both what this stage passes forward AND what this stage's
findings say about prior findings. Both halves live here, at close.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

FORWARD CHARGE: [the single most important open question for the next stage — specific]
CROSS-STAGE SYNTHESIS (Stage 2+ only):
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what this
stage's finding adds to or changes about the prior finding's significance]
[minimum 1 entry per packet for Stage 2+; total ≥ 5 entries across a 6-stage run]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is affected] / NO
```

For exec-office: write `FORWARD CHARGE:` as `PASSING TO ROB SPONSOR:`.

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
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings, before Stage Close:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any FORWARD CHARGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 3 sections
in order. Cross-stage synthesis belongs in the Handoff Packet at stage close — not in a
separate section before the verdict.

---

## V-03 — C-11 Fix on V-05 Base (Enriched Handoff Packet)

**Axes**: V-05 architecture (briefing envelope + global anchor + per-stage inertia check)
+ backward F-ID entries added to the closing handoff packet
**Hypothesis**: V-05 scored 97 with C-11 PARTIAL because its backward synthesis lived at
stage open (Briefing Envelope KEY CONCERNS with F-IDs) rather than at stage close (the
handoff packet). C-11 requires backward entries in the closing packet. V-03 keeps all of
V-05's mechanisms and adds a CROSS-STAGE SYNTHESIS block to the handoff packet — making
the packet formally bi-directional: PASSING TO NEXT STAGE (forward) + CROSS-STAGE SYNTHESIS
(backward F-ID entries) + BLOCKER. Expected benefit: C-11 PASS while preserving V-05's
C-08 lead (three-layer cross-stage mechanism: briefing envelope + cross-stage references
section + handoff packet). Expected risk: having backward synthesis in *both* the briefing
envelope (at open) and the handoff packet (at close) creates redundancy — the model may
write the packet entries as copies of the briefing envelope rather than new synthesis, which
could reduce apparent depth even if criteria are structurally satisfied.

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

Before review work, the incoming stage synthesizes what prior stages surfaced. Not a transcript
— a distillation filtered through *this stage's specific lens*.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries most relevant to this stage's lens.
Lens-directed selection required — a TPM selects for schedule and dependency risk;
a PM selects for adoption and handoff completeness; a Principal Architect selects for
interface coupling and maintenance debt. Generic selection fails.]
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
OPEN QUESTION FORWARDED in the briefing envelope above]

### Cross-Stage References

[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence]
[Stage 1: write "First stage — no cross-stage references."]
[Stage 2+: minimum 1 entry required; must cite a specific F-ID from a prior stage]
```

**PART 4 — STAGE CLOSE**

The handoff packet carries both a forward charge and a backward synthesis. These are two
distinct contributions: the forward charge tells the next stage what to examine; the
cross-stage synthesis tells the full record what this stage's view adds to prior findings.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:" instead.]
CROSS-STAGE SYNTHESIS:
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what this stage's
finding adds to the prior finding's significance or changes about its resolution path.
This is not a copy of the Cross-Stage References section above — it may cover the same
F-IDs but must add something the references section did not say about downstream impact.]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total ≥ 5 entries across a 6-stage run]
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
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings, before Stage Close:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" or "company goals" fails]
```

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BRIEFING CHAIN HEALTH: [Did each stage's briefing envelope distill or copy prior findings?
Were KEY CONCERNS selections lens-specific or generic? Any break in the chain? One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not addressed by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 5 parts
in order. The CROSS-STAGE SYNTHESIS in the Handoff Packet (Part 4) and the Cross-Stage
References section (Part 3) cover different ground: References record the stage-level
assessment; Synthesis states the downstream significance.

---

## V-04 — C-10 + C-11 Fix on V-05 Base (Both Gaps Closed)

**Axes**: All V-05 patterns (briefing envelope + global anchor + per-stage inertia check +
handoff packet + blocker) + backward F-ID entries in closing packet (C-11 fix) +
Cross-Cutting Themes section at end-of-run (C-10 fix)
**Hypothesis**: V-04 is the first R3 variation designed to score above V-05 R2's 97.
V-05's two C-11 PARTIAL (1 pt) and C-10 FAIL (0 pt) gaps cost it 3 points. V-04 fixes both
by (1) adding a CROSS-STAGE SYNTHESIS block to every closing handoff packet and (2) adding
a mandatory CROSS-CUTTING THEMES section after all stages that names themes, cites ≥2 F-IDs
per theme from different stages, and explains why multi-stage recurrence elevates severity.
All other V-05 mechanisms preserved: the briefing envelope remains at stage open as the
role-directed synthesis layer; the Cross-Stage References section in Findings remains as the
per-stage assessment layer; the handoff packet is now bi-directional. Expected risk: the
combination of briefing envelope (open) + cross-stage references section (findings) +
enriched handoff packet (close) + cross-cutting themes section (end-of-run) creates four
overlapping backward-synthesis surfaces — the model may produce shallow entries at each
to satisfy the structure rather than genuine escalation analysis.

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

Synthesize what prior stages surfaced, filtered through this stage's specific lens. Distillation, not transcript.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 F-IDs + one-phrase summaries selected through this stage's lens.
Must be lens-directed — a TPM picks differently than a PM or Principal Architect.]
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
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what this stage's
finding adds to the significance of the prior finding or changes about its resolution path.
Must add substance not already stated in the Cross-Stage References section above.]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
[Stage 2+: minimum 1 entry per packet; total ≥ 5 entries across a 6-stage run]
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
Conditions (if GO WITH CONDITIONS): [what must be resolved]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings, before Stage Close:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic priorities" fails]
```

---

**END-OF-RUN SECTIONS (--stage all only):**

Write in this order after all stage sections.

**SECTION A — CROSS-CUTTING THEMES**

```
## Cross-Cutting Themes

A cross-cutting theme exists when the same concern surfaces independently in ≥2 stages.
Independent recurrence is a stronger signal than any single-stage finding: the concern
survived multiple reviewer lenses and role orientations. That convergence — not the
individual finding — is what a theme documents and why it demands elevated response.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes for a full 6-stage run; each theme must cite ≥2 F-IDs from different stages]

For each theme, write the elevation sentence:
T-[N]: [stage] [F-ID] → [stage] [F-ID] — [one sentence: what does multi-stage recurrence
add to severity that the individual finding did not establish? What changes when two
independent reviewers from different functions surface the same concern?]

Fallback: if fewer than 2 genuine themes exist, write "THEME-SPARSE — [reason]".
```

**SECTION B — ROB SUMMARY**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BRIEFING CHAIN HEALTH: [Did each briefing envelope distill or copy? Were KEY CONCERNS
lens-specific? Any stage break in the chain? One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by exec-office — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all 5 parts
in order. End-of-run sections (A then B) appear after all stages. Cross-Stage Synthesis in
the Handoff Packet and Cross-Stage References in Findings cover the same F-IDs from different
angles — References record the per-stage assessment; Synthesis states downstream significance.

---

## V-05 — Constraint-Minimized Full Coverage

**Axes**: No briefing envelope; backward synthesis consolidated into closing handoff packet
(C-11); Cross-Cutting Themes section at end-of-run (C-10); global anchor + per-stage
inertia check (C-13); 3-section stage structure (minimum viable footprint)
**Hypothesis**: V-04's four backward-synthesis surfaces (briefing envelope + cross-stage
references + handoff packet synthesis + cross-cutting themes) may produce shallow compliance
rather than genuine depth. V-05 tests whether a minimal design — 3-section stage format,
no briefing envelope, all backward synthesis in the closing handoff packet — can pass all
13 criteria with a smaller prompt surface. The briefing envelope's role-directed prior-findings
synthesis is absorbed into the CROSS-STAGE SYNTHESIS field of the handoff packet: each stage
closes by writing both its forward charge AND its backward synthesis with F-IDs. One mechanism
per gap. Expected benefit: each structural element has a single, unambiguous home — no
redundancy, no copy-task risk. Expected risk: without the briefing envelope forcing lens-directed
selection at stage open, C-02 role-specificity may degrade because nothing requires the model
to filter prior findings through the incoming role's orientation before writing findings.

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

INERTIA: [What the organization currently does instead of this topic — specific process, tool,
or behavior being displaced. One sentence. "Current state" or "existing approach" fails.]
DISPLACEMENT COST: [Who bears the switching cost. One sentence.]
```

4. Fallback if files absent: assign by stage name.

---

**STAGE FORMAT — 3 sections per stage:**

**SECTION 1 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global inertia
anchor reads from this role's perspective. What does this role stand to lose or protect?]
```

**SECTION 2 — FINDINGS**

At least one finding must be grounded in the role's specific orientation from `.roles/` —
the concern a TPM notices is not the concern a Principal Architect notices. Generic findings
that any reviewer could have written (e.g., "timeline is aggressive," "adoption may be slow")
do not satisfy C-02 on their own.

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; each finding must name the specific artifact or behavior under review,
not just the problem domain]
```

**SECTION 3 — STAGE CLOSE**

The handoff packet is the stage's only closing artifact. It carries both directions:
FORWARD (what the next stage must examine) and BACKWARD (what this stage's findings say
about prior findings). Both are required from Stage 2 onward.

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must name what would change this verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern for the next stage — specific.
Final stage (exec-office): write "PASSING TO ROB SPONSOR:"]
CROSS-STAGE SYNTHESIS (Stage 2+ only):
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence: what does this
stage's finding add to the significance of the prior finding, or what changes about
its owner and resolution path given this stage's view?]
[minimum 1 entry per packet for Stage 2+; total ≥ 5 entries across a 6-stage run]
[Stage 1: write "First stage — cross-stage synthesis begins Stage 2."]
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

After Findings, before Stage Close:

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

A cross-cutting theme exists when the same concern surfaces independently in ≥2 stages.
Multi-stage recurrence from independent reviewers is a stronger signal than any single-stage
finding: two lenses reached the same conclusion without coordination. Document that convergence
— and explain what it adds to severity that the individual finding alone did not.

| Theme ID | Name             | Stages + F-IDs         | Trajectory               |
|----------|-----------------|------------------------|--------------------------|
| T-01     | [named concern] | [stage F-N, stage F-N] | ESCALATING / STABLE / MIXED |
[minimum 2 themes for a full run; each theme must cite ≥2 F-IDs from different stages]

For each theme:
T-[N]: [stage] [F-ID] → [stage] [F-ID] — [one sentence: what does multi-stage recurrence
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
in order. End-of-run sections (A then B) appear after all stages. The Cross-Stage Synthesis
field in the Handoff Packet is the sole vehicle for backward F-ID linkage — there is no
separate cross-stage references section in this design.
