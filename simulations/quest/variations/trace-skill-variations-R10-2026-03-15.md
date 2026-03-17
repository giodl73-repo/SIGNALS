---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 10
rubric: trace-skill-rubric-v9-2026-03-15.md
---

# trace-skill — Variations R10 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R9 V-05 achieves C-01 through C-32 PASS under v8 scoring. v9 (updated after R9) formalizes three new aspirational criteria from R9 excellence signals: C-33 (C-30 upgrade), C-34 (C-31 upgrade), C-35 (C-32 upgrade).

**R9 C-30/C-31/C-32 PASS state and the R10 upgrade axis per criterion**:

- **C-30 (PASS in R9 V-01)**: `DefectCodeVocab` declared as closed five-value type before the registry table; all codes enumerated; column header carries `(DefectCodeVocab)`. C-33 upgrade: the closed-type declaration carries an explicit **named independence statement** — labeled structurally (not embedded in prose) so it is independently citable as the validation-independence property of the type, not just a description of what "closed" means.

- **C-31 (PASS in R9 V-02)**: C-28 audit tracks 12 total annotation sites (10 pre-C-29 + 2 C-29-composed) and terminates with "confirmed / mismatch." C-34 upgrade: the count assertion is restructured as a **self-evaluating COUNT GATE** — an explicit IF/THEN conditional that resolves to confirmed or mismatch based on whether actual count equals expected count. The gate is the count match condition; confirmed/mismatch is a derived result, not a fill-in-the-blank annotation.

- **C-32 (PASS in R9 V-03)**: C-29 audit at Verdict TOP, check (c) confirms no empty cells. C-35 upgrade: check (c) is promoted to a **structurally independent named PRE-READ GATE section** ordered before the C-29 audit and before the ledger table. A prompt instruction names this ordering as a structural requirement. Violations are caught before traversal begins, not discovered during row-by-row reading.

**R10 variation axes**:

- **V-01 (single axis: C-33)**: Independence statement as named structural element — `DefectCodeVocab` type declaration block carries a labeled `**Independence Statement**:` line, making the validation-independence property structurally isolated and independently citable.

- **V-02 (single axis: C-34)**: COUNT GATE self-evaluating block — C-28 audit restructures the count assertion into an explicit `**C-28 COUNT GATE**:` block with a conditional rule and a single-word gate verdict. The gate is the condition, not the annotation.

- **V-03 (single axis: C-35)**: PRE-READ GATE as named structural section — check (c) of C-29 is extracted into its own `**PRE-READ GATE**` section before the C-29 audit, with its own gate verdict slot and a prompt instruction declaring its ordering as a requirement.

- **V-04 (combined: C-33 + C-34)**: Named independence statement + COUNT GATE.

- **V-05 (combined: C-33 + C-34 + C-35)**: All three — complete R10 target.

All five inherit the full V-05 R9 architecture:
- Defect Classification Registry before Stage 1
- Coverage Matrix with 5 schemas and Role-binding column
- Role-Schema Binding Summary before Stage 2
- Per-role schema binding in Phase 1 Setup
- Schema 2 compliance field in Phase 2 Execute role relays with RequiredVocabulary type
- Uniform (TypeName) annotations across all schema tables (C-28)
- Structural mandates with defect codes (C-29)
- Compliance ledger Verdict fully populated with `--` sentinels (C-32)
- C-29 audit at Verdict TOP (C-32)
- DefectCodeVocab as closed five-value type (C-30)
- C-28 audit tracking 12 annotation sites (C-31)

---

## V-01 — Single axis: C-33 (Independence Statement as named structural element)

**Axis**: Phrasing register / structural labeling — the `DefectCodeVocab` type declaration block carries a dedicated `**Independence Statement**:` label that names the validation-independence property as a structural element of the type, rather than embedding the statement as a prose continuation of the code definitions.

**Hypothesis**: R9 V-05 has the independence statement text ("Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows") embedded as a prose lead-in before the bullet definitions. A scorer confirming C-33 must read and parse prose to locate the statement. C-33 requires the independence property to be a "named structural element" — labeling it `**Independence Statement**:` makes it independently citable, its location predictable, and its presence checkable without parsing the type's definition body. Risk: the label adds one line of instruction overhead. Mitigation: the label is co-located with the type declaration, mirrors the pattern of `**STRUCTURAL MANDATE**:` labels elsewhere in the prompt.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

**Independence Statement**: Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows — compliance is checked at the point of annotation, not by cross-referencing this table.

- `DEFECT: OPEN-WORLD-ASSERTION` — a phase referenced a label not declared in the Coverage Matrix.
- `DEFECT: RELAY-SCHEMA-VIOLATION` — a relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` — a promoted SA gap retained its SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` — a sub-step ran before its prerequisite was satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` — Phase 4 was entered while any enforcement gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure — undeclared label referenced | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema — required field omitted or anti-pattern exhibited | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock — promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering — sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop — Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE — CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any phase referencing a label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful — blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only — no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE — LABEL LOCK**: A promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. A promoted gap retaining SA is a label lock violation.
`DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent — spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
| SG | Setup gap — declared; invoker cannot supply | Carry with SG label |
| EG | Execute gap — contract requires; role cannot produce | Surface in Execute; carry to Findings |
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

**STRUCTURAL MANDATE — GATE HARD-STOP**: Phase 4 is valid only when all gates PASS. Phase 4 entered while any gate = FAIL is a hard-stop violation. `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE — SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite is satisfied is a sequencing violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

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

### Stage 1 — Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using Schema 2 (GapTypeVocab) and Schema 1 (SeverityVocab).

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

### Stage 2 — Hand-Compilation

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
  Reason: [why — one sentence]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock active: promoted gaps use SG in all downstream phases.
`DEFECT: LABEL-LOCK-VIOLATION` if any promoted gap uses SA label downstream.

---

#### Phase 1 — Setup

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
  SA/SG gaps binding this role: [list or "none — confirmed"]
  EG gaps expected: [list or "none — confirmed"]
```

A role entry without schema binding declaration is invalid. "none — confirmed" only after verifying.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 — Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by spec must appear.

**Role Relay Schema** — every role relay must conform.

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` — field required in every valid relay. A relay missing a YES field is structurally invalid.
- `VIOLATION` — row declares an anti-pattern. A relay exhibiting this pattern is structurally invalid regardless of whether any YES field is missing.

**STRUCTURAL MANDATE — RELAY SCHEMA**: A relay omitting any YES field or exhibiting the VIOLATION pattern is a schema violation. `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] — all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none — confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section:

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none — confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 — Findings

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step states its Schema 5 Prerequisite and Unblocks. `DEFECT: OUT-OF-ORDER-EXECUTION` if sequence violated.

##### Step 3a — Severity Legend Declaration

**Schema 5 prerequisite (StepIdentifier)**: Schema 1 declared in Coverage Matrix.
**Schema 5 unblocks (StepIdentifier)**: Step 3b.

| Label (SeverityVocab) | Definition for this trace | Actionability threshold |
|-----------------------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

##### Step 3b — Findings Table

**Schema 5 prerequisite**: Step 3a complete. **Schema 5 unblocks**: Step 3c.

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

##### Step 3c — Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated. **Schema 5 unblocks**: Step 3d (if all-PASS).

**STRUCTURAL MANDATE — GATE HARD-STOP** (Schema 4): FAIL on any gate BLOCKS Step 3d and Phase 4. `DEFECT: PREMATURE-PHASE-ADVANCE`

**G-1** — Source types in Step 3b: [list] — Result: PASS / FAIL
**G-2** — Same-Source pairs: [list or "none"] — Result: PASS / FAIL
**G-3** — Severity labels in Step 3b: [list] — Result: PASS / FAIL

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

##### Step 3d — Channel Taxonomy Activation

**Schema 5 prerequisite**: Step 3c all-PASS. **Schema 5 unblocks**: Phase 4.

Activate Schema 3 channels: spec / invocation / artifact / quality.
Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 — Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Phase 4 BLOCKED. Return to Step 3c.

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}` (GapTypeVocab)] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality (ChannelVocab)] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

---

### Verdict (Phase 5 — C-33 + C-31 + C-32 Audit)

**C-29 audit** (ledger integrity — BEFORE compliance ledger table, per C-32):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows in Defect code column cite a DefectCodeVocab code (not prose): YES / NO
- (c) No empty cells in Defect code column — every row carries `--` (PASS) or a DefectCodeVocab code (FAIL): YES / NO
- C-29 result: PASS (all three YES) / FAIL (any NO)

Fill the compliance ledger completely. Every Defect code cell must carry a value: `--` for PASS rows, a DefectCodeVocab code for FAIL rows.

**C-33 audit** (Independence Statement — named structural element):
- `DefectCodeVocab` type declaration block contains a labeled `**Independence Statement**:` line: YES / NO
- Independence statement asserts validation without consulting registry rows: YES / NO
- C-33 result: PASS (both YES) / FAIL (any NO)

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

**C-28 audit** (uniform type annotation — 12 sites, including 2 C-29-composed per C-31):
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
| VC-5 | Schema 5 | 3a → 3b | Step 3b waited for Step 3a completion | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b → 3c | Step 3c waited for Step 3b population | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c → 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 waited for Step 3d channel activation | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**VC-1 through VC-5 overall**: PASS if all rows in group PASS / FAIL otherwise

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 — Single axis: C-34 (COUNT GATE as self-evaluating block)

**Axis**: Output format — the C-28 audit count assertion is restructured from a prose-embedded "confirmed / mismatch" strike-through annotation into a dedicated `**C-28 COUNT GATE**` block with an explicit conditional rule. The gate block declares: expected count, space for actual count, and an IF/THEN rule that produces the gate verdict. The block is structurally separate from the YES/NO tally lines above it.

**Hypothesis**: R9 V-05's count assertion is `**Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed)**: confirmed / mismatch` — a hybrid of reported number and annotation. A scorer confirming C-34 must infer that "confirmed" means "count matched" and that this is a gate. C-34 requires the assertion to be "self-evaluating rather than a tally requiring external judgment." Structuring it as an IF/THEN COUNT GATE block removes the inference: the condition is stated, the result is derived, and the gate is independent of the YES/NO line tally above it. Risk: adds three lines to the C-28 audit block. Mitigation: the gate block is structurally parallel to G-1/G-2/G-3 in Step 3c, a pattern already established in the prompt.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows:
- `DEFECT: OPEN-WORLD-ASSERTION` — a phase referenced a label not declared in the Coverage Matrix.
- `DEFECT: RELAY-SCHEMA-VIOLATION` — a relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` — a promoted SA gap retained its SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` — a sub-step ran before its prerequisite was satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` — Phase 4 was entered while any enforcement gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure — undeclared label referenced | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema — required field omitted or anti-pattern exhibited | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock — promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering — sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop — Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE — CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any phase referencing a label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful — blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only — no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE — LABEL LOCK**: A promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. `DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent — spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
| SG | Setup gap — declared; invoker cannot supply | Carry with SG label |
| EG | Execute gap — contract requires; role cannot produce | Surface in Execute; carry to Findings |
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

**STRUCTURAL MANDATE — GATE HARD-STOP**: Phase 4 is valid only when all gates PASS. `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE — SUB-STEP SEQUENCE**: `DEFECT: OUT-OF-ORDER-EXECUTION`

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

---

### Stage 1 — Source-Layer Auditor

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]
[layer diversity (DiversityVocab): PASS / FAIL]
```

---

### Stage 2 — Hand-Compilation

**Relay received**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

#### SA-TO-SG PROMOTION

`PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

```
SA-NN -> [result (PromotionVocab)]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

#### Phase 1 — Setup

- [topic: ]  [scope_in: ]  [scope_out: ]  [roles: ]  [stack: ]  [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding (SeverityVocab): [labels]
  Schema 2 binding (GapTypeVocab): [labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none — confirmed"]
  EG gaps expected: [list or "none — confirmed"]
```

#### Phase 2 — Execute

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.

**STRUCTURAL MANDATE — RELAY SCHEMA**: `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] — all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list or "none — confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

#### Phase 3 — Findings (Steps 3a → 3b → 3c → 3d per Schema 5)

**Step 3a**: Severity legend. **Step 3b**: Findings table (>=2 entries, >=2 Source types). **Step 3c**: Gates G-1/G-2/G-3. **Step 3d**: Channel taxonomy activation.

#### Phase 4 — Amend

Schema 4 pre-check before entry. Every Amend entry carries [remediation channel] from ChannelVocab.

---

### Verdict (Phase 5 — C-34 COUNT GATE + C-30 + C-31 + C-32 Audit)

**C-29 audit** (ledger integrity — BEFORE compliance ledger table):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows cite a DefectCodeVocab code (not prose): YES / NO
- (c) No empty cells in Defect code column — every row carries `--` or a DefectCodeVocab code: YES / NO
- C-29 result: PASS (all three YES) / FAIL (any NO)

**C-30 audit** (DefectCodeVocab closure):
- Closed five-value type declared before registry: YES / NO
- All five codes enumerated in declaration: YES / NO
- Registry column header carries (DefectCodeVocab): YES / NO
- C-30 result: PASS / FAIL

**C-27 audit** (RequiredVocabulary closure):
- Declared as closed two-value type before relay schema: YES / NO
- Column header carries (RequiredVocabulary): YES / NO
- Anti-pattern row carries VIOLATION: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation — 12 sites):
- Coverage Matrix typed columns annotated: YES / NO
- Schema 1 typed columns: YES / NO
- Schema 2 typed columns: YES / NO
- Schema 3 typed columns: YES / NO
- Schema 4 typed columns: YES / NO
- Schema 5 typed columns: YES / NO
- Role-Schema Binding Summary typed columns: YES / NO
- Stage 1 table typed columns: YES / NO
- Relay schema typed column: YES / NO
- Step 3b table typed columns: YES / NO
- [C-29-composed site 1] Defect registry Defect code column carries (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger Defect code column carries (DefectCodeVocab): YES / NO

**C-28 COUNT GATE** (self-evaluating — this gate resolves the audit, not the YES/NO tally alone):
- Expected annotation sites: 12 (10 pre-C-29 + 2 C-29-composed)
- Actual annotation sites confirmed above: [count the YES lines above]
- Rule: IF actual = 12 → **confirmed**; IF actual ≠ 12 → **mismatch**
- COUNT GATE result: **confirmed** / **mismatch** [write one — this is the gate]
- C-28 result: PASS (all YES AND COUNT GATE = confirmed) / FAIL (any NO OR COUNT GATE = mismatch)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|-------------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 | [legend stated] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3b | All entries use P1/P2/P3 only | [labels used; count] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate verified | [G-3 result] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries use P1/P2/P3 only | [labels in Amend] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 per binding column | [labels used] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [labels in Stage 1] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; no SA downstream | [which SA promoted] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted show SG | [labels in Step 3b] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance present; Source labels valid | [compliance field value] | PASS / FAIL | -- / DEFECT: RELAY-SCHEMA-VIOLATION |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels; missing count] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [gate results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [gate values at entry] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source coverage checked across all roles | [Source types per role] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a → 3b | Step 3b waited for Step 3a | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b → 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c → 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 — Single axis: C-35 (PRE-READ GATE as named structural section)

**Axis**: Lifecycle emphasis — check (c) of the C-29 audit (no empty cells) is extracted from its position as item three in a three-item checklist and promoted to a standalone `**PRE-READ GATE**` section with its own header, gate verdict slot, and a prompt instruction that names its ordering as a structural requirement. The remaining C-29 audit (checks a and b) runs after the PRE-READ GATE passes.

**Hypothesis**: R9 V-05 places check (c) at the bottom of a three-item C-29 audit block labeled "BEFORE compliance ledger table." A scorer confirming C-35 must infer that the block is a gate and that check (c) is structurally ordered before ledger reading. C-35 requires "pre-read ordering is a named structural requirement, making the empty-cell check a gate rather than a post-hoc discovery." Extracting check (c) into its own section with a gate label and a "DO NOT proceed to ledger until this gate passes" instruction makes the ordering a named structural requirement rather than an emergent sequence. The section header itself enforces ordering: a reader who encounters `**PRE-READ GATE**` before the ledger table cannot read the ledger before resolving it. Risk: two audit blocks where one existed increases structural overhead. Mitigation: each block is smaller and its purpose is immediately clear from its name.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows:
- `DEFECT: OPEN-WORLD-ASSERTION` — a phase referenced a label not declared in the Coverage Matrix.
- `DEFECT: RELAY-SCHEMA-VIOLATION` — a relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` — a promoted SA gap retained its SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` — a sub-step ran before its prerequisite was satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` — Phase 4 was entered while any enforcement gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure — undeclared label referenced | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema — required field omitted or anti-pattern exhibited | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock — promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering — sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop — Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE — CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. `DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE — LABEL LOCK**: `DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
| SG | Setup gap | Carry with SG label |
| EG | Execute gap | Surface in Execute; carry to Findings |
| QO | Quality observation | P3 severity typical |

#### Remediation Channel Taxonomy (Schema 3)

`ChannelVocab` = {spec, invocation, artifact, quality}. `ActivationPhaseRef` = {Step 3d}.

| Channel (ChannelVocab) | Targets | Activated-at (ActivationPhaseRef) |
|------------------------|---------|-----------------------------------|
| spec | Skill specification | Step 3d |
| invocation | How skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement | Step 3d |

#### Enforcement Gate Registry (Schema 4)

`GateIdentifier` = {G-1, G-2, G-3}. `BlockConditionVocab` = {Phase 4 BLOCKED while FAIL}.

**STRUCTURAL MANDATE — GATE HARD-STOP**: `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no duplicate Action text within same Source | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE — SUB-STEP SEQUENCE**: `DEFECT: OUT-OF-ORDER-EXECUTION`

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
| [role from spec] | [severity labels] | [Source labels; label lock rules] | [schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Auditor

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**: [SA: `{{sa_list}}`] [SG: `{{sg_list}}`] [EG: `{{eg_list}}`] [diversity (DiversityVocab): PASS / FAIL]

---

### Stage 2 — Hand-Compilation

**Relay received**: [SA / SG / EG / diversity as relayed]. Do not re-derive.

#### SA-TO-SG PROMOTION

For every SA gap: `SA-NN -> [result (PromotionVocab)]: Gap / Promotion / Reason`

#### Phase 1 — Setup

Confirm inputs. Per-role: Schema 1 binding, Schema 2 binding, SA/SG gaps, EG expected.

#### Phase 2 — Execute

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.

**STRUCTURAL MANDATE — RELAY SCHEMA**: `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels: [list (GapTypeVocab)] — valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list or "none — confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

#### Phase 3 — Findings

Steps 3a (severity legend) → 3b (findings table) → 3c (gates) → 3d (channel activation). Schema 5 transition stated at each step.

#### Phase 4 — Amend

Gate pre-check before entry. Amend entries carry channel from ChannelVocab.

---

### Verdict (Phase 5 — C-35 PRE-READ GATE + C-30 + C-31 + C-32 Audit)

**PRE-READ GATE** — C-35 structural mandate: this section runs before reading any compliance ledger row. It is not part of the C-29 audit list. It is a named structural requirement ordered here by prompt instruction. Violations caught here are flagged before traversal begins.

- Check: No empty cells in Defect code column — every row must carry `--` (PASS rows) or a DefectCodeVocab code (FAIL rows). An empty cell is structurally invalid before any row is read.
- PRE-READ GATE result: PASS / FAIL
- If FAIL: the Defect code column has at least one empty cell. Do not proceed to ledger reading. Write the row number(s) and tag them before continuing.

PRE-READ GATE must be PASS before proceeding to C-29 audit or compliance ledger.

---

**C-29 audit** (ledger integrity — runs after PRE-READ GATE PASS; checks registry and code-source compliance):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows cite a DefectCodeVocab code (not prose description): YES / NO
- C-29 result: PASS (both YES AND PRE-READ GATE passed) / FAIL (any NO or PRE-READ GATE failed)

**C-30 audit** (DefectCodeVocab closure):
- Closed five-value type declared before registry: YES / NO
- All five codes enumerated: YES / NO
- Registry column header carries (DefectCodeVocab): YES / NO
- C-30 result: PASS / FAIL

**C-27 audit**: RequiredVocabulary declared / column header / VIOLATION row / all-YES — C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation — 12 sites including 2 C-29-composed):
- [10 pre-C-29 sites — Coverage Matrix, Schemas 1–5, Role-Schema Binding, Stage 1, Relay schema, Step 3b]: each YES / NO
- [C-29-composed site 1] Defect registry (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger (DefectCodeVocab): YES / NO
- **Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed)**: confirmed / mismatch
- C-28 result: PASS (all YES and count confirmed) / FAIL (any NO or mismatch)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|-------------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend written | [legend] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [labels; count] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate verified | [G-3 result] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries P1/P2/P3 only | [labels] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 | [labels] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [labels] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted → SG; no SA downstream | [promotions] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [labels] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance field present and valid | [compliance value] | PASS / FAIL | -- / DEFECT: RELAY-SCHEMA-VIOLATION |
| VC-3 | Schema 3 | Step 3d | Channels activated | [activation language] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel | [channels used] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered after all gates PASS | [gate values] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source types across all roles | [types per role] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a → 3b | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b → 3c | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c → 3d | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d → Phase 4 | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 — Combined axes: C-33 + C-34 (Named Independence Statement + COUNT GATE)

**Axes**: V-01 (C-33: `**Independence Statement**:` label in DefectCodeVocab type declaration) + V-02 (C-34: `**C-28 COUNT GATE**` block with IF/THEN conditional rule).

**Hypothesis**: C-33 and C-34 operate at distinct structural layers — C-33 in the Defect Classification Registry before Stage 1, C-34 in the Verdict audit block. They are compositionally independent: neither upgrade interacts with the other's mechanism. V-04 combines them to confirm additive compliance. V-03's C-35 change is held out to isolate whether the pre-read gate section introduces any interaction with the C-29 audit block restructuring. Expected behavior: all C-01 through C-34 pass; C-35 fails on the "named pre-read gate as structural requirement" criterion because check (c) remains item three in a three-item C-29 list.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

**Independence Statement**: Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows — compliance is checked at the point of annotation, not by cross-referencing this table.

- `DEFECT: OPEN-WORLD-ASSERTION` — undeclared label referenced in a phase.
- `DEFECT: RELAY-SCHEMA-VIOLATION` — relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` — promoted SA gap retained SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` — sub-step ran before prerequisite satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` — Phase 4 entered while any gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure — undeclared label referenced | Trace invalid |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema — required field omitted or anti-pattern exhibited | Trace invalid |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock — SA label retained after PROMOTION | Trace invalid |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering — prerequisite not satisfied | Trace invalid |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop — Phase 4 entered while gate = FAIL | Trace invalid |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE — CLOSED WORLD**: `DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE — LABEL LOCK**: `DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent | Evaluate at PROMOTION; promoted use SG downstream |
| SG | Setup gap | Carry with SG label |
| EG | Execute gap | Surface in Execute |
| QO | Quality observation | P3 typical |

#### Remediation Channel Taxonomy (Schema 3)

`ChannelVocab` = {spec, invocation, artifact, quality}. `ActivationPhaseRef` = {Step 3d}.

| Channel (ChannelVocab) | Targets | Activated-at (ActivationPhaseRef) |
|------------------------|---------|-----------------------------------|
| spec | Skill specification | Step 3d |
| invocation | How skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement | Step 3d |

#### Enforcement Gate Registry (Schema 4)

`GateIdentifier` = {G-1, G-2, G-3}. `BlockConditionVocab` = {Phase 4 BLOCKED while FAIL}.

**STRUCTURAL MANDATE — GATE HARD-STOP**: `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no duplicate Action within same Source | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: only P1/P2/P3 in Step 3b | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE — SUB-STEP SEQUENCE**: `DEFECT: OUT-OF-ORDER-EXECUTION`

| Step (StepIdentifier) | Prerequisite (StepIdentifier) | Produces | Unblocks (StepIdentifier) |
|-----------------------|------------------------------|---------|--------------------------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table | Step 3c |
| Step 3c | Step 3b populated | Gate results | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

`RoleName` = {role name strings from skill spec}.

| Role (RoleName) | Schema 1 binding (SeverityVocab) | Schema 2 binding (GapTypeVocab) | Notes |
|-----------------|----------------------------------|--------------------------------|-------|
| [role] | [severity labels] | [Source labels; label lock rules] | [schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Auditor

`DiversityVocab` = {PASS, FAIL}.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**: [SA] [SG] [EG] [diversity (DiversityVocab): PASS / FAIL]

---

### Stage 2 — Hand-Compilation

#### SA-TO-SG PROMOTION

For every SA gap: Gap / Promotion (PromotionVocab) / Reason. Label lock active downstream.

#### Phase 1 — Setup

Confirm inputs. Per-role schema bindings (SeverityVocab, GapTypeVocab), SA/SG attribution, EG expected.

#### Phase 2 — Execute

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.

**STRUCTURAL MANDATE — RELAY SCHEMA**: `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels: [list (GapTypeVocab)] — valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list or "none — confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

#### Phase 3 — Findings

Steps 3a → 3b → 3c → 3d per Schema 5 sequence. Schema 5 transitions stated at each step.

#### Phase 4 — Amend

Gate pre-check. Amend entries carry ChannelVocab channel.

---

### Verdict (Phase 5 — C-33 + C-34 + C-30 + C-31 + C-32 Audit)

**C-29 audit** (ledger integrity — BEFORE compliance ledger table):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows cite a DefectCodeVocab code (not prose): YES / NO
- (c) No empty cells in Defect code column — every row carries `--` or a DefectCodeVocab code: YES / NO
- C-29 result: PASS (all three YES) / FAIL (any NO)

**C-33 audit** (Independence Statement as named structural element):
- `DefectCodeVocab` type declaration block contains a labeled `**Independence Statement**:` line: YES / NO
- Statement asserts validation without consulting registry rows: YES / NO
- C-33 result: PASS (both YES) / FAIL (any NO)

**C-30 audit** (DefectCodeVocab closure):
- Closed five-value type declared before registry: YES / NO
- All five codes enumerated in declaration: YES / NO
- Registry column header carries (DefectCodeVocab): YES / NO
- C-30 result: PASS / FAIL

**C-27 audit**: RequiredVocabulary type / column header / VIOLATION row / all-YES — C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation — 12 sites):
- Coverage Matrix typed columns: YES / NO
- Schema 1: YES / NO
- Schema 2: YES / NO
- Schema 3: YES / NO
- Schema 4: YES / NO
- Schema 5: YES / NO
- Role-Schema Binding Summary: YES / NO
- Stage 1 table: YES / NO
- Relay schema: YES / NO
- Step 3b table: YES / NO
- [C-29-composed site 1] Defect registry (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger (DefectCodeVocab): YES / NO

**C-28 COUNT GATE** (C-34 — self-evaluating; this gate resolves C-28 status independently of the YES/NO tally):
- Expected annotation sites: 12 (10 pre-C-29 + 2 C-29-composed)
- Actual annotation sites confirmed in the audit lines above: [count]
- Rule: IF actual = 12 → **confirmed**; IF actual ≠ 12 → **mismatch**
- COUNT GATE result: **confirmed** / **mismatch** [write one — this is the gate; mismatch = C-28 FAIL without further inspection]
- C-28 result: PASS (all YES AND COUNT GATE = confirmed) / FAIL (any NO OR COUNT GATE = mismatch)

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|-------------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend written | [legend] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3b | Entries use P1/P2/P3 only | [labels; count] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate verified | [G-3 result] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | Amend entries P1/P2/P3 only | [labels] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-1 | Schema 1 | [role] EG findings | Role binds Schema 1 | [labels] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [labels] | PASS / FAIL | -- / DEFECT: OPEN-WORLD-ASSERTION |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted → SG; no SA downstream | [promotions] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [labels] | PASS / FAIL | -- / DEFECT: LABEL-LOCK-VIOLATION |
| VC-2 | Schema 2 | [role] relay | Schema 2 compliance present and valid | [compliance value] | PASS / FAIL | -- / DEFECT: RELAY-SCHEMA-VIOLATION |
| VC-3 | Schema 3 | Step 3d | Channels activated | [activation] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel | [channels] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source types across all roles | [types per role] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a → 3b | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b → 3c | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c → 3d | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d → Phase 4 | Transition waited | [evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 — Combined axes: C-33 + C-34 + C-35 (complete R10 target)

**Axes**: All three:
- C-33 (V-01): `**Independence Statement**:` labeled line in DefectCodeVocab type declaration block
- C-34 (V-02): `**C-28 COUNT GATE**` block with IF/THEN rule; gate result is **confirmed** / **mismatch**
- C-35 (V-03): `**PRE-READ GATE**` named structural section before C-29 audit and compliance ledger; check (c) extracted as the gate; prompt instruction names the ordering as a structural requirement

**Hypothesis**: C-33 and C-34 are additive (confirmed by V-04). C-35 interacts with C-29: the pre-read gate extracts check (c) from the C-29 audit list, leaving C-29 with only checks (a) and (b). The C-29 result condition changes: "PASS (both YES AND PRE-READ GATE passed)" rather than "all three YES." This is the correct interaction: the pre-read gate is not a C-29 subcheck but a structurally independent gate that precedes it. The compliance ledger cannot be read until the PRE-READ GATE passes — the gate is ordered by section position, not by list order. V-05 satisfies all 27 aspirational criteria.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed five-value type:
`{DEFECT: OPEN-WORLD-ASSERTION, DEFECT: RELAY-SCHEMA-VIOLATION, DEFECT: LABEL-LOCK-VIOLATION,
DEFECT: OUT-OF-ORDER-EXECUTION, DEFECT: PREMATURE-PHASE-ADVANCE}`

**Independence Statement**: Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows — compliance is checked at the point of annotation, not by cross-referencing this table.

- `DEFECT: OPEN-WORLD-ASSERTION` — a phase referenced a label not declared in the Coverage Matrix.
- `DEFECT: RELAY-SCHEMA-VIOLATION` — a relay omitted a required field or exhibited the prohibited pattern.
- `DEFECT: LABEL-LOCK-VIOLATION` — a promoted SA gap retained its SA label after PROMOTION.
- `DEFECT: OUT-OF-ORDER-EXECUTION` — a sub-step ran before its prerequisite was satisfied.
- `DEFECT: PREMATURE-PHASE-ADVANCE` — Phase 4 was entered while any enforcement gate = FAIL.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure — undeclared label referenced | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema — required field omitted or anti-pattern exhibited | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock — promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering — sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop — Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |

---

### Trace Protocol Schemas (Coverage Matrix)

`ContentVocab` = {vocabulary name string}. `PhaseRef` = {phase or step name string}.
`VCIdentifier` = {VC-1 | VC-2 | VC-3 | VC-4 | VC-5}. `RoleRef` = {role name or "N/A"}.

**STRUCTURAL MANDATE — CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any phase referencing a label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute role relay | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All roles (via Phase 4) | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1: all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (all transitions) | N/A | VC-5 |

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful — blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only — no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

**STRUCTURAL MANDATE — LABEL LOCK**: A promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. A promoted gap retaining SA is a label lock violation.
`DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent — spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted use SG downstream |
| SG | Setup gap — declared; invoker cannot supply | Carry with SG label |
| EG | Execute gap — contract requires; role cannot produce | Surface in Execute; carry to Findings |
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

**STRUCTURAL MANDATE — GATE HARD-STOP**: Phase 4 is valid only when all gates PASS. Phase 4 entered while any gate = FAIL is a hard-stop violation. `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

**STRUCTURAL MANDATE — SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite is satisfied is a sequencing violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

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

### Stage 1 — Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using Schema 2 (GapTypeVocab) and Schema 1 (SeverityVocab).

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

### Stage 2 — Hand-Compilation

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
  Reason: [why — one sentence]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock active: promoted gaps use SG in all downstream phases.
`DEFECT: LABEL-LOCK-VIOLATION` if any promoted gap uses SA label downstream.

---

#### Phase 1 — Setup

Confirm each input with `[name: value]` notation:

- [topic: ]  [scope_in: ]  [scope_out: ]  [roles: ]  [stack: ]  [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding (SeverityVocab): [severity labels applicable to this role's findings]
  Schema 2 binding (GapTypeVocab): [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none — confirmed"]
  EG gaps expected: [list or "none — confirmed"]
```

A role entry without schema binding declaration is invalid.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 — Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by spec must appear.

**Role Relay Schema** — every role relay must conform. (C-27 + C-33 combined: both named types closed with vocabulary and independence properties declared.)

`RequiredVocabulary` is a closed two-value type: `{YES, VIOLATION}`.
- `YES` — field required in every valid relay. A relay missing a YES field is structurally invalid.
- `VIOLATION` — row declares an anti-pattern. A relay exhibiting this pattern is structurally invalid regardless of whether any YES field is missing.

**STRUCTURAL MANDATE — RELAY SCHEMA**: A relay omitting any YES field or exhibiting the VIOLATION pattern is a schema violation. `DEFECT: RELAY-SCHEMA-VIOLATION`

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] — all valid: YES / NO | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none — confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| DO NOT omit Schema 2 compliance field | Relay without Schema 2 compliance is structurally invalid | VIOLATION |

For each role, open its relay before writing the artifact section:

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from SA/SG/EG/QO: YES / NO
- SA/SG gaps affecting this role: [list or "none — confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 — Findings

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step states its Schema 5 Prerequisite and Unblocks. `DEFECT: OUT-OF-ORDER-EXECUTION` if sequence violated.

##### Step 3a — Severity Legend Declaration

**Schema 5 prerequisite (StepIdentifier)**: Schema 1 declared in Coverage Matrix.
**Schema 5 unblocks (StepIdentifier)**: Step 3b.

| Label (SeverityVocab) | Definition for this trace | Actionability threshold |
|-----------------------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

##### Step 3b — Findings Table

**Schema 5 prerequisite**: Step 3a complete. **Schema 5 unblocks**: Step 3c.

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

##### Step 3c — Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated. **Schema 5 unblocks**: Step 3d (if all-PASS).

**STRUCTURAL MANDATE — GATE HARD-STOP** (Schema 4): FAIL on any gate BLOCKS Step 3d and Phase 4. `DEFECT: PREMATURE-PHASE-ADVANCE`

**G-1** — Source types in Step 3b: [list] — Result: PASS / FAIL
**G-2** — Same-Source pairs: [list or "none"] — Result: PASS / FAIL
**G-3** — Severity labels in Step 3b: [list] — Result: PASS / FAIL

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

##### Step 3d — Channel Taxonomy Activation

**Schema 5 prerequisite**: Step 3c all-PASS. **Schema 5 unblocks**: Phase 4.

Activate Schema 3 channels: spec / invocation / artifact / quality.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 — Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Return to Step 3c.

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}` (GapTypeVocab)]
- [remediation channel: spec / invocation / artifact / quality (ChannelVocab)]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

---

### Verdict (Phase 5 — Complete R10 Audit: C-33 + C-34 + C-35 + C-30 + C-31 + C-32)

**PRE-READ GATE** — C-35 structural requirement: this section is a named structural mandate ordered by prompt instruction before the C-29 audit and before the compliance ledger table. It runs before any ledger row is read. Violations are caught and flagged here; they are not discovered during row-by-row traversal.

- Check: No empty cells in Defect code column — every compliance ledger row must carry `--` (PASS rows) or a DefectCodeVocab code (FAIL rows). An empty Defect code cell is structurally invalid at this gate.
- PRE-READ GATE result: PASS / FAIL
- If FAIL: write the row index of each empty cell and tag it before proceeding. Do not read any ledger row until this gate returns PASS.

PRE-READ GATE PASS is required before the C-29 audit and compliance ledger below.

---

**C-29 audit** (ledger integrity — runs after PRE-READ GATE PASS; checks registry presence and code-source compliance):
- (a) Defect Classification Registry declared before Stage 1: YES / NO
- (b) All FAIL rows cite a DefectCodeVocab code (not prose description): YES / NO
- C-29 result: PASS (both YES AND PRE-READ GATE = PASS) / FAIL (any NO or PRE-READ GATE = FAIL)

**C-33 audit** (Independence Statement as named structural element):
- `DefectCodeVocab` type declaration block contains a labeled `**Independence Statement**:` line: YES / NO
- Statement explicitly asserts validation without consulting registry rows: YES / NO
- C-33 result: PASS (both YES) / FAIL (any NO)

**C-30 audit** (DefectCodeVocab closure):
- `DefectCodeVocab` declared as closed five-value type before registry table: YES / NO
- All five codes enumerated in the type declaration block: YES / NO
- Registry Defect code column header carries `(DefectCodeVocab)`: YES / NO
- C-30 result: PASS (all YES) / FAIL (any NO)

**C-27 audit** (RequiredVocabulary closure):
- `RequiredVocabulary = {YES, VIOLATION}` declared as closed two-value type before relay schema: YES / NO
- Column header `Required (RequiredVocabulary)` present: YES / NO
- Anti-pattern row carries VIOLATION in Required column: YES / NO
- All other rows carry YES: YES / NO
- C-27 result: PASS / FAIL

**C-28 audit** (uniform type annotation — 12 sites, including 2 C-29-composed):
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
- [C-29-composed site 1] Defect registry Defect code column carries (DefectCodeVocab): YES / NO
- [C-29-composed site 2] Verdict compliance ledger Defect code column carries (DefectCodeVocab): YES / NO

**C-28 COUNT GATE** (C-34 — self-evaluating; resolves C-28 audit status independently):
- Expected annotation sites: 12 (10 pre-C-29 + 2 C-29-composed)
- Actual annotation sites confirmed above: [count the YES lines]
- Rule: IF actual = 12 → **confirmed**; IF actual ≠ 12 → **mismatch**
- COUNT GATE result: **confirmed** / **mismatch** [write one — this is the gate; mismatch = C-28 FAIL]
- C-28 result: PASS (all YES AND COUNT GATE = confirmed) / FAIL (any NO OR COUNT GATE = mismatch)

Fill the compliance ledger. Every Defect code cell must carry a value (`--` or a DefectCodeVocab code) — confirmed by the PRE-READ GATE above. "Observed behavior: as expected" is structurally invalid.

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
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [channels used; missing count] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 run with explicit PASS/FAIL | [G-1/G-2/G-3 results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL | -- / DEFECT: PREMATURE-PHASE-ADVANCE |
| VC-4 | Schema 4 | G-1 role aggregation | Source coverage checked across all roles | [Source types per role] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a → 3b | Step 3b waited for Step 3a completion | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3b → 3c | Step 3c waited for Step 3b population | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3c → 3d | Step 3d waited for Step 3c all-PASS | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 waited for Step 3d channel activation | [transition evidence] | PASS / FAIL | -- / DEFECT: OUT-OF-ORDER-EXECUTION |

**VC-1 through VC-5 overall**: PASS if all rows in group PASS / FAIL otherwise

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

**Variation summary**:

| Variation | C-33 axis | C-34 axis | C-35 axis | Expected new passes |
|-----------|-----------|-----------|-----------|---------------------|
| V-01 | `**Independence Statement**:` label in type block | R9 V-05 (confirmed/mismatch inline) | R9 V-05 (check c in C-29 list) | C-33 |
| V-02 | R9 V-05 (prose independence) | `**C-28 COUNT GATE**` IF/THEN block | R9 V-05 (check c in C-29 list) | C-34 |
| V-03 | R9 V-05 (prose independence) | R9 V-05 (confirmed/mismatch inline) | `**PRE-READ GATE**` named section | C-35 |
| V-04 | `**Independence Statement**:` label | `**C-28 COUNT GATE**` block | R9 V-05 (check c in C-29 list) | C-33, C-34 |
| V-05 | `**Independence Statement**:` label | `**C-28 COUNT GATE**` block | `**PRE-READ GATE**` named section | C-33, C-34, C-35 |
