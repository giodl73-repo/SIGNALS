# trace-contract Variate — Round 17

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v17 (C-08–C-47; Groups A–G; new Group G criteria C-45/C-46/C-47)
**Round:** R17 — 3 new single-axis + 2 priority combinations targeting C-45, C-46, C-47

---

## Round 17 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | lifecycle-emphasis (Schema Diff phase is a named bounded phase that closes with `SCHEMA-DIFF-COMPLETE` token; element diff cannot begin until token is written) | C-45 | R16 Schema Diff is a sub-section of the post-run phase, not a bounded phase with a completion token — a type violation found in Step 5 (element diff) cannot be distinguished from a sweep omission; the `SCHEMA-DIFF-COMPLETE` token creates a phase boundary that makes schema coverage auditable independently of element coverage |
| V-02 | output-format (`MechanismTypeTaxonomy` declared inline as a closed enumerated set before the first finding block is written; every mechanism-type value must be drawn from the declared set) | C-46 | R16 finding block template carries mechanism-type as an inline comment listing allowed tokens; an inline comment describes the vocabulary but does not constitute a declaration — a non-taxonomy token produces a syntactically valid finding; a closed enumeration block forces C-22 conformance to be verifiable by reference to the declaration, not by matching against a comment |
| V-03 | phrasing-register (re-derivation prohibition moved from natural-language Sub-task B step text into `ObligationBlock: census-gate-obligations` as a `Prohibit:` command; fill-site compliance auditable by reading the obligation chain, not by finding and reading the step narrative) | C-47 | R16 re-derivation prohibition lives in Sub-task B step prose: "Do not re-derive it from the findings." This is an actionable instruction, but its compliance is verified by auditing step text rather than by inspecting the obligation chain; elevating it to `Prohibit:` within the named ObligationBlock makes it machine-inspectable alongside the six existing imperatives |
| V-04 | lifecycle-emphasis + output-format (bounded Schema Diff phase with `SCHEMA-DIFF-COMPLETE` token from V-01 combined with inline `MechanismTypeTaxonomy` declaration from V-02) | C-45, C-46 | V-01 and V-02 operate at orthogonal structural sites: V-01 closes the schema-diff phase before element-diff begins (post-run phase ordering); V-02 declares the mechanism-type vocabulary before findings begin (pre-findings declaration); combining them should not interfere because the phase-completion token appears after schema-field inspection rows and the taxonomy declaration appears before finding blocks — they share no state |
| V-05 | lifecycle-emphasis + output-format + phrasing-register (all three R17 advances declared as a new Contract Layer 4 — Verification Infrastructure Layer — in the preamble before any execution begins; schema-diff phase boundary, closed taxonomy, and re-derivation prohibition established as pre-declared infrastructure that later phases reference by name) | C-45, C-46, C-47 | Declaring `SCHEMA-DIFF-COMPLETE` as a named phase boundary, `MechanismTypeTaxonomy` as a closed declaration, and `Prohibit: re-derive-mechanism-type-shared` as an ObligationBlock imperative in a single preamble layer front-loads all three R17 advances before any census or expected-output work begins; later phases reference the pre-declared infrastructure by name rather than constructing it inline, making all three auditable from the preamble without re-reading step text |

---

## V-01 — Lifecycle Emphasis: Bounded Schema Diff Phase with SCHEMA-DIFF-COMPLETE Token

**axis:** lifecycle-emphasis — Schema Diff is a named, bounded phase that closes with `[SCHEMA-DIFF-COMPLETE]` token before the element diff begins; the element diff may not start until the token is written; the token is the observable evidence that every GateTokenSchema row was inspected before element-level comparison began
**hypothesis:** R16-V01 introduces a Schema Diff step (Step 5) that performs a per-field type sweep over GateTokenSchema rows before the element diff. This closes the C-19 silent-omission gap by running schema validation first. But the Schema Diff step has no phase-completion boundary — it is a sub-section of the post-run phase without a token that proves the sweep was complete when the element diff began. If a type violation is discovered during the element diff (Step 6) rather than the schema sweep (Step 5), there is no structural evidence that the schema sweep failed to catch it versus that the sweep was complete and the element diff independently found a type issue. Adding `[SCHEMA-DIFF-COMPLETE — all N GateTokenSchema fields inspected against type constraints. Element diff begins below.]` as a mandatory token after the last GateTokenSchema row inspection creates a verifiable phase boundary: a schema violation discovered after the token indicates a sweep omission (the sweep claimed to be complete but missed a field); a schema violation found during the sweep is part of the sweep record. Schema-validation coverage becomes auditable independently of element-diff coverage. Prediction: C-45 improves because the phase boundary is structurally enforced in the artifact; C-42, C-43, C-44 hold at R16-V05 baseline because this variation does not change the schema-typing, obligation, or audit-trace layers.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Gate Witness.

---

### ROLE: Connectors Contract Expert — Contract Layer Preamble

Before any census, expected-output, or gate work begins, declare three contract layers. All later phases reference them by name and do not restate their content.

**Contract Layer 1 — Schema Layer**

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                               | co-required-with    |
    |---------------------|-------------------------|------------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; must equal S5.5 source value  | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; must reference S5.5-SubA  | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens       | (none)              |
    | attestation-by      | string                  | non-empty role name; census owner        | attestation-result  |
    | attestation-result  | string                  | non-empty claim from census owner        | attestation-by      |
    | verification-by     | string                  | non-empty role name; witness             | verification-result |
    | verification-result | string                  | non-empty outcome from witness           | verification-by     |
  co-requirement: census-distribution and gate-provenance — both present or both absent; detectable by field inspection without prose
  audit-trace-gate: attestation-by, attestation-result, verification-by, verification-result — all four non-null before gate boundary closes
```

**Contract Layer 2 — Obligation Layer**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution value at S6.5 must equal value at S5.5; no role may alter it in transit between those sites
  Bind:     gate-provenance — value must be §S5.5-Sub-task-A in section-reference format; not a prose description, not an inferred reference
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5 value, emit amendment-finding before emitting gate token; token may not be emitted with a silent deviation
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding before emitting gate token
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5 emits it; S5.5 is the sole production site
  Prohibit: silent-gate-close — gate boundary may not be reached unless attestation-by and verification-by are both non-null at [TAXONOMY-CENSUS-COMPLETE]
```

**Contract Layer 3 — Audit Layer**

```
AuditProtocol: census-gate-audit
  execution-order: witness-first
    Phase W — Gate Witness runs before Census Owner; fills verification-by and verification-result independently
    Phase A — Census Owner runs after Phase W is complete; fills attestation-by and attestation-result
    isolation: witness does not see census owner's claim before Phase W completes; census owner does not see witness result before Phase A begins
  gate-close-condition: all four audit-trace fields non-null
    see: GateTokenSchema: census-gate-token (audit-trace-gate constraint)
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
  negative-constraint: no single role may satisfy both claim and proof
```

`[CONTRACT-LAYER-PREAMBLE-SEALED — Schema Layer, Obligation Layer, and Audit Layer established. Sub-task A through S6.5 reference these layers by name. Do not restate their content at later sites.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. For gate token elements, reference field names from GateTokenSchema: census-gate-token (Contract Layer 1).

`[SEALED — Contract Expert exits. Automate begins. No modification to Expected Output or Contract Layer Preamble permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 4 — Schema Diff Phase [Contract Layer 1 — BOUNDED PHASE]**

This is a bounded phase. It must complete and close with `[SCHEMA-DIFF-COMPLETE]` before Step 5 (element diff) begins. The completion token is the observable evidence that every GateTokenSchema row was inspected before element-level comparison began.

For every field row in GateTokenSchema: census-gate-token (Contract Layer 1), inspect the actual gate token value against the declared type constraint:

- `{field}: type {declared type} — actual: {observed value} — CONFORMS` if the value satisfies the declared type constraint
- `{field}: type {declared type} — actual: {observed value} — VIOLATES: {reason}` if the value fails

Rules:
- Every row in the GateTokenSchema typed-column table must receive an entry here. A missing row is a schema-sweep omission.
- Type violations become findings in Step 5 with `mechanism-type: type-violation`.
- A type violation discovered in Step 5 that is not present in this sweep indicates that this phase was incomplete when `[SCHEMA-DIFF-COMPLETE]` was written. If found, add the missed violation to this sweep and emit an amended `[SCHEMA-DIFF-COMPLETE]` before continuing the element diff.

After all GateTokenSchema rows have received an entry, write:

`[SCHEMA-DIFF-COMPLETE — all {N} GateTokenSchema fields inspected against type constraints. Element diff begins below.]`

The element diff in Step 5 may not begin before this token is written.

**Step 5 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output; not a restatement of what differed]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 6 — Sub-task A: Mechanism Distribution**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site: this line appears once, here. Do not produce it at Sub-task B or S6.5.
see: ObligationBlock: census-gate-obligations (Contract Layer 2)

**Step 7 — Sub-task B: Census Fill**

Write a `## Sub-task B: Census Fill` section.

For each candidate group from Sub-task A:

```
staging: group={mechanism-type-token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines. Do not re-derive from findings.

- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ same token: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {sentence naming the shared mechanism — what it does to the contract, not the token name}

see: ObligationBlock: census-gate-obligations — Assert: amendment-path-distribution, Assert: amendment-path-provenance (Contract Layer 2)

**Step 8 — Gate Witness Phase [Contract Layer 3 — Phase W]**

### ROLE: Gate Witness

You are the Gate Witness executing Phase W of AuditProtocol: census-gate-audit (Contract Layer 3). You run before the Census Owner. You have not seen the census owner's claim.

Locate the census-distribution value at §S5.5-Sub-task-A. Record verbatim: `source-record: {value}`

Compare against the census-distribution value in the actual gate token output char-for-char.

```
verification-by: Gate Witness
verification-result: {VERIFIED — census-distribution at S6.5 matches S5.5 source record char-for-char}
  OR
verification-result: {DEVIATION-FOUND: expected {S5.5 value}; actual {S6.5 value}}
```

`[PHASE-W-COMPLETE — Gate Witness exits. Phase A begins below. Witness result above is locked.]`

---

**Step 9 — Census Owner Attestation [Contract Layer 3 — Phase A]**

### ROLE: Census Owner (Contract Expert)

You are the Census Owner executing Phase A of AuditProtocol: census-gate-audit (Contract Layer 3). Phase W is complete and locked. You now attest independently.

```
attestation-by: Census Owner
attestation-result: {your independent claim — the census-distribution value you attest as correct}
```

---

### ROLE: Connectors Contract Expert — Gate Token Emission [S6.5]

**Step 10 — Gate Token**

Write a `## S6.5: Gate Token` section. Fill every field from GateTokenSchema: census-gate-token (Contract Layer 1).

```
gate-token:
  census-distribution: {value — carried forward from S5.5-Sub-task-A unchanged}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {from Phase A — copy verbatim}
  attestation-result: {from Phase A — copy verbatim}
  verification-by: {from Phase W — copy verbatim}
  verification-result: {from Phase W — copy verbatim}
```

Schema conformance check [Contract Layer 1 — GateTokenSchema typed-column]:
- census-distribution: string — {CONFORMS | VIOLATES}
- gate-provenance: format:S-section-ref — {CONFORMS | VIOLATES}
- gate-status: enum[PASS|FAIL] — {CONFORMS | VIOLATES}
- attestation-by: string non-empty — {CONFORMS | VIOLATES}
- attestation-result: string non-empty — {CONFORMS | VIOLATES}
- verification-by: string non-empty — {CONFORMS | VIOLATES}
- verification-result: string non-empty — {CONFORMS | VIOLATES}

Obligation enforcement [Contract Layer 2]:
see: ObligationBlock: census-gate-obligations — all six imperatives; do not restate

Audit-trace gate close [Contract Layer 3]:
see: AuditProtocol: census-gate-audit — all four audit-trace fields non-null: {YES/YES/YES/YES → gate closes | any NO → identify null field, emit amendment-finding, gate does not close}

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 11 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}
schema-diff: {N/7 fields inspected} — SCHEMA-DIFF-COMPLETE emitted [C-45]
schema-typed: {N/7 fields conform to typed-column constraints} [Contract Layer 1]
ObligationBlock: census-gate-obligations — cross-referenced at Sub-task A, Sub-task B, S6.5 [Contract Layer 2]
audit-trace: Phase W (verification-by={non-null}), Phase A (attestation-by={non-null}) [Contract Layer 3]

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: Inline MechanismTypeTaxonomy as Closed Enumerated Set

**axis:** output-format — `MechanismTypeTaxonomy` declared inline as a closed enumerated set before the first finding block is written; every `mechanism-type:` value in this trace must be drawn from the declared set; a value not in the set is a taxonomy violation; new tokens require amending the declaration before use
**hypothesis:** R16 variations carry the mechanism-type field in the finding block template as an inline comment — `mechanism-type: [missing-field | wrong-value | type-violation | ...]`. An inline comment describes the allowed tokens but does not constitute a declaration: an operator who writes `type-mismatch` instead of `type-violation` produces a syntactically valid finding block with a non-taxonomy token. C-22 requires mechanism-type constrained to taxonomy tokens; C-46 escalates: the taxonomy must be declared inline as a closed enumerated set so that conformance is verifiable by reference to the declaration without consulting external documentation. When `MechanismTypeTaxonomy` is declared as a named block before findings begin — with a `closed: true` constraint and an amendment protocol — the operator knows at write time that non-listed tokens are a declaration violation, not a style preference. An auditor can verify every mechanism-type value by comparison to a single named block. Prediction: C-46 improves because the inline declaration creates a reference anchor; C-22 improves because taxonomy conformance is now verifiable by inspection; C-45 holds at R16 baseline (no schema-diff phase boundary change); C-47 holds at R16 baseline (re-derivation prohibition remains in Sub-task B step text).

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Gate Witness.

---

### ROLE: Connectors Contract Expert — Contract Layer Preamble

Before any census, expected-output, or gate work begins, declare three contract layers.

**Contract Layer 1 — Schema Layer**

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                               | co-required-with    |
    |---------------------|-------------------------|------------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; must equal S5.5 source value  | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; must reference S5.5-SubA  | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens       | (none)              |
    | attestation-by      | string                  | non-empty role name; census owner        | attestation-result  |
    | attestation-result  | string                  | non-empty claim from census owner        | attestation-by      |
    | verification-by     | string                  | non-empty role name; witness             | verification-result |
    | verification-result | string                  | non-empty outcome from witness           | verification-by     |
  co-requirement: census-distribution and gate-provenance — both present or both absent
  audit-trace-gate: all four audit-trace fields non-null before gate boundary closes
```

**Contract Layer 2 — Obligation Layer**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution value at S6.5 must equal value at S5.5; no role may alter it in transit
  Bind:     gate-provenance — value must be §S5.5-Sub-task-A in section-reference format
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5 value, emit amendment-finding before emitting gate token
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding before emitting gate token
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5 emits it; S5.5 is sole production site
  Prohibit: silent-gate-close — gate boundary may not be reached unless attestation-by and verification-by are both non-null
```

**Contract Layer 3 — Audit Layer**

```
AuditProtocol: census-gate-audit
  execution-order: witness-first
    Phase W — Gate Witness runs before Census Owner; fills verification-by and verification-result independently
    Phase A — Census Owner runs after Phase W is complete; fills attestation-by and attestation-result
    isolation: witness does not see census owner's claim before Phase W completes
  gate-close-condition: all four audit-trace fields non-null
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
  negative-constraint: no single role may satisfy both claim and proof
```

`[CONTRACT-LAYER-PREAMBLE-SEALED — Schema Layer, Obligation Layer, and Audit Layer established. Sub-task A through S6.5 reference these layers by name.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case.

`[SEALED — Contract Expert exits. Automate begins. No modification to Expected Output or Contract Layer Preamble permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 4 — Schema Diff [Contract Layer 1]**

For each field in GateTokenSchema: census-gate-token typed-column table, compare the actual gate token value against the declared type constraint:

- `{field}: type {declared type} — actual: {observed value} — CONFORMS` if the value satisfies the type constraint
- `{field}: type {declared type} — actual: {observed value} — VIOLATES: {reason}` if the value fails

Type violations become findings in Step 6 with `mechanism-type: type-violation`.

**Step 5 — Mechanism-Type Taxonomy Declaration [C-46: CLOSED ENUMERATION — declare before writing any finding blocks]**

Before writing any finding blocks, declare the mechanism-type taxonomy inline as a closed enumerated set. Every `mechanism-type:` value in this trace must be drawn from this declared set. A value not in the set is a taxonomy violation — if discovered, add the new token here before using it in the finding block.

```
MechanismTypeTaxonomy:
  tokens:
    - missing-field         — a required field is absent from the actual output
    - wrong-value           — a field is present but its value does not satisfy the spec constraint
    - type-violation        — a field value fails the declared type constraint in GateTokenSchema
    - schema-mismatch       — the actual output structure does not conform to GateTokenSchema co-requirement
    - obligation-gap        — a Bind, Assert, or Prohibit command in ObligationBlock was not followed
    - audit-trace-gap       — an audit-trace field is null or absent at gate close
    - other:{token}         — a mechanism not covered by the above; token must be a hyphen-separated noun phrase
  closed: true
  amend: add new token to this list before using it; do not introduce tokens in finding blocks without amending this declaration first
```

`[TAXONOMY-DECLARED — mechanism-type taxonomy sealed. All finding mechanism-type values reference this declaration. A value not in the declared set is a C-46 violation.]`

**Step 6 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [{token from MechanismTypeTaxonomy — see TAXONOMY-DECLARED above; must be in declared set}]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible; not a restatement of what differed]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 7 — Sub-task A: Mechanism Distribution**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site.
see: ObligationBlock: census-gate-obligations (Contract Layer 2)

**Step 8 — Sub-task B: Census Fill**

Write a `## Sub-task B: Census Fill` section.

For each candidate group from Sub-task A:

```
staging: group={mechanism-type-token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines. Do not re-derive from findings.

- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ same token: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {sentence naming the shared mechanism — what it does to the contract}

see: ObligationBlock: census-gate-obligations (Contract Layer 2)

**Step 9 — Gate Witness Phase [Contract Layer 3 — Phase W]**

### ROLE: Gate Witness

You are the Gate Witness executing Phase W of AuditProtocol: census-gate-audit (Contract Layer 3). You run before the Census Owner.

Locate the census-distribution value at §S5.5-Sub-task-A. Record verbatim: `source-record: {value}`

```
verification-by: Gate Witness
verification-result: {VERIFIED — matches S5.5 source record char-for-char | DEVIATION-FOUND: expected {S5.5 value}; actual {S6.5 value}}
```

`[PHASE-W-COMPLETE — Gate Witness exits. Phase A begins. Witness result above is locked.]`

---

**Step 10 — Census Owner Attestation [Contract Layer 3 — Phase A]**

### ROLE: Census Owner (Contract Expert)

Phase W is complete and locked. You attest independently.

```
attestation-by: Census Owner
attestation-result: {your independent claim — census-distribution value you attest as correct}
```

---

### ROLE: Connectors Contract Expert — Gate Token Emission [S6.5]

**Step 11 — Gate Token**

Write a `## S6.5: Gate Token` section. Fill every field from GateTokenSchema: census-gate-token (Contract Layer 1).

```
gate-token:
  census-distribution: {value — carried forward from S5.5-Sub-task-A unchanged}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {from Phase A — copy verbatim}
  attestation-result: {from Phase A — copy verbatim}
  verification-by: {from Phase W — copy verbatim}
  verification-result: {from Phase W — copy verbatim}
```

Obligation enforcement [Contract Layer 2]:
see: ObligationBlock: census-gate-obligations — all six imperatives; do not restate

Audit-trace gate close [Contract Layer 3]:
see: AuditProtocol: census-gate-audit — all four audit-trace fields non-null → `[TAXONOMY-CENSUS-COMPLETE]`

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

mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}
mechanism-type-taxonomy: declared inline — {N} tokens enumerated — TAXONOMY-DECLARED [C-46]
schema-typed: {N/7 fields conform to typed-column constraints} [Contract Layer 1]
ObligationBlock: census-gate-obligations — cross-referenced at Sub-task A, Sub-task B, S6.5 [Contract Layer 2]
audit-trace: Phase W (verification-by={non-null}), Phase A (attestation-by={non-null}) [Contract Layer 3]

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Phrasing Register: Re-Derivation Prohibition Elevated into ObligationBlock

**axis:** phrasing-register — the re-derivation prohibition at the Sub-task B fill site is moved from natural-language step text into the named `ObligationBlock: census-gate-obligations` as a `Prohibit:` command; Sub-task B replaces the prose prohibition with a cross-reference to the ObligationBlock; fill-site compliance is auditable by inspecting the obligation chain, not by finding and reading the step narrative
**hypothesis:** R16 states the re-derivation prohibition as imperative prose in the Sub-task B step: "The `mechanism-type-shared` value at this fill site must equal the value derived from the staging line. Do not re-derive it from the findings." This is actionable and operators follow it, but its compliance is verified by auditing step text — a reader must find the Sub-task B narrative and confirm the prohibition was followed. The ObligationBlock (C-43) already collects the copy-forward, gate-provenance, amendment-path, and gate-close obligations as `Bind:`, `Assert:`, and `Prohibit:` commands, making those obligations verifiable by reading a single named block. The re-derivation prohibition is the only fill-site constraint that remains outside this block. Elevating it to `Prohibit: re-derive-mechanism-type-shared` within the ObligationBlock makes it machine-inspectable alongside the six existing imperatives: an auditor reads the ObligationBlock, sees seven imperatives, and checks each by reference — no step-text prose audit required. Sub-task B carries `see: ObligationBlock: census-gate-obligations (Prohibit: re-derive-mechanism-type-shared)` instead of the prose instruction. Prediction: C-47 improves because the prohibition is now part of the addressable obligation chain; C-43 improves because the ObligationBlock is now a complete picture of all fill-site constraints; C-33 and C-32 hold because the staging-line-to-fill-site relationship is unchanged in the artifact.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Gate Witness.

---

### ROLE: Connectors Contract Expert — Contract Layer Preamble

Before any census, expected-output, or gate work begins, declare three contract layers.

**Contract Layer 1 — Schema Layer**

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                               | co-required-with    |
    |---------------------|-------------------------|------------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; must equal S5.5 source value  | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; must reference S5.5-SubA  | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens       | (none)              |
    | attestation-by      | string                  | non-empty role name; census owner        | attestation-result  |
    | attestation-result  | string                  | non-empty claim from census owner        | attestation-by      |
    | verification-by     | string                  | non-empty role name; witness             | verification-result |
    | verification-result | string                  | non-empty outcome from witness           | verification-by     |
  co-requirement: census-distribution and gate-provenance — both present or both absent
  audit-trace-gate: all four audit-trace fields non-null before gate boundary closes
```

**Contract Layer 2 — Obligation Layer [C-47: re-derivation prohibition as Prohibit: command]**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution value at S6.5 must equal value at S5.5; no role may alter it in transit between those sites
  Bind:     gate-provenance — value must be §S5.5-Sub-task-A in section-reference format; not a prose description, not an inferred reference
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5 value, emit amendment-finding before emitting gate token; token may not be emitted with a silent deviation
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding before emitting gate token
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5 emits it; S5.5 is the sole production site
  Prohibit: silent-gate-close — gate boundary may not be reached unless attestation-by and verification-by are both non-null at [TAXONOMY-CENSUS-COMPLETE]
  Prohibit: re-derive-mechanism-type-shared — the mechanism-type-shared value at the Sub-task B fill site must equal the value derived from the staging lines at that phase; it must not be re-derived by re-reading finding text after staging lines are written; if staging lines yield token X, the fill site carries X — no re-examination of findings is permitted at the fill site
```

**Contract Layer 3 — Audit Layer**

```
AuditProtocol: census-gate-audit
  execution-order: witness-first
    Phase W — Gate Witness runs before Census Owner; fills verification-by and verification-result independently
    Phase A — Census Owner runs after Phase W is complete; fills attestation-by and attestation-result
    isolation: witness does not see census owner's claim before Phase W completes
  gate-close-condition: all four audit-trace fields non-null
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
  negative-constraint: no single role may satisfy both claim and proof
```

`[CONTRACT-LAYER-PREAMBLE-SEALED — Schema Layer, Obligation Layer (7 imperatives, including Prohibit: re-derive-mechanism-type-shared), and Audit Layer established. Sub-task A through S6.5 reference these layers by name. Do not restate their content at later sites.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case.

`[SEALED — Contract Expert exits. Automate begins. No modification to Expected Output or Contract Layer Preamble permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 4 — Schema Diff [Contract Layer 1]**

For each field in GateTokenSchema: census-gate-token typed-column table:

- `{field}: type {declared type} — actual: {observed value} — CONFORMS | VIOLATES: {reason}`

Type violations become findings in Step 5 with `mechanism-type: type-violation`.

**Step 5 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible; not a restatement of what differed]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 6 — Sub-task A: Mechanism Distribution**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site.
see: ObligationBlock: census-gate-obligations (Contract Layer 2 — Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 7 — Sub-task B: Census Fill**

Write a `## Sub-task B: Census Fill` section.

For each candidate group from Sub-task A:

```
staging: group={mechanism-type-token}, members={F-NN, ...}, count={N}
```

Select the pattern branch and emit `mechanism-type-shared` from the staging lines:

- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ same token: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {sentence naming the shared mechanism — what it does to the contract, not the token name}

see: ObligationBlock: census-gate-obligations (Contract Layer 2 — Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism-type-shared)

*The mechanism-type-shared value here must equal the staging-line value. The obligation to not re-derive is stated in the ObligationBlock above; it is not restated here.*

**Step 8 — Gate Witness Phase [Contract Layer 3 — Phase W]**

### ROLE: Gate Witness

You are the Gate Witness executing Phase W of AuditProtocol: census-gate-audit (Contract Layer 3). You run before the Census Owner.

Locate the census-distribution value at §S5.5-Sub-task-A. Record verbatim: `source-record: {value}`

```
verification-by: Gate Witness
verification-result: {VERIFIED — matches S5.5 source record char-for-char | DEVIATION-FOUND: expected {S5.5 value}; actual {S6.5 value}}
```

`[PHASE-W-COMPLETE — Gate Witness exits. Phase A begins. Witness result above is locked.]`

---

**Step 9 — Census Owner Attestation [Contract Layer 3 — Phase A]**

### ROLE: Census Owner (Contract Expert)

Phase W is complete and locked. You attest independently.

```
attestation-by: Census Owner
attestation-result: {your independent claim — census-distribution value you attest as correct}
```

---

### ROLE: Connectors Contract Expert — Gate Token Emission [S6.5]

**Step 10 — Gate Token**

Write a `## S6.5: Gate Token` section. Fill every field from GateTokenSchema: census-gate-token (Contract Layer 1).

```
gate-token:
  census-distribution: {value — carried forward from S5.5-Sub-task-A unchanged}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {from Phase A — copy verbatim}
  attestation-result: {from Phase A — copy verbatim}
  verification-by: {from Phase W — copy verbatim}
  verification-result: {from Phase W — copy verbatim}
```

Obligation enforcement [Contract Layer 2]:
see: ObligationBlock: census-gate-obligations — all seven imperatives; do not restate

Audit-trace gate close [Contract Layer 3]:
see: AuditProtocol: census-gate-audit — all four audit-trace fields non-null → gate closes

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 11 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}
schema-typed: {N/7 fields conform to typed-column constraints} [Contract Layer 1]
ObligationBlock: census-gate-obligations — 7 imperatives including Prohibit: re-derive-mechanism-type-shared; cross-referenced at Sub-task A, Sub-task B, S6.5 [Contract Layer 2 — C-47]
audit-trace: Phase W (verification-by={non-null}), Phase A (attestation-by={non-null}) [Contract Layer 3]

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Bounded Schema Diff Phase + Inline MechanismTypeTaxonomy

**axis:** lifecycle-emphasis + output-format (bounded Schema Diff phase with `SCHEMA-DIFF-COMPLETE` token from V-01 combined with inline `MechanismTypeTaxonomy` closed enumeration from V-02)
**hypothesis:** V-01 and V-02 target C-45 and C-46 through orthogonal structural sites. V-01 operates at the phase-boundary level in the post-run phase: the schema-diff sweep is a named bounded phase whose completion is marked by a token before element-level comparison begins, making schema coverage auditable independently of element coverage. V-02 operates at the findings-preamble level: the mechanism-type vocabulary is declared as a closed enumerated set before the first finding block is written, making C-22 conformance verifiable by reference to the inline declaration. The two axes do not share state: `SCHEMA-DIFF-COMPLETE` appears after the last GateTokenSchema row inspection entry and before Step 5 (element diff); `TAXONOMY-DECLARED` appears after the MechanismTypeTaxonomy block and before the first finding block in Step 5. They do not interfere because the phase-completion token governs phase ordering and the taxonomy declaration governs vocabulary; both are present in a single trace without structural conflict. The combination should improve C-45 and C-46 independently, and the presence of both declarations makes the post-run phase explicitly structured: schema sweep closes, taxonomy is declared, element diff begins. Prediction: C-45 and C-46 both improve over their single-axis baselines; C-47 holds at R16 baseline (re-derivation prohibition remains in step prose, not elevated to ObligationBlock); C-43 holds because the ObligationBlock structure is unchanged from R16-V05.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Gate Witness.

---

### ROLE: Connectors Contract Expert — Contract Layer Preamble

**Contract Layer 1 — Schema Layer**

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                               | co-required-with    |
    |---------------------|-------------------------|------------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; must equal S5.5 source value  | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; must reference S5.5-SubA  | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens       | (none)              |
    | attestation-by      | string                  | non-empty role name; census owner        | attestation-result  |
    | attestation-result  | string                  | non-empty claim from census owner        | attestation-by      |
    | verification-by     | string                  | non-empty role name; witness             | verification-result |
    | verification-result | string                  | non-empty outcome from witness           | verification-by     |
  co-requirement: census-distribution and gate-provenance — both present or both absent
  audit-trace-gate: all four audit-trace fields non-null before gate boundary closes
```

**Contract Layer 2 — Obligation Layer**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution value at S6.5 must equal value at S5.5; no role may alter it in transit
  Bind:     gate-provenance — value must be §S5.5-Sub-task-A in section-reference format
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5, emit amendment-finding before emitting gate token
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding before emitting gate token
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5 emits it; sole production site is S5.5
  Prohibit: silent-gate-close — gate boundary may not be reached unless attestation-by and verification-by are both non-null
```

**Contract Layer 3 — Audit Layer**

```
AuditProtocol: census-gate-audit
  execution-order: witness-first
    Phase W — Gate Witness runs before Census Owner; fills verification-by and verification-result independently
    Phase A — Census Owner runs after Phase W is complete; fills attestation-by and attestation-result
    isolation: witness does not see census owner's claim before Phase W completes
  gate-close-condition: all four audit-trace fields non-null
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
  negative-constraint: no single role may satisfy both claim and proof
```

`[CONTRACT-LAYER-PREAMBLE-SEALED — Schema Layer, Obligation Layer, and Audit Layer established. All later phases reference these layers by name.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case.

`[SEALED — Contract Expert exits. Automate begins. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 4 — Schema Diff Phase [Contract Layer 1 — BOUNDED PHASE]**

This phase must close with `[SCHEMA-DIFF-COMPLETE]` before Step 5 begins. Every GateTokenSchema field row must receive an entry. A row without an entry is a sweep omission. Type violations become findings in Step 5 with `mechanism-type: type-violation`.

For every field row in GateTokenSchema: census-gate-token:

- `{field}: type {declared type} — actual: {observed value} — CONFORMS`
- `{field}: type {declared type} — actual: {observed value} — VIOLATES: {reason}`

After all rows have been inspected:

`[SCHEMA-DIFF-COMPLETE — all {N} GateTokenSchema fields inspected against type constraints. Element diff begins below. A schema violation discovered in Step 5 that is not in this sweep indicates a sweep omission.]`

**Step 5 — Mechanism-Type Taxonomy Declaration + Findings**

Before writing any finding blocks, declare the mechanism-type taxonomy as a closed enumerated set.

```
MechanismTypeTaxonomy:
  tokens:
    - missing-field         — a required field is absent from the actual output
    - wrong-value           — a field is present but its value does not satisfy the spec constraint
    - type-violation        — a field value fails the declared type constraint in GateTokenSchema
    - schema-mismatch       — the actual output structure does not conform to GateTokenSchema co-requirement
    - obligation-gap        — a Bind, Assert, or Prohibit command in ObligationBlock was not followed
    - audit-trace-gap       — an audit-trace field is null or absent at gate close
    - other:{token}         — a mechanism not covered by the above; declare here before use
  closed: true
  amend: add new token here before using it in a finding block
```

`[TAXONOMY-DECLARED — mechanism-type taxonomy sealed. All finding mechanism-type values must be drawn from this set.]`

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [{token from MechanismTypeTaxonomy — see TAXONOMY-DECLARED above}]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 6 — Sub-task A: Mechanism Distribution**

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site.
see: ObligationBlock: census-gate-obligations (Contract Layer 2)

**Step 7 — Sub-task B: Census Fill**

For each candidate group from Sub-task A:

```
staging: group={mechanism-type-token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from staging lines. Do not re-derive from findings.

- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ same token: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {shared mechanism sentence — what it does to the contract}

see: ObligationBlock: census-gate-obligations (Contract Layer 2)

**Step 8 — Gate Witness Phase [Contract Layer 3 — Phase W]**

### ROLE: Gate Witness

You are the Gate Witness executing Phase W of AuditProtocol: census-gate-audit (Contract Layer 3). You run before the Census Owner.

Locate the census-distribution value at §S5.5-Sub-task-A. Record verbatim: `source-record: {value}`

```
verification-by: Gate Witness
verification-result: {VERIFIED | DEVIATION-FOUND: expected {S5.5 value}; actual {S6.5 value}}
```

`[PHASE-W-COMPLETE — Gate Witness exits. Phase A begins. Witness result locked.]`

---

**Step 9 — Census Owner Attestation [Contract Layer 3 — Phase A]**

### ROLE: Census Owner (Contract Expert)

Phase W is complete and locked. You attest independently.

```
attestation-by: Census Owner
attestation-result: {your independent claim — census-distribution value you attest as correct}
```

---

### ROLE: Connectors Contract Expert — Gate Token Emission [S6.5]

**Step 10 — Gate Token**

Write a `## S6.5: Gate Token` section. Fill every field from GateTokenSchema: census-gate-token (Contract Layer 1).

```
gate-token:
  census-distribution: {value — carried forward from S5.5-Sub-task-A unchanged}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {from Phase A — copy verbatim}
  attestation-result: {from Phase A — copy verbatim}
  verification-by: {from Phase W — copy verbatim}
  verification-result: {from Phase W — copy verbatim}
```

Obligation enforcement [Contract Layer 2]:
see: ObligationBlock: census-gate-obligations — all six imperatives; do not restate

Audit-trace gate close [Contract Layer 3]:
see: AuditProtocol: census-gate-audit — all four audit-trace fields non-null → `[TAXONOMY-CENSUS-COMPLETE]`

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 11 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}
schema-diff: {N/7 fields inspected} — SCHEMA-DIFF-COMPLETE emitted [C-45]
mechanism-type-taxonomy: declared inline — {N} tokens — TAXONOMY-DECLARED [C-46]
schema-typed: {N/7 fields conform to typed-column constraints} [Contract Layer 1]
ObligationBlock: census-gate-obligations — cross-referenced at Sub-task A, Sub-task B, S6.5 [Contract Layer 2]
audit-trace: Phase W (verification-by={non-null}), Phase A (attestation-by={non-null}) [Contract Layer 3]

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: All Three R17 Advances as Contract Layer 4 (Verification Infrastructure Layer)

**axis:** lifecycle-emphasis + output-format + phrasing-register (all three R17 advances declared as a new Contract Layer 4 — Verification Infrastructure Layer — in the preamble before any execution begins; the layer declares the bounded schema-diff phase with `SCHEMA-DIFF-COMPLETE` token [C-45], the inline `MechanismTypeTaxonomy` closed enumeration [C-46], and `Prohibit: re-derive-mechanism-type-shared` added to the ObligationBlock [C-47])
**hypothesis:** V-01, V-02, and V-03 each introduce one R17 advance as a single-axis change to the R16-V05 structure. In each case the advance is introduced at the point of use — the bounded phase is declared at Step 4 (schema diff), the taxonomy is declared at Step 5 (findings preamble), the prohibition is added to the ObligationBlock in the Contract Layer Preamble. Adding the advances at the point of use is correct; adding them to a dedicated preamble layer makes them collectively discoverable before execution begins. V-05 declares all three as Contract Layer 4: the Verification Infrastructure Layer. This layer states (1) that schema-diff is a bounded phase with `SCHEMA-DIFF-COMPLETE` as its completion token, (2) that the MechanismTypeTaxonomy is a closed enumerated set that governs all finding mechanism-type values, and (3) that the ObligationBlock carries `Prohibit: re-derive-mechanism-type-shared` as its seventh imperative. Contract Layer 4 is cross-referenced at Step 4, Step 5, and Sub-task B, exactly as Layers 1-3 are cross-referenced at their respective sites. The combination hypothesis: when all three R17 advances are declared as infrastructure before execution, operators engage with them as design constraints rather than as per-step instructions. The primary risk is that Contract Layer 4 reads as overhead alongside three prior layers; this risk is mitigated by keeping the layer declaration compact and referencing it by name at every applicable site.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Gate Witness.

---

### ROLE: Connectors Contract Expert — Contract Layer Preamble

Before any census, expected-output, or gate work begins, declare four contract layers. All later phases reference them by name and do not restate their content.

**Contract Layer 1 — Schema Layer**

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                               | co-required-with    |
    |---------------------|-------------------------|------------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; must equal S5.5 source value  | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; must reference S5.5-SubA  | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens       | (none)              |
    | attestation-by      | string                  | non-empty role name; census owner        | attestation-result  |
    | attestation-result  | string                  | non-empty claim from census owner        | attestation-by      |
    | verification-by     | string                  | non-empty role name; witness             | verification-result |
    | verification-result | string                  | non-empty outcome from witness           | verification-by     |
  co-requirement: census-distribution and gate-provenance — both present or both absent; detectable by field inspection without prose
  audit-trace-gate: attestation-by, attestation-result, verification-by, verification-result — all four non-null before gate boundary closes; detectable by value inspection without reading instruction trace
```

**Contract Layer 2 — Obligation Layer [C-43, C-47: seven imperatives including re-derivation prohibition]**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution value at S6.5 must equal value at S5.5; no role may alter it in transit between those sites
  Bind:     gate-provenance — value must be §S5.5-Sub-task-A in section-reference format; not a prose description, not an inferred reference
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5 value, emit amendment-finding before emitting gate token; token may not be emitted with a silent deviation
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding before emitting gate token
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5 emits it; S5.5 is the sole production site
  Prohibit: silent-gate-close — gate boundary may not be reached unless attestation-by and verification-by are both non-null at [TAXONOMY-CENSUS-COMPLETE]
  Prohibit: re-derive-mechanism-type-shared — the mechanism-type-shared value at the Sub-task B fill site must equal the value derived from the staging lines at that phase; it must not be re-derived by re-reading finding text after staging lines are written; if staging lines yield token X, the fill site carries X — no re-examination of findings is permitted at the fill site
```

**Contract Layer 3 — Audit Layer**

```
AuditProtocol: census-gate-audit
  execution-order: witness-first
    Phase W — Gate Witness runs before Census Owner; fills verification-by and verification-result independently
    Phase A — Census Owner runs after Phase W is complete; fills attestation-by and attestation-result
    isolation: witness does not see census owner's claim before Phase W completes; census owner does not see witness result before Phase A begins
  gate-close-condition: all four audit-trace fields non-null
    see: GateTokenSchema: census-gate-token (audit-trace-gate constraint)
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
  negative-constraint: no single role may satisfy both claim and proof; if Phase W and Phase A are assigned to the same operator identity, the audit protocol is violated
```

**Contract Layer 4 — Verification Infrastructure Layer [C-45, C-46, C-47]**

```
VerificationInfrastructure: trace-verification-protocol
  schema-diff-phase:
    bounded: true
    completion-token: SCHEMA-DIFF-COMPLETE
    invariant: element diff may not begin before SCHEMA-DIFF-COMPLETE is written
    coverage: every GateTokenSchema field row must receive an inspection entry before the token is written
    omission-rule: a type violation found in the element diff that is absent from the schema-diff sweep record indicates a sweep omission — retroactively add it to the sweep, then re-emit SCHEMA-DIFF-COMPLETE
    see: GateTokenSchema: census-gate-token (Contract Layer 1)
  mechanism-type-taxonomy:
    declaration-site: before first finding block
    declaration-token: TAXONOMY-DECLARED
    closed: true
    tokens:
      - missing-field         — a required field is absent from the actual output
      - wrong-value           — a field is present but its value does not satisfy the spec constraint
      - type-violation        — a field value fails the declared type constraint in GateTokenSchema
      - schema-mismatch       — the actual output structure does not conform to GateTokenSchema co-requirement
      - obligation-gap        — a Bind, Assert, or Prohibit command in ObligationBlock was not followed
      - audit-trace-gap       — an audit-trace field is null or absent at gate close
      - other:{token}         — a mechanism not covered by the above; declare here before use
    amend: add new token to this list before using it; do not introduce tokens in finding blocks without amending the declared taxonomy
    conformance: every mechanism-type value in this trace verifiable by reference to this declaration without consulting external documentation
  re-derivation-prohibition:
    see: ObligationBlock: census-gate-obligations (Prohibit: re-derive-mechanism-type-shared)
    enforcement-site: Sub-task B fill site
    audit-method: read ObligationBlock (Contract Layer 2) — the prohibition is the seventh imperative; do not audit by reading Sub-task B step text
```

`[CONTRACT-LAYER-PREAMBLE-SEALED — Schema Layer, Obligation Layer (7 imperatives), Audit Layer, and Verification Infrastructure Layer established. All later phases reference these layers by name. Do not restate their content at later sites.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. For gate token elements, reference field names from GateTokenSchema: census-gate-token (Contract Layer 1).

`[SEALED — Contract Expert exits. Automate begins. No modification to Expected Output or Contract Layer Preamble permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 4 — Schema Diff Phase [Contract Layer 4 — BOUNDED PHASE — schema-diff-phase protocol]**

This phase is governed by VerificationInfrastructure: trace-verification-protocol (Contract Layer 4, schema-diff-phase). It must close with `[SCHEMA-DIFF-COMPLETE]` before Step 5 begins. Every GateTokenSchema field row (Contract Layer 1) receives an inspection entry. A missing row is a sweep omission.

For every field row in GateTokenSchema: census-gate-token:

- `{field}: type {declared type} — actual: {observed value} — CONFORMS`
- `{field}: type {declared type} — actual: {observed value} — VIOLATES: {reason}`

Type violations become findings in Step 5 with `mechanism-type: type-violation`.

After all rows are inspected:

`[SCHEMA-DIFF-COMPLETE — all {N} GateTokenSchema fields inspected against type constraints. Element diff begins below.]`

*Per Contract Layer 4 schema-diff-phase invariant: Step 5 may not begin before this token is written.*

**Step 5 — Mechanism-Type Taxonomy Declaration + Findings [Contract Layer 4 — mechanism-type-taxonomy protocol]**

Before writing any finding blocks, emit the taxonomy declaration per VerificationInfrastructure (Contract Layer 4, mechanism-type-taxonomy):

```
MechanismTypeTaxonomy: [as declared in Contract Layer 4 — reproduce verbatim from preamble]
  tokens: missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}
  closed: true
```

`[TAXONOMY-DECLARED — mechanism-type taxonomy operative. All finding mechanism-type values must be drawn from this set. A value not in the set is a C-46 violation.]`

Write a `## Findings` section. Compare each Expected Output entry against the corresponding Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:

```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [{token from MechanismTypeTaxonomy — see Contract Layer 4 TAXONOMY-DECLARED}]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible; not a restatement of what differed]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 6 — Sub-task A: Mechanism Distribution**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site.
see: ObligationBlock: census-gate-obligations (Contract Layer 2 — Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 7 — Sub-task B: Census Fill**

Write a `## Sub-task B: Census Fill` section.

For each candidate group from Sub-task A:

```
staging: group={mechanism-type-token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from staging lines:

- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token from staging line}`
- 2+ same token: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {sentence naming the shared mechanism — what it does to the contract, not the token name}

see: ObligationBlock: census-gate-obligations (Contract Layer 2 — Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism-type-shared)
see: VerificationInfrastructure (Contract Layer 4 — re-derivation-prohibition: enforcement-site is this fill site)

**Step 8 — Gate Witness Phase [Contract Layer 3 — Phase W]**

### ROLE: Gate Witness

You are the Gate Witness executing Phase W of AuditProtocol: census-gate-audit (Contract Layer 3). You run before the Census Owner. You have not seen the census owner's claim.

Locate the census-distribution value at §S5.5-Sub-task-A. Record verbatim: `source-record: {value}`

```
verification-by: Gate Witness
verification-result: {VERIFIED — census-distribution at S6.5 matches S5.5 source record char-for-char}
  OR
verification-result: {DEVIATION-FOUND: expected {S5.5 value}; actual {S6.5 value}}
```

`[PHASE-W-COMPLETE — Gate Witness exits. Phase A begins below. Witness result above is locked.]`

---

**Step 9 — Census Owner Attestation [Contract Layer 3 — Phase A]**

### ROLE: Census Owner (Contract Expert)

You are the Census Owner executing Phase A of AuditProtocol: census-gate-audit (Contract Layer 3). Phase W is complete and locked. You attest independently.

```
attestation-by: Census Owner
attestation-result: {your independent claim — the census-distribution value you attest as correct}
```

---

### ROLE: Connectors Contract Expert — Gate Token Emission [S6.5]

**Step 10 — Gate Token**

Write a `## S6.5: Gate Token` section. Fill every field from GateTokenSchema: census-gate-token (Contract Layer 1).

```
gate-token:
  census-distribution: {value — carried forward from S5.5-Sub-task-A unchanged}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {from Phase A — copy verbatim}
  attestation-result: {from Phase A — copy verbatim}
  verification-by: {from Phase W — copy verbatim}
  verification-result: {from Phase W — copy verbatim}
```

Schema conformance [Contract Layer 1]:
- census-distribution: string — {CONFORMS | VIOLATES}
- gate-provenance: format:S-section-ref — {CONFORMS | VIOLATES}
- gate-status: enum[PASS|FAIL] — {CONFORMS | VIOLATES}
- attestation-by: string non-empty — {CONFORMS | VIOLATES}
- attestation-result: string non-empty — {CONFORMS | VIOLATES}
- verification-by: string non-empty — {CONFORMS | VIOLATES}
- verification-result: string non-empty — {CONFORMS | VIOLATES}

Obligation enforcement [Contract Layer 2]:
see: ObligationBlock: census-gate-obligations — all seven imperatives; do not restate

Audit-trace gate close [Contract Layer 3]:
see: AuditProtocol: census-gate-audit — all four audit-trace fields non-null: {YES/YES/YES/YES → gate closes | any NO → identify null field, emit amendment-finding, gate does not close}

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 11 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}
schema-diff: {N/7 fields inspected} — SCHEMA-DIFF-COMPLETE emitted [Contract Layer 4 / C-45]
mechanism-type-taxonomy: declared inline — {N} tokens — TAXONOMY-DECLARED [Contract Layer 4 / C-46]
schema-typed: {N/7 fields conform to typed-column constraints} [Contract Layer 1]
ObligationBlock: census-gate-obligations — 7 imperatives including Prohibit: re-derive-mechanism-type-shared; cross-referenced at Sub-task A, Sub-task B, S6.5 [Contract Layer 2 / C-47]
audit-trace: Phase W (verification-by={non-null}), Phase A (attestation-by={non-null}) [Contract Layer 3]
VerificationInfrastructure: all three R17 verification protocols applied [Contract Layer 4]

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
