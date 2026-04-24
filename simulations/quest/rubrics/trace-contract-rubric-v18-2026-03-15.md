Reading the R17 scorecard, three synthesis patterns emerge:

- **V-R17-A**: `[FINDINGS-COMPLETE]` as count-bearing closure seal — C-25 is PARTIAL for all variations because no variation emits the token; all move directly from the last finding block to Sub-task A. The best variations (V-02, V-04, V-05) demonstrate structural sealing elsewhere — `[TAXONOMY-DECLARED]`, `SCHEMA-DIFF-COMPLETE` — but do not apply the pattern to findings closure. C-25 requires the token; V-R17-A identifies the next escalation: the `[FINDINGS-COMPLETE]` token should carry a count assertion — `[FINDINGS-COMPLETE count=N findings]` — so that the findings-section closure is self-verifying: an inspector can confirm N finding blocks exist without re-scanning the section, making findings completeness auditable by count verification alone and making an off-by-one omission detectable at the closure token without re-entering the finding blocks → **C-48**

- **V-R17-B**: Taxonomy amendment protocol as a named governance constraint — V-02 introduces an amendment protocol alongside `closed: true`: new tokens require taxonomy-block update before first use, enforced by the `[TAXONOMY-DECLARED]` seal. V-04 and V-05 pass C-46 with `closed: true` and a `TAXONOMY-DECLARED` token but without a named amendment protocol. C-46 requires the closed enumerated taxonomy; V-R17-B identifies the next escalation: the taxonomy declaration should carry a named `AmendmentProtocol:` field — `AmendmentProtocol: new tokens require taxonomy-block amendment before first use` — so that taxonomy extension cannot occur by silent addition to the finding template without updating the declaration, converting the `closed` flag from an assertion into an enforceable governance contract whose violation is detectable by comparing the declared set against the tokens in use → **C-49**

- **V-R17-C**: Schema-sweep omission rejection as a named structural failure criterion — The C-19 evidence note records that V-01 additionally requires every `GateTokenSchema` row to receive a schema-sweep entry with an explicit omission rule; this strengthens C-19 at the schema level while all other variations satisfy C-19 through a general "no silent omissions" instruction that does not differentiate schema-level omission from element-diff omission. V-R17-C identifies the next escalation: the Schema Diff phase (C-45) should carry a named omission-rejection rule stated as a structural criterion — `OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result` — so that schema completeness is governed by a named failure mode detectable by row-count comparison alone, rather than a prose completeness admonition that requires reading the sweep output to verify → **C-50**

---

# Rubric: trace-contract v18

Reading the R15 scorecard, three synthesis patterns emerged (carried forward from v16):

- **V-R15-A**: GateTokenSchema field-type completeness — V-01, V-04, and V-05 passed C-39 by declaring a named `GateTokenSchema` with a `required-fields:` manifest and `co-requirement:` annotation. V-05 enumerated `gate-status` as a third required field alongside `census-distribution` and `gate-provenance`. V-02 and V-03 PARTIAL because co-requirement was implied by field adjacency or prose description rather than enforced by a named schema structure. C-39 requires the schema and co-requirement declaration; V-R15-A identified the next escalation: each field in the `required-fields:` manifest should carry an explicit type constraint (`string`, `enum[PASS|FAIL]`, `format: S-section-reference`), converting the schema from a field-existence check into a full structural contract whose violations are detectable by value inspection alone → **C-42**

- **V-R15-B**: Named obligation block as addressable reference unit — V-02, V-04, and V-05 passed C-40 by emitting a complete `Bind:` / `Assert:` / `Prohibit:` chain covering all copy-forward and amendment-path obligations. V-01 PARTIAL because amendment-path obligations at Sub-task B remained in descriptive prose. V-03 PARTIAL because `Prohibit:` was absent and the amendment-path obligation used a weaker prose form. C-40 requires the full formal-imperative chain; V-R15-B identified the next escalation: the complete obligation chain should be declared as a named, addressable block — `ObligationBlock: census-gate-obligations` — cross-referenced from Sub-task A, Sub-task B, and S6.5 without restating the imperatives at each site, so amendment-path consistency is enforceable by reference inspection rather than by auditing prose repetition → **C-43**

- **V-R15-C**: Audit-trace fields encoding two-party execution in the gate token — V-03 and V-05 passed C-41 by assigning attestation to the census owner by explicit role name and assigning independent char-for-char verification to a distinct witness role. V-05 additionally stated the negative constraint: no single role can silently satisfy both claim and proof. V-01 PARTIAL because both steps shared a single S6.5 block without role-name separation. V-02 and V-04 PARTIAL because attestation was not assigned to a named census-owner role. C-41 requires the two-party role structure; V-R15-C identified the next escalation: the gate token itself should carry named audit-trace fields — `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:` — so the two-party exchange is auditable from the emitted token without re-inspecting the instruction trace, and the gate boundary can be closed only when both named fields carry non-null values → **C-44**

---

Reading the R16 scorecard, three synthesis patterns emerged (carried forward from v17):

- **V-R16-A**: Schema Diff as an ordered phase with a phase-completion token — V-01 introduces a dedicated Schema Diff phase (Step 5) that performs a systematic per-field sweep over every `GateTokenSchema` row before the element diff begins, closing the C-19 omission gap. Other variations carry forward their R15 PASS baseline but do not separate the schema sweep from the element comparison as a structurally distinct phase. C-45 requires only that the Schema Diff phase exist; V-R16-A identified the next escalation: the Schema Diff phase should emit a named phase-completion token — `SCHEMA-DIFF-COMPLETE` — before the element diff begins, so that phase ordering is structurally enforced and a schema violation found late in the element diff is traceable to a missing or incomplete Schema Diff phase rather than to an omission in the element sweep, making schema-validation coverage auditable independently of element-diff coverage → **C-45**

- **V-R16-B**: `type-violation` registered as a closed-taxonomy token — R16 introduces `type-violation` as an explicit mechanism-type token with a dedicated Schema Diff detection path, creating a structured detection-to-hypothesis path that separates symptom from root cause. C-22 requires mechanism-type constrained to taxonomy tokens; V-R16-B identified the next escalation: the mechanism-type taxonomy should be declared inline as a closed enumerated set — `MechanismTypeTaxonomy: { missing-field | wrong-value | type-violation | co-requirement-violated | ... }` — so that C-22 conformance is verifiable by reference to the inline declaration without consulting external documentation, and new tokens cannot be introduced without amending the declared taxonomy, converting the vocabulary constraint from an honor-system check into a structural contract → **C-46**

- **V-R16-C**: Re-derivation prohibition elevated into the named ObligationBlock — R16 adds the explicit instruction: "The `mechanism-type-shared` value at this fill site must equal the value derived from the staging line. Do not re-derive it from the findings." All variations carry this instruction as natural-language step text. V-R16-C identified the next escalation: the prohibition should be stated as a `Prohibit:` command within the named `ObligationBlock` (C-43), so that the fill-site re-derivation constraint is part of the addressable obligation chain and machine-inspectable alongside copy-forward and amendment-path obligations, rather than embedded in natural-language step instructions that require prose auditing to verify → **C-47**

---

Reading the R17 scorecard, three synthesis patterns emerge:

- **V-R17-A**: `[FINDINGS-COMPLETE]` as count-bearing closure seal — C-25 is PARTIAL for all variations because no variation emits the token; all move directly from the last finding block to Sub-task A. The best variations (V-02, V-04, V-05) demonstrate structural sealing elsewhere — `[TAXONOMY-DECLARED]`, `SCHEMA-DIFF-COMPLETE` — but do not apply the pattern to findings closure. C-25 requires the token; V-R17-A identifies the next escalation: the `[FINDINGS-COMPLETE]` token should carry a count assertion — `[FINDINGS-COMPLETE count=N findings]` — so that the findings-section closure is self-verifying: an inspector can confirm N finding blocks exist without re-scanning the section, making findings completeness auditable by count verification alone and making an off-by-one omission detectable at the closure token without re-entering the finding blocks → **C-48**

- **V-R17-B**: Taxonomy amendment protocol as a named governance constraint — V-02 introduces an amendment protocol alongside `closed: true`: new tokens require taxonomy-block update before first use, enforced by the `[TAXONOMY-DECLARED]` seal. V-04 and V-05 pass C-46 with `closed: true` and a `TAXONOMY-DECLARED` token but without a named amendment protocol. C-46 requires the closed enumerated taxonomy; V-R17-B identifies the next escalation: the taxonomy declaration should carry a named `AmendmentProtocol:` field — `AmendmentProtocol: new tokens require taxonomy-block amendment before first use` — so that taxonomy extension cannot occur by silent addition to the finding template without updating the declaration, converting the `closed` flag from an assertion into an enforceable governance contract whose violation is detectable by comparing the declared set against the tokens in use → **C-49**

- **V-R17-C**: Schema-sweep omission rejection as a named structural failure criterion — The C-19 evidence note records that V-01 additionally requires every `GateTokenSchema` row to receive a schema-sweep entry with an explicit omission rule, while all other variations satisfy C-19 through a general "no silent omissions" instruction that does not differentiate schema-level omission from element-diff omission. V-R17-C identifies the next escalation: the Schema Diff phase (C-45) should carry a named omission-rejection rule stated as a structural criterion — `OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result` — so that schema completeness is governed by a named failure mode detectable by row-count comparison alone, rather than a prose completeness admonition that requires reading the sweep output to verify → **C-50**

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

*C-34–C-38 carried PASS baseline (not distinguishing); Group C scored on C-26–C-33.*

*Group C max (scored): 32*

---

## Extended Criteria — Schema, Obligation, Audit, Taxonomy, Closure (C-39–C-50) · 12 criteria

| Criterion | Description |
|-----------|-------------|
| C-39 | GateTokenSchema field-type completeness |
| C-40 | Named ObligationBlock |
| C-41 | Two-party audit trace in gate token |
| C-42 | Typed-column constraint per field |
| C-43 | ObligationBlock as named addressable block |
| C-44 | Gate token audit-trace fields named |
| C-45 | Schema Diff phase emits `SCHEMA-DIFF-COMPLETE` token before element diff begins |
| C-46 | MechanismTypeTaxonomy declared inline as closed enumerated set with `[TAXONOMY-DECLARED]` seal |
| C-47 | Re-derivation prohibition stated as `Prohibit:` command within named ObligationBlock |
| C-48 | `[FINDINGS-COMPLETE count=N findings]` token emitted as count-bearing closure seal at end of findings section |
| C-49 | Taxonomy declaration carries named `AmendmentProtocol:` field governing extension before first use |
| C-50 | Schema Diff phase carries named `OmissionRule:` declaring absent GateTokenSchema rows as automatic SCHEMA-PHASE-FAIL |

*Extended Criteria max: 48*

---

*Total assessable max: 48 (A) + 24 (B) + 32 (C) + 48 (Extended) = 152*
