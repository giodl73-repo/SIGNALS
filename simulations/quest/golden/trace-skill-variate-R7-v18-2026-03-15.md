---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 7
rubric: trace-skill-rubric-v18-2026-03-15.md
---

# trace-skill -- Variations v18 R7 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R6 V-05 achieves C-01 through C-23 PASS under v17 scoring. v18 formalizes three
new aspirational criteria from R6 excellence signals: C-24 (N-way independence notation in the
element-criterion table -- where a single structural element satisfies three or more criteria
independently, each criterion gets a named distinct verifiable property, generalizing C-22's
pairwise pattern to arbitrary N-way independence), C-25 (joint satisfaction as a distinct
relationship type -- where two or more structural elements together satisfy a criterion that
neither satisfies alone, the element-criterion table explicitly declares the relationship as
joint with a "neither alone" statement), C-26 (numbered sub-elements as Verdict cross-reference
coordinates -- the sequence-number labels introduced by C-21 become the Location strings in the
C-22 element index, and Verdict citations reference sub-elements by those same coordinates,
creating a two-layer navigation property that neither criterion alone produces).

**R6 V-05 C-24/C-25/C-26 state** (scored against v18):

- C-24: R6 V-05 Verdict contains "satisfies C-17 location requirement and C-18 format requirement
  independently" for E6. This demonstrates pairwise independence (C-22). It does not generalize
  to N-way: no element in R6 V-05 satisfies three or more criteria with three independently
  named verifiable properties. The algorithm table (E2) satisfies C-15, C-19, and C-23 but the
  Verdict does not name the three properties -- it lists the criteria without naming what specific
  aspect of E2 each criterion checks. C-24 = FAIL.

- C-25: R6 V-05 Verdict element-criterion notes name elements and criteria but use only the
  independence relationship. C-14 (relay-seeded evidence capture) is satisfied by the combination
  of Execute relay seeded fields AND the Role Bijection Table reading them, but the Verdict does
  not introduce a "joint" relationship type or declare that neither element alone suffices. C-25
  = FAIL.

- C-26: R6 V-05 Phase 2.5 sub-elements carry sequence labels from C-21 ("sub-element 1 of 3",
  etc.) and the Verdict carries element labels (E1, E2, ...) with location descriptions. However,
  the Location strings in the Verdict element index use prose descriptions ("Phase 2.5 sub-element
  2 of 3 -- five-case algorithm table") rather than the compact C-21 sequence-number coordinates.
  The two-layer navigation property (C-21 number = C-22 Location string) is not present. C-26 =
  FAIL.

**v18 R7 variation axes**:

- **Output format (C-24)**: Element-criterion table restructured to support N-way independence
  notation (V-01) -- for an element satisfying N >= 3 criteria independently, the table carries
  one row per criterion with a named verifiable property column stating the specific aspect of
  the element that criterion checks; the N-way case is annotated "independent (N-way)" to
  distinguish from pairwise independence.

- **Output format (C-25)**: Element-criterion table gains a Relationship column with values
  `sole`, `independent`, `joint` (V-02) -- joint entries identify both elements, declare the
  criteria satisfied, and include a "neither alone" statement naming what each element contributes
  and why the other is insufficient; C-14 is the joint case (Execute relay seeded fields + Role
  Bijection Table).

- **Output format (C-26)**: Phase 2.5 sub-element labels become the Location strings in the
  element index (V-03) -- the C-21 sequence numbers (2.5.1, 2.5.2, 2.5.3) are used verbatim as
  Location column values; Verdict criterion citations reference sub-elements by coordinate; the
  element index becomes a two-layer navigation surface: coordinate locates the element in the
  prompt, criteria column locates the requirement in the rubric.

**Combined variations**:
- V-04: C-24 + C-25 (N-way independence + joint satisfaction)
- V-05: C-24 + C-25 + C-26 (all three -- complete v18 target)

All five inherit the full R6 V-05 architecture (C-01 through C-23 PASS). What varies per V-0N:
only the element-criterion Verdict table and (in V-03/V-05) the Phase 2.5 sub-element Location
coordinate format.

---

## V-01 -- Single axis: Output format (C-24: N-way independence notation)

**Axis**: Output format -- the Verdict element-criterion index is restructured to support N-way
independence notation. A new "Named verifiable property" column is added. For elements satisfying
two criteria independently (pairwise, C-22), each criterion row carries one named property. For
E2 (five-case algorithm table), which satisfies C-15, C-19, and C-23 independently (N-way, three
criteria), each of the three criteria rows carries a distinct named verifiable property stating
the specific aspect of E2 that criterion checks. The three properties are mutually non-overlapping:
a tracer can check each property without consulting the other two. The N-way annotation reads
"independent (N-way with C-15, C-19, C-23)" per row.

**Hypothesis**: R6 V-05 Verdict names criteria in prose ("C-15: PASS (Evidence source column...)
C-19: PASS (five-case exhaustive table...)") but does not name a distinct verifiable property per
criterion for multi-criterion elements. A reviewer scoring C-24 cannot confirm that the three
criteria are checked independently without parsing prose to infer what property each targets.
The named-property column makes independence structural: each row states the specific measurable
property the criterion checks, and the properties are visibly distinct. A reviewer can verify
N-way independence by checking that the three property strings name three non-overlapping aspects
of E2. Risk: the property column increases table width and may tempt tautological entries (e.g.,
"property: satisfies C-19"). Mitigation: properties must name an observable, criterion-agnostic
aspect of the element -- something a reader could check against the prompt text without knowing
the criterion ID.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.
A Coverage Matrix entry is valid if and only if it is referenced in at least one downstream
phase. Both directions constitute the Coverage Matrix closed-world bijection (C-10).

The Phase 2.5 Role Bijection Checkpoint runs between Phase 2 Execute and Phase 3 Findings.
Its three co-located sub-elements appear in canonical order: status column semantics block
first (C-20), five-case algorithm table second (C-19), Role Bijection Table third (C-12).
Re-ordering these sub-elements is a structural violation coequal with schema label violations.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Setup per-role attribution, Step 3b Source column, Execute role relay | All roles (Source labels in relay; promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments from all roles | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 checks Source diversity across all roles' Step 3b contributions | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between sub-steps) | N/A -- applies to Findings phase structure | VC-5 |

**Schema definitions** (biconditional -- violations are structural invalidity, not quality issues):

**Schema 1**: A trace is valid w.r.t. Schema 1 if and only if every severity label in any phase
uses only {P1, P2, P3}. P1 = blocks useful artifact baseline. P2 = quality improvement. P3 = advisory.

**Schema 2**: SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all phases
after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a structural violation.

**Schema 3**: A trace is valid w.r.t. Schema 3 if and only if every Phase 4 Amend entry names
a remediation channel from {spec, invocation, artifact, quality}.

**Schema 4**: G-1 invariant: Step 3b contains >=2 distinct Source types. G-2 invariant: no two
same-Source findings carry identical Action text. G-3 invariant: all Step 3b entries use only
{P1, P2, P3}.

**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >=2 entries. Step 3d
valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

| Schema | Matrix row | Referenced at (all phase/step names) | Orphan? |
|--------|-----------|--------------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend); Step 3b (enforce); Step 3c G-3 (verify); Phase 4 Amend (enforce) | NO |
| Schema 2 | Row 2 | Stage 1 audit; SA-TO-SG PROMOTION; Phase 1 per-role attribution; Step 3b Source; Execute role relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 transitions | NO |

Direction A result: all 5 rows confirmed. Direction A invariant: HOLDS.

---

### Role-Schema Binding Summary

Declare each role that will appear in Phase 2 Execute before Stage 2 begins. Role absent
from this table but appearing in Execute is a structural violation.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable; or "N/A -- no EG findings"] | [Source labels this role may produce; label lock if promoted] | [Schema 3/4 interactions if any] |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Catalog every gap using Schema 2 Source labels and Schema 1
Severity labels. A valid Stage 1 does not consult the test invocation.

**SA audit**: inputs not declared; role handoffs not specified; artifact sections without
content rules.
**SG pre-audit**: declared inputs the test invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

**Schema footprint -- Stage 1**: Schema 2 (Source labels), Schema 1 (Severity labels).

---

### Stage 2 -- Hand-Compilation

Stage 2 receives relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`]. Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION

Every SA gap in the Stage 1 relay is evaluated at the Setup boundary.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

After promotion: [SA remaining: `{{sa_remaining}}`], [SG from promotion: `{{sg_promoted}}`].

**Schema footprint -- SA-TO-SG PROMOTION**: Schema 2 (SA->SG label evaluated).

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable to this role's findings, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

A role entry without schema binding declaration is invalid.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

**Schema footprint -- Phase 1 Setup**: Schema 1 (binding declared per role), Schema 2
(bindings and promoted labels confirmed).

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear. Three required seeded fields in every role relay: `Schema 2 compliance:`, `Binding
Summary row:` (Direction B seed), `Schema-governed action:` (Direction A seed). A relay
missing either seeded field must declare the absence explicitly -- Phase 2.5 reads the relay
and detects relay field absent defects.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed)
- **Schema-governed action**: [action using Schema 1 or 2 labels per Binding Summary declaration]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in relays), Schema 1
(Severity on EG findings per role).

---

#### Phase 2.5 -- Role Bijection Checkpoint

**Named inter-phase checkpoint**. Runs immediately after Phase 2 Execute. Phase 3 cannot
begin until this checkpoint produces a gate result.

**Sub-element ordering invariant (C-21)**: The three sub-elements of Phase 2.5 appear in
canonical order: sub-element 1 first, sub-element 2 second, sub-element 3 third. Re-ordering
is a structural violation coequal with schema label violations.

---

##### Phase 2.5 sub-element 1 of 3 -- Status Column Semantics

The following block explains the meaning of each domain value per status column. An auditor
can verify any status cell in the Role Bijection Table using this block alone: each entry names
the relay field read, the bijection claim the value makes, and the gate consequence.

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.

- `YES` -- Relay field read: `Schema-governed action:` field in Execute relay. Claim: this role
  produced a schema-governed action matching its Binding Summary declaration. Direction A holds
  for this row. Gate consequence: no BLOCKED contribution from column A.
- `SILENT` -- Relay field read: no Execute relay found (or relay carries no action field).
  Binding Summary entry exists. Claim: role declared to act but produced no schema-governed
  action. Direction A violated. Gate consequence: BLOCKED.
- `relay field absent` -- Relay field read: Execute relay exists; `Schema-governed action:`
  field is absent from relay body. Claim: relay structurally incomplete; Direction A seed not
  planted. Direction A indeterminate. Gate consequence: BLOCKED.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.

- `YES` -- Relay field read: `Binding Summary row:` field in Execute relay. Claim: role declared
  its Binding Summary entry via relay seed. Direction B holds. Gate consequence: no BLOCKED.
- `UNDECLARED` -- Relay field read: Execute relay exists; no Binding Summary entry for this
  role. Claim: role produced schema-governed action without declaring intent. Direction B violated.
  Gate consequence: BLOCKED.
- `relay field absent` -- Relay field read: Execute relay exists; `Binding Summary row:` field
  absent from relay body. Claim: relay structurally incomplete; Direction B seed not planted.
  Direction B indeterminate. Gate consequence: BLOCKED.

---

##### Phase 2.5 sub-element 2 of 3 -- Evidence Source Column Population

**Evidence source column population -- exhaustive five-case table (C-19/C-23)**:

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` field in relay; BSR = `Binding Summary row:` field
in relay; BS entry = Binding Summary entry exists for this role.

Locate the matching case; copy A Evidence source and B Evidence source values exactly.
No inference required. Exactly five cases; no additional cases exist.

---

##### Phase 2.5 sub-element 3 of 3 -- Role Bijection Table

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged; relay-assembled; Evidence source column per row;
three-value status column domains):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- SILENT: declared in Summary but produced no schema-governed action in Execute."
- "[role] -- UNDECLARED: acted in Execute without Binding Summary entry."
- "[relay] -- relay field absent: [field name] missing from relay."

**Biconditional hold summary**:

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

**Three defect classes -- coequal BLOCKED triggers**: SILENT, UNDECLARED, and relay field absent
trigger Phase 3 BLOCKED coequally. No asymmetric treatment; none is subordinate to or deferred
relative to the others.

If any A != YES or B != YES:
**Phase 3 BLOCKED: [classify as SILENT / UNDECLARED / relay field absent. Name the role relay
and the specific defect. Enumerate all three defect class names explicitly. Resolve before
proceeding.]**

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent).

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

Phase 3 runs in the sub-step sequence declared in Schema 5.

##### Step 3a -- Severity Legend

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what blocks useful baseline] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

**Schema footprint -- Step 3a**: Schema 1 (legend declared), Schema 5 (transition recorded).

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

Schema 5 transition: >=2 entries -> Step 3c valid.

**Schema footprint -- Step 3b**: Schema 2 (Source column), Schema 1 (Severity column), Schema 5.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).

**G-1**: Source types in Step 3b: [list] -- G-1: PASS / FAIL
**G-2**: Same-Source pairs with identical Action: [list or "none"] -- G-2: PASS / FAIL
**G-3**: Severity labels in Step 3b: [list] -- G-3: PASS / FAIL

If any FAIL: Phase 4 BLOCKED. Resolve, re-run gate, confirm PASS before proceeding.

Schema 5 transition: all-PASS -> Step 3d valid.

**Schema footprint -- Step 3c**: Schema 4 (G-1/G-2/G-3 evaluated), Schema 5 (transition).

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS.
Schema 3 active: every Phase 4 Amend entry requires `[remediation channel: ...]`.
Schema 5 transition: channel active -> Phase 4 valid.

**Schema footprint -- Step 3d**: Schema 3 (activated), Schema 5 (transition).

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`. If any FAIL: BLOCKED.

Channel taxonomy (Schema 3): spec / invocation / artifact / quality.

Change entry:
- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section changed: ]
- [change: ]

Dismissal entry:
- [finding: `{{F-NN}}`], [reason: ], [remediation channel: ], [source type confirmed: YES / NO]

**Schema footprint -- Phase 4 Amend**: Schema 2 (Source lock), Schema 3 (channel field),
Schema 1 (Severity inherited), Schema 4 (gate pre-check).

---

### Verdict (Phase 5 -- Closed-World Audit + Element-Criterion Index)

#### Compliance Ledger

"Observed behavior: as expected" is structurally invalid in any cell.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what legend stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [list severity values, count each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate checked against Schema 1 | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use only P1/P2/P3 | [list labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [list Source labels in Step 3b] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels valid; lock honored | [Source labels used in relay] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels used; any missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity across all roles | [Source types; roles that contributed each] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [prerequisite evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL |

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assembled from per-phase Schema footprint records. Direction B invariant: every schema
referenced in any phase appears in the Coverage Matrix.

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

**C-10 Coverage Matrix bijection**: Direction A (HOLDS) + Direction B (HOLDS) = C-10: PASS.

---

#### Element-Criterion Index (C-24 N-way independence notation)

**Reading instructions**: Each row represents one criterion satisfied by one structural element.
Where an element satisfies N criteria independently, it has N rows. The "Named verifiable
property" column states the specific observable aspect of the element that the criterion checks
-- independent of the criterion ID and independently verifiable. Properties for the same element
must name non-overlapping aspects: a reviewer checks each property without consulting the others.
N-way annotation: where N >= 3, each row carries "independent (N-way)" to distinguish from
pairwise independence.

| Element | Location | Criteria ID | Relationship | Named verifiable property |
|---------|----------|-------------|--------------|--------------------------|
| E1: Status column semantics block | Phase 2.5, sub-element 1 of 3 | C-20 | sole | Block appears immediately before the Role Bijection Table. Each of the six domain values (three per column) has an entry naming: relay field read, bijection claim made, and gate consequence. Verifiable by reading block entries and confirming all three named fields are present per value. |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-15 | independent (N-way) | Each table row carries non-empty "A Evidence source" and "B Evidence source" cells containing relay-field name strings. Verifiable by scanning any row: both evidence-source cells contain a named relay-field string, not a placeholder or blank. |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-19 | independent (N-way) | Table has exactly five rows; section header declares the five-case enumeration exhaustive. Verifiable by counting table data rows: count = 5, no additional rows exist. |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-23 | independent (N-way) | No prose paragraph appears between the section header and the table body. All cells contain only closed-world tokens (present / absent / YES / SILENT / UNDECLARED / relay field absent / relay-field-name string). No parenthetical qualifiers appear inside any cell. Verifiable by checking for paragraph boundaries before the table and scanning cells for non-closed-world content. |
| E3: Role Bijection Table | Phase 2.5, sub-element 3 of 3 | C-12 | independent | Single table carries both A: Acts in Execute and B: Declared in Summary status columns; biconditional hold summary follows the table with one row per direction. Both closed-world directions verified in one surface without separate tables. Verifiable by confirming both A and B columns appear in one table and a two-row hold summary follows. |
| E3: Role Bijection Table | Phase 2.5, sub-element 3 of 3 | C-16 | independent | Column A header text defines domain {YES, SILENT, relay field absent}; column B header text defines domain {YES, UNDECLARED, relay field absent}. All three values for each column appear in the header text inline -- no footnote, no supplementary definition block required. Verifiable by reading column header text only. |
| E3 + E4: Role Bijection Table + Execute relay seeded fields | Phase 2.5, sub-element 3 of 3 + Phase 2 Execute, role relays | C-14 | [see C-25 axis -- not in V-01] | [not applicable to V-01 single-axis] |
| E5: BLOCKED language block | Phase 2.5, gate section | C-17 | independent | Block enumerates all three defect class names (SILENT, UNDECLARED, relay field absent) with an explicit coequal statement that none is subordinate to the others. Verifiable by confirming all three class names appear in the BLOCKED declaration and the word "coequal" or equivalent ("no asymmetric treatment") is present. |
| E6: Gate result fenced block | Phase 3, opening | C-17 | independent | Phase 3 carries gate result forward as first structural element before Step 3a content. The carry-forward precedes any step header or finding content. Verifiable by confirming the gate block appears at the top of Phase 3 before Step 3a begins. |
| E6: Gate result fenced block | Phase 3, opening | C-18 | independent | Gate carry-forward uses a fenced code block with `-> GATE RESULT:` structural label and a literal gate value (PASS or a defect description). No template notation (e.g., `{{value}}`). No prose wrapping. Machine-readable without parsing markdown formatting. Verifiable by confirming fenced block syntax, `-> GATE RESULT:` label, and literal value. |

**C-11 through C-23 citations**: see Phase 2.5 Role Bijection Checkpoint. Verdict cites Phase
2.5 gate result; does not re-run bijection audit (C-13 compliance).

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

**C-11: PASS** (biconditional holds).
**C-12: PASS** (compact merged table; both directions in one surface).
**C-13: PASS** (Phase 2.5 named checkpoint; Verdict cites, does not re-run).
**C-14: PASS** (relay-seeded fields present in Execute relays; three defect classes named; evidence
from relay fields -- see C-14 joint treatment in C-25 axis variations).
**C-15: PASS** (E2: Evidence source column populated per exhaustive table; each row names relay
field -- verified in element-criterion index above).
**C-16: PASS** (E3: column headers define three-value domains inline -- verified in index above).
**C-17: PASS** (E5: coequal enumeration; E6: Phase 3 location -- each independent; index above).
**C-18: PASS** (E6: fenced block with structural label -- independent from C-17; index above).
**C-19: PASS** (E2: exactly five rows, declared exhaustive -- independent property; index above).
**C-20: PASS** (E1: semantic block co-located before E3; all six values named -- index above).
**C-21: PASS** (Phase 2.5 sub-elements in declared canonical order: 1->2->3; invariant stated).
**C-22: PASS** (element-criterion index above; stable E1-E6 labels; independence noted per pair).
**C-23: PASS** (E2: self-contained table; no prose preamble; closed-world cells; index above).
**C-24: PASS** (E2 satisfies C-15/C-19/C-23 with three named non-overlapping verifiable
properties, one per criterion; "independent (N-way)" annotation on each of the three rows).

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Output format (C-25: joint satisfaction relationship type)

**Axis**: Output format -- the element-criterion index gains a Relationship column with three
named values: `sole`, `independent`, `joint`. The `joint` value is used when two or more
structural elements together satisfy a criterion that neither satisfies alone. Joint rows
identify all contributing elements, declare the criterion, and include a "neither alone"
statement that names what each element contributes and why the other element is insufficient.
The canonical joint case is C-14 (relay-seeded evidence capture): the Execute relay seeded
fields (E4) + the Role Bijection Table (E3) together satisfy C-14 and neither alone does.

**Hypothesis**: R6 V-05 Verdict uses independence notation (C-22) for pairwise cases. C-14
is satisfied by two elements together, but the Verdict does not name this relationship --
it lists C-14 under E3 or describes it in prose without declaring that E4 is a co-contributor.
A reviewer checking C-25 cannot confirm the "neither alone" property without reading the whole
Verdict. The `joint` relationship type makes this explicit in the table: the two elements appear
in a single row, the relationship is named, and the "neither alone" declaration is structurally
present. Risk: joint rows require two element names in one cell, which is wider than single-
element rows. Mitigation: the "neither alone" block is written outside the table as a two-line
declaration immediately below the joint row, keeping the table scannable.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

[Coverage Matrix, schema definitions, Direction A, Role-Schema Binding Summary, Stage 1,
Stage 2 SA-TO-SG PROMOTION, Phase 1 Setup, Phase 2 Execute, Phase 2.5 Phase 3 Findings,
Phase 4 Amend: identical to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Element-Criterion Index)

[Compliance Ledger and Direction B tables: identical to V-01.]

---

#### Element-Criterion Index (C-25 joint satisfaction relationship type)

**Reading instructions**: The Relationship column carries three values:
- `sole`: this element is the only structural contributor to this criterion.
- `independent`: this element alone satisfies this criterion; other elements may independently
  satisfy other criteria but this satisfaction does not depend on them.
- `joint`: two elements together satisfy this criterion; neither element alone suffices. The
  "neither alone" declaration follows the joint row outside the table and names what each
  element contributes and why the other is insufficient alone.

| Element | Location | Criteria ID | Relationship |
|---------|----------|-------------|--------------|
| E1: Status column semantics block | Phase 2.5, sub-element 1 of 3 | C-20 | sole |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-15 | independent |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-19 | independent |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-23 | independent |
| E3: Role Bijection Table | Phase 2.5, sub-element 3 of 3 | C-12 | independent |
| E3: Role Bijection Table | Phase 2.5, sub-element 3 of 3 | C-16 | independent |
| E3 + E4 | Phase 2.5, sub-element 3 of 3 + Phase 2 Execute, role relays | C-14 | joint |
| E5: BLOCKED language block | Phase 2.5, gate section | C-17 | independent |
| E6: Gate result fenced block | Phase 3, opening | C-17 | independent |
| E6: Gate result fenced block | Phase 3, opening | C-18 | independent |

**Neither alone -- C-14 joint declaration (E3 + E4)**:
- E3 (Role Bijection Table) alone does not satisfy C-14: the Role Bijection Table mechanism
  exists to read relay fields and detect relay-field-absent defects, but if Execute relays do
  not plant `Binding Summary row:` and `Schema-governed action:` fields, the table has no
  relay-seeded evidence to read. C-14's requirement that "C-11 evidence fields are embedded in
  each Execute relay" is unmet by E3 alone.
- E4 (Execute relay seeded fields) alone does not satisfy C-14: relay fields are planted in
  each Execute relay, but without the Role Bijection Table mechanism (E3), there is no process
  to read those fields, detect their absence as a distinct third defect class, or convert Verdict
  assembly from end-of-trace reconstruction to read-and-copy. C-14's "relay field absence as a
  distinct third defect class" requirement is unmet by E4 alone.
- Together: E4 plants `Binding Summary row:` and `Schema-governed action:` in every Execute
  relay; E3 reads those specific relay fields using the five-case algorithm and detects relay-
  field-absent as a first-class defect class coequal with SILENT and UNDECLARED. C-14 holds.

**C-11 through C-23 citations**: see Phase 2.5 Role Bijection Checkpoint.

**C-14: PASS** (joint: E3 reads relay fields planted by E4; relay-field-absent detectable as
third defect class; neither alone satisfies C-14 -- see "neither alone" declaration above).
**C-25: PASS** (joint relationship type present in element-criterion index; E3+E4 joint row
present; "neither alone" declaration names each element's contribution and states insufficiency
of each alone; joint is a second named relationship type alongside independent in this index).

[All other C-11 through C-24 and C-26 citations: identical to V-01 except C-25 PASS.]

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Output format (C-26: sub-element coordinates as Location strings)

**Axis**: Output format -- Phase 2.5 sub-element labels assigned by C-21 become the Location
string values in the element-criterion index. The C-21 sequence numbers are expressed as
compact coordinate strings: Phase 2.5 sub-element 1 of 3 = `2.5.1`; sub-element 2 of 3 =
`2.5.2`; sub-element 3 of 3 = `2.5.3`. These coordinate strings appear verbatim as Location
column values for Phase 2.5 elements. When the Verdict cites a Phase 2.5 element, it references
the coordinate (e.g., "2.5.1 satisfies C-20") not a prose description. Non-Phase-2.5 elements
(E4, E5, E6) use their phase labels as before. The two-layer navigation property: a reader
looking up C-19 finds Location = `2.5.2`; scanning the Phase 2.5 body for the sub-element
labeled `2.5.2` finds the algorithm table. Neither C-21 alone (sub-element numbers in the
prompt) nor C-22 alone (element index in the Verdict) produces this navigation; the coordinate
equivalence creates it.

**Hypothesis**: R6 V-05 has C-21 sub-element numbers in Phase 2.5 headers ("sub-element 1 of
3", "sub-element 2 of 3", "sub-element 3 of 3") and C-22 element labels in the Verdict (E1,
E2, E3 with prose Location descriptions). The Location column says "Phase 2.5, sub-element 2
of 3 -- five-case algorithm table" -- which is correct but verbose. A reviewer matching Verdict
to prompt must parse the prose location description and match it to the C-21 header. The
coordinate string `2.5.2` creates a one-to-one textual match: the Location value in the index
equals the label in the Phase 2.5 sub-element header. No prose matching required. Risk: the
coordinate string `2.5.2` is less descriptive than "Phase 2.5, sub-element 2 of 3 -- five-case
algorithm table". Mitigation: the element Name column (E2: Five-case algorithm table) provides
the human-readable description; the Location column carries only the navigation coordinate.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Identical to V-01. Coverage Matrix preamble ordering invariant updated to reflect coordinate
labels for Phase 2.5 sub-elements:]

The Phase 2.5 Role Bijection Checkpoint runs between Phase 2 Execute and Phase 3 Findings.
Its three co-located sub-elements appear in canonical order and carry coordinate labels:
sub-element `2.5.1` (status column semantics block) first, `2.5.2` (five-case algorithm table)
second, `2.5.3` (Role Bijection Table) third. Re-ordering these sub-elements is a structural
violation coequal with schema label violations. These coordinate strings are the Location values
for Phase 2.5 elements in the Verdict element-criterion index.

[All remaining Coverage Matrix content, schema definitions, Direction A, Role-Schema Binding
Summary, Stage 1, Stage 2, Phase 1 Setup, Phase 2 Execute: identical to V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint

**Sub-element ordering invariant (C-21)**: Canonical order: `2.5.1` first, `2.5.2` second,
`2.5.3` third. Coordinate labels are the authoritative Location strings for Verdict citations.

---

##### Phase 2.5 `2.5.1` -- Status Column Semantics

[Content identical to V-01 sub-element 1. Header uses coordinate `2.5.1` in place of
"sub-element 1 of 3".]

---

##### Phase 2.5 `2.5.2` -- Evidence Source Column Population

[Content identical to V-01 sub-element 2. Header uses coordinate `2.5.2`.]

---

##### Phase 2.5 `2.5.3` -- Role Bijection Table

[Content identical to V-01 sub-element 3. Header uses coordinate `2.5.3`.]

---

[Phase 3 Findings, Phase 4 Amend: identical to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Element-Criterion Index)

[Compliance Ledger and Direction B tables: identical to V-01.]

---

#### Element-Criterion Index (C-26 sub-element coordinates as Location strings)

**Reading instructions**: Location values for Phase 2.5 elements use coordinate strings
assigned by the C-21 sub-element numbering in Phase 2.5 headers (e.g., `2.5.1`, `2.5.2`,
`2.5.3`). These strings appear verbatim in both the Phase 2.5 sub-element header and this
Location column. A reviewer locates an element by finding its coordinate in the Phase 2.5
body; citations reference elements by coordinate, not by prose description.

| Element | Location | Criteria ID | Relationship | Named verifiable property (abbreviated) |
|---------|----------|-------------|--------------|----------------------------------------|
| E1: Status column semantics block | `2.5.1` | C-20 | sole | Co-located before `2.5.3`; each domain value names relay field, bijection claim, gate consequence. |
| E2: Five-case algorithm table | `2.5.2` | C-15 | independent | Each row has non-empty A Evidence source and B Evidence source cells naming relay-field strings. |
| E2: Five-case algorithm table | `2.5.2` | C-19 | independent | Table has exactly five rows; section header declares exhaustiveness. |
| E2: Five-case algorithm table | `2.5.2` | C-23 | independent | No prose before table; all cells closed-world tokens only; no parenthetical qualifiers. |
| E3: Role Bijection Table | `2.5.3` | C-12 | independent | Single table with A and B status columns and two-row biconditional hold summary. |
| E3: Role Bijection Table | `2.5.3` | C-16 | independent | Column headers define three-value domains inline: no footnote required. |
| E4: Execute relay seeded fields | Phase 2 Execute, role relays | C-14 | independent | `Binding Summary row:` and `Schema-governed action:` fields present in every relay. |
| E5: BLOCKED language block | Phase 2.5, BLOCKED section | C-17 | independent | All three class names (SILENT, UNDECLARED, relay field absent) enumerated with coequal statement. |
| E6: Gate result fenced block | Phase 3, opening | C-17 | independent | Gate carry-forward is first structural element before Step 3a content. |
| E6: Gate result fenced block | Phase 3, opening | C-18 | independent | Fenced block with `-> GATE RESULT:` label and literal gate value; no template notation. |

**Verdict citations using coordinates**:
- `2.5.1` satisfies C-20 (sole): semantic block co-located before `2.5.3`.
- `2.5.2` satisfies C-15 (independent): Evidence source cells populated per relay-field name.
- `2.5.2` satisfies C-19 (independent): exactly five rows, declared exhaustive.
- `2.5.2` satisfies C-23 (independent): self-contained, closed-world cells, no preamble.
- `2.5.3` satisfies C-12 (independent): compact merged table with biconditional hold summary.
- `2.5.3` satisfies C-16 (independent): column headers define three-value domains inline.

**C-26: PASS** (`2.5.1`, `2.5.2`, `2.5.3` coordinate strings appear verbatim in both Phase 2.5
sub-element headers and the Verdict element-criterion index Location column; Verdict citations
reference elements by coordinate -- two-layer navigation property: coordinate locates element
in prompt; criteria locates requirement in rubric; neither C-21 alone nor C-22 alone produces
this; C-26 holds when both coordinates match and citations use coordinates).

[All other C-11 through C-25 citations: identical to V-01 except C-26 PASS. C-24 is partial
in V-03 (the N-way annotation is present in element names but the Named verifiable property
column is abbreviated; a full V-01/V-04 property expansion is required for C-24 full credit).]

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: C-24 + C-25 (N-way independence + joint satisfaction)

**Axes combined**: C-24 (N-way independence with named verifiable properties per criterion,
from V-01) and C-25 (joint satisfaction relationship type with "neither alone" declaration,
from V-02). The element-criterion index carries a full Relationship column (`sole`,
`independent`, `joint`) AND a Named verifiable property column. Joint rows use the property
column for the "neither alone" declaration summary; the full "neither alone" block appears
immediately below the table as in V-02. N-way rows carry "independent (N-way)" in the
Relationship column and a distinct named property in the property column.

**Hypothesis**: V-01 achieves C-24 only; V-02 achieves C-25 only. The two mechanisms are
structurally independent: the Relationship column is a new column added alongside the Named
verifiable property column; N-way rows and joint rows can coexist in the same table. C-24
and C-25 do not interact in the element-criterion index -- N-way independence applies to one
element (E2 with three criteria), joint applies to a two-element pair (E3+E4 for C-14).
A reviewer auditing C-24 scans rows with "independent (N-way)" and checks property distinctness.
A reviewer auditing C-25 scans rows with "joint" and checks for the "neither alone" declaration.
No conflict. V-04 is a safe additive combination.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

[Coverage Matrix, schema definitions, Direction A, Role-Schema Binding Summary, Stage 1,
Stage 2, Phase 1 Setup, Phase 2 Execute, Phase 2.5, Phase 3 Findings, Phase 4 Amend:
identical to V-01.]

---

### Verdict (Phase 5 -- Closed-World Audit + Element-Criterion Index)

[Compliance Ledger and Direction B tables: identical to V-01.]

---

#### Element-Criterion Index (C-24 N-way + C-25 joint)

**Reading instructions**: Relationship values: `sole` (single contributor), `independent`
(element alone satisfies criterion; pairwise: two criteria per element with pairwise
independence notation; N-way: three or more criteria per element with "independent (N-way)"
annotation), `joint` (two or more elements together satisfy criterion; neither alone suffices;
"neither alone" block follows table). Named verifiable property column is present for all rows.
Joint rows carry a brief property summary; the full "neither alone" declaration is below.

| Element | Location | Criteria ID | Relationship | Named verifiable property |
|---------|----------|-------------|--------------|--------------------------|
| E1: Status column semantics block | Phase 2.5, sub-element 1 of 3 | C-20 | sole | Block appears before Role Bijection Table; each of six domain values (three per column) has an entry naming relay field read, bijection claim, and gate consequence. Verifiable by reading the block without consulting other sections. |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-15 | independent (N-way) | Every row carries non-empty A Evidence source and B Evidence source cells containing relay-field name strings. Check: scan any row; both source cells contain a named relay-field string (not a blank or placeholder). |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-19 | independent (N-way) | Table body contains exactly five data rows; section header declares the enumeration exhaustive. Check: count table rows; count = 5; no additional rows follow. |
| E2: Five-case algorithm table | Phase 2.5, sub-element 2 of 3 | C-23 | independent (N-way) | No prose paragraph appears between section header and table. All cells contain only closed-world tokens: present / absent / YES / SILENT / UNDECLARED / relay field absent / relay-field-name string. No parenthetical qualifiers in any cell. Check: paragraph boundaries before table; cell content types only. |
| E3: Role Bijection Table | Phase 2.5, sub-element 3 of 3 | C-12 | independent | Compact merged table carries both A: Acts in Execute and B: Declared in Summary columns; two-row biconditional hold summary follows table. Both bijection directions verified in one surface. Check: single table with both A and B status columns; two-row hold summary present. |
| E3: Role Bijection Table | Phase 2.5, sub-element 3 of 3 | C-16 | independent | Column A header defines domain {YES, SILENT, relay field absent} inline; column B header defines {YES, UNDECLARED, relay field absent} inline. All three values appear in each column header without footnote. Check: read column headers; all three domain values present per header. |
| E3 + E4: Role Bijection Table + Execute relay seeded fields | Phase 2.5, sub-element 3 of 3 + Phase 2 Execute, role relays | C-14 | joint | E3 reads relay fields planted by E4; together they satisfy relay-seeded evidence capture with third defect class. See "neither alone" declaration below. |
| E5: BLOCKED language block | Phase 2.5, gate section | C-17 | independent | All three defect class names (SILENT, UNDECLARED, relay field absent) enumerated with explicit coequal statement; no asymmetric treatment language. Check: three class names present; coequal / no-asymmetric language present. |
| E6: Gate result fenced block | Phase 3, opening | C-17 | independent | Gate carry-forward is first structural element before Step 3a; Phase 3 opening carries gate result forward. Check: gate block precedes Step 3a header and any findings content. |
| E6: Gate result fenced block | Phase 3, opening | C-18 | independent | Fenced code block with `-> GATE RESULT:` structural label; literal gate value (PASS or defect description); no template notation; no prose wrapping. Check: fenced syntax; exact label; literal value. |

**Neither alone -- C-14 joint declaration (E3 + E4)**:
- E3 (Role Bijection Table) alone does not satisfy C-14: Phase 2.5 has a mechanism to read
  relay fields and detect relay-field-absent defects, but if Execute relays do not plant
  `Binding Summary row:` and `Schema-governed action:`, the table reads nothing and no relay-
  field-absent detection occurs. C-14 requires evidence fields "embedded in each Execute relay"
  -- a requirement on Phase 2 Execute, not on Phase 2.5 alone.
- E4 (Execute relay seeded fields) alone does not satisfy C-14: relay fields are planted in
  each Execute relay, but without the Role Bijection Table mechanism (E3), there is no process
  to read those fields against the five-case algorithm or to classify relay-field-absent as a
  distinct third defect class coequal with SILENT and UNDECLARED. C-14's "relay field absence
  as a distinct third defect class" is a property of the reading mechanism, not of the seeds.
- Together: E4 plants fields; E3 reads them; relay-field-absent is detectable. C-14 holds.

**C-11 through C-23 citations**: see Phase 2.5. Verdict cites; does not re-run.

**C-24: PASS** (E2 satisfies C-15, C-19, C-23 with three named non-overlapping verifiable
properties; each row carries "independent (N-way)" annotation; properties are criterion-agnostic
observables -- any can be checked without knowing the other two criterion IDs).

**C-25: PASS** (joint relationship type present; E3+E4 joint row present; Relationship = "joint";
"neither alone" declaration below table names each element's contribution and states insufficiency
of each alone; joint is a second named relationship type not collapsible into independence).

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined: C-24 + C-25 + C-26 (complete v18 target)

**Axes combined**: All three new v18 criteria -- C-24 (N-way independence with named verifiable
properties from V-01), C-25 (joint satisfaction relationship type from V-02), C-26 (sub-element
coordinates as Location strings from V-03). V-04 architecture extended with coordinate-based
Location strings.

**Hypothesis**: C-24 and C-25 are independent additions to the element-criterion index columns.
C-26 is an independent change to the Location column values (coordinates replace prose). The
three changes do not interact: N-way notation populates the Named verifiable property column;
joint notation populates the Relationship column; coordinates populate the Location column. All
three can coexist in one table without format conflict. The resulting element-criterion index
achieves: (1) every Phase 2.5 element has a Location that can be looked up directly in the
Phase 2.5 body by coordinate; (2) multi-criterion elements carry named properties so independence
is verifiable without reading the criteria definitions; (3) multi-element criteria carry a joint
relationship type so the "neither alone" property is structurally declared. A reviewer auditing
v18 against V-05 can check C-24, C-25, and C-26 from the single element-criterion index table
plus its "neither alone" supplement. No other section of the Verdict is needed for those three
criteria.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.
A Coverage Matrix entry is valid if and only if it is referenced in at least one downstream
phase. Both directions constitute the Coverage Matrix closed-world bijection (C-10).

The Phase 2.5 Role Bijection Checkpoint runs between Phase 2 Execute and Phase 3 Findings.
Its three co-located sub-elements appear in canonical order and carry coordinate labels:
`2.5.1` (status column semantics block) first, `2.5.2` (five-case algorithm table) second,
`2.5.3` (Role Bijection Table) third. These coordinate strings are the authoritative Location
values for Phase 2.5 elements in the Verdict element-criterion index and for all Verdict
citations. Re-ordering these sub-elements is a structural violation coequal with schema label
violations. A Verdict Location string that differs from the sub-element coordinate in Phase 2.5
is a navigation defect.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Setup per-role attribution, Step 3b Source column, Execute role relay | All roles (Source labels in relay; promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments from all roles | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 checks Source diversity across all roles' Step 3b contributions | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between sub-steps) | N/A -- applies to Findings phase structure | VC-5 |

**Schema definitions** (biconditional -- violations are structural invalidity, not quality issues):

**Schema 1**: A trace is valid w.r.t. Schema 1 if and only if every severity label in any phase
uses only {P1, P2, P3}. P1 = blocks useful artifact baseline. P2 = quality improvement. P3 = advisory.

**Schema 2**: SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all phases
after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a structural violation.

**Schema 3**: A trace is valid w.r.t. Schema 3 if and only if every Phase 4 Amend entry names
a remediation channel from {spec, invocation, artifact, quality}.

**Schema 4**: G-1 invariant: Step 3b contains >=2 distinct Source types. G-2 invariant: no two
same-Source findings carry identical Action text. G-3 invariant: all Step 3b entries use only
{P1, P2, P3}.

**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >=2 entries. Step 3d
valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

| Schema | Matrix row | Referenced at (all phase/step names) | Orphan? |
|--------|-----------|--------------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend); Step 3b (enforce); Step 3c G-3 (verify); Phase 4 Amend (enforce) | NO |
| Schema 2 | Row 2 | Stage 1 audit; SA-TO-SG PROMOTION; Phase 1 per-role attribution; Step 3b Source; Execute role relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 transitions | NO |

Direction A result: all 5 rows confirmed. Direction A invariant: HOLDS.

---

### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable; or "N/A -- no EG findings"] | [Source labels; label lock if promoted] | [Schema 3/4 interactions if any] |

---

### Stage 1 -- Source-Layer Audit

Read `{{skill_spec_path}}` only. Schema 2 Source labels and Schema 1 Severity labels.

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

Relay received: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`]. Do not re-derive. Do not resolve silently.

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

After promotion: [SA remaining: `{{sa_remaining}}`], [SG from promotion: `{{sg_promoted}}`].

---

#### Phase 1 -- Setup

- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Three required seeded fields in every relay:
`Schema 2 compliance:`, `Binding Summary row:` (Direction B seed), `Schema-governed action:`
(Direction A seed). A missing seeded field must be declared explicitly.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed)
- **Schema-governed action**: [action using Schema 1 or 2 labels]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 2.5 -- Role Bijection Checkpoint

**Named inter-phase checkpoint**. Runs immediately after Phase 2 Execute. Phase 3 cannot
begin until this checkpoint produces a gate result.

**Sub-element ordering invariant (C-21)**: Canonical order: `2.5.1` first, `2.5.2` second,
`2.5.3` third. Coordinate labels are the authoritative Location strings in the Verdict
element-criterion index. Re-ordering is a structural violation coequal with schema label violations.

---

##### Phase 2.5 `2.5.1` -- Status Column Semantics

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.

- `YES` -- Relay field: `Schema-governed action:` in relay. Claim: role produced schema-governed
  action. Direction A holds. Gate consequence: no BLOCKED.
- `SILENT` -- Relay field: no Execute relay or no action field; Binding Summary entry exists.
  Claim: role declared to act but did not. Direction A violated. Gate consequence: BLOCKED.
- `relay field absent` -- Relay field: relay exists; `Schema-governed action:` absent from body.
  Claim: relay structurally incomplete; Direction A seed not planted. Gate consequence: BLOCKED.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.

- `YES` -- Relay field: `Binding Summary row:` in relay. Claim: role declared Binding Summary
  entry via relay seed. Direction B holds. Gate consequence: no BLOCKED.
- `UNDECLARED` -- Relay field: relay exists; no Binding Summary entry for this role. Claim:
  role acted without declaring intent. Direction B violated. Gate consequence: BLOCKED.
- `relay field absent` -- Relay field: relay exists; `Binding Summary row:` absent from body.
  Claim: relay structurally incomplete; Direction B seed not planted. Gate consequence: BLOCKED.

---

##### Phase 2.5 `2.5.2` -- Evidence Source Column Population

**Evidence source column population -- exhaustive five-case table (C-19/C-23)**:

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` relay field; BSR = `Binding Summary row:` relay
field; BS entry = Binding Summary entry exists for this role. Exactly five cases; no additional
cases exist. Locate the matching case; copy Evidence source strings exactly.

---

##### Phase 2.5 `2.5.3` -- Role Bijection Table

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row or ABSENT] | [step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per `2.5.2` table]; B: [per `2.5.2` table] |

Defects (any non-YES):
- SILENT: "[role] -- declared in Summary; produced no schema-governed action in Execute."
- UNDECLARED: "[role] -- acted in Execute without Binding Summary entry."
- relay field absent: "[relay] -- [field name] missing from relay."

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A | Every declared role acts: column A = YES | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B | Every acting role is declared: column B = YES | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

**Three defect classes -- coequal BLOCKED triggers**: SILENT, UNDECLARED, and relay field absent
trigger Phase 3 BLOCKED coequally. No asymmetric treatment.

If any A != YES or B != YES:
**Phase 3 BLOCKED: [classify as SILENT / UNDECLARED / relay field absent. Name the role relay
and defect. Enumerate all three defect class names explicitly. Resolve before proceeding.]**

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent).

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

##### Step 3a -- Severity Legend

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what blocks useful baseline] | Resolve before Findings close |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete -> Step 3b valid.

---

##### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.
Schema 5 transition: >=2 entries -> Step 3c valid.

---

##### Step 3c -- Enforcement Gates

**G-1**: Source types in Step 3b: [list] -- G-1: PASS / FAIL
**G-2**: Same-Source pairs with identical Action: [list or "none"] -- G-2: PASS / FAIL
**G-3**: Severity labels in Step 3b: [list] -- G-3: PASS / FAIL

If any FAIL: Phase 4 BLOCKED. Resolve, re-run, confirm PASS before proceeding.
Schema 5 transition: all-PASS -> Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 3 active: every Phase 4 Amend entry requires `[remediation channel: ...]`.
Schema 5 transition: channel active -> Phase 4 valid.

**Findings carry-forward**: [F-NN: `{{id}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active].

---

#### Phase 4 -- Amend

**Schema 4 pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`. If any FAIL: BLOCKED.

Change: [finding: `{{F-NN}}`], [source: `{{source}}`], [remediation channel: ], [section: ], [change: ]

Dismissal: [finding: `{{F-NN}}`], [reason: ], [remediation channel: ], [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Closed-World Audit + Element-Criterion Index)

#### Compliance Ledger

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what legend stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [severity values, count each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate checked | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings P1/P2/P3 only | [labels this role used] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [Source labels used] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | SA/SG/EG/QO; promoted = SG | [Source labels in Step 3b] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels valid; lock honored | [Source labels in relay] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels used; missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit results | [G-1/G-2/G-3 at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity across roles | [Source types; roles contributed] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [prerequisite evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL |

---

#### Closed-World Verification -- Direction B

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

Undeclared references: NONE. Direction B: HOLDS. **C-10: PASS.**

---

#### Element-Criterion Index (C-24 N-way + C-25 joint + C-26 coordinates)

**Reading instructions**:
- **Location**: coordinate strings from C-21 Phase 2.5 sub-element labels (`2.5.1`, `2.5.2`,
  `2.5.3`). These strings match verbatim in Phase 2.5 sub-element headers and this Location
  column. To locate an element: find the coordinate in the Phase 2.5 body. To find an element's
  criteria: look up its Location in this table.
- **Relationship**: `sole` (single contributor), `independent` (element alone satisfies criterion;
  N-way when 3+ criteria per element), `joint` (two elements together satisfy criterion; neither
  alone; see "neither alone" block below table).
- **Named verifiable property**: a criterion-agnostic observable aspect of the element that the
  corresponding criterion checks. Each property is verifiable without consulting the criterion
  definition. Properties for the same element name non-overlapping aspects.

| Element | Location | Criteria ID | Relationship | Named verifiable property |
|---------|----------|-------------|--------------|--------------------------|
| E1: Status column semantics block | `2.5.1` | C-20 | sole | Block appears immediately before `2.5.3` in Phase 2.5. Each of the six domain values (three per column) has a named entry stating: relay field read to determine this value, bijection claim the value makes, and gate consequence. Verifiable: read the block; confirm all three named fields (relay field, claim, consequence) present per value. |
| E2: Five-case algorithm table | `2.5.2` | C-15 | independent (N-way with C-19, C-23) | Every row's A Evidence source and B Evidence source cells contain relay-field name strings. Verifiable: scan any table row; both source cells are non-empty and contain a named relay-field string (not a blank, placeholder, or generic term). |
| E2: Five-case algorithm table | `2.5.2` | C-19 | independent (N-way with C-15, C-23) | Table contains exactly five data rows; section header at `2.5.2` declares the enumeration exhaustive. Verifiable: count data rows in the table; count equals 5; no additional rows exist; exhaustiveness claim present in section header. |
| E2: Five-case algorithm table | `2.5.2` | C-23 | independent (N-way with C-15, C-19) | No prose paragraph appears between the `2.5.2` section header and the table body. All cells contain only closed-world tokens: present / absent / YES / SILENT / UNDECLARED / relay field absent / relay-field-name string. No parenthetical qualifiers appear in any cell. Verifiable: check for paragraph boundaries before table; scan every cell for non-token content. |
| E3: Role Bijection Table | `2.5.3` | C-12 | independent | Single table carries both A: Acts in Execute and B: Declared in Summary status columns; two-row biconditional hold summary follows immediately. Both bijection directions verified in one surface. Verifiable: confirm single table with both A and B columns; confirm two-row hold summary with Direction A and Direction B rows. |
| E3: Role Bijection Table | `2.5.3` | C-16 | independent | Column A header defines domain {YES, SILENT, relay field absent} inline; column B header defines {YES, UNDECLARED, relay field absent} inline. All three values for each column appear in the header without footnote or supplementary block. Verifiable: read column headers only; confirm all three domain values spelled out per header. |
| E3 + E4: Role Bijection Table + Execute relay seeded fields | `2.5.3` + Phase 2 Execute, role relays | C-14 | joint -- neither alone | See "neither alone" declaration below. |
| E5: BLOCKED language block | Phase 2.5, BLOCKED section | C-17 | independent | BLOCKED block names all three defect classes (SILENT, UNDECLARED, relay field absent) and explicitly states coequal treatment with no asymmetric treatment language. Verifiable: confirm all three class names appear in the BLOCKED declaration; confirm coequal / no-asymmetric statement present. |
| E6: Gate result fenced block | Phase 3, opening | C-17 | independent | Gate carry-forward block is the first structural element in Phase 3, appearing before the Step 3a header and any findings content. Verifiable: confirm gate block precedes Step 3a; no findings content between Phase 3 header and gate block. |
| E6: Gate result fenced block | Phase 3, opening | C-18 | independent | Gate block uses fenced code block syntax with `-> GATE RESULT:` structural label and a literal gate value (PASS or defect description). No template notation (no `{{...}}`). No prose wrapping outside the fence. Verifiable: confirm fenced block syntax; confirm `-> GATE RESULT:` label present; confirm literal value (not a template variable). |

**Neither alone -- C-14 joint declaration (E3 + E4)**:
- **E3 alone is insufficient**: The Role Bijection Table (`2.5.3`) provides a mechanism to read
  relay fields and detect relay-field-absent defects -- but only if those fields were planted in
  Phase 2 Execute relays. If Execute relays do not include `Binding Summary row:` and
  `Schema-governed action:`, Phase 2.5 reads nothing and relay-field-absent detection does not
  occur. C-14's requirement "C-11 evidence fields embedded in each Execute relay" is a property
  of Phase 2 Execute, not of Phase 2.5. E3 alone cannot satisfy this requirement.
- **E4 alone is insufficient**: Execute relays plant `Binding Summary row:` and
  `Schema-governed action:` in each role relay -- but without the Role Bijection Table mechanism
  (E3 at `2.5.3`), there is no process to read those fields against the five-case algorithm,
  classify relay-field-absent as a third defect class coequal with SILENT and UNDECLARED, or
  convert Verdict assembly from end-of-trace reconstruction to read-and-copy. C-14's
  "relay field absence as a distinct third defect class" is a detection property requiring a
  reading mechanism. E4 alone cannot satisfy this requirement.
- **Together**: E4 plants the fields; E3 reads them and detects field absence as a first-class
  defect. C-14 holds when both elements are present.

**C-11 through C-23 citations**: see Phase 2.5 Role Bijection Checkpoint. Verdict cites;
does not re-run (C-13 compliance).

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

**C-11: PASS** (biconditional invariant holds; both directions HOLDS, no defects).
**C-12: PASS** (compact merged table at `2.5.3`; both A and B status columns; biconditional
hold summary; both directions in one surface).
**C-13: PASS** (Phase 2.5 named inter-phase checkpoint present; BLOCKED language on failure;
Verdict cites Phase 2.5 result without re-running bijection audit).
**C-14: PASS** (joint: E3 at `2.5.3` reads relay fields planted by E4 in Phase 2 Execute;
relay-field-absent detectable as third defect class coequal with SILENT and UNDECLARED; neither
element alone satisfies C-14 -- see "neither alone" declaration above).
**C-15: PASS** (E2 at `2.5.2`: Evidence source column populated per `2.5.2` algorithm table;
each row names relay fields in both A and B Evidence source cells; independently verifiable
property per index above).
**C-16: PASS** (E3 at `2.5.3`: column headers define three-value domains inline; independently
verifiable without footnote; property per index above).
**C-17: PASS** (E5: BLOCKED block enumerates all three defect classes with coequal statement --
independently verifiable; E6: Phase 3 gate carry-forward as first structural element before
Step 3a -- independently verifiable; each contributes a distinct C-17 aspect independently).
**C-18: PASS** (E6 at Phase 3 opening: fenced code block with `-> GATE RESULT:` label; literal
gate value; no template notation; independently verifiable from C-17 Phase 3 location aspect).
**C-19: PASS** (E2 at `2.5.2`: exactly five rows; section header declares exhaustiveness;
independently verifiable property per index above -- distinct from C-15 and C-23 properties).
**C-20: PASS** (E1 at `2.5.1`: semantic block co-located before `2.5.3`; each domain value
entry names relay field, bijection claim, gate consequence; independently auditable per index).
**C-21: PASS** (Phase 2.5 sub-elements appear in canonical order `2.5.1` -> `2.5.2` -> `2.5.3`
as declared in Coverage Matrix preamble; ordering invariant stated; re-ordering is structural
violation; sequence-number coordinate labels assigned to each sub-element).
**C-22: PASS** (element-criterion index carries stable E1-E6 labels; Relationship column
present; independence noted per criterion pair; pairwise independence (E6: C-17+C-18) and
N-way independence (E2: C-15+C-19+C-23) both represented; Verdict criterion citations reference
element labels).
**C-23: PASS** (E2 at `2.5.2`: self-contained five-case table; no prose paragraph before table;
all cells closed-world tokens; no parenthetical qualifiers; independently verifiable property
per index above -- distinct from C-15 and C-19 properties).
**C-24: PASS** (E2 at `2.5.2` satisfies C-15, C-19, and C-23 independently (N-way); three
named non-overlapping verifiable properties: C-15 checks evidence source cell population (relay-
field strings present); C-19 checks row count and exhaustiveness claim (exactly 5 rows); C-23
checks self-contained format (no preamble, closed-world cells, no qualifiers); each property
is verifiable without consulting the other two; "independent (N-way)" annotation on each of
the three rows in the index).
**C-25: PASS** (joint relationship type present in element-criterion index as a second named
relationship type alongside independent; E3+E4 joint row present with Relationship = "joint";
"neither alone" declaration below table names each element's contribution and states why each
is insufficient alone; joint is not collapsible into independence: independence means one
element alone satisfies; joint means neither alone does).
**C-26: PASS** (coordinate strings `2.5.1`, `2.5.2`, `2.5.3` from C-21 Phase 2.5 sub-element
headers appear verbatim as Location column values in the element-criterion index; Verdict
criterion citations reference Phase 2.5 elements by coordinate ("`2.5.2` satisfies C-15
independently", "`2.5.3` satisfies C-12 independently"); two-layer navigation: coordinate
locates element in prompt body; criteria ID locates requirement in rubric; neither C-21 alone
(numbers in prompt but not in Verdict) nor C-22 alone (Verdict index but prose Locations)
produces this cross-reference property).

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
