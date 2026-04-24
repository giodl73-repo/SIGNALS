Written to `simulations/quest/golden/crew-review-variate-R10-2026-03-16.md`.

---

# crew-review -- Variate R10

**R9 gap analysis**: V-01 R9 scored 161.25/162.5 -- C-27 PARTIAL because R3 text stayed minimum-count ("name at least one convergence or conflict") even though the criterion-check table's C-27 row created revision pressure. Under v9, C-28 is now aspirational, so the criterion-check table must also include a C-28 row.

**Design changes across R10:**

| Variation | Axis | Key change from R9 |
|-----------|------|-------------------|
| V-01 | Lifecycle emphasis | V-01 R9 + explicit R3 per-slot contract + 5-column criterion-check table through C-28 |
| V-02 | Output format | V-02 R9 + criterion-check table extended to C-28 with full per-row remediation |
| V-03 | Lifecycle (variant) | New: PHASE 3.5 -- SYNTHESIZE with G2 gate; synthesis completeness enforced structurally, not contractually |
| V-04 | Lifecycle + Output format | V-01 + V-02 merged; synthesis contract in both schema section AND R3 text |
| V-05 | Lifecycle + Output format + Role sequence | V-04 + verbatim `expertise.relevance` quotes (V-03 R9 pattern) |

**Critical structural change**: V-01, V-02, V-04, V-05 all use a **5-column criterion-check table** -- the 5th column is `Remediation if NO`, with a specific return-to-phase instruction for every row. This resolves the C-28 gap at the design level (not via a footer instruction).

**V-03** introduces the only architecture change: a new PHASE 3.5 -- SYNTHESIZE with Gate G2. G2 closure predicate requires every manifest slot to have exactly one verdict before VALIDATE runs. C-27 becomes a gate condition rather than a render contract -- a potential C-29 candidate.

**Predicted scores under v9**: V-01, V-02, V-03, V-04, V-05 all predicted at **162.5/162.5**. The question for scoring is whether any variation misses a nuance in C-28 (e.g., "every row" vs. "at least one row") or whether V-03's G2 gate satisfies C-27 with a different evidence signature.
