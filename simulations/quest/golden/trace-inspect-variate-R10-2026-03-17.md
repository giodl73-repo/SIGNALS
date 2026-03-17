---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 10
rubric: trace-inspect-rubric-v6
---

# trace-inspect -- Variations v6 R10 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R9 V-05 achieves 99.5/99.5 under rubric v5 -- all C-01 through C-21 PASS.
Rubric v6 adds two new aspirational criteria (C-22, C-23) at 0.5 pts each. Grand total 100.5.
Entry score for any R10 variant that adds nothing new: 99.5/100.5 (C-22 and C-23 FAIL).

**R9 excellence signals that drove C-22 and C-23**:

From R9 V-05 Signal 3: "Structural vs instructional distinction statement in EG-FIRST block.
V-05 ends its EG-FIRST EXECUTION CONSTRAINT block with: 'Evidence-grounded promotion is
architecturally enforced, not merely recommended.' This explicit structural-vs-instructional
distinction marker does not appear in V-01 or V-04." C-22 generalizes this signal: instead
of one structural-vs-instructional statement at the end of one block, every invariant in the
Coverage Matrix declares its enforcement class.

From R9 V-05 C-19 evidence: "Phase 2a (EG roles only) → EG-RELAY COMPLETE checkpoint →
SA-TO-SG PROMOTION → Phase 2b. Structural invariant: 'SA-TO-SG PROMOTION is structurally
BLOCKED until EG-RELAY COMPLETE checkpoint passes.'" The constraint block carries placeholder
text ("list all roles marked EG-producing YES in Role-Schema Binding Summary") rather than
an explicit membership list. C-23 requires the membership to be declared independently --
auditable without referencing the binding table.

**R10 variation axes** (two new criteria + one alternative format axis):

- **C-22 via Coverage Matrix column (V-01)**: Add an "Enforcement class" column to the
  Coverage Matrix. Each schema row annotated with its enforcement class: `architectural`
  (named structural gate or prerequisite blocks advancement; violation structurally impossible
  in a conformant trace) or `instructional` (vocabulary/format rule; compliance required;
  violations detected in the compliance ledger but not structurally prevented). Schema
  description paragraphs gain an enforcement class sentence. Schema 1/2/3: instructional.
  Schema 4 (gates): architectural. Schema 5 (ordering): architectural.

- **C-23 via standalone membership blocks (V-02)**: Restructure the EG-FIRST EXECUTION
  CONSTRAINT block so PHASE 2a MEMBERSHIP and PHASE 2b MEMBERSHIP are explicit named lists
  of role names -- not pointers to the Role-Schema Binding Summary. The block declares:
  "Membership is declared here independently of the Role-Schema Binding Summary. This block
  is the authority for execution phase assignment." Making role assignment auditable from
  the constraint block alone.

- **C-22 via inline suffix notation (V-03)**: Different format axis for C-22. Instead of a
  Coverage Matrix column, each invariant in the schema description paragraphs receives a
  standardized suffix `[enforcement: architectural]` or `[enforcement: instructional]`.
  The same suffix applies to every named invariant across all phases (G-1/G-2/G-3, EG-RELAY
  COMPLETE, label lock, sub-step prerequisites). Rationale: the column approach annotates at
  the table level; the suffix approach annotates at each invariant's definition point wherever
  it appears in the prompt body, creating richer per-use-site coverage.

- **V-04 (combined: C-22 column + C-23)**: Coverage Matrix enforcement class column (V-01
  approach) + standalone PHASE 2a/2b MEMBERSHIP blocks (V-02 approach).

- **V-05 (combined: C-22 column + C-23 + CRITERION INHERITANCE REGISTRY v6 + cross-reference)**:
  Full integration targeting 100.5/100.5. Adds updated CRITERION INHERITANCE REGISTRY (v5 →
  v6 with C-22/C-23 as NEW with mechanism descriptions). Cross-reference: the EG-FIRST
  EXECUTION CONSTRAINT structural invariant statement references its Coverage Matrix
  enforcement class annotation. C-23 membership blocks cite role count as a verifiable
  invariant (structural parallel to R9's count-as-verifiable-invariant pattern).

All five inherit the full R9 V-05 architecture:
- Coverage Matrix with 5 schemas, Role-binding and Verdict-check columns
- Role-Schema Binding Summary with EG-producing? column
- EG-FIRST EXECUTION CONSTRAINT block (C-19)
- Phase 2a (EG roles only) → EG-RELAY COMPLETE → SA-TO-SG PROMOTION → Phase 2b
- STEP 3b FLOOR CHECK (C-14)
- GATE CLEARANCE SUMMARY + REMEDIATION LOG / C-12 EXEMPTION (C-11, C-12)
- Schema 5 transition sentences and prerequisite verification (C-10, C-13)
- PHASE 4 GATE CLEARANCE SUMMARY (C-11)
- Compliance ledger with VC-4 G-1 C-21 CO-LOCATED ATTRIBUTION sub-table
- Three-way verdict classification rules (C-18)

---

## V-01 -- Single axis: C-22 (enforcement class column in Coverage Matrix)

**Axis**: Coverage Matrix gets an "Enforcement class" column. Every schema row declares
whether its invariant is `architectural` (named structural gate makes violation impossible
in a conformant trace) or `instructional` (vocabulary/format rule; compliance required;
violations detected post-hoc in the compliance ledger).

**Hypothesis**: R9 V-05 carries the structural-vs-instructional distinction in one place
(the end of the EG-FIRST EXECUTION CONSTRAINT block). A scorer checking C-22 must either
read the entire prompt or trust that the single statement covers all invariants. A Coverage
Matrix column makes the enforcement class machine-checkable: one cell per schema, one value
per invariant, readable without scanning the schema descriptions. Risk: the column adds
width to an already wide table. Mitigation: "Enforcement class" is a short value (one word
+ short clause); the column value is not a sentence but a type annotation.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations (labels outside {P1,P2,P3}) are detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required in every Amend entry; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY must declare ALL GATES CLEARED before Step 3d begins; PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4 entry; advancement structurally blocked until gate is PASS |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until prerequisite is satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is a quality improvement. P3 is advisory. Every EG finding from every
role uses only {P1, P2, P3}. No other severity value appears anywhere in the trace. Compliance
is required; violations are detected in VC-1.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
SA = spec-layer gap. SG = setup gap. EG = execute gap. QO = quality observation. Label lock
invariant: a promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. A promoted gap
retaining SA is a structural violation. Compliance is required; violations are detected in VC-2.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`. An entry
without a channel field is structurally incomplete. Compliance is required; omissions are
detected in VC-3.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1: Step 3b
contains >=2 distinct Source types. G-2: no two same-Source findings share identical Action
text. G-3: all Step 3b entries use only {P1, P2, P3}. The GATE CLEARANCE SUMMARY structural
block must declare ALL GATES CLEARED before Step 3d begins. Any defect must be corrected and
re-checked; it cannot be bypassed. Violation is architecturally blocked by the GATE CLEARANCE
SUMMARY gate, not merely instructionally discouraged.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Each sub-step declares a
named prerequisite that must be satisfied before that sub-step begins and a Schema 5 transition
sentence that confirms completion and declares the next step valid. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Before Stage 2 begins, declare which roles are EG-producing and which are SA/SG-only:

```
EG-producing roles (must complete Phase 2a before SA-TO-SG PROMOTION):
  [list all roles marked EG-producing YES in Role-Schema Binding Summary]

SA/SG-only roles (run in Phase 2b, after SA-TO-SG PROMOTION):
  [list all roles marked EG-producing NO]

Structural invariant [enforcement: architectural]: SA-TO-SG PROMOTION is structurally
BLOCKED until EG-RELAY COMPLETE checkpoint passes. A trace that evaluates SA-TO-SG
PROMOTION before EG-RELAY COMPLETE is structurally invalid at that point.
Evidence-grounded promotion is architecturally enforced, not merely recommended.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. The test invocation is not consulted here.
A Stage 1 where all gaps cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap
attribution block for every role. A Setup that lists roles without schema binding declarations
is structurally incomplete.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (EG-producing roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only EG-producing roles from the EG-FIRST EXECUTION
CONSTRAINT block run here. SA/SG-only roles are deferred to Phase 2b. SA-TO-SG PROMOTION
is structurally BLOCKED until the EG-RELAY COMPLETE checkpoint below passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (required structural checkpoint -- SA-TO-SG PROMOTION is BLOCKED
> until this checkpoint passes):
>
> - EG-producing roles declared in EG-FIRST EXECUTION CONSTRAINT: [list]
> - EG-producing roles with completed relays above: [list]
> - All EG-producing roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** (all EG roles relayed) / **FAIL** (relay missing for: [role])
>
> If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION. SA-TO-SG PROMOTION
> structurally cannot begin until this checkpoint shows PASS.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite**: EG-RELAY COMPLETE PASS (confirmed above). Promotion decisions may cite
observed execution evidence from Phase 2a relays.

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output -- trace may not advance to Step 3c
> until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. A missing source layer requires at least one
> finding from that layer. Duplicate Actions require distinct remediation targets. Re-run
> FLOOR CHECK after correction. A bare count without named Finding IDs is not valid.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required structural block before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c GATE CLEARANCE SUMMARY ALL GATES CLEARED.

Channel taxonomy active: every Phase 4 Amend entry must include `[remediation channel:
spec / invocation / artifact / quality]`. An entry without this field is structurally
incomplete.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (required structural block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified across all Phase 2a + 2b roles; attribution table filled in this cell | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase / Role(s) / Finding IDs -- [fill one row per Source type; this cell is not complete until the sub-table is filled; filling ledger and attribution are one operation] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: C-23 (Phase 2a/2b role membership enumerated -- standalone blocks)

**Axis**: Role sequence -- EG-FIRST EXECUTION CONSTRAINT block restructured so that PHASE 2a
MEMBERSHIP and PHASE 2b MEMBERSHIP are explicit named role lists, declared independently of the
Role-Schema Binding Summary. The constraint block is the authority for execution phase
assignment; membership is auditable from the constraint block alone.

**Hypothesis**: R9 V-05's EG-FIRST EXECUTION CONSTRAINT block says "list all roles marked
EG-producing YES in Role-Schema Binding Summary" -- a pointer, not a declaration. A model
filling in the block may copy the pointer text literally rather than resolving it to role names.
C-23 requires the names to appear in the constraint block so that the Phase 2a and Phase 2b
assignments are auditable without cross-referencing the binding table. V-02 adds PHASE 2a
MEMBERSHIP and PHASE 2b MEMBERSHIP sub-blocks with one line per role, a total count, and a
declaration that the block is the authoritative source for execution phase assignment. Risk:
duplication between the constraint block and the binding table creates maintenance surface.
Mitigation: the constraint block is downstream of the binding table and reads from it at
trace-write time; the authoritative declaration in the constraint block is the settlement,
not the derivation.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: {P1, P2, P3} only. P1 blocks usefulness. P2 is a
quality improvement. P3 is advisory. Every EG finding from every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: {SA, SG, EG, QO} only. SA = spec-layer gap. SG = setup
gap. EG = execute gap. QO = quality observation. Label lock invariant: a promoted SA gap uses
SG in all phases after SA-TO-SG PROMOTION.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes `[remediation
channel: spec / invocation / artifact / quality]`. An entry without a channel field is
structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**: G-1: Step 3b contains >=2 distinct Source types.
G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use
only {P1, P2, P3}. Any defect must be corrected and re-checked; it cannot be bypassed.

**Schema 5 -- Sub-Step Ordering**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here. This block is the authority for phase
assignment and is auditable independently of the Role-Schema Binding Summary above.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line, e.g.:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  - [Role B] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line, e.g.:]
  - [Role C] (SA/SG-class: produces SA/SG gaps only; runs in Phase 2b)
  - [Role D] (SA/SG-class: produces SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles declared in Role-Schema Binding Summary)

Structural invariant: SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE
checkpoint passes. A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is
structurally invalid at that point. Evidence-grounded promotion is architecturally enforced,
not merely recommended.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. The test invocation is not consulted here.
A Stage 1 where all gaps cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap
attribution block for every role.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (EG-producing roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here (declared in
EG-FIRST EXECUTION CONSTRAINT block above). SA/SG-only roles are deferred to Phase 2b.
SA-TO-SG PROMOTION is structurally BLOCKED until the EG-RELAY COMPLETE checkpoint below
passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (required structural checkpoint -- SA-TO-SG PROMOTION is BLOCKED
> until this checkpoint passes):
>
> - PHASE 2a MEMBERSHIP declared in EG-FIRST EXECUTION CONSTRAINT: [list role names; count N]
> - EG-producing roles with completed relays above: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** (all Phase 2a roles relayed) / **FAIL** (relay missing for: [role])
>
> If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite**: EG-RELAY COMPLETE PASS (confirmed above). Promotion decisions may cite
observed execution evidence from Phase 2a relays.

Every SA gap from Stage 1 is evaluated.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant: a promoted gap using its SA label in any downstream phase is a
structural violation.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here** (declared in EG-FIRST EXECUTION CONSTRAINT block).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.
Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output -- trace may not advance to Step 3c
> until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.

**G-1**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required structural block before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c GATE CLEARANCE SUMMARY ALL GATES CLEARED.

Channel taxonomy active: every Phase 4 Amend entry must include `[remediation channel:
spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (required structural block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; PHASE 2a + 2b MEMBERSHIP roles enumerated as source attribution | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase / Role(s) / Finding IDs -- [fill one row per Source type; confirm PHASE 2a MEMBERSHIP and PHASE 2b MEMBERSHIP role names match constraint block declaration; this cell is not complete until the sub-table is filled] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: C-22 (enforcement class -- inline suffix at every invariant definition)

**Axis**: Lifecycle emphasis / output format -- rather than annotating enforcement class in the
Coverage Matrix table, every named invariant across all phases carries a standardized inline
suffix at the point where it is defined: `[enforcement: architectural]` or
`[enforcement: instructional]`. This covers the Coverage Matrix schema descriptions AND every
downstream usage where an invariant is re-stated (G-1/G-2/G-3 at Step 3c, EG-RELAY COMPLETE
invariant in Phase 2a, label lock invariant in Phase 2b).

**Hypothesis**: The Coverage Matrix column approach (V-01) centralizes enforcement class
annotation at the table. A reviewer checking C-22 reads one table and sees all classes. The
inline suffix approach distributes annotation across every definition site. When an invariant
is re-stated in Phase 3 (e.g., "G-1: Step 3b contains >=2 distinct Source types"), the suffix
appears there too. This creates per-use-site annotation density: a model executing the trace
reads the enforcement class at every point where the invariant is applied, not only at the
central declaration. Risk: suffix repetition across phases may be treated as redundant noise.
Mitigation: the suffix is a compact annotation (`[enforcement: architectural]`) that adds a
fixed small cost; the benefit is that the classification is present wherever the constraint
fires, reducing the chance that a model treats a gate as instructional when it is architectural.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is a quality improvement. P3 is advisory. Violations are detectable in
VC-1 but are not structurally blocked; the vocabulary must be followed by rule, not by gate.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: a promoted SA gap uses SG in all phases
after SA-TO-SG PROMOTION. A promoted gap retaining SA is a violation detectable in VC-2;
the trace structure does not structurally prevent the wrong label from appearing.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`. Omissions
are detectable in VC-3; field inclusion is a rule, not a gate.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1, G-2, G-3.
The GATE CLEARANCE SUMMARY structural block must declare ALL GATES CLEARED before Step 3d
begins; PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4 entry. Advancement is structurally
blocked until the gate passes -- violation is architecturally impossible in a conformant trace.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Each sub-step declares a
named prerequisite; a Schema 5 transition sentence confirms completion before the next step.
Advancement without a satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

```
EG-producing roles (must complete Phase 2a before SA-TO-SG PROMOTION):
  [list all roles marked EG-producing YES in Role-Schema Binding Summary]

SA/SG-only roles (run in Phase 2b, after SA-TO-SG PROMOTION):
  [list all roles marked EG-producing NO]

Structural invariant [enforcement: architectural]: SA-TO-SG PROMOTION is structurally
BLOCKED until EG-RELAY COMPLETE checkpoint passes. A trace that evaluates SA-TO-SG
PROMOTION before EG-RELAY COMPLETE is structurally invalid at that point.
Evidence-grounded promotion is architecturally enforced, not merely recommended.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (EG-producing roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only EG-producing roles run here. SA-TO-SG PROMOTION is
structurally BLOCKED `[enforcement: architectural]` until the EG-RELAY COMPLETE checkpoint
below passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** `[enforcement: architectural]` (required structural checkpoint --
> SA-TO-SG PROMOTION is BLOCKED until this checkpoint passes):
>
> - EG-producing roles declared in EG-FIRST EXECUTION CONSTRAINT: [list]
> - EG-producing roles with completed relays above: [list]
> - All EG-producing roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** / **FAIL** (relay missing for: [role])

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite** `[enforcement: architectural]`: EG-RELAY COMPLETE PASS (confirmed above).

Every SA gap from Stage 1 is evaluated.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a violation detectable in VC-2.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write** (after all Phase 2a + 2b relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5
`[enforcement: architectural]`.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite `[enforcement: architectural]`: Schema 1 declared in Coverage Matrix.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite `[enforcement: architectural]`: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** `[enforcement: architectural]` (required structural output --
> trace may not advance to Step 3c until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite `[enforcement: architectural]`: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural block):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL
GATES CLEARED.

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

"Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified across all roles | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase / Role(s) / Finding IDs -- [fill one row per Source type; this cell is not complete until sub-table is filled] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: C-22 (Coverage Matrix column) + C-23 (standalone membership blocks)

**Axis**: Role sequence + output format -- V-01's Coverage Matrix enforcement class column
combined with V-02's standalone PHASE 2a/2b MEMBERSHIP declaration blocks.

**Hypothesis**: V-01 and V-02 address independent structural gaps. V-01 makes enforcement
class visible from the Coverage Matrix (one-table audit for C-22). V-02 makes role phase
assignment auditable without referencing the binding table (standalone declaration for C-23).
The two mechanisms are orthogonal: the enforcement class column tells you whether an invariant
is architectural or instructional; the membership blocks tell you which roles are assigned to
which execution phase. No structural conflict. Combined, they cover both new criteria and leave
V-05 to add only the inheritance registry and cross-reference.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is a quality improvement. P3 is advisory.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant: a promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1: Step 3b >=2
distinct Source types. G-2: no duplicate Action text within same Source. G-3: all entries use
{P1, P2, P3}. GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates
Phase 4. Violation is architecturally blocked.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites block
advancement; Schema 5 transition sentences confirm completion.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.
This block is the authority for phase assignment; role names must appear here explicitly.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line:]
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary)

Structural invariant [enforcement: architectural]: SA-TO-SG PROMOTION is structurally
BLOCKED until EG-RELAY COMPLETE checkpoint passes. A trace that evaluates SA-TO-SG
PROMOTION before EG-RELAY COMPLETE is structurally invalid at that point.
Evidence-grounded promotion is architecturally enforced, not merely recommended.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here (enumerated in
EG-FIRST EXECUTION CONSTRAINT block). SA/SG-only roles deferred to Phase 2b. SA-TO-SG
PROMOTION is structurally BLOCKED `[enforcement: architectural]` until EG-RELAY COMPLETE
checkpoint passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (required structural checkpoint -- SA-TO-SG PROMOTION BLOCKED until PASS):
>
> - PHASE 2a MEMBERSHIP declared in constraint block: [list role names + count N]
> - PHASE 2a roles with completed relays: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS / FAIL** (if FAIL, missing: [role name])

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite** `[enforcement: architectural]`: EG-RELAY COMPLETE PASS (confirmed above).

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant `[enforcement: instructional]`: promoted gap retaining SA label is
a violation detectable in VC-2.

---

#### Phase 2b -- SA/SG-Only Role Execution (PHASE 2b MEMBERSHIP roles only)

**Only PHASE 2b MEMBERSHIP roles run here** (enumerated in EG-FIRST EXECUTION CONSTRAINT block).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write**:
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 sub-steps run in the order declared by Schema 5 `[enforcement: architectural]`.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output -- trace may not advance to Step 3c
> until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required structural block before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED.

> **REMEDIATION LOG** (if any gate FAILs; else: "C-12 EXEMPTION APPLIES: all gates passed
> on first evaluation. No remediation loop."):

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c GATE CLEARANCE SUMMARY ALL GATES CLEARED.

Channel taxonomy active: every Phase 4 Amend entry must include `[remediation channel:
spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (required structural block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

"Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG; confirm PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; PHASE 2a + 2b membership cited in attribution | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase / Role(s) / Finding IDs -- [fill one row per Source type; confirm role names match PHASE 2a/2b MEMBERSHIP declaration; this cell is not complete until sub-table is filled] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid after 3a | [confirm] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid after FLOOR CHECK PASS | [cite result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid after GATE CLEARANCE SUMMARY | [state result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 after channel taxonomy active | [state + PHASE 4 summary] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined: C-22 + C-23 + CRITERION INHERITANCE REGISTRY v6 + cross-reference

**Axis**: Role sequence + output format + inertia framing + lifecycle emphasis -- all four
mechanisms combined. V-04's Coverage Matrix column (C-22) and standalone membership blocks
(C-23) plus: (1) CRITERION INHERITANCE REGISTRY updated to v6, listing C-22 and C-23 as NEW
with inline mechanism descriptions; (2) cross-reference between the EG-FIRST EXECUTION
CONSTRAINT structural invariant and its Coverage Matrix enforcement class annotation;
(3) VC-4 G-1 SOURCE ATTRIBUTION TABLE membership confirmation tightened to explicitly
require role count validation against the PHASE 2a/2b MEMBERSHIP blocks.

**Hypothesis**: V-04 achieves C-22 and C-23 PASS independently. V-05 adds three integration
gains. First: the inheritance registry gives C-22 and C-23 entries annotated mechanism
descriptions (parallel to R9 V-05's Signal 2: "registry entries annotated with mechanical
satisfaction"). A scorer auditing v6 can verify not just that C-22 is declared to be satisfied
but how: "enforced via Enforcement class column in Coverage Matrix; per-invariant annotation
present for all five schemas." Second: the cross-reference between the EG-FIRST block's
structural invariant and the Coverage Matrix `[enforcement: architectural]` annotation makes
the two elements mutually reinforcing -- the constraint block cites the class; the class column
cites the constraint block. Third: the VC-4 G-1 co-located attribution cell adds a membership
count check (Phase 2a role count from attribution should equal N declared in PHASE 2a
MEMBERSHIP block), creating a structural link between C-23's membership declaration and the
existing C-21 attribution mechanism. None of these integrations appear in single-axis variants.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v6

This skill body is version 6. The following criteria were established in prior versions and
are explicitly inherited here. A version that does not name a criterion in this registry has
dropped it. Dropping a criterion is a structural act, not a silent omission.

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  Result: traces that pass or fail based on executor judgment, not structural evidence.
  This skill replaces judgment with a 4-phase lifecycle that produces auditable evidence.

INHERITED FROM v1 -- ESSENTIAL CRITERIA:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED CRITERIA:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL CRITERIA:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL CRITERIA:
  C-11 (Phase-entry gate clearance summary): INHERITED
  C-12 (Gate-failure remediation loop): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL CRITERIA:
  C-14 (Pre-scoring mechanism placement): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL CRITERIA:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED
  C-18 (Verdict classification rule citation): INHERITED

INHERITED FROM v5 -- ASPIRATIONAL CRITERIA:
  C-19 (EG-first structural role ordering): INHERITED -- enforced via EG-FIRST EXECUTION
    CONSTRAINT block and EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally BLOCKED
    until PASS; [enforcement: architectural] per Coverage Matrix Schema 4 column
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED -- C-17 table
    embedded directly in VC-4 G-1 cross-role row; filling ledger and attribution are one
    operation; structural drift between ledger and attribution is impossible

NEW IN v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): NEW -- enforced via "Enforcement class" column in
    Coverage Matrix; every schema row annotated as [architectural] or [instructional];
    [enforcement: X] inline suffix on every named invariant in schema description paragraphs;
    per-invariant class is readable from Coverage Matrix without scanning the prompt body
  C-23 (Phase 2a/2b role membership enumerated): NEW -- enforced via PHASE 2a MEMBERSHIP
    and PHASE 2b MEMBERSHIP named blocks in EG-FIRST EXECUTION CONSTRAINT; each block lists
    role names explicitly with role count; membership auditable from the constraint block
    independently of the Role-Schema Binding Summary; count validated in VC-4 G-1 attribution
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1;
not structurally blocked.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA is a violation detectable in VC-2; not structurally blocked.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3; not structurally blocked.

**Schema 4 -- Enforcement Gate Registry** `[enforcement: architectural]`: G-1/G-2/G-3.
GATE CLEARANCE SUMMARY gates Step 3d. PHASE 4 GATE CLEARANCE SUMMARY gates Phase 4.
Advancement is structurally blocked until the gate clears. See EG-FIRST EXECUTION CONSTRAINT
for the architectural gate governing SA-TO-SG PROMOTION.

**Schema 5 -- Sub-Step Ordering** `[enforcement: architectural]`: Named prerequisites gate
each sub-step. Schema 5 transition sentences confirm completion. Advancement without a
satisfied prerequisite is structurally blocked.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.
This block is the authority for phase assignment; role names must appear here explicitly and
are auditable without cross-referencing the binding table.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  [list each EG-producing role by name, one per line:]
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  [list each SA/SG-only role by name, one per line:]
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary;
  count mismatch = missing or misassigned role)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
  A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is structurally
  invalid at that point. Evidence-grounded promotion is architecturally enforced, not
  merely recommended. The enforcement class [architectural] is declared in the Coverage
  Matrix Enforcement class column for Schema 4; the gate mechanism is this constraint block.
```

---

### Stage 1 -- Source-Layer Audit

Inertia note: without a structured Stage 1, a developer reads the spec once and guesses.
Stage 1 forces a systematic read of all three source layers before execution begins.

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A -- produces no EG findings"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here. SA/SG-only roles
deferred to Phase 2b. SA-TO-SG PROMOTION is structurally BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE checkpoint passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** `[enforcement: architectural]` (required structural checkpoint --
> SA-TO-SG PROMOTION BLOCKED until PASS):
>
> - PHASE 2a MEMBERSHIP declared in EG-FIRST EXECUTION CONSTRAINT: [list role names + count N]
> - PHASE 2a roles with completed relays: [list]
> - All PHASE 2a MEMBERSHIP roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** / **FAIL** (if FAIL, missing: [role name])
>
> If FAIL: complete the missing PHASE 2a relay before SA-TO-SG PROMOTION.

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite** `[enforcement: architectural]`: EG-RELAY COMPLETE PASS (confirmed above).
Promotion decisions may cite observed execution evidence from Phase 2a relays.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant `[enforcement: instructional]`: promoted gap retaining SA is a
violation detectable in VC-2; not structurally blocked.

---

#### Phase 2b -- SA/SG-Only Role Execution (PHASE 2b MEMBERSHIP roles only)

**Only PHASE 2b MEMBERSHIP roles run here** (enumerated in EG-FIRST EXECUTION CONSTRAINT).

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [none -- this role does not produce EG findings]

**Artifact write**:
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 sub-steps run in the order declared by Schema 5 `[enforcement: architectural]`.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite `[enforcement: architectural]`: Schema 1 declared in Coverage Matrix.
Schema 5 output: severity legend (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite `[enforcement: architectural]`: Step 3a complete.
Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** `[enforcement: architectural]` (required structural output --
> trace may not advance to Step 3c until this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. Re-run FLOOR CHECK after correction.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite `[enforcement: architectural]`: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural block
> before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation,
> emit instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation
> loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL
GATES CLEARED.
Schema 5 output: Schema 3 channel taxonomy active (unblocks Phase 4).

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required structural
> block at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; C-23 MEMBERSHIP counts validate attribution completeness | **G-1 SOURCE ATTRIBUTION TABLE** (this cell is not complete until the sub-table is filled; filling ledger and attribution are one operation): Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type present in Step 3b; after filling, verify: PHASE 2a role count in attribution = N from PHASE 2a MEMBERSHIP block; PHASE 2b role count = M from PHASE 2b MEMBERSHIP block; count mismatch = C-23 membership block inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
