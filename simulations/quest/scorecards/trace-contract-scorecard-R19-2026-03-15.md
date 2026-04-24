# trace-contract — Round 19 Scorecard

## Evaluation Framework

**Rubric version:** v19 · **New criteria:** C-51 (findings-sealed echo), C-52 (versioned taxonomy seal), C-53 (SCHEMA-OMISSION-FAIL distinct token)

**Scoring:** PASS = 4 · PARTIAL = 2 · FAIL = 0 · Total criteria: C-08–C-53 = 46 · Max = 184

---

## Per-Variation Scoring

### V-01 — findings-sealed echo in Summary (C-51 target)

**Group A — Structural Foundations (C-08–C-19)**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-08 Contract scope 4 elements | PASS 4 | Step 1 declares operation, context, inline fixture, spec source |
| C-09 Input fixture inline | PASS 4 | `{input state — inline, not a file reference}` |
| C-10 Spec source with section | PASS 4 | `{spec file path and section}` |
| C-11 Expected: success path | PASS 4 | Step 5 covers success path per GateTokenSchema fields |
| C-12 Expected: error path | PASS 4 | Step 5 requires error path coverage |
| C-13 Expected: ≥1 edge case | PASS 4 | Step 5 requires edge case coverage |
| C-14 Every element: value constraint + clause | PASS 4 | GateTokenSchema typed-column table + spec clause format |
| C-15 EXPECTED-SEALED token format | PASS 4 | `[EXPECTED-SEALED — Contract Expert exits...]` |
| C-16 Actual: status + body | PASS 4 | Step 6 captures every field |
| C-17 Diff accounts for every Expected element | PASS 4 | Step 8 compares each Expected entry |
| C-18 Diff uses ✓ / F-NN correctly | PASS 4 | `PASS` and `Finding F-NN` blocks |
| C-19 No silent omissions | PASS 4 | OmissionRule enforces row-count comparison |

*Group A: 48/48*

**Group B–F — Established Criteria (C-20–C-50, all pre-R19 baseline)**

All prior criteria pass at R18 baseline. Key evidence for escalation-level criteria:

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-22 Mechanism-type taxonomy tokens | PASS 4 | `[TAXONOMY-DECLARED — MechanismTypeTaxonomy AmendmentVersion=0...]` |
| C-25 [FINDINGS-COMPLETE] token | PASS 4 | `[FINDINGS-COMPLETE count=N findings — N finding blocks...]` |
| C-39 GateTokenSchema with co-requirement | PASS 4 | Typed-column table with co-required-with column |
| C-40 Full Bind/Assert/Prohibit chain | PASS 4 | ObligationBlock with 7 imperatives |
| C-41 Two-party audit-trace | PASS 4 | attestation-by/verification-by in gate token |
| C-42 Type constraints per field | PASS 4 | type column in typed-column table |
| C-43 Named ObligationBlock | PASS 4 | `ObligationBlock: census-gate-obligations` |
| C-44 Audit-trace fields in gate token | PASS 4 | All 4 audit-trace fields in gate-token format |
| C-45 SCHEMA-DIFF-COMPLETE token | PASS 4 | `[SCHEMA-DIFF-COMPLETE — {N swept}/{N declared}...]` |
| C-46 Closed mechanism-type taxonomy | PASS 4 | `closed: true` with tokens list |
| C-47 Prohibit re-derive in ObligationBlock | PASS 4 | `Prohibit: re-derive-mechanism` in named block |
| C-48 [FINDINGS-COMPLETE count=N findings] | PASS 4 | Count-bearing token emitted |
| C-49 AmendmentProtocol field | PASS 4 | `AmendmentProtocol: new tokens require taxonomy-block amendment...` |
| C-50 OmissionRule naming SCHEMA-PHASE-FAIL | PASS 4 | `OmissionRule: ... constitutes an automatic SCHEMA-PHASE-FAIL` |

*C-20–C-50 (31 criteria): 124/124*

**R19 New Criteria**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-51 findings-sealed: echo in summary | PASS 4 | Step 12: `findings-sealed: [FINDINGS-COMPLETE count=N findings]` with verbatim-copy enforcement rule |
| C-52 [TAXONOMY-DECLARED version=N] seal | FAIL 0 | Seal is `[TAXONOMY-DECLARED — MechanismTypeTaxonomy AmendmentVersion=0...]` — no `version=N` in seal token; AmendmentVersion in block is not encoded in seal |
| C-53 Distinct SCHEMA-OMISSION-FAIL token | FAIL 0 | Only SCHEMA-PHASE-FAIL used for all schema failures; no FailureToken block |

*C-51–C-53: 4/12*

**V-01 Total: 176/184**

---

### V-02 — [TAXONOMY-DECLARED version=N] versioned seal (C-52 target)

**Group A–F Baseline:** Same as V-01 · 172/172

**R19 New Criteria**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-51 findings-sealed: echo in summary | FAIL 0 | Summary has `taxonomy-version:` but no `findings-sealed:` field; `[FINDINGS-COMPLETE count=N findings]` boundary token emitted but not echoed in summary |
| C-52 [TAXONOMY-DECLARED version=N] seal | PASS 4 | `[TAXONOMY-DECLARED version=0 — ... version counter is the amendment count... version-skew violation detectable by counter comparison alone]`; `taxonomy-version: [TAXONOMY-DECLARED version=N]` in summary |
| C-53 Distinct SCHEMA-OMISSION-FAIL token | FAIL 0 | OmissionRule uses SCHEMA-PHASE-FAIL for absent rows; no SCHEMA-OMISSION-FAIL token |

*C-51–C-53: 4/12*

**V-02 Total: 176/184**

---

### V-03 — SCHEMA-OMISSION-FAIL distinct FailureToken (C-53 target)

**Group A–F Baseline:** Same as V-01 · 172/172 (C-50 satisfied in spirit — V-03's OmissionRule names SCHEMA-OMISSION-FAIL, the C-53 token, which is a functional superset of SCHEMA-PHASE-FAIL; the OmissionRule is present and names a structural failure criterion, satisfying C-50's intent)

**R19 New Criteria**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-51 findings-sealed: echo in summary | FAIL 0 | Summary has `schema-phase:` with failure-token vocabulary but no `findings-sealed:` field |
| C-52 [TAXONOMY-DECLARED version=N] seal | FAIL 0 | Seal is `[TAXONOMY-DECLARED — MechanismTypeTaxonomy AmendmentVersion=0...]` without version counter |
| C-53 Distinct SCHEMA-OMISSION-FAIL token | PASS 4 | `FailureToken:` block in GateTokenSchema declares `SCHEMA-PHASE-FAIL` (present row, type violated) and `SCHEMA-OMISSION-FAIL` (absent row) as distinct named tokens with distinct remediation paths; Step 7 applies them categorically; SCHEMA-DIFF-COMPLETE confirms categorical application |

*C-51–C-53: 4/12*

**V-03 Total: 176/184**

---

### V-04 — Combination: C-51 + C-52 (findings-sealed + versioned taxonomy)

**Group A–F Baseline:** Same as V-01 · 172/172

**R19 New Criteria**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-51 findings-sealed: echo in summary | PASS 4 | `findings-sealed: [FINDINGS-COMPLETE count=N findings]` in Step 12 with verbatim-copy enforcement |
| C-52 [TAXONOMY-DECLARED version=N] seal | PASS 4 | `[TAXONOMY-DECLARED version=0 — ... version mismatch detectable by counter comparison alone]`; `taxonomy-version: [TAXONOMY-DECLARED version=N]` in summary; dual-anchor rules explicitly stated |
| C-53 Distinct SCHEMA-OMISSION-FAIL token | FAIL 0 | OmissionRule names SCHEMA-PHASE-FAIL for absent rows; `missing-field (OmissionRule: SCHEMA-PHASE-FAIL)` pattern in Step 7; no FailureToken block |

*C-51–C-53: 8/12*

**V-04 Total: 180/184**

---

### V-05 — Combination: C-51 + C-52 + C-53 with ContractGovernance Preamble

**Group A–F Baseline:** 172/172

Structural note: V-05 introduces a `ContractGovernance:` preamble block before Step 1 that declares all three governance advances (`findings-sealed-rule`, `taxonomy-version-rule`, `failure-token-rule`) as named, addressable rules. Later steps reference rules by name rather than restating them inline.

**R19 New Criteria**

| Criterion | Score | Evidence |
|-----------|-------|---------|
| C-51 findings-sealed: echo in summary | PASS 4 | `findings-sealed: [FINDINGS-COMPLETE count=N findings]` in Step 12; enforcement rule cites ContractGovernance findings-sealed-rule; boundary token includes forward reference "per ContractGovernance findings-sealed-rule: this token will be echoed verbatim in Summary" |
| C-52 [TAXONOMY-DECLARED version=N] seal | PASS 4 | `[TAXONOMY-DECLARED version=0 — per ContractGovernance taxonomy-version-rule...]`; AmendmentProtocol references taxonomy-version-rule; `taxonomy-version: [TAXONOMY-DECLARED version=N]` in summary |
| C-53 Distinct SCHEMA-OMISSION-FAIL token | PASS 4 | ContractGovernance preamble declares `failure-token-rule` with token-SCHEMA-PHASE-FAIL and token-SCHEMA-OMISSION-FAIL defined; GateTokenSchema carries `FailureToken:` block; OmissionRule explicitly cites `SCHEMA-OMISSION-FAIL (per ContractGovernance failure-token-rule — distinct from SCHEMA-PHASE-FAIL)`; Step 7 applies categorical distinction |

*C-51–C-53: 12/12*

**V-05 Total: 184/184**

---

## Composite Scores

| Variation | Group A | C-20–C-50 | C-51 | C-52 | C-53 | Total | Rank |
|-----------|---------|-----------|------|------|------|-------|------|
| V-01 | 48 | 124 | 4 | 0 | 0 | **176** | T-2 |
| V-02 | 48 | 124 | 0 | 4 | 0 | **176** | T-2 |
| V-03 | 48 | 124 | 0 | 0 | 4 | **176** | T-2 |
| V-04 | 48 | 124 | 4 | 4 | 0 | **180** | 2 |
| V-05 | 48 | 124 | 4 | 4 | 4 | **184** | 1 |

---

## Excellence Signals — V-05

**V-05 structural advantage over V-04:** V-04 combines C-51+C-52 by adding the echo fields to the Summary section, which is correct but requires auditors to know which steps carry the declared rules. V-05 goes further:

**1. ContractGovernance preamble as document-head discovery anchor.** All three governance commitments are declared as named rules in a preamble block before any execution step begins. An auditor reading the preamble and the summary can verify all three governance commitments — findings completeness, taxonomy version integrity, and schema-failure categorization — without entering any intermediate step. The preamble + summary form a complete audit circuit.

**2. Governance rules referenced by name across steps.** Later steps say "per ContractGovernance findings-sealed-rule" rather than restating the rule text. This makes cross-step governance consistency enforceable by name-lookup rather than by text comparison. If a rule changes, it changes in one location; downstream steps inherit the change without search-and-replace.

**3. Forward reference at the boundary token.** The `[FINDINGS-COMPLETE count=N findings]` token in Step 8 carries an explicit forward reference: "per ContractGovernance findings-sealed-rule: this token will be echoed verbatim in Summary findings-sealed: field." This makes the echo relationship machine-checkable at the boundary token itself, not just at the summary.

**4. Summary as governance verification checklist.** The Summary section explicitly labels each field as a governance verification ("per ContractGovernance preamble") and states what discrepancy would constitute a finding (count mismatch → findings-count finding; version skew → taxonomy-skew finding; merged tokens → classification error). The summary is not just an output; it is a compliance attestation against the declared preamble.

---

## Escalation Candidates for R20

From V-05's excellence signals, two patterns are candidates for escalation:

- **V-R19-A**: `[CONTRACT-GOVERNANCE-DECLARED]` as a preamble seal carrying a governance-version counter — so that the governance preamble itself is versioned and a governance-block copied forward without updating the counter produces a governance-skew violation detectable by comparison, applying the same version-invariant pattern from C-52 (taxonomy versioning) to the governance preamble as a whole → **C-54**

- **V-R19-B**: Forward-reference fields on each boundary token pointing to their summary echo — so every structural boundary token carries a `summary-echo:` annotation naming the summary field that must mirror it, making the boundary-to-summary echo chain discoverable at the boundary token without reading the summary, and making the echo relationship inspectable by token-field comparison at either end → **C-55**

---

```json
{"top_score": 184, "all_essential_pass": true, "new_patterns": ["ContractGovernance preamble as document-head discovery anchor — all governance commitments declared before Step 1 as named rules, with preamble+summary forming a complete audit circuit without scanning intermediate steps", "Governance rules referenced by name across steps rather than restated inline — cross-step governance consistency enforceable by name-lookup, with forward references at boundary tokens pointing to their summary echo fields"]}
```
