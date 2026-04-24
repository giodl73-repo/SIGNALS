Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v7-2026-03-16.md`.

---

**Two new criteria added for R7:**

**C-25 — Marking-Gate Schema Lock** (sharpens C-23, from V-04 Registry pattern)

C-23 closes the loophole where a model places marks mid-batch despite the write-order requirement, by naming the forbidden action. C-25 closes the next loophole: a prose prohibition still relies on the model choosing to honor it. V-04's registry encodes the mark slot as a structural column that physically cannot be populated until all batch rows exist — the gate is an output-schema property, not an instruction. Pass requires: the selection-mark column/slot is gated by a structural null-condition, not only a named prohibition.

**C-26 — AMEND Pool-Composition Constraint** (sharpens C-12, from V-05 "distribution, not labels" signal)

C-12 requires the re-invocability bar. The loophole: a directive can satisfy that bar by changing category taxonomy, emphasis, or framing — producing a "different" pool in presentation but the same underlying candidate ideas. V-05 explicitly closes this by requiring AMEND items to shift candidate distribution (different ideas appear). Pass requires: the prompt names the distribution-shift test as the criterion, not just re-invocability.

**Key structural move in v7:** C-25 extends the peer-comparison lineage to seven levels deep; C-26 opens a second branch (C-05 → C-09 → C-12 → C-26), making explicit that the AMEND chain has its own escalating ceiling. Max raised from 135 to **140**.
