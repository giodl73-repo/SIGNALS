# /quest:score — trace-contract Round 20

## Rubric Summary

**Active criteria:** C-08 through C-56 (49 total)
**R20 new criteria:** C-54, C-55, C-56 (escalating from C-51, C-52, C-53 respectively)

---

## Prior Baseline (C-08 through C-53) — All 5 Variations

All five variations carry the full R19+ structural baseline without reduction:

| Criterion Group | Elements | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|---|
| C-08–C-14 Essential | Contract Scope, role separation, expected/actual format, finding block, Sub-task A/B structure | PASS | PASS | PASS | PASS | PASS |
| C-15–C-22 Taxonomy | MechanismTypeTaxonomy closed enum, AmendmentProtocol, version counter, token governance | PASS | PASS | PASS | PASS | PASS |
| C-23–C-27 Schema | GateTokenSchema typed columns, co-requirement, OmissionRule, [SCHEMA-SEALED] | PASS | PASS | PASS | PASS | PASS |
| C-28–C-35 ObligationBlock | Named census-gate-obligations, full Bind/Assert/Prohibit chain, re-derive prohibition | PASS | PASS | PASS | PASS | PASS |
| C-36–C-41 Findings | F-NN block format, mechanism-type draws from taxonomy, recommendation on breaking/degraded | PASS | PASS | PASS | PASS | PASS |
| C-42–C-44 GateToken | Typed-column schema, named ObligationBlock as cross-reference anchor, audit-trace fields (attestation-by/result, verification-by/result) | PASS | PASS | PASS | PASS | PASS |
| C-45–C-47 Schema Phase | SCHEMA-DIFF-COMPLETE token, inline closed MechanismTypeTaxonomy, re-derive prohibition in ObligationBlock | PASS | PASS | PASS | PASS | PASS |
| C-48–C-50 Boundary Tokens | [FINDINGS-COMPLETE count=N findings], [TAXONOMY-DECLARED version=N] versioned seal, OmissionRule naming SCHEMA-PHASE-FAIL | PASS | PASS | PASS | PASS | PASS |
| C-51–C-53 R19 Advances | `findings-sealed:` named echo field, versioned seal counter in taxonomy block, SCHEMA-PHASE-FAIL and SCHEMA-OMISSION-FAIL as distinct nominally-distinct tokens | PASS | PASS | PASS | PASS | PASS |

---

## R20 New Criteria — Criterion-by-Criterion

### C-54: Named `VerbatimRule:` block governing `findings-sealed:` as string-comparison contract

| V | Result | Evidence |
|---|---|---|
| V-01 | **PASS** | Step 2 declares `VerbatimRule: findings-sealed-echo` with `copy-rule:`, `violation:`, and `verification: string-compare findings-sealed value against [FINDINGS-COMPLETE] token; any character difference is a violation, not a rendering variant`. `[VERBATIM-RULE-DECLARED]` seal emitted. Step 13 cross-references by name without restating. Named block present; string-comparison verification explicit. |
| V-02 | **FAIL** | No `VerbatimRule:` block declared. Step 12 enforces via prose: "MUST be copied verbatim." Enforcement is natural-language; violation requires semantic reading, not string comparison. |
| V-03 | **FAIL** | Same as V-02 baseline. Step 12 prose enforcement only; no named block and no verification field. |
| V-04 | **PASS** | Step 2 GovernancePreamble declares `VerbatimRule: findings-sealed-echo` as Layer-1 with identical structure to V-01: `copy-rule:`, `violation:`, `verification:` fields. `[GOVERNANCE-PREAMBLE-DECLARED]` seal names both rules. Step 13 references by name. |
| V-05 | **PASS** | Step 2 GovernancePreamble Layer-1 declares `VerbatimRule findings-sealed-echo` with full fields. `[FINDINGS-COMPLETE]` token (Step 10) explicitly names the Layer-1 rule: "GovernancePreamble Layer-1 VerbatimRule governs the findings-sealed: echo at Step 14." Summary pre-check lists Layer-1 obligation before writing. |

---

### C-55: Named `taxonomy-version:` field in Summary echoing the versioned seal

| V | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | Summary (Step 13) carries: `findings-sealed:`, `schema-phase:`, `mechanism-type-shared:`, `gate-status:`. No `taxonomy-version:` field. Taxonomy version not auditable from summary anchor. |
| V-02 | **PASS** | Summary (Step 12) carries `taxonomy-version: [TAXONOMY-DECLARED version=N]` as a named field. Taxonomy seal (Step 2) explicitly states: "The Summary section's taxonomy-version: field echoes this seal; version-skew…constitutes a summary-integrity violation." Both fields (`findings-sealed:` and `taxonomy-version:`) present in Summary. |
| V-03 | **FAIL** | Summary (Step 12) does not include `taxonomy-version:` field. Same as V-01 baseline on this criterion. |
| V-04 | **PASS** | Summary (Step 13) carries both `findings-sealed:` and `taxonomy-version:`. Step 13 explicitly requires both echo rules to be satisfied and declares: "If either echo field deviates from its source token, a summary-integrity finding MUST be raised." Dual-anchor fully realized. |
| V-05 | **PASS** | Summary (Step 14) carries both echo fields. Pre-check before writing Summary explicitly lists "Layer-2 TaxonomyEchoRule: copy `taxonomy-version:` verbatim from the most recent `[TAXONOMY-DECLARED version=N]` seal." Governance block confirms Layer-2 status. |

---

### C-56: Named `remediation:` field per `FailureToken:` entry, machine-derivable from token alone

| V | Result | Evidence |
|---|---|---|
| V-01 | **FAIL** | FailureToken block (Step 4) carries only `trigger:` per entry; no `remediation:` field. Corrective action requires prose reading of OmissionRule and surrounding context. |
| V-02 | **FAIL** | Same as V-01 on FailureToken structure. No `remediation:` field. |
| V-03 | **PASS** | FailureToken block (Step 3) carries distinct `remediation:` per entry: `SCHEMA-PHASE-FAIL.remediation: correct field type to match declared constraint and re-sweep the schema from the top`; `SCHEMA-OMISSION-FAIL.remediation: add absent row to actual output and re-sweep the schema from the top`. `[SCHEMA-SEALED]` token explicitly states: "a shared remediation path across both tokens constitutes a structural violation of the FailureToken contract." Step 7 Schema Diff phase references remediation by pointer. |
| V-04 | **FAIL** | FailureToken block (Step 4) is unmodified from V-01/V-02 baseline — `trigger:` only, no `remediation:` field. C-56 axis not targeted. |
| V-05 | **PASS** | GovernancePreamble Layer-3 `RemediationContract failure-token-remediation` governs FailureToken block before GateTokenSchema is declared. GateTokenSchema (Step 4) carries `remediation:` per FailureToken with `governance: see GovernancePreamble Layer-3`. Schema Diff step (Step 8) references remediation via Layer-3 pointer for both failure types. Machine-derivation rule stated in preamble: "required corrective action MUST be derivable from the emitted token alone by field lookup without reading failure rationale text." |

---

## Composite Scores

49 criteria total (C-08–C-56). Prior baseline (C-08–C-53, 46 criteria): uniform PASS across all variations. New criteria (C-54, C-55, C-56, ~2 pts each). V-05 structural bonus (governance status block: +3).

| Variation | Baseline | C-54 | C-55 | C-56 | Bonus | **Score** |
|---|---|---|---|---|---|---|
| V-01 | 80 | +4 | – | – | – | **84** |
| V-02 | 80 | – | +4 | – | – | **84** |
| V-03 | 80 | – | – | +4 | – | **84** |
| V-04 | 80 | +4 | +4 | – | – | **88** |
| V-05 | 80 | +4 | +4 | +4 | +3 | **95** |

**Rank:** V-05 > V-04 >> V-01 = V-02 = V-03

---

## Excellence Signals — V-05

**Pattern 1: GovernancePreamble as a pre-execution declaration unit, parallel to ObligationBlock**
The `GovernancePreamble:` block in V-05 is structurally identical to `ObligationBlock:` in its purpose: it is the single addressable declaration site for all governance layers. No layer is restated inline. Later phases cross-reference by name only. A governance auditor reads the preamble; a census auditor reads the ObligationBlock. The two layers are orthogonal and independently verifiable. This is the same structural pattern applied recursively — the insight that named declaration blocks prevent scattered inline restatement generalizes beyond census obligations to any class of recurring constraint.

**Pattern 2: Governance status block in Summary with per-layer SATISFIED/VIOLATED/NOT-TRIGGERED**
V-05 Step 14 Summary carries:
```
Governance: GovernancePreamble Layer-1 findings-sealed-echo SATISFIED | VIOLATED
            GovernancePreamble Layer-2 taxonomy-version-field SATISFIED | VIOLATED
            GovernancePreamble Layer-3 failure-token-remediation SATISFIED | VIOLATED | NOT-TRIGGERED
```
This converts the summary from a domain-result report into a dual-layer report: domain results (severity table, gate-status) AND governance completeness. A governance auditor who reads only the Governance: block can confirm all three constraints fired correctly without entering the trace body. The NOT-TRIGGERED state for Layer-3 is a clean way to handle the case where no FailureToken was emitted — absence of trigger is itself auditable.

**Pattern 3: Governance violation as a breaking finding against the trace itself**
V-05 declares: "If any Governance entry is VIOLATED, a summary-integrity finding MUST be raised before the trace is closed. A VIOLATED governance layer is a breaking finding against the trace output itself, not the operation under test." This separates two finding classes: findings about the operation (what the contract says) and findings about the trace (whether the trace honored its own commitments). This distinction enables trace-quality auditing independently of operation-quality auditing — the trace can have a PASS gate-status (operation looks clean) while simultaneously carrying a finding that the trace itself was mis-executed.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["GovernancePreamble as pre-execution declaration unit parallel to ObligationBlock — all governance layers declared once and cross-referenced by name, no inline restatement", "Governance status block in Summary with per-layer SATISFIED/VIOLATED/NOT-TRIGGERED — governance completeness auditable from summary anchor without body scanning", "Governance-violation as breaking finding against trace output — VIOLATED layer triggers a finding before trace close, separating instruction-integrity violations from operation-contract violations"]}
```
