Written to `simulations/quest/golden/corps-build-variate-R13-2026-03-17.md`.

---

**R13 Variate Summary**

| V | Axis | C-37 | C-38 | New Pattern |
|---|------|------|------|-------------|
| V-01 | PATH-ISOLATION COP assignment (add COP-14) | PASS | PARTIAL | — |
| V-02 | PROPERTY-COVERAGE-RULE explicit assertion | PARTIAL | PASS | — |
| V-03 | Phase `ENFORCES-INVARIANTS:` annotation | PARTIAL | PARTIAL | seeds C-39 |
| V-04 | V-01 + V-02 — COP-14 live-demonstrates the rule | PASS | PASS | — |
| V-05 | V-01 + V-02 + V-03 + CROSS-REF `enforces-invariant:` | PASS | PASS | seeds C-39, C-40 |

**Root cause of R12 PARTIALs addressed:**
- C-37 gap: `INVARIANT-PATH-ISOLATION` had `cop: (implicit...)` — not a COP-NN identifier. V-01 adds COP-14 (`PATH-ISOLATION-CHECK [team-slug]:`), completing the bidirectional map for all five invariants.
- C-38 gap: V-05 R12's CO-EXTENSIVE DECLARATION named all three layers but never stated the positive rule — "adding a new property requires entries in all three." V-02 adds the explicit `PROPERTY-COVERAGE-RULE` assertion.

**New patterns seeded for rubric v12:**
- **C-39** (Phase ENFORCES-INVARIANTS): each phase header declares which invariants it owns; `ENFORCES-INVARIANTS: NONE` for phases without enforcement. Makes per-phase invariant residency auditable at a glance.
- **C-40** (CROSS-REF invariant-linkage): BUILD-VERIFY CROSS-REF rows carry `enforces-invariant:` annotations, making CROSS-REF a fourth independent verification layer and extending the CO-EXTENSIVE DECLARATION from three to four layers.
