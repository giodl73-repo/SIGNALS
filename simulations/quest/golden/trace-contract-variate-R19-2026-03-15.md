# trace-contract Variate — Round 19

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v19 (C-08–C-53; Groups A–G; new criteria C-51/C-52/C-53)
**Round:** R19 — 3 new single-axis + 2 priority combinations targeting C-51, C-52, C-53

---

## Round 19 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (`findings-sealed:` field echoed in Summary section, mirroring the `[FINDINGS-COMPLETE count=N findings]` boundary token) | C-51 | R18 V-01 introduced `[FINDINGS-COMPLETE count=N findings]` at the findings boundary but the Summary section carries only a severity-count table — confirming findings completeness from the summary requires locating the boundary token in the instruction body; a `findings-sealed:` field that mirrors the boundary token exactly makes count-assertion verification available at the summary anchor without cross-referencing the findings boundary |
| V-02 | output-format (`[TAXONOMY-DECLARED version=N]` seal carrying an `AmendmentVersion:` counter so each amendment increments the declared version) | C-52 | R18 V-02 introduced `AmendmentProtocol:` governance and a `TaxonomyVersion: 1.0` field but the `[TAXONOMY-DECLARED]` seal does not carry the version counter — amendment count is verifiable only by reading the protocol field, not by inspecting the seal; a version counter on the seal (`[TAXONOMY-DECLARED version=N]`) converts amendment governance from a protocol obligation into a numeric invariant whose violation surfaces as a counter mismatch |
| V-03 | lifecycle-emphasis (Schema Diff Phase carries a named `FailureToken:` block declaring `SCHEMA-OMISSION-FAIL` reserved exclusively for row-absent failures, distinct from `SCHEMA-PHASE-FAIL` reserved for type-constraint violations) | C-53 | R18 V-03 named `SCHEMA-PHASE-FAIL` as the single failure token for both type violations and row omissions — an automated inspector cannot distinguish a type-violation failure from an omission failure by token comparison alone; a distinct `SCHEMA-OMISSION-FAIL` token for row-absent failures makes the failure category determinable by token inspection without reading the failure rationale, and prevents a type-violation finding from masking a co-occurring omission that requires a different remediation path |
| V-04 | output-format combination (findings-sealed summary echo from V-01 + versioned taxonomy seal from V-02) | C-51, C-52 | The findings-boundary echo axis (C-51) and the taxonomy-version-counter axis (C-52) operate at orthogonal structural layers — summary section and taxonomy declaration — with no shared state; combining them tests whether the two auditing-redundancy patterns reinforce each other at their respective anchor points without interference |
| V-05 | output-format + lifecycle-emphasis (all three R19 advances declared as co-equal contract-governance layers in a preamble: findings-sealed echo, versioned taxonomy seal, FailureToken distinction) | C-51, C-52, C-53 | Declaring `findings-sealed:` echo (C-51), `[TAXONOMY-DECLARED version=N]` counter (C-52), and `FailureToken: SCHEMA-OMISSION-FAIL` distinction (C-53) as a three-layer governance preamble before any execution begins forces all three to be structurally named and cross-referenced before census or gate work starts; later phases reference pre-declared governance layers by name rather than constructing them inline, and the summary-level audit can verify all three governance commitments from a single anchor |

---

## V-01 — Output Format: findings-sealed Echo in Summary Section

**axis:** output-format — Summary section carries a named `findings-sealed:` field that mirrors `[FINDINGS-COMPLETE count=N findings]` exactly, making count-assertion verification available at the summary anchor without locating the findings boundary in the instruction body

**hypothesis:** C-48 requires `[FINDINGS-COMPLETE count=N findings]` at the findings boundary. C-51 escalates: the Summary section should carry a `findings-sealed:` field whose value equals the boundary token verbatim, so that a summary-level audit can confirm findings completeness without cross-referencing the instruction body. In R18, V-01 introduced the count-bearing boundary token but the Summary section carries only a severity-count table — an auditor reading only the summary cannot confirm the count assertion without scrolling to the findings-closure boundary. The `findings-sealed:` field eliminates this cross-reference dependency: the summary is a self-contained audit anchor for findings completeness. Prediction: C-51 pass rate improves over V-R18 baseline; C-48 holds because the boundary token is still emitted; C-45, C-46, C-49, C-50 hold at baseline because this variation does not change the schema-diff, taxonomy, or omission-rule instructions.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — MechanismTypeTaxonomy Declaration**

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary and its amendment governance:

```
MechanismTypeTaxonomy:
  closed: true
  tokens:
    - missing-field
    - wrong-value
    - type-violation
    - schema-mismatch
    - obligation-gap
    - audit-trace-gap
    - other:{token}
  rule: every mechanism-type value in a finding block must be drawn from the tokens list above
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list, increment AmendmentVersion, and re-seal before writing any finding block that uses the new token
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy AmendmentVersion=0 is now the authoritative vocabulary for this trace. Compliance rule: any mechanism-type value not present in the declared tokens list constitutes a taxonomy violation detectable by comparison. AmendmentProtocol governs all extensions.]`

**Step 3 — GateTokenSchema (typed-column declaration)**

Declare the `GateTokenSchema` using the typed-column table format below. Derive from the spec — do not run the operation.

```
GateTokenSchema:
  required-fields:
    | field               | type                    | constraint                                    | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------------|---------------------|
    | census-distribution | string                  | non-null; matches mechanism-distribution line | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | must name §S5.5-Sub-task-A by identifier      | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | derived from mechanism-type-shared at Sub-B   |                     |
    | attestation-by      | string                  | non-null; census-owner role name              | attestation-result  |
    | attestation-result  | string                  | non-null; claim value from census owner       | attestation-by      |
    | verification-by     | string                  | non-null; witness role name                   | verification-result |
    | verification-result | string                  | non-null; independent verification outcome    | verification-by     |
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace: attestation-by and verification-by must both be non-null before gate close
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness is verified by row-count comparison: declared rows = sweep output rows
```

`[SCHEMA-SEALED]`

**Step 4 — ObligationBlock Construction**

Declare the complete obligation chain as a named, addressable block:

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A by section identifier
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates, emit amendment-finding before gate token
  Assert:   amendment-path-provenance — if gate-provenance absent or wrong source, emit amendment-finding before gate token
  Prohibit: census-distribution-overwrite — no role modifies census-distribution after S5.5 emits it
  Prohibit: silent-gate-close — gate boundary may not close with null attestation-by or null verification-by
  Prohibit: re-derive-mechanism — mechanism-type-shared at fill site must equal staging-line value; do not re-derive from findings
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is the authoritative obligation source. Sub-task A, Sub-task B, and S6.5 cross-reference by name only.]`

**Step 5 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, and MechanismTypeTaxonomy above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 6 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 7 — Schema Diff Phase**

Before the element-level diff, run the schema diff. Apply the OmissionRule declared in GateTokenSchema.

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. If sweep output rows < declared rows: SCHEMA-PHASE-FAIL — record which row(s) are absent and halt element diff until the gap is resolved.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field (OmissionRule: SCHEMA-PHASE-FAIL)` if field absent

Schema sweep row count: {N swept} / {N declared}. If N swept < N declared: write `SCHEMA-PHASE-FAIL` before proceeding.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; OmissionRule satisfied. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED]]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. An inspector may verify completeness by counting F-01 through F-N without re-entering finding content.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy — see [TAXONOMY-DECLARED]. Do not derive mechanism tokens from finding narrative — copy from the `mechanism-type:` field in each finding block.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 10 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings:
- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ findings, same token: `mechanism-type-shared: {token}`
- 2+ findings, mixed tokens: `mechanism-type-shared: mixed`

Rationale: `{sentence naming the shared mechanism — what it does to the contract, not the token name}`

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 11 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token using every required-field row from the sealed GateTokenSchema:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required, MUST differ from attestation-by}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null AND name distinct roles. Verify before writing the completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 12 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

findings-sealed: [FINDINGS-COMPLETE count=N findings]
schema-phase: {PASS | SCHEMA-PHASE-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

The `findings-sealed:` field value MUST be copied verbatim from the `[FINDINGS-COMPLETE count=N findings]` token emitted in Step 8. An auditor reading only the Summary section can confirm findings count without locating the Step 8 boundary token. If the counts differ, a findings-count discrepancy finding must be raised.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: [TAXONOMY-DECLARED version=N] with AmendmentVersion Counter

**axis:** output-format — `MechanismTypeTaxonomy` block carries an `AmendmentVersion:` counter and the `[TAXONOMY-DECLARED]` seal carries the version as `[TAXONOMY-DECLARED version=N]`, so each amendment increments the declared version and the count is verifiable by seal inspection alone

**hypothesis:** C-49 requires a named `AmendmentProtocol:` field in the taxonomy declaration. C-52 escalates: the `[TAXONOMY-DECLARED]` seal should carry a version counter — `[TAXONOMY-DECLARED version=N]` — so that amendment count is verifiable by seal inspection without reading the protocol text. In R18 V-02, the taxonomy carries `TaxonomyVersion: 1.0` and an `AmendmentProtocol:` field, but the `[TAXONOMY-DECLARED]` seal does not encode the version; a taxonomy block copied forward without updating the version field produces a seal that appears valid but reflects a stale amendment state. The version counter on the seal converts amendment governance from a protocol obligation into a numeric invariant: a seal version mismatch is detectable by comparison against the `AmendmentVersion:` field value without reading the protocol text. Prediction: C-52 pass rate improves over V-R18 baseline; C-49 holds because `AmendmentProtocol:` is still declared; C-48 holds because `[FINDINGS-COMPLETE count=N findings]` is still emitted; C-50 holds because `OmissionRule: SCHEMA-PHASE-FAIL` is still declared in the Schema Diff phase.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — MechanismTypeTaxonomy Declaration with Versioned Seal**

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary with amendment governance and a version counter:

```
MechanismTypeTaxonomy:
  closed: true
  tokens:
    - missing-field
    - wrong-value
    - type-violation
    - schema-mismatch
    - obligation-gap
    - audit-trace-gap
    - other:{token}
  rule: every mechanism-type value in a finding block must be drawn from the tokens list above
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment AmendmentVersion by 1, and re-seal as [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token; a taxonomy block copied forward into a new trace must update AmendmentVersion to 0 unless amendments carry over
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. The version counter is the amendment count: version=0 means no amendments have been applied. A seal carrying version=N and a block carrying AmendmentVersion=M where N != M constitutes a version-skew violation detectable by counter comparison alone. AmendmentProtocol governs all extensions.]`

**Step 3 — GateTokenSchema (typed-column declaration)**

Declare the `GateTokenSchema` using the typed-column table format below. Derive from the spec — do not run the operation.

```
GateTokenSchema:
  required-fields:
    | field               | type                    | constraint                                    | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------------|---------------------|
    | census-distribution | string                  | non-null; matches mechanism-distribution line | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | must name §S5.5-Sub-task-A by identifier      | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | derived from mechanism-type-shared at Sub-B   |                     |
    | attestation-by      | string                  | non-null; census-owner role name              | attestation-result  |
    | attestation-result  | string                  | non-null; claim value from census owner       | attestation-by      |
    | verification-by     | string                  | non-null; witness role name                   | verification-result |
    | verification-result | string                  | non-null; independent verification outcome    | verification-by     |
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace: attestation-by and verification-by must both be non-null before gate close
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result
```

`[SCHEMA-SEALED]`

**Step 4 — ObligationBlock Construction**

Declare the complete obligation chain as a named, addressable block:

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A by section identifier
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates, emit amendment-finding before gate token
  Assert:   amendment-path-provenance — if gate-provenance absent or wrong source, emit amendment-finding before gate token
  Prohibit: census-distribution-overwrite — no role modifies census-distribution after S5.5 emits it
  Prohibit: silent-gate-close — gate boundary may not close with null attestation-by or null verification-by
  Prohibit: re-derive-mechanism — mechanism-type-shared at fill site must equal staging-line value; do not re-derive from findings
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is the authoritative obligation source. Sub-task A, Sub-task B, and S6.5 cross-reference by name only.]`

**Step 5 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, and MechanismTypeTaxonomy (version=0) above are locked. Automate begins below. No modification permitted after this line. Any amendment to MechanismTypeTaxonomy after this point requires re-sealing with incremented version.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 6 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 7 — Schema Diff Phase**

Before the element-level diff, run the schema diff. Apply the OmissionRule declared in GateTokenSchema.

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. If sweep output rows < declared rows: SCHEMA-PHASE-FAIL.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field (OmissionRule: SCHEMA-PHASE-FAIL)` if field absent

Schema sweep row count: {N swept} / {N declared}. If N swept < N declared: write `SCHEMA-PHASE-FAIL` before proceeding.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; OmissionRule satisfied. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0]; if a new token is needed, apply AmendmentProtocol before writing this block]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

If any finding requires a new mechanism-type token: pause, apply AmendmentProtocol (add token to list, increment AmendmentVersion, re-seal as `[TAXONOMY-DECLARED version=N+1]`), then write the finding block.

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy at the current version — verify against the most recent `[TAXONOMY-DECLARED version=N]` seal.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 10 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings:
- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ findings, same token: `mechanism-type-shared: {token}`
- 2+ findings, mixed tokens: `mechanism-type-shared: mixed`

Rationale: `{sentence naming the shared mechanism — what it does to the contract, not the token name}`

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 11 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token using every required-field row from the sealed GateTokenSchema:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required, MUST differ from attestation-by}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null AND name distinct roles. Verify before writing the completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 12 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

taxonomy-version: [TAXONOMY-DECLARED version=N]
schema-phase: {PASS | SCHEMA-PHASE-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

The `taxonomy-version:` field value MUST copy the `[TAXONOMY-DECLARED version=N]` seal verbatim from Step 2 (or the most recent re-seal if amendments were applied). If the seal version and the `AmendmentVersion:` field in the taxonomy block differ, a version-skew finding must be raised before the summary is written.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: SCHEMA-OMISSION-FAIL as Distinct FailureToken

**axis:** lifecycle-emphasis — Schema Diff Phase declares a named `FailureToken:` block that distinguishes `SCHEMA-OMISSION-FAIL` (row absent from sweep) from `SCHEMA-PHASE-FAIL` (type-constraint violation on a present row), making failure category determinable by token comparison alone

**hypothesis:** C-50 requires `OmissionRule: SCHEMA-PHASE-FAIL` as the named failure criterion for absent GateTokenSchema rows. C-53 escalates: row-absent failures and type-constraint violations should emit different tokens — `SCHEMA-OMISSION-FAIL` for absent rows and `SCHEMA-PHASE-FAIL` for type violations on present rows — so that an automated inspector can categorize failures by token without reading the failure rationale. In R18 V-03, `SCHEMA-PHASE-FAIL` is used for both failure modes: a present row with a wrong type and an absent row both emit the same token. When both failure modes co-occur, the type-violation token can mask the omission because both produce `SCHEMA-PHASE-FAIL` and the remediation paths diverge — type violations require value correction while omissions require sweep coverage addition. A distinct `SCHEMA-OMISSION-FAIL` token makes the distinction inspectable by token comparison; a finding citing `SCHEMA-OMISSION-FAIL` unambiguously requires adding the missing row to the sweep, not fixing the value. Prediction: C-53 pass rate improves over V-R18 baseline; C-50 holds because `OmissionRule:` still names a failure criterion; C-45 holds because `SCHEMA-DIFF-COMPLETE` is still emitted; C-48 and C-49 hold at baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — MechanismTypeTaxonomy Declaration**

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary and its amendment governance:

```
MechanismTypeTaxonomy:
  closed: true
  tokens:
    - missing-field
    - wrong-value
    - type-violation
    - schema-mismatch
    - obligation-gap
    - audit-trace-gap
    - other:{token}
  rule: every mechanism-type value in a finding block must be drawn from the tokens list above
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment AmendmentVersion, and re-seal before writing any finding block that uses the new token
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy AmendmentVersion=0 is the authoritative vocabulary for this trace. AmendmentProtocol governs all extensions.]`

**Step 3 — GateTokenSchema (typed-column declaration) with FailureToken Declarations**

Declare the `GateTokenSchema` using the typed-column table format below. Derive from the spec — do not run the operation. The schema carries two named failure tokens governing schema-phase validation outcomes:

```
GateTokenSchema:
  required-fields:
    | field               | type                    | constraint                                    | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------------|---------------------|
    | census-distribution | string                  | non-null; matches mechanism-distribution line | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | must name §S5.5-Sub-task-A by identifier      | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | derived from mechanism-type-shared at Sub-B   |                     |
    | attestation-by      | string                  | non-null; census-owner role name              | attestation-result  |
    | attestation-result  | string                  | non-null; claim value from census owner       | attestation-by      |
    | verification-by     | string                  | non-null; witness role name                   | verification-result |
    | verification-result | string                  | non-null; independent verification outcome    | verification-by     |
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace: attestation-by and verification-by must both be non-null before gate close
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-OMISSION-FAIL independent of the element diff result — schema completeness is verified by row-count comparison; any shortfall triggers SCHEMA-OMISSION-FAIL
  FailureToken:
    SCHEMA-PHASE-FAIL: emitted when a GateTokenSchema row IS present in the sweep but its actual value VIOLATES the declared type constraint — the row was swept but the value is wrong; remediation path: correct the field value
    SCHEMA-OMISSION-FAIL: emitted when a GateTokenSchema row is ABSENT from the sweep output — the row was not swept at all; remediation path: add the missing row to the sweep and re-run; this token is DISTINCT from SCHEMA-PHASE-FAIL and indicates a different failure category that cannot be resolved by value correction alone
```

Token usage rule: `SCHEMA-PHASE-FAIL` and `SCHEMA-OMISSION-FAIL` must not be used interchangeably. An automated inspector can categorize schema failures by token comparison without reading the failure rationale text. A finding citing `SCHEMA-OMISSION-FAIL` requires sweep coverage correction; a finding citing `SCHEMA-PHASE-FAIL` requires value correction.

`[SCHEMA-SEALED — FailureToken declarations SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL are now the authoritative schema-failure vocabulary for this trace.]`

**Step 4 — ObligationBlock Construction**

Declare the complete obligation chain as a named, addressable block:

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A by section identifier
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates, emit amendment-finding before gate token
  Assert:   amendment-path-provenance — if gate-provenance absent or wrong source, emit amendment-finding before gate token
  Prohibit: census-distribution-overwrite — no role modifies census-distribution after S5.5 emits it
  Prohibit: silent-gate-close — gate boundary may not close with null attestation-by or null verification-by
  Prohibit: re-derive-mechanism — mechanism-type-shared at fill site must equal staging-line value; do not re-derive from findings
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is the authoritative obligation source. Sub-task A, Sub-task B, and S6.5 cross-reference by name only.]`

**Step 5 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema (FailureToken declarations sealed), ObligationBlock, and MechanismTypeTaxonomy above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 6 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 7 — Schema Diff Phase with Distinct FailureToken Emission**

Before the element-level diff, run the schema diff. The FailureToken declarations in GateTokenSchema govern which token to emit for each failure category.

**FailureToken reference:**
- Use `SCHEMA-PHASE-FAIL` when a row IS in the sweep but its value violates the declared type constraint
- Use `SCHEMA-OMISSION-FAIL` when a row is ABSENT from the sweep output entirely
- These tokens are NOT interchangeable; using one where the other applies constitutes a finding-classification error

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. If sweep output rows < declared rows, identify the missing row(s) — each missing row emits `SCHEMA-OMISSION-FAIL` independently.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES [{SCHEMA-PHASE-FAIL}]: {type constraint failed}` if present but type-violated
- `{field}: declared type {type} — [SCHEMA-OMISSION-FAIL]: row absent from sweep; remediation: add to sweep coverage` if field absent from sweep output

Schema sweep row count: {N swept} / {N declared}. Each absent row is independently logged with `SCHEMA-OMISSION-FAIL`. Each type-violated row is independently logged with `SCHEMA-PHASE-FAIL`.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; FailureToken vocabulary applied; SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL are categorically distinct. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED]]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

For schema-failure findings generated in Step 7, the `mechanism-type:` must use `type-violation` (for `SCHEMA-PHASE-FAIL`) or `schema-mismatch` (for `SCHEMA-OMISSION-FAIL`) — the FailureToken determines the mechanism-type choice without re-inspecting the finding rationale.

When all Expected entries and schema-failure findings have been written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. Do not derive mechanism tokens from finding narrative — copy from the `mechanism-type:` field in each finding block.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 10 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings:
- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ findings, same token: `mechanism-type-shared: {token}`
- 2+ findings, mixed tokens: `mechanism-type-shared: mixed`

Rationale: `{sentence naming the shared mechanism — what it does to the contract, not the token name}`

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 11 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token using every required-field row from the sealed GateTokenSchema:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required, MUST differ from attestation-by}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null AND name distinct roles. Verify before writing the completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 12 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL | both} — {N swept} / {N declared} GateTokenSchema rows swept
  (SCHEMA-PHASE-FAIL: type-constraint violations on present rows; SCHEMA-OMISSION-FAIL: rows absent from sweep)
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: findings-sealed Summary Echo + Versioned Taxonomy Seal (C-51 + C-52)

**axis:** output-format combination — Summary section carries `findings-sealed:` echoing the findings-boundary token (C-51) AND the `[TAXONOMY-DECLARED]` seal carries a version counter `[TAXONOMY-DECLARED version=N]` (C-52); these operate at orthogonal structural layers (summary anchor and taxonomy declaration) with no shared state

**hypothesis:** V-01 establishes that `findings-sealed:` in the summary makes findings count-assertion verification available without locating the boundary token in the instruction body (C-51). V-02 establishes that `[TAXONOMY-DECLARED version=N]` makes amendment count verifiable by seal inspection alone (C-52). Combining them targets both auditing-redundancy patterns at their respective anchor points: the summary carries findings completeness and the taxonomy seal carries amendment governance version. The two axes are structurally independent — `findings-sealed:` lives in Step 12 and `[TAXONOMY-DECLARED version=N]` lives in Step 2 — and combining them should not introduce interference. The summary section becomes a richer audit anchor: an auditor reading only the summary can verify both findings completeness (via `findings-sealed:`) and taxonomy governance state (via `taxonomy-version:` echoing the versioned seal). Prediction: C-51 and C-52 both pass; C-48, C-49, C-50, C-45, C-46 hold at baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — MechanismTypeTaxonomy Declaration with Versioned Seal**

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary with amendment governance and a version counter:

```
MechanismTypeTaxonomy:
  closed: true
  tokens:
    - missing-field
    - wrong-value
    - type-violation
    - schema-mismatch
    - obligation-gap
    - audit-trace-gap
    - other:{token}
  rule: every mechanism-type value in a finding block must be drawn from the tokens list above
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment AmendmentVersion by 1, and re-seal as [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token; a taxonomy block copied forward must update AmendmentVersion to 0 unless amendments carry over
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. The version counter is the amendment count: version=0 means no amendments. A version mismatch between this seal and the AmendmentVersion field is detectable by counter comparison alone. AmendmentProtocol governs all extensions.]`

**Step 3 — GateTokenSchema (typed-column declaration)**

Declare the `GateTokenSchema` using the typed-column table format below. Derive from the spec — do not run the operation.

```
GateTokenSchema:
  required-fields:
    | field               | type                    | constraint                                    | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------------|---------------------|
    | census-distribution | string                  | non-null; matches mechanism-distribution line | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | must name §S5.5-Sub-task-A by identifier      | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | derived from mechanism-type-shared at Sub-B   |                     |
    | attestation-by      | string                  | non-null; census-owner role name              | attestation-result  |
    | attestation-result  | string                  | non-null; claim value from census owner       | attestation-by      |
    | verification-by     | string                  | non-null; witness role name                   | verification-result |
    | verification-result | string                  | non-null; independent verification outcome    | verification-by     |
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace: attestation-by and verification-by must both be non-null before gate close
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness is verified by row-count comparison
```

`[SCHEMA-SEALED]`

**Step 4 — ObligationBlock Construction**

Declare the complete obligation chain as a named, addressable block:

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A by section identifier
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates, emit amendment-finding before gate token
  Assert:   amendment-path-provenance — if gate-provenance absent or wrong source, emit amendment-finding before gate token
  Prohibit: census-distribution-overwrite — no role modifies census-distribution after S5.5 emits it
  Prohibit: silent-gate-close — gate boundary may not close with null attestation-by or null verification-by
  Prohibit: re-derive-mechanism — mechanism-type-shared at fill site must equal staging-line value; do not re-derive from findings
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is the authoritative obligation source. Sub-task A, Sub-task B, and S6.5 cross-reference by name only.]`

**Step 5 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, and MechanismTypeTaxonomy (version=0) above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 6 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 7 — Schema Diff Phase**

Before the element-level diff, run the schema diff. Apply the OmissionRule declared in GateTokenSchema.

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. If sweep output rows < declared rows: SCHEMA-PHASE-FAIL.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field (OmissionRule: SCHEMA-PHASE-FAIL)` if field absent

Schema sweep row count: {N swept} / {N declared}. If N swept < N declared: write `SCHEMA-PHASE-FAIL` before proceeding.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; OmissionRule satisfied. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0]; apply AmendmentProtocol if new token needed]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. An inspector may verify completeness by counting F-01 through F-N without re-entering finding content.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy at the current declared version — verify against `[TAXONOMY-DECLARED version=N]`.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 10 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings:
- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ findings, same token: `mechanism-type-shared: {token}`
- 2+ findings, mixed tokens: `mechanism-type-shared: mixed`

Rationale: `{sentence naming the shared mechanism — what it does to the contract, not the token name}`

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 11 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token using every required-field row from the sealed GateTokenSchema:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required, MUST differ from attestation-by}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null AND name distinct roles. Verify before writing the completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 12 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

findings-sealed: [FINDINGS-COMPLETE count=N findings]
taxonomy-version: [TAXONOMY-DECLARED version=N]
schema-phase: {PASS | SCHEMA-PHASE-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

**Summary anchor rules:**
- `findings-sealed:` MUST equal the `[FINDINGS-COMPLETE count=N findings]` token from Step 8 verbatim. Count discrepancy = findings-count finding.
- `taxonomy-version:` MUST equal the `[TAXONOMY-DECLARED version=N]` seal from Step 2 (or most recent re-seal) verbatim. Version skew between this field and the `AmendmentVersion:` value in the taxonomy block = taxonomy-skew finding.
- An auditor reading only the Summary section can verify both findings completeness and taxonomy governance state from these two fields alone, without locating either the Step 8 boundary token or the Step 2 taxonomy declaration.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: All Three R19 Advances as Co-Equal Governance Preamble (C-51 + C-52 + C-53)

**axis:** output-format + lifecycle-emphasis — all three R19 governance advances are declared as a named `ContractGovernance:` preamble block before any execution begins; later phases reference pre-declared governance layers by name rather than constructing them inline; the Summary section echoes all three governance commitments as named fields

**hypothesis:** V-01, V-02, and V-03 each introduce a single governance advance inline at its natural construction point. The inline approach is correct but creates a discovery problem: an auditor reading the output must know which steps to inspect to verify each governance commitment. V-05 moves all three commitments into a named `ContractGovernance:` preamble declared before Step 1: `findings-sealed-rule:` (C-51), `taxonomy-version-rule:` (C-52), and `failure-token-rule:` (C-53) are each stated with their structural contract before any census or gate work begins. Later phases reference these rules by name — "per ContractGovernance findings-sealed-rule" — rather than restating them. The Summary section carries all three governance echo fields, becoming a complete audit anchor: an auditor reading only the preamble and summary can verify all three governance commitments without entering any intermediate step. The combined governance preamble also makes version-skew detection a single-location check: if any governance commitment was violated, the preamble carries the declared rule and the summary carries the observed state, and the discrepancy is localizable without scanning intermediate steps. Prediction: C-51, C-52, C-53 all pass; all prior criteria hold at baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### CONTRACT GOVERNANCE PREAMBLE

Before any execution step begins, the following governance rules are declared as a named block. All phases reference these rules by name; they are not restated inline.

```
ContractGovernance: {topic}-trace-contract
  findings-sealed-rule:
    description: The findings boundary token [FINDINGS-COMPLETE count=N findings] MUST be echoed verbatim in the Summary section as findings-sealed: [FINDINGS-COMPLETE count=N findings]; count-assertion verification is available from the summary anchor without locating the boundary token in the instruction body; a count discrepancy between boundary token and summary field constitutes a findings-count finding
    boundary-token: [FINDINGS-COMPLETE count=N findings]  (emitted in Step 8)
    summary-field: findings-sealed:  (emitted in Step 12)
    compliance: boundary-token value == summary-field value
  taxonomy-version-rule:
    description: The MechanismTypeTaxonomy seal MUST carry a version counter as [TAXONOMY-DECLARED version=N] matching the AmendmentVersion field; each amendment increments N; a seal version mismatch between [TAXONOMY-DECLARED version=N] and AmendmentVersion constitutes a taxonomy-skew finding detectable by counter comparison alone; taxonomy blocks copied forward without updating the counter are version-skew violations
    seal-format: [TAXONOMY-DECLARED version=N]  (emitted in Step 2 and on each re-seal)
    summary-field: taxonomy-version:  (emitted in Step 12)
    compliance: seal version == AmendmentVersion field == summary-field version
  failure-token-rule:
    description: Schema Diff phase failures must be categorized by named token; SCHEMA-PHASE-FAIL is reserved for type-constraint violations on rows that ARE present in the sweep; SCHEMA-OMISSION-FAIL is reserved for rows that are ABSENT from the sweep output; the two tokens must not be used interchangeably; token comparison alone determines failure category without reading failure rationale; a finding citing SCHEMA-OMISSION-FAIL requires sweep coverage correction; a finding citing SCHEMA-PHASE-FAIL requires value correction
    token-SCHEMA-PHASE-FAIL: row present in sweep, value violates type constraint
    token-SCHEMA-OMISSION-FAIL: row absent from sweep output entirely
    compliance: failure token must match the row's presence state in the sweep output
```

`[CONTRACT-GOVERNANCE-DECLARED — ContractGovernance preamble is the authoritative governance source for this trace. All three rules are active: findings-sealed-rule (C-51), taxonomy-version-rule (C-52), failure-token-rule (C-53). Steps 8, 2/amendments, 7, and 12 execute under these rules by reference.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — MechanismTypeTaxonomy Declaration**

Declare the closed mechanism-type vocabulary under ContractGovernance taxonomy-version-rule:

```
MechanismTypeTaxonomy:
  closed: true
  tokens:
    - missing-field
    - wrong-value
    - type-violation
    - schema-mismatch
    - obligation-gap
    - audit-trace-gap
    - other:{token}
  rule: every mechanism-type value in a finding block must be drawn from the tokens list above
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list, increment AmendmentVersion by 1, and re-seal as [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token; per ContractGovernance taxonomy-version-rule, copied taxonomy blocks must update AmendmentVersion to 0 unless amendments carry over
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — per ContractGovernance taxonomy-version-rule: version=0, no amendments applied. Version-skew detection: if this seal version != AmendmentVersion, a taxonomy-skew finding must be raised.]`

**Step 3 — GateTokenSchema (typed-column declaration)**

Declare the `GateTokenSchema` under ContractGovernance failure-token-rule:

```
GateTokenSchema:
  required-fields:
    | field               | type                    | constraint                                    | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------------|---------------------|
    | census-distribution | string                  | non-null; matches mechanism-distribution line | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | must name §S5.5-Sub-task-A by identifier      | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | derived from mechanism-type-shared at Sub-B   |                     |
    | attestation-by      | string                  | non-null; census-owner role name              | attestation-result  |
    | attestation-result  | string                  | non-null; claim value from census owner       | attestation-by      |
    | verification-by     | string                  | non-null; witness role name                   | verification-result |
    | verification-result | string                  | non-null; independent verification outcome    | verification-by     |
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace: attestation-by and verification-by must both be non-null before gate close
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-OMISSION-FAIL (per ContractGovernance failure-token-rule — distinct from SCHEMA-PHASE-FAIL which governs type-constraint violations on present rows)
  FailureToken:
    SCHEMA-PHASE-FAIL: row IS present in sweep, value violates type constraint; remediation: correct field value
    SCHEMA-OMISSION-FAIL: row is ABSENT from sweep entirely; remediation: add row to sweep coverage
```

`[SCHEMA-SEALED — per ContractGovernance failure-token-rule: SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL are declared as distinct tokens with distinct remediation paths.]`

**Step 4 — ObligationBlock Construction**

Declare the complete obligation chain as a named, addressable block:

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A by section identifier
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates, emit amendment-finding before gate token
  Assert:   amendment-path-provenance — if gate-provenance absent or wrong source, emit amendment-finding before gate token
  Prohibit: census-distribution-overwrite — no role modifies census-distribution after S5.5 emits it
  Prohibit: silent-gate-close — gate boundary may not close with null attestation-by or null verification-by
  Prohibit: re-derive-mechanism — mechanism-type-shared at fill site must equal staging-line value; do not re-derive from findings
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is the authoritative obligation source. Sub-task A, Sub-task B, and S6.5 cross-reference by name only.]`

**Step 5 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. ContractGovernance preamble, GateTokenSchema, ObligationBlock, and MechanismTypeTaxonomy above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 6 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 7 — Schema Diff Phase**

Per ContractGovernance failure-token-rule: apply SCHEMA-PHASE-FAIL for type violations on present rows; apply SCHEMA-OMISSION-FAIL for absent rows. These tokens are not interchangeable.

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. Any shortfall triggers SCHEMA-OMISSION-FAIL — record each absent row independently.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — [SCHEMA-PHASE-FAIL]: {type constraint failed}` if present but type-violated
- `{field}: declared type {type} — [SCHEMA-OMISSION-FAIL]: row absent from sweep; remediation per ContractGovernance failure-token-rule: add to sweep coverage` if field absent

Schema sweep row count: {N swept} / {N declared}. Absent rows emit SCHEMA-OMISSION-FAIL independently of type-violation rows.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; per ContractGovernance failure-token-rule SCHEMA-PHASE-FAIL/SCHEMA-OMISSION-FAIL applied as appropriate. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0]; per ContractGovernance taxonomy-version-rule, apply AmendmentProtocol before using any new token]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries and schema-failure findings have been written:

`[FINDINGS-COMPLETE count=N findings — per ContractGovernance findings-sealed-rule: this token will be echoed verbatim in Summary findings-sealed: field.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy at version declared in `[TAXONOMY-DECLARED version=N]`.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 10 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings:
- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ findings, same token: `mechanism-type-shared: {token}`
- 2+ findings, mixed tokens: `mechanism-type-shared: mixed`

Rationale: `{sentence naming the shared mechanism — what it does to the contract, not the token name}`

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 11 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token using every required-field row from the sealed GateTokenSchema:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required, MUST differ from attestation-by}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null AND name distinct roles. Verify before writing the completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 12 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

findings-sealed: [FINDINGS-COMPLETE count=N findings]
taxonomy-version: [TAXONOMY-DECLARED version=N]
schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL | both} — {N swept} / {N declared} GateTokenSchema rows swept
  (SCHEMA-PHASE-FAIL: {N} type-constraint violations; SCHEMA-OMISSION-FAIL: {N} absent rows)
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

**Summary governance verification (per ContractGovernance preamble):**
- `findings-sealed:` — per findings-sealed-rule: must equal `[FINDINGS-COMPLETE count=N findings]` from Step 8 verbatim; count discrepancy = findings-count finding
- `taxonomy-version:` — per taxonomy-version-rule: must equal `[TAXONOMY-DECLARED version=N]` seal verbatim; version != AmendmentVersion = taxonomy-skew finding
- `schema-phase:` — per failure-token-rule: SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL reported as distinct failure categories; "both" is valid when co-occurring; they must not be merged into a single token

An auditor reading only the ContractGovernance preamble and this Summary section can verify all three R19 governance commitments — findings completeness (C-51), taxonomy version integrity (C-52), and schema-failure categorization (C-53) — without entering any intermediate step.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
