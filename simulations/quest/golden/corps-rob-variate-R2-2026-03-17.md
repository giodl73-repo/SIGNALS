---
skill: quest-variate
skill_target: corps-rob
round: 2
date: 2026-03-17
rubric_version: 2
---

# Variate R2 — corps-rob (rubric v2, 2026-03-17)

5 complete prompt body variations for the `corps-rob` skill against rubric v2.
Single-axis variations V-01 through V-03, then combinations V-04 and V-05.

R1 note: V-04 R1 already achieves ~99 under v2 (handoff packet + blocker field directly present).
R2 explores whether alternate structural paths to C-11/C-12/C-13 perform as well, and whether
adding a briefing envelope (V-05) pushes past V-04 R1's ceiling.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Per-stage distributed inertia (each stage writes own role-specific inertia; no global anchor) | V-01 |
| Blocker-at-open (Stage N+1 clears Stage N's blockers before proceeding; gate-check pattern) | V-02 |
| Handoff-centric structure (handoff packet as primary artifact; findings as supporting evidence) | V-03 |
| Per-stage inertia + handoff-centric + blocker field (all three C-13/C-11/C-12 distributed, no global anchor) | V-04 |
| Briefing envelope + global anchor + handoff + blocker (V-04 R1 structure + explicit prior-stage briefing section) | V-05 |

---

## V-01 — Per-Stage Distributed Inertia

**Axis**: Inertia framing
**Hypothesis**: Requiring each stage to write its own role-specific inertia statement before findings —
rather than referencing a single shared global anchor — produces richer C-13 compliance because a VP's
inertia pressure is genuinely different from a TPM's. The expected benefit: each stage's findings are
grounded in concretely different status-quo pressures, improving C-02 role-specificity. The expected
risk: without a shared anchor, cross-stage inertia coherence (C-08) may degrade — the five inertia
statements may not cohere into a single picture of what the topic displaces.

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
3. Fallback if files absent: assign by stage name (VP Product for leadership, Team Leads for teams,
   Senior PM for pm, TPM Lead for tpm, Principal Architect for arch-board, Chief of Staff for exec-office).
4. No global inertia anchor — each stage writes its own (see Stage Format below).

---

**STAGE FORMAT — all stages follow this structure:**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] — [orientation in one phrase]

### Role Inertia Statement

INERTIA (this role's view): [What specifically does this role stand to lose, have to change,
or have to defend if this topic ships? One sentence. Must name a concrete behavior, process,
tool, or budget item — not "existing approach" or "current state."
Examples that pass: "TPM absorbs unplanned scope without schedule amendment";
"PM displaces a roadmap item already committed to a customer";
"Principal Architect inherits a new integration surface with no owner contract."
Examples that fail: "existing approach will change"; "teams will need to adapt."]

STATUS-QUO PRESSURE: [HIGH / MED / LOW] — [one sentence: why this role feels this level of
pressure to preserve the status quo before looking at the topic]

### Findings

F-01 [HIGH/MED/LOW] [specific concern grounded in this role's lens and inertia context]
     Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern grounded in this role's lens and inertia context]
     Owner: [role] — Resolution: [concrete action]
[minimum 2 findings; at least one finding must connect to the role's inertia statement above]

[Cross-Stage References — Stage 2+ only:]
[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence]
[Stage 1: omit this block entirely]

### Stage Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID; must say what would change the verdict]

### Handoff Packet

PASSING TO NEXT STAGE: [the open question or concern the next stage must address — specific]
BLOCKER: YES — [F-ID] — [one sentence: what is blocked and why] / NO
```

For Stage 1 (leadership): Handoff Packet is required; note `First stage — no cross-stage references.`
in the Findings section.

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings, before Stage Verdict:

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

After Findings, before Stage Verdict:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission must be named specifically — "strategic goals" fails]
```

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

INERTIA PATTERN: [What did the distributed inertia statements reveal in aggregate?
Was there a common displacement target, or did each role feel distinct pressure?
One to two sentences.]
BLOCKERS RAISED: [list each stage that set BLOCKER: YES with finding ID — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE item not resolved by the final stage — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage is its own labeled section in sequence.

---

## V-02 — Blocker-at-Open (Reversed Detection Direction)

**Axis**: Lifecycle emphasis (blocker detection at stage open, not stage close)
**Hypothesis**: Moving blocker detection to the stage open — requiring Stage N to declare whether it
can proceed given Stage N-1's output — shifts accountability from "I raise a blocker for downstream"
to "I must clear upstream blockers before I proceed." This should produce more explicit go/no-go logic
at stage transitions (C-05 analog for non-TPM stages) and force richer cross-stage references (C-08)
because each stage must actively engage with the prior stage's output rather than passively recalling it.
Expected failure mode: the gate check becomes formulaic ("no blockers, proceeding") when no upstream
blockers exist — the mechanism is most valuable in multi-stage runs with a real blocker.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify roles assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic — the existing process,
tool, or behavior this topic would displace. One sentence, specific. "Current state" alone fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT — each stage follows this four-part structure:**

**PART 1 — GATE CHECK (Stage 2+ only; Stage 1 writes: `First stage — no upstream gate.`)**

```
### Gate Check

PRIOR STAGE VERDICT: [restate the prior stage's verdict token exactly — APPROVED /
APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
BLOCKERS FROM PRIOR STAGE: [list any BLOCKER: YES items from prior stage with F-ID — or "None declared"]

PROCEED / HOLD:
- PROCEED if prior verdict is APPROVED or APPROVED WITH CONDITIONS and no unresolved blockers remain.
- HOLD if prior verdict is BLOCKED or an unresolved BLOCKER: YES was declared.

If HOLD: state which F-ID from the prior stage must be resolved before this stage can run.
Write: `HOLD — blocked by [prior stage] [F-ID]: [one sentence on what must be resolved]`
Do not write findings for a held stage — end the stage section after HOLD.
```

**PART 2 — STAGE IDENTITY AND INERTIA CHECK**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence from this role's
perspective: what do they stand to lose or gain if the status quo changes?]
```

**PART 3 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; finding concerns must name the specific artifact or behavior, not just the domain]
```

For Stage 2+: include cross-stage references immediately after findings when this stage's work
confirms, escalates, or contradicts a prior finding:
```
Cross-stage: [prior stage] [F-ID] — [confirm / escalate / contradict] — [one sentence]
```

**PART 4 — CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

BLOCKER: YES — [F-ID] — [which downstream stage this blocks and why] / NO
```

Note: BLOCKER is populated here at stage close based on findings written in this stage.
Name the specific downstream stage it affects — not "future stages" generically.

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings (Part 3), before Verdict (Part 4):

```
### Risk Register

| ID   | Risk             | Severity | Likelihood | Mitigation            |
|------|-----------------|----------|------------|-----------------------|
| R-01 | [specific risk] | HIGH     | HIGH       | [concrete mitigation] |
| R-02 | [specific risk] | MED      | MED        | [concrete mitigation] |
| R-03 | [specific risk] | LOW      | LOW        | [concrete mitigation] |
[minimum 3 entries; at least 1 HIGH severity]

### Go/No-Go

**GO / NO-GO / GO WITH CONDITIONS**
Rationale: [cite at least one F-ID or R-ID]
```

**EXEC-OFFICE STAGE — ADDITIONAL REQUIRED SECTION:**

After Findings, before Verdict:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific]
```

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

GATE HISTORY: [list each stage and PROCEED or HOLD — or "all stages proceeded"]
BLOCKERS RAISED: [list each stage that set BLOCKER: YES with F-ID — or "None"]
OPEN HANDOFFS: [any items not cleared — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. A stage that hits HOLD terminates at the
HOLD declaration — do not write findings for a held stage.

---

## V-03 — Handoff-Centric Structure

**Axis**: Lifecycle emphasis (handoff packet as primary artifact; findings as supporting evidence)
**Hypothesis**: Inverting the structure so each stage opens with "what must I hand forward?" and
builds findings to answer that question — rather than discovering findings and then assembling a
handoff — should produce structurally richer handoff packets (C-11) because the handoff is the goal,
not an afterthought. Each stage becomes explicitly accountable to the next. Expected risk: findings
may become backward-reasoned (written to justify a predetermined handoff destination), degrading
their independence and depth (C-04). Also tests whether omitting a global inertia anchor visibly
degrades C-13.

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
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What this topic displaces — specific existing process, tool, or behavior. One sentence.]
DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE STRUCTURE — three sections per stage:**

**SECTION 1 — FORWARD DECLARATION**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] — [orientation in one phrase]

### Forward Declaration

RECEIVED FROM PRIOR STAGE: [the key concern or open question the prior stage handed forward
— verbatim or paraphrased from the prior stage's HANDOFF PACKET.
Stage 1 writes: "First stage — no forward received."]

MY CHARGE: [what this stage must resolve, escalate, or surface to satisfy the forward
declaration — one sentence. Stage 1 writes: "Conduct initial leadership review and identify
what downstream stages must verify."]
```

**SECTION 2 — FINDINGS**

```
### Findings

[Findings answer: what evidence supports or refutes the forward declaration,
or what does this role's lens surface beyond the forward charge?]

F-01 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
[minimum 2; findings must reference the specific artifact or behavior, not just the domain]
[For Stage 2+: at least one finding must directly respond to MY CHARGE above]

CROSS-STAGE (Stage 2+ only):
[prior stage] [F-ID]: [confirm / escalate / contradict] — [one sentence]
[Omit this block for Stage 1]
```

**SECTION 3 — CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern or question for the next
stage — specific, not generic. Final stage (exec-office) writes: "PASSING TO ROB SPONSOR:"]
CONTEXT: [one sentence of background the next stage needs to evaluate it correctly]
BLOCKER: YES — [F-ID] — [what it blocks downstream and why] / NO
```

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings (Section 2), before Close (Section 3):

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

After Findings, before Close:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific — "strategic goals" fails]
```

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

FORWARD CHAIN HEALTH: [did each stage pick up and address the prior stage's forward declaration?
Was the handoff chain coherent end-to-end, or did a stage break the chain?
One sentence.]
BLOCKERS RAISED: [list each stage that set BLOCKER: YES with F-ID — or "None"]
UNRESOLVED CHARGES: [any MY CHARGE items not resolved by the receiving stage — or "All resolved"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all three sections in order.

---

## V-04 — Distributed Inertia + Handoff-Centric + Blocker Field (No Global Anchor)

**Axes**: Per-stage distributed inertia (V-01) + handoff-centric structure (V-03) + explicit blocker field
**Hypothesis**: Combining distributed role-specific inertia (each stage owns its own inertia framing)
with a handoff-centric structure (findings build toward the forward declaration) and a blocker field
at close delivers all three new v2 criteria (C-13, C-11, C-12) through fully distributed mechanisms —
no global anchor, no global ledger. This tests whether C-13 can be satisfied without a shared reference
point. Expected failure mode: without a global anchor, the five per-stage inertia statements may each
name a different displaced behavior, producing a fragmented picture rather than a coherent one. The
INERTIA MAP in the summary is designed to surface this fragmentation if it occurs.

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
3. Fallback if files absent: use stage-name defaults.
4. No global inertia anchor — each stage authors its own (see Section A below).

---

**STAGE FORMAT — four sections per stage:**

**SECTION A — STAGE OPEN**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] — [orientation in one phrase]

### Inertia Statement (this role)

WHAT THIS ROLE DEFENDS: [The specific behavior, process, budget line, or tool that this
role is accountable for and would have to change or justify if this topic ships. One sentence.
Must be concrete — not "existing approach" or "current priorities."
Pass: "TPM absorbs unplanned dependency without schedule relief."
Fail: "current process will need to change."]

INERTIA PRESSURE: [HIGH / MED / LOW] — [one sentence: how strongly does the status quo
pull against this topic from this role's vantage point?]
```

**SECTION B — RECEIVED FORWARD (Stage 2+ only)**

```
### Received Forward

FROM: [prior stage name]
CHARGE: [the forward concern handed from the prior stage — verbatim or paraphrased from
the prior stage's HANDOFF PACKET]
MY RESPONSE: [one sentence: will this stage RESOLVE, ESCALATE, or DEFER the charge?]
```

For Stage 1: write `First stage — no received forward.`

**SECTION C — FINDINGS**

```
### Findings

[At least one finding must connect to the INERTIA STATEMENT (Section A).
For Stage 2+: at least one finding must address the RECEIVED FORWARD charge (Section B).]

F-01 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern] — Owner: [role] — Resolution: [concrete action]
[minimum 2]

Cross-Stage (Stage 2+ only):
[prior stage] [F-ID]: [confirm / escalate / contradict] — [one sentence]
```

**SECTION D — STAGE CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

### Handoff Packet

PASSING TO NEXT STAGE: [the open concern this stage hands forward — specific]
INERTIA NOTE: [does the inertia pressure at this stage suggest the next stage should expect
resistance? YES — [one sentence reason] / NO — [one sentence reason]]
BLOCKER: YES — [F-ID] — [what is blocked and the downstream impact] / NO
```

For the final stage (exec-office): write `PASSING TO ROB SPONSOR:` and still populate BLOCKER.

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings (Section C), before Verdict (Section D):

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

After Findings, before Verdict:

```
### Mission Cascade

| S-Office Mission   | Program        | Artifact/Topic | Alignment               |
|--------------------|----------------|----------------|-------------------------|
| [named mission]    | [program name] | [topic]        | ALIGNED / PARTIAL / GAP |
[minimum 1 row; mission name must be specific]
```

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

INERTIA MAP: [Across all six role inertia statements, what was the aggregate picture?
Where was inertia pressure highest? Did roles name a common displacement target or
independent pressures? One to two sentences.]
BLOCKER CHAIN: [list each BLOCKER: YES by stage and F-ID — or "None raised"]
FORWARD CHAIN: [list each PASSING TO NEXT STAGE item; note whether the receiving stage's
RECEIVED FORWARD acknowledged it — or "All forwarded items acknowledged"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage contains all four sections
(A, B, C, D) in order.

---

## V-05 — Briefing Envelope + Global Anchor + Handoff + Blocker (Full Integration)

**Axes**: Briefing envelope at stage open (explicit prior-findings synthesis authored by the incoming
stage) + global inertia anchor (V-04 R1 C-13 pattern) + handoff packet at close (C-11) + blocker
field at close (C-12)
**Hypothesis**: Adding an explicit briefing envelope — a structured synthesis of prior findings
authored at the opening of each stage from Stage 2 onward — eliminates reliance on model recall for
cross-stage coherence (C-08). The incoming stage writes the briefing from prior outputs, making it an
active synthesis step rather than a passive memory retrieval. Combined with V-04 R1's global anchor,
handoff, and blocker structure, this should maximize C-08, C-11, C-12, and C-13 simultaneously.
Expected cost: the briefing envelope adds ~4 lines per stage and may produce a copy task (pasting
prior finding text) rather than genuine synthesis. The briefing envelope's value depends on whether
the model treats it as a distillation or a transcript. The scoring will distinguish these.

---

You are running `/corps-rob`. Execute a staged Review of Business for the given topic.

**STAGE SEQUENCE:** leadership → teams → pm → tpm → arch-board → exec-office

Flags:
- `--stage [name]` — run one stage only
- `--stage all` — run full sequence
- `--scope [group]` — restrict org.yaml roles to this division or tribe

**SETUP**

1. Read `org.yaml` — identify roles assigned to each stage.
2. Read `.craft/roles/` — load orientation and lens for each role.
3. Before Stage 1, write the INERTIA ANCHOR block:

```
## Inertia Anchor

INERTIA: [What the organization currently does instead of this topic — the existing process,
tool, or behavior this topic would displace. One sentence, specific. "Current state" alone fails.]

DISPLACEMENT COST: [Who bears the switching cost and what it is. One sentence.]
```

4. Fallback if files absent: use stage-name defaults.

---

**STAGE FORMAT — five parts per stage:**

**PART 1 — BRIEFING ENVELOPE (Stage 2+ only)**

Before any review work, the incoming stage synthesizes what prior stages surfaced. This is not a
copy of prior findings — it is a distillation of what matters to *this stage's* lens.

```
### Briefing Envelope

PRIOR STAGE SUMMARY (from [prior stage name]):
KEY CONCERNS: [1-3 finding IDs and one-phrase summaries most relevant to this stage's lens.
Select based on your role's orientation — a TPM selects differently than a PM.]
OPEN QUESTION FORWARDED: [the specific concern the prior stage passed; verbatim from
the prior stage's HANDOFF PACKET "PASSING TO NEXT STAGE" line]
INERTIA STATUS: [Has any prior stage's finding changed the displacement picture from the
global anchor? YES — [how] / NO — anchor still holds]
```

For Stage 1: write `First stage — no briefing envelope.`

**PART 2 — STAGE IDENTITY**

```
## Stage: [stage-name]

ROLE: [name from .craft/roles/] — [orientation in one phrase]

INERTIA CHECK: [threatened / not at risk this stage] — [one sentence: how the global inertia
anchor looks from this role's perspective. What do they stand to lose or protect?]
```

**PART 3 — FINDINGS**

```
### Findings

F-01 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
F-02 [HIGH/MED/LOW] [specific concern from this role's lens] — Owner: [role] — Resolution: [concrete action]
[minimum 2; for Stage 2+ at least one finding must directly respond to the OPEN QUESTION
FORWARDED from the briefing envelope]

### Cross-Stage References

[prior stage] F-[N]: [confirm / escalate / contradict] — [one sentence]
[Stage 1: write "First stage — no cross-stage references."]
[Stage 2+: minimum 1 cross-stage reference required; reference must cite a specific F-ID]
```

**PART 4 — STAGE CLOSE**

```
### Verdict

VERDICT: APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED
Rationale: [one sentence citing a finding ID]

### Handoff Packet

PASSING TO NEXT STAGE: [the single most important open concern or question — specific]
BLOCKER: YES — [F-ID] — [what is blocked and which downstream stage is impacted] / NO
```

For the final stage (exec-office): write `PASSING TO ROB SPONSOR:` and still populate BLOCKER
with any unresolved concern from the full run.

---

**TPM STAGE — ADDITIONAL REQUIRED SECTIONS:**

After Findings (Part 3), before Close (Part 4):

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

**END-OF-RUN SUMMARY (--stage all only):**

```
## ROB Summary

INERTIA STATUS: [still threatened / partially resolved / not a blocker] — [one sentence]
BRIEFING CHAIN HEALTH: [Did each stage's briefing envelope synthesize or merely copy prior
findings? Were the KEY CONCERNS selections role-specific? Any break in the chain?
One sentence.]
BLOCKERS RAISED: [list stage + F-ID for any BLOCKER: YES entries — or "None"]
OPEN HANDOFFS: [any PASSING TO NEXT STAGE items not resolved by the final stage — or "None"]
```

**OUTPUT RULE:** Do not skip stages. Do not merge stages. Each stage section contains all five parts
in order (BRIEFING ENVELOPE for Stage 1 is always `First stage — no briefing envelope.`).
