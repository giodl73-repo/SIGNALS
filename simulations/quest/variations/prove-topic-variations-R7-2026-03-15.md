**Round 7 complete.** Five variations written to `simulations/quest/golden/prove-topic-variate-R7-2026-03-15.md`.

---

## Round 7 Summary

**Targets:** C-23 (`incumbent_defense_closed` independent of `co_activation_confirmed`) and C-24 (two blocking roles each with sole-owned attestation fields, construction-enforced).

**Severity stack gap from R6 V-05:**
- C-23: `incumbent_defense_closed` present in handoff but defined inside the DUAL-LOCK block — independence is logically true but structurally entangled with `co_activation_confirmed`
- C-24: two roles, two fields — but ownership is declared in GATE S via an echo comment, not at ROLE definition time

| Variation | Axis | C-23 | C-24 | Composite |
|-----------|------|------|------|-----------|
| V-01 | handoff-field-independence | PASS | PARTIAL | ~140/144 |
| V-02 | role-field-ownership | PARTIAL | PASS | ~140/144 |
| V-03 | campaign-open-schema | PASS | PARTIAL | ~140/144 |
| V-04 | V-01 × V-02 | PASS | PASS | 144/144 |
| V-05 | all R6 V-05 + V-01 + V-02 | PASS | PASS | 144/144 |

**Key mechanisms:**
- **V-01/V-04/V-05**: CAMPAIGN OUTCOME block at Stage 4 computes `incumbent_defense_closed` from `null_tally_final` before synthesis begins — independent derivation path, no dual-lock chain inference needed
- **V-02/V-04/V-05**: ATTESTATION MANIFEST at campaign open + `OWNED ATTESTATION FIELD:` at each ROLE header — ownership visible from schema, not from conditional instructions inside GATE S
- **V-03**: Different C-23 angle — HANDOFF SCHEMA pre-declared before Stage 1, listing all fields with derivation sources; independence contract is a campaign invariant, not a synthesis outcome

**Anchor: V-05.** Closes C-01 through C-24 with each criterion arising from its own structural source. The v7 ceiling.
