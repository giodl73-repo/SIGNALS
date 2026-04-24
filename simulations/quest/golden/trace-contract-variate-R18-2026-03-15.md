# trace-contract Variate — Round 18

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v18 (C-08–C-50; Groups A–G; new criteria C-48/C-49/C-50)
**Round:** R18 — 3 new single-axis + 2 priority combinations targeting C-48, C-49, C-50

---

## Round 18 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (`[FINDINGS-COMPLETE count=N findings]` emitted at end of findings section as a count-bearing closure seal) | C-48 | R17 variations move directly from the last finding block to Sub-task A without emitting a findings-closure token; this makes findings completeness auditable only by re-counting blocks — a count-bearing seal at the findings boundary allows inspection to confirm N findings without re-entering the section, making off-by-one omission detectable at the token |
| V-02 | output-format (`AmendmentProtocol:` field added to MechanismTypeTaxonomy declaration, governing token extension before first use) | C-49 | R17 variations that carry `closed: true` and a `[TAXONOMY-DECLARED]` seal assert closure but do not state the amendment procedure — an operator who needs a new token has no named governance path; an `AmendmentProtocol:` field converts the closure assertion into an enforceable contract whose violation is detectable by comparing declared tokens against tokens in use |
| V-03 | lifecycle-emphasis (Schema Diff phase carries a named `OmissionRule:` declaring absent GateTokenSchema rows as automatic SCHEMA-PHASE-FAIL independent of element diff) | C-50 | R17 variations satisfy C-19 through a general no-silent-omissions instruction that does not differentiate schema-level omission from element-diff omission; a named `OmissionRule:` in the Schema Diff phase makes schema completeness a detectable failure mode by row-count comparison alone, without requiring the inspector to read sweep output |
| V-04 | output-format combination (count-bearing findings closure from V-01 + AmendmentProtocol taxonomy governance from V-02) | C-48, C-49 | The findings-closure axis (C-48) and the taxonomy-governance axis (C-49) operate at orthogonal structural layers — findings section and taxonomy declaration — with no shared state; combining them targets both without axis interference and tests whether the two sealing patterns reinforce each other's auditing properties |
| V-05 | output-format + lifecycle-emphasis (all three R18 advances declared as co-equal contract-governance layers in a preamble before any execution begins: count-bearing findings seal, amendment-protocol taxonomy, schema-omission rule) | C-48, C-49, C-50 | Declaring `[FINDINGS-COMPLETE count=N findings]` (C-48), `AmendmentProtocol:` governance (C-49), and `OmissionRule: SCHEMA-PHASE-FAIL` (C-50) as a three-layer contract-governance preamble before Sub-task A forces all three to be structurally present and cross-referenced before any census or gate work begins; later phases reference pre-declared governance layers by name rather than constructing them inline |

---

## V-01 — Output Format: Count-Bearing Findings Closure Seal

**axis:** output-format — `[FINDINGS-COMPLETE count=N findings]` emitted at the end of the findings section as a count-bearing closure seal before Sub-task A begins
**hypothesis:** C-25 requires a `[FINDINGS-COMPLETE]` token at the end of the findings section. C-48 escalates: the token must carry a count assertion — `[FINDINGS-COMPLETE count=N findings]` — so that findings completeness is self-verifying. In all R17 variations, the last finding block is immediately followed by Sub-task A with no closure token; even the best variations (V-02, V-04, V-05) that demonstrate structural sealing elsewhere (`[TAXONOMY-DECLARED]`, `SCHEMA-DIFF-COMPLETE`) do not apply the pattern to findings closure. Without a count-bearing token, confirming that N findings were recorded requires re-counting every block; an off-by-one omission produces a structurally valid document with no detectable closure gap. Adding `[FINDINGS-COMPLETE count=N findings]` forces the operator to assert the count at the boundary; a miscount is detectable at the token without re-entering the finding blocks. Prediction: C-48 pass rate improves over V-R17 baseline because the count assertion creates a verifiable boundary; C-25 holds because the token satisfies the format criterion and extends it; C-45 and C-46 hold at baseline because this variation does not change the schema-diff or taxonomy instructions.

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

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary:

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
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy is now the authoritative vocabulary for this trace. No mechanism-type value may be used that is not listed above. Amend the tokens list before first use of any new token.]`

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
```

`[SCHEMA-SEALED]`

**Step 4 — ObligationBlock Construction**

Declare the complete obligation chain as a named, addressable block before any Expected Output entries:

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

Before the element-level diff, run the schema diff. Compare actual gate token fields against every row in the GateTokenSchema typed-column table.

For each row in GateTokenSchema:
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field` if field absent

A type violation or absent field produces a finding (severity: `breaking` if consumer would infer wrong behavior; `degraded` otherwise).

`[SCHEMA-DIFF-COMPLETE — schema sweep finished. Element diff may now begin.]`

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

Sole production site: this line appears exactly once, here. Do not derive mechanism tokens from the narrative — copy from the `mechanism-type:` field in each finding block.

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
  verification-by: {witness role name — non-null required}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null. Verify before writing the completion token.

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
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: AmendmentProtocol Governance Field in Taxonomy Declaration

**axis:** output-format — `MechanismTypeTaxonomy` block carries a named `AmendmentProtocol:` field specifying that new tokens require taxonomy-block amendment before first use; the `[TAXONOMY-DECLARED]` seal is conditioned on the AmendmentProtocol being named
**hypothesis:** C-46 requires the mechanism-type taxonomy to be declared inline as a closed enumerated set with a `[TAXONOMY-DECLARED]` seal. C-49 escalates: the taxonomy declaration must carry a named `AmendmentProtocol:` field so that the `closed: true` assertion becomes an enforceable governance contract. In R17, V-02 introduces an amendment protocol alongside `closed: true`, but V-04 and V-05 carry `closed: true` and `[TAXONOMY-DECLARED]` without a named protocol — closure is asserted but the extension procedure is undocumented. An operator needing a new token must either violate the closed constraint (silent addition) or infer a procedure that is not in the declared block. The `AmendmentProtocol:` field names the exact amendment procedure, converting the closed flag from an honor-system assertion into a structural governance contract: a token not in the declared set is detectable by comparison, and the protocol for adding it is auditable from the declaration without consulting external documentation. Prediction: C-49 pass rate improves over V-R17 baseline; C-46 holds because the taxonomy is still a closed enumeration; C-48 and C-50 hold at baseline because this variation does not change the findings-closure or schema-omission instructions.

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

**Step 2 — MechanismTypeTaxonomy Declaration with AmendmentProtocol**

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment the taxonomy version, and re-seal before writing any finding block that uses the new token
  TaxonomyVersion: 1.0
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy v1.0 is now the authoritative vocabulary for this trace. Compliance rule: any mechanism-type value not present in the declared tokens list constitutes a taxonomy violation detectable by comparison. AmendmentProtocol governs all extensions.]`

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

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, and MechanismTypeTaxonomy (AmendmentProtocol applies) above are locked. Automate begins below. No modification permitted after this line.]`

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

Before the element-level diff, run the schema diff. Compare actual gate token fields against every row in the GateTokenSchema typed-column table.

For each row in GateTokenSchema:
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field` if field absent

A type violation or absent field produces a finding (severity: `breaking` if consumer would infer wrong behavior; `degraded` otherwise).

`[SCHEMA-DIFF-COMPLETE — schema sweep finished. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED]; AmendmentProtocol applies before use of any new token]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared:

`[FINDINGS-COMPLETE]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy tokens list — see [TAXONOMY-DECLARED].

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
  verification-by: {witness role name — non-null required}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null. Verify before writing the completion token.

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

MechanismTypeTaxonomy: v1.0 — {N tokens declared} tokens; AmendmentProtocol applied: {yes | no}
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: Named OmissionRule in Schema Diff Phase

**axis:** lifecycle-emphasis — the Schema Diff phase carries a named `OmissionRule:` field stating that any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result
**hypothesis:** C-45 requires the Schema Diff phase to emit `SCHEMA-DIFF-COMPLETE` before the element diff begins. C-50 escalates: the Schema Diff phase must carry a named `OmissionRule:` so that schema completeness is governed by a structural failure criterion rather than a prose completeness admonition. In R17, all variations satisfy C-19 through a general "no silent omissions" instruction — but this instruction does not differentiate a schema-level omission (missing GateTokenSchema row in the sweep) from an element-diff omission (missing Expected entry in the comparison). Without a named omission rule, confirming schema sweep completeness requires reading the sweep output to count rows. An `OmissionRule:` in the Schema Diff phase makes completeness a binary test: count declared GateTokenSchema rows vs. sweep output rows; any mismatch triggers SCHEMA-PHASE-FAIL without inspecting row content. The failure mode is detectable by row-count comparison alone and is named, so it can be cited by finding blocks as a structural criterion. Prediction: C-50 pass rate improves over V-R17 baseline; C-45 holds because SCHEMA-DIFF-COMPLETE is still emitted; C-48 and C-49 hold at baseline because this variation does not change the findings-closure or taxonomy instructions.

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

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary:

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
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy is now the authoritative vocabulary for this trace. No mechanism-type value may be used that is not listed above.]`

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness is verified by row-count comparison: declared rows = sweep output rows; any shortfall triggers SCHEMA-PHASE-FAIL before element diff begins
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

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema (OmissionRule declared), ObligationBlock, and MechanismTypeTaxonomy above are locked. Automate begins below. No modification permitted after this line.]`

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

When all Expected entries have been compared:

`[FINDINGS-COMPLETE]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here.

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
  verification-by: {witness role name — non-null required}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null. Verify before writing the completion token.

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

schema-phase: {PASS | SCHEMA-PHASE-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
OmissionRule: {satisfied | violated — {N} rows absent from sweep}
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combination: Count-Bearing Findings Seal + AmendmentProtocol Taxonomy Governance

**axis:** output-format combination — `[FINDINGS-COMPLETE count=N findings]` count-bearing closure seal (V-01 axis) + `AmendmentProtocol:` field in MechanismTypeTaxonomy declaration (V-02 axis)
**hypothesis:** The findings-closure axis (C-48) operates at the boundary of the findings section — a count assertion makes the section self-verifying by inspection. The taxonomy-governance axis (C-49) operates at the MechanismTypeTaxonomy declaration — a named AmendmentProtocol converts `closed: true` from an assertion into an enforceable governance contract. These two axes operate at orthogonal structural layers (findings section vs. taxonomy declaration) with no shared state. V-04 tests whether combining them produces the predicted pass on both C-48 and C-49 without axis interference, and whether the count-bearing seal and the amendment protocol reinforce each other's auditing properties — the seal makes findings completeness verifiable at the token; the protocol makes taxonomy compliance verifiable at the declaration. Prediction: both C-48 and C-49 pass; C-45, C-46, C-47 hold at baseline; C-50 holds at baseline because this variation does not change the schema-omission instructions.

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

**Step 2 — MechanismTypeTaxonomy Declaration with AmendmentProtocol**

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment TaxonomyVersion, and re-seal before writing any finding block that uses the new token
  TaxonomyVersion: 1.0
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy v1.0 is the authoritative vocabulary for this trace. Compliance rule: any mechanism-type value not in the declared tokens list is detectable by comparison. AmendmentProtocol governs all extensions.]`

**Step 3 — GateTokenSchema (typed-column declaration)**

Declare the `GateTokenSchema` using the typed-column table format. Derive from the spec — do not run the operation.

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

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, and MechanismTypeTaxonomy (AmendmentProtocol v1.0) above are locked. Automate begins below. No modification permitted after this line.]`

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

Before the element-level diff, run the schema diff. Compare actual gate token fields against every row in the GateTokenSchema typed-column table.

For each row in GateTokenSchema:
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field` if field absent

A type violation or absent field produces a finding.

`[SCHEMA-DIFF-COMPLETE — schema sweep finished. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy v1.0 — see [TAXONOMY-DECLARED]; AmendmentProtocol applies before use of any new token]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. Completeness is verifiable by counting F-01 through F-N without re-entering finding content.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy v1.0 — see [TAXONOMY-DECLARED]; AmendmentProtocol applies if a new token is needed.

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
  verification-by: {witness role name — non-null required}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply at this site

Gate close condition: `attestation-by` and `verification-by` are both non-null. Verify before writing the completion token.

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
MechanismTypeTaxonomy: v1.0 — {N tokens declared}; AmendmentProtocol applied: {yes | no}
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Full Combination: All Three R18 Governance Layers as Contract Preamble

**axis:** output-format + lifecycle-emphasis — all three R18 advances declared as co-equal contract-governance layers in a named preamble before any execution begins: count-bearing findings seal (`[FINDINGS-COMPLETE count=N findings]`), amendment-protocol taxonomy governance (`AmendmentProtocol:`), and schema-omission rule (`OmissionRule: SCHEMA-PHASE-FAIL`)
**hypothesis:** V-01 through V-03 demonstrate that each C-48, C-49, C-50 advance is independently achievable. V-05 tests whether declaring all three as a named contract-governance preamble — `ContractGovernancePreamble` — before Sub-task A produces a document in which all three governance layers are (1) structurally present before any census or gate work begins, (2) cross-referenced by name from the phases that use them, and (3) auditable from the preamble alone without reading phase content. The preamble declares: the MechanismTypeTaxonomy with AmendmentProtocol (C-49), the GateTokenSchema with OmissionRule (C-50), the ObligationBlock (C-47), and the findings-closure protocol (C-48). Each phase that depends on a governance layer cites it by preamble reference rather than restating the rule. Prediction: C-48, C-49, and C-50 all pass; C-42 through C-47 hold at baseline because the preamble encompasses all prior structural advances; the three new governance layers reinforce each other's auditing properties — findings count verifiable at seal, taxonomy compliance verifiable at declaration, schema completeness verifiable by row count.

---

You are running /trace:contract for Signal.

**Topic:** {topic}
**Operation under test:** {operation — e.g., PATCH /section-items/{id}/census-gate}
**Connector / Automate context:** {connector name or Automate flow and environment}
**Input fixture:** {input state — inline, not a file reference}
**Spec source:** {spec file path and section}

Stock roles: Connectors contract expert + Automate.

---

### ROLE: Connectors Contract Expert — Contract Governance Preamble

Before any Expected Output entries or execution steps, declare the three co-equal contract-governance layers. These layers are pre-declared, named, and cross-referenced by all subsequent phases. No phase may restate a governance rule that is declared here — cite by reference only.

**Preamble Layer 1 — MechanismTypeTaxonomy with AmendmentProtocol**

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add token to tokens list, increment TaxonomyVersion, re-seal before writing any finding block that uses the new token
  TaxonomyVersion: 1.0
```

`[TAXONOMY-DECLARED — MechanismTypeTaxonomy v1.0 governs all mechanism-type values in this trace. AmendmentProtocol governs all extensions. Violation detectable by comparing declared tokens against tokens in use.]`

**Preamble Layer 2 — GateTokenSchema with OmissionRule**

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness verified by row-count: declared rows ({N}) must equal sweep output rows; any shortfall is SCHEMA-PHASE-FAIL
```

`[SCHEMA-SEALED — GateTokenSchema governs the gate token structure and Schema Diff phase. OmissionRule governs schema completeness. Row count is the compliance test.]`

**Preamble Layer 3 — ObligationBlock with Findings-Closure Protocol**

```
ObligationBlock: census-gate-obligations
  Bind:     copy-forward — carry census-distribution from S5.5-Sub-task-A through S6.5 unchanged
  Bind:     gate-provenance — assign gate-provenance = §S5.5-Sub-task-A by section identifier
  Assert:   amendment-path-distribution — if census-distribution at S6.5 deviates, emit amendment-finding before gate token
  Assert:   amendment-path-provenance — if gate-provenance absent or wrong source, emit amendment-finding before gate token
  Prohibit: census-distribution-overwrite — no role modifies census-distribution after S5.5 emits it
  Prohibit: silent-gate-close — gate boundary may not close with null attestation-by or null verification-by
  Prohibit: re-derive-mechanism — mechanism-type-shared at fill site must equal staging-line value; do not re-derive from findings

FindingsClosureProtocol:
  seal: [FINDINGS-COMPLETE count=N findings]
  rule: the seal must be written immediately after the last finding block, before Sub-task A begins
  compliance: an inspector verifies findings completeness by confirming N finding blocks exist without re-entering finding content; an off-by-one omission is detectable at the seal without re-scanning the section
```

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations and FindingsClosureProtocol are the authoritative obligation and closure sources. All phases cite by reference. No imperative or closure rule may be restated at a downstream site.]`

`[CONTRACT-GOVERNANCE-PREAMBLE-COMPLETE — three governance layers declared: MechanismTypeTaxonomy v1.0 (AmendmentProtocol), GateTokenSchema (OmissionRule), ObligationBlock + FindingsClosureProtocol. Pre-run phase may begin.]`

---

### ROLE: Connectors Contract Expert — Pre-Run Phase [20-EXPECTED]

**Step 1 — Contract Scope**

Write a `## Contract Scope` section. State: operation and method, connector or Automate context and environment, input fixture (inline, self-contained), spec version and section governing the output contract.

**Step 2 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries (see Preamble Layer 2).

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. Expected Output locked. Contract Governance Preamble (all three layers) governs this trace. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or the Contract Governance Preamble above.

**Step 3 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 4 — Schema Diff Phase**

Apply OmissionRule (Preamble Layer 2 — GateTokenSchema). Before element diff: count declared GateTokenSchema rows ({N} rows). Count sweep output rows. If sweep output rows < N: `SCHEMA-PHASE-FAIL` — record absent rows; do not begin element diff until resolved.

For each row in GateTokenSchema (sweep every row — OmissionRule applies):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason}` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field (OmissionRule: SCHEMA-PHASE-FAIL)` if field absent

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} rows swept; OmissionRule: {satisfied | SCHEMA-PHASE-FAIL}. Element diff may begin.]`

**Step 5 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token from MechanismTypeTaxonomy v1.0 — Preamble Layer 1; AmendmentProtocol applies before new token use]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible for wrong output]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — FindingsClosureProtocol (Preamble Layer 3): N finding blocks appear above. Completeness verifiable by counting F-01 through F-N without re-entering content. Off-by-one detectable here.]`

**Step 6 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must be in MechanismTypeTaxonomy v1.0 (Preamble Layer 1 — AmendmentProtocol applies if a new token is needed).

see: ObligationBlock: census-gate-obligations — Bind: copy-forward, Prohibit: census-distribution-overwrite (Preamble Layer 3)

**Step 7 — Sub-task B: Staging Lines and Pattern Fill**

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

see: ObligationBlock: census-gate-obligations — Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism (Preamble Layer 3)

**Step 8 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token using every required-field row from the sealed GateTokenSchema (Preamble Layer 2):

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL — derived from mechanism-type-shared at Sub-task B}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required}
  verification-result: {independent verification outcome — non-null required}
```

see: ObligationBlock: census-gate-obligations — all seven imperatives apply (Preamble Layer 3)

Gate close condition: `attestation-by` and `verification-by` both non-null. Verify before writing completion token.

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 9 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

Contract Governance Preamble compliance:
  Layer 1 — MechanismTypeTaxonomy v1.0: {N tokens declared}; AmendmentProtocol applied: {yes | no}
  Layer 2 — GateTokenSchema OmissionRule: {satisfied | SCHEMA-PHASE-FAIL} — {N swept} / {N declared} rows
  Layer 3 — FindingsClosureProtocol: [FINDINGS-COMPLETE count=N findings]

mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
