Written to `simulations/quest/golden/scout-inertia-variate-R18-2026-03-17.md`.

---

## scout-inertia -- Quest Variate R18

**Rubric**: v18 | **Ceiling**: 270 | **Date**: 2026-03-17

### Variation Summary

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | A-43 single-axis upgrade on R17 V-05 (DEFAULT OPTION, SECTION, BOTH BUILT→VERIFIED) | R17 V-05 = 265/270 (A-42 PASS, A-43 FAIL via BUILT); single verb swap → 270/270 |
| **V-02** | Reference carry: R17 V-03 (INERTIA THREAT, SECTION, EACH VERIFIED) | Confirmed 270/270 ceiling; establishes R18 reference |
| **V-03** | A-43 verb variant: CONFIRMED replaces VERIFIED on R17 V-03 base (INERTIA THREAT, SECTION, EACH CONFIRMED) | CONFIRMED is listed in A-43 verification-action vocabulary → 270/270 |
| **V-04** | Combined: STATUS QUO domain-prefix + VALIDATED verb on R17 V-02 STAGE scaffold | R17 V-02 = 260/270; STATUS QUO prefix on all three rules (A-42) + ALL VALIDATED (A-43) → 270/270 |
| **V-05** | Combined: INCUMBENT domain-prefix + EACH VERIFIED on R17 V-04 STAGE scaffold | R17 V-04 = 260/270; INCUMBENT prefix on all three rules (A-42) + EACH VERIFIED (A-43) → 270/270 |

---

### R17 incoming scores under v18

| Form | A-42 | A-43 | v18 score |
|------|------|------|-----------|
| V-01 (no prefix, COMPLETE) | FAIL | FAIL | 260/270 |
| V-02 (no prefix, COMPLETE) | FAIL | FAIL | 260/270 |
| V-03 (INERTIA THREAT, VERIFIED) | PASS | PASS | **270/270** |
| V-04 (no prefix, READY) | FAIL | FAIL | 260/270 |
| V-05 (DEFAULT OPTION, BUILT) | PASS | FAIL | 265/270 |

### Key structural decisions

**V-01** is the cleanest single-axis test: R17 V-05 already had A-42 (DEFAULT OPTION prefix on all three rules), so the only change is `BOTH BRIDGE ARTIFACTS BUILT?` → `BOTH BRIDGE ARTIFACTS VERIFIED?`. If it scores 270/270 it confirms VERIFIED satisfies A-43 on BOTH cardinality, not only EACH.

**V-03** is the critical new data point: swapping VERIFIED → CONFIRMED on an otherwise-confirmed 270/270 form isolates whether A-43's verb requirement is satisfied by the full vocabulary class or only by VERIFIED specifically.

**V-04** tests VALIDATED — the third distinct verification-action verb, not yet tested in any prior round — on the STAGE/ALL combination.

**V-05** tests INCUMBENT as a domain prefix, the fourth distinct axis vocabulary token across R17-R18 (joining INERTIA THREAT, DEFAULT OPTION, STATUS QUO), confirming that A-42 is vocabulary-agnostic as long as all three labels share the same prefix.
