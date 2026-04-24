---
skill: quest-variate
skill_target: trace-skill
date: 2026-03-15
round: 6
rubric: trace-skill-rubric-v6-2026-03-15.md
---

# trace-skill -- Variations R6 (2026-03-15)

5 complete prompt body variations. Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

Round 6 target: C-20, C-21, C-22, C-23 -- the four new v6 aspirational criteria. No R5
variation reaches 100 under v6. The ceiling gap is:

- V-01 (99.1): needs C-22 (hard-stop blocking directive) and C-23 (ordered sub-steps).
- V-02 (98.2): needs C-20 (schema registry before Stage 1) and C-21 (Verdict phase) and C-23.
- V-03 (98.8): needs C-20 and C-21.

Full ceiling requires integrating both architectural philosophies:
  schema-registry + Verdict (V-01 heritage) AND hard-stop + ordered sub-steps (V-02/V-03 heritage).

C-20 requires all schemas co-located BEFORE Stage 1. C-21 requires a fifth lifecycle phase
(post-Amend) that retrospectively audits schema compliance. C-22 requires that FAIL on any
gate carry an explicit blocking directive -- not just a recorded result. C-23 requires that
Findings be structured as an ordered sequence of named sub-steps with declared architectural
dependencies between them (3a cannot begin until its prerequisite is satisfied; 3b cannot
begin until 3a is declared; 3c cannot begin until 3b is populated; 3d fires only when all
3c gates are PASS).

V-01 R5 had C-20 and C-21 but lacked C-22 (no blocking directive) and C-23 (schema-first
bypasses in-phase ordering). V-02/V-03 R5 had C-22 and C-23 but lacked C-20/C-21. R6
integrates all four in every variation; variations differ in how the integration is expressed.

Single-axis selections: Output format (V-01), Phrasing register (V-02),
Lifecycle emphasis (V-03).
Combined: Output format + lifecycle emphasis (V-04), Inertia framing + output format (V-05).

---

## V-01 -- Single axis: Output format (dependency-annotated schema registry)

**Axis**: Output format -- the "Trace Protocol Schemas" block before Stage 1 is extended with
an explicit dependency column: each schema row declares which phase(s) and sub-step(s) require
it. This creates a machine-readable dependency graph at the top of the prompt. The ordered
sub-steps in Findings (Step 3a, 3b, 3c, 3d) are referenced in the dependency column of the
registry, so their ordering becomes traceable back to the registry. The Verdict phase is
extended into a compliance-audit pass that walks each schema row and verifies the declared
dependency was honored.

**Hypothesis**: V-01 R5 placed schemas before Stage 1 (C-20) and added a Verdict (C-21), but
Findings still lacked the sub-step ordering architecture required for C-23, and the gate
failure mode was "return to Phase 3" rather than an explicit blocking directive (C-22 PARTIAL).
The dependency column makes the sub-step ordering a declared constraint visible at schema
declaration time rather than a convention discovered at execution time -- so C-23 emerges from
C-20 rather than requiring a separate architectural addition. The explicit BLOCKED directive
in the gate output closes C-22. Risk: the dependency column adds mechanical overhead to the
schema registry; a tracer who fills it nominally ("Step 3b") without understanding the ordering
semantics satisfies the format without the reasoning. The Verdict compliance-audit pass forces
checking by walking each declared dependency.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas

Declare all schemas here before Stage 1 runs. The Dependency column records which phases and
sub-steps require each schema. The Verdict compliance-audit pass will verify each row.
Fill every cell completely. All phases must use only the labels and channels declared here.

#### Schema 1 -- Severity Vocabulary

| Label | Definition | Action threshold | Dependency |
|-------|-----------|-----------------|------------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | Resolve before leaving Findings; trace verdict reflects open P1s | Step 3a declares; Step 3b enforces; Step 3c (G-3) verifies; Verdict audits |
| P2 | Should address to improve quality -- not blocking | Address in Amend or schedule follow-on | Step 3a declares; Step 3b enforces |
| P3 | Future consideration -- advisory; no immediate action required | Log and proceed | Step 3a declares; Step 3b enforces |

**Vocabulary lock**: every entry in Step 3b and every Amend entry uses exactly P1, P2, or P3.
Any entry using a label not in this table is structurally invalid and does not count.

#### Schema 2 -- Gap Type Taxonomy

| Type | Meaning | Default remediation direction | Dependency |
|------|---------|------------------------------|------------|
| SA | Spec absent -- spec does not declare this input, contract, or rule | Spec must be amended before implementation | Stage 1; SA-TO-SG PROMOTION; Step 3b Source column |
| SG | Setup gap -- declared in spec; value unavailable at invocation time | Invocation change or documentation update | SA-TO-SG PROMOTION output; Setup; Execute; Step 3b |
| EG | Execute gap -- artifact contract requirement role cannot structurally produce | Skill implementation or role definition change | Execute; Step 3b |
| QO | Quality observation -- improvable; not a structural gap | Advisory | Step 3b |

**Label lock**: promoted SA gaps use SG labels in all downstream phases. SA labels appearing
after SA-TO-SG PROMOTION for a promoted gap are invalid.

#### Schema 3 -- Remediation Channel Taxonomy

| Channel | What it targets | Typical source type | Dependency |
|---------|----------------|-------------------|------------|
| spec | Skill specification or artifact contract | SA | Step 3d declares; Phase 4 Amend enforces; Verdict audits |
| invocation | How the skill is called (parameters, context, documentation) | SG | Step 3d declares; Phase 4 Amend enforces |
| artifact | Output document (sections, fields, content) | EG | Step 3d declares; Phase 4 Amend enforces |
| quality | Quality improvement with no direct source-layer finding | QO | Step 3d declares; Phase 4 Amend enforces |

**Channel lock**: every Amend entry (change or dismissal) includes
`[remediation channel: spec / invocation / artifact / quality]`.

#### Schema 4 -- Enforcement Gate Registry

Before Step 3d and Phase 4 may proceed, all three gates must record PASS.
A FAIL result is a hard stop: Phase 4 is BLOCKED until the gate is resolved.

| Gate | Property | Resolves via | Hard-stop condition | Dependency |
|------|----------|-------------|--------------------|-----------  |
| G-1 | Source diversity: >=2 distinct Source types in Step 3b table | Add finding from missing layer; re-run G-1 | Phase 4 BLOCKED while G-1 = FAIL | Step 3c runs G-1; Verdict audits |
| G-2 | Action diversity: no two same-Source findings carry identical Action text | Revise duplicate Action to name distinct target; re-run G-2 | Phase 4 BLOCKED while G-2 = FAIL | Step 3c runs G-2; Verdict audits |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Relabel non-conforming entries; re-run G-3 | Phase 4 BLOCKED while G-3 = FAIL | Step 3c runs G-3; Verdict audits |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Use only the Source labels
declared in Schema 2 and the Severity labels declared in Schema 1.

**SA audit** -- scan for undeclared values:
- Are all inputs declared in the spec with source, type, and format?
- Is the role sequence and each role's handoff contract specified?
- Is the artifact contract complete (naming convention, required sections, content rules)?

**SG pre-audit** -- scan for predictable binding failures:
- Which declared inputs are unlikely to be derivable from the test invocation alone?

**EG pre-audit** -- scan for predictable contract violations:
- Are there artifact sections the spec requires that defined roles may structurally fail to produce?

**Auditor success criterion**: gaps from at least two distinct Source types (Schema 2) appear.
If gaps cluster at one type, examine harder before declaring done.

Produce the audit table (use only SA / SG / EG / QO from Schema 2;
use only P1 / P2 / P3 from Schema 1):

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

SA and SG gaps from Stage 1 are inputs to every phase. Do not re-derive them. Do not silently
resolve them.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

Required at the Setup boundary. For every SA gap in the Stage 1 relay, evaluate:

> Does this gap make implementation impossible (spec defect), or can the invoker supply
> the value at runtime even though the spec does not declare it?

Write an explicit entry for each SA gap:

```
SA-NN -> [result]:
  Gap: [what the spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
  If promoted: SG-NN label to use in all downstream phases (Schema 2 label lock applies)
```

After processing all SA gaps, update the relay:

```
[SA remaining: {{sa_remaining}}]   -- spec defects; block implementation if P1
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

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
enumerate which gaps from SA-TO-SG PROMOTION output and Stage 1 SG/EG list constrain this role:

```
[role: {{role_name}}]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps (contract violations expected): [list or "none -- confirmed"]
```

A role entry without explicit gap attribution is invalid. Write "none -- confirmed" if verified.

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

Phase 3 runs as an ordered sequence of four named sub-steps. Each sub-step has a declared
prerequisite from the Dependency column in the Trace Protocol Schemas. The prerequisite must
be satisfied before the sub-step begins.

---

##### Step 3a -- Severity Legend Reference

**Prerequisite**: Schema 1 (Severity Vocabulary) declared in Trace Protocol Schemas.
**Output**: confirmation that P1/P2/P3 are the active labels for this trace.

> Severity legend active for this trace:
> P1 = must address before artifact is useful | P2 = improve quality | P3 = advisory

All Step 3b entries must use only these labels. Any entry using a label outside P1/P2/P3
does not satisfy Step 3b minimum and must be corrected before Step 3c runs.

---

##### Step 3b -- Findings Table

**Prerequisite**: Step 3a complete (severity legend active).
**Output**: merged findings table with all gaps from Stage 1 and Stage 2.

Merge all gaps into the unified findings table. Use promoted Source labels (SG not SA for
promoted gaps; Schema 2 label lock). Use only P1/P2/P3 from Step 3a:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. Action text must name a component, section, or decision point.

---

##### Step 3c -- Enforcement Gates

**Prerequisite**: Step 3b populated (findings table complete with >=2 entries).
**Output**: explicit PASS or FAIL result for each gate from Schema 4.
**Hard-stop rule**: a FAIL on any gate BLOCKS entry to Step 3d and Phase 4. Resolve the
failing gate -- add or revise findings as needed, re-run the gate -- before proceeding.

**G-1 Source Diversity Gate**
- Property: >=2 distinct Source types present in Step 3b (Schema 4 G-1)
- Source types present in Step 3b: [list all Source values from table]
- Result: PASS / FAIL
- **If FAIL -- BLOCKED**: identify and add a finding from the missing source layer to Step 3b;
  re-run G-1. Do not proceed to Step 3d or Phase 4 while G-1 = FAIL.

**G-2 Action Diversity Gate**
- Property: no two same-Source findings carry identical Action text (Schema 4 G-2)
- Same-Source pairs reviewed: [list pairs and Action fields, or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL -- BLOCKED**: revise Action text for the duplicate pair to name distinct targets;
  re-run G-2. Do not proceed to Step 3d or Phase 4 while G-2 = FAIL.

**G-3 Severity Completeness Gate**
- Property: all Step 3b entries use only P1/P2/P3 (Schema 4 G-3; Schema 1 vocabulary lock)
- Severity labels in Step 3b: [list all Severity values used]
- Result: PASS / FAIL
- **If FAIL -- BLOCKED**: relabel non-conforming entries using Schema 1 vocabulary; re-run G-3.
  Do not proceed to Step 3d or Phase 4 while G-3 = FAIL.

---

##### Step 3d -- Channel Taxonomy Reference (Amend transition)

**Prerequisite**: Step 3c complete with G-1 = PASS, G-2 = PASS, G-3 = PASS.
This sub-step is the architectural bridge from Findings to Phase 4.
**Output**: confirmation that the remediation channel taxonomy (Schema 3) is active.

> Channel taxonomy active for Phase 4:
> spec / invocation / artifact / quality (from Schema 3)

Every Phase 4 Amend entry must include `[remediation channel: spec / invocation / artifact / quality]`.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: `{{PASS}}`], [G-2: `{{PASS}}`], [G-3: `{{PASS}}`],
[channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Gate pre-check**: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
All three must be PASS (Step 3c). If any records FAIL, Phase 4 is BLOCKED -- return to Step 3c.

Channel taxonomy from Step 3d: spec / invocation / artifact / quality.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Schema Compliance Audit)

The Verdict is a retrospective compliance-audit pass. Walk each Schema row from the Trace
Protocol Schemas declaration and verify its Dependency column was honored.

**Schema 1 -- Severity Vocabulary compliance**:
- Declared at: Trace Protocol Schemas (before Stage 1)
- Required by: Step 3a, Step 3b, Step 3c G-3, Phase 4 Amend
- Severity labels used in Step 3b: [list]
- Labels outside P1/P2/P3: [list or "none"]
- Schema 1 compliance: PASS / FAIL

**Schema 2 -- Gap Type Taxonomy compliance**:
- Declared at: Trace Protocol Schemas (before Stage 1)
- Required by: Stage 1, SA-TO-SG PROMOTION, Step 3b
- SA promotion honored (no SA labels for promoted gaps): YES / NO
- Schema 2 compliance: PASS / FAIL

**Schema 3 -- Remediation Channel Taxonomy compliance**:
- Declared at: Trace Protocol Schemas (before Stage 1); activated at Step 3d
- Required by: Phase 4 Amend entries
- Channels used in Amend: [list]
- Labels outside declared taxonomy: [list or "none"]
- Schema 3 compliance: PASS / FAIL

**Schema 4 -- Enforcement Gate Registry compliance**:
- G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
- Hard-stop honored (no Phase 4 entry while any gate = FAIL): YES / NO
- Schema 4 compliance: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-02 -- Single axis: Phrasing register (permission model with hard-stop blocking language)

**Axis**: Phrasing register -- the prompt is written as a permission model. Each phase and
sub-step opens with a permission grant: "You now have permission to begin [phase]." Each gate
and prerequisite condition is expressed as a permission condition: "Permission to enter Step 3b
requires Step 3a complete." Gate FAIL is expressed as a permission revocation: "PERMISSION
REVOKED. You may not begin Phase 4 while [gate] = FAIL." The schema registry appears before
Stage 1 as a "Protocol License" that must be accepted before any phase runs. The Verdict
phase (Phase 5) verifies that each permission condition was honored.

**Hypothesis**: V-02 R5 used imperative second-person commands but had no schema registry
(C-20 FAIL) and no Verdict phase (C-21 FAIL). The permission model in R6 V-02 adds both:
the Protocol License before Stage 1 is the schema registry, and Phase 5 is framed as a
"license audit." C-22 becomes structurally unavoidable: gate FAIL = permission revoked =
Phase 4 BLOCKED is not a suggestion but a permission boundary. C-23 emerges from the
permission sequence: each sub-step is a conditional permission that names its prerequisite.
Risk: "permission revoked" framing may feel bureaucratic; if tracers treat it as permission
theater rather than a genuine stop signal, C-22 degrades to label compliance. The Phase 5
license audit checks whether permissions were honored, not just labeled.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Protocol License

Accept this license before beginning Stage 1. It defines the valid labels, channels, and
gates for every phase. Referencing labels, channels, or gates not declared here is a
protocol violation.

**License Section A -- Severity Labels**

Declare these now. Write the definitions in your own words before Stage 1:

```
P1: [your definition -- when is a finding a blocker?]
P2: [your definition -- when is a quality improvement?]
P3: [your definition -- when is it advisory only?]
```

Permission: you may use P1, P2, P3 in Step 3b and Phase 4.
Permission revoked: any other label in Step 3b or Phase 4.

**License Section B -- Source Labels**

Active labels: SA / SG / EG / QO (meanings below).

- SA: spec does not declare this.
- SG: spec declares it; invoker probably cannot supply it from the invocation.
- EG: artifact contract requires it; role probably cannot produce it.
- QO: improvable, not a gap.

After SA-TO-SG PROMOTION: use SG label for promoted gaps. Using SA label for a promoted gap
is a protocol violation.

**License Section C -- Remediation Channels**

Active channels: spec / invocation / artifact / quality (meanings below).

- spec: change the skill specification or artifact contract.
- invocation: change how the skill is called.
- artifact: update the output document.
- quality: improve quality; no source-layer finding.

Permission: you may use these channels in Phase 4 Amend entries.
Requirement: every Amend entry (change or dismissal) must include
`[remediation channel: spec / invocation / artifact / quality]`.

**License Section D -- Enforcement Gate Conditions**

Three gates must be run in Step 3c. Each must record PASS before Phase 4 is permitted.

- G-1 (Source Diversity): >=2 distinct Source labels in Step 3b.
- G-2 (Action Diversity): no two same-Source findings carry identical Action text.
- G-3 (Severity Completeness): all Step 3b entries use only P1/P2/P3 (License A).

**PERMISSION CONDITION**: Phase 4 requires G-1 = PASS, G-2 = PASS, G-3 = PASS.
If any gate records FAIL -- PERMISSION REVOKED. You may not write Phase 4. Resolve the
failing gate in Step 3c first, then re-run the gate.

---

### Stage 1 -- Spec Audit

**Permission to begin Stage 1**: Protocol License accepted above. Sections A-D declared.

Read `{{skill_spec_path}}`. Do not read the test invocation yet.

Find every gap. Use only SA / SG / EG / QO (License B).
Rate severity using only P1 / P2 / P3 (License A).

- SA: spec does not declare it.
- SG: spec declares it; invoker probably cannot supply it.
- EG: contract requires it; role probably cannot produce it.
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

**Permission to begin Stage 2**: Stage 1 relay complete.

Carry these fields into every phase:

**Relay in**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`], [EG: `{{eg_list}}`],
[layer diversity: `{{diversity_status}}`].

Do not re-derive these gaps. Do not silently resolve them.

---

#### SA-TO-SG PROMOTION

**Permission to begin SA-TO-SG PROMOTION**: Stage 2 relay received.

Do this now, before Setup inputs. For each SA item in the relay, write one entry:

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

From here: use SG labels for promoted gaps (License B). SA labels for promoted gaps = protocol violation.

---

#### Phase 1 -- Setup

**Permission to begin Phase 1**: SA-TO-SG PROMOTION complete.

Confirm each input. Write `[name: value]`:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

For each role in `[roles: ...]`, write its gap attribution:

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

**Permission to begin Phase 2**: Phase 1 carry-forward complete.

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

**Permission to begin Phase 3**: Phase 2 carry-forward complete.

Phase 3 runs in strict sub-step order. Each sub-step declares its permission condition.

---

##### Step 3a -- Severity Legend Declaration

**Permission to begin Step 3a**: Protocol License Section A declared above.

Write the active severity legend for this trace:

| Label | Definition for this trace | When it blocks |
|-------|--------------------------|----------------|
| P1 | [write: what makes this finding a blocker?] | Verdict = NEEDS-SPEC-REVISION or NEEDS-REDESIGN if P1 unresolved |
| P2 | [write: what makes this a quality improvement?] | Address in Amend or schedule follow-on |
| P3 | [write: what makes this advisory only?] | Log; no gate impact |

**Permission granted**: you may now proceed to Step 3b. Step 3b requires Step 3a complete.

---

##### Step 3b -- Findings Table

**Permission to begin Step 3b**: Step 3a complete (severity legend written above).

Merge all gaps into the unified findings table. Use promoted Source labels. Use only P1/P2/P3:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

At least 2 entries. Use only labels from License B (Source) and License A (Severity).

**Permission granted**: you may now proceed to Step 3c once this table has >=2 entries.
Step 3c requires Step 3b populated.

---

##### Step 3c -- Enforcement Gates

**Permission to begin Step 3c**: Step 3b populated with >=2 entries.

Run all three gates. Record PASS or FAIL explicitly.
**If any gate records FAIL -- PERMISSION REVOKED: you may not begin Step 3d or Phase 4.**
Resolve the failing gate (add or revise findings, re-run the gate), then continue.

**G-1 Source Diversity Gate**
- Check: how many distinct Source types are in the table above?
- Types present: [list]
- Result: PASS / FAIL
- **If FAIL -- PERMISSION REVOKED for Step 3d and Phase 4**: add one finding from the missing
  layer. Re-run G-1. Do not proceed until G-1 = PASS.

**G-2 Action Diversity Gate**
- Check: for each pair of findings that share the same Source label, are their Action fields
  pointing at different targets (distinct spec sections, invocation parameters, or artifact sections)?
- Same-Source pairs: [list or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL -- PERMISSION REVOKED for Step 3d and Phase 4**: revise the duplicate Action to name
  a distinct target. Re-run G-2. Do not proceed until G-2 = PASS.

**G-3 Severity Completeness Gate**
- Check: does every finding use only P1/P2/P3 (License A; Step 3a legend)?
- Labels in use: [list]
- Result: PASS / FAIL
- **If FAIL -- PERMISSION REVOKED for Step 3d and Phase 4**: relabel non-conforming entries.
  Re-run G-3. Do not proceed until G-3 = PASS.

**Permission granted for Step 3d**: G-1 = PASS, G-2 = PASS, G-3 = PASS.

---

##### Step 3d -- Channel Taxonomy Declaration (Amend Permission Gate)

**Permission to begin Step 3d**: Step 3c complete with all gates = PASS.

Write the active channel taxonomy for Phase 4:

```
Active channels for Phase 4 Amend:
  spec      = [write: what does changing the spec mean for this trace?]
  invocation = [write: what does changing the invocation mean?]
  artifact   = [write: what does updating the output document mean?]
  quality    = [write: when is a change quality-only?]
```

**Permission granted for Phase 4**: channel taxonomy declared. Every Amend entry must include
`[remediation channel: spec / invocation / artifact / quality]`.

Carry forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active].

---

#### Phase 4 -- Amend

**Permission to begin Phase 4**: Step 3c all gates PASS; Step 3d channel taxonomy declared.

Check permission conditions now:
- G-1: `{{PASS/FAIL}}` -- must be PASS. If FAIL: PERMISSION REVOKED. Return to Step 3c.
- G-2: `{{PASS/FAIL}}` -- must be PASS. If FAIL: PERMISSION REVOKED. Return to Step 3c.
- G-3: `{{PASS/FAIL}}` -- must be PASS. If FAIL: PERMISSION REVOKED. Return to Step 3c.

Apply the finding. Write all five fields. No exceptions:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; License B)
- [remediation channel: spec / invocation / artifact / quality] (License C; Step 3d)
- [change: ]
- [source confirmed: YES / NO]

For dismissals:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (License C; Step 3d)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- License Compliance Audit)

**Permission to begin Phase 5**: Phase 4 complete.

Audit whether each license section was honored.

**License A (Severity Vocabulary)**:
- Labels used in Step 3b: [list]
- Labels used in Phase 4: [list]
- All from P1/P2/P3: YES / NO
- License A: PASS / FAIL

**License B (Source Labels)**:
- SA-TO-SG PROMOTION completed: YES / NO
- SA labels appearing after promotion for promoted gaps: [list or "none"]
- License B: PASS / FAIL

**License C (Remediation Channels)**:
- Channels used in Phase 4: [list]
- All from declared taxonomy: YES / NO
- Every Amend entry includes channel field: YES / NO
- License C: PASS / FAIL

**License D (Enforcement Gates)**:
- G-1: PASS / FAIL | G-2: PASS / FAIL | G-3: PASS / FAIL
- Phase 4 entered while any gate = FAIL: YES (violation) / NO (clean)
- License D: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise. State the basis in one sentence tied to a named finding ID.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-03 -- Single axis: Lifecycle emphasis (Verdict as five-criterion compliance phase)

**Axis**: Lifecycle emphasis -- the Verdict is the structural weight center of this variation.
It is a full fifth lifecycle phase with five named compliance checks, one per new criterion
(C-20, C-21, C-22, C-23) plus one for the existing four-phase lifecycle. The schema registry
appears before Stage 1 as required by C-20 (compact and functional). The Findings sub-steps
(C-23) are named and declare explicit ordering constraints as transition conditions printed
at the end of each sub-step. The hard-stop gate condition (C-22) is expressed via a
"proceed condition" printed at the end of Step 3c. The Verdict audits compliance with all
five structural properties, making the post-Amend check the primary enforcement mechanism
rather than just a summary. Setup and Execute are compact; the structural weight is in
Findings and Verdict.

**Hypothesis**: V-03 R5 concentrated structural weight in Findings-to-Amend (the right
region for C-17/C-18/C-19). R6 V-03 extends this by making Verdict a primary enforcement
mechanism: the Verdict in R5 was a brief summary; here it becomes a five-criterion audit with
named checks. This tests whether C-21 can act as a backstop that catches C-20/C-22/C-23
failures retrospectively even if a tracer moves quickly through the schema registry and
Findings sub-steps. Risk: if the Verdict is the only enforcement point, a tracer who skips
Step 3a-to-3b dependency declarations can still complete all phases and face a failing Verdict
-- which is less valuable than a hard stop mid-trace. To hedge, the transition conditions at
each sub-step are explicit and named so failures are visible in-trace, not only at Verdict.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas

Declare before Stage 1. All phases reference only these labels and channels.

**Severity vocabulary** (active for all Findings entries and Amend entries):

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES -- trace result reflects open P1s |
| P2 | Should address to improve quality | NO -- address in Amend or follow-on |
| P3 | Advisory only -- no immediate action | NO -- log and proceed |

**Gap type taxonomy** (active for all Source columns):

| Type | Meaning |
|------|---------|
| SA | Spec absent -- spec does not declare this |
| SG | Setup gap -- declared; invoker probably cannot supply it |
| EG | Execute gap -- contract requires it; role probably cannot produce it |
| QO | Quality observation -- improvable, not a gap |

**Remediation channel taxonomy** (active for all Phase 4 Amend entries):

| Channel | Targets |
|---------|---------|
| spec | Skill specification or artifact contract |
| invocation | How the skill is called |
| artifact | Output document |
| quality | Quality improvement; no source-layer finding |

**Enforcement gates** (all three must record PASS before Phase 4):

| Gate | Property |
|------|---------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b |
| G-2 | Action diversity: no two same-Source findings share identical Action text |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before the test invocation. Audit for gaps across all three layers.

**SA** -- inputs, role handoffs, or artifact sections the spec does not declare.
**SG** -- inputs the spec declares but the test invocation likely cannot supply.
**EG** -- artifact sections or role outputs the defined roles may structurally fail to produce.

Auditor success criterion: gaps from at least two distinct source layers identified.
Examine harder if all gaps cluster at one layer.

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
appear. For each role: (a) what it received, (b) what it contributed, (c) any EG gaps
encountered. Mark artifact sections with EG gaps as `[EG-NN: reason]`. Do not infer silently.

**Carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], full gap inventory from Stages 1 and 2.

Phase 3 is an ordered sequence of four named sub-steps. Each sub-step prints a transition
condition at its end: what must be true before the next sub-step begins.

---

##### Step 3a -- Severity Legend Declaration

Declare the severity vocabulary for this trace. This declaration is a prerequisite for Step 3b.

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write: what makes a finding a blocker in this trace?] | Resolve before leaving Findings |
| P2 | [write: what makes it a quality improvement?] | Address in Amend or follow-on |
| P3 | [write: what makes it advisory?] | Log; no gate impact |

**Transition condition to Step 3b**: P1, P2, P3 defined above. All Step 3b entries use only
these labels. Entries using other labels do not satisfy the minimum threshold.

---

##### Step 3b -- Findings Table

**Prerequisite for this step**: Step 3a complete (legend declared above).

Merge all gaps into the unified findings table. Use promoted Source labels. Use only P1/P2/P3:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Transition condition to Step 3c**: findings table has >=2 entries. Step 3c gates run
against this table.

---

##### Step 3c -- Enforcement Gates

**Prerequisite for this step**: Step 3b populated with >=2 entries.

Run all three gates. Record PASS or FAIL for each.

**Proceed condition**: all three gates must record PASS before Step 3d begins. A FAIL on any
gate is a hard stop -- resolve the failing condition (add findings, revise actions, or relabel
entries as instructed), re-run the gate, then continue. Do not write Step 3d or Phase 4 while
any gate records FAIL.

**G-1 Source Diversity Gate**
- Property: at least 2 distinct Source types in Step 3b
- Source types present: [list all Source values from table]
- Result: PASS / FAIL
- If FAIL -- HARD STOP: identify a gap from the missing source layer; add to Step 3b; re-run G-1.

**G-2 Action Diversity Gate**
- Property: findings sharing the same Source label carry distinct Action directions
  (distinct targets: different spec sections, invocation parameters, or artifact sections)
- Same-Source groups: [for each group, list finding IDs and Action text]
- Result: PASS / FAIL
- If FAIL -- HARD STOP: revise Action text of conflicting entries to name distinct targets; re-run G-2.

**G-3 Severity Completeness Gate**
- Property: every finding uses only P1, P2, or P3 (from Step 3a legend)
- Severity labels present: [list all Severity values used]
- Result: PASS / FAIL
- If FAIL -- HARD STOP: relabel non-conforming entries using Step 3a vocabulary; re-run G-3.

**Transition condition to Step 3d**: G-1 = PASS, G-2 = PASS, G-3 = PASS. If any gate !=
PASS, do not proceed.

---

##### Step 3d -- Channel Taxonomy Reference (Amend bridge)

**Prerequisite for this step**: Step 3c complete with G-1 = PASS, G-2 = PASS, G-3 = PASS.

Activate the remediation channel taxonomy (from Trace Protocol Schemas) for Phase 4:
spec / invocation / artifact / quality.

Every Phase 4 Amend entry must include `[remediation channel: ...]`.

**Transition condition to Phase 4**: channel taxonomy active. All three gates PASS.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[channel taxonomy: spec/invocation/artifact/quality -- active from Step 3d],
[G-1: `{{PASS}}`], [G-2: `{{PASS}}`], [G-3: `{{PASS}}`].

---

#### Phase 4 -- Amend

Carrying forward: [highest_finding: `{{F-NN}}`], [source: `{{source}}`].
Channel taxonomy: spec / invocation / artifact / quality (Step 3d).
Gate status: G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.

All three gates must be PASS (Step 3c). If any is FAIL, return to Phase 3 Step 3c.

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

### Verdict (Phase 5 -- Five-Criterion Compliance Audit)

The Verdict audits five structural properties. Each is a named check. Record PASS or FAIL
for each. State the evidence.

**V-Check 1 -- Schema Registry (C-20)**:
- Were all schemas declared in "Trace Protocol Schemas" before Stage 1?
- Evidence: [confirm schemas present: severity vocabulary / gap taxonomy / channel taxonomy / gate registry]
- Result: PASS / FAIL

**V-Check 2 -- Post-Amend Audit (C-21)**:
- Is this Verdict a retrospective compliance audit of all phases? (This check being run = YES)
- Evidence: this phase (Phase 5) reviews all schema usage after Phase 4 completed.
- Result: PASS

**V-Check 3 -- Hard-Stop Gate Condition (C-22)**:
- Was Phase 4 entered only after all three gates recorded PASS?
- G-1 status when Phase 4 began: PASS / FAIL
- G-2 status when Phase 4 began: PASS / FAIL
- G-3 status when Phase 4 began: PASS / FAIL
- Phase 4 entered while any gate = FAIL: YES (violation) / NO (clean)
- Result: PASS / FAIL

**V-Check 4 -- Ordered Sub-Steps (C-23)**:
- Did Step 3b wait for Step 3a completion? [YES / NO]
- Did Step 3c wait for Step 3b population? [YES / NO]
- Did Step 3d wait for Step 3c all-PASS? [YES / NO]
- Did Phase 4 wait for Step 3d activation? [YES / NO]
- Result: PASS (all YES) / FAIL (any NO)

**V-Check 5 -- Four-Phase Lifecycle**:
- Stage 1 relay: [present / missing]
- SA-TO-SG PROMOTION: [present / missing]
- Phases 1-4: [present / partial / missing]
- Per-role gap attribution in Setup: [present / missing]
- Result: PASS / FAIL

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG active**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-04 -- Combined axes: Output format + lifecycle emphasis (coverage matrix schema registry + structural Verdict)

**Axes**:
- Output format: the schema registry before Stage 1 uses a "coverage matrix" format. Each
  schema row has four columns: Schema, Declared-at, Referenced-by, Verdict-check. The matrix
  makes the closed loop between declaration (C-20) and audit (C-21) visible at the top of the
  trace. The Findings sub-steps (C-23) declare their prerequisites in the same column format.
- Lifecycle emphasis: the Verdict is a full fifth phase that walks the coverage matrix row by
  row, verifying each declaration was used and each dependency was honored. The Verdict is the
  structural mirror of the schema registry: the registry declares dependencies; the Verdict
  verifies them.

**Hypothesis**: V-04 R5 combined two-stage auditor + maximum named event coverage, making
every criterion a first-class lifecycle event. R6 V-04 applies the same philosophy to all
four new criteria by creating a formal dependency-and-verification loop: declare schemas in a
coverage matrix (C-20), declare sub-step dependencies in the same column format (C-23),
enforce hard-stop gates (C-22), and verify the loop in the Verdict (C-21). The coverage matrix
acts as a contract: if a schema row says "Verdict-check: Schema 1" then the Verdict is
obligated to run that check. This makes C-21 structurally required rather than advisory --
skipping the Verdict leaves undischarged obligations in the matrix. Risk: the coverage matrix
adds mechanical overhead; if tracers treat matrix cells as checkboxes without reasoning, the
structural guarantees become surface compliance. The Verdict must go beyond checking that
cells are filled -- it must verify that the declared usage actually occurred in each phase.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

---

### Trace Protocol Schemas (Coverage Matrix)

Declare all schemas here before Stage 1 runs. The coverage matrix maps each schema to the
phases that require it and the Verdict check that audits it. All phases reference only the
labels declared here.

| Schema | Content | Declared-at | Referenced-by | Verdict-check |
|--------|---------|-------------|---------------|---------------|
| Severity Vocabulary | P1 / P2 / P3 (see below) | Here, before Stage 1 | Step 3a (declare), Step 3b (enforce), Step 3c G-3 (verify) | VC-1 |
| Gap Type Taxonomy | SA / SG / EG / QO (see below) | Here, before Stage 1 | Stage 1, SA-TO-SG PROMOTION, Step 3b Source column | VC-2 |
| Remediation Channel Taxonomy | spec / invocation / artifact / quality (see below) | Here, before Stage 1 | Step 3d (activate), Phase 4 Amend (enforce) | VC-3 |
| Enforcement Gate Registry | G-1, G-2, G-3 (see below) | Here, before Stage 1 | Step 3c (run), Phase 4 pre-check (enforce) | VC-4 |
| Sub-Step Ordering | 3a -> 3b -> 3c -> 3d (see below) | Here, before Stage 1 | Phase 3 (enforce transitions) | VC-5 |

#### Severity Vocabulary (Schema 1)

| Label | Definition | Blocks? |
|-------|-----------|---------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | YES |
| P2 | Should address to improve quality | NO |
| P3 | Advisory only -- no immediate action | NO |

#### Gap Type Taxonomy (Schema 2)

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through Setup and Execute |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable, not structural | Surface anywhere; P3 severity |

#### Remediation Channel Taxonomy (Schema 3)

| Channel | Targets | Activated-at |
|---------|---------|-------------|
| spec | Skill specification or artifact contract | Step 3d |
| invocation | How the skill is called | Step 3d |
| artifact | Output document | Step 3d |
| quality | Quality improvement; no source-layer finding | Step 3d |

#### Enforcement Gate Registry (Schema 4)

| Gate | Property | Hard-stop condition |
|------|---------|-------------------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL |

#### Sub-Step Ordering (Schema 5)

| Step | Prerequisite | Produces | Unblocks |
|------|-------------|---------|---------|
| Step 3a | Schema 1 declared above | Severity legend for this trace | Step 3b |
| Step 3b | Step 3a complete | Findings table (>=2 entries) | Step 3c |
| Step 3c | Step 3b populated | Gate results (all must be PASS) | Step 3d |
| Step 3d | Step 3c all-PASS | Channel taxonomy activated | Phase 4 |

---

### Stage 1 -- Source-Layer Auditor

Read `{{skill_spec_path}}` before consulting the test invocation. Catalog every gap using
the Gap Type Taxonomy (Schema 2) and the Severity Vocabulary (Schema 1).

**SA audit**: inputs not declared, role handoffs not specified, artifact sections without content rules.
**SG pre-audit**: declared inputs the invocation likely cannot supply.
**EG pre-audit**: artifact contract requirements roles may structurally fail to produce.

Success criterion: gaps from at least two distinct Source types (Schema 2). Examine harder
if gaps cluster at one layer.

| ID | Gap | Source | Severity | Affects phase |
|----|-----|--------|----------|--------------|

**Stage 1 relay**:

```
[SA: {{sa_list}}]
[SG: {{sg_list}}]
[EG: {{eg_list}}]
[layer diversity: PASS (>=2 distinct source types) / FAIL]
```

---

### Stage 2 -- Hand-Compilation

**Relay received from Stage 1**: [SA: `{{sa_list}}`], [SG: `{{sg_list}}`],
[EG: `{{eg_list}}`], [layer diversity: `{{diversity_status}}`].

Do not re-derive gaps. Do not resolve silently.

---

#### SA-TO-SG PROMOTION (named lifecycle event)

At the Setup boundary. For every SA gap in the relay:

> Can the invoker supply this value at runtime even though the spec doesn't declare it?

```
SA-NN -> [result]:
  Gap: [what spec does not declare]
  Promotion: PROMOTES TO SG-NN / REMAINS SA
  Reason: [why -- one sentence]
```

Updated relay:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Schema 2 label lock: promoted gaps use SG label in all downstream phases.

---

#### Phase 1 -- Setup

Confirm each input with `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

**Per-role gap attribution** (role -> gaps): For each role, enumerate constraining gaps:

```
[role: {{role_name}}]
  SA/SG gaps binding this role: [list or "none -- confirmed"]
  EG gaps (contract violations expected): [list or "none -- confirmed"]
```

**Setup carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG total: `{{sg_total}}`].

---

#### Phase 2 -- Execute

Carrying forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. All artifact sections required by the spec must
appear. Per-role relay before each artifact section:

**Role relay -- [role name]**:
- Received from: [prior role or Setup]
- Received values: [name: value, ...]
- SA/SG gaps affecting this role: [list or "none -- confirmed"]
- Produced: [artifact content added]
- EG gaps encountered: [EG-NN list or "none"]

Do not infer silently.

**Execute carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carrying forward: [artifact: `{{artifact_path}}`], all gaps from Stages 1 and 2.

Phase 3 runs in the sub-step sequence declared in Schema 5. Each sub-step prints its
prerequisite (from Schema 5 Prerequisite column) and its transition condition (Unblocks column)
before beginning.

---

##### Step 3a -- Severity Legend Declaration

**Schema 5 prerequisite**: Schema 1 (Severity Vocabulary) declared in Coverage Matrix.
**Schema 5 output**: severity legend for this trace (unblocks Step 3b).

Write the active severity legend:

| Label | Definition for this trace | Actionability threshold |
|-------|--------------------------|------------------------|
| P1 | [write for this trace] | Resolve before leaving Findings |
| P2 | [write for this trace] | Address in Amend or follow-on |
| P3 | [write for this trace] | Log; no gate impact |

**Schema 5 transition**: Step 3a complete. Step 3b unblocked.

---

##### Step 3b -- Findings Table

**Schema 5 prerequisite**: Step 3a complete (severity legend written above).
**Schema 5 output**: findings table with >=2 entries (unblocks Step 3c).

Merge all gaps. Use promoted Source labels (Schema 2). Use only P1/P2/P3 (Step 3a):

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Schema 5 transition**: findings table populated with >=2 entries. Step 3c unblocked.

---

##### Step 3c -- Enforcement Gates

**Schema 5 prerequisite**: Step 3b populated (>=2 entries).
**Schema 5 output**: gate results (must be all-PASS to unblock Step 3d).

Run all three gates from Schema 4. Record PASS or FAIL explicitly.

**Hard-stop rule (Schema 4 hard-stop conditions)**: a FAIL on any gate BLOCKS Step 3d
and Phase 4. The gate's hard-stop condition is active. Resolve the failing condition,
re-run the gate, confirm PASS before proceeding.

**G-1 Source Diversity Gate** (Schema 4)
- Property: >=2 distinct Source types present in Step 3b
- Source types present: [list all Source values from table]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active for Step 3d and Phase 4. Add finding from missing
  source layer. Re-run G-1. Do not proceed until PASS.

**G-2 Action Diversity Gate** (Schema 4)
- Property: no two same-Source findings carry identical Action text
- Same-Source pairs reviewed: [list pairs with Action fields, or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active for Step 3d and Phase 4. Revise duplicate Actions
  to name distinct targets. Re-run G-2. Do not proceed until PASS.

**G-3 Severity Completeness Gate** (Schema 4)
- Property: all Step 3b entries use only P1/P2/P3 (Schema 1 vocabulary; Step 3a legend)
- Severity labels in Step 3b: [list all values used]
- Result: PASS / FAIL
- **If FAIL**: Schema 4 hard-stop active for Step 3d and Phase 4. Relabel non-conforming
  entries. Re-run G-3. Do not proceed until PASS.

**Schema 5 transition condition**: G-1 = PASS, G-2 = PASS, G-3 = PASS. Step 3d unblocked.

---

##### Step 3d -- Channel Taxonomy Activation (Amend bridge)

**Schema 5 prerequisite**: Step 3c all gates PASS.
**Schema 5 output**: Schema 3 channel taxonomy activated for Phase 4 (unblocks Phase 4).

Activate the remediation channel taxonomy from Schema 3:
spec / invocation / artifact / quality.

Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Schema 5 transition**: channel taxonomy active. Phase 4 unblocked.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Schema 4 pre-check** (hard-stop conditions): G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.
All must be PASS. If any = FAIL: Schema 4 hard-stop active. Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d (Schema 3): spec / invocation / artifact / quality.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; Schema 2 label lock)
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Schema 3)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Coverage Matrix Audit)

Walk the Coverage Matrix row by row. For each schema, verify the Declared-at, Referenced-by,
and Verdict-check columns were honored. Each Verdict-check (VC-N) maps to one coverage matrix
row.

**VC-1 -- Severity Vocabulary (Schema 1)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- Referenced in Step 3a: YES / NO
- Referenced in Step 3b (only P1/P2/P3 used): YES / NO -- labels used: [list]
- Referenced in Step 3c G-3 (severity completeness verified): YES / NO
- Labels outside P1/P2/P3 found anywhere: [list or "none"]
- VC-1 result: PASS / FAIL

**VC-2 -- Gap Type Taxonomy (Schema 2)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- SA-TO-SG PROMOTION ran (Schema 2 promotion rule honored): YES / NO
- SA labels appearing after promotion for promoted gaps: [list or "none"]
- Step 3b Source column uses only SA/SG/EG/QO: YES / NO
- VC-2 result: PASS / FAIL

**VC-3 -- Remediation Channel Taxonomy (Schema 3)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- Activated at Step 3d: YES / NO
- All Phase 4 Amend entries include channel field: YES / NO
- Channels used in Phase 4: [list]
- Channels outside spec/invocation/artifact/quality: [list or "none"]
- VC-3 result: PASS / FAIL

**VC-4 -- Enforcement Gate Registry (Schema 4)**:
- Declared before Stage 1 in Coverage Matrix: YES / NO
- G-1: [PASS/FAIL] | G-2: [PASS/FAIL] | G-3: [PASS/FAIL]
- Phase 4 entered while any gate = FAIL: YES (hard-stop violated) / NO (clean)
- VC-4 result: PASS / FAIL

**VC-5 -- Sub-Step Ordering (Schema 5)**:
- Step 3a ran before Step 3b: YES / NO
- Step 3b populated before Step 3c ran: YES / NO
- Step 3c all-PASS before Step 3d activated: YES / NO
- Step 3d activated before Phase 4 began: YES / NO
- VC-5 result: PASS (all YES) / FAIL (any NO)

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG total**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`

---

## V-05 -- Combined axes: Inertia framing + output format (schema registry with cost-of-missing statements)

**Axes**:
- Inertia framing: the schema registry before Stage 1 and each Findings sub-step is preceded
  by a "Without this:" statement that names the concrete failure mode the element prevents.
  The inertia framing motivates each structural step by making the cost of skipping it visible.
  The hard-stop gate condition carries an inertia statement: "Without the hard stop, a tracer
  who records FAIL and proceeds to Amend silently converts a structural protocol failure into
  an advisory." The Verdict's "Without this phase:" statement names the leakage it prevents.
- Output format: every schema declaration is a compact table. The sub-step ordering in
  Findings is declared as a prerequisite/output/transition triplet. The Verdict is structured
  as a compliance table walking each schema.

**Hypothesis**: V-05 R5 tested whether inertia cost statements plus compact tables could
eliminate C-17/C-18/C-19 failures. R6 V-05 extends the same combination to cover C-20 (schema
registry with cost statements motivate tracers to fill them), C-21 (Verdict framed as the
element that prevents schema compliance leakage), C-22 (the hard-stop has an inertia
statement making FAIL-and-proceed feel costly), and C-23 (each sub-step's inertia statement
explains why its ordering constraint exists). The hypothesis is that the combination of table
format (production pressure) and cost-of-skipping framing (motivation) makes all four new
criteria feel load-bearing rather than bureaucratic. Risk: inertia statements add prose
overhead that may reduce depth in later phases; tracers motivated by cost framing may fill
tables quickly rather than reasoning carefully. The compact table format partially hedges
this by keeping declarations concise.

---

You are running /trace-skill for: `{{skill_name}}`

**Skill spec**: `{{skill_spec_path}}`
**Test invocation**: `{{invocation}}`

**Without `/{{skill_name}}`**: a developer validating this skill reads the spec manually,
mentally simulates each role, and discovers gaps only after writing code. Each gap this trace
surfaces is a failure they would have paid for in rework. The source layer a gap lives in
determines who pays and when: a spec-layer gap caught here saves an implementation sprint;
the same gap found at runtime derails one.

---

### Trace Protocol Schemas

*Without this block:* schemas are declared inline across phases -- the Severity Vocabulary
appears in Findings, the Channel Taxonomy appears in Amend, the gate list is assembled on
the fly. A tracer who skips inline declarations produces a trace with inconsistent labels,
no channel fields, and unverifiable gate results. Declaring all schemas here, before Stage 1,
creates a protocol contract that every phase can reference and the Verdict can audit.

#### Severity Vocabulary

*Without this table:* two tracers on the same team produce findings using Critical/High or
Blocker/Minor -- incompatible tables that cannot be aggregated across traces. The table forces
convergence before any finding is written.

| Label | Definition | When it blocks |
|-------|-----------|----------------|
| P1 | Must address before artifact is useful -- blocks implementation or invocation | Verdict result = NEEDS-SPEC-REVISION or NEEDS-REDESIGN if P1 unresolved |
| P2 | Should address to improve quality -- not blocking | Address in Amend or schedule follow-on |
| P3 | Future consideration -- advisory; no immediate action | Log; no gate impact |

**Vocabulary lock**: all Step 3b entries and all Phase 4 Amend entries use only P1, P2, P3.

#### Gap Type Taxonomy

*Without this table:* SA and SG gaps are confused -- a tracer records SA for a gap that the
invoker could supply at runtime, and recommends "fix the spec" when the fix is "update the
invocation docs." Promotion at the Setup boundary becomes ambiguous without declared labels.

| Type | Meaning | Promotion rule |
|------|---------|----------------|
| SA | Spec absent -- spec does not declare this | Evaluate at SA-TO-SG PROMOTION; promoted gaps use SG label downstream |
| SG | Setup gap -- declared; invoker cannot supply it | Carry through phases; surface in Findings with SG label |
| EG | Execute gap -- contract requires it; role cannot produce it | Surface in Execute; carry to Findings |
| QO | Quality observation -- improvable, not structural | Surface anywhere; P3 severity typical |

#### Remediation Channel Taxonomy

*Without this table:* Amend entries describe changes without naming the layer they target.
A "fix" that should update the spec instead updates the artifact -- the finding recurs in the
next trace. The channel field makes the remediation target explicit and auditable.

| Channel | Targets | When to use |
|---------|---------|------------|
| spec | Skill specification or artifact contract | SA gap (spec defect); promoted SG that originated as spec omission |
| invocation | How the skill is called | SG gap (invoker must supply missing value) |
| artifact | Output document | EG gap (output section must be added or changed) |
| quality | Quality improvement; no source-layer finding | QO gap |

**Channel lock**: every Phase 4 Amend entry (change or dismissal) includes
`[remediation channel: spec / invocation / artifact / quality]`.

#### Enforcement Gate Registry

*Without this table:* gates are implied conventions -- a tracer who doesn't know the gate
exists skips it; one who knows it exists but doesn't record the result can't be audited.
Declaring gates here before Stage 1 makes them required fill-in items rather than optional checks.

*Without the hard-stop rule:* a tracer records FAIL on G-1 and proceeds to Amend anyway --
converting a structural gap (missing source layer) into a silently dismissed advisory. The
hard-stop prevents this.

| Gate | Property | Hard-stop condition | If FAIL |
|------|---------|-------------------|---------|
| G-1 | Source diversity: >=2 distinct Source types in Step 3b | Phase 4 BLOCKED while G-1 = FAIL | Add finding from missing layer; re-run G-1 |
| G-2 | Action diversity: no two same-Source findings share identical Action text | Phase 4 BLOCKED while G-2 = FAIL | Revise duplicate Action; re-run G-2 |
| G-3 | Severity completeness: all Step 3b entries use only P1/P2/P3 | Phase 4 BLOCKED while G-3 = FAIL | Relabel non-conforming entries; re-run G-3 |

---

### Stage 1 -- Source-Layer Auditor

*Without this stage:* the tracer enters hand-compilation blind to the gap topology. Spec-layer
gaps discovered mid-Execute force backtracking through phases already written.*

Read `{{skill_spec_path}}` and catalog gaps by layer:

**SA (spec absent)**: inputs not declared, role handoffs not specified, artifact sections
without content rules, decisions requiring knowledge outside the skill's scope.

**SG (setup gap)**: inputs the spec declares but that the invocation likely cannot supply.

**EG (execute gap)**: artifact contract requirements the defined roles may structurally fail
to produce.

Success criterion: at least two distinct source layers represented. Examine harder if gaps
cluster at one layer.

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

*Without SA-to-SG promotion here:* SA labels travel into Findings unchanged -- where they
suggest "fix the spec" even for gaps the invoker can resolve at runtime. Promotion here
prevents misdirected remediation recommendations.*

**SA-to-SG Promotion (Setup boundary)**:

For each SA gap in the Stage 1 relay, fill in this table:

| SA ID | Gap description | Promotes? | New SG ID (if promoted) | Reason |
|-------|-----------------|-----------|------------------------|--------|
| SA-NN | | YES / NO | SG-NN or n/a | |

Updated active gap list:

```
[SA remaining: {{sa_remaining}}]
[SG from promotion: {{sg_promoted}}]
[SG original: {{sg_original}}]
```

Confirm inputs using `[name: value]` notation:

- [topic: ]
- [scope_in: ]
- [scope_out: ]
- [roles: ]
- [stack: ] / [detection_method: ]
- [spec_version: ]

Per-role gap attribution (role -> gaps): For each role, name constraining gaps:

```
[role: {{role_name}}]
  SG/SA gaps binding this role: [list or "none -- confirmed"]
  EG gaps expected: [list or "none -- confirmed"]
```

**Carry-forward**: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`],
[SA remaining: `{{sa_remaining}}`], [SG active: `{{sg_active}}`].

---

#### Phase 2 -- Execute

Carry forward: [topic: `{{topic}}`], [scope: `{{scope}}`], [roles: `{{roles}}`].

Produce: `{topic}-skill-trace-{date}.md`. Every artifact section required by the spec must
appear. For each role: (a) what it received, (b) what it contributed, (c) any EG gaps
encountered. Mark artifact sections blocked by EG gaps as `[EG-NN: reason]`.

Do not infer. Do not fill gaps silently.

**Carry-forward**: [artifact: `{{artifact_path}}`], [EG added: `{{eg_new}}`].

---

#### Phase 3 -- Findings

Carry forward: [artifact: `{{artifact_path}}`], full gap inventory from Stages 1 and 2.

Phase 3 runs in ordered sub-steps. Each sub-step declares: (a) what it needs before starting,
(b) what it produces, (c) what it prevents if skipped.

---

##### Step 3a -- Severity Legend Declaration

*Without Step 3a first:* Step 3b findings use undeclared labels -- the Severity Completeness
Gate (G-3) cannot run correctly because there is no declared vocabulary to check against.
Declaring the legend before the table prevents retroactive relabeling.*

**Prerequisite**: Severity Vocabulary declared in Trace Protocol Schemas above.
**Produces**: active severity legend for this trace (unblocks Step 3b).

| Label | Definition for this trace | When it blocks |
|-------|--------------------------|----------------|
| P1 | [write: what makes a finding a blocker here?] | Verdict result reflects open P1s |
| P2 | [write: what makes a quality improvement here?] | Address in Amend or follow-on |
| P3 | [write: what is advisory here?] | Log; no gate impact |

**Step 3b unblocked**: severity legend declared. All Step 3b entries use only P1, P2, P3.

---

##### Step 3b -- Findings Table

*Without Step 3b before Step 3c:* gates run against an empty table -- they trivially pass
or cannot be evaluated. The table must be populated before gates are meaningful.*

**Prerequisite**: Step 3a complete (legend above active).
**Produces**: merged findings table (unblocks Step 3c).

Merge all gaps into the unified findings table. Use promoted Source labels. Use only P1/P2/P3:

| ID | Finding | Source | Severity | Action |
|----|---------|--------|----------|--------|

Minimum 2 entries. At least 2 distinct Source types.

**Step 3c unblocked**: findings table has >=2 entries.

---

##### Step 3c -- Enforcement Gates

*Without gates before Step 3d:* a tracer proceeds to Amend with a single-layer findings table
and an action diversity violation -- the most common structural failures in traces without
enforcement.*

*Without the hard stop:* a tracer who records FAIL and proceeds to Phase 4 anyway converts a
structural gap into a silently completed trace. The hard-stop condition is the enforcement
mechanism that makes gate FAIL meaningful.*

**Prerequisite**: Step 3b populated with >=2 entries.
**Produces**: all-PASS gate results (unblocks Step 3d). A FAIL on any gate hard-stops Step 3d
and Phase 4 until the gate is resolved and re-run.

**G-1 Source Diversity Gate**
- Property: >=2 distinct Source types in Step 3b (from Gap Type Taxonomy)
- Source types present: [list all Source values from table]
- Result: PASS / FAIL
- **If FAIL -- HARD STOP**: without a second source layer, the trace misses an entire
  failure category. Add a finding from the missing source layer. Re-run G-1. Do not proceed
  to Step 3d or Phase 4 until G-1 = PASS.

**G-2 Action Diversity Gate**
- Property: no two same-Source findings share identical Action text
- Same-Source pairs: [list pairs and Action fields, or "none -- all Source types unique"]
- Result: PASS / FAIL
- **If FAIL -- HARD STOP**: duplicate Actions give the implementer no prioritization signal.
  Revise Action text to name distinct targets. Re-run G-2. Do not proceed until G-2 = PASS.

**G-3 Severity Completeness Gate**
- Property: all Step 3b entries use only P1, P2, P3 (Step 3a legend; Severity Vocabulary)
- Labels in use: [list]
- Result: PASS / FAIL
- **If FAIL -- HARD STOP**: non-standard labels break cross-trace aggregation. Relabel
  non-conforming entries using Step 3a vocabulary. Re-run G-3. Do not proceed until G-3 = PASS.

**Step 3d unblocked**: G-1 = PASS, G-2 = PASS, G-3 = PASS.

---

##### Step 3d -- Channel Taxonomy Declaration (Amend bridge)

*Without Step 3d before Phase 4:* Amend entries lack channel fields -- remediations are
described without naming the layer they target. The finding may be fixed at the wrong layer.*

**Prerequisite**: Step 3c all-PASS.
**Produces**: Remediation Channel Taxonomy activated for Phase 4 (unblocks Phase 4).

Active channels for Phase 4 (from Remediation Channel Taxonomy declared above):

| Channel | Use when |
|---------|---------|
| spec | [write: when does this trace's Amend need to change the spec?] |
| invocation | [write: when does this trace's Amend need to change the invocation?] |
| artifact | [write: when does this trace's Amend need to change the output?] |
| quality | [write: when is an improvement quality-only?] |

Every Phase 4 Amend entry requires `[remediation channel: spec / invocation / artifact / quality]`.

**Phase 4 unblocked**: channel taxonomy active and all gates PASS.

---

**Findings carry-forward**: [highest_finding: `{{F-NN}}`], [source: `{{source}}`],
[G-1: PASS], [G-2: PASS], [G-3: PASS],
[channel taxonomy: active from Step 3d].

---

#### Phase 4 -- Amend

**Gate pre-check** (Enforcement Gate Registry): G-1 `{{PASS}}`, G-2 `{{PASS}}`, G-3 `{{PASS}}`.

*Without the pre-check:* a tracer who resolved a gate failure in Step 3c but forgot to
re-run the gate enters Phase 4 with an unverified gate status. The pre-check here catches it.*

All must be PASS. If any = FAIL: HARD STOP -- Phase 4 BLOCKED. Return to Step 3c.

Channel taxonomy from Step 3d: spec / invocation / artifact / quality.

Apply the finding. All fields required:

- [finding: `{{F-NN}}`]
- [source: `{{source}}`] (promoted label; Gap Type Taxonomy label lock)
- [remediation channel: spec / invocation / artifact / quality] (Step 3d)
- [section or field changed: ]
- [change: ]
- [source confirmed: YES -- fix is at the `{{source}}` layer / NO -- `{{explain}}`]

If dismissed:

- [finding: `{{F-NN}}`]
- [reason: ]
- [remediation channel: spec / invocation / artifact / quality] (Step 3d)
- [source type confirmed: YES / NO]

---

### Verdict (Phase 5 -- Schema Compliance Audit)

*Without this phase:* a tracer who used non-standard labels in Phase 4, or who skipped a
sub-step prerequisite in Phase 3, or who entered Phase 4 while a gate was still FAIL -- has
no audit surface. The Verdict catches schema violations that passed through earlier phases
undetected. Without the Verdict, the trace closes without a retrospective compliance check --
the protocol schemas declared at the top would be unverified commitments.*

Walk each schema declared in Trace Protocol Schemas. Record PASS or FAIL.

| Schema | Property audited | Evidence | Result |
|--------|-----------------|---------|--------|
| Severity Vocabulary | Only P1/P2/P3 used in Step 3b and Phase 4 | Labels found: [list] | PASS / FAIL |
| Gap Type Taxonomy | SA-TO-SG PROMOTION ran; no SA labels for promoted gaps downstream | Promoted gaps: [list]; SA after promotion: [list or "none"] | PASS / FAIL |
| Remediation Channel Taxonomy | Every Phase 4 entry includes channel field from declared taxonomy | Channels used: [list]; missing entries: [list or "none"] | PASS / FAIL |
| Enforcement Gate Registry | All gates PASS before Phase 4; hard-stop honored | G-1/G-2/G-3 at Phase 4 entry: [list]; Phase 4 while FAIL: YES/NO | PASS / FAIL |
| Sub-Step Ordering | 3a->3b->3c->3d order honored; each prerequisite satisfied | Step transitions honored: [YES/NO per transition] | PASS / FAIL |

**Stage 1 layer diversity**: `{{diversity_status}}`
**SA remaining**: [count] | **SG active**: [count] | **EG total**: [count]

**Trace result**: `USEFUL` | `NEEDS-REDESIGN` | `NEEDS-SPEC-REVISION`

`NEEDS-SPEC-REVISION` if any P1 SA gap remains SA after promotion.
`NEEDS-REDESIGN` if EG gaps exceed 3 and indicate a structural role gap.
`USEFUL` otherwise. State the basis in one sentence tied to a named finding ID.

**Artifact**: `simulations/trace/skill/{topic}-skill-trace-{date}.md`
