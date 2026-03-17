Now I have the complete R6 V-05 champion structure. I can see exactly what each new criterion (C-15 through C-18) needs to add. Let me generate the R7 variations now.

---

# trace-inspect — Variations v4 R7 (2026-03-17)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**Entry state**: R6 champion is V-05 at 94/100 (estimated — R6 score was against rubric v3). Rubric v4 adds four new aspirational criteria (C-15 through C-18) from R6 excellence signals. The R7 target is to close all four while preserving V-05's existing coverage.

**R6 V-05 baseline coverage of the four new criteria**:

- **C-15 (FLOOR CHECK block)**: PARTIAL → R6 V-05 has the FLOOR CHECK block but the rubric formalization in v4 adds a harder requirement: the block must name every finding ID explicitly (not just a count), assert Action uniqueness, and emit a hard PASS/FAIL that blocks Step 3c. The R6 block meets most of this but "Action uniqueness: any two Action cells share identical text? YES/NO" is phrased as a question, not an assertion that explicitly blocks.

- **C-16 (mandatory execution-evidence citation at SA-TO-SG promotion)**: PARTIAL → R6 V-05 says "Reason: [cite execution evidence if post-execution, or spec inference if pre-execution]." The conditional "if post-execution" is permissive — an executor can cite spec inference even when execution evidence is available. C-16 requires: when execution has run, execution evidence is the required citation basis.

- **C-17 (G-1 cross-role attribution in compliance ledger)**: PARTIAL → R6 V-05 has a VC-4 G-1 cross-role row citing source types and contributing roles — but the row is a single prose entry. C-17 requires a structured attribution that names source types AND the specific roles that produced findings of each type.

- **C-18 (remediation entry precision)**: PARTIAL → R6 V-05 remediation log says "name the specific ID and change" in the instruction text. C-18 requires the named artifact format: "added F-04 (Source: EG, Action: add schema binding step for Role C)" — not just naming the ID but also specifying the Action text change.

**R7 variation axes** (three new axes targeting C-15 through C-18):

- **Lifecycle emphasis (C-16)**: Reposition SA-TO-SG PROMOTION as a post-execution mandatory evidence gate. When execution has run before promotion is evaluated, a mandatory EXECUTION EVIDENCE REQUIRED block forces citation (V-01).

- **Output format (C-17 + C-18 templates)**: Pre-print the G-1 cross-role attribution table as a two-column structure and pre-print the remediation entry as a precision template with finding ID + Action text fields (V-02).

- **Phrasing register — obligation statements (C-16 + C-18)**: Replace "cite if available" and "name the ID" guidance with named MUST/VIOLATION obligation pairs that state the rule, the consequence of violation, and the required artifact format (V-03).

**Combined variations**:

- V-04: Lifecycle emphasis (post-execution promotion) + Role sequence (EG-producing roles first, so promotion always has execution evidence to cite).

- V-05: Full integration — all four new criteria addressed with pre-printed skeletons, mandatory evidence citation, cross-role attribution table, remediation precision template, and inertia framing extended to cover the new criteria.

All five inherit the R6 V-05 architecture: Coverage Matrix with VC compliance columns, PREREQUISITE CHECKPOINTs before each sub-step (C-13), FLOOR CHECK block after Step 3b (C-08/C-15), GATE CLEARANCE SUMMARY at phase boundaries (C-11), C-12 EXEMPTION notice requirement, post-remediation coherence check (C-14).

---

## V-01 — Single axis: Lifecycle emphasis (mandatory execution-evidence citation at SA-TO-SG PROMOTION)

**Axis**: Lifecycle emphasis — SA-TO-SG PROMOTION becomes a post-execution mandatory evidence gate. Promotion decisions that occur after any execution evidence exists are classified as "evidence-grounded" and must cite that evidence. Promotion before execution is classified as "spec-inference" and must state why execution evidence is not yet available.

**Hypothesis**: R6 V-05's "cite execution evidence if post-execution" is conditional. A motivated executor can satisfy the letter by citing spec inference even when execution evidence is present, because the prompt does not define "post-execution" as a structural state. V-01 replaces the conditional with an explicit EVIDENCE CLASSIFICATION block: every SA gap evaluated at SA-TO-SG PROMOTION is classified as evidence-grounded (execution has run before this evaluation) or spec-inference (execution has not yet run). Evidence-grounded gaps must cite execution evidence. Spec-inference gaps must state why the promotion occurs before execution. The classification cannot be omitted. This removes the escape hatch and produces C-16 compliance by making the evidence obligation structurally prior to the promotion decision.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

A valid trace declares all schemas before Stage 1. The Coverage Matrix is the protocol authority: every label, channel, and gate used downstream must be declared here. Anything not declared here is not valid protocol vocabulary.

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b FLOOR CHECK (enforce), Step 3c G-3 (verify), Phase 4 Amend (enforce) | All EG-producing roles | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute role relays | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (run individually), Phase 4 pre-check (enforce composite) | G-1 aggregates Source across all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 prerequisites and transitions | N/A | VC-5 |

**Schema 1**: Valid labels {P1, P2, P3} only. P1 = blocks usefulness; must be resolved before USEFUL verdict. P2 = quality improvement; address in Amend. P3 = advisory; log and continue. No other severity label is valid anywhere in this trace.

**Schema 2**: SA = spec-layer gap. SG = setup gap. EG = execute gap. QO = quality observation. Label lock: once an SA gap is promoted to SG at the SA-TO-SG PROMOTION event, it uses the SG label in every subsequent phase. A promoted gap appearing with SA downstream is a structural violation.

**Schema 3**: spec = fix in the skill spec. invocation = fix in how the skill is called. artifact = fix in the artifact structure. quality = improvement not requiring a spec change. Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 4**: G-1: Step 3b contains >= 2 distinct Source types. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. Any gate defect must be corrected and re-checked; bypassing a FAIL is not valid.

**Schema 5 — Sub-Step Ordering and Prerequisite Protocol**:

| Step | Prerequisite | Produces | Unblocks | Checkpoint required |
|------|-------------|---------|---------|-------------------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b | YES — named artifact: Coverage Matrix Schema 1 row |
| Step 3b | Step 3a complete (checkpoint verified) | Findings table + FLOOR CHECK PASS | Step 3c | YES — named artifact: Step 3a legend table |
| Step 3c | Step 3b FLOOR CHECK PASS (checkpoint verified) | Gate results all PASS | Step 3d | YES — named artifact: Step 3b FLOOR CHECK block |
| Step 3d | Step 3c all-PASS (checkpoint verified) | Channel taxonomy active | Phase 4 | YES — named artifact: Step 3c GATE CLEARANCE SUMMARY |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels applicable, or "N/A — produces no EG findings"] | [Source labels this role may produce; label lock rules if promoted gaps present] | YES / NO | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

A valid Stage 1 produces a gap audit table. Stage 1 reads only `{{skill_spec_path}}`. A Stage 1 audit where all gaps are SA is a warning: the spec is dense enough to supply everything, leaving execution blind spots. At least 2 distinct source types should appear before execution.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>= 2 distinct Source types) / FAIL]
```

---

### Stage 2 — Hand-Compilation

---

#### SA-TO-SG PROMOTION

**Promotion Evidence Classification** (required before evaluating any SA gap):

Every SA gap evaluated at this lifecycle event is classified as one of two evidence states:

- **Evidence-grounded**: Execution has run before this evaluation. At least one EG-producing role has completed its relay. Promotion reason MUST cite specific execution evidence — what the relay produced, what was observed, what was absent. A reason citing only spec inference when execution evidence is available is a structural violation of this criterion.

- **Spec-inference**: Execution has not yet run before this evaluation. Promotion reason must state why (e.g., "evaluated before Phase 2 Execute — no execution evidence available; reasoning from spec structure only").

For each SA gap from Stage 1:

```
SA-NN:
  Gap: [what the spec does not declare]
  Evidence classification: EVIDENCE-GROUNDED / SPEC-INFERENCE
  Evidence classification reason: [if EVIDENCE-GROUNDED: "Execution has run — [role] relay completed above"
                                   if SPEC-INFERENCE: "Evaluated before execution — [reason no execution data available]"]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [if EVIDENCE-GROUNDED: cite the specific execution observation that grounds this decision
           if SPEC-INFERENCE: cite the spec structure that grounds this decision]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original (from Stage 1): {{sg_original}}]
```

Label lock invariant: any promoted gap appearing with its SA label downstream is a structural violation. Verify in VC-2.

---

#### Phase 1 — Setup

A valid Setup produces confirmed input bindings and per-role schema binding for every role. A Setup that lists roles without schema binding and gap attribution is structurally incomplete.

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
  SA/SG gaps binding this role: [list gap IDs or "none — no gaps affect this role at Setup"]
  EG gaps expected for this role: [list gap IDs or "none — confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`], [SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 — Execute

**Execution-first ordering**: EG-producing roles run before SA-only roles. The SA-TO-SG PROMOTION lifecycle event above is positioned to reflect whichever ordering applies to this trace. If PROMOTION is evaluated post-execution, all EG evidence is available for evidence-grounded promotion decisions.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA, SG, EG, QO}: YES / NO
- SA/SG gaps affecting this role: [gap IDs, or "none"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN with severity, or "none — execution completed without EG gaps"]

**Artifact write** (required after all role relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Section confirmation:

  | Section | Status |
  |---------|--------|
  | [required section 1] | WRITTEN |
  | [required section 2] | WRITTEN |

**Execute carry-forward**: [artifact path: `{{artifact_path}}`], [EG gaps added: `{{eg_new}}`].

---

#### Phase 3 — Findings

**Requirement A — PREREQUISITE CHECKPOINT (C-13)**: Each sub-step opens with a PREREQUISITE CHECKPOINT before the sub-step body begins. The checkpoint states the prerequisite, names the specific artifact produced in the prior step, and records CHECK: YES. A bare YES without a named referent is a structural failure.

**Requirement B — FLOOR CHECK (C-15)**: Step 3b closes with a FLOOR CHECK block before advancing to Step 3c. The FLOOR CHECK must: (1) name every finding ID explicitly (not just a count), (2) state row count and confirm >= 3, (3) list every distinct Source type and confirm >= 2, (4) assert Action uniqueness by stating the check result. The FLOOR CHECK must emit PASS or FAIL. A FAIL blocks Step 3c.

---

##### Step 3a — Severity Legend Declaration

> **PREREQUISITE CHECKPOINT — Step 3a**:
> Prerequisite: Schema 1 declared in Coverage Matrix before Stage 1.
> Named artifact: `Coverage Matrix, Schema 1 row — "P1 / P2 / P3", declared at top of this trace`
> Check: YES

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before USEFUL verdict |
| P2 | [what makes it a quality improvement] | Address in Phase 4 Amend |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Severity legend produced. Step 3b is valid to begin.

---

##### Step 3b — Findings Table

> **PREREQUISITE CHECKPOINT — Step 3b**:
> Prerequisite: Step 3a complete and severity legend produced.
> Named artifact: `Step 3a severity legend table, labels P1/P2/P3 defined immediately above`
> Check: YES

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (required before advancing to Step 3c — trace is BLOCKED until PASS):
>
> - Finding IDs present: [list every ID explicitly — e.g., F-01, F-02, F-03. A bare count fails this check.]
> - Row count: [N]. Count >= 3: PASS / FAIL
> - Distinct Source types present: [list each type — e.g., SA, EG]. Count >= 2: PASS / FAIL
> - Action uniqueness: any two Action cells share identical text? [state YES (FAIL) or NO (PASS)]
> - Action uniqueness result: PASS / FAIL
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: identify the deficient dimension, add targeted findings from the underrepresented layer, and re-run this block. Step 3c may not begin until FLOOR CHECK result is PASS.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c — Enforcement Gates

> **PREREQUISITE CHECKPOINT — Step 3c**:
> Prerequisite: Step 3b FLOOR CHECK PASS and findings table populated.
> Named artifact: `Step 3b FLOOR CHECK block, result PASS, finding IDs: [list from FLOOR CHECK above]`
> Check: YES

**G-1 — Source diversity**: Step 3b contains >= 2 distinct Source types.
- Source types present: [list]
- G-1 result: PASS / FAIL

**G-2 — Action uniqueness**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs exist"]
- G-2 result: PASS / FAIL

**G-3 — Severity conformance**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list all used]
- G-3 result: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required before Step 3d begins):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED — Step 3d is valid to begin.
> OR: GATE FAILURE — Step 3d is BLOCKED. Resolve below.

> **REMEDIATION LOG** (required if any gate FAILs on first evaluation):
>
> If all gates PASS on first evaluation, emit:
> "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation loop required."
>
> Gate [X] FAIL:
> - Failure reason: [specific violation]
> - Remediation action: [specific finding ID added or specific Action text changed — "added a finding" fails; "added F-04 (Source: EG, Action: [exact text])" passes]
> - Re-check G-[X]: PASS / FAIL
> - Updated gate result: PASS / FAIL

Schema 5 transition: Step 3c complete (GATE CLEARANCE SUMMARY: ALL GATES CLEARED). Step 3d is valid to begin.

---

##### Step 3d — Channel Taxonomy Activation

> **PREREQUISITE CHECKPOINT — Step 3d**:
> Prerequisite: Step 3c all gates PASS, confirmed by GATE CLEARANCE SUMMARY.
> Named artifact: `Step 3c GATE CLEARANCE SUMMARY, entry verdict "ALL GATES CLEARED", above`
> Check: YES

Schema 3 channel taxonomy is now activated for Phase 4. Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`. Missing = structurally incomplete.

Schema 5 transition: Step 3d complete. Channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active].

---

#### Phase 4 — Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (must reflect post-remediation states — if remediation occurred in Step 3c, this must match the post-remediation results, not the initial FAIL states):
>
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED — Phase 4 is valid to begin.

A valid Amend entry (change):
- [finding: `F-NN`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]

A valid Amend entry (dismissal):
- [finding: `F-NN`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]

---

### Phase 5 — Verdict and VC Compliance Ledger

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must name specific values, label lists, finding IDs, gate results, or section names.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the exact legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS with named IDs | [cite FLOOR CHECK result; list IDs] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used in audit | [list all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Evidence classification assigned; evidence-grounded gaps cite execution evidence | [list SA gaps; state evidence classification and citation for each] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state the Step 3d activation text] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channel per Amend entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three gate results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered after GATE CLEARANCE SUMMARY CLEAR | [cite Phase 4 GATE CLEARANCE SUMMARY verdict] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 cross-role | Step 3b >= 2 Source types; contributing roles identified | [list source types and the specific roles that produced findings of each type] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3a checkpoint | Named artifact: Coverage Matrix Schema 1 row | [exact named artifact from 3a checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b checkpoint | Named artifact: Step 3a legend table | [exact named artifact from 3b checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b FLOOR CHECK | FLOOR CHECK PASS with explicit IDs | [finding IDs from FLOOR CHECK] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3c checkpoint | Named artifact: Step 3b FLOOR CHECK block | [exact named artifact from 3c checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3d checkpoint | Named artifact: Step 3c GATE CLEARANCE SUMMARY | [exact named artifact from 3d checkpoint] | PASS/FAIL |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL | **VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

Classification rules (applied in priority order):
1. `NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
2. `NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
3. `USEFUL` otherwise.

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`
**Rationale**: [one sentence naming the rule that fired and the specific evidence]
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 — Single axis: Output format (pre-printed G-1 cross-role attribution table + remediation precision template)

**Axis**: Output format — two pre-printed structural templates are added. First: the G-1 compliance ledger entry is pre-printed as a two-column attribution table (Source type | Contributing roles). Second: the REMEDIATION LOG entry is pre-printed as a precision template requiring finding ID, Source type, and exact Action text in a named-field format.

**Hypothesis**: R6 V-05's G-1 ledger row is a prose description: "list source types and contributing roles." A model generating this row can satisfy the letter with "SA and EG, contributed by Role A and Role B" — a single sentence that neither structures source types separately nor names which roles contributed which source type. C-17 requires that each Source type be named with the roles that produced it. V-02 pre-prints the G-1 row as a table with `Source type | Contributing roles` columns — the model fills cells rather than generates structure, and the table format forces per-Source-type attribution. The remediation precision template forces the C-18 format by pre-printing `Finding: [F-NN] | Source: [type] | Action: [exact text]` — a model filling this template cannot produce "added a finding."

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

*(Same Coverage Matrix as V-01 — schemas 1 through 5 declared here.)*

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a, Step 3b FLOOR CHECK, Step 3c G-3, Phase 4 Amend | All EG-producing roles | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source column, Execute relays | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d, Phase 4 Amend | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c, Phase 4 pre-check | G-1 aggregates Source across all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 prerequisites and transitions | N/A | VC-5 |

**Schema 1**: {P1, P2, P3} only. P1 blocks usefulness. P2 = quality improvement. P3 = advisory.

**Schema 2**: SA = spec-layer gap. SG = setup gap. EG = execute gap. QO = quality observation. Label lock: promoted gaps use SG label in all phases after SA-TO-SG PROMOTION.

**Schema 3**: Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 4**: G-1: >= 2 distinct Source types in Step 3b. G-2: no two same-Source findings with identical Action. G-3: all Step 3b entries use {P1, P2, P3} only.

**Schema 5 — Sub-Step Ordering and Prerequisite Protocol**:

| Step | Prerequisite | Produces | Unblocks | Checkpoint required |
|------|-------------|---------|---------|-------------------|
| Step 3a | Schema 1 in Coverage Matrix | Severity legend | Step 3b | YES — named artifact: Coverage Matrix Schema 1 row |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c | YES — named artifact: Step 3a legend table |
| Step 3c | Step 3b FLOOR CHECK PASS | Gates all PASS | Step 3d | YES — named artifact: Step 3b FLOOR CHECK block |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 | YES — named artifact: Step 3c GATE CLEARANCE SUMMARY |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels or "N/A"] | [Source labels; label lock rules] | YES / NO | [interactions] |

---

### Stage 1 — Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 — Hand-Compilation

---

#### SA-TO-SG PROMOTION

For each SA gap from Stage 1:

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

---

#### Phase 1 — Setup

Confirmed input bindings:
- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [spec_version: ]

Per-role schema binding and gap attribution:

```
[role: {{role_name}}]
  Schema 1 binding: [labels or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps: [list or "none"]
  EG gaps expected: [list or "none"]
```

---

#### Phase 2 — Execute

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA, SG, EG, QO}: YES / NO
- SA/SG gaps affecting this role: [gap IDs or "none"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN with severity, or "none"]

**Artifact write**:
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Section confirmation:

  | Section | Status |
  |---------|--------|
  | [required section 1] | WRITTEN |

---

#### Phase 3 — Findings

**Requirement A — PREREQUISITE CHECKPOINT**: Each sub-step opens with a checkpoint block. The checkpoint names the specific artifact from the prior step. A bare YES without a named referent fails.

**Requirement B — FLOOR CHECK**: Step 3b closes with a FLOOR CHECK block. The block names every finding ID explicitly, confirms row count >= 3, lists distinct Source types and confirms >= 2, and asserts Action uniqueness.

---

##### Step 3a — Severity Legend Declaration

> **PREREQUISITE CHECKPOINT — Step 3a**:
> Prerequisite: Schema 1 declared in Coverage Matrix.
> Named artifact: `Coverage Matrix, Schema 1 row — "P1 / P2 / P3", declared above`
> Check: YES

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker definition] | Resolve before USEFUL |
| P2 | [quality improvement definition] | Address in Amend |
| P3 | [advisory definition] | Log; no block |

Schema 5 transition: Step 3a complete. Step 3b is valid to begin.

---

##### Step 3b — Findings Table

> **PREREQUISITE CHECKPOINT — Step 3b**:
> Prerequisite: Step 3a complete and severity legend produced.
> Named artifact: `Step 3a severity legend table, P1/P2/P3 defined above`
> Check: YES

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (trace BLOCKED until PASS):
>
> - Finding IDs present: [list every ID — e.g., F-01, F-02, F-03. Bare count fails.]
> - Row count: [N]. Count >= 3: PASS / FAIL
> - Distinct Source types: [list each — e.g., SA, EG]. Count >= 2: PASS / FAIL
> - Action uniqueness: any two Action cells identical? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: add targeted findings, re-run block. Step 3c blocked until PASS.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c — Enforcement Gates

> **PREREQUISITE CHECKPOINT — Step 3c**:
> Prerequisite: Step 3b FLOOR CHECK PASS.
> Named artifact: `Step 3b FLOOR CHECK block, result PASS, IDs: [list from FLOOR CHECK]`
> Check: YES

**G-1**: Source types in Step 3b: [list]. G-1 result: PASS / FAIL

**G-2**: Same-Source pairs examined: [list or "none"]. G-2 result: PASS / FAIL

**G-3**: Severity labels used: [list]. G-3 result: PASS / FAIL

> **GATE CLEARANCE SUMMARY**:
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> ALL GATES CLEARED — Step 3d is valid to begin.
> OR: GATE FAILURE — Step 3d BLOCKED.

> **REMEDIATION LOG** (pre-printed template — fill fields or emit C-12 EXEMPTION):
>
> "C-12 EXEMPTION APPLIES: all gates passed on first evaluation." (emit if no gate fails)
>
> Gate [X] FAIL:
>
> | Field | Value |
> |-------|-------|
> | Finding ID | [F-NN — bare "a finding" fails] |
> | Source type | [SA / SG / EG / QO] |
> | Failure reason | [specific violation text] |
> | Remediation action | [Action text added: "[exact text]" — or Action text changed from "[old]" to "[new]"] |
> | Re-check G-[X] | PASS / FAIL |
> | Updated gate result | PASS / FAIL |

Schema 5 transition: Step 3c complete (ALL GATES CLEARED). Step 3d is valid to begin.

---

##### Step 3d — Channel Taxonomy Activation

> **PREREQUISITE CHECKPOINT — Step 3d**:
> Prerequisite: Step 3c all gates PASS.
> Named artifact: `Step 3c GATE CLEARANCE SUMMARY, "ALL GATES CLEARED", above`
> Check: YES

Schema 3 channel taxonomy activated for Phase 4. Every Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: Step 3d complete. Channel taxonomy active. Phase 4 is valid to begin.

---

#### Phase 4 — Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (post-remediation states — must match Step 3c post-remediation results):
> G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED.

Change entry:
- [finding: F-NN]
- [remediation channel: spec / invocation / artifact / quality]
- [section changed: ]
- [change: ]

Dismissal entry:
- [finding: F-NN]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]

---

### Phase 5 — Verdict and VC Compliance Ledger

"Observed behavior: as expected" is invalid. Every cell must name specific values.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | P1/P2/P3 legend declared | [exact legend text] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b FLOOR CHECK | All P1/P2/P3; FLOOR CHECK PASS with named IDs | [FLOOR CHECK result; IDs listed] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified | [G-3 result and labels] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All entries use P1/P2/P3 | [severity values in Amend] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used | [all Source labels in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; label lock holds | [SA gaps promoted; SG confirmed downstream] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [Source labels; label lock status] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [activation text from Step 3d] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry has channel field | [channel per entry] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 explicit PASS/FAIL | [all three gate results] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered after CLEAR | [Phase 4 GATE CLEARANCE SUMMARY verdict] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 cross-role attribution | Each Source type attributed to contributing roles | **(pre-printed — fill table below)** | PASS/FAIL |
| VC-5 | Schema 5 | Step 3a checkpoint | Named artifact: Coverage Matrix Schema 1 row | [exact named artifact] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b checkpoint | Named artifact: Step 3a legend table | [exact named artifact] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b FLOOR CHECK | FLOOR CHECK PASS with explicit IDs | [finding IDs from FLOOR CHECK] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3c checkpoint | Named artifact: Step 3b FLOOR CHECK block | [exact named artifact] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3d checkpoint | Named artifact: Step 3c GATE CLEARANCE SUMMARY | [exact named artifact] | PASS/FAIL |

**G-1 Cross-Role Attribution Table** (fill for VC-4 G-1 cross-role row — C-17):

| Source type | Contributing roles | Finding IDs of this type |
|-------------|-------------------|--------------------------|
| [SA] | [names of roles that produced SA findings] | [F-NN, F-NN] |
| [EG] | [names of roles that produced EG findings] | [F-NN, F-NN] |
| [add rows for each Source type present] | | |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL | **VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

Classification: `NEEDS-SPEC-REVISION` if P1 SA gap remains SA | `NEEDS-REDESIGN` if EG > 3 structural | `USEFUL` otherwise.

**Verdict**: [classification] — [rationale sentence]
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 — Single axis: Phrasing register (obligation statements for C-16/C-17/C-18)

**Axis**: Phrasing register — every new-criteria obligation is stated as a named MUST/VIOLATION pair that states the rule, the specific consequence of violation, and the required output format. Guidance prose is replaced by obligation statements.

**Hypothesis**: R6 V-05 uses guidance prose at the key C-16/C-17/C-18 sites: "cite execution evidence if post-execution," "list source types and contributing roles," "name the specific ID and change." Guidance prose creates an interpretation space — a model can satisfy the letter while missing the intent. Obligation statements remove interpretation space by naming (1) what is required, (2) what output format satisfies the requirement, and (3) what output fails. A model reading "MUST: cite execution evidence. VIOLATION: 'this gap is probably resolved at runtime' when execution has run fails C-16" cannot produce the violating output without contradicting the explicit VIOLATION statement. This phrasing pattern narrows the compliance gap from interpretation to execution.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Obligations

Before running any phase, read and internalize these obligations. They are not guidelines — they define structural correctness for this trace.

**OBLIGATION — Schema compliance (applies to every phase)**:
MUST: use only {P1, P2, P3} for severity labels and only {SA, SG, EG, QO} for Source labels throughout this trace.
VIOLATION: any label outside these sets, anywhere in the trace, is a structural violation of Schema 1 or Schema 2.

**OBLIGATION — Label lock (applies after SA-TO-SG PROMOTION)**:
MUST: once an SA gap is promoted to SG, it uses the SG label in every subsequent phase.
VIOLATION: a promoted gap appearing with its original SA label in any phase after promotion fails the label lock invariant.

**OBLIGATION — SA-TO-SG PROMOTION evidence citation (C-16)**:
MUST: when evaluating an SA gap at the SA-TO-SG PROMOTION lifecycle event, determine whether execution has already run. If execution has run (at least one role relay has completed before this evaluation), the promotion reason MUST cite specific execution evidence — what the relay observed, produced, or failed to find. Spec inference alone is not sufficient when execution evidence exists.
VIOLATION: "this gap is probably resolved at runtime" or "the spec suggests this will be handled" when execution relay output is available above fails this obligation. The reason must name the specific relay, observation, or produced artifact that grounds the decision.
REQUIRED FORMAT: `Reason: [role name] relay produced [specific observation], which [confirms / fails to confirm] this gap is addressed at runtime.`

**OBLIGATION — Findings floor check (C-15)**:
MUST: after the Step 3b findings table is complete, emit a FLOOR CHECK block that (1) lists every finding ID explicitly, (2) states row count and confirms >= 3, (3) lists every distinct Source type and confirms >= 2, (4) asserts whether any two Action cells are identical.
VIOLATION: advancing to Step 3c without emitting this block, or emitting a block with only a count ("3 findings") without naming the IDs, fails this obligation.

**OBLIGATION — G-1 cross-role attribution (C-17)**:
MUST: the G-1 compliance ledger entry must state, for each Source type present in the Step 3b table, the specific roles that produced findings of that type.
VIOLATION: "SA and EG findings present" without naming which roles contributed SA findings and which roles contributed EG findings fails this obligation.
REQUIRED FORMAT: `Source type [SA]: contributed by [Role A, Role B]. Source type [EG]: contributed by [Role C].`

**OBLIGATION — Remediation entry precision (C-18)**:
MUST: each remediation entry in the REMEDIATION LOG must name the specific finding ID being addressed AND state the exact Action text that was added or changed.
VIOLATION: "added a finding to address G-1" fails. "modified an action" fails.
REQUIRED FORMAT: `Added [F-NN] (Source: [type], Action: "[exact action text]")` or `Changed [F-NN] Action from "[old text]" to "[new text]"`.

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here | Step 3a, Step 3b FLOOR CHECK, Step 3c G-3, Phase 4 | All EG-producing roles | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here | Stage 1, PROMOTION, Step 3b Source, Execute relays | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here | Step 3d, Phase 4 | Phase 4 | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here | Step 3c, Phase 4 | G-1 cross-role | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here | Phase 3 | N/A | VC-5 |

*(Schema definitions: same as V-01/V-02.)*

**Schema 5 — Sub-Step Prerequisite Protocol**:

| Step | Prerequisite | Unblocks | Named artifact required |
|------|-------------|---------|------------------------|
| 3a | Schema 1 in Coverage Matrix | 3b | `Coverage Matrix Schema 1 row` |
| 3b | 3a complete | 3c (after FLOOR CHECK PASS) | `Step 3a legend table` |
| 3c | 3b FLOOR CHECK PASS | 3d | `Step 3b FLOOR CHECK block` |
| 3d | 3c all PASS | Phase 4 | `Step 3c GATE CLEARANCE SUMMARY` |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? |
|------|-----------------|-----------------|---------------|
| [role from spec] | [labels or N/A] | [Source labels] | YES / NO |

---

### Stage 1 — Source-Layer Audit

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: ] [SG: ] [EG: ] [layer diversity: PASS / FAIL]
```

---

### Stage 2 — Hand-Compilation

---

#### SA-TO-SG PROMOTION

**Obligation reminder**: See OBLIGATION — SA-TO-SG PROMOTION evidence citation above. If any role relay has run before this evaluation, the evidence citation requirement applies unconditionally.

For each SA gap from Stage 1:

```
SA-NN:
  Gap: [what the spec does not declare]
  Execution evidence available: YES (relay output above) / NO (pre-execution evaluation)
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [if YES: cite specific relay, observation, or produced artifact per OBLIGATION format
           if NO: cite spec structure and state "pre-execution evaluation"]
```

```
[SA remaining: ] [SG from promotion: ] [SG original: ]
```

---

#### Phase 1 — Setup

Confirmed inputs: [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

Per-role binding:
```
[role: ]
  Schema 1: [labels or N/A]
  Schema 2: [Source labels; label lock rules]
  SA/SG gaps: [list or none]
  EG expected: [list or none]
```

---

#### Phase 2 — Execute

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value]
- Schema 2 compliance: Sources used: [list]. All from {SA,SG,EG,QO}: YES / NO
- SA/SG gaps affecting this role: [IDs or none]
- Produced: [artifact content added]
- EG gaps: [EG-NN with severity, or none]

**Artifact write**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

#### Phase 3 — Findings

**Obligation reminder**: PREREQUISITE CHECKPOINT required before each sub-step. Named artifact required (bare YES fails). FLOOR CHECK required before Step 3c advance.

---

##### Step 3a — Severity Legend

> PREREQUISITE CHECKPOINT — Step 3a: Schema 1 in Coverage Matrix. Named artifact: `Coverage Matrix, Schema 1 row`. Check: YES.

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker] | Resolve before USEFUL |
| P2 | [quality] | Amend |
| P3 | [advisory] | Log |

Schema 5 transition: Step 3a complete. Step 3b valid to begin.

---

##### Step 3b — Findings Table

> PREREQUISITE CHECKPOINT — Step 3b: Step 3a complete. Named artifact: `Step 3a legend, P1/P2/P3 defined above`. Check: YES.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK** (Obligation: MUST emit before advancing — trace BLOCKED until PASS):
>
> Finding IDs present: [list every ID explicitly — obligation states bare count fails]
> Row count: [N] — >= 3: PASS / FAIL
> Source types present: [list] — >= 2: PASS / FAIL
> Action uniqueness: any two Action cells identical? [YES = FAIL / NO = PASS]
> **FLOOR CHECK: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c valid to begin.

---

##### Step 3c — Enforcement Gates

> PREREQUISITE CHECKPOINT — Step 3c: FLOOR CHECK PASS. Named artifact: `Step 3b FLOOR CHECK block, PASS, IDs: [list]`. Check: YES.

G-1: Source types: [list]. Result: PASS / FAIL
G-2: Same-Source pairs: [list or none]. Result: PASS / FAIL
G-3: Severity labels used: [list]. Result: PASS / FAIL

> **GATE CLEARANCE SUMMARY**: G-1: [P/F] | G-2: [P/F] | G-3: [P/F] — ALL GATES CLEARED / BLOCKED.

> **REMEDIATION LOG** (Obligation: if any gate fails, use required precision format):
>
> "C-12 EXEMPTION APPLIES: all gates passed on first evaluation." (if no failures)
>
> Gate [X] FAIL:
> Obligation format — MUST state: finding ID, Source type, exact Action text. "Added a finding" fails.
> - [F-NN added / F-NN Action changed — per OBLIGATION — Remediation entry precision]
> - Re-check G-[X]: PASS / FAIL

Schema 5 transition: Step 3c complete (ALL GATES CLEARED). Step 3d valid to begin.

---

##### Step 3d — Channel Taxonomy Activation

> PREREQUISITE CHECKPOINT — Step 3d: All gates PASS per GATE CLEARANCE SUMMARY. Named artifact: `Step 3c GATE CLEARANCE SUMMARY, ALL GATES CLEARED, above`. Check: YES.

Schema 3 activated. Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: Step 3d complete. Phase 4 valid to begin.

---

#### Phase 4 — Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (post-remediation — must match Step 3c post-remediation results):
> G-1: [P/F] | G-2: [P/F] | G-3: [P/F] — ALL GATES CLEARED.

Change entry: [finding: F-NN] [remediation channel: ] [section changed: ] [change: ]
Dismissal entry: [finding: F-NN] [reason: ] [remediation channel: ]

---

### Phase 5 — Verdict and VC Compliance Ledger

"Observed behavior: as expected" is invalid. Every cell names specific values.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | S1 | Step 3a | P1/P2/P3 legend | [exact text] | P/F |
| VC-1 | S1 | FLOOR CHECK | All P1/P2/P3; PASS with IDs | [result + IDs] | P/F |
| VC-1 | S1 | G-3 | G-3 verified | [result + labels] | P/F |
| VC-1 | S1 | Phase 4 | All entries P1/P2/P3 | [values] | P/F |
| VC-2 | S2 | Stage 1 | SA/SG/EG/QO used | [all Source labels] | P/F |
| VC-2 | S2 | PROMOTION | Evidence citation per OBLIGATION | [citation text for each SA gap; state YES/NO for evidence-grounded] | P/F |
| VC-2 | S2 | Step 3b Source | Label lock holds | [Source labels; promotion label status] | P/F |
| VC-3 | S3 | Step 3d | Taxonomy activated | [activation text] | P/F |
| VC-3 | S3 | Phase 4 | Channel per entry | [channels listed] | P/F |
| VC-4 | S4 | Step 3c | G-1/G-2/G-3 results | [all three] | P/F |
| VC-4 | S4 | Phase 4 | Phase 4 after CLEAR | [verdict] | P/F |
| VC-4 | S4 | G-1 cross-role | Per-Source attribution per OBLIGATION | [Source type [SA]: contributed by [roles]. Source type [EG]: contributed by [roles].] | P/F |
| VC-5 | S5 | 3a checkpoint | Named artifact present | [exact text] | P/F |
| VC-5 | S5 | 3b checkpoint | Named artifact present | [exact text] | P/F |
| VC-5 | S5 | FLOOR CHECK | Explicit IDs | [IDs] | P/F |
| VC-5 | S5 | 3c checkpoint | Named artifact present | [exact text] | P/F |
| VC-5 | S5 | 3d checkpoint | Named artifact present | [exact text] | P/F |

**VC-1**: P/F | **VC-2**: P/F | **VC-3**: P/F | **VC-4**: P/F | **VC-5**: P/F

**Verdict**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION` — [rationale]
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 — Combined: Role sequence + Lifecycle emphasis (post-execution promotion with EG-first ordering)

**Axes**: Role sequence + Lifecycle emphasis.

**Hypothesis**: In R6 V-05, SA-TO-SG PROMOTION is positioned between Stage 1 and Phase 1 Setup — before execution runs. This means the execution-evidence requirement in C-16 is structurally unavailable at the time of promotion, because the relays have not run yet. V-04 restructures the lifecycle: EG-producing roles run first in Phase 2 Execute, then the SA-TO-SG PROMOTION event fires as an explicit gate between Execute and Findings. This makes "execution has run" the definitive state when promotion is evaluated, and the execution-evidence obligation becomes unconditional. The PROMOTION event is a hard lifecycle gate, not an optional sub-step. The role sequence (EG-producing roles first) ensures maximum execution evidence is available before promotion decisions are made.

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

*(Same five schemas as V-01. Schema definitions identical.)*

| Schema | Content | Declared-at | Role-binding | Verdict-check |
|--------|---------|-------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | All EG-producing roles | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | G-1 aggregates Source across all roles | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | N/A | VC-5 |

*(Schema text definitions: identical to V-01.)*

**Schema 5 — Sub-Step Ordering and Prerequisite Protocol**:

| Step | Prerequisite | Produces | Unblocks | Checkpoint required |
|------|-------------|---------|---------|-------------------|
| Step 3a | Schema 1 in Coverage Matrix | Severity legend | Step 3b | YES — named artifact: Coverage Matrix Schema 1 row |
| Step 3b | Step 3a complete | Findings table + FLOOR CHECK PASS | Step 3c | YES — named artifact: Step 3a legend table |
| Step 3c | Step 3b FLOOR CHECK PASS | Gates all PASS | Step 3d | YES — named artifact: Step 3b FLOOR CHECK block |
| Step 3d | Step 3c all-PASS | Channel taxonomy active | Phase 4 | YES — named artifact: Step 3c GATE CLEARANCE SUMMARY |

**Lifecycle sequence for this variation** (differs from standard R6 V-05 ordering):

```
Stage 1 — Source-Layer Audit
Phase 1 — Setup (schema binding; no promotion yet)
Phase 2 — Execute (EG-producing roles first, then SA-only roles)
[LIFECYCLE GATE: SA-TO-SG PROMOTION — fires after all role relays complete]
Phase 3 — Findings (3a → 3b → 3c → 3d)
Phase 4 — Amend
Phase 5 — Verdict
```

The PROMOTION event fires after Execute completes. All promotion decisions are therefore evidence-grounded (execution has run). The "spec-inference" classification from V-01 does not apply here — post-execution promotion is the only mode.

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Sequence position |
|------|-----------------|-----------------|---------------|-------------------|
| [EG-producing role] | [labels] | [Source labels] | YES | FIRST in Phase 2 |
| [SA-only role] | [N/A or labels] | [Source labels] | NO | AFTER EG-producing roles |

---

### Stage 1 — Source-Layer Audit

A valid Stage 1 produces a gap audit table from `{{skill_spec_path}}` only. No role relays run here.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: ] [SG: ] [EG: ] [layer diversity: PASS / FAIL]
```

---

### Phase 1 — Setup

**Note**: SA-TO-SG PROMOTION is NOT evaluated here. Setup produces schema bindings and gap attribution only. Promotion fires after Execute completes.

Confirmed input bindings: [topic: ] [scope_in: ] [scope_out: ] [roles: ] [spec_version: ]

Per-role schema binding and gap attribution (sorted EG-producing first):

```
[role: {{role_name}} — EG-producing: YES/NO]
  Schema 1 binding: [labels or N/A]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps binding this role: [list or none]
  EG gaps expected: [list or none]
  Sequence position in Phase 2: [FIRST — EG-producing / AFTER EG-producing roles — SA-only]
```

**Setup carry-forward**: [topic: `{{topic}}`] [roles sorted for Phase 2: EG-producing first, then SA-only]

---

### Phase 2 — Execute

**EG-producing roles run first**. SA-only roles run after. This ordering ensures the PROMOTION event fires with all execution evidence available.

**Role relay — [EG-producing role name] (FIRST)**:
- Received from: Setup
- Received values: [name: value]
- Schema 2 compliance: Sources used: [list]. All from {SA, SG, EG, QO}: YES / NO
- SA/SG gaps affecting this role: [IDs or none]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN with severity, or none]

**Role relay — [SA-only role name] (AFTER EG-producing roles)**:
- Received from: [prior relay]
- Received values: [name: value]
- Schema 2 compliance: Sources used: [list]. All from {SA, SG, EG, QO}: YES / NO
- SA/SG gaps affecting this role: [IDs or none]
- Produced: [artifact content added]
- EG gaps encountered: [none — SA-only role; EG gaps are not expected]

**Artifact write** (required after all role relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Section confirmation:

  | Section | Status |
  |---------|--------|
  | [required section] | WRITTEN |

---

### LIFECYCLE GATE: SA-TO-SG PROMOTION

**This gate fires after all Phase 2 role relays have completed. Execution evidence is available.**

Every SA gap from Stage 1 is now evaluated with full execution evidence. The promotion reason must cite the specific relay observation that grounds the decision. Reasoning from spec structure alone, when relay output is available above, is a structural violation of this lifecycle gate.

For each SA gap:

```
SA-NN:
  Gap: [what the spec does not declare]
  Execution evidence available: YES — [role] relay completed above
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [cite the specific relay, observation, or produced artifact — e.g., "[Role A] relay
           produced [field X] confirming this gap is addressed; promoted to SG" or "[Role A]
           relay encountered EG-NN at this boundary, confirming gap remains active; REMAINS SA"]
```

```
[SA remaining: ] [SG from promotion: ] [SG original: ]
```

Label lock invariant: promoted gaps use SG in all downstream phases.

---

### Phase 3 — Findings

**Requirement A — PREREQUISITE CHECKPOINT**: Each sub-step opens with a named-artifact checkpoint. Bare YES fails.

**Requirement B — FLOOR CHECK**: Step 3b closes with FLOOR CHECK before Step 3c. Block must list every finding ID explicitly, confirm row count >= 3 and Source count >= 2, and assert Action uniqueness.

---

##### Step 3a — Severity Legend

> PREREQUISITE CHECKPOINT — Step 3a: Schema 1 in Coverage Matrix. Named artifact: `Coverage Matrix, Schema 1 row — P1/P2/P3 declared above`. Check: YES.

| Label | Definition | Actionability |
|-------|-----------|--------------|
| P1 | [blocker] | Resolve before USEFUL |
| P2 | [quality] | Amend |
| P3 | [advisory] | Log |

Schema 5 transition: Step 3a complete. Step 3b valid.

---

##### Step 3b — Findings Table

> PREREQUISITE CHECKPOINT — Step 3b: Step 3a complete. Named artifact: `Step 3a legend table above`. Check: YES.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **FLOOR CHECK** (BLOCKED until PASS):
> Finding IDs: [list every ID]
> Row count: [N] — >= 3: PASS / FAIL
> Source types: [list] — >= 2: PASS / FAIL
> Action uniqueness: identical Actions exist? YES (FAIL) / NO (PASS)
> **FLOOR CHECK: PASS / FAIL**

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c valid.

---

##### Step 3c — Enforcement Gates

> PREREQUISITE CHECKPOINT — Step 3c: FLOOR CHECK PASS. Named artifact: `Step 3b FLOOR CHECK, PASS, IDs: [list]`. Check: YES.

G-1: Source types: [list]. G-1: PASS / FAIL
G-2: Same-Source pairs: [list or none]. G-2: PASS / FAIL
G-3: Severity labels: [list]. G-3: PASS / FAIL

> **GATE CLEARANCE SUMMARY**: G-1: [P/F] | G-2: [P/F] | G-3: [P/F] — ALL GATES CLEARED / BLOCKED.

> **REMEDIATION LOG**:
> "C-12 EXEMPTION APPLIES." (if all pass first evaluation)
> Gate [X] FAIL:
> - Failure: [specific violation]
> - Remediation: [finding ID: F-NN, Source: [type], Action added: "[exact text]"]
> - Re-check: PASS / FAIL

Schema 5 transition: Step 3c complete. Step 3d valid.

---

##### Step 3d — Channel Taxonomy Activation

> PREREQUISITE CHECKPOINT — Step 3d: All gates PASS. Named artifact: `Step 3c GATE CLEARANCE SUMMARY, ALL GATES CLEARED`. Check: YES.

Schema 3 activated. Every Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`.

Schema 5 transition: Step 3d complete. Phase 4 valid.

---

### Phase 4 — Amend

> **PHASE 4 GATE CLEARANCE SUMMARY** (post-remediation states):
> G-1: [P/F] | G-2: [P/F] | G-3: [P/F] — ALL GATES CLEARED.

Change: [finding: F-NN] [channel: ] [section: ] [change: ]
Dismissal: [finding: F-NN] [reason: ] [channel: ]

---

### Phase 5 — Verdict and VC Compliance Ledger

"Observed behavior: as expected" invalid.

| VC | Schema | Usage site | Expected | Observed | Result |
|----|--------|-----------|---------|---------|--------|
| VC-1 | S1 | Step 3a | P1/P2/P3 legend | [exact legend text] | P/F |
| VC-1 | S1 | FLOOR CHECK | All P1/P2/P3; PASS with IDs | [FLOOR CHECK result + IDs] | P/F |
| VC-1 | S1 | G-3 | G-3 verified | [result + labels] | P/F |
| VC-1 | S1 | Phase 4 | All entries P1/P2/P3 | [values] | P/F |
| VC-2 | S2 | Stage 1 | SA/SG/EG/QO in audit | [all labels] | P/F |
| VC-2 | S2 | PROMOTION GATE | Post-execution; execution evidence cited | [for each SA gap: state the relay cited and the observation] | P/F |
| VC-2 | S2 | Step 3b Source | Label lock; promoted = SG | [labels; promotion status] | P/F |
| VC-3 | S3 | Step 3d | Activated | [activation sentence] | P/F |
| VC-3 | S3 | Phase 4 | Channel per entry | [channels] | P/F |
| VC-4 | S4 | Step 3c | G-1/G-2/G-3 explicit | [all three] | P/F |
| VC-4 | S4 | Phase 4 | After CLEAR | [verdict] | P/F |
| VC-4 | S4 | G-1 cross-role | Source types with contributing roles | [list per Source type: Source [type] — roles: [names]] | P/F |
| VC-5 | S5 | 3a checkpoint | Named artifact | [exact text] | P/F |
| VC-5 | S5 | 3b checkpoint | Named artifact | [exact text] | P/F |
| VC-5 | S5 | FLOOR CHECK | Explicit IDs | [IDs] | P/F |
| VC-5 | S5 | 3c checkpoint | Named artifact | [exact text] | P/F |
| VC-5 | S5 | 3d checkpoint | Named artifact | [exact text] | P/F |

**VC totals**: VC-1: P/F | VC-2: P/F | VC-3: P/F | VC-4: P/F | VC-5: P/F

**Verdict**: [classification] — [rationale]
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 — Combined: Full integration (pre-printed skeletons for C-15/C-16/C-17/C-18 + inertia framing)

**Axes**: Output format + Lifecycle emphasis + Inertia framing.

**Hypothesis**: V-01 through V-04 each address one or two of the four new criteria in isolation. V-05 addresses all four simultaneously using pre-printed skeletons — the mechanism that produced the strongest C-13/C-14 compliance in the scout-feasibility golden. Inertia framing from R6 V-05 is extended to cover the new criteria: each phase opens with a sentence stating what a developer would miss without it. Pre-printing the four new criterion structures means the executor transcribes into a fixed form rather than generating structure opportunistically. A model that cannot drop what is already on the page will not fail C-15/C-16/C-17/C-18 through omission.

**Pre-printed structures for the four new criteria**:
- **C-15 (FLOOR CHECK)**: pre-printed four-field block in Step 3b (already in R6 V-05, now confirmed to list all four required checks explicitly)
- **C-16 (execution-evidence promotion)**: pre-printed SA-NN promotion block with mandatory `Execution evidence: [relay name and observation]` field — the field cannot be left blank
- **C-17 (G-1 cross-role attribution)**: pre-printed two-column attribution table in the compliance ledger with Source type and Contributing roles columns
- **C-18 (remediation precision)**: pre-printed remediation entry format in the REMEDIATION LOG requiring `F-NN (Source: [type], Action: "[exact text]")`

---

You are running /trace-inspect for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Why this trace exists

Without running /trace-inspect, the skill contract is hypothetical. You do not know whether the lifecycle phases interact correctly, whether the schemas are sufficient to label all gaps, or whether the artifact produced would be useful to a downstream reviewer. Every structural defect found in this trace is a defect that would otherwise require implementation rework. A skill that cannot be hand-compiled cannot be implemented correctly; the trace either passes or surfaces the reason the spec needs revision first.

This framing has operational consequences for each phase: structural blocks (FLOOR CHECK FAIL, GATE FAILURE, failed PREREQUISITE CHECKPOINT) are not bureaucratic gates — they are signals that the skill design has an unresolved problem. A FAIL at any of these points is a finding, not an inconvenience.

Specific inertia risks for this trace:
- **SA-TO-SG PROMOTION without execution evidence**: A developer who skips this trace writes the spec with a guess about which SA gaps are resolved at runtime. The PROMOTION event with mandatory execution-evidence citation surfaces whether those guesses are correct.
- **Findings table without a floor check**: A developer who stops at two findings has two data points. A findings table with a forced FLOOR CHECK reveals whether the gap coverage across source layers is actually sufficient.
- **G-1 ledger without cross-role attribution**: A developer reviewing the compliance ledger cannot tell which roles contributed which finding types without the attribution table. Cross-role attribution surfaces role design gaps that per-role totals hide.

---

### Trace Protocol Schemas (Coverage Matrix)

| Schema | Content | Declared-at | Referenced-by | Role-binding | Verdict-check |
|--------|---------|-------------|---------------|--------------|---------------|
| Schema 1 — Severity Vocabulary | P1 / P2 / P3 | Here, before Stage 1 | Step 3a (declare), Step 3b FLOOR CHECK (enforce), Step 3c G-3 (verify), Phase 4 (enforce) | All EG-producing roles | VC-1 |
| Schema 2 — Gap Type Taxonomy | SA / SG / EG / QO | Here, before Stage 1 | Stage 1 audit, SA-TO-SG PROMOTION, Step 3b Source column, Execute relays | All roles | VC-2 |
| Schema 3 — Remediation Channel Taxonomy | spec / invocation / artifact / quality | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | Phase 4 amendments | VC-3 |
| Schema 4 — Enforcement Gate Registry | G-1, G-2, G-3 | Here, before Stage 1 | Step 3c (individual + GATE CLEARANCE SUMMARY), Phase 4 pre-check | G-1 cross-role attribution required | VC-4 |
| Schema 5 — Sub-Step Ordering | 3a → 3b → 3c → 3d | Here, before Stage 1 | Phase 3 prerequisite checkpoints + transitions | N/A | VC-5 |

**Schema 1 — Severity Vocabulary**: {P1, P2, P3} only. P1 = blocks usefulness; resolve before USEFUL verdict. P2 = quality improvement; address in Amend. P3 = advisory; log and continue. No other severity label is valid anywhere in this trace.

**Schema 2 — Gap Type Taxonomy**: SA = spec-layer gap. SG = setup gap. EG = execute gap. QO = quality observation. Label lock invariant: once an SA gap is promoted to SG at the SA-TO-SG PROMOTION event, it uses SG in every subsequent phase. A promoted gap retaining SA downstream is a structural violation.

**Schema 3 — Remediation Channel Taxonomy**: Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`. Missing = structurally incomplete.

**Schema 4 — Enforcement Gates**: G-1: Step 3b >= 2 distinct Source types. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. Defects corrected and re-checked; no gate bypassed.

**Schema 5 — Sub-Step Ordering and Prerequisite Protocol**:

| Step | Prerequisite | Produces | Unblocks | Checkpoint required |
|------|-------------|---------|---------|-------------------|
| Step 3a | Schema 1 declared in Coverage Matrix | Severity legend | Step 3b | YES — named artifact: Coverage Matrix Schema 1 row |
| Step 3b | Step 3a complete (checkpoint verified) | Findings table + FLOOR CHECK PASS | Step 3c | YES — named artifact: Step 3a legend table |
| Step 3c | Step 3b FLOOR CHECK PASS (checkpoint verified) | Gate results all PASS | Step 3d | YES — named artifact: Step 3b FLOOR CHECK block |
| Step 3d | Step 3c all-PASS (checkpoint verified) | Channel taxonomy active | Phase 4 | YES — named artifact: Step 3c GATE CLEARANCE SUMMARY |

#### Role-Schema Binding Summary

| Role | Schema 1 binding | Schema 2 binding | EG-producing? | Notes |
|------|-----------------|-----------------|---------------|-------|
| [role from spec] | [severity labels applicable, or "N/A — produces no EG findings"] | [Source labels this role may produce; label lock rules if promoted gaps present] | YES / NO | [Schema 3/4 interactions] |

---

### Stage 1 — Source-Layer Audit

Without Stage 1, you start execution without knowing which spec gaps exist. Gaps that would change the artifact structure surface as EG gaps during execution — discovered too late to influence the spec.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>= 2 distinct Source types) / FAIL]
```

---

### Stage 2 — Hand-Compilation

---

#### SA-TO-SG PROMOTION

Without this event explicitly grounded in execution evidence, promotion decisions remain guesses. A developer who skips the trace promotes SA gaps based on spec reading alone. This event captures whether execution confirmed or contradicted those guesses.

For each SA gap from Stage 1 (pre-printed format — do not omit any field):

```
## SA-NN PROMOTION
Gap: [what the spec does not declare]
Execution evidence: [relay name] relay [produced / encountered / confirmed / failed to produce]
  [specific observation — e.g., "produced a schema-binding block for Role B, confirming this gap
  is addressed at setup time" or "encountered EG-01 at this boundary, confirming gap is active"]
Promotion: PROMOTES TO SG-NN / REMAINS SA
Reason: [cite the specific execution observation above — do not omit the execution evidence field
         and then cite spec structure; this field is required when relay output exists above]
```

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original (from Stage 1): {{sg_original}}]
```

Label lock: promoted gap appears with SA label downstream = structural violation. Verify in VC-2.

---

#### Phase 1 — Setup

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
  Schema 1 binding: [labels or "N/A"]
  Schema 2 binding: [Source labels; label lock rules]
  SA/SG gaps binding this role: [IDs or "none"]
  EG gaps expected: [IDs or "none"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`], [SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 — Execute

**Execution-first ordering**: EG-producing roles run before SA-only roles. This ensures the SA-TO-SG PROMOTION execution evidence field has relay output to cite.

**Role relay — [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- Schema 2 compliance: Source labels used: [list] — all from {SA, SG, EG, QO}: YES / NO
- SA/SG gaps affecting this role: [IDs or "none"]
- Produced: [artifact content added; "no artifact contribution" valid only for support roles]
- EG gaps encountered: [EG-NN with severity, or "none — execution completed without EG gaps"]

**Artifact write** (required after all role relays complete):
- Path: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
- Section confirmation:

  | Section | Status |
  |---------|--------|
  | [required section 1] | WRITTEN |
  | [required section 2] | WRITTEN |

**Execute carry-forward**: [artifact path: `{{artifact_path}}`], [EG gaps added: `{{eg_new}}`].

---

#### Phase 3 — Findings

Without Phase 3, findings are not synthesized into a reviewable form. Without the FLOOR CHECK, a two-finding table can advance to gate evaluation unchallenged.

**Requirement A — PREREQUISITE CHECKPOINT (C-13)**: Each sub-step opens with a PREREQUISITE CHECKPOINT block before the sub-step body begins. The checkpoint names the specific artifact from the prior step and records CHECK: YES. A bare YES without a named referent is a structural failure — the named-artifact field must cite a specific section, table, or block, not a generic path.

**Requirement B — FLOOR CHECK (C-15)**: Step 3b closes with the pre-printed FLOOR CHECK block before advancing to Step 3c. The FLOOR CHECK names every finding ID explicitly, confirms row count >= 3, lists distinct Source types and confirms >= 2, and asserts Action uniqueness. A FAIL result blocks Step 3c — do not omit this block.

---

##### Step 3a — Severity Legend Declaration

> **PREREQUISITE CHECKPOINT — Step 3a** (required before this sub-step body — do not omit):
> Prerequisite: Schema 1 declared in Coverage Matrix before Stage 1.
> Named artifact: `Coverage Matrix, Schema 1 row — "P1 / P2 / P3", declared at top of this trace`
> Check: YES

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [what makes a finding a blocker in this trace] | Resolve before USEFUL verdict |
| P2 | [what makes it a quality improvement] | Address in Phase 4 Amend |
| P3 | [what makes it advisory] | Log; no gate impact |

Schema 5 transition: Step 3a complete. Severity legend produced. Step 3b is valid to begin.

---

##### Step 3b — Findings Table

> **PREREQUISITE CHECKPOINT — Step 3b** (required — do not omit):
> Prerequisite: Step 3a complete and severity legend produced.
> Named artifact: `Step 3a severity legend table, labels P1/P2/P3 defined immediately above`
> Check: YES

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

> **STEP 3b FLOOR CHECK** (pre-printed — fill all four fields — trace BLOCKED until PASS):
>
> - Finding IDs present: [list every ID explicitly — e.g., F-01, F-02, F-03. Do not omit this line. A bare count fails.]
> - Row count: [N]. Count >= 3: PASS / FAIL
> - Distinct Source types present: [list each type]. Count >= 2: PASS / FAIL
> - Action uniqueness: any two Action cells share identical text? YES (FAIL) / NO (PASS)
>
> **FLOOR CHECK result: PASS / FAIL**
>
> If FAIL: identify the deficient dimension, add targeted findings from the underrepresented layer, re-run this block. Step 3c may not begin until FLOOR CHECK PASS.

Schema 5 transition: Step 3b complete (FLOOR CHECK PASS). Step 3c is valid to begin.

---

##### Step 3c — Enforcement Gates

> **PREREQUISITE CHECKPOINT — Step 3c** (required — do not omit):
> Prerequisite: Step 3b FLOOR CHECK PASS and findings table populated.
> Named artifact: `Step 3b FLOOR CHECK block, result PASS, finding IDs: [list from FLOOR CHECK above]`
> Check: YES

**G-1 — Source diversity**: Step 3b contains >= 2 distinct Source types.
- Source types present: [list]
- G-1 result: PASS / FAIL

**G-2 — Action uniqueness**: No two same-Source findings share identical Action text.
- Same-Source pairs examined: [list or "no same-Source pairs exist"]
- G-2 result: PASS / FAIL

**G-3 — Severity conformance**: All Step 3b entries use only {P1, P2, P3}.
- Severity labels present: [list all labels used]
- G-3 result: PASS / FAIL

> **GATE CLEARANCE SUMMARY** (required structural block — do not omit):
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Entry verdict: ALL GATES CLEARED — Step 3d is valid to begin.
> OR: GATE FAILURE — Step 3d is BLOCKED. Resolve below.

> **REMEDIATION LOG** (pre-printed precision template — fill or emit EXEMPTION notice):
>
> If all gates PASS on first evaluation, emit: "C-12 EXEMPTION APPLIES: all gates passed on first evaluation. No remediation loop required."
>
> Gate [X] FAIL:
> - Failure reason: [specific violation text]
> - Remediation action (pre-printed format — do not paraphrase):
>   Added [F-NN] (Source: [SA/SG/EG/QO], Severity: [P1/P2/P3], Action: "[exact action text added]")
>   OR Changed [F-NN] Action from "[old action text]" to "[new action text]"
> - Re-check G-[X]: PASS / FAIL
> - Updated gate result: PASS / FAIL

Schema 5 transition: Step 3c complete (GATE CLEARANCE SUMMARY: ALL GATES CLEARED). Step 3d is valid to begin.

---

##### Step 3d — Channel Taxonomy Activation

> **PREREQUISITE CHECKPOINT — Step 3d** (required — do not omit):
> Prerequisite: Step 3c all gates PASS, confirmed by GATE CLEARANCE SUMMARY.
> Named artifact: `Step 3c GATE CLEARANCE SUMMARY, entry verdict "ALL GATES CLEARED", above`
> Check: YES

Schema 3 channel taxonomy is now activated for Phase 4. Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`. Missing = structurally incomplete and fails VC-3.

Schema 5 transition: Step 3d complete. Channel taxonomy active. Phase 4 is valid to begin.

---

**Findings carry-forward**: [highest finding: `{{F-NN}}`], [G-1: PASS], [G-2: PASS], [G-3: PASS], [channel taxonomy: active from Step 3d].

---

#### Phase 4 — Amend

Without Phase 4, findings have no disposition. A finding without an amendment or dismissal is an unresolved signal — it cannot be traced to a spec change or a deliberate acceptance decision.

> **PHASE 4 GATE CLEARANCE SUMMARY** (pre-printed — post-remediation states — do not omit; must match Step 3c post-remediation results, not initial evaluation states):
>
> G-1: [PASS / FAIL] | G-2: [PASS / FAIL] | G-3: [PASS / FAIL]
> Phase 4 entry verdict: ALL GATES CLEARED — Phase 4 is valid to begin.
> OR: GATE FAILURE — Phase 4 BLOCKED. Return to Step 3c.

A valid Amend entry (change):
- [finding: `F-NN`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]

A valid Amend entry (dismissal):
- [finding: `F-NN`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]

---

### Phase 5 — Verdict and VC Compliance Ledger

Without the compliance ledger, the VC results are asserted rather than traced. A developer reading the verdict cannot verify that every schema invariant was checked at every declared usage site.

"Observed behavior: as expected" is structurally invalid. Every Observed-behavior cell must name specific values, label lists, finding IDs, gate results, or section names. Generic observations fail the VC row.

| VC | Schema | Usage site | Expected behavior | Observed behavior | Result |
|----|--------|-----------|------------------|------------------|--------|
| VC-1 | Schema 1 | Step 3a | Severity legend P1/P2/P3 declared | [name the exact legend text produced] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3b FLOOR CHECK | All entries P1/P2/P3; FLOOR CHECK PASS with named IDs | [cite FLOOR CHECK result; list IDs] | PASS/FAIL |
| VC-1 | Schema 1 | Step 3c G-3 | G-3 verified against Schema 1 | [state G-3 result and all labels checked] | PASS/FAIL |
| VC-1 | Schema 1 | Phase 4 Amend | All Amend entries use only P1/P2/P3 | [list severity values in all Amend entries] | PASS/FAIL |
| VC-2 | Schema 2 | Stage 1 | SA/SG/EG/QO labels used in audit | [list all Source labels present in Stage 1] | PASS/FAIL |
| VC-2 | Schema 2 | SA-TO-SG PROMOTION | Promoted gaps receive SG; execution evidence cited per pre-printed field | [for each SA gap: state the relay cited and the specific observation recorded in the Execution evidence field] | PASS/FAIL |
| VC-2 | Schema 2 | Step 3b Source column | Only SA/SG/EG/QO; promoted gaps show SG | [list Source labels; confirm label lock for promoted gaps] | PASS/FAIL |
| VC-3 | Schema 3 | Step 3d | Channel taxonomy activated | [state the Step 3d activation text] | PASS/FAIL |
| VC-3 | Schema 3 | Phase 4 Amend | Every entry includes channel field | [list channel per Amend entry; flag any missing] | PASS/FAIL |
| VC-4 | Schema 4 | Step 3c | G-1/G-2/G-3 checked with explicit PASS/FAIL | [state all three gate results from Step 3c] | PASS/FAIL |
| VC-4 | Schema 4 | Phase 4 pre-check | Phase 4 entered after GATE CLEARANCE SUMMARY CLEAR | [cite Phase 4 GATE CLEARANCE SUMMARY verdict] | PASS/FAIL |
| VC-4 | Schema 4 | G-1 cross-role attribution | Each Source type attributed to the roles that produced it | **(pre-printed table — fill below)** | PASS/FAIL |
| VC-5 | Schema 5 | Step 3a checkpoint | Named artifact: Coverage Matrix Schema 1 row | [exact named artifact from 3a checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b checkpoint | Named artifact: Step 3a legend table | [exact named artifact from 3b checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3b FLOOR CHECK | FLOOR CHECK PASS with explicit finding IDs | [all finding IDs from FLOOR CHECK block] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3c checkpoint | Named artifact: Step 3b FLOOR CHECK block | [exact named artifact from 3c checkpoint] | PASS/FAIL |
| VC-5 | Schema 5 | Step 3d checkpoint | Named artifact: Step 3c GATE CLEARANCE SUMMARY | [exact named artifact from 3d checkpoint] | PASS/FAIL |

**G-1 Cross-Role Attribution Table** (pre-printed — fill Source types and contributing roles — do not omit):

| Source type present in Step 3b | Contributing roles | Finding IDs of this type |
|-------------------------------|-------------------|--------------------------|
| [fill row per Source type, e.g., SA] | [names of roles that produced SA findings in Phase 2] | [F-NN, F-NN] |
| [fill row per Source type, e.g., EG] | [names of roles that produced EG findings] | [F-NN, F-NN] |

**VC-1 overall**: PASS / FAIL | **VC-2 overall**: PASS / FAIL | **VC-3 overall**: PASS / FAIL | **VC-4 overall**: PASS / FAIL | **VC-5 overall**: PASS / FAIL

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

| ID | Axis(es) | C-15 mechanism | C-16 mechanism | C-17 mechanism | C-18 mechanism |
|----|----------|---------------|---------------|---------------|---------------|
| V-01 | Lifecycle emphasis | FLOOR CHECK block (4-field) in Step 3b | Evidence-classification block: EVIDENCE-GROUNDED / SPEC-INFERENCE classification required before promotion reason | G-1 ledger row prose: "list source types and contributing roles" | Remediation log: named ID + exact Action required |
| V-02 | Output format | FLOOR CHECK block (4-field) — same as R6 V-05 | Reason field: permissive "if post-execution" | Pre-printed G-1 attribution table with Source type / Contributing roles columns | Pre-printed remediation precision template: `F-NN | Source: [type] | Action: [exact text]` |
| V-03 | Phrasing register | OBLIGATION: MUST emit block; VIOLATION: bare count fails | OBLIGATION: MUST cite execution evidence when execution has run; VIOLATION: spec inference when evidence available fails | OBLIGATION: per-Source attribution; VIOLATION: single-sentence summary fails | OBLIGATION: named F-NN + Action text; VIOLATION: "added a finding" fails |
| V-04 | Role sequence + Lifecycle emphasis | FLOOR CHECK block (4-field) — same as R6 V-05 | PROMOTION fires as post-Execute LIFECYCLE GATE; evidence always available; citation unconditional | G-1 ledger row prose: "list per Source type with roles" | Remediation log: ID + exact Action required |
| V-05 | Full integration | Pre-printed FLOOR CHECK 4-field block; "do not omit" reinforcement | Pre-printed SA-NN block with mandatory `Execution evidence:` field that cannot be left blank | Pre-printed G-1 cross-role attribution table with Source type + Contributing roles + Finding IDs columns | Pre-printed remediation precision template: `Added F-NN (Source: [type], Action: "[exact text]")` |

**C-15 predicted pass**: V-01 (PASS — 4-field explicit block), V-02 (PASS — pre-printed block), V-03 (PASS — OBLIGATION enforces all four fields), V-04 (PASS — block present), V-05 (PASS — pre-printed + "do not omit").

**C-16 predicted pass**: V-01 (PASS — evidence classification removes escape hatch), V-02 (PARTIAL — permissive "if post-execution" language survives), V-03 (PASS — VIOLATION statement names the prohibited form), V-04 (PASS — post-execution gate makes citation unconditional), V-05 (PASS — pre-printed mandatory `Execution evidence:` field).

**C-17 predicted pass**: V-01 (PARTIAL — prose instruction "list source types and roles"), V-02 (PASS — pre-printed table forces per-Source-type row), V-03 (PASS — OBLIGATION + VIOLATION pair), V-04 (PARTIAL — prose instruction), V-05 (PASS — pre-printed table with three columns).

**C-18 predicted pass**: V-01 (PASS — explicit precision language), V-02 (PASS — pre-printed template), V-03 (PASS — VIOLATION names exact failing forms), V-04 (PASS — explicit precision language), V-05 (PASS — pre-printed format with named fields + "do not paraphrase").

**Combined C-15/C-16/C-17/C-18 predicted pass**: V-03, V-05 only. V-01 PARTIAL on C-17. V-02 PARTIAL on C-16. V-04 PARTIAL on C-17.

**Regression risk on existing criteria**: All five inherit the R6 V-05 architecture for C-01 through C-14. V-04 restructures the lifecycle (PROMOTION moved to post-Execute) — verify C-01 phase completeness and C-06 SA-TO-SG evaluation are not disrupted by the reordering.

**Recommended R7 candidate**: V-05 predicted to achieve full C-15/C-16/C-17/C-18 PASS with no regression. V-03 is the strongest single-axis challenger. V-02 is the pre-printing approach extended to C-17/C-18 (strong structural guarantees on those two, weaker on C-16).
