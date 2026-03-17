Written to `simulations/quest/rubrics/flow-throttle-rubric-v10-2026-03-16.md`.

---

**Two new criteria extracted from R9:**

**C-27 — Closed-register declaration for structured-output exemption class**
V-03 and V-05 both add "No other element types are added to this register without revising this contract." C-25 names what is exempt; C-27 declares the register exhaustively closed. Without it, an executor encountering an unregistered element type must infer its classification — reintroducing the content-inspection problem C-25 was designed to eliminate. Pass condition: closure declaration present; additions require explicit contract revision.

**C-28 — Gate-annotation audit test**
V-03's Field 3 and V-05's dual-path verification add actionable audit instructions to the C-26 annotation: what to look for when the gate is present (compliance evidence) and what the output looks like when it is absent (failure signature). C-26 explains *why* the gate exists; C-28 explains *how to verify* it. Pass condition: named audit test element with both a compliance-path instruction and a gate-absent failure signature.

**Score delta**: Aspirational 90 pts (18 × 5) → 100 pts (20 × 5), max composite 180 → 190. Golden threshold unchanged.
