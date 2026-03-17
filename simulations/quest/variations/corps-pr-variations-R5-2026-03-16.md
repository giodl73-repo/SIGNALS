Written to `simulations/quest/golden/corps-pr-variate-R5-2026-03-16.md`.

---

## R5 — corps-pr — Variation Summary

**5 complete skill body prompts. Rubric v5 target: C-17 (IA cost ledger) and C-18 (phase-gate structure).**

### Variation Axes

| | Axis | Hypothesis |
|---|---|---|
| **V-01** | Inertia framing — IA cost ledger | 4-category cost ledger schema (Maintenance / Incident exposure / Integration cost / Regression risk) makes C-17 fill-or-fail. Technical roles must cite a specific ledger row in their IA anchor — they can't acknowledge the IA in general terms. |
| **V-02** | Lifecycle emphasis — top-level pipeline declaration | Pipeline spec declared before execution names all 5 phases with entry/exit conditions and criteria gated. Domain-lens gate appears as the Phase C exit condition in the spec. Structure is auditable before a single finding is written. |
| **V-03** | Role sequence — two-pass finding generation | Draft all candidates (4A) → batch audit log (4B) → output only passing findings (4C). The audit log is the Phase C exit gate — incomplete log = incomplete phase. Satisfies C-18 structurally rather than as an inline reminder. |
| **V-04** | Combined: cost ledger + pipeline declaration | Pipeline spec cross-references the cost ledger: Phase B exit requires filled ledger cells; Phase C IA anchors must cite a specific Phase B ledger row. C-17 and C-18 are mutually reinforcing rather than parallel. |
| **V-05** | Combined: cost ledger + two-pass audit + ban-to-fix | Three mechanisms at three different phases: cost ledger enforces IA depth (Phase B), audit log enforces Phase C exit, ban-to-fix substitution table enforces divergence depth (Phase D). Each is independently checkable. |

### What each variation contributes to R5 criteria

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-17 IA cost terms | ledger schema | cost terms (Phase B exit) | cost terms inline | ledger + phase cross-ref | ledger schema |
| C-18 phase gates | inline gates | declared spec up front | audit log as exit gate | declared spec + ledger | audit log as exit gate |
| C-16 AMEND schema | named fields | named fields | named fields | named fields | named fields |
| C-13 ban-to-fix | checklist only | full table | full table | full table | full table |
| C-15 domain-lens gate | per-finding two-step | Phase C exit condition | batch audit per role | Phase C exit condition | batch audit per role |
