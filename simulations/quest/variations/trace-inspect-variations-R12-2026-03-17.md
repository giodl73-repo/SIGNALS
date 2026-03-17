Good. I now have the full picture: R8 v5 was the last run on 2026-03-17, rubric is now v8 (adds C-26 and C-27 from R11 excellence signals), and Round 12 needs to target these two new criteria while consolidating the others. Let me generate the five variations.

---

# trace-inspect — Variations R12 v8 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: Best R11 variation achieves C-01 through C-25 PASS under rubric v7. Rubric v8 adds two new aspirational criteria from R11 excellence signals:

- **C-26** (0.5 pts): NEEDS-REDESIGN EVIDENCE ANCHOR — the verdict names each contributing EG finding by ID; count is derived from the explicit list (e.g., "3 EG findings: F-03, F-05, F-07"), not stated independently.
- **C-27** (0.5 pts): PROMOTION COMPLETENESS GATE — SA-TO-SG PROMOTION includes an arithmetic self-check `(promoted + remaining = Stage 1 SA count)` with explicit PASS/MISMATCH result; MISMATCH structurally blocks Phase 2 (Execute).

**R11 baseline against v8 (C-26/C-27 projected)**:
- C-26: FAIL. Prior prompt defines NEEDS-REDESIGN as "EG gaps exceed 3 and indicate a structural role gap" but does not require the verdict text to enumerate finding IDs or derive count from a named list. A model can write "4 EG gaps suggest redesign" and satisfy the classification rule without naming the IDs.
- C-27: FAIL. Prior prompt's SA-TO-SG PROMOTION section lists individual promotion decisions but includes no arithmetic closure: nothing forces the model to verify `promoted + remaining = Stage 1 SA count`. Omissions pass silently.

**Variation axes selected**:
- **V-01**: Lifecycle emphasis — NEEDS-REDESIGN evidence anchor (targets C-26)
- **V-02**: Output format — Promotion completeness gate table (targets C-27)
- **V-03**: Phrasing register — imperative gate clearance summary blocks + remediation log (targets C-11, C-12)
- **V-04**: Combined V-01 + V-02 (targets C-26, C-27)
- **V-05**: Full integration (targets C-26, C-27, C-11, C-12, with C-09 prohibition reinforce)

---

## V-01

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Adding an explicit NEEDS-REDESIGN evidence anchor mandate in the Verdict section — requiring the verdict to name each contributing EG finding by ID and derive the count from that named list — will close C-26 without disturbing C-01 through C-25.

---

You are running `/trace-skill` for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol authority: every label, channel, and gate used in any downstream phase must be declared in this table. A phase using a label not declared here is in violation of the trace protocol.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relay | All roles (label lock: promoted gaps use SG) | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Applies to all Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | G-1 aggregates Source coverage across all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 (enforce transitions) | N/A — applies to Findings phase structure | VC-5 |

**Schema 1**: Valid severity labels: P1, P2, P3. P1 = blocks artifact usefulness. P2 = quality improvement, does not block. P3 = advisory. Any other label is a structural violation.

**Schema 2**: Valid source labels: SA (spec-layer gap), SG (setup gap), EG (execute gap), QO (quality observation). Label lock: a promoted SA gap uses SG in all phases after SA-TO-SG PROMOTION. A promoted gap retaining SA is a structural violation.

**Schema 3**: Valid remediation channels: spec, invocation, artifact, quality. An Amend entry without a channel field is structurally incomplete.

**Schema 4**: Three invariants — G-1: Step 3b contains ≥2 distinct Source types. G-2: No two same-Source findings share identical Action text. G-3: All Step 3b entries use only {P1, P2, P3}. All three must hold before Phase 4 begins.

**Schema 5**: Step 3b valid only after Step 3a. Step 3c valid only after Step 3b (≥2 findings). Step 3d valid only after Step 3c (all-PASS). Phase 4 valid only after Step 3d.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels for EG findings, or "N/A — produces no EG findings"] | [Source labels this role may produce; label lock rules for promoted gaps] | [any Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one source type is structurally incomplete. Examine all three source layers before declaring done.

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

Stage 2 receives the relay. Carry all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

Every SA gap in the Stage 1 relay is evaluated. A gap a spec-competent invoker can supply at runtime promotes to SG. A gap requiring a spec change remains SA. One entry per SA gap:

```
SA-NN:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [one sentence]
```

After promotion:
```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Label lock invariant: a promoted gap using its SA label in any downstream phase is a structural violation.

---

#### Phase 1 — Setup

Confirmed input bindings: [topic], [scope_in], [scope_out], [roles], [stack/detection_method], [spec_version].

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

Produces: hand-compiled artifact `{topic}-skill-trace-{date}.md` with every section the artifact contract requires, and a per-role relay for each role.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact path], [EG added].

---

#### Phase 3 — Findings

Sub-steps run in the order declared by Schema 5. A sub-step begun without its prerequisite satisfied is structurally invalid.

##### Step 3a — Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with ≥2 entries. Step 3c is valid to begin.

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b populated (≥2 entries).

**G-1**: Step 3b contains ≥2 distinct Source types.
- Source types present: [list]
- Result: PASS / FAIL (if FAIL: structural defect — add a finding from the missing layer, re-check)

**G-2**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none — all Source types unique"]
- Result: PASS / FAIL (if FAIL: revise Action text to name distinct targets, re-check)

**G-3**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- Result: PASS / FAIL (if FAIL: relabel non-conforming entries, re-check)

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS.

Schema 3 channel taxonomy is now active for Phase 4. Valid channels: spec, invocation, artifact, quality. Every Phase 4 Amend entry must name a channel from this set.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Findings carry-forward**: [highest finding], [source], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 — Amend

Invariant status: G-1 PASS, G-2 PASS, G-3 PASS. If any = FAIL: Phase 4 is structurally blocked — return to Step 3c.

A valid Amend entry (change):
- [finding: F-NN]
- [source: {{source}}] (label lock invariant applies)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO + explanation]

A valid Amend entry (dismissal):
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict

The Verdict is produced after Phase 4 completes. A Verdict row with "Observed behavior: as expected" is structurally invalid — the Observed behavior cell must name specific values, labels, role names, or invariant results.

VC compliance ledger:

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 | [state what the legend said — the actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only {P1, P2, P3} | [list severity values used; count of each] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only {P1,P2,P3} | [list severity values in Amend entries] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay — [role producing EG] | EG findings use only {P1,P2,P3} | [severity labels used by this role's EG findings] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used | [list all Source labels in Stage 1 table] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG label | [list SA gaps promoted; confirm SG label in downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [list Source labels; identify any promoted gap] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay — [role] | Source labels from {SA,SG,EG,QO}; label lock honored | [list Source labels used by this role] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [state activation evidence at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry includes channel field | [list channels used; flag any missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked with explicit PASS/FAIL | [state all three results] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 entered only when all gates PASS | [confirm invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | ≥2 distinct Source types from all roles | [list types present and which roles contributed each] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a → 3b | Step 3b valid only after 3a | [confirm 3a completion before 3b] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b → 3c | Step 3c valid only after 3b (≥2 findings) | [state entry count at 3c start] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c → 3d | Step 3d valid only after all-PASS gates | [state gate results before 3d] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d → Phase 4 | Phase 4 valid only after channel taxonomy active | [state activation confirmation before Phase 4] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

Classification rules:
- `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
- `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
- `USEFUL` otherwise.

> **NEEDS-REDESIGN EVIDENCE ANCHOR**: When the trace result is `NEEDS-REDESIGN`, the verdict
> statement must enumerate each contributing EG finding by ID and derive the stated count from
> that named list. Required form:
>
> `NEEDS-REDESIGN: [N] EG findings indicate a structural role gap. Contributing findings: F-XX, F-YY, F-ZZ [, ...].`
>
> Where N = the count of IDs in the named list. A NEEDS-REDESIGN verdict that states a count
> without enumerating the contributing finding IDs is structurally invalid — the count is not
> self-evidencing; it must be derivable by inspection of the ID list. If the trace result is
> USEFUL or NEEDS-SPEC-REVISION, this block is not required.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02

**Variation axis**: Output format
**Hypothesis**: Restructuring the SA-TO-SG PROMOTION section to include a named arithmetic completeness gate — a three-field balance block with explicit PASS/MISMATCH result and a structural block on Execute if MISMATCH — will close C-27 without disturbing prior criteria.

---

You are running `/trace-skill` for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

*(Coverage Matrix identical to V-01 — Schema 1 through Schema 5, all declared before Stage 1.)*

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles; label lock for promoted gaps | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source coverage | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

**Schema 1**: P1 = blocks artifact. P2 = quality improvement. P3 = advisory. No other label valid.
**Schema 2**: SA = spec-layer, SG = setup, EG = execute, QO = quality. Label lock: promoted SA → SG in all downstream phases.
**Schema 3**: spec / invocation / artifact / quality. Every Amend entry names one channel.
**Schema 4**: G-1 (≥2 Source types in 3b), G-2 (no duplicate Action per Source), G-3 (only {P1,P2,P3}). All-PASS required before Phase 4.
**Schema 5**: 3a before 3b, 3b before 3c, 3c (all-PASS) before 3d, 3d before Phase 4.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock] | [interactions] |

---

### Stage 1 — Source-Layer Audit

Reads only `{{skill_spec_path}}`. Examine all three source layers. A Stage 1 where all gaps cluster at one source type is structurally incomplete.

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

Stage 2 receives the relay. Carry all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

Every SA gap in the Stage 1 relay is evaluated. One entry per SA gap:

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

> **PROMOTION COMPLETENESS GATE**: After recording all individual promotion decisions, verify
> the arithmetic closure of this event. Fill the completeness check:
>
> | Field | Value |
> |-------|-------|
> | SA count declared in Stage 1 audit | [N] |
> | SG promoted in this event | [M] |
> | SA remaining after promotion | [K] |
> | Completeness check: M + K = N? | PASS / MISMATCH |
>
> **If MISMATCH**: Phase 2 (Execute) is structurally blocked. The promotion inventory does not
> account for all Stage 1 SA gaps. Audit the individual promotion entries. Identify the
> discrepancy. Correct and re-check until the equation holds. Phase 2 may not begin until this
> gate reads PASS.
>
> **If PASS**: The promotion event is complete. Phase 1 (Setup) may proceed.

Label lock invariant: a promoted gap using its SA label in any downstream phase is a structural violation.

---

#### Phase 1 — Setup

Confirmed input bindings: [topic], [scope_in], [scope_out], [roles], [stack/detection_method], [spec_version].

Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

Produces: hand-compiled artifact at `{topic}-skill-trace-{date}.md`, plus a per-role relay for each role.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact path], [EG added].

---

#### Phase 3 — Findings

Sub-steps run in Schema 5 order.

##### Step 3a — Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker definition] | Resolve before leaving Findings |
| P2 | [quality improvement definition] | Address in Amend or follow-on |
| P3 | [advisory definition] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a complete.
Schema 5 output: findings table with ≥2 entries (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with ≥2 entries. Step 3c is valid to begin.

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b populated (≥2 entries).
Schema 5 output: invariant results for G-1, G-2, G-3 (all-PASS unblocks Step 3d).

**G-1**: ≥2 distinct Source types in Step 3b.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none"]
- G-2: PASS / FAIL

**G-3**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS.
Schema 3 channel taxonomy (spec / invocation / artifact / quality) is now active for Phase 4.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Findings carry-forward**: [highest finding], [source], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 — Amend

Invariant status at Phase 4 entry: G-1 PASS, G-2 PASS, G-3 PASS. If any = FAIL: Phase 4 is structurally blocked.

A valid Amend entry (change): [finding], [source], [remediation channel], [section or field changed], [change], [source confirmed].
A valid Amend entry (dismissal): [finding], [reason], [remediation channel], [source type confirmed].

---

### Verdict

A Verdict row with "Observed behavior: as expected" is structurally invalid — name specific values.

VC compliance ledger: *(same 18-row structure as V-01)*

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 | [actual definitions written] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only {P1, P2, P3} | [list severity values; count of each] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified | [state G-3 result and labels checked] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only {P1,P2,P3} | [list severity values in Amend] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay — [role producing EG] | EG findings use {P1,P2,P3} | [severity labels used by this role] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO used | [all Source labels in Stage 1] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps receive SG; completeness gate PASS | [list promotions; state completeness gate result] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted use SG | [Source labels in Step 3b; any promoted gap confirmed SG] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay — [role] | Source labels from schema; label lock honored | [Source labels per role] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation language at Step 3d] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry has channel field | [channels per Amend entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked | [all three results] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | All gates PASS before Phase 4 | [invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | ≥2 Source types cross-role | [types present and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a → 3b | 3b after 3a | [confirmation] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b → 3c | 3c after 3b (≥2 findings) | [entry count at 3c start] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c → 3d | 3d after all-PASS | [gate results before 3d] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d → Phase 4 | Phase 4 after channel activation | [activation confirmation] | PASS / FAIL |

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

- `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
- `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
- `USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03

**Variation axis**: Phrasing register (imperative/structural)
**Hypothesis**: Replacing the implicit gate result prose at Step 3c with two named structural blocks — a GATE CLEARANCE SUMMARY between Step 3c and Step 3d, and a PHASE 4 GATE CLEARANCE SUMMARY at Phase 4 entry — plus a REMEDIATION LOG structure with an explicit C-12 EXEMPTION clause, will close C-11 and C-12 without disturbing prior criteria.

---

You are running `/trace-skill` for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

*(Schemas identical to V-01 and V-02.)*

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles; label lock for promoted gaps | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source coverage cross-role | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

**Schema 1**: P1 / P2 / P3 only. P1 blocks artifact. P2 does not block. P3 advisory.
**Schema 2**: SA / SG / EG / QO only. Label lock: promoted SA → SG everywhere downstream.
**Schema 3**: spec / invocation / artifact / quality. Every Amend entry names one.
**Schema 4**: G-1 (≥2 Source types), G-2 (no same-Source duplicate Actions), G-3 (only {P1,P2,P3}). All three must PASS.
**Schema 5**: strict sub-step ordering with prerequisite gates.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock] | [interactions] |

---

### Stage 1 — Source-Layer Audit

Reads only `{{skill_spec_path}}`. Examine all three source layers.

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

---

#### SA-TO-SG PROMOTION (named lifecycle event)

Every SA gap evaluated. One entry per SA gap:

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

Label lock invariant: promoted gaps use SG in all downstream phases.

---

#### Phase 1 — Setup

Confirmed input bindings. Per-role schema binding and gap attribution:
```
[role: {{role_name}}]
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact path], [EG added].

---

#### Phase 3 — Findings

##### Step 3a — Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with ≥2 entries. Step 3c is valid to begin.

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b populated (≥2 entries).

**G-1**: ≥2 distinct Source types in Step 3b.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2**: No two same-Source findings share identical Action text.
- Same-Source pairs: [list or "none"]
- G-2: PASS / FAIL

**G-3**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels: [list]
- G-3: PASS / FAIL

---

> #### GATE CLEARANCE SUMMARY (Step 3c → Step 3d)
>
> This block is a structural requirement. It must appear between Step 3c and Step 3d,
> after all three gate evaluations are complete and before Step 3d begins.
>
> | Gate | Result | Evidence |
> |------|--------|----------|
> | G-1 | PASS / FAIL | [Source types present: list] |
> | G-2 | PASS / FAIL | [Same-Source pairs examined: list or "none"] |
> | G-3 | PASS / FAIL | [Severity labels confirmed: list] |
>
> Phase gate: All three PASS — Step 3d is valid to begin. / One or more FAIL — Step 3d is BLOCKED.
>
> **If any gate FAIL — REMEDIATION LOG**:
> For each failing gate, record before re-checking:
> ```
> [Gate: G-N] | [Failure cause: what invariant was violated] | [Remediation action: what was added/changed/removed in Step 3b] | [Re-check result: PASS / still FAIL]
> ```
> Re-check the gate after each remediation. Update the Gate Clearance Summary to reflect
> post-remediation states. Step 3d may not begin until the summary reads all-PASS.
>
> **If all gates PASS on first evaluation — C-12 EXEMPTION**:
> All three gates cleared on first evaluation. No remediation action was taken.
> REMEDIATION LOG: not required. C-12 exemption applies.

---

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS (confirmed in Gate Clearance Summary above). Step 3d is valid.

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS (confirmed in Gate Clearance Summary above).
Schema 3 channels active: spec / invocation / artifact / quality.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Findings carry-forward**: [highest finding], [source], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 — Amend

> #### PHASE 4 GATE CLEARANCE SUMMARY (Phase 3 → Phase 4)
>
> This block is a structural requirement at Phase 4 entry. Confirm invariant status
> before any Amend entry is written.
>
> | Gate | Status | Source |
> |------|--------|--------|
> | G-1 | PASS | Confirmed at Step 3c Gate Clearance Summary |
> | G-2 | PASS | Confirmed at Step 3c Gate Clearance Summary |
> | G-3 | PASS | Confirmed at Step 3c Gate Clearance Summary |
>
> Phase 4 is valid to begin.
>
> If any gate shows FAIL here: Phase 4 is structurally blocked. Return to Step 3c.

A valid Amend entry (change): [finding], [source], [remediation channel], [section/field changed], [change], [source confirmed].
A valid Amend entry (dismissal): [finding], [reason], [remediation channel], [source type confirmed].

---

### Verdict

"Observed behavior: as expected" is structurally invalid — name specific values, labels, role names, or invariant results.

VC compliance ledger:

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared | [actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | Only {P1,P2,P3} | [severity values used; count] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | Only {P1,P2,P3} | [Amend severity values] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay — [EG-producing role] | EG findings use {P1,P2,P3} | [this role's EG severity labels] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO used | [Stage 1 Source labels] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted → SG; label lock | [list promoted; SG confirmed downstream] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted = SG | [Source labels; promoted gap label] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay — [role] | Source from schema; label lock | [per-role Source labels] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry has channel | [channels per entry] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 checked | [three results] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | All gates PASS at Phase 4 entry | [Phase 4 Gate Clearance Summary result] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | ≥2 Source types cross-role | [types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a → 3b | 3b after 3a | [confirmation] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b → 3c | 3c after 3b | [entry count] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c → 3d | 3d after all-PASS | [gate results] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d → Phase 4 | Phase 4 after channel activation | [activation confirmation] | PASS / FAIL |

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

- `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
- `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
- `USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04

**Variation axis**: Combined V-01 + V-02
**Hypothesis**: The NEEDS-REDESIGN evidence anchor (C-26) and the promotion completeness gate (C-27) are independent structural mandates targeting different phases — verdict and SA-TO-SG PROMOTION respectively. Their combination does not create interference; both should PASS while maintaining all prior criteria.

---

You are running `/trace-skill` for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles; label lock | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source coverage | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 | N/A | VC-5 |

**Schema 1**: P1 / P2 / P3 only. **Schema 2**: SA / SG / EG / QO; label lock on promotion. **Schema 3**: spec / invocation / artifact / quality. **Schema 4**: G-1, G-2, G-3 all-PASS required. **Schema 5**: strict sub-step ordering.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock] | [interactions] |

---

### Stage 1 — Source-Layer Audit

Reads only `{{skill_spec_path}}`. All three source layers examined.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Relay:
```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 — Hand-Compilation

---

#### SA-TO-SG PROMOTION (named lifecycle event)

One entry per SA gap:
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

> **PROMOTION COMPLETENESS GATE**: After all individual promotion decisions, verify closure:
>
> | Field | Value |
> |-------|-------|
> | SA count declared in Stage 1 audit | [N] |
> | SG promoted in this event | [M] |
> | SA remaining after promotion | [K] |
> | Completeness check: M + K = N? | PASS / MISMATCH |
>
> **If MISMATCH**: Phase 2 (Execute) is structurally blocked. Audit promotion entries.
> Identify the discrepancy. Correct and re-check. Phase 2 may not begin until PASS.
> **If PASS**: proceed to Phase 1 (Setup).

Label lock invariant holds downstream.

---

#### Phase 1 — Setup

Confirmed input bindings. Per-role schema binding:
```
[role: {{role_name}}]
  Schema 1 binding: [labels or "N/A"]
  Schema 2 binding: [Source labels; label lock]
  SA/SG gaps: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact path], [EG added].

---

#### Phase 3 — Findings

##### Step 3a — Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [blocker] | Resolve before leaving Findings |
| P2 | [quality] | Address in Amend or follow-on |
| P3 | [advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a complete.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with ≥2 entries. Step 3c is valid to begin.

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b populated (≥2 entries).

**G-1**: Source types present: [list] → PASS / FAIL
**G-2**: Same-Source pairs: [list or "none"] → PASS / FAIL
**G-3**: Severity labels: [list] → PASS / FAIL

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d is valid.

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS. Schema 3 channels active.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Findings carry-forward**: [highest finding], [source], G-1/G-2/G-3 PASS, channel taxonomy active.

---

#### Phase 4 — Amend

Invariant pre-check: G-1 PASS, G-2 PASS, G-3 PASS. If any FAIL: Phase 4 blocked.

A valid Amend entry (change): [finding], [source], [remediation channel], [section/field], [change], [source confirmed].
A valid Amend entry (dismissal): [finding], [reason], [remediation channel], [source type confirmed].

---

### Verdict

"Observed behavior: as expected" is structurally invalid — name specific values.

VC compliance ledger:

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 | Step 3a | Legend declared | [actual definitions] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3b | Only {P1,P2,P3} | [severity values; count] | PASS / FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result; labels] | PASS / FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | Only {P1,P2,P3} | [Amend severity values] | PASS / FAIL |
| VC-1 | Schema 1 | Role relay — [EG role] | EG use {P1,P2,P3} | [this role's EG severity labels] | PASS / FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO | [Stage 1 labels] | PASS / FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted → SG; completeness gate PASS | [promotions listed; gate result stated] | PASS / FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only schema labels; promoted = SG | [labels; promoted gap confirmed] | PASS / FAIL |
| VC-2 | Schema 2 | Role relay — [role] | Source from schema; label lock | [per-role Source labels] | PASS / FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation evidence] | PASS / FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel | [channels per entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3c | G-1, G-2, G-3 checked | [three results] | PASS / FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | All gates PASS | [invariant status at Phase 4 entry] | PASS / FAIL |
| VC-4 | Schema 4 | Step 3b aggregate (G-1) | ≥2 Source types | [types and contributing roles] | PASS / FAIL |
| VC-5 | Schema 5 | 3a → 3b | 3b after 3a | [confirmation] | PASS / FAIL |
| VC-5 | Schema 5 | 3b → 3c | 3c after 3b | [entry count] | PASS / FAIL |
| VC-5 | Schema 5 | 3c → 3d | 3d after all-PASS | [gate results] | PASS / FAIL |
| VC-5 | Schema 5 | 3d → Phase 4 | Phase 4 after activation | [activation confirmation] | PASS / FAIL |

**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

- `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
- `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
- `USEFUL` otherwise.

> **NEEDS-REDESIGN EVIDENCE ANCHOR**: When the trace result is `NEEDS-REDESIGN`, the
> verdict statement must enumerate each contributing EG finding by ID and derive the count
> from that named list:
>
> `NEEDS-REDESIGN: [N] EG findings indicate a structural role gap. Contributing findings: F-XX, F-YY, F-ZZ [, ...].`
>
> N must equal the count of IDs in the bracketed list. A count stated independently of the
> named list is structurally invalid. Not required when trace result is USEFUL or NEEDS-SPEC-REVISION.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05

**Variation axis**: Full integration
**Hypothesis**: All three single-axis mechanisms together — NEEDS-REDESIGN evidence anchor (C-26), promotion completeness gate (C-27), and named gate clearance summary blocks + remediation log with exemption clause (C-11, C-12) — achieve all four new-in-v8 aspirational targets simultaneously. Additionally, tightening the C-09 "as expected is structurally invalid" prohibition as an explicit preamble sentence (not just a parenthetical) reinforces the most common partial-credit gap across all prior variations.

---

You are running `/trace-skill` for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas here before Stage 1. The Coverage Matrix is the protocol authority. A phase using a label not declared here is in violation.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend | All roles producing EG findings | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b, Execute relay | All roles; label lock for promoted gaps | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | All Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source coverage cross-role | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 transitions | N/A | VC-5 |

**Schema 1**: P1 / P2 / P3 only. P1 blocks artifact. P2 quality, no block. P3 advisory. Any other label is a structural violation.

**Schema 2**: SA (spec-layer), SG (setup), EG (execute), QO (quality observation). Label lock invariant: a gap promoted in SA-TO-SG PROMOTION uses SG in all downstream phases. SA label on a promoted gap is a structural violation.

**Schema 3**: spec / invocation / artifact / quality. Every Amend entry names exactly one channel. An entry without a channel field is structurally incomplete.

**Schema 4**: G-1 (Step 3b contains ≥2 distinct Source types), G-2 (no two same-Source findings share identical Action text), G-3 (all Step 3b entries use only {P1,P2,P3}). All three invariants must hold before Phase 4 begins. A structural defect must be remediated and re-checked; it cannot be bypassed.

**Schema 5**: Step 3b valid only after 3a. Step 3c valid only after 3b (≥2 findings). Step 3d valid only after 3c (all-PASS). Phase 4 valid only after 3d.

#### Role-Schema Binding Summary

One row per role in the spec. A role without explicit schema binding is invalid.

| Role | Schema 1 binding | Schema 2 binding | Notes |
|------|-----------------|-----------------|-------|
| [role from spec] | [severity labels applicable to this role's EG findings, or "N/A — produces no EG findings"] | [Source labels this role may produce; label lock rules for promoted gaps] | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Reads only `{{skill_spec_path}}`. A Stage 1 where all gaps cluster at one source type is structurally incomplete. Examine all three source layers before declaring done.

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

Stage 2 receives the relay. Carry all gaps forward without re-deriving or silently resolving them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

Every SA gap from the Stage 1 relay is evaluated. A gap a spec-competent invoker can supply at runtime promotes to SG. A gap requiring a spec change remains SA. One entry per SA gap:

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

> **PROMOTION COMPLETENESS GATE**: After recording all individual promotion decisions,
> verify the arithmetic closure of this lifecycle event. This gate is mandatory and
> must appear immediately after the promotion inventory above.
>
> | Field | Value |
> |-------|-------|
> | SA count declared in Stage 1 audit | [N] |
> | SG promoted in this event | [M] |
> | SA remaining after promotion | [K] |
> | Completeness check: M + K = N? | PASS / MISMATCH |
>
> **MISMATCH**: Phase 2 (Execute) is structurally blocked. The promotion inventory does not
> account for all Stage 1 SA gaps. Audit each SA-NN entry. Identify the gap between `M + K`
> and `N`. Correct the discrepancy. Re-run this gate. Phase 2 may not begin until PASS.
>
> **PASS**: The promotion event is arithmetically closed. Phase 1 (Setup) may proceed.

Label lock invariant: a promoted gap using its SA label in any downstream phase is a structural violation of this trace.

---

#### Phase 1 — Setup

A valid Setup produces confirmed input bindings and per-role schema binding blocks.

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
  Schema 1 binding: [severity labels or "N/A"]
  Schema 2 binding: [Source labels; label lock if promoted]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic], [scope], [roles], [SA remaining], [SG total].

---

#### Phase 2 — Execute

Produces: hand-compiled artifact `{topic}-skill-trace-{date}.md` with every section the artifact contract requires. A relay without the "Schema 2 compliance" field is structurally invalid.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used by this role: [list] — all from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

**Execute carry-forward**: [artifact path], [EG added].

---

#### Phase 3 — Findings

Phase 3 is valid if and only if sub-steps run in Schema 5 order. A sub-step begun without its prerequisite is structurally invalid.

##### Step 3a — Severity Legend Declaration

Schema 5 prerequisite: Schema 1 declared in Coverage Matrix (satisfied above).
Schema 5 output: severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before leaving Findings |
| P2 | [what makes it a quality improvement] | Address in Amend or follow-on |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

##### Step 3b — Findings Table

Schema 5 prerequisite: Step 3a complete (severity legend defined above).
Schema 5 output: merged findings table with ≥2 entries (unblocks Step 3c).

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Schema 5 transition: findings table populated with ≥2 entries. Step 3c is valid to begin.

##### Step 3c — Enforcement Gates

Schema 5 prerequisite: Step 3b populated (≥2 entries).
Schema 5 output: invariant results for G-1, G-2, G-3 (all-PASS unblocks Step 3d).

**G-1** (Schema 4): Step 3b contains ≥2 distinct Source types.
- Source types present: [list]
- G-1: PASS / FAIL

**G-2** (Schema 4): No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "none — all Source types unique"]
- G-2: PASS / FAIL

**G-3** (Schema 4): All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list]
- G-3: PASS / FAIL

---

> #### GATE CLEARANCE SUMMARY (Step 3c → Step 3d)
>
> This named block is a structural requirement. It must appear between Step 3c gate
> evaluations and Step 3d. Fill it from the gate results immediately above.
>
> | Gate | Result | Evidence |
> |------|--------|----------|
> | G-1 | PASS / FAIL | [Source types present: list them] |
> | G-2 | PASS / FAIL | [Same-Source pairs examined: list or "none"] |
> | G-3 | PASS / FAIL | [Severity labels confirmed: list them] |
>
> Phase gate: All three PASS — **Step 3d is valid to begin.**
> / One or more FAIL — **Step 3d is BLOCKED. See REMEDIATION LOG below.**
>
> **If any gate FAIL — REMEDIATION LOG** (one row per failing gate):
>
> | Gate | Failure cause | Remediation action taken | Re-check result |
> |------|--------------|--------------------------|-----------------|
> | G-N | [what invariant was violated] | [what was added/changed/removed in Step 3b] | PASS / still FAIL |
>
> After each remediation, re-run the failing gate. Update this log. Update the Gate
> Clearance Summary to reflect post-remediation state. Step 3d may not begin until
> all gates show PASS in the Gate Clearance Summary.
>
> **If all gates PASS on first evaluation — C-12 EXEMPTION**:
> All three gates cleared on first evaluation. No remediation action was required.
> REMEDIATION LOG: not required for this trace. C-12 exemption applies.

---

Schema 5 transition condition: G-1 = PASS, G-2 = PASS, G-3 = PASS (confirmed in Gate Clearance Summary above). Step 3d is valid.

##### Step 3d — Channel Taxonomy Activation

Schema 5 prerequisite: Step 3c all-PASS (confirmed in Gate Clearance Summary above).
Schema 5 output: Schema 3 channel taxonomy active for Phase 4 (unblocks Phase 4).

Valid channels for Phase 4: spec / invocation / artifact / quality. Every Amend entry must name exactly one.

Schema 5 transition: channel taxonomy active. Phase 4 is valid to begin.

**Findings carry-forward**: [highest finding: F-NN], [source], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 — Amend

> #### PHASE 4 GATE CLEARANCE SUMMARY (Phase 3 → Phase 4)
>
> This named block is a structural requirement at Phase 4 entry. Fill it before writing
> any Amend entry. If the trace passed a remediation loop in Step 3c, this summary must
> reflect post-remediation states — the initial FAIL result must not appear here.
>
> | Gate | Status | Confirmed at |
> |------|--------|-------------|
> | G-1 | PASS | Step 3c Gate Clearance Summary |
> | G-2 | PASS | Step 3c Gate Clearance Summary |
> | G-3 | PASS | Step 3c Gate Clearance Summary |
>
> Phase 4 is valid to begin. If any gate shows FAIL here: Phase 4 is structurally blocked.
> Return to Step 3c.

A valid Amend entry (change):
- [finding: F-NN]
- [source: {{source}}] (label lock: promoted gaps use SG)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES / NO + explanation]

A valid Amend entry (dismissal):
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 — Compliance Ledger)

**Structural prohibition**: A Verdict row with "Observed behavior: as expected" is structurally
invalid. The Observed behavior cell must name the specific values, labels, role name, or invariant
result actually observed. "As expected" is never sufficient. Fill each cell with direct evidence.

VC compliance ledger. One row per usage site in the Coverage Matrix Referenced-by column, plus
per-role adherence rows for VC-1 (roles producing EG findings) and VC-2 (all roles with relays),
plus the cross-role G-1 row for VC-4.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Site result |
|----|--------|-----------|------------------|------------------|-------------|
| VC-1 | Schema 1 (Severity) | Step 3a | Legend declared: P1/P2/P3 definitions written | [state the actual definitions written at Step 3a — not "as expected"] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3b | All entries use only {P1, P2, P3} | [list severity values used in Step 3b; count of each; flag any outside {P1,P2,P3}] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and the severity labels it checked; confirm result is PASS] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Phase 4 Amend | All Amend entries use only {P1,P2,P3} | [list severity values in Amend entries, or state which field carries severity] | PASS / FAIL |
| VC-1 | Schema 1 (Severity) | Role relay — [role producing EG] | EG findings use only {P1,P2,P3} | [list severity labels used by this role's EG findings specifically] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Stage 1 | SA/SG/EG/QO labels used | [list all Source labels in Stage 1 table; confirm no labels outside schema] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | SA-TO-SG PROMOTION | Promoted gaps → SG; completeness gate PASS | [list SA gaps promoted; confirm SG label downstream; state completeness gate result M+K=N] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Step 3b Source column | Only {SA,SG,EG,QO}; promoted gaps show SG | [list Source labels in Step 3b; identify any promoted gap and confirm its label] | PASS / FAIL |
| VC-2 | Schema 2 (Gap Type) | Role relay — [role] | Source labels from {SA,SG,EG,QO}; label lock honored | [list Source labels used by this role; confirm label lock if promoted gap present] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Step 3d | Channel taxonomy activated | [state the activation evidence at Step 3d — what language signaled activation] | PASS / FAIL |
| VC-3 | Schema 3 (Channel) | Phase 4 Amend | Every entry includes channel field | [list channels used in each Amend entry; flag any missing] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3c | G-1, G-2, G-3 with explicit PASS/FAIL | [state all three results recorded at Step 3c] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Phase 4 pre-check | Phase 4 entered only when all gates PASS | [state Phase 4 Gate Clearance Summary result; confirm post-remediation states if remediation occurred] | PASS / FAIL |
| VC-4 | Schema 4 (Gates) | Step 3b aggregate (G-1) | ≥2 Source types cross-role | [list Source types present and which roles contributed each] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3a → 3b | 3b valid only after 3a | [state what confirmed 3a complete before 3b began] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3b → 3c | 3c valid only after 3b (≥2 findings) | [state entry count in Step 3b at the point Step 3c began] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3c → 3d | 3d valid only after all-PASS | [state gate results in Gate Clearance Summary before Step 3d began] | PASS / FAIL |
| VC-5 | Schema 5 (Ordering) | 3d → Phase 4 | Phase 4 valid only after channel activation | [state activation confirmation and Phase 4 Gate Clearance Summary before Phase 4 began] | PASS / FAIL |

**VC-1 overall**: PASS if all VC-1 rows PASS / FAIL if any FAIL
**VC-2 overall**: PASS if all VC-2 rows PASS / FAIL if any FAIL
**VC-3 overall**: PASS if all VC-3 rows PASS / FAIL if any FAIL
**VC-4 overall**: PASS if all VC-4 rows PASS / FAIL if any FAIL
**VC-5 overall**: PASS if all VC-5 rows PASS / FAIL if any FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

Classification rules:
- `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
- `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
- `USEFUL` otherwise.

> **NEEDS-REDESIGN EVIDENCE ANCHOR**: When the trace result is `NEEDS-REDESIGN`, the verdict
> statement must enumerate each contributing EG finding by ID. The count stated in the verdict
> must be derived from the named list — it is not self-evidencing.
>
> Required verdict form when NEEDS-REDESIGN:
> `NEEDS-REDESIGN: [N] EG findings indicate a structural role gap. Contributing findings: F-XX, F-YY, F-ZZ [, ...].`
>
> Where N = the count of explicitly named IDs in the list. A verdict that states a number
> without naming the findings is structurally invalid. Not required when trace result is
> USEFUL or NEEDS-SPEC-REVISION.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## Summary

| Variation | Primary axis | C-26 | C-27 | C-11 | C-12 | Prior criteria risk |
|-----------|-------------|------|------|------|------|---------------------|
| V-01 | Lifecycle emphasis — NEEDS-REDESIGN anchor | TARGET | — | — | — | None — verdict-only addition |
| V-02 | Output format — promotion completeness gate table | — | TARGET | — | — | None — promotion-only addition |
| V-03 | Phrasing register — gate clearance summary blocks + remediation log | — | — | TARGET | TARGET | None — Phase 3 structural blocks |
| V-04 | Combined V-01 + V-02 | TARGET | TARGET | — | — | None — two independent sections |
| V-05 | Full integration (all four targets + C-09 prohibition as preamble) | TARGET | TARGET | TARGET | TARGET | None — additive mandates only |

**Predicted leaderboard**: V-05 leads. V-04 close behind (misses C-11/C-12). V-03 and V-02 tied if C-26 is harder to close than C-11/C-12. V-01 last (single-axis, lowest incremental gain over prior round).

**Failure patterns to watch**:
- C-27 MISMATCH gate: model may fill in N/M/K consistently without verifying the arithmetic. If M + K ≠ N, the gate must block Phase 2 — models tend to proceed regardless.
- C-26 count drift: model may state a count and then list a different number of IDs. The mandate that "N = count of IDs in the list" should catch this, but scores it as structural failure if the check is omitted.
- C-11 summary content: the gate clearance summary must reflect post-remediation states when a remediation loop ran. V-03 and V-05 add the coherence directive explicitly.
