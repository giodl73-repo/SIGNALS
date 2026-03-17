Written to `simulations/quest/rubrics/org-committee-rubric-v18-2026-03-16.md`.

---

**What changed v17 → v18**

**C-44 — INVARIANT VALIDATE rules enumerate three independent seal-element failure modes** *(new)*

C-42 requires bilateral VALIDATE on INVARIANT fill rules, but does not specify that failure modes be enumerated independently. The gap: a single FAILS example covering joint absence cannot detect mode (a) — phase-commit reference present but modification prohibition missing. A partial fill that carries the commit identifier but silently omits the prohibition passes the bilateral test. C-44 requires three named FAILS axes: (a) commit-present/prohibition-absent, (b) both elements absent in a present seal line, (c) line absent entirely. Each required seal element becomes an independent failure axis.

**C-45 — VALIDATE rule on the bidirectionality clause fill tests content completeness — both directions named** *(new)*

C-43 requires the bidirectionality clause to be pre-declared with a dedicated fill rule; C-41 requires both directions to be stated. But neither requires the fill rule's VALIDATE to test whether both directions are present — only that the clause was filled with something. A half-coupling (one direction named, reverse direction absent) passes structural presence while omitting the reverse obligation. C-45 adds the explicit ACCEPTABLE/FAILS pair: `both directions stated` passes; `only one direction named — half-coupling` fails.

**C-46 — Inertia-Advocate role is structurally guaranteed as a Phase 3 participant via SYNTHESIZE instruction when absent from charter** *(new)*

C-12 guarantees the switching-cost investigation happens; C-27 ensures findings carry citable labels; C-17 ensures advocates cite them. But none guarantee that the *inertia perspective* is voiced in Phase 3 when the charter lists no inertia-focused role. Phase 1 findings may have no owner-voice. C-46 requires a SYNTHESIZE instruction that injects an Inertia-Advocate into the Phase 3 participant set when the sort produces no natural owner — Phase 1 → Phase 3 continuity is a structural guarantee, not a charter dependency.

**Scoring**: aspirational pool 35 → 38; aspirational max 70 → 76; composite max **160 → 166**.
