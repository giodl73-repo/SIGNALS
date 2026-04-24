Written to `simulations/quest/rubrics/topic-status-rubric-v13-2026-03-15.md`.

---

**v13 summary:**

Two new criteria added as **Structural Tier 12** (+10 pts, max 255 -> 265):

| ID | Name | Isolated by | Points |
|----|------|-------------|--------|
| C-41 | PHASE 3 output declaration with labeled sub-components | V-01 vs V-02 | 5 |
| C-42 | Phase-entry adversary declaration | V-01 vs V-03 | 5 |

**C-41** extends the output-declaration-residency pattern (C-38) and the labeled-sub-component pattern (C-40) from PHASE 2 to PHASE 3. The PHASE 3 execution body must contain its own `PHASE 3 OUTPUT DECLARATION:` block with `INVARIANT:` (consistency guard + `Trigger:` sentence) and `OUTPUT FORM:` (percent, readiness verdict). Implication: `C-41 => C-40, C-39`.

**C-42** extends adversary framing from the output-template site (COMMIT DECISION, C-16) into the PHASE 2 execution body, creating a two-site adversary chain. An explicit `ADVERSARY:` clause at PHASE 2 entry names inertia as what the phase defeats. C-16 presence does not imply C-42. Implication: `C-42 => C-16`.

**Projected R13 scores under v13:** V-01/V-04/V-05 → 265; V-02/V-03 → 260 (symmetric, confirming orthogonality).

The rubric also formally codifies C-39 and C-40 (the v12 Tier 11 criteria that were never written to file) with full criterion text and implication entries.
