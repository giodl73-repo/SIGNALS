# trace-contract Variate — Round 16

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v16 (C-08–C-44; Groups A–F; new Group F criteria C-42/C-43/C-44)
**Round:** R16 — 3 new single-axis + 2 priority combinations targeting C-42, C-43, C-44

---

## Round 16 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (GateTokenSchema as typed-column table — field / type / constraint / co-required-with) | C-42 | A schema declared as prose or free-form YAML can carry field names without type tokens; a typed-column table makes the type cell a required structural position — an untypd field produces a visually incomplete row, not a silently missing annotation |
| V-02 | lifecycle-emphasis (ObligationBlock as an explicit named construction phase before Sub-task A) | C-43 | All prior variations embed Bind/Assert/Prohibit inline at each instruction site; when ObligationBlock is a named construction phase — declared once, given an addressable name, cross-referenced everywhere — the name appears in the artifact as a reference anchor, not as repeated prose |
| V-03 | role-sequence (witness runs independently before census owner attests; gate token fields filled in two isolated steps) | C-44 | When witness fills verification-by/verification-result before census owner fills attestation-by/attestation-result, the gate token's two-party structure is enforced by execution order — the census owner cannot silently satisfy both fields because the witness fills theirs first under role isolation |
| V-04 | output-format + lifecycle-emphasis (typed schema table from V-01 + named ObligationBlock phase from V-02) | C-42, C-43 | The typed-schema axis (C-42) and the named-obligation axis (C-43) operate at orthogonal structural layers — schema declaration and imperative chain — with no shared state; combining them targets both without axis interference |
| V-05 | role-sequence + output-format + lifecycle-emphasis (all three R16 advances declared as co-equal contract layers in a preamble before any execution begins) | C-42, C-43, C-44 | Declaring the typed GateTokenSchema (C-42), the named ObligationBlock (C-43), and the audit-trace token structure (C-44) as a three-layer contract preamble before Sub-task A forces all three to be present and addressable before any census or gate work begins; later phases reference pre-declared layers by name rather than constructing them inline |

---

## V-01 — Output Format: Typed Schema Table for GateTokenSchema

**axis:** output-format — GateTokenSchema declared as a typed-column table with mandatory field / type / constraint / co-required-with columns
**hypothesis:** C-39 established the requirement for a named `GateTokenSchema` with a `required-fields:` manifest. C-42 escalates: each field must carry an explicit type constraint so that field-inspection validates value conformance, not just field presence. All prior variations allow field declarations in free-form YAML or prose — `census-distribution: required` satisfies C-39 without satisfying C-42 because there is no type token. A typed-column table makes the type cell a required structural position in the row. An untyped field produces a visually incomplete row — the type column is empty adjacent to a filled field name — rather than a silently missing annotation buried in prose. The operator cannot complete the table without filling the type column. Prediction: C-42 pass rate improves over V-R15 baseline because the table structure makes type-token absence a visible formatting gap; C-39 holds because the table still constitutes a named schema with required-fields manifest; C-43 and C-44 hold at baseline because this variation does not change the obligation or audit-trace instructions.

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

**Step 2 — GateTokenSchema (typed-column declaration)**

Before writing the Expected Output entries, declare the `GateTokenSchema` using the typed-column table format below. Derive the schema from the spec — do not run the operation.

```
GateTokenSchema:
  required-fields:
    | field               | type                  | constraint                              | co-required-with    |
    |---------------------|-----------------------|-----------------------------------------|---------------------|
    | census-distribution | {type token}          | {value constraint or cardinality rule}  | {co-required field} |
    | gate-provenance     | {type token}          | {value constraint or cardinality rule}  | {co-required field} |
    | gate-status         | {type token}          | {value constraint or cardinality rule}  | {co-required field} |
    | {additional fields} | {type token}          | {value constraint or cardinality rule}  | {co-required field} |
  co-requirement: {field-A} and {field-B} must both be present or both absent — a token carrying one without the other fails structural inspection
```

Type token vocabulary: `string`, `enum[VALUE-A|VALUE-B]`, `format: S-section-reference`, `boolean`, `integer`, `uri`. Use exactly one token per field. Do not use prose type descriptions (`"a string value"`, `"should be a reference"`).

Rules:
- Every row in the table is a field required by the spec. A row with an empty type cell is an incomplete schema declaration — fill it.
- `co-required-with` names the field that must co-appear; leave blank only if the field has no co-requirement.
- The schema is sealed by `[SCHEMA-SEALED]` written after the table. Do not modify the schema after the seal.

`[SCHEMA-SEALED]`

**Step 3 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. For the gate token elements, reference the declared GateTokenSchema fields by name.

When all spec-defined elements are listed, write:

`[SEALED — Contract Expert exits. Expected Output above is locked. Automate begins below. No modification to Expected Output or GateTokenSchema permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output section or the GateTokenSchema above the seal.

**Step 4 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior the operation produces — including every field in the emitted gate token, if any.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded, write: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 5 — Schema Diff**

Before the element-level diff, run the schema diff. Compare the actual gate token fields against the GateTokenSchema typed-column table.

For each field in the GateTokenSchema:
- `{field}: type {declared type} — actual value: {value} — CONFORMS` if the value satisfies the declared type constraint
- `{field}: type {declared type} — actual value: {value} — VIOLATES: {reason}` if the value fails the type constraint

A type violation is a finding (severity: `breaking` if a consumer would infer wrong behavior from the value type; otherwise `degraded`).

**Step 6 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 7 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

Collect all findings from Step 6. Produce one mechanism-distribution line:

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

This line must appear exactly once (sole production site). Do not derive mechanism tokens from the narrative — use the `mechanism-type:` field from each finding block.

**Step 8 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Select the appropriate pattern branch based on finding count:
- 0 findings: emit `mechanism-type-shared: none — contract satisfied`
- 1 finding: emit `mechanism-type-shared: {token from staging line}`
- 2+ findings, same token: emit `mechanism-type-shared: {token}`
- 2+ findings, mixed tokens: emit `mechanism-type-shared: mixed`

Rationale: `{sentence naming the shared mechanism — not the token name, but what the mechanism does to the contract}`

The `mechanism-type-shared` value at this fill site must equal the value derived from the staging line. Do not re-derive it from the findings.

**Step 9 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section.

Emit the gate token using the GateTokenSchema fields. Every required-field row in the sealed GateTokenSchema must appear in the gate token with a non-null value.

```
gate-token:
  census-distribution: {value — carries forward from S5.5-Sub-task-A unchanged}
  gate-provenance: {source reference — names S5.5-Sub-task-A by section identifier}
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name}
  attestation-result: {value or statement from census owner}
  verification-by: {witness role name}
  verification-result: {independent char-for-char verification outcome}
```

ObligationBlock: census-gate-obligations enforcement — verify:
- `census-distribution` was not modified after S5.5-Sub-task-A emitted it (`Prohibit: overwrite`)
- `gate-provenance` names the source by section identifier, not by inference (`Bind: gate-provenance rule`)
- Amendment path: if census-distribution deviated, amendment-finding was emitted before this token (`Assert: amendment path`)
- Gate boundary closes only when `attestation-by` and `verification-by` are both non-null (`Prohibit: silent gate close`)

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 10 — Summary**

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

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Lifecycle Emphasis: Named ObligationBlock Construction Phase

**axis:** lifecycle-emphasis — `ObligationBlock: census-gate-obligations` is an explicit named construction phase before Sub-task A; the block is declared once, given an addressable name, and cross-referenced by name from Sub-task A, Sub-task B, and S6.5 without restating the imperatives
**hypothesis:** C-40 established that all `Bind:` / `Assert:` / `Prohibit:` obligations must be declared as formal imperatives rather than prose. C-43 escalates: the complete obligation chain must be declared as a *named, addressable block* — `ObligationBlock: census-gate-obligations` — so that cross-reference inspection (not prose audit) enforces amendment-path consistency. In all R15 variations, the obligation chain is either embedded inline at each instruction site (V-02, V-04, V-05) or expressed as prose at Sub-task B (V-01). No variation declares the block once and then cross-references it by name. The result: even when V-04 and V-05 pass C-40, they fail C-43 because the same imperatives are restated at Sub-task A, Sub-task B, and S6.5 rather than referenced. Adding an explicit ObligationBlock construction phase — before Sub-task A begins — forces the operator to (1) name the block, (2) list all imperatives once, and (3) use `see: ObligationBlock: census-gate-obligations` at every subsequent site that would otherwise restate them. The cross-reference appears in the artifact as an auditable pointer. Prediction: C-43 pass rate improves over V-R15 baseline; C-40 holds because the named block still contains the full Bind/Assert/Prohibit chain; C-42 and C-44 hold at baseline because this variation does not change the schema-typing or audit-trace instructions.

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

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — ObligationBlock Construction**

Before writing any Expected Output entries and before beginning Sub-task A, declare the complete obligation chain as a named, addressable block.

```
ObligationBlock: census-gate-obligations
  Bind:   copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged; value at S6.5 must equal value produced at S5.5
  Bind:   gate-provenance — assign gate-provenance = source identifier §S5.5-Sub-task-A before emitting any gate token; source must be named by section reference, not inferred
  Assert: amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5 value, emit an amendment-finding before emitting the gate token; gate token may not be emitted with a deviated census-distribution without an amendment record
  Assert: amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit an amendment-finding before emitting the gate token
  Prohibit: census-distribution-overwrite — no role may modify or replace census-distribution after S5.5-Sub-task-A emits it; the sole production site is S5.5
  Prohibit: silent-gate-close — the gate boundary (§S6.5) may not close with null attestation-by or null verification-by; both audit-trace fields must carry non-null values before [TAXONOMY-CENSUS-COMPLETE] is written
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is now the authoritative obligation source for this trace. Sub-task A, Sub-task B, and S6.5 cross-reference this block by name. Do not restate these imperatives at those sites.]`

**Step 3 — GateTokenSchema**

Declare the `GateTokenSchema` from the spec:

```
GateTokenSchema: census-gate-token
  required-fields:
    - census-distribution: required  [co-required with: gate-provenance]
    - gate-provenance: required  [co-required with: census-distribution]
    - gate-status: required
    - attestation-by: required  [audit-trace: census owner role]
    - attestation-result: required  [audit-trace: claim value]
    - verification-by: required  [audit-trace: witness role]
    - verification-result: required  [audit-trace: verification outcome]
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace: attestation-by and verification-by must both be non-null before gate close
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
```

**Step 4 — Expected Output**

Write a `## Expected Output` section from the spec alone. The operation has not been run.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, error path, edge case.

When all spec-defined elements are listed:

`[SEALED — Contract Expert exits. Automate begins. Expected Output and ObligationBlock above are locked.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. The seal above is your start boundary. Your task: produce a complete, independent record of what the operation actually returned.

**Step 5 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field the operation produces including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 6 — Findings**

Write a `## Findings` section. Compare each Expected Output entry against Actual Output.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 7 — Sub-task A: Mechanism Distribution**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site: this line appears once, here. Do not produce it at Sub-task B or S6.5.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 8 — Sub-task B: Census Fill**

Write a `## Sub-task B: Census Fill` section.

For each candidate group from Sub-task A:
```
staging: group={mechanism-type-token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings:
- 0 findings: `mechanism-type-shared: none — contract satisfied`
- 1 finding: `mechanism-type-shared: {token}`
- 2+ same token: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {sentence naming the shared mechanism — what it does to the contract, not the token name}

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance)

**Step 9 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required}
  verification-result: {witness independent verification outcome — non-null required}
```

ObligationBlock enforcement — cite by name, do not restate:
see: ObligationBlock: census-gate-obligations — all six imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null. Verify before writing the completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 10 — Summary**

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
ObligationBlock: census-gate-obligations — applied at Sub-task A, Sub-task B, S6.5

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Role Sequence: Witness-First Audit for Audit-Trace Token Fields

**axis:** role-sequence — the witness role runs independently before the census owner attests; witness fills `verification-by:` and `verification-result:` in an isolated phase; census owner then fills `attestation-by:` and `attestation-result:` in a separate subsequent phase; gate token closes only when both phases have contributed non-null values
**hypothesis:** C-41 established two-party execution: census owner attests, witness verifies independently, no single role satisfies both. C-44 escalates: the gate token itself must carry `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:` as named audit-trace fields, with the gate boundary closing only when all four are non-null. In all R15 variations, the two-party instruction is at the S6.5 phase where the census owner and witness appear sequentially in the same instruction block. V-03 and V-05 pass C-41 by role-name separation, but both allow the two parties to contribute in the same execution step — a single operator can assign both roles' fields if the instruction boundary is merely textual. Reversing the sequence and adding role isolation makes the two-party requirement structural: the witness role fills its fields first (without seeing the census owner's claim), then the census owner fills its fields (using its own evidence, not the witness result). The gate token's audit-trace fields are filled in two isolated steps. The gate boundary can close only when both steps are complete. Prediction: C-44 pass rate improves over V-R15 baseline because the witness phase produces non-null `verification-by` and `verification-result` fields as its primary output before the census owner phase begins; the structure makes it impossible to emit a gate token with null audit-trace fields without the witness phase failing to produce output; C-41 holds; C-42 and C-43 hold at baseline.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate + Gate Witness.

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — GateTokenSchema**

Declare the `GateTokenSchema` from the spec:

```
GateTokenSchema: census-gate-token
  required-fields:
    - census-distribution: required  [co-required with: gate-provenance]
    - gate-provenance: required  [co-required with: census-distribution]
    - gate-status: required
    - attestation-by: required  [census-owner role name]
    - attestation-result: required  [census-owner claim]
    - verification-by: required  [witness role name — filled by Gate Witness phase]
    - verification-result: required  [witness outcome — filled by Gate Witness phase]
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace-gate: gate boundary closes only when attestation-by, attestation-result, verification-by, and verification-result are all non-null
```

**Step 3 — Expected Output**

Write a `## Expected Output` section from the spec. The operation has not been run.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, error path, edge case.

ObligationBlock: census-gate-obligations
  Bind:   census-distribution copies forward from S5.5 unchanged
  Bind:   gate-provenance references §S5.5-Sub-task-A by section identifier
  Assert: amendment-finding emitted before gate token if distribution deviates
  Prohibit: census-distribution-overwrite — sole production site is S5.5
  Prohibit: silent-gate-close — gate closes only when all four audit-trace fields are non-null

`[SEALED — Contract Expert exits. Automate begins. No modification to Expected Output permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here.

**Step 4 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field including all gate token fields the operation produces.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes for findings.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 5 — Findings**

Write a `## Findings` section.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause]
hypothesis: [mechanism sentence — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 6 — Sub-task A: Mechanism Distribution**

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site. Do not reproduce at Sub-task B or S6.5.

**Step 7 — Sub-task B: Census Fill**

For each candidate group:
```
staging: group={token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from staging lines:
- 0 findings: `mechanism-type-shared: none`
- 1 finding: `mechanism-type-shared: {token}`
- 2+ same: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {shared mechanism sentence — what it does to the contract}

**Step 8 — Gate Witness Phase [WITNESS-FIRST]**

The witness role runs before the census owner contributes attestation.

Write a `## Gate Witness Phase` section.

### ROLE: Gate Witness

You are the witness. You are performing independent verification before the census owner attests. You have not seen the census owner's claim. Your task: verify the census-distribution value char-for-char against the source record at §S5.5-Sub-task-A.

**Witness step 1 — Locate source record.** Find the census-distribution value as emitted at §S5.5-Sub-task-A. Record it verbatim: `source-record: {verbatim value from §S5.5}`

**Witness step 2 — Verify gate token value.** Compare the census-distribution in the gate token against the source record char-for-char. Produce your verification result:

```
verification-by: {your role name as witness — e.g., "Gate Witness"}
verification-result: {VERIFIED | DEVIATION-FOUND: {description of deviation}} — verified against source §S5.5-Sub-task-A char-for-char
```

Write: `[WITNESS-COMPLETE — Gate Witness exits. Census Owner phase begins below. Witness result above is locked.]`

---

**Step 9 — Census Owner Attestation Phase**

### ROLE: Census Owner (Contract Expert)

You are the census owner. The witness has completed their phase and their result is locked. You now attest to the census-distribution value independently.

**Attestation step.** Based on your own review of the census:

```
attestation-by: {census owner role name — e.g., "Census Owner"}
attestation-result: {your attestation claim — the census-distribution value you are asserting as correct}
```

---

### ROLE: Connectors Contract Expert — Gate Token Emission [S6.5]

**Step 10 — Gate Token**

Write a `## S6.5: Gate Token` section. Both audit-trace parties have contributed non-null values. Emit the complete gate token:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {value from Census Owner Attestation Phase — copy verbatim, do not re-derive}
  attestation-result: {value from Census Owner Attestation Phase — copy verbatim}
  verification-by: {value from Gate Witness Phase — copy verbatim, do not re-derive}
  verification-result: {value from Gate Witness Phase — copy verbatim}
```

Gate close verification:
- `attestation-by` is non-null: {YES | NO}
- `attestation-result` is non-null: {YES | NO}
- `verification-by` is non-null: {YES | NO}
- `verification-result` is non-null: {YES | NO}

All four non-null: {YES → gate closes | NO → gate cannot close — identify null field and emit amendment-finding}

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

mechanism-type-shared: {token}
gate-status: {PASS | FAIL}
audit-trace: attestation-by={non-null}, verification-by={non-null}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Typed Schema Table + Named ObligationBlock Phase

**axis:** output-format + lifecycle-emphasis (typed-column GateTokenSchema table from V-01 combined with named ObligationBlock construction phase from V-02)
**hypothesis:** V-01 and V-02 target orthogonal structural layers. V-01 targets the schema layer (C-42): the typed-column table makes field-type absence a visible formatting gap rather than a silently missing annotation. V-02 targets the obligation layer (C-43): the named ObligationBlock construction phase forces declaration-once and cross-reference-everywhere rather than repeated inline imperatives. The two axes share no state: the typed-column table is a schema declaration; the ObligationBlock is an imperative chain. They operate at different points in the prompt and produce different structural artifacts. The combination hypothesis: V-01 and V-02 should compound without interference. V-01's table forces type tokens for every GateTokenSchema field (C-42 pass), and V-02's named phase forces the addressable obligation block with cross-references (C-43 pass), and neither change should affect the other's target criterion. The primary interaction risk is prompt length — the ObligationBlock construction phase adds overhead before Expected Output, and the typed-column schema table adds overhead within the Expected Output declaration. Together they increase the pre-execution instruction surface. Prediction: C-42 and C-43 both improve over their single-axis baselines; C-44 holds at V-R15 baseline; no degradation on Groups A-E because the core structure is preserved.

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

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — ObligationBlock Construction [declare before any census or Expected work]**

Declare the complete obligation chain as a named, addressable block. This block will be cross-referenced by name from Sub-task A, Sub-task B, and S6.5. Do not restate these imperatives at those sites.

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution carries from S5.5-Sub-task-A unchanged through S6.5; no role may alter its value in transit
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A (section reference form) before emitting any gate token
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from the S5.5 value, emit amendment-finding before emitting the gate token; a deviated token without an amendment record violates this assertion
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding before emitting gate token
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5-Sub-task-A emits it; sole production site is S5.5
  Prohibit: silent-gate-close — gate may not close with null attestation-by or null verification-by; both audit-trace fields must be non-null at [TAXONOMY-CENSUS-COMPLETE]
```

`[OBLIGATION-BLOCK-SEALED]`

**Step 3 — GateTokenSchema (typed-column format)**

Declare the `GateTokenSchema` as a typed-column table. Every field row must have a non-empty type cell.

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                              | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; equals S5.5 source value     | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; references S5.5-Sub-A   | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens      | (none)              |
    | attestation-by      | string                  | non-empty role name                     | attestation-result  |
    | attestation-result  | string                  | non-empty claim value from census owner | attestation-by      |
    | verification-by     | string                  | non-empty role name (witness)           | verification-result |
    | verification-result | string                  | non-empty outcome from witness          | verification-by     |
  co-requirement: census-distribution and gate-provenance must both be present or both absent
  audit-trace-gate: all four audit-trace fields must be non-null before gate closes
    see: ObligationBlock: census-gate-obligations (Prohibit: silent-gate-close)
```

`[SCHEMA-SEALED]`

**Step 4 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, error path, edge case.

When all spec-defined elements are listed:

`[SEALED — Contract Expert exits. Expected Output, ObligationBlock, and GateTokenSchema above are locked. Automate begins below.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here.

**Step 5 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field the operation produces including all gate token fields.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When complete: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 6 — Schema Diff**

Run the schema diff against the sealed GateTokenSchema typed-column table. For each field row:
- `{field}: type {declared type} — actual value: {value} — CONFORMS` if value matches type constraint
- `{field}: type {declared type} — actual value: {value} — VIOLATES: {reason}` if value fails

A type violation is a finding (add to Step 7 findings). Set mechanism-type: `type-violation`.

**Step 7 — Findings**

Write a `## Findings` section.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause]
hypothesis: [mechanism sentence — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 8 — Sub-task A: Mechanism Distribution**

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site.

see: ObligationBlock: census-gate-obligations

**Step 9 — Sub-task B: Census Fill**

For each candidate group from Sub-task A:
```
staging: group={token}, members={F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from staging lines:
- 0: `mechanism-type-shared: none`
- 1 or 2+ same: `mechanism-type-shared: {token}`
- mixed: `mechanism-type-shared: mixed`

Rationale: {shared mechanism sentence}

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance)

**Step 10 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Fill every field from the sealed GateTokenSchema typed-column table.

```
gate-token:
  census-distribution: {value — carried forward from S5.5-Sub-task-A; must equal source value}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL}
  attestation-by: {census owner role name}
  attestation-result: {census owner claim — non-null}
  verification-by: {witness role name}
  verification-result: {witness outcome — non-null}
```

Schema conformance check — each field against GateTokenSchema typed-column table:
- census-distribution: type string — {CONFORMS | VIOLATES}
- gate-provenance: type format:S-section-ref — {CONFORMS | VIOLATES}
- gate-status: type enum[PASS|FAIL] — {CONFORMS | VIOLATES}
- attestation-by: type string, non-empty — {CONFORMS | VIOLATES}
- attestation-result: type string, non-empty — {CONFORMS | VIOLATES}
- verification-by: type string, non-empty — {CONFORMS | VIOLATES}
- verification-result: type string, non-empty — {CONFORMS | VIOLATES}

see: ObligationBlock: census-gate-obligations — all six imperatives apply at this site

Gate close verification: attestation-by non-null AND verification-by non-null → `[TAXONOMY-CENSUS-COMPLETE]`

**Step 11 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

mechanism-type-shared: {token}
gate-status: {PASS | FAIL}
schema-typed: {N/N fields carry type constraints}
ObligationBlock: census-gate-obligations — cross-referenced from Sub-task A, Sub-task B, S6.5

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combination: All Three R16 Advances as Co-Equal Contract Layers

**axis:** output-format + lifecycle-emphasis + role-sequence (typed GateTokenSchema table [C-42] + named ObligationBlock [C-43] + witness-first audit-trace [C-44] declared as three co-equal contract layers in a preamble before any execution begins)
**hypothesis:** V-01, V-02, and V-03 each target one of the three R16 advances through independent mechanisms. V-01 targets C-42 through output-format (typed-column table makes type absence visible). V-02 targets C-43 through lifecycle-emphasis (ObligationBlock construction phase forces name-before-reference). V-03 targets C-44 through role-sequence (witness-first makes it structurally impossible to close the gate with only one party's evidence). The combination hypothesis is not simply "all three together" but specifically that the three advances are most powerful when declared as co-equal contract layers in a preamble — before Sub-task A, before any execution, before the census even begins. The preamble declares: (1) the typed GateTokenSchema with field-type constraints, (2) the named ObligationBlock with its six imperatives and cross-reference anchor, and (3) the audit-trace protocol with its witness-first execution order and gate-close condition. Later phases reference these three pre-declared layers rather than constructing them inline. This front-loading means the contract is structurally complete before any execution work begins — the schema, the obligation chain, and the audit-trace protocol are established as facts, not built up incrementally. Prediction: C-42, C-43, and C-44 all improve over their single-axis baselines; the primary risk is that the preamble reads as overhead and operators begin Sub-task A before fully engaging with the preamble's content. This risk is mitigated by the `[CONTRACT-LAYER-PREAMBLE-SEALED]` token that marks the preamble as a non-optional foundation.

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

Before any census, expected-output, or gate work begins, declare three contract layers. These layers are the foundation. All later phases reference them by name and do not restate their content.

**Contract Layer 1 — Schema Layer [C-42: typed field constraints]**

```
GateTokenSchema: census-gate-token
  required-fields:
    | field               | type                    | constraint                              | co-required-with    |
    |---------------------|-------------------------|-----------------------------------------|---------------------|
    | census-distribution | string                  | non-empty; must equal S5.5 source value | gate-provenance     |
    | gate-provenance     | format: S-section-ref   | format §X.Y.Z; must reference S5.5-SubA | census-distribution |
    | gate-status         | enum[PASS|FAIL]         | exactly one value; no other tokens      | (none)              |
    | attestation-by      | string                  | non-empty role name; census owner       | attestation-result  |
    | attestation-result  | string                  | non-empty claim from census owner       | attestation-by      |
    | verification-by     | string                  | non-empty role name; witness            | verification-result |
    | verification-result | string                  | non-empty outcome from witness          | verification-by     |
  co-requirement: census-distribution and gate-provenance — both present or both absent; detectable by field-inspection without reading prose
  audit-trace-gate: attestation-by, attestation-result, verification-by, verification-result — all four non-null before gate boundary closes; detectable by value inspection without reading instruction trace
```

**Contract Layer 2 — Obligation Layer [C-43: named addressable ObligationBlock]**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — census-distribution value at S6.5 must equal value at S5.5; no role may alter it in transit between those sites
  Bind:     gate-provenance — value must be §S5.5-Sub-task-A in section-reference format; not a prose description, not an inferred reference
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates from S5.5 value, emit amendment-finding before emitting gate token; token may not be emitted with a silent deviation
  Assert:   amendment-path-provenance — if gate-provenance is absent or references a site other than S5.5-Sub-task-A, emit amendment-finding; token may not be emitted without correct provenance
  Prohibit: census-distribution-overwrite — no role may modify census-distribution after S5.5 emits it; S5.5 is the sole production site
  Prohibit: silent-gate-close — gate boundary (at [TAXONOMY-CENSUS-COMPLETE]) may not be reached unless attestation-by and verification-by are both non-null
```

**Contract Layer 3 — Audit Layer [C-44: witness-first two-party execution]**

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

`[CONTRACT-LAYER-PREAMBLE-SEALED — Schema Layer, Obligation Layer, and Audit Layer are now established. Sub-task A through S6.5 reference these layers by name. Do not restate their content at later sites.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, error path, edge case. For gate token elements, reference field names from GateTokenSchema: census-gate-token.

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

For each field in GateTokenSchema: census-gate-token typed-column table, verify actual value against declared type constraint:
- `{field}: type {declared type} — actual: {value} — CONFORMS | VIOLATES: {reason}`

Type violations become findings with mechanism-type: `type-violation`.

**Step 5 — Findings**

Write a `## Findings` section.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [missing-field | wrong-value | type-violation | schema-mismatch | obligation-gap | audit-trace-gap | other:{token}]
spec: [exact spec clause]
hypothesis: [mechanism sentence — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

**Step 6 — Sub-task A: Mechanism Distribution**

`mechanism-distribution: {F-01: token}, {F-02: token}, ...`

Sole production site.
see: ObligationBlock: census-gate-obligations (Contract Layer 2)

**Step 7 — Sub-task B: Census Fill**

For each candidate group from Sub-task A:
```
staging: group={token}, members={F-NN, ...}, count={N}
```

`mechanism-type-shared: {token | mixed | none}`
Rationale: {shared mechanism sentence — what it does to the contract}

see: ObligationBlock: census-gate-obligations — Assert: amendment-path-distribution (Contract Layer 2)

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
  census-distribution: {value — carried forward from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — from mechanism-type-shared at Sub-task B}
  attestation-by: {from Phase A — copy verbatim}
  attestation-result: {from Phase A — copy verbatim}
  verification-by: {from Phase W — copy verbatim}
  verification-result: {from Phase W — copy verbatim}
```

Schema conformance [Contract Layer 1 — GateTokenSchema typed-column check]:
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
schema-typed: {N/7 fields conform to typed-column constraints} [Contract Layer 1]
ObligationBlock: census-gate-obligations — cross-referenced at Sub-task A, Sub-task B, S6.5 [Contract Layer 2]
audit-trace: Phase W (verification-by={non-null}), Phase A (attestation-by={non-null}) [Contract Layer 3]

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
