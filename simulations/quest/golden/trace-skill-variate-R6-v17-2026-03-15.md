---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 6
rubric: trace-skill-rubric-v17-2026-03-15.md
---

# trace-skill -- Variations v17 R6 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R5 V-05 achieves C-01 through C-20 PASS under v16 scoring. v17 formalizes three
new aspirational criteria from R5 excellence signals: C-21 (canonical Phase 2.5 sub-element
ordering declared as a formal invariant -- semantic block first, algorithm table second, Role
Bijection Table third), C-22 (Verdict criterion tracking with independence notation -- where one
structural element satisfies two criteria independently, the independence is stated explicitly),
C-23 (algorithm table as self-contained population rule -- no prose preamble, no parenthetical
annotations within cells, no supplementary notes -- pure table-lookup, zero inference burden).

**R5 V-05 C-21/C-22/C-23 state** (scored against v17):

- C-21: R5 V-05 Phase 2.5 ordering is observably semantics -> algorithm -> table (semantic block
  appears before five-case table, which appears before Role Bijection Table). The C-20 Verdict
  note mentions "semantics block ordered before five-case algorithm -- semantics -> algorithm ->
  table" in passing. However, the ordering is not declared as a formal invariant anywhere in the
  prompt -- no rule states that re-ordering these elements is a structural violation, and no
  Coverage Matrix preamble encodes the ordering as a protocol constraint. An implementer cannot
  distinguish deliberate ordering from incidental arrangement. C-21 = PARTIAL.

- C-22: R5 V-05 Verdict C-18 note contains "satisfies C-17 location requirement and C-18 format
  requirement independently" -- the independence notation IS present for the C-17/C-18 pair. But
  C-22 requires broader coverage: the Verdict must systematically name which structural element
  satisfies which criteria by ID for all multi-criterion-satisfying elements, not only document
  one case. Additionally, C-22 requires the structural elements themselves to be identified by
  name/label so the criterion-to-element mapping is traceable. R5 V-05 Verdict describes elements
  in prose ("Phase 3 gate carry-forward appears as fenced code block") but does not assign them
  stable element labels. C-22 = PARTIAL.

- C-23: R5 V-05 five-case closed table contains: (1) prose preamble before the table ("This
  table is exhaustive: exactly five cases cover..."); (2) parenthetical annotations within cells:
  `N/A -- no relay` (relay-present column, SILENT row), `YES (in Binding Summary)` (BSR-present
  column, SILENT row), `NO -- field missing` (BSR-present column, relay-absent-B row), `NO -- no
  Binding Summary entry` (BSR-present column, UNDECLARED row); (3) the `Binding Summary row:`
  present? column conflates two distinct relay states (field physically absent vs. no BS entry),
  requiring the reader to parse parenthetical qualifiers to distinguish them -- inference burden
  persists. C-23 = PARTIAL.

**v17 R6 variation axes**:

- **Output format (C-23)**: Five-case closed table restructured as pure table-lookup (V-01) --
  prose preamble removed; a `BS entry` column added to cleanly separate relay-absent-B from
  UNDECLARED without annotations; all cells contain only closed-world values: present/absent/YES/
  SILENT/UNDECLARED/relay-field-absent/exact-string; no inline qualifiers; exhaustiveness declared
  as table section label, not prose preamble.

- **Lifecycle emphasis (C-21)**: Canonical Phase 2.5 sub-element ordering declared as a formal
  protocol invariant (V-02) -- Coverage Matrix preamble encodes the ordering constraint; Phase 2.5
  opens with a labeled ordering declaration; the three elements carry sequence numbers; a violation
  note states that re-ordering is a structural violation coequal with schema label violations.

- **Output format (C-22)**: Verdict criterion tracking restructured with named elements and
  independence notation (V-03) -- each multi-criterion structural element receives a stable label
  (e.g., `[E1: fenced gate block]`); Verdict per-criterion PASS statements are reorganized into
  an element-first table that maps element -> criteria satisfied -> independence noted where
  applicable.

**Combined variations**:
- V-04: C-21 + C-23 (canonical ordering invariant + pure table-lookup algorithm table)
- V-05: C-21 + C-22 + C-23 (all three new criteria -- complete v17 target)

All five inherit the full R5 V-05 architecture (C-01 through C-20 PASS). What varies per V-0N:
only the C-21/C-22/C-23 structural mechanisms.

---

## V-01 -- Single axis: Output format (C-23: algorithm table as pure table-lookup)

**Axis**: Output format -- the five-case Evidence source column population table is restructured
to stand alone with zero inference burden. Three changes: (1) prose preamble before the table is
removed; exhaustiveness is declared in the table section header, not in a paragraph before it.
(2) A `BS entry` column is added, splitting the former `Binding Summary row: present?` column
into two dimensions: whether the `Binding Summary row:` field is physically present in the relay,
and whether a Binding Summary entry exists for this role. This eliminates the ambiguity between
relay-absent-B (field missing, BS entry exists) and UNDECLARED (field may be present, BS entry
absent) without annotations. (3) All cell values become closed-world: present/absent replaces
`N/A -- no relay`, `YES (in Binding Summary)`, `NO -- field missing`, `NO -- no Binding Summary
entry`; no inline qualifiers, no parenthetical explanations.

**Hypothesis**: R5 V-05's C-19 table earned PARTIAL because parenthetical qualifiers in cells
require the reader to infer meaning: `YES (in Binding Summary)` requires knowing why the source
differs from the standard case; `NO -- field missing` requires knowing the distinction from `NO
-- no Binding Summary entry`. Splitting into four pure-state input columns (Execute relay /
SGA field / BSR field / BS entry) makes every row independently readable: the reader scans four
present/absent values left-to-right and maps directly to status and evidence source cells. No
qualifier parsing required. Risk: nine-column table is wider in markdown; but each column value
is either `present`, `absent`, a status value, or an exact string -- rendering width is the
only cost, and the zero-inference gain outweighs it. The exhaustiveness claim moves to the table
header: "**Evidence source column population -- exhaustive five-case table (C-19/C-23)**" signals
closed-world without a prose paragraph.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

A Coverage Matrix entry is valid if and only if the schema it registers is referenced in at
least one downstream phase. A schema referenced in any phase is valid if and only if it appears
in the Coverage Matrix. Both directions constitute the Coverage Matrix closed-world bijection
(C-10), verified by Direction A enumeration (below) and Direction B assembly (Verdict).

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded in Phase 2 relays (`Binding Summary row:` Direction B seed;
`Schema-governed action:` Direction A seed). Assembled into compact merged Role Bijection Table
at Phase 2.5 -- each row carries an Evidence source column populated by the exhaustive five-case
table algorithm (C-15/C-19/C-23): four state columns (Execute relay / SGA field / BSR field /
BS entry) map to status and exact Evidence source string with no inference required. Status
columns A and B carry formal three-value domain definitions: A in {YES, SILENT, relay field
absent}; B in {YES, UNDECLARED, relay field absent} -- all three values inline in status cells,
no annotation (C-16). The table is preceded by a co-located semantic block explaining provenance,
domain boundary, and behavior consequence per domain value (C-20). Three defect classes trigger
Phase 3 BLOCKED coequal: SILENT, UNDECLARED, relay field absent -- no asymmetric treatment
(C-17). Phase 3 opens with fenced structural labeled block -- literal gate value, machine-readable
(C-18). Verdict cites Phase 2.5 result only; does not re-run.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema definitions** (biconditional form -- violations are structural invalidity, not quality
issues):

**Schema 1**: A trace is valid w.r.t. Schema 1 if and only if every severity label in any phase
uses only {P1, P2, P3}. P1 = blocks useful baseline. P2 = quality improvement. P3 = advisory.

**Schema 2**: The SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all
phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a structural violation.

**Schema 3**: A trace is valid w.r.t. Schema 3 if and only if every Phase 4 Amend entry names
a remediation channel from {spec, invocation, artifact, quality}.

**Schema 4**: G-1 invariant: Step 3b contains >=2 distinct Source types. G-2 invariant: no two
same-Source findings carry identical Action text. G-3 invariant: all Step 3b entries use only
{P1, P2, P3}.

**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >=2 entries. Step
3d valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

---

### Closed-World Verification -- Direction A (Coverage Matrix -> Phases)

**Invariant**: Schema X is in the Coverage Matrix if and only if it is referenced by at least
one execution phase. Direction A enumerates the forward mapping.

| Schema | Matrix row | Referenced at (enumerate all phase/step names) | Orphan? |
|--------|-----------|------------------------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend declared); Step 3b (P1/P2/P3 enforced); Step 3c G-3 (verified); Phase 4 Amend (enforced) | NO |
| Schema 2 | Row 2 | Stage 1 audit; SA-TO-SG PROMOTION; Step 3b Source column; Execute role relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (gate status confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 transitions | NO |

Direction A result: all 5 rows confirmed. Direction A invariant: HOLDS.

---

### Role-Schema Binding Summary

A valid trace declares every role that will appear in Phase 2 Execute before Stage 2 begins.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role] | [severity labels applicable, or "N/A -- produces no EG findings"] | [Source labels; label lock rules for promoted gaps] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}` and produces a gap audit table using Schema 2
Source labels and Schema 1 Severity labels.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay to Stage 2: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: PASS (>=2 distinct source types) / FAIL].

**Schema footprint -- Stage 1**: Schema 2 (Source labels in audit table), Schema 1 (Severity
labels).

---

### Stage 2 -- Hand-Compilation

Stage 2 receives relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [layer diversity: `{{status}}`].
All gaps carried forward without re-deriving or silently resolving.

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

**Schema footprint -- SA-TO-SG PROMOTION**: Schema 2 (promotion labels SA->SG evaluated).

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

```
[role: {{name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

Setup carry-forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

**Schema footprint -- Phase 1 Setup**: Schema 1 (binding declared per role), Schema 2
(bindings and promoted labels confirmed).

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Three required fields in every relay: Schema 2
compliance, `Binding Summary row:` (Direction B seed), `Schema-governed action:` (Direction A
seed). A relay missing either seeded field must declare the absence -- Phase 2.5 reads the
relay and detects relay field absent defects.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index] (Direction B seed)
- **Schema-governed action**: [action using Schema 1 or 2 labels per Binding Summary declaration]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps: [EG-NN list or "none"]

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in role relays), Schema 1
(Severity labels on EG findings per role).

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-23 axis: pure table-lookup algorithm table)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions -- none is subordinate to or deferred
relative to the others.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary entry for this role. BLOCKED
   immediately.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace
reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

**Role Bijection Table -- status column semantics (C-20)**:

The following block explains the meaning of each domain value per status column. Read this block
to independently audit any status cell in the table: each entry names the relay field read, the
bijection claim the value makes, and the behavior consequence at the Phase 2.5 gate.

Column A -- `A: Acts in Execute`:
- `YES` -- Relay field read: `Schema-governed action:` field in Execute relay. Claim: this role
  produced a schema-governed action matching its Binding Summary declaration. Bijection direction A
  holds for this row. Gate consequence: no BLOCKED contribution from column A.
- `SILENT` -- Relay field read: no Execute relay found (or relay carries no action field). Binding
  Summary entry exists. Claim: this role was declared to act but produced no schema-governed action.
  Bijection direction A violated. Gate consequence: BLOCKED -- coequal with UNDECLARED and relay
  field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Schema-governed action:` field
  is absent from the relay body. Claim: the relay exists but is structurally incomplete -- the
  Direction A seed was not planted. Bijection direction A indeterminate. Gate consequence: BLOCKED
  -- coequal with SILENT and UNDECLARED.

Column B -- `B: Declared in Summary`:
- `YES` -- Relay field read: `Binding Summary row:` field in Execute relay. Claim: this role
  declared its Binding Summary entry via the relay seed. Bijection direction B holds for this row.
  Gate consequence: no BLOCKED contribution from column B.
- `UNDECLARED` -- Relay field read: Execute relay exists; no Binding Summary entry for this role.
  Claim: this role produced a schema-governed action without declaring intent in the Binding Summary.
  Bijection direction B violated. Gate consequence: BLOCKED -- coequal with SILENT and relay field
  absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Binding Summary row:` field is
  absent from the relay body. Claim: the relay exists but is structurally incomplete -- the
  Direction B seed was not planted. Bijection direction B indeterminate. Gate consequence: BLOCKED
  -- coequal with SILENT and UNDECLARED.

**Evidence source column population -- exhaustive five-case table (C-19/C-23)**:

Four state columns determine the case. Values: `present` or `absent`. Exactly five cases; no
additional cases exist. Locate the matching row; copy the A Evidence source and B Evidence source
values exactly into the Evidence source column.

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` field in relay; BSR = `Binding Summary row:` field
in relay; BS entry = Binding Summary entry exists for this role.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column from exhaustive five-case table -- C-15/C-19/C-23; three-value status column domains
-- C-16; semantic block above -- C-20):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table -- C-12):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per exhaustive
five-case table, no relay fields absent).

**BLOCKED language (C-17 unified -- all three defect classes enumerated explicitly)**:

If any A != YES or B != YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

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
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what the legend stated] | PASS / FAIL |
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
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity verified across all roles | [Source types present; roles contributed each] | PASS / FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b waited for Step 3a | [prerequisite evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c waited for Step 3b | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d waited for Step 3c | [transition evidence] | PASS / FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 waited for Step 3d | [transition evidence] | PASS / FAIL |

---

#### Closed-World Verification -- Direction B (Phases -> Coverage Matrix)

Assembled from per-phase Schema footprint records.

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

#### C-11 through C-20 + C-23 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section is FAIL for C-13.

**C-11 through C-20 and C-23 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no defects).
**C-12: PASS** (compact merged table with SILENT/UNDECLARED status columns and named biconditional
hold summary at Phase 2.5; no separate direction tables).
**C-13: PASS** (Phase 2.5 named checkpoint present; BLOCKED language used on failure; Verdict
cites, does not re-run).
**C-14: PASS** (relay-seeded fields `Binding Summary row:` and `Schema-governed action:` present
in every Execute relay; three defect classes -- SILENT, UNDECLARED, relay field absent -- named
and distinguished; evidence explicitly sourced to relay fields).
**C-15: PASS** (compact merged Role Bijection Table carries Evidence source column per row; each
row names the relay field(s) from which Direction A and Direction B status values were read;
populated at Phase 2.5 directly from relay field names -- no end-of-trace reconstruction).
**C-16: PASS** (status columns A and B carry formal three-value domain {YES, SILENT/UNDECLARED,
relay field absent} in column definition; all three values inline in status cells -- no annotation,
footnote, or separate column).
**C-17: PASS** (relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED
-- explicit coequal statement present at Phase 2.5; BLOCKED message enumerates all three defect
classes explicitly with prescribed format; Phase 3 carries gate result forward as structural
`-> GATE RESULT:` element in opening before findings content begins).
**C-18: PASS** (Phase 3 gate carry-forward appears as fenced code block `-> GATE RESULT: Phase
2.5 Role Bijection Checkpoint = PASS.` -- literal gate value, no template notation, no prose
wrapping; first structural item before any step content; gate status machine-readable without
parsing markdown formatting or template variables; satisfies C-17 location requirement and C-18
format requirement independently).
**C-19: PASS** (Evidence source column population algorithm expressed as exhaustive five-case
table at Phase 2.5; four pure state columns -- Execute relay / SGA field / BSR field / BS entry
-- map to status and evidence source with no inference required; five cases declared exhaustive
in table section header; population rule is pure table-lookup).
**C-20: PASS** (pre-table semantic block co-located immediately before Role Bijection Table;
each domain value in columns A and B has an entry naming: relay field read to determine status,
bijection claim made by the value, bijection direction consequence, and gate behavior consequence;
block enables independent auditability of provenance, domain boundary, and behavior without
consulting other sections).
**C-23: PASS** (exhaustive five-case table stands alone -- no prose preamble before table; all
cells contain closed-world values only: present/absent/YES/SILENT/UNDECLARED/relay-field-absent/
exact-string; no parenthetical annotations within cells; no supplementary notes after table; BS
entry column added to cleanly separate relay-absent-B from UNDECLARED without cell qualifiers;
population rule is pure table-lookup with zero inference burden).

The biconditional invariant -- Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute -- is found to hold: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (C-21: canonical Phase 2.5 sub-element ordering declared as formal invariant)

**Axis**: Lifecycle emphasis -- the ordering of Phase 2.5's three co-located sub-elements is
elevated from observed arrangement to formal protocol invariant. Three changes: (1) The Coverage
Matrix preamble explicitly names the ordering constraint: semantic block (C-20) -> algorithm
table (C-19) -> Role Bijection Table (C-12) is the canonical sequence; re-ordering these elements
is a structural violation coequal with schema label violations. (2) Phase 2.5 opens with a
labeled ordering declaration that assigns sequence numbers to each sub-element (sub-element 1:
semantic block; sub-element 2: algorithm table; sub-element 3: Role Bijection Table), so a reader
scanning top-to-bottom never needs to backtrack to find a referenced element. (3) Each sub-element
header within Phase 2.5 carries its sequence number: "Phase 2.5 sub-element 1 of 3 -- Status
Column Semantics (C-20)", etc.

**Hypothesis**: R5 V-05 ordering is present but undeclared. An implementer building from this
prompt could re-order Phase 2.5 sub-elements (e.g., put the algorithm table before the semantic
block) without violating any stated rule. C-21 closes this gap: the ordering is a constraint,
not a convention. The sequence-numbered sub-element headers also make Phase 2.5's internal
structure navigable -- a reader encountering sub-element 3 knows sub-elements 1 and 2 precede
it and can locate them by scanning upward. Risk: adding sequence numbers to every sub-element
header increases visual noise; but the payoff (unambiguous canonical order) is worth it because
Phase 2.5 is the highest-density section in the prompt -- reader orientation matters most here.

[Phase 2.5 content differs from V-01 on the ordering invariant and sub-element headers. All
other sections (Coverage Matrix preamble note, Phase 1, Phase 2, Phase 3, Phase 4, Verdict) are
the same as V-01 except C-21 replaces C-23 in the Verdict citation section.]

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix table and schema definitions as V-01. Coverage Matrix preamble paragraph
2 updated for C-21:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded in Phase 2 relays (`Binding Summary row:` Direction B seed;
`Schema-governed action:` Direction A seed). Assembled into compact merged Role Bijection Table
at Phase 2.5 -- each row carries an Evidence source column populated by five-case closed table
algorithm (C-15/C-19). Status columns A and B carry three-value domain definitions: A in {YES,
SILENT, relay field absent}; B in {YES, UNDECLARED, relay field absent} -- inline in status
cells, no annotation (C-16). Phase 2.5 contains three co-located sub-elements in canonical
fixed order: (1) status column semantics block (C-20), (2) Evidence source column population
algorithm table (C-19), (3) Role Bijection Table (C-12). This ordering is a formal invariant --
re-ordering these sub-elements is a structural violation. Three defect classes trigger Phase 3
BLOCKED coequal: SILENT, UNDECLARED, relay field absent (C-17). Phase 3 opens with fenced
structural labeled block -- literal gate value, machine-readable (C-18). Verdict cites Phase 2.5
result only.

[Schema table, schema definitions, sub-step ordering table: same as V-01.]

---

[Direction A, Role-Schema Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup, Phase 2
Execute: same as V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-21 axis: canonical sub-element ordering as formal invariant)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Canonical sub-element ordering (C-21)**:

This checkpoint contains exactly three co-located sub-elements. They appear in the following
fixed canonical order. Re-ordering is a structural violation:

1. Sub-element 1 of 3: Status column semantics block (C-20) -- explains provenance, bijection
   claim, and gate consequence per domain value per column.
2. Sub-element 2 of 3: Evidence source column population algorithm table (C-19) -- five-case
   closed table mapping relay/field state to status and evidence source values.
3. Sub-element 3 of 3: Role Bijection Table (C-12) -- compact merged table with biconditional
   hold summary.

A reader scanning top-to-bottom encounters sub-elements in dependency order: semantics before
algorithm, algorithm before table. No forward reference or backtracking required.

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions -- none is subordinate to or deferred
relative to the others.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. BLOCKED immediately.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace
reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate status cells directly -- no annotation, footnote, or separate column.

**Phase 2.5 sub-element 1 of 3 -- Status Column Semantics (C-20)**:

The following block explains the meaning of each domain value per status column. Read this block
to independently audit any status cell in the table: each entry names the relay field read, the
bijection claim the value makes, and the behavior consequence at the Phase 2.5 gate.

Column A -- `A: Acts in Execute`:
- `YES` -- Relay field read: `Schema-governed action:` in Execute relay. Claim: role produced a
  schema-governed action matching its Binding Summary declaration. Direction A holds for this row.
  Gate consequence: no BLOCKED contribution from column A.
- `SILENT` -- Relay field read: no Execute relay found (or relay carries no action field). Binding
  Summary entry exists. Claim: role was declared to act but produced no schema-governed action.
  Direction A violated. Gate consequence: BLOCKED -- coequal with UNDECLARED and relay field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Schema-governed action:` field
  absent from relay body. Claim: relay exists but is structurally incomplete -- Direction A seed
  not planted. Direction A indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and
  UNDECLARED.

Column B -- `B: Declared in Summary`:
- `YES` -- Relay field read: `Binding Summary row:` in Execute relay. Claim: role declared its
  Binding Summary entry via the relay seed. Direction B holds for this row. Gate consequence: no
  BLOCKED contribution from column B.
- `UNDECLARED` -- Relay field read: Execute relay exists; no Binding Summary entry for this role.
  Claim: role produced a schema-governed action without declaring intent. Direction B violated.
  Gate consequence: BLOCKED -- coequal with SILENT and relay field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Binding Summary row:` field
  absent from relay body. Claim: relay exists but is structurally incomplete -- Direction B seed
  not planted. Direction B indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and
  UNDECLARED.

**Phase 2.5 sub-element 2 of 3 -- Evidence Source Column Population Algorithm (C-19)**:

This table is exhaustive: exactly five cases cover the complete space of relay/field state
combinations. No additional cases exist. Populate the Evidence source column by finding the
matching row and copying the A Evidence source and B Evidence source cell content exactly.

| Case | Relay present? | `Schema-governed action:` present? | `Binding Summary row:` present? | A status | B status | A Evidence source (exact cell content) | B Evidence source (exact cell content) |
|------|---------------|-------------------------------------|----------------------------------|----------|----------|----------------------------------------|----------------------------------------|
| Standard | YES | YES | YES | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | NO | N/A -- no relay | YES (in Binding Summary) | SILENT | YES | `no relay (Binding Summary declares absent)` | `Binding Summary row:` relay field |
| Relay field absent (A) | YES | NO -- field missing | YES | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| Relay field absent (B) | YES | YES | NO -- field missing | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | YES | YES | NO -- no Binding Summary entry | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary row` |

**Phase 2.5 sub-element 3 of 3 -- Role Bijection Table (C-12)**:

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

(compact merged -- C-12; relay-assembled -- C-14; Evidence source column from five-case table
-- C-15/C-19; three-value status column domains -- C-16; semantic block sub-element 1 above
-- C-20; canonical ordering sub-elements 1->2->3 -- C-21):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table -- C-12):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per five-case
table, no relay fields absent, canonical sub-element ordering held: semantics -> algorithm ->
table).

**BLOCKED language (C-17 unified -- all three defect classes enumerated explicitly)**:

If any A != YES or B != YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

[Same Phase 3 Steps 3a/3b/3c/3d with Schema footprints as V-01.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### C-11 through C-20 + C-21 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run.

**C-11 through C-20 and C-21 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no defects).
**C-12: PASS** (compact merged table with SILENT/UNDECLARED status columns and named biconditional
hold summary at Phase 2.5; no separate direction tables).
**C-13: PASS** (Phase 2.5 named checkpoint present; BLOCKED language used on failure; Verdict
cites, does not re-run).
**C-14: PASS** (relay-seeded fields present; three defect classes named and distinguished;
evidence sourced to relay fields).
**C-15: PASS** (Evidence source column per row naming relay fields; populated at Phase 2.5 --
no reconstruction).
**C-16: PASS** (three-value status column domains inline; all three values in status cells -- no
annotation or separate column).
**C-17: PASS** (relay field absent BLOCKED coequal; BLOCKED message enumerates all three classes;
Phase 3 carries gate result forward as structural `-> GATE RESULT:` element in opening).
**C-18: PASS** (Phase 3 gate carry-forward as fenced code block with literal gate value; first
structural item before any step content; machine-readable without parsing markdown or templates;
satisfies C-17 location requirement and C-18 format requirement independently).
**C-19: PASS** (Evidence source column population expressed as five-case closed table; each row
names relay state, field state, status, and exact evidence source cell content; five cases
exhaustive; population rule is table-lookup).
**C-20: PASS** (pre-table semantic block co-located before Role Bijection Table; each domain
value names relay field read, bijection claim, direction consequence, and gate behavior; enables
independent auditability without consulting other sections).
**C-21: PASS** (Phase 2.5 canonical sub-element ordering declared as formal invariant in Coverage
Matrix preamble and in Phase 2.5 ordering declaration block: sub-element 1 = semantic block
(C-20), sub-element 2 = algorithm table (C-19), sub-element 3 = Role Bijection Table (C-12);
each sub-element header carries sequence number; ordering stated as structural violation if not
followed; top-to-bottom comprehension enabled without backtracking).

The biconditional invariant holds: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Output format (C-22: Verdict criterion tracking with named elements and independence notation)

**Axis**: Output format -- the Verdict's per-criterion citation section is restructured from a
flat list of per-criterion PASS statements into an element-first citation table. Each structural
element in the trace that satisfies one or more criteria is assigned a stable label (e.g.,
`[E1: fenced gate block]`, `[E2: five-case algorithm table]`, `[E3: semantic block]`,
`[E4: Role Bijection Table]`). The citation table maps element -> criteria satisfied -> evidence
-> where two criteria are satisfied independently by one element, the independence is stated
explicitly with the property each criterion requires. An element index precedes the table to
make element labels findable.

**Hypothesis**: R5 V-05 Verdict per-criterion PASS statements describe elements in prose without
stable labels -- "Phase 3 gate carry-forward appears as fenced code block" cannot be
cross-referenced without re-reading. The independence notation for C-17/C-18 is present but
occurs only in the C-18 line, making it easy to miss. C-22 restructures the Verdict to be
element-centric: a reader interested in element E1 looks up E1 in the table and sees all criteria
it satisfies at once; a reader interested in C-18 sees which element satisfies it and the
independence claim. Risk: element-first organization is a different reading pattern than
criterion-first; the rubric compliance ledger (VC-1 through VC-5) remains criterion-first, so
the Verdict has two parallel views. This is a feature, not a bug: the compliance ledger covers
schema adherence; the element-criterion table covers architectural criteria.

[All phases same as V-01 except the Verdict C-11/C-20 citation section, which uses the element-
first table with independence notation.]

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

[Same Coverage Matrix, Direction A, Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1,
Phase 2, Phase 2.5, Phase 3, Phase 4 as V-01. Phase 2.5 uses V-01's five-case table with
four-column state input (C-23 axis) and C-20 semantic block. Phase 3 opens with fenced gate
block (C-18).]

---

### Verdict (Phase 5 -- Compliance Ledger + Bijection Enumerations)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### Structural Element Index

The following elements are referenced in the criterion citation table below. Labels are stable
within this trace.

| Element label | Description | Location |
|---------------|-------------|---------|
| E1 | Fenced `-> GATE RESULT:` block | Phase 3, first structural item |
| E2 | Exhaustive five-case Evidence source population table | Phase 2.5, between semantic block and Role Bijection Table |
| E3 | Status column semantics block | Phase 2.5, before E2 |
| E4 | Compact merged Role Bijection Table with biconditional hold summary | Phase 2.5, after E2 |
| E5 | Relay-seeded `Binding Summary row:` and `Schema-governed action:` fields | Phase 2 Execute relays |

---

#### C-11 through C-20 + C-22 Citation (element-first)

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
Verdict cites Phase 2.5 gate result; does not re-run. A bijection audit in this section only is
FAIL for C-13.

**Bijection gate summary (cited from Phase 2.5)**:

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**Element-criterion citation table (C-22)**:

| Element | Criteria satisfied | Evidence | Independence note |
|---------|--------------------|----------|-------------------|
| E1: fenced gate block | C-17 (gate result in Phase 3 opening), C-18 (machine-readable fenced format) | `-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.` as first item in Phase 3 | C-17 requires location (Phase 3 opening before step content); C-18 requires format (fenced code block, literal value, no template notation). One element satisfies both independently: location and format are orthogonal properties. |
| E2: five-case algorithm table | C-15 (Evidence source column per row names relay fields), C-19 (five-case closed table population algorithm) | Four-column state input table at Phase 2.5 sub-element 2 | C-15 requires the Evidence source column to name relay fields per row; C-19 requires the population algorithm to be expressed as a five-case exhaustive table. E2 satisfies both: it IS the five-case table (C-19) AND each row's cells name the relay field (C-15). Both criteria are independently verifiable from E2 alone. |
| E3: semantic block | C-20 (pre-table semantic block explaining provenance, domain, and behavior per domain value) | Column A and B value entries at Phase 2.5 sub-element 1 | C-20 satisfied exclusively by E3. No independence note required. |
| E4: Role Bijection Table | C-11 (role bijection invariant held), C-12 (compact merged table with biconditional hold summary), C-13 (checkpoint enforces before Phase 3), C-14 (relay-seeded evidence, three defect classes) | Phase 2.5 compact merged table with biconditional hold summary rows | C-11 requires the invariant to hold; C-12 requires the merged format; C-13 requires the checkpoint gate; C-14 requires relay-seeded fields. E4 (with the Phase 2.5 checkpoint structure) satisfies all four. C-11 and C-12 are independently verifiable from E4's content; C-13 and C-14 depend on E4's context (checkpoint location and relay structure). |
| E5: relay-seeded fields | C-14 (relay-seeded `Binding Summary row:` and `Schema-governed action:` fields), C-16 (three-value domain definition for status columns) | `Binding Summary row:` and `Schema-governed action:` fields in Phase 2 Execute relays | C-14 requires the seeded fields to be present in every Execute relay; C-16 requires the three-value domain to be defined inline in status column headers. E5 (relay fields) satisfies C-14 directly; C-16 is satisfied by the column domain definition in Phase 2.5, not E5 directly -- C-16 cited separately. |

**C-16: PASS** (three-value status column domains {YES, SILENT/UNDECLARED, relay field absent}
defined inline in status column headers at Phase 2.5; all three values in status cells -- no
annotation or separate column).

**C-22: PASS** (Verdict contains structural element index assigning stable labels E1-E5; element-
criterion citation table maps each element to criteria satisfied by ID; where one element satisfies
two criteria independently (E1: C-17 location + C-18 format; E2: C-15 relay-field naming + C-19
five-case table), independence is stated explicitly with the distinct property each criterion
requires; independence claim is verifiable from the element alone without consulting other
sections).

The biconditional invariant holds: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-21 + C-23 (canonical ordering invariant + pure table-lookup algorithm table)

**Axes**:
- Lifecycle emphasis (C-21): Phase 2.5 canonical sub-element ordering declared as formal
  protocol invariant -- Coverage Matrix preamble, Phase 2.5 ordering declaration block, and
  sequence-numbered sub-element headers.
- Output format (C-23): Five-case closed table restructured as pure table-lookup -- four-column
  state input (Execute relay / SGA field / BSR field / BS entry), all cells closed-world values,
  no prose preamble, no annotations, exhaustiveness declared in table section header.

C-22 not on this axis.

**Hypothesis**: V-02 establishes the canonical ordering invariant (C-21). V-01 establishes the
pure table-lookup algorithm table (C-23). V-04 combines them. The structural interaction: C-21
assigns sequence numbers to Phase 2.5 sub-elements (1: semantics, 2: algorithm, 3: table); C-23
removes the prose preamble from sub-element 2. The combined effect is that sub-element 2 of 3
opens directly with the table header "Evidence source column population -- exhaustive five-case
table" without a preceding prose paragraph, making the sequence-numbered structure cleaner. Risk:
sub-element 2 with no prose preamble may feel abrupt given sub-element 1 (the semantic block) is
prose-heavy. But the sequence number header provides structural context -- the reader knows they
are at sub-element 2 of 3 in the algorithm position, which is sufficient orientation.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix table and schema definitions as V-01. Coverage Matrix preamble updated for
C-21 + C-23:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded in Phase 2 relays (`Binding Summary row:` Direction B seed;
`Schema-governed action:` Direction A seed). Assembled into compact merged Role Bijection Table
at Phase 2.5. Each row carries an Evidence source column populated by exhaustive five-case table
algorithm (C-15/C-19/C-23): four pure state columns map to status and evidence source with zero
inference burden. Status columns A and B carry three-value domain definitions (C-16). Phase 2.5
contains three co-located sub-elements in canonical fixed order: (1) status column semantics
block (C-20), (2) exhaustive five-case algorithm table (C-19/C-23), (3) Role Bijection Table
(C-12). This ordering is a formal invariant -- re-ordering is a structural violation (C-21).
Three defect classes trigger Phase 3 BLOCKED coequal (C-17). Phase 3 opens with fenced structural
labeled block -- literal gate value (C-18). Verdict cites Phase 2.5 result only.

[Schema table, schema definitions, sub-step ordering table: same as V-01.]

---

[Direction A, Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup, Phase 2 Execute:
same as V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-21 + C-23 axes)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Canonical sub-element ordering (C-21)**:

This checkpoint contains exactly three co-located sub-elements in fixed canonical order.
Re-ordering is a structural violation:

1. Sub-element 1 of 3: Status column semantics block (C-20)
2. Sub-element 2 of 3: Evidence source column population algorithm table (C-19/C-23)
3. Sub-element 3 of 3: Role Bijection Table (C-12)

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions -- none is subordinate to or deferred
relative to the others.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary entry for this role. BLOCKED
   immediately.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace
reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate status cells directly -- no annotation, footnote, or separate column.

**Phase 2.5 sub-element 1 of 3 -- Status Column Semantics (C-20)**:

The following block explains the meaning of each domain value per status column. Each entry
names the relay field read, the bijection claim the value makes, and the behavior consequence
at the Phase 2.5 gate.

Column A -- `A: Acts in Execute`:
- `YES` -- Relay field read: `Schema-governed action:` in Execute relay. Claim: role produced a
  schema-governed action matching its Binding Summary declaration. Direction A holds. Gate
  consequence: no BLOCKED contribution from column A.
- `SILENT` -- Relay field read: no Execute relay found. Binding Summary entry exists. Claim: role
  was declared to act but produced no schema-governed action. Direction A violated. Gate
  consequence: BLOCKED -- coequal with UNDECLARED and relay field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Schema-governed action:` field
  absent from relay body. Claim: relay exists but Direction A seed not planted. Direction A
  indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

Column B -- `B: Declared in Summary`:
- `YES` -- Relay field read: `Binding Summary row:` in Execute relay. Claim: role declared its
  Binding Summary entry via relay seed. Direction B holds. Gate consequence: no BLOCKED
  contribution from column B.
- `UNDECLARED` -- Relay field read: Execute relay exists; no Binding Summary entry for this role.
  Claim: role produced a schema-governed action without declaring intent. Direction B violated.
  Gate consequence: BLOCKED -- coequal with SILENT and relay field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Binding Summary row:` field
  absent from relay body. Claim: relay exists but Direction B seed not planted. Direction B
  indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

**Phase 2.5 sub-element 2 of 3 -- Evidence Source Column Population Algorithm (C-19/C-23)**:

**Evidence source column population -- exhaustive five-case table (C-19/C-23)**:

Four state columns determine the case. Values: `present` or `absent`. Exactly five cases; no
additional cases exist. Locate the matching row; copy A Evidence source and B Evidence source
exactly into the Evidence source column.

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` field in relay; BSR = `Binding Summary row:` field
in relay; BS entry = Binding Summary entry exists for this role.

**Phase 2.5 sub-element 3 of 3 -- Role Bijection Table (C-12)**:

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

(compact merged -- C-12; relay-assembled -- C-14; Evidence source column from exhaustive five-
case table -- C-15/C-19/C-23; three-value status column domains -- C-16; semantic block
sub-element 1 above -- C-20; canonical ordering -- C-21):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table -- C-12):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per exhaustive
five-case table, no relay fields absent, canonical ordering held).

**BLOCKED language (C-17 unified)**:

If any A != YES or B != YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

[Same Phase 3 Steps 3a/3b/3c/3d as V-01.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### C-11 through C-21 + C-23 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run.

**C-11 through C-21 and C-23 verification (C-22 excluded -- not on this axis): cited from
Phase 2.5 Role Bijection Checkpoint.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects: [list or "none"].

**C-11: PASS.** **C-12: PASS.** **C-13: PASS.** **C-14: PASS.** **C-15: PASS.** **C-16: PASS.**
**C-17: PASS** (relay field absent BLOCKED coequal; all three classes enumerated; Phase 3 carries
gate result forward as structural element in opening).
**C-18: PASS** (fenced code block with literal gate value; first structural item; machine-readable
without parsing formatting or templates; satisfies C-17 location requirement and C-18 format
requirement independently).
**C-19: PASS** (five-case closed table; each row names relay state, field state, status, exact
evidence source; five cases exhaustive; population rule is table-lookup).
**C-20: PASS** (pre-table semantic block sub-element 1; each domain value names relay field read,
bijection claim, direction consequence, gate behavior; enables independent auditability).
**C-21: PASS** (canonical sub-element ordering declared as formal invariant in Coverage Matrix
preamble and in Phase 2.5 ordering declaration block; sub-elements 1/2/3 labeled with sequence
numbers; ordering violation stated as structural violation; top-to-bottom comprehension enabled
without backtracking).
**C-23: PASS** (exhaustive five-case table stands alone -- no prose preamble; all cells closed-
world values: present/absent/status-value/exact-string; no parenthetical annotations; BS entry
column added to disambiguate relay-absent-B from UNDECLARED; pure table-lookup, zero inference
burden).

The biconditional invariant holds: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-21 + C-22 + C-23 (all three new criteria -- complete v17 target)

**Axes**:
- Lifecycle emphasis (C-21): Phase 2.5 canonical sub-element ordering declared as formal protocol
  invariant -- Coverage Matrix preamble, Phase 2.5 ordering declaration, sequence-numbered headers.
- Output format (C-22): Verdict restructured with structural element index and element-first
  criterion citation table; independence noted explicitly where one element satisfies two criteria.
- Output format (C-23): Five-case closed table as pure table-lookup -- four-column state input,
  all cells closed-world values, no prose preamble, no annotations, exhaustiveness in header.

**Hypothesis**: V-04 establishes C-21 + C-23. V-03 establishes C-22. V-05 combines all three.
The structural interaction: C-21 sequence-numbers Phase 2.5 sub-elements (1: semantics, 2:
algorithm, 3: table); C-23 makes sub-element 2 open directly with the table; C-22 assigns stable
element labels E1-E5 in the Verdict and maps each to criteria satisfied with independence noted.
The combination test: do the sequence-numbered sub-element headers in Phase 2.5 (from C-21)
become useful anchors for the element labels in the Verdict (from C-22)? Design answer: yes --
E2 in the Verdict references "Phase 2.5 sub-element 2 of 3" by name, so the element label is
traceable back to a specific numbered location in the trace. C-23's removal of prose preamble
makes E2 leaner while C-21's label makes it findable. The three criteria are synergistic:
C-21 imposes structure, C-23 removes inference burden, C-22 makes the structure auditable from
the Verdict.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in this
table. A phase using a label not declared here is in violation of the trace protocol.

A Coverage Matrix entry is valid if and only if the schema it registers is referenced in at
least one downstream phase. A schema referenced in any phase is valid if and only if it appears
in the Coverage Matrix. Both directions constitute the Coverage Matrix closed-world bijection
(C-10), verified by Direction A enumeration (below) and Direction B assembly (Verdict).

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded in Phase 2 relays (`Binding Summary row:` Direction B seed;
`Schema-governed action:` Direction A seed). Assembled into compact merged Role Bijection Table
at Phase 2.5. Each row carries an Evidence source column populated by exhaustive five-case table
algorithm (C-15/C-19/C-23): four pure state columns (Execute relay / SGA field / BSR field /
BS entry) map to status and exact evidence source with zero inference burden. Status columns A
and B carry three-value domain definitions: A in {YES, SILENT, relay field absent}; B in {YES,
UNDECLARED, relay field absent} -- inline in status cells, no annotation (C-16). Phase 2.5
contains three co-located sub-elements in canonical fixed order: (1) status column semantics
block (C-20), (2) exhaustive five-case algorithm table (C-19/C-23), (3) Role Bijection Table
(C-12). This ordering is a formal invariant -- re-ordering is a structural violation (C-21).
Three defect classes trigger Phase 3 BLOCKED coequal: SILENT, UNDECLARED, relay field absent
(C-17). Phase 3 opens with fenced structural labeled block -- literal gate value, machine-readable
(C-18). Verdict contains structural element index and element-first criterion citation table;
where one element satisfies two criteria independently, independence is stated explicitly (C-22).
Verdict cites Phase 2.5 result only; does not re-run.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema definitions** (biconditional form):

**Schema 1**: Valid iff every severity label uses only {P1, P2, P3}.
**Schema 2**: SA-TO-SG label lock invariant: promoted SA uses SG label in all downstream phases.
**Schema 3**: Valid iff every Phase 4 Amend entry names a channel from {spec, invocation,
artifact, quality}.
**Schema 4**: G-1: Step 3b >=2 distinct Source types. G-2: no two same-Source findings carry
identical Action. G-3: all Step 3b entries use only {P1, P2, P3}.
**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >=2 entries. Step
3d valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

---

### Closed-World Verification -- Direction A

| Schema | Matrix row | Referenced at (enumerate all) | Orphan? |
|--------|-----------|-------------------------------|---------|
| Schema 1 | Row 1 | Step 3a (legend); Step 3b (enforced); Step 3c G-3 (verified); Phase 4 Amend (enforced) | NO |
| Schema 2 | Row 2 | Stage 1 audit; SA-TO-SG PROMOTION; Step 3b Source column; Execute role relay | NO |
| Schema 3 | Row 3 | Step 3d (activated); Phase 4 Amend (channel field required) | NO |
| Schema 4 | Row 4 | Step 3c (G-1/G-2/G-3 run); Phase 4 pre-check (confirmed) | NO |
| Schema 5 | Row 5 | Phase 3 sub-steps: 3a->3b; 3b->3c; 3c->3d; 3d->Phase 4 | NO |

Direction A: all 5 rows confirmed. HOLDS.

---

### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role] | [severity labels or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay to Stage 2: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: PASS / FAIL].

**Schema footprint -- Stage 1**: Schema 2 (Source labels), Schema 1 (Severity labels).

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

After promotion: [SA remaining: `{{sa_remaining}}`], [SG from promotion: `{{sg_promoted}}`].

**Schema footprint -- SA-TO-SG PROMOTION**: Schema 2.

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [stack: ] [spec_version: ]

```
[role: {{name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

Setup carry-forward: [topic], [scope], [roles], [SA remaining], [SG total].

**Schema footprint -- Phase 1 Setup**: Schema 1 (binding declared), Schema 2 (confirmed).

---

#### Phase 2 -- Execute

Produce: `{topic}-skill-trace-{date}.md`. Three required fields in every relay: Schema 2
compliance, `Binding Summary row:` (Direction B seed), `Schema-governed action:` (Direction A
seed). A relay missing either seeded field must declare the absence -- Phase 2.5 reads the relay
and detects relay field absent defects.

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-21 + C-23 axes: canonical ordering + pure table)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Canonical sub-element ordering (C-21)**:

This checkpoint contains exactly three co-located sub-elements in fixed canonical order.
Re-ordering is a structural violation coequal with schema label violations:

1. Sub-element 1 of 3: Status column semantics block (C-20)
2. Sub-element 2 of 3: Evidence source column population algorithm table (C-19/C-23)
3. Sub-element 3 of 3: Role Bijection Table (C-12)

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions -- none is subordinate to or deferred
relative to the others.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary entry for this role. BLOCKED
   immediately.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace
reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate status cells directly -- no annotation, footnote, or separate column.

**Phase 2.5 sub-element 1 of 3 -- Status Column Semantics (C-20)**:

The following block explains the meaning of each domain value per status column. Each entry
names the relay field read, the bijection claim made, and the gate behavior consequence.

Column A -- `A: Acts in Execute`:
- `YES` -- Relay field read: `Schema-governed action:` in Execute relay. Claim: role produced a
  schema-governed action matching its Binding Summary declaration. Direction A holds for this row.
  Gate consequence: no BLOCKED contribution from column A.
- `SILENT` -- Relay field read: no Execute relay found. Binding Summary entry exists. Claim: role
  was declared to act but produced no schema-governed action. Direction A violated. Gate
  consequence: BLOCKED -- coequal with UNDECLARED and relay field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Schema-governed action:` field
  absent from relay body. Claim: relay exists but Direction A seed not planted. Direction A
  indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

Column B -- `B: Declared in Summary`:
- `YES` -- Relay field read: `Binding Summary row:` in Execute relay. Claim: role declared its
  Binding Summary entry via relay seed. Direction B holds. Gate consequence: no BLOCKED
  contribution from column B.
- `UNDECLARED` -- Relay field read: Execute relay exists; no Binding Summary entry for this role.
  Claim: role produced a schema-governed action without declaring intent. Direction B violated.
  Gate consequence: BLOCKED -- coequal with SILENT and relay field absent.
- `relay field absent` -- Relay field read: Execute relay exists; `Binding Summary row:` field
  absent from relay body. Claim: relay exists but Direction B seed not planted. Direction B
  indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

**Phase 2.5 sub-element 2 of 3 -- Evidence Source Column Population Algorithm (C-19/C-23)**:

**Evidence source column population -- exhaustive five-case table (C-19/C-23)**:

Four state columns determine the case. Values: `present` or `absent`. Exactly five cases; no
additional cases exist. Locate the matching row; copy A Evidence source and B Evidence source
exactly into the Evidence source column.

| Case | Execute relay | SGA field | BSR field | BS entry | A status | B status | A Evidence source | B Evidence source |
|------|--------------|-----------|-----------|----------|----------|----------|-------------------|-------------------|
| Standard | present | present | present | present | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | absent | absent | absent | present | SILENT | YES | `no relay` | `Binding Summary row:` (Binding Summary direct) |
| relay-absent-A | present | absent | present | present | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| relay-absent-B | present | present | absent | present | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | present | present | present | absent | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary entry` |

Column key: SGA = `Schema-governed action:` field in relay; BSR = `Binding Summary row:` field
in relay; BS entry = Binding Summary entry exists for this role.

**Phase 2.5 sub-element 3 of 3 -- Role Bijection Table (C-12)**:

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

(compact merged -- C-12; relay-assembled -- C-14; Evidence source column from exhaustive five-
case table -- C-15/C-19/C-23; three-value status column domains -- C-16; semantic block above
sub-element 1 -- C-20; canonical ordering -- C-21):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table -- C-12):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per exhaustive
five-case table, no relay fields absent, canonical sub-element ordering held).

**BLOCKED language (C-17 unified -- all three defect classes enumerated explicitly)**:

If any A != YES or B != YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

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

**Schema footprint -- Step 3b**: Schema 2 (Source column), Schema 1 (Severity column), Schema 5.

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

**Schema footprint -- Phase 4 Amend**: Schema 2 (Source; lock honored), Schema 3 (channel
field present), Schema 1 (Severity inherited), Schema 4 (gate status confirmed).

---

### Verdict (Phase 5 -- Compliance Ledger + Bijection Enumerations)

#### Compliance Ledger

"Observed behavior: as expected" is structurally invalid in any cell.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [what the legend stated] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 only | [list severity values and count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | Completeness gate verified | [G-3 result; labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay -- [role] | EG findings use only P1/P2/P3 | [list labels used] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted -> SG; no SA downstream | [which SA promoted; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; promoted = SG | [list Source labels] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay -- [role] | Source labels valid; lock honored | [list Source labels used] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation language] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Channel field in every entry | [channels used] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [results] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after all gates PASS | [gate values] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity across all roles | [Source types; roles] | PASS / FAIL |
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

Undeclared references: NONE. Direction B: HOLDS.

**C-10 Coverage Matrix bijection**:

| Direction | Evidence | Result |
|-----------|----------|--------|
| A (matrix -> phase) | Direction A table -- all 5 rows confirmed | HOLDS |
| B (phase -> matrix) | Direction B table assembled from footprint records | HOLDS |

**C-10: PASS.**

---

#### Structural Element Index (C-22)

| Element label | Description | Location |
|---------------|-------------|---------|
| E1 | Fenced `-> GATE RESULT:` block | Phase 3, first structural item before Step 3a |
| E2 | Exhaustive five-case Evidence source population table | Phase 2.5 sub-element 2 of 3 |
| E3 | Status column semantics block | Phase 2.5 sub-element 1 of 3 |
| E4 | Compact merged Role Bijection Table with biconditional hold summary | Phase 2.5 sub-element 3 of 3 |
| E5 | Relay-seeded `Binding Summary row:` and `Schema-governed action:` fields | Phase 2 Execute relays (all roles) |

---

#### C-11 through C-23 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section is FAIL for C-13.

**Bijection gate summary (cited from Phase 2.5)**:

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**Element-criterion citation table (C-22)**:

| Element | Criteria satisfied | Evidence | Independence note |
|---------|--------------------|----------|-------------------|
| E1: fenced gate block | C-17 (gate result in Phase 3 opening), C-18 (machine-readable fenced format) | `-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.` as first item in Phase 3 | C-17 requires location (Phase 3 opening before step content); C-18 requires format (fenced code block, literal value, no template notation, no prose wrapping). One element satisfies both independently: location and format are orthogonal properties verifiable without reference to each other. |
| E2: five-case algorithm table | C-15 (Evidence source column names relay fields per row), C-19 (five-case closed table population algorithm), C-23 (pure table-lookup, no prose preamble, no annotations) | Phase 2.5 sub-element 2 of 3 -- exhaustive five-case table with four-column state input | C-15 requires Evidence source column to name relay fields; C-19 requires population algorithm as five-case table; C-23 requires zero inference burden, no annotations. All three are independently verifiable from E2: C-15 checks cell content, C-19 checks table structure, C-23 checks absence of prose/annotations. |
| E3: semantic block | C-20 (pre-table semantic block explaining provenance, domain boundary, and behavior per domain value) | Phase 2.5 sub-element 1 of 3 -- Column A and B value entries | C-20 satisfied exclusively by E3. No independence note required. |
| E4: Role Bijection Table | C-11 (role bijection invariant held), C-12 (compact merged table with biconditional hold summary), C-13 (Phase 2.5 gate enforces before Phase 3), C-14 (relay-seeded evidence, three defect classes named) | Phase 2.5 sub-element 3 of 3 -- compact merged table with biconditional hold summary rows | C-11 and C-12 are independently verifiable from E4's content alone (invariant holds; merged format present). C-13 depends on E4's location (Phase 2.5 checkpoint before Phase 3) -- location is independently verifiable from the trace structure. C-14 depends on E5 (relay fields) and on E4's defect class naming -- C-14 satisfied jointly by E4 and E5. |
| E5: relay-seeded fields | C-14 (relay-seeded fields present in every Execute relay; three defect classes named at Phase 2.5) | `Binding Summary row:` and `Schema-governed action:` fields in Phase 2 Execute relays | C-14 has two requirements: E5 satisfies the relay-field-present requirement; E4 satisfies the defect-class-naming requirement. Neither E4 nor E5 alone satisfies C-14 -- they satisfy it jointly. |

**C-16: PASS** (three-value status column domains defined inline in status column headers; all
three values in status cells -- no annotation or separate column).

**C-21: PASS** (Phase 2.5 canonical sub-element ordering declared as formal invariant in
Coverage Matrix preamble and in Phase 2.5 canonical ordering block; sub-elements numbered 1/2/3
with sequence labels in headers; ordering violation stated as structural violation coequal with
schema label violations; top-to-bottom comprehension of Phase 2.5 enabled without backtracking:
semantics (E3) -> algorithm (E2) -> table (E4)).

**C-22: PASS** (Verdict contains structural element index assigning stable labels E1-E5 with
location references; element-criterion citation table maps each element to all criteria it
satisfies by ID; where one element satisfies two or more criteria independently (E1: C-17
location + C-18 format; E2: C-15 relay-field naming + C-19 five-case table + C-23 pure
table-lookup), independence is stated explicitly with the distinct property each criterion
requires and confirmation that each property is verifiable without reference to the other;
joint satisfaction (E4+E5 for C-14) is also noted, distinguishing it from independence).

**C-23: PASS** (exhaustive five-case table E2 stands alone -- no prose preamble; exhaustiveness
declared in table section header "exhaustive five-case table (C-19/C-23)"; all cells contain
closed-world values only: present/absent/YES/SILENT/UNDECLARED/relay-field-absent/exact-string;
no parenthetical annotations within cells; BS entry column added as fourth state column to
cleanly separate relay-absent-B (BSR field absent, BS entry present) from UNDECLARED (BSR field
present, BS entry absent) without cell qualifiers; no supplementary notes after table;
population rule is pure table-lookup with zero inference burden, directly closing the PARTIAL
defect class from V-02 of earlier rounds).

The biconditional invariant -- Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute -- is found to hold: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
