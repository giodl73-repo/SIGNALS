---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 6
rubric: trace-inspect-rubric-v3
---

# trace-inspect -- Variations v3 R6 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R5 champion is V-05 at 94/100. All essential PASS. All recommended PASS on V-01/V-05.
Two systematic gaps remain across all R5 variations:

- **C-08 (findings depth)**: ALL PARTIAL. No R5 variation imposes a structural floor count. Every
  variation instructs "minimum 3 rows, 2 distinct Source types" somewhere in the prompt text, but
  none require the executor to EMIT a visible floor check that can be independently verified. A model
  that produces 2 findings never sees a BLOCKED signal from the prompt -- it simply continues to
  Step 3c with an under-populated table. C-08 fails because it is an instruction, not an enforcement.

- **C-13 (sub-step prerequisite checkboxes)**: V-02 PASS; V-05 PARTIAL; V-01/V-03/V-04 FAIL. V-05
  inherits structural blocks from R2/R3 architecture (satisfying C-11/C-12) but does not introduce
  the named-artifact checkpoint FORMAT that C-13 specifically requires. C-10 (transition sentences
  AFTER a sub-step) passes in V-05; C-13 (named-artifact verification BEFORE a sub-step begins)
  is still only partial because the prompt does not force a named referent -- a bare YES is
  architecturally possible.

**R6 variation axes** (these two gaps drive all five axes):

- **Output format (C-08 enforcement)**: Add a mandatory FLOOR CHECK block that appears in the
  executor's output after the Step 3b table. The block names row count, distinct Source types, and
  Action-uniqueness status, and produces a PASS/FAIL result. A FAIL result structurally blocks
  advance to Step 3c. Hypothesis: emitting the check changes C-08 from an instruction the executor
  may satisfy lazily to a structural output the reviewer can audit independently (V-01).

- **Output format (C-13 named-artifact checkpoint)**: Add a PREREQUISITE CHECKPOINT block as the
  required opening of each Phase 3 sub-step. The block format: `Prerequisite:` / `Named artifact:`
  / `Check: YES`. The named-artifact field must cite a specific path or section name -- "bare YES
  without a named referent" is called out explicitly as a structural failure. Hypothesis: the
  block format prevents the mechanical YES that makes C-13 fail even when C-10 passes; the named-
  referent requirement is only satisfiable by reading the prior output (V-02).

- **Lifecycle emphasis (C-08 source pre-commitment)**: Restructure Step 3b to open with a SOURCE
  PRE-COMMITMENT block rather than closing with a floor check. The executor declares at least one
  expected finding per Source type represented in execution BEFORE writing any table rows. This
  forces source diversity at the start of synthesis, not as a post-hoc correction. Hypothesis:
  pre-commitment prevents the pattern where an executor writes homogeneous SA findings until the
  table feels complete, then notices the missing EG layer too late (V-03).

**Combined variations**:
- V-04: C-08 floor enforcement + C-13 named-artifact checkboxes (both remaining open criteria)
- V-05: C-08 floor enforcement + C-13 checkboxes + C-03/source pre-commitment + inertia framing
  (full integration targeting 100/100)

All five inherit the R5 V-05 architecture: execution-first ordering, named GATE CLEARANCE SUMMARY
structural block, mandatory C-12 EXEMPTION notice, Coverage Matrix with VC compliance columns,
Schema 5 sub-step transition table.

---

## V-01 -- Single axis: Output format (C-08: Findings floor enforcement block)

**Axis**: Output format -- Step 3b receives a mandatory FLOOR CHECK block in the executor output.

**Hypothesis**: R5 V-05 says "minimum 3 rows, 2 distinct Source types" in the Step 3b instructions
but requires no visible floor-check output. A model can produce 2 findings, never emit the check,
and advance to Step 3c unimpeded. V-01 adds a named FLOOR CHECK block after the Step 3b table as
a required structural output. The executor must emit the block; the block must PASS; if it FAILs
the trace is BLOCKED at Step 3b. Risk: the executor emits the block with inflated counts (says
"row count: 3" when the table has 2). Mitigation: the FLOOR CHECK block requires citing the
specific finding IDs counted -- a mechanical count cannot be inflated without forging IDs.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in this
table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: P1 blocks usefulness. P2 is a quality improvement. P3 is
advisory. Every EG finding from every role uses only {P1, P2, P3}. No other severity value appears
anywhere in the trace.

**Schema 2 -- Gap Type Taxonomy**: SA = spec-layer gap. SG = setup gap. EG = execute gap. QO =
quality observation. Label lock invariant: a promoted SA gap uses SG in all phases after
SA-TO-SG PROMOTION. A promoted gap retaining SA is a structural violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes `[remediation
channel: spec / invocation / artifact / quality]`. An entry without a channel field is structurally
incomplete.

**Schema 4 -- Enforcement Gate Registry**: G-1: Step 3b contains >=2 distinct Source types. G-2:
no two same-Source findings share identical Action text. G-3: all Step 3b entries use only
{P1, P2, P3}. Any defect must be corrected and re-checked; it cannot be bypassed.

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

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 produces a gap audit table and a relay record. Stage 1 reads only
`{{skill_spec_path}}`. A Stage 1 where all gaps are SA is a warning signal; at least 2 distinct
source types should be visible before execution begins.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### SA-TO-SG PROMOTION

Every SA gap from Stage 1 is evaluated at this lifecycle event. Execution-first ordering note:
EG-producing roles run before SA-only roles in Phase 2 (see Execute below). This means promotion
decisions are informed by the execution evidence already observed.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- cite execution evidence if available, or spec inference if pre-execution]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
```

Label lock invariant: a promoted gap using its SA label in any downstream phase is a structural
violation. Verify in VC-2.

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and a per-role schema binding and gap attribution
block for every role.

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
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps present]
  SA/SG gaps binding this role: [list or "none confirmed"]
  EG gaps expected for this role: [list or "none confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**Execution-first ordering**: Run EG-producing roles before SA-only roles. This grounds the
SA-TO-SG PROMOTION decision in observed execution evidence rather than spec inference alone.

A valid Execute produces the hand-compiled artifact `{topic}-skill-trace-{date}.md` and a
per-role relay for each role. A relay missing the "Schema 2 compliance" field is structurally
invalid.

**Role relay -- [role name]** (EG-producing first):
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none confirmed"]
- Produced: [artifact content added or "no artifact contribution at this role"]
- EG gaps encountered: [EG-NN list or "none"]

**Artifact write** (required after all role relays):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Section confirmation: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG gaps added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5 and each
Schema 5 prerequisite is satisfied before the sub-step begins.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: merged findings table + FLOOR CHECK PASS (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output -- trace may not advance to Step 3c until
> this block PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list each type, e.g., SA, EG] (required: >= 2 distinct types)
> - Action-uniqueness check: do any two Action cells share identical text? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. For row count below 3, identify the source layer with
> fewest findings and add at least one finding from that layer. For Source type count below 2,
> identify which layer is missing (SA, SG, EG, or QO) and add a finding from that layer.
> For Action duplicates, revise to name a distinct remediation target.
> Re-run FLOOR CHECK after correction.
>
> A trace that reaches Step 3c without a FLOOR CHECK PASS block is structurally incomplete. The
> FLOOR CHECK must name the specific finding IDs counted -- a bare count without IDs fails.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.
Schema 5 output: gate results (all must be PASS to unblock Step 3d).

**G-1 -- Source diversity**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 result: PASS / FAIL

**G-2 -- Action uniqueness**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs"]
- G-2 result: PASS / FAIL

**G-3 -- Severity conformance**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 result: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required structural block before Step 3d):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation, emit
> instead: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added, or specific text changed]
> - Re-check: G-[X] -- [PASS / FAIL]
> - Updated gate result: [PASS / FAIL]

Schema 5 transition: Step 3c complete (GATE CLEARANCE SUMMARY declares ALL GATES CLEARED).
Step 3d is valid to begin.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all gates PASS (confirmed by GATE CLEARANCE SUMMARY above).
Schema 5 output: Schema 3 channel taxonomy activated (unblocks Phase 4).

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact /
quality]`. An entry without this field is structurally incomplete.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (required structural block at Phase 4 entry -- must reflect
> post-remediation gate states, not initial evaluation states):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
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

---

### Phase 5 -- Verdict and VC Compliance Ledger

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must name
specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b FLOOR CHECK | All entries P1/P2/P3; floor PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG label; lock holds | [list SA gaps promoted; confirm SG downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after all gates PASS | [state Phase 4 GATE CLEARANCE SUMMARY result] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after 3a complete | [confirm what showed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after 3b FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + Phase 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Output format (C-13: Named-artifact prerequisite checkpoint blocks)

**Axis**: Output format -- each Phase 3 sub-step opens with a named-artifact PREREQUISITE
CHECKPOINT block before the sub-step body begins.

**Hypothesis**: R5 V-05 satisfies C-10 (Schema 5 transition sentences after each sub-step
completes) but is PARTIAL on C-13. C-13 requires a verification that fires BEFORE the sub-step
body, not after. The distinction: C-10 says "prior step is done, next is unblocked"; C-13 says
"I have verified the named artifact that prior step produced before I begin this step." A C-10
transition sentence can be written from memory; a C-13 named-artifact checkpoint requires citing
a specific path or section. V-02 adds the PREREQUISITE CHECKPOINT block as the required first
output of each sub-step. Bare YES without a named referent is explicitly called out as a
structural failure. Risk: executors supply a generic path ("simulations/trace/...") that satisfies
the format but not the spirit. Mitigation: the named referent must match the specific artifact
or section produced in the prior sub-step, not the overall output path.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1**: {P1, P2, P3} only. P1 = blocks usefulness. P2 = quality improvement. P3 = advisory.
**Schema 2**: {SA, SG, EG, QO} only. Label lock: promoted SA gap becomes SG in all downstream phases.
**Schema 3**: Every Phase 4 Amend entry carries `[remediation channel: spec / invocation / artifact / quality]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (no same-Source duplicate Actions), G-3 (only {P1,P2,P3}).
**Schema 5**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role] | [severity labels or N/A] | [Source labels; label lock] | YES / NO | [interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]  [layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

Every SA gap evaluated at this lifecycle event. Execution-first ordering applies: EG-producing
roles run before SA-only roles, so promotion reasons may cite observed execution evidence.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite execution evidence or spec inference]
```

```
[SA remaining: {{sa_remaining}}]  [SG from promotion: {{sg_promoted}}]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps binding this role: [list or "none confirmed"]
  EG gaps expected: [list or "none confirmed"]
```

---

#### Phase 2 -- Execute

**Execution-first ordering**: EG-producing roles run before SA-only roles.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Artifact write**: Path `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Section confirmation: [each required section with WRITTEN status]

---

#### Phase 3 -- Findings

Each sub-step MUST begin with a PREREQUISITE CHECKPOINT block. The checkpoint fires before the
sub-step body. A bare "YES" without a named referent is a structural failure -- the named-artifact
field must cite the specific artifact or section produced in the prior step.

---

##### Step 3a -- Severity Legend Declaration

> **PREREQUISITE CHECKPOINT -- Step 3a**:
> Prerequisite: Schema 1 declared in Coverage Matrix before Stage 1.
> Named artifact: `Coverage Matrix, Schema 1 row -- "P1 / P2 / P3", declared above`
> Check: YES

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

> **PREREQUISITE CHECKPOINT -- Step 3b**:
> Prerequisite: Step 3a complete and severity legend produced.
> Named artifact: `Step 3a severity legend table, immediately above`
> Check: YES

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: Step 3b complete. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

> **PREREQUISITE CHECKPOINT -- Step 3c**:
> Prerequisite: Step 3b findings table populated with at least 2 entries.
> Named artifact: `Step 3b findings table, row count: N, row IDs: [list]`
> Check: YES

**G-1**: >=2 distinct Source types in Step 3b. Source types present: [list]. G-1: PASS / FAIL
**G-2**: No same-Source duplicate Actions. Pairs examined: [list or "none"]. G-2: PASS / FAIL
**G-3**: All entries use only {P1, P2, P3}. Labels present: [list]. G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required before Step 3d):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d BLOCKED.

> **REMEDIATION LOG** (required on any FAIL; or: "C-12 EXEMPTION APPLIES: all gates passed on
> first evaluation. No remediation loop."):
> Gate [X] FAIL: Failure reason: [text] / Remediation action: [specific ID or change] /
> Re-check: PASS / FAIL / Updated gate result: PASS / FAIL

Schema 5 transition: Step 3c complete (GATE CLEARANCE SUMMARY ALL CLEAR). Step 3d is valid to begin.

---

##### Step 3d -- Channel Taxonomy Activation

> **PREREQUISITE CHECKPOINT -- Step 3d**:
> Prerequisite: Step 3c all gates PASS, confirmed by GATE CLEARANCE SUMMARY.
> Named artifact: `Step 3c GATE CLEARANCE SUMMARY, declaring "ALL GATES CLEARED"`
> Check: YES

Schema 3 channel taxonomy activated. A valid Phase 4 Amend entry includes
`[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: Step 3d complete. Phase 4 is valid to begin.

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (must reflect post-remediation states, not initial states):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`] [source: `{{source}}`] [remediation channel: spec/invocation/artifact/quality]
- [section or field changed: ] [change: ] [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`] [reason: ] [remediation channel: ]

---

### Phase 5 -- Verdict and VC Compliance Ledger

"Observed behavior: as expected" is invalid. Name specific values, IDs, or results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend declared | [name the legend] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b | All entries P1/P2/P3 | [list labels in table] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result + labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries P1/P2/P3 | [list severity in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels | [list Source labels in audit] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG | [list promotions; confirm SG] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; label lock | [list labels; flag promoted] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [channels per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 gated | [Phase 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Checkpoint: legend named | [C-13 named artifact from 3a checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Checkpoint: table rows named | [C-13 named artifact from 3b checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Checkpoint: GATE CLEARANCE named | [C-13 named artifact from 3c checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Checkpoint: activation named | [C-13 named artifact from 3d checkpoint] | PASS/FAIL |

**VC-1 overall**: PASS/FAIL | **VC-2 overall**: PASS/FAIL | **VC-3 overall**: PASS/FAIL
**VC-4 overall**: PASS/FAIL | **VC-5 overall**: PASS/FAIL

**SA remaining**: [N] | **SG total**: [N] | **EG total**: [N]

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps > 3 and indicate structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (C-08: Source diversity pre-commitment)

**Axis**: Lifecycle emphasis -- Step 3b is restructured to open with a SOURCE PRE-COMMITMENT block
before any table rows are written.

**Hypothesis**: V-01 closes C-08 with a post-table floor check (a correction mechanism). V-03
tests a different mechanical approach: the executor declares one expected finding per represented
Source type BEFORE writing the table. This forces source diversity at synthesis time, not as a
post-hoc correction. The hypothesis is that pre-commitment prevents the failure mode where an
executor writes SA-heavy findings until the table "feels complete" and only then discovers the
EG layer is absent. A pre-commitment to "I will have at least one EG finding and one SA finding"
makes the omission visible at the opening of Step 3b rather than after the table is done.
Risk: executors pre-commit with placeholder seeds then write generic findings that technically
cover the pre-committed sources but add no depth. Mitigation: the pre-commitment seed must name
a specific gap from Stage 1 or Phase 2 execution -- a generic placeholder fails.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All EG-producing roles | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

**Schema 1**: {P1, P2, P3}. P1 blocks. P2 improves. P3 advises.
**Schema 2**: {SA, SG, EG, QO}. Label lock: promoted SA becomes SG in all downstream phases.
**Schema 3**: Every Phase 4 Amend entry carries `[remediation channel: spec/invocation/artifact/quality]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (no same-Source duplicate Actions), G-3 ({P1,P2,P3} only).
**Schema 5**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete + SOURCE PRE-COMMITMENT declared | Findings table | Step 3c |
| Step 3c | Step 3b populated | Gate results all PASS | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role] | [labels or N/A] | [Source labels; lock] | YES / NO | [interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]  [layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

Execution-first: EG-producing roles run first so promotion reasons may cite execution evidence.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [cite execution evidence or spec inference]
```
```
[SA remaining: {{n}}]  [SG from promotion: {{n}}]
```

---

#### Phase 1 -- Setup

Confirmed inputs: [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

Per-role binding:
```
[role: {{role_name}}]
  Schema 1 binding: [labels or N/A]
  Schema 2 binding: [Source labels; lock rules]
  SA/SG gaps binding this role: [list or none]
  EG gaps expected: [list or none]
```

---

#### Phase 2 -- Execute

**Execution-first ordering**: EG-producing roles run before SA-only roles.

**Role relay -- [role name]**:
- Received from: [prior or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels: [list] -- all {SA,SG,EG,QO}: YES / NO
- SA/SG gaps: [list or none]
- Produced: [artifact content added]
- EG gaps: [EG-NN list or none]

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Section confirmation: [each section: WRITTEN]

---

#### Phase 3 -- Findings

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared above.

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker] | Resolve in Findings |
| P2 | [quality] | Amend or follow-on |
| P3 | [advisory] | Log |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

> **SOURCE PRE-COMMITMENT** (required before writing any table rows):
>
> For each Source type represented in Stage 1 or Phase 2 execution, declare at least one specific
> expected finding before writing the table. The seed must name a specific gap from Stage 1 or
> Phase 2 -- a generic placeholder fails.
>
> - SA pre-commitment: "Finding seeded from [SA-NN]: [specific gap description], expected
>   severity [P1/P2/P3], action direction: [brief]"
> - SG pre-commitment (if SG gaps exist): "Finding seeded from [SG-NN]: [specific gap], severity
>   [P1/P2/P3], action direction: [brief]"
> - EG pre-commitment (if EG gaps observed): "Finding seeded from [EG-NN]: [specific gap observed
>   in execution], severity [P1/P2/P3], action direction: [brief]"
> - QO pre-commitment (if QO observations exist): "QO observation: [specific note], severity P3"
>
> Source types committed: [list]. If fewer than 2 Source types can be pre-committed from the
> available Stage 1 and execution inventory, the trace has an underlying source diversity problem
> that must be addressed before the findings table can be written.
>
> **PRE-COMMITMENT result**: Source types pre-committed: N (required: >=2). PASS / FAIL.
> If FAIL: return to Stage 1 or Phase 2 and identify findings from the missing source layer.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Additional findings beyond pre-committed seeds (optional but encouraged for each source type):

Schema 5 transition: Step 3b complete. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated.

**G-1**: Source types in Step 3b: [list]. G-1: PASS / FAIL
**G-2**: Same-Source duplicate Actions: [list or none]. G-2: PASS / FAIL
**G-3**: Severity labels: [list]. G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY**:
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Entry verdict: ALL GATES CLEARED / GATE FAILURE

> **REMEDIATION LOG** (or: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation."):
> Gate [X] FAIL: reason / action / re-check / updated result

Schema 5 transition: Step 3c complete. Step 3d is valid to begin.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all gates PASS.
Channel taxonomy activated. Phase 4 Amend entries require `[remediation channel: ...]`.
Schema 5 transition: Step 3d complete. Phase 4 is valid to begin.

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (post-remediation states only):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED

Change entry: [finding: F-NN] [source] [channel: spec/invocation/artifact/quality] [field] [change] [confirmed: YES/NO]
Dismissal entry: [finding: F-NN] [reason] [channel]

---

### Phase 5 -- Verdict and VC Compliance Ledger

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend declared | [name legend] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b SOURCE PRE-COMMITMENT | Pre-committed sources >=2 | [list pre-committed sources] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b table | All entries P1/P2/P3 | [list labels] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 | All Amend entries P1/P2/P3 | [list] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO used | [list all] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps become SG | [list promotions] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source | Only SA/SG/EG/QO; lock | [list; flag promoted] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Taxonomy activated | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Every Amend has channel | [list channels] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked | [all results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 | Gated on PASS | [GATE CLEARANCE SUMMARY] | PASS/FAIL |
| VC-5 | Schema 5 | 3b opening | PRE-COMMITMENT declared before table | [cite pre-commitment block] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Prerequisite met | [confirm 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Gates cleared | [GATE CLEARANCE SUMMARY] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Taxonomy active + Phase 4 gated | [activation + GATE CLEARANCE] | PASS/FAIL |

**VC-1 overall**: PASS/FAIL | **VC-2 overall**: PASS/FAIL | **VC-3 overall**: PASS/FAIL
**VC-4 overall**: PASS/FAIL | **VC-5 overall**: PASS/FAIL

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA. `NEEDS-REDESIGN` if EG > 3 and structural.
`USEFUL` otherwise. **Verdict**: [classification] **Rationale**: [rule fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: C-08 floor enforcement + C-13 named-artifact checkboxes

**Axis**: Output format (C-08) + Output format (C-13) -- both remaining open criteria targeted
simultaneously.

**Hypothesis**: C-08 and C-13 address different moments in Phase 3: C-08 fires after the Step 3b
table is built (the FLOOR CHECK verifies the table is complete before Step 3c); C-13 fires at
the opening of each sub-step (the checkpoint verifies the prior step's artifact before the current
step begins). The two axes are structurally independent and should not conflict. V-04 tests whether
combining them causes any regression in the criteria that V-01 and V-02 each satisfy individually.
Risk: combined instructions increase prompt density at Phase 3, possibly causing the executor to
satisfy one checkpoint format mechanically while correctly handling the other. Mitigation: the
FLOOR CHECK and PREREQUISITE CHECKPOINT blocks use different formats and fire at different moments;
an executor who completes one mechanically would still encounter the other independently.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b FLOOR CHECK, Step 3c G-3, Phase 4 | All EG-producing roles | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source, Execute relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

**Schema 1**: {P1, P2, P3}. No other severity label valid anywhere in the trace.
**Schema 2**: {SA, SG, EG, QO}. Label lock: promoted SA becomes SG in all downstream phases.
**Schema 3**: Every Phase 4 Amend entry carries `[remediation channel: ...]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (no same-Source duplicate Actions), G-3 ({P1,P2,P3}).
**Schema 5**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a done (checkpoint) | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | Step 3b FLOOR CHECK PASS (checkpoint) | Gate results all PASS | Step 3d |
| Step 3d | Step 3c all-PASS (checkpoint) | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? |
|------|-----------------|-----------------|---------------|
| [role] | [labels or N/A] | [Source labels; lock] | YES / NO |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]  [layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

#### SA-TO-SG PROMOTION

Execution-first: EG-producing roles run first. Promotion reasons may cite execution evidence.

```
SA-NN:
  Gap: [spec omission]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [execution evidence or spec inference]
```
```
[SA remaining: N]  [SG from promotion: N]
```

---

#### Phase 1 -- Setup

Inputs: [topic] [scope_in] [scope_out] [roles] [spec_version]

Per-role binding:
```
[role: {{role_name}}]
  Schema 1 binding: [labels or N/A]
  Schema 2 binding: [Source labels; lock rules]
  SA/SG gaps binding this role: [list or none]
  EG gaps expected: [list or none]
```

---

#### Phase 2 -- Execute

Execution-first ordering: EG-producing roles before SA-only roles.

**Role relay -- [role name]**:
- Received from: [prior or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels: [list] -- all {SA,SG,EG,QO}: YES / NO
- SA/SG gaps: [list or none]
- Produced: [artifact content]
- EG gaps: [EG-NN or none]

Artifact: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections: [each section: WRITTEN]

---

#### Phase 3 -- Findings

Two structural requirements apply to all Phase 3 sub-steps:
1. Each sub-step OPENS with a PREREQUISITE CHECKPOINT (C-13). The named-artifact field must cite
   the specific artifact or section produced in the prior step. Bare YES without a named referent
   is a structural failure.
2. Step 3b CLOSES with a FLOOR CHECK (C-08). The floor check must name finding IDs explicitly.
   A floor check without named IDs is a structural failure.

---

##### Step 3a -- Severity Legend Declaration

> **PREREQUISITE CHECKPOINT -- Step 3a**:
> Prerequisite: Schema 1 declared in Coverage Matrix.
> Named artifact: `Coverage Matrix, Schema 1 row -- "P1 / P2 / P3", declared above`
> Check: YES

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality] | Amend |
| P3 | [advisory] | Log |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

> **PREREQUISITE CHECKPOINT -- Step 3b**:
> Prerequisite: Step 3a complete and severity legend produced.
> Named artifact: `Step 3a severity legend table, labels P1/P2/P3 declared above`
> Check: YES

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required before advancing to Step 3c):
>
> - Finding IDs counted: [list each ID explicitly -- a bare count without IDs fails]
> - Row count: N (required: >= 3). PASS / FAIL
> - Distinct Source types: [list each type] (required: >= 2 distinct). PASS / FAIL
> - Action uniqueness: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings from the underrepresented source layer. Re-run FLOOR CHECK.
> Step 3b is BLOCKED until FLOOR CHECK PASS.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

> **PREREQUISITE CHECKPOINT -- Step 3c**:
> Prerequisite: Step 3b FLOOR CHECK PASS and findings table populated.
> Named artifact: `Step 3b FLOOR CHECK block, result: PASS, finding IDs: [list]`
> Check: YES

**G-1**: Source types in Step 3b: [list]. G-1: PASS / FAIL
**G-2**: Same-Source duplicate Actions: [list or none]. G-2: PASS / FAIL
**G-3**: Severity labels: [list]. G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required before Step 3d):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Entry verdict: ALL GATES CLEARED / GATE FAILURE -- BLOCKED

> **REMEDIATION LOG** (or: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation."):
> Gate [X] FAIL: reason / remediation (specific ID or change) / re-check / updated result

Schema 5 transition: Step 3c complete (ALL GATES CLEARED). Step 3d is valid to begin.

---

##### Step 3d -- Channel Taxonomy Activation

> **PREREQUISITE CHECKPOINT -- Step 3d**:
> Prerequisite: Step 3c all gates PASS confirmed by GATE CLEARANCE SUMMARY.
> Named artifact: `Step 3c GATE CLEARANCE SUMMARY, declaring "ALL GATES CLEARED"`
> Check: YES

Channel taxonomy activated. Phase 4 Amend entries require `[remediation channel: ...]`.
Schema 5 transition: Step 3d complete. Phase 4 is valid to begin.

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (post-remediation states -- not initial FAIL states):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED

Change: [finding: F-NN] [source] [channel] [field changed] [change] [confirmed: YES/NO]
Dismissal: [finding: F-NN] [reason] [channel]

---

### Phase 5 -- Verdict and VC Compliance Ledger

"Observed behavior: as expected" is invalid. Name specific values, IDs, results.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | Schema 1 | Step 3a | Legend declared | [name legend] | P/F |
| VC-1 | Schema 1 | Step 3b FLOOR CHECK | Floor PASS; IDs named | [cite FLOOR CHECK IDs] | P/F |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [result + labels] | P/F |
| VC-1 | Schema 1 | Phase 4 | Amend entries P1/P2/P3 | [list] | P/F |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [list all] | P/F |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted become SG | [promotions] | P/F |
| VC-2 | Schema 2 | Step 3b Source | SA/SG/EG/QO; lock | [list; promoted flagged] | P/F |
| VC-3 | Schema 3 | Step 3d | Taxonomy active | [evidence] | P/F |
| VC-3 | Schema 3 | Phase 4 | Every Amend has channel | [channels] | P/F |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked | [all results] | P/F |
| VC-4 | Schema 4 | Phase 4 pre-check | Gated on PASS | [Phase 4 GATE CLEARANCE] | P/F |
| VC-5 | Schema 5 | 3a: checkpoint | Legend named in C-13 block | [named artifact from checkpoint] | P/F |
| VC-5 | Schema 5 | 3b: checkpoint | Legend named; FLOOR CHECK PASS | [checkpoint + FLOOR CHECK] | P/F |
| VC-5 | Schema 5 | 3c: checkpoint | FLOOR CHECK named in C-13 block | [named artifact from checkpoint] | P/F |
| VC-5 | Schema 5 | 3d: checkpoint | GATE CLEARANCE SUMMARY named | [named artifact from checkpoint] | P/F |

**VC-1**: P/F | **VC-2**: P/F | **VC-3**: P/F | **VC-4**: P/F | **VC-5**: P/F

**SA remaining**: N | **SG total**: N | **EG total**: N
**Verdict**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION
**Rationale**: [rule fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Full integration: V-05 R5 base + C-08 floor enforcement + C-13 checkboxes + inertia framing

**Axis**: Multi-axis -- all three R6 axes applied + inertia framing.

**Hypothesis**: V-01 through V-04 test the new axes in isolation or in pairs. V-05 combines all
three and adds the inertia framing that was exclusive to R5 V-05 (its highest-scoring distinction).
The inertia framing targets a specific failure mode: an executor who perceives hand-compilation as
overhead is more likely to satisfy criteria mechanically rather than substantively. Opening with
the cost of skipping -- what a developer would commit to without this trace -- primes the executor
to treat structural blocks as evidence, not ceremony. The hypothesis is that motivated structural
completion plus all three output-format axes closes the remaining gaps (C-08 and C-13) while
preserving the PASS results across all other criteria.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Why this trace exists

The primary alternative to running /trace-inspect is skipping it and committing to
implementation. Without a hand-compiled trace, the skill contract is hypothetical: you do not
know whether the lifecycle phases interact correctly, whether the schemas are sufficient to
label all gaps, or whether the artifact produced would be useful to a downstream reviewer. The
hand-compiled trace is not documentation after the fact -- it is the design decision made visible
before implementation cost is spent. Every structural defect found here is a defect that would
have required implementation rework. A skill that cannot be hand-compiled cannot be implemented
correctly; the trace either passes or surfaces the reason the spec needs revision first.

This framing has one operational consequence: structural blocks in this trace are not bureaucratic
gates -- they are signals that the skill design has an unresolved problem. Treat a FAIL in any
gate, floor check, or prerequisite checkpoint as a finding, not an inconvenience.

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas before Stage 1. The Coverage Matrix is the protocol authority.
Every label, channel, and gate used downstream must be declared here; anything not declared here
is not valid protocol vocabulary.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b FLOOR CHECK (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All EG-producing roles | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run individually), Phase 4 pre-check (enforce composite) | G-1 aggregates Source across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (prerequisites + transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: Valid labels: {P1, P2, P3} only. P1 = blocks usefulness and
requires resolution before the trace can conclude USEFUL. P2 = quality improvement, address in
Amend. P3 = advisory, log and continue. No other severity label is valid anywhere in this trace.

**Schema 2 -- Gap Type Taxonomy**: SA = spec-layer gap (spec does not declare it). SG = setup
gap (known at setup time, can be supplied by an informed invoker). EG = execute gap (only
observable during execution). QO = quality observation (not a gap; advisory). Label lock
invariant: once an SA gap is promoted to SG at the SA-TO-SG PROMOTION lifecycle event, it uses
the SG label in every subsequent phase. A promoted gap that appears with the SA label downstream
is a structural violation.

**Schema 3 -- Remediation Channel Taxonomy**: spec = fix belongs in the skill spec. invocation =
fix belongs in how the skill is called. artifact = fix belongs in the artifact structure.
quality = improvement that does not require a spec change. Every Phase 4 Amend entry must
include `[remediation channel: spec / invocation / artifact / quality]`. Missing = incomplete.

**Schema 4 -- Enforcement Gate Registry**: G-1 checks source diversity (>=2 distinct Source types
in Step 3b findings). G-2 checks Action uniqueness (no two same-Source findings with identical
Action text). G-3 checks severity conformance (all Step 3b entries use only {P1, P2, P3}). Any
gate defect must be corrected and re-checked before proceeding; bypassing a FAIL is not valid.

**Schema 5 -- Sub-Step Ordering and Prerequisite Protocol**:

| Step | Prerequisite | Produces | Unblocks | Checkpoint required |
|------|-------------|---------|---------|-------------------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b | YES: named artifact = Coverage Matrix Schema 1 row |
| Step 3b | Step 3a complete (checkpoint verified) | Findings table + FLOOR CHECK PASS | Step 3c | YES: named artifact = Step 3a legend table |
| Step 3c | Step 3b FLOOR CHECK PASS (checkpoint verified) | Gate results all PASS | Step 3d | YES: named artifact = Step 3b FLOOR CHECK block |
| Step 3d | Step 3c all-PASS (checkpoint verified) | Channel taxonomy active | Phase 4 | YES: named artifact = Step 3c GATE CLEARANCE SUMMARY |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels applicable, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules] | YES / NO | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 produces a gap audit table. Stage 1 reads only `{{skill_spec_path}}`. A Stage 1
audit where all gaps are SA is a warning: the spec is dense enough to supply everything, leaving
execution blind spots. At least 2 distinct source types should appear before execution.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct Source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: SA list, SG list, EG list from Stage 1.

---

#### SA-TO-SG PROMOTION

Every SA gap from Stage 1 is evaluated at this lifecycle event. Execution-first ordering: EG-
producing roles run before SA-only roles in Phase 2 (see below). Where execution has already
run before promotion is evaluated, promotion reasons must cite the observed execution evidence.

```
SA-NN:
  Gap: [what the spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [cite execution evidence if post-execution, or spec inference if pre-execution]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original (from Stage 1): {{sg_original}}]
```

Label lock: any promoted gap appearing with SA label downstream is a structural violation.
Verify this in VC-2.

---

#### Phase 1 -- Setup

A valid Setup produces confirmed input bindings and per-role schema binding for every role. A
Setup that lists roles without schema binding and gap attribution is structurally incomplete.

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack / detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable to this role's findings, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps present]
  SA/SG gaps binding this role: [list gap IDs or "none -- no gaps affect this role at Setup"]
  EG gaps expected for this role: [list gap IDs or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**Execution-first ordering**: EG-producing roles run before SA-only roles. The SA-TO-SG PROMOTION
decision above is grounded in observed execution evidence because the EG layer runs first. A
promotion reason saying "this is probably resolved at runtime" is insufficiently grounded when
execution evidence is available to confirm or deny it.

**Role relay -- [role name]** (run EG-producing roles first):
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [gap IDs, or "none -- no gaps affect this role"]
- Produced: [artifact content added; "no artifact contribution" is valid only for support roles]
- EG gaps encountered: [EG-NN with severity, or "none -- execution completed without EG gaps"]

**Artifact write** (required after all role relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Section confirmation:

  | Section | Status |
  |---------|--------|
  | [required section 1] | WRITTEN |
  | [required section 2] | WRITTEN |

**Execute carry-forward**: [artifact path: `{{artifact_path}}`], [EG gaps added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 has two structural requirements that apply to every sub-step:

**Requirement A -- PREREQUISITE CHECKPOINT (C-13)**: Each sub-step opens with a PREREQUISITE
CHECKPOINT block before the sub-step body begins. The checkpoint states the prerequisite, names
the specific artifact produced in the prior step, and records CHECK: YES. A bare YES without a
named referent is a structural failure -- the named-artifact field must cite a specific section,
table, or block from the trace output above, not a generic path.

**Requirement B -- FLOOR CHECK (C-08)**: Step 3b closes with a FLOOR CHECK block before
advancing to Step 3c. The FLOOR CHECK names every finding ID counted, confirms row count >= 3,
confirms distinct Source types >= 2, and verifies Action uniqueness. A floor check without
explicit finding IDs is a structural failure. A FAIL result blocks Step 3c.

---

##### Step 3a -- Severity Legend Declaration

> **PREREQUISITE CHECKPOINT -- Step 3a** (required before this sub-step body):
> Prerequisite: Schema 1 declared in Coverage Matrix before Stage 1.
> Named artifact: `Coverage Matrix, Schema 1 row -- "P1 / P2 / P3", declared at top of this trace`
> Check: YES

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before the trace can conclude USEFUL |
| P2 | [what makes it a quality improvement] | Address in Phase 4 Amend or flag for follow-on |
| P3 | [what makes it advisory] | Log; no gate impact; no block |

Schema 5 transition: Step 3a complete. Severity legend produced. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

> **PREREQUISITE CHECKPOINT -- Step 3b** (required before this sub-step body):
> Prerequisite: Step 3a complete and severity legend produced.
> Named artifact: `Step 3a severity legend table, labels P1/P2/P3 defined immediately above`
> Check: YES

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required before advancing to Step 3c -- trace is BLOCKED until PASS):
>
> - Finding IDs counted: [list every ID explicitly, e.g., F-01, F-02, F-03 -- bare count fails]
> - Row count: N (required: >= 3). Row count check: PASS / FAIL
> - Distinct Source types present: [list each type, e.g., SA, EG] (required: >= 2). Source
>   diversity check: PASS / FAIL
> - Action uniqueness: any two Action cells share identical text? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: identify the deficient dimension (count or source diversity or Action duplication),
> add targeted findings from the underrepresented layer, and re-run this block. Step 3c may not
> begin until FLOOR CHECK result is PASS.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

> **PREREQUISITE CHECKPOINT -- Step 3c** (required before this sub-step body):
> Prerequisite: Step 3b FLOOR CHECK PASS and findings table populated.
> Named artifact: `Step 3b FLOOR CHECK block, result PASS, finding IDs: [list from FLOOR CHECK]`
> Check: YES

**G-1 -- Source diversity invariant**: Step 3b contains >=2 distinct Source types.
- Source types present in Step 3b: [list]
- G-1 result: PASS / FAIL

**G-2 -- Action uniqueness invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list pairs, or "no same-Source pairs exist"]
- G-2 result: PASS / FAIL

**G-3 -- Severity conformance invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list all labels used]
- G-3 result: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required structural block before Step 3d begins):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve the failed gate(s) below before continuing.

> **REMEDIATION LOG** (required if any gate records FAIL on first evaluation):
>
> If all gates PASS on first evaluation, emit instead:
> "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation loop required."
>
> Gate [X] FAIL:
> - Failure reason: [specific violation text]
> - Remediation action: [specific finding ID added, or specific Action text changed -- vague
>   descriptions like "added a finding" fail; name the specific ID and change]
> - Re-check G-[X]: PASS / FAIL
> - Updated gate result: PASS / FAIL

Schema 5 transition: Step 3c complete (GATE CLEARANCE SUMMARY declares ALL GATES CLEARED).
Step 3d is valid to begin.

---

##### Step 3d -- Channel Taxonomy Activation

> **PREREQUISITE CHECKPOINT -- Step 3d** (required before this sub-step body):
> Prerequisite: Step 3c all gates PASS, confirmed by GATE CLEARANCE SUMMARY.
> Named artifact: `Step 3c GATE CLEARANCE SUMMARY, entry verdict "ALL GATES CLEARED", above`
> Check: YES

Schema 3 channel taxonomy is now activated for Phase 4. Every Phase 4 Amend entry must include
`[remediation channel: spec / invocation / artifact / quality]`. An entry without this field is
structurally incomplete and fails VC-3.

Schema 5 transition: Step 3d complete. Channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (required structural block at Phase 4 entry -- must reflect
> post-remediation gate states, NOT the initial evaluation states. If remediation occurred in
> Step 3c, this summary must match the post-remediation results documented there, not the initial
> FAIL results. A summary that reports a FAIL that was remediated to PASS in Step 3c fails C-14.):
>
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.
> OR: GATE FAILURE -- Phase 4 BLOCKED. Return to Step 3c.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]

---

### Phase 5 -- Verdict and VC Compliance Ledger

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must name
specific values, label lists, finding IDs, gate results, or section names. A generic observation
fails the VC row.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the exact legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS with named IDs | [cite FLOOR CHECK result; list IDs] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used in audit | [list all Source labels present in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; label lock holds | [list SA gaps promoted; confirm SG downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock for promotions] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state the Step 3d activation text] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channel per Amend entry; flag any missing] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three gate results from Step 3c] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered only after GATE CLEARANCE SUMMARY CLEAR | [cite Phase 4 GATE CLEARANCE SUMMARY verdict] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 cross-role | Step 3b >= 2 Source types | [list source types and contributing roles] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3a checkpoint | Named artifact: Coverage Matrix Schema 1 row | [exact named artifact from 3a checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b checkpoint | Named artifact: Step 3a legend table | [exact named artifact from 3b checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b FLOOR CHECK | FLOOR CHECK PASS with explicit IDs | [finding IDs from FLOOR CHECK] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3c checkpoint | Named artifact: Step 3b FLOOR CHECK block | [exact named artifact from 3c checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3d checkpoint | Named artifact: Step 3c GATE CLEARANCE SUMMARY | [exact named artifact from 3d checkpoint] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL
**VC-2 overall**: PASS / FAIL
**VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL
**VC-5 overall**: PASS / FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

Classification rules (applied in priority order):
1. `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
2. `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
3. `USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired and the specific evidence]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## Summary Table

| ID | Axis(es) | C-08 mechanism | C-13 mechanism | Inertia framing |
|----|----------|---------------|----------------|----------------|
| V-01 | Output format (C-08) | FLOOR CHECK block after Step 3b; IDs must be named explicitly | Inherited: Schema 5 transitions (C-10 only) | No |
| V-02 | Output format (C-13) | Inherited: table instruction only | PREREQUISITE CHECKPOINT block opens each sub-step; named-artifact required | No |
| V-03 | Lifecycle emphasis (C-08 pre-commitment) | SOURCE PRE-COMMITMENT block opens Step 3b; seeds per Source type before table rows | Inherited: Schema 5 transitions only | No |
| V-04 | Output format (C-08) + Output format (C-13) | FLOOR CHECK block after Step 3b | PREREQUISITE CHECKPOINT opens each sub-step | No |
| V-05 | Full integration (all axes) | FLOOR CHECK block after Step 3b + SOURCE PRE-COMMITMENT context | PREREQUISITE CHECKPOINT opens each sub-step; named referent rules explicit | Yes -- opens with cost-of-skipping paragraph |

**C-08 predicted pass**: V-01 (PASS -- named IDs in FLOOR CHECK), V-03 (PASS -- pre-commitment seeds),
V-04 (PASS), V-05 (PASS); V-02 (PARTIAL -- no floor enforcement).

**C-13 predicted pass**: V-02 (PASS -- checkpoint format explicit), V-04 (PASS), V-05 (PASS);
V-01 (FAIL -- no checkpoint format), V-03 (FAIL -- no checkpoint format).

**Combined C-08 + C-13 predicted pass**: V-04, V-05 only.

**V-05 predicted score**: 100 (if combined axes close both gaps without regression in C-01 through C-12, C-14).
