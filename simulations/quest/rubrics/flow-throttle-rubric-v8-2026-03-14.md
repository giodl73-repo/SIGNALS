v8 rubric written. Here's what was extracted and why:

---

**C-27 — Boundary-Event Round-Name Cross-Reference** (Signal 1)

V-03 and V-04 both embed the specific round identifier in the boundary-event phrase:

- V-03: `(before any **Round 2** construct evaluation begins)` — round-specific
- V-04: `(execute before entering **Round 2** evaluation)` — round-specific
- V-02: same phrase as V-03, also names "Round 2" — but fails C-26 (transitional sentence)

A minimal C-25 pass could say "(before any construct evaluation begins)" — generic, no round name. C-27 requires the phrase to be cross-referenceable to the heading hierarchy. A reader can navigate from "Round 2" in the phrase directly to `## ROUND 2` and verify execution order without reading the container content. The R7 form-equivalence finding confirms no form preference — both temporal and imperative satisfy C-27.

**C-28 — Barrier-Container Dual Machine-Verifiability** (Signal 2)

C-25 makes execution order determinable from the container name alone. C-26 makes it determinable from structural position alone. Together they create dual machine-verifiability — neither signal can be removed independently without breaking the other. This is the barrier-layer analog of C-23 (which captured C-21 ∩ C-22). V-02 earns C-27 (round name present) but fails C-28 (fails C-26). Only V-03 and V-04 earn both.

**Dependency map for v8:**
- C-27 requires C-25 (and transitively C-21)
- C-28 requires C-25 AND C-26 (but NOT C-27 — independent)
- V-02 can earn C-27 without C-28 (passes C-25, has round name, fails C-26)

**Updated score table:** 148 → 154. Max band 6 pts for Aspirational v8.

**Retroactive R7 scores under v8:** V-03/V-04 = 154, V-02 = 148, V-01 = 145, V-05 = 142 — four-level spread.
