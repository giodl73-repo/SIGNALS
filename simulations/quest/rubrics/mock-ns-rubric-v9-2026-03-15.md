v9 written to `simulations/quest/rubrics/quest-rubric-mock-ns-v9-2026-03-15.md`.

**What changed:**

Two new criteria from Round 9 excellence signals, both extracted from V-02's notable:

**C-27 — Structural isolation of guarantee-break and cross-site claims** (depends on C-25 + C-26)  
V-01 and V-03 embed both claims as clauses within a single consequence sentence. V-02 surfaces them as individually scannable rows — each a dedicated, labeled table entry. A clause-embedded pass on C-25 and C-26 is machine-readable but cognitively skippable; a fast reader processing the sentence as a unit may register only the core consequence. C-27 requires each claim to occupy an independently scannable unit so neither can be treated as a trailing qualification.

**C-28 — Navigation-anchored cross-site reference** (depends on C-26 + C-27)  
V-01's C-26 pass says "at the consumption site" — a semantic reference with no location pointer. V-02's pass says "see A-1 Failure consequence row below" — a navigable pointer. C-28 requires the cross-reference to name the specific structural location of the target, not just the site. The bidirectional form (A-1 also marks itself as the S-3 reference target) is noted as the aspirational maximum and seeded as a v10 signal.

**Scoring update:** Aspirational denominator 18 → 20 (`pass/20 * 10`).

**Escalation chain now reads:**

| Compute site | Consumption site |
|---|---|
| C-14 prohibit | C-14 prohibit |
| C-16 run-scoped | C-17 first rule |
| C-18 named classes | C-19 named types + closure |
| C-21 affirmative closure | C-22 catch-all type |
| C-23 failure consequence | C-20 failure consequence |
| C-25 guarantee-break framing | C-24 no-instruction-exempt affirmative |
| C-26 cross-site reference | |
| **C-27 isolated units** | |
| **C-28 navigation anchor** | |
