Written to `simulations/quest/rubrics/topic-status-rubric-v15-2026-03-15.md`.

---

**v15 summary — Structural Tier 14 (+10 pts, max 275 → 285):**

| ID | Name | Isolated by | Points |
|----|------|-------------|--------|
| C-45 | Preamble adversary chain declaration | V-01 vs V-02 | 5 |
| C-46 | Adversary defeat condition sub-component | V-01 vs V-03 | 5 |

**C-45** extends the preamble architectural invariant declaration pattern (C-34 for exits, C-44 for output declarations) to adversary chain residency. The preamble carries an `ADVERSARY CHAIN:` block naming both the PHASE 2 and PHASE 3 adversaries as a two-element structural chain with independence assertion. The preamble now carries three architectural invariant blocks: dual-axis exit chain (C-34), output declaration chain (C-44), adversary chain (C-45). Implication: `C-45 => C-43`.

**C-46** extends each phase-entry adversary block from two-part (adversary + trigger) to three-part form by adding a labeled `DEFEAT CONDITION:` sub-component — the adversary-block parallel of C-40's labeled sub-components in OUTPUT DECLARATION. Both PHASE 2 and PHASE 3 adversary blocks must carry the label independently. Implication: `C-46 => C-43`.

Both criteria share C-43 as their sole prerequisite (asymmetric from most prior tier pairs where the two new criteria have different prerequisites), confirming the adversary chain dimension is the common structural anchor for this tier.

**Projected R15 scores:** V-01/V-04/V-05 → 285; V-02/V-03 → 280 (symmetric, confirming orthogonality).
