---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 8
rubric: trace-skill-rubric-v7-2026-03-15.md
---

# trace-skill -- Variations R8 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R7 achieves C-01 through C-26 PASS under v7 scoring. v7 (updated after R7)
formalizes three new aspirational criteria from R7 excellence signals: C-27 (C-24 upgrade),
C-28 (C-25 upgrade), C-29 (C-26 upgrade).

**R7 C-24/C-25/C-26 PASS state and the R8 upgrade axis per criterion**:

- **C-24 (PASS in R7 V-01)**: Role relay schema carries an anti-pattern prohibition row with
  `VIOLATION` in the Required column -- the row is structurally isolated from the format
  content. The Required column itself is an implicit multi-value field carrying {YES, VIOLATION}
  without declaring those two values as a closed vocabulary. C-27 upgrade: declare Required as
  `Required (RequiredVocabulary)` and publish `RequiredVocabulary = {YES, VIOLATION}` as a
  named closed type before the relay schema table. A row's type (compliance vs prohibition) is
  then self-identifiable without sub-table name inspection.

- **C-25 (PASS in R7 V-02)**: Compliance ledger Verdict uses `Expected behavior` column typed
  as `Expected behavior (BehaviorDescription)` -- one column carries a (TypeName) annotation.
  The annotation convention is reusable. C-28 upgrade: apply `(TypeName)` uniformly to every
  column in every schema table that carries a typed vocabulary -- Coverage Matrix, Schema 1-5
  definition tables, role relay schema, findings table. Schema becomes self-describing at every
  column without an external type registry.

- **C-26 (PASS in R7 V-03)**: Coverage Matrix closure terminus is a labeled structural mandate
  ("**STRUCTURAL MANDATE -- CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation.").
  The mandate names the violation in prose ("a phase referencing an undeclared label is a
  structural defect"). C-29 upgrade: the mandate assigns a formal defect classification code
  (`DEFECT: OPEN-WORLD-ASSERTION`) so violations are citable in the Verdict compliance ledger
  by defect code rather than paraphrased prose.

**R8 variation axes**:

- **V-01 (single axis: C-27)**: RequiredVocabulary type declaration -- role relay schema gains
  explicit `RequiredVocabulary = {YES, VIOLATION}` type declaration; column header becomes
  `Required (RequiredVocabulary)`; vocabulary closure makes row type self-validating.

- **V-02 (single axis: C-28)**: Uniform type annotation -- (TypeName) convention applied to
  every typed column in every schema table in the prompt; schema is self-describing without
  external registry.

- **V-03 (single axis: C-29)**: Defect classification -- every named structural mandate carries
  a formal defect code; codes are citable in the Verdict compliance ledger by code.

- **V-04 (combined: C-27 + C-28)**: RequiredVocabulary + uniform type annotation.

- **V-05 (combined: C-27 + C-28 + C-29)**: All three new criteria -- complete R8 target.

All five inherit the full V-04 R7 architecture:
- Coverage Matrix with 5 schemas (Declared-at, Referenced-by, Role-binding, Verdict-check)
- Role-Schema Binding Summary before Stage 2
- Per-role schema binding in Phase 1 Setup
- Schema 2 compliance field in Phase 2 Execute role relays
- Compliance ledger Verdict with one row per declared usage site

---

## V-01 -- Single axis: C-27 (RequiredVocabulary type declaration)

**Axis**: Role sequence / schema typing -- the role relay schema in Phase 2 Execute is
formalized as a named schema table with a `Required (RequiredVocabulary)` column. Before the
table appears, the prompt declares `RequiredVocabulary` as a closed two-value type:
`{YES, VIOLATION}`. YES means the field is required in every valid relay. VIOLATION means the
row declares an anti-pattern whose presence in a relay is a structural violation. The anti-
pattern prohibition row (DO NOT omit Schema 2 compliance field) carries `VIOLATION` in the
Required column -- its row type is now self-identifiable from the column value alone, without
reading the Field cell or the sub-table name.

**Hypothesis**: R7 V-01's relay schema already has the anti-pattern prohibition row with
`VIOLATION` in Required (C-24 PASS). But the Required column has no declared vocabulary: a
reader scoring C-24 must infer that `VIOLATION` is a distinct semantic value from YES by
context. Adding `RequiredVocabulary = {YES, VIOLATION}` as a named closed type makes the
column self-validating: any value outside this vocabulary is a schema error, and VIOLATION rows
are independently identifiable without parsing the Field cell. C-27 is satisfied when the
vocabulary declaration is present. Risk: declaring a type before the table adds one line of
overhead per relay schema. Mitigation: the declaration is a single line adjacent to the table
header, co-located rather than in a separate section.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it, the roles bound by it, and the Verdict check that audits it. All
phases reference only the labels declared here.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source labels in relay; label lock after promotion) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 Amend drawn from all roles | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source coverage across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between all sub-steps) | N/A | VC-5 |

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

Read the skill spec. For each role in the execution sequence, declare its schema obligations.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's findings] | [Source labels this role may produce; label lock rules] | [schema 3/4 interactions] |

One row per role. A role without explicit schema binding is invalid.

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
  Schema 1 binding: [severity labels applicable to this role's findings]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
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

**Role Relay Schema** -- every role relay in this phase must conform to this schema.

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` -- field is required in every valid relay. A relay missing a YES field is structurally
  invalid and does not carry complete source-layer evidence.
- `VIOLATION` -- row declares an anti-pattern. A relay exhibiting this pattern is structurally
  invalid regardless of whether any YES field is missing.

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used by this role: [list] -- all from SA/SG/EG/QO: YES / NO | YES |
| SA/SG gaps affecting this role | [list or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | A relay without Schema 2 compliance does not carry source-layer evidence and is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section. A relay missing any
YES field or exhibiting the VIOLATION pattern is a schema violation; declare it and halt.

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

Carrying forward: [artifact: `{{artifact_path}}`], all gaps from Stages 1 and 2.

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step states its
Schema 5 Prerequisite and Unblocks before beginning.

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

**Hard-stop rule (Schema 4)**: a FAIL on any gate BLOCKS Step 3d and Phase 4. Resolve the
failing condition, re-run the gate, confirm PASS before proceeding.

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

### Verdict (Phase 5 -- Role-Binding Compliance Ledger)

Fill the compliance ledger completely. One row per usage site declared in the Coverage Matrix
Referenced-by column. Where the Role-binding column names specific roles, add per-role rows.
"Observed behavior" must state what was actually found at that specific site -- a cell reading
"Observed behavior: as expected" is structurally invalid.

**Relay Schema audit (C-27)**: Before walking the Coverage Matrix, confirm:
- Role Relay Schema table present in Phase 2 Execute: YES / NO
- `RequiredVocabulary = {YES, VIOLATION}` declared before the table: YES / NO
- `Required (RequiredVocabulary)` column header present: YES / NO
- Anti-pattern prohibition row carries `VIOLATION` in Required column: YES / NO
- All other rows carry `YES` in Required column: YES / NO
- C-27 result: PASS (all YES) / FAIL (any NO)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions written | [what the legend stated at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use only P1/P2/P3 | [severity labels in table; count of each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate verified against Schema 1 | [G-3 result and the severity labels it checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [severity labels in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 per Coverage Matrix Role-binding | [severity labels used by this role] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only in audit table | [Source labels used in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; no SA labels downstream for promoted | [which SA promoted; SG label confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO only; promoted show SG | [Source labels in Step 3b] | PASS / FAIL |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance field present; Source labels valid | [Source labels in this role's relay; compliance field: YES/NO] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated with all four channels | [activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field from declared taxonomy | [channels used; entries missing field if any] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 run with explicit PASS/FAIL | [G-1/G-2/G-3 results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | G-1 role aggregation | G-1 checks Source coverage across all roles | [Source types present; which roles contributed each] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [transition evidence: Schema 5 prerequisite confirmed] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b population | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d channel activation | [transition evidence] | PASS / FAIL |

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

## V-02 -- Single axis: C-28 (uniform type annotation across all typed columns)

**Axis**: Output format -- every column in every schema table that carries a typed vocabulary
receives a `(TypeName)` annotation in its header. The annotation convention `ColumnName (TypeName)`
is applied uniformly: if a column carries a closed vocabulary, its header names the type. This
makes the schema self-describing at the column level. Named types and their closed vocabularies
are declared adjacent to the table that introduces them. Coverage Matrix, Schema 1-5 definition
tables, role relay schema, findings table, and Verdict compliance ledger all carry (TypeName)
annotations where applicable.

**Hypothesis**: R7 V-02 achieves C-25 (PASS) by declaring `PrecedenceVocabulary` as a named
type for the Precedence applied column in the SA-TO-SG PROMOTION block -- one column is typed.
C-28 requires the same convention applied to every typed column. A reviewer scoring C-28 should
be able to identify the type of any column value without cross-referencing a schema definition
section -- the header itself is sufficient. Risk: annotating every column adds visual noise
proportional to the number of typed columns. Mitigation: type names are terse (SeverityVocab,
GapTypeVocab, ChannelVocab, etc.) and declared inline adjacent to their tables; reviewers who
do not need the type can ignore the annotation.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it, the roles bound by it, and the Verdict check that audits it.

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through phases with SG label |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable, not structural | Surface anywhere; P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

`ChannelVocab` = {spec, invocation, artifact, quality}. `ActivationPhaseRef` = {Step 3d}.

| Channel (ChannelVocab) | Targets | Activated-at (ActivationPhaseRef) |
|------------------------|---------|-----------------------------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

`GateIdentifier` = {G-1, G-2, G-3}. `BlockConditionVocab` = {Phase 4 BLOCKED while FAIL}.

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

| Step (StepIdentifier) | Prerequisite (StepIdentifier) | Produces | Unblocks (StepIdentifier) |
|-----------------------|------------------------------|---------|--------------------------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

`RoleName` = {role name strings from skill spec}.

| Role (RoleName) | Schema 1 binding (SeverityVocab) | Schema 2 binding (GapTypeVocab) | Notes |
|-----------------|----------------------------------|--------------------------------|-------|
| [role from spec] | [severity labels applicable] | [Source labels this role may produce; label lock rules] | [schema 3/4 interactions] |

One row per role. A role without explicit schema binding is invalid.

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using
Schema 2 (GapTypeVocab) and Schema 1 (SeverityVocab).

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without
content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types. Examine harder if gaps
cluster at one layer.

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity (DiversityVocab): PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

`PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA} (declared in Schema 2 above).

At the Setup boundary. For every SA gap in the relay, evaluate:

> Can the invoker supply this value at runtime even though the spec doesn't declare it?

```
SA-NN -> [result (PromotionVocab)]:
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

[Identical to V-01 Phase 1 -- Setup.]

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear.

**Role Relay Schema** -- every role relay in this phase must conform to this schema.

`RequiredVocabulary` = {YES, VIOLATION}. (See V-01 for vocabulary semantics.)

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used by this role: [list (GapTypeVocab)] -- all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | A relay without Schema 2 compliance does not carry source-layer evidence and is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

[Phase 3 sub-steps (3a, 3b, 3c, 3d) and Phase 4 Amend: identical to V-01, with typed column
headers in findings table as shown below.]

##### Step 3b -- Findings Table

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

[All other Phase 3 content identical to V-01.]

---

### Verdict (Phase 5 -- Compliance Ledger with Uniform Type Annotations)

**C-28 audit**: Verify uniform (TypeName) annotation before walking the Coverage Matrix.
- Coverage Matrix column headers carry (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier): YES / NO
- Schema 1 table: Label (SeverityVocab), Blocks? (BlocksVocab): YES / NO
- Schema 2 table: Type (GapTypeVocab), Promotion rule (PromotionVocab): YES / NO
- Schema 3 table: Channel (ChannelVocab), Activated-at (ActivationPhaseRef): YES / NO
- Schema 4 table: Gate (GateIdentifier), Hard-stop condition (BlockConditionVocab): YES / NO
- Schema 5 table: Step/Prerequisite/Unblocks (StepIdentifier): YES / NO
- Role Relay Schema: Required (RequiredVocabulary): YES / NO
- Findings table: Source (GapTypeVocab), Severity (SeverityVocab): YES / NO
- C-28 result: PASS (all YES -- every typed column annotated uniformly) / FAIL (any NO)

[Compliance ledger table: identical to V-01 Verdict ledger.]

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: C-29 (formal defect classifications for structural mandates)

**Axis**: Phrasing register -- every named structural mandate in the prompt carries a formal
defect classification code of the form `DEFECT: CODE-NAME`. The defect code is cited in the
Verdict compliance ledger when a violation is declared, replacing paraphrased prose descriptions.
Five defect classes are declared in a Defect Classification Registry before Stage 1. The
Coverage Matrix closure terminus, role relay anti-pattern prohibition, Schema 2 label lock,
sub-step ordering violations, and Phase 4 premature-advance hard-stop each have a formal
defect code. Verdict compliance ledger rows add a Defect code column that is filled on FAIL
or left blank on PASS.

**Hypothesis**: R7 V-03 achieves C-26 (PASS) via assertion-first style where each mandate
declares "a trace violating X is not a valid trace." C-26 requires the mandate to be a
labeled structural element. C-29 requires the mandate to carry a formal defect classification
that is citable in the Verdict by code rather than paraphrased. A reviewer scoring a FAIL in
the Verdict compliance ledger who reads "DEFECT: LABEL-LOCK-VIOLATION" can cross-reference the
defect registry and determine the exact structural violation without inspecting the Verdict
prose. Risk: five defect codes add cognitive overhead for low-context tracers. Mitigation:
all five codes are declared in the Defect Classification Registry before Stage 1; the registry
is a compact five-row table with one code per row.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

All structural violation defect codes for this trace are declared here before Stage 1.
A Verdict compliance ledger FAIL row cites the applicable defect code from this registry.

| Defect code | Mandate violated | Structural consequence |
|-------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure terminus -- a phase referenced a label not declared in the Coverage Matrix | Trace invalid: undeclared label cannot be audited by Verdict |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema anti-pattern prohibition -- relay omitted a required field or exhibited the prohibited pattern | Trace invalid: relay does not carry complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock -- a promoted gap retains SA label after SA-TO-SG PROMOTION | Trace invalid: promoted gap source attribution is incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering -- a sub-step ran before its prerequisite was satisfied | Trace invalid: prerequisite output not available to the out-of-order step |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop -- Phase 4 entered while a gate = FAIL | Trace invalid: structural gap carried forward without resolution |

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it, the roles bound by it, and the Verdict check that audits it.

**STRUCTURAL MANDATE -- CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any
phase referencing a label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | All roles (via Phase 4) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1: all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

**STRUCTURAL MANDATE -- LABEL LOCK**: A promoted SA gap uses SG label in all phases after
SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a label lock violation.
`DEFECT: LABEL-LOCK-VIOLATION`

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

**STRUCTURAL MANDATE -- GATE HARD-STOP**: Phase 4 is valid only when G-1 = PASS AND G-2 = PASS
AND G-3 = PASS. Phase 4 entered while any gate = FAIL is a hard-stop violation.
`DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

**STRUCTURAL MANDATE -- SUB-STEP SEQUENCE**: A sub-step begun without its prerequisite
satisfied is a sequencing violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

[Identical to V-01 Role-Schema Binding Summary.]

---

### Stage 1 -- Source-Layer Auditor

[Identical to V-01 Stage 1.]

---

### Stage 2 -- Hand-Compilation

[Relay received, SA-TO-SG PROMOTION, Phase 1 Setup: identical to V-01.]

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must appear.

**Role Relay Schema** -- every role relay in this phase must conform to this schema.

`RequiredVocabulary` = {YES, VIOLATION}.

**STRUCTURAL MANDATE -- RELAY SCHEMA**: A relay omitting any YES field or exhibiting the
VIOLATION pattern is a schema violation. `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO | YES |
| SA/SG gaps affecting this role | [list or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | A relay without Schema 2 compliance does not carry source-layer evidence and is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

[Phase 3 (Steps 3a-3d) and Phase 4 Amend: identical to V-01, with structural mandate
annotations shown below in the enforcement gate section.]

##### Step 3c -- Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated (>=2 entries).
**Schema 5 output**: gate results (all must be PASS to unblock Step 3d).

**STRUCTURAL MANDATE -- GATE HARD-STOP** (Schema 4): a FAIL on any gate BLOCKS Step 3d and
Phase 4. Resolve the failing condition, re-run the gate, confirm PASS before proceeding.
`DEFECT: PREMATURE-PHASE-ADVANCE`

**G-1 Source Diversity Gate** (Schema 4)
- Source types present: [list all Source values from table]
- Result: PASS / FAIL
- **If FAIL**: `DEFECT: PREMATURE-PHASE-ADVANCE` active. Phase 4 BLOCKED. Add missing-layer
  finding. Re-run G-1.

**G-2 Action Diversity Gate** (Schema 4)
- Same-Source pairs reviewed: [list or "none"]
- Result: PASS / FAIL
- **If FAIL**: `DEFECT: PREMATURE-PHASE-ADVANCE` active. Phase 4 BLOCKED. Revise duplicate Actions.

**G-3 Severity Completeness Gate** (Schema 4)
- Severity labels in Step 3b: [list]
- Result: PASS / FAIL
- **If FAIL**: `DEFECT: PREMATURE-PHASE-ADVANCE` active. Phase 4 BLOCKED. Relabel entries.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.
`DEFECT: OUT-OF-ORDER-EXECUTION` if Step 3d begins before this condition holds.

---

### Verdict (Phase 5 -- Compliance Ledger with Defect Code Citations)

Fill the compliance ledger. One row per usage site. FAIL rows cite the applicable defect code
from the Defect Classification Registry. "Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (if FAIL) |
|----|--------|-----------|------------------|------------------|-------------|-----------------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions written | [what the legend stated] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3b | All entries use only P1/P2/P3 | [severity labels in table; count] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate verified | [G-3 result and labels checked] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use only P1/P2/P3 | [severity labels in Amend] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 per Role-binding | [severity labels used by this role] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [Source labels in Stage 1] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | Step 3b Source | SA/SG/EG/QO; promoted show SG | [Source labels in Step 3b] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance present; Source labels valid | [Source labels in relay] | PASS / FAIL | -- / DEFECT: RELAY-SCHEMA-VIOLATION |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels used; missing if any] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 run with explicit PASS/FAIL | [G-1/G-2/G-3 results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source coverage checked across all roles | [Source types and contributing roles] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**C-29 audit**: All FAIL cells in Defect code column cite a code from the Defect Classification
Registry (not prose): YES / NO. C-29 result: PASS / FAIL.

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-27 + C-28 (RequiredVocabulary + uniform type annotation)

**Axes**:
- C-27 (from V-01): Role relay schema gains `RequiredVocabulary = {YES, VIOLATION}` type
  declaration; column header becomes `Required (RequiredVocabulary)`; vocabulary closure makes
  row type self-validating.
- C-28 (from V-02): Every typed column in every schema table carries a `(TypeName)` annotation
  in its header; types declared inline adjacent to each table; schema is self-describing.

**Hypothesis**: V-01 satisfies C-27 alone and V-02 satisfies C-28 alone. V-04 tests whether
the two axes reinforce each other without collision. Both C-27 and C-28 operate at the column-
header level -- C-27 closes the relay schema Required column vocabulary and C-28 annotates
every typed column with its type name. When combined, `Required (RequiredVocabulary)` in the
relay schema is simultaneously a C-27 vocabulary-closed column and a C-28 uniformly-annotated
column. The combination is additive: the relay schema satisfies both criteria via the same
column header. C-29 is not targeted -- no defect codes are added.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
| SG | Setup gap -- declared; invoker cannot supply | Carry through with SG label |
| EG | Execute gap -- contract requires; role cannot produce | Surface in Execute; carry to Findings |
| QO | Quality observation | P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

`ChannelVocab` = {spec, invocation, artifact, quality}. `ActivationPhaseRef` = {Step 3d}.

| Channel (ChannelVocab) | Targets | Activated-at (ActivationPhaseRef) |
|------------------------|---------|-----------------------------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

`GateIdentifier` = {G-1, G-2, G-3}. `BlockConditionVocab` = {Phase 4 BLOCKED while FAIL}.

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

| Step (StepIdentifier) | Prerequisite (StepIdentifier) | Produces | Unblocks (StepIdentifier) |
|-----------------------|------------------------------|---------|--------------------------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

`RoleName` = {role name strings from skill spec}.

| Role (RoleName) | Schema 1 binding (SeverityVocab) | Schema 2 binding (GapTypeVocab) | Notes |
|-----------------|----------------------------------|--------------------------------|-------|
| [role from spec] | [severity labels applicable] | [Source labels; label lock rules] | [schema 3/4 interactions] |

One row per role. A role without explicit schema binding is invalid.

---

### Stage 1 -- Source-Layer Auditor

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity (DiversityVocab): PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

[Relay received, SA-TO-SG PROMOTION, Phase 1 Setup: identical to V-01, with PromotionVocab
annotation on the Promotion field in the PROMOTION block.]

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

**Role Relay Schema** -- every role relay must conform to this schema.

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` -- field required in every valid relay.
- `VIOLATION` -- row declares anti-pattern; presence is a structural violation.

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] -- all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings and Phase 4 -- Amend

[Phase 3 sub-steps (3a, 3b, 3c, 3d) and Phase 4 Amend: identical to V-01, with typed column
annotations in the findings table (Source (GapTypeVocab), Severity (SeverityVocab)).]

##### Step 3b -- Findings Table

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

---

### Verdict (Phase 5 -- Role-Binding Compliance Ledger, C-27 + C-28 Audit)

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema table: YES / NO
- `Required (RequiredVocabulary)` column header in relay schema: YES / NO
- Anti-pattern row carries VIOLATION in Required column: YES / NO
- All other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation):
- Coverage Matrix: (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier) on all typed columns: YES / NO
- Schema 1: (SeverityVocab), (BlocksVocab): YES / NO
- Schema 2: (GapTypeVocab), (PromotionVocab): YES / NO
- Schema 3: (ChannelVocab), (ActivationPhaseRef): YES / NO
- Schema 4: (GateIdentifier), (BlockConditionVocab): YES / NO
- Schema 5: (StepIdentifier) on Step/Prerequisite/Unblocks: YES / NO
- Role-Schema Binding Summary: (RoleName), (SeverityVocab), (GapTypeVocab): YES / NO
- Stage 1 findings table: (GapTypeVocab), (SeverityVocab), (PhaseRef): YES / NO
- Role relay schema: (RequiredVocabulary): YES / NO
- Step 3b findings table: (GapTypeVocab), (SeverityVocab): YES / NO
- C-28 result: PASS (all YES -- every typed column annotated uniformly) / FAIL (any NO)

[Compliance ledger table: identical to V-01 Verdict ledger.]

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-27 + C-28 + C-29 (complete R8 target)

**Axes**: All three from V-01/V-02/V-03 combined.
- C-27 (V-01): RequiredVocabulary type declaration closing relay schema Required column.
- C-28 (V-02): Uniform (TypeName) annotation across all typed columns in all schema tables.
- C-29 (V-03): Defect Classification Registry; every structural mandate cites a defect code;
  Verdict compliance ledger adds Defect code column for FAIL rows.

**Hypothesis**: V-04 combines C-27 + C-28 without collision. V-05 adds C-29 on top. The
defect code column in the compliance ledger interacts with the typed column annotations (C-28)
-- the Defect code column itself carries `DefectCodeVocab` as its type name. The Defect
Classification Registry is a typed table with `DefectCode (DefectCodeVocab)` as a column
header, making the registry self-describing (C-28) and making the Verdict citations citable
by defect code (C-29). All three axes are additive at distinct structural layers: vocabulary
level (C-27), column-header level (C-28), mandate-to-code mapping level (C-29).

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` = {DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION,
DEFECT: LABEL-LOCK-VIOLATION, DEFECT: OUT-OF-ORDER-EXECUTION,
DEFECT: PREMATURE-PHASE-ADVANCE}.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure -- phase references undeclared label | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema -- relay omits required field or exhibits prohibited pattern | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock -- promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering -- sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop -- Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE -- CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any
phase referencing a label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE -- LABEL LOCK**: A promoted SA gap uses SG in all phases after
SA-TO-SG PROMOTION. A promoted gap retaining SA is a label lock violation.
`DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
| SG | Setup gap -- declared; invoker cannot supply | Carry with SG label |
| EG | Execute gap -- contract requires; role cannot produce | Surface in Execute; carry to Findings |
| QO | Quality observation | P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

`ChannelVocab` = {spec, invocation, artifact, quality}. `ActivationPhaseRef` = {Step 3d}.

| Channel (ChannelVocab) | Targets | Activated-at (ActivationPhaseRef) |
|------------------------|---------|-----------------------------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

`GateIdentifier` = {G-1, G-2, G-3}. `BlockConditionVocab` = {Phase 4 BLOCKED while FAIL}.

**STRUCTURAL MANDATE -- GATE HARD-STOP**: Phase 4 is valid only when all gates PASS. Phase 4
entered while any gate = FAIL is a hard-stop violation. `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE -- SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite
is satisfied is a sequencing violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

| Step (StepIdentifier) | Prerequisite (StepIdentifier) | Produces | Unblocks (StepIdentifier) |
|-----------------------|------------------------------|---------|--------------------------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

`RoleName` = {role name strings from skill spec}.

| Role (RoleName) | Schema 1 binding (SeverityVocab) | Schema 2 binding (GapTypeVocab) | Notes |
|-----------------|----------------------------------|--------------------------------|-------|
| [role from spec] | [severity labels applicable] | [Source labels; label lock rules] | [schema 3/4 interactions] |

One row per role. A role without explicit schema binding is invalid.

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation.

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity (DiversityVocab): PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`]. Do not re-derive. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

`PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA} (declared in Schema 2).

At the Setup boundary. For every SA gap in the relay:

```
SA-NN -> [result (PromotionVocab)]:
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

Schema 2 label lock active: promoted gaps use SG in all downstream phases.
`DEFECT: LABEL-LOCK-VIOLATION` if any promoted gap is found using SA label downstream.

---

#### Phase 1 -- Setup

Confirm each input with `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding (SeverityVocab): [severity labels applicable]
  Schema 2 binding (GapTypeVocab): [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

A role entry without schema binding is invalid.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by spec must appear.

**Role Relay Schema** -- every role relay must conform. (C-27 + C-28 combined.)

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` -- field required; missing = structural violation.
- `VIOLATION` -- anti-pattern row; presence = structural violation.

**STRUCTURAL MANDATE -- RELAY SCHEMA**: A relay omitting any YES field or exhibiting the
VIOLATION pattern is a schema violation. `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] -- all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step states its
Schema 5 Prerequisite and Unblocks. `DEFECT: OUT-OF-ORDER-EXECUTION` if sequence violated.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 prerequisite (StepIdentifier)**: Schema 1 declared in Coverage Matrix.
**Schema 5 unblocks (StepIdentifier)**: Step 3b.

| Label (SeverityVocab) | Definition for this trace | Actionability threshold |
|-----------------------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b -- Findings Table

**Schema 5 prerequisite**: Step 3a complete. **Schema 5 unblocks**: Step 3c.

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

---

##### Step 3c -- Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated. **Schema 5 unblocks**: Step 3d (if all-PASS).

**STRUCTURAL MANDATE -- GATE HARD-STOP** (Schema 4): FAIL on any gate BLOCKS Step 3d and
Phase 4. Resolve, re-run, confirm PASS before proceeding.
`DEFECT: PREMATURE-PHASE-ADVANCE`

**G-1** -- Source types in Step 3b: [list] -- Result: PASS / FAIL
If FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE` active. Phase 4 BLOCKED. Add missing-layer finding.

**G-2** -- Same-Source pairs: [list or "none"] -- Result: PASS / FAIL
If FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE` active. Phase 4 BLOCKED. Revise duplicate Actions.

**G-3** -- Severity labels in Step 3b: [list] -- Result: PASS / FAIL
If FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE` active. Phase 4 BLOCKED. Relabel entries.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.
`DEFECT: OUT-OF-ORDER-EXECUTION` if Step 3d begins before this condition holds.

---

##### Step 3d -- Channel Taxonomy Activation

**Schema 5 prerequisite**: Step 3c all-PASS. **Schema 5 unblocks**: Phase 4.

Activate Schema 3 channels: spec / invocation / artifact / quality.
Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.
`DEFECT: OUT-OF-ORDER-EXECUTION` if Phase 4 begins before Step 3d activation.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d (Schema 3 ChannelVocab): spec / invocation / artifact / quality.

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}` (GapTypeVocab)] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality (ChannelVocab)] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality (ChannelVocab)]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Complete R8 Audit: C-27 + C-28 + C-29)

Fill the compliance ledger. One row per usage site. FAIL rows cite defect code from Defect
Classification Registry. "Observed behavior: as expected" is structurally invalid.

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION: YES / NO
- All other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation -- all typed columns):
- Coverage Matrix: (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier): YES / NO
- Schema 1: (SeverityVocab), (BlocksVocab): YES / NO
- Schema 2: (GapTypeVocab), (PromotionVocab): YES / NO
- Schema 3: (ChannelVocab), (ActivationPhaseRef): YES / NO
- Schema 4: (GateIdentifier), (BlockConditionVocab): YES / NO
- Schema 5: (StepIdentifier) on all three step-reference columns: YES / NO
- Defect registry: (DefectCodeVocab) on Defect code column: YES / NO
- Role-Schema Binding Summary: (RoleName), (SeverityVocab), (GapTypeVocab): YES / NO
- Stage 1 table: (GapTypeVocab), (SeverityVocab), (PhaseRef): YES / NO
- Relay schema: (RequiredVocabulary): YES / NO
- Step 3b table: (GapTypeVocab), (SeverityVocab): YES / NO
- C-28 result: PASS (all YES) / FAIL (any NO)

**C-29 audit** (defect classifications in Verdict):
- Defect Classification Registry declared before Stage 1: YES / NO
- All FAIL rows in compliance ledger cite a DefectCodeVocab code (not prose): YES / NO
- C-29 result: PASS / FAIL

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|-------------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions written | [what the legend stated] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3b | All entries use only P1/P2/P3 | [severity labels in table; count] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate verified | [G-3 result and labels checked] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use only P1/P2/P3 | [severity labels in Amend entries] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 per Role-binding column | [severity labels used by this role] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only in audit table | [Source labels in Stage 1 table] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted show SG | [Source labels in Step 3b] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance present; Source labels valid | [Source labels in relay; compliance field value] | PASS / FAIL | -- / DEFECT: RELAY-SCHEMA-VIOLATION |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels used; entries missing field if any] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 run with explicit PASS/FAIL | [G-1/G-2/G-3 results at Step 3c] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source coverage checked across all roles | [Source types and roles that contributed each] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a completion | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b population | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d channel activation | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

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
