# R19 Scoring — `discover-competitors-alt` (Rubric v18)

## Baseline Assumption

R18 achieved 100.000 (V-03 and V-05 tied). All 38 aspirational criteria satisfied. R19 tests two form boundaries (C-45 and C-46) and robustness under framing/compression/register changes. Criteria C-01–C-44 are baseline-PASS for all five variations unless a variation axis explicitly touches them.

---

## Decisive Criteria — Boundary Analysis

### C-45 for V-01: Roman Numeral Annotations `(i)–(iv)`

**Pass condition:** Each checklist item carries an explicit element-index annotation making its single C-42 element assignment verifiable from the item label alone, without reading item content.

**V-01 evidence:**

1. The preamble explicitly declares: *"Element-index annotations use Roman numeral form — `(i)`, `(ii)`, `(iii)`, `(iv)` — forming a unified {i, ii, iii, iv} four-position set; reading only the four annotations confirms four distinct positions each appearing exactly once."*
2. Each item label prefix is a structurally distinct `(i)` / `(ii)` / `(iii)` / `(iv)` marker.
3. The preamble maps the four Roman numerals to a four-position index — the annotations function as element-indices by prior declaration, not by convention alone.
4. The C-45 pass condition says "explicit element-index annotation" — the preamble's declaration makes the Roman numerals *explicit* element indices. Without the preamble they might be ambiguous; with it, they are unambiguous.
5. The "or equivalent" clause applies: Arabic `(1)`, `(E1)`, `[Element 1]`, and `Item 1 —` all serve the same annotation function. Roman numerals `(i)–(iv)` serve the same function when declared as element-indices.
6. The operative C-45 test is annotation-verifiability without content parsing. Four annotations, each appearing exactly once, each uniquely identifying a position → bijection verifiable from annotations alone.

**Verdict: C-45 PASS.** Roman numeral form satisfies "or equivalent." The preamble declaration anchors the mapping, making the test pass on annotation-label evidence alone.

---

### C-46 for V-02: Table-Format Bijective Preamble

**Pass condition:** The bijective cardinality constraint is explicitly pre-declared as an architectural preamble before the checklist items begin.

**V-02 evidence:**

1. The 2-row native markdown table appears before the four checklist items:

   ```
   | Required item count    | Exactly 4 |
   | C-42 elements per item | Exactly 1 |
   ```

2. Both cardinality conditions are explicitly declared: item count = 4, elements per item = 1.
3. These two conditions together constitute the bijective constraint: 4 items × 1 element each = 4 elements, bijection by construction.
4. The table is structurally prior to the checklist — it is a "declared-contract" in the C-34/C-19 sense.
5. C-46 says "architecturally distinct preamble statement" — it does not restrict form to prose (unlike C-34, which says "prose artifact"). C-46 says only "preamble." A table IS a structurally distinct artifact.
6. C-34 explicitly required "prose artifact." C-46 does not. The omission is meaningful — the criterion tests declaration, not prose form.
7. A table is structurally more explicit than prose: rows are machine-verifiable declarations, not inferrable from prose flow.

**Verdict: C-46 PASS.** Table format satisfies "architecturally distinct preamble statement." Declaration is explicit, structurally prior, and covers both cardinality conditions.

---

## Per-Variation Scoring

### V-01 — Roman Numeral Element-Index Annotations

| Band | Criteria | Score | Notes |
|------|----------|-------|-------|
| Essential | C-01 to C-05 | 60/60 | All pass — template instructs C0-first, 3+ competitors, row-0, grounded findings, AMEND |
| Recommended | C-06 to C-08 | 30/30 | Mechanism-level inertia, WebSearch citation, AMEND input-output pairs |
| Aspirational C-09–C-44 | 36 criteria | 36 × 0.263 = 9.468 | Baseline R18 pass — no axis changes in these criteria |
| C-45 | Annotations | **0.263** | **PASS** — Roman numeral `(i)–(iv)` satisfies "or equivalent"; preamble declaration makes mapping explicit |
| C-46 | Preamble | 0.263 | PASS — prose preamble form (same as R18) |

**Composite: 100.000**

---

### V-02 — Table-Format Bijective Preamble

| Band | Criteria | Score | Notes |
|------|----------|-------|-------|
| Essential | C-01 to C-05 | 60/60 | All pass |
| Recommended | C-06 to C-08 | 30/30 | All pass |
| Aspirational C-09–C-44 | 36 criteria | 9.468 | Baseline R18 pass |
| C-45 | Annotations | 0.263 | PASS — `(Element N)` retained |
| C-46 | Preamble | **0.263** | **PASS** — 2-row native table explicitly declares both cardinality conditions before checklist; "or equivalent" applies since C-46 does not restrict to prose |

**Composite: 100.000**

---

### V-03 — Inertia-Forward Framing

| Band | Criteria | Score | Notes |
|------|----------|-------|-------|
| Essential | C-01 to C-05 | 60/60 | All pass |
| Recommended | C-06 to C-08 | 30/30 | All pass — inertia-forward framing strengthens C-06 and C-12 |
| Aspirational C-09–C-44 | 36 criteria | 9.468 | Baseline pass; C-11 (inertia propagates downstream) is strengthened by `vs [TOKEN]:` as first finding line |
| C-45 | Annotations | 0.263 | PASS — architecture block unchanged (R18 form) |
| C-46 | Preamble | 0.263 | PASS — preamble unchanged |

No boundary cases introduced. TOKEN centrality only benefits C-11, C-12, C-14.

**Composite: 100.000**

---

### V-04 — Compact Architecture Block

| Band | Criteria | Score | Notes |
|------|----------|-------|-------|
| Essential | C-01 to C-05 | 60/60 | All pass |
| Recommended | C-06 to C-08 | 30/30 | All pass |
| C-38 | Both artifact names | 0.263 | PASS — description confirms both artifact names preserved in compressed form |
| C-39 | Verbatim phrases | 0.263 | PASS — description confirms "Declaration site" and "Substitution/inheritance site" preserved |
| C-42 | All four elements | 0.263 | PASS — description confirms all four C-42 elements readable in single-sentence compressed items |
| C-45 | Annotations | 0.263 | PASS — annotations retained alongside compression |
| C-46 | Preamble | 0.263 | PASS — preamble retained |
| Remaining aspirational | 33 criteria | 8.679 | Baseline pass |

Compression risk criteria (C-38, C-39, C-42) explicitly confirmed by variation description: "while preserving all four C-42 elements (both artifact names + both verbatim phrases)."

**Composite: 100.000**

---

### V-05 — Combined: Conversational Register + `(Ei)` + Bijective Preamble

| Band | Criteria | Score | Notes |
|------|----------|-------|-------|
| Essential | C-01 to C-05 | 60/60 | All pass — structural requirements met regardless of register |
| Recommended | C-06 to C-08 | 30/30 | All pass |
| C-22 | Naive-reader AMEND component names | 0.263 | PASS — description explicitly notes C-22 risk mitigated: "AMEND component names kept domain-neutral" |
| C-24 | Manifest as native table | 0.263 | PASS — EXECUTION PLAN retains native markdown |
| C-28 | REQUIRED OUTPUTS as native table | 0.263 | PASS — REQUIRED OUTPUTS tables retained |
| C-45 | Annotations | 0.263 | PASS — `(Ei)` form retained |
| C-46 | Preamble | 0.263 | PASS — bijective preamble retained in conversational prose |
| Remaining aspirational | 33 criteria | 8.679 | Baseline pass — conversational register does not affect structural criteria |

Conversational register risk: register shift only applies to instructional prose, not to table structure, component labels, or preamble declarations. Architecture block retains both verbatim phrases in conversational prose form.

**Composite: 100.000**

---

## Summary Table

| Variation | Axis | C-45 | C-46 | Composite |
|-----------|------|------|------|-----------|
| V-01 | Roman numeral `(i)–(iv)` annotations | **PASS** — equiv. accepted | PASS | **100.000** |
| V-02 | Table-format bijective preamble | PASS | **PASS** — table form accepted | **100.000** |
| V-03 | Inertia-forward framing | PASS | PASS | **100.000** |
| V-04 | Compressed architecture block | PASS | PASS | **100.000** |
| V-05 | Register + Ei + bijective preamble | PASS | PASS | **100.000** |

**All five variations score 100.000. All essential criteria pass in all variations.**

---

## Ranking

All five variations are tied at 100.000. Rank by robustness evidence:

1. **V-05** (100.000) — Strongest evidence: combined stress test (register + annotation + preamble form) with explicit C-22 mitigation. Most dimensions tested simultaneously.
2. **V-03** (100.000) — Inertia-forward framing strengthens C-11/C-12/C-14 propagation; clean single-axis with no risk surface.
3. **V-01** (100.000) — Establishes Roman numeral as third annotation equivalent; preamble anchors the mapping.
4. **V-02** (100.000) — Establishes table as valid preamble form; `(Element N)` retained as stable anchor.
5. **V-04** (100.000) — Compression risk explicitly mitigated in description; single-axis with confirmed element preservation.

---

## Excellence Signals

**From V-01:** Preamble-anchored annotation equivalence. Roman numeral `(i)–(iv)` satisfies C-45 because the *preamble* declares the mapping — the annotation itself is the index label, and the preamble makes it explicit. Pattern: annotation form boundaries are unlocked by prior-declaration architecture, not by the annotation label alone.

**From V-02:** Table-form preamble satisfies declaration criteria when the criterion does not restrict to prose. C-46 says "preamble" (not "prose block"); the table form is *more* machine-verifiable than prose. Pattern: format restrictions must be stated explicitly in a criterion to be binding — absent restriction, the more structured form passes.

**From V-05:** Register isolation. Full conversational register does not penetrate structural criteria (table format, component labels, verbatim phrases) when the template explicitly preserves those elements. Pattern: register is a surface property; structural compliance is structural.

**From V-03:** Inertia-forward framing yields no regressions and strengthens C-11/C-12/C-14 by making TOKEN the explicit primary anchor in every gate template. Pattern: strengthening propagation declarations never costs other criteria.

---

```json
{"top_score": 100.000, "all_essential_pass": true, "new_patterns": ["Roman numeral (i)-(iv) satisfies C-45 'or equivalent' when preamble declares the four-position index mapping explicitly", "Table-format preamble satisfies C-46 when criterion specifies 'preamble' but not 'prose' — more structured form passes absent explicit format restriction", "Conversational register does not penetrate structural compliance criteria when template explicitly preserves table format, verbatim phrases, and component labels"]}
```
