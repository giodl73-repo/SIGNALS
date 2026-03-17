I now have the full picture: the R2 variations used a different phase schema (Gather/Bind/Execute/Verdict) because the rubric was a clean-slate redesign. The current v3 rubric targets the **existing** trace-skill.t3 schema (Stages 1-2, Phases 1-4, Schema 1-5). R3 variations need to work with that schema, targeting the aspirational tier (C-09 through C-14).

---

# trace-skill — Variations R3 (2026-03-17)

**Skill**: `trace-skill`
**Rubric version**: v3 (C-01 through C-14)
**Entry state**: The current skill body (trace-skill.t3) satisfies C-01 through C-08 reliably. The aspirational tier (C-09 through C-14) is the scoring frontier. C-14 is new in v3 and has no prior round coverage. Rounds 1–2 used a different phase schema and cannot be carried forward.

**Variation axes selected** (3 single-axis, 2 combined):
- **V-01** — Lifecycle emphasis: explicit carry-forward summary blocks at every phase boundary + consolidated gate-clearance block before Phase 4. Targets C-10, C-11.
- **V-02** — Output format: named-artifact prerequisite checkboxes opening every Phase 3 sub-step. Targets C-13.
- **V-03** — Phrasing register: imperative HALT/REMEDIATE language at gate checks with structured remediation loop and C-12 exemption notice. Targets C-12, C-14.
- **V-04** — Combined (V-01 + V-02): lifecycle emphasis + prerequisite checkboxes. Targets C-10, C-11, C-13.
- **V-05** — All aspirationals: full integration of C-09 through C-14.

---

## V-01 — Single axis: Lifecycle emphasis (explicit boundary confirmations)

**Axis**: Lifecycle emphasis — every phase boundary is marked by an explicit carry-forward confirmation block that names what was produced and confirms the prerequisite for the next phase. The Schema 5 sub-step transitions are enforced with a two-sentence structure: (1) "Step Xa complete. Produced: [named output]." and (2) "Step Xb prerequisite satisfied. Step Xb is valid to begin." A consolidated Gate-Clearance Summary block appears between Step 3c and Step 3d, naming all three gates and their final results. No phase may begin without its preceding carry-forward block.

**Hypothesis**: The baseline skill has Schema 5 prerequisites written inline as part of phase descriptions, which a model can satisfy by inserting the prerequisite text without actually completing the prior step's output. Making each boundary an explicit two-sentence confirmation — naming the output produced, not just the step label — forces the model to produce the output before writing the confirmation. The consolidated Gate-Clearance Summary (C-11) becomes impossible to skip because it is a required structural block between 3c and 3d, not an optional summary. Risk: the confirmation blocks add overhead per sub-step; a model may write mechanical confirmations without the actual output, satisfying the letter of C-10/C-11 while missing C-13.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol authority: every label, channel, and gate used in any downstream phase must be declared in this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (Source label in each relay; promoted gaps use SG) | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to Phase 4 amendments drawn from all roles' findings | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source column coverage across all roles' Step 3b findings | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (enforce transitions between all sub-steps) | N/A | VC-5 |

**Schema 1 — Severity Vocabulary**: Valid severity labels: P1, P2, P3 only. P1 = blocks artifact from being useful. P2 = quality improvement that does not block. P3 = advisory observation.

**Schema 2 — Gap Type Taxonomy**: Valid Source labels: SA (spec-layer gap), SG (setup gap), EG (execute gap), QO (quality observation). SA-TO-SG label lock invariant: a promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION.

**Schema 3 — Remediation Channel Taxonomy**: Valid channels: spec, invocation, artifact, quality. Every Phase 4 Amend entry must name one channel.

**Schema 4 — Enforcement Gate Registry**: G-1: Step 3b contains >=2 distinct Source types. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. All three must hold before Phase 4 begins.

**Schema 5 — Sub-Step Ordering**:

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's EG findings, or "N/A"] | [Source labels this role may produce; label lock rules for promoted gaps] | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Read only `{{skill_spec_path}}`. Examine all three source layers (SA, SG, EG). A Stage 1 where all gaps cluster at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 — Hand-Compilation

Stage 2 receives the relay: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

All gaps carry forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION

Every SA gap in the Stage 1 relay is evaluated here. A gap a spec-competent invoker can supply at runtime promotes to SG. A gap requiring a spec change remains SA.

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

Post-promotion inventory:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

**STAGE 1 → PHASE 1 CARRY-FORWARD CONFIRMED**
- Produced: Stage 1 gap audit table + relay record + SA-TO-SG PROMOTION entries
- SA remaining count: `{{sa_remaining}}`
- SG total (original + promoted): `{{sg_total}}`
- Layer diversity: `{{diversity_status}}`
- Phase 1 prerequisite: Stage 1 complete and relay produced. Phase 1 is valid to begin.

---

#### Phase 1 — Setup

Confirmed input bindings for all declared inputs, and a per-role schema binding and gap attribution block for each role in the execution sequence.

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
  Schema 1 binding: [severity labels applicable, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock if promoted]
  SA/SG gaps binding this role: [list or "none — confirmed"]
  EG gaps expected for this role: [list or "none — confirmed"]
```

**PHASE 1 → PHASE 2 CARRY-FORWARD CONFIRMED**
- Produced: confirmed input bindings + per-role schema binding blocks for all roles
- Roles in execution sequence: `{{roles}}`
- SA remaining: `{{sa_remaining}}` | SG total: `{{sg_total}}`
- Phase 2 prerequisite: Phase 1 complete and all roles have schema binding blocks. Phase 2 is valid to begin.

---

#### Phase 2 — Execute

Produces the hand-compiled artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md` and a per-role relay for each role.

A role relay without the "Schema 2 compliance" field is structurally invalid.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none — confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**PHASE 2 → PHASE 3 CARRY-FORWARD CONFIRMED**
- Produced: hand-compiled artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md` + per-role relays for all roles
- EG gaps added during execute: `{{eg_new}}`
- Artifact sections written: [count] of [required count] per spec
- Phase 3 prerequisite: Phase 2 complete and artifact produced. Phase 3 is valid to begin.

---

#### Phase 3 — Findings

Phase 3 sub-steps run in the order declared by Schema 5. Each sub-step produces a named output and issues an explicit carry-forward confirmation before the next sub-step begins.

---

##### Step 3a — Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.
Schema 5 prerequisite satisfied: YES — see Coverage Matrix above, Schema 1 row declares {P1, P2, P3}.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

**STEP 3a COMPLETE. Produced: severity legend (P1/P2/P3 definitions above).**
**Step 3b prerequisite satisfied: severity legend produced at Step 3a. Step 3b is valid to begin.**

---

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a complete — severity legend produced (confirmed above).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

A valid findings table uses only Source labels from Schema 2 (promoted gaps use SG) and Severity labels from the Step 3a legend. Minimum 2 entries, covering at least 2 distinct Source types.

**STEP 3b COMPLETE. Produced: findings table with [N] entries covering [M] distinct Source types.**
**Step 3c prerequisite satisfied: findings table populated with >=2 entries. Step 3c is valid to begin.**

---

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b populated — findings table complete (confirmed above).

**G-1 Invariant**: Step 3b contains >=2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL
- If FAIL: structural defect. Identify missing source layer. Add finding. Re-check G-1.

**G-2 Invariant**: No two same-Source findings carry identical Action text.
- Same-Source pairs examined: [list or "none — all Source types unique"]
- G-2: PASS / FAIL
- If FAIL: structural defect. Revise Action text to name distinct targets. Re-check G-2.

**G-3 Invariant**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL
- If FAIL: structural defect. Relabel non-conforming entries. Re-check G-3.

**STEP 3c COMPLETE. Produced: G-1 = [PASS/FAIL], G-2 = [PASS/FAIL], G-3 = [PASS/FAIL].**

---

**GATE-CLEARANCE SUMMARY — Phase 4 Entry**

> This block is required. It consolidates the three gate results for Phase 4 admission. A gate that failed and was remediated is recorded with its final (post-remediation) result here, not its initial result.

| Gate | Final Result | Note |
|------|-------------|------|
| G-1 | PASS / FAIL | [state what satisfied or violated it] |
| G-2 | PASS / FAIL | |
| G-3 | PASS / FAIL | |

**Phase 4 entry: AUTHORIZED** (G-1 = PASS AND G-2 = PASS AND G-3 = PASS)
— or —
**Phase 4 entry: BLOCKED** (gate(s) in FAIL — return to Step 3c, remediate, and re-issue this block)

**Step 3d prerequisite: all gates PASS in Gate-Clearance Summary above. Step 3d is valid to begin.**

---

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS — confirmed in Gate-Clearance Summary above.

Schema 3 channel taxonomy is now active for Phase 4: spec / invocation / artifact / quality. Every Phase 4 Amend entry must include `[remediation channel: ...]`.

**STEP 3d COMPLETE. Produced: Schema 3 channel taxonomy activated.**
**Phase 4 prerequisite: Step 3d complete and channel taxonomy active. Phase 4 is valid to begin.**

---

**PHASE 3 → PHASE 4 CARRY-FORWARD CONFIRMED**
- Produced: severity legend (Step 3a) + findings table (Step 3b) + gate results (Step 3c) + channel taxonomy activation (Step 3d)
- Highest finding: `{{F-NN}}` / Source: `{{source}}`
- Gate-Clearance Summary: G-1 = `{{PASS}}`, G-2 = `{{PASS}}`, G-3 = `{{PASS}}`
- Channel taxonomy: active from Step 3d

---

#### Phase 4 — Amend

Phase 4 is authorized only when the Gate-Clearance Summary above records G-1 = PASS, G-2 = PASS, G-3 = PASS. If any gate is FAIL, return to Step 3c.

A valid Amend entry (change):
- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (Schema 2 label lock: promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO]

A valid Amend entry (dismissal):
- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 — Compliance Ledger)

The Verdict audits every usage site and role binding declared in the Coverage Matrix. A Verdict row with "Observed behavior: as expected" is structurally invalid — the Observed behavior cell must name specific values, labels, role names, or invariant status observed.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions | [state actual definitions written at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use {P1, P2, P3} | [list severity values used; count each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use {P1, P2, P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay — [role name] | EG findings from this role use {P1,P2,P3} | [list severity labels used by this role's EG findings] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used in audit table | [list all Source labels used in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG label; label lock holds | [list SA gaps promoted; confirm SG label in downstream references] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [list Source labels in Step 3b; identify promoted gaps] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay — [role name] | Source labels from {SA,SG,EG,QO}; label lock honored | [list Source labels used by this role; confirm label lock] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state the Step 3d activation language used] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every Amend entry includes channel field | [list channels used in each Amend entry; flag missing fields] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked with explicit PASS/FAIL | [state G-1/G-2/G-3 results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Gate-Clearance Summary shows all-PASS before Phase 4 | [state Gate-Clearance Summary results; confirm Phase 4 authorized] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1) | >=2 distinct Source types across all roles | [list Source types present and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 | 3a → 3b | Step 3b valid only after Step 3a legend produced | [state the carry-forward confirmation text that preceded Step 3b] | PASS / FAIL |
| VC-5 | Schema 5 | 3b → 3c | Step 3c valid only after Step 3b has >=2 findings | [state entry count confirmed in Step 3b carry-forward] | PASS / FAIL |
| VC-5 | Schema 5 | 3c → 3d | Step 3d valid only after Gate-Clearance Summary all-PASS | [state Gate-Clearance Summary results before Step 3d began] | PASS / FAIL |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 valid only after Step 3d activated channel taxonomy | [state Step 3d activation confirmation before Phase 4] | PASS / FAIL |

**VC-1 overall**: PASS / FAIL
**VC-2 overall**: PASS / FAIL
**VC-3 overall**: PASS / FAIL
**VC-4 overall**: PASS / FAIL
**VC-5 overall**: PASS / FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 — Single axis: Output format (named-artifact prerequisite checkboxes)

**Axis**: Output format — every Phase 3 sub-step opens with a structured prerequisite verification block before any content is produced. The block states the required condition, names the specific artifact or table row that satisfies it, and declares YES or NO. A bare YES without a named referent is not accepted. If NO, the sub-step does not begin — return to the preceding step. This replaces the inline transition-sentence approach of the baseline with an explicit two-field check that C-13 requires.

**Hypothesis**: The baseline has Schema 5 prerequisite sentences woven into sub-step descriptions ("Schema 5 prerequisite: Step 3a complete..."). A model satisfying C-10 by writing those sentences may still skip the actual named-artifact check that C-13 requires, because the baseline doesn't enforce *what evidence* confirms the prerequisite — only that the prerequisite is stated. Adding a structured checkbox block with a named-referent field makes C-13 structural: if the model can't name the artifact, the YES is invalid by definition. Risk: the checkbox block may become mechanical fill-in-the-blank if the model treats the "Evidence" field as a label slot rather than a real reference.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol authority.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 cross-role aggregate | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A | VC-5 |

**Schema 1**: P1 = blocks artifact. P2 = quality improvement. P3 = advisory.
**Schema 2**: SA = spec-layer gap. SG = setup gap. EG = execute gap. QO = quality observation. Label lock: promoted SA gaps use SG label in all downstream phases.
**Schema 3**: Channels: spec / invocation / artifact / quality. Every Phase 4 Amend entry must declare one.
**Schema 4**: G-1 (>=2 distinct Source types in Step 3b), G-2 (no same-Source duplicated Action), G-3 (all Step 3b entries use {P1,P2,P3}). All three must PASS before Phase 4.
**Schema 5**: Sub-step ordering contract (see table above).

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all-PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels for this role's EG findings, or "N/A"] | [Source labels; label lock if promoted] | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Read only `{{skill_spec_path}}`. Examine all three source layers. A Stage 1 clustering all gaps at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 — Hand-Compilation

Stage 2 receives the relay. All gaps carry forward.

---

#### SA-TO-SG PROMOTION

Every SA gap evaluated:

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

Post-promotion:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

---

#### Phase 1 — Setup

Confirmed input bindings:
- [topic: ] | [scope_in: ] | [scope_out: ] | [roles: ] | [stack: ] | [spec_version: ]

Per-role schema binding:

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels, or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none — confirmed"]
  EG gaps expected: [list or "none — confirmed"]
```

Setup carry-forward: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

Produce the hand-compiled artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md`. Per-role relay (Schema 2 compliance field required):

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none — confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Execute carry-forward: [artifact path], [EG added].

---

#### Phase 3 — Findings

Each sub-step opens with a PREREQUISITE CHECK block. The block has three fields: Condition, Evidence, and Status. A Status of YES without a named Evidence referent is not accepted — it is treated as an incomplete check.

---

##### Step 3a — Severity Legend Declaration

```
PREREQUISITE CHECK — Step 3a
Condition:  Schema 1 (Severity Vocabulary) is declared in the Coverage Matrix above.
Evidence:   [name the Coverage Matrix row: "Schema 1 — Severity Vocabulary row, Coverage Matrix above, declaring {P1, P2, P3}"]
Status:     YES — Step 3a is valid to begin.
            (If NO: Schema 1 not found in Coverage Matrix. Return to Coverage Matrix and declare it before proceeding.)
```

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Produced: severity legend (table above). Step 3b is valid to begin.

---

##### Step 3b — Findings Table

```
PREREQUISITE CHECK — Step 3b
Condition:  Step 3a has produced a severity legend for this trace.
Evidence:   [name the legend: "Step 3a severity legend table above, row P1: [actual P1 definition], row P2: [actual P2 definition], row P3: [actual P3 definition]"]
Status:     YES — Step 3b is valid to begin.
            (If NO: Step 3a legend not found above. Return to Step 3a and produce it before proceeding.)
```

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Source labels from Schema 2 only. Severity from Step 3a legend only. Minimum 2 entries.

Schema 5 transition: Step 3b complete. Produced: findings table with [N] entries. Step 3c is valid to begin.

---

##### Step 3c — Enforcement Gates

```
PREREQUISITE CHECK — Step 3c
Condition:  Step 3b has produced a findings table with >=2 entries.
Evidence:   [name the table: "Step 3b findings table above; row count: [N]; rows: F-01 ([Source]), F-02 ([Source]), ..."]
Status:     YES — Step 3c is valid to begin.
            (If NO: findings table has <2 entries. Return to Step 3b and add findings before proceeding.)
```

**G-1**: Source types in Step 3b: [list]. G-1: PASS / FAIL.
If FAIL: identify missing source layer, add finding to Step 3b, re-check G-1.

**G-2**: Same-Source pairs: [list or "none"]. G-2: PASS / FAIL.
If FAIL: revise Action text for duplicates, re-check G-2.

**G-3**: Severity labels in Step 3b: [list]. G-3: PASS / FAIL.
If FAIL: relabel non-conforming entries, re-check G-3.

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

---

##### Step 3d — Channel Taxonomy Activation

```
PREREQUISITE CHECK — Step 3d
Condition:  Step 3c has produced PASS results for all three gates (G-1, G-2, G-3).
Evidence:   [name the gate results: "Step 3c above: G-1 = [result], G-2 = [result], G-3 = [result]"]
Status:     YES — Step 3d is valid to begin.
            (If NO: one or more gates are FAIL. Return to Step 3c, remediate, and re-issue gate results before proceeding.)
```

Schema 3 channel taxonomy is now active: spec / invocation / artifact / quality. Every Phase 4 Amend entry must include `[remediation channel: ...]`.

Schema 5 transition: Step 3d complete. Channel taxonomy active. Phase 4 is valid to begin.

---

Findings carry-forward: [highest finding], [source], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 — Amend

```
PREREQUISITE CHECK — Phase 4
Condition:  Step 3d has activated the Schema 3 channel taxonomy (G-1, G-2, G-3 all PASS).
Evidence:   [name the activation: "Step 3d above: channel taxonomy activated; Gate results: G-1=[result], G-2=[result], G-3=[result]"]
Status:     YES — Phase 4 is valid to begin.
            (If NO: Return to Step 3d. Confirm all gates PASS before producing Amend entries.)
```

A valid Amend entry (change): [finding: F-NN], [source: schema-2-label], [remediation channel: schema-3-channel], [section or field changed], [change], [source confirmed: YES/NO].

A valid Amend entry (dismissal): [finding: F-NN], [reason], [remediation channel: schema-3-channel], [source type confirmed: YES/NO].

---

### Verdict (Phase 5 — Compliance Ledger)

A Verdict row with "Observed behavior: as expected" is structurally invalid — name specific values, labels, or invariant results.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend declared: P1/P2/P3 definitions | [state actual P1/P2/P3 definitions written] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use {P1, P2, P3} | [list severity values used; count each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use {P1, P2, P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay — [name] | EG findings use {P1,P2,P3} | [list labels used by this role's EG findings] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used | [list Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG label | [list promoted gaps; confirm SG label downstream] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | {SA,SG,EG,QO}; promoted show SG | [list Source labels in Step 3b; identify promoted] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay — [name] | Source labels from schema; label lock honored | [list labels used; confirm promoted gaps] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state the Step 3d checkbox Evidence field text] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [list channels per entry; flag missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked | [state results at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered with all-PASS | [state Phase 4 prerequisite check Evidence text] | PASS / FAIL |
| VC-4 | Schema 4 | G-1 cross-role | >=2 Source types across all roles | [list Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 | 3a → 3b | Step 3b prerequisite check passed | [state Step 3b Evidence field contents] | PASS / FAIL |
| VC-5 | Schema 5 | 3b → 3c | Step 3c prerequisite check passed | [state Step 3c Evidence field: entry count named] | PASS / FAIL |
| VC-5 | Schema 5 | 3c → 3d | Step 3d prerequisite check passed | [state Step 3d Evidence field: gate results named] | PASS / FAIL |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 prerequisite check passed | [state Phase 4 Evidence field: activation named] | PASS / FAIL |

**VC overall**: VC-1: PASS/FAIL | VC-2: PASS/FAIL | VC-3: PASS/FAIL | VC-4: PASS/FAIL | VC-5: PASS/FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 — Single axis: Phrasing register (imperative HALT/REMEDIATE with loop template)

**Axis**: Phrasing register — gate checks use imperative HALT language when a violation is detected. A FAIL at any gate triggers a structured REMEDIATION LOOP with three mandatory fields: (1) the specific action taken, (2) a re-check of the gate, and (3) the updated result. When all gates pass on first evaluation, the trace emits an explicit **C-12 EXEMPTION NOTICE** confirming that the loop is exempt — it does not silently skip the loop. A post-remediation **C-14 COHERENCE CHECK** confirms that the Phase 4 entry summary reflects the post-remediation gate states, not the initial evaluation states.

**Hypothesis**: The baseline skill tells the tracer to correct structural defects and re-check, but does not provide a loop template. A tracer can satisfy this instruction by adding a finding and immediately proceeding, without re-issuing the gate result — creating a silent FAIL-to-PASS transition that satisfies the letter of the instruction without the auditable trail C-12 requires. The explicit loop template forces the model to (1) state the action, (2) rerun the gate, and (3) write the new result, making the transition visible. The C-12 EXEMPTION NOTICE closes the alternative path where silence means "no loop needed" — silence is no longer valid; either a loop ran or an exemption was declared. C-14 coherence check prevents the Phase 4 summary from reverting to initial states. Risk: the HALT framing may cause the model to over-apply the loop to passing gates; the exemption notice mitigates this by providing a clean exit when no loop is needed.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, role relays | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 cross-role aggregate | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 | N/A | VC-5 |

**Schema 1**: P1 = blocks artifact. P2 = quality improvement. P3 = advisory.
**Schema 2**: SA / SG / EG / QO. Label lock: promoted SA gaps use SG in all downstream phases.
**Schema 3**: Channels: spec / invocation / artifact / quality. Required on every Phase 4 entry.
**Schema 4**: G-1 (>=2 Source types in Step 3b), G-2 (no same-Source duplicate Actions), G-3 (all Step 3b entries use {P1,P2,P3}). All three PASS required before Phase 4.
**Schema 5**: Ordering contract enforced per sub-step.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table >=2 entries | Step 3c |
| Step 3c | Step 3b populated | Gate results all-PASS | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock if promoted] | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Read only `{{skill_spec_path}}`. Examine all three source layers. A Stage 1 with all gaps at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay:

```
[SA: {{sa_list}}]  [SG: {{sg_list}}]  [EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 — Hand-Compilation

Receives relay. All gaps carry forward.

---

#### SA-TO-SG PROMOTION

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

Post-promotion: [SA remaining: N] [SG from promotion: N] [SG original: N]

---

#### Phase 1 — Setup

Input bindings: [topic], [scope_in], [scope_out], [roles], [stack/detection], [spec_version].

Per-role schema binding:

```
[role: name]
  Schema 1 binding: [labels or "N/A"]
  Schema 2 binding: [Source labels; label lock]
  SA/SG gaps: [list or "none — confirmed"]
  EG gaps expected: [list or "none — confirmed"]
```

Setup carry-forward: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

Produce `simulations/trace/skill/{topic}-skill-trace-{date}.md`. Per-role relay:

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value]
- Schema 2 compliance: Source labels used: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps: [list or "none — confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Execute carry-forward: [artifact path], [EG added].

---

#### Phase 3 — Findings

Sub-steps run in Schema 5 order. Each gate check uses HALT language on violation. When all gates pass on first evaluation, emit the C-12 EXEMPTION NOTICE.

---

##### Step 3a — Severity Legend

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix above. Satisfied.

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality improvement] | Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a severity legend above. Satisfied.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. Source labels from Schema 2. Severity from Step 3a legend.

Schema 5 transition: Step 3b complete. Step 3c is valid to begin.

---

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b findings table above, >=2 entries. Satisfied.

**G-1 Check**: Source types in Step 3b: [list]

> **If >=2 distinct Source types present**: G-1 = PASS. Continue to G-2.
>
> **HALT — G-1 VIOLATED**: fewer than 2 Source types detected.
> ```
> C-12 REMEDIATION LOOP — G-1:
> 1. Action:    [name the missing source layer; add a finding from that layer to Step 3b]
> 2. Re-check:  Source types in Step 3b after addition: [updated list]
> 3. G-1 after remediation: PASS / FAIL
> ```
> If G-1 remains FAIL after loop: trace is structurally blocked. State what spec change or additional execution would surface the missing source.

**G-1: PASS** (confirmed above, [initial evaluation / after C-12 remediation loop])

**G-2 Check**: Same-Source pairs with identical Action: [list or "none"]

> **If no duplicates found**: G-2 = PASS. Continue to G-3.
>
> **HALT — G-2 VIOLATED**: duplicate Action text detected for same-Source findings.
> ```
> C-12 REMEDIATION LOOP — G-2:
> 1. Action:    [identify the duplicate pair; revise Action text for one or both to name distinct targets]
> 2. Re-check:  Action text in revised Step 3b: [confirm no two same-Source entries share identical Action]
> 3. G-2 after remediation: PASS / FAIL
> ```

**G-2: PASS** (confirmed above)

**G-3 Check**: Severity labels in Step 3b: [list]

> **If all labels in {P1, P2, P3}**: G-3 = PASS. Continue.
>
> **HALT — G-3 VIOLATED**: non-conforming severity label detected.
> ```
> C-12 REMEDIATION LOOP — G-3:
> 1. Action:    [identify the non-conforming label; relabel the entry using P1, P2, or P3]
> 2. Re-check:  Severity labels in revised Step 3b: [updated list]
> 3. G-3 after remediation: PASS / FAIL
> ```

**G-3: PASS** (confirmed above)

---

> **C-12 EXEMPTION NOTICE** (emit this block when no gate triggered a remediation loop):
> All three gates (G-1, G-2, G-3) passed on first evaluation. No C-12 remediation loop was required. C-12 exemption applies to this trace.
>
> *(If any loop ran above, delete this block — C-12 is not exempt.)*

---

**C-14 COHERENCE CHECK — Phase 4 Entry**

> This block is required when any C-12 remediation loop ran. When C-12 is exempt, emit: "C-14 exempt — no remediation loop ran; initial gate states are final states."

Initial gate evaluation: G-1 = [initial], G-2 = [initial], G-3 = [initial]
Post-remediation states (if any loops ran): G-1 = [final], G-2 = [final], G-3 = [final]
Phase 4 entry summary reflects: **post-remediation states** (C-14 satisfied) / **initial states** (C-14 violated — update summary to reflect final states)

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS (final states). Step 3d is valid.

---

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS (G-1, G-2, G-3 final states above). Satisfied.

Schema 3 channel taxonomy active: spec / invocation / artifact / quality. Every Phase 4 entry requires `[remediation channel: ...]`.

Schema 5 transition: Step 3d complete. Phase 4 is valid to begin.

---

Findings carry-forward: [highest finding], [source], G-1=PASS, G-2=PASS, G-3=PASS (final), channel taxonomy active.

---

#### Phase 4 — Amend

Pre-check: G-1 = PASS, G-2 = PASS, G-3 = PASS (final states from C-14 Coherence Check above). Phase 4 authorized.

*If any gate is FAIL in the C-14 block: HALT. Return to Step 3c. Remediate and re-run C-14 Coherence Check before producing any Amend entries.*

Amend entry (change): [finding], [source (Schema 2)], [remediation channel (Schema 3)], [section changed], [change], [source confirmed].

Amend entry (dismissal): [finding], [reason], [remediation channel (Schema 3)], [source confirmed].

---

### Verdict (Phase 5 — Compliance Ledger)

"Observed behavior: as expected" is structurally invalid. Name specific values.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [state actual P1/P2/P3 definitions written at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use {P1,P2,P3} | [list severity values used; count each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All entries use {P1,P2,P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay — [name] | EG findings use {P1,P2,P3} | [list labels from this role's EG findings] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used | [list Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG | [list promoted gaps; confirm SG downstream] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | {SA,SG,EG,QO}; promoted show SG | [list Source labels; confirm promoted] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay — [name] | Source labels schema-conformant | [list labels used by this role] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state Step 3d activation language] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [list channels per entry; flag missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked | [state initial results; note any remediation loop] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered on all-PASS final states | [state C-14 Coherence Check final states] | PASS / FAIL |
| VC-4 | Schema 4 | G-1 cross-role | >=2 Source types across roles | [list Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 | 3a → 3b | Step 3b began after Step 3a complete | [state Schema 5 transition sentence at Step 3a] | PASS / FAIL |
| VC-5 | Schema 5 | 3b → 3c | Step 3c began after Step 3b >=2 entries | [state Schema 5 transition sentence at Step 3b] | PASS / FAIL |
| VC-5 | Schema 5 | 3c → 3d | Step 3d began after all-PASS | [state Schema 5 transition condition and C-14 final states] | PASS / FAIL |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 began after channel taxonomy active | [state Step 3d Schema 5 transition sentence] | PASS / FAIL |

**VC overall**: VC-1: PASS/FAIL | VC-2: PASS/FAIL | VC-3: PASS/FAIL | VC-4: PASS/FAIL | VC-5: PASS/FAIL

**SA remaining**: [N] | **SG total**: [N] | **EG total**: [N]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 — Combined: Lifecycle emphasis + prerequisite checkboxes (V-01 + V-02)

**Axis**: Combined — V-01 carry-forward blocks at every phase boundary (C-10, C-11) combined with V-02 named-artifact prerequisite checkboxes at every sub-step entry (C-13). Each sub-step has both: an opening PREREQUISITE CHECK block (with named Evidence) and a closing CARRY-FORWARD CONFIRMED block (naming what was produced). The Gate-Clearance Summary from V-01 remains, and the prerequisite checkboxes from V-02 replace the inline prerequisite sentences.

**Hypothesis**: V-01 addresses the phase-boundary confirmation problem (C-10, C-11) but leaves C-13 unaddressed — a model can write carry-forward summaries without opening checkboxes. V-02 addresses C-13 but leaves C-10/C-11 as inline sentences. The combined variation makes all three criteria structural: each sub-step must both open with a named-artifact check AND close with a named-output confirmation. A model that satisfies both for every sub-step has necessarily produced the output and traced the evidence chain. The Gate-Clearance Summary between 3c and 3d ensures C-11 is a distinct block, not folded into a generic carry-forward. Risk: the dual-block structure adds overhead; a model may write both blocks mechanically with generic text, satisfying the format without the substance. The named-artifact requirement in the Evidence field provides the quality gate.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG, Step 3b, relays | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 cross-role | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 | N/A | VC-5 |

**Schema 1**: P1 (blocker), P2 (quality improvement), P3 (advisory). No other labels valid.
**Schema 2**: SA / SG / EG / QO. Label lock invariant: promoted SA gaps use SG in all downstream phases.
**Schema 3**: spec / invocation / artifact / quality. Every Phase 4 Amend entry must declare one channel.
**Schema 4**: G-1 (>=2 Source types), G-2 (no duplicate Actions per Source), G-3 (all {P1,P2,P3}). All-PASS required before Phase 4.
**Schema 5**: ordering contract — 3a → 3b → 3c → 3d.

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a complete | Findings table >=2 entries | Step 3c |
| Step 3c | Step 3b populated | Gate results all-PASS | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role] | [severity labels or "N/A"] | [Source labels; label lock] | [Schema 3/4] |

---

### Stage 1 — Source-Layer Audit

Read `{{skill_spec_path}}` only. All three source layers must be examined.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay: [SA: N], [SG: N], [EG: N], [layer diversity: PASS/FAIL]

---

### Stage 2 — Hand-Compilation

---

#### SA-TO-SG PROMOTION

```
SA-NN: Gap: [text]  Promotion: PROMOTES TO SG / REMAINS SA  Reason: [sentence]
```

Post-promotion: [SA remaining: N] [SG from promotion: N] [SG original: N]

**STAGE 1 → PHASE 1 CARRY-FORWARD CONFIRMED**
Produced: gap audit table + relay + SA-TO-SG PROMOTION entries.
SA remaining: N | SG total: N | Layer diversity: [status].
Phase 1 prerequisite satisfied: Stage 1 relay produced above. Phase 1 is valid to begin.

---

#### Phase 1 — Setup

Input bindings: [topic], [scope_in], [scope_out], [roles], [stack], [spec_version].

Per-role schema binding:
```
[role: name]
  Schema 1: [labels or "N/A"]  Schema 2: [labels; lock]
  SA/SG gaps: [list or "none — confirmed"]  EG expected: [list or "none — confirmed"]
```

**PHASE 1 → PHASE 2 CARRY-FORWARD CONFIRMED**
Produced: input bindings + per-role schema binding blocks for [N] roles.
Roles: [list]. SA remaining: N | SG total: N.
Phase 2 prerequisite satisfied: all roles have schema binding declarations. Phase 2 is valid to begin.

---

#### Phase 2 — Execute

Produce artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md`. Per-role relay required.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value]
- Schema 2 compliance: Source labels used: [list] — all {SA,SG,EG,QO}: YES / NO
- SA/SG gaps: [list or "none — confirmed"]
- Produced: [artifact content]
- EG gaps: [list or "none"]

**PHASE 2 → PHASE 3 CARRY-FORWARD CONFIRMED**
Produced: artifact at [path] + per-role relays for [N] roles.
EG gaps added: [list or "none"]. Artifact sections: [N] of [required N].
Phase 3 prerequisite satisfied: artifact produced and relays complete. Phase 3 is valid to begin.

---

#### Phase 3 — Findings

Each sub-step opens with a PREREQUISITE CHECK (named Evidence required) and closes with a CARRY-FORWARD CONFIRMED block. Both are required. A sub-step without either block is structurally incomplete.

---

##### Step 3a — Severity Legend

```
PREREQUISITE CHECK — Step 3a
Condition:  Schema 1 declared in Coverage Matrix.
Evidence:   [cite the Coverage Matrix Schema 1 row: "Schema 1 row above declares {P1, P2, P3}"]
Status:     YES — proceed.  |  NO — return to Coverage Matrix.
```

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker definition for this trace] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend |
| P3 | [advisory definition] | Log; no gate impact |

```
CARRY-FORWARD CONFIRMED — Step 3a
Produced: severity legend above (P1: [definition summary], P2: [summary], P3: [summary]).
Step 3b prerequisite: Step 3a severity legend named above. Step 3b is valid to begin.
```

---

##### Step 3b — Findings Table

```
PREREQUISITE CHECK — Step 3b
Condition:  Step 3a has produced a severity legend.
Evidence:   [cite the Step 3a legend: "Step 3a table above, row P1: [actual text], row P2: [actual text], row P3: [actual text]"]
Status:     YES — proceed.  |  NO — return to Step 3a.
```

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Source labels from Schema 2. Severity from Step 3a legend. Minimum 2 entries, >=2 Source types.

```
CARRY-FORWARD CONFIRMED — Step 3b
Produced: findings table with [N] entries; Source types: [list]; Severity labels used: [list].
Step 3c prerequisite: Step 3b table has [N] entries (>=2 confirmed). Step 3c is valid to begin.
```

---

##### Step 3c — Enforcement Gates

```
PREREQUISITE CHECK — Step 3c
Condition:  Step 3b findings table has >=2 entries.
Evidence:   [cite Step 3b table: "Step 3b CARRY-FORWARD confirms [N] entries: F-01 ([Source]), F-02 ([Source]), ..."]
Status:     YES — proceed.  |  NO — return to Step 3b.
```

**G-1**: Source types present: [list]. Count: [N]. G-1: PASS (>=2) / FAIL (<2).
If FAIL: add finding from missing source layer; re-check G-1. Updated G-1: [result].

**G-2**: Same-Source duplicate Actions: [list or "none"]. G-2: PASS / FAIL.
If FAIL: revise Action text; re-check G-2. Updated G-2: [result].

**G-3**: Severity labels in Step 3b: [list]. G-3: PASS (all in {P1,P2,P3}) / FAIL.
If FAIL: relabel non-conforming entries; re-check G-3. Updated G-3: [result].

---

**GATE-CLEARANCE SUMMARY — Phase 4 Entry**

> Required block. Records final (post-remediation) gate states. This summary is what Phase 4 reads — not the initial evaluation results above.

| Gate | Initial result | Remediation | Final result |
|------|---------------|-------------|-------------|
| G-1 | [initial] | [action taken, or "none"] | [final] |
| G-2 | [initial] | [action taken, or "none"] | [final] |
| G-3 | [initial] | [action taken, or "none"] | [final] |

**Phase 4 entry: AUTHORIZED** (G-1=PASS, G-2=PASS, G-3=PASS final) / **BLOCKED** (return to Step 3c)

```
CARRY-FORWARD CONFIRMED — Step 3c
Produced: Gate-Clearance Summary above — G-1=[final], G-2=[final], G-3=[final].
Step 3d prerequisite: Gate-Clearance Summary all-PASS confirmed. Step 3d is valid to begin.
```

---

##### Step 3d — Channel Taxonomy Activation

```
PREREQUISITE CHECK — Step 3d
Condition:  Gate-Clearance Summary records G-1=PASS, G-2=PASS, G-3=PASS.
Evidence:   [cite the Gate-Clearance Summary: "Gate-Clearance Summary above: G-1=[final], G-2=[final], G-3=[final], Phase 4 AUTHORIZED"]
Status:     YES — proceed.  |  NO — return to Step 3c.
```

Schema 3 channel taxonomy active: spec / invocation / artifact / quality. All Phase 4 entries must include `[remediation channel: ...]`.

```
CARRY-FORWARD CONFIRMED — Step 3d
Produced: Schema 3 channel taxonomy activated.
Phase 4 prerequisite: Step 3d activation confirmed above. Phase 4 is valid to begin.
```

---

**PHASE 3 → PHASE 4 CARRY-FORWARD CONFIRMED**
Produced: severity legend (3a) + findings table [N entries, M Source types] (3b) + gate results (3c, final: G-1=PASS, G-2=PASS, G-3=PASS) + channel taxonomy activation (3d).
Highest finding: [F-NN / Source / Severity]. Phase 4 prerequisite: all above confirmed.

---

#### Phase 4 — Amend

```
PREREQUISITE CHECK — Phase 4
Condition:  Step 3d has activated channel taxonomy; Gate-Clearance Summary all-PASS.
Evidence:   [cite Step 3d CARRY-FORWARD: "Step 3d CARRY-FORWARD above: channel taxonomy activated; G-1=[final], G-2=[final], G-3=[final]"]
Status:     YES — Phase 4 is valid to begin.  |  NO — return to Step 3d.
```

Amend entry (change): [finding], [source], [remediation channel], [section changed], [change], [source confirmed].
Amend entry (dismissal): [finding], [reason], [remediation channel], [source confirmed].

---

### Verdict (Phase 5 — Compliance Ledger)

"Observed behavior: as expected" is structurally invalid — name the specific values observed.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [state actual definitions from Step 3a table] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries {P1,P2,P3} | [list severity values used; count each] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [state G-3 result and labels scanned] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All entries {P1,P2,P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay — [name] | EG findings {P1,P2,P3} | [list labels from this role's EG findings] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [list Source labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG | Promoted use SG; label lock holds | [list promoted gaps; confirm SG label] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source | {SA,SG,EG,QO}; promoted show SG | [list Source labels; confirm promoted] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay — [name] | Labels schema-conformant | [list labels by role] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state Step 3d CARRY-FORWARD activation text] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [list channels per entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked | [state Gate-Clearance Summary final states] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Entered on all-PASS final states | [state Phase 4 PREREQUISITE CHECK Evidence text] | PASS / FAIL |
| VC-4 | Schema 4 | G-1 cross-role | >=2 Source types across roles | [list Source types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 | 3a → 3b | Step 3b began after Step 3a confirmed | [state Step 3a CARRY-FORWARD text] | PASS / FAIL |
| VC-5 | Schema 5 | 3b → 3c | Step 3c began after Step 3b >=2 entries | [state Step 3b CARRY-FORWARD entry count] | PASS / FAIL |
| VC-5 | Schema 5 | 3c → 3d | Step 3d began after Gate-Clearance all-PASS | [state Step 3c CARRY-FORWARD Gate-Clearance text] | PASS / FAIL |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 began after Step 3d confirmed | [state Step 3d CARRY-FORWARD and Phase 4 PREREQUISITE CHECK Evidence] | PASS / FAIL |

**VC overall**: VC-1: PASS/FAIL | VC-2: PASS/FAIL | VC-3: PASS/FAIL | VC-4: PASS/FAIL | VC-5: PASS/FAIL

**SA remaining**: [N] | **SG total**: [N] | **EG total**: [N]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 — All aspirationals integrated (C-09 through C-14)

**Axis**: Full integration — every aspirational criterion from v3 is addressed by an explicit structural element. C-09 is addressed by a compliance ledger prohibition and named-value requirement. C-10 is addressed by carry-forward confirmation blocks at every phase boundary. C-11 is addressed by the Gate-Clearance Summary block (a distinct required section between Step 3c and 3d). C-12 is addressed by an explicit REMEDIATION LOOP template per gate + a C-12 EXEMPTION NOTICE when no loop is needed. C-13 is addressed by named-artifact PREREQUISITE CHECK blocks at every sub-step entry. C-14 is addressed by the Gate-Clearance Summary recording **final (post-remediation) states only**, with an explicit C-14 COHERENCE CHECK confirming the summary and the Phase 4 pre-check agree.

**Hypothesis**: V-01 through V-04 each address a subset of the aspirational tier. The integration cascade creates structural guarantees no subset achieves: (1) each sub-step entry is blocked until a named artifact confirms the predecessor (C-13), (2) each sub-step exit names what was produced (C-10), (3) the Gate-Clearance Summary consolidates final states in one auditable block (C-11), (4) when a gate fails, the remediation loop is explicit and structured (C-12), (5) the C-14 Coherence Check enforces that Phase 4 reads from the Gate-Clearance Summary final states — a remediation loop that resolves a FAIL cannot be hidden by writing the original FAIL in the Phase 4 header, because Phase 4's prerequisite check cites the Gate-Clearance Summary by name, (6) the compliance ledger requires named values at every site, making it impossible to pass VC checks with generic language (C-09). Risk: the combined overhead may produce a trace that satisfies all structural criteria but produces shallow artifact content in Phase 2, since model attention is distributed across many structural blocks. The carry-forward blocks in Phase 2 partially mitigate this by naming what was produced.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. Every label, channel, and gate used anywhere in this trace must be declared in this table. Using a label not declared here is a protocol violation.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source column, all role relays | All roles; promoted gaps use SG in all downstream phases | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | All Phase 4 amendment entries | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (evaluate), Gate-Clearance Summary (consolidate final states), Phase 4 pre-check | G-1 cross-role; all three gates must PASS (final) before Phase 4 | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (prerequisite checks and carry-forward confirmations at each boundary) | N/A | VC-5 |

**Schema 1 — Severity Vocabulary**: Valid labels: {P1, P2, P3} only. P1 = artifact-blocking. P2 = quality improvement. P3 = advisory. A label outside this set anywhere in the trace is a structural violation.

**Schema 2 — Gap Type Taxonomy**: Valid labels: {SA, SG, EG, QO}. SA-TO-SG label lock invariant: a gap promoted at the SA-TO-SG PROMOTION event uses the SG label in all subsequent phases. A promoted gap appearing as SA in any downstream phase is a label lock violation.

**Schema 3 — Remediation Channel Taxonomy**: Valid channels: {spec, invocation, artifact, quality}. Every Phase 4 Amend entry must include `[remediation channel: ...]`. An entry without this field is structurally incomplete.

**Schema 4 — Enforcement Gate Registry**: Three gates, all must PASS (final states) before Phase 4 begins.
- G-1: Step 3b contains >=2 distinct Source types (cross-role aggregate).
- G-2: No two findings sharing the same Source label carry identical Action text.
- G-3: All Step 3b entries use only {P1, P2, P3}.
A gate that fails and is remediated records PASS in the **Gate-Clearance Summary** (final state), not the initial FAIL.

**Schema 5 — Sub-Step Ordering**: Contract: 3a → 3b → 3c → 3d. Each boundary enforced by a PREREQUISITE CHECK (entry) and a CARRY-FORWARD CONFIRMED block (exit).

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 in Coverage Matrix | Severity legend | Step 3b |
| Step 3b | Step 3a severity legend | Findings table >=2 entries | Step 3c |
| Step 3c | Step 3b >=2 entries | Gate results + Gate-Clearance Summary | Step 3d |
| Step 3d | Gate-Clearance Summary all-PASS | Channel taxonomy active | Phase 4 |

#### Role-Schema Binding Summary

One row per role in the execution sequence. A role without explicit schema binding is invalid.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role name] | [severity labels for this role's EG findings, or "N/A — produces no EG findings"] | [Source labels this role may produce; label lock rule if it handles promoted gaps] | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Read only `{{skill_spec_path}}`. Examine all three source layers before declaring done. A Stage 1 clustering all gaps at one source type is structurally incomplete.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay record:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 — Hand-Compilation

Stage 2 receives the relay. All gaps carry forward without re-derivation or silent resolution.

---

#### SA-TO-SG PROMOTION

Every SA gap from the Stage 1 relay evaluated here. A gap a spec-competent invoker can supply at runtime promotes to SG. A gap requiring a spec change remains SA. Label lock applies from this point forward.

```
SA-NN:
  Gap: [what the spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence — why invoker can / cannot supply this]
```

Post-promotion inventory:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

**STAGE 1 → PHASE 1 CARRY-FORWARD CONFIRMED**
Produced: gap audit table ([N] SA, [N] SG, [N] EG gaps) + relay + SA-TO-SG PROMOTION entries ([N] promoted, [N] remain SA).
SA remaining: [N] | SG total: [N] | Layer diversity: [PASS/FAIL].
Phase 1 prerequisite satisfied: Stage 1 relay and SA-TO-SG PROMOTION complete. Phase 1 is valid to begin.

---

#### Phase 1 — Setup

Confirmed input bindings:
- [topic: ] | [scope_in: ] | [scope_out: ] | [roles: ] | [stack: / detection: ] | [spec_version: ]

Per-role schema binding and gap attribution (one block per role):

```
[role: {{role_name}}]
  Schema 1 binding: [severity labels applicable to this role's EG findings, or "N/A"]
  Schema 2 binding: [Source labels this role may produce; label lock rule for promoted gaps]
  SA/SG gaps binding this role: [list or "none — confirmed after checking gap inventory"]
  EG gaps expected: [list or "none — confirmed"]
```

**PHASE 1 → PHASE 2 CARRY-FORWARD CONFIRMED**
Produced: confirmed input bindings + per-role schema binding blocks for [N] roles: [list role names].
SA remaining: [N] | SG total: [N] | Roles in sequence: [ordered list].
Phase 2 prerequisite satisfied: all roles have schema binding declarations. Phase 2 is valid to begin.

---

#### Phase 2 — Execute

Produce the hand-compiled artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md`. Every section the skill spec requires must be present with real content. No elision markers.

Per-role relay (one per role; Schema 2 compliance field required):

**Role relay — [role name]**:
- Received from: [prior role or Phase 1 Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none — confirmed"]
- Produced: [artifact section(s) content added]
- EG gaps encountered: [EG-NN list or "none — confirmed"]

**PHASE 2 → PHASE 3 CARRY-FORWARD CONFIRMED**
Produced: artifact at `simulations/trace/skill/{topic}-skill-trace-{date}.md` ([N] of [required N] sections written) + per-role relays for [N] roles: [list names].
EG gaps added during execute: [list or "none"].
Phase 3 prerequisite satisfied: artifact produced and all role relays complete. Phase 3 is valid to begin.

---

#### Phase 3 — Findings

Sub-steps run in Schema 5 order. Each sub-step: (1) opens with a PREREQUISITE CHECK naming a specific artifact; (2) closes with a CARRY-FORWARD CONFIRMED block naming what was produced. Both blocks are required. A bare "YES" in the Status field without a named Evidence referent fails C-13.

---

##### Step 3a — Severity Legend Declaration

```
PREREQUISITE CHECK — Step 3a
Condition:  Schema 1 (Severity Vocabulary {P1, P2, P3}) is declared in the Coverage Matrix.
Evidence:   [cite specifically: "Coverage Matrix above, Schema 1 row: 'P1 / P2 / P3'"]
Status:     YES — Step 3a is valid to begin.
            NO — return to Coverage Matrix; declare Schema 1 before proceeding.
```

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [specific definition: what makes a finding a blocker in this trace context] | Resolve before leaving Findings |
| P2 | [specific definition: what makes a finding a quality improvement here] | Address in Amend or follow-on |
| P3 | [specific definition: what makes a finding advisory here] | Log; no gate impact |

```
CARRY-FORWARD CONFIRMED — Step 3a
Produced: severity legend above (P1: [summary of definition], P2: [summary], P3: [summary]).
Step 3b prerequisite: Step 3a severity legend produced and named above. Step 3b is valid to begin.
```

---

##### Step 3b — Findings Table

```
PREREQUISITE CHECK — Step 3b
Condition:  Step 3a has produced a severity legend defining P1, P2, and P3 for this trace.
Evidence:   [cite specifically: "Step 3a CARRY-FORWARD above: produced severity legend, P1=[actual definition summary], P2=[summary], P3=[summary]"]
Status:     YES — Step 3b is valid to begin.
            NO — return to Step 3a; produce severity legend before proceeding.
```

Merge all gaps from Stage 1 + Phase 2 EG additions. Every finding uses Source labels from Schema 2 (promoted gaps use SG, not SA) and Severity labels from the Step 3a legend.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. Minimum 2 distinct Source types (required by G-1). Distinct Action text per Source (required by G-2). Only {P1,P2,P3} Severity (required by G-3).

```
CARRY-FORWARD CONFIRMED — Step 3b
Produced: findings table with [N] entries; Source types: [list, count per type]; Severity labels used: [list]; Action text distinct per Source: [YES/NO — if NO, revise before Step 3c].
Step 3c prerequisite: Step 3b table has [N] entries (>=2 confirmed), covering [M] Source types. Step 3c is valid to begin.
```

---

##### Step 3c — Enforcement Gates

```
PREREQUISITE CHECK — Step 3c
Condition:  Step 3b findings table has >=2 entries and was declared complete.
Evidence:   [cite: "Step 3b CARRY-FORWARD above: [N] entries, Source types [list], Action text distinct: YES"]
Status:     YES — Step 3c is valid to begin.
            NO — return to Step 3b; add findings or resolve Action text issues before proceeding.
```

Run each gate. On FAIL: execute the C-12 REMEDIATION LOOP before recording the gate result.

**G-1 Evaluation**:
Source types present in Step 3b: [list]. Distinct count: [N].

> If N >= 2: G-1 initial = PASS. No loop needed.
>
> If N < 2: G-1 initial = FAIL.
> ```
> C-12 REMEDIATION LOOP — G-1:
> 1. Action:     Identify missing source layer: [name it].
>                Add to Step 3b: [new finding ID, Finding text, Source: [missing type], Severity: [label], Action: [distinct text]].
> 2. Re-check:   Source types in Step 3b after addition: [updated list]. Distinct count: [N+].
> 3. G-1 after remediation: PASS / FAIL (if still FAIL, state what blocks resolution).
> ```

**G-1 final**: PASS / FAIL

**G-2 Evaluation**:
Same-Source finding pairs: [list pairs or "no same-Source pairs found"].

> If no duplicates: G-2 initial = PASS. No loop needed.
>
> If duplicates: G-2 initial = FAIL.
> ```
> C-12 REMEDIATION LOOP — G-2:
> 1. Action:     Identify duplicate: findings [F-NN] and [F-MM] share Source=[X] and Action=[text].
>                Revise [F-MM] Action to: [distinct target text].
> 2. Re-check:   Action text for same-Source pairs after revision: [confirm distinct].
> 3. G-2 after remediation: PASS / FAIL.
> ```

**G-2 final**: PASS / FAIL

**G-3 Evaluation**:
Severity labels in Step 3b: [list all values].

> If all in {P1,P2,P3}: G-3 initial = PASS. No loop needed.
>
> If any outside {P1,P2,P3}: G-3 initial = FAIL.
> ```
> C-12 REMEDIATION LOOP — G-3:
> 1. Action:     Finding [F-NN] uses label [invalid]. Relabel as [P1/P2/P3] because [reason].
> 2. Re-check:   Severity labels in Step 3b after relabeling: [updated list].
> 3. G-3 after remediation: PASS / FAIL.
> ```

**G-3 final**: PASS / FAIL

---

> **C-12 STATUS** (required — choose one):
>
> **C-12 EXEMPTION APPLIES**: All three gates (G-1, G-2, G-3) passed on initial evaluation. No remediation loop was required for this trace. C-12 is exempt.
>
> — or —
>
> **C-12 REMEDIATION LOOP(S) EXECUTED**: [state which gates triggered loops and the final result for each]. C-12 is not exempt; loops are documented above.

---

**GATE-CLEARANCE SUMMARY — Phase 4 Entry**

> Required block. Records final (post-remediation) gate states. Phase 4 reads from this block only — not from initial evaluation results. This block is the C-11 consolidated gate-clearance summary and the C-14 source of truth for Phase 4.

| Gate | Initial result | C-12 loop ran? | Final result | Note |
|------|---------------|----------------|-------------|------|
| G-1 | [initial] | YES / NO | [final] | [state what satisfied or violated it] |
| G-2 | [initial] | YES / NO | [final] | |
| G-3 | [initial] | YES / NO | [final] | |

**Phase 4 entry: AUTHORIZED** (G-1 final=PASS AND G-2 final=PASS AND G-3 final=PASS)
**Phase 4 entry: BLOCKED** (return to Step 3c; remediate failing gate(s); re-issue this block)

```
CARRY-FORWARD CONFIRMED — Step 3c
Produced: gate results (initial + final) + Gate-Clearance Summary (G-1=[final], G-2=[final], G-3=[final]).
C-12 status: [EXEMPT / LOOP(S) EXECUTED].
Step 3d prerequisite: Gate-Clearance Summary all-PASS (final states). Step 3d is valid to begin.
```

---

##### Step 3d — Channel Taxonomy Activation

```
PREREQUISITE CHECK — Step 3d
Condition:  Gate-Clearance Summary records G-1=PASS, G-2=PASS, G-3=PASS (final states).
Evidence:   [cite: "Gate-Clearance Summary above: G-1=[final], G-2=[final], G-3=[final] — Phase 4 AUTHORIZED"]
Status:     YES — Step 3d is valid to begin.
            NO — return to Step 3c; all three gates must show PASS in Gate-Clearance Summary.
```

Schema 3 channel taxonomy is now active for Phase 4: spec / invocation / artifact / quality. Every Phase 4 Amend entry must include `[remediation channel: ...]`. An entry missing this field is structurally incomplete.

```
CARRY-FORWARD CONFIRMED — Step 3d
Produced: Schema 3 channel taxonomy activated (spec / invocation / artifact / quality).
Phase 4 prerequisite: Step 3d activation confirmed; Gate-Clearance Summary all-PASS cited above. Phase 4 is valid to begin.
```

---

**PHASE 3 → PHASE 4 CARRY-FORWARD CONFIRMED**
Produced: severity legend (3a) + findings table ([N] entries, [M] Source types) (3b) + gate results + Gate-Clearance Summary (3c, final: G-1=PASS, G-2=PASS, G-3=PASS) + channel taxonomy activation (3d).
Highest finding: [F-NN] | Source: [label] | Severity: [label].
C-12 status: [EXEMPT / LOOPS EXECUTED for gates: list].

---

#### Phase 4 — Amend

```
PREREQUISITE CHECK — Phase 4
Condition:  Step 3d has activated the Schema 3 channel taxonomy AND Gate-Clearance Summary records all-PASS final states.
Evidence:   [cite: "Step 3d CARRY-FORWARD above: channel taxonomy activated. Gate-Clearance Summary: G-1=[final], G-2=[final], G-3=[final]"]
Status:     YES — Phase 4 is valid to begin.
            NO — return to Step 3d. Confirm Gate-Clearance Summary all-PASS before producing Amend entries.
```

> **C-14 COHERENCE CHECK**:
> The Gate-Clearance Summary (C-11) records: G-1=[final], G-2=[final], G-3=[final].
> This Phase 4 entry reads those final states.
> [If C-12 loops ran: "G-[N] changed from [initial] to [final] via C-12 loop. This Phase 4 entry reflects the post-remediation state, not the initial evaluation state. C-14 satisfied."]
> [If C-12 exempt: "No remediation loops ran. Initial and final states are identical. C-14 satisfied trivially."]

A valid Amend entry (change):
- [finding: F-NN]
- [source: Schema-2-label] (label lock: promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES — fix is at the [source] layer / NO — explain]

A valid Amend entry (dismissal):
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 — Compliance Ledger)

The Verdict audits every usage site declared in the Coverage Matrix. A row with "Observed behavior: as expected" is structurally invalid — the Observed behavior cell must name specific values, labels, role names, finding IDs, or invariant results. Generic observations fail C-09.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared with definitions | [state the actual P1 definition, P2 definition, P3 definition written at Step 3a] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | All entries use only {P1, P2, P3} | [list severity values used in Step 3b table; count of each; flag any outside set] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified: all Step 3b entries use {P1,P2,P3} | [state G-3 initial and final results; list labels G-3 checked] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use {P1,P2,P3} | [list severity values appearing in each Amend entry; flag any outside set] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay — [name] | EG findings from this role use {P1,P2,P3} per Schema 1 binding | [list severity labels used in this role's EG findings specifically; confirm binding honored] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | Source labels SA/SG/EG/QO used in audit table | [list all Source labels that appeared in Stage 1 table; confirm none outside schema] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps use SG; label lock holds downstream | [list SA gaps that promoted; name each downstream reference to confirm SG label used] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [list each Source label in Step 3b table; identify any promoted gap and confirm SG] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay — [name] | Source labels from schema; label lock honored | [list Source labels used by this role in its relay; note promoted gaps and their labels] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [quote the Step 3d CARRY-FORWARD activation statement exactly] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field from {spec,invocation,artifact,quality} | [list: F-NN → channel, for each entry; flag any missing] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 evaluated with explicit PASS/FAIL | [state initial and final results for all three gates; note C-12 loops if run] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered on final-all-PASS from Gate-Clearance Summary | [state the Phase 4 PREREQUISITE CHECK Evidence field text; confirm Gate-Clearance cited] | PASS / FAIL |
| VC-4 | Schema 4 | G-1 cross-role aggregate | >=2 distinct Source types in Step 3b across all roles | [list Source types present and which role relays contributed each] | PASS / FAIL |
| VC-5 | Schema 5 | 3a → 3b | Step 3b PREREQUISITE CHECK cited Step 3a output by name | [quote the Step 3b PREREQUISITE CHECK Evidence field text] | PASS / FAIL |
| VC-5 | Schema 5 | 3b → 3c | Step 3c PREREQUISITE CHECK cited Step 3b entry count by name | [quote the Step 3c PREREQUISITE CHECK Evidence field text] | PASS / FAIL |
| VC-5 | Schema 5 | 3c → 3d | Step 3d PREREQUISITE CHECK cited Gate-Clearance Summary by name | [quote the Step 3d PREREQUISITE CHECK Evidence field text] | PASS / FAIL |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 PREREQUISITE CHECK cited Step 3d CARRY-FORWARD by name | [quote the Phase 4 PREREQUISITE CHECK Evidence field text] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS (including per-role rows) / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**Stage 1 layer diversity**: [PASS/FAIL]
**SA remaining**: [N] | **SG total**: [N] | **EG total**: [N]
**C-12 status**: [EXEMPT / LOOP(S) EXECUTED — gates: list]
**C-14 status**: [SATISFIED — post-remediation states flow to Phase 4 / EXEMPT — no loops ran]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## Variation Summary

| Variation | Axis | Hypothesis | New criteria targeted |
|-----------|------|------------|----------------------|
| V-01 | Lifecycle emphasis | Explicit boundary blocks make C-10/C-11 structural; carry-forward must name output not just label | C-10, C-11 |
| V-02 | Output format | Named-artifact prerequisite checkboxes prevent bare YES at sub-step entries | C-13 |
| V-03 | Phrasing register | Imperative HALT/REMEDIATE loop template closes the silent FAIL-to-PASS path; C-12 EXEMPTION NOTICE closes the silence-means-exempt path; C-14 Coherence Check ties Phase 4 summary to final states | C-12, C-14 |
| V-04 | Combined (V-01 + V-02) | Dual-block structure (entry checkbox + exit confirmation) makes C-10/C-11/C-13 all structural per sub-step | C-10, C-11, C-13 |
| V-05 | All aspirationals | Integration cascade: checkboxes (C-13) + carry-forwards (C-10) + Gate-Clearance Summary (C-11) + remediation loops (C-12) + coherence check (C-14) + named-value ledger (C-09) — each reinforces the next | C-09, C-10, C-11, C-12, C-13, C-14 |

**Expected R3 winner**: V-05, by the same integration-cascade mechanism that made V-05 the R2 winner — aspirationals reinforce each other in a pipeline, and satisfying all of them creates structural guarantees no subset achieves.

**Expected R3 differentiator from R2**: C-14 is the new axis. V-03 and V-05 both address it explicitly. The C-14 COHERENCE CHECK block is the pattern to watch — it enforces that the Gate-Clearance Summary (C-11) and the Phase 4 pre-check agree on final gate states, closing the cross-axis incoherence that C-14 was added to catch.
