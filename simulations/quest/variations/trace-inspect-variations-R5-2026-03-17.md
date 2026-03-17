Now I have the full baseline. Let me generate the 5 variations.

---

# trace-inspect — Round 5 Variations (V-01 through V-05)

**Skill**: `trace-inspect`
**Round**: 5
**Rubric**: v3 (C-01 through C-14)
**Base**: T3 prompt (signal-trace-skill.t3/SKILL.md)

---

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Role sequence | Execution-first ordering surfaces EG gaps before SA-TO-SG promotion, making the promotion decision evidence-grounded rather than spec-layer inferred |
| V-02 | Output format | Structured checkbox prerequisite blocks force named-artifact verification (targets C-13: bare "satisfied above" fails; named artifact passes) |
| V-03 | Lifecycle emphasis | Named structural blocks for gate-clearance summary and remediation log enforce C-11/C-12/C-14 as required outputs, not narrative inference |
| V-04 | Phrasing register + lifecycle | Conversational second-person register with compressed Phase 1/2 reduces parsing overhead before Phase 3; more attention available for high-ceremony gate work |
| V-05 | Inertia framing + role sequence + gate structure | Status-quo cost preamble motivates rigor; execution-first ordering + named GATE CLEARANCE SUMMARY + mandatory C-12 EXEMPTION notice address the three remaining aspirational gaps simultaneously |

---

## V-01 — Role Sequence: Execution-First Ordering

**Axis**: Role sequence
**Hypothesis**: Running EG-producing roles before spec-layer roles surfaces structural gaps before the SA-TO-SG promotion decision. The promotion choices become evidence-grounded (did execution actually resolve this?) rather than spec-inferred (could a competent invoker supply this?). This produces a more defensible gap inventory and better C-06 outcomes.

---

```
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
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate across all roles' findings | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source coverage across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A -- applies to Findings phase structure | VC-5 |

**Schema 1 -- Severity Vocabulary**: Valid labels are P1, P2, P3. P1 = blocks artifact usefulness.
P2 = quality improvement, non-blocking. P3 = advisory. Any other label is structurally invalid.

**Schema 2 -- Gap Type Taxonomy**: Valid Source labels are SA (spec-layer gap), SG (setup gap),
EG (execution gap), QO (quality observation). Label lock invariant: a promoted SA gap uses
the SG label in all phases after SA-TO-SG PROMOTION. SA retained after promotion is a violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes
`[remediation channel: spec / invocation / artifact / quality]`. Missing field = structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**:
- G-1: Step 3b contains >=2 distinct Source types. Fewer = structural defect; cannot advance.
- G-2: No two same-Source findings share identical Action text. Duplicate actions = structural defect.
- G-3: All Step 3b entries use only {P1, P2, P3}. Any other severity = structural defect.
All three must PASS before Phase 4 begins.

**Schema 5 -- Sub-Step Ordering**: Each sub-step is only valid when its predecessor has produced
its required output. Out-of-order execution is structurally invalid.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

Declare every role in the execution sequence before Stage 2 begins. One row per role in spec.
A role without explicit schema binding is invalid in this trace.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules for promoted gaps] | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

Read only `{{skill_spec_path}}` -- do not consult the test invocation here.

Examine all three source layers before declaring done. A Stage 1 where all gaps cluster at
one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record (state all four fields):

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

Carry all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

[[ NOTE: In V-01, SA-TO-SG PROMOTION runs AFTER the execution pass (all EG-producing roles
have relayed), not before Phase 2 begins. This placement is deliberate: promotion decisions
are informed by observed execution evidence, not spec-layer inference alone. ]]

After the execution pass completes, evaluate every SA gap from the Stage 1 relay:

```
SA-NN:
  Gap: [what spec does not declare]
  Execution evidence: [what the execution-pass roles observed about this gap]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence grounded in execution evidence, not spec inference]
```

After promotion:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant: a promoted gap using its SA label in any downstream phase is a
structural violation.

---

#### Phase 1 -- Setup

Confirmed input bindings:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role schema binding and gap attribution (for each role in `[roles: ...]`):

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable to this role's findings, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Execution order assignment** (V-01 rule -- assign before Phase 2 begins):

1. EXECUTION PASS: roles whose primary output generates EG findings (runtime actors,
   implementation components, system behavior evaluators). Run these first.
2. SA-TO-SG PROMOTION: runs after execution pass completes, using execution evidence.
3. SPEC PASS: roles whose primary output generates SA gaps (spec authors, designers,
   requirement owners). Run these after promotion.
4. ORCHESTRATION PASS: roles that coordinate or synthesize (reviewers, orchestrators).
   Run these last.

State the assignment: list each role and its pass assignment.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

**EXECUTION PASS** -- run all execution-layer roles in the assigned order.

For each execution-layer role, record:

**Role relay -- [role name] (EXECUTION PASS)**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

When all execution-pass roles are complete, run SA-TO-SG PROMOTION (see above).

**SPEC PASS** -- run all spec-layer roles using post-promotion gap inventory.

**Role relay -- [role name] (SPEC PASS)**:
- Received from: [prior role or SA-TO-SG PROMOTION event]
- Received values: [name: value, ...] -- note: SA gaps may now be SG-labeled
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list using post-promotion labels]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**ORCHESTRATION PASS** -- run all orchestration roles.

**Role relay -- [role name] (ORCHESTRATION PASS)**:
- Received from: [prior role]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Write the hand-compiled artifact to:
`simulations/trace/skill/{topic}-skill-trace-{date}.md`

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 runs sub-steps in Schema 5 order. Each sub-step is only valid when its predecessor
has produced its required output. Out-of-order execution is structurally invalid.

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
Schema 5 output: invariant results for G-1, G-2, G-3 (all-PASS unblocks Step 3d).

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL
- If FAIL: identify missing source layer, add finding, re-check G-1.

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none"]
- G-2: PASS / FAIL
- If FAIL: revise Action text to distinct targets, re-check G-2.

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL
- If FAIL: relabel non-conforming entries, re-check G-3.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS.
**Gate clearance: G-1 [PASS/FAIL], G-2 [PASS/FAIL], G-3 [PASS/FAIL] -- Phase 4 is valid to begin.**

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS (G-1, G-2, G-3 = PASS).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4 (unblocks Phase 4).

Channel taxonomy active: spec / invocation / artifact / quality.
Every Phase 4 Amend entry must include `[remediation channel: ...]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

Phase 4 is only valid when G-1 = PASS, G-2 = PASS, G-3 = PASS.

Invariant status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
If any = FAIL: Phase 4 is structurally blocked. Return to Step 3c.

Change entry (six fields required):
- [finding: F-NN]
- [source: ] (Schema 2; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

Dismissal entry (four fields required):
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

Fill every row. "Observed behavior: as expected" is invalid -- name specific values observed.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | Schema 1 | Step 3a | Legend declared P1/P2/P3 | [actual definitions] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b | Only {P1,P2,P3} | [severity values used, counts] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Only {P1,P2,P3} | [severity values in Amend entries] | PASS/FAIL |
| VC-1 | Schema 1 | Role relay (each EG-producing role) | EG findings use only {P1,P2,P3} | [labels used by this role's EG findings] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used | [all Source labels in Stage 1 table] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; label lock holds | [SA gaps promoted; confirm SG label downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [Source labels in 3b; promoted gap labels] | PASS/FAIL |
| VC-2 | Schema 2 | Role relay (each role) | Source labels from {SA,SG,EG,QO}; label lock honored | [Source labels per role; promoted gap confirmation] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence at 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked explicit | [all three results at Step 3c] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | All gates PASS at Phase 4 entry | [invariant status at Phase 4 entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b G-1 cross-role | >=2 Source types across all roles | [Source types and contributing roles] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3b valid only after 3a legend | [what confirmed 3a complete] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | 3c valid only after 3b >=2 entries | [entry count in 3b at 3c start] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | 3d valid only after all-PASS | [gate results before 3d] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel active | [activation confirmation before Phase 4] | PASS/FAIL |

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

- NEEDS-SPEC-REVISION: any P1 SA gap remains SA after promotion.
- NEEDS-REDESIGN: EG gaps exceed 3 and indicate a structural role gap.
- USEFUL: otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## V-02 — Output Format: Structured Prerequisite Checkboxes

**Axis**: Output format
**Hypothesis**: Replacing prose prerequisite lines (`Schema 5 prerequisite: X, satisfied above`) with explicit named-artifact checkbox blocks forces the model to identify the specific table, row, or section satisfying each prerequisite. A bare "satisfied above" is a mechanical pass-through; a named artifact is evidence. This directly targets C-13, which fails any trace that opens sub-steps without named-artifact verification.

The Coverage Matrix, Stage 1, SA-TO-SG PROMOTION, Phase 1, and Phase 2 sections are identical to V-01 baseline. The change is entirely in Phase 3 sub-step openings and Phase 4 entry.

---

```
You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[[ identical to V-01 Coverage Matrix and schema definitions ]]

---

### Stage 1 -- Source-Layer Audit

[[ identical to V-01 Stage 1 ]]

---

### Stage 2 -- Hand-Compilation

[[ identical to V-01 Stage 2, including SA-TO-SG PROMOTION and Phase 1 ]]

---

#### Phase 2 -- Execute

[[ identical to V-01 Phase 2, using standard (non-execution-first) role ordering ]]

The role order follows the order declared in `{{skill_spec_path}}`. Write the hand-compiled
artifact to `simulations/trace/skill/{topic}-skill-trace-{date}.md`.

---

#### Phase 3 -- Findings

Phase 3 runs sub-steps in Schema 5 order. Each sub-step opens with a PREREQUISITE CHECK
block. The check must name a specific artifact, table, or section heading -- not "satisfied
above" or "see above." A named referent is required; a bare YES without a named artifact
is treated as unverified.

---

##### Step 3a -- Severity Legend Declaration

> PREREQUISITE CHECK
> - Condition: Schema 1 (Severity Vocabulary) must be declared in the Coverage Matrix before
>   Step 3a begins.
> - Named artifact: [state the exact section heading where Schema 1 is declared in this trace --
>   e.g., "Schema 1 -- Severity Vocabulary block in the Coverage Matrix above"]
> - Check: YES / NO
>
> If NO: Schema 1 declaration is missing. Return to Coverage Matrix. Do not proceed.

Step 3a produces the severity legend for this trace:

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition for this trace] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

> STEP 3a CLOSE: Severity legend produced. Step 3b prerequisite is now satisfiable.

---

##### Step 3b -- Findings Table

> PREREQUISITE CHECK
> - Condition: Step 3a must have produced a severity legend (P1/P2/P3 defined for this trace).
> - Named artifact: [state the exact table heading or section where the Step 3a legend appears --
>   e.g., "Step 3a Severity Legend table, rows P1/P2/P3 with trace-specific definitions"]
> - Check: YES / NO
>
> If NO: Step 3a legend is absent or incomplete. Complete Step 3a before proceeding.

Findings table -- use only Schema 2 Source labels and Step 3a severity labels:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> STEP 3b CLOSE: [N] findings recorded. If N < 2, add findings before proceeding.
> Step 3c prerequisite is satisfiable when entry count >= 2. Current count: [N].

---

##### Step 3c -- Enforcement Gates

> PREREQUISITE CHECK
> - Condition: Step 3b must have produced a findings table with >= 2 entries.
> - Named artifact: [state the exact Step 3b table heading and row count --
>   e.g., "Step 3b Findings Table, rows F-01 through F-0N, N >= 2"]
> - Check: YES / NO
>
> If NO: Step 3b table is empty or has fewer than 2 entries. Complete Step 3b first.

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list from Step 3b Source column]
- Distinct count: [N]
- G-1: PASS (N >= 2) / FAIL (N < 2)
- If FAIL: [REMEDIATION] identify missing source layer -> add finding from that layer ->
  re-check G-1 -> record updated result here: G-1 post-remediation: PASS / FAIL

**G-2 Invariant**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list pairs or "no same-Source pairs"]
- G-2: PASS / FAIL
- If FAIL: [REMEDIATION] differentiate Action text -> re-check G-2 -> record result: PASS / FAIL

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present in Step 3b: [list]
- G-3: PASS / FAIL
- If FAIL: [REMEDIATION] relabel non-conforming entries -> re-check G-3 -> record: PASS / FAIL

**C-12 COMPLIANCE**: If all three gates passed on first evaluation with no FAIL recorded:
> C-12 EXEMPTION: all gates (G-1, G-2, G-3) passed on first evaluation. No remediation loop
> required. Exemption applies.

If any gate required remediation, record the complete remediation loop above (each FAIL ->
action taken -> re-check -> updated result).

**GATE CLEARANCE SUMMARY** (required before Step 3d):
> G-1 [PASS/FAIL], G-2 [PASS/FAIL], G-3 [PASS/FAIL] -- Step 3d is valid to begin.
> Phase 4 is valid to begin when Step 3d completes.

> STEP 3c CLOSE: All gate results recorded. Proceed to Step 3d only if summary shows all PASS.

---

##### Step 3d -- Channel Taxonomy Activation

> PREREQUISITE CHECK
> - Condition: Step 3c must have produced PASS results for G-1, G-2, and G-3 (all three).
> - Named artifact: [state the exact Gate Clearance Summary block in Step 3c --
>   e.g., "Gate Clearance Summary block in Step 3c, reading G-1 PASS, G-2 PASS, G-3 PASS"]
> - Check: YES / NO
>
> If NO: one or more gates did not pass. Return to Step 3c. Do not proceed.

Channel taxonomy active for Phase 4: spec / invocation / artifact / quality.
Every Phase 4 Amend entry must include `[remediation channel: ...]`. An Amend entry
without this field is structurally incomplete.

> STEP 3d CLOSE: Channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

> PHASE 4 ENTRY CHECK
> - Condition: Step 3d must have activated the channel taxonomy and all three Schema 4
>   invariants must hold (G-1 = PASS, G-2 = PASS, G-3 = PASS).
> - Named artifact: [state the Step 3d close block and the Gate Clearance Summary in Step 3c]
> - Check: YES / NO
>
> If NO: Phase 4 is structurally blocked. Return to Step 3c or Step 3d.
>
> NOTE (C-14): If a remediation loop ran during Step 3c, the gate states referenced here
> must be the POST-REMEDIATION results, not the initial evaluation results. Confirm the
> Gate Clearance Summary in Step 3c shows the final (post-remediation) gate states.

Invariant status at Phase 4 entry: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.

Change entry:
- [finding: F-NN]
- [source: ] (Schema 2 label; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

Dismissal entry:
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

[[ identical to V-01 Verdict section ]]
```

---

## V-03 — Lifecycle Emphasis: Named Structural Blocks

**Axis**: Lifecycle emphasis
**Hypothesis**: Naming the gate-clearance summary and remediation log as first-class structural blocks with mandatory headings and field lists ensures C-11/C-12/C-14 compliance because the blocks exist as required output sections, not narrative choices. A trace that skips a required block has a visibly missing section. A trace that satisfies a required block must produce the required fields.

---

```
You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

[[ identical to V-01 ]]

---

### Stage 1 -- Source-Layer Audit

[[ identical to V-01 ]]

---

### Stage 2 -- Hand-Compilation

[[ identical to V-01, standard role ordering ]]

---

#### Phase 3 -- Findings

This phase is structurally divided into five named blocks. Every block is required output.
A trace missing a block has a visible structural gap. Block 5 (GATE CLEARANCE SUMMARY) is
the single authority for gate states entering Phase 4. A Phase 4 that references gate states
not matching Block 5 is structurally incoherent.

---

##### BLOCK 1 -- Severity Legend (Step 3a)

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.
Schema 5 transition: this block complete -> Block 2 valid.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log |

BLOCK 1 COMPLETE.

---

##### BLOCK 2 -- Findings Table (Step 3b)

Schema 5 prerequisite: Block 1 complete (legend defined).
Schema 5 transition: this block complete with >=2 entries -> Block 3 valid.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Entry count: [N]. Block 2 is complete when N >= 2.

BLOCK 2 COMPLETE -- [N] entries.

---

##### BLOCK 3 -- Gate Evaluation (Step 3c, initial evaluation)

Schema 5 prerequisite: Block 2 complete (>=2 entries).

Record initial gate evaluation. Each gate records PASS or FAIL. If any gate FAILs,
BLOCK 4 (REMEDIATION LOG) is required. If all gates PASS on first evaluation,
BLOCK 4 is exempt and must declare its exemption explicitly.

**G-1** (>=2 distinct Source types):
- Source types in Block 2: [list]
- G-1 initial: PASS / FAIL

**G-2** (no duplicate same-Source Action text):
- Same-Source Action pairs: [list or "none"]
- G-2 initial: PASS / FAIL

**G-3** (all severities from {P1, P2, P3}):
- Severity labels in Block 2: [list]
- G-3 initial: PASS / FAIL

BLOCK 3 COMPLETE -- initial results: G-1 [PASS/FAIL], G-2 [PASS/FAIL], G-3 [PASS/FAIL].
Proceed to BLOCK 4.

---

##### BLOCK 4 -- Remediation Log (Step 3c, remediation)

[ If all Block 3 gates = PASS ]

> BLOCK 4 EXEMPTION (C-12): G-1, G-2, and G-3 all passed on first evaluation.
> No remediation actions were taken. This block is exempt.
> BLOCK 4 COMPLETE (exempt).

[ If any Block 3 gate = FAIL -- one sub-block per failing gate ]

**REMEDIATION RECORD -- [gate ID]**:
- Initial result: FAIL
- Cause: [specific condition that caused the FAIL]
- Action taken: [what was added, changed, or removed in Block 2 to resolve the failure --
  name the specific row or cell modified]
- Re-check: [state the gate condition and the updated Block 2 state]
- Post-remediation result: PASS / FAIL

[ Repeat for each failing gate ]

BLOCK 4 COMPLETE -- post-remediation results: G-1 [PASS/FAIL], G-2 [PASS/FAIL], G-3 [PASS/FAIL].

---

##### BLOCK 5 -- Gate Clearance Summary (Step 3c close / Phase 4 authority)

This block is the SINGLE AUTHORITY for gate states entering Phase 4. Phase 4 must reference
this block, not Block 3 initial results, when remediation occurred.

> **GATE CLEARANCE SUMMARY**
> G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
> All gates: PASS -- Step 3d is valid to begin. Phase 4 is valid to begin when Step 3d completes.
>
> Gate states recorded here are FINAL (post-remediation if Block 4 was active, initial if exempt).
> Phase 4 must agree with this block on all three gate states.

BLOCK 5 COMPLETE.

Schema 5 transition: Block 3+4+5 complete, all gates PASS. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Block 5 shows all gates PASS.
Schema 5 output: channel taxonomy active (unblocks Phase 4).

Channel taxonomy active: spec / invocation / artifact / quality.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS],
[G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

Phase 4 entry: all Schema 4 invariants must hold. Confirm against BLOCK 5 (Gate Clearance
Summary) -- not Block 3 initial results.

> PHASE 4 GATE CONFIRMATION:
> Per Block 5: G-1 [PASS/FAIL], G-2 [PASS/FAIL], G-3 [PASS/FAIL]
> These are the FINAL gate states (post-remediation if applicable).
> Phase 4 is valid to begin: YES / NO

NOTE (C-14 compliance): If Block 4 (Remediation Log) was active, the gate states above
must reflect post-remediation results from Block 4, not Block 3 initial results.

Change entry (six fields required):
- [finding: F-NN]
- [source: ] (label lock: promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

Dismissal entry (four fields required):
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

[[ identical to V-01 Verdict section ]]
```

---

## V-04 — Phrasing Register: Conversational Imperative + Compressed Early Phases

**Axes**: Phrasing register (primary), lifecycle emphasis (secondary)
**Hypothesis**: The existing formal schema language ("A valid X produces... A trace is valid with respect to Schema N if and only if...") creates parsing overhead before Phase 3. Converting to direct second-person imperative and compressing Phase 1/2 to their minimum surface area frees the model's attention for the high-ceremony gate work in Phase 3. A compressed Phase 1/2 may reduce C-07 depth slightly but should raise C-11/C-12/C-13 outcomes.

---

```
You are running /trace-inspect for: `{{skill_name}}`

Skill spec: `{{skill_spec_path}}`
Test invocation: `{{invocation}}`

You are acting as the runtime. This is not a review. You are compiling the skill's execution,
step by step, producing the hand-compiled artifact as if the skill had actually run.

---

## Schema Reference (lock these before you start)

You may only use these labels. Any other label anywhere in your output is a structural error.

- **Severity** (Schema 1): P1 (blocker), P2 (quality fix), P3 (advisory). Nothing else.
- **Source** (Schema 2): SA (spec gap), SG (setup gap -- also used for promoted SA gaps),
  EG (execution gap), QO (quality observation). Nothing else.
- **Channels** (Schema 3): spec / invocation / artifact / quality. Every Phase 4 entry needs one.
- **Gates** (Schema 4): G-1 (>=2 Source types in findings), G-2 (no duplicate same-Source Actions),
  G-3 (all findings use Schema 1 severity). All three must PASS before Phase 4.
- **Phase 3 order** (Schema 5): Step 3a -> 3b -> 3c -> 3d. No skipping, no reversing.

Roles and their schema bindings (one row per role in the spec):

| Role | Severity labels | Source labels | Notes |
|------|----------------|---------------|-------|
| [from spec] | [P1/P2/P3 or N/A] | [SA/SG/EG/QO] | [label lock if promotes] |

---

## Stage 1 -- Read the Spec for Gaps

Read `{{skill_spec_path}}` only (not the invocation yet).

Look across all three layers: spec declarations (SA), setup dependencies (SG), and likely
execution behavior (EG). If you only find SA gaps, you missed something -- look again.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Carry forward: `[SA: ...]`, `[SG: ...]`, `[EG: ...]`, `[layer diversity: PASS/FAIL]`

---

## SA-TO-SG Promotion

Before Phase 1 Setup, evaluate every SA gap. Ask: can a spec-competent invoker supply
this at runtime without changing the spec? If yes, it promotes to SG. If no, it stays SA.

For each SA gap:
```
SA-NN -> PROMOTES TO SG-NN | REMAINS SA
Reason: [one sentence]
```

Post-promotion: `[SA remaining: N]`, `[SG from promotion: N]`

**Label lock**: any SA gap you promoted must use the SG label for the rest of this trace.
If you write its SA label again downstream, that is a structural violation.

---

## Phase 1 -- Setup (Confirm Bindings)

Bind the invocation inputs:

| Input | Value | Gap? |
|-------|-------|------|
| topic | | |
| scope_in | | |
| scope_out | | |
| roles | | |
| stack / detection | | |
| spec_version | | |

For each role, confirm its gaps:

```
[role: name]
  Schema 1 binding: [severity labels or N/A]
  Schema 2 binding: [source labels; label lock if promoted]
  SA/SG gaps: [list or none -- confirmed]
  EG risks: [list or none -- confirmed]
```

Carry forward: topic, scope, roles, SA remaining, SG total.

---

## Phase 2 -- Execute (Write the Artifact)

Run each role in the order declared in the spec. For each role:

**[Role name] relay:**
| Field | Value |
|-------|-------|
| Received from | |
| Received values | |
| Schema 2 compliance (Source labels used -- all from {SA,SG,EG,QO}?) | YES / NO |
| SA/SG gaps affecting this role | |
| Produced | |
| EG gaps encountered | |

Write the artifact to `simulations/trace/skill/{topic}-skill-trace-{date}.md`.
Include every section the skill's artifact contract requires. Do not skip sections.

Carry forward: artifact path, EG count added.

---

## Phase 3 -- Findings

Work through these four steps in order. Do not start a step before its predecessor
has produced its required output.

---

### Step 3a -- Define Severity for This Trace

Before you build the findings table, lock down what P1/P2/P3 mean for this specific skill
and invocation. These definitions govern every finding you record.

| Label | What makes something this level in this trace | Gate? |
|-------|----------------------------------------------|-------|
| P1 | [trace-specific blocker definition] | Yes -- resolve before moving to Phase 4 |
| P2 | [trace-specific quality definition] | Address in Amend |
| P3 | [trace-specific advisory definition] | Log only |

Step 3a done. You can now build the findings table.

---

### Step 3b -- Build the Findings Table

Use the severity legend from Step 3a. Use only Schema 2 Source labels (promoted gaps use SG).
You need at least 2 findings covering at least 2 distinct Source types before you can run gates.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Count your Source types. If you have only one -- SA-only or EG-only -- you are missing a layer.
Add findings until you have coverage across at least 2 Source types.

Step 3b done (N=[count] findings, Source types=[list]). You can now run the gates.

---

### Step 3c -- Run the Gates

Check all three gates. Record each explicitly. If a gate fails, fix it and re-check -- do not
skip past a FAIL.

**G-1 check** (need >=2 Source types in the table above):
- Source types present: [list]
- G-1: PASS / FAIL
- [If FAIL: what you added to fix it, then re-check result]

**G-2 check** (no two same-Source findings with identical Action text):
- Same-Source pairs: [list or "none"]
- G-2: PASS / FAIL
- [If FAIL: what you changed, then re-check result]

**G-3 check** (every finding uses P1/P2/P3 from your Step 3a legend):
- Severity labels in table: [list]
- G-3: PASS / FAIL
- [If FAIL: what you relabeled, then re-check result]

**[If all three gates passed on first check -- no FAIL ever occurred:]**
> C-12 EXEMPTION: G-1, G-2, and G-3 all passed on first evaluation. No remediation loop ran.

**Gate clearance (state this before moving to Step 3d):**
> G-1 [PASS/FAIL], G-2 [PASS/FAIL], G-3 [PASS/FAIL] -- Phase 4 is valid to begin.

---

### Step 3d -- Activate Channels

All gates passed. Activate the remediation channel taxonomy for Phase 4.

Channels available: spec / invocation / artifact / quality.
Every Amend entry you write must name one of these channels.

Step 3d done. Phase 4 is valid to begin.

---

## Phase 4 -- Amend

Before writing any entry, confirm: the gate states in Step 3c's Gate Clearance block show
all PASS. If remediation ran in Step 3c, those are the POST-remediation results -- use those.

> Phase 4 entry gate states (from Step 3c Gate Clearance):
> G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
> All PASS: YES / NO

For each finding in Step 3b, write a change or dismissal:

Change:
- finding: [F-NN]
- source: [Schema 2 label; SG if promoted]
- remediation channel: [spec / invocation / artifact / quality]
- what changed: [section and field]
- how: [the change]
- source confirmed: YES / NO

Dismissal:
- finding: [F-NN]
- reason: [why not actionable here]
- remediation channel: [spec / invocation / artifact / quality]
- source confirmed: YES / NO

---

## Verdict

**Compliance ledger** -- fill every row, name specific values (no "as expected"):

| VC | Schema | Site | Expected | Observed | Result |
|----|--------|------|---------|---------|--------|
| VC-1 | Severity | Step 3a | Legend defined P1/P2/P3 | [actual definitions] | P/F |
| VC-1 | Severity | Step 3b | Only {P1,P2,P3} | [values and counts] | P/F |
| VC-1 | Severity | Step 3c G-3 | G-3 verified | [labels checked, result] | P/F |
| VC-1 | Severity | Phase 4 | Only {P1,P2,P3} | [values in Amend entries] | P/F |
| VC-1 | Severity | [EG role relays] | EG findings use Schema 1 | [labels per role] | P/F |
| VC-2 | Source | Stage 1 | SA/SG/EG/QO labels | [labels used] | P/F |
| VC-2 | Source | SA-TO-SG | Promoted -> SG label | [promoted gaps and labels] | P/F |
| VC-2 | Source | Step 3b | {SA,SG,EG,QO}; promoted=SG | [Source column values] | P/F |
| VC-2 | Source | [all role relays] | Schema 2 labels; label lock | [labels per role] | P/F |
| VC-3 | Channel | Step 3d | Taxonomy activated | [activation language at 3d] | P/F |
| VC-3 | Channel | Phase 4 | Every entry has channel | [channels per entry] | P/F |
| VC-4 | Gates | Step 3c | G-1/G-2/G-3 explicit | [all three results] | P/F |
| VC-4 | Gates | Phase 4 pre-check | All PASS at entry | [entry status] | P/F |
| VC-4 | Gates | Step 3b G-1 cross | >=2 Source types | [types and contributing roles] | P/F |
| VC-5 | Ordering | 3a->3b | 3b after 3a legend | [what confirmed 3a done] | P/F |
| VC-5 | Ordering | 3b->3c | 3c after 3b >=2 | [count at 3c start] | P/F |
| VC-5 | Ordering | 3c->3d | 3d after all-PASS | [gate results before 3d] | P/F |
| VC-5 | Ordering | 3d->Phase 4 | Phase 4 after channel active | [activation confirmation] | P/F |

SA remaining: [N] | SG total: [N] | EG total: [N]

**Trace result**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

- NEEDS-SPEC-REVISION: any P1 SA gap is still labeled SA after promotion.
- NEEDS-REDESIGN: EG gaps exceed 3 and indicate a structural role gap.
- USEFUL: otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## V-05 — Combined: Inertia Framing + Execution-First + Named Gate Clearance + C-12 Exemption

**Axes**: Inertia framing + role sequence + lifecycle emphasis
**Hypothesis**: Opening with explicit status-quo cost (what breaks if you skip this trace) establishes rigor stakes before the compilation begins. Execution-first role ordering (from V-01) surfaces EG gaps before SA-TO-SG decisions. A named GATE CLEARANCE SUMMARY block (from V-03) and a mandatory C-12 EXEMPTION notice together close the two most common aspirational failures: C-11 (summary missing) and C-12 (exemption via silence). C-14 is addressed explicitly at Phase 4 entry.

---

```
You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

## Why This Trace Exists

Without this trace, the following costs are hidden until implementation:

- **Spec-layer gaps (SA)** that could have been caught by reading the spec once are discovered
  during code review, after design assumptions have hardened.
- **Setup gaps (SG)** that a competent invoker could supply are never distinguished from gaps
  requiring spec changes -- so the wrong person gets blocked.
- **Execution gaps (EG)** that indicate structural role problems surface as integration bugs
  rather than design decisions.
- **The artifact that would have been produced** is never written down, so the first real
  output becomes the de facto spec rather than a considered baseline.

This trace costs one session. Skipping it costs a redesign cycle. Hand-compile before you build.

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (promoted gaps use SG label) | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Aggregate across all roles' findings | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source coverage across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: Valid labels: P1 (blocker), P2 (quality improvement),
P3 (advisory). Any other label is structurally invalid anywhere in this trace.

**Schema 2 -- Gap Type Taxonomy**: Valid Source labels: SA (spec-layer gap), SG (setup gap
or promoted SA gap), EG (execution gap), QO (quality observation). Label lock: a gap promoted
at SA-TO-SG PROMOTION uses SG in all downstream phases. SA retained after promotion is a violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry must include
`[remediation channel: spec / invocation / artifact / quality]`. Missing = structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**:
- G-1: Step 3b contains >=2 distinct Source types. Fewer = structural defect.
- G-2: No two same-Source findings share identical Action text. Duplicates = structural defect.
- G-3: All Step 3b entries use only {P1, P2, P3}. Any other label = structural defect.
All three must PASS. A structural defect must be corrected and re-checked; it cannot be bypassed.

**Schema 5 -- Sub-Step Ordering**: Sub-steps run in declared order. Each step is only valid when
its predecessor has produced the required output.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2) | Step 3c |
| Step 3c | Step 3b populated | All-PASS gate results | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Execution pass |
|------|-----------------|-----------------|----------------|
| [role] | [severity or N/A] | [source labels; lock if promoted] | [EXECUTION / SPEC / ORCHESTRATION] |

Assign each role to an execution pass before Stage 2 begins:
- **EXECUTION PASS**: roles whose primary output surfaces EG gaps (runtime actors, implementation components). Run first.
- **SPEC PASS**: roles whose primary output surfaces SA gaps (authors, designers). Run after SA-TO-SG PROMOTION.
- **ORCHESTRATION PASS**: roles that coordinate or synthesize. Run last.

---

### Stage 1 -- Source-Layer Audit

Read only `{{skill_spec_path}}`. Examine all three source layers.

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

#### SA-TO-SG PROMOTION (runs after EXECUTION PASS completes, before SPEC PASS)

[[ V-05 placement: promotion event runs after all EG-producing roles have relayed, so each
promotion decision is informed by what was observed during execution, not inferred from spec
alone. This is the same execution-first rationale as V-01. ]]

For each SA gap:
```
SA-NN:
  Gap: [what spec does not declare]
  Execution evidence: [what the execution-pass roles revealed about this gap]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence grounded in execution evidence]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
```

---

#### Phase 1 -- Setup

Confirmed input bindings:

| Input | Value |
|-------|-------|
| topic | |
| scope_in | |
| scope_out | |
| roles | |
| stack / detection | |
| spec_version | |

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or N/A]
  Schema 2 binding: [Source labels; label lock if promoted]
  Execution pass: [EXECUTION / SPEC / ORCHESTRATION]
  SA/SG gaps binding this role: [list or none -- confirmed]
  EG gaps expected: [list or none -- confirmed]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 -- Execute

Run roles in execution-pass order: EXECUTION PASS -> SA-TO-SG PROMOTION -> SPEC PASS ->
ORCHESTRATION PASS.

**EXECUTION PASS roles:**

**Role relay -- [role name] (EXECUTION PASS)**:
- Received from: [prior or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or none]
- Produced: [artifact content added]
- EG gaps encountered: [list or none]

[When all execution-pass roles complete, run SA-TO-SG PROMOTION above]

**SPEC PASS roles** (use post-promotion labels):

**Role relay -- [role name] (SPEC PASS)**:
- Received from: [prior or PROMOTION event]
- Received values: [name: value] -- note: promoted gaps now labeled SG
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps (post-promotion labels): [list or none]
- Produced: [artifact content added]
- EG gaps encountered: [list or none]

**ORCHESTRATION PASS roles:**

**Role relay -- [role name] (ORCHESTRATION PASS)**:
- Received from: [prior role]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps: [list or none]
- Produced: [artifact content added]
- EG gaps encountered: [list or none]

Write the hand-compiled artifact to:
`simulations/trace/skill/{topic}-skill-trace-{date}.md`

**Execute carry-forward**: [artifact path], [EG added].

---

#### Phase 3 -- Findings

Sub-steps run in Schema 5 order. Each sub-step states its prerequisite and transition.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.
Schema 5 transition: legend produced -> Step 3b valid.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker in this trace] | Resolve before Phase 4 |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log |

Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.
Schema 5 transition: >=2 entries produced -> Step 3c valid.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Entry count: [N]. Step 3c is valid when N >= 2. Step 3b complete.

---

##### Step 3c -- Gate Evaluation and Remediation

Schema 5 prerequisite: Step 3b complete (>=2 entries).
Schema 5 transition: GATE CLEARANCE SUMMARY shows all-PASS -> Step 3d valid.

**Initial gate evaluation:**

G-1 (>=2 distinct Source types in Step 3b):
- Source types present: [list]
- G-1 initial: PASS / FAIL

G-2 (no duplicate same-Source Action text):
- Same-Source pairs: [list or "none"]
- G-2 initial: PASS / FAIL

G-3 (all severities from {P1, P2, P3}):
- Severity labels in Step 3b: [list]
- G-3 initial: PASS / FAIL

**Remediation (required if any initial gate = FAIL):**

[ FAIL gate -- one block per failing gate ]
> REMEDIATION -- [gate ID]:
> - Initial result: FAIL
> - Cause: [specific condition]
> - Action taken: [what changed in Step 3b -- name the row or cell]
> - Re-check: [gate condition] -> [updated state]
> - Post-remediation: PASS / FAIL

[ If no gate failed on initial evaluation ]
> C-12 EXEMPTION: G-1, G-2, and G-3 all passed on initial evaluation.
> No remediation actions were taken or needed. Exemption applies.

---

**GATE CLEARANCE SUMMARY** (required block -- authority for Phase 4 entry):

> G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
>
> These are FINAL gate states: post-remediation if any gate required remediation,
> initial if C-12 EXEMPTION applies.
>
> All gates PASS: YES / NO
> Step 3d is valid to begin: YES / NO
> Phase 4 is valid to begin (once Step 3d completes): YES / NO

Step 3c complete.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: GATE CLEARANCE SUMMARY shows all-PASS.
Schema 5 transition: channel taxonomy active -> Phase 4 valid.

Channels active: spec / invocation / artifact / quality.
Every Phase 4 Amend entry requires `[remediation channel: ...]`.

Step 3d complete. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest_finding], [G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CONFIRMATION** (C-14 compliance):
> Per GATE CLEARANCE SUMMARY in Step 3c:
> G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
>
> These are the FINAL gate states from the Gate Clearance Summary.
> If remediation ran in Step 3c, these reflect post-remediation results -- not initial results.
> If C-12 EXEMPTION applies, these are the initial (= final) results.
> Phase 4 is valid: YES / NO

If any gate = FAIL: Phase 4 is structurally blocked. Return to Step 3c.

Change entry (six fields):
- [finding: F-NN]
- [source: ] (Schema 2; promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

Dismissal entry (four fields):
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Compliance Ledger)

Fill every row. "Observed behavior: as expected" is structurally invalid -- name specific values.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | Schema 1 | Step 3a | Legend P1/P2/P3 | [actual definitions] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b | Only {P1,P2,P3} | [values and counts] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [labels and result] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Only {P1,P2,P3} | [values in Amend] | PASS/FAIL |
| VC-1 | Schema 1 | EG role relays | EG findings Schema 1 | [labels per role] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [labels used] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG | Promoted -> SG | [promoted gaps and labels] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source | {SA,SG,EG,QO}; SG for promoted | [Source column values] | PASS/FAIL |
| VC-2 | Schema 2 | Role relays (all) | Schema 2; label lock | [labels per role] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Taxonomy activated | [activation language] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel | [channels per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | All PASS at entry | [entry confirmation] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 cross-role | >=2 Source types | [types and roles] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion evidence] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after >=2 | [count at 3c] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after all-PASS | [gate results before 3d] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after active | [activation before Phase 4] | PASS/FAIL |

**SA remaining**: [N] | **SG total**: [N] | **EG total**: [N]

**Trace result**: USEFUL / NEEDS-REDESIGN / NEEDS-SPEC-REVISION

- NEEDS-SPEC-REVISION: any P1 SA gap remains SA after promotion.
- NEEDS-REDESIGN: EG gaps exceed 3 and indicate a structural role gap.
- USEFUL: otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
```

---

## Round 5 Design Notes

| Criterion targeted | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------------|------|------|------|------|------|
| C-06 (SA-TO-SG grounded in evidence) | Primary gain: execution evidence informs promotion | -- | -- | -- | Primary gain |
| C-11 (consolidated gate-clearance summary) | Summary present inline | Summary block present | BLOCK 5 named block | Summary present | Named GATE CLEARANCE SUMMARY block |
| C-12 (remediation loop + exemption) | Basic FAIL path | Explicit REMEDIATION LOG + EXEMPTION block | BLOCK 4 named block + EXEMPTION | EXEMPTION notice | REMEDIATION block + C-12 EXEMPTION |
| C-13 (named-artifact prerequisite checks) | Schema 5 prose | Checkbox blocks with named artifact | BLOCK open/close | Brief prerequisite | Prerequisite stated at each step |
| C-14 (remediation-to-summary coherence) | Not addressed | Explicit Phase 4 entry C-14 note | BLOCK 5 is final authority | Phase 4 entry note | PHASE 4 GATE CONFIRMATION block with explicit C-14 note |

**Key design choices:**

- **V-02** is the purest C-13 probe: the checkbox format is the minimal change needed to force named-artifact verification. If this variation scores higher on C-13 but lower on C-07 (relay depth), it tells us the checkbox format taxes the model's available output budget.
- **V-03** is the purest C-11/C-12 probe: BLOCK 4 and BLOCK 5 are first-class sections, not inline instructions. If these blocks appear in the output, C-11 and C-12 are satisfied mechanically. If they don't appear, the scoring gap is visible.
- **V-05** combines V-01 (execution-first), V-03 (named blocks), plus the inertia preamble and explicit C-14 note at Phase 4 entry. It is the maximum coverage combination. Its risk is that accumulated structure length compresses relay depth per role (C-07 pressure).
