---

# Variate R2 — corps-rob (rubric v2, 2026-03-17)

5 complete variations targeting the three new v2 criteria (C-11, C-12, C-13) through structurally different mechanisms than V-04 R1.

---

## Variation Axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Per-stage distributed inertia | Each stage writes its own role-specific inertia statement (no global anchor). Richer C-13 per role; risk: fragmented cross-stage picture vs V-04 R1's coherent anchor |
| **V-02** | Blocker-at-open (reversed detection) | Stage N+1 clears Stage N's blockers before proceeding via a GATE CHECK. Shifts accountability upstream. Risk: gate check becomes formulaic when no blockers exist |
| **V-03** | Handoff-centric structure | Handoff packet is the primary artifact; findings are supporting evidence for it. Inverts the usual writing direction. Risk: findings become backward-reasoned, degrading C-04 |
| **V-04** | Distributed inertia + handoff-centric + blocker field | All three new v2 criteria (C-13, C-11, C-12) delivered through fully distributed mechanisms — no global anchor. Tests whether C-13 can hold without a shared reference point |
| **V-05** | Briefing envelope + V-04 R1 structure | Adds an explicit prior-stage briefing section at each stage open (active synthesis, not copy). Combined with global anchor + handoff + blocker. Tests whether eliminating recall-dependence pushes past V-04 R1's ~99 ceiling |

---

## Key Design Decisions

**Why no V-01/V-02/V-03 carry the global anchor simultaneously**: each is a clean single-axis test. V-01 tests distributed inertia alone; V-02 tests gate-at-open alone; V-03 tests handoff-inversion alone. V-04 and V-05 combine.

**V-02's HOLD mechanism**: the only variation that can produce a truncated stage — a stage that hits HOLD terminates at the gate check with no findings. This is a testable structural prediction: does the rubric score a HOLD stage as a failure or as correct behavior?

**V-05 vs V-04 R1**: V-04 R1 achieves C-11/C-12/C-13 via 4-step per-stage structure. V-05 adds one more structural layer (briefing envelope) and sharpens C-08 guarantees. The scoring question is whether the briefing envelope is net positive (better cross-stage coherence) or net negative (length cost + copy-task degradation).

Saved to `simulations/quest/golden/corps-rob-variate-R2-2026-03-17.md`.
