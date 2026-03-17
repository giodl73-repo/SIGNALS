Reading the R16 scorecard, three synthesis patterns emerge:

- **V-R16-A**: Schema Diff as an ordered phase with a phase-completion token — V-01 introduces a dedicated Schema Diff phase (Step 5) that performs a systematic per-field sweep over every `GateTokenSchema` row before the element diff begins, closing the C-19 omission gap. Other variations carry forward their R15 PASS baseline but do not separate the schema sweep from the element comparison as a structurally distinct phase. C-45 requires only that the Schema Diff phase exist; V-R16-A identifies the next escalation: the Schema Diff phase should emit a named phase-completion token — `SCHEMA-DIFF-COMPLETE` — before the element diff begins, so that phase ordering is structurally enforced and a schema violation found late in the element diff is traceable to a missing or incomplete Schema Diff phase rather than to an omission in the element sweep, making schema-validation coverage auditable independently of element-diff coverage → **C-45**

- **V-R16-B**: `type-violation` registered as a closed-taxonomy token — the C-23 evidence note records that R16 introduces `type-violation` as an explicit mechanism-type token with a dedicated Schema Diff detection path, creating a structured detection-to-hypothesis path that separates symptom (wrong value observed) from root cause (type constraint violated at a named field). C-22 requires mechanism-type constrained to taxonomy tokens; V-R16-B identifies the next escalation: the mechanism-type taxonomy should be declared inline as a closed enumerated set — `MechanismTypeTaxonomy: { missing-field | wrong-value | type-violation | co-requirement-violated | ... }` — so that C-22 conformance is verifiable by reference to the inline declaration without consulting external documentation, and new tokens cannot be introduced without amending the declared taxonomy, converting the vocabulary constraint from an honor-system check into a structural contract → **C-46**

- **V-R16-C**: Re-derivation prohibition elevated into the named ObligationBlock — the C-33 evidence note records that R16 adds an explicit instruction: "The `mechanism-type-shared` value at this fill site must equal the value derived from the staging line. Do not re-derive it from the findings." All variations carry this instruction; the PASS variations state it as an imperative instruction in natural-language step text. V-R16-C identifies the next escalation: the prohibition should be stated as a `Prohibit:` command within the named `ObligationBlock` (C-43), so that the fill-site re-derivation constraint is part of the addressable obligation chain and machine-inspectable alongside copy-forward and amendment-path obligations, rather than embedded in natural-language step instructions that require prose auditing to verify → **C-47**

---

# Rubric: trace-contract v17

Reading the R15 scorecard, three synthesis patterns emerged (carried forward from v16):

- **V-R15-A**: GateTokenSchema field-type completeness — V-01, V-04, and V-05 passed C-39 by declaring a named `GateTokenSchema` with a `required-fields:` manifest and `co-requirement:` annotation. V-05 enumerated `gate-status` as a third required field alongside `census-distribution` and `gate-provenance`. V-02 and V-03 PARTIAL because co-requirement was implied by field adjacency or prose description rather than enforced by a named schema structure. C-39 requires the schema and co-requirement declaration; V-R15-A identified the next escalation: each field in the `required-fields:` manifest should carry an explicit type constraint (`string`, `enum[PASS|FAIL]`, `format: S-section-reference`), converting the schema from a field-existence check into a full structural contract whose violations are detectable by value inspection alone → **C-42**

- **V-R15-B**: Named obligation block as addressable reference unit — V-02, V-04, and V-05 passed C-40 by emitting a complete `Bind:` / `Assert:` / `Prohibit:` chain covering all copy-forward and amendment-path obligations. V-01 PARTIAL because amendment-path obligations at Sub-task B remained in descriptive prose. V-03 PARTIAL because `Prohibit:` was absent and the amendment-path obligation used a weaker prose form. C-40 requires the full formal-imperative chain; V-R15-B identified the next escalation: the complete obligation chain should be declared as a named, addressable block — `ObligationBlock: census-gate-obligations` — cross-referenced from Sub-task A, Sub-task B, and S6.5 without restating the imperatives at each site, so amendment-path consistency is enforceable by reference inspection rather than by auditing prose repetition → **C-43**

- **V-R15-C**: Audit-trace fields encoding two-party execution in the gate token — V-03 and V-05 passed C-41 by assigning attestation to the census owner by explicit role name and assigning independent char-for-char verification to a distinct witness role. V-05 additionally stated the negative constraint: no single role can silently satisfy both claim and proof. V-01 PARTIAL because both steps shared a single S6.5 block without role-name separation. V-02 and V-04 PARTIAL because attestation was not assigned to a named census-owner role. C-41 requires the two-party role structure; V-R15-C identified the next escalation: the gate token itself should carry named audit-trace fields — `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:` — so the two-party exchange is auditable from the emitted token without re-inspecting the instruction trace, and the gate boundary can be closed only when both named fields carry non-null values → **C-44**

---

Reading the R16 scorecard, three synthesis patterns emerge:

- **V-R16-A**: Schema Diff as an ordered phase with a phase-completion token — V-01 introduces a dedicated Schema Diff phase (Step 5) that performs a systematic per-field sweep over every `GateTokenSchema` row before the element diff begins, closing the C-19 omission gap. Other variations carry forward their R15 PASS baseline but do not separate the schema sweep from the element comparison as a structurally distinct phase. V-R16-A identifies the next escalation: the Schema Diff phase should emit a named phase-completion token — `SCHEMA-DIFF-COMPLETE` — before the element diff begins, so that phase ordering is structurally enforced and a schema violation found late in the element diff is traceable to a missing or incomplete Schema Diff phase rather than to an omission in the element sweep, making schema-validation coverage auditable independently of element-diff coverage → **C-45**

- **V-R16-B**: `type-violation` registered as a closed-taxonomy token — R16 introduces `type-violation` as an explicit mechanism-type token with a dedicated Schema Diff detection path, creating a structured detection-to-hypothesis path that separates symptom from root cause. C-22 requires mechanism-type constrained to taxonomy tokens; V-R16-B identifies the next escalation: the mechanism-type taxonomy should be declared inline as a closed enumerated set — `MechanismTypeTaxonomy: { missing-field | wrong-value | type-violation | co-requirement-violated | ... }` — so that C-22 conformance is verifiable by reference to the inline declaration without consulting external documentation, and new tokens cannot be introduced without amending the declared taxonomy, converting the vocabulary constraint from an honor-system check into a structural contract → **C-46**

- **V-R16-C**: Re-derivation prohibition elevated into the named ObligationBlock — R16 adds the explicit instruction: "The `mechanism-type-shared` value at this fill site must equal the value derived from the staging line. Do not re-derive it from the findings." All variations carry this instruction as natural-language step text. V-R16-C identifies the next escalation: the prohibition should be stated as a `Prohibit:` command within the named `ObligationBlock` (C-43), so that the fill-site re-derivation constraint is part of the addressable obligation chain and machine-inspectable alongside copy-forward and amendment-path obligations, rather than embedded in natural-language step instructions that require prose auditing to verify → **C-47**

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

## Group E — Criteria R15 (C-39–C-41) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-39 | `census-distribution` and `gate-provenance` declared as co-required sibling fields in named `GateTokenSchema`; detectable by field inspection without prose |
| C-40 | All copy-forward and amendment-path obligations stated as `Bind:` / `Assert:` / `Prohibit:` commands — auditable by structural inspection |
| C-41 | Gate execution protocol assigns attestation to census owner by role name; assigns independent char-for-char verification to distinct witness role; no single role satisfies both |

*Group E max: 12*

---

## Group F — Criteria R16 (C-42–C-44) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-42 | Each field in `GateTokenSchema` `required-fields:` manifest carries an explicit type constraint (`string`, `enum[PASS\|FAIL]`, `format: S-section-reference`); schema validates value conformance not just field presence — violations detectable by value inspection alone |
| C-43 | Complete obligation chain declared as named addressable block — `ObligationBlock: census-gate-obligations` — cross-referenced from Sub-task A, Sub-task B, and S6.5 without restating imperatives at each site; amendment-path consistency enforceable by reference inspection |
| C-44 | Gate token carries named audit-trace fields — `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:` — two-party exchange auditable from emitted token without re-inspecting instruction trace; gate boundary closable only when both named fields carry non-null values |

*Group F max: 12*

---

## Group G — Criteria R17 (C-45–C-47) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-45 | Schema Diff phase emits named phase-completion token — `SCHEMA-DIFF-COMPLETE` — before element diff begins; phase ordering structurally enforced so schema violations cannot be masked by element-level pass results; schema-validation coverage auditable independently of element-diff coverage |
| C-46 | Mechanism-type taxonomy declared inline as closed enumerated set — `MechanismTypeTaxonomy:` block — so C-22 conformance is verifiable by reference to the inline declaration without consulting external documentation; new tokens require amending the declared taxonomy |
| C-47 | Re-derivation prohibition at fill site stated as `Prohibit:` command within the named `ObligationBlock` (C-43); fill-site constraint machine-inspectable as part of the obligation chain alongside copy-forward and amendment-path obligations — not embedded in natural-language step instructions |

*Group G max: 12*

---

**Rubric v17 total max: 160** (C-08–C-47 · 40 criteria)
