Written to `simulations/quest/golden/trace-inspect-variate-R10-2026-03-17.md`.

---

# trace-inspect -- Variations v6 R10 (2026-03-17)

**Entry state**: R9 V-05 at 99.5/99.5 (all C-01–C-21 PASS). Rubric v6 adds C-22 + C-23 at 0.5 pts each. Grand total 100.5. Entry score for any R10 variant that adds nothing new: 99.5/100.5.

---

## Variation axes

**C-22** (enforcement class annotation): Each invariant in the Coverage Matrix declares whether its enforcement is `architectural` (named structural gate blocks advancement; violation impossible in a conformant trace) or `instructional` (vocabulary/format rule; violations detectable in compliance ledger but not structurally blocked).

**C-23** (Phase 2a/2b role membership enumerated): EG-FIRST EXECUTION CONSTRAINT block restructured so PHASE 2a MEMBERSHIP and PHASE 2b MEMBERSHIP are explicit named role lists — not pointers to the Role-Schema Binding Summary — making phase assignment auditable from the constraint block alone.

---

## Variation summary

| Variation | Axis | Hypothesis |
|---|---|---|
| **V-01** | C-22 via Coverage Matrix column | Enforcement class column makes per-invariant annotation machine-checkable from one table; schema descriptions gain `[enforcement: X]` suffix for co-located redundancy |
| **V-02** | C-23 via standalone membership blocks | PHASE 2a/2b MEMBERSHIP sub-blocks with explicit role names + count + total check; EG-RELAY COMPLETE cites MEMBERSHIP counts; VC-4 G-1 attribution confirms role names against membership declaration |
| **V-03** | C-22 via inline suffix (different format axis) | `[enforcement: architectural/instructional]` suffix on every named invariant at every definition site across all phases; distributes annotation rather than centralizing it; richer per-use-site coverage at cost of repetition |
| **V-04** | C-22 column + C-23 | V-01 + V-02 combined; the two mechanisms are orthogonal and don't conflict |
| **V-05** | C-22 + C-23 + v6 registry + cross-reference | Full integration: CRITERION INHERITANCE REGISTRY updated to v6 with C-22/C-23 as NEW with mechanism descriptions; EG-FIRST structural invariant cross-references Coverage Matrix enforcement class column; VC-4 G-1 attribution validates C-23 membership counts |

---

## Predicted scores under rubric v6

| Variation | C-22 | C-23 | All essential | Predicted score |
|---|---|---|---|---|
| V-01 | PASS | FAIL | YES | 100.0 / 100.5 |
| V-02 | FAIL | PASS | YES | 100.0 / 100.5 |
| V-03 | PASS (alt format) | FAIL | YES | 100.0 / 100.5 |
| V-04 | PASS | PASS | YES | 100.5 / 100.5 |
| V-05 | PASS | PASS | YES | 100.5 / 100.5 |

V-04 and V-05 both target perfect score. V-05 adds three integration gains not captured by V-04: (1) CRITERION INHERITANCE REGISTRY v6 with C-22/C-23 mechanism descriptions, (2) cross-reference between the EG-FIRST constraint invariant and the Coverage Matrix Enforcement class column, (3) VC-4 G-1 attribution count-check validates C-23 MEMBERSHIP declarations — creating structural linkage between the two new criteria.
