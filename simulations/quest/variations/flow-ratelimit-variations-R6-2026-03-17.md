**R6 variations written** to `simulations/quest/golden/flow-ratelimit-variate-R6-2026-03-17.md`.

---

## Summary

**Variation axes selected:**
- V-01/V-04: Role sequence (single / combined)
- V-02/V-03: Output format / schema-column (single / imperative register variant)
- V-05: Full integration

**Five complete variations — what each explores:**

| Var | Axis | Key C-23 mechanism | Hypothesis |
|-----|------|--------------------|------------|
| **V-01** | Role sequence — full gate chain | Rejection Clause C in Format Contract declares DERIVATION CHAIN as a named mandatory column | Gate-level enforcement at each role transition makes column presence a gate-blocking condition, not just a content advisory |
| **V-02** | Output format — schema-column as primary structural discipline | DERIVATION CHAIN declared as the 4th column in the schema line with STRUCTURAL REJECTION CLAUSE | Schema declaration is global and scan-visible — a missing column is a structural omission, not a prose-level content gap |
| **V-03** | Phrasing register — imperative per-section column compliance commands | `COLUMN REQUIRED: DERIVATION CHAIN` repeated at each section header containing a table | Per-section commands prevent "forgotten preamble" failure mode; tests whether local vs. global Format Contract placement changes compliance rates |
| **V-04** | Role sequence + schema-column combined (C-21 + C-23) | Full gate chain + FORMAT CONTRACT four-column schema with schema + content rejection clauses | Gate closure prevents section-skipping; schema column prevents table omission — two orthogonal failure modes blocked by different mechanisms |
| **V-05** | Full integration — all five axes | Four-column schema with INERTIA replacing BASELINE; INERTIA-delta rule in DERIVATION CHAIN; per-role Verdict currency; per-section column commands | Compound reinforcement: each axis blocks a distinct failure mode; INERTIA framing forces derivation to prove the mitigation beats the status-quo competitor |

**C-23-specific design decision across all five:** V-01 uses Rejection Clause C (schema column declared as a third named clause), V-02 makes DERIVATION CHAIN the named 4th column in the schema declaration line itself with a dedicated STRUCTURAL REJECTION CLAUSE, V-03 uses per-section imperative commands, V-04 combines V-01's gate chain with V-02's schema declaration, and V-05 adds the INERTIA-delta rule which makes the DERIVATION CHAIN column carry an additional analytical requirement (prove the delta from inertia, not just show arithmetic).
