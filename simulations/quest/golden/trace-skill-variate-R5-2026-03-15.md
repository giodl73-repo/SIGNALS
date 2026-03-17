---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 5
rubric: trace-skill-rubric-v5-2026-03-15.md
---

# trace-skill -- Variations R5 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

Round 5 target: C-17, C-18, C-19 -- the three new v5 aspirational criteria. All Round 4
non-ceiling variations failed C-17 (severity vocabulary unconstrained). V-01 and V-03 also
failed C-18 (no remediation channel field in Amend). V-01 failed C-19 entirely; V-03
got PARTIAL (requirements named but no PASS/FAIL recorded). R4 V-04 is the inferred 100
ceiling; C-04-19 are partially inferred from the round title. Round 5 makes all three new
criteria structurally unavoidable while exploring different delivery architectures.

C-19 requires at minimum TWO named enforcement gates before Amend. R4 V-04 had one
explicit gate (ACTION DIVERSITY CHECK); under v5, a second gate (source diversity, or
severity completeness) must also be named and record PASS/FAIL. All Round 5 variations
include at least two named gates.

Single-axis selections: Output format (V-01), Phrasing register (V-02),
Lifecycle emphasis (V-03).
Combined: Role sequence + lifecycle emphasis (V-04), Inertia framing + output format (V-05).

---

## V-01 -- Single axis: Output format (schema-first declaration block)

**Axis**: Output format -- all three schemas required by the new criteria (severity vocabulary,
gap type taxonomy, remediation channel taxonomy) are collected into a "Trace Protocol Schemas"
block at the very top of the prompt, before Stage 1 runs. Enforcement gates are also listed
there as a required-gate checklist. Every later section references the schemas by name rather
than re-defining them. The schemas themselves are tables; later sections fill in their values.

**Hypothesis**: C-17 fails when severity vocabulary is present by convention rather than
declaration. Placing the severity legend table at the top makes it impossible to skip -- the
tracer declares P1/P2/P3 before writing a single finding. C-18 fails when Amend records
source confirmation but not channel; pre-declaring the channel taxonomy table makes the field
visible before Amend starts. C-19 fails when gates are implicit; pre-listing the gate
checklist converts each gate from an ad hoc check into a required fill-in item. Risk: upfront
schema blocks feel heavy before any execution; tracers who treat them as boilerplate may paste
declarations without ensuring findings actually use the declared labels. The Verdict checks
schema adherence explicitly to close this gap.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas

Declare all schemas here before Stage 1 runs. Fill every table completely. All phases must
use only the labels defined in these tables. The Verdict confirms adherence.

#### Severity Vocabulary

| Label | Definition | Action threshold |
|-------|-----------|-----------------|
| P1 | Must address before this artifact is useful -- blocks implementation or invocation | Resolve before proceeding; trace is NEEDS-SPEC-REVISION or NEEDS-REDESIGN if P1 unresolved |
| P2 | Improve quality -- improvable but not blocking | Address in Amend or schedule follow-on |
| P3 | Future consideration -- advisory; no immediate action required | Log and proceed |

**Vocabulary lock**: All Findings entries and all Amend entries must use exactly P1, P2,
or P3. No other severity labels are permitted.

#### Gap Type Taxonomy

| Type | Meaning | Default remediation direction |
|------|---------|------------------------------|
| SA | Spec absent -- the spec does not declare this input, contract, or rule | Spec must be amended before implementation |
| SG | Setup gap -- declared in spec; value unavailable at invocation time | Invocation change or documentation update |
| EG | Execute gap -- artifact contract requirement the role cannot produce | Skill implementation or role definition change |
| QO | Quality observation -- improvable; not a structural gap | Advisory |

#### Remediation Channel Taxonomy

| Channel | What it targets | Typical source type |
|---------|----------------|-------------------|
| spec | Skill specification or artifact contract | SA |
| invocation | How the skill is called (parameters, context, documentation) | SG |
| artifact | Output document (sections, fields, content) | EG |
| quality | Quality improvement with no direct source-layer finding | QO |

**Channel lock**: Every Amend entry (change or dismissal) must include
`[remediation channel: spec / invocation / artifact / quality]`.

#### Required Enforcement Gates

Before Amend may proceed, all three gates must be run and recorded:

| Gate ID | Property | Required to proceed |
|---------|---------|-------------------|
| G-1 | Source diversity: ≥2 distinct Source types in Findings | PASS or add finding from missing layer |
| G-2 | Action diversity: no two same-Source findings share identical Action text | PASS or revise duplicate Actions |
| G-3 | Severity completeness: all Findings entries use only P1/P2/P3 | PASS or relabel non-conforming entries |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using
the Gap Type Taxonomy declared above.

**SA audit** -- scan for undeclared values:
- Are all inputs declared in the spec with source, type, and format?
- Is the role sequence and each role's handoff contract specified?
- Is the artifact contract complete (naming convention, required sections, content rules)?

**SG pre-audit** -- scan for predictable binding failures:
- Which declared inputs are unlikely to be derivable from the test invocation alone?

**EG pre-audit** -- scan for predictable contract violations:
- Are there artifact sections the spec requires that defined roles may structurally fail to produce?

**Auditor success criterion**: audit succeeds when gaps from at least two distinct Source types
appear. If gaps cluster at one type, examine harder before declaring done.

Produce the audit table (use only SA / SG / EG / QO from the Gap Type Taxonomy):

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay to Stage 2**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL (1 source type only)]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

SA and SG gaps from Stage 1 are live constraints. Do not re-derive them. Do not silently
resolve them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

Required step at the Setup boundary. For every SA gap in the Stage 1 relay, evaluate:

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

After processing all SA gaps, the relay updates:

```
[SA remaining: {{sa_remaining}}]   -- spec defects; block implementation if P1
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

SA labels must not appear in Findings or Amend for promoted gaps. Use the SG label.

---

#### Phase 1 -- Setup

Using the test invocation and repo context. Confirm each input with `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role gap attribution** (role -> gaps direction): For each role in `[roles: ...]`,
enumerate which gaps from the SA-TO-SG PROMOTION output and Stage 1 SG/EG list constrain
this role's execution:

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

Produce the hand-compiled artifact: `{topic}-skill-trace-{date}.md`

Every section the artifact contract defines must appear. For each role, open a role relay
before writing the artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Do not infer silently. EG gaps discovered here continue the numbering from Stage 1.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], all gaps from Stage 1 and Stage 2.

**Step 3a -- Severity legend (reference from Trace Protocol Schemas)**

> P1 = must address before artifact is useful | P2 = improve quality | P3 = future consideration

All entries in Step 3b must use only these labels.

**Step 3b -- Findings table**

Merge all gaps into the unified findings table. Use promoted Source labels (SG, not SA, for
promoted gaps). Use only P1 / P2 / P3 severity labels:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries.

**Step 3c -- Enforcement gates (from Required Enforcement Gates in Trace Protocol Schemas)**

Run each gate. Record PASS or FAIL explicitly:

**G-1 Source Diversity Gate**
- Property checked: >=2 distinct Source types in Findings table above
- Source types present: [list]
- Result: PASS / FAIL
- If FAIL: identify and add a finding from the missing source layer, then re-run.

**G-2 Action Diversity Gate**
- Property checked: no two same-Source findings carry identical Action text
- Same-Source pairs reviewed: [list pairs and their Action fields, or "none -- all Source types unique"]
- Result: PASS / FAIL
- If FAIL: revise Action text for the duplicate pair to name distinct targets, then re-run.

**G-3 Severity Completeness Gate**
- Property checked: all Findings entries use only P1/P2/P3 (from declared vocabulary)
- Severity labels in use: [list]
- Result: PASS / FAIL
- If FAIL: relabel non-conforming entries using the declared vocabulary, then re-run.

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: `{{PASS/FAIL}}`], [G-2: `{{PASS/FAIL}}`], [G-3: `{{PASS/FAIL}}`].

---

#### Phase 4 -- Amend

**Channel taxonomy** (from Trace Protocol Schemas): spec / invocation / artifact / quality

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

All three enforcement gates must be PASS. If any gate is FAIL, return to Phase 3.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; must not be SA if promoted)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict

**Schema adherence**:
- Severity labels used: [list] -- all from P1/P2/P3 vocabulary: YES / NO
- Remediation channels used: [list] -- all from declared taxonomy: YES / NO
- Gates: G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion (spec defect blocks implementation).
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Phrasing register (imperative directive)

**Axis**: Phrasing register -- every instruction is a direct command in second-person
imperative voice. No descriptive prose between requirements. Short sentences. "Declare",
"Write", "Record", "Run", "Fill", "Confirm". The three new criteria become required fill-in
fields rather than described requirements. The trace structure is identical to the baseline
(two-stage, SA-TO-SG PROMOTION, named gates, channel field) -- only the phrasing changes.

**Hypothesis**: Imperative phrasing reduces the cognitive distance between criterion and
action. "The Findings section should include a severity legend declared with definitions" is
a description; "Write the severity legend here. Fill in each label now." is a command that
produces the output immediately. C-17 fails when the tracer understands the requirement but
defers the declaration. C-18 fails when the tracer knows about source confirmation but omits
the channel field. C-19 gates fail when the tracer understands the check but doesn't record
a result. Imperative phrasing collapses the gap between understanding and doing. Risk: terse
commands without explanation may cause tracers to fill fields mechanically without genuine
reasoning. The gate pass/fail fields could become rote checkbox entries.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Stage 1 -- Spec Audit

Read `{{skill_spec_path}}`. Do not read the test invocation yet.

Find every gap. Use only these source labels: SA / SG / EG / QO.

- SA: the spec does not declare it.
- SG: the spec declares it; the invoker probably cannot supply it.
- EG: the artifact contract requires it; the role probably cannot produce it.
- QO: improvable, not a failure.

Produce this table:

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

Stop when you have gaps from at least two distinct Source types. If all gaps are one type,
look harder.

Write the relay record now. Fill in every field:

```
[SA: ]
[SG: ]
[EG: ]
[layer diversity: PASS / FAIL]
```

---

### Stage 2 -- Hand-Compilation

Carry these fields into every phase:

**Relay in**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

Do not re-derive these gaps. Do not silently resolve them.

---

#### SA-TO-SG PROMOTION

Do this now, before Setup inputs.

For each SA item in the relay, write one entry:

```
SA-NN:
  Gap: [what is undeclared]
  Promotes? YES -> SG-NN ([reason invoker can supply this]) / NO -> remains SA ([reason spec must declare this])
```

Update the relay:

```
[SA remaining: ]
[SG from promotion: ]
[SG original: ]
```

From here: use SG labels for promoted gaps. Do not use SA labels for promoted gaps anywhere downstream.

---

#### Phase 1 -- Setup

Confirm each input. Write `[name: value]`:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

For each role in `[roles: ...]`, write its gap attribution now. Use role -> gaps direction:

```
[role: ]
  SG/SA gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected for this role: [list or "none -- confirmed"]
```

Do not list roles without gap attribution. Write "none -- confirmed" if truly none.

Carry forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carry forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the artifact now: `{topic}-skill-trace-{date}.md`

Every section in the artifact contract must be present.

For each role, write its relay before its artifact section:

**Relay -- [role name]**:
- From: [prior role or Setup]
- Values received: [name: value, ...]
- Gaps binding this role: [list or "none -- confirmed"]
- Produced: [content added to artifact]
- EG gaps found: [list or "none"]

Do not infer. Do not fill gaps silently.

Carry forward: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carry forward: [artifact: `{{artifact_path}}`], all gaps.

**Declare the severity legend now. Fill in each cell:**

| Label | Definition |
|-------|-----------|
| P1 | [write the definition: when is this a blocker?] |
| P2 | [write the definition: when is this a quality improvement?] |
| P3 | [write the definition: when is this advisory only?] |

Use only P1, P2, P3 in every finding entry. No other labels.

**Write the findings table:**

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

At least 2 entries. Use promoted Source labels. Use only P1/P2/P3.

**Run the enforcement gates. Record PASS or FAIL for each. Do not proceed to Amend until all three are PASS.**

**Gate 1 -- Source Diversity**
- Check: how many distinct Source types are in the table above?
- Types present: [list]
- Result: PASS / FAIL
- If FAIL: add one finding from the missing layer. Re-run this gate.

**Gate 2 -- Action Diversity**
- Check: for each pair of findings that share the same Source label, are their Action fields pointing at different targets?
- Same-Source pairs: [list or "none -- all Source types unique"]
- Result: PASS / FAIL
- If FAIL: revise the duplicate Action to name a distinct target. Re-run this gate.

**Gate 3 -- Severity Completeness**
- Check: does every finding use only P1/P2/P3?
- Labels in use: [list]
- Result: PASS / FAIL
- If FAIL: relabel non-conforming entries. Re-run this gate.

Carry forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS/FAIL], [G-2: PASS/FAIL], [G-3: PASS/FAIL].

---

#### Phase 4 -- Amend

Carry forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].

**Check gates before writing.** All three must be PASS. If any is FAIL, return to Phase 3.

**Declare the channel taxonomy now:**

- spec = change the skill specification
- invocation = change how the skill is called
- artifact = update the output document
- quality = improve quality without a source-layer finding

For each Amend entry, write all five fields. No exceptions:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`]
- [remediation channel: spec / invocation / artifact / quality]
- [change: ]
- [source confirmed: YES / NO]

For dismissals, write:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict

Write one result: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

- `NEEDS-SPEC-REVISION`: any P1 SA gap remains SA after promotion.
- `NEEDS-REDESIGN`: EG gaps exceed 3 and cluster on a structural role gap.
- `USEFUL`: otherwise.

State the basis in one sentence tied to a named finding ID.

**Gate summary**: G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
**Layer diversity**: `{{diversity_status}}`
**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (Findings-Amend bridge expansion)

**Axis**: Lifecycle emphasis -- the Findings phase is the structural weight center of the
trace. Setup and Execute are compact: necessary confirmations, no expansions. Findings is
organized as a four-step protocol: (1) severity legend declaration, (2) findings table
population, (3) three named enforcement gates, (4) channel taxonomy declaration as the
transition into Amend. Each step in Findings is a named sub-section. The Amend section opens
with the channel taxonomy carried forward from step (4). This concentrates all three new
criteria (C-17, C-18, C-19) in the Findings-to-Amend region where they architecturally belong.

**Hypothesis**: C-17/C-18/C-19 are all boundary conditions at the Findings-to-Amend
transition. Expanding Findings to include explicit protocol steps for each criterion places
enforcement exactly where tracers encounter the boundary. A tracer who rushes Setup and Execute
to reach Findings will find the full protocol already assembled. Compare to V-01 where the
schemas are declared at the very top (before any phase) -- V-03 declares them at the moment of
use. The risk is that compact Setup/Execute may produce shallow carry-forwards. To hedge, the
pre-execution audit is still a separate Stage 1 with a structured relay record; the compression
applies only to Phase 1 Setup and Phase 2 Execute within Stage 2.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before the test invocation. Audit for gaps across all three layers.

**SA** -- inputs, role handoffs, or artifact sections the spec does not declare.
**SG** -- inputs the spec declares but the test invocation likely cannot supply.
**EG** -- artifact sections or role outputs the defined roles may structurally fail to produce.

Auditor success criterion: gaps from at least two distinct source layers identified. Examine
harder if all gaps cluster at one layer.

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

**Relay in**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

---

#### Phase 1 -- Setup

**SA-to-SG promotion** (at Setup boundary): For each SA item, evaluate whether the invoker
can supply the value at runtime. Write `SA-NN -> SG-NN (promoted)` or `SA-NN (remains SA)`.

```
[SA remaining: {{sa_remaining}}]
[SG active: {{sg_active}}]
```

Confirm inputs using `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role gap attribution (role -> gaps): For each role, enumerate gaps that constrain it:

```
[role: {{role_name}}]
  SG/SA gaps: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG active: `{{sg_active}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. Every artifact section required by the spec must
appear. For each role, state: (a) what it received, (b) what it contributed, (c) any EG gaps
encountered. Mark artifact sections with EG gaps as `[EG-NN: reason]`. Do not infer silently.

**Carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], full gap inventory from Stages 1 and 2.

---

##### Step 3a -- Severity Legend Declaration

Declare the severity vocabulary before writing any finding. This legend governs all entries
in Step 3b. All entries must use only the labels defined here.

**Severity legend**:

| Label | Definition | Actionability threshold |
|-------|-----------|------------------------|
| P1 | Must address before this artifact is useful -- blocks implementation or invocation | Resolve before leaving Findings; trace verdict reflects open P1s |
| P2 | Should address to improve quality -- not blocking | Address in Amend phase or schedule follow-on |
| P3 | Future consideration -- advisory; no immediate action required | Log in findings; no gate impact |

---

##### Step 3b -- Findings Table

Merge all gaps into the unified findings table. Use promoted Source labels (SG not SA for
promoted gaps). Use only P1/P2/P3 from the legend above.

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

---

##### Step 3c -- Enforcement Gates

Run all three gates before proceeding to Step 3d. Each gate must record an explicit result.

**Gate 1 -- Source Diversity Gate**
- Property: at least 2 distinct Source types present in Step 3b table
- Source types found: [list all Source values from the table]
- Result: PASS / FAIL
- Resolution if FAIL: identify a gap from the missing source layer; add it to Step 3b; re-run.

**Gate 2 -- Action Diversity Gate**
- Property: findings that share the same Source label carry distinct Action directions (not just different wording -- distinct targets: different spec sections, invocation parameters, or artifact sections)
- Same-Source groups: [for each group, list finding IDs and their Action text]
- Result: PASS / FAIL
- Resolution if FAIL: revise Action text of conflicting entries to name distinct targets; re-run.

**Gate 3 -- Severity Completeness Gate**
- Property: every finding in Step 3b uses only P1, P2, or P3 (from the legend declared in Step 3a)
- Severity labels present: [list all Severity values used]
- Result: PASS / FAIL
- Resolution if FAIL: relabel any non-conforming entry using the declared vocabulary; re-run.

All three gates must show PASS before proceeding to Step 3d.

---

##### Step 3d -- Channel Taxonomy Declaration (transition to Amend)

Declare the remediation channel taxonomy here, at the Findings-to-Amend boundary. Every
Amend entry must use one of these four channel labels:

| Channel | Targets | Typical source type |
|---------|---------|-------------------|
| spec | Skill specification or artifact contract definition | SA |
| invocation | How the skill is called (parameters, context, documentation) | SG |
| artifact | Output document (sections, fields, content) | EG |
| quality | Quality improvement with no direct source-layer finding | QO |

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[channel taxonomy: spec/invocation/artifact/quality declared],
[G-1: `{{PASS/FAIL}}`], [G-2: `{{PASS/FAIL}}`], [G-3: `{{PASS/FAIL}}`].

---

#### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].
Channel taxonomy (from Step 3d): spec / invocation / artifact / quality.
Gate status: G-1 `{{PASS/FAIL}}`, G-2 `{{PASS/FAIL}}`, G-3 `{{PASS/FAIL}}`.

All three gates must be PASS. If any is FAIL, return to Phase 3 Step 3c.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict

**Gate results**: G-1 [PASS/FAIL] | G-2 [PASS/FAIL] | G-3 [PASS/FAIL]
**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG active**: [count] | **EG total**: [count]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: Role sequence (two-stage auditor) + lifecycle emphasis (maximum named event coverage)

**Axes**:
- Role sequence: two-stage architecture from R3/R4 V-04 -- Stage 1 spec-layer auditor produces
  the structured relay record; Stage 2 runs hand-compilation with SA-TO-SG PROMOTION as a named
  lifecycle event and per-role gap relay in Execute.
- Lifecycle emphasis: all five enforcement points (three gates + two taxonomy declarations) are
  first-class named lifecycle events with structured output blocks. SEVERITY LEGEND DECLARATION
  and CHANNEL TAXONOMY DECLARATION join SA-TO-SG PROMOTION and the two existing gates.

**Hypothesis**: R4 V-04 made SA-TO-SG PROMOTION and ACTION DIVERSITY CHECK first-class
lifecycle events. C-19 requires at minimum two named gates -- R4 V-04 had one explicit gate.
V-04 extends the named-event pattern to all five structural requirements of the new criteria:
SEVERITY LEGEND DECLARATION (C-17), LAYER GATE (G-1), ACTION DIVERSITY GATE (G-2, formerly
ACTION DIVERSITY CHECK), SEVERITY COMPLETENESS GATE (G-3, new), CHANNEL TAXONOMY DECLARATION
(C-18). Each event has a header, structured output block, and explicit result where
applicable. Three of the five events are enforcement gates recording PASS/FAIL. This produces
the most auditable trace in Round 5: every criterion has a named structural correspondent.
Risk: named events increase prompt length substantially; a tracer who satisfies each event
header mechanically produces a structurally complete but diagnostically shallow trace.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Stage 1 -- Source-Layer Auditor

Map the gap space before any phase begins. Read `{{skill_spec_path}}` only (do not consult
the test invocation yet).

Catalog every gap by source layer:

**SA (spec absent)**: inputs not declared, role handoffs not specified, artifact sections with
undefined content rules, decisions requiring knowledge outside the skill's scope.

**SG (setup gap)**: inputs the spec declares but that the invocation likely cannot supply.

**EG (execute gap)**: artifact contract requirements the defined roles may structurally fail
to produce.

**Auditor success criterion**: the audit succeeds when gaps from at least two distinct source
layers are identified. If gaps cluster at one layer, examine harder:
- If only EG gaps visible: examine spec's role handoff contracts and naming convention for SA candidates.
- If only SA gaps visible: evaluate whether the test invocation fully specifies all declared inputs for SG candidates.

Produce the audit table:

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

If 0 gaps found after rigorous reading: add one P3 QO. A spec with zero auditable gaps
has not been examined carefully enough.

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

After processing all SA gaps, the relay updates:

```
[SA remaining: {{sa_remaining}}]   -- spec defects; block implementation if P1
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
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

**Role gap attribution** (role -> gaps direction): For each role in `[roles: ...]`, enumerate
which gaps from the SA-TO-SG PROMOTION output and Stage 1 SG/EG list affect this role:

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

Produce the hand-compiled artifact: `{topic}-skill-trace-{date}.md`

Every section the artifact contract defines must appear. For each role, open a role relay
before writing the artifact section:

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

---

##### SEVERITY LEGEND DECLARATION (named lifecycle event)

Declare the severity vocabulary before the findings table. This declaration constrains every
entry in the findings table and every entry in Amend. Declare all three labels explicitly.

```
Severity legend:
  P1 = [definition: when is a finding a blocker?]
  P2 = [definition: when is a finding a quality improvement?]
  P3 = [definition: when is a finding advisory only?]
```

**Vocabulary lock**: all findings entries and all Amend entries must use only P1, P2, P3.
No other severity labels are valid. Entries using unlisted labels do not count toward the
minimum finding threshold.

---

Merge all gaps from Stage 1 and Stage 2 into the unified findings table. Use promoted Source
labels. Use only P1/P2/P3 from the legend above:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|
| | | SA / SG / EG / QO | P1/P2/P3 | |

Minimum 2 entries with at least 2 distinct Source types.

---

##### LAYER GATE (named enforcement gate)

```
Gate: LAYER GATE
Property: at least 2 distinct Source types are present in the findings table above
Source types present: [list all Source values used]
Result: PASS / FAIL
If FAIL: identify and add a finding from the missing source layer; re-run this gate before proceeding.
```

---

##### ACTION DIVERSITY GATE (named enforcement gate)

```
Gate: ACTION DIVERSITY GATE
Property: findings sharing the same Source label carry distinct Action directions
          (distinct targets: different spec sections, invocation parameters, or artifact sections)
For each same-Source group:
  Group: [SA / SG / EG / QO]
  Entries: [finding IDs]
  Action fields: [action text for each entry]
  Diversity: PASS (all distinct targets) / FAIL (overlap found)
  If FAIL: revised Action for [F-NN]: [revised text]
Overall result: PASS / FAIL
If FAIL: revise overlapping Actions before proceeding.
```

---

##### SEVERITY COMPLETENESS GATE (named enforcement gate)

```
Gate: SEVERITY COMPLETENESS GATE
Property: all findings entries use only P1, P2, or P3 (from the SEVERITY LEGEND DECLARATION)
Severity labels in use: [list all Severity values from the findings table]
Non-conforming entries: [list any entries with labels outside P1/P2/P3, or "none"]
Result: PASS / FAIL
If FAIL: relabel non-conforming entries using the declared vocabulary; re-run this gate.
```

---

##### CHANNEL TAXONOMY DECLARATION (named lifecycle event)

Declare the remediation channel taxonomy before Amend. Every Amend entry must include a
channel field using these labels:

```
Channel taxonomy:
  spec      = change the skill specification or artifact contract
  invocation = change how the skill is called (parameters, context, documentation)
  artifact   = update the output document (sections, fields, content)
  quality    = improve quality; no direct source-layer finding
```

**Channel lock**: every Amend entry (change or dismissal) must include
`[remediation channel: spec / invocation / artifact / quality]`.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[LAYER GATE: `{{PASS/FAIL}}`], [ACTION DIVERSITY GATE: `{{PASS/FAIL}}`],
[SEVERITY COMPLETENESS GATE: `{{PASS/FAIL}}`].

---

#### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].
Channel taxonomy: spec / invocation / artifact / quality (from CHANNEL TAXONOMY DECLARATION).

**Gate check**: LAYER GATE `{{PASS/FAIL}}`, ACTION DIVERSITY GATE `{{PASS/FAIL}}`,
SEVERITY COMPLETENESS GATE `{{PASS/FAIL}}`. All three must be PASS.
If any gate is FAIL, return to Phase 3 to resolve.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; must not be SA if promoted)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict

**Named events completed**:
- SA-TO-SG PROMOTION: [count SA processed, count promoted, count remains SA]
- SEVERITY LEGEND DECLARATION: [confirmed P1/P2/P3 declared]
- LAYER GATE: PASS / FAIL
- ACTION DIVERSITY GATE: PASS / FAIL
- SEVERITY COMPLETENESS GATE: PASS / FAIL
- CHANNEL TAXONOMY DECLARATION: [confirmed spec/invocation/artifact/quality declared]

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion (spec defect blocks implementation).
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: Inertia framing + output format (declaration tables with cost statements)

**Axes**:
- Inertia framing: each new declaration (severity legend, channel taxonomy) and each named
  gate is preceded by a "Without this:" statement that describes the concrete failure mode the
  declaration or gate prevents. The prompt opens with a "without this skill" framing. Inertia
  statements motivate each structural step by naming the cost of skipping it.
- Output format: every schema declaration is a compact table. The severity legend is a 3-row
  table. The channel taxonomy is a 4-row table. The enforcement gates are structured blocks
  where the evidence and result fields are explicit column-like entries. The two-stage
  architecture is maintained; per-role gap attribution uses role->gaps direction in Setup;
  inertia statements appear in Execute and Amend as well.

**Hypothesis**: Declaration tables are harder to skip than inline prose declarations. A tracer
who reads "P1 = must address before artifact is useful" as prose can absorb it without writing
it down; a table with an empty second column forces production of the definition. Inertia cost
statements make each structural step feel load-bearing: "Without the severity legend, two
tracers on the same team can produce incompatible findings tables -- one using Critical/High,
one using P1/P2/P3." The combination tests whether the explicit cost-of-skipping framing
(motivation) plus the table format (production pressure) together eliminate the C-17/C-18/C-19
gaps that persisted in non-ceiling R4 variations. Risk: inertia statements add prose overhead
that may reduce execution depth in later phases; the tables may receive perfunctory definitions
if the tracer is focused on filling them rather than understanding them.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Without `/{{skill_name}}`**: A developer validating this skill would read the spec manually,
mentally simulate role behavior for each phase, and discover implementability gaps only after
writing code. Each gap this trace surfaces is a failure they would have paid for in rework.
The source layer a gap lives in determines who pays and when: a spec-layer gap caught here
saves an implementation sprint; the same gap discovered at runtime derails one.

---

### Stage 1 -- Source-Layer Auditor

*Without this stage, a tracer enters the lifecycle blind to the gap topology. Spec-layer
gaps discovered mid-Execute force backtracking through phases already written. This stage
maps the terrain before traversing it.*

Read `{{skill_spec_path}}` and catalog gaps by layer:

**SA (spec absent)**: inputs not declared, role handoffs not specified, artifact sections
without content rules, decisions requiring knowledge outside the skill's scope.

**SG (setup gap)**: inputs the spec declares but that the invocation likely cannot supply.

**EG (execute gap)**: artifact contract requirements the defined roles may structurally fail
to produce.

**Success criterion**: at least two distinct source layers represented. If gaps cluster at one
layer, search harder for the others before declaring done.

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

For each SA gap in the Stage 1 relay, fill in this table:

| SA ID | Gap description | Promotes? | If YES: new SG ID | Reason |
|-------|-----------------|-----------|------------------|--------|
| SA-NN | | YES -> SG-NN / NO (remains SA) | | |

After promotion, the active gap list entering Execute:

```
[SA remaining: {{sa_remaining}}]   -- spec defects; blocks implementation if P1
[SG active (original + promoted): {{sg_active}}]
```

**Input confirmation** using `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role gap attribution** (role -> gaps):

*Without per-role attribution, Execute silently absorbs gaps that should block specific roles
-- producing an artifact that appears complete while carrying invisible constraints.*

For each role in `[roles: ...]`:

| Role | SG/SA gaps binding this role | EG gaps expected |
|------|------------------------------|-----------------|
| [role name] | [list or "none -- confirmed"] | [list or "none -- confirmed"] |

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG active: `{{sg_active}}`].

---

#### Phase 2 -- Execute

*Without per-role gap relay tables, Execute silently absorbs gaps that should constrain role
behavior -- the artifact appears complete while carrying invisible constraints.*

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce the hand-compiled artifact: `{topic}-skill-trace-{date}.md`

For each role, complete the Role Gap Relay Table before writing its artifact section:

---

**Role Gap Relay Table -- [role name]**

*Without this table, gaps that constrain this role are discovered during artifact writing,
after sections exist and must be revised.*

| Gap ID | Gap description | Type | Affects this role? | Note |
|--------|----------------|------|--------------------|------|
| SG-NN / EG-NN | | SG / EG | YES / NO | |

Include every gap from the active list. For any SA remaining that affects this role's execution:
re-label it SG here and note `[SA-NN re-labeled SG-NN at this role boundary]`.

**Role output**: [what this role produced for the artifact] / [EG-NN: sections it could not
produce, and why]

---

(Repeat Role Gap Relay Table for each subsequent role.)

---

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], full gap set from Stages 1 and 2.

---

**Severity Legend Declaration**

*Without a declared severity legend, the P1/P2/P3 vocabulary floats -- two tracers on the
same team can produce incompatible findings tables. A declared legend constrains all entries
to a single shared schema and makes the priority tier machine-checkable.*

Fill in this table now, before writing any finding:

| Label | Definition | When to use |
|-------|-----------|-------------|
| P1 | [write: what makes a finding a blocker?] | [write: condition for P1 assignment] |
| P2 | [write: what makes a finding a quality improvement?] | [write: condition for P2 assignment] |
| P3 | [write: what makes a finding advisory?] | [write: condition for P3 assignment] |

All Findings entries and all Amend entries must use only P1, P2, P3. No other severity labels.

---

**Findings Table**

Merge all gaps into the unified findings table. Use promoted and role-level re-labeled Source
values. Use only P1/P2/P3 from the legend above:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

---

**Enforcement Gates**

*Without named enforcement gates, the checks that precede Amend are implicit -- a future scorer
cannot verify that they ran, only infer from the findings table that they might have. Named gates
with recorded results make enforcement history auditable.*

Run all three gates. Fill in each result field. Do not proceed to Amend until all three are PASS.

**Gate 1 -- Source Diversity Gate**

*Without this gate, a single-layer findings table reaches Amend unchecked -- the tracer fixes
artifacts for what is actually a spec gap, or vice versa.*

```
Gate: Source Diversity
Property: >=2 distinct Source types present in the findings table
Source types found: [list]
Result: PASS / FAIL
Resolution: [if FAIL: describe what was added to satisfy the gate]
```

**Gate 2 -- Action Diversity Gate**

*Without this gate, same-Source findings that share an action direction pad the finding count
without surfacing distinct gaps.*

```
Gate: Action Diversity
Property: findings sharing the same Source label carry distinct Action directions
Same-Source groups reviewed:
  [Group: SA/SG/EG/QO | Entries: F-NN,F-NN | Actions: [list] | Diversity: PASS/FAIL]
Overall result: PASS / FAIL
Resolution: [if FAIL: describe revision made]
```

**Gate 3 -- Severity Completeness Gate**

*Without this gate, non-conforming labels (Critical, High, etc.) can enter the findings table
after the severity legend was declared, defeating the purpose of the declaration.*

```
Gate: Severity Completeness
Property: all findings entries use only P1/P2/P3 from the declared legend
Labels in use: [list]
Non-conforming entries: [list or "none"]
Result: PASS / FAIL
Resolution: [if FAIL: describe relabeling done]
```

---

**Channel Taxonomy Declaration**

*Without a declared channel taxonomy, two Amend entries that both say they fix "the spec" may
target different objects (a field definition vs. an invocation example) without any structural
distinction. The channel taxonomy surfaces this distinction as a declared field.*

Fill in this table before writing any Amend entry:

| Channel | What it targets | Maps from source type |
|---------|----------------|----------------------|
| spec | [write: what kind of spec change?] | SA findings |
| invocation | [write: what kind of invocation change?] | SG findings |
| artifact | [write: what kind of artifact change?] | EG findings |
| quality | [write: quality improvement; no source-layer finding] | QO findings |

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: `{{PASS/FAIL}}`], [G-2: `{{PASS/FAIL}}`], [G-3: `{{PASS/FAIL}}`].

---

#### Phase 4 -- Amend

*Without source-type verification in Amend, a developer could patch an artifact section for
what is actually a spec-layer gap. The patch appears to work; the gap resurfaces at the next
invocation because the spec was never updated. The channel field makes this misapplication
visible.*

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].
Channel taxonomy (from Findings): spec / invocation / artifact / quality.

Gate check: G-1 `{{PASS/FAIL}}`, G-2 `{{PASS/FAIL}}`, G-3 `{{PASS/FAIL}}`.
All three must be PASS before writing any Amend entry.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; must not be SA if promoted)
- [remediation channel: spec / invocation / artifact / quality]
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality]
- [source type confirmed: YES / NO]

---

### Verdict

**Without this skill**: [one sentence -- what the developer did manually before this trace]
**With this skill**: [one sentence -- what the developer has instead]

**Schema tables completed**: severity legend [YES/NO] | channel taxonomy [YES/NO]
**Gates**: G-1 Source Diversity [PASS/FAIL] | G-2 Action Diversity [PASS/FAIL] | G-3 Severity Completeness [PASS/FAIL]
**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG active**: [count] | **EG total**: [count]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains unresolved after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
