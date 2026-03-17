Written to `simulations/quest/golden/crew-review-variate-R8-2026-03-16.md`.

---

**R8 design summary -- what changed from R7:**

R7 V-05 achieved a perfect 155.0. The meta-completeness gap it left: its criterion-check table covers C-11 through C-23, but C-24 and C-25 (the two criteria V-05 itself introduced) are not in the table.

**Three single-axis variations, then two combinations:**

| Variation | Axis | New pattern hypothesis | C-candidate |
|-----------|------|----------------------|-------------|
| V-01 | Lifecycle emphasis | Criterion-check table covers ALL aspirational criteria through current rubric version, including C-24 and C-25 (self-complete) | C-26 |
| V-02 | Output format | Synthesis provides per-slot convergence/conflict/unique verdict for every slot -- exhaustive slot-anchored synthesis, not minimum-count | C-27 |
| V-03 | Role sequence | Manifest non-challenger entries carry verbatim `expertise.relevance` field quote from registry file -- falsifiable selection evidence | C-28 |
| V-04 | V-01 + V-02 | Criterion-check self-inclusion + per-slot synthesis | C-26 + C-27 |
| V-05 | V-01 + V-02 + V-03 + new | All three + severity calibration protocol declared pre-execution (artifact-type-aware severity contract before any row is written) | C-26 + C-27 + C-28 + C-29 |

**V-05 R8 introduces the severity calibration protocol** -- a pre-execution table that maps finding type to expected severity, with an exception-note rule for deviations. Analogous to how the output schema declares column contracts before execution, the calibration protocol declares the interpretive contract for severity before assignment begins.
