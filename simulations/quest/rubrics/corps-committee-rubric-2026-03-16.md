Rubric written to `simulations/quest/rubrics/corps-committee-rubric-v1-2026-03-16.md`.

**Summary of criteria:**

**Essential (60 pts, all must pass):**
- **C-01** — Committee type recognized and declared in Phase 0 (ROB/shiproom/arch-board)
- **C-02** — All 5 phases present with terminal `PHASE-N-COMMIT: [locked]` lines, no content after commits
- **C-03** — `## INERTIA RECORD` has all 4 INERTIA-FINDING-* anchors (no placeholders) + complete INERTIA INVARIANT with both contract elements
- **C-04** — Phase 5 delivers verdict + actionable items (owner/action/deadline) + dissent or explicit no-dissent; Owner+Trigger present if verdict not APPROVED

**Recommended (30 pts):**
- **C-05** — INERTIA CONTINUITY BRIDGE correctly answers YES/NO; injection fires when needed; inertia voice cites a finding label
- **C-06** — Tier 1→2→3 ordering, standalone `STANCE:` line per voice, at least one BLOCK or CONDITION
- **C-07** — TALLY counts match STANCE MANIFEST tokens exactly; OUTCOME derived mechanically from tally

**Aspirational (10 pts):**
- **C-08** — Charter-loaded participants with role-shaped voices; Phase 5 conditions name specific artifacts + authorities (not vague directives)
