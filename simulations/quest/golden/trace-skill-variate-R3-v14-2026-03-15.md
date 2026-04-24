---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 3
rubric: trace-skill-rubric-v14-2026-03-15.md
---

# trace-skill -- Variations v14 R3 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: v13 R2 V-05 achieves C-01 through C-11 PASS under v14 scoring. v14 formalizes
three new aspirational criteria from R2 excellence signals: C-12 (compact merged Role Bijection
Table), C-13 (Phase 2.5 Role Bijection Checkpoint as a hard gate), C-14 (relay-seeded evidence
with read-and-copy assembly). R2 V-05 held all three structurally but v14 sharpens the pass
conditions: C-12 requires the biconditional hold summary to explicitly close the table and the
compact table to use labeled SILENT/UNDECLARED status columns; C-13 requires the Verdict to cite
the gate result rather than re-run the audit (bijection audit in Verdict only = FAIL for C-13);
C-14 introduces relay field absent as a third named defect class distinct from SILENT and UNDECLARED,
and requires the audit to explicitly source its evidence to relay fields.

**v13 R2 V-05 C-11/C-12/C-13/C-14 structure** (the established baseline, scored against v14):
- C-11: Role bijection invariant declared in Coverage Matrix preamble; Role Bijection Table in
  Verdict or at Phase 2.5 with both directions and defect declarations.
- C-12 (R2 V-01/V-04/V-05): compact merged table with per-row SILENT/UNDECLARED columns; V-05
  closes with direction summary but biconditional hold summary label is informal.
- C-13 (R2 V-02/V-05): Phase 2.5 checkpoint present and blocks Phase 3; V-05 Verdict cites
  result but does not name the gate-cite as the binding evidence for C-13.
- C-14 (R2 V-03/V-04/V-05): relay-seeded fields present; relay field absent defect named in
  V-04/V-05 but not formally distinguished as a third class separate from SILENT/UNDECLARED.

**v14 R3 variation axes** (three single-axis, then combined):
- **Output format**: C-12 formalized -- compact merged Role Bijection Table with explicit
  SILENT/UNDECLARED status columns and a named biconditional hold summary closing the table (V-01)
- **Lifecycle emphasis**: C-13 formalized -- Phase 2.5 gate with explicit statement that bijection
  audit in Verdict only = FAIL; Verdict section cites gate result, does not re-run (V-02)
- **Role sequence**: C-14 formalized -- relay fields named exactly as `Binding Summary row:` and
  `Schema-governed action:`; three defect classes (SILENT, UNDECLARED, relay field absent) named
  and distinguished; audit sourced explicitly to relay fields (V-03)

**Combined variations**:
- V-04: Output format + Role sequence (compact relay-assembled table, no Phase 2.5 gate)
- V-05: All three axes (Phase 2.5 gate reads relay fields to populate compact table; Verdict
  cites gate result only; three defect classes; biconditional hold summary in the checkpoint)

All five v14 R3 variations inherit the full v13 R2 V-05 architecture:
- Coverage Matrix with 5 schemas (Role-binding column, biconditional invariant preambles C-10 and C-11)
- Direction A enumeration before Stage 1 (C-10 direction a)
- Role-Schema Binding Summary before Stage 2 (C-08)
- SA-TO-SG PROMOTION as a named lifecycle event (C-04)
- Phase 3 sub-steps 3a/3b/3c/3d governed by Schema 5 (C-05, C-07)
- Schema footprint records per phase (Direction B evidence assembly, C-10 direction b)
- Compliance ledger VC-1 through VC-5 with invariant-witness cells (C-07, C-09)
- Direction B assembled in Verdict from footprint records (C-10 direction b)
- Hard-stop BLOCKED language on gate FAIL (C-05 PASS)

What varies per V-0N: only the C-11/C-12/C-13/C-14 structural mechanism.

---

## V-01 -- Single axis: Output format (C-12: compact merged Role Bijection Table, formalized)

**Axis**: Output format -- the C-11 Role Closed-World Audit uses a single compact merged Role
Bijection Table in the Verdict. Each row covers one role and answers both bijection directions
simultaneously: the Binding Summary row (Direction B), the Execute relay step (Direction A locus),
the schema-governed action evidence, and direction status columns A and B side by side with
`SILENT` / `UNDECLARED` as the defect labels for the absent direction. A named biconditional hold
summary closes the table as a final block. Two separate direction tables satisfy C-11 but fail C-12.

**Hypothesis**: v13 R2 V-01 introduced the compact table format and V-04/V-05 carried it forward.
v14 C-12 raises the bar at two points: (1) the direction status columns must use the exact labels
`SILENT` and `UNDECLARED` (not ad hoc language) so a rubric reader can identify asymmetric cases
by column value rather than by reading prose declarations; (2) a named biconditional hold summary
must explicitly close the table -- the direction summary in V-05 was present but informal. This
formalization makes C-12 an auditable format property: an evaluator checks for the SILENT/UNDECLARED
column labels, checks for the hold summary block, and checks that no separate direction tables
exist. Risk: the compact table's SILENT label in column A requires a row whose Execute relay step
is ABSENT; models may conflate SILENT (declared, absent from Execute) with a simply empty relay
field (relay exists, seeded field missing) -- the compact table, without relay seeding, cannot
distinguish these two cases. C-14 is the axis that resolves this ambiguity.

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
Execute. "Schema-governed action" means an action using a label from Schema 1 or Schema 2 as
declared in the Binding Summary for that role. Verified by the Role Bijection Table in the Verdict
(compact merged format with SILENT/UNDECLARED status columns and biconditional hold summary).
Two separate direction tables satisfy C-11 but fail C-12.

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

**Schema 5**: Step 3b is valid if and only if Step 3a complete. Step 3c valid iff Step 3b >=2
entries. Step 3d valid iff Step 3c all-PASS. Phase 4 valid iff Step 3d channel taxonomy activated.

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
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared (invariant: legend iff Schema 1 declared) | [what the legend stated] | PASS / FAIL |
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

#### Role Bijection Table (C-11 + C-12 -- Compact Merged Format)

**C-12 format**: One row per role. Direction A status column (`A: Acts in Execute`) and Direction
B status column (`B: Declared in Summary`) appear side by side on the same row. Asymmetric cases
populate the absent side with the defect label: `SILENT` in column A when a role is declared in
the Binding Summary but produced no schema-governed action in Execute; `UNDECLARED` in column B
when a role appeared in Execute with no Binding Summary entry. A biconditional hold summary block
closes the table. Two separate direction tables satisfy C-11 but fail C-12.

**Invariant (biconditional form)**: Role R is in the Binding Summary if and only if it produces
at least one schema-governed action in Phase 2 Execute.

Population rules:
- Role has Binding Summary row AND Execute relay: populate both sides from trace.
- Role has Binding Summary row but no Execute relay: `Execute relay step: ABSENT`, `A: SILENT`.
  Declare: "[role] -- Binding Summary defect: declared but produced no schema-governed action."
- Role has Execute relay but no Binding Summary row: `Binding Summary row: ABSENT`, `B: UNDECLARED`.
  Declare: "[role] -- structural defect: acted in Execute without Binding Summary entry."
- Every Binding Summary row must appear as exactly one table row.
- Every Execute relay header must appear as exactly one table row.

| Role | Binding Summary row | Execute relay step | Schema-governed action (Schema ref) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [action + Schema 1 or 2 ref, or "none / silent"] | YES / SILENT | YES / UNDECLARED |

Defect declarations (populate if any A = SILENT or B = UNDECLARED):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action."
- "[role] -- structural defect: acted in Execute without Binding Summary entry."

**Biconditional hold summary** (closes the table):

| Direction | Claim | Result |
|-----------|-------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: no SILENT entries | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: no UNDECLARED entries | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**C-11: PASS / PARTIAL / FAIL** (PASS requires both directions HOLDS with no defects).
**C-12: PASS** (compact merged table with SILENT/UNDECLARED status columns and named biconditional
hold summary present; no separate direction tables used).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (C-13: Phase 2.5 gate formalized)

**Axis**: Lifecycle emphasis -- the C-11 Role Closed-World Audit is extracted from the Verdict
and placed as a mandatory named inter-phase checkpoint, "Phase 2.5 -- Role Bijection Checkpoint,"
between Execute and Findings. Phase 3 cannot begin until Phase 2.5 produces a gate result. If
the bijection fails, Phase 3 is BLOCKED with the exact language: "Phase 3 BLOCKED: [bijection
defect]." The Verdict cites the Phase 2.5 gate result; it does not re-run the audit. A bijection
audit appearing only in the Verdict section (not at Phase 2.5) is FAIL for C-13. The checkpoint
uses two separate direction tables (satisfies C-11 but not C-12 -- this is the single-axis constraint).

**Hypothesis**: R2 V-02 introduced Phase 2.5 and R2 V-05 combined it with relay seeding and the
compact table. v14 C-13 raises the bar at two points not fully formalized in R2: (1) the exact
BLOCKED phrasing "Phase 3 BLOCKED: [bijection defect]" must appear at the gate -- ad hoc blocking
language is PARTIAL; (2) the Verdict must carry an explicit rule that re-running the audit in the
Verdict constitutes a C-13 FAIL. This makes C-13 a named protocol property: an evaluator checks
for the Phase 2.5 named section, checks for the exact BLOCKED phrasing on failure, and checks
that the Verdict section only cites the result. Risk: models trained on end-of-trace audit patterns
may insert a second bijection audit in the Verdict even after Phase 2.5 -- the explicit FAIL rule
in the Verdict citation section is the counter-instruction.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, Role-binding column, biconditional invariant preamble
for C-10. C-11 note updated:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Verified at Phase 2.5 Role Bijection Checkpoint (mandatory gate before Phase 3). If
the bijection fails, Phase 3 BLOCKED. The Verdict cites the Phase 2.5 result; it does not re-run
the audit. A bijection audit appearing only in the Verdict is FAIL for C-13.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

[Schema 1-5 biconditional definitions: same as V-01.]
[Schema 5 sub-step ordering table: same as V-01.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01 -- all 5 schemas confirmed with named phase/step references
before Stage 1 begins. Direction A: HOLDS.]

---

### Role-Schema Binding Summary

[Same Binding Summary table as V-01 -- one row per role, Schema 1 and Schema 2 bindings declared
before Stage 2.]

---

### Stage 1 -- Source-Layer Audit

[Same Stage 1 structure as V-01 -- gap audit table, relay to Stage 2, Schema footprint.]

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

[Same as V-01 -- per SA gap: promote or retain, reason, label lock, Schema footprint.]

#### Phase 1 -- Setup

[Same as V-01 -- confirmed inputs, per-role schema binding and gap attribution, carry-forward,
Schema footprint.]

#### Phase 2 -- Execute

[Same as V-01 -- role relay records with Schema 2 compliance field, artifact production,
carry-forward, Schema footprint. No relay-seeded C-11 fields in V-02 (single axis for C-13 only).]

---

#### Phase 2.5 -- Role Bijection Checkpoint (C-13 axis: hard enforcement gate)

**Named inter-phase checkpoint**: Phase 2.5 runs immediately after Phase 2 Execute completes
and before Phase 3 Findings begins. Phase 3 cannot begin until Phase 2.5 produces a gate result.
This checkpoint is mandatory -- it cannot be deferred to the Verdict.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

---

**Direction A: Binding Summary -> Execute** (no SILENT roles)

For each role declared in the Binding Summary, name the schema-governed action it produced in
Phase 2 Execute. A role with no observable schema-governed action is a SILENT role.

| Role (Binding Summary row) | Schema-governed action in Execute | Evidence locus (relay field or artifact section) | Silent? |
|----------------------------|----------------------------------|------------------------------------------------|---------|
| [role] | [action using Schema 1 or 2 labels as declared in Binding Summary] | [where in the relay this action is observed] | YES / NO |

SILENT roles found: "[role] -- Binding Summary defect: declared but produced no schema-governed
action in Execute."

---

**Direction B: Execute -> Binding Summary** (no UNDECLARED roles)

For each role appearing in Phase 2 Execute (by role relay header), confirm a Binding Summary
row exists.

| Role (Execute relay) | Binding Summary row | Declared? |
|----------------------|--------------------|-----------|
| [role] | [row index] | YES / NO |

UNDECLARED roles found: "[role] -- structural defect: acted in Execute with no Binding Summary entry."

---

**Phase 2.5 gate result**:

| Direction | Claim | Result |
|-----------|-------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: no SILENT roles | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: no UNDECLARED roles | HOLDS / DEFECTS: [list] |

**ROLE BIJECTION: PASS** (both directions HOLD, no defects found).

If FAIL: **Phase 3 BLOCKED: [bijection defect -- name the silent or undeclared role(s) and
classify as Binding Summary defect or structural defect. Resolve before proceeding.]**

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

#### C-11 / C-13 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
The Verdict cites the Phase 2.5 result; it does not re-run the bijection audit. A bijection
audit appearing only in this Verdict section -- without a Phase 2.5 checkpoint earlier in the
trace -- is FAIL for C-13.

**C-11 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

| Direction | Phase 2.5 gate result | Defects |
|-----------|-----------------------|---------|
| A (Binding Summary -> Execute) | HOLDS / DEFECTS | [list or "none"] |
| B (Execute -> Binding Summary) | HOLDS / DEFECTS | [list or "none"] |

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no defects).
**C-13: PASS** (Phase 2.5 named checkpoint present; BLOCKED language used on failure; Verdict
cites, does not re-run).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Role sequence (C-14: relay-seeded evidence, formalized)

**Axis**: Role sequence -- C-11 evidence is captured at the point of production. Each Phase 2
role relay gains two required seeded fields beyond the v12 V-05 baseline: `Binding Summary row:`
(named exactly; Direction B seed -- maps this Execute relay to its Binding Summary declaration)
and `Schema-governed action:` (named exactly; Direction A seed -- names the specific schema-labeled
action this role produced). The Verdict assembles these relay fields into the Direction A and
Direction B audit tables. A relay where a seeded field is missing introduces a third defect class,
`relay field absent` (the relay exists but the seeded field is missing), distinct from SILENT
(role declared but absent from Execute) and UNDECLARED (role present in Execute without
declaration). The audit explicitly names its evidence source as relay fields -- no end-of-trace
reconstruction. This variation uses two separate direction tables (C-11 compliant, C-12 not
satisfied).

**Hypothesis**: R2 V-03 introduced relay-seeded fields and R2 V-04/V-05 carried them forward.
v14 C-14 formalizes three properties not fully specified in R2: (1) the exact field names
`Binding Summary row:` and `Schema-governed action:` must appear in each relay (not paraphrases);
(2) the `relay field absent` defect class must be explicitly named and distinguished from SILENT
and UNDECLARED -- in R2 V-04/V-05 it was present but not formally named as a third class; (3)
the audit section must include a statement that evidence is sourced from relay fields rather than
reconstructed. Risk: the exact-field-name requirement may be over-specified for a prompt; models
that paraphrase the field name ("Binding row:" vs "Binding Summary row:") may still satisfy the
intent. The rubric scores the structural presence of the defect class distinction, not the exact
string, but the prompt should use exact names to maximize model compliance.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- 5 schemas, Role-binding column, biconditional invariant preamble
for C-10. C-11 note updated:]

A second closed-world invariant governs the Role-Schema Binding Summary (C-11): Role R is in
the Binding Summary if and only if it produces at least one schema-governed action in Phase 2
Execute. Evidence relay-seeded: each Execute relay carries `Binding Summary row:` (Direction B
seed) and `Schema-governed action:` (Direction A seed). The Verdict assembles these fields into
the audit tables -- no end-of-trace reconstruction. Three defect classes: SILENT (declared role
absent from Execute), UNDECLARED (Execute role absent from Binding Summary), relay field absent
(relay exists, seeded field missing).

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

[Schema 1-5 biconditional definitions: same as V-01.]
[Schema 5 sub-step ordering table: same as V-01.]

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

#### Phase 2 -- Execute (C-14 axis: relay-seeded C-11 evidence)

Produce: `{topic}-skill-trace-{date}.md`. Three required fields in every relay: Schema 2
compliance, `Binding Summary row:` (Direction B seed), `Schema-governed action:` (Direction A
seed). A relay missing either seeded field introduces a `relay field absent` defect -- distinct
from SILENT (role declared but not in Execute) and UNDECLARED (role in Execute without declaration).

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all SA/SG/EG/QO: YES / NO
- **Binding Summary row**: [row index from Role-Schema Binding Summary table] (Direction B seed)
- **Schema-governed action**: [the specific action this role produced using Schema 1 or Schema 2
  labels as declared in its Binding Summary row -- e.g., "labeled F-01 as EG (Schema 2 Source
  label)" or "assigned P2 severity (Schema 1 label)"]
  **Schema ref**: Schema 1 / Schema 2
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps: [EG-NN list or "none"]

A relay where no schema-governed action can be named must declare: "No schema-governed action
found for [role] -- candidate SILENT role. Binding Summary requires review."
A relay with a missing seeded field must declare: "[field name] absent from relay -- relay field
absent defect."

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in role relays), Schema 1
(Severity labels on EG findings per role).

---

[Phase 3 Steps 3a/3b/3c/3d: same as V-01.]
[Phase 4 Amend: same as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5 with invariant-witness cells.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01 -- assembled from Schema footprint records.]

**C-10: PASS.**

---

#### Role Closed-World Audit (C-11 + C-14 -- Relay-Assembled, Three Defect Classes)

**Evidence source**: relay fields from Phase 2 Execute. This audit reads relay fields directly --
no end-of-trace reconstruction. Relay field presence is a precondition for both direction tables.

**Three defect classes** (named and distinguished):
1. **SILENT**: Role has a Binding Summary row but produced no schema-governed action in Execute
   (Execute relay absent, or relay present with no schema-governed action field value).
2. **UNDECLARED**: Role appeared in an Execute relay with no corresponding Binding Summary row.
3. **relay field absent**: Role has an Execute relay, but the relay is missing one or both seeded
   fields (`Binding Summary row:` or `Schema-governed action:`). Distinct from SILENT and
   UNDECLARED: the relay exists; only the seeded field is missing.

---

**Direction A: Binding Summary -> Execute**
(assembled from `Schema-governed action:` relay fields)

For each role in the Binding Summary, read its Execute relay's `Schema-governed action:` field.

| Role (Binding Summary) | Schema-governed action (from relay field) | Schema ref | Acts in Execute? |
|------------------------|------------------------------------------|------------|-----------------|
| [role] | [copied from relay `Schema-governed action:` field] | Schema 1 / 2 | YES / SILENT / relay field absent |

---

**Direction B: Execute -> Binding Summary**
(assembled from `Binding Summary row:` relay fields)

For each Execute relay, read its `Binding Summary row:` field.

| Role (Execute relay) | Binding Summary row (from relay field) | Declared? |
|----------------------|---------------------------------------|-----------|
| [role] | [copied from relay `Binding Summary row:` field] | YES / UNDECLARED / relay field absent |

---

**Assembly validation**: Every Binding Summary row has a corresponding Direction A table row.
Every Execute relay has a corresponding Direction B table row. A role relay with a missing seeded
field is named explicitly: "[relay name] -- relay-seeded field missing: [Binding Summary row /
Schema-governed action]."

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role has a schema-governed action relay field | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting relay has a Binding Summary row relay field | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

**C-11: PASS / PARTIAL / FAIL.**
**C-14: PASS** (relay-seeded fields `Binding Summary row:` and `Schema-governed action:` present
in every Execute relay; three defect classes -- SILENT, UNDECLARED, relay field absent -- named
and distinguished; audit explicitly sourced to relay fields; no end-of-trace reconstruction).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-12 + C-14 (compact relay-assembled table, no Phase 2.5 gate)

**Axes**:
- Role sequence (C-14): relay-seeded fields `Binding Summary row:` and `Schema-governed action:`
  captured in each Phase 2 role relay at production time; three defect classes named (SILENT,
  UNDECLARED, relay field absent); audit sourced explicitly to relay fields.
- Output format (C-12): compact merged Role Bijection Table in the Verdict populated directly
  from the relay-seeded fields -- each table row reads the two relay fields for its role; the
  SILENT/UNDECLARED status columns are populated from relay evidence; biconditional hold summary
  closes the table.

No Phase 2.5 gate (C-13 not satisfied -- audit remains in the Verdict).

**Hypothesis**: V-01 introduced the compact table but relied on manual end-of-trace evidence
assembly. V-03 introduced relay seeding but used two separate direction tables. V-04 combines
them: the compact table is populated mechanically from relay fields, making each row a direct
read-and-copy from exactly two relay fields per role. This tests whether the compact format is
fully compatible with relay assembly, including the asymmetric case (Binding Summary row present
but no Execute relay -- row is populated from Binding Summary directly; A = SILENT). The three
defect classes must map cleanly onto the compact table: SILENT in column A, UNDECLARED in column
B, relay field absent populating the schema-governed-action cell with the defect label and
affecting the corresponding direction status column. Risk: relay field absent and SILENT occupy
related positions (both affect column A direction status when the action field is missing) and
the compact table must distinguish them by cell content.

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
Execute. Evidence relay-seeded: each Execute relay carries `Binding Summary row:` (Direction B
seed) and `Schema-governed action:` (Direction A seed). Assembled into compact merged Role
Bijection Table in the Verdict (SILENT/UNDECLARED columns, biconditional hold summary). Three
defect classes: SILENT, UNDECLARED, relay field absent.

[Schema table, biconditional definitions, and sub-step ordering table: same as V-01.]

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

Produce: `{topic}-skill-trace-{date}.md`. Three required fields in every relay: Schema 2
compliance, `Binding Summary row:` (Direction B seed for compact table), `Schema-governed action:`
(Direction A seed for compact table). A relay missing either seeded field introduces a `relay
field absent` defect.

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

A relay with no schema-governed action declares: "No schema-governed action -- candidate SILENT role."
A relay with a missing seeded field declares: "[field name] absent -- relay field absent defect."

Execute carry-forward: [artifact: `{{path}}`], [EG added: `{{list}}`].

**Schema footprint -- Phase 2 Execute**: Schema 2 (Source labels in relays), Schema 1 (Severity
labels on EG findings).

---

[Phase 3 Steps 3a/3b/3c/3d: same as V-01.]
[Phase 4 Amend: same as V-01.]

---

### Verdict (Phase 5)

#### Compliance Ledger

[Same compliance ledger as V-01 -- VC-1 through VC-5 with invariant-witness cells.]

---

#### Closed-World Verification -- Direction B

[Same Direction B assembly as V-01.]

**C-10: PASS.**

---

#### Role Bijection Table (C-11 + C-12 + C-14 -- Compact Merged, Relay-Assembled)

**Evidence source**: relay fields from Phase 2 Execute. Each row reads `Binding Summary row:` and
`Schema-governed action:` fields from the corresponding Execute relay. No end-of-trace reconstruction.

**Three defect classes**:
1. **SILENT**: role has Binding Summary row; Execute relay absent or relay carries no action.
   Column A: `SILENT`. Declare: "[role] -- Binding Summary defect: declared but absent from Execute."
2. **UNDECLARED**: role has Execute relay; no Binding Summary row.
   Column B: `UNDECLARED`. Declare: "[role] -- structural defect: acted without Binding Summary entry."
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:` field
   missing from relay. Populate the relevant cell with `relay field absent`. Declare: "[relay] --
   relay-seeded field missing: [field name]."

Population rules:
- Execute relay present: read `Binding Summary row:` field -> column B source; read
  `Schema-governed action:` field -> Schema-governed action cell. If `Schema-governed action:`
  missing: A = `relay field absent`. If `Binding Summary row:` missing: B = `relay field absent`.
- Binding Summary row present, no Execute relay: `Execute relay step: ABSENT`, A = `SILENT`.
- Execute relay present, no Binding Summary row: `Binding Summary row: ABSENT`, B = `UNDECLARED`.

**Invariant (biconditional form)**: Role R is in the Binding Summary if and only if it produces
at least one schema-governed action in Phase 2 Execute.

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay field, or "none / silent / relay field absent"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent |

Defect declarations (for any A != YES or B != YES):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action."
- "[role] -- structural defect: acted in Execute without Binding Summary entry."
- "[relay] -- relay-seeded field missing: [Binding Summary row / Schema-governed action]."

**Biconditional hold summary** (closes the table):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: no SILENT or relay field absent in column A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: no UNDECLARED or relay field absent in column B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**C-11: PASS / PARTIAL / FAIL.**
**C-12: PASS** (compact merged table with SILENT/UNDECLARED status columns and named biconditional
hold summary; no separate direction tables).
**C-14: PASS** (relay-seeded fields `Binding Summary row:` and `Schema-governed action:` present;
three defect classes named and distinguished; audit sourced to relay fields).

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-12 + C-13 + C-14 (all three new criteria)

**Axes**:
- Role sequence (C-14): relay-seeded `Binding Summary row:` and `Schema-governed action:` fields
  in each Phase 2 relay; three defect classes named (SILENT, UNDECLARED, relay field absent);
  audit explicitly sourced to relay fields.
- Lifecycle emphasis (C-13): Phase 2.5 Role Bijection Checkpoint reads relay-seeded fields to
  populate the Role Bijection Table; FAIL produces "Phase 3 BLOCKED: [defect]"; Phase 3 carries
  forward the gate result; Verdict cites Phase 2.5 result only -- no re-run.
- Output format (C-12): compact merged Role Bijection Table at Phase 2.5 with per-row
  SILENT/UNDECLARED status columns and named biconditional hold summary closing the table.

**Hypothesis**: V-04 combines relay seeding with compact presentation but places the audit in the
Verdict (late, after all phases complete). V-05 moves the audit to Phase 2.5 (immediately after
Execute, before findings consolidate) while retaining relay seeding (V-03) and compact presentation
(V-01). Phase 2.5 reads the relay fields to populate the compact table -- no recall from memory.
The three defect classes resolve ambiguity at Phase 2.5: a relay field absent entry is detected
immediately when the checkpoint reads the relay, before Phase 3 begins. The Verdict references
the Phase 2.5 result as a closed audit surface; re-running the audit in the Verdict is explicitly
prohibited (C-13). Combined risk: three axes add three load-bearing requirements to Phase 2.5.
If relay-seeded fields are absent, the checkpoint cannot populate the compact table and must
declare relay field absent defects rather than proceeding with an empty table. Relay field absence
is a Phase 2.5 FAIL condition -- it blocks Phase 3 the same way SILENT or UNDECLARED do.

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
Execute. Evidence relay-seeded in Phase 2 relays (`Binding Summary row:` and `Schema-governed
action:` fields). Assembled into compact merged Role Bijection Table at Phase 2.5 Role Bijection
Checkpoint. Phase 3 BLOCKED if bijection fails (SILENT, UNDECLARED, or relay field absent found).
Verdict cites Phase 2.5 result; does not re-run the audit.

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

**Role-Schema Binding Summary bijection invariant (C-11/C-12/C-13/C-14)**: Role R is in the
Binding Summary if and only if it produces at least one schema-governed action in Phase 2 Execute.
Evidence captured in relay-seeded fields. Assembled as compact merged table at Phase 2.5. Phase 3
blocked on failure. Verdict cites gate result only.

[Schema 1-5 biconditional definitions: same as V-01.]
[Schema 5 sub-step ordering table: same as V-01.]

---

### Closed-World Verification -- Direction A

[Same Direction A table as V-01 -- all 5 schemas confirmed. Direction A: HOLDS.]

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

#### Phase 2 -- Execute (V-05: relay-seeded fields)

Produce: `{topic}-skill-trace-{date}.md`. Three required fields in every relay: Schema 2
compliance, `Binding Summary row:` (Direction B seed), `Schema-governed action:` (Direction A
seed). A relay missing either seeded field must declare the absence -- Phase 2.5 will read the
relay and detect the relay field absent defect.

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

#### Phase 2.5 -- Role Bijection Checkpoint (C-12 + C-13 + C-14: reads relay fields, compact table, hard gate)

**Named inter-phase checkpoint**: Runs immediately after Phase 2 Execute. Phase 3 Findings
cannot begin until this checkpoint produces a gate result.

**Three defect classes recognized at this checkpoint**:
1. **SILENT**: role has Binding Summary row; Execute relay absent or relay action missing. Column A: SILENT.
2. **UNDECLARED**: role has Execute relay; no Binding Summary row. Column B: UNDECLARED.
3. **relay field absent**: relay exists; `Binding Summary row:` or `Schema-governed action:` field
   missing from relay. Any relay field absent is a FAIL condition blocking Phase 3.

**Evidence source**: relay fields read directly from Phase 2 Execute. No end-of-trace reconstruction.

**Population rules**:
- Execute relay present: read `Binding Summary row:` -> column B source; read `Schema-governed
  action:` -> action cell and column A status. If `Schema-governed action:` missing: A = `relay
  field absent`. If `Binding Summary row:` missing: B = `relay field absent`.
- Binding Summary row present, no Execute relay: `Execute relay step: ABSENT`, A = `SILENT`.
- Execute relay present, no Binding Summary row: `Binding Summary row: ABSENT`, B = `UNDECLARED`.

**Role bijection invariant**: Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute.

**Role Bijection Table** (compact merged format -- C-12; populated from relay fields -- C-14):

| Role | Binding Summary row | Execute relay step | Schema-governed action (relay field) | A: Acts in Execute | B: Declared in Summary |
|------|--------------------|--------------------|-------------------------------------|-------------------|----------------------|
| [role] | [row index or ABSENT] | [relay step or ABSENT] | [from relay `Schema-governed action:` field, or "absent / silent / relay field absent"] | YES / SILENT / relay field absent | YES / UNDECLARED / relay field absent |

Defect declarations (for any non-YES column value):
- "[role] -- Binding Summary defect: declared but produced no schema-governed action." (A = SILENT)
- "[role] -- structural defect: acted in Execute without Binding Summary entry." (B = UNDECLARED)
- "[relay] -- relay-seeded field missing: [Binding Summary row / Schema-governed action]." (relay field absent)

**Biconditional hold summary** (closes the table -- C-12):

| Direction | Claim | Evidence source | Result |
|-----------|-------|----------------|--------|
| A (Binding Summary -> Execute) | Every declared role acts: no SILENT or relay field absent in column A | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list] |
| B (Execute -> Binding Summary) | Every acting role is declared: no UNDECLARED or relay field absent in column B | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list] |

Role bijection holds if and only if: all A = YES AND all B = YES.

**ROLE BIJECTION: PASS** (all A = YES, all B = YES, no relay fields absent).

If FAIL: **Phase 3 BLOCKED: [bijection defect -- classify as SILENT / UNDECLARED / relay field
absent; name the role relay and the specific defect. Resolve before proceeding.]**

---

#### Phase 3 -- Findings

Carrying forward from Phase 2.5 Role Bijection Checkpoint: Role Bijection = `{{PASS}}`.
Phase 3 valid to begin.

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

#### C-11 / C-12 / C-13 / C-14 Citation

**C-13 rule**: The Role Closed-World Audit is complete at Phase 2.5 Role Bijection Checkpoint.
This Verdict section cites the Phase 2.5 gate result; it does not re-run the bijection audit.
A bijection audit appearing only in this section -- without a Phase 2.5 checkpoint earlier in
the trace -- is FAIL for C-13.

**C-11 through C-14 verification: cited from Phase 2.5 Role Bijection Checkpoint.**

| Direction | Evidence source | Phase 2.5 gate result |
|-----------|-----------------|-----------------------|
| A (Binding Summary -> Execute) | `Schema-governed action:` relay fields | HOLDS / DEFECTS: [list or "none"] |
| B (Execute -> Binding Summary) | `Binding Summary row:` relay fields | HOLDS / DEFECTS: [list or "none"] |

Relay field absent defects found: [list or "none"].

**C-11: PASS** (Phase 2.5 gate = PASS, both directions HOLDS, no defects).
**C-12: PASS** (compact merged table with SILENT/UNDECLARED status columns and named biconditional
hold summary at Phase 2.5; no separate direction tables used).
**C-13: PASS** (Phase 2.5 named checkpoint present; BLOCKED language used on failure; Verdict
cites, does not re-run).
**C-14: PASS** (relay-seeded fields `Binding Summary row:` and `Schema-governed action:` present
in every Execute relay; three defect classes -- SILENT, UNDECLARED, relay field absent -- named
and distinguished at Phase 2.5; evidence explicitly sourced to relay fields).

The biconditional invariant -- Role R is in the Binding Summary if and only if it produces at
least one schema-governed action in Phase 2 Execute -- is found to hold: YES / NO.

---

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
