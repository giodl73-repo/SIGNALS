Reading the three excellence signals from V-01, mapping each to a distinct criterion slot, then producing the complete v19 rubric (outer quest rubric v3).

**New criteria:**
- **C-14**: Schema-level write-time enforcement (distinct from C-11: not just IDs present, but schema slots that make compliance structurally unavoidable)
- **C-15**: Example row with placeholder syntax (scaffold eliminates ambiguity before generation; V-01's `Step 1 / Step 2` rows)
- **C-16**: Hard no-prose-substitution constraint (named ban on narrative fallback as a declared hard rule)

Aspirational section now has 8 criteria at 2 pts each, capped at 10 — any 5 of 8 earns full aspirational credit.

---

## trace-state rubric (v19)

**5 essential + 3 recommended + 8 aspirational (cap 5) = 16 criteria**

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

### Aspirational (10 pts — 2 pts each, any 5 of 8)

| ID | Criterion |
|----|-----------|
| C-09 | Negative path trace — one rejected operation with all four elements (invalid state, blocked op, unchanged state, named error) |
| C-10 | Reachability annotation — every omitted transition listed with rationale; silent omissions do not qualify |
| C-11 | Inline criterion anchoring — output format embeds rubric criterion IDs at individual elements (e.g., field labels carry IDs like `C-01a`, `C-03: never skip`), making satisfaction auditable at the element level without cross-referencing |
| C-12 | Symmetric interleaving — race condition section describes both orderings (A→B **and** B→A) for at least one concurrent operation pair, surfacing asymmetric conflict outcomes that single-direction analysis misses |
| C-13 | Invariant derivation pipeline — forward trace rows are cross-referenced as invariant candidates with explicit linkage, showing how observed business transitions generate declared invariants rather than declaring invariants independently |
| C-14 | Schema-level write-time enforcement — column headers or schema slots embed criterion IDs such that filling any cell mechanically satisfies the criterion; rubric compliance becomes structurally unavoidable, not instruction-dependent |
| C-15 | Example row with placeholder syntax — the output format includes at least one filled example row with `…` anchors showing exactly what belongs in each cell, eliminating schema ambiguity before generation begins |
| C-16 | Hard no-prose-substitution constraint — a named ban on prose fallback (e.g., "no prose substitutions") is declared as a hard rule, preventing narrative format from evading structural criteria |

**Golden threshold**: all 5 essential pass + composite ≥ 80.

---

### Scoring notes for v19

- **C-11** is earned only when criterion IDs appear as *field labels or inline annotations inside the output format itself*, not merely in section headings or surrounding prose.
- **C-12** requires *both* orderings explicitly described; naming one interleaving and noting "the reverse is symmetric" does not qualify.
- **C-13** requires a visible cross-reference (e.g., row ref, stage ref, or explicit linkage note) between a trace row and a declared invariant — derivation must be traceable, not implied.
- **C-14** is distinct from C-11: C-11 requires IDs to be *present* in the output; C-14 requires the schema structure itself to make criterion satisfaction *unavoidable at write time* — a cell cannot be filled without satisfying the criterion.
- **C-15** requires an actual filled row (not an empty template) with placeholder anchors (`…`, `[value]`, or equivalent) in every column; a blank schema skeleton does not qualify.
- **C-16** requires the constraint to be *named and declared* as a rule, not merely implied by format instructions; "prose is permitted if brief" disqualifies.
- **C-09** and **C-10** remain at their v17 definitions; no scoring change.
- **Aspirational cap**: score min(earned × 2, 10). A perfect output scoring all 8 aspirational criteria still earns 10 aspirational points.
