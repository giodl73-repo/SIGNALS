Written to `simulations/quest/rubrics/flow-throttle-rubric-v21-2026-03-16.md`.

---

**What changed: v20 → v21**

**C-56 — Named executor inertia path per consequence clause** (from ES-01, R20)

This is the single formally-labeled excellence signal from the R20 scorecard. The upgrade relationship:

| Layer | Criterion | What it requires |
|-------|-----------|-----------------|
| Obligation | C-50 | SHALL instruction per sub-step |
| Causal argument | C-53 | "Cannot skip because" structural failure named per step |
| Executor grounding | **C-56** | Executor inertia path named per step — the *reasoning move* that generates the failure |

C-53 names what goes wrong structurally. C-56 names the executor-shortcut that produces it (e.g., `` `GATE-A complete = bypass detected` inertia path ``), connecting the consequence clause to the bypass-detection register (C-47) rather than leaving it as a free-standing annotation.

**Score delta**: 235 pts (47 × 5) → 240 pts (48 × 5), max composite 325 → 330. Golden threshold unchanged.

**Structural Progression Table**: The C-53–C-55 block is extended to C-53–C-56, with C-56 inserted between C-53 and C-49 in the right column to show the precision chain: atomized steps → causal argument → executor-behavior diagnosis → typed audit → joint audit row.
