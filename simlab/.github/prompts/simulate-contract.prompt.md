---
mode: agent
description: "Verify implementation against spec contract. Use --type to target a specific verification dimension: --type component (U"
---
You are running /simulate-contract for: {{topic}}

Verify that the implementation matches the spec contract for {{topic}}. This skill
compares expected behavior (from the spec) against actual output, using a structured
gate schema to identify mismatches.

Provide:
1. The spec or contract to verify against (paste text or provide path)
2. The actual implementation output to compare

The skill will produce a mismatch report with severity ratings and a GO/NO-GO gate result.

Write artifact to: signals/simulate/contract/{{topic}}-contract-{{date}}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
Include frontmatter: skill: simulate-contract, topic: {{topic}}, date: {{date}}, gate_result: PASS|FAIL

---

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