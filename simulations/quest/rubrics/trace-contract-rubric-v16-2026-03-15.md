Reading the R15 scorecard, three synthesis patterns emerge:

- **V-R15-A**: GateTokenSchema field-type completeness — V-01, V-04, and V-05 pass C-39 by declaring a named `GateTokenSchema` with a `required-fields:` manifest and `co-requirement:` annotation. V-05 also enumerates `gate-status` as a third required field alongside `census-distribution` and `gate-provenance`. V-02 and V-03 PARTIAL because co-requirement is implied by field adjacency or prose description rather than enforced by a named schema structure. C-39 requires the schema and co-requirement declaration; V-R15-A identifies the next escalation: each field in the `required-fields:` manifest should carry an explicit type constraint (`string`, `enum[PASS|FAIL]`, `format: S-section-reference`), so that field-inspection validates value conformance as well as field presence — converting the schema from a field-existence check into a full structural contract whose violations are detectable by value inspection alone, without reading authoring prose → **C-42**

- **V-R15-B**: Named obligation block as addressable reference unit — V-02, V-04, and V-05 pass C-40 by emitting a complete `Bind:` / `Assert:` / `Prohibit:` chain covering all copy-forward and amendment-path obligations. V-01 PARTIAL because amendment-path obligations at Sub-task B remain in descriptive prose. V-03 PARTIAL because `Prohibit:` is absent and the amendment-path obligation uses a weaker prose form ("do not overwrite"). C-40 requires the full formal-imperative chain; V-R15-B identifies the next escalation: the complete obligation chain should be declared as a named, addressable block — `ObligationBlock: census-gate-obligations` — that can be cross-referenced from Sub-task A, Sub-task B, and S6.5 without restating the imperatives at each site, so that amendment-path consistency is enforceable by reference inspection rather than by auditing prose repetition across three instruction locations → **C-43**

- **V-R15-C**: Audit-trace fields encoding two-party execution in the gate token — V-03 and V-05 pass C-41 by assigning attestation to the census owner by explicit role name and assigning independent char-for-char verification to a distinct witness role. V-05 additionally states "no single role can silently satisfy both claim and proof" as an explicit negative constraint. V-01 PARTIAL because both steps share a single S6.5 block without role-name separation of the attestation function. V-02 and V-04 PARTIAL because attestation is not assigned to a named census-owner role. C-41 requires the two-party role structure; V-R15-C identifies the next escalation: the gate token itself should carry named audit-trace fields — `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:` — so that the two-party exchange is auditable from the emitted token without re-inspecting the instruction trace, and the gate boundary can be closed only when both named fields carry non-null values → **C-44**

---

# Rubric: trace-contract v16

Reading the scorecard, three synthesis patterns emerge from R15:

- **V-R15-A**: GateTokenSchema field-type completeness — V-01, V-04, and V-05 pass C-39 by declaring a named `GateTokenSchema` with a `required-fields:` manifest and `co-requirement:` annotation. V-05 enumerates `gate-status` as a third required field alongside `census-distribution` and `gate-provenance`. V-02 and V-03 PARTIAL because co-requirement is implied by field adjacency or prose description rather than enforced by a named schema structure. C-39 requires the schema and co-requirement declaration; V-R15-A identifies the next escalation: each field in the `required-fields:` manifest should carry an explicit type constraint (`string`, `enum[PASS|FAIL]`, `format: S-section-reference`), so that field-inspection validates value conformance as well as field presence — converting the schema from a field-existence check into a full structural contract whose violations are detectable by value inspection alone → **C-42**

- **V-R15-B**: Named obligation block as addressable reference unit — V-02, V-04, and V-05 pass C-40 by emitting a complete `Bind:` / `Assert:` / `Prohibit:` chain covering all copy-forward and amendment-path obligations. V-01 PARTIAL because amendment-path obligations at Sub-task B remain in descriptive prose. V-03 PARTIAL because `Prohibit:` is absent and the amendment-path obligation uses a weaker prose form. C-40 requires the full formal-imperative chain; V-R15-B identifies the next escalation: the complete obligation chain should be declared as a named, addressable block — `ObligationBlock: census-gate-obligations` — that can be cross-referenced from Sub-task A, Sub-task B, and S6.5 without restating the imperatives at each site, so that amendment-path consistency is enforceable by reference inspection rather than by auditing prose repetition across three instruction locations → **C-43**

- **V-R15-C**: Audit-trace fields encoding two-party execution in the gate token — V-03 and V-05 pass C-41 by assigning attestation to the census owner by explicit role name and assigning independent char-for-char verification to a distinct witness role. V-05 additionally states the negative constraint: no single role can silently satisfy both claim and proof. V-01 PARTIAL because both steps share a single S6.5 block without role-name separation of the attestation function. V-02 and V-04 PARTIAL because attestation is not assigned to a named census-owner role. C-41 requires the two-party role structure; V-R15-C identifies the next escalation: the gate token itself should carry named audit-trace fields — `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:` — so that the two-party exchange is auditable from the emitted token without re-inspecting the instruction trace, and the gate boundary can be closed only when both named fields carry non-null values → **C-44**

---

## Group A — Structural Foundations (C-08–C-19) · 12 criteria

| Criterion | Description |
|-----------|-------------|
| C-08 | Contract scope has 4 required elements |
| C-09 | Input fixture inline — no external refs |
| C-10 | Spec source cited with section |
| C-11 | Expected output covers success path |
| C-12 | Expected output covers error path |
| C-13 | Expected output covers ≥1 edge case |
| C-14 | Every element has value constraint + clause |
| C-15 | EXPECTED-SEALED token format correct |
| C-16 | Actual output: status + body present |
| C-17 | Diff accounts for every Expected element |
| C-18 | Diff uses ✓ / F-NN symbols correctly |
| C-19 | No silent omissions in Diff |

*Group A max: 48*

---

## Group B — Findings Quality (C-20–C-25) · 6 criteria

| Criterion | Description |
|-----------|-------------|
| C-20 | Finding format: all 5 fields present |
| C-21 | Severity constrained to 3 vocabulary values |
| C-22 | Mechanism-type constrained to taxonomy tokens |
| C-23 | Root-cause names component/path — not symptom |
| C-24 | Hypothesis self-test applied |
| C-25 | FINDINGS-COMPLETE token format correct |

*Group B max: 24*

---

## Group C — Census and Propagation (C-26–C-35) · 10 criteria

| Criterion | Description |
|-----------|-------------|
| C-26 | Sub-task A: mechanism-distribution line emitted |
| C-27 | Sub-task A: sole production site rule respected |
| C-28 | Sub-task B: staging lines present per candidate group |
| C-29 | mechanism-type-shared = single token or `mixed` |
| C-30 | Rationale names shared mechanism — not token |
| C-31 | Pattern fill consumes staging lines — not re-derived |
| C-32 | mechanism-type-shared at fill site = staging-line value |
| C-33 | Staging line + fill site consistency enforced |
| C-34 | Branch selection matches finding count |
| C-35 | TAXONOMY-CENSUS-COMPLETE token format correct |

*Group C max: 40*

---

## Group D — Gate Token and Provenance (C-36–C-38) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-36 | Gate token emitted at S6.5 |
| C-37 | gate-provenance present with named source `S5.5-Sub-task-A` |
| C-38 | Gate token not patched at fill site — amendment goes to staging |

*Group D max: 12*

---

## Group E — Schema and Formal Imperative (C-39–C-41) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-39 | `census-distribution` and `gate-provenance` declared as co-required sibling fields in named `GateTokenSchema`; detectable by field inspection without prose |
| C-40 | All copy-forward and amendment-path obligations stated as `Bind:` / `Assert:` / `Prohibit:` commands — auditable by structural inspection |
| C-41 | Gate execution protocol assigns attestation to census owner by role name; assigns independent char-for-char verification to distinct witness role; no single role satisfies both |

*Group E max: 12*

---

## Group F — New Criteria R16 (C-42–C-44) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-42 | Each field in `GateTokenSchema` `required-fields:` manifest carries an explicit type constraint (`string`, `enum[...]`, `format: S-section-reference`); field-inspection validates value conformance as well as field presence without reading prose |
| C-43 | All `Bind:` / `Assert:` / `Prohibit:` obligations grouped under a named, addressable `ObligationBlock:` that is cross-referenced by name from Sub-task A, Sub-task B, and S6.5 — amendment-path consistency enforceable by reference inspection, not prose audit |
| C-44 | Gate token carries named audit-trace fields `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:`; gate boundary closes only when both named fields carry non-null values; two-party exchange auditable from token without re-inspecting instruction trace |

*Group F max: 12*

---

## Scoring Summary

| Group | Criteria | Max |
|-------|----------|-----|
| A — Structural Foundations | C-08–C-19 | 48 |
| B — Findings Quality | C-20–C-25 | 24 |
| C — Census and Propagation | C-26–C-35 | 40 |
| D — Gate Token and Provenance | C-36–C-38 | 12 |
| E — Schema and Formal Imperative | C-39–C-41 | 12 |
| F — Audit Trace and Addressability | C-42–C-44 | 12 |
| **Total** | **37 criteria** | **148** |
