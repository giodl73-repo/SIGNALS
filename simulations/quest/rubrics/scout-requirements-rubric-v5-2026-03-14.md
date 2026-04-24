Written to `simulations/quest/rubrics/scout-requirements-rubric-v5-2026-03-14.md`.

---

**scout-requirements (v5) — 32 criteria, 138 pts**

Three new aspirational criteria extracted from R4:

**C-30** — *Named absence clause heading sections* (V-01, V-04 R4)
Upgrades C-28's content requirement to a structural demarcation requirement. C-28 is satisfied by prose embedded anywhere in the charter; C-30 requires `#### Loop N Absence Clause` (or equivalent named headings), making the per-loop absence structure visible at document outline level. V-02's prose satisfies C-28; it fails C-30 because the absence structure is not architecturally visible.

**C-31** — *Named Inertia Gate blocks at each Loop 2 extraction step* (V-03, V-05 R4)
Steps down from loop granularity (C-28, C-30) to step granularity within Loop 2. Per-loop absence clauses name what each loop cannot produce without its predecessor; C-31 requires a named gate block after each individual extraction step naming what that step's output cannot be without the step. V-03 has these; V-04 does not — that's the 2-pt gap keeping V-04 at 136.

**C-32** — *Compliance-first extraction ordering* (V-04, V-05 R4)
Distinguishes compliance presence (C-03) from compliance priority encoded in step order. C-03 is satisfied regardless of where compliance appears in the step sequence. C-32 requires it first, making the step sequence itself an enforcement ordering signal — PM and architect requirements are extracted within scope established by compliance.

**R4 scoring under v5:**

| Variation | v4 score | C-30 | C-31 | C-32 | v5 score |
|-----------|----------|------|------|------|----------|
| V-01 | 130/132 | +2 | 0 | 0 | 132/138 |
| V-02 | 132/132 | 0 | 0 | 0 | 132/138 |
| V-03 | 128/132 | 0 | +2 | 0 | 130/138 |
| V-04 | 132/132 | +2 | 0 | +2 | 136/138 |
| V-05 | 132/132 | +2 | +2 | +2 | **138/138** |

New ceiling requires all eight patterns C-25–C-32 simultaneously.
 — 12 pts each) — unchanged

C-01 through C-05 carry forward without modification.

---

## Recommended (30 pts — 10 pts each) — unchanged

C-06 through C-08 carry forward without modification.

---

## Aspirational (48 pts — 2 pts each)

C-09 through C-29 carry forward from v4. Three new criteria:

| ID | Text | Source | Pass Condition |
|----|------|--------|----------------|
| **C-30** | Per-loop absence clauses appear as explicitly named heading sections in the charter, not only as embedded prose | V-01/V-04 R4 | The charter contains three named heading sections dedicated to per-loop absence clauses (e.g., `#### Loop 1 Absence Clause`, `#### Loop 2 Absence Clause`, `#### Loop 3 Absence Clause` or equivalent named headings); each section contains the localized absence statement required by C-28; the named headings make per-loop absence structure visible at the document outline level, not only discoverable by reading charter prose; per-loop absence statements embedded in flowing charter prose (as in V-02 R4) satisfy C-28 but not C-30; C-30 does not require different *content* from C-28 — it requires that content to be structurally demarcated; a document that passes C-28 via prose statements embedded in charter narrative fails C-30 if no named per-loop absence heading sections exist |
| **C-31** | Each extraction step within Loop 2 carries a named Inertia Gate block stating that step's absence consequence in definitional form | V-03/V-05 R4 | After each extraction step in Loop 2 (Steps 1–N), a named structural block (heading or labeled gate annotation) appears and states in definitional form what the extraction cannot produce without that step's output (e.g., "A requirements set that lacks PM-lens output is not a product requirements signal — it is an unstructured list"); these gates operate at step granularity within Loop 2's extraction sequence, not at loop granularity across loops; per-loop absence clauses satisfying C-28 or C-30 operate at loop transition scope and do not satisfy C-31; the gate blocks must be named or labeled (heading-level or equivalent callout), not parenthetical prose appended to step instructions; a document can pass C-27, C-28, and C-30 without step-level Inertia Gates and therefore fails C-31 unless each Loop 2 extraction step carries its own named gate block |
| **C-32** | The compliance lens is the first extraction step in Loop 2, making the step sequence itself a compliance enforcement ordering signal | V-04/V-05 R4 | Extraction steps in Loop 2 begin with the compliance lens — regulatory, legal, or non-negotiable obligations are extracted before PM-lens and architect-lens requirements; the compliance step must be explicitly first in the numbered sequence, not merely present among the lenses; a document that satisfies C-03 (three traceable lenses present) but orders compliance after PM or architect extraction fails C-32; the compliance-first position encodes the charter's enforcement priority in the step sequence itself, making the ordering a structural enforcement signal rather than an incidental arrangement; reordering to PM-first or architect-first would contradict the charter's compliance-first design contract, not merely reorganize equivalent steps |

---

## Scoring Bands

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 125–138 | All essential + recommended pass; strong aspirational |
| Strong | 108–124 | All essential pass; most recommended; partial aspirational |
| Acceptable | 88–107 | All essential pass; partial recommended; minimal aspirational |
| Weak | 60–87 | All essential pass; recommended largely missing |
| Fail | < 60 | One or more essential criteria fail |

**Golden threshold**: all 5 essential pass AND composite >= 111/138 (~80%).

---

**What the three new criteria capture:**

- **C-30** distinguishes C-28's content requirement from structural demarcation. C-28 requires per-loop absence statements to exist — prose embedded in charter narrative satisfies it (as V-02 R4 demonstrates). C-30 requires those same statements to appear as named, navigable heading sections, making the per-loop absence structure visible in the document outline without reading the full charter. V-01 and V-04 realize C-30 by design: `#### Loop 1 Absence Clause` through `#### Loop 3 Absence Clause` are outline-level sections, not prose arguments. A document that satisfies C-28 by weaving absence clauses into charter body text fails C-30 because the per-loop absence structure is discoverable only to a reader who reads the full charter — it is not architecturally visible.

- **C-31** distinguishes loop-granularity absence (C-28, C-30) from step-granularity absence within Loop 2. C-28 and C-30 operate at the loop transition scale: they require Loop 1, 2, and 3 each to carry an absence clause naming what the next loop cannot do without the previous one. C-31 operates one level down: within Loop 2's extraction sequence, each individual step must carry a named Inertia Gate block that names what that specific step's output cannot be without the step's execution. V-03 realizes C-31 by design: each extraction step is followed by a named gate that applies the definitional register at step resolution ("A compliance obligation unlabeled at extraction time is not a compliance obligation with enforcement scope — it is an unscoped requirement"). The difference is resolution: C-28 makes loop dependencies visible; C-31 makes step dependencies within a loop visible.

- **C-32** distinguishes compliance presence (C-03) from compliance priority encoded in step order. C-03 requires three lenses including compliance to be traceable across the extraction; it is satisfied regardless of step ordering. C-32 requires compliance to be the first extraction step, encoding the charter's enforcement hierarchy structurally in the sequence. V-04 realizes C-32 by design: beginning with the compliance lens means every subsequent extraction step operates on a base of compliance-cleared requirements. The ordering is not incidental — it is a design contract claim that PM and architect requirements are extracted within the scope established by compliance first. A document can satisfy C-03 with compliance as step 3 of 9; C-32 fails unless compliance is step 1.

V-01 at 130/132 under v4 scores **132/138** under v5: V-01 passes C-30 (named `#### Loop N Absence Clause` heading sections) but fails C-31 (no step-level Inertia Gates) and C-32 (no compliance-first ordering). V-02 at 132/132 under v4 scores **132/138** under v5: V-02 passes neither C-30 (per-loop absence in prose, no named sections), C-31, nor C-32. V-03 at 128/132 under v4 scores **130/138** under v5: V-03 passes C-31 (named Inertia Gates at each step) but fails C-28 (no Loop 1 absence clause), C-30, and C-32. V-04 at 132/132 under v4 scores **136/138** under v5: V-04 passes C-30 (named sections) and C-32 (compliance-first) but fails C-31 (no step-level Inertia Gates). V-05 at 132/132 under v4 scores **138/138** under v5: V-05 carries named absence sections (C-30), Inertia Gates at each extraction step (C-31), and compliance-first ordering (C-32). The next variation must replicate all eight new patterns (C-25–C-32) to reach the new ceiling.
