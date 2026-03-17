Written to `simulations/quest/golden/org-build-variate-R11-2026-03-16.md`.

---

## org-build Variate — Round 11 (Rubric v8)

**5 variations targeting C-27 + C-28**

| V | Axis | Key Mechanism |
|---|------|--------------|
| **V-01** | Count-conditional binding (single) | Phase 1 binds `T1-COUNT-FLOOR` to `T1-DEPTH-FLAG` as an explicit two-branch conditional in the instruction body, before the record block |
| **V-02** | Record block anchor structure (single) | Prompt-open block architecture declaration explains why `PHASE-ORDERING-GUARD` must be the first field; each gate has an "OUTBOUND GATE -- emit now" prompt |
| **V-03** | Inertia-first verdict declaration (single) | IA scope template selection moves into Phase 1 as gate output `T1-IA-SCOPE-KEY`; Phase 2 consumes it via named input contract |
| **V-04** | Count-conditional + Record anchor + Phrasing register (combined) | Full MUST/FORBIDDEN throughout; adds IA role file skeleton with `{{T1-IA-SCOPE-KEY-TEMPLATE}}` slot (C-22) |
| **V-05** | Count-conditional + Record anchor + Unification architecture (combined) | Each block has in-block commentary naming the three observable properties (gate schema, ordering constraint, materialization); IA skeleton with gate-variable slots (C-22) |

**C-27 closure pattern** (all five): Phase 1 encodes the binding as a named typed output `T1-COUNT-FLOOR` with explicit conditional — `T1-DEPTH-FLAG = standard → T1-COUNT-FLOOR = 20-30; T1-DEPTH-FLAG = deep → T1-COUNT-FLOOR = 50+` — before the record block, not as Phase 2 default or preamble text.

**C-28 closure pattern** (all five): Every record block opens with `PHASE-ORDERING-GUARD: FORBIDDEN: Phase N+1 begins before this block is emitted.` as the structurally first field. The guard is inside the block — the record block can only be parsed by reading the guard first.
