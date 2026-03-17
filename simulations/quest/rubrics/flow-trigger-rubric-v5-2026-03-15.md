**flow-trigger-rubric-v5** written to `simulations/quest/rubrics/flow-trigger-rubric-v5-2026-03-16.md`.

---

**Three new aspirational criteria (C-20–C-22), N_aspirational: 11 → 14:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-20 | V-01/V-03 closure checks (`{count} [must be 0]`) | Named CLOSURE CHECK block with zero-tolerance counters per per-entry obligation — makes the document self-auditing without rescanning every row | C-15–C-19 (per-entry obligations it verifies) |
| C-21 | V-01 PROHIBITION contracts; V-02 gap noted | Named PROHIBITION statements per role/phase — explicit declarations of barred actions, closing scope by role-action definition rather than gate tokens alone | C-14 (scope-closing event gate) |
| C-22 | V-03 "all slots required" mandate | Global template invariant — one declaration that all named slots in all entry types are required, collapsing per-entry obligations into a single auditable structural rule | C-15, C-16, C-17, C-18, C-19 (individual per-entry obligations it unifies) |

**Structural relationship:** C-20 audits whether C-15–C-19 were satisfied across the full enumeration. C-21 prevents later phases from expanding the scope that C-14 closed. C-22 unifies C-15–C-19 into a single global invariant that makes omission detectable by slot-presence rather than criterion-by-criterion review — the structural ceiling of the per-entry obligation family.
