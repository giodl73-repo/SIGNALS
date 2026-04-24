---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 4
rubric: trace-skill-rubric-v4-2026-03-15.md
---

# trace-skill -- Variations R4 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

Round 4 target: C-13/C-14/C-15/C-16 -- the four new v4 aspirational criteria.

R3 V-04 hit 100 under v4 via full two-stage architecture: diversity-first auditor + structured relay
+ SA-to-SG re-labeling + per-role gap attribution + distinct action directions. Round 4 explores
alternative structural paths to the same ceiling:
- V-01: output format (gap propagation matrix threads each gap from discovery through phases)
- V-02: phrasing register (type-system metaphor for SA-to-SG promotion; typed gap manifest)
- V-03: lifecycle emphasis (compact pre-audit preamble embedded in Setup, not a separate stage)
- V-04: extends R3 V-04 with named C-15 enforcement (SA-to-SG Promotion event) + named C-16
  enforcement (Action Diversity Check step)
- V-05: inertia framing + per-role gap relay tables making C-14 structurally enforced

Single-axis selections: Output format (V-01), Phrasing register (V-02), Lifecycle emphasis (V-03).
Combined selections: Role sequence + lifecycle emphasis (V-04), Inertia framing + role sequence (V-05).

---

## V-01 -- Single axis: Output format (gap propagation matrix)

**Axis**: Output format -- a "gap propagation matrix" is the structural spine of the trace.
Every gap detected at any phase is a row in this matrix. The matrix carries each gap from its
discovery layer through Setup, Execute, and Findings, with a dedicated `Promoted?` column that
records whether an SA gap was re-typed as SG at the Setup boundary. Per-role attribution becomes
a column in the matrix (`Roles affected`). Source labeling in Findings maps back to the matrix
ID. The matrix does not replace the four phases -- each phase writes into it.

**Hypothesis**: A shared matrix that every phase writes into makes C-13, C-14, C-15, and C-16
structural: the `Promoted?` column enforces C-15 (SA-to-SG re-labeling), the `Roles affected`
column enforces C-14 (per-role attribution), the matrix header is the structured relay (C-13),
and the matrix construction rules enforce distinct action directions (C-16). Risk: the matrix
may become mechanical -- phases write rows to satisfy column requirements rather than performing
genuine gap reasoning. If the tracer fills `Roles affected` with generic role names rather than
specific attribution, C-14 degrades to label coverage without diagnostic value.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Gap Propagation Matrix

Open this matrix before reading the spec. Every gap you discover at any phase is added here as
a new row. Do not fill the matrix by reviewing prior phases at the end -- add rows as you find
them.

| ID | Gap | Discovery phase | Source | Severity | Roles affected | Promoted? | Action |
|----|-----|-----------------|--------|----------|----------------|-----------|--------|

**Source vocabulary**: SA (spec does not define this) / SG (input unavailable at runtime) /
EG (required artifact section or role output missing) / QO (quality observation)

**Promoted?** column -- fill this during Setup:
- For SA rows discovered in the pre-audit: write `SA → SG-NN` if the gap is invocation-level
  at Setup time, or `SA (remains SA)` if it is a spec defect the invoker cannot resolve.
- For SG and EG rows: write `n/a`.

**Roles affected** column -- fill this during Setup or Execute:
- Name the specific role(s) whose execution is constrained by this gap.
- Write `none` only if you have verified the gap does not affect any executing role.

**Matrix construction rules**:
1. Each row must have a distinct Action. Two rows with the same Source and same Action must be
   merged into one row -- if you cannot merge them without losing information, they carry
   distinct gaps and require distinct Action text.
2. Minimum 2 rows with at least 2 distinct Source types must exist before Findings closes.
3. Action text must name a component, section, or decision point -- not just "update the spec"
   or "fix the artifact".

---

### Phase 1 -- Pre-Audit (spec-first scan)

Read `{{skill_spec_path}}` before touching the test invocation. Populate the Gap Propagation
Matrix with spec-level gaps (SA) and any structurally predictable setup gaps (SG):

- Are all inputs to the skill fully defined in the spec? (undefined inputs = SA-NN)
- Is the role sequence and each role's input/output contract specified? (undefined handoffs = SA-NN)
- Does the spec define every required artifact section and the naming convention? (undefined
  sections = SA-NN)
- Are there setup-level inputs the spec defines but that likely cannot be derived from the
  invocation alone? (predictable setup gaps = SG-NN)

Add each gap as a row. Record `Discovery phase = Pre-Audit`. Leave `Promoted?` blank -- fill
during Setup.

**Pre-Audit relay** (fill after scanning):

```
[SA gaps: {{sa_list}}]
[SG gaps: {{sg_list}}]
[EG gaps: none -- execute not run yet]
[layer diversity: PASS (2+ distinct source types in matrix) / FAIL (single source type)]
```

---

### Phase 2 -- Setup

Read the pre-audit relay above. For each SA row in the matrix: fill the `Promoted?` column now.

**SA-to-SG promotion rule**: An SA gap that identified an undefined spec input is a spec defect.
When you reach Setup, ask: does the invoker have this input available regardless of the spec gap?
If YES, re-label it SG-NN (runtime constraint) -- the spec is defective but the invoker can
supply the value. Write `SA-01 → SG-01` in the `Promoted?` column. If NO, the gap remains SA
(spec must be fixed before implementation is possible). Write `SA (remains SA)`.

Fill Setup inputs using `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] ([detection_method: ])
- [spec_version: ]

For each role enumerated in `[roles: ...]`, fill the `Roles affected` column in the matrix for
every gap that constrains that role's execution. If no gaps affect a role, add a note next to
the role: "no gaps".

**Carry forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
matrix updated -- SA promotions complete, Roles affected filled.

---

### Phase 3 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the skill spec defines must appear. Run each role in sequence. For each role:

1. State what the role received (from Setup or prior role output)
2. State what the role contributed to the artifact
3. For any required output the role cannot produce: add an EG-NN row to the matrix with
   `Roles affected = [this role]`, then mark the artifact section `[EG-NN: reason]` and continue

Do not infer silently. Every gap discovered here becomes a matrix row before proceeding to the
next role.

**Carry forward**: [artifact: `{{artifact_path}}`], matrix updated -- EG rows added.

---

### Phase 4 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], gap matrix complete.

The findings table is derived from the matrix. Copy matrix rows into the findings table, using
the promoted Source label (SG, not SA, for any promoted gaps):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Before closing Findings, apply the construction rules:
- Check: at least 2 distinct Source types present? If not, identify a gap from the missing layer.
- Check: no two same-Source rows carry identical Action text. If a collision exists, differentiate
  the Action text to name distinct components or revise one finding.

Record: `[layers covered: {{source_types}}]`

**Carry forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

---

### Phase 5 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

Apply the finding. Required fields:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (use promoted label -- SG if the original SA was promoted)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [source type confirmed: YES / NO -- was the Source label accurate?]

---

### Verdict

**Matrix summary**: SA rows: [count] (promoted: [count], remains SA: [count]) |
SG rows: [count] | EG rows: [count] | QO rows: [count]
**Layer diversity**: [from pre-audit relay]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA row remains SA after promotion check (not promotable).
`NEEDS-REDESIGN` if EG rows exceed 3 and cluster on a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-02 -- Single axis: Phrasing register (type-system metaphor for gap taxonomy)

**Axis**: Phrasing register -- the gap taxonomy is presented as a type system: SA is an
"unresolved type" (the spec does not declare this value), SG is a "binding failure" (the type
is declared in the spec but the runtime cannot bind the value), EG is a "contract violation"
(the artifact contract requires a section that the role cannot produce). The pre-audit produces
a "gap type manifest" and the SA-to-SG re-labeling is called a "type promotion." Per-role
attribution is called "gap binding per role." The language is formal and precise throughout;
every transition uses typed carry-forward notation.

**Hypothesis**: A type-system metaphor makes the SA-to-SG promotion conceptually precise
(C-15): SA is a declaration gap -- the spec did not declare the type; SG is a binding gap --
the spec declared it but the runtime cannot instantiate it. These are genuinely different
failure modes, and the type-system vocabulary makes the distinction unambiguous. Risk: the
metaphor may be unfamiliar to tracers expecting lifecycle language; if the vocabulary is not
absorbed, per-role "gap binding" may be treated as optional decoration. The relay record
structure (C-13) maps cleanly to a typed manifest, but the per-role attribution (C-14) requires
the tracer to actively enumerate bindings per role, which may produce shallow entries.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Stage 1 -- Gap Type Auditor

Your role here is a **type auditor**. You are not running the skill -- you are constructing
the gap type manifest before any execution begins.

**Gap types**:

| Type | Meaning | Remediation channel |
|------|---------|-------------------|
| SA (Spec Absent) | The spec does not declare this value, input, or contract | Spec must declare it before implementation |
| SG (Setup Gap) | The spec declares it; the runtime invocation cannot bind it | Invocation or documentation change |
| EG (Execute Gap) | The artifact contract requires this section; the role cannot produce it | Skill implementation or role definition change |
| QO (Quality Observation) | No type failure; artifact improvable | Advisory |

Read `{{skill_spec_path}}`. Audit for type failures across all three type categories:

**SA audit** -- scan for undeclared values:
- Are all required inputs declared in the spec with their type, source, and format?
- Is the role sequence declared (order + handoff contracts)?
- Is the artifact contract fully declared (every required section, naming convention,
  content rules)?

**SG pre-audit** -- scan for predictable binding failures:
- Which declared inputs are unlikely to be derivable from the test invocation alone?

**EG pre-audit** -- scan for predictable contract violations:
- Are there artifact sections the spec requires that the defined roles may not be able to
  produce as specified?

Produce the **gap type manifest**:

```
[SA: {{sa_list}}]         -- undeclared values in the spec
[SG: {{sg_list}}]         -- predicted binding failures
[EG: {{eg_list}}]         -- predicted contract violations
[layer diversity: PASS (2+ distinct types) / FAIL (single type)]
```

**Auditor rule**: the manifest is complete when at least two distinct gap types appear.
If only one type is present after careful scanning, examine the spec's role handoff contracts
for SA candidates and the invocation context for SG candidates before declaring the audit done.

---

### Stage 2 -- Hand-Compilation

**Manifest received from Stage 1**:
`[SA: {{sa_list}}]`, `[SG: {{sg_list}}]`, `[EG: {{eg_list}}]`,
`[layer diversity: {{diversity_status}}]`

---

#### Phase 1 -- Setup (type promotion)

Using the test invocation and repo context. Declare confirmed bindings using `[name: value]`
notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**SA-to-SG type promotion**: For each SA item in the manifest, evaluate at Setup time:

> Does the invoker have the information to bind this value at runtime, even though the spec
> does not declare it?

- YES: promote to SG. Write `SA-NN promotes to SG-NN: [reason]`.
  The binding gap is now the invoker's responsibility; the spec gap remains but is not
  blocking at runtime.
- NO: remains SA. Write `SA-NN (remains SA): [reason]`.
  Implementation cannot proceed until the spec declares this value.

**Gap binding per role**: For each role in `[roles: ...]`, enumerate which manifest items
(SA, SG, or EG) constrain this role's execution. Write:

```
[role: {{role_name}}] binds: [SA/SG items] | contract violations: [EG items] | unaffected: [confirmed]
```

A role entry with no binding annotation does not pass -- write "no gaps bind this role" if
that is genuinely the case.

**Carry forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA_promoted: `{{promoted_list}}`], [SG: `{{sg_list}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the artifact contract declares must appear. Run each role in sequence.
Before each role writes its artifact section, state the gap bindings it carries from Setup.
Where a role hits a contract violation: add EG-NN to the manifest, mark the artifact section
`[EG-NN: contract violated -- reason]`, and continue. Do not bind a value not in scope.

**Carry forward**: [artifact: `{{artifact_path}}`], [EG_added: `{{eg_new_list}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], full manifest `[SA: ...][SG: ...][EG: ...]`.

Produce the findings table. Source column must use the promoted type label (SG, not SA, for
any promoted gaps). Entries that share a Source type must carry **distinct remediation channels**
-- not just distinct wording, but pointing at distinct spec sections, invocation parameters,
or artifact sections. If two same-Source entries converge on the same remediation target:
revise one to identify a distinct failure within that type.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Action diversity check**: Before proceeding, review all same-Source pairs. For each pair:
are the Action fields pointing at different remediation targets? If not, differentiate them.

**Carry forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

---

#### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

Apply the finding. Required fields:

- [finding: `{{F-NN}}`]
- [type: `{{source}}`] (use promoted type label)
- [remediation channel: spec / invocation / artifact / quality]
- [change: ]
- [type confirmed: YES -- remediation targets the `{{source}}` channel / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [type label confirmed: YES (the type assignment was correct) / NO (needs re-typing)]

---

### Verdict

**Gap type manifest (final)**:
`[SA (remains): {{count}}]` `[SA (promoted to SG): {{count}}]` `[SG: {{count}}]`
`[EG: {{count}}]` `[QO: {{count}}]`
**Layer diversity**: [from Stage 1 manifest]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion (spec must be revised first).
`NEEDS-REDESIGN` if EG contract violations exceed 3 and cluster on a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (compact pre-audit preamble embedded in Setup)

**Axis**: Lifecycle emphasis -- the pre-execution audit is not a separate Stage 1; it is a
mandatory preamble block inside Phase 1 (Setup). Setup opens with "SPEC AUDIT" as a named
sub-step that produces the structured relay record before any input confirmation begins. SA-to-SG
promotion happens immediately after the spec audit, within Setup, before roles are enumerated.
Per-role gap attribution follows promotion, also within Setup. The lifecycle is still four phases
(Setup, Execute, Findings, Amend), but Setup carries the full audit+promotion+attribution work
that R3 V-04 placed in a separate Stage 1.

**Hypothesis**: Embedding the pre-audit preamble in Setup rather than making it a separate stage
removes the two-stage overhead while preserving all four new criteria. C-08 can be satisfied by
a named preamble sub-step inside Setup as long as it produces a distinct pre-phase output
referenced later. C-13 requires the relay record to be addressable; a preamble block inside
Setup can produce it. C-14 and C-15 are naturally satisfied if per-role attribution and SA
promotion happen within the same Setup section. Risk: the C-08 pass condition requires the
pre-phase audit to occur "before Setup runs" -- embedding it inside Setup may technically fail
C-08 if the rubric interprets "before Setup" strictly. If Setup is treated as the entire section
including its preamble, C-08 should pass; if C-08 requires a separate stage header, it will not.
This variation tests that boundary.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Phase 1 -- Setup

---

#### Preamble: Spec Audit (read spec before reading invocation)

Read `{{skill_spec_path}}` before consulting the test invocation. Audit for gaps:

**Spec-level gaps (SA)** -- things the spec does not declare:
- Undefined inputs (no declared source, type, or format): SA-NN
- Undefined role handoff contracts (role receives what?): SA-NN
- Undefined artifact sections or naming rules: SA-NN

**Predictable setup gaps (SG)** -- inputs the spec declares but the invocation probably cannot provide:
- SG-NN

**Predictable execute gaps (EG)** -- artifact sections the defined roles may structurally fail to produce:
- EG-NN

**Pre-audit relay record**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (2+ distinct types detected) / FAIL (single type only)]
```

The relay record is frozen here. Downstream phases key off these named fields.

---

#### SA-to-SG Promotion

For each SA gap in the relay record, evaluate now whether it becomes a setup-level constraint:

> At invocation time, can the invoker supply this value even though the spec does not declare it?

- YES: write `SA-NN promotes to SG-NN`. In the rest of this trace, use the SG label.
- NO: write `SA-NN remains SA`. This is a spec defect; implementation cannot proceed until
  the spec declares this value.

Promotion rule: SA that promotes to SG shifts the gap from "spec must be fixed" to "invoker
must supply this value." Both are real gaps -- the difference is who acts and when.

---

#### Input Confirmation

Using the test invocation and repo context. Record confirmed values:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] ([detection_method: ])
- [spec_version: ]

Any input not confirmable: label SG-NN. Do not infer silently.

---

#### Role Gap Attribution

For each role in `[roles: ...]`, list which gaps from the relay record affect its execution:

- **[Role name]**: SA gaps (or promoted SG) affecting this role: [list or "none"] |
  EG gaps (contract violations this role may hit): [list or "none"]

A role entry without gap attribution does not pass -- write "no gaps affect this role" if
confirmed.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA_promoted: `{{promoted}}`], [SG: `{{sg_list}}`], relay record above.

---

### Phase 2 -- Execute

Carrying forward from Setup: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the spec defines must appear. Run each role in sequence. For each role:

1. State what the role received (Setup outputs or prior role output)
2. State what the role contributed to the artifact
3. Where a role cannot produce a required section: add EG-NN to the running gap list, mark
   the artifact section `[EG-NN: reason]`, and continue

Do not infer silently. New EG gaps discovered here are labeled with numbers continuing from
the relay record sequence.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], relay record gaps + EG gaps from Execute.

Merge all gaps into the findings table. Use promoted Source labels (SG, not SA, for
promoted gaps):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Requirements before proceeding to Amend:

1. At least 2 entries; at least 2 distinct Source types.
2. **Action diversity**: for any two rows that share the same Source label, verify their
   Action fields name distinct spec sections, invocation parameters, or artifact sections.
   If they do not, revise until they are distinct -- same-Source rows with identical Action
   text are redundant, not informative.
3. Record: `[layers covered: {{source_types}}]`

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

---

### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label)
- [section changed: ]
- [change: ]
- [source confirmed: YES -- fix targets the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:
- [finding: `{{F-NN}}`]
- [dismissal reason: ]
- [source type confirmed: YES / NO]

---

### Verdict

**Relay record** (from Setup preamble):
`[SA: {{count}}]` `[SG: {{count}}]` `[EG: {{count}}]` `[layer diversity: {{status}}]`

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion check.
`NEEDS-REDESIGN` if EG gaps exceed 3 and cluster on a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-04 -- Combined axes: Role sequence (diversity-first auditor) + lifecycle emphasis (named C-15 and C-16 enforcement steps)

**Axes**:
- Role sequence: two-stage architecture from R3 V-04 -- spec-layer auditor (Stage 1) produces
  the relay record before hand-compilation (Stage 2).
- Lifecycle emphasis: two new named enforcement steps are inserted as visible lifecycle events:
  (1) "SA-TO-SG PROMOTION" as an explicit named boundary event at the start of Setup, and
  (2) "ACTION DIVERSITY CHECK" as an explicit named gate at the end of Findings. Both are
  first-class lifecycle steps, not table columns or implicit rules.

**Hypothesis**: R3 V-04 achieved 100 but C-15 and C-16 were satisfied implicitly -- the relay
record noted SA gaps and the Findings table happened to carry distinct action directions. Making
these two criteria explicit named lifecycle steps ensures they cannot be accidentally omitted:
SA-TO-SG PROMOTION is a step the tracer must complete and label before confirming Setup inputs,
and ACTION DIVERSITY CHECK is a step the tracer must run and pass before entering Amend. This
variation is the most explicit architecture in Round 4 -- every criterion has a named structural
correspondent. Risk: named steps increase prompt length and may cause tracers to satisfy each
step mechanically without genuine reasoning; the SA-TO-SG PROMOTION step may receive a one-line
"no SA gaps found" without actually auditing for SA candidates.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Stage 1 -- Source-Layer Auditor

Your job is to map the gap space before any phase begins. Read `{{skill_spec_path}}` and
catalog every gap by source layer:

**Spec-level gaps (SA)**: inputs the spec does not define, role handoff contracts not specified,
artifact sections with undefined content rules, decisions requiring external knowledge.

**Setup-level gaps (SG)**: inputs the spec defines but that are not derivable from the test
invocation or repo context alone.

**Execute-level gaps (EG)**: artifact sections or role outputs the named roles may structurally
fail to produce as specified.

**Auditor success criterion**: this audit succeeds when gaps from at least two distinct source
layers have been identified. If all visible gaps fall at one layer, examine harder:

- If only EG gaps visible: examine the spec's role handoff contracts and artifact naming
  convention for SA candidates.
- If only SA gaps visible: evaluate whether the test invocation fully specifies all declared
  inputs for SG candidates.

Produce the audit table:

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

If 0 gaps found after rigorous reading: add one P3 QO. A spec with zero auditable gaps has
not been examined carefully enough.

**Stage 1 relay to Stage 2**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (2+ distinct layers) / FAIL (1 layer only)]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

SA and SG gaps from Stage 1 are inputs to every phase. Do not re-derive them. Do not silently
resolve them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

This is a required step at the Setup boundary. For every SA gap in the Stage 1 relay, evaluate:

> Does this gap make implementation impossible (spec defect), or can the invoker supply
> the value at runtime even though the spec does not declare it?

Write an explicit entry for each SA gap:

```
SA-NN -> [result]:
  Gap: [what the spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
  If promoted: SG-NN label to use in all downstream phases
```

After processing all SA gaps, the relay is updated:

```
[SA remaining: {{sa_remaining}}]   -- spec defects; block implementation if P1
[SG from promotion: {{sg_promoted}}]   -- invoker-supply gaps; documentation change
[SG original: {{sg_original}}]   -- from Stage 1
```

SA labels must not appear in Findings or Amend for promoted gaps. Use the SG label.

---

#### Phase 1 -- Setup

Using the test invocation and repo context. Record confirmed values with `[name: value]`
notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Role gap attribution**: For each role in `[roles: ...]`, enumerate which gaps from the
SA-TO-SG PROMOTION output and Stage 1 SG/EG list affect this role's execution:

```
[role: {{role_name}}]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps (contract violations expected): [list or "none -- confirmed"]
```

A role entry without explicit gap attribution does not pass -- write "none -- confirmed"
if verified.

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

Every section the artifact contract defines must appear. For each role, open a role relay before
writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Do not infer silently at any decision point. A silently filled gap is invisible to the
implementer.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [SA: `{{sa_remaining}}`],
[SG: `{{sg_total}}`], [EG: `{{eg_all}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], [all gaps: `{{gap_list}}`].

Merge all gaps from Stage 1 and Stage 2 into the unified findings table. Use promoted Source
labels:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|
| | | SA / SG / EG / QO | P1/P2/P3 | |

Minimum 2 entries with at least 2 distinct Source types.

---

**ACTION DIVERSITY CHECK (named lifecycle event)**

This is a required step before Amend. For every group of Findings rows that share the same
Source label, verify:

> Do the Action fields in this group name distinct spec sections, invocation parameters,
> artifact sections, or role behaviors?

Write an explicit check entry for each same-Source group:

```
Source group: [SA / SG / EG / QO]
Entries in group: [F-NN, F-NN, ...]
Action fields: [list the Action text for each]
Diversity: PASS (all distinct targets) / FAIL (overlap found)
If FAIL: revise Action for [F-NN] to: [revised action text]
```

A single-entry group passes automatically. A group where no two entries overlap passes.
A group with overlap must be revised before proceeding to Amend.

**Carry forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

---

#### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; must not be SA if promoted)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [source type confirmed: YES / NO -- was the Source label accurate?]

---

### Verdict

**Stage 1 layer diversity**: `{{diversity_status}}` -- [note if FAIL]
**SA remaining**: [count] (after promotion) | **SG total**: [count] | **EG total**: [count]
**Action Diversity Check**: PASS / FAIL -- [note if any group required revision]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion (spec defect blocks implementation).
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`

---

## V-05 -- Combined axes: Inertia framing + role sequence (per-role gap relay table)

**Axes**:
- Role sequence: a two-stage structure where Stage 1 produces the relay record and Stage 2
  runs hand-compilation; but in Execute, each role opens with a structured "Role Gap Relay
  Table" -- a per-role table that shows which gaps from the pre-audit bind this role, with SA
  gaps displayed under their promoted SG label. The relay table is the structural enforcement
  of C-14 (per-role attribution) and C-15 (SA re-labeled at the boundary where the role first
  encounters it).
- Inertia framing: the prompt opens with a "without this skill" statement and each named gate
  is followed by an inertia cost sentence explaining what a developer skipping this step would
  pay at implementation time.

**Hypothesis**: Per-role gap relay tables make C-14 unavoidable: you cannot write an artifact
section for a role without first declaring which gaps affect it. The SA-to-SG re-labeling
happens at the Role Gap Relay Table for the role that first encounters the promoted gap --
making C-15 distributed across roles rather than a single Setup boundary event. This is an
alternative C-15 implementation that passes if the rubric accepts role-level SA→SG promotion
as equivalent to a Setup-boundary promotion. Inertia framing motivates each gate by explaining
its implementation cost, converting abstract criteria into developer decisions. Risk: C-15's
pass condition requires re-labeling "at or near the start of Setup" -- if promotion is deferred
to Execute (per-role), it may fail C-15 strictly. To hedge, the prompt also includes a Setup-
level SA-to-SG promotion block, with the Role Gap Relay Tables reinforcing it at the role level.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Without `/{{skill_name}}`**: A developer validating this skill would need to read the spec,
mentally simulate role behavior for each phase, and discover implementability gaps only after
writing code. Each gap this trace surfaces is a failure they would have paid for in rework.
The source layer a gap lives in -- spec, setup, or execute -- determines who pays and when:
a spec-layer gap caught here saves implementation work; discovered at runtime, it derails a
sprint.

---

### Stage 1 -- Source-Layer Auditor

*Without this stage, a tracer enters the lifecycle blind to the gap topology. Spec-layer gaps
discovered mid-Execute force backtracking through phases already written. This stage maps the
terrain before traversing it.*

Read `{{skill_spec_path}}` and catalog gaps by layer:

**SA (spec absent)**: inputs not declared, role handoffs not specified, artifact sections without
content rules, decisions requiring knowledge outside the skill's scope.

**SG (setup gap)**: inputs the spec declares but that the invocation likely cannot supply.

**EG (execute gap)**: artifact contract requirements the defined roles may structurally fail
to produce.

**Success criterion**: the audit succeeds when at least two distinct source layers are
represented. If gaps cluster at one layer, search harder for the others before declaring done.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

*Without SA-to-SG promotion here, SA labels travel into Findings unchanged -- where they
suggest "fix the spec" even for gaps that are actually the invoker's responsibility at runtime.
Promotion resolves this before any artifact section is written.*

**SA-to-SG Promotion (Setup boundary)**:

For each SA gap in the Stage 1 relay:

```
SA-NN: [gap description]
  -> Promotion: YES -- promotes to SG-NN ([reason: invoker can supply this value])
             OR NO -- remains SA ([reason: spec must declare this before implementation])
```

After promotion, the active gap list entering Execute:

```
[SA remaining: {{sa_remaining}}]
[SG active (original + promoted): {{sg_active}}]
```

**Input confirmation** using `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG active: `{{sg_active}}`].

---

#### Phase 2 -- Execute

*Without per-role gap attribution, the Execute phase silently absorbs gaps that should block
specific roles -- producing an artifact that appears complete while carrying invisible
constraints. Each Role Gap Relay Table makes those constraints visible before the role writes
its section.*

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-{signal}-{date}.md`

For each role, complete the Role Gap Relay Table before writing its artifact section:

---

**Role Gap Relay Table -- [role name]**

*Without this table, gaps that constrain this role are discovered during writing -- after
the artifact section exists and must be revised.*

| Gap ID | Gap | Type | Affects this role? | Note |
|--------|-----|------|--------------------|------|
| SG-NN / EG-NN | | SG / EG | YES / NO | |

Include every gap from the active list (SA remaining, SG active, EG from prior roles).
For any SA remaining gap that affects this role's execution: re-label it SG here and note
`[SA-NN re-labeled SG-NN at this role boundary]`.

**Role output**: [what this role produced for the artifact] / [EG-NN: sections it could not
produce, and why]

---

(Repeat Role Gap Relay Table for each subsequent role.)

---

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], full gap set from Stages 1 and 2.

*Without source-layer attribution and action diversity enforcement, a findings table lists
symptoms without directing the right fix to the right owner. A developer acting on a single-layer
table may fix the artifact when the real failure is in the spec -- or vice versa.*

Merge all gaps into the findings table. Use promoted and role-level re-labeled Source values:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Before proceeding to Amend:

- **Layer check**: at least 2 distinct Source types present? If not, identify a finding from
  the missing layer.
- **Action diversity**: for each same-Source group, verify Action fields point at distinct
  targets. If any pair overlaps, revise before proceeding.

Record: `[layers covered: {{source_types}}]`

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

---

#### Phase 4 -- Amend

*Without source-type verification in Amend, a developer could patch an artifact section for
what is actually a spec-layer gap. The patch appears to work; the gap resurfaces at the next
invocation because the spec was never updated.*

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

Apply the finding:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [section changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:
- [finding: `{{F-NN}}`]
- [reason: ]
- [source type confirmed: YES / NO]

---

### Verdict

**Without this skill**: [one sentence -- what the developer had to do manually]
**With this skill**: [one sentence -- what the developer has instead]

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG active**: [count] | **EG total**: [count]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains unresolved after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-{signal}-{date}.md`
