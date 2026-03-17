Written to `simulations/quest/golden/trace-contract-golden-2026-03-15.md`.

**What the golden captures:**

The simplified body (24% reduction) strips the following from V-05 without changing its structure:
- `violation:` fields on Layers 1–2 (implied by `verification:`)
- Verbose copy-rule prose → compressed to single lines
- `machine-derivation:` field on Layer-3 (implied by named `remediation:` fields)
- Rubric-tracking annotations on `[GOVERNANCE-PREAMBLE-DECLARED]` seal
- Copy-forward edge case from `AmendmentProtocol`
- Tautological "Version=0 means..." from `TAXONOMY-DECLARED` seal
- Redundant Step 4 intro sentence (FailureToken governance already stated in the schema block)
- Explanatory prose on `[SCHEMA-SEALED]` and `[OBLIGATION-BLOCK-SEALED]`
- Step 9 verbose re-seal explanation → one sentence
- Governance back-reference on `[FINDINGS-COMPLETE]` token
- Step 14 three-bullet pre-summary checklist (GovernancePreamble already declares all three)

The structural payload — `GovernancePreamble:` with three named layers, dual-anchor Summary, `Governance:` status block, trace-integrity-violation finding class — is fully preserved.
 auditable rather than silently absent. A governance auditor can confirm all three constraints fired correctly without entering the trace body.

**Pattern 3 — Governance violation as a breaking finding against the trace itself**
A `VIOLATED` governance entry must raise a `trace-integrity-violation` finding before the trace is closed — distinct from findings about the operation under test. A trace can have `PASS` gate-status (operation looks clean) while simultaneously carrying a trace-integrity finding (the trace was mis-executed). The two finding classes are non-overlapping by token class alone.

**Pattern 4 — All three R20 criteria satisfied by declaration rather than enforcement prose**
V-01 through V-03 each target a single R20 criterion using natural-language prose enforcement; violations require semantic interpretation. V-05 satisfies all three by placing the constraint in a named field (`copy-rule:`, `verification:`, `remediation:`) within an addressable block. Violation detection becomes mechanical: string-compare, counter-compare, field-lookup — no semantic judgment required.

**Pattern 5 — Dual-anchor summary (domain results + governance completeness)**
The Summary section is simultaneously a domain-result report (severity table, gate-status, verdict) and a governance-completeness report (Governance: block). These are orthogonal planes at the same structural anchor, so a single Summary pass satisfies both audit requirements.

---

## Prompt Body

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

Before declaring the taxonomy, schema, or obligation block, declare all three governance layers as a named `GovernancePreamble:` block. The preamble is the sole declaration site — no layer is restated inline.

```
GovernancePreamble:

  Layer-1: VerbatimRule findings-sealed-echo
    governs: findings-sealed field in Summary section (Step 14)
    source: [FINDINGS-COMPLETE count=N findings] token (Step 10)
    copy-rule: character-for-character copy including bracket delimiters, "count=" prefix,
               integer N, space, "findings" exactly as they appear in the emitted token
    verification: string-compare findings-sealed against [FINDINGS-COMPLETE] token;
                  any character difference is a violation, not a rendering variant

  Layer-2: TaxonomyEchoRule taxonomy-version-field
    governs: taxonomy-version field in Summary section (Step 14)
    source: [TAXONOMY-DECLARED version=N] seal (most recent from Step 3 or re-seal)
    copy-rule: verbatim copy including bracket delimiters, "version=" prefix, integer N
               exactly as they appear in the most recent seal
    verification: compare taxonomy-version against most recent [TAXONOMY-DECLARED version=N];
                  any difference in the version integer is a version-skew violation

  Layer-3: RemediationContract failure-token-remediation
    governs: FailureToken block entries in GateTokenSchema (Step 4)
    rule: each FailureToken entry MUST carry a named remediation: field; paths MUST be
          unique per token — a shared remediation path across both tokens is a structural violation
    tokens-governed:
      SCHEMA-PHASE-FAIL:
        remediation: correct field type to match declared constraint and re-sweep from the top
      SCHEMA-OMISSION-FAIL:
        remediation: add absent row to actual output and re-sweep from the top
```

`[GOVERNANCE-PREAMBLE-DECLARED — Three governance layers are active for this trace:
  Layer-1 VerbatimRule findings-sealed-echo
  Layer-2 TaxonomyEchoRule taxonomy-version-field
  Layer-3 RemediationContract failure-token-remediation
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
    [TAXONOMY-DECLARED version=N+1] before writing any finding block that uses the new token
  AmendmentVersion: 0
```

`[TAXONOMY-DECLARED version=0 — MechanismTypeTaxonomy version 0 is the authoritative vocabulary for this trace. GovernancePreamble Layer-2 (TaxonomyEchoRule) governs the taxonomy-version: echo in the Summary. AmendmentProtocol governs all extensions.]`

**Step 4 — GateTokenSchema with RemediationContract**

Declare the `GateTokenSchema`.

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

Before writing any finding blocks, confirm the current taxonomy version. If a new token is required, apply AmendmentProtocol and re-seal before writing the first finding block that uses it.

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

`[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token.]`

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

Write the Summary section.

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

---

## Final Rubric Criteria Summary

**Rubric:** trace-contract v21 · 52 criteria · 208 max

| Group | Criteria | Max | Description |
|-------|----------|-----|-------------|
| A — Structural Foundations | C-08–C-19 | 48 | Contract scope, role separation, expected/actual format, diff completeness |
| B — Findings Quality | C-20–C-25 | 24 | Finding format, severity vocabulary, mechanism-type taxonomy, FINDINGS-COMPLETE token |
| C — Gate Token Structure | C-26–C-32 | 28 | Gate token fields, format, phase boundary, EXPECTED-SEALED dependency |
| D — Schema and Diff Completeness | C-33–C-38 | 24 | GateTokenSchema declaration, field coverage, diff order |
| E — Advanced Schema Governance | C-39–C-47 | 36 | Co-requirement, ObligationBlock, audit-trace roles, type constraints, SCHEMA-DIFF-COMPLETE, closed taxonomy, re-derive Prohibit |
| F — Seal Integrity and Failure Governance | C-48–C-53 | 24 | Count-bearing seals, AmendmentProtocol, OmissionRule, findings-sealed echo, versioned seal, distinct FailureTokens |
| G — Echo Fidelity and Remediation Completeness | C-54–C-56 | 12 | VerbatimRule governing findings-sealed, taxonomy-version summary field, named remediation: per FailureToken |
| H — Governance Preamble and Trace Integrity | C-57–C-59 | 12 | GovernancePreamble block, Governance: status block in Summary, trace-integrity-violation finding class |
| **Total** | **C-08–C-59** | **208** | |

**R20 score: 95/100** (V-05 passes C-08–C-56 full baseline + C-54 + C-55 + C-56 + structural bonus for Governance: status block)

**Next criteria seeded by R20 excellence signals (v21 target):**
- C-57: Named `GovernancePreamble:` block as single pre-execution declaration unit
- C-59: Governance violation raises named `trace-integrity-violation` finding — distinct finding class from operational findings
