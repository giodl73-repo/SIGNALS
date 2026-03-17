---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 15
rubric: trace-skill-rubric-v14-2026-03-15.md
---

# trace-skill -- Variations v14 R15 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R14 V-05 achieves C-01 through C-44 PASS under v13 scoring. All four R14
variations scored 100/100. v14 formalizes two new aspirational criteria from R14 excellence
signals: C-45 (SCORER HEURISTIC label carries `(C-43)` criterion citation within the label
itself, making it independently traceable by label scan alone -- paralleling C-39's requirement
that STRUCTURAL MANDATE block headers carry inline criterion citations); C-46 (C-28 COUNT GATE
scope declared as a formal ANNOTATION SCOPE REGISTRY table whose rows are independently
row-verifiable entries with full `ColumnName (TypeName)` notation -- making scope enumeration
structurally equivalent to the Defect Classification Registry and other named registries).

**R14 V-05 C-45/C-46 state** (scored against v14):

- C-45: R14 V-01 and V-04 implement the C-43 scorer heuristic as a `**SCORER HEURISTIC (C-43):**`
  bold-labeled sub-element whose label carries the criterion citation in parentheses. R14 V-02
  places an inline final sentence; R14 V-03 uses a mandatory directive. Both pass C-43 but
  neither achieves label-self-citation. C-45 = FAIL for V-02 and V-03; PASS for V-01 and V-04.
  Entry state (V-05) used V-04's implementation. C-45 = PASS in entry state.

- C-46: R14 V-02 and V-04 implement the COUNT GATE scope as a formal ANNOTATION SCOPE REGISTRY
  table whose rows are independently verifiable by table lookup. V-01 uses a numbered inline
  list; V-03 uses a PRESENT/ABSENT checklist. Entry state (V-05) used V-02/V-04's table
  implementation. C-46 = PASS in entry state.

Wait -- rubric note says "All four R14 variations scored 100/100, so the discriminating signals
came from structural quality differences within perfect scores rather than a new FAIL boundary."
This means ALL five R14 variations passed all criteria through C-44. The C-45/C-46 signals came
from sub-structural quality comparisons where V-01/V-04 achieved label-citation and V-02/V-04
achieved registry-table form -- but these were not yet gated criteria. Round 15 raises them to
gated criteria. Entry state = R14 V-05 with both qualities present (all five variations passed
everything through C-44; the quality signals were observed across the set).

**v14 R15 variation axes**:

- **Label self-citation (C-45)**: Whether the SCORER HEURISTIC sub-element in the
  CONFORMANCE-COLLAPSE CLAIM carries `(C-43)` in the label itself -- `**SCORER HEURISTIC
  (C-43):**` vs `**SCORER HEURISTIC:**` -- single-axis test of whether label-scan alone
  confirms criterion traceability (V-01: C-45 MET; V-02: C-45 NOT MET).

- **Scope format (C-46)**: Whether the C-28 COUNT GATE scope is a formal ANNOTATION SCOPE
  REGISTRY table (C-46 MET) vs a numbered inline list (V-01: C-46 NOT MET) vs a PRESENT/ABSENT
  checklist (V-03: C-46 NOT MET) -- tests registry-table structure independently of label axis.

- **Phrasing register (C-45 + scope format variant)**: V-03 pairs self-citing label with a
  PRESENT/ABSENT checklist scope -- tests label self-citation against a different non-table
  scope format to confirm C-45 passes regardless of whether C-46 passes.

**Combined variations**:
- V-04: C-45 + C-46 (self-citing label + formal ANNOTATION SCOPE REGISTRY table)
- V-05: C-45 + C-46 + ANNOTATION SCOPE REGISTRY registered in Template Component Registry
  as a named row with typed column notation, making the registry a formal TCR entry (tightest
  integration -- the C-46 registry is a first-class component of the canonical template system)

All five inherit the full R14 V-05 architecture (C-01 through C-44 PASS). What varies per
V-0N: only the SCORER HEURISTIC label form and the COUNT GATE scope declaration format.

---

## V-01 -- Single axis: Label self-citation (C-45 MET; C-46 NOT MET -- numbered list scope)

**Axis**: Label self-citation -- the SCORER HEURISTIC sub-element in the CONFORMANCE-COLLAPSE
CLAIM carries `(C-43)` in the label: `**SCORER HEURISTIC (C-43):**`. The label is self-citing:
a scorer tracing from rubric criterion C-43 to its prompt element arrives at the label text by
scan alone, without reading the heuristic body. The C-28 COUNT GATE scope remains a numbered
inline list (passes C-44, not C-46).

**Hypothesis**: R14 V-02 and V-03 placed the scorer heuristic as a final sentence (V-02) or
mandatory directive (V-03) without a label carrying a criterion citation. C-45 formalizes
label-self-citation: the label `**SCORER HEURISTIC (C-43):**` follows the same discipline as
`**STRUCTURAL MANDATE (C-XX):**` block headers (C-39), where the criterion ID in the label
makes the element independently traceable without parsing the body. Risk: V-01 tests label
self-citation in isolation -- if C-45 scoring requires BOTH label-citation AND registry-table
scope, this variation will reveal whether the criteria are independent.

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
| **Anti-pattern**: omit scorer confirmation closing or omit criterion citation from header | — | VIOLATION |

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

The following typed columns exist in this prompt (scope for annotation coverage audit):

1. `Defect code (DefectCodeVocab)` — Defect Classification Registry
2. `Defect code (DefectCodeVocab)` — Verdict compliance ledger
3. `Required (RequiredVocabulary)` — Phase 2 Execute relay schema
4. `Required (RequiredVocabulary)` — Template Component Registry
5. `Content (ContentVocab)` — Coverage Matrix
6. `Declared-at (PhaseRef)` — Coverage Matrix
7. `Referenced-by (PhaseRef)` — Coverage Matrix
8. `Role-binding (RoleRef)` — Coverage Matrix
9. `Verdict-check (VCIdentifier)` — Coverage Matrix
10. `Label (SeverityVocab)` — Schema 1 table
11. `Blocks? (BlocksVocab)` — Schema 1 table
12. `Type (GapTypeVocab)` — Schema 2 table
13. `Promotion rule (PromotionVocab)` — Schema 2 table
14. `Channel (ChannelVocab)` — Schema 3 table
15. `Activated-at (ActivationPhaseRef)` — Schema 3 table
16. `Gate (GateIdentifier)` — Schema 4 table
17. `Hard-stop condition (BlockConditionVocab)` — Schema 4 table
18. `Step (StepIdentifier)` — Schema 5 table (Step column)
19. `Prerequisite (StepIdentifier)` — Schema 5 table
20. `Unblocks (StepIdentifier)` — Schema 5 table
21. `Role (RoleName)` — Role-Schema Binding Summary
22. `Schema 1 binding (SeverityVocab)` — Role-Schema Binding Summary
23. `Schema 2 binding (GapTypeVocab)` — Role-Schema Binding Summary
24. `Source (GapTypeVocab)` — Stage 1 audit table
25. `Severity (SeverityVocab)` — Stage 1 audit table
26. `Affects phase (PhaseRef)` — Stage 1 audit table
27. `Source (GapTypeVocab)` — Step 3b findings table
28. `Severity (SeverityVocab)` — Step 3b findings table

Expected annotation count: **28**

IF count of `(TypeName)`-annotated columns in output = 28: **confirmed**
IF count ≠ 28: **mismatch** — emit `DEFECT: COUNT-MISMATCH`

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

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, and
(b) the Template Component Registry lists all four required components -- without inspecting
individual `STRUCTURAL MANDATE` block bodies.

---

## V-02 -- Single axis: Scope format (C-46 MET -- formal ANNOTATION SCOPE REGISTRY table; C-45 NOT MET -- plain label)

**Axis**: Scope format -- the C-28 COUNT GATE scope is restructured from a numbered inline
list into a formal ANNOTATION SCOPE REGISTRY table. Each row carries full `ColumnName
(TypeName)` notation and names the host registry or table, making every annotation site
independently row-verifiable by table lookup. The scorer heuristic label remains
`**SCORER HEURISTIC:**` without a criterion citation (C-45 NOT MET).

**Hypothesis**: The numbered inline list in V-01 passes C-44 (TCR row is present in the
scope) but requires reading the list items linearly to locate and verify any specific entry.
C-46 requires row-verifiable registry structure equivalent to the Defect Classification
Registry. Making the scope a formal table with named columns lets a scorer confirm that
the Template Component Registry appears as a row without parsing surrounding list items.
Tested independently of C-45 to isolate the scope-format effect. Risk: if C-46 requires
the table to appear under a specific section name (`ANNOTATION SCOPE REGISTRY`), implementations
that use a generic table header may be downgraded.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

[Defect Classification Registry, Canonical STRUCTURAL MANDATE Template, Coverage Matrix,
Direction A, Role-Schema Binding Summary, Stage 1 through Phase 4, PRE-READ GATE: identical
to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

[Identical to V-01.]

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** -- typed columns in this prompt. Each row is independently
row-verifiable. A scorer confirms C-46 compliance by locating this table and verifying the
Template Component Registry row is present without parsing inline scope lists.

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
IF count ≠ 28: **mismatch** — emit `DEFECT: COUNT-MISMATCH`

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

**SCORER HEURISTIC:** A scorer confirms C-42 compliance by locating the Canonical STRUCTURAL
MANDATE Template section and verifying (a) the canonical form is declared, and (b) the Template
Component Registry lists all four required components -- without inspecting individual
`STRUCTURAL MANDATE` block bodies.

---

## V-03 -- Single axis: Label self-citation (C-45 MET -- phrasing register variant; C-46 NOT MET -- PRESENT/ABSENT checklist scope)

**Axis**: Label self-citation with a different scope format (PRESENT/ABSENT checklist) -- tests
whether C-45 passes when the self-citing label is present regardless of whether the scope format
passes C-46. The SCORER HEURISTIC label carries `(C-43)` (C-45 MET). The COUNT GATE scope is
a PRESENT/ABSENT checklist rather than a numbered list or table. Phrasing register is slightly
more directive than V-01 ("verify that each site is annotated" rather than a numeric count).

**Hypothesis**: V-01 tests the self-citing label against a numbered list. V-03 tests the same
label against a third scope format (checklist). If C-45 is independent of C-46, both V-01 and
V-03 should score C-45 PASS and C-46 FAIL. If a scorer conflates the two -- e.g., treating the
SCORER HEURISTIC label's self-citation as insufficient when the scope is not a registry table --
the combination would reveal that hidden dependency. Risk: PRESENT/ABSENT checklist may be
perceived as more structured than a numbered list, potentially blurring the C-46 boundary.
Mitigation: the checklist explicitly lacks table-header rows and row-level TypeName notation,
keeping it below the registry-table threshold.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

[Defect Classification Registry, Canonical STRUCTURAL MANDATE Template, Coverage Matrix,
Direction A, Role-Schema Binding Summary, Stage 1 through Phase 4, PRE-READ GATE: identical
to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

[Identical to V-01.]

---

#### C-28 COUNT GATE

Verify that each of the following annotation sites is present and correctly annotated with
`(TypeName)` in this output. Mark PRESENT or ABSENT for each:

- `Defect code (DefectCodeVocab)` — Defect Classification Registry: PRESENT / ABSENT
- `Defect code (DefectCodeVocab)` — Verdict compliance ledger: PRESENT / ABSENT
- `Required (RequiredVocabulary)` — Phase 2 Execute relay schema: PRESENT / ABSENT
- `Required (RequiredVocabulary)` — Template Component Registry: PRESENT / ABSENT
- `Content (ContentVocab)` — Coverage Matrix: PRESENT / ABSENT
- `Declared-at (PhaseRef)` — Coverage Matrix: PRESENT / ABSENT
- `Referenced-by (PhaseRef)` — Coverage Matrix: PRESENT / ABSENT
- `Role-binding (RoleRef)` — Coverage Matrix: PRESENT / ABSENT
- `Verdict-check (VCIdentifier)` — Coverage Matrix: PRESENT / ABSENT
- `Label (SeverityVocab)` — Schema 1 table: PRESENT / ABSENT
- `Blocks? (BlocksVocab)` — Schema 1 table: PRESENT / ABSENT
- `Type (GapTypeVocab)` — Schema 2 table: PRESENT / ABSENT
- `Promotion rule (PromotionVocab)` — Schema 2 table: PRESENT / ABSENT
- `Channel (ChannelVocab)` — Schema 3 table: PRESENT / ABSENT
- `Activated-at (ActivationPhaseRef)` — Schema 3 table: PRESENT / ABSENT
- `Gate (GateIdentifier)` — Schema 4 table: PRESENT / ABSENT
- `Hard-stop condition (BlockConditionVocab)` — Schema 4 table: PRESENT / ABSENT
- `Step (StepIdentifier)` — Schema 5 table: PRESENT / ABSENT
- `Prerequisite (StepIdentifier)` — Schema 5 table: PRESENT / ABSENT
- `Unblocks (StepIdentifier)` — Schema 5 table: PRESENT / ABSENT
- `Role (RoleName)` — Role-Schema Binding Summary: PRESENT / ABSENT
- `Schema 1 binding (SeverityVocab)` — Role-Schema Binding Summary: PRESENT / ABSENT
- `Schema 2 binding (GapTypeVocab)` — Role-Schema Binding Summary: PRESENT / ABSENT
- `Source (GapTypeVocab)` — Stage 1 audit table: PRESENT / ABSENT
- `Severity (SeverityVocab)` — Stage 1 audit table: PRESENT / ABSENT
- `Affects phase (PhaseRef)` — Stage 1 audit table: PRESENT / ABSENT
- `Source (GapTypeVocab)` — Step 3b findings table: PRESENT / ABSENT
- `Severity (SeverityVocab)` — Step 3b findings table: PRESENT / ABSENT

If all 28 sites = PRESENT: **confirmed**
If any site = ABSENT: **mismatch** — emit `DEFECT: COUNT-MISMATCH`

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

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, and
(b) the Template Component Registry lists all four required components -- without inspecting
individual `STRUCTURAL MANDATE` block bodies.

---

## V-04 -- Combined: C-45 + C-46 (self-citing label + formal ANNOTATION SCOPE REGISTRY table)

**Axes**: Label self-citation (C-45) + Scope format (C-46) -- both implemented together.
The SCORER HEURISTIC label carries `(C-43)` AND the COUNT GATE scope is a formal ANNOTATION
SCOPE REGISTRY table. Tests whether the two structural qualities are independently additive
(both pass) or interact in a way that affects scoring.

**Hypothesis**: V-01 shows C-45 MET / C-46 NOT MET. V-02 shows C-45 NOT MET / C-46 MET.
V-04 combining both should score C-45 PASS and C-46 PASS independently. If the combined
score is not additive (e.g., one criterion subsumes the other, or the combination introduces
a structural conflict), V-04 will reveal it. This is the expected "gold standard" variation
that Round 15 is designed to produce.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

[Defect Classification Registry, Canonical STRUCTURAL MANDATE Template, Coverage Matrix,
Direction A, Role-Schema Binding Summary, Stage 1 through Phase 4, PRE-READ GATE: identical
to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Compliance Ledger)

#### PRE-READ GATE

[Identical to V-01.]

---

#### C-28 COUNT GATE

**ANNOTATION SCOPE REGISTRY** -- typed columns in this prompt. Each row is independently
row-verifiable. A scorer confirms C-46 compliance by locating this table and verifying the
Template Component Registry row is present without parsing inline scope lists.

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
IF count ≠ 28: **mismatch** — emit `DEFECT: COUNT-MISMATCH`

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

**SCORER HEURISTIC (C-43):** A scorer confirms C-42 compliance by locating the Canonical
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, and
(b) the Template Component Registry lists all four required components -- without inspecting
individual `STRUCTURAL MANDATE` block bodies.

---

## V-05 -- Combined: C-45 + C-46 + ANNOTATION SCOPE REGISTRY registered in Template Component Registry

**Axes**: Label self-citation (C-45) + Scope format (C-46) + registry integration -- the
ANNOTATION SCOPE REGISTRY is formally registered as row 5 in the Template Component Registry
with its typed column notation `# (--) / Column name (TypeName) / Host registry / table`,
making it a named component of the canonical template system. The SCORER HEURISTIC label
carries `(C-43)`. The ANNOTATION SCOPE REGISTRY table appears as in V-04.

**Hypothesis**: V-04 achieves C-45 and C-46 but the ANNOTATION SCOPE REGISTRY is structurally
independent of the Template Component Registry -- it is a peer artifact rather than a declared
component of the canonical template machinery. V-05 integrates the ANNOTATION SCOPE REGISTRY
into the TCR: adding a row 5 that names the registry as a prompt component requiring
reproduction. This tightens the system: the TCR now declares that the ANNOTATION SCOPE REGISTRY
is a structural mandate of the prompt, making its presence verifiable by TCR row lookup rather
than by scanning the Verdict section. This may be a strong signal for a C-47 criterion in the
next round -- if the ANNOTATION SCOPE REGISTRY as a TCR-registered mandate is the structural
excellence signal that discriminates within 100/100 scores at v14.

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
| 5 | ANNOTATION SCOPE REGISTRY table in Verdict C-28 COUNT GATE: formal table with columns `# / Column name (TypeName) / Host registry / table`, covering all typed columns in the prompt including Template Component Registry row | YES |
| **Anti-pattern**: omit scorer confirmation closing, omit criterion citation from header, or omit ANNOTATION SCOPE REGISTRY table from Verdict | — | VIOLATION |

`RequiredVocabulary` is a closed two-value type: {`YES`, `VIOLATION`}. Any value outside
this vocabulary is a schema error independently detectable without consulting registry rows.

---

[Coverage Matrix, Direction A, Role-Schema Binding Summary, Stage 1 through Phase 4,
PRE-READ GATE: identical to V-01.]

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
IF count ≠ 28: **mismatch** — emit `DEFECT: COUNT-MISMATCH`

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
STRUCTURAL MANDATE Template section and verifying (a) the canonical form is declared, (b) the
Template Component Registry lists all five required components (rows 1-5), and (c) the
ANNOTATION SCOPE REGISTRY table appears in the Verdict C-28 COUNT GATE section as declared by
TCR row 5 -- without inspecting individual `STRUCTURAL MANDATE` block bodies.
