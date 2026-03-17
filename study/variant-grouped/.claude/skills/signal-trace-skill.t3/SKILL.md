---
name: signal-trace-skill
description: "Hand-compile a skill execution before building it. Given a skill spec and a test invocation, trace the 4-phase lifecycle (setup, execute, findings, amend) step by step -- producing the expected artifact as if the skill had run. Read the spec. Simulate setup (auto-detect from repo context). Run each stock role through their lens. Synthesize findings into the artifact. List 3 amend options. Deliver a verdict: useful or needs redesign? The hand-compiled artifact becomes the scenario baseline for testing. Findings feed back to the skill spec before implementation.
"
allowed-tools: [Read, Write, Glob, Grep]
param_set: lean
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