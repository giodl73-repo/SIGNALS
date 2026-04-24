Here are the five complete R7 variations, written to `simulations/quest/golden/flow-ratelimit-variate-R7-2026-03-17.md`:

---

**R7 target criteria**: C-24 (Terminal Document-Close Reconciler) and C-25 (Two-Tier Violation Taxonomy in Format Contract)

| Variation | Axis | Key hypothesis | C-24 | C-25 | C-22 expected |
|-----------|------|---------------|------|------|---------------|
| **V-01** | Role sequence | Terminal reconciler (Role 11) catches REVISED marker gaps and DERIVATION CHAIN violations that incomplete per-gate coverage misses | PASS | FAIL | PARTIAL (3-4/9) |
| **V-02** | Output format | Named STRUCTURAL vs CONTENT clauses with different detection methods (scan-time / read-time) and different remediations remove ambiguity about which applies | FAIL | PASS | FAIL (no gate chain) |
| **V-03** | Lifecycle emphasis | Per-phase exit conditions carrying Verdict-currency instructions enforce C-22 at production time; terminal reconciler verifies but doesn't substitute for forward enforcement | PASS | PASS (Preamble B) | PASS (all 8 transitions) |
| **V-04** | V-01 + V-02 | Terminal reconciler + two-tier taxonomy + full gate chain target C-24/C-25/C-21 simultaneously; each mechanism blocks a distinct failure mode | PASS | PASS | PARTIAL (5-6/9) |
| **V-05** | All five | INERTIA framing forces INERTIA-delta proofs in DERIVATION CHAIN cells; per-role COLUMN COMPLIANCE annotations prevent false schema violations on non-table roles; per-gate currency at every transition | PASS | PASS | PASS (all roles) |

**Structural decisions to note**:

- V-01's Role 11 terminal reconciler adds a dedicated `(c) Format Contract Taxonomy Audit` check — this makes the reconciler a witness to C-25 compliance even though V-01 doesn't enforce C-25 in its Format Contract. This tests whether the reconciler can detect a two-tier taxonomy *absence* retroactively.
- V-02 is section-based (no gate chain beyond preambles), reproducing the R6 V-02 pattern that failed C-17/C-21/C-22. This isolates C-25 as the single contribution.
- V-03's Phase 7 terminal reconciler adds step `(c) Rejection Clause Audit` — verifying the Format Contract declared two named types. Since V-03 *does* include the two-tier taxonomy (Preamble B), the reconciler confirms it rather than detecting its absence.
- V-05 adds three V-05-specific mechanisms from R6: INERTIA as named competitor column, INERTIA-delta rule as a DERIVATION CHAIN analytical requirement, and per-role COLUMN COMPLIANCE annotations preventing the STRUCTURAL REJECTION CLAUSE from generating false violations on hop-chain and prose roles.
