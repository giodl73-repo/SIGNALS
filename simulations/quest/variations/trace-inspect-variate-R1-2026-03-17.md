---
skill: trace-inspect
topic: trace-inspect
item: variate
round: R1
date: 2026-03-17
---

# Quest Variate R1 -- trace-inspect

**Skill**: trace-inspect (trace-skill)
**Skill description**: Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had run. The hand-compiled artifact IS the expected output. It becomes the scenario baseline for quest-golden. A skill that cannot be hand-compiled cannot be implemented.

**Rubric**: `simulations/quest/rubrics/trace-inspect-rubric-2026-03-17.md`
**Round**: R1 -- first variation pass, single-axis first then combinations

---

## Variation Axes Selected

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role sequence | x -- Quality-first ordering | -- | -- | x -- EG-first ordering | -- |
| Output format | -- | -- | -- | x -- prose relays | -- |
| Lifecycle emphasis | -- | x -- compress Setup, expand Findings | -- | -- | x -- expand Findings |
| Phrasing register | -- | -- | x -- imperative/commands | -- | x -- imperative |
| Inertia framing | -- | -- | -- | -- | x -- named competitor |

**Single-axis**: V-01 (role sequence), V-02 (lifecycle emphasis), V-03 (phrasing register)
**Combined**: V-04 (role sequence + output format), V-05 (lifecycle emphasis + phrasing register + inertia framing)

---

## V-01 -- Role Sequence Axis

**Variation axis**: Role sequence -- Quality Observer runs first, then Implementation Analyst, then Spec Auditor.
**Hypothesis**: Starting with a quality/consistency lens before diving into spec gaps surfaces EG and QO findings that a spec-first reader would misclassify as SA. The quality pass establishes what the output looks like before the spec tells you what it should look like.

```
---
name: trace-skill
description: "Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had run."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Role execution order**: Quality Observer -> Implementation Analyst -> Spec Auditor
Rationale: Quality Observer runs first to observe what the output LOOKS like without spec priming.
Implementation Analyst runs second to trace execution gaps. Spec Auditor runs last to compare
against spec. This order surfaces EG and QO gaps before SA gaps frame the analysis.

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas before Stage 1. A phase using a label not declared here is in violation.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in each role relay; label lock for promoted gaps) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source coverage across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1**: Valid severity labels are P1, P2, P3. P1 blocks usefulness. P2 degrades quality. P3 is advisory.
**Schema 2**: Valid Source labels are SA (spec-layer gap), SG (setup gap), EG (execute gap), QO (quality observation).
Label lock invariant: a promoted SA gap uses SG in all downstream phases.
**Schema 3**: Valid Phase 4 remediation channels are spec / invocation / artifact / quality.
**Schema 4**: G-1 (>=2 distinct Source types in Step 3b), G-2 (no same-Source findings share identical Action),
G-3 (all Step 3b entries use only {P1,P2,P3}). A FAIL blocks advancement.
**Schema 5**: 3a -> 3b -> 3c -> 3d. Each sub-step requires its predecessor to have produced output.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| Quality Observer | Produces QO findings; EG findings use {P1,P2,P3} | May produce QO and EG; no SA production in this role | Runs first -- no spec priming |
| Implementation Analyst | Produces EG findings using {P1,P2,P3} | Produces EG; receives SG from Setup | Runs second -- observes execution |
| Spec Auditor | Produces SA and SG findings; Schema 1 applies to any EG produced | Produces SA, SG; label lock applies to any SA-to-SG promotion decisions | Runs last -- compares against spec |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Do not consult the test invocation here.
Audit across all three source layers: spec layer (SA), setup layer (SG), execute layer (EG).
A Stage 1 where gaps cluster at only one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record (all four fields required):

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`]. Carry all gaps forward without re-deriving or
silently resolving them.

---

#### SA-TO-SG PROMOTION

Every SA gap from Stage 1 is evaluated here. A gap a spec-competent invoker can supply at
runtime promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

After promotion:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock: a promoted gap using its SA label in any downstream phase is a structural violation.

---

#### Phase 1 -- Setup

Produce confirmed input bindings and per-role schema binding blocks.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: Quality Observer, Implementation Analyst, Spec Auditor (fixed order)]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: Quality Observer]  -- runs FIRST
  Schema 1 binding: EG findings use {P1,P2,P3}; QO findings are advisory
  Schema 2 binding: May produce QO and EG; no SA production
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]

[role: Implementation Analyst]  -- runs SECOND
  Schema 1 binding: EG findings use {P1,P2,P3}
  Schema 2 binding: Produces EG; receives SG from Setup carry-forward
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]

[role: Spec Auditor]  -- runs THIRD
  Schema 1 binding: SA/SG findings; any EG produced uses {P1,P2,P3}
  Schema 2 binding: Produces SA, SG; label lock for any promoted gaps
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`],
[roles: Quality Observer -> Implementation Analyst -> Spec Auditor],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Produce the hand-compiled artifact `{topic}-skill-trace-{date}.md` with every section the
artifact contract requires. Run roles in the declared order: Quality Observer first, then
Implementation Analyst, then Spec Auditor. A relay without the "Schema 2 compliance" field
is structurally invalid.

**Role relay -- Quality Observer** (runs first):
- Received from: Setup carry-forward
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact sections contributed -- quality and consistency observations]
- EG gaps encountered: [EG-NN list or "none"]

**Role relay -- Implementation Analyst** (runs second):
- Received from: Quality Observer relay
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact sections contributed -- execution tracing]
- EG gaps encountered: [EG-NN list or "none"]

**Role relay -- Spec Auditor** (runs third):
- Received from: Implementation Analyst relay
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact sections contributed -- spec compliance check]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Run sub-steps in Schema 5 order. Each sub-step states its prerequisite before beginning.

##### Step 3a -- Severity Legend Declaration
Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker for this trace] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

##### Step 3b -- Findings Table
Schema 5 prerequisite: Step 3a complete (legend defined above).

Findings merge across all three roles. Source labels from Schema 2 (promoted gaps use SG).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

##### Step 3c -- Enforcement Gates
Schema 5 prerequisite: Step 3b populated (>=2 entries).

**G-1**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL
- If FAIL: add a finding from the missing source layer. Re-check G-1.

**G-2**: No two same-Source findings carry identical Action text.
- Same-Source pairs examined: [list or "none"]
- G-2: PASS / FAIL

**G-3**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

Schema 5 transition condition: G-1=PASS, G-2=PASS, G-3=PASS. Step 3d is valid.

##### Step 3d -- Channel Taxonomy Activation
Schema 5 prerequisite: Step 3c all-PASS.

Valid Phase 4 Amend entries include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

Pre-check: G-1=PASS, G-2=PASS, G-3=PASS. If any=FAIL: return to Step 3c.

Change entry (all six fields):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO -- {{explain}}]

Dismissal entry (all four fields):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

One row per usage site. "Observed behavior: as expected" is structurally invalid; name specific
values, labels, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [actual legend stated at 3a] | PASS/FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only {P1,P2,P3} | [list severity values; counts; flags] | PASS/FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified against Schema 1 | [G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use {P1,P2,P3} | [severity values in Amend entries] | PASS/FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- Quality Observer | EG findings use {P1,P2,P3} | [severity labels from this role's EG findings] | PASS/FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- Implementation Analyst | EG findings use {P1,P2,P3} | [severity labels from this role's EG findings] | PASS/FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels in audit table | [all Source labels used; no others] | PASS/FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label | [SA gaps promoted; SG label confirmed downstream] | PASS/FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [Source labels in table; promoted gap labels] | PASS/FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- each role | Source labels from {SA,SG,EG,QO} | [labels per role; label lock confirmed] | PASS/FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry includes channel field | [channels used per entry; missing flags] | PASS/FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked with explicit PASS/FAIL | [G-1/G-2/G-3 results at Step 3c] | PASS/FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 entered only when all gates PASS | [invariant status at Phase 4 entry] | PASS/FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate G-1 cross-role | >=2 distinct Source types across all roles | [Source types and contributing roles] | PASS/FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | 3b valid only when 3a has produced legend | [what confirmed 3a complete] | PASS/FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | 3c valid only when 3b has >=2 entries | [entry count at 3c start] | PASS/FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | 3d valid only when all gates PASS | [gate results before 3d began] | PASS/FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 valid only when channel taxonomy active | [activation confirmation before Phase 4] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## V-02 -- Lifecycle Emphasis Axis

**Variation axis**: Lifecycle emphasis -- Phase 1 (Setup) compressed to a 6-line checklist; Phase 3 (Findings) expanded with explicit STOP banners and mandatory output counts per sub-step.
**Hypothesis**: Most structural failures in hand-compilation traces happen in Findings (skipped sub-steps, missing gates, silent gate passes). Compressing Setup to a checklist reduces noise. Expanding Findings with explicit STOP/GATE language and minimum output counts raises the structural floor without adding length elsewhere.

```
---
name: trace-skill
description: "Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had run."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 aggregate | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce) | N/A | VC-5 |

**Schema 1**: P1 = blocker. P2 = quality improvement. P3 = advisory. Only {P1,P2,P3} valid anywhere.
**Schema 2**: SA = spec gap. SG = setup gap. EG = execute gap. QO = quality observation. Label lock: promoted SA uses SG downstream.
**Schema 3**: Valid channels: spec / invocation / artifact / quality. Every Amend entry declares one.
**Schema 4**: G-1 (>=2 distinct Source types in 3b), G-2 (no duplicate Actions within same Source), G-3 (all 3b entries use {P1,P2,P3}). FAIL blocks advancement.
**Schema 5**: 3a -> 3b -> 3c -> 3d. Strict ordering. No sub-step begins without its predecessor's output.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable, or "N/A"] | [Source labels this role may produce; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Examine all three source layers. A Stage 1 where all gaps
cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Receives: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`], [diversity: `{{status}}`].
Carry all gaps forward without re-deriving or silently resolving them.

#### SA-TO-SG PROMOTION

Evaluate every SA gap. Invoker-supplable at runtime -> SG. Requires spec change -> SA.

```
SA-NN:
  Gap: [spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: {{n}}]
[SG from promotion: {{n}}]
[SG original: {{n}}]
```

---

#### Phase 1 -- Setup [COMPRESSED]

Checklist only. Fill all six lines. No elaboration needed.

```
topic:           [value]
scope_in:        [value]
scope_out:       [value]
roles:           [list from spec]
stack/detection: [value]
spec_version:    [value]
```

Per-role gap attribution (one block per role, abbreviated):
```
[role: {{name}}] SA/SG affecting: [list or none] | EG expected: [list or none]
```

**Setup carry-forward**: topic=`{{topic}}`, roles=`{{roles}}`, SA_remaining=`{{n}}`, SG_total=`{{n}}`.

---

#### Phase 2 -- Execute

Write the hand-compiled artifact `{topic}-skill-trace-{date}.md`. Every section the artifact
contract requires must appear. Run each role in sequence. Per-role relay required; Schema 2
compliance field is mandatory in every relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings [EXPANDED]

GATE: Phase 3 may not begin until Execute carry-forward has confirmed artifact path.
Sub-steps run in strict Schema 5 order. Each sub-step begins with an explicit prerequisite
check. Do not begin a sub-step without printing its prerequisite status.

---

##### >>>STOP: Step 3a gate<<<
**Prerequisite**: Schema 1 declared in Coverage Matrix. Confirmed: YES.
**Minimum output**: Severity legend with all three labels defined (P1, P2, P3). A legend
missing any label is structurally incomplete and blocks Step 3b.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what constitutes a blocker IN THIS TRACE -- name the specific failure mode] | Resolve before leaving Findings |
| P2 | [what constitutes a quality gap IN THIS TRACE -- name the specific pattern] | Address in Amend or follow-on |
| P3 | [what constitutes advisory IN THIS TRACE -- name the specific signal] | Log; no gate impact |

>>>Step 3a COMPLETE. Step 3b is valid to begin.<<<

---

##### >>>STOP: Step 3b gate<<<
**Prerequisite**: Step 3a complete -- severity legend defined above. Confirmed: YES.
**Minimum output**: Findings table with >=3 entries and >=2 distinct Source types. A table
with fewer than 3 entries, or with all entries from a single Source type, fails G-1.

Merge findings from all role relays and Stage 1 audit. Every Source label from Schema 2.
Every Severity label from the Step 3a legend. Promoted gaps use SG, not SA.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|
[minimum: 3 rows. minimum: 2 distinct Source values in the Source column.]

>>>Step 3b COMPLETE. Entry count: {{n}}. Source types: {{list}}. Step 3c is valid to begin.<<<

---

##### >>>STOP: Step 3c gate<<<
**Prerequisite**: Step 3b populated with >=2 entries. Confirmed: YES ({{n}} entries).
**Minimum output**: Explicit PASS or FAIL for G-1, G-2, and G-3. A gate recorded without
an explicit result (e.g., "probably passes") is structurally invalid. A FAIL blocks
Step 3d and Phase 4. The structural defect must be corrected and the gate re-checked.

**G-1** (>=2 distinct Source types in Step 3b):
- Source types present in Step 3b: [list every type and count]
- Distinct Source count: [n]
- G-1 result: **PASS** / **FAIL**
- If FAIL: identify the missing source layer. Return to Step 3b. Add a finding. Re-check G-1.

**G-2** (no two same-Source findings share identical Action text):
- Same-Source pairs examined: [list each pair and its Action text, or "no same-Source pairs"]
- G-2 result: **PASS** / **FAIL**
- If FAIL: revise Action text to name distinct targets. Re-check G-2.

**G-3** (all Step 3b entries use only {P1, P2, P3}):
- Severity labels present: [list every label and count]
- Labels outside {P1,P2,P3}: [list or "none"]
- G-3 result: **PASS** / **FAIL**
- If FAIL: relabel non-conforming entries. Re-check G-3.

>>>Step 3c COMPLETE. G-1={{result}}, G-2={{result}}, G-3={{result}}.
If all three PASS: Step 3d is valid to begin.
If any FAIL: Step 3d is BLOCKED. Do not proceed.<<<

---

##### >>>STOP: Step 3d gate<<<
**Prerequisite**: Step 3c all-PASS. G-1=PASS, G-2=PASS, G-3=PASS confirmed above.
**Output**: Schema 3 channel taxonomy activated for Phase 4.

Channel taxonomy active: spec / invocation / artifact / quality.
Every Phase 4 Amend entry must declare one channel from this set.
An Amend entry without a channel field is structurally incomplete.

>>>Step 3d COMPLETE. Channel taxonomy active. Phase 4 is valid to begin.<<<

**Findings carry-forward**: [highest: `{{F-NN}}`], [source: `{{source}}`],
[G-1:PASS, G-2:PASS, G-3:PASS], [channels: active].

---

#### Phase 4 -- Amend

>>>STOP: Phase 4 pre-check<<<
G-1=PASS, G-2=PASS, G-3=PASS -- all confirmed at Step 3c. Channel taxonomy active from Step 3d.
Phase 4 is valid to begin.

Change entry (all six fields required):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO -- {{explain}}]

Dismissal entry (all four fields required):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

One row per usage site declared in the Coverage Matrix. "Observed behavior: as expected" is
structurally invalid -- name the specific values, labels, roles, or invariant results observed.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend written | [exact legend text produced at 3a] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b | All entries {P1,P2,P3} | [severity values used; counts; any non-conforming] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result; labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use {P1,P2,P3} | [severity values in Amend entries] | PASS/FAIL |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use {P1,P2,P3} | [labels from this role's EG findings] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO in audit | [Source labels used; any outside schema] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG | [gaps promoted; SG label confirmed] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only {SA,SG,EG,QO}; promoted=SG | [Source labels in table; promoted gap labels] | PASS/FAIL |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels from schema; label lock | [labels per role; lock confirmed] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language used at 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [channels per entry; missing flags] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [G-1/G-2/G-3 results stated] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only with all-PASS | [invariant status at Phase 4 entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | >=2 Source types across roles | [Source types; contributing roles] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3b valid after 3a legend | [what confirmed 3a complete] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | 3c valid after >=2 findings | [entry count when 3c began] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | 3d valid after all-PASS | [gate results before 3d] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid after channel active | [activation confirmation] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [n] | **SG total**: [n] | **EG total**: [n]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## V-03 -- Phrasing Register Axis

**Variation axis**: Phrasing register -- all structural/conditional language ("A valid X produces Y. A trace that omits Z fails.") converted to imperative commands ("Write X. Include Y. Stop if Z is missing."). Present tense, second person, action verbs throughout.
**Hypothesis**: Direct commands reduce the cognitive gap between reading the instruction and performing the action. When the instruction says "write the legend" rather than "a valid Step 3a produces a legend", models are less likely to describe what a legend should contain and more likely to actually produce one.

```
---
name: trace-skill
description: "Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had run."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Step 0 -- Declare Your Schemas

Before writing anything else, declare the five trace schemas in this table. Do not begin Stage 1
until this table is filled.

| Schema | Labels | Used at | Role binding | Ledger check |
|--------|--------|---------|--------------|--------------|
| Schema 1 -- Severity | P1 / P2 / P3 | Step 3a (define), Step 3b (apply), Step 3c G-3 (verify), Phase 4 (apply) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type | SA / SG / EG / QO | Stage 1, SA-TO-SG PROMOTION, Step 3b, role relays | All roles | VC-2 |
| Schema 3 -- Channel | spec / invocation / artifact / quality | Step 3d (activate), Phase 4 (apply) | Phase 4 aggregate | VC-3 |
| Schema 4 -- Gates | G-1, G-2, G-3 | Step 3c (run), Phase 4 pre-check | G-1 cross-role | VC-4 |
| Schema 5 -- Ordering | 3a -> 3b -> 3c -> 3d | Phase 3 transitions | N/A | VC-5 |

Remember these rules:
- Use ONLY {P1, P2, P3} for severity. Never write "high", "medium", "low", or "critical".
- Use ONLY {SA, SG, EG, QO} for source labels. Never write "spec gap", "runtime error", or "design issue".
- When you promote an SA gap to SG, use the SG label in every phase that follows. Never use SA for that gap again.
- At Step 3c, write PASS or FAIL for each gate. Never write "likely passes" or leave a gate blank.
- Phase 4 does not begin until all three gates show PASS.

#### Declare Your Roles

List every role from the skill spec. For each role, write its schema bindings now.

| Role | Uses Schema 1? | Uses Schema 2? | Notes |
|------|---------------|---------------|-------|
| [role from spec] | [severity labels this role's EG findings use, or "N/A"] | [Source labels this role produces; label lock rule if promoted] | |

---

### Stage 1 -- Read the Spec and Find the Gaps

Read `{{skill_spec_path}}` now. Do not look at the test invocation yet.
Find gaps across all three source layers. Write them in this table.
If all your gaps are SA, look harder -- find at least one SG or EG gap before moving on.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Now write your relay:
```
[SA: list SA gap IDs, or "none"]
[SG: list SG gap IDs, or "none"]
[EG: list EG gap IDs, or "none"]
[layer diversity: PASS if >=2 distinct source types present, FAIL if not]
```

---

### Stage 2 -- Carry Gaps Forward and Compile

Take the relay from Stage 1. Do not re-derive or silently resolve any gap.

#### Promotion Decision

For every SA gap in your relay, decide: can a spec-competent invoker supply this at runtime?
If yes: promote to SG. If no: it stays SA.
Write one entry per SA gap:

```
SA-NN:
  Gap: [what the spec does not declare]
  Decision: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- why]
```

After all SA gaps are evaluated, write:
```
[SA remaining: n]
[SG from promotion: n]
[SG original: n]
```

Do not use the SA label for a promoted gap in any step that follows.

---

#### Phase 1 -- Bind Your Inputs (Setup)

Confirm every input from the invocation. Fill all six fields:

```
topic:           [fill from invocation]
scope_in:        [fill from invocation]
scope_out:       [fill from invocation]
roles:           [fill from spec -- list each role]
stack/detection: [fill from invocation or auto-detect]
spec_version:    [fill from spec]
```

For each role you just listed, write its gap attribution block:

```
[role: NAME]
  Schema 1 binding: [severity labels for this role's EG output, or "N/A"]
  Schema 2 binding: [Source labels this role produces; "SG label lock" if any promoted gaps bind here]
  SA/SG gaps binding this role: [list gap IDs, or "none -- verified"]
  EG gaps expected: [list gap IDs, or "none -- verified"]
```

Write your carry-forward line:
**Setup carry-forward**: topic=`{{topic}}`, roles=`{{list}}`, SA_remaining=`{{n}}`, SG_total=`{{n}}`.

---

#### Phase 2 -- Run Each Role and Write the Artifact

Write the artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md`.
Every section the artifact contract requires must appear in that file.

For each role, write a relay block now. Fill every field. Do not summarize with "role ran normally."

```
Role relay -- [ROLE NAME]
Received from: [name the prior role, or "Setup"]
Received values: [list name: value pairs]
Schema 2 compliance: Source labels used by this role: [list] -- all from {SA,SG,EG,QO}: YES or NO
SA/SG gaps binding this role: [list gap IDs, or "none -- verified"]
Produced: [describe the artifact content this role added -- be specific about sections]
EG gaps encountered: [list EG gap IDs, or "none"]
```

Write one relay block per role.
Then write: **Execute carry-forward**: artifact=`{{path}}`, EG_added=`{{list}}`.

---

#### Phase 3 -- Find, Gate, and Route

Do these four sub-steps in order. Check the prerequisite before starting each one.

---

**Sub-step 3a: Write your severity legend.**
Prerequisite: Schema 1 declared in Step 0. Check: YES.

Define P1, P2, and P3 for THIS trace -- not generic definitions, but what they mean for this
specific skill and invocation.

| Label | What it means in this trace | What to do about it |
|-------|----------------------------|---------------------|
| P1 | [name the specific failure mode that blocks usefulness here] | Fix before leaving Phase 3 |
| P2 | [name the quality gap pattern in this trace] | Address in Phase 4 or follow-on |
| P3 | [name the advisory signal type in this trace] | Log; no gate effect |

Done with 3a. Move to 3b now.

---

**Sub-step 3b: Build your findings table.**
Prerequisite: 3a complete -- legend written above. Check: YES.

Pull every gap from your role relays and Stage 1 audit. Write them here.
Use only Source labels from Schema 2. Use only Severity labels from your 3a legend.
If you promoted SA gaps, show them as SG here.
Write at least 3 rows. Make sure at least 2 distinct Source types appear in the Source column.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Done with 3b. Count your rows: {{n}}. Source types present: {{list}}. Move to 3c now.

---

**Sub-step 3c: Run the gates.**
Prerequisite: 3b populated with >=2 entries. Check: YES ({{n}} entries).

For each gate, write an explicit result: PASS or FAIL. Nothing else is valid here.

**G-1**: Count distinct Source types in your 3b table.
Source types: [list them]. Count: [n].
G-1 = **PASS** if count >= 2, **FAIL** if count < 2.
G-1 result: [write PASS or FAIL]
If FAIL: go back to 3b. Add a finding from the missing source layer. Return here and re-check.

**G-2**: Check every pair of findings that share a Source label. Do any share identical Action text?
Pairs examined: [list each same-Source pair and their Actions, or write "no same-Source pairs"]
G-2 result: [write PASS or FAIL]
If FAIL: go back to 3b. Revise the duplicate Action text. Return here and re-check.

**G-3**: List every Severity value in your 3b table.
Severity values used: [list them with counts]
Any value outside {P1, P2, P3}? [YES / NO]
G-3 result: [write PASS or FAIL]
If FAIL: go back to 3b. Relabel the non-conforming entries. Return here and re-check.

Done with 3c. Write your gate summary:
G-1={{result}}, G-2={{result}}, G-3={{result}}.
If all three = PASS: move to 3d. If any = FAIL: do not proceed past this point.

---

**Sub-step 3d: Activate the channel taxonomy.**
Prerequisite: G-1=PASS, G-2=PASS, G-3=PASS at 3c. Check: YES.

Write this sentence: "Channel taxonomy active: spec / invocation / artifact / quality.
Every Phase 4 entry must declare one channel from this set."

Done with 3d. Move to Phase 4 now.

**Findings carry-forward**: highest=`{{F-NN}}`, source=`{{source}}`, G-1=PASS, G-2=PASS,
G-3=PASS, channels=active.

---

#### Phase 4 -- Amend

Before writing any entry, confirm: G-1=PASS, G-2=PASS, G-3=PASS. Are they? [YES / NO]
If NO: do not write Phase 4 entries. Return to Step 3c.

For each finding you want to act on, write a change entry with all six fields:

```
Change:
  finding: [F-NN]
  source: [SA / SG / EG / QO] -- use SG for any promoted gap, not SA
  remediation channel: [spec / invocation / artifact / quality]
  section or field changed: [name it]
  change: [describe the change precisely]
  source confirmed: YES -- fix is at the [source] layer / NO -- [explain why not]
```

For each finding you want to dismiss, write a dismissal entry with all four fields:

```
Dismissal:
  finding: [F-NN]
  reason: [why this finding does not require a change]
  remediation channel: [spec / invocation / artifact / quality]
  source type confirmed: YES / NO
```

---

### Phase 5 -- Fill the Compliance Ledger and State Your Verdict

Fill every row. Write specific observed values in the "Observed behavior" column.
Do not write "as expected" -- name the actual value, label, count, or result you observed.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | Severity | Step 3a | P1/P2/P3 legend written | [paste your exact 3a legend entries] | PASS/FAIL |
| VC-1 | Severity | Step 3b | All entries use {P1,P2,P3} | [list: P1=n, P2=n, P3=n; flag any others] | PASS/FAIL |
| VC-1 | Severity | Step 3c G-3 | G-3 verified | [G-3 result; severity labels it checked] | PASS/FAIL |
| VC-1 | Severity | Phase 4 Amend | Amend entries use {P1,P2,P3} | [severity values in your Amend entries] | PASS/FAIL |
| VC-1 | Severity | Role relay -- [name] | EG findings use {P1,P2,P3} | [labels from this role's EG entries] | PASS/FAIL |
| VC-2 | Gap Type | Stage 1 | SA/SG/EG/QO in table | [list Source labels used; any outside schema] | PASS/FAIL |
| VC-2 | Gap Type | SA-TO-SG PROMOTION | Promoted gaps use SG | [which SA gaps promoted; confirm SG downstream] | PASS/FAIL |
| VC-2 | Gap Type | Step 3b Source | {SA,SG,EG,QO} only; SG for promoted | [Source labels in table; promoted gap labels] | PASS/FAIL |
| VC-2 | Gap Type | Role relay -- [name] | Source labels from schema | [labels per relay; lock confirmed] | PASS/FAIL |
| VC-3 | Channel | Step 3d | Taxonomy activated | [your activation sentence from 3d] | PASS/FAIL |
| VC-3 | Channel | Phase 4 Amend | Every entry has channel | [channels per entry; flag missing] | PASS/FAIL |
| VC-4 | Gates | Step 3c | G-1/G-2/G-3 explicit result | [G-1, G-2, G-3 results you wrote at 3c] | PASS/FAIL |
| VC-4 | Gates | Phase 4 pre-check | Phase 4 after all-PASS only | [gate status when you started Phase 4] | PASS/FAIL |
| VC-4 | Gates | G-1 cross-role | >=2 Source types across roles | [Source types; which roles contributed each] | PASS/FAIL |
| VC-5 | Ordering | 3a -> 3b | 3b after legend | [what confirmed 3a complete before 3b] | PASS/FAIL |
| VC-5 | Ordering | 3b -> 3c | 3c after >=2 findings | [entry count when 3c started] | PASS/FAIL |
| VC-5 | Ordering | 3c -> 3d | 3d after all-PASS | [gate results before 3d started] | PASS/FAIL |
| VC-5 | Ordering | 3d -> Phase 4 | Phase 4 after channel active | [activation confirmation before Phase 4] | PASS/FAIL |

Now compute your totals:
**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [n] | **SG total**: [n] | **EG total**: [n]

Now write your trace result. Choose exactly one:
- `NEEDS-SPEC-REVISION` -- if any P1 SA gap is still labeled SA after promotion
- `NEEDS-REDESIGN` -- if EG gaps exceed 3 and indicate a structural role gap
- `USEFUL` -- otherwise

**Trace result**: [write it here]
**Rationale**: [one sentence connecting the gap inventory to your choice]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## V-04 -- Role Sequence + Output Format Combination

**Variation axes**: (1) Role sequence -- EG-first ordering: execution-heavy roles run before spec-audit roles; (2) Output format -- role relays as numbered prose paragraphs instead of field-labeled blocks. Findings table remains structured.
**Hypothesis**: Execution-first role ordering naturally surfaces gaps from running the skill before the spec frames the analysis. Prose relays may capture richer contextual detail about WHY a gap manifests. The risk is that required relay fields (especially Schema 2 compliance) get buried in prose -- this is exactly what the rubric criterion C-07 tests.

```
---
name: trace-skill
description: "Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had run."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Role execution order**: EG-producing roles first (execution-heavy), SA-producing roles last.
Rationale: Run roles that observe execution behavior before spec-knowledge roles frame the analysis.
This surfaces EG gaps before SA classification primes the reader.

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 | Phase 4 aggregate | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 cross-role | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 | N/A | VC-5 |

**Schema 1**: P1=blocker, P2=quality gap, P3=advisory. Only {P1,P2,P3} valid anywhere.
**Schema 2**: SA=spec gap, SG=setup gap, EG=execute gap, QO=quality observation. Promoted SA uses SG label downstream.
**Schema 3**: Channels: spec/invocation/artifact/quality. Every Amend entry declares one.
**Schema 4**: G-1 (>=2 Source types in 3b), G-2 (no duplicate Actions per Source), G-3 (all {P1,P2,P3}). FAIL blocks.
**Schema 5**: 3a prerequisite unlocks 3b, 3b unlocks 3c, 3c all-PASS unlocks 3d, 3d unlocks Phase 4.

#### Role-Schema Binding Summary

Declare roles in EG-first order (execution-heavy roles before spec-audit roles):

| Role | EG-weight | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------|-----------------|-----------------|-------|
| [execution-heavy role] | HIGH | {P1,P2,P3} for EG | EG primary; may produce QO | Runs first |
| [balanced role] | MED | {P1,P2,P3} for EG | EG and SG | Runs second |
| [spec-audit role] | LOW | N/A or minimal EG | SA primary; SG from promotion | Runs last |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Audit all three source layers before concluding.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Receives relay from Stage 1. Carry all gaps without re-deriving.

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: n]  [SG from promotion: n]  [SG original: n]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ]
- [roles: list in EG-first execution order]
- [stack/detection: ] [spec_version: ]

Per-role schema binding (EG-first order):

```
[role: {{execution-heavy}}]  -- runs FIRST (EG-first)
  Schema 1: {P1,P2,P3} for EG findings
  Schema 2: EG primary producer; may emit QO
  SA/SG gaps binding: [list or none]
  EG gaps expected: [list or none]

[role: {{balanced}}]  -- runs SECOND
  Schema 1: {P1,P2,P3} for EG findings
  Schema 2: EG and SG producer
  SA/SG gaps binding: [list or none]
  EG gaps expected: [list or none]

[role: {{spec-audit}}]  -- runs LAST (SA-heavy)
  Schema 1: N/A or minimal EG
  Schema 2: SA primary; SG from promoted gaps
  SA/SG gaps binding: [list or none]
  EG gaps expected: [list or none]
```

**Setup carry-forward**: topic=`{{topic}}`, roles=`{{EG-first list}}`,
SA_remaining=`{{n}}`, SG_total=`{{n}}`.

---

#### Phase 2 -- Execute (Prose Relay Format)

Write the hand-compiled artifact `{topic}-skill-trace-{date}.md`. All artifact contract
sections required. Run roles in EG-first order.

Each relay is a numbered prose paragraph. Every relay paragraph MUST embed all required data
as explicit sentences. Required data: (1) received-from, (2) received values,
(3) Schema 2 compliance declaration, (4) SA/SG gaps affecting this role,
(5) what the role produced in the artifact, (6) EG gaps encountered.
A relay that omits any of these as an implicit assumption fails.

**Relay 1 -- [execution-heavy role name]** (runs first):

Write a prose paragraph of 4-8 sentences. The paragraph must contain as explicit sentences:
"Received from: [prior role or Setup]. Received values: [list]."
"Schema 2 compliance: Source labels used by this role were [list] -- all from {SA,SG,EG,QO}: YES/NO."
"SA/SG gaps affecting this role: [list or none confirmed]."
"This role produced the following artifact content: [describe sections added]."
"EG gaps encountered: [list or none]."

**Relay 2 -- [balanced role name]** (runs second):

[Same prose structure. Same required sentences embedded explicitly.]

**Relay 3 -- [spec-audit role name]** (runs last):

[Same prose structure. Same required sentences embedded explicitly.]

**Execute carry-forward**: artifact=`{{path}}`, EG_added=`{{list}}`.

---

#### Phase 3 -- Findings

Sub-steps in Schema 5 order. State prerequisite before beginning each sub-step.

##### Step 3a -- Severity Legend
Schema 5 prerequisite: Schema 1 declared in Coverage Matrix. Satisfied: YES.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker in this trace] | Resolve before leaving Findings |
| P2 | [quality gap in this trace] | Address in Amend |
| P3 | [advisory in this trace] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid.

##### Step 3b -- Findings Table
Schema 5 prerequisite: Step 3a complete. Satisfied: YES.

Merge findings across all three roles (in EG-first contribution order) and Stage 1.
Source labels from Schema 2. Promoted gaps show SG. Severity labels from 3a legend.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries with >=2 Source types. Step 3c valid.

##### Step 3c -- Enforcement Gates
Schema 5 prerequisite: Step 3b >=2 entries. Satisfied.

**G-1**: Source types present: [list]. Distinct count: [n]. G-1: **PASS / FAIL**
If FAIL: add missing source layer finding. Re-check G-1.

**G-2**: Same-Source Action pairs: [list or none]. G-2: **PASS / FAIL**
If FAIL: revise Action text. Re-check G-2.

**G-3**: Severity labels: [list with counts]. Any outside {P1,P2,P3}: [none / list]. G-3: **PASS / FAIL**
If FAIL: relabel. Re-check G-3.

Schema 5 transition condition: G-1=PASS, G-2=PASS, G-3=PASS -> Step 3d valid.

##### Step 3d -- Channel Taxonomy Activation
Schema 5 prerequisite: Step 3c all-PASS. Satisfied.

Channel taxonomy active: spec / invocation / artifact / quality.

Schema 5 transition: Phase 4 valid.

**Findings carry-forward**: highest=`{{F-NN}}`, G-1=PASS, G-2=PASS, G-3=PASS, channels=active.

---

#### Phase 4 -- Amend

Pre-check: G-1=PASS, G-2=PASS, G-3=PASS. Channel taxonomy active. Phase 4 valid.

Change entry:
- [finding: F-NN]
- [source: SA/SG/EG/QO -- SG for promoted]
- [remediation channel: spec/invocation/artifact/quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO -- explain]

Dismissal entry:
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec/invocation/artifact/quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

"Observed behavior" must name specific values. "As expected" is invalid.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | Severity | Step 3a | P1/P2/P3 legend | [exact legend from 3a] | PASS/FAIL |
| VC-1 | Severity | Step 3b | Only {P1,P2,P3} | [labels used; counts] | PASS/FAIL |
| VC-1 | Severity | Step 3c G-3 | G-3 verified | [G-3 result; labels checked] | PASS/FAIL |
| VC-1 | Severity | Phase 4 | Amend uses {P1,P2,P3} | [severity in Amend] | PASS/FAIL |
| VC-1 | Severity | Relay 1 -- [name] | EG findings {P1,P2,P3} | [severity labels from this relay's EG] | PASS/FAIL |
| VC-1 | Severity | Relay 2 -- [name] | EG findings {P1,P2,P3} | [severity labels from this relay's EG] | PASS/FAIL |
| VC-2 | Gap Type | Stage 1 | SA/SG/EG/QO | [labels used in Stage 1] | PASS/FAIL |
| VC-2 | Gap Type | SA-TO-SG PROMOTION | Promoted -> SG | [gaps promoted; SG confirmed] | PASS/FAIL |
| VC-2 | Gap Type | Step 3b | Only schema labels; SG for promoted | [labels in table] | PASS/FAIL |
| VC-2 | Gap Type | Each relay | Schema labels; label lock | [labels per relay paragraph] | PASS/FAIL |
| VC-3 | Channel | Step 3d | Taxonomy active | [language at 3d] | PASS/FAIL |
| VC-3 | Channel | Phase 4 | Every entry has channel | [channels per entry] | PASS/FAIL |
| VC-4 | Gates | Step 3c | G-1/G-2/G-3 explicit | [G-1/G-2/G-3 stated at 3c] | PASS/FAIL |
| VC-4 | Gates | Phase 4 pre-check | All-PASS before Phase 4 | [gate status at Phase 4 entry] | PASS/FAIL |
| VC-4 | Gates | G-1 cross-role | >=2 Source types aggregate | [types; contributing roles] | PASS/FAIL |
| VC-5 | Ordering | 3a -> 3b | 3b after legend | [3a completion evidence] | PASS/FAIL |
| VC-5 | Ordering | 3b -> 3c | 3c after >=2 entries | [entry count at 3c] | PASS/FAIL |
| VC-5 | Ordering | 3c -> 3d | 3d after all-PASS | [gates before 3d] | PASS/FAIL |
| VC-5 | Ordering | 3d -> Phase 4 | Phase 4 after activation | [activation before Phase 4] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [n] | **SG total**: [n] | **EG total**: [n]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## V-05 -- Lifecycle Emphasis + Phrasing Register + Inertia Framing (Full Combination)

**Variation axes**: (1) Lifecycle emphasis -- compressed Setup checklist, expanded Findings with STOP banners; (2) Phrasing register -- imperative commands throughout; (3) Inertia framing -- the skill opens by naming the status-quo competitor ("build first, trace never") and explaining what this trace prevents.
**Hypothesis**: Naming the inertia competitor (skipping the trace) at the start sets a motivational frame that makes every phase feel load-bearing. Combined with imperative language and expanded Findings gates, the model is most likely to treat each step as a commitment rather than a formatting exercise. This is the full-integration variation -- highest expected composite score if the hypotheses hold, highest expected variance if they conflict.

```
---
name: trace-skill
description: "Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle step by step -- producing the expected artifact as if the skill had run."
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
---
depth: standard

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Why This Trace Exists

The default move is to read the spec, believe it is correct, and start building. That approach
has a known cost: gaps in the spec are discovered during implementation, schema violations appear
at test time, and role boundaries only become clear after the first broken execution. By then the
artifact contract is already wrong and the test baseline does not exist.

This trace is the alternative. It hand-compiles the skill execution before a single line of
implementation is written. The hand-compiled output IS the expected artifact. The gaps discovered
here feed the spec before the spec becomes the implementation. A skill you cannot hand-compile
cannot be implemented without discovery cost -- and this trace surfaces that cost now.

The five schemas below govern every label, gate, and channel this trace will use. Lock them in
before writing anything else.

---

### Step 0 -- Lock In Your Schemas

Fill this table now. Do not begin Stage 1 without it.

| Schema | Valid labels | Used at | Governs | Ledger |
|--------|-------------|---------|---------|--------|
| Schema 1 -- Severity | P1 / P2 / P3 | 3a (define), 3b (apply), 3c G-3 (verify), Phase 4 (apply) | All EG findings everywhere | VC-1 |
| Schema 2 -- Gap Type | SA / SG / EG / QO | Stage 1, PROMOTION, 3b, relays | All Source labels everywhere | VC-2 |
| Schema 3 -- Channel | spec / invocation / artifact / quality | 3d (activate), Phase 4 (apply) | All Amend entries | VC-3 |
| Schema 4 -- Gates | G-1, G-2, G-3 | 3c (run), Phase 4 pre-check | Advancement gates | VC-4 |
| Schema 5 -- Ordering | 3a -> 3b -> 3c -> 3d | Phase 3 transitions | Sub-step sequence | VC-5 |

Hard rules -- commit to these now:
1. Every severity label is P1, P2, or P3. "High", "medium", "low", "critical" are not valid. Ever.
2. Every source label is SA, SG, EG, or QO. "Spec gap", "runtime error", "design issue" are not valid. Ever.
3. When you promote SA-NN to SG-NN, you must use the SG label for that gap in every subsequent phase. Using SA for a promoted gap is a structural violation that invalidates your trace.
4. At Step 3c, write the word PASS or the word FAIL for each gate. Nothing else counts.
5. Phase 4 does not begin until all three gates show PASS. This is not negotiable.

Now declare your roles and their schema bindings:

| Role | Schema 1 binding | Schema 2 binding |
|------|-----------------|-----------------|
| [role] | [severity labels applicable, or "N/A"] | [Source labels produced; label lock if promoted] |

---

### Stage 1 -- Find the Gaps

Read `{{skill_spec_path}}` now. Do not look at the invocation yet.
Look for gaps in all three source layers: spec layer (SA), setup layer (SG), execute layer (EG).
If you only find SA gaps, look harder -- find at least one gap at another layer before continuing.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Write your relay:
```
[SA: list]  [SG: list]  [EG: list]  [layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Carry Forward and Compile

Take the Stage 1 relay. Carry all gaps. Do not re-derive. Do not silently resolve.

#### Promotion Decision

For every SA gap: will a spec-competent invoker be able to supply this at runtime? YES -> promote to SG. NO -> stays SA.

```
SA-NN:
  Gap: [what the spec does not declare]
  Decision: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: n]  [SG from promotion: n]  [SG original: n]
```

Commit now: you will not use the SA label for any promoted gap from this point forward.

---

#### Phase 1 -- Bind Inputs [COMPACT]

Six lines. Fill them all:

```
topic:           [value]
scope_in:        [value]
scope_out:       [value]
roles:           [list]
stack/detection: [value]
spec_version:    [value]
```

One-line gap attribution per role:
```
[role: NAME] | Schema 1: [labels] | Schema 2: [labels] | SA/SG binding: [list or none] | EG expected: [list or none]
```

**Setup carry-forward**: topic=`{{topic}}`, roles=`{{list}}`, SA_remaining=`{{n}}`, SG_total=`{{n}}`.

---

#### Phase 2 -- Run Each Role and Produce the Artifact

Write the artifact now at `simulations/trace/skill/{topic}-skill-trace-{date}.md`.
Every section the artifact contract requires must appear. No partial artifacts.

For each role, write a relay block with all required fields.
Do not write "role ran normally." Fill every field explicitly.

```
Role relay -- [ROLE NAME]
Received from: [name]
Received values: [list]
Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
SA/SG gaps affecting this role: [list or "none -- verified"]
Produced: [specific artifact sections added]
EG gaps encountered: [list or "none"]
```

**Execute carry-forward**: artifact=`{{path}}`, EG_added=`{{list}}`.

---

#### Phase 3 -- Find, Gate, and Route [EXPANDED]

Each sub-step has a gate. Do not advance without passing the gate.

---

##### >>>GATE 3a: Write your severity legend now.<<<

Prerequisite: Schema 1 declared in Step 0. CHECK: YES.
Minimum required: definitions for P1, P2, and P3 for THIS specific trace.
If you write generic definitions ("P1 is a blocker"), revise them to name the specific
failure mode that constitutes a blocker in this trace -- the artifact contract, the schema
violation, the role boundary gap. Specificity here makes the findings table more actionable.

| Label | What it means in this trace | What to do |
|-------|----------------------------|-----------|
| P1 | [specific blocker pattern for this skill trace] | Fix before leaving Phase 3 |
| P2 | [specific quality gap pattern] | Amend or follow-on |
| P3 | [specific advisory signal] | Log only |

>>>3a DONE. Legend written. Step 3b may begin.<<<

---

##### >>>GATE 3b: Build your findings table now.<<<

Prerequisite: 3a complete. CHECK: YES.
Minimum required: at least 3 rows. At least 2 distinct Source types.
Pull every gap from your relays and Stage 1 audit. Promoted SA gaps show as SG here.
Every Source label from Schema 2. Every Severity label from your 3a legend.
If you reach this minimum, Step 3c may begin. If not, add findings until you do.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

>>>3b DONE. Row count: [n]. Source types: [list]. Step 3c may begin.<<<

---

##### >>>GATE 3c: Run the three gates now.<<<

Prerequisite: Step 3b has at least 2 entries. CHECK: YES ([n] entries).
Write PASS or FAIL. No other answer is valid. A FAIL blocks 3d and Phase 4.

**G-1** (>=2 distinct Source types in your 3b table):
Source types present: [list them]. Count: [n].
**G-1 = PASS / FAIL**
If FAIL: go to 3b. Add a finding from the missing layer. Come back and re-check G-1.

**G-2** (no two same-Source findings share identical Action text):
Pairs with same Source: [list each pair and its Actions, or "no pairs"].
**G-2 = PASS / FAIL**
If FAIL: go to 3b. Revise the duplicate Action. Come back and re-check G-2.

**G-3** (all 3b entries use only {P1, P2, P3}):
Labels used: [list with counts]. Any outside {P1,P2,P3}: [none / list].
**G-3 = PASS / FAIL**
If FAIL: go to 3b. Relabel. Come back and re-check G-3.

Gate summary: G-1=[PASS/FAIL], G-2=[PASS/FAIL], G-3=[PASS/FAIL]
>>>If all three PASS: 3c DONE. Step 3d may begin.
If any FAIL: STOP. Do not proceed to 3d. Fix and re-check.<<<

---

##### >>>GATE 3d: Activate the channel taxonomy.<<<

Prerequisite: G-1=PASS, G-2=PASS, G-3=PASS at 3c. CHECK: YES.
Write this activation sentence: "Channel taxonomy active: spec / invocation / artifact / quality.
Every Phase 4 Amend entry must declare one channel from this set."

>>>3d DONE. Channels active. Phase 4 may begin.<<<

**Findings carry-forward**: highest=`{{F-NN}}`, G-1=PASS, G-2=PASS, G-3=PASS, channels=active.

---

#### Phase 4 -- Amend

Before writing: confirm G-1=PASS, G-2=PASS, G-3=PASS and channels=active. Confirmed: YES.
Each entry covers one finding. Use change or dismissal format.

Change:
```
finding: [F-NN]
source: [label -- SG for promoted SA gaps]
remediation channel: [spec / invocation / artifact / quality]
section or field changed: [name it]
change: [describe precisely]
source confirmed: YES -- fix is at the [source] layer / NO -- [explain]
```

Dismissal:
```
finding: [F-NN]
reason: [why no change needed]
remediation channel: [spec / invocation / artifact / quality]
source type confirmed: YES / NO
```

---

### Phase 5 -- Compliance Ledger and Verdict

Fill every row. The "Observed" column names specific values. "As expected" is not valid.

| VC | Schema | Site | Expected | Observed | Result |
|----|--------|------|---------|---------|--------|
| VC-1 | Severity | Step 3a | Legend: P1/P2/P3 defined | [your exact 3a legend] | PASS/FAIL |
| VC-1 | Severity | Step 3b | All {P1,P2,P3} | [labels + counts in table] | PASS/FAIL |
| VC-1 | Severity | Step 3c G-3 | G-3 verified | [G-3 result; labels it checked] | PASS/FAIL |
| VC-1 | Severity | Phase 4 | Amend uses {P1,P2,P3} | [severity per Amend entry] | PASS/FAIL |
| VC-1 | Severity | Role relay -- [name] | EG findings {P1,P2,P3} | [labels from this role's EG] | PASS/FAIL |
| VC-2 | Gap Type | Stage 1 | SA/SG/EG/QO | [Source labels used; outside-schema count] | PASS/FAIL |
| VC-2 | Gap Type | Promotion | Promoted -> SG | [which gaps promoted; SG confirmed] | PASS/FAIL |
| VC-2 | Gap Type | Step 3b | Schema labels; SG for promoted | [labels; promoted gap labels] | PASS/FAIL |
| VC-2 | Gap Type | Role relay -- [name] | Labels from schema; lock honored | [labels per relay; lock] | PASS/FAIL |
| VC-3 | Channel | Step 3d | Taxonomy activated | [exact activation sentence] | PASS/FAIL |
| VC-3 | Channel | Phase 4 | Every entry has channel | [channels per entry; missing] | PASS/FAIL |
| VC-4 | Gates | Step 3c | G-1/G-2/G-3 explicit | [G-1, G-2, G-3 you wrote] | PASS/FAIL |
| VC-4 | Gates | Phase 4 pre-check | Phase 4 only after all-PASS | [gate status when Phase 4 started] | PASS/FAIL |
| VC-4 | Gates | G-1 cross-role | >=2 Source types | [types; contributing roles] | PASS/FAIL |
| VC-5 | Ordering | 3a -> 3b | 3b after legend | [what confirmed 3a done] | PASS/FAIL |
| VC-5 | Ordering | 3b -> 3c | 3c after >=2 entries | [entry count] | PASS/FAIL |
| VC-5 | Ordering | 3c -> 3d | 3d after all-PASS | [gates before 3d] | PASS/FAIL |
| VC-5 | Ordering | 3d -> Phase 4 | Phase 4 after activation | [activation before Phase 4] | PASS/FAIL |

**VC-1**: [PASS/FAIL] | **VC-2**: [PASS/FAIL] | **VC-3**: [PASS/FAIL]
**VC-4**: [PASS/FAIL] | **VC-5**: [PASS/FAIL]

**SA remaining**: [n] | **SG total**: [n] | **EG total**: [n]

Now choose one trace result. The result must match your gap inventory:
- `NEEDS-SPEC-REVISION`: any P1 SA gap remains SA after promotion -- the spec must change first
- `NEEDS-REDESIGN`: EG gaps exceed 3 and indicate a structural role gap -- redesign before implementation
- `USEFUL`: neither condition -- trace complete, artifact is the baseline

**Trace result**: [USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION]
**Rationale**: [one sentence connecting your gap counts and types to this result]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## Variation Summary

| ID | Axis/Axes | Key structural change | Rubric risk | Rubric reward |
|----|-----------|----------------------|-------------|---------------|
| V-01 | Role sequence | Fixed role order: QO first, IA second, SA last | C-07 if QO role missing Schema 2 field | C-08 more diverse Source types from QO pass |
| V-02 | Lifecycle emphasis | Setup compressed to checklist; Findings has STOP banners | C-01 if Setup checklist omits per-role blocks | C-04 gates nearly impossible to skip with banners |
| V-03 | Phrasing register | All instructions as imperative commands | C-09 if ledger feels like a command list | C-02 artifact written because commanded, not described |
| V-04 | Role sequence + Output format | EG-first roles; prose relay paragraphs | C-07 Schema 2 compliance buried in prose | C-08 richer EG finding descriptions |
| V-05 | Lifecycle + Register + Inertia | Inertia named; compressed Setup; imperative; expanded Findings gates | Verbose intro may reduce effective instruction space | C-04 C-05 highest gate and verdict compliance expected |
