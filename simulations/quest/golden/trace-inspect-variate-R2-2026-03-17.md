---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 2
rubric: trace-inspect-rubric-v2
---

# trace-inspect -- Variations v2 R2 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R1 variations discovered three excellence signals not yet in the rubric. The v2 rubric
formalizes them as C-11, C-12, C-13 (all aspirational). R1 best output achieves C-01 through C-10 PASS.
v2 aspirational state entering R2:

- C-11 (phase-entry gate clearance summary): R1 best variation records individual gate results at Step 3c
  (satisfying C-04) but never writes a consolidated named-gate summary before phase transitions. A reviewer
  confirming C-11 must manually scan Step 3c to reconstruct the tri-gate state. C-11 = FAIL.

- C-12 (gate-failure remediation loop documented): R1 best variation records FAIL on violated gates and
  includes corrective action text in the gate block. However the action text appears inside the FAIL
  declaration prose rather than as a structured re-check cycle with (1) remediation action, (2) re-check
  invocation, (3) updated result. No variation in R1 produced a traceable loop. C-12 = FAIL.

- C-13 (sub-step prerequisite verification checkboxes): R1 best variation includes Schema 5 transition
  sentences after each sub-step (satisfying C-10). No variation opens a sub-step with an explicit
  "Prerequisite: X. Check: YES / NO" block before the sub-step body begins. C-13 = FAIL.

**R2 variation axes**:

- **Lifecycle emphasis (C-11)**: Add explicit gate clearance summary blocks at two phase boundaries --
  before Step 3d begins and before Phase 4 begins (V-01). Each block names all three gates and their
  results and states the composite entry verdict. This is structurally distinct from C-04 (individual
  gate results) and from C-10 (sub-step transition sentences).

- **Lifecycle emphasis (C-12)**: Add a structured remediation loop template triggered on FAIL gates in
  Step 3c (V-02). The loop requires three fields: remediation action taken, re-check invocation, updated
  gate result. A trace that advances past a FAIL without this loop is structurally blocked. Traces where
  all gates pass on first evaluation carry an exemption notice.

- **Output format (C-13)**: Add prerequisite verification checkboxes that open each Phase 3 sub-step
  before the sub-step body (V-03). Each checkbox states the prerequisite condition and a YES/NO
  resolution. This is stronger than C-10's post-completion transition sentence: C-13 fires before the
  sub-step body, C-10 fires after.

**Combined variations**:
- V-04: C-11 + C-12 (gate clearance summary + remediation loop)
- V-05: C-11 + C-12 + C-13 (all three -- complete v2 aspirational target)

All five inherit the full R1 architecture (C-01 through C-10 PASS). What varies: only the gate handling
structures (Steps 3c, 3d, Phase 4 entry) and sub-step opening structures (Steps 3a--3d).

---

## V-01 -- Single axis: Lifecycle emphasis (C-11: Phase-entry gate clearance summary)

**Axis**: Lifecycle emphasis -- two gate clearance summary blocks added at phase boundaries.

**Hypothesis**: R1 Step 3c records "G-1 holds: PASS / G-2 holds: PASS / G-3 holds: PASS" as three
separate verdict lines inside the gate block. A reviewer confirming C-11 must parse the gate block,
locate all three results, and mentally compose the entry verdict. The consolidated gate clearance
summary makes the composite entry verdict structural: a single named block states all three gates
and the go/no-go conclusion. Risk: the summary block may be filled mechanically -- copied from the
individual gate results without adding clarity. Mitigation: the summary must name all three gates
and state the entry verdict as a single sentence, not a list of three PASS values.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol authority:
every label, channel, and gate used in any downstream phase must be declared in this table. A phase
using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings (severity label applies to every EG entry they produce) | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in each role relay uses only SA/SG/EG/QO; promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments drawn from all roles' findings (aggregate, not per-relay) | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column coverage across all roles' findings in Step 3b | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions between all sub-steps) | N/A -- applies to Findings phase structure, not individual roles | VC-5 |

**Schema 1 -- Severity Vocabulary**: A valid severity label is P1, P2, or P3. P1 blocks usefulness.
P2 is a quality improvement. P3 is advisory. Every EG finding from every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: SA = spec-layer gap. SG = setup gap. EG = execute gap. QO = quality
observation. Label lock invariant: a promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION.
A promoted gap retaining SA is a structural violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes `[remediation channel:
spec / invocation / artifact / quality]`. An entry without a channel field is structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**: G-1: Step 3b contains >=2 distinct Source types. G-2: no two
same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. A
structural defect must be corrected and re-checked; it cannot be bypassed.

**Schema 5 -- Sub-Step Ordering**: 3b valid only after 3a produces a severity legend. 3c valid only
after 3b has >=2 findings. 3d valid only after 3c is all-PASS. Phase 4 valid only after 3d activates
the channel taxonomy.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's EG findings, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules for promoted gaps] | [any Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 produces a gap audit table covering all three source layers and a relay record carrying
the inventory into Stage 2. Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where gaps cluster at
one source type is structurally incomplete.

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
[layer diversity: `{{diversity_status}}`]. A valid Stage 2 carries all gaps forward without
re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime promotes
to SG. A gap requiring a spec change remains SA. A trace that skips this evaluation is structurally
incomplete.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock invariant: a promoted gap using its SA label in any downstream phase is a
structural violation.

---

#### Phase 1 -- Setup

A valid Setup produces: confirmed input bindings for all declared inputs, and a per-role schema binding
and gap attribution block for each role. A Setup listing roles without schema binding declarations is
structurally incomplete.

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [which severity labels apply to this role's findings, or "N/A"]
  Schema 2 binding: [which Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

A valid Execute produces: the hand-compiled artifact `{topic}-skill-trace-{date}.md` and a per-role
relay for each role with all required fields. A role relay without the "Schema 2 compliance" field is
structurally invalid.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5 and each Schema 5
prerequisite is satisfied before the sub-step begins.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: a severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: a merged findings table with >=2 entries (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).
Schema 5 output: invariant results for G-1, G-2, G-3 -- ALL-PASS required to unblock Step 3d.

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: structural defect. Identify the missing source layer. Add a finding. Re-check G-1.

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none -- all Source types unique"]
- G-2 holds: PASS / G-2 violated: FAIL
- If FAIL: structural defect. Revise Action text to name distinct targets. Re-check G-2.

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL
- If FAIL: structural defect. Relabel non-conforming entries. Re-check G-3.

> **Gate Clearance Summary** (V-01 addition):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) above before continuing.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

Schema 5 prerequisite: Step 3c all invariants hold (confirmed by Gate Clearance Summary above).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4 (unblocks Phase 4).

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

> **Phase 4 Gate Clearance Summary** (V-01 addition):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.
> OR: GATE FAILURE -- Phase 4 is BLOCKED. Return to Step 3c.

A valid Phase 4 begins only when the Gate Clearance Summary above declares ALL GATES CLEARED.

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.

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
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

The Verdict is valid only after Phase 4 completes. "Observed behavior: as expected" is structurally
invalid; Observed behavior must name specific values, labels, role name, or invariant status.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state what the legend said] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only {P1, P2, P3} | [list severity values used; flag any outside schema] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only {P1,P2,P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role producing EG] | EG findings use only {P1,P2,P3} | [list severity labels by this role] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used in audit | [list all Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label; label lock holds | [list SA gaps promoted; confirm SG downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [list Source labels in Step 3b; confirm label lock] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role name] | Source labels from {SA,SG,EG,QO}; label lock honored | [list Source labels by this role; confirm promoted gaps] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every Amend entry includes channel field | [list channels per Amend entry; flag missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked with explicit PASS/FAIL | [state G-1/G-2/G-3 results at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 entered only when all gates PASS | [state gate clearance summary at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1 cross-role) | >=2 distinct Source types in Step 3b | [list Source types and roles contributing each] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | Step 3b valid only after Step 3a complete | [confirm what evidence showed Step 3a done] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | Step 3c valid only after Step 3b has >=2 entries | [state entry count in Step 3b before Step 3c] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | Step 3d valid only after Step 3c all-PASS | [state gate results before Step 3d, including Gate Clearance Summary] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 valid only after Step 3d activates channel taxonomy | [state activation confirmation and Phase 4 Gate Clearance Summary] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Lifecycle emphasis (C-12: Gate-failure remediation loop)

**Axis**: Lifecycle emphasis -- structured remediation loop template triggered on FAIL gates in Step 3c.

**Hypothesis**: R1 Step 3c records FAIL results with corrective action text embedded in the FAIL
declaration prose. A reviewer confirming C-12 cannot distinguish a "note that something must be fixed"
from a traceable remediation loop because there is no structural re-check. V-02 adds a required
`Gate-N Remediation` sub-block that activates only on FAIL: it names the specific change made to
Step 3b, invokes a re-check, and states the updated result. Traces where all gates pass on first
evaluation carry an explicit exemption notice (satisfying C-12 as "exempt"). Risk: the remediation
sub-block may be filled with vague action text ("added a finding") rather than a specific structural
change. Mitigation: the remediation action must name the specific finding ID added or the specific
text changed, not a category.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol authority.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1**: Valid severity labels: {P1, P2, P3}. P1 = blocks usefulness. P2 = quality improvement.
P3 = advisory. Every EG finding from every role uses only {P1, P2, P3}.

**Schema 2**: SA = spec-layer. SG = setup. EG = execute. QO = quality observation. Label lock invariant:
promoted SA gap uses SG in all downstream phases. A promoted gap retaining SA is a structural violation.

**Schema 3**: Every Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact /
quality]`. An entry without a channel field is structurally incomplete.

**Schema 4**: G-1: >=2 distinct Source types in Step 3b. G-2: no two same-Source findings share
identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. Any defect must be corrected
and re-checked; it cannot be bypassed.

**Schema 5**: Ordering invariant for sub-steps 3a -> 3b -> 3c -> 3d -> Phase 4.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

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

Stage 2 carries all gaps forward from the relay without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).
Schema 5 output: invariant results for G-1, G-2, G-3 -- ALL-PASS required to unblock Step 3d.

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL

> **G-1 Remediation** (V-02 addition -- activate only if G-1 = FAIL):
> Defect: [specific reason G-1 failed -- which source layer was missing]
> Action taken: [specific finding ID added and its Source label, e.g. "added F-05 (Source: EG)"]
> Re-check: Source types present after action: [updated list] -- G-1 holds: PASS / FAIL

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none -- all Source types unique"]
- G-2 holds: PASS / G-2 violated: FAIL

> **G-2 Remediation** (V-02 addition -- activate only if G-2 = FAIL):
> Defect: [specific finding pair sharing Action text, e.g. "F-02 and F-04 both Action: 'add spec section'"]
> Action taken: [specific text change made, e.g. "F-04 Action revised to 'add spec section for error codes'"]
> Re-check: Duplicate Action pairs after revision: [list or "none"] -- G-2 holds: PASS / FAIL

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL

> **G-3 Remediation** (V-02 addition -- activate only if G-3 = FAIL):
> Defect: [specific entry ID with non-conforming label, e.g. "F-03 uses label 'critical'"]
> Action taken: [specific relabel, e.g. "F-03 Severity revised to P1"]
> Re-check: Non-conforming labels after revision: [list or "none"] -- G-3 holds: PASS / FAIL

> **Remediation exemption notice** (V-02 addition -- include when all gates pass on first evaluation):
> All three gates (G-1, G-2, G-3) passed on first evaluation. No remediation loops were activated.
> C-12 exemption applies.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all invariants hold (G-1, G-2, G-3 = PASS, confirmed above).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 invariant violated. Phase 4 is structurally blocked. Return to Step 3c.

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

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared | [actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries {P1,P2,P3} | [severity values used; flag any outside schema] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified | [G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries {P1,P2,P3} | [severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role] | EG findings {P1,P2,P3} | [labels by role] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO used | [Source labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps use SG | [list promoted; confirm SG downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | {SA,SG,EG,QO}; promoted = SG | [Source labels in Step 3b; label lock] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role] | Source from schema; label lock | [Source labels by role; promoted gaps] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry has channel field | [channels per Amend entry; flag missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked | [gate results at Step 3c; remediation loops if any] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | All gates PASS before Phase 4 | [invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | >=2 distinct Source types | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | 3b valid after 3a | [evidence Step 3a complete] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | 3c valid after 3b >=2 entries | [entry count before 3c] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | 3d valid after all-PASS | [gate results before 3d] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 valid after channel taxonomy active | [activation confirmation before Phase 4] | PASS / FAIL |

**VC-1 through VC-5 overall**: PASS if all rows in each group PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Output format (C-13: Sub-step prerequisite verification checkboxes)

**Axis**: Output format -- each Phase 3 sub-step opens with an explicit prerequisite verification
block before the sub-step body begins.

**Hypothesis**: R1 best variation satisfies C-10 (Schema 5 transition sentences after each sub-step
completes) but does not satisfy C-13 (prerequisite check before the sub-step begins). The difference
is the direction of the check: C-10 says "the prior step is done, so this step is valid," stated at
the END of the prior step or the START of this step as a retrospective confirmation. C-13 says "I am
about to run this step; let me verify its prerequisite is present NOW," stated at the TOP of the
sub-step as a prospective verification. Risk: the checkbox block becomes mechanical ("YES" is always
written without inspection). Mitigation: the prerequisite statement must name the specific artifact
produced by the prior step -- not a generic "prior step complete" assertion -- so a reader can verify
the claim against the trace body.

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

**Schema 1**: P1 = blocks usefulness. P2 = quality improvement. P3 = advisory.
**Schema 2**: SA/SG/EG/QO. Label lock: promoted SA gap uses SG downstream.
**Schema 3**: Every Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (distinct Action text per Source), G-3 (only {P1,P2,P3}).
**Schema 5**: 3a -> 3b -> 3c -> 3d -> Phase 4. Each sub-step requires its prerequisite before beginning.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

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

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

---

##### Step 3a -- Severity Legend Declaration

> **Prerequisite check** (V-03 addition):
> Prerequisite: Schema 1 (P1/P2/P3) is declared in the Coverage Matrix above.
> Check: YES / NO
> If NO: Coverage Matrix is incomplete. Declare Schema 1 before proceeding.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete -- severity legend produced. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

> **Prerequisite check** (V-03 addition):
> Prerequisite: Step 3a has produced a severity legend defining P1, P2, and P3 for this trace.
> Check: YES / NO -- [name the specific table row(s) from Step 3a that confirm the legend exists]
> If NO: Step 3a is incomplete. Return to Step 3a and produce the legend before proceeding.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

> **Prerequisite check** (V-03 addition):
> Prerequisite: Step 3b has produced a findings table with >=2 entries.
> Check: YES / NO -- [state the entry count in the Step 3b table above]
> If NO: Step 3b is incomplete. Return to Step 3b and add entries until >=2 before proceeding.

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL
- If FAIL: structural defect. Identify the missing source layer. Add a finding. Re-check G-1.

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none -- all Source types unique"]
- G-2 holds: PASS / G-2 violated: FAIL
- If FAIL: structural defect. Revise Action text. Re-check G-2.

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL
- If FAIL: structural defect. Relabel non-conforming entries. Re-check G-3.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

---

##### Step 3d -- Channel Taxonomy Activation

> **Prerequisite check** (V-03 addition):
> Prerequisite: Step 3c has produced G-1 = PASS, G-2 = PASS, and G-3 = PASS.
> Check: YES / NO -- G-1: [PASS/FAIL], G-2: [PASS/FAIL], G-3: [PASS/FAIL]
> If NO: Step 3c has unresolved gate failures. Return to Step 3c and resolve all FAIL gates before
> proceeding.

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Schema 4 invariant violated. Phase 4 is structurally blocked. Return to Step 3c.

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

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared | [actual definitions written] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries {P1,P2,P3} | [severity values used] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries {P1,P2,P3} | [severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role] | EG findings {P1,P2,P3} | [labels by role] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO used | [Source labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps use SG | [promoted list; SG confirmed downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | {SA,SG,EG,QO}; promoted = SG | [Source labels; label lock] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role] | Source from schema; label lock | [Source labels by role] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry has channel field | [channels per entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked | [gate results at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | All gates PASS before Phase 4 | [invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | >=2 distinct Source types | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | 3b valid after 3a | [prerequisite check YES/NO and named artifact from Step 3a] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | 3c valid after 3b >=2 entries | [prerequisite check YES/NO and entry count named] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | 3d valid after all-PASS | [prerequisite check YES/NO and gate results named] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 valid after channel taxonomy | [prerequisite check YES/NO and activation confirmed] | PASS / FAIL |

**VC-1 through VC-5 overall**: PASS if all rows in each group PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: C-11 + C-12 (Gate clearance summary + Remediation loop)

**Axes combined**: Lifecycle emphasis (C-11: consolidated gate clearance summary at phase boundaries)
+ Lifecycle emphasis (C-12: structured remediation loop on FAIL gates).

**Hypothesis**: C-11 and C-12 are co-located in Step 3c but address different failure modes. C-11
ensures phase-boundary visibility (the composite entry verdict is explicit before each transition).
C-12 ensures structural correction traceability (any FAIL has a documented resolution path). When
combined, the gate clearance summary appears both AFTER the individual gate checks (confirming the
current state of all three gates) and BEFORE the phase transition (acting as the go/no-go decision
artifact). The remediation loops provide the correction history that makes the clearance summary
trustworthy: the summary does not just assert PASS -- it is preceded by documented corrections if
any gate required them. Risk: when both are present and all gates pass, the exemption notice (C-12)
and the clearance summary (C-11) may feel redundant. Mitigation: the exemption notice is scoped to
C-12 (no remediation loops activated) while the clearance summary is scoped to C-11 (entry verdict
for the transition). The two serve different reviewers checking different criteria.

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

**Schema 1**: P1 = blocks usefulness. P2 = quality improvement. P3 = advisory.
**Schema 2**: SA/SG/EG/QO. Label lock: promoted SA gap uses SG downstream.
**Schema 3**: Every Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (distinct Action text per Source), G-3 (only {P1,P2,P3}).
**Schema 5**: 3a -> 3b -> 3c -> 3d -> Phase 4. Sub-steps in declared order; prerequisites before each.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

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

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b populated (>=2 entries).

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL

> **G-1 Remediation** (V-04 C-12 -- activate only if G-1 = FAIL):
> Defect: [specific reason G-1 failed -- which source layer was missing]
> Action taken: [specific finding ID added and its Source label]
> Re-check: Source types present after action: [updated list] -- G-1 holds: PASS / FAIL

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none"]
- G-2 holds: PASS / G-2 violated: FAIL

> **G-2 Remediation** (V-04 C-12 -- activate only if G-2 = FAIL):
> Defect: [specific finding pair sharing Action text]
> Action taken: [specific text revision made]
> Re-check: Duplicate pairs after revision: [list or "none"] -- G-2 holds: PASS / FAIL

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL

> **G-3 Remediation** (V-04 C-12 -- activate only if G-3 = FAIL):
> Defect: [specific entry with non-conforming label]
> Action taken: [specific relabel performed]
> Re-check: Non-conforming labels after revision: [list or "none"] -- G-3 holds: PASS / FAIL

> **Remediation exemption notice** (V-04 C-12 -- include when all gates pass on first evaluation):
> All three gates passed on first evaluation. No remediation loops activated. C-12 exemption applies.

> **Gate Clearance Summary** (V-04 C-11):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) and activate remediation loop(s)
> above before continuing.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all invariants hold -- confirmed by Gate Clearance Summary above.

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

> **Phase 4 Gate Clearance Summary** (V-04 C-11):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.
> OR: GATE FAILURE -- Phase 4 is BLOCKED. Return to Step 3c.

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Phase 4 is structurally blocked. Return to Step 3c.

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

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared | [actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries {P1,P2,P3} | [severity values used] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries {P1,P2,P3} | [severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role] | EG findings {P1,P2,P3} | [labels by role] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO used | [Source labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps use SG | [promoted list; SG confirmed] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | {SA,SG,EG,QO}; promoted = SG | [Source labels; label lock] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role] | Source from schema; label lock | [Source labels by role] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry has channel field | [channels per entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked | [gate results; remediation loops if any; clearance summary] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | All gates PASS before Phase 4 | [Phase 4 Gate Clearance Summary verdict] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | >=2 distinct Source types | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | 3b valid after 3a | [evidence Step 3a complete] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | 3c valid after 3b >=2 entries | [entry count before 3c] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | 3d valid after all-PASS | [Gate Clearance Summary verdict before Step 3d] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 valid after channel taxonomy | [activation + Phase 4 Gate Clearance Summary] | PASS / FAIL |

**VC-1 through VC-5 overall**: PASS if all rows in each group PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: C-11 + C-12 + C-13 (All three aspirational criteria)

**Axes combined**: Lifecycle emphasis (C-11: gate clearance summaries at phase boundaries) +
Lifecycle emphasis (C-12: structured remediation loop on FAIL gates) + Output format (C-13:
prerequisite verification checkboxes opening each Phase 3 sub-step).

**Hypothesis**: V-04 shows that C-11 and C-12 integrate without conflict because C-11 fires at the
summary layer (after all gate checks and remediations) and C-12 fires at the correction layer (within
the gate block). V-05 adds C-13, which fires at the entry layer (before the sub-step body). The three
form a temporal bracket: C-13 fires BEFORE the sub-step (what must be true to begin), C-12 fires
WITHIN the gate step (what to do when a gate fails), and C-11 fires AFTER the gates (what the
composite result is before transitioning). Together they close three distinct visibility gaps: (1) a
tracer who skips a prerequisite is caught by C-13's checkpoint before any work begins; (2) a gate
failure that would normally be noted and silently bypassed is forced into a documented loop by C-12;
(3) a reviewer who needs the composite phase-entry decision without parsing individual gate prose has
C-11's summary block. Risk: the three additions create structural verbosity that increases the prompt
length. The increased length may cause the tracer to omit one of the three under length pressure.
Mitigation: all three additions use compressed block formats (a two-line prerequisite check, a
three-field remediation entry, a two-line clearance summary) to minimize added length.

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

**Schema 1**: P1 = blocks usefulness. P2 = quality improvement. P3 = advisory.
**Schema 2**: SA/SG/EG/QO. Label lock: promoted SA gap uses SG downstream.
**Schema 3**: Every Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (distinct Action text per Source), G-3 (only {P1,P2,P3}).
**Schema 5**: 3a -> 3b -> 3c -> 3d -> Phase 4. Prerequisites verified before each sub-step begins.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

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

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

---

##### Step 3a -- Severity Legend Declaration

> **Prerequisite check** (V-05 C-13):
> Prerequisite: Schema 1 (P1/P2/P3) is declared in the Coverage Matrix above.
> Check: YES / NO
> If NO: Coverage Matrix is incomplete. Declare Schema 1 before proceeding.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete -- severity legend produced. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

> **Prerequisite check** (V-05 C-13):
> Prerequisite: Step 3a has produced a severity legend defining P1, P2, and P3 for this trace.
> Check: YES / NO -- [name the specific row(s) from Step 3a confirming the legend exists]
> If NO: Return to Step 3a and produce the legend before proceeding.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with >=2 entries. Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

> **Prerequisite check** (V-05 C-13):
> Prerequisite: Step 3b has produced a findings table with >=2 entries.
> Check: YES / NO -- [state the entry count in the Step 3b table above]
> If NO: Return to Step 3b and add entries until >=2 before proceeding.

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1 holds: PASS / G-1 violated: FAIL

> **G-1 Remediation** (V-05 C-12 -- activate only if G-1 = FAIL):
> Defect: [which source layer was missing]
> Action taken: [specific finding ID added and its Source label]
> Re-check: Source types after action: [updated list] -- G-1 holds: PASS / FAIL

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none"]
- G-2 holds: PASS / G-2 violated: FAIL

> **G-2 Remediation** (V-05 C-12 -- activate only if G-2 = FAIL):
> Defect: [specific finding pair sharing Action text]
> Action taken: [specific text revision made]
> Re-check: Duplicate pairs after revision: [list or "none"] -- G-2 holds: PASS / FAIL

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3 holds: PASS / G-3 violated: FAIL

> **G-3 Remediation** (V-05 C-12 -- activate only if G-3 = FAIL):
> Defect: [specific entry with non-conforming label]
> Action taken: [specific relabel]
> Re-check: Non-conforming labels after revision: [list or "none"] -- G-3 holds: PASS / FAIL

> **Remediation exemption notice** (V-05 C-12 -- include when all gates pass on first evaluation):
> All three gates passed on first evaluation. No remediation loops activated. C-12 exemption applies.

> **Gate Clearance Summary** (V-05 C-11):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED. Resolve failed gate(s) before continuing.

---

##### Step 3d -- Channel Taxonomy Activation

> **Prerequisite check** (V-05 C-13):
> Prerequisite: Step 3c has produced G-1 = PASS, G-2 = PASS, and G-3 = PASS (confirmed by Gate
> Clearance Summary above).
> Check: YES / NO -- Gate Clearance Summary verdict: [ALL GATES CLEARED / GATE FAILURE]
> If NO: Return to Step 3c and resolve all FAIL gates before proceeding.

A valid Phase 4 Amend entry includes `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

> **Phase 4 Gate Clearance Summary** (V-05 C-11):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.
> OR: GATE FAILURE -- Phase 4 is BLOCKED. Return to Step 3c.

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Phase 4 is structurally blocked. Return to Step 3c.

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

The Verdict is valid only after Phase 4 completes. "Observed behavior: as expected" is structurally
invalid. Observed behavior must name specific values, labels, role names, or invariant status.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared with P1/P2/P3 definitions | [state actual definitions written] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries {P1,P2,P3} | [list severity values used; flag any outside schema] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified | [G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries {P1,P2,P3} | [severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay -- [role] | EG findings {P1,P2,P3} | [labels by this role] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO used | [Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps use SG; label lock holds | [list promoted; SG confirmed downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | {SA,SG,EG,QO}; promoted = SG | [Source labels; label lock confirmed] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay -- [role] | Source from schema; label lock | [Source labels by role; promoted gaps] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation evidence at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry has channel field | [channels per Amend entry; flag missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked with PASS/FAIL | [gate results; remediation loops activated; Gate Clearance Summary] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | All gates PASS before Phase 4 | [Phase 4 Gate Clearance Summary verdict] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | >=2 distinct Source types | [Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a -> 3b | 3b valid after 3a complete | [prerequisite check YES/NO; named artifact from Step 3a] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b -> 3c | 3c valid after 3b >=2 entries | [prerequisite check YES/NO; entry count named] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c -> 3d | 3d valid after all-PASS | [prerequisite check YES/NO; Gate Clearance Summary verdict] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d -> Phase 4 | Phase 4 valid after channel taxonomy active | [prerequisite check YES/NO; activation + Phase 4 Gate Clearance Summary] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
