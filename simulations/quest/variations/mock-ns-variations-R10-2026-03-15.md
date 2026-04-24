Written to `simulations/quest/golden/mock-ns-variate-R10-2026-03-15.md`.

---

## R10 Summary

**New criteria targeted**: C-27 (structural isolation of guarantee-break and cross-site as independently scannable units) and C-28 (navigation-anchored cross-reference). Aspirational denominator 20.

**Variation axes** — 3 single-axis, 2 combined:

| V | Axis | Key structural change |
|---|------|-----------------------|
| V-01 | Output format (bidirectionality) | A-1 Failure consequence row labels itself as the target of S-3 Cross-site reference. Forward anchor already present from R9 V-02; V-01 closes the loop. |
| V-02 | Phrasing register (bracket anchors) | `[A-1:FC]` at S-3 and `[S-3:CS]` at A-1 replace prose phrases. Bracket tokens are visually distinct -- harder to absorb without processing than embedded clauses. |
| V-03 | Output format (paragraph isolation) | Bold-header paragraph blocks replace table rows. Tests whether C-27's "independently scannable unit" requirement is satisfied as reliably by paragraph headers as by table-row cell boundaries. |
| V-04 | Format + bidirectionality | R9 V-02 table + V-01 back-ref. Both isolation (C-27) and navigability (C-28 aspirational max) in one structure. |
| V-05 | Format + register + stated protocol | Full table + bracket anchors + a preamble that names the cross-reference design as an explicit protocol before the first row. Tests whether the meta-declaration changes how the executor processes the chain. |

**R10 discriminant**: All five variants attempt all 28 criteria. The question is not coverage -- it is which structural form (prose back-refs / bracket tokens / paragraph blocks / stated protocol) produces the most robust C-27/C-28 adherence under execution pressure.

**v10 signal seeded**: If V-05's stated-protocol preamble outperforms V-04's identical structure without it, C-29 (stated cross-reference protocol) becomes a v10 candidate criterion.
