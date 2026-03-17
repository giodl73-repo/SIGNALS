Written to `simulations/quest/rubrics/draft-proposal-rubric-v15-variate-R15-2026-03-15.md`.

---

## Round 15 — 5 Variations

**Predicted scores (denominator /32):**

| Variation | Axis | Designed fails | Composite |
|-----------|------|----------------|-----------|
| V-01 | Role sequence (Architect-first) | C-39 only | 99.69 |
| V-02 | Output format (compact, PM-first) | C-37 only | 99.69 |
| V-03 | Lifecycle (stale 38-row table) | C-24 + C-38 + C-39 cascade | 99.06 |
| V-04 | Phrasing register (conversational) + PM-first | C-25 + C-33 | 99.38 |
| V-05 | Inertia framing | C-36 + C-37 + C-38 + C-39 | 98.75 |

---

### Key design decisions

**V-01 (C-39 independent fail)** — The only variation that isolates C-39 alone. T-37 CONDITION carries Part 1 (the inline failure exemplar, C-38 PASS) but stops there. No correct-format prescription (Part 2). T-39 fires; T-38 is silent. This is the C-39 boundary case: the one document state that passes C-38 and fails C-39.

**V-02 (C-37 fail, C-38+C-39 both pass)** — The reference exemplar for the full two-part T-37 CONDITION. Phase 9b Domain 2 degrades to row-level ("R-NN IDs applied to risk row"), T-37 fires — but T-37's own CONDITION cell in the amendment spec carries both parts, so T-38 and T-39 are silent. Tests the rubric's key invariant: C-39 PASS is achievable even when T-37 fires.

**V-03 (stale 38-row table)** — Confirms the v15 version-bump cascade. T-37 is present in the stale table but its CONDITION is abstract — C-38 fails independently, C-39 by cascade. T-39 is absent from the 38-row table, so the cascade produces no T-39 finding. Named findings: T-24, T-38. Three fails from one authoring shortcut (carrying the v14 table forward).

**V-04 (C-25 + C-33)** — Combination isolating the two formatting/prohibition fails. T-37 CONDITION is fully compliant (both parts, conversational language) — confirms C-38 and C-39 are satisfiable in non-formal register. The failure surface is entirely in Phase 2 (missing prohibition) and Phase 10 (prose finalization).

**V-05 (quad fail)** — Maximum depth collapse: T-37 CONDITION abstract (C-38, C-39), Domain 1 no P×I (C-36), Domain 2 row-level (C-37). Four findings at finalization. The inertia framing is cosmetic — the scoring failure comes from Phase 9b and the amendment spec, not from the framing axis.
