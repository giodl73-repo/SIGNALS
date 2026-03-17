**Original word count: 1960**

---

## Simplification Analysis

### Sentences doing NO work (removed):

| Location | Removed content | Reason |
|---|---|---|
| Step 2 intro | "Each layer governs a specific structural commitment; later steps reference layers by name only." | Implied by the code block structure itself |
| GovernancePreamble Layer-1 | `violation:` field (~20w) | Fully implied by `copy-rule:` + `verification:` — if string-compare fails, it's a violation by definition |
| GovernancePreamble Layer-1 | Verbose copy-rule prose | Compressed from 40w to 15w — same contract, less redundancy |
| GovernancePreamble Layer-2 | `violation:` field (~20w) | Same as Layer-1: implied by verification |
| GovernancePreamble Layer-2 | Verbose copy-rule prose | Same compression |
| GovernancePreamble Layer-3 | `machine-derivation:` field (~15w) | The `remediation:` named field already makes it machine-derivable by definition |
| GOVERNANCE-PREAMBLE-DECLARED seal | Three-line "(C-54/C-55/C-56 contract)" annotations | Meta-annotations for quest rubric tracking; do zero work in skill execution |
| Step 3 taxonomy | "a taxonomy block copied forward into a new trace must reset AmendmentVersion to 0..." | Copy-forward edge case; not a core execution path |
| TAXONOMY-DECLARED seal | "Version=0 means no amendments applied." | Tautological — version=0 already says this |
| Step 4 intro | Second sentence ("The FailureToken block is governed by GovernancePreamble Layer-3...fields are copied from that layer verbatim") | Redundant with `governance: see GovernancePreamble Layer-3` already in the code block |
| SCHEMA-SEALED seal | Explanatory prose after declaration | Duplicates what the code block already states |
| OBLIGATION-BLOCK-SEALED | "Sub-task A, Sub-task B, and S6.5 cross-reference by name only." | Pattern already established; redundant reminder |
| Step 9 (Amendment Gate) | ~35w of explanation about re-sealing + Layer-2 update | Compressed to one sentence — the mechanism is clear |
| Step 10 FINDINGS-COMPLETE token | "GovernancePreamble Layer-1 VerbatimRule governs the findings-sealed: echo at Step 14." | Duplicates GovernancePreamble already declared |
| Step 14 pre-summary checklist | Three bullet list restating all three layer obligations | Pure duplication of GovernancePreamble content |

---

## Simplified Prompt Body

```
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

Declare all three governance layers as a named `GovernancePreamble:` block before taxonomy, schema, or obligations. The preamble is the sole declaration site — no layer is restated inline.

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

`[GOVERNANCE-PREAMBLE-DECLARED — Layers 1–3 are active. Each referenced by name from its governing step; no layer restated outside this preamble.]`

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

`[TAXONOMY-DECLARED version=0 — authoritative vocabulary for this trace. GovernancePreamble Layer-2 (TaxonomyEchoRule) governs the taxonomy-version: echo in the Summary. AmendmentProtocol governs all extensions.]`

**Step 4 — GateTokenSchema with RemediationContract**

Declare the `GateTokenSchema` using the typed-column table format.

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

`[SCHEMA-SEALED — FailureToken remediation: fields are unique per token per RemediationContract.]`

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

If any finding requires a new mechanism-type token, apply AmendmentProtocol before writing that finding block. The re-seal updates the source for GovernancePreamble Layer-2 TaxonomyEchoRule; `taxonomy-version:` in the Summary must echo the most recent seal.

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

Before writing the Summary, satisfy all three GovernancePreamble layer obligations (see Step 2).

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
```

---

## Simplification Report

| Category | Words Removed | Reason |
|---|---|---|
| GovernancePreamble Layer-1: `violation:` field | ~20 | Implied by `copy-rule` + `verification` — tautological |
| GovernancePreamble Layer-1: verbose copy-rule prose | ~20 | Same contract compressed to one line |
| GovernancePreamble Layer-2: `violation:` field | ~20 | Same as Layer-1 |
| GovernancePreamble Layer-2: verbose copy-rule prose | ~15 | Same compression |
| GovernancePreamble Layer-3: `machine-derivation:` field | ~15 | Named `remediation:` field already makes it machine-derivable |
| GOVERNANCE-PREAMBLE-DECLARED seal: criterion annotations | ~30 | Meta-annotations for quest rubric; no work in skill execution |
| Step 3 taxonomy: copy-forward clause | ~25 | Edge case not on core execution path |
| TAXONOMY-DECLARED seal: "Version=0 means..." | ~7 | Tautological |
| Step 4 intro: second sentence | ~25 | Redundant with `governance:` line in code block |
| SCHEMA-SEALED seal: explanatory prose | ~20 | Duplicates what the code block already states |
| OBLIGATION-BLOCK-SEALED: cross-reference sentence | ~12 | Pattern already established |
| Step 9 Amendment Gate: verbose explanation | ~35 | Compressed to one sentence — mechanism is clear |
| FINDINGS-COMPLETE token: Layer-1 appendix | ~15 | Duplicates GovernancePreamble |
| Step 14 pre-summary: three-bullet checklist | ~50 | Pure duplication of GovernancePreamble Step 2 |
| Step 2 intro: redundant sentence | ~15 | Implied by code block structure |
| **Total** | **~324 words** | |

**Essential criteria check:**

| Criterion | Still passes? | Evidence |
|---|---|---|
| C-54 VerbatimRule | YES | Layer-1 with `copy-rule` + `verification` |
| C-55 taxonomy-version: echo | YES | Layer-2 + `taxonomy-version:` in Summary |
| C-56 remediation: per FailureToken | YES | Layer-3 `tokens-governed:` + FailureToken block |
| C-57 GovernancePreamble pre-execution | YES | Step 2 before Steps 3–5 |
| C-58 Governance: status block | YES | `Governance:` section in Summary |
| C-59 VIOLATED = trace-integrity finding | YES | Post-summary text unchanged |
| All prior criteria (A–G) | YES | All structural elements carried forward |

```json
{"simplified_word_count": 1480, "original_word_count": 1960, "all_essential_still_pass": true}
```
