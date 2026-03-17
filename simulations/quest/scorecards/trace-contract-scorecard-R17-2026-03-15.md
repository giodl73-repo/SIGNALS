## trace-contract — Round 17 Scorecard

**Rubric:** v17 (C-08–C-47) | **Variations:** V-01 through V-05 | **Date:** 2026-03-15

---

### Scoring Key

| Symbol | Points | Meaning |
|--------|--------|---------|
| PASS | 4 | Criterion fully satisfied |
| PARTIAL | 2 | Criterion partially satisfied |
| FAIL | 0 | Criterion not satisfied |

**Scoring scope:** 35 assessable criteria (C-08–C-33, C-39–C-47) × 4 pts = 140 max  
C-34–C-38 carried PASS for all variations (inherited from R16-V05 baseline; not distinguishing in this round).

---

### Group A — Structural Foundations (C-08–C-19) · 12 criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 Contract scope 4 elements | PASS | PASS | PASS | PASS | PASS |
| C-09 Input fixture inline | PASS | PASS | PASS | PASS | PASS |
| C-10 Spec source with section | PASS | PASS | PASS | PASS | PASS |
| C-11 Expected output success path | PASS | PASS | PASS | PASS | PASS |
| C-12 Expected output error path | PASS | PASS | PASS | PASS | PASS |
| C-13 Expected output edge case | PASS | PASS | PASS | PASS | PASS |
| C-14 Value constraint + clause per element | PASS | PASS | PASS | PASS | PASS |
| C-15 EXPECTED-SEALED token format | PASS | PASS | PASS | PASS | PASS |
| C-16 Actual output: status + body | PASS | PASS | PASS | PASS | PASS |
| C-17 Diff accounts for every Expected element | PASS | PASS | PASS | PASS | PASS |
| C-18 ✓ / F-NN symbols correct | PASS | PASS | PASS | PASS | PASS |
| C-19 No silent omissions in Diff | PASS | PASS | PASS | PASS | PASS |

**Group A subtotal:** 48 / 48 all variations.

Evidence notes for C-19:
- All variations instruct "compare each Expected Output entry against the corresponding Actual Output entry" with no omission escape hatch. V-01 additionally requires every GateTokenSchema row to receive a schema-sweep entry with an explicit omission rule; this strengthens C-19 at the schema level, though C-19 is primarily about element diff coverage.

---

### Group B — Findings Quality (C-20–C-25) · 6 criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-20 Finding format: all 5 fields | PASS | PASS | PASS | PASS | PASS |
| C-21 Severity constrained to 3 values | PASS | PASS | PASS | PASS | PASS |
| C-22 Mechanism-type constrained to taxonomy | PARTIAL | PASS | PARTIAL | PASS | PASS |
| C-23 Root-cause names component/path | PASS | PASS | PASS | PASS | PASS |
| C-24 Hypothesis self-test applied | PASS | PASS | PASS | PASS | PASS |
| C-25 FINDINGS-COMPLETE token format | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |

**Group B subtotals:** V-01: 20 | V-02: 22 | V-03: 20 | V-04: 22 | V-05: 22

**C-22 evidence:**
- V-01: Finding block template carries `[missing-field | wrong-value | type-violation | ...]` as an inline bracket comment — describes the vocabulary but does not constitute a constraint; a non-taxonomy token produces a syntactically valid finding → PARTIAL
- V-02: `MechanismTypeTaxonomy` declared inline with `closed: true`, amendment protocol, and `[TAXONOMY-DECLARED]` seal before findings begin; mechanism-type field in finding template references "see TAXONOMY-DECLARED above" → PASS
- V-03: Same inline bracket comment form as V-01 baseline; taxonomy not formalized → PARTIAL
- V-04: Full taxonomy declaration block with `[TAXONOMY-DECLARED]` in Step 5 preamble; finding template references the declared set → PASS
- V-05: Taxonomy declared in Contract Layer 4 with `closed: true` and `TAXONOMY-DECLARED` token at Step 5; finding template cites "see Contract Layer 4 TAXONOMY-DECLARED" → PASS

**C-25 evidence (all PARTIAL):**
No variation explicitly instructs emission of a `[FINDINGS-COMPLETE]` token at the close of the findings section. All move directly from the last finding block to Sub-task A. This is a carried baseline weakness; the criterion requires the token, which is absent from all R17 templates. All variations PARTIAL.

---

### Group C — Census and Propagation (C-26–C-33) · 8 criteria shown

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-26 mechanism-distribution line emitted | PASS | PASS | PASS | PASS | PASS |
| C-27 Sole production site respected | PASS | PASS | PASS | PASS | PASS |
| C-28 Staging lines per candidate group | PASS | PASS | PASS | PASS | PASS |
| C-29 mechanism-type-shared = single token or `mixed` | PASS | PASS | PASS | PASS | PASS |
| C-30 Rationale names mechanism, not token | PASS | PASS | PASS | PASS | PASS |
| C-31 Pattern fill consumes staging lines | PASS | PASS | PASS | PASS | PASS |
| C-32 mechanism-type-shared = staging-line value | PASS | PASS | PASS | PASS | PASS |
| C-33 Staging line + fill site consistency enforced | PASS | PASS | PASS | PASS | PASS |

**Group C subtotal:** 32 / 32 all variations.

Notes:
- C-31/C-32: All variations instruct "Derive `mechanism-type-shared` from the staging lines. Do not re-derive from findings." This satisfies the behavioral constraint. The C-47 escalation moves this from prose to an ObligationBlock `Prohibit:` command — that difference scores at C-47, not C-33.
- C-27: All variations carry the sole-production-site instruction at Sub-task A.

---

### Extended Criteria — Schema, Obligation, Audit (C-39–C-44)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-39 GateTokenSchema field-type completeness | PASS | PASS | PASS | PASS | PASS |
| C-40 Named ObligationBlock | PASS | PASS | PASS | PASS | PASS |
| C-41 Two-party audit trace in gate token | PASS | PASS | PASS | PASS | PASS |
| C-42 Typed-column constraint per field | PASS | PASS | PASS | PASS | PASS |
| C-43 ObligationBlock as named addressable block | PASS | PASS | PASS | PASS | PASS |
| C-44 Gate token audit-trace fields named | PASS | PASS | PASS | PASS | PASS |

**C-39–C-44 subtotal:** 24 / 24 all variations.

Evidence notes:
- C-39: All carry 7-field `required-fields:` table with typed-column (string, format:S-section-ref, enum[PASS|FAIL]).
- C-42: All carry explicit type constraints per field; V-05's Layer 1 adds `detectable by field inspection without prose` annotation.
- C-43: V-01/V-02/V-04 carry 6-imperative ObligationBlock cross-referenced from Sub-task A, Sub-task B, S6.5. V-03 and V-05 carry 7 imperatives (the C-47 `Prohibit: re-derive-mechanism-type-shared` is the seventh). C-43 baseline requires the named addressable block with 6-imperative chain; 7th is a C-47 escalation, not a C-43 requirement. All PASS.
- C-44: All carry `attestation-by`, `attestation-result`, `verification-by`, `verification-result` in the GateTokenSchema `required-fields:` table.

---

### Group G — R17 Verification Infrastructure (C-45–C-47) · 3 new criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-45 Schema Diff phase bounded with SCHEMA-DIFF-COMPLETE | PASS | FAIL | FAIL | PASS | PASS |
| C-46 MechanismTypeTaxonomy as closed enumerated set | FAIL | PASS | FAIL | PASS | PASS |
| C-47 Re-derivation prohibition in ObligationBlock as Prohibit: | FAIL | FAIL | PASS | FAIL | PASS |

**C-45–C-47 subtotals (pts):** V-01: 4 | V-02: 4 | V-03: 4 | V-04: 8 | V-05: 12

**C-45 evidence:**
- V-01: Step 4 labeled "Schema Diff Phase [Contract Layer 1 — BOUNDED PHASE]"; completion token `[SCHEMA-DIFF-COMPLETE — all {N} GateTokenSchema fields inspected]` required before Step 5 begins; retroactive amendment rule included ("If found, add the missed violation to this sweep and emit an amended [SCHEMA-DIFF-COMPLETE]") → PASS
- V-02: Step 4 performs per-field sweep against type constraints but emits no phase-completion token; element diff (Step 6) is not gated on a schema-phase-complete signal → FAIL
- V-03: Step 4 is a sweep-only step with no completion token and no "element diff blocked until token written" rule → FAIL
- V-04: Step 4 labeled "Schema Diff Phase [Contract Layer 1 — BOUNDED PHASE]"; `[SCHEMA-DIFF-COMPLETE]` required before Step 5; sweep-omission rule present → PASS
- V-05: Step 4 governed by `VerificationInfrastructure: trace-verification-protocol (Contract Layer 4, schema-diff-phase)`; Layer 4 declares `bounded: true, completion-token: SCHEMA-DIFF-COMPLETE, invariant: element diff may not begin before SCHEMA-DIFF-COMPLETE is written`; retroactive omission rule included → PASS

**C-46 evidence:**
- V-01: Mechanism-type vocabulary appears only as inline bracket comment in finding block template; no `MechanismTypeTaxonomy:` declaration block, no `closed: true`, no amendment protocol, no `[TAXONOMY-DECLARED]` token → FAIL
- V-02: `MechanismTypeTaxonomy:` block declared inline in Step 5 before findings begin; `closed: true`; per-token definitions with amendment rule; `[TAXONOMY-DECLARED — mechanism-type taxonomy sealed]` token emitted; finding template cites the declaration → PASS
- V-03: Same inline bracket comment as baseline; no formal declaration block → FAIL
- V-04: Step 5 combines taxonomy declaration and findings; `MechanismTypeTaxonomy:` block with `closed: true` and amendment rule; `[TAXONOMY-DECLARED]` before any finding block; finding template references declared set → PASS
- V-05: Contract Layer 4 declares `mechanism-type-taxonomy: declaration-site: before first finding block, declaration-token: TAXONOMY-DECLARED, closed: true` with full token enumeration and amendment rule; Step 5 instructs "reproduce verbatim from preamble" and emits `[TAXONOMY-DECLARED — mechanism-type taxonomy operative]`; finding template cites "Contract Layer 4 TAXONOMY-DECLARED" → PASS

**C-47 evidence:**
- V-01: Sub-task B carries `"Derive mechanism-type-shared from the staging lines. Do not re-derive from findings."` — imperative prose in step text, not a `Prohibit:` command within the named ObligationBlock; compliance requires auditing step narrative → FAIL
- V-02: Same prose prohibition in Sub-task B step text → FAIL
- V-03: ObligationBlock in Contract Layer 2 carries `Prohibit: re-derive-mechanism-type-shared — the mechanism-type-shared value at the Sub-task B fill site must equal the value derived from the staging lines at that phase; it must not be re-derived by re-reading finding text after staging lines are written`. Sub-task B replaces prose instruction with `see: ObligationBlock (Prohibit: re-derive-mechanism-type-shared)` and a note that the obligation is not restated here. Preamble seal confirms "Obligation Layer (7 imperatives, including Prohibit: re-derive-mechanism-type-shared)" → PASS
- V-04: ObligationBlock carries 6 imperatives; re-derivation prohibition remains as prose in Sub-task B step text ("Do not re-derive from findings.") — not elevated to Prohibit: command → FAIL
- V-05: ObligationBlock carries `Prohibit: re-derive-mechanism-type-shared` as 7th imperative; preamble seal confirms it; Contract Layer 4 declares `re-derivation-prohibition: see: ObligationBlock (Prohibit: re-derive-mechanism-type-shared), enforcement-site: Sub-task B fill site, audit-method: read ObligationBlock (Contract Layer 2)`. Sub-task B carries two see: references — one to the ObligationBlock and one to VerificationInfrastructure naming the enforcement site → PASS

---

### Composite Scores

| Variation | A (48) | B (24) | C (32) | C-39–C-44 (24) | C-45–C-47 (12) | Total (140) | % |
|-----------|--------|--------|--------|----------------|----------------|-------------|---|
| V-01 | 48 | 20 | 32 | 24 | 4 | **128** | 91.4% |
| V-02 | 48 | 22 | 32 | 24 | 4 | **130** | 92.9% |
| V-03 | 48 | 20 | 32 | 24 | 4 | **128** | 91.4% |
| V-04 | 48 | 22 | 32 | 24 | 8 | **134** | 95.7% |
| **V-05** | **48** | **22** | **32** | **24** | **12** | **138** | **98.6%** |

**Rank:** V-05 > V-04 > V-02 > V-01 = V-03

---

### Variation Rankings

| Rank | Variation | Score | Primary Contribution |
|------|-----------|-------|----------------------|
| 1 | **V-05** | 138/140 | All three R17 targets as Contract Layer 4; C-45 + C-46 + C-47 all PASS |
| 2 | V-04 | 134/140 | C-45 + C-46 via bounded phase + closed taxonomy; C-47 held at baseline |
| 3 | V-02 | 130/140 | C-46 via formal inline taxonomy; C-22 PASS; C-45/C-47 FAIL |
| 4 | V-01 | 128/140 | C-45 via bounded phase with retroactive amendment rule; C-22 PARTIAL |
| 4 | V-03 | 128/140 | C-47 via ObligationBlock 7th Prohibit: imperative; C-22 PARTIAL |

---

### Excellence Signals — V-05 Patterns

**1. Pre-declared Verification Infrastructure as a named contract layer**
V-05 introduces Contract Layer 4 as a peer to Schema, Obligation, and Audit layers. Rather than declaring the bounded phase at Step 4 and the closed taxonomy at Step 5 (as V-04 does), V-05 declares all three R17 verification constraints before any execution begins. The layer is named, addressable, and cross-referenced at each site. This mirrors the architectural pattern of the other three layers: declare once in the preamble, reference by name at the point of use, never restate the content. The benefit is that an operator reads the preamble and knows all four structural constraints before opening Step 1.

**2. Enforcement-site and audit-method declared inside the infrastructure layer**
V-05's `VerificationInfrastructure` block names, for each protocol, where compliance is enforced (`enforcement-site: Sub-task B fill site`) and how an auditor verifies it (`audit-method: read ObligationBlock (Contract Layer 2) — the prohibition is the seventh imperative; do not audit by reading Sub-task B step text`). This makes the infrastructure self-describing: an auditor reading Layer 4 knows precisely where to check each invariant without reading step narratives.

**3. Summary row as rubric compliance map**
V-05's Summary section annotates each compliance row with both the contract layer and the rubric criterion tag:
```
schema-diff: … SCHEMA-DIFF-COMPLETE emitted [Contract Layer 4 / C-45]
mechanism-type-taxonomy: … TAXONOMY-DECLARED [Contract Layer 4 / C-46]
ObligationBlock: … 7 imperatives including Prohibit: re-derive-mechanism-type-shared … [Contract Layer 2 / C-47]
VerificationInfrastructure: all three R17 verification protocols applied [Contract Layer 4]
```
This turns the Summary into a self-auditing compliance map: an auditor can verify all three R17 advances by reading the Summary alone, without cross-referencing the step log.

**4. Retroactive schema-sweep amendment protocol (V-01 / carried into V-05)**
V-01 introduces — and V-05 inherits — the rule that a type violation discovered during the element diff that is absent from the schema-diff sweep record must be retroactively added to the sweep with an amended `[SCHEMA-DIFF-COMPLETE]`. This closes the edge case where a sweep was reported complete but actually had a gap. V-04 carries the SCHEMA-DIFF-COMPLETE requirement but omits this retroactive correction rule; V-05 inherits it from the VerificationInfrastructure `omission-rule:` declaration in Layer 4.

---

### Patterns That Did Not Reach Full PASS in Any Variation

**C-25 (FINDINGS-COMPLETE token):** No variation in R17 instructs emission of a `[FINDINGS-COMPLETE]` token at the close of the findings section. This was also absent in R16-V05 (the baseline for all R17 variations). The v18 synthesis pattern should elevate the FINDINGS-COMPLETE instruction into the findings step — either as a standalone step-close token or as part of the bounded findings phase in Contract Layer 4.

---

```json
{"top_score": 98, "all_essential_pass": false, "new_patterns": ["Pre-declared Verification Infrastructure as a named fourth contract layer before execution begins — all verification-level structural constraints (phase boundaries, vocabulary closures, prohibition chain) declared as a named, addressable layer peer to Schema, Obligation, and Audit layers, so operators engage with them as design constraints rather than per-step instructions", "Enforcement-site and audit-method declared inside the infrastructure layer — each protocol names where compliance is enforced and how an auditor verifies it, making the infrastructure self-describing without requiring step-text audit", "Summary row as rubric compliance map — each summary compliance row annotates its contract layer and rubric criterion tag, making the artifact self-auditing: all R17 advances verifiable from the Summary alone"]}
```
