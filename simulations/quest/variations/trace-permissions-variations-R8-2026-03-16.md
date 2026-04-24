File written to `simulations/quest/golden/trace-permissions-variate-R8-2026-03-17.md`.

---

## trace-permissions — Round 8 Variate (Rubric v12)

**Baseline:** R7-V-05 = 28/28 (100.0). All R8 variations inherit the full architecture.
**New territory:** C-37 (proposed) — D-2 attestation row must explicitly cite "CA-1.9 PASS" as its stated basis, preventing fabricated ATTESTED when CA-1.9 is absent.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis — explicit attestation basis citation (C-37 single-axis) | Adding a mandatory `"explicit basis: CA-1.9 PASS"` literal to the D-2 CA Confirmation cell converts the co-presence relationship into a visible dependency declaration. D-2 ATTESTED without this exact phrase is a format violation. |
| V-02 | Lifecycle emphasis — symmetric attestation chain | Extends the explicit-basis requirement to all three dimensions: D-1 must cite its Phase 0 evidence tokens verbatim; D-3 must cite CA-1.8 PASS. Tests whether symmetric citation requirements are stable and surfaces any D-1/D-3 fabrication risk. |
| V-03 | Phrasing register — full-imperative vocabulary | Eliminates all descriptive/guidance language; replaces every instruction with SHALL/MUST/PROHIBITED. Increases probability that exact-label requirements (SE-4 STRUCTURED CLOSE prefix, CA-1.9 vocabulary match) survive without soft-language escape. |
| V-04 | Combined V-01+V-02 | All three CA Confirmation cells carry explicit basis citations. Tests structural stability of symmetric requirements and verifies D-1 evidence tokens are achievable without disrupting Phase 0 output structure. |
| V-05 | Combined V-01+V-02+V-03 + Schema ID: CA-ATTEST | Registers the attestation table schema itself (`CA-ATTEST`) in the Schema Registry with an explicit "CA Confirmation: `ATTESTED — explicit basis: [token]` REQUIRED; bare ATTESTED PROHIBITED" rule. Creates a C-38 target surface: the Registry-preamble double-anchor (C-23 pattern) applied to the attestation table itself. |

---

## Key Structural Decisions

**Single-axis selection:** Lifecycle emphasis (V-01, V-02) and phrasing register (V-03). Role sequence and inertia framing are deferred — R7-V-05 already achieves 28/28 with the current role sequence, so sequence disruption risks regression rather than gain.

**The C-37 fabrication risk (from R7 scorecard):** R7-V-05 passes C-36 because CA-1.9 happens to be PASS and the attestation table says ATTESTED. But the attestation table's CA Confirmation cell has no format rule requiring it to cite CA-1.9. A model could write `ATTESTED` for D-2 with a failing or absent CA-1.9 — co-presence is not dependency. V-01 installs the explicit dependency; V-05 schema-anchors it.

**C-38 candidate (surfaced by V-05):** `Schema ID: CA-ATTEST` registration opens a new loop: CA-1 can double-anchor on the attestation table (Registry schema → preamble 0.2 declarations → CA-1.9/CA-1.8 → attestation rows). This is C-23's double-anchor pattern applied one level up.

**Predicted scores under v12:** All five variations inherit 28/28. Differentiation appears only under the expected v13 rubric that formalizes C-37.
