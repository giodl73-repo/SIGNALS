---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 7
rubric: trace-skill-rubric-v7-2026-03-15.md
---

# trace-skill -- Variations R7 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

Round 7 target: C-24, C-25, C-26 -- the three new v7 aspirational criteria. V-04 R6 is the
sole variation to reach 100 under v7. The ceiling gap for V-01/V-02/V-03 was:

- V-01 (99.25): C-24 PARTIAL (Dependency column approximates reference-tracking but does not
  satisfy it), C-26 FAIL (no Schema 5 in registry).
- V-02 (99.0): C-24 FAIL (license letter designators used but not enumerated in the registry
  as reference sites), C-26 FAIL.
- V-03 (98.5): C-24 FAIL, C-25 PARTIAL (Verdict presence-check does not verify usage-site
  adherence), C-26 FAIL.

V-04 R6 reaches 100 by: (1) Coverage Matrix with Declared-at/Referenced-by/Verdict-check
columns (C-24), (2) VC-1 through VC-5 each verify actual adherence at each named usage site,
not just presence (C-25), (3) Schema 5 in the Coverage Matrix with Prerequisite/Unblocks
columns (C-26).

R7 builds on V-04 R6's complete architecture. All five R7 variations inherit:
- Coverage Matrix with 5 schemas (Declared-at, Referenced-by, Verdict-check)
- Schema 5 (Sub-Step Ordering) with Prerequisite and Unblocks columns
- Hard-stop BLOCKED language on gate FAIL
- VC-1 through VC-5 verifying per-usage-site adherence
- All schemas declared before Stage 1

The variations explore formulations that may be more robust to compliance drift:

Single-axis selections: Role sequence (V-01), Output format (V-02), Phrasing register (V-03).
Combined: Role sequence + Output format (V-04), Lifecycle emphasis + Inertia framing (V-05).

---

## V-01 -- Single axis: Role sequence (role-schema binding column in Coverage Matrix)

**Axis**: Role sequence -- the Coverage Matrix gains a fifth column, "Role-binding," that
names every role in the skill spec that each schema governs. Before Stage 2, a Role-Schema
Binding summary table maps each role to its schema obligations. In Phase 1 Setup, each role
entry declares its schema bindings alongside gap attribution. In Phase 2 Execute, every role
relay includes a "Schema 2 compliance" field listing the Source labels used. The Verdict's
VC-1 through VC-4 each include a per-role adherence check.

**Hypothesis**: V-04 R6 maps schemas to phases and Verdict checks via the Referenced-by and
Verdict-check columns, but the role-level binding is implicit. A tracer who faithfully follows
the phase structure might still violate Schema 2 label lock in a role relay without the
Coverage Matrix flagging it. The Role-binding column makes schema obligations role-specific
and auditable by the Verdict at role granularity, not just phase granularity. C-24 is already
satisfied by the Referenced-by column; Role-binding extends it. C-25 benefits because the
Verdict now checks "Schema 2 honored in relay for [role X]" as a specific usage site. Risk:
role-binding adds mechanical overhead; a tracer who fills the Role-binding cell "all roles"
satisfies the format without the reasoning. The Verdict's per-role adherence check requires
evidence per role, not per schema.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it, the roles that are bound by it, and the Verdict check that audits it.
All phases reference only the labels declared here.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings (severity label applies to every EG entry) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Setup per-role attribution, Step 3b Source column, Execute role relay | All roles (Source label in role relay uses only SA/SG/EG/QO; promoted gaps use SG label) | VC-2 |
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

Read the skill spec and declare each role in the execution sequence. For each role, record
which schemas govern its behavior. Fill before Stage 2 begins.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's findings] | [Source labels this role may produce; label lock rules] | [any schema 3/4 interactions] |

A role without explicit schema binding is invalid. One row per role found in the spec.

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using
Schema 2 (Gap Type Taxonomy) and Schema 1 (Severity Vocabulary).

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without
content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types (Schema 2). Examine harder
if gaps cluster at one layer.

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

**Per-role schema binding and gap attribution**: For each role in `[roles: ...]`, declare
its schema obligations from the Role-Schema Binding Summary, then enumerate its gaps:

```
[role: {{role_name}}]
  Schema 1 binding: [which severity labels apply to this role's findings]
  Schema 2 binding: [which Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

A role entry without schema binding declaration is invalid. "none -- confirmed" only after
verifying.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear.

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

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step prints its
Schema 5 Prerequisite and Unblocks values before beginning.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 prerequisite**: Schema 1 (Severity Vocabulary) declared in Coverage Matrix.
**Schema 5 output**: severity legend for this trace (unblocks Step 3b).

Write the active severity legend:

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
P1/P2/P3 (Step 3a):

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
Phase 4. The gate's hard-stop condition is active. Resolve the failing condition, re-run the
gate, confirm PASS before proceeding.

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
- **If FAIL**: Schema 4 hard-stop active for Step 3d and Phase 4. Revise duplicate Actions
  to name distinct targets. Re-run G-2. Do not proceed until PASS.

**G-3 Severity Completeness Gate** (Schema 4)
- Property: all Step 3b entries use only P1/P2/P3 (Schema 1; Step 3a legend)
- Severity labels in Step 3b: [list all values used]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active for Step 3d and Phase 4. Relabel non-conforming
  entries. Re-run G-3. Do not proceed until PASS.

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
[G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active from Step 3d].

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
Role-binding, and Verdict-check columns were honored. VC-1 through VC-4 include a per-role
adherence check naming each role and the observed behavior at that role site.

**VC-1 -- Severity Vocabulary (Schema 1)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- Referenced in Step 3a: YES / NO -- evidence: [what the legend produced]
- Referenced in Step 3b (only P1/P2/P3 used): YES / NO -- labels used: [list]
- Referenced in Step 3c G-3 (severity completeness verified): YES / NO
- Role-binding honored: for each role that produced EG findings, list role and severity labels
  used: [per-role list, e.g., "Role A: P1, P2 -- Schema 1 compliant; Role B: ..."]
- Labels outside P1/P2/P3 found anywhere: [list or "none"]
- VC-1 result: PASS / FAIL

**VC-2 -- Gap Type Taxonomy (Schema 2)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- SA-TO-SG PROMOTION ran: YES / NO -- evidence: [which SA gaps were evaluated]
- SA labels appearing after promotion for promoted gaps: [list or "none"]
- Step 3b Source column uses only SA/SG/EG/QO: YES / NO
- Role-binding honored: for each role relay in Phase 2, list role and Source labels used:
  [per-role list, e.g., "Role A relay: EG -- Schema 2 compliant; Role B relay: SG, EG -- ..."]
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
holds each site accountable.

**Hypothesis**: V-04 R6's Verdict walks each schema as a prose block with fill-in fields
(e.g., "Labels used: [list]"). A tracer writing "Labels used: P1, P2" satisfies the form
without documenting WHERE in Phase 2 Execute P1/P2 were produced by which role. The ledger
forces a row per usage site, making C-25 per-site adherence structural: "Observed behavior at
Step 3b: all 4 entries use P1 or P2 -- no outliers" is more evidenced than "labels used:
P1, P2." Risk: the ledger can become mechanical if "Observed behavior" cells are filled with
tautologies. Mitigation: the Expected behavior cell is pre-filled so the tracer must state
something different (the observed instance), not just restate the expectation.

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

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without
content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types. Examine harder if gaps
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

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear.

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

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step prints its
Schema 5 Prerequisite and Unblocks values before beginning.

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

## V-03 -- Single axis: Phrasing register (assertion-first contract style)

**Axis**: Phrasing register -- the prompt is rewritten in assertion-first declarative style.
Each element declares what a valid instance looks like rather than instructing the tracer what
to do. Coverage Matrix entries are contract assertions ("Schema 1 governs severity labels in
this trace. Step 3b is valid if and only if all entries use P1, P2, or P3."). Gate conditions
are invariants ("The invariant G-1 holds when Step 3b contains >=2 distinct Source types.
A trace violating G-1 cannot advance to Step 3d or Phase 4."). Sub-step ordering is a
contract ("Step 3b is valid only when Step 3a has produced a severity legend. Step 3b begun
without Step 3a complete is structurally invalid."). Phase headers describe what a valid phase
produces. Fill-in placeholders are preserved so the tracer knows what to produce.

**Hypothesis**: V-04 R6 uses imperative second-person commands ("Write the relay", "Run all
three gates"). Assertion style may produce more robust compliance: a tracer who treats
instructions as suggestions may follow assertions more carefully because assertions describe
the thing itself -- a trace that violates an assertion is not just incomplete, it is wrong
as a matter of the definition. C-22 becomes a logical constraint rather than a directive:
"A trace with Phase 4 entered while G-1 = FAIL is not a valid trace" is harder to rationalize
past than "Do not proceed to Phase 4." Risk: assertion style removes procedural scaffolding;
low-context tracers may not know how to produce a valid instance. Fill-in placeholders
explicitly inherited from V-04 mitigate this by preserving the production structure inside
the assertion frame.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The coverage matrix is the authority:
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
SA denotes a spec-layer gap (spec does not declare the element). SG denotes a setup gap
(spec declares it; invoker cannot supply it). EG denotes an execute gap (contract requires
it; role cannot produce it). QO denotes a quality observation. A promoted SA gap uses the SG
label in all phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a
label lock violation.

**Schema 3 -- Remediation Channel Taxonomy**: A valid channel in this trace is spec,
invocation, artifact, or quality. A valid Phase 4 Amend entry includes
`[remediation channel: spec / invocation / artifact / quality]`. An Amend entry without a
channel field is structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**: Three invariants govern the trace:
- Invariant G-1: Step 3b contains >=2 distinct Source types. A trace with fewer is missing
  a source layer. A trace violating G-1 cannot advance to Step 3d or Phase 4.
- Invariant G-2: No two findings sharing the same Source label carry identical Action text.
  A trace violating G-2 has undifferentiated actions and cannot advance.
- Invariant G-3: Every Step 3b entry uses only P1/P2/P3 (Schema 1). A trace violating G-3
  has invalid severity labels and cannot advance.
When any invariant is violated, the violation must be resolved and the invariant re-checked
before Phase 3 can advance. Phase 4 is valid only when G-1 = PASS AND G-2 = PASS AND G-3 = PASS.

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

A valid Stage 1 produces: (1) a gap audit table covering all three source layers, and
(2) a relay record that carries the gap inventory forward into Stage 2. Stage 1 reads only
`{{skill_spec_path}}` -- the test invocation is not consulted here.

A valid Stage 1 gap audit table uses only the Source labels from Schema 2 and the Severity
labels from Schema 1. A gap audit table with a source layer not covered (all gaps cluster
at one type) is incomplete -- examine harder before declaring done.

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
in the Stage 1 relay is evaluated against the question: can the invoker supply this value at
runtime even though the spec does not declare it? A gap that a spec-competent invoker can
supply promotes to SG. A gap requiring a spec change remains SA.

A valid SA-TO-SG PROMOTION produces one entry per SA gap:

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

After promotion, the relay is updated:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

A promoted gap retaining its SA label after this event is a Schema 2 label lock violation.

---

#### Phase 1 -- Setup

A valid Setup produces: confirmed input bindings for all declared inputs, and a per-role gap
attribution table. A Setup that lists roles without gap attribution is incomplete.

Confirmed input bindings (state the value, not a placeholder):

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role gap attribution: for each role in `[roles: ...]`, a valid attribution entry states
which gaps constrain it. "none -- confirmed" is valid only after verification.

```
[role: {{role_name}}]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

A valid Execute produces: the hand-compiled artifact `{topic}-skill-trace-{date}.md` with
every section the artifact contract requires, plus a per-role relay for each role that
records what the role received, what it produced, and any EG gaps it encountered.

A role relay with silent inferences -- values not derivable from the setup carry-forward or
the test invocation but not flagged as EG gaps -- is not valid.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is a sequence governed by Schema 5. A valid Phase 3 runs the sub-steps in the
order declared in Schema 5 and confirms the Schema 5 prerequisite and transition at each step.
A Phase 3 that runs sub-steps out of order or without confirming prerequisites is invalid.

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

A valid Step 3c records an explicit PASS or FAIL for each gate. A trace that records FAIL
on any gate and advances to Step 3d or Phase 4 violates Schema 4 invariants G-1, G-2, or G-3.
The violation must be resolved before the trace can advance. The resolution protocol: identify
the gap in the findings table, correct it, re-run the gate.

**G-1 Invariant** (Schema 4 G-1): Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: Schema 4 hard-stop active for Step 3d and Phase 4. Add finding from missing
  layer. Re-run G-1. A trace with G-1 = FAIL cannot advance.

**G-2 Invariant** (Schema 4 G-2): No two same-Source findings share identical Action text.
- Same-Source pairs: [list or "none"]
- G-2 holds: PASS / G-2 violated: FAIL
- If FAIL: Schema 4 hard-stop active. Revise Action text to name distinct targets. Re-run G-2.

**G-3 Invariant** (Schema 4 G-3): All Step 3b entries use only P1/P2/P3.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL
- If FAIL: Schema 4 hard-stop active. Relabel non-conforming entries. Re-run G-3.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is now valid.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

Schema 5 prerequisite: Step 3c all invariants hold (G-1 = PASS, G-2 = PASS, G-3 = PASS).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4 (unblocks Phase 4).

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.
An Amend entry without this field is not a valid Amend entry.

Schema 5 transition: channel taxonomy active. Phase 4 is now valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

A valid Phase 4 begins only when all three Schema 4 invariants hold: G-1 = PASS, G-2 = PASS,
G-3 = PASS. A Phase 4 entry written while any gate = FAIL is not a valid Amend entry.

Gate status confirmation: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 hard-stop active. Phase 4 is BLOCKED. Return to Step 3c.

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

The Verdict is valid only after Phase 4 completes. A Verdict that runs before Phase 4 or
that checks only schema presence (not usage-site adherence) is not a valid Verdict.

Walk the Coverage Matrix row by row. For each schema, a valid VC-N check states whether
the Declared-at, Referenced-by, and Verdict-check columns were honored, with evidence at
each usage site.

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
- SA-TO-SG PROMOTION ran: YES / NO -- evidence: [which SA gaps were evaluated and outcome]
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
A valid VC-4 check verifies all three invariants were checked and Phase 4 was not entered
while any invariant was violated.
- Declared before Stage 1: YES / NO
- G-1 result at Step 3c: PASS / FAIL | G-2: PASS / FAIL | G-3: PASS / FAIL
- Phase 4 entered while any invariant violated: YES (violation) / NO (clean)
- VC-4 result: PASS / FAIL

**VC-5 -- Sub-Step Ordering (Schema 5)**:
A valid VC-5 check verifies each Schema 5 transition was honored.
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

## V-04 -- Combined axes: Role sequence + Output format (role-schema binding + compliance ledger)

**Axes**:
- Role sequence (from V-01): Coverage Matrix gains a Role-binding column naming every role
  each schema governs. Before Stage 2, a Role-Schema Binding Summary maps each role to its
  schema obligations. Phase 1 Setup per-role entries declare schema bindings. Phase 2 Execute
  role relays include a "Schema 2 compliance" field.
- Output format (from V-02): The Verdict (Phase 5) is a compliance ledger table with one row
  per declared usage site. Observed behavior must be stated for each site, not just schema-level
  summaries. VC-1 through VC-5 ledger rows follow the Coverage Matrix Referenced-by column.

**Hypothesis**: V-01 and V-02 each reach 100 under v7 on the strength of the V-04 R6
foundation. V-04 R7 tests whether the two extensions reinforce each other without creating
mechanical overhead that degrades depth. The role-schema binding makes every schema obligation
role-addressable; the compliance ledger makes every usage site evidence-addressable. Together
they create a two-dimensional accountability structure: schema × role (from V-01) AND
schema × usage-site (from V-02). The Verdict ledger can include per-role rows where the
Coverage Matrix Role-binding column names roles, making VC-1 and VC-2 even more specific.
Risk: the combined mechanical load may cause tracers to fill cells nominally. Mitigation:
the compliance ledger's pre-filled "Expected behavior" forces the tracer to state something
different in "Observed behavior."

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it, the roles bound by it, and the Verdict check that audits it.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source labels in relay; label lock after promotion) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 Amend drawn from all roles | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check | G-1 aggregates Source coverage across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

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
| QO | Quality observation -- improvable, not structural | P3 severity typical |

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

Read the skill spec. For each role in the execution sequence, declare its schema obligations.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable] | [Source labels this role may produce; label lock rules] | [schema 3/4 interactions] |

One row per role. A role without explicit schema binding is invalid.

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Use Schema 2 for Source
labels and Schema 1 for Severity labels.

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without
content rules.
**SG pre-audit**: declared inputs the invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: >=2 distinct Source types. Examine harder if gaps cluster at one layer.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay in**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### SA-TO-SG PROMOTION (named lifecycle event)

```
SA-NN -> [result]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock: promoted gaps use SG label downstream.

---

#### Phase 1 -- Setup

Confirm inputs:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role schema binding and gap attribution**: for each role, declare schema bindings from
the Role-Schema Binding Summary, then enumerate gaps:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels for this role's findings]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear. Per-role relay before each artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Schema 2 compliance field required. Do not infer silently.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 runs in the sequence declared in Schema 5. Each sub-step states its Schema 5
Prerequisite and Unblocks before beginning.

---

##### Step 3a

**Schema 5 prerequisite**: Schema 1 declared. **Schema 5 unblocks**: Step 3b.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write] | Resolve before leaving Findings |
| P2 | [write] | Address in Amend or follow-on |
| P3 | [write] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b

**Schema 5 prerequisite**: Step 3a complete. **Schema 5 unblocks**: Step 3c.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated. Step 3c unblocked.

---

##### Step 3c

**Schema 5 prerequisite**: Step 3b populated. **Schema 5 unblocks**: Step 3d (if all-PASS).

**Hard-stop rule (Schema 4)**: FAIL on any gate BLOCKS Step 3d and Phase 4.

**G-1** -- Source types present: [list] -- Result: PASS / FAIL
**If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Add missing-layer finding. Re-run G-1.

**G-2** -- Same-Source pairs: [list or "none"] -- Result: PASS / FAIL
**If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Revise duplicate Actions. Re-run G-2.

**G-3** -- Severity labels in Step 3b: [list] -- Result: PASS / FAIL
**If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Relabel entries. Re-run G-3.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

---

##### Step 3d

**Schema 5 prerequisite**: Step 3c all-PASS. **Schema 5 unblocks**: Phase 4.

Activate Schema 3: spec / invocation / artifact / quality.
Every Phase 4 entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 hard-stop active. Phase 4 BLOCKED. Return to Step 3c.

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Role-Binding + Compliance Ledger)

Fill the compliance ledger. One row per declared usage site from the Referenced-by column.
Where the Role-binding column names specific roles, add per-role rows for VC-1 and VC-2.
"Observed behavior" must state specific values found -- not "as expected."

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend: P1/P2/P3 defined for this trace | [what the legend stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use P1/P2/P3 only | [severity labels in table; count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate verified | [G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use only P1/P2/P3 | [severity labels in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | [role name] EG findings | Role binds Schema 1 (Coverage Matrix Role-binding) | [severity labels used by this role] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG; no SA downstream | [which SA gaps promoted; SG labels confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source | SA/SG/EG/QO only; promoted show SG | [Source labels in Step 3b] | PASS / FAIL |
| VC-2 | Schema 2 | [role name] relay | Role relay uses only SA/SG/EG/QO (Coverage Matrix Role-binding) | [Source labels in this role's relay] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels used; entries missing field if any] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 run with explicit results | [G-1/G-2/G-3 results] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Hard-stop honored: no Phase 4 while any gate = FAIL | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | G-1 role aggregation | G-1 checks Source coverage across all roles | [Source types present and which roles contributed] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL otherwise
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL otherwise
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL otherwise
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL otherwise
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL otherwise

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: Lifecycle emphasis + Inertia framing (Schema-5-as-spine + cost-of-omission column)

**Axes**:
- Lifecycle emphasis: Schema 5 (Sub-Step Ordering) is declared first in the Coverage Matrix
  and acts as the structural spine of the entire trace. Every phase and sub-step is introduced
  as a Schema 5 node. Schemas 1-4 are declared as dependencies of specific Schema 5 nodes --
  not as standalone declarations. This makes the execution sequence the primary structure and
  all schema definitions secondary. The Coverage Matrix is introduced as "the complete
  execution graph."
- Inertia framing: each schema in the Coverage Matrix includes a "Cost-of-omission" column
  with a one-phrase statement naming the concrete failure mode the schema prevents. The column
  is part of the table, not prose before it -- terse, not explanatory.

**Hypothesis**: V-04 R6 declares schemas in the natural order (1-4, then 5). Schema 5 is
the last row -- an addendum. In V-05 R7, Schema 5 is the first row and the frame: the
execution graph is declared first, and the schema dependencies are declared as properties of
the nodes in that graph. This makes C-26 (sub-step ordering as first-class registered schema)
primary rather than supplementary. The cost-of-omission column provides terse motivation at
declaration time without the prose overhead of V-05 R6. Risk: reordering the Coverage Matrix
could confuse tracers who expect severity/gap/channel before ordering. Mitigation: all five
schemas are still present with complete field values; the order changes, not the content.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix -- Execution Graph)

This coverage matrix is the complete execution graph for this trace. Schema 5 declares the
sequence. Schemas 1-4 declare the contract elements that bind specific nodes in the sequence.
All phases reference only the labels and gates declared here. The Verdict audits compliance
with every row.

| Schema | Content | Declared-at | Referenced-by | Verdict-check | Cost-of-omission |
|--------|---------|-------------|---------------|---------------|-----------------|
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforces all transitions) | VC-5 | Steps run out of order; prerequisites silently skipped |
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (Schema 5 node: declares), Step 3b (enforces), Step 3c G-3 (verifies), Phase 4 (enforces) | VC-1 | Incompatible severity labels across findings; gates unverifiable |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 (audit), SA-TO-SG PROMOTION (promote), Step 3b Source column | VC-2 | SA/SG confused; wrong remediation layer targeted; spec amended when invocation should change |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (Schema 5 node: activates), Phase 4 Amend (enforces) | VC-3 | Amend entries fix wrong layer; finding recurs in next trace |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (Schema 5 node: runs), Phase 4 pre-check (enforces) | VC-4 | Structural gaps advance silently to Amend; incomplete source coverage undetected |

#### Schema 5 -- Sub-Step Ordering (spine of Phase 3)

Declared first because every other schema binds to a named node in this sequence.

| Step | Prerequisite | Schema binding | Produces | Unblocks |
|------|-------------|---------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Schema 1 (declares severity legend) | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Schema 1 (enforces), Schema 2 (enforces Source column) | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Schema 4 (runs all three gates; hard-stop on FAIL) | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Schema 3 (activates channel taxonomy) | Channel taxonomy active | Phase 4 |

#### Schema 1 -- Severity Vocabulary (binds: Step 3a, Step 3b, Step 3c G-3, Phase 4)

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Schema 2 -- Gap Type Taxonomy (binds: Stage 1, SA-TO-SG PROMOTION, Step 3b)

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent | Evaluate at SA-TO-SG PROMOTION; promoted use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through phases with SG label |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation | P3 severity typical |

#### Schema 3 -- Remediation Channel Taxonomy (binds: Step 3d, Phase 4 Amend)

| Channel | Targets | Activated-at |
|---------|---------|-------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Schema 4 -- Enforcement Gate Registry (binds: Step 3c, Phase 4 pre-check)

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Schema 2 governs Source
labels. Schema 1 governs Severity labels. This stage feeds the relay that drives all of
Stage 2.

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without
content rules.
**SG pre-audit**: declared inputs the invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: >=2 distinct Source types. Examine harder if gaps cluster at one layer.

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

**Relay in**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

At the Setup boundary. For every SA gap in the relay:

```
SA-NN -> [result]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock active: promoted gaps use SG label in all downstream phases.

---

#### Phase 1 -- Setup

Confirm inputs:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role gap attribution (role -> gaps): for each role, enumerate constraining gaps.

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

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear. Per-role relay before each artifact section:

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

Phase 3 runs as the sequence declared in Schema 5 (spine of the execution graph). Each
sub-step is a Schema 5 node. The step header states its Schema 5 Prerequisite, its schema
binding, and its Unblocks value. Skipping a sub-step or running out of sequence violates the
Schema 5 Cost-of-omission: prerequisites silently skipped.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 node**: Step 3a
**Schema 5 prerequisite**: Schema 1 declared in Coverage Matrix (satisfied above).
**Schema binding**: Schema 1 (this step declares the severity legend).
**Schema 5 unblocks**: Step 3b.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b -- Findings Table

**Schema 5 node**: Step 3b
**Schema 5 prerequisite**: Step 3a complete (severity legend declared above).
**Schema binding**: Schema 1 (enforce P1/P2/P3), Schema 2 (enforce Source labels).
**Schema 5 unblocks**: Step 3c.

Merge all gaps. Use promoted Source labels (Schema 2). Use only P1/P2/P3 (Step 3a):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

---

##### Step 3c -- Enforcement Gates

**Schema 5 node**: Step 3c
**Schema 5 prerequisite**: Step 3b populated (>=2 entries).
**Schema binding**: Schema 4 (run G-1, G-2, G-3; hard-stop on FAIL).
**Schema 5 unblocks**: Step 3d (only if all gates PASS).

Schema 4 Cost-of-omission: structural gaps advance silently to Amend; incomplete source
coverage undetected.

**Hard-stop rule (Schema 4)**: FAIL on any gate BLOCKS Step 3d and Phase 4. Resolve the
failing condition, re-run the gate, confirm PASS before proceeding.

**G-1 Source Diversity Gate** (Schema 4)
- Source types present: [list]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Add missing-layer finding. Re-run G-1.

**G-2 Action Diversity Gate** (Schema 4)
- Same-Source pairs: [list or "none"]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Revise duplicate Actions. Re-run G-2.

**G-3 Severity Completeness Gate** (Schema 4)
- Severity labels in Step 3b: [list]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active. Phase 4 BLOCKED. Relabel entries. Re-run G-3.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

**Schema 5 node**: Step 3d
**Schema 5 prerequisite**: Step 3c all-PASS.
**Schema binding**: Schema 3 (activates channel taxonomy for Phase 4).
**Schema 5 unblocks**: Phase 4.

Activate Schema 3: spec / invocation / artifact / quality.
Every Phase 4 entry requires `[remediation channel: spec / invocation / artifact / quality]`.

Schema 3 Cost-of-omission: Amend entries fix wrong layer; finding recurs in next trace.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check** (hard-stop conditions): G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
All must be PASS. If any = FAIL: Schema 4 hard-stop active. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d (Schema 3): spec / invocation / artifact / quality.

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock)
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

### Verdict (Phase 5 -- Coverage Matrix Audit, Schema-5-Led)

Walk the Coverage Matrix in declaration order (Schema 5 first, then Schemas 1-4). For each
schema, verify the Declared-at, Referenced-by, and Verdict-check columns were honored, with
evidence at each usage site. Schema 5 is audited first because its ordering constraints are
the prerequisite of all other audits.

**VC-5 -- Sub-Step Ordering (Schema 5)** -- audited first as the execution spine:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- Step 3a ran before Step 3b: YES / NO -- transition evidence: [state what made Step 3b valid]
- Step 3b populated before Step 3c ran: YES / NO -- transition evidence: [state what made Step 3c valid]
- Step 3c all-PASS before Step 3d activated: YES / NO -- transition evidence: [state what made Step 3d valid]
- Step 3d activated before Phase 4 began: YES / NO -- transition evidence: [state what made Phase 4 valid]
- VC-5 result: PASS (all YES) / FAIL (any NO)

**VC-1 -- Severity Vocabulary (Schema 1)** -- binds Step 3a, Step 3b, Step 3c G-3, Phase 4:
- Declared before Stage 1: YES / NO
- Step 3a (Schema 5 node: declares): legend produced with P1/P2/P3 -- YES / NO
- Step 3b (enforces): all entries use only P1/P2/P3 -- YES / NO -- labels used: [list]
- Step 3c G-3 (verifies): severity completeness gate ran -- YES / NO -- G-3 result: [PASS/FAIL]
- Phase 4 (enforces): Amend entries use declared severity only -- YES / NO
- Labels outside P1/P2/P3 found anywhere: [list or "none"]
- VC-1 result: PASS / FAIL

**VC-2 -- Gap Type Taxonomy (Schema 2)** -- binds Stage 1, SA-TO-SG PROMOTION, Step 3b:
- Declared before Stage 1: YES / NO
- Stage 1: only SA/SG/EG/QO used -- YES / NO
- SA-TO-SG PROMOTION ran: YES / NO -- promoted gaps: [list]
- SA labels appearing after promotion for promoted gaps: [list or "none"]
- Step 3b Source column: only SA/SG/EG/QO -- YES / NO
- VC-2 result: PASS / FAIL

**VC-3 -- Remediation Channel Taxonomy (Schema 3)** -- binds Step 3d, Phase 4:
- Declared before Stage 1: YES / NO
- Step 3d (Schema 5 node: activates): channel taxonomy activated -- YES / NO
- Phase 4 (enforces): all Amend entries include channel field -- YES / NO
- Channels used in Phase 4: [list] -- all from declared taxonomy: YES / NO
- VC-3 result: PASS / FAIL

**VC-4 -- Enforcement Gate Registry (Schema 4)** -- binds Step 3c, Phase 4 pre-check:
- Declared before Stage 1: YES / NO
- Step 3c (Schema 5 node: runs gates): G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
- Phase 4 pre-check (enforces): Phase 4 entered while any gate = FAIL: YES (violation) / NO (clean)
- VC-4 result: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
