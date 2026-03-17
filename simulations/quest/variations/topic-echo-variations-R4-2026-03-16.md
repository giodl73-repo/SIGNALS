Written to `simulations/quest/golden/topic-echo-variate-R4-v4rubric-2026-03-16.md`.

---

## Round 4 Variations: `topic:echo` (rubric v4 / C-15 + C-16)

**Baseline:** R3 V-05 scored 120/120 on v3. v4 adds two new aspirational criteria.

**R3 V-05 gaps identified:**
- **C-15 gap:** Role boundary creates structural provenance but never *declares* it — freeze says "PBI frozen" without naming the mechanism type. Reviewer must infer structural vs. temporal from role structure.
- **C-16 gap:** Entry self-check is reviewer-framed ("a reviewer must be able to verify...") — C-16 requires producer attestation with named checks in declaration language.

---

### Variation Summary

| Variation | Axes | C-15 mechanism | C-16 attestation |
|-----------|------|----------------|------------------|
| **V-01** | Mechanism declaration (minimal) | One-line freeze label: "Mechanism: structural provenance (role-scope exclusion)..." | None — self-check remains reviewer-framed |
| **V-02** | Per-entry attestation | None — freeze unchanged | `Verified:` field with three named checks in declaration language |
| **V-03** | Mechanism declaration (strong) | Dedicated `## Pre-Commitment Provenance` section: mechanism type + strength hierarchy (structural > temporal) + reviewer calibration statement | None — self-check remains reviewer-framed |
| **V-04** | Mechanism declaration (minimal) + Attestation | V-01 freeze label | V-02 `Verified:` field |
| **V-05** | Provenance section + Evidentiary attestation | V-03 provenance section with full vocabulary | `Verified:` field that **quotes actual values** checked — evidentiary tier: "PBI-03 confirmed; entry reads: '...'; artifact confirmed; finding reads: '...'" |

---

### Key discriminating questions for R4 scoring

**C-15:** Does the rubric's pass condition require the vocabulary depth of a provenance section (V-03/V-05) or is the freeze label (V-01/V-04) sufficient? The rubric's pass bar is "The artifact declares how its PBI was isolated" — a label declares it. A section additionally explains strength hierarchy and reviewer implication. If declaration alone passes, V-04 wins. If reviewer-calibration guidance is required, V-05 wins.

**C-16:** Does "names each check explicitly" (rubric language) require quoting the actual values checked (V-05) or naming the check type (V-02/V-04)? V-02/V-04 write "Handle confirmed in Ledger; PB-NN confirmed; artifact confirmed." V-05 writes "Handle 'X' confirmed; PB-03 confirmed; entry reads '...'; artifact 'Y' confirmed; finding reads '...'." The rubric says a generic "verified" fails but named checks pass — the quoting may be above the pass threshold.
