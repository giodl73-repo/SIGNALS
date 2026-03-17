Now I have everything I need. Let me score all five variations against the v18 rubric.

---

# Scorecard: trace-contract Round 18

**Rubric:** v18 · **Criteria:** C-08–C-50 · **Max:** 152 · **Date:** 2026-03-15

---

## Scoring Key

- **PASS** = 4 pts · **PARTIAL** = 2 pts · **FAIL** = 0 pts
- **Group A** (C-08–C-19): 12 criteria × 4 = 48 max
- **Group B** (C-20–C-25): 6 criteria × 4 = 24 max
- **Group C** (C-26–C-33): 8 criteria × 4 = 32 max
- **Extended** (C-39–C-50): 12 criteria × 4 = 48 max

---

## Group A — Structural Foundations (C-08–C-19)

All five variations carry the same structural foundation from prior rounds. Each provides a Contract Scope step with 4 required elements, inline fixture instruction, spec citation with section, full expected-output coverage (success + error + edge), value-constraint format per element, correct EXPECTED-SEALED token, Actual Output recording, complete diff coverage, and a no-silent-omissions Schema Diff sweep.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 scope 4 elements | PASS | PASS | PASS | PASS | PASS |
| C-09 fixture inline | PASS | PASS | PASS | PASS | PASS |
| C-10 spec source + section | PASS | PASS | PASS | PASS | PASS |
| C-11 success path | PASS | PASS | PASS | PASS | PASS |
| C-12 error path | PASS | PASS | PASS | PASS | PASS |
| C-13 edge case | PASS | PASS | PASS | PASS | PASS |
| C-14 value constraint + clause | PASS | PASS | PASS | PASS | PASS |
| C-15 EXPECTED-SEALED token | PASS | PASS | PASS | PASS | PASS |
| C-16 actual output status+body | PASS | PASS | PASS | PASS | PASS |
| C-17 diff covers all expected | PASS | PASS | PASS | PASS | PASS |
| C-18 PASS / F-NN symbols | PASS | PASS | PASS | PASS | PASS |
| C-19 no silent omissions | PASS | PASS | PASS | PASS | PASS |

**Group A subtotal — all: 48 / 48**

---

## Group B — Findings Quality (C-20–C-25)

All variations provide 7-field finding blocks (element, deviation, severity, mechanism-type, spec, hypothesis, recommendation), severity constrained to 3 vocabulary values, mechanism-type gated to taxonomy tokens, component-naming hypothesis, and hypothesis self-test. C-25 is distinguished by whether the findings-closure token carries a count assertion.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-20 finding format 5+ fields | PASS | PASS | PASS | PASS | PASS |
| C-21 severity 3 vocab | PASS | PASS | PASS | PASS | PASS |
| C-22 mechanism-type taxonomy | PASS | PASS | PASS | PASS | PASS |
| C-23 root-cause component | PASS | PASS | PASS | PASS | PASS |
| C-24 hypothesis self-test | PASS | PASS | PASS | PASS | PASS |
| C-25 FINDINGS-COMPLETE token | PASS | PASS | PASS | PASS | PASS |

*Evidence — C-25:*
- V-01: `[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. An inspector may verify completeness by counting F-01 through F-N without re-entering finding content.]` — token format correct ✓
- V-02: `[FINDINGS-COMPLETE]` — plain token, correct base format ✓
- V-03: `[FINDINGS-COMPLETE]` — plain token ✓
- V-04: `[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. Completeness is verifiable…]` ✓
- V-05: `[FINDINGS-COMPLETE count=N findings — FindingsClosureProtocol (Preamble Layer 3): N finding blocks appear above. Completeness verifiable by counting F-01 through F-N without re-entering content. Off-by-one detectable here.]` ✓

**Group B subtotal — all: 24 / 24**

---

## Group C — Census and Propagation (C-26–C-33)

All variations carry the baseline census and propagation structure: mechanism-distribution line at sole production site, per-group staging lines, mechanism-type-shared derived from staging (not re-derived from findings), rationale naming mechanism not token, pattern fill consuming staging lines, fill-site consistency via ObligationBlock reference.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-26 mechanism-distribution line | PASS | PASS | PASS | PASS | PASS |
| C-27 sole production site | PASS | PASS | PASS | PASS | PASS |
| C-28 staging lines per group | PASS | PASS | PASS | PASS | PASS |
| C-29 token or mixed | PASS | PASS | PASS | PASS | PASS |
| C-30 rationale names mechanism | PASS | PASS | PASS | PASS | PASS |
| C-31 fill from staging lines | PASS | PASS | PASS | PASS | PASS |
| C-32 fill site = staging value | PASS | PASS | PASS | PASS | PASS |
| C-33 staging/fill consistency | PASS | PASS | PASS | PASS | PASS |

**Group C subtotal — all: 32 / 32**

---

## Extended Criteria (C-39–C-50)

This is where R18 variations differentiate.

### C-39 through C-47 (established baseline) — evidence notes

All variations carry the full typed-column GateTokenSchema (7 fields, each with type + constraint + co-required-with), the named ObligationBlock with 2 Bind + 2 Assert + 3 Prohibit imperatives (including `Prohibit: re-derive-mechanism`), four named audit-trace fields in the gate token, and the SCHEMA-DIFF-COMPLETE boundary token. All pass C-39–C-47.

### C-48 — `[FINDINGS-COMPLETE count=N findings]` count-bearing seal

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Step 8 emits `[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. An inspector may verify completeness by counting F-01 through F-N without re-entering finding content.]` The count assertion is embedded directly. Summary section echoes `findings-sealed: [FINDINGS-COMPLETE count=N findings]`. |
| V-02 | **FAIL** | Step 8 emits plain `[FINDINGS-COMPLETE]` — no count field. C-48 requires count assertion at the boundary token. |
| V-03 | **FAIL** | Step 8 emits plain `[FINDINGS-COMPLETE]` — no count field. |
| V-04 | **PASS** | Step 8 emits `[FINDINGS-COMPLETE count=N findings — N finding blocks appear above this token. Completeness is verifiable by counting F-01 through F-N without re-entering finding content.]` Count assertion present. |
| V-05 | **PASS** | Step 5 emits `[FINDINGS-COMPLETE count=N findings — FindingsClosureProtocol (Preamble Layer 3): N finding blocks appear above. Completeness verifiable by counting F-01 through F-N without re-entering content. Off-by-one detectable here.]` Token carries count assertion and cites preamble source. |

### C-49 — Taxonomy declaration carries named `AmendmentProtocol:` field

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PARTIAL** | Taxonomy block has `closed: true` and rule, but no `AmendmentProtocol:` field in the declaration block. The `[TAXONOMY-DECLARED]` seal text includes "Amend the tokens list before first use of any new token" — the amendment concept is expressed in the seal, not as a named field in the declaration. C-49 requires the named field; seal-text embedding is a weaker structural form. |
| V-02 | **PASS** | Taxonomy block carries `AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment the taxonomy version, and re-seal before writing any finding block that uses the new token` plus `TaxonomyVersion: 1.0`. The named field is present and operational. `[TAXONOMY-DECLARED — MechanismTypeTaxonomy v1.0 … AmendmentProtocol governs all extensions.]` |
| V-03 | **FAIL** | Taxonomy block has `closed: true` but no `AmendmentProtocol:` field. Seal text says "No mechanism-type value may be used that is not listed above" — no amendment instruction at all, no amendment concept in seal. |
| V-04 | **PASS** | Taxonomy block carries `AmendmentProtocol: new tokens require taxonomy-block amendment before first use — add the token to the tokens list above, increment TaxonomyVersion, and re-seal before writing any finding block that uses the new token` plus `TaxonomyVersion: 1.0`. Seal references AmendmentProtocol explicitly. |
| V-05 | **PASS** | Preamble Layer 1 MechanismTypeTaxonomy carries `AmendmentProtocol:` field and `TaxonomyVersion: 1.0`. Seal: `[TAXONOMY-DECLARED — MechanismTypeTaxonomy v1.0 governs all mechanism-type values in this trace. AmendmentProtocol governs all extensions. Violation detectable by comparing declared tokens against tokens in use.]` |

### C-50 — Schema Diff phase carries named `OmissionRule:` declaring absent rows as automatic SCHEMA-PHASE-FAIL

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **FAIL** | Schema Diff (Step 7) has standard per-row sweep format and `[SCHEMA-DIFF-COMPLETE — schema sweep finished.]` token. No `OmissionRule:` field anywhere in the GateTokenSchema block or Schema Diff instructions. |
| V-02 | **FAIL** | Same as V-01 schema diff structure — no OmissionRule. Standard sweep instructions only. |
| V-03 | **PASS** | GateTokenSchema block carries `OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness is verified by row-count comparison: declared rows = sweep output rows; any shortfall triggers SCHEMA-PHASE-FAIL before element diff begins`. Step 7 opens with "Apply the OmissionRule declared in GateTokenSchema" and includes explicit row-count check. SCHEMA-DIFF-COMPLETE token carries `OmissionRule satisfied` status. Summary includes `OmissionRule:` status line. |
| V-04 | **FAIL** | Standard schema diff, no OmissionRule field in GateTokenSchema or Schema Diff phase. |
| V-05 | **PASS** | Preamble Layer 2 GateTokenSchema carries `OmissionRule: any GateTokenSchema row absent from schema-sweep output constitutes an automatic SCHEMA-PHASE-FAIL independent of the element diff result — schema completeness verified by row-count: declared rows ({N}) must equal sweep output rows; any shortfall is SCHEMA-PHASE-FAIL`. Step 4 (Schema Diff) references `Apply OmissionRule (Preamble Layer 2 — GateTokenSchema)` with explicit `SCHEMA-PHASE-FAIL` condition. SCHEMA-DIFF-COMPLETE token carries `OmissionRule: {satisfied | SCHEMA-PHASE-FAIL}`. |

### Extended Criteria Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-39 GateTokenSchema typed | PASS | PASS | PASS | PASS | PASS |
| C-40 Named ObligationBlock | PASS | PASS | PASS | PASS | PASS |
| C-41 Two-party audit trace | PASS | PASS | PASS | PASS | PASS |
| C-42 Typed-column constraints | PASS | PASS | PASS | PASS | PASS |
| C-43 Addressable ObligationBlock | PASS | PASS | PASS | PASS | PASS |
| C-44 Audit-trace fields named | PASS | PASS | PASS | PASS | PASS |
| C-45 SCHEMA-DIFF-COMPLETE token | PASS | PASS | PASS | PASS | PASS |
| C-46 Closed taxonomy declared | PASS | PASS | PASS | PASS | PASS |
| C-47 Prohibit re-derive in OB | PASS | PASS | PASS | PASS | PASS |
| C-48 Count-bearing FINDINGS seal | PASS | FAIL | FAIL | PASS | PASS |
| C-49 AmendmentProtocol field | PARTIAL | PASS | FAIL | PASS | PASS |
| C-50 OmissionRule in schema | FAIL | FAIL | PASS | FAIL | PASS |

**Extended subtotals:**
- V-01: 9×4 + 4 + 2 + 0 = 42 / 48
- V-02: 9×4 + 0 + 4 + 0 = 40 / 48
- V-03: 9×4 + 0 + 0 + 4 = 40 / 48
- V-04: 9×4 + 4 + 4 + 0 = 44 / 48
- V-05: 12×4 = 48 / 48

---

## Composite Scores

| Variation | Group A | Group B | Group C | Extended | Total | % |
|-----------|---------|---------|---------|----------|-------|---|
| V-01 | 48 | 24 | 32 | 42 | **146** | 96.1% |
| V-02 | 48 | 24 | 32 | 40 | **144** | 94.7% |
| V-03 | 48 | 24 | 32 | 40 | **144** | 94.7% |
| V-04 | 48 | 24 | 32 | 44 | **148** | 97.4% |
| V-05 | 48 | 24 | 32 | 48 | **152** | 100%  |

**Ranking: V-05 > V-04 > V-01 > V-02 = V-03**

---

## Excellence Signals — V-05

V-05 introduces two structural advances not seen in any prior variation:

**1. `ContractGovernancePreamble` as a named pre-execution section**

V-05 inserts a dedicated preamble section *before* the Pre-Run Phase, declaring all three governance layers (MechanismTypeTaxonomy, GateTokenSchema, ObligationBlock) as co-equal contract governance. Prior variations (including R17's best) declare governance inline during pre-run steps — the taxonomy in Step 2, schema in Step 3, ObligationBlock in Step 4. V-05 separates governance declaration from execution: the preamble is auditable in isolation, and any governance violation at a phase is traceable to a named preamble layer by reference rather than by reading step prose. The `[CONTRACT-GOVERNANCE-PREAMBLE-COMPLETE]` token seals this section the same way `[EXPECTED-SEALED]` seals expected output.

**2. `FindingsClosureProtocol` as a named sub-block within `ObligationBlock`**

Rather than stating findings closure as a standalone token instruction in Step 8, V-05 declares `FindingsClosureProtocol:` as a named sub-block co-located with `ObligationBlock: census-gate-obligations`. This means the findings-closure rule is part of the addressable obligation chain — an inspector can verify closure compliance by reading the ObligationBlock, not by searching for a step instruction. The `[FINDINGS-COMPLETE count=N findings]` token in Step 5 cites `FindingsClosureProtocol (Preamble Layer 3)` — the token is now an assertion against a named protocol, not just a procedural marker.

**3. Governance citation pattern in downstream phases**

All phases in V-05 cite governance layers by preamble reference: "Apply OmissionRule (Preamble Layer 2 — GateTokenSchema)," "token from MechanismTypeTaxonomy v1.0 — Preamble Layer 1," "see ObligationBlock: census-gate-obligations — all seven imperatives apply (Preamble Layer 3)." No phase restates a governance rule. This structural pattern is the strongest form of the `[OBLIGATION-BLOCK-SEALED — … cross-reference by name only]` principle, now extended across all three governance layers.

**4. Summary as governance compliance audit**

V-05's Summary section includes a "Contract Governance Preamble compliance:" block with per-layer status reporting: Layer 1 taxonomy token count and AmendmentProtocol application status; Layer 2 OmissionRule sweep counts; Layer 3 FindingsClosureProtocol seal. The summary is now an auditable governance attestation, not just a findings tally.

---

## Synthesis Patterns → Next Criteria Candidates

**V-R18-A**: `FindingsClosureProtocol` count cross-verification against Sub-task A entry count — the count in `[FINDINGS-COMPLETE count=N findings]` asserts N finding blocks exist; Sub-task A produces a `mechanism-distribution:` line with N entries (one per finding). An inspector who compares N from the closure seal against the entry count in the mechanism-distribution line can verify that all findings reached the census without consulting the finding blocks. This cross-count consistency is not currently required or produced → **C-51**

**V-R18-B**: `[CONTRACT-GOVERNANCE-PREAMBLE-COMPLETE]` carrying a preamble version and layer-count assertion — V-05 emits this token but without a version or layer inventory. The pattern of `[FINDINGS-COMPLETE count=N]` and `[SCHEMA-DIFF-COMPLETE {N} / {N}]` shows that phase-completion tokens should carry a verifiable count assertion; a `[CONTRACT-GOVERNANCE-PREAMBLE-COMPLETE layers=3 version=1.0]` token would make the preamble surface auditable by count — an inspector knows 3 layers were declared before reading any layer content → **C-52**

**V-R18-C**: `SCHEMA-PHASE-FAIL` propagation into gate-status derivation — V-03 and V-05 declare that a `SCHEMA-PHASE-FAIL` occurs if any GateTokenSchema row is absent from the sweep; but the gate-status derivation at Sub-task B is driven by `mechanism-type-shared`, not by the schema-phase result. A `SCHEMA-PHASE-FAIL` could coexist with `mechanism-type-shared: none` producing `gate-status: PASS` — structurally inconsistent. C-50 requires the OmissionRule; the next escalation: the OmissionRule should carry a `gate-propagation: SCHEMA-PHASE-FAIL forces gate-status: FAIL independent of mechanism-type-shared` clause, so that a schema-integrity failure at the sweep phase cannot produce a passing gate token → **C-53**

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["ContractGovernancePreamble as named pre-execution section declaring all governance layers before any census or gate work begins — makes governance surface auditable independently of execution phases via [CONTRACT-GOVERNANCE-PREAMBLE-COMPLETE] boundary token", "FindingsClosureProtocol declared as named sub-block within ObligationBlock — elevates findings closure from standalone token instruction to addressable obligation in the named chain, enabling preamble-reference citation at the closure site"]}
```
