---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 1
rubric: trace-skill-rubric-v12-2026-03-15.md
---

# trace-skill -- Variations v12 R1 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

v12 entry state: R8 V-05 achieves C-01 through C-09 PASS under v12. C-10 is the only gap.
C-10 v12 sharpens the pass condition from v11: "bijection satisfied" as a claim is PARTIAL.
Full PASS requires explicit enumeration of both directions:

- Direction (a): For each Coverage Matrix row, name the specific phase and step referencing it.
- Direction (b): For each schema reference in any execution phase, name the matrix row that
  registers it.

R8 V-05 contains no Direction (a) or Direction (b) enumeration -- the Coverage Matrix's
Referenced-by column names sites, but no step enumerates matrix-row -> phase mapping explicitly,
and no step traces phase-schema references back to matrix rows. The Verdict compliance ledger
proves schema adherence at each site but does not produce the bijection as a named audit step
with enumerated entries.

v12 R1 axes:

- **Bijection audit block (Direction A)**: Add a standalone "Coverage Matrix Bijection -- Direction A"
  step before Stage 1 that enumerates, for each matrix row, every phase/step it is referenced at.
  Satifies the "for each matrix row -> phase/step" direction. Partial C-10 path.
- **Phase schema footprint log (Direction B)**: Add a per-phase "Schema footprint" log embedded
  in each phase that records every schema-reference made and names its matrix row. The Verdict
  assembles these into a Direction B enumeration. Partial C-10 path.
- **Biconditional framing for bijection (canonical form)**: Rewrite the Coverage Matrix preamble
  and the Verdict's bijection step using the v12 canonical biconditional form. The bijection
  invariant is stated as "Schema X is in the Coverage Matrix if and only if it is referenced by
  at least one execution phase." The closed-world check is named and structured, but relies on
  the ledger rows as proxies -- not full enumeration. PARTIAL C-10 path.
- **Combined: Direction A + Direction B enumeration** (full C-10 path): Both directions walked
  explicitly. A pre-Stage-1 Direction-A table and a Verdict Direction-B table, each enumerating
  the mapping in full. The bijection claim follows from the two tables, not as an assertion.
- **Combined: Direction A + Direction B + Role Closed-World Audit (v13 preview)**: Extends the
  closed-world invariant from the Coverage Matrix to the Role-Schema Binding Summary. Adds a
  "Role Closed-World Audit" in the Verdict: (a) every declared role has at least one
  schema-governed action in Execute; (b) every role appearing in Execute has a Binding Summary
  entry. Pre-positions for v13 open question.

Single-axis selections: Bijection audit block (V-01), Phase schema footprint log (V-02),
Biconditional framing (V-03). Combined: A+B enumeration (V-04), A+B+Role closed-world (V-05).

All five v12 variations inherit the full V-05 R8 architecture:
- Coverage Matrix with Role-binding column (C-08 PASS)
- Role-Schema Binding Summary before Stage 2 (C-08 PASS)
- Compliance ledger with pre-filled Expected behavior (C-09 PASS)
- Per-role adherence rows in VC-1 and VC-2 (C-08 PASS)
- Assertion-first invariant phrasing throughout (C-09 biconditional PASS)
- Hard-stop BLOCKED language on gate FAIL (C-05 PASS)
- SA-TO-SG PROMOTION as a named lifecycle event (C-04 PASS)

---

## V-01 -- Single axis: Bijection audit block (Direction A enumeration before Stage 1)

**Axis**: Bijection audit block -- after the Coverage Matrix is declared and before Stage 1
runs, a standalone "Closed-World Verification -- Direction A" block enumerates, for each
Coverage Matrix row, every specific phase and step where that schema is referenced. The block
produces a two-column table: Schema | Referenced at (phase/step name). This is the Direction A
walk required by v12 C-10. Direction B is not covered by this axis -- no per-phase footprint
log. Biconditional form is used for the Direction A claim. The Verdict records Direction A
enumeration status but does not add Direction B rows.

**Hypothesis**: The R8 V-05 Coverage Matrix lists Referenced-by values but the table is
declarative -- it tells the tracer what sites exist, it does not enumerate the mapping
backward (matrix row -> site). A reader can check Referenced-by against phases, but the trace
itself does not perform that check. Adding a Direction A block makes the enumeration an
artifact of the trace, not a check the reader performs mentally. This satisfies the v12 C-10
Direction (a) requirement. C-10 remains PARTIAL because Direction B (phase -> matrix row) is
absent. C-01 through C-09 are fully inherited from V-05 R8 and are not degraded.

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
G-3 = PASS before Phase 4 begins.

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

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

**Invariant (biconditional form)**: Schema X is in the Coverage Matrix if and only if it is
referenced by at least one execution phase. A matrix entry with no downstream reference is an
orphan entry; its presence is a trace defect. A schema referenced in any phase with no matrix
entry is an undeclared reference; its presence is a trace defect.

Direction A enumerates the forward mapping: for each Coverage Matrix row, name the specific
phase and step where it is referenced. This step runs after the Coverage Matrix is declared and
before Stage 1 begins. Orphan entries found here are named as trace defects, not silently omitted.

| Schema | Matrix row registered | Referenced at -- Phase and Step (enumerate all) | Orphan? |
|--------|-----------------------|--------------------------------------------------|---------|
| Schema 1 | YES -- Row 1 of Coverage Matrix | Step 3a (severity legend declared); Step 3b (P1/P2/P3 enforced in findings table); Step 3c G-3 (severity completeness verified); Phase 4 Amend (severity labels enforced) | NO |
| Schema 2 | YES -- Row 2 of Coverage Matrix | Stage 1 audit (SA/SG/EG/QO labels); SA-TO-SG PROMOTION (promotion decision); Step 3b Source column (Source labels); Execute role relay (Source label in each relay) | NO |
| Schema 3 | YES -- Row 3 of Coverage Matrix | Step 3d (channel taxonomy activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | YES -- Row 4 of Coverage Matrix | Step 3c (G-1/G-2/G-3 run with explicit PASS/FAIL); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | YES -- Row 5 of Coverage Matrix | Phase 3 sub-steps: Step 3a->3b transition; Step 3b->3c transition; Step 3c->3d transition; Step 3d->Phase 4 transition | NO |

**Direction A result**: All 5 Coverage Matrix rows map to at least one phase/step. No orphan
entries found. Direction A invariant: HOLDS.

**Note**: Direction B (for each schema reference in any phase, name the matrix row) is not
enumerated by this variation. C-10 status is PARTIAL pending Direction B enumeration in the
Verdict.

---

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

**Per-role schema binding and gap attribution**: For each role in `[roles: ...]`, declare its
schema obligations from the Role-Schema Binding Summary, then enumerate its gaps. A role entry
without schema binding declaration is invalid.

```
[role: {{role_name}}]
  Schema 1 binding: [which severity labels apply to this role's EG findings, or "N/A"]
  Schema 2 binding: [which Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

A valid Execute produces: the hand-compiled artifact `{topic}-skill-trace-{date}.md` with every
section the artifact contract requires, and a per-role relay for each role. A role relay with
silent inferences is structurally invalid.

For each role, open its relay before writing the artifact section. The "Schema 2 compliance"
field is required. A role relay without it is structurally invalid.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is a sequence governed by Schema 5. A valid Phase 3 runs the sub-steps in the order
declared in Schema 5 and confirms the Schema 5 prerequisite and transition at each step.

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

A valid findings table uses only Schema 2 Source labels (promoted gaps use SG) and Schema 1
Severity labels (P1/P2/P3). A table with fewer than 2 entries is not a valid findings table.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is now valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).
Schema 5 output: gate results for G-1, G-2, G-3 (all-PASS unblocks Step 3d).

A valid Step 3c records an explicit PASS or FAIL for each invariant. A trace that records FAIL
on any invariant and advances to Step 3d or Phase 4 is structurally invalid.

**G-1 Invariant** (Schema 4 G-1): Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: structural defect. Step 3d and Phase 4 are invalid. Add missing-layer finding.
  Re-check G-1. A trace with G-1 = FAIL cannot advance.

**G-2 Invariant** (Schema 4 G-2): No two same-Source findings share identical Action text.
- Same-Source pairs: [list or "none"]
- G-2 holds: PASS / G-2 violated: FAIL
- If FAIL: structural defect. Revise Action text. Re-check G-2.

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

A valid Amend entry (change):

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

A valid Amend entry (dismissal):

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Direction A Bijection Status)

Fill the compliance ledger completely. One row per usage site declared in the Coverage Matrix
Referenced-by column, plus one per-role adherence row for each role bound by Schema 1 or
Schema 2. "Observed behavior" must name specific values, labels, or transition evidence -- not
a schema-level summary. "Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state what the legend said at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only P1/P2/P3 | [list severity values used in Step 3b table, count of each] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | Severity completeness gate verified against Schema 1 | [state G-3 result and the severity labels it checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role producing EG findings] | EG findings from this role use only P1/P2/P3 | [list severity labels used by this role's EG findings] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used in audit table | [list Source labels used in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label; no SA labels downstream for promoted gaps | [list which SA gaps were promoted; confirm SG label used] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG not SA | [list Source labels in Step 3b table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role name] | Source labels in this role's relay from {SA,SG,EG,QO}; label lock honored | [list Source labels used by this role; confirm against promotion list] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated with spec/invocation/artifact/quality | [state activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every Amend entry includes channel field from declared taxonomy | [list channels used; flag any entry missing the field] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 run with explicit PASS/FAIL results | [state G-1/G-2/G-3 results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Hard-stop honored: Phase 4 entered only after all gates PASS | [state gate values at Phase 4 entry; confirm no FAIL gates present] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1 cross-role) | G-1 verified Source diversity across all roles' contributions | [list Source types present and which roles contributed each type] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b waited for Step 3a completion | [state what made Step 3b eligible] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c waited for Step 3b population | [state transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [state transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 waited for Step 3d channel taxonomy activation | [state transition evidence] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS (including per-role rows) / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS (including per-role rows) / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**C-10 Direction A status**: Enumerated before Stage 1 (see "Closed-World Verification --
Direction A" block above). All 5 matrix rows confirmed with named phase/step references.
Direction A invariant: HOLDS.

**C-10 Direction B status**: NOT ENUMERATED by this variation. C-10 = PARTIAL.

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Phase schema footprint log (Direction B enumeration in Verdict)

**Axis**: Phase schema footprint log -- each execution phase (Stage 1, SA-TO-SG PROMOTION,
Phase 1 Setup, Phase 2 Execute, Steps 3a/3b/3c/3d, Phase 4 Amend) closes with a compact
"Schema footprint" record that lists every schema referenced in that phase and names the
Coverage Matrix row registering it. After Phase 4, the Verdict assembles all footprint
records into a "Closed-World Verification -- Direction B" table: for each schema reference
across all phases, the matrix row is named. Direction A (matrix row -> phase/step) is not
added by this axis.

**Hypothesis**: Direction B is harder to structure than Direction A because phase content is
dynamic -- the schemas referenced in a phase depend on what the tracer produces. A per-phase
"Schema footprint" record at phase-close is the lowest-friction mechanism: the tracer records
schema references at the point of use, then the Verdict assembles the Direction B view. This
is more traceable than a post-hoc Verdict enumeration, because each footprint record is
evidence at its production site. Direction A is absent, so C-10 = PARTIAL. But the footprint
records double as schema-reference evidence for VC checks, potentially strengthening C-09.

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
An entry using a label not in {P1, P2, P3} is structurally invalid. A trace is valid with
respect to Schema 1 if and only if every EG finding produced by every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: A valid Source label in this trace is SA, SG, EG, or QO.
The SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all phases after
SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a label lock violation.

**Schema 3 -- Remediation Channel Taxonomy**: A valid Phase 4 Amend entry includes
`[remediation channel: spec / invocation / artifact / quality]`. A trace is valid with respect
to Schema 3 if and only if every Amend entry names a channel from {spec, invocation, artifact, quality}.

**Schema 4 -- Enforcement Gate Registry**: Three invariants govern this trace. A trace violating
any invariant is structurally invalid and cannot advance:
- Invariant G-1: Step 3b contains >=2 distinct Source types.
- Invariant G-2: No two same-Source findings share identical Action text.
- Invariant G-3: Every Step 3b entry uses only {P1, P2, P3}.
A trace is valid with respect to Schema 4 if and only if G-1 = PASS AND G-2 = PASS AND G-3 = PASS
before Phase 4 begins.

**Schema 5 -- Sub-Step Ordering**: Step 3b is valid if and only if Step 3a has produced a
severity legend. Step 3c is valid if and only if Step 3b has produced >=2 findings. Step 3d is
valid if and only if Step 3c has produced all gates PASS. Phase 4 is valid if and only if
Step 3d has activated the channel taxonomy.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

A valid trace declares every role in the execution sequence here before Stage 2 begins.
A role without explicit schema binding is invalid in this trace.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's EG findings, or "N/A"] | [Source labels this role may produce; label lock rules] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 produces a gap audit table and a relay record. Stage 1 reads only
`{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one source type is structurally
incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

**Schema footprint -- Stage 1 close**:

| Schema referenced in this phase | Matrix row | Usage |
|----------------------------------|------------|-------|
| Schema 2 (Gap Type Taxonomy) | Row 2 | SA/SG/EG/QO labels assigned to each gap |
| Schema 1 (Severity Vocabulary) | Row 1 | P1/P2/P3 severity labels assigned to each gap |

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

A valid Stage 2 carries all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

SA-TO-SG PROMOTION is the designated lifecycle event at the Setup boundary. Its invariant: every
SA gap in the Stage 1 relay is evaluated. A gap a spec-competent invoker can supply promotes to
SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock invariant: a promoted gap using its SA label in any downstream phase is
a structural violation.

**Schema footprint -- SA-TO-SG PROMOTION close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 (Gap Type Taxonomy) | Row 2 | SA gaps evaluated; promoted gaps relabeled SG |

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap attribution
block for each role. A Setup listing roles without schema binding declarations is structurally
incomplete.

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels for this role's EG findings, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

**Schema footprint -- Phase 1 Setup close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 1 (Severity Vocabulary) | Row 1 | Schema 1 binding declared per role |
| Schema 2 (Gap Type Taxonomy) | Row 2 | Schema 2 binding declared per role; promoted gap labels confirmed |

---

#### Phase 2 -- Execute

A valid Execute produces: the artifact `{topic}-skill-trace-{date}.md` and a per-role relay.
The "Schema 2 compliance" field is required in every role relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

**Schema footprint -- Phase 2 Execute close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 (Gap Type Taxonomy) | Row 2 | Source labels used in each role relay |
| Schema 1 (Severity Vocabulary) | Row 1 | Severity labels on EG findings produced by roles |

---

#### Phase 3 -- Findings

Phase 3 is governed by Schema 5. Sub-steps run in the order declared.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.
Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

**Schema footprint -- Step 3a close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 1 (Severity Vocabulary) | Row 1 | P1/P2/P3 legend declared for this trace |
| Schema 5 (Sub-Step Ordering) | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.
Schema 5 output: findings table with >=2 entries (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

**Schema footprint -- Step 3b close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 (Gap Type Taxonomy) | Row 2 | Source column uses only SA/SG/EG/QO |
| Schema 1 (Severity Vocabulary) | Row 1 | Severity column uses only P1/P2/P3 |
| Schema 5 (Sub-Step Ordering) | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).
Schema 5 output: G-1/G-2/G-3 results (all-PASS unblocks Step 3d).

A valid Step 3c records an explicit PASS or FAIL for each invariant.

**G-1 Invariant**: Source types present: [list] -- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: structural defect. Step 3d and Phase 4 invalid. Fix and re-check.

**G-2 Invariant**: Same-Source pairs: [list or "none"] -- G-2 holds: PASS / G-2 violated: FAIL

**G-3 Invariant**: Severity labels present: [list] -- G-3 holds: PASS / G-3 violated: FAIL

Schema 5 transition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

**Schema footprint -- Step 3c close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 4 (Enforcement Gate Registry) | Row 4 | G-1/G-2/G-3 invariants evaluated |
| Schema 5 (Sub-Step Ordering) | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

Schema 5 prerequisite: Step 3c all invariants hold.
Schema 5 output: Schema 3 channel taxonomy active for Phase 4.

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Schema footprint -- Step 3d close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 3 (Remediation Channel Taxonomy) | Row 3 | Channel taxonomy activated |
| Schema 5 (Sub-Step Ordering) | Row 5 | Prerequisite confirmed; transition recorded |

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

A valid Phase 4 begins only when G-1 = PASS, G-2 = PASS, G-3 = PASS.

Gate status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 invariant violated. Phase 4 structurally blocked. Return to Step 3c.

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO -- `{{explain if NO}}`]

Or dismissal:
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

**Schema footprint -- Phase 4 Amend close**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 (Gap Type Taxonomy) | Row 2 | Source label on applied finding; label lock honored |
| Schema 3 (Remediation Channel Taxonomy) | Row 3 | Channel field present in Amend entry |
| Schema 1 (Severity Vocabulary) | Row 1 | Severity label on Amend entry inherits from finding |
| Schema 4 (Enforcement Gate Registry) | Row 4 | Gate status confirmed before Phase 4 entered |

---

### Verdict (Phase 5 -- Compliance Ledger with Direction B Bijection Enumeration)

Fill the compliance ledger. One row per usage site from the Coverage Matrix Referenced-by
column, plus per-role rows for Schema 1 and Schema 2. "Observed behavior" must be specific --
"as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state what the legend said] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only P1/P2/P3 | [list severity values used, count of each] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | Severity completeness gate verified against Schema 1 | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role producing EG findings] | EG findings use only P1/P2/P3 | [list severity labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used | [list Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label | [list which SA gaps promoted; confirm SG downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels in Step 3b table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role name] | Source labels from {SA,SG,EG,QO}; label lock honored | [list Source labels in this relay] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [state activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every Amend entry includes channel field | [list channels used; flag missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1/G-2/G-3 run with explicit results | [state G-1/G-2/G-3 results] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [state gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1 cross-role) | G-1 verified Source diversity across all roles | [list Source types and which roles contributed each] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b waited for Step 3a | [state Schema 5 prerequisite confirmation] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c waited for Step 3b population | [state transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [state transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 waited for Step 3d activation | [state transition evidence] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assemble the Direction B enumeration from the Schema footprint records above. For each schema
reference recorded in any phase, name the Coverage Matrix row registering it. If any schema
reference cannot be traced to a matrix row, it is an undeclared reference -- a trace defect.

**Invariant (biconditional form)**: Schema X is in the Coverage Matrix if and only if it is
referenced by at least one execution phase. Verified below by enumerating every phase-side
reference and confirming its matrix registration.

| Phase / Step | Schema referenced | Matrix row | Registered? |
|--------------|------------------|------------|-------------|
| Stage 1 | Schema 2 (Gap Type Taxonomy) | Row 2 | YES |
| Stage 1 | Schema 1 (Severity Vocabulary) | Row 1 | YES |
| SA-TO-SG PROMOTION | Schema 2 (Gap Type Taxonomy) | Row 2 | YES |
| Phase 1 Setup | Schema 1 (Severity Vocabulary) | Row 1 | YES |
| Phase 1 Setup | Schema 2 (Gap Type Taxonomy) | Row 2 | YES |
| Phase 2 Execute | Schema 2 (Gap Type Taxonomy) | Row 2 | YES |
| Phase 2 Execute | Schema 1 (Severity Vocabulary) | Row 1 | YES |
| Step 3a | Schema 1 (Severity Vocabulary) | Row 1 | YES |
| Step 3a | Schema 5 (Sub-Step Ordering) | Row 5 | YES |
| Step 3b | Schema 2 (Gap Type Taxonomy) | Row 2 | YES |
| Step 3b | Schema 1 (Severity Vocabulary) | Row 1 | YES |
| Step 3b | Schema 5 (Sub-Step Ordering) | Row 5 | YES |
| Step 3c | Schema 4 (Enforcement Gate Registry) | Row 4 | YES |
| Step 3c | Schema 5 (Sub-Step Ordering) | Row 5 | YES |
| Step 3d | Schema 3 (Remediation Channel Taxonomy) | Row 3 | YES |
| Step 3d | Schema 5 (Sub-Step Ordering) | Row 5 | YES |
| Phase 4 Amend | Schema 2 (Gap Type Taxonomy) | Row 2 | YES |
| Phase 4 Amend | Schema 3 (Remediation Channel Taxonomy) | Row 3 | YES |
| Phase 4 Amend | Schema 1 (Severity Vocabulary) | Row 1 | YES |
| Phase 4 Amend | Schema 4 (Enforcement Gate Registry) | Row 4 | YES |

Undeclared references found: NONE.

**Direction B result**: All schema references in all phases trace to registered matrix rows.
Direction B invariant: HOLDS.

**C-10 Direction A status**: NOT ENUMERATED by this variation. C-10 = PARTIAL.
**C-10 Direction B status**: Enumerated above. All references confirmed registered.

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Biconditional framing for C-10 (canonical invariant form without enumeration)

**Axis**: Biconditional framing -- the Coverage Matrix preamble and the Verdict are rewritten
so that the closed-world invariant is stated in the v12 canonical biconditional form: "Schema X
is in the Coverage Matrix if and only if it is referenced by at least one execution phase."
A dedicated "Bijection Invariant" section in the Verdict states the biconditional and attempts
to verify it using the ledger rows as evidence proxies (referencing VC row Site result values).
This is the most minimal structural addition: the invariant is named and the claim is made in
canonical form. However, the Verdict does not enumerate both directions as separate tables --
it relies on the VC rows collectively satisfying the biconditional. Under v12, this is
explicitly PARTIAL (an assertion without enumeration fails the v12 C-10 pass condition).

**Hypothesis**: The v12 rubric says "bijection satisfied" as a claim is PARTIAL -- but a
biconditional framing that delegates verification to existing VC rows may be scored differently
than a bare assertion. The hypothesis: if the biconditional is stated with named evidence
(e.g., "VC-1 PASS confirms Schema 1 is referenced by Step 3a, 3b, 3c, Phase 4"), the claim
is partially evidenced. This variation tests whether canonical form + partial evidence reaches
PARTIAL rather than FAIL, and establishes the canonical invariant pattern that V-04 and V-05
will use as the outer wrapper for their explicit enumerations.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority. A Coverage Matrix entry is valid if and only if the schema it registers is
referenced in at least one downstream phase. A schema referenced in any phase is valid if and
only if it appears in the Coverage Matrix. These two directions together constitute the
closed-world bijection invariant for this trace.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Bijection invariant (canonical form)**: Schema X is in the Coverage Matrix if and only if it
is referenced by at least one execution phase. This invariant has two directions:
- Direction A (matrix -> phase): every matrix row is referenced by at least one phase/step.
- Direction B (phase -> matrix): every schema referenced in any phase has a matrix row.
Both directions are verified in the Verdict Bijection Invariant section. An orphan matrix entry
(Direction A fails) or an undeclared reference (Direction B fails) is a trace defect.

**Schema 1 -- Severity Vocabulary**: A trace is valid with respect to Schema 1 if and only if
every EG finding produced by every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: The SA-TO-SG label lock invariant: a promoted SA gap uses
the SG label in all phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is
a label lock violation.

**Schema 3 -- Remediation Channel Taxonomy**: A trace is valid with respect to Schema 3 if and
only if every Amend entry names a channel from {spec, invocation, artifact, quality}.

**Schema 4 -- Enforcement Gate Registry**: A trace is valid with respect to Schema 4 if and
only if G-1 = PASS AND G-2 = PASS AND G-3 = PASS before Phase 4 begins. A trace violating any
invariant is structurally invalid and cannot advance.

**Schema 5 -- Sub-Step Ordering**: Step 3b is valid if and only if Step 3a complete. Step 3c
is valid if and only if Step 3b has >=2 entries. Step 3d is valid if and only if all gates PASS.
Phase 4 is valid if and only if Step 3d activated the channel taxonomy.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels for EG findings, or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`], [diversity: `{{status}}`].

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why]
```

```
[SA remaining: {{n}}] [SG from promotion: {{n}}] [SG original: {{n}}]
```

---

#### Phase 1 -- Setup

- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

```
[role: {{name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Schema 2 compliance field required in every relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels: [list] -- all SA/SG/EG/QO: YES / NO
- SA/SG gaps: [list or "none -- confirmed"]
- Produced: [artifact content]
- EG gaps: [EG-NN or "none"]

**Execute carry-forward**: [artifact: `{{path}}`], [EG added: `{{list}}`].

---

#### Phase 3 -- Findings

##### Step 3a

| Label | Definition for this trace | Threshold |
|-------|--------------------------|-----------|
| P1 | [blocker] | Resolve before Findings close |
| P2 | [quality] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a -> Step 3b.

##### Step 3b

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries -> Step 3c.

##### Step 3c

**G-1**: Source types: [list] -- PASS / FAIL. If FAIL: structurally invalid. Phase 4 BLOCKED.
**G-2**: Same-Source pairs: [list or "none"] -- PASS / FAIL. If FAIL: structurally invalid.
**G-3**: Severity labels: [list] -- PASS / FAIL. If FAIL: structurally invalid.

Schema 5 transition: all PASS -> Step 3d.

##### Step 3d

Channel taxonomy (Schema 3) active. Every Amend entry requires channel field.

Schema 5 transition: channel active -> Phase 4.

---

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS].

---

#### Phase 4 -- Amend

Gates: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`. If any FAIL: Phase 4 BLOCKED.

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section changed: ]
- [change: ]
- [source confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Bijection Invariant)

Fill the ledger. "Observed behavior: as expected" is invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what the legend stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 | [list severity values, count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate verified | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use only P1/P2/P3 | [list labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG | [which SA promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels SA/SG/EG/QO; lock honored | [list Source labels] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field present | [channels used; any missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit results | [results recorded] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all PASS | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity verified across roles | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for 3a | [prerequisite confirmation] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for 3d | [transition evidence] | PASS / FAIL |

**Bijection Invariant (C-10) -- canonical form**:

Schema X is in the Coverage Matrix if and only if it is referenced by at least one execution phase.

**Direction A claim** (matrix -> phase): Each matrix row has at least one VC row with Site result
= PASS, confirming it was referenced in at least one phase. Evidence by schema:
- Schema 1: VC-1 rows cover Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend -- all PASS. Row 1 referenced.
- Schema 2: VC-2 rows cover Stage 1, SA-TO-SG PROMOTION, Step 3b, role relays -- all PASS. Row 2 referenced.
- Schema 3: VC-3 rows cover Step 3d, Phase 4 Amend -- all PASS. Row 3 referenced.
- Schema 4: VC-4 rows cover Step 3c, Phase 4 pre-check, G-1 cross-role -- all PASS. Row 4 referenced.
- Schema 5: VC-5 rows cover four transitions -- all PASS. Row 5 referenced.

**Direction B claim** (phase -> matrix): All VC rows map to schemas that have Coverage Matrix
entries. No VC row references a schema not in the matrix.

**Bijection status**: CLAIMED SATISFIED -- both directions verified by ledger evidence.

**Note**: Under v12 rubric C-10, this biconditional claim without explicit enumeration tables
is PARTIAL. Direction A verification uses VC row evidence as proxy, not a named enumeration.
Direction B verification is an assertion, not an enumeration. Full PASS requires V-04 or V-05.

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: Direction A enumeration + Direction B enumeration (full C-10 path)

**Axes**:
- Bijection audit block (from V-01): A "Closed-World Verification -- Direction A" block runs
  after the Coverage Matrix and before Stage 1. It enumerates, for each matrix row, every
  specific phase and step where the schema is referenced. Orphan entries are named as defects.
- Phase schema footprint log (from V-02): Each execution phase closes with a "Schema footprint"
  record listing every schema referenced in that phase and its matrix row. The Verdict assembles
  these into a "Closed-World Verification -- Direction B" table enumerating all phase-side
  references back to matrix rows.
- Biconditional framing (from V-03): The Coverage Matrix preamble states the biconditional
  invariant. The Verdict Bijection section uses biconditional form for both directions.
  The bijection claim follows from the two enumeration tables, not as an assertion.

**Hypothesis**: V-01 achieves C-10 Direction A PASS; V-02 achieves C-10 Direction B PASS;
V-03 establishes canonical biconditional framing but is PARTIAL because it lacks enumeration.
V-04 integrates all three: Direction A table + Direction B table (from footprint records) +
biconditional outer framing. The claim "bijection satisfied" is backed by two explicit
enumeration tables, each walking one direction. This should satisfy v12 C-10 PASS. Risk: the
combined prompt is the longest yet; a tracer filling footprint records mechanically may produce
a Direction B table that merely lists what was instructed. Mitigation: each footprint record is
produced at phase-close when the phase content is fresh; the tracer must list what was actually
referenced, not a pre-filled template.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority. A Coverage Matrix entry is valid if and only if the schema it registers is referenced
in at least one downstream phase. A schema referenced in any phase is valid if and only if it
appears in the Coverage Matrix. Both directions together are the closed-world bijection
invariant. Both are verified by explicit enumeration in this trace.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Bijection invariant (canonical biconditional form)**: Schema X is in the Coverage Matrix if
and only if it is referenced by at least one execution phase. This trace verifies both
directions by explicit enumeration:
- Direction A (enumeration): for each matrix row, every phase/step referencing it is named.
- Direction B (enumeration): for each schema reference in any execution phase, the matrix row
  registering it is named.
An orphan matrix entry (no phase references it) is a trace defect named at Direction A check.
An undeclared reference (no matrix row registers it) is a trace defect named at Direction B check.

**Schema 1 -- Severity Vocabulary**: A trace is valid with respect to Schema 1 if and only if
every EG finding produced by every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: The SA-TO-SG label lock invariant: a promoted SA gap uses
the SG label in all phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label
is a label lock violation and renders the trace structurally invalid at that point.

**Schema 3 -- Remediation Channel Taxonomy**: A trace is valid with respect to Schema 3 if and
only if every Amend entry names a channel from {spec, invocation, artifact, quality}.

**Schema 4 -- Enforcement Gate Registry**: A trace is valid with respect to Schema 4 if and
only if G-1 = PASS AND G-2 = PASS AND G-3 = PASS before Phase 4 begins.

**Schema 5 -- Sub-Step Ordering**: Step 3b is valid if and only if Step 3a complete. Step 3c
is valid if and only if Step 3b has >=2 entries. Step 3d is valid if and only if all gates
PASS. Phase 4 is valid if and only if Step 3d activated the channel taxonomy.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

This enumeration runs before Stage 1. For each Coverage Matrix row, name every phase and step
where that schema is referenced. An entry with no references is an orphan -- a trace defect.

| Schema | Matrix row | Referenced at -- Phase and Step (enumerate all) | Orphan? |
|--------|-----------|-------------------------------------------------|---------|
| Schema 1 -- Severity Vocabulary | Row 1 | Step 3a (severity legend declared); Step 3b (P1/P2/P3 enforced); Step 3c G-3 (severity completeness verified); Phase 4 Amend (severity labels enforced); Role relays in Phase 2 Execute (EG finding severity labels) | NO |
| Schema 2 -- Gap Type Taxonomy | Row 2 | Stage 1 audit (SA/SG/EG/QO labels); SA-TO-SG PROMOTION (promotion decisions); Step 3b Source column; Phase 2 Execute role relay (Schema 2 compliance field) | NO |
| Schema 3 -- Remediation Channel Taxonomy | Row 3 | Step 3d (channel taxonomy activated); Phase 4 Amend (channel field required in each entry) | NO |
| Schema 4 -- Enforcement Gate Registry | Row 4 | Step 3c (G-1/G-2/G-3 run with explicit PASS/FAIL); Phase 4 pre-check (gate status confirmed before entry) | NO |
| Schema 5 -- Sub-Step Ordering | Row 5 | Phase 3 Step 3a->3b transition; Step 3b->3c transition; Step 3c->3d transition; Step 3d->Phase 4 transition | NO |

**Direction A result**: 5 of 5 matrix rows map to at least one phase/step. No orphan entries.
Direction A invariant: HOLDS.

---

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels for EG findings, or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

**Schema footprint -- Stage 1**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | SA/SG/EG/QO labels assigned |
| Schema 1 | Row 1 | P1/P2/P3 severity labels assigned |

---

### Stage 2 -- Hand-Compilation

Relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`], [diversity: `{{status}}`].

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [description]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why]
```

```
[SA remaining: {{n}}] [SG from promotion: {{n}}] [SG original: {{n}}]
```

**Schema footprint -- SA-TO-SG PROMOTION**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | SA gaps evaluated; promoted gaps relabeled SG |

---

#### Phase 1 -- Setup

- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

```
[role: {{name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{n}}`], [SG total: `{{n}}`].

**Schema footprint -- Phase 1 Setup**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 1 | Row 1 | Schema 1 binding declared per role |
| Schema 2 | Row 2 | Schema 2 binding declared; promoted labels confirmed |

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Schema 2 compliance field required per relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels: [list] -- all SA/SG/EG/QO: YES / NO
- SA/SG gaps: [list or "none -- confirmed"]
- Produced: [artifact content]
- EG gaps: [EG-NN or "none"]

**Execute carry-forward**: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | Source labels in each role relay |
| Schema 1 | Row 1 | Severity labels on EG findings per role |

---

#### Phase 3 -- Findings

##### Step 3a

| Label | Definition for this trace | Threshold |
|-------|--------------------------|-----------|
| P1 | [blocker definition] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

**Schema footprint -- Step 3a**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 1 | Row 1 | P1/P2/P3 legend declared |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3b

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries -> Step 3c valid.

**Schema footprint -- Step 3b**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | Source column: SA/SG/EG/QO only |
| Schema 1 | Row 1 | Severity column: P1/P2/P3 only |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3c

**G-1**: Source types: [list] -- G-1 holds: PASS / violated: FAIL
If FAIL: structurally invalid. Phase 4 BLOCKED until resolved.

**G-2**: Same-Source pairs: [list or "none"] -- G-2 holds: PASS / violated: FAIL

**G-3**: Severity labels: [list] -- G-3 holds: PASS / violated: FAIL

Schema 5 transition: all PASS -> Step 3d valid.

**Schema footprint -- Step 3c**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 4 | Row 4 | G-1/G-2/G-3 invariants evaluated |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3d

Channel taxonomy (Schema 3) activated. Phase 4 Amend entries require channel field.

Schema 5 transition: channel active -> Phase 4 valid.

**Schema footprint -- Step 3d**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 3 | Row 3 | Channel taxonomy activated |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS].

---

#### Phase 4 -- Amend

Gates: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`. If any FAIL: Phase 4 BLOCKED.

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section changed: ]
- [change: ]
- [source confirmed: YES / NO]

Or dismissal:
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

**Schema footprint -- Phase 4 Amend**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | Source label on Amend finding; label lock honored |
| Schema 3 | Row 3 | Channel field present in Amend entry |
| Schema 1 | Row 1 | Severity label inherits from finding (P1/P2/P3) |
| Schema 4 | Row 4 | Gate status confirmed before Phase 4 entry |

---

### Verdict (Phase 5 -- Compliance Ledger with Full Bijection Enumeration)

Fill the compliance ledger. "Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | P1/P2/P3 legend declared | [what the legend stated] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries P1/P2/P3 | [list severity values, count] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | Completeness gate verified | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role producing EG] | EG findings P1/P2/P3 only | [list labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role] | Source labels valid; lock honored | [list Source labels] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Channel field in every entry | [channels used; any missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1/G-2/G-3 explicit results | [results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b G-1 cross-role | Source diversity across roles | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b waited for 3a | [prerequisite confirmation] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c waited for 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d waited for 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 waited for 3d | [transition evidence] | PASS / FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assemble from the Schema footprint records above. For each schema reference recorded in any
phase, name the Coverage Matrix row. Undeclared references are trace defects.

| Phase / Step | Schema referenced | Matrix row | Registered? |
|--------------|------------------|------------|-------------|
| Stage 1 | Schema 2 | Row 2 | YES |
| Stage 1 | Schema 1 | Row 1 | YES |
| SA-TO-SG PROMOTION | Schema 2 | Row 2 | YES |
| Phase 1 Setup | Schema 1 | Row 1 | YES |
| Phase 1 Setup | Schema 2 | Row 2 | YES |
| Phase 2 Execute | Schema 2 | Row 2 | YES |
| Phase 2 Execute | Schema 1 | Row 1 | YES |
| Step 3a | Schema 1 | Row 1 | YES |
| Step 3a | Schema 5 | Row 5 | YES |
| Step 3b | Schema 2 | Row 2 | YES |
| Step 3b | Schema 1 | Row 1 | YES |
| Step 3b | Schema 5 | Row 5 | YES |
| Step 3c | Schema 4 | Row 4 | YES |
| Step 3c | Schema 5 | Row 5 | YES |
| Step 3d | Schema 3 | Row 3 | YES |
| Step 3d | Schema 5 | Row 5 | YES |
| Phase 4 Amend | Schema 2 | Row 2 | YES |
| Phase 4 Amend | Schema 3 | Row 3 | YES |
| Phase 4 Amend | Schema 1 | Row 1 | YES |
| Phase 4 Amend | Schema 4 | Row 4 | YES |

Undeclared references: NONE.

**Direction B result**: All phase-side schema references trace to registered matrix rows.
Direction B invariant: HOLDS.

---

**Bijection closed-world summary**:

Schema X is in the Coverage Matrix if and only if it is referenced by at least one execution phase.

| Direction | Claim | Evidence | Result |
|-----------|-------|----------|--------|
| Direction A: matrix -> phase | Every matrix row has at least one phase/step reference | Enumeration table above -- all 5 rows confirmed with named phase/step references | HOLDS |
| Direction B: phase -> matrix | Every phase-side schema reference has a matrix row | Direction B table assembled from footprint records -- all references confirmed registered | HOLDS |

**Bijection invariant: SATISFIED -- both directions enumerated with named evidence.**
**C-10 result: PASS** (both directions enumerated explicitly; no orphan entries; no undeclared references).

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: Direction A + Direction B + Role Closed-World Audit (v13 preview)

**Axes**:
- All of V-04 (Direction A enumeration + Direction B footprint/assembly + biconditional framing).
- Role Closed-World Audit (v13 preview): After the Coverage Matrix bijection is verified, a
  "Role Closed-World Audit" in the Verdict extends the closed-world invariant to the Role-Schema
  Binding Summary:
  - (a) Every role declared in the Binding Summary produces at least one schema-governed action
    in Phase 2 Execute (no silent roles -- a declared role with no observable schema-governed
    action is a binding violation).
  - (b) Every role appearing in Phase 2 Execute has a Role-Schema Binding Summary entry (no
    undeclared roles -- a role relay written without a Binding Summary row is structurally
    invalid).
  This makes the Role-Schema Binding Summary its own closed-world audit surface, mirroring
  the Coverage Matrix invariant at role granularity, as proposed in the v12 open question.

**Hypothesis**: V-04 achieves C-10 PASS by explicit enumeration of both bijection directions.
V-05 adds the v13 preview: the Role Closed-World Audit. This tests whether the role-level
bijection can be specified and verified within the same prompt structure. The risk is that
"schema-governed action" is harder to define precisely than "schema reference in a phase" --
a role relay that includes a Schema 2 compliance field might be considered schema-governed
even if the field is vacuous. The hypothesis: if the Binding Summary's Role Closed-World Audit
uses the same enumeration-first structure as the Coverage Matrix bijection, the claim is
equally well-evidenced and the v13 criterion can be stated precisely. V-05 also tests whether
C-09 (invariant-witness biconditional) remains intact when a second closed-world invariant is
added -- the biconditional form should extend naturally to the role-level invariant.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority. A Coverage Matrix entry is valid if and only if the schema it registers is referenced
in at least one downstream phase. A schema referenced in any phase is valid if and only if it
appears in the Coverage Matrix. Both directions together are the closed-world bijection
invariant for the Coverage Matrix. Both are verified by explicit enumeration in this trace.

A second closed-world invariant governs the Role-Schema Binding Summary: every role declared
in the Binding Summary produces at least one schema-governed action in Execute (no silent roles),
and every role appearing in Execute has a Binding Summary entry (no undeclared roles). The
Binding Summary bijection is verified by explicit enumeration in the Verdict.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Coverage Matrix bijection invariant (canonical biconditional form)**: Schema X is in the
Coverage Matrix if and only if it is referenced by at least one execution phase. Verified by
Direction A enumeration (before Stage 1) and Direction B enumeration (in the Verdict, assembled
from per-phase Schema footprint records). Orphan entries and undeclared references are trace
defects named at their respective enumeration steps.

**Role-Schema Binding Summary bijection invariant (canonical biconditional form)**: Role R is
in the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. "Schema-governed action" means: an action that uses a label from Schema 1 or Schema 2
as declared in the Binding Summary for that role. A declared role that produces no such action
in Execute is a silent role -- a Binding Summary defect. A role appearing in Execute with no
Binding Summary entry is an undeclared role -- a structural defect. Both directions verified
by explicit enumeration in the Verdict Role Closed-World Audit.

**Schema 1 -- Severity Vocabulary**: A trace is valid with respect to Schema 1 if and only if
every EG finding produced by every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: The SA-TO-SG label lock invariant: a promoted SA gap uses
the SG label in all phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label
is a label lock violation.

**Schema 3 -- Remediation Channel Taxonomy**: A trace is valid with respect to Schema 3 if and
only if every Amend entry names a channel from {spec, invocation, artifact, quality}.

**Schema 4 -- Enforcement Gate Registry**: A trace is valid with respect to Schema 4 if and
only if G-1 = PASS AND G-2 = PASS AND G-3 = PASS before Phase 4 begins.

**Schema 5 -- Sub-Step Ordering**: Step 3b is valid if and only if Step 3a complete. Step 3c
is valid if and only if Step 3b has >=2 entries. Step 3d is valid if and only if all gates
PASS. Phase 4 is valid if and only if Step 3d activated the channel taxonomy.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

Runs before Stage 1. For each Coverage Matrix row, name every phase and step referencing it.
Orphan entries are named as trace defects.

| Schema | Matrix row | Referenced at -- Phase and Step (enumerate all) | Orphan? |
|--------|-----------|-------------------------------------------------|---------|
| Schema 1 -- Severity Vocabulary | Row 1 | Step 3a (legend declared); Step 3b (P1/P2/P3 enforced); Step 3c G-3 (completeness verified); Phase 4 Amend (labels enforced); Role relays in Phase 2 (EG finding severity) | NO |
| Schema 2 -- Gap Type Taxonomy | Row 2 | Stage 1 audit (SA/SG/EG/QO labels); SA-TO-SG PROMOTION; Step 3b Source column; Phase 2 Execute relay (Schema 2 compliance) | NO |
| Schema 3 -- Remediation Channel Taxonomy | Row 3 | Step 3d (taxonomy activated); Phase 4 Amend (channel field) | NO |
| Schema 4 -- Enforcement Gate Registry | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 -- Sub-Step Ordering | Row 5 | Step 3a->3b transition; Step 3b->3c transition; Step 3c->3d transition; Step 3d->Phase 4 transition | NO |

**Direction A result**: 5 of 5 matrix rows confirmed. No orphan entries. Direction A: HOLDS.

---

#### Role-Schema Binding Summary

A valid trace declares every role in the execution sequence here before Stage 2 begins.
"Schema-governed action" means: an action in Execute that uses Schema 1 or Schema 2 labels
as declared in this Binding Summary for that role. A role without explicit schema binding is
invalid. One row per role found in the spec.

| Role | Schema 1 binding | Schema 2 binding | Schema-governed action in Execute | Notes |
|------|-----------------|-----------------|----------------------------------|-------|
| [role from spec] | [severity labels for EG findings, or "N/A"] | [Source labels; label lock rules] | [what constitutes a schema-governed action for this role -- the minimum observable evidence] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

**Schema footprint -- Stage 1**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | SA/SG/EG/QO labels assigned |
| Schema 1 | Row 1 | P1/P2/P3 severity labels assigned |

---

### Stage 2 -- Hand-Compilation

Relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`], [diversity: `{{status}}`].

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [description]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why]
```

```
[SA remaining: {{n}}] [SG from promotion: {{n}}] [SG original: {{n}}]
```

**Schema footprint -- SA-TO-SG PROMOTION**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | SA gaps evaluated; promoted gaps relabeled SG |

---

#### Phase 1 -- Setup

- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

```
[role: {{name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Schema footprint -- Phase 1 Setup**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 1 | Row 1 | Schema 1 binding declared per role |
| Schema 2 | Row 2 | Schema 2 binding declared; promoted labels confirmed |

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Schema 2 compliance field required per relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- Schema-governed action evidence: [name at least one action that used Schema 1 or Schema 2
  labels as declared in the Binding Summary for this role -- this is the Binding Summary
  bijection evidence for this role's Direction A check]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content]
- EG gaps: [EG-NN or "none"]

**Execute carry-forward**: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | Source labels in each role relay |
| Schema 1 | Row 1 | Severity labels on EG findings per role |

---

#### Phase 3 -- Findings

##### Step 3a

| Label | Definition for this trace | Threshold |
|-------|--------------------------|-----------|
| P1 | [blocker definition] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

**Schema footprint -- Step 3a**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 1 | Row 1 | P1/P2/P3 legend declared |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3b

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries -> Step 3c valid.

**Schema footprint -- Step 3b**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | Source column: SA/SG/EG/QO |
| Schema 1 | Row 1 | Severity column: P1/P2/P3 |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3c

**G-1**: Source types: [list] -- G-1 holds: PASS / violated: FAIL (if FAIL: Phase 4 BLOCKED)
**G-2**: Same-Source pairs: [list or "none"] -- G-2 holds: PASS / violated: FAIL
**G-3**: Severity labels: [list] -- G-3 holds: PASS / violated: FAIL

Schema 5 transition: all PASS -> Step 3d valid.

**Schema footprint -- Step 3c**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 4 | Row 4 | G-1/G-2/G-3 invariants evaluated |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

##### Step 3d

Channel taxonomy (Schema 3) activated. Phase 4 requires channel field in every Amend entry.

Schema 5 transition: channel active -> Phase 4 valid.

**Schema footprint -- Step 3d**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 3 | Row 3 | Channel taxonomy activated |
| Schema 5 | Row 5 | Prerequisite confirmed; transition recorded |

---

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS].

---

#### Phase 4 -- Amend

Gates: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`. If any FAIL: Phase 4 BLOCKED.

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section changed: ]
- [change: ]
- [source confirmed: YES / NO]

Or dismissal:
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

**Schema footprint -- Phase 4 Amend**:

| Schema referenced | Matrix row | Usage |
|-------------------|------------|-------|
| Schema 2 | Row 2 | Source label on finding; label lock honored |
| Schema 3 | Row 3 | Channel field present |
| Schema 1 | Row 1 | Severity inherits from finding |
| Schema 4 | Row 4 | Gate status confirmed before entry |

---

### Verdict (Phase 5 -- Compliance Ledger + Full Bijection Enumeration + Role Closed-World Audit)

Fill the compliance ledger. "Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | P1/P2/P3 legend declared | [what the legend stated] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries P1/P2/P3 | [list severity values, count] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | Completeness gate verified | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All entries P1/P2/P3 | [list severity values] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role] | EG findings P1/P2/P3 only | [list labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role] | Source labels valid; lock honored | [list Source labels] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Channel field in every entry | [channels used; any missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1/G-2/G-3 explicit results | [results at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b G-1 cross-role | Source diversity across roles | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b waited for 3a | [prerequisite confirmation] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c waited for 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d waited for 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 waited for 3d | [transition evidence] | PASS / FAIL |

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assembled from Schema footprint records. For each schema reference in any phase, the matrix
row is named. Undeclared references are trace defects.

| Phase / Step | Schema referenced | Matrix row | Registered? |
|--------------|------------------|------------|-------------|
| Stage 1 | Schema 2 | Row 2 | YES |
| Stage 1 | Schema 1 | Row 1 | YES |
| SA-TO-SG PROMOTION | Schema 2 | Row 2 | YES |
| Phase 1 Setup | Schema 1 | Row 1 | YES |
| Phase 1 Setup | Schema 2 | Row 2 | YES |
| Phase 2 Execute | Schema 2 | Row 2 | YES |
| Phase 2 Execute | Schema 1 | Row 1 | YES |
| Step 3a | Schema 1 | Row 1 | YES |
| Step 3a | Schema 5 | Row 5 | YES |
| Step 3b | Schema 2 | Row 2 | YES |
| Step 3b | Schema 1 | Row 1 | YES |
| Step 3b | Schema 5 | Row 5 | YES |
| Step 3c | Schema 4 | Row 4 | YES |
| Step 3c | Schema 5 | Row 5 | YES |
| Step 3d | Schema 3 | Row 3 | YES |
| Step 3d | Schema 5 | Row 5 | YES |
| Phase 4 Amend | Schema 2 | Row 2 | YES |
| Phase 4 Amend | Schema 3 | Row 3 | YES |
| Phase 4 Amend | Schema 1 | Row 1 | YES |
| Phase 4 Amend | Schema 4 | Row 4 | YES |

Undeclared references: NONE.

**Direction B result**: All references confirmed registered. Direction B: HOLDS.

**Coverage Matrix bijection**:

| Direction | Evidence | Result |
|-----------|----------|--------|
| A (matrix -> phase) | Direction A table -- all 5 rows confirmed with named phase/step | HOLDS |
| B (phase -> matrix) | Direction B table assembled from footprint records | HOLDS |

**Coverage Matrix C-10: PASS.**

---

#### Role Closed-World Audit (v13 preview)

**Role-Schema Binding Summary bijection invariant**: Role R is in the Binding Summary if and
only if it produces at least one schema-governed action in Phase 2 Execute.

**Direction A: Binding Summary -> Execute** (no silent roles)
For each role declared in the Binding Summary, name the schema-governed action it produced
in Phase 2 Execute (from the "Schema-governed action evidence" field in its role relay).

| Role (Binding Summary) | Schema-governed action in Execute | Action evidence locus | Silent? |
|------------------------|----------------------------------|----------------------|---------|
| [role from Binding Summary] | [action that used Schema 1 or Schema 2 labels per Binding Summary declaration] | [role relay field: Schema-governed action evidence] | YES / NO |

Roles found to be silent are Binding Summary defects. State: "[role] declared but produced no
schema-governed action in Execute -- Binding Summary defect."

**Direction B: Execute -> Binding Summary** (no undeclared roles)
For each role appearing in Phase 2 Execute (from role relay headers), confirm a Binding
Summary row exists.

| Role (Execute relay) | Binding Summary entry | Declared? |
|----------------------|-----------------------|-----------|
| [role from Execute relay] | [Binding Summary row index] | YES / NO |

Roles found undeclared are structural defects. State: "[role] appeared in Execute with no
Binding Summary entry -- undeclared role defect."

**Role Closed-World Audit summary**:

| Direction | Claim | Result |
|-----------|-------|--------|
| A (Binding Summary -> Execute) | Every declared role produces at least one schema-governed action | [HOLDS if no silent roles / DEFECT: [list] if any silent] |
| B (Execute -> Binding Summary) | Every Execute role has a Binding Summary entry | [HOLDS if no undeclared roles / DEFECT: [list] if any undeclared] |

**Role bijection invariant: SATISFIED / DEFECTS FOUND (see above).**

---

**Bijection summary**:

| Invariant | C-10 Direction | Result |
|-----------|---------------|--------|
| Coverage Matrix bijection | A: HOLDS, B: HOLDS | C-10: PASS |
| Role-Schema Binding Summary bijection | A: [HOLDS/DEFECTS], B: [HOLDS/DEFECTS] | v13 preview: [PASS/PARTIAL] |

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
