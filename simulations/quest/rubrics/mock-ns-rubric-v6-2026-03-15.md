Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v6-2026-03-15.md`.

---

**What changed in v6:**

Two new criteria from Round 5 excellence signals, both following the escalation pattern established in prior rounds:

**C-21 — No-exemption affirmative closure at compute site** (depends on C-18)
V-05's C-18 language was scored "strongest enumeration" because it went beyond named classes to add: *"Every execution path that reaches A-1 carries the FLAG value emitted here. No path is exempt."* The gap closed: even a catch-all clause can be read as illustrative; the affirmative closure states exhaustiveness as a positive fact. Requires both components — positive-path assertion AND no-exemption statement.

**C-22 — Catch-all instruction clause in anti-displacement closure** (depends on C-19)
The Round 5 scoring note flagged V-01 as "C-19 partial for catch-all absence" — V-01 names exactly the three canonical instruction types (field-listing, category lookup, formatting) but omits *"or any other instruction in this step."* This mirrors the C-18 catch-all pattern applied to the consumption side. Closes the gap where a future instruction type not in the named list might not be recognized as subject to the displacement prohibition.

**Scoring update:** Aspirational denominator 12 → 14 (`pass/14 * 10`).

**Escalation chains now read:**

| Compute site | Consumption site |
|---|---|
| C-14 prohibit | C-14 prohibit |
| C-16 run-scoped | C-17 first rule |
| C-18 named classes | C-19 named types + closure |
| **C-21 affirmative closure** | **C-22 catch-all type** |
| | C-20 failure consequence |
