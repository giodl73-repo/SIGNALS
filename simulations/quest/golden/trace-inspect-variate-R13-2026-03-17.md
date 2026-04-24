---
skill: quest-variate
skill_target: trace-inspect
date: 2026-03-17
round: 13
rubric: trace-inspect-rubric-v9
---

# trace-inspect -- Variations R13 v9 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined
(V-04, V-05).

**Entry state**: R12 V-04 achieves 102.5/102.5 under rubric v8 -- all C-01 through C-27 PASS.
Rubric v9 adds C-28 and C-29 (0.5 pts each; grand total 103.5). Baseline = 102.5/103.5.

**R12 V-04 carries**:
- C-26 (NEEDS-REDESIGN EVIDENCE ANCHOR): Phase 5 verdict enumerates EG finding IDs by name;
  EG count derived from the list. A scorer reads the count from the block alone.
- C-27 (PROMOTION COMPLETENESS GATE): SA-TO-SG PROMOTION block has arithmetic closure table:
  `promoted + remaining = Stage 1 SA count` with PASS/MISMATCH result; MISMATCH blocks Phase 2b.

**R12 excellence signals that became C-28 and C-29**:
- V-01 in R12 satisfied C-26: the EVIDENCE ANCHOR lists EG finding IDs (e.g., F-01, F-03,
  F-05). But observation: a model can write F-07 in the EVIDENCE ANCHOR when F-07 does not
  exist as a Step 3b row. The IDs are enumerated but not anchored -- citation is structural
  form without traceable content. C-28 requires the anchor to be traceable: each cited ID
  must resolve to a specific Step 3b row, making the claim auditable from the block alone.
- V-04 in R12 satisfied both C-26 and C-27: EVIDENCE ANCHOR carries EG count, PROMOTION
  COMPLETENESS GATE carries SA remaining count. But the Phase 5 verdict section does not
  co-locate these two structural facts. A scorer reading the verdict must retrieve SA remaining
  from the promotion block (Stage 2) separately. C-29 requires the verdict evidence summary
  to forward-reference the SA remaining count from the promotion arithmetic, placing both
  counts in the same Phase 5 section.

**R13 variation axes**:

- **V-01 (single axis: lifecycle emphasis)**: VERDICT-TO-TABLE TRACEABILITY sub-table inside
  the NEEDS-REDESIGN EVIDENCE ANCHOR block. For each cited EG finding ID, a resolution row:
  `ID | Step 3b Finding excerpt | Source | Severity`. Scorer confirms C-28 from the
  sub-table alone; no Step 3b re-read required.

- **V-02 (single axis: output format)**: VERDICT EVIDENCE SUMMARY block in Phase 5 after the
  EVIDENCE ANCHOR. Two-row summary: EG count (from EVIDENCE ANCHOR) and SA remaining count
  (from PROMOTION COMPLETENESS GATE). Both structural facts co-located at verdict time.

- **V-03 (single axis: phrasing register -- alternative C-28 mechanism)**: Count-reconciliation
  CHECK before verdict classification. Step 3b EG row count must equal EVIDENCE ANCHOR ID list
  count; MISMATCH blocks classification. Tests whether count-check achieves C-28 without a
  per-ID resolution sub-table.

- **V-04 (combined: C-28 + C-29)**: V-01's resolution sub-table PLUS V-02's VERDICT EVIDENCE
  SUMMARY. Both criteria targeted in one prompt.

- **V-05 (full integration: C-28 + C-29 + expanded inertia)**: V-04 combined axes plus
  inertia block extended to name both failure modes addressed by C-28 and C-29.

All five inherit the full R12 V-04 architecture (C-01 through C-27 PASS). What varies per
V-0N: only the structural element listed above and in the CRITERION INHERITANCE REGISTRY
version update.

---

## V-01 -- Single axis: Lifecycle emphasis (C-28 target: Verdict-to-table traceability)

**Axis**: Lifecycle emphasis -- the NEEDS-REDESIGN EVIDENCE ANCHOR block in Phase 5 gains a
VERDICT-TO-TABLE TRACEABILITY sub-table. For each EG finding ID cited in the EVIDENCE ANCHOR,
a resolution row must appear: the ID is linked to its Step 3b row by repeating the Finding
excerpt, Source, and Severity. A scorer confirms C-28 by checking the sub-table; no Step 3b
re-read required.

**Hypothesis**: C-26 made EG count structural (derived from a named list). C-28 makes the
*content* of that list structural: each ID is verifiable at the point of citation, not merely
asserted. The resolution sub-table is a forward reference from Phase 5 back to Step 3b -- the
same linkage logic as C-25 (VC-4 G-1 attribution cites PHASE 2a/2b MEMBERSHIP counts). Risk:
one sub-table row per cited finding; adds N rows for N EG gaps. Mitigation: the sub-table is
a copy of Step 3b EG rows, not new content -- only structure.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v9

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is re-derived,
     not anchored to named finding IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b;
     IDs may be fabricated or mis-remembered with no structural check
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
    embedded directly in VC-4 G-1 cross-role row

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED -- "Enforcement class" column in Coverage
    Matrix; [enforcement: X] inline suffix on every named invariant
  C-23 (Phase 2a/2b role membership enumerated): INHERITED -- PHASE 2a/2b MEMBERSHIP named
    blocks in EG-FIRST EXECUTION CONSTRAINT; role names and counts auditable from the block

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED -- EG-FIRST EXECUTION
    CONSTRAINT states "[enforcement: architectural -- see Coverage Matrix Schema 4 column]"
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED -- VC-4 G-1 attribution
    row verifies Phase 2a/2b role counts match MEMBERSHIP block declarations

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED -- NEEDS-REDESIGN EVIDENCE ANCHOR block
    in Verdict enumerates EG finding IDs from Step 3b; count derived from the named list
  C-27 (Promotion completeness gate): INHERITED -- PROMOTION COMPLETENESS GATE arithmetic
    table in SA-TO-SG PROMOTION: promoted + remaining = Stage 1 SA count; MISMATCH blocks Phase 2b

NEW IN v9 -- ASPIRATIONAL CRITERION (R13 candidate):
  C-28 (Verdict-to-table traceability): NEW -- enforced via VERDICT-TO-TABLE TRACEABILITY
    sub-table inside NEEDS-REDESIGN EVIDENCE ANCHOR; each cited EG finding ID resolved to
    its Step 3b row (Finding excerpt | Source | Severity); traceability auditable from the
    sub-table alone without re-reading Step 3b
```

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol
authority: every label, channel, and gate used in any downstream phase must be declared in
this table.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional: vocabulary compliance required; violations detectable in VC-1 but not structurally blocked |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional: label compliance and label lock required; violations detectable in VC-2 but not structurally blocked |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional: channel field inclusion required; omissions detectable in VC-3 but not structurally blocked |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural: GATE CLEARANCE SUMMARY and PHASE 4 GATE CLEARANCE SUMMARY gate advancement; violation structurally impossible in a conformant trace |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural: each sub-step declares a named prerequisite; Schema 5 transition sentence confirms completion; advancement structurally blocked until satisfied |

**Schema 1 -- Severity Vocabulary** `[enforcement: instructional]`: {P1, P2, P3} only. P1
blocks usefulness. P2 is quality improvement. P3 is advisory. Violations detectable in VC-1.

**Schema 2 -- Gap Type Taxonomy** `[enforcement: instructional]`: {SA, SG, EG, QO} only.
Label lock invariant `[enforcement: instructional]`: promoted SA gap uses SG downstream;
retaining SA after promotion is a violation detectable in VC-2.

**Schema 3 -- Remediation Channel Taxonomy** `[enforcement: instructional]`: Every Phase 4
Amend entry includes channel field. Omissions detectable in VC-3.

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

---

### Phase 1 -- Setup: Role-Schema Binding Summary

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

#### EG-FIRST EXECUTION CONSTRAINT (named structural constraint)

Execution phase membership is declared here independently of the Role-Schema Binding Summary.

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class: SA/SG gaps only; runs in Phase 2b)
  PHASE 2b role count: [M]

Total roles: [N + M] (must equal total roles in Role-Schema Binding Summary)

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION is structurally BLOCKED until EG-RELAY COMPLETE checkpoint passes.
```

---

### Stage 1 -- Source-Layer Audit

A valid Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one
source type is structurally incomplete -- layer diversity is required for G-1 to pass.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: Only PHASE 2a MEMBERSHIP roles run here. SA-TO-SG PROMOTION
is structurally BLOCKED `[enforcement: architectural]` until EG-RELAY COMPLETE passes.

**Role relay -- [EG-producing role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

> **EG-RELAY COMPLETE** (SA-TO-SG PROMOTION is BLOCKED until this PASSES):
>
> - PHASE 2a MEMBERSHIP declared: [list role names + count N]
> - EG-producing roles with completed relays: [list]
> - All PHASE 2a roles relayed: YES / NO
> - **EG-RELAY COMPLETE result: PASS / FAIL**
> - If FAIL: complete the missing EG role relay before SA-TO-SG PROMOTION.

---

### SA-TO-SG PROMOTION (named lifecycle event -- requires EG-RELAY COMPLETE PASS)

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

> **PROMOTION COMPLETENESS GATE** (arithmetic closure -- validates no gap was silently dropped):
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N from Stage 1 relay] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> If MISMATCH: Phase 2b is structurally BLOCKED. Reconcile the missing gap before continuing.

Label lock invariant `[enforcement: instructional]`: a promoted gap using its SA label in
any downstream phase is a structural violation detectable in VC-2.

---

### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Only PHASE 2b MEMBERSHIP roles run here.**

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

### Phase 3 -- Findings

Phase 3 is valid if and only if sub-steps run in the order declared by Schema 5.

#### Step 3a -- Severity Legend Declaration

Prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [quality improvement] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

#### Step 3b -- Findings Table

Prerequisite: Step 3a complete (severity legend defined above).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (trace may not advance to Step 3c until PASSES):
>
> - Finding IDs counted: [list all IDs explicitly, e.g., F-01, F-02, F-03]
> - Row count: N (required: >= 3)
> - Distinct Source types present: [list] (required: >= 2 distinct types)
> - Action-uniqueness check: any two Action cells identical? YES (FAIL) / NO (PASS)
> - **FLOOR CHECK result: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

#### Step 3c -- Enforcement Gates

Prerequisite: Step 3b FLOOR CHECK PASS.

**G-1** `[enforcement: architectural]`: Step 3b contains >=2 distinct Source types.
- Source types present: [list] -- G-1: PASS / FAIL

**G-2** `[enforcement: architectural]`: No two same-Source findings share identical Action.
- Same-Source pairs examined: [list or "no same-Source pairs"] -- G-2: PASS / FAIL

**G-3** `[enforcement: architectural]`: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list] -- G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required before Step 3d):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Entry verdict: ALL GATES CLEARED -- Step 3d is valid to begin.
> OR: GATE FAILURE -- Step 3d is BLOCKED.

> **REMEDIATION LOG** (required if any gate FAILs; if all gates PASS on first evaluation:
> "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation loop."):
>
> Gate [X] FAIL:
> - Failure reason: [specific text]
> - Remediation action: [specific finding ID added or text changed]
> - Re-check: G-[X] result: PASS / FAIL

Schema 5 transition: GATE CLEARANCE SUMMARY declares ALL GATES CLEARED. Step 3d valid.

---

#### Step 3d -- Channel Taxonomy Activation

Prerequisite `[enforcement: architectural]`: Step 3c GATE CLEARANCE SUMMARY ALL GATES CLEARED.

Channel taxonomy active `[enforcement: instructional]`: every Phase 4 Amend entry must include
`[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

---

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]` (required at Phase 4 entry):
> G-1: [PASS] | G-2: [PASS] | G-3: [PASS]
> Phase 4 entry verdict: ALL GATES CLEARED -- Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `{{F-NN}}`] | [source: `{{source}}`] | [remediation channel: spec/invocation/artifact/quality]
- [section or field changed: ] | [change: ] | [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`] | [reason: ] | [remediation channel: spec/invocation/artifact/quality]
- [source type confirmed: YES / NO]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS | [list labels; cite FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; PROMOTION COMPLETENESS GATE PASS | [list SA gaps promoted; confirm SG downstream; confirm gate PASS] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 with explicit PASS/FAIL | [state all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 after PHASE 4 GATE CLEARANCE SUMMARY PASS | [state Phase 4 gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1 cross-role) -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; MEMBERSHIP counts validate attribution | **G-1 SOURCE ATTRIBUTION TABLE**: Source type / Phase (2a or 2b) / Role(s) / Finding IDs -- [fill one row per Source type; verify Phase 2a count = N from MEMBERSHIP block; Phase 2b count = M; mismatch = membership inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | Step 3b valid only after 3a complete | [confirm 3a done] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | Step 3c valid only after FLOOR CHECK PASS | [cite FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | Step 3d valid only after GATE CLEARANCE SUMMARY ALL CLEAR | [state gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation + PHASE 4 GATE CLEARANCE SUMMARY] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite finding IDs) / NO
> - Fires: YES (both conditions true) / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to its Step 3b row):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell from Step 3b] | EG | [P1/P2/P3] |
>
> Traceability check: each ID in the EG findings list above appears as a distinct row
> in this table with matching Source=EG. If any cited ID has no corresponding row here,
> the EVIDENCE ANCHOR contains a non-existent finding reference -- verdict is
> structurally invalid until reconciled.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired; cite finding IDs from EVIDENCE ANCHOR]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Output format (C-29 target: Promotion count forward-reference)

**Axis**: Output format -- Phase 5 adds a VERDICT EVIDENCE SUMMARY block after the NEEDS-REDESIGN
EVIDENCE ANCHOR. The summary contains two rows: EG count (sourced from the EVIDENCE ANCHOR list)
and SA remaining count (sourced from the PROMOTION COMPLETENESS GATE arithmetic closure). Both
structural facts are co-located in Phase 5. A scorer reading the verdict does not need to retrieve
SA remaining from the Stage 2 promotion block.

**Hypothesis**: The PROMOTION COMPLETENESS GATE (C-27) produces a structurally validated SA
remaining count. The EVIDENCE ANCHOR (C-26) produces a structurally derived EG count. Both facts
are relevant to the classification: SA remaining drives the NEEDS-SPEC-REVISION check; EG count
drives NEEDS-REDESIGN. But they live in different phases. C-29 places both in Phase 5 via an
EVIDENCE SUMMARY block, making the verdict's two classification inputs self-contained. Risk: one
additional block in Phase 5. Mitigation: both values are already computed; the block is a
forward-reference, not new computation.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v9

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is not anchored
  8. Reads the verdict without SA remaining count from promotion; must re-read Stage 2 to
     reconstruct the full evidence picture; verdict and promotion data are disconnected
  Result: traces that pass or fail based on executor judgment, not structural evidence.

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
  C-19 (EG-first structural role ordering): INHERITED
  C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
  C-21 (Attribution table co-located in compliance ledger): INHERITED

INHERITED FROM v6 -- ASPIRATIONAL CRITERIA:
  C-22 (Enforcement class annotation): INHERITED
  C-23 (Phase 2a/2b role membership enumerated): INHERITED

INHERITED FROM v7 -- ASPIRATIONAL CRITERIA:
  C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
  C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED
  C-27 (Promotion completeness gate): INHERITED

NEW IN v9 -- ASPIRATIONAL CRITERION (R13 candidate):
  C-29 (Promotion count forward-reference): NEW -- enforced via VERDICT EVIDENCE SUMMARY
    block in Phase 5; block carries EG count (from EVIDENCE ANCHOR) and SA remaining count
    (from PROMOTION COMPLETENESS GATE); both classification inputs co-located at verdict time;
    scorer reads complete evidence picture from Phase 5 without retrieving Stage 2 data
```

---

### Trace Protocol Schemas (Coverage Matrix)

[Same Coverage Matrix as V-01 -- all schemas and enforcement classes identical.]

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, Phase 2a/2b role relays | All roles | VC-2 | instructional |
| Schema 3 -- Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 | architectural |

**Schema 1** `[enforcement: instructional]`: {P1, P2, P3} only.
**Schema 2** `[enforcement: instructional]`: {SA, SG, EG, QO} only. Label lock enforced.
**Schema 3** `[enforcement: instructional]`: channel field required in every Phase 4 entry.
**Schema 4** `[enforcement: architectural]`: G-1/G-2/G-3 gate advancement.
**Schema 5** `[enforcement: architectural]`: named prerequisites gate each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | all-PASS gates | Channel taxonomy activated | Phase 4 |

---

### Phase 1 -- Setup: Role-Schema Binding Summary

[Same Phase 1 structure as V-01.]

Confirmed input bindings: [topic:], [scope_in:], [scope_out:], [roles:], [spec_version:]

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable]
  Schema 2 binding: [Source labels; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

#### EG-FIRST EXECUTION CONSTRAINT
```
PHASE 2a MEMBERSHIP: [EG-class roles] | count: [N]
PHASE 2b MEMBERSHIP: [SA/SG-class roles] | count: [M]
Total: [N+M]
Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE PASS.
```

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Phase 2a -- EG-First Execution

**Role relay -- [EG-producing role]**:
- Received from: / Received values: / Schema 2 compliance: / SA/SG gaps: / Produced: / EG gaps:

> **EG-RELAY COMPLETE**: PHASE 2a roles declared: [N] | relayed: [N] | result: PASS/FAIL

---

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: [gap] | Promotion: PROMOTES TO SG-NN / REMAINS SA | Reason: [one sentence]
```

```
[SA remaining: R] [SG from promotion: P] [SG original: O]
```

> **PROMOTION COMPLETENESS GATE**:
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> **SA remaining (certified): R** -- this value is forward-referenced in Phase 5 VERDICT
> EVIDENCE SUMMARY. If MISMATCH: Phase 2b BLOCKED until reconciled.

Label lock `[enforcement: instructional]`: promoted gap must use SG label downstream.

---

### Phase 2b -- SA/SG-Only Role Execution

**Role relay -- [SA/SG-only role]**:
- Received from: / Received values: / Schema 2 compliance: / SA/SG gaps: / Produced: / EG gaps: none

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

### Phase 3 -- Findings

#### Step 3a -- Severity Legend
| Label | Definition | Threshold |
|-------|-----------|-----------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Amend or follow-on |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

#### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [list] | count >= 3: Y/N | distinct Source types >= 2: Y/N |
> Action uniqueness: PASS/FAIL | **FLOOR CHECK: PASS/FAIL**

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

G-1: [result] | G-2: [result] | G-3: [result]

> **GATE CLEARANCE SUMMARY**: G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL
> ALL GATES CLEARED / GATE FAILURE

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES" if all pass first evaluation)

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

#### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active. Phase 4 valid to begin.

---

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY**: G-1/G-2/G-3 all PASS. Phase 4 valid.

[Amend entries with finding, source, remediation channel, change/dismissal]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All P1/P2/P3 + FLOOR CHECK PASS | [labels; FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result + labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | P1/P2/P3 only | [severity values in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted = SG; COMPLETENESS GATE PASS | [gaps promoted; gate result] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; label lock | [Source labels; lock check] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel field in every entry | [channels listed] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 PASS/FAIL | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 entry | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b G-1 -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; MEMBERSHIP counts check | **G-1 SOURCE ATTRIBUTION TABLE**: Source/Phase/Role(s)/Finding IDs [fill per Source type; verify counts vs MEMBERSHIP blocks] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion evidence] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after FLOOR CHECK | [FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after ALL GATES CLEARED | [gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after channel taxonomy active | [activation + PHASE 4 gate summary] | PASS/FAIL |

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26):
>
> NEEDS-SPEC-REVISION check: P1 SA remaining: [count -- list IDs if > 0] | Fires: YES/NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list IDs, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold 3: EG count > 3: YES/NO | Structural role gap: YES/NO
> - Fires: YES/NO
>
> USEFUL: fires when neither above fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Classification driven by: EG count [N] and SA remaining [R]. Both values are
> structurally derived (EG: named list; SA: arithmetic closure). No re-read of
> prior phases required to verify the classification inputs.

**Trace result**: `NEEDS-SPEC-REVISION` / `NEEDS-REDESIGN` / `USEFUL`
**Verdict**: [classification]
**Rationale**: [one sentence; cite finding IDs and classification rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Phrasing register (C-28 alternative: count-reconciliation check)

**Axis**: Phrasing register -- instead of a resolution sub-table per finding ID, a COUNT
RECONCILIATION CHECK immediately follows the EVIDENCE ANCHOR list. The check counts EG rows
in Step 3b with Source=EG and verifies that count equals the EVIDENCE ANCHOR list length. If
they differ, classification is BLOCKED until reconciled. This tests whether an arithmetic
count-check achieves C-28 without per-ID resolution rows.

**Hypothesis**: C-27 (PROMOTION COMPLETENESS GATE) achieves inventory integrity via arithmetic
(promoted + remaining = Stage 1 SA count). An analogous check for C-28 would count EG entries
in Step 3b and match against the EVIDENCE ANCHOR list length. If the counts match, the list is
self-consistent -- fabricated IDs would show as a count > Step 3b EG row count. Risk: a
count-check detects surplus IDs but not wrong IDs (an ID that exists in Step 3b but refers to
the wrong finding). Mitigation: the per-ID resolution sub-table in V-01 catches wrong IDs; this
variation explores whether the simpler count-check is sufficient for the C-28 criterion.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v9

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is not anchored
  8. Lists EG IDs in the verdict; does not reconcile the list length against the Step 3b
     EG row count; count inconsistencies go undetected
  Result: traces that pass or fail based on executor judgment, not structural evidence.

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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15–C-18: INHERITED
INHERITED FROM v5: C-19–C-21: INHERITED
INHERITED FROM v6: C-22–C-23: INHERITED
INHERITED FROM v7: C-24–C-25: INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED
  C-27 (Promotion completeness gate): INHERITED

NEW IN v9 -- ASPIRATIONAL CRITERION (R13 candidate -- alternative mechanism for C-28):
  C-28 (Verdict-to-table traceability -- count-check variant): CANDIDATE -- enforced via
    COUNT RECONCILIATION CHECK following EVIDENCE ANCHOR; Step 3b EG row count must equal
    EVIDENCE ANCHOR list length; MISMATCH blocks classification; tests whether arithmetic
    reconciliation achieves C-28 without per-ID resolution sub-table
```

---

[Schemas and Phases 1-4 identical to V-01.]

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Enforcement class |
|--------|---------|-------------------|
| Schema 1 -- Severity Vocabulary | P1/P2/P3 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA/SG/EG/QO | instructional |
| Schema 3 -- Channel Taxonomy | spec/invocation/artifact/quality | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a->3b->3c->3d | architectural |

Schema descriptions and sub-step prerequisite table: [same as V-01].

---

### Phase 1 -- Setup

[Same structure as V-01: confirmed bindings, per-role schema binding blocks, EG-FIRST EXECUTION CONSTRAINT with PHASE 2a/2b MEMBERSHIP declarations.]

---

### Stage 1 -- Source-Layer Audit

[Same as V-01.]

---

### Phase 2a -- EG-First Execution / EG-RELAY COMPLETE / SA-TO-SG PROMOTION with PROMOTION COMPLETENESS GATE / Phase 2b

[Same as V-01 through end of Phase 2b including PROMOTION COMPLETENESS GATE.]

---

### Phase 3 -- Findings (Steps 3a, 3b, 3c, 3d)

[Same as V-01.]

---

### Phase 4 -- Amend

[Same as V-01.]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid.

[Compliance ledger VC-1 through VC-5 identical to V-01.]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26):
>
> NEEDS-SPEC-REVISION check: P1 SA remaining: [count -- list IDs if > 0] | Fires: YES/NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold 3: EG count > 3: YES/NO | Structural role gap: YES/NO | Fires: YES/NO
>
> **COUNT RECONCILIATION CHECK** (C-28 candidate -- count-check variant):
> - EG rows in Step 3b with Source=EG: [count by scanning Step 3b Source column]
> - EG IDs listed in EVIDENCE ANCHOR: [N from the list above]
> - Counts match: YES / NO
> - If NO (TRACEABILITY MISMATCH): the EVIDENCE ANCHOR list references EG findings that
>   do not all exist in Step 3b, or Step 3b contains EG findings not cited in the verdict.
>   Classification is BLOCKED until the EVIDENCE ANCHOR list and Step 3b EG rows are
>   reconciled. (Add missing rows or remove non-existent IDs before classifying.)
> - If YES: TRACEABILITY CONFIRMED -- EVIDENCE ANCHOR IDs are consistent with Step 3b.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

**Trace result**: `NEEDS-SPEC-REVISION` / `NEEDS-REDESIGN` / `USEFUL`
**Verdict**: [classification]
**Rationale**: [one sentence; cite finding IDs and classification rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined: Lifecycle emphasis + Output format (C-28 + C-29 targets)

**Axis**: V-01's VERDICT-TO-TABLE TRACEABILITY sub-table (per-ID resolution, C-28) PLUS V-02's
VERDICT EVIDENCE SUMMARY block (SA remaining forward-reference, C-29). Both criteria targeted
in one prompt. No prior criterion degraded.

**Hypothesis**: C-28 and C-29 are structurally independent (C-28 operates on the EG finding
ID list; C-29 adds SA remaining alongside EG count in a summary block). They can coexist in
Phase 5 without conflict: the EVIDENCE ANCHOR lists EG IDs, the TRACEABILITY sub-table resolves
each ID, and the EVIDENCE SUMMARY carries both EG count and SA remaining. The combined structure
produces a Phase 5 verdict section that is fully self-contained: all classification inputs are
present and traceable without re-reading any prior phase.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v9

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is not anchored
  8. Cites EG IDs without verifying each exists in Step 3b; IDs may be wrong or fabricated
  9. Reads the verdict without SA remaining count; must retrieve it from Stage 2 separately;
     verdict and promotion data are in different sections with no structural link
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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 (Stage 1 layer diversity warning): INHERITED
          C-16 (Evidence-grounded promotion citation): INHERITED
          C-17 (Source attribution table): INHERITED
          C-18 (Verdict classification rule citation): INHERITED
INHERITED FROM v5: C-19 (EG-first structural role ordering): INHERITED
          C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
          C-21 (Attribution table co-located in compliance ledger): INHERITED
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED
          C-23 (Phase 2a/2b role membership enumerated): INHERITED
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED -- EVIDENCE ANCHOR enumerates EG IDs;
    count derived from list
  C-27 (Promotion completeness gate): INHERITED -- PROMOTION COMPLETENESS GATE arithmetic
    closure in SA-TO-SG PROMOTION; MISMATCH blocks Phase 2b

NEW IN v9 -- ASPIRATIONAL CRITERIA (R13 targets):
  C-28 (Verdict-to-table traceability): NEW -- VERDICT-TO-TABLE TRACEABILITY sub-table in
    EVIDENCE ANCHOR; each cited EG finding ID resolved to its Step 3b row (Finding excerpt
    | Source | Severity); traceability auditable from sub-table alone
  C-29 (Promotion count forward-reference): NEW -- VERDICT EVIDENCE SUMMARY block in Phase 5;
    EG count from EVIDENCE ANCHOR and SA remaining count from PROMOTION COMPLETENESS GATE
    co-located; both classification inputs present in Phase 5 without re-read of prior phases
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce + FLOOR CHECK), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b Source column, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source across roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 | architectural |

**Schema 1** `[enforcement: instructional]`: {P1, P2, P3}. Violations detectable in VC-1.
**Schema 2** `[enforcement: instructional]`: {SA, SG, EG, QO}. Label lock: promoted SA uses SG.
**Schema 3** `[enforcement: instructional]`: channel field required in every Phase 4 entry.
**Schema 4** `[enforcement: architectural]`: G-1/G-2/G-3 gate advancement structurally blocked.
**Schema 5** `[enforcement: architectural]`: named prerequisites gate each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | all-PASS gates | Channel taxonomy activated | Phase 4 |

---

### Phase 1 -- Setup: Role-Schema Binding Summary

Confirmed input bindings: [topic:], [scope_in:], [scope_out:], [roles:], [spec_version:]

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA], [SG original].

#### EG-FIRST EXECUTION CONSTRAINT

```
PHASE 2a MEMBERSHIP (EG-class roles):
  - [Role A] (EG-class)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles):
  - [Role C] (SA/SG-class)
  PHASE 2b role count: [M]

Total roles: [N + M]

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE PASS.
```

---

### Stage 1 -- Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: SA-TO-SG PROMOTION BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE passes.

**Role relay -- [EG-producing role]**:
- Received from: | Received values: | Schema 2 compliance `[enforcement: instructional]`: Source labels: [list] -- {SA,SG,EG,QO}: YES/NO
- SA/SG gaps: | Produced: | EG gaps: [EG-NN list or "none"]

> **EG-RELAY COMPLETE**: PHASE 2a roles declared: [N] | relayed: [N] | **PASS / FAIL**
> If FAIL: complete missing relay before SA-TO-SG PROMOTION.

---

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: [gap] | Promotion: PROMOTES TO SG-NN / REMAINS SA | Reason: [one sentence -- cite Phase 2a evidence]
```

```
[SA remaining: R] [SG from promotion: P] [SG original: O]
```

> **PROMOTION COMPLETENESS GATE**:
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> If MISMATCH: Phase 2b BLOCKED. Reconcile before continuing.

Label lock `[enforcement: instructional]`: promoted gaps must use SG label downstream.

---

### Phase 2b -- SA/SG-Only Role Execution

**Role relay -- [SA/SG role]**:
- Received from: | Values: | Schema 2 compliance: | SA/SG gaps: | Produced: | EG gaps: none

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections written: [list each required section -- WRITTEN]

---

### Phase 3 -- Findings

#### Step 3a -- Severity Legend

| Label | Definition | Threshold |
|-------|-----------|-----------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Amend or follow-on |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

#### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [e.g., F-01, F-02, F-03] | count >= 3: Y/N |
> distinct Source types >= 2: Y/N | Action uniqueness: Y/N | **FLOOR CHECK: PASS/FAIL**
> If FAIL: add findings. Re-run after correction.

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

**G-1** `[enforcement: architectural]`: >= 2 distinct Source types in Step 3b.
- Source types present: [list] -- G-1: PASS/FAIL

**G-2** `[enforcement: architectural]`: No same-Source findings with identical Action.
- Same-Source pairs: [list or "none"] -- G-2: PASS/FAIL

**G-3** `[enforcement: architectural]`: All entries use {P1, P2, P3}.
- Severity labels: [list] -- G-3: PASS/FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL
> ALL GATES CLEARED -- Step 3d valid. / GATE FAILURE -- Step 3d BLOCKED.

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES: all gates passed on first evaluation"):
> Gate [X] FAIL: reason / remediation action / re-check result

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

#### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active `[enforcement: instructional]`. Phase 4 valid to begin.

---

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS | G-2: PASS | G-3: PASS -- Phase 4 valid to begin.

[Amend entries: finding / source / remediation channel: spec-invocation-artifact-quality / change or dismissal / source confirmed]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Name specific values, label lists,
finding IDs, role names, or invariant results in every Observed-behavior cell.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Legend P1/P2/P3 declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | All P1/P2/P3; FLOOR CHECK PASS | [labels; cite FLOOR CHECK] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result + labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 | P1/P2/P3 in all Amend entries | [severity values in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels | [all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted=SG; COMPLETENESS GATE PASS | [gaps promoted; confirm SG; gate PASS] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; label lock | [Source labels; lock check] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in every entry | [channels per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 PASS/FAIL | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 entry | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3b G-1 -- C-21 | G-1 verified; MEMBERSHIP counts | **G-1 SOURCE ATTRIBUTION TABLE**: Source / Phase / Role(s) / Finding IDs [per Source type; verify counts vs MEMBERSHIP blocks] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion evidence] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after FLOOR CHECK | [FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after ALL GATES CLEARED | [gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after channel taxonomy | [activation + PHASE 4 gate summary] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite IDs) / NO
> - Fires: YES / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to Step 3b row):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of the Finding cell] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of the Finding cell] | EG | [P1/P2/P3] |
>
> Traceability check: every ID above appears as a distinct Step 3b row with Source=EG.
> If any cited ID has no resolution row here, the EVIDENCE ANCHOR is structurally invalid
> -- classification BLOCKED until reconciled.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived. No re-read of prior phases required to verify
> the classification inputs.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence; cite finding IDs from EVIDENCE ANCHOR and rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Full integration: C-28 + C-29 + expanded inertia framing

**Axis**: V-04 combined axes (C-28 resolution sub-table + C-29 VERDICT EVIDENCE SUMMARY) plus
inertia framing extended to name both failure modes explicitly, and V-03's COUNT RECONCILIATION
CHECK added as a secondary verification layer after the resolution sub-table. The count-check
validates the sub-table is complete (no EG row in Step 3b omitted from the sub-table); the
sub-table validates each ID resolves to a real row. Together they provide mutual verification.

**Hypothesis**: V-04 produces structural traceability (per-ID resolution) and co-location (SA
remaining + EG count at verdict). V-03's count-check adds a secondary invariant: the TRACEABILITY
sub-table must be complete, not just correct for the rows it includes. If Step 3b has 4 EG rows
and the sub-table lists only 3, the count-check fires. This prevents selective traceability --
only citing the EG findings that support the verdict while silently omitting others. The inertia
block extension makes both failure modes visible as explicit inertia behaviors the skill corrects.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### CRITERION INHERITANCE REGISTRY -- v9

```
INERTIA COMPETITOR (what a developer does without this skill):
  1. Reads the skill spec once, informally
  2. Guesses which gaps matter based on experience, not evidence
  3. Runs the skill with no baseline for expected output
  4. Cannot distinguish spec-layer gaps from execution-layer gaps
  5. Has no enforcement gate to prevent a flawed trace from producing a verdict
  6. Cannot determine whether a constraint is architecturally enforced or merely instructional
  7. Counts EG findings by re-reading the table at verdict time; count is not anchored to IDs
  8. Cites EG finding IDs in the verdict without verifying each ID exists in Step 3b; a model
     writing "F-07" when Step 3b has no F-07 row produces a structurally unverifiable verdict
  9. Omits EG findings from the verdict citation that inconveniently complicate the verdict
     narrative; cherry-picks IDs that fit the classification; count is not validated against
     the complete Step 3b EG inventory
  10. Reads verdict without SA remaining count; must retrieve it from Stage 2 separately;
      the evidence picture for the classification is split across two sections with no link
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

INHERITED FROM v3: C-14 (Pre-scoring mechanism placement): INHERITED
INHERITED FROM v4: C-15 (Stage 1 layer diversity warning): INHERITED
          C-16 (Evidence-grounded promotion citation): INHERITED
          C-17 (Source attribution table): INHERITED
          C-18 (Verdict classification rule citation): INHERITED
INHERITED FROM v5: C-19 (EG-first structural role ordering): INHERITED -- EG-FIRST
          EXECUTION CONSTRAINT + EG-RELAY COMPLETE gate; [enforcement: architectural]
          C-20 (Inertia registry with inheritance declaration): INHERITED -- this registry
          C-21 (Attribution table co-located in compliance ledger): INHERITED
INHERITED FROM v6: C-22 (Enforcement class annotation): INHERITED
          C-23 (Phase 2a/2b role membership enumerated): INHERITED
INHERITED FROM v7: C-24 (EG-FIRST block cites Coverage Matrix column): INHERITED
          C-25 (VC-4 G-1 count-check for PHASE 2a/2b MEMBERSHIP): INHERITED

INHERITED FROM v8 -- ASPIRATIONAL CRITERIA:
  C-26 (NEEDS-REDESIGN evidence anchor): INHERITED -- EVIDENCE ANCHOR enumerates EG IDs;
    count derived from list; forward linkage Step 3b -> Verdict
  C-27 (Promotion completeness gate): INHERITED -- arithmetic closure in SA-TO-SG PROMOTION;
    promoted + remaining = Stage 1 SA count; MISMATCH blocks Phase 2b

NEW IN v9 -- ASPIRATIONAL CRITERIA (R13 targets -- both):
  C-28 (Verdict-to-table traceability): NEW -- VERDICT-TO-TABLE TRACEABILITY sub-table +
    COUNT COMPLETENESS CHECK; each cited EG finding ID resolved to Step 3b row (Finding
    excerpt | Source | Severity); count-check confirms sub-table lists all Step 3b EG rows
    (not just a cherry-picked subset); fabricated IDs and selective citation both blocked
  C-29 (Promotion count forward-reference): NEW -- VERDICT EVIDENCE SUMMARY block; EG count
    (from EVIDENCE ANCHOR) and SA remaining (from PROMOTION COMPLETENESS GATE) co-located
    in Phase 5; both classification inputs present and structurally derived at verdict time
```

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check | Enforcement class |
|--------|---------|-------------|---------------|--------------|---------------|-------------------|
| Schema 1 -- Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b FLOOR CHECK, Step 3c G-3, Phase 4 | All EG-producing roles | VC-1 | instructional |
| Schema 2 -- Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, EG-RELAY COMPLETE, SA-TO-SG PROMOTION, Step 3b, all relays | All roles | VC-2 | instructional |
| Schema 3 -- Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 | instructional |
| Schema 4 -- Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source across all roles | VC-4 | architectural |
| Schema 5 -- Sub-Step Ordering | 3a -> 3b -> 3c -> 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 | architectural |

**Schema 1** `[enforcement: instructional]`: {P1, P2, P3}. Violations detectable in VC-1.
**Schema 2** `[enforcement: instructional]`: {SA, SG, EG, QO}. Label lock: promoted SA uses SG.
**Schema 3** `[enforcement: instructional]`: channel field required in every Phase 4 entry.
**Schema 4** `[enforcement: architectural]`: GATE CLEARANCE SUMMARY blocks Step 3d advancement.
**Schema 5** `[enforcement: architectural]`: named prerequisite gates each sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c |
| Step 3c | FLOOR CHECK PASS | Gate results all PASS | Step 3d |
| Step 3d | all-PASS gates | Channel taxonomy activated | Phase 4 |

---

### Phase 1 -- Setup: Role-Schema Binding Summary

Confirmed input bindings: [topic:], [scope_in:], [scope_out:], [roles:], [spec_version:]

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable, or "N/A"]
  Schema 2 binding: [Source labels; label lock rules if promoted gaps]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA], [SG original].

#### EG-FIRST EXECUTION CONSTRAINT

```
PHASE 2a MEMBERSHIP (EG-class roles -- must relay before SA-TO-SG PROMOTION):
  - [Role A] (EG-class: produces EG findings in Phase 2a relay)
  PHASE 2a role count: [N]

PHASE 2b MEMBERSHIP (SA/SG-class roles -- relay after SA-TO-SG PROMOTION):
  - [Role C] (SA/SG-class: SA/SG gaps only)
  PHASE 2b role count: [M]

Total roles: [N + M]

Structural invariant [enforcement: architectural -- see Coverage Matrix Schema 4 column]:
  SA-TO-SG PROMOTION BLOCKED until EG-RELAY COMPLETE PASS.
  EG-class roles run first. SA/SG-class roles run after promotion.
```

---

### Stage 1 -- Source-Layer Audit

A Stage 1 where all gaps cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}] [SG: {{sg_list}}] [EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Phase 2a -- EG-First Execution (PHASE 2a MEMBERSHIP roles only)

**EG-FIRST CONSTRAINT ACTIVE**: SA-TO-SG PROMOTION BLOCKED `[enforcement: architectural]`
until EG-RELAY COMPLETE PASS.

**Role relay -- [EG-producing role]**:
- Received from: | Received values: | Schema 2 compliance `[enforcement: instructional]`: Source labels used: [list] -- {SA,SG,EG,QO}: YES/NO
- SA/SG gaps: | Produced: | EG gaps: [EG-NN list or "none"]

> **EG-RELAY COMPLETE**: PHASE 2a declared: [N] | relayed: [N] | **PASS / FAIL**
> If FAIL: complete missing relay before SA-TO-SG PROMOTION.

---

### SA-TO-SG PROMOTION (requires EG-RELAY COMPLETE PASS)

```
SA-NN: [gap] | Promotion: PROMOTES TO SG-NN / REMAINS SA
Reason: [one sentence -- cite Phase 2a execution evidence if available]
```

```
[SA remaining: R] [SG from promotion: P] [SG original: O]
```

> **PROMOTION COMPLETENESS GATE**:
>
> | Stage 1 SA count | Promoted to SG | Remaining as SA | Completeness check |
> |-----------------|---------------|-----------------|-------------------|
> | [N] | [P] | [R] | P + R = N: PASS / MISMATCH |
>
> **SA remaining certified: R** -- forward-referenced in Phase 5 VERDICT EVIDENCE SUMMARY.
> If MISMATCH: Phase 2b BLOCKED. Reconcile before continuing.

Label lock `[enforcement: instructional]`: promoted gaps must use SG label downstream.

---

### Phase 2b -- SA/SG-Only Role Execution (after SA-TO-SG PROMOTION)

**Role relay -- [SA/SG role]**:
- Received from: | Values: | Schema 2 compliance: | SA/SG gaps: | Produced: | EG gaps: none

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
Sections written: [list each required section -- WRITTEN]

---

### Phase 3 -- Findings

#### Step 3a -- Severity Legend

| Label | Definition | Threshold |
|-------|-----------|-----------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Amend or follow-on |
| P3 | [advisory] | Log only |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

#### Step 3b -- Findings Table

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK**: IDs listed: [list all IDs] | count >= 3: Y/N |
> distinct Source types >= 2: Y/N | Action uniqueness: Y/N | **FLOOR CHECK: PASS/FAIL**
> If FAIL: add findings. Re-run after correction.

Schema 5 transition: FLOOR CHECK PASS. Step 3c valid.

#### Step 3c -- Enforcement Gates

**G-1** `[enforcement: architectural]`: >= 2 distinct Source types.
- Types present: [list] -- G-1: PASS/FAIL

**G-2** `[enforcement: architectural]`: No same-Source identical Actions.
- Pairs examined: [list or "none"] -- G-2: PASS/FAIL

**G-3** `[enforcement: architectural]`: All entries in {P1, P2, P3}.
- Labels present: [list] -- G-3: PASS/FAIL

> **GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS/FAIL | G-2: PASS/FAIL | G-3: PASS/FAIL
> ALL GATES CLEARED -- Step 3d valid. / GATE FAILURE -- Step 3d BLOCKED.

> **REMEDIATION LOG** (or "C-12 EXEMPTION APPLIES: all gates passed on first evaluation"):
> Gate [X] FAIL: reason / remediation action / re-check result

Schema 5 transition: ALL GATES CLEARED. Step 3d valid.

#### Step 3d -- Channel Taxonomy Activation

Channel taxonomy active `[enforcement: instructional]`. Phase 4 valid to begin.

---

### Phase 4 -- Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** `[enforcement: architectural]`:
> G-1: PASS | G-2: PASS | G-3: PASS -- Phase 4 valid to begin.

[Amend entries: finding / source / remediation channel / change or dismissal / source confirmed]

---

### Phase 5 -- Verdict

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must
name specific values, label lists, finding IDs, role names, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Legend declared | [legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b + FLOOR CHECK | P1/P2/P3 + FLOOR CHECK PASS | [labels; FLOOR CHECK result] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 + labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 | P1/P2/P3 in all entries | [severity values in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted=SG; COMPLETENESS GATE PASS | [gaps promoted; SG confirmed; gate result] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b | SA/SG/EG/QO; label lock | [Source labels; lock check] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy active | [activation evidence] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 | Channel in every entry | [channels per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 results | [all three results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 entry | PHASE 4 GATE CLEARANCE SUMMARY PASS | [gate summary result] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 -- C-21 CO-LOCATED ATTRIBUTION | G-1 verified; MEMBERSHIP counts | **G-1 SOURCE ATTRIBUTION TABLE**: Source/Phase/Role(s)/Finding IDs [per Source type; verify Phase 2a count = N from PHASE 2a MEMBERSHIP; Phase 2b count = M; mismatch = inconsistency] | PASS/FAIL |
| VC-5 | Schema 5 | 3a->3b | 3b after 3a | [3a completion] | PASS/FAIL |
| VC-5 | Schema 5 | 3b->3c | 3c after FLOOR CHECK | [FLOOR CHECK result] | PASS/FAIL |
| VC-5 | Schema 5 | 3c->3d | 3d after ALL GATES CLEARED | [gate clearance result] | PASS/FAIL |
| VC-5 | Schema 5 | 3d->Phase 4 | Phase 4 after channel taxonomy | [activation + PHASE 4 gate summary] | PASS/FAIL |

**VC-1**: PASS/FAIL | **VC-2**: PASS/FAIL | **VC-3**: PASS/FAIL | **VC-4**: PASS/FAIL | **VC-5**: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

> **NEEDS-REDESIGN EVIDENCE ANCHOR** (C-26: derives verdict from named finding IDs):
>
> NEEDS-SPEC-REVISION check:
> - P1 SA gaps remaining after promotion: [count -- list IDs if > 0]
> - Fires: YES / NO
>
> NEEDS-REDESIGN check:
> - EG findings in Step 3b: [list finding IDs explicitly, e.g., F-01, F-03, F-05]
> - EG count (derived from list): [N]
> - Threshold: 3 -- EG count > 3: YES / NO
> - Structural role gap indicated: YES (cite IDs) / NO
> - Fires: YES / NO
>
> **VERDICT-TO-TABLE TRACEABILITY** (C-28: each cited EG finding ID resolved to Step 3b row):
>
> | Cited ID | Step 3b Finding excerpt | Source | Severity |
> |----------|------------------------|--------|----------|
> | [F-NN] | [first 10 words of Finding cell] | EG | [P1/P2/P3] |
> | [F-MM] | [first 10 words of Finding cell] | EG | [P1/P2/P3] |
>
> **COUNT COMPLETENESS CHECK**: Step 3b EG rows (Source=EG count): [K] |
> Rows in TRACEABILITY sub-table above: [N from EVIDENCE ANCHOR list]
> K = N: COMPLETE / K != N: INCOMPLETE -- [K - N] Step 3b EG row(s) not cited in EVIDENCE ANCHOR.
> INCOMPLETE means the verdict omits Step 3b EG findings. Classification BLOCKED until
> all Step 3b EG rows appear in the TRACEABILITY sub-table.
>
> Traceability confirmed when: every cited ID resolves to a Step 3b row AND K = N.
>
> USEFUL: fires when neither NEEDS-SPEC-REVISION nor NEEDS-REDESIGN fires.

> **VERDICT EVIDENCE SUMMARY** (C-29: co-locates both classification inputs in Phase 5):
>
> | Evidence | Value | Source in this trace |
> |----------|-------|---------------------|
> | EG count | [N] | NEEDS-REDESIGN EVIDENCE ANCHOR list above |
> | SA remaining | [R] | PROMOTION COMPLETENESS GATE (Stage 2 SA-TO-SG PROMOTION) |
>
> Both values are structurally derived (EG: named list; SA: arithmetic closure).
> No re-read of prior phases required to verify the classification inputs.

**Trace result**:
`NEEDS-SPEC-REVISION` if NEEDS-SPEC-REVISION check fires.
`NEEDS-REDESIGN` if NEEDS-REDESIGN check fires.
`USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence; cite finding IDs from EVIDENCE ANCHOR and rule that fired]

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
