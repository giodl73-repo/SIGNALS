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