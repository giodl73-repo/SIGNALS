---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 9
rubric: trace-inspect-rubric-v5
---

# trace-inspect -- Variations v5 R9 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R8 champion is V-05 at ~98/99.5. All 5 essential PASS. All 3 recommended PASS.
Three aspirational criteria remain as systematic gaps across all R8 variations:

- **C-19 (EG-first structural role ordering)**: NO R8 variation makes EG-first execution
  structurally enforced. The R6 architecture carries an "Execution-first ordering note" in the
  Phase 2 header but this is commentary, not constraint. A model executing Phase 2 can run
  SA-only roles before EG-producing roles and no structural element fires. C-19 requires the
  execution model to constrain sequence so EG relay completion is a named prerequisite for
  SA-TO-SG PROMOTION -- violation must be architecturally impossible, not just instructionally
  discouraged.

- **C-20 (Inertia registry with explicit inheritance declaration)**: NO R8 variation includes a
  block that names all prior-version criteria by ID and declares each as inherited. Silence about
  prior criteria implies continuity, but silence is not a structural guarantee. A future version
  could silently drop C-07 or C-12 and no element in the prompt would surface the omission.
  C-20 requires an explicit registry that enumerates every inherited criterion by ID so that any
  version that drops a criterion must actively remove it from the registry -- an auditable act
  rather than a silent omission.

- **C-21 (Attribution table co-located in compliance ledger)**: NO R8 variation embeds the
  source attribution table directly in the VC-4 G-1 row. C-17 (present in all R8 variants) adds
  a standalone attribution table; C-21 requires that table to be a pre-printed sub-structure of
  the VC-4 G-1 row so that filling the ledger and completing attribution are a single operation.
  When the attribution table is a separate element, the two can drift: a model can fill the
  ledger row generically and fill the attribution table separately. Co-location makes this
  impossible.

**R9 variation axes** (these three gaps drive all five axes):

- **Role sequence (C-19 structural enforcement)**: Add an EG-FIRST EXECUTION CONSTRAINT block
  after the Role-Schema Binding Summary. Restructure Stage 2 so EG-producing roles relay in a
  dedicated sub-phase before SA-TO-SG PROMOTION begins. SA-TO-SG PROMOTION becomes structurally
  gated on an EG-RELAY COMPLETE checkpoint -- a named lifecycle event that fires only when all
  EG-producing roles have completed. Hypothesis: moving SA-TO-SG PROMOTION downstream of EG
  relay completion makes execution evidence always available when promotion decisions are made,
  not just recommended. Violation becomes structurally impossible because the gate does not open
  until EG relays are done (V-01).

- **Inertia framing (C-20 inheritance registry)**: Add a CRITERION INHERITANCE REGISTRY block
  at the top of the prompt, before the Coverage Matrix. The block names all prior-version
  criteria (C-01 through C-18) as INHERITED and labels C-19/C-20/C-21 as NEW. Also adds an
  INERTIA COMPETITOR block describing what a developer does without this skill (ad-hoc spec
  reading, no lifecycle structure, no enforcement gates). Hypothesis: an explicit registry
  prevents silent criterion drop; a future version must actively remove a criterion from the
  registry to drop it -- the omission becomes auditable (V-02).

- **Output format (C-21 attribution co-location)**: Restructure the VC-4 G-1 cross-role row
  in the compliance ledger to embed a pre-printed G-1 SOURCE ATTRIBUTION sub-table directly
  inside the row. The sub-table has three columns: Source type / Role(s) that contributed /
  Finding IDs. Filling the G-1 row and completing the attribution table become a single write
  operation -- the two cannot drift because they share the same cell. Hypothesis: co-location
  removes the structural gap between C-09 (compliance ledger) and C-17 (attribution table)
  that exists when these are independent elements (V-03).

**Combined variations**:
- V-04: C-19 structural ordering + C-20 inheritance registry (two highest-impact remaining axes)
- V-05: C-19 + C-20 + C-21 + full integration targeting 99.5/99.5 convergence

All five inherit the R6 V-01/R8 V-05 architecture: named GATE CLEARANCE SUMMARY structural
block, FLOOR CHECK block in Step 3b, C-12 EXEMPTION notice, PHASE 4 GATE CLEARANCE SUMMARY
block, Coverage Matrix with VC compliance columns, Schema 5 sub-step transition table.

---

## V-01 -- Single axis: Role sequence (C-19: EG-first structural ordering)

**Axis**: Role sequence -- EG-producing roles complete in a dedicated sub-phase before
SA-TO-SG PROMOTION lifecycle event begins. Structural constraint, not ordering guidance.

**Hypothesis**: The R6-R8 architecture places SA-TO-SG PROMOTION at the opening of Stage 2,
before Phase 2 Execute begins. An "Execution-first ordering note" in the Phase 2 header tells
the executor that EG roles should run before SA roles, but this note fires after promotion has
already been evaluated. The note is advice; the promotion event already happened. V-01
restructures Stage 2 so EG-producing roles relay in Phase 2a before SA-TO-SG PROMOTION is
declared eligible. An EG-RELAY COMPLETE checkpoint gates the promotion event. A model that
attempts SA-TO-SG PROMOTION before the EG-RELAY COMPLETE checkpoint passes is structurally
blocked. Risk: executor skips the EG-RELAY COMPLETE checkpoint and proceeds to promotion
anyway. Mitigation: the Phase 2a sub-phase header declares "SA-TO-SG PROMOTION is structurally
blocked until this checkpoint passes" -- the block is named, not implied.

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
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: {P1, P2, P3} only. P1 blocks usefulness. P2 is a quality
improvement. P3 is advisory. Every EG finding from every role uses only {P1, P2, P3}. No other
severity value appears anywhere in the trace.

**Schema 2 -- Gap Type Taxonomy**: {SA, SG, EG, QO} only. SA = spec-layer gap. SG = setup gap.
EG = execute gap. QO = quality observation. Label lock invariant: a promoted SA gap uses SG in
all phases after SA-TO-SG PROMOTION. A promoted gap retaining SA is a structural violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes `[remediation
channel: spec / invocation / artifact / quality]`. An entry without a channel field is
structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**: G-1: Step 3b contains >=2 distinct Source types.
G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only
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

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Before Stage 2 begins, declare which roles are EG-producing and which are SA/SG-only:

```
EG-producing roles (must complete Phase 2a before SA-TO-SG PROMOTION):
  [list all roles marked EG-producing YES in Role-Schema Binding Summary]

SA/SG-only roles (run in Phase 2b, after SA-TO-SG PROMOTION):
  [list all roles marked EG-producing NO]

Structural invariant: SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE
checkpoint passes. A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE is
structurally invalid at that point.
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
  Schema 2 binding: [Source labels this role may produce; label lock rules if promoted gaps present]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (EG-producing roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only EG-producing roles from the EG-FIRST EXECUTION CONSTRAINT
block run here. SA/SG-only roles are deferred to Phase 2b. SA-TO-SG PROMOTION is structurally
BLOCKED until the EG-RELAY COMPLETE checkpoint below passes.

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
  Reason: [one sentence -- cite Phase 2a execution evidence if available, spec inference otherwise]
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
> If FAIL: add findings before advancing. A missing source layer requires at least one finding
> from that layer. Duplicate Actions require distinct remediation targets. Re-run FLOOR CHECK
> after correction. A bare count without named Finding IDs is not a valid FLOOR CHECK.

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
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) | G-1 verified across all Phase 2a + 2b roles | [list Source types present and which roles contributed each] | PASS/FAIL |
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

## V-02 -- Single axis: Inertia framing (C-20: Criterion inheritance registry)

**Axis**: Inertia framing -- explicit CRITERION INHERITANCE REGISTRY block at prompt top;
INERTIA COMPETITOR section describing what happens without this skill.

**Hypothesis**: No R8 variation includes a block that names prior-version criteria and
declares each as inherited. Without such a block, a future version could silently drop any
criterion (C-07, C-12, C-16...) and no structural element in the prompt would surface the
omission. V-02 adds a CRITERION INHERITANCE REGISTRY that enumerates every inherited criterion
by ID. A version that drops a criterion must remove it from the registry -- the omission
becomes an auditable deletion rather than a silent gap. The INERTIA COMPETITOR block serves
C-09 evidence (grounding the skill in what a developer does manually) while also reinforcing
why the lifecycle structure exists. Risk: the registry becomes boilerplate that executors
ignore. Mitigation: the registry block is placed before the Coverage Matrix so it is the first
thing a model reads; the INERTIA COMPETITOR establishes the problem frame before the solution.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v5

This skill body is version 5. The following criteria were established in prior versions and
are explicitly inherited here. A version that does not name a criterion in this registry has
dropped it. Dropping a criterion is a structural act, not a silent omission.

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
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

NEW IN v5 -- ASPIRATIONAL CRITERIA:
  C-19 (EG-first structural role ordering): NEW
  C-20 (Inertia registry with inheritance declaration): NEW -- this registry
  C-21 (Attribution table co-located in compliance ledger): NEW
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: {P1, P2, P3} only. P1 blocks usefulness. P2 is a quality
improvement. P3 is advisory.

**Schema 2 -- Gap Type Taxonomy**: {SA, SG, EG, QO} only. Label lock invariant: a promoted SA
gap uses SG in all phases after SA-TO-SG PROMOTION. A promoted gap retaining SA is a structural
violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes `[remediation
channel: spec / invocation / artifact / quality]`.

**Schema 4 -- Enforcement Gate Registry**: G-1: >=2 distinct Source types in Step 3b. G-2: no
two same-Source findings share identical Action text. G-3: all Step 3b entries use only
{P1, P2, P3}. Defects must be corrected and re-checked; they cannot be bypassed.

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

Inertia note: without a structured Stage 1, a developer reads the spec once and guesses which
gaps matter. Stage 1 forces a systematic read of all three source layers before any execution.

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

#### SA-TO-SG PROMOTION (named lifecycle event)

Every SA gap from Stage 1 is evaluated. A gap a spec-competent invoker can supply at runtime
promotes to SG. A gap requiring a spec change remains SA.

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
- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

A valid Execute produces the hand-compiled artifact and a per-role relay for each role. A relay
missing the "Schema 2 compliance" field is structurally invalid.

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Artifact write** (after all role relays):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Phase 3 is valid if and only if its sub-steps run in the order declared by Schema 5.

---

##### Step 3a -- Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b valid.

---

##### Step 3b -- Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required structural output):
>
> - Finding IDs counted: [list all IDs]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2)
> - Action-uniqueness check: YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings. Re-run FLOOR CHECK. A bare count without named Finding IDs fails.

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: FLOOR CHECK PASS.

**G-1**: Source types present: [list] -- G-1: PASS / FAIL
**G-2**: Same-Source pairs: [list or "none"] -- G-2: PASS / FAIL
**G-3**: Severity labels present: [list] -- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY**:
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> ALL GATES CLEARED -- Step 3d valid. / GATE FAILURE -- Step 3d BLOCKED.

> **REMEDIATION LOG** / "C-12 EXEMPTION APPLIES: all gates passed on first evaluation."

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: GATE CLEARANCE SUMMARY ALL GATES CLEARED.

Channel taxonomy active: every Phase 4 Amend entry must carry `[remediation channel: ...]`.

Schema 5 transition: channel taxonomy active. Phase 4 valid.

---

**Findings carry-forward**: [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY**:
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> ALL GATES CLEARED -- Phase 4 valid.

Amend entry (change): [finding] / [source] / [remediation channel] / [section changed] /
[change] / [source confirmed YES/NO]

Amend entry (dismissal): [finding] / [reason] / [remediation channel] / [source confirmed YES/NO]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels | [list all Source labels] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps SG; lock holds | [list SA promoted; SG confirmed downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted SG | [list Source labels; label lock status] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) | G-1 verified across all roles | [Source types and contributing roles] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a complete before 3b | [what confirmed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | FLOOR CHECK PASS before 3c | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | ALL GATES CLEARED before 3d | [gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Channel taxonomy active before Phase 4 | [activation + PHASE 4 GATE CLEARANCE] | PASS/FAIL |

**VC-1 overall**: PASS/FAIL | **VC-2 overall**: PASS/FAIL | **VC-3 overall**: PASS/FAIL
**VC-4 overall**: PASS/FAIL | **VC-5 overall**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Output format (C-21: Attribution table co-located in VC-4 G-1 row)

**Axis**: Output format -- the G-1 SOURCE ATTRIBUTION sub-table is embedded as a pre-printed
structure directly inside the VC-4 G-1 cross-role compliance ledger row.

**Hypothesis**: C-17 (source attribution table) is present in all R8 variants as a standalone
block somewhere in the verdict section. C-21 requires the attribution table to be co-located
with the VC-4 G-1 row specifically. When the attribution table is independent, a model fills
the ledger row with generic text ("G-1 holds across all roles") and fills the attribution table
as a separate pass. The two can say different things. V-03 embeds the attribution sub-table
directly into the VC-4 G-1 cross-role row definition. The "Observed behavior" cell of that row
cannot be filled without filling the attribution table -- they are the same cell. Risk: the
embedded sub-table makes the VC-4 row visually complex and executors skip its inner structure.
Mitigation: the inner table has exactly three columns and the outer row's "Observed behavior"
cell explicitly says "fill the sub-table below; this cell is not complete until the sub-table
is filled."

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles; G-1 attribution sub-table in VC-4 G-1 row | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1**: {P1, P2, P3} only. **Schema 2**: {SA, SG, EG, QO} only; label lock invariant.
**Schema 3**: Every Phase 4 entry includes `[remediation channel: ...]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (no same-Source duplicate Actions), G-3 (only {P1,P2,P3}).
**Schema 5**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [Schema 3/4 interactions] |

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]  [layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### SA-TO-SG PROMOTION (named lifecycle event)

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

```
[SA remaining: {{sa_remaining}}]  [SG from promotion: {{sg_promoted}}]  [SG original: {{sg_original}}]
```

---

#### Phase 1 -- Setup

- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [roles: `{{roles}}`], [SA: `{{sa}}`], [SG: `{{sg}}`].

---

#### Phase 2 -- Execute

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md` -- Sections: [list WRITTEN]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

##### Step 3a -- Severity Legend

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid.

---

##### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK**:
> - Finding IDs: [list all]  Row count: N (>= 3 required)
> - Source types: [list] (>= 2 required)  Action-uniqueness: YES FAIL / NO PASS
> **FLOOR CHECK: PASS / FAIL** -- trace blocked at Step 3b until PASS.

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

---

##### Step 3c -- Enforcement Gates

G-1: Source types: [list] -- PASS/FAIL
G-2: Same-Source pairs: [list or none] -- PASS/FAIL
G-3: Severity labels: [list] -- PASS/FAIL

> **GATE CLEARANCE SUMMARY**: G-1: [P/F] | G-2: [P/F] | G-3: [P/F]
> ALL GATES CLEARED / GATE FAILURE

> **REMEDIATION LOG** / "C-12 EXEMPTION APPLIES: all gates passed on first evaluation."

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active: Phase 4 entries require `[remediation channel: ...]`.

Schema 5 transition: active. Phase 4 valid.

---

**Findings carry-forward**: [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY**: G-1: PASS | G-2: PASS | G-3: PASS -- ALL GATES CLEARED.

Amend (change): [finding] / [source] / [remediation channel] / [section] / [change] / [confirmed]
Amend (dismissal): [finding] / [reason] / [remediation channel] / [confirmed]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend declared | [name the legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All P1/P2/P3; FLOOR CHECK PASS | [labels; FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Only P1/P2/P3 | [severity values in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [all Source labels used] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted SG; lock holds | [SA promoted; SG confirmed downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted SG | [Source labels; label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel | [channels per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | PHASE 4 GATE CLEARANCE PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | **Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION** | G-1 holds across all roles AND attribution table filled as part of this row | **Observed behavior (this cell is not complete until the sub-table below is filled):**<br>G-1 holds: [PASS/FAIL]<br>**G-1 SOURCE ATTRIBUTION TABLE:**<br>&#124; Source type &#124; Role(s) that contributed &#124; Finding IDs &#124;<br>&#124; SA &#124; [role name(s)] &#124; [F-IDs] &#124;<br>&#124; EG &#124; [role name(s)] &#124; [F-IDs] &#124;<br>&#124; [type] &#124; [role name(s)] &#124; [F-IDs] &#124;<br>All Source types in Step 3b attributable to a role: YES/NO | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a complete before 3b | [what confirmed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | FLOOR CHECK PASS before 3c | [FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | ALL GATES CLEARED before 3d | [gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Channel taxonomy active before Phase 4 | [activation + PHASE 4 GATE CLEARANCE] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: C-19 + C-20 (EG-first structural ordering + inheritance registry)

**Axis**: V-01 EG-first structural constraint + V-02 criterion inheritance registry. These two
axes are combined because they address the two highest-value remaining aspirational criteria
(0.5 pts each) and are structurally independent -- EG-first ordering governs Phase 2 execution
sequence; the inheritance registry governs prompt-level version continuity. Combining them does
not create interaction risk.

**Hypothesis**: V-01 proves that EG-first ordering can be made structural rather than advisory.
V-02 proves that inheritance declaration can surface criterion continuity. V-04 tests whether
both mechanisms coexist without interference. The C-19 mechanism (EG-RELAY COMPLETE gate before
SA-TO-SG PROMOTION) is independent of the C-20 mechanism (CRITERION INHERITANCE REGISTRY at
the top of the prompt). No interaction risk identified; C-21 remains deferred to V-05.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v5

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec informally, no structured source-layer separation
  2. Guesses which gaps are spec-layer vs execution-layer
  3. No enforcement gates; trace advances even with under-populated findings
  4. No promotion lifecycle; SA and SG gaps blur together
  5. No compliance ledger; verdict is subjective
  Result: unauditable traces where verdict quality depends on executor experience.

INHERITED FROM v1 -- ESSENTIAL:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL:
  C-11 (Phase-entry gate clearance summary): INHERITED
  C-12 (Gate-failure remediation loop): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL:
  C-14 (Pre-scoring mechanism placement): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED
  C-18 (Verdict classification rule citation): INHERITED

NEW IN v5:
  C-19 (EG-first structural role ordering): NEW -- enforced via EG-FIRST EXECUTION CONSTRAINT
  C-20 (Inertia registry with inheritance declaration): NEW -- this registry
  C-21 (Attribution table co-located in compliance ledger): NEW -- deferred to V-05
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all Phase 2a + 2b roles | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1**: {P1, P2, P3} only. **Schema 2**: {SA, SG, EG, QO} only; label lock invariant.
**Schema 3**: Every Phase 4 entry includes `[remediation channel: ...]`.
**Schema 4**: G-1 (>=2 Source types), G-2 (no same-Source duplicate Actions), G-3 (only {P1,P2,P3}).
**Schema 5**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results (all PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock] | YES / NO | [interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

```
EG-producing roles (must complete Phase 2a before SA-TO-SG PROMOTION):
  [list all roles marked EG-producing YES above]

SA/SG-only roles (Phase 2b, after SA-TO-SG PROMOTION):
  [list all roles marked EG-producing NO above]

Structural invariant: SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE
checkpoint passes. Attempting promotion before EG-RELAY COMPLETE is a structural violation.
```

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]  [layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

- [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [roles], [SA: `{{sa}}`], [SG original: `{{sg_original}}`].

---

#### Phase 2a -- EG-First Execution (EG-producing roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only EG-producing roles run here. SA-TO-SG PROMOTION is
BLOCKED until EG-RELAY COMPLETE checkpoint below shows PASS.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (SA-TO-SG PROMOTION is BLOCKED until PASS):
>
> - EG-producing roles declared: [list from EG-FIRST EXECUTION CONSTRAINT]
> - EG-producing roles relayed: [list completed above]
> - All EG roles relayed: YES / NO
>
> **EG-RELAY COMPLETE: PASS** / **FAIL** (missing relays: [list])

---

#### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

**Prerequisite**: EG-RELAY COMPLETE PASS (confirmed above). Cite execution evidence from
Phase 2a where available.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a EG evidence if available, spec inference if not]
```

```
[SA remaining: {{sa_remaining}}]  [SG from promotion: {{sg_promoted}}]  [SG original: {{sg_original}}]
```

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: none -- this role does not produce EG findings

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md` -- Sections: [list WRITTEN]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

##### Step 3a -- Severity Legend

| Label | Definition for this trace | Actionability |
|-------|--------------------------|--------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality] | Address in Amend |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid.

---

##### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK**:
> Finding IDs: [list all] | Row count: N (>= 3) | Source types: [list] (>= 2) | Duplicates: NO
> **FLOOR CHECK: PASS / FAIL** -- blocked at Step 3b until PASS. IDs must be named explicitly.

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

---

##### Step 3c -- Enforcement Gates

G-1: [Source types] -- PASS/FAIL | G-2: [Same-Source pairs or none] -- PASS/FAIL | G-3: [labels] -- PASS/FAIL

> **GATE CLEARANCE SUMMARY**: G-1: [P/F] | G-2: [P/F] | G-3: [P/F]
> ALL GATES CLEARED -- Step 3d valid. / GATE FAILURE -- blocked.

> **REMEDIATION LOG** / "C-12 EXEMPTION APPLIES: all gates passed on first evaluation."

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active: `[remediation channel: spec / invocation / artifact / quality]` required.

Schema 5 transition: active. Phase 4 valid.

---

**Findings carry-forward**: [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel: active].

---

#### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY**: G-1: PASS | G-2: PASS | G-3: PASS -- ALL GATES CLEARED.

Amend (change): [finding] / [source] / [remediation channel] / [section] / [change] / [confirmed]
Amend (dismissal): [finding] / [reason] / [remediation channel] / [confirmed]

---

### Verdict (Phase 5 -- Compliance Ledger with Role-Level Adherence)

"Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All P1/P2/P3; FLOOR CHECK PASS | [labels; FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Only P1/P2/P3 | [severity values] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO only | [all Source labels] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted SG; EG-RELAY COMPLETE cited | [SA promoted; SG downstream; EG-RELAY COMPLETE PASS cited] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted SG | [Source labels; label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel | [channels per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | PHASE 4 GATE CLEARANCE PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) | G-1 holds across Phase 2a + 2b roles | [Source types and contributing roles per type] | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | 3a complete before 3b | [confirmed 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | FLOOR CHECK PASS before 3c | [FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | ALL GATES CLEARED before 3d | [gate clearance] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Channel active before Phase 4 | [activation + PHASE 4 GATE CLEARANCE] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined: C-19 + C-20 + C-21 (full integration, targeting 99.5/99.5)

**Axis**: All three new v5 criteria integrated. V-01 EG-first structural ordering + V-02
criterion inheritance registry + V-03 attribution table co-located in VC-4 G-1 row. Full
integration targeting dual convergence.

**Hypothesis**: V-04 tests C-19 + C-20 in isolation. V-05 adds C-21 (co-located attribution
sub-table in the VC-4 G-1 row). The three mechanisms are structurally independent: C-19 governs
Phase 2 execution order, C-20 governs prompt-level version continuity, C-21 governs the VC-4
compliance ledger format. No interaction risk. V-05 is the convergence candidate: all 5
essential PASS (inherited), all 3 recommended PASS (inherited), all 9 aspirational mechanisms
present (C-09 through C-18 inherited from prior architecture, C-19/C-20/C-21 added here).
If V-05 scores 99.5/99.5 on round scoring, this is the golden prompt for trace-inspect v5.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v5

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec informally; no structured source-layer separation
  2. Classifies gaps by intuition; SA/SG/EG distinction blurs
  3. Runs the skill with no baseline; no expected-output artifact to compare against
  4. No enforcement gates; under-populated findings advance without challenge
  5. No SA-TO-SG promotion lifecycle; spec gaps and setup gaps resolve ad hoc
  6. No compliance ledger; verdict quality depends on executor experience, not evidence
  Result: traces that cannot be independently audited or compared across runs.

INHERITED FROM v1 -- ESSENTIAL:
  C-01 (Phase completeness): INHERITED
  C-02 (Artifact produced): INHERITED
  C-03 (Schema 1 + Schema 2 compliance): INHERITED
  C-04 (Enforcement gates checked): INHERITED
  C-05 (Verdict present and classified): INHERITED

INHERITED FROM v1 -- RECOMMENDED:
  C-06 (SA-TO-SG promotion evaluated): INHERITED
  C-07 (Per-role relays complete): INHERITED
  C-08 (Findings table depth + FLOOR CHECK): INHERITED

INHERITED FROM v1 -- ASPIRATIONAL:
  C-09 (Compliance ledger populated): INHERITED
  C-10 (Sub-step transition sentences): INHERITED

INHERITED FROM v2 -- ASPIRATIONAL:
  C-11 (Phase-entry GATE CLEARANCE SUMMARY): INHERITED
  C-12 (Gate-failure REMEDIATION LOG): INHERITED
  C-13 (Sub-step prerequisite verification): INHERITED

INHERITED FROM v3 -- ASPIRATIONAL:
  C-14 (Pre-scoring mechanism at Phase 2 entry): INHERITED

INHERITED FROM v4 -- ASPIRATIONAL:
  C-15 (Stage 1 layer diversity warning): INHERITED
  C-16 (Evidence-grounded promotion citation): INHERITED
  C-17 (Source attribution table): INHERITED -- co-located with VC-4 G-1 row per C-21
  C-18 (Verdict classification rule citation): INHERITED

NEW IN v5 -- ASPIRATIONAL:
  C-19 (EG-first structural role ordering): NEW -- enforced via EG-FIRST EXECUTION CONSTRAINT
    and EG-RELAY COMPLETE gate; SA-TO-SG PROMOTION structurally blocked until PASS
  C-20 (Inertia registry with inheritance declaration): NEW -- this registry
  C-21 (Attribution table co-located in compliance ledger): NEW -- C-17 table embedded
    directly in VC-4 G-1 cross-role row; filling ledger and attribution are one operation
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b relays | All roles | VC-2 |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates across Phase 2a + 2b roles; G-1 attribution sub-table co-located in VC-4 G-1 row | VC-4 |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1 -- Severity Vocabulary**: {P1, P2, P3} only. P1 blocks usefulness. P2 is a quality
improvement. P3 is advisory. Every EG finding from every role uses only {P1, P2, P3}.

**Schema 2 -- Gap Type Taxonomy**: {SA, SG, EG, QO} only. Label lock invariant: a promoted SA
gap uses SG in all phases after SA-TO-SG PROMOTION. A promoted gap retaining SA is a structural
violation.

**Schema 3 -- Remediation Channel Taxonomy**: Every Phase 4 Amend entry includes `[remediation
channel: spec / invocation / artifact / quality]`. An entry without a channel field is
structurally incomplete.

**Schema 4 -- Enforcement Gate Registry**: G-1: Step 3b contains >=2 distinct Source types.
G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only
{P1, P2, P3}. Defects must be corrected and re-checked; they cannot be bypassed.

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
| [role from spec] | [severity labels applicable, or "N/A -- produces no EG findings"] | [Source labels this role may produce; label lock rules if promoted gaps] | YES / NO | [Schema 3/4 interactions] |

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

```
EG-producing roles (run Phase 2a -- must complete before SA-TO-SG PROMOTION):
  [list all roles marked EG-producing YES in Role-Schema Binding Summary]

SA/SG-only roles (run Phase 2b -- after SA-TO-SG PROMOTION):
  [list all roles marked EG-producing NO]

Structural invariant: SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE
checkpoint passes. A trace that evaluates SA-TO-SG PROMOTION before EG-RELAY COMPLETE PASS
is structurally invalid at that point. Evidence-grounded promotion is architecturally enforced,
not merely recommended.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete; examine all three layers before declaring done.

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
[layer diversity: `{{diversity_status}}`]. Stage 2 carries all gaps forward without re-deriving.

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

**EG-FIRST CONSTRAINT ACTIVE**: Only EG-producing roles from the EG-FIRST EXECUTION CONSTRAINT
run here. SA/SG-only roles are deferred to Phase 2b. SA-TO-SG PROMOTION is structurally
BLOCKED until the EG-RELAY COMPLETE checkpoint below shows PASS.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (SA-TO-SG PROMOTION is structurally BLOCKED until PASS):
>
> - EG-producing roles declared in EG-FIRST EXECUTION CONSTRAINT: [list]
> - EG-producing roles with completed relays: [list]
> - All EG-producing roles relayed: YES / NO
>
> **EG-RELAY COMPLETE result: PASS** (all EG roles relayed, SA-TO-SG PROMOTION now valid)
> / **FAIL** (missing relays: [role list] -- complete relays before proceeding)

---

#### SA-TO-SG PROMOTION (named lifecycle event -- EG-RELAY COMPLETE PASS required)

**Prerequisite**: EG-RELAY COMPLETE PASS confirmed above. Every SA gap from Stage 1 is
evaluated here. Promotion decisions cite Phase 2a execution evidence where available.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence -- cite Phase 2a execution evidence if available; spec inference otherwise]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant: a promoted gap using SA in any downstream phase is a structural violation.

---

#### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Role relay -- [SA/SG-only role name]**:
- Received from: [prior role or SA-TO-SG PROMOTION]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: none -- this role does not produce EG findings

**Artifact write** (after all Phase 2a + 2b relays):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Sections written: [list each required section with WRITTEN status]

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

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
> - Distinct Source types present: [list each type] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add findings before advancing. A missing source layer requires at least one finding
> from that layer. Duplicate Actions require distinct remediation targets. Re-run FLOOR CHECK.
> A bare count without named Finding IDs is not a valid FLOOR CHECK.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c -- Enforcement Gates

Schema 5 prerequisite: Step 3b FLOOR CHECK PASS.
Schema 5 output: gate results (all PASS to unblock Step 3d).

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
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added or text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY ALL GATES CLEARED. Step 3d valid.

---

##### Step 3d -- Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c GATE CLEARANCE SUMMARY ALL GATES CLEARED.
Schema 5 output: Schema 3 channel taxonomy activated (unblocks Phase 4).

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
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced at Step 3a] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS; IDs named | [list severity labels used; cite FLOOR CHECK result with IDs] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and the labels it checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels used in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted SG; lock holds; EG-RELAY COMPLETE cited | [list SA gaps promoted; confirm SG downstream; confirm EG-RELAY COMPLETE PASS cited as prerequisite] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; identify promoted gaps; confirm SG label] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state the activation language at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry; flag any missing] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three results as recorded at Step 3c] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | PHASE 4 GATE CLEARANCE SUMMARY PASS before Phase 4 | [state Phase 4 GATE CLEARANCE SUMMARY result] | PASS/FAIL |
| VC-4 | Schema 4 | **Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION** | G-1 holds across all Phase 2a + 2b roles AND C-17 attribution filled as sub-table of this row | **This cell is not complete until the G-1 SOURCE ATTRIBUTION TABLE below is filled:**<br>G-1 result: [PASS/FAIL]<br>**G-1 SOURCE ATTRIBUTION TABLE:**<br>&#124; Source type &#124; Phase &#124; Role(s) that contributed &#124; Finding IDs &#124;<br>&#124; [type] &#124; 2a/2b &#124; [role(s)] &#124; [F-IDs] &#124;<br>&#124; [type] &#124; 2a/2b &#124; [role(s)] &#124; [F-IDs] &#124;<br>All Source types in Step 3b attributable to a named role: YES/NO | PASS/FAIL |
| VC-5 | Schema 5 | 3a -> 3b | Step 3b valid only after Step 3a complete | [state what confirmed Step 3a done before Step 3b began] | PASS/FAIL |
| VC-5 | Schema 5 | 3b -> 3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result with finding IDs] | PASS/FAIL |
| VC-5 | Schema 5 | 3c -> 3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result before Step 3d began] | PASS/FAIL |
| VC-5 | Schema 5 | 3d -> Phase 4 | Phase 4 valid only after channel taxonomy active + PHASE 4 GATE CLEARANCE SUMMARY | [state both conditions confirmed before Phase 4 began] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**:
`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the classification rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
