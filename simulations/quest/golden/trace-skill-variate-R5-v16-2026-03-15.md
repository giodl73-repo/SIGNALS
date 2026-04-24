---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 5
rubric: trace-skill-rubric-v16-2026-03-15.md
---

# trace-skill -- Variations v16 R5 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R4 V-05 achieves C-01 through C-17 PASS under v15 scoring. v16 formalizes three
new aspirational criteria from R4 excellence signals: C-18 (`-> GATE RESULT:` labeled structural
block format for Phase 3 gate carry-forward -- not prose), C-19 (five-case closed table for the
Evidence source column population algorithm -- each case names relay field content explicitly),
C-20 (pre-table semantic block explaining provenance, domain, and behavior per domain value per
status column -- enables independent auditability at the table surface).

**R4 V-05 C-18/C-19/C-20 state** (scored against v16):
- C-18: Phase 3 opens with `**-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = {{PASS}}.**`
  -- uses the `-> GATE RESULT:` prefix (C-17 satisfied) but wraps it in bold markdown prose with
  backtick template notation `{{PASS}}`. A structural labeled block must be standalone and
  machine-readable without parsing markdown formatting or expanding template placeholders. The gate
  status `PASS` or `BLOCKED` must be a literal value, not a template variable. C-18 = FAIL.
- C-19: Evidence source column population expressed as five bullet points. Cases named in prose;
  relay field state (present/absent) embedded in case name or parenthetical. An implementer reading
  "relay field absent (action missing)" must infer that this means relay present + `Schema-governed
  action:` field absent. Inference gap: which columns contain what values is not table-scannable.
  C-19 = PARTIAL.
- C-20: C-16 status column domain block lists values with short definitions (`YES`: role has relay
  with populated field; `SILENT`: relay absent or action missing; `relay field absent`: field missing
  from relay). No explicit provenance column (which relay field is read), domain boundary (what the
  value asserts about the bijection), or behavior consequence (what happens at the gate). A table
  reader cannot independently audit provenance or behavior from the table alone. C-20 = FAIL.

**v16 R5 variation axes**:
- **Output format (C-19)**: Evidence source column population algorithm replaced with five-case
  closed table -- relay state columns + field present columns + A/B status + A/B Evidence source
  cell content, one case per row (V-01)
- **Lifecycle emphasis (C-18)**: Phase 3 gate carry-forward changed from bold-prose template
  notation to fenced structural labeled block with literal gate value (V-02)
- **Output format (C-20)**: Pre-table semantic block added before Role Bijection Table, explaining
  provenance, domain, and behavior consequence per domain value in columns A and B (V-03)

**Combined variations**:
- V-04: C-18 + C-19 (fenced gate block + five-case closed table)
- V-05: C-18 + C-19 + C-20 (all three new criteria -- complete v16 target)

All five inherit the full R4 V-05 architecture (C-01 through C-17 PASS). What varies per V-0N:
only the C-18/C-19/C-20 structural mechanism.

---

## V-01 -- Single axis: Output format (C-19: five-case closed table for Evidence source population)

**Axis**: Output format -- the Evidence source column population algorithm at Phase 2.5 is
restructured from a five-bullet-point list into a five-case closed table. The table carries
dedicated columns for: case name, Execute relay present flag, `Schema-governed action:` field
present flag, `Binding Summary row:` field present flag, resulting A status, resulting B status,
A Evidence source cell content (exact string), and B Evidence source cell content (exact string).
Each row is complete: all relay state, field state, status outcome, and exact cell content are
visible in one table row without parsing prose. The five cases cover the exhaustive space: no
additional cases exist. The table is the implementation specification; no auxiliary prose rules
are needed.

**Hypothesis**: R4 V-05 bullet-list population rules named each case but embedded the relay field
state in case names or parentheticals ("relay field absent (action missing)"), requiring the
implementer to infer which columns are present/absent. C-19 closes this inference gap by making
relay and field states explicit table columns -- an implementer reads left-to-right across the
row and has all information to populate the status cells and Evidence source cells. The five-case
table also makes exhaustiveness visible: exactly five rows, no overlap, no gaps. Risk: an
eight-column table is wide in markdown; the closed-world claim (only five cases) must be stated
explicitly so an evaluator knows the table is not illustrative but exhaustive.

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
at Phase 2.5 -- each row carries an Evidence source column populated by a five-case closed table
algorithm naming the relay fields from which Direction A and Direction B status values were read
(C-15/C-19). Status columns A and B carry formal three-value domain definitions: A ∈ {YES,
SILENT, relay field absent}; B ∈ {YES, UNDECLARED, relay field absent} -- all three values
inline in status cells, no annotation (C-16). Three defect classes trigger Phase 3 BLOCKED
coequal: SILENT, UNDECLARED, relay field absent -- no asymmetric treatment (C-17). Phase 3
opens with gate result as structural element. Verdict cites Phase 2.5 result only.

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-19 axis: five-case closed table for Evidence source population)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

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

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

**Evidence source column population -- five-case closed table (C-19)**:

This table is exhaustive: exactly five cases cover the complete space of relay/field state
combinations. No additional cases exist. Populate the Evidence source column by finding the
matching row and copying the A Evidence source and B Evidence source cell content.

| Case | Relay present? | `Schema-governed action:` present? | `Binding Summary row:` present? | A status | B status | A Evidence source (exact cell content) | B Evidence source (exact cell content) |
|------|---------------|-------------------------------------|----------------------------------|----------|----------|----------------------------------------|----------------------------------------|
| Standard | YES | YES | YES | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | NO | N/A -- no relay | YES (in Binding Summary) | SILENT | YES | `no relay (Binding Summary declares absent)` | `Binding Summary row:` relay field |
| Relay field absent (A) | YES | NO -- field missing | YES | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| Relay field absent (B) | YES | YES | NO -- field missing | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | YES | YES | NO -- no Binding Summary entry | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary row` |

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column from five-case table -- C-15/C-19; three-value status column domains -- C-16):

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

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per five-case table,
no relay fields absent).

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

#### C-11 through C-17 + C-19 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section is FAIL for C-13.

**C-11 through C-17 and C-19 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

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
**C-19: PASS** (Evidence source column population algorithm expressed as five-case closed table
at Phase 2.5; each row names relay state, field state, A/B status, and exact Evidence source cell
content; five cases are exhaustive -- no additional cases declared; population rule is table-lookup,
not inference from prose).

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

## V-02 -- Single axis: Lifecycle emphasis (C-18: standalone structural labeled block for Phase 3 gate carry-forward)

**Axis**: Lifecycle emphasis -- Phase 3's gate carry-forward is changed from a bold-formatted
prose line with template notation (`**-> GATE RESULT: ... = {{PASS}}.**`) to a fenced code block
containing a literal-value labeled element. The block appears as the FIRST structural item in
Phase 3, before any step, before any prose. The gate value is literal (`PASS` or `BLOCKED`) --
not a template placeholder. No surrounding prose wraps the block. The block stands alone as a
machine-scannable element: a parser can extract the gate status by reading the `-> GATE RESULT:`
block without parsing markdown formatting or expanding template variables.

**Hypothesis**: R4 V-05 used `**-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = {{PASS}}.**`
which places the `-> GATE RESULT:` label (satisfying C-17's location requirement) but wraps it in
bold prose with a template variable. C-18 requires the gate status to be machine-readable and
scannable WITHOUT parsing body prose. A fenced code block achieves this: the block is structurally
distinct from prose, the value is literal, and no markdown rendering is needed to read the gate
status. Risk: "fenced code block" vs. "bold line" is a rendering distinction, not a semantic one;
the evaluator must recognize that C-18's "machine-readable labeled block" implies structural
distinctness from surrounding prose, which a fenced code block achieves and a bold inline sentence
does not. Secondary risk: if Phase 3 carries additional prose after the gate block ("Phase 3 begins
on PASS. Gate result carried forward..."), this prose may obscure the structural boundary. V-02
removes all prose following the gate block -- the block alone is sufficient.

[Uses R4 V-05 Phase 2.5 architecture without five-case closed table (C-19 not on this axis)
and without pre-table semantic block (C-20 not on this axis).]

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix preamble as V-01 -- 5 schemas, C-11 through C-17 invariants. C-18 note
added to C-11 preamble:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded. Assembled into compact merged Role Bijection Table at Phase 2.5.
Status columns A and B carry three-value domain definitions: A ∈ {YES, SILENT, relay field
absent}; B ∈ {YES, UNDECLARED, relay field absent} (C-16). Each row carries Evidence source
column naming relay fields (C-15). Three defect classes trigger Phase 3 BLOCKED coequal (C-17).
Phase 3 opens with gate result as fenced structural labeled block -- machine-readable, literal
value, no template notation, no prose wrapping (C-18). Verdict cites Phase 2.5 result only.

[Schema table, biconditional definitions, sub-step ordering table: same as V-01.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01 -- all 5 rows confirmed. Direction A: HOLDS.]

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-18 axis: fenced structural block for Phase 3; Phase 2.5 unchanged from R4 V-05)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

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

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column -- C-15; three-value status column domains -- C-16):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [relay field]; B: [relay field] |

Defect declarations (for any non-YES value):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [field name]." (relay field absent)

**Biconditional hold summary** (closes the table -- C-12):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: column A = YES for all rows | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: column B = YES for all rows | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per row).

**BLOCKED language (C-17 unified)**:

If any A ≠ YES or B ≠ YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

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

#### C-11 through C-17 + C-18 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run. A bijection audit appearing
only in this section is FAIL for C-13.

**C-11 through C-17 and C-18 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

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
**C-16: PASS** (three-value status column domains inline in column definitions; all three values
in status cells -- no annotation or separate column).
**C-17: PASS** (relay field absent BLOCKED coequal; BLOCKED message enumerates all three classes;
Phase 3 carries gate result forward as structural `-> GATE RESULT:` element in opening).
**C-18: PASS** (Phase 3 gate carry-forward appears as fenced code block `-> GATE RESULT: Phase
2.5 Role Bijection Checkpoint = PASS.` -- literal gate value, no template notation, no prose
wrapping, first structural item before any step content; gate status machine-readable without
parsing markdown formatting or template variables).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Output format (C-20: pre-table semantic block explaining domain value meanings)

**Axis**: Output format -- before the compact merged Role Bijection Table, a co-located semantic
block is added. The block explains the meaning of each domain value in both status columns --
not as a domain list (C-16 already provides that) but as a semantic specification of what each
value implies for provenance, domain boundary, and behavior consequence. Each value entry names:
(1) which relay field is read to determine this status, (2) what the value asserts about the
relationship between the role's Binding Summary declaration and its Execute relay, and (3) what
the bijection consequence is (direction holds / violated / indeterminate). The block enables
independent auditability: a reader of the table can determine the full meaning of every status
cell without consulting other sections.

**Hypothesis**: C-16 defined the three-value domain per column but provided only short operational
definitions ("YES: role has Execute relay with populated field"; "SILENT: relay absent or action
missing"). An auditor reading only the table cannot determine: what relay field was read to
produce this status? What does SILENT imply about direction A's claim? Is relay field absent a
direction-A violation or an indeterminate state? C-20 makes these semantic dimensions explicit
at the table surface. The distinction from C-16: C-16 names the domain values; C-20 explains
what each value means in terms of provenance, bijection domain, and behavior. Risk: the semantic
block may grow verbose; each entry must be specific enough to enable independent auditability
without repeating the Phase 2.5 defect class definitions verbatim.

[Uses R4 V-05 Phase 2.5 architecture without five-case closed table (C-19 not on this axis)
and without fenced gate block (C-18 not on this axis).]

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix preamble as V-01 -- 5 schemas, C-11 through C-17 invariants. C-20 note
added to C-11 preamble:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded. Assembled into compact merged Role Bijection Table at Phase 2.5.
Status columns A and B carry three-value domain definitions (C-16). Each row carries Evidence
source column naming relay fields (C-15). The table is preceded by a co-located semantic block
explaining provenance, domain boundary, and behavior consequence per domain value per column,
enabling independent auditability at the table surface (C-20). Three defect classes trigger
Phase 3 BLOCKED coequal (C-17). Phase 3 opens with gate result as structural element. Verdict
cites Phase 2.5 result only.

[Schema table, biconditional definitions, sub-step ordering table: same as V-01.]
[Direction A, Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup: same as V-01.]
[Phase 2 Execute: same relay-seeded structure as V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-20 axis: pre-table semantic block for domain value meanings)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. BLOCKED immediately.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:`
   field missing from relay. BLOCKED immediately -- coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate status cells directly -- no annotation, footnote, or separate column.

**Evidence source column population rules (C-15)**:
- Standard row: `A: Schema-governed action: relay field; B: Binding Summary row: relay field`
- SILENT row: `A: no relay (Binding Summary declares absent); B: Binding Summary row: relay field`
- relay field absent (action missing): `A: Schema-governed action: absent from relay; B: Binding Summary row: relay field`
- relay field absent (binding missing): `A: Schema-governed action: relay field; B: Binding Summary row: absent from relay`
- UNDECLARED row: `A: Schema-governed action: relay field; B: no Binding Summary row`

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
  Direction A seed was not planted. Bijection direction A indeterminate (cannot confirm). Gate
  consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

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
  Direction B seed was not planted. Bijection direction B indeterminate (cannot confirm). Gate
  consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column -- C-15; three-value status column domains -- C-16; semantic block above -- C-20):

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

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, Evidence source populated per row, no relay
fields absent).

**BLOCKED language (C-17 unified)**:

If any A ≠ YES or B ≠ YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

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

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### C-11 through C-17 + C-20 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run.

**C-11 through C-17 and C-20 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no defects).
**C-12: PASS** (compact merged table, biconditional hold summary at Phase 2.5).
**C-13: PASS** (Phase 2.5 named checkpoint; BLOCKED language; Verdict cites, does not re-run).
**C-14: PASS** (relay-seeded fields; three defect classes; relay-sourced evidence).
**C-15: PASS** (Evidence source column per row; populated at Phase 2.5 -- no reconstruction).
**C-16: PASS** (three-value status column domains inline; all three values in status cells).
**C-17: PASS** (relay field absent BLOCKED coequal; BLOCKED message enumerates all three classes;
Phase 3 carries gate result forward as structural `-> GATE RESULT:` element in opening).
**C-20: PASS** (pre-table semantic block co-located before Role Bijection Table; each domain value
in columns A and B has an entry naming relay field read, bijection claim made, and behavior
consequence at Phase 2.5 gate; block enables independent auditability of provenance, domain, and
behavior without consulting other sections).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-18 + C-19 (fenced gate block + five-case closed table)

**Axes**:
- Lifecycle emphasis (C-18): Phase 3 gate carry-forward as fenced structural labeled block with
  literal gate value.
- Output format (C-19): Evidence source column population algorithm as five-case closed table.

No pre-table semantic block (C-20 not on this axis).

**Hypothesis**: V-02 establishes the fenced gate block (C-18). V-01 establishes the five-case
closed table (C-19). V-04 combines them. The combination tests whether the two mechanisms are
compatible: both target Phase 2.5 (the five-case table is in Phase 2.5; the fenced block is in
Phase 3 immediately after Phase 2.5). The structural boundary between Phase 2.5's population
algorithm and Phase 3's gate carry-forward is tested -- does the fenced code block in Phase 3
remain distinct from the five-case table in Phase 2.5? Risk: the five-case table ends Phase 2.5;
the fenced code block opens Phase 3. The phase boundary must remain explicit between them.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix preamble as V-01 -- 5 schemas. C-11 preamble updated for C-18 + C-19:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded. Assembled into compact merged Role Bijection Table at Phase 2.5.
Status columns carry three-value domain definitions (C-16). Each row carries Evidence source
column populated by five-case closed table algorithm (C-15/C-19). Three defect classes trigger
Phase 3 BLOCKED coequal (C-17). Phase 3 opens with fenced structural labeled block -- literal
gate value, machine-readable (C-18). Verdict cites Phase 2.5 result only.

[Schema table, biconditional definitions, sub-step ordering: same as V-01.]
[Direction A, Binding Summary, Stage 1, SA-TO-SG PROMOTION, Phase 1 Setup: same as V-01.]
[Phase 2 Execute: same relay-seeded structure as V-01.]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-18 + C-19 axes)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

**Three defect classes -- coequal BLOCKED triggers (C-17 explicit statement)**:

relay field absent triggers Phase 3 BLOCKED coequal with SILENT and UNDECLARED. No asymmetric
treatment: all three defect classes block Phase 3 immediately on discovery. SILENT, UNDECLARED,
and relay field absent are equivalent blocking conditions.

1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no
   schema-governed action. BLOCKED immediately on discovery.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. BLOCKED immediately.
3. **relay field absent**: relay exists; seeded field missing from relay. BLOCKED immediately --
   coequal with SILENT and UNDECLARED.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate the status cell directly -- no annotation, footnote, or separate column.

**Evidence source column population -- five-case closed table (C-19)**:

This table is exhaustive: exactly five cases cover the complete space of relay/field state
combinations. Populate the Evidence source column by finding the matching row and copying the
A Evidence source and B Evidence source cell content exactly.

| Case | Relay present? | `Schema-governed action:` present? | `Binding Summary row:` present? | A status | B status | A Evidence source (exact cell content) | B Evidence source (exact cell content) |
|------|---------------|-------------------------------------|----------------------------------|----------|----------|----------------------------------------|----------------------------------------|
| Standard | YES | YES | YES | YES | YES | `Schema-governed action:` relay field | `Binding Summary row:` relay field |
| SILENT | NO | N/A -- no relay | YES (in Binding Summary) | SILENT | YES | `no relay (Binding Summary declares absent)` | `Binding Summary row:` relay field |
| Relay field absent (A) | YES | NO -- field missing | YES | relay field absent | YES | `Schema-governed action: absent from relay` | `Binding Summary row:` relay field |
| Relay field absent (B) | YES | YES | NO -- field missing | YES | relay field absent | `Schema-governed action:` relay field | `Binding Summary row: absent from relay` |
| UNDECLARED | YES | YES | NO -- no Binding Summary entry | YES | UNDECLARED | `Schema-governed action:` relay field | `no Binding Summary row` |

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source
column from five-case table -- C-15/C-19; three-value status column domains -- C-16):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute {YES \| SILENT \| relay field absent} | B: Declared in Summary {YES \| UNDECLARED \| relay field absent} | Evidence source |
|------|--------------------|--------------------|-------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-----------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay or "none"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent | A: [per five-case table]; B: [per five-case table] |

Defect declarations (for any non-YES value):
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
table, no relay fields absent).

**BLOCKED language (C-17 unified)**:

If any A ≠ YES or B ≠ YES (coequal blocking condition applies):
**Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field absent.
Name the role relay and the specific defect. Resolve before proceeding.]**

The BLOCKED condition applies coequally to all three defect classes. No asymmetric treatment.

---

#### Phase 3 -- Findings

```
-> GATE RESULT: Phase 2.5 Role Bijection Checkpoint = PASS.
```

##### Step 3a -- Severity Legend

[Same Step 3a as V-01.]

##### Step 3b -- Findings Table

[Same Step 3b as V-01.]

##### Step 3c -- Enforcement Gates

[Same Step 3c as V-01.]

##### Step 3d -- Channel Taxonomy Activation

[Same Step 3d as V-01.]

#### Phase 4 -- Amend

[Same Phase 4 as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5.]

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### C-11 through C-17 + C-18 + C-19 Citation

**C-13 rule**: Verdict cites Phase 2.5 result; does not re-run.

**C-11 through C-19 verification (C-20 excluded -- not on this axis): cited from Phase 2.5.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects: [list or "none"].

**C-11: PASS.** (Phase 2.5 gate = PASS, both directions HOLDS.)
**C-12: PASS.** (compact merged table, biconditional hold summary.)
**C-13: PASS.** (Phase 2.5 checkpoint, BLOCKED language, Verdict cites.)
**C-14: PASS.** (relay-seeded fields, three defect classes, relay-sourced evidence.)
**C-15: PASS.** (Evidence source column per row; populated at Phase 2.5 -- no reconstruction.)
**C-16: PASS.** (Three-value status column domains inline; all three values in status cells.)
**C-17: PASS.** (relay field absent BLOCKED coequal; BLOCKED message enumerates all three classes;
Phase 3 carries gate result forward as structural element in opening.)
**C-18: PASS.** (Phase 3 opens with fenced code block `-> GATE RESULT: Phase 2.5 Role Bijection
Checkpoint = PASS.` -- literal gate value, no template notation, no prose wrapping, first
structural item before any step content; gate status machine-readable without parsing formatting.)
**C-19: PASS.** (Evidence source column population algorithm expressed as five-case closed table;
each row names relay state, field state, A/B status, and exact Evidence source cell content;
five cases exhaustive -- no additional cases declared; population rule is table-lookup.)

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-18 + C-19 + C-20 (all three new criteria -- complete v16 target)

**Axes**:
- Lifecycle emphasis (C-18): Phase 3 gate carry-forward as fenced structural labeled block with
  literal gate value.
- Output format (C-19): Evidence source column population algorithm as five-case closed table.
- Output format (C-20): Pre-table semantic block explaining provenance, domain, and behavior
  consequence per domain value per status column.

**Hypothesis**: V-04 establishes C-18 + C-19. V-03 establishes C-20. V-05 combines all three.
The design principle: C-19 specifies HOW to populate the Evidence source column (algorithm);
C-20 specifies WHAT each status value MEANS (semantics); C-18 specifies HOW to carry the gate
result into Phase 3 (format). All three are complementary -- they target different auditable
properties at the Phase 2.5/Phase 3 boundary. The co-location test: Phase 2.5 now carries
coequal-BLOCKED statement (C-17), status column domain definition (C-16), status column semantics
block (C-20), five-case closed table algorithm (C-19), Role Bijection Table, and biconditional
hold summary. Phase 3 opens with fenced gate block (C-18). Risk: Phase 2.5 is the highest
specification-density section. V-05 represents the maximum structural load for this area. The
ordering principle is: semantics before algorithm before table -- semantic block (C-20) -> five-
case algorithm (C-19) -> table (C-12).

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
source column populated by five-case closed table algorithm naming relay field content per case
(C-15/C-19). The table is preceded by a co-located semantic block explaining provenance, domain
boundary, and behavior consequence per domain value (C-20). Three defect classes trigger Phase 3
BLOCKED coequal: SILENT, UNDECLARED, relay field absent -- no asymmetric treatment (C-17).
Phase 3 opens with fenced structural labeled block -- literal gate value, machine-readable (C-18).
Verdict cites Phase 2.5 result only; does not re-run.

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

**Schema 4**: G-1: Step 3b >=2 distinct Source types. G-2: no two same-Source findings carry
identical Action. G-3: all Step 3b entries use only {P1, P2, P3}.

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-18 + C-19 + C-20: fenced gate block, five-case table, pre-table semantic block)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 cannot begin
until this checkpoint produces a gate result.

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

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Status column domain definition (C-16)**:

Column A -- `A: Acts in Execute` -- value domain: {`YES`, `SILENT`, `relay field absent`}.
Column B -- `B: Declared in Summary` -- value domain: {`YES`, `UNDECLARED`, `relay field absent`}.
Values populate status cells directly -- no annotation, footnote, or separate column.

**Role Bijection Table -- status column semantics (C-20)**:

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
  absent from relay body. Claim: relay exists but is structurally incomplete -- Direction A seed not
  planted. Direction A indeterminate. Gate consequence: BLOCKED -- coequal with SILENT and UNDECLARED.

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

**Evidence source column population -- five-case closed table (C-19)**:

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

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged -- C-12; relay-assembled -- C-14; Evidence source column
from five-case table -- C-15/C-19; three-value status column domains -- C-16; semantic block
above -- C-20):

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
table, no relay fields absent).

**BLOCKED language (C-17 unified -- all three defect classes enumerated explicitly)**:

If any A ≠ YES or B ≠ YES (coequal blocking condition applies):
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

#### C-11 through C-20 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section is FAIL for C-13.

**C-11 through C-20 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

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
opening, not only in Verdict).
**C-18: PASS** (Phase 3 gate carry-forward appears as fenced code block `-> GATE RESULT: Phase
2.5 Role Bijection Checkpoint = PASS.` -- literal gate value (`PASS` or `BLOCKED`), no template
notation, no prose wrapping, no bold formatting; first structural item before any step content;
gate status machine-readable and scannable without parsing markdown formatting or template
variables; satisfies C-17 location requirement and C-18 format requirement independently).
**C-19: PASS** (Evidence source column population algorithm expressed as five-case closed table
at Phase 2.5; each row names relay state columns, field present flags, resulting A/B status, and
exact Evidence source cell content for both A and B; five cases declared exhaustive -- no
additional cases exist; population rule is table-lookup with no prose inference required).
**C-20: PASS** (pre-table semantic block co-located immediately before Role Bijection Table;
each domain value in columns A and B has an entry naming: relay field read to determine status,
bijection claim made by the value, bijection direction consequence, and gate behavior consequence;
block enables independent auditability of provenance, domain boundary, and behavior without
consulting Phase 2.5 defect class definitions or other sections; semantics block ordered before
five-case algorithm -- semantics -> algorithm -> table).

The biconditional invariant -- Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute -- is found to hold: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
