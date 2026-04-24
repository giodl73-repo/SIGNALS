# trace-contract Variate — Round 20

**Date:** 2026-03-15
**Skill:** trace-contract
**Rubric:** v20 (C-08–C-56; Groups A–G; new criteria C-54/C-55/C-56)
**Round:** R20 — 3 new single-axis + 2 priority combinations targeting C-54, C-55, C-56

---

## Round 20 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | output-format (`VerbatimRule:` constraint block declared in preamble, governing `findings-sealed:` echo as character-for-character copy) | C-54 | R19 V-01 passes C-51 by emitting `findings-sealed: [FINDINGS-COMPLETE count=N findings]` in the Summary AND attaching a verbatim-copy enforcement sentence; C-51 requires only the named echo field — the enforcement sentence is natural-language prose whose violation requires semantic interpretation; a named `VerbatimRule:` block with explicit string-comparison verification makes reformulation detectable as a structural violation by comparison alone without semantic judgment |
| V-02 | output-format (`taxonomy-version:` named field in Summary section echoing `[TAXONOMY-DECLARED version=N]` seal, parallel to `findings-sealed:`) | C-55 | R19 V-02 passes C-52 by encoding `[TAXONOMY-DECLARED version=N]` on the seal; the Summary section carries `schema-phase:` and `mechanism-type-shared:` but no field that echoes the taxonomy seal — confirming taxonomy version from the summary requires locating the seal in the instruction body; a `taxonomy-version:` field that mirrors the versioned seal exactly makes version-skew detectable from the summary anchor without cross-referencing the taxonomy block |
| V-03 | lifecycle-emphasis (Schema Diff Phase `FailureToken:` block upgraded with a named `remediation:` field per entry, making remediation path machine-derivable from the emitted token alone) | C-56 | R19 V-03 passes C-53 by declaring `SCHEMA-PHASE-FAIL` and `SCHEMA-OMISSION-FAIL` as distinct tokens with distinct remediation paths stated in prose within the block; C-53 requires nominal token distinction; the remediation paths are readable from the block text but are not addressable by field name — an automated inspector must parse prose to determine the required response; a named `remediation:` field per token entry makes the required action derivable by field lookup alone and prevents a shared remediation path from collapsing the two failure modes |
| V-04 | output-format combination (`VerbatimRule:` preamble block from V-01 + `taxonomy-version:` summary echo from V-02) | C-54, C-55 | The verbatim-copy enforcement axis (C-54) and the taxonomy-version echo axis (C-55) both operate on the Summary section as a self-contained audit anchor; combining them tests whether a Summary carrying both `findings-sealed:` (governed by `VerbatimRule:`) and `taxonomy-version:` (echoing the versioned seal) constitutes a single structural anchor point from which both findings completeness and taxonomy version are auditable without entering the instruction body |
| V-05 | output-format + lifecycle-emphasis (all three R20 advances declared as named governance layers in a `GovernancePreamble:` block before execution begins, cross-referenced by name from every phase that emits or consumes a governed value) | C-54, C-55, C-56 | Declaring `VerbatimRule:` (C-54), `TaxonomyEchoRule:` (C-55), and `RemediationContract:` (C-56) as co-equal named governance layers in a preamble forces all three to be structurally committed before census or gate work starts; later phases reference pre-declared governance layers by name rather than re-stating constraints inline, making the governance layer self-contained and verifiable as a unit — a reader auditing governance completeness needs only the preamble block |

---

## V-01 — Output Format: VerbatimRule Block Governing findings-sealed Echo

**axis:** output-format — A named `VerbatimRule:` block is declared in the preamble before execution begins, specifying that `findings-sealed:` in the Summary MUST be copied character-for-character from the `[FINDINGS-COMPLETE count=N findings]` token; reformulation or count adjustment constitutes a summary-integrity violation detectable by string comparison alone

**hypothesis:** R19 V-01 passes C-51 by emitting `findings-sealed: [FINDINGS-COMPLETE count=N findings]` in the Summary and appending a natural-language enforcement sentence. C-54 escalates: the enforcement prose can be paraphrased or ignored without producing a structurally detectable violation — only semantic reading reveals the intent. A `VerbatimRule:` block with a named `verification:` field (`string-compare findings-sealed value against [FINDINGS-COMPLETE] token; any character difference is a violation`) converts the copy obligation from an interpretive norm into a string-comparison contract: any deviation — bracket omission, count adjustment, word substitution — is a structural violation whose presence is detectable by comparison without judgment. Prediction: C-54 pass rate improves over R19 V-01 baseline; C-51 holds because `findings-sealed:` echo is still emitted; C-48 holds because `[FINDINGS-COMPLETE count=N findings]` boundary token is still emitted; C-55 and C-56 remain at R19 baseline — this variation does not modify the taxonomy-version summary field or the FailureToken remediation fields.

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

**Step 2 — Governance Preamble: VerbatimRule**

Before declaring the taxonomy or schema, declare the verbatim-copy rule that governs the `findings-sealed:` echo field. This rule is declared once here and cross-referenced in Step 12; it is not restated inline.

```
VerbatimRule: findings-sealed-echo
  target-field: findings-sealed (Summary section, Step 12)
  source-token: [FINDINGS-COMPLETE count=N findings] (emitted at end of Step 8)
  copy-rule: the findings-sealed field value MUST be copied character-for-character from
             the [FINDINGS-COMPLETE count=N findings] token; the copy includes the bracket
             delimiters, the "count=" prefix, the integer N, the space, and the word
             "findings" exactly as they appear in the emitted token
  violation: any reformulation, paraphrase, count adjustment, or bracket omission
             constitutes a summary-integrity violation; the violation is detectable by
             string comparison alone without semantic interpretation
  verification: string-compare findings-sealed field value against the [FINDINGS-COMPLETE]
                token character-for-character; any character difference is a violation,
                not a rendering variant
```

`[VERBATIM-RULE-DECLARED — findings-sealed-echo is the authoritative copy constraint for this trace. Step 12 references this rule by name; the rule text is not restated at Step 12.]`

**Step 3 — MechanismTypeTaxonomy Declaration**

Declare the closed mechanism-type vocabulary with amendment governance and version counter:

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the
    token to the tokens list, increment AmendmentVersion by 1, and re-seal as
    [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token;
    a taxonomy block copied forward into a new trace must reset AmendmentVersion to 0 unless
    amendments carry over
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. Version=0 means no amendments have been applied. A seal carrying version=N and a block carrying AmendmentVersion=M where N != M is a version-skew violation. AmendmentProtocol governs all extensions.]`

**Step 4 — GateTokenSchema (typed-column declaration)**

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an
    automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness
    is verified by row-count comparison: declared rows = sweep output rows
  FailureToken:
    SCHEMA-PHASE-FAIL:
      trigger: type-constraint violated for any GateTokenSchema field
    SCHEMA-OMISSION-FAIL:
      trigger: row absent from schema-sweep output (OmissionRule violation)
```

`[SCHEMA-SEALED]`

**Step 5 — ObligationBlock Construction**

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

**Step 6 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

When all spec-defined elements are listed:

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, MechanismTypeTaxonomy (version=0), and VerbatimRule findings-sealed-echo above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 7 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 8 — Schema Diff Phase**

Before the element-level diff, run the schema diff. Apply the OmissionRule declared in GateTokenSchema.

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. If sweep output rows < declared rows: SCHEMA-OMISSION-FAIL — record which row(s) are absent and halt element diff until the gap is resolved. If a row is present but its value violates the declared type constraint: SCHEMA-PHASE-FAIL.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES [{reason}] → SCHEMA-PHASE-FAIL` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field → SCHEMA-OMISSION-FAIL` if field absent

Schema sweep row count: {N swept} / {N declared}. If N swept < N declared: write `SCHEMA-OMISSION-FAIL` before proceeding.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; OmissionRule satisfied. Element diff may now begin.]`

**Step 9 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0];
                 if a new token is needed, apply AmendmentProtocol before writing this block]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. An inspector may verify completeness by counting F-01 through F-N without re-entering finding content.]`

**Step 10 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

Sole production site: this line appears exactly once, here. All tokens must appear in MechanismTypeTaxonomy at the current version — verify against the most recent `[TAXONOMY-DECLARED version=N]` seal.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 11 — Sub-task B: Staging Lines and Pattern Fill**

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

Rationale: `{sentence naming the shared mechanism}`

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 12 — Gate Token: S6.5**

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

**Step 13 — Summary**

```
## Summary

| Severity | Count |
|----------|-------|
| breaking |   N   |
| degraded |   N   |
| cosmetic |   N   |
| total    |   N   |

findings-sealed: [FINDINGS-COMPLETE count=N findings]
schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

`findings-sealed:` — see: VerbatimRule: findings-sealed-echo (declared in Step 2). The value of `findings-sealed:` MUST be copied character-for-character from the `[FINDINGS-COMPLETE count=N findings]` token emitted at the end of Step 9. Verification: string-compare character-for-character; any difference is a structural violation. Do not paraphrase, adjust the count, or omit brackets.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-02 — Output Format: taxonomy-version: Summary Echo Field

**axis:** output-format — The Summary section carries a named `taxonomy-version:` field that echoes the `[TAXONOMY-DECLARED version=N]` seal verbatim, parallel to `findings-sealed:`, making taxonomy version auditable from the summary anchor without locating the taxonomy block in the instruction body

**hypothesis:** R19 V-02 passes C-52 by encoding `[TAXONOMY-DECLARED version=N]` on the seal; the Summary section carries `schema-phase:`, `mechanism-type-shared:`, and `gate-status:` — but no field that echoes the taxonomy version. Confirming the taxonomy version in use from the summary requires scrolling to the Step 3 taxonomy block and locating the seal. C-55 escalates: a named `taxonomy-version:` field that mirrors `[TAXONOMY-DECLARED version=N]` exactly in the Summary section makes version-skew auditable at the summary anchor — a summary-level inspector can confirm both findings completeness (`findings-sealed:`) and taxonomy version (`taxonomy-version:`) from the same structural anchor point. Prediction: C-55 pass rate improves over R19 V-02 baseline; C-52 holds because the versioned seal is still emitted in the taxonomy block; C-51 holds because `findings-sealed:` echo is still in the Summary; C-54 and C-56 remain at R19 baseline.

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

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary with amendment governance and a version counter. The version counter on the seal governs the `taxonomy-version:` echo field in the Summary (Step 13).

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the
    token to the tokens list, increment AmendmentVersion by 1, and re-seal as
    [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token;
    a taxonomy block copied forward into a new trace must reset AmendmentVersion to 0 unless
    amendments carry over
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. Version=0 means no amendments have been applied. A seal carrying version=N and a block carrying AmendmentVersion=M where N != M is a version-skew violation detectable by counter comparison. The Summary section's taxonomy-version: field echoes this seal; version-skew between the seal and that echo field constitutes a summary-integrity violation. AmendmentProtocol governs all extensions.]`

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an
    automatic SCHEMA-PHASE-FAIL independent of the element diff result
  FailureToken:
    SCHEMA-PHASE-FAIL:
      trigger: type-constraint violated for any GateTokenSchema field
    SCHEMA-OMISSION-FAIL:
      trigger: row absent from schema-sweep output (OmissionRule violation)
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

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below. If sweep output rows < declared rows: SCHEMA-OMISSION-FAIL. If a row is present but violates its declared type constraint: SCHEMA-PHASE-FAIL.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason} → SCHEMA-PHASE-FAIL` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field → SCHEMA-OMISSION-FAIL` if field absent

Schema sweep row count: {N swept} / {N declared}. If N swept < N declared: write `SCHEMA-OMISSION-FAIL` before proceeding.

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
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0];
                 if a new token is needed, apply AmendmentProtocol before writing this block]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

If any finding requires a new mechanism-type token: pause, apply AmendmentProtocol (add token, increment AmendmentVersion, re-seal as `[TAXONOMY-DECLARED version=N+1]`), then write the finding block.

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

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings.

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

Gate close condition: `attestation-by` and `verification-by` are both non-null AND name distinct roles.

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
schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

The `findings-sealed:` field value MUST be copied verbatim from the `[FINDINGS-COMPLETE count=N findings]` token emitted in Step 8.

The `taxonomy-version:` field value MUST copy the `[TAXONOMY-DECLARED version=N]` seal verbatim from Step 2 (or the most recent re-seal if amendments were applied during Step 8). The version counter in `taxonomy-version:` and the `AmendmentVersion:` field in the taxonomy block MUST agree; any discrepancy is a version-skew violation that MUST be raised as a finding before the summary is written.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-03 — Lifecycle Emphasis: remediation: Field per FailureToken Entry

**axis:** lifecycle-emphasis — Each entry in the `FailureToken:` block declared in the GateTokenSchema carries a named `remediation:` field specifying the required corrective action, making the remediation path machine-derivable from the emitted token alone without reading the failure rationale text

**hypothesis:** R19 V-03 passes C-53 by declaring `SCHEMA-PHASE-FAIL` and `SCHEMA-OMISSION-FAIL` as distinct tokens with distinct remediation described in prose within the FailureToken block. C-56 escalates: the remediation text is readable but not field-addressable — an automated inspector parsing `SCHEMA-PHASE-FAIL` must read the surrounding prose to determine the required corrective action; there is no named slot to query. A named `remediation:` field per token entry makes the required action available by field name: `FailureToken[SCHEMA-PHASE-FAIL].remediation` = `correct field type and re-sweep the schema from the top`. The two tokens cannot share a remediation path by structural construction: `SCHEMA-PHASE-FAIL.remediation` specifies type correction; `SCHEMA-OMISSION-FAIL.remediation` specifies row addition. Collapsing them back into a single remediation is detectable as a structural violation. Prediction: C-56 pass rate improves over R19 V-03 baseline; C-53 holds because both tokens remain nominally distinct; C-50 holds because `OmissionRule:` still names `SCHEMA-PHASE-FAIL`; C-54 and C-55 remain at R19 baseline.

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

Before writing any Expected Output entries, declare the closed mechanism-type vocabulary with amendment governance and version counter:

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the
    token to the tokens list, increment AmendmentVersion by 1, and re-seal as
    [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. Version=0 means no amendments have been applied. AmendmentProtocol governs all extensions.]`

**Step 3 — GateTokenSchema with FailureToken Remediation Contract**

Declare the `GateTokenSchema` using the typed-column table format. Each `FailureToken:` entry carries a named `remediation:` field specifying the required corrective action. The `remediation:` field makes the required response machine-derivable from the token alone without reading failure rationale text; a shared `remediation:` path across both tokens constitutes a structural violation.

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an
    automatic SCHEMA-PHASE-FAIL independent of the element diff result
  FailureToken:
    SCHEMA-PHASE-FAIL:
      trigger: type-constraint violated for any GateTokenSchema field during schema sweep
      remediation: correct field type to match declared constraint and re-sweep the schema from the top; do not proceed to element diff until SCHEMA-DIFF-COMPLETE is re-emitted
    SCHEMA-OMISSION-FAIL:
      trigger: row absent from schema-sweep output (OmissionRule violation)
      remediation: add absent row to actual output and re-sweep the schema from the top; do not proceed to element diff until SCHEMA-DIFF-COMPLETE is re-emitted
```

`[SCHEMA-SEALED — FailureToken remediation paths are declared. SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL have distinct remediation: fields; a shared remediation path across both tokens constitutes a structural violation of the FailureToken contract.]`

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

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema (including FailureToken remediation contract), ObligationBlock, and MechanismTypeTaxonomy above are locked. Automate begins below. No modification permitted after this line.]`

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

Before the element-level diff, run the schema diff. Apply the OmissionRule and FailureToken remediation contract declared in GateTokenSchema.

OmissionRule check: count declared GateTokenSchema rows ({N} rows). Count sweep output rows below.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason} → SCHEMA-PHASE-FAIL` if value fails type constraint
  - remediation: correct field type to match declared constraint and re-sweep from the top (see FailureToken: SCHEMA-PHASE-FAIL.remediation)
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field → SCHEMA-OMISSION-FAIL` if field absent
  - remediation: add absent row to actual output and re-sweep from the top (see FailureToken: SCHEMA-OMISSION-FAIL.remediation)

Schema sweep row count: {N swept} / {N declared}. Emit the appropriate FailureToken if violations exist.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; FailureToken remediation contract satisfied. Element diff may now begin.]`

**Step 8 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0]]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token.]`

**Step 9 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 10 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token from Sub-task A. For each candidate group:

```
staging: group={mechanism-type-token}, members={F-NN, F-NN, ...}, count={N}
```

Derive `mechanism-type-shared` from the staging lines — do not re-derive from findings.

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 11 — Gate Token: S6.5**

Write a `## S6.5: Gate Token` section. Emit the complete gate token:

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
schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

The `findings-sealed:` field value MUST be copied verbatim from the `[FINDINGS-COMPLETE count=N findings]` token emitted in Step 8.

If `schema-phase:` carries `SCHEMA-PHASE-FAIL` or `SCHEMA-OMISSION-FAIL`, the corresponding `remediation:` field from the GateTokenSchema `FailureToken:` block governs the required corrective action before the trace can be considered closed.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-04 — Combined: VerbatimRule Block + taxonomy-version: Summary Echo

**axis:** output-format combination — `VerbatimRule:` constraint block from V-01 + `taxonomy-version:` summary echo from V-02; both governance layers declared in the preamble and both echo fields present in the Summary, making the Summary a self-contained dual-anchor point for findings completeness and taxonomy version

**hypothesis:** C-54 (VerbatimRule governing findings-sealed) and C-55 (taxonomy-version: echoing the versioned seal) both operate on the Summary section as an audit anchor. V-01 and V-02 demonstrate each in isolation. Combining them tests whether a Summary carrying `findings-sealed:` (governed by `VerbatimRule: findings-sealed-echo`) and `taxonomy-version:` (echoing `[TAXONOMY-DECLARED version=N]`) constitutes a structurally complete audit anchor: a reader who reads only the Summary can confirm (a) findings count by string comparison against the VerbatimRule target, and (b) taxonomy version by echo comparison against the versioned seal. Neither field cross-references the other; they are orthogonal governance commitments on orthogonal dimensions. Prediction: C-54 and C-55 both pass; C-56 remains at R19 baseline — the FailureToken block is not modified in this combination.

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

**Step 2 — Governance Preamble: VerbatimRule + TaxonomyEcho**

Before declaring the taxonomy or schema, declare both governance rules that govern Summary section echo fields. These rules are declared once here and cross-referenced in Step 13; neither is restated inline.

```
VerbatimRule: findings-sealed-echo
  target-field: findings-sealed (Summary section, Step 13)
  source-token: [FINDINGS-COMPLETE count=N findings] (emitted at end of Step 9)
  copy-rule: the findings-sealed field value MUST be copied character-for-character from the
             [FINDINGS-COMPLETE count=N findings] token; the copy includes the bracket
             delimiters, the "count=" prefix, the integer N, the space, and the word
             "findings" exactly as they appear in the emitted token
  violation: any reformulation, paraphrase, count adjustment, or bracket omission
             constitutes a summary-integrity violation detectable by string comparison alone
  verification: string-compare findings-sealed value against [FINDINGS-COMPLETE] token;
                any character difference is a violation

TaxonomyEchoRule: taxonomy-version-field
  target-field: taxonomy-version (Summary section, Step 13)
  source-token: [TAXONOMY-DECLARED version=N] (most recent seal from Step 3 or re-seal)
  copy-rule: the taxonomy-version field value MUST copy the [TAXONOMY-DECLARED version=N]
             seal verbatim; the copy includes the bracket delimiters, the "version=" prefix,
             and the integer N exactly as they appear in the most recent seal
  violation: a version-skew between taxonomy-version field and the most recent seal constitutes
             a summary-integrity violation; the discrepancy is detectable by counter comparison
  verification: compare taxonomy-version field value against the most recent [TAXONOMY-DECLARED
                version=N] seal; any difference in the version integer is a version-skew violation
```

`[GOVERNANCE-PREAMBLE-DECLARED — VerbatimRule findings-sealed-echo and TaxonomyEchoRule taxonomy-version-field are the authoritative Summary echo contracts for this trace. Step 13 references both by name; neither rule text is restated at Step 13.]`

**Step 3 — MechanismTypeTaxonomy Declaration with Versioned Seal**

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the
    token to the tokens list, increment AmendmentVersion by 1, and re-seal as
    [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. Version=0 means no amendments have been applied. The TaxonomyEchoRule taxonomy-version-field (declared in Step 2) governs the taxonomy-version: echo in the Summary. AmendmentProtocol governs all extensions.]`

**Step 4 — GateTokenSchema (typed-column declaration)**

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an
    automatic SCHEMA-PHASE-FAIL independent of the element diff result
  FailureToken:
    SCHEMA-PHASE-FAIL:
      trigger: type-constraint violated for any GateTokenSchema field
    SCHEMA-OMISSION-FAIL:
      trigger: row absent from schema-sweep output (OmissionRule violation)
```

`[SCHEMA-SEALED]`

**Step 5 — ObligationBlock Construction**

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

`[OBLIGATION-BLOCK-SEALED — census-gate-obligations is the authoritative obligation source.]`

**Step 6 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema, ObligationBlock, MechanismTypeTaxonomy (version=0), and Governance Preamble above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 7 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 8 — Schema Diff Phase**

Before the element-level diff, run the schema diff. Apply the OmissionRule declared in GateTokenSchema.

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason} → SCHEMA-PHASE-FAIL` if value fails type constraint
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field → SCHEMA-OMISSION-FAIL` if field absent

Schema sweep row count: {N swept} / {N declared}.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; OmissionRule satisfied. Element diff may now begin.]`

**Step 9 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — see [TAXONOMY-DECLARED version=0]]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token.]`

**Step 10 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 11 — Sub-task B: Staging Lines and Pattern Fill**

Write a `## Sub-task B: Census Fill` section.

Group findings by mechanism-type-token. Derive `mechanism-type-shared` from staging lines — do not re-derive from findings.

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Prohibit: re-derive-mechanism)

**Step 12 — Gate Token: S6.5**

Emit the complete gate token using every required-field row from the sealed GateTokenSchema:

```
gate-token:
  census-distribution: {value — carried forward unchanged from S5.5-Sub-task-A}
  gate-provenance: §S5.5-Sub-task-A
  gate-status: {PASS | FAIL}
  attestation-by: {census-owner role name — non-null required}
  attestation-result: {census owner's claim value — non-null required}
  verification-by: {witness role name — non-null required, MUST differ from attestation-by}
  verification-result: {independent verification outcome — non-null required}
```

`[TAXONOMY-CENSUS-COMPLETE]`

**Step 13 — Summary**

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
schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints
```

see: VerbatimRule: findings-sealed-echo — `findings-sealed:` MUST be copied character-for-character from `[FINDINGS-COMPLETE count=N findings]`; string comparison verifies correctness.

see: TaxonomyEchoRule: taxonomy-version-field — `taxonomy-version:` MUST copy the most recent `[TAXONOMY-DECLARED version=N]` seal verbatim; counter comparison detects version-skew.

Both governance rules are declared in the Governance Preamble (Step 2). If either echo field deviates from its source token, a summary-integrity finding MUST be raised before the summary is considered closed.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`

---

## V-05 — Combined: All Three R20 Advances as GovernancePreamble Layers

**axis:** output-format + lifecycle-emphasis — `VerbatimRule:` (C-54), `TaxonomyEchoRule:` (C-55), and `RemediationContract:` (C-56) declared as co-equal named governance layers in a `GovernancePreamble:` block before execution begins; all three cross-referenced by layer name from every phase that emits or consumes a governed value; Summary section carries both echo fields; FailureToken block carries `remediation:` per entry

**hypothesis:** Declaring all three R20 governance advances as co-equal named layers in a pre-execution preamble forces each to be structurally committed before any census or gate work starts. Later phases reference pre-declared governance layers by name rather than constructing constraints inline: Step 9 references `VerbatimRule: findings-sealed-echo` by name; Step 13 references `TaxonomyEchoRule: taxonomy-version-field` by name; Step 8 references `RemediationContract: failure-token-remediation` by name. A reader auditing governance completeness reads only the `GovernancePreamble:` block — no body scanning required. The preamble is to governance what the `ObligationBlock:` is to census obligations: a single, addressable reference unit. Prediction: C-54, C-55, and C-56 all pass; all prior criteria hold at baseline because all structural elements from R19 are carried forward without reduction.

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

**Step 2 — GovernancePreamble: Three Co-Equal Governance Layers**

Before declaring the taxonomy, schema, or obligation block, declare all three R20 governance layers as a named, addressable preamble. Each layer governs a specific structural commitment; later steps reference layers by name only. The preamble is the sole governance declaration site — no layer is restated inline.

```
GovernancePreamble:

  Layer-1: VerbatimRule findings-sealed-echo
    governs: findings-sealed field in Summary section (Step 14)
    source: [FINDINGS-COMPLETE count=N findings] token (Step 10)
    copy-rule: the findings-sealed field value MUST be copied character-for-character from
               the [FINDINGS-COMPLETE count=N findings] token; the copy includes the bracket
               delimiters, the "count=" prefix, the integer N, the space, and the word
               "findings" exactly as they appear in the emitted token
    violation: any reformulation, paraphrase, count adjustment, or bracket omission constitutes
               a summary-integrity violation detectable by string comparison alone
    verification: string-compare findings-sealed value against [FINDINGS-COMPLETE] token;
                  any character difference is a violation, not a rendering variant

  Layer-2: TaxonomyEchoRule taxonomy-version-field
    governs: taxonomy-version field in Summary section (Step 14)
    source: [TAXONOMY-DECLARED version=N] seal (most recent from Step 3 or re-seal)
    copy-rule: the taxonomy-version field value MUST copy the [TAXONOMY-DECLARED version=N]
               seal verbatim; the copy includes the bracket delimiters, the "version=" prefix,
               and the integer N exactly as they appear in the most recent seal
    violation: a version-skew between taxonomy-version field and the most recent seal constitutes
               a summary-integrity violation detectable by counter comparison
    verification: compare taxonomy-version field value against the most recent seal;
                  any difference in the version integer is a version-skew violation

  Layer-3: RemediationContract failure-token-remediation
    governs: FailureToken block entries in GateTokenSchema (Step 4)
    rule: each FailureToken entry MUST carry a named remediation: field specifying the required
          corrective action; the remediation path MUST be unique per token — a shared remediation
          path across SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL constitutes a structural
          violation of the FailureToken contract
    tokens-governed:
      SCHEMA-PHASE-FAIL:
        remediation: correct field type to match declared constraint and re-sweep from the top
      SCHEMA-OMISSION-FAIL:
        remediation: add absent row to actual output and re-sweep from the top
    machine-derivation: the required corrective action MUST be derivable from the emitted
                        token alone by field lookup without reading failure rationale text
```

`[GOVERNANCE-PREAMBLE-DECLARED — Three governance layers are active for this trace:
  Layer-1 VerbatimRule findings-sealed-echo (C-54 contract)
  Layer-2 TaxonomyEchoRule taxonomy-version-field (C-55 contract)
  Layer-3 RemediationContract failure-token-remediation (C-56 contract)
Each layer is referenced by name from its governing step. No layer text is restated outside this preamble.]`

**Step 3 — MechanismTypeTaxonomy Declaration with Versioned Seal**

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
  AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the
    token to the tokens list, increment AmendmentVersion by 1, and re-seal as
    [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token;
    a taxonomy block copied forward into a new trace must reset AmendmentVersion to 0 unless
    amendments carry over
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. Version=0 means no amendments applied. GovernancePreamble Layer-2 (TaxonomyEchoRule) governs the taxonomy-version: echo in the Summary. AmendmentProtocol governs all extensions.]`

**Step 4 — GateTokenSchema with RemediationContract**

Declare the `GateTokenSchema`. The `FailureToken:` block is governed by GovernancePreamble Layer-3 (RemediationContract failure-token-remediation); `remediation:` fields are copied from that layer verbatim.

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
  OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an
    automatic SCHEMA-PHASE-FAIL independent of the element diff result
  FailureToken:
    SCHEMA-PHASE-FAIL:
      trigger: type-constraint violated for any GateTokenSchema field during schema sweep
      remediation: correct field type to match declared constraint and re-sweep the schema from the top; do not proceed to element diff until SCHEMA-DIFF-COMPLETE is re-emitted
    SCHEMA-OMISSION-FAIL:
      trigger: row absent from schema-sweep output (OmissionRule violation)
      remediation: add absent row to actual output and re-sweep the schema from the top; do not proceed to element diff until SCHEMA-DIFF-COMPLETE is re-emitted
  governance: see GovernancePreamble Layer-3 RemediationContract failure-token-remediation
```

`[SCHEMA-SEALED — GateTokenSchema declared. FailureToken block governed by GovernancePreamble Layer-3. remediation: fields are unique per token as required by the RemediationContract.]`

**Step 5 — ObligationBlock Construction**

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

**Step 6 — Expected Output**

Write a `## Expected Output` section from the spec alone. Do not run the operation.

For each spec-defined element: `- {field}: {expected value or constraint}  [spec §X.Y]`
If not spec-defined: `- {field}: not specified in spec`

Cover: success path, at least one error path, at least one edge case. Reference GateTokenSchema fields by name for gate token entries.

`[EXPECTED-SEALED — Contract Expert exits. Expected Output, GateTokenSchema (with FailureToken RemediationContract), ObligationBlock, MechanismTypeTaxonomy (version=0), and GovernancePreamble above are locked. Automate begins below. No modification permitted after this line.]`

---

### ROLE: Automate — Actual Capture Phase [30-ACTUAL]

You begin here. You have not read the Expected Output or any sealed declarations above.

**Step 7 — Actual Output**

Run or simulate the operation. Write a `## Actual Output` section. Record every field, status code, header, and observable behavior — including every field in the emitted gate token.

Format: `- {field}: {observed value}`. If absent: `- {field}: [not returned]`. If not verifiable: `- {field}: [not verifiable — reason]`.

When fully recorded: `[ACTUAL OUTPUT COMPLETE — Automate exits. Contract Expert resumes.]`

---

### ROLE: Connectors Contract Expert — Post-Run Phase

**Step 8 — Schema Diff Phase**

Before the element-level diff, run the schema diff. Apply the OmissionRule and FailureToken RemediationContract (GovernancePreamble Layer-3).

For each row in GateTokenSchema (sweep every row — no row may be omitted):
- `{field}: declared type {type} — actual value: {value} — CONFORMS` if value satisfies type constraint
- `{field}: declared type {type} — actual value: {value} — VIOLATES: {reason} → SCHEMA-PHASE-FAIL` if value fails type constraint
  - see: GovernancePreamble Layer-3 RemediationContract SCHEMA-PHASE-FAIL.remediation
- `{field}: declared type {type} — actual value: [not returned] — VIOLATES: missing-field → SCHEMA-OMISSION-FAIL` if field absent
  - see: GovernancePreamble Layer-3 RemediationContract SCHEMA-OMISSION-FAIL.remediation

Schema sweep row count: {N swept} / {N declared}.

`[SCHEMA-DIFF-COMPLETE — {N swept} / {N declared} GateTokenSchema rows swept; RemediationContract Layer-3 satisfied. Element diff may now begin.]`

**Step 9 — MechanismTypeTaxonomy Amendment Gate**

Before writing any finding blocks, confirm the current taxonomy version. If any finding during the element diff requires a new mechanism-type token: pause, apply AmendmentProtocol (add token, increment AmendmentVersion, re-seal as `[TAXONOMY-DECLARED version=N+1]`). The re-seal updates the source for GovernancePreamble Layer-2 TaxonomyEchoRule: the Summary's `taxonomy-version:` field must echo the most recent seal after all amendments are applied.

**Step 10 — Element Diff and Findings**

Write a `## Findings` section. Compare each Expected Output entry against the Actual Output entry.

Match: `- {field}: PASS`

Deviation — Finding block:
```
Finding F-NN
element: {field name} — {surface: success/error/edge}
deviation: expected {X}; actual {Y}
severity: [breaking | degraded | cosmetic]
mechanism-type: [token drawn from MechanismTypeTaxonomy — verify against current [TAXONOMY-DECLARED version=N] seal]
spec: [exact spec clause violated]
hypothesis: [one sentence naming the mechanism — component, condition, sequence responsible]
recommendation: [amend-spec | fix-impl | needs-discussion] — [rationale]  (breaking/degraded only)
```

When all Expected entries have been compared and all finding blocks are written:

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. GovernancePreamble Layer-1 VerbatimRule governs the findings-sealed: echo at Step 14.]`

**Step 11 — Sub-task A: Mechanism-Distribution Census**

Write a `## Sub-task A: Mechanism Distribution` section.

`mechanism-distribution: {F-01: mechanism-type-token}, {F-02: mechanism-type-token}, ...`

All tokens must appear in MechanismTypeTaxonomy at the current version — verify against the most recent `[TAXONOMY-DECLARED version=N]` seal.

see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)

**Step 12 — Sub-task B: Staging Lines and Pattern Fill**

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

see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance, Prohibit: re-derive-mechanism)

**Step 13 — Gate Token: S6.5**

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

**Step 14 — Summary**

Before writing the Summary, satisfy all three GovernancePreamble layer obligations:
- Layer-1 VerbatimRule: copy `findings-sealed:` character-for-character from `[FINDINGS-COMPLETE count=N findings]`
- Layer-2 TaxonomyEchoRule: copy `taxonomy-version:` verbatim from the most recent `[TAXONOMY-DECLARED version=N]` seal
- Layer-3 RemediationContract: if any FailureToken was emitted, confirm its `remediation:` field is derivable from the token alone

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
schema-phase: {PASS | SCHEMA-PHASE-FAIL | SCHEMA-OMISSION-FAIL} — {N swept} / {N declared} GateTokenSchema rows swept
mechanism-type-shared: {token from Sub-task B}
gate-status: {PASS | FAIL}

Verdict: Contract violated / Contract satisfied

Coverage: {N PASS} / {N total Expected entries} fields verified, {N deviations} deviations
Schema: {N fields typed} / {N total GateTokenSchema fields} fields carry type constraints

Governance: GovernancePreamble Layer-1 findings-sealed-echo SATISFIED | VIOLATED
            GovernancePreamble Layer-2 taxonomy-version-field SATISFIED | VIOLATED
            GovernancePreamble Layer-3 failure-token-remediation SATISFIED | VIOLATED | NOT-TRIGGERED
```

If any Governance entry is VIOLATED, a summary-integrity finding MUST be raised before the trace is closed. A VIOLATED governance layer is a breaking finding against the trace output itself, not the operation under test.

---

**Output artifact:** Write to `simulations/trace/contract/{topic}-contract-{date}.md`
