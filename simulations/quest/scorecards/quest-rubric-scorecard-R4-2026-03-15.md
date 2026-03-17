---

# Quest Score — quest-rubric / Round 4

**Rubric**: v4 | **Scoring**: V-01 and V-02 only (V-03–V-05 not drafted)

---

## Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? |
|------|-----------|-----------|-------------|--------------|-----------|---------|
| 1 | V-01 Schema-First | 5/5 PASS | 2.5/3 | 3.5/8 | **89.4** | YES |
| 2 | V-02 Specificity-Conversion | 4/5 (partials) | 2/3 | 4.5/8 | **73.6** | NO |

---

## Criterion Cross-Reference

| Criterion | V-01 | V-02 | Key Discriminator |
|-----------|------|------|-------------------|
| C-01 | PASS | PARTIAL | Frontmatter template in V-01; none in V-02 |
| C-02 | PASS | PASS | — |
| C-03 | PASS | PARTIAL | V-01 prohibition list covers all criteria; V-02 covers specificity only |
| C-04 | PASS | PASS | — |
| C-05 | PASS | PASS | — |
| C-06 | PASS | PASS | — |
| C-07 | **PARTIAL** | **PASS** | V-02 CONVERSION-MAP produces output-testable criteria; V-01 prohibition stays a prohibition |
| C-08 | PASS | FAIL | V-01 SCHEMA declares date/version; V-02 has none |
| C-09 | PARTIAL | PARTIAL | Universal partial — no per-section mandate in either |
| C-10 | FAIL | FAIL | Universal miss — binary formula in both |
| C-11 | PASS | PASS | Different mechanisms: phrase checklist vs. DO NOT proceed gates |
| C-12 | PASS | PASS | Both sequence failure modes before criteria |
| C-13 | FAIL | **PASS** | V-02 CONVERSION-MAP three-way contrast; V-01 has no foil pair |
| C-14 | FAIL | FAIL | Universal miss — closed enumeration absent in both |
| C-15 | **FAIL** | **PASS** | V-02's axis; V-01 does not convert specificity prohibitions |
| C-16 | **PASS** | **FAIL** | V-01's axis; V-02 has no SCHEMA block |

---

## Why V-01 Beats V-02 Despite C-15 Fail

**F-01 finding**: C-16 is load-bearing at the essential tier. V-02's absent frontmatter template causes **three failures** — C-01 PARTIAL (unanchored skill identity), C-08 FAIL (no date/version), C-16 FAIL (no structural home). The essential partial costs 12 points alone, outweighing V-02's wins on C-07, C-13, C-15. The SCHEMA BLOCK is a multiplier pattern: one structural declaration prevents cascading failures across three criteria.

**F-03 structural prediction**: V-04 (combined SCHEMA BLOCK + CONVERSION-MAP) would inherit PASS on C-01, C-03, C-07, C-08, C-11, C-12, C-13, C-15, C-16 — a predicted 5/5 essential, 3/3 recommended, 6/8 aspirational = **97.5**. The two universal misses (C-10, C-14) persist regardless of combination.

---

## Excellence Signals

**E-1 — SCHEMA BLOCK makes C-16 a structural pre-condition, not an audit**: Requiring the SCHEMA as the *first section of the artifact* converts unanchored field declarations from a detectable error into an impossible one. Absence in SCHEMA = structural error before Phase 2 begins.

**E-2 — CONVERSION-MAP boolean triplet is the only C-15 mechanism found**: The three booleans (`is_prohibition`, `is_input_analysis`, `conversion_complete`) plus `DO NOT proceed` gate force reclassification of every specificity element until it satisfies "testable property of the output artifact." Across all four rounds, this is the only pattern that achieves C-15 PASS.

**Persistent gaps**: C-10 (partial credit in formula), C-14 (closed category enumeration), C-13 for V-01 (foil pair absent).

---

```json
{"top_score": 89.4, "all_essential_pass": true, "new_patterns": ["SCHEMA BLOCK converts required-field anchoring from post-hoc audit to pre-Phase structural declaration: unanchored field absence is a structural error visible before content is written, eliminating C-16 failures cascading into C-01 and C-08", "CONVERSION-MAP boolean triplet (is_prohibition / is_input_analysis / conversion_complete) with DO NOT proceed gate is the only mechanism that converts specificity prohibitions into output-testable criteria, achieving C-15 PASS"]}
```
