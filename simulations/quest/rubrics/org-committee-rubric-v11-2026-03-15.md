**C-31 — Phase transitions carry explicit commit declarations before the next phase begins**

**Signal source**: V-04 "Phase-Commit Architecture." The pattern is latent in C-26's description ("each phase output commits before the next phase begins") but C-26 only enforces phase labeling. The commit step itself — the terminal marker that locks phase output before the next header appears — has no structural criterion.

**Relationship chain**:
- C-26 requires phases to be labeled blocks
- C-29 requires gates to be intra-phase retry loops (phase never halts externally)
- C-30 requires fill rules to be verb-first imperatives
- **C-31** requires each phase to carry a terminal `PHASE-N-COMMIT:` marker so the boundary between "phase content complete" and "next phase begins" is a structural lock, not a header gap

**Why this matters**: Without a commit marker, subsequent phases can retroactively soften Phase N output without violating any existing rule. The commit makes that architecturally impossible — same upgrade pattern C-22 applied to C-16, C-18 applied to C-11.

**Scoring update**: Aspirational pool 22 → 23; aspirational max 44 → 46 pts; composite max **136**.

File written to `simulations/quest/rubrics/org-committee-rubric-v11-2026-03-16.md`.
