---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 8
rubric: trace-skill-rubric-v8-2026-03-15.md
---

# trace-skill -- Variations R8 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

Round 8 target: C-27, C-28, C-29, C-30 -- the four new v8 aspirational criteria. No R7 variation
reaches 100 under v8 because no single-axis variation satisfies all four new criteria and no R7
combined variation integrates all three axes together.

R7 scores under v8:
- V-01 (99.17): C-27 PASS, C-28 PASS, C-29 FAIL (prose Verdict, not ledger), C-30 FAIL (imperative)
- V-02 (98.75): C-27 FAIL, C-28 FAIL (no role-binding), C-29 PASS, C-30 FAIL
- V-03 (98.75): C-27 FAIL, C-28 FAIL, C-29 FAIL, C-30 PASS

The R8 ceiling requires a variation that inherits all 24 v8 criteria and integrates:
- V-01's role-indexed Coverage Matrix (C-27) and per-role Verdict rows (C-28)
- V-02's compliance ledger format with pre-filled Expected behavior (C-29)
- V-03's assertion-first invariant style where FAIL = structural invalidity (C-30)

V-04 combines C-27 + C-28 + C-29 (role-binding + compliance ledger with per-role adherence rows).
V-05 adds C-30 on top (the R8 ceiling: all four new criteria together).

Single-axis selections: Role sequence (V-01), Output format (V-02), Phrasing register (V-03).
Combined: Role sequence + Output format (V-04), all three axes (V-05).

All five R8 variations inherit the full V-04 R6 architecture:
- Coverage Matrix with 5 schemas (Declared-at, Referenced-by, Verdict-check)
- Schema 5 (Sub-Step Ordering) with Prerequisite and Unblocks columns
- Hard-stop BLOCKED language on gate FAIL
- VC-1 through VC-5 verifying per-usage-site adherence
- All schemas declared before Stage 1

---

## V-01 -- Single axis: Role sequence (role-schema binding column + Role-Schema Binding Summary)

**Axis**: Role sequence -- the Coverage Matrix gains a fifth column, "Role-binding," that names
every role in the skill spec that each schema governs. Before Stage 2, a Role-Schema Binding
Summary table maps each role to its schema obligations. In Phase 1 Setup, each role entry
declares its schema bindings alongside gap attribution. In Phase 2 Execute, every role relay
includes a "Schema 2 compliance" field listing the Source labels used. The Verdict's VC-1 and
VC-2 each include per-role adherence checks naming each role and the observed behavior at that
role's usage site.

**Hypothesis**: V-04 R6 maps schemas to phases and Verdict checks via the Referenced-by and
Verdict-check columns, but role-level obligations remain implicit. A tracer who faithfully follows
the phase structure might still violate Schema 2 label lock in a role relay without the Coverage
Matrix flagging it. The Role-binding column makes schema obligations role-specific and auditable
at role granularity. C-27 is satisfied by the Role-binding column and the Role-Schema Binding
Summary. C-28 is satisfied because VC-1 and VC-2 check "Schema honored in relay for [role X]"
as a specific usage site, not just phase-level presence. C-29 and C-30 are not targeted by this
axis -- the Verdict remains prose blocks and the register uses imperative language.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the phases
that require it, the roles bound by it, and the Verdict check that audits it. All phases reference
only the labels declared here.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings (severity label applies to every EG entry) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in role relay uses only SA/SG/EG/QO; promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments drawn from all roles' findings | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 checks Source column coverage across all roles' findings aggregated in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between all sub-steps) | N/A -- applies to Findings phase structure, not individual roles | VC-5 |

#### Severity Vocabulary (Schema 1)

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through phases with SG label |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable, not structural | Surface anywhere; P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

| Channel | Targets | Activated-at |
|---------|---------|-------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

Read the skill spec and declare each role in the execution sequence. For each role, record which
schemas govern its behavior. Fill this table before Stage 2 begins. A role without explicit schema
binding is invalid. One row per role found in the spec.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's findings] | [Source labels this role may produce; label lock rules] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using Schema 2
(Gap Type Taxonomy) and Schema 1 (Severity Vocabulary).

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without
content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types (Schema 2). Examine harder if gaps
cluster at one layer.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

At the Setup boundary. For every SA gap in the relay, evaluate:

> Can the invoker supply this value at runtime even though the spec doesn't declare it?

```
SA-NN -> [result]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock: promoted gaps use SG label in all downstream phases.

---

#### Phase 1 -- Setup

Confirm each input with `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role schema binding and gap attribution**: For each role in `[roles: ...]`, declare its
schema obligations from the Role-Schema Binding Summary, then enumerate its gaps. A role entry
without schema binding declaration is invalid. "none -- confirmed" only after verifying.

```
[role: {{role_name}}]
  Schema 1 binding: [which severity labels apply to this role's findings]
  Schema 2 binding: [which Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must appear.

For each role, open its relay before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

The "Schema 2 compliance" field is required. A role relay without it is structurally invalid.
Do not infer silently.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], all gaps from Stages 1 and 2.

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step prints its Schema 5
Prerequisite and Unblocks values before beginning.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 prerequisite**: Schema 1 (Severity Vocabulary) declared in Coverage Matrix.
**Schema 5 output**: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b -- Findings Table

**Schema 5 prerequisite**: Step 3a complete (severity legend written above).
**Schema 5 output**: findings table with >=2 entries (unblocks Step 3c).

Merge all gaps from Stage 1 and Stage 2. Use promoted Source labels (Schema 2). Use only
P1/P2/P3 (Step 3a legend):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

---

##### Step 3c -- Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated (>=2 entries).
**Schema 5 output**: gate results (all must be PASS to unblock Step 3d).

Run all three gates from Schema 4. Record PASS or FAIL explicitly.

**Hard-stop rule (Schema 4 hard-stop conditions)**: a FAIL on any gate BLOCKS Step 3d and
Phase 4. Resolve the failing condition, re-run the gate, confirm PASS before proceeding.

**G-1 Source Diversity Gate** (Schema 4)
- Property: >=2 distinct Source types present in Step 3b
- Source types present: [list all Source values from table]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active for Step 3d and Phase 4. Add finding from missing
  source layer. Re-run G-1. Do not proceed until PASS.

**G-2 Action Diversity Gate** (Schema 4)
- Property: no two same-Source findings carry identical Action text
- Same-Source pairs reviewed: [list pairs with Action fields, or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Revise duplicate Actions. Re-run G-2.

**G-3 Severity Completeness Gate** (Schema 4)
- Property: all Step 3b entries use only P1/P2/P3 (Schema 1; Step 3a legend)
- Severity labels in Step 3b: [list all values used]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Relabel non-conforming entries. Re-run G-3.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

**Schema 5 prerequisite**: Step 3c all gates PASS.
**Schema 5 output**: Schema 3 channel taxonomy activated for Phase 4 (unblocks Phase 4).

Activate: spec / invocation / artifact / quality (from Schema 3).

Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check** (hard-stop conditions): G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
All must be PASS. If any = FAIL: Schema 4 hard-stop active. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d (Schema 3): spec / invocation / artifact / quality.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Coverage Matrix Audit with Role-Level Adherence)

Walk the Coverage Matrix row by row. For each schema, verify the Declared-at, Referenced-by,
Role-binding, and Verdict-check columns were honored. VC-1 and VC-2 include a per-role adherence
check naming each role and the observed behavior at that role's usage site.

**VC-1 -- Severity Vocabulary (Schema 1)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- Referenced in Step 3a: YES / NO -- evidence: [what the legend produced]
- Referenced in Step 3b (only P1/P2/P3 used): YES / NO -- labels used: [list]
- Referenced in Step 3c G-3 (severity completeness verified): YES / NO
- Role-binding honored: for each role that produced EG findings, list role and severity labels
  used: [per-role list, e.g., "Role A: P1, P2 -- Schema 1 compliant; Role B: P2 -- compliant"]
- Labels outside P1/P2/P3 found anywhere: [list or "none"]
- VC-1 result: PASS / FAIL

**VC-2 -- Gap Type Taxonomy (Schema 2)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- SA-TO-SG PROMOTION ran: YES / NO -- evidence: [which SA gaps were evaluated]
- SA labels appearing after promotion for promoted gaps: [list or "none"]
- Step 3b Source column uses only SA/SG/EG/QO: YES / NO
- Role-binding honored: for each role relay in Phase 2, list role and Source labels used:
  [per-role list, e.g., "Role A relay: EG -- Schema 2 compliant; Role B relay: SG, EG -- compliant"]
- VC-2 result: PASS / FAIL

**VC-3 -- Remediation Channel Taxonomy (Schema 3)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- Activated at Step 3d: YES / NO -- evidence: [activation language used]
- All Phase 4 Amend entries include channel field: YES / NO
- Channels used in Phase 4: [list]
- Channels outside spec/invocation/artifact/quality: [list or "none"]
- VC-3 result: PASS / FAIL

**VC-4 -- Enforcement Gate Registry (Schema 4)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
- Phase 4 entered while any gate = FAIL: YES (hard-stop violated) / NO (clean)
- Role-binding honored: G-1 checks Source column across all roles' findings aggregated in
  Step 3b: YES / NO -- evidence: [Source types present and which roles contributed them]
- VC-4 result: PASS / FAIL

**VC-5 -- Sub-Step Ordering (Schema 5)**:
- Step 3a ran before Step 3b: YES / NO
- Step 3b populated before Step 3c ran: YES / NO
- Step 3c all-PASS before Step 3d activated: YES / NO
- Step 3d activated before Phase 4 began: YES / NO
- VC-5 result: PASS (all YES) / FAIL (any NO)

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Output format (per-usage-site compliance ledger in Verdict)

**Axis**: Output format -- the Verdict (Phase 5) is a compliance ledger table instead of
per-schema prose blocks. The table has columns: VC | Schema | Usage site | Expected behavior |
Observed behavior | Site result. Each row is one declared usage site from the Coverage Matrix
Referenced-by column. A schema referenced at three sites produces three rows. The "Observed
behavior" cell must state what was actually found at that specific site -- not a schema-level
summary. The Coverage Matrix (identical to V-04 R6) declares the sites; the ledger table
holds each site accountable. "Expected behavior" is pre-filled in the prompt; the tracer must
supply "Observed behavior" with specific evidence, making "as expected" physically invalid.

**Hypothesis**: V-04 R6's Verdict walks each schema as a prose block with fill-in fields. A
tracer writing "Labels used: P1, P2" satisfies the form without documenting WHERE in Phase 2
Execute P1/P2 were produced. The ledger forces a row per usage site, making per-site adherence
structural: "Observed behavior at Step 3b: all 4 entries use P1 or P2 -- no outliers" is more
evidenced than "labels used: P1, P2." The pre-filled Expected behavior cell forces the tracer
to state something distinct from the expectation, not restate it. C-29 is satisfied by the
ledger format with pre-filled Expected behavior. C-27/C-28 are not targeted (no role-binding
column; no per-role rows); C-30 is not targeted (imperative phrasing retained).

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it and the Verdict check that audits it. All phases reference only the
labels declared here.

| Schema | Content | Declared-at | Referenced-by | Verdict-check |
|--------|---------|-------------|---------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | VC-5 |

#### Severity Vocabulary (Schema 1)

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through phases with SG label |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable, not structural | Surface anywhere; P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

| Channel | Targets | Activated-at |
|---------|---------|-------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using
Schema 2 (Gap Type Taxonomy) and Schema 1 (Severity Vocabulary).

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types. Examine harder if gaps cluster
at one layer.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

At the Setup boundary. For every SA gap in the relay:

```
SA-NN -> [result]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock: promoted gaps use SG label in all downstream phases.

---

#### Phase 1 -- Setup

Confirm each input with `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role gap attribution** (role -> gaps): For each role, enumerate constraining gaps:

```
[role: {{role_name}}]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must appear.

Per-role relay before each artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Do not infer silently.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], all gaps from Stages 1 and 2.

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step prints its Schema 5
Prerequisite and Unblocks values before beginning.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 prerequisite**: Schema 1 (Severity Vocabulary) declared in Coverage Matrix.
**Schema 5 output**: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b -- Findings Table

**Schema 5 prerequisite**: Step 3a complete (severity legend written above).
**Schema 5 output**: findings table with >=2 entries (unblocks Step 3c).

Merge all gaps. Use promoted Source labels (Schema 2). Use only P1/P2/P3 (Step 3a):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

---

##### Step 3c -- Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated (>=2 entries).
**Schema 5 output**: gate results (all must be PASS to unblock Step 3d).

**Hard-stop rule (Schema 4)**: a FAIL on any gate BLOCKS Step 3d and Phase 4.
Resolve the failing condition, re-run the gate, confirm PASS before proceeding.

**G-1 Source Diversity Gate** (Schema 4)
- Source types present in Step 3b: [list]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Add missing-layer finding. Re-run G-1.

**G-2 Action Diversity Gate** (Schema 4)
- Same-Source pairs reviewed: [list or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Revise duplicate Actions. Re-run G-2.

**G-3 Severity Completeness Gate** (Schema 4)
- Severity labels in Step 3b: [list]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Relabel non-conforming entries. Re-run G-3.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

**Schema 5 prerequisite**: Step 3c all gates PASS.
**Schema 5 output**: Schema 3 channel taxonomy activated for Phase 4 (unblocks Phase 4).

Activate: spec / invocation / artifact / quality (Schema 3).

Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
All must be PASS. If any = FAIL: Schema 4 hard-stop active. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d (Schema 3): spec / invocation / artifact / quality.

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

Fill the compliance ledger completely. One row per usage site declared in the Coverage Matrix
Referenced-by column. "Observed behavior" must state what was actually found at that specific
site -- not a schema-level summary. A Verdict row with "Observed behavior: as expected" is
invalid; name the specific values, labels, or transition evidence observed.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state what the legend said at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only P1/P2/P3 | [list severity values used in Step 3b table, count of each] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | Severity completeness gate verified against Schema 1 | [state G-3 result and the severity labels it checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries, or "no severity field -- inherits from finding"] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used in audit table | [list Source labels used in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label; no SA labels downstream for promoted gaps | [list which SA gaps were promoted; confirm SG label used] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG not SA | [list Source labels in Step 3b table] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated with spec/invocation/artifact/quality | [state activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every Amend entry includes channel field from declared taxonomy | [list channels used; flag any entry missing the field] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 run with explicit PASS/FAIL results | [state G-1/G-2/G-3 results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Hard-stop honored: Phase 4 entered only after all gates PASS | [state gate values at Phase 4 entry; confirm no FAIL gates present] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b waited for Step 3a completion | [state what made Step 3b eligible: Schema 5 prerequisite confirmed] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c waited for Step 3b population | [state transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [state transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 waited for Step 3d channel taxonomy activation | [state transition evidence] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any VC-1 row FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any VC-2 row FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any VC-3 row FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any VC-4 row FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any VC-5 row FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Phrasing register (assertion-first invariant style)

**Axis**: Phrasing register -- the prompt is rewritten in assertion-first declarative style.
Each element declares what a valid instance looks like rather than instructing the tracer what
to do. Coverage Matrix entries are contract assertions. Gate conditions are invariants: "Invariant
G-N holds when [condition]. A trace violating G-N is structurally invalid and cannot advance."
Sub-step ordering is a contract. Phase headers describe what a valid phase produces. The
Verdict audits adherence to these invariants. Fill-in placeholders are preserved so the tracer
knows what to produce. The Verdict remains prose blocks (not ledger) and there is no role-binding
column (C-27/C-28 are not targeted by this axis).

**Hypothesis**: Imperative second-person commands ("Write the relay", "Run all three gates") may
be treated as suggestions by a tracer optimizing for throughput. Assertion style describes the
thing itself -- a trace that violates an assertion is wrong as a matter of definition, not
merely non-compliant with a directive. "A trace with Phase 4 entered while G-1 = FAIL is not a
valid trace" is harder to rationalize past than "Do not proceed to Phase 4." C-30 requires that
FAIL = structural invalidity, not a directive. C-29 and C-27/C-28 are not satisfied by this
axis -- the Verdict stays in prose format and the Coverage Matrix has no Role-binding column.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the authority:
every label, channel, and gate used in any downstream phase must appear in this table.
A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Verdict-check |
|--------|---------|-------------|---------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | VC-5 |

**Schema 1 -- Severity Vocabulary**: A valid severity label in this trace is P1, P2, or P3.
Any entry using a label not in {P1, P2, P3} is structurally invalid and does not count as a
finding. P1 denotes a gap that blocks the artifact from being useful. P2 denotes a quality
improvement that does not block. P3 denotes an advisory observation with no immediate action.

**Schema 2 -- Gap Type Taxonomy**: A valid Source label in this trace is SA, SG, EG, or QO.
SA denotes a spec-layer gap. SG denotes a setup gap. EG denotes an execute gap. QO denotes a
quality observation. A promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION.
A promoted gap retaining its SA label is a label lock violation.

**Schema 3 -- Remediation Channel Taxonomy**: A valid channel in this trace is spec, invocation,
artifact, or quality. A valid Phase 4 Amend entry includes
`[remediation channel: spec / invocation / artifact / quality]`. An Amend entry without a
channel field is structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**: Three invariants govern this trace:
- Invariant G-1: Step 3b contains >=2 distinct Source types. A trace with fewer is missing a
  source layer. A trace violating G-1 is structurally invalid and cannot advance to Step 3d or
  Phase 4.
- Invariant G-2: No two findings sharing the same Source label carry identical Action text. A
  trace violating G-2 has undifferentiated actions and is structurally invalid; it cannot advance.
- Invariant G-3: Every Step 3b entry uses only P1/P2/P3 (Schema 1). A trace violating G-3 has
  invalid severity labels and is structurally invalid; it cannot advance.
When any invariant is violated, the violation is a structural defect that must be corrected and
re-checked. Phase 4 is valid only when G-1 = PASS AND G-2 = PASS AND G-3 = PASS.

**Schema 5 -- Sub-Step Ordering**: The ordering of Phase 3 sub-steps is a contract.
Step 3a is the prerequisite of Step 3b. Step 3b is the prerequisite of Step 3c. Step 3c
all-PASS is the prerequisite of Step 3d. Step 3d is the prerequisite of Phase 4.
A sub-step begun without its prerequisite satisfied is structurally invalid.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 produces: (1) a gap audit table covering all three source layers, and (2) a
relay record carrying the gap inventory forward into Stage 2. Stage 1 reads only
`{{skill_spec_path}}` -- the test invocation is not consulted here.

A valid Stage 1 gap audit table uses only the Source labels from Schema 2 and the Severity
labels from Schema 1. A gap audit table where all gaps cluster at one source type is incomplete
-- the audit must examine harder before declaring done.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

A valid relay record states all four fields:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay from Stage 1: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

A valid Stage 2 carries all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

SA-TO-SG PROMOTION is the designated event at the Setup boundary. Its contract: every SA gap
in the Stage 1 relay is evaluated against the question -- can the invoker supply this value at
runtime even though the spec does not declare it? A gap a spec-competent invoker can supply
promotes to SG. A gap requiring a spec change remains SA.

A valid SA-TO-SG PROMOTION produces one entry per SA gap:

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

A promoted gap retaining its SA label after this event is a Schema 2 label lock violation.

---

#### Phase 1 -- Setup

A valid Setup produces: confirmed input bindings for all declared inputs, and a per-role gap
attribution block. A Setup that lists roles without gap attribution is incomplete.

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role gap attribution: for each role in `[roles: ...]`, a valid entry states which gaps
constrain it. "none -- confirmed" is valid only after verification.

```
[role: {{role_name}}]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

A valid Execute produces: the hand-compiled artifact `{topic}-skill-trace-{date}.md` with every
section the artifact contract requires, and a per-role relay for each role recording what the
role received, what it produced, and any EG gaps it encountered. A role relay with silent
inferences -- values not derivable from the setup carry-forward but not flagged as EG gaps --
is not a valid relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is a sequence governed by Schema 5. A valid Phase 3 runs the sub-steps in the order
declared in Schema 5 and confirms the Schema 5 prerequisite and transition at each step. A
Phase 3 that runs sub-steps out of order or without confirming prerequisites is structurally
invalid.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output of this step: a severity legend for this trace (unblocks Step 3b).

A valid Step 3a produces a table that defines P1, P2, P3 for this specific trace context:

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is now valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output of this step: a merged findings table with >=2 entries (unblocks Step 3c).

A valid findings table uses only the Source labels from Schema 2 (promoted gaps use SG) and
the Severity labels from the Step 3a legend (P1/P2/P3). A table with fewer than 2 entries is
not a valid findings table.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is now valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).
Schema 5 output of this step: gate results for G-1, G-2, G-3 (all-PASS unblocks Step 3d).

A valid Step 3c records an explicit PASS or FAIL for each invariant. A trace that records FAIL
on any invariant and advances to Step 3d or Phase 4 is structurally invalid. The defect must
be corrected before the trace can advance.

**G-1 Invariant** (Schema 4 G-1): Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: structural defect. Step 3d and Phase 4 are invalid. Add missing-layer finding.
  Re-check G-1. A trace with G-1 = FAIL cannot advance.

**G-2 Invariant** (Schema 4 G-2): No two same-Source findings share identical Action text.
- Same-Source pairs: [list or "none"]
- G-2 holds: PASS / G-2 violated: FAIL
- If FAIL: structural defect. Revise Action text to name distinct targets. Re-check G-2.

**G-3 Invariant** (Schema 4 G-3): All Step 3b entries use only P1/P2/P3.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL
- If FAIL: structural defect. Relabel non-conforming entries. Re-check G-3.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is now valid.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

Schema 5 prerequisite: Step 3c all invariants hold (G-1 = PASS, G-2 = PASS, G-3 = PASS).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4 (unblocks Phase 4).

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.
An Amend entry without this field is structurally incomplete.

Schema 5 transition: channel taxonomy active. Phase 4 is now valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

A valid Phase 4 begins only when all three Schema 4 invariants hold: G-1 = PASS, G-2 = PASS,
G-3 = PASS. A Phase 4 entry written while any invariant is violated is not a valid Amend entry.

Gate status confirmation: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 invariant violated. Phase 4 is structurally blocked. Return to Step 3c.

A valid Amend entry (change) states all six fields:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

A valid Amend entry (dismissal) states all four fields:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Coverage Matrix Compliance Audit)

The Verdict is valid only after Phase 4 completes. A Verdict that checks only schema presence
(not usage-site adherence) is not a valid Verdict.

For each schema, a valid VC-N check states whether the Declared-at, Referenced-by, and
Verdict-check columns were honored, with evidence at each usage site.

**VC-1 -- Severity Vocabulary (Schema 1)**:
A valid VC-1 check verifies Schema 1 adherence at every site in the Referenced-by column.
- Declared before Stage 1: YES / NO
- Step 3a: severity legend produced with P1/P2/P3 definitions -- YES / NO
- Step 3b: all entries use only P1/P2/P3 -- YES / NO -- labels used: [list]
- Step 3c G-3: severity completeness verified -- YES / NO
- Phase 4 Amend: all entries use only declared severity -- YES / NO
- Labels outside P1/P2/P3 found: [list or "none"]
- VC-1 result: PASS (all sites compliant) / FAIL (any site non-compliant)

**VC-2 -- Gap Type Taxonomy (Schema 2)**:
A valid VC-2 check verifies Schema 2 adherence at Stage 1, SA-TO-SG PROMOTION, and Step 3b.
- Declared before Stage 1: YES / NO
- Stage 1: only SA/SG/EG/QO used -- YES / NO
- SA-TO-SG PROMOTION ran: YES / NO -- evidence: [which SA gaps evaluated and outcome]
- Promoted gaps use SG downstream (no SA labels for promoted gaps): YES / NO
- Step 3b Source column: only SA/SG/EG/QO -- YES / NO
- VC-2 result: PASS / FAIL

**VC-3 -- Remediation Channel Taxonomy (Schema 3)**:
A valid VC-3 check verifies Schema 3 activated at Step 3d and enforced in Phase 4.
- Declared before Stage 1: YES / NO
- Activated at Step 3d: YES / NO
- All Phase 4 entries include channel field: YES / NO
- Channels used: [list] -- all from {spec, invocation, artifact, quality}: YES / NO
- VC-3 result: PASS / FAIL

**VC-4 -- Enforcement Gate Registry (Schema 4)**:
A valid VC-4 check verifies all three invariants were checked and Phase 4 was not entered while
any invariant was violated.
- Declared before Stage 1: YES / NO
- G-1: PASS / FAIL | G-2: PASS / FAIL | G-3: PASS / FAIL
- Phase 4 entered while any invariant violated: YES (structural defect) / NO (valid)
- VC-4 result: PASS / FAIL

**VC-5 -- Sub-Step Ordering (Schema 5)**:
A valid VC-5 check verifies each Schema 5 ordering contract was honored.
- Step 3b waited for Step 3a: YES / NO
- Step 3c waited for Step 3b population: YES / NO
- Step 3d waited for Step 3c all-PASS: YES / NO
- Phase 4 waited for Step 3d activation: YES / NO
- VC-5 result: PASS (all YES) / FAIL (any NO)

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: Role sequence + Output format (role-binding + compliance ledger with per-role adherence rows)

**Axes**:
- Role sequence (from V-01): Coverage Matrix gains a "Role-binding" column naming every role
  each schema governs. Before Stage 2, a Role-Schema Binding Summary maps each role to its
  schema obligations. Phase 1 Setup per-role entries declare schema bindings. Phase 2 Execute
  role relays include a "Schema 2 compliance" field.
- Output format (from V-02): The Verdict (Phase 5) is a compliance ledger table. Expected
  behavior is pre-filled per row; "Observed behavior" must be stated specifically at each usage
  site. Per-role adherence rows (C-28) extend VC-1 and VC-2: the ledger adds one row per role
  relay for Schema 2 (all roles) and one row per role producing EG findings for Schema 1. These
  per-role rows place role-level accountability directly inside the ledger structure.

**Hypothesis**: V-01 and V-02 each reach 100 under v7, and V-04 R7 combined them with the
per-role rows noted as aspirational. V-04 R8 makes the per-role rows definitive: the Coverage
Matrix Role-binding column declares which roles are bound by which schemas (C-27); the
compliance ledger's per-role adherence rows enforce that declaration at role granularity (C-28);
and the pre-filled Expected behavior in the ledger makes "Observed behavior: as expected"
physically invalid (C-29). C-30 is not targeted -- phrasing remains imperative. The risk is
mechanical overhead: the combined ledger + per-role rows creates more cells than any prior
variation. Mitigation: per-role rows have fewer possible values than usage-site rows (each role
either used the correct labels or didn't), so even a tracer filling nominally is forced to name
the role and its labels explicitly.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the phases
that require it, the roles bound by it, and the Verdict check that audits it. All phases reference
only the labels declared here.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings (severity label applies to every EG entry they produce) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in role relay uses only SA/SG/EG/QO; promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments drawn from all roles' findings (aggregate, not per-relay) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column coverage across all roles' findings in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between all sub-steps) | N/A -- applies to Findings phase structure, not individual roles | VC-5 |

#### Severity Vocabulary (Schema 1)

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through phases with SG label |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable, not structural | Surface anywhere; P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

| Channel | Targets | Activated-at |
|---------|---------|-------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

Read the skill spec and declare each role in the execution sequence. For each role, record which
schemas govern its behavior. Fill this table before Stage 2 begins. A role without explicit schema
binding is invalid. One row per role found in the spec.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's findings, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using Schema 2
(Gap Type Taxonomy) and Schema 1 (Severity Vocabulary).

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types (Schema 2). Examine harder if
gaps cluster at one layer.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

At the Setup boundary. For every SA gap in the relay, evaluate:

> Can the invoker supply this value at runtime even though the spec doesn't declare it?

```
SA-NN -> [result]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock: promoted gaps use SG label in all downstream phases.

---

#### Phase 1 -- Setup

Confirm each input with `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role schema binding and gap attribution**: For each role in `[roles: ...]`, declare its
schema obligations from the Role-Schema Binding Summary, then enumerate its gaps. A role entry
without schema binding declaration is invalid. "none -- confirmed" only after verifying.

```
[role: {{role_name}}]
  Schema 1 binding: [which severity labels apply to this role's findings, or "N/A"]
  Schema 2 binding: [which Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must appear.

For each role, open its relay before writing the artifact section. The "Schema 2 compliance"
field is required. A role relay without it is structurally invalid.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Do not infer silently.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], all gaps from Stages 1 and 2.

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step prints its Schema 5
Prerequisite and Unblocks values before beginning.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 prerequisite**: Schema 1 (Severity Vocabulary) declared in Coverage Matrix.
**Schema 5 output**: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b -- Findings Table

**Schema 5 prerequisite**: Step 3a complete (severity legend written above).
**Schema 5 output**: findings table with >=2 entries (unblocks Step 3c).

Merge all gaps from Stage 1 and Stage 2. Use promoted Source labels (Schema 2). Use only
P1/P2/P3 (Step 3a legend):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

---

##### Step 3c -- Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated (>=2 entries).
**Schema 5 output**: gate results (all must be PASS to unblock Step 3d).

Run all three gates from Schema 4. Record PASS or FAIL explicitly.

**Hard-stop rule (Schema 4)**: a FAIL on any gate BLOCKS Step 3d and Phase 4.
Resolve the failing condition, re-run the gate, confirm PASS before proceeding.

**G-1 Source Diversity Gate** (Schema 4)
- Property: >=2 distinct Source types present in Step 3b
- Source types present: [list all Source values from table]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Add missing-layer finding. Re-run G-1.

**G-2 Action Diversity Gate** (Schema 4)
- Property: no two same-Source findings carry identical Action text
- Same-Source pairs reviewed: [list pairs, or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Revise duplicate Actions. Re-run G-2.

**G-3 Severity Completeness Gate** (Schema 4)
- Property: all Step 3b entries use only P1/P2/P3 (Schema 1; Step 3a legend)
- Severity labels in Step 3b: [list all values used]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Relabel non-conforming entries. Re-run G-3.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

**Schema 5 prerequisite**: Step 3c all gates PASS.
**Schema 5 output**: Schema 3 channel taxonomy activated for Phase 4 (unblocks Phase 4).

Activate: spec / invocation / artifact / quality (from Schema 3).

Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check** (hard-stop conditions): G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
All must be PASS. If any = FAIL: Schema 4 hard-stop active. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d (Schema 3): spec / invocation / artifact / quality.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

Fill the compliance ledger completely. One row per usage site declared in the Coverage Matrix
Referenced-by column, plus one per-role adherence row for each role bound by Schema 1 or
Schema 2 per the Role-binding column.

"Observed behavior" must state what was actually found at that specific site or role relay --
not a schema-level summary. A cell reading "Observed behavior: as expected" is invalid; name
the specific values, labels, role name, or transition evidence observed.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state what the legend said at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only P1/P2/P3 | [list severity values used in Step 3b table, count of each] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | Severity completeness gate verified against Schema 1 | [state G-3 result and the severity labels it checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries, or "no severity field -- inherits from finding"] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role name producing EG findings] | EG findings from this role use only P1/P2/P3 | [list severity labels used by this role's EG findings specifically] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used in audit table | [list Source labels used in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label; no SA labels downstream for promoted gaps | [list which SA gaps were promoted; confirm SG label used in all downstream phases] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG not SA | [list Source labels in Step 3b table; flag any SA label for a promoted gap] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role name] | Source labels in this role's relay from {SA,SG,EG,QO}; label lock honored | [list Source labels used by this role in its relay; confirm against promotion list] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated with spec/invocation/artifact/quality | [state activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every Amend entry includes channel field from declared taxonomy | [list channels used; flag any entry missing the field] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 run with explicit PASS/FAIL results | [state G-1/G-2/G-3 results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Hard-stop honored: Phase 4 entered only after all gates PASS | [state gate values at Phase 4 entry; confirm no FAIL gates present] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1 cross-role) | G-1 verified Source diversity across all roles' contributions | [list Source types present and which roles contributed each type] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b waited for Step 3a completion | [state what made Step 3b eligible: Schema 5 prerequisite confirmed] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c waited for Step 3b population | [state transition evidence: entry count at Step 3c start] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [state transition evidence: gate results present before Step 3d] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 waited for Step 3d channel taxonomy activation | [state transition evidence: channel taxonomy activation confirmed before Phase 4] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS (including per-role rows) / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS (including per-role rows) / FAIL if any FAIL
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

---

## V-05 -- Combined axes: Role sequence + Output format + Phrasing register (R8 ceiling)

**Axes**:
- Role sequence (from V-01 / V-04): Coverage Matrix gains Role-binding column. Role-Schema
  Binding Summary before Stage 2. Per-role schema binding in Phase 1. Schema 2 compliance
  field in Phase 2 role relays.
- Output format (from V-02 / V-04): Verdict is a compliance ledger table with pre-filled
  Expected behavior. Per-role adherence rows for VC-1 (roles producing EG findings) and VC-2
  (all roles with relays) and VC-4 cross-role G-1 check. "Observed behavior: as expected"
  is invalid by format.
- Phrasing register (from V-03): Protocol constraints expressed as logical invariants.
  "Schema 4 governs three invariants of this trace. A trace violating any invariant is
  structurally invalid." Gate conditions state the invariant and its consequence. Sub-step
  ordering is a contract. Phase headers describe what a valid instance produces. FAIL always
  = structural invalidity, never just a directive.

**Hypothesis**: V-04 combines C-27 + C-28 + C-29 and should reach 99+ under v8. The gap
preventing 100 is C-30: V-04 retains imperative language ("Run all three gates", "Phase 4
BLOCKED"). V-05 converts all gate conditions, schema definitions, and phase prerequisites to
assertion-first invariant style. The integration test is whether assertion framing harmonizes
with the compliance ledger: "Invariant G-1 holds when Step 3b contains >=2 distinct Source
types. A trace violating G-1 is structurally invalid. The compliance ledger records G-1's
observed status." The ledger Observed behavior cell becomes a record of whether the invariant
was found to hold, not a directive to check it. This should satisfy all four new v8 criteria:
C-27 (role-binding column + Binding Summary), C-28 (per-role rows in ledger), C-29 (ledger
format + pre-filled Expected), C-30 (invariant framing + structural invalidity language).

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings (severity label applies to every EG entry they produce) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in each role relay uses only SA/SG/EG/QO; promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments drawn from all roles' findings (aggregate, not per-relay) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column coverage across all roles' findings in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between all sub-steps) | N/A -- applies to Findings phase structure, not individual roles | VC-5 |

**Schema 1 -- Severity Vocabulary**: A valid severity label in this trace is P1, P2, or P3.
An entry using a label not in {P1, P2, P3} is structurally invalid. P1 denotes a gap that
blocks the artifact from being useful. P2 denotes a quality improvement that does not block.
P3 denotes an advisory observation. A trace is valid with respect to Schema 1 if and only if
every EG finding produced by every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: A valid Source label in this trace is SA, SG, EG, or QO.
SA denotes a spec-layer gap. SG denotes a setup gap. EG denotes an execute gap. QO denotes a
quality observation. The SA-TO-SG label lock invariant: a promoted SA gap uses the SG label
in all phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a label lock
violation and renders the trace structurally invalid at that point.

**Schema 3 -- Remediation Channel Taxonomy**: A valid Phase 4 Amend entry includes
`[remediation channel: spec / invocation / artifact / quality]`. An Amend entry without a
channel field is structurally incomplete. A trace is valid with respect to Schema 3 if and
only if every Amend entry names a channel from {spec, invocation, artifact, quality}.

**Schema 4 -- Enforcement Gate Registry**: Three invariants govern this trace. A trace violating
any invariant is structurally invalid at the point of violation and cannot advance:
- Invariant G-1: Step 3b contains >=2 distinct Source types. A trace with fewer is missing a
  source layer and is structurally invalid; it cannot advance to Step 3d or Phase 4.
- Invariant G-2: No two findings sharing the same Source label carry identical Action text. A
  trace with undifferentiated actions is structurally invalid; it cannot advance.
- Invariant G-3: Every Step 3b entry uses only {P1, P2, P3} (Schema 1). A trace with invalid
  severity labels is structurally invalid; it cannot advance.
A trace is valid with respect to Schema 4 if and only if G-1 = PASS AND G-2 = PASS AND
G-3 = PASS before Phase 4 begins. A structural defect must be corrected and re-checked;
it cannot be bypassed.

**Schema 5 -- Sub-Step Ordering**: The ordering of Phase 3 sub-steps is a contract. Step 3b
is valid if and only if Step 3a has produced a severity legend. Step 3c is valid if and only
if Step 3b has produced >=2 findings. Step 3d is valid if and only if Step 3c has produced
G-1 = PASS AND G-2 = PASS AND G-3 = PASS. Phase 4 is valid if and only if Step 3d has
activated the channel taxonomy. A sub-step begun without its prerequisite satisfied is
structurally invalid.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

A valid trace declares every role in the execution sequence here before Stage 2 begins. For
each role, the binding declares which schemas govern its behavior. A role without explicit schema
binding is invalid in this trace. One row per role found in the spec.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's EG findings, or "N/A -- produces no EG findings"] | [Source labels this role may produce in its relay; label lock rules for promoted gaps] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 produces: (1) a gap audit table covering all three source layers using only
Schema 2 Source labels and Schema 1 Severity labels, and (2) a relay record carrying the gap
inventory into Stage 2. Stage 1 reads only `{{skill_spec_path}}` -- the test invocation is not
consulted here.

A Stage 1 where all gaps cluster at one source type is structurally incomplete. A valid Stage 1
examines all three source layers before declaring done.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

A valid relay record states all four fields:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

A valid Stage 2 carries all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

SA-TO-SG PROMOTION is the designated lifecycle event at the Setup boundary. Its invariant: every
SA gap in the Stage 1 relay is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA. A trace that skips this evaluation is
structurally incomplete.

A valid SA-TO-SG PROMOTION produces one entry per SA gap:

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

Schema 2 label lock invariant: a promoted gap using its SA label in any downstream phase is
a structural violation of this trace.

---

#### Phase 1 -- Setup

A valid Setup produces: confirmed input bindings for all declared inputs, and a per-role schema
binding and gap attribution block for each role. A Setup that lists roles without schema binding
declarations is structurally incomplete.

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution: for each role in `[roles: ...]`, a valid entry
declares its schema obligations (from the Role-Schema Binding Summary) then states its gaps.
"none -- confirmed" is valid only after verification.

```
[role: {{role_name}}]
  Schema 1 binding: [which severity labels apply to this role's findings, or "N/A"]
  Schema 2 binding: [which Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

A valid Execute produces: the hand-compiled artifact `{topic}-skill-trace-{date}.md` with every
section the artifact contract requires, and a per-role relay for each role that records receipt,
Schema 2 compliance, gaps, output, and any EG gaps encountered. A role relay without the
"Schema 2 compliance" field is structurally invalid. A relay with silent inferences is not valid.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5 and each
Schema 5 prerequisite is satisfied before the sub-step begins. A Phase 3 that runs sub-steps
out of order is structurally invalid.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: a severity legend for this trace (unblocks Step 3b).

A valid Step 3a produces a legend that defines P1, P2, P3 for this specific trace:

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: a merged findings table with >=2 entries (unblocks Step 3c).

A valid findings table uses only Source labels from Schema 2 (promoted gaps use SG) and Severity
labels from the Step 3a legend. A table with fewer than 2 entries is not a valid findings table.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).
Schema 5 output: invariant results for G-1, G-2, G-3 (all-PASS unblocks Step 3d).

A valid Step 3c records an explicit result for each invariant. A trace that records FAIL on any
invariant and advances to Step 3d or Phase 4 is structurally invalid. The structural defect must
be corrected and the invariant re-checked before the trace can advance.

**G-1 Invariant** (Schema 4): Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: structural defect. This trace is invalid and cannot advance to Step 3d or Phase 4.
  Identify the missing source layer. Add a finding from that layer. Re-check G-1.

**G-2 Invariant** (Schema 4): No two findings sharing the same Source label carry identical Action text.
- Same-Source pairs examined: [list or "none -- all Source types unique"]
- G-2 holds: PASS / G-2 violated: FAIL
- If FAIL: structural defect. Revise Action text to name distinct targets. Re-check G-2.

**G-3 Invariant** (Schema 4): All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL
- If FAIL: structural defect. Relabel non-conforming entries. Re-check G-3.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

Schema 5 prerequisite: Step 3c all invariants hold (G-1 = PASS, G-2 = PASS, G-3 = PASS).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4 (unblocks Phase 4).

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.
An Amend entry without this field is structurally incomplete.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

A valid Phase 4 begins if and only if all three Schema 4 invariants hold: G-1 = PASS,
G-2 = PASS, G-3 = PASS. A Phase 4 entry produced while any invariant is violated is not a
valid Amend entry.

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 invariant violated. Phase 4 is structurally blocked. Return to Step 3c.

A valid Amend entry (change) states all six fields:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock invariant; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

A valid Amend entry (dismissal) states all four fields:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

The Verdict is valid if and only if it is produced after Phase 4 completes and audits every
usage site and role binding declared in the Coverage Matrix. A Verdict row with "Observed
behavior: as expected" is structurally invalid; the Observed behavior cell must name the
specific values, labels, role name, or invariant status observed.

Fill the compliance ledger completely. One row per usage site in the Coverage Matrix
Referenced-by column, plus per-role adherence rows for VC-1 (roles producing EG findings)
and VC-2 (all roles with relays), and one cross-role G-1 row for VC-4.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state what the legend said at Step 3a -- the actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only {P1, P2, P3} | [list severity values used in Step 3b table; count of each; flag any outside {P1,P2,P3}] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 invariant verified against Schema 1: all entries use {P1,P2,P3} | [state G-3 result and the severity labels it checked; confirm result is PASS] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only {P1,P2,P3} | [list severity values in Amend entries, or state which field carries severity] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role name producing EG findings] | EG findings from this role use only {P1,P2,P3} per Schema 1 binding | [list severity labels used by this role's EG findings specifically; confirm schema binding honored] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used in audit table | [list all Source labels used in Stage 1 table; confirm no labels outside schema] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label; SA label lock invariant holds downstream | [list SA gaps promoted; confirm each uses SG label in all downstream references] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG not SA | [list Source labels in Step 3b table; identify any promoted gap and confirm its label] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role name] | Source labels in this role's relay from {SA,SG,EG,QO}; label lock invariant honored | [list Source labels used by this role; state if any promoted gap appears and confirm SG label] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated: spec/invocation/artifact/quality declared active | [state the activation evidence at Step 3d -- what language signaled activation] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every Amend entry includes channel field from {spec,invocation,artifact,quality} | [list channels used in each Amend entry; flag any entry missing the field] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 invariants checked with explicit PASS/FAIL | [state G-1/G-2/G-3 results recorded at Step 3c; confirm all three were checked] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Schema 4 invariants hold: Phase 4 entered only when G-1=PASS, G-2=PASS, G-3=PASS | [state invariant status at Phase 4 entry; confirm no violated invariant was present] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1 cross-role) | G-1 invariant verified across all roles: >=2 distinct Source types present in Step 3b | [list Source types present and which roles contributed each; confirm G-1 holds] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b is valid only when Step 3a has produced a severity legend | [state what confirmed Step 3a complete before Step 3b began] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c is valid only when Step 3b has produced >=2 findings | [state entry count in Step 3b at the point Step 3c began] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d is valid only when Step 3c has produced all-PASS invariant results | [state gate results present before Step 3d began] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 is valid only when Step 3d has activated the channel taxonomy | [state activation confirmation present before Phase 4 began] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS (including per-role rows) / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS (including per-role rows) / FAIL if any FAIL
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
