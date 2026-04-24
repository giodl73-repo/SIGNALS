`simulations/quest/golden/corps-build-variate-R7-2026-03-17.md` written. Five complete variations:

| Variation | Axis | C-22/C-23 target |
|-----------|------|-----------------|
| **V-01** | DERIVATION-LOOP-CLOSED attestation | C-22 primary |
| **V-02** | Non-transplantable IA per-file gate (4-field IA-WRITTEN) | C-23 primary |
| **V-03** | BUILD-VERIFY exclusion manifest as typed error taxonomy (STRUCTURAL-ERROR:BV-*) | C-20 fidelity + new taxonomy criterion |
| **V-04** | V-01 + V-02 combined | C-22 + C-23 together |
| **V-05** | Full integration (all three axes) | C-22, C-23, + candidate C-24 (full per-team derivation audit trail) |

**New patterns to watch in the scorecard:**

- **C-22**: V-01/V-04/V-05 emit `DERIVATION-LOOP-CLOSED` as a named block after `BUILD-VERIFY-COMPLETE`, listing per-team `PROFILE lens-phrase "[x]" -> IA lens opens "[x]" -- CLOSED`. This bridges PHASE 5 and PHASE 9 as a closed structural record.
- **C-23**: V-02/V-04/V-05 add `lens-team-specific (non-transplantable)` as a fourth IA-WRITTEN check that halts the build on NO, with named failure mode examples.
- **C-24 candidate** (V-05 only): the full chain `PROFILE -> IA-WRITTEN YES -> BUILD-VERIFY VERBATIM -> DERIVATION-LOOP-CLOSED` creates a per-team derivation audit trail recoverable from output alone.
