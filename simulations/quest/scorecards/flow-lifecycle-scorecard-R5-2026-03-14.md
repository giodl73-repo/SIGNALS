---

# Scorecard -- flow-lifecycle Round 5 (v5 Rubric)

## Base Assessment

All R5 variations inherit the V-05 R4 base (13/13 aspirational pass, 100.00). The only changes are placement of the C-22 format contract and C-23 anti-embedding instruction.

**C-01 through C-21:** PASS all variations (unchanged from V-05 R4).

---

## C-22 -- Evidence Field Format Contract

The key diagnostic: does a bracket template in a per-block hint (`[State name -- S-ID]: AT-RISK, causal source: B-[ID]`) satisfy C-22?

**No.** C-22 requires a *concrete named domain example* (`S-05: Credit Hold Review -- AT-RISK, causal source: B-01`) plus an explicit *preamble-level* fail condition. A bracket template satisfies C-19 (format structure is recognizable) but not C-22 (which requires a filled-in example anchored in the global preamble).

| V | Concrete named example | Preamble fail condition | C-22 |
|---|------------------------|------------------------|------|
| V-01 | NO -- bracket template with placeholders | NO -- in per-block hint only | **FAIL** |
| V-02 | YES -- preamble: `S-05: Credit Hold Review -- AT-RISK, causal source: B-01` | YES -- preamble | **PASS** |
| V-03 | YES -- preserved V-05 R4 preamble form | YES -- preamble | **PASS** |
| V-04 | NO -- bracket template with placeholders | NO -- in per-block hint only | **FAIL** |
| V-05 | YES -- preamble + per-block both concrete | YES -- preamble + per-block | **PASS** |

---

## C-23 -- Chain Status Section Isolation

**Symmetric result:** all four placement forms pass. Section-proximate anti-embedding (V-03/V-04) is fully sufficient; global preamble (V-01/V-02) is fully sufficient; both together (V-05) is strongest.

C-23: **PASS all variations.**

---

## Final Scores

| Rank | V | Essential | Recommended | Aspirational | Composite | Fails |
|------|---|-----------|-------------|--------------|-----------|-------|
| 1 (tie) | **V-02** | 60 | 30 | 15/15 = 10.00 | **100.00** | none |
| 1 (tie) | **V-03** | 60 | 30 | 15/15 = 10.00 | **100.00** | none |
| 1 (tie) | **V-05** | 60 | 30 | 15/15 = 10.00 | **100.00** | none (golden) |
| 4 (tie) | V-01 | 60 | 30 | 14/15 = 9.33 | **99.33** | C-22 |
| 4 (tie) | V-04 | 60 | 30 | 14/15 = 9.33 | **99.33** | C-22 |

**V-05 designated golden** for maximum structural redundancy (both C-22 locations, both C-23 locations).

---

## Excellence Signals

1. **Preamble-level concrete named example is the C-22 load-bearing element** -- a bracket template satisfies C-19 (structure) but not C-22 (contract). Filled-in domain example + preamble fail condition are required; proximity in the block hint is insufficient.

2. **Section-proximate anti-embedding is equivalent to global-preamble for C-23** -- the anti-embedding instruction can live inside the CHAIN STATUS section instruction as its opening constraint; global preamble distance is not required.

3. **C-19 and C-22 are separable by content type** -- structure and contract are independent axes. Getting the format structure right (C-19) does not automatically satisfy the format contract (C-22).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Preamble-level concrete named example is the C-22 load-bearing element -- bracket template in per-block hints passes C-19 (format structure) but fails C-22 (format contract requires a filled-in domain example and preamble fail condition)", "Section-proximate anti-embedding is equivalent to global-preamble for C-23 -- anti-embedding instruction placed as the opening constraint of the CHAIN STATUS section instruction fully satisfies the criterion; preamble distance is not required", "C-19 and C-22 are separable by content type -- structure (C-19) and contract (C-22) are independent axes; a bracket template satisfies structure but not contract; both axes are needed for the strongest Evidence field enforcement"]}
```
ISK SLA
rows* that cite this B-ID. Fail if the field is a general reference without row-level specificity.

R4's V-01/V-03 failed C-19 with hint `[AT-RISK entries that list "causal source: B-01" in SLA
ANALYSIS]` -- no format, no specificity anchor. R5's V-01/V-04 use bracket template
`[State name -- S-ID]: AT-RISK, causal source: B-[ID]` which encodes the exact field-level format
structure (state name + S-ID + AT-RISK tag + causal source B-ID). This is qualitatively more
concrete than R4's vague description and sufficient for C-19 even without a concrete filled-in
example.

| V | Evidence hint form | Verdict |
|---|-------------------|---------|
| V-01 | Bracket template `[State name -- S-ID]: AT-RISK, causal source: B-[ID]` + explicit fail condition in per-block hint. No preamble format contract. | PASS -- format structure explicit enough to elicit row-specific entries; more concrete than R4 V-01 |
| V-02 | Preamble: concrete named example `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` + required format + fail condition. Per-block hints are minimal references. | PASS -- preamble contract anchors required specificity |
| V-03 | Preserved from V-05 R4: preamble + per-block both with concrete examples. | PASS |
| V-04 | Bracket template + explicit fail condition in per-block hint (same C-22 axis as V-01). | PASS -- same reasoning as V-01 |
| V-05 | Preamble + per-block both with concrete examples, consistent across B-01/B-02 (R4 inconsistency corrected). | PASS |

C-19: **PASS all variations.**

---

### C-22 Evidence Field Format Contract

**Pass condition:** the Evidence sub-field hint provides (a) a concrete *named domain example*
like `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` (not a bracket template with
placeholders) and (b) an explicit *preamble* fail condition for general references.
Both elements required. C-22 cannot pass if C-19 fails.

**Distinction from C-19:** C-19 requires the Evidence field to elicit row-specific entries (format
structure sufficient). C-22 requires a concrete named domain example (filled in with real state
names and S-IDs) plus a preamble-level fail condition. A bracket template satisfies C-19 but not
C-22; the criterion's pass evidence in R4 was always a filled-in example
(`S-05: Credit Hold Review -- AT-RISK, causal source: B-01`), not a placeholder template.

| V | Concrete named example | Preamble fail condition | Verdict |
|---|------------------------|------------------------|---------|
| V-01 | NO -- bracket template uses placeholders, not a filled-in domain example | NO -- fail condition is in per-block hint, not global preamble | **FAIL** |
| V-02 | YES -- preamble: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"` | YES -- preamble: explicit fail condition for general references | **PASS** |
| V-03 | YES -- preserved V-05 R4 preamble concrete example | YES -- preamble fail condition preserved | **PASS** |
| V-04 | NO -- bracket template with placeholders (same as V-01) | NO -- fail condition in per-block hint only | **FAIL** |
| V-05 | YES -- preamble concrete example + per-block concrete examples (consistent) | YES -- preamble fail condition + per-block fail condition (both) | **PASS** |

C-22: V-01 FAIL, V-02 PASS, V-03 PASS, V-04 FAIL, V-05 PASS.

**V-01/V-04 diagnostic confirmed:** bracket template + block-level fail condition passes C-19
(format structure present) but fails C-22 (concrete named domain example required in preamble).
The two criteria are not co-satisfied by the same evidence in the block-hint-only case.

---

### C-23 Chain Status Section Isolation

**Pass condition:** CHAIN STATUS declared as the first element of a dedicated top-level section,
not embedded in SLA ANALYSIS; anti-embedding instruction present (in preamble, in section, or both).
Every C-23 pass implies C-20 pass.

All R5 variations inherit the dedicated `## CHAIN STATUS` top-level section from V-05 R4.
The only axis under test is *where* the anti-embedding instruction lives.

| V | Dedicated section | CHAIN STATUS first | Anti-embedding location | Verdict |
|---|-------------------|--------------------|------------------------|---------|
| V-01 | YES | YES | Global preamble (preserved from V-05 R4): "Do not embed chain status as a line or annotation inside the SLA ANALYSIS section." | **PASS** |
| V-02 | YES | YES | Global preamble (preserved from V-05 R4) | **PASS** |
| V-03 | YES | YES | Section instruction opening line: `STRUCTURAL CONSTRAINT: Do not embed chain status inside SLA ANALYSIS` | **PASS** |
| V-04 | YES | YES | Section instruction only (same as V-03) | **PASS** |
| V-05 | YES | YES | Global preamble + section instruction (both locations) | **PASS** |

C-23: **PASS all variations.**

**V-03/V-04 diagnostic confirmed:** section-proximate anti-embedding satisfies C-23. The criterion
requires the instruction to be *present*, not specifically in the global preamble. Placing it as
the opening constraint of the CHAIN STATUS section instruction is sufficient.

---

## Consolidated Per-Variation Scores

### V-01 -- C-22 Isolation: Block-Hint-Only Format Contract

| Tier | Pass / Total | Points |
|------|-------------|--------|
| Essential | 5/5 | 60.00 |
| Recommended | 3/3 | 30.00 |
| Aspirational | 14/15 (fails C-22) | 9.33 |
| **Composite** | | **99.33** |

All essential pass: YES. Meets golden threshold. C-22 is the only failure.

### V-02 -- C-22 Isolation: Preamble-Only Concrete Named Example

| Tier | Pass / Total | Points |
|------|-------------|--------|
| Essential | 5/5 | 60.00 |
| Recommended | 3/3 | 30.00 |
| Aspirational | 15/15 | 10.00 |
| **Composite** | | **100.00** |

All essential pass: YES. Golden.

### V-03 -- C-23 Isolation: Section-Level Anti-Embedding Only

| Tier | Pass / Total | Points |
|------|-------------|--------|
| Essential | 5/5 | 60.00 |
| Recommended | 3/3 | 30.00 |
| Aspirational | 15/15 | 10.00 |
| **Composite** | | **100.00** |

All essential pass: YES. Golden.

### V-04 -- Combined Minimum: Block-Hint C-22 + Section-Instruction C-23

| Tier | Pass / Total | Points |
|------|-------------|--------|
| Essential | 5/5 | 60.00 |
| Recommended | 3/3 | 30.00 |
| Aspirational | 14/15 (fails C-22) | 9.33 |
| **Composite** | | **99.33** |

All essential pass: YES. Meets golden threshold. C-22 is the only failure; C-23 passes at section level.

### V-05 -- Full R5 Synthesis: Dual-Location Both Criteria

| Tier | Pass / Total | Points |
|------|-------------|--------|
| Essential | 5/5 | 60.00 |
| Recommended | 3/3 | 30.00 |
| Aspirational | 15/15 | 10.00 |
| **Composite** | | **100.00** |

All essential pass: YES. Golden.

---

## Full Criterion Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 State Transition Coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 Exception Flow Identification | PASS | PASS | PASS | PASS | PASS |
| C-03 Role Assignment Accuracy | PASS | PASS | PASS | PASS | PASS |
| C-04 Bottleneck and Gap Identification | PASS | PASS | PASS | PASS | PASS |
| C-05 Terminal State Completeness | PASS | PASS | PASS | PASS | PASS |
| C-06 Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS |
| C-07 Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS |
| C-08 Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS |
| C-09 Cross-Process Interaction Modeling | PASS | PASS | PASS | PASS | PASS |
| C-10 SLA and Timing Analysis | PASS | PASS | PASS | PASS | PASS |
| C-11 Decision Supplement Block Structure | PASS | PASS | PASS | PASS | PASS |
| C-12 Role Registry Gate | PASS | PASS | PASS | PASS | PASS |
| C-13 Phase-Scoped Exception Traces | PASS | PASS | PASS | PASS | PASS |
| C-14 SLA-to-Bottleneck Evidence Chain | PASS | PASS | PASS | PASS | PASS |
| C-15 Exception-First Structural Position | PASS | PASS | PASS | PASS | PASS |
| C-16 Bidirectional SLA-Bottleneck Cross-Reference | PASS | PASS | PASS | PASS | PASS |
| C-17 Constructed-Answer Format for Exceptions | PASS | PASS | PASS | PASS | PASS |
| C-18 Ordinal-Label Structural Enforcement | PASS | PASS | PASS | PASS | PASS |
| C-19 Backward-Chain Evidence Injection | PASS | PASS | PASS | PASS | PASS |
| C-20 Chain Status Gate | PASS | PASS | PASS | PASS | PASS |
| C-21 Unified Exception-Block Architecture | PASS | PASS | PASS | PASS | PASS |
| **C-22** Evidence Field Format Contract | **FAIL** | **PASS** | **PASS** | **FAIL** | **PASS** |
| **C-23** Chain Status Section Isolation | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

---

## Ranking

| Rank | Variation | Composite | Fails |
|------|-----------|-----------|-------|
| 1 (tie) | **V-02** | **100.00** | none |
| 1 (tie) | **V-03** | **100.00** | none |
| 1 (tie) | **V-05** | **100.00** | none (golden) |
| 4 (tie) | V-01 | 99.33 | C-22 |
| 4 (tie) | V-04 | 99.33 | C-22 |

**V-05 is designated golden** among the three 100-pt variations: maximum structural redundancy
(both C-22 locations: preamble + block; both C-23 locations: preamble + section), making
enforcement dual-anchored and resilient to partial format drift.

**C-23 is symmetric:** all four non-full-synthesis forms pass (preamble-only V-01/V-02,
section-only V-03/V-04). The criterion's "anti-embedding instruction present" requirement is
satisfied by either location; neither is privileged.

**C-22 is asymmetric:** only preamble-level concrete named example satisfies it. Block-hint
bracket template alone (V-01/V-04) fails -- the placeholder form satisfies C-19 but not C-22's
stricter format contract requirement.

---

## Excellence Signals from Top-Scoring Variations

**Signal 1: Preamble-level concrete named example is the C-22 load-bearing element**
V-02 shows preamble-only with a concrete named example (`S-05: Credit Hold Review -- AT-RISK,
causal source: B-01`) passes C-22; V-01 shows per-block bracket template alone fails C-22 even
when the template is structurally explicit. The pattern: for format contracts where domain
specificity is the pass/fail axis, a concrete filled-in example in the global preamble provides
an unambiguous reference anchor that placeholder templates cannot replace. Placeholder templates
demonstrate structure; concrete examples demonstrate expected content. C-22 requires both, at
preamble level.

**Signal 2: Section-proximate anti-embedding is equivalent to global-preamble for C-23**
V-03 demonstrates that removing global preamble anti-embedding and placing the constraint inside
the CHAIN STATUS section instruction -- as its opening line -- fully satisfies C-23. The proximate
form (`STRUCTURAL CONSTRAINT: Do not embed chain status inside SLA ANALYSIS` at the top of the
CHAIN STATUS instruction block) is co-located with the gated output, which may be a stronger
enforcement form than a distant preamble rule. The pattern: isolation constraints can live at the
section they govern; global preamble distance is not required for C-23.

**Signal 3: C-19 and C-22 are separable by content type, not just strictness**
V-01 passes C-19 and fails C-22 simultaneously, establishing these criteria test different things:
C-19 tests format *structure* (can an AI infer row-specific entries from the hint?); C-22 tests
format *contract* (does the hint provide a named domain example + explicit fail condition as a
preamble-level anchor?). A bracket template satisfies the structural requirement but not the
contract requirement. Structure and contract are independent axes; getting structure right does
not automatically satisfy the contract.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Preamble-level concrete named example is the C-22 load-bearing element -- bracket template in per-block hints passes C-19 (format structure) but fails C-22 (format contract requires a filled-in domain example and preamble fail condition)", "Section-proximate anti-embedding is equivalent to global-preamble for C-23 -- anti-embedding instruction placed as the opening constraint of the CHAIN STATUS section instruction fully satisfies the criterion; preamble distance is not required", "C-19 and C-22 are separable by content type -- structure (C-19) and contract (C-22) are independent axes; a bracket template satisfies structure but not contract; both axes are needed for the strongest Evidence field enforcement"]}
```
