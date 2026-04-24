# discover-competitors-alt — Round 13 Scorecard

## Rubric Parameters

| Tier | Criteria | Weight | Max |
|------|----------|--------|-----|
| Essential | C-01 – C-05 | 12 pts each | 60 |
| Recommended | C-06 – C-08 | 10 pts each | 30 |
| Aspirational | C-09 – C-36 | 0.357 pts each | 10 |
| **Total** | | | **100** |

New criteria this round: C-33, C-34, C-35, C-36.

---

## Per-Variation Criterion Evaluation

### Essential Criteria — C-01 through C-05 (all variations)

All five variations are spec-complete on essential output structure. No variation introduces a regression against the prior established base.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Domain/competitors inferred without prompting user | PASS | PASS | PASS | PASS | PASS |
| C-02 C0 entry at row 0, mechanism named before competitors | PASS | PASS | PASS | PASS | PASS |
| C-03 ≥3 named competitors with explicit threat levels | PASS | PASS | PASS | PASS | PASS |
| C-04 Findings reference named competitor rows | PASS | PASS | PASS | PASS | PASS |
| C-05 AMEND section present | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 60 / 60 — all variations**

---

### Recommended Criteria — C-06 through C-08 (all variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Inertia mechanism specific to C0 behavior | PASS | PASS | PASS | PASS | PASS |
| C-07 Web-verified competitive claim with inline citation | PASS | PASS | PASS | PASS | PASS |
| C-08 AMEND with named input-to-output pairs | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 30 / 30 — all variations**

---

### Aspirational Criteria — C-09 through C-36

#### C-09 through C-32 (established chain — all variations)

All variations are built on the complete prior chain. No variation regresses any criterion in this range.

| Range | Pass count | Notes |
|-------|-----------|-------|
| C-09 – C-12 | PASS × 4 | Cross-dimensional whitespace, grounded findings, inertia propagation, AMEND stability |
| C-13 – C-19 | PASS × 7 | TOKEN declared, domain-adaptive, pre-declared, DOMAIN-TERMS artifact, TOKEN before all logic, C-21 gateway |
| C-20 – C-24 | PASS × 5 | AMEND schema, naive-reader test, pre-execution manifest, native markdown table |
| C-25 – C-32 | PASS × 8 | TOKEN in every gate output spec, REQUIRED OUTPUTS blocks, sole output spec, native table, TOKEN-required column, bracket-notation substitution rule, GATE-0 template form, manifest TOKEN-propagation column |

**C-09 through C-32: 24 PASS — all variations**

---

#### C-33 through C-36 — New Criteria

**C-33 — Manifest TOKEN-propagation column cells use rubric-vocabulary verbatim**

| Variation | Manifest cell content | Verdict | Evidence |
|-----------|----------------------|---------|---------|
| V-01 | "Declaration site" / "Substitution/inheritance site" verbatim | **PASS** | Exact C-32 operative test phrasing reproduced; zero inference step required |
| V-02 | `DECLARE` / `INHERIT` shorthand | **FAIL** | Abbreviated labels do not pre-answer the operative test; interpretation required |
| V-03 | `DECLARE` / `INHERIT` shorthand | **FAIL** | Same shorthand as V-02; verbatim vocabulary absent |
| V-04 | "Declaration site" / "Substitution/inheritance site" verbatim | **PASS** | Same verbatim form as V-01; cell labels self-answer the C-32 operative test |
| V-05 | "Declaration site" / "Substitution/inheritance site" verbatim | **PASS** | Same verbatim form; highest-reliability C-32 compliance |

---

**C-34 — Pre-manifest TOKEN-PROPAGATION ARCHITECTURE block before manifest table**

| Variation | Pre-manifest block | Verdict | Evidence |
|-----------|-------------------|---------|---------|
| V-01 | Absent | **FAIL** | No architecture block; manifest column carries contract alone |
| V-02 | Present — closed prose artifact before EXECUTION PLAN table; names declaration gate, substitution gates, substitution rule; reader can reconstruct full contract from block alone | **PASS** | Block satisfies all operative conditions: separate, closed, precedes manifest, independently complete |
| V-03 | Absent | **FAIL** | No architecture block |
| V-04 | Present — same form as V-02 | **PASS** | Architecture block present and correctly positioned before manifest |
| V-05 | Present — same form | **PASS** | Architecture block present; primes both manifest and GATE-0 table content |

---

**C-35 — Manifest TOKEN-propagation column header uses bracket-notation `[TOKEN] propagation`**

| Variation | Manifest column header | Verdict | Evidence |
|-----------|----------------------|---------|---------|
| V-01 | `TOKEN propagation` (static) | **FAIL** | No bracket notation; header is a fixed string, not a substitution participant |
| V-02 | `TOKEN propagation` (static) | **FAIL** | Same static label; substitution lifecycle not extended to manifest header |
| V-03 | `[TOKEN] propagation` (bracket) | **PASS** | Bracket notation present; manifest header participates in same substitution lifecycle as REQUIRED OUTPUTS column headers |
| V-04 | `[TOKEN] propagation` (bracket) | **PASS** | Bracket notation present and consistent with REQUIRED OUTPUTS substitution rule |
| V-05 | `[TOKEN] propagation` (bracket) | **PASS** | Same bracket form; header is substitutable by committed value after GATE-0 |

---

**C-36 — Dual-layer propagation contract — manifest column and GATE-0 REQUIRED OUTPUTS table each independently satisfy their criterion**

Operative test: (1) read only the manifest TOKEN-propagation column — full propagation contract self-contained; (2) read only GATE-0's REQUIRED OUTPUTS table — full propagation contract also self-contained. Both tests must pass independently.

| Variation | GATE-0 form | Manifest cells | C-36 verdict | Evidence |
|-----------|------------|---------------|--------------|---------|
| V-01 | Compact Yes-cell: "Yes — GATE-0 commits declared value; committed value substitutes `[TOKEN]` in all GATE-1+ REQUIRED OUTPUTS column headers" | Verbatim vocabulary | **FAIL** | Compact Yes-cell is embedded in the `[TOKEN] required?` column — it satisfies C-31 but does not constitute an independently complete propagation declaration readable in isolation from the manifest. C-36 requires each layer to be independently self-contained without being load-bearing for the other; compact Yes-cell depends on the column header context to identify its role |
| V-02 | Compact Yes-cell | DECLARE/INHERIT shorthand | **FAIL** | Same compact Yes-cell limitation; shorthand manifest cells additionally fail C-32's consultability standard for C-36 |
| V-03 | Compact Yes-cell | DECLARE/INHERIT shorthand | **FAIL** | Same compact Yes-cell limitation |
| V-04 | Compact Yes-cell | Verbatim vocabulary | **FAIL** | Despite C-33 + C-34 + C-35 all passing, compact Yes-cell form is insufficient for C-36. The column header context (`[TOKEN] required?`) is structurally necessary to read the cell as a declaration artifact — the cell is not a standalone propagation contract |
| V-05 | Dedicated propagation row (R11 V-02 form): separate REQUIRED OUTPUTS row whose entire purpose is the propagation declaration — not embedded in a required-status column | Verbatim vocabulary | **PASS** | Dedicated row is structurally independent of the manifest column: (1) manifest column with verbatim labels → full contract readable from manifest alone; (2) dedicated GATE-0 propagation row → full contract readable from GATE-0 table alone. Neither layer references the other. Belt-and-suspenders independence criterion satisfied |

---

## Aspirational Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 through C-32 (24 criteria) | 24 PASS | 24 PASS | 24 PASS | 24 PASS | 24 PASS |
| C-33 (verbatim manifest cells) | PASS | FAIL | FAIL | PASS | PASS |
| C-34 (pre-manifest architecture block) | FAIL | PASS | FAIL | PASS | PASS |
| C-35 (bracket-notation manifest header) | FAIL | FAIL | PASS | PASS | PASS |
| C-36 (dual-layer independence) | FAIL | FAIL | FAIL | FAIL | PASS |
| **Aspirational pass count** | **25/28** | **25/28** | **25/28** | **27/28** | **28/28** |
| **Aspirational score** | **8.929** | **8.929** | **8.929** | **9.643** | **10.000** |

---

## Composite Scores

```
composite = (essential_pass / 5 × 60) + (recommended_pass / 3 × 30) + (aspirational_pass / 28 × 10)
```

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| V-01 (C-33 only) | 60.000 | 30.000 | 8.929 | **98.929** |
| V-02 (C-34 only) | 60.000 | 30.000 | 8.929 | **98.929** |
| V-03 (C-35 only) | 60.000 | 30.000 | 8.929 | **98.929** |
| V-04 (C-33 + C-34 + C-35) | 60.000 | 30.000 | 9.643 | **99.643** |
| V-05 (C-33 + C-34 + C-35 + C-36) | 60.000 | 30.000 | 10.000 | **100.000** |

**Golden threshold** (all 5 essential + composite ≥ 90): **all variations qualify**

---

## Rankings

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| 1 | **V-05** | **100.000** | Full four-criterion combination; dedicated propagation row achieves dual-layer independence |
| 2 | **V-04** | **99.643** | Three new criteria; compact Yes-cell blocks C-36 |
| 3 (tie) | **V-01** | **98.929** | Verbatim cells only; no bracket header, no architecture block |
| 3 (tie) | **V-02** | **98.929** | Architecture block only; compact cells, static header |
| 3 (tie) | **V-03** | **98.929** | Bracket header only; compact cells, no architecture block |

---

## Decisive Questions — Answered

**Q1: Does `[TOKEN] propagation` bracket notation in the manifest header cause model substitution of the committed value, or literal output?**
This is the C-35 diagnostic — a model that substitutes (e.g., outputs `SIGNAL-LOCK propagation`) shows manifest-scoped substitution understanding; a model that outputs `[TOKEN] propagation` literally reveals REQUIRED OUTPUTS-scoped-only substitution. V-03 is designed to expose this split. C-35 scores the presence of the bracket-notation template instruction, not whether the model correctly applies substitution downstream.

**Q2: Does the compact Yes-cell pass C-36's independence test?**
**No.** The compact Yes-cell is embedded in the `[TOKEN] required?` column — its meaning as a propagation declaration is context-dependent. Read in isolation without the column header, the cell does not independently carry the full propagation contract. C-36 requires structural independence; the compact Yes-cell provides structural dependence on the column header. V-04 (99.643) vs. V-05 (100.000) cleanly separates on this.

**Q3: Do V-01 (verbatim cells) and V-02 (architecture block) produce different compliance patterns?**
Both score identically (98.929) but test orthogonal mechanisms — V-01 tests whether verbatim vocabulary eliminates manifest interpretation overhead; V-02 tests whether a pre-manifest prose primer reduces manifest drift. Both are single-axis and cannot be ranked against each other on score alone.

---

## Excellence Signals — V-05

Four mutually reinforcing structural layers in V-05 that single-axis variations cannot achieve individually:

1. **Dedicated propagation row as dual-layer independence enabler** — The R11 V-02 form in GATE-0 REQUIRED OUTPUTS creates a standalone propagation declaration artifact separate from the required-status column. This is the only form that passes C-36's independence test; compact Yes-cell is structurally insufficient regardless of what the manifest carries.

2. **Bracket-notation manifest header extends substitution lifecycle to manifest scope** — `[TOKEN] propagation` in the manifest header makes the manifest a participant in the same substitution contract as REQUIRED OUTPUTS tables. A model that correctly substitutes the committed value demonstrates manifest-wide substitution understanding; a model that outputs `[TOKEN]` literally reveals the limitation.

3. **Verbatim vocabulary in manifest cells pre-answers the operative test** — "Declaration site" / "Substitution/inheritance site" cells can be matched against the C-32 operative test phrasing without any translation step. This is the highest-reliability C-32 form: model compliance probability is maximized because the label IS the test answer.

4. **Pre-manifest architecture prose primes both structural layers** — The TOKEN-PROPAGATION ARCHITECTURE block before the manifest table provides a fallback legibility layer independent of manifest column content and GATE-0 table content. Under model drift that corrupts manifest cells or GATE-0 output, the architecture block remains readable. The block also primes the model to produce correct content in both subsequent layers.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dedicated-propagation-row-achieves-c36-independence-compact-yes-cell-cannot", "bracket-notation-manifest-header-extends-substitution-lifecycle-to-manifest-scope", "verbatim-rubric-vocabulary-in-manifest-cells-pre-answers-operative-test-without-inference", "pre-manifest-architecture-prose-primes-both-structural-layers-and-provides-drift-fallback"]}
```
