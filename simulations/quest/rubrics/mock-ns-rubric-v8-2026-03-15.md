Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v8-2026-03-15.md`.

---

**What changed in v8:**

Two new criteria from Round 7 excellence signals, both extracted from the gap between V-04's minimal C-23 pass and V-05's extended form:

**C-25 — Guarantee-break framing at the compute-site consequence** (depends on C-23)
V-04's C-23 pass named the mechanism and effect in minimal form: "If any path modifies FLAG after this point, A-1 will inherit a corrupted value that cannot be distinguished from a correctly-computed one." V-05 added "the guarantee stated above is broken" as a causal bridge connecting the C-21 affirmative closure directly to the consequence. Without this framing, the consequence reads as an independent warning rather than as the cost of violating a stated commitment. C-25 requires the framing to be explicit.

**C-26 — Cross-site consequence reference at the compute site** (depends on C-23, requires C-20)
V-05's extended form additionally named "the same silent category mismatch described at the consumption site," explicitly linking the compute-site consequence to C-20's consumption-site consequence. Without this cross-reference the two consequence statements are isolated — a reader at either site must independently discover the other. C-26 requires the cross-reference to appear in the compute-site consequence statement, making the structural symmetry between the two escalation chains navigable.

**Scoring update:** Aspirational denominator 16 → 18 (`pass/18 * 10`).

**Escalation chains now read:**

| Compute site | Consumption site |
|---|---|
| C-14 prohibit | C-14 prohibit |
| C-16 run-scoped | C-17 first rule |
| C-18 named classes | C-19 named types + closure |
| C-21 affirmative closure | C-22 catch-all type |
| C-23 failure consequence | C-20 failure consequence |
| **C-25 guarantee-break framing** | **C-24 no-instruction-exempt affirmative** |
| **C-26 cross-site reference** | |

The compute site now carries a six-level chain. C-25 and C-26 are both compute-side refinements of C-23 — one deepens the internal framing of the consequence, the other opens a navigation path to the mirror statement at the consumption site.
