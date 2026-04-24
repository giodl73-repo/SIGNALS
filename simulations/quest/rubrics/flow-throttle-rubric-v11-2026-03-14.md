Written to `simulations/quest/rubrics/flow-throttle-rubric-v11-2026-03-15.md`.

---

## What changed (v10 → v11)

**Two new aspirational criteria, 3 pts each. Max score: 166 → 172.**

### C-33 — Pre-Analysis Inertia Frame
*Source: V-04 "Inertia Framing (Phase 0 Baseline)"*

A structurally distinct Phase 0 section precedes Phase 1 and establishes current-state baseline before analysis begins — naming the construct stack, active limits, and operational conditions before any evaluative claim is made. The term "inertia frame" is precise: Phase 0 captures what-is; Phase 1 analyzes what-fails; the delta between them is the analysis contribution.

No prior criterion touches the pre-Phase-1 position. C-17 through C-32 all govern the barrier/container layer (between Phase 4 and Round 2), not the layer before Phase 1.

**Pass condition:** A numbered or labeled structural section (Phase 0, Baseline Frame, or equivalent) appears before Phase 1 and establishes current-state context. Must be a structurally distinct heading-level section — not an unlabeled preamble within Phase 1. No preconditions.

**R10 retroactive:** V-04 passes; V-01–V-03 fail (no Phase 0 introduced).

---

### C-34 — Phase-Anchor Tabular Encoding
*Source: V-02 "Phase 1 and Phase 4 TABLE retention confirms format selectivity is applied correctly"*

Phase 1 (bottleneck register) and Phase 4 (remediation registry) maintain TABLE format regardless of format variation in Phases 2-3. These are the structural anchor phases: Phase 1 is the machine-scannable entry point; Phase 4 is the cross-referenceable action registry. Tabular encoding here makes each row independently addressable and enables bottleneck-to-remediation traceability. Format variation in Phases 2-3 is format-inert for this criterion.

**Pass condition:** Phase 1 contains at least one TABLE AND Phase 4 contains at least one TABLE, regardless of Phases 2-3 format. No preconditions.

**R10 retroactive:** V-01–V-04 all pass (no variation removes Phase 1 or Phase 4 tabular encoding).

---

**R10 retroactive scores under v11:**

| Variation | C-01..C-32 | C-33 | C-34 | Total / 172 |
|-----------|-----------|------|------|-------------|
| V-01 | 166 | FAIL | PASS | **169** |
| V-02 | 166 | FAIL | PASS | **169** |
| V-03 | 166 | FAIL | PASS | **169** |
| V-04 | 166 | PASS | PASS | **172** |

V-04 sets the R10 ceiling. The C-33/C-34 split matches the R8 pattern (C-29/C-30 required V-03/V-04 to differentiate) — C-34 is inert across all four variations; C-33 discriminates only V-04.
