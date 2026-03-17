**flow-throttle-rubric-v14** written to `simulations/quest/rubrics/flow-throttle-rubric-v14-2026-03-16.md`.

---

## What changed

**One new criterion — C-37 (Annotation-inventory extension of FORMAT CONTRACT)**

The Round 13 scorecard surfaces a pattern C-35 and C-36 don't cover: both V-03 and V-05 fail C-18 through different mechanisms (role-boundary relocation vs. register compression) while passing C-35 and C-36. V-04 is the only variation that achieves 230/230 — C-18 survives only because the three-role pipeline carries the annotations intact, not because any architectural mechanism enforces their presence.

The structural progression is consistent across three criteria pairs:

| Instructional layer | Contract-lock layer |
|---------------------|---------------------|
| C-33 field-count declared | C-35 field-count sealed in FORMAT CONTRACT |
| C-34 observable-count at path labels | C-36 observable-count as role-activation condition |
| **C-18 annotation required at anchor** | **C-37 annotation inventory sealed in FORMAT CONTRACT** |

C-37 extends the FORMAT CONTRACT (C-35) with an annotation-inventory block: each C-18 annotation listed by anchor identifier and failure-mode label, sealed under the same FORMAT CONTRACT COMPLETE boundary. Annotation dropout becomes a contract violation detectable at the handoff boundary, not a content gap detectable only by post-assembly rubric scan.

**Score delta**: 140 pts (28 × 5) → 145 pts (29 × 5), max composite 230 → 235. Golden threshold unchanged.
