Looking at the scorecard, I'll extract three distinct excellence patterns from the 100-scoring variants:

- **V-03**: Criterion IDs embedded inline at the element level (`C-01a`, `C-03: never skip`) — rubric satisfaction auditable without cross-referencing
- **V-04**: Symmetric interleaving — both A→B and B→A orderings described for at least one concurrent pair; exclusive role ownership with gate enforcement
- **V-05**: Invariant derivation pipeline — forward trace rows cross-referenced as invariant candidates, showing how observed transitions generate declared invariants

These are all structurally distinct from C-08 (which only requires one interleaving named) and C-07 (non-trivial invariants), so they qualify as new aspirational criteria.

---

## trace-state rubric (v18)

**5 essential + 3 recommended + 5 aspirational = 13 criteria**

### Essential (all must pass, 60 pts)
| ID | Criterion |
|----|-----------|
| C-01 | State Transition Completeness — every operation shows starting state, operation, ending state |
| C-02 | Precondition + Postcondition per operation (explicit, even if "none") |
| C-03 | Two+ domain-meaningful invariants declared and checked after every operation |
| C-04 | At least one labeled defect: type, triggering operation, reason |
| C-05 | Domain plausibility — states/ops recognizable in Sales / CS / Finance |

### Recommended (30 pts)
| ID | Criterion |
|----|-----------|
| C-06 | Consistent trace format — uniform table or numbered steps throughout |
| C-07 | Non-trivial invariants — encode real business rules, not generic structural ones |
| C-08 | Race condition analysis — one concurrent interleaving with conflict or resolution named |

### Aspirational (10 pts — 2 pts each)
| ID | Criterion |
|----|-----------|
| C-09 | Negative path trace — one rejected operation with all four elements (invalid state, blocked op, unchanged state, named error) |
| C-10 | Reachability annotation — every omitted transition listed with rationale; silent omissions do not qualify |
| C-11 | Inline criterion anchoring — output format embeds rubric criterion IDs at individual elements (e.g., field labels carry IDs like `C-01a`, `C-03: never skip`), making satisfaction auditable at the element level without cross-referencing |
| C-12 | Symmetric interleaving — race condition section describes both orderings (A→B **and** B→A) for at least one concurrent operation pair, surfacing asymmetric conflict outcomes that single-direction analysis misses |
| C-13 | Invariant derivation pipeline — forward trace rows are cross-referenced as invariant candidates with explicit linkage, showing how observed business transitions generate declared invariants rather than declaring invariants independently |

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

**Scoring notes for v18:**

- C-11 is earned only when criterion IDs appear as *field labels or inline annotations inside the output format itself*, not merely in section headings or surrounding prose.
- C-12 requires *both* orderings explicitly described; naming one interleaving and noting "the reverse is symmetric" does not qualify.
- C-13 requires a visible cross-reference (e.g., row ref, stage ref, or explicit linkage note) between a trace row and a declared invariant — derivation must be traceable, not implied.
- C-09 and C-10 remain at their v17 definitions; no scoring change.
