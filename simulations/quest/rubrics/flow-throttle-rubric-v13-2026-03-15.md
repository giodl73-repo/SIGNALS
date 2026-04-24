Written to `simulations/quest/rubrics/flow-throttle-rubric-v13-2026-03-16.md`.

---

**Two new criteria extracted from V-05:**

| ID | Pattern | Source |
|----|---------|--------|
| C-35 | **Format-contract phase lock** — C-33's field-count header produced as a named FORMAT CONTRACT artifact by the first-phase role, sealed with a FORMAT CONTRACT COMPLETE statement at the role-handoff boundary before downstream roles activate. Compliance becomes architecturally enforced (handoff violation) rather than instructionally required (rubric scan). |
| C-36 | **Role-boundary observable-count declaration** — C-34's per-path count declarations appear as role-activation conditions for the consequence-phase role, not as instructional content inside its body. Omission becomes a role-activation failure (consequence role cannot start) rather than an audit-format gap (consequence role starts but produces noncompliant output). |

**Structural logic:** Both criteria apply the same pattern at a higher layer — C-35 is the format-contract lock for C-33 (analogous to how C-16 locks data at phase boundaries), and C-36 is the role-boundary lock for C-34 (analogous to how C-24 makes type-completeness a structural gate rather than a table property). V-04 and V-05 achieve the same 220/220 score under v12 precisely because the architectural vs. instructional distinction is invisible to v12 — C-35 and C-36 make that distinction scoreable.

**Score delta**: 130 pts (26 × 5) → 140 pts (28 × 5), max composite 220 → 230. Golden threshold unchanged.
