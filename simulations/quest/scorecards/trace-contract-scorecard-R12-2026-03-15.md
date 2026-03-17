## trace-contract v12 Scorecard — Rounds R12 (census rubric, C-29–C-34)

### Rubric Reference

| ID | Description | Points |
|----|-------------|--------|
| C-26 | Gate-closure confirmation token (`clauses-resolved` echo) | 10 |
| C-27 | Branch-conditional Patterns template slots (pre-printed structural fields per branch) | 10 |
| C-28 | Vocabulary-constrained `mechanism-type:` token per finding | 15 |
| C-29 | `mechanism-type-shared:` in Singleton + Multi-pattern branch templates | 15 |
| C-30 | `mechanism-distribution:` aggregate in Summary | 10 |
| C-31 | S5.5 mandatory interstitial Taxonomy Census (single ordered walk, both sub-tasks) | 20 |
| C-32 | `group-candidate-N:` staging format with `rationale:` clause in Sub-task B | 20 |
| C-33 | Explicit copy-forward directive: Summary names S5.5 Sub-task A as authoritative source for `mechanism-distribution:` | 15 |
| C-34 | Staging-to-template reference chain: `source: group-candidate-N` in each `pattern-N:` Multi-pattern entry | 15 |
| **Total** | | **130** |

---

### V-01 — Phrasing Register: Explicit Verbatim-Copy Directive at Summary

**Axis:** phrasing-register | **Target:** C-33

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | PASS | `[EXPECTED-RESOLVED \| gate-clauses:N \| clauses-resolved:M \| phase:2-complete]` at S5.6 |
| C-27 | PASS | Zero/Singleton/Multi branch templates all carry pre-printed structural fields |
| C-28 | PASS | Named enumeration (`field-mapping \| serialization-path \| conditional-branch …`) + self-test rule |
| C-29 | PASS | `mechanism-type-shared:` in both Singleton and Multi-pattern templates |
| C-30 | PASS | `mechanism-distribution:` field present in Summary template |
| C-31 | PASS | S5.5 mandatory interstitial with Sub-task A tally + Sub-task B staging; `[TAXONOMY-CENSUS-COMPLETE]` token |
| C-32 | PASS | `group-candidate-N: findings=[…] mechanism-type-shared=… rationale=…` staging format with `rationale=` clause |
| C-33 | **PASS** | Named procedural step "**Copy-forward step (required before writing body)**" plus field directive `{VERBATIM-COPY from [S5.5 Sub-task A · mechanism-distribution] — do not recount}`; also: "The `mechanism-distribution:` line must be the exact text from S5.5 Sub-task A." |
| C-34 | **FAIL** | Multi-pattern template: `findings:`, `mechanism-type-shared:`, `root-cause:`, `fix-strategy:` — no `source: group-candidate-N` field |

**Score: 115/130**

---

### V-02 — Output Format: `source: group-candidate-N` Field in Multi-pattern Template

**Axis:** output-format | **Target:** C-34

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | PASS | `[EXPECTED-RESOLVED \| gate-clauses:N \| clauses-resolved:M \| phase:2-complete]` at S5.6 |
| C-27 | PASS | Zero/Singleton/Multi templates with structural fields; Singleton adds `source: group-candidate-1` slot |
| C-28 | PASS | Mechanism-type named enumeration + self-test rule |
| C-29 | PASS | `mechanism-type-shared:` in both Singleton and Multi-pattern templates |
| C-30 | PASS | `mechanism-distribution:` in Summary template |
| C-31 | PASS | S5.5 mandatory with both sub-tasks; `[TAXONOMY-CENSUS-COMPLETE]` |
| C-32 | PASS | `group-candidate-N:` staging with `rationale=` clause |
| C-33 | **PARTIAL** | Field placeholder says `{copy verbatim from S5.5 Sub-task A — do not re-derive}` — names S5.5 Sub-task A as source but no dedicated labeled procedural step preceding S7; lacks the behavioral pre-action form that makes the copy structurally mandatory | 10/15 |
| C-34 | **PASS** | `source: group-candidate-N` present in both Singleton and Multi-pattern templates; "A `pattern-N:` entry without a `source:` field is incomplete" enforcement note |

**Score: 125/130**

---

### V-03 — Lifecycle Emphasis: Gate S6.5 Blocking Summary

**Axis:** lifecycle-emphasis | **Target:** C-33 via hard gate

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | PASS | `[EXPECTED-RESOLVED \| gate-clauses:N \| clauses-resolved:M \| phase:2-complete]` at S5.6 |
| C-27 | PASS | Branch templates with structural slots; Zero: `no-pattern-confirmation:`, Singleton: `single-finding-ref:` + `mechanism-type-shared:`, Multi: `findings:` + `mechanism-type-shared:` |
| C-28 | PASS | Named mechanism-type enumeration |
| C-29 | PASS | `mechanism-type-shared:` in Singleton and Multi-pattern templates |
| C-30 | PASS | `mechanism-distribution:` in Summary template |
| C-31 | PASS | S5.5 mandatory interstitial; `[TAXONOMY-CENSUS-COMPLETE]` |
| C-32 | PASS | `group-candidate-N:` staging with `rationale=` clause |
| C-33 | **PASS** | Gate S6.5 is a blocking precondition: "Do not write the `## Summary` section header until this gate token is emitted." Gate token requires verbatim paste of `mechanism-distribution:` from S5.5 Sub-task A; S7 instruction requires value to match gate token exactly. Structural enforcement mode exceeds a named directive. |
| C-34 | **FAIL** | Multi-pattern template has `mechanism-type-shared:`, `root-cause:`, `fix-strategy:` — no `source: group-candidate-N` field |

**Score: 115/130**

---

### V-04 — Combination: Phrasing Register + Output Format (C-33 + C-34 dual)

**Axis:** phrasing-register + output-format | **Target:** C-33 + C-34

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | PASS | `[EXPECTED-RESOLVED \| gate-clauses:N \| clauses-resolved:M \| phase:2-complete]` at S5.6 |
| C-27 | PASS | Zero/Singleton/Multi templates with pre-printed structural fields; `source:` field added in Singleton and Multi templates |
| C-28 | PASS | Named enumeration + self-test; severity definitions included |
| C-29 | PASS | `mechanism-type-shared:` in Singleton (`copy verbatim from group-candidate-1`) and Multi-pattern (`copy verbatim from the source group-candidate-N staging line`) templates |
| C-30 | PASS | `mechanism-distribution:` field in Summary |
| C-31 | PASS | S5.5 mandatory interstitial; Sub-task A emits "the authoritative value consumed by Summary"; `[TAXONOMY-CENSUS-COMPLETE \| … \| census-author:Connectors-Contract-Expert]` |
| C-32 | PASS | `group-candidate-N:` staging with `rationale=` (naming shared component/path), one line per candidate group |
| C-33 | **PASS** | Labeled procedural step "**Copy-forward step (required before writing body)**"; field directive `{VERBATIM-COPY from [S5.5 Sub-task A · mechanism-distribution] — exact text, no recount}`; authoritativeness declaration: "If a fresh count would produce a different value, the S5.5 value is authoritative." |
| C-34 | **PASS** | `source: group-candidate-N` in both Singleton and Multi-pattern templates; audit rule: "(a) `source:` names a `group-candidate-N` from S5.5 Sub-task B, and (b) `mechanism-type-shared:` matches that staging line's value exactly. A mismatch is a C-34 violation." |

**Score: 130/130**

---

### V-05 — Role Sequence + Lifecycle Emphasis + Output Format: Named Census Artifacts

**Axis:** role-sequence + lifecycle-emphasis + output-format | **Target:** C-29–C-34

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | PASS | `[EXPECTED-RESOLVED \| gate-clauses:N \| clauses-resolved:M \| phase:2-complete]` at S5.6 |
| C-27 | PASS | Zero/Singleton/Multi templates; Singleton carries `source: [CENSUS-ARTIFACT-B · group-candidate-1]`; Multi carries `source: [CENSUS-ARTIFACT-B · group-candidate-N]` |
| C-28 | PASS | Named enumeration; self-test: "the hypothesis requires system knowledge to write" |
| C-29 | PASS | `mechanism-type-shared: {copy verbatim from [CENSUS-ARTIFACT-B · group-candidate-N] mechanism-type-shared value}` in both branch templates |
| C-30 | PASS | `mechanism-distribution:` in Summary |
| C-31 | PASS | S5.5 produces two formally bounded named artifacts; `[TAXONOMY-CENSUS-COMPLETE \| artifact-A:sealed \| artifact-B:sealed \| census-author:Connectors-Contract-Expert]` — census ownership made structurally explicit via artifact sealing |
| C-32 | PASS | `[CENSUS-ARTIFACT-B]` contains `group-candidate-N:` entries with `rationale=` clause; artifact boundary enforces staging before template fill |
| C-33 | **PASS** | Summary instruction: "Consume `[CENSUS-ARTIFACT-A]` by reference. Do not re-derive the distribution." Field: `{VERBATIM-COPY from [CENSUS-ARTIFACT-A · mechanism-distribution] — exact text from the artifact}`; authoritativeness declaration: "If the value in Summary differs from the artifact, the artifact is authoritative." |
| C-34 | **PASS** | `source: [CENSUS-ARTIFACT-B · group-candidate-N]` in Multi-pattern template; audit rule: "every `pattern-N:` entry must have a `source:` field naming a `[CENSUS-ARTIFACT-B · group-candidate-N]`" |

**Score: 130/130**

---

### Rankings

| Rank | Variation | Score | C-33 | C-34 | Notes |
|------|-----------|-------|------|------|-------|
| 1 | V-04 | **130/130** | PASS | PASS | Dual-site closure via directive + source field |
| 1 | V-05 | **130/130** | PASS | PASS | Named-artifact architecture; ceiling variant |
| 3 | V-02 | 125/130 | PARTIAL | PASS | Source field closes C-34; C-33 only partially closed (inline hint, no behavioral step) |
| 4 | V-01 | 115/130 | PASS | FAIL | Named directive closes C-33; no source field at Patterns site |
| 4 | V-03 | 115/130 | PASS | FAIL | Gate closes C-33 (stronger mode than V-01); no source field at Patterns site |

---

### Excellence Signals (top-scoring variations V-04 and V-05)

**1. Two-site orthogonal closure is additive and non-interfering**
C-33 (Summary site) and C-34 (Patterns site) are structurally independent derivation sites. The V-01/V-03 vs. V-02 diagnostic confirms this: each mechanism targets a different lifecycle location, and combining them (V-04) closes both gaps without degrading any existing criterion. The combination is purely additive.

**2. Named procedural step converts field hint into a behavioral precondition**
V-01 and V-04 add "Copy-forward step (required before writing body)" as a labeled instruction preceding the S7 template — not inside a field placeholder. This makes the copy action a behavioral requirement that must occur before writing begins, which is structurally distinct from an inline comment an operator may read after writing.

**3. Named census artifact boundaries create role-owned, formally scoped outputs**
V-05's `[CENSUS-ARTIFACT-A]...[/CENSUS-ARTIFACT-A]` bounded tags — and the corresponding `[CENSUS-ARTIFACT-B]` — give the Expert's outputs physically distinct, nameable scope. Downstream consumers reference artifacts by canonical name (`source: [CENSUS-ARTIFACT-B · group-candidate-N]`), which is stronger than "copy from group-candidate-N in S5.5 Sub-task B" because name-based consumption makes re-derivation at the consumption site structurally visible: if the artifact reference is absent, the derivation chain is broken by inspection.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Two-site orthogonal closure: C-33 (Summary) and C-34 (Patterns) are independent derivation sites — combining mechanisms at each site is additive without interference; single-axis variants (V-01, V-02, V-03) each close one site while leaving the other open", "Named procedural step before section write converts copy-forward from hint to behavioral precondition — 'Copy-forward step (required before writing body)' as a labeled instruction preceding the template is more enforceable than an inline field placeholder comment", "Named census artifact boundaries (CENSUS-ARTIFACT-A/B with open/close tags) create formally scoped role-owned outputs that downstream consumers reference by canonical artifact name rather than positional 'above' reference — makes re-derivation at consumption site structurally detectable"]}
```
