Saved to `simulations/quest/golden/signal-setup-variate-R7-2026-03-16.md`.

---

## signal-setup Variations — Round 7

**Baseline**: V-05 R6 (predicted 100 against v6 rubric). New criterion: **C-21** — secondary optional gates carry path-specific consequence anchors, meaning GATE 6 (Copilot decline) must be semantically distinct from GATE 4's language by tool *and* phase.

**Risk identified in carry-forward baseline**: V-05 R6's GATE 6 decline uses "build suggestion" — same semantic field as GATE 4's "next build." Distinction is by tool name only, not by development phase. C-21's strict reading may require phase-local anchors.

### Variation axes

| | Axis | Hypothesis |
|--|------|------------|
| A | Concretize GATE 6 by phase | Replace "build suggestion" with an implementation-phase artifact ("first function body") — separates GATE 4 (planning/commit) from GATE 6 (implementation/code output) by phase, not just tool name |
| B | Add Copilot already-configured affirm | GATE 6 gets a parallel to GATE 2's C-20 treatment: when copilot-instructions.md already has Signal, name the auto-load mechanism ("Copilot Chat loads workspace instructions at session start") |
| C | Phase-label all decline exits | Make GATE 1 = design phase, GATE 4 = planning/spec phase, GATE 6 = implementation phase — explicit labels, no shared vocabulary possible |

### Variations

| | Axes | Key change | Predicted |
|--|------|------------|-----------|
| **V-01** | A | GATE 6: "before Copilot writes the first function body" | 100.0 |
| **V-02** | B | GATE 6 already-configured affirm added; decline unchanged | 100.0 / 99.2* |
| **V-03** | C | All three declines phase-labeled: design / spec / endpoint | 100.0 |
| **V-04** | A+B | Implementation anchor + Copilot affirm | 100.0 |
| **V-05** | A+B+C | Phase-labeled declines + GATE 6 affirm + concrete anchor | 100.0 |

*V-02 risk: C-21 boundary unchanged — if GATE 6 decline still reads as "build"-adjacent, structural symmetry alone doesn't resolve it.

**Carry-forward recommendation**: V-05 (A+B+C) for robustness; V-01 if scoring shows the single-phrase change is sufficient (prefer minimalism per CLAUDE.md).
