Reading the R19 scorecard, three synthesis patterns emerge:

- **V-R19-A**: `findings-sealed:` field enforced as verbatim copy by a named rule — V-01 passes C-51 by emitting `findings-sealed: [FINDINGS-COMPLETE count=N findings]` in the summary AND attaching a verbatim-copy enforcement rule. C-51 requires only the named echo field; V-R19-A identifies the next escalation: the echo field should be governed by an explicit `VerbatimRule:` constraint — `VerbatimRule: findings-sealed value must be copied character-for-character from the [FINDINGS-COMPLETE] token; reformulation constitutes a summary-integrity violation` — so that correctness of the echo is verifiable by string comparison alone without semantic interpretation, and a paraphrased or count-adjusted echo is detectable as a structural violation rather than a plausible alternative rendering → **C-54**

- **V-R19-B**: `taxonomy-version:` summary field echoing the versioned seal — V-02 passes C-52 by encoding `[TAXONOMY-DECLARED version=N]` and also emits `taxonomy-version: [TAXONOMY-DECLARED version=N]` as a named summary field. C-52 requires the version counter inside the seal token; V-R19-B identifies the next escalation: the summary section should carry a named `taxonomy-version:` field that echoes the versioned seal, parallel to `findings-sealed:` (C-51), so that taxonomy version is auditable from the summary without locating the taxonomy block within the instruction body — making both the findings count and the taxonomy version verifiable from a single structural anchor point → **C-55**

- **V-R19-C**: Named `remediation:` field per failure token in the `FailureToken:` block — V-03 passes C-53 by declaring `SCHEMA-PHASE-FAIL` and `SCHEMA-OMISSION-FAIL` as distinct tokens AND specifying distinct remediation paths for each within the block. C-53 requires only that the two tokens be nominally distinct; V-R19-C identifies the next escalation: each entry in the `FailureToken:` block should carry a named `remediation:` field — e.g., `remediation: correct field type and re-sweep` vs `remediation: add absent row and re-sweep` — so that the required remediation is derivable from the emitted token alone without reading the failure rationale text, making schema failure response machine-actionable from the token and preventing a shared remediation path from collapsing the two failure modes back into a single category → **C-56**

---

```markdown
# Rubric: trace-contract v20

Reading the R15 scorecard, three synthesis patterns emerged (carried forward from v16):

- **V-R15-A**: GateTokenSchema field-type completeness — V-01, V-04, and V-05 passed C-39 by
  declaring a named `GateTokenSchema` with a `required-fields:` manifest and `co-requirement:`
  annotation. V-05 enumerated `gate-status` as a third required field alongside
  `census-distribution` and `gate-provenance`. V-02 and V-03 PARTIAL because co-requirement was
  implied by field adjacency or prose description rather than enforced by a named schema structure.
  C-39 requires the schema and co-requirement declaration; V-R15-A identified the next escalation:
  each field in the `required-fields:` manifest should carry an explicit type constraint (`string`,
  `enum[PASS|FAIL]`, `format: S-section-reference`), converting the schema from a field-existence
  check into a full structural contract whose violations are detectable by value inspection alone
  → **C-42**

- **V-R15-B**: Named obligation block as addressable reference unit — V-02, V-04, and V-05 passed
  C-40 by emitting a complete `Bind:` / `Assert:` / `Prohibit:` chain covering all copy-forward and
  amendment-path obligations. V-01 PARTIAL because amendment-path obligations at Sub-task B
  remained in descriptive prose. V-03 PARTIAL because `Prohibit:` was absent and the
  amendment-path obligation used a weaker prose form. C-40 requires the full formal-imperative
  chain; V-R15-B identified the next escalation: the complete obligation chain should be declared as
  a named, addressable block — `ObligationBlock: census-gate-obligations` — cross-referenced from
  Sub-task A, Sub-task B, and S6.5 without restating the imperatives at each site, so
  amendment-path consistency is enforceable by reference inspection rather than by auditing prose
  repetition → **C-43**

- **V-R15-C**: Audit-trace fields encoding two-party execution in the gate token — V-03 and V-05
  passed C-41 by assigning attestation to the census owner by explicit role name and assigning
  independent char-for-char verification to a distinct witness role. V-05 additionally stated the
  negative constraint: no single role can silently satisfy both claim and proof. V-01 PARTIAL
  because both steps shared a single S6.5 block without role-name separation. V-02 and V-04
  PARTIAL because attestation was not assigned to a named census-owner role. C-41 requires the
  two-party role structure; V-R15-C identified the next escalation: the gate token itself should
  carry named audit-trace fields — `attestation-by:`, `attestation-result:`, `verification-by:`,
  `verification-result:` — so the two-party exchange is auditable from the emitted token without
  re-inspecting the instruction trace, and the gate boundary can be closed only when both named
  fields carry non-null values → **C-44**

---

Reading the R16 scorecard, three synthesis patterns emerged (carried forward from v17):

- **V-R16-A**: Schema Diff as an ordered phase with a phase-completion token — V-01 introduces a
  dedicated Schema Diff phase (Step 5) that performs a systematic per-field sweep over every
  `GateTokenSchema` row before the element diff begins, closing the C-19 omission gap. Other
  variations carry forward their R15 PASS baseline but do not separate the schema sweep from the
  element comparison as a structurally distinct phase. C-45 requires only that the Schema Diff
  phase exist; V-R16-A identified the next escalation: the Schema Diff phase should emit a named
  phase-completion token — `SCHEMA-DIFF-COMPLETE` — before the element diff begins, so that phase
  ordering is structurally enforced and a schema violation found late in the element diff is
  traceable to a missing or incomplete Schema Diff phase rather than to an omission in the element
  sweep, making schema-validation coverage auditable independently of element-diff coverage
  → **C-45**

- **V-R16-B**: `type-violation` registered as a closed-taxonomy token — R16 introduces
  `type-violation` as an explicit mechanism-type token with a dedicated Schema Diff detection path,
  creating a structured detection-to-hypothesis path that separates symptom from root cause. C-22
  requires mechanism-type constrained to taxonomy tokens; V-R16-B identified the next escalation:
  the mechanism-type taxonomy should be declared inline as a closed enumerated set —
  `MechanismTypeTaxonomy: { missing-field | wrong-value | type-violation | co-requirement-violated
  | ... }` — so that C-22 conformance is verifiable by reference to the inline declaration without
  consulting external documentation, and new tokens cannot be introduced without amending the
  declared taxonomy, converting the vocabulary constraint from an honor-system check into a
  structural contract → **C-46**

- **V-R16-C**: Re-derivation prohibition elevated into the named ObligationBlock — R16 adds the
  explicit instruction: "The `mechanism-type-shared` value at this fill site must equal the value
  derived from the staging line. Do not re-derive it from the findings." All variations carry this
  instruction as natural-language step text. V-R16-C identified the next escalation: the
  prohibition should be stated as a `Prohibit:` command within the named `ObligationBlock` (C-43),
  so that the fill-site re-derivation constraint is part of the addressable obligation chain and
  machine-inspectable alongside copy-forward and amendment-path obligations, rather than embedded
  in natural-language step instructions that require prose auditing to verify → **C-47**

---

Reading the R17 scorecard, three synthesis patterns emerged (carried forward from v18):

- **V-R17-A**: `[FINDINGS-COMPLETE]` as count-bearing closure seal — C-25 is PARTIAL for all
  variations because no variation emits the token; all move directly from the last finding block to
  Sub-task A. The best variations (V-02, V-04, V-05) demonstrate structural sealing elsewhere —
  `[TAXONOMY-DECLARED]`, `SCHEMA-DIFF-COMPLETE` — but do not apply the pattern to findings
  closure. C-25 requires the token; V-R17-A identifies the next escalation: the
  `[FINDINGS-COMPLETE]` token should carry a count assertion — `[FINDINGS-COMPLETE count=N
  findings]` — so that the findings-section closure is self-verifying: an inspector can confirm N
  finding blocks exist without re-scanning the section, making findings completeness auditable by
  count verification alone and making an off-by-one omission detectable at the closure token
  without re-entering the finding blocks → **C-48**

- **V-R17-B**: Taxonomy amendment protocol as a named governance constraint — V-02 introduces an
  amendment protocol alongside `closed: true`: new tokens require taxonomy-block update before
  first use, enforced by the `[TAXONOMY-DECLARED]` seal. V-04 and V-05 pass C-46 with `closed:
  true` and a `TAXONOMY-DECLARED` token but without a named amendment protocol. C-46 requires the
  closed enumerated taxonomy; V-R17-B identifies the next escalation: the taxonomy declaration
  should carry a named `AmendmentProtocol:` field — `AmendmentProtocol: new tokens require
  taxonomy-block amendment before first use` — so that taxonomy extension cannot occur by silent
  addition to the finding template without updating the declaration, converting the `closed` flag
  from an assertion into an enforceable governance contract whose violation is detectable by
  comparing the declared set against the tokens in use → **C-49**

- **V-R17-C**: Schema-sweep omission rejection as a named structural failure criterion — The C-19
  evidence note records that V-01 additionally requires every `GateTokenSchema` row to receive a
  schema-sweep entry with an explicit omission rule; this strengthens C-19 at the schema level
  while all other variations satisfy C-19 through a general "no silent omissions" instruction that
  does not differentiate schema-level omission from element-diff omission. V-R17-C identifies the
  next escalation: the Schema Diff phase (C-45) should carry a named omission-rejection rule stated
  as a structural criterion — `OmissionRule: any GateTokenSchema row absent from schema-sweep
  output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result` — so
  that schema completeness is governed by a named failure mode detectable by row-count comparison
  alone, rather than a prose completeness admonition that requires reading the sweep output to
  verify → **C-50**

---

Reading the R18 scorecard, three synthesis patterns emerged (carried forward from v19):

- **V-R18-A**: Count-bearing seal echoed in summary section as a named field — V-01 emits
  `[FINDINGS-COMPLETE count=N findings]` at the findings boundary AND echoes it in the summary
  section as `findings-sealed: [FINDINGS-COMPLETE count=N findings]`. C-48 requires only the count
  at the boundary token; V-R18-A identifies the next escalation: the summary section should carry a
  named `findings-sealed:` field that mirrors the `[FINDINGS-COMPLETE count=N findings]` boundary
  token, so that count-assertion verification is available at either the findings boundary or the
  summary section without cross-referencing both locations, and a summary-level audit does not
  require locating the findings boundary within the instruction body — making findings completeness
  verifiable from any structural anchor point → **C-51**

- **V-R18-B**: `[TAXONOMY-DECLARED]` seal carrying a version counter — C-49 requires
  `AmendmentProtocol:` as a named governance field; the excellence signal is an additional
  `AmendmentVersion:` counter on the taxonomy block so that each amendment increments the declared
  version, expressed as `[TAXONOMY-DECLARED version=N]` at the seal, making amendment count
  verifiable by counter inspection alone and enabling version-skew detection when a taxonomy block
  is copied forward without updating the counter — converting amendment governance from a protocol
  obligation into a numeric invariant whose violation surfaces as a counter mismatch without reading
  the amendment protocol text → **C-52**

- **V-R18-C**: Schema-omission failure mode distinguished from schema-phase failure by a named
  token — C-50 requires `OmissionRule:` naming `SCHEMA-PHASE-FAIL` as the failure token; the
  excellence signal is a distinct `FailureToken: SCHEMA-OMISSION-FAIL` reserved exclusively for
  row-absent failures, so that row-missing failures are distinguishable from type-violation failures
  by token comparison alone, allowing an automated inspector to categorize schema failures without
  reading the failure rationale text, and preventing a type-violation finding from masking a
  co-occurring omission that would produce a different remediation path → **C-53**

---

Reading the R19 scorecard, three synthesis patterns emerge:

- **V-R19-A**: `findings-sealed:` field enforced as verbatim copy by a named rule — V-01 passes
  C-51 by emitting `findings-sealed: [FINDINGS-COMPLETE count=N findings]` in the summary AND
  attaching a verbatim-copy enforcement rule. C-51 requires only the named echo field; V-R19-A
  identifies the next escalation: the echo field should be governed by an explicit `VerbatimRule:`
  constraint — `VerbatimRule: findings-sealed value must be copied character-for-character from the
  [FINDINGS-COMPLETE] token; reformulation constitutes a summary-integrity violation` — so that
  correctness of the echo is verifiable by string comparison alone without semantic interpretation,
  and a paraphrased or count-adjusted echo is detectable as a structural violation rather than a
  plausible alternative rendering → **C-54**

- **V-R19-B**: `taxonomy-version:` summary field echoing the versioned seal — V-02 passes C-52 by
  encoding `[TAXONOMY-DECLARED version=N]` and also emits `taxonomy-version: [TAXONOMY-DECLARED
  version=N]` as a named summary field. C-52 requires the version counter inside the seal token;
  V-R19-B identifies the next escalation: the summary section should carry a named
  `taxonomy-version:` field that echoes the versioned seal, parallel to `findings-sealed:` (C-51),
  so that taxonomy version is auditable from the summary without locating the taxonomy block within
  the instruction body — making both the findings count and the taxonomy version verifiable from a
  single structural anchor point → **C-55**

- **V-R19-C**: Named `remediation:` field per failure token in the `FailureToken:` block — V-03
  passes C-53 by declaring `SCHEMA-PHASE-FAIL` and `SCHEMA-OMISSION-FAIL` as distinct tokens AND
  specifying distinct remediation paths for each within the block. C-53 requires only that the two
  tokens be nominally distinct; V-R19-C identifies the next escalation: each entry in the
  `FailureToken:` block should carry a named `remediation:` field — e.g., `remediation: correct
  field type and re-sweep` vs `remediation: add absent row and re-sweep` — so that the required
  remediation is derivable from the emitted token alone without reading the failure rationale text,
  making schema failure response machine-actionable from the token and preventing a shared
  remediation path from collapsing the two failure modes back into a single category → **C-56**

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
| C-23 | Hypothesis names causal mechanism |
| C-24 | Remediation is actionable |
| C-25 | [FINDINGS-COMPLETE] token present |

*Group B max: 24*

---

## Group C — Gate Token Structure (C-26–C-32) · 7 criteria

| Criterion | Description |
|-----------|-------------|
| C-26 | Gate token has gate-id field |
| C-27 | Gate token has gate-status field |
| C-28 | Gate token has gate-provenance field |
| C-29 | Gate token has census-distribution field |
| C-30 | Gate token format matches GateTokenSchema |
| C-31 | Gate token emitted at correct phase boundary |
| C-32 | Gate token not emitted without EXPECTED-SEALED |

*Group C max: 28*

---

## Group D — Schema and Diff Completeness (C-33–C-38) · 6 criteria

| Criterion | Description |
|-----------|-------------|
| C-33 | GateTokenSchema declared before Expected |
| C-34 | Schema covers all gate token fields |
| C-35 | Schema required-fields manifest present |
| C-36 | Diff covers schema fields before element diff |
| C-37 | No schema field omitted from diff |
| C-38 | Schema diff result referenced in gate token |

*Group D max: 24*

---

## Group E — Advanced Schema Governance (C-39–C-47) · 9 criteria

| Criterion | Description |
|-----------|-------------|
| C-39 | GateTokenSchema with named co-requirement annotation |
| C-40 | Full Bind / Assert / Prohibit obligation chain |
| C-41 | Two-party audit-trace roles (attestation + verification) |
| C-42 | Type constraint per field in GateTokenSchema |
| C-43 | Named ObligationBlock as addressable reference unit |
| C-44 | Audit-trace fields (attestation-by / verification-by / results) in gate token |
| C-45 | SCHEMA-DIFF-COMPLETE phase-completion token emitted |
| C-46 | Mechanism-type taxonomy declared as closed enumerated set |
| C-47 | Re-derive prohibition stated as Prohibit: in named ObligationBlock |

*Group E max: 36*

---

## Group F — Seal Integrity and Failure Governance (C-48–C-53) · 6 criteria

| Criterion | Description |
|-----------|-------------|
| C-48 | [FINDINGS-COMPLETE count=N findings] count-bearing seal |
| C-49 | AmendmentProtocol: named governance field on taxonomy |
| C-50 | OmissionRule: naming SCHEMA-PHASE-FAIL as structural failure criterion |
| C-51 | findings-sealed: echo field in summary section |
| C-52 | [TAXONOMY-DECLARED version=N] versioned seal with AmendmentVersion counter |
| C-53 | Distinct SCHEMA-OMISSION-FAIL FailureToken for row-absent failures |

*Group F max: 24*

---

## Group G — Echo Fidelity and Remediation Completeness (C-54–C-56) · 3 criteria

| Criterion | Description |
|-----------|-------------|
| C-54 | VerbatimRule: governing findings-sealed echo — character-for-character copy enforced by named constraint |
| C-55 | taxonomy-version: summary field echoing [TAXONOMY-DECLARED version=N] seal |
| C-56 | Named remediation: field per FailureToken entry — remediation path machine-derivable from token alone |

*Group G max: 12*

---

## Scoring Summary

| Group | Criteria | Max |
|-------|----------|-----|
| A — Structural Foundations | C-08–C-19 | 48 |
| B — Findings Quality | C-20–C-25 | 24 |
| C — Gate Token Structure | C-26–C-32 | 28 |
| D — Schema and Diff Completeness | C-33–C-38 | 24 |
| E — Advanced Schema Governance | C-39–C-47 | 36 |
| F — Seal Integrity and Failure Governance | C-48–C-53 | 24 |
| G — Echo Fidelity and Remediation Completeness | C-54–C-56 | 12 |
| **Total** | **C-08–C-56 · 49 criteria** | **196** |
```
