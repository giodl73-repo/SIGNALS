---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 16
rubric: trace-skill-rubric-v15-2026-03-15.md
---

# trace-skill -- Variations R16 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R15 V-05 achieves C-01 through C-47 PASS under v15 scoring. v15 (updated
after R15) formalizes one new aspirational criterion: C-47 (ANNOTATION SCOPE REGISTRY is
registered as a named component in the Template Component Registry as TCR row 5, making its
presence verifiable by TCR row lookup rather than Verdict-section scan or table-name search).

**R15 V-04 / V-05 discrimination signal** (scored against v15):

- R15 V-04 implements the ANNOTATION SCOPE REGISTRY as a formal table (C-46 PASS) but keeps
  the TCR at 4 components -- the ANNOTATION SCOPE REGISTRY is a peer artifact rather than a
  declared TCR component. C-47 = FAIL for V-04.

- R15 V-05 adds TCR row 5 naming the ANNOTATION SCOPE REGISTRY as a required prompt component
  with its typed-column notation `# / Column name (TypeName) / Host registry / table`. The
  ANNOTATION SCOPE REGISTRY header says "(Component 5 of Template Component Registry)". The
  CONFORMANCE-COLLAPSE CLAIM updates to reference rows 1-5 and names TCR row 5 by its registry
  function. C-47 = PASS for V-05.

Entry state = R15 V-05. All C-01 through C-47 PASS.

**R16 upgrade axes** -- exploring the next structural refinement layer within C-47-passing
prompts:

- **V-01 (single axis: TCR row 5 self-citation)**: TCR row 5 Component description carries
  `(C-47)` criterion citation in parentheses, making the TCR row independently traceable to
  its governing criterion by header scan alone -- paralleling C-39's self-citing STRUCTURAL
  MANDATE block headers and C-45's self-citing SCORER HEURISTIC label. The ANNOTATION SCOPE
  REGISTRY table and SCORER HEURISTIC are unchanged from entry state.

- **V-02 (single axis: ANNOTATION SCOPE REGISTRY self-lists its own typed column)**: ANNOTATION
  SCOPE REGISTRY adds row 29 for `Column name (TypeName) | ANNOTATION SCOPE REGISTRY` -- the
  registry enumerates all typed columns in the prompt including its own, making it self-complete.
  Expected annotation count changes to 29. TCR row 5 and SCORER HEURISTIC unchanged.

- **V-03 (single axis: SCORER HEURISTIC cites C-47 explicitly in its confirmation path)**:
  SCORER HEURISTIC (C-43) names C-47 explicitly: "confirming C-47 compliance by locating TCR
  row 5 and verifying the ANNOTATION SCOPE REGISTRY appears in the Verdict C-28 COUNT GATE
  section" -- making the C-47 lookup path a named step in the SCORER HEURISTIC rather than
  implied by "(b) rows 1-5". TCR row 5 and ANNOTATION SCOPE REGISTRY unchanged.

- **V-04 (combined: V-01 + V-02)**: Self-citing TCR row 5 `(C-47)` + self-complete
  ANNOTATION SCOPE REGISTRY (row 29, count=29).

- **V-05 (combined: V-01 + V-02 + V-03)**: All three -- self-citing TCR row, self-complete
  registry, C-47-named SCORER HEURISTIC path.

All five inherit the full R15 V-05 architecture (C-01 through C-47 PASS).

---

## V-01 -- Single axis: TCR row 5 self-citation (C-47 row carries criterion ID)

**Axis**: TCR row 5 Component description carries `(C-47)` criterion citation, making TCR
row 5 independently traceable to its governing criterion without consulting the rubric. The
self-citation follows the established discipline of C-39 (STRUCTURAL MANDATE block headers
carry `(C-XX)`) and C-45 (SCORER HEURISTIC label carries `(C-43)`). The ANNOTATION SCOPE
REGISTRY table is unchanged (28 rows). The SCORER HEURISTIC is unchanged.

**Hypothesis**: R15 V-05 places the ANNOTATION SCOPE REGISTRY as TCR row 5 (C-47 PASS) but
the Component description does not carry the criterion citation `(C-47)`. A scorer tracing
C-47 must know to look at TCR row 5 by prior rubric knowledge, not by row-label scan. V-01
adds `(C-47)` to the Component cell of row 5 so a scorer can trace bidirectionally: from
rubric C-47 to TCR row 5 by `(C-47)` label scan, and from TCR row 5 to rubric C-47 by inline
citation. Risk: the Component column of the TCR is not declared as a typed-column with a
criterion-citation vocabulary; the `(C-47)` annotation may not satisfy any formal schema
constraint. Mitigation: the self-citation value is a structural quality signal regardless of
formal vocabulary declaration, matching how C-39 and C-45 were first observed.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed type. Enumerated below. Any value outside this vocabulary is a
schema error independently detectable without consulting registry rows.

> STRUCTURAL MANDATE (C-36): The **Independence Statement**: label within the `DefectCodeVocab`
> type declaration is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-36 compliance by locating the `**Independence Statement**:` label within
> the DefectCodeVocab declaration block without parsing surrounding definition bullets.

**Independence Statement**: Any value outside `DefectCodeVocab` is a schema error independently
detectable without consulting registry rows.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure -- phase references undeclared label | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema -- relay omits required field or exhibits prohibited pattern | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock -- promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering -- sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop -- Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |
| DEFECT: EMPTY-CELL | Verdict ledger completeness -- Defect code cell empty in compliance ledger | Trace invalid: ledger self-certification requires no empty cells |
| DEFECT: COUNT-MISMATCH | C-28 annotation count gate -- typed-column count in output does not match declared scope | Trace invalid: annotation coverage cannot be confirmed |

---

### Canonical STRUCTURAL MANDATE Template

All `STRUCTURAL MANDATE` blocks in this prompt conform to the following canonical form:

> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt. Reproduce
> it exactly as shown. A scorer confirms C-XX compliance by [specific method] alone without
> [parsing alternative].

Additional mandates are mechanically derivable from this canonical form. Any block that
deviates from the template is a schema error independently detectable without cross-checking
other blocks.

**Template Component Registry:**

| # | Component | Required (RequiredVocabulary) |
|---|-----------|-------------------------------|
| 1 | Block header `> STRUCTURAL MANDATE (C-XX):` with criterion citation `(C-XX)` in parentheses | YES |
| 2 | Named-element declaration: `[element] is a named structural mandate of this prompt.` | YES |
| 3 | Reproduce instruction: `Reproduce it exactly as shown.` | YES |
| 4 | Scorer confirmation closing: `A scorer confirms C-XX compliance by [method] alone without [alternative].` | YES |
| 5 | ANNOTATION SCOPE REGISTRY (C-47): formal table in Verdict C-28 COUNT GATE with columns `# / Column name (TypeName) / Host registry / table`, covering all typed columns in the prompt including Template Component Registry row | YES |
| **Anti-pattern**: omit scorer confirmation closing, omit criterion citation from header, or omit ANNOTATION SCOPE REGISTRY table from Verdict | -- | VIOLATION |

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation.

A Coverage Matrix entry is valid if and only if it is referenced in at least one downstream
phase. Both directions constitute the Coverage Matrix closed-world bijection (C-10).

The Phase 2.5 Role Bijection Checkpoint runs between Phase 2 Execute and Phase 3 Findings.
Its three co-located sub-elements appear in canonical order: status column semantics block
first, five-case algorithm table second, Role Bijection Table third. Re-ordering is a
structural violation coequal with schema label violations.

> STRUCTURAL MANDATE (C-20): The Coverage Matrix CLOSED WORLD declaration is a named structural
> mandate of this prompt. Reproduce it exactly as shown. A scorer confirms C-20 compliance by
> locating the CLOSED WORLD block before the Coverage Matrix table without parsing matrix row
> values.

**CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any phase referencing a
label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup per-role, Step 3b Source, Phase 2 Execute relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | All roles via Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1: all roles aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (all sub-step transitions) | N/A | VC-5 |

**Schema definitions** (biconditional -- violations are structural invalidity):

**Schema 1**: Trace valid w.r.t. Schema 1 iff every severity label uses only {P1, P2, P3}.
P1 = blocks useful artifact. P2 = quality improvement. P3 = advisory.

**Schema 2**: SA-TO-SG label lock: a promoted SA gap uses SG in all phases after promotion.
Retaining SA after promotion is a structural violation. `DEFECT: LABEL-LOCK-VIOLATION`

**Schema 3**: Trace valid w.r.t. Schema 3 iff every Phase 4 Amend entry names a channel from
{spec, invocation, artifact, quality}.

**Schema 4**: G-1 = >=2 distinct Source types in Step 3b. G-2 = no two same-Source findings
share identical Action text. G-3 = all Step 3b entries use only P1/P2/P3.

**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >= 2 entries.
Step 3d valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

> STRUCTURAL MANDATE (C-23): The LABEL LOCK mandate is a named structural mandate of this
> prompt. Reproduce it exactly as shown. A scorer confirms C-23 compliance by locating the
> LABEL LOCK block within Schema 2 and confirming the defect code `DEFECT: LABEL-LOCK-VIOLATION`
> is present without parsing downstream phase content.

**LABEL LOCK**: A promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. Retained
SA label after promotion is a structural violation. `DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG downstream |
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

> STRUCTURAL MANDATE (C-29): The GATE HARD-STOP mandate is a named structural mandate of this
> prompt. Reproduce it exactly as shown. A scorer confirms C-29 compliance by locating the GATE
> HARD-STOP block within Schema 4 and confirming the defect code `DEFECT: PREMATURE-PHASE-ADVANCE`
> is present without parsing Step 3c gate results.

**GATE HARD-STOP**: Phase 4 is valid only when all gates PASS. Phase 4 entered while any
gate = FAIL is a hard-stop violation. `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

> STRUCTURAL MANDATE (C-31): The SUB-STEP SEQUENCE mandate is a named structural mandate of
> this prompt. Reproduce it exactly as shown. A scorer confirms C-31 compliance by locating the
> SUB-STEP SEQUENCE block within Schema 5 and confirming the defect code
> `DEFECT: OUT-OF-ORDER-EXECUTION` is present without parsing sub-step transition records.

**SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite is satisfied is a sequencing
violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

| Step (StepIdentifier) | Prerequisite (StepIdentifier) | Produces | Unblocks (StepIdentifier) |
|-----------------------|------------------------------|---------|--------------------------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

**Invariant**: Schema X is in the Coverage Matrix iff it is referenced by at least one phase.
Direction A enumerates the forward mapping.

| Schema | Matrix row | Referenced at (all phase/step names) | Orphan? |
|--------|-----------|--------------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend); Step 3b (enforce); Step 3c G-3 (verify); Phase 4 Amend (enforce) | NO |
| Schema 2 | Row 2 | Stage 1; SA-TO-SG PROMOTION; Phase 1 Setup per-role; Step 3b Source; Phase 2 Execute relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 transitions | NO |

Direction A result: all 5 rows confirmed. Direction A invariant: HOLDS.

---

### Role-Schema Binding Summary

`RoleName` = {role name strings from skill spec}.

Declare every role that will appear in Phase 2 Execute before Stage 2 begins.

| Role (RoleName) | Schema 1 binding (SeverityVocab) | Schema 2 binding (GapTypeVocab) | Notes |
|-----------------|----------------------------------|--------------------------------|-------|
| [role from spec] | [severity labels applicable; or "N/A -- no EG findings"] | [Source labels this role may produce; label lock if promoted] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Catalog every gap using Schema 2 Source labels and Schema 1
Severity labels. Do not consult the test invocation.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`]. Do not re-derive. Do not resolve silently.

---

#### SA-TO-SG PROMOTION

Every SA gap in the Stage 1 relay is evaluated at the Setup boundary.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

Updated relay:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock active. `DEFECT: LABEL-LOCK-VIOLATION` if promoted gap uses SA downstream.

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding (SeverityVocab): [severity labels applicable, or "N/A"]
  Schema 2 binding (GapTypeVocab): [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear. Three required seeded fields in every role relay: `Schema 2 compliance:`,
`Binding Summary row:` (Direction B seed), `Schema-governed action:` (Direction A seed).
A relay missing either seeded field must declare the absence explicitly.

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

> STRUCTURAL MANDATE (C-21): The relay anti-pattern prohibition row is a named structural
> mandate of this prompt. Reproduce it exactly as shown. A scorer confirms C-21 compliance by
> locating the row carrying `VIOLATION` in the `Required (RequiredVocabulary)` column without
> parsing the Field or Format cells.

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] -- all valid: YES / NO | YES |
| Binding Summary row | [row index] (Direction B seed) | YES |
| Schema-governed action | [action using Schema 1 or 2 labels per Binding Summary declaration] | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| **Anti-pattern**: DO NOT omit Schema 2 compliance field or relay seeded fields | Relay without these fields is structurally invalid | VIOLATION |

For each role, write the relay before the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed)
- **Schema-governed action**: [action] **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 2.5 -- Role Bijection Checkpoint

**Named inter-phase checkpoint**. Runs immediately after Phase 2 Execute. Phase 3 cannot
begin until this checkpoint produces a gate result.

**Sub-element ordering invariant**: The three sub-elements appear in canonical order:
sub-element 1 (status column semantics) first, sub-element 2 (five-case algorithm table)
second, sub-element 3 (Role Bijection Table) third. Re-ordering is a structural violation.

---

##### Phase 2.5 sub-element 1 of 3 -- Status Column Semantics

Column A -- `A: Acts in Execute` -- domain: {`YES`, `SILENT`, `relay field absent`}.

- `YES`: `Schema-governed action:` field read from Execute relay. Role produced a
  schema-governed action matching its Binding Summary declaration. Direction A holds.
- `SILENT`: No Execute relay found, or relay carries no action field. Binding Summary
  entry exists. Role declared to act but produced no schema-governed action. Direction A
  violated. Gate consequence: BLOCKED.
- `relay field absent`: Execute relay exists; `Schema-governed action:` field absent from
  relay body. Relay structurally incomplete; Direction A seed not planted. Gate: BLOCKED.

Column B -- `B: Declared in Summary` -- domain: {`YES`, `UNDECLARED`, `relay field absent`}.

- `YES`: `Binding Summary row:` field read from Execute relay. Role declared its entry via
  relay seed. Direction B holds.
- `UNDECLARED`: Execute relay exists; no Binding Summary entry for this role. Role produced
  schema-governed action without declaring intent. Direction B violated. Gate: BLOCKED.
- `relay field absent`: Execute relay exists; `Binding Summary row:` field absent from relay
  body. Relay structurally incomplete; Direction B seed not planted. Gate: BLOCKED.

---

##### Phase 2.5 sub-element 2 of 3 -- Evidence Source Column Population (exhaustive five-case table)

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` field in relay; BSR = `Binding Summary row:` field
in relay; BS entry = Binding Summary row exists for this role.

Locate the matching case; copy A Evidence source and B Evidence source values exactly.
Exactly five cases; no additional cases exist.

---

##### Phase 2.5 sub-element 3 of 3 -- Role Bijection Table

**Role bijection invariant**: Role R is in the Binding Summary iff it produces at least one
schema-governed action in Phase 2 Execute.

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- SILENT: declared in Summary but produced no schema-governed action in Execute."
- "[role] -- UNDECLARED: acted in Execute without Binding Summary entry."
- "[relay] -- relay field absent: [field name] missing from relay."

**Biconditional hold summary**:

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

**Three defect classes -- coequal BLOCKED triggers**: SILENT, UNDECLARED, and relay field
absent trigger Phase 3 BLOCKED coequally. None is subordinate to or deferred relative to
the others.

If any A != YES or B != YES:
**Phase 3 BLOCKED: [classify as SILENT / UNDECLARED / relay field absent. Name the role relay
and the specific defect. Enumerate all three defect class names explicitly: SILENT, UNDECLARED,
relay field absent. Resolve before proceeding.]**

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent).

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

Phase 3 runs in the sub-step sequence declared in Schema 5.

##### Step 3a -- Severity Legend

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label (SeverityVocab) | Definition for this trace | Actionability threshold |
|-----------------------|--------------------------|------------------------|
| P1 | [what blocks useful baseline] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

Minimum 2 entries. At least 2 distinct Source types.

Schema 5 transition: >=2 entries -> Step 3c valid.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated.

**G-1**: Source types in Step 3b: [list] -- G-1: PASS / FAIL
**G-2**: Same-Source pairs with identical Action: [list or "none"] -- G-2: PASS / FAIL
**G-3**: Severity labels in Step 3b: [list] -- G-3: PASS / FAIL

If any FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Phase 4 BLOCKED. Resolve, re-run, confirm
PASS before proceeding.

Schema 5 transition: all-PASS -> Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS.

Activate Schema 3 channels: spec / invocation / artifact / quality.
Every Phase 4 Amend entry requires `[remediation channel: ...]`.

Schema 5 transition: channel active -> Phase 4 valid.

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy (Schema 3 ChannelVocab): spec / invocation / artifact / quality.

Change entry:
- [finding: `{{F-NN}}`]
- [source: `{{source}}` (GapTypeVocab)] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality (ChannelVocab)]
- [section changed: ]
- [change: ]

Dismissal entry:
- [finding: `{{F-NN}}`], [reason: ], [remediation channel: ], [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

> STRUCTURAL MANDATE (C-35): The PRE-READ GATE is a named structural mandate of this prompt.
> Reproduce it exactly as shown. A scorer confirms C-35 compliance by locating the PRE-READ GATE
> block immediately before the compliance ledger without parsing ledger row values.

Before reading the compliance ledger, confirm in sequence:
1. Defect Classification Registry is present before Stage 1 in this output.
2. All FAIL rows carry a `DefectCodeVocab` value -- not free-form prose.
3. No cell in the `Defect code (DefectCodeVocab)` column is empty.

If check 3 fires: emit `DEFECT: EMPTY-CELL` before proceeding.

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** (Component 5 of Template Component Registry) -- typed columns
in this prompt. Each row is independently row-verifiable. A scorer confirms C-46 compliance
by locating this table (declared as TCR Component 5) and verifying the Template Component
Registry row is present without parsing inline scope lists.

| # | Column name (TypeName) | Host registry / table |
|---|------------------------|----------------------|
| 1 | `Defect code (DefectCodeVocab)` | Defect Classification Registry |
| 2 | `Defect code (DefectCodeVocab)` | Verdict compliance ledger |
| 3 | `Required (RequiredVocabulary)` | Phase 2 Execute relay schema |
| 4 | `Required (RequiredVocabulary)` | Template Component Registry |
| 5 | `Content (ContentVocab)` | Coverage Matrix |
| 6 | `Declared-at (PhaseRef)` | Coverage Matrix |
| 7 | `Referenced-by (PhaseRef)` | Coverage Matrix |
| 8 | `Role-binding (RoleRef)` | Coverage Matrix |
| 9 | `Verdict-check (VCIdentifier)` | Coverage Matrix |
| 10 | `Label (SeverityVocab)` | Schema 1 table |
| 11 | `Blocks? (BlocksVocab)` | Schema 1 table |
| 12 | `Type (GapTypeVocab)` | Schema 2 table |
| 13 | `Promotion rule (PromotionVocab)` | Schema 2 table |
| 14 | `Channel (ChannelVocab)` | Schema 3 table |
| 15 | `Activated-at (ActivationPhaseRef)` | Schema 3 table |
| 16 | `Gate (GateIdentifier)` | Schema 4 table |
| 17 | `Hard-stop condition (BlockConditionVocab)` | Schema 4 table |
| 18 | `Step (StepIdentifier)` | Schema 5 table (Step column) |
| 19 | `Prerequisite (StepIdentifier)` | Schema 5 table |
| 20 | `Unblocks (StepIdentifier)` | Schema 5 table |
| 21 | `Role (RoleName)` | Role-Schema Binding Summary |
| 22 | `Schema 1 binding (SeverityVocab)` | Role-Schema Binding Summary |
| 23 | `Schema 2 binding (GapTypeVocab)` | Role-Schema Binding Summary |
| 24 | `Source (GapTypeVocab)` | Stage 1 audit table |
| 25 | `Severity (SeverityVocab)` | Stage 1 audit table |
| 26 | `Affects phase (PhaseRef)` | Stage 1 audit table |
| 27 | `Source (GapTypeVocab)` | Step 3b findings table |
| 28 | `Severity (SeverityVocab)` | Step 3b findings table |

Expected annotation count: **28** (count of rows above).

IF count of `(TypeName)`-annotated columns in output = 28: **confirmed**
IF count ≠ 28: **mismatch** -- emit `DEFECT: COUNT-MISMATCH`

---

#### Compliance Ledger

`Observed behavior: as expected` is structurally invalid in any cell.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|--------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what legend stated] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [list severity values] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate checked | [G-3 result; labels checked] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values in Amend] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use only P1/P2/P3 | [list labels this role used] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL | -- |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [list Source labels] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels valid; lock honored | [Source labels in relay] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels used; any missing] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [G-1/G-2/G-3 results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL | -- |
| VC-4 | Schema 4 | G-1 cross-role | Source diversity across all roles | [Source types and roles per type] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [transition evidence] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c | [transition evidence] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL | -- |

Rules: PASS rows carry `--` in Defect code. FAIL rows carry a `DefectCodeVocab` code. No
empty cells.

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assembled from Schema footprint records. Direction B invariant: every schema referenced in
any phase appears in the Coverage Matrix.

| Phase / Step | Schema referenced | Matrix row | Registered? |
|--------------|------------------|------------|-------------|
| Stage 1 | Schema 2, Schema 1 | Rows 2, 1 | YES |
| SA-TO-SG PROMOTION | Schema 2 | Row 2 | YES |
| Phase 1 Setup | Schema 1, Schema 2 | Rows 1, 2 | YES |
| Phase 2 Execute | Schema 2, Schema 1 | Rows 2, 1 | YES |
| Step 3a | Schema 1, Schema 5 | Rows 1, 5 | YES |
| Step 3b | Schema 2, Schema 1, Schema 5 | Rows 2, 1, 5 | YES |
| Step 3c | Schema 4, Schema 5 | Rows 4, 5 | YES |
| Step 3d | Schema 3, Schema 5 | Rows 3, 5 | YES |
| Phase 4 Amend | Schema 2, Schema 3, Schema 1, Schema 4 | Rows 2, 3, 1, 4 | YES |

Undeclared references: NONE. Direction B: HOLDS.

**C-10 Coverage Matrix bijection**: Direction A (HOLDS) + Direction B (HOLDS) = C-10: PASS.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

### CONFORMANCE-COLLAPSE CLAIM

All `STRUCTURAL MANDATE` blocks in this prompt conform to the canonical template declared in
the Canonical STRUCTURAL MANDATE Template section. Any block conforming to the canonical
template satisfies both C-39 (self-citing header `(C-XX)`) and C-40 (scorer confirmation
closing) by a single template-conformance check -- without inspecting individual block bodies.
The ANNOTATION SCOPE REGISTRY table is declared as Component 5 (C-47) of the Template
Component Registry, making its presence verifiable by TCR row lookup rather than Verdict
section scan.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, (b) the
Template Component Registry lists all five required components (rows 1-5), and (c) the
ANNOTATION SCOPE REGISTRY table appears in the Verdict C-28 COUNT GATE section as declared by
TCR row 5 -- without inspecting individual `STRUCTURAL MANDATE` block bodies.

---

## V-02 -- Single axis: ANNOTATION SCOPE REGISTRY self-lists its own typed column (row 29)

**Axis**: ANNOTATION SCOPE REGISTRY self-inclusion -- the registry adds row 29 for its own
typed column `Column name (TypeName)`, making the registry self-complete. The ANNOTATION
SCOPE REGISTRY enumerates all typed columns in the prompt including its own. Expected
annotation count changes from 28 to 29. TCR row 5 component description and SCORER HEURISTIC
are unchanged from the entry state.

**Hypothesis**: R15 V-05 establishes the ANNOTATION SCOPE REGISTRY as a 28-row table but
the table's own typed column `Column name (TypeName)` is not listed in the registry. The
registry is claimed to enumerate "all typed columns in this prompt" but omits itself -- an
open-world gap about its own typed column. V-02 closes this gap by adding row 29:
`Column name (TypeName) | ANNOTATION SCOPE REGISTRY`. The registry then truly enumerates
every typed column including its own, and the count gate changes to 29. Risk: the self-
referential nature of row 29 may create a perceived infinite-recursion concern; mitigation
is that the registry is a static enumeration (all rows are present simultaneously), not
a dynamic self-modifying list -- row 29 names the `Column name` column of the registry
table itself, which is a well-defined static column.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

[Identical to V-01.]

---

### Canonical STRUCTURAL MANDATE Template

All `STRUCTURAL MANDATE` blocks in this prompt conform to the following canonical form:

> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt. Reproduce
> it exactly as shown. A scorer confirms C-XX compliance by [specific method] alone without
> [parsing alternative].

Additional mandates are mechanically derivable from this canonical form. Any block that
deviates from the template is a schema error independently detectable without cross-checking
other blocks.

**Template Component Registry:**

| # | Component | Required (RequiredVocabulary) |
|---|-----------|-------------------------------|
| 1 | Block header `> STRUCTURAL MANDATE (C-XX):` with criterion citation `(C-XX)` in parentheses | YES |
| 2 | Named-element declaration: `[element] is a named structural mandate of this prompt.` | YES |
| 3 | Reproduce instruction: `Reproduce it exactly as shown.` | YES |
| 4 | Scorer confirmation closing: `A scorer confirms C-XX compliance by [method] alone without [alternative].` | YES |
| 5 | ANNOTATION SCOPE REGISTRY table in Verdict C-28 COUNT GATE: formal table with columns `# / Column name (TypeName) / Host registry / table`, covering all typed columns in the prompt including Template Component Registry row and this registry's own `Column name (TypeName)` column at row 29 | YES |
| **Anti-pattern**: omit scorer confirmation closing, omit criterion citation from header, or omit ANNOTATION SCOPE REGISTRY table from Verdict | -- | VIOLATION |

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

---

[Coverage Matrix through Phase 4 -- identical to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

[Identical to V-01.]

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** (Component 5 of Template Component Registry) -- typed columns
in this prompt, including this registry's own typed column at row 29. Each row is independently
row-verifiable. A scorer confirms C-46 compliance by locating this table (declared as TCR
Component 5) and verifying the Template Component Registry row is present without parsing
inline scope lists.

| # | Column name (TypeName) | Host registry / table |
|---|------------------------|----------------------|
| 1 | `Defect code (DefectCodeVocab)` | Defect Classification Registry |
| 2 | `Defect code (DefectCodeVocab)` | Verdict compliance ledger |
| 3 | `Required (RequiredVocabulary)` | Phase 2 Execute relay schema |
| 4 | `Required (RequiredVocabulary)` | Template Component Registry |
| 5 | `Content (ContentVocab)` | Coverage Matrix |
| 6 | `Declared-at (PhaseRef)` | Coverage Matrix |
| 7 | `Referenced-by (PhaseRef)` | Coverage Matrix |
| 8 | `Role-binding (RoleRef)` | Coverage Matrix |
| 9 | `Verdict-check (VCIdentifier)` | Coverage Matrix |
| 10 | `Label (SeverityVocab)` | Schema 1 table |
| 11 | `Blocks? (BlocksVocab)` | Schema 1 table |
| 12 | `Type (GapTypeVocab)` | Schema 2 table |
| 13 | `Promotion rule (PromotionVocab)` | Schema 2 table |
| 14 | `Channel (ChannelVocab)` | Schema 3 table |
| 15 | `Activated-at (ActivationPhaseRef)` | Schema 3 table |
| 16 | `Gate (GateIdentifier)` | Schema 4 table |
| 17 | `Hard-stop condition (BlockConditionVocab)` | Schema 4 table |
| 18 | `Step (StepIdentifier)` | Schema 5 table (Step column) |
| 19 | `Prerequisite (StepIdentifier)` | Schema 5 table |
| 20 | `Unblocks (StepIdentifier)` | Schema 5 table |
| 21 | `Role (RoleName)` | Role-Schema Binding Summary |
| 22 | `Schema 1 binding (SeverityVocab)` | Role-Schema Binding Summary |
| 23 | `Schema 2 binding (GapTypeVocab)` | Role-Schema Binding Summary |
| 24 | `Source (GapTypeVocab)` | Stage 1 audit table |
| 25 | `Severity (SeverityVocab)` | Stage 1 audit table |
| 26 | `Affects phase (PhaseRef)` | Stage 1 audit table |
| 27 | `Source (GapTypeVocab)` | Step 3b findings table |
| 28 | `Severity (SeverityVocab)` | Step 3b findings table |
| 29 | `Column name (TypeName)` | ANNOTATION SCOPE REGISTRY |

Expected annotation count: **29** (count of rows above, including this registry's own
typed column at row 29).

IF count of `(TypeName)`-annotated columns in output = 29: **confirmed**
IF count ≠ 29: **mismatch** -- emit `DEFECT: COUNT-MISMATCH`

---

#### Compliance Ledger

[Identical to V-01.]

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

[Identical to V-01.]

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

### CONFORMANCE-COLLAPSE CLAIM

All `STRUCTURAL MANDATE` blocks in this prompt conform to the canonical template declared in
the Canonical STRUCTURAL MANDATE Template section. Any block conforming to the canonical
template satisfies both C-39 (self-citing header `(C-XX)`) and C-40 (scorer confirmation
closing) by a single template-conformance check -- without inspecting individual block bodies.
The ANNOTATION SCOPE REGISTRY table is declared as Component 5 of the Template Component
Registry, making its presence verifiable by TCR row lookup rather than Verdict section scan.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, (b) the
Template Component Registry lists all five required components (rows 1-5), and (c) the
ANNOTATION SCOPE REGISTRY table appears in the Verdict C-28 COUNT GATE section as declared by
TCR row 5 -- without inspecting individual `STRUCTURAL MANDATE` block bodies.

---

## V-03 -- Single axis: SCORER HEURISTIC cites C-47 explicitly in its confirmation path

**Axis**: SCORER HEURISTIC (C-43) names C-47 explicitly in step (b) of the confirmation
path -- "confirming C-47 compliance by locating TCR row 5 and verifying the ANNOTATION SCOPE
REGISTRY table appears in the Verdict C-28 COUNT GATE section". The SCORER HEURISTIC step (b)
now traces two verification targets: canonical template form AND the C-47 TCR row lookup for
the ANNOTATION SCOPE REGISTRY. TCR row 5 Component description and ANNOTATION SCOPE REGISTRY
table are unchanged from the entry state (28 rows).

**Hypothesis**: R15 V-05 SCORER HEURISTIC says "(b) the Template Component Registry lists all
five required components (rows 1-5)" -- this confirms C-47 implicitly (row 5 = ANNOTATION
SCOPE REGISTRY) but does not name C-47 by criterion ID. V-03 makes C-47 a named step: "(b)
TCR rows 1-4 conform to the canonical template; TCR row 5 (C-47) names the ANNOTATION SCOPE
REGISTRY with its typed-column notation; (c) the ANNOTATION SCOPE REGISTRY table appears in
the Verdict C-28 COUNT GATE section as declared by TCR row 5". This makes C-47 traceable
through the SCORER HEURISTIC path by criterion ID, paralleling how C-42's CONFORMANCE-COLLAPSE
mechanism made C-39/C-40 traceable by template-conformance check. Risk: splitting step (b)
into two sub-steps adds prompt length; mitigation is that each sub-step is precisely scoped.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

[Identical to V-01.]

---

### Canonical STRUCTURAL MANDATE Template

[Identical to V-01 -- TCR has 5 rows with row 5 as `ANNOTATION SCOPE REGISTRY table in
Verdict C-28 COUNT GATE: formal table with columns # / Column name (TypeName) / Host registry
/ table, covering all typed columns in the prompt including Template Component Registry row
| YES`.]

---

[Coverage Matrix through Phase 4 -- identical to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

[Identical to V-01.]

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** (Component 5 of Template Component Registry) -- typed columns
in this prompt. Each row is independently row-verifiable. A scorer confirms C-46 compliance
by locating this table (declared as TCR Component 5) and verifying the Template Component
Registry row is present without parsing inline scope lists.

[28-row table identical to V-01.]

Expected annotation count: **28** (count of rows above).

IF count of `(TypeName)`-annotated columns in output = 28: **confirmed**
IF count ≠ 28: **mismatch** -- emit `DEFECT: COUNT-MISMATCH`

---

#### Compliance Ledger

[Identical to V-01.]

---

#### Closed-World Verification -- Direction B

[Identical to V-01.]

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

### CONFORMANCE-COLLAPSE CLAIM

All `STRUCTURAL MANDATE` blocks in this prompt conform to the canonical template declared in
the Canonical STRUCTURAL MANDATE Template section. Any block conforming to the canonical
template satisfies both C-39 (self-citing header `(C-XX)`) and C-40 (scorer confirmation
closing) by a single template-conformance check -- without inspecting individual block bodies.
The ANNOTATION SCOPE REGISTRY table is declared as Component 5 of the Template Component
Registry, making its presence verifiable by TCR row lookup rather than Verdict section scan.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared;
(b) TCR rows 1-4 conform to the canonical template and TCR row 5 (C-47) names the ANNOTATION
SCOPE REGISTRY with its typed-column notation `# / Column name (TypeName) / Host registry /
table` -- confirming C-47 compliance by TCR row 5 label scan alone; and (c) the ANNOTATION
SCOPE REGISTRY table appears in the Verdict C-28 COUNT GATE section as declared by TCR row 5
-- without inspecting individual `STRUCTURAL MANDATE` block bodies.

---

## V-04 -- Combined: TCR row 5 self-citation (C-47) + ANNOTATION SCOPE REGISTRY self-lists row 29

**Axes**: V-01 (TCR row 5 Component carries `(C-47)`) + V-02 (ANNOTATION SCOPE REGISTRY adds
row 29 for its own typed column; count = 29).

**Hypothesis**: V-01 tests whether TCR row 5 self-citation is recognized as a structural
quality signal parallel to C-39/C-45. V-02 tests whether self-inclusion of the registry's own
typed column is recognized as a closed-world completeness signal. V-04 combines both to
determine whether the conjunction produces a stronger signal than either alone. A model
running V-04 will encounter: TCR row 5 with `(C-47)` citation AND a 29-row ANNOTATION SCOPE
REGISTRY that is self-complete. Neither change breaks any existing criterion. Risk: the count
change from 28 to 29 is the only observable difference in Verdict execution behavior; scoring
systems may not distinguish V-01 from V-04 on criterion-pass rates, but the structural signals
are qualitatively distinct.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

[Identical to V-01.]

---

### Canonical STRUCTURAL MANDATE Template

All `STRUCTURAL MANDATE` blocks in this prompt conform to the following canonical form:

> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt. Reproduce
> it exactly as shown. A scorer confirms C-XX compliance by [specific method] alone without
> [parsing alternative].

Additional mandates are mechanically derivable from this canonical form. Any block that
deviates from the template is a schema error independently detectable without cross-checking
other blocks.

**Template Component Registry:**

| # | Component | Required (RequiredVocabulary) |
|---|-----------|-------------------------------|
| 1 | Block header `> STRUCTURAL MANDATE (C-XX):` with criterion citation `(C-XX)` in parentheses | YES |
| 2 | Named-element declaration: `[element] is a named structural mandate of this prompt.` | YES |
| 3 | Reproduce instruction: `Reproduce it exactly as shown.` | YES |
| 4 | Scorer confirmation closing: `A scorer confirms C-XX compliance by [method] alone without [alternative].` | YES |
| 5 | ANNOTATION SCOPE REGISTRY (C-47): formal table in Verdict C-28 COUNT GATE with columns `# / Column name (TypeName) / Host registry / table`, covering all typed columns in the prompt including Template Component Registry row and this registry's own `Column name (TypeName)` column at row 29 | YES |
| **Anti-pattern**: omit scorer confirmation closing, omit criterion citation from header, or omit ANNOTATION SCOPE REGISTRY table from Verdict | -- | VIOLATION |

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

---

[Coverage Matrix through Phase 4 -- identical to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

[Identical to V-01.]

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** (Component 5 of Template Component Registry, C-47) -- typed
columns in this prompt, including this registry's own typed column at row 29. Each row is
independently row-verifiable. A scorer confirms C-46 compliance by locating this table
(declared as TCR Component 5, C-47) and verifying the Template Component Registry row is
present without parsing inline scope lists.

| # | Column name (TypeName) | Host registry / table |
|---|------------------------|----------------------|
| 1 | `Defect code (DefectCodeVocab)` | Defect Classification Registry |
| 2 | `Defect code (DefectCodeVocab)` | Verdict compliance ledger |
| 3 | `Required (RequiredVocabulary)` | Phase 2 Execute relay schema |
| 4 | `Required (RequiredVocabulary)` | Template Component Registry |
| 5 | `Content (ContentVocab)` | Coverage Matrix |
| 6 | `Declared-at (PhaseRef)` | Coverage Matrix |
| 7 | `Referenced-by (PhaseRef)` | Coverage Matrix |
| 8 | `Role-binding (RoleRef)` | Coverage Matrix |
| 9 | `Verdict-check (VCIdentifier)` | Coverage Matrix |
| 10 | `Label (SeverityVocab)` | Schema 1 table |
| 11 | `Blocks? (BlocksVocab)` | Schema 1 table |
| 12 | `Type (GapTypeVocab)` | Schema 2 table |
| 13 | `Promotion rule (PromotionVocab)` | Schema 2 table |
| 14 | `Channel (ChannelVocab)` | Schema 3 table |
| 15 | `Activated-at (ActivationPhaseRef)` | Schema 3 table |
| 16 | `Gate (GateIdentifier)` | Schema 4 table |
| 17 | `Hard-stop condition (BlockConditionVocab)` | Schema 4 table |
| 18 | `Step (StepIdentifier)` | Schema 5 table (Step column) |
| 19 | `Prerequisite (StepIdentifier)` | Schema 5 table |
| 20 | `Unblocks (StepIdentifier)` | Schema 5 table |
| 21 | `Role (RoleName)` | Role-Schema Binding Summary |
| 22 | `Schema 1 binding (SeverityVocab)` | Role-Schema Binding Summary |
| 23 | `Schema 2 binding (GapTypeVocab)` | Role-Schema Binding Summary |
| 24 | `Source (GapTypeVocab)` | Stage 1 audit table |
| 25 | `Severity (SeverityVocab)` | Stage 1 audit table |
| 26 | `Affects phase (PhaseRef)` | Stage 1 audit table |
| 27 | `Source (GapTypeVocab)` | Step 3b findings table |
| 28 | `Severity (SeverityVocab)` | Step 3b findings table |
| 29 | `Column name (TypeName)` | ANNOTATION SCOPE REGISTRY |

Expected annotation count: **29** (count of rows above, including this registry's own
typed column at row 29).

IF count of `(TypeName)`-annotated columns in output = 29: **confirmed**
IF count ≠ 29: **mismatch** -- emit `DEFECT: COUNT-MISMATCH`

---

#### Compliance Ledger

[Identical to V-01.]

---

#### Closed-World Verification -- Direction B

[Identical to V-01.]

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

### CONFORMANCE-COLLAPSE CLAIM

All `STRUCTURAL MANDATE` blocks in this prompt conform to the canonical template declared in
the Canonical STRUCTURAL MANDATE Template section. Any block conforming to the canonical
template satisfies both C-39 (self-citing header `(C-XX)`) and C-40 (scorer confirmation
closing) by a single template-conformance check -- without inspecting individual block bodies.
The ANNOTATION SCOPE REGISTRY table is declared as Component 5 (C-47) of the Template
Component Registry, making its presence verifiable by TCR row lookup rather than Verdict
section scan.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, (b) the
Template Component Registry lists all five required components (rows 1-5), and (c) the
ANNOTATION SCOPE REGISTRY table appears in the Verdict C-28 COUNT GATE section as declared by
TCR row 5 (C-47) -- without inspecting individual `STRUCTURAL MANDATE` block bodies.

---

## V-05 -- Combined: TCR row 5 self-citation + self-complete registry (row 29) + SCORER HEURISTIC cites C-47

**Axes**: V-01 (TCR row 5 carries `(C-47)`) + V-02 (ANNOTATION SCOPE REGISTRY self-lists
row 29; count = 29) + V-03 (SCORER HEURISTIC explicitly names C-47 in step (b)).

**Hypothesis**: V-04 provides the TCR self-citation and self-complete registry. V-05 adds the
explicit C-47 naming in the SCORER HEURISTIC, making the confirmation path fully self-
documenting: a scorer reading the SCORER HEURISTIC can confirm C-47 compliance (TCR row 5
lookup) without consulting the rubric for what row 5 governs. The combination closes three
independent paths for C-47 structural legibility: (1) the TCR row itself carries `(C-47)` for
bidirectional traceability; (2) the registry is self-complete including its own typed column;
(3) the SCORER HEURISTIC names C-47 explicitly so the confirmation path is self-documented.
If the scoring system for Round 17 formalizes any of these three as a new criterion, V-05
positions the combined form as the excellence signal.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Defect Classification Registry

`DefectCodeVocab` is a closed type. Enumerated below. Any value outside this vocabulary is a
schema error independently detectable without consulting registry rows.

> STRUCTURAL MANDATE (C-36): The **Independence Statement**: label within the `DefectCodeVocab`
> type declaration is a named structural mandate of this prompt. Reproduce it exactly as shown.
> A scorer confirms C-36 compliance by locating the `**Independence Statement**:` label within
> the DefectCodeVocab declaration block without parsing surrounding definition bullets.

**Independence Statement**: Any value outside `DefectCodeVocab` is a schema error independently
detectable without consulting registry rows.

| Defect code (DefectCodeVocab) | Mandate violated | Structural consequence |
|-------------------------------|-----------------|----------------------|
| DEFECT: OPEN-WORLD-ASSERTION | Coverage Matrix closure -- phase references undeclared label | Trace invalid: undeclared label cannot be Verdict-audited |
| DEFECT: RELAY-SCHEMA-VIOLATION | Role relay schema -- relay omits required field or exhibits prohibited pattern | Trace invalid: relay lacks complete source-layer evidence |
| DEFECT: LABEL-LOCK-VIOLATION | Schema 2 label lock -- promoted gap retains SA label after PROMOTION | Trace invalid: source attribution incorrect downstream |
| DEFECT: OUT-OF-ORDER-EXECUTION | Schema 5 sub-step ordering -- sub-step ran before prerequisite satisfied | Trace invalid: prerequisite output unavailable |
| DEFECT: PREMATURE-PHASE-ADVANCE | Schema 4 hard-stop -- Phase 4 entered while any gate = FAIL | Trace invalid: structural gap unresolved at phase entry |
| DEFECT: EMPTY-CELL | Verdict ledger completeness -- Defect code cell empty in compliance ledger | Trace invalid: ledger self-certification requires no empty cells |
| DEFECT: COUNT-MISMATCH | C-28 annotation count gate -- typed-column count in output does not match declared scope | Trace invalid: annotation coverage cannot be confirmed |

---

### Canonical STRUCTURAL MANDATE Template

All `STRUCTURAL MANDATE` blocks in this prompt conform to the following canonical form:

> STRUCTURAL MANDATE (C-XX): [element] is a named structural mandate of this prompt. Reproduce
> it exactly as shown. A scorer confirms C-XX compliance by [specific method] alone without
> [parsing alternative].

Additional mandates are mechanically derivable from this canonical form. Any block that
deviates from the template is a schema error independently detectable without cross-checking
other blocks.

**Template Component Registry:**

| # | Component | Required (RequiredVocabulary) |
|---|-----------|-------------------------------|
| 1 | Block header `> STRUCTURAL MANDATE (C-XX):` with criterion citation `(C-XX)` in parentheses | YES |
| 2 | Named-element declaration: `[element] is a named structural mandate of this prompt.` | YES |
| 3 | Reproduce instruction: `Reproduce it exactly as shown.` | YES |
| 4 | Scorer confirmation closing: `A scorer confirms C-XX compliance by [method] alone without [alternative].` | YES |
| 5 | ANNOTATION SCOPE REGISTRY (C-47): formal table in Verdict C-28 COUNT GATE with columns `# / Column name (TypeName) / Host registry / table`, covering all typed columns in the prompt including Template Component Registry row and this registry's own `Column name (TypeName)` column at row 29 | YES |
| **Anti-pattern**: omit scorer confirmation closing, omit criterion citation from header, or omit ANNOTATION SCOPE REGISTRY table from Verdict | -- | VIOLATION |

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation.

A Coverage Matrix entry is valid if and only if it is referenced in at least one downstream
phase. Both directions constitute the Coverage Matrix closed-world bijection (C-10).

The Phase 2.5 Role Bijection Checkpoint runs between Phase 2 Execute and Phase 3 Findings.
Its three co-located sub-elements appear in canonical order: status column semantics block
first, five-case algorithm table second, Role Bijection Table third. Re-ordering is a
structural violation coequal with schema label violations.

> STRUCTURAL MANDATE (C-20): The Coverage Matrix CLOSED WORLD declaration is a named structural
> mandate of this prompt. Reproduce it exactly as shown. A scorer confirms C-20 compliance by
> locating the CLOSED WORLD block before the Coverage Matrix table without parsing matrix row
> values.

**CLOSED WORLD**: Coverage Matrix is CLOSED for this invocation. Any phase referencing a
label, channel, or gate not declared in this table is in violation.
`DEFECT: OPEN-WORLD-ASSERTION`

| Schema | Content (ContentVocab) | Declared-at (PhaseRef) | Referenced-by (PhaseRef) | Role-binding (RoleRef) | Verdict-check (VCIdentifier) |
|--------|------------------------|------------------------|--------------------------|------------------------|------------------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup per-role, Step 3b Source, Phase 2 Execute relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | All roles via Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1: all roles aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (all sub-step transitions) | N/A | VC-5 |

**Schema definitions** (biconditional -- violations are structural invalidity):

**Schema 1**: Trace valid w.r.t. Schema 1 iff every severity label uses only {P1, P2, P3}.
P1 = blocks useful artifact. P2 = quality improvement. P3 = advisory.

**Schema 2**: SA-TO-SG label lock: a promoted SA gap uses SG in all phases after promotion.
Retaining SA after promotion is a structural violation. `DEFECT: LABEL-LOCK-VIOLATION`

**Schema 3**: Trace valid w.r.t. Schema 3 iff every Phase 4 Amend entry names a channel from
{spec, invocation, artifact, quality}.

**Schema 4**: G-1 = >=2 distinct Source types in Step 3b. G-2 = no two same-Source findings
share identical Action text. G-3 = all Step 3b entries use only P1/P2/P3.

**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >= 2 entries.
Step 3d valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

#### Severity Vocabulary (Schema 1)

`SeverityVocab` = {P1, P2, P3}. `BlocksVocab` = {YES, NO}.

| Label (SeverityVocab) | Definition | Blocks? (BlocksVocab) |
|-----------------------|-----------|----------------------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

`GapTypeVocab` = {SA, SG, EG, QO}. `PromotionVocab` = {PROMOTES TO SG-NN, REMAINS SA}.

> STRUCTURAL MANDATE (C-23): The LABEL LOCK mandate is a named structural mandate of this
> prompt. Reproduce it exactly as shown. A scorer confirms C-23 compliance by locating the
> LABEL LOCK block within Schema 2 and confirming the defect code `DEFECT: LABEL-LOCK-VIOLATION`
> is present without parsing downstream phase content.

**LABEL LOCK**: A promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. Retained
SA label after promotion is a structural violation. `DEFECT: LABEL-LOCK-VIOLATION`

| Type (GapTypeVocab) | Meaning | Promotion rule (PromotionVocab) |
|---------------------|---------|--------------------------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG downstream |
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

> STRUCTURAL MANDATE (C-29): The GATE HARD-STOP mandate is a named structural mandate of this
> prompt. Reproduce it exactly as shown. A scorer confirms C-29 compliance by locating the GATE
> HARD-STOP block within Schema 4 and confirming the defect code `DEFECT: PREMATURE-PHASE-ADVANCE`
> is present without parsing Step 3c gate results.

**GATE HARD-STOP**: Phase 4 is valid only when all gates PASS. Phase 4 entered while any
gate = FAIL is a hard-stop violation. `DEFECT: PREMATURE-PHASE-ADVANCE`

| Gate (GateIdentifier) | Property | Hard-stop condition (BlockConditionVocab) |
|-----------------------|---------|------------------------------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

`StepIdentifier` = {Step 3a, Step 3b, Step 3c, Step 3d, Phase 4}.

> STRUCTURAL MANDATE (C-31): The SUB-STEP SEQUENCE mandate is a named structural mandate of
> this prompt. Reproduce it exactly as shown. A scorer confirms C-31 compliance by locating the
> SUB-STEP SEQUENCE block within Schema 5 and confirming the defect code
> `DEFECT: OUT-OF-ORDER-EXECUTION` is present without parsing sub-step transition records.

**SUB-STEP SEQUENCE**: A sub-step begun before its prerequisite is satisfied is a sequencing
violation. `DEFECT: OUT-OF-ORDER-EXECUTION`

| Step (StepIdentifier) | Prerequisite (StepIdentifier) | Produces | Unblocks (StepIdentifier) |
|-----------------------|------------------------------|---------|--------------------------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

**Invariant**: Schema X is in the Coverage Matrix iff it is referenced by at least one phase.
Direction A enumerates the forward mapping.

| Schema | Matrix row | Referenced at (all phase/step names) | Orphan? |
|--------|-----------|--------------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend); Step 3b (enforce); Step 3c G-3 (verify); Phase 4 Amend (enforce) | NO |
| Schema 2 | Row 2 | Stage 1; SA-TO-SG PROMOTION; Phase 1 Setup per-role; Step 3b Source; Phase 2 Execute relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 transitions | NO |

Direction A result: all 5 rows confirmed. Direction A invariant: HOLDS.

---

### Role-Schema Binding Summary

`RoleName` = {role name strings from skill spec}.

Declare every role that will appear in Phase 2 Execute before Stage 2 begins.

| Role (RoleName) | Schema 1 binding (SeverityVocab) | Schema 2 binding (GapTypeVocab) | Notes |
|-----------------|----------------------------------|--------------------------------|-------|
| [role from spec] | [severity labels applicable; or "N/A -- no EG findings"] | [Source labels this role may produce; label lock if promoted] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Catalog every gap using Schema 2 Source labels and Schema 1
Severity labels. Do not consult the test invocation.

| ID | Gap | Source (GapTypeVocab) | Severity (SeverityVocab) | Affects phase (PhaseRef) |
|----|-----|-----------------------|--------------------------|--------------------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`]. Do not re-derive. Do not resolve silently.

---

#### SA-TO-SG PROMOTION

Every SA gap in the Stage 1 relay is evaluated at the Setup boundary.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

Updated relay:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock active. `DEFECT: LABEL-LOCK-VIOLATION` if promoted gap uses SA downstream.

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding (SeverityVocab): [severity labels applicable, or "N/A"]
  Schema 2 binding (GapTypeVocab): [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear. Three required seeded fields in every role relay: `Schema 2 compliance:`,
`Binding Summary row:` (Direction B seed), `Schema-governed action:` (Direction A seed).
A relay missing either seeded field must declare the absence explicitly.

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

> STRUCTURAL MANDATE (C-21): The relay anti-pattern prohibition row is a named structural
> mandate of this prompt. Reproduce it exactly as shown. A scorer confirms C-21 compliance by
> locating the row carrying `VIOLATION` in the `Required (RequiredVocabulary)` column without
> parsing the Field or Format cells.

| Field | Format | Required (RequiredVocabulary) |
|-------|--------|-------------------------------|
| Received from | [prior role or Setup] | YES |
| Received values | [name: value, ...] | YES |
| Schema 2 compliance | Source labels used: [list (GapTypeVocab)] -- all valid: YES / NO | YES |
| Binding Summary row | [row index] (Direction B seed) | YES |
| Schema-governed action | [action using Schema 1 or 2 labels per Binding Summary declaration] | YES |
| SA/SG gaps affecting this role | [list (GapTypeVocab) or "none -- confirmed"] | YES |
| Produced | [artifact content added] | YES |
| EG gaps encountered | [EG-NN list or "none"] | YES |
| **Anti-pattern**: DO NOT omit Schema 2 compliance field or relay seeded fields | Relay without these fields is structurally invalid | VIOLATION |

For each role, write the relay before the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed)
- **Schema-governed action**: [action] **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 2.5 -- Role Bijection Checkpoint

**Named inter-phase checkpoint**. Runs immediately after Phase 2 Execute. Phase 3 cannot
begin until this checkpoint produces a gate result.

**Sub-element ordering invariant**: The three sub-elements appear in canonical order:
sub-element 1 (status column semantics) first, sub-element 2 (five-case algorithm table)
second, sub-element 3 (Role Bijection Table) third. Re-ordering is a structural violation.

---

##### Phase 2.5 sub-element 1 of 3 -- Status Column Semantics

Column A -- `A: Acts in Execute` -- domain: {`YES`, `SILENT`, `relay field absent`}.

- `YES`: `Schema-governed action:` field read from Execute relay. Role produced a
  schema-governed action matching its Binding Summary declaration. Direction A holds.
- `SILENT`: No Execute relay found, or relay carries no action field. Binding Summary
  entry exists. Role declared to act but produced no schema-governed action. Direction A
  violated. Gate consequence: BLOCKED.
- `relay field absent`: Execute relay exists; `Schema-governed action:` field absent from
  relay body. Relay structurally incomplete; Direction A seed not planted. Gate: BLOCKED.

Column B -- `B: Declared in Summary` -- domain: {`YES`, `UNDECLARED`, `relay field absent`}.

- `YES`: `Binding Summary row:` field read from Execute relay. Role declared its entry via
  relay seed. Direction B holds.
- `UNDECLARED`: Execute relay exists; no Binding Summary entry for this role. Role produced
  schema-governed action without declaring intent. Direction B violated. Gate: BLOCKED.
- `relay field absent`: Execute relay exists; `Binding Summary row:` field absent from relay
  body. Relay structurally incomplete; Direction B seed not planted. Gate: BLOCKED.

---

##### Phase 2.5 sub-element 2 of 3 -- Evidence Source Column Population (exhaustive five-case table)

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` field in relay; BSR = `Binding Summary row:` field
in relay; BS entry = Binding Summary row exists for this role.

Locate the matching case; copy A Evidence source and B Evidence source values exactly.
Exactly five cases; no additional cases exist.

---

##### Phase 2.5 sub-element 3 of 3 -- Role Bijection Table

**Role bijection invariant**: Role R is in the Binding Summary iff it produces at least one
schema-governed action in Phase 2 Execute.

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- SILENT: declared in Summary but produced no schema-governed action in Execute."
- "[role] -- UNDECLARED: acted in Execute without Binding Summary entry."
- "[relay] -- relay field absent: [field name] missing from relay."

**Biconditional hold summary**:

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

**Three defect classes -- coequal BLOCKED triggers**: SILENT, UNDECLARED, and relay field
absent trigger Phase 3 BLOCKED coequally. None is subordinate to or deferred relative to
the others.

If any A != YES or B != YES:
**Phase 3 BLOCKED: [classify as SILENT / UNDECLARED / relay field absent. Name the role relay
and the specific defect. Enumerate all three defect class names explicitly: SILENT, UNDECLARED,
relay field absent. Resolve before proceeding.]**

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent).

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

Phase 3 runs in the sub-step sequence declared in Schema 5.

##### Step 3a -- Severity Legend

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label (SeverityVocab) | Definition for this trace | Actionability threshold |
|-----------------------|--------------------------|------------------------|
| P1 | [what blocks useful baseline] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source (GapTypeVocab) | Severity (SeverityVocab) | Action |
|----|---------|----------------------|--------------------------|--------|

Minimum 2 entries. At least 2 distinct Source types.

Schema 5 transition: >=2 entries -> Step 3c valid.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated.

**G-1**: Source types in Step 3b: [list] -- G-1: PASS / FAIL
**G-2**: Same-Source pairs with identical Action: [list or "none"] -- G-2: PASS / FAIL
**G-3**: Severity labels in Step 3b: [list] -- G-3: PASS / FAIL

If any FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Phase 4 BLOCKED. Resolve, re-run, confirm
PASS before proceeding.

Schema 5 transition: all-PASS -> Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS.

Activate Schema 3 channels: spec / invocation / artifact / quality.
Every Phase 4 Amend entry requires `[remediation channel: ...]`.

Schema 5 transition: channel active -> Phase 4 valid.

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: `DEFECT: PREMATURE-PHASE-ADVANCE`. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy (Schema 3 ChannelVocab): spec / invocation / artifact / quality.

Change entry:
- [finding: `{{F-NN}}`]
- [source: `{{source}}` (GapTypeVocab)] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality (ChannelVocab)]
- [section changed: ]
- [change: ]

Dismissal entry:
- [finding: `{{F-NN}}`], [reason: ], [remediation channel: ], [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

> STRUCTURAL MANDATE (C-35): The PRE-READ GATE is a named structural mandate of this prompt.
> Reproduce it exactly as shown. A scorer confirms C-35 compliance by locating the PRE-READ GATE
> block immediately before the compliance ledger without parsing ledger row values.

Before reading the compliance ledger, confirm in sequence:
1. Defect Classification Registry is present before Stage 1 in this output.
2. All FAIL rows carry a `DefectCodeVocab` value -- not free-form prose.
3. No cell in the `Defect code (DefectCodeVocab)` column is empty.

If check 3 fires: emit `DEFECT: EMPTY-CELL` before proceeding.

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** (Component 5 of Template Component Registry, C-47) -- typed
columns in this prompt, including this registry's own typed column at row 29. Each row is
independently row-verifiable. A scorer confirms C-46 compliance by locating this table
(declared as TCR Component 5, C-47) and verifying the Template Component Registry row is
present without parsing inline scope lists.

| # | Column name (TypeName) | Host registry / table |
|---|------------------------|----------------------|
| 1 | `Defect code (DefectCodeVocab)` | Defect Classification Registry |
| 2 | `Defect code (DefectCodeVocab)` | Verdict compliance ledger |
| 3 | `Required (RequiredVocabulary)` | Phase 2 Execute relay schema |
| 4 | `Required (RequiredVocabulary)` | Template Component Registry |
| 5 | `Content (ContentVocab)` | Coverage Matrix |
| 6 | `Declared-at (PhaseRef)` | Coverage Matrix |
| 7 | `Referenced-by (PhaseRef)` | Coverage Matrix |
| 8 | `Role-binding (RoleRef)` | Coverage Matrix |
| 9 | `Verdict-check (VCIdentifier)` | Coverage Matrix |
| 10 | `Label (SeverityVocab)` | Schema 1 table |
| 11 | `Blocks? (BlocksVocab)` | Schema 1 table |
| 12 | `Type (GapTypeVocab)` | Schema 2 table |
| 13 | `Promotion rule (PromotionVocab)` | Schema 2 table |
| 14 | `Channel (ChannelVocab)` | Schema 3 table |
| 15 | `Activated-at (ActivationPhaseRef)` | Schema 3 table |
| 16 | `Gate (GateIdentifier)` | Schema 4 table |
| 17 | `Hard-stop condition (BlockConditionVocab)` | Schema 4 table |
| 18 | `Step (StepIdentifier)` | Schema 5 table (Step column) |
| 19 | `Prerequisite (StepIdentifier)` | Schema 5 table |
| 20 | `Unblocks (StepIdentifier)` | Schema 5 table |
| 21 | `Role (RoleName)` | Role-Schema Binding Summary |
| 22 | `Schema 1 binding (SeverityVocab)` | Role-Schema Binding Summary |
| 23 | `Schema 2 binding (GapTypeVocab)` | Role-Schema Binding Summary |
| 24 | `Source (GapTypeVocab)` | Stage 1 audit table |
| 25 | `Severity (SeverityVocab)` | Stage 1 audit table |
| 26 | `Affects phase (PhaseRef)` | Stage 1 audit table |
| 27 | `Source (GapTypeVocab)` | Step 3b findings table |
| 28 | `Severity (SeverityVocab)` | Step 3b findings table |
| 29 | `Column name (TypeName)` | ANNOTATION SCOPE REGISTRY |

Expected annotation count: **29** (count of rows above, including this registry's own
typed column at row 29).

IF count of `(TypeName)`-annotated columns in output = 29: **confirmed**
IF count ≠ 29: **mismatch** -- emit `DEFECT: COUNT-MISMATCH`

---

#### Compliance Ledger

`Observed behavior: as expected` is structurally invalid in any cell.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result | Defect code (DefectCodeVocab) |
|----|--------|-----------|------------------|------------------|--------|-------------------------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what legend stated] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [list severity values] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Step 3c G-3 | Severity completeness gate checked | [G-3 result; labels checked] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values in Amend] | PASS / FAIL | -- |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use only P1/P2/P3 | [list labels this role used] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL | -- |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [list Source labels] | PASS / FAIL | -- |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels valid; lock honored | [Source labels in relay] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL | -- |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels used; any missing] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [G-1/G-2/G-3 results] | PASS / FAIL | -- |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL | -- |
| VC-4 | Schema 4 | G-1 cross-role | Source diversity across all roles | [Source types and roles per type] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [transition evidence] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c | [transition evidence] | PASS / FAIL | -- |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL | -- |

Rules: PASS rows carry `--` in Defect code. FAIL rows carry a `DefectCodeVocab` code. No
empty cells.

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assembled from Schema footprint records. Direction B invariant: every schema referenced in
any phase appears in the Coverage Matrix.

| Phase / Step | Schema referenced | Matrix row | Registered? |
|--------------|------------------|------------|-------------|
| Stage 1 | Schema 2, Schema 1 | Rows 2, 1 | YES |
| SA-TO-SG PROMOTION | Schema 2 | Row 2 | YES |
| Phase 1 Setup | Schema 1, Schema 2 | Rows 1, 2 | YES |
| Phase 2 Execute | Schema 2, Schema 1 | Rows 2, 1 | YES |
| Step 3a | Schema 1, Schema 5 | Rows 1, 5 | YES |
| Step 3b | Schema 2, Schema 1, Schema 5 | Rows 2, 1, 5 | YES |
| Step 3c | Schema 4, Schema 5 | Rows 4, 5 | YES |
| Step 3d | Schema 3, Schema 5 | Rows 3, 5 | YES |
| Phase 4 Amend | Schema 2, Schema 3, Schema 1, Schema 4 | Rows 2, 3, 1, 4 | YES |

Undeclared references: NONE. Direction B: HOLDS.

**C-10 Coverage Matrix bijection**: Direction A (HOLDS) + Direction B (HOLDS) = C-10: PASS.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

### CONFORMANCE-COLLAPSE CLAIM

All `STRUCTURAL MANDATE` blocks in this prompt conform to the canonical template declared in
the Canonical STRUCTURAL MANDATE Template section. Any block conforming to the canonical
template satisfies both C-39 (self-citing header `(C-XX)`) and C-40 (scorer confirmation
closing) by a single template-conformance check -- without inspecting individual block bodies.
The ANNOTATION SCOPE REGISTRY table is declared as Component 5 (C-47) of the Template
Component Registry, making its presence verifiable by TCR row lookup rather than Verdict
section scan.

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared;
(b) TCR rows 1-4 conform to the canonical template and TCR row 5 (C-47) names the ANNOTATION
SCOPE REGISTRY with its typed-column notation `# / Column name (TypeName) / Host registry /
table` -- confirming C-47 compliance by TCR row 5 label scan alone; and (c) the ANNOTATION
SCOPE REGISTRY table appears in the Verdict C-28 COUNT GATE section as declared by TCR row 5
(C-47), containing 29 rows including the registry's own typed column at row 29 -- without
inspecting individual `STRUCTURAL MANDATE` block bodies.
