---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 4
rubric: trace-skill-rubric-v15-2026-03-15.md
---

# trace-skill -- Variations v15 R4 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R3 V-05 achieves C-01 through C-14 PASS under v14 scoring. v15 formalizes three
new aspirational criteria from R3 excellence signals: C-15 (Evidence source column per row in
merged Role Bijection Table), C-16 (relay field absent as first-class inline status column value),
C-17 (Phase 2.5 gate unification -- relay field absent coequal blocking, BLOCKED message
enumerating all three classes, Phase 3 structural gate header).

**R3 V-05 C-15/C-16/C-17 state** (scored against v15):
- C-15: Biconditional hold summary carries Evidence source column at summary level. Main table
  has a column labeled "Schema-governed action (relay field)" but no dedicated Evidence source
  column per row naming relay fields for A and B separately. C-15 = FAIL.
- C-16: Status columns show `YES / SILENT / relay field absent` and `YES / UNDECLARED / relay
  field absent` as template notation. The column definition does not formally enumerate the
  three-value domain {YES, SILENT/UNDECLARED, relay field absent} as a named set. C-16 = PARTIAL.
- C-17: BLOCKED message enumerates all three defect classes. Phase 3 carry-forward in prose body
  text ("Carrying forward from Phase 2.5..."). Coequal treatment for relay field absent implicit
  ("FAIL condition") but not stated as explicit coequal. C-17 = PARTIAL.

**v15 R4 variation axes**:
- **Output format (C-15)**: Evidence source column per row in compact table, naming relay fields
  from which Direction A and Direction B status values were read (V-01)
- **Output format (C-16)**: Status column headers define three-value domain formally inline,
  not as template notation (V-02)
- **Lifecycle emphasis (C-17)**: Explicit coequal blocking statement, BLOCKED message exact
  format, Phase 3 opens with structural gate result element (V-03)

**Combined variations**:
- V-04: C-15 + C-16 (Evidence source column + three-value status column domain definition)
- V-05: C-15 + C-16 + C-17 (all three new criteria -- complete v15 target)

All five inherit the full R3 V-05 architecture (C-01 through C-14). What varies per V-0N:
only the C-15/C-16/C-17 structural mechanism.

---

## V-01 -- Single axis: Output format (C-15: Evidence source column per row)

**Axis**: Output format -- the compact merged Role Bijection Table gains a dedicated Evidence
source column. Each row names the relay fields from which Direction A and Direction B status
values were read: `A: Schema-governed action: relay field; B: Binding Summary row: relay field`
for standard rows. For SILENT rows (no Execute relay): `A: no relay (Binding Summary declares
absent); B: Binding Summary row: relay field`. For relay field absent rows: the absent field is
named in the Evidence source cell. The column is populated at Phase 2.5 from relay field names
directly -- not from end-of-trace reconstruction. R3 V-05 had Evidence source at the
biconditional hold summary level; C-15 extends this to the per-row table so every row carries
individual provenance.

**Hypothesis**: R3 V-04/V-05 placed Evidence source in the biconditional summary only -- an
aggregate declaration rather than per-row attribution. C-15 formalizes per-row provenance so an
evaluator can trace each row's A and B status values to specific relay fields without reading
the summary. The new column also resolves an asymmetric case gap: SILENT rows have no Execute
relay, so their Evidence A cell must explicitly state `no relay` rather than naming a relay
field. Risk: a six-column table may be wide; model compliance depends on whether the population
rule for the Evidence source column covers all four case types (standard, SILENT, UNDECLARED,
relay field absent).

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
at Phase 2.5 -- each row carries an Evidence source column naming the relay fields from which
Direction A and Direction B status values were read (C-15). Phase 3 BLOCKED if bijection fails.
Verdict cites Phase 2.5 result; does not re-run.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema definitions** (biconditional form -- violations are structural invalidity, not quality issues):

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
one execution phase. Direction A enumerates the forward mapping: for each Coverage Matrix row,
name every specific phase and step where it is referenced.

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

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role] | [severity labels applicable to this role's EG findings, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules for promoted gaps] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}` and produces a gap audit table using Schema 2
Source labels and Schema 1 Severity labels.

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-15 axis: Evidence source column per row)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes**:
1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. Column A = SILENT.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. Column B = UNDECLARED.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing. A relay field absent is a FAIL condition blocking Phase 3.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Evidence source column population rules** (C-15):
- Standard row (relay present, both seeded fields populated):
  `A: Schema-governed action: relay field; B: Binding Summary row: relay field`
- SILENT row (no Execute relay):
  `A: no relay (Binding Summary declares absent); B: Binding Summary row: relay field`
- relay field absent -- `Schema-governed action:` missing:
  `A: Schema-governed action: absent from relay; B: Binding Summary row: relay field`
- relay field absent -- `Binding Summary row:` missing:
  `A: Schema-governed action: relay field; B: Binding Summary row: absent from relay`
- UNDECLARED row (no Binding Summary row):
  `A: Schema-governed action: relay field; B: no Binding Summary row`

**Population rules**:
- Execute relay present: read `Binding Summary row:` -> B column source; read
  `Schema-governed action:` -> action cell and A column status.
  If `Schema-governed action:` absent: A = `relay field absent`.
  If `Binding Summary row:` absent: B = `relay field absent`.
- Binding Summary row present, no Execute relay: A = `SILENT`.
- Execute relay present, no Binding Summary row: B = `UNDECLARED`.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged format with Evidence source column -- C-12 + C-14 + C-15):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute | B: Declared in Summary | Evidence source |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay, or "SILENT" / "relay field absent"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [relay field or "no relay"]; B: [relay field or "no row"] |

Defect declarations (for any non-YES value in A or B):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [Binding Summary row / Schema-governed action]." (relay field absent)

**Biconditional hold summary** (closes the table):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: no SILENT or relay field absent in column A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: no UNDECLARED or relay field absent in column B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source column populated per row,
no relay fields absent).

If FAIL: **Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field
absent. Name the role relay and the specific defect. Resolve before proceeding.]**

---

#### Phase 3 -- Findings

Carrying forward from Phase 2.5 Role Bijection Checkpoint: Role Bijection = `{{PASS}}`.
Phase 3 valid to begin.

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

#### C-11 through C-15 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section is FAIL for C-13.

**C-11 through C-15 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

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
**C-15: PASS** (compact merged Role Bijection Table carries Evidence source column; each row
names the relay field(s) from which Direction A and Direction B status values were read;
populated at Phase 2.5 directly from relay field names -- no end-of-trace reconstruction).

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

## V-02 -- Single axis: Output format (C-16: relay field absent as first-class status column value)

**Axis**: Output format -- the status columns in the compact merged Role Bijection Table carry
formal three-value domain definitions. Column A -- `A: Acts in Execute` -- declares value domain
{`YES`, `SILENT`, `relay field absent`} in its column header or a co-located domain definition
block. Column B -- `B: Declared in Summary` -- declares value domain {`YES`, `UNDECLARED`,
`relay field absent`}. All three values appear inline in the appropriate status cell -- no
annotation, footnote, or separate column. The column definition is not template notation for
possible values; it is a formal specification of the column's domain named before the table is
populated.

**Hypothesis**: R3 V-04/V-05 showed relay field absent as `YES / SILENT / relay field absent`
in table cell notation -- enumerated in the template placeholder rather than in a formal column
definition. C-16 formalizes the three-value domain at the column definition level, not as a
cell value hint. The distinction: C-14 names relay field absent as a defect class and places
it in appropriate cells; C-16 requires the column itself to declare it as an enumerated first-
class member of the column's value domain, so a structural auditor reading only the column
header knows the column accepts three values. Risk: embedding the domain declaration in a
preamble block rather than the column header may satisfy intent but not the C-16 criterion;
the domain must be in the column definition position, not in surrounding prose.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, Role-binding column, biconditional invariant preambles.
C-11 note updated:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded. Assembled into compact merged Role Bijection Table at Phase 2.5.
Status columns A and B carry formal three-value domain definitions: A ∈ {YES, SILENT, relay
field absent}; B ∈ {YES, UNDECLARED, relay field absent} -- all three values inline in the
status cell, no annotation or separate column (C-16). Phase 3 BLOCKED if bijection fails.
Verdict cites Phase 2.5 result only.

[Schema table, biconditional definitions, and sub-step ordering table: same as V-01.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01 -- all 5 schemas confirmed. Direction A: HOLDS.]

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

#### Phase 2 -- Execute

[Same relay-seeded structure as V-01 -- `Binding Summary row:` and `Schema-governed action:`
seeded fields in every relay.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-16 axis: three-value status column domain formalized)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes** (C-14):
1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no action.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row.
3. **relay field absent**: relay exists; seeded field missing from relay.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- three-value domain:
- `YES`: role has Execute relay with populated `Schema-governed action:` field
- `SILENT`: role has Binding Summary row; Execute relay absent or action missing
- `relay field absent`: relay exists; `Schema-governed action:` field is missing from relay

Column B -- `B: Declared in Summary` -- three-value domain:
- `YES`: role has `Binding Summary row:` field populated in Execute relay
- `UNDECLARED`: role has Execute relay; no Binding Summary row
- `relay field absent`: relay exists; `Binding Summary row:` field is missing from relay

All values populate the status cell directly. No annotation, footnote, or separate column for
relay field absent.

**Population rules**:
- Execute relay present, both seeded fields populated: A = YES, B = YES.
- Execute relay present, `Schema-governed action:` missing: A = `relay field absent`.
- Execute relay present, `Binding Summary row:` missing: B = `relay field absent`.
- Binding Summary row present, no Execute relay: A = `SILENT`.
- Execute relay present, no Binding Summary row: B = `UNDECLARED`.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged format with three-value status column domains -- C-12 + C-14 + C-16):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay, or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent |

Defect declarations (for any non-YES value):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (A or B = relay field absent)

**Biconditional hold summary** (closes the table):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (A ∈ {YES} for all rows; B ∈ {YES} for all rows).

If FAIL: **Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field
absent. Name the role relay and the specific defect. Resolve before proceeding.]**

---

#### Phase 3 -- Findings

Carrying forward from Phase 2.5 Role Bijection Checkpoint: Role Bijection = `{{PASS}}`.
Phase 3 valid to begin.

[Same Phase 3 -- Steps 3a/3b/3c/3d with Schema footprints -- as V-01.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5 with invariant-witness cells.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### C-11 through C-14 + C-16 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run. A bijection audit appearing
only in this section is FAIL for C-13.

**C-11 through C-14 and C-16 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no defects).
**C-12: PASS** (compact merged table with named biconditional hold summary at Phase 2.5).
**C-13: PASS** (Phase 2.5 named checkpoint present; Verdict cites, does not re-run).
**C-14: PASS** (relay-seeded fields present; three defect classes named and distinguished;
evidence sourced to relay fields).
**C-16: PASS** (status columns A and B carry formal three-value domain {YES, SILENT/UNDECLARED,
relay field absent} in column definition; all three values inline in status cells; no annotation,
footnote, or separate column).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (C-17: Phase 2.5 gate unification)

**Axis**: Lifecycle emphasis -- three C-17 sub-requirements are formalized over R3 V-05:
(1) An explicit coequal blocking statement at Phase 2.5 names all three defect classes as
equal triggers: "relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED
-- no asymmetric treatment."
(2) The BLOCKED message enumerates all three classes with the C-17 prescribed format:
"Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]"
(3) Phase 3 opens with a structural gate result element -- a labeled block before any findings
content -- carrying the Phase 2.5 gate result. The gate result appears in Phase 3's structural
opening, not only in Verdict.

**Hypothesis**: R3 V-05 had relay field absent as "a FAIL condition" but did not use the word
coequal or state explicitly that no asymmetric treatment applies. The BLOCKED message in R3 V-05
enumerated all three classes but the coequal framing was implicit. Phase 3 in R3 V-05 carried
the gate result as prose text ("Carrying forward from Phase 2.5...") in the section body. C-17
requires: (1) the explicit coequal declaration so an evaluator does not infer parity from defect
class enumeration alone; (2) the BLOCKED message format is locked -- no variation; (3) Phase 3's
structural opening carries the gate result as a labeled element, not body prose. Risk: the
distinction between "labeled structural element" and "first line of body prose" is subtle; the
v15 criterion says "gate result present in Phase 3 header" -- the implementation uses a
`-> GATE RESULT:` labeled block as the first structural element of Phase 3.

[Uses R3 V-05 table format without Evidence source column (C-15 not on this axis) and without
explicit three-value domain definition (C-16 not on this axis).]

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, Role-binding column, biconditional invariants.
C-11 note updated:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded. Assembled into compact merged Role Bijection Table at Phase 2.5.
Three defect classes trigger Phase 3 BLOCKED coequal -- SILENT, UNDECLARED, relay field absent
-- no asymmetric treatment (C-17 explicit). Phase 3 opens with gate result as structural element.
Verdict cites Phase 2.5 result only.

[Schema table, biconditional definitions, sub-step ordering table: same as V-01.]
[Direction A, Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup: same as V-01.]
[Phase 2 Execute: same relay-seeded structure as V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-17 axis: gate unification, coequal blocking)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions -- none is subordinate to or deferred
relative to the others.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. BLOCKED immediately on discovery.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Population rules**:
- Execute relay present: read `Binding Summary row:` -> B; read `Schema-governed action:` -> A.
- `Schema-governed action:` absent: A = `relay field absent`.
- `Binding Summary row:` absent: B = `relay field absent`.
- Binding Summary row present, no Execute relay: A = `SILENT`.
- Execute relay present, no Binding Summary row: B = `UNDECLARED`.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged format -- C-12; populated from relay fields -- C-14):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay, or "SILENT" / "relay field absent"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent |

Defect declarations (for any non-YES value in A or B):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: no SILENT or relay field absent in column A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: no UNDECLARED or relay field absent in column B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent).

**BLOCKED language (C-17 unified -- all three defect classes, coequal)**:

If any A ≠ YES or B ≠ YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. SILENT, UNDECLARED, and
relay field absent all trigger this exact BLOCKED language with no asymmetric treatment.

---

#### Phase 3 -- Findings

**-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = `{{PASS}}`.**

Phase 3 begins on PASS. Gate result carried forward from Phase 2.5; not re-evaluated here.

[Same Phase 3 -- Steps 3a/3b/3c/3d with Schema footprints -- as V-01.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5 with invariant-witness cells.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### C-11 through C-14 + C-17 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run. A bijection audit appearing
only in this section is FAIL for C-13.

**C-11 through C-14 and C-17 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

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
**C-17: PASS** (relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED --
explicit coequal statement present at Phase 2.5; BLOCKED message enumerates all three defect
classes explicitly; Phase 3 carries gate result forward as structural `-> GATE RESULT:` element
in opening before findings content begins).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-15 + C-16 (Evidence source column + three-value status column domains)

**Axes**:
- Output format (C-15): Evidence source column per row in compact table, naming relay fields
  for Direction A and Direction B status values.
- Output format (C-16): Status column headers carry formal three-value domain definitions
  {YES, SILENT/UNDECLARED, relay field absent} inline.

No Phase 2.5 gate unification (C-17 not on this axis -- coequal blocking not explicitly stated,
Phase 3 opening is body prose).

**Hypothesis**: V-01 added the Evidence source column (C-15). V-02 formalized the three-value
status column domain (C-16). V-04 combines them into a single table: six columns, with the
status columns carrying formal domain definitions AND each row carrying per-row relay field
provenance. The combination tests whether the two format extensions coexist without ambiguity:
Evidence source names where each status came from; the column domain definition names what each
status can be. A SILENT row's Evidence source reads `A: no relay` while the domain definition
confirms SILENT is a valid A value. A relay field absent row's Evidence source reads
`A: Schema-governed action: absent from relay` while A = relay field absent. Risk: table width
increases with six columns; the column header for A and B must carry both the domain declaration
and be parseable as table cells.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, Role-binding column, biconditional invariants.
C-11 note updated:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded. Assembled into compact merged Role Bijection Table at Phase 2.5.
Status columns A and B carry three-value domain definitions: A ∈ {YES, SILENT, relay field
absent}; B ∈ {YES, UNDECLARED, relay field absent} -- all three values inline in status cells.
Each row carries an Evidence source column naming the relay fields from which status values were
read (C-15). Phase 3 BLOCKED if bijection fails. Verdict cites Phase 2.5 result only.

[Schema table, biconditional definitions, sub-step ordering table: same as V-01.]
[Direction A, Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup: same as V-01.]
[Phase 2 Execute: same relay-seeded structure as V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-15 + C-16 axes)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes** (C-14):
1. **SILENT**: Binding Summary row present; Execute relay absent or no schema-governed action.
2. **UNDECLARED**: Execute relay present; no Binding Summary row.
3. **relay field absent**: relay exists; seeded field missing.

**Evidence source**: relay fields read directly. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

**Evidence source column population rules (C-15)**:
- Standard row: `A: Schema-governed action: relay field; B: Binding Summary row: relay field`
- SILENT row: `A: no relay (Binding Summary declares absent); B: Binding Summary row: relay field`
- relay field absent (action missing): `A: Schema-governed action: absent from relay; B: Binding Summary row: relay field`
- relay field absent (binding missing): `A: Schema-governed action: relay field; B: Binding Summary row: absent from relay`
- UNDECLARED row: `A: Schema-governed action: relay field; B: no Binding Summary row`

**Population rules**:
- Execute relay present: read `Binding Summary row:` -> B; read `Schema-governed action:` -> A.
- `Schema-governed action:` absent: A = `relay field absent`, Evidence A = `Schema-governed action: absent from relay`.
- `Binding Summary row:` absent: B = `relay field absent`, Evidence B = `Binding Summary row: absent from relay`.
- No Execute relay for Binding Summary row: A = `SILENT`, Evidence A = `no relay`.
- Execute relay for undeclared role: B = `UNDECLARED`, Evidence B = `no Binding Summary row`.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column -- C-15; three-value status column domains -- C-16):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [relay field]; B: [relay field] |

Defect declarations (for any non-YES status value):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per row).

If FAIL: **Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field
absent. Name the role relay and the specific defect. Resolve before proceeding.]**

---

#### Phase 3 -- Findings

Carrying forward from Phase 2.5 Role Bijection Checkpoint: Role Bijection = `{{PASS}}`.
Phase 3 valid to begin.

[Same Phase 3 -- Steps 3a/3b/3c/3d -- as V-01.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same as V-01 -- VC-1 through VC-5.]

#### Closed-World Verification -- Direction B

[Same as V-01.]

**C-10: PASS.**

---

#### C-11 through C-16 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run.

**C-11 through C-16 verification: cited from Phase 2.5.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects: [list or "none"].

**C-11: PASS.** (Phase 2.5 gate = PASS, both directions HOLDS.)
**C-12: PASS.** (compact merged table, biconditional hold summary.)
**C-13: PASS.** (Phase 2.5 checkpoint, BLOCKED language, Verdict cites.)
**C-14: PASS.** (relay-seeded fields, three defect classes, relay-sourced evidence.)
**C-15: PASS.** (Evidence source column per row naming relay fields for A and B; populated at
Phase 2.5 from relay field names -- no reconstruction.)
**C-16: PASS.** (Status columns A and B carry formal three-value domain {YES, SILENT/UNDECLARED,
relay field absent} inline in column definition; all three values in status cells -- no annotation
or separate column.)

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-15 + C-16 + C-17 (all three new criteria)

**Axes**:
- Output format (C-15): Evidence source column per row in compact Role Bijection Table.
- Output format (C-16): Three-value status column domain formally defined inline.
- Lifecycle emphasis (C-17): Explicit coequal blocking, BLOCKED message exact format, Phase 3
  structural gate header.

**Hypothesis**: V-04 establishes the full output format (C-15 + C-16). V-03 establishes the
lifecycle unification (C-17). V-05 combines all three: Phase 2.5 reads relay fields into a
six-column table with formalized status column domains and per-row Evidence source attribution;
Phase 3 opens with a `-> GATE RESULT:` structural element; the BLOCKED message enumerates all
three defect classes coequally. The three criteria are complementary -- C-15 names provenance,
C-16 names domains, C-17 names behavior -- and all apply at Phase 2.5. The co-location test:
does the Phase 2.5 section remain parseable with the coequal declaration, domain definition,
Evidence source rules, and compact table all present? Risk: Phase 2.5 carries the most
specification density of any phase in the trace; V-05 represents the maximum structural load.
The design principle is that all three formalizations target the same Phase 2.5 gate surface --
they are not redundant; they specify different auditable properties of the same table.

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
at Phase 2.5 Role Bijection Checkpoint. Status columns A and B carry three-value domain
definitions: A ∈ {YES, SILENT, relay field absent}; B ∈ {YES, UNDECLARED, relay field absent}
-- all three values inline in status cells, no annotation (C-16). Each row carries Evidence
source column naming relay fields (C-15). Three defect classes trigger Phase 3 BLOCKED coequal:
SILENT, UNDECLARED, relay field absent -- no asymmetric treatment (C-17). Phase 3 opens with
gate result as structural element. Verdict cites Phase 2.5 result only; does not re-run.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema definitions** (biconditional form):

**Schema 1**: A trace is valid w.r.t. Schema 1 if and only if every severity label in any phase
uses only {P1, P2, P3}. P1 = blocks useful baseline. P2 = quality improvement. P3 = advisory.

**Schema 2**: The SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all
phases after SA-TO-SG PROMOTION. A promoted gap retaining its SA label is a structural violation.

**Schema 3**: A trace is valid w.r.t. Schema 3 if and only if every Phase 4 Amend entry names
a remediation channel from {spec, invocation, artifact, quality}.

**Schema 4**: G-1 invariant: Step 3b >=2 distinct Source types. G-2: no two same-Source findings
carry identical Action. G-3: all Step 3b entries use only {P1, P2, P3}.

**Schema 5**: Step 3b valid iff Step 3a complete. Step 3c valid iff Step 3b >=2 entries. Step 3d
valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

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

Direction A: all 5 rows confirmed. Direction A invariant: HOLDS.

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-15 + C-16 + C-17: Evidence source, three-value domains, coequal unified gate)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions -- none is subordinate to or deferred
relative to the others.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. BLOCKED immediately on discovery.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

**Evidence source column population rules (C-15)**:
- Standard row: `A: Schema-governed action: relay field; B: Binding Summary row: relay field`
- SILENT row: `A: no relay (Binding Summary declares absent); B: Binding Summary row: relay field`
- relay field absent (action missing): `A: Schema-governed action: absent from relay; B: Binding Summary row: relay field`
- relay field absent (binding missing): `A: Schema-governed action: relay field; B: Binding Summary row: absent from relay`
- UNDECLARED row: `A: Schema-governed action: relay field; B: no Binding Summary row`

**Population rules**:
- Execute relay present: read `Binding Summary row:` -> B; read `Schema-governed action:` -> A.
- `Schema-governed action:` absent: A = `relay field absent`, Evidence A = `Schema-governed action: absent from relay`.
- `Binding Summary row:` absent: B = `relay field absent`, Evidence B = `Binding Summary row: absent from relay`.
- No Execute relay for Binding Summary row: A = `SILENT`, Evidence A = `no relay`.
- Execute relay for undeclared role: B = `UNDECLARED`, Evidence B = `no Binding Summary row`.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column -- C-15; three-value status column domains -- C-16):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [relay field]; B: [relay field] |

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

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per row, no
relay fields absent).

**BLOCKED language (C-17 unified -- all three defect classes enumerated explicitly)**:

If any A ≠ YES or B ≠ YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

---

#### Phase 3 -- Findings

**-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = `{{PASS}}`.**

Phase 3 begins on PASS. Gate result carried forward from Phase 2.5; not re-evaluated here.

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
- [source: `{{source}}`] (Schema 2 label lock)
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
| VC-4 | Schema 4 | Step 3b G-1 cross-role | Source diversity across all roles | [Source types; roles contributed each] | PASS / FAIL |
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

#### C-11 through C-17 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section is FAIL for C-13.

**C-11 through C-17 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

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
`-> GATE RESULT:` element in opening before findings content begins -- gate result in Phase 3
header, not only in Verdict).

The biconditional invariant -- Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute -- is found to hold: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
