---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 2
rubric: trace-skill-rubric-v13-2026-03-15.md
---

# trace-skill -- Variations v13 R2 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: v12 R1 V-05 achieves C-01 through C-10 PASS and C-11 as a preview. v13 formalizes
C-11 (Role Closed-World Audit) and sharpens its scoring: aspirational denominator moves from 2 to 3.
Under v13, V-04 from v12 R1 scores 96.7 (no C-11); V-05 from v12 R1 scores 100 with both directions
enumerated. v13 R2 target: explore alternative structural mechanisms for C-11 that are equally
reliable but lighter, or that improve C-11 evidence quality through different capture points.

**v12 R1 V-05 C-11 structure** (the established baseline):
- Role-Schema Binding Summary bijection invariant declared in Coverage Matrix preamble
- "Schema-governed action evidence" field in each Phase 2 role relay (Direction A witness)
- Role Closed-World Audit in Verdict: Direction A table + Direction B table separately
- Roles found silent or undeclared are named as trace defects

**v13 R2 variation axes** (three single-axis, then combined):
- **Output format**: compact merged Role Bijection Table replaces two-direction separate tables (V-01)
- **Lifecycle emphasis**: Phase 2.5 Role Bijection Checkpoint between Execute and Findings (V-02)
- **Role sequence**: relay-seeded C-11 evidence captured at production, assembled in Verdict (V-03)

**Combined variations**:
- V-04: Output format + Role sequence (compact table fed by relay-seeded evidence)
- V-05: All three axes (Phase 2.5 checkpoint + relay-seeded fields + compact table in checkpoint)

All five v13 R2 variations inherit the full v12 R1 V-05 architecture:
- Coverage Matrix with 5 schemas (Role-binding column, biconditional invariant preamble)
- Direction A enumeration before Stage 1 (C-10 direction a)
- Role-Schema Binding Summary before Stage 2 (C-08)
- SA-TO-SG PROMOTION as a named lifecycle event (C-04)
- Phase 3 sub-steps 3a/3b/3c/3d governed by Schema 5 (C-05, C-07)
- Schema footprint records per phase (Direction B evidence assembly, C-10 direction b)
- Compliance ledger VC-1 through VC-5 with invariant-witness cells (C-07, C-09)
- Direction B assembled in Verdict from footprint records (C-10 direction b)

What varies per V-0N: only the C-11 structural mechanism.

---

## V-01 -- Single axis: Output format (Compact Role Bijection Table)

**Axis**: Output format -- the C-11 Role Closed-World Audit uses a single merged Role Bijection
Table in the Verdict instead of two separate Direction A and Direction B tables. Each row covers
one role and answers both directions simultaneously: the Binding Summary row, the Execute relay
step, the schema-governed action, and both direction statuses (A: Acts? B: Declared?). The
biconditional is verified by inspecting every row for A = YES and B = YES.

**Hypothesis**: v12 R1 V-05 uses two tables (one per direction), which is structurally correct
but requires the reader to cross-reference rows across tables to identify a violation. A single
merged table puts both directions in one view: a "SILENT" in column A and an "UNDECLARED" in
column B are visible in the same row. This reduces cross-table lookup and makes violations
immediately legible. Risk: merged rows may obscure direction-specific violations when a role
appears in one side but not the other -- the separate-table structure handles asymmetric cases
(roles declared but absent from Execute, roles acting in Execute without declaration) more
explicitly by having empty rows on the other table. The compact table must explicitly handle
asymmetric cases by allowing rows with one direction empty and the other populated.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority. A Coverage Matrix entry is valid if and only if the schema it registers is referenced
in at least one downstream phase. A schema referenced in any phase is valid if and only if it
appears in the Coverage Matrix. Both directions are the Coverage Matrix closed-world bijection
(C-10), verified by Direction A enumeration (below) and Direction B assembly (Verdict).

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. "Schema-governed action" means: an action using a label from Schema 1 or Schema 2 as
declared in the Binding Summary for that role. Verified by the Role Bijection Table in the Verdict.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema definitions** (biconditional form -- violations are structural invalidity, not quality issues):

**Schema 1**: A trace is valid w.r.t. Schema 1 if and only if every severity label in any phase
uses only {P1, P2, P3}. An entry using a label outside this set is structurally invalid at that
point. P1 = blocks useful baseline. P2 = quality improvement. P3 = advisory.

**Schema 2**: The SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all
phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a structural violation.

**Schema 3**: A trace is valid w.r.t. Schema 3 if and only if every Phase 4 Amend entry names
a remediation channel from {spec, invocation, artifact, quality}.

**Schema 4**: G-1 invariant: Step 3b contains >=2 distinct Source types. G-2 invariant: no two
same-Source findings carry identical Action text. G-3 invariant: all Step 3b entries use only
{P1, P2, P3}. A trace violating any gate cannot advance to Step 3d or Phase 4.

**Schema 5**: Step 3b is valid if and only if Step 3a complete. Step 3c valid iff Step 3b
>=2 entries. Step 3d valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy
activated.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

**Invariant**: Schema X is in the Coverage Matrix if and only if it is referenced by at least
one execution phase. Direction A enumerates the forward mapping: for each Coverage Matrix row,
name every specific phase and step where it is referenced. Orphan entries are trace defects.

| Schema | Matrix row | Referenced at (enumerate all phase/step names) | Orphan? |
|--------|-----------|------------------------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend declared); Step 3b (P1/P2/P3 enforced); Step 3c G-3 (verified); Phase 4 Amend (enforced) | NO |
| Schema 2 | Row 2 | Stage 1 audit; SA-TO-SG PROMOTION; Step 3b Source column; Execute role relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 transitions | NO |

Direction A result: all 5 rows confirmed with named references. No orphan entries.
Direction A invariant: HOLDS.

---

### Role-Schema Binding Summary

A valid trace declares every role that will appear in Phase 2 Execute before Stage 2 begins.
For each role, the binding declares which schemas govern its behavior. A role without explicit
schema binding is structurally invalid in this trace. One row per role from the skill spec.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role] | [severity labels applicable to this role's EG findings, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules for promoted gaps] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}` (not the test invocation) and produces a gap
audit table using Schema 2 Source labels and Schema 1 Severity labels. A Stage 1 where all
gaps cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay to Stage 2: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: PASS (>=2 distinct source types) / FAIL].

**Schema footprint -- Stage 1**: Schema 2 (Source labels in audit table), Schema 1 (Severity labels).

---

### Stage 2 -- Hand-Compilation

Stage 2 receives relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [layer diversity: `{{status}}`].
All gaps carried forward without re-deriving or silently resolving.

---

#### SA-TO-SG PROMOTION

Every SA gap in the Stage 1 relay is evaluated at the Setup boundary. A gap a spec-competent
invoker can supply at runtime promotes to SG. A gap requiring a spec change remains SA.
Schema 2 label lock: promoted gaps use SG in all downstream phases.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

After promotion: [SA remaining: `{{sa_remaining}}`], [SG from promotion: `{{sg_promoted}}`].

**Schema footprint -- SA-TO-SG PROMOTION**: Schema 2 (promotion labels SA->SG evaluated).

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

Per-role schema binding (from Binding Summary) and gap attribution:

```
[role: {{name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

Setup carry-forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

**Schema footprint -- Phase 1 Setup**: Schema 1 (binding declared per role), Schema 2 (bindings
and promoted labels confirmed).

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Schema 2 compliance field required in every relay.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps: [EG-NN list or "none"]

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in role relays), Schema 1
(Severity labels on EG findings per role).

---

#### Phase 3 -- Findings

##### Step 3a -- Severity Legend

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

**Schema footprint -- Step 3a**: Schema 1 (P1/P2/P3 legend declared), Schema 5 (prerequisite
confirmed; transition recorded).

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: >=2 entries -> Step 3c valid.

**Schema footprint -- Step 3b**: Schema 2 (Source column: SA/SG/EG/QO), Schema 1 (Severity
column: P1/P2/P3), Schema 5 (prerequisite confirmed; transition recorded).

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).

**G-1**: Source types in Step 3b: [list] -- G-1: PASS / FAIL
**G-2**: Same-Source pairs with identical Action: [list or "none"] -- G-2: PASS / FAIL
**G-3**: Severity labels in Step 3b: [list] -- G-3: PASS / FAIL

If any FAIL: Step 3d and Phase 4 are BLOCKED. State: "Phase 4 BLOCKED: [gate condition]."

Schema 5 transition: all-PASS -> Step 3d valid.

**Schema footprint -- Step 3c**: Schema 4 (G-1/G-2/G-3 evaluated), Schema 5 (transition).

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS.
Schema 3 channel taxonomy now active: every Phase 4 entry requires `[remediation channel: ...]`.

Schema 5 transition: channel active -> Phase 4 valid.

**Schema footprint -- Step 3d**: Schema 3 (channel taxonomy activated), Schema 5 (transition).

Findings carry-forward: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active].

---

#### Phase 4 -- Amend

Gates: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`. If any FAIL: Phase 4 BLOCKED.

Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock -- promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section changed: ]
- [change: ]

Or dismissal:
- [finding: `{{F-NN}}`], [reason: ], [remediation channel: ], [source type confirmed: YES / NO]

**Schema footprint -- Phase 4 Amend**: Schema 2 (Source label; lock honored), Schema 3 (channel
field present), Schema 1 (Severity inherited from finding), Schema 4 (gate status confirmed).

---

### Verdict (Phase 5 -- Compliance Ledger + Bijection Enumerations)

#### Compliance Ledger

"Observed behavior: as expected" is structurally invalid in any cell.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared (invariant: legend if and only if Schema 1 declared) | [what the legend stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [list severity values and count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate verified against Schema 1 | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use only P1/P2/P3 | [list labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; promoted = SG not SA | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels valid; lock honored | [list Source labels used] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels used; flag any missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity verified across all roles | [Source types present; which roles contributed each] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [prerequisite evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL |

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assembled from per-phase Schema footprint records. For each schema reference in any phase,
name the Coverage Matrix row. Undeclared references are trace defects.

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

Undeclared references: NONE. Direction B: HOLDS.

**C-10 Coverage Matrix bijection**:

| Direction | Evidence | Result |
|-----------|----------|--------|
| A (matrix -> phase) | Direction A table -- all 5 rows confirmed | HOLDS |
| B (phase -> matrix) | Direction B table assembled from footprint records | HOLDS |

**C-10: PASS.**

---

#### Role Bijection Table (C-11 -- Compact Merged Format)

**V-01 axis**: One row per role. Each row answers both bijection directions simultaneously.

**Invariant (biconditional form)**: Role R is in the Binding Summary if and only if it produces
at least one schema-governed action in Phase 2 Execute.

| Role | Binding Summary row | Execute relay step | Schema-governed action (Schema ref) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index] | [relay step name] | [action + Schema 1 or 2 reference] | YES / SILENT | YES / UNDECLARED |

Rules:
- "SILENT": role has a Binding Summary row but produced no schema-governed action in Execute.
  Declare: "[role] -- Binding Summary defect: declared but silent."
- "UNDECLARED": role appeared in Execute with no Binding Summary entry.
  Declare: "[role] -- structural defect: undeclared role."
- Every Binding Summary row must appear as exactly one table row.
- Every Execute relay header must appear as exactly one table row.
- Asymmetric cases (present in one side, absent from the other) produce separate rows with the
  absent side empty and the direction status set to SILENT or UNDECLARED accordingly.

**Role bijection holds if and only if: all A = YES AND all B = YES.**

| Direction | Claim | Result |
|-----------|-------|--------|
| A (Binding Summary -> Execute) | Every declared role acts | [HOLDS / DEFECTS: list] |
| B (Execute -> Binding Summary) | Every acting role is declared | [HOLDS / DEFECTS: list] |

**C-11: PASS / PARTIAL / FAIL** (PASS requires both directions HOLDS with no defects).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (Phase 2.5 Role Bijection Checkpoint)

**Axis**: Lifecycle emphasis -- the C-11 Role Closed-World Audit is extracted from the Verdict
and placed as a mandatory Phase 2.5 "Role Bijection Checkpoint" between Execute and Findings.
Phase 3 cannot begin until Phase 2.5 is complete and produces a gate result. If the role
bijection fails (silent role found or undeclared role found), Phase 3 is BLOCKED -- the same
hard-stop mechanism as Schema 4 enforcement gates. The checkpoint uses the same two-table
format as v12 R1 V-05 (Direction A and Direction B separately). The Verdict references the
Phase 2.5 result rather than re-running the audit.

**Hypothesis**: In v12 R1 V-05, C-11 lives in the Verdict, which means a model producing the
trace might defer or compress the role audit after producing the compliance ledger (late in the
trace). Moving C-11 to Phase 2.5 makes it a mandatory gate before Findings: the tracer must
verify role bijection before consolidating gap findings. This positions C-11 evidence at the
point of highest recall (immediately after all role relays are written), not at the point of
highest fatigue (end of Verdict). Risk: adding Phase 2.5 makes the lifecycle appear to have 5
phases (Setup, Execute, 2.5 Checkpoint, Findings, Amend), which may confuse models expecting
the standard 4-phase structure. The checkpoint must be clearly labeled as a between-phase gate,
not a fifth phase.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same as V-01 Coverage Matrix section -- 5 schemas, Role-binding column, biconditional invariants
for C-10 and C-11. Phase 2.5 Role Bijection Checkpoint is identified as the C-11 enforcement
point in the biconditional invariant preamble.]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Verified at Phase 2.5 Role Bijection Checkpoint by explicit enumeration of both
directions. If the bijection fails, Phase 3 is BLOCKED.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

Schema definitions: [same biconditional definitions as V-01].

Sub-step ordering table: [same as V-01 Schema 5 table].

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01 -- all 5 schemas confirmed with named phase/step references
before Stage 1 begins. Direction A: HOLDS.]

---

### Role-Schema Binding Summary

[Same Binding Summary table as V-01 -- one row per role, Schema 1 and Schema 2 bindings
declared before Stage 2.]

---

### Stage 1 -- Source-Layer Audit

[Same Stage 1 structure as V-01 -- gap audit table, relay to Stage 2, Schema footprint.]

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

[Same promotion structure as V-01 -- per SA gap: promote or retain, reason, label lock confirmed.]

#### Phase 1 -- Setup

[Same Setup structure as V-01 -- confirmed inputs, per-role schema binding and gap attribution,
carry-forward, Schema footprint.]

#### Phase 2 -- Execute

[Same Execute structure as V-01 -- role relay records with Schema 2 compliance field, artifact
production, carry-forward, Schema footprint.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (V-02 axis)

**Lifecycle gate**: Phase 2.5 runs immediately after Phase 2 Execute completes and before
Phase 3 Findings begins. Phase 3 cannot begin until Phase 2.5 produces a gate result.

**Role-Schema Binding Summary bijection invariant**: Role R is in the Binding Summary if and
only if it produces at least one schema-governed action in Phase 2 Execute.

---

**Direction A: Binding Summary -> Execute** (no silent roles)

For each role declared in the Binding Summary, name the schema-governed action it produced
in Phase 2 Execute. A role with no observable schema-governed action in Execute is a silent
role -- Binding Summary defect.

| Role (Binding Summary row) | Schema-governed action in Execute | Action evidence locus | Silent? |
|----------------------------|----------------------------------|----------------------|---------|
| [role] | [action using Schema 1 or 2 labels as declared in Binding Summary] | [role relay field or artifact section where action is observed] | YES / NO |

Silent roles found (if any): "[role] declared but produced no schema-governed action in Execute
-- Binding Summary defect."

---

**Direction B: Execute -> Binding Summary** (no undeclared roles)

For each role appearing in Phase 2 Execute (by role relay header), confirm a Binding Summary
row exists.

| Role (Execute relay) | Binding Summary row | Declared? |
|----------------------|--------------------|-----------|
| [role] | [row index] | YES / NO |

Undeclared roles found (if any): "[role] appeared in Execute with no Binding Summary entry --
undeclared role defect."

---

**Phase 2.5 gate result**:

| Direction | Claim | Result |
|-----------|-------|--------|
| A (Binding Summary -> Execute) | Every declared role acts | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared | HOLDS / DEFECTS: [list] |

**ROLE BIJECTION: PASS** (both directions HOLD, no defects) **/ FAIL** (defects found).

If FAIL: Phase 3 BLOCKED: [role bijection defect: name the silent or undeclared role(s) and
classify as Binding Summary defect or structural defect. Resolve before proceeding.]

---

#### Phase 3 -- Findings

Carrying forward from Phase 2.5: Role Bijection = `{{PASS}}`. Phase 3 valid to begin.

[Same Phase 3 structure as V-01 -- Steps 3a/3b/3c/3d with Schema footprints.]

#### Phase 4 -- Amend

[Same Phase 4 structure as V-01 -- gate confirmation, Amend entry, Schema footprint.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5 with invariant-witness cells.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01 -- assembled from Schema footprint records.]

**C-10: PASS.**

---

#### C-11 Reference

**C-11 verification**: Completed at Phase 2.5 Role Bijection Checkpoint.

| Direction | Phase 2.5 result | Defects |
|-----------|-----------------|---------|
| A (Binding Summary -> Execute) | HOLDS / DEFECTS | [list or "none"] |
| B (Execute -> Binding Summary) | HOLDS / DEFECTS | [list or "none"] |

**C-11: PASS** (Phase 2.5 gate result = PASS, both directions HOLDS, no defects).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Role sequence (Relay-Seeded C-11 Evidence)

**Axis**: Role sequence -- C-11 evidence is captured at the point of production (in Phase 2
role relays) rather than reconstructed in the Verdict. Each role relay gains two required fields
beyond the v12 R1 V-05 baseline: `Binding Summary row: [row index]` (Direction B evidence --
maps this Execute relay to its Binding Summary declaration) and `Schema-governed action:
[description] -- Schema ref: [Schema 1 or 2]` (Direction A evidence -- names the specific
action this role produced using declared schema labels). The Verdict assembles these relay fields
into the C-11 Direction A and Direction B tables rather than re-deriving from memory. A relay
missing either field is a structural defect detected during Verdict assembly.

**Hypothesis**: v12 R1 V-05 asks the Verdict to reconstruct the role-level bijection after all
execution phases are complete. This requires the model to remember which roles produced
schema-governed actions -- a recall task at the end of a long trace. Relay-seeded fields
capture this evidence at production time (immediately after each role relay is written),
distributing C-11 evidence through Execute rather than concentrating it at the end. Verdict
assembly becomes a read-and-copy operation (mechanically reliable) rather than a re-derivation
(susceptible to fatigue-based omissions). Risk: adding two required fields per relay increases
relay verbosity; the "Schema-governed action" field may be trivially satisfied if the role
relay's "Produced" field already names schema labels, blurring the distinction.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, Role-binding column, biconditional invariant
preamble for both C-10 and C-11. C-11 note: "Evidence is relay-seeded: captured in each role
relay's 'Binding Summary row' and 'Schema-governed action' fields. Verdict assembles from
relay fields."]

[Same schema definitions as V-01 -- biconditional forms for Schemas 1-5.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01.]

---

### Role-Schema Binding Summary

[Same Binding Summary table as V-01.]

---

### Stage 1 -- Source-Layer Audit

[Same Stage 1 as V-01.]

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

[Same as V-01.]

#### Phase 1 -- Setup

[Same as V-01.]

#### Phase 2 -- Execute (V-03 axis: relay-seeded C-11 evidence)

Produce: `{topic}-skill-trace-{date}.md`. Three fields required in every relay:
Schema 2 compliance, Binding Summary row, and Schema-governed action. A relay missing any of
these three fields is a structural defect.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index in Role-Schema Binding Summary table] (Direction B seed)
- **Schema-governed action**: [describe the specific action this role produced that used Schema 1
  or Schema 2 labels as declared in its Binding Summary row -- e.g., "labeled F-01 as EG (Schema 2
  Source label)" or "assigned P2 severity to finding (Schema 1 label)"]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps: [EG-NN list or "none"]

A relay where no schema-governed action can be named must declare: "No schema-governed action
found for [role] -- candidate silent role. Binding Summary requires review."

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in relays), Schema 1 (Severity
labels on EG findings per role).

---

[Phase 3 Steps 3a/3b/3c/3d: same as V-01.]

[Phase 4 Amend: same as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### Role Closed-World Audit (C-11 -- Relay-Assembled)

**V-03 axis**: Assembled from relay-seeded fields. Each table row reads the relevant relay field
directly. A missing field in a relay is a structural defect named here, not silently omitted.

**Direction A: Binding Summary -> Execute** (assembled from "Schema-governed action" relay fields)

For each role in the Binding Summary, read its Execute relay's "Schema-governed action" field.

| Role (Binding Summary) | Schema-governed action (from relay field) | Schema ref | Acts in Execute? |
|------------------------|------------------------------------------|------------|-----------------|
| [role] | [copied from relay "Schema-governed action" field] | Schema 1 / 2 | YES / NO (if relay missing field: "relay field absent -- structural defect") |

**Direction B: Execute -> Binding Summary** (assembled from "Binding Summary row" relay fields)

For each Execute relay, read its "Binding Summary row" field.

| Role (Execute relay) | Binding Summary row (from relay field) | Declared? |
|----------------------|---------------------------------------|-----------|
| [role] | [copied from relay "Binding Summary row" field] | YES / NO (if relay missing field: "relay field absent -- structural defect") |

**Assembly validation**: Every Binding Summary row has a corresponding Direction A row. Every
Execute relay has a corresponding Direction B row. A role relay with "relay field absent" in
either direction is a structural defect -- name the relay and the missing field.

| Direction | Claim | Result |
|-----------|-------|--------|
| A (Binding Summary -> Execute) | Every declared role acts | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared | HOLDS / DEFECTS: [list] |

**C-11: PASS / PARTIAL / FAIL.**

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: Output format + Role sequence (compact table fed by relay-seeded evidence)

**Axes**:
- Role sequence (V-03): relay-seeded C-11 evidence -- "Binding Summary row" and "Schema-governed
  action" fields captured in each Phase 2 role relay at production time.
- Output format (V-01): compact merged Role Bijection Table in the Verdict -- one row per role,
  both direction statuses in a single view, populated from the relay-seeded fields.

**Hypothesis**: V-01's compact table reduces cross-table lookup but leaves evidence re-derivation
to the Verdict author. V-03's relay seeding captures evidence at production but re-derives it in
the familiar two-table format. V-04 combines the relay seeding's evidence reliability with the
compact table's visual density: the Verdict assembles the compact table directly from relay
fields, making both evidence quality and presentation legibility maximal. The combined structure
tests whether the compact table format is compatible with relay-assembly: each compact table row
has exactly two evidence sources (Direction A field and Direction B field from the same relay),
making the assembly mechanical. Risk: roles that appear only in the Binding Summary (declared but
absent from Execute) have no relay and therefore no relay field to read -- the compact table must
handle this asymmetric case by reading from the Binding Summary directly.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, biconditional invariants. C-11 note: "Evidence
relay-seeded in Execute relays. Assembled into compact Role Bijection Table in Verdict."]

[Same schema definitions and sub-step ordering table as V-01.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01.]

---

### Role-Schema Binding Summary

[Same as V-01.]

---

### Stage 1 -- Source-Layer Audit

[Same as V-01.]

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

[Same as V-01.]

#### Phase 1 -- Setup

[Same as V-01.]

#### Phase 2 -- Execute (V-04: relay-seeded fields, same structure as V-03)

Produce: `{topic}-skill-trace-{date}.md`. Three required relay fields:
Schema 2 compliance, Binding Summary row (Direction B seed), Schema-governed action (Direction A seed).

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed for compact table)
- **Schema-governed action**: [action using Schema 1 or 2 labels as declared for this role]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content]
- EG gaps: [EG-NN or "none"]

A relay with no schema-governed action declares: "No schema-governed action -- candidate silent
role."

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in relays), Schema 1 (Severity
labels on EG findings).

---

[Phase 3 Steps 3a/3b/3c/3d: same as V-01.]

[Phase 4 Amend: same as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### Role Bijection Table (C-11 -- Compact + Relay-Assembled, V-04 axis)

**Invariant**: Role R is in the Binding Summary if and only if it produces at least one
schema-governed action in Phase 2 Execute.

Assembled from relay-seeded fields. Each row corresponds to one role. Population rules:
- If role has an Execute relay: read "Binding Summary row" field (Direction B) and
  "Schema-governed action" field (Direction A) from that relay.
- If role has a Binding Summary row but no Execute relay (declared, never ran): row is populated
  from Binding Summary only; "Execute relay step" = ABSENT; A = SILENT.
- If role has an Execute relay but no Binding Summary row: row is populated from relay only;
  "Binding Summary row" = ABSENT; B = UNDECLARED.

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [copied from relay field, or "no action / silent"] | YES / SILENT | YES / UNDECLARED |

Defect declarations:
- SILENT: "[role] -- Binding Summary defect: declared but produced no schema-governed action."
- UNDECLARED: "[role] -- structural defect: acted in Execute without Binding Summary entry."

**Role bijection holds if and only if: all A = YES AND all B = YES.**

| Direction | Claim | Result |
|-----------|-------|--------|
| A | Every declared role acts | HOLDS / DEFECTS: [list] |
| B | Every acting role is declared | HOLDS / DEFECTS: [list] |

**C-11: PASS / PARTIAL / FAIL.**

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: Lifecycle emphasis + Role sequence + Output format

**Axes**:
- Lifecycle emphasis (V-02): Phase 2.5 Role Bijection Checkpoint between Execute and Findings --
  a mandatory hard gate that BLOCKS Phase 3 if the role bijection fails.
- Role sequence (V-03): relay-seeded "Binding Summary row" and "Schema-governed action" fields
  captured in each Phase 2 role relay.
- Output format (V-01): compact merged Role Bijection Table -- one row per role, both directions
  visible simultaneously.

**Hypothesis**: V-04 combines relay seeding with compact table presentation but places the audit
in the Verdict (end of trace). V-05 moves the audit to Phase 2.5 (between Execute and Findings)
while retaining relay seeding (V-03) and compact presentation (V-01). The Phase 2.5 checkpoint
reads the relay fields to populate the compact table, declares a gate result, and blocks Phase 3
on failure. The Verdict then references the Phase 2.5 result as evidence -- it does not re-run
the audit. This is the most complete C-11 structure: evidence captured at production (V-03),
assembled into a compact view (V-01) at the earliest possible gate point (V-02), with Phase 3
blocked on failure. Combined risk: three axes add three layers of structural specification to
a single criterion; a model may satisfy one layer while silently omitting another. The relay
fields are the load-bearing evidence; if they are absent, Phase 2.5 must detect the absence and
declare a defect -- not proceed with an empty table.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, biconditional invariants. C-11 note: "Evidence
relay-seeded in Phase 2 relays. Assembled into compact Role Bijection Table at Phase 2.5 Role
Bijection Checkpoint. Phase 3 blocked if bijection fails. Verdict references Phase 2.5 result."]

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

**Coverage Matrix bijection invariant (C-10)**: Schema X is in the Coverage Matrix if and only
if it is referenced by at least one execution phase. Verified by Direction A enumeration (below)
and Direction B assembly (Verdict).

**Role-Schema Binding Summary bijection invariant (C-11)**: Role R is in the Binding Summary if
and only if it produces at least one schema-governed action in Phase 2 Execute. Verified at
Phase 2.5 Role Bijection Checkpoint. Evidence relay-seeded. Compact table populated from relay
fields. Phase 3 blocked if C-11 gate fails.

[Schema 1-5 biconditional definitions: same as V-01.]

[Schema 5 sub-step ordering table: same as V-01.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01 -- all 5 schemas confirmed before Stage 1. Direction A: HOLDS.]

---

### Role-Schema Binding Summary

[Same Binding Summary table as V-01 -- one row per role, Schema 1 and Schema 2 bindings.]

---

### Stage 1 -- Source-Layer Audit

[Same Stage 1 as V-01 -- gap audit, relay, Schema footprint.]

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

[Same as V-01.]

#### Phase 1 -- Setup

[Same as V-01 -- confirmed inputs, per-role schema binding, carry-forward, Schema footprint.]

#### Phase 2 -- Execute (V-05: relay-seeded fields, same as V-03/V-04)

Produce: `{topic}-skill-trace-{date}.md`. Three required relay fields:
Schema 2 compliance, Binding Summary row (Direction B seed), Schema-governed action (Direction A seed).
A relay missing either seeded field declares "relay field absent" -- Phase 2.5 will detect it.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed)
- **Schema-governed action**: [action using Schema 1 or 2 labels per Binding Summary declaration]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content]
- EG gaps: [EG-NN or "none"]

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in relays), Schema 1 (Severity
labels on EG findings).

---

#### Phase 2.5 -- Role Bijection Checkpoint (V-05: reads relay-seeded fields, compact table)

**Lifecycle gate**: Runs immediately after Phase 2 Execute. Phase 3 Findings cannot begin until
this checkpoint produces a gate result.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact -- V-01 format, relay-assembled -- V-03 method):

Population rules:
- Execute relay present: read "Binding Summary row" and "Schema-governed action" fields.
- Binding Summary row present but no Execute relay: A = SILENT (orphan declaration).
- Execute relay present but no Binding Summary row: B = UNDECLARED (structural defect).
- Relay field absent: state "relay field absent -- structural defect" in the relevant column.

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "absent / silent"] | YES / SILENT | YES / UNDECLARED |

Defect declarations:
- SILENT: "[role] -- Binding Summary defect: declared but produced no schema-governed action."
- UNDECLARED: "[role] -- structural defect: acted in Execute without Binding Summary entry."
- Relay field absent: "[role relay] -- relay-seeded field missing: [Binding Summary row / Schema-governed action]."

**Phase 2.5 gate result**:

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts | Schema-governed action relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared | Binding Summary row relay fields | HOLDS / DEFECTS: [list] |

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent)
**/ FAIL** (any A = SILENT, B = UNDECLARED, or relay field absent).

If FAIL: Phase 3 BLOCKED: [state the defect -- silent role, undeclared role, or absent relay
field. Classify: Binding Summary defect / structural defect / relay defect. Do not proceed
until resolved or explicitly accepted as a trace finding.]

---

#### Phase 3 -- Findings

Carrying forward from Phase 2.5: Role Bijection = `{{PASS}}`. Phase 3 valid to begin.

[Same Phase 3 structure as V-01 -- Steps 3a/3b/3c/3d with Schema footprints.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5 with invariant-witness cells.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01 -- assembled from Schema footprint records.]

**C-10: PASS.**

---

#### C-11 Reference

**C-11 verification**: Completed at Phase 2.5 Role Bijection Checkpoint (relay-seeded, compact table).

| Direction | Evidence source | Phase 2.5 result |
|-----------|----------------|-----------------|
| A (Binding Summary -> Execute) | "Schema-governed action" relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | "Binding Summary row" relay fields | HOLDS / DEFECTS: [list] |

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no relay field defects).

The biconditional invariant -- Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute -- is found to hold: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
