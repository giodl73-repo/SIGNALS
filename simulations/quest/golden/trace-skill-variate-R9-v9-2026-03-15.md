---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 9
rubric: trace-skill-rubric-v8-2026-03-15.md
---

# trace-skill -- Variations R9 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R8 V-05 achieves C-01 through C-29 PASS under v8 scoring. v8 (updated after R8)
formalizes three new aspirational criteria from R8 excellence signals: C-30 (C-27 upgrade),
C-31 (C-28 upgrade), C-32 (C-29 upgrade).

**R8 C-27/C-28/C-29 PASS state and the R9 upgrade axis per criterion**:

- **C-27 (PASS in R8 V-01)**: Role relay schema Required column carries `RequiredVocabulary =
  {YES, VIOLATION}` as a named closed two-value type. The vocabulary closure makes each row
  self-validating. C-30 upgrade: the same vocabulary-closure discipline propagates to
  `DefectCodeVocab` in the Defect Classification Registry -- the Registry declares
  `DefectCodeVocab` as a named closed five-value type with each code defined, making every named
  type in the schema closed-typed and self-enumerating, not just `RequiredVocabulary`.

- **C-28 (PASS in R8 V-02)**: Uniform `(TypeName)` annotation applied to every typed column in
  every schema table -- 11 audit sites in R8 V-05. The Defect Classification Registry's Defect
  code column is site #11. C-31 upgrade: the same convention propagates to the Verdict compliance
  ledger's Defect code column (introduced as the second composed column by C-29 composition).
  The C-28 audit block explicitly tracks total annotation site count (12) and audits both C-29-
  composed columns separately, confirming composed-column coverage is verifiable.

- **C-29 (PASS in R8 V-03)**: Structural mandates carry formal defect codes; Verdict compliance
  ledger cites codes by name; C-29 audit block at Verdict bottom confirms FAIL citations are from
  the registry. C-32 upgrade: the Verdict compliance ledger Defect code column is fully populated
  -- every row carries a value (PASS rows carry `--` sentinel, FAIL rows carry a DefectCodeVocab
  code, no cells empty). The C-29 audit block moves to Verdict TOP and adds a third check: (c) no
  empty cells in the Defect code column. The audit self-certifies ledger integrity without
  requiring re-inspection of the registry.

**R9 variation axes**:

- **V-01 (single axis: C-30)**: DefectCodeVocab closed type -- Defect Classification Registry
  declares `DefectCodeVocab` as a closed five-value type using the same structural formalism as
  `RequiredVocabulary`; each code is defined inline; C-30 audit in Verdict confirms closure.

- **V-02 (single axis: C-31)**: C-28 site count audit -- Verdict compliance ledger Defect code
  column added as a separate composed annotation site (#12); C-28 audit block explicitly states
  total site count (12) and confirms composed-column coverage.

- **V-03 (single axis: C-32)**: Fully populated ledger + C-29 audit at Verdict top -- every ledger
  row carries a value; C-29 audit block moves to Verdict TOP with three-part check: (a) registry
  present before Stage 1, (b) all FAIL citations from DefectCodeVocab, (c) no empty cells.

- **V-04 (combined: C-30 + C-31)**: DefectCodeVocab closed type + C-28 site count audit.

- **V-05 (combined: C-30 + C-31 + C-32)**: All three new criteria -- complete R9 target.

All five inherit the full V-05 R8 architecture:
- Defect Classification Registry before Stage 1
- Coverage Matrix with 5 schemas and Role-binding column
- Role-Schema Binding Summary before Stage 2
- Per-role schema binding in Phase 1 Setup
- Schema 2 compliance field in Phase 2 Execute role relays with RequiredVocabulary type
- Uniform (TypeName) annotations across all schema tables (C-28)
- Structural mandates with defect codes (C-29)
- Compliance ledger Verdict with defect code column (DefectCodeVocab)

---

## V-01 -- Single axis: C-30 (DefectCodeVocab declared as closed type)

**Axis**: Role sequence / vocabulary closure -- the Defect Classification Registry declares
`DefectCodeVocab` as a named closed five-value type before the registry table, using the same
structural formalism that C-27 applied to `RequiredVocabulary`. Each of the five defect codes is
defined with its mandate and structural consequence. The registry table column header becomes
`Defect code (DefectCodeVocab)` (already present in R8 V-05 via C-28). A C-30 audit block at
Verdict confirms: type declaration present, all five codes enumerated, column header carries
(DefectCodeVocab). Any value in the Defect code column outside DefectCodeVocab is a schema error
without requiring manual cross-reference.

**Hypothesis**: R8 V-05 declares `DefectCodeVocab` as a named set in a single line (`DefectCodeVocab
= {...}`) before the registry table. C-30 requires this declaration to carry the same structural
weight as `RequiredVocabulary` in C-27: not just a set assignment but a closed-type declaration
with each code defined and a vocabulary-closure statement. A reviewer scoring C-30 should be able
to identify that DefectCodeVocab is closed (finite, enumerated) without inspecting the registry
rows -- the type declaration block is sufficient. Risk: five-code type declaration adds three to
five lines before the registry table. Mitigation: the block is co-located with the registry,
parallel to how `RequiredVocabulary` is co-located with the relay schema.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

Each value names a structural defect class. Any value in the Defect code column outside this
vocabulary is a schema error:
- `DEFECT: OPEN-WORLD-ASSERTION` -- a phase referenced a label, channel, or gate not declared in
  the Coverage Matrix. The undeclared label cannot be Verdict-audited.
- `DEFECT: RELAY-SCHEMA-VIOLATION` -- a role relay omitted a required field or exhibited the
  prohibited pattern. The relay lacks complete source-layer evidence.
- `DEFECT: LABEL-LOCK-VIOLATION` -- a promoted SA gap retained its SA label after SA-TO-SG
  PROMOTION. Source attribution is incorrect in all downstream phases.
- `DEFECT: OUT-OF-ORDER-EXECUTION` -- a sub-step ran before its prerequisite was satisfied. The
  prerequisite output was unavailable to the out-of-order step.
- `DEFECT: PREMATURE-PHASE-ADVANCE` -- Phase 4 was entered while any enforcement gate = FAIL. A
  structural gap was carried forward without resolution.

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
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE -- LABEL LOCK**: A promoted SA gap uses SG in all phases after
SA-TO-SG PROMOTION. A promoted gap retaining SA is a label lock violation.
`DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
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
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE -- SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite
is satisfied is a sequencing violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

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
  Schema 1 binding (SeverityVocab): [severity labels applicable to this role's findings]
  Schema 2 binding (GapTypeVocab): [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

A role entry without schema binding declaration is invalid.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by spec must appear.

**Role Relay Schema** -- every role relay must conform to this schema.

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` -- field required in every valid relay. A relay missing a YES field is structurally invalid.
- `VIOLATION` -- row declares an anti-pattern. A relay exhibiting this pattern is structurally
  invalid regardless of whether any YES field is missing.

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

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step states its Schema 5
Prerequisite and Unblocks. `DEFECT: OUT-OF-ORDER-EXECUTION` if sequence violated.

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

### Verdict (Phase 5 -- Compliance Ledger with C-30 Audit)

Fill the compliance ledger completely. One row per usage site. FAIL rows cite defect code from
the Defect Classification Registry. "Observed behavior: as expected" is structurally invalid.

**C-30 audit** (DefectCodeVocab closure -- before walking coverage matrix):
- `DefectCodeVocab` declared as closed five-value type before registry table: YES / NO
- All five codes enumerated in the type declaration block: YES / NO
- Defect code column header in registry carries `(DefectCodeVocab)`: YES / NO
- Any value in a Defect code column outside DefectCodeVocab is independently detectable as a
  schema error without consulting registry rows: YES / NO
- C-30 result: PASS (all YES) / FAIL (any NO)

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema table: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION in Required column: YES / NO
- All other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation -- all typed columns):
- Coverage Matrix: (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier) on typed columns: YES / NO
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
- C-28 result: PASS (all YES -- every typed column annotated uniformly) / FAIL (any NO)

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

---

## V-02 -- Single axis: C-31 (C-28 audit tracks annotation site count)

**Axis**: Output format -- the C-28 audit block in the Verdict explicitly tracks the total
annotation site count and audits the Verdict compliance ledger's Defect code column as a separate
composed site. R8 V-05 audits 11 sites (10 pre-C-29 + 1 C-29-composed: the Defect registry's
code column). C-31 requires the Verdict compliance ledger's Defect code column to be recognized
as a second C-29-composed column and audited separately, bringing the total to 12. The C-28 audit
block terminates with an explicit count line: "Total annotation sites audited: 12 (10 pre-C-29 +
2 C-29-composed)." A reviewer confirming C-31 can verify composed-column coverage from the count
alone without tallying individual audit lines.

**Hypothesis**: R8 V-05's C-28 audit audits the Defect registry's code column as site #11 but
does not separately audit the Verdict compliance ledger's code column -- both columns carry
`(DefectCodeVocab)`, but only one is tracked. C-31 upgrade: treat both as composed annotation
sites, add site #12 explicitly, and state the total. The site count makes composed-column coverage
verifiable: if the count does not match the expected total, the audit flags a gap without requiring
the reviewer to enumerate sites manually. Risk: adding a count assertion introduces a brittle
invariant if the schema evolves. Mitigation: the count is declared once, in the audit block, and
updates naturally when schema tables change.

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
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE -- LABEL LOCK**: A promoted SA gap uses SG in all phases after
SA-TO-SG PROMOTION. `DEFECT: LABEL-LOCK-VIOLATION`

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

**STRUCTURAL MANDATE -- GATE HARD-STOP**: Phase 4 is valid only when all gates PASS.
`DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
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

[Relay received, SA-TO-SG PROMOTION, Phase 1 Setup: identical to V-01.]

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

**Role Relay Schema** -- every role relay must conform.

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

[Role relay format and Phase 3/Phase 4 structure: identical to V-01.]

##### Step 3b -- Findings Table

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

---

### Verdict (Phase 5 -- Compliance Ledger with C-31 Site Count Audit)

Fill the compliance ledger. One row per usage site. FAIL rows cite defect code from registry.

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION: YES / NO
- All other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation -- 12 sites, including 2 C-29-composed):
- Coverage Matrix: (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier) on typed columns: YES / NO
- Schema 1: (SeverityVocab), (BlocksVocab): YES / NO
- Schema 2: (GapTypeVocab), (PromotionVocab): YES / NO
- Schema 3: (ChannelVocab), (ActivationPhaseRef): YES / NO
- Schema 4: (GateIdentifier), (BlockConditionVocab): YES / NO
- Schema 5: (StepIdentifier) on all three step-reference columns: YES / NO
- Role-Schema Binding Summary: (RoleName), (SeverityVocab), (GapTypeVocab): YES / NO
- Stage 1 table: (GapTypeVocab), (SeverityVocab), (PhaseRef): YES / NO
- Relay schema: (RequiredVocabulary): YES / NO
- Step 3b table: (GapTypeVocab), (SeverityVocab): YES / NO
- [C-29-composed site 1] Defect registry: Defect code column carries (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger: Defect code column carries (DefectCodeVocab): YES / NO
- **Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed)**: confirmed / mismatch
- C-28 result: PASS (all YES and count confirmed) / FAIL (any NO or count mismatch)

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

**VC-1 through VC-5 overall**: PASS if all rows in that VC PASS / FAIL otherwise

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: C-32 (fully populated ledger + C-29 audit at Verdict top)

**Axis**: Lifecycle emphasis -- the C-29 audit block moves from the bottom of the Verdict section
to the TOP, becoming the first thing declared before the compliance ledger table. The audit gains
a third check: "(c) no empty cells in the Defect code column." Every row in the compliance ledger
carries a value in the Defect code column -- PASS rows carry `--` as an explicit sentinel, FAIL
rows carry a DefectCodeVocab code. No cell is left blank. The audit self-certifies ledger
integrity: a reviewer confirming C-32 can verify the three conditions in order and declare the
ledger self-certified without re-inspecting the Defect Classification Registry row by row.

**Hypothesis**: R8 V-05's C-29 audit is placed at the bottom of the Verdict section and checks
only that FAIL rows cite a code -- it does not confirm PASS rows carry `--` and does not check for
empty cells. A partial audit allows an empty-cell defect to pass undetected if no FAIL rows exist.
Moving the audit to the Verdict TOP and adding check (c) closes this gap: the audit runs before
the reviewer reads the ledger, making the ledger's integrity precondition rather than postcondition.
Risk: a top-of-Verdict audit adds three lines before the table, increasing the distance between
audit instruction and table. Mitigation: the three-part structure is compact and directly names
the conditions it checks; reviewers can scan the audit checklist before inspecting the table.

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

[Schema 1-5 definition tables, Role-Schema Binding Summary: identical to V-01.]

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

[Relay received, SA-TO-SG PROMOTION, Phase 1 Setup, Phase 2 Execute (with RequiredVocabulary
typed relay schema and structural mandates), Phase 3 (Steps 3a-3d), Phase 4 Amend: identical
to V-01.]

---

### Verdict (Phase 5 -- Compliance Ledger with C-32: Fully Populated + Top-of-Verdict C-29 Audit)

**C-29 audit** (ledger integrity -- before compliance ledger table):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows in Defect code column cite a DefectCodeVocab code (not prose description):
  YES / NO
- (c) No empty cells in Defect code column -- every row carries `--` (PASS) or a
  DefectCodeVocab code (FAIL): YES / NO
- C-29 result: PASS (all three YES) / FAIL (any NO)

Fill the compliance ledger completely. One row per usage site. Every Defect code cell must carry
a value: `--` for PASS rows, a DefectCodeVocab code for FAIL rows. An empty cell is a C-32
violation detectable by check (c) above.

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION in Required column: YES / NO
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

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|-------------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions written | [what the legend stated] | PASS | -- |
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

**VC-1 through VC-5 overall**: PASS if all rows in that VC PASS / FAIL otherwise

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-30 + C-31 (DefectCodeVocab closed type + C-28 site count audit)

**Axes**:
- C-30 (from V-01): Defect Classification Registry declares `DefectCodeVocab` as a named closed
  five-value type with each code defined inline; vocabulary closure makes every named type in the
  schema self-enumerating.
- C-31 (from V-02): C-28 audit block audits both C-29-composed columns separately (sites #11 and
  #12), explicitly counts all 12 annotation sites, and confirms composed-column coverage via count.

**Hypothesis**: V-01 satisfies C-30 alone and V-02 satisfies C-31 alone. V-04 tests whether the
two axes combine without collision. C-30 operates in the Defect Classification Registry (type
declaration block before the registry table). C-31 operates in the Verdict C-28 audit block (adds
a line and a count). The two changes are structurally independent -- C-30 adds a type declaration
section, C-31 adds audit lines. When combined, the registry carries the closed-type declaration
(C-30) AND the C-28 audit explicitly tracks the registry column as composed site #11 and the
ledger column as composed site #12 (C-31). C-32 is not targeted.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

Each value names a structural defect class. Any value in the Defect code column outside this
vocabulary is a schema error:
- `DEFECT: OPEN-WORLD-ASSERTION` -- a phase referenced a label not declared in the Coverage Matrix.
- `DEFECT: RELAY-SCHEMA-VIOLATION` -- a relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` -- a promoted SA gap retained its SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` -- a sub-step ran before its prerequisite was satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` -- Phase 4 was entered while any enforcement gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure -- undeclared label referenced | Trace invalid: cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema -- required field omitted or anti-pattern exhibited | Trace invalid: relay lacks source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock -- promoted gap retains SA label | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering -- prerequisite not satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop -- Phase 4 entered with gate = FAIL | Trace invalid: structural gap unresolved |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE -- CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation.
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

**STRUCTURAL MANDATE -- LABEL LOCK**: Promoted SA gaps use SG downstream.
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

**STRUCTURAL MANDATE -- GATE HARD-STOP**: Phase 4 valid only when all gates PASS.
`DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE -- SUB-STEP SEQUENCE**: Prerequisite must be satisfied before sub-step runs.
`DEFECT: OUT-OF-ORDER-EXECUTION`

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

---

### Stage 1 -- Source-Layer Auditor

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity (DiversityVocab): PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

[SA-TO-SG PROMOTION with PromotionVocab annotation, Phase 1 Setup with per-role schema binding:
identical to V-01.]

---

#### Phase 2 -- Execute

**Role Relay Schema** -- (C-27 + C-30 combined: both named types closed.)

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` -- field required; missing = structural violation.
- `VIOLATION` -- anti-pattern row; presence = structural violation.

**STRUCTURAL MANDATE -- RELAY SCHEMA**: `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] -- all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

[Role relay format identical to V-01. Phase 3 sub-steps (3a-3d) and Phase 4 Amend identical to
V-01, with typed column headers in all tables.]

##### Step 3b -- Findings Table

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

---

### Verdict (Phase 5 -- C-30 + C-31 Audit: Closed Type + Site Count)

Fill the compliance ledger. FAIL rows cite defect code from registry.

**C-30 audit** (DefectCodeVocab closure):
- `DefectCodeVocab` declared as closed five-value type before registry table: YES / NO
- All five codes enumerated in the type declaration block: YES / NO
- Defect code column header carries `(DefectCodeVocab)` in registry table: YES / NO
- C-30 result: PASS (all YES) / FAIL (any NO)

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION: YES / NO; all other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation -- 12 sites, including 2 C-29-composed):
- Coverage Matrix: (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier): YES / NO
- Schema 1: (SeverityVocab), (BlocksVocab): YES / NO
- Schema 2: (GapTypeVocab), (PromotionVocab): YES / NO
- Schema 3: (ChannelVocab), (ActivationPhaseRef): YES / NO
- Schema 4: (GateIdentifier), (BlockConditionVocab): YES / NO
- Schema 5: (StepIdentifier) on all three step-reference columns: YES / NO
- Role-Schema Binding Summary: (RoleName), (SeverityVocab), (GapTypeVocab): YES / NO
- Stage 1 table: (GapTypeVocab), (SeverityVocab), (PhaseRef): YES / NO
- Relay schema: (RequiredVocabulary): YES / NO
- Step 3b table: (GapTypeVocab), (SeverityVocab): YES / NO
- [C-29-composed site 1] Defect registry: Defect code column carries (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger: Defect code column carries (DefectCodeVocab): YES / NO
- **Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed)**: confirmed / mismatch
- C-28 result: PASS (all YES and count confirmed) / FAIL (any NO or mismatch)

**C-29 audit** (defect classifications):
- Defect Classification Registry declared before Stage 1: YES / NO
- All FAIL rows cite a DefectCodeVocab code (not prose): YES / NO
- C-29 result: PASS / FAIL

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|-------------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions written | [what the legend stated] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3b | All entries use only P1/P2/P3 | [severity labels; count] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate verified | [G-3 result and labels] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use only P1/P2/P3 | [severity labels in Amend] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 per Role-binding column | [severity labels this role used] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [Source labels in Stage 1] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted use SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted show SG | [Source labels in Step 3b] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance present; labels valid | [Source labels in relay; compliance field] | PASS / FAIL | -- / DEFECT: RELAY-SCHEMA-VIOLATION |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels used; missing if any] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 run with explicit PASS/FAIL | [gate results at Step 3c] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source coverage across all roles | [Source types and contributing roles] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**VC-1 through VC-5 overall**: PASS if all rows in that VC PASS / FAIL otherwise

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-30 + C-31 + C-32 (complete R9 target)

**Axes**: All three from V-01/V-02/V-03 combined.
- C-30 (V-01): DefectCodeVocab declared as closed five-value type; every named type in the
  schema is now closed-typed and self-enumerating.
- C-31 (V-02): C-28 audit explicitly tracks 12 total annotation sites (10 pre-C-29 + 2 C-29-
  composed); both composed columns audited separately; count asserted.
- C-32 (V-03): Verdict compliance ledger Defect code column fully populated (PASS rows `--`,
  FAIL rows code, no empty cells); C-29 audit moves to Verdict TOP with three-part check
  including "(c) no empty cells."

**Hypothesis**: V-04 combines C-30 + C-31. V-05 adds C-32 on top. C-32 interacts with C-31:
the Verdict compliance ledger Defect code column must carry `(DefectCodeVocab)` annotation
(C-31 composed site #12) AND be fully populated with `--` or a code in every row (C-32). When
combined, the ledger column is simultaneously typed (C-31), fully populated (C-32), and self-
certifiable via the top-of-Verdict audit (C-32). C-30 is independent: it operates in the
registry. All three axes are additive at distinct structural layers: registry-type level (C-30),
audit-count level (C-31), ledger-population level (C-32). The combined prompt satisfies all 24
v8 aspirational criteria.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

Each value names a structural defect class. Any value in any Defect code column outside this
vocabulary is a schema error independently detectable without consulting registry rows:
- `DEFECT: OPEN-WORLD-ASSERTION` -- a phase referenced a label not declared in the Coverage Matrix.
- `DEFECT: RELAY-SCHEMA-VIOLATION` -- a relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` -- a promoted SA gap retained its SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` -- a sub-step ran before its prerequisite was satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` -- Phase 4 was entered while any enforcement gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure -- undeclared label referenced | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema -- required field omitted or anti-pattern exhibited | Trace invalid: relay lacks complete source-layer evidence |
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
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE -- LABEL LOCK**: A promoted SA gap uses SG in all phases after
SA-TO-SG PROMOTION. A promoted gap retaining SA is a label lock violation.
`DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
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
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE -- SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite
is satisfied is a sequencing violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

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
| [role from spec] | [severity labels applicable to this role's findings] | [Source labels this role may produce; label lock rules] | [schema 3/4 interactions] |

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
  Schema 1 binding (SeverityVocab): [severity labels applicable to this role's findings]
  Schema 2 binding (GapTypeVocab): [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

A role entry without schema binding declaration is invalid. "none -- confirmed" only after
verifying.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by spec must appear.

**Role Relay Schema** -- every role relay must conform. (C-27 + C-30 combined: both named types
closed.)

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` -- field required in every valid relay. A relay missing a YES field is structurally invalid.
- `VIOLATION` -- row declares an anti-pattern. A relay exhibiting this pattern is structurally
  invalid regardless of whether any YES field is missing.

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

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step states its Schema 5
Prerequisite and Unblocks. `DEFECT: OUT-OF-ORDER-EXECUTION` if sequence violated.

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

### Verdict (Phase 5 -- Complete R9 Audit: C-30 + C-31 + C-32)

**C-29 audit** (ledger integrity -- BEFORE compliance ledger table, per C-32):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows in Defect code column cite a DefectCodeVocab code (not prose description):
  YES / NO
- (c) No empty cells in Defect code column -- every row carries `--` (PASS) or a
  DefectCodeVocab code (FAIL): YES / NO
- C-29 result: PASS (all three YES) / FAIL (any NO)

Fill the compliance ledger completely. One row per usage site declared in the Coverage Matrix
Referenced-by column. Every Defect code cell must carry a value: `--` for PASS rows, a
DefectCodeVocab code for FAIL rows. An empty Defect code cell is a C-32 violation detectable
by check (c) of the C-29 audit above. "Observed behavior: as expected" is structurally invalid.

**C-30 audit** (DefectCodeVocab closure):
- `DefectCodeVocab` declared as closed five-value type before registry table: YES / NO
- All five codes enumerated in the type declaration block: YES / NO
- Defect code column header in registry carries `(DefectCodeVocab)`: YES / NO
- C-30 result: PASS (all YES) / FAIL (any NO)

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared before relay schema table: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION in Required column: YES / NO
- All other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation -- 12 sites, including 2 C-29-composed per C-31):
- Coverage Matrix: (ContentVocab), (PhaseRef), (RoleRef), (VCIdentifier) on typed columns: YES / NO
- Schema 1: (SeverityVocab), (BlocksVocab): YES / NO
- Schema 2: (GapTypeVocab), (PromotionVocab): YES / NO
- Schema 3: (ChannelVocab), (ActivationPhaseRef): YES / NO
- Schema 4: (GateIdentifier), (BlockConditionVocab): YES / NO
- Schema 5: (StepIdentifier) on all three step-reference columns: YES / NO
- Role-Schema Binding Summary: (RoleName), (SeverityVocab), (GapTypeVocab): YES / NO
- Stage 1 table: (GapTypeVocab), (SeverityVocab), (PhaseRef): YES / NO
- Relay schema: (RequiredVocabulary): YES / NO
- Step 3b table: (GapTypeVocab), (SeverityVocab): YES / NO
- [C-29-composed site 1] Defect registry: Defect code column carries (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger: Defect code column carries (DefectCodeVocab): YES / NO
- **Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed)**: confirmed / mismatch
- C-28 result: PASS (all YES and count confirmed) / FAIL (any NO or mismatch)

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
