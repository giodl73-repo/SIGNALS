---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 8
rubric: trace-inspect-rubric-v5-2026-03-17.md
---

# trace-inspect -- Variations R8 v5 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: Best R7 variation achieves C-01 through C-18 PASS under rubric v5. Rubric v5
adds three aspirational criteria from R7 excellence signals: C-19 (EG-producing roles declared
before SA-TO-SG PROMOTION as a structural ordering guarantee, not just a MUST rule), C-20 (an
explicit criterion inheritance registry names all prior-version criteria by ID and declares each
inherited -- silence does not imply continuity), C-21 (attribution table embedded as pre-printed
sub-structure of VC-4 G-1 row -- filling the ledger and attribution are a single operation).

**R7 baseline against v5** (C-19/C-20/C-21 projected):
- C-19: FAIL. Prior prompt declares EG-producing roles in the Role-Schema Binding Summary but does
  not sequence them into a named lifecycle event before SA-TO-SG PROMOTION. A model following the
  prompt can run roles in any order and still pass C-16 (execution evidence cited). Violation is
  possible because no structural guard prevents roles from running after promotion.
- C-20: FAIL. Prior prompt contains no inheritance registry. Criteria C-01 through C-18 are present
  in the prompt body but are not explicitly declared as inherited from prior versions. A future
  revision could silently drop a criterion with no structural element surfacing the omission.
- C-21: FAIL. Prior prompt has a standalone attribution table (which roles contributed which Source
  types) separate from the VC-4 compliance ledger row. The two can drift: a model filling the ledger
  may not fill the attribution, or vice versa.

Variation axes for R8:
- V-01: Single axis -- C-19 (EG Evidence Pass as named lifecycle event before SA-TO-SG PROMOTION)
- V-02: Single axis -- C-20 (Criterion Inheritance Registry block)
- V-03: Single axis -- C-21 (Attribution sub-table embedded in VC-4 G-1 ledger row)
- V-04: Combined -- C-19 + C-20
- V-05: Combined -- C-19 + C-20 + C-21

---

## V-01 -- Single axis: C-19 (EG Evidence Pass as structural lifecycle event)

**Variation axis**: Role sequence
**Hypothesis**: Declaring all EG-producing roles in a named "EG Evidence Pass" lifecycle event
that runs before SA-TO-SG PROMOTION makes EVIDENCE-GROUNDED state architectural. The promotion
evaluation cannot begin until every EG-producing role has completed its evidence pass. Violation
of C-16 (execution evidence cited before promotion) becomes structurally impossible because the
pass ordering is a declared contract, not a compliance instruction.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. Every label, channel, and gate used
in any downstream phase must be declared in this table.

| Schema | Declared Elements | Invariant |
|--------|-------------------|-----------|
| Schema 1 | Severity labels: {P1, P2, P3} | No other severity value anywhere in the trace |
| Schema 2 | Source labels: {SA, SG, EG, QO} | No other source value anywhere in the trace |
| Schema 3 | Lifecycle events: EG Evidence Pass, SA-TO-SG PROMOTION, Stage 1 relay, Stage 2 relay | Events occur in declared order; EG Evidence Pass precedes SA-TO-SG PROMOTION |
| Schema 4 | Enforcement gates: G-1, G-2, G-3 | All three checked at Step 3c; no gate skipped |
| Schema 5 | Phase 3 sub-steps: 3a -> 3b -> 3c -> 3d | Sub-steps run in declared order with transition confirmation |

**Schema 3 EG-first ordering invariant**: The EG Evidence Pass is a structural lifecycle event.
All roles declared with Schema 1 or Schema 2 binding that can produce EG findings MUST complete
their evidence pass before SA-TO-SG PROMOTION evaluates. A trace where SA-TO-SG PROMOTION begins
before any EG-producing role has run its evidence pass is a structural violation of Schema 3.

#### Role-Schema Binding Summary

Declare every role here before Stage 1. The EG-capable column identifies which roles must run
in the EG Evidence Pass (before SA-TO-SG PROMOTION).

| Role | Schema 1 binding | Schema 2 binding | EG-capable (must run in Evidence Pass) |
|------|-----------------|-----------------|----------------------------------------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO |

---

### Stage 1 -- Source-Layer Audit

Reads only `{{skill_spec_path}}`. Produces gap inventory across all three source layers using
only Schema 2 Source labels and Schema 1 Severity labels.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record:
```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### EG Evidence Pass (Schema 3 lifecycle event -- runs before SA-TO-SG PROMOTION)

**Schema 3 contract**: All roles marked EG-capable in the Role-Schema Binding Summary run here.
SA-TO-SG PROMOTION is structurally blocked until this pass completes.

For each EG-capable role, produce a brief evidence relay:

```
[EG Evidence Pass -- role: {{role_name}}]
  Schema 2 compliance: Source labels producible by this role: [list] -- all from {SA,SG,EG,QO}: YES
  EG gaps surfaced in this pass: [EG-NN list or "none -- confirmed"]
  Evidence state after pass: EVIDENCE-GROUNDED / EVIDENCE-ABSENT
```

**Evidence Pass carry-forward**:
```
[EG-capable roles completed: {{count}}]
[EG gaps from pass: {{eg_pass_list}}]
[Evidence pass state: COMPLETE -- SA-TO-SG PROMOTION may now begin]
```

A trace that proceeds to SA-TO-SG PROMOTION while "Evidence pass state" is not COMPLETE is
a structural violation of Schema 3.

---

### SA-TO-SG PROMOTION (Schema 3 lifecycle event)

**Schema 3 gate**: Evidence pass state must be COMPLETE before this event begins.

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

After promotion:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock: a promoted gap retaining its SA label downstream is a structural violation.

---

### Phase 1 -- Setup

Confirmed input bindings for all declared inputs. Per-role schema binding and gap attribution.

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  EG Evidence Pass completed: YES / NO (must be YES for EG-capable roles)
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

### Phase 2 -- Execute

Produces the hand-compiled artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md`.
Per-role relay for each role (EG-capable roles carry forward their Evidence Pass findings).

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- EG Evidence Pass findings carried forward: [EG-NN from pass, or "none"]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- New EG gaps encountered in Execute: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG total: `{{eg_total}}`].

---

### Phase 3 -- Findings

Sub-steps run in the order declared by Schema 5. Each prerequisite must be satisfied.

##### Step 3a -- Severity Legend

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

##### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries present. Step 3c valid to begin.

##### Step 3c -- Enforcement Gates

**G-1**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2**: No two findings sharing the same Source label carry identical Action text.
- Same-Source pairs examined: [list or "none"]
- G-2: PASS / FAIL

**G-3**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d valid.

##### Step 3d -- Channel Taxonomy Activation

Schema 3 channel taxonomy active. Every Phase 4 Amend entry requires:
`[remediation channel: spec / invocation / artifact / quality]`

Schema 5 transition: channel taxonomy active. Phase 4 valid to begin.

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active].

---

### Phase 4 -- Amend

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 | [actual definitions stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries {P1,P2,P3} | [severity values used; count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 | Amend entries {P1,P2,P3} | [severity values in Amend] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO used | [Source labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG | [SA gaps promoted; SG label confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | {SA,SG,EG,QO}; promoted = SG | [Source labels; promoted gap labels] | PASS / FAIL |
| VC-3 | Schema 3 | EG Evidence Pass | Pass completes before PROMOTION | [pass completion evidence] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel field in every entry | [channels used; any entry missing field] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked | [G-1/G-2/G-3 results recorded] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered with all-PASS | [invariant status at entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 (attribution) | >=2 distinct Source types; roles attributed | Role\|Source\|Count -- [fill for each role] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a legend complete before 3b | [confirmation 3a was complete] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | 3b has >=2 findings | [entry count at 3c start] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | 3c all-PASS | [gate results before 3d] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | 3d activated channel taxonomy | [activation confirmation] | PASS / FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: C-20 (Criterion Inheritance Registry)

**Variation axis**: Inertia framing
**Hypothesis**: An explicit CRITERION INHERITANCE REGISTRY at the top of the prompt names all
prior-version criteria by ID and declares each as inherited and unmodified. Silence no longer
implies continuity. When new criteria are added (C-19 through C-21), the prior criteria are
not silently present -- they are explicitly declared. A future version that drops C-06 must
update the registry row, making the omission structurally visible before any scoring occurs.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Criterion Inheritance Registry

This block declares the version inheritance chain for all active criteria. A criterion listed
as Inherited: YES is unconditionally active in this trace. A criterion not listed here does
not apply. Absence from this registry = inactive, not implicit.

| ID | Criterion (short) | Inherited | Source version | Status |
|----|-------------------|-----------|----------------|--------|
| C-01 | Phase completeness | YES | v1 | Active -- unchanged |
| C-02 | Artifact produced | YES | v1 | Active -- unchanged |
| C-03 | Schema 1 + Schema 2 compliance | YES | v1 | Active -- unchanged |
| C-04 | Enforcement gates checked | YES | v1 | Active -- unchanged |
| C-05 | Verdict present and classified | YES | v1 | Active -- unchanged |
| C-06 | SA-TO-SG promotion evaluated | YES | v1 | Active -- unchanged |
| C-07 | Per-role relays complete | YES | v1 | Active -- unchanged |
| C-08 | Findings table depth | YES | v1 | Active -- unchanged |
| C-09 | Compliance ledger populated | YES | v1 | Active -- unchanged |
| C-10 | Layer diversity in Stage 1 | YES | v1 | Active -- unchanged |
| C-11 | Schema 3 channel taxonomy activated | YES | v2 | Active -- unchanged |
| C-12 | Coverage Matrix BLOCKED gate | YES | v2 | Active -- unchanged |
| C-13 | Artifact delimiter pattern | YES | v2 | Active -- unchanged |
| C-14 | Phase Label Schema precedes trace | YES | v2 | Active -- unchanged |
| C-15 | Verdict as compliance ledger | YES | v3 | Active -- unchanged |
| C-16 | Bind status enum RESOLVED/UNRESOLVED/BLOCKED | YES | v3 | Active -- unchanged |
| C-17 | Precedence rule declared | YES | v4 | Active -- unchanged |
| C-18 | Binding column format constraint | YES | v4 | Active -- unchanged |
| C-19 | EG-first structural role ordering | NEW | v5 | Active -- new in this version |
| C-20 | Inertia registry with inheritance declaration | NEW | v5 | Active -- new in this version |
| C-21 | Attribution table co-located in compliance ledger | NEW | v5 | Active -- new in this version |

**Registry invariant**: A criterion with Inherited: YES and Status: Active applies to every trace
produced by this prompt. A trace omitting any Active criterion fails that criterion regardless of
other output quality. A future version of this prompt must update this table to reflect any removal
-- removing a criterion without updating this table is a structural registry violation.

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. Every label, channel, and gate used
in any downstream phase must be declared in this table.

| Schema | Declared Elements | Invariant |
|--------|-------------------|-----------|
| Schema 1 | Severity labels: {P1, P2, P3} | No other severity value anywhere in the trace |
| Schema 2 | Source labels: {SA, SG, EG, QO} | No other source value anywhere in the trace |
| Schema 3 | Lifecycle events: Stage 1 relay, SA-TO-SG PROMOTION, Stage 2 relay | Events occur in declared order |
| Schema 4 | Enforcement gates: G-1, G-2, G-3 | All three checked at Step 3c; no gate skipped |
| Schema 5 | Phase 3 sub-steps: 3a -> 3b -> 3c -> 3d | Sub-steps run in declared order with transition confirmation |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

Reads only `{{skill_spec_path}}`. Three source layers examined before declaring done.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record:
```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### SA-TO-SG PROMOTION (Schema 3 lifecycle event)

Every SA gap evaluated. One entry per SA gap:

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

After promotion:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant: promoted gap using SA label downstream = structural violation.

---

### Phase 1 -- Setup

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

### Phase 2 -- Execute

Produces artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md`.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

### Phase 3 -- Findings

##### Step 3a -- Severity Legend

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b valid.

##### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries. Step 3c valid.

##### Step 3c -- Enforcement Gates

**G-1**: >=2 distinct Source types in Step 3b.
- Source types present: [list] | G-1: PASS / FAIL

**G-2**: No two same-Source findings share identical Action text.
- G-2: PASS / FAIL

**G-3**: All entries use only {P1, P2, P3}.
- G-3: PASS / FAIL

Schema 5 transition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d valid.

##### Step 3d -- Channel Taxonomy Activation

Schema 3 active: `[remediation channel: spec / invocation / artifact / quality]` required in all
Phase 4 entries.

**Findings carry-forward**: [highest_finding], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel: active].

---

### Phase 4 -- Amend

Invariant status: G-1 PASS, G-2 PASS, G-3 PASS.

Amend change entry: [finding], [source], [remediation channel], [section changed], [change], [source confirmed].
Amend dismissal entry: [finding], [reason], [remediation channel], [source type confirmed].

---

### Verdict (Phase 5 -- Compliance Ledger)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend P1/P2/P3 declared | [actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries {P1,P2,P3} | [values used; count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result; labels] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 | Amend entries {P1,P2,P3} | [values in Amend] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | {SA,SG,EG,QO} | [labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted = SG label | [SA gaps promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | {SA,SG,EG,QO}; promoted = SG | [Source labels; promoted labels] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel field in every entry | [channels used] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked | [G-1/G-2/G-3 results] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Entered with all-PASS | [invariant status] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 | >=2 Source types attributed | [roles: which contributed which] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a complete | [3a completion confirmation] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | >=2 findings | [entry count] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | All-PASS gates | [gate results] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Channel activated | [activation confirmation] | PASS / FAIL |

**VC-1 through VC-5 overall**: PASS / FAIL per vector.

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: C-21 (Attribution sub-table co-located in VC-4 G-1 ledger row)

**Variation axis**: Output format
**Hypothesis**: Embedding the role-to-Source attribution table as a pre-printed sub-structure
inside the VC-4 G-1 ledger row makes filling the ledger and completing the attribution a single
operation. The two cannot drift: a model that fills the VC-4 row must fill the sub-table. The
sub-table is not a separate section to locate -- it is the required content of the VC-4 G-1
Observed behavior cell. Omitting the sub-table means the VC-4 G-1 row has no valid Observed
behavior, which fails C-09 independently.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Declared Elements | Invariant |
|--------|-------------------|-----------|
| Schema 1 | Severity labels: {P1, P2, P3} | No other severity value anywhere in the trace |
| Schema 2 | Source labels: {SA, SG, EG, QO} | No other source value anywhere in the trace |
| Schema 3 | Lifecycle events: Stage 1 relay, SA-TO-SG PROMOTION, Stage 2 relay | Events occur in declared order |
| Schema 4 | Enforcement gates: G-1, G-2, G-3 | All three checked at Step 3c; no gate skipped |
| Schema 5 | Phase 3 sub-steps: 3a -> 3b -> 3c -> 3d | Sub-steps run in declared order with transition confirmation |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | [interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay:
```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### SA-TO-SG PROMOTION

```
SA-NN: Gap / Promotion / Reason
[SA remaining: {{n}}] [SG from promotion: {{n}}] [SG original: {{n}}]
```

---

### Phase 1 -- Setup

Confirmed inputs: [topic], [scope_in], [scope_out], [roles], [stack/detection_method], [spec_version].

Per-role schema binding: [role], [Schema 1 binding], [Schema 2 binding], [gaps binding role], [EG gaps expected].

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

### Phase 2 -- Execute

Artifact: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

Per-role relay: Received from / Received values / Schema 2 compliance / SA-SG gaps / Produced / EG gaps.

**Execute carry-forward**: [artifact path], [EG added].

---

### Phase 3 -- Findings

**Step 3a**: Severity legend (P1/P2/P3 defined for this trace). -> Step 3b valid.

**Step 3b**: Findings table (>=2 entries, Source from {SA,SG,EG,QO}, Severity from {P1,P2,P3}).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

-> Step 3c valid.

**Step 3c**: G-1 (>=2 Source types), G-2 (no duplicate Action per Source), G-3 (only {P1,P2,P3}).
All three: PASS / FAIL. -> Step 3d valid when all PASS.

**Step 3d**: Channel taxonomy active. -> Phase 4 valid.

---

### Phase 4 -- Amend

[finding / source / channel / section / change / source-confirmed] per entry.

---

### Verdict (Phase 5 -- Compliance Ledger)

**VC-4 G-1 attribution format**: The Observed behavior cell for the VC-4 G-1 row MUST contain
the attribution sub-table below, filled completely. The VC-4 G-1 row is not valid without it.
Filling the ledger row and filling the attribution are the same operation.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend | [definitions stated at 3a] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All {P1,P2,P3} | [values used in 3b; count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 PASS | [G-3 result; labels verified] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 | Amend {P1,P2,P3} | [severity values in Phase 4] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | {SA,SG,EG,QO} | [Source labels used] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted = SG | [SA gaps promoted; SG label] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | {SA,SG,EG,QO}; SG for promoted | [labels; promoted confirmed] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel active | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in all entries | [channels; any missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked | [all three results stated] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | All-PASS at entry | [invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 (role attribution) | >=2 Source types; per-role attribution complete | **ATTRIBUTION SUB-TABLE (required -- fill or this row is invalid):** Role \| Source types contributed \| Finding IDs \| Count -- [one row per role that contributed to Step 3b; "none" is not valid if G-1 = PASS] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a complete | [3a completion] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | >=2 findings | [entry count] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | All gates PASS | [G results before 3d] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Channel activated | [activation before Phase 4] | PASS / FAIL |

**Note on VC-4 G-1 row**: The attribution sub-table in the Observed behavior cell must name each
role that contributed findings to Step 3b, the Source type(s) that role contributed, the Finding
IDs attributed to that role, and the count. This is the only location where attribution appears.
There is no separate attribution section. Do not write attribution anywhere else.

**VC-1 through VC-5 overall**: PASS / FAIL per vector.

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: C-19 + C-20 (EG Evidence Pass + Criterion Inheritance Registry)

**Variation axes**: Role sequence + Inertia framing
**Hypothesis**: Combining C-19 (structural EG-first ordering) and C-20 (inheritance registry)
addresses two distinct failure modes: roles running in wrong order (structural), and criteria
silently disappearing across versions (compositional). They operate in different parts of the
prompt (Schema 3 lifecycle declaration vs. preamble registry block) with no interaction risk.
V-04 tests whether both can coexist without the registry competing with the lifecycle structure
for attention.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Criterion Inheritance Registry

All active criteria for this trace declared below. Inherited: YES = active and unmodified.
New = added in this version. A criterion not listed here does not apply.

| ID | Criterion (short) | Inherited | Status |
|----|-------------------|-----------|--------|
| C-01 | Phase completeness | YES | Active |
| C-02 | Artifact produced | YES | Active |
| C-03 | Schema 1 + Schema 2 compliance | YES | Active |
| C-04 | Enforcement gates checked | YES | Active |
| C-05 | Verdict present and classified | YES | Active |
| C-06 | SA-TO-SG promotion evaluated | YES | Active |
| C-07 | Per-role relays complete | YES | Active |
| C-08 | Findings table depth | YES | Active |
| C-09 | Compliance ledger populated | YES | Active |
| C-10 | Layer diversity in Stage 1 | YES | Active |
| C-11 | Schema 3 channel taxonomy activated | YES | Active |
| C-12 | Coverage Matrix BLOCKED gate | YES | Active |
| C-13 | Artifact delimiter pattern | YES | Active |
| C-14 | Phase Label Schema precedes trace | YES | Active |
| C-15 | Verdict as compliance ledger | YES | Active |
| C-16 | Bind status enum RESOLVED/UNRESOLVED/BLOCKED | YES | Active |
| C-17 | Precedence rule declared | YES | Active |
| C-18 | Binding column format constraint | YES | Active |
| C-19 | EG-first structural role ordering | NEW | Active -- v5 |
| C-20 | Inertia registry with inheritance declaration | NEW | Active -- v5 |
| C-21 | Attribution co-located in VC-4 G-1 | NEW | Active -- v5 |

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Declared Elements | Invariant |
|--------|-------------------|-----------|
| Schema 1 | Severity labels: {P1, P2, P3} | No other severity value |
| Schema 2 | Source labels: {SA, SG, EG, QO} | No other source value |
| Schema 3 | Lifecycle events: **EG Evidence Pass**, SA-TO-SG PROMOTION, Stage 1 relay, Stage 2 relay | EG Evidence Pass precedes SA-TO-SG PROMOTION -- structural invariant |
| Schema 4 | Enforcement gates: G-1, G-2, G-3 | All three checked at Step 3c |
| Schema 5 | Phase 3 sub-steps: 3a -> 3b -> 3c -> 3d | Sub-steps in declared order |

**Schema 3 EG-first invariant**: EG Evidence Pass is a structural lifecycle event. All EG-capable
roles complete their pass before SA-TO-SG PROMOTION begins. Violation = structural Schema 3 defect.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-capable |
|------|-----------------|-----------------|------------|
| [role from spec] | [labels or "N/A"] | [Source labels; lock rules] | YES / NO |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay:
```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### EG Evidence Pass (Schema 3 lifecycle event -- before SA-TO-SG PROMOTION)

All EG-capable roles run here. SA-TO-SG PROMOTION is structurally blocked until pass completes.

```
[EG Evidence Pass -- role: {{role_name}}]
  EG gaps surfaced: [EG-NN list or "none -- confirmed"]
  Evidence state: EVIDENCE-GROUNDED / EVIDENCE-ABSENT
```

```
[Evidence pass state: COMPLETE -- SA-TO-SG PROMOTION may begin]
```

---

### SA-TO-SG PROMOTION (requires Evidence pass state = COMPLETE)

```
SA-NN: Gap / Promotion (PROMOTES TO SG-NN / REMAINS SA) / Reason
[SA remaining: {{n}}] [SG from promotion: {{n}}] [SG original: {{n}}]
```

Label lock: promoted gap retaining SA label downstream = structural violation.

---

### Phase 1 -- Setup

Confirmed inputs: [topic], [scope_in], [scope_out], [roles], [stack/detection_method], [spec_version].

Per-role binding:
```
[role: {{name}}]
  Schema 1 binding: [labels or N/A]
  Schema 2 binding: [Source labels; label lock]
  EG Evidence Pass completed: YES (EG-capable) / N/A (not EG-capable)
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

### Phase 2 -- Execute

Artifact: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

Per-role relay: Received from / Received values / Schema 2 compliance / EG pass findings carried /
SA-SG gaps / Produced / New EG gaps.

**Execute carry-forward**: [artifact path], [EG total].

---

### Phase 3 -- Findings

**3a** Severity legend (P1/P2/P3 defined). -> 3b valid.
**3b** Findings table (>=2 entries).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

-> 3c valid.
**3c** G-1 (>=2 Source types) / G-2 (no duplicate Action per Source) / G-3 ({P1,P2,P3}). All PASS -> 3d valid.
**3d** Channel taxonomy active: `[remediation channel: spec / invocation / artifact / quality]`. -> Phase 4 valid.

**Findings carry-forward**: [highest_finding], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel: active].

---

### Phase 4 -- Amend

Invariant status: G-1 PASS, G-2 PASS, G-3 PASS (required before first entry).

Change entry: [finding] / [source] / [channel] / [section changed] / [change] / [source confirmed].
Dismissal entry: [finding] / [reason] / [channel] / [source type confirmed].

---

### Verdict (Phase 5 -- Compliance Ledger)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend | [actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All {P1,P2,P3} | [values used; count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [result; labels] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 | {P1,P2,P3} in Amend | [values in Amend] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | {SA,SG,EG,QO} | [Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted = SG | [promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | {SA,SG,EG,QO}; promoted SG | [labels; promoted] | PASS / FAIL |
| VC-3 | Schema 3 | EG Evidence Pass | Pass before PROMOTION | [pass completion evidence; state = COMPLETE] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel active | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in all entries | [channels; missing?] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked | [all three results] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | All-PASS at entry | [invariant status] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 | >=2 Source types attributed | [roles: Source types; counts] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a complete | [3a completion] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | >=2 findings | [entry count] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | All-PASS | [gate results] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Channel activated | [activation] | PASS / FAIL |

**VC-1 through VC-5 overall**: PASS / FAIL per vector.

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined: C-19 + C-20 + C-21 (Full integration)

**Variation axes**: Role sequence + Inertia framing + Output format
**Hypothesis**: All three R7 excellence patterns applied together. C-19 (EG Evidence Pass as
structural lifecycle event) + C-20 (Criterion Inheritance Registry making prior criteria explicitly
declared) + C-21 (attribution sub-table embedded in VC-4 G-1 row, single operation). The three
axes operate in non-overlapping sections (Schema 3 lifecycle events, preamble registry, compliance
ledger VC-4 row) so there is no interaction risk. V-05 tests whether all three can coexist at
full strength without any one degrading the others.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Criterion Inheritance Registry

All active criteria declared. Inherited: YES = active and unmodified from prior version.
New = first active in this version. A criterion not listed here does not apply to this trace.

| ID | Criterion (short) | Inherited | Status |
|----|-------------------|-----------|--------|
| C-01 | Phase completeness | YES | Active |
| C-02 | Artifact produced | YES | Active |
| C-03 | Schema 1 + Schema 2 compliance | YES | Active |
| C-04 | Enforcement gates checked | YES | Active |
| C-05 | Verdict present and classified | YES | Active |
| C-06 | SA-TO-SG promotion evaluated | YES | Active |
| C-07 | Per-role relays complete | YES | Active |
| C-08 | Findings table depth | YES | Active |
| C-09 | Compliance ledger populated | YES | Active |
| C-10 | Layer diversity in Stage 1 | YES | Active |
| C-11 | Schema 3 channel taxonomy activated | YES | Active |
| C-12 | Coverage Matrix BLOCKED gate | YES | Active |
| C-13 | Artifact delimiter pattern | YES | Active |
| C-14 | Phase Label Schema precedes trace | YES | Active |
| C-15 | Verdict as compliance ledger | YES | Active |
| C-16 | Bind status enum | YES | Active |
| C-17 | Precedence rule declared | YES | Active |
| C-18 | Binding column format constraint | YES | Active |
| C-19 | EG-first structural role ordering | NEW | Active -- v5 (EG Evidence Pass named lifecycle event before SA-TO-SG PROMOTION) |
| C-20 | Inertia registry with inheritance declaration | NEW | Active -- v5 (this table) |
| C-21 | Attribution co-located in VC-4 G-1 | NEW | Active -- v5 (attribution sub-table in VC-4 G-1 Observed cell) |

**Registry invariant**: All rows with Status: Active apply unconditionally. Removing an Active
criterion requires updating this table. Silence = inactive, not inherited.

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Declared Elements | Invariant |
|--------|-------------------|-----------|
| Schema 1 | Severity labels: {P1, P2, P3} | No other severity value |
| Schema 2 | Source labels: {SA, SG, EG, QO} | No other source value |
| Schema 3 | Lifecycle events: **EG Evidence Pass** (C-19), SA-TO-SG PROMOTION, Stage 1 relay, Stage 2 relay | EG Evidence Pass precedes SA-TO-SG PROMOTION -- structural invariant; violation = Schema 3 defect |
| Schema 4 | Enforcement gates: G-1, G-2, G-3 | All three checked at Step 3c; no gate skipped |
| Schema 5 | Phase 3 sub-steps: 3a -> 3b -> 3c -> 3d | Declared order enforced; prerequisite confirmed per step |

**Schema 3 EG-first invariant (C-19)**: EG-producing roles complete their evidence pass before
SA-TO-SG PROMOTION. The pass is a named lifecycle event, not a recommendation. A trace where
promotion begins while any EG-capable role has not completed its pass is a structural Schema 3
violation regardless of whether C-16 is otherwise satisfied.

#### Role-Schema Binding Summary

One row per role. EG-capable column determines Evidence Pass obligation.

| Role | Schema 1 binding | Schema 2 binding | EG-capable (Evidence Pass required) |
|------|-----------------|-----------------|--------------------------------------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock] | YES / NO |

---

### Stage 1 -- Source-Layer Audit

Reads only `{{skill_spec_path}}`. All three source layers examined before done.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay:
```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### EG Evidence Pass (C-19 -- Schema 3 structural lifecycle event)

**Structural gate**: SA-TO-SG PROMOTION is blocked until "Evidence pass state: COMPLETE."

For each role with EG-capable: YES:

```
[EG Evidence Pass -- role: {{role_name}}]
  Schema 2 compliance: Source labels producible: [list] -- {SA,SG,EG,QO}: YES
  EG gaps surfaced in this pass: [EG-NN: description; or "none -- confirmed"]
  Evidence state: EVIDENCE-GROUNDED / EVIDENCE-ABSENT
```

```
[EG-capable roles completed: {{count}} of {{total}}]
[EG gaps from pass: {{eg_pass_list}}]
[Evidence pass state: COMPLETE -- SA-TO-SG PROMOTION valid to begin]
```

A trace that proceeds to SA-TO-SG PROMOTION with "Evidence pass state" not COMPLETE is a
structural Schema 3 violation. Correct by completing all EG Evidence Pass entries first.

---

### SA-TO-SG PROMOTION (Schema 3 lifecycle event -- requires Evidence pass state = COMPLETE)

Every SA gap from Stage 1 evaluated. Promotion decision made with full EG inventory available.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

After promotion:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant: promoted gap retaining SA label in any downstream phase = structural violation.

---

### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution. One block per role. "none -- confirmed" valid only
after explicit verification, not assumption.

```
[role: {{role_name}}]
  Schema 1 binding: [applicable severity labels, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  EG Evidence Pass completed: YES (EG-capable) / N/A (not EG-capable)
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

### Phase 2 -- Execute

A valid Execute produces the hand-compiled artifact and a per-role relay for each role.
EG-capable roles carry forward their Evidence Pass findings -- they do not re-derive them.

**[ARTIFACT BEGINS HERE]**

*(artifact content here -- every section the artifact contract requires)*

**[ARTIFACT ENDS HERE]**

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- EG Evidence Pass findings carried forward: [EG-NN from pass, or "none"]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact section content added]
- New EG gaps encountered in Execute (beyond pass): [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG total: `{{eg_total}}`].

---

### Phase 3 -- Findings

Sub-steps in Schema 5 declared order. Each prerequisite stated before sub-step begins.

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix. (satisfied above)

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend above).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries in table above. Step 3c valid to begin.

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b has >=2 entries.

**G-1** (Schema 4): Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL (if FAIL: identify missing layer, add finding, re-check)

**G-2** (Schema 4): No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none -- all Source types appear once"]
- G-2: PASS / FAIL (if FAIL: revise Action to distinct targets, re-check)

**G-3** (Schema 4): All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL (if FAIL: relabel non-conforming entries, re-check)

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d valid to begin.

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

Schema 5 prerequisite: Step 3c G-1 = PASS, G-2 = PASS, G-3 = PASS.

Schema 3 channel taxonomy active. Every Phase 4 Amend entry must include:
`[remediation channel: spec / invocation / artifact / quality]`
An Amend entry without this field is structurally incomplete.

Schema 5 transition: channel taxonomy active. Phase 4 valid to begin.

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

### Phase 4 -- Amend

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 violated. Phase 4 structurally blocked. Return to Step 3c.

Amend entry (change) -- all six fields required:
- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock invariant; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

Amend entry (dismissal) -- all four fields required:
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

Produced after Phase 4 completes. Observed behavior cell must name specific values, labels,
role names, or invariant results -- "as expected" is structurally invalid in any Observed cell.

**Note on VC-4 G-1 row (C-21)**: The Observed behavior cell for the VC-4 G-1 row contains the
role attribution sub-table. This is the only location where attribution appears -- there is no
separate attribution section. Filling the VC-4 G-1 ledger row and completing the attribution
are a single operation. The VC-4 G-1 row is invalid without a filled sub-table.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions written | [state actual P1/P2/P3 definitions from Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use only {P1, P2, P3} | [list severity values used in 3b; count of each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result; labels checked; confirm PASS] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use only {P1,P2,P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay (EG-producing roles) | EG findings from role use only {P1,P2,P3} | [list severity labels per EG-producing role; schema binding honored] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used | [list Source labels in Stage 1; confirm no out-of-schema] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; label lock holds | [list SA gaps promoted; each uses SG downstream] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | {SA,SG,EG,QO}; promoted = SG not SA | [Source labels in 3b; promoted gap labels] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay (all roles) | Source labels from {SA,SG,EG,QO}; lock honored | [labels per role; any promoted gap confirmed SG] | PASS / FAIL |
| VC-3 | Schema 3 | EG Evidence Pass (C-19) | Pass completes before PROMOTION; state = COMPLETE | [EG-capable role count; pass state at PROMOTION entry] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language stated at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels used per entry; any missing flagged] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked with explicit PASS/FAIL | [G-1/G-2/G-3 results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only when all-PASS | [invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 (C-21 attribution sub-table) | >=2 distinct Source types; per-role attribution complete | **Fill sub-table (required -- this cell is invalid without it):** \| Role \| Source types contributed \| Finding IDs \| Count \| (one row per role contributing to Step 3b; "none" invalid when G-1 = PASS) | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3b begins only after 3a legend complete | [what confirmed 3a complete before 3b] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | 3c begins only after >=2 findings | [entry count in 3b when 3c started] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | 3d begins only after all-PASS gates | [gate results present before 3d began] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 begins only after channel activated | [channel activation confirmation before Phase 4] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
