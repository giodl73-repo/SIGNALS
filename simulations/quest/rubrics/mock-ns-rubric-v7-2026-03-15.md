Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v7-2026-03-15.md`.

---

**What changed in v7:**

Two new criteria from Round 6 excellence signals:

**C-23 — Failure-consequence statement at the compute site** (depends on C-21)
V-02's C-21 pass demonstrated the affirmative closure pattern — "Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt." — but the compute site carried no explanation of what goes wrong if a path violates that guarantee. C-23 closes this gap by requiring the compute-site prohibition to name the upstream contamination mechanism: if any path modifies FLAG after S-N, the closure's guarantee is broken and A-1 inherits a corrupted value that is indistinguishable from a correctly-computed one. This mirrors C-20 (failure-consequence at consumption) applied to the compute side.

**C-24 — No-instruction-exempt affirmative closure at the consumption site** (depends on C-22)
V-01's C-22 pass demonstrated the catch-all clause — "or any other instruction in this step" — but added no positive-obligation statement asserting coverage as a fact. C-24 requires the closure to conclude: "Every instruction in this step — named or unnamed — is governed by this rule. No instruction is exempt." This mirrors C-21's pattern (positive-obligation + no-exemption applied to path enumeration) applied to instruction enumeration at the consumption side, completing the structural symmetry between both prohibition sites.

**Scoring update:** Aspirational denominator 14 → 16 (`pass/16 * 10`).

**Escalation chains now read:**

| Compute site | Consumption site |
|---|---|
| C-14 prohibit | C-14 prohibit |
| C-16 run-scoped | C-17 first rule |
| C-18 named classes | C-19 named types + closure |
| C-21 affirmative closure | C-22 catch-all type |
| **C-23 failure consequence** | C-20 failure consequence |
| | **C-24 no-instruction-exempt affirmative** |

Both sites now carry the full five-level escalation chain. The compute site lacked a failure-consequence level (C-20 existed only on the consumption side); the consumption side lacked a positive-affirmative level (C-21 existed only on the compute side). v7 closes both asymmetries.
